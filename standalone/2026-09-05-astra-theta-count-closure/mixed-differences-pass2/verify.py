#!/usr/bin/env python3
"""Bounded exact controls for PR790 mixed-difference pass 2.

Standard-library rational arithmetic only. No zero census, floating point,
prime sweep, analytic proof certification, or inference of RH. --check
compares a freshly reconstructed result with the complete retained JSON.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import json
from math import comb, factorial
from pathlib import Path

G = tuple[F, F]
ZERO: G = (F(0), F(0))
ONE: G = (F(1), F(0))

def g(x: int | F, y: int | F = 0) -> G:
    return F(x), F(y)

def add(z: G, w: G) -> G:
    return z[0] + w[0], z[1] + w[1]

def neg(z: G) -> G:
    return -z[0], -z[1]

def sub(z: G, w: G) -> G:
    return add(z, neg(w))

def mul(z: G, w: G) -> G:
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

def scale(z: G, x: F | int) -> G:
    return z[0]*x, z[1]*x

def norm2(z: G) -> F:
    return z[0]**2+z[1]**2

def div(z: G, w: G) -> G:
    q = norm2(w)
    if q == 0:
        raise ZeroDivisionError("rational complex division by zero")
    return mul(z, (w[0]/q, -w[1]/q))

def power(z: G, n: int) -> G:
    if n < 0:
        return power(div(ONE, z), -n)
    r = ONE
    while n:
        if n & 1:
            r = mul(r, z)
        z = mul(z, z)
        n >>= 1
    return r

def total(terms) -> G:
    result = ZERO
    for z in terms:
        result = add(result, z)
    return result

def multiply(a: list[F], b: list[F], degree: int) -> list[F]:
    c = [F(0)]*(degree+1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i+j <= degree:
                c[i+j] += x*y
    return c

def binomial_series(exponent: F, degree: int) -> list[F]:
    c = [F(1)]
    for k in range(1, degree+1):
        c.append(c[-1]*(exponent-k+1)/k)
    return c

def exp_series(f: list[F], degree: int) -> list[F]:
    if f[0] != 0:
        raise ValueError("exp_series requires zero constant")
    c = [F(1)]+[F(0)]*degree
    for n in range(1, degree+1):
        c[n] = sum(F(k)*f[k]*c[n-k] for k in range(1,n+1))/n
    return c

def kernel_ladder(b: int, depth: int) -> list[dict[tuple[int,int], F]]:
    p = {(2*j-1, 0): F(comb(b,j))*(-F(1,4))**(b-j)
         for j in range(b+1)}
    out = [p]
    for _ in range(depth):
        q: dict[tuple[int,int], F] = {}
        for (r, ell), value in p.items():
            for key, c in (((r-2,ell), F(r,2)*value),
                           ((r-1,ell+1), -value/2)):
                q[key] = q.get(key,F(0))+c
        p = {key: val for key,val in q.items() if val}
        out.append(p)
    return out

def evaluate_kernel(p, r: F, ell: F) -> F:
    return sum(c*r**i*ell**j for (i,j),c in p.items())

def run() -> dict:
    counts: Counter[str] = Counter()
    def check(group: str, ok: bool) -> None:
        if not ok:
            raise ArithmeticError(f"failed exact control: {group}")
        counts[group] += 1

    e_lower = F(163,60)
    check("heat_constants", sum(F(1,factorial(j)) for j in range(6)) == e_lower)
    constants = [F(20000)*F(2500,49)**k*F(60,163)**97 for k in range(23)]
    for k,c in enumerate(constants):
        check("heat_constants", 0 < c < F(3,5))
        if k <= 20:
            check("heat_constants", c < F(1,4096))
        check("heat_constants", -100+F(226,100)+F(k,20000)<-97)
        check("heat_constants", 2*(k+1)<100)
        for z in (F(100), F(101), F(200)):
            ratio = sum(F(factorial(k+1),factorial(k+1-j))/z**j
                        for j in range(k+2))
            check("integer_gamma_tail", 1 <= ratio < 2)

    r = F(227,10000)*F(197,196)**100
    check("small_ratio_cone", 0<r<1)
    check("small_ratio_cone", F(3,2)*227*r*r<F(1,2))
    check("phase_modulus", (1+F(3,20000))**2<F(100,99))
    check("zero_reservoir", F(888,1000)*4-F(278,1000)*2-F(2512,1000)>0)
    check("zero_reservoir", F(888,1000)-F(278,4000)>0)
    check("zero_reservoir", F(100,6)>9)
    col = F(20000)*75**20*F(60,163)**99
    q = F(300)*F(60,163)**19
    check("column_wedge_constants", col<F(1,10))
    check("column_wedge_constants", q<F(1,8000))
    check("column_wedge_constants", 4*q<1)
    for n in range(1,65):
        check("column_wedge_constants", n*n<=4**(n-1))
        check("column_wedge_constants", F(n+2,20*n)<F(99,100))

    # Source-faithful strip geometry at exact rational beta and gamma inputs.
    for height in (F(100),F(101),F(1000)):
        for beta in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
            atom = g(height**2+beta*(1-beta), height*(1-2*beta))
            check("atom_geometry", norm2(atom)<=(height**2+F(1,2))**2)
            for v in (F(1),F(3,4),F(10)):
                k = div(g(v), add(g(v),atom))
                check("atom_geometry", norm2(sub(ONE,k))<1)

    # Root-free recurrence for the parent's three-factor polynomial model.
    model = [g(1),g(2,1),g(2,-1)]
    kappas = [div(ONE,add(ONE,a)) for a in model]
    w = [F(2),F(3,5)]
    for n in range(2,102):
        w.append(F(3,5)*w[-1]-F(1,10)*w[-2])
    p = [F(0)]+[F(1,2)**n+w[n] for n in range(1,102)]
    for n in range(1,25):
        check("model_power_sum", total(power(k,n) for k in kappas)==g(p[n]))
    def H(a: int,b: int) -> F:
        return sum((-1)**j*comb(b,j)*p[a+j+1] for j in range(b+1))
    witness = H(0,14)
    check("mixed_counterexample", witness==-F(433316717939,10**15))
    for a in range(8):
        for b in range(8):
            direct=total(mul(power(k,a+1),power(sub(ONE,k),b)) for k in kappas)
            check("mixed_atom_identity", direct==g(H(a,b)))

    z = g(F(4,5),F(3,5))
    check("phase_counterexample", norm2(z)==1)
    bases=[add(sub(ONE,k),mul(k,z)) for k in kappas]
    expected=[g(F(9,10),F(3,10)),g(1,F(1,5)),g(F(22,25),F(4,25))]
    for base,expected_base,sq in zip(bases,expected,(F(9,10),F(26,25),F(4,5))):
        check("phase_counterexample", base==expected_base)
        check("phase_counterexample", norm2(base)==sq)
    z_points=[g(1),g(-1),g(0,1),z]
    for N in list(range(21))+[30,50,100]:
        row=[F(comb(N,a))*H(a,N-a) for a in range(N+1)]
        variation=sum(abs(x) for x in row)
        debt=sum(max(F(0),-x) for x in row)
        check("row_conservation", sum(row)==p[1])
        check("row_conservation", variation==p[1]+2*debt)
        for zz in z_points:
            poly=total(scale(power(zz,a),value) for a,value in enumerate(row))
            atoms=total(mul(k,power(add(sub(ONE,k),mul(k,zz)),N)) for k in kappas)
            binomial=total(scale(power(sub(zz,ONE),j),comb(N,j)*p[j+1])
                           for j in range(N+1))
            check("row_three_reconstructions", poly==atoms==binomial)
            check("row_circle_bound", norm2(poly)<=variation**2)
        if N==100:
            last_variation=variation
            last_debt=debt
            q100=total(mul(k,power(base,N)) for k,base in zip(kappas,bases))
            check("row_exponential_witness", norm2(q100)>p[1]**2)
            check("row_exponential_witness", debt>0)

    # The Laguerre integral is evaluated exactly after integrating monomials.
    for v in (F(1),F(2),F(3,4)):
        for atom in model:
            c=add(ONE,scale(atom,1/v))
            k=div(ONE,c)
            for N in range(8):
                integral=total(scale(div(power(sub(z,ONE),j),power(c,j+1)),comb(N,j))
                               for j in range(N+1))
                expected=mul(k,power(add(sub(ONE,k),mul(k,z)),N))
                check("laguerre_atom_integral", integral==expected)

    # Independent Taylor expansion versus the Laurent recurrence (10.4).
    degree=6
    root=binomial_series(F(1,2),degree)
    invroot=binomial_series(F(-1,2),degree)
    for b in range(5):
        kernels=kernel_ladder(b,degree)
        u_power=[F(comb(b,j))*F(3,4)**(b-j) if j<=b else F(0)
                 for j in range(degree+1)]
        for ell in (F(0),F(1),F(2)):
            exponent=[F(0)]+[-ell*x for x in root[1:]]
            jet=multiply(multiply(u_power,invroot,degree),exp_series(exponent,degree),degree)
            for m in range(degree+1):
                actual=evaluate_kernel(kernels[m],F(1),ell)
                check("prime_kernel_taylor", factorial(m)*jet[m]==actual)
    k11=kernel_ladder(1,1)[1]
    check("prime_kernel_sign", evaluate_kernel(k11,F(1),F(1))==F(1,4))
    check("prime_kernel_sign", evaluate_kernel(k11,F(1),F(2))==-F(1,8))
    check("prime_kernel_sign", 3**5<7**3)

    return {
        "status":"PASS_EXACT_MIXED_DIFFERENCE_PASS2",
        "arithmetic":"EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "groups":dict(sorted(counts.items())),
        "total_checks":sum(counts.values()),
        "witnesses":{
            "model_H_0_14":str(witness),
            "model_p1":str(p[1]),
            "model_phase":"(4+3i)/5",
            "unique_dominant_base":"1+i/5",
            "dominant_base_norm_squared":"26/25",
            "N100_circle_modulus_exceeds_mass":True,
            "N100_negative_row_mass_positive":True,
            "heat_C22_less_than":"3/5",
            "heat_C20_less_than":"1/4096",
            "column_ratio_less_than":"1/10",
            "wedge_ratio_less_than":"1/10"
        },
        "zero_census_executed":False,
        "analytic_theorems_machine_proved":False,
        "unrestricted_mixed_inequality_proved":False,
        "rh_proved":False
    }

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",type=Path)
    args=parser.parse_args()
    result=run()
    if args.check is not None:
        expected=json.loads(args.check.read_text(encoding="utf-8"))
        if expected!=result:
            raise SystemExit("FAIL: retained result differs from exact reconstruction")
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
