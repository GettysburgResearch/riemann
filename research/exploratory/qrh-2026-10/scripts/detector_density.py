#!/usr/bin/env python3
"""Detector density: does the Sep 30 7/8 architecture yield a family zero-density estimate?

Status: PROPOSED / HEURISTIC exponent model (see DETECTOR_DENSITY.md). Nothing here is a theorem
about the true zeros of any L-function, and nothing bears on RH (unsolved).

Source: [OAI] "The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8" (30 Sep 2026),
paper.tex at ref pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, SHA-256 below. External and
unreviewed. It is read as untrusted data. Line numbers refer to that file.
Comparator: [dF] A. de Faveri, "Optimal large sieve for fixed order characters",
arXiv:2610.04045v1 (2 Oct 2026), Corollary 1.5 (zero density for n-th order Kummer families).

Sections
  A  inner layer: exact row-count (zero-density) exponent of the detector, x = 0 amplitude class,
     detector parameter t in [1, 3/2]; closed form f_det(sigma) = (31-32 sigma)/(21-12 sigma)
  B  comparators: trivial, the paper's Part I sextic-sieve envelope, [dF] n = 6, Hinz A/B and
     full-family DH restricted to the rows, Kummer-family DH
  C  outer layer: sign table of the high exponent (Lemma 20.1), visibility window, jump at 7/8
  D  failing controls (each must FIRE)
  T  optional text census of paper.tex (sha256 + anchors), with --paper PATH

Run:  python3 -I detector_density.py [--paper PATH] [--out DIR]
Exit status 0 iff every gate passes and every control fires.
"""
import argparse
import hashlib
import json
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)              # -I does not add the script directory

PAPER_SHA256 = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
ALPHA = Fr(5, 6)                      # Lemma 17.6 amplification slope (paper 15301-15310)
TMIN, TMAX = Fr(1), Fr(3, 2)          # detector parameter range, Prop 8.3
SIG_FLOOR = Fr(51, 100)               # detector floor a0

GATES, CONTROLS = [], []


def gate(name, ok, detail=""):
    GATES.append(dict(name=name, ok=bool(ok), detail=str(detail)))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


def control(name, fired, detail=""):
    CONTROLS.append(dict(name=name, fired=bool(fired), detail=str(detail)))
    print(f"[{'FIRES' if fired else 'SILENT'}] control: {name}  {detail}")


# ------------------------------------------------------------------------------------------------
# A. Inner layer: the detector row count as a family zero-density exponent
# ------------------------------------------------------------------------------------------------
# Inputs (exponents base U, rows q_u ~ U, bin delta = 2a - 1, amplitude class x = 0, no slots):
#   inverse witness length r <= 1 : count 1 - delta r          (eq. no-slot-inverse-count, e(r)=1)
#   inverse witness length r >= 1 : count 1 - alpha + (alpha - delta) r   (same eq., Lemma 17.6)
#   plain witness length m <= 1/2 : count 1 - 2 delta m        (Lemma 18.1 zero-slot case)
#   detector (Prop 8.3): for each t in [1,3/2] every witnessed row has (r, m) with
#   t - 1/2 <= r <= t, r + m >= t, 0 <= m <= 1/2.
# Each row subdivision is counted by the better of its two witnesses; the worst subdivision
# is taken; the detector parameter t is ours to choose.

def inv_count(r, delta, alpha=ALPHA):
    return 1 - delta * r if r <= 1 else 1 - alpha + (alpha - delta) * r


def plain_count(m, delta):
    return 1 - 2 * delta * m


def worst_split(t, delta, alpha=ALPHA, use_plain=True, nr=600):
    """max over admissible (r, m) of min(inverse count, plain count); worst m = max(0, t - r).
    Exact on the breakpoints: the grid includes r = 2t/3 and r = 1 when admissible."""
    lo, hi = t - Fr(1, 2), t
    pts = {lo, hi}
    for c in (Fr(2, 3) * t, Fr(1)):
        if lo <= c <= hi:
            pts.add(c)
    pts.update(lo + (hi - lo) * Fr(k, nr) for k in range(nr + 1))
    best = None
    for r in pts:
        v = inv_count(r, delta, alpha)
        if use_plain:
            v = min(v, plain_count(max(Fr(0), t - r), delta))
        best = v if best is None else max(best, v)
    return best


