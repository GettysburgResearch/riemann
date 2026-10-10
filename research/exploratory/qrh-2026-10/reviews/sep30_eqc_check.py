#!/usr/bin/env python3
"""sep30_eqc_check.py -- numerical check of eq. (C) (label eq:first-poisson-column) of the OpenAI
manuscript "The Quasi-Riemann Hypothesis", 30 Sep 2026 (pr908 import, paper.tex,
SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3).  External, unreviewed;
read as data.  RH is unsolved; nothing here bears on it.

Status: review instrument (exploration level), written for SEP30_EQC_CHECK.md.
Scope:  paper.tex lines 10145-10295 (first Poisson transformation in the proof of Lemma 17.2):
        eq:first-masked-data (10166), the u_1-side factor list (10214-10229), the fixed-ray quotient
        G(u_1u_2^{-1}) R(u_1u_2^{-1},P_T) (10234-10245), the exponent table (10255-10272), and the
        column coefficient (C) (10279).  Conventions: 573-664 (symbols, gamma_j, alpha, e(z)),
        843-1100 (Gamma, r, R, G, eq:signal, CRT), 9289-9294/7290-7313 (a(n), Psi_k, marks),
        9722-9746 (Lemma 17.5, masked primitive Poisson), 9984-9997 (block (A)).
Arithmetic: residue symbols are EXACT (integer power tables in O/p, cross-checked against the
        independent a2/eis.py).  Gauss sums, Gamma, kernels and lattice sums are double-precision
        floating point: these are EMPIRICAL checks, tolerance 1e-9 (pointwise, absolute; every
        compared quantity has modulus 0 or 1) and 1e-9 relative (replay).  Not certified.
What the checks are:
  A  conventions: symbol tables; Gamma four-term vs definition; r table and bicharacter; sextic
     reciprocity chi_b(a) = r(a,b) chi_a(b) (composite, prime powers); G = conj chi_c(4) gamma_3
     vs the mod-4 class function; eq:signal; G(vw)=G(v)G(w)R(v,w); G(v^-1)=chi_v(-1)conj G(v);
     gamma_2(ab) CRT; gamma(conj chi_u;u) = chi_u(-1) conj gamma_1(u); chi_u(f)^4 = conj chi_u(f^2).
  B  eq:first-masked-data (k-character = psi_1 times the mask C B/R_1), m_1 = 1 iff (n_1 = n_2 and
     b_1 b_2 a square), the 8-row table, eq:retained-cube-label.
  C  eq. (C) pointwise: RAW = a(n1) conj a(n2) chi_{n1}(f)^4 conj chi_{n2}(f)^4 gamma(psi_1;m_1)
     psi_1(d_k) conj psi_1(h), computed from the definitions (Gauss sum by direct summation mod m_1,
     no CRT), against CLAIM = Coef_1(u_1) conj Coef_2(u_2) G(u_1u_2^{-1}) R(u_1u_2^{-1},P_T) OUTER,
     Coef_i = (C) with nu_i := nu before Fourier expansion, OUTER independent of u_1, u_2.
     C2 checks u-independence WITHOUT the explicit OUTER (ratio constancy over many u-pairs).
     C3 checks the intermediate u_1-side list of 10220-10223 and the cross factor R(u_1,u_2).
     C4 checks the slot-priority split of the mark d(n_i b_i^3) into outer slots times d_I'(u_i).
  D  failing controls (wrong conjugation, wrong reciprocity factor, dropped mark/label), each must fail.
  E  end-to-end replay of the first Poisson transform of block (A) at tiny scale, for a fixed label f:
     LHS = sum_k Phi(k) |sum_b beta(b,f) chi_b(k)^3 sum_n a(n) chi_n(k) chi_n(f)^4 d(nb^3) W(q_n/X)|^2
     by direct lattice summation, RHS = Lemma 17.5 with every coefficient written in form (C).
     Radial Gaussian Phi (as in Lemma 17.5) and a shifted Gaussian (non-radial, so that characters
     nontrivial on units do not vanish identically).  Two failing controls must break it.
Run:  nice -n 10 python3 -I sep30_eqc_check.py [--quick] [--out PATH.json]
"""
import cmath
import itertools
import json
import math
import os
import random
import sys
import time

import numpy as np

QUICK = '--quick' in sys.argv
T0 = time.time()
SQ3 = math.sqrt(3.0)
OMEGA = cmath.exp(2j * math.pi / 3)
ZETA = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]
ZETA_ARR = np.array(ZETA + [0j])           # code 6 = zero of the zero-extended symbol
UNITS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]   # (1+w)^k = e^{i pi k/3}
LAMBDA = (1, 2)                                                 # 1 + 2w = sqrt(-3)
TOL = 1e-9
RESULTS = []
OUT = {}


def rec(part, claim, ok, detail=''):
    RESULTS.append((part, claim, bool(ok), detail))
    print(('PASS ' if ok else 'FAIL ') + f'[{part}] {claim}' + (f'  -- {detail}' if detail else ''), flush=True)


# ------------------------------------------------------------------------------------------------
# 0. Arithmetic in O = Z[w], elements (a, b) <-> a + b w
# ------------------------------------------------------------------------------------------------
def emul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def econj(x):
    return (x[0] - x[1], -x[1])


def enorm(x):
    a, b = x
    return a * a - a * b + b * b


def ecx(x):
    return complex(x[0] - x[1] / 2, x[1] * SQ3 / 2)


def eprod(xs):
    r = (1, 0)
    for x in xs:
        r = emul(r, x)
    return r


def epow(x, e):
    r = (1, 0)
    for _ in range(e):
        r = emul(r, x)
    return r


def is_primary(x):
    return x[0] % 3 == 1 and x[1] % 3 == 0


def primary(x):
    for u in UNITS:
        y = emul(u, x)
        if is_primary(y):
            return y
    raise ValueError(x)


def alpha(x):
    z = ecx(x)
    return z / abs(z)


def e_of(w):
    """e(w) = exp(4 pi i Im w / sqrt 3) for complex w (paper line 607)."""
    return cmath.exp(4j * math.pi * w.imag / SQ3)


class Prime:
    """primary prime element outside S, with an exact table of chi_p on O/p (code 6 = zero)."""

    def __init__(self, gen, name):
        self.gen, self.name, self.N = gen, name, enorm(gen)
        a, b = gen
        e = (self.N - 1) // 6
        if b == 0:                                    # inert: gen = -q, q = 2 mod 3
            self.kind, self.q = 'inert', -a
            q = self.q
            zimg = [(u0 % q, u1 % q) for u0, u1 in UNITS]
            tab = np.full(q * q, 6, dtype=np.int8)
            for c in range(q):
                for d in range(q):
                    if (c, d) == (0, 0):
                        continue
                    r, base, k = (1, 0), (c, d), e
                    while k:
                        if k & 1:
                            r = self._mq(r, base)
                        base = self._mq(base, base)
                        k >>= 1
                    tab[c * q + d] = zimg.index(r)
        else:                                         # split: gen | p = N, w -> r in F_p
            self.kind, self.p = 'split', self.N
            p = self.p
            self.r = (-a * pow(b, -1, p)) % p
            zimg = [(u0 + u1 * self.r) % p for u0, u1 in UNITS]
            tab = np.full(p, 6, dtype=np.int8)
            for x in range(1, p):
                tab[x] = zimg.index(pow(x, e, p))
        self.tab = tab

    def _mq(self, s, t):
        q = self.q
        a, b = s
        c, d = t
        return ((a * c - b * d) % q, (a * d + b * c - b * d) % q)

    def code(self, x):
        a, b = x
        if self.kind == 'split':
            return int(self.tab[(a + b * self.r) % self.p])
        q = self.q
        return int(self.tab[(a % q) * q + (b % q)])

    def codes(self, A, B):
        if self.kind == 'split':
            return self.tab[(A + B * self.r) % self.p]
        q = self.q
        return self.tab[(A % q) * q + (B % q)]

    def __repr__(self):
        return self.name


