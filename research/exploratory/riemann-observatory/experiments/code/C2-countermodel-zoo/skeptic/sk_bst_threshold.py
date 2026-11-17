#!/usr/bin/env python3
"""SKEPTIC side check (prior art cited in C2-12): Betermin-Samaj-Travenec (arXiv:2110.09368) Conjecture 1.1
states that the unique solution of zeta2(1/2, Delta) = 0, Delta in (0,1), is Delta = e^gamma/(4 pi), where
zeta2(s, Delta) = (1/2) sum' (j^2 + Delta^2 k^2)^{-s}.  Chowla-Selberg at s = 1/2 (exact; see sk_epstein_cs.py) gives,
for Z_k(s) = sum'(x^2 + k^2 y^2)^{-s} (k = 1/Delta by their symmetry (1.3)):
      Z_k(1/2) = 2 gamma + 2 log(k/(4 pi)) + 8 sum_{N>=1} d(N) K_0(2 pi N k),
so at k = 4 pi e^{-gamma} the value is 8 sum d(N) K_0(...) > 0, i.e. NOT zero.
Two independent high-precision evaluations (mpmath, NON-RIGOROUS):
 (a) the closed form above;  (b) Riemann's theta-integral  Z_k(1/2) = (2/sqrt k)... see below.
For Q = x^2 + k^2 y^2 (det k^2): with q(m,n) = (m^2/k + k n^2) (det 1),  Z_k(s) = k^{-s} Z_q(s), and
Z_q(1/2) = 2 int_1^inf (theta_q(t) - 1) t^{-1/2} dt - 4,  theta_q(t) = theta3(e^{-pi t/k}) theta3(e^{-pi t k})."""
import sys, os, json
import mpmath as mp
mp.mp.dps = 50
k0 = 4 * mp.pi * mp.exp(-mp.euler)


def closed(k):
    S = mp.fsum(len([d for d in range(1, N + 1) if N % d == 0]) * mp.besselk(0, 2 * mp.pi * N * k) for N in range(1, 6))
    return 2 * mp.euler + 2 * mp.log(k / (4 * mp.pi)) + 8 * S, 8 * S


def theta_route(k):
    th = lambda t: mp.jtheta(3, 0, mp.exp(-mp.pi * t / k)) * mp.jtheta(3, 0, mp.exp(-mp.pi * t * k)) - 1
    I = mp.quad(lambda t: th(t) / mp.sqrt(t), [1, 3, 10, 30, 100, 300, 1000, mp.inf])
    Zq = 2 * I - 4
    return Zq / mp.sqrt(k)        # Z_k(1/2) = k^{-1/2} Z_q(1/2)


out = {}
v, S = closed(k0)
out['k0 = 4 pi e^-gamma'] = mp.nstr(k0, 30)
out['closed form Z_k0(1/2)'] = mp.nstr(v, 10)
out['8 sum d(N) K0(2 pi N k0)'] = mp.nstr(S, 10)
out['theta-integral Z_k0(1/2)'] = mp.nstr(theta_route(k0), 10)
out['theta-integral Z_k(1/2) at k=7 (check vs closed)'] = [mp.nstr(theta_route(mp.mpf(7)), 20), mp.nstr(closed(mp.mpf(7))[0], 20)]
kstar = mp.findroot(lambda k: closed(k)[0], k0)
out['k* (root of closed form)'] = mp.nstr(kstar, 30)
out['relative gap 1 - k*/k0'] = mp.nstr(1 - kstar / k0, 6)
out['Delta*_c = 1/k*  vs  e^gamma/(4 pi)'] = [mp.nstr(1 / kstar, 30), mp.nstr(mp.exp(mp.euler) / (4 * mp.pi), 30)]
print(json.dumps(out, indent=1))
os.makedirs(sys.argv[1], exist_ok=True)
json.dump(out, open(os.path.join(sys.argv[1], 'sk_bst_threshold.json'), 'w'), indent=1)