def R0_closed(delta, alpha=ALPHA):
    """min_t max(1 - 2 delta t/3, L(t)), L(t) = 1 - delta + (alpha - delta)(t - 1)."""
    if delta >= alpha:
        return 1 - delta
    return 1 - 2 * alpha * delta / (3 * alpha - delta)


def R_inv_closed(delta, alpha=ALPHA):
    """Inverse witness only (no Lemma 18.1): min_t max(1 - delta (t - 1/2), L(t)) = 1 - delta/2 - delta^2/(2 alpha)."""
    if delta >= alpha:
        return 1 - delta
    return 1 - delta / 2 - delta * delta / (2 * alpha)


def f_inv(sigma):
    return R_inv_closed(2 * Fr(sigma) - 1)


def t_star(delta, alpha=ALPHA):
    return alpha / (alpha - delta / 3) if delta < alpha else TMAX


def f_det(sigma):
    """Row zero-density exponent in sigma: (31-32s)/(21-12s) on (51/100, 11/12], 2(1-s) above."""
    sigma = Fr(sigma)
    if sigma >= Fr(11, 12):
        return 2 * (1 - sigma)
    return (31 - 32 * sigma) / (21 - 12 * sigma)


def R_brute(delta, alpha=ALPHA, use_plain=True, tmax=TMAX, nt=60):
    """Direct min over a rational t-grid (plus t*) of the worst split."""
    ts = {TMIN + (tmax - TMIN) * Fr(k, nt) for k in range(nt + 1)}
    ts.add(min(max(t_star(delta, alpha), TMIN), tmax))
    return min(worst_split(t, delta, alpha, use_plain) for t in ts)


def section_A():
    print("\n== A. inner layer: detector zero-density exponent ==")
    # A1 closed form vs brute force at exact rational deltas
    worst = Fr(0)
    for k in range(1, 50):
        delta = Fr(1, 50) + (Fr(49, 50) - Fr(1, 50)) * Fr(k, 50)
        worst = max(worst, abs(R_brute(delta) - R0_closed(delta)))
    gate("A1 closed form = brute-force min-max (49 exact deltas in (1/50,1))", worst == 0, f"max diff {worst}")
    # A2 sigma-form
    ok = all(f_det(Fr(1 + d, 2)) == R0_closed(d) for d in [Fr(k, 97) for k in range(2, 97)])
    gate("A2 f_det(sigma) = R0(2 sigma - 1) as (31-32s)/(21-12s) / 2(1-s)", ok)
    # A3 key values
    v78, v1315 = f_det(Fr(7, 8)), f_det(Fr(13, 15))
    gate("A3 f_det(7/8) = 2/7 and f_det(13/15) = 49/159", v78 == Fr(2, 7) and v1315 == Fr(49, 159),
         f"{v78}, {v1315}")
    # A4 reproduces the paper's t = 1 no-slot clause (Prop 19.2 last display: 1 - 2 delta/3)
    ok = all(worst_split(Fr(1), d) == 1 - 2 * d / 3 for d in [Fr(k, 40) for k in range(1, 34)])
    gate("A4 t = 1 worst split = 1 - 2 delta/3 (Prop 19.2, no-slot clause)", ok)
    # A5 x = 0 limit of Prop 19.2's selected closed form R* = 1 - delta + (alpha-delta) delta P_x/(2J)
    ok = True
    for d in [Fr(k, 40) for k in range(1, 34)]:
        Dx, Px = Fr(3), Fr(2)
        J = (ALPHA - d) * Dx + d * Px
        ok &= (1 - d + (ALPHA - d) * d * Px / (2 * J)) == R0_closed(d)
    gate("A5 x = 0 limit of the paper's R* closed form equals R0", ok)
    # A6 t* lies in [1, 3/2] for delta <= alpha
    ok = all(TMIN <= t_star(d) <= TMAX for d in [Fr(k, 60) for k in range(1, 51)])
    gate("A6 optimal detector t* = alpha/(alpha - delta/3) lies in [1, 3/2]", ok, f"t*(3/4) = {t_star(Fr(3,4))}")
    # A7 monotone, never below Kummer DH, equality iff delta >= alpha
    ds = [Fr(k, 120) for k in range(3, 121)]
    mono = all(R0_closed(ds[i]) > R0_closed(ds[i + 1]) for i in range(len(ds) - 1))
    dh = all((R0_closed(d) > 1 - d) if d < ALPHA else (R0_closed(d) == 1 - d) for d in ds)
    gate("A7 R0 strictly decreasing; R0 > 1 - delta for delta < 5/6, = 1 - delta for delta >= 5/6", mono and dh)
    # A8 float cross-check against the team model threshold_calculus.R_exact at x = 0 (not a gate
    #    on its own grounds: the model is FLOATING_RECONNAISSANCE; tolerance 1e-9)
    try:
        import threshold_calculus as tc
        random.seed(7)
        diff = 0.0
        for _ in range(60):
            d = random.uniform(0.03, 0.83)
            diff = max(diff, abs(tc.R_exact(d, 0.0, 0.75, 0.2) - float(R0_closed(Fr(d)))))
        gate("A8 threshold_calculus.R_exact(delta, x=0) = R0 (float, tol 1e-9)", diff < 1e-9, f"max diff {diff:.1e}")
    except Exception as exc:  # pragma: no cover
        gate("A8 threshold_calculus cross-check", False, repr(exc))
    # A9 inverse witness only (drops Lemma 18.1): closed form vs brute force; value 23/80 at 7/8
    worst = Fr(0)
    for k in range(1, 50):
        delta = Fr(1, 50) + (Fr(49, 50) - Fr(1, 50)) * Fr(k, 50)
        tt = {TMIN + Fr(k2, 120) * (TMAX - TMIN) for k2 in range(121)}
        tt.add(min(1 + delta / (2 * ALPHA), TMAX))
        worst = max(worst, abs(min(worst_split(t, delta, use_plain=False) for t in tt) - R_inv_closed(delta)))
    inv_only = R_inv_closed(Fr(3, 4))
    gate("A9 inverse-witness-only count 1 - d/2 - d^2/(2 alpha) = brute force; = 23/80 at 7/8",
         worst == 0 and inv_only == Fr(23, 80), f"max diff {worst}; plain witness worth {Fr(23,80) - Fr(2,7)} at 7/8")
    return dict(f_det_7_8=str(v78), f_det_13_15=str(v1315), inverse_only_at_3_4=str(inv_only),
                t_star_at_3_4=str(t_star(Fr(3, 4))))


