"""
amp_ledger.py -- exact-rational exponent ledger for amplified extraction in the Oct 5 sextic
family (README.md sections 1-5).  Exponents are base D; H = D^h rows, L = D^lam amplifier
length, M_amp <= D^e the amplified mean square, |sum_l x_l|^2 = L^(2 beta) on the principal rows.
Bookkeeping only (sympy, exact).  All asserts must pass.  Run: python3 -I amp_ledger.py
"""
from sympy import Rational as R, symbols, simplify, solve, Max, Min, nsimplify
import itertools

h, lam, e, beta, kap, delta, s, eta = symbols("h lam e beta kappa delta s eta", real=True)

def sigma(e_, h_, lam_, beta_=1):
    """Lemma A1: |A_1|^2 << M_amp / (H^{1/6} |sum x|^2)  (+ D^2 H^{-1/3} extraction error)."""
    return (e_ - h_ / 6 - 2 * beta_ * lam_) / 2

out = []
def rec(name, val):
    out.append((name, val))
    print(f"{name}: {val}")

# 0. no amplifier, Oct 5 import e = 1 + h at h -> 1+
s0 = sigma(1 + h, h, 0)
assert simplify(s0.subs(h, 1) - R(11, 12)) == 0
rec("D0 sigma(h) no amplifier", simplify(s0))

# 1. user's count: diagonal size times L^kappa at h = 1 + lam (+ row excess delta*lam)
eH = h + 1 + lam + kap * lam
s1 = simplify(sigma(eH, h, lam).subs(h, 1 + lam + delta * lam))
rec("H0 sigma at h=1+(1+delta)lam, e=h+1+(1+kappa)lam", s1)
assert simplify(s1 - (R(11, 12) + lam * (kap + R(5, 6) * delta - R(1, 6)) / 2)) == 0
rec("  break-even kappa (delta=0)", solve(s1.subs(delta, 0) - R(11, 12), kap))
rec("  break-even delta (kappa=0)", solve(s1.subs(kap, 0) - R(11, 12), delta))
assert solve(s1.subs(delta, 0) - R(11, 12), kap) == [R(1, 6)]
assert solve(s1.subs(kap, 0) - R(11, 12), delta) == [R(1, 5)]

# 2. twisted-moment route: h = 1 + s*lam (0 <= s <= 1), diagonal l = l' gives L*H*D,
#    off-diagonal sum_{l != l'} |T(l l'^5)| <= L^2 * H D * N(r)^(-eta), N(r) = L^2:
#    M_amp <= H D L^(1+kappa), kappa = max(0, 1 - 2 eta)
eT = h + 1 + lam + Max(0, 1 - 2 * eta) * lam
s2 = sigma(eT, 1 + s * lam, lam)
s2_lin = simplify((h + 1 + lam + (1 - 2 * eta) * lam - h / 6 - 2 * lam).subs(h, 1 + s * lam) / 2)
rec("TM route sigma (eta <= 1/2)", s2_lin)
assert simplify(s2_lin - (R(11, 12) + lam * (R(5, 6) * s - 2 * eta) / 2)) == 0
rec("  break-even eta(s)", solve(s2_lin - R(11, 12), eta))
assert solve(s2_lin - R(11, 12), eta) == [R(5, 12) * s]
for sv in (0, R(1, 2), 1):
    rec(f"  s={sv}: eta* =", R(5, 12) * sv)

# 3. Design (a): Moebius-compatible prime amplifier, Poisson+absorption, Cauchy-Schwarz over l,
#    imported Prop. canonical with F = L (valid iff dual rows (2+2lam-h) < 1 + lam):
#    sum_k |B^b_k|^2 <= L * (D L)^2, M_amp <= H D L + (H/(D L)) L^3 D^2 = H D L^2.
eA = h + 1 + 2 * lam
sA = simplify(sigma(eA, h, lam))
rec("Design (a) C-S + Prop canonical: e = h+1+2lam, sigma", sA)
rec("  at h = 1+lam (edge of validity)", simplify(sA.subs(h, 1 + lam)))
assert simplify(sA.subs(h, 1 + lam) - (R(11, 12) + R(5, 12) * lam)) == 0
rec("  kappa (H = D L normalisation)", 1)

# 4. Design (a'): Prop. R + quadratic large sieve per (k, l), no transfer recursion:
#    sum_l sum_k |C_l(k)|^2 <= D L (Hc + Hc^2 L / D), Hc = (D L)^2 / H (b = 1 part only)
Hc = 2 + 2 * lam - h
# M_amp <= H D L + (H/(D L)) * L * [L * D * (Hc + Hc^2 L / D)] = H D L + H L Hc + H L^2 Hc^2 / D
e_terms = [h + 1 + lam, h + lam + Hc, h + 2 * lam + 2 * Hc - 1]
e_terms = [simplify(t) for t in e_terms]
assert e_terms[1] == 2 + 3 * lam and simplify(e_terms[2] - (3 + 6 * lam - h)) == 0
rec("Design (a'') exponents of M_amp terms", e_terms)
best = None
for hv in [R(k, 40) for k in range(40, 200)]:
    for lv in [R(1, 10), R(1, 4), R(1, 2)]:
        ev = max(t.subs({h: hv, lam: lv}) for t in e_terms)
        sv = sigma(ev, hv, lv)
        if best is None or sv < best[0]:
            best = (sv, hv, lv)
rec("  min sigma over grid h in [1,5), lam in {1/10,1/4,1/2}", best)
assert best[0] > R(11, 12)

