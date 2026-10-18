#!/usr/bin/env python3
"""Authenticate the original fourteen files and optionally restore to a NEW directory."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import lzma
from pathlib import Path
import tarfile

ARCHIVE = '802088f4f03ab066532d0a60778db0d3ef90db82abdd0206aca279d49b42cb8e'
TREE = '3dacc1583090517a0ccec3008904d11ccd6d1166'
NAMES = {'.gitattributes','CHECKS.json','MANIFEST.json','MUTATIONS.json',
         'PROOF.md','README.md','REVIEW_AND_LIMITS.md','SOURCES_AND_RECOVERY.md',
         'STRATA.json','VALIDATION.md','replay.py','run_mutations.py','verify.py',
         'verify_manifest.py'}

def git_hash(kind: str, data: bytes) -> str:
    return hashlib.sha1(kind.encode()+b' '+str(len(data)).encode()+b'\0'+data).hexdigest()

def payload(root: Path) -> dict[str, bytes]:
    data = b''.join((root/'parts'/f'part-{i:02}').read_bytes() for i in range(4))
    if hashlib.sha256(data).hexdigest() != ARCHIVE:
        raise ValueError('archive hash mismatch')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(lzma.decompress(data)), mode='r:') as ar:
        for member in ar:
            if not member.isfile() or member.name not in NAMES or member.name in files:
                raise ValueError('unexpected archive member')
            handle = ar.extractfile(member)
            if handle is None:
                raise ValueError('missing archive member')
            files[member.name] = handle.read()
    if set(files) != NAMES:
        raise ValueError('incomplete payload')
    tree = b''.join(b'100644 '+name.encode()+b'\0'+bytes.fromhex(git_hash('blob',files[name]))
                    for name in sorted(files))
    if git_hash('tree',tree) != TREE:
        raise ValueError('original Git tree mismatch')
    manifest = json.loads(files['MANIFEST.json'])['files']
    if set(manifest) != NAMES-{'MANIFEST.json'}:
        raise ValueError('manifest member mismatch')
    for name, record in manifest.items():
        b = files[name]
        actual = (len(b),hashlib.sha256(b).hexdigest(),git_hash('blob',b))
        expected = (record['size'],record['sha256'],record['git_blob'])
        if actual != expected:
            raise ValueError('original manifest mismatch: '+name)
    return files

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    files = payload(Path(__file__).resolve().parent)
    if args.output is not None:
        args.output.mkdir(parents=True,exist_ok=False)
        for name,data in files.items():
            (args.output/name).write_bytes(data)
    print(json.dumps({'authenticated_files':len(files),'original_tree':TREE,
                      'archive_sha256':ARCHIVE,'executed_restored_code':False},indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
