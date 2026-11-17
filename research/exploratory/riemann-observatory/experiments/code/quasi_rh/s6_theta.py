# s6_theta.py -- numerical Kubota cubic theta function from the Dunn-Radziwill / Patterson
# coefficient formulas, written from scratch for the Level-2 audit of Section 6 of
# "The Quasi-Riemann Hypothesis" (paper2.tex).  No code from the OpenAI repository.
#
# Source formulas (read from the rendered pages of arXiv:2109.07463v?, pp.16-18 and App. A):
#   DR (5.1): gamma w = (((az+b) conj(cz+d) + a conj(c) v^2)/(|cz+d|^2+|c|^2 v^2), v/(|cz+d|^2+|c|^2 v^2))
#   DR (5.4): chi(gamma) = (c/a)_3 for gamma = (a b; c d) in Gamma_1(3) (= I mod 3), c != 0; 1 otherwise;
#             chi = 1 on SL_2(Z); theta automorphic on Gamma_2 = SL_2(Z) Gamma_1(3) with multiplier chi.
#   DR (5.6): theta(w) = sigma v^{2/3} + sum_{mu in lambda^-3 O} tau(mu) v K_{1/3}(4 pi |mu| v) ebreve(mu z),
#             sigma = 3^{5/2}/2.
#   DR (5.7)-(5.8): tau(mu) = conj g(lambda^2,c) |d/c| 3^{n/2+2}               mu = +-lambda^{3n-4} c d^3, n>=1
#                            e^{-2 pi i/9} conj g(omega lambda^2,c)|d/c|3^{n/2+2}  mu = +-omega lambda^{3n-4} c d^3
#                            e^{+2 pi i/9} conj g(omega^2 lambda^2,c)|d/c|3^{n/2+2} mu = +-omega^2 lambda^{3n-4} c d^3
#                            conj g(1,c) |d/c| 3^{n/2+5/2}                         mu = +-lambda^{3n-3} c d^3, n>=0
#                            0 otherwise;  c,d = 1 mod 3, c squarefree (no coprimality of c,d).
#   DR (2.1): g(r,c) = sum_{x mod c} (x/c)_3 ebreve(r x / c), ebreve(z) = exp(2 pi i (z + conj z)).
#   DR (5.13),(5.14): tau_1, tau_2 (cusp coefficients); DR App. A: d_10(mu) = omega tau_2(omega mu) ebreve(mu),
#             d_19(mu) = omega^2 tau_1(omega^2 mu) ebreve(mu); F_j = theta(gamma_j w) = F_j^* for j >= 10.
import sys, os, math, cmath
import numpy as np
from scipy.special import kv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s6_zw import *

SIGMA = 3 ** 2.5 / 2
_gauss_cache = {}

def gauss(r, c):
    """DR (2.1) generalized: g(r,c) = sum_{x mod c} (x/c)_3 ebreve(r x/c)."""
    key = (r, c)
    if key in _gauss_cache: return _gauss_cache[key]
    if norm(c) == 1:
        val = complex(1.0)
    else:
        u, fac = factor(c)
        cc = cv(c); rr = cv(r)
        s = 0j
        for x in residues(c):
            tot = 0; zero = False
            for pi, e in fac:
                j = cubic_exp_prime(x, pi)
                if j is None: zero = True; break
                tot += j * e
            if zero: continue
            s += omega_pow(tot) * ebreve(rr * cv(x) / cc)
        val = s
    _gauss_cache[key] = val
    return val

def lam_pow(k):
    if k >= 0: return power(LAM, k)
    raise ValueError

