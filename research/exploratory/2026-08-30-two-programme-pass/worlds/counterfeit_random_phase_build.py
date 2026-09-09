"""World 'counterfeit_random_phase': a seeded completely multiplicative
counterfeit with unimodular real 'phases' eps_p in {+1, -1}.

    L(s) = sum_{n >= 1} a_n n^{-s},   a_n = prod_p eps_p^{v_p(n)}
         = prod_p (1 - eps_p p^{-s})^{-1}      (Re s > 1),

where the sign sequence (eps_p) is DETERMINISTIC:
  * for the 46 primes p <= 200, eps_p is the explicit hardcoded literal
    EPS_LITERAL below — FIXED ARBITRARILY AT BUILD TIME (a human-typed
    irregular pattern; no randomness at runtime, no generating rule);
  * for p > 200, eps_p = +1 if the binary digit sum of p is even, else -1
    (a closed-form deterministic tail).  DESIGN NOTE: the tail must NOT be
    eventually +1 — a tail identically +1 would make L(s) equal to zeta(s)
    times a FINITE product of rational Euler corrections, importing zeta's
    meromorphic continuation and collapsing this row into the
    'counterfeit_deleted_euler' family (finitely-modified zeta, where the
    FE failure is even PROVABLE).  The digit-parity tail keeps the object
    genuinely structureless as far as anyone knows: no continuation beyond
    Re s > 1 is known.

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.counterfeit_random_phase_build

regenerates worlds/counterfeit_random_phase.json identically.

ROLE IN THE MATRIX.  The cheap-to-counterfeit lower floors: L0-L4 (and the
formal layer of L7) come FOR FREE from complete multiplicativity of an
arbitrary sign table — degree-1 integral local factors 1 - eps_p T, all
inverse roots on |alpha| = 1 (weight-0 purity, exact), self-dual because the
signs are real.  Everything above (completion, FE, explicit formula,
positivity, family) is missing and OPEN.  The exact content of the row is a
FINITE EXCLUSION CERTIFICATE: eps is not the character pattern of ANY real
Dirichlet character of modulus q <= 50, even after arbitrary changes at the
ramified primes p | q.  MATRIX HEADLINE: the detector's LOCAL axiom battery
(A1-A5) returns all-HOLDS at every tested prime — verdicts indistinguishable
from a genuine Dirichlet-character world — so LOCAL tests cannot see the
missing global structure; purity and self-duality are local properties and
are exactly what a counterfeit fakes for free.

EXACT LAYER (integer / Fraction arithmetic only; no floats anywhere):
  1. THE EXCLUSION CERTIFICATE (PROVED_HERE, exhaustive).  For every modulus
     q <= 50, ALL real characters mod q are enumerated with an in-script
     completeness proof, twice, and the two enumerations are verified equal:
       (i)  abstract enumeration: real characters mod q = group
            homomorphisms U(q) -> {+-1}.  Any such kills squares
            (chi(u^2) = chi(u)^2 = 1) hence is +1 on the square subgroup S,
            and is determined by its values on a set generating U(q) over S
            (a greedy basis b_1..b_r with verified coset-doubling,
            span == U(q)); so there are AT MOST 2^r of them.  The script
            constructs 2^r candidates, verifies EACH is multiplicative on
            all of U(q) x U(q), and verifies they are pairwise distinct:
            the list is therefore complete.
       (ii) classical generation 'via Jacobi symbols': products of the
            Jacobi symbols u -> (u/m) over odd m | q (built from Legendre
            symbols via Euler's criterion) with the Kronecker 2-part
            characters chi_4, chi_8.  The set of functions so generated is
            asserted EQUAL to (i) for every q — re-proving the classical
            Gauss-Jacobi-Kronecker description of real characters in this
            range, with no imported classification theorem load-bearing.
     Then for every one of the enumerated characters chi mod q (principal
     included; q = 1 included), a prime p <= 200 with p NOT dividing q and
     eps_p != chi(p) is exhibited (ramified primes p | q are SKIPPED, so
     the certificate rules out coincidence even up to arbitrary changes of
     the Euler factors at p | q).  Totals and the worst-case minimal
     distinguishing prime are embedded in the record.
  2. a_n in {+1, -1} for ALL n (product of signs); COMPLETE multiplicativity
     a_{mn} = a_m a_n verified exhaustively for every pair m, n >= 2 with
     mn <= 512, on top of the one-line proof v_p(mn) = v_p(m) + v_p(n).
  3. Euler product: the truncated Dirichlet convolution of the local series
     (eps_p^k at p^k) over all primes p <= 512 reproduces (a_n)_{n<=512}
     exactly.  Local factors 1 - eps_p T: degree 1, integer, constant 1.
  4. Signed von Mangoldt identity (exact, symbolic): with
     Lambda_eps(p^k) = eps_p^k log p, the convolution identity
     sum_{d|n} Lambda_eps(d) a_{n/d} = a_n log n holds for all n <= 512 in
     the free Z-module on symbols {log p}.  The prime side of a would-be
     explicit formula exists formally but has SIGNED coefficients
     (Lambda(n) a_n; e.g. the coefficient at n = 3 is -log 3): even
     prime-side positivity fails, unlike zeta and the deleted-Euler row.
  5. Detector runs at p = 2, 3, 13, 197 (both signs represented): degree 1,
     denominator 1 - eps_p T, weight-(p,0) purity HOLDS (eps_p^2 = 1 = p^0),
     self-duality exact (op_dual_satake fixes [1, -eps_p]), A1-A5 all HOLD;
     exact A6 tensor certificates (1 - eps_p T) tensor (1 - eps_q T) =
     1 - eps_p eps_q T with all predicted coefficients verified.

WHAT IS *NOT* CLAIMED (honesty): no completion/FE is known and none is
expected; proving nonexistence is beyond this pass — the not-a-real-character
certificate rules out the standard completions with conductor <= 50, nothing
more.  Continuation beyond Re s = 1 is OPEN.  No family, no trace formula,
no positivity structure is known.  critical_line: NOT_FORMULATED (the
function is only known to exist on Re s > 1, where the absolutely convergent
Euler product makes it zero-free — elementary).  RH is not addressed;
rh_established = false.

IMPORTS (context only — no cell status rests on them):
  C1. P. G. L. Dirichlet (1837): Dirichlet characters and L-functions (the
      classical objects the certificate excludes at q <= 50).
  C2. J. Kaczorowski and A. Perelli (1999), classification of the Selberg
      class in degree 1: a degree-1 element with standard completion is
      (a shift of) a Dirichlet L-function of a primitive character — the
      reason 'standard completion with conductor <= 50' reduces to the
      not-a-real-character certificate.  Context for the L5/L6 notes only.
  C3. Elementary analysis: absolute convergence by comparison (|a_n| = 1)
      and nonvanishing of absolutely convergent products of nonzero factors.
  C4. A. O. Gelfond (~1968); C. Mauduit and J. Rivat (~2010): digit-sum
      equidistribution (context for why the digit-parity tail is believed
      not to be eventually any character pattern; NOT used in any cell).
"""

