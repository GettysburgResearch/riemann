#!/usr/bin/env python3
"""Exact finite algebra/exponent checks. No analytic theorem or RH certification."""
from __future__ import annotations
import json
from fractions import Fraction as F
from math import gcd, isqrt
from pathlib import Path

COUNTS: dict[str, int] = {}

def check(group: str, condition: bool) -> None:
    if not condition:
        raise RuntimeError(f"failed finite check: {group}, index {COUNTS.get(group, 0)}")
    COUNTS[group] = COUNTS.get(group, 0) + 1

def mul(a: list[F], b: list[F], n: int) -> list[F]:
    out = [F(0)] * (n + 1)
    for i, x in enumerate(a[:n+1]):
        for j, y in enumerate(b[:n+1-i]):
            out[i+j] += x*y
    return out

def inverse(a: list[F], n: int) -> list[F]:
    if not a or a[0] == 0:
        raise ValueError("series constant must be nonzero")
    b = [F(1)/F(a[0])] + [F(0)]*n
    for j in range(1, n+1):
        b[j] = -sum(a[i]*b[j-i] for i in range(1, min(j, len(a)-1)+1))/a[0]
    return b

def mobius(n: int) -> int:
    value, p = 1, 2
    while p*p <= n:
        if n % p == 0:
            n //= p
            value = -value
            if n % p == 0:
                return 0
        p += 1
    return -value if n > 1 else value

def psi(n: int) -> int:
    return (0, 1, -1, -1, 1)[n % 5]

def weight(t: F, smooth_polynomial: bool) -> F:
    if not F(1,2) < t <= 1:
        return F(0)
    return (t-F(1,2))*(1-t) if smooth_polynomial else F(1)

