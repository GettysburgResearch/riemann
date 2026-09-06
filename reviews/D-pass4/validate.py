#!/usr/bin/env python3
"""Authenticate retained files and result semantics, not a primitive replay."""
from __future__ import annotations
import csv,hashlib,json,re,sys
from pathlib import Path
sys.dont_write_bytecode=True
from checks import Failure,need,read,p61_contract
ROOT=Path(__file__).resolve().parent
OLD={'D':'d3a136e4558b574c906ca679793bf9b67389278d','D-final':'5b37dae592cb49614f8e9b5819d53aea0eb0ea16','D-pass3':'e0ec904c81b2d080a2a42abef35e7987254040cc'}
def object_hash(kind,data):return hashlib.sha1(kind.encode()+b' '+str(len(data)).encode()+b'\0'+data).hexdigest()
def tree_hash(path):
    entries=[]
    for p in sorted(path.iterdir(),key=lambda p:p.name.encode()):
        need(p.is_file() and not p.is_symlink(),'unexpected old directory/symlink')
        entries.append(b'100644 '+p.name.encode()+b'\0'+bytes.fromhex(object_hash('blob',p.read_bytes())))
    return object_hash('tree',b''.join(entries))
def validate(root=ROOT):
    lines=(root/'SHA256SUMS').read_text().splitlines();seen=set()
    for line in lines:
        digest,name=line.split('  ',1)
        need(bool(re.fullmatch('[0-9a-f]{64}',digest)) and name not in seen,'manifest syntax')
        need('/' not in name and name not in {'','..','SHA256SUMS'},'manifest path');seen.add(name)
        p=root/name;need(p.is_file() and not p.is_symlink(),'missing file/symlink')
        need(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'hash mismatch '+name)
    need({p.name for p in root.iterdir()}==seen|{'SHA256SUMS'},'unexpected/missing inventory')
    for name,expected in OLD.items():need(tree_hash(root.parent/name)==expected,'predecessor changed '+name)
    a=read(root/'checks.normal.json');b=read(root/'checks.optimized.json')
    need(a==b and a['schema']=='reviewer-D.pass4.checks.v1' and a['status']=='PASS','bounded check outputs')
    need(a['named_checks']==14 and len(a['records'])==14 and a['bounded_fixtures']==6253,'bounded counts')
    need(sum(x['fixtures'] for x in a['records'])==6253 and a['RH_proved'] is False and a['primitive_Pick_values_recomputed'] is False,'bounded scopes')
    x=read(root/'p61.full.json');y=read(root/'p61.clang.json');p61_contract(x);p61_contract(y);need(x==y,'P61 outputs')
    rows=lambda f:list(csv.DictReader((root/f).open(),delimiter='\t'))
    need(len(rows('CLAIMS.tsv'))==30 and len(rows('EDGES.tsv'))==35,'ledger counts')
    src=rows('SOURCES.tsv');need(len(src)==29 and len({r['source_id'] for r in src})==29,'source count')
    for r in src:
        need(bool(re.fullmatch('[0-9a-f]{40}',r['source_sha'])) and bool(re.fullmatch('[0-9a-f]{40}',r['source_blob'])),'source hash syntax')
    need(sum(int(r['canonical_claim_count']) for r in rows('COVERAGE.tsv') if r['canonical_claim_count'])==139,'canonical coverage count')
    need(len(rows('INTEGRATOR_ACTIONS.tsv'))==18,'action count')
    return {'status':'PASS_D4_PACKAGE','new_files':len(seen)+1,'old_packets_authenticated':3,'claims':30,'edges':35,'source_records':29,'primitive_replay_performed_by_validator':False}
if __name__=='__main__':
    try:print(json.dumps(validate(),sort_keys=True))
    except (Failure,ValueError,KeyError,OSError,TypeError) as e:print('REJECTED:',e,file=sys.stderr);raise SystemExit(2)
