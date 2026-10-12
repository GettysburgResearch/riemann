#!/usr/bin/env python3
"""Ordinary R reconnaissance for convex mixtures of two reviewed global lines.
This file supplies no directed continuum sign certificate.
"""
import sys,json
from pathlib import Path
import numpy as np
from flint import arb,arb_mat,ctx
from physical_length_source import OLD,LengthSource,PhysicalSource,build_length,projection_gram

class Moments(LengthSource):
    moment=PhysicalSource.moment
    basis_moment=PhysicalSource.basis_moment

def run(kind):
    ctx.prec=256;L=arb(21)/20 if kind=='21/20' else arb(3).log();last=128
    source,u,coef,_=build_length(L,7,100);ms=Moments(L)
    fc=arb_mat([ms.basis_moment(t,7,100) for t in list(range(last+1))+['sinh']])*coef
    pp=arb_mat([[fc[i,j] for j in range(10)] for i in list(range(8))+[last+1]])
    proj=projection_gram(7,ms).solve(pp);protected=arb_mat(121,10)
    for n in range(8,129):
        cross=ms.b*((-1)**n*(ms.b*L).cosh()-1)/(ms.b**2+(arb.pi()*n/L)**2)
        for j in range(10):protected[n-8,j]=fc[n,j]-cross*proj[8,j]
    sample=json.loads((OLD/('exploratory_length_21over20.json' if kind=='21/20' else 'exploratory_length_log3.json')).read_text())
    r=np.array(sample['sampled_R_matrix']);U=np.array([[float(u[i,j].mid()) for j in range(10)] for i in range(10)])
    moments=np.array([[float(protected[i,j].mid()) for j in range(10)] for i in range(121)])
    lf=float(L.mid());grid=[]
    for theta in np.arange(0,1.0001,.025):
        alpha=.8+.5*theta;constant=244+466*theta
        first=alpha-constant*lf*lf/(8*np.pi)**2
        if first<=0:continue
        tail=1/(alpha-constant*lf*lf/(129*np.pi)**2);cost=1.5*tail*r
        for n in range(8,129):
            delta=1/(alpha-constant*lf*lf/(n*np.pi)**2)-tail;row=moments[n-8]
            cost+=3/lf*delta*np.outer(row,row)
        eigen=np.linalg.eigvalsh(U-cost)
        grid.append({'theta_display':float(theta),'minimum_weight_display':first,'ordinary_minimum_lower_eigenvalue':float(eigen[0])})
    best=max(grid,key=lambda x:x['ordinary_minimum_lower_eigenvalue'])
    return {'status':'ORDINARY_R_SUPPORTING_LINE_MIXTURE_DISCOVERY_ONLY','exact_length':kind,'grid':grid,'best':best,
       'complete_source_moments_are_directed_but_converted_to_float':True,'R_is_ordinary_old_sample':True,
       'not_proved':['weighted native sign','positive effective operator','RH']}

if __name__=='__main__':
    out=Path(__file__).with_name('supporting_line_mixture_reconnaissance.json');result={k:run(k) for k in ['21/20','log3']};out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v['best'] for k,v in result.items()},indent=2))
