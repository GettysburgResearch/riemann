#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, sys
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

sys.set_int_max_str_digits(0)
DEN = 10**70
NLOG = 260
P61 = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61)
BASE = ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3),(11,11),(13,13))
NMAX = 67*67


def ftxt(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def dec(x: F, n: int = 18) -> str:
    s = 10**n
    q = x.numerator*s//x.denominator
    return f"{q//s}.{q%s:0{n}d}"


def sqrt_iv(x: F) -> tuple[F,F]:
    k = isqrt(x.numerator*DEN*DEN//x.denominator)
    lo = F(k,DEN)
    hi = lo if lo*lo == x else F(k+1,DEN)
    assert lo*lo <= x <= hi*hi
    return lo,hi


def invsqrt_iv(x: F) -> tuple[F,F]:
    lo,hi = sqrt_iv(x)
    return F(1,hi),F(1,lo)


def log_iv(x: F) -> tuple[F,F]:
    assert x > 0
    e,y = 0,x
    while y >= 2:
        y /= 2; e += 1
    while y < 1:
        y *= 2; e -= 1

    def series(z: F) -> tuple[F,F]:
        z2,p,s = z*z,z,F(0)
        for k in range(NLOG):
            s += p/F(2*k+1); p *= z2
        s *= 2
        return s, s + 2*p/(F(2*NLOG+1)*(1-z2))

    lo,hi = series((y-1)/(y+1))
    l2,u2 = series(F(1,3))
    return (lo+e*l2,hi+e*u2) if e >= 0 else (lo+e*u2,hi+e*l2)


def factor(n: int) -> dict[int,int]:
    out,x,q = {},n,2
    while q*q <= x:
        while x%q == 0:
            out[q] = out.get(q,0)+1; x //= q
        q = 3 if q == 2 else q+2
    if x > 1: out[x] = out.get(x,0)+1
    return out


def boolean_lambda(n: int) -> dict[int,int]:
    fac = factor(n)
    small = [q for q in P61 if q in fac]
    out = {q:0 for q in fac}
    for mask in range(1<<len(small)):
        sign = -1 if mask.bit_count()%2 else 1
        chosen = {small[i] for i in range(len(small)) if mask>>i&1}
        for q,a in fac.items(): out[q] += sign*(a-(q in chosen))
    return {q:a for q,a in out.items() if a}


def expected_lambda(n: int) -> dict[int,int]:
    fac = factor(n); small = [q for q in P61 if q in fac]
    if not small: return fac
    return {small[0]:1} if len(small)==1 else {}


def main() -> dict[str,object]:
    # Directed lower packet for R(67).
    rlo, base_lines = F(0),[]
    for n,p in BASE:
        lp,up = log_iv(F(p)); li,ui = invsqrt_iv(F(n)); lr,ur = log_iv(F(67,n))
        a,b = lp*li*lr, up*ui*ur
        assert a > 0
        rlo += a
        base_lines.append(f"{n}:{ftxt(a)}:{ftxt(b)}")
    assert rlo > F(23,2)

    # Exact moat constants.
    assert F(41,67) < F(16,25)
    assert F(67) < F(33,4)**2
    assert log_iv(F(67))[1] < F(9,2)
    deriv = F(27,25)-F(9,67)-F(2,3)
    assert deriv == F(1402,5025) > 0
    base_gap = F(23,2)-F(4,3)*F(33,4)
    assert base_gap == F(1,2)
    dens30 = F(1)
    for q in (2,3,5): dens30 *= F(q-1,q)
    score_coeff = 3*F(5,3)*dens30
    assert dens30 == F(4,15) and score_coeff == F(4,3)

    # Exact Boolean density regression and Lambda domination.
    density_lines, vm_checks = [],0
    for n in range(2,NMAX+1):
        actual,expected = boolean_lambda(n),expected_lambda(n)
        assert actual == expected and all(a >= 0 for a in actual.values())
        fac = factor(n)
        if len(fac)==1:
            q = next(iter(fac)); assert actual.get(q,0) >= 1; vm_checks += 1
        density_lines.append(f"{n}:"+",".join(f"{q}^{a}" for q,a in sorted(actual.items())))

    return {
      "classification":"PASS_P61_PHYSICAL_ENTROPY_DEBT_ABSORPTION",
      "p61_prime_count":len(P61),
      "base_terms_checked":len(BASE),
      "r67_subset_lower_decimal":dec(rlo),
      "r67_threshold":"23/2",
      "base_physical_entropy_margin":ftxt(base_gap),
      "derivative_margin":ftxt(deriv),
      "derivative_margin_decimal":dec(deriv),
      "p30_density":ftxt(dens30),
      "declared_score_upper_coefficient":ftxt(score_coeff),
      "density_regression_max_n":NMAX,
      "density_regression_checks":NMAX-1,
      "mangoldt_dominance_checks":vm_checks,
      "base_record_digest_sha256":hashlib.sha256("\n".join(base_lines).encode()).hexdigest(),
      "density_record_digest_sha256":hashlib.sha256("\n".join(density_lines).encode()).hexdigest(),
      "checks":{
        "directed_prime_power_base_terms":len(BASE),
        "sqrt_41_over_67_below_4_over_5":1,
        "sqrt_67_below_33_over_4":1,
        "log_67_below_9_over_2":1,
        "positive_log_derivative_margin":1,
        "p30_declared_score_bound":1,
        "boolean_entropy_density_regression":NMAX-1,
      },
      "scope":(
        "Exact Fraction arithmetic and outward square-root/logarithm enclosures certify the base and scalar constants in the P_61 physical-entropy moat. "
        "The Boolean regression checks the exact nonnegative entropy-density formula through n=4489. Together with the published Chebyshev bound psi(x)>=0.9x for x>=41 and the algebra in L-91682, this proves that every P_61 one-prime causal signed row with p>=67 and 1<=y<67 has literal physical entropy exceeding its signed declared score by more than 1/2. "
        "It does not prove the target/row determinants, the finite causal profile corridor, the root equality realization, or RH."
      )
    }


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--json",type=Path); args = ap.parse_args()
    result = main(); text = json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True); args.json.write_text(text)
    print(result["classification"])
    print("base entropy margin:",result["base_physical_entropy_margin"])
    print("derivative margin:",result["derivative_margin"])
    print("R(67) subset lower:",result["r67_subset_lower_decimal"])
