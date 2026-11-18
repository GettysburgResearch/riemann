#!/usr/bin/env python3
"""C3-failure-anatomy: Arb (python-flint) replay of the Conrey-Li (IMRN 2000; arXiv math/9812166)
witnesses against de Branges' positivity conditions, plus a scan over the first K zeros.

Normalisations exactly as in Conrey-Li Sec. 3 and their Mathematica appendix:
  xi(s)   = s (s-1) pi^{-s/2} Gamma(s/2) zeta(s)
  xi4(s)  = (4 pi)^{-s/2} Gamma((s+1)/2) (zeta(s,1/4) - zeta(s,3/4))   [= (4/pi)^{s/2} Gamma((s+1)/2) L(s,chi_4)]
Conrey-Li Theorem 1 (de Branges): if Re<F(z),F(z+i)>_{H(E)} >= 0 for all admissible F, then
  Re{ conj(E)'(w) E(w+i) / (2 pi i) } >= 0 at every zero w of E, where E(z) = xi(1 - i z).
With rho = 1 - i w this is  -Re{ xi'(rho) xi(1+rho) } >= 0  (C-L eq. (3.2)); C-L exhibit rho_34 where it is < 0.
Conrey-Li Theorem 2 condition for F(W), W = 1/xi(1-iz): Re{ xi(1+it)/xi(2+it) } >= 0 for all real t
  (C-L eq. (3.4): t = 282 gives a negative value).
Every reported sign is certified by Arb balls (the ball for the zero contains the true zero; the
quantity is evaluated on that ball, so its true value lies in the output ball).

Usage: python3 conrey_li_debranges.py K outjson [ZEROS_TSV[,ZEROS_TSV2]]
"""
import sys, json, time, platform
import flint
from flint import acb, arb, acb_series, ctx

ctx.prec = 192
PI = arb.pi()


def xi_series(s0, n=2):
    s = acb_series([s0, 1], prec=n)
    return s * (s - 1) * (-(s / 2) * acb(PI).log()).exp() * acb_series.gamma(s / 2) * acb_series.zeta(s)


def xi(s0):
    return s0 * (s0 - 1) * (-(s0 / 2) * acb(PI).log()).exp() * (s0 / 2).gamma() * s0.zeta()


def xi4_series(s0, n=2):
    s = acb_series([s0, 1], prec=n)
    h = acb_series.zeta(s, acb(1) / 4) - acb_series.zeta(s, acb(3) / 4)
    return (-(s / 2) * (4 * acb(PI)).log()).exp() * acb_series.gamma((s + 1) / 2) * h


def xi4(s0):
    h = s0.zeta(acb(1) / 4) - s0.zeta(acb(3) / 4)
    return (-(s0 / 2) * (4 * acb(PI)).log()).exp() * ((s0 + 1) / 2).gamma() * h


def krawczyk(F, Fp_ball, m, r):
    """Krawczyk test on the complex box B = m +/- r (real and imag radius r).
    F(m) evaluated at the (exact) midpoint; Fp_ball(B) encloses F' on B.
    Returns (ok, K)."""
    B = acb(arb(m.real.mid(), r), arb(m.imag.mid(), r))
    mm = acb(m.real.mid(), m.imag.mid())
    fm = F(mm)
    dm = Fp_ball(mm)
    dB = Fp_ball(B)
    Y = 1 / acb(dm.real.mid(), dm.imag.mid())
    K = mm - Y * fm + (1 - Y * dB) * (B - mm)
    return B.contains(K) and (K.real.rad() < r) and (K.imag.rad() < r), K


def sign_of(x):
    if x > 0:
        return "+"
    if x < 0:
        return "-"
    return "undetermined"


