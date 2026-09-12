#!/usr/bin/env python3
"""PCR26 separate primitive reconstruction; no producer/repository imports."""
from __future__ import annotations
import argparse, copy, hashlib, json, math, tempfile
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path

S=1<<160
O=1<<40
PARENT="6671339d48c7f9bb846c15d8265e53f6856c2852"
SCOPE={"all_scale_native_covariance_bound_proved":False,"rh_proved":False,
       "normalization":"full cumulative energy; P_c(1)=0; tail amplitude cap 3",
       "diagonal":"coalesced integer product indices; no unaggregated duplicate split",
       "native_covariance_sign":"only the 28 complete declared finite annuli",
       "analytic_diagonal_and_tail":"written proofs, not finite extrapolation"}

def check(ok,why):
    if not ok:raise ValueError(why)

def encode(x):return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
def digest(x):return hashlib.sha256(encode(x)).hexdigest()
def up(a,b):return -((-a)//b)
def pair(q):return [q.numerator,q.denominator]
def enclose(q):return (q.numerator*S//q.denominator,up(q.numerator*S,q.denominator))
def sq(v):
    l,u=v
    return (0 if l<=0<=u else min(l*l,u*u),max(l*l,u*u))
def times(a,b):
    vv=[x*y for x in a for y in b]
    return min(vv)//S,up(max(vv),S)
def quant(v):
    l=v[0]*O//S;u=v[1]*O//S
    check(l==u,'unresolved canonical interval, not accepted')
    return [l,l+1]
def norm(v):
    bounds=[sq(x) for x in v]
    return sum(x[0] for x in bounds)//S,up(sum(x[1] for x in bounds),S)

@lru_cache(None)
def factors(n):
    ff=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:ff.append((p,e))
        p+=1
    if n>1:ff.append((n,1))
    return tuple(ff)
@lru_cache(None)
def divisors(n):
    dd=[1]
    for p,e in factors(n):dd=[a*p**j for a in dd for j in range(e+1)]
    return tuple(dd)
def mu(n):
    ff=factors(n)
    return 0 if any(e>1 for p,e in ff) else (-1)**len(ff)

def state(Y,fake):
    a={n:Q(int(n==1) if fake else mu(n)) for n in range(1,Y+1)}
    a={n:c for n,c in a.items() if c}
    original=sum((c/n for n,c in a.items()),Q());amp=abs(original)
    check(amp<=1,'source reciprocal bound');sgn=1 if original>=0 else -1
    if amp:
        budget=Q();L=None
        for d in range(Y+1,Y+(Y+1)//2+1):
            new=budget+Q(3,d)
            if new>=amp:
                a[d]=-sgn*d*(amp-budget);L=d;break
            a[d]=Q(-3*sgn);budget=new
        check(L is not None,'finite clipping cover')
    else:L=Y
    scale=math.lcm(*(c.denominator for c in a.values()))
    ints={n:int(c*scale) for n,c in a.items()}
    z={}
    for n in range(1,L*L+1):
        val=sum(ints.get(d,0)*ints.get(n//d,0) for d in divisors(n))
        if val:z[n]=val
    check(sum((c/n for n,c in a.items()),Q())==0,'zero at one')
    check(all(abs(c)<=3 for c in a.values()),'coefficient cap')
    x=[];reciprocal=Q()
    for k in range(1,L+1):reciprocal+=a.get(k,Q())/k;x.append(reciprocal)
    check(reciprocal==0,'complete innovation tail')
    f=sum((v*v for v in x[:Y]),Q());tail=sum((v*v for v in x[Y:]),Q())
    check(tail<=f,'trace control')
    # Independent whole norm: ordered max-kernel, including the terminal future.
    whole=sum((c*d/Q(max(r,s)) for r,c in a.items() for s,d in a.items()),Q())
    check(whole==f+tail,'whole norm')
    return a,L,scale,ints,z,x,f,tail,whole

def output(Y,a,L,den,ints,z,native):
    B=(Y+1)**2-1
    v=[0]+[2*den*ints.get(n,0)-sum(z.get(d,0) for d in divisors(n)) for n in range(1,B+1)]
    if native:check(all(v[n]==den*den*mu(n) for n in range(1,B+1)),'native Newton coefficients')
    return v

def logq(q):
    t=(q-1)/(q+1);step=t*t;power=t;total=Q()
    for i in range(192):total+=2*power/Q(2*i+1);power*=step
    return total,total+2*power/Q(385)/(1-step)
@lru_cache(None)
def prime_log(p):
    base=1;e=0
    while 4*base<=p:base*=4;e+=1
    l4,u4=logq(Q(4));l,u=logq(Q(p,base))
    return enclose(e*l4+l)[0],enclose(e*u4+u)[1]
def logint(d):
    lo=hi=0
    for p,e in factors(d):a,b=prime_log(p);lo+=e*a;hi+=e*b
    return lo,hi

def Htable(B):
    vals=[(0,0)];h=Q()
    for k in range(1,B+1):h+=Q(1,k);vals.append(enclose(h))
    return vals

def panel(Y,fake=False):
    a,L,den,ints,z,x,F,T,whole=state(Y,fake);v=output(Y,a,L,den,ints,z,not fake)
    b=Y+1;B=b*b-1;ht=Htable(B)
    check(sum((Q(c,d) for d,c in z.items()),Q())==0,'product reciprocal moment')
    for p in {p for d in z for p,e in factors(d)}:
        check(sum((Q(c*dict(factors(d)).get(p,0),d) for d,c in z.items()),Q())==0,'additive prime-log cancellation')
    lo=hi=0;qs=[(0,0)]
    for n in range(1,B+1):
        lo+=v[n]*S//(den*den*n);hi+=up(v[n]*S,den*den*n);qs.append((lo,hi))
    xc=[(0,0)]*(B+1)
    for k,val in enumerate(x,1):xc[k]=enclose(val)
    # q can also be reconstructed directly from the primitive future mu here;
    # primitive comparison was at coefficient level, before any rounding.
    Qs=[(2*xc[k][0]-qs[k][1],2*xc[k][1]-qs[k][0]) for k in range(b,B+1)]
    QE=norm(Qs);outE=norm(qs[b:]);lower=upper=0
    for d,zz in sorted(z.items()):
        sum_lo=sum_hi=Alo=Ahi=0
        for k in range(b,B+1):
            h=(ht[k//d][0]-ht[k][1],ht[k//d][1]-ht[k][0])
            sum_lo+=h[0];sum_hi+=h[1];v0,v1=sq(h);Alo+=v0;Ahi+=v1
        # Sum the polynomial in log d, instead of squaring each full packet.
        ld=logint(d);mix=times(ld,(sum_lo,sum_hi));l2=sq(ld);count=B-b+1
        total_lo=Alo//S+2*mix[0]+count*l2[0]//S
        total_hi=up(Ahi,S)+2*mix[1]+up(count*l2[1],S)
        total_lo=max(0,total_lo)
        denominator=den**4*d*d
        lower+=zz*zz*total_lo//denominator;upper+=up(zz*zz*total_hi,denominator)
    cross=(QE[0]-upper,QE[1]-lower)
    check(cross[0]>0 if fake else cross[1]<0,'finite sign control')
    row={"Y":Y,"B":B,"L":L,"nonzero_source_coefficients":len(a),"product_indices":len(z),
         "kernel_cells":len(z)*(B-b+1),"input_energy":pair(F),"completion_extra":pair(T),
         "complete_input_energy":pair(whole),"diagonal":quant((lower,upper)),
         "cross_covariance":quant(cross),"Q_energy":quant(QE),"annular_output_energy":quant(outE),
         "source_sha256":digest([[n,*pair(a[n])] for n in sorted(a)]),
         "products_sha256":digest([[d,z[d]] for d in sorted(z)]),"coefficient_denominator":den}
    if Y==3:
        pl=ph=0
        for k in range(b,B+1):
            vals=[]
            for d in (2,3):
                ld,ud=logint(d);lv=ht[k//d][0]-ht[k][1]+ld;uv=ht[k//d][1]-ht[k][0]+ud
                c=Q(z[d],den*den*d)
                ll,uu=(c*Q(lv,S),c*Q(uv,S)) if c>=0 else (c*Q(uv,S),c*Q(lv,S))
                vals.append((enclose(ll)[0],enclose(uu)[1]))
            l,u=times(*vals);pl+=2*l;ph+=2*u
        check(40*pl>S,'positive individual native cross pair margin');row['positive_pair_2_3']=quant((pl,ph))
    return row

def reconstruct():
    prefix=[]
    for Y in (1,3,15,63,127,255):
        a,L,den,ints,z,x,F,T,J=state(Y,False);v=output(Y,a,L,den,ints,z,True)
        prefix.append({"Y":Y,"through":len(v)-1,"coefficients":len(v)-1,
                       "output_sha256":digest(v[1:]),"denominator_squared":den*den})
    for n in range(1,257):check(sum(mu(d) for d in divisors(n))==int(n==1),'native divisor identity')
    native=[panel(y) for y in list(range(1,25))+[31,32,47,63]]
    fake=[panel(y,True) for y in (16,32,64)]
    a0,L0,d0,i0,z0,x0,f0,t0,j0=state(127,True)
    v0=output(127,a0,L0,d0,i0,z0,False)
    lo=hi=0;q0=[(0,0)]
    for n in range(1,len(v0)):
        lo+=v0[n]*S//(d0*d0*n);hi+=up(v0[n]*S,d0*d0*n);q0.append((lo,hi))
    b0=128;I=[k for k in range(1,b0*b0) if b0*b0<=4*k and 3*k<=b0*b0]
    J=[k for k in range(1,b0*b0) if 3*b0*b0<=4*k]
    gap=(min(q0[k][0] for k in J)-max(q0[k][1] for k in I),
         min(q0[k][1] for k in J)-max(q0[k][0] for k in I))
    ee=norm([q0[k] for k in I+J])
    check(gap[0]*2>S and ee[0]*128>=b0*b0*S,'large fake-bound control')
    fake_large={"Y":127,"early_cells":len(I),"late_cells":len(J),
                "all_pair_gap":quant(gap),"two_block_energy":quant(ee),
                "proved_energy_floor":[b0*b0,128]}
    tails=[{"d":d,"first_omitted":R,"whole_l2_upper":pair(Q(18,d)),"tail_l2_upper":pair(Q(4,R-1))}
           for d in (1,2,3,7,31,127) for R in (max(d,2),max(2*d,3))]
    for e in range(65):check((e+1)**2<=math.comb(e+3,3),'prime-power divisor bound')
    return {"schema":"PCR26-v1","parent":PARENT,"scope":SCOPE,"interval_denominator":O,
            "native_panels":native,"fake_panels":fake,"prefix_production":prefix,
            "packet_tail_bounds":tails,"fake_large_control":fake_large,
            "coverage":{"native_annuli":len(native),"fake_annuli":len(fake),"native_divisor_equations":256,
                        "native_coefficients":sum(r['coefficients'] for r in prefix),
                        "kernel_cells":sum(r['kernel_cells'] for r in native+fake),"scalar_tail_cases":len(tails)},
            "all_scale_constants":{"tail_coefficient_cap":3,"completion_factor":2,"packet_l2_constant":18,
                                   "diagonal_constant":1458,"recurrence_linear":9,
                                   "fake_Q_lower_denominator":128,"fake_bound_first_b":128}}

def no_duplicates(pairs):
    out={}
    for k,v in pairs:
        check(k not in out,'duplicate JSON key');out[k]=v
    return out
def read(path):return json.loads(path.read_text(),object_pairs_hook=no_duplicates)
def validate(report,expected):
    check(type(report) is dict and set(report)=={'body','sha256'},'schema')
    check(digest(report['body'])==report['sha256'],'digest')
    check(encode(report['body'])==encode(expected),'typed primitive reconstruction mismatch')

def self_test(expected):
    changes=[lambda b:b['scope'].update(rh_proved=True),
      lambda b:b['scope'].update(all_scale_native_covariance_bound_proved=True),
      lambda b:b['native_panels'].pop(),
      lambda b:b['native_panels'][0].__setitem__('Y',True),
      lambda b:b['all_scale_constants'].__setitem__('tail_coefficient_cap',3.0),
      lambda b:b['native_panels'][0]['diagonal'].__setitem__(1,0),
      lambda b:b['native_panels'][0]['cross_covariance'].__setitem__(1,1),
      lambda b:b['fake_panels'][0]['cross_covariance'].__setitem__(0,0),
      lambda b:b['prefix_production'][-1].__setitem__('through',65536),
      lambda b:b['native_panels'][2]['positive_pair_2_3'].__setitem__(0,0),
      lambda b:b['packet_tail_bounds'][-1].__setitem__('tail_l2_upper',[0,1]),
      lambda b:b['coverage'].__setitem__('kernel_cells',0)]
    rejected=0
    with tempfile.TemporaryDirectory() as td:
        p=Path(td)/'changed.json'
        for mutate in changes:
            bad=copy.deepcopy(expected);mutate(bad)
            check(encode(bad)!=encode(expected),'no-op tamper')
            p.write_bytes(encode({'body':bad,'sha256':digest(bad)}))
            try:validate(read(p),expected)
            except ValueError as e:
                check('reconstruction' in str(e),'mutation only failed the checksum');rejected+=1
            else:raise ValueError('resealed tamper accepted')
        p.write_text('{"body":{},"body":{},"sha256":"x"}')
        try:read(p)
        except ValueError as e:check('duplicate' in str(e),'wrong duplicate-key refusal')
        else:raise ValueError('duplicate key accepted')
    return rejected

def main():
    ap=argparse.ArgumentParser();ap.add_argument('report',type=Path);ap.add_argument('--self-test',action='store_true');ap.add_argument('--output',type=Path)
    a=ap.parse_args();expected=reconstruct();validate(read(a.report),expected)
    if a.output:a.output.write_bytes(encode({'body':expected,'sha256':digest(expected)})+b'\n')
    print('SEPARATE RECONSTRUCTION PASS',digest(expected))
    if a.self_test:print('RESEALED CORRUPTIONS REJECTED',self_test(expected),'AND DUPLICATE KEY')
if __name__=='__main__':main()
