#!/usr/bin/env python3
"""Second review of PART1_FREE_ROUTE.md: independent exact checks and new failing controls.

Status: review instrument (exploration level). Not a verdict on any analytic lemma, not an
        integration record. RH is unsolved; nothing here bears on it.
Object: paper.tex, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6, Sep 30 build/paper.tex). Untrusted data.
Independence: the census regex, the notation exclusions (explicit line numbers fixed by reading)
        and every formula below are written from the TeX, not copied from part1_free_checks.py.
        Only NC1 imports part1_free_checks.py, because NC1 is a mutation test of its census gate T2.
Groups:
  C   own census of Part II (6806-16463): every hit of the bound-carrying symbols, minus lines read
      as other notation; compared line by line with the 153-line set in part1_free_checks_output.json.
  X   exact arithmetic (fractions.Fraction; identities by exact polynomial expansion in sympy):
      eq:common-high-exponent, the high-bin count on both sides of r = 1, the margin, delta = 1 with
      r = 1 - gamma, the intermediate-row display (16159-16165), the no-amplification value (S1).
  NC  new failing controls (each must produce an exact counterexample or a census failure);
      NI  informational mutation rows that show what census gate T2 does NOT detect.
Run:    python3 -I part1_free_review2_checks.py PAPER_TEX [--workdir DIR]
Exit 0 iff every X gate holds and every NC control fires.
"""
import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import sys
import tempfile
from fractions import Fraction as F
from itertools import product

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
SHA = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
P2 = (6806, 16463)
OUT = []


def rec(cid, claim, ok, detail="", kind="gate"):
    OUT.append(dict(id=cid, claim=claim, ok=bool(ok), kind=kind, detail=detail))
    tag = {"gate": "PASS " if ok else "FAIL ", "control": "CONTROL-OK " if ok else "CONTROL-FAILED ",
           "info": "INFO "}[kind]
    print(f"{tag}[{cid}] {claim}" + (f" :: {detail}" if detail not in ("", None) else ""), flush=True)


# ------------------------------------------------------------------------------------------------
# C. Own census
# ------------------------------------------------------------------------------------------------
PAT = re.compile(r"\\beta_\*|\\beta_\\ast|\\beta\^\*|\\Delta(?![_a-zA-Z])|\\kappa(?![_a-zA-Z])|"
                 r"(?<!\\bar)\\alpha(?![_a-zA-Z])|5/6|\\frac56|\\tfrac56|\\frac\{5\}\{6\}|1/24|\\frac1\{24\}|"
                 r"\\frac\{1\}\{24\}|11/12|\\frac\{11\}\{12\}|part-II-bootstrap|part-II-bin-ceiling|"
                 r"eleven-twelfths")
# lines read as other notation (fixed by reading the TeX; see PART1_FREE_ROUTE_REVIEW2.md Sec. 1).
# The regex already excludes subscripted symbols (kappa_P, alpha_j, Delta_H, ...) and the arithmetic
# function bar-alpha(n) (13 lines in Secs. 13-17).
OTHER = {
    6864: "geometry M = l_x + l_y = 5/6",
    7011: "weight q_p^{-5/6}", 7013: "weight y^{-5/6}", 7035: "weight y^{-5/6}",
    7379: "coefficient alpha(mu)", 8087: "coefficient alpha(cn^3)",
    10102: "Laplacian (1 - Delta)^{m_0}",
    10458: "cutoff index Omega_{1,alpha}", 10464: "product over alpha", 10534: "index y_alpha",
    11129: "cutoff index Omega_{2,alpha}", 11149: "product over alpha",
    11942: "cutoff index Omega_{init,alpha}", 11989: "product over alpha",
    12449: "Lemma 17.6: U^{1/6} H^{5/6}",
    14438: "Lemma 18.1 sixth-power threshold A - 5M/6", 14446: "Lemma 18.1 amplifier 5/6 g_2",
    14457: "Lemma 18.1 amplifier 5/6 m'", 14466: "Lemma 18.1 5/6 delta_fr", 14481: "Lemma 18.1 5/6 delta_fr",
    14492: "Lemma 18.1 5/6 delta_fr", 14493: "Lemma 18.1 5/6 delta_fr", 14499: "Lemma 18.1 5/6 delta_fr",
    14500: "Lemma 18.1 5/6 delta_fr", 14501: "Lemma 18.1 5/6 delta_fr", 14760: "Lemma 18.1 A - 5M/6",
    14824: "differences Delta M, Delta A, Delta z",
    15563: "weight q_p^{-5/6}", 15570: "weight y^{-5/6}", 15583: "weight y^{-5/6}", 15606: "weight q_p^{-5/6}",
    15658: "Gaussian (s - 5/6)^2", 16292: "weight y^{-5/6}",
}


