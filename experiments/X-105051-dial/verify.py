#!/usr/bin/env python3
"""Lane A3 verify.py — machine checks for the graded dial theorem T-105051.

Sections:
  1 exact arithmetic identities (Fractions): eta*eta=1, a*a*mu = h*h = b*b*1, Vaughan.
  2 sympy: kernel Mellin algebra (hat A_- hat A_+ = hat K_1, notch zeros).
  3 numerics: A_+ = A_- - 2T A_-; Mellin transforms; K_1 closed form vs numeric Mellin;
    Type-I decay; W_1 = T_U + B_U; B_U field-factorization; |B_U| <= 3 H_U;
    zeta(sigma)<0 on (1/2,1).
  4 empirical gate-energy exponent scan (dyadic blocks), written to results.json.
"""
import json, math, sys, time
from fractions import Fraction
import numpy as np

OUT = {}
SQRT2 = math.sqrt(2.0)

def sieve_spf(N):
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i][spf[i::i] == 0] = i
    return spf

def mobius(N, spf):
    mu = np.ones(N + 1, dtype=np.int64)
    for n in range(2, N + 1):
        p = spf[n]; m = n // p
        mu[n] = 0 if m % p == 0 else -mu[m]
    mu[0] = 0
    return mu

# ---------- 1. exact identities ----------
def eta_exact(N):
    from math import comb
    spf = sieve_spf(N)
    eta = [Fraction(0)] * (N + 1); eta[1] = Fraction(1)
    for n in range(2, N + 1):
        p = int(spf[n]); k = 0; m = n
        while m % p == 0: m //= p; k += 1
        rest = n // p**k
        etapk = Fraction(comb(2 * k, k), 4**k)
        eta[n] = etapk * eta[rest] if rest > 1 else etapk
    return eta

