#!/usr/bin/env python3
"""Kintali QRH (7 Oct 2026): what a better Hecke zero-density input buys, in exact rationals.

Companion to ../KINTALI_DENSITY_UPGRADE.md.  Arithmetic class: EXACT_RATIONAL (fractions.Fraction;
sympy only for the closed-form cross-checks).  Run:  python3 -I kintali_density_upgrade.py

Model (taken from [K] Sec. 4.1, eq. (16), and Sec. 4.4, Lemma 7; see the review
../reviews/KINTALI_REVIEW.md Sec. 4):

  * a row bin with label a (a finite set of labels in [51/100, beta*]) has
        #B_a << U^{R(a)+delta} (3+T)^A,   R(a) = min(1, g(a)),
    where g(sigma) is the CONDUCTOR (Q-) exponent of a zero-density bound
        sum_{N f <= Q} sum*_{psi mod f} N(sigma, T, psi) << Q^{g(sigma)+eps} T^B
    for the primitive finite-order Hecke characters of K = Q(sqrt(-3)).  Any fixed T-power B is
    allowed, because [K] takes T = 3 Z^tau with tau <= m0/(4(A+1)) AFTER A is fixed.
  * at the worst dyad d = 1/2 the saving is E(1/2, a) = a - beta* + R(a)/2 - 1/3, so the high side
    certifies every b > bstar(g) := sup_a [a + min(1, g(a))/2 - 1/3];
  * the low side (J << Z^{1/4+eps}) and |H_eta| >= 1/2 cap the architecture at 11/12;
  * [K] states b = 47/48 = 29/30 + 1/80 (a generous margin; see the .md for what it absorbs).

Every g used below is a minimum of bounds of the form  c (1 - s) / (p + q s)  valid on [s0, 1].
On each such piece  s + g(s)/2  is strictly decreasing for s in [1/2, 1] (checked below), and the
validity ranges only start (never end) as s increases, so the supremum is reached as s increases to
    sigma_1(g) := sup{ s : g(s) >= 1 },   and   bstar(g) = sigma_1(g) + 1/6.
The script computes bstar both by this formula and by a direct exact search (candidate points plus
left limits, then a rational grid), and asserts that they agree.
"""
from fractions import Fraction as F
import sympy as sp

ONE, HALF, THIRD, SIXTH = F(1), F(1, 2), F(1, 3), F(1, 6)
LO = F(51, 100)          # detector floor in [K]
CAP = F(11, 12)          # low-side cap of the architecture
KMARGIN = F(1, 80)       # [K]'s margin: 47/48 - 29/30

# ---------------------------------------------------------------------------------------------
# A bound is (name, c, p, q, s0, status): g(s) = c (1-s)/(p + q s) on s0 <= s <= 1.
# Q-exponent convention: a bound (Q^2 T^a)^{A(s)(1-s)} has Q-exponent 2 A(s) (1-s).
# ---------------------------------------------------------------------------------------------
def bound(name, c, p, q, s0, status):
    return dict(name=name, c=F(c), p=F(p), q=F(q), s0=F(s0), status=status)

def gval(b, s):
    return b["c"] * (1 - s) / (b["p"] + b["q"] * s)

# Hecke characters of K (n = 2): published, power-uniform in the conductor
HINZ_A = bound("Hinz 1976 Satz A: (Q^2 T^b)^{3(1-s)/(2-s)}", 6, 2, -1, HALF, "PUBLISHED (Hecke, any K)")
HINZ_B = bound("Hinz 1976 Satz B: (Q^2 T^n)^{2(1-s)/s}, s>=3/4", 4, 0, 1, F(3, 4), "PUBLISHED (Hecke, any K)")
K_CONST = bound("[K] as written: 2h(a) <= 5, i.e. g = 5(1-s)", 5, 1, 0, HALF, "[K] display (16)")
# Dirichlet characters over Q (K = Q): published; NO Hecke analogue located
HUX76 = bound("Huxley 1976: (Q^2 T^2)^{(20/9)(1-s)}", F(40, 9), 1, 0, HALF, "PUBLISHED for Dirichlet only")
HB79_2 = bound("Heath-Brown 1979 Thm 2(2): (Q^2 T^{6/5})^{5(1-s)/(3-s)}", 10, 3, -1, HALF, "PUBLISHED for Dirichlet only")
JUT77 = bound("Jutila 1977: (Q^2 T^2)^{2(1-s)}, s>=7/9", 4, 1, 0, F(7, 9), "PUBLISHED for Dirichlet only")
HB79_3 = bound("Heath-Brown 1979 Thm 3: (Q^2 T^2)^{2(1-s)}, s>=129/167", 4, 1, 0, F(129, 167), "PUBLISHED for Dirichlet only")
HB79_1 = bound("Heath-Brown 1979 Thm 1: (Q^2 T)^{2(1-s)}, s>=11/14", 4, 1, 0, F(11, 14), "PUBLISHED for Dirichlet only")
# Hypothetical
DH_Q = bound("Q-aspect DH on [3/4,1]: Q^{4(1-s)} T^B", 4, 1, 0, F(3, 4), "HYPOTHETICAL (not located for Hecke; for Dirichlet located only on [129/167,1])")