from fractions import Fraction
from itertools import product as iproduct
from math import gcd

from core.exact import F, op_dual_satake
from core.reconstruct import detect, tensor_compatibility, HOLDS
from core.worlds import cell, save_world, validate_world

N = 512                 # exact coefficient-wise verification range
P_MAX = 200             # the hardcoded sign table covers primes <= P_MAX
Q_MAX = 50              # exclusion certificate covers all moduli q <= Q_MAX
DETECTOR_WINDOW = 12    # detector window (a_{p^0} .. a_{p^11})
HOLDOUT = 4             # detector holdout
DETECTOR_PRIMES = (2, 3, 13, 197)   # both signs represented (see literal)

# ---------------------------------------------------------------------------
# THE SEED.  Hardcoded literal sign table for the 46 primes p <= 200.
# FIXED ARBITRARILY AT BUILD TIME: an irregular human-typed +-1 pattern, not
# produced by any rule, formula, or random generator; there is NO runtime
# randomness — rerunning the script uses these exact literals.  The
# exclusion certificate below PROVES this pattern is not that of any real
# Dirichlet character mod q <= 50 (off the ramified primes).
# ---------------------------------------------------------------------------
EPS_LITERAL = {
      2: +1,   3: -1,   5: -1,   7: +1,  11: -1,  13: +1,  17: +1,  19: -1,
     23: -1,  29: +1,  31: -1,  37: -1,  41: +1,  43: -1,  47: +1,  53: +1,
     59: -1,  61: +1,  67: -1,  71: +1,  73: -1,  79: -1,  83: +1,  89: +1,
     97: -1, 101: +1, 103: -1, 107: +1, 109: -1, 113: -1, 127: +1, 131: -1,
    137: +1, 139: +1, 149: -1, 151: +1, 157: -1, 163: +1, 167: -1, 173: +1,
    179: -1, 181: -1, 191: +1, 193: -1, 197: -1, 199: +1,
}


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


def eps_table():
    """Full sign table for all primes p <= N: the hardcoded literal on
    p <= 200, the deterministic binary-digit-parity rule above 200."""
    ps = primes_upto(N)
    small = [p for p in ps if p <= P_MAX]
    assert sorted(EPS_LITERAL) == small          # literal covers EXACTLY p<=200
    assert len(EPS_LITERAL) == 46
    assert all(v in (1, -1) for v in EPS_LITERAL.values())
    eps = dict(EPS_LITERAL)
    for p in ps:
        if p > P_MAX:
            # deterministic closed-form tail: parity of the binary digit sum
            eps[p] = 1 if bin(p).count("1") % 2 == 0 else -1
    return eps


# ---------------------------------------------------------------------------
# Step A: THE EXCLUSION CERTIFICATE — exhaustive real-character enumeration
# for every q <= 50, proven complete in-script, plus the Jacobi cross-check
# ---------------------------------------------------------------------------

