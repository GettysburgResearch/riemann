#!/usr/bin/env python3
"""SKEPTIC: independent evaluation of Epstein zeta Z_Q(s) = sum' (a m^2 + c n^2)^{-s} via the
Chowla-Selberg / Poisson-summation (K-Bessel) expansion, derived here for b = 0 (NON-RIGOROUS, mpmath):

 Z_Q(s) = 2 a^{-s} zeta(2s) + 2 sqrt(pi/a) Gamma(s-1/2)/Gamma(s) c^{1/2-s} zeta(2s-1)
        + (8 pi^s a^{-s} / Gamma(s)) sum_{N>=1} K_{s-1/2}(2 pi N sqrt(c/a)) (c/a)^{(1/2-s)/2}
                                   * sum_{k n = N} k^{s-1/2} n^{1/2-s}.
(Poisson summation in m of (a m^2 + c n^2)^{-s}, n != 0.)
This uses no Dirichlet L-function and no genus theory, so it is independent of the investigator's
genus-theory formulas (C2-08) on which all their Epstein computations rest.
Checks: x^2+y^2 against 4 zeta(s) beta(s); x^2+5y^2 and x^2+57y^2 against the genus formulas
(mpmath dirichlet) at complex s; values at the investigator's zeros; Z_{x^2+57y^2} on (1/2,1).
Usage: python3 sk_epstein_cs.py OUTDIR
"""
import sys, os, json, time
import mpmath as mp


