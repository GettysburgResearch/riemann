#!/usr/bin/env python3
"""Exact finite comparison for the separately proposed 49/54 extension.

Imports rational arithmetic and the original DF detector from verify_theta.
No fourth-moment or analytic-family theorem is certified by this script.
"""
from fractions import Fraction as F
import argparse
import json
from collections import Counter
from verify_theta import Poly, Checks, density, closed_g, domain, e, EMAX

A=F(4,9); H=1-A; THETA=A/2; SHIFT=F(5,6)-A/3
Z0=F(2,5); SMALL=F(1,1000); ZSMALL=F(1,3)
THRESHOLDS=[F(i,6000) for i in range(4000,5641)]
MUTATIONS=['old-second-mean','omit-conductor','upper-count','old-small-line','old-shift','zero-tail-gap']

def scale(x,y,z):return A/2+x-1+H*z+A*(y-1)

def run(mutation=None,details=False):
    c=Checks();rows=[];vertices=[(1+e,1+e,Z0)]
    c.identity('support',2*A,F(8,9))
    c.identity('theta',THETA,F(2,9))
    c.identity('shift',F(3419,5000) if mutation=='old-shift' else SHIFT,F(37,54))
    c.identity('boundary',SHIFT+THETA,F(49,54))
    c.identity('improvement over 9081/10000',F(9081,10000)-SHIFT-THETA,F(187,270000))
    c.identity('improvement over 109/120',F(109,120)-SHIFT-THETA,F(1,1080))
    for sigma in [F(3,5),F(3,4),F(9,10)]:
        for delta in [F(1,100),F(1,1000)]:
            invp=(1+delta-sigma)/(2+4*delta)
            c.check('fourth-interpolation','finite right line',0<invp<F(1,4))
            c.check('fourth-interpolation','arbitrary small norm loss',0<=invp-(1-sigma)/2<=delta/2)
    for y in [F(1,10),F(1,4),F(2,5)]:
        for nu in [F(1,4),F(3,4),F(1)]:
            cost=0 if mutation=='omit-conductor' else F(1,2)-y
            reflected=nu*(1-y/2)+F(7,12)*y+cost
            c.identity('fourth conductor cost',reflected,F(1,2)+nu-y*(F(5,12)+nu/2))
            c.identity('fourth at center',F(1,2)+nu-F(1,2)*(F(5,12)+nu/2),3*nu/4+F(7,24))
            c.identity('fourth versus second',F(1,2)+nu*(1-y)-(F(1,2)+nu-y*(F(5,12)+nu/2)),y*(F(5,6)-nu)/2)
    for j,s in enumerate(THRESHOLDS):
        aa,bb,z,g,height=density(s)
        c.check('density-domains',str(j),F(2,3)<=s<1 and 0<aa<=bb and 0<g<1)
        c.check('density-formula',str(j),g==closed_g(s))
        if j:c.check('partition-grid',str(j),s-THRESHOLDS[j-1]==F(1,6000))
        first=[aa,F(1),aa/3+F(5,6),5*aa/6+F(1,3)]
        terms=[(F(1,2)+(F(1,2)-s)*bb+t/2,(F(1,2)-s)*z+F(1,4)) for t in first]
        terms += [((2-2*s)*bb,(2-2*s)*z),(1+(1-2*s)*aa,F(0))]
        for base,k in [(F(1,3),F(11,6)-2*s),(F(5,6),F(4,3)-2*s)]:
            terms.extend([(base+k*aa,F(0)),(base+k*bb,k*z)])
        for i,(u,v) in enumerate(terms):
            c.check('density-norm-monomials',f'{j}/{i}',u<=g)
            c.check('density-height-monomials',f'{j}/{i}',v<=height)
        R=2-s-e/4;ro=2-s-e/2;rt=2-s-e;ri=1-e/4
        for name,p in [('R-ro',R-ro),('ro-rt',ro-rt),('rt-ri',rt-ri),('ri',ri)]:
            c.positive('reciprocal-disks',f'{j}/{name}',p,True)

    def add(name,x,y,nu,method,lower=None,upper=None):
        if method=='second':numerator=(nu+1)/2
        elif method=='fourth':
            numerator=(nu+1)/2 if mutation=='old-second-mean' else 3*nu/4+F(7,24)
        elif method=='fourth-interpolated':
            numerator=F(1,2)+nu*(1-y) if mutation=='old-second-mean' else F(1,2)+nu-y*(F(5,12)+nu/2)
            c.positive('interpolation-lines',name+' lower',y,True)
            c.positive('interpolation-lines',name+' upper',F(1,2)-y,True)
        else:numerator=nu+(1-y)/2
        row=numerator-Z0
        growth=scale(x,y,Z0)+(H+e)*row
        c.positive('row-exponents',name,row,True)
        c.positive('central-budgets',name,THETA+4*e-growth,True)
        vertices.extend([(x,1+e,Z0),(x,y,Z0)])
        rows.append({'name':name,'method':method,'lower':None if lower is None else str(lower),
            'upper':None if upper is None else str(upper),'x':Poly.cast(x).strings(),
            'y':Poly.cast(y).strings(),'nu':Poly.cast(nu).strings(),
            'growth':growth.strings(),'constant_margin':str(THETA-growth(0))})
        return growth

    good=add('good',THRESHOLDS[0]+e,F(1,2),F(1),'second',upper=THRESHOLDS[0])
    c.identity('good growth at tied boundary',good,Poly(THETA,F(8,5)))
    for j,(lo,hi) in enumerate(zip(THRESHOLDS,THRESHOLDS[1:])):
        count_at=hi if mutation=='upper-count' else lo
        c.check('partition-count',str(j),count_at==lo)
        if lo<F(3,4):method='fourth';y=F(1,2)
        else:method='fourth-interpolated';y=1-hi+e
        val=add(f'middle-{j}',hi+e,y,density(count_at)[3]+e,method,lo,hi)
        c.check('middle-strict-margin',str(j),val(0)<THETA)
    add('last',1+e,e,density(THRESHOLDS[-1])[3]+e,'convexity',THRESHOLDS[-1])
    c.check('partition-count','all classes',len(rows)==1642)

    principal_w=scale(1+e,F(1,2),F(1,6)+e)
    principal_z=scale(1+e,1,e)
    zsmall=Z0 if mutation=='old-small-line' else ZSMALL
    small=scale(1+e,F(1,2),zsmall)+SMALL*(F(5,4)-zsmall)
    large=A/2+3+3*A+H-10-e
    c.identity('principal w',principal_w,Poly(F(5,54),F(14,9)))
    c.identity('principal z',principal_z,Poly(F(2,9),F(14,9)))
    c.identity('small rows',small,Poly(F(20099,108000),1))
    c.identity('large rows',large,Poly(-F(44,9),-1))
    eL=10+2*e
    c.identity('large contour cleared',e*(A/2+3+3*A)+H*eL+(H+e)*(e-eL),e*large)
    for name,p in [('principal-w',principal_w),('principal-z',principal_z),('small',small),('large',large)]:
        c.positive('other-budgets',name,THETA+4*e-p,True)
    c.positive('tail-gap','positive',0 if mutation=='zero-tail-gap' else e,True)
    c.positive('tail-gap','cutoff below .56',F(14,25)-H-e,True)
    vertices += [(1+e,1+e,F(1,6)+e),(1+e,F(1,2),F(1,6)+e),
        (1+e,1,F(1,6)+e),(1+e,1,e),(1+e,F(1,2),Z0),
        (1+e,F(1,2),ZSMALL),(4,4,2)]
    for i,v in enumerate(vertices):
        for j,p in enumerate(domain(*v)):c.positive('contour-domain',f'{i}/{j}',p,True)
    c.identity('final Mellin loss',SHIFT+THETA+5*e,Poly(F(49,54),5))
    worst=min((r for r in rows if r['name'].startswith('middle-')),key=lambda r:F(r['constant_margin']))
    return {'status':'EXACT_RATIONAL finite bookkeeping; analytic fourth-moment extension proposed',
        'a':str(A),'support':str(2*A),'theta':str(THETA),'Mellin_shift':str(SHIFT),
        'proposed_boundary':str(SHIFT+THETA),'e_interval':'0 < e <= '+str(EMAX),
        'small_norm_cutoff':str(SMALL),'small_z_line':str(ZSMALL),
        'threshold_count':len(THRESHOLDS),'class_count':len(rows),
        'method_counts':dict(sorted(Counter(r['method'] for r in rows).items())),
        'minimum_middle_constant_margin':worst,'checks':dict(sorted(c.groups.items())),
        **({'classes':rows} if details else {})}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mutation',choices=MUTATIONS)
    p.add_argument('--details',action='store_true')
    a=p.parse_args()
    print(json.dumps(run(a.mutation,a.details),sort_keys=True,indent=2))
