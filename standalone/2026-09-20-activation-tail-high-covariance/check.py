#!/usr/bin/env python3
"""ATC29: exact finite tests of tail cancellation and native semiprime packets.

Uses an authenticated byte-for-byte copy of the NCG28 arithmetic implementation.
This checks finite algebra/enclosures, not the written asymptotic theorems.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parent
PRIMITIVE_SHA256 = '05900fe68163fe06c7fe3d3df14ebd84b4ee280d204296ee02568bea5fcc2b64'

def load_primitives(path: Path):
    if path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != PRIMITIVE_SHA256:
        raise ValueError('NCG28 primitive source identity differs')
    spec = importlib.util.spec_from_file_location('atc29_ncg28', path)
    if spec is None or spec.loader is None:
        raise ValueError('cannot load authenticated primitives')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

n = load_primitives(ROOT / 'ncg28_primitives.py')
Z = n.ZERO


def integer_scale(a, k: int):
    return (a[0]*k, a[1]*k) if k >= 0 else (a[1]*k, a[0]*k)


def divide(a, k: int):
    n.require(type(k) is int and k > 0, 'positive integral divisor required')
    return a[0] // k, -((-a[1]) // k)


def fraction_iv(a: int, b: int = 1):
    return divide((a*n.SCALE, a*n.SCALE), b)


def abs_upper(a):
    return F(max(abs(a[0]), abs(a[1])), n.SCALE)


def sign(a):
    return 'positive' if a[0] > 0 else 'negative' if a[1] < 0 else 'unresolved'


def period_checks(limit: int = 48):
    cases = 0
    tail_cases = 0
    for q in range(2, limit+1):
        rv = [n.R(q, k) for k in range(q)]
        n.require(sum(rv, F()) == 0, 'period mean')
        n.require(sum((r*r for r in rv), F()) == F(q*n.jordan2(q), 12), 'period variance')
        # Every possible starting residue and partial period.
        for start in range(q):
            acc = F()
            for length in range(1, q+1):
                acc += rv[(start+length-1) % q]
                n.require(abs(acc) <= F(q*q, 2), 'period partial-sum envelope')
                cases += 1
        for K in [1, 2, 5, 17, 64, 5*q+1]:
            H, _ = n.harmonics(K-1, set())
            p = n.pp_base(q)
            z = n.sumiv([n.times(H[(K-1)//d], n.mobius_trial(q//d))
                         for d in n.divisors(q)] + ([n.log_iv(p)] if p else []))
            a = n.sub(n.rational(n.R(q,K-1)/K), z)
            n.require(abs_upper(a) <= F(q*q, 2*K*(K+1)), 'complete periodic-tail bound')
            tail_cases += 1
    # Constants in the dyadic majorant calculations; no rounded powers.
    n.require(5632**2 * 8 * 7 * 4 < 2**34, 'native constant')
    n.require(12**2 * 11 * 3 < 2**13, 'generic constant')
    n.require(2**5 * 3**11 > 4**11, 'geometric sum < 4')
    n.require(2**9 * 2**11 > 3**11, 'geometric sum < 3')
    n.require(2**4 * 4**11 > 5**11, 'geometric sum < 5')
    return {'periods': limit-1, 'cyclic_partial_sums': cases, 'full_tail_cases': tail_cases}


def complete_panel(Y: int):
    n.require(type(Y) is int and 31 <= Y <= 127, 'complete panel range 31..127')
    c, F0 = n.completion(Y)
    amps, U, zz, D = n.amplitudes(c)
    L, b, last = len(c)-1, Y+1, 5*Y//4
    Q = n.root(Y**4*b**6, 11)
    composites = {q for q in amps if not n.prime(q)}
    primes = set(amps)-composites
    activation = {}
    for q in composites:
        X = b
        while q**11 > Y**4 * X**6:
            X *= 2
        activation[q] = X
    extra = {K-1 for K in activation.values()}
    extra |= {(activation[q]-1)//d for q in composites for d in n.divisors(q)}
    H0, H1 = n.harmonics(last, extra)
    def H(k): return H0[k] if k <= last else H1[k]
    def zq(q,k):
        p = n.pp_base(q)
        return n.sumiv([n.times(H(k//d), n.mobius_trial(q//d)) for d in n.divisors(q)]
                       + ([n.log_iv(p)] if p else []))
    tails = {}
    majorants = {}
    for q in composites:
        K = activation[q]
        tails[q] = n.sub(n.rational(n.R(q,K-1)/K), zq(q,K-1))
        majorants[q] = F(q*q, 2*K*(K+1))
        n.require(abs_upper(tails[q]) <= majorants[q], 'activation tail component')
    X, correction_energy, bound, blocks = b, Z, F(), []
    while X < max(activation.values(), default=b):
        inactive = {q for q in composites if activation[q] > X}
        correction = n.sumiv(n.times(tails[q],amps[q]) for q in inactive)
        cap = sum((abs(amps[q])*majorants[q] for q in inactive), F())
        n.require(abs_upper(correction) <= cap, 'signed correction envelope')
        correction_energy = n.add(correction_energy, integer_scale(n.square(correction), X))
        bound += X*cap*cap
        blocks.append({'X':X,'Q':min(L*L,n.root(Y**4*X**6,11)),
                       'inactive':len(inactive),'correction':n.enc(correction),
                       'absolute_tail_envelope':n.enc(n.rational(cap))})
        X *= 2
    n.require(F(correction_energy[1],n.SCALE) <= bound, 'whole infinite correction energy')
    n.require(blocks and not n.contains((int(blocks[0]['correction']['lower']),
                                       int(blocks[0]['correction']['upper'])),0),
              'nonzero correction control')
    # Exact integer Newton verification on EVERY cell used in this new panel.
    sums = [0]*(last+1)
    for d in range(1,min(last,len(zz)-1)+1):
        if zz[d]:
            for k in range(d,last+1,d): sums[k] += zz[d]
    mu = n.mobius_sieve(last)
    for k in range(1,last+1):
        v = (2*D*int(c[k]*D) if k < len(c) else 0)-sums[k]
        n.require(v == mu[k]*D*D, 'full local Newton coefficient')
        n.require(mu[k] == n.mobius_trial(k), 'trial/sieve native source')
    ps = [p for p in range(2,Y+1) if 4*p>3*(Y+1) and n.prime(p)]
    pair_q = {p*r for i,p in enumerate(ps) for r in ps[i+1:]}
    a = sum((F(1,p) for p in ps),F())**2-sum((F(1,p*p) for p in ps),F())
    n.require(pair_q and min(pair_q)>last and min(pair_q)>Q, 'semiprime high/support')
    for p in ps:
        n.require(2*p>L and U[p]==F(-1,p), 'isolated native prime coefficient')
    for q in pair_q: n.require(amps[q]==F(2,q), 'native semiprime coefficient')
    prim_spec = n.component_coefficients(amps,primes)
    low_spec = n.component_coefficients(amps,{q for q in composites if q<=Q})
    high_spec = n.component_coefficients(amps,{q for q in composites if q>Q})
    m, cm = Z, Z
    energy = {s:Z for s in ['total_Q','instantaneous_high','semiprime','other_high','twice_covariance']}
    direct_points = {b,(b+last)//2,last}
    rows=[]
    for k in range(1,last+1):
        m=n.add(m,fraction_iv(mu[k],k))
        if k<len(c): cm=n.add(cm,n.rational(c[k]/k))
        if k<b:continue
        Qall=n.sub(integer_scale(cm,2),m)
        pv=n.evaluate(*prim_spec,k,H)
        lv=n.evaluate(*low_spec,k,H)
        high=n.sub(n.sub(Qall,pv),lv)
        semi=n.times(n.sub(H(k),fraction_iv(2)),a)
        if k in direct_points:
            n.require(n.overlap(high,n.evaluate(*high_spec,k,H)), 'direct full high spectral check')
            explicit=n.sumiv(n.times(zq(q,k),amps[q]) for q in pair_q)
            n.require(n.overlap(semi,explicit),'semiprime rank-one identity')
        rest=n.sub(high,semi)
        for key,v in [('total_Q',Qall),('instantaneous_high',high),('semiprime',semi),('other_high',rest)]:
            energy[key]=n.add(energy[key],n.square(v))
        energy['twice_covariance']=n.add(energy['twice_covariance'],integer_scale(n.mul(semi,rest),2))
        rows.append((Qall,pv,lv,high,semi,rest))
    n.require(n.overlap(energy['instantaneous_high'],n.sumiv([energy['semiprime'],energy['other_high'],energy['twice_covariance']])), 'signed high covariance ledger')
    return {'Y':Y,'L':L,'b':b,'last':last,'native_cells':last-Y,'instantaneous_Q':Q,
            'seed_F':n.enc(n.rational(F0)), 'prime_band':ps,'semiprime_count':len(pair_q),
            'semiprime_amplitude':[str(a.numerator),str(a.denominator)],
            'energy':{k:n.enc(v) for k,v in energy.items()},
            'covariance_sign':sign(energy['twice_covariance']),
            'correction_entire_future_energy':n.enc(correction_energy),
            'correction_entire_future_finite_envelope':n.enc(n.rational(bound)),
            'correction_blocks':blocks,'zero_correction_from':X,
            'direct_high_spectral_points':sorted(direct_points),
            'rows_sha256':n.vector_hash(rows),
            'high_evaluation':'exact complement on every cell; independent full spectral sums at listed points',
            'future_mu_scope':'finite independent native reconstruction check only; amplitudes from prefix and completion'}


def large_band(Y: int):
    """Linear-range finite comparison with the FULL spectral complement, not just high modes."""
    n.require(type(Y) is int and 128<=Y<=131071,'large-band range')
    b,last=Y+1,5*Y//4
    mu=n.mobius_sieve(last)
    ps=[p for p in range(2,Y+1) if 4*p>3*(Y+1) and n.prime(p)]
    # A second sieve reconstructs the same seed via a smallest-prime recurrence.
    spf=list(range(last+1))
    for p in range(2,n.isqrt(last)+1):
        if spf[p]==p:
            for k in range(p*p,last+1,p):
                if spf[k]==k:spf[k]=p
    mu2=[0]*(last+1);mu2[1]=1
    for k in range(2,last+1):
        p=spf[k];r=k//p
        mu2[k]=0 if r%p==0 else -mu2[r]
    n.require(mu==mu2,'independent full local Mobius source')
    g=mu[:Y+1]
    prod=[0]*(last+1)
    for r in range(1,Y+1):
        if g[r]:
            for s in range(1,min(Y,last//r)+1):
                if g[s]:prod[r*s]+=g[r]*g[s]
    inv=[0]*(last+1)
    for d in range(1,last+1):
        if prod[d]:
            for k in range(d,last+1,d):inv[k]+=prod[d]
    for k in range(1,last+1):
        n.require(inv[k]==(2*g[k] if k<=Y else 0)-mu[k], 'source-first local Newton reconstruction')
    s1=n.sumiv(fraction_iv(1,p) for p in ps)
    s2=n.sumiv(fraction_iv(1,p*p) for p in ps)
    amp=n.sub(n.square(s1),s2)
    h,m,qg=Z,Z,Z
    seed_energy=Z
    energy={s:Z for s in ['semiprime','full_other_modes','twice_covariance','total_Q']}
    cm=Z;my=Z;sgn=0
    rows=[]
    for k in range(1,last+1):
        h=n.add(h,fraction_iv(1,k));m=n.add(m,fraction_iv(mu[k],k));qg=n.add(qg,fraction_iv(inv[k],k))
        if k<=Y:
            seed_energy=n.add(seed_energy,n.square(m))
            if k==Y:
                my,cm=m,m
                n.require(m[0]>0 or m[1]<0,'endpoint sign unresolved')
                sgn=1 if m[0]>0 else -1
            continue
        # The known-prefix capped reciprocal completion, outwardly enclosed.
        r=cm if sgn>0 else n.neg(cm)
        r=n.sub(r,fraction_iv(3,k));r=(max(0,r[0]),max(0,r[1]))
        cm=r if sgn>0 else n.neg(r)
        total=n.sub(integer_scale(cm,2),m)
        direct=n.add(qg,integer_scale(n.sub(cm,my),2))
        n.require(n.overlap(total,direct),'completion-restored harmonic source')
        total = direct  # Accept the short-source reconstruction, not the checking oracle.
        semi=n.mul(amp,n.sub(h,fraction_iv(2)))
        rest=n.sub(total,semi)
        for key,v in [('semiprime',semi),('full_other_modes',rest),('total_Q',total)]:
            energy[key]=n.add(energy[key],n.square(v))
        energy['twice_covariance']=n.add(energy['twice_covariance'],integer_scale(n.mul(semi,rest),2))
        rows.append((total,semi,rest))
    n.require(n.overlap(energy['total_Q'],n.sumiv([energy['semiprime'],energy['full_other_modes'],energy['twice_covariance']])), 'large full-complement covariance')
    return {'Y':Y,'b':b,'last':last,'native_cells':last-Y,'prime_count':len(ps),
            'semiprime_count':len(ps)*(len(ps)-1)//2,'seed_F':n.enc(seed_energy),
            'amplitude':n.enc(amp),'energy':{k:n.enc(v) for k,v in energy.items()},
            'scope':'semiprime packet versus ALL other spectral modes, not high-only',
            'independent_local_Newton_coefficients':last,'rows_sha256':n.vector_hash(rows)}


def produce(quick: bool = False):
    return {'packet':'ATC29','schema':1,'bits':n.BITS,'RH_proved':False,
            'campaign': 'quick' if quick else 'default',
            'infinite_theorems_checked_by_code':False,
            'primitive_sha256':PRIMITIVE_SHA256,
            'period_tests':period_checks(12 if quick else 48),
            'complete_panels':[complete_panel(Y) for Y in ([31] if quick else [31,63,95,127])],
            'large_band_panels':[large_band(Y) for Y in ([255] if quick else [4095,16383,65535])]}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--quick', action='store_true', help='separate bounded CLI test campaign; not the default receipt')
    g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--write',type=Path);g.add_argument('--check',type=Path)
    args=ap.parse_args()
    actual=produce(args.quick)
    payload=n.canonical(actual)
    if args.write:args.write.write_bytes(payload)
    else:n.require(n.same_types(n.read_json(args.check),actual),'report differs from full reconstruction')
    print('PASS_ATC29',hashlib.sha256(payload).hexdigest())

if __name__=='__main__':main()