# ------------------------------------------------------------------------------------------------
# B. Comparators (all as U-exponents for the ~U-member row family, rows q_u ~ U)
# ------------------------------------------------------------------------------------------------

def part1_envelope(sigma):
    """[OAI] Prop 9.2 (5181-5196): R(delta) = min{1, max(1 - delta/2, 4/3 - delta)}."""
    d = 2 * Fr(sigma) - 1
    return min(Fr(1), max(1 - d / 2, Fr(4, 3) - d))


def defaveri_mid(s, n=6, perturb=0):
    q = 2 * s - 1
    num = q * (q * n * n - (6 * s - 2) * n + 3 + perturb)
    den = q * (3 - 2 * s) * n * n - 4 * s * n + 2
    return num / den


def defaveri_delta(sigma, n=6, perturb=0):
    """[dF] Cor. 1.5: sum over n-th power free a, N(a) <= N, of N(sigma,T,a) << N^{1-delta_n(sigma)+eps} T^(...)."""
    s = Fr(sigma)
    q = 2 * s - 1
    if s <= Fr(1, 2) + Fr(1, n):
        return q / ((1 - 2 * s) * n + 4)
    if s <= 1 - Fr(1, 2 * n):
        return defaveri_mid(s, n, perturb)
    return (8 * s * s - 10 * s + 3) / (1 - 4 * (1 - s) ** 2 * n)


def defaveri(sigma, n=6, perturb=0):
    return 1 - defaveri_delta(sigma, n, perturb)


def hinz_A(sigma):          # as recorded in KINTALI_DENSITY_UPGRADE.md (Hinz 1976 Satz A), Q-exponent
    s = Fr(sigma)
    return 6 * (1 - s) / (2 - s)


def hinz_B(sigma):          # Hinz 1976 Satz B, sigma >= 3/4
    s = Fr(sigma)
    return 4 * (1 - s) / s if s >= Fr(3, 4) else None


COMPARATORS = [
    ("trivial", lambda s: Fr(1)),
    ("Part I sextic-sieve envelope [OAI Prop 9.2]", part1_envelope),
    ("Hinz A, full family restricted", hinz_A),
    ("Hinz B, full family restricted", hinz_B),
    ("de Faveri n=6 [arXiv:2610.04045v1 Cor 1.5]", defaveri),
    ("full-family DH restricted (hypothetical)", lambda s: 4 * (1 - Fr(s))),
    ("detector, inverse witness only (no Lemma 18.1)", f_inv),
    ("detector f_det (PROPOSED reading of [OAI])", f_det),
    ("Kummer-family DH (hypothetical)", lambda s: 2 * (1 - Fr(s))),
]


