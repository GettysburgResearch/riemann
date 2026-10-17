"""Authenticate and restore the unchanged thirteen-file historical packet."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tarfile

ARCHIVE_SHA256 = '3f6588cd688efc7bd18796896d851c563fd5ad68c507c0117e1b596b386a0d9f'
TREE = '2385ec9053f269f736ee52f54bfd7c1af60d26c5'
NAMES = set(('CHECKS.json INPUTS_AND_REVIEW.md MANIFEST.json MOMENTS.md '
             'MUTATIONS.json PROOF.md README.md RECOVERY_AUDIT.md VALIDATION.md '
             'run_mutations.py strata.json verify.py verify_manifest.py').split())

def oid(kind, data):
    return hashlib.sha1(kind.encode() + b' ' + str(len(data)).encode() + b'\0' + data).digest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--replay', action='store_true', help='Also execute the original manifest and both checker modes.')
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError('Output must not exist; refusing overwrite.')
    here = Path(__file__).resolve().parent
    raw = b''.join((here / f'archive.part{i:02}').read_bytes() for i in range(1, 5))
    if hashlib.sha256(raw).hexdigest() != ARCHIVE_SHA256:
        raise ValueError('Archive digest mismatch.')
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:xz') as archive:
        members = archive.getmembers()
        if len(members) != len(NAMES) or {m.name for m in members} != NAMES:
            raise ValueError('Unexpected or duplicate archive members.')
        if any(not m.isfile() or '/' in m.name or m.size > 200000 for m in members):
            raise ValueError('Unsafe archive member.')
        files = {m.name: archive.extractfile(m).read() for m in members}
    tree = b''.join(b'100644 ' + name.encode() + b'\0' + oid('blob', files[name]) for name in sorted(files))
    if oid('tree', tree).hex() != TREE:
        raise ValueError('Original Git tree mismatch.')
    args.output.mkdir(parents=True)
    for name, data in files.items():
        (args.output / name).write_bytes(data)
    if args.replay:
        subprocess.run([sys.executable, 'verify_manifest.py'], cwd=args.output, check=True)
        for flags in ([], ['-O']):
            out = subprocess.check_output([sys.executable, *flags, 'verify.py'], cwd=args.output)
            if out != files['CHECKS.json']:
                raise ValueError('Historical checker output differs.')
    print(json.dumps({'restored_files': len(files), 'original_tree': TREE, 'replayed': args.replay}, sort_keys=True))

if __name__ == '__main__':
    main()
