"""Verify every sealed payload's bytes, SHA-256 and Git blob identity."""
import hashlib
import json
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / 'MANIFEST.json').read_text(encoding='utf-8'))
    for name, expected in manifest['files'].items():
        path = here / name
        if path.parent != here or not path.is_file():
            raise ValueError('Missing or unsafe payload: ' + name)
        data = path.read_bytes()
        actual = {
            'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest(),
        }
        if actual != expected:
            raise ValueError('Payload mismatch: ' + name)
    print(json.dumps({'status': 'PASS', 'authenticated_payloads': len(manifest['files'])}, sort_keys=True))


if __name__ == '__main__':
    main()
