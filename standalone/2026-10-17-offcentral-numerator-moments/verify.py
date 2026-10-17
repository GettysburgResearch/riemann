#!/usr/bin/env python3
"""Finite exact diagnostics, NOT analytic certification or actual L-values."""
from __future__ import annotations
import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as F
from arith import (A,H,Z0,TARGET,EMAX,E,ONE_E,poly,add,sub,mul,scale,
                   bernstein,closed_nonnegative,open_positive,real_exponent,
                   domain,density,encode)

SIGMAS=tuple(map(F,('2/3','29/40','377/500','773/1000','197/250','801/1000',
                    '813/1000','103/125','209/250','849/1000','108/125',
                    '441/500','907/1000','477/500')))
MUTATIONS=('wrong_dual_weight','erase_mask','impose_coprimality',
           'fourth_to_second','eighth_to_second','wrong_lower_count',
           'old_small_line','drop_diagonal','zero_tail_gap','old_mellin_shift')

def verify(mutation=None):
    counts=Counter()
    def ck(group,name,condition):
        counts[group]+=1
        if not condition: raise ValueError(f'{group}:{name}')
    ck('setup','mutation',mutation is None or mutation in MUTATIONS)
    ck('setup','positive_subcritical',0<2*A<1 and A+H==1)
    ck('setup','thresholds',len(SIGMAS)==14 and SIGMAS[0]==F(2,3)
       and all(x<y for x,y in zip(SIGMAS,SIGMAS[1:])) and SIGMAS[-1]<1)
    ck('setup','positive_slack',open_positive(E) and not open_positive(poly(0)))

    # Both AFE sums, all conductor sizes: linear exponents on a triangle.
    sieve=((F(1),F(0)),(F(0),F(1)),(F(5,6),F(1,3)),(F(1,3),F(5,6)))
    moments=[]
    for k,sigma in ((1,F(1,2)),(2,F(7,12)),(4,F(3,4))):
        vertices=((F(0),F(0)),(F(1),F(0)),(F(1),F(k,2)))
        original=[]; dual=[]
        for u,v in sieve:
            for q,l in vertices:
                original.append(u+(v+1-2*sigma)*l)
                dual_power=0 if mutation=='wrong_dual_weight' else k*(1-2*sigma)
                dual.append(u+(v+2*sigma-1)*l+dual_power*q)
        for j,x in enumerate(original): ck('afe_original',f'{k}_{j}',x<=1)
        for j,x in enumerate(dual): ck('afe_dual',f'{k}_{j}',x<=1)
        ck('afe_exact','unit_bound',max(original+dual)==1)
        reflection=1+2*k*(sigma-F(1,2))
        ck('afe_exact','reflected_exponent',reflection=={1:F(1),2:F(4,3),4:F(3)}[k])
        moments.append(dict(order=2*k,right_sigma=sigma,left_sigma=1-sigma,
                            right_power=F(1),left_power=reflection,
                            original_vertex_powers=original,dual_vertex_powers=dual))

    # Abstract sixth-root character with nonunit zero, NOT a real field census.
    def phase(row,vals,angles):
        if any(r and v for r,v in zip(row,vals)): return None
        return sum(v*t for v,t in zip(vals,angles))%6
    def product(x,y): return None if x is None or y is None else (x+y)%6
    for row in itertools.product(range(2),repeat=2):
        for vals in itertools.product(range(14),repeat=2):
            rem=tuple(v%6 for v in vals); power=tuple(v//6 for v in vals)
            ck('column_factor','exact_exponents',all(v==r+6*c for v,r,c in zip(vals,rem,power)))
            if mutation=='impose_coprimality':
                ck('column_factor','retain_shared_prime',not any(r and c for r,c in zip(rem,power)))
            for angles in ((1,5),(2,3)):
                lhs=phase(row,vals,angles)
                mask=True if mutation=='erase_mask' else not any(r and c for r,c in zip(row,power))
                rhs=phase(row,rem,angles) if mask else None
                ck('column_mask','sixth_power_identity',lhs==rhs)
    for k in (1,2,4):
        coeff=[1]+[0]*18
        for _ in range(k):
            coeff=[sum(coeff[:n+1]) for n in range(19)]
        for n,c in enumerate(coeff):
            ck('divisor_coeff','complete_local_convolution',c==math.comb(n+k-1,k-1))
    for order in (2,4,8):
        for vals in itertools.product(range(4),repeat=4):
            ck('holder','finite_array',sum(vals)**order<=len(vals)**(order-1)*sum(v**order for v in vals))

    ds=[density(s) for s in SIGMAS]
    for j,d in enumerate(ds):
        ck('density_setup','parameters',0<=d['r']<=d['s'] and d['z']>0)
        ck('density_setup','same_corollary',d['g']==d['corollary_g'])
        for l,t in enumerate(d['norm_terms']): ck('density_norm',f'{j}_{l}',t<=d['g'])
        for l,t in enumerate(d['height_terms']): ck('density_height',f'{j}_{l}',t<=d['height'])
        ck('density_setup','active_norm',max(d['norm_terms'])==d['g'])
        ck('density_setup','active_height',max(d['height_terms'])==d['height'])

    # Exhaustive rank model for nested E_j: rank k means membership j<k.
    for rank in range(15):
        members=[rank>j for j in range(14)]
        bins=[not members[0]]+[members[j] and not members[j+1] for j in range(13)]+[members[-1]]
        ck('partition','exactly_one',sum(bins)==1)
        for j in range(13):
            if bins[j+1]:
                count_index=j+1 if mutation=='wrong_lower_count' else j
                ck('partition','lower_count',members[count_index])
                ck('partition','upper_zero_free',not members[j+1])

    def numerator(mode,nu,y):
        if mode=='m2': return scale(add(nu,1),F(1,2))
        if mode=='m4':
            if mutation=='fourth_to_second': return add(scale(add(nu,1),F(1,2)),F(1,12))
            return add(scale(nu,F(3,4)),F(1,3))
        if mode=='m8':
            if mutation=='eighth_to_second': return add(scale(add(nu,1),F(1,2)),F(1,4))
            return add(scale(nu,F(7,8)),F(3,8))
        return add(nu,scale(sub(1,y),F(1,2)))
    rows=[('good',add(SIGMAS[0],E),poly(F(1,2)),poly(1),'m2')]
    for j in range(13):
        mode='m4' if j<2 else ('m8' if j<12 else 'convexity')
        y=poly(F(5,12) if j<2 else F(1,4)) if j<12 else add(1-SIGMAS[j+1],E)
        rows.append((f'middle_{j}',add(SIGMAS[j+1],E),y,add(ds[j]['g'],E),mode))
    rows.append(('last',ONE_E,E,add(ds[-1]['g'],E),'convexity'))
    table=[]
    for name,x,y,nu,mode in rows:
        r=numerator(mode,nu,y)
        for v in ((ONE_E,ONE_E,poly(Z0)),(x,ONE_E,poly(Z0)),(x,y,poly(Z0))):
            for j,m in enumerate(domain(*v)): ck('contour',f'{name}_{j}',open_positive(m))
        ck('row_power',name,open_positive(sub(r,Z0)))
        exponent=add(real_exponent(x,y,Z0),mul(add(H,E),sub(r,Z0)))
        budget=sub(add(TARGET,scale(E,3)),exponent)
        ck('class_budget',name,closed_nonnegative(budget))
        ck('class_constant',name,exponent[0]<=TARGET)
        table.append(dict(name=name,mode=mode,x=x,y=y,nu=nu,row_cost=r,
                          exponent=exponent,margin=TARGET-exponent[0],bernstein=bernstein(budget)))
    ck('class_setup','full_list',len(table)==15)
    ck('class_exact','good',table[0]['exponent']==poly((TARGET,F(8,5))))

    principal_vertices=((ONE_E,ONE_E,add(F(1,6),E)),
                        (ONE_E,F(1,2),add(F(1,6),E)),(ONE_E,1,add(F(1,6),E)),(ONE_E,1,E))
    for v in principal_vertices:
        for j,m in enumerate(domain(*v)): ck('principal_domain',str(j),open_positive(m))
    wrem=real_exponent(ONE_E,F(1,2),add(F(1,6),E))
    zrem=real_exponent(ONE_E,1,E)
    ck('principal_exact','w',wrem==poly((F(5,54),F(14,9))))
    ck('principal_exact','z',zrem==poly((TARGET,F(14,9))))
    for name,ex in (('w',wrem),('z',zrem)):
        ck('principal_budget',name,closed_nonnegative(sub(add(TARGET,scale(E,3)),ex)))
    zs=Z0 if mutation=='old_small_line' else F(1,3)
    small=add(real_exponent(ONE_E,F(1,2),zs),F(1,100)*(1+F(1,4)-zs))
    ck('small_budget','separate_line',closed_nonnegative(sub(add(TARGET,scale(E,3)),small)))
    for v in ((ONE_E,ONE_E,F(2)),(ONE_E,ONE_E,zs),(ONE_E,F(1,2),zs)):
        for j,m in enumerate(domain(*v)): ck('small_domain',str(j),open_positive(m))
    ck('height_tail','cutoff_bound',H+EMAX<F(14,25))
    ck('height_tail','decay',2+2*F(14,25)-F(600,100)<-1)
    # Substitute L=10/e+2 symbolically. The coefficient of 1/e cancels.
    gap=poly(0) if mutation=='zero_tail_gap' else E
    ck('large_tail','positive_gap',open_positive(gap))
    large=poly((-6+F(5,2)*A,-1))
    ck('large_tail','value',large==poly((F(-44,9),-1)))
    ck('large_tail','decay',open_positive(sub(-1,large)))
    for v in ((4,4,2),(4,4,3)):
        for j,m in enumerate(domain(*v)): ck('large_domain',str(j),open_positive(m))

    for s in SIGMAS:
        radii=(sub(2-s,scale(E,F(1,4))),sub(2-s,scale(E,F(1,2))),sub(2-s,E),sub(1,scale(E,F(1,4))))
        for i in range(3): ck('reciprocal_disks','ordered',open_positive(sub(radii[i],radii[i+1])))
        ck('reciprocal_disks','inner_positive',open_positive(radii[-1]))
        ck('reciprocal_disks','contour_inside',open_positive(sub(sub(2-s,scale(E,F(1,2))),sub(2-s,E))))
    reflected=4*A-1 if mutation=='drop_diagonal' else max(2*A,4*A-1)
    ck('theta','diagonal_retained',reflected>=2*A)
    ck('theta','full_pairing',(reflected-A)/2==TARGET)
    b0=F(17,25) if mutation=='old_mellin_shift' else 1-A/2-H/6
    ck('mellin','new_shift',b0==F(37,54))
    ck('mellin','boundary',b0+TARGET==F(49,54))
    ck('mellin','nonvanishing_domain',b0+TARGET>F(2,3))
    ck('comparison','965',F(91,100)-F(49,54)==F(7,2700))
    ck('comparison','966',F(109,120)-F(49,54)==F(1,1080))

    # Exact coefficient identities in the restricted positive-estimate model.
    for a in map(F,('1/10','1/3','4/9','9/20','1/2')):
        hh=1-a
        for y in (F(1,10),F(1,4),F(5,12),F(1,2),F(3,4)):
            if y>=F(1,2):
                at_x=F(2,3)-1+a*(y-F(1,2))+hh
                ck('model','right_difference',at_x-(F(2,3)-a)==a*(y-F(1,2)))
            else:
                at_x=(F(5,2)-y)/3-1+a*(y-F(1,2))+hh*(F(3,2)-y)
                ck('model','left_difference',at_x-(F(2,3)-a)==(2*a-F(4,3))*(y-F(1,2)))
        boundary=F(5,6)-a/3+max(a/2,F(2,3)-a)
        predicted=F(3,2)-4*a/3 if a<=F(4,9) else F(5,6)+a/6
        ck('model','two_branches',boundary==predicted)
        ck('model','floor',boundary>=F(49,54))
    return dict(status='finite_checks_passed_not_analytic_certification',
                counts=dict(sorted(counts.items())),total=sum(counts.values()),
                e_interval=['0 (excluded analytically)',str(EMAX)],moments=moments,
                density=[{k:v for k,v in d.items() if k not in ('norm_terms','height_terms')} for d in ds],
                classes=table,remainders=dict(w=wrem,z=zrem,small=small,large=large),
                theta_growth=TARGET,mellin_shift=b0,boundary=F(49,54))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mutation',choices=MUTATIONS)
    args=parser.parse_args()
    print(json.dumps(encode(verify(args.mutation)),indent=2,sort_keys=True))
