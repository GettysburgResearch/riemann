"""World 'beurling': Beurling generalized prime systems as a corpus row.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.beurling_build

regenerates worlds/beurling.json identically.

TWO SUB-RECORDS IN ONE WORLD FILE (scoped inside cell witnesses and notes):

(a) IMPORTED row — the Diamond-Montgomery-Vorhauer style CONTINUUM system:
    a Beurling generalized prime system whose integer counting function is
    regular enough to yield PNT-type asymptotics, while its zeta analogue
    nevertheless has zeros violating the RH analogue.  Everything about (a)
    is IMPORTED_THEOREM with conservative statements and CITATION-NEEDED
    flags (a boundary audit will fix attributions).  Nothing about (a) is
    computed here.

(b) EXACT discrete toy (SYNTHETIC_CONTROL) — generalized primes are the
    ordinary primes with 2 replaced by TWO copies of 3:

        P_B = multiset {3, 3, 5, 7, 11, 13, ...}

    Generalized integers = the free commutative monoid on P_B, mapped to N
    by multiplication; the Beurling zeta counts monoid elements by size:

        zeta_B(s) = sum_n b_n n^{-s},   b_n = #{monoid elements of size n}
                  = prod over q in P_B (1 - q^{-s})^{-1}
                  = zeta(s) * (1 - 2^{-s}) / (1 - 3^{-s}).

    Closed form (proved coefficient-wise below): b_n = 0 for even n, and
    b_n = v_3(n) + 1 for odd n (the two indistinguishable copies of 3 give
    multiplicity v+1 at 3-adic valuation v).

    ALL computations for (b) are exact Fraction arithmetic; every claim is
    asserted before being embedded as a witness string.  Exact results:
      - b_n computed to n-level N = 3^8 = 6561 by Dirichlet convolution
        b = u * f * g with u = coefficients of zeta (all ones), f = coeffs
        of (1 - 2^{-s}), g = coeffs of (1 - 3^{-s})^{-1};
      - Euler product over the generalized-prime multiset verified
        coefficient-wise EXACTLY for all n <= 3^8 (PROVED_HERE);
      - closed form verified exactly for all n <= 3^8;
      - multiplicativity b_{mn} = b_m b_n for ALL coprime pairs mn <= 3^8;
        non-TOTAL multiplicativity witness: b_9 = 3 != b_3^2 = 4;
      - bounded-degree rational local factors certified by
        minimal_rational_form: degree 0 at p=2, degree 2 at p=3
        (1/(1-T)^2), degree 1 at p=5,7 (uniform bound 2);
      - exact density: sum_{n<=3^8} b_n = 4925 with |S - 3N/4| = 17/4,
        matching the exact residue (1-1/2)/(1-1/3) = 3/4 of zeta_B at s=1;
      - detector runs (core.reconstruct.detect) at p = 2, 3, 5;
      - direct-sum (union-of-prime-multisets) structure and a formal tensor
        check on local data, all exact.

ROLE IN THE MATRIX: Euler product WITHOUT duality — the complement of the
davenport_heilbronn row (duality without Euler product).  L6 is OPEN, not
FAILS: no functional equation for a Beurling system is known to us, but
nonexistence is not proved.  rh_established=false throughout; no floats
appear anywhere in this file.
"""

from fractions import Fraction
from math import gcd

from core.exact import (
    F,
    coefficient_sequence_from_satake,
    minimal_rational_form,
    op_direct_sum,
    op_dual_satake,
    poly_mul,
    power_sums_from_satake,
    satake_poly_from_power_sums,
)
from core.reconstruct import detect, tensor_compatibility
from core.worlds import cell, validate_world, save_world

N = 3 ** 8            # 6561: exact coefficient window for the toy
KMAX3 = 11            # 3-column extended to 3^11 for a window-12 detector run

CN_DMV = ("CITATION-NEEDED: Diamond-Montgomery-Vorhauer (~2006), Beurling "
          "primes with large oscillation; Zhang (Beurling PNT results); "
          "note Hilberdink and Debruyne-Vindas refinements")


# ---------------------------------------------------------------------------
# exact arithmetic helpers (Fractions only)
# ---------------------------------------------------------------------------

