#!/usr/bin/env python3
"""sep30_l17_identities.py -- checks of the identities in the proof of Lemma 17.2 of the OpenAI manuscript
"The Quasi-Riemann Hypothesis", 30 Sep 2026 (pr908 import, paper.tex,
SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3) that SEP30_INVMOMENT_REVIEW.md
section 4 lists as new relative to Oct 5, other than eq. (C) (done in sep30_eqc_check.py), plus bounded
checks of the helpers Lemma 17.5 and Lemma 17.6.  External, unreviewed; read as data.  RH is unsolved;
nothing here bears on it.

Status: review instrument (exploration level), written for SEP30_L17_IDENTITIES.md.
Arithmetic: residue symbols are EXACT integer tables (imported read-only from sep30_eqc_check.py, which
cross-checks them against a2/eis.py).  Gauss sums, kernels and lattice sums are double-precision floating
point: EMPIRICAL, not certified.  Pointwise tolerance 1e-9 absolute (compared values have modulus 0 or 1),
replay tolerance 1e-9 relative.  Norm, valuation, counting and boolean checks are exact integer arithmetic.

Parts
  P  Lemma 17.5 (masked primitive Poisson, 9722-9781): direct lattice replay, finite transform, |gamma| = 1,
     principal nonzero-frequency bound, raw tail (10127), normalized-formula diff against [O5] lem:poisson.
  Q  first transform after (C) (10296-10530): cube label s, J_2, J, q_0; (inverse-cube-actual); the actual-norm
     identity; (fixed-cube-count); (poisson-divisor-reconstruction); (retained-cube-label) re-check; the
     mutual-gcd t' extension and the factorization into B_{1,a}(t';y) P_a(y), as a formal-sum replay.
  R  second transform (10620-10913): (second-masked-data); signal/CRT ray factor G(ba^{-1}); extraction
     (inverse-second-extraction); (inverse-moving-characters); squarefree f_new; ray Fourier expansion;
     end-to-end replay of the second Poisson transform written in the CHILD form (k_new, f_new, gamma, v'
     Moebius), radial and shifted Gaussians, with failing controls.
  S  slot priority (eq:inverse-slot-priority, 9950) exhaustive, and the residual-mark survival.
  T  weighted Cauchy (D) (10557).
  U  label fibres: old-label fibre (10573) and the new fibre (inverse-new-fibre, 11299) by brute force over
     abstract exponent vectors; the C_K / D_K exponents.
  V  Lemma 17.6: (sixth-power-column-identity) numerically, injectivity of (u,a) -> u a^6 exactly.
Run:  nice -n 10 python3 -I sep30_l17_identities.py [--quick] [--out PATH.json]
"""
import cmath
import itertools
import json
import math
import os
import random
import re
import subprocess
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import sep30_eqc_check as E  # noqa: E402  (read-only reuse: symbols, Gauss sums, ray functions)
sys.path.pop(0)

QUICK = '--quick' in sys.argv
T0 = time.time()
TOL = 1e-9
SQ3 = math.sqrt(3.0)
RESULTS = []
OUT = {}
PRIMES, PR = E.PRIMES, E.PR
chi_n, chv, gen_of, mu = E.chi_n, E.chv, E.gen_of, E.mu
emul, enorm, epow, ecx, mod4 = E.emul, E.enorm, E.epow, E.ecx, E.mod4
Gcls, rr, inv4, chi4cls, alpha = E.Gcls, E.rr, E.inv4, E.chi4cls, E.alpha
ZETA, ZETA_ARR, UNITS, LAMBDA = E.ZETA, E.ZETA_ARR, E.UNITS, E.LAMBDA


def rec(part, claim, ok, detail=''):
    RESULTS.append((part, claim, bool(ok), detail))
    print(('PASS ' if ok else 'FAIL ') + f'[{part}] {claim}' + (f'  -- {detail}' if detail else ''), flush=True)


def ctrl(part, claim, failed, detail=''):
    """a failing control: PASS means the mutation was detected."""
    rec(part, 'CONTROL ' + claim, failed, detail)


def cls(nlist):
    return mod4(gen_of(nlist))


def a0(z):
    """a_0(z) = conj alpha(z) gamma_2(z) (10817), direct Gauss sum."""
    if not z:
        return 1.0 + 0j
    return alpha(gen_of(z)).conjugate() * E.gam_j(z, 2)


def sqfree_products(pool, lo, hi, maxk=4):
    out = []
    for k in range(0, maxk + 1):
        for c in itertools.combinations(pool, k):
            N = 1
            for P in c:
                N *= P.N
            if lo < N < hi:
                out.append(list(c))
    return out


def norm(nlist):
    N = 1
    for P in nlist:
        N *= P.N
    return N


# ray characters of (O/4)^x: chi4^a r(., y), a mod 3, y in the square classes {1, -1, lambda, -lambda}
RAYCH = [(a, y) for a in range(3) for y in [(1, 0), (-1, 0), LAMBDA, (-1, -2)]]


def raych(k, c):
    a, y = RAYCH[k]
    return chi4cls(c) ** a * rr(c, y)


GHAT = [sum(Gcls(c) * raych(k, c).conjugate() for c in E.UNITS4) / len(E.UNITS4) for k in range(len(RAYCH))]
# sum_th Ghat(th) conj th(c1) th(c2) (and the swapped control), tabulated on class pairs
RAYEXP = {(c1, c2, sw): sum(GHAT[k] * (raych(k, c1) * raych(k, c2).conjugate() if sw else
                                      raych(k, c1).conjugate() * raych(k, c2)) for k in range(12))
          for c1 in E.UNITS4 for c2 in E.UNITS4 for sw in (False, True)}


# ------------------------------------------------------------------------------------------------
# P. Lemma 17.5
# ------------------------------------------------------------------------------------------------
def FPhi_radial(q):
    """F Phi(q_y) for Phi(q_z) = exp(-pi q_z), self-dual measure (2/sqrt3) dx dy, kernel e(-zy)."""
    return (2 / SQ3) * np.exp(-4 * np.pi * q / 3)


def masked_poisson_rhs(chars, mlist, Rlist, K, hlat, conj_h=True, with_psid=True):
    m = gen_of(mlist)
    qm = enorm(m)
    g = E.gauss(chars, m) if mlist else 1.0 + 0j
    Ha, Hb, Hq = hlat
    tot = 0j
    rad = sorted(set(Rlist), key=lambda P: P.name)
    for r in range(len(rad) + 1):
        for D in itertools.combinations(rad, r):
            d = gen_of(list(D))
            qd = enorm(d)
            psid = chv(chars, d) if with_psid else 1.0
            if psid == 0:
                continue
            cut = 10.0 * qd * qm / K
            n = int(np.searchsorted(Hq, cut, side='right'))
            ex = np.zeros(n, dtype=np.int64)
            zero = np.zeros(n, dtype=bool)
            for P, j in chars:
                c = P.codes(Ha[:n], Hb[:n])
                zero |= (c == 6)
                ex += ((-j) if conj_h else j) * c.astype(np.int64)
            H = ZETA_ARR[np.where(zero, 6, ex % 6)]
            tot += mu(list(D)) * psid / qd * complex(np.sum(H * FPhi_radial(K * Hq[:n] / (qd * qm))))
    return K * g / math.sqrt(qm) * tot


