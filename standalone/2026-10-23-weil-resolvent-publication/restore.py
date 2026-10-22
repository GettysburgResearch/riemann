#!/usr/bin/env python3
"""Verify the frozen 48-file delivery; optionally restore into a NEW directory.

Uses only the standard library. Does not run the restored research code.
The archive digest is pinned here; ordinary and optimized Python behave alike.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import sys
import tarfile

ARCHIVE_SHA256 = '8185bfe6f9a5e2899cae78083a2d9e232f7b723d02a76eb88fb6116c0db03646'
ROOT = Path(__file__).resolve().parent
PREFIXES = (
    'standalone/2026-10-22-report-led-boundary-sprint/',
    'standalone/2026-10-22-weil-resolvent-selection/',
    'standalone/2026-10-22-structural-continuation-delivery/',
)

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def unique_object(pairs: list) -> dict:
    out = {}
    for key, value in pairs:
        require(key not in out, 'duplicate JSON key: ' + str(key))
        out[key] = value
    return out

def load(name: str) -> dict:
    return json.loads((ROOT / name).read_text(encoding='utf-8'),
                      object_pairs_hook=unique_object)

def verified_files() -> dict[str, bytes]:
    meta, expected = load('ARCHIVE.json'), load('ORIGINALS.json')
    require(meta['archive_sha256'] == ARCHIVE_SHA256, 'archive pin changed')
    require(len(meta['parts']) == 25, 'wrong part count')
    chunks, seen = [], set()
    for name, size, sha in meta['parts']:
        require(isinstance(name, str) and Path(name).name == name
                and name.startswith('payload.tar.xz.'), 'unsafe part path')
        require(name not in seen, 'duplicate part')
        seen.add(name)
        path = ROOT / name
        require(path.is_file() and not path.is_symlink(), 'missing or linked part: ' + name)
        data = path.read_bytes()
        require(len(data) == size, 'part size mismatch: ' + name)
        actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        require(actual == sha, 'part hash mismatch: ' + name)
        chunks.append(data)
    archive = b''.join(chunks)
    require(len(archive) == 194964 == meta['archive_bytes'], 'archive size mismatch')
    require(hashlib.sha256(archive).hexdigest() == ARCHIVE_SHA256, 'archive hash mismatch')
    require(len(expected) == 48, 'wrong inventory count')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:xz') as tf:
        for member in tf:
            name = member.name
            path = PurePosixPath(name)
            require(member.isfile() and not member.issym() and not member.islnk(),
                    'not a regular file: ' + name)
            require(not path.is_absolute() and '..' not in path.parts
                    and str(path) == name and '\\' not in name
                    and name.startswith(PREFIXES), 'unsafe archive path: ' + name)
            require(name in expected and name not in files, 'unexpected or duplicate member: ' + name)
            size, digest = expected[name]
            require(member.size == size and 0 <= size <= 200000, 'member size mismatch: ' + name)
            stream = tf.extractfile(member)
            require(stream is not None, 'missing member body: ' + name)
            data = stream.read()
            require(len(data) == size and hashlib.sha256(data).hexdigest() == digest,
                    'member hash mismatch: ' + name)
            files[name] = data
    require(set(files) == set(expected), 'incomplete archive')
    require(sum(map(len, files.values())) == 775673 == meta['original_bytes'], 'total bytes mismatch')
    return files

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='New destination; an existing path is refused')
    args = parser.parse_args()
    files = verified_files()
    if args.output is not None:
        require(not args.output.exists() and not args.output.is_symlink(), 'output already exists')
        args.output.mkdir(parents=True, exist_ok=False)
        for name, data in files.items():
            target = args.output.joinpath(*PurePosixPath(name).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as handle:
                handle.write(data)
        print('Restored 48 original files (775673 bytes). No research code executed.')
    else:
        print('Verified 25 archive parts and 48 original files (775673 bytes).')
    return 0

if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, KeyError, TypeError, tarfile.TarError) as exc:
        print('RESTORE REJECTED: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
