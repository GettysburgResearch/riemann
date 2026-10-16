#!/usr/bin/env python3
"""Fetch the versioned original papers; no overwrite and no implicit build.

Not network-executed during this research pass. Hashes computed here bind the
newly fetched bytes, not an independently authenticated earlier full snapshot.
The displayed Hexagon SHA-256 prefixes are checked for the TeX sources.
"""
from __future__ import annotations
import hashlib
import json
import sys
import urllib.request
from pathlib import Path

BASE = 'https://hexagonmath.org'
SOURCES = {
    'DedekindZeta-v1.pdf': (BASE+'/pdf/2610.00200v1', None),
    'DedekindZeta-v2.pdf': (BASE+'/pdf/2610.00200v2', None),
    'DedekindZeta-v1.tex': (BASE+'/api/v1/works/2610.00200v1/source?path=DedekindZeta.tex', 'fe4107a2ac3fd506'),
    'DedekindZeta-v2.tex': (BASE+'/api/v1/works/2610.00200v2/source?path=DedekindZeta.tex', 'f54808ad0f967b54'),
}

def main(destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    targets = [destination/name for name in SOURCES] + [destination/'FETCHED.json']
    if any(path.exists() for path in targets):
        raise FileExistsError('Destination has existing output files; choose a fresh directory.')
    downloaded: dict[str, bytes] = {}
    receipts = {}
    for name, (url, prefix) in SOURCES.items():
        request = urllib.request.Request(url, headers={'User-Agent':'riemann-research-source-import/1.0'})
        with urllib.request.urlopen(request, timeout=60) as response:
            data = response.read(50*1024*1024+1)
        if len(data)>50*1024*1024 or not data:
            raise ValueError(f'Invalid size for {name}')
        if name.endswith('.pdf') and not data.startswith(b'%PDF-'):
            raise ValueError(f'Not a PDF: {name}')
        if name.endswith('.tex') and b'\\documentclass' not in data[:2000]:
            raise ValueError(f'Not the expected TeX source: {name}')
        digest = hashlib.sha256(data).hexdigest()
        if prefix is not None and not digest.startswith(prefix):
            raise ValueError(f'Published hash prefix mismatch for {name}: {digest}')
        downloaded[name]=data
        receipts[name]={'url':url,'bytes':len(data),'sha256':digest,
                        'prechecked_sha256_prefix':prefix,'license':'CC BY 4.0'}
    for name, data in downloaded.items():
        with (destination/name).open('xb') as handle:
            handle.write(data)
    with (destination/'FETCHED.json').open('x',encoding='utf-8') as handle:
        json.dump(receipts,handle,indent=2,sort_keys=True)
        handle.write('\n')
    print(f'Downloaded {len(downloaded)} sources to {destination}; no Lean build was run.')

if __name__ == '__main__':
    try:
        main(Path(sys.argv[1]) if len(sys.argv)>1 else Path('downloaded-upstream'))
    except Exception as exc:
        print(f'Source fetch failed: {exc}',file=sys.stderr)
        raise SystemExit(1) from exc
