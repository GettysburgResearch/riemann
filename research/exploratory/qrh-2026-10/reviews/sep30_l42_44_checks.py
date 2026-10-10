#!/usr/bin/env python3
"""
sep30_l42_44_checks.py -- exact finite checks for Lemmas 4.2, 4.3 and 4.4 of the external,
unreviewed OpenAI manuscript "The Quasi-Riemann Hypothesis" (30 Sep 2026), paper.tex at pr908,
sha256 42a5ee0f...6a3:

  Lemma 4.2 (prime Gauss identities, TeX 766-836)
  Lemma 4.3 (quadratic four-term formula, TeX 841-932)
  Lemma 4.4 (sextic reciprocity and the fixed Gauss phase, TeX 934-1052)

Conventions follow the manuscript (TeX 562-646) and a2/eis.py (imported unchanged):
O = Z[omega]; primary = 1 mod 3; e(z) = exp(4 pi i Im z / sqrt 3); chi_p(a) = sixth root of
unity == a^{(Np-1)/6} mod p; chi_c = prod chi_p^{v_p(c)}; gamma_j(c) = Nc^{-1/2} sum_v chi_c(v)^j e(v/c).

Labels.
  EXACT        integer arithmetic in O, or in O[zeta_M] = Z[omega][x]/(Phi_M) (M prime to 3),
               or in Z[zeta_N]; equality is tested by reduction modulo Phi_M (no floating point).
  EXACT+GAUSS  as EXACT, but it also uses Gauss's classical evaluation of the rational quadratic
               Gauss sum sum_{x mod N} exp(2 pi i x^2/N) = sqrt N (N = 1 mod 4) or i sqrt N
               (N = 3 mod 4), N odd. That theorem is imported, not re-proved.
  SYMBOLIC     sympy identity.
  FLOAT        ordinary double precision (FLOATING_RECONNAISSANCE; not directed, not certified).
  CONTROL      a deliberately wrong variant that MUST fail; it "passes" when it fails as predicted.

Every Gauss sum is multiplied by a power of sqrt(N) so that it lies in O[zeta_M]: tau_j(c) =
sum_v chi_c(v)^j e(v/c) = sqrt(Nc) gamma_j(c), and S(c) = sum_{x mod c} e(x^2/c) = |c| Gamma(c).

Run:  nice -n 10 python3 -I sep30_l42_44_checks.py [out.json]
"""
import json
import math
import os
import random
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "a2"))
import eis as E  # noqa: E402

RES = []
OUT = {}
UA = np.array([u[0] for u in E.UNITS], dtype=np.int64)   # zeta6^k = UA[k] + UB[k] omega
UB = np.array([u[1] for u in E.UNITS], dtype=np.int64)
ZERO = 6                                                  # code for a zero symbol value

XA = int(os.environ.get("XA", 1500))      # Lemma 4.2: split primes N <= XA
QA = int(os.environ.get("QA", 47))        # Lemma 4.2: inert primes q <= QA
XB = int(os.environ.get("XB", 1200))      # Lemma 4.3: all odd c with N <= XB
XC = int(os.environ.get("XC", 1200))      # Lemma 4.4: squarefree primary c with N <= XC
XR = int(os.environ.get("XR", 10000))     # Lemma 4.4: prime pairs with N <= XR
XS = int(os.environ.get("XS", 20000))     # supplements at primes with N <= XS
XP = int(os.environ.get("XP", 3000))      # supplements on all primary ideals (powers incl.) N <= XP


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    sys.stdout.flush()


def control(name, nfail, ntot, expect=None, detail=""):
    """A control passes when the wrong variant fails (nfail > 0), and, if `expect` is given,
    fails on exactly the predicted number of cases."""
    ok = nfail > 0 and (expect is None or nfail == expect)
    d = f"wrong variant fails on {nfail}/{ntot}" + (f" (predicted {expect})" if expect is not None else "")
    check("CONTROL " + name, ok, d + ((" " + detail) if detail else ""))


# =============================================================================================
# O arithmetic (vectorized), residues, primes
# =============================================================================================
def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


class Mod:
    """Residues of O modulo n: nO has HNF basis (d1, 0), (w0, g); residue i + j omega with
    0 <= i < d1, 0 <= j < g has flat index j*d1 + i (the same system as eis.residues)."""

    def __init__(self, n):
        a1, b1 = n
        a2, b2 = E.mul(n, (0, 1))
        N = abs(a1 * b2 - a2 * b1)
        g, x, y = egcd(b1, b2)
        self.n, self.N, self.g, self.d1 = n, N, g, N // g
        self.w0 = x * a1 + y * a2
        assert N == E.norm(n) and self.d1 * g == N

    def idx(self, z0, z1):
        z0 = np.asarray(z0, dtype=np.int64)
        z1 = np.asarray(z1, dtype=np.int64)
        j = z1 % self.g
        t = (z1 - j) // self.g
        i = (z0 - t * self.w0) % self.d1
        return j * self.d1 + i

    def residues(self):
        r = np.arange(self.N, dtype=np.int64)
        return r % self.d1, r // self.d1


def vmul(c, z0, z1):
    a, b = c
    return a * z0 - b * z1, a * z1 + b * z0 - b * z1


def dcoef(z0, z1, n):
    """omega-coefficient of z conj(n): e(z/n) = exp(2 pi i d / N(n))."""
    c = E.conj(n)
    return z0 * c[1] + z1 * c[0] - z1 * c[1]


def emul(*xs):
    r = (1, 0)
    for x in xs:
        r = E.mul(r, x)
    return r


def epow(x, k):
    r = (1, 0)
    for _ in range(k):
        r = E.mul(r, x)
    return r