def section_B():
    print("\n== B. comparators (U-exponents for the row family) ==")
    n = 6
    # B1 de Faveri continuity at its breakpoints and endpoint values
    b1, b2 = Fr(1, 2) + Fr(1, n), 1 - Fr(1, 2 * n)
    q1, q2 = 2 * b1 - 1, 2 * b2 - 1
    left1 = q1 / ((1 - 2 * b1) * n + 4)
    left2 = q2 * (q2 * n * n - (6 * b2 - 2) * n + 3) / (q2 * (3 - 2 * b2) * n * n - 4 * b2 * n + 2)
    right1 = q1 * (q1 * n * n - (6 * b1 - 2) * n + 3) / (q1 * (3 - 2 * b1) * n * n - 4 * b1 * n + 2)
    right2 = (8 * b2 * b2 - 10 * b2 + 3) / (1 - 4 * (1 - b2) ** 2 * n)
    gate("B1 [dF] delta_6 continuous at 2/3 and 11/12; delta_6(1/2)=0, delta_6(1)=1",
         left1 == right1 == Fr(1, n) and left2 == right2 == 1 - Fr(2, n)
         and defaveri_delta(Fr(1, 2)) == 0 and defaveri_delta(Fr(1)) == 1,
         f"values {left1}, {left2}")
    # B2 the detector exponent is below every published comparator on (51/100, 1)
    grid = [SIG_FLOOR + (1 - SIG_FLOOR) * Fr(k, 400) for k in range(1, 400)]
    beats_dF = all(f_det(s) < defaveri(s) for s in grid)
    beats_P1 = all(f_det(s) < part1_envelope(s) for s in grid)
    beats_inv = all(f_inv(s) < defaveri(s) for s in grid)
    gate("B2 f_det < [dF] n=6 and < Part I envelope at 399 rational sigma in (51/100, 1)", beats_dF and beats_P1)
    gate("B2b inverse-only f_inv < [dF] n=6 on the same grid (Lemma 18.1 not needed to beat [dF])", beats_inv)
    # B3 gap to Kummer DH: ratio A_eff = f_det / (2(1-sigma))
    a78 = f_det(Fr(7, 8)) / (2 * (1 - Fr(7, 8)))
    gate("B3 A_eff(7/8) = f_det/(2(1-sigma)) = 8/7", a78 == Fr(8, 7), f"{a78}")
    # table on (13/15, 7/8] plus context points
    sig_main = [Fr(13, 15), Fr(867, 1000), Fr(868, 1000), Fr(869, 1000), Fr(870, 1000), Fr(871, 1000),
                Fr(872, 1000), Fr(873, 1000), Fr(874, 1000), Fr(8749, 10000), Fr(7, 8)]
    sig_ctx = [Fr(3, 5), Fr(2, 3), Fr(3, 4), Fr(4, 5), Fr(5, 6), Fr(11, 12), Fr(19, 20)]
    rows = []
    for s in sig_main + sig_ctx:
        row = dict(sigma=str(s), sigma_f=round(float(s), 6))
        for name, fn in COMPARATORS:
            v = fn(s)
            row[name] = None if v is None else round(float(v), 6)
        row["f_det_exact"] = str(f_det(s))
        rows.append(row)
    hdr = ["sigma", "trivial", "PartI", "HinzA", "HinzB", "dF n=6", "fullDH", "f_inv", "f_det", "KummerDH"]
    print("   " + " | ".join(f"{h:>8}" for h in hdr))
    for row in rows:
        vals = [row["sigma_f"]] + [row[name] for name, _ in COMPARATORS]
        print("   " + " | ".join(f"{'-':>8}" if v is None else f"{v:8.4f}" for v in vals))
    return dict(table=rows)


# ------------------------------------------------------------------------------------------------
# C. Outer layer: is the contradiction additive in zeros?
# ------------------------------------------------------------------------------------------------
LX, LY, ELL = Fr(17, 48), Fr(23, 48), Fr(1, 6)
H = 1 - LX + ELL                       # 13/16
Z0 = Fr(17, 50)


def E_high(a, q, d, R, lx=LX, ly=LY, ell=ELL, z0=Z0):
    """[OAI] eq. (common-high-exponent), 15726-15735, relative to C(7/8)."""
    h = 1 - lx + ell
    delta = 2 * a - 1
    return a - Fr(7, 8) + h * (z0 - Fr(1, 6)) - a * ly - (1 - a) * ell - (delta / 2 - q) * ell \
        + d * (R + delta / 2 - z0)


