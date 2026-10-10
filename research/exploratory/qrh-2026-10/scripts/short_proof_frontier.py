#!/usr/bin/env python3
"""Short-proof frontier: the Part II (prime-slot) architecture with row counts taken ONLY from
classical, published-type zero-density theorems for the full family of Hecke characters of
Q(sqrt(-3)) (Kintali-style), instead of the manuscript's Sec. 8.2 / 9 / 17-19 machinery.

Status: EXPLORATORY (PROPOSED model analysis).  Exact rational LP certificates for the linear
barrier statements; FLOATING_RECONNAISSANCE Nelder-Mead runs of the full threshold_calculus model.
Sources: [OAI] "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026,
sha256 in SOURCES.txt), Prop. 9.2 (eq. sextic-row-count), Lemma 8.1 (buffered bins), Lemma 20.1
(eq. common-high-exponent); [K] Kintali (7 Oct 2026) eq. (16), Lemma 2; [Hinz] Acta Arith. 31
(1976) Satz A, Satz B (statements as recorded in ../reviews/KINTALI_REVIEW.md Sec. 1.2).

Dictionary (see SHORT_PROOF_FRONTIER.md Sec. 1).  threshold_calculus's row-count exponent R is
    #{rows u : q_u ~ U = Z^d, u in bin (i,a)}  <<  U^{R + eps} (1 + T_1)^{A_A},     delta = 2a - 1,
exactly the input of [OAI] Lemma 20.1 and Prop. 9.2, and exactly [K]'s R(a) in (16).  Each row in
a non-floor bin owns a zero rho, Re rho >= a, of a primitive finite-order Hecke character of
conductor norm << U, and each character is hit by O(1) rows ([K] Lemma 2).  A full-family density
theorem  sum_{Nq<=Q} sum_chi N(sigma,T,chi) << (Q^2 T^2)^{A(sigma)(1-sigma)+eps}  with Q ~ U gives
    R_A(delta) = min(1, 2 A(a) (1 - a)) = min(1, A (1 - delta))   (constant A).
So threshold_calculus's counts='DH' (R = 1 - delta) is A = 1 in this normalisation (density
hypothesis for the ROW family of ~U members), whereas DH for the full Hecke family is A = 2.

Usage (from any directory; -I is fine because the script adds its own directory to sys.path):
    python3 -I short_proof_frontier.py lp              exact LP table + certificates (seconds)
    python3 -I short_proof_frontier.py check           full model at the LP optima (fine grid)
    python3 -I short_proof_frontier.py run NAME        one Nelder-Mead scenario -> ../results/SPF_NAME.json
    python3 -I short_proof_frontier.py list            list scenario names
Nothing in the existing scripts is modified on disk; threshold_calculus.R_bin is wrapped at runtime
(the wrapper falls through to the original for every counts mode it does not own).
"""
import json
import os
import sys
import time
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import numpy as np                      # noqa: E402
import threshold_calculus as tc         # noqa: E402
import barrier_lp as B                  # noqa: E402

# ------------------------------------------------------------------------------------------------
# Density exponents A(sigma):  N(sigma, T, family of conductor <= Q) << (Q^2 T^2)^{A(sigma)(1-sigma)}
# ------------------------------------------------------------------------------------------------

def A_const(A):
    return lambda sigma: A


def A_hinz(sigma):
    """Hinz 1976, n = 2: Satz A (3/(2-sigma), all 1/2 <= sigma <= 1) and Satz B (2/sigma, sigma >= 3/4).
    = min(3/(2-sigma), 2/sigma) on [3/4,1]: the form of [K ref 4, Lemma 3.3]; max 5/2 at sigma = 4/5."""
    v = 3/(2 - sigma)
    if sigma >= 0.75:
        v = min(v, 2/sigma)
    return v


def A_hinz_exact_fr(a):
    """same, in exact rationals (for LP rows)."""
    v = Fr(3)/(2 - a)
    if a >= Fr(3, 4):
        v = min(v, Fr(2)/a)
    return v


