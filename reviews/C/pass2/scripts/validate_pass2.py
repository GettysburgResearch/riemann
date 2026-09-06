#!/usr/bin/env python3
"""Offline evidence consistency, NOT remote authenticity or mathematical acceptance.

Reads only this review packet. All acceptance checks survive python -O.
"""
from __future__ import annotations
import copy
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SHA40 = re.compile(r'[0-9a-f]{40}')
FIRST_PASS_BLOB = '0d98aab08518bca855b387cdafa2a8e141ef2502'
REAL_PRS = {337} | (set(range(368,708)) - {417})
PASS1_PRS = set(range(370,390)) | set(range(700,708))
BASE = '8d16f8d9c475db290bc85e53d775b93b9bcdb336'
AFFECTED_XI = {'OPERATOR.XI.PICK_ORDER2','OPERATOR.XI.PICK_ORDER3.TP_CURVATURE',
 'OPERATOR.XI.RECIPROCAL_CONCAVITY.ACTUAL','OPERATOR.XI.PICK_ORDER3','OPERATOR.XI.LOEWNER_LOW_ORDER'}
SOURCE_BLOBS = {
 'evidence/PASS1_VALIDATION.md':'64e59e1ab00eaf6ed30fd4b2f953305732b7b3a3',
 'evidence/PASS1_RELEASE_BLOCKERS.md':'fac739274c28d729ecf4433a8a991a7083e2212d',
 'evidence/PASS1_STRUCTURE_AND_EXTRACTION.md':'7ed44cc511bda411cf3379656ea0aa31eb443a35',
 'evidence/PASS1_check_census.py':'6844efea894c2822efdfcb3d0d8112611d5a3f21',
 'evidence/PASS1_README.md':'f115047d08605c8d0cedfadab441579664483abe',
 'evidence/PASS1_census_counts.json':'3114fe4d8a2bedc102b09230523e5d5f871051ea',
 'replay/references/pr568_recorded/verify.py':'c946104810907deb55db18a4f2897e28618a04db',
 'replay/references/pr568_current/verify.py':'f0e8f85e195162d745477cfb69e68b9b24443289',
 'replay/references/pr599/verify.py':'121a2767b0e9fe8ed0d76d6146f11807b9a4b587',
 'replay/references/formal/check_no_sorry.sh':'b1ef22a399fd9b2a8f8eab6c8eaf53d4da6a410b',
}

class InvalidEvidence(ValueError):
    pass

def require(condition: bool, message: str) -> None:
    if not condition:
        raise InvalidEvidence(message)

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def unique_json(text: str):
    def pairs(items):
        result={}
        for key, value in items:
            require(key not in result, 'duplicate JSON key: '+key)
            result[key]=value
        return result
    return json.loads(text,object_pairs_hook=pairs)

def parse_tsv(text: str):
    result=list(csv.DictReader(io.StringIO(text),delimiter='\t'))
    require(all(None not in row and all(v is not None for v in row.values()) for row in result),
            'malformed TSV row shape')
    return result

