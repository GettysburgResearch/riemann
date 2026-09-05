#!/usr/bin/env python3
"""Validate the two-pass handoff, its tables, and immutable first-pass bytes.
No remote source/primitive computation is performed here.
"""
from pathlib import Path
import csv, hashlib, json, re

ROOT=Path(__file__).resolve().parent
FILES={'CLAIMS.tsv','COVERAGE.tsv','EDGES.tsv','README.md','REPAIRS.md','REPORT.md',
       'SOURCES.tsv','VALIDATION.md','checks.py','checks.normal.json','checks.optimized.json',
       'rejections.py','rejections.json','validate.py','package_rejections.json','SHA256SUMS'}
PARENT_MANIFEST='99c1b6bacfc8bff9e433cc3065d01655d7f473a4cfc6ac89e5334396a92f8ac0'
def require(x,msg):
    if not x:raise ValueError(msg)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def hashes(root,expected=None):
    manifest=root/'SHA256SUMS';names=set()
    for line in manifest.read_text().splitlines():
        h,name=line.split('  ',1)
        require(re.fullmatch('[0-9a-f]{64}',h),'hash syntax')
        require(name not in names and '/' not in name and name not in {'.','..'},'hash path')
        names.add(name)
        require((root/name).is_file() and not (root/name).is_symlink(),'missing or symbolic file')
        require(digest(root/name)==h,'digest mismatch: '+name)
    present={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
    require(present==names|{'SHA256SUMS'},'manifest file coverage')
    if expected is not None: require(present==expected,'required file coverage')
    return len(names)
def rows(name):
    with (ROOT/name).open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def main():
    parent=ROOT.parent/'D'
    require(digest(parent/'SHA256SUMS')==PARENT_MANIFEST,'original D manifest changed')
    require(hashes(parent)==15,'original file count')
    count=hashes(ROOT,FILES)
    sources=rows('SOURCES.tsv');claims=rows('CLAIMS.tsv');edges=rows('EDGES.tsv');coverage=rows('COVERAGE.tsv')
    require((len(sources),len(claims),len(edges),len(coverage))==(39,40,61,28),'table count')
    ids={r['source_id'] for r in sources};uids={r['review_id'] for r in claims}
    require(len(ids)==39 and len(uids)==40,'duplicate table IDs')
    require(len({r['edge_id'] for r in edges})==61,'duplicate edge IDs')
    for row in sources:
        for key in ['commit_sha','blob_sha']:
            require(re.fullmatch('[0-9a-f]{40}',row[key]),'source SHA syntax')
        require(row['path'] and row['inspection'] and row['note'],'source boundary missing')
    oldids={r['source_id'] for r in csv.DictReader((parent/'SOURCES.tsv').open(),delimiter='\t')}
    for row in claims:
        require(row['reason'] and row['required_action'] and row['evidence'],'missing review reasoning')
        for ident in row['sources'].split(';'):
            require(ident in ids or (ident.startswith('../D/') and ident[5:] in oldids),'unknown source '+ident)
    for row in edges:
        require(all(ident in uids for ident in row['review_units'].split(';')),'unknown edge review unit')
    canonical=[r for r in coverage if r['canonical_claim_count']]
    require(len(canonical)==24 and sum(int(r['canonical_claim_count']) for r in canonical)==139,'canonical denominator')
    require((ROOT/'checks.normal.json').read_bytes()==(ROOT/'checks.optimized.json').read_bytes(),'mode mismatch')
    result=json.loads((ROOT/'checks.normal.json').read_text())
    require(result['named_checks']==35 and result['fixtures']==26407,'bounded check scope')
    reject=json.loads((ROOT/'rejections.json').read_text())
    require(all(reject[k]['rejected']==8 and all(x['rejected'] is True for x in reject[k]['cases']) for k in ['normal','optimized']),'rejection scope')
    package=json.loads((ROOT/'package_rejections.json').read_text())
    require(len(package)==8 and all(x['rejected'] is True for x in package),'package refusal records')
    print(json.dumps({'status':'PASS_D_FINAL_MANIFEST','original_D_unchanged':True,
        'new_files':len(FILES),'new_hashes':count,'new_review_units':40,'new_edges':61,
        'source_inspection_records':39,'canonical_denominator':139},sort_keys=True))
if __name__=='__main__':main()