def make_primes(Nmax):
    out = []
    isp = [True] * (Nmax + 1)
    isp[0] = isp[1] = False
    for i in range(2, int(Nmax ** 0.5) + 1):
        if isp[i]:
            isp[i * i::i] = [False] * len(isp[i * i::i])
    for p in range(5, Nmax + 1):
        if not isp[p]:
            continue
        if p % 3 == 1:
            found = None
            for a in range(0, p + 1):
                for b in range(-p, p + 1):
                    if a * a - a * b + b * b == p:
                        found = (a, b)
                        break
                if found:
                    break
            g1, g2 = primary(found), primary(econj(found))
            gens = sorted({g1, g2})
            out += [Prime(gens[0], f'{p}a'), Prime(gens[1], f'{p}b')]
        elif p % 3 == 2 and p * p <= Nmax:
            out.append(Prime((-p, 0), f'{p * p}i'))
    return sorted(out, key=lambda P: (P.N, P.name))


PRIMES = make_primes(200)
PR = {P.name: P for P in PRIMES}


def chv(chars, x):
    """prod chi_P(x)^j over (P, j) in chars, zero-extended at every listed P (also for j = 0 mod 6)."""
    tot = 0
    for P, j in chars:
        k = P.code(x)
        if k == 6:
            return 0
        tot += j * k
    return ZETA[tot % 6]


def chi_n(nlist, x, power=1):
    """chi_n(x)^power for n = product of the listed primes (with repetition = valuation)."""
    return chv([(P, power) for P in nlist], x)


def gen_of(nlist):
    return eprod([P.gen for P in nlist])


def mu(nlist):
    return (-1) ** len(nlist) if len(set(nlist)) == len(nlist) else 0


def hnf(m):
    p, q = m
    a, b = [p, q], [-q, p - q]                   # m and m w in the basis (1, w)
    while b[0] != 0:
        t = a[0] // b[0]
        a = [a[0] - t * b[0], a[1] - t * b[1]]
        a, b = b, a
    if a[0] < 0:
        a = [-a[0], -a[1]]
    A, C = a[0], abs(b[1])
    assert A * C == enorm(m)
    return A, C


def residues(m):
    A, C = hnf(m)
    return np.repeat(np.arange(A, dtype=np.int64), C), np.tile(np.arange(C, dtype=np.int64), A)


def e_over_arr(I, J, m):
    """e(x/m) for x = I + J w: x conj(m) = c + d w, e(x/m) = exp(2 pi i d / N(m))."""
    s, t = econj(m)
    d = I * t + J * s - J * t
    N = enorm(m)
    return np.exp(2j * np.pi * (d % N) / N)


_GC = {}


def gauss(chars, m):
    """gamma(psi; m) = N(m)^{-1/2} sum_{x mod m} psi(x) e(x/m), psi = prod chi_P^j, by DIRECT summation."""
    key = (tuple(sorted((P.name, j % 6) for P, j in chars)), m)
    if key in _GC:
        return _GC[key]
    if enorm(m) == 1:
        _GC[key] = 1.0 + 0j
        return _GC[key]
    I, J = residues(m)
    tot = np.zeros(len(I), dtype=np.int64)
    zero = np.zeros(len(I), dtype=bool)
    for P, j in chars:
        c = P.codes(I, J)
        zero |= (c == 6)
        tot += (j % 6) * c.astype(np.int64)
    val = ZETA_ARR[np.where(zero, 6, tot % 6)]
    s = complex(np.sum(val * e_over_arr(I, J, m))) / math.sqrt(enorm(m))
    _GC[key] = s
    return s


def gam_j(nlist, j):
    """gamma_j(n) for squarefree n (paper line 642), direct summation."""
    if not nlist:
        return 1.0 + 0j
    return gauss([(P, j) for P in nlist], gen_of(nlist))


# ---- quadratic phase, r, R, G as functions of residues mod 4 (paper 843-1035) ----
def mod4(x):
    return (x[0] % 4, x[1] % 4)


UNITS4 = [c for c in itertools.product(range(4), repeat=2) if enorm(c) % 2 == 1]


def inv4(c):
    for d in UNITS4:
        if mod4(emul(c, d)) == (1, 0):
            return d
    raise ValueError(c)


def Gam(c):
    a, b = c
    return (1 + 1j ** ((-b) % 4) + 1j ** (a % 4) + 1j ** ((b - a) % 4)) / 2


def rr(x, y):
    v = Gam(mod4(emul(x, y))) / (Gam(mod4(x)) * Gam(mod4(y)))
    assert abs(v.imag) < 1e-12 and abs(abs(v) - 1) < 1e-12, (x, y, v)
    return int(round(v.real))


def chi4cls(c):
    return {(1, 0): 1, (0, 1): OMEGA, (1, 1): OMEGA ** 2}[(c[0] % 2, c[1] % 2)]


def Gcls(c):
    c = mod4(c)
    return chi4cls(c).conjugate() * Gam(c)


NUS = {'triv': lambda c: 1.0,
       'chi4': lambda c: chi4cls(c),
       'quad': lambda c: float(rr(c, LAMBDA)),
       'nu6': lambda c: chi4cls(c) * rr(c, LAMBDA)}


