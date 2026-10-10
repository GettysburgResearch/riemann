#!/usr/bin/env python3
"""Conditional low-side hypotheses for the Sep 30 "7/8" architecture, priced in the manuscript's
OWN exponent model.  PROPOSED / EXPLORATORY.  No statement here is about RH.

Status: PROPOSED model computation.  Arithmetic classes:
  * low side under each hypothesis: EXACT_RATIONAL closed form (Fractions) and the same float formula;
  * LP barriers (low side + floor bin, ANY row counts): EXACT_RATIONAL.  The LP optimum is
    certified twice: by a rational dual certificate and by an exact primal vertex that is checked
    feasible against every row in Fractions.  Equal values => exact optimum;
  * paper-count model (Prop. 19.2 counts via threshold_calculus / bilinear_b2.H_high):
    FLOATING_RECONNAISSANCE (grid sup over bins, Nelder-Mead over the geometry).
Source: [OAI] "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8", OpenAI,
        30 Sep 2026 (unreviewed; sha256 in SOURCES.txt / CONDITIONAL_B2.md).  Untrusted data.
Imports threshold_calculus, barrier_lp, bilinear_b2 UNCHANGED.  The floor-lowered variant sets
threshold_calculus.DELTA0 at run time (module attribute; the file is not modified).

The hypotheses (exact statements in ../CONDITIONAL_B2.md Sec. 2).  For the rescaled subset with
depth d in [0, ell]: Q = Z^{M'}, M' = M - 2d, Y' = Z^{ly-d}, ell' = ell - d, P_a = Z^b,
E_B = E_B(M', ell') the reflected-energy exponent (THRESHOLD_CALCULUS Sec. 2), and the tuple
bookkeeping "- d/2" of Prop. 15.3 / (5.5).  The low threshold is
    sigma_low = 1 - lx/2 - h/6 + max_{d in {0, ell}} sep(d)      (convex in d: endpoints suffice)
with
    CS (manuscript):  sep = [-(ly-d) + G_paper + E_B]/2 - d/2,  G_paper = max(0, b/6, 2b-ly+d);
    H-dFDH:           G -> G_dFDH  = max(0, b/6)                 (Xi_6 replaces (8354));
    H-biasA:          G -> G_nobias = max(0, 2b-ly+d)            (Gauss-sum bias absent from ||A||^2);
    H-LS (= H-lam, lam=0): G -> 0                                 (sharp sieve over s for the theta row);
    H-lam:            sep = [-(ly-d) - lam (lx-d) + E_B]/2 - d/2  (sum_s|B(chi_s)|^2 << Y'^lam Q^{1-lam}||b||^2);
    H-diag (= H-lam, lam=1): sep = [E_B - M']/2 - d/2.
Uniform-theta mode (bilinear_b2's B2(theta)) is kept only as a cross-check.

Usage:  python3 conditional_b2.py              (self-tests, LP table, paper-count model table)
        python3 conditional_b2.py --quick      (self-tests and LP table only)
        python3 conditional_b2.py --json OUT   (also write the results as JSON)
"""
import argparse
import json
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np                      # noqa: E402
import threshold_calculus as tc         # noqa: E402
import barrier_lp as BL                 # noqa: E402
import bilinear_b2 as B2                # noqa: E402

PAPER_GEOM = (Fr(17, 48), Fr(23, 48), Fr(1, 6))
DELTA0_PAPER = tc.DELTA0                # 1/50, i.e. a0 = 51/100
DELTA0_LOW = 1/1000                     # float proxy for a0 -> 1/2+ in the paper-count model

# name -> (gram option, lam).  lam > 0 bypasses the Gram bound entirely (s-route), so gram is 'none'.
HYPS = {
    'CS':     ('paper',  Fr(0)),
    'dFDH':   ('dfdh',   Fr(0)),
    'biasA':  ('nobias', Fr(0)),
    'LS':     ('none',   Fr(0)),
    'lam1/4': ('none',   Fr(1, 4)),
    'lam1/2': ('none',   Fr(1, 2)),
    'lam3/4': ('none',   Fr(3, 4)),
    'diag':   ('none',   Fr(1)),
}

