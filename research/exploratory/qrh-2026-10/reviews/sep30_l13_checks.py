"""sep30_l13_checks.py -- exact checks of the local layer of Lemmas 13.2-13.4 (lem:prime-power-fourier,
lem:full-correlation, lem:complete-support-correlation) of the OpenAI QRH manuscript (30 Sep 2026;
pr908 paper.tex, sha256 42a5ee0f...deac6a3), plus floating spot checks for Lemma 4.5
(lem:smooth-calculus).  Line numbers refer to that file.

Every value of F(u,v;j), L_C and the predicted right sides is a sum of sixth roots of unity, so it
lies in Z[omega] = Z[zeta_6].  Parts A, B, C, X and N compare such values EXACTLY, as integer pairs
(a, b) <-> a + b*omega.  Part D compares sums that involve the additive character e(.), and does
so exactly in Z[zeta_L], by reduction modulo the cyclotomic polynomial Phi_L.  Only part S uses
floating point.

  A  Lemma 13.3, global formula (eq:correlation-lift) [l. 7081-7132]. For each configuration
     (u, v), F(u,v;j) is brute-forced from its definition (old-eq:2.11) for EVERY j mod uv. It is
     compared with chi_{n1}(k) conj chi_{n2}(-k) R(n1,n2) L_C(n1,n2;k), or with 0 when C does not
     divide j. Here R is the paper's four-class bicharacter (eq:reciprocity-four-class), and L_C
     is the product of the closed local factors (eq:correlation-local and the one-sided formula).
     Part A also checks four further claims:
     - L_C as a congruence sum agrees with the closed product for every k mod C;
     - F(u,v;0) = phi(u) 1_{u=v};
     - |L_C| <= q_C;
     - R(n1,n2) = chi_{n2}(n1) conj chi_{n1}(n2) on the coprime residual pair.
  B  The local factor L_{p^c}(n1,n2;k), exhaustively over k mod p^c and many (n1, n2). It is
     computed in two ways:
     - full (x,y)-grid brute force, for split P=7 (c<=3), P=13 (c<=2), inert 5 (P=25, c<=2) and
       inert 11 (P=121, c=1);
     - solution enumeration in Z/7^c for c = 4..7. This covers the principal branch 6 | c (c = 6)
       and c = 7 = 1 mod 6. Each y (or x) has exactly one partner, because the other residual is
       a unit mod p^c.
     Part B also checks periodicity modulo p (= rad C) in each residual column on the genuine
     locus. Finally, a field-level power sweep (modulus p, character chi_p^c, c = 1..12) covers
     the inert principal branch, which cannot be reached at c = 6 by enumeration.
  C  Lemma 13.4 (eq:correlation-child-character) [l. 7196-7229]. F(Da,Eb;j) is brute-forced for
     every j mod DEab and compared with F(D,E;j) R(a,E) conj R(b,D) R(a,b) chi_a(j) conj chi_b(-j).
     The configurations include D, E with shared primes of unequal multiplicity, D = 1 or E = 1,
     prime-power a, b, inert primes, and every R-factor equal to -1 somewhere.
  X  Off-locus statements [l. 7123-7131, 7231-7247]:
     - the artificial value 0 of L_C at p | (n1,n2) differs from the congruence sum there, as the
       paper warns;
     - F~_{D,E}(a,b;j) differs from F(Da,Eb;j) at some non-coprime (a,b);
     - the Moebius insertion identity holds exactly on a finite array.
  D  Exact Z[zeta_L] checks of e(.)-sums:
     - D1: the Fourier form F = (q_u q_v)^{-1/2} sum_h G(u,h) conj G(v,h) e(-jh/uv) of Lemma 13.3;
     - D2: Lemma 13.2 (eq:gauss-local). For 6 !| a it checks |S|^2 = P^{2a-1} 1_{v_p(k)=a-1}; for
       6 | a (a = 6, P = 7) it checks the integer value of S = q^{a/2} G.
  N  Failing controls. Each mutation of a displayed formula must be detected, i.e. produce at least
     one exact mismatch on the configurations of A, B and C. The mutations are: -1 -> +1;
     orientation n1/n2 -> n2/n1; P-2 -> P-1; dropping 1_{6|c} on the one-sided factor; dropping R;
     chi_{n2}(-k) -> chi_{n2}(k); phi(u) -> q_u; and, in 13.4, dropping R(a,b) or R(a,E), or
     chi_b(-j) -> chi_b(j).
  S  Lemma 4.5 spot checks (floating; EMPIRICAL):
     - the N-fold integration-by-parts identity behind eq:pointwise-mellin-tail, on W_G (Mellin
       e^{s^2}), with failing controls;
     - the derivative order 2m <= J+d+2 with 2m > J+d (exact);
     - the two elementary inequalities of eq:joint-gaussian-slice;
     - the explicit 1-D constant in eq:parameter-sobolev.

Ramified and S primes: the prime over 3 (lambda, norm 3) and the inert prime 2 (norm 4) lie in S.
(q-1)/6 is not an integer for them, so the sextic symbol and the lemmas are not defined there. No
check applies. Reuses a2/eis.py unchanged (read-only import).
Run: nice -n 10 python3 -I sep30_l13_checks.py
"""
import itertools
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
UA = np.array([u[0] for u in E.UNITS], dtype=np.int64)   # zeta^k = UA[k] + UB[k] omega
UB = np.array([u[1] for u in E.UNITS], dtype=np.int64)


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    sys.stdout.flush()


# ----------------------------------------------------------------------------------------------
# exact Z[omega] helpers (vectorized)
# ----------------------------------------------------------------------------------------------
def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


