#!/usr/bin/env python3
"""C2 zoo -- independent-library replay (mpmath, NON-RIGOROUS) of the Arb-certified zeros.

For each certified zero rho (read from the JSON outputs), evaluate the function with mpmath's own
implementations (Hurwitz zeta / dirichlet() / direct sums) at the enclosure midpoint and at points at
distance 1e-6, and report |F(mid)| relative to |F(mid +- 1e-6)|.  This replays the *definitions* with a
different code base; it is not a certificate.
Usage: python3 crosscheck_mpmath.py RESULTS_DIR
"""
import sys, os, json, hashlib
import mpmath as mp

mp.mp.dps = 40
K = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)


def dh(s):
    return 5 ** (-s) * (mp.zeta(s, mp.mpf(1) / 5) + K * mp.zeta(s, mp.mpf(2) / 5) - K * mp.zeta(s, mp.mpf(3) / 5)
                        - mp.zeta(s, mp.mpf(4) / 5))


def kron(d, n):
    # small helper, Kronecker symbol via mpmath-free code
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
    return mp.dirichlet(s, [kron(d, n) if n % q else 0 for n in range(q)])


def ep5(s):
    return mp.zeta(s) * L(s, -20) + L(s, -4) * L(s, 5)


def zeta_N(N):
    return lambda s: mp.fsum(mp.power(n, -s) for n in range(1, N + 1))


def check(F, re, im):
    z = mp.mpc(mp.mpf(re), mp.mpf(im))
    f0 = abs(F(z))
    fn = min(abs(F(z + d)) for d in (mp.mpf('1e-6'), -mp.mpf('1e-6'), mp.mpc(0, '1e-6'), mp.mpc(0, '-1e-6')))
    return dict(re=re[:22], im=im[:22], abs_F_mid=mp.nstr(f0, 5), min_abs_F_at_dist_1e-6=mp.nstr(fn, 5),
                ratio=mp.nstr(f0 / fn, 5))


def main():
    R = sys.argv[1]
    out = {}
    d = json.load(open(os.path.join(R, 'dh_zeros.json')))
    out['davenport_heilbronn'] = [check(dh, z['re_mid'], z['im_mid']) for z in d['zeros_in_region'] if z.get('ok')]
    e = json.load(open(os.path.join(R, 'epstein_zeros.json')))
    out['epstein_x2+5y2_first5'] = [check(ep5, z['re_mid'], z['im_mid']) for z in e['offline_zeros_x2+5y2'][:5]]
    p = json.load(open(os.path.join(R, 'partial_sums_N19.json')))
    out['zeta_19'] = [check(zeta_N(19), z['re_mid'], z['im_mid']) for z in p['zeros'] if z.get('re_gt_1_certified')]
    fn = os.path.join(R, 'crosscheck_mpmath.json')
    json.dump(dict(mpmath=mp.__version__, dps=mp.mp.dps, results=out), open(fn, 'w'), indent=1)
    print(json.dumps(out, indent=1))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