# ------------------------------------------------------------------------------------------------
# Affine forms in (lx, ly, ell): tuples (c_lx, c_ly, c_ell, c_0) of Fractions
# ------------------------------------------------------------------------------------------------
LX, LY, ELL, ONE = (Fr(1), Fr(0), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0), Fr(0)), \
                   (Fr(0), Fr(0), Fr(1), Fr(0)), (Fr(0), Fr(0), Fr(0), Fr(1))
ZERO = (Fr(0),) * 4


def add(*fs):
    return tuple(sum(f[i] for f in fs) for i in range(4))


def mul(c, f):
    return tuple(Fr(c) * x for x in f)


def ev(f, lx, ly, ell):
    return f[0]*lx + f[1]*ly + f[2]*ell + f[3]


def gram_branches(opt, d):
    b = add(LY, mul(-1, LX))
    third = add(mul(2, b), mul(-1, LY), d)                 # 2b - (ly - d)
    if opt == 'paper':
        return [ZERO, mul(Fr(1, 6), b), third]
    if opt == 'dfdh':
        return [ZERO, mul(Fr(1, 6), b)]
    if opt == 'nobias':
        return [ZERO, third]
    if opt == 'none':
        return [ZERO]
    raise ValueError(opt)


def energy_branches(d):
    Mp = add(LX, LY, mul(-2, d))
    lp = add(ELL, mul(-1, d))
    return [Mp, mul(Fr(1, 4), add(mul(2, Mp), ONE, mul(3, lp))), add(mul(2, Mp), lp, mul(-1, ONE))]


def low_forms(gram, lam, theta=Fr(0), dset=('0', 'ell')):
    """All affine pieces f with sigma_low = max f (exact: max over d in {0, ell}, gram and E branches)."""
    h = add(ONE, mul(-1, LX), ELL)
    base = add(ONE, mul(Fr(-1, 2), LX), mul(Fr(-1, 6), h), mul(-1, mul(theta, ONE)))
    out = []
    for dk in dset:
        d = ZERO if dk == '0' else ELL
        for G in gram_branches(gram, d):
            for E in energy_branches(d):
                sep = add(mul(-1, LY), d, G, E, mul(-lam, add(LX, mul(-1, d))))
                out.append(add(base, mul(Fr(1, 2), sep), mul(Fr(-1, 2), d)))
    return out


def sigma_low(lx, ly, ell, gram='paper', lam=Fr(0), theta=Fr(0)):
    return max(ev(f, lx, ly, ell) for f in low_forms(gram, lam, theta))


# ------------------------------------------------------------------------------------------------
# Exact LP: minimise s subject to s >= every low piece, the floor-bin row, validity rows
# ------------------------------------------------------------------------------------------------

def rows_from_forms(forms):
    # s >= f  <=>  f_lx lx + f_ly ly + f_ell ell - s <= -f_0
    return [([f[0], f[1], f[2], Fr(-1)], -f[3]) for f in forms]


def validity(require_ly_ge_lx=True):
    rows = [([Fr(-1), 0, Fr(1), 0], Fr(0)),            # ell <= lx   (h <= 1)
            ([0, 0, Fr(-1), 0], Fr(0)),                # ell >= 0
            ([0, Fr(-1), Fr(1), 0], Fr(0))]            # ell <= ly   (Y' >= 1 at d = ell)
    if require_ly_ge_lx:
        rows.append(([Fr(1), Fr(-1), 0, 0], Fr(0)))    # lx <= ly    (Prop. 15.2: P_a >= 1)
    return rows


def exact_vertex(rows, x):
    """Solve the tight rows exactly (Fractions) for the vertex; return it if feasible for all rows."""
    import itertools
    slack = [float(r[1]) - sum(float(c)*xi for c, xi in zip(r[0], x)) for r in rows]
    tight = [i for i, s in enumerate(slack) if abs(s) < 1e-7]
    for comb in itertools.combinations(tight, 4):
        A = [[Fr(c) for c in rows[i][0]] for i in comb]
        bvec = [Fr(rows[i][1]) for i in comb]
        sol = _solve4(A, bvec)
        if sol is None:
            continue
        if all(sum(Fr(c)*v for c, v in zip(r[0], sol)) <= r[1] for r in rows):
            return sol
    return None


