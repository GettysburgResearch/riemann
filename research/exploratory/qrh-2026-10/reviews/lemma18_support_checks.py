"""lemma18_support_checks.py -- exact-symbol and exhaustive checks of the complete-common-support
allocations in the two finite Poisson transforms of Lemma 18.1 (lem:plain) of the OpenAI QRH
manuscript (30 Sep 2026; pr908 paper.tex, sha256 42a5ee0f...deac6a3).  Line numbers refer to it.

What is checked (each prints PASS/FAIL):

  A  abstract-UFD exhaustive checks (exponent vectors on 3 primes, exponents 0..7):
     A1 (n,n') <-> (C,D,a,b) complete-common-support decomposition is a bijection with
        rad C = rad D, (a,b)=1, (ab,CD)=1                                    [l. 13192-13196]
     A2 R <= p, E <= p - R; local data r = 1_{6 !| i-j}                     [l. 13209-13217]
     A3 (old-eq:2.6) B_c + B_d <= c + d - 2p - R with random positive log-weights,
        and the list of local (i,j) where the first-transform slack is zero  [l. 13384-13408]
     A4 Moebius over the divisor lattice: sum_{s | a, s | b} mu(s) = 1_{(a,b)=1}
                                                                          [l. 13300-13306, 13889-13897]
     A5 t-allocation identity 1_{t | n1 n2 p_slot} = prod_p sum_{J != 0} (-1)^{|J|+1} prod 1_{p|n_i},
        with "two divisor primes selecting one prime slot" giving zero      [l. 13905-13923]
  B  exact sextic symbols in Z[omega]:
     B1 chi_C(k) conj chi_D(k) = xi_r(k) 1_{(k, c/r)=1} for all k mod rad    [l. 13211-13224]
     B2 xi_r primitive: sum_{x mod r} xi_r(x) e(xh/r) = conj xi_r(h) tau(xi_r), |tau|^2 = q_r
     B3 CRT factorization of the Gauss sum modulo r a b (a, b may be prime powers)  [l. 13250-13262]
     B4 R(a,b) := chi_b(a) conj chi_a(b) equals the fixed four-class bicharacter
        Gamma(ab)/(Gamma(a)Gamma(b)) on coprime primary pairs                [l. 857-870, 940-945]
  D  end-to-end first-transform bridge (eq:first-poisson-bridge) with nontrivial complete
     common support: the lattice sum sum_k exp(-pi N(k)/H) chi_{Ca}(k) conj chi_{Db}(k) equals the
     paper's display (sum over e | c/r of mu(e) xi_r(e) H/(q_e sqrt q_r sqrt(q_a q_b))
     G_xi(r,h) tau_C(a) conj tau_D(b) conj R(a,b) G(a,h) conj G(b,-h) kernel), with a Gaussian
     test function so that both sides are computable to rounding error.     [l. 13226-13268]
  E  Lemma complete-support-correlation (eq:correlation-child-character), brute force from the
     definition (old-eq:2.11) of F(u,v;j)                                   [l. 7196-7230, 13712-13718]
  F  single-prime correlation table of the second transform: F(p^i, p^j0; j) by solving the
     congruence in Z/7^(i+j0); checks the vanishing pattern, eq:correlation-local, the unequal
     formula P^{j0-1}(P-1) chi_p(k)^{i-j0}, and the absolute table at l. 13742-13751.
  L  exact-rational ledgers for the Moebius labels: s (first transform) nets to zero; the
     t-count identity (old-eq:2.18h); the clipped-shell bound; (old-eq:2.19) maximum at v = L.

Floating point is used only in B2, B3, D, E, F, where both sides are finite sums of roots of unity
(times a Gaussian in D); tolerances are stated.  Reuses a2/eis.py unchanged (read-only import).
Run: nice -n 10 python3 -I lemma18_support_checks.py
"""
import cmath
import itertools
import math
import os
import random
import sys
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "a2"))
import eis as E  # noqa: E402

RES = []


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    sys.stdout.flush()


