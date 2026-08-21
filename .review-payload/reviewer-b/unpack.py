#!/usr/bin/env python3
"""Fail-closed deterministic unpacker for the Reviewer B review artifacts."""
from __future__ import annotations

import base64
import hashlib
import io
import lzma
import tarfile
from pathlib import Path, PurePosixPath

CHUNK_COUNT = 8
B64_SHA256 = "6dcd46bb8613f2b77587abc5dfc7adef61f234ef22ce8e69394c7cc8b50d22c4"
COMPRESSED_SHA256 = "b8f1ba7b00f513f5693297db7a4d8fba1e004f6a1581260f27d41cf53c0532c5"
TAR_SHA256 = "ea84a180b3af8d158652a080de96655e3dac478e76ddb48d4bcbd7527e20406e"
TARGET_PREFIX = PurePosixPath("review/2026-08-21/operator")
EXPECTED_MEMBERS = 17


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    repo = Path.cwd().resolve()
    payload_dir = Path(__file__).resolve().parent
    chunks = sorted(payload_dir.glob("chunk-*.txt"))
    if len(chunks) != CHUNK_COUNT:
        raise RuntimeError(f"expected {CHUNK_COUNT} chunks, found {len(chunks)}")

    encoded = "".join(path.read_text(encoding="ascii") for path in chunks).encode("ascii")
    if digest(encoded) != B64_SHA256:
        raise RuntimeError("encoded payload hash mismatch")

    compressed = base64.b64decode(encoded, validate=True)
    if digest(compressed) != COMPRESSED_SHA256:
        raise RuntimeError("compressed payload hash mismatch")

    raw_tar = lzma.decompress(compressed)
    if digest(raw_tar) != TAR_SHA256:
        raise RuntimeError("tar payload hash mismatch")

    with tarfile.open(fileobj=io.BytesIO(raw_tar), mode="r:") as archive:
        members = archive.getmembers()
        if len(members) != EXPECTED_MEMBERS:
            raise RuntimeError(f"expected {EXPECTED_MEMBERS} files, found {len(members)}")
        for member in members:
            member_path = PurePosixPath(member.name)
            if not member.isfile():
                raise RuntimeError(f"non-regular payload member: {member.name}")
            if member_path.is_absolute() or ".." in member_path.parts:
                raise RuntimeError(f"unsafe payload member: {member.name}")
            if member_path.parts[: len(TARGET_PREFIX.parts)] != TARGET_PREFIX.parts:
                raise RuntimeError(f"unexpected payload path: {member.name}")
            target = (repo / Path(*member_path.parts)).resolve()
            if repo not in target.parents:
                raise RuntimeError(f"payload escaped repository: {member.name}")
            source = archive.extractfile(member)
            if source is None:
                raise RuntimeError(f"missing bytes for payload member: {member.name}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read())

    print("PASS_REVIEWER_B_PAYLOAD_UNPACK")


if __name__ == "__main__":
    main()

# Write-enabled retrigger for PR #708 on 2026-08-21; payload bytes remain unchanged.