def A_huxley_sigma(sigma):
    """HYPOTHETICAL for this family: Ingham-Montgomery 3/(2-sigma) for sigma <= 3/4 and Huxley's
    3/(3 sigma - 1) for sigma >= 3/4 (the shape of Huxley's Dirichlet-family theorem; max 12/5 at 3/4).
    Not located as a published theorem for Hecke characters of Q(sqrt(-3)) in the conductor aspect."""
    return 3/(2 - sigma) if sigma <= 0.75 else 3/(3*sigma - 1)


def A_huxley_sigma_fr(a):
    return Fr(3)/(2 - a) if a <= Fr(3, 4) else Fr(3)/(3*a - 1)


def R_density(delta, Afun):
    a = (1 + delta)/2
    return min(1.0, 2*Afun(a)*(1 - a))


def crossing(Afun, lo=0.5, hi=1.0):
    """a* = inf{a : 2 A(a)(1-a) <= 1}: rows with rightmost zero left of a* are counted trivially."""
    f = lambda a: 2*Afun(a)*(1 - a) - 1
    if f(lo) <= 0:
        return lo
    for _ in range(200):
        m = (lo + hi)/2
        if f(m) > 0:
            lo = m
        else:
            hi = m
    return hi

# ------------------------------------------------------------------------------------------------
# Wrapping threshold_calculus (runtime only; files untouched)
# ------------------------------------------------------------------------------------------------

class DensityInputs(tc.Inputs):
    """threshold_calculus.Inputs with counts taken from a full-family density exponent A(sigma).
    Every other lemma constant (energy, z0, ...) is the manuscript's unless overridden."""
    def __init__(self, Afun, label, **kw):
        super().__init__(counts=label, **kw)
        self.Afun = Afun

    def describe(self):
        d = {k: v for k, v in vars(self).items() if k != 'Afun'}
        return d


_ORIG_R_BIN = tc.R_bin


def _R_bin_wrapped(delta, x, d, kappa, ell, inp=tc.PAPER):
    Afun = getattr(inp, 'Afun', None)
    if Afun is None:
        return _ORIG_R_BIN(delta, x, d, kappa, ell, inp)
    if delta <= tc.DELTA0 + 1e-12:
        return 1.0                                   # floor bin: trivial count, as in [OAI]
    return R_density(delta, Afun)


tc.R_bin = _R_bin_wrapped


def high_sup_kink(lx, ly, ell, sigma0, beta_prev, inp, nde=41, nx=6, nd=5):
    """tc.high_sup plus the bins at (and just around) the crossing delta* = 2a* - 1, where the
    density count leaves the trivial value 1.  F is maximal at that kink, which a uniform delta grid
    can miss (the optimiser then exploits the gap).  Same F, same x and d sets as tc.high_sup."""
    worst = tc.high_sup(lx, ly, ell, sigma0, beta_prev, inp, nde=nde, nx=nx, nd=nd)
    a_star = getattr(inp, 'a_star', None)
    if a_star is None:
        return worst
    h = 1 - lx + ell
    dsel = list(np.linspace(inp.d_sel, h, nd)) if h > inp.d_sel else []
    ds = 2*a_star - 1
    for delta in (ds - 1e-9, ds, ds + 1e-9):
        if not (tc.DELTA0 < delta <= 2*beta_prev - 1):
            continue
        a = (1 + delta)/2
        beta = max(sigma0 + 1e-12, a)
        for x in np.linspace(0, 0.5, nx):
            for d in [0.01, min(inp.d_sel, h)] + dsel:
                R = tc.R_bin(delta, x, d, 0.75, ell, inp)
                Fv = tc.F_high(delta, x, d, lx, ly, ell, beta, R, inp.z0)
                if Fv > worst[0]:
                    worst = (Fv, ('kink', round(delta, 6), round(x, 3), round(d, 5), round(R, 6)))
    return worst


def closes_kink(lx, ly, ell, beta_prev, inp, fine=False):
    s0 = tc.low_threshold(lx, ly, ell, inp)
    kw = dict(nde=241, nx=26, nd=17) if fine else dict(nde=41, nx=6, nd=5)
    return s0, high_sup_kink(lx, ly, ell, s0, beta_prev, inp, **kw)