# ----------------------------------------------------------------------------------------------
# A. abstract UFD checks
# ----------------------------------------------------------------------------------------------
def part_A():
    NP, EMAX = 3, 7
    vecs = list(itertools.product(range(EMAX + 1), repeat=NP))
    seen = {}
    ok_bij, ok_props, ok_RE = True, True, True
    for n in vecs:
        for m in vecs:
            common = [k for k in range(NP) if n[k] > 0 and m[k] > 0]
            C = tuple(n[k] if k in common else 0 for k in range(NP))
            D = tuple(m[k] if k in common else 0 for k in range(NP))
            a = tuple(n[k] - C[k] for k in range(NP))
            b = tuple(m[k] - D[k] for k in range(NP))
            radC = tuple(1 if C[k] else 0 for k in range(NP))
            radD = tuple(1 if D[k] else 0 for k in range(NP))
            ok_props &= radC == radD
            ok_props &= all(not (a[k] and b[k]) for k in range(NP))          # (a,b)=1
            ok_props &= all(not ((a[k] or b[k]) and radC[k]) for k in range(NP))  # (ab,CD)=1
            key = (C, D, a, b)
            if key in seen:
                ok_bij = False
            seen[key] = (n, m)
            ok_bij &= tuple(C[k] + a[k] for k in range(NP)) == n and tuple(D[k] + b[k] for k in range(NP)) == m
            r = [k for k in common if (C[k] - D[k]) % 6]
            p = len(common)
            ok_RE &= len(r) <= p and (p - len(r)) >= 0
    # surjectivity: random admissible (C,D,a,b) with rad C = rad D, (a,b)=1, (ab,CD)=1 round-trip
    rng0 = random.Random(5)
    ok_onto, cnt = True, 0
    while cnt < 20000:
        C = tuple(rng0.randint(0, EMAX) for _ in range(NP))
        D = tuple((rng0.randint(1, EMAX) if C[k] else 0) for k in range(NP))
        a = tuple((0 if C[k] else rng0.choice([0, 0, rng0.randint(1, EMAX)])) for k in range(NP))
        b = tuple((0 if (C[k] or a[k]) else rng0.choice([0, rng0.randint(1, EMAX)])) for k in range(NP))
        if max(C[k] + a[k] for k in range(NP)) > EMAX or max(D[k] + b[k] for k in range(NP)) > EMAX:
            continue
        n = tuple(C[k] + a[k] for k in range(NP))
        m = tuple(D[k] + b[k] for k in range(NP))
        ok_onto &= seen.get((C, D, a, b)) == (n, m)
        cnt += 1
    check("A1 complete-common-support decomposition is a bijection (3 primes, exps 0..7)",
          ok_bij and ok_props and ok_onto and len(seen) == len(vecs) ** 2, "pairs=%d, round-trips=%d" % (len(seen), cnt))
    check("A2 R <= p and E <= p - R for every pair", ok_RE)

    # A3: (2.6) with random log-weights, 4 primes, exps 0..9 on common primes
    rng = random.Random(7)
    worst = None
    okA3 = True
    for _ in range(20000):
        k = rng.randint(1, 4)
        w = [Fr(rng.randint(1, 50), rng.randint(1, 7)) for _ in range(k)]
        ij = [(rng.randint(1, 12), rng.randint(1, 12)) for _ in range(k)]
        c = sum(wi * i for wi, (i, j) in zip(w, ij))
        d = sum(wi * j for wi, (i, j) in zip(w, ij))
        p = sum(w)
        R = sum(wi for wi, (i, j) in zip(w, ij) if (i - j) % 6)
        Bc = max(Fr(0), (3 * c - 5 * d - R) / 6)
        Bd = max(Fr(0), (3 * d - 5 * c - R) / 6)
        slack = c + d - 2 * p - R - Bc - Bd
        okA3 &= slack >= 0
        worst = slack if worst is None else min(worst, slack)
    zero_local = [(i, j) for i in range(1, 40) for j in range(1, i + 1)
                  if Fr(i + j - 2 - (1 if (i - j) % 6 else 0)) - max(Fr(0), Fr(3 * i - 5 * j - (1 if (i - j) % 6 else 0), 6)) == 0]
    check("A3 (2.6) B_c+B_d <= c+d-2p-R, 20000 random multi-prime configurations",
          okA3 and worst == 0, "min slack=%s; zero-slack local (i,j), i>=j: %s" % (worst, zero_local))

    # A4: Moebius on divisor lattice (squarefree s | a and s | b)
    okA4 = True
    for a in itertools.product(range(4), repeat=4):
        for b in itertools.product(range(4), repeat=4):
            tot = 0
            for s in itertools.product(range(2), repeat=4):
                if all(s[k] <= min(a[k], b[k]) for k in range(4)):
                    tot += (-1) ** sum(s)
            okA4 &= tot == (1 if all(min(a[k], b[k]) == 0 for k in range(4)) else 0)
    check("A4 sum_{s|a,s|b} mu(s) = 1_{(a,b)=1} (4 primes, exps 0..3)", okA4)

    # A5: t-allocation identity.  Primes 0..3; plain variables n1, n2 (exponent vectors) and one
    # slot which is a single prime (index) or absent.  For squarefree t (subset of primes),
    # 1_{t | n1 n2 slot} = sum over assignments J_p (nonempty subsets of {n1,n2,slot}) of
    # prod_p (-1)^{|J_p|+1} * [selected plain variables divisible by the product of their selected
    # primes] * [slot selected only by primes equal to it, and by at most one prime].
    okA5 = True
    nchk = 0
    for n1 in itertools.product(range(3), repeat=3):
        for n2 in itertools.product(range(3), repeat=3):
            for slot in [None, 0, 1, 2]:
                full = [n1[k] + n2[k] + (1 if slot == k else 0) for k in range(3)]
                for t in itertools.product(range(2), repeat=3):
                    tp = [k for k in range(3) if t[k]]
                    lhs = 1 if all(full[k] >= 1 for k in tp) else 0
                    rhs = 0
                    for Js in itertools.product([1, 2, 3, 4, 5, 6, 7], repeat=len(tp)):
                        # bitmask: 1=n1, 2=n2, 4=slot
                        sign = 1
                        d1 = [0] * 3
                        d2 = [0] * 3
                        slot_sel = []
                        for k, J in zip(tp, Js):
                            sign *= (-1) ** (bin(J).count("1") + 1)
                            if J & 1:
                                d1[k] += 1
                            if J & 2:
                                d2[k] += 1
                            if J & 4:
                                slot_sel.append(k)
                        if len(slot_sel) > 1:
                            continue           # two distinct divisor primes select one prime slot: zero
                        if slot_sel and slot != slot_sel[0]:
                            continue
                        if all(n1[k] >= d1[k] for k in range(3)) and all(n2[k] >= d2[k] for k in range(3)):
                            rhs += sign
                    okA5 &= lhs == rhs
                    nchk += 1
    check("A5 t-allocation inclusion-exclusion identity (exhaustive)", okA5, "%d cases" % nchk)