def validate(old, observed, comparison, slots, formal, current, sources):
    historic={}
    for r in old:
        if not r['item_id'].startswith('OLD-'): continue
        n=int(r['item_id'][4:])
        require(n not in historic, 'duplicate historical PR')
        historic[n]=r
    require(set(historic)==REAL_PRS|{417},'wrong historical denominator')
    require(slots=={'slots':[417], 'source':'PASS1_CENSUS.tsv', 'included_in_real_pr_denominator':False},
            'no-object sentinel must be excluded')
    require({int(n) for n in observed}==REAL_PRS-PASS1_PRS,'missing/extra fresh observation')
    seen=set(); delta=set(); counts=Counter()
    for r in comparison:
        n=int(r['pr'])
        require(n in REAL_PRS and n not in seen,'missing/duplicate/non-PR comparison row')
        seen.add(n)
        for field in ('recorded_source_sha','observed_head_sha'):
            require(bool(SHA40.fullmatch(r[field])),'invalid '+field)
        require(r['recorded_source_sha']==historic[n]['frozen_source'],'historical pin changed')
        if n in PASS1_PRS:
            require(r['observation_pass']=='1' and historic[n]['coverage']=='B1', 'bad inherited receipt')
            h=historic[n]['frozen_source']
        else:
            o=observed[str(n)]
            require(r['observation_pass']=='2','new receipt falsely inherited')
            require(bool(SHA40.fullmatch(o['sha'])),'bad observed SHA')
            require(o['capture_kind']=='transcribed_head_fields_from_connector_not_raw_response',
                    'capture scope overstated')
            require(o['source_endpoint'].startswith('https://api.github.com/repos/GettysburgResearch/riemann/git/matching-refs/pull/'),
                    'wrong observation endpoint')
            prefix=o['source_endpoint'].rsplit('/',1)[-1]
            require(str(n).startswith(prefix), 'prefix cannot contain PR')
            require(r['observation_source']==o['source_endpoint'],'receipt endpoint differs')
            require(r['observation_time_utc']==o['observed_at_utc'],'observation time differs')
            h=o['sha']
        require(r['observed_head_sha']==h,'head differs from observation receipt')
        expected='MATCH' if h==historic[n]['frozen_source'] else 'DIFFERENT'
        require(r['comparison']==expected, 'false comparison verdict')
        counts[expected]+=1
        if expected=='DIFFERENT':
            delta.add(n)
            require(r['scientific_disposition']=='pending integrator reconciliation',
                    'unreconciled delta promoted or failed')
    require(seen==REAL_PRS,'comparison census incomplete')
    require(delta=={568,599},'unexpected exception set')
    ids=[r['formal_id'] for r in formal]
    require(len(ids)==37 and len(set(ids))==37,'wrong formal catalog denominator/duplicates')
    require(all(r['source_commit']==BASE for r in formal),'mixed formal baseline')
    require(Counter(r['owner'] for r in formal)=={'A':5,'B':14,'C':12,'C_API':6},'owner counts differ')
    canonical=[r for r in formal if r['kind']=='CANONICAL']
    status=Counter(r['reported_formal_status'] for r in canonical)
    require(status=={'STATED':1,'PROVED':7,'PROVED_CONDITIONAL':8,'REFUTED_FORMALIZED':3,'BLOCKED_MATHEMATICS':12},
            'canonical catalog status count differs')
    missing={r['formal_id'] for r in canonical if not r['lean_declaration']}
    require(missing=={'OPEN.ARITH.ROWS23_NATIVE','OPEN.ARITH.FIVE_THREE_NEGATIVE_MASS','OPEN.ARITH.FIXED_DETECTOR_NEGATIVE_MASS'},
            'open producer declaration boundary differs')
    active = [r for r in formal if r['lean_declaration']]
    require(len(active)==34 and len({r['lean_declaration'] for r in active})==33,
            'declaration denominator differs')
    require(len({r['lean_module'] for r in active})==15,'defining module count differs')
    require({r['formal_id'] for r in formal
             if r['independent_c_verdict']=='FAIL_NONVACUITY_OF_HEADLINE_INPUT'}==AFFECTED_XI,
            'nonvacuity finding silently altered or over-propagated')
    src_ids=[r['source_id'] for r in sources]
    require(len(src_ids)==len(set(src_ids)), 'duplicate inspected source identity')
    source_index={(r['repository'],r['source_commit'],r['source_path']):r for r in sources}
    for r in active:
        source = source_index.get(('GettysburgResearch/riemann',BASE,r['definition_source_path']))
        require(source is not None and source['source_git_blob']==r['definition_git_blob'],
                'declaration source binding differs')
        require('NOT_COMPILED' in r['c_review_scope'],'unperformed build silently promoted')
    now={r['item_id']:r for r in current}
    before={r['item_id']:r for r in old}
    require(len(now)==len(current)==566 and set(now)==set(before),'current census objects changed')
    for key,r in now.items():
        require(r['frozen_source']==before[key]['frozen_source'],'current census overwrote historical pin')
        if r['reviewer'] in ('A','B'):
            require(r['disposition']=='pending integrator reconciliation','current census promoted A/B')
    for r in comparison:
        row=now['OLD-'+r['pr']]
        expected='B1' if r['comparison']=='MATCH' else 'B2'
        require(row['coverage']==expected,'current census comparison disagrees')
        require('current_observed_head='+r['observed_head_sha'] in row['notes'],
                'current census omits exact observed head')
    require(now['OLD-417']['coverage']=='historical-absence','absent slot relabeled')
    return {'real_historical_prs':len(seen),'new_observations':len(observed),
            'inherited_pass1_observations':len(PASS1_PRS),'head_matches':counts['MATCH'],
            'head_differences':sorted(delta),'formal_catalog_transcribed_rows':len(formal),
            'catalog_declaration_mappings_desk_read':len(active),'unique_declarations_desk_read':33,
            'definition_modules_desk_read':15,'inspected_source_records':len(sources),
            'source_level_nonvacuity_finding_ids':sorted(AFFECTED_XI),
            'scientific_review_completeness_certified':False,'remote_read_authentication_certified':False,
            'all_repository_branches_or_prs_certified':False,'new_lean_build':False}

