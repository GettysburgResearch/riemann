#!/usr/bin/env python3
"""Budget ledger for "Uniform exclusion of Landau-Siegel zeros" (OpenAI, 1 Oct 2026; unreviewed).

Source: pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026/build/paper.tex  (773 lines)

Part A  EXACT_RATIONAL: reproduces the manuscript's displayed constants (Cor. 4, Lemma 6, eq. (5.1)).
Part B  parametric contradiction condition and its closed-form optimum (PROPOSED algebra; the
        transcendental constants e, log are rounded UP to rationals so delta_max is a lower bound).
Part C  explicit constant c for every q >= 3, q != 8, following the manuscript's own constants
        (conditional on the manuscript's lemmas; FLOATING for logs).
Part D  heuristic "ideal-bias" ceilings and the dimension-count generalization (HEURISTIC; float).

Nothing here checks a lemma. It only checks how the lemma outputs combine.
Run: python3 -I siegel_budget.py      (standard library only; < 1 s)
"""
from fractions import Fraction as Fr
import math

checks = []
def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

print("=== Part A: manuscript constants (exact) ===")
# Corollary 4 (TeX 410-432): T1 = 32 H^{2/3} U, T2 = T3 = 32 H^{-1/3} U, U^3 = N^4.
check("Cor 4: T1*T2*T3 = 32^3 U^3 = 32768 N^4", 32**3 == 32768)
check("Cor 4: prod (T_j - 3(N-1)) >= T1T2T3/8 = 4096 N^4 > 256 N^4 > (4N-3)^4", Fr(32**3, 8) == 4096 and 4096 > 4**4)
check("Cor 4 / Sec 4: weight bound T1 + H T2 + H T3 = (32 + 2*32) H^{2/3} U = 96 H^{2/3} U", 32 + 2*32 == 96)
# Lemma 6 (TeX 517-550)
c0 = Fr(1, 4 * 97**2); C0 = Fr(192)
check("Lemma 6: c0 = 1/(4*97^2) = 1/37636", c0 == Fr(1, 37636))
check("Lemma 6: C0 = 2*96 = 192", C0 == 2 * 96)
ratio = C0 / c0
check("Lemma 6: S2/S1 <= (C0/c0)/H with C0/c0 = 7226112", ratio == 7226112)
H_paper = 12 * ratio
check("Sec 5: (C0/c0)/H <= 1/12 iff H >= 86713344 (Lean uses H := 86713344)", H_paper == 86713344)
check("Lemma 6: M >= 2 Q0 needs H^{2/3} N^{4/3} >= 2*97^2 = 18818 (Lean: 18818 <= N)", 2 * 97**2 == 18818)
kappa = Fr(3, 4)          # log N / log U, from U^3 = N^4
eps = Fr(1, 12)
first = kappa * (1 + eps)
check("Sec 5: first term of (5.1) (3/4)(1 + 1/12) = 13/16", first == Fr(13, 16))
check("Sec 5: limit 13/16 + 1/16 = 7/8 < 1", first + Fr(1, 16) == Fr(7, 8) < 1)
check("Sec 5: log M = 3 log U and log N = (3/4) log U (M = N^4 = U^3)", Fr(4, 3) * kappa == 1)

print("\n=== Part B: the contradiction condition ===")
print("""Master inequality (5.1), divided by S1 log U, in the limit q -> oo at fixed H and lambda:
   phi_adm(U)  >  kappa (1+eps)  +  c_arch (1+eps)/lambda  +  R(U)
 with  phi_adm = (admissible prime mass up to U)/log U >= 1 - C1/lambda - Cd*delta*lambda,
   kappa = log N/log U = 3/4,  eps = S2/S1 <= (C0/c0)/H,  lambda = log U / log q,
   c_arch = 1/2 (from |sqrt d| <= sqrt q),  delta = (1-beta) log q.
 => Gamma := 1 - kappa(1+eps) - R  >  (C1 + c_arch(1+eps))/lambda + Cd*delta*lambda.
 Optimal lambda* = sqrt((C1 + c_arch(1+eps))/(Cd delta));
   delta_max = Gamma^2 / (4 Cd (C1 + c_arch(1+eps))).""")
