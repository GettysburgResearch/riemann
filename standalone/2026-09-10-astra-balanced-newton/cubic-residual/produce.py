#!/usr/bin/env python3
"""CIR26 finite producer: complete coefficients and outward annular sums."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

W=1<<128
OUT=1<<28
PANELS=list(range(1,13))+[15,19]
PREFIXES=[1,3,7,15,31,63]
PARENT='098acb780655eb81f8b842be201596a50198e757'
SCOPE={'rh_proved':False,'native_all_scale_covariance_proved':False,
       'update':'3c-3(1*c*c)+(1*1*c*c*c); native n<(Y+1)^3',
       'energy':'finite annular output; explicit finite recompletion includes its whole future',
       'diagonal':'one combined quadratic/cubic atom per integer product',
       'new_packet_bound':'finite cutoff with (1+log X)^3; NOT uniform infinite raw-stage energy'}

def need(c,m):
    if not c:raise ValueError(m)
def enc(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def sha(x):return hashlib.sha256(enc(x)).hexdigest()
def up(a,b):return -((-a)//b)
def rat(q):return [q.numerator,q.denominator]
def fi(q):return (q.numerator*W//q.denominator,up(q.numerator*W,q.denominator))
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(a,q):
    q=F(q);v=[q.numerator*a[0],q.numerator*a[1]]
    return min(v)//q.denominator,up(max(v),q.denominator)
def mul(a,b):
    z=[x*y for x in a for y in b];return min(z)//W,up(max(z),W)
def square(a):
    x,y=a;return (0 if x<=0<=y else min(x*x,y*y),max(x*x,y*y))
def energy(v):
    a=b=0
    for x in v:l,h=square(x);a+=l;b+=h
    return a//W,up(b,W)
def cell(v):return [v[0]*OUT//W,up(v[1]*OUT,W)]

def logq(q):
    e=0
    while q>=2:q/=2;e+=1
    def base(q):
        t=(q-1)/(q+1);power=t;s=F()
        for j in range(72):s+=2*power/(2*j+1);power*=t*t
        return s,s+2*power/F(145)/(1-t*t)
    a,b=base(F(2));c,d=base(q)
    return fi(e*a+c)[0],fi(e*b+d)[1]

def gamma():
    N=256;B=[F(1)]
    for n in range(1,23):B.append(-sum(F(math.comb(n+1,j))*B[j] for j in range(n))/F(n+1))
    s=sum((F(1,k) for k in range(1,N+1)),F())-F(1,2*N)
    s+=sum((B[2*k]/(2*k*N**(2*k)) for k in range(1,11)),F())
    err=abs(B[22]/(22*N**22));l,h=logq(F(N))
    return fi(s-err)[0]-h,fi(s+err)[1]-l

def mobius(N):
    mu=[1]*(N+1);mu[0]=0;mark=[False]*(N+1)
    for p in range(2,N+1):
        if not mark[p]:
            for n in range(p,N+1,p):mark[n]=True;mu[n]*=-1
            for n in range(p*p,N+1,p*p):mu[n]=0
    return mu

def state(Y,mu,fake=False):
    c={n:F(int(n==1) if fake else mu[n]) for n in range(1,Y+1)}
    c={n:a for n,a in c.items() if a}
    v=sum((a/n for n,a in c.items()),F());sgn=1 if v>=0 else-1;r=abs(v);j=Y
    need(r<=1,'endpoint bound')
    while r:
        j+=1;t=min(r,F(3,j));c[j]=-sgn*j*t;r-=t
    L=max(Y,j);need(L<=Y+(Y+1)//2 and max(map(abs,c.values()))<=3,'cap/support')
    need(sum((a/n for n,a in c.items()),F())==0,'source normalization')
    D=math.lcm(*(a.denominator for a in c.values()));ci={n:int(D*a) for n,a in c.items()}
    return c,L,D,ci

def convolution(c,d):
    out={}
    for n,a in c.items():
        for m,b in d.items():out[n*m]=out.get(n*m,0)+a*b
    return {n:a for n,a in out.items() if a}

def source_energy(c,Y,L):
    s=F();f=F();t=F();rows=[];physical=F();A=F()
    for k in range(1,L+1):
        s+=c.get(k,F())/k;rows.append(s)
        if k<=Y:f+=s*s
        else:t+=s*s
        A+=c.get(k,F());physical+=A*A/F(k*(k+1)) if k<L else A*A/F(k)
    need(s==0 and t<=f and physical==f+t,'complete source energy')
    return f,t,rows

def divisor_counts(N):
    a=[0]*(N+1)
    for d in range(1,N+1):
        for n in range(d,N+1,d):a[n]+=1
    return a

def cubic(c,L,D,ci,Y,tau):
    z2=convolution(ci,ci);z3=convolution(z2,ci);B=(Y+1)**3-1
    v=[0]*(B+2)
    for d,a in z3.items():
        for n in range(d,B+2,d):v[n]+=a*tau[n//d]
    for d,a in z2.items():
        for n in range(d,B+2,d):v[n]-=3*D*a
    for n,a in ci.items():
        if n<=B+1:v[n]+=3*D*D*a
    return z2,z3,v

def moments(z2,z3,L):
    primes=[p for p in range(2,L+1) if all(p%d for d in range(2,math.isqrt(p)+1))]
    den=math.lcm(*range(1,L+1))**3
    tests=0
    for degree,z in [(2,z2),(3,z3)]:
        terms=[]
        for d,a in z.items():
            x=d;vs=[]
            for p in primes:
                k=0
                while x%p==0:x//=p;k+=1
                vs.append(k)
            need(x==1,'factor coverage');terms.append((a*(den//d),vs))
        need(sum(a for a,_ in terms)==0,'zero moment');tests+=1
        for j in range(len(primes)):
            need(sum(a*v[j] for a,v in terms)==0,'prime moment');tests+=1
        if degree==3:
            for j in range(len(primes)):
                for k in range(j,len(primes)):
                    need(sum(a*v[j]*v[k] for a,v in terms)==0,'prime-pair moment');tests+=1
    return tests

def harmonics(B,tau):
    hlo=[0]*(B+1);hhi=hlo.copy();alo=hlo.copy();ahi=hlo.copy()
    for k in range(1,B+1):
        hlo[k]=hlo[k-1]+W//k;hhi[k]=hhi[k-1]+up(W,k)
        alo[k]=alo[k-1]+W*tau[k]//k;ahi[k]=ahi[k-1]+up(W*tau[k],k)
    return hlo,hhi,alo,ahi

def output_coords(v,D,B):
    lo=hi=0;out=[(0,0)]
    for k in range(1,B+1):
        lo+=v[k]*W//(D**3*k);hi+=up(v[k]*W,D**3*k);out.append((lo,hi))
    return out

def panel(Y,mu,tau,G,fake=False):
    c,L,D,ci=state(Y,mu,fake);f,t,iv=source_energy(c,Y,L)
    z2,z3,v=cubic(c,L,D,ci,Y,tau);B=(Y+1)**3-1;b=Y+1
    if not fake:need(v[1:B+1]==[D**3*x for x in mu[1:B+1]],'complete native cubic prefix')
    mt=moments(z2,z3,L);hlo,hhi,alo,ahi=harmonics(B,tau)
    q=output_coords(v,D,B);tvs=[(0,0)]*(B+1)
    for k,x in enumerate(iv,1):tvs[k]=fi(x)
    S=[(q[k][0]-3*tvs[k][1],q[k][1]-3*tvs[k][0]) for k in range(b,B+1)]
    se=energy(S);dl=du=0;cells=0;pk=0;mix=0
    lb=logq(F(B));theorem2lo=F(3300)*(1+F(lb[0],W))**3
    for d in sorted(set(z2)|set(z3)):
        ld=logq(F(d));ld2=mul(ld,ld);gl=mul(G,ld)
        con=(gl[0]-up(ld2[1],2),gl[1]-ld2[0]//2)
        aa=bb=kl=kh=ll=lh=0
        if d in z2 and d in z3:mix+=1
        for k in range(b,B+1):
            K=(hlo[k//d]-hhi[k]+ld[0],hhi[k//d]-hlo[k]+ld[1])
            P=mul(ld,(hlo[k],hhi[k]))
            Lam=(alo[k//d]-ahi[k]+P[0]+con[0],ahi[k//d]-alo[k]+P[1]+con[1])
            atom=add(scale(Lam,F(z3.get(d,0),D**3*d)),scale(K,F(-3*z2.get(d,0),D**2*d)))
            l,h=square(atom);aa+=l;bb+=h
            if d<=20:
                x,y=square(scale(K,F(1,d)));kl+=x;kh+=y
                x,y=square(scale(Lam,F(1,d)));ll+=x;lh+=y
        dl+=aa//W;du+=up(bb,W);cells+=B-b+1
        if d<=20:
            need(F(kh,W*W)<=F(18,d) and F(lh,W*W)<=theorem2lo/d,'packet finite bound');pk+=2
    cross=(se[0]-du,se[1]-dl)
    need(cross[1]<0 if not fake else True,'native finite sign failed; investigate, not extrapolate')
    ann=energy(q[b:]);row={'Y':Y,'B':B,'L':L,'native':not fake,'F_Y':rat(f),'collar':rat(t),
       'products':len(set(z2)|set(z3)),'combined_degree_indices':mix,'kernel_cells':cells,
       'moment_checks':mt,'packet_checks':pk,'S_energy':cell(se),'diagonal':cell((dl,du)),
       'covariance':cell(cross),'annular_output':cell(ann),
       'source_sha256':sha([[n,*rat(c[n])] for n in sorted(c)]),
       'products_sha256':sha([[d,z2.get(d,0)*D,z3.get(d,0)] for d in sorted(set(z2)|set(z3))])}
    # Exact native identity is checked without any transcendental constants.
    if Y<=5:
        for k in range(b,B+1):
            s2=sum((F(z2[d],D*D*d)*sum((F(1,j) for j in range(1,k//d+1)),F()) for d in z2),F())
            s3=sum((F(z3[d],D**3*d)*sum((F(tau[j],j) for j in range(1,k//d+1)),F()) for d in z3),F())
            actual=sum((F(v[n],D**3*n) for n in range(1,k+1)),F())
            need(actual==3*(iv[k-1] if k<=L else 0)-3*s2+s3,'rational aggregate identity')
    return row

def build():
    maxB=64**3;mu=mobius(maxB);tau=divisor_counts(maxB);G=gamma();prefix=[]
    for Y in PREFIXES:
        c,L,D,ci=state(Y,mu);z2,z3,v=cubic(c,L,D,ci,Y,tau);B=(Y+1)**3-1
        need(v[1:B+1]==[D**3*x for x in mu[1:B+1]],'prefix reconstruction')
        e=D*(int(Y+1==1))-sum(a for n,a in ci.items() if (Y+1)%n==0)
        need(D**3*mu[B+1]-v[B+1]==e**3,'sharp boundary error')
        prefix.append({'Y':Y,'B':B,'coefficients':B,'denominator':D,'output_sha256':sha(v[1:B+1]),'boundary_error_numerator':e**3})
    rows=[panel(y,mu,tau,G) for y in PANELS]
    fake=[panel(y,mu,tau,G,True) for y in [4,8,12]]
    constraints=0
    for n in range(1,257):
        need(sum(mu[d] for d in range(1,n+1) if n%d==0)==int(n==1),'divisor constraint');constraints+=1
    return {'schema':'CIR26/v1','parent':PARENT,'scope':SCOPE,'interval_denominator':OUT,
       'panels':rows,'fake':fake,'prefixes':prefix,'divisor_constraints':constraints,
       'gamma':cell(G),'kernel_cells':sum(r['kernel_cells'] for r in rows+fake),
       'primitive_generation':'new coefficients computed from short source; future Mobius used only as independent check'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--check',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    body=build();r={'body':body,'sha256':sha(body)}
    if a.check:need(enc(json.loads(a.check.read_text()))==enc(r),'canonical report mismatch')
    if a.output:a.output.write_bytes(enc(r)+b'\n')
    print('PASS',r['sha256']);print('panels',len(body['panels']),'kernel_cells',body['kernel_cells'])
if __name__=='__main__':main()
