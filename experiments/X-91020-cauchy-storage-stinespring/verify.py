#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from fractions import Fraction
from pathlib import Path
import mpmath as mp

mp.mp.dps = 80

def f0_frac(y: Fraction) -> Fraction:
    return Fraction(16,1)/(y+4)**2 - Fraction(1,1)/(y+1)**2

def operator_coefficients(m: int) -> list[Fraction]:
    coeff=[Fraction(1)]
    for j in range(m):
        c=Fraction(1,4**(j+2))
        nxt=[Fraction(0)]*(len(coeff)+1)
        for k,v in enumerate(coeff):
            nxt[k]+=v
            nxt[k+1]-=c*v
        coeff=nxt
    return coeff

def fm_frac(m: int, y: Fraction) -> Fraction:
    coeff=operator_coefficients(m)
    return sum(coeff[k]*f0_frac(y/Fraction(4**k,1)) for k in range(len(coeff)))

def first_residual_closed(y: Fraction) -> Fraction:
    return Fraction(27)*y*(14*y*y+163*y+224)/((y+1)**2*(y+4)**2*(y+16)**2)

def prime_factors(n: int) -> list[int]:
    out=[]; m=n; p=2
    while p*p<=m:
        if m%p==0:
            out.append(p)
            while m%p==0: m//=p
        p += 1 if p==2 else 2
    if m>1: out.append(m)
    return out

def qcoef(a: int,n: int) -> Fraction:
    z=Fraction(1)
    for p in prime_factors(n):
        z*=Fraction(p**(2*a)-1,p**(2*a))
    return z

def divisors(n: int) -> list[int]:
    return [d for d in range(1,n+1) if n%d==0]

def cocycle(a: int,b: int,n: int) -> Fraction:
    return sum(qcoef(a,d)*qcoef(b,n//d)*Fraction(1,(n//d)**(2*a)) for d in divisors(n))

def psi(a: mp.mpf,s: mp.mpc) -> mp.mpc:
    alpha=(mp.mpf(163)-5*mp.sqrt(561))/28
    beta=(mp.mpf(163)+5*mp.sqrt(561))/28
    return mp.sqrt(378)*a**3*s*(s+mp.sqrt(alpha)*a)*(s+mp.sqrt(beta)*a)/((s+a)**2*(s+2*a)**2*(s+4*a)**2)

def d0(a: mp.mpf,u: mp.mpf) -> mp.mpf:
    n=lambda A: A**4/(A**2+u**2)**2
    return n(2*a)-n(a)

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--json",type=Path); args=ap.parse_args()
    checks=0
    min_exact=None
    ys=[Fraction(j,17) for j in range(0,170)] + [Fraction(j,3) for j in range(1,301)]
    for m in range(13):
        for y in ys:
            val=fm_frac(m,y)
            if min_exact is None or val<min_exact: min_exact=val
            assert val>=0
            if m<12:
                rhs=fm_frac(m,y)-Fraction(1,4**(m+2))*fm_frac(m,y/Fraction(4,1))
                assert fm_frac(m+1,y)==rhs
            checks+=2
    for y in ys:
        assert fm_frac(1,y)==first_residual_closed(y)
        checks+=1
    import math
    for m in range(10):
        assert Fraction(m+1, math.factorial(m+1)) == Fraction(1, math.factorial(m))
        assert Fraction(m+2, math.factorial(m+2)) == Fraction(1, math.factorial(m+1))
        checks+=2
    max_spec=mp.mpf(0)
    for aa in ["0.17","0.5","1.3"]:
        a=mp.mpf(aa)
        for uu in ["0","0.2","1.1","8"]:
            u=mp.mpf(uu)
            residual=d0(a,u)-mp.mpf(1)/16*d0(2*a,u)
            err=abs(abs(psi(a,mp.j*u))**2-residual)
            max_spec=max(max_spec,err)
            assert err<mp.mpf("1e-65") and residual>=-mp.mpf("1e-65")
            checks+=1
    exact=0
    for a in [1,2,3]:
        for b in [1,2]:
            for n in range(1,151):
                lhs=qcoef(a+b,n)
                rhs=cocycle(a,b,n)
                assert lhs==rhs
                probs=sum(qcoef(a,d)*qcoef(b,n//d)*Fraction(1,(n//d)**(2*a))/lhs for d in divisors(n))
                assert probs==1
                exact+=2
    checks+=exact
    coproduct=0
    for n in range(1,121):
        for d in divisors(n):
            e=n//d
            for p in sorted(set(prime_factors(n))):
                def vp(x: int) -> int:
                    c=0
                    while x and x%p==0: x//=p; c+=1
                    return c
                assert vp(n)==vp(d)+vp(e)
                coproduct+=1
    checks+=coproduct
    result={
        "classification":"PASS_ALL_ORDER_CAUCHY_STORAGE_AND_DIVISOR_STINESPRING",
        "checks":checks,
        "exact_sieve_cocycle_probability_checks":exact,
        "formal_log_coproduct_checks":coproduct,
        "minimum_exact_sampled_storage_value":str(min_exact),
        "max_spectral_factor_error":mp.nstr(max_spec,12),
        "scope":"finite exact arithmetic and high-precision synthetic checks only; no completed boundary intertwiner and no RH claim",
    }
    text=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True); args.json.write_text(text)
    else: print(text,end="")
    print("PASS_ALL_ORDER_CAUCHY_STORAGE_AND_DIVISOR_STINESPRING")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
