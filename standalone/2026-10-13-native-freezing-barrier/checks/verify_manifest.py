#!/usr/bin/env python3
"""Authenticate packet bytes, not mathematical claims."""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path


def main() -> None:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    manifest = json.loads((root / 'MANIFEST.json').read_text())
    for entry in manifest['files']:
        relative = Path(entry['path'])
        if relative.is_absolute() or '..' in relative.parts:
            raise RuntimeError('unsafe manifest path')
        data = (root / relative).read_bytes()
        actual = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                  'git_blob': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}
        for key, value in actual.items():
            if entry[key] != value:
                raise RuntimeError(f"{relative}: {key} mismatch")
    print(json.dumps({'status': 'PASS', 'files': len(manifest['files']),
                      'scope': 'byte identity only'}, sort_keys=True))


if __name__ == '__main__':
    main()
