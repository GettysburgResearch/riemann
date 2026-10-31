#!/usr/bin/env python3
"""Verify the recovered research packet; optionally restore to a NEW directory."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import tarfile

ARCHIVE_SHA256 = "eaf3fb5fe828e33974f2bab471647576083b4917154ecfe5f7acf219929566cd"

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def safe_name(name: str) -> bool:
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts and "\\" not in name

def verify(root: Path) -> dict[str, bytes]:
    index = json.loads((root / "PARTS.json").read_text())
    blocks = []
    for item in index["parts"]:
        if not safe_name(item["path"]):
            raise ValueError("Unsafe part name")
        data = (root / item["path"]).read_bytes()
        if len(data) != item["bytes"] or sha256(data) != item["sha256"]:
            raise ValueError("Part integrity failure: " + item["path"])
        blocks.append(data)
    archive = b"".join(blocks)
    if len(archive) != 79868 or sha256(archive) != ARCHIVE_SHA256:
        raise ValueError("Archive integrity failure")
    files: dict[str, bytes] = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:xz") as tar:
        members = tar.getmembers()
        if len(members) != 39 or sum(m.size for m in members) > 300000:
            raise ValueError("Unexpected archive size")
        for member in members:
            if not member.isfile() or not safe_name(member.name) or member.name in files:
                raise ValueError("Unsafe or duplicate archive member")
            source = tar.extractfile(member)
            if source is None:
                raise ValueError("Unreadable member")
            files[member.name] = source.read()
    manifest = json.loads(files["MANIFEST.json"])
    expected = {entry["path"] for entry in manifest["files"]} | {"MANIFEST.json"}
    if expected != set(files) or len(manifest["files"]) != 38:
        raise ValueError("Manifest membership mismatch")
    for entry in manifest["files"]:
        data = files[entry["path"]]
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        if (len(data), sha256(data), blob) != (entry["bytes"], entry["sha256"], entry["git_blob_sha1"]):
            raise ValueError("Original file integrity failure: " + entry["path"])
    return files

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="New directory; existing paths are never overwritten")
    args = parser.parse_args()
    files = verify(Path(__file__).resolve().parent)
    if args.output is not None:
        args.output.mkdir(parents=True, exist_ok=False)
        for name, data in files.items():
            target = args.output / name
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
    print(json.dumps({"status": "PASS", "verified_files": len(files), "restored": args.output is not None}))

if __name__ == "__main__":
    main()
