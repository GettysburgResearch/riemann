#!/usr/bin/env python3
"""CD26 strict package integrity, inventory and coverage; not an analytic proof."""
from pathlib import Path
import csv,hashlib,json,sys
EXPECTED=set('README.md PROOF.md ATTEMPT.md EXTERNAL_INPUTS.md SOURCES.json CLAIMS.tsv EDGES.tsv REVIEW.md VALIDATION.md certificate.py certificate.json checks.py checks.json validate.py rejections.py rejections.json SHA256SUMS'.split())

def verify(root):
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    if actual!=EXPECTED:raise ValueError('unexpected package inventory')
    records={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        h,n=line.split('  ',1)
        if n in records or n not in EXPECTED-{'SHA256SUMS'}:raise ValueError('bad manifest member')
        if len(h)!=64 or any(c not in '0123456789abcdef' for c in h):raise ValueError('bad digest')
        records[n]=h
    if set(records)!=EXPECTED-{'SHA256SUMS'}:raise ValueError('incomplete manifest')
    for n,h in records.items():
        if hashlib.sha256((root/n).read_bytes()).hexdigest()!=h:raise ValueError('hash mismatch: '+n)
    c=json.loads((root/'certificate.json').read_text())
    if c['orders']!=[1,2,4,8,16,32,64,128] or c['tail_start_Y']!=32768:raise ValueError('wrong coverage')
    if len(c['rows'])!=8:raise ValueError('wrong row count')
    for N,r in zip(c['orders'],c['rows']):
        if type(r['N']) is not int or r['N']!=N or r['complete_integrated_cells']!=32768-N-1 or r['exact_zero_cells']!=N:raise ValueError('wrong cells')
        if r['complete_infinite_tail'] is not True or r['b']!='1/2' or r['target']!='t*exp(-t/2)':raise ValueError('wrong source')
    if c['RH_proved'] is not False or c['domain_completed'] is not False:raise ValueError('false promotion')
    k=json.loads((root/'checks.json').read_text())
    if len(k['checks'])!=k['named_checks'] or sum(r['fixtures'] for r in k['checks'])!=k['fixtures']:raise ValueError('incorrect control counts')
    claims=list(csv.DictReader((root/'CLAIMS.tsv').open(),delimiter='\t'))
    if len(claims)!=8 or claims[-1]['status']!='OPEN':raise ValueError('claim scope')
    return {'schema':'CD26.package.v1','authenticated_files':len(records),'inventory_files':len(actual),'status':'PASS_INTEGRITY_ONLY'}

def main():
    try:r=verify(Path(__file__).resolve().parent);code=0
    except Exception as e:r={'status':'REJECTED','reason':str(e)};code=2
    print(json.dumps(r,sort_keys=True));return code
if __name__=='__main__':sys.exit(main())
