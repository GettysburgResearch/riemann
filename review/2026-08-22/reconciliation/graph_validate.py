#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, re, sys
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SHA=re.compile(r'^[0-9a-f]{40}$')
VALID={'VERIFIED','VERIFIED_WITH_FIXES','CONDITIONAL_EXACT','OPEN_SUFFICIENT_FOR_RH','OPEN_RH_EQUIVALENT','GAP_BLOCKED','FALSE','REFUTED_MECHANISM','SUPERSEDED','DUPLICATE_ALIAS','EMPIRICAL_ONLY','RETAINED_HEAVY_CERTIFICATE','TARGETED_REVIEW_REQUIRED'}
PROVED={'VERIFIED','VERIFIED_WITH_FIXES'}
OPEN={'OPEN_SUFFICIENT_FOR_RH','OPEN_RH_EQUIVALENT','CONDITIONAL_EXACT'}
INACTIVE={'FALSE','REFUTED_MECHANISM','GAP_BLOCKED','SUPERSEDED','EMPIRICAL_ONLY','TARGETED_REVIEW_REQUIRED'}
LIFECYCLE={'CANONICALIZED','LIVE_OPEN_GATE','SUPERSEDED','REFUTED','HISTORICAL_FULL_PROPOSAL','RETAINED_COMPUTATIONAL_CERTIFICATE','DUPLICATE_RECOVERY','ADMINISTRATIVE','TARGETED_REVIEW_REQUIRED'}
ALIAS_REL={'SAME_OBJECT_AT_TYPED_SCOPE','SAME_OBJECT','SAME_OBJECT_MOD_L1','NOT_THE_SAME_OBJECT','RELATED_NOT_IDENTICAL','NAMESPACE_MIGRATION','PATH_QUALIFIED_ID','PROVENANCE_ONLY','SYNTHESIZED_COORDINATE','SAME_OPEN_CUT_CLASS','SAME_TERMINAL_CLASS'}
REQ=['FREEZE.json','FINAL_CLAIMS.tsv','FINAL_EDGES.tsv','FINAL_ALIASES.tsv','FINAL_REFUTATIONS.tsv','FINAL_COMPUTATIONS.tsv','FINAL_FAMILIES.tsv','FINAL_PR_DISPOSITIONS.tsv','CONFLICTS.tsv','FIXES_REQUIRED.md','GRAPH_REPORT.md','OPEN_CUTS.md','EXTRACTION_PLAN.tsv','INTEGRATION_READY.md','README.md','RECONCILIATION_CHANGELOG.md','ISSUE_ARCHAEOLOGY_SUMMARY.md','DIRECT_MAIN_SUMMARY.md']

def load(name):
    with (ROOT/name).open(newline='',encoding='utf-8') as f: return list(csv.DictReader(f,delimiter='\t'))
def unique(rows,key,name):
    xs=[r[key] for r in rows]
    if len(xs)!=len(set(xs)): raise AssertionError(f'duplicate {key} in {name}')
def missing_list(s): return [x for x in s.split('|') if x]