def census(L):
    hits = [i + 1 for i in range(P2[0] - 1, P2[1]) if PAT.search(L[i])]
    subst = [n for n in hits if n not in OTHER]
    stale = sorted(n for n in OTHER if n not in hits)
    rec("C1", f"own census: {len(hits)} hit lines in Part II, {len(hits) - len(subst)} read as other notation, "
        f"{len(subst)} substantive", not stale, dict(stale_notation_entries=stale))
    theirs = None
    p = os.path.join(RESULTS, "part1_free_checks_output.json")
    if os.path.exists(p):
        js = json.load(open(p))
        t2 = [c for c in js["checks"] if c["id"] == "T2"][0]["detail"]["per_item"]
        theirs = sorted({n for v in t2.values() for n in v})
    if theirs is None:
        rec("C2", "comparison with part1_free_checks_output.json skipped (file absent)", True, kind="info")
        return subst
    only_mine = sorted(set(subst) - set(theirs))
    only_theirs = sorted(set(theirs) - set(subst))
    rec("C2", "own substantive set equals the 153-line set of the original census (line by line)",
        not only_mine and not only_theirs and len(theirs) == 153,
        dict(n_mine=len(subst), n_theirs=len(theirs), only_mine=only_mine, only_theirs=only_theirs))
    # the hypothesis-bearing occurrences that a high bin (delta > 5/6) would violate if read literally
    lit = {n: L[n - 1].strip()[:90] for n in subst
           if re.search(r"\\le\\frac56|\\le5/6|\\le\\frac1\{24\}|\\le\\alpha|<\\alpha|\\delta=\\alpha|"
                        r"\(3/4,5/6\]|\[3/4,5/6\]|kappa<1", L[n - 1])}
    rec("C3", f"{len(lit)} substantive lines carry a literal upper bound (<= 5/6, <= 1/24, <= alpha, = alpha, "
        "kappa < 1, [3/4,5/6]); each is listed in the review table", True, lit, kind="info")
    return subst


# ------------------------------------------------------------------------------------------------
# X. Exact arithmetic
# ------------------------------------------------------------------------------------------------
dl, qq, dd, RR, DD, la, rr = sp.symbols("delta q d R Delta lambda r")
Q = sp.Rational
h, ell, ly, z0 = Q(13, 16), Q(1, 6), Q(23, 48), Q(17, 50)


def E_first(delta, q, R, d):
    """First line of eq:common-high-exponent (15726-15730), with a = (1 + delta)/2."""
    a = (1 + delta) / 2
    return a - Q(7, 8) + h * (z0 - Q(1, 6)) - a * ly - (1 - a) * ell - (delta / 2 - q) * ell + d * (R + delta / 2 - z0)


def E_second(delta, q, R, d):
    """Second line (15731-15733)."""
    return Q(-1, 48) + Q(2, 3) * delta + q / 6 - h * (1 - R) + (d - h) * (R + delta / 2 - z0)


def Ef(delta, q, R, d):
    return F(-1, 48) + F(2, 3) * delta + q / 6 - F(13, 16) * (1 - R) + (d - F(13, 16)) * (R + delta / 2 - F(17, 50))


