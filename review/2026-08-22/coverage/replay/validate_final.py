#!/usr/bin/env python3
from __future__ import annotations
import csv, json, re, sys
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]

def read(name):
    with (HERE/name).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f,delimiter='\t'))

census=read('PR_CENSUS.tsv')
backlog=read('PASS2_BACKLOG.tsv')
final=read('PASS2_FINAL_REVIEW.tsv')
heads=read('FINAL_HEAD_RECONCILIATION.tsv')
errors=[]
if len(census)!=341: errors.append(f'census rows={len(census)}')
if len(backlog)!=73 or len(final)!=73 or len(heads)!=73: errors.append('pass-two row count mismatch')
back={r['pr'] for r in backlog}
if back!={r['pr'] for r in final} or back!={r['pr'] for r in heads}: errors.append('pass-two key set mismatch')
if any(r['delta_action']=='TARGETED_REVIEW_STILL_REQUIRED' for r in census): errors.append('targeted review rows remain')
blanks=[r['pr'] for r in census if not r['exact_head_sha']]
if blanks!=['417']: errors.append(f'unexpected blank heads {blanks}')
mal=[]
for r in census:
    if r['pr']=='417': continue
    h=r['exact_head_sha']
    if not re.fullmatch(r'[0-9a-f]{40}',h) or h.endswith('0'*32): mal.append(r['pr'])
if mal: errors.append(f'malformed heads {mal}')
if [r['pr'] for r in heads if r['status']=='NO_REMOTE_PR_OBJECT']!=['417']: errors.append('no-object set mismatch')
if sum(r['status']=='EXACT_CURRENT_HEAD_RECOVERED' for r in heads)!=72: errors.append('recovered-head count mismatch')
for r in heads:
    if r['status']=='EXACT_CURRENT_HEAD_RECOVERED' and not re.fullmatch(r'[0-9a-f]{40}',r['reconciled_head']): errors.append(f"bad reconciliation {r['pr']}")
if any(r['heavy_policy']!='HEAVY_CAMPAIGN_NOT_RE_RUN' for r in final): errors.append('heavy policy missing')
if any('[UNPINNED TITLE]' in r['title'] or '[DESCRIPTIVE]' in r['title'] for r in final): errors.append('placeholder title remains in final pass')
freeze=json.loads((HERE/'FREEZE.json').read_text(encoding='utf-8'))
if freeze.get('rh_status')!='UNPROVED': errors.append('RH status not UNPROVED')
p2=freeze.get('pass_two',{})
if p2.get('targeted_after')!=0 or p2.get('blank_heads_after')!=1: errors.append('freeze final counts mismatch')
result={
 'status':'PASS_REVIEWER_C_FINAL' if not errors else 'FAIL',
 'errors':errors,
 'census_rows':len(census),
 'pass_two_rows':len(final),
 'exact_heads_recovered':72,
 'no_remote_pr_objects':[417],
 'remaining_targeted':sum(r['delta_action']=='TARGETED_REVIEW_STILL_REQUIRED' for r in census),
 'remaining_blank_heads':len(blanks),
 'remaining_malformed_heads':len(mal),
 'heavy_campaigns_rerun':False,
 'rh_proved':False,
}
print(json.dumps(result,indent=2,sort_keys=True))
sys.exit(1 if errors else 0)
