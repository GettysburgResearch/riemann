#!/usr/bin/env python3
"""Authenticate the historical nineteen-file packet; optionally extract to a NEW path."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import lzma
import tarfile
from pathlib import Path

SHA256 = '48e7398a17d57ba2e1f07a1bf39caaa318817ab931b6d246c857efea2df7f490'
NAMES = set('CERTIFICATES.json CHECKS.json LOCAL_DOMAIN.md MANIFEST.json MOMENTS_AND_DENSITY.md MUTATIONS.json NEXT_TARGETS.md PROOF.md README.md RECOVERY_AUDIT.json RECOVERY_AUDIT.md SOURCES.md TABLE.json TABLE.md VALIDATION.md local_checks.py run_mutations.py verify.py verify_manifest.py'.split())

def payload(root: Path) -> dict[str, bytes]:
    compressed = b''.join((root / 'parts' / f'part-{i:02}').read_bytes() for i in range(6))
    if hashlib.sha256(compressed).hexdigest() != SHA256:
        raise ValueError('Archive hash mismatch')
    files: dict[str, bytes] = {}
    with tarfile.open(fileobj=io.BytesIO(lzma.decompress(compressed)), mode='r:') as archive:
        for member in archive:
            if not member.isfile() or member.name not in NAMES or member.name in files:
                raise ValueError(f'Unsafe or unexpected member: {member.name!r}')
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError('Missing member data')
            files[member.name] = stream.read()
    if set(files) != NAMES:
        raise ValueError('Incomplete archive')
    return files

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New directory; existing paths are refused')
    args = parser.parse_args()
    files = payload(Path(__file__).resolve().parent)
    if args.output is not None:
        args.output.mkdir(parents=True, exist_ok=False)
        for name, data in files.items():
            (args.output / name).write_bytes(data)
    print(json.dumps({'verified_original_files': len(files), 'archive_sha256': SHA256,
                      'extracted_to': str(args.output) if args.output else None,
                      'executed_recovered_code': False}, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
