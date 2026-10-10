"""kintali_lemma3_finite.py -- finite / algebraic checks of Kintali App. B (and (8)), read from the
rendered PDF (pdftoppm -r 300), with the overbars as printed.

Labels:
  F1 FLOATING_RECONNAISSANCE  g~_3(c) = chi_c(lambda)^{-2} gamma_2(c), squarefree primary c prime to 6
  F2 FLOATING_RECONNAISSANCE  local mask C_{p,j}(h): four-case closed form, and Fourier inversion
                              sum_h C_{p,j}(h) e(hx/p) = chi_p(x)^j with Kintali's zero convention
  F3 EXACT                    additive CRT: ech(-delta mu/c) = theta(x) prod_p e(eps_p h_p^{-1} x/p),
                              x = lambda^4 mu, f = lambda^3 c_F, eps_p = -(lambda^5 c_F^2 (r/p)^2)^{-1}
  F4 FLOATING_RECONNAISSANCE  h_p Gauss sums: sum_{h != 0} C_{p,j}(h) conj(chi_p(a_h)^2) e(eps_p h^{-1} x/p)
                              = K_j * B_p(x) with |K_j| = 1 independent of x (j = 1 is the R-prime case)
  F5 EXACT                    (B.2): kappa(g H^{-1}) from DR (5.4) equals Kintali's three closed forms, and
                              kappa_fix = kappa / (a/r)_3 is constant over lifted frequency tuples
  F6 EXACT (sympy) + FLOATING Mellin constants of (B.3), the dual moment, the prefactor -i/81 and (2pi)^4/27;
                              Bessel Mellin formula; kernel V# sample values
  F7 EXACT (sympy)            (8) from the j = 0 line of table (A.4) at (x, w, z) = (s, 1, 1/6), u = 1
Run:  python3 -I kintali_lemma3_finite.py OUT.json
"""
import cmath
import itertools
import json
import math
import os
import random
import sys
import time
from fractions import Fraction

import mpmath
import sympy

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kintali_lemma3_common as K  # noqa: E402

LAM = K.LAM


def e_frac(alpha, beta):
    """Kintali e(alpha/beta), exact exponent as Fraction mod 1."""
    return K.frac_e_coord(alpha, beta) % 1


def ech_frac(alpha, beta):
    return K.frac_ech_coord(alpha, beta) % 1


def cx(fr):
    return cmath.exp(2j * math.pi * float(fr))


def chi_code(x, p):
    return K.sextic_code(x, p)


def chi_pow(x, p, j):
    """chi_p(x)^j with Kintali's convention (zero at p | x for every j, incl. j = 0)."""
    k = chi_code(x, p)
    if k is None:
        return 0j
    return K.zeta_pow((j * k) % 6)


def prod_elems(lst):
    r = (1, 0)
    for p in lst:
        r = K.mul(r, p)
    return r


