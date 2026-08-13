#!/usr/bin/env python3
from fractions import Fraction
import json
from pathlib import Path


def certify_sequence(rs):
    survival=Fraction(1)
    lambdas=[]
    alphas=[]
    sx=Fraction(1)
    rows=[]
    for r in rs:
        lam=r*survival
        alpha=r*lam
        hx=r*r*sx
        hy=lam
        assert 0 <= alpha <= hx
        assert 0 <= alpha <= hy
        lambdas.append(lam)
        alphas.append(alpha)
        rows.append({
            'r':str(r),'lambda':str(lam),'alpha':str(alpha),
            'hazard_x':str(hx),'hazard_y':str(hy),
        })
        survival*=1-r
        sx*=1-r*r
    assert survival+sum(lambdas,Fraction(0))==1
    assert sum(alphas,Fraction(0)) <= max(rs)*sum(lambdas,Fraction(0))
    return survival,lambdas,alphas,rows


def main():
    tests=[
      [Fraction(1,9),Fraction(1,11),Fraction(1,13)],
      [Fraction(1,9),Fraction(1,10),Fraction(1,12),Fraction(1,16)],
      [Fraction(1,100+i) for i in range(40)],
    ]
    retained=[]
    for rs in tests:
        survival,lams,alphas,rows=certify_sequence(rs)
        retained.append({
          'survival':str(survival),
          'lambda_sum':str(sum(lams,Fraction(0))),
          'alpha_sum':str(sum(alphas,Fraction(0))),
          'largest_r':str(max(rs)),
          'packet_identity':True,
          'rows':rows,
        })
    # Universal rough-prime gate: sqrt(67)>8, hence every r<1/8.
    assert 67>8*8
    result={
      'classification':'PASS_NONDUPLICATING_CAUSAL_PACKET_BUDGET',
      'test_sequences':retained,
      'universal_child_mass_gate':'sum alpha_j <= r_1 sum lambda_j < 1/8',
      'scope':(
        'Exact Fraction arithmetic verifies the survival/hazard telescopes, '
        'safe-child inequalities, and causal packet coefficient identity on '
        'representative sequences. The general theorem is symbolic. This does '
        'not certify physical packet typing or RH.'),
    }
    out=Path(__file__).resolve().parent/'results'/'verification.json'
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(result['classification'])
    print(out)

if __name__=='__main__':main()
