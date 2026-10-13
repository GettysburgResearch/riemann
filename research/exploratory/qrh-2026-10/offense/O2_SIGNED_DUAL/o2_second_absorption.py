#!/usr/bin/env python3
"""Round 2: apply the Moebius absorption a second time, to the dual variable g of Prop. G.

Status: [EXACT] checks are exact on finitely many cases; [FLOAT] checks are floating point, finite.

Over O = Z[omega], for squarefree g composed of split primes of distinct norms (so O/g = Z/N(g)):
  C5 [FLOAT]  Oct 5 eq:gj in our conventions: gamma_1 gamma_2 = mu alpha G and gamma_2^3 = mu alpha,
              with G(n) = conj chi_n(4) gamma_3(n), e(z) = exp(4 pi i Im z / sqrt 3).
  C6 [EXACT]  mu(g) 1_{g|k} = prod_{p|g} (|chi_p(k)|^2 - 1) = sum_{d|g} mu(g/d) chi_d(k)^6
              (chi_d(k)^6 = principal character mod d), with true sextic symbols.
  C7 [FLOAT]  'Gauss sum in the row': for j = 1..5,
                 sum_{x mod g} chi_g(x)^j e(k x / g) = conj chi_g(k)^j sqrt(N g) gamma_j(g)   if (k,g) = 1,
                                                    = 0                                     if g | k,
              so every multiplicative Gauss sum of modulus g vanishes on the support of 1_{g|k}.
  C8 [FLOAT]  the only modulus-g object supported there is the principal character, whose Gauss sum is
              the Ramanujan sum: sum_{x mod g, (x,g)=1} e(u x / g) = sum_{e | (g,u)} mu(g/e) N(e), and at
              u = 1 it equals mu(g) = conj(alpha G)(g) gamma_1(g) gamma_2(g)  (second absorption = identity).

Usage: python3 -I o2_second_absorption.py OUT.json
"""
import cmath
import itertools
import json
import math
import os
import random
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import signed_dual_numerics as sdn  # noqa: E402  (own code in this folder)

SQ3 = math.sqrt(3.0)
W6 = complex(-0.5, SQ3 / 2)  # omega


def e(z):
    return cmath.exp(4j * math.pi * z.imag / SQ3)


def cx(a, b):
    return a + b * W6


def primary_prime(q):
    """primary pi = a + b w (a = 1, b = 0 mod 3) with N(pi) = q; returns both conjugate primaries."""
    out = []
    R = int(math.isqrt(4 * q)) + 2
    for a in range(-R, R + 1):
        for b in range(-R, R + 1):
            if a * a - a * b + b * b == q and a % 3 == 1 and b % 3 == 0:
                out.append((a, b))
    return out


def mul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def sym_table(q, a, b):
    """exponent table x mod q -> e with (x/pi)_6 = zeta6^e (ZERO if q | x), pi = a + b w, w -> r mod q."""
    r = (-a * pow(b, -1, q)) % q
    f = sdn.exponent_table((q, "s", r))
    return r, f


random.seed(13102026)
split = [q for q in sdn.primes_upto(400) if q % 3 == 1][:40]
PR = []
for q in split:
    q = int(q)
    for (a, b) in primary_prime(q)[:1]:
        r, f = sym_table(q, a, b)
        PR.append(dict(q=q, pi=(a, b), r=r, f=f))

ZERO = sdn.ZERO


def chi_int(primes, x, j=1):
    """chi_g(x)^j for rational integer x, g = prod primes; 0 if not coprime."""
    tot = 0
    for p in primes:
        v = int(p["f"](np.array([x % p["q"]]), np.array([0]))[0])
        if v >= ZERO:
            return 0
        tot += v
    return cmath.exp(2j * math.pi * (j * tot % 6) / 6)


def chi_elt(primes, ka, kb, j=1):
    tot = 0
    for p in primes:
        v = int(p["f"](np.array([ka]), np.array([kb]))[0])
        if v >= ZERO:
            return 0
        tot += v
    return cmath.exp(2j * math.pi * (j * tot % 6) / 6)


def gen(primes):
    g = (1, 0)
    for p in primes:
        g = mul(g, p["pi"])
    return g


def gauss(primes, j, shift=complex(1, 0)):
    """N(g)^{-1/2} sum_{x mod g} chi_g(x)^j e(shift x / g); residues = rational integers mod N(g)."""
    N = 1
    for p in primes:
        N *= p["q"]
    ga, gb = gen(primes)
    gc = cx(ga, gb)
    s = 0j
    for x in range(N):
        c = chi_int(primes, x, j)
        if c != 0:
            s += c * e(shift * x / gc)
    return s / math.sqrt(N)


out = {}
# ---------------- C5 eq:gj ----------------
err_gj = 0.0
err_g23 = 0.0
cases = 0
for trial in range(60):
    k = random.randint(1, 3)
    ps = random.sample(PR[:25], k)
    if len({p["q"] for p in ps}) < k or math.prod(p["q"] for p in ps) > 60000:
        continue
    ga, gb = gen(ps)
    g = cx(ga, gb)
    alpha = g / abs(g)
    mu = (-1) ** k
    g1, g2, g3 = gauss(ps, 1), gauss(ps, 2), gauss(ps, 3)
    G = np.conj(chi_int(ps, 4)) * g3
    err_gj = max(err_gj, abs(g1 * g2 - mu * alpha * G))
    err_g23 = max(err_g23, abs(g2 ** 3 - mu * alpha))
    cases += 1
