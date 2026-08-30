"""World 'davenport_heilbronn': the classical Davenport-Heilbronn function —
a Dirichlet series with a self-dual functional equation but NO Euler product,
and with zeros off the critical line (imported).  The complement row to
'beurling' (which has an Euler product but no duality).

Deterministic build script (no input, no randomness).  Run from pass root:

    python3 -m worlds.davenport_heilbronn_build

regenerates worlds/davenport_heilbronn.json identically.

DEFINITION.  f(s) = 5^{-s} ( zeta(s,1/5) + kappa zeta(s,2/5)
                             - kappa zeta(s,3/5) - zeta(s,4/5) ),
kappa = tan(theta) the unique real constant making f satisfy the SAME
self-dual functional equation as an odd character of conductor 5.  The
constant is NOT taken from the literature: it is DERIVED from scratch below
by exact arithmetic in the cyclotomic field K = Q(zeta_20), realized as
Q[x] / Phi_20(x) with Phi_20 = x^8 - x^6 + x^4 - x^2 + 1 and Fraction
coefficients.  Every step is an exact assertion:

  1. Unfolding 5^{-s} zeta(s, a/5) = sum_{n = a mod 5} n^{-s} (definition of
     the Hurwitz zeta, imported/trivial), f(s) = sum_n c(n) n^{-s} with
     c(n) depending only on n mod 5: pattern (1, kappa, -kappa, -1, 0) on
     residues (1,2,3,4,0).  c is an ODD function on (Z/5)^*, hence a linear
     combination of the two odd characters chi, chibar mod 5 (chi(2) = i).
     PROVED EXACTLY: the full 4-character Fourier expansion of c is computed
     in K and the even components (principal and quadratic) vanish; the odd
     components are alpha (on chi) and beta (on chibar).
  2. IMPORTED (classical, Hurwitz-era): for a primitive ODD character chi
     mod q,  Lambda(s,chi) = (q/pi)^{(s+1)/2} Gamma((s+1)/2) L(s,chi)
     satisfies Lambda(s,chi) = eps(chi) Lambda(1-s,chibar) with
     eps(chi) = tau(chi) / (i sqrt q),  tau(chi) = sum_a chi(a) e^{2 pi i a/q}.
  3. PROVED HERE, exactly in K: tau(chi) computed as an element of K;
     tau(chi) tau(chibar) = -5;  tau(chi) conj(tau(chi)) = 5;
     sqrt5 realized as r = 1 + 2 zeta_5 + 2 zeta_5^4 with r^2 = 5;
     eps = tau(chi)/(i r) and epsbar = tau(chibar)/(i r) satisfy
     eps * epsbar = 1 and conj(eps) = eps^{-1} (|eps| = 1 symbolically).
  4. SELF-DUALITY EQUATION solved exactly: f = alpha L(s,chi) +
     beta L(s,chibar) satisfies Lambda_f(s) = Lambda_f(1-s) iff
     alpha eps = beta and beta epsbar = alpha (equivalent given
     eps epsbar = 1).  With the normalization alpha + beta = 1 (so that
     c(1) = 1) the unique solution is alpha = 1/(1+eps), beta = eps/(1+eps);
     both FE conditions are VERIFIED as exact identities in K.
  5. kappa = i (alpha - beta) is verified to be real (fixed by the
     conjugation z -> z^19), irrational, of exact degree 4 over Q with
     minimal polynomial T^4 + 2 T^3 - 6 T^2 - 2 T + 1 (computed as the
     Galois orbit product, verified rational, verified to annihilate kappa,
     irreducible because the 4 conjugates are pairwise distinct).  The
     classical closed form is proved as the exact identity
     (kappa (sqrt5 - 1) + 2)^2 = 10 - 2 sqrt5, and the root is localized by
     EXACT Sturm: exactly one root of the minimal polynomial lies in
     (28/100, 29/100).  (Which real number the canonical embedding
     z -> e^{i pi/10} sends kappa to is corroborated numerically at 60
     digits: 0.2840790438... = (sqrt(10-2 sqrt5)-2)/(sqrt5-1).)
  6. BONUS (exact): the 2-dimensional space C L(s,chi) + C L(s,chibar)
     splits into root-number eigenlines: the w = -1 eigenline constant
     kappa_minus = i (1+eps)/(1-eps) satisfies kappa * kappa_minus = -1 and
     kappa_minus = sigma_9(kappa) (a Galois conjugate).

NO EULER PRODUCT (exact refutation for this normalization):
  a_2 = kappa, a_3 = -kappa, a_6 = c(6 mod 5) = c(1) = 1, and
  a_2 a_3 = -kappa^2 != a_6:  a_6 - a_2 a_3 = 1 + kappa^2 is a NONZERO
  element of K (exact coordinates; Norm_{K/Q}(1+kappa^2) = 6400 != 0).
  LEMMA (proved, formal): a Dirichlet series with a_1 = 1 that factors as a
  formal Euler product over the rational primes with unital local factors
  (constant term 1) has completely determined multiplicative coefficients
  a_{mn} = a_m a_n for coprime m, n; the witness therefore refutes ANY such
  factorization, not just one candidate.  The historical statement and the
  off-line-zero phenomenon are imported (Davenport-Heilbronn 1936).

CURIOSITY, recorded honestly: every prime-power coefficient COLUMN
(a_{p^k})_k of f is individually a pure weight-0 rational sequence of degree
<= 2 (period divides 4 because u^4 = 1 in (Z/5)^*), certified by detector
runs — yet these columns are NOT local factors of anything: their product
does not rebuild f (same witness a_6 != a_2 a_3).  Passing a local battery
does not certify an Euler product.

FLOATS appear ONLY in the quarantined numeric_corroboration() section
(mpmath at 60 dps), used ONLY for NON_DIRECTED_NUMERIC corroboration cells:
the approximate off-line zero rho = 0.8085... + 85.6993... i (existence of
off-line zeros is imported from the literature, NOT established by this
numeric), a numeric FE defect check, and the embedding value of kappa.

RH is not established by anything here; rh_established = false throughout.
"""

from fractions import Fraction

from core.exact import (
    count_real_roots_in,
    poly_divmod,
    poly_mul,
    poly_trim,
)
from core.reconstruct import detect, HOLDS, FAILS, SKIPPED
from core.worlds import cell, save_world, validate_world

# ---------------------------------------------------------------------------
# Exact arithmetic in K = Q(zeta_20) = Q[x] / Phi_20(x), Fractions only
# ---------------------------------------------------------------------------

# Phi_20(x) = x^8 - x^6 + x^4 - x^2 + 1, low-first coefficient order.
PHI20 = [Fraction(c) for c in (1, 0, -1, 0, 1, 0, -1, 0, 1)]


def _red(p):
    """Reduce a low-first Fraction polynomial mod Phi_20; pad to length 8."""
    r = list(poly_divmod([Fraction(c) for c in p], PHI20)[1])
    return (r + [Fraction(0)] * 8)[:8]


