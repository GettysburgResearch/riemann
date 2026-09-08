#!/usr/bin/env python3
"""Authenticate this packet's bytes; optional parent-file authentication."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

EXPECTED = {
 'PROOF.md','ATTEMPT_AND_REVIEW.md','README.md','EXTERNAL_INPUTS.md',
 'CLAIMS.tsv','SOURCES.json','checks.py','checks.normal.json','checks.optimized.json',
 'validate.py','test_rejections.py','rejections.normal.json','rejections.optimized.json',
 'VALIDATION.md','SHA256SUMS'
}

def require(ok, msg):
    if not ok: raise ValueError(msg)


def unique_pairs(items):
    d={}
    for k,v in items:
        require(k not in d,'duplicate JSON key')
        d[k]=v
    return d


def validate(root: Path, repo: Path | None):
    require(not root.is_symlink(),'symlink packet')
    found=set()
    for p in root.rglob('*'):
        require(not p.is_symlink(),'symlink member')
        if p.is_file(): found.add(p.relative_to(root).as_posix())
    require(found==EXPECTED,'missing or extra inventory')
    lines=(root/'SHA256SUMS').read_text().splitlines()
    seen=set()
    for line in lines:
        digest,name=line.split('  ',1)
        require(name in EXPECTED-{'SHA256SUMS'} and name not in seen,'bad manifest coverage')
        require(len(digest)==64 and set(digest)<=set('0123456789abcdef'),'bad digest')
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'file hash mismatch: '+name)
        seen.add(name)
    require(seen==EXPECTED-{'SHA256SUMS'},'incomplete manifest')
    sources=json.loads((root/'SOURCES.json').read_text(),object_pairs_hook=unique_pairs)
    require(sources['status']=='RH_NOT_PROVED','wrong scope status')
    parents=0
    if repo:
        for row in sources['sources']:
            p=repo/row['path']
            require(not p.is_symlink(),'parent symlink')
            b=p.read_bytes()
            require(len(b)==row['bytes'],'parent size')
            require(hashlib.sha256(b).hexdigest()==row['sha256'],'parent hash')
            require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==row['git_blob'],'parent blob')
            parents+=1
    return {'status':'PASS_PACKET_BYTES','files':len(EXPECTED),'manifest_entries':len(seen),
            'parent_files_authenticated':parents,'mathematical_acceptance':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repo-root',type=Path)
    a=ap.parse_args()
    print(json.dumps(validate(Path(__file__).parent,a.repo_root),sort_keys=True))
