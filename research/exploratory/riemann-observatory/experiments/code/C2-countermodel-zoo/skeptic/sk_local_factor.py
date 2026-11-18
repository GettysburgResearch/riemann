#!/usr/bin/env python3
"""SKEPTIC: a countermodel family MISSING from the zoo, relevant to C2-00(i), C2-25 and C2-31.

  F_c(s) = zeta(s) * D_c(s),   D_c(s) = 1 + c 2^{-s} + 2 * 4^{-s} = (1 + a 2^{-s})(1 + b 2^{-s}),  ab = 2, a + b = c.
Facts (elementary; checked numerically below with mpmath):
 * ordinary Dirichlet series over N, a_1 = 1, real coefficients; a_n >= 0 when c >= 0;
 * Euler product over the rational primes (F_p = (1-p^-s)^{-1} for p odd, F_2 = D_c(s)/(1-2^-s)),
   hence multiplicative coefficients;
 * self-dual degree-1 functional equation with Gamma_R(s) and conductor 4:
     Lambda(s) = pi^{-s/2} Gamma(s/2) zeta(s) * (2^s + c + 2^{1-s}) = Lambda(1-s)   [2^s D_c(s) = 2^s + c + 2^{1-s}];
 * simple pole at s = 1, order 1;
 * zeros of D_c: 2^{-s} = -1/a, -1/b, i.e. Re s = log2(a), log2(b) = log2(a), 1 - log2(a)  (vertical progressions).
   c = 3  (a = 1, b = 2): zeros on Re s = 0 and Re s = 1  (integer coefficients 1, 3, 2);
   c = 2(2^{-1/4} + 2^{-3/4}) (a = 2^{1/4}... ): zeros on Re s = 1/4 and 3/4, strictly inside the strip.
 So F_c is RH-false.  It is not in the Selberg class only because the local factor at 2 has |alpha| = 2^{3/4}
 (resp. 2) > 1, i.e. the Euler-product axiom b(p^k) << p^{k theta}, theta < 1/2, (Ramanujan at the Satake level)
 fails.  Variant G(s) = zeta(s)(1-2^{-s})(1-2^{1-s}) is ENTIRE (pole cancelled), has the same FE and zeros on
 Re s = 0, 1, but negative coefficients.  NOTE: every member of this family has Lambda_F(2^k) < 0 for some k
 (numerator local roots beta_1 beta_2 = 2 force beta_1^k + beta_2^k > 1), so von Mangoldt positivity
 Lambda_F(n) >= 0 DOES exclude it; the zoo's 'explicit formula' column should record this.
Usage: python3 sk_local_factor.py OUTDIR"""
import sys, os, json, random, math
import mpmath as mp
mp.mp.dps = 30
out = {}


def F(s, c):
    return mp.zeta(s) * (1 + c * mp.power(2, -s) + 2 * mp.power(4, -s))


def Lam(s, c):
    return mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s) * (mp.power(2, s) + c + mp.power(2, 1 - s))


for name, c in [('c=3', mp.mpf(3)), ('c=2(2^-1/4+2^-3/4)', 2 * (mp.power(2, -0.25) + mp.power(2, -0.75)))]:
    random.seed(2)
    fe = []
    for _ in range(3):
        s = mp.mpc(random.uniform(-1, 2), random.uniform(1, 60))
        fe.append(float(abs(Lam(s, c) - Lam(1 - s, c)) / abs(Lam(s, c))))
    # roots of 2 x^2 + c x + 1 = 0 in x = 2^{-s}
    r = mp.polyroots([2, c, 1])
    zs = [-mp.log(abs(x), 2) + 1j * mp.pi / mp.log(2) for x in r]    # x negative real: 2^{-s} = |x| e^{i pi}
    vals = [mp.nstr(abs(F(z, c)), 3) for z in zs]
    # coefficient positivity and multiplicativity for n <= 64
    D = {1: 1, 2: c, 4: 2}
    a = [None] + [mp.fsum(D[d] for d in D if n % d == 0) for n in range(1, 65)]
    mult = all(abs(a[m * n] - a[m] * a[n]) < 1e-20 for m in range(1, 9) for n in range(1, 9) if math.gcd(m, n) == 1 and m * n <= 64)
    out[name] = dict(FE_rel_defect=fe, zeros=[[mp.nstr(mp.re(z), 12), mp.nstr(mp.im(z), 12)] for z in zs],
                     abs_F_at_zeros=vals, min_a_n_le_64=mp.nstr(min(a[1:]), 6), multiplicative_le_64=mult)
# variant G: entire, Lambda_G(n) >= 0
G = lambda s: mp.zeta(s) * (1 - mp.power(2, -s)) * (1 - mp.power(2, 1 - s))
LG = lambda s: mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s) * (mp.power(2, s) - 3 + mp.power(2, 1 - s))
s = mp.mpc(0.3, 17.2)
out['G: FE rel defect at 0.3+17.2i'] = float(abs(LG(s) - LG(1 - s)) / abs(LG(s)))
out['G: |G(1 + 2 pi i/log 2)|'] = mp.nstr(abs(G(1 + 2j * mp.pi / mp.log(2))), 3)
out['G: value near s=1 (entire, no pole)'] = mp.nstr(G(mp.mpf(1) + mp.mpf('1e-12')), 8)
# von Mangoldt at 2^k: zeta's own 2-factor contributes +1, numerator factor (1 - beta x) contributes -beta^k,
# numerator factor (1 + a x) contributes -(-a)^k
out['G: Lambda_G(2^k)/log 2 for k=1..5 (negative)'] = [1 - 1 - 2 ** k for k in range(1, 6)]
out['F_3: Lambda_F(2^k)/log 2 for k=1..5 (sign changes)'] = [1 - (-1) ** k - (-2) ** k for k in range(1, 6)]
print(json.dumps(out, indent=1))
os.makedirs(sys.argv[1], exist_ok=True)
json.dump(out, open(os.path.join(sys.argv[1], 'sk_local_factor.json'), 'w'), indent=1)