class Cyc:
    """Element of Q(zeta_20) on the power basis 1, z, ..., z^7 (z = zeta_20).

    All coefficients are Fractions; every operation is exact."""

    __slots__ = ("v",)

    def __init__(self, v):
        if isinstance(v, Cyc):
            self.v = list(v.v)
        elif isinstance(v, (int, Fraction)):
            self.v = [Fraction(v)] + [Fraction(0)] * 7
        else:
            self.v = _red(v)

    def __add__(s, o):
        return Cyc([a + b for a, b in zip(s.v, Cyc(o).v)])

    __radd__ = __add__

    def __sub__(s, o):
        return Cyc([a - b for a, b in zip(s.v, Cyc(o).v)])

    def __neg__(s):
        return Cyc([-a for a in s.v])

    def __mul__(s, o):
        return Cyc(_red(poly_mul(s.v, Cyc(o).v)))

    __rmul__ = __mul__

    def __eq__(s, o):
        return s.v == Cyc(o).v

    def __hash__(s):
        return hash(tuple(s.v))

    def is_rational(s):
        return all(c == 0 for c in s.v[1:])

    def inv(s):
        """Exact inverse by the extended Euclidean algorithm in Q[x]."""
        def sub(a, b):
            n = max(len(a), len(b))
            a = list(a) + [Fraction(0)] * (n - len(a))
            b = list(b) + [Fraction(0)] * (n - len(b))
            return poly_trim([x - y for x, y in zip(a, b)])

        r0, r1 = PHI20, poly_trim(s.v)
        t0, t1 = [Fraction(0)], [Fraction(1)]
        while poly_trim(r1):
            q, r = poly_divmod(r0, r1)
            r0, r1 = r1, r
            t0, t1 = t1, sub(t0, poly_mul(q, t1))
        g = poly_trim(r0)
        assert len(g) == 1 and g[0] != 0, "element not invertible"
        out = Cyc([c / g[0] for c in t0])
        assert out * s == Cyc(1), "inverse certificate failed"
        return out

    def __repr__(s):
        return "[" + ", ".join(str(c) for c in s.v) + "]"


def zpow(k):
    """z^k as a Cyc element (k reduced mod 20 since z^20 = 1; asserted below)."""
    return Cyc([Fraction(0)] * (k % 20) + [Fraction(1)])


def cyc_pow(x, n):
    r = Cyc(1)
    for _ in range(n):
        r = r * x
    return r


def sigma(a, e):
    """Galois automorphism sigma_a : z -> z^a (a coprime to 20), by Horner."""
    za = zpow(a)
    out = Cyc(0)
    for c in reversed(e.v):
        out = out * za + Cyc(c)
    return out


def conj(e):
    """Complex conjugation = sigma_19 (z -> z^{-1})."""
    return sigma(19, e)


def vecstr(e):
    """Deterministic coordinate string on the basis 1, z, ..., z^7."""
    return "(" + ", ".join(str(c) for c in e.v) + ")"


# ---------------------------------------------------------------------------
# Step A: exact derivation of the Davenport-Heilbronn constant
# ---------------------------------------------------------------------------