# ----------------------------------------------------------------------------------------------
# Z[omega] helpers (exact)
# ----------------------------------------------------------------------------------------------
def egcd(a, b):
    if b == 0:
        return (a, 1, 0) if a >= 0 else (-a, -1, 0)
    g, x, y = egcd(b, a % b)
    return (g, y, x - (a // b) * y)


class Mod:
    """Canonical residues of O modulo n (HNF of the lattice nO in the basis 1, omega)."""

    def __init__(self, n):
        v1, v2 = n, E.mul(n, (0, 1))
        a1, b1 = v1
        a2, b2 = v2
        N = abs(a1 * b2 - a2 * b1)
        g, x, y = egcd(b1, b2)
        self.n, self.N, self.g, self.d1 = n, N, g, N // g
        self.w = (x * a1 + y * a2, g)
        assert self.N == E.norm(n)

    def red(self, z):
        j = z[1] % self.g
        t = (z[1] - j) // self.g
        i = (z[0] - t * self.w[0]) % self.d1
        return (i, j)

    def idx(self, z):
        i, j = self.red(z)
        return j * self.d1 + i

    def residues(self):
        return [(i, j) for j in range(self.g) for i in range(self.d1)]


def prod(elems):
    r = (1, 0)
    for x in elems:
        r = E.mul(r, x)
    return r


def elem(fac):
    return prod([E.mul((1, 0), p) for p, e in fac.items() for _ in range(e)])


_symcache = {}


def sym(u, p):
    """(u/p)_6 code 0..5, or None if p | u."""
    M = _symcache.get(("M", p))
    if M is None:
        M = Mod(p)
        _symcache[("M", p)] = M
    key = (M.red(u), p)
    v = _symcache.get(key, "x")
    if v == "x":
        v = E.sym_prime(u, p)
        _symcache[key] = v
    return v


ZETA = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]


def chi(fac, u):
    """chi_n(u) for n = prod p^e (fac dict), zero-extended; complex."""
    s = 0
    for p, e in fac.items():
        if e == 0:
            continue
        k = sym(u, p)
        if k is None:
            return 0.0
        s += k * e
    return ZETA[s % 6]


def neg(z):
    return (-z[0], -z[1])


def gauss_table(fac, nfac_exp=None):
    """G(n,h) = q_n^{-1/2} sum_{x mod n} chi_n(x) e(hx/n) for all canonical h mod n.
    nfac_exp: optional dict p -> exponent used in the character (for xi_r); default = fac."""
    n = elem(fac)
    M = Mod(n)
    R = M.residues()
    cf = nfac_exp if nfac_exp is not None else fac
    cv = np.array([chi(cf, x) for x in R], dtype=complex)
    X0 = np.array([x[0] for x in R], dtype=np.int64)
    X1 = np.array([x[1] for x in R], dtype=np.int64)
    cn = E.conj(n)
    N = M.N
    # omega-coefficient of x*h*conj(n): (x*conj n) first
    y0 = X0 * cn[0] - X1 * cn[1]
    y1 = X0 * cn[1] + X1 * cn[0] - X1 * cn[1]
    tab = np.zeros(len(R), dtype=complex)
    for hi, h in enumerate(R):
        d = (y0 * h[1] + y1 * h[0] - y1 * h[1]) % N
        tab[hi] = (cv * np.exp(2j * np.pi * d / N)).sum()
    return M, tab / math.sqrt(N)


# ----------------------------------------------------------------------------------------------
# B. symbols, primitivity, CRT, reciprocity
# ----------------------------------------------------------------------------------------------
def part_B(PR):
    p7, p7b, p13, p13b, p19, p19b, q5, p31 = PR[0], PR[1], PR[2], PR[3], PR[4], PR[5], PR[6], PR[7]
    # B1
    okB1 = True
    for (Ce, De) in [({p7: 1, p7b: 2, p13: 7}, {p7: 1, p7b: 1, p13: 1}),
                     ({p7: 5, q5: 3}, {p7: 2, q5: 9}),
                     ({p13: 6, p7b: 1}, {p13: 12, p7b: 4})]:
        cr = list(Ce)
        rr = {p: (Ce[p] - De[p]) % 6 for p in cr if (Ce[p] - De[p]) % 6}
        comp = [p for p in cr if (Ce[p] - De[p]) % 6 == 0]
        M = Mod(prod(cr))
        for k in M.residues():
            lhs = chi(Ce, k) * np.conj(chi(De, k))
            rhs = chi(rr, k) * (0.0 if any(sym(k, p) is None for p in comp) else 1.0)
            okB1 &= abs(lhs - rhs) < 1e-12
    check("B1 chi_C conj chi_D = xi_r * 1_{(k, c/r)=1} (exact symbols, all k mod rad)", okB1)

    # B2 primitivity of xi_r
    okB2, worst = True, 0.0
    for rr in [{p7b: 1}, {p7: 3, p13: 2}, {q5: 5}, {p7: 2, p7b: 4, p13: 1}]:
        n = elem({p: 1 for p in rr})
        M = Mod(n)
        R = M.residues()
        # recompute with modulus rad(r) and character xi_r
        cv = [chi(rr, x) for x in R]
        tau = sum(cv[i] * E.e_of(R[i], n) for i in range(len(R)))
        okB2 &= abs(abs(tau) ** 2 - M.N) < 1e-8
        for h in R:
            g = sum(cv[i] * E.e_of(E.mul(R[i], h), n) for i in range(len(R)))
            pred = np.conj(chi(rr, h)) * tau
            worst = max(worst, abs(g - pred))
    okB2 &= worst < 1e-8
    check("B2 xi_r primitive mod r: Gauss sum = conj xi_r(h) tau(xi_r) for all h", okB2, "max dev %.1e" % worst)

    # B3 CRT factorization: sum_{x mod rab} xi_r(x) chi_a(x) conj chi_b(x) e(xh/(rab))
    #   = xi_r(ab) chi_a(rb) conj chi_b(ra) * sqrt(q_r) G_xi(r,h) * sqrt(q_a) G(a,h) * sqrt(q_b) conj G(b,-h)
    worst = 0.0
    nh = 0
    for rr, af, bf in [({p7: 1}, {p13: 1}, {p19: 1}),
                       ({p7: 3}, {p7b: 2}, {p13: 1}),
                       ({p7b: 2, p13b: 5}, {p19: 1}, {q5: 1}),
                       ({p13: 4}, {p7: 1}, {p7b: 2})]:
        rad_r = {p: 1 for p in rr}
        r_el, a_el, b_el = elem(rad_r), elem(af), elem(bf)
        Q = prod([r_el, a_el, b_el])
        MQ = Mod(Q)
        RQ = MQ.residues()
        X0 = np.array([x[0] for x in RQ], dtype=np.int64)
        X1 = np.array([x[1] for x in RQ], dtype=np.int64)
        gv = np.array([chi(rr, x) * chi(af, x) * np.conj(chi(bf, x)) for x in RQ], dtype=complex)
        cq = E.conj(Q)
        y0 = X0 * cq[0] - X1 * cq[1]
        y1 = X0 * cq[1] + X1 * cq[0] - X1 * cq[1]
        Mr, Gr = gauss_table(rad_r, rr)
        Ma, Ga = gauss_table(af)
        Mb, Gb = gauss_table(bf)
        ph = chi(rr, E.mul(a_el, b_el)) * chi(af, E.mul(r_el, b_el)) * np.conj(chi(bf, E.mul(r_el, a_el)))
        sq = math.sqrt(MQ.N)
        hs = RQ if len(RQ) <= 2000 else random.Random(1).sample(RQ, 2000)
        for h in hs:
            d = (y0 * h[1] + y1 * h[0] - y1 * h[1]) % MQ.N
            lhs = (gv * np.exp(2j * np.pi * d / MQ.N)).sum()
            rhs = ph * sq * Gr[Mr.idx(h)] * Ga[Ma.idx(h)] * np.conj(Gb[Mb.idx(neg(h))])
            worst = max(worst, abs(lhs - rhs) / sq)
            nh += 1
    check("B3 CRT factorization of the Gauss sum mod r a b (prime powers allowed)", worst < 1e-8,
          "%d frequencies, max dev/sqrt(q_Q) %.1e" % (nh, worst))

    # B4 reciprocity bicharacter
    def Gam(c):
        a, b = c
        return (1 + 1j ** ((-b) % 4) + 1j ** (a % 4) + 1j ** ((b - a) % 4)) / 2

    gens = []
    for es in itertools.product(range(3), repeat=4):
        fac = {p: e for p, e in zip([p7, p7b, p13, q5], es) if e}
        gens.append((fac, elem(fac)))
    for es in itertools.product(range(2), repeat=4):
        fac = {p: e for p, e in zip([p13b, p19, p19b, p31], es) if e}
        gens.append((fac, elem(fac)))
    okB4, n4 = True, 0
    for fa, a in gens:
        for fb, b in gens:
            if set(fa) & set(fb):
                continue
            Rab = chi(fb, a) * np.conj(chi(fa, b))
            frak = Gam(E.mul(a, b)) / (Gam(a) * Gam(b))
            okB4 &= abs(Rab - frak) < 1e-12
            n4 += 1
    check("B4 chi_b(a) conj chi_a(b) = Gamma(ab)/(Gamma(a)Gamma(b)) (fixed mod-4 bicharacter)", okB4,
          "%d coprime primary pairs" % n4)


# ----------------------------------------------------------------------------------------------
# D. end-to-end first-transform bridge
# ----------------------------------------------------------------------------------------------
def lattice_points(Nmax):
    out = []
    bmax = int(2 * math.sqrt(Nmax / 3)) + 2
    for b in range(-bmax, bmax + 1):
        disc = Nmax - 0.75 * b * b
        if disc < 0:
            continue
        lo = int(math.floor(b / 2 - math.sqrt(disc))) - 1
        hi = int(math.ceil(b / 2 + math.sqrt(disc))) + 1
        for a in range(lo, hi + 1):
            n = a * a - a * b + b * b
            if n <= Nmax:
                out.append(((a, b), n))
    return out


def part_D(PR, H, cfgs, cut=36.0):
    p = PR
    for name, ij, af, bf in cfgs:
        common = list(ij)
        Cf = {q: ij[q][0] for q in common}
        Df = {q: ij[q][1] for q in common}
        rr = {q: (ij[q][0] - ij[q][1]) % 6 for q in common if (ij[q][0] - ij[q][1]) % 6}
        comp = [q for q in common if (ij[q][0] - ij[q][1]) % 6 == 0]
        CA = dict(Cf)
        CA.update(af)
        DB = dict(Df)
        DB.update(bf)
        # LHS
        k0 = complex(0.31, 0.17) * math.sqrt(H)          # shift: breaks the unit symmetry
        R0 = math.sqrt(cut * H / math.pi) + abs(k0)
        pts = lattice_points(R0 * R0)
        lhs, mass = 0.0 + 0.0j, 0.0
        for k, n in pts:
            if n == 0:
                continue
            f = chi(CA, k) * np.conj(chi(DB, k))
            kc = E.to_complex(k) if hasattr(E, "to_complex") else complex(k[0] - 0.5 * k[1], k[1] * math.sqrt(3) / 2)
            wgt = math.exp(-math.pi * abs(kc - k0) ** 2 / H)
            lhs += wgt * f
            mass += wgt * abs(f)
        # RHS: paper's display, summed over e | c/r and all h (h = 0 included)
        rad_r = {q: 1 for q in rr}
        r_el, a_el, b_el = elem(rad_r), elem(af), elem(bf)
        q_r, q_a, q_b = E.norm(r_el), E.norm(a_el), E.norm(b_el)
        Q = prod([r_el, a_el, b_el])
        qQ = E.norm(Q)
        Mr, Gr = gauss_table(rad_r, rr) if rr else (None, None)
        Ma, Ga = gauss_table(af) if af else (None, None)
        Mb, Gb = gauss_table(bf) if bf else (None, None)
        rhs = 0.0 + 0.0j
        terms = []
        for sub in itertools.product(range(2), repeat=len(comp)):
            efac = {q: 1 for q, s in zip(comp, sub) if s}
            e_el = elem(efac)
            q_e = E.norm(e_el)
            mu = (-1) ** len(efac)
            er = E.mul(e_el, r_el)
            tauC = chi(af, er) * chi(rr, a_el)                 # tau_C(a) without tau
            tauD = chi(bf, er) * np.conj(chi(rr, b_el))        # tau_D(b) without tau
            Rbar = chi(af, b_el) * np.conj(chi(bf, a_el))      # conj R(a,b) = chi_a(b) conj chi_b(a)
            scal = mu * chi(rr, e_el)                          # scalar in the frozen labels
            pref = (2 / math.sqrt(3)) * H / (q_e * math.sqrt(q_r) * math.sqrt(q_a * q_b))
            scale = 3.0 * qQ * q_e / (4 * math.pi * H)
            hs = lattice_points(cut * scale)
            s = 0.0 + 0.0j
            Qc = complex(Q[0] - 0.5 * Q[1], Q[1] * math.sqrt(3) / 2)
            ec = complex(e_el[0] - 0.5 * e_el[1], e_el[1] * math.sqrt(3) / 2)
            for h, nh in hs:
                hc = complex(h[0] - 0.5 * h[1], h[1] * math.sqrt(3) / 2)
                xi = 2j * hc.conjugate() / (math.sqrt(3) * Qc.conjugate())   # dual-lattice point
                eta = xi / ec.conjugate()
                ker = math.exp(-4 * math.pi * H * nh / (3.0 * qQ * q_e)) \
                    * cmath.exp(-2j * math.pi * (eta * k0.conjugate()).real)
                gx = Gr[Mr.idx(h)] if rr else 1.0
                ga = Ga[Ma.idx(h)] if af else 1.0
                gb = np.conj(Gb[Mb.idx(neg(h))]) if bf else 1.0
                s += ker * gx * ga * gb
            rhs += scal * pref * tauC * np.conj(tauD) * Rbar * s
            terms.append((len(efac), scal, pref, tauC, np.conj(tauD), Rbar, s, chi(rr, e_el)))
        dev = abs(lhs - rhs)
        # negative controls: each mutation of the allocation data must be detected
        muts = {
            "only e=1 (no complementary-mask Moebius)": sum(t[1] * t[2] * t[3] * t[4] * t[5] * t[6] for t in terms if t[0] == 0),
            "drop xi_r(e)": sum(t[1] / (t[7] if t[7] != 0 else 1) * t[2] * t[3] * t[4] * t[5] * t[6] for t in terms),
            "drop conj R(a,b)": sum(t[1] * t[2] * t[3] * t[4] * t[6] for t in terms),
            "1/(q_a q_b) instead of 1/sqrt(q_a q_b)": sum(t[1] * t[2] * t[3] * t[4] * t[5] * t[6] for t in terms)
            / math.sqrt(q_a * q_b),
        }
        detected = [k for k, v in muts.items() if abs(v - lhs) > 1e-6 * max(1.0, abs(lhs))]
        undetected = [k for k in muts if k not in detected]
        check("D bridge %s" % name, dev < 1e-8 * max(1.0, mass),
              "lhs=%.6f%+.6fi rhs=%.6f%+.6fi |dev|=%.1e mass=%.1f" % (lhs.real, lhs.imag, rhs.real, rhs.imag, dev, mass))
        print("     negative controls detected: %s; not applicable/undetected: %s" % (detected, undetected))


# ----------------------------------------------------------------------------------------------
# E. complete-support correlation, brute force
# ----------------------------------------------------------------------------------------------
def F_brute(ufac, vfac, js):
    u, v = elem(ufac), elem(vfac)
    Mu, Mv = Mod(u), Mod(v)
    Ru, Rv = Mu.residues(), Mv.residues()
    cu = np.array([chi(ufac, x) for x in Ru], dtype=complex)
    cv = np.conj(np.array([chi(vfac, y) for y in Rv], dtype=complex))
    X0 = np.array([x[0] for x in Ru], dtype=np.int64)
    X1 = np.array([x[1] for x in Ru], dtype=np.int64)
    Y0 = np.array([y[0] for y in Rv], dtype=np.int64)
    Y1 = np.array([y[1] for y in Rv], dtype=np.int64)
    vx0 = X0 * v[0] - X1 * v[1]
    vx1 = X0 * v[1] + X1 * v[0] - X1 * v[1]
    uy0 = Y0 * u[0] - Y1 * u[1]
    uy1 = Y0 * u[1] + Y1 * u[0] - Y1 * u[1]
    m = E.mul(u, v)
    cm, Nm = E.conj(m), E.norm(m)
    out = []
    for j in js:
        d0 = vx0[:, None] - uy0[None, :] - j[0]
        d1 = vx1[:, None] - uy1[None, :] - j[1]
        z0 = d0 * cm[0] - d1 * cm[1]
        z1 = d0 * cm[1] + d1 * cm[0] - d1 * cm[1]
        ok = (z0 % Nm == 0) & (z1 % Nm == 0)
        out.append((cu[:, None] * cv[None, :] * ok).sum())
    return out


def part_E(PR):
    p7, p7b, p13, p13b, p19 = PR[0], PR[1], PR[2], PR[3], PR[4]
    cfgs = [("D=E=p7; a=p13,b=p7'", {p7: 1}, {p7: 1}, {p13: 1}, {p7b: 1}),
            ("D=E=p7^2; a=p13,b=p7'", {p7: 2}, {p7: 2}, {p13: 1}, {p7b: 1}),
            ("D=E=p7 p13; a=p19,b=p7'", {p7: 1, p13: 1}, {p7: 1, p13: 1}, {p19: 1}, {p7b: 1}),
            ("D=E=p7; a=p13^2,b=p19", {p7: 1}, {p7: 1}, {p13: 2}, {p19: 1}),
            ("D=p7^2,E=p7 (unequal, min 1: must vanish); a=p13,b=p7'", {p7: 2}, {p7: 1}, {p13: 1}, {p7b: 1})]
    rng = random.Random(11)
    for name, Df, Ef, af, bf in cfgs:
        a_el, b_el = elem(af), elem(bf)
        D_el, E_el = elem(Df), elem(Ef)
        js = [(0, 0), (1, 0), (2, 1)]
        for base in [D_el, E_el, E.mul(D_el, E_el), a_el, b_el, prod([D_el, a_el])]:
            for _ in range(3):
                t = (rng.randint(-4, 4), rng.randint(-4, 4))
                js.append(E.mul(base, t))
        for _ in range(6):
            js.append((rng.randint(-30, 30), rng.randint(-30, 30)))
        uf = dict(Df)
        uf.update(af)
        vf = dict(Ef)
        vf.update(bf)
        lhs = F_brute(uf, vf, js)
        fDE = F_brute(Df, Ef, js)

        def Rb(xf, x, yf, y):          # R(x,y) = chi_y(x) conj chi_x(y)
            return chi(yf, x) * np.conj(chi(xf, y))

        worst, nz = 0.0, 0
        for j, L, f0 in zip(js, lhs, fDE):
            rhs = f0 * Rb(af, a_el, Ef, E_el) * np.conj(Rb(bf, b_el, Df, D_el)) * Rb(af, a_el, bf, b_el) \
                * chi(af, j) * np.conj(chi(bf, neg(j)))
            worst = max(worst, abs(L - rhs))
            nz += abs(L) > 1e-6
        check("E complete-support correlation %s" % name, worst < 1e-7,
              "%d frequencies (%d nonzero), max dev %.1e" % (len(js), nz, worst))


# ----------------------------------------------------------------------------------------------
# F. single-prime correlation table in Z/7^K
# ----------------------------------------------------------------------------------------------
def part_F(PR):
    pi = PR[0]
    p = E.norm(pi)
    assert p == 7
    # Hensel-lift the root r of t^2+t+1 with pi -> 0 mod p
    a, b = pi
    r = (-a * pow(b, -1, p)) % p
    tab = [sym((c, 0), pi) for c in range(p)]           # chi_pi on integer representatives

    def lift(K):
        rk = r
        mod = p
        while mod < p ** K:
            mod = min(mod * mod, p ** K)
            f = (rk * rk + rk + 1) % mod
            df = (2 * rk + 1) % mod
            rk = (rk - f * pow(df, -1, mod)) % mod
        assert (rk * rk + rk + 1) % p ** K == 0 and rk % p == r
        return rk

    def chival(x, e):
        k = tab[x % p]
        return 0.0 if k is None else ZETA[(k * e) % 6]

    worst_table = 0.0
    fails = []
    ncase = 0
    pairs = [(i, j0) for i in range(1, 8) for j0 in range(1, 8) if i + j0 <= 13] + [(7, 6), (6, 7)]
    pairs = sorted(set(pairs))
    for i, j0 in pairs:
        K = i + j0
        pK = p ** K
        rk = lift(K)
        w = (a + b * rk) % pK                       # image of pi, valuation 1
        assert w % p == 0 and w % (p * p) != 0
        eps = w // p
        inv_eps = pow(eps, -1, pK)
        wi = pow(w, i, pK)
        y = np.arange(p ** j0, dtype=np.int64)
        cy = np.array([np.conj(chival(int(t), j0)) for t in range(p)])[y % p]
        units = [1, 3, 5]
        for v in range(0, K + 1):
            for un in units:
                if v == K and un != 1:
                    continue
                J = (pow(w, v, pK) * un) % pK if v < K else 0
                T = (J + (wi * y) % pK) % pK
                okm = (T % p ** j0) == 0
                x = ((T // p ** j0) * pow(inv_eps, j0, pK)) % p ** i
                cx = np.array([chival(int(t), i) for t in range(p)])[x % p]
                F = (cx * cy * okm).sum()
                g = min(i, j0)
                P = p
                # predicted values (lem:full-correlation and the text at l. 13722-13734)
                if v < g:
                    pred = 0.0
                elif i == j0:
                    kunit = (v == i)            # divided frequency j/G_c is a unit at p
                    kval = (J // pow(w, i, pK)) % p if v < K else 0
                    if i % 6:
                        pred = P ** (i - 1) * (-1.0 if kunit else (P - 1.0))
                    else:
                        pred = P ** (i - 1) * ((P - 2.0) if kunit else (P - 1.0))
                else:
                    g6 = (g % 6 == 0)
                    if g6 and v == g:
                        # J = w^g * k with k a unit: chi_pi(k)^{|i-j0|} (on the larger side; conj if j0 > i)
                        kk = (J // pow(p, g)) * pow(pow(eps, g, pK), -1, pK) % pK
                        val = chival(int(kk), abs(i - j0))
                        if j0 > i:
                            # F(p^i, p^j0; j): the excess is on the second side: conj chi_p(-k)^{j0-i}
                            val = np.conj(chival(int((-kk) % pK), j0 - i))
                        pred = P ** (g - 1) * (P - 1.0) * val
                    else:
                        pred = 0.0
                dev = abs(F - pred)
                if dev > 1e-6 * max(1.0, abs(pred)):
                    fails.append((i, j0, v, un, F, pred))
                # absolute table l. 13742-13751
                if i == j0 and i % 6 and v == i:
                    bound = P ** (i - 1)
                elif i == j0:
                    bound = P ** i
                elif v == g:
                    bound = P ** g
                else:
                    bound = 0.0
                worst_table = max(worst_table, abs(F) - bound)
                ncase += 1
    check("F single-prime correlation: vanishing, eq:correlation-local, unequal formula (p=7, i,j0<=7, (7,6))",
          not fails, "%d cases; first failures: %s" % (ncase, fails[:3]))
    check("F absolute table |F(p^i,p^j0;j)| <= P^{g2-t2} locally (l. 13742-13751)", worst_table < 1e-6,
          "max(|F|-bound) = %.2e" % worst_table)


# ----------------------------------------------------------------------------------------------
# L. exact-rational ledgers for the Moebius labels
# ----------------------------------------------------------------------------------------------
def part_L():
    grid = [Fr(k, 4) for k in range(0, 17)]
    # s in the first transform: count s0 + (1/2)(-s0 - s0) = 0 ; second transform: count (p2 - s0)
    # against allowance -s0: net p2.
    ok = all(s0 + Fr(1, 2) * (-s0 - s0) == 0 for s0 in grid)
    check("L1 s-label nets to zero in the first-transform ledger", ok)
    # (old-eq:2.18h): t_- - r1 - r2 - (r - r1)_+ = (t_- - r2) - max(r, r1)
    ok = True
    for t_, r1, r2, r in itertools.product(grid[:9], repeat=4):
        ok &= t_ - r1 - r2 - max(Fr(0), r - r1) == (t_ - r2) - max(r, r1)
    check("L2 (2.18h) identity", ok)
    # with t_- <= r2 + omega2 the t-count never costs more than omega2 - r (and volume form without r)
    ok = True
    for t_, r1, r2, r, om in itertools.product(grid[:7], grid[:7], grid[:7], grid[:7], [Fr(0), Fr(1, 8)]):
        if t_ <= r2 + om and t_ <= r1 + om:
            ok &= (t_ - r1 - r2 - max(Fr(0), r - r1)) <= om - r
            ok &= t_ - (r1 + r2) / 2 <= om
    check("L3 t-count bounded by the extraction coefficients (clipped-shell / exceptional sums)", ok)
    # (old-eq:2.19): max_v A - 5M/6 - 2v/3 - (L-v)_+ = A - M at v = L = M/4
    ok = True
    for M in [Fr(k, 3) for k in range(1, 13)]:
        L = M / 4
        A = M
        vals = [(A - Fr(5, 6) * M - Fr(2, 3) * v - max(Fr(0), L - v), v) for v in [L * Fr(k, 24) for k in range(0, 73)]]
        mx = max(vals)
        ok &= mx[0] == A - M and mx[1] == L
    check("L4 (2.19) deficit maximised exactly at v = L with value A - M (zero slack)", ok)


def main():
    PR = E.primes_upto(40)   # norms 7,7,13,13,19,19,25,31,31,37,37
    PR = [q for q in PR]
    print("primes:", [(q, E.norm(q)) for q in PR[:8]])
    part_A()
    part_L()
    part_B(PR)
    p7, p7b, p13, p13b, p19, p19b, q5, p31 = PR[:8]
    cfgs = [
        ("[(1,1)@7,(2,1)@7',(7,1)@13; a=p19^2, b=p31]",
         {p7: (1, 1), p7b: (2, 1), p13: (7, 1)}, {p19: 2}, {p31: 1}),
        ("[r=1: (1,1)@7,(7,1)@13; a=p19, b=p7'^2]",
         {p7: (1, 1), p13: (7, 1)}, {p19: 1}, {p7b: 2}),
        ("[inert (3,1)@5, (2,8)@7; a=p7'^2, b=p13 p13']",
         {q5: (3, 1), p7: (2, 8)}, {p7b: 2}, {p13: 1, p13b: 1}),
        ("[(1,1)@13,(3,1)@7'; a=p19, b=p31 (R(a,b) = -1)]",
         {p13: (1, 1), p7b: (3, 1)}, {p19: 1}, {p31: 1}),
    ]
    part_D(PR, 2500.0, cfgs)
    part_E(PR)
    part_F(PR)
    nf = sum(1 for _, o in RES if not o)
    print("\n%d/%d PASS" % (len(RES) - nf, len(RES)))
    return nf


if __name__ == "__main__":
    sys.exit(main())
