#!/usr/bin/env python3
"""Exact-rational check of the row-count junction of the 30 Sep 2026 OpenAI 7/8 manuscript.

Status: review instrument (exploration level). Not a verdict on any analytic lemma.
Object: paper.tex, SHA-256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
        (pr908: standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex). External, unreviewed.
Scope:  Lemma 19.1 (15015-15062), the selection prose (15095-15184), Prop 19.2 (15185-15446) and
        the endpoint prose (15920-15993, 16073-16111). For every invocation of Lemma 17.1
        (lem:marked), Lemma 17.6 (lem:inverse-amplification), Lemma 18.1 (lem:plain),
        Prop 8.3 (prop:detector-witness) and Lemma 19.1 (lem:bin-prime-bound), the QUANTITATIVE
        hypotheses (length inequalities, capacities, ranges, supply, kappa range) are checked
        over the whole parameter box, together with the Delta/4 capacity comparison
        (eq:capacity-comparison, 15392-15405), the case cover of Prop 19.2 and the endpoint
        algebra. Qualitative hypotheses (coefficient classes, Theta-membership, smooth seminorms,
        rowwise heights, Sobolev arguments) are NOT checked here; they are listed in the report.
Arithmetic: every gate is exact. Identities: sympy over Q. Inequalities: fractions.Fraction
        branch-and-bound (natural interval extension, mean-value form, exact monotonicity
        reduction to faces, bisection). No floating point enters any gate. One float
        cross-check against scripts/threshold_calculus.py is labelled FLOATING_RECONNAISSANCE.
Run:    nice -n 10 python3 -I sep30_junction_check.py [paper.tex]
        (writes sep30_junction_check_output.json next to this file; exit 0 iff no gate fails
        and every failing control fails as designed)
"""
from fractions import Fraction as F
import hashlib
import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
EXPECTED_SHA = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
OUT = []


def rec(group, cid, lines, claim, ok, detail="", control=False):
    """control=True: a deliberately false statement; it passes iff a violation is exhibited."""
    OUT.append(dict(group=group, id=cid, lines=lines, claim=claim, ok=bool(ok), control=control,
                    detail=detail if isinstance(detail, (dict, list)) else str(detail)))
    tag = ("CONTROL-OK " if ok else "CONTROL-FAILED ") if control else ("PASS " if ok else "FAIL ")
    print(f"{tag}[{cid}] {claim}" + (f" :: {detail}" if detail != "" else ""), flush=True)


# =============================================================================================
# Exact polynomial branch-and-bound
# =============================================================================================
def to_pd(expr, vs):
    """exact polynomial coefficient dict; the expression must reduce to a polynomial in vs
    (any denominator must be a nonzero rational constant)."""
    num, den = sp.fraction(sp.cancel(sp.together(sp.sympify(expr))))
    if sp.Poly(den, *vs).total_degree() > 0 or den.free_symbols:
        raise ValueError(f"not a polynomial in {vs}: denominator {den}")
    den = sp.Rational(den)
    P = sp.Poly(sp.expand(num), *vs)
    out = {}
    for mon, c in P.terms():
        c = sp.Rational(c) / den
        out[mon] = F(int(c.p), int(c.q))
    return out


def ev(pd, pt):
    s = F(0)
    for mon, c in pd.items():
        term = c
        for xi, e in zip(pt, mon):
            if e:
                term *= xi ** e
        s += term
    return s


def ival(pd, box):
    """natural interval extension on a box with nonnegative coordinates"""
    lo = hi = F(0)
    for mon, c in pd.items():
        mlo = mhi = F(1)
        for (a, b), e in zip(box, mon):
            if e:
                mlo *= a ** e
                mhi *= b ** e
        if c >= 0:
            lo += c * mlo
            hi += c * mhi
        else:
            lo += c * mhi
            hi += c * mlo
    return lo, hi


def deriv(pd, k):
    out = {}
    for mon, c in pd.items():
        e = mon[k]
        if e:
            m2 = list(mon)
            m2[k] -= 1
            m2 = tuple(m2)
            out[m2] = out.get(m2, F(0)) + c * e
    return out


def certify_ge(expr, vs, box, c=F(0), budget=300000, seconds=240):
    """Decide  expr >= c  on the box exactly.  Returns dict(ok, boxes, witness?, value?).
    ok=True is a proof (every leaf box has an exact lower bound >= c, or was reduced by an exact
    monotonicity argument to a face, ending in exact point evaluations).  ok=False with a witness
    is an exact counterexample point.  ok=False without witness = budget exhausted (undecided)."""
    box = [(F(a), F(b)) for a, b in box]
    for a, b in box:
        if a < 0 or b < a:
            raise ValueError("box must be nonnegative and ordered")
    pd = to_pd(expr - sp.Rational(c.numerator, c.denominator), vs)
    nv = len(vs)
    grads = [deriv(pd, k) for k in range(nv)]
    W = [b - a for a, b in box]
    stack, n, t_start = [tuple(box)], 0, time.time()
    while stack:
        bx = stack.pop()
        n += 1
        if n > budget or (n % 2000 == 0 and time.time() - t_start > seconds):
            return dict(ok=False, boxes=n, undecided=True)
        if ival(pd, bx)[0] >= 0:
            continue
        cen = tuple((a + b) / 2 for a, b in bx)
        fc = ev(pd, cen)
        if fc < 0:
            return dict(ok=False, boxes=n, witness=[str(v) for v in cen], value=str(fc + c),
                        excess=str(fc), excess_float=float(fc))
        gi = [ival(g, bx) for g in grads]
        mv = fc - sum(max(abs(g[0]), abs(g[1])) * (b - a) / 2 for g, (a, b) in zip(gi, bx))
        if mv >= 0:
            continue
        nb, changed = list(bx), False
        for k, ((a, b), g) in enumerate(zip(bx, gi)):
            if a < b:
                if g[0] >= 0:
                    nb[k], changed = (a, a), True
                elif g[1] <= 0:
                    nb[k], changed = (b, b), True
        if changed:
            stack.append(tuple(nb))
            continue
        rel = [((b - a) / W[k]) if W[k] else F(0) for k, (a, b) in enumerate(bx)]
        k = max(range(nv), key=lambda i: rel[i])
        if rel[k] == 0:      # a point with value < 0 would have been caught as fc < 0
            continue
        a, b = bx[k]
        m = (a + b) / 2
        l1, l2 = list(bx), list(bx)
        l1[k], l2[k] = (a, m), (m, b)
        stack += [tuple(l1), tuple(l2)]
    return dict(ok=True, boxes=n)