SCENARIOS = [
    ("S0 [K] as written (A = 5/2 constant)", [K_CONST]),
    ("S1 Hinz Satz A only", [HINZ_A]),
    ("S2 Hinz Satz B only (s >= 3/4; trivial below)", [HINZ_B]),
    ("S3 Hinz Satz A + B (sigma-dependent h)", [HINZ_A, HINZ_B]),
    ("S4 + Huxley 1976 analogue", [HINZ_A, HINZ_B, HUX76]),
    ("S5 + Heath-Brown 1979 Thm 2 analogue", [HINZ_A, HINZ_B, HUX76, HB79_2]),
    ("S6 + Jutila 1977 analogue", [HINZ_A, HINZ_B, HUX76, HB79_2, JUT77]),
    ("S7 + Heath-Brown 1979 Thm 1 and Thm 3 analogues", [HINZ_A, HINZ_B, HUX76, HB79_2, JUT77, HB79_1, HB79_3]),
    ("S8 hypothetical Q-aspect DH on [3/4,1]", [HINZ_A, HINZ_B, DH_Q]),
]

def gstar(bounds, s):
    """Best available Q-exponent at s, or None if no bound is valid (then R = 1, trivial count)."""
    vals = [gval(b, s) for b in bounds if b["s0"] <= s <= 1]
    return min(vals) if vals else None

def Rfun(bounds, s):
    g = gstar(bounds, s)
    return ONE if g is None else min(ONE, g)

def Fobj(bounds, s):
    return s + Rfun(bounds, s) / 2 - THIRD

def sigma1(bounds):
    """sup{s in [LO,1): gstar(s) >= 1 or no bound valid}, exactly.

    Candidates: LO, every validity start s0, every root of g_i = 1 (linear in s)."""
    cands = {LO}
    for b in bounds:
        cands.add(b["s0"])
        # c(1-s) = p + q s  ->  s = (c - p)/(c + q)
        den = b["c"] + b["q"]
        if den != 0:
            r = (b["c"] - b["p"]) / den
            if LO <= r < 1:
                cands.add(r)
    # sigma_1 is the largest candidate x such that g >= 1 holds on a left-neighbourhood of x
    best = LO
    for x in sorted(cands):
        eps = F(1, 10**9)
        if x - eps >= LO and (gstar(bounds, x - eps) is None or gstar(bounds, x - eps) >= 1):
            best = max(best, x)
    return best

def bstar_direct(bounds, grid_den=20000):
    """Direct exact search: candidate points with left limits, then a rational grid."""
    s1 = sigma1(bounds)
    cands = {LO, s1, F(1) - F(1, 10**6)}
    for b in bounds:
        cands.add(b["s0"])
    best = max(Fobj(bounds, x) for x in cands if LO <= x < 1)
    # left limit at each candidate (sup may be unattained)
    leftlim = max((x + SIXTH for x in cands if LO < x < 1
                   and (gstar(bounds, x - F(1, 10**12)) is None or gstar(bounds, x - F(1, 10**12)) >= 1)),
                  default=best)
    best = max(best, leftlim)
    # grid sanity check: no grid point exceeds the claimed supremum
    grid_max = max(Fobj(bounds, LO + F(k, grid_den) * (1 - LO)) for k in range(grid_den))
    assert grid_max <= best, (grid_max, best)
    return best, grid_max

def monotone_check(bounds):
    """d/ds [s + g(s)/2] < 0 on [1/2, 1] for each piece: exact via sympy on the closed interval."""
    s = sp.symbols("s", real=True)
    for b in bounds:
        g = sp.Rational(b["c"]) * (1 - s) / (sp.Rational(b["p"]) + sp.Rational(b["q"]) * s)
        dF = sp.simplify(sp.diff(s + g / 2, s))
        # dF is a rational function; check its sup on [1/2,1] is < 0 by sampling critical points
        crit = [c for c in sp.solve(sp.diff(dF, s), s) if c.is_real and sp.Rational(1, 2) <= c <= 1]
        pts = [sp.Rational(1, 2), sp.Integer(1)] + crit
        mx = max(dF.subs(s, x) for x in pts)
        assert mx < 0, (b["name"], dF, mx)

def dslope_ok(bounds):
    """[K] Lemma 7 uses E(d,a) increasing in d (slope R(a)+a-21/25 > 0). If the slope were negative,
    the worst dyad is d=0, where E(0,a) = a/2 - beta* + 13/150 < 0 anyway. Report the slope range."""
    pts = [LO + F(k, 2000) * (1 - LO) for k in range(2000)]
    sl = [Rfun(bounds, a) + a - F(21, 25) for a in pts]
    return min(sl), max(sl)

