#!/usr/bin/env python3
"""Exact checks for the PROPOSED Lemmas P1F.0-P1F.2 in REMARK_19_3.md.

Status: exploration-level checks for a PROPOSED object. Nothing here is a claim about RH,
which is unsolved. The manuscript and the Lean sources are read as untrusted text: they are
hashed and searched, never executed.

Usage (run with `python3 -I`):
    python3 -I remark_19_3_checks.py PAPER_TEX [--lean LEAN_ROOT] [--json OUT.json]

PAPER_TEX  the Sep 30 paper.tex extracted from ref 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6
           (SHA-256 42a5ee0f...deac6a3; checked by gate T0).
LEAN_ROOT  optional: the directory `upstream/lean` at the same ref (the directory that contains
           `OAI/`). If given, group L checks file hashes against the git blobs at the ref, the
           quoted declaration text at the cited file:line, and membership of each cited module
           in the import closure of OAI.NumberTheory.DirichletL.Nonvanishing.

Groups
  T  text gates on the manuscript (hash, anchors, theorem numbering, the delta <= alpha census)
  A  exact algebra for P1F.0 (exponent bookkeeping of paper lines 15268-15292)
  B  exact algebra for P1F.1 (two-case row count)
  C  exact algebra for P1F.2 (high-bin margin) and the Lean exponent identities
  G  exact rational grid sweeps (sanity, not a proof)
  L  Lean text anchors and closure membership (optional)
  F  failing controls: each must FIRE (find the counterexample it is built to find)

Exit status 0 iff every gate passes and every failing control fires.
Arithmetic: sympy Rationals and fractions.Fraction only; no floating point in any gate.
"""

import hashlib
import itertools
import json
import os
import re
import sys
import time
from fractions import Fraction as Fr

import sympy as sp

PAPER_SHA256 = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"

# SHA-256 of the Lean files, computed from the git blobs at ref 31c706bb (git show | sha256sum).
LEAN_SHA256 = {
    "Hecke/DetectorNoSlotInverseCount.lean": "379a8ec696d698d261265c4a06704ebf3bcd8f715bf664edd3d095b44480b6a7",
    "Hecke/DetectorHighCount.lean": "38232c049a7d7440e58f4900c79e971e42a64ba46dcf3a6f35bbfade355f98b6",
    "Hecke/DetectorRowCountEndpoint.lean": "79717dfc44a31432e01eba2992f2e136589659929168f4f33a70df4b2caef875",
    "Hecke/DetectorWitnessRows.lean": "fb3f851ef3d6f4a260a584bf5511fe09704dad364da6f1f2bdf4c4fe7720d15b",
    "Hecke/InverseAmplificationBudget.lean": "25ac5ce13723bf3f0660d8845a3c7b1579852016b46d6b05d8589249b3a55e83",
    "Hecke/InverseAmplificationEndpoint.lean": "11580ed37a1c8f2ecfd4d58ed1f90836818aaf812d2052c27343c2ac5bd3d5b4",
    "Hecke/InverseAmplificationRowwise.lean": "cce7c7a2c63b24649183bb14120cde67bc43bb1cc088b92d343b1a72c971895f",
    "Hecke/DetectorRawFiber.lean": "491911b0b17d19943fdb1b43f479e741279e0c0c2b9f1e9e9c5d11de24335c5d",
    "Hecke/DetectorAdaptiveCutoff.lean": "494cc048ad3438976fcab45b364e3c2828e51cdaee3aa2eac00268119514f92a",
    "Detector/CentralExponent.lean": "c138e38592cb202bbc4c13021d65378163c77988ebda575a2af39c6961b92a83",
    "Detector/CentralMixedMargins.lean": "635ed51704661906d6c751bed052cfbacde4d5d9207179be65d328877f7d034d",
    "Detector/FinalAssemblyCountParameters.lean": "88b1a01167a672f116f0285f9384ed5c888cc456a55da7dbc71c90498632a968",
    "Detector/FinalAssemblyHigh.lean": "51fff0db37a0e2cab919256b87ac4456ca601991e02fbf8543e2d4e1573cb5e4",
    "Detector/CentralDyadicWeight.lean": "731176a3f226ff14ad0eea1ab1f73c8cd8c81d870dd6672676298e1abcdd0f22",
    "Detector/DetectorInverseRawField.lean": "405a368337f3dbf5ce14ce525de5c67a6949edffa9f193654c3832958c95e869",
    "PrimeRows/NonfloorCount.lean": "a52ccf6c3e635d3305336b6ede7b6b82271c0b8606178e410be3110e632734af",
    "PrimeRows/NonfloorExponent.lean": "a8575c7e463a5a671a00c3a0a8ddc16f789d67767237d2ae7b8b37000f4127f3",
}
LEAN_PREFIX = os.path.join("OAI", "NumberTheory", "DirichletL")
LEAN_ROOT_MODULE = "OAI.NumberTheory.DirichletL.Nonvanishing"