def certify_auto(expr, vs, box, c=F(0), **kw):
    """For c == 0, first factor the numerator over Q and certify the sign of each odd-multiplicity
    factor separately (exact; this avoids the dependency problem of interval arithmetic on faces where
    a factor vanishes identically).  Falls back to the plain branch-and-bound otherwise."""
    if c == 0:
        num, den = sp.fraction(sp.cancel(sp.together(sp.sympify(expr))))
        if not den.free_symbols:
            const, facs = sp.factor_list(sp.expand(num), *vs)
            if facs and (len(facs) > 1 or facs[0][1] > 1):
                sign, nb, okf = (1 if const / den > 0 else -1), 0, True
                for f, e in facs:
                    if e % 2 == 0:
                        continue
                    rp = certify_ge(f, vs, box, F(0), **kw)
                    nb += rp["boxes"]
                    if rp["ok"]:
                        continue
                    rn = certify_ge(-f, vs, box, F(0), **kw)
                    nb += rn["boxes"]
                    if rn["ok"]:
                        sign = -sign
                        continue
                    okf = False
                    break
                if okf and sign > 0:
                    return dict(ok=True, boxes=nb, method="factored: " + " * ".join(
                        f"({sp.sstr(f)})^{e}" for f, e in facs) + f" * {sp.sstr(const / den)}")
    r = certify_ge(expr, vs, box, c, **kw)
    r["method"] = "direct"
    return r


def gate(group, cid, lines, claim, expr, vs, box, c=F(0), **kw):
    t0 = time.time()
    r = certify_auto(expr, vs, box, c, **kw)
    det = dict(boxes=r["boxes"], seconds=round(time.time() - t0, 2), method=r.get("method", ""))
    if not r["ok"]:
        det.update({k: r[k] for k in r if k not in ("ok", "boxes", "method")})
    rec(group, cid, lines, claim, r["ok"], det)
    return r


def control(group, cid, lines, claim, expr, vs, box, c=F(0), **kw):
    """A deliberately false inequality: the control passes iff an exact counterexample is found."""
    r = certify_ge(expr, vs, box, c, **kw)
    found = (not r["ok"]) and ("witness" in r)
    if found:   # re-verify the witness exactly
        pt = [sp.Rational(w) for w in r["witness"]]
        val = sp.nsimplify(expr.subs(dict(zip(vs, pt))) - sp.Rational(c.numerator, c.denominator))
        found = bool(val < 0)
    rec(group, cid, lines, claim, found,
        {k: r[k] for k in r if k in ("witness", "value", "excess", "excess_float", "boxes", "undecided")},
        control=True)
    return r


def ident(group, cid, lines, claim, lhs, rhs):
    lhs, rhs = sp.Matrix([lhs]) if not isinstance(lhs, sp.MatrixBase) else lhs, \
        sp.Matrix([rhs]) if not isinstance(rhs, sp.MatrixBase) else rhs
    diffs = [sp.simplify(sp.together(a - b)) for a, b in zip(lhs, rhs)]
    ok = len(lhs) == len(rhs) and all(dd == 0 for dd in diffs)
    rec(group, cid, lines, claim, ok, "" if ok else f"differences {diffs}")


# =============================================================================================
# 0. Source binding
# =============================================================================================
src = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("SEP30_TEX")
if src and os.path.isfile(src):
    with open(src, "rb") as fh:
        raw = fh.read()
    sha = hashlib.sha256(raw).hexdigest()
    lines = raw.decode("utf-8").splitlines()
    rec("0 source", "S0", "-", "paper.tex SHA-256 matches the reviewed object", sha == EXPECTED_SHA, sha)
    anchors = {4510: "prop:detector-witness", 9250: "lem:marked", 9296: "lem:canonical-moment",
               12362: "lem:inverse-amplification", 12531: "lem:plain", 12562: "old-eq:3.9",
               15015: "lem:bin-prime-bound", 15177: "eq:plain-zero-loss-capacity",
               15185: "prop:detector-counts", 15282: "eq:no-slot-inverse-count", 15335: "eq:selected-counts",
               15402: "eq:capacity-comparison", 15415: "eq:short-crossing-count",
               15946: "eq:large-delta-endpoint", 15966: "eq:target-cutoff",
               15994: "lem:balanced-endpoint", 16104: "eq:adaptive-endpoint"}
    okA = all("\\label{" + lab + "}" in lines[ln - 1] for ln, lab in anchors.items())
    rec("0 source", "S1", "anchors", "label anchors found at the cited line numbers", okA, anchors)
else:
    rec("0 source", "S0", "-", "paper.tex not supplied: line anchors not re-checked (pass the path to bind)",
        True, "skipped")

# =============================================================================================
# 1. Symbols, geometry and the manuscript's formulas (transcribed, then checked)
# =============================================================================================
de, x, t, Dl, s, mu, v, nu, d, r, m, q, y = sp.symbols("delta x t Delta s mu v nu0 d r m q y",
                                                         nonnegative=True)
