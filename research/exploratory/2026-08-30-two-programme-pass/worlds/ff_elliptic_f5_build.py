"""World 'ff_elliptic_f5': the zeta function of the elliptic curve

        E : y^2 = x^3 + x + 1   over F_5.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.ff_elliptic_f5_build

regenerates worlds/ff_elliptic_f5.json identically.

This is the MODEL WORLD for the POSITIVITY_PURITY mechanism: the one row of
the cross-world matrix where the mechanism that forces the critical line is
identified, finite, and exactly checkable.

What is computed here (Fraction / integer arithmetic ONLY, no floats):

  1. Nonsingularity of E: disc(x^3 + x + 1) = -4 - 27 = -31 == 4 mod 5 != 0.
  2. F_{5^k} for k = 1..6 built explicitly as F_5[x]/(f_k) with f_k the FIRST
     irreducible monic polynomial of degree k in a fixed exhaustive search
     order (irreducibility proved by trial division against every monic
     polynomial of degree <= k/2).  All arithmetic is integer arithmetic on
     coefficient tuples.
  3. #E(F_{5^k}) counted EXACTLY for k = 1..6 by exhaustive point counting
     (square tables in each constructed field), giving
         N = [9, 27, 108, 675, 3069, 15552].
  4. Independent cross-check: a_1 = 5 + 1 - N_1 = -3 determines
     P(T) = 1 - a_1 T + 5 T^2 = 1 + 3T + 5T^2; the power sums p_k of the
     Satake datum (via core.exact.power_sums_from_satake, i.e. the recursion
     a_k = alpha^k + beta^k) must PREDICT N_k = 5^k + 1 - p_k for k = 2..6,
     and the five predictions are confirmed against the raw exhaustive
     counts.  (The task requires k = 2,3; we cross-check k = 2..6.)
  5. Zeta = P(T) / ((1-T)(1-5T)).  Rationality window check: the coefficient
     series of P/((1-T)(1-5T)) equals exp(sum_k N_k T^k / k) through T^6
     (formal exp with Fractions), and equals the closed-point Euler product
     prod_{d<=6} (1 - T^d)^{-B_d} through T^6, with B_d the exactly computed
     number of closed points of degree d (Moebius inversion, integrality
     asserted).
  6. FUNCTIONAL EQUATION PROVED EXACTLY as a rational-function identity:
     (5T)^2 P(1/(5T)) == 5 * P(T) and (5T)^2 Q(1/(5T)) == 5 * Q(T) for
     Q = (1-T)(1-5T), hence Z(1/(5T)) == Z(T) exactly; also verified by
     cross-multiplication of the two scaled reciprocals.
  7. COMPLETE degree-2 purity certificate (the headline):
     alpha * beta = 5 exactly and disc = a^2 - 4*5 = -11 < 0, so alpha, beta
     are a complex-conjugate pair with |alpha|^2 = alpha*beta = 5 EXACTLY:
     |alpha| = |beta| = 5^{1/2}.  Corroborated by an exact Sturm count: the
     characteristic polynomial T^2 + 3T + 5 has ZERO real roots in (-100,100].
     Hence every zero T_0 of Z has |T_0| = 5^{-1/2}; under T = 5^{-s} this is
     Re(s) = 1/2: the critical line is a THEOREM for this world.
  8. The POSITIVITY mechanism made exact (Hasse's proof scheme): the degree
     form deg(m + n phi) = m^2 + a m n + 5 n^2 (a = -3) is positive definite;
     exact certificates: disc = -11 < 0, sum-of-squares identity
     4(m^2 - 3mn + 5n^2) = (2m - 3n)^2 + 11 n^2 (verified as a polynomial
     identity in m, n), and a brute-force positive window.  Positivity of the
     degree map is the Castelnuovo-positivity input that FORCES a^2 < 4q and
     hence purity.  This is the slot that is OPEN for the Riemann zeta world.
  9. Tensor/twist operations, all exact: quadratic twist E^(2): y^2 = x^3 +
     4x + 3 counted independently (N' = 3, a' = +3 = -a); Sym^2 and Ext^2 of
     the Satake datum with COMPLETE purity certificates of weight 2 (Ext^2 =
     det = weight-2 Tate: power sums exactly 5^k); Adams/base-change to F_25
     and F_125 matching the direct counts; Poincare duality as the exact
     identity (dual Satake twisted by q) == P.
 10. Family sweep: ALL 20 nonsingular short-Weierstrass curves y^2 = x^3 +
     Ax + B over F_5 are counted exhaustively; every member satisfies the
     strict Hasse inequality a^2 <= 16 < 20 = 4q (complete purity for the
     whole family), and the quadratic-twist involution (A,B) -> (4A, 3B)
     negates a across the family, exactly.
 11. Detector runs (core.reconstruct.detect) on coefficient data of 1/P with
     weight (5,1): COMPLETE exact degree-2 purity test; all five axioms HOLD.
     Also runs for the twist and the F_25/F_125 base changes.  A traces-mode
     run is included and refuses at A1: annotated honestly as a properness
     limitation of the reconstruction interface (numerator degree equals
     denominator degree for trace generating functions), not a structural
     failure of the world.

RH over Q is NOT addressed by any of this; rh_established = false.
"""

import itertools
from fractions import Fraction
from math import comb

from core.exact import (
    F,
    coefficient_sequence_from_satake,
    power_sums_from_satake,
    satake_poly_from_power_sums,
    series_of_rational,
    poly_mul,
    poly_divmod,
    poly_eval,
    poly_scale,
    op_sym2,
    op_ext2,
    op_tensor,
    op_adams,
    op_dual_satake,
    count_real_roots_in,
    charpoly_of_matrix,
)
from core.reconstruct import detect, tensor_compatibility
from core.worlds import cell, validate_world, save_world

# ---------------------------------------------------------------------------
# Fixed data of the world (all literals; no randomness anywhere)
# ---------------------------------------------------------------------------
MOD = 5                      # the prime q
CURVE_A, CURVE_B = 1, 1      # E: y^2 = x^3 + x + 1
TWIST_D = 2                  # a fixed non-square mod 5 (squares are {0,1,4})
KMAX = 6                     # count points over F_{5^k}, k = 1..KMAX
WINDOW = 12                  # detector window
HOLDOUT = 4                  # detector holdout
INV5 = [0, 1, 3, 2, 4]       # multiplicative inverses mod 5 (index 0 unused)


