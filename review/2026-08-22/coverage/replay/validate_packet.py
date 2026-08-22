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
    'PROVENANCE_DEFECTS.tsv','MISSING_COVERAGE.md','CANONICAL_SALVAGE.md','INTEGRATION_HANDOFF.md'
]
PR_HEADER = ['pr','exact_head_sha','title','family','creation_or_update_scope','reviewer_a_coverage','reviewer_b_coverage','controlling_later_pr','controlling_review','strongest_surviving_result','first_broken_arrow','current_open_gate','lifecycle_recommendation','delta_action','notes']
HIST_HEADER = ['proposal_pr','proposal_head','claimed_route','first_broken_arrow','controlling_evidence','surviving_claims','current_descendant','final_classification','lifecycle_recommendation']
errors=[]; warnings=[]
for name in REQUIRED:
    if not (HERE/name).is_file(): errors.append(f'missing required file: {name}')
freeze=json.loads((HERE/'FREEZE.json').read_text())
if freeze.get('rh_status')!='UNPROVED': errors.append('RH status must be UNPROVED')
if freeze['review_inputs_only']['reviewer_b']['pr']!=708 or freeze['review_inputs_only']['reviewer_a']['pr']!=709: errors.append('review inputs wrong')
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
    if not re.fullmatch(r'[0-9a-f]{40}',sha or '') or sha.endswith('0'*32):
        if row['delta_action']!='TARGETED_REVIEW_STILL_REQUIRED' and row['delta_action'] not in {'ADMINISTRATIVE_TEST','NO_NEW_MATHEMATICS'}:
            errors.append(f"PR {row['pr']} unresolved head without fail-closed action")
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
# Provenance file must retain malformed-SHA evidence rather than normalize it away.
prov=(HERE/'PROVENANCE_DEFECTS.tsv').read_text(encoding='utf-8')
if '928fd615d753882706bb88c51b717bd8d4a86ba' not in prov: errors.append('known A malformed SHA defect missing')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'warnings':warnings,'census_rows':len(census),'post_cutoff_rows':sum(375<=n<=707 for n in nums),'unresolved_heads':sum(not re.fullmatch(r'[0-9a-f]{40}',x['exact_head_sha'] or '') or x['exact_head_sha'].endswith('0'*32) for x in census)}
print(json.dumps(result,indent=2,sort_keys=True))
sys.exit(0 if not errors else 1)