R = sp.Rational
al = R(5, 6)                       # alpha (15102)
h, ell, lx, ly, z0 = R(13, 16), R(1, 6), R(17, 48), R(23, 48), R(17, 50)   # (15513-15514), Re z
C0 = R(-1, 48)
kap = R(3, 4) + 2 * Dl             # kappa = 2 beta_* - 1 (15100, 6816)
betastar = R(7, 8) + Dl
Dx = 3 - R(17, 9) * x              # (15195)
Px = (2 - R(8, 9) * x) * (1 - x)
Nt = (2 - R(8, 9) * x) * t - R(5, 9) * x       # r_*(t) = Nt / Dx (15350)
rstar = Nt / Dx
Rshort = 1 - de + de * Px / Dx * (R(3, 2) - t)  # (15207)
Lt = 1 - de + (al - de) * (t - 1)              # (15208), (15303)
AI = lambda rr: 1 - de * (x + (1 - x) * rr)                                   # (15337)
St = lambda rr: 1 - de * (R(4, 9) * x + (2 - R(8, 9) * x) * (t - rr))        # (15338)
zM = lambda rr: (1 - rr) / 2                                                  # (15181)
zP = lambda mm: (1 - 2 * mm) / (6 * kap)                                      # (15174-15177)
zP0 = lambda mm: 2 * (1 - 2 * mm) / 9                                         # Delta = 0 (15330)
qq = x * de
C_inv = lambda rr, zz: 1 - de * rr - 2 * qq * zz              # Lemma 17.1 count (15234)
C_pl = lambda mm, zz: 1 - 2 * de * mm - 2 * qq * zz           # Lemma 18.1 count (15237)
J = (al - de) * Dx + de * Px                                  # (15965)
tcut = 1 + de * Px / (2 * J)
Rstar_end = Lt.subs(t, tcut)

BOXdx = [(0, F(5, 6)), (0, F(1, 2))]               # (delta, x), Lemma 20.2 box
BOXtx = [(1, F(3, 2)), (0, F(1, 2))]               # (t, x), Prop 19.2 "every t in [1,3/2]"

# =============================================================================================
# 2. Identities (sympy, exact)
# =============================================================================================
G = "1 identities"
ident(G, "I1", "15174-15177", "z_P(m) = (1-2m)/(6 kappa) = (1-2m)/(9/2+12 Delta)", zP(m), (1 - 2 * m) / (R(9, 2) + 12 * Dl))
ident(G, "I2", "15178-15179, 12571", "Lemma 18.1 instance n1=n2=m, M=1 (row width 1, q=0): n1+n2+6 kappa z_P(m) = M exactly",
      2 * m + 6 * kap * zP(m), 1)
ident(G, "I3", "15106, 12573", "Lemma 18.1 zero-free hypothesis beta_* <= (1+kappa)/2 holds with equality", (1 + kap) / 2, betastar)
ident(G, "I4", "15337", "inverse count at full capacity z_M(r) equals A_I(r)", C_inv(r, zM(r)), AI(r))
ident(G, "I5", "15338", "baseline plain count at z = 2(1-2m)/9, m = t-r, equals S_t(r)", C_pl(t - r, zP0(t - r)), St(r))
ident(G, "I6", "15350", "A_I(r_*) = S_t(r_*) (r_* is the crossing)", AI(rstar), St(rstar))
ident(G, "I7", "15352-15359", "r_*(3/2) = 1 and t - r_*(t) = ((1-x)t + 5x/9)/D_x",
      sp.Matrix([rstar.subs(t, R(3, 2)), t - rstar]), sp.Matrix([1, ((1 - x) * t + R(5, 9) * x) / Dx]))
ident(G, "I8", "15408-15415", "R_short(t) = [(2-8x/9) A_I(r) + (1-x) S_t(r)]/D_x for every r (r cancels)",
      ((2 - R(8, 9) * x) * AI(r) + (1 - x) * St(r)) / Dx, Rshort)
ident(G, "I9", "15392-15397", "capacity comparison: 2q(1-2m)(2/9 - 1/(9/2+12D)) = 24q(1-2m)D/((9/2)(9/2+12D)) "
      "= C_pl(m, z_P(m)) - C_pl(m, z_P0(m))",
      sp.Matrix([2 * qq * (1 - 2 * m) * (R(2, 9) - 1 / (R(9, 2) + 12 * Dl)), C_pl(m, zP(m)) - C_pl(m, zP0(m))]),
      sp.Matrix([24 * qq * (1 - 2 * m) * Dl / (R(9, 2) * (R(9, 2) + 12 * Dl))] * 2))
ident(G, "I10", "15373-15377", "Lemma 17.1 instance: with z = z_M(r) - nu0, 1-r-2z = 2 nu0 and 3-2r-8z = 4(1-r-2z)+(2r-1)",
      sp.Matrix([1 - r - 2 * (zM(r) - nu), 3 - 2 * r - 8 * (zM(r) - nu)]),
      sp.Matrix([2 * nu, 4 * (1 - r - 2 * (zM(r) - nu)) + (2 * r - 1)]))
ident(G, "I11", "15969-15972", "D_x - P_x = 1 + x - 8x^2/9", Dx - Px, 1 + x - R(8, 9) * x ** 2)
ident(G, "I12", "15976-15982", "D_x (R_short(t) - L(t)) at the cutoff t = 1 + delta P_x/(2J) vanishes",
      Dx * (Rshort - Lt).subs(t, tcut), 0)
ident(G, "I13", "15986-15989", "at delta = alpha: J = alpha P_x, t = 3/2, R_* = 1 - delta",
      sp.Matrix([J.subs(de, al), tcut.subs(de, al), Rstar_end.subs(de, al)]), sp.Matrix([al * Px, R(3, 2), 1 - al]))
ident(G, "I14", "16020-16021, PR910", "R_* = 1 - delta + (alpha-delta) delta P_x/(2J)",
      Rstar_end, 1 - de + (al - de) * de * Px / (2 * J))