# ------------------------------------------------------------------------------------------------
# A. Conventions
# ------------------------------------------------------------------------------------------------
def part_A(rng):
    # A0 symbol tables vs the independent implementation a2/eis.py (sym_prime by modular powering)
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(here, '..', 'a2'))
    try:
        from eis import sym_prime
        bad = n = 0
        for P in PRIMES[:24]:
            for _ in range(150):
                u = (rng.randint(-400, 400), rng.randint(-400, 400))
                k = sym_prime(u, P.gen)
                bad += ((6 if k is None else k) != P.code(u))
                n += 1
        rec('A0', f'symbol tables agree with a2/eis.sym_prime on {n} random (p,u)', bad == 0, f'{bad} mismatches')
    except ImportError:
        rec('A0', 'a2/eis.py not importable; table cross-check skipped', True, 'SKIPPED')
    finally:
        sys.path.pop(0)
    # every P is primary and chi_P(P-multiple) = 0, values are units
    rec('A0', f'{len(PRIMES)} primary primes outside S with norms <= 200 (incl. inert 25, 121)',
        all(is_primary(P.gen) for P in PRIMES) and all(P.code(emul(P.gen, (3, 1))) == 6 for P in PRIMES))

    # A1 Gamma four-term formula vs the definition |c|^{-1} sum_{x mod c} e(x^2/c), odd c (any)
    worst, cnt = 0.0, 0
    for a in range(-9, 10):
        for b in range(-9, 10):
            c = (a, b)
            if enorm(c) % 2 == 0 or enorm(c) > 300:
                continue
            I, J = residues(c)
            X2a, X2b = I * I - J * J, 2 * I * J - J * J
            direct = complex(np.sum(e_over_arr(X2a, X2b, c))) / math.sqrt(enorm(c))
            worst = max(worst, abs(direct - Gam(mod4(c))))
            cnt += 1
    rec('A1', f'Gamma(c) four-term formula = definition on {cnt} odd c (non-primary, non-squarefree incl.)',
        worst < TOL, f'max err {worst:.1e}')

    # A2 r table and bicharacter
    ok = True
    for e, f, g, h in itertools.product(range(2), repeat=4):
        x = emul(epow((-1, 0), e), epow(LAMBDA, f))
        y = emul(epow((-1, 0), g), epow(LAMBDA, h))
        ok &= rr(x, y) == (-1) ** (e * h + f * g + f * h)
    for x, y, z in itertools.product(UNITS4, repeat=3):
        ok &= rr(x, y) == rr(y, x) and rr(emul(x, y), z) == rr(x, z) * rr(y, z)
    for x, y, s in itertools.product(UNITS4, UNITS4, UNITS4):
        ok &= rr(emul(x, emul(s, s)), y) == rr(x, y)
    rec('A2', 'r((-1)^e l^f,(-1)^g l^h) = (-1)^{eh+fg+fh}; r symmetric bicharacter of square classes mod 4', ok)

    # A3 sextic reciprocity on coprime primary pairs, composite and prime powers
    pool = PRIMES[:20]
    worst, cnt = 0, 0
    for _ in range(3000):
        A = [rng.choice(pool) for _ in range(rng.randint(1, 3))]
        B = [rng.choice([P for P in pool if P not in A]) for _ in range(rng.randint(1, 3))]
        a, b = gen_of(A), gen_of(B)
        lhs = chi_n(B, a)
        rhs = rr(a, b) * chi_n(A, b)
        worst = max(worst, abs(lhs - rhs))
        cnt += 1
    rec('A3', f'chi_b(a) = r(a,b) chi_a(b) on {cnt} coprime primary pairs (composite, prime powers)',
        worst < TOL, f'max err {worst:.1e}')

    # A4 G and eq:signal on squarefree c; chi_c(4) on primary c incl prime powers
    sq = []
    for P in PRIMES[:16]:
        sq.append([P])
    for P, Q in itertools.combinations(PRIMES[:12], 2):
        if P.N * Q.N <= 2000:
            sq.append([P, Q])
    for P, Q, R in itertools.combinations(PRIMES[:8], 3):
        if P.N * Q.N * R.N <= 6000:
            sq.append([P, Q, R])
    wG = wS1 = wS2 = w4 = 0.0
    for c in sq:
        cg = gen_of(c)
        Gd = chi_n(c, (4, 0)).conjugate() * gam_j(c, 3)
        wG = max(wG, abs(Gd - Gcls(cg)))
        wS1 = max(wS1, abs(gam_j(c, 2) ** 3 - mu(c) * alpha(cg)))
        wS2 = max(wS2, abs(gam_j(c, 1) * gam_j(c, 2) - mu(c) * alpha(cg) * Gd))
    for _ in range(500):
        c = [rng.choice(PRIMES[:20]) for _ in range(rng.randint(1, 4))]
        w4 = max(w4, abs(chi_n(c, (4, 0)) - chi4cls(gen_of(c))))
    rec('A4', f'G(c) = conj chi_c(4) gamma_3(c) equals the mod-4 class function on {len(sq)} squarefree c',
        wG < TOL, f'{wG:.1e}')
    rec('A4', 'eq:signal gamma_2^3 = mu alpha and gamma_1 gamma_2 = mu alpha G (direct Gauss sums)',
        max(wS1, wS2) < TOL, f'{wS1:.1e}, {wS2:.1e}')
    rec('A4', 'chi_c(4) = cube root of unity == c mod 2 (500 primary c incl. prime powers)', w4 < TOL, f'{w4:.1e}')

    # A5 G(vw) = G(v)G(w)R(v,w) on the class group; G(v^-1) = R(v,v) conj G(v); chi_v(-1) = R(v,v)
    wq = 0.0
    for v, w in itertools.product(UNITS4, repeat=2):
        wq = max(wq, abs(Gcls(emul(v, w)) - Gcls(v) * Gcls(w) * rr(v, w)))
    wi = max(abs(Gcls(inv4(v)) - rr(v, v) * Gcls(v).conjugate()) for v in UNITS4)
    wm = 0.0
    for _ in range(500):
        c = [rng.choice(PRIMES[:20]) for _ in range(rng.randint(1, 4))]
        wm = max(wm, abs(chi_n(c, (-1, 0)) - rr(gen_of(c), gen_of(c))))
    rec('A5', 'G(vw)=G(v)G(w)R(v,w) (eq:G-quadratic-refinement), G(v^-1)=R(v,v)conj G(v), chi_v(-1)=R(v,v)',
        max(wq, wi, wm) < TOL, f'{wq:.1e}, {wi:.1e}, {wm:.1e}')

    # A6 gamma_2(ab) = gamma_2(a) gamma_2(b) chi_b(a)^4 = ... chi_a(b)^2 chi_b(a)^2 (10214-10218)
    w6 = 0.0
    cnt = 0
    for A in sq:
        for B in sq:
            if set(A) & set(B) or enorm(gen_of(A + B)) > 40000:
                continue
            a, b = gen_of(A), gen_of(B)
            lhs = gam_j(A + B, 2)
            r1 = gam_j(A, 2) * gam_j(B, 2) * chi_n(B, a, 4)
            r2 = gam_j(A, 2) * gam_j(B, 2) * chi_n(A, b, 2) * chi_n(B, a, 2)
            w6 = max(w6, abs(lhs - r1), abs(lhs - r2))
            cnt += 1
            if cnt >= (60 if QUICK else 250):
                break
        if cnt >= (60 if QUICK else 250):
            break
    rec('A6', f'gamma_2(ab) = gamma_2(a)gamma_2(b)chi_b(a)^4 = ..chi_a(b)^2chi_b(a)^2 on {cnt} coprime pairs',
        w6 < TOL, f'{w6:.1e}')

    # A7 gamma(conj chi_u; u) = chi_u(-1) conj gamma_1(u); raw second Gauss-signal factor (10237-10241)
    w7 = w7b = 0.0
    for c in sq:
        cg = gen_of(c)
        gm = gauss([(P, -1) for P in c], cg)
        w7 = max(w7, abs(gm - chi_n(c, (-1, 0)) * gam_j(c, 1).conjugate()))
        raw2 = alpha(cg) * gam_j(c, 2).conjugate() * gm
        w7b = max(w7b, abs(raw2 - mu(c) * chi_n(c, (-1, 0)) * Gcls(cg).conjugate()))
    rec('A7', 'gamma(conj chi_u;u) = chi_u(-1) conj gamma_1(u); alpha conj(gamma_2) gamma(conj chi_u) = mu chi_u(-1) conj G',
        max(w7, w7b) < TOL, f'{w7:.1e}, {w7b:.1e}')

    # A8 chi_u(f)^4 = conj chi_u(f^2) including zeros (10248)
    w8 = 0.0
    for _ in range(2000):
        u = [rng.choice(PRIMES[:20]) for _ in range(rng.randint(1, 3))]
        f = (rng.randint(-60, 60), rng.randint(-60, 60))
        if rng.random() < 0.2:
            f = emul(f, rng.choice(u).gen)
        w8 = max(w8, abs(chi_n(u, f, 4) - chi_n(u, emul(f, f)).conjugate()))
    rec('A8', 'chi_u(f)^4 = conj chi_u(f^2) incl. zeros (2000 random u, f)', w8 < TOL, f'{w8:.1e}')

    # A9 the twists used for nu are characters of (O/4)^x
    ok = all(abs(nu(mod4(emul(x, y))) - nu(x) * nu(y)) < TOL for nu in NUS.values()
             for x, y in itertools.product(UNITS4, repeat=2))
    rec('A9', 'test twists nu in {triv, chi4 (order 3), r(.,lambda) (order 2), nu6} are characters mod 4', ok)


# ------------------------------------------------------------------------------------------------
# Decomposition of a raw column pair (paper 10146-10180) and the two sides of eq. (C)
# ------------------------------------------------------------------------------------------------
TEX_TABLE = {(0, 0, 0): (0, 0), (0, 1, 0): (1, 0), (0, 0, 1): (5, 0), (0, 1, 1): (0, 4),
             (1, 0, 0): (3, 4), (1, 1, 0): (4, 4), (1, 0, 1): (2, 4), (1, 1, 1): (3, 4)}   # (pi,a1,a2) -> (t, exp)


def decompose(n1, n2, b1, b2):
    """n_i: squarefree lists of Primes; b_i: dict Prime -> valuation (>0).  Returns the paper's data."""
    Bset = sorted(set(b1) | set(b2), key=lambda P: P.name)
    A1 = [P for P in n1 if P in Bset]
    A2 = [P for P in n2 if P in Bset]
    r1 = [P for P in n1 if P not in Bset]
    r2 = [P for P in n2 if P not in Bset]
    C = [P for P in r1 if P in r2]
    U1 = [P for P in r1 if P not in C]
    U2 = [P for P in r2 if P not in C]
    rows, t = {}, {}
    for P in Bset:
        pi = (b1.get(P, 0) + b2.get(P, 0)) % 2
        a1, a2 = int(P in A1), int(P in A2)
        rows[P] = (pi, a1, a2)
        t[P] = (a1 - a2 + 3 * pi) % 6
    R1 = [P for P in Bset if t[P] != 0]
    Rmask = C + [P for P in Bset if t[P] == 0]
    PT = eprod([epow(P.gen, t[P]) for P in R1])
    E = eprod([epow(P.gen, rows[P][1] + rows[P][2]) for P in Bset if rows[P][0] == 1])
    xi_exp = {P: TEX_TABLE[rows[P]][1] for P in Bset}
    return dict(B=Bset, A1=A1, A2=A2, C=C, U1=U1, U2=U2, rows=rows, t=t, R1=R1, Rmask=Rmask, PT=PT, E=E,
                xi_exp=xi_exp, m1=gen_of(U1 + U2 + R1),
                psi1=[(P, 1) for P in U1] + [(P, -1) for P in U2] + [(P, t[P]) for P in R1],
                psiR=[(P, t[P]) for P in R1])


