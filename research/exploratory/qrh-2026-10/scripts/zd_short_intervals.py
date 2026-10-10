"""zd_short_intervals.py -- primes in short intervals from A(sigma) with/without QRH-IMPORT.

Status: CONDITIONAL on QRH-IMPORT (external, unreviewed) / reconnaissance (float grid search).

Input: the best-known unconditional zero-density table A(sigma) on [1/2, 7/8] (ANTEDB
blueprint Table "Current best upper bound on A(sigma)", excluding Kerr's unpublished
preprint; checked against zd_antedb_qrh.py part 'best').  QRH-IMPORT gives N(sigma,T)=0
for sigma > 7/8 and does NOT change A on [1/2, 7/8] (see ZERO_DENSITY_CONDITIONAL.md).

Explicit formula: with h = x^theta and T = x^(1 - theta + eta),
  psi(x+h) - psi(x) - h << h x^eps [ x^(-eta) + max_{1/2<=s<=Theta} x^((s-1) + (1-theta+eta) D(s)) ],
D(s) = A(s)(1-s).  Under QRH Theta = 7/8, so the saving is a power x^(-delta(theta)) with
  delta(theta) = sup_eta min( eta, min_s [ (1-s) - (1-theta+eta) D(s) ] ).
Unconditionally Theta = 1 and the inner minimum tends to 0 as s -> 1 (only a
Vinogradov-Korobov-type sub-power saving).  Grid search only: not a certified optimum.
"""
from fractions import Fraction as F

PIECES = [  # (lo, hi, A as function) -- unconditional best known (ANTEDB table)
    (F(1, 2), F(7, 10), lambda s: 3 / (2 - s)),                 # Ingham 1940
    (F(7, 10), F(19, 25), lambda s: 15 / (3 + 5 * s)),          # Guth-Maynard 2024
    (F(19, 25), F(127, 167), lambda s: 9 / (8 * s - 2)),        # Ivic
    (F(127, 167), F(13, 17), lambda s: 15 / (13 * s - 3)),      # Ivic
    (F(13, 17), F(17, 22), lambda s: 6 / (5 * s - 1)),          # Ivic
    (F(17, 22), F(41, 53), lambda s: 2 / (9 * s - 6)),          # Tao-Trudgian-Yang
    (F(41, 53), F(7, 9), lambda s: 9 / (7 * s - 1)),            # Ivic / Heath-Brown
    (F(7, 9), F(1867, 2347), lambda s: 9 / (8 * (2 * s - 1))),  # Tao-Trudgian-Yang
    (F(1867, 2347), F(7, 8), lambda s: 3 / (2 * s)),            # Bourgain 2000/2002, Ivic
]


def A(s):
    vals = [f(s) for (lo, hi, f) in PIECES if lo <= s <= hi]
    return min(vals)


def delta(theta, n_s=3000, n_eta=400):
    ss = [0.5 + (0.875 - 0.5) * i / n_s for i in range(n_s + 1)]
    Ds = [(s, A(F(s).limit_denominator(10**9)) * (1 - s)) for s in ss]
    Ds = [(s, float(d)) for s, d in Ds]
    best = (-1.0, None)
    for j in range(n_eta + 1):
        eta = 0.25 * j / n_eta
        inner = min((1 - s) - (1 - theta + eta) * d for s, d in Ds)
        val = min(eta, inner)
        if val > best[0]:
            best = (val, eta)
    return best


if __name__ == "__main__":
    smax = max((float(A(F(i, 4000))), i / 4000) for i in range(2000, 3501))
    print(f"sup A on [1/2,7/8] = {smax[0]:.6f} at sigma = {smax[1]:.4f} (30/13 = {30/13:.6f})")
    print(f"Hoheisel-type threshold theta > 1 - 1/sup A = {1 - 1/smax[0]:.6f} (17/30 = {17/30:.6f}); "
          f"almost-all threshold 1 - 2/sup A = {1 - 2/smax[0]:.6f} (2/15 = {2/15:.6f})")
    print(f"{'theta':>6} {'delta_QRH(theta)':>17} {'eta':>7} {'RH value theta-1/2':>19}")
    for theta in [0.57, 0.58, 0.6, 0.65, 0.7, 0.75, 0.8, 0.875, 0.9, 1.0]:
        d, eta = delta(theta)
        print(f"{theta:6.3f} {d:17.5f} {eta:7.4f} {theta - 0.5:19.3f}")