a_ = (1 + de) / 2
Ed1 = a_ - R(7, 8) + h * (z0 - R(1, 6)) - a_ * ly - (1 - a_) * ell - (de / 2 - qq) * ell + d * (sp.Symbol("RR") + de / 2 - z0)
Ed2 = C0 + R(2, 3) * de + qq / 6 - h * (1 - sp.Symbol("RR")) + (d - h) * (sp.Symbol("RR") + de / 2 - z0)
ident(G, "I15", "15726-15734", "the two lines of eq:common-high-exponent agree at the Part II geometry (C_0 = -1/48)", Ed1, Ed2)
RR = sp.Symbol("RR")
Eh = Ed2.subs(d, h)
ident(G, "I16", "15942-15946", "delta = alpha endpoint: E(h) at R = 1-delta, q = delta/2 equals -1/48 - delta/16",
      Eh.subs({RR: 1 - de, x: R(1, 2)}), C0 + (R(3, 4) - h) * de)
ident(G, "I17", "16089-16091", "coefficient of R in E(d) is d: E(h)|_{R+Delta/4} - E(h)|_R = h Delta/4",
      Eh.subs(RR, RR + Dl / 4) - Eh, h * Dl / 4)
ident(G, "I18", "16094-16101", "-49/440640 + h Delta/4 - Delta = -49/440640 - (51/64) Delta",
      -R(49, 440640) + h * Dl / 4 - Dl, -R(49, 440640) - R(51, 64) * Dl)
Estar = Eh.subs(RR, Rstar_end)
ident(G, "I19", "16019-16023", "-E_* = (1+(3+8y)delta)/48 - (13/32)(5/6-delta) delta P_x/J with y = 1/2 - x",
      -Estar, (1 + (3 + 8 * (R(1, 2) - x)) * de) / 48 - R(13, 32) * (al - de) * de * Px / J)
ident(G, "I20", "15434-15444", "no-slot t=1 count: R_short(1) at x=0 is 1 - 2delta/3 and L(1) = 1 - delta",
      sp.Matrix([Rshort.subs({t: 1, x: 0}), Lt.subs(t, 1)]), sp.Matrix([1 - R(2, 3) * de, 1 - de]))
# Lemma 17.6 loss bookkeeping (15269-15281), symbolic in eps_m, R0 >= 1 and R0 <= 1 separately
em, R0, cc, rr_ = sp.symbols("eps_m R0 c rr", positive=True)
c_choice = lambda Rm: 3 * em / (10 * Rm)
ok76 = sp.simplify(5 * c_choice(R0) * R0 / 6 + (1 + R0) * em / (4 * (1 + R0)) - em / 2) == 0
ok76b = sp.simplify(5 * c_choice(1) * R0 / 6 - em * R0 / 4) == 0
rec(G, "I21", "15269-15281", "Lemma 17.6 losses: 5cR0/6 + (1+R0)eps0 = eps_m/2 if R0>=1 (and <= eps_m/2 if R0<1)",
    ok76 and ok76b)
# Lemma 17.1 -> Lemma 17.2 initial margins (12205-12287) at the junction's c1 = 2 nu0, c2 = 9/37
cb = sp.Symbol("cbar", positive=True)
okm = (sp.simplify((cb - 9 * cb / 100 - cb / 100) - R(9, 10) * cb) == 0
       and sp.simplify((cb - 22 * cb / 100 - 3 * cb / 100) - R(3, 4) * cb) == 0)
rec(G, "I22", "12216-12287", "17.1 init: with eta, tau_init <= cbar/100 both canonical margins >= 3cbar/4 > c_* = cbar/2; "
    "at the junction cbar = min(2 nu0, 9/37) = 2 nu0 for nu0 < 9/74, so c_* = nu0", okm)

# =============================================================================================
# 3. Exact inequalities on the parameter box (branch-and-bound)
# =============================================================================================
G = "2 crossing geometry"
gate(G, "B1a", "15353, 15969", "D_x >= 37/18 on x in [0,1/2]", Dx, [x], [(0, F(1, 2))], F(37, 18))
gate(G, "B1b", "15969", "P_x >= 7/9", Px, [x], [(0, F(1, 2))], F(7, 9))
gate(G, "B1c", "15969", "P_x <= 2", 2 - Px, [x], [(0, F(1, 2))])
gate(G, "B1d", "15970", "D_x - P_x >= 1 (> 0)", Dx - Px, [x], [(0, F(1, 2))], F(1))
gate(G, "B1e", "15972", "J >= 35/54 on [0,5/6]x[0,1/2] (tight at delta=5/6, x=1/2)", J, [de, x], BOXdx, F(35, 54))
gate(G, "B1f", "15972", "J <= 5/2", R(5, 2) - J, [de, x], BOXdx)
gate(G, "B2a", "15360-15363", "r_*(t) >= 23/37 on t in [1,3/2], x in [0,1/2] (times D_x; tight at t=1, x=1/2)",
     Nt - R(23, 37) * Dx, [t, x], BOXtx)
gate(G, "B2b", "15363", "r_*(t) <= 1", Dx - Nt, [t, x], BOXtx)
gate(G, "B2c", "15363", "t - r_*(t) >= 1/3 (tight at t=1, x=0)", Dx * t - Nt - Dx / 3, [t, x], BOXtx)
gate(G, "B2d", "15363", "t - r_*(t) <= 1/2 (tight at t=3/2)", Dx / 2 - (Dx * t - Nt), [t, x], BOXtx)
gate(G, "B2e", "15322-15329", "plain exponents decrease in m: 2 - 4x/(9/2+12D) >= 14/9 and 2 - 8x/9 >= 14/9",
     (2 - 4 * x / (R(9, 2) + 12 * Dl) - R(14, 9)) * (R(9, 2) + 12 * Dl), [x, Dl], [(0, F(1, 2)), (0, F(1, 24))])