def derive_constant():
    """Derive kappa exactly and verify the FE self-duality identities in K.

    Returns a dict of exact objects and witness strings.  Every claim is
    asserted; nothing is copied from the literature except the imported FE
    of odd Dirichlet L-functions (step 2 of the module docstring)."""
    W = {}
    one, i = Cyc(1), zpow(5)

    # -- the ambient field: z has exact multiplicative order 20 -------------
    z = zpow(1)
    assert cyc_pow(z, 20) == one
    for d in (1, 2, 4, 5, 10):          # proper divisors of 20
        assert cyc_pow(z, d) != one, d
    assert i * i == Cyc(-1)             # z^5 = i
    z5 = zpow(4)                        # z^4 = zeta_5
    assert cyc_pow(z5, 5) == one and z5 != one

    # -- sqrt5 inside K:  r = 1 + 2 zeta_5 + 2 zeta_5^4,  r^2 = 5 ----------
    r = one + 2 * zpow(4) + 2 * zpow(16)
    assert r * r == Cyc(5)
    W["sqrt5"] = ("sqrt5 realized exactly: r = 1 + 2 zeta_5 + 2 zeta_5^4 = "
                  + vecstr(r) + " with r^2 = 5 (positive root under the "
                  "standard embedding z -> e^{i pi/10}, since zeta_5 + "
                  "zeta_5^4 = 2 cos 72deg > 0; embedding statement "
                  "corroborated numerically only)")

    # -- the two odd characters mod 5 (chi(2) = i) --------------------------
    chi = {1: one, 2: i, 3: -i, 4: -one}
    chib = {a: conj(chi[a]) for a in chi}
    # character property on the generator 2: chi(2^k) = i^k, and oddness
    assert chi[4] == chi[2] * chi[2]            # 4 = 2^2 mod 5
    assert chi[3] == chi[2] * chi[2] * chi[2]   # 3 = 2^3 mod 5
    assert chi[4] == -one                        # chi(-1) = -1: odd
    assert chib[4] == -one                       # chibar odd too

    # -- Gauss sums, exactly in K ------------------------------------------
    tau = sum((chi[a] * zpow(4 * a) for a in (1, 2, 3, 4)), Cyc(0))
    taub = sum((chib[a] * zpow(4 * a) for a in (1, 2, 3, 4)), Cyc(0))
    assert tau * taub == Cyc(-5)        # tau(chi) tau(chibar) = chi(-1) q
    assert tau * conj(tau) == Cyc(5)    # |tau|^2 = 5, symbolically
    W["gauss"] = ("tau(chi) = sum_a chi(a) zeta_5^a computed exactly in K: "
                  "tau = " + vecstr(tau) + "; verified tau(chi) tau(chibar) "
                  "= -5 = chi(-1) 5 and tau(chi) conj(tau(chi)) = 5 "
                  "(PROVED_HERE, no import)")

    # -- root numbers eps = tau/(i sqrt5), exactly --------------------------
    ir_inv = (i * r).inv()
    eps = tau * ir_inv
    epsb = taub * ir_inv
    assert eps * epsb == one            # eps(chi) eps(chibar) = 1
    assert conj(eps) == eps.inv()       # |eps| = 1 symbolically
    W["eps"] = ("eps(chi) = tau(chi)/(i sqrt5) = " + vecstr(eps) +
                "; verified eps(chi) eps(chibar) = 1 and conj(eps) = "
                "eps^{-1} exactly (unitarity of the root number, "
                "symbolic in K)")

    # -- solve the self-duality equation ------------------------------------
    # Lambda_f(s) = Lambda_f(1-s) for f = alpha L(chi) + beta L(chibar)
    # requires alpha eps = beta and beta epsbar = alpha; normalize
    # alpha + beta = 1 so that the n=1 Dirichlet coefficient of f is 1.
    alpha = (one + eps).inv()           # existence certified by .inv()
    beta = eps * alpha
    assert alpha + beta == one          # normalization
    assert alpha * eps == beta          # FE condition 1 (exact identity)
    assert beta * epsb == alpha         # FE condition 2 (exact identity)
    assert conj(alpha) == beta          # beta = conj(alpha): f real-valued
    W["fe_solution"] = (
        "self-duality solved exactly: alpha = 1/(1+eps) = " + vecstr(alpha) +
        ", beta = eps/(1+eps) = 1 - alpha; VERIFIED as exact identities in "
        "K: alpha + beta = 1, alpha eps(chi) = beta, beta eps(chibar) = "
        "alpha, conj(alpha) = beta.  Hence Lambda_f(s) := (5/pi)^{(s+1)/2} "
        "Gamma((s+1)/2) f(s) satisfies Lambda_f(s) = Lambda_f(1-s), GIVEN "
        "the imported classical FE Lambda(s,chi) = eps(chi) "
        "Lambda(1-s,chibar) for the odd primitive characters mod 5")

    # -- the constant -------------------------------------------------------
    kappa = i * (alpha - beta)
    assert conj(kappa) == kappa         # kappa is real (fixed by sigma_19)
    assert not kappa.is_rational()      # and irrational
    W["kappa"] = ("kappa = i (alpha - beta) = " + vecstr(kappa) +
                  " on the basis 1, z, ..., z^7 of Q(zeta_20); verified "
                  "real (sigma_19-fixed) and irrational")

    # -- coefficient pattern of f: c = alpha chi + beta chibar --------------
    c = {a: alpha * chi[a] + beta * chib[a] for a in (1, 2, 3, 4)}
    c[0] = Cyc(0)
    assert c[1] == one and c[2] == kappa and c[3] == -kappa and c[4] == -one
    for a in (1, 2, 3, 4):
        assert c[5 - a] == -c[a]        # c is odd on (Z/5)^*
    # full 4-character Fourier expansion: even components vanish exactly
    chi0 = {1: one, 2: one, 3: one, 4: one}
    chiq = {1: one, 2: -one, 3: -one, 4: one}       # quadratic character
    inv_mod5 = {1: 1, 2: 3, 3: 2, 4: 4}
    quarter = Cyc(Fraction(1, 4))
    comp = {}
    for name, ps in (("chi0", chi0), ("chi_quad", chiq),
                     ("chi", chi), ("chibar", chib)):
        comp[name] = quarter * sum((c[a] * ps[inv_mod5[a]]
                                    for a in (1, 2, 3, 4)), Cyc(0))
    assert comp["chi0"] == Cyc(0) and comp["chi_quad"] == Cyc(0)
    assert comp["chi"] == alpha and comp["chibar"] == beta
    W["decomposition"] = (
        "coefficient function c(n) of f (period 5, pattern (1, kappa, "
        "-kappa, -1, 0) on residues (1,2,3,4,0)) expanded exactly over ALL "
        "four Dirichlet characters mod 5: even components (principal, "
        "quadratic) are EXACTLY 0; odd components are alpha on chi and "
        "beta on chibar.  Hence f = alpha L(s,chi) + beta L(s,chibar) "
        "identically (coefficient-wise), where 5^{-s} zeta(s,a/5) = "
        "sum_{n = a mod 5} n^{-s} is the definitional Hurwitz unfolding")

    # -- minimal polynomial of kappa over Q, via the Galois orbit -----------
    orbit = [sigma(a, kappa) for a in (1, 3, 7, 9)]   # coset reps of {+-1}
    assert len({tuple(x.v) for x in orbit}) == 4      # pairwise distinct
    mp_coeffs = [Cyc(1)]                              # prod (T - conjugate)
    for x in orbit:
        new = [Cyc(0)] * (len(mp_coeffs) + 1)
        for j, cf in enumerate(mp_coeffs):
            new[j] = new[j] - x * cf
            new[j + 1] = new[j + 1] + cf
        mp_coeffs = new
    minpoly = []
    for cf in mp_coeffs:
        assert cf.is_rational(), cf                   # rational coefficients
        minpoly.append(cf.v[0])
    assert minpoly == [Fraction(1), Fraction(-2), Fraction(-6),
                       Fraction(2), Fraction(1)]      # 1 -2T -6T^2 +2T^3 +T^4
    acc = Cyc(0)                                      # m(kappa) = 0 in K
    for cf in reversed(minpoly):
        acc = acc * kappa + Cyc(cf)
    assert acc == Cyc(0)
    # exact Sturm localization of the four (all-real) roots of m:
    assert count_real_roots_in(minpoly, -10, 10) == 4
    assert count_real_roots_in(minpoly, Fraction(28, 100),
                               Fraction(29, 100)) == 1
    assert count_real_roots_in(minpoly, -4, -3) == 1
    assert count_real_roots_in(minpoly, -1, 0) == 1
    assert count_real_roots_in(minpoly, 1, 2) == 1
    W["minpoly"] = (
        "minimal polynomial of kappa over Q computed as the Galois-orbit "
        "product prod_{a in {1,3,7,9}} (T - sigma_a(kappa)): m(T) = T^4 + "
        "2T^3 - 6T^2 - 2T + 1 (low-first [1, -2, -6, 2, 1]); coefficients "
        "verified rational, m(kappa) = 0 verified in K, degree exactly 4 "
        "(the 4 conjugates are pairwise distinct => m irreducible, kappa "
        "irrational).  EXACT Sturm: m has 4 real roots, localized one each "
        "in (-4,-3), (-1,0), (28/100, 29/100), (1,2)")

    # -- classical closed form, proved as an exact identity -----------------
    lhs = kappa * (r - one) + Cyc(2)
    assert lhs * lhs == Cyc(10) - 2 * r
    W["closed_form"] = (
        "classical closed form PROVED as the exact identity in K: "
        "(kappa (sqrt5 - 1) + 2)^2 = 10 - 2 sqrt5, i.e. kappa = "
        "(+-sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1); combined with the Sturm "
        "localization, kappa is the root of m in (28/100, 29/100) UNDER "
        "the standard embedding z -> e^{i pi/10} (the embedding "
        "identification itself is corroborated numerically at 60 digits: "
        "kappa = 0.2840790438404122960..., the + sign)")

    # -- root-number eigenline decomposition (bonus, exact) -----------------
    alpha_m = (one - eps).inv()
    beta_m = -eps * alpha_m
    assert alpha_m + beta_m == one
    assert alpha_m * eps == -beta_m               # w = -1 FE condition
    kappa_m = i * (alpha_m - beta_m)
    assert conj(kappa_m) == kappa_m
    assert kappa * kappa_m == Cyc(-1)
    assert sigma(9, kappa) == kappa_m
    W["eigenlines"] = (
        "the 2-dim space C L(s,chi) + C L(s,chibar) splits exactly into "
        "root-number eigenlines: the w = -1 combination (alpha_-, beta_-) "
        "= (1/(1-eps), -eps/(1-eps)) satisfies alpha_- eps = -beta_- "
        "(exact), with constant kappa_- = i(alpha_- - beta_-) = " +
        vecstr(kappa_m) + "; verified kappa * kappa_- = -1 and kappa_- = "
        "sigma_9(kappa), a Galois conjugate.  Lambda of that combination "
        "satisfies Lambda(s) = -Lambda(1-s) under the same imported FE")

    return {"W": W, "kappa": kappa, "one": one, "i": i, "c": c,
            "alpha": alpha, "beta": beta, "minpoly": minpoly}


