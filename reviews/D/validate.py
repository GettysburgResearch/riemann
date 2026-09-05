#!/usr/bin/env python3
"""Validate the frozen Reviewer D packet and ledger coverage; not mathematical proof."""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sys

EXPECTED={
    'README.md','REPORT.md','REPAIRS.md','CLAIMS.tsv','EDGES.tsv','COVERAGE.tsv',
    'SOURCES.tsv','VALIDATION.md','checks.py','checks.normal.json',
    'checks.optimized.json','rejection_checks.py','rejections.json',
    'validate.py','package_rejections.json','SHA256SUMS',
}
MAIN='8d16f8d9c475db290bc85e53d775b93b9bcdb336'


def require(condition: bool,message: str) -> None:
    if not condition:
        raise ValueError(message)


def strict_json(path: Path):
    def pairs(items):
        result={}
        for k,v in items:
            require(k not in result,'duplicate JSON key')
            result[k]=v
        return result
    def refuse(value):
        raise ValueError('unexpected JSON noninteger numeric constant: '+value)
    return json.loads(path.read_text(),object_pairs_hook=pairs,
                      parse_float=refuse,parse_constant=refuse)


def rows(root: Path,name: str):
    with (root/name).open(newline='') as handle:
        result=list(csv.DictReader(handle,delimiter='\t'))
    require(bool(result) and all(None not in r for r in result),'malformed TSV '+name)
    return result


def validate(root: Path) -> None:
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    require(actual==EXPECTED,'exact packet file coverage')
    lines=(root/'SHA256SUMS').read_text().splitlines()
    seen=set()
    for line in lines:
        digest,name=line.split('  ',1)
        require(re.fullmatch('[0-9a-f]{64}',digest) is not None,'malformed checksum')
        require(name in EXPECTED-{'SHA256SUMS'} and name not in seen,'checksum path coverage')
        seen.add(name)
        require(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'checksum mismatch: '+name)
    require(seen==EXPECTED-{'SHA256SUMS'},'manifest coverage')
    sources=rows(root,'SOURCES.tsv');claims=rows(root,'CLAIMS.tsv')
    edges=rows(root,'EDGES.tsv');coverage=rows(root,'COVERAGE.tsv')
    require((len(sources),len(claims),len(edges),len(coverage))==(67,74,62,28),'ledger counts')
    sid={r['source_id'] for r in sources};uid={r['review_id'] for r in claims}
    require(len(sid)==67 and len(uid)==74,'duplicate source/unit IDs')
    require(len({r['edge_id'] for r in edges})==62,'duplicate edge IDs')
    for source in sources:
        for key in ['commit_sha','blob_sha']:
            require(re.fullmatch('[0-9a-f]{40}',source[key]) is not None,'source SHA shape')
    for claim in claims:
        require(set(claim['sources'].split(';'))<=sid,'unknown source ID')
    for edge in edges:
        require(set(edge['review_units'].split(';'))<=uid,'unknown edge review unit')
    canonical=[r for r in coverage if r['canonical_claim_count']!='']
    require(len(canonical)==24 and sum(int(r['canonical_claim_count']) for r in canonical)==139,'canonical denominator')
    for row in coverage:
        require(not row['review_units'] or set(row['review_units'].split(';'))<=uid,'unknown coverage unit')
    normal=(root/'checks.normal.json').read_bytes()
    require(normal==(root/'checks.optimized.json').read_bytes(),'mode outputs differ')
    result=strict_json(root/'checks.normal.json')
    require(result['rh_proved'] is False and result['upstream_producers_executed'] is False,'incorrect scientific flag')
    require(result['main_sha']==MAIN,'baseline mismatch')
    require(result['named_checks']==45 and type(result['named_checks']) is int,'check count')
    require(result['fixture_count']==9380 and type(result['fixture_count']) is int,'fixture count')
    require(len(result['checks'])==45 and len({r['name'] for r in result['checks']})==45,'named check coverage')
    require(sum(r['fixtures'] for r in result['checks'])==9380,'fixture accounting')
    require(result['script_sha256']==hashlib.sha256((root/'checks.py').read_bytes()).hexdigest(),'checker binding')
    refusals=strict_json(root/'rejections.json')
    require(refusals['count']==12 and refusals['all_expected_refusals'] is True,'checker refusal count')
    require(refusals['checker_sha256']==result['script_sha256'],'refusal checker binding')
    require(refusals['driver_sha256']==hashlib.sha256((root/'rejection_checks.py').read_bytes()).hexdigest(),'refusal driver binding')
    require(all(r['returncode']==2 for r in refusals['rows']) and len(refusals['rows'])==12,'refusal outcomes')
    extra=strict_json(root/'package_rejections.json')
    require(extra['count']==4 and len(extra['rows'])==4,'packet refusal count')
    require(extra['validator_sha256']==hashlib.sha256((root/'validate.py').read_bytes()).hexdigest(),'validator binding')
    require(all(r['returncode']==2 for r in extra['rows']),'packet refusal outcomes')
    print('PASS_REVIEWER_D_PACKET: 74 units; 62 edges; 67 pins; 45 checks / 9380 fixtures; 16 refusals')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parent)
    args=parser.parse_args()
    try:
        validate(args.root.resolve())
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print('REJECT_PACKET: '+str(exc),file=sys.stderr)
        sys.exit(2)
