#!/usr/bin/env python3
"""Authenticate this exact review packet's bytes and structure, not its mathematics."""
from pathlib import Path, PurePosixPath
import csv
import hashlib
import json
import re
import sys

EXPECTED = ['CLOSING.json', 'DECISIONS.tsv', 'EXECUTION.json', 'EXTRACTION.tsv', 'FILES.tsv', 'IMPORTS.md', 'LICENSE', 'README.md', 'REPAIRS.md', 'REPORT.md', 'SOURCE_HEADS.json', 'VALIDATION.md', 'evidence/cd-normal.json', 'evidence/fr-normal.json', 'evidence/mw-independent-normal.json', 'evidence/mw-normal.json', 'evidence/mw-original-parser.json', 'evidence/replay-tests-normal.json', 'evidence/ssq-normal.json', 'independent_mw.py', 'replay.py', 'sources/CD/certificate.py', 'sources/FR/certificate.py', 'sources/FR/interval_core.py', 'sources/MW/certify.py', 'sources/SSQ/check.py', 'test_mw_original_parser.py', 'test_replay.py', 'verify_packet.py']
SOURCE_BLOBS = {
 'sources/FR/interval_core.py':'92f484bc6bc7b12bf26313bd7d323c637cd834b9',
 'sources/FR/certificate.py':'dbf67ac52636916a59a9c7a11aa87356518143bc',
 'sources/CD/certificate.py':'a0f15cd4fdef7cc6aa24bfea2939e04b08d19525',
 'sources/MW/certify.py':'3d1e3b10135a8504a5d3639b507211014be7eecc',
 'sources/SSQ/check.py':'a8e35ea57c3a5cad5872e5b9d1134ae42ca35e6a'
}
RESULTS = {
 'fr':'ef76ca01c9b32456db9f214f6a210f304f8b10563bbaa7b8f014e32d87d84bcf',
 'cd':'2fb2b2961ad9d6ec1a24fe60a3e05c500ca3a4bd246ce2e1965f80ab046f3ecb',
 'mw':'ddaa01ec89167f7604939711c548ce80e856eb8197bf34b566e69439883dc9d6',
 'ssq':'e7a80214068439ae01bb3714825634dd821480117d6ac1f478546725d2edbe06',
 'mw-independent':'d2e7dc09e44a4f3bd93627ce3081090ef6ff146f8c3b70ded369b792a25ccbb8',
 'replay-tests':'e97b6dec23e8ec4921bc7143a02a687750a322394d38c0337e1efccb7e5163e8'
}

def need(ok, message):
    if not ok: raise ValueError(message)

def validate(root):
    need(root.is_dir() and not root.is_symlink(), 'packet root')
    allowed=set(EXPECTED)|{'SHA256SUMS'}
    directories={str(p) for f in allowed for p in PurePosixPath(f).parents if str(p)!='.'}
    seen=set()
    for path in root.rglob('*'):
        rel=path.relative_to(root).as_posix()
        need(not path.is_symlink(), 'symlink')
        if path.is_dir(): need(rel in directories, 'unexpected directory')
        else:
            need(path.is_file(), 'nonregular file')
            seen.add(rel)
    need(seen==allowed, 'exact file inventory')
    manifest=(root/'SHA256SUMS').read_bytes()
    need(0<len(manifest)<=100000, 'manifest length')
    entries={}
    for line in manifest.decode('ascii').splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_./-]+)',line)
        need(m is not None, 'manifest syntax')
        digest,name=m.groups()
        need(name in EXPECTED and name not in entries, 'manifest path or duplicate')
        entries[name]=digest
    need(set(entries)==set(EXPECTED), 'manifest coverage')
    total=0
    for name,digest in entries.items():
        raw=(root/name).read_bytes(); total+=len(raw)
        need(hashlib.sha256(raw).hexdigest()==digest, 'hash mismatch: '+name)
        if name in SOURCE_BLOBS:
            actual=hashlib.sha1(('blob '+str(len(raw))+'\0').encode()+raw).hexdigest()
            need(actual==SOURCE_BLOBS[name], 'consumed source blob')
    for stem,digest in RESULTS.items():
        need(entries['evidence/'+stem+'-normal.json']==digest, 'selected evidence identity')
    with (root/'EXTRACTION.tsv').open(encoding='utf-8',newline='') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    need(len(rows)==45 and len({r['packet'] for r in rows})==45, 'extraction census')
    with (root/'DECISIONS.tsv').open(encoding='utf-8',newline='') as f:
        decisions=list(csv.DictReader(f,delimiter='\t'))
    need(len(decisions)==22 and len({r['decision'] for r in decisions})==22, 'decision inventory')
    return {'status':'PASS_AUTHENTICATED_FINAL_REVIEW_PACKET',
            'scope':'Byte and table structure only; run replay.py for selected numerical reconstruction.',
            'files':len(allowed),'manifest_entries':len(entries),
            'payload_bytes_excluding_manifest':total,
            'manifest_sha256':hashlib.sha256(manifest).hexdigest(),
            'extraction_packets':45,'final_dispositions':22,'rh_proved':False}

if __name__=='__main__':
    try:
        print(json.dumps(validate(Path(__file__).absolute().parent),sort_keys=True,indent=2))
    except (OSError,UnicodeError,ValueError,KeyError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);raise SystemExit(2)
