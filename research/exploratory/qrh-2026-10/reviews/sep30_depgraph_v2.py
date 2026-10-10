#!/usr/bin/env python3
"""Verification-status map v2 of the 30 Sep 2026 OpenAI 7/8 manuscript (dependency graph + statuses).

Status: EXPLORATORY bookkeeping tool (lexical extraction plus a hand-entered status table; not a
        proof checker and not a review). See SEP30_VERIFICATION_MAP_V2.md.
Input : paper.tex (sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3), e.g.
        `git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > paper.tex`
Run   : python3 -I sep30_depgraph_v2.py paper.tex [out.json [node_table.md]]

The graph logic is copied unchanged from sep30_depgraph.py (v1, sha256 ac667abf...e459), with
two changes, both taken from reviews/PART1_SUBSTITUTION.md:
  * a manual verbal edge Lemma 5.7 -> Def 5.6 (Lemma 5.7's statement is phrased in Def 5.6's
    terms; v1 missed it), so Def 5.6 is no longer "via 3.1";
  * a second graph in which Thm 3.1 and the eight Part-I-only nodes are deleted and the
    bootstrap prose S12.0 cites the external node "O5" ([O5] thm:main) instead of Thm 3.1.
STATUS below is entered by hand from the review files named in EVIDENCE; the script only
counts, ranks and sums lines. Changing a status needs a review, not an edit here.
"""
import collections
import hashlib
import json
import math
import re
import sys

EXPECTED = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
ENVS = ("theorem", "proposition", "lemma", "corollary", "definition", "remark")
SPECIAL_PROSE = {(12580, 14984): "18.1", (16454, 16463): "1.1"}
MANUAL = {  # stated in words in the source, without \ref
    "20.3": {"S20.4", "S20.5", "15.3"},  # v1
    "S20.4": {"20.2"},                   # v1
    "1.1": {"S12.0"},                    # v1
    "5.7": {"5.6"},                      # v2: PART1_SUBSTITUTION.md Sec. 3.2
}
# Leave the 7/8 path when [O5] thm:main replaces Thm 3.1 (PART1_SUBSTITUTION.md Sec. 6).
SUBSTITUTED = {"3.1", "5.8", "6.1", "6.2", "6.3", "9.1", "9.2", "11.2"}

