#!/usr/bin/env python3
"""Exact finite tests. No L-values, zero census, or infinite proof certification."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial, gcd, isqrt
from pathlib import Path
import sys

COUNTS: Counter[str] = Counter()
MUTATION = ""


def check(ok: bool, group: str) -> None:
    COUNTS[group] += 1
    if not ok:
        raise ValueError("FAILED:" + group)


def mul(a: tuple[int, int], b: tuple[int, int], d: int) -> tuple[int, int]:
    return a[0]*b[0]+d*a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def power(a: tuple[int, int], n: int, d: int) -> tuple[int, int]:
    out = (1, 0)
    for _ in range(n):
        out = mul(out, a, d)
    return out


def derivative_coefficient(r: int, j: int) -> int:
    if j > r:
        return 0
    if MUTATION == "hasse":
        return comb(r, j)
    return factorial(r)//factorial(r-j)


def jet(poly: dict[tuple[int, int], int], x: int, y: int,
        j: int, d: int) -> tuple[int, int]:
    a = b = 0
    for (r, s), c in poly.items():
        if j <= r:
            v = mul(power((x, y), r-j, d), power((x, -y), s, d), d)
            w = c*derivative_coefficient(r, j)
            a += w*v[0]
            b += w*v[1]
    return a, b


def poly_mul(a: dict, b: dict) -> dict:
    out: dict[tuple[int, int], int] = {}
    for (r, s), c in a.items():
        for (u, v), e in b.items():
            out[r+u, s+v] = out.get((r+u, s+v), 0)+c*e
    return {k:v for k,v in out.items() if v}


def bareiss(matrix: list[list[int]]) -> int:
    a = [r[:] for r in matrix]
    n = len(a)
    if not n:
        return 1
    prev, sign = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            row = next((i for i in range(k+1, n) if a[i][k]), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                value = a[i][j]*pivot-a[i][k]*a[k][j]
                quotient, remainder = divmod(value, prev)
                if remainder:
                    raise ArithmeticError("Bareiss nonexact division")
                a[i][j] = quotient
            a[i][k] = 0
        prev = pivot
    return sign*a[-1][-1]


def gram(rows: list[list[tuple[int, int]]], d: int) -> list[list[int]]:
    return [[2*sum(a*c+abs(d)*b*e for (a,b),(c,e) in zip(u,v))
             for v in rows] for u in rows]


def primes(n: int) -> list[int]:
    return [p for p in range(2, n+1) if all(p%j for j in range(2,isqrt(p)+1))]


def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("valuation of zero not used")
    out = 0
    while n%p == 0:
        out += 1
        n //= p
    return out


def template(R: int, S: int, p: int) -> int:
    factor = 1 if MUTATION == "factor-two" else 2
    return factor*sum(min(r//p,S-1-s) for r in range(R) for s in range(S))


def template_closed(R: int, S: int, p: int) -> int:
    k = min((R-1)//p,S-1)
    return 2*(R*S*k-(R+p*S)*k*(k+1)//2+p*k*(k+1)*(2*k+1)//6)


def ramp(x: Q, S: int, p: int) -> Q:
    return 2*sum((S-h)*max(Q(0),x-p*h) for h in range(1,S))


def mobius(n: int) -> int:
    out, k = 1, 2
    while k*k <= n:
        if n%k == 0:
            n //= k
            out = -out
            if n%k == 0:
                return 0
        k += 1
    return -out if n>1 else out


def root4ceil(value: Q) -> int:
    lo, hi = 0, 1
    while hi**4 < value:
        hi *= 2
    while hi-lo>1:
        m = (lo+hi)//2
        if m**4 >= value:
            hi = m
        else:
            lo = m
    return hi


def ceiling(x: Q) -> int:
    return -(-x.numerator//x.denominator)


def run() -> dict:
    # Ordinary derivatives across and above the prime order, not Hasse jets.
    for p in [3,5,7,11]:
        for j in range(1,p+3):
            c = derivative_coefficient(p,j)
            check(c%p == 0, "ordinary_derivatives")
        check(derivative_coefficient(p,p)==factorial(p), "ordinary_derivatives")

    # Actual Sylvester determinants for f=z^m-a and its ordinary derivative.
    for m in range(1,9):
        for a0 in [-2,-1,0,1,2]:
            f = [1]+[0]*(m-1)+[-a0]
            g = [m]+[0]*(m-1)
            n = 2*m-1
            syl = [[0]*i+f+[0]*(n-i-len(f)) for i in range(m-1)]
            syl += [[0]*i+g+[0]*(n-i-len(g)) for i in range(m)]
            check(bareiss(syl)==(-1)**(m-1)*m**m*a0**(m-1),
                  "resultant_fixture")

    # Complete declared finite parameter range, using two independent formulas.
    for R in range(1,33):
        for S in range(1,11):
            for p in [2,3,5,7,11]:
                e = template(R,S,p)
                check(e == template_closed(R,S,p), "valuation_template")
                check(e == ramp(Q(R),S,p), "valuation_template")
                alpha = Q(1)-Q(1,R)-Q(1,2*S)
                check(Q(e,S*R*R)>=alpha/p-Q(2,R)-Q(R,3*S*p*p),
                      "valuation_lower_bound")
    for p in [2,3,5,7]:
        for x in [Q(n,2) for n in range(2,51)]:
            for h in range(1,8):
                check(ramp(x,h+1,p)-2*ramp(x,h,p)+ramp(x,h-1,p)
                      == 2*max(Q(0),x-p*h), "second_difference")

    # All rows, grid points and derivative orders for 15 real/imaginary cases.
    records = []
    for d in [-3,-1,2,5,13]:
        for a,b,R,S,J in [(4,4,5,3,5),(6,3,6,2,6),(5,4,8,4,8)]:
            check(J*a*b > max(a,b)*(R+S)+2*R*S+max(0,J-max(a,b))*S,
                  "rank_parameters")
            coords = [(x,y,j) for x in range(a) for y in range(b) for j in range(J)]
            keys = [(r,s) for r in range(R) for s in range(S)]
            rows = [[jet({(r,s):1},x,y,j,d) for x,y,j in coords] for r,s in keys]
            G = gram(rows,d)
            det = bareiss(G)
            check(det>0, "quadratic_gram")
            if d == -1:
                phased = [[mul(v,[(1,0),(0,1),(-1,0),(0,-1)][i%4],d)
                           for i,v in enumerate(row)] for row in rows]
                check(gram(phased,d)==G,"phase_gram_control")
            check(det <= product(G[i][i] for i in range(len(G))), "quadratic_gram")
            rec = {"d":d,"a":a,"b":b,"R":R,"S":S,"J":J,
                   "det_sha256":hashlib.sha256(str(det).encode()).hexdigest(),
                   "inert":[]}
            for p in primes(R-1):
                if p==2 or d%p==0 or pow(d%p,(p-1)//2,p)!=p-1:
                    continue
                normalized = []
                total_h = 0
                for r,s in keys:
                    h = min(r//p,S-1-s)
                    total_h += h
                    poly = {(r-p*h,s):1}
                    for _ in range(h):
                        poly = poly_mul(poly,{(p,0):1,(0,1):-1})
                    new = []
                    for at,(x,y,j) in enumerate(coords):
                        direct = jet(poly,x,y,j,d)
                        combine = [0,0]
                        for i in range(h+1):
                            u = rows[(r-p*i)*S+s+i][at]
                            w = (-1)**i*comb(h,i)
                            combine[0] += w*u[0]
                            combine[1] += w*u[1]
                        check(direct==tuple(combine), "full_row_identity")
                        check(direct[0]%(p**h)==0 and direct[1]%(p**h)==0,
                              "full_row_divisibility")
                        new.append((direct[0]//p**h,direct[1]//p**h))
                    normalized.append(new)
                check(bareiss(gram(normalized,d))*p**(2*total_h)==det,
                      "gram_congruence")
                e = template(R,S,p)
                vp = valuation(det,p)
                check(vp>=e, "actual_determinant_valuation")
                rec["inert"].append({"p":p,"valuation":vp,"lower_template":e})
            records.append(rec)

    # Rank is not inferred from dimensions alone: (z-w)^2 annihilates jets.
    rows = [[derivative_coefficient(r,j)*x**(r-j+s) if j<=r else 0
             for x in range(5) for j in range(2)]
            for r in range(3) for s in range(3)]
    G = [[sum(a*b for a,b in zip(u,v)) for v in rows] for u in rows]
    check(bareiss(G)==0,"collapsed_grid_control")

    # Exact large parameter checks; analytic all-R proof is in the manuscript.
    log2lo = 2*sum((Q(1,(2*j+1)*3**(2*j+1)) for j in range(50)),Q(0))
    log2hi = log2lo+Q(9,4*101*3**101)
    for k in [64,80,96,128]:
        R = 2**k
        lo,hi = (k+1)*log2lo,(k+1)*log2hi
        check(ceiling(lo)==ceiling(hi),"balanced_parameters")
        S = R//ceiling(hi)
        for D in [1,2,3,13,R//2,R]:
            a = root4ceil(Q(16*R*R*D))
            b = root4ceil(Q(16*R*R,D))
            check(4*R<=a*b<=9*R and a>=b and a<=S and S<=R//4,
                  "balanced_parameters")
            check(S*a*b > a*(R+S)+2*R*S+(S-a)*S,"balanced_parameters")
            sq = isqrt(D)+(isqrt(D)**2 != D)
            check((a+b*sq)**4 <= 6**4*R*R*D,"balanced_parameters")
    check(Q(1,2)+Q(1,48)==Q(25,48),"prime_sum_coefficient")

    # Complete rational Hermite matrices; derivatives are not divided by j!.
    for N in range(2,7):
        for J in range(1,4):
            V = [[derivative_coefficient(r,j)*a**(r-j) if j<=r else 0
                  for a in range(N) for j in range(J)] for r in range(N*J)]
            exact = product(factorial(j) for j in range(J))**N
            exact *= product((b-a)**(J*J) for a in range(N) for b in range(a+1,N))
            check(bareiss(V)**2==exact**2,"hermite_determinant")
            check(product(m**(N-m) for m in range(1,N))
                  ==product(factorial(m) for m in range(1,N)),"factorial_profile")

    # Complete ordinary-integer desieving, independently via valuations/lcms.
    mu = [0]+[mobius(n) for n in range(1,129)]
    plist = primes(128)
    for n in range(1,129):
        check(sum(mu[m] for m in range(1,n+1) if n%m==0)==(n==1),
              "mobius_inverse")
    for N in range(2,129):
        for p in (p for p in plist if p<=N):
            signed = 0
            for m in range(1,N+1):
                c = abs(mu[m]) if MUTATION=="unsigned" else mu[m]
                for n in range(p,N//m+1):
                    signed += c*(N-m*n)*valuation(n,p)
            target, pk = 0,p
            while pk<=N:
                target += N-pk
                if MUTATION=="prime-powers":
                    break
                pk *= p
            check(signed==target and signed>=0,"primitive_integer")
            lcm_v = sum(max((j for j in range(1,8) if p**j<=r),default=0)
                        for r in range(1,N))
            check(signed==lcm_v,"lcm_identity")

    for N in range(2,33):
        quotient = Q(1)
        for m in range(1,N+1):
            K = N//m
            Bk = product(factorial(k) for k in range(1,K))
            quotient *= Q(Bk**m*factorial(K)**(N-m*K))**mu[m]
        lcm, target = 1,1
        for r in range(1,N):
            lcm = lcm*r//gcd(lcm,r)
            target *= lcm
        check(quotient==target,"factorial_quotient")

    for s in [Q(i,2) for i in range(3,23)]:
        c = Q(0) if MUTATION=="continuum" else Q(1)
        lhs = (Q(1)/(s-1)-2/s+c/(s+1))/2
        check(lhs==1/((s-1)*s*(s+1)),"one_sided_continuum")
        check(1/s-1/(s+1)==1/(s*(s+1)),"mellin_ramp")
    for u in [Q(i,20) for i in range(21)]:
        check(0<=u*(1-u)/2<=Q(1,8),"integer_mesh")
    for m0 in range(5):
        for mc in range(5):
            inert = Q(mc,2) if MUTATION=="common-zero" else Q(mc-m0,2)
            check(inert-Q(mc,2)==-Q(m0,2),"common_zero_residue")
            check(inert-Q(mc+m0,2)==-m0,"split_inert_residues")
    for rho in [Q(3,5),Q(3,4),Q(7,8)]:
        for m in range(1,9):
            used = 1 if MUTATION=="multiplicity" else m
            residue = -used/(rho*(rho+1))
            check(residue*rho*(rho+1)==-m,"zero_multiplicity")
    # Lower bounds cannot be differentiated by subtracting inequalities.
    lower, slack = [0,0,0],[0,100,0]
    actual = [x+y for x,y in zip(lower,slack)]
    check(all(a>=b for a,b in zip(actual,lower)) and actual[2]-2*actual[1]+actual[0]<0,
          "slack_control")
    return {"status":"PASS_FINITE_ONLY","counts":dict(sorted(COUNTS.items())),
            "total_predicates":sum(COUNTS.values()),"quadratic_cases":records,
            "scope":"15 complete quadratic grids; 15 rational Hermite matrices; declared finite integer ranges. No analytic certification, L-values or real zero data."}


def product(xs) -> int:
    out = 1
    for x in xs:
        out *= x
    return out


def main() -> int:
    global MUTATION
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mutate",choices=["hasse","factor-two","unsigned","prime-powers",
                                      "continuum","common-zero","multiplicity"],default="")
    args = ap.parse_args()
    MUTATION = args.mutate
    try:
        out = run()
        print(json.dumps(out,sort_keys=True,indent=2))
        return 0
    except (ValueError,ArithmeticError) as exc:
        print(str(exc),file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
