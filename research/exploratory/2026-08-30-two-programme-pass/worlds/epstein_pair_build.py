"""World build: epstein_pair — two binary-quadratic-form Epstein zetas as one
world with two sub-rows:

  Q1 = x^2 + y^2        (disc  -4, class number h(-4)  = 1, the CM/arithmetic
                         sublocus: Z_Q1(s) = 4 zeta(s) L(s, chi_-4))
  Q2 = x^2 + 5 y^2      (disc -20, class number h(-20) = 2, the generic
                         member: NO Euler product; Davenport-Heilbronn
                         off-line zeros imported)

Everything conclusion-bearing here is EXACT (Python ints and Fractions; no
floating point anywhere in this script).  What is computed and asserted:

  * representation numbers r_Q(n) for n <= 400 for THREE forms (Q1, Q2 and
    Q2' = 2x^2 + 2xy + 3y^2, the genus partner of Q2) by exhaustive integer
    search with proved box bounds, cross-validated against an independent
    per-n quadratic-formula counter;
  * Jacobi's two-squares identity r_Q1(n) = 4 sum_{d|n} chi_-4(d) for ALL
    1 <= n <= 400 (finite witness PROVED_HERE; the identity for all n is
    imported: Jacobi 1829);
  * EXACT non-multiplicativity witnesses for Q2: r_Q2(2) = r_Q2(3) = 0 but
    r_Q2(6) = 4, refuting multiplicativity of c * r_Q2 for EVERY nonzero
    scalar c (in particular the /4-normalization: r(6)/4 = 1 != 0 =
    (r(2)/4)(r(3)/4)); exhaustive failure tallies over all coprime pairs;
  * the genus identity r_Q2(n) + r_Q2'(n) = 2 sum_{d|n} chi_-20(d) for all
    n <= 400 — averaging over the genus RESTORES multiplicativity exactly;
  * the full genus-character decomposition, coefficientwise for n <= 400:
        r_Q2(n)  = (1 * chi_-20)(n) + (chi_-4 * chi_5)(n)
        r_Q2'(n) = (1 * chi_-20)(n) - (chi_-4 * chi_5)(n)
    (Dirichlet convolutions), i.e. Z_Q2 = zeta L(chi_-20) + L(chi_-4)L(chi_5)
    at the level of the first 400 coefficients: a SUM of two Euler products,
    not an Euler product;
  * class numbers h(-4) = 1 and h(-20) = 2 by exhaustive enumeration of
    reduced forms;
  * splitting laws (finite instances): #{x mod p : x^2 = -1}  = 1 + chi_-4(p)
    for all odd p <= 400 and #{x mod p : x^2 = -20} = 1 + chi_-20(p) for all
    odd p <= 400 (p = 5 ramified included);
  * detector battery (core.reconstruct.detect) runs:
      - Q1 local factors certified (A1-A5) at p = 2, 5, 13, and at the inert
        primes 3, 7 factorwise (zeta-factor and chi_-4-factor separately);
      - Q2 raw prime-power slices: p = 2 and the split-principal p = 29 are
        rational and effective, but the split-NONprincipal primes 3 and 7
        are REFUSED at A2_EFFECTIVITY (virtual numerator 1 + T^2) — the
        principal-form slice is not an effective Euler factor;
      - both Hecke constituents of Q2 certified locally (zeta_K slice and
        genus-character psi slice, all axioms HOLD);
      - cross-prime refutation: the would-be Euler assembly of the certified
        Q2 slices predicts coefficient 0 at n = 6 and n = 14; the true
        values are 2 (normalization r/2) — local rationality does NOT
        assemble into a global Euler product.

RH/GRH is NOT established by anything here.  critical_line for the pair is
FALSE for the generic member Q2 (imported: Davenport-Heilbronn), while the
Q1 sub-row is CONJECTURE (equivalent to RH for zeta and GRH for L(chi_-4));
the record embeds rh_established = false.

Deterministic: no input, no randomness, exact arithmetic only.  Re-run with
    python3 -m worlds.epstein_pair_build
from the pass root to regenerate worlds/epstein_pair.json and the sibling
data file worlds/epstein_pair_data.json identically.
"""

import json
import os
from fractions import Fraction
from math import gcd, isqrt

from core.exact import (
    F, poly_mul, minimal_rational_form, series_of_rational,
    power_sums_from_satake, satake_poly_from_power_sums,
    coefficient_sequence_from_satake, op_direct_sum,
)
from core.reconstruct import detect, tensor_compatibility, HOLDS, FAILS, SKIPPED
from core.worlds import cell, save_world, validate_world


N = 400          # exhaustive representation-number range
W1 = 10          # detector window, Q1 local factors
W2 = 14          # detector window, Q2 slices at p = 2, 3, 7
W29 = 9          # detector window, Q2 slice at p = 29 (29^8 ~ 5e11 is enough)
HOLDOUT = 3      # A5 held-out tail length


# ---------------------------------------------------------------------------
# The three forms.  Q(x, y) = a x^2 + b x y + c y^2, disc D = b^2 - 4ac < 0.
# ---------------------------------------------------------------------------

FORM_Q1 = (1, 0, 1)     # x^2 + y^2,           D = -4
FORM_Q2 = (1, 0, 5)     # x^2 + 5y^2,          D = -20
FORM_Q2B = (2, 2, 3)    # 2x^2 + 2xy + 3y^2,   D = -20 (genus partner of Q2)


def disc(form):
    a, b, c = form
    return b * b - 4 * a * c


def assert_positive_definite(form):
    """Exact positive-definiteness + box-bound identities, as INTEGER
    coefficient identities (no numerics):
        4a Q(x,y) = (2ax + by)^2 + |D| y^2     and
        4c Q(x,y) = (bx + 2cy)^2 + |D| x^2.
    Checked by expanding both sides coefficientwise in Z[x, y]."""
    a, b, c = form
    D = disc(form)
    assert a > 0 and D < 0
    absD = -D
    # identity 1: 4a*Q(x,y) = (2ax+by)^2 + |D| y^2, coefficientwise in Z[x,y]
    #   x^2:  4a*a  == (2a)^2
    #   x y:  4a*b  == 2*(2a)*b
    #   y^2:  4a*c  == b^2 + |D|
    assert 4 * a * a == (2 * a) ** 2
    assert 4 * a * b == 2 * (2 * a) * b
    assert 4 * a * c == b * b + absD
    # identity 2: 4c*Q(x,y) = (bx+2cy)^2 + |D| x^2, coefficientwise in Z[x,y]
    #   x^2:  4c*a  == b^2 + |D|
    #   x y:  4c*b  == 2*b*(2c)
    #   y^2:  4c*c  == (2c)^2
    assert 4 * c * a == b * b + absD
    assert 4 * c * b == 2 * b * (2 * c)
    assert 4 * c * c == (2 * c) ** 2


