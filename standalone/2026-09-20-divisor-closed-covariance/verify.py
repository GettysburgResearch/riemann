"""Separate checks. Does not import transport.py or harmonic.py.
Full physical P/comparable/near panels: trial factors and quotient enumeration.
Harmonic: every output coefficient, full small matrices, selected larger entries.
It shares only interval primitives and strict JSON utilities with the producer.
"""
import argparse, hashlib
from fractions import Fraction
from math import isqrt, gcd
from pathlib import Path
from arithmetic import require,canonical,strict_read
from exact import ZERO,S,BITS,rat,add,sub,scale,mul,log_int,intersect,decode

def factor(n):
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return out

def number_data(N):
    fs=[[]]+[factor(n) for n in range(1,N+1)]
    mu=[0]+[(-1)**len(f) if all(e==1 for p,e in f) else 0 for f in fs[1:]]
    rad=[1]*(N+1);repeat=[0]*(N+1)
    for n in range(2,N+1):
        for p,e in fs[n]:rad[n]*=p
        bad=[(p,e) for p,e in fs[n] if e>1]
        if len(bad)==1 and bad[0][1]==2:repeat[n]=bad[0][0]
    primes=[n for n in range(2,N+1) if fs[n]==[(n,1)]]
    return fs,mu,rad,repeat,primes

def divs_of(f):
    out=[1]
    for p,e in f:out=[d*p**j for d in out for j in range(e+1)]
    return out

