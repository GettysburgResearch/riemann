#!/usr/bin/env python3
"""Prepare rational Newton data for the separate directed checker.

This producer may use ordinary Decimal arithmetic and floating-point QR. The
checker recomputes all load-bearing inequalities with directed intervals.
"""
from pathlib import Path
from decimal import Decimal as D,getcontext
import argparse,json
import numpy as np
from scipy.linalg import qr
import search_full as s


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidates',type=Path,default=s.ROOT/'gaussian_candidates.json')
    p.add_argument('--output',type=Path,default=s.ROOT/'gaussian_parameters.json')
    args=p.parse_args()
    getcontext().prec=160
    chosen=json.loads(args.candidates.read_text())
    if chosen['schema']!='gaussian.theta.chosen_candidates.v1':
        raise ValueError('unexpected curated candidate schema')
    models=[]
    for degree,count in ((22,64),(24,128),(26,128)):
        candidate=next(r for r in chosen['models'] if r['degree']==degree
                       and r['nodes']==count and r['settled'])
        centers=list(map(D,candidate['b']))
        target=list(map(D,candidate['target']))
        m=degree//2-1
        full=[[r*x**(r-1) for x in centers]for r in range(2,m+2)]
        matrix=np.array([[float(v*x/q)for v,x in zip(row,centers)]for row,q in zip(full,target)])
        _,_,piv=qr(matrix,pivoting=True,mode='economic')
        active=list(map(int,piv[:m]))
        J=[[row[j]for j in active]for row in full]
        cols=[s.linear_solve(J,[D(i==j)for i in range(m)])for j in range(m)]
        R=[[cols[j][i]for j in range(m)]for i in range(m)]
        model={'degree':degree,'nodes':count,'centers':[str(x)for x in centers],
               'active':active,'preconditioner':[[str(x)for x in row]for row in R],
               'radius':'1e-50','producer_file':candidate['source_file'],
               'variable_meaning':'positive b_j in exp(-a*z^2)*product(1-b_j*z^2)',
               'a_definition':'1/2-sum(b_j)'}
        models.append(model)
        print('GAUSSIAN_NEWTON_DATA',degree,count,active,
              'R_INFINITY_NORM',max(sum(abs(x)for x in row)for row in R),flush=True)
    output={'schema':'gaussian.theta.jets.parameters.v1',
            'status':'RATIONAL_INPUTS_NOT_CERTIFICATE','models':models}
    args.output.write_text(json.dumps(output,indent=2)+'\n')


if __name__=='__main__':main()
