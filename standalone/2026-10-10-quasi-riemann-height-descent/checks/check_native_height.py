#!/usr/bin/env python3
"""Exact finite structural controls for native_height.md.

No zeta values, asymptotic extrapolations, or physical-height trigonometry.
All acceptance gates execute under normal and optimized Python.
"""
from fractions import Fraction as F
import json

count = 0
Z = (F(0), F(0))
ONE = (F(1), F(0))

def check(condition, label):
    global count
    count += 1
    if not condition:
        raise RuntimeError(label)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def mul(a, b):
    return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])

def scale(a, c):
    return (a[0]*c, a[1]*c)

def norm(a):
    return a[0]*a[0] + a[1]*a[1]

def total(xs):
    ans = Z
    for x in xs:
        ans = add(ans, x)
    return ans

def mobius(n):
    mu = [1] * (n + 1)
    mu[0] = 0
    prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if prime[p]:
            for j in range(p, n + 1, p):
                mu[j] *= -1
                if j != p:
                    prime[j] = False
            for j in range(p*p, n + 1, p*p):
                mu[j] = 0
    return mu

def character(n):
    ans = ONE
    for p, v in [(2, (F(0), F(1))), (3, (F(3,5), F(4,5))), (5, (F(-1), F(0)))]:
        while n % p == 0:
            ans = mul(ans, v)
            n //= p
    return ans

