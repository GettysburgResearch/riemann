#!/usr/bin/env python3
"""Exact-arithmetic checks for the centred Theta-row stage of Lemma 18.1 (lem:plain).

Status: REVIEW support script (exact rational arithmetic; sympy and fractions.Fraction).
Source: paper.tex at pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6,
        sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3.
Target lines: 14312-14778 ((old-eq:2.15)-(2.19), eq:exceptional-row-count, (2.18h)).

What it does
  S*  symbolic identities (sympy): (2.15)-(2.16), the intermediate form at 14462-14466,
      the J >= 0 simplification of F_1 at 14474-14477, (2.18h), (2.14) from the table.
  P*  exhaustive per-prime tables (Fraction), recomputed from the DEFINITIONS of
      b2, g2, p2, t2, V, f (not from the paper's displayed table).
  E*  end-to-end random exact check: build aggregate lengths from random per-prime data of
      the two transforms, compute the exceptional excess from the definitions
      (m', M', Delta_child, a0, b2, r), and compare with the paper's chain
      excess <= (A - M) + 3 sigma + 5 delta_fr1 / 6.
  Z*  zero-slack witness: an explicit configuration where the excess equals A - M exactly
      (up to the sigma terms), and the max over v of (2.19).
  C*  controls that MUST fail: drop f from F2, drop the centred saving, shrink the saving by
      a fixed lambda, drop B_c.

Run: python3 -I theta_row_ledger.py [out.json]
Nothing here is floating point; every PASS is an exact rational or symbolic statement.
A finite random sample is not a proof of the inequalities; the symbolic and exhaustive
per-prime checks are the load-bearing ones.
"""
import json
import random
import sys
from fractions import Fraction as Fr

import sympy as sp

RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append({"check": name, "pass": bool(ok), "detail": str(detail)})
    print(("PASS " if ok else "FAIL ") + name + ("   " + str(detail) if detail else ""))


def pos(x):
    return x if x > 0 else 0 * x


# ---------------------------------------------------------------------------
# S1-S5: symbolic identities
# ---------------------------------------------------------------------------
(A, m, q, c, d, R, E, K0mK, w, wo, g, ell, c2, d2, g2, p2, t2, V, f, Bc, M_) = sp.symbols(
    "A m q c d R E K0mK w w_o g ell c2 d2 g2 p2 t2 V f B_c M", real=True)
M = m + q
qt = q + R + E                              # q~ = q + R + E          (old-eq:2.3)
K0 = 2 * A - c - d + R + E - m              # K_0                       (l. 13285)
K = K0 - K0mK                               # K = K_0 - (K_0 - K)
a0 = A - c - w                              # a_0                       (l. 13418)
b2 = (c2 + d2) / 2
mp = 2 * a0 - K - g - g2 - V                # m'                        (old-eq:2.13)
qp = qt + wo + t2 + V                       # q'
Mp = mp + qp                                # M'
Dchild = b2 - p2 + w + Bc + ell             # Delta_child               (old-eq:2.14)
J = d - c + K0mK - 2 * w + wo               # J                         (old-eq:2.8)

lhs215 = (mp - f) / 6 + a0 - b2 - (Mp + Dchild)
F1 = c / 6 + sp.Rational(5, 6) * (d + K0mK) + w / 3 + qt / 6 + wo + Bc - sp.Rational(5, 6) * g + ell
F2 = 2 * b2 - sp.Rational(5, 6) * g2 - p2 + t2 + V / 6 + f / 6
rhs215 = A - sp.Rational(5, 6) * M - F1 - F2
record("S1 (old-eq:2.15)-(2.16) identity", sp.simplify(lhs215 - rhs215) == 0,
       "lhs - rhs = " + str(sp.simplify(lhs215 - rhs215)))

inter = a0 - 2 * b2 + p2 - w - Bc - ell - sp.Rational(5, 6) * mp - qp - f / 6
record("S2 intermediate form (l. 14462-14466)", sp.simplify(lhs215 - inter) == 0)

# J >= 0, g = J, ell = 0:  F1 = c + 2w + q~/6 + w_o/6 + B_c   (l. 14474-14477)
F1_Jpos = F1.subs({g: J, ell: 0})
record("S3 F1 at g=J, ell=0 equals c+2w+q~/6+w_o/6+B_c",
       sp.simplify(F1_Jpos - (c + 2 * w + qt / 6 + wo / 6 + Bc)) == 0)

