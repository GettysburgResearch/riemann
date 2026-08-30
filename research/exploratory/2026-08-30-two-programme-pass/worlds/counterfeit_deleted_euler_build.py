"""World 'counterfeit_deleted_euler': the 2-deleted zeta

    zeta_odd(s) = (1 - 2^{-s}) zeta(s) = sum_{n odd} n^{-s} = L(s, chi_0 mod 2),

the Riemann zeta function with its Euler factor at p = 2 deleted; equivalently
the (imprimitive) Dirichlet L-function of the principal character mod 2.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.counterfeit_deleted_euler_build

regenerates worlds/counterfeit_deleted_euler.json identically.

ROLE IN THE MATRIX.  Deleting ONE Euler factor keeps every local structure
(complete multiplicativity, Euler product over the odd primes, bounded-degree
weight-0 self-dual local factors, twist/tensor calculus, an explicit-formula
prime side with nonnegative von Mangoldt coefficients) and kills exactly one
thing: the reflection symmetry s -> 1-s of the zero set, hence every
functional equation of standard reflection type.  This is the exact converse
of the 'davenport_heilbronn' row (duality without Euler product); here:
Euler product without duality, by the most local possible surgery.

EXACT LAYER (Fraction / integer arithmetic only; no floats anywhere in this
file):
  1. a_n = [n odd] (0/1 indicator).  Coefficient-wise identities verified
     exactly for ALL n <= 512:
       (a) deleted-factor identity: the Dirichlet convolution of
           c = (1, -1 at n=2, 0, 0, ...) with the all-ones sequence equals a
           — i.e. (1 - 2^{-s}) zeta(s) = sum_{n odd} n^{-s} formally;
       (b) COMPLETE multiplicativity: a_{mn} = a_m a_n for every pair
           m, n >= 2 with mn <= 512 (exhaustive), on top of the one-line
           full proof a_n = [gcd(n,2) = 1] = chi_0 mod 2;
       (c) Euler product over the ODD primes: the truncated Dirichlet
           convolution of the local geometric series at every odd prime
           p <= 512 reproduces (a_n)_{n<=512} exactly; the factor at 2 is
           the constant 1 (deleted);
       (d) explicit-formula prime side: with Lambda_odd supported on odd
           prime powers, the convolution identity
           sum_{d | n} Lambda_odd(d) a_{n/d} = a_n log n holds for all
           n <= 512 as an identity in the free Z-module on symbols
           {log p : p prime} (so -zeta_odd'/zeta_odd = sum over ODD prime
           powers of Lambda(n) n^{-s}, all coefficients >= 0);
       (e) twist repair: the termwise twist by the primitive odd character
           chi_{-4} mod 4 equals the PRIMITIVE L(s, chi_{-4})
           coefficient-wise to 512 (a 2-ramified twist erases the defect);
       (f) local detector runs and an exact local tensor certificate.
  2. THE HEADLINE (L6 FAILS, exact zero-symmetry witness):
       s_k = 2 pi i k / log 2  (k a nonzero integer) satisfies
       2^{-s_k} = e^{-s_k log 2} = e^{-2 pi i k} = 1 EXACTLY — note log 2
       enters only through this cancellation; no numerical value of log 2 is
       used anywhere.  Hence 1 - 2^{-s_k} = 0, and since zeta is finite at
       s_k (its only pole is s = 1; imported, Riemann 1859),
       zeta_odd(s_k) = 0.  At the reflected point,
       2^{-(1 - s_k)} = 2^{-1} 2^{s_k} = 1/2 exactly, so
       |1 - 2^{-(1-s_k)}| = 1/2 != 0, and zeta(1 - s_k) = zeta(1 + i t_k)
       with t_k = -2 pi k / log 2 != 0 is NONZERO — imported theorem
       (J. Hadamard 1896; C.-J. de la Vallee Poussin 1896).  Therefore
       zeta_odd(1 - s_k) != 0: the zero multiset of zeta_odd is NOT
       invariant under s -> 1 - s.
     PRECISE STATEMENT PROVED (the scope of 'FAILS'): no identity
       F(s) zeta_odd(s) = w G(s) zeta_odd(1-s)   (w != 0),
     with F, G meromorphic and finite-and-nonvanishing at s_1 and 1 - s_1
     respectively, can hold: evaluation at s = s_1 gives 0 = w G(s_1) *
     (nonzero).  In particular no completed functional equation
     Lambda(s) = w Lambda(1-s) or Lambda(s) = w conj(Lambda(1 - conj(s)))
     with Lambda(s) = Q^s prod_j Gamma(lambda_j s + mu_j) zeta_odd(s)
     (Q > 0, lambda_j > 0, mu_j real) exists: Gamma never vanishes and has
     poles only at real arguments, while lambda_j s_k + mu_j has imaginary
     part lambda_j 2 pi k / log 2 != 0.  Strengthening: even allowing
     complex mu_j (Selberg-class-type data), each factor
     Gamma(lambda_j s + mu_j) has at most ONE pole on the line Re s = 0
     (its poles s = (-n - mu_j)/lambda_j, n = 0, 1, 2, ..., have strictly
     decreasing real parts), so any finite product of gamma factors is
     finite and nonvanishing at all but finitely many of the infinitely
     many exact zeros {s_k : k != 0} — while EVERY reflected point 1 - s_k
     is a non-zero of zeta_odd.  So no reflection-type FE survives even
     with finitely many gamma-pole exceptions.  What is NOT refuted:
     'functional equations' relating zeta_odd to a DIFFERENT function
     (e.g. the trivial rewriting through the FE of zeta itself).
  3. critical_line: FALSE for the natural formulation 'all nontrivial zeros
     (non-real zeros in the closed strip 0 <= Re s <= 1) lie on
     Re s = 1/2': s_1 = 2 pi i / log 2 is a non-real zero with Re s_1 = 0.
     The surviving zeros of zeta_odd are exactly the zeros of zeta, which
     are CONJECTURALLY on Re s = 1/2 (RH, open).  rh_established = false
     everywhere.

IMPORTS (the complete list — everything else is PROVED_HERE):
  I1. zeta has a meromorphic continuation to C whose only pole is a simple
      pole at s = 1 (B. Riemann, 1859).
  I2. zeta(1 + it) != 0 for real t != 0 (J. Hadamard, 1896; C.-J. de la
      Vallee Poussin, 1896 — the nonvanishing at the edge of the strip from
      the prime number theorem proofs).
  I3. Classical Gamma-function facts (Euler/Weierstrass, 18th-19th c.):
      Gamma is nowhere zero and its poles are exactly the nonpositive
      integers.  (Used only to scope which completing factors the L6
      refutation covers.)
  I4. e^{2 pi i m} = 1 for every integer m (Euler's identity; elementary).
  I5. For the L7 note only: the primitive Dirichlet L-function L(s, chi_{-4})
      satisfies the classical odd-character functional equation
      (A. Hurwitz ~1882; exposition H. Davenport, Multiplicative Number
      Theory, 1967).
"""

