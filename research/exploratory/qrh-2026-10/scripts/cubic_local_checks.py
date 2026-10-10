"""cubic_local_checks.py -- EXACT finite checks of the n = 3 (cubic) analogues of the local
correlation lemmas, the complete-common-support allocation, the Kummer / fixed-numerator-ray
lemma and the exceptional-row ledger used by the cubic transfer of Lemma 18.1 (lem:plain) of the
external, unreviewed OpenAI manuscript "The Quasi-Riemann Hypothesis" (30 Sep 2026; pr908
paper.tex, sha256 42a5ee0f...deac6a3).  Line numbers refer to that file.  Adapted from
reviews/lemma18_support_checks.py (sextic) and reviews/lemma18_local.py.  Imports a2/eis.py
read-only (exact arithmetic in O = Z[omega]).

ARITHMETIC CLASS.  EXACT throughout.  Character values are cube roots of unity, stored as pairs
(a, b) = a + b*omega of int64 (counts of each root; no floating point).  Sums containing the
additive character e(z) = exp(2 pi i Tr(z/lambda)) are stored as integer vectors over the exponent
group Z/N (N = norm of the modulus, prime to 3) with Z[omega] coefficients and tested for zero by
reduction modulo the cyclotomic polynomial Phi_N (Q(omega) and Q(zeta_N) are linearly disjoint
since 3 does not divide N, so this test is exact).  The sympy part [L] is symbolic.

Sections (each line prints PASS/FAIL):
  [S] cubic symbol = square of the sextic symbol; order exactly 3 on (O/p)^x; chi_n(-1) = 1;
      cubic reciprocity bicharacter R(a,b) = chi_b(a) conj chi_a(b) == 1 on coprime primary pairs.
  [G] cubic eq:gauss-local (l. 7056-7079 with 6 -> 3) at split p (N=7, 13) and inert p (N=25),
      all frequencies k mod p^a; |g|^2 exactly; zero row G(p^a,0) = 0 unless 3 | a.
  [F] single-prime correlation F(p^i, p^j0; j) (old-eq:2.11) by brute force over ALL (x, y),
      hence all j mod p^(i+j0): vanishing pattern, eq:correlation-local, and the unequal formula
      P^{j0-1}(P-1) chi_p(k)^{i-j0} with 3 | j0 (includes j0 = 3: (4,3),(5,3),(3,4),(3,5)).
  [T] the cubic absolute table (analogue of l. 13742-13751) and the cubic F_2 table (analogue of
      l. 14507-14516) DERIVED from the brute-force maxima of [F].
  [C] lem:full-correlation (cubic local factors) for composite moduli with prime powers, all j.
  [E] lem:complete-support-correlation (eq:correlation-child-character), all j, including
      D = p^4, E = p^3 (unequal j0 = 3), D = E = p^3, inert primes, prime-power residuals.
  [A] first-transform allocation: r-primes = {3 does not divide i - j}; row-character
      factorisation (B1), primitivity of xi_r (B2), CRT factorisation of the Gauss sum mod r a b
      (B3), cubic budget (old-eq:2.6) with B_c = ((3c - 4d - 2R)/6)_+ and F_1 >= 5c/6 (J < 0).
  [K] cubic Kummer / fixed-numerator-ray lemma: fixed S-numerators give characters periodic
      mod 18 (3 unit classes x valuations mod 3: 27 characters, not 6^3); good numerators are
      ramified exactly when 3 does not divide the valuation; exceptional rows are exactly
      (h') = h_0 v^3; forced residues at second-transform primes (nonunit i = 1 -> 1 mod 3).
  [L] exact exponent ledger: (old-eq:2.15)-(2.16) at theta = 1/3 (sympy), the centred deficit
      max_v [A - 2M/3 - F_1 - F_2 - (L - v)_+] with F_1 + F_2 >= (5/6) v, and the loss tolerance.
  Failing controls (marked CTRL) must be DETECTED: sextic vanishing rules at j0 = 3 / c = 3,
  conjugated child character, sextic r-classification in B2, sextic theta in (2.15), sextic
  6-periodicity of unit numerators, forced residue 4 instead of 1, etc.

Run: nice -n 10 python3 -I scripts/cubic_local_checks.py      (about 1-2 minutes, < 1 GB)
"""
import itertools
import math
import os
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "a2"))
import eis as E  # noqa: E402

RES = []
T0 = time.time()


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    sys.stdout.flush()


# ---------------------------------------------------------------------------------------------
# exact helpers
# ---------------------------------------------------------------------------------------------
def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


def emul(x, y):
    return E.mul(x, y)


def epow(x, e):
    r = (1, 0)
    for _ in range(e):
        r = emul(r, x)
    return r


def eprod(fac):
    """element prod p^e for fac = {p: e}"""
    r = (1, 0)
    for p, e in fac.items():
        r = emul(r, epow(p, e))
    return r


def vmul(c, X0, X1):
    """vectorised c * (X0 + X1 omega) for a fixed element c"""
    a, b = c
    return a * X0 - b * X1, a * X1 + b * X0 - b * X1


class Mod:
    """canonical residues of O modulo n (HNF of nO in the basis 1, omega); vectorised idx."""

    def __init__(self, n):
        a1, b1 = n
        a2, b2 = emul(n, (0, 1))
        N = abs(a1 * b2 - a2 * b1)
        g, x, y = egcd(b1, b2)
        self.n, self.N, self.g, self.d1 = n, N, g, N // g
        self.w0 = x * a1 + y * a2
        assert N == E.norm(n)

    def idx(self, z0, z1):
        j = z1 % self.g
        t = (z1 - j) // self.g
        i = (z0 - t * self.w0) % self.d1
        return j * self.d1 + i

    def res(self):
        J, I = np.divmod(np.arange(self.N, dtype=np.int64), self.d1)
        return I, J                       # element I + J omega, in idx order


_tab = {}


def c3tab(p):
    """cubic symbol exponent table on residues mod p (0,1,2; -1 for zero)."""
    if p not in _tab:
        M = Mod(p)
        I, J = M.res()
        t = np.full(M.N, -1, dtype=np.int64)
        for k in range(M.N):
            s = E.sym_prime((int(I[k]), int(J[k])), p)
            if s is not None:
                t[k] = s % 3              # (u/p)_3 = (u/p)_6^2 = omega^(s mod 3)
        _tab[p] = (M, t)
    return _tab[p]


def c3(p, z0, z1):
    M, t = c3tab(p)
    return t[M.idx(np.asarray(z0, dtype=np.int64), np.asarray(z1, dtype=np.int64))]


def s6(p, z0, z1):
    """sextic exponent (for controls)"""
    return E.sym_prime((int(z0), int(z1)), p)


def chi_exp(fac, z0, z1, conj=False):
    """exponent of chi_n(z) (cubic, zero-extended) for n = prod p^e; -1 marks zero."""
    z0 = np.asarray(z0, dtype=np.int64)
    z1 = np.asarray(z1, dtype=np.int64)
    tot = np.zeros(np.broadcast(z0, z1).shape, dtype=np.int64)
    zero = np.zeros(tot.shape, dtype=bool)
    for p, e in fac.items():
        if e == 0:
            continue
        s = c3(p, z0, z1)
        zero |= s < 0
        tot += np.where(s < 0, 0, s) * e
    if conj:
        tot = -tot
    return np.where(zero, -1, tot % 3)


