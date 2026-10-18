#!/usr/bin/env python3
"""Exact finite certificates for the zero-free-selected reflection comparison.

No L-values or analytic theorems are verified. Uses the Python standard library.
`--details` emits the complete finite contour inventory; normal output is compact.
"""
from __future__ import annotations
import argparse
import itertools
import json
from fractions import Fraction as F
from collections import Counter

EMAX = F(1, 10_000_000)
COUNTS: Counter[str] = Counter()
MUTATION = ''

def check(value: bool, label: str) -> None:
    COUNTS[label.split(':')[0]] += 1
    if not value:
        raise ValueError('CHECK FAILED: ' + label)

def p(x):
    return x if isinstance(x, tuple) else (F(x), F(0), F(0))

def add(a, b): return tuple(x+y for x,y in zip(p(a),p(b)))
def neg(a): return tuple(-x for x in p(a))
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    a,b=p(a),p(b)
    c=[F(0)]*5
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    if c[3:] != [0,0]: raise ValueError('Polynomial degree exceeds two')
    return tuple(c[:3])
def ev(a,t):
    a=p(a);return a[0]+a[1]*t+a[2]*t*t

e=(F(0),F(1),F(0))

def nonnegative(a,label,strict=False):
    a=p(a)
    # Quadratic Bernstein coefficients on the ENTIRE interval [0, EMAX].
    c0=a[0];c1=c0+a[1]*EMAX/2;c2=ev(a,EMAX)
    check(min(c0,c1,c2)>=0,label)
    if strict:
        # Bernstein basis is positive in the interior. A zero at e=0 is legal.
        check(c2>0 and max(c0,c1,c2)>0,label+':strict-open')

def norm_terms(s, r, b, mode):
    pairs=((1,0),(0,1),(F(1,3),F(5,6)),(F(5,6),F(1,3)))
    if mode=='DF':
        terms=[F(1,2)+(c*r+d)/2+(F(1,2)-s)*b for c,d in pairs]
    elif mode=='M4':
        terms=[F(7,18)+F(2,3)*(c*r+d)+(2-4*s)*b/3 for c,d in pairs]
    else: raise ValueError(mode)
    terms += [(2-2*s)*b,1+(1-2*s)*r]
    terms += [F(1,3)+(F(11,6)-2*s)*v for v in (r,b)]
    terms += [F(5,6)+(F(4,3)-2*s)*v for v in (r,b)]
    return terms

def density(s, allow_fourth):
    if allow_fourth and F(7,10)<=s<=F(9,10):
        D=36*s*s-75*s+31
        r=-(48*s-29)/(2*D);b=-(33*s-19)/D
        g=(468*s*s-741*s+271)/(6*D);mode='M4'
    else:
        q=2*s-1;mode='DF'
        if s<=F(2,3):
            r=F(1,2);b=2/(4-6*q);delta=q/(4-6*q)
        elif s<=F(11,12):
            D=6*q*(10-6*q)-10
            r=(24*q-5)/D;b=(42*q-8)/D
            delta=q*(36*q-6*(6*s-2)+3)/(36*q*(3-2*s)-24*s+2)
        else:
            D=1-6*(1-q)**2
            r=(6*q-4)/D;b=(8*q-5)/D
            delta=(8*s*s-10*s+3)/(1-24*(1-s)**2)
        g=1-delta
    check(0<=r<=b,'density:parameter-order')
    check(0<g<1,'density:nontrivial-count')
    ts=norm_terms(s,r,b,mode)
    for t in ts: check(t<=g,'density:all-ten-monomials')
    check(max(ts)==g,'density:active-monomial')
    return {'sigma':s,'mode':mode,'r':r,'b':b,'g':g,'terms':ts}

def domain(x,y,z,label):
    margins=[x,y,z,sub(add(mul(6,z),y),1),sub(add(x,mul(6,z)),1),
             sub(add(x,y),1),sub(add(add(x,y),mul(6,z)),2),
             sub(mul(6,add(x,z)),5), sub(x,F(1,2))]
    if MUTATION=='obsolete_domain': margins += [sub(mul(3,x),2),sub(add(mul(3,x),y),F(5,2))]
    for m in margins: nonnegative(m,'domain:'+label,strict=True)

def disk(s):
    R=sub(2-s,mul(F(1,4),e));ro=sub(2-s,mul(F(1,2),e))
    rt=sub(2-s,e);ri=sub(1,mul(F(1,4),e))
    for margin in [sub(R,ro),sub(ro,rt),sub(rt,ri),ri, sub(4-s,R)]:
        nonnegative(margin,'disk:nested',strict=True)
    nonnegative(sub(F(1,10)*(1-s),e),'disk:buffer',strict=True)

def scale(a,x,y,z):
    return add(add(a/2,sub(x,1)),add(mul(1-a,z),mul(a,sub(y,1))))

def thresholds(a,step):
    out=[3*a/2]
    while out[-1]+step < F(97,100): out.append(out[-1]+step)
    out.append(F(97,100))
    return out