def a_coef(n, nu, rho):
    """a(n) = conj alpha(n) gamma_2(n) nu(n) rho(n) (paper 7293)."""
    if any(P.name in rho for P in n):
        return 0j
    g = gen_of(n)
    return alpha(g).conjugate() * gam_j(n, 2) * nu(mod4(g))


def raw_value(n1, n2, b1, b2, f, h, dk, nu, rho, dec):
    """the u-dependent product produced by expanding the square and applying Lemma 17.5 (no CRT used)."""
    fa = gen_of(f)
    a1 = a_coef(n1, nu, rho) * chi_n(n1, fa, 4)
    a2 = a_coef(n2, nu, rho) * chi_n(n2, fa, 4)
    if a1 == 0 or a2 == 0:
        return 0j
    g = gauss(dec['psi1'], dec['m1'])
    return a1 * a2.conjugate() * g * chv(dec['psi1'], gen_of(dk)) * chv(dec['psi1'], h).conjugate()


def xi_val(u, dec, sidesign=None, table=None, orient=False):
    """xi(u) = prod_{p | B} chi_u(p)^{exp_p} (exponent 0 = puncture).  Variants used only by controls."""
    v = 1.0 + 0j
    for P in dec['B']:
        e = dec['xi_exp'][P] if table is None else table[P]
        if orient:
            v *= chv([(P, e)], gen_of(u)) if u else 1.0
        else:
            v *= chv([(Q, e) for Q in u], P.gen)
    return v


def claim_value(dec, f, h, dk, nu, rho, variant='', upart_only=False):
    """CLAIM = Coef_1(u1) conj Coef_2(u2) * G(u1 u2^-1) R(u1 u2^-1, P_T) * OUTER, Coef_i from eq. (C).
    upart_only: return Coef_1 conj Coef_2 G R without OUTER (used by the u-independence check C2)."""
    U1, U2, C = dec['U1'], dec['U2'], dec['C']
    fa, d = gen_of(f), gen_of(dk)
    E = (1, 0) if variant == 'drop_E' else dec['E']
    f2 = (1, 0) if variant == 'drop_f2' else emul(fa, fa)
    htil = emul(emul(h, f2), E)

    def coef(u, side):
        if any(P.name in rho for P in u):
            return 0j
        ug = gen_of(u)
        val = (1 if variant == 'drop_mu' else mu(u)) * nu(mod4(ug))
        ch = chi_n(u, htil)
        val *= ch if variant == 'conj_h' else ch.conjugate()
        if variant != 'drop_C4':
            val *= chi_n(u, gen_of(C), 4)
        if variant != 'drop_dk':
            val *= chi_n(u, d)
        if variant == 'drop_xi':
            pass
        elif variant == 'xi_orient':
            val *= xi_val(u, dec, orient=True)
        elif variant == 'side2_plus' and side == 2:
            tab = {}
            for P in dec['B']:
                pi, a1, a2 = dec['rows'][P]
                tt = dec['t'][P]
                tab[P] = (4 * a2 + (1 + tt if tt else 0) + pi * (a1 + a2)) % 6
            val *= xi_val(u, dec, table=tab)
        elif variant == 'xi_2pi':
            tab = {}
            for P in dec['B']:
                pi, a1, a2 = dec['rows'][P]
                tt = (a1 - a2 + 2 * pi) % 6
                s = 1 if side == 1 else -1
                ai = a1 if side == 1 else a2
                tab[P] = (4 * ai + ((1 + s * tt) if tt else 0) + pi * (a1 + a2)) % 6
            val *= xi_val(u, dec, table=tab)
        else:
            val *= xi_val(u, dec)
        return val

    c1, c2 = coef(U1, 1), coef(U2, 2)
    if c1 == 0 or c2 == 0:
        return 0j
    u1g, u2g = gen_of(U1), gen_of(U2)
    q = mod4(emul(u1g, inv4(mod4(u2g))))           # ray class of u1 u2^{-1}
    if variant == 'G_swap':
        Gf = Gcls(inv4(q))
    elif variant == 'G_split':
        Gf = Gcls(u1g) * Gcls(u2g).conjugate()
    elif variant == 'drop_R12':
        Gf = Gcls(u1g) * chi_n(U2, (-1, 0)) * Gcls(u2g).conjugate()
    elif variant == 'drop_chim1':
        Gf = Gcls(u1g) * Gcls(u2g).conjugate() * rr(u1g, u2g)
    else:
        Gf = Gcls(q)
    Rf = 1 if variant == 'drop_RPT' else rr(q, dec['PT'])
    if upart_only:
        return c1 * c2.conjugate() * Gf * Rf
    # OUTER: everything not involving u1, u2 (explicit form derived in SEP30_EQC_CHECK.md section 3)
    O1, O2 = dec['A1'] + C, dec['A2'] + C
    outer = (a_coef(O1, nu, rho) * chi_n(O1, fa, 4)) * (a_coef(O2, nu, rho) * chi_n(O2, fa, 4)).conjugate()
    outer *= gauss(dec['psiR'], gen_of(dec['R1'])) * chv(dec['psiR'], d) * chv(dec['psiR'], h).conjugate()
    return c1 * c2.conjugate() * Gf * Rf * outer


# ------------------------------------------------------------------------------------------------
# Random admissible tuples with forced coverage
# ------------------------------------------------------------------------------------------------
ROWS8 = list(TEX_TABLE.keys())


def random_tuple(rng, k, mmax=150000, nmax=30000):
    """builds (n1, n2, b1, b2, f, h, d_k, nu, rho) from components, cycling through the 8 table rows."""
    smallB = PRIMES[:9]                                   # norms 7..37 incl. inert 25
    pool = PRIMES[:26]
    while True:
        nb = [1, 1, 2, 2, 3, 0][k % 6] if k % 11 else 1
        Bp = rng.sample(smallB, nb)
        b1, b2, a1s, a2s = {}, {}, [], []
        for j, P in enumerate(Bp):
            pi, a1, a2 = ROWS8[(k + 3 * j) % 8]
            vv = [(v1, v2) for v1 in range(4) for v2 in range(4) if v1 + v2 >= 1 and (v1 + v2) % 2 == pi]
            v1, v2 = rng.choice(vv)
            if v1:
                b1[P] = v1
            if v2:
                b2[P] = v2
            if a1:
                a1s.append(P)
            if a2:
                a2s.append(P)
        rest = [P for P in pool if P not in Bp]
        rng.shuffle(rest)
        nC, nu1, nu2 = rng.choice([0, 0, 1, 1, 2]), rng.choice([0, 1, 1, 2, 2]), rng.choice([0, 1, 1, 2, 2])
        C, U1, U2 = rest[:nC], rest[nC:nC + nu1], rest[nC + nu1:nC + nu1 + nu2]
        n1, n2 = a1s + C + U1, a2s + C + U2
        dec = decompose(n1, n2, b1, b2)
        if enorm(dec['m1']) > mmax or enorm(gen_of(n1)) > nmax or enorm(gen_of(n2)) > nmax:
            continue
        assert sorted(dec['U1'], key=str) == sorted(U1, key=str) and sorted(dec['C'], key=str) == sorted(C, key=str)
        # label f: may meet u_i, C, A_i or b (zeros are part of the identity)
        f = rng.sample(pool, rng.choice([0, 1, 1, 2]))
        # frequency h: random element; sometimes forced to meet u_1 u_2 R_1, sometimes 0
        h = (rng.randint(-45, 45), rng.randint(-45, 45))
        x = rng.random()
        if x < 0.12 and (dec['U1'] + dec['U2'] + dec['R1']):
            h = emul(h, rng.choice(dec['U1'] + dec['U2'] + dec['R1']).gen)
        elif x < 0.15:
            h = (0, 0)
        elif x < 0.25:
            h = rng.choice(UNITS)
        dk = [P for P in dec['Rmask'] if rng.random() < 0.5]
        nu = rng.choice(list(NUS))
        rho = set()
        if rng.random() < 0.15:
            rho = {rng.choice(pool).name}
        return n1, n2, b1, b2, f, h, dk, nu, rho, dec


