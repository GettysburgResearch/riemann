#!/usr/bin/env python3
"""Lexical checks for PART1_SUBSTITUTION.md (stdlib only; run with `python3 -I`).

Usage:
  python3 -I part1_substitution_check.py SEP30_TEX OCT5_TEX

The two inputs are paper.tex (Sep 30) and paper2.tex (Oct 5) as stored at
pr908 = 31c706bbb3dce49a7ebabbe71cd7cbacdaa6cbb6.  Extract them with
  git show pr908:standalone/2026-10-07-openai-quasi-riemann-import/upstream/preprints/\
The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex > sep30.tex
  git show pr908:.../The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex > oct5.tex

What this authenticates: only text-level facts (hashes, which labels are cited
where, which lines carry the bootstrap constants).  It does not check any
mathematics.  A verbal use without \\ref is found only by the explicit phrase
searches listed below.
"""
import hashlib
import re
import sys

SEP30_SHA = "42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3"
OCT5_SHA = "d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d"
PART2_START = 6806  # \part{The seven-eighths zero-free half-plane} is at 6807

# Line spans (statement and proof) of the nine nodes tagged "via 3.1" in
# SEP30_VERIFICATION_MAP.md Sec. 4.
VIA31 = {
    "Thm 3.1": [(532, 537), (6783, 6805)],
    "Def 5.6": [(2888, 2950)],
    "Lem 5.8": [(3138, 3285)],
    "Lem 6.1": [(3497, 3580)],
    "Lem 6.2": [(3587, 3666)],
    "Prop 6.3": [(3672, 3721)],
    "Lem 9.1": [(4707, 5171)],
    "Prop 9.2": [(5181, 5446)],
    "Prop 11.2": [(6582, 6698)],
}
# Part-I-only prose blocks that also leave if Thm 3.1 is replaced.
PROSE_P1 = {
    "Sec 6.2 prose": (3486, 3496),
    "Sec 10.5 'Applying the row envelope'": (5905, 6012),
    "Sec 11 margin table": (6493, 6512),
}

failures = []


def check(cond, msg):
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        failures.append(msg)


def load(path, sha):
    data = open(path, "rb").read()
    h = hashlib.sha256(data).hexdigest()
    check(h == sha, f"sha256({path}) = {h[:16]}... expected {sha[:16]}...")
    return data.decode("utf-8").split("\n")


def labels(lines):
    out = {}
    for i, l in enumerate(lines, 1):
        for m in re.finditer(r"\\label\{([^}]*)\}", l):
            out[m.group(1)] = i
    return out


def main():
    sep, oct5 = sys.argv[1], sys.argv[2]
    S = load(sep, SEP30_SHA)
    O = load(oct5, OCT5_SHA)
    lab = labels(S)

    # 1. Part II citations into the via-3.1 spans and the Part-I-only prose.
    hits = {}
    for i, l in enumerate(S, 1):
        if i < PART2_START:
            continue
        for m in re.finditer(r"(?:eq)?ref\{([^}]*)\}", l):
            L = lab.get(m.group(1))
            if L is None:
                continue
            for name, spans in list(VIA31.items()) + [(k, [v]) for k, v in PROSE_P1.items()]:
                if any(a <= L <= b for a, b in spans):
                    hits.setdefault(name, []).append((i, m.group(1)))
    print("Part II \\ref/\\eqref into via-3.1 spans or Part-I-only prose:", hits)
    check(hits == {"Thm 3.1": [(6812, "thm:eleven-twelfths")]},
          "the only Part II citation of the cluster is thm:eleven-twelfths at 6812")

    # 2. Verbal edge Def 5.6 -> Lemma 5.7 -> Lemma 14.3 (missed by sep30_depgraph.py).
    check("For an unmarked reflected block" in S[2958 - 1],
          "Lemma 5.7 statement (2958) opens 'For an unmarked reflected block' (Def 5.6 object)")
    l143 = [i for i in range(7747, 7994) if "eq:unmarked-structural-block" in S[i - 1]]
    check(bool(l143), f"Lemma 14.3 cites eq:unmarked-structural-block (Lemma 5.7) at {l143}")
    check(lab.get("eq:unmarked-structural-block") in range(2956, 3002),
          "eq:unmarked-structural-block lies inside the Lemma 5.7 statement")

    # 3. Every Part II line that carries a bootstrap constant or cites the bootstrap.
    pat = re.compile(r"11/12|frac1\{24\}|1/24|part-II-bootstrap|part-II-bin-ceiling|"
                     r"\\delta\\le5/6|5/6<1|\\kappa\\in\[3/4,5/6\]|kappa<1")
    uses = [i for i, l in enumerate(S, 1) if i >= PART2_START and pat.search(l)]
    print("Part II lines with 11/12, 1/24, the bootstrap/bin-ceiling labels or 5/6 ceilings:", uses)

    # 4. beta_* definition: primitive finite-order Hecke characters, zeros in [1/2,1].
    d = "\n".join(S[377:386])
    check("primitive finite-order Hecke character" in d and "1/2\\le\\Re\\rho\\le1" in d,
          "beta_* (Sep30 378-386) ranges over primitive finite-order Hecke characters, 1/2<=Re rho<=1")
    check("finite-order Hecke character $\\eta$ modulo" in "\n".join(S[51:56])
          and "ray class group" in "\n".join(S[51:56]),
          "Sep30 52-54 defines finite-order Hecke character = ray class character")

    # 5. Oct 5 statement and non-circularity.
    check("Every finite-order Hecke $L$-function over $K$ has no zeros in the half-plane $\\Rea s>11/12$"
          in O[74 - 1], "Oct5 thm:main (74) is the full finite-order family over K, open half-plane")
    check("K=\\Q(\\sqrt{-3})" in O[71 - 1], "Oct5 K = Q(sqrt(-3)) (line 71)")
    cites = [i for i, l in enumerate(O, 1) if "OpenAI26" in l and "bibitem" not in l]
    check(cites == [81], f"Oct5 cites the 7/8 paper only at {cites} (intro), not in a proof")
    check("Fix a finite-order Hecke character $\\nu$ of $K$ and a finite set $S$" in O[665 - 1],
          "Oct5 reduction (665) fixes an arbitrary finite-order nu; S contains its conductor primes")

    print("ALL CHECKS PASSED" if not failures else f"{len(failures)} FAILURE(S)")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
