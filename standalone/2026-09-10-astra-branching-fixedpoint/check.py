#!/usr/bin/env python3
"""Exact bounded checks for BSR26. No zero-location oracle or float acceptance.

--emit is a producer operation, not an accepting check of an existing result.
The analytic theorems in PROPOSAL.md are not consequences of this finite replay.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
FILES = {'PROPOSAL.md', 'README.md', 'SOURCES.json', 'VALIDATION.md',
         'check.py', 'test_check.py', 'verification.json', 'SHA256SUMS'}
BASE = 'f99d9e3908dde4865377c75d9ca051c1f545bf4f'
BROWNIAN = '4a68887f9f713aea7f63444030379fb864766a2d'
FERROMAGNET = '7ff754c7347d6ee9d59608e562e469351b3d37e7'


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def pair(q: F | int) -> list[int]:
    q = F(q)
    return [q.numerator, q.denominator]


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode()


def strict_load(path: Path) -> object:
    need(path.is_file() and not path.is_symlink(), 'receipt must be a regular non-symlink file')
    need(path.stat().st_size <= 2_000_000, 'oversize receipt')
    def pairs(items):
        out = {}
        for k, v in items:
            need(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    def no_float(text):
        raise ValueError('floating/nonfinite JSON is not accepted')
    obj = json.loads(path.read_text(), object_pairs_hook=pairs,
                     parse_float=no_float, parse_constant=no_float)
    need(type(obj) is dict and bool(obj), 'nonempty object required')
    return obj


def authenticate() -> None:
    actual = {p.name for p in ROOT.iterdir()}
    need(actual == FILES, 'unexpected/missing packet inventory')
    for name in FILES:
        p = ROOT / name
        need(p.is_file() and not p.is_symlink(), 'nonregular packet member')
    rows = (ROOT / 'SHA256SUMS').read_text().splitlines()
    got = {}
    for line in rows:
        parts = line.split('  ')
        need(len(parts) == 2, 'malformed manifest')
        digest, name = parts
        need(name in FILES - {'SHA256SUMS'} and name not in got, 'manifest identity')
        need(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'digest format')
        need(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'packet hash mismatch')
        got[name] = digest
    need(set(got) == FILES - {'SHA256SUMS'}, 'manifest coverage')
    source = strict_load(ROOT / 'SOURCES.json')
    need(source['base'] == BASE and source['brownian_pr']['head'] == BROWNIAN
         and source['ferromagnetic_pr']['head'] == FERROMAGNET, 'source version mismatch')
    need(source['publication']['author_session_pushed'] is False, 'local publication boundary')


def a(k: int) -> F:
    return F(1) if k == 0 else (1-F(1, 2**(2*k-1)))/(2*k-1)


def moments_step(m: list[F]) -> list[F]:
    return [a(k)*sum((F(comb(k,j))*m[j]*m[k-j] for j in range(k+1)), F(0))
            for k in range(len(m))]


def fixed_moments(K: int) -> list[F]:
    m = [F(1), F(1)]
    for k in range(2,K+1):
        m.append(a(k)/(1-2*a(k))*sum((F(comb(k,j))*m[j]*m[k-j]
                                     for j in range(1,k)), F(0)))
    return m


def sinh_moments(K: int) -> list[F]:
    # Independent reciprocal series for sinh(sqrt(6t))/sqrt(6t).
    d = [F(6**k,factorial(2*k+1)) for k in range(K+1)]
    c = [F(1)]
    for k in range(1,K+1):
        c.append(-sum((d[j]*c[k-j] for j in range(1,k+1)), F(0)))
    return [(-1)**k*factorial(k)*c[k] for k in range(K+1)]


def gamma_moments(shape: F, K: int) -> list[F]:
    out=[F(1)]
    for k in range(1,K+1):
        out.append(out[-1]*(shape+k-1)/shape)
    return out


def bernstein_quarters() -> list[list[F]]:
    coeff = [F(1,25), -F(1,4), F(23,48), F(0), -F(1,4)]
    allrows=[]
    for j in range(4):
        lo=F(j,4); length=F(1,4)
        power=[sum((coeff[k]*comb(k,i)*lo**(k-i)*length**i
                    for k in range(i,5)),F(0)) for i in range(5)]
        b=[sum((power[i]*F(comb(k,i),comb(4,i)) for i in range(k+1)),F(0))
           for k in range(5)]
        # Independently expand Bernstein polynomials into monomials.
        expanded=[F(0)]*5
        for k in range(5):
            for j2 in range(5-k):
                expanded[k+j2] += b[k]*comb(4,k)*comb(4-k,j2)*(-1)**j2
        need(expanded == power, 'Bernstein polynomial identity')
        need(all(v>0 for v in b), 'gamma phase lower bound fails')
        allrows.append(b)
    expected=[
      [F(1,25),F(39,1600),F(1583,115200),F(311,38400),F(497,76800)],
      [F(497,76800),F(31,6400),F(833,115200),F(81,6400),F(23,1200)],
      [F(23,1200),F(493,19200),F(3833,115200),F(1,25),F(1099,25600)],
      [F(1099,25600),F(587,12800),F(5183,115200),F(359,9600),F(23,1200)]]
    need(allrows == expected, 'independent printed Bernstein coefficients')
    need(F(59,84)+F(1,48)==F(243,336), 'small phase constant')
    need(F(243,168)<F(3,2) and F(13,24)<F(3,2), 'phase sector')
    # A complete rational pi bracket from the alternating Machin formula.
    def atan_bounds(q):
        n=24
        v=sum((F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(n)),F(0))
        term=F((-1)**n,(2*n+1)*q**(2*n+1))
        return min(v,v+term),max(v,v+term)
    l5,h5=atan_bounds(5); l239,h239=atan_bounds(239)
    plo=16*l5-4*h239; phi=16*h5-4*l239
    need(plo>F(25,8) and phi<F(22,7), 'complete Machin pi range')
    return allrows


def validate_law(law: list[tuple[F,F]]) -> None:
    need(bool(law), 'empty law')
    need(all(type(x) is F and type(p) is F and x>0 and p>0 for x,p in law), 'positive rational law')
    need(all(law[i][0]<law[i+1][0] for i in range(len(law)-1)), 'unmerged/unsorted atoms')
    need(sum((p for x,p in law),F(0))==1, 'probability mass')
    need(sum((x*p for x,p in law),F(0))==1, 'mean-one condition')


def quantize(law: list[tuple[F,F]], L: int) -> list[tuple[F,F]]:
    validate_law(law); need(type(L) is int and L>=1, 'positive bin count')
    out=defaultdict(F)
    for x,p in law:
        for y,q in law:
            for j in range(L):
                lo=F(L+j,L); hi=F(L+j+1,L)
                out[(x+y)/(lo*hi)] += p*q/L
    ans=sorted(out.items()); validate_law(ans)
    return ans


def quantile_cost(law, other):
    validate_law(law); validate_law(other)
    i=j=0; p=law[0][1]; q=other[0][1]; total=F(0); rows=[]
    while i<len(law) and j<len(other):
        mass=min(p,q)
        rows.append((i,j,mass))
        total+=mass*(law[i][0]-other[j][0])**2
        p-=mass; q-=mass
        if not p:
            i+=1
            if i<len(law):p=law[i][1]
        if not q:
            j+=1
            if j<len(other):q=other[j][1]
    need(i==len(law) and j==len(other), 'transport leftover')
    for i,(x,p) in enumerate(law):
        need(sum((m for ii,jj,m in rows if ii==i),F(0))==p,'transport source margin')
    for j,(x,p) in enumerate(other):
        need(sum((m for ii,jj,m in rows if jj==j),F(0))==p,'transport destination margin')
    need(all(rows[k][0]<=rows[k+1][0] and rows[k][1]<=rows[k+1][1]
             for k in range(len(rows)-1)), 'transport crossings')
    return total, rows


def sqrt_bounds(q: F, bits: int=96) -> tuple[F,F]:
    need(q>=0, 'negative radicand')
    scale=1<<bits
    r=isqrt(q.numerator*scale*scale//q.denominator)
    lo=F(r,scale); hi=lo if lo*lo==q else F(r+1,scale)
    need(lo*lo<=q<=hi*hi, 'directed square-root check')
    return lo,hi


def decimal_bounds(lo: F, hi: F, places: int=12):
    scale=10**places
    a=lo.numerator*scale//lo.denominator
    b=-((-hi.numerator*scale)//hi.denominator)
    def fmt(k):
        return f'{k//scale}.{k%scale:0{places}d}'
    return [fmt(a),fmt(b)]


def reconstruct() -> dict:
    need(a(1)==F(1,2) and 2*a(2)==F(7,12), 'shared-uniform contraction constant')
    need(F(9,16)<2*a(2)<F(16,25), 'contraction interval')
    m=fixed_moments(12)
    need(m==sinh_moments(12), 'smoothing versus independent sinh moments')
    gm=gamma_moments(F(5,2),12); orbit=[]
    for n in range(17):
        need(gm[1]==1 and gm[2]==F(7,5), 'exact gamma-orbit mean/variance')
        need(gm[3]==F(93,35)-F(24,175)*F(31,80)**n, 'third-moment orbit identity')
        orbit.append({'depth':n,'moments_0_to_6':[pair(x) for x in gm[:7]]})
        gm=moments_step(gm)
    mart=[F(1)]*13
    for n in range(13):
        need(mart[2]==F(7,5)-F(2,5)*F(7,12)**n,'deterministic-leaf second moment')
        need(all(mart[j]<=m[j] for j in range(13)), 'conditional convex moment bound')
        mart=moments_step(mart)
    b=bernstein_quarters()
    law=[(F(1),F(1))]; qs=[]
    for n in range(3):
        L=2**(n+1); new=quantize(law,L)
        m2=sum((p*x*x for x,p in law),F(0))
        m2new=sum((p*x*x for x,p in new),F(0))
        eps2=F(0)
        for j in range(L):
            lo=F(L+j,L); hi=F(L+j+1,L); h=hi-lo
            e1=(1/lo-1/hi)/h
            e2=(lo**-3-hi**-3)/(3*h)
            need(e1==1/(lo*hi), 'bin mean primitive')
            need(e2-e1*e1==h*h/(3*lo**3*hi**3), 'bin variance primitive')
            eps2 += (2*m2+2)*h**3/(3*lo**3*hi**3)
        need(m2new+eps2==a(2)*(2*m2+2), 'complete conditional-variance identity')
        need(m2new<=F(7,5) and eps2<=F(2*m2+2,3*L*L), 'uniform quantization bounds')
        cost,rows=quantile_cost(law,new)
        d0,d1=sqrt_bounds(cost); e0,e1=sqrt_bounds(eps2)
        low=max(F(0),d0-e1); high=d1+e1
        atombytes=canon([[pair(x),pair(p)] for x,p in new])
        qs.append({'depth':n,'L':L,'atoms_before':len(law),'atoms_after':len(new),
          'all_output_atoms_sha256':hashlib.sha256(atombytes).hexdigest(),
          'transport_segments':len(rows),'variance_before':pair(m2-1),
          'bin_coupling_cost_squared':pair(eps2),'discrete_W2_squared':pair(cost),
          'true_map_residual_interval':[pair(low),pair(high)],
          'decimal_outward_residual':decimal_bounds(low,high)})
        law=new
    return {'schema':'BSR26-1','rh_proved':False,'orbit_strip_preservation_proved':False,
      'gamma_seed_strip_scope':'all real k >= 1; proof manuscript, not a zero scan',
      'source':{'base':BASE,'brownian_pr':BROWNIAN,'ferromagnetic_pr':FERROMAGNET},
      'r':pair(2*a(2)),'fixed_moments_0_to_12':[pair(x) for x in m],
      'gamma_orbit':orbit,'gamma_Bernstein_rows':[[pair(v) for v in row] for row in b],
      'quantized_laws':qs,
      'coverage':{'sinh_moments_compared':13,'gamma_depths':17,'gamma_moments_per_depth':13,
                  'deterministic_second_moments':13,'Bernstein_intervals':4,
                  'Bernstein_coefficients':20,'quantization_transitions':3,
                  'uniform_bins':14,'largest_finite_support':350},
      'actual_zeta_values_computed':False,'quadrature_used_for_acceptance':False}


def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument('--check',type=Path)
    parser.add_argument('--emit',type=Path)
    args=parser.parse_args()
    need((args.check is None)!=(args.emit is None), 'choose check OR producer emit')
    if args.check is not None:
        authenticate()
        expected=strict_load(args.check)
        computed=reconstruct()
        need(canon(expected)==canon(computed),'reconstruction mismatch (typed canonical JSON)')
        print('PASS_BSR26_BOUNDED_RECONSTRUCTION '+hashlib.sha256(canon(computed)).hexdigest())
    else:
        args.emit.write_text(json.dumps(reconstruct(),sort_keys=True,indent=2)+'\n')
        print('PRODUCED_UNAUTHENTICATED_BSR26_RESULT')
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (ValueError,KeyError,TypeError,OSError,ZeroDivisionError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr)
        raise SystemExit(2)
