#!/usr/bin/env python3
"""Replay the finite component checks and authenticate this packet's bytes.

This verifies finite regressions and local integrity, not analytic theorems.
The manifest is meaningful as a commitment only when obtained from the frozen
Git commit; it is not independent evidence supplied by its own contents.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


COMPONENTS = [
    ("verify_audit_components.py", "VERIFICATION.json"),
    ("check_fourier_transfer.py", "FOURIER_CHECK_RESULTS.json"),
    ("check_pole_calibration.py", "POLE_CHECK_RESULTS.json"),
    ("check_memory_and_scattering.py", "MEMORY_CHECK_RESULTS.json"),
]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--with-probe", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    manifest = root / "SHA256SUMS"
    require(manifest.is_file(), "SHA256SUMS is missing")
    seen = set()
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, name = line.split("  ", 1)
        require(name not in seen, "duplicate manifest entry")
        require(Path(name).name == name and name != manifest.name,
                "manifest entries must be distinct direct children")
        seen.add(name)
        path = root / name
        require(path.is_file(), "missing manifest file: " + name)
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                "hash mismatch: " + name)
    actual = {p.name for p in root.iterdir() if p.is_file() and p != manifest}
    require(seen == actual, "manifest file coverage mismatch")

    for script in root.glob("*.py"):
        compile(script.read_text(encoding="utf-8"), str(script), "exec")

    checked = []
    with tempfile.TemporaryDirectory(prefix="riemann-scattering-replay-") as td:
        for script, report in COMPONENTS:
            expected = (root / report).read_bytes()
            for optimized in (False, True):
                command = [sys.executable]
                if optimized:
                    command.append("-O")
                command.append(str(root / script))
                if script == "verify_audit_components.py":
                    command.extend(["--output", str(Path(td) / report)])
                result = subprocess.run(command, cwd=root, capture_output=True,
                                        check=False, timeout=120)
                require(result.returncode == 0,
                        script + " failed: " + result.stderr.decode(errors="replace"))
                require(result.stdout == expected,
                        script + " differs from its archived finite report")
                json.loads(result.stdout)
                checked.append({"script": script, "optimized": optimized,
                                "matches_archived_bytes": True})
        if args.with_probe:
            result = subprocess.run([sys.executable, str(root / "prime_detector_probe.py")],
                                    cwd=root, capture_output=True, check=False, timeout=120)
            require(result.returncode == 0, "prime probe failed")
            require(result.stdout == (root / "PRIME_PROBE_RESULTS.json").read_bytes(),
                    "prime probe differs from archived binary64 sample")

    print(json.dumps({"status": "PASS_FINITE_REPLAY", "manifest_files": len(seen),
                      "component_runs": checked, "prime_probe_replayed": args.with_probe,
                      "scope": "Finite exact algebra and non-directed Gaussian regressions; no RH proof, infinite theorem check, or interval certificate."},
                     indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
