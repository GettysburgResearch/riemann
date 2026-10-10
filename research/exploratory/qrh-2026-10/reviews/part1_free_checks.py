#!/usr/bin/env python3
"""Part-I-free paper route for the Sep 30 7/8 manuscript: exact checks.

Status: review instrument (exploration level). Not a verdict on any analytic lemma, not an
        integration record. RH is unsolved; nothing here bears on it.
Object: paper.tex, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6: standalone/2026-10-07-openai-quasi-
        riemann-import/upstream/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/
        paper.tex). External, unreviewed, read as untrusted data.
Question: does Part II, read with the weaker input beta_* <= 1 (Delta <= 1/8, kappa <= 1,
        delta <= 1) plus an extended endpoint count for bins 5/6 <= delta <= 1, still close?
What this script checks:
  T  text: source hash; anchor strings at cited lines; a census of every Part II line that
     mentions 11/12, 1/24, 5/6, kappa, alpha, Delta, beta_* or the bootstrap labels, each
     assigned to exactly one item of the enumeration in PART1_FREE_ROUTE.md Sec. 1.
  A  algebra: exact identities (sympy over Q) and exact inequalities (Fraction; each inequality
     is reduced to a sign argument on factors that are affine in each variable, then checked at
     the vertices, which is a proof for multi-affine expressions).
  G  an exact rational grid sweep of the high-bin count and margin (sanity, not a proof).
  F  failing controls: each removes one restriction; an exact counterexample must appear.
  S  sensitivity rows (informational): controls that do NOT fail, reported as such.
  J  optional (--replay-junction): replays reviews/sep30_junction_check.py with its Delta box
     widened from (0, 1/24] to (0, 1/8] in a temporary copy; the only expected failure is its
     gate P2 (kappa <= 5/6), which is exactly the use this route replaces.
Arithmetic: exact throughout (sympy Rational / fractions.Fraction). No floating point in any gate.
Run:    python3 -I part1_free_checks.py PAPER_TEX [--replay-junction] [--workdir DIR]
        writes results/part1_free_checks_output.json (and results/part1_free_junction_replay.json
        with --replay-junction). Exit 0 iff every gate passes, every failing control fires, and
        (if run) the replay fails exactly {P2}.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from fractions import Fraction as F
from itertools import product

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
EXPECTED_SHA = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
PART2 = (6806, 16463)          # \part{The seven-eighths zero-free half-plane} .. end of the proof
OUT = []


def rec(group, cid, claim, ok, detail="", kind="gate"):
    """kind: gate (must hold), control (deliberately false; ok means a counterexample was exhibited),
    sens (informational sensitivity row; ok just records the observed truth value)."""
    OUT.append(dict(group=group, id=cid, claim=claim, ok=bool(ok), kind=kind,
                    detail=detail if isinstance(detail, (dict, list, str)) else str(detail)))
    tag = {"gate": "PASS " if ok else "FAIL ",
           "control": "CONTROL-OK " if ok else "CONTROL-FAILED ",
           "sens": "INFO "}[kind]
    print(f"{tag}[{cid}] {claim}" + (f" :: {detail}" if detail not in ("", None) else ""), flush=True)


def ident(group, cid, claim, lhs, rhs):
    d = sp.simplify(sp.together(sp.sympify(lhs) - sp.sympify(rhs)))
    rec(group, cid, claim, d == 0, "" if d == 0 else f"difference {d}")


def fr(x):
    x = sp.Rational(x)
    return F(int(x.p), int(x.q))


def vertex_max(expr, vs, box):
    """Exact max of an expression that is affine in each variable separately (multi-affine) over a box:
    attained at a vertex. Verifies multi-affinity first (degree <= 1 in each variable)."""
    P = sp.Poly(sp.expand(expr), *vs)
    if any(e > 1 for mon in P.monoms() for e in mon):
        raise ValueError("not multi-affine: " + str(expr))
    best = None
    for vert in product(*box):
        val = fr(expr.subs(dict(zip(vs, [sp.Rational(v.numerator, v.denominator) for v in vert]))))
        if best is None or val > best[0]:
            best = (val, vert)
    return best


# =================================================================================================
# T. Text
# =================================================================================================
def text_checks(path):
    G = "T text"
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    rec(G, "T0", "paper.tex SHA-256 matches the reviewed object", sha == EXPECTED_SHA, sha)
    L = raw.decode("utf-8").splitlines()
    anchors = [
        (387, r"so $1/2\le\beta_*\le1$.", "beta_* <= 1 by definition and Euler convergence (input of this route)"),
        (1593, r"If $b>1$", "Lemma 4.9 global clause covers b > 1 (contours at beta_*+e when beta_* = 1)"),
        (4054, r"x_r\ge51/100,\quad z_r\ge17/50,\quad w_r\ge-1/100", "Lemma 7.1 region one allows w_r >= -1/100"),
        (4285, r"a\in(51/100+e\mathbb Z_{\ge0})\cap[51/100,1]", "Lemma 8.1 bins cover a in [51/100, 1]"),
        (4338, "This reasoning allows a zero on the line one.", "Lemma 8.1 allows a zero on Re s = 1"),
        (4372, r"\delta=2a-1,\qquad 1/50\le\delta\le1.", "detector delta range is [1/50, 1]"),
        (4513, r"For every \(t\in[1,3/2]\),", "Prop 8.3 for every t in [1, 3/2]"),
        (4529, r"t-\tfrac12-O(\epsilon)\le r\le t+O(1/\log U),", "Prop 8.3 witness: r >= t - 1/2 - O(eps)"),
        (5857, r"Also $\Re w\ge-6e>-1/100$ and", "Lemma 10.3 contour Re w = 1-a-6e stays in region one for a <= 1"),
        (6300, r"This also covers $\beta_*=1$.", "Lemma 10.5 (principal signal) covers beta_* = 1"),
        (6812, r"Theorem~\ref{thm:eleven-twelfths} applies to every primitive character", "the bootstrap sentence"),
        (6817, r"\Delta:=\beta_*-\frac78,\qquad 0<\Delta\le\frac1{24},", "eq:part-II-bootstrap"),
        (6825, r"a\le\beta_*,\qquad \delta=2a-1\le\kappa\le\frac56.", "eq:part-II-bin-ceiling"),
        (8854, r"Let $51/100\le a\le1$, $0<e\le10^{-3}$, and take", "Prop 16.1 for 51/100 <= a <= 1"),
        (12532, r"Let \(3/4\le\kappa\le1\).", "Lemma 18.1 stated for kappa in [3/4, 1]"),
        (12565, r"If \(\kappa=1\), no zero-free", "Lemma 18.1 kappa = 1 clause"),
        (15023, r"uniform for \(51/100\le a\le1\)", "Lemma 19.1 uniform for 51/100 <= a <= 1"),
        (15104, r"Since \(\kappa<1\) and", "Sec 19.2 preamble uses kappa < 1"),
        (15275, r"e(r)=\max\left\{1,\frac{1+5r}{6}\right\}.", "no-slot amplified exponent e(r)"),
        (15282, r"\label{eq:no-slot-inverse-count}", "eq:no-slot-inverse-count"),
        (15448, r"\begin{remark}[Unselected inverse witnesses beyond the Part II bin ceiling]", "Remark 19.3"),
        (15458, r"a>51/100,\qquad 1/50<\delta=2a-1\le1,", "Remark 19.3: valid for delta <= 1"),
        (15928, r"At the live upper endpoint \(\delta=\alpha\), take \(t=3/2\) in", "endpoint argument at delta = alpha"),
        (15946, r"\label{eq:large-delta-endpoint}", "eq:large-delta-endpoint"),
        (16133, r"\ge\frac{33}{50}-\frac{\delta}{2}\ge\frac4{25}>0.", "frequency slope 4/25 (the delta <= 1 value)"),
        (16141, r"R_*+\Delta/4\le\frac{139}{96},", "139/96 (the Delta <= 1/8 value)"),
        (16165, r"the last inequality uses \(\delta\le5/6\).", "intermediate range uses delta <= 5/6"),
        (16168, r"already control every \(d\le h\).", "delta = alpha count used for all d <= h"),
        (16223, r"m_{\rm high}:=\min\{m_{\rm hi},m_{\rm small}\}>0.", "m_high is a min"),
        (16241, r"closure \(\kappa\in[3/4,5/6]\) used here", "Prop 20.3 mesh sentence"),
        (16269, r"The second inequality uses \(\delta\le5/6<1\).", "Prop 20.3 rounding sentence"),
        (16324, r"only on \(\Delta\) and the pretarget slot system.", "choices depend on Delta"),
    ]
    bad = [(ln, s) for ln, s, _ in anchors if s not in L[ln - 1]]
    rec(G, "T1", f"{len(anchors)} anchor strings found at the cited lines", not bad,
        {"missing": bad} if bad else {str(ln): note for ln, _, note in anchors})

    # census -----------------------------------------------------------------------------------
    pat = re.compile(r"11/12|\\frac\{?11\}?\{?12\}?|1/24|\\frac1\{24\}|\\frac\{1\}\{24\}|5/6|\\t?frac56|"
                     r"\\frac\{5\}\{6\}|\\kappa|\\alpha|\\Delta|\\beta_\*|\\beta_\{\*\}|"
                     r"part-II-bootstrap|part-II-bin-ceiling|eleven-twelfths")
    notation = [r"\\kappa_\{?(F|\\mathrm G|\\mathrm\{G\}|i|1|2|a|c|\\zeta|P)", r"\\(widehat|bar)\\kappa",
                r"\\kappa_\{\\zeta", r"\\bar\\alpha", r"\\alpha\(", r"\\alpha_", r"\\Omega_\{[^}]*\\alpha",
                r"\\Omega_\{\{\\rm init\},\\alpha\}", r"x_\\alpha", r"\\prod_\\alpha", r"_\\alpha\b",
                r"\\alpha\\in", r"\\Delta_", r"\\Delta[ ]?(M|A|z)\b", r"\(1-\\Delta\)", r"y\^\{-5/6\}",
                r"q_p\^\{-5/6\}", r"\(s-5/6\)", r"\\tfrac56", r"-\\frac56(M|\\delta)", r"H\^\{5/6\}",
                r"M=l_x\+l_y=\\frac56"]

    def strip(s):
        for n in notation:
            s = re.sub(n, "", s)
        return s

    hits = [i + 1 for i in range(PART2[0] - 1, PART2[1]) if pat.search(L[i])]
    subst = [ln for ln in hits if pat.search(strip(L[ln - 1]))]
    unclassified = [ln for ln in subst if not any(lo <= ln <= hi for _, lo, hi, _ in ITEMS)]
    overlap = [ln for ln in subst if sum(lo <= ln <= hi for _, lo, hi, _ in ITEMS) > 1]
    per_item = {iid: [ln for ln in subst if lo <= ln <= hi] for iid, lo, hi, _ in ITEMS}
    empty = [iid for iid, v in per_item.items() if not v and iid not in ITEMS_WITHOUT_HITS]
    cats = {}
    for iid, lo, hi, cat in ITEMS:
        cats[cat] = cats.get(cat, 0) + len(per_item[iid])
    rec(G, "T2", f"census: {len(hits)} Part II pattern lines, {len(hits) - len(subst)} notation-only "
        f"(other symbols), {len(subst)} substantive; every substantive line lies in exactly one item",
        not unclassified and not overlap and not empty,
        dict(unclassified=unclassified, overlap=overlap, items_without_hits=empty, lines_per_category=cats,
             per_item={k: v for k, v in per_item.items()}))
    # the only citation of Thm 3.1 in Part II
    cit = [i + 1 for i in range(PART2[0] - 1, PART2[1]) if "thm:eleven-twelfths" in L[i]]
    rec(G, "T3", "the only Part II citation of Thm 3.1 (thm:eleven-twelfths) is line 6812", cit == [6812], cit)
    # the remark is unlabeled and not cited: it becomes load-bearing only through this route
    rem = [i + 1 for i in range(len(L)) if "Unselected inverse witnesses" in L[i]]
    rec(G, "T4", "Remark 19.3 (15448) is the only occurrence of its title (unlabeled; no \\ref reaches it)",
        rem == [15448], rem)
    return L


# Enumeration items: (id, first line, last line, category). Categories:
#   R   replaced by beta_* <= 1 (the bootstrap sentence)
#   a   fine for Delta <= 1/8 as written (possibly after a literal restatement of a bound)
#   b   needs the extended high-bin count (PART1_FREE_ROUTE.md Sec. 2)
#   c   breaks if applied to bins delta > 5/6 as written; not needed once (b) is used
ITEMS = [
    ("U1", 6812, 6815, "R"), ("U2", 6816, 6819, "a"), ("U3", 6821, 6830, "b"), ("U4", 6842, 6842, "a"),
    ("U5", 8647, 8648, "a"), ("U6", 9110, 9139, "a"), ("U7", 12532, 12573, "a"), ("U8", 12581, 12584, "a"),
    ("U9", 12833, 12906, "a"), ("U10", 12932, 14906, "a"), ("U11", 15097, 15108, "b"),
    ("U12", 15175, 15180, "a"), ("U13", 15185, 15226, "a"), ("U14", 15289, 15311, "a"),
    ("U15", 15326, 15341, "a"), ("U16", 15398, 15420, "a"), ("U17", 15429, 15429, "a"),
    ("U18", 15447, 15466, "a"), ("U19", 15498, 15504, "a"), ("U20", 15614, 15692, "a"),
    ("U21", 15724, 15724, "a"), ("U22", 15763, 15763, "a"), ("U23", 15859, 15882, "a"),
    ("U24", 15926, 15946, "b"), ("U25", 15949, 15992, "a"), ("U26", 15995, 16072, "a"),
    ("U27", 16087, 16108, "a"), ("U28", 16128, 16144, "b"), ("U29", 16146, 16168, "c"),
    ("U30", 16174, 16185, "a"), ("U31", 16196, 16233, "b"), ("U32", 16241, 16241, "a"),
    ("U33", 16269, 16269, "a"), ("U34", 16324, 16324, "a"), ("U35", 16333, 16350, "b"),
    ("U36", 16370, 16446, "a"), ("U37", 16454, 16460, "a"),
]
ITEMS_WITHOUT_HITS = set()


# =================================================================================================
# A. Algebra
# =================================================================================================
de, q, d, r, Dl, lam, z, gam, m, x = sp.symbols("delta q d r Delta lambda zeta gamma m x", real=True)
R_ = sp.Rational
h, ell, lx, ly, z0, al, C0 = R_(13, 16), R_(1, 6), R_(17, 48), R_(23, 48), R_(17, 50), R_(5, 6), R_(-1, 48)
RR = sp.Symbol("R", real=True)
a_ = (1 + de) / 2
E1 = a_ - R_(7, 8) + h * (z0 - R_(1, 6)) - a_ * ly - (1 - a_) * ell - (de / 2 - q) * ell + d * (RR + de / 2 - z0)
E2 = C0 + R_(2, 3) * de + q / 6 - h * (1 - RR) + (d - h) * (RR + de / 2 - z0)
e_hi = (1 + 5 * r) / 6              # e(r) on r >= 1
BOUND = C0 - de / 16 - Dl           # claimed high margin relative to C(beta_*)


def algebra():
    G = "A algebra"
    ident(G, "A1", "eq:common-high-exponent (15726-15734): first line = second line, C_0 = -1/48 (identity in "
          "delta, q, R, d; no range used)", E1, E2)
    ident(G, "A2", "count, r >= 1: (1+5r)/6 - delta r - (1-delta) = (5/6 - delta)(r - 1)",
          e_hi - de * r - (1 - de), (al - de) * (r - 1))
    ident(G, "A3", "count, r < 1 (e(r) = 1): 1 - delta r - (1-delta) = delta (1 - r)", 1 - de * r - (1 - de), de * (1 - r))
    rec(G, "A4", "(1+5r)/6 <= 1 iff r <= 1, so e(r) = 1 on r <= 1 and (1+5r)/6 on r >= 1",
        sp.solve_univariate_inequality(e_hi <= 1, r, relational=False) == sp.Interval(-sp.oo, 1))
    # count bound on the whole witness range [1 - gamma, 3/2]: case split, each a product of signed factors
    # r >= 1: (5/6 - delta) <= 0 and (r - 1) >= 0; r in [1-gamma, 1): delta(1-r) <= delta*gamma <= gamma
    vm = vertex_max((al - de) * (r - 1), [de, r], [(F(5, 6), F(1)), (F(1), F(3, 2))])
    rec(G, "A5", "for 5/6 <= delta <= 1 and 1 <= r <= 3/2: (1+5r)/6 - delta r <= 1 - delta (max of the difference "
        "is 0, at delta = 5/6 or r = 1)", vm[0] == 0, dict(max=str(vm[0]), at=[str(v) for v in vm[1]]))
    rec(G, "A6", "Lean high_bin_count shape: for r in [1-gamma, 1), 1 - delta r <= 1 - delta + gamma "
        "(checked as max of delta(1-r) - gamma over r >= 1-gamma: substitute r = 1 - s gamma)",
        vertex_max(de * (sp.Symbol("s") * gam) - gam, [de, sp.Symbol("s"), gam],
                   [(F(5, 6), F(1)), (F(0), F(1)), (F(0), F(1, 10))])[0] <= 0)
    # the margin identity
    RRv = 1 - de + lam
    lhs = E2.subs(RR, RRv) - Dl
    rhs = BOUND + (q - de / 2) / 6 + R_(13, 16) * lam + (d - h) * (R_(33, 50) - de / 2 + lam)
    ident(G, "A7", "high margin identity with R = 1 - delta + lambda: E(d) - Delta = -1/48 - delta/16 - Delta "
          "+ (q - delta/2)/6 + (13/16) lambda + (d - h)(33/50 - delta/2 + lambda)", lhs, rhs)
    ident(G, "A8", "at d = h, q = delta/2, lambda = 0: E(h) - Delta = -1/48 - delta/16 - Delta (the claimed margin; "
          "paper (eq:large-delta-endpoint) minus Delta; Lean high_source_margin)",
          lhs.subs({d: h, q: de / 2, lam: 0}), BOUND)
    S = R_(33, 50) - de / 2
    rec(G, "A9", "frequency slope S(delta) = R + delta/2 - 17/50 at R = 1-delta: S(1) = 4/25 > 0, S(5/6) = 73/300 < 2; "
        "S is decreasing, so 4/25 <= S <= 73/300 on [5/6, 1]",
        S.subs(de, 1) == R_(4, 25) and S.subs(de, al) == R_(73, 300) and sp.diff(S, de) < 0)
    # sign proof of the margin over the whole range: each correction term has a sign
    #   (q - delta/2)/6 <= 0 since q <= delta/2;   (d - h) S <= 0 for d <= h;   (d - h) S <= zeta*73/300 for d <= h+zeta
    rec(G, "A10", "margin over the whole range: for 5/6 <= delta <= 1, 0 <= Delta <= 1/8, 0 <= q <= delta/2, "
        "1/100 <= d <= h: E(d) - Delta <= -1/48 - delta/16 - Delta, equality iff d = h and q = delta/2 "
        "(by A7: both correction terms are products of factors of fixed sign; checked at the vertices "
        "of (q/delta, delta, d))",
        vertex_max((sp.Symbol("u") * de - de / 2) / 6 + (d - h) * S, [sp.Symbol("u"), de, d],
                   [(F(0), F(1, 2)), (F(5, 6), F(1)), (F(1, 100), F(13, 16))])[0] == 0)
    rec(G, "A11", "extension h < d <= h + zeta: (d - h) S <= (73/300) zeta <= 2 zeta (Lean relative_extend uses 2 zeta)",
        vertex_max((sp.Symbol("w") * z) * S - R_(73, 300) * z, [sp.Symbol("w"), de, z],
                   [(F(0), F(1)), (F(5, 6), F(1)), (F(0), F(1, 48))])[0] <= 0 and R_(73, 300) < 2)
    corners = {f"delta={dv},Delta={Dv}": str(BOUND.subs({de: dv, Dl: Dv}))
               for dv in (al, 1) for Dv in (0, R_(1, 8))}
    rec(G, "A12", "claimed margin at the corners: -7/96 (5/6, 0), -19/96 (5/6, 1/8), -1/12 (1, 0), -5/24 (1, 1/8); "
        "maximum over the range is -7/96 < 0", corners == {"delta=5/6,Delta=0": "-7/96", "delta=5/6,Delta=1/8": "-19/96",
                                                           "delta=1,Delta=0": "-1/12", "delta=1,Delta=1/8": "-5/24"},
        corners)
    mhi = R_(51, 64) * Dl
    vm = vertex_max(BOUND + mhi + R_(7, 96), [de, Dl], [(F(5, 6), F(1)), (F(0), F(1, 8))])
    rec(G, "A13", "high-bin margin dominates the balanced one: -1/48 - delta/16 - Delta <= -(51/64)Delta - 7/96 "
        "(so every high bin keeps more than m_hi >= m_high)", vm[0] <= 0, str(vm[0]))
    # balanced side with Delta <= 1/8
    ident(G, "A14", "balanced: -49/440640 + h Delta/4 - Delta = -49/440640 - (51/64) Delta (any Delta)",
          -R_(49, 440640) + h * Dl / 4 - Dl, -R_(49, 440640) - R_(51, 64) * Dl)
    inc = 24 * q * (1 - 2 * m) * Dl / (R_(9, 2) * (R_(9, 2) + 12 * Dl))
    num = sp.expand(sp.cancel((Dl / 4 - inc) * 4 * R_(9, 2) * (R_(9, 2) + 12 * Dl) / Dl))
    ident(G, "A15a", "capacity comparison: (Delta/4 - increase) * 18(9/2+12 Delta)/Delta = 81/4 + 54 Delta - 96 q (1-2m)",
          num, R_(81, 4) + 54 * Dl - 96 * q * (1 - 2 * m))
    vm = vertex_max(-(R_(81, 4) + 54 * Dl - 96 * q * sp.Symbol("v")), [Dl, q, sp.Symbol("v")],
                    [(F(0), F(1, 8)), (F(0), F(1, 2)), (F(0), F(1, 3))])
    rec(G, "A15", "capacity comparison <= Delta/4 for every Delta in [0, 1/8] (q <= 1/2, 1 - 2m <= 1/3): "
        "the bracket is >= 17/4 > 0; it only grows with Delta", vm[0] == -R_(17, 4), str(vm[0]))
    rec(G, "A16", "139/96 = 17/12 + (1/8)/4 exactly (the paper's R_* + Delta/4 bound is the Delta <= 1/8 value; "
        "with Delta <= 1/24 it would be 137/96); 139/96 + 1/2 - 17/50 < 2",
        R_(17, 12) + R_(1, 8) / 4 == R_(139, 96) and R_(17, 12) + R_(1, 24) / 4 == R_(137, 96)
        and R_(139, 96) + R_(1, 2) - z0 < 2)
    Dstar = R_(63, 800) / R_(51, 64)
    rec(G, "A17", "m_high = min{51 Delta/64, 63/800} switches at Delta = 42/425, inside (1/24, 1/8]: for larger "
        "Delta, m_high = m_small (Prop 20.3 defines it as the min, so nothing changes)",
        Dstar == R_(42, 425) and R_(1, 24) < Dstar < R_(1, 8), str(Dstar))
    rec(G, "A18", "kappa = 3/4 + 2 Delta lies in [3/4, 1] iff Delta in [0, 1/8]; kappa = 1 iff Delta = 1/8 iff "
        "beta_* = 1 (then Lemma 18.1's kappa = 1 clause applies); delta <= kappa <= 1",
        sp.solve(R_(3, 4) + 2 * Dl - 1, Dl) == [R_(1, 8)] and R_(7, 8) + R_(1, 8) == 1)
    rec(G, "A19", "high bins (delta > 5/6) can occur only if kappa > 5/6, i.e. Delta > 1/24",
        sp.solve(R_(3, 4) + 2 * Dl - al, Dl) == [R_(1, 24)])
    ee = sp.Symbol("e", positive=True)
    rec(G, "A20", "Lemma 10.3 / Prop 16.1 contours for a <= 1, 0 < e < 1/1000: Re w = 1 - a - 6e >= -6e > -1/100, and "
        "Re s + Re w = 1 + 10e (region one with eps_0 = 10e)",
        (1 - 1 - 6 * R_(1, 1000)) > -R_(1, 100) and sp.simplify((1 + 16 * ee - 6 * ee) - (1 + 10 * ee)) == 0)
    xr = R_(7, 8) + sp.Symbol("D2", nonnegative=True)
    expo = [-xr, 4 - 5 * xr - 6 * z0]
    rec(G, "A21", "Lemma 16.2 small-row line x_r = beta_* + e: the local exponents -x_r and 4 - 5x_r - 6z_r decrease "
        "in beta_*, so beta_* >= 7/8 is the binding case and beta_* <= 1 is never used",
        all(sp.diff(ex, sp.Symbol("D2", nonnegative=True)) < 0 for ex in expo))
    sg = sp.Symbol("sigma")
    rec(G, "A22", "Prop 8.3 Gamma-integral exponent -3 + t(5/4 - sigma) <= -189/100 uses only sigma >= 51/100 "
        "(decreasing in sigma; at sigma = 1 it is -21/8)",
        (-3 + R_(3, 2) * (R_(5, 4) - R_(51, 100))) == -R_(189, 100) and (-3 + R_(3, 2) * (R_(5, 4) - 1)) == -R_(21, 8))


# =================================================================================================
# G. Exact grid sweep (sanity)
# =================================================================================================
def grid():
    G = "G grid"
    deltas = [F(5, 6) + F(k, 60) for k in range(11)]
    Deltas = [F(0), F(1, 96), F(1, 24), F(42, 425), F(1, 10), F(1, 8)]
    rs = [F(1) - F(1, 100), F(1) - F(1, 1000), F(1), F(9, 8), F(5, 4), F(3, 2)]
    ds = [F(1, 100), F(1, 4), F(1, 2), F(3, 4), F(13, 16), F(13, 16) + F(1, 96), F(13, 16) + F(1, 48)]
    lams = [F(0), F(1, 1000)]
    worst_count = None
    worst_margin = None
    n = 0
    for dv, rv in product(deltas, rs):
        eR = max(F(1), (1 + 5 * rv) / 6)
        excess = (eR - dv * rv) - (1 - dv) - dv * max(F(0), 1 - rv)
        n += 1
        if worst_count is None or excess > worst_count[0]:
            worst_count = (excess, dv, rv)
    for dv, Dv, qfrac, dd, lv in product(deltas, Deltas, [F(0), F(1, 4), F(1, 2)], ds, lams):
        qv = qfrac * dv
        Rv = 1 - dv + lv
        E = (C0f + F(2, 3) * dv + qv / 6 - F(13, 16) * (1 - Rv) + (dd - F(13, 16)) * (Rv + dv / 2 - F(17, 50)))
        allowance = F(13, 16) * lv + 2 * max(F(0), dd - F(13, 16))
        excess = (E - Dv) - (C0f - dv / 16 - Dv) - allowance
        n += 1
        if worst_margin is None or excess > worst_margin[0]:
            worst_margin = (excess, dv, Dv, qv, dd, lv)
    rec(G, "G1", "exact grid: e(r) - delta r <= 1 - delta + delta (1-r)_+ on 11 delta x 6 r points in "
        "[5/6,1] x [1 - 1/100, 3/2]", worst_count[0] <= 0, dict(max_excess=str(worst_count[0])))
    rec(G, "G2", "exact grid: E(d) - Delta <= -1/48 - delta/16 - Delta + (13/16)lambda + 2(d-h)_+ on "
        "11 delta x 6 Delta x 3 q x 7 d x 2 lambda points (corners delta = 5/6, 1 and Delta = 0, 1/8 included)",
        worst_margin[0] <= 0, dict(points=n, max_excess=str(worst_margin[0]),
                                   at=[str(v) for v in worst_margin[1:]]))


C0f = F(-1, 48)


# =================================================================================================
# F. Failing controls and S. sensitivity rows
# =================================================================================================
def controls():
    G = "F controls"

    def Eh(dv, Rv, qv):
        return C0f + F(2, 3) * dv + qv / 6 - F(13, 16) * (1 - Rv)

    v = (1 + 5 * F(3, 2)) / 6 - F(4, 5) * F(3, 2) - (1 - F(4, 5))
    rec(G, "FC1", "drop delta >= 5/6: at delta = 4/5, r = 3/2 the amplified count exceeds 1 - delta", v > 0, str(v),
        kind="control")
    v = [1 - dv * F(1, 2) - (1 - dv) for dv in (F(5, 6), F(1))]
    rec(G, "FC2", "drop the t = 3/2 witness (r >= 1 - O(eps)): at r = 1/2 the count is 1 - delta/2 > 1 - delta",
        all(x_ > 0 for x_ in v), [str(x_) for x_ in v], kind="control")
    v = Eh(F(5, 6), 1 - F(2, 3) * F(5, 6), F(5, 12))
    rec(G, "FC3", "use the t = 1 no-slot count R = 1 - 2 delta/3 in a high bin: E(h) = -1/48 + 5 delta/24 > 0 "
        "(11/72 at delta = 5/6)", v == F(11, 72) and v > 0, str(v), kind="control")
    E12 = lambda dv: (C0f + F(2, 3) * dv + dv / 12 - F(13, 16) * (1 - (F(76, 75) - F(2, 3) * dv))
                      + (F(1, 2) - F(13, 16)) * ((F(76, 75) - F(2, 3) * dv) + dv / 2 - F(17, 50)))
    ok = (E12(F(1)) == F(1, 25) and E12(F(5, 6)) == F(-49, 14400) and E12(F(5, 6) + F(1, 60)) > F(-49, 14400)
          and E12(F(529, 625)) == 0)
    rec(G, "FC4", "reuse the paper's intermediate count (16146-16165) in a high bin: E(1/2) = -529/2400 + 25 delta/96 "
        "is <= -49/14400 exactly iff delta <= 5/6, vanishes at delta = 529/625 and equals +1/25 at delta = 1",
        ok, dict(E_at_1=str(E12(F(1))), E_at_5_6=str(E12(F(5, 6)))), kind="control")
    v = F(17, 12) + F(1, 7) / 4 - F(139, 96)
    rec(G, "FC5", "139/96 chain beyond Delta = 1/8: at Delta = 1/7, 17/12 + Delta/4 > 139/96", v > 0, str(v),
        kind="control")
    v = F(51, 64) * F(1, 8) - F(63, 800)
    rec(G, "FC6", "the literal 'm_high = 51 Delta/64' (SEP30_DETECTOR_QUANTIFIERS 6.2) at Delta = 1/8: 51/512 > 63/800",
        v > 0, str(v), kind="control")
    v = -F(49, 440640) + F(13, 64) * F(1, 8)
    rec(G, "FC7", "drop the subtraction of Delta (16106-16108) in a balanced bin at Delta = 1/8: "
        "-49/440640 + h Delta/4 > 0", v > 0, str(v), kind="control")
    v = F(3, 4) + 2 * F(1, 8) - F(5, 6)
    rec(G, "FC8", "kappa <= 5/6 (16241, eq:part-II-bootstrap) at Delta = 1/8: kappa = 1 > 5/6", v > 0, str(v),
        kind="control")
    v = (1 - F(101, 100) - 6 * F(1, 1000)) + F(1, 100)
    rec(G, "FC9", "a beyond 1 (a = 101/100, e = 1/1000): Re w = 1 - a - 6e < -1/100 leaves region one",
        v < 0, str(v), kind="control")
    v = F(33, 50) - F(1, 2) - F(73, 300)
    rec(G, "FC10", "the slope bound 73/300 (exact min on delta <= 5/6, JUNCTION R3) fails at delta = 1; "
        "the paper's 4/25 is the delta <= 1 value", v < 0, str(v), kind="control")

    S = "S sensitivity"
    # S1: no amplification: raw moment exponent max{1, r} (eq:raw-moment) at t = 3/2
    Rraw = lambda dv: max((max(F(1), rv) - dv * rv) for rv in (F(1), F(5, 4), F(3, 2)))
    vals = {str(dv): str(Eh(dv, Rraw(dv), dv / 2)) for dv in (F(5, 6), F(9, 10), F(1))}
    ident(S, "S1a", "without amplification (raw moment, exponent max{1,r}) at t = 3/2: R = (3/2)(1-delta), "
          "E(h) = 37/96 - 15 delta/32", C0 + R_(3, 4) * de - h * (1 - R_(3, 2) * (1 - de)), R_(37, 96) - R_(15, 32) * de)
    rec(S, "S1", "control 'drop the amplification' does NOT fail on [5/6, 1]: E(h) <= -1/192 (zero at delta = 37/45 "
        "< 5/6); the margin shrinks from 7/96 to 1/192 at delta = 5/6", all(F(v_) < 0 for v_ in vals.values()),
        vals, kind="sens")
    rec(S, "S2", "control 'e(r) = 1' (an unproven, stronger moment) does NOT fail: it lowers the count to "
        "1 - delta r <= 1 - delta for r >= 1; uninformative", True, "", kind="sens")


# =================================================================================================
# J. Junction replay with the Delta box widened to (0, 1/8]
# =================================================================================================
def replay_junction(paper, workdir):
    G = "J junction replay"
    src = os.path.join(HERE, "sep30_junction_check.py")
    raw = open(src, "rb").read()
    text = raw.decode("utf-8")
    old, new = "(0, F(1, 24))", "(0, F(1, 8))"
    nsub = text.count(old)
    patched = text.replace(old, new)
    wd = tempfile.mkdtemp(prefix="p1free_junction_", dir=workdir)
    target = os.path.join(wd, "sep30_junction_check_delta8.py")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(patched)
    t0 = time.time()
    proc = subprocess.run([sys.executable, "-I", target, paper], capture_output=True, text=True, timeout=3000)
    secs = round(time.time() - t0, 1)
    js = json.load(open(os.path.join(wd, "sep30_junction_check_output.json")))
    gates = [c for c in js["checks"] if not c["control"] and c["group"] != "12 float reconnaissance"]
    ctrls = [c for c in js["checks"] if c["control"]]
    failed = sorted(c["id"] for c in gates if not c["ok"])
    ctrl_bad = sorted(c["id"] for c in ctrls if not c["ok"])
    summary = dict(original=os.path.relpath(src, HERE), original_sha256=hashlib.sha256(raw).hexdigest(),
                   substitution=f"{old} -> {new}", n_substitutions=nsub, seconds=secs,
                   exit_code=proc.returncode, n_gates=len(gates), n_gates_pass=len(gates) - len(failed),
                   failed_gates=failed, n_controls=len(ctrls), controls_not_firing=ctrl_bad,
                   failed_detail=[c for c in gates if not c["ok"]],
                   delta_dependent_gates={c["id"]: c["ok"] for c in gates
                                          if c["id"] in ("B2e", "P1", "P2", "P3", "P5", "K1", "C6", "E5", "E11")},
                   stdout_tail=proc.stdout.splitlines()[-3:])
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "part1_free_junction_replay.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    rec(G, "J1", f"junction gates replayed on Delta in (0, 1/8] ({nsub} box substitutions): every gate passes except "
        "P2 (kappa <= 5/6), and all failing controls still fire", failed == ["P2"] and not ctrl_bad and nsub >= 8,
        dict(failed=failed, controls_not_firing=ctrl_bad, n_gates=len(gates), seconds=secs))
    shutil.rmtree(wd, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper")
    ap.add_argument("--replay-junction", action="store_true")
    ap.add_argument("--workdir", default=None, help="parent directory for the temporary replay copy")
    args = ap.parse_args()
    text_checks(args.paper)
    algebra()
    grid()
    controls()
    if args.replay_junction:
        replay_junction(args.paper, args.workdir)
    gates = [o for o in OUT if o["kind"] == "gate"]
    ctr = [o for o in OUT if o["kind"] == "control"]
    summary = dict(object_sha256=EXPECTED_SHA, n_gates=len(gates), n_gates_pass=sum(o["ok"] for o in gates),
                   n_controls=len(ctr), n_controls_fire=sum(o["ok"] for o in ctr),
                   junction_replay=bool(args.replay_junction),
                   arithmetic="EXACT: sympy over Q; fractions.Fraction; multi-affine vertex maxima",
                   items=[dict(id=i, lines=f"{lo}-{hi}", category=c) for i, lo, hi, c in ITEMS],
                   checks=OUT)
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "part1_free_checks_output.json"), "w") as fh:
        json.dump(summary, fh, indent=1)
    print(f"\n{summary['n_gates_pass']}/{summary['n_gates']} gates pass; "
          f"{summary['n_controls_fire']}/{summary['n_controls']} failing controls fire")
    sys.exit(0 if summary["n_gates_pass"] == summary["n_gates"] and summary["n_controls_fire"] == summary["n_controls"]
             else 1)


if __name__ == "__main__":
    main()