def Z_cs(s, a, c, Nmax=None):
    s = mp.mpc(s)
    if abs(s - mp.mpf('0.5')) < mp.mpf('1e-25'):      # removable singularity of the two first terms
        h = mp.mpf('1e-15')
        return (Z_cs(s + h, a, c, Nmax) + Z_cs(s - h, a, c, Nmax)) / 2
    lam = 2 * mp.pi * mp.sqrt(mp.mpf(c) / a)
    if Nmax is None:
        Nmax = int(60 / float(lam) + abs(mp.im(s)) / float(lam) * 1.5) + 8
    t1 = 2 * mp.power(a, -s) * mp.zeta(2 * s)
    t2 = 2 * mp.sqrt(mp.pi / a) * mp.gamma(s - 0.5) / mp.gamma(s) * mp.power(c, 0.5 - s) * mp.zeta(2 * s - 1)
    tot = mp.mpc(0)
    for N in range(1, Nmax + 1):
        dsum = mp.fsum(mp.power(k, s - 0.5) * mp.power(N // k, 0.5 - s) for k in range(1, N + 1) if N % k == 0)
        tot += mp.besselk(s - 0.5, lam * N) * dsum
    t3 = 8 * mp.power(mp.pi, s) * mp.power(a, -s) / mp.gamma(s) * mp.power(mp.mpf(c) / a, (0.5 - s) / 2) * tot
    return t1 + t2 + t3


def kron(d, n):
    from math import gcd
    if gcd(abs(d), n) != 1:
        return 0
    res = 1
    while n % 2 == 0:
        n //= 2
        res *= 1 if d % 8 in (1, 7) else -1
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
    return res * j if m == 1 else 0


def L(s, d):
    if d == 1:
        return mp.zeta(s)
    q = abs(d)
    return mp.dirichlet(s, [kron(d, n) for n in range(q)])


def genus5(s):
    return L(s, 1) * L(s, -20) + L(s, -4) * L(s, 5)


def genus57(s):
    return (L(s, 1) * L(s, -228) + L(s, -4) * L(s, 57) + L(s, -3) * L(s, 76) + L(s, -19) * L(s, 12)) / 2


def main():
    t0 = time.time()
    mp.mp.dps = 40
    out = {}
    # calibration: x^2+y^2 = 4 zeta beta
    for s in [mp.mpf(3), mp.mpc(0.3, 7.1), mp.mpc(0.8, 21.5)]:
        ref = 4 * mp.zeta(s) * mp.dirichlet(s, [0, 1, 0, -1])
        out[f'x2+y2 at {s}: |CS-4zeta*beta|/|ref|'] = float(abs(Z_cs(s, 1, 1) - ref) / abs(ref))
    # genus formulas vs CS at complex points
    for s in [mp.mpc(0.3, 11.7), mp.mpc(0.8, 40.1), mp.mpc(0.65, 3.3), mp.mpf(3)]:
        out[f'x2+5y2 at {s}: |CS-genus|/|CS|'] = float(abs(Z_cs(s, 1, 5) - genus5(s)) / abs(Z_cs(s, 1, 5)))
        out[f'x2+57y2 at {s}: |CS-genus|/|CS|'] = float(abs(Z_cs(s, 1, 57) - genus57(s)) / abs(Z_cs(s, 1, 57)))
    # investigator's lowest zeros of x^2+5y^2: Z_cs at midpoint vs at distance 1e-6
    zs = [('0.932969697485414104762', '15.6682495312784723623'), ('0.937666906700399378', '29.9833952351555166601'),
          ('0.696927045312291478', '36.3740636863851281382'), ('0.705682684763995327', '198.604559010664998673')]
    zr = []
    for re_, im_ in zs:
        z = mp.mpc(mp.mpf(re_), mp.mpf(im_))
        f0 = abs(Z_cs(z, 1, 5))
        f1 = min(abs(Z_cs(z + d, 1, 5)) for d in (mp.mpf('1e-6'), mp.mpc(0, '1e-6')))
        zr.append(dict(z=[re_, im_], abs_mid=mp.nstr(f0, 5), abs_at_1em6=mp.nstr(f1, 5), ratio=mp.nstr(f0 / f1, 5)))
    out['x2+5y2 zeros via CS'] = zr
    # x^2+57y^2: values at 1/2, 0.99, the zero, and sign scan on (0,1)
    out['Z57(1/2) CS'] = mp.nstr(Z_cs(mp.mpf('0.5'), 1, 57).real, 20)
    out['Z57(0.99) CS'] = mp.nstr(Z_cs(mp.mpf('0.99'), 1, 57).real, 20)
    x0 = mp.mpf('0.654651202577622799100319554290')
    out['Z57 at claimed real zero (CS)'] = mp.nstr(Z_cs(x0, 1, 57).real, 5)
    out['Z57 at claimed zero +-1e-10 (CS)'] = [mp.nstr(Z_cs(x0 - mp.mpf('1e-10'), 1, 57).real, 5),
                                              mp.nstr(Z_cs(x0 + mp.mpf('1e-10'), 1, 57).real, 5)]
    out['Z57 root via findroot (CS)'] = mp.nstr(mp.findroot(lambda x: Z_cs(x, 1, 57).real, mp.mpf('0.65')), 30)
    out['Z5(1/2) CS'] = mp.nstr(Z_cs(mp.mpf('0.5'), 1, 5).real, 20)
    sc = []
    prev = None
    for k in range(1, 200):
        x = mp.mpf(k) / 200
        v = Z_cs(x, 1, 57).real
        if prev is not None and (v > 0) != (prev > 0):
            sc.append(float(x))
        prev = v
    out['Z57 sign changes on (0,1) grid 1/200'] = sc
    sc5 = []
    prev = None
    for k in range(1, 200):
        x = mp.mpf(k) / 200
        v = Z_cs(x, 1, 5).real
        if prev is not None and (v > 0) != (prev > 0):
            sc5.append(float(x))
        prev = v
    out['Z5 sign changes on (0,1) grid 1/200'] = sc5
    # threshold quantity: Bateman-Grosswald type, sign of Z(1/2) for x^2+k^2... use x^2 + c y^2 near c = 49.78
    thr = []
    for c in [49.0, 49.5, 49.78, 50.0, 50.5]:
        thr.append((c, mp.sqrt(c), mp.nstr(Z_cs(mp.mpf('0.5'), 1, c).real, 8)))
    out['Z_{x^2+cy^2}(1/2) near threshold (c, k=sqrt c, value)'] = [(a, float(b), v) for a, b, v in thr]
    out['root k* of Z_{x^2+k^2 y^2}(1/2)=0'] = mp.nstr(mp.sqrt(mp.findroot(lambda c: Z_cs(mp.mpf('0.5'), 1, c).real, 49.8, verify=False)), 15)
    out['4 pi exp(-gamma)'] = mp.nstr(4 * mp.pi * mp.exp(-mp.euler), 15)
    out['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    json.dump(out, open(os.path.join(sys.argv[1], 'sk_epstein_cs.json'), 'w'), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