def real_characters_mod(q):
    """Return (U, chars): U = units mod q (sorted), chars = ALL group
    homomorphisms U -> {+-1} as dicts u -> chi(u).

    COMPLETENESS PROOF (runs inside this function):
      * S = {u^2 mod q} is verified to be a subgroup; any homomorphism
        f: U -> {+-1} has f(u^2) = f(u)^2 = 1, so f == +1 on S.
      * A greedy basis b_1..b_r is built with verified coset-doubling
        (each step: the coset span*b is disjoint from span and of equal
        size) until span == U.  Hence S together with b_1..b_r generates
        U, so f is determined by (f(b_1), ..., f(b_r)): AT MOST 2^r
        homomorphisms exist.
      * The 2^r candidates are constructed, EACH verified multiplicative
        on all of U x U with chi(1) = 1, and verified pairwise distinct.
        2^r distinct verified homomorphisms + at most 2^r possible
        => the enumeration is complete.  PROVED_HERE, no imports."""
    assert q >= 2
    U = [u for u in range(1, q) if gcd(u, q) == 1]
    Uset = set(U)
    for u in U:                              # sanity: U is closed under *
        for v in U:
            assert (u * v) % q in Uset
    S = {(u * u) % q for u in U}
    for x in S:                              # S is a subgroup
        for y in S:
            assert (x * y) % q in S
    assert 1 in S
    span, basis = set(S), []
    while span != Uset:
        u = min(x for x in U if x not in span)      # deterministic choice
        coset = {(x * u) % q for x in span}
        assert coset.isdisjoint(span) and len(coset) == len(span)
        span |= coset
        basis.append(u)
    r = len(basis)
    assert len(U) == len(S) * 2 ** r
    chars, seen = [], set()
    for signs in iproduct((1, -1), repeat=r):
        chi = {s: 1 for s in S}
        for b, t in zip(basis, signs):
            add = {}
            for x, v in list(chi.items()):
                key = (x * b) % q
                assert key not in chi and key not in add
                add[key] = v * t
            chi.update(add)
        assert set(chi) == Uset
        for u in U:                          # THE load-bearing verification
            for v in U:
                assert chi[(u * v) % q] == chi[u] * chi[v]
        assert chi[1] == 1
        tup = tuple(chi[u] for u in U)
        assert tup not in seen
        seen.add(tup)
        chars.append(chi)
    assert len(chars) == 2 ** r
    return U, chars


