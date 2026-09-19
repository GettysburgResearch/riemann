#!/usr/bin/env python3
"""Exact finite NSR26 replay. Standard library only; no zeta or float oracle.

The infinite family theorem is a written analytic proof, not proved by this
program. The supplied ternary word is the authoritative finite primitive.
"""
from __future__ import annotations
import argparse
import base64
import hashlib
import json
import math
from pathlib import Path
from fractions import Fraction as F
import zlib

ROOT = Path(__file__).resolve().parent
SOURCE_SHA256 = '6f277d7d6d8c2adff9d37b59c759af174f8b2befdfc1fd2ed2a7460802d3b610'
BITS = 96
SCALE = 1 << BITS
MAX_Y = 1023
ALPHA = {1: 1, 2: -1, 3: -1, 5: -1, 6: -1, 10: 1, 15: 1, 30: 1}


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def unique_pairs(pairs):
    out = {}
    for key, value in pairs:
        need(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def canonical(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode()


def interval_text(lo: F, hi: F, places: int = 12) -> list[str]:
    need(lo <= hi, 'reversed interval')
    q = 10**places
    a = lo.numerator*q//lo.denominator
    b = -((-hi.numerator*q)//hi.denominator)
    def show(n):
        sign = '-' if n < 0 else ''
        n = abs(n)
        return f'{sign}{n//q}.{n%q:0{places}d}'
    return [show(a), show(b)]


def square_interval(lo: F, hi: F) -> tuple[F, F]:
    return (F(0) if lo <= 0 <= hi else min(lo*lo, hi*hi), max(lo*lo, hi*hi))


def read_source() -> dict:
    raw = (ROOT/'counterexample.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest() == SOURCE_SHA256, 'primitive source SHA mismatch')
    return json.loads(raw, object_pairs_hook=unique_pairs)


def audit_source(d: dict):
    for key in ('R', 'Y', 'start', 'X0', 'X1', 'bins', 'word_length'):
        need(type(d[key]) is int, 'integer metadata required')
    need(d['kind'] == 'ternary-cumulative-rounding-v1', 'source kind')
    need(d['word_codec'] == 'zlib-base64-ascii', 'source codec')
    need(0 < d['word_length'] <= 100000 and 1 <= d['bins'] <= 8192, 'resource bounds')
    packed = base64.b64decode(d['word_zlib_b64'], validate=True)
    dec = zlib.decompressobj()
    raw = dec.decompress(packed, d['word_length']+1)
    need(dec.eof and not dec.unused_data and not dec.unconsumed_tail, 'compressed source boundary')
    need(len(raw) == d['word_length'], 'word length')
    word = raw.decode('ascii')
    need(set(word) <= set('+-0'), 'ternary alphabet')
    a = d['start']; b = a+len(word)-1
    need(30 < a <= b < d['Y']+1, 'source support')
    need(d['Y'] == 2*d['R'], 'declared cutoff')
    need(d['alpha'] == [[k,v] for k,v in ALPHA.items()], 'baseline identity')
    need(sum(ALPHA.values()) == 0 and sum(F(v,k) for k,v in ALPHA.items()) == 0, 'baseline moments')
    running=0; baseline_energy=F(0)
    for k in range(1,31):
        running+=ALPHA.get(k,0);baseline_energy+=F(running*running,k*(k+1))
    need(baseline_energy == F(23,15), 'baseline energy')
    c = [{'+': 1, '-': -1, '0': 0}[ch] for ch in word]
    C=[]; acc=0
    for z in c:
        acc += z; C.append(acc)
    need(acc == 0, 'nonzero total prefix')
    x0=d['X0']; x1=d['X1']; cutoff=d['Y']+1
    need(2*cutoff < x0 < x1 <= cutoff*cutoff, 'output window')
    need(x1 < 2*a*a and x1 < cutoff*a, 'unpaid product/cofactor sector')
    return a,b,c,C


def model_report(d: dict) -> dict:
    a,b,c,C = audit_source(d)
    nc=len(c); cutoff=d['Y']+1
    # All these sums use integer directed rounding, including signed means.
    ul=el=bl=0
    L=sum(abs(z) for z in c)
    for n,z,cur in zip(range(a,b+1),c,C):
        den=n*(n+1)
        ul += cur*SCALE//den
        el += cur*cur*SCALE//den
        if z: bl += SCALE//n+1
    ulo=F(ul,SCALE); uhi=F(ul+nc,SCALE)
    ua=max(abs(ulo),abs(uhi)); tailcap=2*cutoff*ua
    need(tailcap <= 1, 'canonical completion coefficient cap')
    Ahi=F(23,15)+F(el+nc,SCALE)+2*cutoff*ua*ua
    Alo=F(23,15)+F(el,SCALE)+2*cutoff*square_interval(ulo,uhi)[0]
    Bhi=F(bl,SCALE)
    x0=d['X0']; x1=d['X1']; bins=d['bins']
    lower=0; active=0; digest=hashlib.sha256(); peak=0
    # Canonical completion has total variation 4*cutoff*|u|.
    # The fixed baseline has l1 norm 8. All its interactions are paid.
    constant=9*L+32+32*cutoff*ua
    for j in range(bins):
        left=x0+(x1-x0)*j//bins
        right=x0+(x1-x0)*(j+1)//bins
        mid=(left+right)//2
        # First exact implementation: ordered product fibers.
        W=0
        r0=max(a,mid//(b+1)+1); r1=min(b,mid//a)
        for r in range(r0,r1+1):
            W += c[r-a]*C[mid//r-a]
        # Second exact implementation: hyperbola split and square correction.
        root=math.isqrt(mid); half=0
        for r in range(a,min(b,root)+1):
            q=mid//r
            if a <= q <= b: half += c[r-a]*C[q-a]
        corner=0 if root<a or root>b else C[root-a]
        W2=2*half-corner*corner
        need(W == W2, 'independent product-fiber mismatch')
        distance=max(mid-left,right-mid)
        z=max(F(0),abs(W)-distance*Bhi-constant)
        term=z*z*F(right-left,left*right)
        lower += term.numerator*SCALE//term.denominator
        active += int(z>0); peak=max(peak,abs(W))
        digest.update(f'{left} {right} {mid} {W}\n'.encode())
    lower=F(lower,SCALE)
    need((1+lower)**2 > 4*(1+Ahi)**3, 'advertised generic gain not refuted')
    need(Ahi < F(163,100) and lower > F(15732,1000), 'advertised rational margins')
    return {
        'status':'EXACT_FINITE_NON_MOBIUS_COUNTEREXAMPLE',
        'Y':d['Y'],'B':cutoff*cutoff-1,'support':[a,b],
        'ternary_prefix_entries':d['Y'],'nonzero_wave_entries':L,
        'native_initial_coefficients_matched':5,
        'input_A':interval_text(Alo,Ahi),
        'prefix_u':interval_text(ulo,uhi,18),
        'completion_abs_coefficient_upper':interval_text(tailcap,tailcap,15)[1],
        'output_energy_lower':interval_text(lower,lower,12)[0],
        'output_window':[x0,x1],'covered_intervals':bins,
        'positive_lower_intervals':active,'exact_midpoint_peak':peak,
        'midpoint_sha256':digest.hexdigest(),
        'G_refuted_on_this_nonnative_source':True,
        'native_G_refuted':False,
    }


def mobius_linear(n: int) -> list[int]:
    least=[0]*(n+1); mu=[0]*(n+1); mu[1]=1; primes=[]
    for k in range(2,n+1):
        if not least[k]: least[k]=k; primes.append(k); mu[k]=-1
        for p in primes:
            q=k*p
            if q>n: break
            least[q]=p
            if k%p==0: mu[q]=0; break
            mu[q]=-mu[k]
    return mu


def mobius_square_sieve(n: int) -> list[int]:
    prime=bytearray(b'\1')*(n+1); prime[0]=prime[1]=0
    mu=[1]*(n+1); mu[0]=0
    for p in range(2,n+1):
        if prime[p]:
            for k in range(p,n+1,p): mu[k]=-mu[k]
            if p*p<=n:
                for k in range(p*p,n+1,p): prime[k]=0
                for k in range(p*p,n+1,p*p): mu[k]=0
    return mu


def energy_table(mu: list[int], keys: set[int]):
    out={}; M=ul=el=0
    for k in range(1,max(keys)+1):
        M+=mu[k];den=k*(k+1)
        ul+=M*SCALE//den;el+=M*M*SCALE//den
        if k in keys:
            us=(F(ul,SCALE),F(ul+k,SCALE)); es=(F(el,SCALE),F(el+k,SCALE))
            sq=square_interval(*us)
            out[k]={'E':es,'u':us,'A':(es[0]+2*(k+1)*sq[0],es[1]+2*(k+1)*sq[1]),'M':M}
    return out


def divisor_first(mu: list[int], Y: int):
    b=Y+1; B=b*b-1; e=[0]*(B+1); e[1]=1
    for r in range(1,Y+1):
        if mu[r]:
            for n in range(r,B+1,r): e[n]-=mu[r]
    need(not any(e[:b]), 'native divisor inverse was not used')
    v=[0]*(B+1); v[1:Y+1]=mu[1:Y+1]
    for r in range(1,Y+1):
        if mu[r]:
            for s in range(b,B//r+1): v[r*s]+=mu[r]*e[s]
    need(v == mu[:B+1], 'Newton native prefix mismatch')
    return e


def bank_report(mu: list[int], e: list[int], Y: int) -> list[dict]:
    b=Y+1;B=b*b-1; Ee=[]; acc=0
    for z in e: acc+=z;Ee.append(acc)
    M=[];acc=0
    for z in mu[:B+1]:acc+=z;M.append(acc)
    width=B-b+1; exact_total=M[b:B+1]
    il=sum(z*z*SCALE//(n*(n+1)) for n,z in zip(range(b,B+1),exact_total))
    I=(F(il,SCALE),F(il+width,SCALE));reports=[]
    for P in (1,6,30,210):
        divisors=[d for d in range(1,P+1) if P%d==0]
        h=[sum(mu[d]*Ee[k//d] for d in divisors) for k in range(B+1)]
        rows=[[M[Y]]*width]
        for j in range(Y.bit_length()):
            v=[0]*width
            for r in range(1<<j,min(Y+1,2<<j)):
                if mu[r] and math.gcd(r,P)==1:
                    for i,x in enumerate(range(b,B+1)): v[i]+=mu[r]*h[x//r]
            rows.append(v)
        need(all(sum(row[i] for row in rows)==exact_total[i] for i in range(width)), 'prime-bank reconstruction')
        diag=0
        for i,n in enumerate(range(b,B+1)):
            diag+=sum(row[i]**2 for row in rows)*SCALE//(n*(n+1))
        D=(F(diag,SCALE),F(diag+width,SCALE))
        reports.append({'P':P,'rows':len(rows),'full_I':interval_text(*I),
                        'separate_row_energy':interval_text(*D),
                        'Cauchy_upper':interval_text(len(rows)*D[1],len(rows)*D[1])[1],
                        'signed_cross':interval_text(I[0]-D[1],I[1]-D[0]),
                        'all_integer_output_cells_equal':width})
    return reports


def native_report() -> dict:
    n=(MAX_Y+1)**2-1
    mu=mobius_linear(n); independent=mobius_square_sieve(n)
    need(mu==independent, 'independent Mobius sieve disagreement')
    keys=set(range(1,MAX_Y+1)) | {(y+1)**2-1 for y in range(1,MAX_Y+1)}
    table=energy_table(mu,keys)
    worst=F(0);worst_y=None
    for y in range(1,MAX_Y+1):
        ratio=(1+table[(y+1)**2-1]['A'][1])**2/(4*(1+table[y]['A'][0])**3)
        need(ratio <= 1, 'native finite gain failed')
        if ratio>worst:worst=ratio;worst_y=y
    reconstructed=0;e255=None;ys=(1,3,15,63,255,1023)
    for y in ys:
        e=divisor_first(mu,y);reconstructed+=len(e)-1
        if y==255:e255=e
    panels=[]
    for y in ys:
        z=(y+1)**2-1
        panels.append({'Y':y,'B':z,'input_A':interval_text(*table[y]['A']),
                       'output_A':interval_text(*table[z]['A']),
                       'input_u':interval_text(*table[y]['u'],15),
                       'output_u':interval_text(*table[z]['u'],15)})
    need(e255 is not None,'missing bank primitive')
    return {'status':'EXACT_FINITE_NATIVE_CONTROLS_NOT_ASYMPTOTICS',
            'max_output_integer':n,'two_sieve_comparisons':n,
            'gain_cutoffs':[1,MAX_Y],'gain_predicates':MAX_Y,
            'squared_gain_ratio_upper':interval_text(worst,worst,15)[1],
            'worst_cutoff':worst_y,'Newton_cutoffs':list(ys),
            'Newton_coefficients_compared':reconstructed,
            'panels':panels,'prime_bank_Y':255,
            'prime_banks':bank_report(mu,e255,255)}


def report() -> dict:
    return {'schema':1,'packet':'NSR26','source_sha256':SOURCE_SHA256,
            'arithmetic':'Python integers and Fraction; 96-bit directed rational sums',
            'model':model_report(read_source()),'native':native_report(),
            'infinite_theorem_checked_by_code':False,'RH_proved':False}


def check_result(path: Path, actual: dict) -> None:
    saved=json.loads(path.read_bytes(),object_pairs_hook=unique_pairs)
    need(canonical(saved)==canonical(actual),'result does not match complete reconstruction')


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--write',type=Path)
    group.add_argument('--check',type=Path)
    args=parser.parse_args(); actual=report()
    if args.write:args.write.write_bytes(json.dumps(actual,indent=2,sort_keys=True).encode()+b'\n')
    else:check_result(args.check,actual)
    print('PASS NSR26',hashlib.sha256(canonical(actual)).hexdigest())


if __name__=='__main__':
    try:main()
    except (ValueError,KeyError,TypeError,OSError,UnicodeError,zlib.error) as exc:
        raise SystemExit(f'REJECT: {exc}')
