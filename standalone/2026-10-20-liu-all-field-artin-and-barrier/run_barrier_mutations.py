#!/usr/bin/env python3
"""Replay exactly three negative controls for beyond_hybrid_barrier.py.

Uses only the standard library. Mutated copies live in an automatically
removed temporary directory; the original checker is never modified.
"""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    source_path = Path(__file__).resolve().with_name("beyond_hybrid_barrier.py")
    source_bytes = source_path.read_bytes()
    source = source_bytes.decode("utf-8")
    controls = [
        {
            "name": "quartic_changed",
            "old": "Q = [-275, 1290, 9936, -27405, 16686]",
            "new": "Q = [-274, 1290, 9936, -27405, 16686]",
            "gate": "quartic endpoint signs",
        },
        {
            "name": "witness_overlap_broken",
            "old": "b0, b1, b2 = F(969, 10000), F(273, 2500), F(13, 100)",
            "new": "b0, b1, b2 = F(969, 10000), F(1093, 10000), F(13, 100)",
            "gate": "0.0969<=b<=0.1092 pointwise margin",
        },
        {
            "name": "unequal_length_sign_flipped",
            "old": "C0, C0 - 3 * theta / 4]",
            "new": "C0, C0 + 3 * theta / 4]",
            "gate": "free-length affine identity 3",
        },
    ]
    results = []
    with tempfile.TemporaryDirectory(prefix="barrier_mutation_controls_") as directory:
        for control in controls:
            require(source.count(control["old"]) == 1,
                    "mutation locator is not unique: " + control["name"])
            mutated = source.replace(control["old"], control["new"])
            path = Path(directory, control["name"] + ".py")
            path.write_text(mutated, encoding="utf-8")
            result = subprocess.run(
                [sys.executable, "-I", "-S", "-B", "-O", str(path)],
                capture_output=True, text=True, check=False)
            expected = "certificate failed: " + control["gate"]
            require(result.returncode != 0 and expected in result.stderr,
                    "mutation did not fail at its designated gate: " + control["name"])
            results.append({"name": control["name"],
                            "return_code": result.returncode,
                            "rejected_at": control["gate"],
                            "mutated_sha256": sha256(mutated.encode("utf-8")).hexdigest()})
    print(json.dumps({"status": "PASS", "mode": "optimized isolated Python",
                      "checker": source_path.name,
                      "checker_sha256": sha256(source_bytes).hexdigest(),
                      "controls": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