G = "3 Lemma 17.1 instances"
# r = r_* + s (1 - r_*), s in [0,1];  selected whole-slot length z' = mu * z_M(r), mu in [0,1]
# (z' <= z_M(r) - nu0 <= z_M(r) is a superset of the manuscript's domain).
r_s = rstar + s * (1 - rstar)
g2 = (3 - R(9, 37)) - 2 * r_s - 8 * mu * zM(r_s)
gate(G, "M1", "15371-15379, 9278", "2r + 8z <= 3m - c2 with m = 1, c2 = 9/37 for every r >= r_*(t), "
     "z <= z_M(r)  [times D_x; tight only at t=1, x=1/2, s=0, mu=1]",
     sp.expand(sp.cancel(g2 * Dx)), [t, x, s, mu], BOXtx + [(0, 1), (0, 1)])
g1 = (1 - 2 * nu) - r - 2 * mu * (zM(r) - nu)
gate(G, "M2", "15371-15373, 9278", "r + 2z <= m - c1 with c1 = 2 nu0 for z = mu (z_M(r) - nu0), r in [23/37, 1-2nu0], "
     "nu0 in (0,1/1000]  [s parametrises r]",
     sp.expand(g1.subs(r, R(23, 37) + s * (1 - 2 * nu - R(23, 37)))), [s, mu, nu],
     [(0, 1), (0, 1), (0, F(1, 1000))])
gate(G, "M3", "15385-15386", "inverse capacity z_M(r) <= 7/37 on r >= r_*(t)  [times D_x]",
     sp.expand(sp.cancel((R(7, 37) - zM(r_s)) * Dx)), [t, x, s], BOXtx + [(0, 1)])
gate(G, "M4", "15372, 9277", "0 <= r <= 1 on the inverse branch  [times D_x]", sp.expand(sp.cancel(r_s * Dx)), [t, x, s], BOXtx + [(0, 1)])

G = "4 Lemma 18.1 instances"
# plain branch: r in [t - 1/2, r_*], m in [t - r, 1/2]  =>  m in [t - r_*, 1/2] subset [1/3, 1/2]
m_v = (t - rstar) + v * (R(1, 2) - (t - rstar))
zsel = mu * zP(m_v)
hyp18 = 1 - 2 * m_v - 6 * kap * zsel
gate(G, "P1", "15174-15179, 12571", "n1+n2+6 kappa z <= M (M = 1) for z = mu z_P(m), every m in [t-r_*, 1/2]  "
     "[margin 0 at mu = 1: invoked at equality; the hypothesis is non-strict]",
     sp.expand(sp.cancel(hyp18 * Dx)), [t, x, v, mu, Dl], BOXtx + [(0, 1), (0, 1), (0, F(1, 24))])
gate(G, "P2", "12531", "kappa = 3/4 + 2 Delta in [3/4, 1] for Delta in [0, 1/24]  (kappa <= 5/6)",
     R(5, 6) - kap, [Dl], [(0, F(1, 24))])
gate(G, "P3", "15386-15387", "plain capacity z_P(m) <= 2/27 on the plain branch  [times 6 kappa D_x]",
     sp.expand(sp.cancel((R(2, 27) - zP(m_v)) * 6 * kap * Dx)), [t, x, v, Dl], BOXtx + [(0, 1), (0, F(1, 24))])
gate(G, "P4", "16118-16121, 12560", "mesh: base-U slot length ell_i/d <= 2 ell_i for d in [1/2, h + 1/48]",
     2 * d - 1, [d], [(F(1, 2), F(5, 6))])
gate(G, "P5", "15166-15179", "robust variant: with z = z_P(m) - nu0 the Lemma 18.1 condition has margin 6 kappa nu0 >= 9 nu0/2",
     sp.expand((1 - 2 * m - 6 * kap * (zP(m) - nu)) - R(9, 2) * nu), [m, Dl, nu],
     [(F(1, 3), F(1, 2)), (0, F(1, 24)), (0, F(1, 1000))])

G = "5 supply"
gate(G, "Q1", "15388-15391", "supply ell/d - 7/37 >= 23/1443 for d in [1/2, h]  [times d; tight at d=h]",
     ell - (R(7, 37) + R(23, 1443)) * d, [d], [(F(1, 2), F(13, 16))])
gate(G, "Q2", "16121-16126", "supply ell/d >= 1/5 for d in [1/2, h+1/48]; margin over 7/37 is 2/185",
     ell - R(1, 5) * d, [d], [(F(1, 2), F(5, 6))])
rec(G, "Q3", "16116, 16126", "8/39 - 7/37 = 23/1443, 1/5 - 7/37 = 2/185, 5 ell - h = 1/48, 2/27 < 7/37",
    R(8, 39) - R(7, 37) == R(23, 1443) and R(1, 5) - R(7, 37) == R(2, 185) and 5 * ell - h == R(1, 48)
    and R(2, 27) < R(7, 37))

G = "6 Delta/4 comparison"
lossfac = R(1, 4) - 48 * x * de * (1 - 2 * m) / (9 * (R(9, 2) + 12 * Dl))   # (Delta/4 - increase)/Delta
gate(G, "K1", "15392-15405", "increase <= Delta/4 with slack >= (83/972) Delta on delta<=5/6, x<=1/2, m in [1/3,1/2], "
     "Delta<=1/24 [times 9(9/2+12D); tight at delta=5/6, x=1/2, m=1/3, Delta=0]",
     sp.expand((lossfac - R(83, 972)) * 9 * (R(9, 2) + 12 * Dl)), [de, x, m, Dl],
     [(0, F(5, 6)), (0, F(1, 2)), (F(1, 3), F(1, 2)), (0, F(1, 24))])
rec(G, "K2", "15402-15404", "manuscript's crude chain: 24*(1/2)*(1/3)/(4*4) = 1/4 (2q<=1, 1-2m<=1/3, denominators>=4)",
    R(24) * R(1, 2) * R(1, 3) / 16 == R(1, 4))
