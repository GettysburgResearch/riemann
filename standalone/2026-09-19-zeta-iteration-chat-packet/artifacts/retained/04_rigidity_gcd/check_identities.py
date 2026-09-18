#!/usr/bin/env python3
"""Small exact checks for the reflection/GCD research note.

These check finite identities and a counterexample to mixing two inner
products. They do not test RH or establish an asymptotic estimate.
Uses only the Python standard library.
"""
from __future__ import annotations
from fractions import Fraction as F
from math import gcd, lcm
import json
from pathlib import Path


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def mu(n: int) -> int:
    fs = factor(n)
    return 0 if any(a > 1 for a in fs.values()) else (-1) ** len(fs)


def phi(n: int) -> int:
    return sum(gcd(a, n) == 1 for a in range(1, n + 1))


def j2(n: int) -> int:
    return sum(mu(n // d) * d * d for d in divisors(n))


def b(n: int, k: int) -> F:
    return F(k % n, n)


def atom(d: int, k: int) -> int:
    # s_d = sum_{n|d} mu(d/n) n b_n; b_1 is identically zero.
    return sum(mu(d // n) * (k % n) for n in divisors(d))


def ramanujan(d: int, k: int) -> int:
    return sum(n * mu(d // n) for n in divisors(gcd(d, k)))


def log_interval(r: int, terms: int = 36) -> tuple[F, F]:
    """Rational enclosure from the atanh series, for integer r>1."""
    if r <= 1 or terms < 1:
        raise ValueError('Require r>1 and terms>=1')
    u = F(r - 1, r + 1)
    lower = 2 * sum((u ** (2*j + 1) / (2*j + 1)
                     for j in range(terms)), F(0))
    tail_bound = 2*u**(2*terms + 1) / ((2*terms + 1)*(1-u*u))
    return lower, lower + tail_bound


def exact_checks(max_n: int = 8) -> dict:
    moment_checks = 0
    for d in range(2, max_n + 1):
        for k in range(0, 2*max_n + 1):
            assert sum(atom(q, k) for q in divisors(d) if q >= 2) == d*b(d, k)
            if k:
                assert atom(d, k)-atom(d, k-1) == -ramanujan(d, k)
        # <1,s_d> = sum mu(d/n)log n: check logarithm prime exponents.
        exponents: dict[int, int] = {}
        for n in divisors(d):
            for p, a in factor(n).items():
                exponents[p] = exponents.get(p, 0) + mu(d//n)*a
        exponents = {p: a for p, a in exponents.items() if a}
        fs = factor(d)
        expected = {next(iter(fs)): 1} if len(fs) == 1 else {}
        assert exponents == expected
        for e in range(2, max_n + 1):
            period = lcm(d, e)
            sd = [atom(d, k) for k in range(period)]
            se = [atom(e, k) for k in range(period)]
            md, me = F(sum(sd),period), F(sum(se),period)
            assert md == F(phi(d),2)
            assert me == F(phi(e),2)
            covariance = F(sum(a*z for a,z in zip(sd,se)),period)-md*me
            assert covariance == (F(j2(d),12) if d == e else F(0))
            # Original discrete covariance.
            cov_b = sum((b(d,k)*b(e,k) for k in range(period)),F(0))/period
            cov_b -= F(d-1,2*d)*F(e-1,2*e)
            assert cov_b == F(gcd(d,e)**2-1,12*d*e)
            moment_checks += 1

    bulk = []
    for N in range(2, max_n+1):
        S = sum((F(phi(d)**2,j2(d)) for d in range(2,N+1)), F(0))
        den = 1+3*S
        y = {d: 6*F(phi(d),j2(d))/den for d in range(2,N+1)}
        coeff = {n: n*sum((mu(d//n)*y[d] for d in range(n,N+1,n)), F(0))
                 for n in range(2,N+1)}
        P = lcm(*range(2,N+1))
        residual = []
        for k in range(P):
            A1 = sum((y[d]*atom(d,k) for d in y),F(0))
            A2 = sum((coeff[n]*b(n,k) for n in coeff),F(0))
            assert A1 == A2
            residual.append(1-A1)
        error = sum((r*r for r in residual),F(0))/P
        assert error == 1/den
        for d in y:
            assert sum((residual[k]*atom(d,k) for k in range(P)),F(0)) == 0
        bulk.append({'N':N,'periodic_optimum_exact':str(error)})

    # N=3: combine periodic Gram with the wrong (RH-weighted) source.
    a,A = log_interval(2)
    b0,B = log_interval(3)
    qlo = (20*a*a - 12*A*B + 6*b0*b0)/7
    qhi = (20*A*A - 12*a*b0 + 6*B*B)/7
    assert qlo > F(11018,10000)
    assert qhi < F(11019,10000)
    return {
        'status':'all exact checks passed; no RH conclusion',
        'max_denominator':max_n,
        'pairwise_exact_moment_checks':moment_checks,
        'bulk_optimum_checks':bulk,
        'N3_mixed_metric_projection_q_interval_exact':[str(qlo),str(qhi)],
        'N3_mixed_metric_projection_q_decimal_display':[float(qlo),float(qhi)],
        'N3_false_squared_distance_decimal_display':[float(1-qhi),float(1-qlo)],
        'rigorous_simple_enclosure':'1.1018 < q < 1.1019, hence -0.1019 < 1-q < -0.1018',
        'log_enclosure_method':'36-term rational atanh series with rigorous geometric tail',
    }


if __name__ == '__main__':
    result = exact_checks()
    target = Path(__file__).with_name('exact_checks.json')
    target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(result['status'])
    print(result['rigorous_simple_enclosure'])
    print('saved:',target)
