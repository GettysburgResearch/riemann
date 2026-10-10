#!/usr/bin/env python3
"""Floor-bin barrier: boundary sigma0 when the floor-bin (or every bin) row sum is assumed to
enjoy a saving U^{-theta} from cancellation across rows.

Status: EXPLORATORY wrapper around threshold_calculus.py (same black-box conventions).
Mechanism: Lemma 10.4 / eq. (10.15) of the OpenAI manuscript only uses the row sum through
U^{R + delta/2}; a hypothetical bound U^{R - theta + delta/2} is modelled as R -> R - theta.

Usage: python3 floor_theta.py [out.json]   (prints all tables; optional JSON dump)
"""
import json, sys, time
import numpy as np
import threshold_calculus as tc

_R_ORIG = tc.R_bin
THETAS = [0.0, 0.05, 0.1, 0.25, 0.5]


def make_R(theta, where):
    """where='floor': saving only in the floor bin (delta = delta0), R_floor = 1 - theta;
       where='all'  : saving in every bin, capped at square-root cancellation inside the bin,
                      R -> max(R - theta, R/2)."""
    def R(delta, x, d, kappa, ell, inp=tc.PAPER):
        r = _R_ORIG(delta, x, d, kappa, ell, inp)
        if delta <= tc.DELTA0 + 1e-12:
            return r - theta
        if where == 'all':
            return max(r - theta, r/2)
        return r
    return R


STARTS = [(17/48, 23/48, 1/6), (0.3551, 0.4781, 0.1668), (0.4061, 0.4061, 0.1871),
          (0.4, 0.4, 0.2), (0.37, 0.43, 0.2)]


def run(theta, where, inp, beta_prev, delta0=1/50):
    tc.DELTA0 = delta0
    tc.R_bin = make_R(theta, where)
    try:
        res = tc.optimise(beta_prev, inp, starts=STARTS)
    finally:
        tc.R_bin = _R_ORIG
        tc.DELTA0 = 1/50
    return res


def _job(args):
    label, where, theta, counts, bp, delta0 = args[:6]
    energy = args[6] if len(args) > 6 else 'paper'
    r = run(theta, where, tc.Inputs(counts=counts, energy=energy), bp, delta0)
    return dict(label=label, where=where, theta=theta, delta0=delta0, sigma0=float(r['sigma0']),
                lx=float(r['lx']), ly=float(r['ly']), ell=float(r['ell']),
                high_sup=float(r['high_sup']), arg=str(r['arg']))


def barrier(lx, ly, ell, delta0=0.0):
    """delta -> delta0 limit of the high exponent at d = h with R = 1 - delta0 (x = 1/2):
    sigma0 must exceed a(1-ly) + h(5/6 - delta0/2) - ell/2 + delta0*ell/2,  a = (1+delta0)/2."""
    h = 1 - lx + ell
    a = (1 + delta0)/2
    return a*(1 - ly) + h*(5/6 - delta0/2) - ell/2 + delta0*ell/2


def minimax_barrier(inp, delta0=0.0):
    """min over geometry of max(low side, near-critical barrier): the absolute-value ceiling."""
    from scipy.optimize import minimize
    def obj(p):
        lx, ly, ell = p
        if not tc.valid_geometry(lx, ly, ell): return 2.0
        return max(tc.low_threshold(lx, ly, ell, inp, nd=81), barrier(lx, ly, ell, delta0))
    best = (9, None)
    for st in [(0.4, 0.4, 0.19), (0.35, 0.45, 0.17), (0.3, 0.5, 0.2), (0.45, 0.45, 0.1)]:
        r = minimize(obj, st, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-9, maxiter=4000))
        if r.fun < best[0]: best = (r.fun, tuple(r.x))
    return best


def low_only(inp):
    """inf over admissible geometry of the low threshold alone (high side ignored)."""
    from scipy.optimize import minimize
    def obj(p):
        lx, ly, ell = p
        if not tc.valid_geometry(lx, ly, ell): return 2.0
        return tc.low_threshold(lx, ly, ell, inp, nd=81)
    best = (9, None)
    for st in [(0.4, 0.4, 0.19), (0.3, 0.5, 0.2), (0.45, 0.5, 0.3), (0.6, 0.6, 0.5)]:
        r = minimize(obj, st, method='Nelder-Mead', options=dict(xatol=1e-7, fatol=1e-9, maxiter=4000))
        if r.fun < best[0]: best = (r.fun, tuple(r.x))
    return best


if __name__ == '__main__':
    from multiprocessing import Pool
    out = {}
    t0 = time.time()
    jobs = []
    for label, counts, bp in [('paper_bp11_12', 'paper', 11/12), ('paper_bp7_8', 'paper', 7/8),
                              ('DH_bp11_12', 'DH', 11/12)]:
        for where in ('floor', 'all'):
            for th in THETAS:
                jobs.append((label, where, th, counts, bp, 1/50))
    for where in ('floor', 'all'):                  # improved low side (large-sieve diagonal only)
        for th in THETAS:
            jobs.append(('DH_optE_bp11_12', where, th, 'DH', 11/12, 1/50, 'optimal'))
            jobs.append(('paper_optE_bp11_12', where, th, 'paper', 11/12, 1/50, 'optimal'))
    for d0 in (1/100, 1/500):                       # floor lowered towards 1/2 (needs D1 extended)
        for th in (0.0, 0.5):
            jobs.append(('DH_bp11_12_lowfloor', 'floor', th, 'DH', 11/12, d0))
            jobs.append(('paper_bp11_12_lowfloor', 'floor', th, 'paper', 11/12, d0))
    with Pool(4) as pool:
        rows = pool.map(_job, jobs, chunksize=1)
    for r in rows:
        print(f"{r['label']:22s} {r['where']:5s} delta0={r['delta0']:.3f} theta={r['theta']:4.2f} "
              f"sigma0={r['sigma0']:.6f} (lx,ly,ell)=({r['lx']:.4f},{r['ly']:.4f},{r['ell']:.4f}) "
              f"supF={r['high_sup']:+.1e} at {r['arg']}", flush=True)
    out['runs'] = rows
    for d0 in (1/50, 0.0):
        v, g = minimax_barrier(tc.Inputs(counts='DH'), d0)
        print(f"minimax(low, near-critical barrier at delta0={d0}) = {v:.6f} at {tuple(round(t, 5) for t in g)}")
        out[f'minimax_barrier_delta0_{d0}'] = dict(value=v, geometry=g)
    v, g = low_only(tc.Inputs())
    print(f"low side alone (high side ignored): inf sigma0 = {v:.6f} at {tuple(round(t, 5) for t in g)}")
    out['low_only'] = dict(value=v, geometry=g)
    out['seconds'] = round(time.time() - t0, 1)
    print('seconds', out['seconds'])
    if len(sys.argv) > 1:
        json.dump(out, open(sys.argv[1], 'w'), indent=1, default=float)
        print('wrote', sys.argv[1])