rec(G, "K3", "15392-15405", "exact worst ratio increase/(Delta/4) as Delta->0 is 160/243 (< 1)",
    sp.limit(4 * 48 * R(5, 12) * (1 - 2 * R(1, 3)) / (9 * (R(9, 2) + 12 * Dl)), Dl, 0) == R(160, 243))

G = "7 Prop 19.2 case cover"
# Independent of the manuscript's decomposition: for each branch, the count used <= stated bound.
# Plain branch: r = r_* - s (r_* - (t-1/2)), m = (t-r) + v (1/2 - (t-r)), actual capacity z_P(m).
r_pl = rstar - s * (rstar - (t - R(1, 2)))
m_pl = (t - r_pl) + v * (R(1, 2) - (t - r_pl))
marg_pl = (Rshort + Dl / 4) - C_pl(m_pl, zP(m_pl))
ident(G, "C1a", "15363-15418", "plain branch decomposition (derived here): R_short(t) + Delta/4 - C_pl(m, z_P(m)) = "
      "delta(2-8x/9)[(r_* - r) + (m - (t-r))] + Delta*K(m), K = 1/4 - 48 q(1-2m)/(9(9/2+12 Delta))",
      Rshort + Dl / 4 - C_pl(m, zP(m)), de * (2 - R(8, 9) * x) * ((rstar - r) + (m - (t - r))) + Dl * lossfac)
rec(G, "C1", "15363-15418", "plain branch: C_pl(m, z_P(m)) <= R_short(t) + Delta/4 on r in [t-1/2, r_*], m in [t-r, 1/2]: "
    "each term of C1a is >= 0 (r <= r_*, m >= t-r by the branch; 2-8x/9 >= 14/9 by B2e; K >= 83/972 by K1 since "
    "m >= t - r_* >= 1/3 by B2c)",
    all(o["ok"] for o in OUT if o["id"] in ("C1a", "B2e", "K1", "B2c")))
# Supplementary direct attempt (no decomposition), time-boxed; informational only
r_pl = rstar - s * (rstar - (t - R(1, 2)))
m_pl = (t - r_pl) + v * (R(1, 2) - (t - r_pl))
marg_pl = (Rshort + Dl / 4) - C_pl(m_pl, zP(m_pl))
_rd = certify_ge(sp.expand(sp.cancel(marg_pl * Dx * (R(9, 2) + 12 * Dl))), [de, x, t, Dl, s, v],
                 [(0, F(5, 6)), (0, F(1, 2)), (1, F(3, 2)), (0, F(1, 24)), (0, 1), (0, 1)], budget=60000, seconds=60)
DIRECT_C1 = dict(ok=_rd["ok"], boxes=_rd["boxes"], undecided=_rd.get("undecided", False), witness=_rd.get("witness"))
print("INFO [C1-direct] plain branch by direct 6-variable B&B (not a gate):", DIRECT_C1, flush=True)
ident(G, "C2a", "15364-15418", "inverse branch: R_short(t) - A_I(r) = delta(1-x)(r - r_*)", Rshort - AI(r), de * (1 - x) * (r - rstar))
ident(G, "C3a", "15297-15311", "long branch: L(t) - (1-alpha+(alpha-delta)r) = (alpha-delta)(t-r)",
      Lt - (1 - al + (al - de) * r), (al - de) * (t - r))
r_in = rstar + s * (1 - rstar)
gate(G, "C2", "15364-15418", "inverse branch: A_I(r) <= R_short(t) for r in [r_*, 1]  [times D_x]",
     sp.expand(sp.cancel((Rshort - AI(r_in)) * Dx)), [de, x, t, s],
     [(0, F(5, 6)), (0, F(1, 2)), (1, F(3, 2)), (0, 1)])
r_lg = 1 + s * (t - 1)
gate(G, "C3", "15297-15311", "long branch (Lemma 17.6, r in [1,t]): 1-alpha+(alpha-delta)r <= L(t) for delta <= alpha",
     sp.expand(Lt - (1 - al + (al - de) * r_lg)), [de, t, s], [(0, F(5, 6)), (1, F(3, 2)), (0, 1)])
gate(G, "C4", "15312-15315", "m >= 1/2 branch: 1-2 delta m <= 1-delta <= R_short(t)  [times D_x]",
     sp.expand(sp.cancel((Rshort - (1 - 2 * de * (R(1, 2) + v))) * Dx)), [de, x, t, v],
     [(0, F(5, 6)), (0, F(1, 2)), (1, F(3, 2)), (0, F(1, 2))])
gate(G, "C5", "15421-15426", "zero inverse capacity (r >= 1-2nu0): 1-delta r <= 1-delta+2 delta nu0",
     sp.expand((1 - de + 2 * de * nu) - (1 - de * (1 - 2 * nu + 2 * nu * s))), [de, nu, s],
     [(0, F(5, 6)), (0, F(1, 1000)), (0, 1)])
gate(G, "C6", "15426-15428", "zero plain capacity (1-2m <= 6 kappa nu0): 1-2 delta m <= 1-delta+6 delta nu0",
     sp.expand((1 - de + 6 * de * nu) - (1 - de * (1 - 6 * kap * nu * s))), [de, nu, s, Dl],
     [(0, F(5, 6)), (0, F(1, 1000)), (0, 1), (0, F(1, 24))])
gate(G, "C7", "15315, 15428", "R_short(t) >= 1 - delta  [times D_x]", sp.expand(sp.cancel((Rshort - (1 - de)) * Dx)),
     [de, x, t], [(0, F(5, 6)), (0, F(1, 2)), (1, F(3, 2))])
