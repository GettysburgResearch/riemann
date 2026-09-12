#!/usr/bin/env python3
"""Exact bounded checks for HBR28; NOT a proof of RH or infinite analysis.

Standard library only. Each check reconstructs its inputs using Fraction.
--check compares the entire freshly computed receipt, not only a stored hash.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations
from typing import Any


def need(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def mul(a: list[F], b: list[F], n: int) -> list[F]:
    c = [F(0)] * (n + 1)
    for i, x in enumerate(a[:n+1]):
        if x:
            for j, y in enumerate(b[:n+1-i]):
                if y:
                    c[i+j] += x*y
    return c


def inv(a: list[F], n: int) -> list[F]:
    need(bool(a and a[0]), "inverse requires nonzero constant")
    c = [1/a[0]] + [F(0)]*n
    for k in range(1, n+1):
        c[k] = -sum(a[j]*c[k-j] for j in range(1, min(k, len(a)-1)+1))/a[0]
    return c


def power(a: list[F], k: int, n: int) -> list[F]:
    need(k >= 0, "power must be nonnegative")
    out = [F(1)] + [F(0)]*n
    while k:
        if k & 1:
            out = mul(out, a, n)
        a = mul(a, a, n)
        k >>= 1
    return out


def a(m: int) -> F:
    need(m >= 1, "a(m) in this checker requires m>=1")
    return (1-F(1, 2**(2*m-1)))/(2*m-1)


def source(n: int) -> list[F]:
    # 1/L(t)=sinh(sqrt(6t))/sqrt(6t).
    return inv([F(6**k, math.factorial(2*k+1)) for k in range(n+1)], n)


def moments(m: int, n: int, x: list[F], pareto: bool = False) -> list[F]:
    p = [F(1)]
    for k in range(1, n+1):
        b = F(2*m-1, 2*(m+k)-1) if pareto else a(m+k)/a(m)
        p.append(b/(1-b)*sum(p[j]*x[k-j] for j in range(k)))
    return p


def d_coeff(k: int) -> list[F]:
    d = [F(1)]
    for ell in range(1, k):
        d = mul(d, [F(-ell*ell), F(1)], len(d))
    return d


def B_coeff(m: int) -> list[F]:
    out = [F(0)]*m
    for k in range(1, m+1):
        fac = F(math.comb(m-1, k-1)*2**(2*k), math.factorial(2*k-1))
        for j, c in enumerate(d_coeff(k)):
            out[j] += fac*c
    return out


def determinant(matrix: list[list[F]]) -> F:
    b = [row[:] for row in matrix]
    value = F(1)
    for k in range(len(b)):
        pivot = next((i for i in range(k, len(b)) if b[i][k]), None)
        if pivot is None:
            return F(0)
        if pivot != k:
            b[k], b[pivot] = b[pivot], b[k]
            value = -value
        p = b[k][k]
        value *= p
        for i in range(k+1, len(b)):
            ratio = b[i][k]/p
            for j in range(k+1, len(b)):
                b[i][j] -= ratio*b[k][j]
    return value


def compute() -> dict[str, Any]:
    counts: dict[str, int] = {}
    witnesses: dict[str, Any] = {}
    stream: list[str] = []
    def eq(actual: Any, expected: Any, family: str) -> None:
        need(actual == expected, f"{family}: {actual!r} != {expected!r}")
        counts[family] = counts.get(family, 0) + 1
        stream.append(f"{family}:{actual}")
    def bound(ok: bool, family: str, value: Any) -> None:
        need(ok, f"failed {family}: {value}")
        counts[family] = counts.get(family, 0) + 1
        stream.append(f"{family}:{value}")

    degree = 36
    ell = source(degree)
    x = [(-1)**k*ell[k] for k in range(degree+1)]
    reciprocal = [F(6**k, math.factorial(2*k+1)) for k in range(degree+1)]
    for k, v in enumerate(mul(ell, reciprocal, degree)):
        eq(v, F(k == 0), "source_reciprocal")
        bound(0 < x[k] <= 1, "source_moment_bounds", x[k])
    # The source itself satisfies the nonlinear smoothing equation.
    squared = mul(ell, ell, degree)
    for k in range(1, degree+1):
        eq(a(k)*squared[k], ell[k], "source_fixed_point")

    deltas = {}
    for m in range(1, 13):
        p = moments(m, degree, x)
        pt = moments(m, degree, x, True)
        pp = [(-1)**k*p[k] for k in range(degree+1)]
        ht = mul(ell, pp, degree)
        for n in range(degree+1):
            eq(a(m+n)*ht[n], a(m)*pp[n], "native_eigenmode")
            eq((2*n+2*m-1)*pp[n],
               (ht[n]-F(1, 2**(2*m-1))*ht[n]/4**n)/a(m), "native_delay")
            bound(p[n] <= math.comb(n+2*m-1, 2*m-1), "perpetuity_majorant", p[n])
            if n:
                b = a(m+n)/a(m)
                bound(b <= F(2*m, n+2*m), "coarse_moment_ratio", b)
                eq(pt[n], F(2*m-1, 2*n)*sum(pt[j]*x[n-j] for j in range(n)),
                   "pareto_ode")
        eps = F(1, 2**(2*m-1))
        pt_signed = [(-1)**n*pt[n] for n in range(degree+1)]
        inverse_pt = inv(pt_signed, degree)
        ratio = mul(pp, inverse_pt, degree)
        numerator_over_t = [ht[n+1]*(1-F(1,4**(n+1))) for n in range(degree)]
        right = mul(numerator_over_t,inverse_pt,degree-1)
        for n in range(degree):
            eq((n+1)*ratio[n+1],eps/(2*a(m))*right[n],"survival_ratio_derivative")
        delta = 3*eps*(4*m*m-1)/(16-(12*m+10)*eps)
        eq(p[1]-F(2*m-1, 2), delta, "exact_W1")
        eq(-ratio[1],delta,"cutoff_density_at_origin")
        deltas[str(m)] = str(delta)

    # Explicit original-coordinate inverse and full coefficient tail weights.
    for k in range(1, degree+1):
        test = [F(0)]*(degree+1)
        test[k] = F(1)
        coeff = mul(ell, test, degree)
        image = [F(0)]+[2*a(n)*coeff[n] for n in range(1, degree+1)]
        diagonal_inverse = [F(0)]+[(2*n-1)*image[n]/(2*(1-F(2,4**n)))
                                   for n in range(1,degree+1)]
        eq(mul(reciprocal, diagonal_inverse, degree), test, "inverse_on_monomials")
    for R in (F(1,4), F(1,2), F(3,4)):
        for N in (8,16,32,64,128):
            q = 2*a(N+1)/(1-R)
            lam = F(1,3)
            if q < lam:
                J = 7
                exact_scalar_tail = (q/lam)**(J+1)/(lam-q)
                stated = q**(J+1)/(lam**(J+1)*(lam-q))
                eq(exact_scalar_tail, stated, "resolvent_tail_formula")

    # Conjugacy: in the r-coordinate, f=r*tanh(r/2)^k.
    nr = 32
    e = [F(1,math.factorial(n)) for n in range(nr+1)]
    numerator = e[:]; numerator[0] -= 1
    denominator = e[:]; denominator[0] += 1
    tanh_half = mul(numerator, inv(denominator,nr),nr)
    Lr = [F(0)]*(nr+1)
    invLr = [F(0)]*(nr+1)
    for n in range(nr//2+1):
        invLr[2*n] = F(1,math.factorial(2*n+1))
    Lr = inv(invLr,nr)
    for k in range(1,12,2):
        g = power(tanh_half,k,nr)
        f = [F(0)]+g[:-1]
        product = mul(Lr,f,nr)
        actual = [F(0)]*(nr+1)
        for n in range(1,nr//2+1):
            actual[2*n] = 2*a(n)*product[2*n]
        expected = [F(0)]+[F(2,k)*g[n]*(1-F(1,2**n)) for n in range(nr)]
        eq(actual,expected,"hyperbolic_conjugacy")

    # Compare Pareto ODE recurrence with the explicit tanh solution.
    base = [2*tanh_half[2*n+1]*6**n for n in range((nr-1)//2+1)]
    small_degree = len(base)-1
    for m in range(1,13):
        closed = power(base,2*m-1,small_degree)
        rec = moments(m,small_degree,x,True)
        eq(closed,[(-1)**n*rec[n] for n in range(small_degree+1)],"pareto_closed_series")

    # Clear denominators in the sech-power expansion, a polynomial identity in u=e^-2a.
    plus, minus = [F(1),F(1)], [F(1),F(-1)]
    Btable = {}
    for m in range(1,13):
        n = 2*m
        lhs = [F(0)] + [4*v for v in power(minus,2*m-2,n-1)]
        rhs = [F(0)]*(n+1)
        for k in range(1,m+1):
            coeff = F((-1)**(k-1)*math.comb(m-1,k-1)*4**k)
            term = power(plus,2*m-2*k,n-k)
            for j,v in enumerate(term):
                rhs[k+j] += coeff*v
        eq(lhs,rhs,"sech_polynomial_identity")
        bc = B_coeff(m)
        eq(bc[-1],F(2**(2*m),math.factorial(2*m-1)),"shift_diagonal")
        Btable[str(m)] = [str(v) for v in bc]
        for k in range(1,m+1):
            dc = d_coeff(k)
            for v in range(1,2*m+2):
                polynomial = v*sum(c*v**(2*j) for j,c in enumerate(dc))
                target = math.factorial(2*k-1)*math.comb(v+k-1,2*k-1) if v>=k else 0
                eq(polynomial,F(target),"sech_exponential_coefficients")

    # Native order-three counterexample; rational inverse of h is x=2h/(1+h^2).
    hs = [F(1,2),F(3,5),F(2,3)]
    xs = [2*v/(1+v*v) for v in hs]
    eq(xs,[F(4,5),F(15,17),F(12,13)],"half_angle_rational")
    ys = [F(5,8),F(3,4),F(5,6)]
    mat = [[F(2,y) if hh<y<xx else F(0) for y in ys] for hh,xx in zip(hs,xs)]
    eq(determinant(mat),F(-512,25),"native_TP3_counterexample")
    for rows in combinations(range(3),2):
        for cols in combinations(range(3),2):
            minor = determinant([[mat[i][j] for j in cols] for i in rows])
            bound(minor>=0,"TP2_control_minors",minor)
    witnesses["first_eigenvalues"] = [str(2*a(m)) for m in range(1,13)]
    witnesses["W1_distances"] = deltas
    witnesses["shift_coefficients_B"] = Btable
    witnesses["native_TP3_determinant"] = "-512/25"
    return {"schema":"HBR28-bounded-exact-v1", "status":"bounded rational identities only; RH not proved",
            "counts":counts, "total_checks":sum(counts.values()),
            "algebra_sha256":hashlib.sha256("\n".join(stream).encode()).hexdigest(),
            "witnesses":witnesses}


def unique_object(pairs: list[tuple[str,Any]]) -> dict[str,Any]:
    result: dict[str,Any] = {}
    for k,v in pairs:
        need(k not in result,f"duplicate JSON key {k}")
        result[k]=v
    return result


def compare(actual: dict[str,Any], expected: dict[str,Any]) -> None:
    need(actual == expected,"receipt mismatch")


def self_test(actual: dict[str,Any]) -> int:
    mutants = []
    for key in ("schema","status","algebra_sha256","total_checks"):
        x=copy.deepcopy(actual); x[key]="altered"; mutants.append(x)
    x=copy.deepcopy(actual); x["witnesses"]["native_TP3_determinant"]="512/25"; mutants.append(x)
    x=copy.deepcopy(actual); x["witnesses"]["W1_distances"]["2"]="0"; mutants.append(x)
    for x in mutants:
        try: compare(actual,x)
        except ValueError: pass
        else: raise ValueError("altered receipt was accepted")
    try: json.loads('{"a":1,"a":2}',object_pairs_hook=unique_object)
    except ValueError: pass
    else: raise ValueError("duplicate-key JSON was accepted")
    return len(mutants)+1


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write",type=Path,help="producer mode: write a new receipt")
    group.add_argument("--check",type=Path,help="recompute and compare a receipt")
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    actual=compute()
    if args.write:
        args.write.write_text(json.dumps(actual,indent=2,sort_keys=True)+"\n")
        print("PRODUCED",args.write)
    else:
        expected=json.loads(args.check.read_text(),object_pairs_hook=unique_object)
        compare(actual,expected)
        print("PASS",actual["algebra_sha256"],actual["total_checks"],"bounded exact checks")
    if args.self_test:
        print("SELF-TEST PASS:",self_test(actual),"altered/invalid records rejected by actual comparator/parser")
    return 0

if __name__=="__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"FAIL: {exc}")