def exact():
    rec("X1", "eq:common-high-exponent: first line = second line as polynomials in (delta, q, R, d)",
        sp.expand(E_first(dl, qq, RR, dd) - E_second(dl, qq, RR, dd)) == 0)
    # high-bin count: e(r) - delta r = 1 - delta + delta (1-r)_+ + (5/6 - delta)(r-1)_+ on both branches
    left = sp.expand(1 - dl * rr - (1 - dl + dl * (1 - rr)))
    right = sp.expand((1 + 5 * rr) / 6 - dl * rr - (1 - dl + (Q(5, 6) - dl) * (rr - 1)))
    rec("X2", "count identity on both branches: e(r) - delta r = 1 - delta + delta(1-r)_+ + (5/6-delta)(r-1)_+",
        left == 0 and right == 0)
    # worst case over delta in [5/6,1], r in [1-gamma, 3/2+eta]: excess over 1 - delta is delta*gamma (r<1 side)
    worst = max(max(F(1), (1 + 5 * r) / 6) - de * r - (1 - de)
                for de in (F(5, 6), F(9, 10), F(1)) for r in (F(1) - F(76, 1000), F(1), F(3, 2), F(3, 2) + F(1, 100)))
    rec("X3", "delta in {5/6, 9/10, 1}, r in {1 - 76/1000, 1, 3/2, 3/2 + 1/100}: max excess of the amplified count over "
        "1 - delta is 76/1000, attained at delta = 1, r = 1 - 76/1000 (the r < 1 branch, excess delta*gamma)",
        worst == F(76, 1000), str(worst))
    # margin with R = 1 - delta + lambda, q = x delta
    xs = sp.Symbol("x")
    diff = sp.expand(E_second(dl, xs * dl, 1 - dl + la, dd) - DD
                     - (Q(-1, 48) - dl / 16 - DD + dd * la + (xs - Q(1, 2)) * dl / 6 + (dd - h) * (Q(33, 50) - dl / 2)))
    rec("X4", "E(d) - Delta = -1/48 - delta/16 - Delta + d lambda + (x - 1/2) delta/6 + (d - h)(33/50 - delta/2), "
        "R = 1 - delta + lambda, q = x delta", diff == 0)
    # sign: on [5/6,1] x [0,1/2] x [1/100, h]: (x-1/2)delta/6 <= 0 and (d-h)(33/50-delta/2) <= 0 (factor signs)
    mx = max((x - F(1, 2)) * de / 6 + (d - F(13, 16)) * (F(33, 50) - de / 2)
             for de, x, d in product((F(5, 6), F(1)), (F(0), F(1, 2)), (F(1, 100), F(13, 16))))
    rec("X5", "the two correction terms are <= 0 on delta in [5/6,1], x in [0,1/2], d in [1/100, 13/16] "
        "(multi-affine; vertex maximum)", mx == 0, str(mx))
    corners = {f"delta={de},Delta={D}": str(F(-1, 48) - de / 16 - D) for de in (F(5, 6), F(1)) for D in (F(0), F(1, 8))}
    rec("X6", "margin corners -7/96, -19/96, -1/12, -5/24; worst -7/96 at delta = 5/6, Delta = 0",
        sorted(corners.values()) == sorted(["-7/96", "-19/96", "-1/12", "-5/24"]), corners)
    # P1F.2 second bullet: (73/300 + lambda) zeta <= 2 zeta needs lambda <= 527/300
    rec("X7", "P1F.2 extension bound (73/300 + lambda) zeta <= 2 zeta holds iff lambda <= 527/300 "
        "(the note states lambda >= 0 only; harmless for small losses)", F(73, 300) + F(527, 300) == 2)
    # the paper's intermediate display (16146-16165), recomputed from the second line
    Ei = sp.expand(E_second(dl, dl / 2, Q(76, 75) - Q(2, 3) * dl, Q(1, 2)))
    rec("X8", "intermediate rows: E(1/2) with R = 76/75 - 2 delta/3, q = delta/2 equals -529/2400 + 25 delta/96 "
        "(paper 16159-16161); value -49/14400 at delta = 5/6; zero at 529/625; +1/25 at delta = 1",
        Ei == sp.expand(-Q(529, 2400) + Q(25, 96) * dl) and Ei.subs(dl, Q(5, 6)) == -Q(49, 14400)
        and sp.solve(Ei, dl) == [Q(529, 625)] and Ei.subs(dl, 1) == Q(1, 25), str(Ei))
    slope_i = Q(76, 75) - Q(2, 3) * dl + dl / 2 - z0
    rec("X9", "intermediate slope 101/150 - delta/6 > 0 on [0,1] (so E(d) <= E(1/2) for d <= 1/2, all delta <= 1)",
        sp.expand(slope_i - (Q(101, 150) - dl / 6)) == 0 and Q(101, 150) - Q(1, 6) > 0)
    # S1 (no amplification) recomputed: raw moment exponent max{1, r(1+c)}, c -> 0, r <= 3/2
    Eraw = sp.expand(E_second(dl, dl / 2, Q(3, 2) * (1 - dl), h))
    rec("X10", "no amplification at t = 3/2: E(h) = 37/96 - 15 delta/32, -1/192 at delta = 5/6, root 37/45",
        Eraw == sp.expand(Q(37, 96) - Q(15, 32) * dl) and Eraw.subs(dl, Q(5, 6)) == -Q(1, 192)
        and sp.solve(Eraw, dl) == [Q(37, 45)], str(Eraw))
    # capacity comparison at Delta = 1/8 with the sharper q <= 5/12 (balanced bins)
    inc = lambda q, v, D: 24 * q * v * D / (F(9, 2) * (F(9, 2) + 12 * D))
    worst = max(inc(q, v, D) / (D / 4) for q in (F(5, 12), F(1, 2)) for v in (F(1, 3),) for D in (F(1, 1000), F(1, 8)))
    rec("X11", "capacity comparison 24q(1-2m)Delta/((9/2)(9/2+12Delta)) <= Delta/4 for q <= 1/2, 1-2m <= 1/3, "
        "Delta in (0,1/8] (ratio to Delta/4 at most 1, decreasing in Delta)", worst <= 1, str(worst))