out["C5"] = dict(cases=cases, max_err_gamma1gamma2_eq_mu_alpha_G=err_gj, max_err_gamma2cubed_eq_mu_alpha=err_g23)

# ---------------- C6 mu(g)1_{g|k} = sum_{d|g} mu(g/d) chi_d(k)^6 ----------------
bad = 0
n6 = 0
ndiv = 0
for trial in range(400):
    k = random.randint(0, 3)
    ps = random.sample(PR, k)
    ka, kb = random.randint(-300, 300), random.randint(-300, 300)
    if (ka, kb) == (0, 0):
        continue
    if ps and random.random() < 0.4:
        # force divisibility by multiplying by the generator of g
        m = gen(ps)
        ka, kb = mul((ka % 7 + 1, kb % 5), m)
    divides = all(chi_elt([p], ka, kb) == 0 for p in ps)
    lhs = ((-1) ** len(ps)) * (1 if divides else 0)
    rhs = 0
    for r in range(len(ps) + 1):
        for d in itertools.combinations(ps, r):
            c6 = chi_elt(list(d), ka, kb, 6)
            rhs += ((-1) ** (len(ps) - r)) * (1 if abs(c6) > 0.5 else 0)
    bad += int(lhs != rhs)
    ndiv += int(divides and len(ps) > 0)
    n6 += 1
assert bad == 0
out["C6"] = dict(cases=n6, cases_with_nontrivial_g_dividing_k=ndiv, failures=bad)

# ---------------- C7 shifted Gauss sums vanish on g | k ----------------
err_cop = 0.0
max_on_div = 0.0
nc7 = 0
for trial in range(30):
    k = random.randint(1, 2)
    ps = random.sample(PR[:20], k)
    if len({p["q"] for p in ps}) < k or math.prod(p["q"] for p in ps) > 20000:
        continue
    ga, gb = gen(ps)
    for j in range(1, 6):
        gj = gauss(ps, j)
        # coprime shift
        while True:
            ka, kb = random.randint(-50, 50), random.randint(-50, 50)
            if (ka, kb) != (0, 0) and chi_elt(ps, ka, kb) != 0:
                break
        sh = gauss(ps, j, cx(ka, kb))
        err_cop = max(err_cop, abs(sh - np.conj(chi_elt(ps, ka, kb, j)) * gj))
        # shift divisible by g
        ma, mb = mul((random.randint(1, 9), random.randint(0, 9)), (ga, gb))
        shd = gauss(ps, j, cx(ma, mb))
        max_on_div = max(max_on_div, abs(shd))
        nc7 += 1
out["C7"] = dict(cases=nc7, max_err_coprime_shift=err_cop, max_abs_on_g_divides_k=max_on_div)

# ---------------- C8 Ramanujan sums: principal Gauss sum = mu ----------------
err_ram = 0.0
err_abs = 0.0
nc8 = 0
for trial in range(30):
    k = random.randint(1, 3)
    ps = random.sample(PR[:20], k)
    if len({p["q"] for p in ps}) < k or math.prod(p["q"] for p in ps) > 30000:
        continue
    N = math.prod(p["q"] for p in ps)
    ga, gb = gen(ps)
    gcx = cx(ga, gb)
    for _ in range(3):
        ua, ub = random.randint(-40, 40), random.randint(-40, 40)
        if random.random() < 0.4:
            ua, ub = mul((ua % 5 + 1, ub % 3), gen(random.sample(ps, random.randint(1, k))))
        u = cx(ua, ub)
        c = 0j
        for x in range(N):
            if chi_int(ps, x) != 0:
                c += e(u * x / gcx)
        # closed form sum_{e | (g,u)} mu(g/e) N(e)
        cf = 0
        for r in range(k + 1):
            for sub in itertools.combinations(ps, r):
                if all(chi_elt([p], ua, ub) == 0 for p in sub):
                    Ne = math.prod(p["q"] for p in sub)
                    cf += ((-1) ** (k - r)) * Ne
        err_ram = max(err_ram, abs(c - cf))
        nc8 += 1
    # u = 1 and the second absorption
    c1 = sum(e(complex(x, 0) / gcx) for x in range(N) if chi_int(ps, x) != 0)
    mu = (-1) ** k
    alpha = gcx / abs(gcx)
    G = np.conj(chi_int(ps, 4)) * gauss(ps, 3)
    err_abs = max(err_abs, abs(c1 - mu), abs(np.conj(alpha * G) * gauss(ps, 1) * gauss(ps, 2) - c1))
out["C8"] = dict(cases=nc8, max_err_ramanujan_closed_form=err_ram,
                 max_err_c_g_1_eq_mu_eq_conj_alphaG_gamma1_gamma2=err_abs)

with open(sys.argv[1], "w") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps(out, indent=1))