def sieve(X):
    s = np.ones(X + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(X ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return [int(v) for v in np.nonzero(s)[0]]


def prime_elems(X):
    """Primary prime elements prime to 6 with norm <= X: dicts gen, N, ell, kind."""
    out = []
    for ell in sieve(X):
        if ell % 3 == 1:
            ab = None
            for b in range(1, int(2 * math.sqrt(ell / 3)) + 3):
                disc = 4 * ell - 3 * b * b
                if disc < 0:
                    break
                s = math.isqrt(disc)
                if s * s == disc and (b + s) % 2 == 0:
                    ab = ((b + s) // 2, b)
                    break
            assert ab and E.norm(ab) == ell
            for g in {E.primary(ab), E.primary(E.conj(ab))}:
                out.append(dict(gen=g, N=ell, ell=ell, kind="split"))
        elif ell % 3 == 2 and ell != 2 and ell * ell <= X:
            out.append(dict(gen=E.primary((ell, 0)), N=ell * ell, ell=ell, kind="inert"))
    out.sort(key=lambda P: (P["N"], P["gen"]))
    return out


def primitive_root(ell):
    fs = [f for f in sieve(int(math.isqrt(ell - 1)) + 1) if (ell - 1) % f == 0]
    m = ell - 1
    for f in list(fs):
        while m % f == 0:
            m //= f
    if m > 1:
        fs.append(m)
    for g in range(2, ell):
        if all(pow(g, (ell - 1) // f, ell) != 1 for f in fs):
            return g
    raise RuntimeError


_TAB = {}


def sym_table(P):
    """codes (int8) of chi_p on the canonical residues of O/p, ZERO at 0. Split primes use one
    eis.sym_prime value at a primitive root and the discrete log; inert primes call eis.sym_prime
    on every residue. Validated against eis.sym_prime in part 0."""
    p = P["gen"]
    if p in _TAB:
        return _TAB[p]
    m = Mod(p)
    T = np.full(m.N, ZERO, dtype=np.int8)
    if P["kind"] == "split":
        ell = P["ell"]
        assert m.g == 1 and m.d1 == ell
        g = primitive_root(ell)
        k0 = E.sym_prime((g, 0), p)
        x = 1
        for t in range(ell - 1):
            T[x] = (k0 * t) % 6
            x = (x * g) % ell
    else:
        z0, z1 = m.residues()
        for i in range(1, m.N):
            T[i] = E.sym_prime((int(z0[i]), int(z1[i])), p)
    _TAB[p] = (m, T)
    return m, T


def code_at(P, z):
    m, T = sym_table(P)
    return int(T[int(m.idx(z[0], z[1]))])


# =============================================================================================
# O[zeta_M]: arrays of shape (2, M) (coefficients of 1 and omega at zeta_M^k)
# =============================================================================================
def cyc_conv(a, b, M):
    assert int(np.abs(a).max(initial=0)) * int(np.abs(b).max(initial=0)) * M < 2 ** 62
    full = np.convolve(a, b)
    out = full[:M].copy()
    out[:len(full) - M] += full[M:]
    return out


def omul(A, B, M):
    c00 = cyc_conv(A[0], B[0], M)
    c11 = cyc_conv(A[1], B[1], M)
    c01 = cyc_conv(A[0], B[1], M) + cyc_conv(A[1], B[0], M)
    return np.stack([c00 - c11, c01 - c11])


def oscal(z, A):
    a, b = z
    return np.stack([a * A[0] - b * A[1], a * A[1] + b * A[0] - b * A[1]])


def oconj(A):
    idx = (-np.arange(A.shape[1])) % A.shape[1]
    return np.stack([A[0][idx] - A[1][idx], -A[1][idx]])


def oconst(z, M):
    A = np.zeros((2, M), dtype=np.int64)
    A[0, 0], A[1, 0] = z
    return A


def embed(A, Msmall, Mbig):
    assert Mbig % Msmall == 0
    B = np.zeros((2, Mbig), dtype=np.int64)
    B[:, np.arange(Msmall) * (Mbig // Msmall)] = A
    return B


_RED = {}
_PRIME_CACHE = {}


def is_prime(n):
    if n not in _PRIME_CACHE:
        _PRIME_CACHE[n] = n > 1 and all(n % d for d in range(2, int(math.isqrt(n)) + 1))
    return _PRIME_CACHE[n]


def red_matrix(M):
    if M in _RED:
        return _RED[M]
    if len(_RED) > 4:
        _RED.clear()
    import sympy
    x = sympy.Symbol("x")
    phi = np.array([int(c) for c in sympy.Poly(sympy.cyclotomic_poly(M, x), x).all_coeffs()][::-1],
                   dtype=np.int64)
    deg = len(phi) - 1
    R = np.zeros((M, deg), dtype=np.int64)
    R[:deg, :deg] = np.eye(deg, dtype=np.int64)
    for k in range(deg, M):
        prev = R[k - 1]
        row = np.zeros(deg, dtype=np.int64)
        row[1:] = prev[:-1]
        row -= prev[-1] * phi[:deg]
        R[k] = row
    assert int(np.abs(R).max()) < 2 ** 24
    _RED[M] = R
    return R


def zvec_is_zero(v, M):
    """v in Z^M represents sum v_k zeta_M^k; test v(zeta_M) = 0 exactly."""
    v = np.asarray(v, dtype=np.int64)
    if M == 1:
        return int(v[0]) == 0
    if is_prime(M):
        return bool((v == v[0]).all())
    R = red_matrix(M)
    assert int(np.abs(v).max(initial=0)) * int(np.abs(R).max()) * M < 2 ** 62
    return bool((v @ R == 0).all())


def o_is_zero(A, M):
    """O[zeta_M] with 3 not dividing M: O tensor Z[zeta_M], test componentwise."""
    assert M % 3 != 0
    return zvec_is_zero(A[0], M) and zvec_is_zero(A[1], M)


def o_eq(A, B, M):
    return o_is_zero(A - B, M)


# =============================================================================================
# closed forms (Lemma 4.3): Gamma(c) in {1, i, -i} as quarter-turn exponent mod 4
# =============================================================================================
IPOW = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def two_gamma(c):
    """2 Gamma(c) = 1 + i^{-b} + i^a + i^{b-a} as a Gaussian integer (re, im)."""
    a, b = c
    t = [IPOW[0], IPOW[(-b) % 4], IPOW[a % 4], IPOW[(b - a) % 4]]
    return (sum(x[0] for x in t), sum(x[1] for x in t))


def gamma_q(c):
    """Gamma(c) = i^k for odd c: return k (mod 4); assert 2Gamma is 2 i^k."""
    tg = two_gamma(c)
    for k in range(4):
        if tg == (2 * IPOW[k][0], 2 * IPOW[k][1]):
            return k
    raise AssertionError(("Gamma not a unit", c, tg))


def r_code(a, b):
    """r(a,b) = Gamma(ab)/(Gamma(a)Gamma(b)) as 0 (+1) or 1 (-1)."""
    k = (gamma_q(E.mul(a, b)) - gamma_q(a) - gamma_q(b)) % 4
    assert k in (0, 2), (a, b, k)
    return k // 2


def mod2_cube_code(c):
    """the cube root of unity congruent to c mod 2 (c odd), as a zeta6 code: 1->0, omega->2, omega^2->4."""
    return {(1, 0): 0, (0, 1): 2, (1, 1): 4}[(c[0] % 2, c[1] % 2)]


def is_odd(c):
    return not (c[0] % 2 == 0 and c[1] % 2 == 0)


# =============================================================================================
# part 0: infrastructure validation
# =============================================================================================
def part0(PR):
    print("== part 0: infrastructure ==", flush=True)
    small = {P["gen"] for P in PR if P["N"] <= 400}
    check("0.1 prime list (N<=400) equals eis.primes_upto(400)", small == set(E.primes_upto(400)),
          f"{len(small)} primes")
    rng = random.Random(1)
    bad = tested = 0
    for P in PR:
        m, T = sym_table(P)
        z0, z1 = m.residues()
        idxs = range(m.N) if P["N"] <= 400 else rng.sample(range(m.N), 25)
        for i in idxs:
            k = E.sym_prime((int(z0[i]), int(z1[i])), P["gen"])
            bad += (ZERO if k is None else k) != int(T[i])
            tested += 1
    check("0.2 symbol tables agree with eis.sym_prime (direct a^{(N-1)/6} mod p)", bad == 0,
          f"{tested} values over {len(PR)} primes (all residues for N<=400, 25 random otherwise)")
    # residue systems agree with eis.residues
    bad = 0
    for n in [(5, 3), (-5, 0), (7, 0), (1, 3), (4, 3), (-2, 3), (13, 9), (7, 3)]:
        R, N = E.residues(n)
        m = Mod(n)
        z0, z1 = m.residues()
        bad += sorted(R) != sorted(zip(z0.tolist(), z1.tolist()))
        bad += len(set(m.idx(z0, z1).tolist())) != N
    check("0.3 residue systems agree with eis.residues; idx is a bijection", bad == 0)
    # cyclotomic zero test sanity: 1 + z + ... + z^{M-1} = 0, sum over primitive roots = mu(M)
    ok = True
    for M in [5, 7, 9, 15, 21, 25, 35, 45, 49, 63, 105]:
        ok &= zvec_is_zero(np.ones(M, dtype=np.int64), M)
        v = np.zeros(M, dtype=np.int64)
        v[1] = 1
        ok &= not zvec_is_zero(v, M)
    check("0.4 cyclotomic zero test (geometric sums vanish, zeta != 0)", ok)


# =============================================================================================
# part A: Lemma 4.2 at single primes
# =============================================================================================
def tau_vectors(P, gen=None, flip=False):
    """tau_j(p) = sum_x H(x)^j e(x/gen) in O[zeta_M], j = 0..5 (gen defaults to the primary p)."""
    p = P["gen"]
    m, T = sym_table(P)
    gen = gen or p
    z0, z1 = m.residues()
    d = dcoef(z0, z1, gen) % m.N
    g = math.gcd(m.N, int(np.gcd.reduce(d)))
    M = m.N // g
    ex = d // g
    nz = T != ZERO
    taus = {}
    for j in range(6):
        k = ((-1 if flip else 1) * j * T[nz].astype(np.int64)) % 6
        A = np.zeros((2, M), dtype=np.int64)
        np.add.at(A[0], ex[nz], UA[k])
        np.add.at(A[1], ex[nz], UB[k])
        taus[j] = A
    return taus, M


def part_A(PR):
    print(f"== part A: Lemma 4.2 (split N<={XA}, inert q<={QA}) ==", flush=True)
    t0 = time.time()
    plist = [P for P in PR if (P["kind"] == "split" and P["N"] <= XA) or
             (P["kind"] == "inert" and P["ell"] <= QA)]
    fails = {k: 0 for k in ["A1", "A2", "A3", "A4a", "A4b", "A5a", "A5b", "A5c", "A5d", "A6a", "A6b", "A6c", "A7"]}
    ctrl = dict(nonprimary=0, nonprimary_tot=0, nobar=0, nobar_pred=0, flip=0, flip_pred=0)
    for P in plist:
        p, N = P["gen"], P["N"]
        m, T = sym_table(P)
        taus, M = tau_vectors(P)
        NN = oconst((N, 0), M)
        # A1: |gamma_j| = 1 for j = 1..5: tau_j conj(tau_j) = N
        for j in range(1, 6):
            fails["A1"] += not o_eq(omul(taus[j], oconj(taus[j]), M), NN, M)
        # A2: gamma_2^3 = -alpha(p): tau_2^3 = -p N
        t2_3 = omul(omul(taus[2], taus[2], M), taus[2], M)
        fails["A2"] += not o_eq(t2_3, oconst(E.mul((-N, 0), p), M), M)
        # A3: gamma_1 gamma_2 = conj(H(4)) gamma_3 gamma_2^3: N tau_1 tau_2 = conj(H(4)) tau_3 tau_2^3
        h4 = code_at(P, (4, 0))
        lhs = N * omul(taus[1], taus[2], M)
        rhs3 = omul(taus[3], t2_3, M)
        fails["A3"] += not o_eq(lhs, oscal(E.UNITS[(-h4) % 6], rhs3), M)
        # controls on A3 (bar dropped) and on A2 (non-primary generator, flipped orientation)
        if h4 != 0:
            ctrl["nobar_pred"] += 1
        ctrl["nobar"] += not o_eq(lhs, oscal(E.UNITS[h4], rhs3), M)
        for u in E.UNITS[1:]:
            up = E.mul(u, p)
            tu, Mu = tau_vectors(P, gen=up)
            ctrl["nonprimary_tot"] += 1
            ctrl["nonprimary"] += not o_eq(omul(omul(tu[2], tu[2], Mu), tu[2], Mu),
                                           oconst(E.mul((-N, 0), up), Mu), Mu)
        tf, Mf = tau_vectors(P, flip=True)
        ctrl["flip_pred"] += P["kind"] == "split"
        ctrl["flip"] += not o_eq(omul(omul(tf[2], tf[2], Mf), tf[2], Mf), oconst(E.mul((-N, 0), p), Mf), Mf)
        # A4: tau(A) tau(conj A) = A(-1) N; Gauss-Jacobi tau_a tau_b = J(H^a,H^b) tau_{a+b}
        z0, z1 = m.residues()
        c1 = T.astype(np.int64)
        c2 = T[m.idx(1 - z0, -z1)].astype(np.int64)            # code of 1 - x
        hm1 = code_at(P, (-1, 0))
        for j in range(1, 6):
            sgn = E.UNITS[(j * hm1) % 6]
            fails["A4a"] += not o_eq(omul(taus[j], taus[6 - j], M), oconst(E.mul(sgn, (N, 0)), M), M)
        both = (c1 != ZERO) & (c2 != ZERO)

        def J(a, b):
            k = (a * c1[both] + b * c2[both]) % 6
            return (int(UA[k].sum()), int(UB[k].sum()))
        for a in range(1, 6):
            for b in range(1, 6):
                if (a + b) % 6 == 0:
                    continue
                fails["A4b"] += not o_eq(omul(taus[a], taus[b], M), oscal(J(a, b), taus[(a + b) % 6]), M)
        # A5: J(H,H^3) = H(4) J(H,H); J(H^2,H^2) = -p; |J|^2 = N; J(H^2,H^2) = -1 mod 3
        J11, J13, J22 = J(1, 1), J(1, 3), J(2, 2)
        fails["A5a"] += J13 != E.mul(E.UNITS[h4], J11)
        fails["A5b"] += J22 != (-p[0], -p[1])
        fails["A5c"] += E.norm(J22) != N or E.norm(J11) != N
        fails["A5d"] += not ((J22[0] + 1) % 3 == 0 and J22[1] % 3 == 0)
        # A6: #{x: 4x(1-x) = y} = 1 + H^3(1-y); H^2(-1) = 1; prod_{x != 0,1} x(1-x) = 1; sum j_x = 0 mod 3
        f0, f1 = (z0 * (1 - z0) - (z1 * (-z1)), z0 * (-z1) + z1 * (1 - z0) - z1 * (-z1))  # x(1-x)
        y0, y1 = 4 * f0, 4 * f1
        cnt = np.bincount(m.idx(y0, y1), minlength=m.N)
        c1my = T[m.idx(1 - z0, -z1)].astype(np.int64)                 # code of 1 - y, y = residue
        h3 = np.where(c1my == ZERO, 0, np.where(c1my % 2 == 0, 1, -1))
        fails["A6a"] += not np.array_equal(cnt, 1 + h3)
        fails["A6b"] += (2 * hm1) % 6 != 0
        prod = (1, 0)
        sj = 0
        for i in range(m.N):
            if c1[i] == ZERO or c2[i] == ZERO:
                continue
            prod = E.reduce_mod(E.mul(prod, (int(f0[i]), int(f1[i]))), p)
            sj += ((2 * (c1[i] + c2[i])) % 6) // 2
        fails["A6c"] += not (E.divides(p, (prod[0] - 1, prod[1])) and sj % 3 == 0)
        # A7 (Lemma 4.4 proof, first display): Gamma(p) = gamma_3(p) and sum e(u x^2/p) = chi_p(u)^3 sum e(x^2/p)
        for u in [(1, 0), (-1, 0), (0, 1), (2, 0), (1, 2), (3, 1), (5, -2)]:
            if E.divides(p, u):
                continue
            s0, s1 = vmul(u, *(z0 * z0 - z1 * z1, 2 * z0 * z1 - z1 * z1))
            d = dcoef(s0, s1, p) % m.N
            g = m.N // M
            S = np.zeros((2, M), dtype=np.int64)
            np.add.at(S[0], d // g, 1)
            ku = code_at(P, u)
            fails["A7"] += not o_eq(S, oscal(E.UNITS[(3 * ku) % 6], taus[3]), M)
    n_split = sum(P["kind"] == "split" for P in plist)
    n_inert = len(plist) - n_split
    desc = f"{len(plist)} primes ({n_split} split, {n_inert} inert)"
    check("A1 |gamma_j(p)|=1, j=1..5: tau_j conj(tau_j) = N p [EXACT]", fails["A1"] == 0, desc)
    check("A2 gamma_2(p)^3 = -alpha(p): tau_2^3 = -p N p [EXACT]", fails["A2"] == 0, desc)
    check("A3 gamma_1 gamma_2 = conj(H(4)) gamma_3 gamma_2^3 [EXACT]", fails["A3"] == 0, desc)
    check("A4a tau(H^j) tau(H^-j) = H^j(-1) N, j=1..5 [EXACT]", fails["A4a"] == 0)
    check("A4b Gauss-Jacobi tau_a tau_b = J(H^a,H^b) tau_{a+b}, all 20 pairs a+b != 0 mod 6 [EXACT]",
          fails["A4b"] == 0)
    check("A5a J(H,H^3) = H(4) J(H,H) in O [EXACT]", fails["A5a"] == 0)
    check("A5b J(H^2,H^2) = -p (primary p) in O [EXACT]", fails["A5b"] == 0)
    check("A5c |J(H,H)|^2 = |J(H^2,H^2)|^2 = N p [EXACT]", fails["A5c"] == 0)
    check("A5d J(H^2,H^2) = -1 mod 3 [EXACT]", fails["A5d"] == 0)
    check("A6a #{x: 4x(1-x)=y} = 1 + H^3(1-y) for every y [EXACT]", fails["A6a"] == 0)
    check("A6b H^2(-1) = 1 [EXACT]", fails["A6b"] == 0)
    check("A6c prod_{x!=0,1} x(1-x) = 1 mod p and sum j_x = 0 mod 3 [EXACT]", fails["A6c"] == 0)
    check("A7 sum_x e(u x^2/p) = chi_p(u)^3 tau_3(p) (u = 1 gives Gamma(p) = gamma_3(p)) [EXACT]",
          fails["A7"] == 0, "7 multipliers u")
    control("A-c1 non-primary generator u p (u != 1): gamma_2(up)^3 = -alpha(up)", ctrl["nonprimary"],
            ctrl["nonprimary_tot"], expect=ctrl["nonprimary_tot"])
    control("A-c2 bar dropped on H(4) in A3", ctrl["nobar"], len(plist), expect=ctrl["nobar_pred"],
            detail="(predicted: primes with H(4) != 1)")
    control("A-c3 orientation flipped (H -> conj H) in A2", ctrl["flip"], len(plist), expect=ctrl["flip_pred"],
            detail="(predicted: split primes; inert p = conj p)")
    OUT["A"] = dict(primes=len(plist), split=n_split, inert=n_inert, XA=XA, QA=QA, fails=fails,
                    controls=ctrl, seconds=round(time.time() - t0, 1))


# =============================================================================================
# part B: Lemma 4.3
# =============================================================================================
def part_B(PR):
    print(f"== part B: Lemma 4.3 (all odd c with N <= {XB}) ==", flush=True)
    t0 = time.time()
    elems = []
    bmax = int(2 * math.sqrt(XB / 3)) + 2
    for b in range(-bmax, bmax + 1):
        for a in range(-2 * bmax - 2, 2 * bmax + 3):
            N = a * a - a * b + b * b
            if 0 < N <= XB and is_odd((a, b)):
                elems.append((a, b))
    elems.sort(key=lambda c: (E.norm(c), c))
    # prime elements for square-freeness labels: lambda, and all good primes
    lam = (1, 2)
    plist = [lam] + [P["gen"] for P in PR if P["N"] <= XB]
    stats = dict(elements=len(elems), non_primary=0, lambda_div=0, nonsquarefree=0, prime_power_k2=0,
                 rational=0)
    fa = fb = 0
    ctrl_sign = 0
    gauss_ratio_bad = 0
    gamma_by_mod2 = {}
    curN, gN = None, None
    for c in elems:
        N = E.norm(c)
        if N != curN:
            curN = N
            gN = np.bincount((np.arange(N, dtype=np.int64) ** 2) % N, minlength=N)
        stats["non_primary"] += not E.is_primary(c)
        stats["lambda_div"] += E.divides(lam, c)
        stats["rational"] += c[1] == 0
        sq = False
        pp = False
        for q in plist:
            nq = E.norm(q)
            if nq * nq > N:
                break
            if E.divides(E.mul(q, q), c):
                sq = True
                # prime power: c = unit * q^k, k >= 2
                k, t = 0, c
                while E.divides(q, t):
                    t = E.mul(t, E.conj(q))
                    t = (t[0] // nq, t[1] // nq)
                    k += 1
                pp |= E.norm(t) == 1
        stats["nonsquarefree"] += sq
        stats["prime_power_k2"] += pp
        m = Mod(c)
        z0, z1 = m.residues()
        d = dcoef(z0 * z0 - z1 * z1, 2 * z0 * z1 - z1 * z1, c) % N
        S = np.bincount(d, minlength=N).astype(np.int64)
        k = gamma_q(c)                                     # Gamma = i^k, k in {0,1,3}
        gamma_by_mod2.setdefault((c[0] % 2, c[1] % 2), set()).add(k)
        # B1a: S^2 = Gamma^2 N  (import-free)
        S2 = cyc_conv(S, S, N)
        S2[0] -= (1 if k % 2 == 0 else -1) * N
        fa += not zvec_is_zero(S2, N)
        # B1b: S = (Gamma/eps_N) g_N, eps_N = 1 or i (Gauss)
        eps = 0 if N % 4 == 1 else 1
        ratio = (k - eps) % 4
        if ratio not in (0, 2):
            gauss_ratio_bad += 1
            fb += 1
            continue
        s = 1 if ratio == 0 else -1
        fb += not zvec_is_zero(S - s * gN, N)
        ctrl_sign += not zvec_is_zero(S + s * gN, N)
    check("B1a S(c)^2 = Gamma(c)^2 N(c) for the four-term Gamma, all odd c [EXACT, import-free]",
          fa == 0, f"{len(elems)} odd c; " + ", ".join(f"{k} {v}" for k, v in stats.items() if k != "elements"))
    check("B1b S(c) = |c| Gamma(c) with the sign, all odd c [EXACT+GAUSS]", fb == 0 and gauss_ratio_bad == 0,
          "Gamma/eps_N is +-1 in every case" if gauss_ratio_bad == 0 else f"ratio not real: {gauss_ratio_bad}")
    control("B-c1 opposite sign S = -|c| Gamma(c)", ctrl_sign, len(elems), expect=len(elems))
    vals = sorted(gamma_by_mod2.items())
    nconst = sum(len(v) > 1 for _, v in vals)
    control("B-c2 'Gamma depends only on c mod 2' (classes mod 2 with >1 value)", nconst, len(vals))
    # variant closed form with i^{+b} in place of i^{-b}
    bad_var = 0
    for c in elems:
        a, b = c
        t = [IPOW[0], IPOW[b % 4], IPOW[a % 4], IPOW[(b - a) % 4]]
        tg = (sum(x[0] for x in t), sum(x[1] for x in t))
        bad_var += tg != two_gamma(c)
    control("B-c3 four-term formula with i^{+b} (differs from the stated closed form)", bad_var, len(elems))
    OUT["B1"] = dict(stats=stats, fails_a=fa, fails_b=fb, XB=XB, seconds=round(time.time() - t0, 1))


def part_B2():
    print("== part B2: square classes mod 4 (Lemma 4.3 table) [EXACT] ==", flush=True)
    U4 = [(a, b) for a in range(4) for b in range(4) if is_odd((a, b))]
    m4 = lambda z: (z[0] % 4, z[1] % 4)  # noqa: E731
    check("B2.1 units mod 4: 12 classes; odd = unit mod 4",
          len(U4) == 12 and all(any(m4(E.mul(u, v)) == (1, 0) for v in U4) for u in U4))
    sqs = {m4(E.mul(u, u)) for u in U4}
    check("B2.2 squares mod 4 = {1, omega, omega^2}; x^2 mod 4 depends on x mod 2",
          sqs == {(1, 0), (0, 1), (3, 3)} and all(m4(E.mul(u, u)) == m4(E.mul(v, v)) for u in U4 for v in U4
                                                   if (u[0] - v[0]) % 2 == 0 and (u[1] - v[1]) % 2 == 0))
    lam = (1, 2)
    reps = {}
    for e in (0, 1):
        for f in (0, 1):
            x = epow(lam, f)
            reps[(e, f)] = (-x[0], -x[1]) if e else x
    cosets = [frozenset(m4(E.mul(r, s)) for s in sqs) for r in reps.values()]
    check("B2.3 reps 1,-1,lambda,-lambda are distinct mod squares and cover; lambda^2 = -3 = 1 mod 4",
          len(set(cosets)) == 4 and set().union(*cosets) == set(U4) and m4(E.mul(lam, lam)) == (1, 0))
    check("B2.4 Gamma(c v^2) = Gamma(c) for all 12 x 12 unit classes",
          all(gamma_q(E.mul(c, E.mul(v, v))) == gamma_q(c) for c in U4 for v in U4))
    tab = [gamma_q(reps[k]) for k in [(0, 0), (1, 0), (0, 1), (1, 1)]]
    check("B2.5 Gamma table on 1, -1, lambda, -lambda = 1, 1, i, -i", tab == [0, 0, 1, 3])
    bad = 0
    for (e, f), x in reps.items():
        for (g, h), y in reps.items():
            bad += r_code(x, y) != (e * h + f * g + f * h) % 2
    check("B2.6 r((-1)^e lam^f, (-1)^g lam^h) = (-1)^{eh+fg+fh}, all 16 entries", bad == 0)
    sym = all(r_code(u, v) == r_code(v, u) for u in U4 for v in U4)
    bic = all(r_code(E.mul(u, v), w) == (r_code(u, w) + r_code(v, w)) % 2 for u in U4 for v in U4 for w in U4)
    check("B2.7 r symmetric, sign-valued bicharacter on all 12^3 unit-class triples", sym and bic)
    # parity link used in Lemma 4.4: N(c) = 3^f mod 4 on the square class (-1)^e lam^f
    par = all((E.norm(c) % 4 == 1) == (gamma_q(c) % 2 == 0) for c in U4)
    check("B2.8 N(c) = 1 mod 4 iff Gamma(c)^2 = 1 (f = 0), all 12 classes", par)
    # diagonal: r(t,t) = r(-1,t) (residue class -1) on all classes
    check("B2.9 r(t,t) = r(-1,t) for all 12 classes (Lemma 4.4 diagonal)",
          all(r_code(t, t) == r_code((-1, 0), t) for t in U4))
    # the generators alone do not force a bicharacter: an arbitrary function on 4 classes with
    # Gamma(1)=1 need not give one (shows the proof's "evaluate on the generators" needs the table)
    alt = {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 1}       # Gamma' = 1, i, i, i on 1,-1,lam,-lam

    def rr(x, y, G):
        def cls(z):
            for kk, v in reps.items():
                if m4(z) in [m4(E.mul(v, s)) for s in sqs]:
                    return kk
        k = (G[cls(E.mul(x, y))] - G[cls(x)] - G[cls(y)]) % 4
        return k
    nb = sum(rr(E.mul(u, v), w, alt) != (rr(u, w, alt) + rr(v, w, alt)) % 4 for u in reps.values()
             for v in reps.values() for w in reps.values())
    control("B2-c1 a different class function (1,i,i,i) does not give a bicharacter", nb, 64)


def part_B3():
    print("== part B3: Gaussian Fourier normalization in the proof of Lemma 4.3 [SYMBOLIC] ==", flush=True)
    import sympy as sp
    eps, R, Y1, Y2 = sp.symbols("epsilon R Y1 Y2", positive=True)
    q = R ** 2
    r = 1 + 3 * q * eps ** 2 / 16
    beta = 4 * sp.I / (sp.sqrt(3) * R)
    A = sp.Matrix([[eps, -beta], [-beta, eps]])
    ok_det = sp.simplify(A.det() - 16 * r / (3 * q)) == 0
    # integrand exp(-pi w^T A w + b^T w), b = -(4 pi i/sqrt3) (Y2, Y1) (Y = e^{i theta/2} y rotated)
    bvec = -(4 * sp.pi * sp.I / sp.sqrt(3)) * sp.Matrix([Y2, Y1])
    expo = sp.simplify((bvec.T * A.inv() * bvec)[0, 0] / (4 * sp.pi))
    # claimed: -pi eps q |y|^2/(4r) - (4 pi i/sqrt3) Im(c y^2)/(4r), Im(c y^2) = R Im(Y^2) = 2 R Y1 Y2
    claim = -sp.pi * eps * q * (Y1 ** 2 + Y2 ** 2) / (4 * r) - (4 * sp.pi * sp.I / sp.sqrt(3)) * (2 * R * Y1 * Y2) / (4 * r)
    ok_exp = sp.simplify(expo - claim) == 0
    amp = (2 / sp.sqrt(3)) / sp.sqrt(16 * r / (3 * q))
    ok_amp = sp.simplify(amp - R / (2 * sp.sqrt(r))) == 0
    check("B3 f_eps^(y): det = 16 r_eps/(3 q_c), amplitude |c|/(2 sqrt r), exponent as stated [SYMBOLIC]",
          ok_det and ok_exp and ok_amp, "uses the standard complex Gaussian integral (Re A > 0)")


def part_B4():
    print("== part B4: Poisson identity at finite eps [FLOAT] ==", flush=True)
    # LHS sum_z e(z^2/c) e^{-pi eps |z|^2}; RHS sum_y f^(y), f^ as in the proof
    worst = 0.0
    nctrl = ncase = 0
    nreal = 0
    for c in [(1, 0), (1, 2), (-2, 3), (5, 0), (1, 3), (4, 3), (3, 1), (2, 1)]:
        cc = complex(c[0] - c[1] / 2, c[1] * math.sqrt(3) / 2)
        qc = abs(cc) ** 2
        for eps in [0.4, 0.15, 0.06]:
            Rr = int(math.sqrt(40 / (math.pi * eps * min(1, qc / 4))) * 2) + 4
            a = np.arange(-Rr, Rr + 1)
            A_, B_ = np.meshgrid(a, a, indexing="ij")
            z = A_ - B_ / 2 + 1j * B_ * math.sqrt(3) / 2
            e = lambda w: np.exp(4j * np.pi * w.imag / math.sqrt(3))  # noqa: E731
            lhs = (e(z ** 2 / cc) * np.exp(-np.pi * eps * np.abs(z) ** 2)).sum()
            r = 1 + 3 * qc * eps ** 2 / 16
            fh = abs(cc) / (2 * math.sqrt(r)) * np.exp(-np.pi * eps * qc * np.abs(z) ** 2 / (4 * r))
            rhs = (fh * e(-cc * z ** 2 / (4 * r))).sum()
            rhs_bad = (fh * e(+cc * z ** 2 / (4 * r))).sum()
            worst = max(worst, abs(lhs - rhs) / max(1, abs(lhs)))
            ncase += 1
            nctrl += abs(lhs - rhs_bad) / max(1, abs(lhs)) > 1e-6
            nreal += abs(lhs.imag) / max(1, abs(lhs)) < 1e-9
    check("B4 Poisson identity sum f_eps = sum f_eps^ at finite eps (8 c, 3 eps) [FLOAT]", worst < 1e-9,
          f"max rel dev {worst:.1e}")
    # flipping the phase sign replaces the RHS by its complex conjugate, so it can only fail
    # when the sum is not real; predicted failures = cases with a non-real sum
    control("B4-c1 sign of the phase flipped in f^ [FLOAT]", nctrl, ncase, expect=ncase - nreal,
            detail="(predicted: cases with a non-real sum)")
    OUT["B4"] = dict(max_rel_dev=worst, ctrl_fail=nctrl, cases=ncase, real_cases=nreal)


# =============================================================================================
# part C: Lemma 4.4
# =============================================================================================
def ideals_sqf(PR, X):
    """squarefree primary good c with N <= X: (gen, N, [prime dicts])."""
    ps = [P for P in PR if P["N"] <= X]
    out = []

    def rec(start, gen, n, fac):
        for i in range(start, len(ps)):
            P = ps[i]
            if n * P["N"] > X:
                break
            g2 = E.mul(gen, P["gen"])
            out.append((g2, n * P["N"], fac + [P]))
            rec(i + 1, g2, n * P["N"], fac + [P])
    rec(0, (1, 0), 1, [])
    out.sort(key=lambda t: (t[1], t[0]))
    return out


def chi_code_fac(fac, z):
    s = 0
    for P in fac:
        k = code_at(P, z)
        if k == ZERO:
            return ZERO
        s += k
    return s % 6


def part_C1(PR):
    print(f"== part C1: complete Gauss identities (eq:signal) and CRT, squarefree primary c, N <= {XC} ==",
          flush=True)
    t0 = time.time()
    cs = ideals_sqf(PR, XC)
    cache = {}
    f = {k: 0 for k in ["i", "ii", "iii", "iv", "v", "vi", "vii"]}
    nob = nob_pred = nomu = nomu_pred = 0
    ncomp = ninert = nrat = 0
    for (c, N, fac) in cs:
        m = Mod(c)
        z0, z1 = m.residues()
        code = np.zeros(m.N, dtype=np.int64)
        zero = np.zeros(m.N, dtype=bool)
        for P in fac:
            mp, T = sym_table(P)
            kk = T[mp.idx(z0, z1)].astype(np.int64)
            zero |= kk == ZERO
            code += np.where(kk == ZERO, 0, kk)
        code %= 6
        nz = ~zero
        d = dcoef(z0, z1, c) % N
        g = math.gcd(N, int(np.gcd.reduce(d)))
        M = N // g
        ex = d // g
        tau = {}
        for j in (1, 2, 3):
            A = np.zeros((2, M), dtype=np.int64)
            k = (j * code[nz]) % 6
            np.add.at(A[0], ex[nz], UA[k])
            np.add.at(A[1], ex[nz], UB[k])
            tau[j] = A
        cache[c] = (tau, M)
        mu = (-1) ** len(fac)
        ncomp += len(fac) > 1
        ninert += any(P["kind"] == "inert" for P in fac)
        nrat += len(fac) == 2 and fac[0]["ell"] == fac[1]["ell"]
        # (i) Gamma(c) = gamma_3(c): sum_x e(x^2/c) = tau_3
        dq = dcoef(z0 * z0 - z1 * z1, 2 * z0 * z1 - z1 * z1, c) % N
        S = np.zeros((2, M), dtype=np.int64)
        np.add.at(S[0], dq // g, 1)
        f["i"] += not o_eq(S, tau[3], M)
        # (ii) gamma_2^3 = mu alpha: tau_2^3 = mu c N
        t23 = omul(omul(tau[2], tau[2], M), tau[2], M)
        f["ii"] += not o_eq(t23, oconst(E.mul((mu * N, 0), c), M), M)
        nomu_pred += mu == -1
        nomu += not o_eq(t23, oconst(E.mul((N, 0), c), M), M)
        # (iii) gamma_1 gamma_2 = mu alpha G, G = conj(chi_c(4)) gamma_3: tau_1 tau_2 = mu c conj(chi_c(4)) tau_3
        c4 = chi_code_fac(fac, (4, 0))
        t12 = omul(tau[1], tau[2], M)
        f["iii"] += not o_eq(t12, oscal(E.mul((mu, 0), E.mul(c, E.UNITS[(-c4) % 6])), tau[3]), M)
        nob_pred += c4 != 0
        nob += not o_eq(t12, oscal(E.mul((mu, 0), E.mul(c, E.UNITS[c4])), tau[3]), M)
        # (v) |gamma_j(c)| = 1 for j = 1,2,3
        for j in (1, 2, 3):
            f["v"] += not o_eq(omul(tau[j], oconj(tau[j]), M), oconst((N, 0), M), M)
        # (vi) gamma_3(c)^2 = Gamma(c)^2 for the four-term closed form; chi_c(4) = c mod 2
        k = gamma_q(c)
        f["vi"] += not o_eq(omul(tau[3], tau[3], M), oconst(((1 if k % 2 == 0 else -1) * N, 0), M), M)
        f["vii"] += c4 != mod2_cube_code(c)
        # (iv) CRT: tau_j(pb) = chi_p(b)^j chi_b(p)^j tau_j(p) tau_j(b)
        if len(fac) > 1:
            P0 = fac[0]
            p = P0["gen"]
            b = emul(*[Q["gen"] for Q in fac[1:]])
            tp, Mp = cache[p]
            tb, Mb = cache[b]
            kpb = code_at(P0, b)
            kbp = chi_code_fac(fac[1:], p)
            for j in (1, 2, 3):
                rhs = omul(embed(tp[j], Mp, M), embed(tb[j], Mb, M), M)
                f["iv"] += not o_eq(tau[j], oscal(E.UNITS[(j * (kpb + kbp)) % 6], rhs), M)
    desc = f"{len(cs)} squarefree primary c ({ncomp} composite, {ninert} with an inert factor, {nrat} = p conj(p))"
    check("C1(i) Gamma(c) = gamma_3(c): sum_x e(x^2/c) = sum_v chi_c(v)^3 e(v/c) [EXACT]", f["i"] == 0, desc)
    check("C1(ii) gamma_2(c)^3 = mu(c) alpha(c) [EXACT]", f["ii"] == 0)
    check("C1(iii) gamma_1 gamma_2 = mu alpha G, G = conj(chi_c(4)) gamma_3 [EXACT]", f["iii"] == 0)
    check("C1(iv) CRT gamma_j(ab) = chi_a(b)^j chi_b(a)^j gamma_j(a) gamma_j(b), j=1,2,3 [EXACT]",
          f["iv"] == 0, f"{ncomp} composites x 3")
    check("C1(v) |gamma_j(c)| = 1, j = 1,2,3 [EXACT]", f["v"] == 0)
    check("C1(vi) gamma_3(c)^2 = Gamma_four-term(c)^2, hence |G(c)| = 1 [EXACT]", f["vi"] == 0)
    check("C1(vii) chi_c(4) = (c mod 2) as a cube root of unity [EXACT]", f["vii"] == 0)
    control("C1-c1 G without the bar (chi_c(4) Gamma) in (iii)", nob, len(cs), expect=nob_pred,
            detail="(predicted: c with chi_c(4) != 1)")
    control("C1-c2 mu dropped in (ii)", nomu, len(cs), expect=nomu_pred, detail="(predicted: mu(c) = -1)")
    OUT["C1"] = dict(count=len(cs), composite=ncomp, inert=ninert, p_conjp=nrat, fails=f, XC=XC,
                     seconds=round(time.time() - t0, 1))


def part_C2(PR):
    print(f"== part C2: sextic reciprocity at all pairs of distinct good primes, N <= {XR} ==", flush=True)
    t0 = time.time()
    ps = [P for P in PR if P["N"] <= XR]
    n = len(ps)
    G0 = np.array([P["gen"][0] for P in ps], dtype=np.int64)
    G1 = np.array([P["gen"][1] for P in ps], dtype=np.int64)
    C = np.zeros((n, n), dtype=np.int64)
    for i, P in enumerate(ps):
        m, T = sym_table(P)
        C[i] = T[m.idx(G0, G1)]
    # class of each prime mod 4 and r from the closed-form table
    U4 = [(a, b) for a in range(4) for b in range(4) if is_odd((a, b))]
    cid = {u: k for k, u in enumerate(U4)}
    rt = np.array([[r_code(u, v) for v in U4] for u in U4], dtype=np.int64)
    cls = np.array([cid[(P["gen"][0] % 4, P["gen"][1] % 4)] for P in ps])
    Rm = rt[cls][:, cls]
    off = ~np.eye(n, dtype=bool)
    sameideal = np.zeros((n, n), dtype=bool)   # distinct primes are distinct ideals; diagonal excluded
    assert not (C[off] == ZERO).any()
    diff = (C.T - C) % 6                       # chi_q(p) - chi_p(q), (i, j) = (p, q)
    rec = (diff == 3 * Rm) & off
    cub = ((2 * diff) % 6 == 0) & off
    sgn = ((3 * (C + C.T)) % 6 == 3 * Rm) & off
    npairs = int(off.sum())
    check("C2a sextic reciprocity chi_q(p) = r(p,q) chi_p(q), all ordered pairs of distinct primes [EXACT]",
          int(rec.sum()) == npairs, f"{n} primes, {npairs} ordered pairs, {int((Rm[off] == 1).sum())} with r = -1")
    check("C2b cubic reciprocity (imported in the proof) (p/q)_3 = (q/p)_3 [EXACT]", int(cub.sum()) == npairs)
    check("C2c sign identification r(p,q) = chi_p(q)^3 chi_q(p)^3 [EXACT]", int(sgn.sum()) == npairs)
    control("C2-c1 reciprocity without the correction (R = 1)", int(((diff != 0) & off).sum()), npairs,
            expect=int((Rm[off] == 1).sum()))
    _ = sameideal
    OUT["C2"] = dict(primes=n, ordered_pairs=npairs, r_minus=int((Rm[off] == 1).sum()), XR=XR,
                     seconds=round(time.time() - t0, 1))


def part_C3(PR):
    print(f"== part C3: supplements and fixed phases at primes N <= {XS}; all primary ideals N <= {XP} ==",
          flush=True)
    t0 = time.time()
    lam = (1, 2)
    ps = [P for P in PR if P["N"] <= XS]
    f = {k: 0 for k in ["2sup", "2cub", "m1", "m1par", "Gp3", "Gp2", "Rpp", "rm1"]}
    c_ideal = c_ideal_pred = c_gbar = c_gbar_pred = 0
    sup = {}
    for P in ps:
        p, N = P["gen"], P["N"]
        k2 = E.sym_prime((2, 0), p)
        km2 = E.sym_prime((-2, 0), p)
        k4 = E.sym_prime((4, 0), p)
        km1 = E.sym_prime((-1, 0), p)
        kl = E.sym_prime(lam, p)
        kw = E.sym_prime((0, 1), p)
        sup[p] = (kl, kw)
        # 2-supplement: chi_p(4) = (2/p)_3 = (-2/p)_3 = (p/(-2))_3 = p mod 2
        f["2sup"] += not (k4 == (2 * k2) % 6 == (2 * km2) % 6 == mod2_cube_code(p))
        f["2cub"] += k4 % 2 != 0
        # unit supplement: chi_p(-1) = (-1)^{(N-1)/6}, parity equals (N-1)/2
        f["m1"] += km1 != (3 * ((N - 1) // 6)) % 6
        f["m1par"] += ((N - 1) // 6 - (N - 1) // 2) % 2 != 0
        gk = gamma_q(p)
        # Gamma(p)^2 = chi_p(-1) = R(p,p) = r(-1,p)
        f["Rpp"] += not ((gk % 2 == 0) == (km1 == 0) and r_code(p, p) == (km1 // 3) and
                         r_code((-1, 0), p) == (km1 // 3))
        # G(p^3) = Gamma(p) (closed forms; chi_{p^3}(4) = chi_p(4)^3 = 1), G(p^2) = chi_p(4)
        p2, p3 = E.mul(p, p), epow(p, 3)
        f["Gp3"] += not ((3 * k4) % 6 == 0 and gamma_q(p3) == gk)
        # G(p^2) = conj(chi_p(4))^2 Gamma(p^2) as 12th-root exponent: 2*(-k4) (zeta6 code) and Gamma(p^2)=1
        f["Gp2"] += not (gamma_q(p2) == 0 and (-2 * k4) % 6 == k4 % 6)
        c_ideal_pred += km1 == 3
        c_ideal += km1 != 0               # "R(p,p) = value at the ideal (-1)" = 1 fails when chi_p(-1) = -1
        c_gbar_pred += k4 != 0
        c_gbar += (2 * k4) % 6 != k4      # G(p^2) = conj(chi_p(4)) fails when chi_p(4) != 1
    desc = f"{len(ps)} primes"
    check("C3a 2-supplement chi_p(4) = (2/p)_3 = (-2/p)_3 = (p/(-2))_3 = p mod 2 [EXACT]", f["2sup"] == 0, desc)
    check("C3b chi_p(4) has order dividing 3 [EXACT]", f["2cub"] == 0)
    check("C3c unit supplement chi_p(-1) = (-1)^{(N-1)/6}; same parity as (N-1)/2 [EXACT]",
          f["m1"] == 0 and f["m1par"] == 0)
    check("C3d Gamma(p)^2 = chi_p(-1) = R(p,p) = r(-1,p) [EXACT]", f["Rpp"] == 0)
    check("C3e G(p^3) = Gamma(p) (= gamma_3(p) by A7) and G(p^2) = chi_p(4) [EXACT]",
          f["Gp3"] == 0 and f["Gp2"] == 0)
    control("C3-c1 diagonal read at the ideal ray class of (-1) (value 1)", c_ideal, len(ps), expect=c_ideal_pred)
    control("C3-c2 G(p^2) = conj(chi_p(4))", c_gbar, len(ps), expect=c_gbar_pred)
    # all primary good ideals with N <= XP (prime powers and nonsquarefree included)
    pp = [P for P in ps if P["N"] <= XP]
    ids = [((1, 0), 1, [])]

    def rec(start, gen, n, fac):
        for i in range(start, len(pp)):
            P = pp[i]
            if n * P["N"] > XP:
                break
            g, mm, e = gen, n, 0
            while mm * P["N"] <= XP:
                g, mm, e = E.mul(g, P["gen"]), mm * P["N"], e + 1
                ids.append((g, mm, fac + [(P, e)]))
                rec(i + 1, g, mm, fac + [(P, e)])
    rec(0, (1, 0), 1, [])
    ids = ids[1:]
    nonsq = sum(any(e > 1 for _, e in fac) for _, _, fac in ids)
    fb = {"m1": 0, "c4": 0, "Gv2": 0, "diag": 0, "Nmod4": 0}
    for (n, N, fac) in ids:
        km1 = sum(e * code_at(P, (-1, 0)) for P, e in fac) % 6
        k4 = sum(e * code_at(P, (4, 0)) for P, e in fac) % 6
        fb["m1"] += not (km1 in (0, 3) and r_code(n, n) == km1 // 3)
        fb["diag"] += r_code((-1, 0), n) != r_code(n, n)
        fb["Nmod4"] += (N % 4 == 1) != (km1 == 0)
        fb["c4"] += k4 != mod2_cube_code(n)
        n2 = E.mul(n, n)
        fb["Gv2"] += not (gamma_q(n2) == 0 and (-(2 * k4)) % 6 == k4)
    check("C3f chi_n(-1) = R(n,n) = r(-1,n) = (-1)^{(N n-1)/2} on all primary good ideals [EXACT]",
          fb["m1"] == 0 and fb["diag"] == 0 and fb["Nmod4"] == 0,
          f"{len(ids)} ideals N<={XP}, {nonsq} nonsquarefree")
    check("C3g chi_n(4) = n mod 2 and G(n^2) = chi_n(4) on all primary good ideals [EXACT]",
          fb["c4"] == 0 and fb["Gv2"] == 0)
    OUT["C3"] = dict(primes=len(ps), ideals=len(ids), nonsquarefree=nonsq, XS=XS, XP=XP,
                     seconds=round(time.time() - t0, 1))
    return sup


def part_C4():
    print("== part C4: G on the ray group mod 12 (class level) [EXACT] ==", flush=True)
    # primary classes mod 12 prime to 2  <->  units mod 4
    P12 = [(a, b) for a in range(12) for b in range(12) if a % 3 == 1 and b % 3 == 0 and is_odd((a, b))]
    U4 = sorted({(a % 4, b % 4) for a, b in P12})
    check("C4.1 primary classes mod 12 prime to 2 map bijectively onto the 12 units mod 4",
          len(P12) == 12 and len(U4) == 12)
    # ray-class argument: alpha = 1 mod 12, unit u, u*alpha*c primary with c primary => u = 1
    ok = True
    for u in E.UNITS:
        for (a, b) in P12:
            for al in [(1, 0), (13, 0), (1, 12), (-11, 24), (25, -12)]:
                y = emul(u, al, (a, b))
                if E.is_primary(y):
                    ok &= u == (1, 0) and ((y[0] - a) % 4, (y[1] - b) % 4) == (0, 0)
    check("C4.2 same ray class mod 12 + both primary => same residue mod 4", ok)

    def G12(c):   # G = conj(chi_c(4)) Gamma(c) as an exponent mod 12 (e^{2 pi i k/12})
        return (-2 * mod2_cube_code(c) + 3 * gamma_q(c)) % 12
    bad = 0
    for v in P12:
        for w in P12:
            bad += G12(E.mul(v, w)) != (G12(v) + G12(w) + 6 * r_code(v, w)) % 12
    check("C4.3 G(vw) = G(v) G(w) R(v,w) on all 144 class pairs; G(1) = 1",
          bad == 0 and G12((1, 0)) == 0)
    vals = sorted({G12(c) for c in P12})
    OUT["C4"] = dict(G_values_12ths=vals)
    print(f"   G takes the 12th-root exponents {vals}")


def part_D(PR, sup):
    print(f"== part D: cubic supplements for lambda and units mod 9 (Prop 5.1 context; N <= {XS}) [EXACT] ==",
          flush=True)
    tab = {}
    bad = 0
    for P in PR:
        if P["N"] > XS:
            continue
        p = P["gen"]
        kl, kw = sup[p]
        key = (p[0] % 9, p[1] % 9)
        val = ((2 * kl) % 6, (2 * kw) % 6)        # cubic symbols (lambda/p)_3, (omega/p)_3 as zeta6 codes
        if key in tab and tab[key] != val:
            bad += 1
        tab.setdefault(key, val)
    classes = sorted(tab)
    # homomorphism on the group of primary classes mod 9 (9 classes)
    hom = 0
    for x in classes:
        for y in classes:
            z = E.mul(x, y)
            z = (z[0] % 9, z[1] % 9)
            if z in tab:
                hom += tab[z] != ((tab[x][0] + tab[y][0]) % 6, (tab[x][1] + tab[y][1]) % 6)
    check("D1 (lambda/p)_3 and (omega/p)_3 depend only on p mod 9 and form a character on the 9 primary classes",
          bad == 0 and hom == 0 and len(classes) == 9, f"{len(classes)} classes hit")
    check("D2 (u lambda^k/p)_3 = 1 when p = 1 mod 9", tab.get((1, 0)) == (0, 0))
    OUT["D"] = dict(classes={f"{k}": v for k, v in tab.items()})


def main():
    out_path = sys.argv[1] if len(sys.argv) > 1 else None
    t0 = time.time()
    PR = prime_elems(max(XR, XS, XA, QA * QA))
    print(f"primes: {len(PR)} primary good prime elements with N <= {max(XR, XS, XA, QA * QA)}", flush=True)
    for P in PR:
        if P["N"] <= max(XR, XA, QA * QA):
            sym_table(P)
    print(f"symbol tables built ({time.time() - t0:.1f}s)", flush=True)
    part0([P for P in PR if P["N"] <= max(XR, XA, QA * QA)])
    part_A(PR)
    part_B(PR)
    part_B2()
    part_B3()
    part_B4()
    part_C1(PR)
    part_C2(PR)
    sup = part_C3(PR)
    part_C4()
    part_D(PR, sup)
    npass = sum(ok for _, ok in RES)
    print(f"\n{npass}/{len(RES)} PASS, total {time.time() - t0:.0f}s")
    OUT["results"] = RES
    OUT["params"] = dict(XA=XA, QA=QA, XB=XB, XC=XC, XR=XR, XS=XS, XP=XP)
    OUT["seconds"] = round(time.time() - t0, 1)
    if out_path:
        with open(out_path, "w") as fh:
            json.dump(OUT, fh, indent=1, default=str)
    sys.exit(0 if npass == len(RES) else 1)


if __name__ == "__main__":
    main()
