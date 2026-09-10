#!/usr/bin/env python3
"""Exact finite algebra for the reciprocal gamma cascade.

No zeros, quadratures, special-function values or RH claim enter acceptance.
All arithmetic here is Python integer/Fraction arithmetic. The infinite
convergence and Bessel spectral arguments are written proofs in PROPOSAL.md.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from math import factorial, comb
import json
from pathlib import Path
import sys


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def rat(x: F | int) -> str:
    x = F(x)
    return f"{x.numerator}/{x.denominator}"


def multiply(p: list[F], q: list[F]) -> list[F]:
    out = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def polynomial(rates: list[int], skip: int | None = None) -> list[F]:
    result = [F(1)]
    for a in rates:
        if a != skip:
            result = multiply(result, [F(a*a), F(2*a), F(1)])
    return result


def coefficients(nmax: int) -> list[tuple[int, F, F]]:
    """Return (rate, coefficient of x, constant) in f_N(x)."""
    require(type(nmax) is int and nmax >= 1, "N must be a positive integer")
    out = []
    for n in range(1, nmax+1):
        a = n*n
        b = F(2*factorial(nmax)**2,
              factorial(nmax-n)*factorial(nmax+n))**2
        c = F(1) - 2*a*sum((F(1, k*k-a)
                           for k in range(1, nmax+1) if k != n), F(0))
        out.append((a, b*a*a, b*a*(c-1)))
    return out


def moment_via_poles(rows: list[tuple[int,F,F]], k: int) -> F:
    return sum((u*F(factorial(k+1), a**(k+2))
                +v*F(factorial(k), a**(k+1))
                for a,u,v in rows), F(0))


def moments_via_convolution(nmax: int, order: int) -> list[F]:
    out = [F(1)] + [F(0)]*order
    for n in range(1,nmax+1):
        gamma = [F(factorial(k+1), n**(2*k)) for k in range(order+1)]
        out = [sum((comb(k,j)*out[j]*gamma[k-j] for j in range(k+1)), F(0))
               for k in range(order+1)]
    return out


def tail_budget(n: int) -> F:
    require(type(n) is int and n >= 1, "invalid tail cutoff")
    return F((n+1)*(2*n+1), n**3)


def reconstruct() -> dict:
    laplace_panels = 0
    boundary_panels = 0
    ode_panels = 0
    moment_panels = 0
    finite_products = 0
    for nmax in range(1,13):
        rows = coefficients(nmax)
        rates = [n*n for n in range(1,nmax+1)]
        numerator = [F(0)]*(2*nmax)
        for a,u,v in rows:
            other = polynomial(rates, skip=a)
            term = multiply(other, [u+v*a, v])
            for j,x in enumerate(term): numerator[j] += x
            # Independent local double-pole residue computation.
            local = F(a*a)
            slope = F(0)
            for b in rates:
                if b != a:
                    local *= F(b*b, (b-a)**2)
                    slope -= F(2,b-a)
            require(u == local and v == local*slope, "wrong local partial fraction")
            laplace_panels += 1
        expected = F(1)
        for a in rates: expected *= a*a
        require(numerator == [expected]+[F(0)]*(2*nmax-1), "wrong Laplace numerator")
        for k in range(2*nmax):
            derivative = sum((v*(-a)**k + (u*k*(-a)**(k-1) if k else 0)
                              for a,u,v in rows), F(0))
            require(derivative == (expected if k == 2*nmax-1 else 0),
                    "wrong density boundary jet")
            boundary_panels += 1
        independent_moments = moments_via_convolution(nmax, 8)
        for k, target in enumerate(independent_moments):
            require(moment_via_poles(rows,k) == target, "wrong full gamma moment")
            moment_panels += 1
        old = {a:(u,v) for a,u,v in rows}
        new = coefficients(nmax+1)
        birth = (nmax+1)**2
        for a,u,v in new:
            transformed = ((birth-a)**2*u, (birth-a)**2*v+2*(birth-a)*u)
            expected_pair = tuple(birth**2*x for x in old.get(a,(F(0),F(0))))
            require(transformed == expected_pair, "wrong cascade differential equation")
            ode_panels += 1
    for n in range(1,33):
        require(tail_budget(n) <= F(6,n), "tail rate too large")
        for m in [n+1,2*n+3,4*n+7]:
            product, derivative = F(1), F(0)
            for k in range(n+1,m+1):
                product *= F(k*k,k*k-1)**2
                derivative += F(2,k*k-1)
            exact_product = F((n+1)*m,n*(m+1))**2
            exact_derivative = F(1,n)+F(1,n+1)-F(1,m)-F(1,m+1)
            require(product == exact_product and derivative == exact_derivative,
                    "wrong telescoping tail")
            require(product*derivative < tail_budget(n), "finite tail exceeds whole tail")
            finite_products += 1
    flow_panels = 0
    for a in [4,9,16,25,36]:
        for u in [F(0), F(1,4), F(1,2), F(1)]:
            for q in [F(0),F(1,3),F(1),F(7,2)]:
                factor = (1+u*q/a)**(-2)
                derivative = -F(2)*q/a*(1+u*q/a)**(-3)
                require((a+u*q)*derivative == -2*q*factor, "wrong continuous flow symbol")
                flow_panels += 1
    # Rational parts of the normalizer and weighted-tail estimates.
    require(F(1,4)+F(1,2) == F(3,4), "sum/integral majorant")
    require(1-F(3,2)/2 == F(1,4), "Markov mass guard")
    require(F(3)/F(5,4) == F(12,5), "central interval lower bound")
    require(F(22,7)*F(5,4) < 4, "central interval upper bound")
    require(F(1,4)*(F(12,5)-2)*F(1,5) == F(1,50), "normalizer coefficient")
    require(F(1,50*3**4) == F(1,4050), "normalizer rational lower bound")
    require(3*(28*4050+16*28*4050**2) == 22045300200, "strip constant")
    return {
        "status": "EXACT_FINITE_ALGEBRA_ONLY",
        "rh_proved": False,
        "infinite_theorems_machine_proved": False,
        "numerical_zero_certificate": False,
        "coverage": {
            "density_cutoffs": list(range(1,13)),
            "local_partial_fractions": laplace_panels,
            "boundary_derivatives": boundary_panels,
            "convolution_moments": moment_panels,
            "cascade_coefficient_identities": ode_panels,
            "finite_tail_products": finite_products,
            "continuous_flow_symbols": flow_panels,
            "normalizer_and_strip_constant_controls": 7
        },
        "tail_budgets": {str(n):rat(tail_budget(n)) for n in [1,2,4,8,16,32]},
        "density_N2": [[a,rat(u),rat(v)] for a,u,v in coefficients(2)],
        "raw_moments_N4": [rat(v) for v in moments_via_convolution(4,8)]
    }


def strict_load(path: Path):
    def pairs(items):
        d = {}
        for key,value in items:
            require(key not in d, "duplicate JSON key")
            d[key] = value
        return d
    def bad(value):
        raise ValueError("nonfinite JSON token")
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=pairs,
                      parse_constant=bad)


def same_typed(a, b) -> bool:
    if type(a) is not type(b): return False
    if isinstance(a,dict):
        return a.keys() == b.keys() and all(same_typed(a[k],b[k]) for k in a)
    if isinstance(a,list):
        return len(a)==len(b) and all(same_typed(x,y) for x,y in zip(a,b))
    return a == b


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",type=Path,help="Producer mode, not receipt acceptance")
    group.add_argument("--check",type=Path,help="Reconstruct all finite algebra and compare typed JSON")
    args=parser.parse_args()
    result=reconstruct()
    if args.write:
        args.write.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        print("PRODUCED_EXACT_ALGEBRA_RECEIPT")
    else:
        require(same_typed(strict_load(args.check),result),"receipt does not match fresh exact reconstruction")
        print("PASS_EXACT_FINITE_ALGEBRA_ONLY")

if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        print("FAIL: "+str(exc),file=sys.stderr)
        sys.exit(1)
