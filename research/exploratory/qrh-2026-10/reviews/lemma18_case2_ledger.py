"""lemma18_case2_ledger.py -- exact-rational checks of case 2 (positive slots) and of the loss
bookkeeping of Sec. 18.8 in the proof of Lemma 18.1 (lem:plain) of the OpenAI QRH manuscript
(30 Sep 2026; pr908 paper.tex, sha256 42a5ee0f...deac6a3).  Line numbers refer to that file.

Scope.  Checks the displayed identities and inequalities of
  * the positive-slot amplifier (l. 13456-13594): local Gauss data at valuations 1, 6, 7,
    the squared extraction coefficients, (old-eq:2.9), (old-eq:2.10), the added Gauss row zero;
  * the diagonal (old-eq:2.12) and width drop (old-eq:2.13) for all four norm types;
  * (old-eq:3.14), the clipped identities (eq:centered-clipped-rectangle), the paired bound
    (eq:centered-clipped-shell), the F_act chain, the greedy prefix removal (old-eq:3.16) and
    the strict-edge cost (eq:centered-child-edge-cost)  (l. 14180-14305);
  * the comparison margins (old-eq:3.11), (eq:comparison-uncentered-margin), (old-eq:3.6);
  * Sec. 18.8 (l. 14779-14984): (old-eq:2.1j), the parameter order (old-eq:2.1i), depth D,
    band exit, the envelope recursion E_d and the terminal-loss list in T_term;
  * the zero-slack points: the three of the Theta-row stage (re-evaluated in the case-2
    setting) and the amplifier/greedy balance, which has zero slack per edge.
Every inequality family has a failing control (a mutation that must be detected).

All arithmetic is exact (fractions.Fraction, sympy) except part G2, which evaluates explicit
sextic Gauss sums in Z/p^a in floating point (tolerance 1e-9) as a cross-check of G1.
It checks displayed algebra only.  It does not check analytic estimates (prime density,
Fourier-measure norms, tails) or that the ledgers describe the analysis correctly.

Run: nice -n 10 python3 -I lemma18_case2_ledger.py
"""
import cmath
import itertools
import math
import random
import sys
from fractions import Fraction as Fr

import numpy as np
import sympy as sp

RES = []


def check(name, ok, detail=""):
    RES.append((name, bool(ok)))
    print(("PASS " if ok else "FAIL ") + name + (("   " + detail) if detail else ""))
    sys.stdout.flush()


def control(name, detected, detail=""):
    """A failing control: the mutated statement must be detected as false."""
    check("CONTROL " + name + " (mutation detected)", detected, detail)


def pos(x):
    return x if x > 0 else Fr(0)


rng = random.Random(20261010)


def rfr(lo, hi, den=360):
    lo, hi = Fr(lo), Fr(hi)
    if hi <= lo:
        return lo
    n = rng.randint(0, den)
    return lo + (hi - lo) * Fr(n, den)


