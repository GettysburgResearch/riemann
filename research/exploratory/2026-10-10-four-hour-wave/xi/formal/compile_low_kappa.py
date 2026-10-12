#!/usr/bin/env python3
"""Compile the real arithmetic adapter using the repository's pinned Lean."""

import hashlib
import json
from pathlib import Path
import re
import subprocess


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def invoke_lean(formal_root, arguments):
    return subprocess.run(
        ["bash", "-c",
         'source /workspace/.riemann-tools/activate.sh\nexec lake env lean "$@"',
         "low-kappa-adapter", *arguments],
        cwd=formal_root, text=True, capture_output=True, check=False,
    )


def main():
    here = Path(__file__).resolve().parent
    checkout = next(parent for parent in here.parents
                    if (parent / "formal" / "lakefile.toml").is_file())
    formal_root = checkout / "formal"
    source = here / "LowKappaCapacity.lean"
    source_text = source.read_text()
    require(not re.search(r"\b(?:sorry|admit)\b", source_text), "no admissions in candidate source")
    declarations = re.findall(r"^theorem (\w+)", source_text, flags=re.MULTILINE)
    require(len(declarations) == 15, "expected 15 candidate theorems")
    build = here / ".build"
    build.mkdir(exist_ok=True)
    olean, ilean = build / "LowKappaCapacity.olean", build / "LowKappaCapacity.ilean"
    arguments = ["-DwarningAsError=true", f"--root={here}",
                 "-o", str(olean), "-i", str(ilean), str(source)]
    result = invoke_lean(formal_root, arguments)
    output = result.stdout + result.stderr
    (here / "compiler-output.txt").write_text(output)
    require(result.returncode == 0, f"Lean returned {result.returncode}; see compiler-output.txt")
    require(olean.is_file() and ilean.is_file(), "compiled olean and ilean artifacts")
    permitted = {"propext", "Classical.choice", "Quot.sound"}
    axiom_reports = {}
    for match in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", output):
        name, raw = match.groups()
        axioms = {value.strip() for value in raw.split(",") if value.strip()}
        require(axioms <= permitted, f"unexpected axiom for {name}: {axioms - permitted}")
        axiom_reports[name] = sorted(axioms)
    namespace = "FourHourWave.LowKappaCapacity."
    require(set(axiom_reports) == {namespace + name for name in declarations},
            "axiom report covers every candidate theorem")
    version = invoke_lean(formal_root, ["--version"])
    require(version.returncode == 0, "Lean version query")
    manifest = json.loads((formal_root / "lake-manifest.json").read_text())
    mathlib = next(package for package in manifest["packages"] if package["name"] == "mathlib")
    receipt = {
        "status": "PASS_COMPILED_REAL_ARITHMETIC_ADAPTERS",
        "scope": "Real reflection/capacity inequalities with explicit hypotheses only",
        "lean_version": version.stdout.strip(),
        "mathlib_revision": mathlib["rev"],
        "source_sha256": sha(source),
        "runner_sha256": sha(Path(__file__)),
        "compiler_output_sha256": sha(here / "compiler-output.txt"),
        "olean_sha256": sha(olean),
        "ilean_sha256": sha(ilean),
        "lean_arguments": arguments,
        "candidate_theorem_count": len(declarations),
        "axiom_reports": axiom_reports,
        "explicit_real_nonvacuity": {
            "strict_comparison": {"M": "60", "A": "51", "z": "2",
                                  "kappa": "13/18", "Acomp": "43", "xi": "0"},
            "positive_support_error": {"M": "60", "A": "51", "z": "2",
                                       "kappa": "13/18", "Acomp": "44", "xi": "1"},
            "simultaneous_upper_equalities": {"M": "60", "A": "50", "z": "3",
                                              "kappa": "13/18", "Acomp": "46", "xi": "0"},
            "clipped_reflection": {"M": "60", "short": "10", "along": "50", "z": "1",
                                   "ell": "3", "kappa": "13/18", "reflected": "10", "xi": "0"},
        },
        "analytic_reflection_identity_formalized": False,
        "fourth_moment_parameter_extension_formalized": False,
        "zero_free_conclusion_formalized": False,
        "actual_xi_evaluated": False,
        "rh_proved": False,
    }
    target = here / "low-kappa-compilation.json"
    target.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(receipt["status"], f"theorems={len(declarations)}")


if __name__ == "__main__":
    main()
