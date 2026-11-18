"""Spectral-side cross-check of the window ground state (zeros side vs arithmetic side).

For L in {0.6, 0.8}: assemble the high-precision arithmetic-side matrix (hp_core), take the
even-sector ground state v (inverse iteration), and evaluate on the zeros side
    S(Gamma) = sum_{0 < gamma <= Gamma} 2 |h_v(gamma)|^2,   h_v(r) = sum_j v_j i^j sqrt(2L(2j+1)) j_j(L r),
using the Arb-certified ordinates (midpoints) and mpmath spherical Bessel functions at 50 digits.
Under RH (verified to height 3e12) S(Gamma) increases to the Rayleigh quotient lambda as Gamma -> inf;
the comparison tests the arithmetic-side assembly at the level of the tiny eigenvalue itself.
Also reports |v(+-L)| (endpoint values; they control the 1/r tail of h_v).
"""
import os, sys, json, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, "/home/user/riemann/research/exploratory/riemann-observatory/experiments/code/C1-detection-horizons")
import mpmath as mp
from flint import arb, ctx
from hp_core import HPWeil, legendre_vals
from exp_lambda_profile import block, lam_min_block
from common import load_zeros

RES = "/home/user/riemann/research/exploratory/riemann-observatory/experiments/results/C4-weil-window-locality"


def main():
    g, rad = load_zeros(as_str=False)
    _, _, gs = load_zeros(as_str=True)
    out = []
    for L, N, prec, Gmax in [(0.6, 48, 300, 3000.0), (0.8, 72, 350, 3000.0)]:
        t0 = time.time()
        ctx.prec = prec
        H = HPWeil(L, N, prec=prec)
        W = H.matrix(S=max(200, 2 * N + 120))
        ev = list(range(0, N, 2))
        lam, x = lam_min_block(block(W, ev))
        mp.mp.dps = 60
        v = [mp.mpf(x[i, 0].mid().str(70, radius=False)) for i in range(len(ev))]
        Lm = mp.mpf(L)
        # endpoint value v(L) = sum_j v_j phi_j(L), phi_j(L) = sqrt((2j+1)/(2L))
        vL = sum(v[i] * mp.sqrt((2 * j + 1) / (2 * Lm)) for i, j in enumerate(ev))
        coef = [v[i] * (1 if (j // 2) % 2 == 0 else -1) * mp.sqrt(2 * Lm * (2 * j + 1)) for i, j in enumerate(ev)]
        partial, checkpoints = mp.mpf(0), []
        marks = [100, 300, 1000, 3000]
        k = 0
        for idx, gam in enumerate(g):
            if gam > Gmax:
                break
            z = Lm * mp.mpf(gs[idx])
            # spherical Bessel j_n(z) = sqrt(pi/(2z)) J_{n+1/2}(z)
            pref = mp.sqrt(mp.pi / (2 * z))
            h = mp.fsum(coef[i] * pref * mp.besselj(j + mp.mpf(0.5), z) for i, j in enumerate(ev))
            partial += 2 * h * h
            while k < len(marks) and (idx + 1 == len(g) or g[idx + 1] > marks[k]):
                checkpoints.append([marks[k], mp.nstr(partial, 12)])
                k += 1
        rec = {"L": L, "N": N, "prec_bits": prec, "lambda_arith": lam.str(15, radius=False),
               "zeros_side_partial_sums": checkpoints, "v_at_L": mp.nstr(vL, 6), "seconds": round(time.time() - t0, 1)}
        out.append(rec)
        print(json.dumps(rec), flush=True)
    path = os.path.join(RES, "hp_spectral_check.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", path, hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