class Mod:
    """Canonical residues of O modulo n: HNF basis (d1, 0), (w0, g) of nO; residue (i, j) = i + j omega,
    0 <= i < d1, 0 <= j < g, flat index j*d1 + i."""

    def __init__(self, n):
        a1, b1 = n
        a2, b2 = E.mul(n, (0, 1))
        N = abs(a1 * b2 - a2 * b1)
        g, x, y = egcd(b1, b2)
        self.n, self.N, self.g, self.d1 = n, N, g, N // g
        self.w0 = x * a1 + y * a2
        assert N == E.norm(n) and (N // g) * g == N

    def red(self, z0, z1):
        z0 = np.asarray(z0, dtype=np.int64)
        z1 = np.asarray(z1, dtype=np.int64)
        j = z1 % self.g
        t = (z1 - j) // self.g
        i = (z0 - t * self.w0) % self.d1
        return i, j

    def idx(self, z0, z1):
        i, j = self.red(z0, z1)
        return j * self.d1 + i

    def residues(self):
        r = np.arange(self.N, dtype=np.int64)
        return r % self.d1, r // self.d1


def vmul(c, z0, z1):
    """c * z for a fixed element c and arrays z."""
    a, b = c
    return a * z0 - b * z1, a * z1 + b * z0 - b * z1


def elem(fac):
    r = (1, 0)
    for p, e in fac.items():
        for _ in range(e):
            r = E.mul(r, p)
    return r


def norm_fac(fac):
    return math.prod(E.norm(p) ** e for p, e in fac.items())


def phi_fac(fac):
    return math.prod(E.norm(p) ** (e - 1) * (E.norm(p) - 1) for p, e in fac.items() if e > 0)


_PT = {}


def ptab(p):
    """(Mod(p), table of sextic-symbol exponents on residues mod p; -1 marks p | x)."""
    if p not in _PT:
        M = Mod(p)
        X0, X1 = M.residues()
        tab = []
        for a, b in zip(X0.tolist(), X1.tolist()):
            s = E.sym_prime((a, b), p)
            tab.append(-1 if s is None else s)
        _PT[p] = (M, np.array(tab, dtype=np.int64))
    return _PT[p]


def chi_vec(fac, z0, z1):
    """exponent of chi_n(z), n = prod p^e, zero-extended (-1 marks the value 0)."""
    z0 = np.asarray(z0, dtype=np.int64)
    z1 = np.asarray(z1, dtype=np.int64)
    out = np.zeros(z0.shape, dtype=np.int64)
    zero = np.zeros(z0.shape, dtype=bool)
    for p, e in fac.items():
        if e == 0:
            continue
        M, tab = ptab(p)
        k = tab[M.idx(z0, z1)]
        zero |= k < 0
        out += e * np.where(k < 0, 0, k)
    out %= 6
    out[zero] = -1
    return out


def chi1(fac, z):
    return int(chi_vec(fac, [z[0]], [z[1]])[0])


def divides_fac(p, z):
    return E.divides(p, z)


# four-class bicharacter r(a,b) = Gamma(ab)/(Gamma(a)Gamma(b)), Gamma(c) = (1+i^{-b}+i^a+i^{b-a})/2
_I = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def Gamma4(c):
    a, b = c
    s = [1, 0]
    for e in (-b, a, b - a):
        s[0] += _I[e % 4][0]
        s[1] += _I[e % 4][1]
    assert s[0] % 2 == 0 and s[1] % 2 == 0, c
    g = (s[0] // 2, s[1] // 2)
    assert g in _I, (c, g)
    return _I.index(g)          # exponent of i


def r_bichar(a, b):
    e = (Gamma4(E.mul(a, b)) - Gamma4(a) - Gamma4(b)) % 4
    assert e in (0, 2)
    return 0 if e == 0 else 3          # as a zeta_6 exponent: +1 -> 0, -1 -> 3


def R_sym(afac, bfac):
    """chi_b(a) conj chi_a(b) on a coprime pair (zeta_6 exponent)."""
    a, b = elem(afac), elem(bfac)
    x, y = chi1(bfac, a), chi1(afac, b)
    assert x >= 0 and y >= 0
    return (x - y) % 6


def pairs_of(vi, ve):
    """integer vi times zeta^ve -> (a, b) arrays."""
    vi = np.asarray(vi, dtype=np.int64)
    ve = np.asarray(ve, dtype=np.int64) % 6
    return vi * UA[ve], vi * UB[ve]


def fmt(f):
    return "*".join("%s^%d" % (NAME.get(p, str(p)), e) if e > 1 else NAME.get(p, str(p)) for p, e in f.items()) or "1"


# ----------------------------------------------------------------------------------------------
# brute-force correlation F(u,v;j) for all j mod uv, from (old-eq:2.11)
# ----------------------------------------------------------------------------------------------
def F_table(ufac, vfac):
    u, v = elem(ufac), elem(vfac)
    uv = E.mul(u, v)
    Mu, Mv, Muv = Mod(u), Mod(v), Mod(uv)
    X0, X1 = Mu.residues()
    kx = chi_vec(ufac, X0, X1)
    s = kx >= 0
    X0, X1, kx = X0[s], X1[s], kx[s]
    Y0, Y1 = Mv.residues()
    ky = chi_vec(vfac, Y0, Y1)
    s = ky >= 0
    Y0, Y1, ky = Y0[s], Y1[s], ky[s]
    vx0, vx1 = vmul(v, X0, X1)
    uy0, uy1 = vmul(u, Y0, Y1)
    m0 = (vx0[:, None] - uy0[None, :]).ravel()
    m1 = (vx1[:, None] - uy1[None, :]).ravel()
    idx = Muv.idx(m0, m1)
    kk = ((kx[:, None] - ky[None, :]) % 6).ravel()
    T = np.bincount(idx * 6 + kk, minlength=Muv.N * 6).reshape(Muv.N, 6)
    return Muv, T @ UA, T @ UB


def L_table(Cfac, n1, n2):
    """genuine congruence sum L_C(n1,n2;k) = sum_{x,y mod C, n2 x - n1 y = k mod C} chi_C(x) conj chi_C(y),
    for every k mod C (Mod(C) index order)."""
    C = elem(Cfac)
    M = Mod(C)
    X0, X1 = M.residues()
    kx = chi_vec(Cfac, X0, X1)
    s = kx >= 0
    X0, X1, kx = X0[s], X1[s], kx[s]
    a0, a1 = vmul(n2, X0, X1)
    b0, b1 = vmul(n1, X0, X1)
    m0 = (a0[:, None] - b0[None, :]).ravel()
    m1 = (a1[:, None] - b1[None, :]).ravel()
    idx = M.idx(m0, m1)
    kk = ((kx[:, None] - kx[None, :]) % 6).ravel()
    T = np.bincount(idx * 6 + kk, minlength=M.N * 6).reshape(M.N, 6)
    return M, T @ UA, T @ UB


# ----------------------------------------------------------------------------------------------
# closed forms (with optional mutations for the failing controls)
# ----------------------------------------------------------------------------------------------
def L_closed(Cfac, n1, n2, k0, k1, mut=frozenset()):
    """artificial product extension of eq:correlation-local / one-sided formula; returns (int, exp)."""
    k0 = np.asarray(k0, dtype=np.int64)
    Li = np.ones(k0.shape, dtype=object)
    Le = np.zeros(k0.shape, dtype=np.int64)
    for p, c in Cfac.items():
        if c == 0:
            continue
        P = E.norm(p)
        Mp, tab = ptab(p)
        pk = tab[Mp.idx(k0, k1)] < 0
        d1, d2 = divides_fac(p, n1), divides_fac(p, n2)
        if not d1 and not d2:
            a1 = int(tab[int(Mp.idx([n1[0]], [n1[1]])[0])])
            a2 = int(tab[int(Mp.idx([n2[0]], [n2[1]])[0])])
            eA = (c * (a2 - a1)) % 6 if "orient" in mut else (c * (a1 - a2)) % 6
            if c % 6:
                base = np.where(pk, P - 1, 1 if "minus1" in mut else -1)
            else:
                base = np.where(pk, P - 1, P - 1 if "P2" in mut else P - 2)
            Li = Li * (P ** (c - 1)) * base.astype(object)
            Le = Le + eA
        elif d1 != d2:
            six = 1 if ("onesided_no6" in mut or c % 6 == 0) else 0
            base = np.where(pk, 0, (P - 1) * six)
            Li = Li * (P ** (c - 1)) * base.astype(object)
        else:
            Li = Li * 0
    return Li, Le % 6


def split_moduli(ufac, vfac):
    ps = set(ufac) | set(vfac)
    Cf = {p: min(ufac.get(p, 0), vfac.get(p, 0)) for p in ps}
    Cf = {p: c for p, c in Cf.items() if c > 0}
    n1f = {p: ufac.get(p, 0) - Cf.get(p, 0) for p in ps}
    n2f = {p: vfac.get(p, 0) - Cf.get(p, 0) for p in ps}
    return Cf, {p: e for p, e in n1f.items() if e}, {p: e for p, e in n2f.items() if e}


def pred_13_3(ufac, vfac, J0, J1, mut=frozenset()):
    Cf, n1f, n2f = split_moduli(ufac, vfac)
    C, n1, n2 = elem(Cf), elem(n1f), elem(n2f)
    NC = E.norm(C)
    w0, w1 = vmul(E.conj(C), J0, J1)
    div = (w0 % NC == 0) & (w1 % NC == 0)
    k0, k1 = w0 // NC, w1 // NC
    e1 = chi_vec(n1f, k0, k1)
    e2 = chi_vec(n2f, k0, k1) if "chi2_plus" in mut else chi_vec(n2f, -k0, -k1)
    eR = 0 if "dropR" in mut else r_bichar(n1, n2)
    Li, Le = L_closed(Cf, n1, n2, k0, k1, mut)
    ok = div & (e1 >= 0) & (e2 >= 0)
    vi = np.where(ok, Li, 0).astype(np.int64)
    ve = (np.where(e1 < 0, 0, e1) - np.where(e2 < 0, 0, e2) + eR + Le) % 6
    return pairs_of(vi, ve)


# ----------------------------------------------------------------------------------------------
# A. Lemma 13.3 global formula
# ----------------------------------------------------------------------------------------------
def configs_13_3():
    return [
        ({p7: 1}, {p7: 1}), ({p7: 2}, {p7: 2}), ({p7: 3}, {p7: 3}),
        ({p7: 2}, {p7: 1}), ({p7: 1}, {p7: 3}), ({p7: 3}, {p7: 2}),
        ({p7: 1, p13: 1}, {p7: 1, p7b: 1}),
        ({p7: 2, p13: 1}, {p7: 1, p19: 1}),
        ({p7: 1, p13: 1}, {p7: 2, p13: 1}),
        ({p7: 1}, {p13: 1}), ({p7: 1}, {p7b: 1}),
        ({p13: 1, p7: 1}, {p13: 1, p7b: 2}),
        ({p7b: 2, p19: 1}, {p7b: 2, p13: 1}),
        ({q5: 1}, {q5: 1}), ({q5: 2}, {q5: 2}), ({q5: 2}, {q5: 1}),
        ({q5: 1, p7: 1}, {q5: 1, p13: 1}), ({q5: 1, p7: 1}, {q5: 2, p7b: 1}),
        ({q11: 1}, {q11: 1}), ({q11: 1}, {q11: 1, p7: 1}),
        ({p19: 1, p31: 1}, {p19: 1, p31b: 1}),
    ]


def part_A(mut=frozenset(), quiet=False):
    total_j, mism, mism_L, Lchk = 0, 0, 0, 0
    zero_ok, bound_ok, Rcons = True, True, True
    for ufac, vfac in configs_13_3():
        Muv, Fa, Fb = F_table(ufac, vfac)
        J0, J1 = Muv.residues()
        Pa, Pb = pred_13_3(ufac, vfac, J0, J1, mut)
        bad = (Pa != Fa) | (Pb != Fb)
        mism += int(bad.sum())
        total_j += Muv.N
        # zero frequency (index 0 is j = 0)
        u, v = elem(ufac), elem(vfac)
        want = phi_fac(ufac) if u == v else 0
        if "phi_q" in mut and u == v:
            want = norm_fac(ufac)
        zero_ok &= (int(Fa[0]), int(Fb[0])) == (want, 0)
        Cf, n1f, n2f = split_moduli(ufac, vfac)
        if n1f and n2f:
            Rcons &= R_sym(n1f, n2f) == r_bichar(elem(n1f), elem(n2f))
        if Cf:
            n1, n2 = elem(n1f), elem(n2f)
            MC, La, Lb = L_table(Cf, n1, n2)
            K0, K1 = MC.residues()
            Li, Le = L_closed(Cf, n1, n2, K0, K1, mut)
            Qa, Qb = pairs_of(Li.astype(np.int64), Le)
            mism_L += int(((Qa != La) | (Qb != Lb)).sum())
            Lchk += MC.N
            qC = norm_fac(Cf)
            nrm = La * La - La * Lb + Lb * Lb
            bound_ok &= bool((nrm <= qC * qC).all())
        if not quiet:
            print("   A %-26s %-26s  j mod uv: %7d  mismatches %d" % (fmt(ufac), fmt(vfac), Muv.N, int(bad.sum())))
    if not quiet:
        check("A1 eq:correlation-lift (F = 0 unless C|j; chi_n1(k) conj chi_n2(-k) R(n1,n2) L_C) for every j, %d configs"
              % len(configs_13_3()), mism == 0, "%d (u,v,j) values, %d mismatches" % (total_j, mism))
        check("A2 L_C congruence sum = product of closed local factors (genuine locus, every k mod C)", mism_L == 0,
              "%d (C,k) values, %d mismatches" % (Lchk, mism_L))
        check("A3 F(u,v;0) = phi(u) 1_{u=v}", zero_ok)
        check("A4 |L_C| <= q_C on every computed value", bound_ok)
        check("A5 R(n1,n2) from symbols = four-class bicharacter r (eq:reciprocity-four-class)", Rcons)
    return mism + mism_L + (0 if zero_ok else 1)


# ----------------------------------------------------------------------------------------------
# B. local factor L_{p^c}
# ----------------------------------------------------------------------------------------------
def local_elems(p, c):
    """test residuals: units in every sixth-power class (two lifts differing by p each), and p*unit."""
    M, tab = ptab(p)
    X0, X1 = M.residues()
    reps = {}
    for a, b, k in zip(X0.tolist(), X1.tolist(), tab.tolist()):
        if k >= 0 and k not in reps:
            reps[k] = (a, b)
    units = [reps[k] for k in sorted(reps)]
    lifts = [E.mul((1, 0), x) for x in units[:3]]
    lifts = [(x[0] + p[0], x[1] + p[1]) for x in lifts]          # x + p: same class mod p, different mod p^2
    nonunits = [E.mul(p, units[1]), E.mul(p, units[4])]
    return units + lifts, nonunits


def part_B(mut=frozenset(), quiet=False, enum_cs=(4, 5, 6, 7)):
    mism, cases = 0, 0
    period_ok = True
    grid = [(p7, 1), (p7, 2), (p7, 3), (p13, 1), (p13, 2), (q5, 1), (q5, 2), (q11, 1)]
    for p, c in grid:
        units, nonunits = local_elems(p, c)
        Cf = {p: c}
        pairs = [(a, b) for a in units for b in units[:6]] + [(a, b) for a in nonunits for b in units[:4]] \
            + [(b, a) for a in nonunits for b in units[:4]] + [(a, b) for a in units[:6] for b in units[6:]]
        vals = {}
        for n1, n2 in pairs:
            MC, La, Lb = L_table(Cf, n1, n2)
            K0, K1 = MC.residues()
            Li, Le = L_closed(Cf, n1, n2, K0, K1, mut)
            Qa, Qb = pairs_of(Li.astype(np.int64), Le)
            mism += int(((Qa != La) | (Qb != Lb)).sum())
            cases += MC.N
            vals[(n1, n2)] = (La, Lb)
        # periodicity mod p in each column on the genuine locus: n1 -> n1 + p (lifts)
        for i in range(3):
            for n2 in units[:6]:
                A_ = vals[(units[i], n2)]
                B_ = vals[(units[6 + i], n2)]
                period_ok &= bool((A_[0] == B_[0]).all() and (A_[1] == B_[1]).all())
                A_ = vals[(n2, units[i])]
                B_ = vals[(n2, units[6 + i])]
                period_ok &= bool((A_[0] == B_[0]).all() and (A_[1] == B_[1]).all())
        if not quiet:
            print("   B grid p=%s c=%d: %d (n1,n2) pairs x %d k" % (NAME[p], c, len(pairs), E.norm(p) ** c))
    # solution enumeration in Z/7^c for c = 4..7 (split prime p7)
    P = 7
    M1, tab1 = ptab(p7)
    chi_int = {}
    for t in range(P):
        chi_int[t] = int(tab1[int(M1.idx([t], [0])[0])])
    ctab = np.array([chi_int[t] for t in range(P)], dtype=np.int64)
    units_int = []
    seen = set()
    for t in range(1, P):
        if ctab[t] not in seen:
            seen.add(ctab[t])
            units_int.append(t)
    for c in enum_cs:
        PC = P ** c
        Mc = Mod(elem({p7: c}))
        assert Mc.g == 1 and Mc.d1 == PC          # O/p^c = Z/P^c, omega -> -w0
        Cf = {p7: c}
        ks = [0, 1, 3, P, 2 * P, P ** (c - 1), 5 * P ** 2] + units_int
        ns = [(a, 0) for a in units_int] + [(a + P, 0) for a in units_int[:2]] + [(P, 0), (3 * P, 0)]
        y = np.arange(PC, dtype=np.int64)
        for n1 in ns:
            for n2 in ns:
                r1, r2 = n1[0] % PC, n2[0] % PC
                if r1 % P == 0 and r2 % P == 0:
                    continue
                for k in ks:
                    if r2 % P:                        # n2 unit: x = (k + n1 y)/n2
                        x = (pow(r2, -1, PC) * ((k + r1 * y) % PC)) % PC
                        assert ((r2 * x - r1 * y - k) % PC == 0).all()
                        ex, ey = ctab[x % P], ctab[y % P]
                    else:                             # n1 unit: y = (n2 x - k)/n1
                        x = y
                        yy = (pow(r1, -1, PC) * ((r2 * x - k) % PC)) % PC
                        assert ((r2 * x - r1 * yy - k) % PC == 0).all()
                        ex, ey = ctab[x % P], ctab[yy % P]
                    keep = (ex >= 0) & (ey >= 0)
                    kk = ((c * ex - c * ey) % 6)[keep]
                    cnt = np.bincount(kk, minlength=6)
                    La, Lb = int(cnt @ UA), int(cnt @ UB)
                    Li, Le = L_closed(Cf, n1, n2, [k], [0], mut)
                    Qa, Qb = pairs_of(np.array(Li, dtype=object).astype(np.int64), Le)
                    mism += int((int(Qa[0]), int(Qb[0])) != (La, Lb))
                    cases += 1
        if not quiet:
            print("   B enum p=7 c=%d: %d (n1,n2) x %d k (each over %d values)" % (c, len(ns) ** 2, len(ks), PC))
    # field-level power sweep: modulus p, character chi_p^c (c = 1..12), all k mod p
    sweep_bad = 0
    for p in (p7, p13, q5, q11):
        M, tab = ptab(p)
        X0, X1 = M.residues()
        units, nonunits = local_elems(p, 1)
        P = E.norm(p)
        for c in range(1, 13):
            for n1 in units[:6] + nonunits[:1]:
                for n2 in units[:6]:
                    for (m1, m2) in ((n1, n2), (n2, n1)):
                        a0, a1 = vmul(m2, X0, X1)
                        b0, b1 = vmul(m1, X0, X1)
                        kx = tab
                        s = kx >= 0
                        idx = M.idx((a0[s][:, None] - b0[s][None, :]).ravel(), (a1[s][:, None] - b1[s][None, :]).ravel())
                        kk = ((c * kx[s][:, None] - c * kx[s][None, :]) % 6).ravel()
                        T = np.bincount(idx * 6 + kk, minlength=M.N * 6).reshape(M.N, 6)
                        Fa, Fb = T @ UA, T @ UB
                        K0, K1 = M.residues()
                        Li, Le = L_closed({p: c}, m1, m2, K0, K1, mut)
                        Qa, Qb = pairs_of((Li // (P ** (c - 1))).astype(np.int64), Le)
                        sweep_bad += int(((Qa != Fa) | (Qb != Fb)).sum())
                        cases += M.N
    mism += sweep_bad
    if not quiet:
        check("B1 eq:correlation-local + one-sided formula, local factor L_{p^c}: grid (split 7,13; inert 5,11) "
              "and Z/7^c enumeration (c=4..7, incl. 6|c)", mism - sweep_bad == 0,
              "%d (n1,n2,k) cases, %d mismatches" % (cases, mism - sweep_bad))
        check("B2 field-level sweep: modulus p, character chi_p^c, c=1..12 (principal branch at inert 5, 11)",
              sweep_bad == 0, "%d mismatches" % sweep_bad)
        check("B3 genuine L_{p^c} periodic modulo p in each column (n_i -> n_i + p), c<=3", period_ok)
    return mism


# ----------------------------------------------------------------------------------------------
# C. Lemma 13.4
# ----------------------------------------------------------------------------------------------
def configs_13_4():
    return [
        ({p7: 1}, {p7: 1}, {p13: 1}, {p19: 1}),
        ({p7: 2}, {p7: 1}, {p13: 1}, {p19: 1}),
        ({p7: 1}, {p7: 2}, {p13: 1}, {p7b: 1}),
        ({p7: 1, q5: 1}, {p7: 1}, {p13: 1}, {p7b: 1}),
        ({p7: 1}, {p13: 1}, {p19: 1}, {p7b: 1}),
        ({}, {p7: 1}, {p13: 2}, {p19: 1}),
        ({p7: 2}, {}, {p13: 1}, {p7b: 2}),
        ({p7: 1}, {p7: 1}, {}, {p13: 1, p19: 1}),
        ({p7: 1}, {p7: 1}, {q5: 1}, {p13: 1}),
        ({p13: 1}, {p13: 1}, {p19: 1}, {p31: 1}),
        ({p19: 1}, {p19: 1}, {p31: 1}, {p7: 1}),
        ({p7b: 1}, {p7b: 2}, {p19: 1}, {p31: 1}),
        ({p31: 1}, {p31: 1}, {p19: 1}, {p13: 1}),
        ({p7: 1, p13: 1}, {p7: 1, p13: 1}, {p19: 1}, {}),
        ({p7: 2}, {p7: 2}, {p13: 1}, {}),
    ]


def pred_13_4(Df, Ef, af, bf, J0, J1, FDE, mut=frozenset()):
    D, Ee, a, b = elem(Df), elem(Ef), elem(af), elem(bf)
    MDE, Fa, Fb = FDE
    jj = MDE.idx(J0, J1)
    f_a, f_b = Fa[jj], Fb[jj]
    eR = 0
    if "drop_RaE" not in mut:
        eR += r_bichar(a, Ee)
    eR += r_bichar(b, D)        # conj of a sign is itself
    if "drop_Rab" not in mut:
        eR += r_bichar(a, b)
    ea = chi_vec(af, J0, J1)
    eb = chi_vec(bf, J0, J1) if "chib_plus" in mut else chi_vec(bf, -J0, -J1)
    ok = (ea >= 0) & (eb >= 0)
    e = (np.where(ea < 0, 0, ea) - np.where(eb < 0, 0, eb) + eR) % 6
    # (f_a + f_b omega) * zeta^e
    za, zb = UA[e], UB[e]
    ra = f_a * za - f_b * zb
    rb = f_a * zb + f_b * za - f_b * zb
    return np.where(ok, ra, 0), np.where(ok, rb, 0)


def coprime_fac(f, g):
    return not (set(f) & set(g))


def part_C(mut=frozenset(), quiet=False):
    mism, tot = 0, 0
    signs = {"R(a,E)": set(), "R(b,D)": set(), "R(a,b)": set()}
    for Df, Ef, af, bf in configs_13_4():
        assert coprime_fac(af, bf) and coprime_fac(af, {**Df, **Ef}) and coprime_fac(bf, {**Df, **Ef})
        uf = dict(Df)
        uf.update(af)
        vf = dict(Ef)
        vf.update(bf)
        Muv, Fa, Fb = F_table(uf, vf)
        FDE = F_table(Df, Ef)
        J0, J1 = Muv.residues()
        Pa, Pb = pred_13_4(Df, Ef, af, bf, J0, J1, FDE, mut)
        bad = int(((Pa != Fa) | (Pb != Fb)).sum())
        mism += bad
        tot += Muv.N
        D, Ee, a, b = elem(Df), elem(Ef), elem(af), elem(bf)
        signs["R(a,E)"].add(r_bichar(a, Ee))
        signs["R(b,D)"].add(r_bichar(b, D))
        signs["R(a,b)"].add(r_bichar(a, b))
        if not quiet:
            print("   C D=%-12s E=%-12s a=%-10s b=%-10s j: %6d nonzero F: %6d mismatches %d"
                  % (fmt(Df), fmt(Ef), fmt(af), fmt(bf), Muv.N, int(((Fa != 0) | (Fb != 0)).sum()), bad))
    if not quiet:
        check("C1 eq:correlation-child-character, every j mod DEab, %d configs" % len(configs_13_4()), mism == 0,
              "%d (config,j) values, %d mismatches" % (tot, mism))
        check("C2 the configurations realise each R-factor = -1 at least once",
              all(3 in s for s in signs.values()), str({k: sorted(v) for k, v in signs.items()}))
    return mism


# ----------------------------------------------------------------------------------------------
# X. off-locus statements
# ----------------------------------------------------------------------------------------------
def part_X():
    # (i) artificial zero of L_C at p | (n1, n2) vs the congruence sum there
    diffs = 0
    for p, c in [(p7, 1), (p7, 2), (q5, 1)]:
        units, nonunits = local_elems(p, c)
        MC, La, Lb = L_table({p: c}, nonunits[0], nonunits[1])
        diffs += int(((La != 0) | (Lb != 0)).sum())
    check("X1 at p | (n1,n2) the congruence sum is not the artificial value 0 (paper's own caveat, l. 7123-7131)",
          diffs > 0, "%d nonzero congruence-sum values where the extension is 0" % diffs)
    # (ii) F~ vs F at non-coprime (a, b), and (iii) Moebius insertion identity
    Df, Ef = {p7: 1}, {p7: 1}
    alist = [{}, {p13: 1}, {p19: 1}, {p13: 1, p19: 1}, {p13: 2}]
    rng = random.Random(3)
    FDE = F_table(Df, Ef)
    js = None
    lhs, rhs = None, None
    off_diff = 0
    for af in alist:
        for bf in alist:
            cab = rng.randint(-5, 5)
            uf = dict(Df)
            uf.update(af)
            vf = dict(Ef)
            vf.update(bf)
            # evaluate at a fixed list of frequencies j in O
            if js is None:
                js = [(0, 0), (1, 0), (2, 1), (7, -3), (13, 4), (-9, 11), (91, 0), (3, 30)]
                J0 = np.array([j[0] for j in js])
                J1 = np.array([j[1] for j in js])
                lhs = np.zeros((2, len(js)), dtype=np.int64)
                rhs = np.zeros((2, len(js)), dtype=np.int64)
            Ft = pred_13_4(Df, Ef, af, bf, J0, J1, FDE)
            common = set(af) & set(bf)
            mob = sum((-1) ** len(S) for r in range(len(common) + 1) for S in itertools.combinations(sorted(common), r))
            rhs += cab * mob * np.array(Ft)
            if not common:
                Muv, Fa, Fb = F_table(uf, vf)
                ii = Muv.idx(J0, J1)
                lhs += cab * np.array([Fa[ii], Fb[ii]])
            else:
                Muv, Fa, Fb = F_table(uf, vf)
                ii = Muv.idx(J0, J1)
                off_diff += int(((Fa[ii] != Ft[0]) | (Fb[ii] != Ft[1])).sum())
    check("X2 F~_{D,E}(a,b;j) != F(Da,Eb;j) at some non-coprime (a,b) (paper: 'artificial', l. 7243)", off_diff > 0,
          "%d differing (a,b,j) values" % off_diff)
    check("X3 Moebius insertion: sum_{(a,b)=1} c F(Da,Eb;j) = sum c F~ sum_{t|a,b} mu(t) (exact)",
          bool((lhs == rhs).all()))


# ----------------------------------------------------------------------------------------------
# D. exact cyclotomic checks: Fourier form of Lemma 13.3, and Lemma 13.2
# ----------------------------------------------------------------------------------------------
_RM = {}


def reduction_matrix(L):
    """rows: x^k mod Phi_L for k = 0..L-1 (integer coefficients, length phi(L))."""
    if L in _RM:
        return _RM[L]
    import sympy
    x = sympy.Symbol("x")
    phi = [int(c) for c in sympy.Poly(sympy.cyclotomic_poly(L, x), x).all_coeffs()][::-1]   # low -> high
    deg = len(phi) - 1
    M = np.zeros((L, deg), dtype=object)
    r = [0] * deg
    r[0] = 1
    for k in range(L):
        M[k] = r
        top = r[-1]
        r = [0] + r[:-1]
        if top:
            r = [r[i] - top * phi[i] for i in range(deg)]
    assert max(abs(int(v)) for v in M.ravel()) < 2 ** 30
    M = M.astype(np.int64)
    _RM[L] = M
    return M


def is_zero_cyclo(vec, L):
    M = reduction_matrix(L)
    vec = np.asarray(vec, dtype=object)
    assert max(abs(int(v)) for v in vec) < 2 ** 30
    red = vec.astype(np.int64) @ M
    return bool((red == 0).all())


def dcoef(z0, z1, n):
    """omega-coefficient of z * conj(n): e(z/n) = exp(2 pi i d / N(n))."""
    c = E.conj(n)
    return z0 * c[1] + z1 * c[0] - z1 * c[1]


def part_D():
    # D1: q_u q_v F(u,v;j) = sum_h S_u(h) conj S_v(h) e(-jh/uv)  in Z[zeta_L], L = lcm(6, N(uv))
    cfgs = [({p7: 1}, {p7: 1}), ({p7: 1}, {p7: 2}), ({p7: 2}, {p7: 1}), ({p7: 1}, {p13: 1}),
            ({p7: 1}, {p7b: 1}), ({q5: 1}, {q5: 1})]
    bad, tot = 0, 0
    rng = random.Random(17)
    for ufac, vfac in cfgs:
        u, v = elem(ufac), elem(vfac)
        uv = E.mul(u, v)
        Nu, Nv, Nuv = E.norm(u), E.norm(v), E.norm(uv)
        L = 6 * Nuv // math.gcd(6, Nuv)
        Muv, Fa, Fb = F_table(ufac, vfac)
        Mu, Mv = Mod(u), Mod(v)
        X0, X1 = Mu.residues()
        kx = chi_vec(ufac, X0, X1)
        s = kx >= 0
        X0, X1, kx = X0[s], X1[s], kx[s]
        Y0, Y1 = Mv.residues()
        ky = chi_vec(vfac, Y0, Y1)
        s = ky >= 0
        Y0, Y1, ky = Y0[s], Y1[s], ky[s]
        H0, H1 = Muv.residues()
        J0, J1 = Muv.residues()
        jlist = list(range(Muv.N)) if Muv.N <= 400 else [0] + rng.sample(range(1, Muv.N), 40)
        # per-h phases
        hx0, hx1 = (H0[:, None] * X0[None, :] - H1[:, None] * X1[None, :]), (H0[:, None] * X1[None, :] + H1[:, None] * X0[None, :] - H1[:, None] * X1[None, :])
        ex = ((L // 6) * kx[None, :] + (L // Nu) * (dcoef(hx0, hx1, u) % Nu)) % L
        hy0, hy1 = (H0[:, None] * Y0[None, :] - H1[:, None] * Y1[None, :]), (H0[:, None] * Y1[None, :] + H1[:, None] * Y0[None, :] - H1[:, None] * Y1[None, :])
        ey = ((L // 6) * ky[None, :] + (L // Nv) * (dcoef(hy0, hy1, v) % Nv)) % L
        pair = (ex[:, :, None] - ey[:, None, :])          # (h, x, y)
        for ji in jlist:
            j0, j1 = int(J0[ji]), int(J1[ji])
            jh0, jh1 = j0 * H0 - j1 * H1, j0 * H1 + j1 * H0 - j1 * H1
            ej = ((L // Nuv) * (dcoef(jh0, jh1, uv) % Nuv)) % L
            tot_e = (pair - ej[:, None, None]) % L
            vec = np.bincount(tot_e.ravel(), minlength=L).astype(object)
            vec[0] -= Nu * Nv * int(Fa[ji])
            vec[L // 3] -= Nu * Nv * int(Fb[ji])
            bad += 0 if is_zero_cyclo(vec, L) else 1
            tot += 1
    check("D1 Fourier form of F (Lemma 13.3, first display) exact in Z[zeta_L], 6 configs (split, inert)",
          bad == 0, "%d (config,j) values, %d failures" % (tot, bad))
    # control: drop the conj on G(v,h) (use G(v,h)) -> must fail somewhere
    ufac, vfac = {p7: 1}, {p7: 1}
    u = elem(ufac)
    Nuv = E.norm(E.mul(u, u))
    L = 6 * Nuv // math.gcd(6, Nuv)
    Muv, Fa, Fb = F_table(ufac, vfac)
    Mu = Mod(u)
    X0, X1 = Mu.residues()
    kx = chi_vec(ufac, X0, X1)
    s = kx >= 0
    X0, X1, kx = X0[s], X1[s], kx[s]
    H0, H1 = Muv.residues()
    hx0 = H0[:, None] * X0[None, :] - H1[:, None] * X1[None, :]
    hx1 = H0[:, None] * X1[None, :] + H1[:, None] * X0[None, :] - H1[:, None] * X1[None, :]
    ex = ((L // 6) * kx[None, :] + (L // 7) * (dcoef(hx0, hx1, u) % 7)) % L
    ctrl_fail = 0
    for ji in range(Muv.N):
        j0, j1 = int(H0[ji]), int(H1[ji])
        jh0, jh1 = j0 * H0 - j1 * H1, j0 * H1 + j1 * H0 - j1 * H1
        ej = ((L // Nuv) * (dcoef(jh0, jh1, E.mul(u, u)) % Nuv)) % L
        tot_e = (ex[:, :, None] + ex[:, None, :] - ej[:, None, None]) % L   # G(v,h) without conj
        vec = np.bincount(tot_e.ravel(), minlength=L).astype(object)
        vec[0] -= 49 * int(Fa[ji])
        vec[L // 3] -= 49 * int(Fb[ji])
        ctrl_fail += 0 if is_zero_cyclo(vec, L) else 1
    check("D1c control: G(u,h) G(v,h) without conjugation is detected", ctrl_fail > 0, "%d failing j" % ctrl_fail)

    # D2: Lemma 13.2. S(p^a,k) = sum_{x mod p^a} chi_p(x)^a e(kx/p^a) = q^{a/2} G(p^a,k)
    bad2, tot2 = 0, 0
    for p, a in [(p7, 1), (p7, 2), (p7, 3), (p13, 1), (p13, 2), (q5, 1), (q5, 2), (q11, 1)]:
        n = elem({p: a})
        P = E.norm(p)
        M = Mod(n)
        L = 6 * M.N // math.gcd(6, M.N)
        X0, X1 = M.residues()
        kx = chi_vec({p: a}, X0, X1)
        s = kx >= 0
        X0, X1, kx = X0[s], X1[s], kx[s]
        K0, K1 = M.residues()
        klist = range(M.N) if M.N <= 400 else [0] + random.Random(5).sample(range(1, M.N), 60)
        for ki in klist:
            k0, k1 = int(K0[ki]), int(K1[ki])
            z0, z1 = vmul((k0, k1), X0, X1)
            e = ((L // 6) * kx + (L // M.N) * (dcoef(z0, z1, n) % M.N)) % L
            # valuation of k at p
            vk, kk = 0, (k0, k1)
            if kk == (0, 0):
                vk = 10 ** 9
            else:
                while E.divides(p, kk):
                    c = E.mul(kk, E.conj(p))
                    kk = (c[0] // P, c[1] // P)
                    vk += 1
            if a % 6:
                prod = (e[:, None] - e[None, :]) % L
                vec = np.bincount(prod.ravel(), minlength=L).astype(object)
                vec[0] -= P ** (2 * a - 1) if vk == a - 1 else 0
            else:
                vec = np.bincount(e, minlength=L).astype(object)
                vec[0] -= (P ** a if vk >= a else 0) - (P ** (a - 1) if vk >= a - 1 else 0)
            bad2 += 0 if is_zero_cyclo(vec, L) else 1
            tot2 += 1
    # 6 | a at P = 7, a = 6: principal (zero-extended) character, phases of order 7^6. In Z[zeta_{7^6}]
    # a vector is zero iff it is constant on every coset r + 7^5 Z.
    a, P = 6, 7
    PC = P ** a
    M1, tab1 = ptab(p7)
    Mn = Mod(elem({p7: a}))
    assert Mn.g == 1 and Mn.d1 == PC
    xs = np.arange(PC, dtype=np.int64)
    unit = xs % P != 0
    for k in [0, 1, 3, P, 2 * P, P ** 4, 3 * P ** 5, P ** 5, P ** 6 - P ** 5]:
        # e(kx/p^a) on Z/7^a: the additive character of O/p^a = Z/P^a is t -> exp(2 pi i c t / P^a) for a unit c;
        # compute it from dcoef on the element (k*x, 0) to stay faithful to e(.)
        d = (dcoef((k * xs) % PC, np.zeros_like(xs), elem({p7: a})) % PC)[unit]
        vec = np.bincount(d, minlength=PC).astype(np.int64)
        kv = k % PC
        vk = 10 ** 9 if kv == 0 else next(i for i in range(a + 1) if kv % P ** (i + 1))
        want = (P ** a if vk >= a else 0) - (P ** (a - 1) if vk >= a - 1 else 0)
        vec[0] -= want
        V = vec.reshape(P, PC // P)
        ok = bool((V == V[0]).all())
        bad2 += 0 if ok else 1
        tot2 += 1
    check("D2 Lemma 13.2 (eq:gauss-local) exact: |S|^2 = P^{2a-1} 1_{v=a-1} (6!|a) and S integer formula (a=6, P=7)",
          bad2 == 0, "%d (p^a,k) values, %d failures" % (tot2, bad2))


# ----------------------------------------------------------------------------------------------
# N. failing controls
# ----------------------------------------------------------------------------------------------
def part_N():
    for m in ["minus1", "orient", "P2", "onesided_no6"]:
        nb = part_B(frozenset([m]), quiet=True, enum_cs=(6,))
        check("N control eq:correlation-local mutated '%s' is detected" % m, nb > 0, "%d mismatches" % nb)
    for m in ["dropR", "chi2_plus", "phi_q", "orient", "minus1"]:
        na = part_A(frozenset([m]), quiet=True)
        check("N control eq:correlation-lift mutated '%s' is detected" % m, na > 0, "%d mismatches" % na)
    for m in ["drop_Rab", "drop_RaE", "chib_plus"]:
        nc = part_C(frozenset([m]), quiet=True)
        check("N control eq:correlation-child-character mutated '%s' is detected" % m, nc > 0, "%d mismatches" % nc)


# ----------------------------------------------------------------------------------------------
# S. Lemma 4.5 spot checks (floating; EMPIRICAL)
# ----------------------------------------------------------------------------------------------
def part_S():
    # S1: M W(s) = (-iT)^{-N} int F_sigma^{(N)}(u) e^{iTu} du, F^{(N)} = e^{sigma u} sum_j C(N,j) sigma^{N-j} D^j W(e^u),
    #     for W_G(y) = exp(-(log y)^2/4)/(2 sqrt pi), whose Mellin transform is e^{s^2} (Lemma 4.6).
    u = np.linspace(-60.0, 60.0, 240001)
    du = u[1] - u[0]
    g = np.exp(-u * u / 4) / (2 * math.sqrt(math.pi))
    # (d/du)^j g = (-1/2)^j He_j-type: use exact recursion g_j = P_j(u) g with P_{j+1} = P_j' - (u/2) P_j
    polys = [np.poly1d([1.0])]
    for _ in range(8):
        Pj = polys[-1]
        polys.append(np.polyder(Pj) - np.poly1d([0.5, 0.0]) * Pj)
    worst, worst_c1, worst_c2 = 0.0, 0.0, 0.0
    for sig in (-1.0, 0.3, 2.0):
        for T in (0.7, 1.5, 3.0):
            s = complex(sig, T)
            ref = np.exp(s * s)
            for N in range(0, 6):
                FN = np.exp(sig * u) * sum(math.comb(N, j) * sig ** (N - j) * polys[j](u) for j in range(N + 1)) * g
                integ = (FN * np.exp(1j * T * u)).sum() * du
                val = (-1j * T) ** (-N) * integ
                worst = max(worst, abs(val - ref) / abs(ref))
                if N % 2 == 1:
                    worst_c1 = max(worst_c1, abs((1j * T) ** (-N) * integ - ref) / abs(ref))
                if N >= 2 and sig != 0:
                    FN2 = np.exp(sig * u) * sum(polys[j](u) for j in range(N + 1)) * g
                    worst_c2 = max(worst_c2, abs((-1j * T) ** (-N) * (FN2 * np.exp(1j * T * u)).sum() * du - ref) / abs(ref))
    check("S1 eq:pointwise-mellin-tail IBP identity on W_G (sigma in {-1,.3,2}, T in {.7,1.5,3}, N<=5) [FLOAT]",
          worst < 1e-7, "max rel dev %.1e" % worst)
    check("S1c controls: (iT)^{-N} for odd N, and dropping the binomial weights, are detected [FLOAT]",
          worst_c1 > 1e-3 and worst_c2 > 1e-3, "rel dev %.2f, %.2f" % (worst_c1, worst_c2))
    # S2: derivative order: m = floor((J+d)/2)+1 has J+d < 2m <= J+d+2, and int (1+|t|)^J (1+|t|^2)^{-m} d^dt < oo
    ok = True
    for J in range(0, 30):
        for d in range(1, 8):
            m = (J + d) // 2 + 1
            ok &= (2 * m > J + d) and (2 * m <= J + d + 2) and (J + d - 1 - 2 * m < -1)
            m2 = m - 1
            ok &= not (2 * m2 > J + d)       # m is the least admissible
    check("S2 smooth-calculus order: least m with 2m > J+d has 2m <= J+d+2 (J<30, d<8; exact)", ok)
    # S3: elementary inequalities of eq:joint-gaussian-slice
    rng = np.random.default_rng(1)
    T, v, w = (rng.standard_cauchy(200000) * 5 for _ in range(3))
    i1 = 1 + abs(T) <= (1 + abs(T + v)) * (1 + abs(v)) + 1e-9
    i2 = 1 + abs(T) + abs(v) + abs(w) <= 2 * (1 + abs(T + v)) * (1 + abs(v)) * (1 + abs(w)) + 1e-9
    i3 = 1 + abs(T) + abs(v) + abs(w) <= 1.0 * (1 + abs(T + v)) * (1 + abs(v)) * (1 + abs(w)) + 1e-9
    check("S3 joint-slice inequalities hold on 2e5 Cauchy samples; the factor 2 is needed (control) [FLOAT]",
          bool(i1.all() and i2.all() and not i3.all()), "factor-1 violations: %d" % int((~i3).sum()))
    # S4: 1-D eq:parameter-sobolev with the proof's explicit constant: sup_I |F|^2 <= (2/3) int |F|^2 + 6 int |F'|^2
    #     over I + [-1, 1] (length 3), on random trigonometric polynomials and narrow bumps.
    x = np.linspace(-1.0, 2.0, 30001)
    dx = x[1] - x[0]
    inI = (x >= 0) & (x <= 1)
    worst_ratio = 0.0
    for trial in range(300):
        K = rng.integers(1, 12)
        a = rng.standard_normal(K) / (1 + np.arange(K))
        ph = rng.uniform(0, 2 * np.pi, K)
        fr = rng.uniform(0, 3 * K, K)
        F = sum(a[i] * np.cos(fr[i] * x + ph[i]) for i in range(K))
        if trial % 3 == 0:
            c, wdt = rng.uniform(0, 1), 10 ** rng.uniform(-2, 0)
            F = np.exp(-((x - c) / wdt) ** 2)
        dF = np.gradient(F, dx)
        rhs = (2 / 3) * (F * F).sum() * dx + 6 * (dF * dF).sum() * dx
        worst_ratio = max(worst_ratio, (F[inI] ** 2).max() / rhs)
    check("S4 1-D parameter-Sobolev with explicit constant (2/3, 6): max sup/rhs over 300 tests <= 1 [FLOAT]",
          worst_ratio <= 1.0, "max ratio %.3f" % worst_ratio)


# ----------------------------------------------------------------------------------------------
def main():
    global p7, p7b, p13, p13b, p19, q5, p31, p31b, q11, NAME
    t0 = time.time()
    PR = E.primes_upto(130)
    byn = {}
    for q in PR:
        byn.setdefault(E.norm(q), []).append(q)
    p7, p7b = byn[7]
    p13, p13b = byn[13]
    p19 = byn[19][0]
    q5 = byn[25][0]
    p31, p31b = byn[31]
    q11 = byn[121][0]
    NAME = {p7: "p7", p7b: "p7'", p13: "p13", p13b: "p13'", p19: "p19", q5: "q5", p31: "p31", p31b: "p31'",
            q11: "q11"}
    print("primes:", {v: k for k, v in NAME.items()})
    for nm, n in (("lambda", (1, 2)), ("2", (2, 0))):
        print("   N/A: prime %s has norm %d; (N-1)/6 = %s is not an integer, so it lies in S and chi is undefined"
              % (nm, E.norm(n), (E.norm(n) - 1) / 6))
    part_A()
    part_B()
    part_C()
    part_X()
    part_D()
    part_N()
    part_S()
    nf = sum(1 for _, o in RES if not o)
    print("\n%d/%d PASS   (%.0f s)" % (len(RES) - nf, len(RES), time.time() - t0))
    return nf


if __name__ == "__main__":
    sys.exit(main())
