#!/usr/bin/env python3
import argparse
import json
import math
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 70


def catalan(n: int) -> int:
    return math.comb(2*n, n) // (n+1)


def F(w):
    return 1 / (2 * (1 + mp.sqrt(1-w))**2)


def c_exact(k: int) -> Fraction:
    return Fraction(catalan(k+1), 8 * (4**k))


def beta_cell(k: int, m: int):
    return mp.beta(k + mp.mpf("1.5"), m + mp.mpf("1.5")) / mp.pi


def stieltjes_integral(w):
    return mp.quad(lambda lam: mp.sqrt(lam*(1-lam)) / (mp.pi*(1-w*lam)), [0, 1])


def pick_matrix(nodes):
    n = len(nodes)
    M = mp.matrix(n)
    for i, z in enumerate(nodes):
        for j, w in enumerate(nodes):
            if i == j:
                M[i,j] = mp.diff(F, z)
            else:
                M[i,j] = (F(z)-F(w)) / (z-w)
    return M


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", required=True)
    args = ap.parse_args()

    catalan_rows = []
    max_catalan_error = mp.mpf("0")
    for k in range(21):
        numeric = mp.diff(F, 0, k) / mp.factorial(k)
        exact = mp.mpf(c_exact(k).numerator) / c_exact(k).denominator
        err = abs(numeric-exact)
        max_catalan_error = max(max_catalan_error, err)
        catalan_rows.append({
            "k": k,
            "numerator": c_exact(k).numerator,
            "denominator": c_exact(k).denominator,
            "numeric_error": float(err),
        })

    stieltjes_rows = []
    max_stieltjes_error = mp.mpf("0")
    for w in [mp.mpf("0"), mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf("0.9")]:
        val = F(w)
        integ = stieltjes_integral(w)
        err = abs(val-integ)
        max_stieltjes_error = max(max_stieltjes_error, err)
        stieltjes_rows.append({
            "w": float(w),
            "closed": float(val),
            "integral": float(integ),
            "absolute_error": float(err),
        })

    beta_rows = []
    max_beta_error = mp.mpf("0")
    for k,m in [(0,0),(3,0),(2,2),(7,3),(20,4)]:
        fd = Fraction(0)
        for j in range(m+1):
            fd += ((-1)**j)*math.comb(m,j)*c_exact(k+j)
        fdm = mp.mpf(fd.numerator)/fd.denominator
        b = beta_cell(k,m)
        err = abs(fdm-b)
        max_beta_error=max(max_beta_error,err)
        beta_rows.append({
            "k":k,"m":m,
            "finite_difference":float(fdm),
            "beta_cell":float(b),
            "absolute_error":float(err),
        })

    nodes = [
        mp.mpf("-0.35"),
        mp.mpf("-0.05"),
        mp.mpf("0.22"),
        mp.mpf("0.55"),
    ]
    P = pick_matrix(nodes)
    eigvals = list(mp.eigsy(P, eigvals_only=True))
    pick_min = min(eigvals)

    algebra_rows=[]
    max_algebra_error=mp.mpf("0")
    for w in [mp.mpf("0.05"),mp.mpf("0.3"),mp.mpf("0.6"),mp.mpf("0.74")]:
        r=mp.sqrt(1-w)
        left=(2-w-2*r)/(w*w)
        right=1/(1+r)**2
        err=abs(left-right)
        max_algebra_error=max(max_algebra_error,err)
        algebra_rows.append({"w":float(w),"absolute_error":float(err)})

    boundary_rows=[]
    max_radius_ratio=mp.mpf("0")
    max_delta_ratio=mp.mpf("0")
    for k in [16,32,64,128,256]:
        R=mp.mpf("0.75")-1/mp.mpf(k+4)
        delta=mp.sqrt(1-R)-mp.mpf("0.5")
        radius_ratio=(R**(-k))/((mp.mpf(4)/3)**k)
        delta_ratio=(1/delta)/(k+4)
        max_radius_ratio=max(max_radius_ratio,radius_ratio)
        max_delta_ratio=max(max_delta_ratio,delta_ratio)
        boundary_rows.append({
            "k":k,
            "R":float(R),
            "delta":float(delta),
            "radius_ratio":float(radius_ratio),
            "delta_inverse_over_kplus4":float(delta_ratio),
        })

    critical = 1/mp.log(mp.mpf(4)/3)
    threshold_rows=[]
    for log_carrier in [mp.mpf("50"),mp.mpf("100"),mp.mpf("200"),mp.mpf("500")]:
        k=1
        while (k+1)*mp.log(mp.mpf(4)/3)+mp.mpf("2.5")*mp.log(k+1) <= log_carrier:
            k+=1
        threshold_rows.append({
            "log_ell":float(log_carrier),
            "max_k":k,
            "k_over_log_ell":float(mp.mpf(k)/log_carrier),
        })

    crossover_rows=[]
    for y in [mp.mpf("0.2"),mp.mpf("0.4"),mp.mpf("0.49")]:
        wy=1-y*y
        for logell in [mp.mpf("20"),mp.mpf("50"),mp.mpf("100")]:
            ell=mp.e**logell
            k=1
            while True:
                gamma=ell*(mp.mpf(c_exact(k).numerator)/c_exact(k).denominator)
                pair=4*y*y*wy**(-k-3)
                if pair>=gamma:
                    break
                k+=1
                if k>10000:
                    raise RuntimeError("crossover not found")
            predicted=logell/mp.log(1/wy)
            crossover_rows.append({
                "depth":float(y),
                "log_ell":float(logell),
                "first_pair_dominant_k":k,
                "leading_prediction":float(predicted),
                "ratio":float(mp.mpf(k)/predicted),
            })

    gates={
        "gamma_algebra": max_algebra_error < mp.mpf("1e-60"),
        "catalan_coefficients": max_catalan_error < mp.mpf("1e-50"),
        "stieltjes_integral": max_stieltjes_error < mp.mpf("1e-45"),
        "beta_finite_differences": max_beta_error < mp.mpf("1e-50"),
        "strict_pick_matrix": pick_min > mp.mpf("1e-8"),
        "cauchy_boundary_scaling": max_radius_ratio < 5 and max_delta_ratio < 2,
        "critical_constant": abs(critical-mp.mpf("3.476059496782206910376499401645766")) < mp.mpf("1e-30"),
    }
    if not all(gates.values()):
        raise AssertionError(gates)

    result={
        "status":"PASS_GAMMA_CATALAN_SAFE_DISC",
        "gates":gates,
        "gamma_algebra":{"rows":algebra_rows,"max_error":float(max_algebra_error)},
        "catalan":{"rows":catalan_rows,"max_error":float(max_catalan_error)},
        "stieltjes":{"rows":stieltjes_rows,"max_error":float(max_stieltjes_error)},
        "beta_cells":{"rows":beta_rows,"max_error":float(max_beta_error)},
        "pick_matrix":{
            "nodes":[float(z) for z in nodes],
            "eigenvalues":[float(mp.re(v)) for v in eigvals],
            "minimum_eigenvalue":float(pick_min),
        },
        "cauchy_boundary":{
            "rows":boundary_rows,
            "max_radius_ratio":float(max_radius_ratio),
            "max_delta_inverse_over_kplus4":float(max_delta_ratio),
        },
        "critical_order":{
            "one_over_log_four_thirds":float(critical),
            "threshold_rows":threshold_rows,
        },
        "synthetic_pair_crossover":crossover_rows,
    }

    with open(args.json,"w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,sort_keys=True)
        f.write("\n")
    print(result["status"])


if __name__ == "__main__":
    main()
