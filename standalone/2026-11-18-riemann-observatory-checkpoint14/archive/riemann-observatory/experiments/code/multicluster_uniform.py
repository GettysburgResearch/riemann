#!/usr/bin/env python3
"""UNVALIDATED float experiments for fixed-m colliding frequency clusters.
Standard library only. No close-node divided-difference subtraction is used.
The analytic proofs are in proposals/independent_campaigns/multicluster_uniform.md.
"""
import cmath,math,json
from pathlib import Path
from fractions import Fraction

def h_coeffs(nodes,terms=60):
    m=len(nodes);ans=[]
    for j in range(m):
        hom=[0.0]*terms;hom[0]=1.0
        for c in nodes[:j+1]:
            for r in range(1,terms):hom[r]+=c*hom[r-1]
        ans.append([math.factorial(j)*(1j)**r*hom[r]/math.factorial(j+r) for r in range(terms)])
    return ans

def values(coeffs,x):
    ans=[]
    for j,co in enumerate(coeffs):
        z=0j
        for a in reversed(co):z=z*x+a
        ans.append(x**j*z)
    return ans

def sample_gram(coeffs,L,simpson=False):
    m=len(coeffs);a=[[0j]*m for _ in range(m)]
    for k in range(L+1):
        z=values(coeffs,k/L)
        weight=(1 if k in [0,L] else (4 if k%2 else 2)) if simpson else 1
        for j in range(m):
            for t in range(m):a[j][t]+=weight*z[j]*z[t].conjugate()
    scale=1/(3*L) if simpson else 1/(L+1)
    return [[v*scale for v in row] for row in a]

def solve(a,b):
    a=[list(row)+[z] for row,z in zip(a,b)];m=len(b)
    for k in range(m):
        p=max(range(k,m),key=lambda j:abs(a[j][k]));a[k],a[p]=a[p],a[k]
        pivot=a[k][k]
        if abs(pivot)<1e-14:raise ArithmeticError('Float matrix nearly singular: no validated conclusion.')
        a[k]=[v/pivot for v in a[k]]
        for j in range(m):
            if j!=k:
                q=a[j][k];a[j]=[x-q*y for x,y in zip(a[j],a[k])]
    return [row[-1] for row in a]

def exact_coalesced(L,m):
    product=Fraction(1)
    for j in range(m):product*=Fraction(L-j,L+j+1)
    return 1-product

def run():
    configurations=[[0.0],[0.0,0.0],[0.0,1e-8],[-1,1],
       [0,0,0],[-1,-1,1],[-1,0,1],[-1,-1+1e-8,1],
       [0,0,0,0],[-1,-1,1,1],[-1,-0.5,0.5,1]]
    rows=[]
    for nodes in configurations:
        m=len(nodes);co=h_coeffs(nodes);g=sample_gram(co,2048,True)
        v=solve(g,[1]+[0]*(m-1));kappa=v[0].real
        ends=[values(co,0),values(co,1)]
        beta=sum(abs(sum(z.conjugate()*w for z,w in zip(h,v)))**2 for h in ends)/2
        for N in [0,8,32,128]:
            L=N+m;gs=sample_gram(co,L);vs=solve(gs,[1]+[0]*(m-1))
            scaled=L*vs[0].real/(L+1)
            record={'nodes':nodes,'N':N,'L':L,'kappa_float':kappa,'beta_float':beta,
              'scaled_optimum_float':scaled,'L_times_first_error_float':L*(scaled-kappa),
              'L2_times_corrected_error_float':L*L*(scaled-kappa+beta/(L+1))}
            if len(set(nodes))==1:
                ex=exact_coalesced(L,m)
                record['exact_coalesced_error_squared']=str(ex)
                record['float_vs_exact_abs_error']=abs(scaled-L*float(ex))
                record['kappa_vs_m_squared_abs_error']=abs(kappa-m*m)
                record['beta_vs_formula_abs_error']=abs(beta-(m**4+m*m)/2)
            rows.append(record)
    out=Path(__file__).resolve().parents[1]/'results'/'multicluster_uniform.json'
    out.write_text(json.dumps({'arithmetic':'UNVALIDATED double precision; source proof does not rely on these values',
       'basis':'convergent complete homogeneous polynomial series,60 terms',
       'continuous_gram':'composite Simpson2048 subintervals, not interval arithmetic',
       'cases':len(rows),'rows':rows},indent=2)+'\n')
    print(out);print('Cases:',len(rows))
    print('Max coalesced float-vs-exact error:',max(r.get('float_vs_exact_abs_error',0) for r in rows))
if __name__=='__main__':run()
