#!/usr/bin/env python3
"""Replay resident hashes and exact finite component checks, not an RH proof."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "MANIFEST.json").read_text())
    for name, expected in manifest["files_sha256"].items():
        path = root / name
        if path.parent != root or not path.is_file():
            raise ValueError("invalid resident path: " + name)
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError("hash mismatch: " + name)
    check = subprocess.run(
        [sys.executable, "-I", "-S", "-B", str(root / "verify_signed_components.py")],
        check=True, capture_output=True, text=True,
    )
    actual = json.loads(check.stdout)
    saved = json.loads((root / "SIGNED_CHECKS.json").read_text())
    if actual != saved or actual["status"] != "PASS":
        raise ValueError("finite component receipt mismatch")
    print(json.dumps({
        "status": "PASS",
        "resident_files_verified": len(manifest["files_sha256"]),
        "symbolic_comparison_cases": len(actual["symbolic_comparison_cases"]),
        "scope": "Resident hashes and finite algebra; no smaller zero-free boundary established.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