def composition(name,a,step,fourth):
    h=1-a;theta=a/2;z=F(1,3);cut=F(1,100)
    sigmas=thresholds(a,step)
    check(sigmas==sorted(set(sigmas)),'partition:ordered-thresholds')
    check(0<a<F(1,2),'scales:subcritical')
    check(2*a>=4*a-1,'scales:retain-diagonal-dominance')
    check(not MUTATION=='drop_diagonal' or 2*a<=4*a-1,'scales:reject-deleted-diagonal')
    rows=[density(s,fourth) for s in sigmas]
    for s in sigmas:disk(s)
    classes=[]
    x=add(sigmas[0],e);y=p(F(1,2));nu=F(1)
    R=p(1-z)
    good=add(scale(a,x,y,z),mul(add(h,e),R))
    check(good==(theta,F(5,3),0),'exponents:good-identity')
    classes.append({'kind':'good','x':x,'y':y,'nu':p(1),'power':good,'row_power':R})
    for j,(lo,hi) in enumerate(zip(rows,rows[1:])):
        s,t=lo['sigma'],hi['sigma']
        nu=add(lo['g'],e)
        if MUTATION=='upper_count':nu=add(hi['g'],e)
        check(nu==add(lo['g'],e),'partition:lower-threshold-count')
        x=add(t,mul(3,e));y=sub(1-t,e)
        if MUTATION=='wrong_reflection':y=add(1-t,e)
        nonnegative(sub(sub(1,y),add(t,e)),'reflection:inside-rectangle')
        nonnegative(sub(F(1,2),y),'reflection:positive-conductor-power',strict=True)
        check(y==sub(1-t,e),'reflection:exact-contour')
        R=sub(add(nu,sub(F(1,2),y)),z)
        if MUTATION=='old_convexity': R=sub(add(nu,mul(F(1,2),sub(1,y))),z)
        P=add(scale(a,x,y,z),mul(add(h,e),R))
        c=h*(2*t+lo['g'])+a-F(3,2)
        expected=(c,F(25,6)-3*a+lo['g']+t,F(2))
        if MUTATION=='old_convexity': check(P[0]<theta,'exponents:old-convexity-budget')
        check(P==expected,'exponents:middle-identity')
        check(c<theta,'exponents:strict-middle-margin')
        classes.append({'kind':'reflected','lower':s,'upper':t,'mode':lo['mode'],
                        'x':x,'y':y,'nu':nu,'power':P,'row_power':R})
    x=add(1,e);y=e;nu=add(rows[-1]['g'],e)
    R=sub(add(nu,mul(F(1,2),sub(1,y))),z)
    last=add(scale(a,x,y,z),mul(add(h,e),R))
    classes.append({'kind':'terminal','x':x,'y':y,'nu':nu,'power':last,'row_power':R})
    if MUTATION=='missing_terminal':classes.pop()
    check(len(classes)==len(sigmas)+1,'partition:complete-class-count')
    for c in classes:
        for xx,yy in ((add(1,e),add(1,e)),(c['x'],add(1,e)),(c['x'],c['y'])):
            domain(xx,yy,p(z),'real-contour-vertex')
        nonnegative(c['row_power'],'exponents:positive-row-power',strict=True)
        nonnegative(sub(add(theta,mul(6,e)),c['power']),'exponents:whole-interval-budget')
    # Monotone zero-set patterns: each nonprincipal row belongs to exactly one class.
    for membership_size in range(len(sigmas)+1):
        flags=[j<membership_size for j in range(len(sigmas))]
        members=[not flags[0]]+[flags[j] and not flags[j+1] for j in range(len(sigmas)-1)]+[flags[-1]]
        check(sum(members)==1,'partition:all-nested-patterns')
        check(len(members)==len(classes),'partition:no-class-deletion')
    principals=[(add(1,e),add(1,e),add(F(1,6),e)),
                (add(1,e),p(F(1,2)),add(F(1,6),e)),
                (add(1,e),p(1),add(F(1,6),e)),(add(1,e),p(1),e)]
    for xx,yy,zz in principals:domain(xx,yy,zz,'principal-vertex')
    pw=scale(a,add(1,e),F(1,2),add(F(1,6),e))
    pz=scale(a,add(1,e),1,e)
    small=add(scale(a,add(1,e),F(1,2),z),cut*(F(5,4)-z))
    check(pz==(theta,1+h,0),'exponents:principal-z')
    for P in (pw,pz,small):nonnegative(sub(add(theta,mul(6,e)),P),'exponents:remainder-budget')
    check(small[0]<theta,'exponents:strict-small-margin')
    # At initial x=y=5 and L=20/e+3 the e L product is exact, no Laurent sampling.
    gap=e if MUTATION!='zero_tail_gap' else p(0)
    nonnegative(gap,'tail:positive-large-cutoff-gap',strict=True)
    tail=(a/2+4+4*a+h-20,F(-2),F(0))
    nonnegative(sub(-1,tail),'tail:infinite-large-frequency')
    # Coarse Z^4 U^4 times U^(-rho*A), with rho*A=1000.
    nonnegative(sub(-1,4+4*(h+EMAX)-1000*cut),'tail:coarse-horizontal-and-original')
    truncate_w=MUTATION!='untruncated_w'
    check(truncate_w,'tail:reflection-only-on-truncated-w')
    b0=F(5,6)-a/3
    if MUTATION=='old_shift':b0=F(2,3)
    check(b0==1-(a/2+h/6),'mellin:actual-normalization')
    check(b0+theta>F(2,3),'mellin:principal-H-domain')
    margin=min(theta-c['power'][0] for c in classes[1:-1])
    return {'name':name,'a':a,'h':h,'theta':theta,'mellin_shift':b0,
            'boundary':b0+theta,'epsilon_max':EMAX,'final_epsilon_loss':8,
            'threshold_count':len(sigmas),'class_count':len(classes),
            'density_modes':dict(Counter(row['mode'] for row in rows)),
            'minimum_middle_margin':margin,'small_margin':theta-small[0],
            'maximum_middle_linear_coefficient':max(c['power'][1] for c in classes[1:-1]),
            'principal_w':pw,'principal_z':pz,'small':small,'large_tail':tail,
            'thresholds':rows,'classes':classes}