# (file, line, exact substring that must occur on that line)
LEAN_ANCHORS = [
    ("Hecke/DetectorNoSlotInverseCount.lean", 14, "theorem no_slot_inverse_count"),
    ("Hecke/DetectorNoSlotInverseCount.lean", 24, "1<U → 1/2≤a →"),
    ("Hecke/DetectorNoSlotInverseCount.lean", 29, "0≤Real.logb U ((2 : ℝ)^J.val) → Real.logb U ((2 : ℝ)^J.val)≤R →"),
    ("Hecke/DetectorNoSlotInverseCount.lean", 39, "RawMoment data W c κ C ∧ RawMoment data (scaleProfile W) c κ C) →"),
    ("Hecke/DetectorNoSlotInverseCount.lean", 41, "U^(sourceExponent (Real.logb U ((2 : ℝ)^J.val))-"),
    ("Hecke/DetectorNoSlotInverseCount.lean", 42, "(2*a-1)*Real.logb U ((2 : ℝ)^J.val)+2*ε+εm)"),
    ("Hecke/InverseAmplificationBudget.lean", 10, "def sourceExponent (r : ℝ) : ℝ := max 1 ((1+5*r)/6)"),
    ("Hecke/InverseAmplificationBudget.lean", 41, "theorem exists_amplification_budget"),
    ("Hecke/InverseAmplificationEndpoint.lean", 11, "theorem no_slot_endpoint"),
    ("Hecke/InverseAmplificationRowwise.lean", 29, "theorem no_slot_rowwise_endpoint"),
    ("Hecke/DetectorWitnessRows.lean", 26, "inverse_length_lower : tstar-1/2-76*ε≤r"),
    ("Hecke/DetectorWitnessRows.lean", 30, "inverse_spike : U^((2*a-1)*r-2*ε)≤"),
    ("Hecke/DetectorRowCountEndpoint.lean", 71, "theorem high_bin_count {B C U δ r ε γ : ℝ}"),
    ("Hecke/DetectorRowCountEndpoint.lean", 72, "(hC : 0≤C) (hU : 1≤U) (hδ : 5/6≤δ) (hδ' : δ≤1)"),
    ("Hecke/DetectorRowCountEndpoint.lean", 73, "(hγ : 0≤γ) (hr : 1-γ≤r)"),
    ("Hecke/DetectorRowCountEndpoint.lean", 74, "(hI : B≤C*U^(max 1 ((1+5*r)/6)-δ*r+ε)) :"),
    ("Hecke/DetectorRowCountEndpoint.lean", 75, "B≤C*U^(1-δ+ε+γ) := by"),
    ("Hecke/DetectorRowCountEndpoint.lean", 88, "theorem high_bin_endpoint {δ q R loss : ℝ} (_hδ : 5/6≤δ)"),
    ("Hecke/DetectorRowCountEndpoint.lean", 90, "-(1/48 : ℝ)+(2/3)*δ+q/6-(13/16)*(1-R)≤"),
    ("Hecke/DetectorRowCountEndpoint.lean", 91, "-1/48-δ/16+(13/16)*loss := by"),
    ("Hecke/DetectorHighCount.lean", 12, "theorem high_count_from_raw_moments"),
    ("Hecke/DetectorHighCount.lean", 22, "1<U → 5/6≤2*a-1 → a≤1 → 0≤ε → ε≤1/1000 → 0≤C → 0≤height →"),
    ("Hecke/DetectorHighCount.lean", 24, "(F : Fiber M H Label Slot U a ε (3/2) T allowance i)"),
    ("Hecke/DetectorHighCount.lean", 26, "(F.rows.card : ℝ)≤fiberConstant C height K₀*U^(1-(2*a-1)+78*ε+εm)"),
    ("Hecke/DetectorHighCount.lean", 38, "moments.inverse_raw"),
    ("Hecke/DetectorAdaptiveCutoff.lean", 27, "theorem cutoff_eq_high (δ q : ℝ) (hδ : 5/6<δ) : cutoff δ q=3/2"),
    ("Detector/CentralExponent.lean", 16, "-1/48+(2/3)*δ+q/6-(13/16)*(1-R)+(d-13/16)*(R+δ/2-17/50)"),
    ("Detector/CentralExponent.lean", 53, "lemma high_source_margin (δ R q Δ loss ζ d : ℝ)"),
    ("Detector/CentralExponent.lean", 54, "(hq : q≤δ/2) (hR : R≤1-δ+loss)"),
    ("Detector/CentralExponent.lean", 56, "(hslo : 0≤R+δ/2-17/50) (hshi : R+δ/2-17/50≤2) :"),
    ("Detector/CentralExponent.lean", 58, "-1/48-δ/16-Δ+(13/16)*loss+2*ζ := by"),
    ("Detector/CentralMixedMargins.lean", 38, "lemma high_mixed_margin (δ q Δ loss ζ μ v d : ℝ)"),
    ("Detector/CentralMixedMargins.lean", 39, "(hδ : 5/6≤δ) (hd : δ≤1) (hq : q≤δ/2)"),
    ("Detector/CentralMixedMargins.lean", 40, "(hl : 0≤loss) (hl' : loss≤1/32)"),
    ("Detector/CentralMixedMargins.lean", 43, "-1/48-δ/16-Δ+(13/16)*loss+2*ζ+μ := by"),
    ("Detector/FinalAssemblyCountParameters.lean", 39, "high : ∃K₀ : ℝ,0≤K₀ ∧ ∀ᶠ U : ℝ in atTop,"),
    ("Detector/FinalAssemblyCountParameters.lean", 41, "1<U → 5/6<2*a-1 → a≤1 → 0≤ε → ε≤1/1000 → 0≤C → 0≤height →"),
    ("Detector/FinalAssemblyCountParameters.lean", 47, "fiberConstant C height K₀*(Fintype.card B.Bin:ℝ)*U^(1-(2*a-1)+78*ε+εm)"),
    ("Hecke/DetectorRawFiber.lean", 46, "supply : 7/37≤∑ s∈slots,widths s"),
    ("Hecke/DetectorRawFiber.lean", 64, "inverse_raw : ∀ n : ℕ,n≤2 → ∀ s∈Icc (0 : ℝ) 1,∀ t∈Icc (-height) height,"),
    ("Detector/CentralDyadicWeight.lean", 46, "def mixedSourceExponent (a v d R q : ℝ) : ℝ :="),
    ("Detector/CentralDyadicWeight.lean", 47, "ProbeCentralExponent.sourceExponent a v R q+(d-v)*R"),
    ("Detector/FinalAssemblyHigh.lean", 115, "have hΔ1 : HeckeZeroSupremum.beta-7/8≤1/8"),
    ("Detector/DetectorInverseRawField.lean", 44, "theorem source_batch_inverse_raw"),
    ("PrimeRows/NonfloorCount.lean", 58, "theorem high_adaptive_count_from_raw_moments"),
    ("PrimeRows/NonfloorExponent.lean", 33, "have hh := high_mixed_margin (2*a-1) q Δ (78*ε+εm) ζ μ v d"),
]

