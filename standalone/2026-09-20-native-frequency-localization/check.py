#!/usr/bin/env python3
"""NCL29 finite replay; Python standard library, exact sources, outward reals.

The infinite theorem is the written proof, not something this checker proves.
No network, floating arithmetic, special-function package, or zeta oracle is
used in accepting computations. Bounded defaults are intentional.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, gcd, isqrt, lcm
from pathlib import Path
from typing import Iterable

BITS = 144
SCALE = 1 << BITS
IV = tuple[int, int]
ZERO: IV = (0, 0)
ONE: IV = (SCALE, SCALE)
ROOT = Path(__file__).resolve().parent


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def ceildiv(a: int, b: int) -> int:
    require(b > 0, 'nonpositive integer denominator')
    return -((-a) // b)


def rat(x: int | F) -> IV:
    v = F(x)
    return v.numerator * SCALE // v.denominator, ceildiv(v.numerator * SCALE, v.denominator)


def add(a: IV, b: IV) -> IV:
    return a[0] + b[0], a[1] + b[1]


def neg(a: IV) -> IV:
    return -a[1], -a[0]


def sub(a: IV, b: IV) -> IV:
    return add(a, neg(b))


def mul(a: IV, b: IV) -> IV:
    v = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(v)//SCALE, ceildiv(max(v), SCALE)


def scale(a: IV, r: int | F) -> IV:
    x = F(r)
    if x < 0:
        return scale(neg(a), -x)
    return a[0]*x.numerator//x.denominator, ceildiv(a[1]*x.numerator, x.denominator)


def divint(a: IV, n: int) -> IV:
    require(n > 0, 'nonpositive divisor')
    return a[0]//n, ceildiv(a[1], n)


def square(a: IV) -> IV:
    v = min(a[0]*a[0], a[1]*a[1]) if a[0]*a[1] > 0 else 0
    return v//SCALE, ceildiv(max(a[0]*a[0], a[1]*a[1]), SCALE)


def reciprocal(a: IV) -> IV:
    require(a[0] > 0, 'reciprocal interval touches zero')
    return SCALE*SCALE//a[1], ceildiv(SCALE*SCALE, a[0])


def sumiv(values: Iterable[IV]) -> IV:
    lo = hi = 0
    for a,b in values:
        lo += a
        hi += b
    return lo, hi


def contains(a: IV, r: int | F) -> bool:
    x = F(r)*SCALE
    return a[0] <= x <= a[1]


def overlaps(a: IV, b: IV) -> bool:
    return max(a[0],b[0]) <= min(a[1],b[1])


def decimal_endpoint(n: int, places: int, upper: bool) -> str:
    v = ceildiv(n*10**places, SCALE) if upper else n*10**places//SCALE
    sign = '-' if v < 0 else ''
    v = abs(v)
    return f'{sign}{v//10**places}.{v%10**places:0{places}d}'


def enc(a: IV) -> dict:
    require(a[0] <= a[1], 'reversed interval')
    return {'lo': str(a[0]), 'hi': str(a[1]), 'bits': BITS,
            'decimal_outward': [decimal_endpoint(a[0],16,False),decimal_endpoint(a[1],16,True)]}


def frac(r: F) -> list[str]:
    return [str(r.numerator), str(r.denominator)]


@lru_cache(None)
def ataninverse(d: int) -> IV:
    require(d >= 2, 'arctangent parameter')
    n = 128
    acc = ZERO
    for j in range(n):
        acc = add(acc, rat(F((-1)**j, (2*j+1)*d**(2*j+1))))
    # Alternating series: n even, next term positive.
    tail = rat(F(1,(2*n+1)*d**(2*n+1)))
    return acc[0], acc[1]+tail[1]


@lru_cache(None)
def pi_iv() -> IV:
    # Machin identity. A distinct arctan(1/2)+arctan(1/3) reference is tested.
    return sub(scale(ataninverse(5),16),scale(ataninverse(239),4))


@lru_cache(None)
def cos_fraction(a: int, q: int) -> IV:
    require(q > 0, 'cos denominator')
    a %= q
    a = min(a, q-a)
    if a == 0:
        return ONE
    g = gcd(a,q)
    if g > 1:
        return cos_fraction(a//g,q//g)
    x = scale(pi_iv(),F(2*a,q))
    xx = square(x)
    term, out = ONE, ONE
    for j in range(1,49):
        term = divint(mul(term,xx),(2*j-1)*(2*j))
        out = add(out,term) if j%2 == 0 else sub(out,term)
    err = ceildiv(SCALE*4**98,factorial(98))
    # Taylor degree 97 (zero odd coefficient), real argument in [0,pi]<4.
    return max(-SCALE,out[0]-err), min(SCALE,out[1]+err)


def atanhpositive(z: IV) -> IV:
    require(0 <= z[0] <= z[1] <= ceildiv(SCALE,3), 'atanh domain')
    z2 = mul(z,z)
    term, out = z, ZERO
    for j in range(96):
        out = add(out,divint(term,2*j+1))
        term = mul(term,z2)
    out = scale(out,2)
    # Exact argument <=1/3. Full positive Taylor tail beyond exponent 191.
    tail = rat(F(9,4*193*3**193))
    return out[0], out[1]+tail[1]


@lru_cache(None)
def log2_iv() -> IV:
    return atanhpositive(rat(F(1,3)))


def log_dyadic(t: int) -> IV:
    require(t > 0, 'log requires positive input')
    k = t.bit_length()-1-BITS
    if k >= 0:
        num, den = t, SCALE << k
    else:
        num, den = t << (-k), SCALE
    require(den <= num < 2*den, 'log range reduction')
    z = rat(F(num-den,num+den))
    return add(scale(log2_iv(),k),atanhpositive(z))


def log_iv(x: IV) -> IV:
    require(x[0] > 0, 'log interval touches zero')
    return log_dyadic(x[0])[0], log_dyadic(x[1])[1]


@lru_cache(None)
def log_sine(a: int,q: int) -> IV:
    require(0 < a < q, 'log-sine root')
    # log(2sin(pi*a/q)) = (1/2)log(2-2cos(2pi*a/q)).
    return divint(log_iv(sub(rat(2),scale(cos_fraction(a,q),2))),2)


@lru_cache(None)
def factors(n: int) -> tuple[tuple[int,int], ...]:
    require(n >= 1, 'factor domain')
    out=[]
    p=2
    while p*p<=n:
        if n%p == 0:
            k=0
            while n%p == 0:
                n//=p; k+=1
            out.append((p,k))
        p+=1
    if n>1: out.append((n,1))
    return tuple(out)


@lru_cache(None)
def divisors(n: int) -> tuple[int, ...]:
    ds=[1]
    for p,a in factors(n):
        ds=[d*p**j for d in ds for j in range(a+1)]
    return tuple(sorted(ds))


def mu_trial(n: int) -> int:
    fs=factors(n)
    return 0 if any(a>1 for _,a in fs) else (-1)**len(fs)


def mu_sieve(N: int) -> list[int]:
    mu=[1]*(N+1); mu[0]=0
    mark=bytearray(N+1)
    for p in range(2,N+1):
        if not mark[p]:
            for k in range(p,N+1,p):
                mu[k]=-mu[k]
                if k>p: mark[k]=1
            for k in range(p*p,N+1,p*p): mu[k]=0
    return mu


def completion(y: int) -> tuple[list[F],F]:
    require(type(y) is int and 2<=y<=63,'finite checker cutoff outside 2..63')
    c=[F(mu_trial(n)) if n else F() for n in range(y+1)]
    m=F(); fy=F()
    for n in range(1,y+1):
        m+=c[n]/n;fy+=m*m
    while m:
        n=len(c)
        t=-min(F(3),n*abs(m))*(1 if m>0 else -1)
        c.append(t);m+=t/n
    require(len(c)-1<=2*y and max(map(abs,c))<=3,'invalid capped completion')
    return c,fy


def source_data(c: list[F], verify: bool=True) -> tuple[dict[int,F],list[F]]:
    L=len(c)-1
    require(sum((c[n]/n for n in range(1,L+1)),F())==0,'source is unbalanced')
    z=[F()]*(L*L+1)
    for r in range(1,L+1):
        for s in range(1,L+1): z[r*s]+=c[r]*c[s]
    amps={q:sum((z[d]/d for d in range(q,L*L+1,q)),F()) for q in range(2,L*L+1)}
    amps={q:v for q,v in amps.items() if v}
    if verify:
        U=[F()]*(L*L+1)
        for d in range(1,L+1):U[d]=sum((c[n]/n for n in range(d,L+1,d)),F())
        for q in range(2,L*L+1):
            other=sum((mu_trial(h)*U[d*h]*U[q//d] for d in divisors(q)
                       for h in divisors(q//d)),F())
            require(other==amps.get(q,F()),'gcd-threshold amplitude mismatch')
        for p in range(2,L+1):
            if factors(p)==((p,1),):
                q=p;s=F()
                while q<=L*L:s+=amps.get(q,F());q*=p
                require(s==0,'uncancelled full prime-log coefficient')
    return amps,z


def amplitude_moment(amps: dict[int,F]) -> F:
    return sum((q*v*v for q,v in amps.items()),F())


def blocks(Y: int) -> list[tuple[int,int,int]]:
    require(type(Y) is int and Y>=7,'global cutoff must be >=7')
    b=Y+1;B=b*b-1;x=b;out=[]
    while x<=B:
        end=min(2*x-1,B);y=isqrt(end)
        require(y<=Y and end<(y+1)**2 and 2*y<=x,'source schedule failure')
        out.append((x,end,y));x*=2
    require(len(out)==Y.bit_length(),'dyadic block count')
    return out


def spectral_values(amps: dict[int,F],last: int,H: int,far: bool) -> tuple[list[IV],IV,int]:
    """Direct angular spectral calculation, including full log tail constants.

    Conjugate pairs are combined BEFORE evaluation. For each denominator a
    finite cosine table is constructed with outward Taylor enclosures. Its
    entries are then summed with integer multiplicities (no floating FFT).
    """
    require(H>=2,'angular cutoff denominator')
    deriv=[ZERO]*(last+1);logc=ZERO;count=0
    for q,bq in amps.items():
        aa=[a for a in range(1,(q//2)+1) if gcd(a,q)==1 and
            ((H*a>=q)==far)]
        if not aa:continue
        multiplicities=[1 if 2*a==q else 2 for a in aa]
        count+=sum(multiplicities)
        logc=add(logc,scale(sumiv(scale(log_sine(a,q),m) for a,m in zip(aa,multiplicities)),bq))
        table=[cos_fraction(j,q) for j in range(q)]
        # Frequencies are q-periodic; compute only the required residue values.
        vals=[]
        for k in range(min(q,last+1)):
            low=high=0
            for a,m in zip(aa,multiplicities):
                t=table[(a*k)%q];low+=m*t[0];high+=m*t[1]
            vals.append(scale((low,high),bq))
        for k in range(1,last+1):deriv[k]=add(deriv[k],vals[k%q])
    acc=logc;out=[acc]
    for k in range(1,last+1):
        acc=add(acc,divint(deriv[k],k));out.append(acc)
    return out,logc,count


def prime_power_values(amps: dict[int,F],last: int) -> list[F]:
    """Whole prime-power sector; full prime-log constants cancel, not truncated."""
    coefficients: dict[int,F]={}
    logs: dict[int,F]={}
    for q,bq in amps.items():
        fs=factors(q)
        if len(fs)!=1:continue
        p,a=fs[0]
        coefficients[q]=coefficients.get(q,F())+bq
        d=q//p
        coefficients[d]=coefficients.get(d,F())-bq
        logs[p]=logs.get(p,F())+bq
    require(all(v==0 for v in logs.values()),'prime-power sector centering not zero')
    hs=[F()]*(last+1)
    for k in range(1,last+1):hs[k]=hs[k-1]+F(1,k)
    return [sum((v*hs[k//d] for d,v in coefficients.items()),F()) for k in range(last+1)]


def native_values(y: int,last: int,c: list[F],z: list[F]) -> tuple[list[F],int]:
    """Actual short-source output, with a separate full sieve for comparison."""
    future=mu_sieve(last)
    m=F();seq=[F()]
    for n in range(1,last+1):
        source=(2*c[n] if n<len(c) else F())-sum((z[d] for d in divisors(n) if d<len(z)),F())
        require(source==future[n],f'Newton coefficient mismatch at {n}')
        if n<=y:require(future[n]==mu_trial(n),'primitive mu disagreement')
        m+=source/n;seq.append(m)
    return seq,last


def block_panel(lo: int,hi: int,y: int,H: int,direct_near: bool) -> dict:
    c,fy=completion(y);amps,z=source_data(c)
    native,nchecked=native_values(y,hi,c,z)
    pp=prime_power_values(amps,hi)
    mixed={q:bq for q,bq in amps.items() if len(factors(q))>=2}
    far,logfar,nfar=spectral_values(mixed,hi,H,True)
    if direct_near:
        near,lognear,nnear=spectral_values(mixed,hi,H,False)
        require(contains(add(logfar,lognear),0),'full mixed angular log sum does not cancel')
        for k in range(hi+1):
            mc=sum((c[n]/n for n in range(1,min(k,len(c)-1)+1)),F())
            require(contains(add(add(far[k],near[k]),rat(pp[k])),2*mc-native[k]),'direct full spectral mismatch')
    else:
        near=[ZERO]*(hi+1)
        for k in range(lo,hi+1):near[k]=sub(rat(-native[k]-pp[k]),far[k])
        lognear=neg(logfar)
        nnear=sum(sum(1 for a in range(1,q) if gcd(a,q)==1) for q in mixed)-nfar
    good=[add(far[k],rat(pp[k])) for k in range(hi+1)]
    ef=sumiv(square(far[k]) for k in range(lo,hi+1))
    en=sumiv(square(near[k]) for k in range(lo,hi+1))
    ep=rat(sum((pp[k]**2 for k in range(lo,hi+1)),F()))
    eg=sumiv(square(good[k]) for k in range(lo,hi+1))
    cross=scale(sumiv(mul(good[k],near[k]) for k in range(lo,hi+1)),2)
    crosspf=scale(sumiv(scale(far[k],pp[k]) for k in range(lo,hi+1)),2)
    crosspn=scale(sumiv(scale(near[k],pp[k]) for k in range(lo,hi+1)),2)
    crossfn=scale(sumiv(mul(far[k],near[k]) for k in range(lo,hi+1)),2)
    native_energy=sum((native[k]**2 for k in range(lo,hi+1)),F())
    require(contains(add(add(eg,en),cross),native_energy),'energy/mixed-term decomposition')
    require(contains(sumiv([ep,ef,en,crosspf,crosspn,crossfn]),native_energy),'three-channel decomposition')
    L=len(c)-1;Q=L*L
    moment=amplitude_moment(amps)
    HL=sum((F(1,k) for k in range(1,L+1)),F())
    HQ=sum((F(1,k) for k in range(1,Q+1)),F())
    require(moment<=1024*3**4*HL**4*HQ**4,'denominator moment upper bound')
    oldQ=iroot(y**4*lo**6,11)
    beyond=sum(sum(1 for a in range(1,q) if gcd(a,q)==1 and H*min(a,q-a)>=q)
               for q in amps if q>oldQ and len(factors(q))>=2)
    return {'lo':lo,'hi':hi,'source_cutoff':y,'source_end':L,'eta':[1,H],
            'native_energy':enc(rat(native_energy)), 'far_energy':enc(ef),
            'near_energy':enc(en),'prime_power_energy':enc(ep),'good_energy':enc(eg),
            'twice_good_near':enc(cross),'twice_pp_far':enc(crosspf),
            'twice_pp_near':enc(crosspn),'twice_far_near':enc(crossfn),
            'far_centering_constant':enc(logfar),'near_centering_constant':enc(lognear),
            'near_method':'direct spectral' if direct_near else 'exact native complement',
            'far_frequencies':nfar,'near_frequencies':nnear,
            'far_composite_frequencies_beyond_local_NCG28_denominator_cut':beyond,
            'comparison_denominator_cut':oldQ,
            'coefficient_checks_including_overlap':nchecked,
            'weighted_amplitude_moment':frac(moment),
            'native_values_sha256':sha256(json.dumps([frac(v) for v in native],separators=(',',':')).encode()).hexdigest()}


def iroot(n: int,k: int) -> int:
    require(n>=0 and k>=1,'integer root domain')
    lo=0;hi=1<<(ceildiv(n.bit_length(),k)+1)
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**k<=n:lo=mid
        else:hi=mid
    return lo


def dec_iv(d: dict) -> IV:
    require(d['bits']==BITS,'wrong interval precision')
    return int(d['lo']),int(d['hi'])


def campaign(Y: int) -> dict:
    H=2*Y.bit_length()
    ps=[block_panel(lo,hi,y,H,y<=7) for lo,hi,y in blocks(Y)]
    totals={name:enc(sumiv(dec_iv(p[name]) for p in ps)) for name in
            ['native_energy','prime_power_energy','far_energy','near_energy','good_energy',
             'twice_good_near','twice_pp_far','twice_pp_near','twice_far_near']}
    return {'Y':Y,'B':(Y+1)**2-1,'eta':[1,H], 'covered_cells':sum(p['hi']-p['lo']+1 for p in ps),
            'panels':ps,'totals':totals}


def canonical(obj: object) -> bytes:
    return (json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode()


def reject_duplicates(pairs: list) -> dict:
    out={}
    for k,v in pairs:
        require(k not in out,'duplicate JSON key');out[k]=v
    return out


def read_report(path: Path) -> dict:
    require(path.is_file() and not path.is_symlink(),'not a regular report')
    return json.loads(path.read_text(),object_pairs_hook=reject_duplicates)


def same_types(a: object,b: object) -> bool:
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(same_types(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(same_types(x,y) for x,y in zip(a,b))
    return a==b


def validate_report(path: Path,actual: dict) -> None:
    expected=read_report(path)
    require(same_types(expected,actual),'report differs from complete reconstruction')


def produce(cutoffs: tuple[int,...]=(15,31)) -> dict:
    require(all(type(v) is int and 7<=v<=31 for v in cutoffs),'bounded campaign: Y in 7..31')
    return {'packet':'NCL29','schema':1,'arithmetic':'exact source algebra; 144-bit outward real intervals',
            'RH_proved':False,'infinite_theorem_proved_by_code':False,
            'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'cutoffs':list(cutoffs),'campaigns':[campaign(Y) for Y in cutoffs]}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write',type=Path)
    ap.add_argument('--check',type=Path)
    ap.add_argument('--cutoffs',type=int,nargs='+',default=[15,31])
    args=ap.parse_args()
    require(bool(args.write)^bool(args.check),'choose exactly one of --write and --check')
    data=produce(tuple(args.cutoffs))
    if args.write:args.write.write_bytes(canonical(data))
    else:validate_report(args.check,data)
    print('PASS_NCL29',sha256(canonical(data)).hexdigest())


if __name__=='__main__':main()
