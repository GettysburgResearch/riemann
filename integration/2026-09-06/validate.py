#!/usr/bin/env python3
"""Fail-closed integration validator and conservative current-registry resolver.

Default: validate an actual checkout, authenticate frozen inputs, and emit the
current view. --payload-only checks only the supplied release payload. Neither
mode executes archived research programs, proves analytic inputs, or runs Lean.
"""
from __future__ import annotations
import argparse
import copy
import csv
import hashlib
import importlib.util
import io
import json
from pathlib import Path, PurePosixPath
import re
import subprocess

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
SHA=re.compile(r'^[0-9a-f]{40}$')
EXPECTED_REVIEWS={'reviews/A','reviews/B','reviews/C','reviews/D','reviews/D-final','reviews/D-pass3','reviews/D-pass4'}
EXPECTED_PROGRAMMES={736,737,738,739,740,741,743,744,746,763,764}
EXPECTED_TABLES={'A','A-supplement','B','C4','D1','D2','D3','D4'}
PROVEN={'VERIFIED','VERIFIED_WITH_FIXES'}
RELATIONS={'VERIFIED','VERIFIED_WITH_FIXES','CONDITIONAL_EXACT'}
STATUSES={'REPAIRED_SCOPE','REFUTED_PROMOTION','EVIDENCE_REPLACED','CONDITIONAL_CERTIFICATE','OPEN_INTERFACE','HOLD_PROOF','HOLD_EXECUTION','CONDITIONAL_EXACT','BLOCKED_FORMAL_SOURCE','HOLD_INDEPENDENT_REVIEW','EXPLICIT_EXCLUSIONS'}


def require(ok,message):
    if not ok:raise ValueError(message)


def pairs(values):
    ans={}
    for k,v in values:
        require(k not in ans,'duplicate JSON key: '+k)
        ans[k]=v
    return ans


