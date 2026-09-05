#!/usr/bin/env python3
"""Frozen (61-smooth) variant: complete cell-exact verification of
TB_s(x) = 4 sqrt(x) A^s_x - 3 B^s_x >= 0 for ALL real x in [2, P_61],
by enumerating all 2^18 squarefree divisors of P_61 (the entire index lattice).
On each cell [d_i, d_{i+1}) the prefix sums are constant and TB is monotone in x,
so the global min is attained at cell endpoints. Also: a_min = min_{t>=62} A^s_t,
B^s sign change, B^s limit Pi(1 - p^{-1/2})."""
import numpy as np
from itertools import combinations

P = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61]
n = len(P)
# enumerate all subsets: divisor value (float64 log-safe), mu, 1/d, 1/sqrt(d)
divs = np.ones(1, dtype=np.float64)
mus = np.ones(1, dtype=np.int8)
for p in P:
    divs = np.concatenate([divs, divs*p])
    mus = np.concatenate([mus, -mus])
order = np.argsort(divs)
d = divs[order]; m = mus[order].astype(np.float64)
A = np.cumsum(m/d)          # A^s at threshold d_i (inclusive)
B = np.cumsum(m/np.sqrt(d))
print(f"lattice size = {len(d)}; P_61 = {d[-1]:.6e}")
print(f"A at top = {A[-1]:.10f}  (should be prod(1-1/p) = {np.prod([1-1/p for p in P]):.10f})")
print(f"B at top = {B[-1]:.10f}  (prod(1-1/sqrt(p)) = {np.prod([1-1/np.sqrt(p)for p in P]):.10f})")

# a_min = min A^s_t over thresholds t >= 62 (i.e. cells whose divisor >= 62... careful:
# A^s_t is the value on cell [d_i, d_{i+1}); t >= 62 means all cells with d_{i+1} > 62,
# value A_i for cell starting at d_i; the L-105022 claim: A_i >= 0 for every cell [d_i,.) with d_i >= 62)
cells62 = d >= 62
print(f"min A^s on cells with d_i >= 62: {A[cells62].min():.12f} at d = {d[cells62][np.argmin(A[cells62])]:.6e}")
print(f"count A^s < 0 cells (all should start below 62): {(A < 0).sum()}; "
      f"largest divisor starting a negative cell: {d[A < 0].max():.1f}")

# B sign structure
neg = B < 0
first_pos_after = None
idx3 = np.searchsorted(d, 3.0)
post = np.where(~neg[idx3:])[0]
if len(post): first_pos_after = d[idx3 + post[0]]
print(f"B^s < 0 fraction of cells: {neg.mean():.4f}; first cell with B^s >= 0 at d >= 3: {first_pos_after:.6e}")
print(f"max B^s over cells d_i >= 3: {B[idx3:].max():.6f}; min: {B[idx3:].min():.6f}")

# TB cell-exact min over ALL x in [2, P_61]
# cell i spans [d_i, d_{i+1}); evaluate TB at left end (x=d_i) and right end (x=d_{i+1}^-).
sq_l = np.sqrt(d)
sq_r = np.sqrt(np.concatenate([d[1:], [d[-1]*1.0]]))  # right endpoint (last cell: itself)
TB_l = 4*sq_l*A - 3*B
TB_r = 4*sq_r*A - 3*B
TBmin_cell = np.minimum(TB_l, TB_r)
# restrict to x >= 2 (cells overlapping [2, inf)): d_{i+1} > 2 -> from cell containing 2
start = np.searchsorted(d, 2.0, side='right') - 1
sub = TBmin_cell[start:]
i = int(np.argmin(sub)) + start
print(f"GLOBAL: min over all real x in [2, P_61] of TB_s(x) = {sub.min():.9f} "
      f"attained in cell starting at d = {d[i]:.6f} (A={A[i]:+.6e}, B={B[i]:+.6f})")
print(f"  (evaluated at cell {'left' if TB_l[i]<=TB_r[i] else 'right'} endpoint)")
# also beyond P_61: TB = 4 sqrt(x) * 0.1316 - 3*B_top -> increasing, min at x=P_61:
print(f"  at x = P_61: TB = {4*np.sqrt(d[-1])*A[-1] - 3*B[-1]:.4e} (huge, growing)")