def _solve4(A, b):
    n = 4
    M = [row[:] + [bi] for row, bi in zip(A, b)]
    for col in range(n):
        piv = next((r for r in range(col, n) if M[r][col] != 0), None)
        if piv is None:
            return None
        M[col], M[piv] = M[piv], M[col]
        for r in range(n):
            if r != col and M[r][col] != 0:
                f = M[r][col] / M[col][col]
                M[r] = [a - f*c for a, c in zip(M[r], M[col])]
    return [M[i][n] / M[i][i] for i in range(n)]


def lp(gram, lam, a0, theta=Fr(0), require_ly_ge_lx=True, dset=('0', 'ell')):
    rows = rows_from_forms(low_forms(gram, lam, theta, dset)) + [BL.floor_row(a0=a0)] + validity(require_ly_ge_lx)
    res = BL.solve(rows)
    if res.status != 0:
        return dict(ok=False, status=res.status)
    ok_d, bound, _ = BL.certify(rows, res)
    vert = exact_vertex(rows, res.x)
    ok_p = vert is not None and (not ok_d or vert[3] == bound)
    val = bound if ok_d else (vert[3] if vert is not None else None)
    tight = []
    if vert is not None:
        lx, ly, ell, s = vert
        tight = [k for k, f in enumerate(low_forms(gram, lam, theta, dset)) if ev(f, lx, ly, ell) == s]
        fl = BL.floor_row(a0=a0)
        floor_tight = sum(c*v for c, v in zip(fl[0], vert)) == fl[1]
    else:
        floor_tight = None
    return dict(ok=bool(ok_d and ok_p), dual_ok=bool(ok_d), primal_ok=bool(ok_p), value=val,
                vertex=None if vert is None else tuple(vert[:3]), low_tight=tight, floor_tight=floor_tight)


# ------------------------------------------------------------------------------------------------
# Paper-count model (FLOATING): sigma = inf_geom max(sigma_low^H, H_high(geom))
# ------------------------------------------------------------------------------------------------

def sigma_geom(p, gram, lam, beta_prev=11/12, grid=B2.COARSE):
    lx, ly, ell = (float(t) for t in p)
    if not tc.valid_geometry(lx, ly, ell):
        return 2.0, None
    low = float(sigma_low(Fr(lx), Fr(ly), Fr(ell), gram, lam))
    Hh, arg, small = B2.H_high(lx, ly, ell, beta_prev, tc.PAPER, **grid)
    if small >= 0:
        return 1.5 + small, ('small-rows',)
    s = max(low, Hh)
    if s > 7/8 + 1e-9:
        return 1.0 + s, ('kappa-lock',)
    return s, dict(low=low, high=float(Hh), arg=arg, binding='low' if low >= Hh else 'high')


def optimise(gram, lam, starts, beta_prev=11/12):
    from scipy.optimize import minimize
    best = (9.0, None)
    for st in starts:
        r = minimize(lambda p: sigma_geom(p, gram, lam, beta_prev)[0], st, method='Nelder-Mead',
                     options=dict(xatol=1e-6, fatol=1e-8, maxiter=500))
        if r.fun < best[0]:
            best = (float(r.fun), tuple(float(t) for t in r.x))
    s_fine, info = sigma_geom(best[1], gram, lam, beta_prev, B2.FINE)
    return dict(sigma_coarse=best[0], sigma=float(s_fine), geom=best[1], info=info)


STARTS = [(17/48, 23/48, 1/6), (0.36, 0.475, 0.167), (0.40, 0.42, 0.17), (0.42, 0.46, 0.12),
          (0.45, 0.48, 0.08), (0.48, 0.50, 0.03), (0.38, 0.50, 0.14)]


# ------------------------------------------------------------------------------------------------