# ---------------------------------------------------------------------------
# Section 1: explicit finite fields F_{5^k} = F_5[x]/(f_k), integer arithmetic
# ---------------------------------------------------------------------------

def pdivmod5(a, b):
    """Division with remainder for int-coefficient polynomials mod 5,
    low-first lists.  b must be nonzero mod 5."""
    a = [c % MOD for c in a]
    b = [c % MOD for c in b]
    while a and a[-1] == 0:
        a.pop()
    while b and b[-1] == 0:
        b.pop()
    assert b, "division by zero polynomial"
    q = [0] * max(0, len(a) - len(b) + 1)
    r = a[:]
    while r and len(r) >= len(b):
        c = (r[-1] * INV5[b[-1]]) % MOD
        d = len(r) - len(b)
        q[d] = c
        for i, bc in enumerate(b):
            r[d + i] = (r[d + i] - c * bc) % MOD
        while r and r[-1] == 0:
            r.pop()
    return q, r


def find_irreducible(k):
    """First monic irreducible polynomial of degree k over F_5 in the fixed
    exhaustive order tail = (c_0, ..., c_{k-1}) of itertools.product.
    Irreducibility is PROVED by trial division: a reducible polynomial of
    degree k has a monic factor of degree <= k // 2, and every monic
    polynomial of those degrees is tried.  Deterministic."""
    if k == 1:
        return [0, 1]                       # f_1 = x; F_5[x]/(x) = F_5
    for tail in itertools.product(range(MOD), repeat=k):
        f = list(tail) + [1]
        reducible = False
        for d in range(1, k // 2 + 1):
            for gt in itertools.product(range(MOD), repeat=d):
                g = list(gt) + [1]
                _, r = pdivmod5(f, g)
                if not r:
                    reducible = True
                    break
            if reducible:
                break
        if not reducible:
            return f
    raise RuntimeError("no irreducible polynomial found (impossible)")


class GF:
    """F_{5^k} as coefficient tuples (c_0, ..., c_{k-1}) modulo f_k.
    Multiplication = integer convolution + reduction by a precomputed table
    of x^j mod f_k for j = k .. 2k-2.  Pure integer arithmetic."""

    def __init__(self, k):
        self.k = k
        self.f = find_irreducible(k)
        base = [(-c) % MOD for c in self.f[:k]]      # x^k == base (mod f)
        red = {k: base}
        for j in range(k + 1, 2 * k - 1):
            shifted = [0] + red[j - 1][:]
            carry = shifted[k] if len(shifted) > k else 0
            shifted = shifted[:k]
            if carry:
                shifted = [(shifted[i] + carry * base[i]) % MOD
                           for i in range(k)]
            red[j] = shifted
        self.red = red

    def mul(self, a, b):
        k = self.k
        prod = [0] * (2 * k - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    if bj:
                        prod[i + j] += ai * bj
        out = [c % MOD for c in prod[:k]]
        for j in range(k, 2 * k - 1):
            c = prod[j] % MOD
            if c:
                rj = self.red[j]
                for i in range(k):
                    out[i] = (out[i] + c * rj[i]) % MOD
        return tuple(out)


# ---------------------------------------------------------------------------
# Section 2: exact exhaustive point counting
# ---------------------------------------------------------------------------

def count_points(k, A, B):
    """#{(x,y) in F_{5^k}^2 : y^2 = x^3 + A x + B} + 1 (the single point at
    infinity of a smooth Weierstrass cubic), by exhaustive enumeration.
    Builds the full table of squares of F_{5^k} and checks membership.
    Returns (N, f_k).  Sanity assertion: F_q (q odd) has exactly (q-1)/2
    nonzero squares -- a nontrivial consistency check of the field build."""
    Fq = GF(k)
    elems = list(itertools.product(range(MOD), repeat=k))
    squares = set(Fq.mul(t, t) for t in elems)
    assert len(squares) == (MOD ** k - 1) // 2 + 1, "square count wrong"
    zero = (0,) * k
    n = 1                                   # point at infinity
    for x in elems:
        x3 = Fq.mul(Fq.mul(x, x), x)
        rhs = tuple((x3[i] + A * x[i] + (B if i == 0 else 0)) % MOD
                    for i in range(k))
        if rhs == zero:
            n += 1                          # y = 0, one point
        elif rhs in squares:
            n += 2                          # y = +-sqrt(rhs), two points
    return n, Fq.f


# ---------------------------------------------------------------------------
# Section 3: witness builders (every claim asserted before embedding)
# ---------------------------------------------------------------------------

def fmt(p):
    return "[" + ", ".join(str(F(c)) for c in p) + "]"


def scaled_reciprocal(p, c):
    """(cT)^d * p(1/(cT)) for p of degree d: coefficient i is p_{d-i} c^i."""
    p = [F(x) for x in p]
    d = len(p) - 1
    return [p[d - i] * F(c) ** i for i in range(d + 1)]


def build_counts_and_satake():
    """Nonsingularity, exact counts N_1..N_6, the Satake polynomial P, and
    the recursion-versus-raw-counting cross-check."""
    W = {}

    # (a) nonsingularity: disc(x^3 + ax + b) = -4a^3 - 27b^2 != 0 mod 5
    disc = (-4 * CURVE_A ** 3 - 27 * CURVE_B ** 2) % MOD
    assert disc == 4 and disc != 0
    W["nonsingular"] = ("disc(x^3 + x + 1) = -4*1 - 27*1 = -31 == 4 (mod 5), "
                       "nonzero, so E: y^2 = x^3 + x + 1 is a nonsingular "
                       "(elliptic) curve over F_5 (char 5 != 2,3, short "
                       "Weierstrass discriminant criterion)")

    # (b) exact exhaustive counts over explicitly constructed F_{5^k}
    N = []
    fields = []
    for k in range(1, KMAX + 1):
        n, f = count_points(k, CURVE_A, CURVE_B)
        N.append(n)
        fields.append(f)
    assert N == [9, 27, 108, 675, 3069, 15552], N
    W["counts"] = ("exhaustive point counts over F_{5^k} = F_5[x]/(f_k), "
                   "k=1..6: N = [9, 27, 108, 675, 3069, 15552]; moduli f_k "
                   "(low-first int lists, monic, irreducibility proved by "
                   "trial division vs all monic polys of degree <= k/2): "
                   + "; ".join(f"f_{k+1}={fields[k]}"
                               for k in range(KMAX)))

    # (c) Satake polynomial from a_1 alone
    a1 = MOD + 1 - N[0]
    assert a1 == -3
    P = [F(1), F(-a1), F(MOD)]              # 1 - a_1 T + 5 T^2 = 1 + 3T + 5T^2
    assert P == [F(1), F(3), F(5)]

    # (d) cross-check: recursion a_k = alpha^k + beta^k (power sums of the
    # Satake datum) must predict the RAW counts for k = 2..6.  The k=1 count
    # DEFINES a_1; the five further agreements are genuine predictions of
    # Hasse's structure theorem confirmed by independent exhaustive counting.
    p = power_sums_from_satake(P, WINDOW)
    assert p[:KMAX] == [F(-3), F(-1), F(18), F(-49), F(57), F(74)]
    for k in range(1, KMAX + 1):
        assert F(MOD) ** k + 1 - p[k - 1] == N[k - 1], (k, p[k - 1], N[k - 1])
    W["recursion_vs_raw"] = (
        "a_1 = 5+1-9 = -3 fixes P(T) = 1 + 3T + 5T^2; power sums p_k of P "
        "(exact, core.exact.power_sums_from_satake == the recursion "
        "a_k = -3 a_{k-1} - 5 a_{k-2}) give p = [-3, -1, 18, -49, 57, 74] "
        "and the predictions N_k = 5^k + 1 - p_k = [9, 27, 108, 675, 3069, "
        "15552] agree with the independent exhaustive counts for ALL k = "
        "1..6 (k = 2..6 are genuine confirmations, five for five)")

    # (e) trivia identities pinned exactly
    assert poly_eval(P, 1) == F(N[0]) == 9
    W["class_number"] = ("P(1) = 1 + 3 + 5 = 9 = N_1 = #E(F_5): the divisor "
                         "class number h of the function field equals the "
                         "group order of E(F_5), verified exactly")
    return W, N, P, p, fields


def build_fe_witnesses(P):
    """The functional equation of Z(T) = P(T)/((1-T)(1-5T)), proved exactly
    as a rational-function identity with Fractions."""
    W = {}
    Qd = poly_mul([F(1), F(-1)], [F(1), F(-5)])          # (1-T)(1-5T)
    assert Qd == [F(1), F(-6), F(5)]

    # numerator: (5T)^2 P(1/(5T)) == 5 P(T)
    numflip = scaled_reciprocal(P, MOD)
    assert numflip == poly_scale(P, MOD) == [F(5), F(15), F(25)]
    # denominator: (5T)^2 Q(1/(5T)) == 5 Q(T)
    denflip = scaled_reciprocal(Qd, MOD)
    assert denflip == poly_scale(Qd, MOD) == [F(5), F(-30), F(25)]
    # cross-multiplied identity (equivalent to Z(1/(5T)) == Z(T)):
    assert poly_mul(numflip, Qd) == poly_mul(P, denflip)
    W["fe"] = ("functional equation PROVED as an exact rational-function "
               "identity: (5T)^2 P(1/(5T)) = [5, 15, 25] = 5*P(T) and "
               "(5T)^2 Q(1/(5T)) = [5, -30, 25] = 5*Q(T) for Q = (1-T)(1-5T)"
               " = [1, -6, 5]; hence Z(1/(5T)) = (5P)/(5Q) = Z(T) exactly; "
               "cross-multiplication [(5T)^2 P(1/(5T))]*Q == P*[(5T)^2 "
               "Q(1/(5T))] asserted coefficientwise in Fractions. Root "
               "number +1; genus 1 so the FE has no T-power prefactor")

    # gcd sanity: P shares no root with the denominator
    assert poly_eval(P, 1) != 0 and poly_eval(P, Fraction(1, 5)) != 0
    W["coprime"] = ("P(1) = 9 != 0 and P(1/5) = 9/5 != 0: numerator and "
                    "denominator of Z are exactly coprime; Z has simple "
                    "poles at T = 1, 1/5 and no others")
    return W, Qd


def build_euler_product_witnesses(N, P, Qd):
    """Closed points, Euler product, exp-identity, effectivity: all exact,
    all through the T^6 window fixed by KMAX = 6."""
    W = {}
    mu = {1: 1, 2: -1, 3: -1, 4: 0, 5: -1, 6: 1}

    # (a) closed points of degree d by Moebius inversion (integrality forced)
    B = {}
    for d in range(1, KMAX + 1):
        s = sum(mu[d // e] * N[e - 1] for e in range(1, d + 1) if d % e == 0)
        assert s % d == 0, (d, s)
        B[d] = s // d
    assert B == {1: 9, 2: 9, 3: 33, 4: 162, 5: 612, 6: 2571}, B
    # inversion consistency: N_k = sum_{d | k} d * B_d
    for k in range(1, KMAX + 1):
        assert N[k - 1] == sum(d * B[d] for d in range(1, k + 1) if k % d == 0)
    W["closed_points"] = (
        "closed points of degree d (places of the function field): B = "
        "{1: 9, 2: 9, 3: 33, 4: 162, 5: 612, 6: 2571} by exact Moebius "
        "inversion of the counts (integrality asserted); inversion "
        "N_k = sum_{d|k} d B_d re-verified for k = 1..6")

    # (b) zeta series three ways, compared through T^6:
    zser = series_of_rational(P, Qd, KMAX + 1)          # from closed form

    #     (b1) exp(sum N_k T^k / k), formal exponential over Q
    S = [Fraction(0)] + [Fraction(N[k - 1], k) for k in range(1, KMAX + 1)]
    E = [Fraction(1)]
    for n in range(1, KMAX + 1):
        E.append(sum(F(j) * S[j] * E[n - j] for j in range(1, n + 1)) / n)
    assert E == zser, (E, zser)
    W["exp_identity"] = (
        "exp(sum_{k=1..6} N_k T^k / k) == P/((1-T)(1-5T)) through T^6, "
        "formal exp computed with Fractions; series = " + fmt(zser))

    #     (b2) Euler product over closed points, prod (1 - T^d)^{-B_d}
    prod = [Fraction(1)] + [Fraction(0)] * KMAX
    for d in range(1, KMAX + 1):
        factor = [Fraction(0)] * (KMAX + 1)
        j = 0
        while d * j <= KMAX:
            factor[d * j] = Fraction(comb(B[d] - 1 + j, j))
            j += 1
        prod = poly_mul(prod, factor)[: KMAX + 1]
        prod += [Fraction(0)] * (KMAX + 1 - len(prod))
    assert prod == zser, (prod, zser)
    W["euler_product"] = (
        "closed-point Euler product prod_{d<=6} (1 - T^d)^{-B_d} == "
        "P/((1-T)(1-5T)) through T^6, exact (binomial series, Fractions); "
        "the identity holds because effective divisors form the FREE "
        "commutative monoid on closed points (complete combinatorial proof "
        "of the Euler product shape), while the equality with P/Q is "
        "window-checked here and holds for all degrees by Hasse (imported)")

    # (c) effectivity: divisor counts b_n are nonnegative integers with the
    #     exact closed form b_n = h (q^n - 1)/(q - 1) = 9(5^n - 1)/4, n >= 1
    zlong = series_of_rational(P, Qd, 13)
    for n, b in enumerate(zlong):
        assert b.denominator == 1 and b >= 0
        if n >= 1:
            assert b == Fraction(9 * (5 ** n - 1), 4), (n, b)
    W["effectivity"] = (
        "coefficients b_n of Z (numbers of effective divisors of degree n) "
        "are nonnegative integers with exact closed form b_n = 9(5^n - 1)/4 "
        "for 1 <= n <= 12 (b_0 = 1): b = " + fmt(zlong[:7]) + " ...; "
        "h = 9 is the class number")
    return W, B


def build_purity_witnesses(P):
    """The COMPLETE degree-2 purity certificate and the positivity mechanism
    (Hasse degree form) with exact certificates.  This is the headline."""
    W = {}
    a = -P[1]                                # trace alpha + beta = -3
    prodroots = P[2]                         # alpha * beta = 5
    disc = a * a - 4 * prodroots             # 9 - 20 = -11
    assert a == -3 and prodroots == 5 and disc == -11 and disc < 0
    W["purity"] = (
        "COMPLETE exact degree-2 purity certificate: alpha+beta = -3, "
        "alpha*beta = 5 (both exact integers from P = [1, 3, 5]), disc = "
        "(-3)^2 - 4*5 = -11 < 0, so alpha, beta are a complex-conjugate "
        "pair and |alpha|^2 = alpha*conj(alpha) = alpha*beta = 5 EXACTLY: "
        "|alpha| = |beta| = 5^(1/2).  Every zero T_0 of Z(T) is an inverse "
        "root of P, so |T_0| = 5^(-1/2); writing T = 5^(-s), |5^(-s)| = "
        "5^(-Re s) = 5^(-1/2) iff Re(s) = 1/2: ALL zeros lie on the "
        "critical line, as an exact finite computation")

    # Sturm corroboration (still exact): char poly T^2 + 3T + 5 has no real
    # roots at all, so the pair is genuinely complex.
    charpoly = [F(5), F(3), F(1)]            # low-first T^2 + 3T + 5
    nroots = count_real_roots_in(charpoly, -100, 100)
    assert nroots == 0
    W["sturm"] = ("exact Sturm count: T^2 + 3T + 5 has 0 real roots in "
                  "(-100, 100] (and |roots| <= 1 + 5 < 100 by the Cauchy "
                  "bound, so 0 real roots anywhere): independent exact "
                  "confirmation that disc < 0 route is sound")

    # companion-matrix realization of Frobenius on H^1 and its relation
    M = [[0, -5], [1, -3]]
    cp = charpoly_of_matrix(M)
    assert cp == charpoly
    MM = [[sum(M[i][t] * M[t][j] for t in range(2)) for j in range(2)]
          for i in range(2)]
    rel = [[MM[i][j] + 3 * M[i][j] + (5 if i == j else 0) for j in range(2)]
           for i in range(2)]
    assert rel == [[0, 0], [0, 0]]
    W["companion"] = ("Frobenius eigenvalue package realized by the exact "
                      "integer companion matrix M = [[0, -5], [1, -3]]: "
                      "charpoly_of_matrix(M) = T^2 + 3T + 5 "
                      "(Faddeev-LeVerrier, exact) and M^2 + 3M + 5I = 0")

    # THE MECHANISM: positivity of the degree form (Hasse's proof scheme).
    # deg(m + n*phi) = m^2 + a m n + q n^2 with a = -3, q = 5.  Exact
    # positive-definiteness certificates:
    #   (i) leading coefficient 1 > 0 and disc = a^2 - 4q = -11 < 0;
    #  (ii) sum-of-squares identity 4 Q(m,n) = (2m + a n)^2 + (4q - a^2) n^2,
    #       verified as a polynomial identity in (m, n) over Z;
    # (iii) brute positive window (executable corroboration, exact ints).
    q4 = 4 * 5 - (-3) ** 2
    assert q4 == 11 and q4 > 0
    # (ii) expand both sides as {(i,j): coeff} dictionaries over Z
    lhs = {(2, 0): 4 * 1, (1, 1): 4 * (-3), (0, 2): 4 * 5}
    rhs = {}
    for (i1, j1, c1) in [(1, 0, 2), (0, 1, -3)]:          # 2m - 3n
        for (i2, j2, c2) in [(1, 0, 2), (0, 1, -3)]:
            key = (i1 + i2, j1 + j2)
            rhs[key] = rhs.get(key, 0) + c1 * c2
    rhs[(0, 2)] = rhs.get((0, 2), 0) + 11                 # + 11 n^2
    assert lhs == {k: v for k, v in rhs.items() if v}, (lhs, rhs)
    # (iii)
    for m in range(-25, 26):
        for n in range(-25, 26):
            if (m, n) != (0, 0):
                assert m * m - 3 * m * n + 5 * n * n > 0
    W["positivity"] = (
        "POSITIVITY MECHANISM (Hasse degree form): deg(m + n phi) = "
        "m^2 - 3mn + 5n^2 on Z + Z phi in End(E) is positive definite; "
        "exact certificates: disc = -11 < 0 with leading coefficient 1, "
        "sum-of-squares identity 4(m^2 - 3mn + 5n^2) = (2m - 3n)^2 + 11 n^2 "
        "verified as a polynomial identity over Z, and Q(m,n) > 0 checked "
        "for all 0 < max(|m|,|n|) <= 25.  Positivity of the degree map "
        "(deg >= 0, = 0 only at 0: Castelnuovo-type positivity, geometric "
        "input) forces a^2 < 4q = 20 (indeed a^2 = 9), which IS the purity "
        "|alpha| = 5^(1/2).  The mechanism is identified, finite, and "
        "exactly checkable -- the model for the POSITIVITY_PURITY slot")
    return W


def build_tensor_witnesses(P, p, N):
    """Twist, Sym^2/Ext^2, Adams/base change, duality: all exact."""
    W = {}
    checks = []

    # (a) quadratic twist E^(2): y^2 = x^3 + d^2 A x + d^3 B = x^3 + 4x + 3
    tA = (TWIST_D ** 2 * CURVE_A) % MOD
    tB = (TWIST_D ** 3 * CURVE_B) % MOD
    assert (tA, tB) == (4, 3)
    tdisc = (-4 * tA ** 3 - 27 * tB ** 2) % MOD
    assert tdisc == 1 and tdisc != 0
    Ntw1, _ = count_points(1, tA, tB)
    Ntw2, _ = count_points(2, tA, tB)
    atw = MOD + 1 - Ntw1
    assert (Ntw1, Ntw2, atw) == (3, 27, 3) and atw == -(-3)
    Ptw = [F(1), F(-atw), F(MOD)]
    assert Ptw == [F(1), F(-3), F(5)]
    ptw = power_sums_from_satake(Ptw, WINDOW)
    assert F(25) + 1 - ptw[1] == Ntw2       # F_25 count matches recursion too
    # twist purity, complete deg-2 test
    assert Ptw[2] == 5 and (-Ptw[1]) ** 2 - 4 * Ptw[2] == -11 < 0
    W["twist"] = (
        "quadratic twist by the non-square d = 2: E^(2): y^2 = x^3 + 4x + 3 "
        "(disc == 1 mod 5, nonsingular), counted independently and "
        "exhaustively: N'_1 = 3, N'_2 = 27, so a' = 3 = -a exactly (twist "
        "negates the trace, chi(2) = -1); P'(T) = 1 - 3T + 5T^2 passes the "
        "same complete purity test (product 5, disc = -11 < 0); over F_25 "
        "the twist trivializes: both curves have 27 points, exactly")

    # (b) Ext^2 = determinant = weight-2 Tate object: power sums exactly 5^k
    ext2 = op_ext2(p, KMAX)
    assert ext2 == [F(5) ** k for k in range(1, KMAX + 1)]
    sat_ext2 = satake_poly_from_power_sums(ext2[:1], 1)
    assert sat_ext2 == [F(1), F(-5)]
    W["ext2"] = ("Ext^2(H^1) power sums are exactly [5, 25, 125, 625, 3125, "
                 "15625] = 5^k: Ext^2 = det = the weight-2 Tate object, "
                 "Satake [1, -5] -- Poincare duality pairing made exact")

    # (c) Sym^2: satake (1-5T)(1 + T + 25T^2), complete purity of weight 2
    sym2 = op_sym2(p, KMAX)
    assert [sym2[i] + ext2[i] for i in range(KMAX)] == op_tensor(p, p, KMAX)
    sat_sym2 = satake_poly_from_power_sums(sym2[:3], 3)
    assert sat_sym2 == poly_mul([F(1), F(-5)], [F(1), F(1), F(25)])
    assert sat_sym2 == [F(1), F(-4), F(20), F(-125)]
    quo, rem = poly_divmod(sat_sym2, [F(1), F(-5)])
    assert rem == [] and quo == [F(1), F(1), F(25)]
    # complete purity, weight 2 (q^w = 25): real root 5 with 5^2 == 25;
    # quadratic factor: product 25 == q^w, disc = 1 - 100 = -99 < 0.
    assert F(5) ** 2 == 25
    assert quo[2] == 25 and quo[1] ** 2 - 4 * quo[2] == -99 < 0
    W["sym2"] = (
        "Sym^2(H^1): power sums (p_k^2 + p_{2k})/2 exact; Satake factor "
        "(1 - 5T)(1 + T + 25T^2) = [1, -4, 20, -125] (asserted, and exact "
        "division by (1 - 5T) leaves [1, 1, 25] with remainder 0); COMPLETE "
        "purity of weight 2: real inverse root 5 has 5^2 = 25 = q^2, and "
        "the quadratic factor has product 25 = q^2 with disc = -99 < 0, so "
        "|alpha^2| = |beta^2| = 5 exactly; Sym^2 + Ext^2 == tensor square "
        "on power sums, asserted for k = 1..6")

    # (d) Adams operations = base change: satake over F_25 and F_125 from
    #     op_adams must reproduce the INDEPENDENT raw counts
    p2 = op_adams(p, 2, 2)
    sat25 = satake_poly_from_power_sums(p2, 2)
    assert sat25 == [F(1), F(1), F(25)]
    assert F(25) + 1 - p2[0] == N[1] == 27
    assert (-sat25[1]) ** 2 - 4 * sat25[2] == -99 < 0 and sat25[2] == 25
    p3 = op_adams(p, 3, 2)
    sat125 = satake_poly_from_power_sums(p3, 2)
    assert sat125 == [F(1), F(-18), F(125)]
    assert F(125) + 1 - p3[0] == N[2] == 108
    assert (-sat125[1]) ** 2 - 4 * sat125[2] == -176 < 0 and sat125[2] == 125
    W["adams"] = (
        "base change = Adams operations, exactly: psi^2 gives Satake "
        "[1, 1, 25] over F_25 (N_2 = 25 + 1 - (-1) = 27 matches the raw "
        "exhaustive count) and psi^3 gives [1, -18, 125] over F_125 "
        "(N_3 = 125 + 1 - 18 = 108 matches); complete purity persists: "
        "products 25, 125 = q^k with discs -99 < 0, -176 < 0: RH for "
        "E/F_25 and E/F_125 also PROVED by finite exact computation")

    # (e) Poincare duality as an exact Satake identity: dual twisted by q
    dual = op_dual_satake(P, F(5))
    assert dual == [F(1), Fraction(3, 5), Fraction(1, 5)]
    assert [dual[j] * F(5) ** j for j in range(3)] == P
    W["duality"] = ("op_dual_satake(P, det=5) = [1, 3/5, 1/5] and twisting "
                    "T -> 5T returns exactly P: the involution alpha -> "
                    "5/alpha fixes the inverse-root multiset {alpha, beta} "
                    "(Poincare duality / Weil pairing on H^1), exact")

    # (f) A6 machinery runs (tensor_compatibility); both are labelled as
    #     internal-consistency exercises of the exact tensor calculus.
    unit = [F(1), F(-1)]                     # unit object, eigenvalue 1
    t1 = tensor_compatibility(P, unit, coefficient_sequence_from_satake(P, 10))
    assert t1["status"] == "HOLDS", t1
    checks.append({"name": "tensor_with_unit",
                   "detail": "H^1(E) (x) unit == H^1(E): A6 exact",
                   "result": t1})
    pa = power_sums_from_satake(P, 20)
    pb = power_sums_from_satake([F(1), F(-3), F(5)], 20)
    pt = op_tensor(pa, pb, 4)
    satT = satake_poly_from_power_sums(pt, 4)
    t2 = tensor_compatibility(P, [F(1), F(-3), F(5)],
                              coefficient_sequence_from_satake(satT, 12))
    assert t2["status"] == "HOLDS", t2
    checks.append({"name": "tensor_E_with_twist",
                   "detail": ("H^1(E) (x) H^1(E^(2)) degree-4 Satake "
                              "predicted by op_tensor; A6 consistency of "
                              "the exact tensor calculus (product series "
                              "constructed from the same calculus, so this "
                              "checks machinery coherence, not an "
                              "independent count)"),
                   "result": t2})
    return W, checks


def build_family_sweep():
    """ALL short-Weierstrass elliptic curves over F_5, counted exhaustively:
    strict Hasse bound and twist involution across the whole family."""
    members = []
    table = {}
    for A in range(MOD):
        for Bc in range(MOD):
            disc = (-4 * A ** 3 - 27 * Bc ** 2) % MOD
            if disc == 0:
                continue
            n, _ = count_points(1, A, Bc)
            a = MOD + 1 - n
            assert a * a <= 16 < 20, (A, Bc, a)   # strict Hasse: a^2 < 4q
            # complete purity for the member (given Hasse structure
            # P_AB = 1 - aT + 5T^2): product 5, disc a^2 - 20 < 0
            assert a * a - 20 < 0
            table[(A, Bc)] = a
            members.append((A, Bc, n, a))
    assert len(members) == 20
    # twist involution across the family: (A, B) -> (4A, 3B) negates a
    for (A, Bc), a in table.items():
        assert table[(4 * A % MOD, 3 * Bc % MOD)] == -a, (A, Bc)
    assert table[(1, 1)] == -3
    W = ("horizontal family sweep: all 20 nonsingular y^2 = x^3 + Ax + B "
         "over F_5 counted exhaustively; every member has a^2 <= 16 < 20 = "
         "4q (strict Hasse inequality, hence disc(P_AB) = a^2 - 20 < 0 and "
         "the COMPLETE degree-2 purity test passes for the ENTIRE family); "
         "the quadratic-twist involution (A,B) -> (4A, 3B) exactly negates "
         "a across all 20 members; members (A,B,N,a): "
         + str(members))
    return W, members


# ---------------------------------------------------------------------------
# Section 4: detector runs
# ---------------------------------------------------------------------------

def run_detector(P):
    """core.reconstruct.detect on exact coefficient data with weight (5,1):
    the COMPLETE degree-2 purity test.  Plus twist and base-change runs, and
    one honestly-annotated traces-mode refusal."""
    runs = []

    def expect_all_holds(sat, q, tag, note):
        ser = coefficient_sequence_from_satake(sat, WINDOW)
        v = detect(ser, mode="coefficients", weight=(q, 1), holdout=HOLDOUT)
        d = v.as_dict()
        assert d["refusal"] is None, (tag, d)
        got = {c["axiom"]: c["status"] for c in d["cells"]}
        assert got == {"A1_FINITE_RANK": "HOLDS", "A2_EFFECTIVITY": "HOLDS",
                       "A3_INTEGRALITY": "HOLDS", "A4_PURITY": "HOLDS",
                       "A5_HELD_OUT": "HOLDS"}, (tag, got)
        # the purity cell must be the COMPLETE deg-2 branch, exact rigor
        a4 = next(c for c in d["cells"] if c["axiom"] == "A4_PURITY")
        assert a4["rigor"] == "EXACT_RATIONAL" and "complete test" in a4["witness"]
        assert d["object"]["degree"] == 2
        assert d["object"]["numerator"] == "[1]"
        runs.append({"name": tag, "weight": [q, 1], "mode": "coefficients",
                     "series": note, "verdict": d})
        return d

    d1 = expect_all_holds(P, 5, "E_over_F5_weight_(5,1)",
                          "a_{5^k}-side coefficient data of 1/P, P = "
                          "[1, 3, 5], window 12, holdout 4")
    assert d1["object"]["denominator"] == "[1, 3, 5]"
    d2 = expect_all_holds([F(1), F(-3), F(5)], 5, "twist_E2_weight_(5,1)",
                          "coefficient data of 1/P', P' = [1, -3, 5] "
                          "(quadratic twist), window 12, holdout 4")
    assert d2["object"]["denominator"] == "[1, -3, 5]"
    d3 = expect_all_holds([F(1), F(1), F(25)], 25, "E_over_F25_weight_(25,1)",
                          "coefficient data of 1/[1, 1, 25] (base change to "
                          "F_25), window 12, holdout 4")
    assert d3["object"]["denominator"] == "[1, 1, 25]"
    d4 = expect_all_holds([F(1), F(-18), F(125)], 125,
                          "E_over_F125_weight_(125,1)",
                          "coefficient data of 1/[1, -18, 125] (base change "
                          "to F_125), window 12, holdout 4")
    assert d4["object"]["denominator"] == "[1, -18, 125]"

    # traces-mode run: deterministic REFUSAL at A1, annotated honestly.
    ptr = power_sums_from_satake(P, WINDOW)
    vt = detect(ptr, mode="traces", weight=(5, 1), holdout=HOLDOUT)
    dt = vt.as_dict()
    assert dt["refusal"] == "A1_FINITE_RANK", dt
    runs.append({
        "name": "E_traces_mode_refusal_annotated",
        "weight": [5, 1], "mode": "traces",
        "series": "p_1..p_12 of P = [1, 3, 5]",
        "verdict": dt,
        "annotation": (
            "HONEST ANNOTATION: the trace generating function sum_k p_k T^k "
            "= -T P'(T)/P(T) has numerator degree EQUAL to denominator "
            "degree; core.exact.minimal_rational_form only certifies proper "
            "forms (it truncates the numerator below deg Q), so the "
            "detector refuses at A1 in traces mode.  This is a properness "
            "limitation of the reconstruction interface, NOT a structural "
            "failure of the world: the same object is fully reconstructed "
            "and passes all five axioms in coefficient mode (see run "
            "E_over_F5_weight_(5,1)).  The refusal is deterministic and is "
            "recorded as detector metadata, not as evidence against E")})
    return runs


# ---------------------------------------------------------------------------
# Section 5: the world record
# ---------------------------------------------------------------------------

def build_world(W, N, P, detector_runs, tensor_checks, family_members):
    hasse = ("H. Hasse (1936), proof of the Riemann hypothesis for elliptic "
             "curves over finite fields (|a| <= 2 sqrt(q), via positivity "
             "of the degree form on the endomorphism ring)")
    weil = ("A. Weil (1948), Riemann hypothesis for curves and abelian "
            "varieties over finite fields (Castelnuovo inequality / Hodge "
            "index positivity)")
    deligne = "P. Deligne (1974), La conjecture de Weil I (general purity)"
    schmidt = ("F. K. Schmidt (1931), rationality and functional equation "
               "of zeta functions of curves over finite fields "
               "(Riemann-Roch)")
    artin = ("E. Artin (1924), zeta functions of function fields "
             "(doctoral thesis work)")
    groth = ("A. Grothendieck (1965), etale cohomology and the Lefschetz "
             "trace formula for Frobenius (SGA; cohomological expression "
             "of zeta)")

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=(W["nonsingular"] + ". " + W["counts"] +
                     ". Z(T) = exp(sum N_k T^k / k) is a well-defined "
                     "formal power series over Q with integer "
                     "coefficients; its closed form P/((1-T)(1-5T)) is "
                     "window-verified: " + W["exp_identity"]),
            citation=artin),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("effective divisors on E form the FREE commutative "
                     "monoid on closed points (a divisor is by definition "
                     "a finite Z_{>=0}-combination of closed points), so "
                     "the coefficient b_n factorizes over closed points -- "
                     "a complete combinatorial proof of local-global "
                     "multiplicativity; exact window witness: " +
                     W["euler_product"] + ". " + W["effectivity"]),
            citation=schmidt),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=(W["closed_points"] + ". " + W["euler_product"]),
            citation=(artin + "; " + schmidt)),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("each closed point x contributes the DEGREE-1 local "
                     "factor (1 - N(x)^{-s})^{-1} in its own variable "
                     "N(x)^{-s} (uniformly bounded degree, GL(1)-shaped "
                     "places); globally Z(T) is the rational function "
                     "[1,3,5]/[1,-6,5] with H^1 factor of degree exactly "
                     "2: detector A1 certifies P/Q on 12 terms with "
                     "held-out tail (run E_over_F5_weight_(5,1)); " +
                     W["coprime"]),
            citation=(schmidt + "; general varieties: B. Dwork (1960), "
                      "rationality of zeta functions; " + groth)),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("weight-1 self-duality of the H^1 datum, exact: " +
                     W["duality"] + "; product of inverse roots = 5 = q; " +
                     W["fe"]),
            citation=(schmidt + "; Poincare duality / Weil pairing: " +
                      weil)),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("canonical completed object IS Z itself: H^0 and H^2 "
                     "contribute the factors 1/(1-T) and 1/(1-5T) (the "
                     "function-field analogue of the gamma factor), the "
                     "conductor is trivial (E is smooth and proper over "
                     "F_5; every place is a good place), and the root "
                     "number is +1, read off exactly from the proved FE "
                     "identity (5T)^2 P(1/(5T)) = +5 P(T); " + W["fe"]),
            citation=schmidt),
        "L6_CONTINUATION_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("continuation: Z is literally the rational function "
                     "P/((1-T)(1-5T)) (entire in T except simple poles at "
                     "T = 1, 1/5), window-identity with the defining "
                     "series proved through T^6 and valid for all k by "
                     "Hasse (imported, and confirmed 5-for-5 at k = 2..6: "
                     + W["recursion_vs_raw"] + "). FUNCTIONAL EQUATION "
                     "PROVED EXACTLY HERE: " + W["fe"]),
            citation=(schmidt + "; " + hasse)),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=(W["twist"] + ". " + W["adams"] + ". " + W["sym2"] +
                     ". " + W["ext2"]),
            citation=("standard; quadratic twists and base change of "
                      "elliptic curves: " + hasse)),
        "L8_REALIZATION": cell(
            "HOLDS", "IMPORTED_THEOREM",
            witness=("geometric/motivic realization par excellence: P(T) "
                     "= det(1 - Frob T | H^1) for the actual smooth "
                     "projective curve E, and N_k = 5^k + 1 - p_k is the "
                     "Lefschetz fixed-point identity, instantiated "
                     "exactly here for k = 1..6 against raw exhaustive "
                     "counts; eigenvalue package realized by an explicit "
                     "integer matrix: " + W["companion"]),
            citation=(groth + "; elliptic case via End(E): " + hasse)),
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("the explicit formula is FINITE and EXACT here: "
                     "N_k = 5^k + 1 - alpha^k - beta^k pairs the zeros "
                     "against point counts with no analytic remainder "
                     "(verified k = 1..6, five independent confirmations); "
                     "and -- unlike the zeta world -- the positivity slot "
                     "is FILLED by an independent mechanism: " +
                     W["positivity"]),
            citation=(hasse + "; " + weil + "; " + deligne)),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("supplied by closed points of E/F_5 (free-monoid "
                     "divisor structure); " + W["closed_points"] + "; " +
                     W["euler_product"]),
            citation=artin),
        "DUALITY_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("supplied by Poincare duality / the Weil pairing on "
                     "H^1; the FE is proved exactly as a rational-function "
                     "identity: " + W["fe"] + "; " + W["duality"]),
            citation=schmidt),
        "TRACE_FORMULA": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("supplied by the Lefschetz fixed-point formula for "
                     "Frobenius: N_k = 5^k + 1 - p_k, instantiated exactly "
                     "for k = 1..6 (raw exhaustive counts vs power sums of "
                     "P: " + W["recursion_vs_raw"] + ")"),
            citation=(groth + "; " + hasse)),
        "POSITIVITY_PURITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("THE MODEL CELL. Mechanism identified by name: "
                     "Frobenius eigenvalue purity via Castelnuovo "
                     "positivity -- concretely, positive-definiteness of "
                     "the degree form on End(E) (Hasse). Exact instance "
                     "certificates: " + W["positivity"] + " " + W["purity"] +
                     " " + W["sturm"] + ". This is the mechanism that "
                     "FORCES the critical line in this world, and its "
                     "analogue is precisely what the zeta world lacks"),
            citation=(hasse + "; " + weil + "; " + deligne)),
        "TENSOR_OPS": cell(
            "HOLDS", "EXACT_WITNESS",
            witness=("Sym^2, Ext^2, Adams (base change), dual and tensor "
                     "all computed exactly on the Satake datum with purity "
                     "preserved and COMPLETE certificates in degrees <= 3: "
                     + W["sym2"] + "; " + W["ext2"] + "; " + W["adams"] +
                     "; A6 machinery runs embedded in detector_runs"),
            citation=weil),
        "FAMILY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("horizontal AND vertical family structure verified "
                     "exactly: " + W["family"] + ". Vertical: base changes "
                     "to F_25 and F_125 carry complete purity certificates "
                     "(discs -99 and -176 < 0). The Hasse structure P_AB = "
                     "1 - aT + 5T^2 for each member is imported; the "
                     "sweep's strict inequality a^2 < 4q is exhaustive and "
                     "exact"),
            citation=hasse),
    }

    critical_line = {
        "status": "THEOREM",
        "detail": ("ALL zeros of Z(T) = P(T)/((1-T)(1-5T)) lie on "
                   "|T| = 5^(-1/2), equivalently Re(s) = 1/2 under "
                   "T = 5^(-s).  For THIS INSTANCE the statement is a "
                   "finite exact computation completed in this build: the "
                   "complete degree-2 purity test (product of inverse "
                   "roots = 5, disc = -11 < 0) plus the exact FE.  It "
                   "presupposes P is the true numerator for all k, which "
                   "is Hasse's theorem (imported) and is confirmed here "
                   "against independent exhaustive counts for k = 1..6.  "
                   "For the CLASS: Hasse (1936) for elliptic curves; Weil "
                   "(1948) for curves and abelian varieties; Deligne "
                   "(1974) for smooth projective varieties.  None of this "
                   "transfers to RH over Q; rh_established = false."),
        "rigor": "PROVED_HERE",
        "citation": (hasse + "; " + weil + "; " + deligne),
        "witness": (W["purity"] + " " + W["sturm"]),
    }

    world = {
        "id": "ff_elliptic_f5",
        "title": ("Zeta of the elliptic curve y^2 = x^3 + x + 1 over F_5 "
                  "(model world for positivity/purity)"),
        "definition": ("E: y^2 = x^3 + x + 1 over F_5 (nonsingular: cubic "
                       "discriminant -31 == 4 mod 5).  Z(T) = exp(sum_{k>=1}"
                       " #E(F_{5^k}) T^k / k) = P(T)/((1-T)(1-5T)) with "
                       "P(T) = 1 + 3T + 5T^2 (a_1 = -3 from N_1 = 9).  "
                       "Point counts N_k = [9, 27, 108, 675, 3069, 15552] "
                       "for k = 1..6, by exhaustive enumeration over "
                       "explicitly constructed fields F_{5^k}."),
        "arithmetic_class": ("EXACT_RATIONAL; zeta of a smooth projective "
                             "genus-1 curve over F_5; H^1 is a weight-1 "
                             "pure motive of rank 2; function-field analogue"
                             " of a degree-2 L-function"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "H. Hasse (1936), Riemann hypothesis for elliptic curves over "
            "finite fields (Crelle series of three papers on abstract "
            "elliptic function fields)",
            "E. Artin (1924), thesis work on zeta functions of function "
            "fields",
            "F. K. Schmidt (1931), rationality and functional equation for "
            "curve zeta functions",
            "A. Weil (1948), Riemann hypothesis for curves and abelian "
            "varieties (Castelnuovo / Hodge index positivity)",
            "P. Deligne (1974), La conjecture de Weil I",
            "B. Dwork (1960), rationality of zeta functions of varieties "
            "over finite fields",
            "A. Grothendieck (1965), etale cohomology, Lefschetz trace "
            "formula for Frobenius (SGA)",
            "J. H. Silverman, The Arithmetic of Elliptic Curves (degree "
            "form positivity and the Hasse bound, ch. V)",
        ],
        "rh_established": False,
        "notes": (
            "MODEL WORLD for the POSITIVITY_PURITY mechanism: every ladder "
            "row closes, and L9 closes through an IDENTIFIED, FINITE, "
            "EXACTLY-CHECKED positivity input (degree-form "
            "positive-definiteness, certified by disc = -11 < 0 and the "
            "SOS identity 4(m^2 - 3mn + 5n^2) = (2m - 3n)^2 + 11n^2), in "
            "deliberate contrast to the zeta world where the same slot is "
            "OPEN (Weil positivity is RH-equivalent, not supplied).  All "
            "witnesses are Fraction/integer computations; NO floats appear "
            "anywhere in this build.  The traces-mode detector refusal "
            "embedded in detector_runs is an annotated interface "
            "limitation (numerator degree = denominator degree), not "
            "evidence against the world.  Nothing here bears on RH over "
            "Q: rh_established = false."),
        "detector_runs": {
            "description": ("core.reconstruct.detect on exact coefficient "
                            "data (window 12, holdout 4): E at weight "
                            "(5,1), quadratic twist at (5,1), base changes "
                            "at (25,1) and (125,1) -- all five axioms HOLD "
                            "with the COMPLETE deg-2 A4 purity branch; one "
                            "annotated traces-mode refusal; plus exact "
                            "tensor checks"),
            "runs": detector_runs,
            "tensor_checks": tensor_checks,
            "point_counts": {"N_k_over_F_5^k, k=1..6": N,
                             "closed_points_B_d": {str(d): b for d, b in
                                                   [(1, 9), (2, 9), (3, 33),
                                                    (4, 162), (5, 612),
                                                    (6, 2571)]},
                             "family_sweep_members_(A,B,N,a)":
                                 [list(m) for m in family_members]},
        },
    }
    return world


def main():
    W, N, P, p, fields = build_counts_and_satake()
    Wfe, Qd = build_fe_witnesses(P)
    W.update(Wfe)
    Wep, B = build_euler_product_witnesses(N, P, Qd)
    W.update(Wep)
    W.update(build_purity_witnesses(P))
    Wt, tensor_checks = build_tensor_witnesses(P, p, N)
    W.update(Wt)
    W["family"], family_members = build_family_sweep()
    detector_runs = run_detector(P)
    world = build_world(W, N, P, detector_runs, tensor_checks, family_members)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("N_k:", N)
    print("P:", fmt(P))
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector runs:",
          [(r["name"], r["verdict"]["refusal"]) for r in detector_runs])


if __name__ == "__main__":
    main()
