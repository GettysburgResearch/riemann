#!/usr/bin/env python3
"""Exact finite bookkeeping, not a verifier of the imported analytic inputs."""
import argparse
from fractions import Fraction as F
import json

UPPERS = '''2/3 14527/20000 2363/3125 38727/50000 15743/20000
39821/50000 80359/100000 16187/20000 20353/25000 81817/100000
82169/100000 1031/1250 82759/100000 83013/100000 83247/100000
41733/50000 83673/100000 83871/100000 42031/50000 10531/12500
84431/100000 84613/100000 16959/20000 84979/100000 85167/100000
85361/100000 85563/100000 5361/6250 86003/100000 86247/100000
86599/100000 87223/100000 88359/100000 9053/10000 19/20 1'''.split()
E0 = F(1, 10**7)
COUNTS = {}
MUTATE = None

def need(ok, gate):
    COUNTS[gate] = COUNTS.get(gate, 0) + 1
    if not ok:
        raise ValueError('REJECT: ' + gate)

def bernstein(fun, gate, strict=False):
    f0, fm, f1 = fun(F(0)), fun(E0/2), fun(E0)
    b = [f0, 2*fm-(f0+f1)/2, f1]
    need(all(x >= 0 for x in b), gate)
    if strict:
        # Positive at every e in (0,E0], allowing equality at zero only.
        need(b[2] > 0 and (b[0] > 0 or b[1] > 0), gate)
    return b

def sieve():
    return [(F(1),F(0)),(F(0),F(1)),(F(5,6),F(1,3)),(F(1,3),F(5,6))]

def rest(s,a,b):
    return [(2-2*s)*b, 1+(1-2*s)*a,
            F(1,3)+(F(11,6)-2*s)*a,
            F(1,3)+(F(11,6)-2*s)*b,
            F(5,6)+(F(4,3)-2*s)*a,
            F(5,6)+(F(4,3)-2*s)*b]

def density(s):
    if s == F(19,20):
        return F(70,47), F(110,47), F(11,47)
    den = 72*s*s-132*s+53
    return (-(48*s-29)/(2*den), -(42*s-25)/den,
            (216*s*s-342*s+127)/(2*den))

def records():
    us = list(map(F,UPPERS))
    rr = [dict(lower=None,upper=us[0],nu=F(1),method='M2')]
    for lo,hi in zip(us,us[1:]):
        a,b,n = density(lo)
        need(0 <= a <= b and 0 <= n <= 1, 'density_parameters')
        for c,d in sieve():
            value=F(1,2)+(c+d*a)/2+(F(1,2)-lo)*b
            need(value <= n, 'density_first_terms')
        for value in rest(lo,a,b):
            need(value <= n, 'density_remaining_terms')
        if MUTATE == 'upper_count':
            n=density(hi)[2] if hi < 1 else F(0)
            need(F(1,2)+max(c+d*a for c,d in sieve())/2+(F(1,2)-lo)*b <= n,
                 'lower_threshold_count')
        rr.append(dict(lower=lo,upper=hi,nu=n,A=a,B=b,
                       method='M4L' if hi < F(86599,100000) else 'CV'))
    return rr

def xyz(row,e):
    x=row['upper']+e
    if row['method']=='M2': y=F(1,2)
    elif row['method']=='M4L': y=F(1,2) if MUTATE=='central' else F(5,12)
    else: y=1-row['upper']+e
    return x,y,F(1,3)

def physical(x,y,z,e):
    a=F(4,9)+e; h=1-a
    return a/2+x-1+h*z+a*(y-1)

def domain(x,y,z):
    return [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
            6*x+6*z-5,x-F(1,2),3*x-2,3*x+y-F(5,2)]

def class_power(row,e):
    x,y,z=xyz(row,e); nu=row['nu']; h=F(5,9)-e
    if row['method']=='M2': mu=(nu+1)/2
    elif row['method']=='M4L': mu=3*nu/4+(F(7,24) if MUTATE=='central' else F(1,3))
    else: mu=nu+(1-y)/2
    return physical(x,y,z,e)+(h+e)*(mu-z)

