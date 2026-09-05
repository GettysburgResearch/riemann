#!/usr/bin/env python3
from __future__ import annotations
import csv, hashlib, json, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
VERDICTS = {
    'REPRESENTED_BY_A','REPRESENTED_BY_B','REPRESENTED_BY_BOTH','PARTIALLY_REPRESENTED',
    'DELTA_VERIFIED','DELTA_VERIFIED_WITH_FIXES','DELTA_CONDITIONAL','DELTA_OPEN_SUFFICIENT',
    'DELTA_OPEN_RH_EQUIVALENT','DELTA_GAP','DELTA_FALSE','CONTROLLED_BY_LATER_REFUTATION',
    'CONTROLLED_BY_LATER_REVIEW','SUPERSEDED','DUPLICATE_RECOVERY','HISTORICAL_FULL_PROPOSAL',
    'RETAINED_HEAVY_CERTIFICATE','ADMINISTRATIVE_TEST','NO_NEW_MATHEMATICS',
    'TARGETED_REVIEW_STILL_REQUIRED'
}
REQUIRED = [
    'FREEZE.json','PR_CENSUS.tsv','DELTA_CLAIMS.tsv','DELTA_REFUTATIONS.tsv',
    'DELTA_ALIASES.tsv','DELTA_COMPUTATIONS.tsv','HISTORICAL_PROPOSALS.tsv',
    'PROVENANCE_DEFECTS.tsv','MISSING_COVERAGE.md','CANONICAL_SALVAGE.md','INTEGRATION_HANDOFF.md',
    'CROSS_REVIEW_FOLLOWUP.tsv','CROSS_REVIEW_FOLLOWUP.md',
    'PASS1_REPORT.md','PASS1_TARGETED_REVIEW.tsv','HEAD_RECONCILIATION.tsv',
    'ISSUE_CENSUS.tsv','ISSUE_GENEALOGY.md','PASS2_BACKLOG.tsv',
    'PASS2_FINAL_REVIEW.tsv','FINAL_HEAD_RECONCILIATION.tsv','FINAL_REPORT.md','FINAL_CLOSURE_MAP.md',
    'FINAL_PUBLICATION_INSTRUCTIONS.md'
]
PR_HEADER = ['pr','exact_head_sha','title','family','creation_or_update_scope','reviewer_a_coverage','reviewer_b_coverage','controlling_later_pr','controlling_review','strongest_surviving_result','first_broken_arrow','current_open_gate','lifecycle_recommendation','delta_action','notes']
HIST_HEADER = ['proposal_pr','proposal_head','claimed_route','first_broken_arrow','controlling_evidence','surviving_claims','current_descendant','final_classification','lifecycle_recommendation']
errors=[]; warnings=[]
for name in REQUIRED:
    if not (HERE/name).is_file(): errors.append(f'missing required file: {name}')
freeze=json.loads((HERE/'FREEZE.json').read_text())
if freeze.get('rh_status')!='UNPROVED': errors.append('RH status must be UNPROVED')
if freeze['review_inputs_only']['reviewer_b']['pr']!=708 or freeze['review_inputs_only']['reviewer_a']['pr']!=709: errors.append('review inputs wrong')

cross=freeze.get('cross_review_inputs_only',{})
expected_cross={
    'reviewer_a_cross_review_b':(710,'e91d6aa25d2e8576e82d26170127941eec430f75'),
    'reviewer_b_cross_review_a':(711,'27784928fbcecff975bc947e13c3a30d3b630ce0'),
}
for key,(pr,sha) in expected_cross.items():
    obj=cross.get(key,{})
    if obj.get('pr')!=pr or obj.get('head')!=sha:
        errors.append(f'cross-review freeze mismatch for {key}')

for label,sha in [('main',freeze['frozen_main']),('A',freeze['review_inputs_only']['reviewer_a']['head']),('B',freeze['review_inputs_only']['reviewer_b']['head'])]:
    if not re.fullmatch(r'[0-9a-f]{40}',sha): errors.append(f'malformed frozen {label} SHA: {sha}')