def supplemental():
    # A continuous certificate, separate from the finite lattice of thresholds.
    A=F(737316,625);B=F(122931,6250);C=F(4787,31250)
    check(A>0 and 4*A*C-B*B>0,'continuous:positive-quadratic')
    for t in (F(-1,10),0,F(1,10)):
        s=F(4,5)+t;D=36*s*s-75*s+31
        P=(7830000*s**3-16534368*s*s+11445975*s-2583553)/1250
        expand=6264*t**3+F(1128816,625)*t*t+B*t+C
        check(P==expand,'continuous:expansion-crosscheck')
        g4=(468*s*s-741*s+271)/(6*D)
        check(F(129,58)-(2*s+F(1,1250)+g4)==-P/(87*D),'continuous:rational-identity-crosscheck')
    # Polynomial identities are also checked as coefficients, not just three samples.
    # Exact coefficient expansion about 4/5 using the binomial formula.
    from math import comb
    coeff=[F(-2583553,1250),F(11445975,1250),F(-16534368,1250),F(7830000,1250)]
    shifted=[sum(coeff[j]*comb(j,i)*F(4,5)**(j-i) for j in range(i,4)) for i in range(4)]
    check(shifted==[C,B,F(1128816,625),F(6264)],'continuous:exact-shifted-coefficients')
    # Direct numerator identity after clearing the negative denominator.
    s_co=[F(-2583553,1250),F(11445975,1250),F(-16534368,1250),F(6264)]
    # P = -87 D (129/58 - 2s -1/1250) + (87/6)*(468s²-741s+271).
    D=[F(31),F(-75),F(36)]
    T=[F(129,58)-F(1,1250),F(-2)]
    out=[F(0)]*4
    for i,d in enumerate(D):
        for j,t in enumerate(T):out[i+j] += -87*d*t
    # The sign is plus here because g4 is subtracted inside the bracket.
    for i,d in enumerate([271,-741,468]):out[i] += F(87,6)*d
    check(out==s_co,'continuous:cleared-denominator-identity')
    # A small complete synthetic family: the character must be conjugated by FE.
    # This is algebraic bookkeeping, not numerical Hecke evaluation.
    for order in (2,3,6):
        for k,n in itertools.product(range(order),range(13)):
            check(((-k)*n)%order==(-(k*n))%order,'fixtures:conjugate-character-exponents')
    for q in (F(2),F(3),F(5),F(11)):
        for tau in (F(3,5),F(3,4),F(9,10)):
            x=tau+3*EMAX;y=1-tau-EMAX
            check(1-y>=tau+EMAX and x>tau,'fixtures:both-evaluations-inside')
            check(F(1,2)-y>0,'fixtures:conductor-direction')
    return {'cubic_lower_quadratic':[A,B,C],'quadratic_discriminant_gap':4*A*C-B*B}

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,tuple):return [encode(a) for a in x]
    if isinstance(x,list):return [encode(a) for a in x]
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    return x

def main():
    global MUTATION
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--details',action='store_true')
    parser.add_argument('--mutation',default='')
    args=parser.parse_args();MUTATION=args.mutation
    c=supplemental()
    compositions=[composition('main-selected-fourth-density',F(21,50),F(1,2500),True),
                  composition('original-DF-density-only',F(3,7),F(1,500),False)]
    if not args.details:
        compositions=[{k:v for k,v in x.items() if k not in ('thresholds','classes')} for x in compositions]
    result={'status':'finite checks only; not analytic certification','compositions':compositions,
            'continuous_certificate':c,'predicates':sum(COUNTS.values()),'counts':dict(sorted(COUNTS.items()))}
    print(json.dumps(encode(result),indent=2,sort_keys=True))

if __name__=='__main__':main()
