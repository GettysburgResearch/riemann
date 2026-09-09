"""World build: dirichlet_mod5 — Dirichlet L-functions mod 5.

Concentrates on the quadratic character chi_5 = Legendre symbol mod 5, with
EXACT arithmetic only (Python ints, Fraction, Fraction-pair Gaussian rationals,
integer vectors in Z[zeta_5]).  No floating point anywhere in this script.

What is computed and asserted exactly here:
  * chi_5(n) by Euler's criterion n^((5-1)/2) mod 5, checked against the
    quadratic-residue table {1,4} mod 5 and 5-periodicity for n <= 200;
  * complete multiplicativity chi_5(mn) = chi_5(m) chi_5(n) for ALL
    1 <= m, n <= 200 (40000 pairs, ramified cases included);
  * finite Euler-product witness: a_n = prod_p chi_5(p)^{v_p(n)} for n <= 200;
  * detector battery (core.reconstruct.detect) on the exact coefficient
    sequence a_k = chi_5(p^k) at primes p in {2,3,7,11,13,19,29} with purity
    claim weight (p, 0), plus the ramified prime p = 5 (local factor 1);
  * Gauss-sum square tau(chi_5)^2 = 5 computed exactly in Z[zeta_5]
    (vectors mod x^5 - 1, canonicalized by 1 + z + z^2 + z^3 + z^4 = 0);
  * splitting law: for every odd prime p <= 200, p != 5,
    #{x mod p : x^2 = 5 mod p} = 1 + chi_5(p)  (an exact finite instance of
    quadratic reciprocity, tying chi_5 to Q(sqrt 5));
  * order-4 character chi4 mod 5 realized in an exact Gaussian-rational class
    (pairs of Fractions), complete multiplicativity for all m, n <= 200, and
    the twist-compatibility witness chi4 * chi4 = chi_5 pointwise on units
    mod 5 (and at every prime p <= 200) — an exact finite L7 witness;
  * chi_5 tensor chi_5 = chi_0 certified by the A6 tensor axiom
    (core.reconstruct.tensor_compatibility) at each test prime;
  * full character table mod 5 over Q(i) with the orthogonality relations
    sum_n chi_i(n) conj(chi_j(n)) = 4 delta_ij verified exactly (16 pairs).

RH/GRH is NOT established by anything here; critical_line is CONJECTURE and
the record embeds rh_established = false.

Deterministic: no input, no randomness, pure exact arithmetic.  Re-run with
    python3 -m worlds.dirichlet_mod5_build
from the pass root to regenerate worlds/dirichlet_mod5.json identically.
"""

import os
from fractions import Fraction

from core.exact import coefficient_sequence_from_satake
from core.reconstruct import detect, tensor_compatibility, HOLDS, SKIPPED
from core.worlds import cell, save_world, validate_world


# ---------------------------------------------------------------------------
# chi_5: the quadratic (Legendre) character mod 5, by Euler's criterion
# ---------------------------------------------------------------------------