def dconv(a, b, N):
    c = [Fraction(0)] * (N + 1)
    for d in range(1, N + 1):
        if a[d] == 0: continue
        for m in range(1, N // d + 1):
            if b[m]: c[d * m] += a[d] * b[m]
    return c

def section1(N=400):
    spf = sieve_spf(N); mu = mobius(N, spf)
    eta = eta_exact(N)
    one = [Fraction(0)] + [Fraction(1)] * N
    ee = dconv(eta, eta, N)
    assert ee[1:] == one[1:], "eta*eta != 1"
    muf = [Fraction(int(m)) for m in mu]
    for U in (3, 10):
        bU = [Fraction(0)] * (N + 1)
        muU = [Fraction(0)] * (N + 1)
        for n in range(1, N + 1):
            (bU if n > U else muU).__setitem__(n, muf[n])
        aU = dconv(muU, one, N)
        aU = [-x for x in aU]; aU[1] += 1  # eps - mu_U*1
        assert all(aU[n] == 0 for n in range(1, U + 1)), "a_U(n)!=0 for n<=U"
        hU = dconv(bU, eta, N)
        lhs = dconv(dconv(aU, aU, N), muf, N)
        mid = dconv(hU, hU, N)
        rhs = dconv(dconv(bU, bU, N), one, N)
        assert lhs[1:] == mid[1:] == rhs[1:], "a*a*mu != h*h != b*b*1"
        # Vaughan: mu = 2 mu_U - mu_U*mu_U*1 + a_U*a_U*mu
        vau = [2 * muU[n] for n in range(N + 1)]
        t2 = dconv(dconv(muU, muU, N), one, N)
        for n in range(1, N + 1): vau[n] += -t2[n] + lhs[n]
        assert vau[1:] == muf[1:], "Vaughan identity fails"
    OUT["sec1_exact_identities"] = "PASS (N=%d, U in {3,10})" % N
    print(OUT["sec1_exact_identities"])

# ---------- 2. sympy Mellin algebra ----------
def section2():
    import sympy as sp
    s = sp.symbols('s')
    tw = 2 ** (-s)
    hatA = (1 - tw) * (1 - sp.sqrt(2) * tw) / (s * (s - sp.Rational(1, 2)))
    hatAm = (s - sp.Rational(1, 2)) * hatA
    hatAp = (s + sp.Rational(3, 2)) * hatA
    hatK1 = (1 - sp.sqrt(2) * tw) ** 2 * (1 - tw) ** 2 * (s + sp.Rational(3, 2)) / (s ** 2 * (s - sp.Rational(1, 2)))
    assert sp.simplify(hatAm * hatAp - hatK1) == 0, "hatA_- hatA_+ != hatK_1"
    # piecewise Mellin of A_- and A_+ agree with formulas
    y = sp.symbols('y', positive=True)
    Am = sp.Piecewise((1, (y > 1) & (y < 2)), (-sp.sqrt(2), (y > 2) & (y < 4)), (0, True))
    Ap = sp.Piecewise((4 * sp.sqrt(y) - 3, (y > 1) & (y < 2)),
                      (sp.sqrt(2) * (3 - 2 * sp.sqrt(y)), (y > 2) & (y < 4)), (0, True))
    Mm = sp.integrate(Am * y ** (-s - 1), (y, 1, 4))
    Mp = sp.integrate(Ap * y ** (-s - 1), (y, 1, 4))
    chk = [sp.simplify((Mm - hatAm).subs(s, v)) for v in (sp.Rational(3, 4), 2)]
    assert all(sp.nsimplify(c) == 0 or abs(complex(c)) < 1e-12 for c in chk), "Mellin A_- mismatch"
    chk = [complex((Mp - hatAp).subs(s, v).evalf()) for v in (sp.Rational(3, 4), 2)]
    assert all(abs(c) < 1e-10 for c in chk), "Mellin A_+ mismatch"
    # notch: hat A_-(1/2)=0, hat K_1(1/2)=0 (limit), zeros of hatK1 in Re s>0 on Re s=1/2 only
    assert sp.simplify(hatAm.subs(s, sp.Rational(1, 2))) == 0
    lim = sp.limit(hatK1 * 1, s, sp.Rational(1, 2))
    assert lim == 0, "hatK1(1/2) limit != 0 -> %s" % lim
    OUT["sec2_sympy_mellin"] = "PASS"
    print(OUT["sec2_sympy_mellin"])

# ---------- 3 helpers: exact-analytic K_1 ----------
# pieces (const c0 + c1*sqrt(w)): A_-: [(1,2,1,0),(2,4,-SQRT2,0)]
# A_+: [(1,2,-3,4),(2,4,3*SQRT2,-2*SQRT2)]
AM_P = [(1.0, 2.0, 1.0, 0.0), (2.0, 4.0, -SQRT2, 0.0)]
AP_P = [(1.0, 2.0, -3.0, 4.0), (2.0, 4.0, 3 * SQRT2, -2 * SQRT2)]

def _blk(x, al, be, a, b, c, d):
    # int_{al}^{be} (a + b sqrt(y)) (c + d sqrt(x/y)) dy/y
    if be <= al: return 0.0
    sx = math.sqrt(x); L = math.log(be / al)
    return (a * c * L + a * d * sx * (-2.0) * (be ** -0.5 - al ** -0.5)
            + b * c * 2.0 * (math.sqrt(be) - math.sqrt(al)) + b * d * sx * L)

def K1(x):
    if x <= 1.0 or x >= 16.0: return 0.0
    tot = 0.0
    for (l1, h1, a, b) in AM_P:
        for (l2, h2, c, d) in AP_P:
            al = max(l1, x / h2); be = min(h1, x / l2)
            tot += _blk(x, al, be, a, b, c, d)
    return tot

def Am(y):
    return 1.0 if 1 < y < 2 else (-SQRT2 if 2 < y < 4 else 0.0)

def Ap(y):
    if 1 < y < 2: return 4 * math.sqrt(y) - 3
    if 2 < y < 4: return SQRT2 * (3 - 2 * math.sqrt(y))
    return 0.0

def hatK1_formula(s):
    tw = 2.0 ** (-s) if not isinstance(s, complex) else np.exp(-s * math.log(2))
    return (1 - SQRT2 * tw) ** 2 * (1 - tw) ** 2 * (s + 1.5) / (s * s * (s - 0.5))

def section3():
    # (a) Hardy relation A_+ = A_- - 2 T A_- pointwise (numeric integral)
    for y in (1.3, 1.9, 2.5, 3.7):
        u = math.log(y)
        ts = np.linspace(0, 25, 400001)
        vals = np.exp(-ts / 2) * np.array([Am(math.exp(u + t)) for t in ts])
        TAm = np.trapezoid(vals, ts)
        lhs = Ap(y); rhs = Am(y) - 2 * TAm
        assert abs(lhs - rhs) < 2e-3, (y, lhs, rhs)
    # multiplier sup = 3 at xi=0
    xi = np.linspace(-50, 50, 10001)
    mod2 = (2.25 + xi ** 2) / (0.25 + xi ** 2)
    assert abs(mod2.max() - 9.0) < 1e-6
    # (b) K1 closed form: support, numeric Mellin vs formula, vanishing 3/2-moment
    xs = np.exp(np.linspace(math.log(1.0001), math.log(15.9999), 200001))
    k1v = np.array([K1(x) for x in xs])
    for sv in (0.75, 1.5, 2.0 + 0.7j):
        num = np.trapezoid(k1v * xs ** (-sv - 1), xs)
        assert abs(num - hatK1_formula(sv)) < 5e-4 * (1 + abs(hatK1_formula(sv))), (sv, num, hatK1_formula(sv))
    m32 = np.trapezoid(k1v * xs ** (-1.5 - 1), xs)  # hatK1(3/2)?? no: moment int K1 y^{-3/2} dy = hatK1(1/2)
    m_half = np.trapezoid(k1v * xs ** (-0.5 - 1), xs)
    assert abs(m_half) < 1e-4, m_half  # hatK1(1/2)=0
    OUT["sec3_kernel"] = "PASS (K1 supp [1,16], Mellin matches, hatK1(1/2)=0 numerically %.2e)" % m_half
    print(OUT["sec3_kernel"])
    # (c) Type-I decay: |sum m^{-1/2} K1(Y/m)| * Y^{3/2} bounded
    dec = {}
    for Y in (10.0, 100.0, 1000.0, 5000.0):
        S = sum(K1(Y / m) / math.sqrt(m) for m in range(max(1, int(Y / 16)), int(Y) + 1))
        dec[Y] = S * Y ** 1.5
    OUT["sec3_typeI_scaled"] = {str(k): v for k, v in dec.items()}
    assert max(abs(v) for v in dec.values()) < 50.0, dec
    print("sec3 Type-I scaled residuals (should be O(1)):", dec)
    # (d) exact-coefficient objects at moderate size
    N = 4096; spf = sieve_spf(N); mu = mobius(N, spf)
    eta = np.zeros(N + 1)
    from math import comb
    eta[1] = 1.0
    for n in range(2, N + 1):
        p = int(spf[n]); k = 0; m = n
        while m % p == 0: m //= p; k += 1
        eta[n] = (comb(2 * k, k) / 4 ** k) * (eta[n // p ** k] if n // p ** k > 1 else 1.0)
    def h_of(U, Nn):
        h = np.zeros(Nn + 1)
        for d in range(U + 1, Nn + 1):
            if mu[d]:
                h[d::d] += mu[d] * eta[1:Nn // d + 1]
        return h
    X = 2000.0; U = 12  # floor(2000^{1/3}) = 12
    Nn = int(X)  # need a*a*mu up to X
    h = h_of(U, Nn)
    # B via h*h trilinear with exact K1
    hh = np.zeros(Nn + 1)
    for m in range(U + 1, Nn + 1):
        if h[m]:
            top = Nn // m
            if top > U:
                hh[m * (U + 1):: 1]  # noop guard
            for n in range(U + 1, top + 1):
                if h[n]: hh[m * n] += h[m] * h[n]
    B_tri = sum(hh[n] / math.sqrt(n) * K1(X / n) for n in range(1, Nn + 1) if hh[n])
    # B via field integral (fine log-grid Simpson)
    def Hm(Y):
        lo, hi = int(Y / 4), int(Y)
        return sum(h[n] / math.sqrt(n) * Am(Y / n) for n in range(max(1, lo), min(Nn, hi) + 1) if h[n])
    def Hp(Y):
        lo, hi = int(Y / 4), int(Y)
        return sum(h[n] / math.sqrt(n) * Ap(Y / n) for n in range(max(1, lo), min(Nn, hi) + 1) if h[n])
    M = 20001
    lg = np.linspace(math.log(U), math.log(X / U), M)
    Ys = np.exp(lg)
    vals = np.array([Hm(Yv) * Hp(X / Yv) for Yv in Ys])
    B_field = np.trapezoid(vals, lg)
    OUT["sec3_B_two_ways"] = {"B_trilinear": B_tri, "B_field_integral": float(B_field),
                              "rel_err": abs(B_tri - B_field) / max(1e-12, abs(B_tri))}
    assert OUT["sec3_B_two_ways"]["rel_err"] < 2e-2, OUT["sec3_B_two_ways"]
    print("sec3 B two ways:", OUT["sec3_B_two_ways"])
    # (e) |B| <= 3 H  (H via exact stepfunction sweep)
    HU = gate_energy_exact(h, U, X, Nn)
    ht = h.copy(); ht[int(X / U) + 1:] = 0.0
    HUt = gate_energy_exact(ht, U, X, Nn)   # truncated-field energy H~ (rigorous gate object)
    OUT["sec3_B_le_3H"] = {"absB": abs(B_tri), "3H": 3 * HU, "3Htrunc": 3 * HUt,
                           "ok_untrunc": bool(abs(B_tri) <= 3 * HU),
                           "ok_trunc": bool(abs(B_tri) <= 3 * HUt)}
    assert abs(B_tri) <= 3 * HUt
    print("sec3 |B|<=3H:", OUT["sec3_B_le_3H"])
    # (f) W_1 = T_U + B_U
    W1 = sum(mu[n] / math.sqrt(n) * K1(X / n) for n in range(1, Nn + 1) if mu[n])
    TU = 0.0
    for a in range(1, U + 1):
        if not mu[a]: continue
        for b in range(1, U + 1):
            if not mu[b]: continue
            ab = a * b
            TU -= mu[a] * mu[b] / math.sqrt(ab) * sum(
                K1(X / (ab * m)) / math.sqrt(m) for m in range(max(1, int(X / (16 * ab))), int(X / ab) + 1))
    OUT["sec3_vaughan_W1"] = {"W1": W1, "T+B": TU + B_tri, "abs_err": abs(W1 - (TU + B_tri))}
    assert abs(W1 - (TU + B_tri)) < 1e-8 * max(1.0, abs(W1)), OUT["sec3_vaughan_W1"]
    print("sec3 W1 = T + B:", OUT["sec3_vaughan_W1"])
    # (g) zeta(sigma)<0 on (1/2,1)
    import mpmath as mp
    zs = [float(mp.zeta(sig)) for sig in (0.6, 0.75, 0.9, 0.99)]
    assert all(z < 0 for z in zs), zs
    OUT["sec3_zeta_negative_on_strip"] = zs
    print("sec3 zeta(sigma) on (1/2,1):", zs)

def gate_energy_exact(h, U, X, Nn):
    """H_U(X) = int_U^{4X/U} |H_{U,-}|^2 dY/Y, exact for the step field (float)."""
    Z = 4.0 * X / U
    top = int(math.floor(Z))
    NE = min(Nn, top)  # n with any window intersecting [.., Z]: n < Z
    add = np.zeros(4 * NE + 2)
    n = np.arange(1, NE + 1, dtype=np.int64)
    v = h[1:NE + 1] / np.sqrt(n)
    np.add.at(add, n, v)
    np.add.at(add, np.minimum(2 * n, 4 * NE + 1), -(1 + SQRT2) * v * (2 * n <= 4 * NE + 1))
    np.add.at(add, np.minimum(4 * n, 4 * NE + 1), SQRT2 * v * (4 * n <= 4 * NE + 1))
    F = np.cumsum(add)  # F[y] = field on (y, y+1)
    ymax = min(len(F) - 1, top)
    ys = np.arange(U, ymax)
    w = np.log((ys + 1.0) / ys)
    E = float(np.sum(F[ys] ** 2 * w))
    if top < Z and top < len(F):
        E += F[top] ** 2 * math.log(Z / top)
    return E

# ---------- 4. empirical gate exponent ----------
def section4(Lmin=8, Lmax=21, nsamp=8):
    from math import comb
    rng = np.random.default_rng(7)
    rows = []
    for L in range(Lmin, Lmax + 1):
        t0 = time.time()
        us = (np.arange(nsamp) + 0.5) / nsamp
        Xs = 2.0 ** (L + us)
        Hs = []; Hts = []
        for X in Xs:
            U = int(X ** (1.0 / 3.0))
            Nn = int(4 * X / U) + 1
            spf = sieve_spf(Nn); mu = mobius(Nn, spf)
            eta = np.zeros(Nn + 1); eta[1] = 1.0
            for nn in range(2, Nn + 1):
                p = int(spf[nn]); k = 0; m = nn
                while m % p == 0: m //= p; k += 1
                eta[nn] = (comb(2 * k, k) / 4 ** k) * (eta[nn // p ** k] if nn // p ** k > 1 else 1.0)
            h = np.zeros(Nn + 1)
            for d in range(U + 1, Nn + 1):
                if mu[d]:
                    h[d::d] += mu[d] * eta[1:Nn // d + 1]
            Hs.append(gate_energy_exact(h, U, X, Nn))
            ht = h.copy(); ht[int(X / U) + 1:] = 0.0
            Hts.append(gate_energy_exact(ht, U, X, Nn))
        blk = float(np.mean(Hs) * math.log(2.0))
        blkt = float(np.mean(Hts) * math.log(2.0))
        rows.append({"L": L, "block_integral": blk, "block_integral_trunc": blkt,
                     "mean_H": float(np.mean(Hs)), "mean_Htrunc": float(np.mean(Hts)),
                     "H_over_X13": [float(Hv / Xv ** (1 / 3)) for Hv, Xv in zip(Hs, Xs)],
                     "secs": round(time.time() - t0, 1)})
        print("L=%d block=%.4g  block_trunc=%.4g  mean H/X^(1/3)=%.4g  (%.1fs)" % (
            L, blk, blkt, np.mean(rows[-1]["H_over_X13"]), rows[-1]["secs"]))
        sys.stdout.flush()
    Ls = np.array([r["L"] for r in rows], dtype=float)
    A = np.vstack([Ls, np.ones_like(Ls)]).T
    hi = Ls >= (Lmin + Lmax) // 2
    fits = {}
    for key in ("block_integral", "block_integral_trunc"):
        lb = np.log2([r[key] for r in rows])
        fits[key] = {"all": float(np.linalg.lstsq(A, lb, rcond=None)[0][0]),
                     "upper_half": float(np.linalg.lstsq(A[hi], lb[hi], rcond=None)[0][0])}
    OUT["sec4_gate_scan"] = {"rows": rows, "fit_exponents": fits,
                             "reference": "1/3 = 0.3333 (converse floor), 2/3 trivial"}
    print("empirical gate exponents:", fits)

if __name__ == "__main__":
    t0 = time.time()
    section1()
    section2()
    section3()
    args = sys.argv[1:]
    Lmax = int(args[0]) if args else 21
    section4(Lmax=Lmax)
    OUT["total_seconds"] = round(time.time() - t0, 1)
    with open(__file__.replace("verify.py", "results.json"), "w") as f:
        json.dump(OUT, f, indent=1, default=float)
    print("WROTE results.json  (%.1fs total)" % OUT["total_seconds"])
