#!/usr/bin/env python3
"""O3 exact-rational barrier LPs (PROPOSED model; inputs are the Sep 30 manuscript's stated lemma outputs).

Imports ../../../scripts/barrier_lp.py UNCHANGED for the floor row, validity rows and the certificate
routine, and adds two dials:
  theta_gram in {b/12 (paper Prop. 15.2), 0 (P_a^{1/6} term removed)}: the low-side Gram loss;
  f >= 0: a signed saving U^{-f} on the floor-bin row sum at the top dyad d = h (Lemma 10.4 replaced
          by a cancellation statement); enters the floor row as  - f*h.
Low side (d = 0 term of THRESHOLD_CALCULUS Sec. 2):
  s >= 1 - lx/2 - h/6 + (-ly + g + E)/2,  g = theta-dependent Gram exponent (b/6 or 0),
  E in {M, (2M+1+3ell)/4, 2M+ell-1},  h = 1 - lx + ell, M = lx + ly, b = ly - lx.
Every reported bound comes with nonnegative rational multipliers verified in Fractions.
"""
import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'scripts'))
import barrier_lp as B   # unchanged import
import numpy as np

def low_rows(gram):
    """gram = 'paper' (g = b/6) or 'zero' (g = 0). Variables (lx, ly, ell, s); rows coeffs.v <= rhs."""
    rows = []
    # s >= 1 - lx/2 - (1 - lx + ell)/6 + (-ly + g + E)/2  =  5/6 - lx/3 - ly/2 - ell/6 + g/2 + E/2
    base = {'lx': Fr(-1, 3), 'ly': Fr(-1, 2), 'ell': Fr(-1, 6), 'c': Fr(5, 6)}
    if gram == 'paper':        # + (ly - lx)/12
        base['lx'] += Fr(-1, 12); base['ly'] += Fr(1, 12)
    Es = [({'lx': 1, 'ly': 1, 'ell': 0, 'c': 0}),                                   # E = M
          ({'lx': Fr(1, 2), 'ly': Fr(1, 2), 'ell': Fr(3, 4), 'c': Fr(1, 4)}),       # E = (2M+1+3ell)/4
          ({'lx': 2, 'ly': 2, 'ell': 1, 'c': -1})]                                   # E = 2M+ell-1
    # second Gram term P_a^2/Y' (always kept): g = 2b - ly = -2 lx + ly  ->  + g/2
    base2 = {'lx': Fr(-1, 3) - 1, 'ly': Fr(-1, 2) + Fr(1, 2), 'ell': Fr(-1, 6), 'c': Fr(5, 6)}
    for bb in ((base, base2) if gram == 'zero' else (base, base2)):
        for E in Es:
            co = {k: bb[k] + Fr(E[k]) / 2 for k in bb}
            # s >= co.lx lx + co.ly ly + co.ell ell + co.c   ->   co.lx lx + co.ly ly + co.ell ell - s <= -co.c
            rows.append(([co['lx'], co['ly'], co['ell'], Fr(-1)], -co['c']))
    return rows

def floor_row_f(a0, f):
    """barrier_lp.floor_row with an extra saving U^{-f} at d = h: constraint s >= ... - f*h."""
    coeffs, rhs = B.floor_row(a0=a0)
    # floor_row encodes  s >= const - c_h lx - a0 ly + (...) ell  with h = 1 - lx + ell; subtract f*h:
    coeffs = [coeffs[0] - f, coeffs[1], coeffs[2] + f, coeffs[3]]
    rhs = rhs + f
    return (coeffs, rhs)

def run(gram, a0, f, extra=()):
    rows = low_rows(gram) + [floor_row_f(a0, f)] + B.validity_rows() + list(extra)
    res = B.solve(rows)
    ok, bound, y = B.certify(rows, res)
    return dict(gram=gram, a0=str(a0), f=str(f), lp=res.fun, x=[float(v) for v in res.x[:3]],
                certificate_valid=ok, bound=str(bound), bound_float=float(bound))

if __name__ == '__main__':
    out = []
    # self-test: gram='paper' reproduces barrier_lp's Barrier 2 (167/192) and Barrier 2' (13/15)
    for gram in ('paper', 'zero'):
        for a0 in (Fr(51, 100), Fr(1, 2)):
            for f in (Fr(0), Fr(1, 100), Fr(1, 50), Fr(1, 20), Fr(1, 10)):
                r = run(gram, a0, f); out.append(r)
                print(f"gram={gram:5s} a0={str(a0):7s} f={str(f):5s}: barrier = {r['bound']:>12s} = {r['bound_float']:.6f}"
                      f"  at (lx,ly,ell)={np.round(r['x'],5)}  cert={r['certificate_valid']}")
    json.dump(out, open(os.path.join(os.path.dirname(__file__), '..', 'results', 'o3_barriers.json'), 'w'), indent=1)