# ---------------------------------------------------------------------------
# Step B: exact refutation of multiplicativity / Euler product
# ---------------------------------------------------------------------------

def refute_multiplicativity(D):
    """a_6 != a_2 a_3, exactly in K.  Returns witness strings."""
    kappa, one = D["kappa"], D["one"]
    c = D["c"]

    def a(n):
        return c[n % 5]

    a2, a3, a6 = a(2), a(3), a(6)
    assert a(1) == one                      # normalization a_1 = 1
    assert a2 == kappa and a3 == -kappa and a6 == one
    defect = a6 - a2 * a3                   # = 1 + kappa^2
    assert defect == one + kappa * kappa
    assert defect != Cyc(0)                 # THE refutation
    # norm certificate that the defect is nonzero (and how nonzero):
    norm = Cyc(1)
    for g in (1, 3, 7, 9, 11, 13, 17, 19):
        norm = norm * sigma(g, defect)
    assert norm == Cyc(6400)
    w = ("EXACT WITNESS (coefficients of f in K = Q(zeta_20), coordinates "
         "on 1, z, ..., z^7): a_2 = kappa = " + vecstr(a2) + ", a_3 = "
         "-kappa, a_6 = 1 (6 = 1 mod 5).  a_2 a_3 = -kappa^2 and a_6 - "
         "a_2 a_3 = 1 + kappa^2 = " + vecstr(one + kappa * kappa) +
         " != 0; nonzero-ness certified by Norm_{K/Q}(1 + kappa^2) = 6400 "
         "(product over all 8 Galois conjugates, exact).  All three "
         "coefficients lie in the real quartic subfield Q(kappa).  "
         "LEMMA (formal, proved): a formal Dirichlet series with a_1 = 1 "
         "admitting ANY Euler product over the rational primes with "
         "unital local factors (local constant term 1) has multiplicative "
         "coefficients — the coefficient of n^{-s} in prod_p L_p is "
         "prod_p b_{p, v_p(n)}.  Hence a_6 != a_2 a_3 refutes every such "
         "factorization of f, for this (intrinsic) normalization; a "
         "vertical shift s -> s + c rescales both sides of a_6 = a_2 a_3 "
         "by 6^{-c} and changes nothing")
    return w


# ---------------------------------------------------------------------------
# Step C: exact column structure + detector runs (rational data only)
# ---------------------------------------------------------------------------

def column_structure(D):
    """Prime-power coefficient columns of f are pure degree <= 2 rational
    sequences — and yet are NOT local factors.  All exact."""
    kappa, one, c = D["kappa"], D["one"], D["c"]
    NW = 12       # detector window
    HO = 4        # holdout

    # every unit u mod 5 has u^4 = 1, so every column has period dividing 4;
    # u^2 in {1, 4} and c(-x) = -c(x), so a_{p^{k+2}} = +- a_{p^k} exactly.
    for u in (1, 2, 3, 4):
        assert pow(u, 4, 5) == 1
        assert pow(u, 2, 5) in (1, 4)
        assert c[(5 - u) % 5] == -c[u]
    # exact columns a_{p^k} = c(p^k mod 5) for representative primes of the
    # four residue classes: 11 = 1, 2 = 2, 3 = 3 wait 3 handled via 2's
    # component structure; use p = 2 (order 4), p = 19 = -1 (order 2),
    # p = 11 = 1 (order 1).  Column values decomposed exactly in the basis
    # (1, kappa) of the Q-span of the coefficient values (canonical since
    # kappa is irrational — proved in derive_constant).
    basis_decomp = {tuple(one.v): (1, 0), tuple((-one).v): (-1, 0),
                    tuple(kappa.v): (0, 1), tuple((-kappa).v): (0, -1),
                    tuple(Cyc(0).v): (0, 0)}
    cols = {}
    for p in (2, 11, 19):
        u_part, k_part = [], []
        for k in range(NW):
            val = c[pow(p, k, 5)]
            x, y = basis_decomp[tuple(val.v)]
            assert val == Cyc(x) + Cyc(y) * kappa    # decomposition exact
            u_part.append(Fraction(x))
            k_part.append(Fraction(y))
        cols[p] = (u_part, k_part)

    # p = 2: column = u + kappa * v with u = [1,0,-1,0,...], v = T*u (shift)
    u2, v2 = cols[2]
    assert u2 == [Fraction(x) for x in (1, 0, -1, 0)] * 3
    assert v2 == [Fraction(0)] + u2[:-1]              # v2 = shift of u2
    # p = 11 (= 1 mod 5): true column is rational, all ones
    u11, v11 = cols[11]
    assert u11 == [Fraction(1)] * NW and v11 == [Fraction(0)] * NW
    # p = 19 (= -1 mod 5): true column is rational, alternating
    u19, v19 = cols[19]
    assert u19 == [Fraction((-1) ** k) for k in range(NW)]
    assert v19 == [Fraction(0)] * NW

    runs = []

    # detector on the rational component of the 2-column: degree 2, pure
    d2 = detect(u2, mode="coefficients", weight=(2, 0), holdout=HO).as_dict()
    assert d2["refusal"] is None, d2
    got = {x["axiom"]: x["status"] for x in d2["cells"]}
    assert got == {"A1_FINITE_RANK": HOLDS, "A2_EFFECTIVITY": HOLDS,
                   "A3_INTEGRALITY": HOLDS, "A4_PURITY": HOLDS,
                   "A5_HELD_OUT": HOLDS}, got
    assert d2["object"]["degree"] == 2
    assert d2["object"]["denominator"] == "[1, 0, 1]"    # 1 + T^2
    runs.append({"prime": 2, "weight": [2, 0], "mode": "coefficients",
                 "series": "rational component of (a_{2^k}) in the basis "
                           "(1, kappa): [1,0,-1,0,...], window 12",
                 "verdict": d2})

    # REFUSAL DEMONSTRATION: the kappa-component of the 2-column starts
    # with 0, so coefficient mode refuses at A1 (a_0 = 1 required).
    dv = detect(v2, mode="coefficients", weight=(2, 0), holdout=HO).as_dict()
    assert dv["refusal"] == "A1_FINITE_RANK", dv
    runs.append({"prime": 2, "weight": [2, 0], "mode": "coefficients",
                 "series": "kappa-component of (a_{2^k}): [0,1,0,-1,...] "
                           "(= T times the rational component, exactly)",
                 "note": "honest refusal: not a unital coefficient series",
                 "verdict": dv})

    # true (fully rational) columns at p = 11 and p = 19
    d11 = detect(u11, mode="coefficients", weight=(11, 0),
                 holdout=HO).as_dict()
    assert d11["refusal"] is None
    assert d11["object"]["degree"] == 1
    assert d11["object"]["denominator"] == "[1, -1]"
    assert all(x["status"] == HOLDS for x in d11["cells"])
    runs.append({"prime": 11, "weight": [11, 0], "mode": "coefficients",
                 "series": "true column (a_{11^k}) = [1,1,1,...] "
                           "(11 = 1 mod 5), window 12",
                 "verdict": d11})

    d19 = detect(u19, mode="coefficients", weight=(19, 0),
                 holdout=HO).as_dict()
    assert d19["refusal"] is None
    assert d19["object"]["degree"] == 1
    assert d19["object"]["denominator"] == "[1, 1]"
    assert all(x["status"] == HOLDS for x in d19["cells"])
    runs.append({"prime": 19, "weight": [19, 0], "mode": "coefficients",
                 "series": "true column (a_{19^k}) = [1,-1,1,-1,...] "
                           "(19 = -1 mod 5), window 12",
                 "verdict": d19})

    witness = (
        "every prime-power column (a_{p^k})_k of f satisfies the exact "
        "period-4 recurrence a_{p^{k+2}} = c(p^2 mod 5) a_{p^k} sign-"
        "pattern (u^4 = 1 in (Z/5)^*, c odd — verified exactly for all "
        "units); each column is a rational sequence of degree <= 2 over "
        "Q(kappa) with all inverse roots on |T| = 1 (weight-0 pure).  "
        "Detector certificates (exact, on rational data): p=2 rational "
        "component -> denominator 1 + T^2 (deg 2, disc -4 < 0, product "
        "1 = 2^0: complete degree-2 purity test HOLDS); p=11 true column "
        "-> 1 - T; p=19 true column -> 1 + T; kappa-component refusal at "
        "A1 recorded honestly.  BUT these columns are NOT local factors: "
        "the product of the column generating functions does not rebuild "
        "f — a_6 != a_2 a_3.  Column-level purity certifies NOTHING "
        "global without multiplicativity")
    return witness, runs


