#!/usr/bin/env python3
"""Exact finite checks of compensated Euler phases, not an asymptotic certificate.
Primitive Eisenstein enumeration is adapted from PR #942 census.py at
377f548cab8759399aca80ed3188c495667d562a (MIT); this is NOT a byte-exact copy.
Requires NumPy for bounded integer row-array acceleration.
"""
from fractions import Fraction as F
from collections import Counter
from functools import lru_cache
from math import isqrt, lcm
import argparse
import json
from pathlib import Path

CHECKS = 0
ROOTS = ((1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(0,0))

def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise ValueError(message)

def trim(a):
    a = list(a)
    while len(a)>1 and not a[-1]: a.pop()
    return tuple(a)

def padd(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def pscale(a,c): return trim([v*c for v in a])

def pmul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b): c[i+j]+=v*w
    return trim(c)

def pmoment(m):
    c=[F(0)]*(m+1); c[1]+=F(1,m); c[m]-=F(1,m)
    return trim(c)

def exp_series(a,n):
    b=[(F(1),)]
    for j in range(1,n+1):
        v=(F(0),)
        for m in range(1,j+1):
            v=padd(v,pscale(pmul(a[m],b[j-m]),F(m,j)))
        b.append(v)
    return b

@lru_cache(None)
def local(n,r=2):
    logk=[(F(0),)]*(n+1)
    for m in range(r+1,n+1): logk[m]=pmoment(m)
    h=exp_series(logk,n)
    g=exp_series([pscale(a,-1) for a in logk],n)
    f=[h[0]]+[padd(h[j],pscale(h[j-1],-1)) for j in range(1,n+1)]
    return tuple(f),tuple(h),tuple(g)

def direct_local(n,r):
    # Independent product assembly: (1-z*x)(1-x)^(1-z) exp(counterterms).
    b=[(F(1),)]
    for j in range(1,n+1): b.append(pscale(pmul(b[-1],(F(j-2),F(1))),F(1,j)))
    c=[b[0]]+[padd(b[j],pscale(pmul((F(0),F(1)),b[j-1]),-1)) for j in range(1,n+1)]
    loge=[(F(0),)]*(n+1)
    for m in range(2,min(r,n)+1): loge[m]=pscale(pmoment(m),-1)
    e=exp_series(loge,n)
    out=[]
    for j in range(n+1):
        v=(F(0),)
        for m in range(j+1): v=padd(v,pmul(c[m],e[j-m]))
        out.append(v)
    return out

def emul(x,y):
    a,b=x; c,d=y
    return (a*c-b*d,a*d+b*c-b*d)

def eadd(x,y): return (x[0]+y[0],x[1]+y[1])
def econj(x): return (x[0]-x[1],-x[1])
def enorm(x): return x[0]*x[0]-x[0]*x[1]+x[1]*x[1]
def peval(a,z):
    out=(F(0),F(0))
    for c in reversed(a): out=eadd(emul(out,z),(c,F(0)))
    return out

def field_pow(x,e,p):
    y=(1,0)
    while e:
        if e&1: y=tuple(v%p for v in emul(y,x))
        x=tuple(v%p for v in emul(x,x)); e//=2
    return y

def primes_through(n):
    flags=bytearray(b'\1')*(n+1); flags[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if flags[p]: flags[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
    return [p for p in range(5,n+1) if flags[p]]

@lru_cache(None)
def prime_ideals(n):
    out=[]
    for p in primes_through(n):
        if p%3==1:
            roots=[r for r in range(p) if (r*r+r+1)%p==0]
            check(len(roots)==2,'two split ideals')
            for r in roots:
                sixth={pow(1+r,e,p):e for e in range(6)}
                check(len(sixth)==6,'split sixth-root order')
                table=[6 if x==0 else sixth[pow(x,(p-1)//6,p)] for x in range(p)]
                out.append((p,p,r,table))
        elif p*p<=n:
            sixth={(a%p,b%p):e for e,(a,b) in enumerate(ROOTS[:6])}
            table=[6 if a==b==0 else sixth[field_pow((a,b),(p*p-1)//6,p)]
                   for a in range(p) for b in range(p)]
            out.append((p*p,p,None,table))
    return sorted(out,key=lambda x:(x[0],-1 if x[2] is None else x[2]))

def ideals_through(n,primes):
    out=[(1,())]
    for j,(q,_,_,_) in enumerate(primes):
        extra=[]
        for d,fac in out:
            v,e=q,1
            while d*v<=n:
                extra.append((d*v,fac+((j,e),))); v*=q; e+=1
        out.extend(extra)
    out=sorted(out)
    # Independent norm-count assembly from zeta(s)L(s,chi_-3), then delete 3,4.
    a=[0]*(n+1)
    for d in range(1,n+1):
        c=0 if d%3==0 else (1 if d%3==1 else -1)
        for t in range(d,n+1,d): a[t]+=c
    counts=Counter(d for d,_ in out)
    for d in range(1,n+1):
        expected=a[d]-(a[d//3] if d%3==0 else 0)-(a[d//4] if d%4==0 else 0)+(a[d//12] if d%12==0 else 0)
        check(counts[d]==expected,'complete good ideal norm count')
    return out

def rows_through(h):
    b=isqrt(4*h//3)+1
    return [(a,c) for a in range(-b,b+1) for c in range(-b,b+1)
            if 0<enorm((a,c))<=h]

def ceil_height(d):
    lo,hi=0,2*d
    while hi**20<d**21: hi*=2
    while hi-lo>1:
        m=(lo+hi)//2
        if m**20>=d**21: hi=m
        else: lo=m
    return hi

def fac_poly(fac,r=2,which=0):
    a=(F(1),)
    for _,e in fac: a=pmul(a,local(e,r)[which][e])
    return a

def array_poly_multiply(a,b):
    import numpy as np
    ma=max(1,int(np.max(np.abs(a)))); mb=max(1,int(np.max(np.abs(b))))
    check(3*min(a.shape[0],b.shape[0])*ma*mb<2**62,'array product int64 guard')
    out=np.zeros((a.shape[0]+b.shape[0]-1,a.shape[1],2),dtype=np.int64)
    for i in range(a.shape[0]):
        for j in range(b.shape[0]):
            x,y=a[i,:,0],a[i,:,1]; s,t=b[j,:,0],b[j,:,1]
            out[i+j,:,0]+=x*s-y*t
            out[i+j,:,1]+=x*t+y*s-y*t
    return out

def rational(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

def circular_check(coeff,k):
    # Direct Laurent multiplication, independently of analytic-power Parseval.
    deg=len(coeff)-1; size=2*k*deg+1
    ring=[(F(0),F(0))]*size
    for i,x in enumerate(coeff):
        for j,y in enumerate(coeff):
            ring[(i-j)%size]=eadd(ring[(i-j)%size],emul(x,econj(y)))
    v=[(F(0),F(0))]*size; v[0]=(F(1),F(0))
    for _ in range(k):
        w=[(F(0),F(0))]*size
        for i,x in enumerate(v):
            if x==(0,0): continue
            for j,y in enumerate(ring):
                if y!=(0,0): w[(i+j)%size]=eadd(w[(i+j)%size],emul(x,y))
        v=w
    return v[0]

def census(d,h):
    import numpy as np
    primes=prime_ideals(d); ideals=ideals_through(d,primes); rows=rows_through(h)
    columns=[(n,fac,fac_poly(fac)) for n,fac in ideals if d<2*n<=2*d]
    active=[v for v in columns if any(v[2])]
    denominator=1
    for _,_,poly in active:
        for c in poly: denominator=lcm(denominator,c.denominator)
    deg=max(len(poly)-1 for _,_,poly in active)
    budget=sum(sum(abs(int(c*denominator)) for c in poly) for _,_,poly in active)
    check(3*budget<2**62,'row coefficient assembly int64 guard')
    rr=np.asarray(rows,dtype=np.int64); vals=np.asarray(ROOTS,dtype=np.int64)
    check((d+2)*max(1,int(np.max(np.abs(rr))))<2**62,'residue int64 guard')
    chars=[]
    for q,p,r,table in primes:
        idx=(rr[:,0]+r*rr[:,1])%p if r is not None else (rr[:,0]%p)*p+rr[:,1]%p
        chars.append(np.asarray(table,dtype=np.int8)[idx])
    coeff=np.zeros((deg+1,len(rows),2),dtype=np.int64)
    native=np.zeros((len(rows),2),dtype=np.int64)
    for _,fac,poly in active:
        phase=np.zeros(len(rows),dtype=np.int64); zero=np.zeros(len(rows),dtype=bool)
        for j,e in fac:
            phase+=(chars[j].astype(np.int64)%6)*e; zero|=(chars[j]==6)
        phase%=6; phase[zero]=6; roots=vals[phase]
        for j,c in enumerate(poly): coeff[j]+=int(c*denominator)*roots
        if all(e==1 for _,e in fac): native+=(-1)**len(fac)*roots
    check(bool(np.array_equal(coeff[0],denominator*native)),'native constant mode on EVERY row')
    energies=[enorm((int(a),int(b))) for a,b in native]
    powers=np.zeros((1,len(rows),2),dtype=np.int64); powers[0,:,0]=1
    moments={}
    for k in range(1,5):
        powers=array_poly_multiply(powers,coeff)
        total=sum(enorm((int(a),int(b))) for a,b in powers.reshape(-1,2))
        mean=F(total,denominator**(2*k)); m=sum(e**k for e in energies)
        check(mean>=m,'positive averaged excess')
        moments[str(2*k)]={'native':str(m),'completed_circle':rational(mean),'excess':rational(mean-m)}
        if d in (256,512):
            for row in ((1,0),(-2,1),(3,1)):
                idx=rows.index(row)
                cs=[(F(int(a),denominator),F(int(b),denominator)) for a,b in coeff[:,idx,:]]
                direct=circular_check(cs,k)
                parsed=F(sum(enorm((int(a),int(b))) for a,b in powers[:,idx,:]),denominator**(2*k))
                check(direct==(parsed,0),'independent circular Laurent check')
    known={256:3021246,512:24073938,1024:181593786,8192:114923460372}
    if d in known and h==ceil_height(d): check(int(moments['4']['native'])==known[d],'published complete native replay')
    return {'D':d,'H':h,'rows':len(rows),'all_good_ideals_through_D':len(ideals),
            'all_good_columns_in_window':len(columns),'native_squarefree_columns':sum(all(e==1 for _,e in fac) for _,fac,_ in columns),
            'completed_nonzero_columns':len(active),'global_phase_degree':deg,'coefficient_denominator':denominator,'moments':moments}

def algebra_checks():
    for r in range(1,5):
        f,h,g=local(12,r); direct=direct_local(12,r)
        for n in range(13):
            check(f[n]==direct[n],'two complete local constructions')
            product=(F(0),)
            for j in range(n+1): product=padd(product,pmul(h[j],g[n-j]))
            check(product==((F(1),) if n==0 else (F(0),)),'signed inverse local kernel')
            if 1<=n<=r: check(f[n]==((F(-1),) if n==1 else (F(0),)),'retained low prime powers')
            check(f[n][0]==(1 if n==0 else -1 if n==1 else 0),'unbiased constant local coefficient')
            for z in ((0,0),(1,0),(-1,0),(0,1),(F(1,2),0)):
                if z in ((0,0),(1,0)):
                    check(peval(f[n],z)==((1 if n==0 else -1 if n==1 else 0),0),'both deterministic endpoints')
    f,h,g=local(6,2)
    check(f[3]==(0,F(1,3),0,F(-1,3)),'first compensated cubic coefficient')
    check(peval(h[4],(F(1,2),0))!=peval(f[4],(F(1,2),0)),'negative control: extra coprimality destroys p^4 convolution')
    # Without the square counterterm the p^2 coefficient is nonzero.
    check(local(2,1)[0][2]!=(F(0),),'negative control: omit quadratic counterterm')
    check(F(1,7)<F(4,25) and F(16,6)<F(25,9) and F(50,27)<2,'rational bounds giving log C < 2')
    # Exact nonunit mask, including sixth charge zero.
    primes=prime_ideals(32)
    p=next(v for v in primes if v[0]==7 and v[2]==2)
    check(p[3][(-2+p[2])%7]==6,'nonunit has literal zero')
    check(ROOTS[6]!=(1,0),'negative control: neutral exponent is not an unmasked unit')
    # Uniform coefficientwise bounds for both directions, finite-degree diagnostic.
    logmajor=[(F(0),)]*13
    for n in range(3,13): logmajor[n]=(F(2,n),)
    major=exp_series(logmajor,12)
    for n in range(13):
        for z in ((-1,0),(0,1),(1,1),(F(1,2),0)):
            for kernel in (local(12,2)[1],local(12,2)[2]):
                check(enorm(peval(kernel[n],z))<=major[n][0]**2,'universal absolute majorant')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sizes',type=int,nargs='+',default=[256,512,1024,2048,4096,8192])
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    check(all(4<=d<=8192 for d in args.sizes),'validated sizes are 4 through 8192')
    algebra_checks()
    data={'status':'exact finite diagnostics; not an infinite moment bound',
          'weight':'hard columns D/2<Nn<=D; sharp nonzero rows Nu<=ceil(D^(21/20))',
          'phase':'one common continuous unit-circle parameter; exact Parseval, not phase sampling',
          'cases':[census(d,ceil_height(d)) for d in args.sizes]}
    data['explicit_checks_including_setup']=CHECKS
    data['negative_controls']=3
    data['review']='same-author two algebra assemblies, shared primitive arithmetic; no independent referee'
    text=json.dumps(data,sort_keys=True,indent=2)+'\n'
    if args.output: args.output.write_text(text,encoding='utf-8')
    else: print(text,end='')

if __name__=='__main__': main()
