"""World build: counterfeit_wrong_gamma — the gamma-mismatch obstruction row.

OBJECT.  Lambda_wrong(s) = pi^{-(s+1)/2} Gamma((s+1)/2) L(s, chi_5), where
chi_5 is the EVEN quadratic Dirichlet character mod 5 (Legendre symbol, unit
table (1,-1,-1,1), chi_5(-1) = +1).  The attached archimedean factor
Gamma_R(s+1) = pi^{-(s+1)/2} Gamma((s+1)/2) is the standard factor for ODD
characters; the canonical completion of L(s, chi_5) uses
Gamma_R(s) = pi^{-s/2} Gamma(s/2) (parity a = (1 - chi(-1))/2 = 0).  The
finite part (coefficients, Euler product, degree-1 local factors) is
untouched; ONLY the archimedean dressing is counterfeited.  Role in the
pass: the row witnessing #764 axis H — archimedean data is NOT a free
parameter.

THEOREM (proved here, elementary).  There is NO constant w (in particular
none with |w| = 1) such that
    Lambda_wrong(s) = w Lambda_wrong(1-s)
as an identity of meromorphic functions; moreover no renormalization
c N^{s/2} Lambda_wrong (c != 0, N > 0) admits such an FE either.

IMPORTED INGREDIENTS (and nothing else analytic):
 (i)   Gamma is meromorphic on C, NOWHERE ZERO, with simple poles exactly at
       the nonpositive integers 0, -1, -2, ...  (Euler 1729; Weierstrass
       ~1856: 1/Gamma is entire with zeros exactly there); the special
       values Gamma(1) = 1, Gamma(1/2) = pi^{1/2}, and the recursion
       Gamma(z+1) = z Gamma(z) (hence Gamma(3/2) = (1/2) pi^{1/2},
       Gamma(m+1) = m!).
 (ii)  The TRUE completed functional equation:
       Lambda_true(s) = (5/pi)^{s/2} Gamma(s/2) L(s, chi_5) is entire and
       Lambda_true(s) = Lambda_true(1-s)  (classical Dirichlet-L FE, chi_5
       even primitive quadratic mod 5, root number +1; imported, same as in
       the sibling world dirichlet_mod5).
 (iii) The identity theorem for meromorphic functions (two meromorphic
       functions agreeing off a discrete set agree everywhere).

PROOF.  Set
    G(s) = [pi^{-(s+1)/2} Gamma((s+1)/2)] / [pi^{-s/2} Gamma(s/2)]
         = pi^{-1/2} Gamma((s+1)/2) / Gamma(s/2).
By (i), G is meromorphic on C with zeros exactly at
    Z0 = {0, -2, -4, ...}      (the poles of Gamma(s/2)),
and poles exactly at
    P0 = {-1, -3, -5, ...}     (the poles of Gamma((s+1)/2)).
Z0 and P0 are disjoint by parity (even vs. odd — exact integer check
below), so there is no cancellation and every zero/pole of G is simple.

Since Lambda_wrong(s) = G(s) 5^{-s/2} Lambda_true(s), the assumed FE plus
(ii) gives, wherever everything is defined,
    G(s) 5^{-s/2} Lambda_true(s) = w G(1-s) 5^{-(1-s)/2} Lambda_true(1-s)
                                 = w G(1-s) 5^{-(1-s)/2} Lambda_true(s).
Lambda_true is entire and not identically zero: Lambda_true(2)
= 5 pi^{-1} L(2, chi_5) with L(2, chi_5) >= 49/100 > 0, PROVED EXACTLY
below (partial sum S_100 in exact Fractions plus the telescoping tail bound
sum_{n>N} n^{-2} < sum_{n>N} 1/(n(n-1)) = 1/N).  So the zero set of
Lambda_true is discrete; dividing it off and applying (iii),
    G(s) = w 5^{(2s-1)/2} G(1-s)
as an identity of meromorphic functions on all of C.

Now compare the two sides at s = 0.
  LHS: ord_{s=0} G = +1 — a SIMPLE ZERO (Gamma(s/2) has a simple pole at
       s = 0, and Gamma((0+1)/2) = Gamma(1/2) is finite and nonzero).
  RHS: 5^{(2s-1)/2} = exp(((2s-1)/2) log 5) is entire and nowhere zero, and
       G(1-0) = G(1) = [Gamma(1) pi^{-1}] / [Gamma(1/2) pi^{-1/2}]
              = pi^{-1/2} / Gamma(1/2) = 1/pi,
       computed EXACTLY below in the monomial ring {c pi^a 5^b : c,a,b in Q}
       with the imported reductions Gamma(1) = 1, Gamma(1/2) = pi^{1/2}.
       1/pi is finite and NONZERO (1 lies in neither Z0 nor P0), so for
       w != 0 the RHS has ord_{s=0} = 0.
Order 1 != order 0: CONTRADICTION — the zero of G at s = 0 reflects to
s = 1, where a zero would have to sit, but G(1) = 1/pi.  If instead w = 0,
the FE forces Lambda_wrong == 0, contradicting
Lambda_wrong(2) = pi^{-3/2} Gamma(3/2) L(2, chi_5) = L(2, chi_5) / (2 pi)
>= 49/(200 pi) > 0 (exact lower bound on L(2, chi_5) again).  Finally,
replacing Lambda_wrong by c N^{s/2} Lambda_wrong multiplies both sides of
the displayed meromorphic identity by nowhere-zero entire factors and
changes no zero/pole order, so the identical contradiction applies: no
constant/conductor renormalization rescues the wrong gamma.  QED.

REMARK 1 (every zero and every pole breaks, not just s = 0).  The
reflection s -> 1-s maps Z0 = {0,-2,-4,...} to {1,3,5,...} and
P0 = {-1,-3,...} to {2,4,6,...}; G is holomorphic and nonvanishing at every
positive integer (positive integers lie in neither Z0 nor P0).  Verified
below by exact integer bookkeeping for the first 51 elements of each set.

REMARK 2 (second, independent refutation by direct pole transport).
Lambda_wrong has a GENUINE simple pole at s = -1: Gamma((s+1)/2) has a
simple pole there, and L(-1, chi_5) != 0 because the true FE gives
Lambda_true(-1) = Lambda_true(2) = 5 pi^{-1} L(2, chi_5) != 0 while the
completion factors of Lambda_true are finite and nonzero at s = -1 (the
argument -1/2 of Gamma(s/2) is not a pole, and Gamma is nowhere zero).
But Lambda_wrong is holomorphic at 1-(-1) = 2, so
Lambda_wrong(s) = w Lambda_wrong(1-s) is impossible near s = -1 for every
constant w: the left side blows up, the right side stays bounded.  More
generally Lambda_wrong has genuine simple poles at every s = -(2k+1):
L(-(2k+1), chi_5) != 0 since Lambda_true(-(2k+1)) = Lambda_true(2k+2) =
(5/pi)^{k+1} k! L(2k+2, chi_5) and L(2k+2, chi_5) > 3/4 for k >= 1 by the
uniform elementary bound |L(2k+2, chi_5) - 1| <= sum_{n>=2} n^{-(2k+2)}
<= 4^{-k} sum_{n>=2} n^{-2} < 4^{-k} <= 1/4 (using n^{-2k} <= 2^{-2k} for
n >= 2, and the telescoping bound sum_{n>=2} n^{-2} < 1).  So the wrong
completion is NOT EVEN ENTIRE, while Lambda_true is.

REMARK 3 (non-realizability of the completed object as a Dirichlet
series).  At s = 2m+1 the completion factor equals m! pi^{-(m+1)} exactly
(Gamma(m+1) = m!), so with pi < 4 (Archimedes) and L(2m+1, chi_5) > 1/2
(same uniform bound, sum_{n>=2} n^{-3} < 1/2), we get
Lambda_wrong(2m+1) > (1/2) m! / 4^{m+1} -> infinity; every Dirichlet
series convergent in some half-plane tends to its FIRST COEFFICIENT a_1
(finite) along the real axis.  Hence Lambda_wrong is not a Dirichlet
series and lies in no Dirichlet-series-based class (Selberg class, etc.).
The exact rationals F_m = m!/4^{m+1} satisfy F_{m+1}/F_m = (m+1)/4 >= 2
for m >= 7 — checked exactly below up to m = 40.

DEEPER RIGIDITY ANCHORS (imported, not used in the proof): Hamburger
(1921-1922), the Riemann zeta function is determined by its functional
equation; and 'CITATION-NEEDED: gamma-factor uniqueness in the Selberg
class (Kaczorowski-Perelli context)'.

RH/GRH is NOT established (or even addressed) by anything here; the record
embeds rh_established = false and critical_line = NOT_FORMULATED for the
wrong completion (the underlying L(s, chi_5) keeps its usual, unproved GRH
conjecture — see the sibling world dirichlet_mod5).

Deterministic: no input, no randomness, exact arithmetic only (integers,
Fractions, and exact monomials c * pi^a * 5^b with c, a, b in Q).  No
floating point anywhere.  Re-run with
    python3 -m worlds.counterfeit_wrong_gamma_build
from the pass root to regenerate worlds/counterfeit_wrong_gamma.json
identically.
"""