# Status codes: R (whole-node bounded-review verdict), Rp (bounded-review verdicts on parts of
# the node, named parts only read or numerically checked, or the reviewer declined a
# whole-node verdict), I, A, U as in v1.  Values: (v1 code, v2 code).
STATUS = {
    "1.1": ("I", "I"), "2.1": ("I", "I"), "3.1": ("A", "A"),
    "4.1": ("U", "R"), "4.2": ("A", "A"), "4.3": ("A", "A"), "4.4": ("A", "A"),
    "4.5": ("U", "R"), "4.6": ("U", "R"), "4.7": ("U", "R"), "4.8": ("U", "R"),
    "4.9": ("U", "R"), "4.10": ("U", "R"),
    "5.1": ("U", "R"), "5.2": ("U", "R"), "5.3": ("U", "R"), "5.4": ("U", "R"),
    "5.5": ("U", "R"), "5.6": ("U", "I"), "5.7": ("U", "R"), "5.8": ("U", "U"),
    "6.1": ("U", "U"), "6.2": ("U", "U"), "6.3": ("A", "A"),
    "7.1": ("R", "Rp"),
    "8.1": ("U", "R"), "8.2": ("U", "R"), "8.3": ("U", "R"),
    "9.1": ("U", "U"), "9.2": ("U", "U"),
    "10.1": ("R", "R"), "10.2": ("R", "R"), "10.3": ("R", "R"), "10.4": ("R", "R"),
    "10.5": ("R", "R"), "10.6": ("R", "R"),
    "11.1": ("U", "R"), "11.2": ("A", "A"), "11.3": ("I", "I"),
    "13.1": ("U", "R"), "13.2": ("A", "R"), "13.3": ("U", "R"), "13.4": ("U", "R"),
    "14.1": ("U", "R"), "14.2": ("U", "R"), "14.3": ("A", "R"),
    "15.1": ("R", "Rp"), "15.2": ("U", "R"), "15.3": ("A", "R"),
    "16.1": ("I", "R"), "16.2": ("R", "R"),
    "17.1": ("U", "A"), "17.2": ("U", "Rp"), "17.3": ("U", "R"), "17.4": ("U", "R"),
    "17.5": ("U", "R"), "17.6": ("U", "R"),
    "18.1": ("R", "R"), "18.2": ("I", "R"), "18.3": ("I", "R"),
    "19.1": ("U", "R"), "19.2": ("A", "Rp"),
    "20.1": ("I", "I"), "20.2": ("R", "R"), "20.3": ("I", "Rp"),
}
# Verdicts taken from SEP30_SEC4_REVIEW.md, whose committed text still has output placeholders
# (its full run log in the session scratchpad ends "ALL PASS"). Counted as R; the script also
# reports the counts with these three reverted to U.
PROVISIONAL = {"4.1", "4.6", "13.1"}
# Evidence per node (file names are in reviews/ unless prefixed). Abbreviations:
# DIFF = SEP30_REFLECTION_DIFF, LOW = SEP30_LOWSIDE_REVIEW, INV = SEP30_INVMOMENT_REVIEW,
# EQC = SEP30_EQC_CHECK, L17 = SEP30_L17_IDENTITIES, L18a/b/c = LEMMA18_1_REVIEW /
# LEMMA18_1_COMMON_SUPPORT / LEMMA18_1_CASE2_SEC188, JUNC = SEP30_JUNCTION_CHECK,
# DET = SEP30_DETECTOR_QUANTIFIERS, L13 = SEP30_L13_L45_REVIEW, SEC4 = SEP30_SEC4_REVIEW,
# SUB = PART1_SUBSTITUTION, CONT = CONTOUR_LEMMAS_BELOW_7_8, P910 = PR910_REPLAY,
# C74 = numerics/COEFF74_CHECK, MAP1 = SEP30_VERIFICATION_MAP (v1 evidence carried over).
EVIDENCE = {
    "1.1": "MAP1 (PR 908 audit §3.1, inspection). Final paragraph 16454-16463 not line-checked.",
    "2.1": "MAP1 (PR 908 §3.1). DET §6.1 uses its pretarget requirement only. Proof not line-checked.",
    "3.1": "MAP1 ledger only. Leaves with the substitution (SUB §3.1).",
    "4.1": "SEC4 §1: no wrong step; A1-A4 exact (conductors, S-family).",
    "4.2": "MAP1 numerics (w5copg, PR 908). Proof unreviewed.",
    "4.3": "MAP1 numerics K1/K2''. C74 uses the four-term Gamma (agrees 1.4e-14). Proof unreviewed.",
    "4.4": "MAP1 numerics K2',K3,K4; L13 A5; L18b B4. Proof unreviewed.",
    "4.5": "L13: no wrong step (line by line).",
    "4.6": "SEC4 §2: no wrong step; B1-B4.",
    "4.7": "L13 (as used) + SEC4 §3: no wrong step.",
    "4.8": "SEC4 §4: no wrong step (constant C ~ 0.69); L13 as used.",
    "4.9": "SEC4 §5 + L13: no wrong step (constants ineffective, harmless).",
    "4.10": "SEC4 §6 + L13: no wrong step.",
    "5.1": "DIFF: arithmetic core = R3-reviewed Oct 5 appendix proof; remainder R-a..R-g; PL/contour by reading.",
    "5.2": "DIFF §4.2: no error.",
    "5.3": "DIFF §4.3: no error.",
    "5.4": "DIFF §4.3: no error.",
    "5.5": "DIFF §3.2 (new vs Oct 5), check Q: no error.",
    "5.6": "Definition; read in DIFF scope. Direct via Lemma 5.7 (SUB §3.2).",
    "5.7": "DIFF §3.3, check U: no error.",
    "5.8": "Unreviewed. Leaves with the substitution.",
    "6.1": "Unreviewed. Leaves with the substitution.",
    "6.2": "Unreviewed. Leaves with the substitution.",
    "6.3": "MAP1 ledger only. Leaves with the substitution.",
    "7.1": "MAP1 numerics L1-L5, CONT tables; DET region one; C74 (7.4)->(7.10) on 166,144 tuples (FLOAT). (7.5) analytic not checked.",
    "8.1": "DET §1: no gap found.",
    "8.2": "DET §2: no gap found.",
    "8.3": "DET §3: no gap found.",
    "9.1": "Unreviewed. Leaves with the substitution.",
    "9.2": "Unreviewed. Leaves with the substitution.",
    "10.1": "CONT: no gap.",
    "10.2": "CONT: no gap.",
    "10.3": "CONT: no gap.",
    "10.4": "CONT + P910: no gap.",
    "10.5": "CONT: no gap.",
    "10.6": "CONT: no gap.",
    "11.1": "SUB §4: no wrong step.",
    "11.2": "MAP1 ledger only. Leaves with the substitution.",
    "11.3": "MAP1 (PR 908 §2.4 read).",
    "13.1": "SEC4 §7: no wrong step; G0-G1 EMPIRICAL.",
    "13.2": "L13 §3: correct; D2 exact.",
    "13.3": "L13 §1: no wrong step (A, B exact); LOW brute force.",
    "13.4": "L13 §2: no wrong step (C1 exact).",
    "14.1": "LOW: no wrong step, given Prop 5.1 branch compatibility (DIFF R-e).",
    "14.2": "LOW: no wrong step.",
    "14.3": "LOW: no wrong step.",
    "15.1": "PR 910 REVIEW §1.1 + P910 + LOW (exponents). Analytic transfer not re-proved.",
    "15.2": "LOW: no wrong step.",
    "15.3": "LOW: no wrong step; zero excess at d = 0.",
    "16.1": "DET §5: no gap; geometry-free. Ray presentation rests on Lemma 4.4.",
    "16.2": "CONT + P910.",
    "17.1": "INV: statement diff + initialization ledger PASS. Initialization transform not replayed (L17).",
    "17.2": "INV ledgers, EQC eq. (C), L17 identities 1-10. Fourier separations (10538, 11209, 11247) read only.",
    "17.3": "L17 §1.2: correct.",
    "17.4": "L17 §1.2: correct.",
    "17.5": "L17 §1.2: correct.",
    "17.6": "L17 §1.2: correct (given Lemma 4.5).",
    "18.1": "L18a + L18b + L18c: every proof line read, no wrong step.",
    "18.2": "Inside L18 coverage (coefficient lemma; L18c §6).",
    "18.3": "Inside L18 coverage (Theta rows, lattice cancellation; L18c §6).",
    "19.1": "SUB §5: no wrong step; JUNC hypothesis instance.",
    "19.2": "JUNC (84 exact gates) + L18c §4 interface. Qualitative row-dependent-test clause in prose only.",
    "20.1": "CONT read; DET §5 consumption exact; P910; ledger.",
    "20.2": "Certified: PR 908, P910, JUNC E8-E9.",
    "20.3": "DET §6: order admissible. I2, I10, I12 rest on proofs outside its scope.",
}
# Risk rubric of v1 Sec. 6: length (from owned lines) + novelty (1-3) + numerology slack (1-3).
# Only novelty and slack are entered by hand; nodes not listed are not ranked.
NOVELTY_SLACK = {
    "4.1": (2, 1), "4.2": (1, 1), "4.3": (2, 1), "4.4": (2, 1), "4.6": (1, 1), "13.1": (1, 1),
    "17.1": (3, 2),
    "3.1": (2, 2), "5.8": (2, 2), "6.1": (1, 1), "6.2": (2, 1), "6.3": (2, 2), "9.1": (2, 1),
    "9.2": (3, 2), "11.2": (2, 2),
    # residual (I / Rp) nodes, ranked separately
    "1.1": (1, 1), "2.1": (2, 1), "5.6": (2, 1), "11.3": (1, 1), "20.1": (2, 2),
    "7.1": (2, 1), "15.1": (2, 3), "17.2": (3, 2), "19.2": (3, 3), "20.3": (2, 2),
}