def main():
    raw=(ROOT/'evidence/PASS1_CENSUS.tsv').read_bytes()
    require(git_blob(raw)==FIRST_PASS_BLOB,'first-pass census bytes do not match published blob')
    for path,sha in SOURCE_BLOBS.items():
        require(git_blob((ROOT/path).read_bytes())==sha,'target source changed: '+path)
    old=parse_tsv(raw.decode());obs=unique_json((ROOT/'evidence/observed_heads.json').read_text())
    comp=parse_tsv((ROOT/'HISTORICAL_HEAD_COMPARISON.tsv').read_text())
    slots=unique_json((ROOT/'evidence/NO_OBJECT_SLOTS.json').read_text())
    formal=parse_tsv((ROOT/'FORMAL_CATALOG_AUDIT.tsv').read_text())
    current=parse_tsv((ROOT.parent/'CENSUS.tsv').read_text())
    sources=parse_tsv((ROOT/'INSPECTED_SOURCES.tsv').read_text())
    result=validate(old,obs,comp,slots,formal,current,sources)
    fixtures=[]
    for name, mutate in [
        ('missing_observation', lambda x:x[1].pop('337')),
        ('missing_comparison', lambda x:x[2].pop()),
        ('duplicate_comparison', lambda x:x[2].append(copy.deepcopy(x[2][0]))),
        ('malformed_sha', lambda x:x[1]['337'].__setitem__('sha','BAD')),
        ('false_match',lambda x:next(r for r in x[2] if r['pr']=='599').__setitem__('comparison','MATCH')),
        ('unreconciled_acceptance',lambda x:next(r for r in x[2] if r['pr']=='599').__setitem__('scientific_disposition','ACCEPTED')),
        ('count_absent_417',lambda x:x[3].__setitem__('included_in_real_pr_denominator',True)),
        ('claim_raw_export',lambda x:x[1]['337'].__setitem__('capture_kind','signed_raw_API_export')),
        ('duplicate_formal_id',lambda x:x[4].append(copy.deepcopy(x[4][0]))),
        ('different_formal_baseline',lambda x:x[4][0].__setitem__('source_commit','0'*40)),
        ('hide_vacuity',lambda x:next(r for r in x[4] if r['formal_id']=='OPERATOR.XI.PICK_ORDER3').__setitem__('independent_c_verdict','ACCEPTED')),
        ('invent_build',lambda x:x[4][0].__setitem__('c_review_scope','KERNEL_CHECKED')),
        ('overwrite_historical_pin',lambda x:x[5][0].__setitem__('frozen_source','0'*40)),
        ('false_current_match',lambda x:next(r for r in x[5] if r['item_id']=='OLD-599').__setitem__('coverage','B1')),
        ('bad_definition_blob',lambda x:x[4][0].__setitem__('definition_git_blob','0'*40)),
        ('duplicate_inspected_source',lambda x:x[6].append(copy.deepcopy(x[6][0]))),
    ]:
        payload=copy.deepcopy([old,obs,comp,slots,formal,current,sources]);mutate(payload)
        try: validate(*payload)
        except (InvalidEvidence,KeyError,ValueError) as exc:
            fixtures.append({'case':name,'rejected':True,'reason':str(exc)})
        else: raise InvalidEvidence('bad fixture accepted: '+name)
    try: unique_json('{"a":1,"a":2}')
    except InvalidEvidence as exc:
        fixtures.append({'case':'duplicate_json_key','rejected':True,'reason':str(exc)})
    else: raise InvalidEvidence('duplicate JSON accepted')
    result['negative_fixtures']=fixtures
    (ROOT/'reports/pass2_consistency.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))

if __name__=='__main__': main()
