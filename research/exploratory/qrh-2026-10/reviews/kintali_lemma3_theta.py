"""kintali_lemma3_theta.py -- numerical test of the cubic-theta inputs used in Kintali App. B.

Label: FLOATING_RECONNAISSANCE (double precision; truncated Bessel series; not certified).

Inputs implemented verbatim from Dunn-Radziwill, arXiv:2109.07463v3 (DR):
  (5.1) action of SL2(C) on H^3; (5.4) Kubota character chi(g) = (c/a)_3 on Gamma_1(3), c != 0;
  (5.6)-(5.8) theta(z,v) = sigma v^{2/3} + sum_{mu in lambda^-3 O} tau(mu) v K_{1/3}(4 pi|mu|v) ech(mu z);
  (5.13)-(5.14) tau_1, tau_2; Appendix A table: d_10(mu) = w tau_2(w mu) ech(mu),
  d_19(mu) = w^2 tau_1(w^2 mu) ech(mu); (5.9) F_j = theta o gamma_j, gamma_10 = L(w), gamma_19 = L(w^2).
  g(r, c) = sum_{d mod c} (d/c)_3 ech(r d / c)  (Patterson's Gauss sum; g(1, c) = DR's g(c)).

Tests:
  T0  Gauss-sum plumbing: prime sums vs direct sums; twisted multiplicativity and g(r,c) = conj((r/c)_3) g(c)
      on small composite c (direct sums).  |g~(c)| = 1 for squarefree c.
  T1  automorphy theta(gw) = chi(g) theta(w) for g in Gamma_1(3) (and the alternative conj chi(g)).
  T2  cusp expansions: theta(L(w) w) = F_10, theta(L(w^2) w) = F_19 (DR table), and Kintali's
      identification theta(L(lambda) w) = F_19, theta(L(-lambda) w) = F_10.
  T3  Kintali App. B "derivative and reflected local characters": for rational cusps a/c built by
      Kintali's recipe (three lambda-cases), compare
          LHS = d/dzbar conj(theta)(a/c + z, v) at z = 0           (from the expansion at infinity)
          RHS = conj(kappa(k_g)) * (-(c v)^-2) * sum_mu d_H(mu) 2 pi i mu v' K(4 pi|mu| v') ech(-mu delta/c)
      with d_H(mu) = conj(d_j(-mu)), v' = 1/(q_c v), H chosen by Kintali, kappa(k_g) from (5.4) directly,
      and compare kappa(k_g) with Kintali's closed form (B.2) (exact symbols).
      Also the undifferentiated identity conj theta(w) = conj kappa(k_g) conj theta(H g^-1 w).

Run:  python3 -I kintali_lemma3_theta.py OUT.json
"""
import cmath
import json
import math
import os
import sys
import time

import numpy as np
from scipy.special import kv

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kintali_lemma3_common as K  # noqa: E402

SQ3 = math.sqrt(3.0)
SIGMA = 3 ** 2.5 / 2
LAM3_C = K.to_c(K.power(K.LAM, 3))      # lambda^3 = -3 sqrt(-3)
LAM4_C = K.to_c(K.power(K.LAM, 4))      # 9
W = K.OMEGA
PH = {0: 1.0, 1: cmath.exp(-2j * math.pi / 9), 2: cmath.exp(2j * math.pi / 9)}
T_CUT = 26.0                             # Bessel argument cut-off: K_{1/3}(y) ~ e^{-y}

# ---------------------------------------------------------------- Gauss sums
_G1 = {}


def g_prime_direct(p, r=(1, 0)):
    """g(r, p) = sum_{d mod p} (d/p)_3 ech(r d/p) for a prime element p (not above 3), direct sum."""
    s = 0j
    for d in K.residues(p):
        k = K.cubic_code(d, p)
        if k is None:
            continue
        s += K.omega_pow(k) * cmath.exp(2j * math.pi * float(K.frac_ech_coord(K.mul(r, d), p)))
    return s


