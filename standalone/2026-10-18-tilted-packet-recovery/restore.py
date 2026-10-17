#!/usr/bin/env python3
"""Restore authenticated historical research files; never execute their code."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path
import shutil
import tarfile
import tempfile

ARCHIVE_SHA = 'e2161170738aece61d4b4ae50b33c69ea3af9a308d963e4f1815b975081bd860'
TREE_SHA = '41b9a88ffefc1bef154f5c6ea7d62fce5dd73c72'
NAMES = frozenset('CHECKS.json COMPOSITION.md CONCURRENT.md DETAILED_CERTIFICATE.json MANIFEST.json METHOD_FLOOR.md MUTATIONS.json PARAMETERS.json PARENT_REPLAY.json PUBLISH.md README.md SOURCES.md SOURCE_LOCK.json TILTED_MOMENTS.md VALIDATION.md replay.py verify.py verify_manifest.py'.split())

def blob(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()

def restore(destination: Path) -> None:
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('Refusing existing destination: ' + str(destination))
    here = Path(__file__).resolve().parent
    archive = b''.join((here / ('packet.part' + str(i))).read_bytes() for i in range(4))
    if len(archive) != 28444 or hashlib.sha256(archive).hexdigest() != ARCHIVE_SHA:
        raise ValueError('Archive authentication failed')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:xz') as tar:
        for member in tar.getmembers():
            if not member.isfile() or member.name not in NAMES or member.name in files:
                raise ValueError('Unexpected archive member: ' + member.name)
            if member.size > 1000000:
                raise ValueError('Oversized member')
            stream = tar.extractfile(member)
            if stream is None:
                raise ValueError('Missing regular-file data')
            files[member.name] = stream.read()
    if set(files) != NAMES:
        raise ValueError('Incomplete file inventory')
    payload = b''.join(b'100644 ' + name.encode() + b'\0' + bytes.fromhex(blob(files[name])) for name in sorted(files))
    tree = hashlib.sha1(b'tree ' + str(len(payload)).encode() + b'\0' + payload).hexdigest()
    if tree != TREE_SHA:
        raise ValueError('Original Git tree differs')
    records = json.loads(files['MANIFEST.json'])['files']
    if {record['path'] for record in records} != NAMES - {'MANIFEST.json'} or len(records) != 17:
        raise ValueError('Manifest inventory differs')
    for record in records:
        data = files[record['path']]
        if len(data) != record['bytes'] or blob(data) != record['git_blob'] or hashlib.sha256(data).hexdigest() != record['sha256']:
            raise ValueError('Manifest mismatch: ' + record['path'])
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix='.tilted-recovery-', dir=destination.parent))
    try:
        for name, data in files.items():
            (temporary / name).write_bytes(data)
        if destination.exists() or destination.is_symlink():
            raise FileExistsError('Destination appeared during restoration')
        temporary.rename(destination)
    except BaseException:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    print(json.dumps({'files': len(files), 'git_tree': tree, 'destination': str(destination), 'executed_recovered_code': False}, sort_keys=True))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    restore(parser.parse_args().output)
