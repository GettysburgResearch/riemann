#!/usr/bin/env python3
"""Package integrity only. Mathematical verification is verify.py."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
expected={'PROOF.md','README.md','SOURCES.md','SOURCE_LOCK.json','VALIDATION.md','certificate.json','result.json','checks.json','refusals.json','refusals-optimized.json','intervals.py','verify.py','test_checks.py','test_rejections.py','validate.py'}
rows={}
for line in (ROOT/'SHA256SUMS').read_text().splitlines():
 m=re.fullmatch(r'([0-9a-f]{64})  ([A-Za-z0-9_.-]+)',line)
 if not m or m[2] in rows:raise ValueError('bad or duplicate manifest row')
 rows[m[2]]=m[1]
if set(rows)!=expected:raise ValueError('manifest coverage')
actual={p.name for p in ROOT.iterdir() if p.is_file()}
if actual!=expected|{'SHA256SUMS'}:raise ValueError('directory coverage')
for name,digest in rows.items():
 p=ROOT/name
 if p.is_symlink() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:raise ValueError('hash mismatch: '+name)
from verify import load,reject_pairs
load(ROOT/'certificate.json')
r=json.loads((ROOT/'result.json').read_text(),object_pairs_hook=reject_pairs)
if r.get('rh_proved') is not False or r.get('full_source_positivity') is not True or r.get('source_window')!='1':raise ValueError('scope marker')
if type(r.get('finite_coefficients')) is not int or r['finite_coefficients']!=2049:raise ValueError('coefficient denominator')
print(json.dumps({'status':'PASS_PACKAGE_INTEGRITY_ONLY','manifest_entries':len(rows),'files':len(actual),'rh_proved':False},sort_keys=True))