import math
import os
from fractions import Fraction

from core.exact import coefficient_sequence_from_satake
from core.reconstruct import detect, tensor_compatibility, HOLDS, SKIPPED
from core.worlds import cell, save_world, validate_world


# ---------------------------------------------------------------------------
# chi_5: the even quadratic character mod 5 (same construction as the
# sibling world dirichlet_mod5, kept self-contained here)
# ---------------------------------------------------------------------------

def chi5(n: int) -> int:
    """Legendre symbol (n|5) via Euler's criterion, exact integers only."""
    if n % 5 == 0:
        return 0
    r = pow(n, (5 - 1) // 2, 5)
    assert r in (1, 4), f"Euler criterion residue out of range: {r}"
    return 1 if r == 1 else -1


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
# Exact monomials c * pi^a * 5^b with c, a, b in Q.  This is enough to
# evaluate the Gamma-ratio G at integers exactly, given the IMPORTED
# reductions Gamma(1) = 1 and Gamma(1/2) = pi^{1/2} (and the recursion for
# Gamma(3/2)).  pi and 5^{1/2} are multiplicatively independent over Q with
# these exponents tracked formally; equality of monomials is equality of
# (coeff, pi-exponent, 5-exponent) triples — no floats anywhere.
# ---------------------------------------------------------------------------

class PiMono:
    """Exact monomial c * pi^a * 5^b, with c, a, b Fractions."""

    __slots__ = ("c", "a", "b")

    def __init__(self, c, a=0, b=0):
        self.c = Fraction(c)
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __mul__(self, o):
        return PiMono(self.c * o.c, self.a + o.a, self.b + o.b)

    def __truediv__(self, o):
        assert o.c != 0, "division by zero monomial"
        return PiMono(self.c / o.c, self.a - o.a, self.b - o.b)

    def __eq__(self, o):
        return (self.c, self.a, self.b) == (o.c, o.a, o.b)

    def is_zero(self):
        return self.c == 0

    def __repr__(self):
        return f"({self.c}) * pi^({self.a}) * 5^({self.b})"


# Imported special values (see docstring ingredient (i)):
GAMMA_1 = PiMono(1, 0, 0)                      # Gamma(1) = 1
GAMMA_HALF = PiMono(1, Fraction(1, 2), 0)      # Gamma(1/2) = pi^{1/2}
GAMMA_3HALF = PiMono(Fraction(1, 2), Fraction(1, 2), 0)  # (1/2) Gamma(1/2)


# ---------------------------------------------------------------------------
# Zero/pole bookkeeping for G(s) = pi^{-1/2} Gamma((s+1)/2) / Gamma(s/2).
# Membership predicates for the two arithmetic progressions (exact ints):
#   Z0 = zeros of G  = poles of Gamma(s/2)      = {0, -2, -4, ...}
#   P0 = poles of G  = poles of Gamma((s+1)/2)  = {-1, -3, -5, ...}
# ---------------------------------------------------------------------------

def in_Z0(x: int) -> bool:
    return x <= 0 and x % 2 == 0


def in_P0(x: int) -> bool:
    return x <= -1 and x % 2 == 1


def main():
    N = 200
    TEST_PRIMES = [2, 3, 7, 11, 13, 19, 29]   # fixed literal, deterministic
    N_TERMS = 12
    HOLDOUT = 4
    K_REFLECT = 50                            # zeros/poles checked: k = 0..50

    # =====================================================================
    # PART A — the finite part is an honest, untouched Dirichlet series
    # =====================================================================

    # --- L0: chi_5 well-defined, even; Lambda_wrong well-defined ----------
    table = tuple(chi5(u) for u in (1, 2, 3, 4))
    assert table == (1, -1, -1, 1), table
    for n in range(1, N + 1):
        assert chi5(n) == (chi5(n % 5) if n % 5 != 0 else 0)
    # evenness: chi_5(-1) = chi_5(4) = +1 (Python (-1) % 5 == 4, exact)
    assert chi5(-1) == chi5(4) == 1
    parity_canonical = (1 - chi5(-1)) // 2
    parity_attached = 1                        # Gamma_R(s + 1) was attached
    assert parity_canonical == 0
    assert parity_attached != parity_canonical
    l0_witness = (
        "Lambda_wrong is a well-defined meromorphic function on C: chi_5 "
        "well-defined by Euler's criterion (unit table "
        f"(chi(1),chi(2),chi(3),chi(4)) = {table}, 5-periodicity checked "
        f"for all n <= {N}, evenness chi_5(-1) = chi_5(4) = +1 exact); the "
        "Dirichlet series converges absolutely for Re(s) > 1 (|chi_5| <= 1, "
        "comparison with sum n^{-sigma}, elementary); L(s, chi_5) is entire "
        "(imported) and the completion factor pi^{-(s+1)/2} Gamma((s+1)/2) "
        "is meromorphic and nowhere zero (imported Gamma facts). "
        "WELL-DEFINED but WRONGLY COMPLETED: definedness is not at issue; "
        "canonicity is (see L5).")

    # --- L1: complete multiplicativity, all pairs m, n <= 200 -------------
    pairs = 0
    for m in range(1, N + 1):
        for n in range(1, N + 1):
            assert chi5(m * n) == chi5(m) * chi5(n), (m, n)
            pairs += 1
    assert pairs == N * N
    l1_witness = (
        f"chi_5(mn) = chi_5(m) chi_5(n) verified exactly for all 1 <= m, n "
        f"<= {N} ({pairs} pairs, ramified cases chi_5(5k) = 0 included); "
        "the counterfeit does not touch the coefficients")

    # --- L2: finite Euler-product witness ---------------------------------
    for n in range(1, N + 1):
        prod = 1
        for p, e in factorize(n):
            prod *= chi5(p) ** e
        assert prod == chi5(n), n
    l2_witness = (
        f"a_n = prod_p chi_5(p)^(v_p(n)) verified exactly against "
        f"trial-division factorization for all n <= {N}; the formal Euler "
        "product follows from complete multiplicativity (L1); analytic "
        "convergence for Re(s) > 1 is imported.  The Euler product belongs "
        "to the FINITE part and is untouched by the wrong gamma")

    # --- L3: bounded-degree rational local factors, detector battery ------
    detector_runs = []
    for p in TEST_PRIMES:
        cp = chi5(p)
        assert cp in (-1, 1)
        series = [Fraction(chi5(p ** k)) for k in range(N_TERMS)]
        satake = [Fraction(1), Fraction(-cp)]
        assert coefficient_sequence_from_satake(satake, N_TERMS) == series
        v = detect(series, mode="coefficients", weight=(p, 0),
                   holdout=HOLDOUT)
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
    l3_witness = (
        "every local factor has degree <= 1: L_p(T) = 1 - chi_5(p) T for "
        "p != 5 and L_5(T) = 1; detect() certified deg Q = 1 with A1-A5 all "
        f"HOLDS at p in {{{', '.join(str(p) for p in TEST_PRIMES)}}} "
        f"({N_TERMS}-term windows, {HOLDOUT}-term holdout) and deg Q = 0 at "
        "the ramified prime p = 5.  Identical to the true world "
        "dirichlet_mod5: the counterfeit lives entirely at infinity")

    # --- L4: finite duality untouched; archimedean incoherence booked at L5
    for u in range(1, 5):
        assert chi5(u) * chi5(u) == 1
        inv = pow(u, 3, 5)
        assert (u * inv) % 5 == 1
        assert chi5(u) * chi5(inv) == 1
    l4_witness = (
        "finite local data remain self-dual and weight-0 pure, exactly as "
        "in the true world: chi_5 is real-valued, chi_5(u) chi_5(u^{-1}) = 1 "
        "on all units mod 5 (exact), and the inverse root a = chi_5(p) "
        "satisfies a^2 = 1 = p^0.  The ARCHIMEDEAN parity incoherence is "
        "real — attached parity a = 1 (factor Gamma_R(s+1)) vs canonical "
        "a = (1 - chi_5(-1))/2 = 0 with chi_5(-1) = chi_5(4) = +1, an exact "
        "mismatch 1 != 0 — but in this schema that datum belongs to L5 "
        "(canonical conductor+gamma+root), where it is booked as FAILS with "
        "proof.  L4 records that the counterfeit did NOT touch the finite "
        "duality structure")

    # =====================================================================
    # PART B — the exact obstruction: no FE for the wrong completion
    # =====================================================================

    # --- B1: zero/pole sets of G and their disjointness (parity) ----------
    zeros_first = [-2 * k for k in range(6)]
    poles_first = [-(2 * k + 1) for k in range(6)]
    for k in range(K_REFLECT + 1):
        z = -2 * k
        p = -(2 * k + 1)
        assert in_Z0(z) and not in_P0(z), z          # zeros: even <= 0
        assert in_P0(p) and not in_Z0(p), p          # poles: odd <= -1
    # disjointness is parity: no integer is both even and odd
    for x in range(-2 * K_REFLECT - 1, 1):
        assert not (in_Z0(x) and in_P0(x)), x

    # --- B2: reflection s -> 1-s sends every zero/pole to a regular,
    #         nonvanishing point of G (a positive integer) -----------------
    refl_zeros_first = [1 - z for z in zeros_first]
    refl_poles_first = [1 - p for p in poles_first]
    assert refl_zeros_first == [1, 3, 5, 7, 9, 11]
    assert refl_poles_first == [2, 4, 6, 8, 10, 12]
    for k in range(K_REFLECT + 1):
        rz = 1 - (-2 * k)          # = 2k + 1, a positive odd integer
        rp = 1 - (-(2 * k + 1))    # = 2k + 2, a positive even integer
        assert rz >= 1 and not in_Z0(rz) and not in_P0(rz), rz
        assert rp >= 2 and not in_Z0(rp) and not in_P0(rp), rp

    # --- B3: EXACT evaluation G(1) = 1/pi ---------------------------------
    #   G(1) = [Gamma(1) pi^{-1}] / [Gamma(1/2) pi^{-1/2}]
    # in the exact monomial ring, with imported Gamma(1)=1, Gamma(1/2)=pi^{1/2}
    num = GAMMA_1 * PiMono(1, Fraction(-1), 0)
    den = GAMMA_HALF * PiMono(1, Fraction(-1, 2), 0)
    assert den == PiMono(1, 0, 0)              # Gamma(1/2) pi^{-1/2} = 1
    G_at_1 = num / den
    assert G_at_1 == PiMono(1, Fraction(-1), 0), G_at_1   # G(1) = pi^{-1}
    assert not G_at_1.is_zero()
    # RHS of the meromorphic identity at s = 0 equals w * 5^{-1/2} * G(1):
    rhs_at_0_unit = PiMono(1, 0, Fraction(-1, 2)) * G_at_1
    assert rhs_at_0_unit == PiMono(1, Fraction(-1), Fraction(-1, 2))
    assert not rhs_at_0_unit.is_zero()         # nonzero for every w != 0

    # --- B4: order mismatch at s = 0 (the contradiction) ------------------
    ord_lhs_at_0 = 1     # simple zero of G at 0 (simple pole of Gamma(s/2))
    ord_rhs_at_0 = 0     # w * (entire nowhere-zero) * G(1), G(1) = 1/pi != 0
    assert ord_lhs_at_0 != ord_rhs_at_0

    # --- B5: the w = 0 branch: Lambda_wrong is not identically zero -------
    # L(2, chi_5) >= 49/100 > 0, fully exact:
    #   S_100 = sum_{n<=100} chi_5(n)/n^2 (exact Fractions), and
    #   |L(2,chi_5) - S_100| <= sum_{n>100} n^{-2} < 1/100
    # by the telescoping bound 1/n^2 < 1/(n(n-1)), sum_{n>N} 1/(n(n-1)) = 1/N.
    S100 = sum(Fraction(chi5(n), n * n) for n in range(1, 101))
    assert Fraction(1, 2) < S100 < Fraction(1, 1), S100
    L2_lower = S100 - Fraction(1, 100)
    assert L2_lower >= Fraction(49, 100), L2_lower
    # instance check of the telescoping comparison on a grid (exact):
    for n in range(2, 200):
        assert Fraction(1, n * n) < Fraction(1, n * (n - 1))
    # Lambda_wrong(2) = pi^{-3/2} Gamma(3/2) L(2,chi) = L(2,chi)/(2 pi):
    lam2_prefactor = PiMono(1, Fraction(-3, 2), 0) * GAMMA_3HALF
    assert lam2_prefactor == PiMono(Fraction(1, 2), Fraction(-1), 0)
    assert not lam2_prefactor.is_zero()

    # --- B6 (Remark 2/3 support): uniform bounds and divergence -----------
    # n^{-(2k+2)} <= 4^{-k} n^{-2} for n >= 2, k >= 1 (since n^{2k} >= 4^k);
    # instances checked exactly on a grid; general proof in the docstring.
    for n in range(2, 31):
        for k in range(1, 11):
            assert (Fraction(1, n ** (2 * k + 2))
                    <= Fraction(1, 4 ** k) * Fraction(1, n * n)), (n, k)
    # partial-sum instance for k = 1: sum_{n=2}^{100} n^{-4} < 1/4
    assert sum(Fraction(1, n ** 4) for n in range(2, 101)) < Fraction(1, 4)
    # divergence witness F_m = m!/4^{m+1}: ratio (m+1)/4 >= 2 for m >= 7
    F = {m: Fraction(math.factorial(m), 4 ** (m + 1)) for m in range(1, 41)}
    for m in range(7, 40):
        assert F[m + 1] / F[m] == Fraction(m + 1, 4) >= 2, m
    assert F[40] > 10 ** 20
    F20_str = str(F[20])

    # --- The complete obstruction proof, embedded as the witness ----------
    PROOF = (
        "THEOREM (proved here). Let chi_5 be the even quadratic Dirichlet "
        "character mod 5 (unit table (1,-1,-1,1), chi_5(-1) = +1, verified "
        "exactly) and Lambda_wrong(s) = pi^{-(s+1)/2} Gamma((s+1)/2) "
        "L(s, chi_5).  There is NO constant w (in particular none with "
        "|w| = 1) with Lambda_wrong(s) = w Lambda_wrong(1-s); no "
        "renormalization c N^{s/2} Lambda_wrong (c != 0, N > 0) admits such "
        "an FE either.  IMPORTED INGREDIENTS: (i) Gamma is meromorphic on "
        "C, NOWHERE ZERO, with simple poles exactly at 0, -1, -2, ... "
        "(Euler 1729; Weierstrass ~1856: 1/Gamma entire), plus Gamma(1)=1, "
        "Gamma(1/2)=pi^{1/2}, Gamma(z+1)=z Gamma(z); (ii) the true "
        "completed FE: Lambda_true(s) = (5/pi)^{s/2} Gamma(s/2) L(s,chi_5) "
        "is entire with Lambda_true(s) = Lambda_true(1-s) (classical "
        "Dirichlet-L functional equation, root number +1); (iii) the "
        "identity theorem for meromorphic functions.  PROOF.  Set G(s) = "
        "[pi^{-(s+1)/2} Gamma((s+1)/2)] / [pi^{-s/2} Gamma(s/2)].  By (i), "
        "G has zeros exactly at Z0 = {0,-2,-4,...} (poles of Gamma(s/2)) "
        "and poles exactly at P0 = {-1,-3,-5,...} (poles of "
        "Gamma((s+1)/2)); Z0 and P0 are disjoint by parity (exact integer "
        "check, k = 0..50), so all are simple with no cancellation.  Since "
        "Lambda_wrong(s) = G(s) 5^{-s/2} Lambda_true(s), the assumed FE "
        "plus (ii) forces G(s) 5^{-s/2} Lambda_true(s) = w G(1-s) "
        "5^{-(1-s)/2} Lambda_true(s).  Lambda_true is entire and not "
        "identically zero (Lambda_true(2) = 5 pi^{-1} L(2,chi_5) and "
        "L(2,chi_5) >= 49/100, PROVED EXACTLY: partial sum S_100 in "
        "(1/2, 1) in exact Fractions, tail < 1/100 by the telescoping "
        "bound 1/n^2 < 1/(n(n-1))), so its zero set is discrete; dividing "
        "it off and applying (iii) gives G(s) = w 5^{(2s-1)/2} G(1-s) as "
        "an identity of meromorphic functions on C.  Compare orders at "
        "s = 0.  LHS: ord = +1, a simple zero (Gamma(s/2) has a simple "
        "pole at 0; Gamma(1/2) finite nonzero).  RHS: 5^{(2s-1)/2} is "
        "entire nowhere zero, and G(1) = [Gamma(1) pi^{-1}] / [Gamma(1/2) "
        "pi^{-1/2}] = 1/pi, an EXACT monomial computation (coeff 1, "
        "pi-exponent -1) using Gamma(1) = 1 and Gamma(1/2) = pi^{1/2}: "
        "finite, NONZERO (1 lies in neither Z0 nor P0), so ord = 0 for "
        "any w != 0.  1 != 0: contradiction — the zero of G at s = 0 "
        "reflects to s = 1, where a zero would have to sit, but "
        "G(1) = 1/pi.  If w = 0, the FE forces Lambda_wrong == 0, "
        "contradicting Lambda_wrong(2) = L(2,chi_5)/(2 pi) >= "
        "49/(200 pi) > 0 (exact).  A factor c N^{s/2} is entire and "
        "nowhere zero and so changes no order: the same contradiction.  "
        "QED.  Moreover s -> 1-s maps ALL of Z0 to {1,3,5,...} and ALL of "
        "P0 to {2,4,6,...} — positive integers, where G is holomorphic and "
        "nonvanishing (checked exactly for the first 51 of each): every "
        "zero and every pole breaks the symmetry, not just s = 0.")

    DIRECT = (
        "Second, independent refutation (direct pole transport, proved "
        "here from the same imports): Lambda_wrong has a GENUINE simple "
        "pole at s = -1, because Gamma((s+1)/2) has a simple pole there "
        "and L(-1, chi_5) != 0 — the true FE gives Lambda_true(-1) = "
        "Lambda_true(2) = 5 pi^{-1} L(2, chi_5) != 0 (L(2, chi_5) >= "
        "49/100 exact) while the completion factors of Lambda_true are "
        "finite and nonzero at s = -1.  But Lambda_wrong is holomorphic "
        "at 1 - (-1) = 2, so Lambda_wrong(s) = w Lambda_wrong(1-s) fails "
        "near s = -1 for EVERY constant w: the left side blows up, the "
        "right side stays bounded.  In fact Lambda_wrong has genuine "
        "simple poles at every s = -(2k+1) (L(-(2k+1), chi_5) != 0 via "
        "Lambda_true(2k+2) and the uniform bound |L(2k+2, chi_5) - 1| < "
        "4^{-k}): the wrong completion is not even entire, while "
        "Lambda_true is.")

    l5_witness = (
        "THE ATTACHED GAMMA IS NOT CANONICAL, AND NO CHOICE OF ROOT NUMBER "
        "OR CONDUCTOR RESCUES IT.  Parity mismatch (exact): chi_5(-1) = "
        "chi_5(4) = +1, so the canonical archimedean datum is a = "
        "(1 - chi_5(-1))/2 = 0, i.e. Gamma_R(s) = pi^{-s/2} Gamma(s/2); "
        "attached instead is a = 1, i.e. Gamma_R(s+1).  " + PROOF)

    l6_witness = (
        "MEROMORPHIC CONTINUATION HOLDS, THE FUNCTIONAL EQUATION FAILS — "
        "and the failure is proved, not conjectured.  Lambda_wrong is "
        "meromorphic on all of C (entire L(s, chi_5) times a nowhere-zero "
        "meromorphic completion factor) with genuine simple poles at "
        "s = -1, -3, -5, ... (see the pole-transport refutation in the "
        "notes): unlike Lambda_true, the wrong completion is NOT ENTIRE.  "
        "NO functional equation Lambda_wrong(s) = w Lambda_wrong(1-s) "
        "exists for any constant w: see the L5 witness (proved here).  "
        "DISTINCTION, stated carefully: the underlying Dirichlet series "
        "L(s, chi_5) is untouched and RETAINS its true entire continuation "
        "and true FE Lambda_true(s) = Lambda_true(1-s) with the correct "
        "gamma factor Gamma_R(s) (imported; see world dirichlet_mod5).  "
        "What fails is a property of the wrong-completion OBJECT "
        "Lambda_wrong — of the archimedean dressing — not of L itself.")

    # =====================================================================
    # PART C — L7 finite twisting untouched (exact A6 tensor battery)
    # =====================================================================
    tensor_runs = []
    for p in TEST_PRIMES:
        satp = [Fraction(1), Fraction(-chi5(p))]
        prod_series = [Fraction(1)] * 8    # chi_0(p^k) = 1 for p != 5
        a6 = tensor_compatibility(satp, satp, prod_series)
        assert a6["status"] == HOLDS, (p, a6)
        tensor_runs.append({"prime": p, "statement":
                            "chi_5 (x) chi_5 = chi_0 locally at p",
                            "a6": a6})
    l7_witness = (
        "finite-part twist/tensor structure is untouched by the "
        "counterfeit: chi_5 (x) chi_5 = chi_0 certified by the exact A6 "
        "tensor axiom (tensor_compatibility) at p in "
        f"{{{', '.join(str(p) for p in TEST_PRIMES)}}}.  SCOPED: this "
        "lives entirely on the finite part; completed-level twisting "
        "bookkeeping (epsilon factors, conductors of twists) requires the "
        "canonical archimedean data and has no footing here (L5 FAILS)")

    l8_witness = (
        "Refutation of realization for the OBJECT Lambda_wrong (the "
        "underlying L(s, chi_5) of course retains its GL(1) realization — "
        "with the OTHER gamma).  (1) Lambda_wrong is not a Dirichlet "
        "series at all, hence lies in no Dirichlet-series-based class "
        "(Selberg class etc.): at s = 2m+1 the completion factor equals "
        "m! pi^{-(m+1)} exactly (Gamma(m+1) = m!), so with pi < 4 "
        "(imported: Archimedes) and L(2m+1, chi_5) > 1/2 (elementary "
        "uniform bound sum_{n>=2} n^{-3} < 1/2), Lambda_wrong(2m+1) > "
        "(1/2) m!/4^{m+1} -> infinity — the exact rationals F_m = "
        "m!/4^{m+1} satisfy F_{m+1}/F_m = (m+1)/4 >= 2 for m >= 7 "
        f"(checked exactly to m = 40; F_20 = {F20_str}, F_40 > 10^20) — "
        "while every Dirichlet series convergent in some half-plane tends "
        "to its finite first coefficient a_1 along the real axis.  "
        "(2) As a candidate completion of its own finite data: the "
        "archimedean component of the GL(1) Hecke character attached to "
        "chi_5 is forced by chi_5(-1) = +1 to Gamma_R(s), not "
        "Gamma_R(s+1) (imported: Hecke/Tate local-global structure), and "
        "any realization in a formalism whose completed L-functions "
        "satisfy an s <-> 1-s FE is refuted outright by the L5/L6 proof.  "
        "(3) Rigidity anchors (imported, not load-bearing): Hamburger "
        "(1921-22); CITATION-NEEDED: gamma-factor uniqueness in the "
        "Selberg class (Kaczorowski-Perelli context).  CAVEAT: a "
        "'realization' in some sense requiring neither a Dirichlet-series "
        "shape nor an FE is not formally excluded — see notes")

    l9_witness = (
        "no principled explicit formula attaches to the wrong completion: "
        "the Weil explicit formula is an identity DERIVED FROM the "
        "functional equation (contour shift plus the s <-> 1-s symmetry "
        "of the completed function), and Lambda_wrong provably admits no "
        "such FE for any constant w (L5/L6, proved here) — so the "
        "derivation has no footing for this object.  The true explicit "
        "formula for L(s, chi_5) exists (imported: Weil 1952) and its "
        "archimedean term is dictated by the TRUE gamma factor "
        "Gamma_R(s); the counterfeit's Gamma_R(s+1) would contribute a "
        "provably different archimedean term (digamma((s+1)/2) vs "
        "digamma(s/2) contributions differ by the reflection/shift "
        "bookkeeping of Part B: the pole sets differ at every negative "
        "integer).  FAILS is scoped to: no s <-> 1-s explicit-formula "
        "symmetry exists for THIS completion")

    # =====================================================================
    # Assemble the world record
    # =====================================================================
    gamma_citation = (
        "Gamma pole/zero structure: Euler (1729); Weierstrass (c. 1856), "
        "1/Gamma entire with zeros exactly at the nonpositive integers.  "
        "True Dirichlet-L FE (imported): CITATION-NEEDED: classical "
        "functional equation for Dirichlet L-functions (Hurwitz ~1882 "
        "era).  Rigidity anchors: Hamburger (1921-1922), zeta determined "
        "by its FE; CITATION-NEEDED: gamma-factor uniqueness in the "
        "Selberg class (Kaczorowski-Perelli context)")

    world = {
        "id": "counterfeit_wrong_gamma",
        "title": ("Counterfeit: wrong gamma factor on L(s, chi_5) "
                  "(archimedean-mismatch obstruction row)"),
        "definition": (
            "Lambda_wrong(s) = pi^{-(s+1)/2} Gamma((s+1)/2) L(s, chi_5), "
            "where chi_5 is the EVEN quadratic Dirichlet character mod 5 "
            "(Legendre symbol, unit table (1,-1,-1,1), chi_5(-1) = +1).  "
            "The attached archimedean factor Gamma_R(s+1) = pi^{-(s+1)/2} "
            "Gamma((s+1)/2) is the standard factor for ODD characters; the "
            "canonical completion of L(s, chi_5) uses Gamma_R(s) = "
            "pi^{-s/2} Gamma(s/2) (parity a = (1 - chi(-1))/2 = 0).  The "
            "finite part (coefficients, Euler product, degree-1 local "
            "factors 1 - chi_5(p) T) is untouched; only the archimedean "
            "dressing is counterfeited.  Engineered obstruction row: "
            "witnesses that archimedean data is NOT a free parameter "
            "(#764 axis H)."),
        "arithmetic_class": (
            "EXACT_RATIONAL + EXACT_SYMBOLIC_MONOMIALS (integers, "
            "Fractions; exact monomials c * pi^a * 5^b with c, a, b in Q "
            "for the Gamma-ratio evaluations, using the imported "
            "reductions Gamma(1) = 1, Gamma(1/2) = pi^{1/2}).  No "
            "floating point anywhere in the build."),
        "ladder": {
            "L0_WELL_DEFINED": cell(
                "HOLDS", "PROVED_HERE", witness=l0_witness,
                citation="Euler's criterion (Euler, ~1748-1761); Gamma "
                         "meromorphy: Euler (1729), Weierstrass (c. 1856)"),
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
                "FAILS", "PROVED_HERE", witness=l5_witness,
                citation=gamma_citation),
            "L6_CONTINUATION_FE": cell(
                "FAILS", "PROVED_HERE", witness=l6_witness,
                citation=gamma_citation),
            "L7_TWIST_TENSOR_COMPAT": cell(
                "HOLDS", "PROVED_HERE", witness=l7_witness,
                citation=""),
            "L8_REALIZATION": cell(
                "FAILS", "PROVED_HERE", witness=l8_witness,
                citation="Hecke (1918-1920); Tate's thesis (1950): "
                         "archimedean component of a GL(1) Hecke character "
                         "forced by parity; Hamburger (1921-1922); "
                         "CITATION-NEEDED: gamma-factor uniqueness in the "
                         "Selberg class (Kaczorowski-Perelli context); "
                         "Archimedes (c. 250 BC): pi < 22/7 < 4"),
            "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
                "FAILS", "PROVED_HERE", witness=l9_witness,
                citation="Explicit formula (for the TRUE completion, "
                         "imported): Weil (1952); Guinand (1948)"),
        },
        "mechanisms": {
            "EULER_PRODUCT": cell(
                "HOLDS", "PROVED_HERE", witness=(
                    "supplied by complete multiplicativity of chi_5 "
                    f"(verified exactly for all m, n <= {N}); degree <= 1 "
                    "local factors; entirely a finite-part mechanism, "
                    "untouched by the wrong gamma"),
                citation="Dirichlet (1837)"),
            "DUALITY_FE": cell(
                "FAILS", "PROVED_HERE", witness=(
                    "THE EXACT OBSTRUCTION OF THIS WORLD.  " + PROOF +
                    "  " + DIRECT),
                citation=gamma_citation),
            "TRACE_FORMULA": cell(
                "FAILS", "PROVED_HERE", witness=(
                    "any theta/Poisson-summation (GL(1) trace-formula) "
                    "mechanism attached to a completion produces exactly "
                    "the s <-> 1-s functional equation for it; for "
                    "Lambda_wrong that FE is refuted (see DUALITY_FE), so "
                    "no trace-formula mechanism can underlie this "
                    "completion.  The theta mechanism exists for the TRUE "
                    "completion only — the theta transformation for the "
                    "even theta series of chi_5 produces Gamma_R(s), i.e. "
                    "parity a = 0 (imported: classical theta / Tate 1950); "
                    "this is precisely the mechanism the counterfeit "
                    "violates"),
                citation="Tate's thesis (1950); classical theta "
                         "transformation"),
            "POSITIVITY_PURITY": cell(
                "NOT_APPLICABLE", "PROVED_HERE", witness=(
                    "finite-part weight-0 purity is exact and untouched "
                    "(|chi_5(p)| = 1, a^2 = 1 = p^0, detect A4 HOLDS at "
                    "every tested prime), but it forces nothing; the "
                    "positivity half (Weil-type explicit-formula "
                    "positivity) is FORMULATED THROUGH the functional "
                    "equation and completed object, which this world "
                    "provably lacks (L5/L6 proved) — the mechanism has no "
                    "formulation for the wrong completion.  See "
                    "critical_line: NOT_FORMULATED"),
                citation=""),
            "TENSOR_OPS": cell(
                "HOLDS", "PROVED_HERE", witness=(
                    "finite-part tensor structure untouched: chi_5 (x) "
                    "chi_5 = chi_0 certified by the exact A6 tensor axiom "
                    f"at {len(TEST_PRIMES)} primes; SCOPED to the finite "
                    "part — completed-level twisting bookkeeping requires "
                    "the canonical archimedean data (L5 FAILS)"),
                citation=""),
            "FAMILY": cell(
                "HOLDS", "SYNTHETIC_CONTROL", witness=(
                    "engineered member of the two-element parity family "
                    "Lambda_a(s) = pi^{-(s+a)/2} Gamma((s+a)/2) "
                    "L(s, chi_5), a in {0, 1}: a = 0 is the canonical "
                    "completion (true FE imported; sibling world "
                    "dirichlet_mod5), a = 1 is this counterfeit (FE "
                    "refuted exactly here).  The family contrast isolates "
                    "the archimedean parity bit as the unique failing "
                    "datum: every finite-place cell (L0-L3, L4, L7, "
                    "EULER_PRODUCT, TENSOR_OPS) is IDENTICAL between the "
                    "two members; only L5/L6/L8/L9 flip.  This is the "
                    "#764 axis-H control: archimedean data is not a free "
                    "parameter"),
                citation=""),
        },
        "critical_line": {
            "status": "NOT_FORMULATED",
            "detail": (
                "NOT_FORMULATED for the world object: a critical line is "
                "canonically attached through the functional equation "
                "s <-> 1-s (its fixed axis Re(s) = 1/2); Lambda_wrong "
                "provably admits NO such FE for any constant w (proved "
                "here, see L5/L6), so no critical line is canonically "
                "attached to the wrong completion.  The underlying "
                "L(s, chi_5) retains its usual critical line and GRH "
                "remains an unproved CONJECTURE for it (see world "
                "dirichlet_mod5).  Nothing here bears on RH/GRH."),
            "rigor": "PROVED_HERE",
            "citation": "",
            "witness": "the L5/L6 obstruction proof (this build)",
        },
        "sources": [
            "Euler (1729): the Gamma function; Weierstrass (c. 1856): "
            "1/Gamma entire with zeros exactly at the nonpositive "
            "integers (Gamma nowhere zero, simple poles at 0, -1, -2, "
            "...)",
            "Dirichlet (1837): Dirichlet characters and L-series",
            "CITATION-NEEDED: classical functional equation for Dirichlet "
            "L-functions (Hurwitz ~1882 era), imported exactly as in the "
            "sibling world dirichlet_mod5",
            "Hamburger (1921-1922): the Riemann zeta function is "
            "determined by its functional equation (rigidity/uniqueness)",
            "CITATION-NEEDED: gamma-factor uniqueness in the Selberg "
            "class (Kaczorowski-Perelli context)",
            "Hecke (1918-1920); Tate's thesis (1950): archimedean "
            "component of a GL(1) Hecke character forced by the parity of "
            "chi (local-global structure); theta mechanism for the FE",
            "Weil (1952): explicit formula (attaches to the TRUE "
            "completion only)",
            "Archimedes (c. 250 BC): 3 + 10/71 < pi < 3 + 1/7 (used only "
            "as pi < 4 in the divergence witness)",
        ],
        "rh_established": False,
        "notes": (
            "ROLE: the #764 axis-H obstruction row — archimedean data is "
            "NOT a free parameter.  The finite part of this world is "
            "bit-for-bit the true world dirichlet_mod5; ONLY the gamma "
            "factor was replaced by the odd-parity factor Gamma_R(s+1), "
            "and that single wrong bit provably destroys L5, L6, L8, L9, "
            "DUALITY_FE and TRACE_FORMULA while leaving L0-L4, L7, "
            "EULER_PRODUCT and TENSOR_OPS untouched.  " + DIRECT + "  "
            "SCOPE CAVEAT on L8: what is proved is (a) Lambda_wrong is "
            "not a Dirichlet series (exact divergence witness along s = "
            "2m+1), hence in no Dirichlet-series-based class, and (b) no "
            "FE-based completion assignment and no GL(1) completion of "
            "chi_5 yields it; a 'realization' in some sense requiring "
            "neither is not formally excluded.  Detector refusal "
            "semantics were never triggered: all runs completed with "
            "refusal = None.  RH/GRH is not established or addressed by "
            "anything in this record; rh_established = false."),
        "detector_runs": {
            "coefficient_battery": detector_runs,
            "tensor_battery": tensor_runs,
            "obstruction_bookkeeping": {
                "G_definition": ("G(s) = [pi^{-(s+1)/2} Gamma((s+1)/2)] / "
                                 "[pi^{-s/2} Gamma(s/2)]"),
                "zeros_of_G_first_six": zeros_first,
                "poles_of_G_first_six": poles_first,
                "reflection_of_zeros_first_six": refl_zeros_first,
                "reflection_of_poles_first_six": refl_poles_first,
                "reflection_checked_k_range": [0, K_REFLECT],
                "disjointness": "Z0 even <= 0, P0 odd <= -1: parity-disjoint "
                                "(exact integer checks)",
                "G_at_1": "pi^(-1): exact monomial (coeff 1, pi-exp -1, "
                          "5-exp 0), from Gamma(1) = 1, Gamma(1/2) = "
                          "pi^(1/2)",
                "rhs_unit_at_0": "5^(-1/2) G(1) = (coeff 1, pi-exp -1, "
                                 "5-exp -1/2): nonzero for every w != 0",
                "ord_at_0_lhs": ord_lhs_at_0,
                "ord_at_0_rhs_if_w_nonzero": ord_rhs_at_0,
                "parity_attached": parity_attached,
                "parity_canonical": parity_canonical,
                "S100_bracket": ["1/2", "1"],
                "L2_chi5_lower_bound": str(L2_lower) + " >= 49/100",
                "lambda_wrong_at_2": "L(2, chi_5)/(2 pi) >= 49/(200 pi) > 0",
                "divergence_F20_eq_20fact_over_4pow21": F20_str,
            },
        },
    }

    probs = validate_world(world)
    assert not probs, probs
    out_dir = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "worlds")
    path = save_world(world, out_dir)
    print(f"wrote {path}")
    print("counterfeit_wrong_gamma: all exact assertions passed; "
          "no-FE obstruction proof witnessed; rh_established=false")


if __name__ == "__main__":
    main()
