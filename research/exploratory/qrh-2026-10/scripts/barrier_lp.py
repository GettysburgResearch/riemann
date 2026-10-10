#!/usr/bin/env python3
"""Exact barrier certificates for the Part II architecture (PROPOSED; conditional on the manuscript's
lemma output formulas holding in general geometry).

Barrier 1 (low side alone):     sigma0 >= 13/15 for every geometry (paper reflected-energy lemma).
Barrier 2 (low side + floor bin): sigma0 >= sigma_FB for every geometry and ANY row-count input,
  because rows with no zero right of 51/100 can only be counted trivially (U^1 rows).
Certificates are nonnegative rational multipliers; verification is exact (fractions)."""
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import linprog

# variables v = (lx, ly, ell, s); every constraint written as  coeffs . v <= rhs
def low_rows():
    # s >= 5/6 - 5/12 lx - 5/12 ly - ell/6 + E/2 for E in {M, (2M+1+3ell)/4, 2M+ell-1}
    rows = []
    # E = M:  s >= 5/6 + lx/12 + ly/12 - ell/6
    rows.append(([Fr(1,12), Fr(1,12), Fr(-1,6), Fr(-1)], Fr(-5,6)))
    # E = (2M+1+3ell)/4: s >= 5/6 + 1/8 + (1/4 - 5/12)(lx+ly) + (3/8 - 1/6) ell
    rows.append(([Fr(-1,6), Fr(-1,6), Fr(5,24), Fr(-1)], Fr(-23,24)))
    # E = 2M + ell - 1: s >= 5/6 - 1/2 + (1 - 5/12)(lx+ly) + (1/2 - 1/6) ell
    rows.append(([Fr(7,12), Fr(7,12), Fr(1,3), Fr(-1)], Fr(-1,3)))
    return rows

def floor_row(a0=Fr(51,100), x=Fr(1,2), z0=Fr(17,50)):
    # F at d = h for the floor bin, delta0 = 2a0-1, R = 1, beta* >= s:  need s >= a0(1-ly) - h/6 - ell/2 + x d0 ell + h(1 + d0/2)
    d0 = 2*a0 - 1
    c_h = -Fr(1,6) + 1 + d0/2          # coefficient of h = 1 - lx + ell
    const = a0 + c_h
    # s >= const - a0 ly - c_h lx + (c_h - 1/2 + x d0) ell
    return ([-c_h, -a0, c_h - Fr(1,2) + x*d0, Fr(-1)], -const)

def validity_rows():
    # lx <= ly ; ell <= lx ; -ell <= 0
    return [([Fr(1), Fr(-1), 0, 0], Fr(0)), ([Fr(-1), 0, Fr(1), 0], Fr(0)), ([0, 0, Fr(-1), 0], Fr(0))]

def solve(rows):
    A = np.array([[float(c) for c in r[0]] for r in rows]); b = np.array([float(r[1]) for r in rows])
    res = linprog([0, 0, 0, 1], A_ub=A, b_ub=b, bounds=[(None, None)]*4, method='highs')
    return res

def certify(rows, res):
    """Rationalise duals y >= 0 with y^T A = -(0,0,0,1)... i.e. sum y_i A_i = (0,0,0,-1); bound = -y.b"""
    y = -res.ineqlin.marginals
    yr = [Fr(v).limit_denominator(10**6) for v in y]
    comb = [sum(yr[i]*rows[i][0][j] for i in range(len(rows))) for j in range(4)]
    bound = -sum(yr[i]*rows[i][1] for i in range(len(rows)))
    ok = all(v >= 0 for v in yr) and comb[:3] == [0, 0, 0] and comb[3] == -1
    return ok, bound, yr

if __name__ == '__main__':
    r1 = low_rows() + validity_rows()
    res = solve(r1); ok, bound, y = certify(r1, res)
    print(f"Barrier 1 (low side): LP min s = {res.fun:.9f}; exact certificate valid={ok}, bound = {bound} ; multipliers {y}")
    r2 = low_rows() + [floor_row()] + validity_rows()
    res = solve(r2); ok, bound, y = certify(r2, res)
    print(f"Barrier 2 (low + floor bin): LP min s = {res.fun:.9f} at (lx,ly,ell) = {np.round(res.x[:3],5)}; exact certificate valid={ok}, bound = {bound} = {float(bound):.6f}; multipliers {y}")
    # optimal energy (only branches E=M and E=2M+ell-1) + floor + M >= 2 ell
    rows_opt = [low_rows()[0], low_rows()[2], floor_row()] + validity_rows() + [([Fr(-1), Fr(-1), Fr(2), 0], Fr(0))]
    res = solve(rows_opt); ok, bound, y = certify(rows_opt, res)
    print(f"Barrier 3 (optimal energy + floor bin): LP min s = {res.fun:.9f} at {np.round(res.x[:3],5)}; certificate valid={ok}, bound = {bound} = {float(bound):.6f}")
    # floor bin limit if the detector floor a0 -> 1/2
    r4 = low_rows() + [floor_row(a0=Fr(1,2))] + validity_rows()
    res = solve(r4); ok, bound, y = certify(r4, res)
    print(f"Barrier 2' (floor at a0=1/2): LP min s = {res.fun:.9f}; certificate valid={ok}, bound = {bound} = {float(bound):.6f}")
