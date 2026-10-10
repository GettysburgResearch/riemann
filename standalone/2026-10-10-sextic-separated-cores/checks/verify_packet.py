#!/usr/bin/env python3
"""Verify a frozen packet and the exact retained source/review bindings."""

from pathlib import Path, PurePosixPath
import hashlib
import json
import subprocess


def require(condition, detail):
    if not condition:
        raise RuntimeError(detail)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def git_blob(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main():
    packet = Path(__file__).resolve().parents[1]
    repo = packet.parents[1]
    manifest = json.loads((packet / "MANIFEST.json").read_text())
    entries = manifest["files"]
    seen = set()
    for entry in entries:
        relative = entry["path"]
        canonical = PurePosixPath(relative)
        require(
            not canonical.is_absolute() and ".." not in canonical.parts
            and str(canonical) == relative and "\\" not in relative,
            "noncanonical manifest path: " + relative,
        )
        require(relative not in seen, "duplicate manifest path: " + relative)
        seen.add(relative)
        path = (packet / relative).resolve()
        require(path.is_relative_to(packet), "unsafe manifest path: " + relative)
        data = path.read_bytes()
        require(len(data) == entry["bytes"], "file size mismatch: " + relative)
        require(sha256(data) == entry["sha256"], "file hash mismatch: " + relative)

    actual = set()
    for path in packet.rglob("*"):
        require(not path.is_symlink(), "symlink in packet: " + str(path))
        if path.is_file():
            relative = path.relative_to(packet).as_posix()
            if relative != "MANIFEST.json":
                actual.add(relative)
    require(
        actual == seen,
        "manifest inventory differs: missing=" + str(sorted(actual - seen))
        + ", extra=" + str(sorted(seen - actual)),
    )

    lock = json.loads((packet / "SOURCE_LOCK.json").read_text())
    for source in lock["sources"]:
        if "snapshot" in source:
            data = (packet / source["snapshot"]).read_bytes()
        else:
            relative = source["retained_path"]
            path = repo / relative
            data = (
                path.read_bytes() if path.exists()
                else subprocess.check_output(["git", "show", "HEAD:" + relative], cwd=repo)
            )
        require(len(data) == source["bytes"], "source size mismatch: " + source["path"])
        require(sha256(data) == source["sha256"], "source hash mismatch: " + source["path"])
        require(git_blob(data) == source["git_blob"], "source Git blob mismatch: " + source["path"])
        lookup = subprocess.run(
            ["git", "rev-parse", "--verify", source["commit"] + ":" + source["path"]],
            cwd=repo, capture_output=True, text=True,
        )
        require(
            lookup.returncode == 0,
            "pinned source object unavailable locally; fetch its exact locked commit: "
            + source["commit"] + " for " + source["path"],
        )
        require(
            lookup.stdout.strip() == source["git_blob"],
            "source commit:path does not resolve to locked blob: " + source["path"],
        )

    bindings = 0
    for review in manifest["review_bindings"]:
        report = (packet / review["review"]).read_text()
        for target, expected in review["targets"].items():
            data = (packet / target).read_bytes()
            require(sha256(data) == expected, "review target changed: " + target)
            require(expected in report, "target hash absent from review: " + target)
            bindings += 1
    print(json.dumps({
        "status": "PASS",
        "manifest_files": len(entries),
        "pinned_source_copies": len(lock["sources"]),
        "source_commit_path_bindings": len(lock["sources"]),
        "review_target_bindings": bindings,
        "scope": "Byte/source/review integrity only; not an analytic proof.",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
