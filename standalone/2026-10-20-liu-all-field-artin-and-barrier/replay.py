#!/usr/bin/env python3
"""Replay the finite certificates and packet integrity checks, using stdlib only.

No analytic theorem is certified by this runner. The optional independent
SymPy review is documented in VALIDATION.md and is outside this stdlib run.
"""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "MANIFEST.json").read_text())
    listed = manifest["files"]
    observed = {p.name for p in root.iterdir() if p.is_file() and p.name != "MANIFEST.json"}
    require(set(listed) == observed, "packet file coverage differs from MANIFEST.json")
    for name, record in listed.items():
        content = (root / name).read_bytes()
        require(len(content) == record["bytes"], "file length mismatch: " + name)
        require(sha256(content).hexdigest() == record["sha256"], "file digest mismatch: " + name)
    for path in root.glob("*.py"):
        compile(path.read_text(), str(path), "exec")

    # Links in the packet are either external references or sibling files.
    for path in root.glob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            name = target.split("#", 1)[0]
            require((path.parent / name).exists(), "missing local Markdown target: " + target)

    checks = [
        ("beyond_hybrid_barrier.py", "beyond_hybrid_barrier.json"),
        ("verify_a5_artin.py", "A5_CERTIFICATE.json"),
        ("verify_principal_factorization.py", "PRINCIPAL_FACTORIZATION_CERTIFICATE.json"),
        ("run_barrier_mutations.py", "beyond_mutation_controls.json"),
    ]
    results = []
    for checker, receipt in checks:
        expected = (root / receipt).read_bytes()
        outputs = []
        for optimized in (False, True):
            command = [sys.executable, "-I", "-S", "-B"]
            if optimized:
                command.append("-O")
            command.append(str(root / checker))
            run = subprocess.run(command, capture_output=True, check=False)
            require(run.returncode == 0, checker + " failed: " + run.stderr.decode())
            require(run.stdout == expected, checker + " differs from its pinned receipt")
            outputs.append(run.stdout)
        require(outputs[0] == outputs[1], "optimization changed receipt: " + checker)
        results.append({"checker": checker, "normal_and_optimized": "PASS",
                        "receipt_sha256": sha256(expected).hexdigest()})
    print(json.dumps({
        "status": "PASS",
        "scope": "Packet hashes, local links, Python syntax, and four finite certificate replays only",
        "manifest_sha256": sha256((root / "MANIFEST.json").read_bytes()).hexdigest(),
        "files_authenticated": len(listed),
        "checks": results,
        "analytic_proof_certified": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
