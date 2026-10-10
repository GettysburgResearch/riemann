#!/usr/bin/env python3
"""Payoff of a hypothetical bilinear saving on the low (reflection) side of the Sep 30 "7/8"
architecture, evaluated in the manuscript's OWN exponent model.  PROPOSED / EXPLORATORY.

Status: PROPOSED model computation.  Arithmetic classes:
  * low side: EXACT_RATIONAL (closed form, Fractions) and the identical float formula;
  * high side with the manuscript's row counts: FLOATING_RECONNAISSANCE (grid sup over bins,
    amplitudes and dyads; the row counts are threshold_calculus.R_bin, exact piecewise-affine);
  * floor-bin barrier: EXACT_RATIONAL LP certificates (barrier_lp rows, low rows shifted by theta).
Source: [OAI] "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", OpenAI, 30 Sep 2026
        (unreviewed; sha256 in SOURCES.txt).  Section/equation numbers refer to that manuscript.
No statement here is about RH.  Nothing here proves any saving; theta is HYPOTHETICAL.

ASSUMPTION B2(theta) -- the ONLY change made to threshold_calculus's model:
  In the exact low separation (eq. (6.x) "low-separated"; TeX label eq:low-separated),
      I = Q^{-1/2} (2 pi)^{-1} sum_sigma int W0^(iv) sum_m Omega(q_m/Q) xi(m) (q_m/Q)^{-iv} A_m(Y') B^J_m(Z) dv,
  Cauchy-Schwarz in m is replaced by a bound that is smaller by a factor Z^{-theta}:
      |sum_m ... A_m B^J_m| << Z^{-theta + eps} (sum_m |A_m|^2)^{1/2} (sum_m |B^J_m|^2)^{1/2},
  with the SAME factor norms (Prop. 15.2 Gram bound; Lemma 15.1 / Lemma 14.5 reflected energy),
  uniformly in the geometry (lx, ly, ell), in every rescaled slot subset J (every d in [0, ell]),
  in the ray class sigma and in the Mellin height v.  Hence theta_low -> theta_low - theta and
      sigma_low(theta) = 1 - lx/2 - h/6 + max_{0<=d<=ell} [sep(d) - d/2] - theta.
  Everything else is the manuscript's stated lemma output, exactly as in threshold_calculus.py:
  row counts of Prop. 19.2 (paper counts), floor bin a0 = 51/100 counted trivially, central contour
  z0 = 17/50, detector t in [1, 3/2], amplification slope 5/6, kappa = max(2 beta* - 1, 3/4)
  (Lemma 18.1 is stated for kappa in [3/4, 1]; this is threshold_calculus's default convention),
  validity ly >= lx (Prop. 15.2 needs P_a >= 1), lx - ell > 0.01, ly - ell > 0.01, and the
  small-row condition h (z0 - 1/6) - ly/2 < 0 (Sec. 20.3).
  A saving measured in the row length, Q^{-theta_Q} with Q = Z^{M'}, corresponds to
  theta = theta_Q * min_d M' (M' = M - 2d >= M - 2 ell); it is NOT modelled separately.

High-side closure without bisection.  For sigma0 <= 7/8 and kappa floor 3/4, every bin has
kappa = max(delta, 3/4) whatever sigma0 is.  Write g(bin) = a + h(z0-1/6) - a ly - ell/2 + x delta ell
+ d (R + delta/2 - z0) (Lemma 10.4, eq. (10.15), with beta* removed).  A bin with a <= sigma0 needs
sigma0 > g; a bin with a > sigma0 has beta* >= a and needs g < a.  So the high side closes at sigma0
iff sigma0 > H(geom) := sup{ g(bin) : g(bin) >= a(bin) }  (sup over the grid; -inf if empty), and
      sigma(theta; geom) = max( sigma_low(geom) - theta, H(geom) ),   sigma(theta) = inf_geom.
This reproduces threshold_calculus.high_sup's sign test exactly (self-test below).

Usage:  python3 bilinear_b2.py            (self-tests, sigma(theta) table, LP barriers)
        python3 bilinear_b2.py --quick    (self-tests and LP barriers only)
        python3 bilinear_b2.py --json OUT (also dump the table as JSON to OUT)
"""
import argparse
import json
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np                      # noqa: E402
import threshold_calculus as tc         # noqa: E402
import barrier_lp as B                  # noqa: E402

THETAS = [Fr(1, 1000), Fr(1, 200), Fr(1, 100), Fr(1, 50), Fr(1, 20)]
PAPER_GEOM = (Fr(17, 48), Fr(23, 48), Fr(1, 6))
COARSE = dict(nde=41, nx=6, nd=5)
FINE = dict(nde=241, nx=26, nd=17)


# ---------------------------------------------------------------------------------------------
# Low side (Lemma 14.5 -> Lemma 15.1, Prop. 15.2, Prop. 15.3, Prop. 15.4); exact closed form
# ---------------------------------------------------------------------------------------------