from fractions import Fraction

from core.exact import (
    F,
    power_sums_from_satake,
    op_tensor,
    op_dual_satake,
    satake_poly_from_power_sums,
)
from core.reconstruct import detect, tensor_compatibility, HOLDS, SKIPPED
from core.worlds import cell, save_world, validate_world

N = 512                 # exact coefficient-wise verification range
DETECTOR_WINDOW = 12    # detector window (a_{p^0} .. a_{p^11})
HOLDOUT = 4             # detector holdout
ZERO_FAMILY_K = [-3, -2, -1, 1, 2, 3, 5, 8]   # exact zero-family exponents


# ---------------------------------------------------------------------------
# Elementary exact number theory helpers (integers only — exact)
# ---------------------------------------------------------------------------

def primes_upto(n):
    """Deterministic sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= n:                       # pure integer bound (no floats)
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = False
        p += 1
    return [p for p in range(2, n + 1) if sieve[p]]


def factorize(n):
    """Exact factorization by trial division; returns {p: v_p(n)}."""
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


def dirichlet_conv(f, g, n):
    """Exact Dirichlet convolution of integer arrays indexed 1..n."""
    h = [0] * (n + 1)
    for d in range(1, n + 1):
        if f[d]:
            for m in range(1, n // d + 1):
                h[d * m] += f[d] * g[m]
    return h


# ---------------------------------------------------------------------------
# Step A: the coefficient layer — a_n = [n odd], all identities exact
# ---------------------------------------------------------------------------

def coefficient_layer():
    """Exact coefficient-wise verifications (a)-(c) and (e).  Every claim is
    asserted before its witness string is embedded."""
    W = {}
    a = [0] + [1 if n % 2 == 1 else 0 for n in range(1, N + 1)]

    # -- (a) deleted-factor identity: (1 - 2^{-s}) zeta = sum_{n odd} n^{-s}
    c = [0] * (N + 1)
    c[1], c[2] = 1, -1                      # Dirichlet series 1 - 2^{-s}
    ones = [0] + [1] * N                    # Dirichlet series of zeta
    conv = dirichlet_conv(c, ones, N)
    assert conv[1:] == a[1:]
    W["deleted_factor"] = (
        "deleted-factor identity verified coefficient-wise for ALL n <= "
        f"{N}: the Dirichlet convolution of (1, -1 at n=2, 0, ...) with the "
        "all-ones sequence equals a_n = [n odd] exactly — i.e. "
        "(1 - 2^{-s}) zeta(s) = sum_{n odd} n^{-s} as formal Dirichlet "
        "series (and hence as analytic functions on Re s > 1 by absolute "
        "convergence, coefficients bounded by 1)")

    # -- (b) COMPLETE multiplicativity, exhaustively checked ----------------
    pairs = coprime_pairs = 0
    for m in range(2, N + 1):
        for n in range(2, N // m + 1):
            assert a[m * n] == a[m] * a[n], (m, n)
            pairs += 1
            # gcd via Euclid (exact integers)
            x, y = m, n
            while y:
                x, y = y, x % y
            if x == 1:
                coprime_pairs += 1
    assert pairs == sum(max(N // m - 1, 0) for m in range(2, N + 1))
    W["multiplicativity"] = (
        "COMPLETE multiplicativity a_{mn} = a_m a_n verified exactly for "
        f"all {pairs} pairs m, n >= 2 with mn <= {N} (of which "
        f"{coprime_pairs} coprime pairs — ordinary multiplicativity is the "
        "coprime subset).  Full one-line proof, valid for ALL m, n: "
        "a_n = [gcd(n, 2) = 1] is the principal Dirichlet character chi_0 "
        "mod 2, and gcd(mn, 2) = 1 iff gcd(m, 2) = 1 and gcd(n, 2) = 1; "
        "the finite check corroborates the proof")

    # -- (c) Euler product over the ODD primes, coefficient-wise ------------
    odd_primes = [p for p in primes_upto(N) if p != 2]
    E = [0] * (N + 1)
    E[1] = 1
    for p in odd_primes:
        local = [0] * (N + 1)
        pk = 1
        while pk <= N:                      # local factor 1/(1 - p^{-s}):
            local[pk] = 1                   # geometric series, coeffs 1
            pk *= p
        E = dirichlet_conv(E, local, N)
    assert E[1:] == a[1:]
    # the factor at p = 2 is the constant 1: including it changes nothing
    # (its truncated Dirichlet series is the identity delta_1) — deleted.
    W["euler_product"] = (
        "Euler product over the ODD primes verified coefficient-wise for "
        f"ALL n <= {N}: the truncated Dirichlet convolution of the local "
        "geometric series (coefficients a_{p^k} = 1, i.e. local factor "
        f"1/(1 - p^{{-s}})) over all {len(odd_primes)} odd primes p <= {N} "
        "reproduces a_n = [n odd] exactly.  The local factor at p = 2 is "
        "the CONSTANT 1 (the deleted factor): its truncated Dirichlet "
        "series is delta_1 and contributes nothing.  Formally the product "
        "also follows from complete multiplicativity plus |a_n| <= 1")

    return W, a


def twist_repair():
    """Exact check (e): termwise twist by chi_{-4} equals the primitive
    L(s, chi_{-4}) coefficient-wise, Euler product included."""
    chi4 = [0] + [(0, 1, 0, -1)[n % 4] for n in range(1, N + 1)]
    a = [0] + [1 if n % 2 == 1 else 0 for n in range(1, N + 1)]
    # termwise twist: (a_n chi4(n)) == (chi4(n)) since chi4 kills even n
    for n in range(1, N + 1):
        assert a[n] * chi4[n] == chi4[n]
    # chi4 is completely multiplicative: full Euler product over odd primes
    odd_primes = [p for p in primes_upto(N) if p != 2]
    E4 = [0] * (N + 1)
    E4[1] = 1
    for p in odd_primes:
        local = [0] * (N + 1)
        pk, v = 1, 1
        while pk <= N:
            local[pk] = v
            pk *= p
            v *= chi4[p]
        E4 = dirichlet_conv(E4, local, N)
    assert E4[1:] == chi4[1:]
    return (
        "TWIST REPAIR (exact, all n <= 512): the termwise twist of zeta_odd "
        "by the primitive odd character chi_{-4} mod 4 has coefficients "
        "a_n chi_{-4}(n) = chi_{-4}(n) — identical to the PRIMITIVE "
        "L(s, chi_{-4}) (chi_{-4} already vanishes on even n, so the "
        "deleted 2-factor is invisible after this ramified twist); its full "
        "Euler product prod_{p odd} (1 - chi_{-4}(p) p^{-s})^{-1} is "
        "verified coefficient-wise to 512.  L(s, chi_{-4}) DOES satisfy a "
        "genuine reflection functional equation (imported, classical "
        "odd-character FE) — the duality defect of zeta_odd is concentrated "
        "entirely at the deleted prime 2 and is erased by any twist "
        "ramified at 2.  Twists by characters chi with chi(2) != 0 instead "
        "REPRODUCE the defect: sum_{n odd} chi(n) n^{-s} = "
        "(1 - chi(2) 2^{-s}) L(s, chi), another one-factor deletion")


# ---------------------------------------------------------------------------
# Step B: explicit-formula prime side — symbolic von Mangoldt identity
# ---------------------------------------------------------------------------

def von_mangoldt_prime_side():
    """Exact identity in the free Z-module on symbols {log p}:
    sum_{d | n} Lambda_odd(d) a_{n/d} = a_n log n for all n <= N, where
    Lambda_odd(p^k) = log p for ODD primes p and Lambda_odd = 0 elsewhere.
    Hence -zeta_odd'/zeta_odd = sum_{n an odd prime power} Lambda(n) n^{-s}
    formally, with all coefficients nonnegative (integer multiples >= 0 of
    the symbols log p)."""
    a = [0] + [1 if n % 2 == 1 else 0 for n in range(1, N + 1)]
    checked = 0
    for n in range(1, N + 1):
        # rhs: a_n * log n as an exponent vector {p: v_p(n)}
        rhs = {p: e for p, e in factorize(n).items()} if (a[n] and n > 1) \
            else {}
        # lhs: sum over divisors d = p^k (p odd) of Lambda(d) a_{n/d}
        lhs = {}
        for p, e in factorize(n).items():
            if p == 2:
                continue
            pk = 1
            for _ in range(e):              # d = p, p^2, ..., p^e divide n
                pk *= p
                if a[n // pk]:
                    lhs[p] = lhs.get(p, 0) + 1
        lhs = {p: v for p, v in lhs.items() if v}
        assert lhs == rhs, (n, lhs, rhs)
        checked += 1
    assert checked == N
    return (
        "EXPLICIT-FORMULA PRIME SIDE (exact, symbolic): with Lambda_odd "
        "supported on odd prime powers (Lambda_odd(p^k) = log p, p odd), "
        "the convolution identity sum_{d|n} Lambda_odd(d) a_{n/d} = "
        f"a_n log n was verified for ALL n <= {N} as an identity in the "
        "free Z-module on the symbols {log p : p prime} (log n = sum_p "
        "v_p(n) log p; no floating-point logarithm anywhere).  Hence "
        "-zeta_odd'/zeta_odd(s) = sum over ODD prime powers of "
        "Lambda(n) n^{-s} as formal Dirichlet series: the log-derivative "
        "is still a Dirichlet series with NONNEGATIVE von Mangoldt "
        "coefficients — the arithmetic prime side of an explicit formula "
        "survives the deletion intact (it merely loses the powers of 2).  "
        "Equivalently -zeta_odd'/zeta_odd = -zeta'/zeta - log 2 "
        "sum_{k>=1} 2^{-ks}, and the zero side of the corresponding "
        "explicit formula gains the exact vertical progression "
        "{2 pi i k/log 2 : k in Z} on Re s = 0")


# ---------------------------------------------------------------------------
# Step C: THE HEADLINE — exact zero-symmetry witness refuting any
# reflection-type functional equation (L6 FAILS)
# ---------------------------------------------------------------------------

def zero_symmetry_witness():
    """Exact algebra layer of the L6 refutation.

    Numbers of the form e^{2 pi i q}, q rational, equal 1 exactly iff q is
    an integer (import I4: Euler's identity).  The whole computation runs in
    that exact model plus Fraction arithmetic; log 2 appears ONLY through
    the cancellation (2 pi i k / log 2) * log 2 = 2 pi i k."""
    checked = []
    for k in ZERO_FAMILY_K:
        assert k != 0
        # s_k = 2 pi i k / log 2.  Exponent of 2^{-s_k} = e^{-s_k log 2}:
        # -s_k log 2 = 2 pi i * (-k).  q = -k is an INTEGER:
        q = Fraction(-k)
        assert q.denominator == 1           # => e^{2 pi i q} = 1 exactly (I4)
        two_pow_minus_sk = Fraction(1)      # 2^{-s_k} = 1 EXACTLY
        euler_factor_at_sk = Fraction(1) - two_pow_minus_sk
        assert euler_factor_at_sk == 0      # (1 - 2^{-s}) vanishes at s_k
        # Reflected point 1 - s_k:  2^{-(1-s_k)} = 2^{-1} * 2^{s_k};
        # exponent of 2^{s_k} is 2 pi i * k, k an INTEGER:
        q2 = Fraction(k)
        assert q2.denominator == 1          # => 2^{s_k} = 1 exactly (I4)
        two_pow_at_reflection = Fraction(1, 2) * Fraction(1)
        euler_factor_at_reflection = Fraction(1) - two_pow_at_reflection
        assert euler_factor_at_reflection == Fraction(1, 2)
        assert euler_factor_at_reflection != 0
        # zeta pin at the reflected point: 1 - s_k = 1 + i t_k with
        # t_k = -2 pi k / log 2 != 0 (k != 0; 2 pi != 0; log 2 finite,
        # nonzero since 2 != 1).  Import I2 gives zeta(1 + i t_k) != 0.
        checked.append(k)
    assert checked == ZERO_FAMILY_K

    # Family version at other deleted primes (for the FAMILY mechanism):
    # deleting the factor at p yields zeros at 2 pi i k / log p whose
    # reflections carry Euler-factor value 1 - 1/p != 0.
    family_vals = {}
    for p in (2, 3, 5):
        v = Fraction(1) - Fraction(1, p)
        assert v == Fraction(p - 1, p) and v != 0
        family_vals[p] = v
    assert family_vals[2] == Fraction(1, 2)

    witness = (
        "EXACT ZERO-SYMMETRY WITNESS.  For every nonzero integer k put "
        "s_k = 2 pi i k / log 2 (Re s_k = 0).  Then 2^{-s_k} = "
        "e^{-s_k log 2} = e^{-2 pi i k} = 1 EXACTLY — log 2 enters only "
        "through this cancellation (import I4: e^{2 pi i m} = 1 for m in "
        "Z); no numerical value of log 2 is used.  Hence the Euler factor "
        "(1 - 2^{-s}) vanishes at s_k, and since zeta is finite at s_k "
        "(only pole s = 1, Re = 1 != 0: import I1, Riemann 1859), "
        "zeta_odd(s_k) = (1 - 2^{-s_k}) zeta(s_k) = 0: an exact zero.  At "
        "the reflected point, 2^{-(1 - s_k)} = 2^{-1} 2^{s_k} = 1/2 "
        "exactly, so 1 - 2^{-(1-s_k)} = 1/2 != 0; and zeta(1 - s_k) = "
        "zeta(1 + i t_k) with t_k = -2 pi k / log 2 real and nonzero, "
        "which is NONZERO by import I2 (Hadamard 1896; de la Vallee "
        "Poussin 1896).  Therefore zeta_odd(1 - s_k) = "
        "(1/2) zeta(1 - s_k) != 0.  CONCLUSION (proved): the zero multiset "
        "of the continued zeta_odd is NOT invariant under s -> 1 - s; "
        "witness pair (s_1 = 2 pi i / log 2 is a zero, 1 - s_1 is not), "
        "and in fact an infinite family {s_k : k in Z, k != 0} of zeros "
        "on Re s = 0 ALL of whose reflections are non-zeros.  Verified "
        "here for k in " + str(ZERO_FAMILY_K) + " (uniform proof for all "
        "k != 0)")

    scope = (
        "PRECISE SCOPE OF 'FAILS' (the exact statement proved).  Refuted: "
        "every identity F(s) zeta_odd(s) = w G(s) zeta_odd(1 - s) of "
        "meromorphic functions on C with w != 0 and F, G finite and "
        "nonvanishing at s_1 and 1 - s_1 respectively — evaluating at "
        "s = s_1 gives 0 on the left and w G(s_1) zeta_odd(1 - s_1) != 0 "
        "on the right.  This covers every completed FE Lambda(s) = "
        "w Lambda(1 - s) and every conjugate-dual FE Lambda(s) = "
        "w conj(Lambda(1 - conj(s))) with Lambda(s) = Q^s prod_j "
        "Gamma(lambda_j s + mu_j) zeta_odd(s), Q > 0, lambda_j > 0, mu_j "
        "real: such factors are finite and nonvanishing at every point "
        "with nonzero imaginary part (import I3: Gamma is zero-free with "
        "poles exactly at the nonpositive integers, and lambda_j s_k + "
        "mu_j has imaginary part lambda_j 2 pi k / log 2 != 0); the "
        "conjugate-dual variant is refuted by the SAME family since "
        "1 - conj(s_k) = 1 - s_{-k} is also a non-zero.  STRENGTHENING "
        "(elementary): even allowing complex mu_j with a gamma pole placed "
        "on Re s = 0, each factor Gamma(lambda_j s + mu_j) has at most "
        "ONE pole on that line (its poles s = (-n - mu_j)/lambda_j, "
        "n >= 0, have strictly decreasing real parts), so a finite product "
        "of gamma factors (times Q^s, zero-free, and any polynomial "
        "factor, finitely many zeros) is finite and nonvanishing at all "
        "but FINITELY many of the infinitely many exact zeros s_k, while "
        "EVERY reflection 1 - s_k is a non-zero: no reflection-type FE "
        "survives even with finitely many exceptional factors.  NOT "
        "refuted (honesty): identities relating zeta_odd(s) to a "
        "DIFFERENT function at 1 - s — e.g. zeta_odd(s) = (1 - 2^{-s}) "
        "chi(s) zeta(1 - s) via the FE of zeta itself — exist trivially; "
        "the failure is specifically the self-reflection of zeta_odd, "
        "i.e. the s -> 1-s symmetry of ITS zero set")

    return witness, scope


# ---------------------------------------------------------------------------
# Step D: local structure — detector runs and exact tensor certificate
# ---------------------------------------------------------------------------

def local_structure():
    """Detector certificates: odd primes carry the degree-1 weight-0 factor
    1 - T; the prime 2 carries the EMPTY (degree-0) factor — the detector
    sees the deletion.  Plus an exact self-duality and tensor certificate."""
    runs = []
    one = Fraction(1)

    # odd primes: column a_{p^k} = 1 for all k -> local factor 1 - T
    for p in (3, 5):
        col = [one] * DETECTOR_WINDOW
        d = detect(col, mode="coefficients", weight=(p, 0),
                   holdout=HOLDOUT).as_dict()
        assert d["refusal"] is None, d
        assert d["object"]["degree"] == 1
        assert d["object"]["denominator"] == "[1, -1]"
        got = {x["axiom"]: x["status"] for x in d["cells"]}
        assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                       "A3_INTEGRALITY": HOLDS, "A4_PURITY": HOLDS,
                       "A5_HELD_OUT": HOLDS}, got
        runs.append({"prime": p, "weight": [p, 0], "mode": "coefficients",
                     "series": f"true column (a_{{{p}^k}}) = [1,1,1,...], "
                               f"window {DETECTOR_WINDOW}",
                     "verdict": d})

    # p = 2: column a_{2^k} = [1, 0, 0, ...] -> DEGREE-0 (empty) factor
    col2 = [one] + [Fraction(0)] * (DETECTOR_WINDOW - 1)
    d2 = detect(col2, mode="coefficients", weight=(2, 0),
                holdout=HOLDOUT).as_dict()
    assert d2["refusal"] is None, d2
    assert d2["object"]["degree"] == 0
    assert d2["object"]["denominator"] == "[1]"
    got2 = {x["axiom"]: x["status"] for x in d2["cells"]}
    assert got2 == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                    "A3_INTEGRALITY": HOLDS, "A4_PURITY": SKIPPED,
                    "A5_HELD_OUT": HOLDS}, got2
    runs.append({"prime": 2, "weight": [2, 0], "mode": "coefficients",
                 "series": "true column (a_{2^k}) = [1,0,0,...], window "
                           f"{DETECTOR_WINDOW}",
                 "note": "the detector SEES the deletion: certified local "
                         "factor of degree 0 (the constant 1); A4 purity "
                         "is vacuous for an empty factor (SKIPPED)",
                 "verdict": d2})

    # exact self-duality of the odd local factor: dual of 1 - T is 1 - T
    sat = [Fraction(1), Fraction(-1)]
    assert op_dual_satake(sat, Fraction(1)) == sat
    # exact weight-0 purity of the inverse root: alpha = 1, alpha^2 = p^0
    assert Fraction(1) ** 2 == Fraction(1)

    # exact local tensor certificate at an odd prime:
    # (1 - T) tensor (1 - T) = 1 - T; predicted coefficients all ones
    ps = power_sums_from_satake(sat, 8)
    assert ps == [Fraction(1)] * 8
    pt = op_tensor(ps, ps, 8)
    assert pt == [Fraction(1)] * 8
    assert satake_poly_from_power_sums(pt[:1], 1) == sat
    tc = tensor_compatibility(sat, sat, [Fraction(1)] * 8)
    assert tc["status"] == HOLDS, tc

    witness = (
        "LOCAL STRUCTURE (exact).  Odd p: local factor 1/(1 - p^{-s}), "
        "Satake polynomial 1 - T (degree 1), inverse root alpha = 1 with "
        "alpha^2 = 1 = p^0 (weight-0 purity, exact) and op_dual_satake"
        "([1,-1], 1) == [1,-1] (self-dual, exact); detector certificates "
        "at p = 3, 5 with weight (p, 0): degree 1, denominator 1 - T, all "
        "five axioms HOLD.  p = 2: the detector run on the true column "
        "(a_{2^k}) = [1, 0, 0, ...] certifies a DEGREE-0 local factor "
        "(the constant 1) — the deletion is visible as an empty local "
        "object, not as any local pathology.  Tensor certificate: "
        "(1 - T) tensor (1 - T) = 1 - T with all predicted coefficients "
        "verified (A6 HOLDS).  Uniform degree bound: deg L_p = 1 for odd "
        "p, deg L_2 = 0 — bounded by 1 everywhere")
    return witness, runs


# ---------------------------------------------------------------------------
# The world record
# ---------------------------------------------------------------------------

def build_world(CW, mult_a, twist_w, vm_witness, zw, scope, loc_w, runs):
    riemann1859 = ("B. Riemann (1859), Ueber die Anzahl der Primzahlen "
                   "unter einer gegebenen Groesse: meromorphic "
                   "continuation of zeta with a single simple pole at "
                   "s = 1 (import I1)")
    hdlvp1896 = ("J. Hadamard (1896); C.-J. de la Vallee Poussin (1896): "
                 "zeta(1 + it) != 0 for real t != 0 (edge-of-strip "
                 "nonvanishing from the prime number theorem proofs; "
                 "import I2)")
    gamma_classical = ("classical Gamma-function theory (Euler, "
                       "Weierstrass, 18th-19th c.): Gamma is zero-free "
                       "with poles exactly at the nonpositive integers "
                       "(import I3)")
    fe_import = ("classical functional equation of primitive Dirichlet "
                 "L-functions (A. Hurwitz ~1882; exposition H. Davenport, "
                 "Multiplicative Number Theory, 1967) — used ONLY for the "
                 "L7 note that the chi_{-4}-twist has a genuine FE "
                 "(import I5)")
    selberg_cn = ("CITATION-NEEDED: A. Selberg (~1989-1992), Old and new "
                  "conjectures ... (definition of the Selberg class, "
                  "whose functional-equation axiom zeta_odd fails)")

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=("zeta_odd(s) = sum_{n odd} n^{-s}: 0/1 coefficients, "
                     "absolutely convergent for Re s > 1; identified with "
                     "(1 - 2^{-s}) zeta(s) exactly — " +
                     CW["deleted_factor"] + ".  Meromorphic continuation "
                     "to C with a single simple pole at s = 1 (residue "
                     "1/2) inherited from zeta through this identity "
                     "(continuation of zeta imported)"),
            citation=riemann1859),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=CW["multiplicativity"]),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=CW["euler_product"]),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "PROVED_HERE",
            witness=("uniform degree bound 1: L_p(T) = 1 - T (degree 1) "
                     "at every odd prime, L_2(T) = 1 (degree 0, the "
                     "deleted slot).  " + loc_w)),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("every local factor PRESENT is weight-0 pure and "
                     "self-dual, exactly: Satake polynomial 1 - T, inverse "
                     "root 1 with 1^2 = p^0, op_dual_satake([1,-1], 1) == "
                     "[1,-1]; the empty factor at 2 is trivially self-"
                     "dual.  SCOPE: local weight/duality data is fully "
                     "coherent — the GLOBAL duality failure (L6) is not a "
                     "local-weight incoherence but the imprimitivity of "
                     "the deleted slot; this world separates 'coherent "
                     "local duality data' from 'global functional "
                     "equation'")),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "FAILS", "PROVED_HERE",
            witness=("no canonical (conductor, gamma, root number) datum "
                     "exists FOR zeta_odd ITSELF: any such datum would "
                     "complete zeta_odd to a functional equation of "
                     "standard reflection type, and every such FE is "
                     "refuted exactly by the L6 zero-symmetry witness "
                     "(s_1 = 2 pi i / log 2 is a zero, 1 - s_1 is not).  "
                     "The FE-carrying completed object in zeta_odd's "
                     "packet is the PRIMITIVE zeta (conductor 1, "
                     "Gamma_R(s) = pi^{-s/2} Gamma(s/2), root number +1) "
                     "— it completes zeta, not zeta_odd; imprimitive "
                     "character L-functions carry no canonical triple of "
                     "their own"),
            citation=hdlvp1896 + "; " + riemann1859),
        "L6_CONTINUATION_FE": cell(
            "FAILS", "PROVED_HERE",
            witness=("continuation HOLDS (meromorphic on C, simple pole "
                     "at s = 1, via the deleted-factor identity and "
                     "import I1) — the FAILURE is the functional "
                     "equation.  " + zw + "  " + scope),
            citation=(hdlvp1896 + "; " + riemann1859 + "; " +
                      gamma_classical)),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("termwise character twist and local tensor calculus "
                     "act exactly on the class of finitely-deleted Euler "
                     "products.  " + twist_w + "  Local tensor "
                     "certificate at odd p: (1 - T) tensor (1 - T) = "
                     "1 - T, A6 HOLDS (exact); the deleted slot at 2 "
                     "tensors to a deleted slot"),
            citation=fe_import),
        "L8_REALIZATION": cell(
            "HOLDS", "PROVED_HERE",
            witness=("realized as a genuine arithmetic object: zeta_odd = "
                     "L(s, chi_0 mod 2), the Dirichlet L-function of the "
                     "PRINCIPAL character mod 2 — the identification "
                     "chi_0(n) = [gcd(n, 2) = 1] = a_n is definitional "
                     "and was verified coefficient-wise (L1 witness).  "
                     "The realization is IMPRIMITIVE: the primitive "
                     "character inducing chi_0 mod 2 is the trivial "
                     "character of conductor 1, whose L-function is zeta "
                     "itself; the FE lives on the primitive, not on "
                     "zeta_odd.  NOT in the Selberg class: zeta_odd "
                     "satisfies the Dirichlet-series, continuation and "
                     "Euler-product requirements but provably has no "
                     "reflection FE (L6) — the mirror image of "
                     "davenport_heilbronn, which fails only the "
                     "Euler-product axiom"),
            citation=selberg_cn),
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "FAILS", "PROVED_HERE",
            witness=("the explicit-formula PRIME SIDE survives (see "
                     "TRACE_FORMULA: nonnegative von Mangoldt "
                     "coefficients on odd prime powers, exact), but "
                     "PRINCIPLED POSITIVITY FAILS: any Weil-type "
                     "positivity criterion asserting that all non-real "
                     "zeros of zeta_odd in the closed strip lie on "
                     "Re s = 1/2 asserts a FALSEHOOD — exact witness the "
                     "zero family s_k = 2 pi i k / log 2 on Re s = 0 "
                     "(zeta finite there, import I1).  No positivity "
                     "mechanism targeting the critical line can exist "
                     "for this world"),
            citation=riemann1859),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("present, supplied by complete multiplicativity of "
                     "the principal character mod 2: product over the ODD "
                     "primes of (1 - p^{-s})^{-1}, verified coefficient-"
                     "wise to 512 (L2 witness).  One factor deleted — "
                     "the surgical difference from the 'zeta' row")),
        "DUALITY_FE": cell(
            "FAILS", "PROVED_HERE",
            witness=("absent, and PROVABLY unrestorable: the zero set of "
                     "zeta_odd is not s -> 1-s symmetric (exact witness "
                     "family s_k = 2 pi i k / log 2, zeros with non-zero "
                     "reflections — L6).  This is the isolated-mechanism "
                     "row: EULER PRODUCT WITHOUT DUALITY, the exact "
                     "converse of davenport_heilbronn (duality without "
                     "Euler product).  Deleting one local factor is the "
                     "minimal surgery that kills this mechanism while "
                     "leaving every local mechanism intact"),
            citation=hdlvp1896),
        "TRACE_FORMULA": cell(
            "HOLDS", "PROVED_HERE",
            witness=("an explicit-formula variant still exists: the "
                     "log-derivative is meromorphic and " + vm_witness +
                     "  The analytic explicit formula for zeta "
                     "(Riemann-von Mangoldt) transfers through "
                     "-zeta_odd'/zeta_odd = -zeta'/zeta - log 2 "
                     "sum_{k>=1} 2^{-ks}: the prime side loses the "
                     "powers of 2, the zero side gains the progression "
                     "{s_k} on Re s = 0.  The coefficient-level identity "
                     "is PROVED_HERE; the analytic formula for zeta is "
                     "imported"),
            citation=("B. Riemann (1859); H. von Mangoldt (1895), the "
                      "explicit formula for zeta (imported for the "
                      "analytic transfer only)")),
        "POSITIVITY_PURITY": cell(
            "FAILS", "PROVED_HERE",
            witness=("local purity is PRESENT (every odd-prime factor is "
                     "weight-0 pure with inverse root on |alpha| = 1, "
                     "exact — L4), yet NO global positivity mechanism can "
                     "exist: 'all non-real strip zeros on Re s = 1/2' is "
                     "FALSE by the exact zero s_1 = 2 pi i / log 2 on "
                     "Re s = 0.  MECHANISM LESSON: purity of local data "
                     "survives factor deletion; positivity does not — "
                     "positivity is a GLOBAL property mediated by the "
                     "duality/FE mechanism, and dies with it (compare "
                     "davenport_heilbronn: there duality survives and "
                     "positivity still dies for lack of an Euler "
                     "product; the two mechanisms are JOINTLY, not "
                     "separately, load-bearing)"),
            citation=riemann1859),
        "TENSOR_OPS": cell(
            "HOLDS", "PROVED_HERE",
            witness=("local twist/tensor calculus exists and is exact at "
                     "the odd primes (Satake {1}: tensor and sym^k are "
                     "trivial; A6 tensor certificate HOLDS), and the "
                     "termwise character twist acts on the class: twists "
                     "unramified at 2 reproduce one-factor deletions, "
                     "the 2-ramified twist by chi_{-4} REPAIRS the "
                     "defect and lands on the primitive L(s, chi_{-4}) "
                     "(exact to 512 — L7).  The deleted slot is inert "
                     "under all operations")),
        "FAMILY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("member of the explicit family of finite Euler "
                     "modifications of zeta — equivalently the "
                     "imprimitive principal-character L-functions "
                     "L(s, chi_0 mod q) = zeta(s) prod_{p | q} "
                     "(1 - p^{-s}).  The SAME exact argument applies to "
                     "every member: deleting the factor at p plants the "
                     "zero progression {2 pi i k / log p : k != 0} on "
                     "Re s = 0 whose reflections carry Euler-factor "
                     "value 1 - 1/p != 0 (verified exactly here for "
                     "p = 2, 3, 5: values 1/2, 2/3, 4/5).  An anti-rigid "
                     "family: every non-trivial member fails the FE its "
                     "primitive (zeta) satisfies — family membership "
                     "supplies structure but no rigidity"),
            citation=hdlvp1896),
    }

    critical_line = {
        "status": "FALSE",
        "detail": (
            "natural formulation: 'all nontrivial zeros of zeta_odd — its "
            "non-real zeros in the closed strip 0 <= Re s <= 1 — lie on "
            "Re s = 1/2'.  This is FALSE: s_1 = 2 pi i / log 2 is a "
            "non-real zero (exact: 2^{-s_1} = e^{-2 pi i} = 1, so the "
            "deleted factor vanishes; zeta is finite there, import I1) "
            "with Re s_1 = 0 != 1/2, and likewise the whole progression "
            "s_k, k != 0.  The zero set of zeta_odd is exactly "
            "{zeros of zeta} union {2 pi i k / log 2 : k in Z} (the k = 0 "
            "point is the extra real zero s = 0, since zeta(0) = -1/2 is "
            "finite and the factor vanishes); the surviving zeta-zeros "
            "are CONJECTURALLY on Re s = 1/2 (RH — open, not established "
            "here or anywhere; rh_established = false).  The counterfeit "
            "is perfect locally and fails only globally: every new zero "
            "sits on the group-theoretic line Re s = 0 of the deleted "
            "factor, not on the critical line"),
        "rigor": "PROVED_HERE",
        "citation": riemann1859 + "; " + hdlvp1896,
        "witness": (
            "exact witness s_1 = 2 pi i / log 2: 2^{-s_1} = 1 exactly "
            "(integer exponent check, import I4 only), Euler factor value "
            "1 - 1 = 0, zeta(s_1) finite (import I1) => zeta_odd(s_1) = "
            "0; Re s_1 = 0.  Verified for k in " + str(ZERO_FAMILY_K) +
            ".  Asymmetry pin (for L6, not needed for FALSE itself): "
            "zeta_odd(1 - s_1) = (1/2) zeta(1 - s_1) != 0 by import I2"),
    }

    world = {
        "id": "counterfeit_deleted_euler",
        "title": "2-deleted zeta (Euler product without duality)",
        "definition": (
            "zeta_odd(s) = sum_{n odd} n^{-s} = (1 - 2^{-s}) zeta(s) = "
            "prod_{p odd} (1 - p^{-s})^{-1} = L(s, chi_0 mod 2): the "
            "Riemann zeta function with its Euler factor at p = 2 "
            "deleted; coefficients a_n = [n odd], completely "
            "multiplicative.  Meromorphic on C with a single simple pole "
            "at s = 1 (residue 1/2).  Zero set = {zeros of zeta} union "
            "{2 pi i k / log 2 : k in Z} — the deleted factor plants an "
            "exact vertical arithmetic progression of zeros on Re s = 0, "
            "destroying the s -> 1-s symmetry of the zero set and with "
            "it every functional equation of standard reflection type"),
        "arithmetic_class": (
            "imprimitive degree-1 arithmetic L-function: the L-function "
            "of the principal Dirichlet character mod 2 (a one-factor "
            "Euler modification of zeta).  Possesses Euler product, "
            "complete multiplicativity, bounded-degree weight-0 "
            "self-dual local factors, twist/tensor calculus and an "
            "explicit-formula prime side — but provably NO duality/FE: "
            "the designed converse of the 'davenport_heilbronn' row"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "B. Riemann (1859), Ueber die Anzahl der Primzahlen unter "
            "einer gegebenen Groesse (continuation and pole of zeta)",
            "J. Hadamard (1896) and C.-J. de la Vallee Poussin (1896), "
            "proofs of the prime number theorem (zeta(1 + it) != 0 for "
            "real t != 0)",
            "L. Euler (1737), Euler product of zeta (classical context "
            "for the odd-primes product); Euler's identity e^{2 pi i} = "
            "1 (elementary import I4)",
            "H. Davenport, Multiplicative Number Theory (1967): "
            "imprimitive vs primitive Dirichlet L-functions and the "
            "odd-character functional equation (import I5, L7 note "
            "only)",
            "E. C. Titchmarsh, The Theory of the Riemann Zeta-Function "
            "(2nd ed., rev. D. R. Heath-Brown, 1986): standard "
            "reference for zeta facts imported here",
            "CITATION-NEEDED: A. Selberg (~1989-1992), Old and new "
            "conjectures and results about a class of Dirichlet series "
            "(the Selberg class, whose FE axiom zeta_odd fails)",
        ],
        "rh_established": False,
        "notes": (
            "ROLE IN THE MATRIX: the minimal counterfeit — delete ONE "
            "Euler factor from zeta and nothing local changes (complete "
            "multiplicativity, odd-primes Euler product, weight-0 "
            "self-dual degree-<=1 local factors, twist/tensor calculus, "
            "nonnegative von Mangoldt prime side: all verified exactly "
            "to n <= 512, plus full one-line proofs where available), "
            "yet duality dies PROVABLY: the deleted factor 1 - 2^{-s} "
            "plants the exact zero progression s_k = 2 pi i k / log 2 "
            "on Re s = 0 (2^{-s_k} = e^{-2 pi i k} = 1 exactly — log 2 "
            "appears only through this cancellation), while every "
            "reflected point 1 - s_k carries Euler-factor value 1/2 and "
            "a nonvanishing zeta value (zeta(1 + it) != 0, the ONLY "
            "deep import).  Hence no functional equation whose zero set "
            "would be s -> 1-s symmetric can hold — spelled out with "
            "precise scope in the L6 cell, including the Selberg-type "
            "strengthening (a finite product of gamma factors can "
            "excuse only finitely many of the infinitely many witness "
            "zeros).  Exact converse of davenport_heilbronn (duality "
            "without Euler product; zeros also stray there): together "
            "the two rows witness that EULER PRODUCT and DUALITY are "
            "jointly, not separately, load-bearing for critical-line "
            "phenomena.  Bonus exact structure: the 2-ramified twist by "
            "chi_{-4} repairs the defect exactly (lands on the "
            "primitive L(s, chi_{-4}), which has a genuine FE) — the "
            "disease is concentrated at the deleted prime.  The "
            "detector sees the deletion as a certified DEGREE-0 local "
            "factor at p = 2, not as any local pathology.  "
            "critical_line FALSE via the exact witness s_1 (Re = 0); "
            "the surviving zeta-zeros are conjecturally on 1/2 (RH, "
            "open).  No floats anywhere in this build.  "
            "rh_established=false."),
        "detector_runs": {
            "description": (
                "core.reconstruct.detect on exact 0/1 column data of "
                "zeta_odd: p = 3, 5 true columns (all-ones; degree 1, "
                "denominator 1 - T, weight-(p,0) purity and all axioms "
                "HOLD) and the p = 2 true column ([1,0,0,...]; certified "
                "degree-0 local factor — the deleted slot — with A4 "
                "purity vacuously SKIPPED).  Plus exact A6 tensor "
                "certificate (1 - T) tensor (1 - T) = 1 - T"),
            "runs": runs,
        },
    }
    return world


def main():
    CW, a = coefficient_layer()
    twist_w = twist_repair()
    vm_witness = von_mangoldt_prime_side()
    zw, scope = zero_symmetry_witness()
    loc_w, runs = local_structure()
    world = build_world(CW, a, twist_w, vm_witness, zw, scope, loc_w, runs)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector degrees:",
          [(r["prime"], r["verdict"]["object"]["degree"]) for r in runs])


if __name__ == "__main__":
    main()
