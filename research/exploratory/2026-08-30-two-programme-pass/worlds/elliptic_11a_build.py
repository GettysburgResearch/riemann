"""World 'elliptic_11a': the L-function of the elliptic curve 11a1,

    E : y^2 + y = x^3 - x^2 - 10x - 20   over Q      (E = X_0(11)).

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.elliptic_11a_build

regenerates worlds/elliptic_11a.json identically.

Structure of this file:
  1. exact curve invariants: b2, b4, b6, b8, c4, c6, Delta computed from the
     a-invariants (0, -1, 1, -10, -20) with integer arithmetic; assertions
     Delta = -11^5, 4 b8 = b2 b6 - b4^2, c4^3 - c6^2 = 1728 Delta.  Delta != 0
     proves E is nonsingular; Delta % p != 0 proves good reduction at each
     good prime p <= 97; 11 | Delta, 11 does not divide c4 gives multiplicative
     reduction at 11 (conductor exponent 1, imported criterion).
  2. exact point counting: for every good prime p <= 97 (all p != 11),
     #E(F_p) = 1 + #{(x,y) in F_p^2 : y^2 + y = x^3 - x^2 - 10x - 20} by a
     plain double loop over F_p x F_p; a_p = p + 1 - #E(F_p).  All integer
     arithmetic.  Cross-checks: the classical values a_2=-2, a_3=-1, a_5=1,
     a_7=-2, a_13=4; the rational 5-torsion point (5,5) on E forces
     5 | #E(F_p), verified for every good p.
  3. exact Hasse bound: a_p^2 <= 4p asserted as an integer inequality at
     every good p (in fact a_p^2 < 4p strictly, also asserted) — this is the
     LOCAL purity of weight 1: both inverse roots of 1 - a_p T + p T^2 have
     modulus p^{1/2}.
  4. detector runs: core.reconstruct.detect on the exact coefficient sequence
     of 1/(1 - a_p T + p T^2) with purity weight (p, 1) at ALL 24 good primes
     p <= 97.  Degree 2, so the A4 purity test is COMPLETE and exact
     (product of inverse roots == p and discriminant < 0), not merely a
     necessary condition.  All five axioms must return HOLDS.
  5. exact modular cross-check: the eta product q prod (1-q^n)^2 (1-q^{11n})^2
     is expanded EXACTLY to q^100 with integer arithmetic; its coefficient at
     every good prime p <= 97 equals the point-count a_p, and the Euler
     local-global product over the local factors (including 1 - T at p = 11,
     a_11 = +1 read off the expansion) reproduces every a_n, n <= 100.
     This is a finite exact CONSISTENCY witness for modularity; modularity
     itself is imported (Eichler 1954 for this curve; Wiles/Taylor-Wiles
     1995, BCDT 2001 for the class).
  6. exact weight-1 self-duality: op_dual_satake followed by T -> pT fixes
     each local factor: the Frobenius eigenvalue multiset is stable under
     alpha -> p/alpha, per prime.
  7. exact Sym^2 computation at p = 2 and p = 3: op_sym2 on the power sums
     gives an INTEGRAL degree-3 Satake polynomial matching the closed form
     [1, -(a_p^2 - p), p a_p^2 - p^2, -p^3]; Ext^2 power sums are exactly
     [p, p^2, p^3] (determinant = weight-2 Tate twist); the tensor square
     decomposes exactly as Sym^2 (+) Ext^2 on power sums; A6 tensor
     compatibility (tensor_compatibility) HOLDS against the degree-4
     product factor; detect runs on the Sym^2 coefficient sequences with
     weight (p, 2) — degree 3, so purity there is NECESSARY_ONLY, and the
     record says so.
  8. the world record: ladder L0..L9, mechanisms, critical_line = CONJECTURE
     (GRH for L(E,s)).  Global analytic facts are IMPORTED_THEOREM with
     honest citations; the POSITIVITY_PURITY mechanism cell carefully splits
     local purity (a theorem, proved here per prime) from the global
     critical-line mechanism (not identified, OPEN).  rh_established=false.

No floats appear anywhere in this file.
"""

from fractions import Fraction

from core.exact import (
    F,
    coefficient_sequence_from_satake,
    power_sums_from_satake,
    op_dual_satake,
    op_sym2,
    op_ext2,
    op_tensor,
    satake_poly_from_power_sums,
    poly_mul,
    is_integer_poly,
)
from core.reconstruct import detect, tensor_compatibility
from core.worlds import cell, validate_world, save_world

# --- fixed exact data ------------------------------------------------------
# a-invariants of the minimal Weierstrass model 11a1 (Cremona label):
#   y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6
AINV = {"a1": 0, "a2": -1, "a3": 1, "a4": -10, "a6": -20}

