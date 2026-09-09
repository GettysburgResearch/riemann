#!/usr/bin/env python3
"""Validate exact delivery coverage and reconstruct the finite arithmetic."""
from hashlib import sha256
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROOF.md', 'README.md', 'SOURCES.md', 'SOURCE_LOCK.json', 'VALIDATION.md',
         'verify.py', 'validate.py', 'test_rejections.py', 'result.json', 'SHA256SUMS'}

def need(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    present = {p.name for p in ROOT.iterdir() if p.is_file()}
    need(present == FILES, 'file coverage mismatch')
    entries = {}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        digest, name = line.split('  ')
        need(name not in entries and name in FILES-{'SHA256SUMS'}, 'bad manifest entry')
        need(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest),
             'bad digest syntax')
        entries[name] = digest
    need(set(entries) == FILES-{'SHA256SUMS'}, 'manifest coverage mismatch')
    for name, digest in entries.items():
        need(sha256((ROOT/name).read_bytes()).hexdigest() == digest,
             'manifest hash mismatch: '+name)
    mode = ['-O'] if sys.flags.optimize else []
    subprocess.run([sys.executable, '-B', *mode, str(ROOT/'verify.py'),
                    '--check', str(ROOT/'result.json')], check=True,
                   stdout=subprocess.DEVNULL)
    print('PASS_HT_DELIVERY_AND_FINITE_ARITHMETIC: 10 files, 9 hashes')


if __name__ == '__main__':
    main()
