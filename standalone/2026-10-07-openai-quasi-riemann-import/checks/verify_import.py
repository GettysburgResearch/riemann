#!/usr/bin/env python3
"""Authenticate the mirrored source bytes against the frozen source manifest.

This is an integrity check, not a Lean build or mathematical proof checker.
Optionally compare the entire selected file set and every blob identity to the
hardcoded upstream commit in an independently fetched checkout:
  python checks/verify_import.py --source /path/to/openai-math
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import subprocess

from import_upstream import (
    DIRECTORIES, SCHEMA, SINGLE_FILES, SOURCE_COMMIT_DATE_UTC,
    UPSTREAM_COMMIT, UPSTREAM_REPOSITORY, git_blob_id, regular_file_path,
    relative_posix_path, selected_path, selected_tree,
)


def mirrored_files(packet: Path) -> set[str]:
    root = packet / "upstream"
    if root.is_symlink() or not root.is_dir():
        raise ValueError("The upstream mirror must be an ordinary directory")
    present = set()
    for path in root.rglob("*"):
        mode = path.lstat().st_mode
        if stat.S_ISLNK(mode):
            raise ValueError(f"Symlink in upstream mirror: {path.relative_to(packet)}")
        if stat.S_ISREG(mode):
            present.add(path.relative_to(packet).as_posix())
        elif not stat.S_ISDIR(mode):
            raise ValueError(f"Nonregular object in upstream mirror: {path.relative_to(packet)}")
    return present


def compare_paths(actual: set[str], expected: set[str], label: str) -> None:
    if actual != expected:
        missing, extra = sorted(expected - actual), sorted(actual - expected)
        raise ValueError(f"{label}: missing {len(missing)} {missing[:20]}; "
                         f"extra {len(extra)} {extra[:20]}")


def verify_packet(packet: Path, source: Path | None = None) -> dict:
    packet = packet.resolve()
    manifest_path = regular_file_path(packet, "UPSTREAM_FILES.json", must_exist=True)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError("Manifest must be a JSON object")
    for key, expected in (
        ("schema", SCHEMA), ("upstream_commit", UPSTREAM_COMMIT),
        ("upstream_repository", UPSTREAM_REPOSITORY),
        ("source_commit_date_utc", SOURCE_COMMIT_DATE_UTC),
        ("selection", {"complete_directories": list(DIRECTORIES),
                       "individual_files": list(SINGLE_FILES)}),
    ):
        if manifest.get(key) != expected:
            raise ValueError(f"Frozen manifest metadata mismatch: {key}")
    rows = manifest.get("files")
    if not isinstance(rows, list):
        raise ValueError("Manifest files must be a list")

    expected_paths: set[str] = set()
    upstream_paths: set[str] = set()
    declared_bytes = 0
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Invalid manifest file entry")
        relative = relative_posix_path(row.get("path"))
        upstream = relative_posix_path(row.get("upstream_path"))
        if relative.as_posix() != "upstream/" + upstream.as_posix():
            raise ValueError(f"Invalid upstream-to-mirror path mapping: {relative}")
        if not selected_path(upstream.as_posix()):
            raise ValueError(f"Path outside the frozen import selection: {upstream}")
        if relative.as_posix() in expected_paths or upstream.as_posix() in upstream_paths:
            raise ValueError(f"Duplicate manifest file entry: {relative}")
        expected_paths.add(relative.as_posix())
        upstream_paths.add(upstream.as_posix())
        if type(row.get("bytes")) is not int or row["bytes"] < 0:
            raise ValueError(f"Invalid byte count: {relative}")
        if row.get("git_mode") not in {"100644", "100755"}:
            raise ValueError(f"Invalid regular-file Git mode: {relative}")
        for key, length in (("sha256", 64), ("git_blob_sha1", 40)):
            value = row.get(key)
            if not isinstance(value, str) or not re.fullmatch(rf"[0-9a-f]{{{length}}}", value):
                raise ValueError(f"Invalid {key}: {relative}")
        declared_bytes += row["bytes"]
    if type(manifest.get("file_count")) is not int or manifest["file_count"] != len(rows):
        raise ValueError("Manifest count mismatch")
    if type(manifest.get("total_bytes")) is not int or manifest["total_bytes"] != declared_bytes:
        raise ValueError("Manifest total byte count mismatch")
    absent = set(SINGLE_FILES) - upstream_paths
    absent_directories = [d for d in DIRECTORIES
                          if not any(path.startswith(d + "/") for path in upstream_paths)]
    if absent or absent_directories:
        raise ValueError(f"Missing required import selection: {sorted(absent)}, {absent_directories}")

    source_entries = selected_tree(source.resolve()) if source is not None else None
    if source_entries is not None:
        compare_paths(upstream_paths, set(source_entries), "Frozen upstream selection mismatch")
    # Enumerate before reading so no unlisted symlink or other object is overlooked.
    compare_paths(mirrored_files(packet), expected_paths, "Mirrored path mismatch")
    actual_bytes = 0
    for row in rows:
        relative = row["path"]
        path = regular_file_path(packet, relative, must_exist=True)
        data = path.read_bytes()
        actual = hashlib.sha256(data).hexdigest()
        blob = git_blob_id(data)
        if len(data) != row["bytes"] or actual != row["sha256"] or blob != row["git_blob_sha1"]:
            raise ValueError(f"Source integrity failure: {relative}")
        executable = bool(path.stat().st_mode & stat.S_IXUSR)
        if executable != (row["git_mode"] == "100755"):
            raise ValueError(f"Mirrored Git executable mode mismatch: {relative}")
        if source_entries is not None and source_entries[row["upstream_path"]] != (
                row["git_mode"], blob):
            raise ValueError(f"Frozen upstream tree mismatch: {relative}")
        actual_bytes += len(data)
    if actual_bytes != manifest["total_bytes"]:
        raise ValueError("Actual total byte count mismatch")
    return {"status": "PASS", "check": "source byte integrity only",
            "files": len(expected_paths), "bytes": actual_bytes,
            "frozen_git_tree_compared": source_entries is not None,
            "complete_frozen_selection_compared": source_entries is not None,
            "kernel_build_run": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parents[1]
    try:
        result = verify_packet(packet, args.source)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        raise SystemExit(str(exc)) from None
    print(json.dumps(result))


if __name__ == "__main__":
    main()
