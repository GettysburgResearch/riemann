#!/usr/bin/env python3
"""Prepare rational endpoint data for the separate incremental certificate.

The numerical paths are not certified. This producer uses only the chosen
84- and 104-node endpoints, then prepares independently checked full cubes.
"""
from pathlib import Path
from decimal import Decimal as D,getcontext
import argparse,hashlib,json
import numpy as np
from scipy.linalg import qr
import search_full as s
from search_gaussian_polynomial import targets


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidates',type=Path,
                   default=s.ROOT/'extension/power_extension_candidates.json')
    p.add_argument('--candidates26',type=Path,
                   default=s.ROOT/'extension/power_extension26_candidates.json')
    p.add_argument('--output',type=Path,default=s.ROOT/'incremental_parameters.json')
    args=p.parse_args();getcontext().prec=160
    models=[]
    for degree,count,path in [(24,84,args.candidates),(26,104,args.candidates26)]:
        raw=path.read_bytes();data=json.loads(raw)
        candidate=next(x for x in data['models'] if x['degree']==degree and x['nodes']==count)
        centers=list(map(D,candidate['b']));target=targets(degree);m=degree//2-1
        old=count-20
        full=[[r*x**(r-1)for x in centers]for r in range(2,m+2)]
        matrix=np.array([[float(v*x/q)for v,x in zip(row[:old],centers[:old])]
                         for row,q in zip(full,target)])
        _,_,pivot=qr(matrix,pivoting=True,mode='economic')
        active=list(map(int,pivot[:m]));J=[[row[j]for j in active]for row in full]
        cols=[s.linear_solve(J,[D(i==j)for i in range(m)])for j in range(m)]
        R=[[cols[j][i]for j in range(m)]for i in range(m)]
        model={'degree':degree,'nodes':count,'centers':[str(x)for x in centers],
               'active':active,'preconditioner':[[str(x)for x in row]for row in R],
               'radius':'1e-50','a_definition':'1/2-sum(b_j)',
               'variable_meaning':'positive b_j in exp(-a*z^2)*product(1-b_j*z^2)',
               'producer_file':path.name,
               'producer_sha256':hashlib.sha256(raw).hexdigest(),
               'endpoint_scope':'20 identical fixed cloud nodes; the numerical path is not certified'}
        models.append(model)
        print('INCREMENTAL_NEWTON_DATA',degree,count,active,flush=True)
    result={'schema':'gaussian.theta.incremental.parameters.v1',
            'status':'RATIONAL_INPUTS_NOT_CERTIFICATE','models':models}
    args.output.write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()