gate(G, "C8", "15434-15444", "no-slot t=1: inverse 1-delta r (r in [2/3,1]) and plain 1-2 delta m (m >= 1-r, r<=2/3) "
     "are <= 1 - 2 delta/3",
     sp.expand((1 - R(2, 3) * de) - (1 - de * (R(2, 3) + s / 3))), [de, s], [(0, F(5, 6)), (0, 1)])

G = "8 endpoint"
gate(G, "E1", "15974-15975", "cutoff t >= 1 (delta P_x >= 0) on the Lemma 20.2 box", de * Px, [de, x], BOXdx)
gate(G, "E2", "15974-15975", "cutoff t <= 3/2: J - delta P_x = (alpha-delta) D_x >= 0", J - de * Px, [de, x], BOXdx)
gate(G, "E3", "16130", "R_* >= 1 - delta  [times 2J]", sp.expand(sp.cancel((Rstar_end - (1 - de)) * 2 * J)), [de, x], BOXdx)
gate(G, "E4", "16139", "R_* <= 17/12  [times 2J]  (in fact R_* <= 1)", sp.expand(sp.cancel((R(17, 12) - Rstar_end) * 2 * J)),
     [de, x], BOXdx)
gate(G, "E4b", "16139 (sharper)", "R_* <= 1  [times 2J]", sp.expand(sp.cancel((1 - Rstar_end) * 2 * J)), [de, x], BOXdx)
gate(G, "E5", "16141", "R_* + Delta/4 <= 139/96  [times 2J]", sp.expand(sp.cancel((R(139, 96) - Rstar_end - Dl / 4) * 2 * J)),
     [de, x, Dl], BOXdx + [(0, F(1, 24))])
gate(G, "E6", "16131-16134", "slope R + delta/2 - 17/50 >= 4/25 for R >= 1 - delta, delta <= 5/6",
     (1 - de) + de / 2 - z0 - R(4, 25), [de], [(0, F(5, 6))])
rec(G, "E7", "16143-16144", "extension cost: 139/96 + 1/2 - 17/50 < 2; floor slope 1+1/100-17/50 and alpha-slope "
    "(1-5/6)+5/12-17/50 are < 2", R(139, 96) + R(1, 2) - z0 < 2 and 1 + R(1, 100) - z0 < 2 and R(1, 6) + R(5, 12) - z0 < 2)
negE = sp.expand(sp.cancel(-Estar * 2 * J))
t0 = time.time()
gate(G, "E8", "15994-16072 (Lemma 20.2)", "-E_* >= 49/440640 on [0,5/6]x[0,1/2]  [times 2J; independent of (20.9)]",
     sp.expand(negE - R(49, 440640) * 2 * J), [de, x], BOXdx)
gate(G, "E9", "beyond source", "-E_* >= 228/10^6 (true minimum ~2.2815e-4)", sp.expand(negE - R(228, 10 ** 6) * 2 * J),
     [de, x], BOXdx)
gate(G, "E10", "15942-15946", "delta = alpha endpoint: E(h) <= -1/48 - delta/16 for q <= delta/2 (R = 1-delta)",
     sp.expand((C0 + (R(3, 4) - h) * de) - Eh.subs({RR: 1 - de})), [de, x], BOXdx)
gate(G, "E11", "16080-16106", "adaptive endpoint: E_* + h Delta/4 - Delta <= -49/440640 - (51/64) Delta  [times 2J]",
     sp.expand(sp.cancel((-R(49, 440640) - R(51, 64) * Dl - (Estar + h * Dl / 4 - Dl)) * 2 * J)),
     [de, x, Dl], BOXdx + [(0, F(1, 24))])

G = "9 ranges of invoked lemmas"
gate(G, "H1", "4512-4517, 15929", "Prop 8.3 is invoked with t in [1,3/2]: both cutoff bounds (E1, E2) and "
     "1/50 < delta <=> a > 51/100", (1 + de) / 2 - R(51, 100) - (de - R(1, 50)) / 2, [de], [(F(1, 50), F(5, 6))])
gate(G, "H2", "15022-15024", "Lemma 19.1 range: a = (1+delta)/2 in [51/100, 1] for delta in [1/50, 5/6]",
     1 - (1 + de) / 2, [de], [(F(1, 50), F(5, 6))])
gate(G, "H3", "12397-12401, 15269", "Lemma 17.6: inverse witness length r in [t-1/2, t] subset [1/2, 3/2] = bounded "
     "nonnegative range (R0 = 3/2 + o(1))", t - R(1, 2) - R(1, 2), [t], [(1, F(3, 2))])
gate(G, "H4", "4523-4531", "Prop 8.3 saturation: 2 delta (m-1/2)_+ <= C eps gives (m-1/2)_+ <= 25 C eps for delta >= 1/50",
     25 * 2 * de - 1, [de], [(F(1, 50), F(5, 6))])
gate(G, "H5", "15476-15485", "height ceiling: tau_0 = d_min eps_ht/(20(A+1)) <= d_min/100 whenever eps_ht <= 1/5 "
     "(A >= 0); y stands for eps_ht", R(1, 100) - y / 20, [y], [(0, F(1, 5))])

# derivative (Lipschitz) bounds behind 16074-16075
G = "10 Lipschitz bounds"
dt_dd = sp.cancel(sp.diff(tcut, de))
dt_dx = sp.cancel(sp.diff(tcut, x))
dR_dd = sp.cancel(sp.diff(Rstar_end, de))
dR_dx = sp.cancel(sp.diff(Rstar_end, x))
ident(G, "L0", "16074", "dt/d delta = alpha P_x D_x/(2 J^2)", dt_dd, al * Px * Dx / (2 * J ** 2))
for cid, ex, bd in (("L1", dt_dd, 6), ("L2", dt_dx, 3), ("L3", dR_dd, 6), ("L4", dR_dx, 2)):
    nume, deno = sp.fraction(sp.together(ex))
    # deno is (a power of) J times positive constants: verify sign, then certify |ex| <= bd
    sgn = ival(to_pd(deno, [de, x]), [(F(0), F(5, 6)), (F(0), F(1, 2))])
    ok_den = sgn[0] > 0
    up = certify_ge(sp.expand(bd * deno - nume), [de, x], BOXdx)
    lo = certify_ge(sp.expand(bd * deno + nume), [de, x], BOXdx)
    rec(G, cid, "16074-16075", f"|{['dt/ddelta', 'dt/dx', 'dR_*/ddelta', 'dR_*/dx'][int(cid[1]) - 1]}| <= {bd} on the box",
        ok_den and up["ok"] and lo["ok"], dict(boxes=up["boxes"] + lo["boxes"]))
