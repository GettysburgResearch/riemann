#!/usr/bin/env python3
"""Validate the composite A report and fresh receipts, not every mathematical proof."""
from pathlib import Path
import csv,hashlib,json,re,sys

def need(ok,msg):
    if not ok: raise RuntimeError(msg)
def js(p):
    def pairs(items):
        out={}
        for k,v in items:
            need(k not in out,'duplicate JSON key');out[k]=v
        return out
    return json.loads(p.read_text(),object_pairs_hook=pairs)
def table(p):
    with p.open(newline='') as f:
        out=list(csv.DictReader(f,delimiter='\t'))
    need(all(None not in r and all(v is not None for v in r.values()) for r in out),'ragged table')
    return out

def validate(root):
    s=root/'supplement';meta=js(s/'SCOPE.json')
    need(meta['rh_proved'] is False and meta['all_historical_proofs_accepted'] is False,'scope overclaim')
    need(meta['research_terminal_pr']==707 and meta['unpublished_reviewer_dependency'] is False,'baseline drift')
    sources=table(root/'SOURCES.tsv')+table(s/'SOURCES.tsv')
    claims=table(root/'CLAIMS.tsv')+table(s/'CLAIMS.tsv')
    edges=table(root/'EDGES.tsv')+table(s/'EDGES.tsv')
    for rows,key,count in [(sources,'source_id','combined_sources'),(claims,'review_id','combined_claims'),(edges,'edge_id','combined_edges')]:
        need(len({r[key] for r in rows})==len(rows),'duplicate '+key)
        need(type(meta[count]) is int and meta[count]==len(rows),'composite count mismatch')
    ids={r['source_id'] for r in sources}
    for row in sources:
        for key in ['commit_sha','git_blob']:
            need(re.fullmatch('[a-f0-9]{40}',row[key]) is not None,'malformed source SHA')
    for row in claims:
        need(row['source_id'] in ids,'missing source')
        need(all(row.get(k) for k in ['claim','verdict','exact_scope','dependencies','evidence','required_repair','proposed_destination','independence']),'empty claim scope')
        file,anchor=row['evidence'].split('#',1)
        need(not Path(file).is_absolute() and '..' not in Path(file).parts,'unsafe evidence path')
        text=(root/file).read_text()
        need(('id="'+anchor+'"') in text or ('{#'+anchor+'}') in text,'missing evidence anchor '+row['evidence'])
    for row in edges:
        need(row['all_required_premises'] and row['review_reference'],'empty implication')
        need(not (row['conclusion']=='RH' and row['status'] in ['PROVED','UNCONDITIONAL','VALID_FINITE_THEOREM']),'RH overclaim')
    outputs=[]
    for n in ['seven_result.json','seven_result.optimized.json','seven_result.repeated.json']:
        d=js(s/'replay'/n);d.pop('seconds')
        need(d['verdict']=='PASS_INDEPENDENT_DYADIC_SEVEN_POINT' and d['target']=='19/5000','bad seven-point result')
        need(d['zeta_bound_proved_by_this_code'] is False,'finite/analytic boundary')
        c=d['counts'];initial=d['initial_boxes']
        need(all(type(v) is int and v>=0 for v in c.values()),'bad count type')
        need(c['nodes']==initial+2*c['splits'],'tree node coverage')
        need(c['pressure']+c['interval']+c['tangent']==initial+c['splits'],'tree leaf coverage')
        outputs.append(d)
    need(outputs[0]==outputs[1]==outputs[2],'mode mathematical result mismatch')
    for n in ['optimized.exit','repeated.exit','rank2.optimized.final.exit']:
        need((s/'replay'/n).read_text().strip()=='0','nonzero replay exit')
    for base in ['finite_controls','selector_controls']:
        need((s/'replay'/(base+'.json')).read_bytes()==(s/'replay'/(base+'.optimized.json')).read_bytes(),'small-control mode mismatch')
    rec=js(s/'EXECUTION_RECEIPT.json')
    need(rec['rh_proved'] is False and rec['full_lean_build'] is False and rec['new_pdf_page_audit'] is False,'receipt overclaim')
    for n,h in rec['sha256'].items():
        need(hashlib.sha256((s/'replay'/n).read_bytes()).hexdigest()==h,'replay byte mismatch '+n)
    need(hashlib.sha256((root/'final-pass/replay/rank2_cone_repaired.certificate.json').read_bytes()).hexdigest()==rec['rank_two']['certificate_sha256'],'rank-two certificate drift')
    return {'status':'PASS_A_OMISSIONS_SUPPLEMENT','combined_claims':len(claims),'combined_sources':len(sources),'combined_edges':len(edges),'seven_nodes':outputs[0]['counts']['nodes'],'rh_proved':False,'kernel_build_claimed':False}
if __name__=='__main__':
    root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
    print(json.dumps(validate(root),sort_keys=True))
