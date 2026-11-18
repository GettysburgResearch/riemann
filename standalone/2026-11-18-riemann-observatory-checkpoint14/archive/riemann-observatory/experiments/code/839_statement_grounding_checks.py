"""Lightweight static definition and exact-ratio checks, not a Lean build."""
from pathlib import Path
from fractions import Fraction
from decimal import Decimal, localcontext
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
LEAN = ROOT / "sources/formal_round2/839-v1/lean"
UPSTREAM = ROOT / "sources/formal_round2/formal-math-fbdc36b-zeta23"


def definition(path: Path, name: str) -> str:
    lines = path.read_text().splitlines()
    start = next(i for i, line in enumerate(lines) if line.startswith(f"def {name} "))
    block = [lines[start]]
    for line in lines[start + 1:]:
        if line and line[0].isspace():
            block.append(line)
        else:
            break
    return "\n".join(block)


matches = []
for challenge, names in {
    "Challenge839.lean": ["IsNontrivialZero", "zeroMult", "zerosIn", "Ncount", "Ndist"],
    "Challenge673.lean": ["IsNontrivialZero", "zeroMult", "zerosIn", "Ncount", "N0simple"],
    "Challenge889.lean": ["IsNontrivialZero", "zeroMult", "zerosIn", "Ncount"],
    "ChallengeFurther.lean": ["IsNontrivialZero", "zeroMult", "zerosIn", "Ncount"],
}.items():
    for name in names:
        body = definition(LEAN / challenge, name)
        assert body == definition(UPSTREAM / "ChallengeDeps.lean", name)
        assert body == definition(UPSTREAM / "Zeta23/Statement.lean", name)
        matches.append({"challenge": challenge, "definition": name,
                        "matches_pinned_dependency_exactly": True})

for path in ["Challenge839.lean", "ChallengeFurther.lean", "Solution839.lean", "SolutionFurther.lean"]:
    assert definition(LEAN / path, "Nsimple") == definition(UPSTREAM / "Zeta23/Statement.lean", "Nsimple")

union = definition(LEAN / "Challenge889.lean", "NsimpleOrLine")
for path in ["ChallengeFurther.lean", "Solution889.lean", "SolutionFurther.lean", "Further/Defs.lean"]:
    assert union == definition(LEAN / path, "NsimpleOrLine")

n0 = definition(LEAN / "ChallengeFurther.lean", "N0mult")
assert n0 == definition(LEAN / "SolutionFurther.lean", "N0mult")
assert n0 == definition(LEAN / "Further/Defs.lean", "N0mult")
assert n0.replace("def N0mult ", "def N0 ", 1) == definition(UPSTREAM / "Zeta23/Statement.lean", "N0")

q = Fraction(1645064, 1960733)
simple = Fraction(1329395, 1960733)
simple_critical = Fraction(1669159, 2478195)
average = Fraction(2073677, 2478195)
union_first = Fraction(3376433, 3797325)
union_third = Fraction(50652159, 56956375)
assert simple == 2 * q - 1
assert average == (1 + simple_critical) / 2
assert union_first < union_third

with localcontext() as ctx:
    ctx.prec = 30
    ratios = [{"quantity": name, "exact": str(val),
               "decimal": str(Decimal(val.numerator) / Decimal(val.denominator))}
              for name, val in [("distinct_anywhere", q), ("simple_anywhere", simple),
                                ("simple_and_critical", simple_critical),
                                ("average_simple_and_critical_mult", average),
                                ("union_first_window_mult", union_first),
                                ("union_third_window_mult", union_third)]]

files = [LEAN / f for f in ["Challenge839.lean", "Challenge673.lean", "Challenge889.lean",
                           "ChallengeFurther.lean", "Solution839.lean", "Solution673.lean",
                           "Solution889.lean", "SolutionFurther.lean"]]
result = {"kind": "static_statement_grounding_not_kernel_replay",
          "source_commit": "0e961ea199b425010843bc8044676d4ad29fe031",
          "dependency_commit_as_pinned_by_source_readme": "fbdc36bbf17d20af3fd0447c6d1a8a02773c9844",
          "definition_matches": matches,
          "additional_checks": ["Nsimple definitions exactly match actual riemannZeta count",
                                "union definitions exactly match Challenge/Solution/development",
                                "N0mult is exact renamed copy of Zeta23.N0",
                                "simple constant equals 2q-1",
                                "average constant equals (1+s0)/2"],
          "ratios": ratios,
          "sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
          "scope": "Exact source-text and rational arithmetic checks only; no Lean build or axiom-closure certification."}
out = ROOT / "experiments/results/839_statement_grounding_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "passed", "definition_matches": len(matches), "ratios": ratios}, indent=2))