with (HERE/'PR_CENSUS.tsv').open(newline='',encoding='utf-8') as f:
    r=csv.DictReader(f,delimiter='\t');
    if r.fieldnames!=PR_HEADER: errors.append('PR_CENSUS header mismatch')
    census=list(r)
nums=[int(x['pr']) for x in census]
for p in range(375,708):
    if nums.count(p)!=1: errors.append(f'PR #{p} count={nums.count(p)}')
if 708 in nums or 709 in nums: errors.append('review PR appeared as research census row')
for row in census:
    if row['delta_action'] not in VERDICTS: errors.append(f"PR {row['pr']} invalid delta_action {row['delta_action']}")
    sha=row['exact_head_sha']
    if row['pr']=='417':
        if sha or row['delta_action']!='NO_NEW_MATHEMATICS': errors.append('PR 417 sequence-gap record malformed')
    elif not re.fullmatch(r'[0-9a-f]{40}',sha or '') or sha.endswith('0'*32):
        errors.append(f"PR {row['pr']} unresolved or malformed exact head in final packet")
with (HERE/'HISTORICAL_PROPOSALS.tsv').open(newline='',encoding='utf-8') as f:
    r=csv.DictReader(f,delimiter='\t')
    if r.fieldnames!=HIST_HEADER: errors.append('HISTORICAL_PROPOSALS header mismatch')
    for row in r:
        if row['final_classification'] not in VERDICTS: errors.append(f"historical PR {row['proposal_pr']} invalid classification")
for fn,col in [('DELTA_CLAIMS.tsv','verdict'),('DELTA_REFUTATIONS.tsv','verdict'),('DELTA_ALIASES.tsv','status'),('DELTA_COMPUTATIONS.tsv','verdict')]:
    with (HERE/fn).open(newline='',encoding='utf-8') as f:
        r=csv.DictReader(f,delimiter='\t')
        seen=[]
        for row in r:
            if row[col] not in VERDICTS: errors.append(f"{fn}: invalid {col}={row[col]}")
            key=next(iter(row.values()))
            seen.append(key)
            if fn=='DELTA_COMPUTATIONS.tsv' and row['heavy_campaign_not_re_run']!='HEAVY_CAMPAIGN_NOT_RE_RUN': errors.append(f"{fn}: missing heavy flag for {key}")
        dups=[k for k,v in Counter(seen).items() if v>1]
        if dups: errors.append(f'{fn}: duplicate primary IDs {dups}')

with (HERE/'CROSS_REVIEW_FOLLOWUP.tsv').open(newline='',encoding='utf-8') as f:
    r=csv.DictReader(f,delimiter='\t')
    expected_header=['handoff_pr','handoff_head','candidate_id','source_pr','source_head','source_claim','prior_packet_status','followup_disposition','canonical_record','notes']
    if r.fieldnames!=expected_header: errors.append('CROSS_REVIEW_FOLLOWUP header mismatch')
    cross_rows=list(r)
if len(cross_rows)!=22: errors.append(f'cross-review candidate count={len(cross_rows)}')
if len({x['candidate_id'] for x in cross_rows})!=22: errors.append('duplicate cross-review candidate ID')
if {x['handoff_pr'] for x in cross_rows}!={'710','711'}: errors.append('cross-review handoff PR set mismatch')
for row in cross_rows:
    if not re.fullmatch(r'[0-9a-f]{40}',row['source_head']): errors.append(f"cross-review malformed source head {row['candidate_id']}")


# Pass-one exact-head and issue archaeology checks.
with (HERE/'HEAD_RECONCILIATION.tsv').open(newline='',encoding='utf-8') as f:
    hr=list(csv.DictReader(f,delimiter='\t'))
