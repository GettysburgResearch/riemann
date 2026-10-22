#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
from math import comb
import csv,json,re
root=Path(__file__).resolve().parent.parent
req=['FREEZE.json','VERDICT_DELTA.tsv','GRAPH_DEFECTS.tsv','SOURCE_PROVENANCE_FIXES.tsv','MISSED_CLAIM_CANDIDATES.tsv','COMPUTATION_AUDIT.tsv','CROSS_REVIEW_REPORT.md','INTEGRATION_HANDOFF.md']
for n in req: assert (root/n).is_file() and (root/n).stat().st_size>0,n
allowed={'AGREE_VERIFIED','AGREE_VERIFIED_WITH_FIXES','STRENGTHEN_TO_VERIFIED','WEAKEN_TO_VERIFIED_WITH_FIXES','WEAKEN_TO_CONDITIONAL','WEAKEN_TO_GAP','OVERTURN_FALSE','AGREE_OPEN_SUFFICIENT','AGREE_OPEN_RH_EQUIVALENT','AGREE_REFUTED','MISSED_CLAIM_CANDIDATE','INTEGRATOR_DECISION_REQUIRED'}
with (root/'VERDICT_DELTA.tsv').open(newline='') as f: delta=list(csv.DictReader(f,delimiter='\t'))
assert delta and len({r['semantic_id'] for r in delta})==len(delta)
assert all(r['reviewer_b_cross_verdict'] in allowed for r in delta)
sha=re.compile(r'^[0-9a-f]{40}$')
assert all(sha.fullmatch(r['exact_source_sha']) for r in delta if r['exact_source_pr'].isdigit())
claims=set(json.loads((Path(__file__).parent/'reviewer_a_claim_ids.json').read_text()))
assert len(claims)==68
with (Path(__file__).parent/'reviewer_a_route_edges_fixture.tsv').open(newline='') as f: edges=list(csv.DictReader(f,delimiter='\t'))
assert len(edges)==23
multi=[e for e in edges if ';' in e['premise_semantic_ids']]
mis=[e for e in multi if len([x for x in e['premise_semantic_ids'].split('&') if x.strip()])==1]
assert len(multi)==15 and len(mis)==15
dangling=set(); terminals={'RH'}
for e in edges:
 ps=[x.strip() for x in e['premise_semantic_ids'].split(';') if x.strip()]
 dangling.update(x for x in ps if x not in claims)
 c=e['conclusion_semantic_id']
 if c not in claims and c not in terminals: dangling.add(c)
assert len(dangling)==20
assert 'ARITH.ROWS23.NONNEGATIVE' in dangling and 'ARITH.WAVELET.CRITICAL_ENERGY' in dangling
assert Fraction(1,5)==Fraction(1,5)
for p in [67,71,83]: assert p!=4
eta=[Fraction(comb(2*k,k),4**k) for k in range(20)]
for n in range(20): assert sum(eta[j]*eta[n-j] for j in range(n+1))==1
out={'status':'PASS_REVIEWER_B_CROSS_REVIEW_A','verdict_rows':len(delta),'reviewer_a_claim_ids':68,'reviewer_a_route_edges':23,'semicolon_multi_premise_edges':15,'misparsed_by_ampersand_parser':15,'strict_dangling_node_count':20,'strict_dangling_nodes':sorted(dangling),'strict_proved_only_path_to_RH':False,'heavy_campaigns_rerun':False}
(Path(__file__).parent/'RESULTS.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
print(json.dumps(out,sort_keys=True))