# (2.18h): t_- - r1 - r2 - (r - r1)_+ = (t_- - r2) - max(r, r1)
tm, r1, r2, rr = sp.symbols("t_- r1 r2 r", real=True)
ok = True
for _ in range(4000):
    vals = {tm: Fr(random.randint(0, 60), 7), r1: Fr(random.randint(0, 60), 7),
            r2: Fr(random.randint(0, 60), 7), rr: Fr(random.randint(0, 60), 7)}
    L_ = vals[tm] - vals[r1] - vals[r2] - pos(vals[rr] - vals[r1])
    R_ = (vals[tm] - vals[r2]) - max(vals[rr], vals[r1])
    ok &= (L_ == R_)
record("S4 (old-eq:2.18h) identity t- - r1 - r2 - (r-r1)_+ = (t- - r2) - max(r, r1)", ok,
       "4000 exact random cases")

# (2.14) from the exponent table at l. 13838-13861
Lam = a0 + qt + wo + w + Bc - sp.Symbol("s0")  # (old-eq:2.7) without eps_G
table = (K + g - ell - a0 + p2 - sp.Symbol("s0") + g2 - t2 - b2)
record("S5 (old-eq:2.14) = (2.7) minus the exponent table",
       sp.simplify(Lam - table - (Mp + Dchild)) == 0)

# ---------------------------------------------------------------------------
# P1-P2: per-prime F2 table, recomputed from definitions
# ---------------------------------------------------------------------------


def local_second(i, j0, unit):
    """Local (b2, g2, p2, t2, V, f) at one common prime of D2, E2 with multiplicities i, j0.

    Returns None if the local correlation vanishes (then the allocation does not occur).
    Rules (l. 13723-13751 and 14347-14352): equal multiplicity i, 6 !| i: unit -> t2 += 1,
    nonunit -> V += 1, and f += 2 if i == 1; equal 6 | i: neither; unequal: nonzero only if
    6 | min(i, j0) and the divided frequency is a unit; then neither t2 nor V.
    """
    if i == j0:
        if i % 6 != 0:
            if unit:
                return (Fr(i), Fr(i), Fr(1), Fr(1), Fr(0), Fr(0))
            return (Fr(i), Fr(i), Fr(1), Fr(0), Fr(1), Fr(2) if i == 1 else Fr(0))
        return (Fr(i), Fr(i), Fr(1), Fr(0), Fr(0), Fr(0))
    lo = min(i, j0)
    if lo % 6 != 0 or not unit:
        return None
    return (Fr(i + j0, 2), Fr(lo), Fr(1), Fr(0), Fr(0), Fr(0))


def F2loc(i, j0, unit, use_f=True):
    loc = local_second(i, j0, unit)
    if loc is None:
        return None
    b, gg, pp, tt, VV, ff = loc
    return 2 * b - Fr(5, 6) * gg - pp + tt + VV / 6 + (ff / 6 if use_f else 0), b


minslack, zeros, n = None, [], 0
for i in range(1, 121):
    for j0 in range(1, 121):
        for unit in (True, False):
            res = F2loc(i, j0, unit)
            if res is None:
                continue
            n += 1
            F2v, b = res
            s = F2v - Fr(2, 3) * b
            if minslack is None or s < minslack:
                minslack = s
            if s == 0:
                zeros.append((i, j0, "unit" if unit else "nonunit"))
record("P1 F2 >= 2 b2/3 at every admissible local type, 1 <= i, j0 <= 120",
       minslack >= 0, "cases=%d min slack=%s zero-slack types=%s" % (n, minslack, zeros[:6]))

# the four displayed lines of the table at l. 14507-14514
okt = True
for i in range(1, 121):
    if i % 6:
        okt &= F2loc(i, i, True)[0] == Fr(7 * i, 6)
        okt &= F2loc(i, i, False)[0] == Fr(7 * i - 5, 6) + (Fr(1, 3) if i == 1 else 0)
    else:
        okt &= F2loc(i, i, True)[0] == Fr(7 * i, 6) - 1
    for j0 in range(6, i, 6):
        okt &= F2loc(i, j0, True)[0] == i + Fr(j0, 6) - 1
record("P2 displayed F2 table (l. 14507-14514) agrees with the definition", okt)

# ---------------------------------------------------------------------------
# E1-E3: end-to-end random exact check from raw local data
# ---------------------------------------------------------------------------


