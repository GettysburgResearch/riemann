#!/usr/bin/env python3
"""C2 countermodel zoo -- Epstein zeta functions of binary quadratic forms with class number > 1.

Z_Q(s) = sum'_{(m,n) != 0} Q(m,n)^{-s}.  For forms in a genus containing one class (idoneal case) Z_Q is a
finite combination of products of Dirichlet L-functions (genus theory), which Arb evaluates rigorously:
  Q1 = x^2 + 5 y^2   (D = -20, h = 2):  Z_Q1 = zeta(s) L(s,chi_-20) + L(s,chi_-4) L(s,chi_5)
  Q2 = x^2 + 57 y^2  (D = -228, h = 4, class group (Z/2)^2):
       Z_Q2 = 1/2 [ zeta L_-228 + L_-4 L_57 + L_-3 L_76 + L_-19 L_12 ]
(derivation: sum_C psi(C) Z_C(s) = w L_K(s,psi), w = 2, and for a genus character psi attached to
D = D1 D2, L_K(s,psi) = L(s,chi_D1) L(s,chi_D2); every genus has one class, so the genus characters
separate the classes).  Both identities are checked numerically against direct lattice sums at s = 3.
Functional equation: Lambda_Q(s) = (sqrt|D|/(2 pi))^s Gamma(s) Z_Q(s) = Lambda_Q(1-s) (checked in Arb).

Outputs
  * rigorous right edge: Z_Q1 has no zeros for Re s >= sigma_E (argument bound, see REPORT sect. EP-2);
  * NON-RIGOROUS scan + RIGOROUS Krawczyk certificates for off-line zeros of Z_Q1 in 1/2+eta <= sigma, t <= T;
  * RIGOROUS real zero of Z_Q2 in (1/2, 1) by a certified sign change (Arb) and bisection.
Usage: python3 epstein_zeros.py OUTDIR [T_MAX]
"""
import sys, os, json, time, hashlib, math
import numpy as np
import flint
from flint import acb, arb, acb_series
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zoo_common import certify_zero, newton_polish, series_eval, winding_number, versions

flint.ctx.prec = 128


def kronecker(d, n):
    """Kronecker symbol (d/n) for n >= 1."""
    if n == 1:
        return 1
    res = 1
    while n % 2 == 0:
        n //= 2
        if d % 2 == 0:
            return 0
        res *= 1 if d % 8 in (1, 7) else -1
    # now n odd: Jacobi symbol (d/n)
    a, m, j = d % n, n, 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                j = -j
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            j = -j
        a %= m
    return res * (j if m == 1 else 0)


_CHAR = {}


def char_for(d):
    """python-flint dirichlet_char (modulus |d|) equal to the Kronecker character (d/.) (d fundamental)."""
    if d in _CHAR:
        return _CHAR[d]
    q = abs(d)
    want = [kronecker(d, n) for n in range(1, q + 1)]
    for lab in range(1, q + 1):
        if math.gcd(lab, q) != 1:
            continue
        c = flint.dirichlet_char(q, lab)
        if c.order() > 2:
            continue
        vals = []
        for n in range(1, q + 1):
            if math.gcd(n, q) != 1:
                vals.append(0)
            else:
                e = c.chi_exponent(n)
                vals.append(1 if e == 0 else -1)
        if vals == want:
            _CHAR[d] = c
            return c
    raise ValueError(d)


def Lval(s, d):
    return acb.zeta(s) if d == 1 else acb.dirichlet_l(s, char_for(d))


def Lser(s, d):
    return acb_series.zeta(s) if d == 1 else acb_series.dirichlet_l(s, char_for(d))


FORMS = {
    'x2+5y2': dict(D=-20, a=1, c=5, terms=[(1, 1, -20), (1, -4, 5)], h=2),
    'x2+57y2': dict(D=-228, a=1, c=57, terms=[(arb(1) / 2, 1, -228), (arb(1) / 2, -4, 57),
                                            (arb(1) / 2, -3, 76), (arb(1) / 2, -19, 12)], h=4),
}


def Z(s, form):
    return sum((acb(c) * Lval(s, d1) * Lval(s, d2) for c, d1, d2 in FORMS[form]['terms']), acb(0))


