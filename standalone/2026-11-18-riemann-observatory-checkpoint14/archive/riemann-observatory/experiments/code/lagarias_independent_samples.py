#!/usr/bin/env python3
"""Compare directed-integer certificate with direct rational series at three samples."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json

def main():
    root=Path(__file__).resolve().parents[2]
    spec=importlib.util.spec_from_file_location('lf',root/'experiments/code/lagarias_finite.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    path=root/'experiments/results/lagarias_finite_certificate.jsonl'
    if not path.exists(): m.run()
    records={r['n']:r for r in map(json.loads,path.read_text().splitlines())}
    H=F(0);out=[]
    for n in range(1,5041):
        H+=F(1,n)
        if n not in (2,12,5040): continue
        r=records[n];x=F(r['harmonic_lower_numerator'],m.S)
        assert x<=H
        E=term=F(1)
        for k in range(1,101):term=term*x/k;E+=term
        y=(x-1)/(x+1)
        L=2*sum((y**(2*j+1)/F(2*j+1) for j in range(100)),F(0))
        assert F(m.exp_lower(r['harmonic_lower_numerator']),m.S)<=E
        assert F(m.log_lower(r['harmonic_lower_numerator']),m.S)<=L
        rhs=x+E*L
        assert rhs>r['sigma']
        assert F(r['rhs_lower_numerator'],m.S)<=rhs
        out.append({'n':n,'exact_harmonic_comparison_passed':True,'exact_rational_positive_series_comparison_passed':True,'sigma':r['sigma'],'direct_rational_truncated_gap_display_only':float(rhs-r['sigma']),'integer_certificate_gap_display_only':r['gap_numerator']/m.S})
    print(json.dumps(out,indent=2))
    (root/'experiments/results/lagarias_independent_samples.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