# ---------------------------------------------------------------------------
# Step D: quarantined numeric corroboration (floats live ONLY here)
# ---------------------------------------------------------------------------

def numeric_corroboration(D):
    """NON_DIRECTED_NUMERIC corroboration with mpmath at 60 digits.

    Nothing here is the basis of any HOLDS/FAILS/FALSE status: the FALSE
    critical-line status is imported from the literature; these numerics
    only corroborate.  Deterministic: fixed precision, fixed seeds."""
    import mpmath as mp
    mp.mp.dps = 60

    z = mp.e ** (mp.mpc(0, 1) * mp.pi / 10)        # standard embedding
    kap = mp.mpc(0)
    for j, cf in enumerate(D["kappa"].v):
        kap += mp.mpf(cf.numerator) / mp.mpf(cf.denominator) * z ** j
    closed = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
    assert abs(mp.im(kap)) < mp.mpf(10) ** (-50)
    assert abs(mp.re(kap) - closed) < mp.mpf(10) ** (-50)
    k = mp.re(kap)

    def f(s):
        return 5 ** (-s) * (mp.zeta(s, mp.mpf(1) / 5)
                            + k * mp.zeta(s, mp.mpf(2) / 5)
                            - k * mp.zeta(s, mp.mpf(3) / 5)
                            - mp.zeta(s, mp.mpf(4) / 5))

    def Lam(s):
        return (5 / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * f(s)

    fe_defects = []
    for s in (mp.mpc("0.3", "2"), mp.mpc("0.7", "14.2"),
              mp.mpc("-1.2", "5.5")):
        fe_defects.append(abs(Lam(s) - Lam(1 - s)))
    assert all(d < mp.mpf(10) ** (-50) for d in fe_defects)

    # off-line zero: literature seed (Spira-era computations), refined here
    rho = mp.findroot(f, mp.mpc("0.808517", "85.699348"))
    resid = abs(f(rho))
    assert resid < mp.mpf(10) ** (-50)
    assert mp.re(rho) - mp.mpf(1) / 2 > mp.mpf("0.3")   # far off the line

    return {
        "label": "NON_DIRECTED_NUMERIC (mpmath, 60 dps) — corroboration "
                 "only, never the basis of a status",
        "kappa_embedding": ("kappa -> " + mp.nstr(mp.re(kap), 40) +
                            " under z -> e^{i pi/10}; matches the closed "
                            "form (sqrt(10-2 sqrt5)-2)/(sqrt5-1) to < "
                            "1e-50; imaginary part < 1e-50"),
        "fe_defect": ("|Lambda_f(s) - Lambda_f(1-s)| < 1e-50 at s = "
                      "0.3+2i, 0.7+14.2i, -1.2+5.5i (corroborates the "
                      "exactly-derived FE end to end, conventions "
                      "included)"),
        "off_line_zero": ("approximate zero rho = " + mp.nstr(rho, 30) +
                          " with |f(rho)| < 1e-50 and Re(rho) - 1/2 = " +
                          mp.nstr(mp.re(rho) - mp.mpf(1) / 2, 12) +
                          "; zero LOCATION approximate (numeric); the "
                          "EXISTENCE of off-line zeros is imported from "
                          "the literature, not from this numeric"),
    }


# ---------------------------------------------------------------------------
# The world record
# ---------------------------------------------------------------------------

def build_world(D, mult_witness, col_witness, runs, numerics):
    W = D["W"]
    dh1936 = ("H. Davenport, H. Heilbronn (1936), on the zeros of certain "
              "Dirichlet series, J. London Math. Soc. (papers I-II): "
              "zeta(s,a) for rational (and transcendental) a, and "
              "combinations of the Davenport-Heilbronn type, have "
              "infinitely many zeros in Re s > 1")
    fe_import = ("functional equation of Dirichlet L-functions / Hurwitz "
                 "zeta at rational parameters: classical (A. Hurwitz, "
                 "~1882); modern exposition: H. Davenport, Multiplicative "
                 "Number Theory (1967), with eps(chi) = tau(chi)/(i sqrt q) "
                 "for odd primitive chi")
    cn_density = ("CITATION-NEEDED: zero-density work on the Davenport-"
                  "Heilbronn function — positive (in fact power-scale) "
                  "counts of zeros in fixed strips 1/2 < sigma_1 < Re s < "
                  "sigma_2 < 1 (Balanzario-Sanchez-Ortiz, ~2007, Math. "
                  "Comp.; context: Bombieri-Hejhal (~1995) on the "
                  "distribution of zeros of linear combinations of Euler "
                  "products)")

    fe_witness = (
        "EXACT DERIVATION CHAIN (all identities verified in K = Q(zeta_20) "
        "= Q[x]/(x^8 - x^6 + x^4 - x^2 + 1), Fraction coefficients; z = "
        "zeta_20 of exact order 20, i = z^5, zeta_5 = z^4): [sqrt5] " +
        W["sqrt5"] + " || [gauss] " + W["gauss"] + " || [eps] " + W["eps"] +
        " || [decomposition] " + W["decomposition"] + " || [fe_solution] " +
        W["fe_solution"] + " || [kappa] " + W["kappa"] + " || [minpoly] " +
        W["minpoly"] + " || [closed_form] " + W["closed_form"] +
        " || [eigenlines] " + W["eigenlines"] +
        " || IMPORTED INGREDIENTS: the FE of the two odd primitive "
        "characters mod 5 (citation field) and the meromorphic (here "
        "entire) continuation of L(s,chi), L(s,chibar); everything else "
        "PROVED_HERE.  Analytic conclusion: f is entire and Lambda_f(s) = "
        "(5/pi)^{(s+1)/2} Gamma((s+1)/2) f(s) = Lambda_f(1-s)")

    ladder = {
        "L0_WELL_DEFINED": cell(
            "HOLDS", "PROVED_HERE",
            witness=("f(s) = 5^{-s}(zeta(s,1/5) + kappa zeta(s,2/5) - "
                     "kappa zeta(s,3/5) - zeta(s,4/5)) = sum_n c(n) n^{-s} "
                     "with c(n) the exact period-5 pattern (1, kappa, "
                     "-kappa, -1, 0); kappa is the EXACT field element " +
                     vecstr(D["kappa"]) + " in Q(zeta_20) (derived, not "
                     "quoted — see L6), real with minimal polynomial T^4 + "
                     "2T^3 - 6T^2 - 2T + 1; coefficients bounded, so the "
                     "series converges absolutely for Re s > 1; "
                     "continuation is inherited from the two entire "
                     "Dirichlet L-functions (imported)"),
            citation=fe_import),
        "L1_MULTIPLICATIVITY": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("a_6 != a_2 a_3.  " + mult_witness +
                     ".  SCOPE: this refutes multiplicativity of THIS "
                     "normalization (a_1 = 1, the one forced by any unital "
                     "Euler product); it is a single exact triple, which "
                     "is all that is needed"),
            citation=dh1936),
        "L2_EULER_PRODUCT": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("no Euler product over the rational primes with "
                     "unital local factors exists: any such formal "
                     "factorization forces a_{mn} = a_m a_n for coprime "
                     "m, n (proved lemma in the L1 witness), refuted "
                     "exactly by a_6 - a_2 a_3 = 1 + kappa^2 != 0 "
                     "(Norm = 6400).  The historical statement — f is a "
                     "functional-equation zeta WITHOUT Euler product — is "
                     "the point of the Davenport-Heilbronn construction "
                     "(imported)"),
            citation=dh1936),
        "L3_BOUNDED_DEGREE_RATIONAL": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("there are no local factors to bound: a system of "
                     "bounded-degree rational local factors multiplying "
                     "out to f would BE a unital Euler product, refuted by "
                     "the L1/L2 witness (a_6 != a_2 a_3, exact).  "
                     "CURIOSITY (exact, recorded honestly): " + col_witness),
            citation=""),
        "L4_WEIGHT_DUALITY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("GLOBAL self-duality coherence, proved exactly: "
                     "conj(alpha) = beta in K, so all Dirichlet "
                     "coefficients of f are real (c(n) in the real quartic "
                     "field Q(kappa)); the FE is self-dual with sign +1 by "
                     "exact construction (alpha eps = beta, beta epsbar = "
                     "alpha).  SCOPE: there is NO local weight data (no "
                     "Euler product, no Frobenius/Satake parameters) — "
                     "the cell is scoped to coefficient/FE-level duality, "
                     "which is what the Davenport-Heilbronn example "
                     "possesses"),
            citation=""),
        "L5_CONDUCTOR_GAMMA_ROOT": cell(
            "HOLDS", "PROVED_HERE",
            witness=("canonical data (conductor, gamma, root number) = "
                     "(5, Gamma_R(s+1) = pi^{-(s+1)/2} Gamma((s+1)/2), "
                     "+1): both constituent characters are odd, primitive, "
                     "of conductor 5, so they share the gamma factor and "
                     "conductor; the sign +1 is the exactly-solved "
                     "self-duality (alpha eps = beta).  Root-number "
                     "unitarity eps epsbar = 1 proved exactly in K; the "
                     "w = -1 eigenline (sign -1 companion function) also "
                     "computed exactly (see L6 witness [eigenlines])"),
            citation=fe_import),
        "L6_CONTINUATION_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=fe_witness,
            citation=fe_import),
        "L7_TWIST_TENSOR_COMPAT": cell(
            "OPEN", "OPEN",
            witness=("no twist/tensor theory exists for f itself: with no "
                     "Euler product there is no local data to tensor, and "
                     "no Rankin-Selberg theory applies.  Termwise twisting "
                     "by a character psi maps f to alpha L(s,chi psi) + "
                     "beta L(s,chibar psi) — another combination of the "
                     "same type, generally NOT self-dual with the same "
                     "coefficients (its FE mixes the pair), so the "
                     "DH-type family is closed under termwise twist but "
                     "the self-dual normalization is not; no canonical "
                     "tensor structure is known, and nonexistence is not "
                     "proved — OPEN, not FAILS"),
            citation=""),
        "L8_REALIZATION": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("FAILS for every realization class that entails an "
                     "Euler product over its own primes/closed orbits "
                     "(automorphic L(s,pi), motivic/Hasse-Weil, "
                     "Selberg/Ruelle dynamical, Ihara-type combinatorial): "
                     "each such realization forces multiplicative "
                     "coefficients, refuted exactly by a_6 != a_2 a_3.  "
                     "In particular f is NOT in the Selberg class (the "
                     "Euler-product axiom fails; the other axioms — "
                     "Dirichlet series, continuation, FE, coefficient "
                     "growth — f satisfies, which is what makes it the "
                     "classical counterexample delimiting that class).  "
                     "The only realization f has is its construction: a "
                     "vector in the 2-dim space C L(s,chi) + C "
                     "L(s,chibar) (exact decomposition proved in L6).  "
                     "An exotic realization in some framework NOT "
                     "entailing an Euler product is not excluded — see "
                     "notes"),
            citation=("Selberg class context: CITATION-NEEDED: A. Selberg "
                      "(~1989-1992), Old and new conjectures ... "
                      "(definition of the class); " + dh1936)),
        "L9_EXPLICIT_FORMULA_POSITIVITY": cell(
            "FAILS", "IMPORTED_THEOREM",
            witness=("two independent failures.  (i) POSITIVITY: f has "
                     "zeros off the critical line — infinitely many in "
                     "Re s > 1 (Davenport-Heilbronn 1936, imported) and "
                     "zeros in the open strip 1/2 < Re s < 1 (imported, "
                     "citation-needed density work); any Weil-type "
                     "positivity for the zero multiset of Lambda_f would "
                     "force the RH analogue, so it fails.  (ii) PRIME "
                     "SIDE: with no Euler product, -f'/f has no prime-"
                     "power Dirichlet coefficients, so there is no "
                     "arithmetic explicit formula at all — the zero side "
                     "(Hadamard product of the entire order-1 function "
                     "Lambda_f) pairs with nothing multiplicative.  "
                     "NON_DIRECTED_NUMERIC corroboration of (i): " +
                     numerics["off_line_zero"]),
            citation=(dh1936 + "; " + cn_density)),
    }

    mechanisms = {
        "EULER_PRODUCT": cell(
            "FAILS", "REFUTED_BY_WITNESS",
            witness=("absent, and exactly refuted: a_6 - a_2 a_3 = 1 + "
                     "kappa^2 != 0 (Norm_{K/Q} = 6400); the proved formal "
                     "lemma (L1 witness) upgrades the single triple to "
                     "the nonexistence of ANY unital Euler product over "
                     "the rational primes.  This absence is the designed "
                     "point of the world"),
            citation=dh1936),
        "DUALITY_FE": cell(
            "HOLDS", "PROVED_HERE",
            witness=("supplied by construction: f is the exact solution "
                     "of the self-duality eigenvalue problem on the "
                     "2-dim space spanned by the two odd-character "
                     "L-functions mod 5 — alpha/beta ratio solved and "
                     "verified symbolically in Q(zeta_20) (alpha eps = "
                     "beta, beta epsbar = alpha, eps epsbar = 1), on top "
                     "of the imported classical FE of L(s,chi), "
                     "L(s,chibar).  This is the isolated-mechanism row: "
                     "duality WITHOUT Euler product (complement of "
                     "'beurling': Euler product without duality)"),
            citation=fe_import),
        "TRACE_FORMULA": cell(
            "OPEN", "OPEN",
            witness=("no Euler product => no prime side: -f'/f is not a "
                     "Dirichlet series supported on prime powers, so no "
                     "explicit-formula/trace identity pairing zeros "
                     "against arithmetic data exists in any known form.  "
                     "The analytic zero side alone (Hadamard factorization "
                     "of the entire order-1 completed function, zero-"
                     "counting N_f(T)) survives; a trace-formula "
                     "structure for f is unknown, and nonexistence in "
                     "every conceivable pairing is not proved — OPEN"),
            citation=""),
        "POSITIVITY_PURITY": cell(
            "FAILS", "IMPORTED_THEOREM",
            witness=("no positivity/purity mechanism exists for f, and "
                     "none CAN: the RH analogue is FALSE for f (off-line "
                     "zeros, imported), so any candidate positivity "
                     "mechanism would prove a falsehood.  The exact "
                     "weight-0 purity of the coefficient COLUMNS (all "
                     "column inverse roots on |T| = 1, certified by the "
                     "detector) is vacuous for positivity — purity "
                     "without multiplicativity supplies nothing.  This is "
                     "the sharpest mechanism lesson of the row: DUALITY "
                     "ALONE (a perfect self-dual FE with conductor, "
                     "gamma, and root number +1) does NOT constrain zeros "
                     "to the line"),
            citation=(dh1936 + "; " + cn_density)),
        "TENSOR_OPS": cell(
            "OPEN", "OPEN",
            witness=("no local data, hence no tensor/Rankin-Selberg "
                     "calculus for f itself; the ambient 2-dim space is "
                     "closed under termwise character twist (see L7) but "
                     "carries no known tensor structure; nonexistence "
                     "not proved — OPEN"),
            citation=""),
        "FAMILY": cell(
            "HOLDS", "PROVED_HERE",
            witness=("f sits in the explicit 2-parameter family {a "
                     "L(s,chi) + b L(s,chibar)}: the family's root-number "
                     "eigenline decomposition is computed exactly here "
                     "(w = +1 line through f; w = -1 line with constant "
                     "kappa_- = sigma_9(kappa), kappa kappa_- = -1).  "
                     "Family membership supplies NO rigidity: generic "
                     "members (and f itself) violate the RH analogue "
                     "(imported: Davenport-Heilbronn; context: "
                     "Bombieri-Hejhal on linear combinations of Euler "
                     "products, citation-needed) — an anti-rigid family, "
                     "like the Beurling class row"),
            citation=(dh1936 + "; " + cn_density)),
    }

    critical_line = {
        "status": "FALSE",
        "detail": (
            "the RH analogue for f is FALSE: f has infinitely many zeros "
            "with Re s > 1 (Davenport-Heilbronn 1936, imported theorem), "
            "and zeros in the open critical strip off the line 1/2 < "
            "Re s < 1 (imported; density work citation-needed).  f also "
            "has infinitely many zeros ON Re s = 1/2 (imported, "
            "citation-needed: Karatsuba-era results for DH-type series) — "
            "the line is populated but not exclusive.  Everything exact "
            "in this record (FE, constant, non-multiplicativity) is "
            "consistent with and explanatory of this: duality holds, "
            "Euler product fails, zeros stray"),
        "rigor": "IMPORTED_THEOREM",
        "citation": (dh1936 + "; " + cn_density + "; CITATION-NEEDED: "
                     "A. A. Karatsuba (~1980s-1990s), lower bounds for "
                     "zeros of Davenport-Heilbronn-type series on the "
                     "critical line; CITATION-NEEDED: R. Spira (~1960s-"
                     "1970s), numerical zero computations for the "
                     "Davenport-Heilbronn function (source of the "
                     "numeric seed used here)"),
        "witness": (
            "corroboration only (" + numerics["label"] + "): " +
            numerics["off_line_zero"] + " || " + numerics["fe_defect"] +
            " || " + numerics["kappa_embedding"] + ".  The FALSE status "
            "rests on the imported theorems, not on these numerics"),
    }

    world = {
        "id": "davenport_heilbronn",
        "title": "Davenport-Heilbronn function (FE without Euler product)",
        "definition": (
            "f(s) = 5^{-s} ( zeta(s,1/5) + kappa zeta(s,2/5) - kappa "
            "zeta(s,3/5) - zeta(s,4/5) ), zeta(s,a) the Hurwitz zeta, "
            "where kappa = tan(theta) is the unique real constant making "
            "f satisfy the self-dual functional equation Lambda_f(s) = "
            "Lambda_f(1-s), Lambda_f(s) = (5/pi)^{(s+1)/2} "
            "Gamma((s+1)/2) f(s).  Derived exactly here (not quoted): "
            "kappa = i(1 - eps)/(1 + eps) with eps = tau(chi)/(i sqrt5) "
            "the root number of the odd character chi mod 5, chi(2) = i; "
            "as an element of Q(zeta_20), kappa = " ),
        "arithmetic_class": (
            "linear combination of GL(1) L-functions (the two odd "
            "Dirichlet L-functions of conductor 5), coefficients in the "
            "real quartic field Q(kappa) = Q(zeta_20)^+; possesses "
            "duality/FE but NO Euler product — the designed complement "
            "of the 'beurling' row (Euler product without duality)"),
        "ladder": ladder,
        "mechanisms": mechanisms,
        "critical_line": critical_line,
        "sources": [
            "H. Davenport, H. Heilbronn (1936), on the zeros of certain "
            "Dirichlet series (I, II), J. London Math. Soc.",
            "A. Hurwitz (~1882), functional equation for zeta(s,a) at "
            "rational a / Dirichlet L-functions (classical import)",
            "H. Davenport, Multiplicative Number Theory (1967): standard "
            "exposition of the odd-character functional equation and "
            "eps(chi) = tau(chi)/(i sqrt q)",
            "E. C. Titchmarsh, The Theory of the Riemann Zeta-Function "
            "(2nd ed., rev. D. R. Heath-Brown, 1986), ch. X: context for "
            "Davenport-Heilbronn-type examples",
            "CITATION-NEEDED: E. P. Balanzario, J. Sanchez-Ortiz (~2007, "
            "Math. Comp.), zeros of the Davenport-Heilbronn "
            "counterexample in the strip",
            "CITATION-NEEDED: E. Bombieri, D. Hejhal (~1995), on the "
            "distribution of zeros of linear combinations of Euler "
            "products",
            "CITATION-NEEDED: A. A. Karatsuba (~1980s-1990s), zeros of "
            "Davenport-Heilbronn-type series on the critical line",
            "CITATION-NEEDED: A. Selberg (~1989-1992), Old and new "
            "conjectures and results about a class of Dirichlet series "
            "(the Selberg class, whose Euler-product axiom f fails)",
            "CITATION-NEEDED: R. Spira (~1960s-1970s), numerical "
            "computations of zeros of the Davenport-Heilbronn function",
        ],
        "rh_established": False,
        "notes": (
            "ROLE IN THE MATRIX: duality WITHOUT Euler product — the "
            "exact complement of the 'beurling' row (Euler product "
            "without duality).  The record's centerpiece is a reusable "
            "exact artifact: the Davenport-Heilbronn constant DERIVED "
            "from scratch in Q(zeta_20) = Q[x]/(x^8 - x^6 + x^4 - x^2 + "
            "1) with Fraction coefficients — Gauss sum tau(chi) computed "
            "exactly, tau(chi) tau(chibar) = -5 and |tau|^2 = 5 proved "
            "symbolically, root number eps = tau/(i sqrt5) unitary "
            "(eps epsbar = 1), self-duality equation alpha eps = beta "
            "solved exactly, kappa = i(alpha - beta) = "
            + vecstr(D["kappa"]) + " real irrational of degree 4 with "
            "minimal polynomial T^4 + 2T^3 - 6T^2 - 2T + 1, classical "
            "closed form proved as the identity (kappa(sqrt5 - 1) + 2)^2 "
            "= 10 - 2 sqrt5, root localized by exact Sturm in "
            "(28/100, 29/100).  L1/L2/L3/L8 FAIL by the single exact "
            "witness a_6 - a_2 a_3 = 1 + kappa^2 != 0 (Norm 6400) plus a "
            "proved formal lemma (unital Euler product => "
            "multiplicativity); statements about zeros are IMPORTED "
            "(rigor labels say which), with CITATION-NEEDED flags for "
            "the boundary audit.  Floats appear ONLY in the quarantined "
            "NON_DIRECTED_NUMERIC corroboration (60-digit mpmath: "
            "embedding value of kappa, FE defect < 1e-50 at three "
            "points, refined off-line zero near 0.8085 + 85.6993i from "
            "a literature seed).  theta itself (kappa = tan theta) is "
            "never needed: all exact work uses kappa.  "
            "rh_established=false."),
        "detector_runs": {
            "description": (
                "core.reconstruct.detect on EXACT RATIONAL column data "
                "of f (the columns live in Q + Q kappa; the canonical "
                "basis decomposition is proved exact before any run): "
                "p=2 rational component (degree 2, denominator 1 + T^2, "
                "complete degree-2 purity test HOLDS at weight (2,0)); "
                "p=2 kappa-component (honest A1 REFUSAL: not a unital "
                "series); p=11 and p=19 true columns (degrees 1, "
                "denominators 1 - T and 1 + T, all axioms HOLD).  "
                "LESSON: every column passes a purity battery, yet f "
                "has no Euler product — column-level structure does not "
                "certify global multiplicativity (a_6 != a_2 a_3)"),
            "runs": runs,
            "numeric_corroboration": numerics,
        },
    }
    # the definition string above ends mid-sentence by construction; close it
    world["definition"] += (vecstr(D["kappa"]) + " on the power basis "
                            "1, z, ..., z^7, with minimal polynomial "
                            "T^4 + 2T^3 - 6T^2 - 2T + 1 over Q "
                            "(numerically 0.28407904384..., equal to "
                            "(sqrt(10 - 2 sqrt5) - 2)/(sqrt5 - 1)).  "
                            "Coefficient-wise, f(s) = sum_n c(n) n^{-s} "
                            "with c(n) of period 5, pattern (1, kappa, "
                            "-kappa, -1, 0) on residues (1, 2, 3, 4, 0) "
                            "mod 5; equivalently f = alpha L(s,chi) + "
                            "beta L(s,chibar) with alpha = 1/(1+eps), "
                            "beta = 1 - alpha")
    return world


def main():
    D = derive_constant()
    mult_witness = refute_multiplicativity(D)
    col_witness, runs = column_structure(D)
    numerics = numeric_corroboration(D)
    world = build_world(D, mult_witness, col_witness, runs, numerics)
    probs = validate_world(world)
    assert not probs, probs
    path = save_world(world, "worlds")
    print("wrote", path)
    print("ladder:", {k: v["status"] for k, v in world["ladder"].items()})
    print("mechanisms:",
          {k: v["status"] for k, v in world["mechanisms"].items()})
    print("critical_line:", world["critical_line"]["status"])
    print("kappa =", vecstr(D["kappa"]),
          "; minpoly (low-first) =", [str(c) for c in D["minpoly"]])
    print("detector refusals:",
          [r["verdict"]["refusal"] for r in runs])


if __name__ == "__main__":
    main()