def Zser(s, form):
    tot = None
    for c, d1, d2 in FORMS[form]['terms']:
        t = Lser(s, d1) * Lser(s, d2) * acb(c)
        tot = t if tot is None else tot + t
    return tot


def Lam(s, form):
    D = FORMS[form]['D']
    return ((arb(-D).sqrt() / (2 * arb.pi())).log() * s).exp() * s.gamma() * Z(s, form)


def direct_sum(form, s=3.0, M=1500):
    a, c = FORMS[form]['a'], FORMS[form]['c']
    m = np.arange(-M, M + 1, dtype=float)
    tot = 0.0
    for n in range(-M, M + 1):
        q = a * m * m + c * n * n
        if n == 0:
            q = q[q > 0]
        tot += np.sum(q ** (-s))
    return tot


def right_edge_Q1(P=10_000_000):
    """Z_Q1 = zeta_K (1 + R), R = ((1-2^-s)/(1+2^-s)) prod_{p = 3,7 mod 20} ((1-p^-s)/(1+p^-s))^2 (sigma > 1).
    No zero where S(sigma) = 2 atan(2^-sigma) + sum_{p=3,7 mod 20} 4 atan(p^-sigma) < pi."""
    sieve = np.ones(P + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(P ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    ps = [int(p) for p in np.nonzero(sieve)[0] if p % 20 in (3, 7)]
    psf = np.array(ps, dtype=float)
    Sf = lambda sg: 2 * math.atan(2 ** -sg) + float(np.sum(4 * np.arctan(psf ** (-sg))))
    lo, hi = 1.0001, 4.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if Sf(mid) > math.pi else (lo, mid)
    approx = (lo + hi) / 2

    def bounds(sig):
        s = arb(sig)
        tot = 2 * (arb(2) ** (-s)).atan()
        for p in ps:
            tot += 4 * (arb(p) ** (-s)).atan()
        tail = 4 * arb("1.25506") * s * arb(P) ** (1 - s) / ((s - 1) * arb(P).log())
        return tot, tot + tail
    out = dict(P=P, float_root_partial=approx)
    for d in [1e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2]:
        lo_b, up_b = bounds(approx + d)
        if up_b < arb.pi():
            out['zero_free_for_sigma_ge'] = approx + d
            out['S_upper'] = up_b.str(15)
            break
    for d in [1e-4, 5e-4, 1e-3, 2e-3, 5e-3]:
        lo_a, _ = bounds(approx - d)
        if lo_a > arb.pi():
            out['S_exceeds_pi_at_sigma'] = approx - d
            break
    cum = np.cumsum(4 * np.arctan(psf ** (-1.0))) + 2 * math.atan(0.5)
    K = int(np.searchsorted(cum, math.pi)) + 1
    out['primes_needed_at_sigma_1'] = dict(K_including_2=K + 1, primes=[2] + ps[:K])
    return out


def real_zero_Q2():
    """Certified sign change of Z_Q2 on (1/2, 1) and bisection to width 1e-25 (all in Arb, real s)."""
    form = 'x2+57y2'
    v = lambda x: Z(acb(x), form).real
    a, b = arb("0.5"), arb("0.99")
    va, vb = v(a), v(b)
    out = dict(Z_at_half=va.str(20), Z_at_0_99=vb.str(20))
    if not (va > 0 and vb < 0):
        out['certified'] = False
        return out
    lo, hi = a, b
    for _ in range(90):
        mid = (lo + hi) / 2
        vm = v(mid)
        if vm > 0:
            lo = mid
        elif vm < 0:
            hi = mid
        else:
            break
    out.update(certified=True, enclosure_lo=lo.str(30, radius=False), enclosure_hi=hi.str(30, radius=False),
               note='Z_Q2 real-analytic on [1/2, 0.99]; Arb sign certificates at both ends of each bracket')
    # also Z_Q1 at 1/2 for contrast (no real zero expected, k = sqrt5 < 4 pi e^-gamma)
    out['Z_Q1_at_half'] = Z(acb("0.5"), 'x2+5y2').real.str(20)
    out['k_Q2'] = math.sqrt(57)
    out['threshold_4pi_exp_minus_gamma'] = float(4 * arb.pi() * (-arb.const_euler()).exp())
    return out


def scan_Q1(T_MAX, SIGMA_MAX, eta=0.02, dt=0.05, ds=0.02):
    form = 'x2+5y2'
    fv = lambda s: Z(s, form)
    fdd = lambda z: series_eval(lambda s: Zser(s, form), z)
    cands, blocks = [], []
    T = 2.0
    while T < T_MAX:
        T2 = min(T + 10.0, T_MAX)
        sig = list(np.arange(0.5 + eta, SIGMA_MAX + 1e-9, ds))
        tt = list(np.arange(T - 0.5, T2 + 0.5, dt))
        flint.ctx.prec = 53
        A = np.array([[abs(complex(fv(acb(x, y)))) for y in tt] for x in sig])
        flint.ctx.prec = 128
        for i in range(len(sig)):
            for j in range(1, len(tt) - 1):
                lo_i, hi_i = max(0, i - 1), min(len(sig), i + 2)
                if A[i, j] <= A[lo_i:hi_i, j - 1:j + 2].min() and T <= tt[j] < T2:
                    z, res = newton_polish(fdd, complex(sig[i], tt[j]))
                    if res < 1e-20 and 0.5 + eta / 2 < z.real <= SIGMA_MAX + 0.05 and T - 1 <= z.imag <= T2 + 1:
                        if all(abs(z - c) > 1e-8 for c in cands):
                            cands.append(z)
        flint.ctx.prec = 53
        w = winding_number(fv, [complex(0.5 + eta, T), complex(SIGMA_MAX, T), complex(SIGMA_MAX, T2),
                                complex(0.5 + eta, T2)], n_per_edge=600)
        flint.ctx.prec = 128
        blocks.append(dict(t_lo=T, t_hi=T2, winding=round(w, 4)))
        T = T2
    zeros = []
    for z in sorted(cands, key=lambda z: z.imag):
        c = certify_zero(fdd, z)
        c['approx'] = [z.real, z.imag]
        zeros.append(c)
    return zeros, blocks


def main():
    outdir = sys.argv[1]
    T_MAX = float(sys.argv[2]) if len(sys.argv) > 2 else 150.0
    t0 = time.time()
    rep = dict(model='Epstein zeta functions x^2+5y^2 (h=2), x^2+57y^2 (h=4)', versions=versions(),
               prec_bits=128, params=dict(T_MAX=T_MAX, eta=0.02))
    chk = {}
    for form in FORMS:
        chk[f'{form}: direct lattice sum (M=1500) at s=3 minus L-formula (non-rigorous)'] = \
            direct_sum(form) - float(Z(acb(3), form).real)
        for pt in [acb("0.3", "11.7"), acb("0.8", "40.1")]:
            d = Lam(pt, form) - Lam(1 - pt, form)
            chk[f'{form}: Lambda(s)-Lambda(1-s) at {complex(pt)} contains 0'] = bool(d.contains(0))
            chk[f'{form}: |Lambda(s)-Lambda(1-s)| enclosure at {complex(pt)}'] = str(d)
    rep['checks'] = chk
    rep['characters'] = {str(d): [char_for(d).modulus(), char_for(d).number()] for d in
                         [-20, -4, 5, -228, 57, -3, 76, -19, 12]}
    rep['real_zero_x2+57y2'] = real_zero_Q2()
    print('real zero', rep['real_zero_x2+57y2'], flush=True)
    edge = right_edge_Q1()
    rep['right_edge_x2+5y2'] = edge
    print('edge', edge, flush=True)
    sigmax = min(edge.get('zero_free_for_sigma_ge', 2.0), 2.0)
    zeros, blocks = scan_Q1(T_MAX, sigmax)
    rep['offline_zeros_x2+5y2'] = zeros
    rep['blocks'] = blocks
    rep['winding_total'] = sum(b['winding'] for b in blocks)
    rep['n_certified_off_line'] = sum(1 for c in zeros if c.get('ok') and c.get('off_line'))
    rep['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(outdir, exist_ok=True)
    fn = os.path.join(outdir, 'epstein_zeros.json')
    json.dump(rep, open(fn, 'w'), indent=1, default=str)
    print(json.dumps(dict(n=len(zeros), n_off=rep['n_certified_off_line'], winding=rep['winding_total'],
                          runtime=rep['runtime_s'])))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
