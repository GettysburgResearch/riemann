#!/usr/bin/env python3
from __future__ import annotations
import csv, json, re
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
def rows(name):
    with (HERE/name).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f,delimiter='\t'))
census=rows('PR_CENSUS.tsv')
heads=rows('HEAD_RECONCILIATION.tsv')
issues=rows('ISSUE_CENSUS.tsv')
pass2=rows('PASS2_BACKLOG.tsv')
assert len(census)==341
assert len(heads)==101
assert sum(r['status']=='EXACT_CURRENT_HEAD_RECOVERED' for r in heads)==100
assert [r['pr'] for r in heads if r['status']=='NO_REMOTE_PR_OBJECT']==['417']
assert all(re.fullmatch(r'[0-9a-f]{40}',r['reconciled_head']) for r in heads if r['status']=='EXACT_CURRENT_HEAD_RECOVERED')
assert len(issues)==171 and len({r['issue'] for r in issues})==171
assert all(r['theorem_reachability']=='EXCLUDE_UNLESS_EXACT_PR/CLAIM_OBJECT_EXISTS' for r in issues)
targeted_at_pass1={r['pr'] for r in pass2 if r['current_disposition']=='TARGETED_REVIEW_STILL_REQUIRED'}
assert len(targeted_at_pass1)==67
assert sum(r['status']=='EXACT_CURRENT_HEAD_RECOVERED' for r in heads)==100
print(json.dumps({
  'status':'PASS_REVIEWER_C_PASS1',
  'census_rows':len(census),
  'heads_recovered':100,
  'no_remote_pr_objects':[417],
  'issues_classified':len(issues),
  'remaining_targeted_at_pass1':len(targeted_at_pass1),
  'final_packet_may_have_resolved_these_rows':True,
  'heavy_campaigns_rerun':False,
  'rh_proved':False
},indent=2,sort_keys=True))