def decompose(mu_num, lam_shift):
    """Given mu = mu_num / lambda^lam_shift (mu_num in O, nonzero), return (u, M, c, d) with
    mu = u * lambda^M * c * d^3, c squarefree primary, d primary, u unit; or None if some prime exponent = 2 mod 3."""
    u, fac = factor(mu_num)
    M = -lam_shift
    c = ONE; d = ONE
    for pi, e in fac:
        if pi == LAM:
            M += e
        else:
            if e % 3 == 2: return None
            if e % 3 == 1: c = mul(c, pi)
            d = mul(d, power(pi, e // 3))
    # now mu_num = u * lambda^{M+lam_shift} * c * d^3 exactly (primes primary, LAM=1+2w)
    return u, M, c, d

E9 = cmath.exp(2j * math.pi / 9)
LAM2 = power(LAM, 2)

def tau(mu_num, lam_shift=3):
    """DR (5.7) at mu = mu_num / lambda^lam_shift."""
    dec = decompose(mu_num, lam_shift)
    if dec is None: return 0j
    u, M, c, d = dec
    ratio = math.sqrt(norm(d) / norm(c))
    if M % 3 == 2 and M >= -1:
        n = (M + 4) // 3
        if u in ((1, 0), (-1, 0)):
            return np.conj(gauss(LAM2, c)) * ratio * 3 ** (n / 2 + 2)
        if u in ((0, 1), (0, -1)):
            return E9 ** (-1) * np.conj(gauss(mul(OM, LAM2), c)) * ratio * 3 ** (n / 2 + 2)
        return E9 * np.conj(gauss(mul(OM2, LAM2), c)) * ratio * 3 ** (n / 2 + 2)
    if M % 3 == 0 and M >= -3:
        n = (M + 3) // 3
        if u in ((1, 0), (-1, 0)):
            return np.conj(gauss(ONE, c)) * ratio * 3 ** (n / 2 + 2.5)
        return 0j
    return 0j

def tau1(mu_num, lam_shift=4):
    """DR (5.13) at mu = mu_num / lambda^lam_shift."""
    dec = decompose(mu_num, lam_shift)
    if dec is None: return 0j
    u, M, c, d = dec
    if M != -4: return 0j
    ratio = math.sqrt(norm(d) / norm(c))
    if u == (1, 0):
        return 9 * OMEGA * np.conj(gauss(LAM2, c)) * ratio
    if u == (0, 1):
        return 9 * E9 ** (-1) * OMEGA ** 2 * np.conj(gauss(mul(OM, LAM2), c)) * ratio
    if u == (-1, -1):
        return 9 * E9 * np.conj(gauss(mul(OM2, LAM2), c)) * ratio
    return 0j

def tau2(mu_num, lam_shift=4):
    """DR (5.14) at mu = mu_num / lambda^lam_shift."""
    dec = decompose(mu_num, lam_shift)
    if dec is None: return 0j
    u, M, c, d = dec
    if M != -4: return 0j
    ratio = math.sqrt(norm(d) / norm(c))
    if u == (-1, 0):
        return 9 * OMEGA ** 2 * np.conj(gauss(LAM2, c)) * ratio
    if u == (0, -1):          # -omega
        return 9 * E9 ** (-1) * np.conj(gauss(mul(OM, LAM2), c)) * ratio
    if u == (1, 1):           # -omega^2
        return 9 * OMEGA * E9 * np.conj(gauss(mul(OM2, LAM2), c)) * ratio
    return 0j

def lattice_points(R, lam_shift):
    """All nonzero m in O with |m / lambda^lam_shift| <= R."""
    rad = R * 3 ** (lam_shift / 2)
    pts = []
    B = int(rad * 2 / SQ3) + 2
    for b in range(-B, B + 1):
        for a in range(-int(rad) - B - 2, int(rad) + B + 3):
            if (a, b) == (0, 0): continue
            if abs(cv((a, b))) <= rad: pts.append((a, b))
    return pts

class FourierSeries:
    """f(z,v) = const(v) + sum coef[mu] v K_{1/3}(4 pi |mu| v) ebreve(mu z), mu = m/lambda^shift."""
    def __init__(self, coeff_fn, lam_shift, R, const=0.0):
        lamc = cv(LAM) ** lam_shift
        mus = []; cs = []
        for m in lattice_points(R, lam_shift):
            t = coeff_fn(m, lam_shift)
            if abs(t) > 0:
                mus.append(cv(m) / lamc); cs.append(t)
        self.mu = np.array(mus); self.c = np.array(cs, dtype=complex)
        self.const = const
    def __call__(self, z, v):
        x = 4 * math.pi * np.abs(self.mu) * v
        val = np.sum(self.c * v * kv(1.0 / 3, x) * np.exp(4j * math.pi * (self.mu * z).real))
        return val + self.const * v ** (2.0 / 3)

def act(g, z, v):
    """DR (5.1) action of g=((a,b),(c,d)) (complex entries) on (z,v)."""
    (a, b), (c, d) = g
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * v * v
    zn = ((a * z + b) * np.conj(c * z + d) + a * np.conj(c) * v * v) / den
    return zn, v / den
