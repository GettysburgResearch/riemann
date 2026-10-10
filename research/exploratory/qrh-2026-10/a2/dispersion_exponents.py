#!/usr/bin/env python3
"""PROPOSED exponent bookkeeping for DISPERSION_GRH_STEP.md (exact rationals via sympy; no number theory is
computed here).  All quantities are exponents of D (columns L = D, rows H = D^rho, dual rows calH = D^(2-rho)).

Extraction (PR 910 Prop. 7.2 with k = 1, linear in the moment exponent):  a second-moment bound
sum_{N u <= D^rho} |A_u(D)|^2 << D^m  gives the boundary  sigma(m, rho) = (m - rho/6)/2.

Checked statements (asserts):
  (1) Oct 5 pipeline run at rho < 1 (positivity step + reflection + quadratic large sieve):
      m = max(1+rho, 2, 3-rho); its boundary is minimised at rho = 1, value 11/12.
  (2) positivity step alone (perfect row-blind dual bound, dual diagonal kept): m = max(1+rho, 2).
  (3) DR transplant: Axiom 4 (Def. 3.1(iv) of Dunn-Radziwill) for the family at loss eta gives
      m = 1 + rho + 2 eta, boundary 1/2 + eta + 5 rho/12 = beta* + 5 rho/12 > beta* when eta = beta* - 1/2.
  (4) zero-density exponent Adens plus zero-free half-plane beta*:
      m = max(1+rho, max_{1/2 <= s <= beta*} (Adens rho (1-s) + 2 s));
      the bootstrap fixed point is 1 - 1/(6 Adens); for Adens = 2 (DH) and beta* = 11/12 the output is
      exactly 11/12 for every rho in (0, 1].
  (5) relative precision reached by (4) with Adens = 2 on the dual side: (H/L)^(2(1-beta*)), vs the
      required (H/L)^1.
  (6) [INF about DR] dispersion term D_2 in DR variables (a = log A/log X, b = log B/log X, a + b = 1):
      pointwise GRH: 2b;  Heath-Brown cubic large sieve on the dual: max(a/3 + 2b, a + b, 2b);
      DR's main-term scale (AB)^(2/3) B: 2a/3 + 5b/3.  The large sieve suffices iff b < a.
"""
from fractions import Fraction as Fr
import sympy as sp

rho, beta, A, eta, s = sp.symbols('rho beta A eta s', positive=True)

def sigma(m, r):
    return (m - r / 6) / 2

grid = [Fr(k, 20) for k in range(1, 20)] + [Fr(1)]      # rho in (0, 1]


out = []
# (1), (2)
oct_m = lambda r: max(1 + r, Fr(2), 3 - r)
blind_m = lambda r: max(1 + r, Fr(2))
for r in grid:
    so, sb, st = sigma(oct_m(r), r), sigma(blind_m(r), r), sigma(1 + r, r)
    if r < 1:
        assert so > Fr(11, 12) and sb > Fr(11, 12) and st < Fr(11, 12)
        assert so == Fr(3, 2) - 7 * r / 12 and sb == 1 - r / 12
    else:
        assert so == sb == st == Fr(11, 12)
out.append("(1)-(2) rho : oct5-pipeline  positivity-only  target(1/2+5rho/12)")
for r in [Fr(1, 2), Fr(3, 4), Fr(9, 10), Fr(1)]:
    out.append(f"   {str(r):>5} : {str(sigma(oct_m(r), r)):>8} {str(sigma(blind_m(r), r)):>8} {str(sigma(1 + r, r)):>8}")

# (3) DR transplant: Axiom 4 with eta = beta* - 1/2
s3 = sp.simplify(sigma(1 + rho + 2 * eta, rho).subs(eta, beta - sp.Rational(1, 2)))
assert sp.simplify(s3 - (beta + 5 * rho / 12)) == 0
out.append(f"(3) DR transplant boundary = {s3}  (> beta* for every rho > 0)")

# (4) zero density + half-plane: f(s) = A rho (1-s) + 2 s is linear in s, so its max is at an endpoint
def m_zd(Ad, b, r):
    f = lambda x: Ad * r * (1 - x) + 2 * x
    return max(1 + r, f(Fr(1, 2)), f(b))
for r in grid:
    assert sigma(m_zd(Fr(2), Fr(11, 12), r), r) == Fr(11, 12)          # DH, beta* = 11/12: no gain at any rho
    for b in [Fr(3, 4), Fr(5, 6), Fr(7, 8), Fr(9, 10)]:                  # DH, beta* < 11/12: output > beta*
        assert sigma(m_zd(Fr(2), b, r), r) > b
    for b in [Fr(19, 20), Fr(99, 100)]:                                  # DH, beta* > 11/12: output >= 11/12
        assert sigma(m_zd(Fr(2), b, r), r) >= Fr(11, 12)
# fixed point for rho < 2/A (max at s = beta*): beta* + rho (A (1-beta*) - 1/6)/2 = beta*
sig4 = sp.expand(sigma(A * rho * (1 - beta) + 2 * beta, rho))
fp = sp.solve(sp.Eq(sig4, beta), beta)
assert len(fp) == 1 and sp.simplify(fp[0] - (1 - 1 / (6 * A))) == 0
out.append(f"(4) zero-density bootstrap: sigma_new = {sp.simplify(sig4)};  fixed point beta* = {sp.simplify(1 - 1/(6*A))}  (A=2: 11/12)")
for Ad in [Fr(2), Fr(12, 5), Fr(3)]:
    best = min(min(sigma(m_zd(Ad, b, r), r) for r in grid + [Fr(2) / Ad]) for b in [Fr(99, 100)])
    out.append(f"    density exponent A = {Ad}: best boundary over rho (beta* = 99/100) = {best} ; 1 - 1/(6A) = {1 - 1/(6*Ad)}")

# (5) relative precision on the dual side, DH, rho < 1
L, H = sp.symbols('L H', positive=True)
err = 2 * beta + 2 * rho * (1 - beta)          # D-exponent of the DH+beta* bound for M_2
rel = sp.simplify(err - 2)                      # relative to the dual-diagonal scale L^2 (original side D^2)
assert sp.simplify(rel - 2 * (1 - beta) * (rho - 1)) == 0
out.append(f"(5) DH + beta*: error/L^2 = D^({sp.factor(rel)}) = (H/L)^(2(1-beta*)); needed (H/L)^1; at beta*=11/12: (H/L)^(1/6)")

# (6) DR's D_2 in X-exponents
out.append("(6) DR D_2 (a = log A, b = log B, a + b = 1): b, pointwise-GRH, cubic-LS, main (AB)^(2/3)B, LS ok?")
for b in [Fr(1, 3) + Fr(1, 30), Fr(2, 5), Fr(1, 2), Fr(2, 3)]:
    a = 1 - b
    grh, ls, main = 2 * b, max(a / 3 + 2 * b, a + b, 2 * b), 2 * a / 3 + 5 * b / 3
    assert (ls < main) == (b < a)
    out.append(f"    b = {str(b):>5}: {str(grh):>5} {str(ls):>5} {str(main):>6}  {ls < main}")
print("\n".join(out))
print("all asserts passed")