def self_tests():
    out = []
    lx, ly, ell = PAPER_GEOM
    s_cs = sigma_low(lx, ly, ell, 'paper', Fr(0))
    out.append((f"CS low at paper geometry = {s_cs} (expect 7/8)", s_cs == Fr(7, 8)))
    s_p1 = sigma_low(Fr(1, 2), Fr(1, 2), Fr(0), 'paper', Fr(0))
    out.append((f"CS low at Part I geometry = {s_p1} (expect 11/12)", s_p1 == Fr(11, 12)))
    rng = np.random.default_rng(5)
    worst = Fr(0)
    for _ in range(300):
        g = (Fr(rng.uniform(0.2, 0.5)).limit_denominator(10**5),)
        lx_ = g[0]
        ell_ = Fr(rng.uniform(0.0, float(lx_) - 0.01)).limit_denominator(10**5)
        ly_ = lx_ + Fr(rng.uniform(0.0, 0.2)).limit_denominator(10**5)
        worst = max(worst, abs(sigma_low(lx_, ly_, ell_, 'paper') - B2.low_exact(lx_, ly_, ell_)))
    out.append((f"CS low == bilinear_b2.low_exact on 300 random rational geometries (max diff {worst})", worst == 0))
    # H-diag at the paper geometry: theta_low = 0, sigma_low = 1 - lx/2 - h/6 = 11/16
    s_d = sigma_low(lx, ly, ell, 'none', Fr(1))
    out.append((f"H-diag low at paper geometry = {s_d} (expect 11/16)", s_d == Fr(11, 16)))
    # H-LS / H-dFDH at the paper geometry: 7/8 - b/12 and 7/8
    out.append((f"H-LS low at paper geometry = {sigma_low(lx, ly, ell, 'none', Fr(0))} (expect 7/8 - 1/96 = 83/96)",
                sigma_low(lx, ly, ell, 'none', Fr(0)) == Fr(83, 96)))
    out.append((f"H-dFDH low at paper geometry = {sigma_low(lx, ly, ell, 'dfdh', Fr(0))} (expect 7/8)",
                sigma_low(lx, ly, ell, 'dfdh', Fr(0)) == Fr(7, 8)))
    # my d = 0, gram = b/6 rows reproduce barrier_lp.low_rows() exactly
    mine = rows_from_forms(low_forms('dfdh', Fr(0), dset=('0',)))
    want = BL.low_rows()
    mine_b6 = [r for r in mine if r in want]
    out.append((f"d=0, gram=b/6 rows contain barrier_lp.low_rows() ({len(mine_b6)}/3)", len(mine_b6) == 3))
    # relaxed LP (d = 0, gram >= b/6) reproduces bilinear_b2.lp_barrier for uniform theta
    for th, a0 in [(Fr(0), Fr(51, 100)), (Fr(0), Fr(1, 2)), (Fr(1, 100), Fr(1, 2)), (Fr(1, 20), Fr(51, 100))]:
        relaxed =[(c, rhs + th) for (c, rhs) in BL.low_rows()] + [BL.floor_row(a0=a0)] + BL.validity_rows()
        res = BL.solve(relaxed)
        ok, bnd, _ = BL.certify(relaxed, res)
        ok2, bnd2, _ = B2.lp_barrier(th, a0)
        out.append((f"uniform theta={th}, a0={a0}: relaxed LP {bnd} == bilinear_b2.lp_barrier {bnd2}", ok and ok2 and bnd == bnd2))
    # full LP (all d, all gram branches) at theta = 0 equals the relaxed barriers 167/192 and 13/15
    r1 = lp('paper', Fr(0), Fr(51, 100))
    r2 = lp('paper', Fr(0), Fr(1, 2))
    out.append((f"full CS LP: a0=51/100 -> {r1['value']}, a0=1/2 -> {r2['value']} (expect 167/192, 13/15)",
                r1['ok'] and r2['ok'] and r1['value'] == Fr(167, 192) and r2['value'] == Fr(13, 15)))
    # convexity in d: endpoint max equals a fine d-grid max (float) for each hypothesis
    worst = 0.0
    for _ in range(100):
        lx_, ell_ = rng.uniform(0.25, 0.5), rng.uniform(0.0, 0.2)
        ly_ = lx_ + rng.uniform(0.0, 0.15)
        for name, (gram, lam) in HYPS.items():
            M, b, h = lx_ + ly_, ly_ - lx_, 1 - lx_ + ell_
            grid = []
            for d in np.linspace(0, ell_, 401):
                Mp, lp_ = M - 2*d, ell_ - d
                E = max(Mp, (2*Mp + 1 + 3*lp_)/4, 2*Mp + lp_ - 1)
                G = {'paper': max(0, b/6, 2*b - ly_ + d), 'dfdh': max(0, b/6),
                     'nobias': max(0, 2*b - ly_ + d), 'none': 0.0}[gram]
                grid.append((-(ly_ - d) + G + E - float(lam)*(lx_ - d))/2 - d/2)
            direct = 1 - lx_/2 - h/6 + max(grid)
            worst = max(worst, abs(direct - float(sigma_low(Fr(lx_), Fr(ly_), Fr(ell_), gram, lam))))
    out.append((f"endpoint formula == 401-point d-grid for all hypotheses (max diff {worst:.1e})", worst < 1e-12))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quick', action='store_true')
    ap.add_argument('--json', default=None)
    args = ap.parse_args()
    allok = True
    print("== self-tests ==")
    for msg, ok in self_tests():
        allok &= bool(ok)
        print(("PASS " if ok else "FAIL ") + msg)

    print("\n== exact LP: low side under each hypothesis + floor-bin row (ANY row counts) ==")
    lpres = {}
    for name, (gram, lam) in HYPS.items():
        r = {}
        for a0 in (Fr(51, 100), Fr(1, 2)):
            for req in (True, False):
                x = lp(gram, lam, a0, require_ly_ge_lx=req)
                r[f"{a0}|ly>=lx={req}"] = x
                allok &= bool(x['ok'])
        lpres[name] = r
        for a0 in ('51/100', '1/2'):
            x = r[f"{a0}|ly>=lx=True"]
            y = r[f"{a0}|ly>=lx=False"]
            v = x['value']
            print(f"{name:7s} a0={a0:6s}: {str(v):>14s} = {float(v):.6f} cert={x['ok']} vertex={tuple(str(t) for t in x['vertex'])} "
                  f"floor_tight={x['floor_tight']} | without ly>=lx: {y['value']} ({float(y['value']):.6f})")
    # low side alone (no floor): the low barrier of each hypothesis
    print("\n== exact LP: low side alone (no floor row) ==")
    low_alone = {}
    for name, (gram, lam) in HYPS.items():
        rows = rows_from_forms(low_forms(gram, lam)) + validity(True)
        res = BL.solve(rows)
        ok, bnd, _ = BL.certify(rows, res)
        vert = exact_vertex(rows, res.x)
        low_alone[name] = dict(ok=bool(ok and vert is not None and vert[3] == bnd), value=bnd,
                               vertex=None if vert is None else tuple(vert[:3]))
        allok &= low_alone[name]['ok']
        print(f"{name:7s}: {bnd} = {float(bnd):.6f} cert={low_alone[name]['ok']} at {tuple(str(t) for t in vert[:3]) if vert else None}")
    if args.quick:
        return 0 if allok else 1

    print("\n== paper-count model (FLOATING): inf_geom max(sigma_low^H, H_high), beta_prev = 11/12 ==")
    model = {}
    for d0, tag in ((DELTA0_PAPER, 'a0=51/100'), (DELTA0_LOW, 'a0=1/2+1/2000')):
        tc.DELTA0 = d0
        for name in ('CS', 'dFDH', 'biasA', 'LS', 'lam1/4', 'lam1/2', 'lam3/4', 'diag'):
            gram, lam = HYPS[name]
            starts = list(STARTS)
            v = lpres[name][('51/100' if d0 == DELTA0_PAPER else '1/2') + '|ly>=lx=True']['vertex']
            if v is not None:
                vf = tuple(float(t) for t in v)
                if tc.valid_geometry(*vf):
                    starts.append(vf)
            r = optimise(gram, lam, starts)
            g = r['geom']
            r['low_CS_at_geom'] = float(sigma_low(Fr(g[0]), Fr(g[1]), Fr(g[2]), 'paper', Fr(0)))
            r['theta_eff'] = r['low_CS_at_geom'] - (r['info']['low'] if isinstance(r['info'], dict) else float('nan'))
            model[f"{name}|{tag}"] = r
            print(f"{tag:14s} {name:7s} sigma={r['sigma']:.6f} (coarse {r['sigma_coarse']:.6f}) "
                  f"geom={tuple(round(t, 5) for t in g)} theta_eff={r['theta_eff']:.5f} info={r['info']}")
    tc.DELTA0 = DELTA0_PAPER

    if args.json:
        def enc(o):
            if isinstance(o, Fr):
                return str(o)
            if isinstance(o, (np.floating,)):
                return float(o)
            return str(o)
        with open(args.json, 'w') as f:
            json.dump(dict(lp=lpres, low_alone=low_alone, model=model), f, indent=1, default=enc)
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
