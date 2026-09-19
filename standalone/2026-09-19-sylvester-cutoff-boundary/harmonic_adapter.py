#!/usr/bin/env python3
"""Exact boundary -> PCR26/RCB26 harmonic-source adapter and bounded covariance panels."""
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import accumulate
from math import lcm
from pathlib import Path

S = 1 << 100


def need(ok, msg):
    if not ok: raise ValueError(msg)


def factors(n):
    out=[];p=2
    while p*p<=n:
        a=0
        while n%p==0:n//=p;a+=1
        if a:out.append((p,a))
        p+=1
    if n>1:out.append((n,1))
    return out


def mu(n):
    fs=factors(n)
    return 0 if any(a>1 for _,a in fs) else (-1)**len(fs)


def box_fraction(x):
    q,r=divmod(x.numerator*S,x.denominator)
    return (q,q+bool(r))


def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[1],x[1]-y[0])
def scale(x,a):
    if a<0:return scale((-x[1],-x[0]),-a)
    num,den=a.numerator,a.denominator
    return (x[0]*num//den,-((-x[1]*num)//den))
def square(x):
    a,b=x
    low=0 if a<=0<=b else min(a*a,b*b)
    return (low//S,(max(a*a,b*b)+S-1)//S)


def log_rational(a,b):
    """log(a/b) for 1<=a/b<=2, using positive atanh series and exact remainder."""
    need(b<=a<=2*b,'log range')
    u=F(a-b,a+b);power=u;ans=(0,0)
    for j in range(70):
        ans=add(ans,box_fraction(2*power/F(2*j+1)))
        power*=u*u
    remainder=2*power/(141*(1-u*u))
    return ans[0],ans[1]+box_fraction(remainder)[1]


def log_integer(n):
    e=n.bit_length()-1
    return add(scale(log_rational(2,1),F(e)),log_rational(n,1<<e))


def completion(y):
    c=[F(0)]+[F(mu(n)) for n in range(1,y+1)]
    residual=sum((c[n]/n for n in range(1,len(c))),F(0))
    while residual:
        n=len(c)
        coeff=-min(F(3),n*residual) if residual>0 else min(F(3),-n*residual)
        c.append(coeff);residual+=coeff/n
        need(len(c)<=2*y+2,'completion failed to terminate in declared support')
    need(all(abs(x)<=3 for x in c),'coefficient cap')
    need(sum((c[n]/n for n in range(1,len(c))),F(0))==0,'reciprocal moment')
    return c


def run(y,panels):
    b,B=y+1,(y+1)**2-1
    c=completion(y);L=len(c)-1
    den=lcm(*(x.denominator for x in c));a=[int(x*den) for x in c]
    z=[0]*(L*L+1)
    for r in range(1,L+1):
        for s in range(1,L+1):z[r*s]+=a[r]*a[s]
    # Full z is retained, including d>B, since centered kernels need those terms.
    conv=[0]*(B+1)
    for d in range(1,min(B,L*L)+1):
        if z[d]:
            for k in range(d,B+1,d):conv[k]+=z[d]
    native=[0]+[mu(n) for n in range(1,B+1)]
    for n in range(1,B+1):
        ac=a[n] if n<=L else 0
        need(conv[n]==2*ac*den-native[n]*den*den,'full completed Newton adapter')
    # Construct native m(k) from g*e, not by summing a future Mobius oracle.
    e=[0]*(B+1);e[1]=1
    for d in range(1,y+1):
        for n in range(d,B+1,d):e[n]-=native[d]
    bd=[0]*(B+1)
    for r in range(1,y+1):
        for n in range(b,B//r+1):bd[r*n]+=native[r]*e[n]
    need(bd[b:]==native[b:],'boundary adapter coefficients')
    out=dict(Y=y,L=L,full_product_support=L*L,adapter_coefficients=B,
             nonzero_products_above_B=sum(bool(v) for v in z[B+1:]),
             coefficient_denominator=str(den),reciprocal_moment='0')
    if not panels:return out
    m=list(accumulate([F(0)]+[F(native[n],n) for n in range(1,B+1)]))
    mc=list(accumulate([F(0)]+[(c[n]/n if n<=L else F(0)) for n in range(1,B+1)]))
    Q=[2*mc[k]-m[k] for k in range(b,B+1)]
    H=[(0,0)]
    for k in range(1,B+1):H.append(add(H[-1],box_fraction(F(1,k))))
    terms=[(d,F(v,den*den),log_integer(d)) for d,v in enumerate(z) if d and v]
    total=(0,0)
    for v in Q:total=add(total,box_fraction(v*v))
    out['Q_energy']=list(total)
    # Prime-log cancellation is symbolic globally; each block retains its own logs.
    tail_refusal = False
    for bank in (1,6):
        ds=(0,0);individual=(0,0)
        for k in range(b,B+1):
            blocks={};truncated=(0,0)
            for d,v,logd in terms:
                kern=scale(add(sub(H[k//d],H[k]),logd),F(1,d))
                term=scale(kern,v)
                if d<=B:truncated=add(truncated,term)
                individual=add(individual,square(term))
                core=1
                for p,power in factors(d):
                    if power%2 and bank%p:core*=p
                blocks[core]=add(blocks.get(core,(0,0)),term)
            for value in blocks.values():ds=add(ds,square(value))
            whole=(0,0)
            for value in blocks.values():whole=add(whole,value)
            exact=Q[k-b]*S
            if not F(truncated[0])<=exact<=F(truncated[1]):tail_refusal=True
            need(F(whole[0])<=exact<=F(whole[1]),'centered full-source kernel identity')
        out['bank_'+str(bank)]=dict(rough_block_diagonal=list(ds),
                                  cross_block_covariance=list(sub(total,ds)),
                                  product_diagonal=list(individual),
                                  distinct_product_covariance=list(sub(total,individual)))
    need(tail_refusal,'dropping above-B centered products must be detected')
    out['above_B_deletion_rejected']=tail_refusal
    return out


def report():
    return dict(status='finite directed-rational covariance; no uniform sign or gain',
                denominator=str(S),cases=[run(y,y<=15) for y in (3,7,15,63,255)])


def main():
    ap=argparse.ArgumentParser(description=__doc__);g=ap.add_mutually_exclusive_group()
    g.add_argument('--write',type=Path);g.add_argument('--check',type=Path);a=ap.parse_args()
    text=json.dumps(report(),sort_keys=True,separators=(',',':'))+'\n'
    if a.write:a.write.write_text(text,encoding='utf-8')
    if a.check:need(a.check.read_text(encoding='utf-8')==text,'adapter report mismatch')
    print('PASS',hashlib.sha256(text.encode()).hexdigest())

if __name__=='__main__':main()