def first_transform_local(i, j):
    """Local contributions to (c, d, p, R, B_c-numerator) at one first-transform common prime."""
    r = 1 if (i - j) % 6 else 0
    return Fr(i), Fr(j), Fr(1), Fr(r), Fr(3 * i - 5 * j - r)


def sample_config(rng, sigma, dfr1, kind):
    """Random exact configuration. Returns dict of aggregate lengths."""
    cfg = {}
    # first transform common primes
    c_ = d_ = p_ = R_ = Bnum = E_ = Fr(0)
    for _ in range(rng.randint(0, 3)):
        lam = Fr(rng.randint(1, 40), 400)
        i, j = rng.randint(1, 8), rng.randint(1, 8)
        lc, ld, lp, lR, lB = first_transform_local(i, j)
        c_ += lam * lc
        d_ += lam * ld
        p_ += lam * lp
        R_ += lam * lR
        Bnum += lam * lB
        if lR == 0 and rng.random() < 0.5:
            E_ += lam      # E <= p - R: Moebius-selected primes of the complementary mask
    Bc_ = pos(Bnum / 6)
    # second transform common primes
    c2_ = d2_ = g2_ = p2_ = t2_ = V_ = f_ = Fr(0)
    for _ in range(rng.randint(0, 3)):
        lam = Fr(rng.randint(1, 40), 400)
        while True:
            i, j0, unit = rng.randint(1, 13), rng.randint(1, 13), rng.random() < 0.5
            if rng.random() < 0.5:
                j0 = i
            loc = local_second(i, j0, unit)
            if loc is not None:
                break
        b, gg, pp, tt, VV, ff = loc
        c2_ += lam * i
        d2_ += lam * j0
        g2_ += lam * gg
        p2_ += lam * pp
        t2_ += lam * tt
        V_ += lam * VV
        f_ += lam * ff
    m_ = Fr(rng.randint(0, 400), 100)
    q_ = Fr(rng.randint(0, 100), 100)
    M_v = m_ + q_
    A_v = Fr(rng.randint(0, 600), 100)
    # frequency perturbation K0 - K in [-dfr1, K0]
    K0_v = 2 * A_v - c_ - d_ + R_ + E_ - m_
    K0mK_v = -dfr1 + Fr(rng.randint(0, 100), 100) * max(K0_v + dfr1, Fr(0))
    if kind == "zero":
        w_, wo_, ell_, extra = Fr(0), Fr(0), Fr(0), sigma
    elif kind == "main":
        w_, wo_, ell_, extra = Fr(0), Fr(0), sigma / 3, 2 * sigma
    else:
        ip = rng.choice([1, 6, 7])
        lp = sigma / 6 + Fr(rng.randint(0, 100), 100) * (sigma / 3 - sigma / 6)
        w_, wo_, ell_, extra = ip * lp, (lp if ip in (1, 7) else Fr(0)), Fr(0), sigma
    J_v = d_ - c_ + K0mK_v - 2 * w_ + wo_
    g_ = pos(J_v) + extra
    cfg.update(dict(A=A_v, m=m_, q=q_, M=M_v, c=c_, d=d_, p=p_, R=R_, E=E_, Bc=Bc_, c2=c2_,
                    d2=d2_, g2=g2_, p2=p2_, t2=t2_, V=V_, f=f_, K0mK=K0mK_v, w=w_, wo=wo_,
                    ell=ell_, g=g_, J=J_v))
    return cfg


def excess(cfg, centred=True, saving_loss=Fr(0)):
    """Nominal exceptional excess from the definitions (left side of (2.15) minus r)."""
    qt_ = cfg["q"] + cfg["R"] + cfg["E"]
    K0_ = 2 * cfg["A"] - cfg["c"] - cfg["d"] + cfg["R"] + cfg["E"] - cfg["m"]
    K_ = K0_ - cfg["K0mK"]
    a0_ = cfg["A"] - cfg["c"] - cfg["w"]
    b2_ = (cfg["c2"] + cfg["d2"]) / 2
    mp_ = 2 * a0_ - K_ - cfg["g"] - cfg["g2"] - cfg["V"]
    qp_ = qt_ + cfg["wo"] + cfg["t2"] + cfg["V"]
    Mp_ = mp_ + qp_
    Dch = b2_ - cfg["p2"] + cfg["w"] + cfg["Bc"] + cfg["ell"]
    L_ = cfg["M"] / 4
    v_ = cfg["c"] + cfg["w"] + min(cfg["c2"], cfg["d2"])
    r_ = pos(L_ - v_ - saving_loss) if centred else Fr(0)
    return (mp_ - cfg["f"]) / 6 + a0_ - b2_ - r_ - (Mp_ + Dch)