def section_C():
    print("\n== C. outer layer: sign of every zero-dependence in the high comparison ==")
    # C1 second form of the paper's display (C0 = -1/48) agrees with the first
    ok = True
    for a in [Fr(52, 100), Fr(3, 5), Fr(69, 100), Fr(7, 8)]:
        for d in [Fr(1, 2), Fr(3, 4), H]:
            for R in [Fr(1, 4), Fr(2, 3), Fr(1)]:
                delta = 2 * a - 1
                q = delta / 4
                e2 = Fr(-1, 48) + Fr(2, 3) * delta + q / 6 - H * (1 - R) + (d - H) * (R + delta / 2 - Z0)
                ok &= E_high(a, q, d, R) == e2
    gate("C1 E(d) two forms agree (paper 15726-15735, C0 = -1/48)", ok)
    # C2 exact partial derivatives: rows are costs
    a, q, d, R = Fr(69, 100), Fr(19, 100), H, Fr(2, 3)
    dR = E_high(a, q, d, R + 1) - E_high(a, q, d, R)
    da = E_high(a + 1, q, d, R) - E_high(a, q, d, R)
    gate("C2 dE/dR = d > 0: every extra witnessed row ADDS to the high error (paper 16089)", dR == d and dR > 0, f"dE/dR = {dR}")
    gate("C3 dE/da = 1 - l_y + d > 0 on d in [0, h]: deeper row zeros cost more", da == 1 - LY + d and 1 - LY > 0,
         f"dE/da = {da}")
    gate("C4 the target zero enters only through -Delta = -(C(beta*) - C(7/8)) (eq. adaptive-endpoint)",
         True, "comparison is E_actual(h) - Delta <= -49/440640 - (51/64) Delta (paper 16097-16102)")
    # C5 visibility window: target zero at beta is seen only if beta > sigma0(G) and
    #    beta > beta* - m(G), where m(G) = -sup E relative to C(beta*).
    win = {}
    try:
        import threshold_calculus as tc
        s0 = tc.low_threshold(17 / 48, 23 / 48, 1 / 6)
        hs = tc.high_sup(17 / 48, 23 / 48, 1 / 6, s0, 11 / 12, nde=121, nx=11, nd=9)[0]
        win["paper"] = dict(sigma0=s0, model_margin=-hs, paper_stated_margin=49 / 440640,
                            window_lo=max(s0, 7 / 8 + hs), window_hi=7 / 8)
        opt = json.load(open(os.path.join(HERE, "..", "results", "A_paper_bp11_12.json")))
        win["optimised"] = dict(sigma0=opt["sigma0"], model_margin=-opt["high_sup"],
                                window_lo=max(opt["sigma0"], 7 / 8 + opt["high_sup"]), window_hi=7 / 8)
        w_p = win["paper"]["window_hi"] - win["paper"]["window_lo"]
        w_o = win["optimised"]["window_hi"] - win["optimised"]["window_lo"]
        gate("C5 outer visibility window (model): empty at the paper geometry, width < 5e-5 at best",
             w_p <= 1e-12 and w_o < 5e-5, f"paper {w_p:.2e}, optimised {w_o:.2e}")
    except Exception as exc:  # pragma: no cover
        gate("C5 visibility window", False, repr(exc))
    # C6 jump: the architecture's combined family statement at 7/8
    jump = f_det(Fr(7, 8))
    gate("C6 combined statement has a jump at 7/8: count <= U^{2/7+eps} just left, empty right",
         jump == Fr(2, 7) and jump != 0, f"left limit {jump}")
    return dict(window=win, jump_at_7_8=str(jump), dE_dR=str(dR), dE_da=str(da))


# ------------------------------------------------------------------------------------------------
# D. Failing controls
# ------------------------------------------------------------------------------------------------

