#!/usr/bin/env python3
"""Separate finite reconstruction: divisor inverse, unordered fibers, log expansion."""
from __future__ import annotations
import argparse, copy, hashlib, json, math
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

PREC=224; U=1<<PREC; GRID=1<<28
PARENT='2f0056d542603cb8118b9ac9da45b397162778e4'
SCOPE='finite native crossing panels and exact source identities; all-cofinal covariance bound and RH OPEN'

def demand(ok,text):
    if not ok:raise ValueError(text)
def canonical(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()
def sha(v):return hashlib.sha256(canonical(v)).hexdigest()
def rational(v):return [v.numerator,v.denominator]
def interval(a,b=1):
    demand(b>0,'denominator');return a*U//b,(a*U+b-1)//b
def iv(v):return interval(v.numerator,v.denominator)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def times(a,b):
    p=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]);return min(p)//U,(max(p)+U-1)//U
def integer(a,j):return (a[0]*j,a[1]*j) if j>=0 else (a[1]*j,a[0]*j)
def quotient(a,j):return a[0]//j,(a[1]+j-1)//j
def sq(a):
    p=(a[0]**2,a[1]**2);lo=0 if a[0]<=0<=a[1] else min(p)
    return lo//U,(max(p)+U-1)//U
def rounded(a):return [a[0]*GRID//U,(a[1]*GRID+U-1)//U]

@lru_cache(None)
def ln2():
    t=Fraction(1,3);a=t;r=Fraction(0)
    for k in range(96):r+=a/(2*k+1);a/=9
    e=2*a/Fraction(193)/Fraction(8,9)
    return (iv(2*r)[0],iv(2*r+e)[1])

@lru_cache(None)
def logarithm(n):
    demand(n>0,'log domain')
    if n==1:return (0,0)
    # Prime-by-prime expansion, exact rational series before directed conversion.
    for p in range(2,math.isqrt(n)+1):
        if n%p==0:return plus(logarithm(p),logarithm(n//p))
    e=n.bit_length()-1;den=1<<e;t=Fraction(n-den,n+den);a=t;r=Fraction(0)
    for k in range(96):r+=a/(2*k+1);a*=t*t
    error=2*a/(193*(1-t*t))
    base=(iv(2*r)[0],iv(2*r+error)[1])
    return plus(base,integer(ln2(),e))

def primitive(N):
    sp=list(range(N+1));mu=[0]*(N+1);mu[1]=1;la=[1]*(N+1)
    for p in range(2,math.isqrt(N)+1):
        if sp[p]==p:
            for n in range(p*p,N+1,p):
                if sp[n]==n:sp[n]=p
    for n in range(2,N+1):
        p=sp[n];v=n//p;mu[n]=0 if v%p==0 else -mu[v];la[n]=-la[v]
    return mu,la

def crossings(mu,N):
    den=1
    for k in range(1,N+1):den=math.lcm(den,k)
    total=0;out=[]
    for k in range(1,N+1):
        old=total;total+=mu[k]*(den//k)
        if k>1 and mu[k] and old*total<=0:
            demand(abs(total)*k<=den,'crossing inequality')
            out.append([k,rational(Fraction(old,den)),rational(Fraction(total,den))])
    return out

def make_source(prefix,Y,la):
    m=sum((Fraction(prefix[k],k) for k in range(1,Y+1)),Fraction(0))
    demand(prefix[Y] and m*(m-Fraction(prefix[Y],Y))<=0,'crossing guard')
    seq={k:Fraction(prefix[k]) for k in range(1,Y+1) if prefix[k]}
    if m:seq[2*Y]=-2*Y*m
    demand(all(la[k]*a>=0 and abs(a)<=2 for k,a in seq.items()),'sign/cap')
    den=1
    for a in seq.values():den=math.lcm(den,a.denominator)
    nums={k:int(a*den) for k,a in seq.items()}
    demand(sum((Fraction(a,k) for k,a in nums.items()),Fraction(0))==0,'moment')
    # Whole ordered max-kernel norm: a different calculation from source cells.
    norm=sum((Fraction(a*b,den*den*max(k,l)) for k,a in nums.items() for l,b in nums.items()),Fraction(0))
    m0=Fraction(0);energy=Fraction(0)
    for k in range(1,Y+1):m0+=seq.get(k,Fraction(0))/k;energy+=m0*m0
    tail=(Y-1)*m*m
    demand(norm==energy+tail and tail<=Fraction(1,Y),'full norm/tail')
    z={};keys=sorted(nums)
    for i,k in enumerate(keys):
        for l in keys[i:]:z[k*l]=z.get(k*l,0)+(1 if k==l else 2)*nums[k]*nums[l]
    z={k:v for k,v in z.items() if v}
    demand(all(la[k]*v>=0 for k,v in z.items()),'all convolution signs')
    demand(sum((Fraction(v,k) for k,v in z.items()),Fraction(0))==0,'product moment')
    # Recover the weighted-log identity at each prime independently.
    for p in range(2,2*Y+1):
        if any(p%d==0 for d in range(2,math.isqrt(p)+1)):continue
        total=Fraction(0)
        for d,zv in z.items():
            v=d;e=0
            while v%p==0:v//=p;e+=1
            if e:total+=Fraction(e*zv,d)
        demand(total==0,'prime log identity')
    return seq,m,den,nums,z,energy,tail,norm

def reconstruct(prefix,Y,native,mu,la):
    c,m,q,cn,z,FY,T,J=make_source(prefix,Y,la);B=(Y+1)**2-1;den=q*q
    # c*(delta+e), e=delta-1*c. No use of the producer's 2c-1*c*c expansion.
    e=[0]*(B+2);e[1]=q
    for d,v in cn.items():
        for k in range(d,B+2,d):e[k]-=v
    v=[0]*(B+2)
    for d,a in cn.items():
        if d<=B+1:v[d]+=q*a
        for j in range(1,(B+1)//d+1):
            if e[j]:v[d*j]+=a*e[j]
    if native:
        demand(all(v[k]==den*mu[k] for k in range(1,B+1)),'entire output prefix')
        demand(den*mu[B+1]-v[B+1]==e[Y+1]**2,'excluded index')
    H=[(0,0)]*(B+1);pH=[(0,0)]*(B+1);p2=[(0,0)]*(B+1)
    out=(0,0);mc=(0,0);new=(0,0);old=(0,0);QN=(0,0)
    for k in range(1,B+1):
        H[k]=plus(H[k-1],interval(1,k));pH[k]=plus(pH[k-1],H[k]);p2[k]=plus(p2[k-1],sq(H[k]))
        out=plus(out,interval(v[k],den*k));mc=plus(mc,interval(cn.get(k,0),q*k))
        if k<=Y:old=plus(old,sq(out))
        else:
            new=plus(new,sq(out));Q=minus(integer(mc,2),out);QN=plus(QN,sq(Q))
    D=(0,0);groups=0
    for d,zv in sorted(z.items()):
        lg=logarithm(d);start=Y+1;whole=(0,0)
        while start<=B:
            j=start//d;end=min(B,(j+1)*d-1);cnt=end-start+1;groups+=1
            if Y<=19:
                term=(0,0)
                for k in range(start,end+1):term=plus(term,sq(plus(minus(H[j],H[k]),lg)))
            else:
                sh=minus(pH[end],pH[start-1]);sh2=minus(p2[end],p2[start-1])
                # Expand separately in log d and the harmonic difference.
                a=minus(integer(H[j],cnt),sh)
                b=plus(minus(integer(sq(H[j]),cnt),integer(times(H[j],sh),2)),sh2)
                term=plus(plus(integer(sq(lg),cnt),integer(times(lg,a),2)),b)
            demand(term[1]>=0,'block upper nonnegative');whole=plus(whole,(max(0,term[0]),term[1]));start=end+1
        D=plus(D,times(interval(zv*zv,den*den*d*d),whole))
    C=minus(QN,D);FB=plus(old,new)
    demand(FB[0]<=plus(plus(iv(FY+8*T),integer(D,2)),integer(C,2))[1],'update')
    if native:demand(C[1]<0,'native finite sign')
    else:demand(100*C[0]>177*U and 100*C[1]<178*U,'fake finite sign')
    return {'Y':Y,'native':native,'B':B,'source_rows_sha256':sha([[k,rational(a)] for k,a in sorted(c.items())]),'late_coefficient':rational(c.get(2*Y,Fraction(0))),
            'source_J':rounded(iv(J)),'F_Y':rounded(iv(FY)),'tail_energy':rational(T),'products':len(z),
            'product_rows_sha256':sha([[k,rational(Fraction(a,den))] for k,a in sorted(z.items())]),
            'all_output_sha256':sha([rational(Fraction(a,den)) for a in v[1:]]),'coefficient_count':B,
            'diagonal_groups':groups,'D':rounded(D),'Q_squared':rounded(QN),'covariance':rounded(C),'F_B':rounded(FB)}

def fake_prefix():
    a=[Fraction(0)]*20
    for n in [1,3,5,7,8,11,12,13,17,18,19]:a[n]=Fraction(-1)
    a[1]=Fraction(1);a[3]=-Fraction(16328359,38798760)
    demand(sum((a[k]/k for k in range(1,20)),Fraction(0))==-Fraction(1,38),'fake exact endpoint')
    return a

def native_pair(mu,la):
    c,m,q,cn,z,FY,T,J=make_source(mu,5,la)
    H=[(0,0)]*36
    for k in range(1,36):H[k]=plus(H[k-1],interval(1,k))
    p=(0,0)
    for k in range(6,36):
        a=plus(minus(H[k//2],H[k]),logarithm(2))
        b=plus(minus(H[k//5],H[k]),logarithm(5))
        p=plus(p,quotient(times(a,b),10))
    p=times(interval(2*z[2]*z[5],q**4),p)
    demand(p[0]*100>U,'positive pair')
    return {'Y':5,'pair':[2,5],'ordered_pair':rounded(p),'strict_lower':[1,100]}

def rebuild():
    mu,la=primitive(4*432**2);xs=crossings(mu,1024)
    Ys=[r[0] for r in xs if r[0]<=127]+[173,210,431]
    rows=[reconstruct(mu,Y,True,mu,la) for Y in Ys]
    fake=reconstruct(fake_prefix(),19,False,mu,la)
    b={'schema':'XCC26-1','parent':PARENT,'scope':SCOPE,'scale':GRID,'crossing_cutoff':1024,'crossing_indices':[r[0] for r in xs],'crossing_rows_sha256':sha(xs),
       'panels':rows,'fake_panel':fake,'positive_native_pair':native_pair(mu,la),'native_sign_bound_unbounded':False,'RH_proved':False,
       'counts':{'crossings':len(xs),'native_panels':len(rows),'product_time_cells':sum(r['products']*(r['B']-r['Y']) for r in rows),
                 'diagonal_groups':sum(r['diagonal_groups'] for r in rows),'reproduced_coefficients':sum(r['B'] for r in rows)}}
    return {'body':b,'sha256':sha(b)}

def pairs(kv):
    d={}
    for k,v in kv:
        demand(k not in d,'duplicate key');d[k]=v
    return d

def read(path):
    def reject_float(s):raise ValueError('noninteger JSON number')
    return json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=reject_float,parse_constant=reject_float)

def accept(given,expected):
    demand(type(given) is dict and set(given)=={'body','sha256'},'envelope')
    demand(type(given['sha256']) is str and given['sha256']==sha(given['body']),'seal')
    demand(canonical(given)==canonical(expected),'primitive typed reconstruction')

def selftest(expected):
    tests=[]
    def change(fn):
        v=copy.deepcopy(expected);fn(v['body']);v['sha256']=sha(v['body']);tests.append(v)
    change(lambda b:b.__setitem__('RH_proved',True))
    change(lambda b:b.__setitem__('native_sign_bound_unbounded',True))
    change(lambda b:b['panels'].pop())
    change(lambda b:b.__setitem__('crossing_cutoff',2048))
    change(lambda b:b['panels'][0].__setitem__('B',36))
    change(lambda b:b['panels'][0]['covariance'].__setitem__(0,0))
    change(lambda b:b['fake_panel'].__setitem__('native',True))
    change(lambda b:b['positive_native_pair'].__setitem__('ordered_pair',[0,0]))
    change(lambda b:b['positive_native_pair']['pair'].__setitem__(0,True))
    change(lambda b:b.__setitem__('scale',float(GRID)))
    change(lambda b:b['panels'][0]['source_J'].__setitem__(0,b['panels'][0]['source_J'][0]+1))
    change(lambda b:b['crossing_indices'].pop())
    for t in tests:
        demand(canonical(t)!=canonical(expected),'genuine mutation')
        try:accept(t,expected)
        except ValueError:pass
        else:raise ValueError('corruption accepted')
    try:json.loads('{"a":1,"a":2}',object_pairs_hook=pairs)
    except ValueError:pass
    else:raise ValueError('duplicate accepted')
    print('RESEALED CORRUPTIONS REJECTED',len(tests),'DUPLICATE KEYS REJECTED')

def manifest():
    root=Path(__file__).resolve().parent;m=root/'MANIFEST.json'
    demand(m.is_file() and not m.is_symlink(),'required manifest')
    doc=read(m);expected=set(doc)|{'MANIFEST.json'}
    actual={p.name for p in root.iterdir() if p.name!='__pycache__'}
    demand(actual==expected,'exact inventory')
    for n,h in doc.items():
        p=root/n;demand(p.is_file() and not p.is_symlink(),'regular file')
        demand(hashlib.sha256(p.read_bytes()).hexdigest()==h,'source hash '+n)

def main():
    p=argparse.ArgumentParser();p.add_argument('report',type=Path);p.add_argument('--output',type=Path);p.add_argument('--self-test',action='store_true');a=p.parse_args()
    manifest();expected=rebuild();accept(read(a.report),expected)
    if a.self_test:selftest(expected)
    if a.output:a.output.write_bytes(canonical(expected)+b'\n')
    print('SEPARATE REPLAY PASS',expected['sha256']);print(expected['body']['counts'])
if __name__=='__main__':main()
