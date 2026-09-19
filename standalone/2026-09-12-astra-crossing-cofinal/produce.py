#!/usr/bin/env python3
"""XCC26 finite producer. No zero input or all-scale sign assertion."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

BITS=192; S=1<<BITS; G=1<<28
PARENT='2f0056d542603cb8118b9ac9da45b397162778e4'
SCOPE='finite native crossing panels and exact source identities; all-cofinal covariance bound and RH OPEN'

def req(x,why):
    if not x: raise ValueError(why)
def enc(x): return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def digest(x): return hashlib.sha256(enc(x)).hexdigest()
def add(x,y): return x[0]+y[0],x[1]+y[1]
def neg(x): return -x[1],-x[0]
def sub(x,y): return add(x,neg(y))
def rat(a,b=1):
    req(b>0,'positive denominator'); return a*S//b,-((-a*S)//b)
def mul(x,y):
    v=[a*b for a in x for b in y];return min(v)//S,-((-max(v))//S)
def scale(x,n): return (x[0]*n,x[1]*n) if n>=0 else (x[1]*n,x[0]*n)
def div(x,n):
    req(n>0,'positive divisor');return x[0]//n,-((-x[1])//n)
def square(x):
    lo=0 if x[0]<=0<=x[1] else min(x[0]**2,x[1]**2)
    return lo//S,-((-max(x[0]**2,x[1]**2))//S)
def fr(x): return rat(x.numerator,x.denominator)
def published(x): return [x[0]*G//S,-((-x[1]*G)//S)]
def pq(x): return [x.numerator,x.denominator]

@lru_cache(None)
def logn(n):
    req(n>=1,'positive log');
    if n==1:return (0,0)
    # Factor first: only the bounded source primes require transcendental series.
    for p in range(2, math.isqrt(n)+2):
        if p*p>n:break
        if n%p==0:return add(logn(p),logn(n//p))
    e=n.bit_length()-1; b=1<<e
    q=rat(n-b,n+b); q2=mul(q,q); power=q; acc=(0,0); terms=80
    for j in range(terms):
        acc=add(acc,div(power,2*j+1));power=mul(power,q2)
    out=scale(acc,2)
    # q <= 1/3: an explicit bound for the complete positive omitted tail.
    rem=rat(3,(2*terms+1)*3**(2*terms+1))[1]
    out=(out[0],out[1]+rem)
    if n==2:
        # Above range reduction has q=0; evaluate log 2 directly.
        q=rat(1,3);q2=mul(q,q);power=q;acc=(0,0)
        for j in range(terms):acc=add(acc,div(power,2*j+1));power=mul(power,q2)
        return (2*acc[0],2*acc[1]+rem)
    return add(out,scale(logn(2),e))

def sieve(N):
    mu=[1]*(N+1);mu[0]=0;marked=bytearray(N+1)
    for p in range(2,N+1):
        if not marked[p]:
            for n in range(p,N+1,p):mu[n]=-mu[n];marked[n]=1
            for n in range(p*p,N+1,p*p):mu[n]=0
    return mu

def liouville(n):
    s=1;p=2
    while p*p<=n:
        while n%p==0:n//=p;s=-s
        p+=1
    return -s if n>1 else s

def crossing_data(mu,N):
    m=F(0);rows=[]
    for n in range(1,N+1):
        old=m;m+=F(mu[n],n)
        if n>=2 and mu[n] and old*m<=0:
            req(abs(m)<=F(1,n),'crossing amplitude')
            rows.append([n,pq(old),pq(m)])
    return rows

def completion(a,Y):
    m=sum((F(a[n],n) for n in range(1,Y+1)),F(0))
    before=m-F(a[Y],Y)
    req(a[Y]!=0 and before*m<=0,'actual crossing guard')
    c={n:F(a[n]) for n in range(1,Y+1) if a[n]}
    if m:c[2*Y]=-2*Y*m
    req(sum((v/n for n,v in c.items()),F(0))==0,'safe point')
    req(max(abs(v) for v in c.values())<=2,'coefficient cap')
    req(all(liouville(n)*v>=0 for n,v in c.items()),'sign coherence')
    return c,m

def source_identity(c,Y,m):
    # Direct physical cells, including the infinite terminal constant tail.
    ks=sorted(c);total=F(0);J=F(0)
    for i,n in enumerate(ks):
        total+=c[n]
        nextn=ks[i+1] if i+1<len(ks) else None
        J+=total*total*(F(1,n)-(F(1,nextn) if nextn else 0))
    x=F(0);FY=F(0)
    for k in range(1,Y+1):x+=c.get(k,F(0))/k;FY+=x*x
    T=(Y-1)*m*m
    req(J==FY+T,'complete source norm')
    return FY,T,J

def coalesce(c):
    from math import lcm
    q=1
    for v in c.values():q=lcm(q,v.denominator)
    ci={n:int(v*q) for n,v in c.items()};z={}
    for n,a in ci.items():
        for m,b in ci.items():z[n*m]=z.get(n*m,0)+a*b
    z={n:a for n,a in z.items() if a}
    req(all(liouville(n)*a>=0 for n,a in z.items()),'convolution sign')
    req(sum((F(a,n) for n,a in z.items()),F(0))==0,'zero product moment')
    # log moment is authenticated coefficientwise, not by rounded logs.
    moments={}
    for n,a in z.items():
        d=n;p=2
        while p*p<=d:
            e=0
            while d%p==0:d//=p;e+=1
            if e:moments[p]=moments.get(p,F(0))+F(e*a,n)
            p+=1
        if d>1:moments[d]=moments.get(d,F(0))+F(a,n)
    req(all(v==0 for v in moments.values()),'prime log moment')
    return q,ci,z

def panel(a,Y,native,mu):
    c,m=completion(a,Y);FY,T,J=source_identity(c,Y,m);q,ci,z=coalesce(c)
    B=(Y+1)**2-1;q2=q*q
    prod=[0]*(B+2)
    for d,w in z.items():
        for k in range(d,B+2,d):prod[k]+=w
    H=[(0,0)]*(B+1);SH=[(0,0)]*(B+1);SH2=[(0,0)]*(B+1)
    V=[];Q=(0,0);QN=(0,0);out=(0,0);EN=(0,0);old=(0,0);tail=(0,0)
    # Independent of the diagonal: coefficientwise divisor/Newton output.
    for k in range(1,B+2):
        v=2*q*ci.get(k,0)-prod[k];V.append(v)
        if native and k<=B:req(v==q2*mu[k],'every reproduced coefficient')
        if k>B:continue
        H[k]=add(H[k-1],rat(1,k));SH[k]=add(SH[k-1],H[k]);SH2[k]=add(SH2[k-1],square(H[k]))
        Q=add(Q,rat(prod[k],q2*k));out=add(out,rat(v,q2*k))
        if k<=Y:old=add(old,square(out))
        else:QN=add(QN,square(Q));EN=add(EN,square(out))
    if native:
        b=Y+1;e=-sum(ci.get(d,0) for d in range(1,b+1) if b%d==0)
        req(q2*mu[b*b]-V[-1]==e*e,'excluded boundary error')
    D=(0,0);groups=0
    for d,w in sorted(z.items()):
        energy=(0,0);start=Y+1;ld=logn(d)
        while start<=B:
            j=start//d;end=min(B,(j+1)*d-1);n=end-start+1
            A=add(H[j],ld);s1=sub(SH[end],SH[start-1]);s2=sub(SH2[end],SH2[start-1])
            term=add(sub(scale(square(A),n),scale(mul(A,s1),2)),s2)
            term=(max(0,term[0]),term[1]);req(term[1]>=0,'nonnegative block energy')
            energy=add(energy,term);groups+=1;start=end+1
        D=add(D,mul(rat(w*w,q2*q2*d*d),energy))
    C=sub(QN,D);FB=add(old,EN)
    # Written inequality tested without assuming sign of C.
    rhs=add(add(fr(FY+8*T),scale(D,2)),scale(C,2))
    req(FB[0]<=rhs[1],'finite update enclosure')
    if native:req(C[1]<0,'finite native negative sign')
    else:req(100*C[0]>177*S and 100*C[1]<178*S,'non-native positive control')
    crows=[[n,pq(v)] for n,v in sorted(c.items())]
    zrows=[[n,pq(F(w,q2))] for n,w in sorted(z.items())]
    return {'Y':Y,'native':native,'B':B,'source_rows_sha256':digest(crows),'late_coefficient':pq(c.get(2*Y,F(0))),'source_J':published(fr(J)),'F_Y':published(fr(FY)),'tail_energy':pq(T),
            'products':len(z),'product_rows_sha256':digest(zrows),'all_output_sha256':digest([pq(F(v,q2)) for v in V]),
            'coefficient_count':B,'diagonal_groups':groups,'D':published(D),'Q_squared':published(QN),'covariance':published(C),'F_B':published(FB)}

def fake():
    Y=19;a=[F(0)]*20;a[1]=F(1);a[19]=F(-1);r=F(1)-F(1,38)
    for n in range(18,1,-1):
        if liouville(n)==-1:
            a[n]=-min(F(1),n*r);r+=a[n]/n
            if r==0:break
    req(r==0 and sum((a[k]/k for k in range(1,20)),F(0))==-F(1,38),'fake construction')
    return a

def pair_control(mu):
    Y=5;c,m=completion(mu,Y);q,ci,z=coalesce(c);H=[(0,0)]*36
    for k in range(1,36):H[k]=add(H[k-1],rat(1,k))
    total=(0,0)
    for k in range(6,36):
        a=div(add(sub(H[k//2],H[k]),logn(2)),2)
        b=div(add(sub(H[k//5],H[k]),logn(5)),5)
        total=add(total,mul(a,b))
    value=mul(rat(2*z[2]*z[5],q**4),total)
    req(value[0]>S//100,'native positive pair')
    return {'Y':5,'pair':[2,5],'ordered_pair':published(value),'strict_lower':[1,100]}

def build():
    mu=sieve(432**2);cross=crossing_data(mu,1024)
    Ys=[r[0] for r in cross if r[0]<=127]+[173,210,431]
    rows=[panel(mu,Y,True,mu) for Y in Ys]
    f=panel(fake(),19,False,mu)
    body={'schema':'XCC26-1','parent':PARENT,'scope':SCOPE,'scale':G,'crossing_cutoff':1024,'crossing_indices':[r[0] for r in cross],'crossing_rows_sha256':digest(cross),
          'panels':rows,'fake_panel':f,'positive_native_pair':pair_control(mu),
          'native_sign_bound_unbounded':False,'RH_proved':False,
          'counts':{'crossings':len(cross),'native_panels':len(rows),'product_time_cells':sum(r['products']*(r['B']-r['Y']) for r in rows),
                    'diagonal_groups':sum(r['diagonal_groups'] for r in rows),'reproduced_coefficients':sum(r['B'] for r in rows)}}
    return {'body':body,'sha256':digest(body)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--check',type=Path);a=p.parse_args();r=build()
    if a.check:req(enc(json.loads(a.check.read_text()))==enc(r),'canonical mismatch')
    if a.output:a.output.write_bytes(enc(r)+b'\n')
    print('PASS',r['sha256']);print(r['body']['counts']);print('last',r['body']['panels'][-1]['covariance']);print('fake',r['body']['fake_panel']['covariance'])
if __name__=='__main__':main()