def legendre(n, p):
    """Legendre symbol (n/p), p an odd prime, p not dividing n, computed by
    Euler's criterion with exact modular integer arithmetic.  Correctness of
    the classical criterion is NOT load-bearing: every function built from
    this is verified against the abstract enumeration by set equality."""
    assert p % 2 == 1 and n % p != 0
    t = pow(n, (p - 1) // 2, p)
    assert t in (1, p - 1)
    return 1 if t == 1 else -1


def jacobi_symbol(n, m):
    """Jacobi symbol (n/m) for odd m >= 1 with gcd(n, m) = 1, as the product
    of Legendre symbols over the prime factorization of m (the definition)."""
    v = 1
    for p, e in factorize(m).items():
        v *= legendre(n, p) ** e
    return v


def jacobi_generated_set(q, U):
    """The classical generation of real characters mod q 'via Jacobi
    symbols': all products of  u -> (u/m)  for odd m | q  (equivalently,
    subsets of Legendre symbols at the odd primes dividing q) with the
    Kronecker 2-part characters chi_4 (u -> +-1 by u mod 4) and chi_8
    (u -> +-1 by u mod 8), the 2-part options depending on v_2(q).
    Returns the set of value-tuples on U."""
    fac = factorize(q)
    e2 = fac.get(2, 0)
    odd_ps = sorted(p for p in fac if p != 2)
    if e2 >= 3:
        two_parts = ((0, 0), (1, 0), (0, 1), (1, 1))
    elif e2 == 2:
        two_parts = ((0, 0), (1, 0))
    else:
        two_parts = ((0, 0),)
    out = set()
    for use4, use8 in two_parts:
        for mask in iproduct((0, 1), repeat=len(odd_ps)):
            m = 1
            for p, on in zip(odd_ps, mask):
                if on:
                    m *= p
            vals = []
            for u in U:
                v = 1
                if use4:                     # chi_4: +1 iff u = 1 mod 4
                    v *= 1 if u % 4 == 1 else -1
                if use8:                     # chi_8: +1 iff u = +-1 mod 8
                    v *= 1 if u % 8 in (1, 7) else -1
                if m > 1:
                    v *= jacobi_symbol(u, m)
                vals.append(v)
            out.add(tuple(vals))
    return out


def exclusion_certificate(eps):
    """For EVERY modulus q <= Q_MAX and EVERY real character chi mod q,
    exhibit a prime p <= P_MAX with p not dividing q and eps_p != chi(p).
    Ramified primes p | q are SKIPPED, so the certificate holds even up to
    arbitrary modification of the Euler factors at p | q.  Also cross-checks
    the abstract enumeration against the Jacobi/Kronecker generation."""
    p200 = primes_upto(P_MAX)
    total = 0
    worst = (0, 0)                           # (distinguishing prime, its q)
    per_q = []
    for q in range(1, Q_MAX + 1):
        if q == 1:
            # the unique character mod 1 is chi(n) = 1 for all n
            U, chars = [], [None]
        else:
            U, chars = real_characters_mod(q)
            aset = {tuple(chi[u] for u in U) for chi in chars}
            jset = jacobi_generated_set(q, U)
            # BOTH directions verified: every Jacobi/Kronecker product is a
            # real character, and the classical generation is exhaustive.
            assert aset == jset, q
        for chi in chars:
            found = None
            for p in p200:
                if q % p == 0:               # ramified prime: SKIP
                    continue
                cp = 1 if chi is None else chi[p % q]
                assert cp in (1, -1)
                if eps[p] != cp:
                    found = p
                    break
            assert found is not None, (q, chi)   # THE certificate
            if found > worst[0]:
                worst = (found, q)
            total += 1
        per_q.append((q, len(chars)))
    assert total == sum(c for _, c in per_q)
    return total, worst, per_q


# ---------------------------------------------------------------------------
# Step B: coefficient layer — a_n = prod eps_p^{v_p(n)}, all checks exact
# ---------------------------------------------------------------------------

def coefficient_layer(eps):
    """Exact verifications: unimodularity, COMPLETE multiplicativity
    (exhaustive), and the Euler product coefficient-wise to N."""
    W = {}
    a = [0] * (N + 1)
    a[1] = 1
    for n in range(2, N + 1):
        v = 1
        for p, e in factorize(n).items():
            v *= eps[p] ** e
        a[n] = v
    assert all(a[n] in (1, -1) for n in range(1, N + 1))
    W["unimodular"] = (
        f"a_n in {{+1, -1}} for ALL n <= {N} (verified; trivially true for "
        "all n: a finite product of signs) — unimodular real 'phases', "
        "|a_n| = 1, so the Dirichlet series converges absolutely for "
        "Re s > 1 by comparison with zeta (elementary)")

    pairs = 0
    for m in range(2, N + 1):
        for n in range(2, N // m + 1):
            assert a[m * n] == a[m] * a[n], (m, n)
            pairs += 1
    assert pairs == sum(max(N // m - 1, 0) for m in range(2, N + 1))
    W["multiplicativity"] = (
        "COMPLETE multiplicativity a_{mn} = a_m a_n verified exactly for "
        f"all {pairs} pairs m, n >= 2 with mn <= {N}.  Full one-line proof, "
        "valid for ALL m, n: a_n = prod_p eps_p^{v_p(n)} and "
        "v_p(mn) = v_p(m) + v_p(n); the exhaustive check corroborates it")

    E = [0] * (N + 1)
    E[1] = 1
    for p in primes_upto(N):
        local = [0] * (N + 1)
        pk, v = 1, 1
        while pk <= N:                       # local series: eps_p^k at p^k,
            local[pk] = v                    # i.e. 1/(1 - eps_p p^{-s})
            pk *= p
            v *= eps[p]
        E = dirichlet_conv(E, local, N)
    assert E[1:] == a[1:]
    W["euler_product"] = (
        "Euler product verified coefficient-wise for ALL n <= "
        f"{N}: the truncated Dirichlet convolution of the local geometric "
        "series (a_{p^k} = eps_p^k, local factor 1/(1 - eps_p p^{-s})) over "
        f"all {len(primes_upto(N))} primes p <= {N} reproduces a_n exactly. "
        " Formally the product also follows from complete multiplicativity "
        "plus |a_n| = 1")
    return W, a


def von_mangoldt_prime_side(eps, a):
    """Exact identity in the free Z-module on symbols {log p}:
    sum_{d | n} Lambda_eps(d) a_{n/d} = a_n log n for all n <= N, with
    Lambda_eps(p^k) = eps_p^k log p.  So -L'/L = sum Lambda(n) a_n n^{-s}
    formally — the prime side exists but its coefficients are SIGNED."""
    for n in range(1, N + 1):
        fac = factorize(n)
        rhs = {p: a[n] * e for p, e in fac.items()} if n > 1 else {}
        lhs = {}
        for p, e in fac.items():
            pk, s = 1, 0
            for k in range(1, e + 1):        # divisors d = p, p^2, ..., p^e
                pk *= p
                s += (eps[p] ** k) * a[n // pk]
            if s:
                lhs[p] = s
        assert lhs == rhs, (n, lhs, rhs)
    # exact witness of FAILED prime-side positivity: coefficient at n = 3
    assert a[3] == EPS_LITERAL[3] == -1
    neg = sum(1 for n in range(2, N + 1)
              if len(factorize(n)) == 1
              and a[n] == -1)                # prime powers with sign -1
    return (
        "SIGNED VON MANGOLDT IDENTITY (exact, symbolic): with Lambda_eps "
        "supported on prime powers (Lambda_eps(p^k) = eps_p^k log p), the "
        "convolution identity sum_{d|n} Lambda_eps(d) a_{n/d} = a_n log n "
        f"was verified for ALL n <= {N} as an identity in the free Z-module "
        "on the symbols {log p} (no floating-point logarithm anywhere).  "
        "Hence -L'/L(s) = sum_n Lambda(n) a_n n^{-s} as formal Dirichlet "
        "series: a prime side EXISTS formally, but its coefficients "
        "Lambda(n) a_n are SIGNED — exact witness: the coefficient at "
        f"n = 3 is a_3 log 3 = -log 3 < 0; among the prime powers n <= {N} "
        f"exactly {neg} carry a negative coefficient.  Even prime-side "
        "positivity (which held for zeta and for the deleted-Euler "
        "counterfeit) fails here; and with no known continuation there is "
        "no zero side at all")


# ---------------------------------------------------------------------------
# Step C: local structure — detector runs and exact tensor certificates
# ---------------------------------------------------------------------------

def local_structure(eps):
    """Detector certificates at DETECTOR_PRIMES (both signs occur): every
    local factor is degree 1, integral, weight-0 pure, self-dual, with
    perfect held-out prediction — all-HOLDS verdicts indistinguishable from
    a genuine Dirichlet-character world.  THE MATRIX HEADLINE: local tests
    cannot see the missing global structure."""
    runs = []
    for p in DETECTOR_PRIMES:
        e = eps[p]
        col = [F(e ** k) for k in range(DETECTOR_WINDOW)]   # a_{p^k} = eps^k
        d = detect(col, mode="coefficients", weight=(p, 0),
                   holdout=HOLDOUT).as_dict()
        assert d["refusal"] is None, d
        assert d["object"]["degree"] == 1
        assert d["object"]["denominator"] == ("[1, -1]" if e == 1
                                              else "[1, 1]")
        got = {x["axiom"]: x["status"] for x in d["cells"]}
        assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                       "A3_INTEGRALITY": HOLDS, "A4_PURITY": HOLDS,
                       "A5_HELD_OUT": HOLDS}, got
        runs.append({"prime": p, "eps": e, "weight": [p, 0],
                     "mode": "coefficients",
                     "series": f"true column (a_{{{p}^k}}) = eps_{p}^k, "
                               f"window {DETECTOR_WINDOW}",
                     "verdict": d})

    # exact self-duality of both local factors: dual of 1 - e T is itself
    for e in (1, -1):
        sat = [F(1), F(-e)]
        assert op_dual_satake(sat, F(e)) == sat
        assert F(e) ** 2 == F(1)             # weight-0 purity: alpha^2 = p^0

    # exact A6 tensor certificates: (1 - e1 T) tensor (1 - e2 T) =
    # 1 - e1 e2 T, with all predicted product coefficients verified.
    # Certifies that the local twist/tensor calculus is the termwise sign
    # product — the class of counterfeits is closed under it.
    tc_same = tensor_compatibility([F(1), F(1)], [F(1), F(1)],
                                   [F(1)] * 8)          # (-1)x(-1) -> +1
    assert tc_same["status"] == HOLDS, tc_same
    tc_cross = tensor_compatibility([F(1), F(-1)], [F(1), F(1)],
                                    [F((-1) ** k) for k in range(8)])
    assert tc_cross["status"] == HOLDS, tc_cross

    witness = (
        "LOCAL STRUCTURE (exact).  Every local factor is 1 - eps_p T: "
        "degree 1, integer coefficients, constant term 1, inverse root "
        "alpha = eps_p with alpha^2 = 1 = p^0 (weight-0 purity, exact) and "
        "op_dual_satake([1, -eps_p], eps_p) == [1, -eps_p] (self-dual, "
        "exact, both signs).  Detector certificates at p = "
        f"{DETECTOR_PRIMES} (signs {tuple(eps[p] for p in DETECTOR_PRIMES)})"
        ": degree 1, denominator 1 -+ T, ALL FIVE axioms HOLD including "
        "A4 purity at weight (p, 0) and A5 held-out prediction.  Tensor "
        "certificates (A6, exact): (1 - eps T) tensor (1 - eps' T) = "
        "1 - eps eps' T, verified for the same-sign and cross-sign pairs "
        "with all predicted coefficients checked.  Uniform degree bound 1")
    return witness, runs


# ---------------------------------------------------------------------------
# The world record
# ---------------------------------------------------------------------------

MANDATED_HONESTY_NOTE = (
    "no completion/FE is known and none is expected; proving nonexistence "
    "is beyond this pass — the not-a-real-character certificate rules out "
    "the standard completions with conductor <= 50")


def build_world(CW, vm_witness, loc_w, runs, total, worst, per_q, eps_fp):
    dirichlet_ctx = ("P. G. L. Dirichlet (1837), Dirichlet characters and "
                     "L-functions (the classical objects excluded by the "
                     "certificate at modulus <= 50; context C1)")
    kp_ctx = ("J. Kaczorowski and A. Perelli (1999), classification of the "
              "Selberg class in degree 1 (a degree-1 element with standard "
              "completion is a shifted Dirichlet L-function of a primitive "
              "character) — context C2 for the scope of 'standard "
              "completions with conductor <= 50'; no cell status rests on it")
    selberg_cn = ("CITATION-NEEDED: A. Selberg (~1989-1992), Old and new "
                  "conjectures ... (definition of the Selberg class; "
                  "context only for which completions the finite "
                  "certificate excludes)")

    cert_witness = (
        "EXCLUSION CERTIFICATE (exhaustive, PROVED_HERE).  Sign table "
        f"fingerprint over the 46 primes 2, 3, ..., 199 in order: {eps_fp} "
        "(hardcoded literal, fixed arbitrarily at build time; deterministic "
        "digit-parity tail for p > 200).  For EVERY modulus q <= 50 and "
        f"EVERY real character chi mod q ({total} characters in total, "
        "principal characters and q = 1 included; per-q counts "
        + ";".join(f"{q}:{c}" for q, c in per_q) + ") there is a prime "
        "p <= 200 with p NOT dividing q and eps_p != chi(p); ramified "
        "primes p | q are skipped, so the certificate holds even after "
        "arbitrary modification of the Euler factors at p | q.  Worst case: "
        f"the largest minimal distinguishing prime over all {total} "
        f"characters is p = {worst[0]} (attained at modulus q = {worst[1]});"
        " every other character is distinguished by a smaller prime.  The "
        "character enumeration is proven complete IN-SCRIPT two independent "
        "ways, verified equal for every q: (i) abstract Hom(U(q), {+-1}) "
        "enumeration — any homomorphism is +1 on the square subgroup and "
        "determined on a verified generating set, giving at most 2^r; 2^r "
        "distinct candidates are constructed and each verified "
        "multiplicative on all of U x U; (ii) the classical generation via "
        "Jacobi symbols (products of (u/m) for odd m | q, built from "
        "Legendre symbols by Euler's criterion) times the Kronecker 2-part "
        "characters chi_4, chi_8 — asserted set-equal to (i), so the "
        "classical description of real characters is itself re-proved on "
        "this range rather than imported")

    headline = (
        "MATRIX HEADLINE: LOCAL TESTS CANNOT SEE THE MISSING GLOBAL "
        "STRUCTURE.  At every tested prime the detector certifies a "
        "degree-1, integral, weight-0-PURE, SELF-DUAL local factor with "
        "perfect held-out prediction (A1-A5 all HOLD) — verdicts "
        "indistinguishable from the genuine dirichlet_mod5 row — while the "
        "global object is certified NOT to be any real Dirichlet character "
        "of modulus <= 50.  Purity and self-duality are LOCAL properties, "
        "and are exactly what an arbitrary sign table counterfeits for "
        "free; only global structure (completion/FE, family, positivity) "
        "separates the real thing from the counterfeit, and every global "
        "floor is OPEN here")

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=("L(s) = sum a_n n^{-s} with a_n = prod_p "
                     "eps_p^{v_p(n)}: fully specified by the explicit "
                     "deterministic sign table (hardcoded literal "
                     f"{eps_fp} on the primes <= 200 in order, fixed "
                     "arbitrarily at build time; digit-parity tail for "
                     "p > 200 — a tail of all +1 would collapse the world "
                     "into a finitely-modified zeta, see notes).  " +
                     CW["unimodular"] + ".  Known domain: Re s > 1 only")),
        "L1_MULTIPLICATIVITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=CW["multiplicativity"]),
        "L2_EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=CW["euler_product"]),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "HOLDS", "PROVED_HERE",
            witness=("uniform degree bound 1: L_p(T) = 1 - eps_p T at "
                     "every prime — integer coefficients, constant term "
                     "1.  " + loc_w)),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("trivially HOLDS because the coefficients are real "
                     "signs: every local factor is exactly self-dual "
                     "(op_dual_satake([1, -eps_p], eps_p) == [1, -eps_p], "
                     "verified for both signs) and weight-0 pure "
                     "(eps_p^2 = 1 = p^0, exact).  NOTE: this self-duality "
                     "is a property of the coefficient FIELD, obtained for "
                     "free by any real sign table; it carries no "
                     "functional-equation content whatsoever (L6 is OPEN). "
                     " The cheapest floor of the ladder to counterfeit")),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "OPEN", "OPEN",
            witness=("no canonical (conductor, gamma, root number) datum "
                     "is known for this object; " + MANDATED_HONESTY_NOTE +
                     ".  That finite certificate is the exact content of "
                     "this cell: " + cert_witness),
            citation=kp_ctx),
        "L6_CONTINUATION_FE": cell(
            "OPEN", "OPEN",
            witness=("BOTH halves are open: no analytic continuation "
                     "beyond Re s = 1 is known (contrast "
                     "counterfeit_deleted_euler, where continuation HOLDS "
                     "and the FE provably FAILS — here nothing is even "
                     "known to continue), and " + MANDATED_HONESTY_NOTE +
                     ".  Conditional remark (not used): square-root "
                     "cancellation of the partial sums of a_n would extend "
                     "convergence to Re s > 1/2 — CONJECTURAL, a "
                     "random-phase heuristic, claimed nowhere"),
            citation=kp_ctx),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("at the FORMAL/LOCAL level only, and exactly: the "
                     "class of completely multiplicative sign sequences is "
                     "closed under termwise product (twist by any real "
                     "character or by another counterfeit), with local "
                     "rule (1 - eps_p T) tensor (1 - eps'_p T) = "
                     "1 - eps_p eps'_p T — certified by the exact A6 "
                     "tensor checks (same-sign and cross-sign, all "
                     "predicted coefficients verified).  SCOPE: no "
                     "analytic content — with no completions in sight, "
                     "the analytic half of L7 (root numbers, conductors "
                     "under twist) is not even formulable")),
        "L8_REALIZATION": cell(
            "HOLDS", "SYNTHETIC_CONTROL",
            witness=("realized ONLY as an explicit combinatorial/synthetic "
                     "object: the hardcoded 46-sign literal plus the "
                     "deterministic digit-parity tail, extended "
                     "multiplicatively.  That is a complete combinatorial "
                     "realization (this world is a designed synthetic "
                     "control), but it supplies no automorphic, motivic, "
                     "spectral or dynamical structure.  The exclusion "
                     "certificate PROVES it is not the pattern of any real "
                     "Dirichlet character of modulus <= 50 (even off the "
                     "ramified primes); whether some classical realization "
                     "of larger conductor exists is OPEN — believed none "
                     "(the digit-parity tail is believed incompatible with "
                     "any eventual periodicity in p; Gelfond/Mauduit-Rivat "
                     "context C4, not relied upon)"),
            citation=dirichlet_ctx),
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "OPEN", "OPEN",
            witness=("no principled explicit formula is known: the prime "
                     "side exists formally but with SIGNED coefficients "
                     "(exact witness: Lambda(3) a_3 = -log 3 < 0 — see "
                     "TRACE_FORMULA), and there is no zero side at all "
                     "absent continuation.  Weil-type positivity cannot "
                     "even be formulated (no zero set is defined).  " +
                     MANDATED_HONESTY_NOTE)),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("present, supplied by COMPLETE MULTIPLICATIVITY BY "
                     "CONSTRUCTION (the object is defined as a "
                     "multiplicative extension of prime signs): product of "
                     "(1 - eps_p p^{-s})^{-1} over all p, verified "
                     "coefficient-wise to 512 (L2 witness).  The mechanism "
                     "is real but structurally EMPTY here: it constrains "
                     "nothing beyond what the sign table dictates — an "
                     "Euler product alone is cheap")),
        "DUALITY_FE": cell(
            "OPEN", "OPEN",
            witness=("none known; " + MANDATED_HONESTY_NOTE + ".  The "
                     "finite exclusion certificate is the exact content: "
                     + cert_witness),
            citation=kp_ctx),
        "TRACE_FORMULA": cell(
            "OPEN", "OPEN",
            witness=("no trace formula or explicit formula is known.  "
                     "What exists is only the formal identity: " +
                     vm_witness)),
        "POSITIVITY_PURITY": cell(
            "OPEN", "OPEN",
            witness=("LOCAL purity is exactly present — every inverse "
                     "root is eps_p with |eps_p|^2 = 1 = p^0 (weight-0 "
                     "purity, exact at every prime) — but it is supplied "
                     "by nothing: the signs are an arbitrary table, not "
                     "Frobenius weights or adjacency self-adjointness.  "
                     "No global positivity statement is known or even "
                     "formulable (no zero set); prime-side positivity "
                     "FAILS exactly (coefficient -log 3 at n = 3).  "
                     "MECHANISM LESSON: weight-0 purity of degree-1 local "
                     "data is a vacuous constraint — any sign table has "
                     "it; purity begins to bite only with degree >= 2 or "
                     "weight > 0, where it forces real algebraic "
                     "relations")),
        "TENSOR_OPS": cell(
            "HOLDS", "PROVED_HERE",
            witness=("exact local twist/tensor calculus: termwise sign "
                     "product, (1 - eps T) tensor (1 - eps' T) = "
                     "1 - eps eps' T, A6 certificates HOLD (same-sign and "
                     "cross-sign).  The class of counterfeits is CLOSED "
                     "under tensor/twist — the operations exist but "
                     "never leave the counterfeit class, so they detect "
                     "nothing (L7 witness has the scope caveat)")),
        "FAMILY": cell(
            "OPEN", "OPEN",
            witness=("no structural family is known (FAILS-like in "
                     "spirit; recorded OPEN because nonexistence of any "
                     "good family is not provable here).  The ambient "
                     "2^46-cube of sign tables is a CONTAINER, not a "
                     "family: no conductor/weight parameter, no completed "
                     "members, no orthogonality or averaging structure, "
                     "no trace-formula linkage — contrast the "
                     "dirichlet_mod5 row (character orthogonality) and "
                     "the ihara rows (spectral families)")),
    }

    critical_line = {
        "status": "NOT_FORMULATED",
        "detail": (
            "the function is only known to exist on Re s > 1 (absolute "
            "convergence, |a_n| = 1), where the absolutely convergent "
            "Euler product of nonzero factors makes it ZERO-FREE "
            "(elementary: |eps_p p^{-s}| = p^{-Re s} < 1, and an "
            "absolutely convergent product of nonzero factors is nonzero "
            "— context C3).  With no known continuation there is no strip, "
            "no zero set, and no line: 'critical line' cannot be "
            "formulated for this object.  The exclusion certificate rules "
            "out the standard route to a formulation (a hidden classical "
            "completion) for conductor <= 50.  RH is not addressed; "
            "rh_established = false"),
        "rigor": "OPEN",
        "citation": "",
        "witness": "",
    }

    world = {
        "id": "counterfeit_random_phase",
        "title": "seeded random-phase counterfeit",
        "definition": (
            "L(s) = sum_{n>=1} a_n n^{-s} = prod_p (1 - eps_p p^{-s})^{-1} "
            "(Re s > 1), a_n = prod_p eps_p^{v_p(n)} in {+1, -1}, where "
            "eps_p is DETERMINISTIC: the hardcoded literal sign table " +
            eps_fp + " on the 46 primes 2, 3, 5, ..., 199 (in increasing "
            "order; fixed arbitrarily at build time, no runtime "
            "randomness), and eps_p = (-1)^{binary digit sum of p} for "
            "p > 200 (deterministic closed-form tail; an all-+1 tail is "
            "deliberately avoided, see notes).  A completely "
            "multiplicative unimodular counterfeit: all local floors of "
            "the ladder hold exactly, all global floors are OPEN, and an "
            "exact finite certificate shows it is not a disguised real "
            "Dirichlet character of modulus <= 50"),
        "arithmetic_class": (
            "synthetic degree-1 counterfeit (random-phase model): a "
            "completely multiplicative +-1 sequence with no known analytic "
            "continuation, completion, or realization beyond its own "
            "defining table; certified not induced by any real Dirichlet "
            "character of modulus <= 50, even up to changing the Euler "
            "factors at ramified primes"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "P. G. L. Dirichlet (1837), Dirichlet characters and "
            "L-functions (the classical comparison class for the "
            "exclusion certificate)",
            "C. F. Gauss (1801), Disquisitiones Arithmeticae (quadratic "
            "residues); C. G. J. Jacobi (1837), the Jacobi symbol — "
            "classical generation of real characters, used as the "
            "cross-check enumeration and re-proved in-script by set "
            "equality for every q <= 50",
            "J. Kaczorowski and A. Perelli (1999), classification of the "
            "Selberg class in degree 1 (context for 'standard completions "
            "with conductor <= 50'; no cell status rests on it)",
            "H. Davenport, Multiplicative Number Theory (1967): standard "
            "reference for real/quadratic Dirichlet characters",
            "A. O. Gelfond (~1968) and C. Mauduit and J. Rivat (~2010), "
            "digit-sum equidistribution results (context only for the "
            "digit-parity tail; no cell relies on them)",
            "CITATION-NEEDED: A. Selberg (~1989-1992), Old and new "
            "conjectures and results about a class of Dirichlet series "
            "(the Selberg class; context only)",
        ],
        "rh_established": False,
        "notes": (
            "ROLE IN THE MATRIX: the cheap-to-counterfeit lower floors.  "
            "An ARBITRARY hardcoded sign table, extended multiplicatively, "
            "buys L0-L4 and the formal layer of L7 EXACTLY (complete "
            "multiplicativity, Euler product coefficient-wise to 512, "
            "degree-1 integral local factors, weight-0 purity and "
            "self-duality at every prime, closed twist/tensor calculus) — "
            "while every global floor (completion, conductor/gamma/root, "
            "FE, explicit formula, positivity, family) is OPEN, and the "
            "exact finite certificate shows the object is not a disguised "
            "classical character at any modulus <= 50 (all "
            + str(total) +
            " real characters excluded by a prime <= " + str(worst[0]) +
            ", ramified primes skipped).  " + headline + ".  DESIGN NOTE "
            "(tail): eps_p for p > 200 is the digit-parity rule, NOT +1 — "
            "an eventually-+1 tail would make L(s) = zeta(s) times a "
            "finite rational Euler correction, importing zeta's "
            "continuation and collapsing this row into the "
            "counterfeit_deleted_euler family (finitely-modified zeta, "
            "provable FE failure); the point of THIS row is the object "
            "with NO known global analytic structure at all.  CONTRAST "
            "WITHIN THE COUNTERFEIT BAND: deleted_euler = continuation "
            "HOLDS + FE provably FAILS; random_phase = everything global "
            "honestly OPEN; both have perfect local floors.  Prime-side "
            "positivity fails here exactly (signed von Mangoldt "
            "coefficients, e.g. -log 3 at n = 3) — even the arithmetic "
            "half of an explicit formula degrades.  No floats anywhere in "
            "this build; every HOLDS/FAILS cell is exact.  "
            "rh_established=false."),
        "detector_runs": {
            "description": (
                "core.reconstruct.detect on the exact local columns "
                "a_{p^k} = eps_p^k at p = " + str(DETECTOR_PRIMES) +
                " (both signs represented), weight claim (p, 0): every "
                "run certifies degree 1, denominator 1 -+ T, and ALL "
                "FIVE axioms HOLD — including A4 purity — plus exact A6 "
                "tensor certificates.  The instructive point (matrix "
                "headline): these verdicts are indistinguishable from a "
                "genuine Dirichlet-character world; local tests cannot "
                "see the missing global structure"),
            "runs": runs,
        },
    }
    return world


def main():
    eps = eps_table()
    eps_fp = "".join("+" if EPS_LITERAL[p] == 1 else "-"
                     for p in primes_upto(P_MAX))
    # Step A: the exhaustive exclusion certificate (the exact headline)
    total, worst, per_q = exclusion_certificate(eps)
    # Step B: coefficient layer + signed von Mangoldt identity
    CW, a = coefficient_layer(eps)
    vm_witness = von_mangoldt_prime_side(eps, a)
    # Step C: local structure, detector runs, tensor certificates
    loc_w, runs = local_structure(eps)
    world = build_world(CW, vm_witness, loc_w, runs, total, worst, per_q,
                        eps_fp)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("exclusion certificate: %d real characters over q <= %d, worst "
          "minimal distinguishing prime %d at q = %d"
          % (total, Q_MAX, worst[0], worst[1]))
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("detector:", [(r["prime"], r["eps"],
                         r["verdict"]["object"]["denominator"]) for r in runs])


if __name__ == "__main__":
    main()