rng = random.Random(20261010)
sigma, dfr1 = Fr(1, 50), Fr(1, 400)
worst = {"zero": None, "main": None, "err": None}
worst_unc = {"zero": None, "main": None, "err": None}
nsamp = 0
ok_c, ok_u = True, True
for kind in ("zero", "main", "err"):
    for _ in range(20000):
        cfg = sample_config(rng, sigma, dfr1, kind)
        nsamp += 1
        x = excess(cfg) - (cfg["A"] - cfg["M"])
        bound = 3 * sigma + Fr(5, 6) * dfr1
        ok_c &= x <= bound
        if worst[kind] is None or x > worst[kind]:
            worst[kind] = x
        xu = excess(cfg, centred=False) - (cfg["A"] - Fr(5, 6) * cfg["M"])
        ok_u &= xu <= bound
        if worst_unc[kind] is None or xu > worst_unc[kind]:
            worst_unc[kind] = xu
record("E1 centred: excess - (A - M) <= 3 sigma + 5 dfr1/6 (from raw local data)", ok_c,
       "samples=%d sigma=%s dfr1=%s max(excess-(A-M)) by type %s" % (
           nsamp, sigma, dfr1, {k: str(v) for k, v in worst.items()}))
record("E2 uncentred: excess - (A - 5M/6) <= 3 sigma + 5 dfr1/6 (from raw local data)", ok_u,
       "max(excess-(A-5M/6)) by type %s" % {k: str(v) for k, v in worst_unc.items()})

# E3: the paper's lower bounds (2.17) on the same samples, F1 and F2 separately
ok1, ok2 = True, True
rng = random.Random(7)
for kind in ("zero", "main", "err"):
    for _ in range(20000):
        cfg = sample_config(rng, sigma, dfr1, kind)
        qt_ = cfg["q"] + cfg["R"] + cfg["E"]
        F1v = (cfg["c"] / 6 + Fr(5, 6) * (cfg["d"] + cfg["K0mK"]) + cfg["w"] / 3 + qt_ / 6
               + cfg["wo"] + cfg["Bc"] - Fr(5, 6) * cfg["g"] + cfg["ell"])
        b2_ = (cfg["c2"] + cfg["d2"]) / 2
        F2v = 2 * b2_ - Fr(5, 6) * cfg["g2"] - cfg["p2"] + cfg["t2"] + cfg["V"] / 6 + cfg["f"] / 6
        ok1 &= F1v >= Fr(2, 3) * (cfg["c"] + cfg["w"]) - 3 * sigma - Fr(5, 6) * dfr1
        ok2 &= F2v >= Fr(2, 3) * b2_
record("E3 (old-eq:2.17) F1 >= 2(c+w)/3 - 3 sigma - 5 dfr1/6 and F2 >= 2 b2/3 on 60000 samples",
       ok1 and ok2)

# ---------------------------------------------------------------------------
# Z1-Z2: zero slack
# ---------------------------------------------------------------------------
Av, vv = sp.symbols("A v", real=True)
Ms = sp.Symbol("M", positive=True)
Ls = Ms / 4
dfc = Av - sp.Rational(5, 6) * Ms - sp.Rational(2, 3) * vv - sp.Max(Ls - vv, 0)
low = sp.simplify(Av - sp.Rational(5, 6) * Ms - Ls + vv / 3)       # v <= L
high = sp.simplify(Av - sp.Rational(5, 6) * Ms - sp.Rational(2, 3) * vv)  # v >= L
ok = (sp.diff(low, vv) == sp.Rational(1, 3) and sp.diff(high, vv) == -sp.Rational(2, 3)
      and sp.simplify(low.subs(vv, Ls) - (Av - Ms)) == 0
      and sp.simplify(high.subs(vv, Ls) - (Av - Ms)) == 0)
record("Z1 (old-eq:2.19) max_v [A - 5M/6 - 2v/3 - (L-v)_+] = A - M, attained only at v = L", ok)