def required_A(b, s):
    """Largest constant A (Kintali normalization, Q-exponent 2A(1-s)) allowed at s for target b:
    need 2A(1-s) < 2(b + 1/3 - s) when s > b - 1/6 (nothing is needed for s <= b - 1/6)."""
    return (b + THIRD - s) / (1 - s)

def main():
    print("== closed form for a constant exponent A:  bstar = 7/6 - 1/(2A) ==")
    A = sp.symbols("A", positive=True)
    print("  sigma_1 = 1 - 1/(2A); bstar =", sp.simplify(1 - 1 / (2 * A) + sp.Rational(1, 6)))
    for Aval in (F(5, 2), F(12, 5), F(7, 3), F(20, 9), F(2)):
        print(f"  A = {Aval}: bstar = {F(7, 6) - 1 / (2 * Aval)}  (= {float(F(7, 6) - 1 / (2 * Aval)):.6f})")

    all_bounds = {id(b): b for _, bs in SCENARIOS for b in bs}.values()
    monotone_check(list(all_bounds))
    print("\n== monotonicity: s + g(s)/2 strictly decreasing on [1/2,1] for every piece: OK ==")

    print("\n== scenarios ==")
    results = {}
    for name, bs in SCENARIOS:
        s1 = sigma1(bs)
        bst, gm = bstar_direct(bs)
        assert bst == s1 + SIXTH, (name, bst, s1)
        eff = max(CAP, bst)
        smin, smax = dslope_ok(bs)
        results[name] = (s1, bst, eff)
        print(f"{name}")
        for b in bs:
            print(f"    - {b['name']}  [{b['status']}]")
        print(f"    sigma_1 = {s1} (~{float(s1):.6f});  bstar = sigma_1 + 1/6 = {bst} (~{float(bst):.6f})")
        print(f"    boundary max(11/12, bstar) = {eff} (~{float(eff):.6f});  with [K]'s 1/80 margin: "
              f"{eff + KMARGIN} (~{float(eff + KMARGIN):.6f});  grid max = {float(gm):.6f}")
        print(f"    d-slope R(a)+a-21/25 on [51/100,1): [{float(smin):.4f}, {float(smax):.4f}]")

    # Pinned values
    assert results["S0 [K] as written (A = 5/2 constant)"][1] == F(29, 30)
    assert results["S3 Hinz Satz A + B (sigma-dependent h)"][1] == F(29, 30)
    assert results["S4 + Huxley 1976 analogue"][1] == F(113, 120)
    assert results["S6 + Jutila 1977 analogue"][1] == F(113, 120)
    assert results["S7 + Heath-Brown 1979 Thm 1 and Thm 3 analogues"][1] == F(941, 1002)
    assert results["S8 hypothetical Q-aspect DH on [3/4,1]"][2] == F(11, 12)
    assert F(29, 30) + KMARGIN == F(47, 48)

    print("\n== where each bound first beats the row count (g(s) = 1) ==")
    for b in (HINZ_A, HINZ_B, HUX76, HB79_2, JUT77, HB79_3, DH_Q):
        r = (b["c"] - b["p"]) / (b["c"] + b["q"])
        valid = max(r, b["s0"])
        print(f"  {b['name']}: g=1 at s={r} (~{float(r):.6f}); g<1 on ({valid}, 1] "
              f"(validity starts at {b['s0']})")
    print("  Note: 31/40 =", float(F(31, 40)), " 7/9 =", float(F(7, 9)), " 129/167 =", float(F(129, 167)),
          " -> Jutila's 7/9 lies right of Huxley's 31/40, so it does not move sigma_1; 129/167 does.")

    print("\n== required Kintali-normalized A(s) for target b (need A(s) < (b+1/3-s)/(1-s) on (b-1/6, 1)) ==")
    for b in (F(11, 12), F(941, 1002), F(113, 120), F(29, 30)):
        row = []
        for s in sorted({b - SIXTH, F(4, 5), F(17, 20), F(9, 10), F(19, 20)}):
            if s > b - SIXTH - F(1, 10**9) and s < 1:
                row.append(f"s={s}: {float(required_A(b, s)):.4f}")
        print(f"  b={b} (~{float(b):.5f}): window ({b - SIXTH}, 1);  " + ";  ".join(row))
    print("  Available constant-A values for comparison: Hinz 5/2 at s=4/5 (h(s) peaks exactly there),"
          " Huxley-analogue 20/9 = 2.2222, DH 2.")

    print("\n== sanity: [K]'s own arithmetic ==")
    print("  47/48 - 29/30 =", F(47, 48) - F(29, 30), "; E(1/2,a) < -1/80 then +1/1000 for d <= 501/1000:",
          F(-1, 80) + F(1, 1000))

if __name__ == "__main__":
    main()
