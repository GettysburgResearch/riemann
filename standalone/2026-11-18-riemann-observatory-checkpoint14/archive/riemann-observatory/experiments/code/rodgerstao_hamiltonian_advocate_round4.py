#!/usr/bin/env python3
"""Exact rational local Hamiltonian identity checks (not a heat-flow proof)."""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import json


def check(points, subset):
    K = set(subset)
    velocity = [2*sum((1/(x-y) for j,y in enumerate(points) if j != i),F(0))
                for i,x in enumerate(points)]
    lhs = -sum(((velocity[k]-velocity[l])/(points[k]-points[l])
                for k in K for l in K if k != l),F(0))
    energy = sum((1/(points[k]-points[l])**2
                  for k in K for l in K if k != l),F(0))
    cross = sum((1/((points[i]-points[k])*(points[i]-points[l]))
                 for i in range(len(points)) if i not in K
                 for k in K for l in K if k != l),F(0))
    assert lhs == -4*energy+2*cross
    if max(K)-min(K)+1 == len(K):
        assert cross >= 0


def main():
    count = 0
    for size in range(3,10):
        points = [F(i*i+3*i-2, i+1) for i in range(size)]
        for k in range(2,size+1):
            for subset in combinations(range(size), k):
                check(points, subset)
                count += 1
    # Exact family witnessing the printed max-endpoint bound's scope failure:
    # at j=a in I=[a,2a], the leading odd-cube sum includes r=1 and is >=1,
    # while 1/max(j-a,2a-j)^2=1/a^2.
    endpoint = []
    for a in [4,8,16,32,64]:
        cutoff = (a-1)//2
        odd_sum = sum((F(1,r**3) for r in range(1,cutoff+1)),F(0))
        ratio = odd_sum*a*a
        assert ratio >= a*a
        endpoint.append({'a':a,'ratio_to_printed_scale_exact':str(ratio)})
    out = {'status':'all_exact_assertions_passed','hamiltonian_checks':count,
           'arithmetic':'Python standard-library Fraction',
           'endpoint_scope_witnesses':endpoint,
           'scope':'Finite local algebra and an explicit asymptotic scale witness only; not certification of infinite zero dynamics or the entire paper.'}
    target=Path(__file__).resolve().parents[1]/'results'/'rodgerstao_hamiltonian_advocate_round4.json'
    target.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