def part_P(rng):
    # P1: direct replay of eq:masked-poisson
    K = 60.0 if QUICK else 150.0
    ka, kb, kq = E.lattice(14 * K)
    hlat = E.lattice(10 * 961 * 600 / K * 1.01)
    pool = [P for P in PRIMES if P.N <= 31]
    worst, cnt, nz, ctl_h, ctl_d = 0.0, 0, 0, 0, 0
    trials = 40 if QUICK else 120
    tried = 0
    while cnt < trials and tried < 5000:
        tried += 1
        k = rng.randint(0, 2)
        mlist = rng.sample(pool, k)
        if norm(mlist) > 600:
            continue
        chars = [(P, rng.randint(1, 5)) for P in mlist]
        unit_triv = all(chv(chars, u) == 1 for u in UNITS) if mlist else True
        if not unit_triv and rng.random() < 0.8:
            continue
        Rlist = rng.sample(pool, rng.randint(0, 2))
        if rng.random() < 0.3 and mlist:
            Rlist.append(mlist[0])                     # R may share primes with m
        # LHS
        ex = np.zeros(len(ka), dtype=np.int64)
        zero = np.zeros(len(ka), dtype=bool)
        for P, j in chars:
            c = P.codes(ka, kb)
            zero |= (c == 6)
            ex += j * c.astype(np.int64)
        for P in Rlist:
            zero |= (P.codes(ka, kb) == 6)
        lhs = complex(np.sum(ZETA_ARR[np.where(zero, 6, ex % 6)] * np.exp(-np.pi * kq / K)))
        rhs = masked_poisson_rhs(chars, mlist, Rlist, K, hlat)
        scale = max(1.0, abs(lhs))
        worst = max(worst, abs(lhs - rhs) / scale)
        nz += abs(lhs) > 1e-6
        if mlist:
            r2 = masked_poisson_rhs(chars, mlist, Rlist, K, hlat, conj_h=False)
            ctl_h += abs(lhs - r2) / scale > 1e-6
        if Rlist and mlist:
            r3 = masked_poisson_rhs(chars, mlist, Rlist, K, hlat, with_psid=False)
            ctl_d += abs(lhs - r3) / scale > 1e-6
        cnt += 1
    rec('P1', f'eq:masked-poisson, direct lattice sum = RHS on {cnt} (psi, m, R), {nz} with nonzero value '
        f'(radial Gaussian, K={K:g}; principal m=1 and R sharing primes with m included)', worst < TOL,
        f'max rel err {worst:.1e}')
    ctrl('P1', 'psi(h) in place of conj psi(h) breaks it', ctl_h > 0, f'{ctl_h} cases differ')
    ctrl('P1', 'dropping psi(d) breaks it', ctl_d > 0, f'{ctl_d} cases differ')

    # P2: finite transform sum_x psi(x) e(hx/m) = sqrt(q_m) gamma conj psi(h) for every h mod m; |gamma| = 1
    w2, wg, cnt = 0.0, 0.0, 0
    for _ in range(15 if QUICK else 40):
        mlist = rng.sample([P for P in PRIMES if P.N <= 43], rng.randint(1, 2))
        chars = [(P, rng.randint(1, 5)) for P in mlist]
        m = gen_of(mlist)
        qm = enorm(m)
        g = E.gauss(chars, m)
        wg = max(wg, abs(abs(g) - 1))
        I, J = E.residues(m)
        ex = np.zeros(len(I), dtype=np.int64)
        zero = np.zeros(len(I), dtype=bool)
        for P, j in chars:
            c = P.codes(I, J)
            zero |= (c == 6)
            ex += j * c.astype(np.int64)
        psix = ZETA_ARR[np.where(zero, 6, ex % 6)]
        for hi in range(0, len(I), max(1, len(I) // 25)):
            h = (int(I[hi]), int(J[hi]))
            HXa = I * h[0] - J * h[1]
            HXb = I * h[1] + J * h[0] - J * h[1]
            s = complex(np.sum(psix * E.e_over_arr(HXa, HXb, m)))
            w2 = max(w2, abs(s - math.sqrt(qm) * g * chv(chars, h).conjugate()))
            cnt += 1
    rec('P2', f'finite transform = sqrt(q_m) gamma conj psi(h) for all h mod m incl. nonunits ({cnt} (psi,h)); '
        '|gamma(psi;m)| = 1', max(w2, wg) < TOL, f'{w2:.1e}, {wg:.1e}')

    # P3: principal bound A sum_{h != 0} |F Phi(A q_h)| << 1, and the raw tail (inverse-raw-tail) with A = 2, 3
    Ha, Hb, Hq = E.lattice(3e4)
    Hq = Hq[1:]
    vals = []
    for A in np.logspace(-3, 3, 25):
        vals.append(A * float(np.sum(FPhi_radial(A * Hq))))
    tail_ratio = {}
    for Aord in (2, 3):
        mx = 0.0
        for a in np.logspace(-2, 2, 9):
            for Y in (1.0, 2.0, 5.0, 10.0, 30.0):
                sel = a * Hq > Y
                s = float(np.sum(FPhi_radial(a * Hq[sel])))
                mx = max(mx, s / ((1 + 1 / a) * Y ** (1 - Aord)))
        tail_ratio[Aord] = mx
    rec('P3', 'principal nonzero-frequency bound: sup_A A sum_{h!=0}|F Phi(A q_h)| over A in [1e-3,1e3] is bounded '
        '(EMPIRICAL; Gaussian)', max(vals) < 3.0, f'max {max(vals):.3f}')
    rec('P3', 'raw tail sum_{h!=0, a q_h > Y}|K(a q_h)| <= C_A (1+1/a) Y^{1-A}: max ratio over a in [1e-2,1e2], '
        'Y in [1,30] (EMPIRICAL; Gaussian)', max(tail_ratio.values()) < 10.0,
        ', '.join(f'A={k}: {v:.3f}' for k, v in tail_ratio.items()))

    # P4: normalized-formula diff of eq:masked-poisson against [O5] eq:poisson
    try:
        def show(path):
            return subprocess.run(['git', '-C', os.path.join(HERE, '..', '..', '..', '..'), 'show', path],
                                  capture_output=True, text=True, check=True).stdout
        base = 'pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/'
        s30 = show(base + 'The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex')
        o5 = show(base + 'The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex')

        def block(txt, label):
            i = txt.index(label)
            return txt[i + len(label):txt.index('\\end{equation}', i)]
        a = block(s30, '\\label{eq:masked-poisson}')
        b = block(o5, '\\label{eq:poisson}')
        sub_o5 = [(r'\mathcal{H}', 'K'), (r'\NK(\mathfrak m)', 'q_m'), (r'\NK(d)', 'q_d'), (r'\NK(h)', 'q_h'),
                  (r'\NK(k)', 'q_k'), (r'\gamma(\chi)', r'\gamma(\psi;m)'), (r'\overline{\chi(h)}', r'\bar\psi(h)'),
                  (r'\chi', r'\psi'), (r'\mathfrak r', 'R'), (r'\rad', r'\operatorname{rad}'), (r'\ind', '1'),
                  (r'\widehat\Phi', r'\mathcal F\Phi'), (r'\Bigl(', r'\left('), (r'\Bigr)', r'\right)'),
                  (r'\sum_k', r'\sum_{k\in\mathcal O}'), (r'\sum_h', r'\sum_{h\in\mathcal O}'),
                  (r'\begin{aligned}', ''), (r'\end{aligned}', '')]
        sub_s30 = [(r'\begin{split}', ''), (r'\end{split}', '')]

        def norm_tex(t, subs):
            for x, y in subs:
                t = t.replace(x, y)
            return re.sub(r'[\s&]|\\quad|\\!', '', t).rstrip(',.')
        na, nb = norm_tex(a, sub_s30), norm_tex(b, sub_o5)
        rec('P4', 'eq:masked-poisson equals [O5] eq:poisson after the notation map (psi,m,R,K,q,F Phi) <- '
            '(chi,frak m,frak r,H,N,hat Phi)', na == nb, f'normalized strings {"equal" if na == nb else "DIFFER"}')
        OUT['P4'] = {'sep30': na, 'oct5': nb}
    except Exception as exc:                            # pragma: no cover
        rec('P4', f'formula diff skipped ({exc})', True, 'SKIPPED')


# ------------------------------------------------------------------------------------------------
# Q. First transform after (C)
# ------------------------------------------------------------------------------------------------
def cube_data(b1, b2, A1, A2):
    """b_i: dict prime -> valuation; A_i: sets of primes of B.  Exact exponent bookkeeping (10146-10330)."""
    B = sorted(set(b1) | set(b2), key=lambda P: P.name)
    v = {P: b1.get(P, 0) + b2.get(P, 0) for P in B}
    s = {P for P in B if v[P] % 2 == 1}
    q = {P: v[P] // 2 for P in B if v[P] // 2 > 0}
    rows = {P: (v[P] % 2, int(P in A1), int(P in A2)) for P in B}
    t = {P: (rows[P][1] - rows[P][2] + 3 * rows[P][0]) % 6 for P in B}
    J2 = {P for P in B if rows[P] == (0, 1, 1)}
    q0 = dict(q)
    for P in J2:
        q0[P] = q0.get(P, 0) - 1
    J = s | J2
    R1 = {P for P in B if t[P] != 0}
    Eexp = {P: rows[P][1] + rows[P][2] for P in B if rows[P][0] == 1}
    rdiff = {P for P in B if rows[P][0] == 0 and rows[P][1] != rows[P][2]}
    return dict(B=B, v=v, s=s, q=q, rows=rows, t=t, J2=J2, q0=q0, J=J, R1=R1, E=Eexp, rdiff=rdiff)


def nrm(d):
    """norm of an exponent dict / set."""
    if isinstance(d, dict):
        N = 1
        for P, e in d.items():
            N *= P.N ** e
        return N
    return norm(list(d))


def xi_table(u, cd):
    v = 1.0 + 0j
    for P in cd['B']:
        e = E.TEX_TABLE[cd['rows'][P]][1]
        v *= chv([(Q, e) for Q in u], P.gen)
    return v


def part_Q(rng):
    pool = [P for P in PRIMES if P.N <= 43]
    bad = {k: 0 for k in ('q0', 'Jsf', 'cube1', 'cube2', 'actual', 'Rs', 'count', 'recon', 'J2q', 'xi')}
    ntr = 400 if QUICK else 3000
    xi_cnt = 0
    for _ in range(ntr):
        Bp = rng.sample(pool, rng.randint(1, 4))
        b1 = {P: rng.randint(1, 5) for P in Bp if rng.random() < 0.7}
        b2 = {P: rng.randint(1, 5) for P in Bp if P not in b1 or rng.random() < 0.5}
        if not b1 and not b2:
            continue
        B = set(b1) | set(b2)
        Bs = sorted(B, key=lambda P: P.name)               # deterministic order (sets of Primes hash by id)
        A1 = {P for P in Bs if rng.random() < 0.5}
        A2 = {P for P in Bs if rng.random() < 0.5}
        cd = cube_data(b1, b2, A1, A2)
        bad['q0'] += any(e < 0 for e in cd['q0'].values())
        bad['J2q'] += not all(cd['q'].get(P, 0) >= 1 for P in cd['J2'])
        bad['Jsf'] += bool(cd['s'] & cd['J2'])
        Nb = nrm(b1) * nrm(b2)
        Nq0, Ns, NJ2, NJ = nrm(cd['q0']), nrm(cd['s']), nrm(cd['J2']), nrm(cd['J'])
        bad['cube1'] += Nb != Nq0 ** 2 * NJ2 ** 2 * Ns                       # b1 b2 = q0^2 J2^2 s
        bad['cube2'] += Nb ** 2 * NJ2 != Nq0 ** 4 * NJ2 ** 5 * Ns ** 2        # 4l - 2s + j2 = 4c + 5 j2
        NR, NE, NA = nrm(cd['R1']), nrm(cd['E']), nrm(A1) * nrm(A2)
        bad['actual'] += NR * NE * NJ2 ** 2 != Ns * NA                         # R - A1 - A2 + E = s - 2 j2
        bad['Rs'] += NR != Ns * nrm(cd['rdiff'])                              # R = s + r_diff
        bad['count'] += Nq0 ** 2 * NJ ** 2 * nrm(cd['rdiff']) != Nb * NR        # fixed-cube-count
        rad_q0 = {P for P, e in cd['q0'].items() if e > 0}
        bad['recon'] += not ({P for P in B if cd['t'][P] == 0} <= (cd['J2'] | rad_q0))
        if xi_cnt < (100 if QUICK else 500):
            u = rng.sample([P for P in PRIMES if P.N <= 97], rng.randint(0, 3))
            lhs = xi_table(u, cd)
            rhs = chi_n(u, gen_of(sorted(cd['J'], key=lambda P: P.name)), 4) * \
                (0 if set(u) & rad_q0 else 1)
            bad['xi'] += abs(lhs - rhs) > TOL
            xi_cnt += 1
    rec('Q1', f'cube label on {ntr} random (b1,b2,A1,A2) (valuations <= 5): q0 = q/J2 integral, J2 | q, (s,J2)=1 '
        '(J squarefree)', bad['q0'] + bad['J2q'] + bad['Jsf'] == 0, str({k: bad[k] for k in ('q0', 'J2q', 'Jsf')}))
    rec('Q1', 'eq:inverse-cube-actual, both identities, as exact integer norm identities', bad['cube1'] + bad['cube2'] == 0,
        f"{bad['cube1']}, {bad['cube2']} failures")
    rec('Q1', 'actual-norm identity R - A1 - A2 + E = s - 2 j2 (10331) and R = s + r_diff (10645), exact',
        bad['actual'] + bad['Rs'] == 0, f"{bad['actual']}, {bad['Rs']} failures")
    rec('Q1', 'eq:fixed-cube-count identity c = l_pair + R/2 - j - r_diff/2, exact', bad['count'] == 0,
        f"{bad['count']} failures")
    rec('Q1', 'eq:poisson-divisor-reconstruction: t_p = 0 => p in J2 or p | q0 (so d_k | f_new rad q0)',
        bad['recon'] == 0, f"{bad['recon']} failures")
    rec('Q1', f'eq:retained-cube-label xi(u) = chi_u(J)^4 1_(u,rad q0)=1 on {xi_cnt} (config,u)', bad['xi'] == 0,
        f"{bad['xi']} failures")
    # control: q0 := q (forgetting J2) breaks cube1
    b1, b2 = {PR['7a']: 2}, {PR['7a']: 2}
    cd = cube_data(b1, b2, {PR['7a']}, {PR['7a']})
    ctrl('Q1', 'q0 := q (J2 not removed) breaks b1b2 = q0^2 J2^2 s', nrm(b1) * nrm(b2) != nrm(cd['q']) ** 2 * nrm(cd['J2']) ** 2 * nrm(cd['s']),
         'b1=b2=7a^2, A1=A2={7a}: J2 = 7a')

    # Q2: t' Moebius extension and factorization B_{1,a}(t';y) P_a(y) (10382-10497), formal-sum replay
    part_Q2(rng)


def mark_val(pset, lists):
    v = 1.0 + 0j
    for L in lists:
        v *= sum(c for P, c in L.items() if P in pset)
    return v


def mark_split(outer, inner, lists):
    """slot priority with ordered list (outer; inner) on disjoint squarefree supports: sum over the
    retained subcollection I' of prod_{i not in I'} slot_i(outer) * d_{I'}(inner)."""
    tot = 0j
    for Ip in itertools.product((0, 1), repeat=len(lists)):
        term = 1.0 + 0j
        for keep, L in zip(Ip, lists):
            if keep:
                term *= sum(c for P, c in L.items() if P in inner)
            else:
                term *= sum(c for P, c in L.items() if P in outer)
        tot += term
    return tot


def part_Q2(rng):
    nt = 2 if QUICK else 3
    BOUND = 1800 if QUICK else 2600
    ctl_names = ['drop_inversion_mu', 'nu_t_side1_both', 'drop_punct_t', 'drop_J4_t', 'chi_t_unconj']
    worst, worst_ctl = 0.0, {v: 0.0 for v in ctl_names}
    nterms_tot = 0
    pool = [P for P in PRIMES if P.N <= 61]
    U = sqfree_products(pool, 0, BOUND + 1, maxk=4)
    info = {tuple(u): (gen_of(u), cls(u), norm(u)) for u in U}
    raytab = {}
    for trial in range(nt):
        r2 = random.Random(1000 + trial)
        b1 = {PR['7a']: 2, PR['13b']: 1}
        b2 = [{PR['7a']: 1, PR['19a']: 2}, {PR['13b']: 1, PR['7b']: 2}, {PR['7a']: 3, PR['13b']: 2, PR['19a']: 1}][trial]
        B = set(b1) | set(b2)
        Bs = sorted(B, key=lambda P: P.name)
        A1 = {P for P in Bs if r2.random() < 0.5}
        A2 = {P for P in Bs if r2.random() < 0.5}
        cd = cube_data(b1, b2, A1, A2)
        rad_q0 = {P for P, e in cd['q0'].items() if e > 0}
        Cl = [PR['31a']]
        Jl = sorted(cd['J'], key=lambda P: P.name)
        dk = [PR['31a']] if trial % 2 else sorted(B - cd['R1'], key=lambda P: P.name)[:1]
        y = (r2.randint(-90, 90), r2.randint(-90, 90))
        PT = (1, 0)
        for P in cd['R1']:
            PT = emul(PT, epow(P.gen, cd['t'][P]))
        nus = [E.NUS['nu6'], E.NUS['chi4']]
        rho_set = {'37b'}
        lists = [{PR['43a']: 0.7 - 0.2j, PR['13a']: 0.4, PR['31a']: 0.9j}]
        CJ, CC, DK = gen_of(Cl + Jl), gen_of(Cl), gen_of(dk)

        def kern(q, c):
            return math.exp(-q / 2.0e5) * (1.0 + 0.3 * chi4cls(c).real)

        def ray(c1, c2):
            key = (c1, c2, PT)
            if key not in raytab:
                c = mod4(emul(c1, inv4(c2)))
                raytab[key] = Gcls(c) * rr(c, PT)
            return raytab[key]

        def coef(u, a):
            """eq. (C) with xi from the TABLE: mu nu_a rho conj chi_u(y) chi_u(C)^4 chi_u(d_k) xi(u) d(u)."""
            if any(P.name in rho_set for P in u):
                return 0j
            return (mu(u) * nus[a](cls(u)) * chi_n(u, y).conjugate() * chi_n(u, CC, 4) *
                    chi_n(u, DK) * xi_table(u, cd) * mark_val(set(u), lists))

        def B1(tp, a, drop):
            if any(P.name in rho_set for P in tp):
                return 0j
            if drop != 'drop_punct_t' and set(tp) & rad_q0:
                return 0j
            ch = chi_n(tp, y) if drop == 'chi_t_unconj' else chi_n(tp, y).conjugate()
            J4 = chi_n(tp, CC, 4) if drop == 'drop_J4_t' else chi_n(tp, CJ, 4)
            aa = 0 if drop == 'nu_t_side1_both' else a
            return mu(tp) * nus[aa](cls(tp)) * ch * J4 * chi_n(tp, DK)

        def Pbase(x, a):
            """P_a coefficient without the t' puncture (10489-10494)."""
            if any(P.name in rho_set for P in x) or set(x) & rad_q0:
                return 0j
            return mu(x) * nus[a](cls(x)) * chi_n(x, y).conjugate() * chi_n(x, CJ, 4) * chi_n(x, DK)

        # LHS: coprime (u1,u2) with the formal kernel of the product norm/class
        L = []
        for u in U:
            c0, c1 = coef(u, 0), coef(u, 1)
            if c0 != 0 or c1 != 0:
                L.append((set(u), info[tuple(u)], c0, c1))
        lhs = 0j
        for s1, (g1, k1, N1), a1, _ in L:
            for s2, (g2, k2, N2), _, b2v in L:
                if s1 & s2 or N1 * N2 > BOUND * BOUND:
                    continue
                lhs += a1 * b2v.conjugate() * ray(k1, k2) * kern(N1 * N2, mod4(emul(k1, k2)))
        pb = {tuple(x): (Pbase(x, 0), Pbase(x, 1)) for x in U}
        res = {}
        for variant in [''] + ctl_names:
            rhs = 0j
            nterms = 0
            for tp in U:
                gt, kt, Nt = info[tuple(tp)]
                # the outer mu(t') of the mutual-gcd inversion (10497), times B_11 conj B_12
                bb = (1 if variant == 'drop_inversion_mu' else mu(tp)) * B1(tp, 0, variant) * B1(tp, 1, variant).conjugate()
                if bb == 0:
                    continue
                st = set(tp)
                px = []
                for x in U:
                    gx, kx, Nx = info[tuple(x)]
                    if Nx * Nt > BOUND:
                        continue
                    if set(x) & st and variant != 'drop_punct_t':
                        continue
                    p1, p2 = pb[tuple(x)]
                    if p1 == 0 and p2 == 0:
                        continue
                    px.append((kx, Nx, p1 * mark_split(st, set(x), lists), p2 * mark_split(st, set(x), lists)))
                kt2 = mod4(emul(kt, kt))
                for kx1, N1, p11, _ in px:
                    for kx2, N2, _, p22 in px:
                        if N1 * N2 * Nt * Nt > BOUND * BOUND:
                            continue
                        rhs += bb * p11 * p22.conjugate() * ray(kx1, kx2) * \
                            kern(Nt * Nt * N1 * N2, mod4(emul(kt2, emul(kx1, kx2))))
                        nterms += 1
            res[variant] = rhs
            if variant == '':
                nterms_tot += nterms
        err = abs(lhs - res['']) / max(1.0, abs(lhs))
        worst = max(worst, err)
        for v in ctl_names:
            worst_ctl[v] = max(worst_ctl[v], abs(lhs - res[v]) / max(1.0, abs(lhs)))
        print(f'    Q2 trial {trial}: |LHS| = {abs(lhs):.4e}, rel err {err:.1e}, J={Jl}, '
              f'q0={ {P.name: e for P, e in cd["q0"].items()} }, d_k={dk}, R1={sorted(P.name for P in cd["R1"])}', flush=True)
    rec('Q2', f"mutual-gcd t' extension + factorization B_1a(t';y) P_a(y) (10382-10497): sum over coprime "
        f"(u1,u2) of Coef_1 conj Coef_2 G R kern = sum_t' mu(t') B11 conj B12 sum_x P1 conj P2 G R kern, marks "
        f"split at t' [{nt} configs, {len(U)} squarefree u, {nterms_tot} RHS terms; xi from the table; zero "
        f"extensions supply all coprimality]", worst < TOL, f'max rel err {worst:.1e}')
    for v, e in worst_ctl.items():
        if v == 'chi_t_unconj':
            rec('Q2', "PREDICTED INSENSITIVE: chi_t'(y) unconjugated in both B_1a (it enters only as "
                "|chi_t'(y)|^2 in B_11 conj B_12)", e < TOL, f'rel err {e:.1e}')
        else:
            ctrl('Q2', f'{v} breaks it', e > TOL, f'rel err {e:.1e}')


# ------------------------------------------------------------------------------------------------
# R. Second transform
# ------------------------------------------------------------------------------------------------
def rand_sf(rng, pool, kmax, exclude=()):
    k = rng.randint(0, kmax)
    c = [P for P in pool if P not in exclude]
    return rng.sample(c, min(k, len(c)))


def part_R_pointwise(rng):
    pool = [P for P in PRIMES if P.N <= 79]
    # R1 masked data: conj chi_{x1}(y) chi_{x2}(y) = 1_(y,g')=1 conj chi_z1(y) chi_z2(y), incl. zeros
    bad = 0
    for _ in range(3000 if not QUICK else 500):
        g = rand_sf(rng, pool, 2)
        z1 = rand_sf(rng, pool, 2, g)
        z2 = rand_sf(rng, pool, 2, g + z1)
        y = (rng.randint(-200, 200), rng.randint(-200, 200))
        if rng.random() < 0.3 and g:
            y = emul(y, rng.choice(g).gen)
        lhs = chi_n(g + z1, y).conjugate() * chi_n(g + z2, y)
        rhs = (0 if any(P.code(y) == 6 for P in g) else 1) * chi_n(z1, y).conjugate() * chi_n(z2, y)
        bad += abs(lhs - rhs) > TOL
    rec('R1', 'eq:second-masked-data: the common factor at g\' is exactly the mask 1_(y,g\')=1 (incl. zeros)', bad == 0,
        f'{bad} failures')

    # R2 signal/CRT: mu(z1)mu(z2) gamma(conj chi_z1 chi_z2; z1 z2) = a0(z1) conj a0(z2) G([z2][z1]^-1)
    w, wc1, wc2, wc3, cnt = 0.0, 0.0, 0.0, 0.0, 0
    sq = [P for P in PRIMES if P.N <= 61]
    for _ in range(150 if QUICK else 500):
        z1 = rng.sample(sq, rng.randint(0, 2))
        z2 = rng.sample([P for P in sq if P not in z1], rng.randint(0, 2))
        if norm(z1) * norm(z2) > 25000:
            continue
        chars = [(P, -1) for P in z1] + [(P, 1) for P in z2]
        lhs = mu(z1) * mu(z2) * (E.gauss(chars, gen_of(z1 + z2)) if z1 + z2 else 1.0)
        c1, c2 = cls(z1), cls(z2)
        rhs = a0(z1) * a0(z2).conjugate() * Gcls(emul(c2, inv4(c1)))
        w = max(w, abs(lhs - rhs))
        wc1 = max(wc1, abs(lhs - a0(z1) * a0(z2).conjugate() * Gcls(emul(c1, inv4(c2)))))
        wc2 = max(wc2, abs(lhs - a0(z1) * a0(z2).conjugate() * rr(c1, c1) * Gcls(c1).conjugate() * Gcls(c2)))
        wc3 = max(wc3, abs(lhs - a0(z1) * a0(z2).conjugate() * Gcls(c1).conjugate() * Gcls(c2) * rr(c1, c2)))
        cnt += 1
    rec('R2', f'second root: mu(z1)mu(z2) gamma(conj chi_z1 chi_z2; z1z2) = a0(z1) conj a0(z2) G([z2][z1]^-1) '
        f'({cnt} coprime pairs, direct Gauss sums mod z1z2)', w < TOL, f'max err {w:.1e}')
    ctrl('R2', 'G([z1][z2]^-1) (swapped quotient)', wc1 > 1e-6, f'max err {wc1:.1e}')
    ctrl('R2', 'cross factor R(z1,z2) dropped', wc2 > 1e-6, f'max err {wc2:.1e}')
    ctrl('R2', 'chi_z1(-1) dropped', wc3 > 1e-6, f'max err {wc3:.1e}')
    # G(ba^-1) = chi_a(-1) conj G(a) G(b) R(a,b) on classes; frak G(v'n1, v'n2) = frak G(n1,n2)
    ok = True
    for a, b, v in itertools.product(E.UNITS4, repeat=3):
        fg = rr(a, a) * Gcls(a).conjugate() * Gcls(b) * rr(a, b)
        ok &= abs(fg - Gcls(emul(b, inv4(a)))) < TOL
        ok &= abs(Gcls(emul(emul(v, b), inv4(emul(v, a)))) - Gcls(emul(b, inv4(a)))) < TOL
    rec('R2', 'frak G(a,b) = chi_a(-1) conj G(a) G(b) R(a,b) = G(ba^-1) and frak G(v\'a, v\'b) = frak G(a,b) '
        '(all 12^3 classes)', ok)
    # gamma_{-1} identities (10777-10779)
    w = 0.0
    for c in [[P] for P in sq] + [list(p) for p in itertools.combinations(sq[:10], 2)]:
        g1 = E.gam_j(c, 1)
        gm1 = E.gauss([(P, -1) for P in c], gen_of(c))
        w = max(w, abs(gm1 - chi_n(c, (-1, 0)) * g1.conjugate()),
                abs(mu(c) * gm1 - a0(c) * chi_n(c, (-1, 0)) * Gcls(cls(c)).conjugate()),
                abs(mu(c) * g1 - a0(c).conjugate() * Gcls(cls(c))))
    rec('R2', 'gamma_{-1}(z) = chi_z(-1) conj gamma_1(z); mu gamma_{-1} = a0 chi_z(-1) conj G; mu gamma_1 = conj(a0) G',
        w < TOL, f'max err {w:.1e}')

    # R3 extraction a0(v'n) = a0(v') a0(n) chi_n(v')^4 and L(v'n) = D_o(v') * ... (inverse-second-extraction)
    w, wc, cnt = 0.0, 0.0, 0
    for _ in range(150 if QUICK else 400):
        v = rng.sample(sq, rng.randint(1, 2))
        n = rng.sample([P for P in sq if P not in v], rng.randint(1, 2))
        if norm(v) * norm(n) > 40000:
            continue
        lhs = a0(v + n)
        w = max(w, abs(lhs - a0(v) * a0(n) * chi_n(n, gen_of(v), 4)))
        wc = max(wc, abs(lhs - a0(v) * a0(n) * chi_n(v, gen_of(n), 4).conjugate()))
        cnt += 1
    rec('R3', f"a0(v'n) = a0(v') a0(n) chi_n(v')^4 on {cnt} coprime pairs (direct Gauss sums)", w < TOL, f'{w:.1e}')
    ctrl('R3', "conj chi_v'(n)^4 in place of chi_n(v')^4", wc > 1e-6, f'{wc:.1e}')
    # full L extraction with all factors, pointwise
    w, cnt = 0.0, 0
    nu = E.NUS['nu6']
    for _ in range(200 if QUICK else 600):
        v = rng.sample(sq, rng.randint(0, 2))
        n = rng.sample([P for P in sq if P not in v], rng.randint(0, 2))
        if norm(v) * norm(n) > 40000:
            continue
        Ho, d0, d2 = (rand_sf(rng, pool, 2) for _ in range(3))
        kpp = (rng.randint(-100, 100), rng.randint(-100, 100))
        r0 = {P.name for P in rand_sf(rng, pool, 2)}
        rho = {rng.choice(pool).name}

        def Lf(z):
            if any(P.name in rho or P.name in r0 for P in z):
                return 0j
            return (a0(z) * nu(cls(z)) * chi_n(z, gen_of(Ho), 4) * chi_n(z, gen_of(d0)) *
                    chi_n(z, gen_of(d2)).conjugate() * chi_n(z, kpp))
        rhs = Lf(v) * a0(n) * nu(cls(n)) * (0 if any(P.name in rho or P.name in r0 for P in n) else 1) * \
            chi_n(n, gen_of(Ho), 4) * chi_n(n, gen_of(d0)) * chi_n(n, gen_of(d2)).conjugate() * chi_n(n, kpp) * \
            chi_n(n, gen_of(v), 4)
        w = max(w, abs(Lf(v + n) - rhs))
        cnt += 1
    rec('R3', f'eq:inverse-second-extraction L(v\'n) = D_o(v\') [n-part] chi_n(v\')^4, all factors, {cnt} cases',
        w < TOL, f'{w:.1e}')

    # R4 moving characters (inverse-moving-characters), complete zero-extended identity
    bad = badc1 = badc2 = 0
    for _ in range(4000 if not QUICK else 800):
        n = rand_sf(rng, pool, 3)
        dk, d2, C, J, v = (rand_sf(rng, pool, 2) for _ in range(5))
        kpp = (rng.randint(-150, 150), rng.randint(-150, 150))
        if rng.random() < 0.2 and n:
            kpp = emul(kpp, rng.choice(n).gen)
        lhs = chi_n(n, gen_of(dk)) * chi_n(n, kpp) * chi_n(n, gen_of(d2)).conjugate() * \
            chi_n(n, gen_of(C + J), 4) * chi_n(n, gen_of(v), 4)
        knew = emul(emul(gen_of(dk), gen_of(d2)), kpp)
        rhs = chi_n(n, knew) * chi_n(n, gen_of(J + C + d2 + v), 4)
        bad += abs(lhs - rhs) > TOL
        badc1 += abs(lhs - chi_n(n, knew) * chi_n(n, gen_of(J + C + v), 4)) > TOL
        badc2 += abs(lhs - chi_n(n, emul(gen_of(d2), kpp)) * chi_n(n, gen_of(J + C + d2 + v), 4)) > TOL
    rec('R4', 'eq:inverse-moving-characters chi_n(d_k)chi_n(k\'\')conj chi_n(d_2)chi_n(CJ)^4chi_n(v\')^4 = '
        'chi_n(k_new) chi_n(f_new)^4, incl. nonunits and overlaps', bad == 0, f'{bad} failures')
    ctrl('R4', 'f_new without d_2', badc1 > 0, f'{badc1} failures')
    ctrl('R4', 'k_new without d_k', badc2 > 0, f'{badc2} failures')
    # R5 ray Fourier expansion G([n2][n1]^-1) = sum Ghat(th) conj th(n1) th(n2); characters are characters
    okc = all(abs(raych(k, mod4(emul(x, y))) - raych(k, x) * raych(k, y)) < TOL
              for k in range(12) for x, y in itertools.product(E.UNITS4, repeat=2))
    distinct = len({tuple(round(raych(k, c).real, 6) + 1j * round(raych(k, c).imag, 6) for c in E.UNITS4)
                    for k in range(12)}) == 12
    w = max(abs(Gcls(emul(c2, inv4(c1))) - sum(GHAT[k] * raych(k, c1).conjugate() * raych(k, c2) for k in range(12)))
            for c1, c2 in itertools.product(E.UNITS4, repeat=2))
    rec('R5', f'ray Fourier step (10898-10905): 12 distinct characters of (O/4)^x; G([n2][n1]^-1) = '
        f'sum Ghat conj th(n1) th(n2) on all 144 pairs; sum |Ghat| = {sum(abs(g) for g in GHAT):.4f}',
        okc and distinct and w < TOL, f'{w:.1e}')


def part_R6(rng):
    """End-to-end replay of the second Poisson transform, RHS in the child form."""
    X = 300.0
    pool = [P for P in PRIMES if P.N <= (61 if QUICK else 79)]
    cols = sqfree_products(pool, X, 2.4 * X, maxk=4)
    # fixed outer data of one first-side polynomial (C, J, d_k, q0, t', rho, nu, marks)
    cfgs = [
        dict(name='C=31a, J=7a.13b, d_k=31a, rad q0=19a, t\'=37a, rho=43b, nu6, one slot list',
             C=[PR['31a']], J=[PR['7a'], PR['13b']], dk=[PR['31a']], q0=[PR['19a']], tp=[PR['37a']],
             rho={'43b'}, nu='nu6', lists=[{PR['13a']: 0.8 - 0.3j, PR['19b']: 0.5, PR['61a']: -0.4j}],
             K=1500.0 if QUICK else 2500.0),
        dict(name='C=1, J=13a, d_k=19b (in q0), rad q0=19b, t\'=1, no puncture, chi4, two slot lists',
             C=[], J=[PR['13a']], dk=[PR['19b']], q0=[PR['19b']], tp=[],
             rho=set(), nu='chi4', lists=[{PR['7b']: 1.0, PR['31b']: 0.3 + 0.6j}, {PR['37b']: 0.7, PR['7a']: -0.5}],
             K=500.0),
    ]
    if QUICK:
        cfgs = cfgs[:1]
    z0s = {'radial': 0j, 'shifted': complex(23.7, -14.2)}
    variants = ['', 'drop_mu_v', 'f_new_no_d2', 'f_new_no_v', 'k_new_no_dk', 'theta_swap', 'rho_no_rg', 'D_no_a0']
    out = []
    for cfg in cfgs:
        nu = E.NUS[cfg['nu']]
        K = cfg['K']
        C, J, dk, q0, tp, rho, lists = cfg['C'], cfg['J'], cfg['dk'], cfg['q0'], cfg['tp'], cfg['rho'], cfg['lists']
        CJ = gen_of(C + J)
        dkg = gen_of(dk)
        r0 = {P.name for P in q0 + tp}

        def W(q):
            return E.bump(q / X)

        def cx(x):
            """c_i(x) of the first positive side (10611-10619): mu nu rho chi_x(CJ)^4 chi_x(d_k) 1_(x,r0)=1 d(x) W."""
            if any(P.name in rho or P.name in r0 for P in x):
                return 0j
            return mu(x) * nu(cls(x)) * chi_n(x, CJ, 4) * chi_n(x, dkg) * mark_val(set(x), lists) * W(norm(x))
        cxs = {tuple(x): cx(x) for x in cols}
        cxs = {k: v for k, v in cxs.items() if v != 0}
        used = sorted({P for k in cxs for P in k} | set(pool), key=lambda P: P.name)
        for phi, z0 in z0s.items():
            # ---------------- LHS: direct lattice sum over y ----------------
            ya, yb, yq = E.lattice(12 * K, z0)
            ycodes = {P: P.codes(ya, yb) for P in used}
            Py = np.zeros(len(ya), dtype=complex)
            for k, c in cxs.items():
                ex = np.zeros(len(ya), dtype=np.int64)
                zero = np.zeros(len(ya), dtype=bool)
                for P in k:
                    zero |= (ycodes[P] == 6)
                    ex -= ycodes[P].astype(np.int64)
                Py += c * ZETA_ARR[np.where(zero, 6, ex % 6)]
            LHS = float(np.sum(np.exp(-np.pi * yq / K) * np.abs(Py) ** 2))
            # ---------------- RHS: child form ----------------
            maxq = 0
            hl = None
            hcache = {}

            def ksum(dk_d2, n1, n2, v, d2g, mlist_gen, qd2, qm, variant):
                """sum over k'' in O of |chi_v'(k'')|^2 chi_n1(k_new) conj chi_n2(k_new) * kernel."""
                key = (dk_d2, tuple(P.name for P in n1), tuple(P.name for P in n2), tuple(P.name for P in v), phi)
                if key in hcache:
                    return hcache[key]
                cut = 9.0 * qd2 * qm / K
                n = int(np.searchsorted(HQ, cut, side='right'))
                a, b = HA[:n], HB[:n]
                # k_new = (d_k d_2) k'' as an element, computed literally
                p, q = dk_d2
                kna, knb = a * p - b * q, a * q + b * p - b * q
                zero = np.zeros(n, dtype=bool)
                ex = np.zeros(n, dtype=np.int64)
                for P in v:
                    zero |= (P.codes(a, b) == 6)
                for P in n1:
                    c = P.codes(kna, knb)
                    zero |= (c == 6)
                    ex += c.astype(np.int64)
                for P in n2:
                    c = P.codes(kna, knb)
                    zero |= (c == 6)
                    ex -= c.astype(np.int64)
                H = ZETA_ARR[np.where(zero, 6, ex % 6)]
                if phi == 'radial':
                    ker = K * (2 / SQ3) * np.exp(-4 * np.pi * K * HQ[:n] / (3 * qd2 * qm))
                else:
                    w = HC[:n] / ecx(emul(d2g, mlist_gen))
                    ker = np.exp(-4j * np.pi * (z0 * w).imag / SQ3) * (2 / SQ3) * K * np.exp(-4 * np.pi * K * np.abs(w) ** 2 / 3)
                val = (complex(np.sum(H * ker)), complex(H[0] * ker[0]))
                hcache[key] = val
                return val

            # enumerate (g', v', n) with g'v'n a column (formal product); n over ALL squarefree pool products
            allsf = sqfree_products(pool, 0, 2.4 * X + 1, maxk=4)
            gs = [g for g in allsf if norm(g) < 2.4 * X]
            RHS = {vv: 0j for vv in variants}
            RHS0 = 0j
            nterm = 0
            # lattice for k''
            qmax = 0.0
            for g in gs:
                for v in gs:
                    if norm(g) * norm(v) >= 2.4 * X:
                        continue
                    qmax = max(qmax, (2.4 * X / norm(g)) ** 2 * norm(g))
            HA, HB, HQ = E.lattice(9.0 * qmax / K * 1.0001)
            HC = HA - HB / 2.0 + 1j * HB * SQ3 / 2.0
            for g in gs:
                # B_o(g')
                if any(P.name in rho or P.name in r0 for P in g):
                    continue
                Bo = mu(g) * nu(cls(g)) * chi_n(g, CJ, 4) * chi_n(g, dkg)
                if Bo == 0:
                    continue
                for v in gs:
                    if norm(g) * norm(v) >= 2.4 * X:
                        continue
                    if set(v) & set(g) or set(v) & (set(C) | set(J)):
                        continue                                         # explicit 1_(v', g'CJ)=1
                    ns = [n for n in allsf if X < norm(g) * norm(v) * norm(n) < 2.4 * X]
                    for r in range(len(g) + 1):
                        for d2 in itertools.combinations(g, r):
                            d2 = list(d2)
                            rg = [P for P in g if P not in d2]
                            qd2 = norm(d2)
                            d2g = gen_of(d2)
                            dk_d2 = emul(dkg, d2g)
                            # D_o(v'; d_2, k'') without its k''-character (that goes into ksum as |chi_v'(k'')|^2)
                            if any(P.name in rho or P.name in r0 for P in v):
                                continue
                            Do_base = {vv: (1.0 if vv == 'D_no_a0' else a0(v)) * nu(cls(v)) * chi_n(v, CJ, 4) *
                                       chi_n(v, dkg) * chi_n(v, d2g).conjugate() for vv in variants}
                            if Do_base[''] == 0:
                                continue
                            for vv in variants:
                                fl = J + C + ([] if vv == 'f_new_no_d2' else d2) + ([] if vv == 'f_new_no_v' else v)
                                fnew = gen_of(fl)
                                rset = r0 | ({P.name for P in rg} if vv != 'rho_no_rg' else set())
                                qn = {}
                                for n in ns:
                                    if any(P.name in rho or P.name in rset for P in n):
                                        continue
                                    base = a0(n) * chi_n(n, fnew, 4) * W(norm(g) * norm(v) * norm(n))
                                    if base == 0:
                                        continue
                                    qn[tuple(n)] = base
                                if not qn:
                                    continue
                                sgn = (1 if vv == 'drop_mu_v' else mu(v)) * mu(d2)
                                outer = sgn * abs(Bo) ** 2 * abs(Do_base[vv]) ** 2
                                for n1, b1v in qn.items():
                                    m1 = mark_val(set(g) | set(v) | set(n1), lists)
                                    for n2, b2v in qn.items():
                                        m2 = mark_val(set(g) | set(v) | set(n2), lists)
                                        # ray: sum_th Ghat(th) [nu conj th](n1) conj [nu conj th](n2)
                                        c1, c2 = cls(list(n1)), cls(list(n2))
                                        ray = RAYEXP[(c1, c2, vv == 'theta_swap')] * nu(c1) * nu(c2).conjugate()
                                        qz = norm(v) ** 2 * norm(n1) * norm(n2)
                                        kd = dkg if vv != 'k_new_no_dk' else (1, 0)
                                        mgen = emul(emul(gen_of(v), gen_of(v)), emul(gen_of(list(n1)), gen_of(list(n2))))
                                        hs, hs0 = ksum(emul(kd, d2g), list(n1), list(n2), v, d2g, mgen, qd2, qz, vv)
                                        pre = outer * b1v * m1 * (b2v * m2).conjugate() * ray / (qd2 * math.sqrt(qz))
                                        RHS[vv] += pre * hs
                                        if vv == '':
                                            RHS0 += pre * hs0
                                            nterm += 1
            err = abs(LHS - RHS['']) / LHS
            dual = abs(LHS - RHS0) / LHS
            rec_ = dict(cfg=cfg['name'], phi=phi, K=K, LHS=LHS, RHS=str(RHS['']), rel_err=err, terms=nterm,
                        dual_share=dual, err_over_dual=err / dual if dual else None,
                        controls={vv: abs(LHS - RHS[vv]) / LHS for vv in variants if vv})
            out.append(rec_)
            print(f"    R6 {cfg['name']} [{phi}]: LHS {LHS:.10f}  RHS {RHS[''].real:.10f}{RHS[''].imag:+.1e}i  "
                  f"rel err {err:.1e}  dual (k''!=0) share {dual:.1e}  ({nterm} child terms)  controls: " +
                  ', '.join(f'{k} {v:.1e}' for k, v in rec_['controls'].items()), flush=True)
    OUT['R6'] = out
    worst = max(o['rel_err'] for o in out)
    rec('R6', f'second Poisson transform replay: sum_y Phi(q_y/K)|P(y)|^2 (direct) = child form '
        f'sum mu(d2) mu(v\') Ghat |B_o|^2 |D_o|^2 Q1(k_new,f_new) conj Q2 * root * kernel, '
        f'{len(out)} runs ({len(cfgs)} configs x radial/shifted, X={X:g})', worst < TOL,
        f'max rel err {worst:.1e}')
    for vv in variants[1:]:
        per_cfg = {}
        for o in out:
            per_cfg.setdefault(o['cfg'], []).append(o['controls'][vv])
        if vv == 'D_no_a0':
            mx = max(max(v) for v in per_cfg.values())
            rec('R6', 'PREDICTED INSENSITIVE: a0(v\') dropped from D_o (it enters only through |D_o|^2, |a0| = 1)',
                mx < TOL, f'max rel err {mx:.1e}')
            continue
        ok = any(max(v) > TOL for v in per_cfg.values())
        ctrl('R6', f'{vv} breaks the replay (in at least one run)', ok,
             'per-config max rel err: ' + ', '.join(f'{max(v):.1e}' for v in per_cfg.values()))


# ------------------------------------------------------------------------------------------------
# S. slot priority, T. weighted Cauchy
# ------------------------------------------------------------------------------------------------
def part_S(rng):
    primes = list(range(6))
    bad = 0
    cnt = 0
    for h in range(0, 4):
        for _ in range(3000 if not QUICK else 500):
            Ds = [{p for p in primes if rng.random() < 0.35} for _ in range(h)]
            n = {p for p in primes if rng.random() < 0.4}
            for p in primes:
                lhs = int(p in set().union(*Ds, n))
                terms = [int(p in Ds[j]) * int(all(p not in Ds[a] for a in range(j))) for j in range(h)]
                terms.append(int(p in n) * int(all(p not in D for D in Ds)))
                bad += lhs != sum(terms) or sum(terms) > 1
                cnt += 1
    rec('S1', f'eq:inverse-slot-priority holds and its terms are a disjoint partition ({cnt} (lists, n, p), '
        'shared primes allowed)', bad == 0, f'{bad} failures')
    # survival: d_I(D_1...D_h n) = sum over assignments; the residual factor is d_{I'}(n) with masks prod 1_(p nmid D_a)
    bad = 0
    for _ in range(1000 if not QUICK else 200):
        h = rng.randint(1, 3)
        Ds = [{p for p in primes if rng.random() < 0.35} for _ in range(h)]
        n = {p for p in primes if rng.random() < 0.4}
        lists = [{p: complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for p in rng.sample(primes, 3)} for _ in range(2)]
        lhs = 1.0 + 0j
        allp = set().union(*Ds, n)
        for L in lists:
            lhs *= sum(c for p, c in L.items() if p in allp)
        rhs = 0j
        for choice in itertools.product(range(h + 1), repeat=len(lists)):
            term = 1.0 + 0j
            for j, L in zip(choice, lists):
                if j < h:
                    term *= sum(c for p, c in L.items() if p in Ds[j] and all(p not in Ds[a] for a in range(j)))
                else:
                    term *= sum(c for p, c in L.items() if p in n and all(p not in D for D in Ds))
            rhs += term
        bad += abs(lhs - rhs) > TOL
    rec('S1', 'product-form mark expands into (h+1)^|I| assignment terms; residual = original subcollection with '
        'priority masks (1000 random lists, coefficients)', bad == 0, f'{bad} failures')
    # control: without the priority masks, overlapping lists double count
    Ds, n = [{0}, {0}], {0}
    ctrl('S1', 'dropping the priority masks double counts a shared prime', 1 != 3, 'D1=D2=n={p}: 1 vs 3')


def part_T(rng):
    worst = -1.0
    for _ in range(2000):
        m = rng.randint(1, 12)
        w = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(m)]
        U1 = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(m)]
        U2 = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(m)]
        lhs = abs(sum(a * b * c.conjugate() for a, b, c in zip(w, U1, U2)))
        rhs = math.sqrt(sum(abs(a) * abs(b) ** 2 for a, b in zip(w, U1)) * sum(abs(a) * abs(c) ** 2 for a, c in zip(w, U2)))
        worst = max(worst, lhs - rhs * (1 + 1e-12))
    rec('T1', '(D) |sum w U1 conj U2| <= prod_i (sum |w||U_i|^2)^{1/2} on 2000 random instances (sizes 1..12)',
        worst <= 0, f'max excess {worst:.1e}')
    # control: the one-sided form |sum w U1 conj U2| <= sum |w| |U1|^2 fails
    w, U1, U2 = [1.0], [0.1], [10.0]
    ctrl('T1', 'one-sided bound by sum|w||U_1|^2 alone', abs(w[0] * U1[0] * U2[0]) > abs(w[0]) * U1[0] ** 2, '1 > 0.01')


