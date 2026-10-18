"""Verify sealed bytes and the complete top-level payload inventory."""
import hashlib
import json
from pathlib import Path
import re


def identity(data):
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()}


def verify(root=None):
    here = Path(root) if root else Path(__file__).resolve().parent
    manifest = json.loads((here/'MANIFEST.json').read_text(encoding='utf-8'))
    expected = manifest['files']
    for name, record in expected.items():
        if (not isinstance(name, str) or not re.fullmatch(r'[A-Za-z0-9_.-]+', name)
                or name in {'.', '..', 'MANIFEST.json'}):
            raise ValueError('Unsafe or recursive manifest path.')
        path = here/name
        if path.is_symlink() or not path.is_file() or identity(path.read_bytes()) != record:
            raise ValueError('Sealed payload mismatch: '+name)
    actual = {p.name for p in here.iterdir() if p.is_file()}
    if actual != set(expected)|{'MANIFEST.json'}:
        raise ValueError('Unexpected or missing top-level payload: '
                         +str(sorted(actual ^ (set(expected)|{'MANIFEST.json'}))))
    return {'status': 'PASS: sealed bytes and complete payload inventory',
            'authenticated_payloads': len(expected), 'base_commit': manifest['base_commit'],
            'boundary': 'File authentication only; the frozen Git commit authenticates the manifest itself.'}


if __name__ == '__main__':
    print(json.dumps(verify(), sort_keys=True))
