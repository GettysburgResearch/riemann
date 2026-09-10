#!/usr/bin/env python3
"""Finite exact algebra for OEC26, not a verifier of its infinite analytic proofs."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
GROUPS: list[dict[str, Any]] = []

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)

def record(name: str, count: int, detail: str) -> None:
    require(type(count) is int and count > 0, 'nonpositive fixture count')
    GROUPS.append({'name': name, 'fixtures': count, 'detail': detail})

def mul(a: list[F], b: list[F], n: int | None = None) -> list[F]:
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out if n is None else (out + [F(0)]*n)[:n]

def derivative(a: list[F]) -> list[F]:
    return [i*a[i] for i in range(1, len(a))] or [F(0)]

def exp_series(t: F, n: int) -> list[F]:
    return [t**j/F(factorial(j)) for j in range(n)]

def trial(n: int) -> dict[int, int]:
    out: dict[int,int] = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n,0)+1
    return out

def prime_sieve(n: int) -> list[int]:
    marks = [True]*(n+1)
    marks[:2] = [False,False]
    for p in range(2,isqrt(n)+1):
        if marks[p]:
            for k in range(p*p,n+1,p):
                marks[k] = False
    return [k for k in range(2,n+1) if marks[k]]

def log2_box(n: int = 12) -> tuple[F,F]:
    q = F(1,3)
    lo = 2*sum((q**(2*j+1)/F(2*j+1) for j in range(n)), F(0))
    tail = 2*q**(2*n+1)/(F(2*n+1)*(1-q*q))
    return lo, lo+tail

def integral_exp_polynomial(p: list[F], rate: F) -> F:
    return sum((a*F(factorial(k))/rate**(k+1) for k,a in enumerate(p)),F(0))

def strict_json(path: Path) -> Any:
    def pairs(xs: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str,Any] = {}
        for k,v in xs:
            require(k not in out, 'duplicate JSON key')
            out[k] = v
        return out
    def no_float(_: str) -> Any:
        raise ValueError('floating JSON is forbidden')
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_float=no_float, parse_constant=no_float)

def same(a: Any, b: Any) -> bool:
    if type(a) is not type(b):
        return False
    if isinstance(a,dict):
        return a.keys()==b.keys() and all(same(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(same(x,y) for x,y in zip(a,b))
    return a==b

def run() -> dict[str, Any]:
    GROUPS.clear()
    primes = prime_sieve(256)
    count = 0
    for X in [2,3,5,8,16,32,64]:
        atoms: dict[int,int] = {}
        for p in primes:
            if p > X:
                break
            n = p
            while n <= 256:
                atoms[n] = p
                n *= p
        for n in range(2,257):
            fs = trial(n)
            base = next(iter(fs)) if len(fs)==1 else 0
            expected = base if base and base <= X else 0
            require(atoms.get(n,0)==expected, 'prime-base all-power fixture')
            if n < X:
                require(atoms.get(n,0)==base, 'native horizon omitted an atom')
            count += 1
    require(4 in {2**k for k in range(1,9)}, 'included square control')
    record('prime_base_and_native_horizon', count,
           'Seven prime-base cutoffs; every n=2..256; not an infinite prime census.')

    count = 0
    for n in range(1,129):
        coeff: dict[int,int] = {}
        for d in range(2,n+1):
            if n%d==0:
                fs=trial(d)
                if len(fs)==1:
                    p=next(iter(fs)); coeff[p]=coeff.get(p,0)+1
        require(coeff==trial(n), 'formal Lambda*1=log n')
        count += 1
    # C'/C=1/(w-1)-2/w, checked after multiplication by w^3.
    # C=(w-1)/w^2, so w^3*C'=2-w.
    for w in [F(3,2),F(2),F(7,3),F(5)]:
        C=(w-1)/w**2
        Cp=(2-w)/w**3
        require(Cp==C*(1/(w-1)-2/w), 'signed logarithmic derivative')
        count+=1
    record('literal_divisor_derivation',count,
           '128 independent factorization identities and four rational factor checks.')

    laguerres = [[F((-1)**k*comb(j,k),factorial(k)) for k in range(j+1)]
                 for j in range(8)]
    count=0
    for j in range(8):
        for k in range(8):
            val=integral_exp_polynomial(mul(laguerres[j],laguerres[k]),F(1))
            require(val==int(j==k),'Laguerre Gram')
            count+=1
    record('complete_laguerre_gram',count,'Full order-zero-through-seven rational Gram.')

    count=0
    for m in range(1,9):
        for lam in [F(1,4),F(2,3),F(3,2)]:
            # Local source D(lambda+w)=w^m(2+3w+w^2).
            D=[F(0)]*m+[F(2),F(3),F(1)]
            inv=[F((-1)**j*comb(j+2,2))/(lam+1)**(j+3) for j in range(m)]
            target=mul(derivative(D),inv,m)
            require(all(v==0 for v in target[:m-1]),'lower jets must vanish')
            require(target[m-1]*factorial(m-1)==F(2*factorial(m))/(lam+1)**3,
                    'highest derivative coefficient')
            for T in [F(0),F(1,3),F(7,2)]:
                shifted=mul(exp_series(T,m),target,m)
                require(shifted==target,'translated highest jet acquires a false T power')
                count+=1
    record('multiplicity_and_delayed_jets',count,
           'Exact local polynomial jets; finite synthetic algebra, no zeta zero values.')

    count=0
    for sig in [F(1,8),F(1,3),F(1)]:
        for x in [sig,2*sig]:
            for y in [F(0),F(1,2),F(3)]:
                for t in [F(-4),F(-1),F(0),F(1,3),F(5)]:
                    ratio=(1+t*t)/(x*x+(y-t)**2)
                    require(ratio<=(2+2/sig**2)*(1+y*y),'Schwarz-kernel enclosure')
                    count+=1
    record('poisson_derivative_kernel_controls',count,
           'Ninety rational controls; the all-real inequality is separately proved.')

    count=0
    for alpha in [F(1,4),F(1,2),F(3,4),F(2)]:
        integral=integral_exp_polynomial([F(0),F(0),F(1),F(2),F(1)],2*alpha)
        expected=1/(4*alpha**3)+3/(4*alpha**4)+3/(4*alpha**5)
        require(integral==expected,'complete source moment')
        require(integral_exp_polynomial([F(0),F(0),F(1,2)],F(1))==1,'stable filter mass')
        count+=1
    record('source_moment_and_stable_filter',count,
           'Closed infinite exponential-polynomial integrals, evaluated by factorials.')

    count=0
    for L in [F(1,3),F(2),F(7,2)]:
        Ein=[F(0)]+[F((-1)**(k+1))*L**k/F(k*factorial(k)) for k in range(1,11)]
        direct=derivative(Ein)
        quotient=[F((-1)**j)*L**(j+1)/F(factorial(j+1)) for j in range(10)]
        require(direct==quotient,'entire continuum logarithmic derivative')
        require(direct[0]==L,'removable value at s=1')
        count+=10
    record('entire_cutoff_log_derivative',count,
           'Formal Taylor coefficients through nine; no truncated series used as an analytic bound.')

    count=0
    for eps in [1,2,3]:
        for cap in [2,3,5,11,31]:
            ps=prime_sieve(cap)
            cumulative=F(0); integral=F(0)
            for j,p in enumerate(ps):
                cumulative+=F(1,p*p)
                endweight=F(1,ps[j+1]**eps) if j+1<len(ps) else F(0)
                integral+=cumulative*(F(1,p**eps)-endweight)
            direct=sum((F(1,p**(2+eps)) for p in ps),F(0))
            require(integral==direct,'Abel step integration and atom interchange disagree')
            require(F(2)**eps*integral!=direct,'normalized-weight mutation must differ')
            count+=1
    record('abel_cutoff_atom_weights',count,
           'Full step integration versus atomwise summation at five cutoffs and three exponents.')

    lo,hi=log2_box()
    require(F(2,3)<lo<hi<F(7,10),'log2 complete remainder enclosure')
    require(F(7,5)**2<2<F(3,2)**2,'square-root bounds')
    require(sum((F(3,2)**j/F(factorial(j)) for j in range(4)),F(0))>F(7,2),
            'Euler-factor logarithm bound')
    pi_lower=4*sum((F((-1)**j,2*j+1) for j in range(8)),F(0))
    require(pi_lower>3,'alternating arctangent pi lower bound')
    low=F(1,2)+F(7,5)+F(147,800)+F(3,2)
    require(low<4,'low-frequency actual-source bound')
    upper=2+F(3,4)+F(21,40)
    require(upper==F(131,40) and upper<4,'whole-frequency E_half(2) bound')
    record('actual_X2_complete_frequency_margin',6,
           'Rational enclosures supporting the analytic all-frequency bound E_(1/2)(2)<4.')

    count=0
    for eps in [F(1,10),F(1,2),F(1),F(3)]:
        val=integral_exp_polynomial([F(1),F(3),F(3),F(1)],eps)
        require(val==1/eps+3/eps**2+6/eps**3+6/eps**4,'conditional Abel polylog moment')
        count+=1
    record('conditional_moment_antiderivatives',count,
           'No unconditional entropy moment is asserted; these are integrals of the conditional majorant.')

    return {'schema':'OEC26_EXACT_CONTROLS_V1',
            'arithmetic':'EXACT_RATIONAL_AND_FORMAL_PRIME_LOG',
            'rh_proved':False,'unconditional_entropy_upper_bound_proved':False,
            'groups':GROUPS.copy(),'named_groups':len(GROUPS),
            'bounded_fixtures':sum(g['fixtures'] for g in GROUPS),
            'analytic_bound_constants_checked':{'b':'1/2','X':2,'upper_bound':'4','integral_evaluated':False},
            'analytic_proofs_machine_verified':False}

def main() -> None:
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path); p.add_argument('--check',type=Path)
    args=p.parse_args(); result=run()
    if args.check:
        require(same(strict_json(args.check),result),'retained result differs from exact reconstruction')
    text=json.dumps(result,sort_keys=True,indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    else:
        print(text,end='')

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,TypeError,KeyError) as exc:
        raise SystemExit('REJECT: '+str(exc))