def _sep_minus(d, lx, ly, ell, energy='paper'):
    """[-(ly-d) + gram + E_B(M-2d, ell-d)]/2 - d/2 ; works for Fractions and floats."""
    M, b = lx + ly, ly - lx
    Mp, lp = M - 2*d, ell - d
    if energy == 'paper':
        EB = max(Mp, (2*Mp + 1 + 3*lp)/4, 2*Mp + lp - 1)
    else:
        EB = max(Mp, 2*Mp + lp - 1)
    gram = max(0*b, b/6, 2*b - (ly - d))
    return (-(ly - d) + gram + EB)/2 - d/2


def low_exact(lx, ly, ell, energy='paper'):
    """sigma_low at theta = 0.  The bracket is a sum of maxima of affine functions of d (convex in d),
    so its max over [0, ell] is attained at d = 0 or d = ell; this is exact for Fractions."""
    h = 1 - lx + ell
    worst = max(_sep_minus(0*ell, lx, ly, ell, energy), _sep_minus(ell, lx, ly, ell, energy))
    return 1 - lx/2 - h/6 + worst


# ---------------------------------------------------------------------------------------------
# High side: H(geom) as described in the module docstring
# ---------------------------------------------------------------------------------------------

def H_high(lx, ly, ell, beta_prev, inp=tc.PAPER, nde=41, nx=6, nd=5):
    assert inp.kappa_floor == 0.75, "closed-form closure assumes the kappa floor 3/4"
    h = 1 - lx + ell
    best, arg = -np.inf, None
    dsel = list(np.linspace(inp.d_sel, h, nd)) if h > inp.d_sel else []
    dgrid = [0.01, min(inp.d_sel, h)] + dsel
    for delta in np.linspace(tc.DELTA0, 2*beta_prev - 1, nde):
        a = (1 + delta)/2
        kappa = max(delta, inp.kappa_floor)
        for x in np.linspace(0, 0.5, nx):
            for d in dgrid:
                R = tc.R_bin(delta, x, d, kappa, ell, inp)
                g = tc.F_high(delta, x, d, lx, ly, ell, 0.0, R, inp.z0)
                if g >= a and g > best:
                    best, arg = g, (round(float(delta), 5), round(float(x), 3), round(float(d), 5), round(float(R), 6))
    small = h*(inp.z0 - 1/6) - ly/2
    return best, arg, small


def sigma_geom(p, theta, beta_prev, inp=tc.PAPER, grid=COARSE):
    lx, ly, ell = (float(t) for t in p)
    if not tc.valid_geometry(lx, ly, ell):
        return 2.0, None
    low = float(low_exact(lx, ly, ell)) - float(theta)
    Hh, arg, small = H_high(lx, ly, ell, beta_prev, inp, **grid)
    if small >= 0:
        return 1.5 + small, ('small-rows',)
    s = max(low, Hh)
    if s > 7/8 + 1e-9:                       # kappa lock (sigma0 <= 7/8) no longer valid; reject
        return 1.0 + s, ('kappa-lock',)
    return s, dict(low=low, high=Hh, arg=arg, binding='low' if low >= Hh else 'high')


def optimise_theta(theta, beta_prev, warm=None, inp=tc.PAPER):
    from scipy.optimize import minimize
    starts = [(17/48, 23/48, 1/6), (0.40, 0.42, 0.17), (0.38, 0.46, 0.15), (0.33, 0.47, 0.20),
              (0.42, 0.44, 0.12)]
    if warm is not None:                     # warm start plus two fixed starts (keeps the run light)
        starts = [tuple(warm), starts[0], starts[1]]
    best = (9.0, None)
    for st in starts:
        r = minimize(lambda p: sigma_geom(p, theta, beta_prev, inp)[0], st, method='Nelder-Mead',
                     options=dict(xatol=1e-6, fatol=1e-8, maxiter=600))
        if r.fun < best[0]:
            best = (r.fun, tuple(float(t) for t in r.x))
    s_fine, info = sigma_geom(best[1], theta, beta_prev, inp, FINE)
    return dict(theta=float(theta), sigma_coarse=best[0], sigma=s_fine, geom=best[1], info=info)


# ---------------------------------------------------------------------------------------------
# Exact LP barriers (any row counts; floor bin only) with the low rows shifted by theta
# ---------------------------------------------------------------------------------------------

def lp_barrier(theta, a0):
    rows = [(c, rhs + theta) for (c, rhs) in B.low_rows()] + [B.floor_row(a0=a0)] + B.validity_rows()
    res = B.solve(rows)
    ok, bound, _ = B.certify(rows, res)
    return ok, bound, tuple(round(float(t), 5) for t in res.x[:3])


# ---------------------------------------------------------------------------------------------