if len(hr)!=101 or {int(x['pr']) for x in hr}!=set(range(399,500)):
    errors.append('HEAD_RECONCILIATION must cover PRs 399-499 exactly once')
if sum(x['status']=='EXACT_CURRENT_HEAD_RECOVERED' for x in hr)!=100:
    errors.append('pass-one recovered-head count mismatch')
if [x['pr'] for x in hr if x['status']=='NO_REMOTE_PR_OBJECT']!=['417']:
    errors.append('pass-one no-PR-object record mismatch')
for x in hr:
    if x['status']=='EXACT_CURRENT_HEAD_RECOVERED' and not re.fullmatch(r'[0-9a-f]{40}',x['reconciled_head']):
        errors.append(f"pass-one malformed reconciled head PR {x['pr']}")

with (HERE/'PASS1_TARGETED_REVIEW.tsv').open(newline='',encoding='utf-8') as f:
    p1=list(csv.DictReader(f,delimiter='\t'))
if len(p1)!=101 or {int(x['pr']) for x in p1}!=set(range(399,500)):
    errors.append('PASS1_TARGETED_REVIEW must cover PRs 399-499 exactly once')

with (HERE/'ISSUE_CENSUS.tsv').open(newline='',encoding='utf-8') as f:
    issue_rows=list(csv.DictReader(f,delimiter='\t'))
if len(issue_rows)!=171 or len({x['issue'] for x in issue_rows})!=171:
    errors.append(f'issue census count/uniqueness mismatch: {len(issue_rows)}')
if any(x['theorem_reachability']!='EXCLUDE_UNLESS_EXACT_PR/CLAIM_OBJECT_EXISTS' for x in issue_rows):
    errors.append('issue theorem-reachability firewall missing')

with (HERE/'PASS2_BACKLOG.tsv').open(newline='',encoding='utf-8') as f:
    pass2=list(csv.DictReader(f,delimiter='\t'))
targeted={x['pr'] for x in census if x['delta_action']=='TARGETED_REVIEW_STILL_REQUIRED'}
if targeted:
    errors.append(f'final packet retains targeted rows: {sorted(targeted)}')
with (HERE/'PASS2_FINAL_REVIEW.tsv').open(newline='',encoding='utf-8') as f:
    final2=list(csv.DictReader(f,delimiter='\t'))
with (HERE/'FINAL_HEAD_RECONCILIATION.tsv').open(newline='',encoding='utf-8') as f:
    finalh=list(csv.DictReader(f,delimiter='\t'))
if len(pass2)!=73 or len(final2)!=73 or len(finalh)!=73:
    errors.append('pass-two/final-resolution row count mismatch')
if {x['pr'] for x in pass2}!={x['pr'] for x in final2} or {x['pr'] for x in pass2}!={x['pr'] for x in finalh}:
    errors.append('pass-two/final-resolution key mismatch')
if [x['pr'] for x in finalh if x['status']=='NO_REMOTE_PR_OBJECT']!=['417']:
    errors.append('final no-remote-object set mismatch')
if sum(x['status']=='EXACT_CURRENT_HEAD_RECOVERED' for x in finalh)!=72:
    errors.append('final recovered-head count mismatch')

# Provenance file must retain malformed-SHA evidence rather than normalize it away.
prov=(HERE/'PROVENANCE_DEFECTS.tsv').read_text(encoding='utf-8')
if '928fd615d753882706bb88c51b717bd8d4a86ba' not in prov: errors.append('known A malformed SHA defect missing')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'warnings':warnings,'census_rows':len(census),'post_cutoff_rows':sum(375<=n<=707 for n in nums),'cross_review_candidates':len(cross_rows),'unresolved_heads':sum(not re.fullmatch(r'[0-9a-f]{40}',x['exact_head_sha'] or '') or x['exact_head_sha'].endswith('0'*32) for x in census)}
print(json.dumps(result,indent=2,sort_keys=True))
sys.exit(0 if not errors else 1)