r_dt = sp.cancel(sp.diff(rstar, t))
gate(G, "L5", "16074", "0 <= dr_*/dt = (2-8x/9)/D_x <= 1", Dx - (2 - R(8, 9) * x), [x], [(0, F(1, 2))])

# =============================================================================================
# 4. Failing controls: each removes one load-bearing restriction; an exact violation must appear
# =============================================================================================
G = "11 failing controls"
control(G, "FC1", "control", "Lemma 17.1 c2 = 9/37 on the WHOLE witness range r in [t-1/2, 1] (drop r >= r_*)",
        sp.expand((3 - R(9, 37)) - 2 * (t - R(1, 2) + s * (R(3, 2) - t)) - 8 * zM(t - R(1, 2) + s * (R(3, 2) - t))),
        [t, s], [(1, F(3, 2)), (0, 1)])
control(G, "FC2", "control", "r_*(t) >= 23/37 with the amplitude range widened to x in [0,1]",
        Nt - R(23, 37) * Dx, [t, x], [(1, F(3, 2)), (0, 1)])
control(G, "FC3", "control", "Delta/4 comparison without m >= 1/3 (m in [0,1/2])",
        sp.expand(lossfac * 9 * (R(9, 2) + 12 * Dl)), [de, x, m, Dl],
        [(0, F(5, 6)), (0, F(1, 2)), (0, F(1, 2)), (0, F(1, 24))])
control(G, "FC4", "control", "supply ell/d >= 7/37 on d in [1/2, 9/10] (frequency range beyond h + 1/48)",
        ell - R(7, 37) * d, [d], [(F(1, 2), F(9, 10))])
control(G, "FC5", "control", "Lemma 18.1 with the BASELINE capacity 2(1-2m)/9 at the actual kappa = 3/4 + 2Delta",
        1 - 2 * m - 6 * kap * zP0(m), [m, Dl], [(F(1, 3), F(1, 2)), (0, F(1, 24))])
control(G, "FC6", "control", "Lemma 20.2 with margin 229/10^6 (above the true minimum)",
        sp.expand(negE - R(229, 10 ** 6) * 2 * J), [de, x], BOXdx)
control(G, "FC7", "control", "plain-side bound WITHOUT the Delta/4 term (C_pl(m,z_P(m)) <= R_short(t))",
        sp.expand(sp.cancel((Rshort - C_pl(m_pl, zP(m_pl))) * Dx * (R(9, 2) + 12 * Dl))), [de, x, t, Dl, s, v],
        [(0, F(5, 6)), (0, F(1, 2)), (1, F(3, 2)), (0, F(1, 24)), (0, 1), (0, 1)])
control(G, "FC8", "control", "B&B sanity: J >= 1 (false; min is 35/54)", J, [de, x], BOXdx, F(1))

# =============================================================================================
# 5. FLOATING_RECONNAISSANCE (not a gate): our model's optimised count vs R_* + Delta/4
# =============================================================================================
G = "12 float reconnaissance"
try:
    sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
    import threshold_calculus as tc
    import numpy as np
    fR = sp.lambdify((de, x), Rstar_end, "numpy")
    worst_excess, worst_ratio = -1.0, 0.0
    for Dv in (1e-3, 1 / 96, 1 / 48, 1 / 24):
        kv = 0.75 + 2 * Dv
        for dv in np.linspace(0.03, min(kv, 5 / 6) - 1e-9, 23):
            for xv in np.linspace(0, 0.5, 11):
                Rm = tc.R_fast(float(dv), float(xv), kv, (1 / 6) / (13 / 16))
                ex = Rm - (fR(dv, xv) + Dv / 4)
                worst_excess = max(worst_excess, ex)
                worst_ratio = max(worst_ratio, (Rm - fR(dv, xv)) / Dv)
    rec(G, "F1", "model", "threshold_calculus.R_fast(kappa=3/4+2Delta) <= R_* + Delta/4 on a grid (float, not a gate)",
        worst_excess <= 1e-12, dict(max_excess=worst_excess, max_model_penalty_over_Delta=worst_ratio))
except Exception as exc:  # pragma: no cover
    rec(G, "F1", "model", "float reconnaissance skipped", True, repr(exc))

# =============================================================================================
gates = [o for o in OUT if not o["control"] and o["group"] != "12 float reconnaissance"]
ctrls = [o for o in OUT if o["control"]]
summary = dict(object_sha256=EXPECTED_SHA, n_gates=len(gates), n_gates_pass=sum(o["ok"] for o in gates),
               n_controls=len(ctrls), n_controls_ok=sum(o["ok"] for o in ctrls),
               arithmetic="EXACT: sympy over Q for identities; Fraction branch-and-bound for inequalities",
               supplementary_direct_C1=DIRECT_C1,
               checks=OUT)
with open(os.path.join(HERE, "sep30_junction_check_output.json"), "w") as fh:
    json.dump(summary, fh, indent=1)
print(f"\n{summary['n_gates_pass']}/{summary['n_gates']} gates pass; "
      f"{summary['n_controls_ok']}/{summary['n_controls']} failing controls fail as designed")
sys.exit(0 if (summary["n_gates_pass"] == summary["n_gates"] and summary["n_controls_ok"] == summary["n_controls"]) else 1)
