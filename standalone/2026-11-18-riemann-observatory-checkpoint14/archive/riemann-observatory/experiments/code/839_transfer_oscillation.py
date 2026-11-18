"""Exact first-window state-oscillation bound from the bundled frozen potentials."""
from pathlib import Path
import json
B=Path(__file__).resolve().parents[2];p=json.loads((B/'experiments/inputs/839_first_window/inputs.json').read_text());K=p['cob_knots'];parts=[]
assert len(K)==6 and all(sum(K[i][t][k] for i in range(6))==0 for t in range(3) for k in range(14))
for r in range(5):
 vals=[0]+[sum(K[i][t][k] for i in range(r+1)) for t in range(3) for k in range(14)];parts.append(max(vals)-min(vals))
out={'kind':'exact_frozen_potential_oscillation_bound','prefix_oscillation_integer_bounds':parts,'sum':sum(parts),'denominator':p['denominator'],'omega':'15882/1000000','matches_source_omega':sum(parts)==15882,'reason':'Each prefix potential is piecewise linear on shared knots, zero outside; extrema across all pair types occur at knots or exterior0. Summing individual oscillations bounds the coupled state oscillation.'}
assert out['matches_source_omega'];(B/'experiments/results/839_transfer_oscillation.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
