#!/usr/bin/env python3
from pathlib import Path
from fractions import Fraction
from math import comb
import csv, json, hashlib
root=Path(__file__).resolve().parent.parent
required=['FREEZE.json','CLAIMS.tsv','ROUTE_EDGES.tsv','ALIASES.tsv','REFUTATIONS.tsv','COMPUTATIONS.tsv','FIXES.md','REPORT.md','INTEGRATION_HANDOFF.md']
for name in required:
    assert (root/name).exists(), name
with (root/'CLAIMS.tsv').open() as f:
    claims=list(csv.DictReader(f,delimiter='\t'))
with (root/'ROUTE_EDGES.tsv').open() as f:
    edges=list(csv.DictReader(f,delimiter='\t'))
assert len(claims)>=30
assert len({r['semantic_id'] for r in claims})==len(claims)
# Exact rows-2/3 elimination factor.
# -3(a-1)(a-2) = -3a^2+9a-6
for a in [Fraction(0),Fraction(1,2),Fraction(-2,3),Fraction(7,11)]:
    assert -3*(a-1)*(a-2)==-3*a*a+9*a-6
# eta*eta=1 on prime powers.
N=32
eta=[Fraction(comb(2*k,k),4**k) for k in range(N+1)]
for n in range(N+1):
    assert sum(eta[j]*eta[n-j] for j in range(n+1))==1
# Native alpha mutation differs for representative rational r.
for r in [Fraction(1,67),Fraction(1,71),Fraction(2,3)]:
    assert r != 2*r*r
# Typed proved-only reachability.
proved={'VERIFIED','VERIFIED_WITH_FIXES'}
known={r['semantic_id'] for r in claims if r['mathematical_verdict'] in proved}
changed=True
while changed:
    changed=False
    for e in edges:
        if e['review_verdict'] not in proved:
            continue
        premises=[x.strip() for x in e['premise_semantic_ids'].split('&') if x.strip()]
        if premises and all(x in known for x in premises) and e['conclusion_semantic_id'] not in known:
            known.add(e['conclusion_semantic_id']); changed=True
assert 'RH' not in known
summary={
  'status':'PASS_REVIEWER_A_RECOVERY_PACKET',
  'claim_rows':len(claims),
  'route_edges':len(edges),
  'proven_only_path_to_RH':False,
  'heavy_campaigns_rerun':False,
  'required_files':required,
}
print(json.dumps(summary,sort_keys=True))