def same(v,reported,label):
    x=decode(reported)
    require(x[1]-x[0] < S//10**16,'unacceptably wide certificate '+label)
    require(intersect(v,x),'independent mismatch '+label)

def typed_numbers(x):
    if isinstance(x,dict):
        for v in x.values():typed_numbers(v)
    elif isinstance(x,list):
        for v in x:typed_numbers(v)
    elif not isinstance(x,str):
        require(type(x) is int,'numeric type alias')

def verify_transport(report):
    typed_numbers(report)
    require(report.get('schema')=='DCN26-transport-1' and report.get('bits')==BITS,'transport schema')
    near_total=triple_total=0
    for row in report['stages']:
        Y=row['Y'];require(type(Y) is int and Y>=1,'typed cutoff')
        b=Y+1;N=b*b-1;X=N+1
        require(row['N']==N,'reported endpoint')
        fs,mu,rad,repeat,primes=number_data(N)
        M=[0]*(N+1);A=[ZERO]*(N+1)
        for n in range(1,N+1):M[n]=M[n-1]+mu[n]
        for p in primes:
            lp=log_int(p)
            for n in range(1,N//p+1):
                if mu[n]:A[p*n]=add(A[p*n],scale(lp,mu[n]))
        suffix=[ZERO]*(N+2)
        for k in range(N,b-1,-1):suffix[k]=add(suffix[k+1],rat(M[k],k*(k+1)))
        P=ZERO
        for p in primes:
            v=ZERO
            for n in range(1,N//p+1):
                if mu[n]:v=add(v,scale(suffix[max(b,p*n)],mu[n]))
            P=add(P,mul(log_int(p),v))
        same(P,row['P'],'full prime transport')
        weights=[rat(X-max(b,n),X*max(b,n)) for n in range(N+1)]
        comparable=ZERO
        # Direct original triples, without using the favorable-sign formula.
        for p in primes:
            subtotal=ZERO
            for n in range(1,N//p+1):
                if not mu[n]:continue
                t=p*n
                for m in divs_of(fs[t]):
                    if mu[m]:subtotal=add(subtotal,scale(weights[t],mu[m]*mu[n]));triple_total+=1
                for m in range(2*t,N+1,t):
                    if mu[m]:subtotal=add(subtotal,scale(weights[m],mu[m]*mu[n]));triple_total+=1
            comparable=add(comparable,mul(log_int(p),subtotal))
        same(comparable,row['comparable'],'comparable direct triples')
        H=max(p['width'] for p in row['panels']);bins=[ZERO]*(H+1);ct=[0]*(H+1)
        for d in range(2,N):
            lo=-min(H,(d-1)//2);hi=min(H,d//2)
            for r in range(lo,hi+1):
                if not r:continue
                first=1 if r>0 else 2
                for q in range(first,(N-r)//d+1):
                    s=q*d+r
                    if s<=d:continue
                    a=scale(A[s],mu[d]);c=scale(A[d],mu[s])
                    if a==ZERO and c==ZERO:continue
                    k=d//gcd(d,rad[s])
                    if repeat[s] and mu[d] and 1<k<=repeat[s]:continue
                    j=abs(r);bins[j]=add(bins[j],mul(add(a,c),weights[s]));ct[j]+=1
        for p in row['panels']:
            h=p['width'];v=ZERO
            for j in range(1,h+1):v=add(v,bins[j])
            same(v,p['near'],'near panel')
            same(sub(sub(P,comparable),v),p['remaining'],'far transport')
            require(sum(ct[:h+1])==p['pairs'],'near count')
        near_total+=sum(ct)
    return dict(physical_near_pairs=near_total,original_comparable_triples=triple_total,
                physical_stages=len(report['stages']))

def local_source(Y,mu):
    c=[Fraction(0)]+[Fraction(mu[n]) for n in range(1,Y+1)]
    residual=sum((c[n]/n for n in range(1,len(c))),Fraction())
    while residual:
        n=len(c);a=-residual*n
        if a>3:a=Fraction(3)
        if a< -3:a=Fraction(-3)
        c.append(a);residual+=a/n
    return {n:v for n,v in enumerate(c) if v}

def direct_harmonic_values(Y):
    N=(Y+1)**2-1;fs,mu,*_=number_data(N)
    c=local_source(Y,mu);D=max(c)**2
    z={}
    # Product fibres, not an ordered c-by-c producer loop.
    for t in range(1,D+1):
        a=sum((c.get(d,Fraction())*c.get(t//d,Fraction()) for d in divs_of(factor(t))),Fraction())
        if a:z[t]=a
    h=[Fraction(0)]*(N+1)
    for d,v in z.items():
        for n in range(d,N+1,d):h[n]+=v
    Q=ZERO;norm=ZERO;checks=0
    for n in range(1,N+1):
        require(h[n]==2*c.get(n,Fraction())-mu[n],'every Newton coefficient')
        v=h[n]/n;Q=add(Q,rat(v.numerator,v.denominator))
        if n>Y:norm=add(norm,mul(Q,Q))
        checks+=1
    return c,z,norm,checks

def harmonic_entry_direct(d,e,b,N):
    # Independent cell integration on the union of d/e floor jumps.
    H=[ZERO]*(N+1)
    for k in range(1,N+1):H[k]=add(H[k-1],rat(1,k))
    def hp(k):return ZERO if k<=0 else sub(scale(H[k],k+1),rat(k))
    def h2p(k):
        if k<=0:return ZERO
        return add(sub(scale(mul(H[k],H[k]),k+1),scale(H[k],2*k+1)),rat(2*k))
    jumps={b,N+1}
    jumps.update(range(((b+d-1)//d)*d,N+1,d))
    jumps.update(range(((b+e-1)//e)*e,N+1,e))
    xs=sorted(jumps);ans=ZERO
    for l,u in zip(xs,xs[1:]):
        a=add(H[l//d],log_int(d));c=add(H[l//e],log_int(e))
        sh=sub(hp(u-1),hp(l-1));sh2=sub(h2p(u-1),h2p(l-1))
        ans=add(ans,scale(add(sub(scale(mul(a,c),u-l),mul(add(a,c),sh)),sh2),1,d*e))
    return ans

def verify_harmonic(report):
    typed_numbers(report)
    require(report.get('schema')=='DCN26-harmonic-1' and report.get('bits')==BITS,'harmonic schema')
    checked=entries=0
    for row in report['stages']:
        Y=row['Y'];N=(Y+1)**2-1;c,z,norm,ct=direct_harmonic_values(Y)
        checked+=ct;same(norm,row['full_Q_energy'],'full original Q norm')
        if Y<=15:
            ds=sorted(d for d in z if d>1);diag=square=ZERO;geo={h:ZERO for h in (0,1,3)}
            for d in ds:
                v=z[d]*z[d];G=harmonic_entry_direct(d,d,Y+1,N)
                diag=add(diag,scale(G,v.numerator,v.denominator));entries+=1
            for i,d in enumerate(ds):
                sd=1
                for p,k in factor(d):
                    if k%2:sd*=p
                for e in ds[i+1:]:
                    se=1
                    for p,k in factor(e):
                        if k%2:se*=p
                    r=e%d;r=min(r,d-r)
                    if sd!=se and r>3:continue
                    v=2*z[d]*z[e];G=harmonic_entry_direct(d,e,Y+1,N)
                    val=scale(G,v.numerator,v.denominator);entries+=1
                    if sd==se:square=add(square,val)
                    else:
                        for h in geo:
                            if r<=h:geo[h]=add(geo[h],val)
            same(diag,row['individual_diagonal'],'small full diagonal')
            same(square,row['squareclass_covariance'],'small full squareclass')
            for p in row['panels']:
                h=p['width'];same(geo[h],p['additional_geometric'],'small full geometric sector')
                same(sub(sub(sub(norm,diag),square),geo[h]),p['remaining_covariance'],'small far sector')
    return dict(harmonic_coefficients=checked,independently_resummed_small_Gram_entries=entries,
        scope='all coefficients/norms, full selected sectors through Y=15; large sector totals are producer replays')

def run(folder):
    a=verify_transport(strict_read(folder/'transport_result.json'))
    b=verify_harmonic(strict_read(folder/'harmonic_result.json'))
    out=dict(**a,**b)
    samples=strict_read(folder/'kernel_samples.json')
    for p in samples['samples']:
        same(harmonic_entry_direct(p['d'],p['e'],p['b'],p['N']),p['G'],'union-of-jumps kernel')
    out['additional_independent_kernel_samples']=len(samples['samples'])
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--directory',type=Path,default=Path(__file__).parent/'reports')
    args=ap.parse_args();print('DCN26 independent scope',canonical(run(args.directory)))
if __name__=='__main__':main()
