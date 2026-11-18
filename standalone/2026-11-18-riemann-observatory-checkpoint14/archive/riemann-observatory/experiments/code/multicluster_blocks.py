#!/usr/bin/env python3
"""UNVALIDATED float checks of phase-separated finite cluster blocks.
Uses stable local DD series, not raw close-node subtraction.
"""
import cmath,math,json
from pathlib import Path
from multicluster_uniform import h_coeffs,values,solve

def delta_const(m,R):
    T=sum((2*j+1)*math.comb(m+j,m-j-1)**2*math.comb(2*j,j)**2 for j in range(m))
    s=1/(1+2*R*math.sqrt(m*T))
    return s**(2*m-1)/(4*T)

def gram(groups,L):
    co=[h_coeffs(offsets) for _,offsets in groups]
    m=sum(len(z) for _,z in groups);g=[[0j]*m for _ in range(m)]
    for k in range(L+1):
        x=k/L;vec=[]
        for (center,_),cf in zip(groups,co):
            vec.extend(cmath.exp(1j*center*x)*z for z in values(cf,x))
        for j in range(m):
            for t in range(m):g[j][t]+=vec[j]*vec[t].conjugate()/(L+1)
    return g
rows=[]
for size,L,kind in [(1,64,'separated'),(1,128,'separated'),(1,512,'near_alias'),
                     (2,2048,'separated'),(2,4096,'separated')]:
    center=math.pi*L if kind=='separated' else 2*math.pi*L+1
    groups=[(0,[0]*size),(center,[0]*size)]
    m=2*size;p=2;q=size;R=0.0;delta=delta_const(size,R);D=2*size*size
    sigma=(L+1)*abs(1-cmath.exp(1j*center/L));eps=2*m*(q+R)/sigma
    g=gram(groups,L);b=[1]+[0]*(size-1)+[1]+[0]*(size-1)
    v=solve(g,b);full=L/(L+1)*sum(x.conjugate()*y for x,y in zip(b,v)).real
    loc=gram([groups[0]],L);lv=solve(loc,[1]+[0]*(size-1));local_sum=2*L*lv[0].real/(L+1)
    cond=L>=2*D/delta and eps<=delta/4
    rows.append({'size_per_group':size,'L':L,'case':kind,'center_difference_float':center,
       'phase_separation_sigma_float':sigma,'cross_epsilon_float':eps,
       'sufficient_conditions_hold_float':cond,'scaled_full_optimum_float':full,
       'sum_scaled_local_optima_float':local_sum,'absolute_difference_float':abs(full-local_sum),
       'conditional_bound_float':8*p*eps/delta**2 if cond else None})
pth=Path(__file__).resolve().parents[1]/'results'/'multicluster_blocks.json'
pth.write_text(json.dumps({'arithmetic':'UNVALIDATED double precision; analytic Abel proof is source of theorem','rows':rows},indent=2)+'\n')
print(pth)
for r in rows:print(r['case'],r['size_per_group'],r['L'],'condition',r['sufficient_conditions_hold_float'],'difference',r['absolute_difference_float'])
