#!/usr/bin/env python3
"""Separate CIR26 reconstruction: residual powers, unordered factors, hyperbolas."""
from __future__ import annotations
import argparse, copy, hashlib, json, math
from fractions import Fraction as R
from pathlib import Path

PREC=1<<128
UNIT=1<<28
NATIVE=list(range(1,13))+[15,19]
STAGES=[1,3,7,15,31,63]
PARENT='098acb780655eb81f8b842be201596a50198e757'
SCOPE={'rh_proved':False,'native_all_scale_covariance_proved':False,
       'update':'3c-3(1*c*c)+(1*1*c*c*c); native n<(Y+1)^3',
       'energy':'finite annular output; explicit finite recompletion includes its whole future',
       'diagonal':'one combined quadratic/cubic atom per integer product',
       'new_packet_bound':'finite cutoff with (1+log X)^3; NOT uniform infinite raw-stage energy'}

def check(x,why):
    if not x:raise ValueError(why)
def dump(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def digest(x):return hashlib.sha256(dump(x)).hexdigest()
def ceiling(n,d):return -(-n//d)
def rational(q):return [q.numerator,q.denominator]
def interval(q):return q.numerator*PREC//q.denominator,ceiling(q.numerator*PREC,q.denominator)
def plus(a,b):return a[0]+b[0],a[1]+b[1]
def minus(a,b):return a[0]-b[1],a[1]-b[0]
def times(a,b):
    products=[x*y for x in a for y in b]
    return min(products)//PREC,ceiling(max(products),PREC)
def by(a,q):
    q=R(q);xs=[x*q.numerator for x in a]
    return min(xs)//q.denominator,ceiling(max(xs),q.denominator)
def square(a):
    l,h=a;return (0 if l<=0<=h else min(l*l,h*h),max(l*l,h*h))
def norm(xs):
    low=high=0
    for x in xs:a,b=square(x);low+=a;high+=b
    return low//PREC,ceiling(high,PREC)
def coarse(x):return [x[0]*UNIT//PREC,ceiling(x[1]*UNIT,PREC)]

def ln_base(x):
    v=(x-1)/(x+1);v2=v*v;term=v;s=R()
    for j in range(80):s+=term/R(2*j+1);term*=v2
    lo=2*s;hi=lo+2*term/(161*(1-v2))
    return lo,hi

def ln_integer(n):
    # Factoring logs in the consumer differs from binary reduction in producer.
    l=R();u=R();v=n;p=2
    while p*p<=v:
        e=0
        while v%p==0:v//=p;e+=1
        if e:
            k=p.bit_length()-1;a,b=ln_base(R(p,1<<k));c,d=ln_base(R(2));l+=e*(a+k*c);u+=e*(b+k*d)
        p+=1
    if v>1:
        k=v.bit_length()-1;a,b=ln_base(R(v,1<<k));c,d=ln_base(R(2));l+=a+k*c;u+=b+k*d
    return interval(l)[0],interval(u)[1]

def gamma_interval():
    # Independent Bernoulli reconstruction from t/(exp(t)-1), at N=512.
    degree=22;a=[R(1)]+[R(0)]*degree
    for j in range(1,degree+1):a[j]=-sum(a[j-k]/math.factorial(k+1) for k in range(1,j+1))
    bern=[a[j]*math.factorial(j) for j in range(degree+1)]
    n=512;H=sum((R(1,k) for k in range(1,n+1)),R())
    s=H-R(1,2*n)+sum((bern[2*k]/(2*k*n**(2*k)) for k in range(1,11)),R())
    error=abs(bern[22]/(22*n**22));lo,hi=ln_integer(n)
    return interval(s-error)[0]-hi,interval(s+error)[1]-lo

def primitives(N):
    smallest=[0]*(N+1)
    for p in range(2,N+1):
        if smallest[p]==0:
            for j in range(p,N+1,p):
                if smallest[j]==0:smallest[j]=p
    mu=[0]*(N+1);mu[1]=1
    for n in range(2,N+1):
        p=smallest[n];mu[n]=0 if (n//p)%p==0 else -mu[n//p]
    return mu

def completion(Y,mu,fake=False):
    source={n:R(int(n==1) if fake else mu[n]) for n in range(1,Y+1)}
    source={n:a for n,a in source.items() if a};m=sum((a/n for n,a in source.items()),R())
    sign=1 if m>=0 else-1;remaining=abs(m);capacity=R();previous=remaining;last=Y
    for j in range(1,(Y+1)//2+1):
        if previous==0:break
        n=Y+j;capacity+=R(3,n);current=max(R(),remaining-capacity)
        source[n]=sign*n*(current-previous);last=n;previous=current
    check(previous==0,'complete capped tail')
    D=1
    for q in source.values():D=math.lcm(D,q.denominator)
    ints={n:int(q*D) for n,q in source.items()}
    return source,last,D,ints

def products(ints):
    entries=sorted(ints.items());second={};third={}
    for i,(a,x) in enumerate(entries):
        for j in range(i,len(entries)):
            b,y=entries[j];second[a*b]=second.get(a*b,0)+(1 if i==j else 2)*x*y
            for k in range(j,len(entries)):
                c,z=entries[k];mult=1 if i==k else (3 if i==j or j==k else 6)
                third[a*b*c]=third.get(a*b*c,0)+mult*x*y*z
    return {n:v for n,v in second.items() if v},{n:v for n,v in third.items() if v}

def residual_output(ints,D,Y):
    B=(Y+1)**3-1;b=Y+1;end=B+1
    e=[0]*(end+1);e[1]=D
    for d,a in ints.items():
        for n in range(d,end+1,d):e[n]-=a
    # Fake controls do NOT have the native residual gap at b.
    first=next((n for n in range(1,end+1) if e[n]),end+1)
    ee=[0]*(end+1)
    for r in range(first,math.isqrt(end)+1):
        if not e[r]:continue
        for s in range(r,end//r+1):
            if e[s]:ee[r*s]+=(1 if r==s else 2)*e[r]*e[s]
    output=[0]*(end+1)
    for d,a in ints.items():
        if d<=end:output[d]+=a*D*D
        for m in range(first,end//d+1):output[d*m]+=a*(D*e[m]+ee[m])
    return output,e[b]

def energies(source,Y,L):
    m=R();old=R();tail=R();xs=[]
    for k in range(1,L+1):
        m+=source.get(k,R())/k;xs.append(m)
        if k<=Y:old+=m*m
        else:tail+=m*m
    check(m==0 and tail<=old,'tail trace')
    # Whole pair kernel includes the infinite constant cumulative tail.
    physical=sum((a*b/R(max(n,k)) for n,a in source.items() for k,b in source.items()),R())
    check(physical==old+tail,'full pair-kernel identity')
    return old,tail,xs

def rational_moments(z2,z3,L):
    ps=[p for p in range(2,L+1) if all(p%d for d in range(2,math.isqrt(p)+1))]
    modulus=math.lcm(*range(1,L+1))**3;tests=0
    for j,z in ((2,z2),(3,z3)):
        terms=[]
        for d,a in z.items():
            powers=[];n=d
            for p in ps:
                h=0
                while n%p==0:n//=p;h+=1
                powers.append(h)
            check(n==1,'all product factors');terms.append((a*(modulus//d),powers))
        check(sum(x for x,_ in terms)==0,'product mean');tests+=1
        for p in range(len(ps)):
            check(sum(x*v[p] for x,v in terms)==0,'first valuation jet');tests+=1
        if j==3:
            for p in range(len(ps)):
                for q in range(p,len(ps)):
                    check(sum(x*v[p]*v[q] for x,v in terms)==0,'second valuation jet');tests+=1
    return tests

def harmonic_hyperbola(N):
    H=[(0,0)]*(N+1)
    for k in range(1,N+1):H[k]=plus(H[k-1],interval(R(1,k)))
    A=[(0,0)]*(N+1)
    for k in range(1,N+1):
        r=math.isqrt(k);total=(0,0)
        for a in range(1,r+1):total=plus(total,by(H[k//a],R(2,a)))
        A[k]=minus(total,times(H[r],H[r]))
    return H,A

def partial_coordinates(v,D,B):
    answer=[(0,0)]
    for k in range(1,B+1):answer.append(plus(answer[-1],interval(R(v[k],D**3*k))))
    return answer

def reconstruct_panel(Y,mu,G,fake=False):
    c,L,D,ci=completion(Y,mu,fake);z2,z3=products(ci);v,eb=residual_output(ci,D,Y)
    B=(Y+1)**3-1;b=Y+1
    if not fake:check(v[1:B+1]==[x*D**3 for x in mu[1:B+1]],'native full interval')
    FY,T,xs=energies(c,Y,L);count=rational_moments(z2,z3,L);H,A=harmonic_hyperbola(B)
    q=partial_coordinates(v,D,B);t=[(0,0)]*(B+1)
    for k,x in enumerate(xs,1):t[k]=interval(x)
    S=[minus(q[k],by(t[k],3)) for k in range(b,B+1)]
    sumS=norm(S);diag=(0,0);cells=0;packet_tests=0;mixed=0
    logB=ln_integer(B);bound=R(3300)*(1+R(logB[0],PREC))**3
    for d in sorted(set(z2)|set(z3)):
        logd=ln_integer(d);const=minus(times(G,logd),by(times(logd,logd),R(1,2)))
        if d in z2 and d in z3:mixed+=1
        accumL=accumU=kl=kh=ll=lh=0
        for k in range(b,B+1):
            K=plus(minus(H[k//d],H[k]),logd)
            Lam=plus(plus(minus(A[k//d],A[k]),times(logd,H[k])),const)
            atom=plus(by(Lam,R(z3.get(d,0),D**3*d)),by(K,R(-3*z2.get(d,0),D**2*d)))
            l,h=square(atom);accumL+=l;accumU+=h
            if d<=20:
                l,h=square(by(K,R(1,d)));kl+=l;kh+=h
                l,h=square(by(Lam,R(1,d)));ll+=l;lh+=h
        diag=plus(diag,(accumL//PREC,ceiling(accumU,PREC)));cells+=B-b+1
        if d<=20:
            check(R(kh,PREC**2)<=R(18,d) and R(lh,PREC**2)<=bound/d,'finite packet budget');packet_tests+=2
    cross=minus(sumS,diag)
    if not fake:check(cross[1]<0,'finite native covariance is not negative')
    return {'Y':Y,'B':B,'L':L,'native':not fake,'F_Y':rational(FY),'collar':rational(T),
       'products':len(set(z2)|set(z3)),'combined_degree_indices':mixed,'kernel_cells':cells,
       'moment_checks':count,'packet_checks':packet_tests,'S_energy':coarse(sumS),'diagonal':coarse(diag),
       'covariance':coarse(cross),'annular_output':coarse(norm(q[b:])),
       'source_sha256':digest([[n,*rational(c[n])] for n in sorted(c)]),
       'products_sha256':digest([[d,z2.get(d,0)*D,z3.get(d,0)] for d in sorted(set(z2)|set(z3))])}

def reconstruct():
    mu=primitives(64**3);G=gamma_interval();stages=[]
    for Y in STAGES:
        c,L,D,ci=completion(Y,mu);v,e=residual_output(ci,D,Y);B=(Y+1)**3-1
        check(v[1:B+1]==[x*D**3 for x in mu[1:B+1]],'independent cubic generation')
        check(D**3*mu[B+1]-v[B+1]==e**3,'exact omitted boundary')
        stages.append({'Y':Y,'B':B,'coefficients':B,'denominator':D,'output_sha256':digest(v[1:B+1]),'boundary_error_numerator':e**3})
    panels=[reconstruct_panel(y,mu,G) for y in NATIVE]
    fake=[reconstruct_panel(y,mu,G,True) for y in [4,8,12]]
    for n in range(1,257):check(sum(mu[d] for d in range(1,n+1) if n%d==0)==int(n==1),'native inverse constraint')
    body={'schema':'CIR26/v1','parent':PARENT,'scope':SCOPE,'interval_denominator':UNIT,
       'panels':panels,'fake':fake,'prefixes':stages,'divisor_constraints':256,
       'gamma':coarse(G),'kernel_cells':sum(r['kernel_cells'] for r in panels+fake),
       'primitive_generation':'new coefficients computed from short source; future Mobius used only as independent check'}
    return {'body':body,'sha256':digest(body)}

def no_duplicates(pairs):
    d={}
    for k,v in pairs:
        check(k not in d,'duplicate JSON key');d[k]=v
    return d

def parse(text):return json.loads(text,object_pairs_hook=no_duplicates,parse_constant=lambda x:(_ for _ in ()).throw(ValueError('nonfinite JSON')))
def validate(actual,expected):
    check(type(actual) is dict and set(actual)=={'body','sha256'},'report keys')
    check(actual['sha256']==digest(actual['body']),'bad digest')
    check(dump(actual)==dump(expected),'typed primitive reconstruction mismatch')

def self_test(expected):
    changes=[lambda b:b['scope'].update(rh_proved=True),
       lambda b:b['scope'].update(native_all_scale_covariance_proved=True),
       lambda b:b['panels'].pop(),lambda b:b['prefixes'][-1].update(B=262144),
       lambda b:b['panels'][2]['covariance'].__setitem__(0,0),
       lambda b:b['panels'][0].update(combined_degree_indices=0),
       lambda b:b['prefixes'][0].update(boundary_error_numerator=0),
       lambda b:b['fake'][-1]['covariance'].__setitem__(1,0),
       lambda b:b.update(divisor_constraints=255),
       lambda b:b['panels'][0].update(native=1),
       lambda b:b['panels'][0].update(Y=1.0),
       lambda b:b.update(kernel_cells=1)]
    for i,f in enumerate(changes):
        bad=copy.deepcopy(expected);f(bad['body']);check(dump(bad)!=dump(expected),'no-op tamper')
        bad['sha256']=digest(bad['body'])
        try:validate(parse(dump(bad)),expected)
        except ValueError:continue
        raise ValueError('resealed corruption accepted '+str(i))
    try:parse('{"x":1,"x":2}')
    except ValueError:pass
    else:raise ValueError('duplicate key accepted')
    print('RESEALED CORRUPTIONS REJECTED',len(changes),'DUPLICATE KEYS REJECTED')

def main():
    p=argparse.ArgumentParser();p.add_argument('report',type=Path);p.add_argument('--self-test',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args()
    expected=reconstruct();validate(parse(a.report.read_text()),expected)
    if a.self_test:self_test(expected)
    if a.output:a.output.write_bytes(dump(expected)+b'\n')
    print('SEPARATE RECONSTRUCTION PASS',expected['sha256'])
if __name__=='__main__':main()