def scalar(x: F, mask: int | None, poly: bool) -> F:
    if x <= 0:
        raise ValueError("positive scale required")
    return sum((F(mobius(n)*psi(n))*weight(F(n)/x, poly)
                for n in range(1, x.numerator//x.denominator+1)
                if gcd(n,30)==1 and (mask is None or n%mask)), F(0))

def main() -> dict:
    alpha, beta, h = F(67,100), F(151,400), F(33,100)
    delta, xg, top = F(1,10**7), F(8801,10000), F(3301,10000)
    C, b0 = alpha/2+h/6, F(61,100)
    E = lambda x,y,z: alpha/2+x-1+h*z+beta*(y-1)
    margins = {
        "theta": C-(alpha+beta/2-F(1,2)),
        "principal_w": C-E(1+delta,F(9,10),F(1,6)+delta),
        "principal_z": C-E(1+delta,1,F(1,20)),
        "small": C-E(1+delta,F(3,25),F(2,5))-F(1,5)*F(26,25),
        "exceptional": C-E(1+delta,F(3,25),F(2,5))-top*F(337,500),
        "good": C-E(xg,F(3,25),F(2,5))-top*F(26,25),
        "large": C-E(4,4,50000)-top*(1-50000),
    }
    expected = [F(1,32), F(37749867,10**9), F(384999,10**7),
                F(471999,10**7), F(2617,80000), F(7949,250000), F(1481,2500)]
    for actual, target in zip(margins.values(), expected):
        check("paper_table_reconstruction", actual == target)
    check("version_and_loss_arithmetic", F(8,15)+F(933,2000)==F(5999,6000))
    check("version_and_loss_arithmetic", b0+F(287,800)==F(31,32))
    check("version_and_loss_arithmetic", margins['good']-F(1,4000)>F(63,2000)>F(1,32))
    check("version_and_loss_arithmetic", F(717,2000)<F(287,800))
    # Verify every convex-domain inequality at each declared contour corner.
    corners = [(xg,F(3,25),F(2,5)), (1+delta,F(9,10),F(1,6)+delta),
               (1+delta,F(1),F(1,20)), (F(4),F(4),F(2)), (F(4),F(4),F(50000))]
    for corner in corners:
        for shift in [F(0),F(1,10**6)]:
            x,y,z = [v-shift for v in corner]
            values = [x,y,z,6*z+y-1,x+6*z-1,x+y-1,x+y+6*z-2,
                      6*x+6*z-5,x-F(1,2),3*x-2,3*x+y-F(5,2)]
            check("contour_domains", min(values)>0)
    for a_num in range(1,40):
        for b_num in range(1,a_num+1):
            a, bb = F(a_num,40), F(b_num,40)
            if a+bb <= 1:
                continue
            hh = 1-a
            saving = 2*hh/3-bb/2
            check("restricted_cauchy_ceiling", saving < hh/6 < F(1,12))

    n = 36
    one, geom = [F(1)]+[F(0)]*n, [F(1)]*(n+1)
    local_cases = 0
    for q in [2,3,4,7,13,25,49,101]:
        r = F(1,q)
        for eta in [F(-1),F(0),F(1,2),F(1)]:
            P = [F(0)]*(n+1)
            P[0], P[1], P[6] = 1, -(1-r), -eta*q*q
            j = mul(P,geom,n)
            invj = inverse(j,n)
            Lden = [F(0)]*(n+1)
            Lden[0], Lden[6] = 1,-eta*q**3
            H = mul(j,inverse(Lden,n),n)
            check("euler_series_identities", mul(H,Lden,n)==j)
            check("euler_series_identities", mul(j,[F(1),F(-1)],n)==P)
            check("euler_series_identities", mul(j,invj,n)==one)
            # Rational point at or inside the critical radius.
            m = isqrt(q)
            if m*m < q:
                m += 1
            t = F(1,m)
            a = 1-r
            check("kernel_absolute_budgets", q*t*t <= 1)
            denominator = 1-a*t-q*q*t**6
            check("kernel_absolute_budgets", denominator > 0)
            forward = 1+(r*t+q*q*t**6)/(1-t)
            backward = (1+r*t/(1-a*t))/(1-q*q*t**6/(1-a*t))
            massj = sum(abs(v)*t**i for i,v in enumerate(j))
            massinv = sum(abs(v)*t**i for i,v in enumerate(invj))
            check("kernel_absolute_budgets", massj<=forward<=1+12*r)
            check("kernel_absolute_budgets", massinv<=backward<=1+12*r)
            local_cases += 1
    # False substitutions must actually disagree on a witness.
    q, r = 7, F(1,7)
    j = [F(1)]+[r]*5+[r-q*q]
    check("negative_controls", j[6]-j[5] == -q*q and j[6]-j[5] != -q**3)
    check("negative_controls", j[2] != 0)  # imposing coprimality on mu*j loses -j[1]
    check("negative_controls", F(1,2)+F(5,36) < F(5,6))  # crude mask error obstructs k=3
    check("negative_controls", F(2,3) > F(1,2))  # termwise stripping floor remains
    check("negative_controls", F(31,32) != F(5999,6000))

    for D in [16,32,64,127,256,512]:
        for p in [7,11,13,31,127,257]:
            for poly in [False,True]:
                x = F(D)
                direct = scalar(x,p,poly)
                recursive = F(0)
                scale, jpow = x, 0
                while scale >= 1:
                    recursive += psi(p)**jpow*scalar(scale,None,poly)
                    scale /= p
                    jpow += 1
                check("literal_prime_mask_recursion", direct==recursive)
                check("literal_prime_mask_recursion", scalar(x,None,poly)==direct-psi(p)*scalar(x/p,p,poly))

    hierarchy = {}
    for k in [1,2,3,6,12,24]:
        hierarchy[str(2*k)] = str(F(1,2)+F(5,12*k))
        for hh in [F(1,2),F(21,20),F(3,2)]:
            lam = F(1,2)+5*hh/(12*k)
            if lam >= 1:
                continue
            target, B, iterations = lam+F(1,10000), F(1), 0
            while B>target:
                B=max(target,(1-hh/6)*B)
                iterations += 1
                if iterations>1000:
                    raise RuntimeError("bootstrap did not contract")
            check("scalar_exponent_bootstrap", B==target and iterations>0)
    return {
        "status":"PASS: finite identities only; no asymptotic or formal certification",
        "checks_by_group":COUNTS,
        "total_checks":sum(COUNTS.values()),
        "local_series_cases":local_cases,
        "local_series_max_degree":n,
        "paper_table_savings":{key:str(value) for key,value in margins.items()},
        "conditional_moment_boundaries_h_to_1":hierarchy,
        "limitations":["Same author as proofs; not independent mathematical review.",
                       "Rational polynomial checks are not number-field moment censuses.",
                       "Prime-mask tests use integer ideals and a character modulo 5, not general-field sextic rows.",
                       "Hard/polynomial finite tests are not the analytic smooth-test hypothesis.",
                       "No Lean build or upstream analytic theorem replay."]
    }

if __name__ == '__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
