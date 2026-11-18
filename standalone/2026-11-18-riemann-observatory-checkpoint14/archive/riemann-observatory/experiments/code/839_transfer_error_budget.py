"""Exact exploration of the frozen transfer's uniform kernel-error budget.
This does not verify the local inequality or improve an asymptotic zero proportion.
"""
from pathlib import Path
from fractions import Fraction as F
import itertools,json,hashlib
B=Path(__file__).resolve().parents[2]
pth=B/'experiments/inputs/839_first_window/inputs.json';raw=pth.read_bytes();p=json.loads(raw)
pairs=list(itertools.combinations(range(7),2));D=p['denominator']
rows=[]
for labels in itertools.product([0,1],repeat=7):
 val=sum(p['weights'][labels[i]+labels[j]][r] for r,(i,j) in enumerate(pairs))
 rows.append((val,labels))
maximum,lab=max(rows);minimum,_=min(rows)
assert maximum==47999993 and lab==(1,)*7
assert minimum==11999992
result={'kind':'exact_frozen_uniform_error_budget_exploration','input_sha256':hashlib.sha256(raw).hexdigest(),'labelings_checked':len(rows),'pair_count':21,'max_total_local_weight':str(F(maximum,D)),'maximizer_labels_0simple_1double':list(lab),'min_total_local_weight':str(F(minimum,D)),'old_per_site_error_coefficient':'48','relative_coefficient_gain':str((F(48)-F(maximum,D))/48),'conditional_refinement':'For chain length ell>=6, original nonnegative near energies and uniform kernel defect epsilon, the direct local-window sum costs at most(47999993/10^6)*epsilon*max(ell-6,0). This follows by replacing each local kernel square by e+epsilon before applying the nonnegative weight cap. This M refinement is asserted only for nonnegative near energies; the signed-energy extension retains the previously documented per-pair shifted-energy defect D_delta instead.','conclusion':'The worst-case label pattern almost saturates48. This exploration gives only a negligible uniform coefficient improvement and no asymptotic density gain; do not prioritize it over pressure-aware boundary work.'}
(B/'experiments/results/839_transfer_error_budget.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
