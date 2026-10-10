#!/usr/bin/env python3
"""sep30_misc_checks.py -- bounded checks for SEP30_MISC_REVIEW.md on the OpenAI manuscript
"The Quasi-Riemann Hypothesis", 30 Sep 2026 (pr908 import, paper.tex,
SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3).  External, unreviewed; read as
data.  RH is unsolved; nothing here bears on it.

Status: review instrument (exploration level).
Arithmetic: residue symbols are EXACT integer tables (imported read-only from sep30_eqc_check.py).  Gauss
sums, kernels, bumps and lattice sums are double-precision floating point: EMPIRICAL, not certified.
Tolerance 1e-9 (pointwise absolute on unimodular-or-zero quantities; replay relative).  Exponent
identities are exact sympy/Fraction arithmetic.

Parts
  A  Lemma 17.1 initialization transform (proof 11606-12341), replayed at tiny scale:
     A1  overlap reduction eq:initial-overlap-polynomial (11650-11667): M_u(Z^r;W) Q_u computed directly
         equals the sum over assigned subsets and assigned tuples of U_{u,j}, for both signs, at rows that
         include zeros of the symbols; the y_c support window; normalization Z^{-(r+z)/2}=Z^{-G}Z^{-D'/2}.
     A2  pointwise identities: eq:initial-common-extraction (11866), the s-extraction square
         1_{(s,h')=1} (11876), child character/puncture reconstruction (11893-11899), the Gauss-signal
         factor mu(z1)mu(z2)gamma(conj chi_z1 chi_z2) = a0(z1) conj a0(z2) G([z2][z1]^-1) on the pairs used.
     A3  exact exponent identities: eq:initial-root-kernel, kappa split eq:initial-poisson-prefactor,
         canonical lengths, kappa_c + P_1 + 2F_c = m, the two margin identities (12207-12212).
     A4  END-TO-END replay: sum_u Phi(q_u/K)|R_0(u)|^2 by direct lattice summation equals
         (i)  principal + Lemma 17.5 on raw coprime column pairs (RHS_A), and
         (ii) principal zero frequency + the child form of eq:initial-separated-identity BEFORE the
              Fourier separation (profile evaluated at the actual coordinates): Moebius s-extension,
              common extraction, outer weight eq:initial-outer-weight with priority-split marks,
              child polynomials eq:initial-child-polynomial with k=d'h', f=d's, rho_{t,j} (RHS_B).
         Radial and shifted Gaussians; failing controls (each must break RHS_B in at least one run).
     A5  fibre eq:initial-fibre (12133-12140): brute-force Z-model of (C,d',s,h') -> (t,k,f).
     A6  outer-mask containment (11760-11776): ratio <= Z^tau implies q_{d'h'} <= Z^{M_init}, random
         actual exponents within the eta windows; control with 5 eta.
  B  Lemma 15.1 (8111-8332): exact exponent algebra of the displayed row proof.
  C  Lemma 20.1 (15699-15841): exact exponent algebra.
  D  Prop 2.1 (400-502) and the final contradiction of Thm 1.1: exact arithmetic of the displayed steps.
Run:  nice -n 10 python3 -I sep30_misc_checks.py [--quick] [--out PATH.json]
"""
import cmath
import itertools
import json
import math
import os
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sep30_eqc_check as E  # noqa: E402  (read-only reuse: symbols, Gauss sums, ray functions, lattice)
import sep30_l17_identities as L  # noqa: E402  (read-only reuse: a0, ray-character expansion, marks)
sys.path.pop(0)

QUICK = '--quick' in sys.argv
T0 = time.time()
TOL = 1e-9
SQ3 = math.sqrt(3.0)
RESULTS = []
OUT = {}
PRIMES, PR = E.PRIMES, E.PR
chi_n, chv, gen_of, mu = E.chi_n, E.chv, E.gen_of, E.mu
emul, enorm, ecx, mod4 = E.emul, E.enorm, E.ecx, E.mod4
ZETA_ARR = E.ZETA_ARR
a0, cls, RAYEXP, mark_val = L.a0, L.cls, L.RAYEXP, L.mark_val


def rec(part, claim, ok, detail=''):
    RESULTS.append((part, claim, bool(ok), detail))
    print(('PASS ' if ok else 'FAIL ') + f'[{part}] {claim}' + (f'  -- {detail}' if detail else ''), flush=True)


def ctrl(part, claim, failed, detail=''):
    rec(part, 'CONTROL ' + claim, failed, detail)


def norm(nlist):
    N = 1
    for P in nlist:
        N *= P.N
    return N


def sqfree(pool, lo, hi, maxk=5):
    out = []
    for k in range(0, maxk + 1):
        for c in itertools.combinations(pool, k):
            N = norm(c)
            if lo < N < hi:
                out.append(list(c))
    return out


def bump(y, lo=1.0, hi=2.4):
    return E.bump(y, lo, hi)


def slot(L_, pset):
    """sum_{p in list, p | A} coefficient (one factor of old-eq:4.2)."""
    return sum((c for P, c in L_.items() if P in pset), 0j)


