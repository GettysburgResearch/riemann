#!/usr/bin/env python3
"""PCR26 fixed-corpus producer. Exact integers/rationals; no asymptotic inference."""
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction as F
from pathlib import Path

BITS=128
W=1<<BITS
OUT=1<<40
PANELS=list(range(1,25))+[31,32,47,63]
PREFIXES=[1,3,15,63,127,255]
PARENT="6671339d48c7f9bb846c15d8265e53f6856c2852"
SCOPE={"all_scale_native_covariance_bound_proved":False,"rh_proved":False,
       "normalization":"full cumulative energy; P_c(1)=0; tail amplitude cap 3",
       "diagonal":"coalesced integer product indices; no unaggregated duplicate split",
       "native_covariance_sign":"only the 28 complete declared finite annuli",
       "analytic_diagonal_and_tail":"written proofs, not finite extrapolation"}

def require(c, m):
    if not c: raise ValueError(m)

def enc(x): return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def sha(x): return hashlib.sha256(enc(x)).hexdigest()
def ceildiv(a,b): return -((-a)//b)
def rat(x): return [x.numerator,x.denominator]
def fi(x): return (x.numerator*W//x.denominator,ceildiv(x.numerator*W,x.denominator))
def square(v):
    a,b=v
    return (0 if a<=0<=b else min(a*a,b*b),max(a*a,b*b))
def cell(v):
    a,b=v
    lo=a*OUT//W;hi=b*OUT//W
    require(lo==hi,"coarse interval unresolved: raise precision, do not accept")
    return [lo,lo+1]
def product(a,b):
    v=[a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1]]
    return (min(v)//W,ceildiv(max(v),W))

def mobius(N):
    mu=[1]*(N+1);mu[0]=0;sieve=[True]*(N+1)
    for p in range(2,N+1):
        if sieve[p]:
            for n in range(p,N+1,p):mu[n]*=-1;sieve[n]=False
            for n in range(p*p,N+1,p*p):mu[n]=0
    return mu

def state(Y, mu, fake=False):
    c={n:F(int(n==1) if fake else mu[n]) for n in range(1,Y+1)}
    c={n:a for n,a in c.items() if a}
    a=sum((v/n for n,v in c.items()),F()); require(abs(a)<=1,"native reciprocal bound")
    r=abs(a);sgn=1 if a>=0 else -1;n=Y
    while r:
        n+=1;t=min(r,F(3,n));c[n]=-sgn*n*t;r-=t
    require(n<=Y+(Y+1)//2 and all(abs(v)<=3 for v in c.values()),"bounded-tail guards")
    require(sum((v/n for n,v in c.items()),F())==0,"safe-point zero")
    L=max(Y,max(c));D=math.lcm(*(v.denominator for v in c.values()))
    ci={n:int(v*D) for n,v in c.items()}
    z={}
    for r,a in ci.items():
        for s,b in ci.items():z[r*s]=z.get(r*s,0)+a*b
    z={n:a for n,a in z.items() if a}
    return c,L,D,ci,z

def primitive_values(c,Y,L):
    a=F();fy=F();tail=F();innovation=[]
    for k in range(1,L+1):
        a+=c.get(k,F())/k
        (innovation.append(a))
        if k<=Y:fy+=a*a
        else:tail+=a*a
    require(a==0 and tail<=fy,"energy trace guard")
    physical=F();s=F()
    for k in range(1,L):
        s+=c.get(k,F());physical+=s*s/F(k*(k+1))
    s+=c.get(L,F());physical+=s*s/F(L)
    require(physical==fy+tail,"entire physical norm identity")
    return fy,tail,physical,innovation

def newton(Y,c,L,D,ci,z,mu,native=True):
    B=(Y+1)**2-1
    v=[0]*(B+1)
    for d,a in z.items():
        for k in range(d,B+1,d):v[k]-=a
    for n,a in ci.items():
        if n<=B:v[n]+=2*a*D
    if native:require(all(v[n]==D*D*mu[n] for n in range(1,B+1)),"native coefficient production")
    return v

def harmonic(B):
    lo=[0]*(B+1);hi=[0]*(B+1)
    for k in range(1,B+1):lo[k]=lo[k-1]+W//k;hi[k]=hi[k-1]+ceildiv(W,k)
    return lo,hi

def log_unit(q):
    t=(q-1)/(q+1);u=t;v=F()
    for j in range(64):v+=2*u/F(2*j+1);u*=t*t
    error=2*u/F(129)/(1-t*t)
    return v,v+error

def log_integer(d):
    e=d.bit_length()-1
    a,b=log_unit(F(2));c,f=log_unit(F(d,1<<e))
    return fi(e*a+c)[0],fi(e*b+f)[1]

def logs_for(z,L):
    primes=[p for p in range(2,L+1) if all(p%d for d in range(2,math.isqrt(p)+1))]
    lp={p:log_integer(p) for p in primes};logs={};factors={}
    for d in z:
        n=d;a=b=0;fs={}
        for p in primes:
            v=0
            while n%p==0:n//=p;v+=1
            if v:fs[p]=v;a+=v*lp[p][0];b+=v*lp[p][1]
        require(n==1,"product prime coverage");logs[d]=(a,b);factors[d]=fs
    return logs,factors

def q_intervals(v,D):
    lo=hi=0;out=[(0,0)]
    for n in range(1,len(v)):
        lo+=v[n]*W//(D*D*n);hi+=ceildiv(v[n]*W,D*D*n);out.append((lo,hi))
    return out

def energy(vs):
    lo=hi=0
    for v in vs:
        a,b=square(v);lo+=a;hi+=b
    return lo//W,ceildiv(hi,W)

def panel(Y,mu,fake=False):
    c,L,D,ci,z=state(Y,mu,fake);fy,t,physical,iv=primitive_values(c,Y,L)
    v=newton(Y,c,L,D,ci,z,mu,not fake);B=(Y+1)**2-1;b=Y+1
    Hlo,Hhi=harmonic(B);logs,factors=logs_for(z,L)
    require(sum((F(a,d) for d,a in z.items()),F())==0,"zeroth product moment")
    for p in sorted({p for fs in factors.values() for p in fs}):
        require(sum((F(z[d]*factors[d].get(p,0),d) for d in z),F())==0,"prime-log product moment")
    q=q_intervals(v,D);xs=[(0,0)]*(B+1)
    for k,val in enumerate(iv,1):xs[k]=fi(val)
    Q=[(2*xs[k][0]-q[k][1],2*xs[k][1]-q[k][0]) for k in range(b,B+1)]
    qenergy=energy(q[b:]);Qenergy=energy(Q)
    dl=du=0;terms=0;pair_vectors={}
    for d,zint in sorted(z.items()):
        lo=hi=0;vec=[]
        ld,ud=logs[d]
        for k in range(b,B+1):
            aa=Hlo[k//d]-Hhi[k]+ld;bb=Hhi[k//d]-Hlo[k]+ud
            al,au=square((aa,bb));lo+=al;hi+=au
            if Y==3 and d in (2,3):
                zz=F(zint,D*D*d)
                vec.append((fi(zz*F(aa,W))[0],fi(zz*F(bb,W))[1]) if zz>=0 else
                           (fi(zz*F(bb,W))[0],fi(zz*F(aa,W))[1]))
        den=D**4*d*d*W
        dl+=zint*zint*lo//den;du+=ceildiv(zint*zint*hi,den);terms+=B-b+1
        if vec:pair_vectors[d]=vec
    cross=(Qenergy[0]-du,Qenergy[1]-dl)
    if not fake:require(cross[1]<0,"finite native covariance sign failed; retain failure")
    else:require(cross[0]>0,"fake covariance control missing")
    row={"Y":Y,"B":B,"L":L,"nonzero_source_coefficients":len(c),"product_indices":len(z),
         "kernel_cells":terms,"input_energy":rat(fy),"completion_extra":rat(t),
         "complete_input_energy":rat(physical),"diagonal":cell((dl,du)),
         "cross_covariance":cell(cross),"Q_energy":cell(Qenergy),"annular_output_energy":cell(qenergy),
         "source_sha256":sha([[n,*rat(c[n])] for n in sorted(c)]),
         "products_sha256":sha([[d,z[d]] for d in sorted(z)]),"coefficient_denominator":D}
    if Y==3:
        pl=ph=0
        for a,bv in zip(pair_vectors[2],pair_vectors[3]):
            aa,bb=product(a,bv);pl+=2*aa;ph+=2*bb
        require(40*pl>W,"positive native pair margin missing");row["positive_pair_2_3"]=cell((pl,ph))
    return row

def build():
    mu=mobius(65536);prefix=[];constraints=0
    for Y in PREFIXES:
        c,L,D,ci,z=state(Y,mu);v=newton(Y,c,L,D,ci,z,mu)
        prefix.append({"Y":Y,"through":len(v)-1,"coefficients":len(v)-1,
                       "output_sha256":sha(v[1:]),"denominator_squared":D*D})
    for n in range(1,257):
        require(sum(mu[d] for d in range(1,n+1) if n%d==0)==int(n==1),"native divisor constraint")
        constraints+=1
    rows=[panel(y,mu) for y in PANELS]
    fake=[panel(y,mu,True) for y in (16,32,64)]
    # Test the all-parameter fake lower bound at its first permitted b, without
    # expanding its much larger covariance grid.
    fy0=127;c0,L0,D0,ci0,z0=state(fy0,mu,True)
    v0=newton(fy0,c0,L0,D0,ci0,z0,mu,False);q0=q_intervals(v0,D0);b0=128
    I=list(range(ceildiv(b0*b0,4),b0*b0//3+1))
    J=list(range(ceildiv(3*b0*b0,4),b0*b0))
    gap=(min(q0[k][0] for k in J)-max(q0[k][1] for k in I),
         min(q0[k][1] for k in J)-max(q0[k][0] for k in I))
    ene=energy([q0[k] for k in I+J])
    require(2*gap[0]>W and 128*ene[0]>=b0*b0*W,"fake analytic-bound control")
    fake_large={"Y":fy0,"early_cells":len(I),"late_cells":len(J),
                "all_pair_gap":cell(gap),"two_block_energy":cell(ene),
                "proved_energy_floor":[b0*b0,128]}
    # Entire harmonic packet tails: |kappa_d(k)|<=2/k for k>=d.
    tails=[{"d":d,"first_omitted":R,"whole_l2_upper":rat(F(18,d)),
            "tail_l2_upper":rat(F(4,R-1))}
           for d in (1,2,3,7,31,127) for R in (max(d,2),max(2*d,3))]
    require(all((e+1)**2<=math.comb(e+3,3) for e in range(65)),"divisor collision inequality")
    return {"schema":"PCR26-v1","parent":PARENT,"scope":SCOPE,"interval_denominator":OUT,
            "native_panels":rows,"fake_panels":fake,"prefix_production":prefix,
            "packet_tail_bounds":tails,"fake_large_control":fake_large,
            "coverage":{"native_annuli":len(rows),"fake_annuli":len(fake),
                        "native_divisor_equations":constraints,"native_coefficients":sum(r['coefficients'] for r in prefix),
                        "kernel_cells":sum(r['kernel_cells'] for r in rows+fake),"scalar_tail_cases":len(tails)},
            "all_scale_constants":{"tail_coefficient_cap":3,"completion_factor":2,
                                   "packet_l2_constant":18,"diagonal_constant":1458,"recurrence_linear":9,
                                   "fake_Q_lower_denominator":128,"fake_bound_first_b":128}}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',type=Path);ap.add_argument('--output',type=Path)
    args=ap.parse_args();body=build();report={"body":body,"sha256":sha(body)}
    if args.check:require(enc(json.loads(args.check.read_text()))==enc(report),"canonical mismatch")
    if args.output:args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(enc(report)+b'\n')
    print('PASS',report['sha256']);print(json.dumps(body['coverage'],sort_keys=True))
if __name__=='__main__':main()