# 5. Design (b): Gauss-sum (theta-like) amplifier: dual twist unchanged (kappa >= 1 as in (a)),
#    principal value |sum_l gamma(l)|^2 = L^(2 beta), beta = 1/2 (no bias) or 5/6 (hypothetical bias)
for bv in (R(1, 2), R(5, 6)):
    sv = simplify(sigma(h + 1 + 2 * lam, h, lam, bv).subs(h, 1 + lam))
    rec(f"Design (b) beta={bv}: sigma at h=1+lam", sv)
    assert simplify(sv - R(11, 12)).subs(lam, R(1, 10)) > 0

# 6. Design (d): resonator with trivially bounded off-diagonal: |Amp|^2 <= L^2 pointwise
sD = simplify(sigma(1 + h + 2 * lam, h, lam))
rec("Design (d) trivial off-diagonal: sigma", sD)
assert simplify(sD - s0) == 0          # exactly break-even, any lam

# 7. Twist-exponent lemma: amplifier character chi_l^e; dual n-sum twisted by chi_n(l)^(1+e)
#    (own CRT/reciprocity factor) and chi_n(l')^(1-e) (partner); both trivial iff ...
tab = []
for ev in range(1, 6):
    own, partner = (1 + ev) % 6, (1 - ev) % 6
    order = lambda j: 6 // __import__("math").gcd(6, j) if j else 1
    tab.append((ev, own, order(own), partner, order(partner)))
rec("Twist table (e, own exp, own order, partner exp, partner order)", tab)
assert all(not (t[1] == 0 and t[3] == 0) for t in tab)

# 8. Q_RHO invariant: amplified polynomial length 1+lam; gap |cols - rows| at h
rec("gap |cols-rows| for amplified family", simplify(abs(1 + lam - h)))

# 9. GRH-consistency of TM_eta: random-model |T(r)| ~ D sqrt(H) (plus principal H^(1/6)|A_1|^2):
#    D^{1+h/2} <= H D N(r)^(-eta) iff eta <= h/(4 lam) (N(r) = L^2)
rec("TM_eta GRH-consistent range (h=1, N(r)=L^2)", "eta <= 1/(4 lam)")

# 10. Round 2: the j = 4 design (plain prime amplifier e = 1; R3 law B_{p,4} = Ramanujan, cost N(l)).
#     Post-reflection, rows k <= Hd = D L^(1-delta) (H = D L^(1+delta)), P-normalised target D L^(1+kappa).
#     Column counts J (base-L exponents above D): per-l reflected length qY = L Hd^2/D, l in [1, L].
from sympy import Piecewise, minimum, Interval, oo
dl = symbols("delta_", nonnegative=True)
def best_sigma(kappa_expr, name):
    f = kappa_expr + R(5, 6) * dl          # sigma = 11/12 + lam*(f - 1/6)/2
    cands = [R(k, 120) for k in range(0, 721)]
    vals = [(f.subs(dl, c), c) for c in cands]
    m, at = min(vals, key=lambda t: t[0])
    rec(f"{name}: min over delta of kappa+5delta/6 = {m} at delta = {at}; sigma = 11/12 + lam*({m - R(1, 6)})/2", "")
    return m, at
# (i) C-S over l + QLS per l (Prop. R with j=4 cost):  L Hd + L^2 Hd^2/D  ->  kappa = max(0, 1-delta, 3-2delta)
mi, _ = best_sigma(Max(0, 1 - dl, 3 - 2 * dl), "J4 (i) C-S + QLS per l")
# (ii) optimal row-blind joint sieve over (k; l, n'): Hd + L^2 Hd^2/D -> kappa = max(0, -delta, 3-2delta)
mii, _ = best_sigma(Max(0, -dl, 3 - 2 * dl), "J4 (ii) optimal joint sieve, rows+columns")
# (ii') same, if the j=4 congruence were free and no phase survived: Hd + L Hd^2/D
mfree, _ = best_sigma(Max(0, -dl, 2 - 2 * dl), "J4 (ii') cost-free congruence, no phase")
# ideal: single smooth column m of length D L (not available): Hd + Hd^2/(D L)
mid, _ = best_sigma(Max(0, -dl, -2 * dl), "ideal single-variable reflection (not available)")
assert mi == R(5, 4) and mii == R(5, 4) and mfree == R(5, 6) and mid == 0
assert mi > R(1, 6) and mii > R(1, 6) and mfree > R(1, 6) and mid < R(1, 6)
# Infeasibility: no delta >= 0 with max(0, 3 - 2 delta) + 5 delta/6 < 1/6 (any row-blind joint sieve has norm >= #columns)
# branch delta >= 3/2: 5 delta/6 < 1/6 => delta < 1/5 (contradiction); branch delta < 3/2: 3 - 7 delta/6 < 1/6 => delta > 17/7 (contradiction)
assert solve(R(5, 6) * dl - R(1, 6), dl) == [R(1, 5)] and solve(3 - R(7, 6) * dl - R(1, 6), dl) == [R(17, 7)]
rec("J4 required saving below the column count at delta=0 (base L)", R(4) - (1 + R(1, 6)))

with open(__import__("os").path.join(__import__("os").path.dirname(__import__("os").path.abspath(__file__)),
                                      "results", "amp_ledger.out"), "w") as fh:
    for n, v in out:
        fh.write(f"{n}: {v}\n")
print("all asserts passed")