def mark(lists, pset):
    v = 1.0 + 0j
    for L_ in lists:
        v *= slot(L_, pset)
    return v


# ================================================================================================
# A1. overlap reduction
# ================================================================================================
def part_A1(rng):
    Z = 6.0
    r = 2.9
    pool = [P for P in PRIMES if P.N <= 199]
    # three disjoint slot lists; the slot primes are also allowed in n (that is what creates overlaps)
    slots = [  # (z_i, {prime: a_i(p)}) with q_p / Z^{z_i} in (1, 2.4)
        (math.log(5.5, Z), {PR['7a']: 0.9 - 0.2j, PR['7b']: -0.6}),
        (math.log(14.0, Z), {PR['19a']: 0.7, PR['19b']: -0.5 + 0.4j, PR['31a']: 0.8j}),
        (math.log(30.0, Z), {PR['37a']: -0.9, PR['43b']: 0.45 + 0.45j}),
    ]
    for z_i, Li in slots:
        for P in Li:
            assert 1 < P.N / Z ** z_i < 2.4, (P, P.N / Z ** z_i)
    I = list(range(len(slots)))
    z = sum(s[0] for s in slots)
    Xr = Z ** r
    ncols = sqfree(pool, Xr, 2.4 * Xr, maxk=4)
    sfcache = {}

    def cprimes(qj):
        """all squarefree c' with q_{c'} in the W-support window (Xr/q_j, 2.4 Xr/q_j)."""
        if qj not in sfcache:
            sfcache[qj] = sqfree(pool, Xr / qj, 2.4 * Xr / qj, maxk=4)
        return sfcache[qj]
    nus = {'nu6': E.NUS['nu6'], 'chi4': E.NUS['chi4']}
    rows = []
    for _ in range(6 if QUICK else 16):
        u = (rng.randint(-400, 400), rng.randint(-400, 400))
        t = rng.random()
        if t < 0.35:
            u = emul(u, rng.choice([P for s in slots for P in s[1]]).gen)
        elif t < 0.55:
            u = emul(u, rng.choice(pool[:8]).gen)
        if u != (0, 0):
            rows.append(u)
    variants = ['', 'psi_j_once', 'drop_mu_P0', 'drop_cj_coprime', 'ratio_mult', 'drop_mu_j']
    worst = {v: 0.0 for v in variants}
    ycmin, ycmax, nterms = 1e9, 0.0, 0
    for nuname, nu in nus.items():
        for eps in (1, -1):
            pc_cache = {}

            def psi(nlist, u):
                if not nlist:
                    return 1.0 + 0j
                key = (tuple(sorted(P.name for P in nlist)), u)
                if key not in pc_cache:
                    pc_cache[key] = nu(cls(nlist)) * chi_n(nlist, u, eps)
                return pc_cache[key]
            for u in rows:
                Mu = Z ** (-r / 2) * sum(mu(n) * psi(n, u) * bump(norm(n) / Xr) for n in ncols)
                Qu = 1.0 + 0j
                for z_i, Li in slots:
                    Qu *= Z ** (-z_i / 2) * sum(a * psi([P], u) * bump(P.N / Z ** z_i) for P, a in Li.items())
                direct = Mu * Qu
                red = {v: 0j for v in variants}
                for A in itertools.chain.from_iterable(itertools.combinations(I, k) for k in range(len(I) + 1)):
                    I0 = [i for i in I if i not in A]
                    G = sum(slots[i][0] for i in A)
                    Dp = r + z - 2 * G
                    for tupA in itertools.product(*[list(slots[i][1].items()) for i in A]):
                        j = [P for P, _ in tupA]
                        qj = norm(j)
                        yj = qj / Z ** G
                        outerA = np.prod([a * bump(P.N / Z ** slots[i][0]) for i, (P, a) in zip(A, tupA)]) if A else 1.0
                        pj = psi(j, u)
                        for tup0 in itertools.product(*[list(slots[i][1].items()) for i in I0]):
                            P0 = [P for P, _ in tup0]
                            w = 1.0 + 0j
                            yprod = 1.0
                            for i, (P, a) in zip(I0, tup0):
                                yi = P.N / Z ** slots[i][0]
                                w *= a * bump(yi)
                                yprod *= yi
                            for cp in cprimes(qj):
                                if set(cp) & set(P0):
                                    continue                      # c = P_0 c' not squarefree: mu(c) = 0
                                c = P0 + cp
                                pc = mu(c) * psi(c, u)
                                if pc == 0:
                                    continue
                                yc = norm(c) / Z ** Dp
                                hitj = bool(set(c) & set(j))
                                for v in variants:
                                    if hitj and v != 'drop_cj_coprime':
                                        continue
                                    arg = yj * yc * yprod if v == 'ratio_mult' else yj * yc / yprod
                                    wv = bump(arg)
                                    if wv == 0:
                                        continue
                                    if v == '':
                                        ycmin, ycmax = min(ycmin, yc), max(ycmax, yc)
                                        nterms += 1
                                    pre = (pj if v == 'psi_j_once' else pj ** 2) * Z ** (-G) * Z ** (-Dp / 2)
                                    pre *= outerA * (1 if v == 'drop_mu_j' else mu(j))
                                    sg = 1 if v == 'drop_mu_P0' else mu(P0)
                                    red[v] += pre * pc * sg * w * wv
                for v in variants:
                    e = abs(direct - red[v])
                    worst[v] = max(worst[v], e / abs(direct) if abs(direct) > 1e-12 else e)
    lo, hi = 2.4 ** (-len(I)), 2.4 ** (1 + len(I))
    rec('A1', f'eq:initial-overlap-polynomial: M_u Q_u (direct) = sum over assigned subsets/tuples of U_(u,j); '
        f'{len(rows)} rows x 2 characters x 2 signs, 3 slots, {nterms} nonzero inner terms', worst[''] < TOL,
        f'max rel err {worst[""]:.1e}')
    rec('A1', f'y_c lies in the fixed window ({lo:.3f}, {hi:.1f}) on every nonzero term', lo < ycmin and ycmax < hi,
        f'observed [{ycmin:.3f}, {ycmax:.2f}]')
    for v in variants[1:]:
        ctrl('A1', f'{v} breaks the overlap identity', worst[v] > 1e-6, f'max rel err {worst[v]:.1e}')
    OUT['A1'] = dict(worst=worst, yc=[ycmin, ycmax], rows=len(rows), nterms=nterms)