# explicit configuration: zero slots, first transform one prime (i,j)=(2,1), second transform
# nonunit multiplicity-one primes, q = E = 0, K = K0, chosen so that v = c + c2 = L.
Mv = Fr(4)
lam1 = Fr(1, 4)                  # c = 2 lam1 = 1/2, d = lam1
c2v = Mv / 4 - 2 * lam1          # so that v = L
cfg = dict(A=Mv, m=Mv, q=Fr(0), M=Mv, c=2 * lam1, d=lam1, p=lam1, R=lam1, E=Fr(0),
           Bc=pos((3 * 2 - 5 * 1 - 1) * lam1 / 6), c2=c2v, d2=c2v, g2=c2v, p2=c2v, t2=Fr(0),
           V=c2v, f=2 * c2v, K0mK=Fr(0), w=Fr(0), wo=Fr(0), ell=Fr(0))
cfg["J"] = cfg["d"] - cfg["c"]
for sg in (Fr(0), Fr(1, 100)):
    cfg["g"] = pos(cfg["J"]) + sg
    x = excess(cfg)
    record("Z2 witness (2,1)-prime + nonunit mult-1 primes, v = L, sigma=%s: excess = A - M + 5 sigma/6"
           % sg, x == cfg["A"] - cfg["M"] + Fr(5, 6) * sg, "excess=%s" % x)
# the witness is realizable at the level of lengths: K0 >= 0, a0 >= 0, m' - f >= 0
K0w = 2 * cfg["A"] - cfg["c"] - cfg["d"] + cfg["R"] + cfg["E"] - cfg["m"]
a0w = cfg["A"] - cfg["c"]
mpw = 2 * a0w - K0w - cfg["g"] - cfg["g2"] - cfg["V"]
record("Z3 witness lengths admissible (K0, a0, m'-f >= 0)", K0w >= 0 and a0w >= 0 and mpw - cfg["f"] >= 0,
       "K0=%s a0=%s m'=%s f=%s" % (K0w, a0w, mpw, cfg["f"]))

# ---------------------------------------------------------------------------
# C1-C5: controls that must fail
# ---------------------------------------------------------------------------
# C1: drop f/6 from F2 -> the multiplicity-one nonunit prime violates F2 >= 2b2/3
F2v, b = F2loc(1, 1, False, use_f=False)
record("C1 control: without f, F2 < 2b2/3 at nonunit i=1 (expected FAIL of the bound)",
       F2v < Fr(2, 3) * b, "F2=%s 2b2/3=%s" % (F2v, Fr(2, 3) * b))
# C2: without the centred saving, the witness has excess A - 5M/6 - M/6 ... set v = 0
cfg0 = dict(cfg)
for k in ("c", "d", "p", "R", "Bc", "c2", "d2", "g2", "p2", "V", "f"):
    cfg0[k] = Fr(0)
cfg0["g"] = Fr(0)
xu = excess(cfg0, centred=False)
record("C2 control: v = 0 and no centring gives excess A - 5M/6 = M/6 > 0 at A = M",
       xu == cfg0["A"] - Fr(5, 6) * cfg0["M"] and xu > 0, "excess=%s" % xu)
# C3: a fixed loss lambda in the saving r -> max over v becomes A - M + 2 lambda/3
lamb = Fr(1, 10)
best = max(Fr(4) - Fr(5, 6) * 4 - Fr(2, 3) * vq - pos(Fr(1) - vq - lamb)
           for vq in [Fr(k, 1000) for k in range(0, 2001)])
record("C3 control: saving (L - v - lambda)_+ gives max = A - M + 2 lambda/3 (fixed-power loss)",
       best == Fr(2, 3) * lamb, "max=%s at A=M=4, lambda=%s" % (best, lamb))
# C4: drop B_c in F1 at J<0 for the (2,1)-type configuration with R=0 forced -> F1 < 2c/3
#      (shows B_c and q~ >= R are both load-bearing at Z3)
c_, d_, R_ = Fr(5), Fr(2), Fr(0)
F1_noB = c_ / 6 + Fr(5, 6) * d_ + R_ / 6
record("C4 control: dropping B_c at 3c > 5d gives F1 < 2c/3", F1_noB < Fr(2, 3) * c_,
       "F1=%s 2c/3=%s" % (F1_noB, Fr(2, 3) * c_))

npass = sum(r["pass"] for r in RESULTS)
print("%d/%d PASS (C* controls PASS when the mutated claim is shown to fail)" % (npass, len(RESULTS)))
if len(sys.argv) > 1:
    with open(sys.argv[1], "w") as fh:
        json.dump({"source_sha256": "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3",
                   "results": RESULTS, "npass": npass, "n": len(RESULTS)}, fh, indent=1)
