#!/usr/bin/env python3
"""Reference-level dependency graph of the 30 Sep 2026 OpenAI 7/8 manuscript.

Status: EXPLORATORY tool (lexical extraction; not a proof checker).
Input : paper.tex (sha256 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3),
        e.g. `git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/
        The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > paper.tex`
Run   : python3 -I sep30_depgraph.py paper.tex [out.json]

Method (see SEP30_VERIFICATION_MAP.md, Section 1):
  * numbers theorem-like environments as LaTeX does (shared counter per \\section);
  * every source line gets an owner: the environment, its proof (the next proof block, or an
    explicit "Proof of \\ref{X}"), the prose proof of Lemma 18.1 (12580-14984) and of Thm 1.1
    (16454-16463), or else the enclosing subsection's prose node "S<sec>.<subsec>";
  * an edge A -> B means a line owned by A contains \\ref/\\eqref to a label owned by B;
  * MANUAL edges add dependencies that the text states in words without \\ref.
It is a "mentions" graph: an edge is a citation, not a verified logical use.
"""
import collections
import hashlib
import json
import re
import sys

EXPECTED = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
ENVS = ("theorem", "proposition", "lemma", "corollary", "definition", "remark")
SPECIAL_PROSE = {(12580, 14984): "18.1", (16454, 16463): "1.1"}
MANUAL = {  # stated in words in the source, without \ref
    "20.3": {"S20.4", "S20.5", "15.3"},  # "The endpoint inequality" (16346); low estimate (15505)
    "S20.4": {"20.2"},                   # Lemma 20.2 sits inside the endpoint-inequality prose
    "1.1": {"S12.0"},                    # final paragraph uses the Part II bootstrap (6810-6826)
}
PART_I_ONLY = {"3.1", "5.6", "5.8", "6.1", "6.2", "6.3", "9.1", "9.2", "11.2"}


def main(path, out=None):
    raw = open(path, "rb").read()
    digest = hashlib.sha256(raw).hexdigest()
    lines = raw.decode("utf-8").split("\n")
    n = len(lines)
    sec = sub = cnt = 0
    owner = [None] * (n + 2)
    envs, labels_of = [], {}
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
    rev = collections.defaultdict(set)
    for a, bs in deps.items():
        for b in bs:
            rev[b].add(a)

    def closure(root, g):
        seen, st = set(), [root]
        while st:
            x = st.pop()
            if x not in seen:
                seen.add(x)
                st.extend(g.get(x, ()))
        return seen

    c78, c1112 = closure("1.1", deps), closure("3.1", deps)
    nodes = []
    for e in envs:
        num = e["num"]
        anc = {x for x in closure(num, rev) - {num} if not x.startswith("S") and x in c78}
        lb = "no" if num not in c78 else ("part-I-only" if num in PART_I_ONLY else "direct")
        nodes.append(dict(num=num, kind=e["kind"], title=e["title"], statement=[e["start"], e["end"]],
                          proofs=e["proofs"], owned_lines=size[num], load_bearing=lb,
                          in_11_12_closure=num in c1112, transitive_dependents=len(anc),
                          deps=sorted(deps.get(num, ()))))
    res = dict(sha256=digest, sha256_ok=digest == EXPECTED, lines=n, nodes=nodes,
               prose_in_closure={p: sorted(deps.get(p, ())) for p in sorted(c78) if p.startswith("S")})
    if out:
        json.dump(res, open(out, "w"), indent=1)
    print(f"sha256 ok: {res['sha256_ok']}  lines: {n}  environments: {len(nodes)}")
    print("load-bearing:", collections.Counter(x["load_bearing"] for x in nodes))
    for x in nodes:
        print(f"{x['kind'][:5]:5} {x['num']:6} {x['statement']} proofs={x['proofs']} "
              f"lb={x['load_bearing']:11} ndep={x['transitive_dependents']:3} deps={','.join(x['deps'])}")
    return 0 if res["sha256_ok"] else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