# ================================================================================================
# A2. pointwise identities
# ================================================================================================
def part_A2(rng):
    sq = [P for P in PRIMES if P.N <= 61]
    pool = [P for P in PRIMES if P.N <= 97]
    nu0 = E.NUS['nu6']
    th = 5                                      # one ray character index for nu_* = nu_0 conj theta

    def Astar(z):
        return a0(z) * nu0(cls(z)) * L.raych(th, cls(z)).conjugate() if z else 1.0 + 0j

    w = wc1 = wc2 = wc3 = 0.0
    cnt = 0
    for _ in range(150 if QUICK else 500):
        s = rng.sample(sq, rng.randint(0, 2))
        n = rng.sample([P for P in sq if P not in s], rng.randint(0, 2))
        if norm(s) * norm(n) > 40000:
            continue
        dp = L.rand_sf(rng, pool, 2)
        hp = (rng.randint(-120, 120), rng.randint(-120, 120))
        if rng.random() < 0.3 and (s or n):
            hp = emul(hp, rng.choice(s + n).gen)
        dg = gen_of(dp)
        lhs = Astar(s + n) * chi_n(s + n, dg).conjugate() * chi_n(s + n, hp)
        sp = Astar(s) * chi_n(s, dg).conjugate() * chi_n(s, hp)
        k = emul(dg, hp)
        f = emul(dg, gen_of(s))
        rhs = sp * Astar(n) * chi_n(n, k) * chi_n(n, f, 4)
        w = max(w, abs(lhs - rhs))
        wc1 = max(wc1, abs(lhs - sp * Astar(n) * chi_n(n, k) * chi_n(n, dg, 4)))           # drop chi_n(s)^4
        wc2 = max(wc2, abs(lhs - sp * Astar(n) * chi_n(n, k) * chi_n(n, f, 4).conjugate()))  # wrong orientation
        wc3 = max(wc3, abs(lhs - sp * Astar(n) * chi_n(n, hp) * chi_n(n, f, 4)))           # k without d'
        cnt += 1
    rec('A2', f'eq:initial-common-extraction A*(sn) conj chi_sn(d\') chi_sn(h\') = [s-part] A*(n) chi_n(d\'h\') '
        f'chi_n(d\'s)^4, incl. zeros ({cnt} cases)', w < TOL, f'max err {w:.1e}')
    ctrl('A2', 'CRT factor chi_n(s)^4 dropped', wc1 > 1e-6, f'{wc1:.1e}')
    ctrl('A2', 'conj chi_n(d\'s)^4 in place of chi_n(d\'s)^4', wc2 > 1e-6, f'{wc2:.1e}')
    ctrl('A2', 'k = h\' without d\'', wc3 > 1e-6, f'{wc3:.1e}')

    # |A*(s) conj chi_s(d') chi_s(h')|^2 = 1_{(s,h')=1} when d' | C, (s, C) = 1
    bad = 0
    for _ in range(600 if QUICK else 2000):
        C = L.rand_sf(rng, pool, 3)
        dp = [P for P in C if rng.random() < 0.5]
        s = L.rand_sf(rng, pool, 2, C)
        hp = (rng.randint(-150, 150), rng.randint(-150, 150))
        if rng.random() < 0.3 and s:
            hp = emul(hp, rng.choice(s).gen)
        v = abs(Astar(s) * chi_n(s, gen_of(dp)).conjugate() * chi_n(s, hp)) ** 2
        want = 0.0 if any(P.code(hp) == 6 for P in s) else 1.0
        bad += abs(v - want) > TOL
    rec('A2', 's-extraction square |A*(s) conj chi_s(d\') chi_s(h\')|^2 = 1_(s,h\')=1 for d\'|C, (s,C)=1', bad == 0,
        f'{bad} failures')

    # exclusions: for squarefree s n and pairwise data, the original column conditions
    # 1_{(sn, Cj)=1} * [n coprime to s] * (numerator zeros at d',h')  ==  1_{(s,Cj)=1} * zero-pattern of
    # rho_{t,j}(n) chi_n(k) chi_n(f)^4  with t = C/d', k = d'h', f = d's
    bad = badc = 0
    for _ in range(1000 if QUICK else 4000):
        C = L.rand_sf(rng, pool, 3)
        j = L.rand_sf(rng, pool, 1, C)
        dp = [P for P in C if rng.random() < 0.5]
        t = [P for P in C if P not in dp]
        s = L.rand_sf(rng, pool, 2)
        n = L.rand_sf(rng, pool, 2)
        hp = (rng.randint(-150, 150), rng.randint(-150, 150))
        if rng.random() < 0.3 and n:
            hp = emul(hp, rng.choice(n).gen)
        if set(s) & (set(C) | set(j)):
            continue
        orig = (not set(n) & (set(C) | set(j) | set(s))) and all(P.code(hp) != 6 for P in n)
        k = emul(gen_of(dp), hp)
        f = emul(gen_of(dp), gen_of(s))
        rho = not set(n) & (set(t) | set(j))
        child = rho and abs(chi_n(n, k) * chi_n(n, f, 4)) > 0.5
        childc = (not set(n) & set(j)) and abs(chi_n(n, k) * chi_n(n, f, 4)) > 0.5    # rho without t
        bad += orig != child
        badc += orig != childc
    rec('A2', 'rho_{t,j}(n) chi_n(k) chi_n(f)^4 reproduces exactly the original exclusions at C, s, j and the '
        'numerator zeros at d\', h\' (11893-11899)', bad == 0, f'{bad} mismatches')
    ctrl('A2', 'puncture without t', badc > 0, f'{badc} mismatches')

    # Gauss-signal factor on directly summed Gauss sums (pairs of the size used in A4 when small)
    w = 0.0
    cnt = 0
    for _ in range(60 if QUICK else 200):
        z1 = rng.sample(sq, rng.randint(0, 2))
        z2 = rng.sample([P for P in sq if P not in z1], rng.randint(0, 2))
        if norm(z1) * norm(z2) > 30000 or not (z1 or z2):
            continue
        chars = [(P, -1) for P in z1] + [(P, 1) for P in z2]
        lhs = mu(z1) * mu(z2) * E.gauss(chars, gen_of(z1 + z2))
        rhs = a0(z1) * a0(z2).conjugate() * E.Gcls(emul(cls(z2), E.inv4(cls(z1))))
        w = max(w, abs(lhs - rhs))
        cnt += 1
    rec('A2', f'mu(z1)mu(z2) gamma(conj chi_z1 chi_z2; z1z2) = a0(z1) conj a0(z2) G([z2][z1]^-1), direct Gauss '
        f'sums ({cnt} pairs)', w < TOL, f'{w:.1e}')


