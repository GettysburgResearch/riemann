#!/usr/bin/env python3
"""Validate source-qualified final A review inventory and immutable file manifest.
This checks the report package, not the mathematical truth of every disposition.
Run separately from historical replay/validate_packet.py, which targets pass 2.
"""
from pathlib import Path
import csv,hashlib,json,re,sys

def need(test,message):
    if not test: raise RuntimeError(message)
def strict_json(path):
    def pairs(items):
        out={}
        for k,v in items:
            if k in out:raise RuntimeError('duplicate JSON key: '+k)
            out[k]=v
        return out
    return json.loads(path.read_text(),object_pairs_hook=pairs)
def validate(root):
    required=['REPORT.md','CLAIMS.tsv','EDGES.tsv','SOURCES.tsv','FIXES_AND_EXTRACTION.md',
      'FINAL_AUDIT.md','MATHEMATICAL_AUDIT.md','OMISSIONS.md','CROSS_REVIEW_QUESTIONS.md',
      'SOURCE_LOCK.json','FINAL_SCOPE.json','SOURCE_VERSION_DIFFS.tsv','PR_SOURCE_CENSUS.tsv',
      'PACKET_COUNTS.json','final-pass/EXECUTION_RECEIPT.json','SHA256SUMS']
    for n in required:need((root/n).is_file() and (root/n).stat().st_size>0,'missing '+n)
    def rows(n):
        with (root/n).open(newline='') as f:
            out=list(csv.DictReader(f,delimiter='\t'))
        need(all(None not in row and all(v is not None for v in row.values()) for row in out),'ragged table '+n)
        return out
    sources=rows('SOURCES.tsv'); claims=rows('CLAIMS.tsv');edges=rows('EDGES.tsv');pins=rows('PR_SOURCE_CENSUS.tsv')
    by={r['source_id']:r for r in sources}
    need(len(by)==len(sources),'source ID collision')
    need(len({r['review_id'] for r in claims})==len(claims),'claim ID collision')
    need(len({r['edge_id'] for r in edges})==len(edges),'edge ID collision')
    for row in sources:
        for key in ('commit_sha','git_blob'):need(re.fullmatch('[0-9a-f]{40}',row[key]) is not None,'bad source '+key)
        need(row['repository'] and row['path'] and not row['path'].startswith('/') and '..' not in Path(row['path']).parts,'invalid source locator')
    for row in claims:
        need(row['source_id'] in by,'missing claim source')
        for key in ('claim','verdict','exact_scope','dependencies','evidence','required_repair','proposed_destination','independence'):
            need(bool(row[key]),'empty claim field '+key)
        file,anchor=row['evidence'].split('#',1)
        text=(root/file).read_text()
        need(('id="'+anchor+'"') in text or ('{#'+anchor+'}') in text,'missing review anchor '+row['evidence'])
    for row in edges:
        need(row['all_required_premises'] and row['review_reference'],'unqualified edge')
        if row['conclusion']=='RH':
            need(row['status'] not in ('VALID_FINITE_THEOREM','UNCONDITIONAL','PROVED'),'unconditional RH edge')
    counts=strict_json(root/'PACKET_COUNTS.json')
    for key,count in [('source_files',len(sources)),('claim_dispositions',len(claims)),('hyperedges',len(edges)),('pr_pin_rows',len(pins))]:
        need(type(counts[key]) is int and counts[key]==count,'count/type mismatch '+key)
    need(counts['rh_proved'] is False and counts['whole_repository_proof_audit'] is False,'scope altered')
    scope=strict_json(root/'FINAL_SCOPE.json');need(scope['rh_proved'] is False and scope['exhaustive_proof_audit_of_all_files'] is False,'completion overclaim')
    lock=strict_json(root/'SOURCE_LOCK.json');need(lock['research_terminal_pr']==707 and lock['unpublished_reviewer_dependency'] is False,'release boundary altered')
    rec=strict_json(root/'final-pass/EXECUTION_RECEIPT.json')
    need(rec['original_normal_exit']==1 and rec['api_repair_normal_exit']==1 and rec['cone_repair_normal_exit']==0,'execution history altered')
    need(rec['rh_proved'] is False,'replay RH overclaim')
    old=(root/'final-pass/replay/rank2_author.py').read_bytes()
    need(hashlib.sha1(b'blob '+str(len(old)).encode()+b'\0'+old).hexdigest()==rec['author_blob'],'author source blob mismatch')
    need((root/'final-pass/replay/small_controls.json').read_bytes()==(root/'final-pass/replay/small_controls.optimized.json').read_bytes(),'small control mode mismatch')
    manifest={}
    for line in (root/'SHA256SUMS').read_text().splitlines():
        digest,name=line.split('  ',1)
        need(name not in manifest,'duplicate manifest entry')
        need(re.fullmatch('[0-9a-f]{64}',digest) and not Path(name).is_absolute() and '..' not in Path(name).parts,'unsafe manifest entry')
        need(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'content mismatch '+name)
        manifest[name]=digest
    # Historical uploader/coordination records belong to the branch, not this packet.
    excluded={'SHA256SUMS','COORDINATION.md','HANDOFF_IMPORT.md','IMPORT_SHA256SUMS'}
    files={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.relative_to(root).as_posix() not in excluded and not p.relative_to(root).as_posix().startswith('handoff/')}
    need(set(manifest)==files,'manifest coverage differs from package')
    return {'status':'PASS_REVIEWER_A_FINAL_DISPOSITION_PACKET','source_files':len(sources),'claim_dispositions':len(claims),'hyperedges':len(edges),'pr_pin_rows':len(pins),'manifest_files':len(manifest),'rh_proved':False,'scope':'independent disposition with explicit exclusions'}
if __name__=='__main__':
    root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parent
    print(json.dumps(validate(root),sort_keys=True))