def wpow(e):
    """omega^e as exact pair arrays; e = -1 -> 0"""
    e = np.asarray(e)
    A = np.select([e == 0, e == 1, e == 2], [1, 0, -1], 0).astype(np.int64)
    B = np.select([e == 0, e == 1, e == 2], [0, 1, -1], 0).astype(np.int64)
    return A, B


def zmul(x, y):
    a, b = x
    c, d = y
    return a * c - b * d, a * d + b * c - b * d


def zconj(x):
    return x[0] - x[1], -x[1]


def znorm(x):
    a, b = x
    return a * a - a * b + b * b


def zeq(x, y):
    return np.array_equal(np.asarray(x[0]), np.asarray(y[0])) and np.array_equal(np.asarray(x[1]), np.asarray(y[1]))


def hist_sum(idx, e, N):
    """sum over entries of omega^e (e = -1 skipped), bucketed by idx: exact Z[omega] array."""
    out = []
    for c in range(3):
        m = e == c
        out.append(np.bincount(idx[m], minlength=N).astype(np.int64))
    n0, n1, n2 = out
    return n0 - n2, n1 - n2


def valuation(p, z0, z1, cap):
    """v_p of elements (vectorised), capped; zero elements get cap."""
    cp = E.conj(p)
    Np = E.norm(p)
    v = np.zeros(z0.shape, dtype=np.int64)
    alive = np.ones(z0.shape, dtype=bool)
    c0, c1 = z0.copy(), z1.copy()
    for _ in range(cap):
        m0, m1 = vmul(cp, c0, c1)
        div = alive & (m0 % Np == 0) & (m1 % Np == 0)
        v += div
        c0 = np.where(div, m0 // Np, c0)
        c1 = np.where(div, m1 // Np, c1)
        alive = div
    return v


def divide_by(p, e, z0, z1):
    cp = E.conj(p)
    Np = E.norm(p)
    for _ in range(e):
        m0, m1 = vmul(cp, z0, z1)
        assert np.all(m0 % Np == 0) and np.all(m1 % Np == 0)
        z0, z1 = m0 // Np, m1 // Np
    return z0, z1


# --- exact cyclotomic zero test -------------------------------------------------------------
def mobius(n):
    r, m, q = 1, n, 2
    while q * q <= m:
        if m % q == 0:
            m //= q
            if m % q == 0:
                return 0
            r = -r
        q += 1
    if m > 1:
        r = -r
    return r


_phi = {}


def cyclo(N):
    """integer coefficients of Phi_N (low degree first) via prod (X^d - 1)^{mu(N/d)}."""
    if N in _phi:
        return _phi[N]
    num, den = [1], [1]
    for d in range(1, N + 1):
        if N % d:
            continue
        mu = mobius(N // d)
        if mu == 0:
            continue
        f = [-1] + [0] * (d - 1) + [1]
        tgt = num if mu == 1 else den
        new = [0] * (len(tgt) + d)
        for i, c in enumerate(tgt):
            if c:
                new[i] -= c
                new[i + d] += c
        if mu == 1:
            num = new
        else:
            den = new
    # exact division num / den (den monic)
    num = num[:]
    q = [0] * (len(num) - len(den) + 1)
    for k in range(len(q) - 1, -1, -1):
        c = num[k + len(den) - 1]
        q[k] = c
        if c:
            for i, dc in enumerate(den):
                num[k + i] -= c * dc
    assert all(x == 0 for x in num[:len(den) - 1])
    _phi[N] = np.array(q, dtype=np.int64)
    return _phi[N]


def cyclo_zero(vec, N):
    """vec: integer array indexed by exponent mod N (sum c_d zeta_N^d).  True iff the sum is 0."""
    vec = np.array(vec, dtype=np.int64)
    # prime-power N: kernel = vectors constant on cosets of the subgroup of order p
    f = [q for q in range(2, N + 1) if N % q == 0 and all(q % r for r in range(2, int(q ** .5) + 1))]
    if len(f) == 1:
        p = f[0]
        s = N // p
        return bool(np.all(vec.reshape(p, s) == vec.reshape(p, s)[0:1, :]))
    ph = cyclo(N)
    deg = len(ph) - 1
    c = vec.copy()
    for k in range(N - 1, deg - 1, -1):
        a = c[k]
        if a:
            c[k - deg:k + 1] -= a * ph
    assert np.abs(c).max() < 2 ** 60
    return bool(np.all(c[:deg] == 0))


def zcyclo_zero(A, B, N):
    return cyclo_zero(A, N) and cyclo_zero(B, N)


def addchar_exp(n, z0, z1):
    """exponent d (mod N(n)) of e(z/n) = exp(2 pi i d / N): omega-coordinate of z conj(n)."""
    cn = E.conj(n)
    _, d = vmul(cn, z0, z1)
    return d % E.norm(n)


# =============================================================================================
# [S] symbols and reciprocity
# =============================================================================================
def part_S(PR):
    good = PR[:9]                                    # norms 7,7,13,13,19,19,25,31,31
    ok_sq, ok_ord, ok_m1, ok_mult = True, True, True, True
    for p in good:
        M, t = c3tab(p)
        I, J = M.res()
        for k in range(M.N):
            s = E.sym_prime((int(I[k]), int(J[k])), p)
            ok_sq &= (s is None and t[k] == -1) or (s is not None and t[k] == (2 * s) % 6 // 2)
        vals = set(int(x) for x in t if x >= 0)
        ok_ord &= vals == {0, 1, 2}                  # order exactly 3 on (O/p)^x
        ok_m1 &= int(c3(p, -1, 0)) == 0
        rng = random.Random(1)
        for _ in range(200):
            x = (rng.randint(-40, 40), rng.randint(-40, 40))
            y = (rng.randint(-40, 40), rng.randint(-40, 40))
            a, b = int(c3(p, *x)), int(c3(p, *y))
            ab = int(c3(p, *emul(x, y)))
            ok_mult &= (ab == -1) if (a < 0 or b < 0) else (ab == (a + b) % 3)
    check("[S1] cubic symbol = (sextic)^2, multiplicative, order exactly 3 on (O/p)^x, chi_p(-1) = 1",
          ok_sq and ok_ord and ok_m1 and ok_mult, "%d primes (split 7..31, inert 5)" % len(good))
    # [S2] cubic reciprocity: R(a,b) = chi_b(a) conj chi_a(b) == 1 for coprime primary a, b
    gens = []
    base = PR[:8]
    for es in itertools.product(range(3), repeat=4):
        fac = {p: e for p, e in zip(base[:4], es) if e}
        gens.append(fac)
    for es in itertools.product(range(2), repeat=4):
        fac = {p: e for p, e in zip(base[4:8], es) if e}
        gens.append(fac)
    ok, n, sext_nontriv = True, 0, 0
    for fa in gens:
        a = eprod(fa)
        for fb in gens:
            if set(fa) & set(fb):
                continue
            b = eprod(fb)
            e1 = int(chi_exp(fb, a[0], a[1]))
            e2 = int(chi_exp(fa, b[0], b[1]))
            ok &= e1 >= 0 and e2 >= 0 and (e1 - e2) % 3 == 0
            n += 1
            # sextic R for contrast (control: must be nontrivial for some pairs)
            s1 = sum(s6(p, *a) * e for p, e in fb.items())
            s2 = sum(s6(p, *b) * e for p, e in fa.items())
            sext_nontriv += (s1 - s2) % 6 != 0
    check("[S2] cubic reciprocity: chi_b(a) = chi_a(b) for all coprime primary pairs (R == 1)", ok,
          "%d pairs" % n)
    check("[S2-CTRL] the sextic bicharacter is nontrivial on some of the same pairs (check is sensitive)",
          sext_nontriv > 0, "%d/%d pairs with sextic R != 1" % (sext_nontriv, n))


# =============================================================================================
# [G] cubic prime-power Fourier sums
# =============================================================================================
def gauss_vec(fac, n, h, nexp=None):
    """unnormalised sum_{x mod n} chi_fac(x)^... e(hx/n) as exact (A, B) vectors over Z/N(n)."""
    M = Mod(n)
    I, J = M.res()
    ce = chi_exp(fac if nexp is None else nexp, I, J)
    hx0, hx1 = vmul(h, I, J)
    d = addchar_exp(n, hx0, hx1)
    return hist_sum(d, ce, M.N)


def part_G(PR):
    p7, p13, q5 = PR[0], PR[2], PR[6]
    nchk, fails, ctrl_hits = 0, [], 0
    rng = random.Random(2)
    for p, amax in [(p7, 4), (p13, 3), (q5, 2)]:
        P = E.norm(p)
        for a in range(1, amax + 1):
            n = epow(p, a)
            N = E.norm(n)
            ks = [(0, 0)]
            for v in range(0, a + 1):
                for _ in range(3):
                    u = (rng.randint(-30, 30), rng.randint(-30, 30))
                    if int(c3(p, *u)) < 0:
                        continue
                    ks.append(emul(u, epow(p, v)))
            for k in ks:
                A, B = gauss_vec({p: a}, n, k)
                v = a + 5 if k == (0, 0) else int(valuation(p, np.array([k[0]]), np.array([k[1]]), a + 5)[0])
                if a % 3 == 0:
                    tgt = (P ** a if v >= a else 0) - (P ** (a - 1) if v >= a - 1 else 0)
                    A2 = A.copy()
                    A2[0] -= tgt
                    ok = zcyclo_zero(A2, B, N)
                    # CTRL: sextic rule (6 | a) would predict a vanishing sum with |g|^2 = P^{2a-1}
                    if a == 3 and v == a - 1:
                        ctrl_hits += not zcyclo_zero(A, B, N)
                else:
                    if v != a - 1:
                        ok = zcyclo_zero(A, B, N)
                    else:
                        # |g|^2 = g * conj(g) = P^{2a-1} exactly (cyclic convolution in Z[omega][C_N])
                        Ar, Br = np.roll(A[::-1], 1), np.roll(B[::-1], 1)        # X -> X^{-1}
                        Cc, Dc = Ar - Br, -Br                                    # conj coefficients
                        def cconv(x, y):
                            z = np.convolve(x, y)
                            out = z[:N].copy()
                            out[:len(z) - N] += z[N:]
                            return out
                        R0 = cconv(A, Cc) - cconv(B, Dc)
                        R1 = cconv(A, Dc) + cconv(B, Cc) - cconv(B, Dc)
                        R0[0] -= P ** (2 * a - 1)
                        ok = zcyclo_zero(R0, R1, N)
                if not ok:
                    fails.append((E.norm(p), a, k))
                nchk += 1
    check("[G1] cubic eq:gauss-local exact: |G(p^a,k)| = P^{(a-1)/2} 1_{v(k)=a-1} (3 !| a); "
          "G = P^{a/2}1_{p^a|k} - P^{a/2-1}1_{p^{a-1}|k} (3 | a); includes k = 0 (zero row)",
          not fails, "%d (p, a, k) cases at N p = 7 (a<=4), 13 (a<=3), 25 inert (a<=2); fails %s" % (nchk, fails[:3]))
    check("[G1-CTRL] at a = 3, v(k) = 2 the sextic rule (sum vanishes unless 6 | a fails) is contradicted",
          ctrl_hits > 0, "%d nonvanishing a = 3 sums" % ctrl_hits)


# =============================================================================================
# [F] single-prime correlation, brute force over all (x, y)
# =============================================================================================
def corr_hist(ufac, vfac):
    """F(u, v; j) = sum_{vx - uy = j mod uv} chi_u(x) conj chi_v(y), for ALL j (exact)."""
    u, v = eprod(ufac), eprod(vfac)
    uv = emul(u, v)
    Mu, Mv, Muv = Mod(u), Mod(v), Mod(uv)
    X0, X1 = Mu.res()
    Y0, Y1 = Mv.res()
    cx = chi_exp(ufac, X0, X1)
    cy = chi_exp(vfac, Y0, Y1, conj=True)
    vx0, vx1 = vmul(v, X0, X1)
    uy0, uy1 = vmul(u, Y0, Y1)
    idx = Muv.idx(vx0[:, None] - uy0[None, :], vx1[:, None] - uy1[None, :]).ravel()
    ce = np.where((cx[:, None] >= 0) & (cy[None, :] >= 0), (cx[:, None] + cy[None, :]) % 3, -1).ravel()
    F = hist_sum(idx, ce, Muv.N)
    J0, J1 = Muv.res()
    return F, J0, J1, Muv


def predict_single(p, i, j0, J0, J1, rule=3, conj_child=False):
    P = E.norm(p)
    K = i + j0
    val = valuation(p, J0, J1, K)
    g = min(i, j0)
    A = np.zeros(J0.shape, dtype=np.int64)
    B = np.zeros(J0.shape, dtype=np.int64)
    if i == j0:
        c = i
        nonunit = val >= c + 1
        unit = val == c
        A = np.where(nonunit, P ** (c - 1) * (P - 1), A)
        A = np.where(unit, P ** (c - 1) * ((P - 2) if c % rule == 0 else -1), A)
        return (A, B), val
    sel = (val == g) if g % rule == 0 else np.zeros(J0.shape, dtype=bool)
    k0, k1 = J0.copy(), J1.copy()
    k0 = np.where(val >= g, k0, 0)
    k1 = np.where(val >= g, k1, 0)
    k0, k1 = divide_by(p, g, k0, k1)
    if i > j0:
        e = chi_exp({p: i - j0}, k0, k1, conj=conj_child)
    else:
        e = chi_exp({p: j0 - i}, -k0, -k1, conj=not conj_child)
    W = wpow(e)
    amp = P ** (g - 1) * (P - 1)
    A = np.where(sel, amp * W[0], 0)
    B = np.where(sel, amp * W[1], 0)
    return (A, B), val


def part_F(PR):
    p7, p13, q5 = PR[0], PR[2], PR[6]
    plan = [(p7, 8), (p13, 5), (q5, 4)]
    ncase, fails = 0, []
    ctrl6, ctrlc = 0, 0
    absfails, maxima = [], {}
    for p, tot in plan:
        P = E.norm(p)
        for i in range(1, tot):
            for j0 in range(1, tot - i + 1):
                F, J0, J1, Muv = corr_hist({p: i}, {p: j0})
                pred, val = predict_single(p, i, j0, J0, J1)
                ok = zeq(F, pred)
                if not ok:
                    fails.append((P, i, j0))
                ncase += 1
                # controls: sextic rule; conjugated child character
                if i != j0 and min(i, j0) == 3 or (i == j0 and i == 3):
                    p6, _ = predict_single(p, i, j0, J0, J1, rule=6)
                    ctrl6 += not zeq(F, p6)
                if i != j0 and min(i, j0) % 3 == 0 and (i - j0) % 3:
                    pc, _ = predict_single(p, i, j0, J0, J1, conj_child=True)
                    ctrlc += not zeq(F, pc)
                # absolute table (cubic analogue of l. 13742-13751), via exact norms
                nr = znorm(F)
                g = min(i, j0)
                if i == j0:
                    unit = val == i
                    for lab, m in (("unit", unit), ("nonunit", val >= i + 1)):
                        if m.any() and nr[m].max() > 0:
                            key = (P, i, j0, lab)
                            maxima[key] = int(nr[m].max())
                    bound = np.where(unit & (i % 3 != 0), P ** (2 * (i - 1)), P ** (2 * i))
                    bound = np.where(val >= i, bound, 0)
                else:
                    bound = np.where(val == g, P ** (2 * g), 0)
                    m = val == g
                    if m.any() and nr[m].max() > 0:
                        maxima[(P, i, j0, "unit")] = int(nr[m].max())
                if np.any(nr > bound):
                    absfails.append((P, i, j0))
    check("[F1] single-prime correlation F(p^i,p^j0;j) = cubic eq:correlation-local / unequal formula, "
          "ALL j mod p^(i+j0), exact", not fails,
          "%d (p,i,j0) tables: Np=7 (i+j0<=8, incl. (4,3),(5,3),(3,4),(3,5)), 13 (<=5), 25 inert (<=4); fails %s"
          % (ncase, fails[:4]))
    check("[F1-CTRL] sextic rules (6 | j0, 6 | c) mis-predict every table with j0 = 3 or c = 3", ctrl6 >= 5,
          "%d tables detected" % ctrl6)
    check("[F1-CTRL] conjugated child character chi_p(k)^{-(i-j0)} mis-predicts the unequal j0 = 3 tables",
          ctrlc >= 2, "%d tables detected" % ctrlc)
    check("[T1] cubic absolute table: |F| <= P^{i-1} (equal, 3!|i, unit); P^i (equal, else); "
          "P^{j0} (unequal, 3|j0, v(j)=j0); 0 otherwise", not absfails, "violations %s" % absfails[:3])
    return maxima


def part_T(maxima):
    """derive t2 (correlation saving) from the brute-force maxima and build the cubic F_2 table."""
    def eobs(P, nr):          # smallest integer e with |F|^2 <= P^{2e}
        e = 0
        while P ** (2 * e) < nr:
            e += 1
        return e
    rows = {}
    for (P, i, j0, lab), nr in sorted(maxima.items()):
        g2 = min(i, j0)
        t2 = g2 - eobs(P, nr)
        if i == j0:
            typ = ("eq", i % 3 == 0, lab)
        else:
            typ = ("uneq", True, lab)
        rows.setdefault(typ, set()).add((i, j0, t2))
    # t2 = 1 exactly for (equal, 3 !| i, unit), else 0 -- from data
    ok = True
    for typ, s in rows.items():
        for (i, j0, t2) in s:
            want = 1 if (typ[0] == "eq" and not typ[1] and typ[2] == "unit") else 0
            ok &= t2 == want
    check("[T2] correlation saving t2 read off the brute-force maxima: t2 = 1 exactly at equal 3 !| i unit primes",
          ok, "types seen: %s" % sorted((k, sorted(v)[:3]) for k, v in rows.items())[:2])

    # exact F_2 table (theta = 1/3): F_2 = 2 b_2 - (2/3) g_2 - p_2 + t_2 + V/3 + f/3 per prime
    th = Fr(1, 3)
    tab_ok, tab_nof_min, tight = True, None, []
    lines = []
    for i in range(1, 31):
        for j0 in range(1, 31):
            if i == j0:
                cases = []
                if i % 3:
                    cases.append(("eq unit", i, 1, 0, 0))
                    cases.append(("eq nonunit", i, 0, 1, 1 if i == 1 else 0))
                else:
                    cases.append(("eq 3|i", i, 0, 0, 0))
                for lab, g2, t2, V, f in cases:
                    b2 = Fr(i)
                    F2 = 2 * b2 - (1 - th) * g2 - 1 + t2 + th * V + th * f
                    F2nof = 2 * b2 - (1 - th) * g2 - 1 + t2 + th * V
                    tab_ok &= F2 >= b2
                    tab_nof_min = min(tab_nof_min or Fr(9), F2nof / b2)
                    if F2 == b2:
                        tight.append((lab, i))
                    if i <= 4:
                        lines.append("%s i=%d: F2=%s b2=%s" % (lab, i, F2, b2))
            elif i > j0 and j0 % 3 == 0:
                b2 = Fr(i + j0, 2)
                F2 = 2 * b2 - (1 - th) * j0 - 1
                tab_ok &= F2 >= b2
                if F2 == b2:
                    tight.append(("uneq", i, j0))
                if j0 == 3 and i <= 5:
                    lines.append("uneq (%d,3): F2=%s b2=%s" % (i, F2, b2))
    check("[T3] cubic F_2 table: F_2 >= b_2 at every local type (kappa_2 = 1, nonunit i=1 forcing f = v_1)",
          tab_ok, "tight at %s; unequal j0=3 has slack (i-3)/2 >= 1/2" % sorted(set(tight)))
    check("[T3-CTRL] without the nonunit forcing f, min F_2/b_2 = 2/3 (= 2 theta: the zero-margin case)",
          tab_nof_min == Fr(2, 3), "min = %s" % tab_nof_min)
    print("     " + "; ".join(lines))


# =============================================================================================
# [C] full correlation lemma (cubic local factors), composite moduli
# =============================================================================================
def part_C(PR):
    p7, p7b, p13, p13b, p19, p19b, q5 = PR[:7]
    cfgs = [
        ("u=p7^3 p13, v=p7^3 p7'  (C=p7^3 equal, n1=p13, n2=p7')", {p7: 3, p13: 1}, {p7: 3, p7b: 1}),
        ("u=p7^4, v=p7^3 p13  (C=p7^3 one-sided at p7, c=3)", {p7: 4}, {p7: 3, p13: 1}),
        ("u=p7^2 p7', v=p7 p7'^2 (one-sided c=1 at both: F == 0)", {p7: 2, p7b: 1}, {p7: 1, p7b: 2}),
        ("u=p7 p13, v=p7 p19", {p7: 1, p13: 1}, {p7: 1, p19: 1}),
        ("u=q5 p7, v=q5 p13 (inert c=1)", {q5: 1, p7: 1}, {q5: 1, p13: 1}),
        ("u=p13^2 p7, v=p13^2 p7'^2", {p13: 2, p7: 1}, {p13: 2, p7b: 2}),
    ]
    ok_all = True
    det = []
    for name, uf, vf in cfgs:
        F, J0, J1, Muv = corr_hist(uf, vf)
        Cf = {p: min(uf.get(p, 0), vf.get(p, 0)) for p in set(uf) | set(vf)}
        Cf = {p: e for p, e in Cf.items() if e}
        n1 = {p: uf.get(p, 0) - Cf.get(p, 0) for p in uf}
        n1 = {p: e for p, e in n1.items() if e}
        n2 = {p: vf.get(p, 0) - Cf.get(p, 0) for p in vf}
        n2 = {p: e for p, e in n2.items() if e}
        # C | j ?
        divC = np.ones(J0.shape, dtype=bool)
        k0, k1 = J0.copy(), J1.copy()
        for p, e in Cf.items():
            vv = valuation(p, k0, k1, e)
            divC &= vv >= e
        k0 = np.where(divC, k0, 0)
        k1 = np.where(divC, k1, 0)
        for p, e in Cf.items():
            k0, k1 = divide_by(p, e, k0, k1)
        # chi_{n1}(k) conj chi_{n2}(-k) R(n1, n2)
        e1 = chi_exp(n1, k0, k1)
        e2 = chi_exp(n2, -k0, -k1, conj=True)
        n1e, n2e = eprod(n1), eprod(n2)
        R = (int(chi_exp(n2, *n1e)) - int(chi_exp(n1, *n2e))) % 3 if (n1 and n2) else 0
        ee = np.where((e1 >= 0) & (e2 >= 0), (e1 + e2 + R) % 3, -1)
        val = wpow(ee)
        amp = np.ones(J0.shape, dtype=np.int64)
        phase = np.zeros(J0.shape, dtype=np.int64)
        for p, c in Cf.items():
            P = E.norm(p)
            pk = valuation(p, k0, k1, 1) >= 1
            if p in n1 or p in n2:
                loc = np.where(pk, 0, P ** (c - 1) * (P - 1)) if c % 3 == 0 else np.zeros(J0.shape, dtype=np.int64)
            else:
                # chi_p(n1/n2)^c phase and P^{c-1}{P-1, -1, P-2}
                loc = np.where(pk, P ** (c - 1) * (P - 1), P ** (c - 1) * ((P - 2) if c % 3 == 0 else -1))
                ph = (int(c3(p, *n1e)) - int(c3(p, *n2e))) * c
                phase += ph
            amp = amp * loc
        W = wpow(phase % 3)
        rhs = zmul((amp * W[0], amp * W[1]), val)
        rhs = (np.where(divC, rhs[0], 0), np.where(divC, rhs[1], 0))
        ok = zeq(F, rhs)
        ok_all &= ok
        det.append("%s:%s(nz=%d)" % (name.split()[0], "ok" if ok else "FAIL", int(np.count_nonzero(znorm(F)))))
    check("[C1] lem:full-correlation with cubic local factors (P-1 | -1 | P-2 if 3|c; one-sided P^{c-1}(P-1)1_{3|c}), "
          "ALL j", ok_all, "; ".join(det))


# =============================================================================================
# [E] complete-support correlation
# =============================================================================================
def part_E(PR):
    p7, p7b, p13, p13b, p19, p19b, q5 = PR[:7]
    cfgs = [
        ("D=p7^4,E=p7^3 (unequal j0=3); a=p7', b=1", {p7: 4}, {p7: 3}, {p7b: 1}, {}),
        ("D=p7^3,E=p7^4 (unequal, mirror); a=1, b=p7'", {p7: 3}, {p7: 4}, {}, {p7b: 1}),
        ("D=E=p7^3 (equal 3|i); a=p7', b=p13", {p7: 3}, {p7: 3}, {p7b: 1}, {p13: 1}),
        ("D=E=p7 p13; a=p7'^2, b=p19", {p7: 1, p13: 1}, {p7: 1, p13: 1}, {p7b: 2}, {p19: 1}),
        ("D=E=q5 (inert); a=p7, b=p7'", {q5: 1}, {q5: 1}, {p7: 1}, {p7b: 1}),
        ("D=p7^2,E=p7 (unequal j0=1: zero); a=p13, b=p7'", {p7: 2}, {p7: 1}, {p13: 1}, {p7b: 1}),
    ]
    for name, Df, Ef, af, bf in cfgs:
        uf = dict(Df)
        uf.update(af)
        vf = dict(Ef)
        vf.update(bf)
        F, J0, J1, Muv = corr_hist(uf, vf)
        FDE, _, _, MDE = corr_hist(Df, Ef)
        k = MDE.idx(J0, J1)
        base = (FDE[0][k], FDE[1][k])
        a, b = eprod(af), eprod(bf)
        D, Ee = eprod(Df), eprod(Ef)

        def Rexp(xf, x, yf, y):                  # R(x, y) = chi_y(x) conj chi_x(y)
            if not xf or not yf:
                return 0
            return (int(chi_exp(yf, *x)) - int(chi_exp(xf, *y))) % 3
        Rtot = (Rexp(af, a, Ef, Ee) - Rexp(bf, b, Df, D) + Rexp(af, a, bf, b)) % 3
        ea = chi_exp(af, J0, J1) if af else np.zeros(J0.shape, dtype=np.int64)
        eb = chi_exp(bf, -J0, -J1, conj=True) if bf else np.zeros(J0.shape, dtype=np.int64)
        ee = np.where((ea >= 0) & (eb >= 0), (ea + eb + Rtot) % 3, -1)
        rhs = zmul(base, wpow(ee))
        ok = zeq(F, rhs)
        nz = int(np.count_nonzero(znorm(F)))
        # control: drop chi_a(j) (replace by its conjugate) -- must be detected when a nontrivial
        ctrl = ""
        if af:
            ea2 = chi_exp(af, J0, J1, conj=True)
            ee2 = np.where((ea2 >= 0) & (eb >= 0), (ea2 + eb + Rtot) % 3, -1)
            det = not zeq(F, zmul(base, wpow(ee2))) if nz else True
            ctrl = "; CTRL conj chi_a(j) %s" % ("detected" if det else "NOT detected")
            ok &= det
        check("[E] complete-support correlation %s" % name, ok,
              "all %d frequencies (%d nonzero), R-phase total %d%s" % (Muv.N, nz, Rtot, ctrl))


# =============================================================================================
# [A] first transform: allocation, row character, xi_r, CRT, budget
# =============================================================================================
def part_A(PR):
    p7, p7b, p13, p13b, p19, p19b, q5, p31 = PR[:8]
    # B1: chi_C conj chi_D = xi_r 1_{(k, c/r)=1}, r = {p : 3 !| i-j}, xi_r = prod chi_p^{(i-j) mod 3}
    cfgs = [({p7: 2, p7b: 4, p13: 3}, {p7: 1, p7b: 1, p13: 1}),      # (2,1) r; (4,1) e (cubic) ; (3,1) r
            ({p7: 5, q5: 3}, {p7: 2, q5: 1}),                          # (5,2) e; inert (3,1) r
            ({p13: 6, p7b: 1}, {p13: 3, p7b: 4})]                      # (6,3) e; (1,4) e
    ok = True
    for Cf, Df in cfgs:
        rr = {p: (Cf[p] - Df[p]) % 3 for p in Cf if (Cf[p] - Df[p]) % 3}
        comp = [p for p in Cf if (Cf[p] - Df[p]) % 3 == 0]
        M = Mod(eprod({p: 1 for p in Cf}))
        I, J = M.res()
        lhs_e = np.where((chi_exp(Cf, I, J) >= 0) & (chi_exp(Df, I, J) >= 0),
                         (chi_exp(Cf, I, J) - chi_exp(Df, I, J)) % 3, -1)
        rhs_e = chi_exp(rr, I, J) if rr else np.zeros(M.N, dtype=np.int64)
        for p in comp:
            rhs_e = np.where(c3(p, I, J) < 0, -1, rhs_e)
        ok &= np.array_equal(lhs_e, rhs_e)
    check("[A-B1] chi_C conj chi_D = xi_r 1_{(k,c/r)=1} with r = {3 !| i-j} (exact, all k mod rad)", ok,
          "types (2,1),(4,1),(3,1),(5,2),(6,3),(1,4), inert (3,1)")

    # B2: xi_r primitive: sum_{x mod r} xi_r(x) e(xh/r) = conj xi_r(h) tau(xi_r), |tau|^2 = q_r (exact)
    def b2(rr):
        r = eprod({p: 1 for p in rr})
        M = Mod(r)
        N = M.N
        I, J = M.res()
        ce = chi_exp(rr, I, J)
        tau = gauss_vec(None, r, (1, 0), nexp=rr)
        good = True
        for hi in range(N):
            h = (int(I[hi]), int(J[hi]))
            g = gauss_vec(None, r, h, nexp=rr)
            ch = int(chi_exp(rr, h[0], h[1], conj=True))
            pred = zmul(tau, tuple(np.int64(x) for x in wpow(ch))) if ch >= 0 else (np.zeros(N, np.int64), np.zeros(N, np.int64))
            good &= zcyclo_zero(g[0] - pred[0], g[1] - pred[1], N)
        return good
    rrs = [{p7b: 1}, {p7: 2}, {p7: 1, p13: 2}, {q5: 1}]
    okB2 = all(b2(rr) for rr in rrs)
    check("[A-B2] xi_r primitive: Gauss sum = conj xi_r(h) tau(xi_r) for every h mod r (exact cyclotomic test)",
          okB2, "r = p7', p7 (exp 2), p7 p13 (exps 1,2), inert 5")
    # CTRL: sextic classification at (4,1): cubic exponent 3 -> principal -> identity fails
    okc = b2({p7: 3}) is False
    check("[A-B2-CTRL] classifying (4,1) as an r-prime (sextic rule 6 !| 3) gives a non-primitive xi_r: identity fails",
          okc)

    # B3: CRT factorisation of the Gauss sum mod r a b (exact, sampled h)
    def b3(rr, af, bf, nh=12):
        rad_r = {p: 1 for p in rr}
        r_el, a_el, b_el = eprod(rad_r), eprod(af), eprod(bf)
        Q = eprod({**rad_r, **af, **bf}) if not (set(rad_r) & set(af) or set(af) & set(bf)) else None
        MQ = Mod(Q)
        N = MQ.N
        Nr, Na, Nb = E.norm(r_el), E.norm(a_el), E.norm(b_el)
        I, J = MQ.res()
        e_l = np.where((chi_exp(rr, I, J) >= 0) & (chi_exp(af, I, J) >= 0) & (chi_exp(bf, I, J, conj=True) >= 0),
                       (chi_exp(rr, I, J) + chi_exp(af, I, J) + chi_exp(bf, I, J, conj=True)) % 3, -1)
        ph = (int(chi_exp(rr, *emul(a_el, b_el))) + int(chi_exp(af, *emul(r_el, b_el)))
              + int(chi_exp(bf, *emul(r_el, a_el), conj=True)))
        rng = random.Random(5)
        good = True
        for _ in range(nh):
            hi = rng.randrange(N)
            h = (int(I[hi]), int(J[hi]))
            hx0, hx1 = vmul(h, I, J)
            L = hist_sum(addchar_exp(Q, hx0, hx1), e_l, N)
            # RHS: product of the three Gauss sums embedded in C_N
            parts = []
            for fac, el, Nx, cj, hh in ((rr, r_el, Nr, False, h), (af, a_el, Na, False, h), (bf, b_el, Nb, True, h)):
                Mx = Mod(el)
                Ix, Jx = Mx.res()
                ce = chi_exp(fac, Ix, Jx, conj=cj)
                s0, s1 = vmul(hh, Ix, Jx)
                d = addchar_exp(el, s0, s1) * (N // Nx)
                parts.append((d[ce >= 0], ce[ce >= 0]))
            (d1, c1), (d2, c2), (d3, c3_) = parts
            dd = (d1[:, None, None] + d2[None, :, None] + d3[None, None, :]).ravel() % N
            cc = ((c1[:, None, None] + c2[None, :, None] + c3_[None, None, :]).ravel() + ph) % 3
            Rv = hist_sum(dd, cc, N)
            good &= zcyclo_zero(L[0] - Rv[0], L[1] - Rv[1], N)
        return good
    okB3 = b3({p7: 1}, {p13: 1}, {p19: 1}) and b3({p7: 2}, {p7b: 2}, {p13: 1}) and b3({q5: 1}, {p7: 1}, {p13: 1}, nh=6)
    check("[A-B3] CRT: sum_{x mod rab} xi_r chi_a conj chi_b e(xh/rab) = xi_r(ab) chi_a(rb) conj chi_b(ra) "
          "g_xi(r,h) g(a,h) conj g(b,-h) (exact)", okB3, "(r,a,b) = (p7,p13,p19), (p7 exp2, p7'^2, p13), (q5, p7, p13)")

    # A3: cubic budget (old-eq:2.6) and F_1 >= 5c/6 on the J < 0 branch (worst case q = E = w = 0)
    rng = random.Random(7)
    okb, okf, worst, rat = True, True, None, None
    for _ in range(30000):
        k = rng.randint(1, 4)
        w = [Fr(rng.randint(1, 50), rng.randint(1, 7)) for _ in range(k)]
        ij = [(rng.randint(1, 12), rng.randint(1, 12)) for _ in range(k)]
        c = sum(wi * i for wi, (i, j) in zip(w, ij))
        d = sum(wi * j for wi, (i, j) in zip(w, ij))
        p = sum(w)
        R = sum((wi for wi, (i, j) in zip(w, ij) if (i - j) % 3), Fr(0))
        Bc = max(Fr(0), (3 * c - 4 * d - 2 * R) / 6)
        Bd = max(Fr(0), (3 * d - 4 * c - 2 * R) / 6)
        slack = c + d - 2 * p - R - Bc - Bd
        okb &= slack >= 0
        worst = slack if worst is None else min(worst, slack)
        F1 = c / 3 + 2 * d / 3 + R / 3 + Bc
        okf &= F1 >= Fr(5, 6) * c
        rat = F1 / c if rat is None else min(rat, F1 / c)
    zl = [(i, j) for i in range(1, 30) for j in range(1, i + 1)
          if Fr(i + j - 2 - (1 if (i - j) % 3 else 0)) - max(Fr(0), Fr(3 * i - 4 * j - 2 * (1 if (i - j) % 3 else 0), 6)) == 0]
    check("[A3] cubic budget B_c + B_d <= c+d-2p-R and F_1 >= 5c/6 (J<0) over 30000 multi-prime configurations",
          okb and okf and worst == 0 and rat == Fr(5, 6),
          "min slack %s, min F_1/c = %s (attained at (2,1)); zero-slack local types %s" % (worst, rat, zl))
    # CTRL: the sextic allowance ((3c-5d-R)/6)_+ (with cubic theta and cubic r) falls short at a (4,1) prime,
    # which is an e-prime (r = 0) for n = 3
    c, d, R = Fr(4), Fr(1), Fr(0)
    Bs = max(Fr(0), (3 * c - 5 * d - R) / 6)
    check("[A3-CTRL] the sextic allowance ((3c-5d-R)/6)_+ gives F_1/c = 19/24 < 5/6 at a cubic (4,1) prime",
          (c / 3 + 2 * d / 3 + R / 3 + Bs) / c == Fr(19, 24))


# =============================================================================================
# [K] cubic Kummer / fixed-numerator-ray lemma and exceptional rows
# =============================================================================================
def primary_ideals(PR, Nmax):
    """primary generators of good ideals (prime to 6) with norm <= Nmax, with factorisations."""
    out = [((1, 0), {})]
    for p in PR:
        if E.norm(p) > Nmax:
            break
        new = []
        for el, fac in out:
            e, x = 0, el
            while True:
                e += 1
                x = emul(x, p)
                if E.norm(x) > Nmax:
                    break
                f = dict(fac)
                f[p] = e
                new.append((x, f))
        out += new
    return out


def fast_primes(Nmax):
    """primary prime elements prime to 6 with norm <= Nmax (split pairs and inert p, p^2 <= Nmax)."""
    out = []
    for p in range(5, Nmax + 1):
        if any(p % r == 0 for r in range(2, int(p ** .5) + 1)):
            continue
        if p % 3 == 1:
            for b in range(0, int((4 * p / 3) ** .5) + 2):
                D = 4 * p - 3 * b * b
                s_ = int(round(D ** .5)) if D >= 0 else -1
                if s_ >= 0 and s_ * s_ == D and (b + s_) % 2 == 0:
                    a = (b + s_) // 2
                    assert a * a - a * b + b * b == p
                    out += [E.primary((a, b)), E.primary(E.conj((a, b)))]
                    break
        elif p % 3 == 2 and p * p <= Nmax:
            out.append(E.primary((p, 0)))
    return sorted(set(out), key=E.norm)


def part_K(PR):
    PRb = fast_primes(3000)
    ns = primary_ideals(PRb, 400)
    lam = (1, 2)                      # 1 + 2 omega = sqrt(-3)
    two = (2, 0)

    def chi_n(fac, a):
        e = 0
        for p, k in fac.items():
            s = int(c3(p, *a))
            if s < 0:
                return -1
            e += s * k
        return e % 3

    def red_mod(x, m):              # residue class of element x modulo integer m
        return (x[0] % m, x[1] % m)
    # [K1] numerators u lambda^e 2^f: n -> chi_n(.) periodic modulo 18 on good primary n
    funcs = {}
    okper, ok6 = True, True
    for u in E.UNITS:
        for e in range(6):
            for f in range(6):
                a = emul(u, emul(epow(lam, e), epow(two, f)))
                seen, seen6 = {}, {}
                vec = []
                for el, fac in ns:
                    val = chi_n(fac, a)
                    key = red_mod(el, 18)
                    if key in seen and seen[key] != val:
                        okper = False
                    seen[key] = val
                    key6 = red_mod(el, 6)
                    if key6 in seen6 and seen6[key6] != val:
                        ok6 = False
                    seen6[key6] = val
                    vec.append(val)
                funcs[tuple(vec)] = (u, e % 3, f % 3)
    check("[K1] fixed S-numerators u lambda^e 2^f: n -> chi_n(.) depends only on n mod 18 (ray class, conductor | 18)",
          okper, "%d good primary n, N n <= 400" % len(ns))
    check("[K1-CTRL] the same characters are NOT all periodic mod 6 (the 9 = lambda^4 part is needed)", not ok6)
    check("[K2] exactly 27 = 3^{|S|+1} distinct S-numerator characters (units mod cubes: 3 classes; valuations mod 3)",
          len(funcs) == 27, "distinct = %d (sextic analogue would be 6^3 = 216)" % len(funcs))
    # [K3] good numerators: n -> chi_n(m) is periodic mod 18*rad(m_good) iff every good valuation of m is 0 mod 3
    rng = random.Random(3)
    test_m = []
    small = [p for p in PRb if E.norm(p) <= 31]
    for _ in range(120):
        m = rng.choice(E.UNITS)
        mf = {}
        for p in rng.sample(small, 2):
            k = rng.randint(0, 4)
            if k:
                mf[p] = k
                m = emul(m, epow(p, k))
        m = emul(m, epow(lam, rng.randint(0, 2)))
        test_m.append((m, mf))
    ok3 = True
    for m, mf in test_m:
        excl = set(mf)
        # exceptional (character with conductor supported on S) iff periodic mod 18 on n prime to m
        seen, per = {}, True
        for el, fac in ns:
            if set(fac) & excl:
                continue
            val = chi_n(fac, m)
            key = red_mod(el, 18)
            if key in seen and seen[key] != val:
                per = False
                break
            seen[key] = val
        pred = all(k % 3 == 0 for k in mf.values())
        ok3 &= per == pred
    check("[K3] Kummer: n -> chi_n(m) is a ray character with conductor on S iff 3 | v_p(m) at every good p",
          ok3, "%d random m (good exponents 0..4 at two primes of norm <= 31)" % len(test_m))
    # [K4] (EMPIRICAL consistency) exceptional rows by the CHARACTER criterion = valuations 0 mod 3
    tests = primary_ideals(PRb, 1500)
    X = 3000
    allh = primary_ideals(PRb, X)
    exc_char, exc_val = 0, 0
    agree = True
    tprimes = sorted({p for _, tf in tests for p in tf}, key=E.norm)
    for el, fac in allh:
        h = emul(el, epow(lam, len(fac) % 3))          # include an S-part
        sy = {p: int(c3(p, *h)) for p in tprimes}
        seen, per = {}, True
        for tel, tfac in tests:
            if set(tfac) & set(fac):
                continue
            val = sum(sy[p] * k for p, k in tfac.items()) % 3
            key = red_mod(tel, 18)
            if key in seen and seen[key] != val:
                per = False
                break
            seen[key] = val
        pv = all(k % 3 == 0 for k in fac.values())
        exc_char += per
        exc_val += pv
        agree &= per == pv
    ncub = sum(1 for el, fac in allh if all(k % 3 == 0 for k in fac.values()))
    check("[K4] (h') exceptional by the character test <=> (h') = h_0 v^3 with h_0 an S-ideal (all good h' of norm <= 3000)",
          agree and exc_char == exc_val == ncub,
          "%d good h', %d exceptional (= cubes of good ideals), %d test n" % (len(allh), exc_char, len(tests)))
    # [K5] forced residues at a second-transform prime (no older moving character there):
    # child exponent at p is e_p + v_p(h'), unramified iff = 0 mod 3.  nonunit equal i: e_p = i + 1.
    p = PR[0]
    ok5, forced = True, {}
    for i in range(1, 7):
        for vh in range(0, 6):
            e = i + 1 + vh
            m = epow(p, e)
            seen, per = {}, True
            for el, fac in ns:
                if p in fac:
                    continue
                val = chi_n(fac, m)
                key = red_mod(el, 18)
                if key in seen and seen[key] != val:
                    per = False
                    break
                seen[key] = val
            if per:
                forced.setdefault(i, set()).add(vh % 3)
            ok5 &= per == (e % 3 == 0)
    fr = {i: sorted(s) for i, s in forced.items()}
    check("[K5] forced residue of v_p(h') at a nonunit prime of equal multiplicity i: -(i+1) mod 3 "
          "(i=1 -> 1, i=2 -> 0, i=4 -> 1)", ok5 and fr[1] == [1] and fr[2] == [0] and fr[4] == [1], str(fr))
    check("[K5-CTRL] the sextic residue class 4 (mod 6) is not the cubic answer for i = 2 (cubic forces 0, not 1)",
          fr[2] != [4 % 3])


# =============================================================================================
# [L] exact exponent ledger for the centred stage at theta = 1/3
# =============================================================================================
def part_L():
    import sympy as sp
    A, M, m, q, c, d, R, Ee, K, w, wo, Bc, g, l, g2, p2, t2, V, f, b2 = sp.symbols(
        "A M m q c d R E K w w_o B_c g ell g_2 p_2 t_2 V f b_2", real=True)

    def ledger(th):
        a0 = A - c - w
        K0 = 2 * A - c - d + R + Ee - m
        qt = q + R + Ee
        mp = 2 * a0 - K - g - g2 - V
        qp = qt + wo + t2 + V
        Mp = mp + qp
        Dchild = b2 - p2 + w + Bc + l
        lhs = th * (mp - f) + a0 - b2 - (Mp + Dchild)
        F1 = th * c + (1 - th) * (d + K0 - K) + 2 * th * w + th * qt + wo + Bc - (1 - th) * g + l
        F2 = 2 * b2 - (1 - th) * g2 - p2 + t2 + th * V + th * f
        rhs = A - (1 - th) * (m + q) - F1 - F2
        return sp.simplify(lhs - rhs), F1
    z3, F1c = ledger(sp.Rational(1, 3))
    z6, _ = ledger(sp.Rational(1, 6))
    check("[L1] (old-eq:2.15)-(2.16) at theta = 1/3: count Z^{(m'-f)/3} x volume / allowance = A - 2M/3 - F_1 - F_2 "
          "(sympy identity; theta = 1/6 reproduces the paper)", z3 == 0 and z6 == 0)
    # control: cubic count with the sextic F_1 coefficients does not close
    a0 = A - c - w
    K0 = 2 * A - c - d + R + Ee - m
    F1s = c / 6 + sp.Rational(5, 6) * (d + K0 - K) + w / 3 + (q + R + Ee) / 6 + wo + Bc - sp.Rational(5, 6) * g + l
    zc = sp.simplify(F1c - F1s)
    check("[L1-CTRL] the sextic F_1 differs from the cubic one (identity is theta-sensitive)", zc != 0)
    # F_1 on the J >= 0 branch: g = J = D0 - c - 2w + wo  ->  F_1 = c + 2w + qt/3 + wo/3 + Bc
    D0 = sp.Symbol("D0")
    F1J = (c / 3 + sp.Rational(2, 3) * D0 + sp.Rational(2, 3) * w + (q + R + Ee) / 3 + wo + Bc
           - sp.Rational(2, 3) * (D0 - c - 2 * w + wo) + l)
    check("[L2] cubic F_1 on the branch J >= 0 equals c + 2w + q~/3 + w_o/3 + B_c + ell (>= c + 2w: kappa_1 = 1)",
          sp.simplify(F1J - (c + 2 * w + (q + R + Ee) / 3 + wo / 3 + Bc + l)) == 0)
    # actual g <= J_+ + 2 sigma: the sigma loss in F_1 is (1 - theta) 2 sigma = 4 sigma / 3 (paper: 5 sigma / 3)
    check("[L3] terminal sigma-loss in F_1: (1-theta)*2*sigma = 4*sigma/3 for n = 3 (paper n = 6: 5*sigma/3)",
          (1 - Fr(1, 3)) * 2 == Fr(4, 3) and (1 - Fr(1, 6)) * 2 == Fr(5, 3))
    # centred deficit: max over v >= 0 of A - 2M/3 - kappa v - (L - v)_+ equals A - 2M/3 - kappa L at v = L
    ok = True
    for kap in (Fr(2, 3), Fr(5, 6), Fr(1)):
        for L in [Fr(k, 100) for k in range(20, 51)]:
            for Aq in [Fr(k, 100) for k in range(67, 102)]:
                vals = [(Aq - Fr(2, 3) - kap * v - max(Fr(0), L - v), v) for v in [L * Fr(t, 40) for t in range(0, 121)]]
                mx = max(vals)
                ok &= mx[0] == Aq - Fr(2, 3) - kap * L and mx[1] == L
    check("[L4] centred deficit max_v [A - 2M/3 - kappa v - (L-v)_+] = A - 2M/3 - kappa L, attained at v = L "
          "(kappa in {2/3, 5/6, 1}; exact grid)", ok)
    # two-stage nested windows with an extra uniform centred loss c*M: smallest A-grid margin
    def margin(b1, Atop, loss=Fr(0), kap=Fr(5, 6), grid=200):
        s0 = Fr(2, 3)
        worst = None
        for lo_, hi_, prev in ((s0, b1, s0), (b1, Atop, b1)):
            for t in range(1, grid + 1):
                Aq = lo_ + (hi_ - lo_) * Fr(t, grid)
                # best L maximises min( kap L - (A - s0) - loss , prev - (1 - A + 2L), A - 1/2 - L, A/2 - L )
                # piecewise linear in L: evaluate at breakpoints
                def mu(L):
                    return min(kap * L - (Aq - s0) - loss, prev - (1 - Aq + 2 * L), Aq - Fr(1, 2) - L)
                cands = [Fr(0), Aq / 2,
                         (prev - 1 + Aq + (Aq - s0) + loss) / (kap + 2),
                         (Aq - Fr(1, 2) + (Aq - s0) + loss) / (kap + 1)]
                best = max(mu(L) for L in cands if Fr(0) <= L <= Aq / 2)
                worst = best if worst is None else min(worst, best)
        return worst
    best = max((margin(Fr(b, 1000), Fr(1)), b) for b in range(840, 900, 3))
    best101 = max((margin(Fr(b, 1000), Fr(101, 100)), b) for b in range(840, 900, 3))
    check("[L5] two nested centred stages, kappa = 5/6: uniform margin over (2/3, 1] and (2/3, 1.01] is positive",
          best[0] > 0 and best101[0] > 0,
          "margin %.4f M (split %.3f) for A <= M; %.4f M (split %.3f) for A <= 1.01 M"
          % (float(best[0]), best[1] / 1000, float(best101[0]), best101[1] / 1000))


def main():
    PR = E.primes_upto(60)
    print("primes:", [(p, E.norm(p)) for p in PR[:9]])
    part_S(PR)
    print("  [%.0fs]" % (time.time() - T0))
    part_G(PR)
    print("  [%.0fs]" % (time.time() - T0))
    mx = part_F(PR)
    part_T(mx)
    print("  [%.0fs]" % (time.time() - T0))
    part_C(PR)
    print("  [%.0fs]" % (time.time() - T0))
    part_E(PR)
    print("  [%.0fs]" % (time.time() - T0))
    part_A(PR)
    print("  [%.0fs]" % (time.time() - T0))
    part_K(PR)
    print("  [%.0fs]" % (time.time() - T0))
    part_L()
    nf = sum(1 for _, o in RES if not o)
    print("\n%d/%d PASS  (%.0f s)" % (len(RES) - nf, len(RES), time.time() - T0))
    return nf


if __name__ == "__main__":
    sys.exit(main())