# ================================================================================================
# A3. exact exponent identities of the initialization
# ================================================================================================
def part_A3():
    import sympy as sp
    m, r, z, G, B, th, v, H, eta = sp.symbols('m r z G B theta v H eta', real=True)
    Dp = r + z - 2 * G
    z0 = z - G
    P1 = B - th
    kc = m - 2 * Dp + P1
    Nc = Dp - B - v
    Vc = th + v
    Fc = Dp - P1
    Mc = 2 * Dp - m - 2 * P1
    ok = []
    # root: Z^{-D'} Z^m / (q_d' q_s sqrt(q_n1 q_n2)) with q_d'=Z^th x_d, q_s = Z^v x_s, q_n = Z^Nc x
    ok.append(sp.simplify((-Dp + m - th - v - Nc) - kc) == 0)
    # kernel: Z^{m+H} / (q_d' q_s^2 q_n1 q_n2)
    ok.append(sp.simplify((m + H - th - 2 * v - 2 * Nc) - (m + H - th - 2 * (Dp - B))) == 0)
    # W_0 argument: q_C q_s q_n / Z^D' = x_C x_s x_n
    ok.append(sp.simplify(B + v + Nc - Dp) == 0)
    # canonical lengths
    ok.append(sp.simplify(Nc + Vc - Fc) == 0)
    # energy identity kappa_c + P1 + 2 Fc = m
    ok.append(sp.simplify(kc + P1 + 2 * Fc - m) == 0)
    # margins (12207-12212)
    ok.append(sp.simplify(Fc - Mc - (P1 + G) - z0 - (m - r - 2 * z + 2 * G)) == 0)
    ok.append(sp.simplify(4 * Fc - 3 * Mc - 6 * z0 - (3 * m - 2 * r - 8 * z + 10 * G + 2 * P1)) == 0)
    # normalization
    ok.append(sp.simplify((r + z) / 2 - (G + Dp / 2)) == 0)
    # kappa split (11780-11786): kappa_1 + kappa_2 = 2(m - D' - theta^ - L^/2) with L^ = c1+c2-2B
    c1, c2 = sp.symbols('c1 c2', real=True)
    k1 = m - Dp - th - c1 + B
    k2 = m - Dp - th - c2 + B
    ok.append(sp.simplify(k1 + k2 - 2 * (-Dp + m - th - (c1 + c2 - 2 * B) / 2)) == 0)
    # side bound kappa_i <= kc + 3 eta at worst-case deviations (theta^ >= theta - eta, c_i >= D' - eta, B^ <= B + eta)
    ok.append(sp.simplify((m - Dp - (th - eta) - (Dp - eta) + (B + eta)) - (kc + 3 * eta)) == 0)
    rec('A3', 'initialization exponents: root, kernel, W_0 argument, F_c = N_c + V_c, kappa_c + P_1 + 2F_c = m, '
        'both margin identities, normalization, kappa split and its 3 eta (exact sympy)', all(ok),
        f'{sum(ok)}/{len(ok)}')
    # margins under the premises: m-r-2z+2G >= c1 and 3m-2r-8z+10G+2P1 >= c2 - 4 eta
    rng = random.Random(5)
    bad = badc = 0
    for _ in range(20000):
        c1v, c2v = Fr(rng.randint(1, 50), 100), Fr(rng.randint(1, 50), 100)
        rv, zv = Fr(rng.randint(0, 200), 100), Fr(rng.randint(0, 100), 100)
        mv = max(rv + 2 * zv + c1v, (2 * rv + 8 * zv + c2v) / 3) + Fr(rng.randint(0, 30), 100)
        Gv = Fr(rng.randint(0, 100), 100) * zv
        etav = Fr(rng.randint(0, 10), 1000)
        P1v = Fr(rng.randint(-20, 100), 1000)
        if P1v < -2 * etav:
            P1v = -2 * etav
        bad += not (mv - rv - 2 * zv + 2 * Gv >= c1v)
        bad += not (3 * mv - 2 * rv - 8 * zv + 10 * Gv + 2 * P1v >= c2v - 4 * etav)
        badc += not (3 * mv - 2 * rv - 8 * zv + 10 * Gv + 2 * P1v >= c2v - 3 * etav) and P1v == -2 * etav \
            and Gv == 0 and 2 * rv + 8 * zv + c2v == 3 * mv
    rec('A3', 'formal margins >= c_1 and >= c_2 - 4 eta under the marked premises, G >= 0, P_1 >= -2 eta '
        '(20000 exact random instances)', bad == 0, f'{bad} failures')


