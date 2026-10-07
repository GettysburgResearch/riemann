#!/usr/bin/env python3
"""Copy the frozen family-003 source subset from an existing upstream checkout.

No network access, source rewriting, Lean execution, or theorem acceptance occurs.
Run: python checks/import_upstream.py /absolute/path/to/openai-math
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import subprocess

SCHEMA = "openai-quasi-rh-source-import-v1"
UPSTREAM_COMMIT = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"
UPSTREAM_REPOSITORY = "https://github.com/openai/math"
SOURCE_COMMIT_DATE_UTC = "2026-10-06T21:58:50Z"
DIRECTORIES = (
    "preprints/The-Quasi-Riemann-Hypothesis-September-30-2026",
    "preprints/The-Quasi-Riemann-Hypothesis-October-5-2026",
    "preprints/Uniform-exclusion-of-Landau-Siegel-zeros-October-1-2026",
    "lean/OAI/NumberTheory/DirichletL",
    "lean/OAI/NumberTheory/SiegelZeros",
    "lean/patches",
)
SINGLE_FILES = (
    "LICENSE", "README.md", "CONTENTS.md", "overview.tex", "overview.pdf",
    "lean/LICENSE", "lean/README.md", "lean/lakefile.lean",
    "lean/lake-manifest.json", "lean/lean-toolchain", "lean/formalization.yaml",
    "lean/docs/003.md", "lean/ComparatorChallenges/README.md",
    *(f"lean/ComparatorChallenges/{stem}.{suffix}"
      for stem in ("QuasiRiemannHypothesis", "DirichletSevenEighths",
                   "HeckeSevenEighths", "SiegelZeros")
      for suffix in ("lean", "json")),
)


def git(source: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(source), *args])


def git_blob_id(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def relative_posix_path(value: str) -> PurePosixPath:
    if not isinstance(value, str) or not value or "\\" in value or "\0" in value:
        raise ValueError("Invalid relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts or not path.parts or path.as_posix() != value:
        raise ValueError(f"Invalid relative path: {value!r}")
    return path


def selected_path(path: str) -> bool:
    return path in SINGLE_FILES or any(path.startswith(d + "/") for d in DIRECTORIES)


def regular_file_path(base: Path, relative: str, *, must_exist: bool = False) -> Path:
    """Reject existing symlinks and nonregular files, including in ancestors.

    The caller controls the base directory. This preflight check does not claim
    protection against another process changing the filesystem during a write.
    """
    parts = relative_posix_path(relative).parts
    current = base.resolve()
    for index, part in enumerate(parts):
        current = current / part
        try:
            mode = current.lstat().st_mode
        except FileNotFoundError:
            if must_exist:
                raise ValueError(f"Missing regular file: {relative}") from None
            continue
        if stat.S_ISLNK(mode):
            raise ValueError(f"Symlink in file path: {relative}")
        if index < len(parts) - 1:
            if not stat.S_ISDIR(mode):
                raise ValueError(f"Nondirectory ancestor in file path: {relative}")
        elif not stat.S_ISREG(mode):
            raise ValueError(f"Expected a regular file: {relative}")
    return current


def selected_tree(source: Path) -> dict[str, tuple[str, str]]:
    """Read the complete selected file set from the hardcoded commit object."""
    entries = {}
    for raw in git(source, "ls-tree", "-r", "-z", UPSTREAM_COMMIT).split(b"\0"):
        if not raw:
            continue
        metadata, path_raw = raw.split(b"\t", 1)
        mode, object_type, blob = metadata.decode().split()
        path = path_raw.decode()
        if selected_path(path):
            relative_posix_path(path)
            if object_type != "blob" or mode not in {"100644", "100755"}:
                raise ValueError(f"Unexpected source object: {path}")
            entries[path] = (mode, blob)
    absent = set(SINGLE_FILES).difference(entries)
    if absent:
        raise ValueError(f"Missing required upstream files: {sorted(absent)}")
    absent_directories = [d for d in DIRECTORIES
                          if not any(path.startswith(d + "/") for path in entries)]
    if absent_directories:
        raise ValueError(f"Missing required upstream directories: {absent_directories}")
    return entries


def import_sources(source: Path, packet: Path) -> dict:
    source = source.resolve()
    packet = packet.resolve()
    if git(source, "rev-parse", "HEAD").decode().strip() != UPSTREAM_COMMIT:
        raise ValueError("The source checkout is not at the frozen upstream commit.")
    entries = selected_tree(source)
    # Verify the whole input and every destination before changing any file.
    manifest_path = regular_file_path(packet, "UPSTREAM_FILES.json")
    payloads = []
    for path, (mode, blob) in sorted(entries.items()):
        data = regular_file_path(source, path, must_exist=True).read_bytes()
        if git_blob_id(data) != blob:
            raise ValueError(f"Dirty or incomplete upstream source: {path}")
        regular_file_path(packet, "upstream/" + path)
        payloads.append((path, mode, blob, data))
    manifest = []
    for path, mode, blob, data in payloads:
        target = regular_file_path(packet, "upstream/" + path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        target.chmod(0o755 if mode == "100755" else 0o644)
        manifest.append({"path": "upstream/" + path, "upstream_path": path,
                         "git_blob_sha1": blob, "sha256": hashlib.sha256(data).hexdigest(),
                         "bytes": len(data), "git_mode": mode})
    document = {
        "schema": SCHEMA,
        "upstream_repository": UPSTREAM_REPOSITORY,
        "upstream_commit": UPSTREAM_COMMIT,
        "source_commit_date_utc": SOURCE_COMMIT_DATE_UTC,
        "selection": {"complete_directories": list(DIRECTORIES),
                      "individual_files": list(SINGLE_FILES)},
        "file_count": len(manifest),
        "total_bytes": sum(row["bytes"] for row in manifest),
        "files": manifest,
    }
    regular_file_path(packet, "UPSTREAM_FILES.json")
    manifest_path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
    return document


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    args = parser.parse_args()
    packet = Path(__file__).resolve().parents[1]
    try:
        document = import_sources(args.source, packet)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        raise SystemExit(str(exc)) from None
    print(json.dumps({key: document[key] for key in
                     ("upstream_commit", "file_count", "total_bytes")}))


if __name__ == "__main__":
    main()