def run():
    # All vertices of the original and dual AFE exponent triangles.
    for c,d in sieve():
        for v in [F(0),F(1)]:
            need(c+(d-F(1,6))*v <= 1, 'original_AFE_vertices')
        for q,v in [(F(0),F(0)),(F(1),F(0)),(F(1),F(1))]:
            dual=c+(d+F(1,6))*v-(F(0) if MUTATE=='dual' else q/3)
            need(dual <= 1, 'dual_AFE_vertices')
    # Exact sixth-root phase and nonunit-mask identities, including exponent 7.
    for phase in [None,0,1,2,3,4,5]:
        for exponent in range(20):
            def ch(v):
                return None if phase is None and v else ((phase or 0)*v)%6
            c,d=exponent%6,exponent//6
            left=ch(exponent)
            right=None if phase is None and d and MUTATE!='mask' else ch(c)
            if MUTATE=='coprime' and c and d: right=None
            need(left==right, 'sixth_power_masks_and_shared_primes')
    rows=records()
    need(len(rows)==36, 'complete_class_count')
    # Each possible interval for a zero's real part has exactly one class.
    classes=list(range(len(rows)))
    if MUTATE=='last_class': classes.remove(len(rows)-1)
    for z in [F(0),F(1),F(2)]+list(map(F,UPPERS[:-1]))+[(F(a)+F(b))/2 for a,b in zip(UPPERS,UPPERS[1:])]:
        hits=sum((j==0 and z<rows[0]['upper']) or
                 (j>0 and rows[j]['lower']<=z and (j==len(rows)-1 or z<rows[j]['upper'])) for j in classes)
        need(hits==1, 'disjoint_exhaustive_classes')
    mins=[]
    for row in rows:
        bernstein(lambda e:class_power(row,e)-physical(*xyz(row,e),e), 'top_dyad_positive', strict=True)
        if row['upper'] < 1:
            ss=row['upper']
            for fun in [lambda e:e/4, lambda e:e/2,
                        lambda e,ss=ss:1-ss-3*e/4,
                        lambda e,ss=ss:1-e/4,
                        lambda e:e/4]:
                bernstein(fun, 'reciprocal_disks', strict=True)
        bernstein(lambda e:(F(4,9)+e)/2+2*e-class_power(row,e), 'class_power_interval')
        if row['lower'] is not None:
            mins.append(F(2,9)-class_power(row,F(0)))
        for vertex in range(3):
            for j in range(11):
                def check(e,vertex=vertex,j=j):
                    x,y,z=xyz(row,e)
                    if vertex==0: x,y=1+e,1+e
                    elif vertex==1: y=1+e
                    return domain(x,y,z)[j]
                bernstein(check, 'all_contour_domain_vertices', strict=True)
    need(min(mins)>F(1,4000), 'middle_strict_margin')
    theta=lambda e:(F(4,9)+e)/2
    for corner in [(F(1,2),'w'),(F(1),'z')]:
        def power(e,corner=corner):
            y,label=corner
            z=F(1,6)+e if label=='w' else e
            return physical(1+e,y,z,e)
        bernstein(lambda e:theta(e)+2*e-power(e), 'principal_remainders')
        for j in range(11):
            bernstein(lambda e,j=j,corner=corner:domain(1+e,corner[0],F(1,6)+e if corner[1]=='w' else e)[j],
                      'principal_domain',strict=True)
    bernstein(lambda e:theta(e)+2*e-(physical(1+e,F(1,2),F(1,3),e)+F(1,100)*F(2,3)),
              'small_frequencies')
    def large_power(e):
        a=F(4,9)+e; h=1-a
        if MUTATE=='large_gap': return 4+F(5,2)*a
        # Expanded expression, valid also at zero by polynomial continuation.
        return 4+F(5,2)*a-10-e
    bernstein(lambda e:-1-large_power(e), 'large_frequencies')
    for e in [F(0),E0/2,E0]:
        a=F(4,9)+e
        need(2*a<1 and a>0, 'short_support_not_extrapolated')
        b=F(41,60) if MUTATE=='shift' else F(5,6)-a/3
        need(b==F(37,54)-e/3, 'true_principal_Mellin_shift')
        need(b+theta(e)+4*e==F(49,54)+F(25,6)*e, 'zero_free_sum')
        need((3*a-1)/24 == a/12-(1-a)/24, 'offcentral_gain')
    need(F(109,120)-F(49,54)==F(1,1080), 'stronger_than_966')
    need(F(10,11)-F(49,54)==F(1,594), 'stronger_than_968')
    return dict(status='PASS_FINITE_BOOKKEEPING_ONLY',classes=len(rows),
                methods={m:sum(r['method']==m for r in rows) for m in ['M2','M4L','CV']},
                epsilon_max=str(E0),minimum_middle_base_margin=str(min(mins)),
                proposed_boundary='49/54',
                counts=COUNTS,total_predicates=sum(COUNTS.values()),
                analytic_inputs_verified=False,independent_review=False,
                rows=[{k:(str(v) if isinstance(v,F) else v) for k,v in r.items()} for r in rows])

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--mutate',choices=['central','dual','mask','coprime','upper_count','last_class','shift','large_gap'])
    args=ap.parse_args(); MUTATE=args.mutate
    print(json.dumps(run(),sort_keys=True,indent=2))