def optimise_capped(beta_prev, inp, cap=None, starts=None, penalty=200.0, slack=2e-5):
    """tc.optimise with (i) the kink bin added to the high side and (ii) an optional extra constraint
    lx + ly + ell <= cap (cap = 1 keeps the manuscript's Lemma 15.1 hypothesis M + ell = 1 as '<=').
    Reported sigma0_eff = sigma0 + max(0, sup F) is the boundary the geometry actually certifies."""
    from scipy.optimize import minimize
    def obj(p):
        lx, ly, ell = p
        if not tc.valid_geometry(lx, ly, ell):
            return 2.0
        if cap is not None and lx + ly + ell > cap + 1e-12:
            return 2.0 + (lx + ly + ell - cap)
        s0 = tc.low_threshold(lx, ly, ell, inp, nd=41)
        if s0 >= beta_prev:
            return 1.5 + s0
        hs = high_sup_kink(lx, ly, ell, s0, beta_prev, inp, nde=41, nx=6, nd=5)[0]
        return s0 + penalty*max(0.0, hs + slack)
    best = (9.0, None)
    for st in starts:
        r = minimize(obj, st, method='Nelder-Mead',
                     options=dict(xatol=1e-7, fatol=1e-9, maxiter=2500))
        if r.fun < best[0]:
            best = (r.fun, tuple(r.x))
    lx, ly, ell = best[1]
    s0, hs = closes_kink(lx, ly, ell, beta_prev, inp, fine=True)
    return dict(sigma0=s0, sigma0_eff=s0 + max(0.0, hs[0]), lx=lx, ly=ly, ell=ell,
                M_plus_ell=lx + ly + ell, high_sup=hs[0], arg=hs[1], objective=best[0])

# ------------------------------------------------------------------------------------------------
# Exact LP (extends barrier_lp.py: same variables v = (lx, ly, ell, s), same low-side rows)
# ------------------------------------------------------------------------------------------------

def bin_row(a, R, x=Fr(1, 2)):
    """bin with real part a <= s, count U^R, slot amplitude q = x delta, at the top dyad d = h
    (eq. 10.15 / Lemma 20.1 with beta* -> s; the z0 terms cancel at d = h):
        a(1 - ly) + h(R + delta/2 - 1/6) - ell/2 + x delta ell - s <= 0,  h = 1 - lx + ell."""
    delta = 2*a - 1
    c_h = R + delta/2 - Fr(1, 6)
    return ([-c_h, -a, c_h - Fr(1, 2) + x*delta, Fr(-1)], -(a + c_h))


def small_rows_row(z0=Fr(17, 50)):
    """Sec. 20.3 small rows: h (z0 - 1/6) - ly/2 <= 0 (no s)."""
    c = z0 - Fr(1, 6)
    return ([-c, Fr(-1, 2), c, Fr(0)], -c)


def lp_rows(a_star, Rfun_fr=None, energy='paper', cap=None, a_hi=Fr(13, 15)):
    low = B.low_rows()
    if energy == 'optimal':
        low = [low[0], low[2], ([Fr(-1), Fr(-1), Fr(2), Fr(0)], Fr(0))]
    rows = low + B.validity_rows() + [small_rows_row()]
    rows.append(bin_row(Fr(51, 100), Fr(1)))         # floor bin
    rows.append(bin_row(a_star, Fr(1)))               # last trivially counted bin (the crossing)
    if Rfun_fr is not None:                           # descending-branch bins a* < a <= a_hi (a_hi = 13/15 <= s
                                                      # always, by Barrier 1; bins above: model check)
        k = 1
        while True:
            a = a_star + Fr(k, 400)
            if a > a_hi:
                break
            rows.append(bin_row(a, min(Fr(1), Rfun_fr(a))))
            k += 1
    if cap is not None:
        rows.append(([Fr(1), Fr(1), Fr(1), Fr(0)], Fr(cap)))
    return rows