def g_prime_fast(p):
    """g(1, p) with numpy, for split p (O/p = Z/N), inert p and p = -2."""
    N = K.norm(p)
    if N % 3 == 1 and sympy_isprime(N):           # split: residues 0..N-1 are integers
        d = np.arange(1, N, dtype=np.int64)
        t = np.ones_like(d)
        b = d.copy()
        e = (N - 1) // 3
        while e:
            if e & 1:
                t = (t * b) % N
            b = (b * b) % N
            e >>= 1
        # images of 1, w, w^2 in Z/N: w = root r with p | (w - r)
        import sympy
        s3 = sympy.sqrt_mod(-3 % N, N)
        r = None
        for cand in (((-1 + s3) * pow(2, -1, N)) % N, ((-1 - s3) * pow(2, -1, N)) % N):
            if K.divides(p, (-cand, 1)):
                r = cand
        assert r is not None
        code = np.full(d.shape, -1)
        code[t == 1] = 0
        code[t == r] = 1
        code[t == (r * r) % N] = 2
        assert (code >= 0).all()
        tr = K.frac_ech_coord((1, 0), p)          # Tr(1/p), exact
        ph = np.exp(2j * np.pi * ((d * tr.numerator) % tr.denominator) / tr.denominator)
        return complex(np.sum(np.exp(2j * np.pi * code / 3) * ph))
    return g_prime_direct(p)


def sympy_isprime(n):
    import sympy
    return sympy.isprime(n)


def g1(c_fac):
    """g(1, c) for squarefree primary c given as a tuple of primary prime elements (twisted mult.)."""
    key = tuple(sorted(c_fac))
    if key in _G1:
        return _G1[key]
    if len(key) == 0:
        val = 1.0 + 0j
    elif len(key) == 1:
        val = g_prime_fast(key[0])
    else:
        a = key[:-1]
        b = key[-1]
        ae = (1, 0)
        for p in a:
            ae = K.mul(ae, p)
        # DR (2.?) twisted multiplicativity: g(ab) = conj((a/b)_3) g(a) g(b) for coprime a, b
        k = K.cubic_code(ae, b)
        val = np.conj(K.omega_pow(k)) * g1(a) * g1((b,))
    _G1[key] = val
    return val


def g_r(r, c_fac):
    """g(r, c) = conj((r/c)_3) g(1, c) for r prime to c (r = unit * lambda^2)."""
    ce = (1, 0)
    for p in c_fac:
        ce = K.mul(ce, p)
    k = 0
    for p in c_fac:
        k += K.cubic_code(r, p)
    return np.conj(K.omega_pow(k % 3)) * g1(c_fac)


def g_direct_composite(r, c):
    s = 0j
    for d in K.residues(c):
        k = K.cubic_symbol(d, c)
        if k is None:
            continue
        s += K.omega_pow(k) * cmath.exp(2j * math.pi * float(K.frac_ech_coord(K.mul(r, d), c)))
    return s


# ---------------------------------------------------------------- coefficients
def unit_index(u):
    """u = +-w^i -> i."""
    k = K.UNITS.index(u)
    return {0: 0, 3: 0, 2: 1, 5: 1, 4: 2, 1: 2}[k], (1 if k in (0, 2, 4) else -1)


