#!/usr/bin/env python3
"""Authenticate this proposed packet and optionally replay its finite checks.

Hashes authenticate bytes, not analytic theorems. The scientific scope of each
check is recorded in VALIDATION.md and the corresponding proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def authenticate():
    manifest = json.loads((ROOT / "MANIFEST.json").read_text())
    require(manifest["format"] == 1, "unsupported manifest format")
    for name, expected in manifest["files"].items():
        path = (ROOT / name).resolve()
        require(path.is_relative_to(ROOT), "manifest path outside packet")
        data = path.read_bytes()
        require(len(data) == expected["bytes"], f"size mismatch: {name}")
        require(hashlib.sha256(data).hexdigest() == expected["sha256"],
                f"SHA-256 mismatch: {name}")
    return manifest


def run(command, label):
    result = subprocess.run(command, cwd=ROOT, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    require(result.returncode == 0,
            f"{label} failed ({result.returncode})\n{result.stdout}\n{result.stderr}")
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay", action="store_true")
    parser.add_argument("--theta-source", type=Path,
                        help="Override the exact inherited theta source directory")
    args = parser.parse_args()
    manifest = authenticate()
    result = {
        "status": "MANIFEST_PASS",
        "files_authenticated": len(manifest["files"]),
        "source_commit": manifest["source_commit"],
        "scope": "byte authentication; no analytic proof claimed by hashes",
    }
    if args.replay:
        shared_output = run(
            [sys.executable, "-O", str(ROOT / "shared/check_shared_factor.py"),
             "--output", str(ROOT / "shared/check_report.json")], "shared")
        require(json.loads(shared_output)["status"] == "PASS",
                "shared checker did not report PASS")
        strip_command = [sys.executable, "-O", str(ROOT / "strip/check_strip.py")]
        if args.theta_source:
            strip_command += ["--source", str(args.theta_source.resolve())]
        strip_output = run(strip_command, "strip")
        require(strip_output.startswith("STRIP_FINITE_AND_GRAPH_PASS "),
                "strip checker did not report PASS")
        certificate = json.loads((ROOT / "strip/certificate.json").read_text())
        require(certificate["status"] == "PASS", "strip certificate status")
        authenticate()
        result.update({
            "status": "MANIFEST_AND_FINITE_REPLAY_PASS",
            "optimized_python": True,
            "shared": "exact integer, rational and complex-rational identities",
            "strip": "authenticated primitive theta replay; directed degree-4 model; exact graph enumeration",
            "generated_artifacts": "byte-identical to the committed manifest",
            "not_certified": [
                "analytic family limits",
                "imported theorems",
                "proposed degree-20 source root",
                "empirical degree-22 continuation",
                "cofinal moment matching",
                "improved zeta zero-free strip",
                "RH",
            ],
        })
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