def main():
    for name in REQ:
        p=ROOT/name
        if not p.is_file() or p.stat().st_size==0: raise AssertionError(f'missing required file: {name}')
    freeze=json.loads((ROOT/'FREEZE.json').read_text())
    exp={708:'eb1987502ef9043e782ac6ab1e19c47be9daef93',709:'55fe0b6f23d9163e2b602608da84194ba243d7c4',710:'e91d6aa25d2e8576e82d26170127941eec430f75',711:'945a6eec3406cce8f6cd63eba6c69fb60676c41d',712:'a6aa936ba8bf538177e34af60db7e2f0a58f8dfd',717:'dad61b954dd8404520631058d1ce717e7a910a3b'}
    got={int(x['pr']):x['head'] for x in freeze['review_objects']}
    if got!=exp: raise AssertionError(f'review heads mismatch: {got}')
    if freeze['frozen_main']['sha']!='677203992eb0168920365ee45ae9db76bfa97dcf': raise AssertionError('wrong frozen main')
    if freeze['reviewer_c_completion']['targeted_review_rows']!=0 or freeze['reviewer_c_completion']['unresolved_exact_heads']!=1: raise AssertionError('stale Reviewer C metrics')
    if freeze['direct_main_completion']['commit_count']!=85 or freeze['direct_main_completion']['packet_count']!=11: raise AssertionError('wrong direct-main metrics')

    claims=load('FINAL_CLAIMS.tsv'); edges=load('FINAL_EDGES.tsv'); aliases=load('FINAL_ALIASES.tsv'); refs=load('FINAL_REFUTATIONS.tsv'); comps=load('FINAL_COMPUTATIONS.tsv'); fams=load('FINAL_FAMILIES.tsv'); prs=load('FINAL_PR_DISPOSITIONS.tsv'); conflicts=load('CONFLICTS.tsv'); extraction=load('EXTRACTION_PLAN.tsv')
    for rows,key,name in [(claims,'semantic_id','claims'),(edges,'edge_id','edges'),(aliases,'alias_id','aliases'),(refs,'refutation_id','refutations'),(comps,'computation_id','computations'),(fams,'family_id','families'),(prs,'pr','PR dispositions'),(conflicts,'conflict_id','conflicts'),(extraction,'semantic_id','extraction')]: unique(rows,key,name)
    by={r['semantic_id']:r for r in claims}
    if 'RH' not in by: raise AssertionError('RH missing')
    heads=freeze['source_heads']
    for r in claims:
        if r['final_verdict'] not in VALID: raise AssertionError(f"bad verdict {r['semantic_id']}")
        pr=r['source_pr']; sha=r['source_head_sha']; path=r['source_path']
        if not SHA.fullmatch(sha): raise AssertionError(f"malformed SHA {r['semantic_id']}: {sha}")
        if pr=='0':
            if sha!='0'*40: raise AssertionError(f"synthetic SHA {r['semantic_id']}")
            local=ROOT/path.removeprefix('review/2026-08-22/reconciliation/')
            if not local.is_file(): raise AssertionError(f"missing local source {r['semantic_id']}: {path}")
        else:
            if heads.get(pr)!=sha: raise AssertionError(f"source/head mismatch {r['semantic_id']} {pr} {sha}")
            if not path or path in {'PR_BODY','UNRESOLVED'} or '*' in path: raise AssertionError(f"unresolved path {r['semantic_id']}: {path}")
            for part in path.split('|'):
                if '/' not in part or not re.search(r'\.(md|tsv|json|py|yaml|yml)$',part): raise AssertionError(f"bad path syntax {r['semantic_id']}: {part}")
    if any(r['final_verdict']=='TARGETED_REVIEW_REQUIRED' for r in claims): raise AssertionError('targeted claim remains')

    for a in aliases:
        if a['canonical_semantic_id'] not in by: raise AssertionError(f"dangling alias {a['alias_id']}")
        if a['relation'] not in ALIAS_REL: raise AssertionError(f"bad alias relation {a['alias_id']} {a['relation']}")
        if not a['final_status'].startswith('RESOLVED'): raise AssertionError(f"unresolved alias {a['alias_id']}")

    for e in edges:
        prem=json.loads(e['premise_ids']); src_pr=json.loads(e['source_prs']); src_sha=json.loads(e['source_shas'])
        if not isinstance(prem,list) or not prem or len(prem)!=len(set(prem)): raise AssertionError(f"bad hyperedge {e['edge_id']}")
        for n in prem+[e['conclusion_id']]:
            if n not in by: raise AssertionError(f"dangling node {n} in {e['edge_id']}")
        if e['final_verdict'] not in VALID: raise AssertionError(f"bad edge verdict {e['edge_id']}")
        if len(src_pr)!=len(src_sha): raise AssertionError(f"edge source length {e['edge_id']}")
        for pr,sha in zip(src_pr,src_sha):
            key=str(pr)
            if not SHA.fullmatch(sha) or heads.get(key)!=sha: raise AssertionError(f"edge source mismatch {e['edge_id']} {key} {sha}")
        if e['conclusion_id']=='RH' and e['final_verdict'] not in PROVED and e['final_verdict']!='FALSE':
            ms=missing_list(e['first_missing_premise'])
            if not ms: raise AssertionError(f"conditional RH edge hides premise {e['edge_id']}")
            if any(x not in prem for x in ms): raise AssertionError(f"missing node not explicit {e['edge_id']}")
        if e['final_verdict'] in PROVED:
            for n in prem:
                if by[n]['final_verdict'] in INACTIVE|{'OPEN_RH_EQUIVALENT','OPEN_SUFFICIENT_FOR_RH'}: raise AssertionError(f"inactive/open premise in proved edge {e['edge_id']}: {n}")

    prset={int(r['pr']) for r in prs}
    expected=set(range(375,708))
    if prset!=expected: raise AssertionError(f"PR coverage mismatch missing={sorted(expected-prset)[:5]} extra={sorted(prset-expected)[:5]}")
    for r in prs:
        if r['final_lifecycle_disposition'] not in LIFECYCLE: raise AssertionError(f"bad lifecycle #{r['pr']}")
    if any(r['final_lifecycle_disposition']=='TARGETED_REVIEW_REQUIRED' for r in prs): raise AssertionError('targeted PR lifecycle remains')
    r417=next(r for r in prs if r['pr']=='417')
    if r417['head_resolution']!='NO_REMOTE_PR_OBJECT_SEQUENCE_GAP' or r417['final_lifecycle_disposition']!='ADMINISTRATIVE': raise AssertionError('#417 not fail-closed')

    if {r['semantic_id'] for r in extraction}!=set(by): raise AssertionError('extraction plan is not one-to-one')
    unresolved=[r for r in conflicts if not r['resolution_status'].startswith('RESOLVED')]
    if unresolved: raise AssertionError(f"unresolved conflicts: {[r['conflict_id'] for r in unresolved]}")

    known={sid for sid,r in by.items() if r['final_verdict'] in PROVED}
    active=[e for e in edges if e['final_verdict'] in PROVED]
    change=True
    while change:
        change=False
        for e in active:
            if all(x in known for x in json.loads(e['premise_ids'])) and e['conclusion_id'] not in known:
                known.add(e['conclusion_id']); change=True
    if 'RH' in known: raise AssertionError('accidental proven-only path to RH')

    cuts=sorted({x for e in edges if e['conclusion_id']=='RH' and e['final_verdict'] not in PROVED|{'FALSE'} for x in missing_list(e['first_missing_premise'])})
    conj=[]
    for e in edges:
        if e['conclusion_id']=='RH' and e['final_verdict'] not in PROVED|{'FALSE'}:
            ps=[x for x in json.loads(e['premise_ids']) if by[x]['final_verdict'] in {'OPEN_SUFFICIENT_FOR_RH','OPEN_RH_EQUIVALENT'}]
            if len(ps)>=2: conj.append({'edge_id':e['edge_id'],'open_premises':ps})
    dead=sorted(r['semantic_id'] for r in claims if r['final_verdict'] in {'FALSE','REFUTED_MECHANISM'})
    result={'verdict':'PASS_REVIEWER_D_COMPLETE_RECONCILIATION','RH_STATUS':'UNPROVED','PROVEN_ONLY_PATH_TO_RH':False,'CLAIM_ROWS':len(claims),'EDGE_ROWS':len(edges),'ALIAS_ROWS':len(aliases),'REFUTATION_ROWS':len(refs),'COMPUTATION_ROWS':len(comps),'FAMILY_ROWS':len(fams),'PR_DISPOSITION_ROWS':len(prs),'CONFLICT_ROWS':len(conflicts),'TARGETED_REVIEW_REQUIRED_COUNT':0,'UNRESOLVED_CONFLICT_COUNT':0,'REVIEWER_C_SEQUENCE_GAPS':[417],'DIRECT_MAIN_COMMITS_CLASSIFIED':85,'MINIMAL_OPEN_CUTS':cuts,'MINIMAL_CONJUNCTIVE_OPEN_CUTS':conj,'DEAD_MECHANISM_CLASSES':dead,'HEAVY_CAMPAIGNS_RERUN':False,'INTEGRATION_READINESS':'READY_WITH_EXPLICIT_EXCLUSIONS'}
    (ROOT/'replay/validation.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
    return result
if __name__=='__main__': main()
