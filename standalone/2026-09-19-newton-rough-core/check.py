#!/usr/bin/env python3
"""Exact finite arithmetic and outward dyadic enclosures for RCB26.

No third-party packages, zero tables, floating quadrature, or network.
The written all-Y estimates in PROOF.md are not proved by these finite tests.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from functools import lru_cache
from math import isqrt
from pathlib import Path

BITS = 112
S = 1 << BITS
F = Fraction


def need(ok: bool, text: str) -> None:
    if not ok:
        raise ValueError(text)


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def enclosure(q: F) -> tuple[int, int]:
    return q.numerator * S // q.denominator, ceil_div(q.numerator * S, q.denominator)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def scale(a, num: int, den: int = 1):
    need(den > 0, 'positive denominator required')
    lo, hi = (a[0]*num, a[1]*num) if num >= 0 else (a[1]*num, a[0]*num)
    return lo//den, ceil_div(hi, den)


def square(a):
    lo,hi=a
    return (0 if lo <= 0 <= hi else min(lo*lo,hi*hi), max(lo*lo,hi*hi))


def product(a,b):
    vals=[x*y for x in a for y in b]
    return min(vals),max(vals)


def overlap(a,b):
    return max(a[0],b[0]) <= min(a[1],b[1])


def pack(a, bits=2*BITS):
    return {'lo_numerator':str(a[0]),'hi_numerator':str(a[1]),'denominator_power_of_two':bits}


def factors(n: int) -> dict[int,int]:
    need(n >= 1, 'positive integer required')
    result={};p=2
    while p*p<=n:
        while n%p==0:
            result[p]=result.get(p,0)+1;n//=p
        p+=1
    if n>1: result[n]=result.get(n,0)+1
    return result


def rough_core(n: int, bank: frozenset[int]) -> int:
    a=1
    for p,e in factors(n).items():
        if e%2 and p not in bank: a*=p
    return a


def mu_trial(n: int) -> int:
    fs=factors(n)
    return 0 if any(e>1 for e in fs.values()) else (-1)**len(fs)


def sieve(n: int) -> list[int]:
    mu=[1]*(n+1);mu[0]=0;prime=[];comp=[False]*(n+1)
    for i in range(2,n+1):
        if not comp[i]: prime.append(i);mu[i]=-1
        for p in prime:
            if i*p>n: break
            comp[i*p]=True
            if i%p==0: mu[i*p]=0;break
            mu[i*p]=-mu[i]
    return mu


def clipped(prefix: list[int]) -> dict[int,F]:
    y=len(prefix)-1
    need(y>=1, 'empty prefix')
    c={n:F(prefix[n]) for n in range(1,y+1) if prefix[n]}
    m=sum((F(prefix[n],n) for n in range(1,y+1)),F(0))
    residual=abs(m); sign=1 if m>0 else -1
    n=y
    while residual:
        n+=1;value=min(F(3),n*residual)
        c[n]=-sign*value;residual-=value/n
    need(sum((v/n for n,v in c.items()),F(0))==0,'reciprocal balance')
    need(max(abs(v) for v in c.values())<=3,'coefficient cap')
    return c


def coalesce(c: dict[int,F]) -> dict[int,F]:
    z={}
    for r,u in c.items():
        for s,v in c.items(): z[r*s]=z.get(r*s,F(0))+u*v
    return {d:v for d,v in z.items() if v}


def log_series(y: F, terms: int=48) -> tuple[F,F]:
    need(0<=y<=F(1,3),'log reduction outside contract')
    q=y;total=F(0)
    for j in range(terms):
        total+=2*q/(2*j+1);q*=y*y
    rem=2*q/((2*terms+1)*(1-y*y))
    return total,total+rem


@lru_cache(None)
def log_bounds(n: int):
    need(n>=1,'log domain')
    k=n.bit_length()-1;two=1<<k
    a,b=log_series(F(1,3));c,d=log_series(F(n-two,n+two))
    lo=k*a+c;hi=k*b+d
    return lo.numerator*S//lo.denominator,ceil_div(hi.numerator*S,hi.denominator)


def harmonic(n):
    lo=[0]*(n+1);hi=[0]*(n+1)
    for k in range(1,n+1):
        lo[k]=lo[k-1]+S//k;hi[k]=hi[k-1]+ceil_div(S,k)
    return lo,hi


def running_reciprocal(values: dict[int,F],n: int):
    out=[(0,0)]*(n+1);a=(0,0)
    for k in range(1,n+1):
        a=add(a,enclosure(values.get(k,F(0))/k));out[k]=a
    return out


def add_sq(total,a):
    lo,hi=square(a);return total[0]+lo,total[1]+hi


def exact_source(y: int, native=True):
    B=(y+1)**2-1
    mu=sieve(B)
    prefix=mu[:y+1] if native else [0,1]+[0]*(y-1)
    c=clipped(prefix);z=coalesce(c)
    # A different divisor-fibre calculation of the complete Newton coefficients.
    v={n:2*c.get(n,F(0)) for n in range(1,B+1)}
    for d,a in z.items():
        for n in range(d,B+1,d): v[n]-=a
    if native:
        need(all(v[n]==mu[n] for n in range(1,B+1)), 'native Newton prefix')
        need(max(c)<=y+(y+1)//2,'clipped completion length')
    need(sum((a/d for d,a in z.items()),F(0))==0,'product reciprocal balance')
    # Authenticate log cancellation by exact coefficients of EACH prime logarithm.
    lp={}
    for d,a in z.items():
        for p,e in factors(d).items(): lp[p]=lp.get(p,F(0))+a*e/d
    need(all(a==0 for a in lp.values()),'prime-log cancellation')
    return B,mu,prefix,c,z,v


def panel(y: int,banks: list[list[int]],native=True):
    B,mu,prefix,c,z,v=exact_source(y,native)
    hl,hh=harmonic(B)
    mc=running_reciprocal(c,B);q=running_reciprocal(v,B)
    zitems=[(d,a.numerator,a.denominator*d,log_bounds(d)) for d,a in sorted(z.items())]
    banksets=[frozenset(bank) for bank in banks]
    classes=[{d:rough_core(d,bank) for d in z} for bank in banksets]
    energies=[(0,0) for _ in banks];diag=(0,0);qn=(0,0);increment=(0,0);tail=(0,0);mixed=(0,0)
    fy=(0,0)
    for k in range(1,y+1):fy=add_sq(fy,mc[k])
    for k in range(y+1,B+1):
        groups=[{} for _ in banks];Q=(0,0)
        for d,num,den,lg in zitems:
            raw=(hl[k//d]-hh[k]+lg[0],hh[k//d]-hl[k]+lg[1])
            term=scale(raw,num,den);Q=add(Q,term);diag=add_sq(diag,term)
            for j,cls in enumerate(classes):
                a=cls[d];groups[j][a]=add(groups[j].get(a,(0,0)),term)
        Q2=sub(scale(mc[k],2),q[k])
        need(overlap(Q,Q2),'centered and rational Newton output disagree')
        qn=add_sq(qn,Q2);increment=add_sq(increment,q[k]);tail=add_sq(tail,mc[k])
        pp=product(mc[k],Q2);mixed=(mixed[0]+pp[0],mixed[1]+pp[1])
        for j,group in enumerate(groups):
            for value in group.values(): energies[j]=add_sq(energies[j],value)
    ledger=(4*tail[0]+qn[0]-4*mixed[1],4*tail[1]+qn[1]-4*mixed[0])
    need(overlap(ledger,increment),'collar energy ledger')
    if native: need(tail[1] <= fy[1], 'finite tail-price control')
    panels=[]
    for bank,energy,cls in zip(banks,energies,classes):
        panels.append({'bank':bank,'groups':len(set(cls.values())),
            'block_energy':pack(energy),
            'within_block_off_diagonal':pack((energy[0]-diag[1],energy[1]-diag[0])),
            'cross_block_covariance':pack((qn[0]-energy[1],qn[1]-energy[0]))})
    return {'Y':y,'B':B,'source':'native_mu' if native else 'fake_delta1_prefix',
            'completion_end':max(c),'products_including_above_B':len(z),
            'products_above_B':sum(d>B for d in z),'source_input_energy':pack(fy),
            'output_annulus_energy':pack(increment),'Q_energy':pack(qn),
            'collision_diagonal':pack(diag),'collar_energy':pack(tail),
            'minus_four_collar_cross':pack((-4*mixed[1],-4*mixed[0])),
            'partitions':panels}


def small_checks():
    mu=sieve(4096)
    need(all(mu[n]==mu_trial(n) for n in range(1,4097)),'independent Mobius values')
    need(rough_core(12,frozenset())==3 and rough_core(18,frozenset({2}))==1,'parity core')
    count=0
    for d in range(1,129):
        fd=factors(d);tau=1;tau3=1
        for e in fd.values(): tau*=2*e+1;tau3*=(e+1)*(e+2)//2
        need(tau<=tau3,'squared-divisor majorant')
        for e in range(1,65):
            for bank in [frozenset(),frozenset({2,3})]:
                equivalent=all(p in bank or v%2==0 for p,v in factors(d*e).items())
                need((rough_core(d,bank)==rough_core(e,bank))==equivalent,'pair partition semantics')
                count+=1
    # Native all-order coefficient majorant tested independently on complete finite products.
    for y in range(1,41):
        c={n:F(mu[n]) for n in range(1,y+1) if mu[n]};z=coalesce(c)
        for d,a in z.items():
            ff=factors(d);need(all(e<=2 for e in ff.values()),'cube-free product')
            core=rough_core(d,frozenset());r=isqrt(d//core)
            need(r*r*core==d,'square factor')
            aa=0
            for u in range(1,y+1):
                if d%u==0 and d//u<=y:aa+=mu[u]*mu[d//u]
            need(a==aa and abs(a)<=2**len(factors(core)) and a*mu_trial(core)>=0,'native fibre bound')
    # A native nonzero collar, not only examples where completion is one atom.
    B,mu,prefix,c,z,v=exact_source(95)
    mc=running_reciprocal(c,B)
    need(max(c)>96 and mc[96][0]>0, 'nonzero native collar was not exercised')
    q95=running_reciprocal(v,B);I95=(0,0);T95=(0,0);Q95=(0,0);mix95=(0,0)
    for k in range(96,B+1):
        Q=sub(scale(mc[k],2),q95[k])
        I95=add_sq(I95,q95[k]);T95=add_sq(T95,mc[k]);Q95=add_sq(Q95,Q)
        vv=product(mc[k],Q);mix95=(mix95[0]+vv[0],mix95[1]+vv[1])
    ledger95=(4*T95[0]+Q95[0]-4*mix95[1],4*T95[1]+Q95[1]-4*mix95[0])
    need(overlap(ledger95,I95),'nonzero native full collar ledger')
    need(not overlap(I95,Q95),'dropping the nonzero collar must be detected')
    collar95={'annulus':[96,B],'I':pack(I95),'T':pack(T95),'Q_squared':pack(Q95),
              'minus_four_mixed':pack((-4*mix95[1],-4*mix95[0]))}

    # The strict square boundary genuinely fails for a small native completion.
    c=clipped([0,1]);z=coalesce(c)
    value=2*c.get(4,F(0))-sum((a for d,a in z.items() if 4%d==0),F(0))
    need(value!=mu_trial(4),'invalid inclusive square endpoint escaped')
    # Fake prefix fails the actual source test, though cap and balance are valid.
    fake=clipped([0,1]+[0]*14)
    need(sum(fake.get(d,F(0)) for d in [1,2])!=0,'fake native divisor inverse')
    # Deleting the completed product above B must break the balance ledger.
    B,_,_,c,z,_=exact_source(3)
    zz={d:a for d,a in z.items() if d<=B}
    need(sum((a/d for d,a in zz.items()),F(0))!=0,'dropped product control ineffective')
    # Explicit cap-three fake family: the whole declared interval is large.
    cf=clipped([0,1]+[0]*127);hf0,hf1=harmonic(4096);large_count=0
    for k in range(2048,4097):
        qq=(-hf1[k],-hf0[k])
        for n,value in cf.items():
            if n>1:
                qq=add(qq,scale((hf0[k//n],hf1[k//n]),-2*value.numerator,value.denominator*n))
        need(qq[1] <= -S//8,'cap-three fake quadratic lower-bound control')
        large_count+=1
    # Complete infinite off-diagonal Gram sign, with an explicit two-sided tail.
    R=8192;gl,gh=harmonic(R);gram=(0,0)
    for k in range(1,R+1):
        cols=[]
        for d in (2,4):
            lb=log_bounds(d)
            cols.append(scale((gl[k//d]-gh[k]+lb[0],gh[k//d]-gl[k]+lb[1]),1,d))
        pp=product(*cols);gram=(gram[0]+pp[0],gram[1]+pp[1])
    tail=ceil_div(4*S*S,R)
    gram=(gram[0]-tail,gram[1]+tail)
    need(gram[1]<0,'negative complete kernel entry')
    return {'trial_vs_sieve':4096,'pair_partition_checks':count,'native_fibre_cutoffs':40,
            'complete_G_2_4_enclosure':pack(gram),'complete_Gram_tail_from':R,
            'fake_Y128_entire_large_interval_checks':large_count,
            'nonzero_native_collar_Y':95,'native_Y95_collar_ledger':collar95,'native_collar_end':max(clipped(sieve(95))),
            'strict_boundary_control':True,'fake_source_rejected':True,'above_B_drop_rejected':True}


def make_report():
    checks=small_checks()
    p=[]
    for y in [5,15,31]:p.append(panel(y,[[],[2,3],[2,3,5,7]]))
    p.append(panel(63,[[2,3]]))
    p.append(panel(15,[[2,3]],False))
    # Certified counterexample to monotonicity under enlarging the prime bank.
    a=p[2]['partitions'][1]['block_energy'];b=p[2]['partitions'][2]['block_energy']
    need(int(b['lo_numerator'])>int(a['hi_numerator']),'bank monotonicity counterexample')
    need(int(p[1]['partitions'][0]['within_block_off_diagonal']['lo_numerator'])>0,'positive same-core control')
    need(int(p[-1]['partitions'][0]['cross_block_covariance']['lo_numerator'])>0,'fake positive cross control')
    return {'schema':'RCB26-1','mathematical_status':'proposed_component_proofs_RH_open',
            'arithmetic':'outward integer dyadic enclosures; exact rational source algebra',
            'bits':BITS,'checks':checks,'panels':p,
            'not_run':['unbounded estimate','independent mathematical review','whole-repository validator','Lean','remote CI']}


def canonical(report):
    return json.dumps(report,sort_keys=True,indent=2,ensure_ascii=True)+'\n'


def load_strict(path):
    def hook(items):
        out={}
        for key,value in items:
            need(key not in out,'duplicate JSON key');out[key]=value
        return out
    return json.loads(Path(path).read_text(),object_pairs_hook=hook)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',type=Path);group.add_argument('--check',type=Path)
    args=parser.parse_args();report=make_report();payload=canonical(report)
    if args.write:args.write.write_text(payload)
    else:
        need(canonical(load_strict(args.check))==payload,'result mismatch')
    print('PASS RCB26 finite source, partition, enclosure and controls')
    print('semantic_sha256='+hashlib.sha256(payload.encode()).hexdigest())

if __name__=='__main__':main()