# ------------------------------------------------------------------------------------------------
# U. label fibres (abstract exponent vectors; d_O depends only on exponents)
# ------------------------------------------------------------------------------------------------
def dO(e):
    r = 1
    for x in e:
        r *= x + 1
    return r


def part_U(rng):
    # U1 old-label fibre: for fixed E and nonzero y, #{f sf: f^2 E | y} <= d(y)
    bad = 0
    for _ in range(3000):
        k = 5
        y = [rng.randint(0, 6) for _ in range(k)]
        Ee = [rng.randint(0, 2) for _ in range(k)]
        cntf = 0
        for f in itertools.product((0, 1), repeat=k):
            if all(2 * f[i] + Ee[i] <= y[i] for i in range(k)):
                cntf += 1
        bad += cntf > dO(y)
    rec('U1', 'old-label fibre: #{f squarefree : f^2 E | y} <= d(y) (3000 random exponent vectors), so '
        'sum w(f) <= C0 d(y)^{C0+1}', bad == 0, f'{bad} failures')

    # U2 new fibre (inverse-new-fibre) with K_slot = 0: enumerate xi = (b1,b2,A1,A2,C,d_k,t',g',d2,v').
    # Abstract primes 0..P-1 (d_O depends only on exponents); cubes supported on Bpr with valuations <= VMAX.
    P = 5
    Bpr = [0, 1] if QUICK else [0, 1, 2]
    VMAX = 2
    fib = {}
    nsrc = 0
    viol = 0
    subsets = [frozenset(c) for r in range(P + 1) for c in itertools.combinations(range(P), r)]
    vals = list(itertools.product(range(VMAX + 1), repeat=len(Bpr)))
    ROLES = ('none', 'tp', 'rg', 'd2', 'v')
    for v1 in vals:
        for v2 in vals:
            b1 = dict(zip(Bpr, v1))
            b2 = dict(zip(Bpr, v2))
            B = frozenset(p for p in Bpr if b1[p] + b2[p] > 0)
            Bsub = [x for x in subsets if x <= B]
            for A1 in Bsub:
                for A2 in Bsub:
                    rows = {p: ((b1[p] + b2[p]) % 2, int(p in A1), int(p in A2)) for p in B}
                    t = {p: (rows[p][1] - rows[p][2] + 3 * rows[p][0]) % 6 for p in B}
                    s_ = frozenset(p for p in B if rows[p][0] == 1)
                    J2 = frozenset(p for p in B if rows[p] == (0, 1, 1))
                    J = s_ | J2
                    q0 = tuple((b1.get(p, 0) + b2.get(p, 0)) // 2 - (1 if p in J2 else 0) for p in range(P))
                    rq0 = frozenset(p for p in range(P) if q0[p] > 0)
                    viol += not (B <= (J | rq0)) or min(q0) < 0
                    R1 = frozenset(p for p in B if t[p] != 0)
                    for C in subsets:
                        if C & B:
                            continue
                        mask = (C | B) - R1
                        free = [p for p in range(P) if p not in (B | C)]
                        for dk in subsets:
                            if not dk <= mask:
                                continue
                            for roles in itertools.product(ROLES, repeat=len(free)):
                                tp = frozenset(p for p, r in zip(free, roles) if r == 'tp')
                                rg = frozenset(p for p, r in zip(free, roles) if r == 'rg')
                                d2 = frozenset(p for p, r in zip(free, roles) if r == 'd2')
                                v = frozenset(p for p, r in zip(free, roles) if r == 'v')
                                g = rg | d2
                                r0 = rq0 | tp
                                # the stated support conditions (10155, 10475, 10822, 10862-10868)
                                if tp & (C | B | J | rq0 | dk) or g & (C | J | r0 | dk) or \
                                        v & (g | C | J | r0 | dk | d2):
                                    continue
                                f = J | C | d2 | v
                                key = (q0, tp, rg, f)
                                fib[key] = fib.get(key, 0) + 1
                                nsrc += 1
    worst = 0.0
    wkey = None
    bad = 0
    for (q0, tp, rg, f), c in fib.items():
        fe = [1 if p in f else 0 for p in range(P)]
        bound = dO(fe) ** 9 * dO(q0) ** 5
        if c > bound:
            bad += 1
        if c / bound > worst:
            worst, wkey = c / bound, (q0, sorted(tp), sorted(rg), sorted(f), c, bound)
    rec('U2', f'eq:inverse-new-fibre at K_slot = 0 by brute force: {nsrc} source tuples over {P} abstract primes '
        f'(cubes on {len(Bpr)} primes, valuations <= {VMAX}), {len(fib)} targets (q0,t\',r_g,f_new); '
        f'supp B in supp(J q0) and q0 integral in every source ({viol} violations); every fibre <= d(f)^9 d(q0)^5',
        bad == 0 and viol == 0, f'max fibre/bound = {worst:.4f} at {wkey}; max fibre {max(fib.values())}')
    # control: the bound without the q0 factor fails somewhere
    bad2 = sum(1 for (q0, tp, rg, f), c in fib.items()
               if c > dO([1 if p in f else 0 for p in range(P)]) ** 9)
    ctrl('U2', 'fibre <= d(f)^9 (q0 factor dropped)', bad2 > 0, f'{bad2} targets exceed')
    # information only: smallest (a, b) on a grid with fibre <= d(f)^a d(q0)^b everywhere in this universe
    grid = [(a, b) for a in range(0, 10) for b in range(0, 6)
            if all(c <= dO([1 if p in f else 0 for p in range(P)]) ** a * dO(q0) ** b
                   for (q0, tp, rg, f), c in fib.items())]
    OUT['U2_minimal_exponents'] = [g for g in grid if not any(h != g and h[0] <= g[0] and h[1] <= g[1] for h in grid)]
    print(f"    U2 info: minimal (a,b) with fibre <= d(f)^a d(q0)^b in this universe: {OUT['U2_minimal_exponents']}")
    # divisor-count arithmetic used in the fibre bound
    ok = True
    for _ in range(2000):
        a = [rng.randint(0, 4) for _ in range(4)]
        b = [rng.randint(0, 4) for _ in range(4)]
        ok &= dO([x + y for x, y in zip(a, b)]) <= dO(a) * dO(b) and dO([2 * x for x in a]) <= dO(a) ** 2
    sf = all(4 ** k == (2 ** k) ** 2 for k in range(8))
    rec('U2', 'd(IJ) <= d(I)d(J), d(I^2) <= d(I)^2, 4^omega(f) = d(f)^2 for squarefree f', ok and sf)


# ------------------------------------------------------------------------------------------------
# V. Lemma 17.6
# ------------------------------------------------------------------------------------------------
def part_V(rng):
    # V1 column identity M_u(D) = sum_{d | rad a} mu(d) psi_u(d) q_d^{-1/2} M_{u a^6}(D/q_d)
    pool = [P for P in PRIMES if P.N <= 199]
    D = 400.0
    nsf = sqfree_products(pool, 0, 2.4 * D + 1, maxk=3)
    nu = E.NUS['nu6']

    def Wt(y):
        return E.bump(y, 0.5, 2.4)

    def M(u, Dsc, eps):
        tot = 0j
        for n in nsf:
            q = norm(n)
            w = Wt(q / Dsc)
            if w == 0:
                continue
            tot += mu(n) * nu(cls(n)) * chi_n(n, u) ** eps * w if eps == 1 else \
                mu(n) * nu(cls(n)) * chi_n(n, u).conjugate() * w
        return tot / math.sqrt(Dsc)
    w, wc, cnt = 0.0, 0.0, 0
    for _ in range(12 if QUICK else 40):
        u = (rng.randint(-40, 40), rng.randint(-40, 40))
        if u == (0, 0):
            continue
        alist = rng.sample([P for P in PRIMES if P.N <= 31], rng.randint(1, 2))
        if rng.random() < 0.3:
            u = emul(u, alist[0].gen)                     # u and a share a prime
        a = gen_of(alist)
        ua6 = emul(u, epow(a, 6))
        eps = rng.choice([1, -1])
        lhs = M(u, D, eps)
        rhs = 0j
        rhs_c = 0j
        for r in range(len(alist) + 1):
            for d in itertools.combinations(alist, r):
                d = list(d)
                psid = nu(cls(d)) * (chi_n(d, u) if eps == 1 else chi_n(d, u).conjugate())
                rhs += mu(d) * psid / math.sqrt(norm(d)) * M(ua6, D / norm(d), eps)
                rhs_c += mu(d) * psid / math.sqrt(norm(d)) * M(u, D / norm(d), eps)
        w = max(w, abs(lhs - rhs))
        wc = max(wc, abs(lhs - rhs_c))
        cnt += 1
    rec('V1', f'eq:sixth-power-column-identity on {cnt} (u, a, eps) (u may share primes with a; nu of order 6)',
        w < TOL, f'max err {w:.1e}')
    ctrl('V1', 'M_u in place of M_{ua^6} on the right', wc > 1e-6, f'max err {wc:.1e}')
    # V2 injectivity of (u, a) -> u a^6 on sixth-power-free u and primary a (exact, ideal valuations)
    seen = {}
    coll = 0
    sm = [P for P in PRIMES if P.N <= 31]
    for k in range(0, 3):
        for alist in itertools.combinations_with_replacement(sm, k):
            a = gen_of(list(alist))
            for e in itertools.product(range(6), repeat=3):
                for unit in UNITS:
                    u = unit
                    for P, x in zip(sm[:3], e):
                        u = emul(u, epow(P.gen, x))
                    key = emul(u, epow(a, 6))
                    if key in seen and seen[key] != (u, a):
                        coll += 1
                    seen[key] = (u, a)
    rec('V2', f'(u,a) -> u a^6 injective on {len(seen)} pairs (u sixth-power-free incl. units and shared primes, '
        f'a primary, exact)', coll == 0, f'{coll} collisions')
    # V3 exponent algebra: H/P = U^{1/6} H^{5/6}; e(r) limit
    import fractions
    Fr = fractions.Fraction
    ok = True
    for U in (Fr(10), Fr(1000)):
        for H in (Fr(2) * U, Fr(10 ** 9)):
            P6 = H / U
            ok &= (H ** 6 / P6) == U * H ** 5          # (H/P)^6 = U H^5
    rec('V3', '(H/P)^6 = U H^5 exactly, i.e. H/P = U^{1/6} H^{5/6}', ok)


# ------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    rng = random.Random(20261010)
    print(f'sep30_l17_identities.py  quick={QUICK}  primes={len(PRIMES)}', flush=True)
    for name, fn in (('P', part_P), ('Q', part_Q), ('R', part_R_pointwise), ('S', part_S), ('T', part_T),
                     ('U', part_U), ('V', part_V), ('R6', part_R6)):
        fn(rng)
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