def sieve_primes(n):
    """Deterministic sieve of Eratosthenes up to n inclusive."""
    mark = [True] * (n + 1)
    mark[0] = mark[1] = False
    p = 2
    while p * p <= n:
        if mark[p]:
            for m in range(p * p, n + 1, p):
                mark[m] = False
        p += 1
    return [i for i in range(2, n + 1) if mark[i]]


def dirichlet_conv(a, b):
    """Exact Dirichlet convolution of arrays indexed 1..N (index 0 unused)."""
    out = [Fraction(0)] * (N + 1)
    for i in range(1, N + 1):
        ai = a[i]
        if ai == 0:
            continue
        for j in range(1, N // i + 1):
            if b[j] != 0:
                out[i * j] += ai * b[j]
    return out


def v3(n):
    v = 0
    while n % 3 == 0:
        v += 1
        n //= 3
    return v


# ---------------------------------------------------------------------------
# the exact toy: coefficients, Euler product, closed form, density
# ---------------------------------------------------------------------------

def build_toy_witnesses():
    W = {}

    # --- coefficient arrays of the three factors -------------------------
    u = [Fraction(0)] + [Fraction(1)] * N            # zeta: a_n = 1
    f = [Fraction(0)] * (N + 1)                      # 1 - 2^{-s}
    f[1] = Fraction(1)
    f[2] = Fraction(-1)
    g = [Fraction(0)] * (N + 1)                      # (1 - 3^{-s})^{-1}
    k = 1
    while k <= N:
        g[k] = Fraction(1)
        k *= 3

    # --- b = u * f * g : DEFINITION of the toy's Dirichlet coefficients --
    b = dirichlet_conv(dirichlet_conv(u, f), g)
    assert b[1] == 1

    # --- closed form: b_n = 0 (n even), v_3(n)+1 (n odd), exact all n<=N -
    for n in range(1, N + 1):
        expected = Fraction(0) if n % 2 == 0 else Fraction(v3(n) + 1)
        assert b[n] == expected, (n, b[n], expected)
    W["closed_form"] = (
        "b_n computed exactly as the triple Dirichlet convolution "
        "zeta * (1-2^{-s}) * (1-3^{-s})^{-1} and verified for ALL n <= 3^8 "
        "= 6561 to equal the closed form: b_n = 0 for even n, "
        "b_n = v_3(n)+1 for odd n; e.g. b_1..b_12 = "
        + ",".join(str(b[n]) for n in range(1, 13)))

    # --- Euler product over the generalized-prime MULTISET, exact --------
    # multiset {3, 3, 5, 7, 11, ...}: 2 deleted, 3 doubled, deterministic
    # ascending order.  Multiplying by (1-q^{-s})^{-1} = sum_k q^{-ks} is
    # the increasing-order in-place recurrence e[m] += e[m//q].
    gen_primes = [3, 3] + [p for p in sieve_primes(N) if p not in (2, 3)]
    e = [Fraction(0)] * (N + 1)
    e[1] = Fraction(1)
    for q in gen_primes:
        for m in range(q, N + 1, q):
            e[m] += e[m // q]
    for n in range(1, N + 1):
        assert e[n] == b[n], (n, e[n], b[n])
    W["euler"] = (
        "Euler product identity verified coefficient-wise EXACTLY: the "
        "truncated product over the generalized-prime multiset {3,3,5,7,"
        "11,...} (all generalized primes <= 6561; 2 deleted, 3 doubled) "
        "reproduces b_n for ALL n <= 3^8 = 6561 (Fraction arithmetic). "
        "Coefficients at level n depend only on factors with q <= n, so "
        "the same computation run at every N proves the formal-Dirichlet-"
        "series identity zeta_B = prod_{q in P_B} (1-q^{-s})^{-1}")

    # --- multiplicativity: ALL coprime pairs with mn <= N ----------------
    for m in range(1, N + 1):
        for n in range(1, N // m + 1):
            if gcd(m, n) == 1:
                assert b[m * n] == b[m] * b[n], (m, n)
    # non-TOTAL multiplicativity witness (contrast with zeta):
    assert b[3] == 2 and b[9] == 3 and b[3] * b[3] == 4 != b[9]
    W["mult"] = (
        "b_{mn} = b_m b_n verified exactly for ALL coprime pairs (m,n) "
        "with mn <= 6561; b is multiplicative but NOT totally "
        "multiplicative: b_9 = 3 != b_3^2 = 4 (exact witness) — the two "
        "indistinguishable copies of 3 break total multiplicativity")

    # --- exact density / residue at s = 1 --------------------------------
    S = sum(b[1:], Fraction(0))
    assert S == 4925
    defect = abs(S - Fraction(3 * N, 4))
    assert defect == Fraction(17, 4) and defect < 10
    residue = (1 - Fraction(1, 2)) / (1 - Fraction(1, 3))
    assert residue == Fraction(3, 4)
    W["density"] = (
        "exact generalized-integer density check: sum_{n<=6561} b_n = 4925 "
        "and |4925 - 3N/4| = 17/4 < 10 (N = 6561), matching the exact "
        "residue of zeta_B at s = 1: (1-1/2)/(1-1/3) = 3/4 — the toy's "
        "counting function is regular, N_B(x) ~ (3/4) x")

    # --- local factors at rational primes: certified rational forms ------
    # grouped by RATIONAL prime p, the local factor of zeta_B is:
    #   p = 2 : 1               (prime deleted)      degree 0
    #   p = 3 : (1 - T)^{-2}    (prime doubled)      degree 2
    #   p >= 5: (1 - T)^{-1}                          degree 1
    seq2 = [b[2 ** k] for k in range(13)]            # 2^12 = 4096 <= N
    seq3 = [b[3 ** k] for k in range(9)]             # 3^8  = 6561 <= N
    seq5 = [b[5 ** k] for k in range(6)]             # 5^5  = 3125 <= N
    seq7 = [b[7 ** k] for k in range(5)]             # 7^4  = 2401 <= N
    mr2 = minimal_rational_form(seq2)
    mr3 = minimal_rational_form(seq3)
    mr5 = minimal_rational_form(seq5)
    mr7 = minimal_rational_form(seq7)
    assert mr2 == ([Fraction(1)], [Fraction(1)])
    assert mr3 == ([Fraction(1)], [Fraction(1), Fraction(-2), Fraction(1)])
    assert mr5 == ([Fraction(1)], [Fraction(1), Fraction(-1)])
    assert mr7 == ([Fraction(1)], [Fraction(1), Fraction(-1)])
    # (1-T)^2 == [1,-2,1] exactly:
    assert poly_mul([Fraction(1), Fraction(-1)],
                    [Fraction(1), Fraction(-1)]) == mr3[1]
    W["local"] = (
        "minimal_rational_form certificates (Berlekamp-Massey, exact, "
        "full-window verified): p=2 -> P/Q = 1/1 (degree 0, prime "
        "deleted); p=3 -> 1/(1-T)^2 = 1/[1,-2,1] (degree 2, prime "
        "doubled); p=5,7 -> 1/(1-T) (degree 1). Grouped by rational prime "
        "the degrees are uniformly bounded by 2; grouped by generalized "
        "prime q every factor is (1-q^{-s})^{-1} of degree 1")

    return W, b, seq3


def build_3column_extended():
    """The 3-power column b_{3^k} for k <= KMAX3, computed HONESTLY as the
    full triple Dirichlet convolution (u*f*g)(3^k) over all divisor triples
    of 3^k (divisors of 3^k are exactly 3^j, j <= k).  This extends the
    3-level window beyond N for a window-12 detector run."""
    def u_val(n):
        return Fraction(1)

    def f_val(n):
        if n == 1:
            return Fraction(1)
        if n == 2:
            return Fraction(-1)
        return Fraction(0)

    def g_val(n):
        while n % 3 == 0:
            n //= 3
        return Fraction(1) if n == 1 else Fraction(0)

    col = []
    for k in range(KMAX3 + 1):
        n = 3 ** k
        total = Fraction(0)
        d1 = 1
        while d1 <= n:
            if n % d1 == 0:
                rest = n // d1
                d2 = 1
                while d2 <= rest:
                    if rest % d2 == 0:
                        total += u_val(d1) * f_val(d2) * g_val(rest // d2)
                    d2 += 1
            d1 += 1
        col.append(total)
    # closed form at the 3-column: b_{3^k} = k + 1
    assert col == [Fraction(k + 1) for k in range(KMAX3 + 1)]
    return col


# ---------------------------------------------------------------------------
# detector runs and structure checks (all exact)
# ---------------------------------------------------------------------------

def run_detector(b3col, seq3):
    runs = []

    # consistency: extended 3-column agrees with the full convolution
    assert b3col[:9] == seq3

    # p = 3 (doubled prime): window 12, purity weight (3, 0), holdout 4.
    v3run = detect(b3col[:12], mode="coefficients", weight=(3, 0), holdout=4)
    d = v3run.as_dict()
    assert d["refusal"] is None, d
    got = {c["axiom"]: c["status"] for c in d["cells"]}
    assert got == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                   "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                   "A5_HELD_OUT": "HOLDS"}, got
    assert d["object"]["degree"] == 2
    assert d["object"]["numerator"] == "[1]"
    assert d["object"]["denominator"] == "[1, -2, 1]"
    runs.append({"prime": 3, "weight": [3, 0], "mode": "coefficients",
                 "series": "b_{3^k} = k+1 (doubled prime), window 12",
                 "verdict": d})

    # p = 2 (deleted prime): window 13, holdout 4. Degree-0 local factor;
    # A4 is SKIPPED (vacuous for degree 0) — recorded honestly.
    seq2w = [Fraction(1)] + [Fraction(0)] * 12
    v2run = detect(seq2w, mode="coefficients", weight=(2, 0), holdout=4)
    d2 = v2run.as_dict()
    assert d2["refusal"] is None, d2
    got2 = {c["axiom"]: c["status"] for c in d2["cells"]}
    assert got2 == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                    "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "SKIPPED",
                    "A5_HELD_OUT": "HOLDS"}, got2
    assert d2["object"]["degree"] == 0
    runs.append({"prime": 2, "weight": [2, 0], "mode": "coefficients",
                 "series": "b_{2^k} = [1,0,0,...] (deleted prime), window 13",
                 "verdict": d2})

    # p = 5 (untouched prime): all-ones window 12, weight (5, 0).
    v5run = detect([Fraction(1)] * 12, mode="coefficients", weight=(5, 0),
                   holdout=4)
    d5 = v5run.as_dict()
    assert d5["refusal"] is None, d5
    got5 = {c["axiom"]: c["status"] for c in d5["cells"]}
    assert got5 == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                    "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                    "A5_HELD_OUT": "HOLDS"}, got5
    assert d5["object"]["degree"] == 1
    assert d5["object"]["denominator"] == "[1, -1]"
    runs.append({"prime": 5, "weight": [5, 0], "mode": "coefficients",
                 "series": "b_{5^k} = 1 (untouched prime), window 12",
                 "verdict": d5})

    return runs


def run_structure_checks():
    """Exact structural facts about the toy's local data.

    (1) DIRECT SUM = union of generalized-prime multisets.  The class-level
        monoidal operation on Beurling systems is UNION of prime multisets,
        which multiplies the zetas; at each rational prime it is the direct
        sum of local Satake data.  Exact check at p=3: the toy is
        {odd primes} union {3}, and op_direct_sum of two trivial rank-1
        data reproduces the certified local factor [1,-2,1].
    (2) formal TENSOR calculus applies to the local data (no global
        meaning is claimed): [1,-2,1] (x) [1,-1] predicts the sequence
        b_{3^k} = k+1 exactly (A6-style check).
    (3) exact local self-duality (vacuous: all inverse roots equal 1).
    """
    out = []

    sat3 = [Fraction(1), Fraction(-2), Fraction(1)]     # (1-T)^2
    sat1 = [Fraction(1), Fraction(-1)]                  # 1-T

    # (1) direct sum
    ones = power_sums_from_satake(sat1, 12)
    assert ones == [Fraction(1)] * 12
    ds = op_direct_sum(ones, ones, 12)
    assert ds == [Fraction(2)] * 12
    satds = satake_poly_from_power_sums(ds[:2], 2)
    assert satds == sat3
    out.append({
        "name": "union_is_direct_sum",
        "detail": ("union of generalized-prime multisets = direct sum of "
                   "local Satake data: op_direct_sum([1]*12,[1]*12) -> "
                   "power sums [2]*12 -> Satake [1,-2,1], exactly the "
                   "certified local factor of the toy at p=3"),
        "result": {"status": "HOLDS", "rigor": "EXACT_RATIONAL",
                   "witness": "satake_poly_from_power_sums == [1, -2, 1]"}})

    # (2) formal tensor check on local data
    prod_series = [Fraction(k + 1) for k in range(9)]   # coeffs of 1/(1-T)^2
    t = tensor_compatibility(sat3, sat1, prod_series)
    assert t["status"] == "HOLDS", t
    out.append({
        "name": "formal_tensor_on_local_data",
        "detail": ("[1,-2,1] (x) [1,-1] predicts b_{3^k} = k+1 exactly "
                   "(A6-style); records only that the exact tensor "
                   "CALCULUS applies to local data — no global tensor "
                   "structure on Beurling systems is claimed"),
        "result": t})

    # (3) exact local self-duality (trivial: all inverse roots are 1)
    assert op_dual_satake(sat3, Fraction(1)) == sat3
    assert op_dual_satake(sat1, Fraction(1)) == sat1
    # every inverse root a = 1 satisfies a^2 == p^0 == 1 at each prime
    for p in (2, 3, 5, 7):
        a = Fraction(1)
        assert a * a == Fraction(p) ** 0
    out.append({
        "name": "vacuous_local_self_duality",
        "detail": ("op_dual_satake fixes [1,-2,1] and [1,-1] exactly; all "
                   "inverse roots equal 1, pure of weight 0 (a^2 == p^0). "
                   "This locally exact self-duality is VACUOUS: it feeds "
                   "no global duality/functional equation (see L6)"),
        "result": {"status": "HOLDS", "rigor": "EXACT_RATIONAL",
                   "witness": "op_dual_satake(sat)==sat; a=1, a^2==p^0"}})

    return out


# ---------------------------------------------------------------------------
# the world record
# ---------------------------------------------------------------------------

def build_world(W, detector_runs, structure_checks):
    beurling1937 = ("A. Beurling (1937), generalized primes and integers "
                    "(introduced the class)")

    ladder = {
        # L0: the toy is an explicit combinatorial construction, exact; the
        # class is Beurling's (imported).  Exact density witness included.
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=("TOY: free commutative monoid on the multiset "
                     "{3,3,5,7,11,...}; " + W["closed_form"] + "; "
                     + W["density"] + ". 0 <= b_n <= v_3(n)+1 <= "
                     "log_3(n)+1, so the Dirichlet series converges for "
                     "Re s > 1. CLASS: Beurling systems are well-defined "
                     "for any nondecreasing sequence of reals > 1"),
            citation=beurling1937),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("TOY: " + W["mult"] + ". The general statement for "
                     "all coprime m,n follows from the Euler product over "
                     "the generalized-prime multiset (standard formal-"
                     "Dirichlet-series argument, each coefficient involves "
                     "finitely many factors)"),
            citation=""),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("TOY: " + W["euler"] + ". CLASS: every Beurling "
                     "system has an Euler product BY CONSTRUCTION — this "
                     "world isolates the Euler-product mechanism with no "
                     "duality attached"),
            citation=beurling1937),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("TOY: " + W["local"] + ". CLASS: local factors of any "
                     "Beurling system are degree-1 in q^{-s} per "
                     "generalized prime by construction; bounded degree "
                     "per RATIONAL prime holds for the toy (bound 2) but "
                     "is not meaningful for continuum systems (imported "
                     "row (a)), whose 'primes' are not integers"),
            citation=""),
        # L4: honest OPEN — exact local self-duality is vacuous, no weight/
        # duality structure is known for Beurling systems, and we cannot
        # prove nonexistence.
        "L4_WEIGHT_DUALITY": cell(
            "OPEN", "OPEN",
            witness=("TOY: local self-duality holds exactly but VACUOUSLY "
                     "(all inverse roots equal 1, weight 0: see "
                     "structure_checks.vacuous_local_self_duality). No "
                     "weight/duality structure coherent with a global "
                     "functional equation is known for the toy or for any "
                     "Beurling system; nonexistence is not proved, so the "
                     "cell is OPEN, not FAILS"),
            citation=""),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "OPEN", "OPEN",
            witness=("no canonical conductor, gamma factor, or root "
                     "number is known for any Beurling system. TOY: the "
                     "elementary factor (1-2^{-s})/(1-3^{-s}) has zeros "
                     "and poles on Re s = 0 in periodic progressions "
                     "(2 pi i k / log 2, 2 pi i k / log 3); no gamma-"
                     "factor completion producing a self-dual xi is known "
                     "to us"),
            citation=""),
        # L6: OPEN per honest split — continuation of the toy HOLDS
        # (inherited from zeta), but no functional equation is known, and
        # the ladder cell requires both.  NOT claimed FAILS.
        "L6_CONTINUATION_FE": cell(
            "OPEN", "OPEN",
            witness=("SPLIT. (i) TOY continuation HOLDS: the coefficient "
                     "identity zeta_B = zeta * (1-2^{-s})/(1-3^{-s}) is "
                     "proved here exactly (it is the definition b = u*f*g "
                     "plus the Euler-product verification), and the right "
                     "side continues meromorphically to C since zeta does "
                     "(imported: Riemann 1859); the elementary factor "
                     "only adds zeros/poles on Re s = 0. (ii) FUNCTIONAL "
                     "EQUATION: none is known for the toy or for ANY "
                     "Beurling system — and nonexistence is unproved, so "
                     "the cell is OPEN, not FAILS. (iii) CLASS: for "
                     "general Beurling systems even continuation beyond "
                     "the convergence abscissa is unavailable without "
                     "regularity hypotheses on the counting function"),
            citation=("continuation of zeta: B. Riemann (1859); class "
                      "regularity/continuation: " + CN_DMV)),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "OPEN", "OPEN",
            witness=("no canonical twist or tensor theory exists for "
                     "Beurling systems (no characters, no Rankin-Selberg). "
                     "Exact structure found: the class carries a DIRECT-SUM "
                     "monoidal operation (union of generalized-prime "
                     "multisets = product of zetas), verified exactly at "
                     "p=3 (structure_checks.union_is_direct_sum); the "
                     "formal tensor calculus applies to the toy's local "
                     "data (structure_checks.formal_tensor_on_local_data, "
                     "A6-style HOLDS) but carries no known global meaning"),
            citation=""),
        "L8_REALIZATION": cell(
            "HOLDS", "SYNTHETIC_CONTROL",
            witness=("TOY: combinatorial realization BY CONSTRUCTION — "
                     "the free commutative monoid on {3,3,5,7,11,...} with "
                     "the size homomorphism into (N, *); this world is a "
                     "deliberate synthetic control. IMPORTED row (a): the "
                     "DMV-style system is realized as a continuum measure "
                     "(prime-counting measure chosen by construction). No "
                     "automorphic, motivic, spectral, or dynamical "
                     "realization is known for either — that ABSENCE is "
                     "the point of the row"),
            citation=CN_DMV),
        # L9: the class-level imported obstruction.  FAILS is scoped to the
        # CLASS: a member with regular counting and RH-analogue-violating
        # zeros exists (imported theorem), so no class-wide explicit-
        # formula positivity principle can exist.  The toy's own L9 is
        # open (equivalent to classical RH; see critical_line).
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "FAILS", "IMPORTED_THEOREM",
            witness=("CLASS-LEVEL FAILS (imported row (a)): there exists a "
                     "Beurling generalized prime system whose integer "
                     "counting function is regular enough to yield PNT-"
                     "type asymptotics (with de la Vallee Poussin-shape "
                     "error), while its zeta analogue has zeros violating "
                     "the RH analogue (zeros approaching Re s = 1); hence "
                     "NO explicit-formula positivity principle can hold "
                     "uniformly over the Beurling class — Euler product + "
                     "regular counting do NOT force positivity. Stated "
                     "conservatively; attribution flagged for audit. "
                     "TOY-LEVEL: open — equivalent to classical RH via "
                     "the exact factorization (see critical_line)"),
            citation=CN_DMV),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("supplied by the free-monoid construction itself "
                     "(unique factorization into generalized primes holds "
                     "BY FIAT in the monoid). TOY: " + W["euler"]),
            citation=beurling1937),
        "DUALITY_FE": cell(
            "OPEN", "OPEN",
            witness=("no Beurling system with a genuine functional "
                     "equation is known to us — flagged as a discovery "
                     "question. The toy inherits meromorphic continuation "
                     "from zeta but no reflection s -> 1-s; the class was "
                     "designed to isolate the Euler product mechanism "
                     "WITHOUT duality (complement of davenport_heilbronn, "
                     "which has duality without Euler product)"),
            citation=""),
        "TRACE_FORMULA": cell(
            "OPEN", "OPEN",
            witness=("no unconditional explicit-formula/trace identity is "
                     "known for the toy or the class; Tauberian and "
                     "explicit-formula-style analyses of Beurling zetas "
                     "exist only under supplementary regularity "
                     "hypotheses on the counting functions"),
            citation=("CITATION-NEEDED: Debruyne-Vindas complex Tauberian "
                      "theorems with applications to Beurling primes "
                      "(~2016-2018); Diamond-Zhang monograph on Beurling "
                      "generalized numbers (~2016)")),
        "POSITIVITY_PURITY": cell(
            "OPEN", "OPEN",
            witness=("no positivity/purity mechanism is known. TOY: local "
                     "weight-0 purity holds exactly but vacuously (all "
                     "inverse roots equal 1); this supplies nothing "
                     "global. CLASS: the imported row (a) shows regular "
                     "counting + Euler product do not force an RH "
                     "analogue, so any candidate positivity mechanism "
                     "must come from structure the class lacks (duality? "
                     "spectral realization?) — precisely the missing-"
                     "mechanism contrast this row contributes to the "
                     "matrix"),
            citation=CN_DMV),
        "TENSOR_OPS": cell(
            "OPEN", "OPEN",
            witness=("only a DIRECT-SUM monoidal structure is present "
                     "(union of generalized-prime multisets = product of "
                     "zetas), verified exactly at p=3: op_direct_sum of "
                     "two trivial rank-1 local data reproduces the "
                     "certified [1,-2,1]. The formal tensor calculus on "
                     "local data works exactly (A6-style check HOLDS) but "
                     "no global tensor/twist structure on Beurling "
                     "systems is known"),
            citation=""),
        "FAMILY": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("the Beurling class is a genuine continuum family "
                     "containing ordinary zeta (prime multiset = ordinary "
                     "primes), the exact toy (this record), and RH-"
                     "analogue-violating members (imported row (a)). "
                     "Family membership supplies NO rigidity here — the "
                     "family is anti-rigid, which is exactly its value as "
                     "a control: it shows which mechanisms (Euler product, "
                     "regular counting) are INSUFFICIENT"),
            citation=(beurling1937 + "; " + CN_DMV)),
    }

    critical_line = {
        "status": "OPEN",
        "detail": ("SPLIT ACROSS THE TWO SUB-RECORDS. TOY (b): the "
                   "elementary factor (1-2^{-s})/(1-3^{-s}) has all its "
                   "zeros and poles on Re s = 0 (|2^{-s}| = 1 iff Re s = "
                   "0), so in the open strip 0 < Re s < 1 the zeros of "
                   "zeta_B coincide exactly with those of zeta; the RH "
                   "analogue for the toy is therefore EQUIVALENT to the "
                   "classical Riemann Hypothesis — OPEN. CLASS/IMPORTED "
                   "(a): the RH analogue FAILS for specific Beurling "
                   "systems with regular counting (zeros approaching "
                   "Re s = 1; imported theorem, attribution flagged), so "
                   "no class-wide critical-line statement is even "
                   "formulable. Recorded status is OPEN, scoped to the "
                   "exact object (b) of this record; rh_established="
                   "false"),
        "rigor": "OPEN",
        "citation": ("classical RH: B. Riemann (1859); class-level "
                     "failure: " + CN_DMV),
        "witness": ("exact input to the toy reduction: the coefficient "
                    "identity zeta_B = zeta * (1-2^{-s})/(1-3^{-s}) is "
                    "verified coefficient-wise for all n <= 3^8 in this "
                    "build (PROVED_HERE); the strip-zero identification "
                    "is elementary analysis on top of it"),
    }

    world = {
        "id": "beurling",
        "title": "Beurling generalized prime systems",
        "definition": (
            "Beurling generalized prime system: any multiset P_B of reals "
            "> 1 (the 'generalized primes'), with generalized integers the "
            "free commutative monoid on P_B and zeta_B(s) = prod_{q in "
            "P_B} (1 - q^{-s})^{-1}. Sub-record (a), IMPORTED: a Diamond-"
            "Montgomery-Vorhauer style continuum system with regular "
            "integer counting whose zeta analogue violates the RH "
            "analogue. Sub-record (b), EXACT TOY (synthetic control): "
            "P_B = {3,3,5,7,11,13,...} (ordinary primes, 2 replaced by "
            "two copies of 3); zeta_B(s) = zeta(s) (1-2^{-s})/(1-3^{-s}) "
            "= sum b_n n^{-s} with b_n = 0 for even n and v_3(n)+1 for "
            "odd n (proved coefficient-wise here to n = 3^8 = 6561)"),
        "arithmetic_class": (
            "Beurling generalized prime systems (synthetic-control "
            "class); toy member: elementary rational modification of "
            "zeta; imported member: DMV-style continuum system"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "A. Beurling (1937), on generalized primes and integers "
            "(class definition)",
            "CITATION-NEEDED: H. G. Diamond, H. L. Montgomery, U. M. A. "
            "Vorhauer (~2006), Beurling primes with large oscillation",
            "CITATION-NEEDED: W.-B. Zhang, results on the prime number "
            "theorem for Beurling generalized numbers",
            "CITATION-NEEDED: T. Hilberdink, well-behaved Beurling "
            "systems and moments of zeta analogues",
            "CITATION-NEEDED: G. Debruyne, J. Vindas, complex Tauberian "
            "theorems with applications to Beurling generalized primes "
            "(~2016-2018)",
            "CITATION-NEEDED: H. G. Diamond, W.-B. Zhang, monograph on "
            "Beurling generalized numbers (AMS, ~2016)",
        ],
        "rh_established": False,
        "notes": (
            "ROLE: Euler product WITHOUT duality — the complement of the "
            "davenport_heilbronn row (duality without Euler product). TWO "
            "SUB-RECORDS scoped inside cells: (a) IMPORTED continuum "
            "system (all such content is IMPORTED_THEOREM with "
            "conservative statements and CITATION-NEEDED flags for the "
            "boundary audit; nothing about (a) is computed here); (b) "
            "EXACT discrete toy, a SYNTHETIC_CONTROL: every claim about "
            "it is computed and asserted in beurling_build.py with "
            "Fraction arithmetic — Dirichlet convolution to n = 3^8 = "
            "6561, coefficient-wise Euler product verification over the "
            "multiset {3,3,5,7,...}, closed form b_n = [n odd](v_3(n)+1), "
            "full coprime multiplicativity check, non-total-"
            "multiplicativity witness b_9 = 3 != b_3^2 = 4, certified "
            "local factors (degrees 0/2/1 at p = 2/3/5), exact density "
            "sum b_n = 4925 vs 3N/4 (residue 3/4), detector runs, and "
            "exact direct-sum/tensor/duality structure checks. L6 is "
            "OPEN, not FAILS: no functional equation for a Beurling "
            "system is known to us (flagged as a discovery question), "
            "but nonexistence is unproved. L9 FAILS is scoped to the "
            "CLASS via the imported row; the toy's critical-line "
            "question is equivalent to classical RH and remains OPEN. "
            "No floats were used anywhere in this build. "
            "rh_established=false."),
        "detector_runs": {
            "description": (
                "core.reconstruct.detect on exact toy local data: p=3 "
                "(doubled prime, window 12, weight (3,0), holdout 4 — "
                "degree-2 local factor [1,-2,1], all axioms HOLD "
                "including the complete degree-2 purity test); p=2 "
                "(deleted prime, window 13 — degree-0 factor, A4 "
                "honestly SKIPPED as vacuous); p=5 (untouched prime, "
                "window 12 — degree-1 factor [1,-1], all axioms HOLD). "
                "Plus exact structure checks: union-of-multisets = "
                "direct sum of Satake data; formal tensor calculus; "
                "vacuous local self-duality"),
            "runs": detector_runs,
            "structure_checks": structure_checks,
        },
    }
    return world


def main():
    W, b, seq3 = build_toy_witnesses()
    b3col = build_3column_extended()
    detector_runs = run_detector(b3col, seq3)
    structure_checks = run_structure_checks()
    world = build_world(W, detector_runs, structure_checks)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector refusals:",
          [r["verdict"]["refusal"] for r in detector_runs])


if __name__ == "__main__":
    main()