# ------------------------------------------------------------------------------------------------
# NC. New failing controls
# ------------------------------------------------------------------------------------------------
def unamplified_balanced(de, x, D):
    """Balanced bin with the raw (unamplified) long count L_raw(t) = 1 - delta + (1 - delta)(t - 1):
    re-balance against R_short and evaluate E(h) - Delta with the paper's + h Delta/4 allowance."""
    Dx = 3 - F(17, 9) * x
    Px = (2 - F(8, 9) * x) * (1 - x)
    tm1 = de * Px / (2 * (de * Px + (1 - de) * Dx))
    Rraw = 1 - de + (1 - de) * tm1
    return Ef(de, x * de, Rraw + D / 4, F(13, 16)) - D


def amplified_balanced(de, x, D):
    Dx = 3 - F(17, 9) * x
    Px = (2 - F(8, 9) * x) * (1 - x)
    J = (F(5, 6) - de) * Dx + de * Px
    tm1 = de * Px / (2 * J)
    Rs = 1 - de + (F(5, 6) - de) * tm1
    return Ef(de, x * de, Rs + D / 4, F(13, 16)) - D


def controls(paper, workdir):
    # NC1: census mutation (T2 of part1_free_checks.py must fail on a planted bound outside every item)
    sys.dont_write_bytecode = True
    sys.path.insert(0, HERE)
    import part1_free_checks as orig  # noqa: E402  (mutation test of its census gate)
    L = open(paper, encoding="utf-8").read().splitlines()
    wd = tempfile.mkdtemp(prefix="p1f_review2_", dir=workdir)

    def t2_on(lines):
        p = os.path.join(wd, "mut.tex")
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        orig.OUT.clear()
        with contextlib.redirect_stdout(io.StringIO()):
            orig.text_checks(p)
        return [o for o in orig.OUT if o["id"] == "T2"][0]

    def plant(ln, s):
        M = list(L)
        M[ln - 1] = M[ln - 1] + " " + s
        return M

    base = t2_on(L)
    m1 = t2_on(plant(10000, r"\(\delta\le\frac56\)"))
    rec("NC1", "census mutation: plant '\\delta\\le\\frac56' on line 10000 (outside every item); T2 must fail",
        base["ok"] and not m1["ok"], dict(T2_unmutated=base["ok"], T2_mutated=m1["ok"],
                                          unclassified=m1["detail"]["unclassified"]), kind="control")
    m2 = t2_on(plant(10000, r"\(\delta\le\tfrac56\)"))
    rec("NI1", "census blind spot: the same bound spelled '\\tfrac56' is stripped as notation, so T2 still passes",
        m2["ok"], dict(T2_mutated=m2["ok"]), kind="info")
    m3 = t2_on(plant(13500, r"\(0<\Delta\le\frac1{24}\)"))
    rec("NI2", "census range absorption: '\\Delta\\le\\frac1{24}' planted on line 13500 (inside item U10 = "
        "12932-14906) is absorbed by the item range, so T2 still passes",
        m3["ok"], dict(T2_mutated=m3["ok"], U10_lines=m3["detail"]["per_item"]["U10"][-3:]), kind="info")
    shutil.rmtree(wd, ignore_errors=True)

    # NC2: amplification is load-bearing in the balanced range (S1 must not be read as 'Lemma 17.6 is removable')
    best = None
    for k in range(2, 83):
        de = F(k, 100)
        for x in (F(0), F(1, 4), F(1, 2)):
            v = unamplified_balanced(de, x, F(0))
            if best is None or v > best[0]:
                best = (v, de, x)
    v1000 = unamplified_balanced(best[1], best[2], F(1, 1000))
    amp = amplified_balanced(best[1], best[2], F(0))
    rec("NC2", "drop the amplification in a BALANCED bin (raw long count, slope 1 - delta instead of 5/6 - delta), "
        "re-balance t: E(h) - Delta > 0 at Delta = 0 and at Delta = 1/1000 (the amplified count gives < 0 there)",
        best[0] > 0 and v1000 > 0 and amp < 0,
        dict(delta=str(best[1]), x=str(best[2]), E_raw_Delta0=str(best[0]), E_raw_Delta1e3=str(v1000),
             E_amplified_Delta0=str(amp), approx=float(best[0])), kind="control")
    # the threshold in Delta below which the unamplified balanced count fails at this point
    Dcrit = best[0] / (1 - F(13, 64))
    rec("NI3", "at that point the unamplified balanced margin is restored only for Delta > E_raw/(51/64); "
        "no uniform Delta -> 0 statement survives", True, dict(Delta_crit=str(Dcrit), approx=float(Dcrit)), kind="info")

    # NC3: fixed (non-shrinking) witness deficit: r >= 1 - gamma with gamma = 1/8 breaks the high-bin margin
    vals = {}
    for de in (F(5, 6), F(1)):
        Rv = 1 - de + de * F(1, 8)              # the r < 1 branch at r = 1 - 1/8
        vals[str(de)] = Ef(de, de / 2, Rv, F(13, 16))
    crit = {str(de): str((F(1, 48) + de / 16) / (F(13, 16) * de)) for de in (F(5, 6), F(1))}
    rec("NC3", "replace the saturated witness r >= 1 - O(eps) by a fixed deficit gamma = 1/8: E(h) > 0 at "
        "delta = 5/6 and delta = 1 (Delta = 0); the tolerated deficit is gamma < 7/65 (5/6) and 4/39 (1)",
        all(v > 0 for v in vals.values()) and crit == {"5/6": "7/65", "1": "4/39"},
        dict(E_h={k: str(v) for k, v in vals.items()}, gamma_crit=crit), kind="control")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paper")
    ap.add_argument("--workdir", default=None)
    args = ap.parse_args()
    raw = open(args.paper, "rb").read()
    rec("X0", "paper.tex SHA-256 matches", hashlib.sha256(raw).hexdigest() == SHA, hashlib.sha256(raw).hexdigest())
    L = raw.decode("utf-8").splitlines()
    census(L)
    exact()
    controls(args.paper, args.workdir)
    gates = [o for o in OUT if o["kind"] == "gate"]
    ctr = [o for o in OUT if o["kind"] == "control"]
    summ = dict(object_sha256=SHA, n_gates=len(gates), n_gates_pass=sum(o["ok"] for o in gates),
                n_controls=len(ctr), n_controls_fire=sum(o["ok"] for o in ctr), checks=OUT)
    os.makedirs(RESULTS, exist_ok=True)
    with open(os.path.join(RESULTS, "part1_free_review2_output.json"), "w") as fh:
        json.dump(summ, fh, indent=1, default=str)
    print(f"\n{summ['n_gates_pass']}/{summ['n_gates']} gates pass; {summ['n_controls_fire']}/{summ['n_controls']} "
          "new failing controls fire")
    sys.exit(0 if summ["n_gates_pass"] == summ["n_gates"] and summ["n_controls_fire"] == summ["n_controls"] else 1)


if __name__ == "__main__":
    main()