# ================================================================================================
# A4. end-to-end replay
# ================================================================================================
def part_A4(rng):
    X = 300.0 if not QUICK else 200.0
    pool = [P for P in PRIMES if P.N <= (79 if not QUICK else 61)]
    cfgs = [
        dict(name='j=13a, nu_0=nu6, upsilon=1.3, two surviving slot lists', j=[PR['13a']], nu='nu6', ups=1.3,
             lists=[{PR['7b']: 0.8 - 0.3j, PR['31a']: 0.5, PR['61a']: -0.4j}, {PR['37b']: 0.7, PR['19a']: -0.5 + 0.2j}],
             K=1500.0 if not QUICK else 900.0),
        dict(name='j=7a.19b, nu_0=chi4, upsilon=-0.7, one surviving slot list', j=[PR['7a'], PR['19b']], nu='chi4',
             ups=-0.7, lists=[{PR['13b']: 1.0, PR['43a']: 0.3 + 0.6j, PR['31b']: -0.6}], K=600.0),
    ]
    if QUICK:
        cfgs = cfgs[:1]
    z0s = {'radial': 0j, 'shifted': complex(17.3, -9.1)}
    variants = ['', 'drop_mu_s', 'f_no_s', 'k_no_d', 'rho_no_t', 'rho_no_j', 'theta_swap', 'drop_sh_mask',
                'assigned_dropped', 'kernel_lcm_norm']
    out = []
    for cfg in cfgs:
        nu0 = E.NUS[cfg['nu']]
        K, j, lists, ups = cfg['K'], cfg['j'], cfg['lists'], cfg['ups']
        jset = set(j)

        def W0(y):
            b = bump(y)
            return b * cmath.exp(1j * ups * math.log(y)) if b else 0j

        def coef(c):
            if set(c) & jset:
                return 0j
            return mu(c) * nu0(cls(c)) * mark(lists, set(c)) * W0(norm(c) / X)
        cols = sqfree(pool, X, 2.4 * X, maxk=4)
        cc = {tuple(c): coef(c) for c in cols}
        cc = {k_: v_ for k_, v_ in cc.items() if v_ != 0}
        used = sorted({P for k_ in cc for P in k_} | set(pool), key=lambda P: P.name)
        allsf = sqfree(pool, 0, 2.4 * X + 1, maxk=4)
        for phi, z0 in z0s.items():
            # ---------------- LHS ----------------
            ua, ub, uq = E.lattice(12 * K, z0)
            ucodes = {P: P.codes(ua, ub) for P in used}
            Ru = np.zeros(len(ua), dtype=complex)
            for k_, c_ in cc.items():
                ex = np.zeros(len(ua), dtype=np.int64)
                zero = np.zeros(len(ua), dtype=bool)
                for P in k_:
                    zero |= (ucodes[P] == 6)
                    ex -= ucodes[P].astype(np.int64)                 # conj chi_c(u)
                Ru += c_ * ZETA_ARR[np.where(zero, 6, ex % 6)]
            LHS = float(np.sum(np.exp(-np.pi * uq / K) * np.abs(Ru) ** 2)) / X     # Z^{-D'} = 1/X
            # ---------------- common h-lattice ----------------
            HA, HB, HQ = E.lattice(9.0 * (2.4 * X) ** 2 / K * 1.0001)
            HC = HA - HB / 2.0 + 1j * HB * SQ3 / 2.0
            nz = HQ > 0
            HA, HB, HQ, HC = HA[nz], HB[nz], HQ[nz], HC[nz]

            def kernel(n, w_den_gen, qden):
                """K * F Phi at h / den for the first n lattice points (h != 0)."""
                if phi == 'radial':
                    return K * (2 / SQ3) * np.exp(-4 * np.pi * K * HQ[:n] / (3 * qden))
                w = HC[:n] / ecx(w_den_gen)
                return np.exp(-4j * np.pi * (z0 * w).imag / SQ3) * (2 / SQ3) * K * np.exp(-4 * np.pi * K * np.abs(w) ** 2 / 3)
            # principal zero frequency (z1 = z2 = 1, h = 0): K sum_{d|C} mu(d)/q_d * F Phi(0)
            P0 = 0.0
            for k_, c_ in cc.items():
                s_ = sum(mu(list(D)) / norm(D) for r_ in range(len(k_) + 1) for D in itertools.combinations(k_, r_))
                P0 += abs(c_) ** 2 * K * (2 / SQ3) * s_
            P0 /= X
            # ---------------- RHS_A: Lemma 17.5 on raw coprime pairs ----------------
            RHS_A = P0
            keys = list(cc)
            for k1 in keys:
                for k2 in keys:
                    Cl = [P for P in k1 if P in k2]
                    z1 = [P for P in k1 if P not in k2]
                    z2 = [P for P in k2 if P not in k1]
                    qm = norm(z1) * norm(z2)
                    mg = gen_of(z1 + z2)
                    # mu(c1)mu(c2) gamma via the signal identity (checked directly in A2 for small pairs)
                    gam = a0(z1) * a0(z2).conjugate() * E.Gcls(emul(cls(z2), E.inv4(cls(z1)))) if (z1 or z2) else 1.0
                    # gamma(conj chi_z1 chi_z2; z1z2) = mu(z1)mu(z2) a0(z1) conj a0(z2) G([z2][z1]^-1)
                    base = cc[k1] * cc[k2].conjugate() * mu(z1) * mu(z2) * gam
                    tot = 0j
                    for r_ in range(len(Cl) + 1):
                        for D in itertools.combinations(Cl, r_):
                            D = list(D)
                            qd = norm(D)
                            dg = gen_of(D)
                            psid = (chi_n(z1, dg).conjugate() * chi_n(z2, dg)) if (z1 or z2) else 1.0
                            if psid == 0:
                                continue
                            n = int(np.searchsorted(HQ, 9.0 * qd * qm / K, side='right'))
                            zero = np.zeros(n, dtype=bool)
                            ex = np.zeros(n, dtype=np.int64)
                            for P in z1:
                                c = P.codes(HA[:n], HB[:n])
                                zero |= c == 6
                                ex += c.astype(np.int64)
                            for P in z2:
                                c = P.codes(HA[:n], HB[:n])
                                zero |= c == 6
                                ex -= c.astype(np.int64)
                            Hv = ZETA_ARR[np.where(zero, 6, ex % 6)]
                            tot += mu(D) * psid / qd * complex(np.sum(Hv * kernel(n, emul(dg, mg), qd * qm)))
                    RHS_A += base * tot / math.sqrt(qm) / X
            # ---------------- RHS_B: child form ----------------
            RHS = {vv: P0 for vv in variants}
            hcache = {}
            nterm = 0
            Cs = [C for C in allsf if not set(C) & jset]
            for C in Cs:
                qC = norm(C)
                for s in allsf:
                    qs = norm(s)
                    if qC * qs >= 2.4 * X:
                        continue
                    if set(s) & (set(C) | jset):
                        continue                                   # explicit 1_{(s,Cj)=1}
                    ns = [n for n in allsf if X < qC * qs * norm(n) < 2.4 * X]
                    if not ns:
                        continue
                    for r_ in range(len(C) + 1):
                        for dp in itertools.combinations(C, r_):
                            dp = list(dp)
                            t = [P for P in C if P not in dp]
                            qd = norm(dp)
                            dg = gen_of(dp)
                            for vv in variants:
                                fl = dp + ([] if vv == 'f_no_s' else s)
                                fgen = gen_of(fl)
                                pun = (set() if vv == 'rho_no_t' else set(t)) | (set() if vv == 'rho_no_j' else jset)
                                outer_sets = set(C) | set(s)
                                # child summands per side, with the priority split of the mark
                                subs = list(itertools.product((0, 1), repeat=len(lists)))
                                qn = {}
                                for n in ns:
                                    if set(n) & pun:
                                        continue
                                    b = a0(n) * nu0(cls(n)) * chi_n(n, fgen, 4) * W0(qC * qs * norm(n) / X)
                                    if b == 0:
                                        continue
                                    parts = []
                                    for Ip in subs:
                                        if vv == 'assigned_dropped' and any(k_ == 0 for k_ in Ip):
                                            parts.append(0j)
                                            continue
                                        term = 1.0 + 0j
                                        for keep, L_ in zip(Ip, lists):
                                            term *= slot(L_, set(n)) if keep else slot(L_, outer_sets)
                                        parts.append(term)
                                    qn[tuple(n)] = (b, sum(parts))
                                if not qn:
                                    continue
                                sgn = (1 if vv == 'drop_mu_s' else mu(s)) * mu(dp)
                                for n1, (b1, m1) in qn.items():
                                    for n2, (b2, m2) in qn.items():
                                        c1, c2 = cls(list(n1)), cls(list(n2))
                                        ray = RAYEXP[(c1, c2, vv == 'theta_swap')] * nu0(c1) * nu0(c2).conjugate()
                                        qz = qs * qs * norm(n1) * norm(n2)
                                        qzk = qz if vv != 'kernel_lcm_norm' else qs * norm(n1) * norm(n2)
                                        hv = vv if vv in ('k_no_d', 'drop_sh_mask', 'kernel_lcm_norm') else ''
                                        key = (tuple(P.name for P in dp), tuple(P.name for P in s),
                                               tuple(P.name for P in n1), tuple(P.name for P in n2), hv)
                                        if key not in hcache:
                                            n_ = int(np.searchsorted(HQ, 9.0 * qd * qzk / K, side='right'))
                                            a, bb = HA[:n_], HB[:n_]
                                            if vv == 'k_no_d':
                                                ka, kb = a, bb
                                            else:
                                                p, q = dg
                                                ka, kb = a * p - bb * q, a * q + bb * p - bb * q
                                            zero = np.zeros(n_, dtype=bool)
                                            ex = np.zeros(n_, dtype=np.int64)
                                            if vv != 'drop_sh_mask':
                                                for P in s:
                                                    zero |= P.codes(a, bb) == 6
                                            for P in n1:
                                                c = P.codes(ka, kb)
                                                zero |= c == 6
                                                ex += c.astype(np.int64)
                                            for P in n2:
                                                c = P.codes(ka, kb)
                                                zero |= c == 6
                                                ex -= c.astype(np.int64)
                                            Hv = ZETA_ARR[np.where(zero, 6, ex % 6)]
                                            den = emul(dg, emul(emul(gen_of(s), gen_of(s)),
                                                                emul(gen_of(list(n1)), gen_of(list(n2)))))
                                            if vv == 'kernel_lcm_norm':
                                                den = emul(dg, emul(gen_of(s), emul(gen_of(list(n1)), gen_of(list(n2)))))
                                            hcache[key] = complex(np.sum(Hv * kernel(n_, den, qd * qzk)))
                                        hs = hcache[key]
                                        pre = sgn * b1 * m1 * (b2 * m2).conjugate() * ray / (qd * qs * math.sqrt(norm(n1) * norm(n2)))
                                        RHS[vv] += pre * hs / X
                                        if vv == '':
                                            nterm += 1
            errA = abs(LHS - RHS_A) / LHS
            errB = abs(LHS - RHS['']) / LHS
            share = abs(LHS - P0) / LHS
            r_ = dict(cfg=cfg['name'], phi=phi, K=K, X=X, LHS=LHS, P0=P0, RHS_A=str(RHS_A), RHS_B=str(RHS['']),
                      errA=errA, errB=errB, nonzero_freq_share=share, terms=nterm,
                      controls={vv: abs(LHS - RHS[vv]) / LHS for vv in variants if vv})
            out.append(r_)
            print(f"    A4 {cfg['name']} [{phi}]: LHS {LHS:.10f}  RHS_A rel err {errA:.1e}  RHS_B rel err {errB:.1e}  "
                  f"nonzero-frequency share {share:.2e}  ({nterm} child terms, {time.time() - T0:.0f}s)  controls: " +
                  ', '.join(f'{k_} {v_:.1e}' for k_, v_ in r_['controls'].items()), flush=True)
    OUT['A4'] = out
    rec('A4', f'Lemma 17.5 on raw coprime column pairs: sum_u Phi|R_0(u)|^2 (direct) = principal + nonprincipal '
        f'Poisson ({len(out)} runs)', max(o['errA'] for o in out) < TOL, f"max rel err {max(o['errA'] for o in out):.1e}")
    rec('A4', f'eq:initial-separated-identity before separation: direct = P_0 + child form (s-Moebius, extraction, '
        f'outer weight, priority-split marks, k=d\'h\', f=d\'s, rho_(t,j)) ({len(out)} runs)',
        max(o['errB'] for o in out) < TOL, f"max rel err {max(o['errB'] for o in out):.1e}")
    rec('A4', 'non-vacuity: the nonzero-frequency part is a visible share of the LHS in every run',
        min(o['nonzero_freq_share'] for o in out) > 1e-4,
        f"min share {min(o['nonzero_freq_share'] for o in out):.1e}")
    for vv in variants[1:]:
        per = [o['controls'][vv] for o in out]
        ctrl('A4', f'{vv} breaks the child-form replay (in at least one run)', max(per) > 1e-6,
             'per-run rel err: ' + ', '.join(f'{x:.1e}' for x in per))