def describe(t):
    n1, n2, b1, b2, f, h, dk, nu, rho, dec = t
    return {'n1': [P.name for P in n1], 'n2': [P.name for P in n2],
            'b1': {P.name: v for P, v in b1.items()}, 'b2': {P.name: v for P, v in b2.items()},
            'f': [P.name for P in f], 'h': list(h), 'd_k': [P.name for P in dk], 'nu': nu, 'rho': sorted(rho),
            'u1': [P.name for P in dec['U1']], 'u2': [P.name for P in dec['U2']], 'C': [P.name for P in dec['C']],
            'rows': {P.name: dec['rows'][P] for P in dec['B']}, 'N(m1)': enorm(dec['m1'])}


# ------------------------------------------------------------------------------------------------
# B. masked data, m_1 = 1 case, table, retained cube label
# ------------------------------------------------------------------------------------------------
def part_B(rng, tuples):
    # B1 the table (10255-10272) from the formula 4a_i + 1_{t!=0}(1 +- t) + pi(a1+a2)
    ok = True
    for (pi, a1, a2), (tt, ex) in TEX_TABLE.items():
        t = (a1 - a2 + 3 * pi) % 6
        s1 = (4 * a1 + ((1 + t) if t else 0) + pi * (a1 + a2)) % 6
        s2 = (4 * a2 + ((1 - t) if t else 0) + pi * (a1 + a2)) % 6
        ok &= (t == tt and s1 == ex and s2 == ex)
    rec('B1', 'the 8-row table: t_p and the common exponent on both sides', ok)

    # B2 eq:first-masked-data
    worst, cnt, nz = 0.0, 0, 0
    for (n1, n2, b1, b2, f, h, dk, nu, rho, dec) in tuples[: (40 if QUICK else 200)]:
        mask = dec['Rmask']
        for _ in range(60):
            k = (rng.randint(-300, 300), rng.randint(-300, 300))
            if rng.random() < 0.3:
                k = emul(k, rng.choice(n1 + n2 + list(b1) + list(b2) or [PRIMES[0]]).gen)
            kc = chi_n(n1, k) * chi_n(n2, k).conjugate()
            for P, v in b1.items():
                kc *= chv([(P, 3 * v)], k)
            for P, v in b2.items():
                kc *= chv([(P, 3 * v)], k).conjugate()
            rhs = chv(dec['psi1'], k) * (0 if any(P.code(k) == 6 for P in mask) else 1)
            worst = max(worst, abs(kc - rhs))
            cnt += 1
            nz += abs(kc) > 0.5
    rec('B2', f'eq:first-masked-data: k-character = psi_1(k) 1_(k, CB/R_1)=1 on {cnt} (tuple,k) ({nz} nonzero)',
        worst < TOL, f'{worst:.1e}')

    # B3 m_1 = 1 iff n1 = n2 and b1 b2 a square (10194-10197)
    Bs = [dict(), {PR['7a']: 1}, {PR['7a']: 2}, {PR['7a']: 3}, {PR['7b']: 1}, {PR['7a']: 1, PR['7b']: 1},
          {PR['13a']: 2}, {PR['7a']: 1, PR['13a']: 1}]
    ns = [[], [PR['7a']], [PR['7b']], [PR['13a']], [PR['7a'], PR['13a']], [PR['19a']], [PR['7a'], PR['19a']],
          [PR['25i']], [PR['13a'], PR['19a']]]
    ok, cnt = True, 0
    for b1, b2, n1, n2 in itertools.product(Bs, Bs, ns, ns):
        dec = decompose(n1, n2, b1, b2)
        m1one = enorm(dec['m1']) == 1
        allv = {P: b1.get(P, 0) + b2.get(P, 0) for P in set(b1) | set(b2)}
        sq = all(v % 2 == 0 for v in allv.values())
        ok &= (m1one == (set(n1) == set(n2) and sq))
        cnt += 1
    rec('B3', f'm_1 = 1 iff n_1 = n_2 and b_1 b_2 is a square ({cnt} combinations)', ok)

    # B4 eq:retained-cube-label xi(n) = chi_n(J)^4 1_(n, rad q0)=1 for every squarefree n (incl. meeting B)
    worst, cnt = 0.0, 0
    for (n1, n2, b1, b2, f, h, dk, nu, rho, dec) in tuples[: (60 if QUICK else 300)]:
        val = {P: b1.get(P, 0) + b2.get(P, 0) for P in dec['B']}
        s = [P for P in dec['B'] if val[P] % 2 == 1]
        qv = {P: val[P] // 2 for P in dec['B']}
        J2 = [P for P in dec['B'] if dec['rows'][P] == (0, 1, 1)]
        q0v = {P: qv[P] - (1 if P in J2 else 0) for P in dec['B']}
        assert all(v >= 0 for v in q0v.values())
        J, q0rad = s + J2, [P for P in dec['B'] if q0v[P] > 0]
        for _ in range(25):
            n = rng.sample(PRIMES[:26], rng.randint(1, 3))
            lhs = 1.0 + 0j
            for P in dec['B']:
                lhs *= chv([(Q, dec['xi_exp'][P]) for Q in n], P.gen)
            rhs = chi_n(n, gen_of(J), 4) * (0 if set(n) & set(q0rad) else 1)
            worst = max(worst, abs(lhs - rhs))
            cnt += 1
    rec('B4', f'eq:retained-cube-label xi(n) = chi_n(J)^4 1_(n,rad q0)=1 on {cnt} (tuple, n)', worst < TOL, f'{worst:.1e}')


# ------------------------------------------------------------------------------------------------
# C. eq. (C) pointwise, u-independence, intermediate factor list, mark split
# ------------------------------------------------------------------------------------------------
def part_C(rng, tuples):
    worst, nz, zz, mism0 = 0.0, 0, 0, 0
    cov = {'rows': set(), 'composite_u': 0, 'prime_power_b': 0, 'inert': 0, 'C_nontriv': 0, 'dk_nontriv': 0,
           'R1_nontriv': 0, 'm1_one': 0, 'f_meets_u': 0, 'nu': set(), 'rho': 0}
    keep = []
    for t in tuples:
        n1, n2, b1, b2, f, h, dk, nu, rho, dec = t
        raw = raw_value(n1, n2, b1, b2, f, h, dk, NUS[nu], rho, dec)
        cl = claim_value(dec, f, h, dk, NUS[nu], rho)
        err = abs(raw - cl)
        worst = max(worst, err)
        if abs(raw) > 0.5:
            nz += 1
            keep.append((t, raw))
            cov['rows'] |= {dec['rows'][P] for P in dec['B']}
            cov['composite_u'] += len(dec['U1']) >= 2 or len(dec['U2']) >= 2
            cov['prime_power_b'] += any(v >= 2 for v in list(b1.values()) + list(b2.values()))
            cov['inert'] += any(P.kind == 'inert' for P in n1 + n2 + list(b1) + list(b2))
            cov['C_nontriv'] += bool(dec['C'])
            cov['dk_nontriv'] += bool(dk)
            cov['R1_nontriv'] += bool(dec['R1'])
            cov['m1_one'] += enorm(dec['m1']) == 1
            cov['nu'].add(nu)
            cov['rho'] += bool(rho)
        else:
            zz += 1
            mism0 += abs(cl) > 0.5
            cov['f_meets_u'] += bool(set(f) & set(dec['U1'] + dec['U2']))
        if abs(abs(raw) - 1) > 1e-9 and abs(raw) > 1e-9:
            worst = max(worst, 1.0)                       # all compared quantities have modulus 0 or 1
    cov['rows'] = sorted(cov['rows'])
    cov['nu'] = sorted(cov['nu'])
    OUT['C1_coverage'] = cov
    rec('C1', f'eq. (C) with explicit OUTER: RAW = CLAIM on {len(tuples)} tuples ({nz} nonzero, {zz} zero on both sides)',
        worst < TOL and mism0 == 0 and len(cov['rows']) == 8, f'max err {worst:.1e}; coverage {cov}')

    # C2 u-independence without the explicit OUTER: ratio RAW/(Coef1 conj Coef2 G R) constant in (u1,u2)
    fams = 0
    worst2, pairs = 0.0, 0
    for k in range(4 if QUICK else 12):
        # outer data from a fresh tuple, then all (u1,u2) from a disjoint pool
        t = random_tuple(rng, 7 * k + 1, mmax=60000)
        n1, n2, b1, b2, f, h, dk, nu, rho, dec = t
        taken = set(dec['B']) | set(dec['C']) | set(f)
        upool = [P for P in PRIMES[:30] if P not in taken][:9]
        cands = [[]] + [[P] for P in upool] + [list(c) for c in itertools.combinations(upool, 2)
                                               if c[0].N * c[1].N <= 1200]
        h2 = h
        while any(P.code(h2) == 6 for P in PRIMES[:30]):
            h2 = (rng.randint(-45, 45), rng.randint(-45, 45))
        ratio0 = None
        for U1 in cands:
            for U2 in cands:
                if set(U1) & set(U2):
                    continue
                m1 = dec['A1'] + dec['C'] + U1
                m2 = dec['A2'] + dec['C'] + U2
                d2 = decompose(m1, m2, b1, b2)
                if enorm(d2['m1']) > 150000:
                    continue
                raw = raw_value(m1, m2, b1, b2, f, h2, dk, NUS[nu], set(), d2)
                if abs(raw) < 0.5:
                    continue
                # u-part of the claim only: Coef_1 conj Coef_2 G(u1u2^-1) R(u1u2^-1,P_T), no OUTER used
                upart = claim_value(d2, f, h2, dk, NUS[nu], set(), upart_only=True)
                ratio = raw / upart
                if ratio0 is None:
                    ratio0 = ratio
                worst2 = max(worst2, abs(ratio - ratio0))
                pairs += 1
        fams += 1
    rec('C2', f'u-independence: RAW / (Coef_1 conj Coef_2 G R) is the same for all {pairs} (u1,u2) pairs in {fams} outer families',
        worst2 < TOL, f'max spread {worst2:.1e}')

    # C3 intermediate: Poisson root = U1part * U2part * R(u1,u2) * Rpart (10220-10231), and a(n) split
    worst3 = worst3b = 0.0
    cnt = 0
    for t, raw in keep[: (80 if QUICK else 400)]:
        n1, n2, b1, b2, f, h, dk, nu, rho, dec = t
        U1, U2, R1 = dec['U1'], dec['U2'], dec['R1']
        u1, u2, d, R1g, PT = gen_of(U1), gen_of(U2), gen_of(dk), gen_of(R1), dec['PT']
        root = gauss(dec['psi1'], dec['m1']) * chv(dec['psi1'], d) * chv(dec['psi1'], h).conjugate()
        p1 = gam_j(U1, 1) * chi_n(U1, h).conjugate() * chi_n(U1, emul(d, R1g)) * chi_n(U1, PT) * rr(u1, PT)
        p2 = (gauss([(P, -1) for P in U2], u2) if U2 else 1) * chi_n(U2, h) * \
            chi_n(U2, emul(d, R1g)).conjugate() * chi_n(U2, PT) * rr(u2, PT)
        pR = gauss(dec['psiR'], R1g) * chv(dec['psiR'], d) * chv(dec['psiR'], h).conjugate()
        worst3 = max(worst3, abs(root - p1 * p2 * rr(u1, u2) * pR))
        for n, A, U in ((n1, dec['A1'], U1), (n2, dec['A2'], U2)):
            nuF = NUS[nu]
            lhs = a_coef(n, nuF, set())
            ug = gen_of(U)
            rhs = a_coef(A + dec['C'], nuF, set()) * alpha(ug).conjugate() * gam_j(U, 2) * nuF(mod4(ug)) * \
                chi_n(U, gen_of(A + dec['C']), 4)
            worst3b = max(worst3b, abs(lhs - rhs))
        cnt += 1
    rec('C3', f'u_1-side list gamma_1(u1) conj chi_u1(h) chi_u1(d_k R_1) chi_u1(P_T) x R(u1,P_T), u_2 side with -t_p, '
              f'cross factor R(u1,u2) ({cnt} nonzero tuples)', worst3 < TOL, f'{worst3:.1e}')
    rec('C3', f'a(A C u) = a(A C) conj alpha(u) gamma_2(u) nu(u) chi_u(A C)^4 ({2 * cnt} sides)', worst3b < TOL, f'{worst3b:.1e}')

    # C4 slot priority: d(n_i b_i^3) = sum_{I'} prod_{slots not in I'} (outer slot) * d_I'(u_i), original coefficients
    lists = [{PR['7a']: 0.6 + 0.3j, PR['13a']: -0.8 + 0.1j, PR['31b']: 0.25j},
             {PR['19a']: 1.1, PR['37a']: 0.4 - 0.7j},
             {PR['7b']: -0.5 + 0.5j, PR['43a']: 0.9}]

    def mark(primes_set, Ls):
        v = 1.0 + 0j
        for L in Ls:
            v *= sum(c for P, c in L.items() if P in primes_set)
        return v
    worst4, cnt = 0.0, 0
    for t in tuples[: (100 if QUICK else 600)]:
        n1, n2, b1, b2, f, h, dk, nu, rho, dec = t
        for n, b, A, U in ((n1, b1, dec['A1'], dec['U1']), (n2, b2, dec['A2'], dec['U2'])):
            whole = mark(set(n) | set(b), lists)
            outer_set = set(b) | set(A) | set(dec['C'])
            split = 0j
            for Ip in itertools.product((0, 1), repeat=len(lists)):
                term = 1.0 + 0j
                for L, inu in zip(lists, Ip):
                    if inu:
                        term *= sum(c for P, c in L.items() if P in set(U))        # original coefficients on u
                    else:
                        term *= sum(c for P, c in L.items() if P in outer_set)
                split += term
            worst4 = max(worst4, abs(whole - split))
            cnt += 1
    rec('C4', f'mark split d(n b^3) = sum_I\' outer slots x d_I\'(u) with original coefficients ({cnt} sides)',
        worst4 < 1e-12, f'{worst4:.1e}')

    # C5 fixed-ray Fourier step (10242-10245): for each class of P_T, F(x,y) = G(xy^-1) R(xy^-1,P_T) on T x T,
    # T = primary classes = (O/4)^x (order 12), is a combination of theta_1(x) conj theta_2(y) with
    # sum |c| <= |T x T|^{1/2} = 12.  Characters: chi4^a * r(., y), a in Z/3, y in the 4 square classes.
    chars = []
    for a in range(3):
        for y in [(1, 0), (-1, 0), LAMBDA, (-1, -2)]:
            chars.append({x: (chi4cls(x) ** a) * rr(x, y) for x in UNITS4})
    distinct = len({tuple(round(c[x].real, 9) + 1j * round(c[x].imag, 9) for x in UNITS4) for c in chars}) == 12
    mult = all(abs(c[mod4(emul(x, y))] - c[x] * c[y]) < TOL for c in chars for x in UNITS4 for y in UNITS4)
    worst5, l1max = 0.0, 0.0
    for PT in [(1, 0), (-1, 0), LAMBDA, (-1, -2)]:
        F = {(x, y): Gcls(emul(x, inv4(y))) * rr(emul(x, inv4(y)), PT) for x in UNITS4 for y in UNITS4}
        coef = {}
        for i, c1 in enumerate(chars):
            for j, c2 in enumerate(chars):
                coef[(i, j)] = sum(F[(x, y)] * c1[x].conjugate() * c2[y] for x in UNITS4 for y in UNITS4) / 144
        l1max = max(l1max, sum(abs(v) for v in coef.values()))
        for x in UNITS4:
            for y in UNITS4:
                rec_v = sum(v * chars[i][x] * chars[j][y].conjugate() for (i, j), v in coef.items())
                worst5 = max(worst5, abs(rec_v - F[(x, y)]))
    rec('C5', '12 distinct ray characters chi4^a r(.,y) of (O/4)^x; G(u1u2^-1)R(u1u2^-1,P_T) = sum c theta1(u1) conj theta2(u2) '
              'for each class of P_T, sum|c| <= 12', distinct and mult and worst5 < TOL and l1max <= 12 + 1e-9,
        f'reconstruction err {worst5:.1e}, max sum|c| = {l1max:.4f}')
    return keep


# ------------------------------------------------------------------------------------------------
# D. failing controls
# ------------------------------------------------------------------------------------------------
CONTROLS = {
    'conj_h': 'wrong conjugation: chi_u(h~) instead of conj chi_u(h~)',
    'G_swap': 'wrong conjugation: G(u2 u1^-1) instead of G(u1 u2^-1)',
    'drop_RPT': 'wrong reciprocity: R(u1u2^-1, P_T) dropped',
    'drop_R12': 'wrong reciprocity: cross factor R(u1,u2) dropped',
    'drop_chim1': 'G(u2^-1) replaced by conj G(u2) (chi_u2(-1) dropped)',
    'G_split': 'G(u1)conj G(u2) instead of G(u1u2^-1) (both R(u1,u2) and chi_u2(-1) dropped)',
    'side2_plus': 'conjugated side keeps +t_p (t_p -> -t_p not applied)',
    'xi_2pi': 'table built with t = a1 - a2 + 2 pi (3 pi -> 2 pi)',
    'drop_E': 'dropped label: E removed from h~ = h f^2 E',
    'drop_f2': 'dropped label: f^2 removed from h~',
    'drop_C4': 'dropped mark: chi_u(C)^4 removed',
    'drop_dk': 'dropped mark: chi_u(d_k) removed',
    'drop_xi': 'dropped mark: xi removed',
    'drop_mu': 'mu(u) removed',
}
EXPECTED_INSENSITIVE = {'xi_orient': 'xi(u) as prod chi_p(u)^e (orientation swapped); exponents e in {0,4} are even, '
                                     'so R(u,p)^e = 1 and this is NOT expected to fail'}


def part_D(keep):
    res = {}
    for var, desc in list(CONTROLS.items()) + list(EXPECTED_INSENSITIVE.items()):
        fails, best = 0, None
        for t, raw in keep:
            n1, n2, b1, b2, f, h, dk, nu, rho, dec = t
            cl = claim_value(dec, f, h, dk, NUS[nu], rho, variant=var)
            if abs(raw - cl) > 1e-6:
                fails += 1
                size = enorm(dec['m1']) * enorm(gen_of(n1)) * enorm(gen_of(n2))
                if best is None or size < best[0]:
                    best = (size, describe(t), raw, cl)
        res[var] = {'description': desc, 'fails': fails, 'of': len(keep),
                    'minimal_counterexample': None if best is None else
                    {'tuple': best[1], 'RAW': [best[2].real, best[2].imag], 'mutated': [best[3].real, best[3].imag]}}
        if var in EXPECTED_INSENSITIVE:
            rec('D', f'control {var} ({desc}): fails on {fails}/{len(keep)}', fails == 0, 'insensitive, as predicted')
        else:
            rec('D', f'control {var} ({desc}) must fail: fails on {fails}/{len(keep)}', fails > 0,
                '' if best is None else f'minimal: u1={best[1]["u1"]} u2={best[1]["u2"]} rows={best[1]["rows"]}')
    OUT['D_controls'] = res


# ------------------------------------------------------------------------------------------------
# E. end-to-end replay of the first Poisson transform of block (A) at tiny scale
# ------------------------------------------------------------------------------------------------
def bump(y, lo=1.0, hi=2.4):
    if not (lo < y < hi):
        return 0.0
    return math.exp(2.0 - 1.0 / ((y - lo) * (hi - y)) * 0.49)


def lattice(R, z0=0j):
    A = int(math.sqrt(4 * R / 3)) + abs(int(z0.real)) + abs(int(z0.imag)) + 3
    a, b = np.meshgrid(np.arange(-A, A + 1), np.arange(-A, A + 1), indexing='ij')
    a, b = a.ravel(), b.ravel()
    zr, zi = a - b / 2.0, b * SQ3 / 2.0
    q = (zr - z0.real) ** 2 + (zi - z0.imag) ** 2
    sel = q <= R
    a, b, q = a[sel], b[sel], q[sel]
    o = np.argsort(q, kind='stable')
    return a[o].astype(np.int64), b[o].astype(np.int64), q[o]


def part_E(rng):
    K = 4000.0 if QUICK else 10000.0
    X = 58.0
    pA, pB = PR['7a'], PR['7b']
    Bs = [dict(), {pA: 1}, {pA: 2}, {pB: 1}, {pA: 1, pB: 1}, {pA: 3}]
    small = [P for P in PRIMES if P.N <= 139]
    ns = []
    for P in small:
        if 1.0 < P.N / X < 2.4:
            ns.append([P])
    for P, Q in itertools.combinations(small, 2):
        if 1.0 < P.N * Q.N / X < 2.4:
            ns.append([P, Q])
    if QUICK:
        ns = ns[::2]
    beta0 = [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in Bs]
    z0s = {'radial': 0j, 'shifted': complex(37.3, -21.9)}
    configs = [
        {'name': 'f=1, empty mark, nu6, puncture 73a', 'f': [], 'lists': [], 'nu': 'nu6', 'rho': {'73a'}},
        {'name': 'f=13a, two slot lists, chi4', 'f': [PR['13a']],
         'lists': [{pA: 0.6 + 0.3j, PR['13b']: -0.8 + 0.1j, PR['97a']: 0.3}, {PR['19a']: 1.1, PR['61a']: 0.4 - 0.7j, pB: 0.5j}],
         'nu': 'chi4', 'rho': set()},
        {'name': 'f=7b (meets b), one slot list, trivial nu, puncture 103a', 'f': [pB],
         'lists': [{PR['13a']: 1.0, PR['19b']: -0.6 + 0.6j, PR['109a']: 0.8, pA: 0.5 - 0.2j}], 'nu': 'triv',
         'rho': {'103a'}},
    ]
    if QUICK:
        configs = configs[:2]
    primes_used = sorted({P for n in ns for P in n} | {pA, pB}, key=lambda P: P.name)

    def markv(pset, lists):
        v = 1.0 + 0j
        for L in lists:
            v *= sum(c for P, c in L.items() if P in pset)
        return v

    # -------- RHS ingredients: h-sums, cached per (u1, u2, R1 with t, d, Phi) --------
    tuples = []
    maxcut = 0.0
    for i1, b1 in enumerate(Bs):
        for i2, b2 in enumerate(Bs):
            for n1 in ns:
                for n2 in ns:
                    dec = decompose(n1, n2, b1, b2)
                    qm = enorm(dec['m1'])
                    for r in range(len(dec['Rmask']) + 1):
                        for D in itertools.combinations(dec['Rmask'], r):
                            maxcut = max(maxcut, 9.0 * enorm(gen_of(list(D))) * qm / K)
                    tuples.append((i1, i2, n1, n2, dec))
    Ha, Hb, Hq = lattice(maxcut * 1.0001)
    hcodes = {P: P.codes(Ha, Hb) for P in primes_used}
    Hc = Ha - Hb / 2.0 + 1j * Hb * SQ3 / 2.0
    print(f'  E: {len(ns)} columns, {len(Bs)} cube ideals, {len(tuples)} raw tuples, h-lattice {len(Ha)} points '
          f'(N(h) <= {maxcut:.0f}), K = {K:g}', flush=True)
    hcache = {}

    def hsum(dec, D, phi):
        key = (tuple(P.name for P in dec['U1']), tuple(P.name for P in dec['U2']),
               tuple((P.name, dec['t'][P]) for P in dec['R1']), tuple(P.name for P in D), phi)
        if key in hcache:
            return hcache[key]
        qm, d = enorm(dec['m1']), gen_of(list(D))
        qd = enorm(d)
        cut = 9.0 * qd * qm / K
        n = int(np.searchsorted(Hq, cut, side='right'))
        ex = np.zeros(n, dtype=np.int64)
        zero = np.zeros(n, dtype=bool)
        # H(h) = conj chi_u1(h) * chi_u2(h) * conj psi_R(h): the h-parts of Coef_1, conj Coef_2 and OUTER
        for P, s in [(P, -1) for P in dec['U1']] + [(P, 1) for P in dec['U2']] + [(P, -dec['t'][P]) for P in dec['R1']]:
            c = hcodes[P][:n]
            zero |= (c == 6)
            ex += s * c.astype(np.int64)
        H = ZETA_ARR[np.where(zero, 6, ex % 6)]
        assert Hq[0] == 0                                  # lattice sorted by norm: index 0 is h = 0
        if phi == 'radial':
            ker = K * (2 / SQ3) * np.exp(-4 * np.pi * K * Hq[:n] / (3 * qd * qm))
        else:
            z0 = z0s[phi]
            y = Hc[:n] / ecx(emul(d, dec['m1']))
            ker = np.exp(-4j * np.pi * (z0 * y).imag / SQ3) * (2 / SQ3) * K * np.exp(-4 * np.pi * K * np.abs(y) ** 2 / 3)
        val = (complex(np.sum(H * ker)) / math.sqrt(qm), complex(H[0] * ker[0]) / math.sqrt(qm))   # (all h, h = 0)
        hcache[key] = val
        return val

    out = []
    for cfg in configs:
        nu, rho, f, lists = NUS[cfg['nu']], cfg['rho'], cfg['f'], cfg['lists']
        fa = gen_of(f)
        beta = [beta0[i] * (0 if set(b) & set(f) else 1) for i, b in enumerate(Bs)]
        coefn = {}
        for n in ns:
            coefn[tuple(n)] = a_coef(n, nu, rho) * chi_n(n, fa, 4) * bump(enorm(gen_of(n)) / X)
        for phi in ('radial', 'shifted'):
            z0 = z0s[phi]
            # -------- LHS: direct lattice sum over k (no Poisson, no decomposition) --------
            ka, kb, kq = lattice(12 * K, z0)
            kcodes = {P: P.codes(ka, kb) for P in primes_used}
            if phi == 'radial':
                Phi = np.exp(-np.pi * kq / K)
            else:
                Phi = np.exp(-np.pi * kq / K)            # kq is |k - z0|^2 here
            Sb = [np.zeros(len(ka), dtype=complex) for _ in Bs]
            for n in ns:
                cn = coefn[tuple(n)]
                if cn == 0:
                    continue
                ex = np.zeros(len(ka), dtype=np.int64)
                zero = np.zeros(len(ka), dtype=bool)
                for P in n:
                    zero |= (kcodes[P] == 6)
                    ex += kcodes[P].astype(np.int64)
                chik = ZETA_ARR[np.where(zero, 6, ex % 6)]
                for i, b in enumerate(Bs):
                    if beta[i] == 0:
                        continue
                    mk = markv(set(n) | set(b), lists) if lists else 1.0
                    if mk != 0:
                        Sb[i] += (cn * mk) * chik
            T = np.zeros(len(ka), dtype=complex)
            for i, b in enumerate(Bs):
                if beta[i] == 0:
                    continue
                ex = np.zeros(len(ka), dtype=np.int64)
                zero = np.zeros(len(ka), dtype=bool)
                for P, v in b.items():
                    zero |= (kcodes[P] == 6)
                    ex += 3 * v * kcodes[P].astype(np.int64)
                T += beta[i] * ZETA_ARR[np.where(zero, 6, ex % 6)] * Sb[i]
            LHS = float(np.sum(Phi * np.abs(T) ** 2))
            # -------- RHS: Lemma 17.5 per raw tuple, coefficients in form (C) --------
            RHS = {'': 0j, 'drop_RPT': 0j, 'drop_E': 0j}
            RHS0 = 0j                                        # h = 0 (principal zero-frequency) part
            nterms = nnz = 0
            for (i1, i2, n1, n2, dec) in tuples:
                if beta[i1] == 0 or beta[i2] == 0:
                    continue
                W1, W2 = bump(enorm(gen_of(n1)) / X), bump(enorm(gen_of(n2)) / X)
                if any(P.name in rho for P in n1 + n2):
                    continue
                b1, b2 = Bs[i1], Bs[i2]
                # marks after the slot-priority assignment: outer slots x d_I'(u_i)
                mks = []
                for n, b, A, U in ((n1, b1, dec['A1'], dec['U1']), (n2, b2, dec['A2'], dec['U2'])):
                    if not lists:
                        mks.append(1.0)
                        continue
                    oset = set(b) | set(A) | set(dec['C'])
                    s = 0j
                    for Ip in itertools.product((0, 1), repeat=len(lists)):
                        term = 1.0 + 0j
                        for L, inu in zip(lists, Ip):
                            term *= sum(c for P, c in L.items() if (P in set(U) if inu else P in oset))
                        s += term
                    mks.append(s)
                if mks[0] == 0 or mks[1] == 0:
                    continue
                pref = beta[i1] * beta[i2].conjugate() * W1 * W2 * mks[0] * mks[1].conjugate()
                # S0 x Sd(d): CLAIM at h = 1 with the h-part split off; h-part carried by hsum()
                for var in RHS:
                    acc = acc0 = 0j
                    for r in range(len(dec['Rmask']) + 1):
                        for D in itertools.combinations(dec['Rmask'], r):
                            D = list(D)
                            cl1 = claim_value(dec, f, (1, 0), D, nu, rho, variant=var)
                            if cl1 == 0:
                                continue
                            hv, hv0 = hsum(dec, D, phi)
                            acc += (mu(D) / enorm(gen_of(D))) * cl1 * hv
                            acc0 += (mu(D) / enorm(gen_of(D))) * cl1 * hv0
                    RHS[var] += pref * acc
                    if var == '':
                        RHS0 += pref * acc0
                nterms += 1
                nnz += abs(hcache.get((tuple(P.name for P in dec['U1']), tuple(P.name for P in dec['U2']),
                                       tuple((P.name, dec['t'][P]) for P in dec['R1']), (), phi), (0, 0))[0]) > 1e-12
            rel = abs(LHS - RHS['']) / abs(LHS)
            relc = {v: abs(LHS - RHS[v]) / abs(LHS) for v in RHS if v}
            nonp = abs(LHS - RHS0)                           # size of the h != 0 (nonprincipal) part
            rel_np = abs(LHS - RHS['']) / nonp
            row = {'config': cfg['name'], 'Phi': phi, 'K': K, 'k_points': int(len(ka)), 'tuples': nterms,
                   'tuples_with_nonvanishing_d1_hsum': nnz, 'LHS': LHS, 'RHS': [RHS[''].real, RHS[''].imag],
                   'RHS_h0': [RHS0.real, RHS0.imag], 'nonprincipal_share': nonp / abs(LHS),
                   'rel_err': rel, 'err_rel_to_nonprincipal_part': rel_np, 'controls_rel_err': relc}
            out.append(row)
            rec('E', f'replay [{cfg["name"]}; {phi} Phi]: LHS {LHS:.12g} vs RHS {RHS[""].real:.12g}{RHS[""].imag:+.1e}i '
                     f'({nterms} tuples, {nnz} with nonvanishing h-sum at d=1; h!=0 share {nonp / abs(LHS):.2e})',
                rel < 1e-9 and rel_np < 1e-9, f'rel err {rel:.1e}, relative to the h!=0 part {rel_np:.1e}')
            rec('E', f'replay controls must break [{cfg["name"]}; {phi}]: drop R(.,P_T) rel {relc["drop_RPT"]:.1e}, '
                     f'drop E rel {relc["drop_E"]:.1e}', min(relc.values()) > 1e-6)
    OUT['E_replay'] = out


# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    rng = random.Random(20261010)
    print(f'sep30_eqc_check.py  quick={QUICK}  primes={len(PRIMES)}', flush=True)
    part_A(rng)
    print(f'  [A done {time.time() - T0:.1f}s]', flush=True)
    ntup = 150 if QUICK else 900
    tuples = [random_tuple(rng, k) for k in range(ntup)]
    part_B(rng, tuples)
    print(f'  [B done {time.time() - T0:.1f}s]', flush=True)
    keep = part_C(rng, tuples)
    print(f'  [C done {time.time() - T0:.1f}s]', flush=True)
    part_D(keep)
    print(f'  [D done {time.time() - T0:.1f}s]', flush=True)
    part_E(rng)
    print(f'  [E done {time.time() - T0:.1f}s]', flush=True)
    npass = sum(r[2] for r in RESULTS)
    print(f'\n{npass}/{len(RESULTS)} checks passed in {time.time() - T0:.1f}s')
    OUT['results'] = [{'part': p, 'claim': c, 'pass': ok, 'detail': d} for p, c, ok, d in RESULTS]
    if '--out' in sys.argv:
        path = sys.argv[sys.argv.index('--out') + 1]
        with open(path, 'w') as fh:
            json.dump(OUT, fh, indent=1, default=str)
        print('wrote', path)
    sys.exit(0 if npass == len(RESULTS) else 1)
