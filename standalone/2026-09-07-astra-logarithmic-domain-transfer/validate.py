#!/usr/bin/env python3
"""Byte inventory and bounded claims gates. Not a proof of RH or the paper."""
from __future__ import annotations
import csv
import hashlib
import re
from pathlib import Path
import checks

ROOT=Path(__file__).resolve().parent
FILES=frozenset('''ABEL_AND_ATTEMPT.md CLAIMS.tsv EDGES.tsv EXTERNAL_INPUTS.md PROOF.md
README.md REVIEW.md SHA256SUMS SOURCES.json VALIDATION.md checks.py checks.normal.json
checks.optimized.json rejections.py rejections.json validate.py'''.split())
BASE='0f6ee91f1a8c8bece1618bde155d62fb0bfb4cad'
SOURCE_PINS={
 'supplied_OE26':('310cf1dc40694d053ec955c2ad404eaec35fa7ed','070574df29d3b5a3f92628c43092271675b5a35249cdc9cbd268bab55e420fbe',18207),
 'CSM26':('593d99995f70c3cb565aebbfb455f93147d09e1e','5e1805229509e0567f88bddb9ce29adefe5d1cc2662ebac82d35e7aed10c05e8',12266),
 'MWR26':('f51ee8c99e3b5b5c8d8b8c325f346474c549200c','d6825b78304b5a69aba5cde008a18551034fc14390a974efdeae4b4645d88307',10327)}
STATUSES={'OEC26.T1':'PROPOSED_PROVED','OEC26.T2':'PROPOSED_PROVED',
 'OEC26.T3':'PROPOSED_PROVED','OEC26.T4':'CONDITIONAL_PROVED',
 'OEC26.C1':'PROPOSED_EQUIVALENCE','OEC26.T5':'CONDITIONAL_PROVED',
 'OEC26.C2':'PROPOSED_PROVED','OEC26.OPEN':'OPEN_RH_EQUIVALENT'}

def validate() -> dict:
    actual=set()
    for p in ROOT.iterdir():
        if p.name=='__pycache__':
            continue
        checks.require(not p.is_symlink() and p.is_file(),'non-regular packet entry')
        actual.add(p.name)
    checks.require(actual==FILES,'exact packet inventory mismatch')
    manifest={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        match=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)',line)
        checks.require(match is not None,'bad checksum syntax')
        digest,name=match.groups()
        checks.require(name not in manifest,'duplicate checksum')
        manifest[name]=digest
    checks.require(set(manifest)==FILES-{'SHA256SUMS'},'manifest coverage mismatch')
    for name,digest in manifest.items():
        checks.require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,
                       'checksum mismatch: '+name)
    source=checks.strict_json(ROOT/'SOURCES.json')
    checks.require(source['remote_baseline_commit']==BASE,'changed remote baseline')
    checks.require(source['unconditional_RH_claimed'] is False,'false proof promotion')
    checks.require({x['name']:(x['git_blob'],x['sha256'],x['bytes']) for x in source['sources']}==SOURCE_PINS,
                   'changed source identity')
    claims=list(csv.DictReader((ROOT/'CLAIMS.tsv').open(),delimiter='\t'))
    checks.require(len(claims)==8 and {x['claim']:x['status'] for x in claims}==STATUSES,
                   'claim count or status mismatch')
    edges=list(csv.DictReader((ROOT/'EDGES.tsv').open(),delimiter='\t'))
    checks.require(len(edges)==11,'edge count mismatch')
    expected=checks.run()
    for name in ['checks.normal.json','checks.optimized.json']:
        checks.require(checks.same(checks.strict_json(ROOT/name),expected),'result reconstruction mismatch')
    return {'verdict':'PASS_OEC26_BYTE_AND_BOUNDED_CHECKS','files':len(FILES),
            'sha256_entries':len(manifest),'claims':len(claims),'edges':len(edges),
            'groups':expected['named_groups'],'bounded_fixtures':expected['bounded_fixtures'],
            'analytic_proofs_machine_verified':False,'RH_proved':False}

if __name__=='__main__':
    import json
    try:
        print(json.dumps(validate(),sort_keys=True))
    except (ValueError,OSError,KeyError,TypeError) as exc:
        raise SystemExit('REJECT: '+str(exc))