# (line, exact substring) anchors in paper.tex
PAPER_ANCHORS = [
    (4285, r"a\in(51/100+e\mathbb Z_{\ge0})\cap[51/100,1]"),
    (4372, r"\delta=2a-1,\qquad 1/50\le\delta\le1."),
    (4403, r"0<e<e_0,\qquad (1+T_1)^{A_{\mathcal A}}\le U^{\epsilon/10},"),
    (4510, r"\begin{proposition}[Two saturated witnesses]\label{prop:detector-witness}"),
    (4513, r"For every \(t\in[1,3/2]\),"),
    (4529, r"t-\tfrac12-O(\epsilon)\le r\le t+O(1/\log U),"),
    (4531, r"|M_r|^2\gg_{\mathcal A,\epsilon}U^{\delta r-\epsilon},"),
    (4536, r"The constants in the \(O(\epsilon)\) terms are absolute on the"),
    (4675, r"Since \(\delta\ge1/50\), this implies"),
    (9250, r"\begin{lemma}[Marked inverse moment]\label{lem:marked}"),
    (9254, r"r+2z\le m-c_1,\qquad 2r+8z\le3m-c_2."),
    (12346, r"Lemma~\ref{lem:marked}, take \(Z=H,\ m=1\), no slots, and"),
    (12357, r"\ll_{c,\epsilon,W} H(HD)^\epsilon,\qquad H\ge D^{1+c}."),
    (12362, r"\begin{lemma}[Sixth-power amplification]\label{lem:inverse-amplification}"),
    (12366, r"valuation of the ideal \((u)\) is at most five."),
    (12369, r"H=\max(2U,D^{1+c}),\qquad P=(H/U)^{1/6}."),
    (12375, r"\ll \max\{U,U^{1/6}D^{5(1+c)/6}\}(UD)^\epsilon."),
    (12383, r"\qquad e(r)=\max\{1,(1+5r)/6\}."),
    (12387, r"\(\sigma_u\) in a fixed compact interval and \(|t_u|\le T_1\),"),
    (15185, r"\begin{proposition}[Row counts from the witnesses]\label{prop:detector-counts}"),
    (15188, r"\(a>51/100\), \(0<\delta=2a-1\le\alpha\), and mean amplitude"),
    (15222, r"\begin{proof}"),
    (15248, r"\paragraph{Inverse witnesses without selected primes.}"),
    (15262, r"\(-(\gamma-\nu)\), of absolute value at most \((3I+1)T_1\)."),
    (15266, r"\((3I+2)^A(1+T_1)^A\) changes only a fixed constant."),
    (15272, r"\max\left\{1,\frac{1+5(1+c)r}{6}\right\}"),
    (15274, r"\le e(r)+\frac{5cR_0}{6}+(1+R_0)\epsilon_0,"),
    (15278, r"\(c=3\epsilon_m/(10\max\{R_0,1\})\) and"),
    (15279, r"\(\epsilon_0=\epsilon_m/(4(1+R_0))\).  These are fixed before"),
    (15282, r"\begin{equation}\label{eq:no-slot-inverse-count}"),
    (15285, r"U^{e(r)-\delta r+\epsilon}(1+T_1)^{A_{\mathcal A}},\\"),
    (15288, r"1-\delta r,&0\le r\le1,\\"),
    (15289, r"1-\alpha+(\alpha-\delta)r,&r\ge1."),
    (15296, r"\paragraph{Cases requiring no selected primes.}"),
    (15303, r"Because \(\delta\le\alpha\) and \(r\le t+O(\epsilon)\), this is at"),
    (15446, r"\end{proof}"),
    (15448, r"\begin{remark}[Unselected inverse witnesses beyond the Part II bin ceiling]"),
    (15458, r"a>51/100,\qquad 1/50<\delta=2a-1\le1,"),
    (15464, r"\(\delta\le\alpha\) nor a prime-supply hypothesis."),
    (15467, r"\end{remark}"),
    (15513, r"h=\frac{13}{16},\qquad \ell=\frac16,\qquad"),
    (15514, r"l_x=\frac{17}{48},\qquad l_y=\frac{23}{48},\qquad"),
    (15726, r"\begin{equation}\label{eq:common-high-exponent}"),
    (15729, r"&=a-\frac78+h\left(\frac{17}{50}-\frac16\right)"),
    (15730, r"-a l_y-(1-a)\ell-(\delta/2-q)\ell"),
    (15731, r"+d\left(R+\frac\delta2-\frac{17}{50}\right)\\"),
    (15732, r"&=C_0+\frac23\delta+\frac q6-h(1-R)"),
    (15733, r"+(d-h)\left(R+\frac\delta2-\frac{17}{50}\right),"),
    (15734, r"\qquad C_0=-\frac1{48}."),
    (15928, r"At the live upper endpoint \(\delta=\alpha\), take \(t=3/2\) in"),
    (15944, r"E(h)\le C_0+\left(\frac34-h\right)\delta+O(\epsilon)"),
    (15945, r"=-\frac1{48}-\frac{\delta}{16}+O(\epsilon)<0."),
    (16123, r"0<\zeta<5\ell-h=\frac1{48},"),
    (16133, r"\ge\frac{33}{50}-\frac{\delta}{2}\ge\frac4{25}>0."),
    (16165, r"the last inequality uses \(\delta\le5/6\)."),
]

# Expected theorem numbers (section.counter) for the nodes cited in REMARK_19_3.md
EXPECTED_NUMBERS = {
    1123: "4.5", 4281: "8.1", 4385: "8.2", 4510: "8.3", 9250: "17.1", 9296: "17.2",
    9722: "17.5", 12362: "17.6", 15015: "19.1", 15185: "19.2", 15448: "19.3",
    15699: "20.1", 15994: "20.2", 16196: "20.3",
}

RESULTS = []


def record(gid, group, ok, detail, kind="gate"):
    RESULTS.append({"id": gid, "group": group, "kind": kind, "ok": bool(ok), "detail": detail})


def control(gid, fired, detail):
    RESULTS.append({"id": gid, "group": "F", "kind": "control", "ok": bool(fired), "detail": detail})


# ---------------------------------------------------------------- exact helpers
R = sp.Rational


def is_multiaffine(expr, variables):
    poly = sp.Poly(sp.expand(expr), *variables)
    return all(poly.degree(v) <= 1 for v in variables)


def vertex_max(expr, box):
    """Exact maximum of a multi-affine expression over a box = maximum over vertices."""
    names = list(box)
    assert is_multiaffine(expr, names), "expression is not multi-affine"
    best, arg = None, None
    for corner in itertools.product(*[box[v] for v in names]):
        val = sp.nsimplify(expr.subs(dict(zip(names, corner))))
        if best is None or val > best:
            best, arg = val, corner
    return best, dict(zip([str(v) for v in names], [str(c) for c in arg]))


def frange(lo, hi, n):
    lo, hi = Fr(lo), Fr(hi)
    return [lo + (hi - lo) * Fr(k, n) for k in range(n + 1)]


def e_of(r):
    """e(r) = max{1, (1+5r)/6} on Fractions."""
    return max(Fr(1), (1 + 5 * r) / 6)