E_UP = Fr(27182819, 10**7)        # e < 2.7182819
def delta_max(Gamma, C1, Cd, c_arch, eps):
    return Gamma**2 / (4 * Cd * (C1 + c_arch * (1 + eps)))
# Explicit Lemma 2 (derived in SIEGEL_DETERMINANT.md, Sec. 2): chi(p)=+1 mass <= (e/4) l + (e/2) delta (log X)^2 / l.
Cd = E_UP / 2
C1_paper = 1 + E_UP / 4            # + sum_{p|q} log p/p <= l  (the manuscript's crude bound)
C1_refined = E_UP / 4              # sum_{p|q} log p / p = O(log log q) = o(l)
half = Fr(1, 2)
for label, C1, e_ in [("paper constants, eps=1/12", C1_paper, eps),
                      ("paper constants, eps->0", C1_paper, Fr(0)),
                      ("refined C1=e/4, eps->0", C1_refined, Fr(0))]:
    G = 1 - kappa * (1 + e_)
    dm = delta_max(G, C1, Cd, half, e_)
    lam = math.sqrt(float((C1 + half * (1 + e_)) / (Cd * dm)))
    print(f"  {label:28s}: Gamma={float(G):.4f}  delta_max >= {float(dm):.5f}  (lambda*={lam:.1f}, gamma*=3 lambda*/4={0.75*lam:.1f})")
dm_paper = delta_max(1 - kappa * (1 + eps), C1_paper, Cd, half, eps)
check("Part B: with the paper's constants and eps = 1/12, delta_max > 1/400", dm_paper > Fr(1, 400))

print("\n=== Part C: explicit c for all q >= 3, q != 8 (conditional on the manuscript) ===")
# Finite-size residual numerator R_num (divided by log U in (5.1)):
#   Mertens (Rosser-Schoenfeld 1962, (3.22)): sum_{p<=x} log p/p > log x - 1.3326 - 1/(2 log x)
#   C_H: sum_{p<=H} log p/p < log H  (RS (3.24)) ; plus log 2/2 for p = 2 (p | 2q)
#   (1+eps) log 8 from |nu(theta_n)| <= 8 N sqrt q
#   M theta(U)/S1 <= 1.01624 U M/S1 <= 1.01624/(c0 H^{2/3})   (RS: theta(x) < 1.01624 x)
#   (M/2) log M/(S1 log U) = 1.5 M/S1 <= 1.5/(c0 H^{2/3} U)  (negligible)
# For fixed q (l = log q) the best lambda gives the closed form
#   delta_M(l) = Gamma0^2 / (4 Cd (C1 + c_arch(1+eps) + R_num/l)),   Gamma0 = 1 - kappa(1+eps),
# attained at lambda = 2a/Gamma0 with a = C1 + c_arch(1+eps) + R_num/l.
def R_num(H, eps_):
    return 1.3326 + 0.5 + math.log(2) / 2 + math.log(H) + (1 + eps_) * math.log(8) + 1.01624 / (float(c0) * H ** (2 / 3))
def delta_M(l, H):
    e_ = float(ratio) / H
    G0 = 1 - 0.75 * (1 + e_)
    a = float(C1_paper) + 0.5 * (1 + e_) + R_num(H, e_) / l
    return G0**2 / (4 * float(Cd) * a), 2 * a / G0
best = None
for H in [86713344, 10**8, 3 * 10**8, 10**9, 10**10, 10**12]:
    e_ = float(ratio) / H
    if 0.75 * (1 + e_) >= 1:
        continue
    lmin = math.log(3)
    d3, lam3 = delta_M(lmin, H)
    dinf = (1 - 0.75 * (1 + e_))**2 / (4 * float(Cd) * (float(C1_paper) + 0.5 * (1 + e_)))
    print(f"  H={H:>14,d} eps={e_:.4f} R_num={R_num(H, e_):6.2f}  delta_M(q=3)={d3:.2e} (log U={lam3*lmin:.0f})  delta_M(q->oo)={dinf:.5f}")
    if best is None or d3 > best[1]:
        best = (H, d3)
print(f"  => rough explicit c (all q>=3, q!=8, conditional): c >= {best[1]:.1e} at H = {best[0]:,d}")
check("Part C: delta_M(l) is increasing in l, so its infimum over q>=3 is at q=3 (sampled)",
      all(delta_M(math.log(q), 86713344)[0] < delta_M(math.log(q + 1), 86713344)[0] for q in range(3, 200)))
