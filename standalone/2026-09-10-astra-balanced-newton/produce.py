#!/usr/bin/env python3
"""BNR26 exact producer. Finite checks; the all-scale energy gain is OPEN."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path

BITS = 128
SCALE = 1 << BITS
LIMIT = 65535
SCHEMA = 'BNR26-v1'
SCOPE = {'rh_proved': False, 'unbounded_gain_proved': False,
         'finite_native_prefix_reconstruction': True,
         'raw_future_tail': 'analytic bound, not omitted or fully enumerated',
         'generic_control_is_mobius': False}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def raw(obj: object) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()


def digest(obj: object) -> str:
    return sha256(raw(obj)).hexdigest()


def frac(q: F) -> list[int]:
    return [q.numerator, q.denominator]


def mobius(N: int) -> list[int]:
    mu = [1]*(N+1)
    mu[0] = 0
    composite = [False]*(N+1)
    for p in range(2, N+1):
        if not composite[p]:
            for n in range(p, N+1, p):
                mu[n] *= -1
                composite[n] = True
            for n in range(p*p, N+1, p*p):
                mu[n] = 0
    return mu


def balance(prefix: list[int]) -> dict[int, F]:
    Y = len(prefix)-1
    b = Y+1
    M = sum(prefix[1:])
    m = sum((F(prefix[k], k) for k in range(1, b)), F())
    c = {k: F(prefix[k]) for k in range(1, b) if prefix[k]}
    c[b] = M-2*b*m
    c[2*b] = 2*b*m-2*M
    c = {k: v for k, v in c.items() if v}
    require(sum(c.values(), F()) == 0, 'total moment')
    require(sum((v/k for k, v in c.items()), F()) == 0, 'reciprocal moment')
    return c


def energy(c: dict[int, F]) -> F:
    items = sorted(c.items())
    total = cumulative = F()
    for i, (n, value) in enumerate(items):
        cumulative += value
        total += cumulative*cumulative*(F(1, n)-F(1, items[i+1][0]) if i+1 < len(items) else F(1, n))
    return total


def state(prefix: list[int]) -> tuple[F,F,F]:
    E = u = F()
    M = 0
    for k in range(1, len(prefix)):
        M += prefix[k]
        E += F(M*M, k*(k+1))
        u += F(M, k*(k+1))
    return E, u, E+2*len(prefix)*u*u


def scaled(c: dict[int, F]) -> tuple[dict[int,int],int]:
    D = 1
    for v in c.values():
        D = D*v.denominator//gcd(D, v.denominator)
    return {k: int(v*D) for k, v in c.items()}, D


def newton(c: dict[int,F], N: int) -> list[F]:
    C, D = scaled(c)
    cc = [0]*(N+1)
    for r, a in C.items():
        for s, b in C.items():
            if r*s <= N:
                cc[r*s] += a*b
    values = [0]*(N+1)
    for d, a in enumerate(cc):
        if d and a:
            for n in range(d, N+1, d):
                values[n] -= a
    for k, a in C.items():
        if k <= N:
            values[k] += 2*D*a
    return [F(a, D*D) for a in values]


def kernel(c: dict[int,F], x: int, endpoint_zero: bool = False) -> F:
    value = F()
    for r, a in c.items():
        for s, b in c.items():
            q, rem = divmod(x, r*s)
            psi = F(0) if endpoint_zero and rem == 0 else F(rem, r*s)-F(1,2)
            value += a*b*psi
    return value


def finite_panels(mu: list[int]) -> dict:
    projections, kernels, boundaries, stages = [], [], [], []
    for Y in range(1, 25):
        b, B = Y+1, (Y+1)**2-1
        c = balance(mu[:b])
        E,u,A = state(mu[:b])
        require(energy(c) == A, 'balanced optimum')
        # Three tail events: both moment constraints are unchanged.
        perturb = {b: F(b*((b+1)-2*b)), b+1: F((b+1)*(2*b-b)), 2*b: F(2*b*(b-(b+1)))}
        for multiplier in (F(-2,3), F(1), F(5,2)):
            d = {k: multiplier*v for k,v in perturb.items()}
            cd = dict(c)
            for k,v in d.items(): cd[k] = cd.get(k,F())+v
            require(energy(cd) == A+energy(d), 'Pythagorean comparison')
            projections.append([Y, frac(multiplier), frac(A), frac(energy(d))])
        values = newton(c, B+1)
        require(values[1:B+1] == mu[1:B+1], 'native entire new prefix')
        eb = -sum((v for d,v in c.items() if b%d == 0), F())
        require(F(mu[B+1])-values[B+1] == eb*eb, 'sharp support endpoint')
        boundaries.append([Y, frac(eb), frac(values[B+1]), mu[B+1]])
        V = F()
        I = ell = F()
        for k in range(1,B+1):
            V += values[k]
            if k >= b:
                I += V*V/F(k*(k+1))
                ell += V/F(k*(k+1))
            if Y <= 10 and k >= b:
                collar = 2*sum((v for r,v in c.items() if r <= k), F())
                psi = kernel(c,k)
                psi0 = kernel(c,k,True)
                div = sum((a*bv for r,a in c.items() for s,bv in c.items() if k%(r*s)==0),F())
                require(V == collar+psi, 'centered hyperbola identity including collar')
                require(psi == psi0-div/2, 'integer endpoint Fourier correction')
                kernels.append([Y,k,frac(V),frac(collar),frac(div)])
        EB,uB,AB = state(mu[:B+1])
        require(EB==E+I and uB==u+ell, 'joint energy and mean innovation')
        require(AB==E+I+2*(B+1)*(u+ell)**2, 'joint map')
        stages.append([Y,B,frac(I),frac(ell),frac(AB)])
    return {'projection_cases':len(projections),'kernel_cases':len(kernels),
            'boundary_cases':len(boundaries),'joint_map_cases':len(stages),
            'projection_sha256':digest(projections),'kernel_sha256':digest(kernels),
            'boundary_rows':boundaries,'joint_map_sha256':digest(stages)}


def recursive_ladder(mu: list[int]) -> list[dict]:
    prefix = [0,1]
    rows=[]
    for Y in (1,3,15,255):
        require(len(prefix)==Y+1, 'recursive source scale')
        B=(Y+1)**2-1
        values=newton(balance(prefix),B)
        require(all(v.denominator==1 for v in values), 'predicted integer coefficients')
        nxt=[int(v) for v in values]
        require(nxt==mu[:B+1], 'independent sieve comparison')
        rows.append({'Y':Y,'B':B,'coefficients_checked':B,
                     'source_sha256':digest(prefix[1:]),'predicted_sha256':digest(nxt[1:])})
        prefix=nxt
    return rows


def prefix_enclosures(mu: list[int]) -> dict:
    ys=list(range(1,65))+[127,255]
    targets=sorted(set(ys+[(Y+1)**2-1 for Y in ys]))
    table={}
    e=u=M=0
    for k in range(1,LIMIT+1):
        M+=mu[k]
        e+=(SCALE*M*M)//(k*(k+1))
        u+=(SCALE*M)//(k*(k+1))
        if k in targets:
            el,eh=F(e,SCALE),F(e+k,SCALE)
            ul,uh=F(u,SCALE),F(u+k,SCALE)
            low_square=F(0) if ul<=0<=uh else min(ul*ul,uh*uh)
            high_square=max(ul*ul,uh*uh)
            al,ah=el+2*(k+1)*low_square,eh+2*(k+1)*high_square
            table[k]={'Y':k,'M':M,'E':[frac(el),frac(eh)],'u':[frac(ul),frac(uh)],'A':[frac(al),frac(ah)]}
    tests=[]
    for Y in ys:
        B=(Y+1)**2-1
        a=F(*table[Y]['A'][0]); upper=F(*table[B]['A'][1])
        # Only this fixed finite pilot, not an unbounded estimate.
        margin=4*(1+a)**3-(1+upper)**2
        require(margin>0,'finite candidate inequality failed')
        tests.append([Y,B,frac(margin)])
    return {'rounding_bits':BITS,'all_prefix_entries':LIMIT,'enclosed_cutoffs':len(targets),'all_rows_sha256':digest([table[k] for k in targets]),
            'candidate':'1+A_B <= 2(1+A_Y)^(3/2)',
            'candidate_cases':len(tests),'candidate_sha256':digest(tests),
            'ladder_rows':[table[k] for k in [1,3,15,255,65535]]}


def raw_tails(mu: list[int]) -> list[dict]:
    rows=[]
    for Y in (1,2,3,7):
        c=balance(mu[:Y+1]); X=4096
        values=newton(c,X)
        V=F();total=0
        for k in range(1,X):
            V+=values[k]
            term=V*V/F(k*(k+1))
            total+=(SCALE*term.numerator)//term.denominator
        lo=F(total,SCALE);hi=F(total+X-1,SCALE)
        mass=sum((abs(v) for v in c.values()),F())
        tail=mass**4/F(4*X)
        rows.append({'Y':Y,'first_unintegrated_cell':X,'lower':frac(lo),
                     'upper':frac(hi+tail),'whole_tail_bound':frac(tail)})
    return rows


def generic_obstruction() -> list[dict]:
    rows=[]
    for b in (16,32,64,128):
        c={1:F(1),b:F(1-2*b),2*b:F(2*b-2)}
        require(sum(c.values())==0 and sum(v/k for k,v in c.items())==0,'fake balance')
        J=energy(c)
        require(J==2*b-3+F(1,b) and J<=2*b,'fake input energy')
        out=0
        for k in range(b*b//2,b*b):
            V=-k-2*(1-2*b)*(k//b)-2*(2*b-2)*(k//(2*b))
            require(2*V>=k,'fake half-annulus lower bound')
            out+=(SCALE*V*V)//(k*(k+1))
        outlo=F(out,SCALE);outhi=F(out+b*b//2,SCALE)
        require(outlo>=F(b*b,16) and outlo>=J*J/64,'quadratic lower bound')
        rows.append({'b':b,'input_J':frac(J),'annular_energy':[frac(outlo),frac(outhi)],'lower':frac(F(b*b,16)),
                     'native_mobius':False})
    return rows


def make() -> dict:
    mu=mobius(LIMIT)
    body={'schema':SCHEMA,'scope':SCOPE,'base':'f99d9e3908dde4865377c75d9ca051c1f545bf4f',
          'panels':finite_panels(mu),'recursive_ladder':recursive_ladder(mu),
          'prefix_energy':prefix_enclosures(mu),'raw_tails':raw_tails(mu),
          'generic_obstruction':generic_obstruction()}
    return {'body':body,'sha256':digest(body)}


def parse(path: Path) -> object:
    def unique(pairs):
        result={}
        for key,value in pairs:
            require(key not in result,'duplicate JSON key')
            result[key]=value
        return result
    return json.loads(path.read_text(),object_pairs_hook=unique,
                      parse_constant=lambda s: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path);ap.add_argument('--check',type=Path)
    args=ap.parse_args(); result=make()
    if args.check: require(raw(parse(args.check))==raw(result),'canonical typed reconstruction mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_bytes(raw(result)+b'\n')
    print('BNR PRODUCER PASS',result['sha256'])
    print('ladder',[r['B'] for r in result['body']['recursive_ladder']])
    print('finite gain panels',result['body']['prefix_energy']['candidate_cases'])

if __name__=='__main__':main()