def lp_solve(rows):
    res = B.solve(rows)
    ok, bound, y = B.certify(rows, res)
    # exact primal: rationalise the geometry and check every row at s = bound
    g = [Fr(float(v)).limit_denominator(2000) for v in res.x[:3]]
    prim = g + [bound]
    feas = all(sum(r[0][j]*prim[j] for j in range(4)) <= r[1] for r in rows)
    return dict(value=float(res.fun), cert_ok=ok, bound=bound, geom=g, primal_ok=feas,
                tight=[i for i, yi in enumerate(y) if yi != 0])


def closed_form(a_star, cap=None):
    """Conjectured closed forms (verified against the LP below), in terms of the crossing a*."""
    a = Fr(a_star)
    if a <= Fr(3, 4):
        return max(Fr(167, 192), (36*a - 5)/(36*a - 3))
    if cap == 1:
        return a + Fr(1, 6)                           # = 7/6 - 1/(2A): Kintali's formula
    return (1 + 6*a)/(3 + 4*a)                        # = (7A - 3)/(7A - 2)


# scenario table: name -> (a* exact, A(.) float, A(.) exact or None, label)
def _const(A):
    A = Fr(A)
    return (1 - 1/(2*A), A_const(float(A)), (lambda a, A=A: 2*A*(1 - a)), f"A={A}")


SCEN = {
    'hinz_linear':   _const(Fr(5, 2)) [:3] + ("Hinz/[K] linear form R = min(1, 5(1-a)) (A = 5/2)",),
    'hinz_exact':    (Fr(4, 5), A_hinz, (lambda a: 2*A_hinz_exact_fr(a)*(1 - a)),
                      "Hinz Satz A+B exact sigma-dependent form"),
    'huxley_12_5':   _const(Fr(12, 5))[:3] + ("Huxley-type constant A = 12/5 (hypothetical for this family)",),
    'huxley_sigma':  (Fr(7, 9), A_huxley_sigma, (lambda a: 2*A_huxley_sigma_fr(a)*(1 - a)),
                      "Ingham/Huxley sigma-dependent shape (hypothetical for this family)"),
    'A_7_3':         _const(Fr(7, 3))[:3] + ("A = 7/3 (hypothetical)",),
    'A_9_4':         _const(Fr(9, 4))[:3] + ("A = 9/4 (hypothetical)",),
    'A_2_DH':        _const(Fr(2))[:3] + ("A = 2: density hypothesis for the full Hecke family (conjectural)",),
    'A_3_2':         _const(Fr(3, 2))[:3] + ("A = 3/2: beyond full-family DH (hypothetical)",),
    'A_1_rowDH':     _const(Fr(1))[:3] + ("A = 1: = threshold_calculus 'DH' (row-family DH)",),
}


def cmd_lp():
    print("Exact LP: low side (paper energy) + small rows + floor + crossing bin + descending bins")
    print(f"{'scenario':14s} {'a*':>6s} | {'uncapped':>26s} {'geom (lx,ly,ell)':>22s} | {'cap M+ell<=1':>22s} | {'optimal energy':>14s}")
    out = {}
    for name, (a_star, Afl, Rfr, label) in SCEN.items():
        r1 = lp_solve(lp_rows(a_star, Rfr))
        r2 = lp_solve(lp_rows(a_star, Rfr, cap=1))
        r3 = lp_solve(lp_rows(a_star, Rfr, energy='optimal'))
        cf1, cf2 = closed_form(a_star), closed_form(a_star, cap=1)
        chk = (r1['bound'] == cf1 and r2['bound'] == cf2 and r1['cert_ok'] and r2['cert_ok']
               and r1['primal_ok'] and r2['primal_ok'])
        print(f"{name:14s} {str(a_star):>6s} | {str(r1['bound']):>10s} = {float(r1['bound']):.6f} "
              f"{str(tuple(str(v) for v in r1['geom'])):>26s} | {str(r2['bound']):>8s} = {float(r2['bound']):.6f} |"
              f" {str(r3['bound']):>8s}  closed-form match: {chk}")
        out[name] = dict(label=label, a_star=str(a_star), uncapped=str(r1['bound']), uncapped_float=float(r1['bound']),
                         geom=[str(v) for v in r1['geom']], cert=r1['cert_ok'], primal=r1['primal_ok'],
                         capped=str(r2['bound']), capped_geom=[str(v) for v in r2['geom']],
                         optimal_energy=str(r3['bound']), closed_form_match=chk)
    # the 7/8 requirement
    a78 = Fr(19, 36)
    r = lp_solve(lp_rows(a78, lambda a: 2*Fr(18, 17)*(1 - a)))
    print(f"crossing needed for 7/8: a* = {a78} (A = 18/17): LP = {r['bound']} geom {[str(v) for v in r['geom']]}")
    out['needed_for_7_8'] = dict(a_star=str(a78), A='18/17', value=str(r['bound']))
    return out