def convolution(a, b, n):
    out = [Z] * (n + 1)
    for i in range(1, min(n, len(a)-1) + 1):
        if a[i] == Z:
            continue
        for j in range(1, min(n//i, len(b)-1) + 1):
            if b[j] != Z:
                out[i*j] = add(out[i*j], mul(a[i], b[j]))
    return out

def floor_cuberoot_ratio(a2, b):
    lo, hi = 0, a2 + 1
    while hi - lo > 1:
        mid = (lo + hi)//2
        if b * mid**3 <= a2:
            lo = mid
        else:
            hi = mid
    return lo

def mesh(y):
    b = y + 1
    end = b*b
    a = b
    out = []
    while a < end:
        h = min(end-a, floor_cuberoot_ratio(a*a, b))
        check(h >= 1, "mesh has a positive length")
        out.append((a, h))
        a += h
    check(a == end, "mesh has complete endpoint")
    return out

def run():
    max_y = 31
    nmax = (max_y + 1)**2 - 1
    mu = mobius(nmax)
    chi = [Z] + [character(n) for n in range(1, nmax + 1)]
    check(chi[1] == ONE, "character at one")
    for n in range(1, nmax + 1):
        check(norm(chi[n]) == 1, "unitary character")
        divisor_sum = sum(mu[d] for d in range(1, n + 1) if n % d == 0)
        check(divisor_sum == int(n == 1), "independent divisor inverse")
    for a in range(1, 33):
        for b in range(1, 33):
            if a*b <= nmax:
                check(chi[a*b] == mul(chi[a], chi[b]), "complete multiplicativity")

    ht = [Z] * (nmax + 1)
    pt = [Z] * (nmax + 1)
    mt = [Z] * (nmax + 1)
    for n in range(1, nmax + 1):
        ht[n] = add(ht[n-1], scale(chi[n], F(1,n)))
        pt[n] = add(pt[n-1], chi[n])
        mt[n] = add(mt[n-1], scale(chi[n], F(mu[n],n)))

    for a in range(1, 25):
        for d in range(1, 25):
            r = (a-1)//d
            formula = sub(scale(ht[r], F(a)), scale(pt[r], F(d)))
            direct = total(ht[k//d] for k in range(a))
            check(formula == direct, "twisted harmonic antiderivative")

    panels = []
    for y in [1, 2, 3, 5, 7, 15, 31]:
        b = y + 1
        end = b*b - 1
        g = [Z] + [scale(chi[n], F(mu[n])) for n in range(1, y + 1)]
        z = convolution(g, g, end)
        onez = convolution(chi[:end+1], z, end)
        error = convolution(chi[:end+1], g, end)
        for n in range(1, end + 1):
            native = scale(chi[n], F(mu[n]))
            output = sub(scale(g[n] if n <= y else Z, F(2)), onez[n])
            check(output == native, "coherent Newton complete native square step")
            if n <= y:
                check(error[n] == (ONE if n == 1 else Z), "twisted inverse has zero defect head")
            raw_z = sum(mu[d]*mu[n//d] for d in range(1, n+1)
                        if n % d == 0 and d <= y and n//d <= y)
            check(z[n] == scale(chi[n], F(raw_z)), "twist preserves product coefficients")

        # Actual reciprocal reconstruction on every native cell.
        for k in range(y+1, end+1):
            rhs = scale(mt[y], F(2))
            terms = []
            for d in range(1, min(y*y, k)+1):
                terms.append(scale(mul(z[d], ht[k//d]), F(1,d)))
            rhs = sub(rhs, total(terms))
            check(rhs == mt[k], "coherent reciprocal Newton formula")

        cells = mesh(y)
        budget = sum((F(h*(h*h-1), 12*a*a) for a,h in cells), F(0))
        check(len(cells) < 10*b, "complete block count")
        check(budget < F(5,6), "uniform detail budget")
        for center in [Z, (F(2,3), F(-1,4))]:
            complete = sum((norm(sub(mt[k], center)) for k in range(b, end+1)), F(0))
            coarse = F(0)
            detail = F(0)
            for a,h in cells:
                mean = scale(total(mt[k] for k in range(a,a+h)), F(1,h))
                coarse += h * norm(sub(mean, center))
                local_detail = sum((norm(sub(mt[k], mean)) for k in range(a,a+h)), F(0))
                detail += local_detail
                check(local_detail <= F(h*(h*h-1), 12*a*a), "complex block detail inequality")
                if y <= 7:
                    pair = sum((norm(sub(mt[a+j], mt[a+i]))
                                for i in range(h) for j in range(i+1,h)), F(0))/h
                    check(pair == local_detail, "complex pairwise variance")
            check(complete == coarse + detail, "complete centered covariance identity")
            check(detail <= budget, "complete detail paid")
        panels.append({"Y": y, "last_native_index": end, "blocks": len(cells),
                       "exact_detail_majorant": str(budget)})

    # Product-defect coefficients, computed independently of Newton.
    for y in range(1, 32):
        e = [0]*(y*y + 1)
        for a in range(1,y+1):
            for b in range(1,y+1):
                e[a*b] += mu[a]
        e[1] -= 1
        for n in range(1,y*y + 1):
            if n <= y:
                check(e[n] == 0, "joint product has exact zero head")
            else:
                large = sum(mu[d] for d in range(1,n+1) if n%d == 0 and d>y)
                small = sum(mu[d] for d in range(1,n+1) if n%d == 0 and d*y<n)
                check(e[n] == -large-small, "two exact cutoff boundaries")
                if n <= 2*y:
                    check(e[n] == -1-mu[n], "first collar identity")
            divs = sum(1 for d in range(1,n+1) if n%d == 0)
            check(abs(e[n]) <= divs, "coefficient divisor majorant")

    for a in range(25):
        lhs = (a+1)**2
        rhs = (a+3)*(a+2)*(a+1)//6
        check(lhs <= rhs, "prime-power divisor-square majorant")
        check(rhs-lhs == (a+1)*a*(a-1)//6, "exact divisor-square gap")

    return {"status": "PASS", "explicit_predicates": count,
            "arithmetic": "INTEGER_FRACTION_GAUSSIAN_RATIONAL",
            "structural_character": {"chi_2": "i", "chi_3": "(3+4i)/5", "chi_5": "-1",
                                     "other_primes": "1"},
            "panels": panels,
            "not_run": ["zeta zero evaluations", "infinite analytic moment verification",
                        "physical-height interval arithmetic", "Lean build"]}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