def cube_split(y):
    """y primary -> (c_fac tuple, |d|, |c|) with y = c d^3, c squarefree, or None."""
    u, fac = K.factor(y)
    cf, dabs2, cabs2 = [], 1, 1
    for p, e in fac:
        if e % 3 == 2:
            return None
        if e % 3 == 1:
            cf.append(p)
            cabs2 *= K.norm(p)
        dabs2 *= K.norm(p) ** (e // 3)
    return tuple(cf), math.sqrt(dabs2), math.sqrt(cabs2)


def tau_of_x(x):
    """tau(mu) for mu = x / lambda^3 (DR (5.7))."""
    v, w = K.lam_val(x)
    if v % 3 == 1:
        return 0j
    u, y = K.primary(w)
    i, sgn = unit_index(u)
    cs = cube_split(y)
    if cs is None:
        return 0j
    cf, dab, cab = cs
    if v % 3 == 0:
        if i != 0:
            return 0j
        n = v // 3
        return np.conj(g1(cf)) * dab / cab * 3 ** (n / 2 + 2.5)
    n = (v + 1) // 3
    r = K.mul(K.power((0, 1), i), K.power(K.LAM, 2))
    return PH[i] * np.conj(g_r(r, cf)) * dab / cab * 3 ** (n / 2 + 2)


def tau12_of_xp(xp, which):
    """tau_1 or tau_2 at nu = xp / lambda^4 (DR (5.13), (5.14))."""
    v, w = K.lam_val(xp)
    if v != 0:
        return 0j
    u, y = K.primary(w)
    i, sgn = unit_index(u)
    if (which == 1 and sgn != 1) or (which == 2 and sgn != -1):
        return 0j
    cs = cube_split(y)
    if cs is None:
        return 0j
    cf, dab, cab = cs
    r = K.mul(K.power((0, 1), i), K.power(K.LAM, 2))
    gb = np.conj(g_r(r, cf))
    if which == 1:
        pre = {0: 9 * W, 1: 9 * PH[1] * W ** 2, 2: 9 * PH[2]}[i]
    else:
        pre = {0: 9 * W ** 2, 1: 9 * PH[1], 2: 9 * W * PH[2]}[i]
    return pre * gb * dab / cab


def d_j_of_xp(xp, j):
    """d_j(mu) at mu = xp / lambda^4 for j in {1, 10, 19} (DR Appendix A table)."""
    mu = K.to_c(xp) / LAM4_C
    if j == 1:
        # mu in lambda^-3 O iff lambda | xp
        if not K.divides(K.LAM, xp):
            return 0j
        return tau_of_x(K.exact_div(xp, K.LAM))
    if j == 10:
        return W * tau12_of_xp(K.mul((0, 1), xp), 2) * K.ech(mu)
    if j == 19:
        return W ** 2 * tau12_of_xp(K.mul((-1, -1), xp), 1) * K.ech(mu)
    raise ValueError(j)


# ---------------------------------------------------------------- series
class Series:
    """sum_{x in O, 0 < N x <= X} coef(x) v K_{1/3}(4 pi |x/den| v) ech((x/den) z)."""

    def __init__(self, den_c, coef_fn, X):
        pts = K.lattice(X)
        coefs = np.array([coef_fn(x) for x in pts], dtype=complex)
        keep = np.abs(coefs) > 0
        self.mu = np.array([K.to_c(x) for x in pts], dtype=complex)[keep] / den_c
        self.coef = coefs[keep]
        self.X = X

    def value(self, z, v):
        a = np.abs(self.mu)
        return np.sum(self.coef * v * kv(1 / 3, 4 * np.pi * a * v) * np.exp(4j * np.pi * (self.mu * z).real))

    def dz(self, z, v):
        """d/dz (holomorphic Wirtinger) of the series: brings down 2 pi i mu."""
        a = np.abs(self.mu)
        return np.sum(self.coef * 2j * np.pi * self.mu * v * kv(1 / 3, 4 * np.pi * a * v)
                      * np.exp(4j * np.pi * (self.mu * z).real))

    def min_tail_arg(self, v):
        # smallest Bessel argument among omitted terms
        return 4 * np.pi * math.sqrt(self.X) / abs(self.den_abs) * v if hasattr(self, "den_abs") else None


def X_for(den_abs, v):
    """lattice norm bound so that omitted terms have Bessel argument >= T_CUT."""
    return int((den_abs * T_CUT / (4 * math.pi * v)) ** 2) + 1


def act(g, z, v):
    """DR (5.1): g = ((a,b),(c,d)) with complex entries."""
    (a, b), (c, d) = g
    den = abs(c * z + d) ** 2 + abs(c) ** 2 * v * v
    zz = ((a * z + b) * np.conj(c * z + d) + a * np.conj(c) * v * v) / den
    return zz, v / den


def cmat(g):
    return tuple(tuple(K.to_c(e) for e in row) for row in g)


def matmul(g, h):
    (a, b), (c, d) = g
    (e, f), (gg, hh) = h
    return ((K.add(K.mul(a, e), K.mul(b, gg)), K.add(K.mul(a, f), K.mul(b, hh))),
            (K.add(K.mul(c, e), K.mul(d, gg)), K.add(K.mul(c, f), K.mul(d, hh))))


def matinv(g):
    (a, b), (c, d) = g
    return ((d, K.neg(b)), (K.neg(c), a))


def kappa(g):
    """DR (5.4): (c/a)_3 for g in Gamma_1(3) with c != 0, else 1; returned as code mod 3."""
    (a, b), (c, d) = g
    for e, t in ((a, 1), (d, 1), (b, 0), (c, 0)):
        assert K.congruent(e, (t, 0), (3, 0)), ("not in Gamma_1(3)", g)
    if K.is_zero(c):
        return 0
    k = K.cubic_symbol(c, a)
    assert k is not None
    return k


# ---------------------------------------------------------------- main
def main(out):
    t0 = time.time()
    res = {"label": "FLOATING_RECONNAISSANCE", "T_CUT": T_CUT}
    # ---- T0 Gauss sums
    t0rows = []
    primes = K.primary_primes_upto(400, include_two=True)
    maxd = 0.0
    for p in primes[:40]:
        gd = g_prime_direct(p)
        gf = g_prime_fast(p)
        maxd = max(maxd, abs(gd - gf))
        assert abs(abs(gd) - math.sqrt(K.norm(p))) < 1e-8
    t0rows.append({"check": "prime g(1,p): numpy vs direct; |g| = sqrt(Np)", "primes": 40, "max_dev": maxd})
    maxd = 0.0
    cnt = 0
    small = [p for p in primes if K.norm(p) <= 61]
    for i in range(len(small)):
        for j in range(i + 1, len(small)):
            c = K.mul(small[i], small[j])
            if K.norm(c) > 1300:
                continue
            for r in [(1, 0), K.power(K.LAM, 2), K.mul((0, 1), K.power(K.LAM, 2)),
                      K.mul((-1, -1), K.power(K.LAM, 2))]:
                gd = g_direct_composite(r, c)
                gt = g_r(r, (small[i], small[j])) if r != (1, 0) else g1((small[i], small[j]))
                maxd = max(maxd, abs(gd - gt) / math.sqrt(K.norm(c)))
                cnt += 1
    t0rows.append({"check": "composite g(r,c), r in {1, w^i lambda^2}: direct vs twisted-mult + conj((r/c)_3)",
                   "cases": cnt, "max_rel_dev": maxd})
    res["T0"] = t0rows
    print("T0", t0rows, flush=True)

    # ---- theta series (expansion at infinity), built once for the smallest height needed
    vmin_inf = 0.085
    Xinf = X_for(abs(LAM3_C), vmin_inf)
    print("building theta series, X =", Xinf, flush=True)
    TH = Series(LAM3_C, tau_of_x, Xinf)
    print("theta terms", len(TH.coef), "t", round(time.time() - t0, 1), flush=True)

    def theta(z, v):
        assert v >= vmin_inf - 1e-12
        return SIGMA * v ** (2 / 3) + TH.value(z, v)

    # ---- T1 automorphy on Gamma_1(3)
    rng = np.random.default_rng(7)
    t1 = []
    cands = []
    for cc in [(3, 0), (0, 3), (3, 3), (-3, 6), K.mul((3, 0), K.LAM), (6, 3), (3, -3), (9, 3)]:
        for aa in [(1, 0), (4, 0), (1, 3), (-2, 0), (7, 3), (4, 6), (-5, -3), (1, -6), (10, 3)]:
            if not K.is_primary(aa):
                continue
            g_, s_, t_ = K.egcd(aa, K.mul(cc, (3, 0)))
            if K.norm(g_) != 1:
                continue
            dd = K.inv_mod(aa, K.mul(cc, (3, 0)))
            bb = K.exact_div(K.sub(K.mul(aa, dd), (1, 0)), cc)
            g = ((aa, bb), (cc, dd))
            cands.append(g)
    for g in cands[:14]:
        gc = cmat(g)
        (a, b), (c, d) = gc
        v = 1.0 / abs(c)
        z = -d / c + complex(rng.normal(0, 0.25), rng.normal(0, 0.25)) * v
        z2, v2 = act(gc, z, v)
        if min(v, v2) < vmin_inf:
            continue
        lhs = theta(z2, v2)
        rhs = theta(z, v)
        k = kappa(g)
        t1.append({"g": g, "kappa_code": k, "v": v, "v_img": v2,
                   "rel_dev_chi": abs(lhs - K.omega_pow(k) * rhs) / abs(lhs),
                   "rel_dev_conjchi": abs(lhs - np.conj(K.omega_pow(k)) * rhs) / abs(lhs)})
    res["T1"] = t1
    print("T1", [(r["kappa_code"], "%.1e" % r["rel_dev_chi"], "%.1e" % r["rel_dev_conjchi"]) for r in t1], flush=True)

    # ---- cusp series F_10, F_19 (mu in lambda^-4 O)
    vmin_cusp = 0.16
    Xc = X_for(abs(LAM4_C), vmin_cusp)
    print("building cusp series, X =", Xc, flush=True)
    pts = K.lattice(Xc)
    DJ = {j: {xp: d_j_of_xp(xp, j) for xp in pts} for j in (1, 10, 19)}
    F = {}
    for j in (10, 19):
        F[j] = Series(LAM4_C, lambda xp, j=j: DJ[j][xp], Xc)
    # conj expansions d_H(mu) = conj(d_j(-mu)) on lambda^-4 O (identity cusp included)
    DH = {}
    for j in (1, 10, 19):
        DH[j] = Series(LAM4_C, lambda xp, j=j: np.conj(DJ[j][K.neg(xp)]), Xc)
    print("cusp series built t", round(time.time() - t0, 1), flush=True)

    # ---- T2 cusp identification
    t2 = []
    Lm = lambda t: (((1, 0), (0, 0)), (t, (1, 0)))
    tests = [("L(w) -> F_10", (0, 1), 10), ("L(w^2) -> F_19", (-1, -1), 19),
             ("L(lambda) -> F_19 [Kintali]", K.LAM, 19), ("L(-lambda) -> F_10 [Kintali]", K.neg(K.LAM), 10),
             ("L(lambda) -> F_10 [alternative]", K.LAM, 10)]
    for name, t, j in tests:
        devs = []
        for _ in range(3):
            z = complex(rng.normal(0, 0.3), rng.normal(0, 0.3))
            v = 0.55
            z2, v2 = act(cmat(Lm(t)), z, v)
            lhs = theta(z2, v2)
            rhs = F[j].value(z, v)
            devs.append(abs(lhs - rhs) / abs(lhs))
        t2.append({"test": name, "max_rel_dev": max(devs)})
    res["T2"] = t2
    print("T2", t2, flush=True)

    # ---- T3 Kintali's reflected translate
    t3 = []
    lam = K.LAM
    p7 = [p for p in K.primary_primes_upto(7) if K.norm(p) == 7][0]
    p13 = [p for p in K.primary_primes_upto(13) if K.norm(p) == 13][0]
    p19 = [p for p in K.primary_primes_upto(19) if K.norm(p) == 19][0]
    p5 = K.primes_above(5)[0]                    # inert prime -5, norm 25
    base_list = [  # (c_F, a_F, prime list); z_h = a_F/c_F + lambda^2 sum h_p/p ; need q_c <= 67
        (K.power(lam, 2), (1, 0), [p7]), (K.power(lam, 2), (-2, 0), [p7]),
        (K.power(lam, 2), (1, 0), []), (K.power(lam, 3), (1, 0), []), (K.power(lam, 3), (4, 3), []),
        (lam, (1, 0), [p7]), (K.neg(lam), (1, 0), [p7]), (lam, (-2, 0), [p13]), (K.neg(lam), (4, 0), [p19]),
        ((1, 0), (0, 0), [p7]), ((1, 0), (1, 0), [p13]), ((1, 0), lam, [p19]), ((1, 0), (0, 1), [p5]),
        ((1, 0), (2, 1), [p7, (1, 0)][:1]), ((-2, 0), (1, 0), [p7]), ((-2, 0), (0, 1), [p13]),
    ]
    examples = []
    for (cF, aF, rl) in base_list:
        hl_opts = [[]] if not rl else [[h] for h in [(1, 0), (2, 0), (1, 1), (3, 0), (2, -1), (4, 1)]]
        for hl in hl_opts:
            if any(K.divides(p, h) for p, h in zip(rl, hl)):
                continue
            examples.append((cF, aF, rl, hl))
    M = K.mul(K.power(lam, 8), (4, 0))
    for (cF, aF, rl, hl) in examples:
        r = (1, 0)
        for p in rl:
            r = K.mul(r, p)
        a = K.mul(aF, r)
        for p, h in zip(rl, hl):
            a = K.add(a, K.mul(K.mul(K.power(lam, 2), cF), K.mul(K.exact_div(r, p), h)))
        c = K.mul(cF, r)
        if K.norm(K.egcd(a, c)[0]) != 1:
            print("skip non-reduced", cF, aF, rl, hl)
            continue
        vl = K.lam_val(c)[0]
        v2c = 0
        t_ = c
        while K.divides((2, 0), t_):
            t_ = K.exact_div(t_, (2, 0))
            v2c += 1
        # delta by Kintali's CRT recipe (with test modulus M = lambda^8 * 4)
        parts = []
        lam_mod = K.power(lam, 8 + vl)
        parts.append((K.inv_mod(a, lam_mod) if vl > 0 else (0, 0), lam_mod))
        two_mod = K.power((2, 0), 2 + v2c)
        parts.append((K.inv_mod(a, two_mod) if v2c > 0 else (0, 0), two_mod))
        for p in rl:
            parts.append((K.inv_mod(a, p), p))
        delta, MM = K.crt(parts)
        if K.is_zero(delta):
            delta = MM
        b0 = K.exact_div(K.sub(K.mul(a, delta), (1, 0)), c)
        g = ((a, b0), (c, delta))
        # H per Kintali
        if vl >= 2:
            case, H, j = 1, (((1, 0), (0, 0)), ((0, 0), (1, 0))), 1
            u0 = None
        elif vl == 1:
            case = 2
            u0 = lam if K.congruent(c, lam, (3, 0)) else K.neg(lam)
            assert K.congruent(c, u0, (3, 0))
            H = (((1, 0), (0, 0)), (u0, (1, 0)))
            j = 19 if u0 == lam else 10
        else:
            case = 3
            u0 = K.reduce_mod(a, (3, 0))
            H = ((u0, (-1, 0)), ((1, 0), (0, 0)))
            t_cls = (-u0[1]) % 3          # -u0 = s + t w ; class of t mod 3
            j = {0: 1, 1: 10, 2: 19}[t_cls]
        kg = matmul(g, matinv(H))
        kcode = kappa(kg)
        # Kintali (B.2) closed forms
        ar = 0
        for p in rl:
            ar += K.cubic_code(a, p)
        if case == 1:
            fixed = K.cubic_symbol(cF, a) if K.norm(a) > 1 else 0
        elif case == 2:
            A0 = K.sub(a, K.mul(u0, b0))
            cFu0 = K.exact_div(cF, u0)
            f1 = K.cubic_symbol(K.neg(u0), A0) if K.norm(A0) > 1 else 0
            f2 = K.cubic_symbol(cFu0, a) if K.norm(a) > 1 else 0
            fixed = (f1 + f2) % 3
        else:
            fixed = 0
            if K.norm(cF) > 1:
                _, fcF = K.factor(cF)
                for p, e in fcF:
                    fixed += e * K.cubic_code(a, p)
            fixed %= 3
        formula = (fixed + ar) % 3
        # numerics
        cc = K.to_c(c)
        qc = K.norm(c)
        v = math.sqrt(0.58 / qc)
        vp = 1.0 / (qc * v)
        if v < vmin_inf or vp < vmin_cusp:
            v = max(v, vmin_inf)
            vp = 1.0 / (qc * v)
        zc = K.to_c(a) / cc
        lhs = np.conj(TH.dz(zc, v))
        zprime = -K.to_c(delta) / cc
        ser = DH[j]
        rhs = np.conj(K.omega_pow(kcode)) * (-1.0 / (cc * cc * v * v)) * ser.dz(zprime, vp)
        # undifferentiated identity at a nearby point
        zz = zc + complex(0.13, -0.07) * v
        gi = matinv(g)
        z1, v1 = act(cmat(gi), zz, v)
        Hz, Hv = act(cmat(H), z1, v1)
        lhs0 = np.conj(theta(zz, v))
        sig = SIGMA * v1 ** (2 / 3) if j == 1 else 0.0
        rhs0 = np.conj(K.omega_pow(kcode)) * (sig + ser.value(z1, v1))
        t3.append({"c_F": cF, "a_F": aF, "r": r, "a": a, "c": c, "delta": delta, "b0": b0,
                   "case": case, "u0": u0, "cusp_j": j, "kappa_direct": kcode, "kappa_B2": formula,
                   "B2_match": kcode == formula, "v": v, "v_dual": vp,
                   "deriv_rel_dev": abs(lhs - rhs) / abs(lhs), "|lhs|": abs(lhs),
                   "value_rel_dev": abs(lhs0 - rhs0) / abs(lhs0),
                   "deriv_rel_dev_if_kappa_unconjugated":
                       abs(lhs - K.omega_pow(kcode) * (-1.0 / (cc * cc * v * v)) * ser.dz(zprime, vp)) / abs(lhs)})
        print("T3", case, j, kcode, formula, "%.2e" % t3[-1]["deriv_rel_dev"], "%.2e" % t3[-1]["value_rel_dev"],
              round(time.time() - t0, 1), flush=True)
    res["T3"] = t3
    res["seconds"] = time.time() - t0
    with open(out, "w") as fh:
        json.dump(res, fh, indent=1, default=str)
    print("done", round(time.time() - t0, 1))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "kintali_lemma3_theta.json")