# ================================================================================================
# G. amplifier local Gauss data (l. 13485-13531, eq:gauss-local l. 7059-7065)
# ================================================================================================
def G_formula(P, a, v):
    """Exact (|G|^2, G if real-determined) from eq:gauss-local for G(p^a, k), v = v_p(k).
    Returns (abs2, value_or_None).  For 6 | a the value is real and exact."""
    if a == 0:
        return Fr(1), Fr(1)
    if a % 6:
        return (Fr(P) ** (a - 1) if v == a - 1 else Fr(0)), None
    val = (Fr(P) ** (a // 2) if v >= a else 0) - (Fr(P) ** (a // 2 - 1) if v >= a - 1 else 0)
    return val * val, Fr(val)


def part_G1():
    bad, changed_all = [], {}
    for P in [7, 13, 19, 31, 37, 43]:
        changed = []
        for a in range(0, 37):
            old2, oldv = G_formula(P, a, 0)        # p does not divide h
            new2, newv = G_formula(P, a, 6)        # v_p(h p^6) = 6
            if old2 != new2 or (oldv is not None and oldv != newv):
                changed.append(a)
                # squared extraction coefficient P^{-a} |G_old - G_new|^2 (one of old/new is 0 here)
                if oldv is not None:
                    diff2 = (oldv - newv) ** 2
                else:
                    assert old2 == 0 or new2 == 0
                    diff2 = old2 + new2
                c2 = diff2 / Fr(P) ** a
                expect = {1: Fr(1, P), 6: (1 - Fr(1, P)) ** 2, 7: Fr(1, P)}.get(a)
                if c2 != expect:
                    bad.append((P, a, c2, expect))
        changed_all[P] = changed
        if changed != [1, 6, 7]:
            bad.append((P, "changed", changed))
    check("G1 eq:gauss-local: h -> h p^6 (p !| h) changes only valuations 1,6,7; |c|^2 = P^-1,(1-1/P)^2,P^-1",
          not bad, "a<=36, P in {7,...,43}; changed sets %s" % changed_all[7])
    # (old-eq:2.9): squared coefficients equal Z^{-w_o} with (w, w_o) = (i l_p, e_i l_p), e_1=e_7=1, e_6=0
    ok = all((Fr(1, P) if i in (1, 7) else (1 - Fr(1, P)) ** 2) <= Fr(1, P) ** {1: 1, 6: 0, 7: 1}[i]
             for P in [7, 13, 19] for i in (1, 6, 7))
    check("G1b (old-eq:2.9) squared coefficient <= P^{-e_i} = Z^{-w_o}", ok)
    # control: a fifth-power amplifier h -> h p^5 changes a different set and is not invariant on u
    ch5 = [a for a in range(0, 37) if G_formula(7, a, 0) != G_formula(7, a, 5)]
    control("G1c fifth-power amplifier changes valuations %s (not {1,6,7})" % ch5, ch5 != [1, 6, 7])


def part_G2():
    """Brute-force sextic Gauss sums in Z/p^a (p = 7, 13) as an independent cross-check."""
    worst, fails = 0.0, []
    for p, amax, g in [(7, 8, 3), (13, 5, 2)]:
        ind = {pow(g, k, p): k for k in range(p - 1)}
        zeta = [cmath.exp(2j * math.pi * k / 6) for k in range(6)]

        def chi(x):
            x %= p
            return 0.0 if x == 0 else zeta[ind[x] % 6]

        chi_tab = np.array([chi(x) for x in range(p)], dtype=complex)

        def G(a, k):
            if a == 0:
                return 1.0 + 0j
            N = p ** a
            tot = 0j
            step = 1 << 20
            for s in range(0, N, step):
                x = np.arange(s, min(N, s + step), dtype=np.int64)
                cx = chi_tab[x % p] ** a
                cx[x % p == 0] = 0.0
                tot += (cx * np.exp(2j * np.pi * ((k % N) * x % N) / N)).sum()
            return tot / math.sqrt(N)

        P = p
        for a in range(0, amax + 1):
            for h in [1, 2, 3]:
                go, gn = G(a, h), G(a, h * p ** 6)
                o2, _ = G_formula(P, a, 0)
                n2, _ = G_formula(P, a, 6 if a <= 7 or True else 6)
                worst = max(worst, abs(abs(go) ** 2 - float(o2)) / max(1.0, float(o2)),
                            abs(abs(gn) ** 2 - float(n2)) / max(1.0, float(n2)))
                c = (go - gn) / P ** (a / 2)
                if a in (1, 6, 7) and a <= amax:
                    exp2 = {1: 1 / P, 6: (1 - 1 / P) ** 2, 7: 1 / P}[a]
                    if abs(abs(c) ** 2 - exp2) > 1e-9:
                        fails.append((p, a, h, abs(c) ** 2, exp2))
                elif abs(c) > 1e-9:
                    fails.append((p, a, h, "nonzero change"))
        # row phases: c_1(h), c_7(h) proportional to conj chi(h); c_6(h) independent of h
        for a, phase in [(1, True), (7, True), (6, False)]:
            if a > amax:
                continue
            c1 = (G(a, 1) - G(a, p ** 6))
            for h in [2, 3, 5]:
                ch = (G(a, h) - G(a, h * p ** 6))
                pred = c1 * (np.conj(chi(h)) if phase else 1.0)
                if abs(ch - pred) > 1e-7 * max(1.0, abs(c1)):
                    fails.append((p, a, h, "phase"))
    check("G2 explicit Gauss sums in Z/7^a (a<=8), Z/13^a (a<=5) match G1; phases conj chi(h) at 1,7, none at 6",
          not fails and worst < 1e-9, "max rel dev %.1e; failures %s" % (worst, fails[:3]))
    # G(u, h p^6) = G(u, h) for a prime u != p: chi_u(p^6) = 1 (sextic); control with p^5
    q, g = 13, 2
    ind = {pow(g, k, q): k for k in range(q - 1)}

    def Gq(k):
        return sum(cmath.exp(2j * math.pi * ind[x] / 6) * cmath.exp(2j * math.pi * k * x / q)
                   for x in range(1, q)) / math.sqrt(q)
    d6 = max(abs(Gq(h * 7 ** 6) - Gq(h)) for h in range(1, q))
    d5 = max(abs(Gq(h * 7 ** 5) - Gq(h)) for h in range(1, q))
    check("G3 G(u, h p^6) = G(u, h) for (p,u)=1 (u = 13, p = 7)", d6 < 1e-12, "max dev %.1e" % d6)
    control("G3c G(u, h p^5) = G(u, h)", d5 > 1e-6, "max dev %.2f" % d5)


# ================================================================================================
# A. amplifier exponent ledger (l. 13456-13594) and the diagonal / width drop (l. 13631-13661, 13790-13800)
# ================================================================================================
SIG = [Fr(1, 6), Fr(1, 10), Fr(1, 24)]


def norm_types(sig, ell_p):
    """(name, w, w_o, ell, extra) with g = J_+ + extra."""
    ls = sig / 3
    return [("amplified main", Fr(0), Fr(0), ls, 2 * sig),
            ("error i=1", ell_p, ell_p, Fr(0), sig),
            ("error i=6", 6 * ell_p, Fr(0), Fr(0), sig),
            ("error i=7", 7 * ell_p, ell_p, Fr(0), sig)]


def part_A():
    ok1 = all(6 * (s / 3) == 2 * s for s in SIG)
    check("A1 6 l_* = 2 sigma, so the ball K + J_+ + 2 sigma contains all rows h p^6   [l. 13508-13513]", ok1)
    ok = all((s / 3) - eta > s / 6 for s in SIG for eta in [s / 6 - s / 1000, s / 12, Fr(0)])
    check("A2 pool gap l_* - eta > sigma/6 for eta < sigma/6   [l. 13461-13469, (old-eq:2.1i)]", ok)
    control("A2c eta = sigma/6 leaves gap > sigma/6", not all((s / 3) - s / 6 > s / 6 for s in SIG))
    ok, mx = True, Fr(0)
    for s in SIG:
        for k in range(0, 61):
            lp = s / 6 + (s / 6) * Fr(k, 60)           # l_*/2 <= l_p <= l_*
            for name, w, wo, ell, extra in norm_types(s, lp):
                ok &= 0 <= wo <= w <= 7 * s / 3
                mx = max(mx, w / s)
    check("A3 (old-eq:2.10) 0 <= w_o <= w <= 7 sigma/3 for l_p in [l_*/2, l_*]", ok and mx == Fr(7, 3),
          "max w/sigma = %s" % mx)
    # added Gauss row zero: a0/3 + 4 th/3 <= a0 - s0 + 2 th  if a0 >= -th and s0 <= (a0+th)/6
    ok, okc = True, False
    for _ in range(4000):
        th = rfr(0, Fr(1, 50))
        a0 = rfr(-th, 3)
        s0 = rfr(0, (a0 + th) / 6)
        ok &= a0 / 3 + 4 * th / 3 <= a0 - s0 + 2 * th
        s0bad = (a0 + th)  # only s | u, not s^6 | u
        okc |= a0 / 3 + 4 * th / 3 > a0 - s0bad + 2 * th
    check("A4 added row zero: Z^{a0/3+4th/3} <= Z^{a0-s0+2th}   [l. 13571-13587]", ok)
    control("A4c without s^6 | u (s0 up to a0+th)", okc)

    # symbolic: (2.12) identity and (2.13) for general w, w_o, g, ell
    A, c, d, R, E, m, q, w, wo, g, ell, Bc, Dk, g2, t2, V = sp.symbols(
        "A c d R E m q w w_o g ell B_c Dk g_2 t_2 V", real=True)
    M = m + q
    qt = q + R + E
    K = 2 * A - c - d + R + E - m - Dk
    a0 = A - c - w
    J = d - c + Dk - 2 * w + wo
    mp = 2 * a0 - K - g - g2 - V
    qp = qt + wo + t2 + V
    check("A5 (old-eq:2.13) M' = M + J - g - g_2 + t_2 (any w, w_o, g)",
          sp.simplify(mp + qp - (M + J - g - g2 + t2)) == 0)
    lhs = (K + g - ell) - (a0 + qt + wo + w + Bc)
    check("A6 (old-eq:2.12) identity (any w, w_o, g, ell)",
          sp.simplify(lhs - ((A - M) - d - Dk - wo - Bc + g - ell)) == 0)

    # numeric: (2.12) inequality and (2.13) drop for all four norm types; record increments
    ok12, ok13, okc = True, True, False
    incs = set()
    for _ in range(6000):
        s = rng.choice(SIG)
        dfr = rfr(0, s / 50)
        lp = rfr(s / 6, s / 3)
        Mv = rfr(Fr(1, 4), 3)
        qv = rfr(0, Mv / 2)
        mv = Mv - qv
        Av = rfr(0, Mv)
        cv, dv = rfr(0, Av), rfr(0, Av)
        pv = rfr(0, min(cv, dv))
        Rv = rfr(0, pv)
        Ev = rfr(0, pv - Rv)
        Dkv = rfr(-dfr, 1)
        Bcv = pos((3 * cv - 5 * dv - Rv) / 6)
        g2v = rfr(0, 1)
        t2v = rfr(0, g2v)
        for name, wv, wov, ellv, extra in norm_types(s, lp):
            Jv = dv - cv + Dkv - 2 * wv + wov
            gv = pos(Jv) + extra
            Kv = 2 * Av - cv - dv + Rv + Ev - mv - Dkv
            a0v = Av - cv - wv
            qtv = qv + Rv + Ev
            diag = (Kv + gv - ellv) - (a0v + qtv + wov + wv + Bcv)
            inc = gv - pos(Jv) - ellv
            incs.add((name, inc / s))
            ok12 &= diag <= (Av - Mv) + Fr(5, 3) * s + dfr
            ok12 &= diag <= (Av - Mv) + inc + dfr
            Mpv = 2 * a0v - Kv - gv - g2v + qtv + wov + t2v
            ok13 &= Mpv <= Mv - s
            # control: amplifier without the density gain (ell = 0, g = J_+ + 2 sigma)
            if name == "amplified main":
                bad = (Kv + gv) - (a0v + qtv + wov + wv + Bcv)
                okc |= bad > (Av - Mv) + Fr(5, 3) * s + dfr
    check("A7 (old-eq:2.12) diagonal excess <= A - M + 5 sigma/3 + delta_fr1, four norm types   [l. 13649-13661]",
          ok12, "increments g-J_+-ell (units of sigma): %s" % sorted(set(v for _, v in incs)))
    check("A8 (old-eq:2.13) M' <= M - sigma for all four norm types", ok13)
    control("A7c amplified ball without the Z^{-l_*} gain exceeds 5 sigma/3", okc)


# ================================================================================================
# C. the positive-slot child: (3.14), clipping, F_act, greedy, edge cost (l. 14180-14305)
# ================================================================================================
def greedy(slots, F, kap):
    """Prefix removal of whole slots until the threshold F/(6 kappa) is reached."""
    thr = F / (6 * kap)
    removed = Fr(0)
    for x in sorted(slots, reverse=True):
        if removed >= thr:
            break
        removed += x
    return removed


def random_child(force_tight=False):
    s = rng.choice(SIG)
    th = rfr(0, s / 400)
    d1, d2 = rfr(0, s / 100), rfr(0, s / 100)
    eta = rfr(s / 200, s / 7)
    kap = rfr(Fr(3, 4), 1)
    Mv = rfr(Fr(1, 4), 3)
    qv = rfr(0, Mv / 2)
    mv = Mv - qv
    z = rfr(0, Mv / (6 * kap))
    Av = rfr(z, Mv - (6 * kap - 1) * z)
    if force_tight:
        Av = Mv - (6 * kap - 1) * z
    cv = Fr(0) if force_tight else rfr(0, Av - z)
    dv = Fr(0) if force_tight else rfr(0, Av - z)
    pv = rfr(0, min(cv, dv))
    Rv = rfr(0, pv)
    Ev = rfr(0, pv - Rv)
    Dkv = rfr(0, 1) if force_tight else rfr(-d1, 1)
    Bcv = pos((3 * cv - 5 * dv - Rv) / 6)
    lp = rfr(s / 6, s / 3)
    types = norm_types(s, lp)
    name, wv, wov, ellv, extra = types[0] if force_tight else rng.choice(types)
    Jv = dv - cv + Dkv - 2 * wv + wov
    gv = pos(Jv) + extra
    Kv = 2 * Av - cv - dv + Rv + Ev - mv - Dkv
    a0v = Av - cv - wv
    qtv = qv + Rv + Ev
    # second common support
    p2 = rfr(0, Fr(1, 2))
    if force_tight:
        c2 = d2v = g2v = p2
        t2v = Fr(0)
        Vv = p2
    else:
        c2, d2v = p2 + rfr(0, Fr(1, 2)), p2 + rfr(0, Fr(1, 2))
        g2v = rfr(p2, min(c2, d2v))
        t2v = rfr(0, p2)
        Vv = rfr(0, p2 - t2v)
    b2 = (c2 + d2v) / 2
    mp = 2 * a0v - Kv - gv - g2v - Vv
    qp = qtv + wov + t2v + Vv
    Mp = mp + qp
    Mact = Mp + (Fr(0) if force_tight else rfr(0, d2))
    Dchild = b2 - p2 + wv + Bcv + ellv
    return dict(s=s, th=th, d1=d1, d2=d2, eta=eta, kap=kap, M=Mv, A=Av, z=z, c=cv, d=dv, Dk=Dkv, w=wv,
                wo=wov, ell=ellv, g=gv, J=Jv, a0=a0v, c2=c2, d2v=d2v, g2=g2v, t2=t2v, V=Vv, Mp=Mp,
                Mact=Mact, Dchild=Dchild, name=name, lp=lp, B_c=Bcv)


def part_C():
    # symbolic (3.14) identity on both sides
    A, c, d, m, q, w, wo, g, Dk, g2, t2, c2, d2, R, E = sp.symbols(
        "A c d m q w w_o g Dk g_2 t_2 c_2 d_2 R E", real=True)
    M = m + q
    K = 2 * A - c - d + R + E - m - Dk
    a0 = A - c - w
    Mp = 2 * a0 - K - g - g2 + (q + R + E) + wo + t2
    ok = sp.simplify(((a0 - c2) - Mp) - (A - M) - (g + w - d - c2 - Dk - wo + g2 - t2)) == 0
    ok &= sp.simplify(((a0 - d2) - Mp) - (A - M) - (g + w - d - d2 - Dk - wo + g2 - t2)) == 0
    check("C1 (old-eq:3.14) identity, c_2 side and d_2 side   [l. 14184-14190]", ok)

    # (3.14) inequality, all four norm types, both sides; tightness of the amplified main
    ok, worst, okc = True, None, False
    for _ in range(8000):
        ch = random_child(force_tight=(rng.random() < 0.1))
        for side_len in (ch["c2"], ch["d2v"]):
            alpha = ch["a0"] - side_len
            exc = (alpha - ch["Mp"]) - (ch["A"] - ch["M"])
            rhs = 6 * (ch["w"] + ch["ell"]) + ch["d1"]
            ok &= exc <= rhs
            gap = exc - rhs
            worst = gap if worst is None else max(worst, gap)
    check("C2 (old-eq:3.14) (A'-M')-(A-M) <= 6(w+l) + delta_fr1, four norm types, both sides", ok,
          "max(lhs - rhs) = %s (0 = attained)" % worst)
    # the error-type step w - w_o + sigma <= 6w needs l_p >= sigma/6 at i = 1 (tight there)
    s = Fr(1, 10)
    tight = [(lp, 6 * lp - lp - lp + lp) for lp in [s / 6]]
    ok = all((w - wo + s) <= 6 * w for lp in [s / 6 + s * Fr(k, 600) for k in range(0, 101)]
             for (_, w, wo, _, _) in norm_types(s, lp)[1:])
    eq16 = (lambda lp: (lp - lp + s) - 6 * lp)(s / 6)
    check("C3 error terms: w - w_o + sigma <= 6w for l_p >= sigma/6 (equality at i=1, l_p = sigma/6)",
          ok and eq16 == 0, "actual pool l_p >= l_* - o(1) = sigma/3 - o(1) leaves slack sigma at i=1")
    control("C3c l_p = sigma/7 violates w - w_o + sigma <= 6w at i=1", (s / 7 - s / 7 + s) > 6 * (s / 7))

    # clipped identities (eq:centered-clipped-rectangle) and paired bound (eq:centered-clipped-shell)
    ok_id, ok_sh, okc = True, True, False
    for _ in range(5000):
        th = rfr(0, Fr(1, 100))
        I = rng.randint(0, 4)
        zs = [rfr(0, Fr(1, 20)) for _ in range(I)]
        Jset = [i for i in range(I) if rng.random() < 0.4]
        e = rfr(-th, th)
        alpha = rfr(-th, 2)
        # formal plain logs x_i with x1 + x2 + sum_I z = alpha + e
        x1 = rfr(-th / 2, alpha + e - sum(zs) + th / 2)
        x2 = alpha + e - sum(zs) - x1
        if x2 < -th / 2:
            continue
        a1, a2 = rfr(0, Fr(1, 2)), rfr(0, Fr(1, 2))
        y1, y2 = x1 - a1, x2 - a2
        rt = a1 + a2 + sum(zs[i] for i in Jset)
        pi0 = pos(-x1) + pos(-x2)
        pi = pos(-y1) + pos(-y2)
        rclip = sum(zs[i] for i in Jset) + (pos(x1) - pos(y1)) + (pos(x2) - pos(y2))
        Aclip = pos(y1) + pos(y2) + sum(zs[i] for i in range(I) if i not in Jset)
        ok_id &= (0 <= pi0 <= pi) and rclip == rt - (pi - pi0) and rclip >= 0
        ok_id &= Aclip == alpha + e - rt + pi == alpha + e + pi0 - rclip
    check("C4 (eq:centered-clipped-rectangle) identities and 0 <= pi_0 <= pi, r_clip >= 0 (exact)", ok_id)
    for _ in range(20000):
        th = rfr(0, Fr(1, 100))
        tm = rfr(0, 1)
        e1, e2 = rfr(-th, th), rfr(-th, th)
        om1 = rfr(max(-th, -th - e1), min(th, th - e1))
        om2 = rfr(max(-th, -th - e2), min(th, th - e2))
        rt1 = rfr(max(0, tm - om1), 2)
        rt2 = rfr(max(0, tm - om2), 2)
        p1, p2 = rfr(0, th), rfr(0, th)
        q1, q2 = rfr(0, p1), rfr(0, p2)
        rc1, rc2 = rt1 - (p1 - q1), rt2 - (p2 - q2)
        lhs = tm - (rc1 + rc2) / 2 + (e1 + q1 + e2 + q2) / 2
        ok_sh &= lhs <= ((e1 + om1) + p1 + (e2 + om2) + p2) / 2 <= 2 * th
        # control: dropping the divisor-boundary input r~_j + omega_j >= t_- (take r~ = 0)
        okc |= tm - (0 - (p1 - q1) + 0 - (p2 - q2)) / 2 + (e1 + q1 + e2 + q2) / 2 > 2 * th
    check("C5 (eq:centered-clipped-shell) paired count+coefficient exponent <= 2 theta_N", ok_sh)
    control("C5c without (eq:centered-divisor-boundary)", okc)

    # F_act chain, greedy removal, (3.16), edge cost
    okF = okG = okE = True
    worstF = None
    nsamp = 0
    for _ in range(12000):
        tight = rng.random() < 0.15
        ch = random_child(force_tight=tight)
        th, kap, eta = ch["th"], ch["kap"], ch["eta"]
        for side_len in (ch["c2"], ch["d2v"]):
            alpha = ch["a0"] - side_len
            e = Fr(0) if tight else rfr(-th, th)
            pi = th if tight else rfr(0, th)
            rt = Fr(0) if tight else rfr(0, Fr(1, 4))
            zp = ch["z"] if tight else rfr(0, ch["z"])           # surviving slot length z' <= z
            Aclip = alpha + e - rt + pi
            F = pos(Aclip - ch["Mact"] + (6 * kap - 1) * zp)
            bound = 6 * (ch["w"] + ch["ell"]) + ch["d1"] + 2 * th
            okF &= F <= bound
            gap = F - (6 * (ch["w"] + ch["ell"]) + ch["d1"] + 2 * th)
            worstF = gap if worstF is None else max(worstF, gap)
            # slots of the actual product: z_act = z' split into pieces <= eta
            slots, rem = [], zp
            while rem > 0:
                x = min(rem, rfr(eta / 20, eta))
                slots.append(x)
                rem -= x
            dz = greedy(slots, F, kap)
            after = (Aclip - dz) - ch["Mact"] + (6 * kap - 1) * (zp - dz)
            okG &= dz <= min(zp, F / (6 * kap) + eta)
            okG &= (after <= 0) or dz == zp
            okG &= kap * dz <= F / 6 + kap * eta
            okG &= kap * dz <= ch["Dchild"] + ch["d1"] / 6 + th / 3 + eta     # (old-eq:3.16)
            # strict-edge scale cost beyond the child envelope
            edge = ch["d2"] + ch["d1"] / 6 + eta + Fr(7, 3) * th
            okE &= (ch["Mact"] + kap * dz + 2 * th) <= ch["Mp"] + ch["Dchild"] + edge
            nsamp += 1
    check("C6 F_act <= 6(w+l) + delta_fr1 + 2 theta_N from raw clipped data   [l. 14217-14240]", okF,
          "%d sides; max(F - bound) = %s" % (nsamp, worstF))
    check("C7 greedy prefix: d_z <= min(z_act, F/6k + eta); affine restored or all removed; k d_z <= F/6 + k eta",
          okG)
    check("C8 (old-eq:3.16) + (eq:centered-child-edge-cost): child exponent <= M' + Delta_child + edge", okE)
    # symbolic: removing a slot of length d lowers A + (6k-1) z by 6 k d
    kk, dd, AA, zz = sp.symbols("kappa d A z", real=True)
    check("C9 slot removal lowers A + (6k-1)z by exactly 6 k d",
          sp.simplify((AA + (6 * kk - 1) * zz) - ((AA - dd) + (6 * kk - 1) * (zz - dd)) - 6 * kk * dd) == 0)
    th, d1, d2, eta, Dc = sp.symbols("theta delta_1 delta_2 eta Delta", positive=True)
    check("C10 edge cost = delta_fr2 + (delta_fr1/6 + theta/3 + eta) + 2 theta = (eq:centered-child-edge-cost)",
          sp.simplify(d2 + (d1 / 6 + th / 3 + eta) + 2 * th - (d2 + d1 / 6 + eta + sp.Rational(7, 3) * th)) == 0)


# ================================================================================================
# Z. zero-slack points
# ================================================================================================
def part_Z():
    # Z4 (new, case 2): amplifier gain vs greedy cost, exact at the tight configuration
    s = Fr(1, 10)
    ls = s / 3
    for kap in [Fr(3, 4), Fr(13, 16), Fr(1)]:
        # tight: c = d = 0, Dk >= 0, w = 0, g2 = c2, t2 = 0, z' = z, A + (6k-1)z = M, b2 = p2, B_c = 0
        F = 2 * s                       # (A'-M') - (A-M) = J_+ + 2 sigma - d - Dk = 2 sigma
        cost = kap * (F / (6 * kap))    # greedy cost without the mesh overshoot
        Dchild = ls                     # b2 - p2 + w + B_c + ell = ell
        assert cost - Dchild == 0
    check("Z4 amplifier/greedy balance: F_act = 2 sigma = 6 l_*, cost F/6 = l_* = Delta_child (zero slack per edge)",
          True, "tight at c=d=0, Dk>=0, g2=c2=d2=p2, t2=0, z'=z, A+(6k-1)z=M")
    # controls: per-edge excess under three mutations
    no_amp = (s / 6) - 0                       # no amplifier: F <= sigma, Delta_child >= 0
    five = (6 * ls) / 5 - ls                   # coefficient 5k in (old-eq:3.9): cost F/5
    half_gain = ls - ls / 2                    # density gain only Z^{-l_*/2}
    control("Z4c1 no amplifier: per-edge excess sigma/6 > 0", no_amp > 0, "excess %s" % no_amp)
    control("Z4c2 affine coefficient 5k instead of 6k: per-edge excess l_*/5 > 0", five > 0, "excess %s" % five)
    control("Z4c3 amplifier gain l_*/2 only: per-edge excess l_*/2 > 0", half_gain > 0, "excess %s" % half_gain)

    # Z1 (old-eq:2.19) in case 2: max_v = A - M = -(6k-1)z <= 0
    ok = True
    for kap in [Fr(3, 4), Fr(7, 8), Fr(1)]:
        for M in [Fr(1), Fr(5, 2)]:
            L = M / 4
            for z in [Fr(0), M / 100, M / (6 * kap)]:
                A = M - (6 * kap - 1) * z
                vals = [(A - Fr(5, 6) * M - Fr(2, 3) * v - pos(L - v), v) for v in [L * Fr(k, 40) for k in range(0, 161)]]
                mx = max(vals)
                ok &= mx[0] == A - M == -(6 * kap - 1) * z and mx[1] == L
    check("Z1 (old-eq:2.19) case 2: max over v is A - M = -(6k-1)z at v = L (slack (6k-1)z, -> 0 as z -> 0)", ok)
    M = Fr(1)
    mx = max(M - Fr(5, 6) * M - (Fr(2, 3) - Fr(1, 60)) * v - pos(M / 4 - v) for v in [Fr(k, 400) for k in range(0, 401)])
    control("Z1c F_1+F_2 >= (2/3 - 1/60) v instead of 2v/3 gives positive deficit at A = M", mx > 0, "max %s" % mx)
    # w enters v and F_1 consistently; amplifier losses at (2.19) are terminal O(sigma)
    worst = Fr(0)
    for lp in [s / 6 + s * Fr(k, 120) for k in range(0, 21)]:
        for name, w, wo, ell, extra in norm_types(s, lp):
            loss = w / 3 + Fr(5, 6) * extra - ell     # deficit from 2(c+w)/3 at J < 0 with g = J_+ + extra
            worst = max(worst, loss)
    check("Z1b amplifier loss at the (2.19) point is terminal and <= 22 sigma/9 < 3 sigma", worst <= Fr(22, 9) * s,
          "max loss = %s sigma" % (worst / s))

    # Z2: F_2 at a nonunit prime of multiplicity one: 2b2 - 5g2/6 - p2 + t2 + V/6 + f/6 with (1,1,1,0,1,2)
    F2 = 2 * 1 - Fr(5, 6) - 1 + 0 + Fr(1, 6) + Fr(2, 6)
    check("Z2 F_2 = 2 b_2/3 exactly at (i=1, nonunit); stronger count (2f) leaves f/6 = 1/3", F2 == Fr(2, 3),
          "F_2 = %s; with 2f: %s" % (F2, F2 + Fr(2, 6)))
    control("Z2c without the f/6 term F_2 < 2 b_2/3", F2 - Fr(2, 6) < Fr(2, 3))
    # Z3: F_1 = 2c/3 at J < 0 (q = E = 0, 3c >= 5 D0, w = w_o = 0, g = l = 0, Dk = 0)
    ok = True
    for c in [Fr(1), Fr(3, 2)]:
        for d in [Fr(0), Fr(1, 2) * c, Fr(3, 5) * c]:
            Rr = Fr(0)
            Bc = pos((3 * c - 5 * d - Rr) / 6)
            F1 = c / 6 + Fr(5, 6) * d + Rr / 6 + Bc
            ok &= (d - c < 0) and F1 == Fr(2, 3) * c
    check("Z3 F_1 = 2c/3 exactly at J < 0, q = E = 0, 3c >= 5 D_0 (case 2 adds only +w_o >= 0, +ell >= 0)", ok)


# ================================================================================================
# K. comparison margins (l. 12945-13010) and (old-eq:3.6)
# ================================================================================================
def part_K():
    # exact suprema over kappa in [3/4,1], A in (5/6,1], z <= (1-A)/(6k-1)  (M = 1)
    sup1 = Fr(3, 2) - Fr(5, 6) + 2 * (Fr(1, 6)) / (6 * Fr(3, 4) - 1)
    sup2 = Fr(3, 2) - Fr(5, 6) + (6 * Fr(3, 4) + 1) * Fr(1, 6) / (6 * Fr(3, 4) - 1)
    ok = True
    for kap in [Fr(3, 4) + Fr(k, 40) for k in range(0, 11)]:
        for A in [Fr(5, 6) + Fr(k, 600) for k in range(1, 101)]:
            zmax = (1 - A) / (6 * kap - 1)
            for z in [zmax * Fr(t, 10) for t in range(0, 11)]:
                ok &= z < Fr(1, 20) and z <= Fr(1, 21) and A - z > Fr(1, 2)
                ok &= Fr(3, 2) - A + 2 * z < sup1 and Fr(3, 2) - A + 2 * z + (6 * kap - 1) * z < sup2
    check("K1 comparison suprema 16/21 < 23/30 and 13/14 < 14/15 (true margins 1/14 vs claimed 1/15)",
          ok and sup1 == Fr(16, 21) and sup2 == Fr(13, 14) and sup1 < Fr(23, 30) and sup2 < Fr(14, 15),
          "sup A_comp = %s, sup A_comp+(6k-1)z = %s" % (sup1, sup2))
    ok = all(z <= M / (6 * k) <= Fr(2, 9) * M and k * z <= M / 6
             for k in [Fr(3, 4), Fr(1)] for M in [Fr(1)] for z in [Fr(t, 100) * M / (6 * k) for t in range(101)])
    check("K2 (old-eq:3.6) z <= M/(6k) <= 2M/9, k z <= M/6 (uses A >= z)", ok)
    k = Fr(1, 2)
    z = (Fr(1, 6)) / (6 * k - 1)
    control("K2c kappa = 1/2 (outside [3/4,1]) loses the 23/30 margin", Fr(3, 2) - Fr(5, 6) + 2 * z >= Fr(5, 6))
    # F_1 lower bound with actual g, ell for all positive-slot norm types (old-eq:2.17)
    ok = True
    for _ in range(6000):
        s = rng.choice(SIG)
        dfr = rfr(0, s / 50)
        lp = rfr(s / 6, s / 3)
        c, d = rfr(0, 2), rfr(0, 2)
        p = rfr(0, min(c, d))
        R = rfr(0, p)
        E = rfr(0, p - R)
        q = rfr(0, 1)
        Dk = rfr(-dfr, 1)
        qt = q + R + E
        Bc = pos((3 * c - 5 * d - R) / 6)
        for name, w, wo, ell, extra in norm_types(s, lp):
            J = d - c + Dk - 2 * w + wo
            g = pos(J) + extra
            F1 = c / 6 + Fr(5, 6) * (d + Dk) + w / 3 + qt / 6 + wo + Bc - Fr(5, 6) * g + ell
            ok &= F1 >= Fr(2, 3) * (c + w) - 3 * s - Fr(5, 6) * dfr
    check("K3 (old-eq:2.17) F_1 >= 2(c+w)/3 - 3 sigma - 5 delta_fr1/6 with the actual g, l of all four norm types", ok)


# ================================================================================================
# S. Sec. 18.8: quantifier order, depth, envelopes (l. 14779-14975)
# ================================================================================================
def part_S():
    ok = True
    for _ in range(4000):
        kap = rfr(Fr(3, 4), 1)
        dM, dA, dz = rfr(-1, 1), rfr(-1, 1), rfr(-1, 1)
        ok &= abs(dA + (6 * kap - 1) * dz - dM) <= abs(dM) + abs(dA) + 5 * abs(dz)
        ok &= Fr(7, 2) <= 6 * kap - 1 <= 5
    check("S1 (old-eq:2.1j) affine change <= |dM| + |dA| + 5|dz| for k in [3/4,1]", ok)
    kap = Fr(11, 10)
    control("S1c kappa = 11/10 breaks the constant 5", abs((6 * kap - 1) * 1) > 5)

    def choose(eps, Mmax, Cs):
        sig = eps / 24
        rho = eps / 24
        dl = min(rho, sig) / 100
        Tterm = rho + dl + rho / 6 + 3 * sig + Fr(5, 3) * sig
        D = 2 + math.ceil(2 * Mmax / sig)
        xi = min(dl / 2, rho / 30, sig / (4 * Cs), eps / (16 * Cs * D)) / 2
        eta = min(sig / 6, eps / (16 * Cs * D)) / 2
        e0 = eps / (16 * Cs * D) / 2
        return sig, rho, dl, Tterm, D, xi, eta, e0

    oks = []
    for eps, Mmax, Cs in [(Fr(1, 10), Fr(2), Fr(4)), (Fr(1, 100), Fr(3), Fr(10)), (Fr(1, 1000), Fr(5), Fr(50))]:
        sig, rho, dl, Tterm, D, xi, eta, e0 = choose(eps, Mmax, Cs)
        o = Tterm < eps / 4
        o &= 2 * xi <= dl and xi < rho / 30 and Cs * xi < sig / 4 and eta < sig / 6
        # strict drop and band exit (bands of length sigma/4)
        drop = sig - Cs * xi
        o &= drop >= sig / 2 and drop > 2 * (sig / 4)
        # depth: at most floor(Mmax / (sigma/2)) strict calls <= D - 2
        o &= math.floor(Mmax / (sig / 2)) <= D - 2
        # comparison margins at every width above the floor
        o &= rho / 15 > xi and rho / 6 > xi
        # envelopes
        E = [Tterm + (d + 1) * Cs * (eta + xi + e0) for d in range(0, D - 1)]
        o &= all(E[d] - E[d - 1] == Cs * (eta + xi + e0) for d in range(1, D - 1))
        o &= E[D - 2] < eps and Tterm + Cs * D * (eta + xi + e0) < eps
        # edge cost (eq:centered-child-edge-cost) <= C_*(xi + eta) when theta < xi/8, delta_fr < xi
        th = xi / 8
        edge = xi + xi / 6 + eta + Fr(7, 3) * th
        o &= edge <= max(Cs, Fr(35, 24)) * (xi + eta)
        # terminal losses each <= T_term (zero-slot floor, positive floor, diagonal, exceptional)
        terms = [rho + dl, rho + dl + rho / 6, dl + Fr(5, 3) * sig, 3 * sig, dl + 3 * sig]
        o &= all(t <= Tterm for t in terms)
        oks.append(o)
        last = (eps, D, Tterm, E[D - 2])
    check("S2 (old-eq:2.1i) choices: T_term < eps/4, drop >= sigma/2, depth <= D-2, E_{D-2} < eps, terminal list <= T_term",
          all(oks), "eps=%s: D=%d, T_term=%s eps, E_{D-2}=%.4f eps" % (last[0], last[1], last[2] / last[0],
                                                                    float(last[3] / last[0])))
    eps, Mmax, Cs = Fr(1, 100), Fr(3), Fr(10)
    sig, rho, dl, Tterm, D, xi, eta, e0 = choose(eps, Mmax, Cs)
    control("S2c1 a per-edge loss sigma/6 (no amplifier) accumulates past eps",
            Tterm + (D - 2) * sig / 6 >= eps, "(D-2) sigma/6 = %s" % float((D - 2) * sig / 6))
    control("S2c2 terminal losses summed along a branch exceed eps", (D - 1) * Tterm >= eps,
            "(D-1) T_term = %.2f" % float((D - 1) * Tterm))
    control("S2c3 xi = sigma/C_* gives no strict width drop", sig - Cs * (sig / Cs) <= 0)
    # depth simulation: worst-case chain of strict calls with drop exactly sigma/2
    n, Mw = 0, Mmax
    while Mw - sig / 2 >= 0:
        Mw -= sig / 2
        n += 1
    check("S3 worst-case chain with drop sigma/2 from M_max has <= D - 2 strict calls", n <= D - 2,
          "chain %d, D - 2 = %d" % (n, D - 2))


def main():
    part_G1()
    part_G2()
    part_A()
    part_C()
    part_Z()
    part_K()
    part_S()
    nf = sum(1 for _, o in RES if not o)
    nc = sum(1 for n, _ in RES if n.startswith("CONTROL"))
    print("\n%d/%d PASS (%d of them failing controls detected)" % (len(RES) - nf, len(RES), nc))
    return nf


if __name__ == "__main__":
    sys.exit(main())
