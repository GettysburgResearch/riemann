"""Static AF count-definition and comparator-type checks; no Lean compilation."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "sources/formal_round2/zeta-23-lean-v1.0"


def definition(path, name):
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(f"def {name} "))
    result = [lines[start]]
    for line in lines[start + 1:]:
        if line and line[0].isspace():
            result.append(line)
        else:
            break
    return "\n".join(result)


def theorem_type(path, name):
    src = path.read_text()
    match = re.search(r"(?m)^theorem " + re.escape(name) + r"\s*:", src)
    assert match, (path, name)
    return " ".join(src[match.end():].split(":=", 1)[0].split())


names = ["IsNontrivialZero", "zeroMult", "zerosIn", "Ncount", "Ndist",
         "N0", "N0star", "N0simple", "Nsimple"]
for name in names:
    assert definition(BASE / "comparator/ChallengeDeps.lean", name) == definition(
        BASE / "Zeta23/Statement.lean", name)

base_names = ["two_thirds_on_critical_line", "two_thirds_on_critical_line_cumulative",
              "half_simple_on_critical_line", "half_simple_on_critical_line_cumulative",
              "three_quarters_distinct", "three_quarters_distinct_cumulative",
              "montgomery_taylor_on_critical_line", "montgomery_taylor_simple_on_critical_line",
              "montgomery_taylor_distinct"]
mult_names = ["two_thirds_simple_on_critical_line", "two_thirds_simple_on_critical_line_cumulative",
              "five_sixths_distinct", "five_sixths_distinct_cumulative",
              "montgomery_taylor_simple_on_critical_line_mult",
              "montgomery_taylor_simple_on_critical_line_mult_cumulative",
              "montgomery_taylor_distinct_mult", "montgomery_taylor_distinct_mult_cumulative"]
types = []
for challenge, solution, theorem_names in [
    ("comparator/Challenge.lean", "comparator/Solution.lean", base_names),
    ("comparator/Challenge/Multiplicity.lean", "comparator/Solution/Multiplicity.lean", mult_names),
]:
    for name in theorem_names:
        typ = theorem_type(BASE / challenge, name)
        assert typ == theorem_type(BASE / solution, name)
        types.append({"name": name, "challenge": challenge, "solution": solution,
                      "whitespace_normalized_type": typ, "exact_source_type_match": True})

files = ["comparator/ChallengeDeps.lean", "comparator/Challenge.lean", "comparator/Solution.lean",
         "comparator/Challenge/Multiplicity.lean", "comparator/Solution/Multiplicity.lean",
         "Zeta23/Statement.lean", "Zeta23/Statement/Seam.lean", "Zeta23/Statement/SeamClosed.lean",
         "Zeta23/Defs/Counting.lean", "Zeta23/FinalMult.lean", "Zeta23/ThmD/Mult.lean"]
result = {"kind": "static_semantic_source_comparison_not_lean_build",
          "repository_commit": "3635e74826a4c1fcece7d1cd2b6fa75e43a00510",
          "mathlib_commit": "51e6992efd06126df61a496bebf8f49482a4e129",
          "literal_definition_matches": names,
          "zeta_only_comparator_type_matches": types,
          "sha256": {file: hashlib.sha256((BASE / file).read_bytes()).hexdigest() for file in files},
          "scope": "Definition/type source equality only. The semantic proof is independently reconstructed in the accompanying review; no kernel replay, successful build, or complete axiom-closure claim."}
(ROOT / "experiments/results/AF_count_semantics_static_checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"Passed: {len(names)} literal definition matches; {len(types)} zeta Challenge/Solution type matches.")