def cmd_check():
    """full threshold_calculus model (fine grid, all bins/amplitudes/dyads, beta_prev = 1) at the LP optima."""
    rows = []
    for name, (a_star, Afl, Rfr, label) in SCEN.items():
        inp = DensityInputs(Afl, 'density:' + name); inp.a_star = float(a_star)
        for cap in (None, 1):
            r = lp_solve(lp_rows(a_star, Rfr, cap=cap))
            lx, ly, ell = (float(v) for v in r['geom'])
            s0, hs = closes_kink(lx, ly, ell, 1.0, inp, fine=True)
            rows.append((name, cap, str(r['bound']), s0, hs[0], hs[1]))
            print(f"{name:14s} cap={cap}: LP {str(r['bound']):>8s} ({float(r['bound']):.6f}); model low = {s0:.6f};"
                  f" sup F = {hs[0]:+.2e} at {hs[1]}", flush=True)
    return rows


def cmd_run(name, cap=None, energy='paper'):
    a_star, Afl, Rfr, label = SCEN[name]
    inp = DensityInputs(Afl, 'density:' + name, energy=energy); inp.a_star = float(a_star)
    r = lp_solve(lp_rows(a_star, Rfr, cap=cap))
    lpg = tuple(float(v) for v in r['geom'])
    starts = [lpg, (0.5, 0.5, 0.0), (17/48, 23/48, 1/6), (0.4, 0.45, 0.1), (0.3, 0.45, 0.2),
              (0.52, 0.53, 0.02), (0.45, 0.5, 0.05)]
    t0 = time.time()
    res = optimise_capped(1.0, inp, cap=cap, starts=starts)
    res = {k: (float(v) if isinstance(v, (int, float, np.floating)) else str(v)) for k, v in res.items()}
    res.update(scenario=name, label=label, cap=cap, energy=energy, beta_prev=1.0, lp_value=str(r['bound']),
               lp_value_float=float(r['bound']), lp_geom=[str(v) for v in r['geom']],
               seconds=round(time.time() - t0, 1), inputs=inp.describe())
    tag = name + ('_cap1' if cap else '') + ('_optE' if energy != 'paper' else '')
    out = os.path.join(HERE, '..', 'results', 'SPF_' + tag + '.json')
    with open(out, 'w') as f:
        json.dump(res, f, indent=1)
    print(tag, json.dumps(res), flush=True)
    return res


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'lp'
    if cmd == 'lp':
        o = cmd_lp()
        with open(os.path.join(HERE, '..', 'results', 'SPF_lp.json'), 'w') as f:
            json.dump(o, f, indent=1)
    elif cmd == 'check':
        cmd_check()
    elif cmd == 'list':
        for k, v in SCEN.items():
            print(k, '-', v[3])
    elif cmd == 'run':
        nm = sys.argv[2]
        cap = None
        energy = 'paper'
        for extra in sys.argv[3:]:
            if extra == 'cap1':
                cap = 1
            if extra == 'optE':
                energy = 'optimal'
        cmd_run(nm, cap=cap, energy=energy)
    else:
        print(__doc__)