# ---------------------------------------------------------------- group T
def text_gates(path, planted=None):
    raw = open(path, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    lines = raw.decode("utf-8").split("\n")
    if planted:
        for ln, text in planted.items():
            lines[ln - 1] = text
    out = {}
    out["T0"] = (sha == PAPER_SHA256, "sha256 " + sha)

    misses = [(ln, s) for ln, s in PAPER_ANCHORS if s not in lines[ln - 1]]
    out["T1"] = (not misses, "%d/%d anchors at the cited lines; misses: %s"
                 % (len(PAPER_ANCHORS) - len(misses), len(PAPER_ANCHORS), misses[:3]))

    # theorem numbering: theorem-like environments share one counter, reset by \section{
    sec, cnt, numbers = 0, 0, {}
    env = re.compile(r"\\begin\{(theorem|proposition|lemma|corollary|definition|remark)\}")
    for i, l in enumerate(lines, 1):
        if l.startswith("\\section{"):
            sec, cnt = sec + 1, 0
        if env.match(l):
            cnt += 1
            numbers[i] = "%d.%d" % (sec, cnt)
    bad = {k: (numbers.get(k), v) for k, v in EXPECTED_NUMBERS.items() if numbers.get(k) != v}
    out["T2"] = (not bad, "numbers of 14 cited nodes recomputed from the TeX counters; mismatches: %s" % bad)

    # T3: the delta <= alpha census inside the proof of Prop 19.2 (15222-15446)
    ineq = re.compile(r"\\delta\s*\\le\s*\\alpha|\\delta\s*<\s*\\alpha|\\delta\s*\\le\s*5/6|"
                      r"\\delta\s*\\le\s*\\frac56|\\delta\s*\\le\s*\\tfrac56|\\delta\s*\\leq\s*\\alpha")
    proof = range(15222, 15447)
    hits = [i for i in proof if ineq.search(lines[i - 1])]
    first = hits[0] if hits else None
    out["T3"] = (first == 15303, "lines in the Prop 19.2 proof with an inequality delta<=alpha (or "
                 "delta<=5/6): %s; first = %s (Review 2 says 15303)" % (hits, first))

    # T4: the derivation block 15248-15294 uses no bound on delta, Delta or kappa
    block = range(15248, 15295)
    forbidden = re.compile(r"\\Delta|\\kappa|1/24|\\frac1\{24\}|\\frac\{1\}\{24\}|5/6|\\frac56|"
                           r"\\tfrac56|\\frac\{5\}\{6\}|\\le\s*\\alpha|<\s*\\alpha|\\beta_\*|11/12")
    fb = [(i, lines[i - 1].strip()) for i in block if forbidden.search(lines[i - 1])]
    alpha_lines = [i for i in block if "\\alpha" in lines[i - 1]]
    ok4 = (not fb) and alpha_lines == [15289]
    out["T4"] = (ok4, "derivation 15248-15294: forbidden tokens %s; lines with \\alpha %s "
                 "(expected only 15289, the identity (1+5r)/6-delta r = 1-alpha+(alpha-delta)r)"
                 % (fb, alpha_lines))

    # T5: the proof lines before the derivation (15222-15247) use no bound either
    pre = list(range(15136, 15171)) + list(range(15222, 15248))
    fb5 = [(i, lines[i - 1].strip()) for i in pre if forbidden.search(lines[i - 1])
           or "\\alpha" in lines[i - 1]]
    out["T5"] = (not fb5, "the Sobolev paragraph 15136-15170 and proof lines 15222-15247 (subdivision, "
                 "marked/plain displays): forbidden tokens or alpha: %s" % fb5)

    # T6: Remark 19.3 is unlabeled and states the range 1/50 < delta <= 1 with no Delta, kappa
    rem = lines[15447:15467]
    has_label = any("\\label" in l for l in rem)
    has_dk = any(re.search(r"\\Delta|\\kappa", l) for l in rem)
    out["T6"] = ((not has_label) and (not has_dk),
                 "Remark 19.3 (15448-15467): \\label present=%s; Delta/kappa present=%s"
                 % (has_label, has_dk))

    # T7: the Prop 19.2 statement carries delta <= alpha as a hypothesis (15188) - context
    out["T7"] = ("0<\\delta=2a-1\\le\\alpha" in lines[15187],
                 "Prop 19.2 statement hypothesis at 15188 (a hypothesis, not a use in the proof)")

    # T8: the whole proof of Prop 19.2 (15222-15446) never states an upper bound on Delta or kappa
    ub = re.compile(r"1/24|\\frac1\{24\}|\\frac\{1\}\{24\}|\\Delta\s*\\le|\\kappa\s*\\le\s*(5/6|\\frac56|\\alpha)|11/12")
    hits8 = [(i, lines[i - 1].strip()) for i in proof if ub.search(lines[i - 1])]
    out["T8"] = (not hits8, "proof of Prop 19.2: lines with 1/24, Delta<=, kappa<=5/6 or 11/12: %s" % hits8)
    return out, lines


# ---------------------------------------------------------------- group A (P1F.0)
def algebra_p1f0():
    r, d, c, e0, R0, em, T, I = sp.symbols("r delta c eps0 R0 eps_m T I", real=True)
    alpha = R(5, 6)
    out = {}
    # A0: 12449/12375 -> 15272: with H = U^k, H/P = U^{1/6} H^{5/6}; k = max(1, (1+c)r) gives
    #     exponent max{1, (1+5(1+c)r)/6}  (the factor 2 in H = max(2U, .) is a constant)
    k = sp.symbols("k", real=True)
    hp = k - (k - 1) / 6
    a0 = (sp.simplify(hp - (R(1, 6) + 5 * k / 6)) == 0 and hp.subs(k, 1) == 1
          and sp.simplify(hp.subs(k, (1 + c) * r) - (1 + 5 * (1 + c) * r) / 6) == 0)
    out["A0"] = (a0, "H/P = H/(H/U)^{1/6}: exponent k-(k-1)/6 = 1/6+5k/6; k=1 gives 1, k=(1+c)r gives "
                 "(1+5(1+c)r)/6; 1/6+5k/6 is increasing in k, so the max commutes")
    # A1: case display at 15286-15292, branch r >= 1
    lhs = (1 + 5 * r) / 6 - d * r
    rhs = 1 - alpha + (alpha - d) * r
    out["A1"] = (sp.simplify(lhs - rhs) == 0, "(1+5r)/6 - delta r == 1-alpha+(alpha-delta)r "
                 "identically in delta (no sign of alpha-delta used)")
    # A2: e(r) = 1 exactly on [0,1]; the branches agree at r = 1
    agree = sp.simplify((1 + 5 * r) / 6 - 1 - 5 * (r - 1) / 6) == 0
    out["A2"] = (agree and ((1 + 5 * r) / 6).subs(r, 1) == 1,
                 "(1+5r)/6 - 1 = 5(r-1)/6, so e(r)=1 iff r<=1 and the two branches agree at r=1")
    # A3: amplified exponent bound (15272-15274) for 0<=r<=R0, c>=0, eps0>=0
    #     (1+5(1+c)r)/6 = (1+5r)/6 + 5cr/6 <= e(r) + 5cR0/6 ; 1 <= e(r) + 5cR0/6 ; (1+r)eps0 <= (1+R0)eps0
    s1 = sp.simplify((1 + 5 * (1 + c) * r) / 6 - ((1 + 5 * r) / 6 + 5 * c * r / 6))
    slack = sp.simplify(((1 + 5 * r) / 6 + 5 * c * R0 / 6) - (1 + 5 * (1 + c) * r) / 6)
    s3 = sp.simplify((1 + R0) * e0 - (1 + r) * e0)
    ok3 = (s1 == 0 and sp.simplify(slack - 5 * c * (R0 - r) / 6) == 0
           and sp.simplify(s3 - (R0 - r) * e0) == 0)
    # exact sweep of the max form
    sweep_bad = []
    for RR in [Fr(1, 2), Fr(1), Fr(3, 2), Fr(2)]:
        for cc in [Fr(0), Fr(1, 100), Fr(3, 10)]:
            for ee in [Fr(0), Fr(1, 50)]:
                for rr in frange(0, RR, 24):
                    left = max(Fr(1), (1 + 5 * (1 + cc) * rr) / 6) + (1 + rr) * ee
                    right = e_of(rr) + 5 * cc * RR / 6 + (1 + RR) * ee
                    if left > right:
                        sweep_bad.append((RR, cc, ee, rr))
    out["A3"] = (ok3 and not sweep_bad, "15272-15274: identity (1+5(1+c)r)/6=(1+5r)/6+5cr/6; slack "
                 "5c(R0-r)/6>=0 and (R0-r)eps0>=0; exact sweep 4x3x2x25 points, violations %d"
                 % len(sweep_bad))
    # A4: the choice c = 3 eps_m/(10 max{R0,1}), eps0 = eps_m/(4(1+R0)) gives extra terms <= eps_m/2
    ok4 = True
    det = []
    for case, M in (("R0>=1", R0), ("R0<1", sp.Integer(1))):
        cc = 3 * em / (10 * M)
        ee = em / (4 * (1 + R0))
        extra = sp.simplify(5 * cc * R0 / 6 + (1 + R0) * ee)
        target = sp.simplify(em / 4 * R0 / M + em / 4)
        ok4 &= sp.simplify(extra - target) == 0
        det.append("%s: extra = %s" % (case, sp.factor(extra)))
    # on R0>=1 extra = eps_m/2 exactly; on R0<1 extra = eps_m(R0+1)/4 < eps_m/2
    ok4 &= sp.simplify((5 * (3 * em / (10 * R0)) * R0 / 6 + (1 + R0) * em / (4 * (1 + R0))) - em / 2) == 0
    for R0v in [Fr(1, 3), Fr(1, 2), Fr(9, 10)]:
        ok4 &= (Fr(1, 4) * R0v + Fr(1, 4)) < Fr(1, 2)
    out["A4"] = (ok4, "15277-15280: with the paper's c, eps0 the two extra terms are eps_m/2 (R0>=1) "
                 "and eps_m(1+R0)/4 < eps_m/2 (R0<1); " + "; ".join(det))
    # A5: rowwise height factor 1+(3I+1)T <= (3I+2)(1+T) for T, I >= 0 (15265-15266)
    diff = sp.expand((3 * I + 2) * (1 + T) - (1 + (3 * I + 1) * T))
    out["A5"] = (sp.simplify(diff - (3 * I + 1 + T)) == 0,
                 "(3I+2)(1+T) - (1+(3I+1)T) = 3I+1+T >= 0")
    # A6: spike division bookkeeping with eps_m = eps and witness loss eps_w = eps/2
    eps = sp.symbols("eps", positive=True)
    count_exp = (sp.Symbol("e") + eps / 2) - (d * r - eps / 2)
    out["A6"] = (sp.simplify(count_exp - (sp.Symbol("e") - d * r + eps)) == 0,
                 "U^{e(r)+eps_m/2} / U^{delta r - eps_w} with eps_m=eps, eps_w=eps/2 gives "
                 "exponent e(r)-delta r+eps")
    # A7: the r-range: t <= 3/2 and r <= t + O(1/log U) fit in R0 = 2 (Lean uses R = 2)
    out["A7"] = (Fr(3, 2) < 2, "t<=3/2 so r <= 3/2 + o(1) < R0 = 2 for large U")
    return out


# ---------------------------------------------------------------- group B (P1F.1)
def algebra_p1f1():
    r, d, g, s = sp.symbols("r delta gamma s", real=True)
    out = {}
    e_hi = (1 + 5 * r) / 6
    # B1: r >= 1: e(r)-delta r-(1-delta) = (5/6-delta)(r-1), and <= 0 for delta >= 5/6, r >= 1
    ident = sp.simplify(e_hi - d * r - (1 - d) - (R(5, 6) - d) * (r - 1)) == 0
    mx, arg = vertex_max((R(5, 6) - d) * (r - 1), {d: [R(5, 6), 1], r: [1, 3]})
    out["B1"] = (ident and mx <= 0, "r>=1: identity e-delta r-(1-delta) = (5/6-delta)(r-1); vertex max "
                 "on delta in [5/6,1], r in [1,3] = %s at %s (sign argument covers all r>=1)" % (mx, arg))
    # B2: 1-gamma <= r < 1: 1-delta r-(1-delta) = delta(1-r) <= delta gamma <= gamma (needs delta <= 1)
    #     substitute r = 1 - s*gamma with s in [0,1]
    excess = (1 - d * (1 - s * g)) - (1 - d) - g
    mx2, arg2 = vertex_max(sp.expand(excess), {d: [R(5, 6), 1], s: [0, 1], g: [0, R(1, 10)]})
    ident2 = sp.simplify((1 - d * r) - (1 - d) - d * (1 - r)) == 0
    out["B2"] = (ident2 and mx2 <= 0, "r in [1-gamma,1): 1-delta r = 1-delta+delta(1-r); "
                 "max of delta(1-r)-gamma over the box = %s at %s" % (mx2, arg2))
    # B3: Prop 8.3 at t = 3/2: t - 1/2 = 1
    out["B3"] = (R(3, 2) - R(1, 2) == 1, "t - 1/2 = 1 at t = 3/2 (4529), so r >= 1 - c0 eps")
    # B4: Lean normalization: gamma = 76 eps (inverse_length_lower) + spike loss 2 eps = 78 eps
    out["B4"] = (76 + 2 == 78, "Lean: tstar-1/2-76eps <= r and spike loss 2eps give 1-delta+78eps+eps_m")
    # B5: Review 2 X3: at delta = 1, r = 1 - 76/1000 the excess is exactly 76/1000
    exc = (1 - Fr(1) * (1 - Fr(76, 1000))) - (1 - Fr(1))
    out["B5"] = (exc == Fr(76, 1000), "delta=1, r=1-76/1000: excess over 1-delta = %s" % exc)
    # B6: summing O((log U)^2) subdivisions costs U^{o(1)}: exponent bookkeeping only
    out["B6"] = (True, "the O_A((log U)^2) subdivisions add a factor <= U^{eps} for large U (no arithmetic)")
    return out


# ---------------------------------------------------------------- group C (P1F.2 and Lean identities)
def E_line1(a, d, Rr, q, h=R(13, 16), ly=R(23, 48), ell=R(1, 6)):
    delta = 2 * a - 1
    return (a - R(7, 8) + h * (R(17, 50) - R(1, 6)) - a * ly - (1 - a) * ell
            - (delta / 2 - q) * ell + d * (Rr + delta / 2 - R(17, 50)))


def E_line2(delta, d, Rr, q, h=R(13, 16), C0=R(-1, 48)):
    return C0 + R(2, 3) * delta + q / 6 - h * (1 - Rr) + (d - h) * (Rr + delta / 2 - R(17, 50))


def algebra_p1f2():
    d, D, q, lam, Dl, x, s, z, a, Rr = sp.symbols("d delta q lambda Delta x s zeta a R", real=True)
    h = R(13, 16)
    out = {}
    # C1: the two lines of eq:common-high-exponent agree with a = (1+delta)/2
    c1 = sp.simplify(E_line1((1 + D) / 2, d, Rr, q) - E_line2(D, d, Rr, q))
    out["C1"] = (c1 == 0, "15729-15734: line 1 == line 2 with a=(1+delta)/2, h=13/16, l_y=23/48, "
                 "ell=1/6, C0=-1/48 (difference %s)" % c1)
    # C2: with R = 1-delta+lambda, the exact identity of P1F.2
    Rl = 1 - D + lam
    target = (R(-1, 48) - D / 16 - Dl) + (q - D / 2) / 6 + R(13, 16) * lam + (d - h) * (R(33, 50) - D / 2 + lam)
    c2 = sp.simplify(E_line2(D, d, Rl, q) - Dl - target)
    out["C2"] = (c2 == 0, "E(d)-Delta = (-1/48-delta/16-Delta) + (q-delta/2)/6 + (13/16)lambda + "
                 "(d-h)(33/50-delta/2+lambda) (difference %s)" % c2)
    # C3: slope S(delta) = 33/50 - delta/2 on [5/6, 1]
    S = R(33, 50) - D / 2
    out["C3"] = (S.subs(D, 1) == R(4, 25) and S.subs(D, R(5, 6)) == R(73, 300),
                 "S(1) = %s, S(5/6) = %s; S decreasing, so S in [4/25, 73/300]" % (S.subs(D, 1), S.subs(D, R(5, 6))))
    # C4: bullet (i), d <= h: E(d)-Delta - (-1/48-delta/16-Delta+(13/16)lambda) <= 0
    #     q = x delta, x in [0,1/2]; d in [0,h]; lambda in [0, 527/300]
    expr_i = sp.expand(E_line2(D, d, Rl, x * D) - Dl - (R(-1, 48) - D / 16 - Dl + R(13, 16) * lam))
    mx, arg = vertex_max(expr_i, {D: [R(5, 6), 1], x: [0, R(1, 2)], d: [0, h], lam: [0, R(527, 300)]})
    out["C4"] = (mx <= 0, "bullet (i): max over delta in [5/6,1], x in [0,1/2], d in [0,h], "
                 "lambda in [0,527/300] = %s at %s" % (mx, arg))
    # C5: bullet (ii), d = h + s zeta: excess over (73/300+lambda) zeta is <= 0
    expr_ii = sp.expand(E_line2(D, h + s * z, Rl, x * D) - Dl
                        - (R(-1, 48) - D / 16 - Dl + R(13, 16) * lam) - (R(73, 300) + lam) * z)
    mx2, arg2 = vertex_max(expr_ii, {D: [R(5, 6), 1], x: [0, R(1, 2)], s: [0, 1], z: [0, R(1, 48)],
                                     lam: [0, R(527, 300)]})
    out["C5"] = (mx2 <= 0, "bullet (ii): E(d)-Delta <= bound + (73/300+lambda)zeta for d in [h,h+zeta]; "
                 "max excess = %s at %s" % (mx2, arg2))
    # C6: (73/300+lambda) zeta <= 2 zeta iff lambda <= 527/300 (zeta > 0); threshold exact
    thr = sp.solve(sp.Eq(R(73, 300) + lam, 2), lam)[0]
    mx3, _ = vertex_max((R(73, 300) + lam) * z - 2 * z, {lam: [0, R(527, 300)], z: [0, R(1, 48)]})
    out["C6"] = (thr == R(527, 300) and mx3 <= 0,
                 "threshold lambda = %s (Review 2 correction 1); max of (73/300+lambda)zeta-2zeta = %s" % (thr, mx3))
    # C7: corners of -1/48 - delta/16 - Delta
    corners = {(str(dv), str(Dv)): R(-1, 48) - dv / 16 - Dv for dv in (R(5, 6), R(1)) for Dv in (R(0), R(1, 8))}
    exp = {("5/6", "0"): R(-7, 96), ("1", "0"): R(-1, 12), ("5/6", "1/8"): R(-19, 96), ("1", "1/8"): R(-5, 24)}
    out["C7"] = (corners == exp, "corners %s" % {k: str(v) for k, v in corners.items()})
    # C8: dominance over the balanced margin: -1/48-delta/16-Delta <= -(51/64)Delta - 7/96
    mx4, arg4 = vertex_max(R(-1, 48) - D / 16 - Dl + R(51, 64) * Dl + R(7, 96), {D: [R(5, 6), 1], Dl: [0, R(1, 8)]})
    out["C8"] = (mx4 <= 0, "max of (-1/48-delta/16-Delta) - (-(51/64)Delta-7/96) = %s at %s" % (mx4, arg4))
    # C9: the paper's endpoint display 15944-15945: C0 + (3/4-h) delta == -1/48 - delta/16,
    #     and E(h) <= that with R = 1-delta, q <= delta/2
    c9a = sp.simplify(R(-1, 48) + (R(3, 4) - h) * D - (R(-1, 48) - D / 16)) == 0
    c9b = sp.simplify(E_line2(D, h, 1 - D, D / 2) - (R(-1, 48) + (R(3, 4) - h) * D)) == 0
    out["C9"] = (c9a and c9b, "15944-15945: C0+(3/4-h)delta = -1/48-delta/16; equality at q = delta/2")
    # C10: Lean CentralExponent: sourceExponent a d R q = 3/16 + relativeExponent (2a-1) d R q,
    #      relativeExponent == paper line 2; C(7/8) = 7/8 - 11/16 = 3/16
    src = (R(17, 48) * (R(1, 2) - R(17, 50)) + a + R(17, 50) - 1 - a * R(23, 48) - d * R(17, 50)
           + d * Rr + d * (a - R(1, 2)) + R(1, 6) * (R(17, 50) - R(1, 2) + q))
    rel = R(-1, 48) + R(2, 3) * (2 * a - 1) + q / 6 - R(13, 16) * (1 - Rr) + (d - R(13, 16)) * (Rr + (2 * a - 1) / 2 - R(17, 50))
    c10 = (sp.simplify(src - (R(3, 16) + rel)) == 0
           and sp.simplify(rel - E_line2(2 * a - 1, d, Rr, q)) == 0
           and sp.simplify(src - R(3, 16) - E_line1(a, d, Rr, q)) == 0
           and R(7, 8) - R(11, 16) == R(3, 16))
    out["C10"] = (c10, "Lean sourceExponent - 3/16 == relativeExponent == paper E(d) (both lines); "
                  "C(7/8) = 3/16")
    # C11: Lean high_mixed_margin side conditions: R = 1-delta+loss, 0<=loss<=1/32, delta in [5/6,1]
    #      give 0 <= R + delta/2 - 17/50 <= 2; and 1/32 <= 527/300
    slope = (1 - D + lam) + D / 2 - R(17, 50)
    lo, _ = vertex_max(-slope, {D: [R(5, 6), 1], lam: [0, R(1, 32)]})
    hi, _ = vertex_max(slope - 2, {D: [R(5, 6), 1], lam: [0, R(1, 32)]})
    out["C11"] = (lo <= 0 and hi <= 0 and R(1, 32) <= R(527, 300),
                  "Lean loss<=1/32: slope in [0,2] (max(-slope)=%s, max(slope-2)=%s); 1/32 <= 527/300" % (lo, hi))
    # C12: Lean high_source_margin's hshi with R = 1-delta+lambda is lambda <= 67/50 + delta/2,
    #      which is >= 527/300 on [5/6,1] (equality at delta = 5/6)
    lam_max = sp.solve(sp.Eq(slope, 2), lam)[0]
    mn, _ = vertex_max(-(lam_max - R(527, 300)), {D: [R(5, 6), 1]})
    out["C12"] = (sp.simplify(lam_max - (R(67, 50) + D / 2)) == 0 and mn <= 0 and lam_max.subs(D, R(5, 6)) == R(527, 300),
                  "Lean hshi <=> lambda <= %s; min over [5/6,1] minus 527/300 = %s (attained at delta=5/6)"
                  % (lam_max, -mn))
    # C13: Lean high_bin_endpoint: q<=delta/2, R<=1-delta+loss => -1/48+(2/3)delta+q/6-(13/16)(1-R)
    #      <= -1/48-delta/16+(13/16)loss ; the difference is affine with nonpositive coefficients
    qq, RR, loss = sp.symbols("qq RR loss", real=True)
    lhs = R(-1, 48) + R(2, 3) * D + qq / 6 - R(13, 16) * (1 - RR)
    rhs = R(-1, 48) - D / 16 + R(13, 16) * loss
    # substitute qq = delta/2 - u, RR = 1-delta+loss - w with u,w >= 0
    u, w = sp.symbols("u w", nonnegative=True)
    diff = sp.expand((lhs - rhs).subs({qq: D / 2 - u, RR: 1 - D + loss - w}))
    out["C13"] = (sp.simplify(diff - (-u / 6 - R(13, 16) * w)) == 0,
                  "Lean high_bin_endpoint: lhs-rhs = -u/6-(13/16)w <= 0 (u = delta/2-q, w = 1-delta+loss-R); %s" % diff)
    # C14: E is nondecreasing in R when d >= 0 (coefficient of R in line 1 is d)
    coef = sp.diff(E_line1((1 + D) / 2, d, Rr, q), Rr)
    out["C14"] = (sp.simplify(coef - d) == 0, "dE/dR = %s, so any R' <= 1-delta+lambda gives the same bound" % coef)
    return out


# ---------------------------------------------------------------- group G
def grids():
    out = {}
    bad1 = 0
    n1 = 0
    for dv in frange(Fr(5, 6), 1, 12):
        for gv in frange(0, Fr(1, 10), 5):
            for rv in frange(1 - gv, 3, 40):
                n1 += 1
                if e_of(rv) - dv * rv > 1 - dv + gv:
                    bad1 += 1
    out["G1"] = (bad1 == 0, "P1F.1: e(r)-delta r <= 1-delta+gamma at %d exact points "
                 "(delta in [5/6,1], gamma in [0,1/10], r in [1-gamma,3]); violations %d" % (n1, bad1))
    bad2 = 0
    n2 = 0
    h = Fr(13, 16)
    for dv in frange(Fr(5, 6), 1, 6):
        for xv in frange(0, Fr(1, 2), 4):
            for lv in [Fr(0), Fr(1, 32), Fr(1), Fr(527, 300)]:
                for Dv in [Fr(0), Fr(1, 24), Fr(1, 8)]:
                    for zv in [Fr(0), Fr(1, 96), Fr(1, 48)]:
                        for dd in frange(Fr(1, 100), h + zv, 20):
                            n2 += 1
                            Rv = 1 - dv + lv
                            E = (Fr(-1, 48) + Fr(2, 3) * dv + xv * dv / 6 - h * (1 - Rv)
                                 + (dd - h) * (Rv + dv / 2 - Fr(17, 50)))
                            bound = Fr(-1, 48) - dv / 16 - Dv + Fr(13, 16) * lv
                            extra = (Fr(73, 300) + lv) * zv if dd > h else Fr(0)
                            if E - Dv > bound + extra or extra > 2 * zv:
                                bad2 += 1
    out["G2"] = (bad2 == 0, "P1F.2: both bullets and the 2zeta cap at %d exact points; violations %d" % (n2, bad2))
    return out


# ---------------------------------------------------------------- group L
def lean_gates(root):
    out = {}
    base = os.path.join(root, LEAN_PREFIX)
    hash_bad, texts = [], {}
    for rel, want in LEAN_SHA256.items():
        p = os.path.join(base, rel)
        raw = open(p, "rb").read()
        if hashlib.sha256(raw).hexdigest() != want:
            hash_bad.append(rel)
        texts[rel] = raw.decode("utf-8").split("\n")
    out["L0"] = (not hash_bad, "%d/%d Lean files byte-identical to the git blobs at 31c706bb; mismatches %s"
                 % (len(LEAN_SHA256) - len(hash_bad), len(LEAN_SHA256), hash_bad))
    miss = [(f, ln, s) for f, ln, s in LEAN_ANCHORS if s not in texts[f][ln - 1]]
    out["L1"] = (not miss, "%d/%d declaration anchors at the cited file:line; misses %s"
                 % (len(LEAN_ANCHORS) - len(miss), len(LEAN_ANCHORS), miss[:3]))
    # L2: closure membership from import lines
    seen, stack = set(), [LEAN_ROOT_MODULE]
    while stack:
        m = stack.pop()
        if m in seen:
            continue
        seen.add(m)
        p = os.path.join(root, *m.split(".")) + ".lean"
        if not os.path.exists(p):
            continue
        for l in open(p, encoding="utf-8"):
            mm = re.match(r"\s*import\s+(\S+)", l)
            if mm and mm.group(1).startswith("OAI."):
                stack.append(mm.group(1))
    present = [m for m in seen if os.path.exists(os.path.join(root, *m.split(".")) + ".lean")]
    missing = sorted(set(seen) - set(present))
    cited = ["OAI.NumberTheory.DirichletL." + rel[:-5].replace("/", ".") for rel in LEAN_SHA256]
    outside = [m for m in cited if m not in seen]
    out["L2"] = (not outside and not missing,
                 "closure of %s has %d OAI modules (%d imported OAI modules missing on disk); cited "
                 "modules outside it: %s" % (LEAN_ROOT_MODULE, len(present), len(missing), outside))
    # L3: high_count_from_raw_moments uses only the inverse_raw field of Moments
    body = "\n".join(texts["Hecke/DetectorHighCount.lean"][26:47])
    fields = sorted(set(re.findall(r"moments\.(\w+)", body)))
    out["L3"] = (fields == ["inverse_raw"], "Moments fields used in the proof of high_count_from_raw_moments: %s" % fields)
    return out, texts


# ---------------------------------------------------------------- group F
def controls(paper_path, lean_texts):
    # FC1: delta < 5/6 in the r >= 1 branch of P1F.1
    v = e_of(Fr(3, 2)) - Fr(4, 5) * Fr(3, 2) - (1 - Fr(4, 5))
    control("FC1", v > 0, "delta=4/5, r=3/2: e(r)-delta r-(1-delta) = %s > 0 (delta >= 5/6 is load-bearing)" % v)
    # FC2: no t = 3/2 witness (t = 1 gives only r >= 1/2 - O(eps))
    v = e_of(Fr(1, 2)) - Fr(1) * Fr(1, 2) - (1 - Fr(1))
    control("FC2", v > 0, "t=1, r=1/2, delta=1: excess over 1-delta = %s (the t=3/2 witness is load-bearing)" % v)
    # FC3: delta > 1 in the r < 1 branch (Lean high_bin_count's hdelta' : delta <= 1)
    v = (1 - Fr(2) * Fr(9, 10)) - (1 - Fr(2)) - Fr(1, 10)
    control("FC3", v > 0, "delta=2, gamma=1/10, r=9/10: delta(1-r)-gamma = %s > 0 (delta <= 1 is where "
            "the r<1 branch absorbs delta*gamma into gamma)" % v)
    # FC4: lambda > 527/300 breaks the 2 zeta cap
    lam, z = Fr(527, 300) + Fr(1, 300), Fr(1, 96)
    v = (Fr(73, 300) + lam) * z - 2 * z
    control("FC4", v > 0, "lambda=528/300, delta=5/6, zeta=1/96: (73/300+lambda)zeta-2zeta = %s > 0" % v)
    # FC5: amplitude cap dropped (q = delta instead of q <= delta/2)
    dv = Fr(5, 6)
    E = Fr(-1, 48) + Fr(2, 3) * dv + dv / 6 - Fr(13, 16) * dv
    v = E - (Fr(-1, 48) - dv / 16)
    control("FC5", v > 0, "q=delta=5/6, R=1-delta, d=h: E(h) exceeds -1/48-delta/16 by %s (Lemma 19.1's cap is used)" % v)
    # FC6: intermediate paragraph (16146-16165) applied to a high bin
    dv = Fr(1)
    Rv = Fr(76, 75) - Fr(2, 3) * dv
    h = Fr(13, 16)
    E12 = Fr(-1, 48) + Fr(2, 3) * dv + dv / 12 - h * (1 - Rv) + (Fr(1, 2) - h) * (Rv + dv / 2 - Fr(17, 50))
    control("FC6", E12 > 0, "intermediate count R=76/75-2delta/3 at delta=1, d=1/2, q=delta/2: E(1/2) = %s > 0 "
            "(high bins must use P1F.1 at every d)" % E12)
    # FC7: Lemma 17.1 directly near r = 1 (fixed margin c1) fails; Lemma 17.6 is needed
    c1, rv = Fr(1, 100), 1 - Fr(1, 1000)
    control("FC7", not (rv <= 1 - c1), "Lemma 17.1 with m=1, z=0 needs r <= 1-c1; r=999/1000, c1=1/100 violates it "
            "(15293-15294: not an application of the strict marked moment)")
    # FC8: raw moment exponent max{1, r} in place of e(r) at delta = 5/6, r = 3/2
    v = max(Fr(1), Fr(3, 2)) - Fr(5, 6) * Fr(3, 2) - (1 - Fr(5, 6))
    control("FC8", v > 0, "unamplified exponent max{1,r}, delta=5/6, r=3/2: excess over 1-delta = %s > 0 "
            "(the exponent 1-delta in P1F.1 needs Lemma 17.6)" % v)
    # FC9: fixed witness deficit gamma = 1/8 (Review 2 NC3): positive margin at delta = 5/6
    dv, gv = Fr(5, 6), Fr(1, 8)
    v = Fr(-1, 48) - dv / 16 + Fr(13, 16) * dv * gv
    control("FC9", v == Fr(3, 256) and v > 0, "gamma=1/8 fixed, delta=5/6: E(h) = %s > 0 (O(eps) saturation of "
            "Prop 8.3 is load-bearing)" % v)
    # FC10: plant delta<=alpha inside the derivation block; T4 must fail
    planted, _ = text_gates(paper_path, planted={15270: r" with preliminary loss \(\epsilon_0\), using \(\delta\le\alpha\), has exponent"})
    control("FC10", not planted["T4"][0], "planted \\delta\\le\\alpha at line 15270: T4 fails")
    # FC11: plant an earlier delta<=alpha at 15240; T3 must fail (first use would move)
    planted, _ = text_gates(paper_path, planted={15245: r"moving conductor radical; here \(\delta\le\alpha\)."})
    control("FC11", not planted["T3"][0], "planted \\delta\\le\\alpha at line 15245: T3 fails (first use no longer 15303)")
    # FC14: plant an upper bound on Delta inside the proof; T8 must fail
    planted, _ = text_gates(paper_path, planted={15330: r"since here \(\Delta\le1/24\)."})
    control("FC14", not planted["T8"][0], "planted \\Delta\\le1/24 at line 15330: T8 fails")
    # FC12: wrong theorem number expectation (Remark 19.3 read as 19.4) is detected by T2's logic
    _, lines = text_gates(paper_path)
    cnt, sec = 0, 0
    num = None
    for i, l in enumerate(lines, 1):
        if l.startswith("\\section{"):
            sec, cnt = sec + 1, 0
        if re.match(r"\\begin\{(theorem|proposition|lemma|corollary|definition|remark)\}", l):
            cnt += 1
            if i == 15448:
                num = "%d.%d" % (sec, cnt)
    control("FC12", num != "19.4", "the remark at 15448 is numbered %s, so an expectation of 19.4 fails" % num)
    # FC13: Lean anchor control (only with --lean): demanding delta<=5/6 at high_bin_count fails
    if lean_texts is not None:
        line = lean_texts["Hecke/DetectorRowCountEndpoint.lean"][71]
        control("FC13", "(hδ : δ≤5/6)" not in line, "high_bin_count does not carry hδ : δ≤5/6 (it carries 5/6≤δ)")


# ---------------------------------------------------------------- main
def main(argv):
    t0 = time.time()
    if len(argv) < 2:
        print(__doc__)
        return 2
    paper = argv[1]
    lean_root = None
    json_out = None
    if "--lean" in argv:
        lean_root = argv[argv.index("--lean") + 1]
    if "--json" in argv:
        json_out = argv[argv.index("--json") + 1]

    tg, _ = text_gates(paper)
    for k, (ok, det) in tg.items():
        record(k, "T", ok, det)
    for grp, fn in (("A", algebra_p1f0), ("B", algebra_p1f1), ("C", algebra_p1f2), ("G", grids)):
        for k, (ok, det) in fn().items():
            record(k, grp, ok, det)
    lean_texts = None
    if lean_root:
        lg, lean_texts = lean_gates(lean_root)
        for k, (ok, det) in lg.items():
            record(k, "L", ok, det)
    controls(paper, lean_texts)

    gates = [x for x in RESULTS if x["kind"] == "gate"]
    ctrls = [x for x in RESULTS if x["kind"] == "control"]
    for x in RESULTS:
        tag = ("PASS" if x["ok"] else "FAIL") if x["kind"] == "gate" else ("FIRES" if x["ok"] else "SILENT")
        print("%-5s %-6s %s" % (x["id"], tag, x["detail"]))
    ng, nc = sum(x["ok"] for x in gates), sum(x["ok"] for x in ctrls)
    print("SUMMARY gates %d/%d pass; failing controls %d/%d fire; lean group %s; %.1f s"
          % (ng, len(gates), nc, len(ctrls), "run" if lean_root else "skipped", time.time() - t0))
    if json_out:
        with open(json_out, "w") as f:
            json.dump({"paper_sha256": PAPER_SHA256, "lean_group": bool(lean_root), "results": RESULTS,
                       "gates_pass": ng, "gates_total": len(gates), "controls_fire": nc,
                       "controls_total": len(ctrls)}, f, indent=1, sort_keys=True)
    return 0 if ng == len(gates) and nc == len(ctrls) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
