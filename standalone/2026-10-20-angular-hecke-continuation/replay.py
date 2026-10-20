#!/usr/bin/env python3
"""Verify packet bytes and the limited exact finite algebra receipt.

The enclosing Git commit authenticates MANIFEST.json. This program does
not authenticate or reprove external analytic sources, or certify any
infinite-family theorem.
"""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "MANIFEST.json").read_text())
    actual = {p.name for p in root.iterdir() if p.is_file() and p.name != "MANIFEST.json"}
    require(actual == set(manifest["files"]), "packet file coverage mismatch")
    for name, expected in manifest["files"].items():
        path = root / name
        require(not path.is_symlink(), "symlink is outside this manifest contract")
        data = path.read_bytes()
        require(len(data) == expected["bytes"], f"byte count changed: {name}")
        require(hashlib.sha256(data).hexdigest() == expected["sha256"],
                f"digest changed: {name}")

    for name, expected in manifest.get("local_dependencies", {}).items():
        path = root / name
        require(path.is_file(), f"missing local dependency: {name}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == expected,
                f"dependency changed: {name}")

    for path in root.glob("*.md"):
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text()):
            if "://" in link or link.startswith("#"):
                continue
            local = link.split("#", 1)[0]
            require((root / local).exists(), f"missing local link in {path.name}: {local}")

    result = subprocess.run(
        [sys.executable, "-I", "-S", "-B", str(root / "verify_local_algebra.py")],
        check=True, text=True, capture_output=True,
    )
    expected = (root / "LOCAL_ALGEBRA.json").read_text()
    require(result.stdout == expected, "local algebra receipt differs byte for byte")
    require(json.loads(result.stdout)["accepted"] is True, "finite algebra rejected")
    print(json.dumps({
        "status": "PASS",
        "manifest_files": len(actual),
        "local_dependencies": len(manifest.get("local_dependencies", {})),
        "finite_algebra": "reproduced byte for byte in isolated standard-library Python",
        "scope": "file integrity and exact finite identities only; analytic theorems are not certified",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
