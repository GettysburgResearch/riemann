#!/usr/bin/env python3
"""MCB31 bounded finite checks. Infinite estimates require written proof review."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path
import exact as e

ROOT=Path(__file__).resolve().parent

def cutoff(t: F,H: int) -> F:
    e.require(type(H) is int and H>=1,'invalid bandwidth')
    e.require(t>=0,'negative scaled frequency')
    if t<=H:return F(1)
    if t>=2*H:return F()
    u=(t-H)/H
    return 1-10*u**3+15*u**4-6*u**5

def completion(y: int) -> tuple[list[F],list[F]]:
    e.require(type(y) is int and 2<=y<=255,'bounded cutoff must be 2..255')
    c=[F()]+[F(e.mu_trial(n)) for n in range(1,y+1)]
    m=F(); prefix=[F()]
    for n in range(1,y+1):m+=c[n]/n;prefix.append(m)
    while m:
        n=len(c);c.append(-min(F(3),n*abs(m))*(1 if m>0 else -1));m+=c[n]/n
    e.require(len(c)-1<=y+(y+1)//2,'completion support')
    e.require(max(map(abs,c))<=3,'completion cap')
    return c,prefix

def innovations(c: list[F]) -> list[F]:
    x=[F()];s=F()
    for n in range(1,len(c)):s+=c[n]/n;x.append(s)
    e.require(s==0,'source not reciprocally balanced')
    return x

def source(c: list[F]) -> tuple[list[F],dict[int,F]]:
    L=len(c)-1;innovations(c)
    z=[F()]*(L*L+1)
    for r in range(1,L+1):
        for s in range(1,L+1):z[r*s]+=c[r]*c[s]
    amps={q:sum((z[d]/d for d in range(q,L*L+1,q)),F()) for q in range(2,L*L+1)}
    U=[F()]*(L*L+1)
    for d in range(1,L+1):U[d]=sum((c[n]/n for n in range(d,L+1,d)),F())
    for q in range(2,L*L+1):
        alt=sum((e.mu_trial(h)*U[d*h]*U[q//d] for d in e.divisors(q) for h in e.divisors(q//d)),F())
        e.require(alt==amps[q],'threshold amplitude disagreement')
    return z,{q:a for q,a in amps.items() if a}

def frequency_map(amps: dict[int,F],X: int,H: int) -> dict[F,F]:
    e.require(X>=8*H,'band reaches unsafe angular range')
    out={}
    for q,b in amps.items():
        for a in range(1,min(q//2,(2*H*q+X-1)//X)):
            if gcd(a,q)!=1:continue
            w=cutoff(F(X*a,q),H)
            if w:out[F(a,q)]=b*w
    return out

def product_frequency_map(c: list[F],X: int,H: int) -> dict[F,F]:
    out={};L=len(c)-1
    for r in range(1,L+1):
        for s in range(1,L+1):
            if not c[r]*c[s]:continue
            d=r*s
            for j in range(1,(2*H*d+X-1)//X):
                w=cutoff(F(j*X,d),H)
                if w:
                    alpha=F(j,d)
                    out[alpha]=out.get(alpha,F())+c[r]*c[s]*w/d
    return {a:b for a,b in out.items() if b}

def newton(c: list[F],z: list[F],y: int,last: int) -> tuple[list[F],int]:
    e.require(last<(y+1)**2,'strict native endpoint exceeded')
    mu=e.mu_sieve(last);m=F();out=[F()]
    for n in range(1,last+1):
        v=(2*c[n] if n<len(c) else F())-sum((z[d] for d in e.divisors(n) if d<len(z)),F())
        e.require(v==mu[n],'native Newton coefficient mismatch')
        if n<=y:e.require(mu[n]==e.mu_trial(n),'primitive Mobius mismatch')
        m+=v/n;out.append(m)
    return out,last

def spectral(freq: dict[F,F],last: int) -> tuple[list[e.IV],e.IV]:
    deriv=[e.ZERO]*(last+1);constant=e.ZERO
    for alpha,b in sorted(freq.items()):
        a,q=alpha.numerator,alpha.denominator
        e.require(0<2*a<q,'conjugate-pair convention')
        co=e.cos_fraction(a,q);si=e.cos_fraction(q-4*a,4*q)
        constant=e.add(constant,e.scale(e.log_sine(a,q),2*b))
        cn,sn=e.ONE,e.ZERO
        for k in range(1,last+1):
            cn,sn=e.sub(e.mul(cn,co),e.mul(sn,si)),e.add(e.mul(sn,co),e.mul(cn,si))
            if k in (1,last//2,last):
                e.require(e.overlaps(cn,e.cos_fraction(k*a,q)),'rotation versus direct cosine')
            deriv[k]=e.add(deriv[k],e.scale(cn,2*b))
    acc=constant;out=[acc]
    for k in range(1,last+1):acc=e.add(acc,e.divint(deriv[k],k));out.append(acc)
    return out,constant

def energy(seq: list[e.IV],X: int,last: int) -> e.IV:
    return e.sumiv(e.square(seq[k]) for k in range(X,last+1))

def cross(a: list[e.IV],b: list[e.IV],X: int,last: int) -> e.IV:
    return e.scale(e.sumiv(e.mul(a[k],b[k]) for k in range(X,last+1)),2)

def encode_fraction(x: F) -> list[str]:return [str(x.numerator),str(x.denominator)]

def verify_difference_identity(c: list[F],z: list[F]) -> int:
    """Exact coefficients of f(d), before any numerical evaluation of f."""
    x=innovations(c);L=len(c)-1;coef={}
    for r in range(1,L):
        for s in range(1,L):
            for d,sgn in ((r*s,1),((r+1)*s,-1),(r*(s+1),-1),((r+1)*(s+1),1)):
                coef[d]=coef.get(d,F())+sgn*x[r]*x[s]
    for d in range(1,L*L+1):e.require(coef.get(d,F())==z[d]/d,'double summation-by-parts mismatch')
    return L*L

def panel(y: int,H: int,X: int | None=None,last: int | None=None) -> dict:
    if X is None:X=(y+1)**2//2
    if last is None:last=(y+1)**2-1
    e.require(X<=last<2*X and isqrt(last)==y,"observation block mismatch")
    c,old=completion(y);L=len(c)-1
    e.require(X>=8*H and L*L<=8*X and L<=X,'block/source hypotheses')
    z,amps=source(c);freq=frequency_map(amps,X,H)
    e.require(freq==product_frequency_map(c,X,H),'reduced/product dictionary mismatch')
    identity_checks=verify_difference_identity(c,z)
    native,nchecks=newton(c,z,y,last)
    # Only microscopic modes are directly summed. The complement uses the exact full identity.
    low,logc=spectral(freq,last)
    remainder=[e.ZERO]*(last+1)
    for k in range(X,last+1):remainder[k]=e.sub(e.rat(-native[k]),low[k])
    elow=energy(low,X,last);erem=energy(remainder,X,last);cmix=cross(low,remainder,X,last)
    actual=sum((native[k]**2 for k in range(X,last+1)),F())
    e.require(e.contains(e.add(e.add(elow,erem),cmix),actual),'full covariance identity')
    # Direct prime-power and a named semiprime subpacket; nothing inferred from their signs.
    pp={a:b for a,b in freq.items() if len(e.factors(a.denominator))==1}
    ppvals,pplog=spectral(pp,last)
    mixed=[e.sub(low[k],ppvals[k]) for k in range(last+1)]
    primes=[p for p in range(2,y+1) if 4*p>3*(y+1) and e.factors(p)==((p,1),)]
    sem={p*r for p in primes for r in primes if p<r}
    for q in sem:e.require(amps.get(q,F())==F(2,q),'native semiprime amplitude')
    sf={a:b for a,b in freq.items() if a.denominator in sem}
    sv,_=spectral(sf,last)
    other=[e.sub(low[k],sv[k]) for k in range(last+1)]
    es=energy(sv,X,last);eo=energy(other,X,last);cs=cross(sv,other,X,last)
    e.require(e.overlaps(e.add(e.add(es,eo),cs),elow),'semiprime covariance identity')
    inn=innovations(c);a=max(0,X//(2*H*L)-1)
    local=sum((v*v for v in inn[a+1:L]),F())
    a0=max(0,y//(8*H)-1)
    recent=sum((v*v for v in old[a0+1:]),F())
    tail=sum((v*v for v in inn[y+1:L]),F())
    e.require(tail<=sum((v*v for v in old[y//2+1:]),F()),'local completion price')
    e.require(local<=2*recent,'recent input domination')
    bound=F(2**21)*H**4*local**2
    e.require(elow[1]<e.rat(bound)[0],'microscopic energy upper budget')
    return {'y':y,'X':X,'last':last,'H':H,'L':L,'cells':last-X+1,
            'paired_frequencies':len(freq),'full_weight_frequencies':sum(1 for a in freq if X*a<=H),
            'transition_frequencies':sum(1 for a in freq if X*a>H),
            'native_energy':e.enc(e.rat(actual)),'micro_energy':e.enc(elow),
            'complement_energy':e.enc(erem),'twice_micro_complement':e.enc(cmix),
            'micro_prime_power_energy':e.enc(energy(ppvals,X,last)),
            'micro_mixed_energy':e.enc(energy(mixed,X,last)),
            'twice_micro_pp_mixed':e.enc(cross(ppvals,mixed,X,last)),
            'semiprime_primes':primes,'semiprime_denominators':len(sem),
            'semiprime_energy':e.enc(es),'other_micro_energy':e.enc(eo),'twice_semiprime_other_micro':e.enc(cs),
            'centering_constant':e.enc(logc),'pp_centering_constant':e.enc(pplog),
            'input_energy':encode_fraction(sum((v*v for v in inn),F())),
            'localized_input_energy':encode_fraction(local),'recent_native_energy':encode_fraction(recent),
            'explicit_upper_budget':encode_fraction(bound),'local_first_retained_index':a+1,
            'native_first_retained_index':a0+1,'newton_coefficient_checks':nchecks,
            'summation_by_parts_coefficient_checks':identity_checks,
            'complement_method':'exact full native identity minus directly summed microscopic component',
            'frequency_dictionary_sha256':sha256(canonical([[encode_fraction(a),encode_fraction(b)] for a,b in sorted(freq.items())])).hexdigest()}

def canonical(obj: object) -> bytes:
    return (json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=True)+'\n').encode()

def reject_duplicates(pairs: list) -> dict:
    out={}
    for k,v in pairs:e.require(k not in out,'duplicate key');out[k]=v
    return out

def strict_equal(a: object,b: object) -> bool:
    if type(a) is not type(b):return False
    if isinstance(a,dict):return a.keys()==b.keys() and all(strict_equal(a[k],b[k]) for k in a)
    if isinstance(a,list):return len(a)==len(b) and all(strict_equal(x,y) for x,y in zip(a,b))
    return a==b

def global_campaign(Y: int,H: int,cache: dict) -> dict:
    e.require(Y>=7 and Y+1>=8*H,'global source/band hypothesis')
    X=Y+1;last=(Y+1)**2-1;panels=[]
    while X<=last:
        hi=min(2*X-1,last);y=isqrt(hi);key=(y,H,X,hi)
        if key not in cache:cache[key]=panel(y,H,X,hi)
        panels.append(cache[key]);X*=2
    _,old=completion(Y);fy=sum((x*x for x in old),F())
    rec=[F(*map(int,p['recent_native_energy'])) for p in panels]
    overlap=12+2*(H-1).bit_length()
    e.require(sum(rec,F())<=overlap*fy,'native recent-energy overlap bound')
    total={name:e.enc(e.sumiv((int(p[name]['lo']),int(p[name]['hi'])) for p in panels)) for name in
           ('native_energy','micro_energy','complement_energy','twice_micro_complement','micro_prime_power_energy','micro_mixed_energy','twice_micro_pp_mixed')}
    budget=2**23*H**4*overlap*fy*max(rec)
    e.require(int(total['micro_energy']['hi'])<e.rat(budget)[0],'whole-step coherent-band bound')
    return {'Y':Y,'B':last,'H':H,'panels':panels,'totals':total,
            'F_Y':encode_fraction(fy),'maximum_recent_energy':encode_fraction(max(rec)),
            'sum_recent_energies':encode_fraction(sum(rec,F())),'overlap_budget':overlap,
            'linear_times_recent_upper_budget':encode_fraction(budget),
            'complete_new_cells':last-Y}

def produce(quick: bool=False) -> dict:
    cache={}
    if quick:
        focus=[panel(7,1)];campaigns=[]
    else:
        campaigns=[global_campaign(15,1,cache),global_campaign(31,1,cache)]
        focus=[panel(31,2)]
    executed=list(cache.values())+focus
    return {'packet':'MCB31','schema':1,'arithmetic':'integers/Fraction and credited NCL29 144-bit outward real arithmetic',
            'unbounded_theorem_checked_by_code':False,'RH_proved':False,'quick':quick,
            'source_files':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in ('check.py','exact.py')},
            'campaigns':campaigns,'focused_panels':focus,
            'unique_block_evaluations':len(executed),
            'evaluated_cells_including_overlap':sum(p['cells'] for p in executed),
            'newton_checks_including_overlap':sum(p['newton_coefficient_checks'] for p in executed)}

def validate(path: Path,actual: dict) -> None:
    e.require(path.is_file() and not path.is_symlink(),'report must be a regular nonsymlink file')
    expected=json.loads(path.read_text(),object_pairs_hook=reject_duplicates)
    e.require(strict_equal(expected,actual),'report differs from reconstructed mathematics')

def receipt(actual: dict) -> dict:
    return {'packet':'MCB31','receipt_schema':1,'full_report_sha256':sha256(canonical(actual)).hexdigest(),
            'arithmetic':actual['arithmetic'],'quick':actual['quick'],
            'source_files':actual['source_files'],
            'coverage':{k:actual[k] for k in ('unique_block_evaluations','evaluated_cells_including_overlap','newton_checks_including_overlap')},
            'campaigns':[{'Y':p['Y'],'B':p['B'],'H':p['H'],'complete_new_cells':p['complete_new_cells'],'totals':p['totals']} for p in actual['campaigns']],
            'focused_panels':[{k:p[k] for k in ('y','X','last','H','native_energy','micro_energy','complement_energy','twice_micro_complement')} for p in actual['focused_panels']],
            'RH_proved':False,'unbounded_theorem_checked_by_code':False}

def validate_receipt(path: Path,actual: dict) -> None:
    e.require(path.is_file() and not path.is_symlink(),'receipt must be a regular nonsymlink file')
    expected=json.loads(path.read_text(),object_pairs_hook=reject_duplicates)
    e.require(strict_equal(expected,receipt(actual)),'receipt differs from complete reconstruction')

def main() -> None:
    ap=argparse.ArgumentParser();ap.add_argument('--write',type=Path);ap.add_argument('--check',type=Path);ap.add_argument('--quick',action='store_true');ap.add_argument('--write-receipt',type=Path);ap.add_argument('--check-receipt',type=Path)
    args=ap.parse_args();result=produce(args.quick)
    if args.write:args.write.write_bytes(canonical(result))
    if args.check:validate(args.check,result)
    if args.write_receipt:args.write_receipt.write_bytes(canonical(receipt(result)))
    if args.check_receipt:validate_receipt(args.check_receipt,result)
    print('MCB31 PASS',sha256(canonical(result)).hexdigest())

if __name__=='__main__':main()
