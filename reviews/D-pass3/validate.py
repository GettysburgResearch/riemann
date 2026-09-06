#!/usr/bin/env python3
"""Strict inventory, hash and relational checks; not a mathematical proof checker."""
import argparse,csv,hashlib,json,re
from pathlib import Path
EXPECTED={'README.md','REPORT.md','PROOFS_AND_REPAIRS.md','EXTERNAL_INPUTS.md',
'CLAIMS.tsv','EDGES.tsv','COVERAGE.tsv','SOURCES.tsv','VALIDATION.md',
'checks.py','checks.normal.json','checks.optimized.json','validate.py',
'rejections.py','rejections.json','SHA256SUMS'}
def req(ok,msg):
    if not ok:raise ValueError(msg)
def blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def manifest(root,expected=None):
    raw=(root/'SHA256SUMS').read_text();entries={}
    for line in raw.splitlines():
        h,p=line.split('  ',1)
        req(re.fullmatch('[0-9a-f]{64}',h) is not None,'bad hash')
        req('/' not in p and p not in entries and p!='SHA256SUMS','bad or duplicate manifest path')
        entries[p]=h
    actual={p.name for p in root.iterdir()}
    req(actual==set(entries)|{'SHA256SUMS'},'inventory mismatch')
    if expected is not None:req(actual==expected,'expected file set mismatch')
    for p,h in entries.items():
        req((root/p).is_file() and hashlib.sha256((root/p).read_bytes()).hexdigest()==h,'hash mismatch: '+p)
    return len(entries)
def table(root,p):return list(csv.DictReader((root/p).open(),delimiter='\t'))
def validate(root,prior=False):
    n=manifest(root,EXPECTED)
    sources=table(root,'SOURCES.tsv');ss={s['source_id']:s for s in sources}
    req(len(sources)==len(ss)==29,'source count')
    for s in sources:
        for f in ['source_sha','source_blob']:req(re.fullmatch('[0-9a-f]{40}',s[f]) is not None,'source SHA')
        req(s['source_path'] and not s['source_path'].startswith('/'),'source path')
    claims=table(root,'CLAIMS.tsv');ids={r['review_id'] for r in claims}
    req(len(claims)==len(ids)==42,'claim count or duplicate')
    for r in claims:
        refs=r['source_ids'].split(';');req(set(refs)<=set(ss),'unresolved source')
        s=ss[refs[0]];req(r['source_sha']==s['source_sha'] and r['source_path']==s['source_path'],'primary source mismatch')
        for f in ['source_claim','verdict','scope','reason','required_action','proof_reference']:req(bool(r[f]),'empty disposition')
        req(r['extraction_destination'].startswith('research/integrated/'),'destination')
    edges=table(root,'EDGES.tsv');req(len(edges)==45 and len({e['edge_id'] for e in edges})==45,'edge count')
    for e in edges:req(set(e['review_units'].split(';'))<=ids,'edge unit')
    cov=table(root,'COVERAGE.tsv');req(len(cov)==28,'coverage rows')
    req(sum(int(c['canonical_claim_count'] or 0) for c in cov)==139,'canonical denominator')
    req(sum(bool(c['canonical_claim_count']) for c in cov)==24,'family denominator')
    linked=[u for c in cov for u in c['pass3_units'].split(';') if u]
    req(len(linked)==len(set(linked))==42 and set(linked)==ids,'coverage unit mismatch')
    r1=(root/'checks.normal.json').read_bytes();r2=(root/'checks.optimized.json').read_bytes()
    req(r1==r2,'Python-mode outputs differ')
    data=json.loads(r1);req(data['schema']=='reviewer-D-pass3-controls-v1','result schema')
    req(data['named_checks']==len(data['checks'])==34,'named checks')
    req(sum(c['fixtures'] for c in data['checks'])==data['fixtures']==6999,'fixture count')
    rej=json.loads((root/'rejections.json').read_text())
    req(rej['schema']=='reviewer-D-pass3-rejections-v1','rejection schema')
    req(len(rej['result_mutations'])==8 and len(rej['package_mutations'])==4,'rejection count')
    req(all(x['rejected'] for x in rej['result_mutations']+rej['package_mutations']),'unrejected mutation')
    prior_checked=[]
    if prior:
        anchors={'D':'15796849d2d9141f05375a1997d3b1e74d92dbcb',
                 'D-final':'d756662534a582d9675bb0ba1490e1b2b08438bf'}
        for name,anchor in anchors.items():
            d=root.parent/name
            req(blob((d/'SHA256SUMS').read_bytes())==anchor,'prior published manifest changed')
            req(manifest(d)==15,'prior manifest count');prior_checked.append(name)
    return {'status':'PASS','files':16,'hashes':n,'claims':42,'edges':45,'source_pins':29,
            'named_checks':34,'fixtures':6999,'prior_manifests_authenticated':prior_checked}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--directory',type=Path,default=Path(__file__).resolve().parent);ap.add_argument('--prior',action='store_true');a=ap.parse_args()
    print(json.dumps(validate(a.directory,a.prior),sort_keys=True))
