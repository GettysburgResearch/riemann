#!/usr/bin/env python3
"""Replay the finite component reports; never interpret PASS as an RH proof."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

ROOT = Path(__file__).resolve().parent


def require(value, message):
    if not value:
        raise RuntimeError(message)


def main():
    manifest = ROOT / "SHA256SUMS"
    if manifest.exists():
        for line in manifest.read_text(encoding="utf-8").splitlines():
            digest, name = line.split("  ", 1)
            require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                    "manifest mismatch: " + name)
    reports = []
    cases = [
        ("check_direct_identity.py", "DIRECT_CHECKS.json", True),
        ("check_native_angular_rays.py", "NATIVE_ANGULAR_CHECK_RESULTS.json", False),
        ("check_capped_norm_transfer.py", "CAPPED_CHECK_RESULTS.json", False),
    ]
    for script, report, output_argument in cases:
        require((ROOT / script).is_file(), "missing checker: " + script)
        expected = (ROOT / report).read_bytes()
        results = []
        for optimized in (False, True):
            with tempfile.TemporaryDirectory(prefix="riemann-component-") as tmp:
                directory = Path(tmp)
                shutil.copy2(ROOT / script, directory / script)
                command = [sys.executable] + (["-O"] if optimized else []) + [str(directory / script)]
                if output_argument:
                    command += ["--output", str(directory / report)]
                result = subprocess.run(command, cwd=directory, capture_output=True, check=True)
                actual = (directory / report).read_bytes()
                require(actual == expected, "archived report mismatch: " + report)
                results.append({"optimized": optimized, "report_sha256": hashlib.sha256(actual).hexdigest()})
        reports.append({"script": script, "runs": results})
    print(json.dumps({"status": "PASS", "scope": "Finite archived reports and file bytes only", "reports": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
