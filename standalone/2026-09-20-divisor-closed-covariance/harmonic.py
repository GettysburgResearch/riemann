"""Actual PCR/RCB harmonic covariance; full floors, moments and endpoint products.
Gram entries use an exact floor-event formula, with directed intervals for logs.
"""
import argparse,hashlib
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
from arithmetic import sieve,divisors,near_candidates,completed_source,convolution,require,canonical,strict_read
from exact import ZERO,ONE,BITS,S,rat,add,sub,scale,mul,log_int,intersect
from transport import logs_from_sieve
CUTOFFS=(3,7,15,31,63,127,255)
WIDTHS=(0,1,3)

def abs_iv(v):
    return (max(0,v[0],-v[1]),max(abs(v[0]),abs(v[1])))

def pow_iv(x,n):
    ans=ONE
    for _ in range(n): ans=mul(ans,x)
    return ans

class Gram:
    """Closed sums for K_d(k)=(H_floor(k/d)-H_k+log d)/d, b<=k<=N."""
    def __init__(self,b,N,D,logs=None):
        require(1<=b<=N and D>=1,'Gram domain')
        self.b,self.N,self.D=b,N,D
        self.H=[ZERO]*(max(N,D)+1)
        for k in range(1,len(self.H)): self.H[k]=add(self.H[k-1],rat(1,k))
        if logs is None:
            spf,*_=sieve(max(N,D));logs=logs_from_sieve(max(N,D),spf)
        self.logs=logs
        self.hs=sub(self.hp(N),self.hp(b-1))
        self.h2s=sub(self.h2p(N),self.h2p(b-1))
        self.count=N-b+1
        self.cache={}
    def hp(self,k):
        return ZERO if k<=0 else sub(scale(self.H[k],k+1),rat(k))
    def h2p(self,k):
        if k<=0:return ZERO
        return add(sub(scale(mul(self.H[k],self.H[k]),k+1),scale(self.H[k],2*k+1)),rat(2*k))
    def fp(self,d,k):
        if k<0:return ZERO
        q=k//d
        return sub(scale(self.H[q],k+1),rat(d*q))
    def f2p(self,d,k):
        if k<0:return ZERO
        q=k//d
        return add(scale(self.h2p(q-1),d),scale(mul(self.H[q],self.H[q]),k-d*q+1))
    def fsum(self,d,l):
        if l>self.N:return ZERO
        return sub(self.fp(d,self.N),self.fp(d,max(self.b,l)-1))
    def pre(self,d):
        if d not in self.cache:
            a=self.fsum(d,self.b);mixed=ZERO
            for j in range(1,self.N//d+1):
                l=max(self.b,d*j)
                mixed=add(mixed,scale(sub(self.hp(self.N),self.hp(l-1)),1,j))
            self.cache[d]=(a,mixed)
        return self.cache[d]
    def pair(self,d,e):
        if d>e:d,e=e,d
        if d==1:return ZERO
        ad,bd=self.pre(d);ae,be=self.pre(e)
        if d==e:
            cross=sub(self.f2p(d,self.N),self.f2p(d,self.b-1))
        else:
            cross=ZERO
            for j in range(1,self.N//e+1):
                cross=add(cross,scale(self.fsum(d,max(self.b,e*j)),1,j))
        v=add(sub(sub(cross,bd),be),self.h2s)
        v=add(v,mul(self.logs[d],sub(ae,self.hs)))
        v=add(v,mul(self.logs[e],sub(ad,self.hs)))
        v=add(v,scale(mul(self.logs[d],self.logs[e]),self.count))
        return scale(v,1,d*e)

def stage(Y):
    b=Y+1;N=b*b-1;hmax=max(WIDTHS)
    spf,mu,rad,core,primes=sieve(N)
    c=completed_source(Y,mu);z=convolution(c);L=max(c);D=L*L
    spf,mu,rad,core,primes=sieve(max(N,D)+hmax)
    logs=logs_from_sieve(max(N,D),spf)
    zi={d:rat(v.numerator,v.denominator) for d,v in z.items()}
    civi={d:rat(v.numerator,v.denominator) for d,v in c.items()}
    require(sum((v/d for d,v in z.items()),Fraction())==0,'product reciprocal moment')
    # Log moment is proved prime by prime, with exact rational valuations.
    valuation_sums=defaultdict(Fraction)
    for d,v in z.items():
        n=d
        while n>1:
            p=spf[n];j=0
            while n%p==0:n//=p;j+=1
            valuation_sums[p]+=j*v/d
    require(all(v==0 for v in valuation_sums.values()),'product log moment')
    g=Gram(b,N,D,logs)
    norm=FY=FB=tail=cross=ZERO;mc=m=ZERO
    for k in range(1,N+1):
        m=add(m,rat(mu[k],k))
        if k in civi:mc=add(mc,scale(civi[k],1,k))
        FB=add(FB,mul(m,m))
        if k<b:FY=add(FY,mul(m,m))
        else:
            Q=sub(scale(mc,2),m)
            norm=add(norm,mul(Q,Q));tail=add(tail,mul(mc,mc));cross=add(cross,mul(mc,Q))
    require(intersect(FB,add(FY,add(sub(scale(tail,4),scale(cross,4)),norm))),'innovation update')
    diagonal=ZERO
    for d in sorted(z):diagonal=add(diagonal,mul(mul(zi[d],zi[d]),g.pair(d,d)))
    divs=divisors(D+hmax)
    classes=defaultdict(list);sq=abs_sq=ZERO;sq_count=0
    bins=[ZERO]*(hmax+1);absolute=[ZERO]*(hmax+1);counts=[0]*(hmax+1)
    all_pairs=above=0;sum_floor_terms=0
    for e in sorted(z):
        if e==1:continue
        candidates={d:(True,None) for d in classes[core[e]]}
        for d,r in near_candidates(e,hmax,divs):
            if d>=2 and d in z and d not in candidates:candidates[d]=(False,r)
        for d,(matched,r) in sorted(candidates.items()):
            G=g.pair(d,e);v=scale(mul(mul(zi[d],zi[e]),G),2)
            all_pairs+=1;above+=e>N;sum_floor_terms+=N//e
            if matched:sq=add(sq,v);abs_sq=add(abs_sq,abs_iv(v));sq_count+=1
            else:
                bins[r]=add(bins[r],v);absolute[r]=add(absolute[r],abs_iv(v));counts[r]+=1
        classes[core[e]].append(e)
    Htot=ZERO
    for k in range(1,D+hmax+1):Htot=add(Htot,rat(1,k))
    panels=[]
    for h in WIDTHS:
        geo=ab=ZERO;ct=0
        for j in range(h+1):geo=add(geo,bins[j]);ab=add(ab,absolute[j]);ct+=counts[j]
        if h==0:
            bound=scale(mul(pow_iv(add(ONE,logs[D]),2),pow_iv(Htot,6)),64*81)
        else:
            bound=scale(mul(pow_iv(add(ONE,logs[D]),2),pow_iv(Htot,7)),128*81*(2*h+1))
        require(ab[1]<=bound[0],'harmonic geometric sector envelope')
        remaining=sub(sub(sub(norm,diagonal),sq),geo)
        panels.append(dict(width=h,additional_geometric=geo,pair_absolute=ab,
            universal_envelope=bound,remaining_covariance=remaining,additional_pairs=ct,
            controlled_total=add(sq,geo)))
    return dict(Y=Y,N=N,L=L,D=D,active_products=len(z),products_above_endpoint=sum(d>N for d in z),
        source_digest=hashlib.sha256(canonical({str(k):[v.numerator,v.denominator] for k,v in c.items()}).encode()).hexdigest(),
        full_Q_energy=norm,individual_diagonal=diagonal,full_covariance=sub(norm,diagonal),
        squareclass_covariance=sq,squareclass_pair_absolute=abs_sq,squareclass_pairs=sq_count,
        F_input=FY,F_output=FB,completion_tail=tail,completion_cross=cross,
        pairs_evaluated=all_pairs,pairs_with_above_endpoint_product=above,floor_events=sum_floor_terms,panels=panels)

def build():
    return dict(schema='DCN26-harmonic-1',bits=BITS,stages=[stage(y) for y in CUTOFFS],
        status='proposed bound for near-integer-ratio covariance; far cross-core remainder open')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path)
    args=ap.parse_args();out=build();s=canonical(out)
    if args.write:args.write.write_text(s+'\n')
    if args.check:require(s==canonical(strict_read(args.check)),'harmonic report differs')
    print('DCN26 harmonic OK',hashlib.sha256(s.encode()).hexdigest())
if __name__=='__main__':main()
