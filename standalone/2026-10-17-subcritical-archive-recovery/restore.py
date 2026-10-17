#!/usr/bin/env python3
"""Verify the lossless historical packet, optionally extract into a NEW directory."""
from __future__ import annotations
import argparse, hashlib, io, json, lzma, tarfile
from pathlib import Path

ARCHIVE_SHA256 = 'b62d32003291be5b24d57d79232463d1853aed7a860668ecdc60753e22172c30'
NAMES = {'AUDIT.md','CHECKS.json','MANIFEST.json','MUTATIONS.json','PROOF.md',
         'README.md','SOURCES.md','SOURCE_ADAPTER.md','TABLE.md','VALIDATION.md',
         'run_mutations.py','verify.py','verify_manifest.py'}

def payload(root: Path) -> dict[str, bytes]:
    compressed = b''.join((root/'parts'/f'part-{i:02}').read_bytes() for i in range(4))
    if hashlib.sha256(compressed).hexdigest() != ARCHIVE_SHA256:
        raise ValueError('Archive hash mismatch')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(lzma.decompress(compressed)), mode='r:') as ar:
        for m in ar:
            if not m.isfile() or m.name not in NAMES or m.name in files:
                raise ValueError(f'Unexpected archive member: {m.name!r}')
            f = ar.extractfile(m)
            if f is None:
                raise ValueError('Missing member data')
            files[m.name] = f.read()
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
            (args.output/name).write_bytes(data)
    print(json.dumps({'verified_original_files':len(files), 'archive_sha256':ARCHIVE_SHA256,
                      'extracted_to': str(args.output) if args.output else None,
                      'executed_recovered_code':False}, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