def main(out):
    t0 = time.time()
    res = {}
    random.seed(11)
    primes = K.primary_primes_upto(400)          # prime to 6
    small = [p for p in primes if K.norm(p) <= 100]

    # ---------------- F1
    maxd, cnt = 0.0, 0
    sqf = []
    for k in (1, 2):
        for combo in itertools.combinations([p for p in primes if K.norm(p) <= 160], k):
            c = prod_elems(combo)
            if K.norm(c) <= 700:
                sqf.append((c, combo))
    for c, combo in sqf:
        q = K.norm(c)
        g3 = 0j
        gam2 = 0j
        for d in K.residues(c):
            kk = K.cubic_symbol(d, c)
            if kk is None:
                continue
            g3 += K.omega_pow(kk) * cx(ech_frac(d, c))
            # gamma_2: chi_c(d)^2 = (d/c)_3, additive character e(d/c)
            gam2 += K.omega_pow(kk) * cx(e_frac(d, c))
        g3 /= math.sqrt(q)
        gam2 /= math.sqrt(q)
        lam_code = sum(chi_code(LAM, p) for p in combo)          # chi_c(lambda) = zeta^lam_code
        pred = K.zeta_pow((-2 * lam_code) % 6) * gam2
        maxd = max(maxd, abs(g3 - pred), abs(abs(g3) - 1))
        cnt += 1
    res["F1"] = {"cases": cnt, "max_dev": maxd}
    print("F1", res["F1"], flush=True)

    # ---------------- F2
    maxd, cnt = 0.0, 0
    for p in [q for q in primes if K.norm(q) <= 61]:
        q = K.norm(p)
        R = K.residues(p)
        for j in range(6):
            tau_minus = sum(chi_pow(x, p, j) * cx(e_frac(K.neg(x), p)) for x in R) / math.sqrt(q)
            C = {}
            for h in R:
                C[h] = sum(chi_pow(x, p, j) * cx(e_frac(K.neg(K.mul(h, x)), p)) for x in R) / q
                hz = K.divides(p, h)
                if j != 0 and not hz:
                    pred = tau_minus * chi_pow(h, p, -j) / math.sqrt(q)
                elif j != 0 and hz:
                    pred = 0
                elif j == 0 and not hz:
                    pred = -1 / q
                else:
                    pred = 1 - 1 / q
                maxd = max(maxd, abs(C[h] - pred))
                cnt += 1
            for x in R:
                inv = sum(C[h] * cx(e_frac(K.mul(h, x), p)) for h in R)
                maxd = max(maxd, abs(inv - chi_pow(x, p, j)))
            if j != 0:
                maxd = max(maxd, abs(abs(tau_minus) - 1))
    res["F2"] = {"cases": cnt, "max_dev": maxd}
    print("F2", res["F2"], flush=True)

    # ---------------- F3 (exact)
    cFs = [(1, 0), LAM, K.neg(LAM), K.power(LAM, 2), K.power(LAM, 3), (-2, 0), K.mul((-2, 0), LAM),
           K.mul((-2, 0), K.power(LAM, 2)), (4, 0)]
    fails, cnt = 0, 0
    for trial in range(60):
        cF = random.choice(cFs)
        rl = random.sample(small, random.choice([1, 2, 3]))
        r = prod_elems(rl)
        f = K.mul(K.power(LAM, 3), cF)
        # a_F coprime to c_F
        while True:
            aF = (random.randint(-20, 20), random.randint(-20, 20))
            if not K.is_zero(aF) and K.norm(K.egcd(aF, cF)[0]) == 1:
                break
        hs = []
        for p in rl:
            while True:
                h = (random.randint(-30, 30), random.randint(-30, 30))
                if not K.divides(p, h):
                    break
            hs.append(h)
        a = K.mul(aF, r)
        for p, h in zip(rl, hs):
            a = K.add(a, K.mul(K.mul(K.power(LAM, 2), cF), K.mul(K.exact_div(r, p), h)))
        c = K.mul(cF, r)
        if K.norm(K.egcd(a, c)[0]) != 1:
            continue
        delta = K.inv_mod(a, c)
        deltaF = K.reduce_mod(delta, f)
        rinv = K.inv_mod(r, f)
        eps = {}
        for p in rl:
            rp = K.exact_div(r, p)
            t = K.mul(K.power(LAM, 5), K.mul(K.mul(cF, cF), K.mul(rp, rp)))
            eps[p] = K.reduce_mod(K.neg(K.inv_mod(t, p)), p)
        for _ in range(40):
            x = (random.randint(-400, 400), random.randint(-400, 400))
            # ech(-delta mu / c) with mu = x / lambda^4  ->  ech(-delta x / (lambda^4 c))
            lhs = ech_frac(K.neg(K.mul(delta, x)), K.mul(K.power(LAM, 4), c))
            rhs = e_frac(K.neg(K.mul(K.mul(deltaF, rinv), x)), f)
            for p, h in zip(rl, hs):
                rhs += e_frac(K.mul(K.mul(eps[p], K.inv_mod(h, p)), x), p)
            cnt += 1
            if (lhs - rhs) % 1 != 0:
                fails += 1
    res["F3"] = {"cases": cnt, "failures": fails}
    print("F3", res["F3"], flush=True)

    # ---------------- F4
    maxd, maxu, cnt = 0.0, 0.0, 0
    recs = []
    for trial in range(24):
        cF = random.choice(cFs)
        rl = random.sample([p for p in small if K.norm(p) <= 61], 2)
        r = prod_elems(rl)
        p = rl[0]
        q = K.norm(p)
        rp = K.exact_div(r, p)
        R = K.residues(p)
        t = K.mul(K.power(LAM, 5), K.mul(K.mul(cF, cF), K.mul(rp, rp)))
        eps = K.reduce_mod(K.neg(K.inv_mod(t, p)), p)
        for j in range(6):
            S = {}
            for x in R:
                s = 0j
                for h in R:
                    if K.divides(p, h):
                        continue
                    Cj = sum(chi_pow(y, p, j) * cx(e_frac(K.neg(K.mul(h, y)), p)) for y in R) / q
                    ah = K.mul(K.mul(K.power(LAM, 2), cF), K.mul(rp, h))
                    mult = chi_pow(ah, p, -2)          # conj(chi_p(a)^2), a = lambda^2 c_F (r/p) h mod p
                    s += Cj * mult * cx(e_frac(K.mul(K.mul(eps, K.inv_mod(h, p)), x), p))
                S[x] = s
            # Kintali's B_p (j = 1 is the R-prime case: chi_p(x)^3)
            def B(x):
                if j == 1:
                    return chi_pow(x, p, 3)
                if j == 4:
                    return (-1 + q * (1 if K.divides(p, x) else 0)) / math.sqrt(q)
                if j == 0:
                    return chi_pow(x, p, -2) / math.sqrt(q)
                return chi_pow(x, p, -j - 2)
            ratios = [S[x] / B(x) for x in R if abs(B(x)) > 1e-12]
            Kj = ratios[0]
            dev = max(abs(S[x] - Kj * B(x)) for x in R)
            maxd = max(maxd, dev)
            maxu = max(maxu, abs(abs(Kj) - 1))
            cnt += 1
            recs.append((K.norm(p), j, round(abs(Kj), 12), dev))
    res["F4"] = {"cases": cnt, "max_dev_from_constant_times_B": maxd, "max_||K_j|-1|": maxu}
    print("F4", res["F4"], flush=True)

    # ---------------- F5 (exact symbols)
    Mt = K.mul(K.power(LAM, 8), (4, 0))          # test stand-in for M = lambda^12 L^4

    def build(cF, aF, rl, hs):
        r = prod_elems(rl)
        a = K.mul(aF, r)
        for p, h in zip(rl, hs):
            a = K.add(a, K.mul(K.mul(K.power(LAM, 2), cF), K.mul(K.exact_div(r, p), h)))
        c = K.mul(cF, r)
        vl = K.lam_val(c)[0]
        v2 = 0
        t_ = c
        while K.divides((2, 0), t_):
            t_ = K.exact_div(t_, (2, 0))
            v2 += 1
        parts = []
        lm = K.power(LAM, 8 + vl)
        parts.append((K.inv_mod(a, lm) if vl > 0 else (0, 0), lm))
        tm = K.power((2, 0), 2 + v2)
        parts.append((K.inv_mod(a, tm) if v2 > 0 else (0, 0), tm))
        for p in rl:
            parts.append((K.inv_mod(a, p), p))
        delta, MM = K.crt(parts)
        if K.is_zero(delta):
            delta = MM
        b0 = K.exact_div(K.sub(K.mul(a, delta), (1, 0)), c)
        return r, a, c, delta, b0, vl

    def kappa_code(g):
        (A, B), (C, D) = g
        for e_, t_ in ((A, 1), (D, 1), (B, 0), (C, 0)):
            assert K.congruent(e_, (t_, 0), (3, 0)), g
        if K.is_zero(C):
            return 0
        return K.cubic_symbol(C, A)

    def mm(g, h):
        (a, b), (c, d) = g
        (e, f), (gg, hh) = h
        return ((K.add(K.mul(a, e), K.mul(b, gg)), K.add(K.mul(a, f), K.mul(b, hh))),
                (K.add(K.mul(c, e), K.mul(d, gg)), K.add(K.mul(c, f), K.mul(d, hh))))

    def minv(g):
        (a, b), (c, d) = g
        return ((d, K.neg(b)), (K.neg(c), a))

    f5 = {"cases": 0, "B2_mismatch": 0, "by_case": {1: 0, 2: 0, 3: 0}, "kappa_fix_nonconstant_branches": 0,
          "branches": 0}
    cF_by_case = {1: [K.power(LAM, 2), K.power(LAM, 3), K.mul((-2, 0), K.power(LAM, 2))],
                  2: [LAM, K.neg(LAM), K.mul((-2, 0), LAM)],
                  3: [(1, 0), (-2, 0), (4, 0)]}
    for case in (1, 2, 3):
        for trial in range(14):
            cF = random.choice(cF_by_case[case])
            while True:
                aF = (random.randint(-12, 12), random.randint(-12, 12))
                if K.is_zero(aF) or K.norm(K.egcd(aF, cF)[0]) != 1:
                    continue
                if case in (1, 2) and not K.is_primary(aF):
                    continue
                break
            rl = random.sample([p for p in small if K.norm(p) <= 43], random.choice([1, 2]))
            base = []
            for p in rl:
                while True:
                    h = (random.randint(-9, 9), random.randint(-9, 9))
                    if not K.divides(p, h):
                        break
                base.append(h)
            fixes = set()
            for lift in range(4):
                # Kintali: lift h_p to h_p' = h_p (mod p), h_p' = 0 (mod M); here M -> Mt
                hs = []
                for p, h in zip(rl, base):
                    hh, _ = K.crt([(h, p), ((0, 0), Mt)])
                    hh = K.add(hh, K.mul(K.mul(p, Mt), (lift, lift % 2)))
                    hs.append(hh)
                r, a, c, delta, b0, vl = build(cF, aF, rl, hs)
                if vl >= 2:
                    H = (((1, 0), (0, 0)), ((0, 0), (1, 0)))
                    u0 = None
                elif vl == 1:
                    u0 = LAM if K.congruent(c, LAM, (3, 0)) else K.neg(LAM)
                    H = (((1, 0), (0, 0)), (u0, (1, 0)))
                else:
                    u0 = K.reduce_mod(a, (3, 0))
                    H = ((u0, (-1, 0)), ((1, 0), (0, 0)))
                g = ((a, b0), (c, delta))
                kg = mm(g, minv(H))
                kc = kappa_code(kg)
                ar = sum(K.cubic_code(a, p) for p in rl) % 3
                if vl >= 2:
                    fixed = K.cubic_symbol(cF, a) if K.norm(a) > 1 else 0
                elif vl == 1:
                    A0 = K.sub(a, K.mul(u0, b0))
                    f1 = K.cubic_symbol(K.neg(u0), A0) if K.norm(A0) > 1 else 0
                    f2 = K.cubic_symbol(K.exact_div(cF, u0), a) if K.norm(a) > 1 else 0
                    fixed = (f1 + f2) % 3
                else:
                    fixed = 0
                    if K.norm(cF) > 1:
                        for p, e in K.factor(cF)[1]:
                            fixed += e * K.cubic_code(a, p)
                    fixed %= 3
                f5["cases"] += 1
                f5["by_case"][case] += 1
                if (fixed + ar) % 3 != kc:
                    f5["B2_mismatch"] += 1
                fixes.add((kc - ar) % 3)
            f5["branches"] += 1
            if len(fixes) != 1:
                f5["kappa_fix_nonconstant_branches"] += 1
    res["F5"] = f5
    print("F5", f5, flush=True)

    # ---------------- F6 constants
    t, w, y, x, v, mu, q = sympy.symbols("t w y x v mu q", positive=True)
    # Bessel Mellin: int_0^oo K_{1/3}(y) y^{w-1} dy = 2^{w-2} Gamma((w-1/3)/2) Gamma((w+1/3)/2)
    bes = []
    for wv in (1.0, 1.7, 2.5, 3.3):
        lhs = mpmath.quad(lambda yy: mpmath.besselk(mpmath.mpf(1) / 3, yy) * yy ** (wv - 1), [0, 1, mpmath.inf])
        rhs = 2 ** (wv - 2) * mpmath.gamma((wv - mpmath.mpf(1) / 3) / 2) * mpmath.gamma((wv + mpmath.mpf(1) / 3) / 2)
        bes.append(float(abs(lhs - rhs) / abs(rhs)))
    # infinity side constant: 2 pi i mubar * 3^{5/2}|b| with mubar = -i |cb^3| conj(alpha)/(3 sqrt 3)
    ts = sympy.Symbol("t")
    const_inf = 2 * sympy.pi * sympy.I * (-sympy.I / (3 * sympy.sqrt(3))) * 3 ** sympy.Rational(5, 2)
    # times int v K(4 pi |mu| v) v^{2t} dv = (4 pi |mu|)^{-2t-2} 4^t Gamma(1+t+-1/6), |mu| = 3^{-3/2}|cb^3|
    # coefficient of (q_c q_b^3)^{-t} q_c^{-1/2} q_b^{-1} Gamma Gamma:
    c_inf = const_inf * (4 * sympy.pi) ** (-2 * ts - 2) * 4 ** ts * (3 ** sympy.Rational(3, 2)) ** (2 * ts + 2)
    target_inf = sympy.Rational(81, 8) / sympy.pi * (27 / (4 * sympy.pi ** 2)) ** ts
    d1 = sympy.simplify(sympy.expand_power_base(sympy.powsimp(c_inf / target_inf, force=True), force=True))
    # dual side: -(c v)^-2 * 2 pi i mu * v' K(4 pi|mu| v'), v' = 1/(q_c v); Mellin in v with v^{2t}
    # = -2 pi i c^{-2} q_c^{-1} * (4 pi |mu| / q_c)^{2t-2} 4^{-t} Gamma(1-t+-1/6) * mu
    # target: -(i/(8 pi)) conj(alpha_c)^2 (4 pi^2)^t q_c^{-2t} alpha(mu) q_mu^{t-1/2}
    # check the scalar: [-2 pi i (4 pi)^{2t-2} 4^{-t}] / [-(i/(8 pi)) (4 pi^2)^t]  == 1
    d2 = sympy.simplify(sympy.powsimp(((-2 * sympy.pi * sympy.I) * (4 * sympy.pi) ** (2 * ts - 2) * 4 ** (-ts))
                                      / (-(sympy.I / (8 * sympy.pi)) * (4 * sympy.pi ** 2) ** ts), force=True))
    # combined: (8 pi/81)(4 pi^2/27)^t * (-(i/(8 pi))(4 pi^2)^t) = (-i/81) ((2 pi)^4 / 27)^t
    d3 = sympy.simplify(sympy.powsimp((8 * sympy.pi / 81) * (4 * sympy.pi ** 2 / 27) ** ts
                                      * (-(sympy.I / (8 * sympy.pi)) * (4 * sympy.pi ** 2) ** ts)
                                      / ((-sympy.I / 81) * ((2 * sympy.pi) ** 4 / 27) ** ts), force=True))
    # numeric spot check of a single dual Mellin moment
    cq, mabs = 21.0, 0.37
    tt = -0.9 + 0.3j
    f_int = mpmath.quad(lambda vv: (1 / (cq * vv)) * mpmath.besselk(mpmath.mpf(1) / 3, 4 * mpmath.pi * mabs / (cq * vv))
                        * vv ** (2 * tt - 2), [0, 0.05, 1, mpmath.inf])
    f_cf = (4 * mpmath.pi * mabs / cq) ** (2 * tt - 2) * 4 ** (-tt) * mpmath.gamma(1 - tt - mpmath.mpf(1) / 6) \
        * mpmath.gamma(1 - tt + mpmath.mpf(1) / 6) / cq
    # kernel V#(x) = (1/2 pi i) int_(s) e^{t^2} prod Gamma(1+t+-1/6)/Gamma(1-t+-1/6) ((2pi)^4 x/27)^{-t} dt
    def Vsharp(xx, s0):
        f = lambda u: mpmath.e ** ((s0 + 1j * u) ** 2) * mpmath.gamma(1 + s0 + 1j * u + mpmath.mpf(1) / 6) \
            * mpmath.gamma(1 + s0 + 1j * u - mpmath.mpf(1) / 6) / (mpmath.gamma(1 - s0 - 1j * u + mpmath.mpf(1) / 6)
                                                                * mpmath.gamma(1 - s0 - 1j * u - mpmath.mpf(1) / 6)) \
            * ((2 * mpmath.pi) ** 4 * xx / 27) ** (-(s0 + 1j * u))
        return mpmath.quad(f, [-mpmath.inf, 0, mpmath.inf]) / (2 * mpmath.pi)
    vs = []
    for xx in (0.01, 0.1, 1.0, 10.0):
        a0 = Vsharp(xx, 0.0)
        a1 = Vsharp(xx, 1.0)
        vs.append({"x": xx, "V#(line 0)": complex(a0), "V#(line 1)": complex(a1),
                   "line_shift_dev": float(abs(a0 - a1))})
    res["F6"] = {"bessel_mellin_rel_dev": bes, "inf_const_ratio_minus_1": str(sympy.simplify(d1 - 1)),
                 "dual_const_ratio_minus_1": str(sympy.simplify(d2 - 1)),
                 "combined_prefactor_ratio_minus_1": str(sympy.simplify(d3 - 1)),
                 "dual_moment_rel_dev": float(abs(f_int - f_cf) / abs(f_cf)), "Vsharp": vs}
    print("F6", res["F6"], flush=True)

    # ---------------- F7: (8) from (A.4), j = 0, u = 1, (x, w, z) = (s, 1, 1/6)
    Q, eta, Dd, Rr = sympy.symbols("Q eta D R")
    tq = 1 / Q
    V = Q ** -1                  # V = Q^{-6z}, z = 1/6
    Wl = tq                      # W_l = rho Q^{-w}, rho = 1, w = 1
    Dval = Dd                    # D = eta(p) Q^{-x}
    # eta(p)(Q-1)Q^{-x-w} V = D (Q-1) Q^{-1} Q^{-1}
    term = Dval * (Q - 1) / Q * V
    J0 = -Dval + Wl * Rr          # -eta(p) rho^{-1} Q^{-x} + W_l R
    Pstar = (Rr * (1 - 1 / Q) - term * 1) / ((1 - Rr) * (1 - V)) + J0 / (1 - Rr)
    P = 1 / (1 - V) + Wl / (1 - Wl) + Pstar
    Hp = P * (1 - V) * (1 - tq) / (1 - Dval)
    H8 = (1 - tq ** 2) / (1 - Rr) * (1 + tq * (Dval - Rr) / (1 - Dval))
    full_kintali = (1 + tq) / (1 - tq) + (1 + tq) * (Rr - Dval) / (1 - Rr)
    res["F7"] = {"Hp_minus_(8)": str(sympy.simplify(Hp - H8)),
                 "P_minus_stated_full_factor": str(sympy.simplify(P - full_kintali))}
    print("F7", res["F7"], flush=True)
    res["seconds"] = time.time() - t0
    with open(out, "w") as fh:
        json.dump(res, fh, indent=1, default=str)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "kintali_lemma3_finite.json")
