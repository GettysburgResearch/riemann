#!/usr/bin/env python3
"""MHB32 bounded algebra and native covariance checks; not infinite proof verification."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import exact as e
import inherited_mcb as m

ROOT = Path(__file__).resolve().parent
INHERITED = {
    'exact.py': '68a70dfd171a9cd66b2815197d7ad81c16c466bf96cbc981a7dad557d30c450c',
    'inherited_mcb.py': 'cb605c06a8b299770d618014a748071623b84d137a8ede2b833b9c9d14d006fe',
}
THETA = F(27,164)
BAND_EXPONENT = 2 + 2*THETA
OUTPUT_EXPONENT = BAND_EXPONENT/(BAND_EXPONENT+1)
INPUT_EXPONENT = 2/(BAND_EXPONENT+1)

def authenticate() -> None:
    for name, expected in INHERITED.items():
        p = ROOT/name
        e.require(not p.is_symlink(), 'inherited source symlink')
        e.require(sha256(p.read_bytes()).hexdigest()==expected, 'inherited source identity')

def root_floor(n: int, degree: int) -> int:
    e.require(type(n) is int and n>=0 and type(degree) is int and degree>=1, 'integer root domain')
    if n<2:return n
    lo,hi=0,1<<((n.bit_length()+degree-1)//degree)
    while hi-lo>1:
        mid=(hi+lo)//2
        if mid**degree<=n:lo=mid
        else:hi=mid
    return lo

def power_upper(H: int) -> F:
    """A 64-fractional-bit outward rational bound for H**(191/82)."""
    e.require(type(H) is int and H>=1, 'bandwidth domain')
    n=(H**191)<<(64*82)
    low=root_floor(n,82)
    return F(low+(low**82!=n),1<<64)

def poly_f(d: int, X: int) -> F:
    e.require(type(d) is int and d>=0 and type(X) is int and X>=1, 'polynomial fixture domain')
    if d==0:return F()
    return sum(((1-F(j*X,d))**4 for j in range(1,d//X+1)),F())

def polynomial_fixture(c: list[F], X: int) -> dict:
    """g(t)=(1-t)^4_+, integral 1/5; all finite identities are rational."""
    x=m.innovations(c);L=len(c)-1;A=F(1,5)
    f=[poly_f(d,X) for d in range(L*L+1)]
    centered=[f[d]-A*d/X for d in range(L*L+1)]
    def source_form(values: list[F]) -> F:
        return sum((c[r]*c[s]*values[r*s]/(r*s) for r in range(1,L+1) for s in range(1,L+1)),F())
    def differences(values: list[F]) -> F:
        return sum((x[r]*x[s]*(values[r*s]-values[(r+1)*s]-values[r*(s+1)]+values[(r+1)*(s+1)])
                    for r in range(1,L) for s in range(1,L)),F())
    raw=source_form(f); rem=source_form(centered)
    total=sum(c,F()); rank=A*total**2/X
    e.require(raw==differences(f) and rem==differences(centered),'finite Hankel/source disagreement')
    e.require(raw==rank+rem,'rank-one subtraction lost')
    e.require(sum(x,F())==-total,'reciprocal-balance/total identity')
    return {'X':X,'source':[e.frac(t) for t in c], 'raw':e.frac(raw),
            'centered':e.frac(rem),'rank_one':e.frac(rank),'source_total':e.frac(total)}

def source_from_innovations(x: list[F]) -> list[F]:
    e.require(x and x[0]==0 and x[-1]==0,'innovation endpoints')
    return [F()]+[n*(x[n]-x[n-1]) for n in range(1,len(x))]

def algebra_report() -> dict:
    e.require(BAND_EXPONENT==F(191,82),'band exponent')
    e.require(OUTPUT_EXPONENT==F(191,273) and INPUT_EXPONENT==F(164,273),'optimized exponents')
    e.require(OUTPUT_EXPONENT+INPUT_EXPONENT/2==1,'critical fixed-point exponent')
    fixtures=[]
    for L in range(2,10):
        for seed in range(5):
            x=[F()]+[F(((r+seed)**2%7)-3,seed+1) for r in range(1,L)]+[F()]
            c=source_from_innovations(x)
            for X in (1,2,5):fixtures.append(polynomial_fixture(c,X))
    decisive=polynomial_fixture([F(),F(1),F(-2)],1)
    e.require(F(*map(int,decisive['raw']))==F(33,128),'exact raw polynomial control')
    e.require(F(*map(int,decisive['centered']))==F(37,640),'exact centered polynomial control')
    e.require(F(*map(int,decisive['rank_one']))==F(1,5),'nonzero rank-one control')
    for H in range(1,33):
        upper=power_upper(H)
        e.require(upper**82>=H**191 and (upper-F(1,1<<64))**82<H**191,'outward fractional power')
    return {'polynomial_fixtures':len(fixtures), 'fixture_sha256':sha256(m.canonical(fixtures)).hexdigest(),
            'nonzero_rank_control':decisive,'band_exponent':e.frac(BAND_EXPONENT),
            'full_block_X_exponent':e.frac(OUTPUT_EXPONENT),'full_block_F_exponent':e.frac(INPUT_EXPONENT),
            'critical_fixed_point':e.frac(OUTPUT_EXPONENT+INPUT_EXPONENT/2),'outward_power_controls':32}

def spectral_stable(freq: dict[F,F], last: int) -> tuple[list[e.IV],e.IV]:
    """Outward rotations, reseeded from exact rational phases every 32 steps.

    The unmodified inherited routine is retained for comparison. Its valid
    enclosures become very wide at larger angles; that is not a wrong value.
    """
    deriv=[e.ZERO]*(last+1);constant=e.ZERO
    for alpha,b in sorted(freq.items()):
        a,q=alpha.numerator,alpha.denominator
        e.require(0<2*a<q,'paired phase domain')
        co=e.cos_fraction(a,q);si=e.cos_fraction(q-4*a,4*q)
        constant=e.add(constant,e.scale(e.log_sine(a,q),2*b))
        cn,sn=e.ONE,e.ZERO
        for k in range(1,last+1):
            cn,sn=e.sub(e.mul(cn,co),e.mul(sn,si)),e.add(e.mul(sn,co),e.mul(cn,si))
            if k%32==0 or k==last:
                dc=e.cos_fraction(k*a,q);ds=e.cos_fraction(q-4*k*a,4*q)
                e.require(e.overlaps(cn,dc) and e.overlaps(sn,ds),'reseed/rotation disagreement')
                cn=(max(cn[0],dc[0]),min(cn[1],dc[1]))
                sn=(max(sn[0],ds[0]),min(sn[1],ds[1]))
            deriv[k]=e.add(deriv[k],e.scale(cn,2*b))
    acc=constant;out=[acc]
    for k in range(1,last+1):
        acc=e.add(acc,e.divint(deriv[k],k));out.append(acc)
    return out,constant

def native_ladder(y: int, X: int, last: int, bands: list[int]) -> dict:
    e.require(type(y) is int and type(X) is int and type(last) is int, 'integer native endpoints')
    e.require(bands and bands==sorted(set(bands)) and all(type(h) is int and h>=1 for h in bands),'ordered bandwidths')
    e.require(X<=last<2*X and last<(y+1)**2 and X>=8*max(bands),'native observation/band hypotheses')
    c,old=m.completion(y);L=len(c)-1
    e.require(L<=X and L*L<=8*X,'short source hypotheses')
    z,amps=m.source(c)
    native,nchecks=m.newton(c,z,y,last)
    nvals=[e.rat(v) for v in native]
    frequency_maps=[m.frequency_map(amps,X,H) for H in bands]
    for H, fm in zip(bands,frequency_maps):
        e.require(fm==m.product_frequency_map(c,X,H),'reduced/product frequency identity')
    # Difference the exact rational weights first; each shell has its own direct evaluation.
    shell_maps=[];previous={}
    for fm in frequency_maps:
        shell_maps.append({a:fm.get(a,F())-previous.get(a,F()) for a in fm.keys()|previous.keys()
                           if fm.get(a,F())!=previous.get(a,F())})
        previous=fm
    shells=[spectral_stable(fm,last)[0] for fm in shell_maps]
    cumulative=[]; running=[e.ZERO]*(last+1)
    for sh in shells:
        running=[e.add(a,b) for a,b in zip(running,sh)]
        cumulative.append(running)
    direct,direct_log=spectral_stable(frequency_maps[-1],last)
    for k in range(X,last+1):e.require(e.overlaps(direct[k],cumulative[-1][k]),'shell/direct spectral disagreement')
    complement=[e.sub(e.neg(nvals[k]),cumulative[-1][k]) for k in range(last+1)]
    components=shells+[complement]
    labels=[f'U_{bands[0]}']+[f'U_{bands[j]}-U_{bands[j-1]}' for j in range(1,len(bands))]+[f'complement_to_U_{bands[-1]}']
    diagonal=[m.energy(v,X,last) for v in components]
    crosses=[]; total=e.sumiv(diagonal)
    for i in range(len(components)):
        for j in range(i+1,len(components)):
            value=m.cross(components[i],components[j],X,last)
            crosses.append({'i':i,'j':j,'twice_covariance':e.enc(value)})
            total=e.add(total,value)
    truth=sum((native[k]**2 for k in range(X,last+1)),F())
    e.require(e.contains(total,truth),'complete shell covariance identity')
    x=m.innovations(c);panels=[]
    for H,fm,vals in zip(bands,frequency_maps,cumulative):
        a=max(0,X//(2*H*L)-1)
        local=sum((t*t for t in x[a+1:L]),F())
        first=max(0,y//(8*H)-1)
        recent=sum((t*t for t in old[first+1:]),F())
        e.require(local<=2*recent,'native recent energy price')
        eh=m.energy(vals,X,last)
        new_upper=2**60*power_upper(H)*local**2
        new_lower=2**60*(power_upper(H)-F(1,1<<64))*local**2
        old_upper=2**21*H**4*local**2
        e.require(eh[1]<=e.rat(new_lower)[0] and eh[1]<=e.rat(old_upper)[0],'finite sector bound')
        remainder=[e.sub(e.neg(nvals[k]),vals[k]) for k in range(last+1)]
        cross=m.cross(vals,remainder,X,last)
        panels.append({'H':H,'paired_frequencies':len(fm),'micro_energy':e.enc(eh),
                       'complement_energy':e.enc(m.energy(remainder,X,last)),
                       'twice_covariance':e.enc(cross),'local_input_energy':e.frac(local),
                       'recent_native_energy':e.frac(recent),'new_bound_rational_upper':e.frac(new_upper),
                       'old_bound':e.frac(old_upper)})
    # An independently derived coefficient identity, not a check only of sums of energies.
    diff_checks=m.verify_difference_identity(c,z)
    return {'y':y,'X':X,'last':last,'L':L,'cells':last-X+1,'bandwidths':bands,
            'native_energy':e.enc(e.rat(truth)), 'F_y':e.frac(sum((t*t for t in old),F())),
            'source_total':e.frac(sum(c,F())), 'newton_checks':nchecks,'difference_coefficient_checks':diff_checks,
            'panels':panels,'component_labels':labels,'component_energies':[e.enc(t) for t in diagonal],
            'all_pairwise_cross_terms':crosses,'reconstructed_full_energy':e.enc(total),
            'largest_band_centering_constant':e.enc(direct_log),
            'complement_method':'exact native full identity minus directly evaluated smooth spectral bands',
            'frequency_map_sha256':sha256(m.canonical([[[e.frac(a),e.frac(b)] for a,b in sorted(fm.items())]
                                                      for fm in frequency_maps])).hexdigest()}

def produce(quick: bool=False) -> dict:
    authenticate()
    cases=[native_ladder(7,32,63,[1,2])] if quick else [native_ladder(15,128,255,[1,2,4]),native_ladder(31,512,1023,[1,2,4,8])]
    return {'packet':'MHB32','schema':1,'RH_proved':False,'infinite_proof_verified_by_code':False,
            'arithmetic':'exact Fraction source and inherited 144-bit outward elementary arithmetic',
            'quick':quick,'algebra':algebra_report(),'native_blocks':cases,
            'native_coverage':{'cells':sum(p['cells'] for p in cases),'coefficient_checks_counting_overlap':sum(p['newton_checks'] for p in cases),
                               'maximum_native_endpoint':max(p['last'] for p in cases)},
            'source_sha256':{name:sha256((ROOT/name).read_bytes()).hexdigest() for name in ['check.py','exact.py','inherited_mcb.py']}}

def load(path: Path) -> object:
    e.require(not path.is_symlink(),'report symlink')
    return json.loads(path.read_text(),object_pairs_hook=m.reject_duplicates)

def check(path: Path, actual: dict) -> None:
    e.require(m.strict_equal(load(path),actual),'canonical typed result mismatch')

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--quick',action='store_true')
    parser.add_argument('--write',type=Path)
    parser.add_argument('--check',type=Path)
    args=parser.parse_args()
    actual=produce(args.quick)
    if args.check:check(args.check,actual)
    if args.write:args.write.write_bytes(m.canonical(actual))
    print('MHB32 PASS '+sha256(m.canonical(actual)).hexdigest())

if __name__=='__main__':main()