def chi5(n: int) -> int:
    """Legendre symbol (n|5) via Euler's criterion, exact integers only.

    chi_5(n) = n^((5-1)/2) mod 5, read in {-1, 0, +1} (4 == -1 mod 5)."""
    if n % 5 == 0:
        return 0
    r = pow(n, (5 - 1) // 2, 5)  # n^2 mod 5
    assert r in (1, 4), f"Euler criterion residue out of range: {r}"
    return 1 if r == 1 else -1


# ---------------------------------------------------------------------------
# Exact Gaussian rationals Q(i): pairs of Fractions.  Enough structure for the
# order-4 character chi4 mod 5 (values in {1, i, -1, -i}).
# ---------------------------------------------------------------------------

class GQ:
    """Gaussian rational a + b i with a, b exact Fractions."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, o):
        return GQ(self.re + o.re, self.im + o.im)

    def __mul__(self, o):
        return GQ(self.re * o.re - self.im * o.im,
                  self.re * o.im + self.im * o.re)

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def conj(self):
        return GQ(self.re, -self.im)

    def __repr__(self):
        return f"({self.re})+({self.im})i"


GQ_ZERO = GQ(0)
GQ_ONE = GQ(1)
GQ_I = GQ(0, 1)


def _build_dlog_base2_mod5() -> dict:
    """Discrete log base 2 on (Z/5)^*: 2 generates the unit group."""
    dlog, x = {}, 1
    for k in range(4):
        dlog[x] = k
        x = (x * 2) % 5
    assert sorted(dlog) == [1, 2, 3, 4], "2 must generate (Z/5)^*"
    return dlog


_DLOG = _build_dlog_base2_mod5()


def chi4(n: int) -> GQ:
    """Order-4 Dirichlet character mod 5 with chi4(2) = i (exact in Q(i))."""
    if n % 5 == 0:
        return GQ_ZERO
    v = GQ_ONE
    for _ in range(_DLOG[n % 5]):
        v = v * GQ_I
    return v


def chi0(n: int) -> GQ:
    """Principal character mod 5."""
    return GQ_ZERO if n % 5 == 0 else GQ_ONE


def chi5_gq(n: int) -> GQ:
    return GQ(chi5(n))


def chi4bar(n: int) -> GQ:
    return chi4(n).conj()


# ---------------------------------------------------------------------------
# Small exact number-theory helpers (no floats)
# ---------------------------------------------------------------------------

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


def factorize(n: int) -> list:
    """Trial division: list of (p, e)."""
    out, d = [], 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out.append((d, e))
        d += 1
    if n > 1:
        out.append((n, 1))
    return out


# ---------------------------------------------------------------------------
# Z[zeta_5] as integer vectors mod x^5 - 1, canonicalized via Phi_5 = 0
# ---------------------------------------------------------------------------

def z5_mul(a: list, b: list) -> list:
    """Multiply two length-5 integer vectors modulo x^5 - 1 (zeta_5^5 = 1)."""
    out = [0] * 5
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[(i + j) % 5] += x * y
    return out


def z5_canonical(a: list) -> list:
    """Canonical representative on basis 1, z, z^2, z^3 using
    1 + z + z^2 + z^3 + z^4 = 0: subtract a[4] * (1,1,1,1,1)."""
    c = a[4]
    return [a[k] - c for k in range(5)]


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def main():
    N = 200
    TEST_PRIMES = [2, 3, 7, 11, 13, 19, 29]   # fixed literal, deterministic
    N_TERMS = 12                               # detector window length
    HOLDOUT = 4

    # --- L0: well-definedness of chi_5 ------------------------------------
    # Euler-criterion table on units must equal the quadratic-residue
    # indicator: squares mod 5 are {1, 4}.
    squares_mod5 = sorted({(x * x) % 5 for x in range(1, 5)})
    assert squares_mod5 == [1, 4]
    table = tuple(chi5(u) for u in (1, 2, 3, 4))
    assert table == (1, -1, -1, 1), table
    for u in range(1, 5):
        assert chi5(u) == (1 if u in (1, 4) else -1)
    # 5-periodicity on 1..N
    for n in range(1, N + 1):
        assert chi5(n) == chi5(n % 5) if n % 5 != 0 else chi5(n) == 0
    l0_witness = ("chi_5 by Euler criterion n^((5-1)/2) mod 5 in exact integer "
                  "arithmetic; unit table (chi(1),chi(2),chi(3),chi(4)) = "
                  f"{table} matches the quadratic-residue set {{1,4}} mod 5; "
                  f"5-periodicity verified for all n <= {N}")

    # --- L1: complete multiplicativity, all pairs m, n <= 200 -------------
    pairs = 0
    for m in range(1, N + 1):
        for n in range(1, N + 1):
            assert chi5(m * n) == chi5(m) * chi5(n), (m, n)
            pairs += 1
    assert pairs == N * N
    l1_witness = (f"chi_5(mn) = chi_5(m) chi_5(n) verified exactly for all "
                  f"1 <= m, n <= {N} ({pairs} pairs, ramified cases "
                  "chi_5(5k) = 0 included)")

    # --- L2: finite Euler-product witness ---------------------------------
    for n in range(1, N + 1):
        prod = 1
        for p, e in factorize(n):
            prod *= chi5(p) ** e
        assert prod == chi5(n), n
    l2_witness = (f"a_n = prod_p chi_5(p)^(v_p(n)) verified exactly against "
                  f"trial-division factorization for all n <= {N}; the formal "
                  "Euler product identity follows from complete "
                  "multiplicativity (L1); analytic convergence for Re(s) > 1 "
                  "is imported")

    # --- Detector runs: exact local reconstruction at test primes ---------
    detector_runs = []
    for p in TEST_PRIMES:
        cp = chi5(p)
        assert cp in (-1, 1)
        # exact coefficient sequence a_k = chi_5(p^k), computed from the
        # character itself (large integer powers, exact)
        series = [Fraction(chi5(p ** k)) for k in range(N_TERMS)]
        # cross-check against the Satake polynomial [1, -chi_5(p)]
        satake = [Fraction(1), Fraction(-cp)]
        assert coefficient_sequence_from_satake(satake, N_TERMS) == series
        v = detect(series, mode="coefficients", weight=(p, 0), holdout=HOLDOUT)
        assert v.refusal is None, (p, v.refusal)
        got = {c["axiom"]: c["status"] for c in v.cells}
        assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                       "A3_INTEGRALITY": HOLDS, "A4_PURITY": HOLDS,
                       "A5_HELD_OUT": HOLDS}, (p, got)
        assert v.object["degree"] == 1, (p, v.object)
        detector_runs.append({"prime": p, "chi5_of_p": cp,
                              "weight_claim": [p, 0],
                              "series_terms": N_TERMS, "holdout": HOLDOUT,
                              "verdict": v.as_dict()})

    # ramified prime p = 5: local factor is 1, coefficient tail is zero
    series5 = [Fraction(chi5(5 ** k)) for k in range(N_TERMS)]
    assert series5 == [Fraction(1)] + [Fraction(0)] * (N_TERMS - 1)
    v5 = detect(series5, mode="coefficients", weight=(5, 0), holdout=HOLDOUT)
    assert v5.refusal is None, v5.refusal
    got5 = {c["axiom"]: c["status"] for c in v5.cells}
    assert got5 == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                    "A3_INTEGRALITY": HOLDS, "A4_PURITY": SKIPPED,
                    "A5_HELD_OUT": HOLDS}, got5
    assert v5.object["degree"] == 0, v5.object
    detector_runs.append({"prime": 5, "chi5_of_p": 0, "weight_claim": [5, 0],
                          "series_terms": N_TERMS, "holdout": HOLDOUT,
                          "note": "ramified prime: local factor L_5(T) = 1; "
                                  "A4 purity vacuous at degree 0",
                          "verdict": v5.as_dict()})
    l3_witness = ("every local factor has degree <= 1: L_p(T) = "
                  "1 - chi_5(p) T for p != 5 and L_5(T) = 1; detect() "
                  "certified deg Q = 1 with A1-A5 all HOLDS at p in "
                  f"{{{', '.join(str(p) for p in TEST_PRIMES)}}} "
                  f"({N_TERMS}-term windows, {HOLDOUT}-term holdout) and "
                  "deg Q = 0 at the ramified prime p = 5")

    # --- L4: self-duality / weight-0 purity -------------------------------
    for u in range(1, 5):
        assert chi5(u) * chi5(u) == 1                       # chi real, unit
        # chi(u) * chi(u^{-1} mod 5) = chi(1) = 1  (inverse = conjugate)
        inv = pow(u, 3, 5)                                  # u^{-1} mod 5
        assert (u * inv) % 5 == 1
        assert chi5(u) * chi5(inv) == 1
    l4_witness = ("chi_5 is real-valued (quadratic): chi = conj(chi) = "
                  "chi^{-1} verified exactly on all units mod 5; weight-0 "
                  "purity holds exactly: the inverse root a = chi_5(p) "
                  "satisfies a^2 = 1 = p^0 (detect A4 complete degree-1 test "
                  "HOLDS at every tested prime)")

    # --- L5: conductor / gamma / root number ------------------------------
    # Primitivity witness: chi_5 nonconstant on units => conductor is 5.
    assert len({chi5(u) for u in range(1, 5)}) == 2
    # Parity: chi_5(-1) = chi_5(4) = +1 => even character, gamma = Gamma_R(s).
    assert chi5(4) == 1
    # Gauss sum tau = sum_{n=1}^{4} chi_5(n) zeta_5^n in Z[zeta_5];
    # exact claim: tau^2 = 5.
    tau = [0, chi5(1), chi5(2), chi5(3), chi5(4)]           # coeff of zeta^n
    tau_sq = z5_canonical(z5_mul(tau, tau))
    assert tau_sq == [5, 0, 0, 0, 0], tau_sq
    l5_witness = ("conductor 5 (primitivity witnessed: chi_5 nonconstant on "
                  "units); chi_5(-1) = chi_5(4) = +1 so the character is even "
                  "and the gamma factor is Gamma_R(s) = pi^{-s/2} Gamma(s/2); "
                  "Gauss sum tau = zeta - zeta^2 - zeta^3 + zeta^4 satisfies "
                  "tau^2 = 5 EXACTLY (computed in Z[zeta_5] as integer "
                  "vectors mod x^5 - 1, canonical witness [5,0,0,0,0]); "
                  "root number tau/sqrt(5) = +1 uses Gauss's sign theorem "
                  "(imported) for tau > 0")

    # --- L7: twist/tensor compatibility -----------------------------------
    # (a) chi4 well-defined and completely multiplicative (exact, Q(i)).
    chi4_table = tuple(chi4(u) for u in (1, 2, 3, 4))
    assert chi4_table == (GQ_ONE, GQ_I, GQ(0, -1), GQ(-1)), chi4_table
    for m in range(1, N + 1):
        for n in range(1, N + 1):
            assert chi4(m * n) == chi4(m) * chi4(n), (m, n)
    # order exactly 4: chi4(2)^4 = 1, chi4(2)^2 != 1
    assert chi4(2) * chi4(2) * chi4(2) * chi4(2) == GQ_ONE
    assert chi4(2) * chi4(2) != GQ_ONE
    # (b) THE twist witness: chi4 * chi4 = chi_5 pointwise on units mod 5.
    for u in range(1, 5):
        assert chi4(u) * chi4(u) == chi5_gq(u), u
    # ... and at every prime p <= 200 (and in fact every n <= 200).
    for n in range(1, N + 1):
        assert chi4(n) * chi4(n) == chi5_gq(n), n
    # (c) chi_5 tensor chi_5 = chi_0: A6 tensor axiom at each test prime.
    tensor_runs = []
    for p in TEST_PRIMES:
        satp = [Fraction(1), Fraction(-chi5(p))]
        # product world = principal character: a_k = chi_0(p^k) = 1 for p != 5
        prod_series = [Fraction(1)] * 8
        a6 = tensor_compatibility(satp, satp, prod_series)
        assert a6["status"] == HOLDS, (p, a6)
        tensor_runs.append({"prime": p, "statement":
                            "chi_5 (x) chi_5 = chi_0 locally at p", "a6": a6})
    l7_witness = ("chi4 * chi4 = chi_5 verified pointwise EXACTLY in Q(i) "
                  "(Fraction pairs) on the units mod 5 — table "
                  "(1, i, -i, -1)^2 = (1, -1, -1, 1) — and for every "
                  f"n <= {N}; chi_5 (x) chi_5 = chi_0 certified by the exact "
                  "A6 tensor axiom (tensor_compatibility) at p in "
                  f"{{{', '.join(str(p) for p in TEST_PRIMES)}}}; the "
                  "character group mod 5 is closed under twisting")

    # --- L8: realization (motivic side: Q(sqrt 5); automorphic: GL(1)) ----
    # Exact splitting-law witness: for odd p != 5, the number of square roots
    # of 5 mod p equals 1 + chi_5(p) — an instance of quadratic reciprocity
    # ((5|p) = (p|5) since 5 = 1 mod 4) checked by brute force.
    odd_primes = [p for p in primes_upto(N) if p not in (2, 5)]
    for p in odd_primes:
        roots = sum(1 for x in range(p) if (x * x - 5) % p == 0)
        assert roots == 1 + chi5(p), (p, roots)
    l8_witness = (f"splitting law verified exactly for all {len(odd_primes)} "
                  f"odd primes p <= {N}, p != 5: #{{x mod p : x^2 = 5}} = "
                  "1 + chi_5(p) (finite instances of quadratic reciprocity, "
                  "(5|p) = (p|5) as 5 = 1 mod 4); chi_5 is the quadratic "
                  "character of Q(sqrt 5), so L(s, chi_5) = "
                  "zeta_{Q(sqrt 5)}(s) / zeta(s); automorphic realization: "
                  "GL(1) Hecke character via class field theory / Tate")

    # --- FAMILY mechanism: full character table + orthogonality -----------
    chars = [("chi_0", chi0), ("chi_4", chi4),
             ("chi_5", chi5_gq), ("chi_4bar", chi4bar)]
    ortho_pairs = 0
    for i, (_, ci) in enumerate(chars):
        for j, (_, cj) in enumerate(chars):
            s = GQ_ZERO
            for u in range(1, 5):
                s = s + ci(u) * cj(u).conj()
            assert s == (GQ(4) if i == j else GQ_ZERO), (i, j, s)
            ortho_pairs += 1
    assert ortho_pairs == 16
    family_witness = ("all 4 Dirichlet characters mod 5 realized exactly "
                      "(chi_0, chi_4, chi_5, chi_4bar; chi_4 of order 4 over "
                      "Q(i)); orthogonality sum_u chi_i(u) conj(chi_j(u)) = "
                      "4 delta_ij verified exactly for all 16 pairs; "
                      "complete multiplicativity of chi_4 verified for all "
                      f"m, n <= {N}")

    # --- Assemble the world record ----------------------------------------
    world = {
        "id": "dirichlet_mod5",
        "title": "Dirichlet L-functions mod 5 (quadratic character chi_5)",
        "definition": (
            "L(s, chi_5) = sum_{n>=1} chi_5(n) n^{-s} = prod_p "
            "(1 - chi_5(p) p^{-s})^{-1}, where chi_5 is the Legendre symbol "
            "mod 5 (the quadratic Dirichlet character of conductor 5, unit "
            "table (1,-1,-1,1)).  Local factor at p != 5: degree 1, Satake "
            "polynomial 1 - chi_5(p) T with T = p^{-s}; at the ramified "
            "prime 5 the local factor is 1.  The order-4 characters chi_4, "
            "chi_4bar mod 5 (values in Q(i)) are carried as exact side "
            "objects; chi_4^2 = chi_5."),
        "arithmetic_class": (
            "EXACT_RATIONAL (integers, Fractions; Gaussian rationals Q(i) as "
            "Fraction pairs; Z[zeta_5] as integer vectors mod x^5 - 1). "
            "No floating point anywhere in the build."),
        "ladder": {
            "L0_WELL_DEFINED": cell(
                "HOLDS", "PROVED_HERE", witness=l0_witness,
                citation="Euler's criterion (Euler, ~1748-1761); Legendre "
                         "symbol (Legendre, 1798)"),
            "L1_MULTIPLICATIVITY": cell(
                "HOLDS", "PROVED_HERE", witness=l1_witness,
                citation="Dirichlet characters: Dirichlet (1837)"),
            "L2_EULER_PRODUCT": cell(
                "HOLDS", "PROVED_HERE", witness=l2_witness,
                citation="Euler product for Dirichlet L-series: Dirichlet "
                         "(1837), after Euler (1737)"),
            "L3_BOUNDED_DEGREE_RATIONAL": cell(
                "HOLDS", "EXACT_WITNESS", witness=l3_witness,
                citation=""),
            "L4_WEIGHT_DUALITY": cell(
                "HOLDS", "PROVED_HERE", witness=l4_witness,
                citation=""),
            "L5_CONDUCTOR_GAMMA_ROOT": cell(
                "HOLDS", "IMPORTED_THEOREM", witness=l5_witness,
                citation="Quadratic Gauss sums: Gauss (1801); sign of the "
                         "Gauss sum: Gauss (1811); standard completed-L "
                         "normalization: CITATION-NEEDED: classical "
                         "19th-century references for conductor-gamma-root "
                         "data of Dirichlet L-functions"),
            "L6_CONTINUATION_FE": cell(
                "HOLDS", "IMPORTED_THEOREM", witness=(
                    "Lambda(s) = (5/pi)^{s/2} Gamma(s/2) L(s, chi_5) "
                    "= Lambda(1 - s) with root number +1 (chi_5 even, "
                    "self-dual); entire continuation"),
                citation="Functional equation and continuation for Dirichlet "
                         "L-functions: classical, theta/Hurwitz-zeta "
                         "methods; CITATION-NEEDED: precise original "
                         "attribution (Hurwitz ~1882 / de la Vallee Poussin "
                         "era)"),
            "L7_TWIST_TENSOR_COMPAT": cell(
                "HOLDS", "PROVED_HERE", witness=l7_witness,
                citation=""),
            "L8_REALIZATION": cell(
                "HOLDS", "IMPORTED_THEOREM", witness=l8_witness,
                citation="Quadratic reciprocity: Gauss (1801); "
                         "L(s,chi) factorization of Dedekind zeta for "
                         "quadratic fields: Dirichlet (1837-1839 era); "
                         "GL(1)/Hecke-character realization: Tate's thesis "
                         "(1950), Hecke (1918-1920)"),
            "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
                "HOLDS", "IMPORTED_THEOREM", witness=(
                    "the explicit formula (zeros of L(s, chi_5) vs. prime "
                    "powers chi_5(p^k) log p) holds unconditionally; the "
                    "POSITIVITY half — Weil's positivity criterion for the "
                    "explicit-formula functional, equivalent to GRH for "
                    "chi_5 — is OPEN and NOT claimed here"),
                citation="Explicit formula: Weil (1952); Guinand (1948); "
                         "von Mangoldt-style forms: CITATION-NEEDED: "
                         "precise Dirichlet-character reference"),
        },
        "mechanisms": {
            "EULER_PRODUCT": cell(
                "HOLDS", "PROVED_HERE", witness=(
                    "supplied by complete multiplicativity of chi_5 "
                    f"(verified exactly for all m, n <= {N}); degree <= 1 "
                    "local factors"),
                citation="Dirichlet (1837)"),
            "DUALITY_FE": cell(
                "HOLDS", "IMPORTED_THEOREM", witness=(
                    "self-dual: chi_5 is real; FE s <-> 1-s with root "
                    "number +1 (tau^2 = 5 exact here; sign of tau imported "
                    "from Gauss)"),
                citation="CITATION-NEEDED: classical functional equation "
                         "for Dirichlet L-functions (Hurwitz ~1882 era)"),
            "TRACE_FORMULA": cell(
                "HOLDS", "IMPORTED_THEOREM", witness=(
                    "GL(1) trace formula = Poisson summation (theta "
                    "transformation underlying the FE); the explicit "
                    "formula plays the spectral-side role, pairing zeros "
                    "against prime powers chi_5(p^k)"),
                citation="Tate's thesis (1950); Weil (1952)"),
            "POSITIVITY_PURITY": cell(
                "OPEN", "OPEN", witness=(
                    "none known as a GRH-forcing mechanism: weight-0 purity "
                    "|chi_5(p)| = 1 is trivially exact (a^2 = 1 = p^0 "
                    "witnessed at every tested prime by detect A4), but no "
                    "positivity / self-adjointness / Frobenius-weight "
                    "structure is known that forces the zeros of "
                    "L(s, chi_5) onto Re(s) = 1/2"),
                citation=""),
            "TENSOR_OPS": cell(
                "HOLDS", "PROVED_HERE", witness=(
                    "character group mod 5 (cyclic of order 4) closed under "
                    "tensor: chi_4^2 = chi_5, chi_5^2 = chi_0 — chi_4^2 "
                    f"verified exactly in Q(i) for all n <= {N}, chi_5 (x) "
                    "chi_5 = chi_0 certified by exact A6 tensor axiom at "
                    f"{len(TEST_PRIMES)} primes"),
                citation=""),
            "FAMILY": cell(
                "HOLDS", "PROVED_HERE", witness=family_witness,
                citation="Dirichlet (1837)"),
        },
        "critical_line": {
            "status": "CONJECTURE",
            "detail": (
                "GRH for L(s, chi_5): all nontrivial zeros on Re(s) = 1/2. "
                "Unproved.  Known unconditionally: L(1, chi_5) != 0 "
                "(Dirichlet) and a classical zero-free region near "
                "Re(s) = 1; nothing in this record moves the conjecture."),
            "rigor": "OPEN",
            "citation": (
                "GRH for Dirichlet L-functions (generalization of Riemann "
                "1859; commonly attributed to the Piltz era, ~1884 — "
                "CITATION-NEEDED for the precise origin); zero-free "
                "regions: de la Vallee Poussin (1896-1899)"),
            "witness": "",
        },
        "sources": [
            "Dirichlet (1837), primes in arithmetic progressions "
            "(introduction of Dirichlet characters and L-series)",
            "Gauss, Disquisitiones Arithmeticae (1801): quadratic "
            "reciprocity, Gauss sums",
            "Gauss (1811): sign of the quadratic Gauss sum",
            "Tate's thesis (1950): GL(1) automorphic realization, FE via "
            "Poisson summation",
            "Weil (1952): explicit formula and positivity criterion "
            "equivalent to GRH",
            "de la Vallee Poussin (1896-1899): zero-free regions for "
            "Dirichlet L-functions",
            "CITATION-NEEDED: precise original reference for the "
            "functional equation of Dirichlet L-functions (Hurwitz ~1882 "
            "era)",
        ],
        "rh_established": False,
        "notes": (
            "Order-4 characters chi_4, chi_4bar (a conjugate pair, values "
            "in Q(i), conductor 5): ODD (chi_4(-1) = chi_4(4) = -1, "
            "verified exactly in this build), hence gamma factor "
            "Gamma_R(s + 1); non-self-dual, dual(chi_4) = chi_4bar; their "
            "L-functions are not treated by the Q-rational detector here "
            "(coefficients lie in Z[i]), but their exact character-level "
            "structure is: complete multiplicativity (all m, n <= 200) and "
            "chi_4^2 = chi_5 are proved exactly above.  GRH for the "
            "order-4 L-functions is equally CONJECTURE.  Detector refusal "
            "semantics were never triggered: all runs completed with "
            "refusal = None."),
        "detector_runs": {
            "coefficient_battery": detector_runs,
            "tensor_battery": tensor_runs,
        },
    }

    # chi_4 parity claim in the notes must itself be checked exactly:
    assert chi4(4) == GQ(-1)

    probs = validate_world(world)
    assert not probs, probs
    out_dir = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "worlds")
    path = save_world(world, out_dir)
    print(f"wrote {path}")
    print("dirichlet_mod5: all exact assertions passed; "
          "rh_established=false")


if __name__ == "__main__":
    main()