def length_score(n):
    return 1 if n < 150 else (2 if n <= 500 else 3)


def parse(path):
    raw = open(path, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    lines = raw.decode("utf-8").split("\n")
    n = len(lines)
    sec = sub = cnt = 0
    owner = [None] * (n + 2)
    envs = []
    cur = None
    for i, line in enumerate(lines, 1):
        if re.match(r"\s*\\section\{", line):
            sec += 1; sub = 0; cnt = 0
        if re.match(r"\s*\\subsection\{", line):
            sub += 1
        owner[i] = f"S{sec}.{sub}"
        m = re.match(r"\s*\\begin\{(" + "|".join(ENVS) + r")\}(\[[^\]]*\])?", line)
        if m:
            cnt += 1
            cur = dict(num=f"{sec}.{cnt}", kind=m.group(1), title=(m.group(2) or "").strip("[]"),
                       start=i, end=None, labels=[], proofs=[])
            envs.append(cur)
        if cur and cur["end"] is None:
            cur["labels"] += re.findall(r"\\label\{([^}]*)\}", line)
            if re.match(r"\s*\\end\{" + cur["kind"] + r"\}", line):
                cur["end"] = i
    lab2env = {lab: e["num"] for e in envs for lab in e["labels"]}
    for (a, b), o in SPECIAL_PROSE.items():
        for i in range(a, b + 1):
            owner[i] = o
    for e in envs:
        for i in range(e["start"], e["end"] + 1):
            owner[i] = e["num"]
    i = 1
    while i <= n:
        if re.match(r"\s*\\begin\{proof\}", lines[i - 1]):
            j, depth = i, 0
            while True:
                depth += len(re.findall(r"\\begin\{proof\}", lines[j - 1]))
                depth -= len(re.findall(r"\\end\{proof\}", lines[j - 1]))
                if depth == 0:
                    break
                j += 1
            m = re.search(r"Proof of [A-Za-z]+~?\\ref\{([^}]*)\}", lines[i - 1])
            o = lab2env[m.group(1)] if m else [e for e in envs if e["end"] < i][-1]["num"]
            next(e for e in envs if e["num"] == o)["proofs"].append((i, j))
            for k in range(i, j + 1):
                owner[k] = o
            i = j + 1
        else:
            i += 1
    lab_owner = {}
    for i, line in enumerate(lines, 1):
        for lab in re.findall(r"\\label\{([^}]*)\}", line):
            lab_owner[lab] = lab2env.get(lab, owner[i])
    deps = collections.defaultdict(set)
    size = collections.Counter()
    for i, line in enumerate(lines, 1):
        o = owner[i]
        size[o] += 1
        for r in re.findall(r"\\(?:eq)?ref\{([^}]*)\}", line):
            t = lab_owner.get(r)
            if t and t != o:
                deps[o].add(t)
    for k, v in MANUAL.items():
        deps[k] |= v
    return digest, n, envs, deps, size


def closure(root, g):
    seen, st = set(), [root]
    while st:
        x = st.pop()
        if x not in seen:
            seen.add(x)
            st.extend(g.get(x, ()))
    return seen


def reverse(g):
    rev = collections.defaultdict(set)
    for a, bs in g.items():
        for b in bs:
            rev[b].add(a)
    return rev


def ndeps(nums, deps):
    c = closure("1.1", deps)
    rev = reverse(deps)
    return c, {x: len({y for y in closure(x, rev) - {x} if y in nums and y in c}) for x in nums if x in c}


def main(path, out=None, md=None):
    digest, n, envs, deps, size = parse(path)
    nums = {e["num"] for e in envs}
    c78, nd = ndeps(nums, deps)
    lb = sorted((x for x in nums if x in c78), key=lambda s: tuple(map(int, s.split("."))))
    # substitution graph: delete the eight nodes, S12.0 cites O5 instead of 3.1
    sdeps = collections.defaultdict(set)
    for a, bs in deps.items():
        if a in SUBSTITUTED:
            continue
        sdeps[a] = {b for b in bs if b not in SUBSTITUTED}
    sdeps["S12.0"].add("O5")
    c78s, nds = ndeps(nums - SUBSTITUTED, sdeps)
    lbs = [x for x in lb if x in c78s]
    assert set(STATUS) == set(lb), sorted(set(STATUS) ^ set(lb))
    assert set(EVIDENCE) == set(STATUS), sorted(set(EVIDENCE) ^ set(STATUS))
    assert PROVISIONAL <= {x for x in STATUS if STATUS[x][1] == "R"}
    dropped = sorted(set(lb) - set(lbs) - SUBSTITUTED)
    print(f"sha256 ok: {digest == EXPECTED}  lines: {n}  environments: {len(envs)}")
    print(f"load-bearing as written: {len(lb)}; with O5 substitution: {len(lbs)}; "
          f"unexpectedly dropped: {dropped}")
    via31 = {x for x in lb if x in SUBSTITUTED}

    def count(nodes, which):
        c = collections.Counter(STATUS[x][which] for x in nodes)
        return {k: c.get(k, 0) for k in ("R", "Rp", "I", "A", "U")}

    res = dict(sha256=digest, sha256_ok=digest == EXPECTED, lines=n)
    res["counts_v1_codes"] = count(lb, 0)
    res["counts_v2_as_written"] = count(lb, 1)
    res["counts_v2_as_written_direct"] = count([x for x in lb if x not in via31], 1)
    res["counts_v2_as_written_via31"] = count(via31, 1)
    res["counts_v2_with_O5"] = count(lbs, 1)
    def count_without_provisional(nodes):
        c = count(nodes, 1)
        k = len(PROVISIONAL & set(nodes))
        c["R"] -= k; c["U"] += k
        return c
    res["counts_v2_as_written_wo_provisional"] = count_without_provisional(lb)
    res["counts_v2_with_O5_wo_provisional"] = count_without_provisional(lbs)
    for k in ("counts_v1_codes", "counts_v2_as_written", "counts_v2_as_written_direct",
              "counts_v2_as_written_via31", "counts_v2_with_O5",
              "counts_v2_as_written_wo_provisional", "counts_v2_with_O5_wo_provisional"):
        print(f"{k:30} {res[k]}  total={sum(res[k].values())}")
    # owned lines by status
    def lines_by(nodes):
        c = collections.Counter()
        for x in nodes:
            c[STATUS[x][1]] += size[x]
        return dict(c), sum(c.values())
    res["lines_as_written"], tot = lines_by(lb)
    res["lines_with_O5"], tots = lines_by(lbs)
    for name, (d, t) in (("as written", (res["lines_as_written"], tot)),
                         ("with O5", (res["lines_with_O5"], tots))):
        r = d.get("R", 0); rp = d.get("Rp", 0)
        print(f"owned lines {name}: total {t}; R {r} ({100*r/t:.1f}%), R+Rp {r+rp} "
              f"({100*(r+rp)/t:.1f}%), by code {d}")
    # rankings
    def rank(nodes, ndmap):
        rows = []
        for x in nodes:
            if x not in NOVELTY_SLACK:
                continue
            nv, sl = NOVELTY_SLACK[x]
            L = length_score(size[x])
            score = (L + nv + sl) * math.sqrt(1 + ndmap[x])
            rows.append(dict(node=x, status=STATUS[x][1], L=L, N=nv, S=sl, ndep=ndmap[x],
                             owned_lines=size[x], score=round(score, 1)))
        return sorted(rows, key=lambda r: -r["score"])
    au = [x for x in lb if STATUS[x][1] in ("A", "U")]
    res["rank_AU_as_written"] = rank(au, nd)
    res["rank_AU_with_O5"] = rank([x for x in au if x in c78s], nds)
    res["rank_residual_with_O5"] = rank([x for x in lbs if STATUS[x][1] in ("I", "Rp")], nds)
    for k in ("rank_AU_with_O5", "rank_AU_as_written", "rank_residual_with_O5"):
        print(k)
        for r in res[k]:
            print(f"  {r['node']:5} {r['status']:2} L+N+S={r['L']}+{r['N']}+{r['S']} "
                  f"ndep={r['ndep']:2} lines={r['owned_lines']:4} score={r['score']}")
    env = {e["num"]: e for e in envs}
    res["nodes"] = [dict(num=x, kind=env[x]["kind"], title=env[x]["title"],
                         statement=[env[x]["start"], env[x]["end"]], proofs=env[x]["proofs"],
                         v1=STATUS[x][0], v2=STATUS[x][1], owned_lines=size[x],
                         ndep_as_written=nd[x], ndep_with_O5=nds.get(x),
                         leaves_with_O5=x in SUBSTITUTED, evidence=EVIDENCE[x]) for x in lb]
    print("node v1 v2 lines ndep ndep_O5")
    for r in res["nodes"]:
        print(f"  {r['num']:5} {r['v1']:2} {r['v2']:2} {r['owned_lines']:5} {r['ndep_as_written']:3} "
              f"{'-' if r['ndep_with_O5'] is None else r['ndep_with_O5']}")
    if out:
        json.dump(res, open(out, "w"), indent=1)
    if md:
        abbrev = {"theorem": "Thm", "proposition": "Prop", "lemma": "Lem", "corollary": "Cor",
                  "definition": "Def", "remark": "Rem"}
        rows = ["| Node | Title | TeX (statement; proof) | own lines | ndep (as written / O5) "
                "| v1 | v2 as written | v2 with O5 | Evidence |",
                "|---|---|---|---:|---|---|---|---|---|"]
        for r in res["nodes"]:
            pf = ", ".join(f"{a}-{b}" for a, b in r["proofs"]) or (
                "no proof (definition)" if r["kind"] == "definition" else "prose")
            if r["num"] == "18.1":
                pf = "12580-14984 (prose)"
            v2 = "Rp" if r["v2"] == "Rp" else r["v2"]
            v2o = "**L**" if r["leaves_with_O5"] else v2
            nd_o = "-" if r["ndep_with_O5"] is None else r["ndep_with_O5"]
            title = r["title"] or {"1.1": "Main theorem (7/8)"}.get(r["num"], "")
            pf = "16454-16463 (prose)" if r["num"] == "1.1" else pf
            rows.append(f"| {abbrev[r['kind']]} {r['num']} | {title} | "
                        f"{r['statement'][0]}-{r['statement'][1]}; {pf} | {r['owned_lines']} | "
                        f"{r['ndep_as_written']} / {nd_o} | {r['v1']} | {v2} | {v2o} | "
                        f"{r['evidence']} |")
        open(md, "w").write("\n".join(rows) + "\n")
    return 0 if res["sha256_ok"] and not dropped else 1


if __name__ == "__main__":
    a = sys.argv[1:]
    sys.exit(main(a[0], a[1] if len(a) > 1 else None, a[2] if len(a) > 2 else None))