def load(path):
    return json.loads(path.read_text(encoding='utf-8'),object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON number '+x)))


def relative(name):
    require(type(name) is str and name!='','empty/nonstring path')
    p=PurePosixPath(name)
    require(not p.is_absolute() and '..' not in p.parts and ':' not in name and '\\' not in name,'unsafe path '+name)
    return ROOT.joinpath(*p.parts)


def blob(data):
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def git(*args):
    return subprocess.check_output(['git','-c','core.hooksPath=/dev/null',*args],cwd=ROOT).decode().strip()


def rows(path):
    reader=csv.DictReader(io.StringIO(path.read_text(encoding='utf-8')),delimiter='\t')
    require(reader.fieldnames and len(set(reader.fieldnames))==len(reader.fieldnames),'bad TSV header '+str(path))
    ans=[]
    for row in reader:
        require(None not in row,'extra TSV cells '+str(path))
        if not any(v for v in row.values()):continue
        ans.append({k:('' if v is None else v) for k,v in row.items()})
    require(ans,'empty TSV '+str(path))
    return reader.fieldnames,ans


def check_payload(release,freeze,decisions,programmes,tables,frontier,proofs):
    require(release['schema']=='riemann.integration.release.v1' and release['release']=='2026-09-06','release identity')
    for k in ('rh_proved','exhaustive_new_scientific_review','public_launch_cleared','fresh_lean_build','fresh_heavy_campaigns'):
        require(type(release[k]) is bool and release[k] is False,'forbidden/ill-typed release promotion: '+k)
    require(release['status']=='SCOPED_INTEGRATION_WITH_EXPLICIT_EXCLUSIONS','release scope')
    rr=freeze['reviews'];require(type(rr) is list and len(rr)==7,'seven frozen review trees required')
    require({r['path'] for r in rr}==EXPECTED_REVIEWS,'review tree coverage')
    for r in rr:
        require(SHA.fullmatch(r['tree']) and SHA.fullmatch(r['head']),'bad source SHA')
        require(type(r['pr']) is int and r['pr'] in {795,796,798,799},'bad source PR')
        relative(r['path'])
    require(release['baseline']==freeze['baseline']=='8d16f8d9c475db290bc85e53d775b93b9bcdb336','baseline mismatch')
    require(type(decisions) is list and len(decisions)==43,'exact decision coverage')
    ids=[d['id'] for d in decisions]
    require(len(ids)==len(set(ids)),'duplicate decision ID')
    require({f'D-F{i:02d}' for i in range(1,19)} <= set(ids),'missing D finding')
    for d in decisions:
        require(d['status'] in STATUSES and d['correction'].strip(),'unknown decision status or empty correction')
        require(type(d['block_original_graph_use']) is bool,'ill-typed graph flag')
        require(type(d['evidence']) is list and bool(d['evidence']),'empty decision evidence')
        require(type(d['base_source_claims']) is list and type(d['base_semantic_ids']) is list,'invalid match lists')
        for e in d['evidence']:relative(e)
    require(type(programmes) is list and len(programmes)==11,'eleven programmes required')
    require(all(type(p['issue']) is int for p in programmes),'boolean programme alias')
    require({p['issue'] for p in programmes}==EXPECTED_PROGRAMMES,'programme coverage')
    for p in programmes:require(p['next_gate'].strip() and p['evidence'],'missing programme gate/evidence')
    require(len(tables)==8 and {t['packet'] for t in tables}==EXPECTED_TABLES,'claim-table coverage')
    for t in tables:
        relative(t['path']);n=t['expected_rows']
        require(n is None or (type(n) is int and n>0),'bad review count')
    ns=frontier['nodes'];es=frontier['edges']
    require(type(ns) is list and len(ns)==16 and type(es) is list and len(es)==6,'frontier coverage')
    nd={n['id']:n for n in ns};require(len(nd)==len(ns),'duplicate frontier node')
    for n in ns:
        require(n['id'].startswith('I20260906.') and n['evidence'],'unqualified frontier node')
        if n['kind']=='OPEN_HYPOTHESIS':require(n['status']=='OPEN','open hypothesis promoted')
    require(len({e['id'] for e in es})==len(es),'duplicate frontier edge')
    for e in es:
        require(type(e['traversable']) is bool and e['traversable'] is False,'frontier is not an accepted adapter')
        require(e['conclusion']=='RH' and type(e['premises']) is list and len(e['premises'])>0,'bad frontier edge')
        require(all(x in nd and nd[x]['kind']=='OPEN_HYPOTHESIS' and nd[x]['status']=='OPEN' for x in e['premises']),'frontier lacks explicit open leaf')
    require(len(proofs)==10 and len({p['path'] for p in proofs})==10,'proof payload coverage')
    for p in proofs:relative(p['path']);relative(p['source']);require(SHA.fullmatch(p['blob']),'bad proof blob')


def typed_edges(claims, base_edges, blocked=()):
    """Interpret applications separately from records of available APIs.

    A verdict describes the statement's review status, not whether all of its
    application hypotheses hold. The historical first_missing_premise column
    is a conjunction of node IDs; never discard it when computing closure.
    No historical row is mutated. Exported premise_ids are the effective
    prerequisites, and historical_premise_ids retains the original text.
    """
    by={r['semantic_id']:r for r in claims}
    require(len(by)==len(claims) and 'RH' in by,'base claim identity')
    applications={'HYPEREDGE','CONDITIONAL_REDUCTION','COORDINATE_IDENTIFICATION',
                  'EQUIVALENCE','EQUIVALENCE_MOD_L1','CONDITIONAL_ROUTE',
                  'CONDITIONAL_IMPLICATION'}
    metadata={'CONDITIONAL_API','STRUCTURAL_USE','OPEN_EXTENSION',
              'PURPORTED_IMPLICATION','PURPORTED_EQUIVALENCE',
              'PURPORTED_DESCENT','PURPORTED_EXTENSION'}
    edges=copy.deepcopy(base_edges)
    require(len({e['edge_id'] for e in edges})==len(edges),'duplicate inherited edge')
    for e in edges:
        ps=json.loads(e['premise_ids'],object_pairs_hook=pairs)
        require(type(ps) is list and bool(ps) and
                all(type(p) is str and bool(p) for p in ps),'bad inherited hyperedge')
        require(len(ps)==len(set(ps)),'duplicate inherited premise')
        text=e.get('first_missing_premise','')
        require(type(text) is str,'bad missing-premise declaration')
        missing=[p.strip() for p in text.split('|')] if text else []
        require(all(missing),'empty missing-premise ID')
        require(len(missing)==len(set(missing)),'duplicate missing-premise ID')
        required=list(dict.fromkeys(ps+missing))
        require(all(p in by for p in required) and e['conclusion_id'] in by,
                'dangling inherited endpoint or missing prerequisite')
        kind=e.get('edge_type')
        require(kind in applications|metadata,'unknown or absent edge type')
        reasons=[]
        if e['final_verdict'] not in RELATIONS:
            reasons.append('RELATION_NOT_ACCEPTED')
        if kind in metadata:
            reasons.append('NOT_AN_APPLICATION_EDGE')
        if e['conclusion_id'] in required:
            reasons.append('UNRESOLVED_SELF_DEPENDENCY')
        if (set(required)|{e['conclusion_id']}) & set(blocked):
            reasons.append('BLOCKED_BY_CURRENT_DECISION')
        e['historical_premise_ids']=e['premise_ids']
        e['premise_ids']=json.dumps(required)
        e['current_missing_prerequisite_ids']=json.dumps(missing)
        e['current_block_reasons']=json.dumps(reasons)
        e['current_traversable']=not reasons
    return edges


def graph_closure(claims, edges):
    """Least fixed point of explicitly typed, fully premised implications.

    OPEN nodes are not initial facts, but may be derived by an actual accepted
    implication. Do not hide errors by banning all OPEN conclusions or by
    removing RH from the resulting closure.
    """
    reach={r['semantic_id'] for r in claims if r['final_verdict'] in PROVEN
           and not r['semantic_id'].startswith('OPEN.') and r['semantic_id']!='RH'}
    changed=True
    while changed:
        changed=False
        for e in edges:
            require(type(e.get('current_traversable')) is bool,
                    'closure requires a typed edge')
            if e['current_traversable'] and set(json.loads(e['premise_ids']))<=reach:
                if e['conclusion_id'] not in reach:
                    reach.add(e['conclusion_id']);changed=True
    return reach


def resolve(base_claims,base_edges,decisions):
    claims=copy.deepcopy(base_claims);by={r['semantic_id']:r for r in claims}
    require(len(by)==len(claims) and 'RH' in by,'base claim identity')
    matches={d['id']:[] for d in decisions}
    blocked=set()
    for r in claims:
        prior=r['final_verdict'];r['previous_final_verdict']=prior
        tokens=set(re.findall(r'\b[LTR]-\d+',r.get('source_claim_id','')))
        found=[d for d in decisions if r['semantic_id'] in d['base_semantic_ids'] or tokens.intersection(d['base_source_claims'])]
        r['current_decision_ids']=json.dumps([d['id'] for d in found])
        r['current_scope_repairs']=' | '.join(d['correction'] for d in found)
        r['current_evidence']=json.dumps(sorted({e for d in found for e in d['evidence']}))
        for d in found:matches[d['id']].append(r['semantic_id'])
        if any(d['block_original_graph_use'] for d in found):
            r['final_verdict']='GAP_BLOCKED';blocked.add(r['semantic_id'])
        elif found and prior in PROVEN:r['final_verdict']='VERIFIED_WITH_FIXES'
    # Apply the SAME corrected semantics to both historical and current views.
    # The literal historical TSV remains unchanged, including its API records.
    old_edges=typed_edges(base_claims,base_edges)
    edges=typed_edges(claims,base_edges,blocked)
    old=graph_closure(base_claims,old_edges);new=graph_closure(claims,edges)
    require(new<=old,'current graph illegally strengthens inherited reachability')
    require('RH' not in old and 'RH' not in new,'reviewed-only graph reaches RH: inspect proof inputs')
    return claims,edges,{
        'interpretation':'typed-applications-v2',
        'matched_base_claims':matches,'blocked_original_nodes':sorted(blocked),
        'base_reachable':len(old),'current_reachable':len(new),
        'base_reachable_ids':sorted(old),'current_reachable_ids':sorted(new),
        'base_nonapplication_edges':[e['edge_id'] for e in old_edges
                                    if not e['current_traversable']],
        'reviewed_only_path_to_rh':False}

def self_tests(payload):
    check_payload(*payload)
    mutations=[
      lambda p:p[0].__setitem__('rh_proved',True),
      lambda p:p[0].__setitem__('rh_proved',0),
      lambda p:p[0].__setitem__('public_launch_cleared',True),
      lambda p:p[1].__setitem__('reviews',[]),
      lambda p:p[1]['reviews'][0].__setitem__('head','x'*40),
      lambda p:p[2].pop(0),
      lambda p:p[2][1].__setitem__('id',p[2][0]['id']),
      lambda p:p[2][0].__setitem__('evidence',[]),
      lambda p:p[2][0].__setitem__('status','PROVED_RH'),
      lambda p:p[3][0].__setitem__('issue',True),
      lambda p:p[4][0].__setitem__('expected_rows',128.0),
      lambda p:p[5]['edges'][0].__setitem__('traversable',True),
      lambda p:p[5]['edges'][0].__setitem__('premises',[]),
      lambda p:p[6][0].__setitem__('path','../escaped.md')]
    for mutate in mutations:
        p=copy.deepcopy(payload);mutate(p)
        try:check_payload(*p)
        except (ValueError,KeyError,TypeError):pass
        else:raise ValueError('a payload mutation was accepted')
    for bad in ('{"a":1,"a":2}','{"a":NaN}'):
        try:json.loads(bad,object_pairs_hook=pairs,parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
        except ValueError:pass
        else:raise ValueError('strict JSON accepted corruption')
    cs=[{'semantic_id':'API','source_claim_id':'L-123','final_verdict':'VERIFIED'},
        {'semantic_id':'OPEN.X','source_claim_id':'','final_verdict':'OPEN_SUFFICIENT_FOR_RH'},
        {'semantic_id':'RH','source_claim_id':'','final_verdict':'OPEN_RH_EQUIVALENT'}]
    es=[{'edge_id':'e','premise_ids':'["API","OPEN.X"]','conclusion_id':'RH','final_verdict':'CONDITIONAL_EXACT','edge_type':'HYPEREDGE','first_missing_premise':''}]
    resolve(cs,es,[])
    bad=copy.deepcopy(es);bad[0]['premise_ids']='["API"]'
    try:resolve(cs,bad,[])
    except ValueError:pass
    else:raise ValueError('collapsed producer premise was accepted')
    bad=copy.deepcopy(es);bad[0]['premise_ids']='["MISSING"]'
    try:resolve(cs,bad,[])
    except ValueError:pass
    else:raise ValueError('dangling endpoint was accepted')
    return {'payload_rejections':len(mutations),'strict_json_rejections':2,'graph_rejections':2}


def emit_tsv(path,records):
    fields=list(dict.fromkeys(k for r in records for k in r))
    with path.open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(records)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--payload-only',action='store_true',help='NOT full checkout verification')
    args=parser.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    names=['RELEASE.json','SOURCE_FREEZE.json','DECISIONS.json','PROGRAMMES.json','REVIEW_TABLES.json','FRONTIER_GRAPH.json','PROOF_PAYLOADS.json']
    payload=[load(HERE/n) for n in names]
    rejection=self_tests(payload)
    release,freeze,decisions,programmes,tables,frontier,proofs=payload
    spec=importlib.util.spec_from_file_location('integration_exact_fixtures',HERE/'independent_fixtures.py')
    require(spec and spec.loader,'fixture module unavailable')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);fixtures=mod.run()
    report={'schema':'riemann.integration.validation.v1','mode':'PAYLOAD_ONLY' if args.payload_only else 'FULL_CHECKOUT',
            'release':'2026-09-06','decisions':len(decisions),'programmes':len(programmes),
            'rejection_tests':rejection,'independent_fixtures':fixtures,'rh_proved':False,
            'fresh_lean_build':False,'fresh_heavy_campaigns':False,'public_launch_cleared':False,
            'exhaustive_scientific_review':False}
    if not args.payload_only:
        for r in freeze['reviews']:
            require(git('rev-parse','HEAD:'+r['path'])==r['tree'],'frozen review tree changed: '+r['path'])
        for d in decisions:
            for e in d['evidence']:require(relative(e).is_file(),'missing evidence: '+e)
        for p in proofs:
            data=relative(p['path']).read_bytes()
            require(data==relative(p['source']).read_bytes() and blob(data)==p['blob'],'proof extract mismatch: '+p['path'])
        base=[]
        for k in ('base_claims','base_edges'):
            entry=release[k];p=relative(entry['path'])
            require(blob(p.read_bytes())==entry['blob'],'changed historical input: '+entry['path'])
            _,data=rows(p);require(len(data)==entry['rows'],'historical row count mismatch');base.append(data)
        claims,edges,graph=resolve(base[0],base[1],decisions)
        report['graph']=graph;review_index=[];counts={}
        for table in tables:
            fields,data=rows(relative(table['path']));ids=[r[fields[0]] for r in data]
            require(all(ids) and len(set(ids))==len(ids),'review ID coverage: '+table['packet'])
            if table['expected_rows'] is not None:require(len(data)==table['expected_rows'],'review row count: '+table['packet'])
            counts[table['packet']]=len(data)
            for r in data:review_index.append({'qualified_id':table['packet']+'/'+r[fields[0]],'source_table':table['path'],'registry_role':table['registry_role'],'unconditional_seed':False,'record':r})
        require(sum(v for k,v in counts.items() if k.startswith('D'))==186,'D four-pass coverage')
        report['review_table_counts']=counts;report['review_disposition_records']=len(review_index)
        _,census=rows(ROOT/'reviews/C/CENSUS.tsv')
        report['retained_C_census_rows']=len(census)
        report['checkout_commit']=git('rev-parse','HEAD');report['checkout_tree']=git('rev-parse','HEAD^{tree}')
        emit_tsv(out/'claims_current.tsv',claims);emit_tsv(out/'edges_current.tsv',edges)
        (out/'review_dispositions.json').write_text(json.dumps(review_index,ensure_ascii=False,indent=2)+'\n')
        report['marker']='PASS_SCOPED_INTEGRATION_FULL_CHECKOUT'
    else:
        report['marker']='PASS_RELEASE_PAYLOAD_NOT_FULL_CHECKOUT'
        report['unperformed']=['actual-checkout source tree authentication','historical registry resolution','review-table/census parsing','full local-link validation','Lean and transitive import replay','heavy research campaigns','public-launch clearance']
    (out/'validation.json').write_text(json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,sort_keys=True,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