def self_tests():
    out = []
    lx, ly, ell = PAPER_GEOM
    out.append(("low_exact(paper geometry) == 7/8", low_exact(lx, ly, ell) == Fr(7, 8)))
    out.append(("low_exact(Part I) == 11/12", low_exact(Fr(1, 2), Fr(1, 2), Fr(0)) == Fr(11, 12)))
    rng = np.random.default_rng(3)
    worst = 0.0
    for _ in range(200):
        lx_, ell_ = rng.uniform(0.2, 0.5), rng.uniform(0.0, 0.2)
        ly_ = lx_ + rng.uniform(0.0, 0.2)
        worst = max(worst, abs(float(low_exact(lx_, ly_, ell_)) - tc.low_threshold(lx_, ly_, ell_, nd=401)))
    out.append((f"low_exact vs threshold_calculus.low_threshold (200 random, nd=401): max diff {worst:.1e}",
                worst < 1e-12))
    # closure test equals threshold_calculus.high_sup sign test at the paper geometry
    Hh, arg, _ = H_high(17/48, 23/48, 1/6, 11/12, **COARSE)
    hs = tc.high_sup(17/48, 23/48, 1/6, 0.875, 11/12, **COARSE)[0]
    out.append((f"paper geometry: H = {Hh:.7f} (< 7/8) at bin {arg}; high_sup(7/8) = {hs:+.3e}",
                Hh < 0.875 and hs < 0))
    for s0 in (0.870, 0.8745, round(Hh - 1e-6, 7), round(Hh + 1e-6, 7), 0.8749):
        lhs = tc.high_sup(17/48, 23/48, 1/6, s0, 11/12, **COARSE)[0] < 0
        out.append((f"closure equivalence at sigma0 = {s0}: high_sup<0 is {lhs}, sigma0>H is {s0 > Hh}", lhs == (s0 > Hh)))
    ok0, b0, _ = lp_barrier(Fr(0), Fr(1, 2))
    ok1, b1, _ = lp_barrier(Fr(0), Fr(51, 100))
    ok2, b2, _ = lp_barrier(Fr(1, 100), Fr(1, 2))
    out.append((f"LP barrier theta=0: a0=1/2 -> {b0}, a0=51/100 -> {b1}; theta=1/100, a0=1/2 -> {b2}",
                ok0 and ok1 and ok2 and b0 == Fr(13, 15) and b1 == Fr(167, 192) and b2 == Fr(322, 375)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quick', action='store_true')
    ap.add_argument('--json', default=None)
    args = ap.parse_args()

    print("== self-tests ==")
    allok = True
    for msg, ok in self_tests():
        allok &= bool(ok)
        print(("PASS " if ok else "FAIL ") + msg)

    print("\n== exact LP barriers (any row counts; floor bin + low rows shifted by theta) ==")
    lp = {}
    for th in [Fr(0)] + THETAS:
        r = {}
        for a0 in (Fr(51, 100), Fr(1, 2)):
            ok, b, g = lp_barrier(th, a0)
            r[str(a0)] = (str(b), float(b), ok, g)
        lp[str(th)] = r
        print(f"theta={str(th):7s} a0=51/100: {r['51/100'][0]:>12s} = {r['51/100'][1]:.6f} (cert {r['51/100'][2]}) "
              f"| a0=1/2: {r['1/2'][0]:>10s} = {r['1/2'][1]:.6f} (cert {r['1/2'][2]}) geom {r['1/2'][3]}")
    if args.quick:
        return 0 if allok else 1

    print("\n== sigma(theta) in the manuscript's own model (paper counts), beta_prev = 11/12 ==")
    rows, warm = [], None
    r0 = optimise_theta(Fr(0), 11/12)
    warm = r0['geom']
    print(f"theta=0       sigma={r0['sigma']:.6f} geom={tuple(round(t, 5) for t in r0['geom'])} {r0['info']}")
    rows.append(r0)
    for th in THETAS:
        r = optimise_theta(th, 11/12, warm)
        warm = r['geom']
        rows.append(r)
        print(f"theta={str(th):7s} sigma={r['sigma']:.6f} gain={r0['sigma'] - r['sigma']:.6f} "
              f"geom={tuple(round(t, 5) for t in r['geom'])} {r['info']}")

    print("\n== local slope of the gain (no cap is computed: the high side alone has no useful infimum,")
    print("   since H = -inf once no bin binds; what limits sigma(theta) is the trade-off low - theta vs H) ==")
    for r in rows[1:]:
        print(f"theta={r['theta']:.3f}  gain/theta = {(r0['sigma'] - r['sigma'])/r['theta']:.4f}")
    print("\n== check: a priori bound beta_prev = 7/8 (Part II accepted), at the theta=1/20 optimum ==")
    r78 = optimise_theta(THETAS[-1], 7/8, rows[-1]['geom'])
    print(f"theta={THETAS[-1]} beta_prev=7/8: sigma={r78['sigma']:.6f} geom={tuple(round(t, 5) for t in r78['geom'])} {r78['info']}")

    if args.json:
        with open(args.json, 'w') as f:
            json.dump(dict(lp=lp, rows=rows, beta78=r78), f, indent=1, default=str)
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
