#!/usr/bin/env python3
"""ADJUDICATOR (C2-countermodel-zoo): independent checks of skeptic findings F1 and F7.  NUMERICAL-NONRIGOROUS
(mpmath, 50 digits) consistency checks of statements whose proofs are given in FINAL.md (the proofs do not rely on
these numbers).

(F1) F_c(s) = zeta(s) (1 + c 2^{-s} + 2 4^{-s}).  Checks: Lambda_c(s) := pi^{-s/2} Gamma(s/2) zeta(s) (2^s + c + 2^{1-s})
     satisfies Lambda_c(s) = Lambda_c(1-s) at random points; F_c vanishes at s = log2(a) + i pi(2k+1)/log 2 etc.;
     the coefficients b(2^k) of log F_c (k = 1..12) and Lambda_F(2^k) = b(2^k) k log 2.
(F7) Rectangular Epstein Z_k(s) = sum' (m^2 + k^2 n^2)^{-s}.  Riemann theta integral (no Bessel functions):
       Z_k(1/2) = -2 - 2/k + int_1^inf (th(t) - 1) t^{-1/2} dt + (1/k) int_1^inf (th*(t) - 1) t^{-1/2} dt,
       th(t) = theta3(e^{-pi t}) theta3(e^{-pi k^2 t}),  th*(t) = theta3(e^{-pi t}) theta3(e^{-pi t/k^2}),
     compared with Chowla-Selberg  Z_k(1/2) = 2 gamma + 2 log(k/(4 pi)) + 8 sum_N d(N) K_0(2 pi N k)
     at k0 = 4 pi e^{-gamma}; then the root k* of Z_k(1/2) = 0 and Delta* = 1/k* versus e^gamma/(4 pi)
     (Betermin-Samaj-Travenec arXiv:2110.09368v2, Conjecture 1.1, normalisation zeta^(2)(s,Delta) = (1/2) sum'(j^2+Delta^2 k^2)^{-s}).

Usage: python3 adj_side_checks.py OUTDIR
"""
import sys, os, json, time, hashlib, random
import mpmath as mp

mp.mp.dps = 50


def F1_checks():
    out = {}
    for label, c in (('c=3', mp.mpf(3)), ('c=2^(3/4)+2^(1/4)', mp.mpf(2) ** 0.75 + mp.mpf(2) ** 0.25)):
        Lam = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s) * (mp.power(2, s) + c + mp.power(2, 1 - s))
        random.seed(1)
        defects = []
        for _ in range(4):
            s = mp.mpc(random.uniform(-2, 3), random.uniform(-30, 30))
            defects.append(float(abs(Lam(s) - Lam(1 - s)) / abs(Lam(s))))
        disc = mp.sqrt(c ** 2 - 8)
        a, b = (c + disc) / 2, (c - disc) / 2           # 1 + c u + 2u^2 = (1 + a u)(1 + b u), ab = 2
        zeros = []
        for x in (a, b):
            for k in (0, 1, 5):
                s = mp.log(x, 2) + 1j * mp.pi * (2 * k + 1) / mp.log(2)
                F = mp.zeta(s) * (1 + c * mp.power(2, -s) + 2 * mp.power(4, -s))
                zeros.append(dict(s=mp.nstr(s, 15), absF=float(abs(F))))
        bcoef = []
        for k in range(1, 13):
            bk = mp.mpf(1) / k + (-1) ** (k + 1) * (a ** k + b ** k) / k     # log F_c coefficient at n = 2^k
            bcoef.append(dict(k=k, b=float(bk), b_over_n_half=float(bk / mp.power(2, k / 2)),
                              Lambda_F=float(bk * k * mp.log(2))))
        out[label] = dict(a=float(a), b=float(b), Re_zero_lines=[float(mp.log(a, 2)), float(mp.log(b, 2))],
                          FE_relative_defects=defects, predicted_zeros=zeros, log_coefficients=bcoef)
    return out


def Z_half_theta(k):
    k = mp.mpf(k)
    th3 = lambda q: mp.jtheta(3, 0, q)
    f1 = lambda t: (th3(mp.exp(-mp.pi * t)) * th3(mp.exp(-mp.pi * k * k * t)) - 1) / mp.sqrt(t)
    f2 = lambda t: (th3(mp.exp(-mp.pi * t)) * th3(mp.exp(-mp.pi * t / (k * k))) - 1) / mp.sqrt(t)
    I1 = mp.quad(f1, [1, 2, 5, 20, mp.inf])
    I2 = mp.quad(f2, [1, 2, 5, 20, 50, 150, 400, 1000, 3000, mp.inf])
    return -2 - 2 / k + I1 + I2 / k


def Z_half_CS(k, Nmax=6):
    k = mp.mpf(k)
    s = mp.mpf(0)
    for N in range(1, Nmax + 1):
        s += mp.mpf(len(mp.divisors(N)) if hasattr(mp, 'divisors') else sum(1 for d in range(1, N + 1) if N % d == 0)) \
            * mp.besselk(0, 2 * mp.pi * N * k)
    return 2 * mp.euler + 2 * mp.log(k / (4 * mp.pi)) + 8 * s, 8 * s


def F7_checks():
    k0 = 4 * mp.pi * mp.exp(-mp.euler)
    zt = Z_half_theta(k0)
    zcs, ksum = Z_half_CS(k0)
    # root of Z_k(1/2) = 0 in k (Chowla-Selberg form), Newton from k0
    g = lambda k: Z_half_CS(k)[0]
    kstar = mp.findroot(g, k0)
    Dstar, Dconj = 1 / kstar, mp.exp(mp.euler) / (4 * mp.pi)
    # a second, generic point to validate the theta-vs-CS agreement where both are O(1)
    k1 = mp.mpf(3)
    return dict(k0=mp.nstr(k0, 30), Z_half_theta_at_k0=mp.nstr(zt, 12), Z_half_CS_at_k0=mp.nstr(zcs, 12),
                eight_sum_dK0_at_k0=mp.nstr(ksum, 12),
                check_k3=dict(theta=mp.nstr(Z_half_theta(k1), 30), CS=mp.nstr(Z_half_CS(k1, 40)[0], 30)),
                k_star=mp.nstr(kstar, 30), Delta_star=mp.nstr(Dstar, 30), e_gamma_over_4pi=mp.nstr(Dconj, 30),
                Delta_star_minus_conjecture=mp.nstr(Dstar - Dconj, 6),
                relative_gap=mp.nstr((Dstar - Dconj) / Dconj, 6),
                dZ_dk_at_k0=mp.nstr(mp.diff(g, k0), 10))


def main():
    t0 = time.time()
    res = dict(script='adj_side_checks.py', mp_dps=mp.mp.dps, mpmath=mp.__version__)
    res['F1'] = F1_checks()
    res['F7'] = F7_checks()
    res['runtime_s'] = round(time.time() - t0, 1)
    os.makedirs(sys.argv[1], exist_ok=True)
    fn = os.path.join(sys.argv[1], 'adj_side_checks.json')
    with open(fn, 'w') as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
    print(hashlib.sha256(open(fn, 'rb').read()).hexdigest(), fn)


if __name__ == '__main__':
    main()
