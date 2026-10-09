#!/usr/bin/env python3
"""Independently enumerate and hash a fresh selected-source assembly."""
import argparse
import hashlib
import json
from pathlib import Path
import stat

PACKET = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    root = args.directory
    if root.is_symlink() or not root.is_dir():
        raise SystemExit("Expected an ordinary assembled directory")
    manifest = json.loads((PACKET / "SOURCE_MANIFEST.json").read_text())
    expected = {r["upstream_path"]: r for r in manifest["files"]}
    if len(expected) != manifest["file_count"]:
        raise SystemExit("Manifest path count mismatch")
    actual = set()
    for file in root.rglob("*"):
        mode = file.lstat().st_mode
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise SystemExit(f"Nonregular assembly object: {file}")
        actual.add(file.relative_to(root).as_posix())
    if actual != set(expected):
        raise SystemExit("Assembly contains missing or additional files")
    for path, row in expected.items():
        file = root / path
        data = file.read_bytes()
        if len(data) != row["bytes"] or hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise SystemExit(f"Assembly byte mismatch: {path}")
        if bool(file.stat().st_mode & stat.S_IXUSR) != (row["git_mode"] == "100755"):
            raise SystemExit(f"Assembly executable-mode mismatch: {path}")
    print(json.dumps({"status": "PASS", "check": "independent assembled path, SHA-256, and executable-mode comparison",
                      "files": len(actual), "extra_files": 0, "missing_files": 0,
                      "kernel_build_run": False}, indent=2))


if __name__ == "__main__":
    main()