def main():
    K = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    out = sys.argv[2] if len(sys.argv) > 2 else None
    t0 = time.time()
    res = {"versions": {"python": platform.python_version(), "python_flint": flint.__version__},
           "prec_bits": ctx.prec, "K": K}
    # --- witness (3.2): 34th zero of zeta
    rho34 = acb.zeta_zeros(34, 1)[0]
    d = xi_series(rho34, 2).coeffs()
    q = -(d[1] * xi(1 + rho34)).real
    res["CL_3.2"] = {"rho34": str(rho34), "-Re{xi'(rho)xi(1+rho)}": str(q), "sign": sign_of(q),
                     "conrey_li_value": "-5.389100507182945e-69"}
    # --- witness (3.4)
    v = (xi(acb(1, 282)) / xi(acb(2, 282))).real
    res["CL_3.4"] = {"Re{xi(1+282i)/xi(2+282i)}": str(v), "sign": sign_of(v),
                     "conrey_li_value": "-0.000131957"}
    # --- chi_4 witnesses: certify the zero near 1/2 + 67.63692086354606839805 i
    m = acb("0.5", "67.6369208635460683980549")
    F = lambda s: xi4(s)
    Fp = lambda s: xi4_series(s, 2).coeffs()[1]
    # refine by a few Newton steps at midpoint precision
    for _ in range(4):
        mm = acb(m.real.mid(), m.imag.mid())
        m = mm - F(mm) / Fp(mm)
        m = acb(m.real.mid(), m.imag.mid())
    ok, Kbox = krawczyk(F, Fp, m, arb("1e-30"))
    rho4 = Kbox
    d4 = Fp(rho4)
    q4 = -(d4 * xi4(1 + rho4)).real
    res["CL_chi4_zero"] = {"krawczyk_ok": bool(ok), "zero_ball": str(rho4),
                           "re_minus_half_contains_0": bool((rho4.real - arb("0.5")).contains(0))}
    res["CL_chi4_3.7"] = {"-Re{xi4'(rho)xi4(1+rho)}": str(q4), "sign": sign_of(q4),
                          "conrey_li_value": "-2.310349004993483456e-45"}
    v4 = (xi4(acb(1, "8714.2")) / xi4(acb(2, "8714.2"))).real
    res["CL_chi4_3.8"] = {"Re{xi4(1+8714.2i)/xi4(2+8714.2i)}": str(v4), "sign": sign_of(v4),
                          "conrey_li_value": "-0.000422340607"}
    # --- scan: sign of -Re{xi'(rho)xi(1+rho)} for the first K zeros
    if len(sys.argv) > 3:
        # certified ordinates (n, midpoint, radius) from TSV files produced by zeros_arb.py (Arb zeta_zeros)
        zs = []
        for path in sys.argv[3].split(","):
            for line in open(path):
                parts = line.split()
                if len(parts) >= 3 and len(zs) < K:
                    assert int(parts[0]) == len(zs) + 1
                    zs.append(acb(arb("0.5"), arb(parts[1], parts[2])))
        res["zeros_source"] = sys.argv[3]
    else:
        zs = acb.zeta_zeros(1, K)
        res["zeros_source"] = "flint.acb.zeta_zeros"
    neg = []; pos = 0; und = []
    for n, rho in enumerate(zs, start=1):
        dd = xi_series(rho, 2).coeffs()[1]
        qq = -(dd * xi(1 + rho)).real
        sg = sign_of(qq)
        if sg == "-":
            neg.append(n)
        elif sg == "+":
            pos += 1
        else:
            und.append(n)
    res["scan"] = {"K": K, "num_negative": len(neg), "num_positive": pos, "num_undetermined": len(und),
                   "first_negative_indices": neg[:60], "undetermined_indices": und[:20],
                   "note": "negative = de Branges necessary condition (C-L Thm 1) violated at that zero"}
    # --- scan of Theorem-2 quantity on a t-grid (sign changes of Re{xi(1+it)/xi(2+it)})
    grid_neg = []
    t = 1.0
    while t <= 1000.0:
        val = (xi(acb(1, t)) / xi(acb(2, t))).real
        if val < 0:
            grid_neg.append(round(t, 2))
        t += 0.25
    res["thm2_grid"] = {"t_range": [1, 1000], "step": 0.25, "num_negative_gridpoints": len(grid_neg),
                        "first_negative_t": grid_neg[:20]}
    res["runtime_s"] = time.time() - t0
    s = json.dumps(res, indent=1)
    print(s)
    if out:
        open(out, "w").write(s + "\n")


if __name__ == "__main__":
    main()