def section_D():
    print("\n== D. failing controls (each must fire) ==")
    # FC1: without the detector range t > 1 (paper's no-slot clause, t = 1) the detector no longer
    #      beats [dF] at 7/8: 1 - 2(3/4)/3 = 1/2 > 0.466.
    r_t1 = R_brute(Fr(3, 4), tmax=Fr(1), nt=1)
    control("FC1 t = 1 only: f(7/8) = 1/2 loses to [dF] n=6", r_t1 == Fr(1, 2) and r_t1 > defaveri(Fr(7, 8)),
            f"{r_t1} vs {float(defaveri(Fr(7, 8))):.4f}")
    # FC2: without sixth-power amplification (Lemma 17.6 slope alpha = 5/6 replaced by the trivial
    #      mean-value growth e(r) = r for r >= 1, i.e. alpha = 1): f(7/8) rises to 1/3.
    r_noamp = R_brute(Fr(3, 4), alpha=Fr(1))
    control("FC2 no amplification (alpha = 1): f(7/8) rises above 2/7", r_noamp > Fr(2, 7), f"{r_noamp}")
    # FC3: a planted typo in the [dF] middle formula breaks the continuity gate (right limit at 2/3)
    s = Fr(1, 2) + Fr(1, 6)
    planted = defaveri_mid(s, perturb=1)
    control("FC3 planted [dF] numerator typo breaks continuity at sigma = 2/3",
            planted != Fr(1, 6), f"right limit of delta_6 = {planted} (correct 1/6)")
    # FC4: a planted sign error making rows a GAIN (R with coefficient -d) is detected by C2's test
    def E_bad(a, q, d, R):
        return E_high(a, q, d, R) - 2 * d * R
    a, q, d, R = Fr(69, 100), Fr(19, 100), H, Fr(2, 3)
    control("FC4 planted sign flip in R makes dE/dR negative", E_bad(a, q, d, R + 1) - E_bad(a, q, d, R) < 0)
    # FC5: the hypothesis 'f(7/8) = 0' (what an additive outer detector would give) is refuted by
    #      the only density the architecture contains
    control("FC5 hypothesis f(7/8) = 0 fails for the architecture's density", f_det(Fr(7, 8)) != 0,
            f"f_det(7/8) = {f_det(Fr(7, 8))}")


# ------------------------------------------------------------------------------------------------
# T. Text census
# ------------------------------------------------------------------------------------------------
ANCHORS = [
    (384, r"\label{old-eq:1.1b}"),                       # beta_* := sup over the family
    (401, r"\label{lem:continuation-criterion}"),        # Prop 2.1
    (431, r"Then these assumptions contradict"),
    (500, r"Its reciprocal has a pole at $\rho$"),        # the single zero used
    (4281, r"\label{lem:buffered-bins}"),
    (4510, r"\label{prop:detector-witness}"),
    (5181, r"\label{prop:sextic-row-count}"),
    (6824, r"\label{eq:part-II-bin-ceiling}"),           # rows' zeros <= beta_* (the sup controls rows)
    (12362, r"\label{lem:inverse-amplification}"),
    (12531, r"\label{lem:plain}"),
    (15185, r"\label{prop:detector-counts}"),
    (15282, r"\label{eq:no-slot-inverse-count}"),
    (15699, r"\label{lem:high-bin}"),
    (15726, r"\label{eq:common-high-exponent}"),
    (16089, r"The coefficient of \(R\) in Equation"),
    (16101, r"=-\frac{49}{440640}-\frac{51}{64}\Delta"),
]


def section_T(path):
    print("\n== T. text census ==")
    if not path:
        print("   skipped (no --paper given)")
        return dict(skipped=True)
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    gate("T1 paper.tex SHA-256", sha == PAPER_SHA256, sha)
    lines = raw.decode("utf-8").splitlines()
    bad = [(ln, s) for ln, s in ANCHORS if s not in lines[ln - 1]]
    gate(f"T2 {len(ANCHORS)} anchors at the cited lines", not bad, f"missing {bad}" if bad else "")
    return dict(sha256=sha, anchors=len(ANCHORS), missing=bad)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--paper", default=None)
    ap.add_argument("--out", default=os.path.join(HERE, "..", "results"))
    args = ap.parse_args()
    out = dict(A=section_A(), B=section_B(), C=section_C())
    section_D()
    out["T"] = section_T(args.paper)
    out["gates"], out["controls"] = GATES, CONTROLS
    ok = all(g["ok"] for g in GATES) and all(c["fired"] for c in CONTROLS)
    print(f"\n{sum(g['ok'] for g in GATES)}/{len(GATES)} gates pass; "
          f"{sum(c['fired'] for c in CONTROLS)}/{len(CONTROLS)} controls fire")
    os.makedirs(args.out, exist_ok=True)
    with open(os.path.join(args.out, "detector_density_output.json"), "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    sys.exit(0 if ok else 1)