def rep_table(form, N):
    """r_Q(n) for 0 <= n <= N by exhaustive search.  Box bounds are proved by
    the identities in assert_positive_definite: Q(x,y) <= N forces
    y^2 <= 4aN/|D| and x^2 <= 4cN/|D| (both sides integers, so the floor
    isqrt bound is exact)."""
    a, b, c = form
    absD = -disc(form)
    xb = isqrt((4 * c * N) // absD)
    yb = isqrt((4 * a * N) // absD)
    t = [0] * (N + 1)
    for x in range(-xb, xb + 1):
        for y in range(-yb, yb + 1):
            v = a * x * x + b * x * y + c * y * y
            if v <= N:
                t[v] += 1
    return t


def count_reps(form, n):
    """r_Q(n) for a single (possibly large) n, independent method: for each
    admissible y solve the exact integer quadratic a x^2 + (by) x +
    (c y^2 - n) = 0 via its discriminant D y^2 + 4an and isqrt."""
    a, b, c = form
    D = disc(form)
    absD = -D
    total = 0
    yb = isqrt((4 * a * n) // absD)
    for y in range(-yb, yb + 1):
        d = D * y * y + 4 * a * n
        if d < 0:
            continue
        s = isqrt(d)
        if s * s != d:
            continue
        if s == 0:
            if (-b * y) % (2 * a) == 0:
                total += 1
        else:
            for num in (-b * y + s, -b * y - s):
                if num % (2 * a) == 0:
                    total += 1
    return total


# ---------------------------------------------------------------------------
# Exact quadratic characters (integer-valued, defined for arbitrary ints >= 0)
# ---------------------------------------------------------------------------

def chi_m4(n: int) -> int:
    """Kronecker character mod 4 attached to Q(i): chi_-4."""
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def chi_5(n: int) -> int:
    """Legendre symbol (n|5) (the even quadratic character mod 5)."""
    m = n % 5
    if m == 0:
        return 0
    return 1 if m in (1, 4) else -1


def chi_m20(n: int) -> int:
    """Kronecker character mod 20 attached to Q(sqrt(-5)): chi_-4 * chi_5."""
    return chi_m4(n) * chi_5(n)


def divisors(n: int) -> list:
    small, large = [], []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def dsum(chi, n: int) -> int:
    return sum(chi(d) for d in divisors(n))


def conv(chiA, chiB, n: int) -> int:
    return sum(chiA(d) * chiB(n // d) for d in divisors(n))


def primes_upto(N: int) -> list:
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i * i <= N:
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False
        i += 1
    return [p for p in range(2, N + 1) if sieve[p]]


# ---------------------------------------------------------------------------
# Reduced-form enumeration (exact class numbers)
# ---------------------------------------------------------------------------

def reduced_forms(D: int) -> list:
    """All reduced positive definite integral binary quadratic forms of
    discriminant D < 0: |b| <= a <= c, b = D mod 2, b >= 0 if |b| = a or
    a = c.  Exhaustive over the proved bound a <= sqrt(|D|/3)."""
    assert D < 0 and D % 4 in (0, 1)
    out = []
    for a in range(1, isqrt((-D) // 3) + 1):
        for b in range(-a, a + 1):
            if (b - D) % 2:
                continue
            num = b * b - D
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if c < a:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            out.append((a, b, c))
    return out


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def main():
    # =====================================================================
    # 0.  Exact representation tables + cross-validation of two counters
    # =====================================================================
    for form in (FORM_Q1, FORM_Q2, FORM_Q2B):
        assert_positive_definite(form)
    assert disc(FORM_Q1) == -4 and disc(FORM_Q2) == -20 and disc(FORM_Q2B) == -20

    r1 = rep_table(FORM_Q1, N)
    r2 = rep_table(FORM_Q2, N)
    r2b = rep_table(FORM_Q2B, N)
    for n in range(N + 1):
        assert r1[n] == count_reps(FORM_Q1, n), n
        assert r2[n] == count_reps(FORM_Q2, n), n
        assert r2b[n] == count_reps(FORM_Q2B, n), n

    # spot values (hand-checkable)
    assert (r1[0], r1[1], r1[2], r1[4], r1[5], r1[25]) == (1, 4, 4, 4, 8, 12)
    assert (r2[0], r2[1], r2[2], r2[3], r2[4], r2[5]) == (1, 2, 0, 0, 2, 2)
    assert (r2[6], r2[9], r2[14], r2[21], r2[29]) == (4, 6, 4, 8, 4)
    assert (r2b[1], r2b[2], r2b[3], r2b[7]) == (0, 2, 4, 4)

    # unit divisibility: 4 | r_Q1(n), 2 | r_Q2(n), 2 | r_Q2'(n) for n >= 1
    for n in range(1, N + 1):
        assert r1[n] % 4 == 0 and r2[n] % 2 == 0 and r2b[n] % 2 == 0, n

    # =====================================================================
    # 1.  Characters: literal period tables + complete multiplicativity
    # =====================================================================
    assert [chi_m4(n) for n in range(4)] == [0, 1, 0, -1]
    assert [chi_5(n) for n in range(5)] == [0, 1, -1, -1, 1]
    assert [chi_m20(n) for n in range(20)] == \
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1]
    for m in range(1, N + 1):
        for n in range(1, N + 1):
            assert chi_m4(m * n) == chi_m4(m) * chi_m4(n)
            assert chi_5(m * n) == chi_5(m) * chi_5(n)
            assert chi_m20(m * n) == chi_m20(m) * chi_m20(n)

    d4 = [0] + [dsum(chi_m4, n) for n in range(1, N + 1)]
    d20 = [0] + [dsum(chi_m20, n) for n in range(1, N + 1)]
    b_psi = [0] + [r2[n] - d20[n] for n in range(1, N + 1)]

    # =====================================================================
    # 2.  Q1: Jacobi's identity, exact for all n <= 400
    # =====================================================================
    for n in range(1, N + 1):
        assert r1[n] == 4 * d4[n], n
    jacobi_witness = (
        f"r_Q1(n) = 4 sum_(d|n) chi_-4(d) verified exactly for ALL "
        f"1 <= n <= {N} (two independent exact counters agree on r_Q1); "
        "hence Z_Q1(s) = 4 zeta(s) L(s, chi_-4) coefficientwise to n = 400; "
        "the identity for all n is imported (Jacobi 1829, two-squares "
        "theorem)")

    # Q1 normalized multiplicativity: zero failures over all coprime pairs
    q1_pairs = q1_fail = 0
    for m in range(2, N + 1):
        for n in range(m, N // m + 1):
            if m * n > N or gcd(m, n) != 1:
                continue
            q1_pairs += 1
            if 4 * r1[m * n] != r1[m] * r1[n]:
                q1_fail += 1
    assert q1_fail == 0 and q1_pairs > 0

    # =====================================================================
    # 3.  Q2: exact non-multiplicativity witnesses (the L1/L2 FAILS core)
    # =====================================================================
    assert r2[2] == 0 and r2[3] == 0 and r2[6] == 4
    # /4-normalization instance (as posed):
    assert Fraction(r2[6], 4) == 1 and Fraction(r2[2], 4) * Fraction(r2[3], 4) == 0
    # /2-normalization (r_Q2(1) = 2) instance:
    assert Fraction(r2[6], 2) == 2 and Fraction(r2[2], 2) * Fraction(r2[3], 2) == 0
    # any-normalization argument: for every scalar c != 0,
    # c*r(6) = 4c != 0 = (c*r(2))(c*r(3)).  Witnessed by the integers alone.

    q2_pairs = q2_fail_4 = q2_fail_2 = q2_fail_bothpos = 0
    first_fail = None
    for m in range(2, N + 1):
        for n in range(m, N // m + 1):
            if m * n > N or gcd(m, n) != 1:
                continue
            q2_pairs += 1
            if 4 * r2[m * n] != r2[m] * r2[n]:
                q2_fail_4 += 1
            if 2 * r2[m * n] != r2[m] * r2[n]:
                q2_fail_2 += 1
                if first_fail is None:
                    first_fail = (m, n)
                if r2[m] > 0 and r2[n] > 0:
                    q2_fail_bothpos += 1
    assert q2_fail_2 > 0 and q2_fail_4 > 0
    assert first_fail == (2, 3), first_fail
    nonmult_witness = (
        "EXACT witness: r_Q2(2) = 0, r_Q2(3) = 0, r_Q2(6) = 4 with "
        "gcd(2,3) = 1.  This refutes multiplicativity of c*r_Q2 for EVERY "
        "nonzero scalar normalization c (LHS c*4 != 0 = RHS); in the posed "
        "/4-normalization: r(6)/4 = 1 != 0 = (r(2)/4)(r(3)/4).  Exhaustive "
        f"tally over all {q2_pairs} unordered coprime pairs 2 <= m <= n, "
        f"mn <= {N}: {q2_fail_2} failures of 2 r(mn) = r(m) r(n) "
        f"(= the r/2 unit normalization; {q2_fail_bothpos} with both "
        f"factors nonzero, e.g. none needed), {q2_fail_4} failures of the "
        "/4 normalization; first failing pair (2, 3).  Structural reason "
        "(classical): 2 and 3 are represented by the OTHER class of the "
        "genus (2x^2+2xy+3y^2: r_Q2'(2) = 2, r_Q2'(3) = 4) while their "
        "product 6 is represented by the principal form")

    # Q1 control: the same scan found ZERO failures for r_Q1/4
    control_witness = (
        f"control on the CM locus: the identical scan over all {q1_pairs} "
        f"coprime pairs found 0 failures of 4 r_Q1(mn) = r_Q1(m) r_Q1(n)")

    # =====================================================================
    # 4.  Genus identity + full genus-character decomposition (n <= 400)
    # =====================================================================
    for n in range(1, N + 1):
        assert r2[n] + r2b[n] == 2 * d20[n], n
        assert b_psi[n] == conv(chi_m4, chi_5, n), n
        assert r2[n] == d20[n] + b_psi[n], n
        assert r2b[n] == d20[n] - b_psi[n], n
    genus_witness = (
        f"genus identity r_Q2(n) + r_Q2'(n) = 2 sum_(d|n) chi_-20(d) "
        f"verified exactly for all 1 <= n <= {N} (Q2' = 2x^2+2xy+3y^2, the "
        "second reduced class of disc -20): averaging over the genus/family "
        "RESTORES multiplicativity exactly")
    decomp_witness = (
        "full genus-character decomposition, coefficientwise for all "
        f"n <= {N}: r_Q2 = (1 * chi_-20) + (chi_-4 * chi_5) and "
        "r_Q2' = (1 * chi_-20) - (chi_-4 * chi_5) (Dirichlet convolutions, "
        "exact).  I.e. Z_Q2(s) = zeta(s) L(s, chi_-20) + "
        "L(s, chi_-4) L(s, chi_5): a SUM of two Euler products sharing "
        "gamma factor and conductor data — not itself an Euler product.  "
        "The psi-part b(n) = r_Q2(n) - (1*chi_-20)(n) IS multiplicative "
        "(it is a convolution of completely multiplicative characters); "
        "global identification with the class-group/genus character of "
        "Q(sqrt(-5)) is imported (Gauss genus theory / Kronecker factor "
        "formula; Hecke L-functions)")
    # b_psi multiplicativity: zero failures (b(1) = 1)
    assert b_psi[1] == 1
    for m in range(2, N + 1):
        for n in range(m, N // m + 1):
            if m * n > N or gcd(m, n) != 1:
                continue
            assert b_psi[m * n] == b_psi[m] * b_psi[n], (m, n)
            assert d20[m * n] == d20[m] * d20[n], (m, n)

    # =====================================================================
    # 5.  Class numbers by exhaustive reduced-form enumeration
    # =====================================================================
    assert reduced_forms(-4) == [(1, 0, 1)]
    assert reduced_forms(-20) == [(1, 0, 5), (2, 2, 3)]
    class_witness = (
        "exhaustive reduced-form enumeration (|b| <= a <= c <= over the "
        "proved bound a <= sqrt(|D|/3)): disc -4 has exactly one reduced "
        "form (1,0,1), h(-4) = 1; disc -20 has exactly two, (1,0,5) and "
        "(2,2,3), h(-20) = 2.  Bijection reduced forms <-> classes is "
        "imported (Gauss 1801)")

    # =====================================================================
    # 6.  Splitting laws (finite exact instances of the field realizations)
    # =====================================================================
    odd_primes = [p for p in primes_upto(N) if p != 2]
    for p in odd_primes:
        assert sum(1 for x in range(p) if (x * x + 1) % p == 0) \
            == 1 + chi_m4(p), p
        assert sum(1 for x in range(p) if (x * x + 20) % p == 0) \
            == 1 + chi_m20(p), p
    split_witness = (
        f"splitting laws verified exactly for all {len(odd_primes)} odd "
        f"primes p <= {N}: #(x mod p : x^2 = -1) = 1 + chi_-4(p) and "
        "#(x mod p : x^2 = -20) = 1 + chi_-20(p) (p = 5 ramified included, "
        "1 root); finite instances of the splitting of p in Q(i) and "
        "Q(sqrt(-5)) — chi_-4 and chi_-20 are the field characters")

    # =====================================================================
    # 7.  Detector battery — Q1 local factors
    # =====================================================================
    detector_runs_q1 = []

    def q1_series(p, W):
        vals = [count_reps(FORM_Q1, p ** k) for k in range(W)]
        assert all(v % 4 == 0 for v in vals)
        return [Fraction(v, 4) for v in vals]

    def q1_satake(p):
        if p == 2:
            return [F(1), F(-1)]                       # ramified: zeta factor
        if chi_m4(p) == 1:
            return [F(1), F(-2), F(1)]                 # split: (1-T)^2
        return [F(1), F(0), F(-1)]                     # inert: (1-T)(1+T)

    for p in (2, 5, 13):
        series = q1_series(p, W1)
        sat = q1_satake(p)
        assert coefficient_sequence_from_satake(sat, W1) == series, p
        v = detect(series, mode="coefficients", weight=(p, 0), holdout=HOLDOUT)
        assert v.refusal is None, (p, v.refusal)
        got = {c["axiom"]: c["status"] for c in v.cells}
        assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                       "A3_INTEGRALITY": HOLDS, "A4_PURITY": HOLDS,
                       "A5_HELD_OUT": HOLDS}, (p, got)
        assert v.object["degree"] == (1 if p == 2 else 2), (p, v.object)
        detector_runs_q1.append({
            "sub_row": "Q1", "prime": p, "series": "r_Q1(p^k)/4",
            "window": W1, "holdout": HOLDOUT, "weight_claim": [p, 0],
            "note": ("ramified: local factor 1/(1-T), the chi_-4 factor is "
                     "trivial at 2" if p == 2 else
                     "split p = 1 mod 4: local factor 1/(1-T)^2, A4 "
                     "complete deg-2 purity test HOLDS (double root 1)"),
            "verdict": v.as_dict()})

    for p in (3, 7):   # inert primes: split-sign pure pair {+1, -1}
        series = q1_series(p, W1)
        sat = q1_satake(p)
        assert coefficient_sequence_from_satake(sat, W1) == series, p
        # manual exact purity: minimal form is (1-T)(1+T); inverse roots +-1
        P, Q = minimal_rational_form(series)
        assert P == [F(1)] and Q == [F(1), F(0), F(-1)], (p, P, Q)
        assert poly_mul([F(1), F(-1)], [F(1), F(1)]) == Q
        for alpha in (1, -1):
            assert alpha * alpha == p ** 0 == 1        # weight-0 purity, exact
        v = detect(series, mode="coefficients", weight=None, holdout=HOLDOUT)
        assert v.refusal is None, (p, v.refusal)
        got = {c["axiom"]: c["status"] for c in v.cells}
        assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                       "A3_INTEGRALITY": HOLDS, "A4_PURITY": SKIPPED,
                       "A5_HELD_OUT": HOLDS}, (p, got)
        # factor-level runs, each degree 1 with an exact A4 purity pass
        vz = detect([F(1)] * W1, weight=(p, 0), holdout=HOLDOUT)
        vx = detect([F((-1) ** k) for k in range(W1)], weight=(p, 0),
                    holdout=HOLDOUT)
        for vv in (vz, vx):
            assert vv.refusal is None
            assert all(c["status"] == HOLDS for c in vv.cells)
        detector_runs_q1.append({
            "sub_row": "Q1", "prime": p, "series": "r_Q1(p^k)/4",
            "window": W1, "holdout": HOLDOUT, "weight_claim": None,
            "a4_note": (
                "weight claim deliberately withheld from the full deg-2 run: "
                "detect()'s complete deg-2 A4 test requires product of "
                "inverse roots = q^w, which the PURE split-sign pair "
                "{+1, -1} violates (product -1, q^w = 1).  Purity is "
                "certified manually by the exact factorization "
                "Q = (1-T)(1+T), inverse roots +-1, alpha^2 = 1 = p^0; and "
                "factorwise by detect() on the zeta factor 1/(1-T) and the "
                "chi factor 1/(1+T), each with A1-A5 all HOLDS at weight "
                "(p, 0)"),
            "verdict": v.as_dict(),
            "factor_runs": {"zeta_factor": vz.as_dict(),
                            "chi_factor": vx.as_dict()}})

    # A6 tensor: chi_-4 (x) chi_-4 = trivial, exact at each odd test prime
    tensor_runs = []
    for p in (3, 5, 7, 13):
        chi = chi_m4(p)
        a6 = tensor_compatibility([F(1), F(-chi)], [F(1), F(-chi)],
                                  [F(1)] * 8)
        assert a6["status"] == HOLDS, (p, a6)
        tensor_runs.append({"prime": p,
                            "statement": "chi_-4 (x) chi_-4 = chi_0 at p",
                            "a6": a6})

    # direct-sum certification: Q1 local object = zeta_p (+) chi_-4,p exactly
    for p in (3, 5, 7, 13):
        chi = chi_m4(p)
        psZ = power_sums_from_satake([F(1), F(-1)], 6)
        psX = power_sums_from_satake([F(1), F(-chi)], 6)
        ps = op_direct_sum(psZ, psX, 6)
        sat2 = satake_poly_from_power_sums(ps[:2], 2)
        assert sat2 == poly_mul([F(1), F(-1)], [F(1), F(-chi)]), p
        assert coefficient_sequence_from_satake(sat2, W1) == q1_series(p, W1)
    dsum_witness = (
        "Q1 local object certified as a DIRECT SUM zeta_p (+) chi_-4,p by "
        "exact power-sum calculus at p in {3, 5, 7, 13}: op_direct_sum of "
        "the two degree-1 power-sum lists reproduces the Satake polynomial "
        "and the full r_Q1(p^k)/4 window; chi (x) chi = trivial certified "
        "by the exact A6 tensor axiom at the same primes")

    # =====================================================================
    # 8.  Detector battery — Q2 prime-power slices + Hecke constituents
    # =====================================================================
    detector_runs_q2 = []

    def q2_slice(p, W):
        vals = [count_reps(FORM_Q2, p ** k) for k in range(W)]
        assert all(v % 2 == 0 for v in vals)
        return [Fraction(v, 2) for v in vals]

    # p = 2 (ramified, ideal class of p_2 nonprincipal): slice 1/(1-T^2)
    s2 = q2_slice(2, W2)
    assert s2 == coefficient_sequence_from_satake([F(1), F(0), F(-1)], W2)
    v = detect(s2, weight=None, holdout=HOLDOUT)
    assert v.refusal is None
    got = {c["axiom"]: c["status"] for c in v.cells}
    assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                   "A3_INTEGRALITY": HOLDS, "A4_PURITY": SKIPPED,
                   "A5_HELD_OUT": HOLDS}, got
    detector_runs_q2.append({
        "sub_row": "Q2", "prime": 2, "series": "r_Q2(2^k)/2", "window": W2,
        "holdout": HOLDOUT, "weight_claim": None,
        "note": ("slice is rational and effective: 1/(1-T^2) = "
                 "1/((1-T)(1+T)), pure split-sign roots +-1 (weight "
                 "claim withheld for the same deg-2 A4 product-form "
                 "reason as Q1 at inert p; purity manual: alpha^2 = 1)"),
        "verdict": v.as_dict()})

    # p = 3, 7 (split, both prime factors nonprincipal): virtual numerator
    for p in (3, 7):
        assert chi_m20(p) == 1 and r2[p] == 0     # split but not principal
        sp = q2_slice(p, W2)
        expected = [F((k + 1) if k % 2 == 0 else 0) for k in range(W2)]
        assert sp == expected, p
        assert sp == series_of_rational([F(1), F(0), F(1)],
                                        [F(1), F(0), F(-2), F(0), F(1)], W2)
        v = detect(sp, weight=(p, 0), holdout=HOLDOUT)
        assert v.refusal == "A2_EFFECTIVITY", (p, v.refusal)
        got = {c["axiom"]: c["status"] for c in v.cells}
        assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": FAILS,
                       "A3_INTEGRALITY": HOLDS, "A4_PURITY": HOLDS,
                       "A5_HELD_OUT": HOLDS}, (p, got)
        assert v.object["degree"] == 4 and v.object["numerator"] == "[1, 0, 1]"
        detector_runs_q2.append({
            "sub_row": "Q2", "prime": p, "series": "r_Q2(p^k)/2",
            "window": W2, "holdout": HOLDOUT, "weight_claim": [p, 0],
            "note": ("REFUSAL at A2_EFFECTIVITY: the principal-class slice "
                     "at a split-nonprincipal prime is (1+T^2)/(1-T^2)^2 — "
                     "rational (A1) and integral (A3) with pure roots "
                     "(A4, necessary conditions at degree 4) but carries "
                     "the virtual numerator 1 + T^2: NOT an effective "
                     "Euler factor"),
            "verdict": v.as_dict()})

    # p = 29 (split, both prime factors principal): perfect effective slice
    assert chi_m20(29) == 1 and r2[29] == 4
    s29 = q2_slice(29, W29)
    assert s29 == coefficient_sequence_from_satake([F(1), F(-2), F(1)], W29)
    v29 = detect(s29, weight=(29, 0), holdout=HOLDOUT)
    assert v29.refusal is None
    assert all(c["status"] == HOLDS for c in v29.cells)
    assert v29.object["degree"] == 2
    detector_runs_q2.append({
        "sub_row": "Q2", "prime": 29, "series": "r_Q2(29^k)/2",
        "window": W29, "holdout": HOLDOUT, "weight_claim": [29, 0],
        "note": ("split-PRINCIPAL prime: the slice 1/(1-T)^2 passes every "
                 "axiom including complete deg-2 purity — locally the "
                 "generic Epstein zeta can look perfectly motivic"),
        "verdict": v29.as_dict()})

    # cross-prime refutation of any Euler assembly of the certified slices
    c2 = {m: Fraction(count_reps(FORM_Q2, m), 2) for m in (2, 3, 6, 7, 14)}
    assert c2[6] == 2 and c2[2] * c2[3] == 0
    assert c2[14] == 2 and c2[2] * c2[7] == 0
    euler_refutation = (
        "the would-be Euler product assembled from the certified rational "
        "prime-power slices predicts a_6 = c(2) c(3) = 0 and a_14 = "
        "c(2) c(7) = 0 in the unit normalization c = r_Q2/2; the true "
        "exact values are c(6) = 2 and c(14) = 2.  Local rationality of "
        "every slice does NOT assemble into a global Euler product")

    # Hecke-constituent slices: both constituents are certified locally.
    # zeta_K slice at p = 3: (1 * chi_-20)(3^k) = k+1  ->  1/(1-T)^2
    zk = [F(sum(chi_m20(3) ** j for j in range(k + 1))) for k in range(W1)]
    assert zk == coefficient_sequence_from_satake([F(1), F(-2), F(1)], W1)
    vzk = detect(zk, weight=(3, 0), holdout=HOLDOUT)
    assert vzk.refusal is None and all(c["status"] == HOLDS for c in vzk.cells)
    # psi slice at p = 3: b(3^k) = (k+1)(-1)^k  ->  1/(1+T)^2
    bp3 = [F(count_reps(FORM_Q2, 3 ** k)
             - sum(chi_m20(3) ** j for j in range(k + 1))) for k in range(W1)]
    assert bp3 == [F((k + 1) * (-1) ** k) for k in range(W1)]
    assert bp3 == [F(conv(chi_m4, chi_5, 3 ** k)) for k in range(W1)]
    assert bp3 == coefficient_sequence_from_satake([F(1), F(2), F(1)], W1)
    vps3 = detect(bp3, weight=(3, 0), holdout=HOLDOUT)
    assert vps3.refusal is None and all(c["status"] == HOLDS for c in vps3.cells)
    # psi slice at p = 2: b(2^k) = (-1)^k  ->  1/(1+T)
    bp2 = [F(count_reps(FORM_Q2, 2 ** k) - 1) for k in range(W2)]
    assert bp2 == [F((-1) ** k) for k in range(W2)]
    assert bp2 == coefficient_sequence_from_satake([F(1), F(1)], W2)
    vps2 = detect(bp2, weight=(2, 0), holdout=HOLDOUT)
    assert vps2.refusal is None and all(c["status"] == HOLDS for c in vps2.cells)
    for tag, vv, note in (
            ("zeta_K_slice_p3", vzk,
             "constituent zeta(s)L(s,chi_-20) local slice at split p=3: "
             "1/(1-T)^2, all axioms HOLD"),
            ("psi_slice_p3", vps3,
             "constituent L(chi_-4)L(chi_5) (genus character psi) local "
             "slice at p=3: 1/(1+T)^2, all axioms HOLD incl. complete "
             "deg-2 purity (double root -1)"),
            ("psi_slice_p2", vps2,
             "psi slice at ramified p=2: 1/(1+T), all axioms HOLD")):
        detector_runs_q2.append({
            "sub_row": "Q2", "constituent": tag, "holdout": HOLDOUT,
            "note": note, "verdict": vv.as_dict()})
    constituent_witness = (
        "BOTH Hecke constituents of Z_Q2 = zeta L(chi_-20) + "
        "L(chi_-4) L(chi_5) are certified locally by the detector (all "
        "axioms HOLD: zeta_K slice 1/(1-T)^2 at p=3; psi slices 1/(1+T)^2 "
        "at p=3 and 1/(1+T) at p=2, exact deg-2 purity where applicable), "
        "while the RAW principal-form slice at p in {3, 7} is REFUSED at "
        "A2_EFFECTIVITY with virtual numerator 1 + T^2.  The detector "
        "separates the sum into its Euler-product parts")

    # =====================================================================
    # 9.  Assemble the world record
    # =====================================================================
    l0_witness = (
        "both forms (and the genus partner (2,2,3)) certified positive "
        "definite by integer coefficient identities 4a Q = (2ax+by)^2 + "
        "|D| y^2; representation numbers r_Q(n) computed for all n <= "
        f"{N} by exhaustive search with PROVED box bounds and "
        "cross-validated by an independent exact per-n counter (three "
        "forms, all n agree); convergence of Z_Q(s) for Re s > 1 and "
        "meromorphy are imported (Epstein 1903)")

    l3_witness = (
        "no local factors exist for the generic member: any Euler "
        "factorization would force a_6 = a_2 a_3 in every normalization "
        "(refuted: " + euler_refutation + ").  Remarkably, every TESTED "
        "prime-power slice of Q2 is individually rational of degree <= 4 "
        "with exact BM certificates (p = 2: 1/(1-T^2); p = 3, 7: "
        "(1+T^2)/(1-T^2)^2, A2-refused virtual numerator; p = 29: "
        "1/(1-T)^2) — slice rationality does not assemble.  Q1 sub-row: "
        "uniformly degree <= 2 local factors certified A1-A5")

    l4_witness = (
        "generic member has NO local weight data to be coherent: " +
        nonmult_witness[:180] + "... (see L1).  What DOES hold for both "
        "sub-rows: global self-duality — real coefficients and the "
        "Epstein FE s <-> 1-s (imported).  Q1 sub-row: local weight-0 "
        "purity exact (inverse roots +-1 and double root 1 at split p; "
        "detect A4 HOLDS at p = 2, 5, 13 and factorwise at 3, 7)")

    world = {
        "id": "epstein_pair",
        "title": ("Epstein pair: Z_(x^2+y^2) vs Z_(x^2+5y^2) "
                  "(class number 1 vs 2)"),
        "definition": (
            "Z_Q(s) = sum_((x,y) in Z^2, (x,y) != 0) Q(x,y)^(-s), Re s > 1, "
            "for the positive definite binary quadratic forms Q1 = x^2 + "
            "y^2 (disc -4, h = 1) and Q2 = x^2 + 5y^2 (disc -20, h = 2), "
            "treated as ONE world with two sub-rows.  Exact coefficient "
            "layer (this build, n <= 400): r_Q1 = 4 (1 * chi_-4), so "
            "Z_Q1 = 4 zeta(s) L(s, chi_-4) = 4 zeta_Q(i)(s); r_Q2 = "
            "(1 * chi_-20) + (chi_-4 * chi_5), so Z_Q2 = zeta(s) "
            "L(s, chi_-20) + L(s, chi_-4) L(s, chi_5) — a sum of two Euler "
            "products, itself NOT an Euler product (exact witness at "
            "n = 6).  Genus partner Q2' = 2x^2 + 2xy + 3y^2 carried as an "
            "exact side object: r_Q2 + r_Q2' = 2 (1 * chi_-20)."),
        "arithmetic_class": (
            "EXACT_INTEGER / EXACT_RATIONAL (Python ints, Fractions). "
            "No floating point anywhere in the build."),
        "ladder": {
            "L0_WELL_DEFINED": cell(
                "HOLDS", "PROVED_HERE", witness=l0_witness,
                citation="Epstein (1903), Zur Theorie allgemeiner "
                         "Zetafunktionen (Math. Annalen ~56)"),
            "L1_MULTIPLICATIVITY": cell(
                "FAILS", "REFUTED_BY_WITNESS",
                witness=("generic member Q2: " + nonmult_witness + ".  " +
                         control_witness + ".  Sub-row Q1 HOLDS: " +
                         jacobi_witness),
                citation="Jacobi (1829), Fundamenta Nova (two-squares "
                         "theorem, for the Q1 sub-row identity)"),
            "L2_EULER_PRODUCT": cell(
                "FAILS", "REFUTED_BY_WITNESS",
                witness=("generic member Q2: " + euler_refutation +
                         ".  Sub-row Q1 HOLDS on the class-number-1 locus: "
                         "Z_Q1/4 = zeta L(chi_-4) coefficientwise to "
                         f"n = {N} (exact), Euler products of zeta and "
                         "L(chi_-4) imported"),
                citation="Euler product of zeta: Euler (1737); of Dirichlet "
                         "L-series: Dirichlet (1837)"),
            "L3_BOUNDED_DEGREE_RATIONAL": cell(
                "FAILS", "REFUTED_BY_WITNESS", witness=l3_witness,
                citation=""),
            "L4_WEIGHT_DUALITY": cell(
                "FAILS", "REFUTED_BY_WITNESS", witness=l4_witness,
                citation="Epstein (1903) for the FE-level self-duality"),
            "L5_CONDUCTOR_GAMMA_ROOT": cell(
                "HOLDS", "IMPORTED_THEOREM",
                witness=("class-number-INDEPENDENT: every Z_Q of a "
                         "positive definite binary form has the canonical "
                         "completed form Lambda_Q(s) = "
                         "(2 pi / sqrt(det A_Q))^(-s) Gamma(s) Z_Q(s) with "
                         "det A_Q the Gram determinant (1 for Q1; 5 for Q2 "
                         "and Q2'), gamma factor Gamma(s) (2 pi)^(-s) "
                         "(degree-2, Gamma_C type), root number +1 "
                         "(symmetric FE).  The Gram determinant plays the "
                         "conductor role"),
                citation="Epstein (1903); CITATION-NEEDED: exact "
                         "normalization conventions of the completed "
                         "Epstein FE (Epstein 1903; cf. also Chowla-"
                         "Selberg 1949-1967 era treatments)"),
            "L6_CONTINUATION_FE": cell(
                "HOLDS", "IMPORTED_THEOREM",
                witness=("Epstein 1903: Z_Q(s) continues meromorphically "
                         "to C with a single simple pole at s = 1, and "
                         "Lambda_Q(s) = Lambda_Q(1-s).  Holds for BOTH "
                         "sub-rows — continuation+FE are blind to class "
                         "number.  Q1 cross-check: consistent with the "
                         "completed FEs of zeta (Riemann 1859) and "
                         "L(chi_-4) via Z_Q1 = 4 zeta L(chi_-4) (exact "
                         f"coefficient identity to n = {N} here)"),
                citation="Epstein (1903), Zur Theorie allgemeiner "
                         "Zetafunktionen; CITATION-NEEDED: precise "
                         "statement/volume; theta-transformation method "
                         "after Riemann (1859), Jacobi theta inversion"),
            "L7_TWIST_TENSOR_COMPAT": cell(
                "FAILS", "REFUTED_BY_WITNESS",
                witness=("generic member: no local Satake data exists to "
                         "twist or tensor (see L1/L2 witness: r_Q2(2) = "
                         "r_Q2(3) = 0, r_Q2(6) = 4).  Sub-row Q1: " +
                         dsum_witness + ".  Constituent level for Q2: the "
                         "psi-part is EXACTLY the convolution "
                         "chi_-4 * chi_5 (verified n <= 400) — twisting "
                         "lives on the Hecke constituents, not on the "
                         "Epstein zeta itself"),
                citation=""),
            "L8_REALIZATION": cell(
                "HOLDS", "PROVED_HERE",
                witness=("lattice/theta realization is literally computed: "
                         "r_Q(0..400) are the theta coefficients of the "
                         "lattices Z^2 and Z + Z sqrt(-5) (and the "
                         "nonprincipal ideal lattice for Q2').  " +
                         split_witness + ".  " + class_witness +
                         ".  Imported: real-analytic Eisenstein-series "
                         "realization Z_Q(s) ~ E(z_Q, s) on SL(2,Z)\\H; "
                         "Q1 motivic/automorphic: Z_Q1/4 = zeta_Q(i) "
                         "(Dedekind zeta, GL(1) Hecke); Q2 constituents "
                         "are Hecke L-functions of Q(sqrt(-5))"),
                citation="Epstein (1903); Gauss (1801) genus theory and "
                         "reduced forms; Hecke (1918-1920) Groessen-"
                         "charaktere; CITATION-NEEDED: standard identity "
                         "Epstein zeta = zeta(2s)-normalized real-analytic "
                         "Eisenstein series (classical, e.g. Chowla-"
                         "Selberg 1967 era)"),
            "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
                "FAILS", "IMPORTED_THEOREM",
                witness=("generic member Q2: any Weil-positivity "
                         "functional for Z_Q2 is impossible — Z_Q2 has "
                         "zeros OFF the critical line, and (imported, "
                         "Davenport-Heilbronn phenomenon for class number "
                         "> 1) even infinitely many zeros in Re s > 1; an "
                         "explicit formula still exists via the "
                         "constituents but its positivity half is dead.  "
                         "Sub-row Q1: explicit formula unconditional for "
                         "zeta and L(chi_-4); positivity (Weil criterion) "
                         "OPEN, equivalent to RH+GRH(chi_-4) — NOT claimed"),
                citation="Davenport and Heilbronn (1936), On the zeros of "
                         "certain Dirichlet series, J. London Math. Soc. "
                         "(CITATION-NEEDED: precise paper I/II and the "
                         "class-number>1 Epstein statement); Weil (1952) "
                         "explicit formula/positivity criterion"),
        },
        "mechanisms": {
            "EULER_PRODUCT": cell(
                "FAILS", "REFUTED_BY_WITNESS",
                witness=("generic member Q2: r_Q2(2) = 0, r_Q2(3) = 0, "
                         "r_Q2(6) = 4 — no normalization is "
                         "multiplicative; " + euler_refutation +
                         ".  HOLDS exactly on the CM/class-number-1 locus: "
                         "Q1 sub-row, r_Q1/4 = 1 * chi_-4 exact to "
                         f"n = {N} (Jacobi), Euler products imported"),
                citation="Jacobi (1829) for the Q1 identity"),
            "DUALITY_FE": cell(
                "HOLDS", "IMPORTED_THEOREM",
                witness=("supplied for EVERY member of the lattice family "
                         "by the Epstein FE (theta transformation / "
                         "Poisson): Lambda_Q(s) = Lambda_Q(1-s), root "
                         "number +1, real coefficients (self-dual).  The "
                         "one mechanism here that is blind to class "
                         "number — it survives exactly where the Euler "
                         "product dies"),
                citation="Epstein (1903); CITATION-NEEDED: exact completed "
                         "normalization"),
            "TRACE_FORMULA": cell(
                "HOLDS", "IMPORTED_THEOREM",
                witness=("Poisson summation on the lattice L_Q (= the "
                         "trace formula for R^2/L_Q) gives the theta "
                         "transformation theta_Q(1/t) = (t / sqrt(det "
                         "A_Q)) theta_Q(t), which supplies L6 by the "
                         "Riemann method; the exact theta coefficients "
                         f"r_Q(0..{N}) computed here are the geometric "
                         "side data"),
                citation="Jacobi theta inversion (1829 era); Riemann "
                         "(1859) method; Epstein (1903)"),
            "POSITIVITY_PURITY": cell(
                "FAILS", "IMPORTED_THEOREM",
                witness=("FAILS for the generic member Q2: off-critical-"
                         "line zeros (imported, Davenport-Heilbronn) "
                         "refute any positivity mechanism, and there is "
                         "no purity structure on the raw coefficients "
                         "(non-multiplicativity witness at (2,3,6)).  "
                         "Sub-row Q1: unitarized local purity is exact "
                         "(all inverse roots of modulus 1, certified), "
                         "but positivity forcing GRH is OPEN — none "
                         "known.  The detector adds a sharp exact point: "
                         "the Q2 slice at p = 3, 7 has a VIRTUAL part "
                         "(numerator 1 + T^2, A2 refusal) — "
                         "effectivity/positivity of local data already "
                         "fails at the slice level"),
                citation="Davenport and Heilbronn (1936); CITATION-NEEDED "
                         "as in L9"),
            "TENSOR_OPS": cell(
                "FAILS", "REFUTED_BY_WITNESS",
                witness=("generic member: no local objects exist to "
                         "tensor (witness (2,3,6) as in L1).  Sub-row Q1: "
                         + dsum_witness),
                citation=""),
            "FAMILY": cell(
                "HOLDS", "PROVED_HERE",
                witness=("the pair spans the bifurcation locus of the "
                         "2-parameter lattice moduli space SL(2,Z)\\H "
                         "(the pass's epstein/ zero-bifurcation lab lives "
                         "on this family).  Exact family results here: " +
                         class_witness + ".  " + genus_witness + ", and "
                         "the genus average (r_Q2 + r_Q2')/2 = 1 * "
                         "chi_-20 is multiplicative with ZERO failures "
                         "over all coprime pairs mn <= 400 — the FAMILY "
                         "average restores the Euler-product mechanism "
                         "that the individual member loses"),
                citation="Gauss (1801) genus theory"),
        },
        "critical_line": {
            "status": "FALSE",
            "detail": (
                "Recorded for the GENERIC member Q2 (class number 2): "
                "FALSE — imported: Epstein zeta functions of positive "
                "definite binary forms with class number > 1 have zeros "
                "off the critical line, indeed infinitely many zeros in "
                "the region of absolute convergence Re s > 1 "
                "(Davenport-Heilbronn phenomenon), consistent with the "
                "exact structural decomposition proved coefficientwise "
                "here: Z_Q2 = zeta L(chi_-20) + L(chi_-4) L(chi_5) is a "
                "sum of two Euler products with independent phases.  "
                "Sub-row Q1 (class number 1): CONJECTURE — Z_Q1 = "
                "4 zeta(s) L(s, chi_-4) (exact to n = 400 here; Jacobi), "
                "so its nontrivial zeros lie on Re s = 1/2 iff RH holds "
                "for zeta AND GRH holds for L(chi_-4).  Unproved; nothing "
                "in this record moves either conjecture.  Also imported: "
                "Z_Q for binary forms has infinitely many zeros ON the "
                "critical line (Potter-Titchmarsh era)."),
            "rigor": "IMPORTED_THEOREM",
            "citation": (
                "Davenport and Heilbronn (1936), On the zeros of certain "
                "Dirichlet series I, II, J. London Math. Soc. — "
                "CITATION-NEEDED: which paper carries the class-number>1 "
                "Epstein case and the exact statement; Potter and "
                "Titchmarsh (1935), The zeros of Epstein's zeta-functions "
                "— CITATION-NEEDED: precise scope (infinitely many zeros "
                "on the line; off-line zeros in the strip for specific "
                "forms); Voronin (1976 era) off-line zeros in the strip "
                "for class number > 1 — CITATION-NEEDED"),
            "witness": (
                "structural exact witness for the sub-row split: "
                "r_Q2(2) = r_Q2(3) = 0, r_Q2(6) = 4 (no Euler product) "
                "vs r_Q1 = 4 (1 * chi_-4) exact to n = 400 (Euler "
                "product on the CM locus)"),
        },
        "sources": [
            "P. Epstein (1903), Zur Theorie allgemeiner Zetafunktionen, "
            "Mathematische Annalen (~56): definition, continuation, "
            "functional equation",
            "C. G. J. Jacobi (1829), Fundamenta Nova Theoriae Functionum "
            "Ellipticarum: r(n) = 4 sum chi_-4(d) (two squares)",
            "C. F. Gauss (1801), Disquisitiones Arithmeticae: reduction "
            "theory, class numbers, genus theory / genus characters",
            "H. Davenport and H. Heilbronn (1936), On the zeros of certain "
            "Dirichlet series I, II, J. London Math. Soc.: zeros of "
            "Epstein zetas with h > 1 off the line / in Re s > 1 "
            "(CITATION-NEEDED: precise statement location)",
            "H. S. A. Potter and E. C. Titchmarsh (1935), The zeros of "
            "Epstein's zeta-functions (CITATION-NEEDED: precise scope)",
            "E. Hecke (1918-1920), Groessencharaktere: the constituents "
            "of Z_Q2 as Hecke L-functions of Q(sqrt(-5))",
            "S. Chowla and A. Selberg (1949/1967), Epstein zeta and "
            "Eisenstein series / Kronecker limit circle (CITATION-NEEDED: "
            "which statements are used is descriptive only)",
        ],
        "rh_established": False,
        "sub_rows": {
            "Q1": {
                "form": "x^2 + y^2", "gram_det": 1, "disc": -4,
                "class_number": 1,
                "euler_product": "HOLDS (exact to n <= 400; Jacobi "
                                 "imported for all n)",
                "critical_line": "CONJECTURE (iff RH for zeta and GRH for "
                                 "L(chi_-4))",
                "key_witness": "r_Q1(n) = 4 sum_(d|n) chi_-4(d), all "
                               "n <= 400, exact"},
            "Q2": {
                "form": "x^2 + 5y^2", "gram_det": 5, "disc": -20,
                "class_number": 2,
                "euler_product": "FAILS (exact witness (2,3,6); no "
                                 "normalization multiplicative)",
                "critical_line": "FALSE (imported: Davenport-Heilbronn)",
                "key_witness": "r_Q2 = (1*chi_-20) + (chi_-4*chi_5), all "
                               "n <= 400, exact; r_Q2(2)=r_Q2(3)=0, "
                               "r_Q2(6)=4"},
        },
        "notes": (
            "Two-sub-row semantics: where cells differ between the "
            "sub-rows, the recorded status is that of the GENERIC member "
            "Q2 and the witness carries the Q1/CM-locus exception "
            "explicitly (per the pass convention for family worlds).  "
            "The exact theta data r_Q(0..400) for Q1, Q2 and the genus "
            "partner Q2' = 2x^2+2xy+3y^2, plus the divisor-sum sequences "
            "1*chi_-4 and 1*chi_-20 and the genus-character convolution "
            "chi_-4*chi_5, are embedded in the sibling data file "
            "worlds/epstein_pair_data.json for reuse by the epstein/ "
            "bifurcation lab.  First terms: r_Q1(0..20) = "
            f"{r1[:21]}; r_Q2(0..20) = {r2[:21]}; r_Q2'(0..20) = "
            f"{r2b[:21]}.  Key structural exact results: (i) " +
            genus_witness + "; (ii) " + decomp_witness + "; (iii) " +
            constituent_witness + ".  Detector caveat recorded honestly: "
            "detect()'s complete deg-2 A4 purity test demands product of "
            "inverse roots = q^w and therefore mis-flags the PURE "
            "split-sign pair {+1,-1}; wherever that configuration occurs "
            "(Q1 inert primes, Q2 slice at p=2) the weight claim was "
            "withheld and purity was certified manually by exact "
            "factorization (1-T)(1+T), alpha^2 = 1 = p^0.  Nothing here "
            "establishes RH/GRH; rh_established = false."),
        "detector_runs": {
            "q1_local_battery": detector_runs_q1,
            "q1_tensor_battery": tensor_runs,
            "q2_slice_and_constituent_battery": detector_runs_q2,
        },
    }

    probs = validate_world(world)
    assert not probs, probs
    out_dir = os.path.dirname(os.path.abspath(__file__))
    path = save_world(world, out_dir)

    # =====================================================================
    # 10.  Sibling data file: exact first Fourier/theta data for reuse
    # =====================================================================
    data = {
        "id": "epstein_pair_data",
        "N": N,
        "forms": {
            "Q1": {"a": 1, "b": 0, "c": 1, "disc": -4, "gram_det": 1,
                   "class_number": 1},
            "Q2": {"a": 1, "b": 0, "c": 5, "disc": -20, "gram_det": 5,
                   "class_number": 2},
            "Q2_genus_partner": {"a": 2, "b": 2, "c": 3, "disc": -20,
                                 "gram_det": 5, "class_number": 2},
        },
        "r_Q1": r1,
        "r_Q2": r2,
        "r_Q2_genus_partner": r2b,
        "divisor_sum_chi_minus4": d4,
        "divisor_sum_chi_minus20": d20,
        "genus_character_convolution_chi4_star_chi5": b_psi,
        "index_convention": ("lists are indexed by n = 0..400; r(0) = 1 "
                             "counts the zero vector; divisor sums and the "
                             "convolution are set to 0 at n = 0 by "
                             "convention"),
        "chi_minus4_period4": [0, 1, 0, -1],
        "chi_5_period5": [0, 1, -1, -1, 1],
        "chi_minus20_period20": [0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, -1, 0,
                                 -1, 0, 0, 0, -1, 0, -1],
        "identities_verified_exactly": [
            "r_Q1(n) = 4 * divisor_sum_chi_minus4(n) for 1 <= n <= 400",
            "r_Q2(n) + r_Q2'(n) = 2 * divisor_sum_chi_minus20(n) for "
            "1 <= n <= 400",
            "r_Q2(n) = divisor_sum_chi_minus20(n) + "
            "(chi_-4 * chi_5)(n) for 1 <= n <= 400",
            "r_Q2'(n) = divisor_sum_chi_minus20(n) - "
            "(chi_-4 * chi_5)(n) for 1 <= n <= 400",
            "r_Q2(2) = r_Q2(3) = 0, r_Q2(6) = 4: non-multiplicativity of "
            "every scalar normalization of r_Q2",
        ],
        "generator": "worlds/epstein_pair_build.py (deterministic, exact "
                     "integer arithmetic only)",
        "rh_established": False,
    }
    data_path = os.path.join(out_dir, "epstein_pair_data.json")
    with open(data_path, "w") as f:
        json.dump(data, f, indent=1, sort_keys=True)
        f.write("\n")

    print(f"wrote {path}")
    print(f"wrote {data_path}")
    print("epstein_pair: all exact assertions passed; rh_established=false")


if __name__ == "__main__":
    main()