# ================================================================================================
# A5. fibre bound, Z-model
# ================================================================================================
def part_A5():
    from sympy import factorint, divisors

    def sqf(n):
        return all(e == 1 for e in factorint(n).values())
    LIM = 60 if QUICK else 120
    HLIM = 40
    fib = {}
    for C in range(1, LIM + 1):
        if not sqf(C):
            continue
        for d in divisors(C):
            for s in range(1, LIM + 1):
                if not sqf(s) or math.gcd(s, C) != 1:
                    continue
                for h in range(1, HLIM + 1):
                    key = (C // d, d * h, d * s)
                    fib.setdefault(key, set()).add((C, d, s, h))
    worst = max(len(v) / len(divisors(k[2])) for k, v in fib.items())
    sq_ok = all(sqf(k[2]) for k in fib)
    inv_ok = all((t * d, d, f // d, k // d) == (C, d, s, h) for (t, k, f), v in fib.items() for (C, d, s, h) in v)
    big = max(len(v) for v in fib.values())
    rec('A5', f'fibre of (C,d\',s,h\') -> (t,k,f) has at most d(f) elements; f squarefree; reconstruction '
        f'(d\'|f, s=f/d\', C=td\', h\'=k/d\') is the inverse ({len(fib)} images)', worst <= 1 and sq_ok and inv_ok,
        f'max fibre/d(f) = {worst:.2f}, max fibre {big}')
    ctrl('A5', 'fibres are not singletons (the d(f) loss is needed)', big > 1, f'max fibre {big}')


# ================================================================================================
# A6. outer-mask containment
# ================================================================================================
def part_A6():
    rng = random.Random(11)
    bad = badc = 0
    for _ in range(200000):
        eta = rng.uniform(0, 0.05)
        tau = rng.uniform(0, 0.05)
        Dp, B, th, m = rng.uniform(-0.05, 3), rng.uniform(0, 2), rng.uniform(0, 2), rng.uniform(0, 5)
        th = min(th, B + 2 * eta)
        # actual exponents within the eta windows, with theta^ <= B^ (d' | C)
        Bh = B + rng.uniform(-eta, eta)
        thh = min(th + rng.uniform(-eta, eta), Bh)
        if abs(thh - th) > eta:
            continue
        c1 = Dp + rng.uniform(-eta, eta)
        c2 = Dp + rng.uniform(-eta, eta)
        L_ = c1 + c2 - 2 * Bh
        # largest h^ allowed by ratio <= Z^tau:  m + h^ - thh - L_ <= tau
        hh = tau - m + thh + L_
        dh = thh + hh
        P1 = B - th
        Minit = 2 * Dp - m - 2 * P1 + 6 * eta + tau
        bad += dh > Minit + 1e-12
        badc += dh > 2 * Dp - m - 2 * P1 + 5 * eta + tau + 1e-12
    rec('A6', 'ratio <= Z^tau implies log q_(d\'h\') <= M_init = 2D\'-m-2P_1+6eta+tau (200000 random actual '
        'exponents in the eta windows)', bad == 0, f'{bad} violations')
    ctrl('A6', '5 eta in place of 6 eta', badc > 0, f'{badc} violations')


if __name__ == '__main__':
    rng = random.Random(20261010)
    print(f'sep30_misc_checks.py  quick={QUICK}', flush=True)
    parts = [('A1', lambda: part_A1(rng)), ('A2', lambda: part_A2(rng)), ('A3', part_A3), ('A5', part_A5),
             ('A6', part_A6), ('A4', lambda: part_A4(rng))]
    extra = [a for a in sys.argv[1:] if a.startswith('--only=')]
    if extra:
        want = extra[0][7:].split(',')
        parts = [p for p in parts if p[0] in want]
    for name, fn in parts:
        fn()
        print(f'  [{name} done {time.time() - T0:.1f}s]', flush=True)
    npass = sum(r[2] for r in RESULTS)
    print(f'\n{npass}/{len(RESULTS)} checks passed in {time.time() - T0:.1f}s')
    OUT['results'] = [{'part': p, 'claim': c, 'pass': ok, 'detail': d} for p, c, ok, d in RESULTS]
    if '--out' in sys.argv:
        path = sys.argv[sys.argv.index('--out') + 1]
        with open(path, 'w') as fh:
            json.dump(OUT, fh, indent=1, default=str)
        print('wrote', path)
    sys.exit(0 if npass == len(RESULTS) else 1)
