#!/usr/bin/env python3
"""Verify and optionally restore two byte-preserved research packets. Runs no recovered code."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import lzma
import tarfile
from pathlib import Path, PurePosixPath

ARCHIVE_SHA256 = "9e105eed5a7b87861dcc34c24c682a6ad611877a51619e0f5607c851eb172a0d"
TREES = {
    "standalone/2026-10-18-circle-prime-bracketing": "45a5b3b3743c2083a68d6b08f3c57f694f166b1f",
    "standalone/2026-10-18-degree20-continuation-attempt": "fe8b5af4d603d6a5dca6fb43008a3e77c739c5fb",
}
NAMES = {
    "standalone/2026-10-18-circle-prime-bracketing": set(
        "CHECKS.json EXPLORATION.md MANIFEST.json MUTATIONS.json NUMERIC_DIAGNOSTIC.json "
        "PROOF.md PUBLICATION.md README.md SOURCES.md VALIDATION.md numeric_probe.py "
        "replay.py verify.py".split()),
    "standalone/2026-10-18-degree20-continuation-attempt": set(
        "MANIFEST.json README.md RESULTS.json SOURCES.json baseline_parameters.json "
        "diagnose.py manifold_face.py manifold_search.py search_state.json source24.json "
        "spin_model.py tangent_scan.json theta_source24.py".split()),
}

def git_hash(kind: str, data: bytes) -> str:
    return hashlib.sha1(f"{kind} {len(data)}".encode() + b"\0" + data).hexdigest()

def directory_tree(files: dict[str, bytes]) -> str:
    entries = []
    for name, data in sorted(files.items()):
        entries.append(b"100644 " + name.encode() + b"\x00" + bytes.fromhex(git_hash("blob", data)))
    return git_hash("tree", b"".join(entries))

def payload(root: Path) -> dict[str, bytes]:
    data = b"".join((root / "parts" / f"part-{i:02}").read_bytes() for i in range(8))
    if len(data) != 60400 or hashlib.sha256(data).hexdigest() != ARCHIVE_SHA256:
        raise ValueError("Archive size or SHA-256 mismatch")
    decompressor = lzma.LZMADecompressor()
    raw = decompressor.decompress(data, max_length=300001)
    if len(raw) > 300000 or not decompressor.eof or decompressor.unused_data:
        raise ValueError("Unexpected uncompressed archive size or trailing stream")
    expected = {f"{directory}/{name}" for directory, names in NAMES.items() for name in names}
    files = {}
    with tarfile.open(fileobj=io.BytesIO(raw), mode="r:") as archive:
        for member in archive:
            path = PurePosixPath(member.name)
            if (not member.isfile() or member.name not in expected or member.name in files
                    or path.is_absolute() or ".." in path.parts or member.size > 200000):
                raise ValueError(f"Unexpected archive member: {member.name!r}")
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError("Missing regular-file content")
            files[member.name] = stream.read()
    if set(files) != expected or sum(map(len, files.values())) != 183164:
        raise ValueError("Original file inventory or size mismatch")
    for directory in NAMES:
        local = {name: files[f"{directory}/{name}"] for name in NAMES[directory]}
        if directory_tree(local) != TREES[directory]:
            raise ValueError(f"Original Git tree mismatch: {directory}")
        manifest = json.loads(local["MANIFEST.json"])["files"]
        records = manifest if isinstance(manifest, list) else [
            dict(record, path=name) for name, record in manifest.items()]
        if {record["path"] for record in records} != set(local) - {"MANIFEST.json"}:
            raise ValueError("Original manifest coverage mismatch")
        for record in records:
            value = local[record["path"]]
            if len(value) != record["bytes"] or hashlib.sha256(value).hexdigest() != record["sha256"]:
                raise ValueError(f"Original manifest mismatch: {record['path']}")
    return files

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="NEW directory; an existing path is refused")
    args = parser.parse_args()
    files = payload(Path(__file__).resolve().parent)
    if args.output is not None:
        args.output.mkdir(parents=True, exist_ok=False)
        for name, data in sorted(files.items()):
            target = args.output.joinpath(*PurePosixPath(name).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("xb") as stream:
                stream.write(data)
    print(json.dumps({"verified_original_files": len(files), "bytes": 183164,
                      "archive_sha256": ARCHIVE_SHA256, "original_trees": TREES,
                      "output": str(args.output) if args.output is not None else None,
                      "executed_recovered_code": False}, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