check("Part C: at H = 86713344, log N = (3/4) log U >= log H at the optimal lambda for q = 3",
      0.75 * delta_M(math.log(3), 86713344)[1] * math.log(3) >= math.log(86713344))

print("\n=== Part D: heuristic ideal-bias ceilings (HEURISTIC) ===")
print("""A single real zero beta contributes  -(1 - X^{beta-1})/(1-beta) = -(l/delta)(1 - e^{-x}),  x = delta*lambda,
to sum_{p<=X} chi(p) log p/p (explicit-formula heuristic, other zeros ignored). So the inert mass up to
U = q^lambda is  I = (lambda l)/2 + (l/(2 delta))(1 - e^{-x}).  The determinant closes iff
usable mass > kappa log U + c_arch l  (leading order, eps -> 0).""")
# (i) paper: usable = inert only, kappa = 3/4: condition delta < (1 - e^{-x} - x/2)/(2 c_arch); max at x = ln 2.
for c_arch, name in [(0.5, "cube box (paper), |theta| <= 8N sqrt q"), (0.25, "anisotropic box, |theta| ~ N q^{1/4}")]:
    xs = [i / 10000 for i in range(1, 40000)]
    dmax = max((1 - math.exp(-x) - x / 2) / (2 * c_arch) for x in xs)
    closed = (1 - math.log(2)) / (4 * c_arch)
    print(f"  inert-only, n=4, {name}: delta < {dmax:.4f} (closed form (1-ln2)/(4 c_arch) = {closed:.4f})")
check("Part D: inert-only cube-box ceiling equals (1 - ln 2)/2 = 0.1534",
      abs(max((1 - math.exp(-x) - x / 2) for x in [i / 10000 for i in range(1, 40000)]) - (1 - math.log(2)) / 2) < 1e-7)
print("""  Generalization: Galois group G = (Z/2)^r, n = 2^r, coordinates S = {id} u sigma*G0 (k = n/2+1),
  kappa = k/n = 1/2 + 1/n; Siegel-biased Frobenius lies in sigma*G0 (all usable); split primes usable
  with weight 2/n. Ideal ceiling: delta < (1 - 2/n)/(2 c_arch). Codim-1 family S = G minus {g*}
  (k = n-1, the only case the TeX Lemma 3 proves): kappa = 1 - 1/n, ceiling delta < 1/(n c_arch).""")
print(f"  {'n':>4} {'k':>4} {'kappa':>8} {'margin 1-kappa':>15} {'ceil(cube)':>11} {'ceil(aniso)':>12} | {'codim-1 kappa':>13} {'ceil(cube)':>11}")
for r in range(2, 7):
    n = 2**r; k = n // 2 + 1
    kap = Fr(k, n)
    print(f"  {n:>4} {k:>4} {str(kap):>8} {str(1-kap):>15} {(1-2/n)/(2*0.5):>11.3f} {(1-2/n)/(2*0.25):>12.3f} | {str(Fr(n-1,n)):>13} {1/(n*0.5):>11.3f}")
check("Part D: n=4 is the only n where {id} u sigma G0 has codim-1 kernel (k = n-1)",
      [2**r for r in range(2, 8) if 2**r // 2 + 1 == 2**r - 1] == [4])
check("Part D: margins 1-kappa for {id} u sigma G0 increase to 1/2 and never reach it",
      all(Fr(1, 2) - Fr(1, 2**r) < Fr(1, 2) for r in range(2, 12)))
# (c) middle strip: a zero at beta <= 1 - eta contributes at most 1/eta to the log-mass bias,
# the determinant needs >= c_arch * l * (1+eps) extra usable mass.
print("\n  Middle strip: a zero at beta = 1 - eta moves sum chi(p) log p/p by at most 1/eta, hence the")
print("  usable mass by at most 1/(2 eta); the determinant needs more than c_arch*l >= l/4 extra:")
for eta in [0.5, 0.25, 0.1, 0.01]:
    print(f"    eta={eta:<5}: possible only if log q < {2/eta:.0f} (anisotropic box, zero noise, any n)")

print(f"\n{sum(ok for _, ok in checks)}/{len(checks)} checks passed")
if not all(ok for _, ok in checks):
    raise SystemExit(1)