PMAX = 97          # good primes p <= PMAX are treated exactly
BAD_PRIME = 11     # conductor 11: the single bad prime
WINDOW = 12        # detector window (a_{p^0} .. a_{p^11})
HOLDOUT = 4        # detector held-out tail
SYM2_WINDOW = 14   # detector window for the degree-3 Sym^2 factor
NEULER = 100       # Euler local-global / eta cross-check range


def isqrt_int(n):
    """Integer square root by pure-integer search (n is tiny here); keeps
    the no-floats discipline airtight even in loop bounds."""
    r = 0
    while (r + 1) * (r + 1) <= n:
        r += 1
    return r


def primes_upto_exact(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for d in range(2, isqrt_int(n) + 1):
        if sieve[d]:
            for m in range(d * d, n + 1, d):
                sieve[m] = False
    return [p for p in range(2, n + 1) if sieve[p]]


GOOD_PRIMES = [p for p in primes_upto_exact(PMAX) if p != BAD_PRIME]
assert len(GOOD_PRIMES) == 24 and GOOD_PRIMES[0] == 2 and GOOD_PRIMES[-1] == 97


def factorize(n):
    """Exact integer factorization by trial division."""
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


# --- 1. curve invariants ---------------------------------------------------

def compute_invariants():
    """Standard b/c-invariants and discriminant, exact integers, with the
    defining identities asserted.  Formulas: Silverman, The Arithmetic of
    Elliptic Curves, III.1."""
    a1, a2, a3, a4, a6 = (AINV["a1"], AINV["a2"], AINV["a3"],
                          AINV["a4"], AINV["a6"])
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 + 4 * a2 * a6 - a1 * a3 * a4 + a2 * a3 * a3 - a4 * a4
    c4 = b2 * b2 - 24 * b4
    c6 = -b2 ** 3 + 36 * b2 * b4 - 216 * b6
    delta = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6

    # defining identities (exact integer checks)
    assert 4 * b8 == b2 * b6 - b4 * b4
    assert c4 ** 3 - c6 ** 2 == 1728 * delta
    # the concrete values for 11a1
    assert (b2, b4, b6, b8) == (-4, -20, -79, -21)
    assert (c4, c6) == (496, 20008)
    assert delta == -161051 == -(11 ** 5)
    # nonsingular: Delta != 0  -> E is an elliptic curve
    assert delta != 0
    # good reduction at every good prime p <= 97: p does not divide Delta
    for p in GOOD_PRIMES:
        assert delta % p != 0, p
    # at 11: 11 | Delta but 11 does not divide c4  -> multiplicative reduction
    assert delta % 11 == 0 and c4 % 11 != 0

    return {"b2": b2, "b4": b4, "b6": b6, "b8": b8,
            "c4": c4, "c6": c6, "delta": delta}


# --- 2. exact point counting ----------------------------------------------

def count_points(p):
    """#E(F_p) for E: y^2 + y = x^3 - x^2 - 10x - 20, counting the point at
    infinity plus a plain double loop over all (x, y) in F_p x F_p.
    Pure integer arithmetic."""
    count = 1  # the point at infinity O
    for x in range(p):
        rhs = (x * x * x - x * x - 10 * x - 20) % p
        for y in range(p):
            if (y * y + y - rhs) % p == 0:
                count += 1
    return count


def build_point_counts():
    """(#E(F_p), a_p) for all good p <= 97, with cross-checks."""
    # the rational point (5, 5) lies on E (it generates the 5-torsion):
    x, y = 5, 5
    assert y * y + y == x * x * x - x * x - 10 * x - 20  # 30 == 30
    table = {}
    for p in GOOD_PRIMES:
        Np = count_points(p)
        ap = p + 1 - Np
        # reduction of the rational 5-torsion forces 5 | #E(F_p):
        assert Np % 5 == 0, (p, Np)
        table[p] = (Np, ap)
    # classical cross-check values (coefficients of the level-11 weight-2
    # newform, e.g. LMFDB 11.2.a.a / Cremona tables):
    assert table[2][1] == -2 and table[3][1] == -1 and table[5][1] == 1
    assert table[7][1] == -2 and table[13][1] == 4
    return table


# --- 3.-4. Hasse bound, Hecke recursion, self-duality, detector ------------

def satake_of(p, ap):
    """Local Satake polynomial det(1 - Frob_p T | H^1) = 1 - a_p T + p T^2,
    low-first, constant term 1."""
    return [Fraction(1), Fraction(-ap), Fraction(p)]


def build_local_witnesses(table):
    W = {}

    # (a) exact Hasse bound = LOCAL purity of weight 1, per prime.
    hasse_bits = []
    for p in GOOD_PRIMES:
        ap = table[p][1]
        assert ap * ap <= 4 * p, (p, ap)          # Hasse: |a_p| <= 2 sqrt(p)
        assert ap * ap < 4 * p, (p, ap)           # strict (4p is no square)
        hasse_bits.append(f"{p}:{ap * ap}<={4 * p}")
    W["hasse"] = ("exact integer inequalities a_p^2 <= 4p (all strict) at "
                  "every good p <= 97: " + ", ".join(hasse_bits))

    # (b) point-count table as a witness string.
    W["points"] = ("(#E(F_p), a_p) by exhaustive double-loop point count: " +
                   ", ".join(f"{p}:({table[p][0]},{table[p][1]})"
                             for p in GOOD_PRIMES))

    # (c) Hecke recursion a_{p^{k+1}} = a_p a_{p^k} - p a_{p^{k-1}} holds
    #     exactly for the coefficient sequence of every local factor.
    for p in GOOD_PRIMES:
        ap = table[p][1]
        seq = coefficient_sequence_from_satake(satake_of(p, ap), WINDOW)
        assert seq[0] == 1 and seq[1] == ap
        for k in range(1, WINDOW - 1):
            assert seq[k + 1] == ap * seq[k] - p * seq[k - 1], (p, k)
        assert all(F(c).denominator == 1 for c in seq)
    W["hecke"] = (f"a_(p^(k+1)) = a_p a_(p^k) - p a_(p^(k-1)) verified "
                  f"exactly for k < {WINDOW - 1} at all 24 good p <= 97; "
                  "all a_(p^k) integers")

    # (d) exact weight-1 self-duality: alpha -> p/alpha fixes each local
    #     factor.  op_dual_satake gives det(1 - Frob^{-1} T); rescaling
    #     T -> pT gives det(1 - p Frob^{-1} T), which must equal the
    #     original factor (Frobenius eigenvalue pair {alpha, p/alpha}).
    for p in GOOD_PRIMES:
        ap = table[p][1]
        sat = satake_of(p, ap)
        dd = op_dual_satake(sat, F(p))
        dual_w1 = [dd[i] * F(p) ** i for i in range(len(dd))]
        assert dual_w1 == sat, (p, dual_w1)
        # determinant of Frobenius = p exactly (coefficient of T^2):
        assert sat[2] == p
    W["selfdual"] = ("op_dual_satake + rescaling T -> pT fixes every local "
                     "factor 1 - a_p T + p T^2 exactly (det Frob_p = p, "
                     "eigenvalue multiset stable under alpha -> p/alpha), "
                     "all 24 good p <= 97")

    return W


def run_detectors(table):
    """core.reconstruct.detect at every good prime, purity weight (p, 1).
    Degree 2 => the A4 purity test is COMPLETE and exact."""
    runs = []
    for p in GOOD_PRIMES:
        ap = table[p][1]
        sat = satake_of(p, ap)
        series = coefficient_sequence_from_satake(sat, WINDOW)
        v = detect(series, mode="coefficients", weight=(p, 1),
                   holdout=HOLDOUT)
        d = v.as_dict()
        assert d["refusal"] is None, (p, d)
        got = {c["axiom"]: c["status"] for c in d["cells"]}
        assert got == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                       "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                       "A5_HELD_OUT": "HOLDS"}, (p, got)
        # degree 2: purity verdict must be the complete exact test, not a
        # necessary-only surrogate.
        a4 = next(c for c in d["cells"] if c["axiom"] == "A4_PURITY")
        assert a4["rigor"] == "EXACT_RATIONAL", (p, a4)
        assert "deg-2 complete test" in a4["witness"], (p, a4)
        # the reconstructed object is exactly 1/(1 - a_p T + p T^2):
        assert d["object"]["degree"] == 2
        expect = "[" + ", ".join(str(c) for c in [1, -ap, p]) + "]"
        assert d["object"]["denominator"] == expect, (p, d["object"])
        assert d["object"]["numerator"] == "[1]"
        runs.append({"prime": p, "a_p": ap, "weight": [p, 1],
                     "mode": "coefficients",
                     "series": [str(int(c)) for c in series],
                     "verdict": d})
    return runs


# --- 5. eta product and Euler local-global cross-check ---------------------

def eta_coefficients(N):
    """Exact integer q-expansion of f(q) = q prod_{n>=1} (1-q^n)^2
    (1-q^{11n})^2 up to q^N.  Returns a list a with a[n] the coefficient of
    q^n (a[0] = 0).  Classically f is the unique newform in
    S_2(Gamma_0(11)) — that identification is IMPORTED; the expansion here
    is exact."""
    # product part truncated at degree N-1
    P = [0] * N
    P[0] = 1
    for k in range(1, N):
        for _rep in range(2):                      # (1 - q^k)^2
            for i in range(N - 1, k - 1, -1):
                P[i] -= P[i - k]
        if 11 * k < N:
            for _rep in range(2):                  # (1 - q^{11k})^2
                for i in range(N - 1, 11 * k - 1, -1):
                    P[i] -= P[i - 11 * k]
    a = [0] * (N + 1)
    for n in range(1, N + 1):
        a[n] = P[n - 1]
    return a


def build_global_witnesses(table):
    W = {}
    eta = eta_coefficients(NEULER)
    assert eta[1] == 1

    # (e) point counts match the eta-product coefficients at every good
    #     p <= 97 — an exact finite consistency witness for modularity.
    for p in GOOD_PRIMES:
        assert eta[p] == table[p][1], (p, eta[p], table[p][1])
    W["eta_match"] = ("exact q-expansion of q prod(1-q^n)^2(1-q^(11n))^2 to "
                      "q^100 (integer arithmetic) has coefficient at q^p "
                      "equal to the point-count a_p for ALL 24 good p <= 97 "
                      "(finite consistency witness; modularity itself "
                      "imported)")

    # (f) bad prime: a_11 read off the exact expansion is +1, consistent
    #     with split multiplicative reduction (local factor 1 - T).
    a11 = eta[BAD_PRIME]
    assert a11 == 1
    W["a11"] = ("a_11 = +1 read off the exact eta expansion; local factor "
                "at the bad prime 11 is 1 - T (split multiplicative "
                "reduction: 11 | Delta, 11 does not divide c4; "
                "classification criterion imported)")

    # (g) Euler local-global: a_n = prod_{p^v || n} a_{p^v} from the exact
    #     local coefficient sequences reproduces the eta expansion for ALL
    #     n <= 100 (bad prime included via a_{11^v} = 1).
    local = {p: coefficient_sequence_from_satake(satake_of(p, table[p][1]), 8)
             for p in GOOD_PRIMES}
    for n in range(1, NEULER + 1):
        prod = Fraction(1)
        for p, v in factorize(n).items():
            if p == BAD_PRIME:
                prod *= Fraction(a11) ** v         # (1 - T)^{-1}: a_{11^v}=1
            else:
                prod *= local[p][v]
        assert prod == eta[n], (n, prod, eta[n])
    W["euler"] = (f"a_n rebuilt multiplicatively from the exact local "
                  f"factors (deg-2 at good p, 1 - T at 11) equals the eta "
                  f"expansion coefficient for ALL n <= {NEULER}")
    return W


# --- 7. exact Sym^2 at p = 2, 3 -------------------------------------------

def run_sym2(table):
    """op_sym2 -> integral degree-3 Satake polynomial at p = 2, 3, with the
    closed form asserted, Ext^2 = Tate twist asserted, tensor-square
    decomposition asserted, A6 tensor compatibility, and a detect run on the
    Sym^2 coefficient sequence (degree 3: purity NECESSARY_ONLY)."""
    out = []
    for p in (2, 3):
        ap = table[p][1]
        sat = satake_of(p, ap)
        ps = power_sums_from_satake(sat, 6)        # p_1..p_6 of Frob_p
        s2 = op_sym2(ps, 3)                        # p_1..p_3 of Sym^2
        sat3 = satake_poly_from_power_sums(s2, 3)  # degree-3 Satake
        assert is_integer_poly(sat3), (p, sat3)
        # closed form: [1, -(a^2-p), p a^2 - p^2, -p^3]
        A = Fraction(ap)
        expected = [Fraction(1), -(A * A - p), p * A * A - Fraction(p) ** 2,
                    -Fraction(p) ** 3]
        assert sat3 == expected, (p, sat3, expected)
        # Sym^2 purity bookkeeping: product of inverse roots = p^3 = (p^2)^{3/2}
        assert sat3[3] == -Fraction(p) ** 3
        # Ext^2 of the degree-2 object is the determinant = weight-2 Tate
        # twist: power sums exactly [p, p^2, p^3].
        e2 = op_ext2(ps, 3)
        assert e2 == [Fraction(p), Fraction(p) ** 2, Fraction(p) ** 3], (p, e2)
        # tensor square decomposes exactly: p_k(E (x) E) = p_k(Sym^2) + p_k(Ext^2)
        tens = op_tensor(ps, ps, 3)
        assert tens == [s2[k] + e2[k] for k in range(3)], p
        # A6: the degree-4 tensor-square factor Sym^2 * Ext^2 is exactly
        # what tensor_compatibility reconstructs from two copies of sat.
        sat4 = poly_mul(sat3, [Fraction(1), Fraction(-p)])
        prod_series = coefficient_sequence_from_satake(sat4, 10)
        t6 = tensor_compatibility(sat, sat, prod_series)
        assert t6["status"] == "HOLDS", (p, t6)
        # detect on the Sym^2 coefficient sequence, claimed weight (p, 2).
        s3series = coefficient_sequence_from_satake(sat3, SYM2_WINDOW)
        v = detect(s3series, mode="coefficients", weight=(p, 2),
                   holdout=HOLDOUT)
        d = v.as_dict()
        assert d["refusal"] is None, (p, d)
        got = {c["axiom"]: c["status"] for c in d["cells"]}
        assert got == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                       "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                       "A5_HELD_OUT": "HOLDS"}, (p, got)
        a4 = next(c for c in d["cells"] if c["axiom"] == "A4_PURITY")
        # degree 3 > 2: the detector's purity verdict is NECESSARY_ONLY and
        # we record that honestly.
        assert a4["rigor"] == "NECESSARY_ONLY", (p, a4)
        out.append({
            "prime": p, "a_p": ap,
            "sym2_satake": [str(int(c)) for c in sat3],
            "closed_form": "[1, -(a_p^2-p), p a_p^2 - p^2, -p^3]",
            "ext2_power_sums": [str(int(c)) for c in e2],
            "tensor_decomposition":
                "p_k(E x E) == p_k(Sym^2) + p_k(Ext^2) exactly, k <= 3",
            "tensor_A6": t6,
            "sym2_detect": d,
            "purity_note": ("Sym^2 has degree 3: detector purity at weight "
                            "(p,2) is NECESSARY_ONLY (self-reciprocity), "
                            "unlike the COMPLETE degree-2 test for E itself"),
        })
    return out


# --- 8. world record -------------------------------------------------------

def build_world(inv, table, W, detector_runs, sym2_runs):
    hasse1936 = ("H. Hasse (1936), Zur Theorie der abstrakten elliptischen "
                 "Funktionenkoerper I-III (RH for elliptic function fields)")
    modularity = ("A. Wiles (1995), Modular elliptic curves and Fermat's "
                  "Last Theorem; R. Taylor, A. Wiles (1995); C. Breuil, "
                  "B. Conrad, F. Diamond, R. Taylor (2001); for THIS curve "
                  "already classical: E = X_0(11), M. Eichler (1954), "
                  "G. Shimura (1958)")

    ap_str = ", ".join(f"a_{p}={table[p][1]}" for p in GOOD_PRIMES)

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=("Delta = -161051 = -(11^5) != 0 computed exactly from "
                     "the a-invariants (0,-1,1,-10,-20); identities "
                     "4b8 = b2 b6 - b4^2 and c4^3 - c6^2 = 1728 Delta "
                     "asserted; Delta % p != 0 for every good p <= 97 "
                     "(good reduction proved here for these p); rational "
                     "point (5,5) on E verified; L(E,s) well-defined for "
                     "Re s > 3/2 by the Hasse bound (" + W["hasse"][:60] +
                     "...)"),
            citation=("invariant formulas: J. Silverman, The Arithmetic of "
                      "Elliptic Curves (1986), III.1; convergence via " +
                      hasse1936)),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=(W["hecke"] + "; " + W["euler"] +
                     "; per-prime witnesses proved here for p <= 97 / "
                     "n <= 100; multiplicativity for ALL n imported "
                     "(Hecke theory via modularity)"),
            citation=("E. Hecke (1937), Euler products for modular forms; "
                      + modularity)),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=(W["euler"] + "; " + W["a11"] +
                     "; the full Euler product over all p converges for "
                     "Re s > 3/2 by the Hasse bound (imported for all p)"),
            citation=(hasse1936 + "; Hasse-Weil L-function: H. Hasse "
                      "(1930s), A. Weil (1952)")),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "PROVED_HERE",
            witness=("uniform degree 2 at every good prime: the detector "
                     "reconstructs P/Q = 1/(1 - a_p T + p T^2) "
                     "(Berlekamp-Massey certified on 12 exact terms, "
                     "held-out tail of 4 predicted exactly) at ALL 24 good "
                     "p <= 97; degree 1 factor 1 - T at p = 11; bounded "
                     "degree for all p imported (good/bad reduction "
                     "dichotomy)"),
            citation="J. Silverman (1986); J. Tate (1975), algorithm for "
                     "singular fibres"),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=(W["selfdual"] + "; " + W["hasse"][:80] + "... — local "
                     "data pure of weight 1 and exactly self-dual under "
                     "alpha -> p/alpha at every good p <= 97 (proved "
                     "here); coherence with the weight-2 self-dual "
                     "functional equation s <-> 2-s imported"),
            citation=(hasse1936 + "; self-duality of L(E,s): Hecke theory "
                      "via " + modularity)),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("conductor N = 11: proved-here support computation "
                     "(11 | Delta = -11^5, 11 does not divide c4 = 496 => "
                     "multiplicative reduction => conductor exponent 1; "
                     "criterion imported); gamma factor (2 pi)^{-s} "
                     "Gamma(s); root number epsilon = +1, so Lambda(s) = "
                     "11^{s/2} (2 pi)^{-s} Gamma(s) L(E,s) = "
                     "+ Lambda(2-s)"),
            citation=("J. Tate (1975), Algorithm for determining the type "
                      "of a singular fibre (Antwerp IV); epsilon and FE "
                      "via modularity: E. Hecke (1936/37); tabulated for "
                      "11a: J. Cremona, Algorithms for Modular Elliptic "
                      "Curves (1992/1997); CITATION-NEEDED: preferred "
                      "primary reference for the root-number computation "
                      "at level 11 (Atkin-Lehner eigenvalue)")),
        "L6_CONTINUATION_FE": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("L(E,s) = L(f,s) for the unique newform f in "
                     "S_2(Gamma_0(11)); hence entire continuation and "
                     "functional equation Lambda(s) = Lambda(2-s) by "
                     "Hecke theory. Exact finite consistency witness "
                     "computed here: " + W["eta_match"]),
            citation=(modularity + "; continuation/FE for newforms: "
                      "E. Hecke (1936/37); CITATION-NEEDED: classical "
                      "identification of eta(z)^2 eta(11z)^2 with the "
                      "level-11 newform (dim S_2(Gamma_0(11)) = 1 = genus "
                      "X_0(11); eta-quotient criteria, e.g. Ligozat 1975)")),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("exact local witnesses proved here at p = 2, 3: "
                     "op_sym2 gives the INTEGRAL degree-3 Satake factor "
                     "[1, -(a_p^2-p), p a_p^2 - p^2, -p^3] (p=2: "
                     "[1,-2,4,-8]; p=3: [1,2,-6,-27]); Ext^2 power sums "
                     "exactly [p, p^2, p^3] (det = Tate twist); tensor "
                     "square decomposes exactly as Sym^2 (+) Ext^2; A6 "
                     "tensor_compatibility HOLDS for the degree-4 product "
                     "factor. Global automorphy of the lifts imported: "
                     "Sym^2 f on GL(3), Rankin-Selberg f x f, all "
                     "symmetric powers"),
            citation=("S. Gelbart, H. Jacquet (1978), GL(2) -> GL(3) "
                      "symmetric square lift; R. Rankin (1939), A. Selberg "
                      "(1940), convolution; J. Newton, J. Thorne (2021), "
                      "symmetric power functoriality for holomorphic "
                      "modular forms")),
        "L8_REALIZATION": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("triple realization: automorphic (weight-2 newform of "
                     "level 11 on GL(2)/Q), motivic (h^1(E), pure of "
                     "weight 1), and modular-geometric (E IS the modular "
                     "curve X_0(11); the modular parametrization has "
                     "degree 1). Exact finite consistency witness: point "
                     "counts = eta-product coefficients for all good "
                     "p <= 97 (proved here)"),
            citation=(modularity + "; X_0(11) has genus 1; CITATION-NEEDED:"
                      " standard reference identifying X_0(11) with the "
                      "isogeny class 11a (e.g. Ligozat 1975, Antwerp "
                      "tables)")),
        # L9 SPLIT with care (house style of this pass): the explicit
        # formula for L(E,s) IS a theorem given modularity, but the
        # positivity of the corresponding Weil functional is EQUIVALENT to
        # GRH for L(E,s) and is OPEN.  No independent positivity input over
        # Q is known.
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "CONJECTURAL", "OPEN",
            witness=("SPLIT: (i) the explicit formula pairing zeros of "
                     "L(E,s) against prime data {a_{p^k}} HOLDS as an "
                     "IMPORTED_THEOREM (it needs only the continuation/FE "
                     "from modularity); (ii) POSITIVITY of the associated "
                     "Weil functional on the relevant test-function class "
                     "is EQUIVALENT to GRH for L(E,s) and is OPEN; no "
                     "independent positivity mechanism (no analogue of the "
                     "Castelnuovo/Hodge-index input that closes the "
                     "function-field case) is known for this world"),
            citation=("explicit formula framework: A. Weil (1952); for "
                      "elliptic-curve L-functions: J.-F. Mestre (1986), "
                      "Formules explicites et minorations de conducteurs; "
                      "function-field contrast: A. Weil (1948), P. Deligne "
                      "(1974)")),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("supplied by the good/bad reduction of E: degree-2 "
                     "factors 1 - a_p T + p T^2 at good p, 1 - T at 11; " +
                     W["euler"] + " (proved here for n <= 100; all n "
                     "imported via Hecke theory)"),
            citation="H. Hasse (1930s); E. Hecke (1937)"),
        "DUALITY_FE": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("supplied by modularity + Hecke theory (Fricke "
                     "involution w_11 on X_0(11)); exact local shadow "
                     "proved here: " + W["selfdual"]),
            citation=("E. Hecke (1936/37); " + modularity)),
        "TRACE_FORMULA": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("two genuine trace formulas feed this world: (i) a_p "
                     "= tr(Frob_p | H^1(E)) — the Lefschetz/Frobenius "
                     "trace, realized here LITERALLY as the exact point "
                     "count a_p = p + 1 - #E(F_p) at all 24 good p <= 97; "
                     "(ii) the Eichler-Selberg trace formula computes "
                     "tr(T_p | S_2(Gamma_0(11))) = a_p spectrally"),
            citation=("Lefschetz trace for elliptic curves: " + hasse1936 +
                      "; Eichler-Selberg: M. Eichler (1956), A. Selberg "
                      "(1956); CITATION-NEEDED: precise modern statement "
                      "(e.g. D. Zagier's appendix, 1970s)")),
        "POSITIVITY_PURITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("LOCAL purity of weight 1 is a THEOREM and is proved "
                     "here for every good p <= 97: exact integer "
                     "inequalities a_p^2 <= 4p (all strict), equivalently "
                     "both inverse roots of 1 - a_p T + p T^2 have modulus "
                     "p^{1/2} — certified by the COMPLETE exact degree-2 "
                     "purity test (product = p, discriminant < 0) in all "
                     "24 detector runs. SPLIT NOTE — do not conflate: "
                     "local purity comes from positivity on the curve side "
                     "(Hasse's proof; in modern terms Castelnuovo/Hodge-"
                     "index positivity on E x E), one prime at a time. The "
                     "GLOBAL mechanism that would force the zeros of "
                     "L(E,s) itself to the critical line — a positivity "
                     "structure playing that same role over Q — is NOT "
                     "identified and remains OPEN. Local purity is an "
                     "input to, not a proof of, the global critical-line "
                     "statement."),
            citation=(hasse1936 + " (for the class of all elliptic curves "
                      "over finite fields); function-field global "
                      "analogue: A. Weil (1948), P. Deligne (1974)")),
        "TENSOR_OPS": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("exact Sym^2 at p = 2, 3 proved here: op_sym2 -> "
                     "integral degree-3 Satake [1,-2,4,-8] (p=2) and "
                     "[1,2,-6,-27] (p=3), matching the closed form "
                     "[1, -(a_p^2-p), p a_p^2 - p^2, -p^3]; Ext^2 = Tate "
                     "twist ([p, p^2, p^3] power sums); tensor square = "
                     "Sym^2 (+) Ext^2 exactly; A6 tensor_compatibility "
                     "HOLDS; global automorphy of Sym^k f imported "
                     "(Gelbart-Jacquet 1978; Newton-Thorne 2021)"),
            citation=("S. Gelbart, H. Jacquet (1978); J. Newton, "
                      "J. Thorne (2021)")),
        "FAMILY": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("E sits in several structured families: the isogeny "
                     "class 11a (three curves, one L-function); the family "
                     "of all elliptic curves /Q ordered by conductor "
                     "(modular by Wiles et al.); the family of weight-2 "
                     "newforms; quadratic twists E_d with conductor-"
                     "predictable L-functions"),
            citation=("J. Cremona, Algorithms for Modular Elliptic Curves "
                      "(1992/1997); " + modularity)),
    }

    critical_line = {
        "status": "CONJECTURE",
        "detail": ("GRH for L(E,s): all nontrivial zeros on the critical "
                   "line Re s = 1 in the classical weight-2 normalization "
                   "(center s = 1 of the functional equation s <-> 2-s; "
                   "Re s = 1/2 after analytic normalization). Open even "
                   "for this single curve of conductor 11. What IS known: "
                   "entire continuation and FE (modularity); "
                   "L(E,1) != 0 (analytic rank 0, consistent with the "
                   "finite Mordell-Weil group E(Q) = Z/5Z via "
                   "Kolyvagin/Gross-Zagier and BSD work); the LOCAL "
                   "analogue at every good p is a theorem (Hasse) and is "
                   "verified exactly here for p <= 97."),
        "rigor": "OPEN",
        "citation": ("GRH for elliptic-curve L-functions: standard "
                     "conjecture (see e.g. Iwaniec-Kowalski 2004, ch. 5); "
                     "L(E,1) != 0 and rank 0 for 11a: V. Kolyvagin "
                     "(1988-90) framework, B. Gross, D. Zagier (1986); "
                     "CITATION-NEEDED: preferred primary reference for "
                     "rank(11a) = 0 and E(Q) = Z/5Z (classical; Cremona "
                     "tables)"),
        "witness": "",
    }

    world = {
        "id": "elliptic_11a",
        "title": "L-function of the elliptic curve 11a1 (X_0(11))",
        "definition": ("E: y^2 + y = x^3 - x^2 - 10x - 20 over Q, minimal "
                       "model, Delta = -11^5, conductor 11 (E = X_0(11)). "
                       "L(E,s) = prod_{p != 11} (1 - a_p p^{-s} + "
                       "p^{1-2s})^{-1} * (1 - 11^{-s})^{-1} with a_p = "
                       "p + 1 - #E(F_p). Local Satake datum at good p: "
                       "det(1 - Frob_p T) = 1 - a_p T + p T^2 = "
                       "[1, -a_p, p] (low-first). Computed here exactly: " +
                       ap_str + "; a_11 = 1."),
        "arithmetic_class": ("degree-2 motivic L-function over Q, weight 1, "
                             "conductor 11; h^1 of an elliptic curve; "
                             "equivalently the unique weight-2 newform of "
                             "level 11 (eta(z)^2 eta(11z)^2, LMFDB "
                             "11.2.a.a)"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "J. Silverman, The Arithmetic of Elliptic Curves (1986)",
            "J. Cremona, Algorithms for Modular Elliptic Curves "
            "(1992/1997), isogeny class 11a",
            "LMFDB, elliptic curve isogeny class 11.a and newform 11.2.a.a",
            "H. Hasse (1936), RH for elliptic function fields",
            "A. Wiles (1995); R. Taylor, A. Wiles (1995); "
            "C. Breuil, B. Conrad, F. Diamond, R. Taylor (2001)",
            "M. Eichler (1954); G. Shimura (1958), Eichler-Shimura for "
            "X_0(11)",
            "S. Gelbart, H. Jacquet (1978), symmetric square lift",
            "J. Newton, J. Thorne (2021), symmetric power functoriality",
            "J.-F. Mestre (1986), explicit formulas",
            "H. Iwaniec, E. Kowalski (2004), Analytic Number Theory",
        ],
        "rh_established": False,
        "notes": ("This world is the sharpest classical contrast in the "
                  "matrix: EVERY local cell is a theorem with an exact "
                  "witness computed here (point counts, Hasse purity, "
                  "complete degree-2 purity certification at 24 primes, "
                  "Sym^2 integrality), and every global analytic cell is "
                  "a real imported theorem (modularity), yet the global "
                  "POSITIVITY mechanism — the one structural input that "
                  "closes the function-field analogue — has no known "
                  "counterpart, so L9 stays CONJECTURAL and critical_line "
                  "stays CONJECTURE. The Hasse bound holding at every "
                  "prime is LOCAL purity (proved, per prime, by "
                  "positivity on E x E); it does not supply a global "
                  "positivity for L(E,s). All exact witnesses are integer/"
                  "Fraction computations; floats appear nowhere in the "
                  "build. rh_established=false."),
        "detector_runs": {
            "description": ("core.reconstruct.detect on the exact "
                            "coefficient sequence of 1/(1 - a_p T + p T^2) "
                            f"(window {WINDOW}, holdout {HOLDOUT}) with "
                            "purity weight (p, 1) at all 24 good p <= 97 — "
                            "degree 2, so A4 purity is the COMPLETE exact "
                            "test; plus exact Sym^2 runs at p = 2, 3 "
                            "(degree 3: purity NECESSARY_ONLY, recorded "
                            "as such)"),
            "runs": detector_runs,
            "sym2_runs": sym2_runs,
        },
    }
    return world


def main():
    inv = compute_invariants()
    table = build_point_counts()
    W = build_local_witnesses(table)
    W.update(build_global_witnesses(table))
    detector_runs = run_detectors(table)
    sym2_runs = run_sym2(table)
    world = build_world(inv, table, W, detector_runs, sym2_runs)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("a_p:", {p: table[p][1] for p in GOOD_PRIMES})
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector refusals:",
          [r["verdict"]["refusal"] for r in detector_runs])
    print("sym2 satake:", [(r["prime"], r["sym2_satake"]) for r in sym2_runs])


if __name__ == "__main__":
    main()
