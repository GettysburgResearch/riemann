#!/usr/bin/env python3
"""Fail-closed local registry, status and content-manifest validation."""
from pathlib import Path
import csv, hashlib, json, re, sys
ROOT=Path(__file__).resolve().parents[1]
def table(name):
    with (ROOT/name).open() as f:return list(csv.DictReader(f,delimiter='\t'))
def need(test,msg):
    if not test:raise RuntimeError(msg)
def main():
    required=['REPORT.md','MATHEMATICAL_AUDIT.md','CLAIMS.tsv','EDGES.tsv','SOURCES.tsv','SOURCE_LOCK.json',
              'PR_SOURCE_CENSUS.tsv','FIXES_AND_EXTRACTION.md','OMISSIONS.md','CROSS_REVIEW_QUESTIONS.md',
              'UPLOAD_HANDOFF.md','PACKET_COUNTS.json','prior-pass/REPORT.md','prior-pass/CLAIMS.tsv',
              'prior-pass/EDGES.tsv','prior-pass/FIXES_AND_EXTRACTION.md','replay/result.json',
              'replay/EXECUTION_RECEIPT.json','SHA256SUMS']
    for p in required:need((ROOT/p).is_file() and (ROOT/p).stat().st_size>0,'missing '+p)
    s=table('SOURCES.tsv'); c=table('CLAIMS.tsv'); e=table('EDGES.tsv'); p=table('PR_SOURCE_CENSUS.tsv')
    sources={r['source_id']:r for r in s};need(len(sources)==len(s),'source ID collision')
    need(len({r['review_id'] for r in c})==len(c),'review ID collision')
    need(len({r['edge_id'] for r in e})==len(e),'edge ID collision')
    for row in s:
        need(bool(re.fullmatch('[0-9a-f]{40}',row['commit_sha'])),'bad source SHA')
        need(bool(re.fullmatch('[0-9a-f]{40}',row['git_blob'])),'bad source blob')
        need(row['path'] and not row['path'].startswith('/'),'nonrelative source path')
    for row in c:
        need(row['source_id'] in sources,'unregistered claim source')
        z=sources[row['source_id']]
        need(row['source_sha']==z['commit_sha'] and row['source_path']==z['path'] and row['source_blob']==z['git_blob'],'source mismatch')
        anchor=row['proof_review'].split('#')[-1]
        need('id="'+anchor+'"' in (ROOT/'MATHEMATICAL_AUDIT.md').read_text(),'missing mathematical review anchor')
    counts=json.loads((ROOT/'PACKET_COUNTS.json').read_text())
    need(counts['source_files']==len(s) and counts['claim_dispositions']==len(c) and counts['hyperedges']==len(e),'count mismatch')
    need(counts['rh_proved'] is False,'RH status altered')
    rec=json.loads((ROOT/'replay/EXECUTION_RECEIPT.json').read_text())
    need(rec['status']=='PASS' and rec['normal_optimized_byte_identical'] is True,'replay not passed')
    need(rec['rh_proved'] is False and rec['upstream_campaigns_rerun'] is False,'computation scope altered')
    manifest={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,name=line.split('  ',1);need(name not in manifest,'duplicate manifest path');manifest[name]=h
        need(not Path(name).is_absolute() and '..' not in Path(name).parts,'unsafe manifest path')
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'hash mismatch '+name)
    files={str(f.relative_to(ROOT)) for f in ROOT.rglob('*') if f.is_file() and f.name!='SHA256SUMS' and '__pycache__' not in f.parts}
    need(set(manifest)==files,'manifest does not cover exactly the packet')
    print(json.dumps({'status':'PASS_REVIEWER_A_PACKET','sources':len(s),'claim_dispositions':len(c),'hyperedges':len(e),'pr_pins':len(p),'manifest_files':len(manifest),'rh_proved':False,'exhaustive_allotment_completion_claimed':False},sort_keys=True))
if __name__=='__main__':main()
