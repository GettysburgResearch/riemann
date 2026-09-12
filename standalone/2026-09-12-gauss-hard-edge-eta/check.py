#!/usr/bin/env python3
"""Exact finite checks for the proposed Gauss--Thorin hard-edge manuscript.

Python standard library only. No floating arithmetic, zeta evaluator, or zero
list is used. These checks do NOT certify RH or replace the all-order proofs.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

MAX_ORDER = 24
NODE_ORDERS = (8, 32, 64)
BISECTIONS = 55
SCHEMA = 'gauss-hard-edge-eta-v1'


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def trim(p: list[F]) -> list[F]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a: list[F], b: list[F]) -> list[F]:
    p = [F(0)] * max(len(a), len(b))
    for j, v in enumerate(a): p[j] += v
    for j, v in enumerate(b): p[j] += v
    return trim(p)


def scale(p: list[F], a: F, shift: int = 0) -> list[F]:
    return trim([F(0)] * shift + [a * v for v in p])


def mul(a: list[F], b: list[F]) -> list[F]:
    p = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): p[i+j] += x*y
    return trim(p)


def derivative(p: list[F]) -> list[F]:
    return [F(j) * p[j] for j in range(1, len(p))] or [F(0)]


def poch(a: F, n: int) -> F:
    r = F(1)
    for j in range(n): r *= a+j
    return r


def diag(n: int) -> F:
    return F(2, 5) if n == 0 else F(12, (4*n+1)*(4*n+5))


def offsq(n: int) -> F:
    require(n >= 1, 'off-diagonal index must be positive')
    return F(36, (4*n-1)*(4*n+1)**2*(4*n+3))


def shape(m: int) -> F:
    return F(m*(2*m+3), 2)


def beta(m: int) -> F:
    den = 1
    for j in range(1, 4*m+2, 2): den *= j
    return F(6**m, den)


def continuants(n: int) -> tuple[list[list[F]], list[list[F]]]:
    ps, qs = [[F(1)], [F(1), F(2,5)]], [[F(0)], [F(1)]]
    for m in range(1, n):
        ps.append(add(mul([F(1),diag(m)],ps[m]), scale(ps[m-1],-offsq(m),2)))
        qs.append(add(mul([F(1),diag(m)],qs[m]), scale(qs[m-1],-offsq(m),2)))
    return ps[:n+1], qs[:n+1]


def closed_p(m: int) -> list[F]:
    return [F(comb(2*m-j,j))*F(3,2)**j /
            (poch(F(3,2),j)*poch(F(4*m+3-2*j,2),j)) for j in range(m+1)]


def closed_q(m: int) -> list[F]:
    if m == 0: return [F(0)]
    return [F(comb(2*m-1-j,j))*F(3,2)**j /
            (poch(F(5,2),j)*poch(F(4*m+3-2*j,2),j)) for j in range(m)]


def divide_series(numer: list[F], denom: list[F], n: int) -> list[F]:
    require(denom[0] != 0, 'noninvertible formal series')
    out: list[F] = []
    for j in range(n+1):
        v = numer[j] if j < len(numer) else F(0)
        v -= sum((denom[k]*out[j-k] for k in range(1,min(j,len(denom)-1)+1)), F(0))
        out.append(v/denom[0])
    return out


def source_moments(n: int) -> list[F]:
    # S(t)=sinh(sqrt(6t))/sqrt(6t), g=S'/S. Independent of the Jacobi recurrence.
    s = [F(6**j, factorial(2*j+1)) for j in range(n+2)]
    gs = divide_series(derivative(s),s,n)
    return [(-1)**j*v for j,v in enumerate(gs)]


def edge_coeff(m: int, r: int) -> F:
    if r > m: return F(0)
    a = shape(m)
    c = F(2,3)**r/F(factorial(2*r))
    for j in range(r):
        c *= (1-F(j*(2*j+3),2)/a)*(1-F((2*j-1)*(j+1),2)/a)
    return c


def check_order(m: int, ps: list[list[F]], qs: list[list[F]], mu: list[F]) -> dict[str, Any]:
    p, q = ps[m], qs[m]
    require(p == closed_p(m), f'P closed form at {m}')
    require(q == closed_q(m), f'Q closed form at {m}')
    require(all(x > 0 for x in p), f'positive P coefficients at {m}')
    a, b = shape(m), beta(m)
    require(p[-1] == b and q[-1]/b == a, f'shape / leading coefficient at {m}')
    h = F(3)*b*b/F(4*m+3)
    hp = F(1)
    for j in range(1,m+1): hp *= offsq(j)
    require(h == hp, f'norm product at {m}')
    pm = [F((-1)**(m-j))*p[m-j] for j in range(m+1)]
    for j in range(m):
        require(sum((pm[i]*mu[i+j] for i in range(m+1)),F(0)) == 0,
                f'orthogonality at {m},{j}')
    require(sum((pm[i]*mu[i+m] for i in range(m+1)),F(0)) == h, f'norm integral at {m}')
    gs = divide_series(q,p,2*m)
    require(gs[:2*m] == [(-1)**j*mu[j] for j in range(2*m)],f'moment matching at {m}')
    require(mu[2*m]-gs[2*m] == h,f'first error coefficient at {m}')
    # Complete rational Riccati numerator, not a Taylor truncation.
    ric = add(scale(add(mul(derivative(q),p),scale(mul(q,derivative(p)),F(-1))),F(2),1),
              scale(mul(q,p),F(3)))
    ric = add(ric,scale(mul(q,q),F(2),1))
    ric = add(ric,scale(mul(p,p),F(-3)))
    require(ric == [F(0)]*(2*m)+[-3*b*b],f'complete Riccati residual at {m}')
    adj = add(mul(qs[m+1],p),scale(mul(q,ps[m+1]),F(-1)))
    require(adj == [F(0)]*(2*m)+[h],f'adjacent identity at {m}')
    tr = sum((diag(j) for j in range(m)),F(0))
    tr2 = sum((diag(j)**2 for j in range(m)),F(0))+2*sum((offsq(j) for j in range(1,m)),F(0))
    mean, var = F(3,4*m+1), F(18,(4*m-1)*(4*m+1)**2)
    require(1-tr == mean and F(2,5)-tr2 == var, f'thin-tail moments at {m}')
    require(var/mean**2 == F(2,4*m-1),f'thin-tail CV at {m}')
    require(p[-2]/p[-1] == a*(2*a+1)/6,f'inverse-node trace at {m}')
    # Dual polynomial (1 - pm(x)^2/pm(0)^2)/x; no roots or weights are needed.
    sq = scale(mul(pm,pm),F(1)/pm[0]**2)
    dual = [-sq[j] for j in range(1,len(sq))]
    require(sum((v*mu[j] for j,v in enumerate(dual)),F(0)) == a,f'minimal-shape dual at {m}')
    for r in range(m+9):
        ec = edge_coeff(m,r)
        if r <= m:
            require(ec == p[m-r]/(b*a**(2*r)),f'edge product coefficient at {m},{r}')
        base = F(2,3)**r/F(factorial(2*r))
        if r == 0:
            require(ec == 1,'edge normalization')
            continue
        first = F(r*(7-4*r*r),6)
        require(abs(ec-base) <= base*r**3/a,f'first edge bound at {m},{r}')
        require(abs(ec-base*(1+first/a)) <= 2*base*r**6/a**2,f'second edge bound at {m},{r}')
        e = F(r*(2*r+3),2)
        nc = ec*(1-e/a) if r <= m else F(0)
        if r < m:
            require(nc/F(2*r+1) == q[m-1-r]/(b*a**(2*r+1)),
                    f'exact reversed numerator at {m},{r}')
        elif r == m:
            require(nc == 0, f'numerator leading edge cancellation at {m}')
        # Independent coefficient evaluation of the displayed hyperbolic corrections.
        phi_first = -F(2*r*(2*r-1),4)+r-F(2*r*(2*r-1)*(2*r-2),12)
        psi_first = -F((2*r+1)*(2*r),4)-F((2*r+1)*(2*r)*(2*r-1),12)
        require(phi_first == first, f'phi hyperbolic correction at {m},{r}')
        require(psi_first == first-e, f'psi hyperbolic correction at {m},{r}')
        require(abs(nc-base*(1+(first-e)/a)) <= 5*base*r**6/a**2,
                f'numerator edge bound at {m},{r}')
    return {'m':m, 'shape':str(a), 'beta':str(b), 'h':str(h), 'd':str(h/F(2*m+1)),
            'tail_mean':str(mean),'tail_variance':str(var)}


def sturm_count(m: int, scaled_point: F) -> int:
    # LDL inertia of J_m - scaled_point/A_m^2. Off-diagonals enter squared.
    x = scaled_point/shape(m)**2
    pivot = diag(0)-x
    require(pivot != 0,'zero LDL pivot; use a different rational endpoint')
    count = int(pivot < 0)
    for j in range(1,m):
        pivot = diag(j)-x-offsq(j)/pivot
        require(pivot != 0,'zero LDL pivot; use a different rational endpoint')
        count += int(pivot < 0)
    return count


def isolate(m: int, j: int) -> dict[str, Any]:
    brackets = ((F(0),F(5)),(F(5),F(40)),(F(40),F(110)))
    lo,hi = brackets[j-1]
    require(sturm_count(m,lo)==j-1 and sturm_count(m,hi)==j,'initial root bracket')
    for _ in range(BISECTIONS):
        mid=(lo+hi)/2
        n=sturm_count(m,mid)
        require(n in (j-1,j),'unexpected extra root')
        if n==j-1: lo=mid
        else: hi=mid
    require(sturm_count(m,lo)==j-1 and sturm_count(m,hi)==j,'final root bracket')
    return {'m':m,'j':j,'variable':'A_m^2 times j-th smallest quadrature node',
            'lower':str(lo),'upper':str(hi),'count_below_lower':j-1,'count_below_upper':j}


def build_record() -> dict[str, Any]:
    ps,qs=continuants(MAX_ORDER+1)
    mu=source_moments(2*MAX_ORDER+2)
    rows=[check_order(m,ps,qs,mu) for m in range(1,MAX_ORDER+1)]
    nodes=[isolate(m,j) for m in NODE_ORDERS for j in (1,2,3)]
    return {'schema':SCHEMA,'scope':'finite rational identities and finite Jacobi-node counts; NOT xi-zero certification',
            'max_order':MAX_ORDER,'bisections':BISECTIONS,'orders':rows,'nodes':nodes}


def canonical(x: Any) -> str:
    return json.dumps(x,sort_keys=True,separators=(',',':'),allow_nan=False)


def verify_record(record: Any) -> None:
    require(canonical(record)==canonical(build_record()),'result record does not match exact reconstruction')


def strict_json(text: str) -> Any:
    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        out: dict[str, Any] = {}
        for key, value in items:
            require(key not in out, f'duplicate JSON key: {key}')
            out[key] = value
        return out
    def invalid_constant(value: str) -> Any:
        raise ValueError(f'nonfinite JSON constant: {value}')
    return json.loads(text, object_pairs_hook=pairs, parse_constant=invalid_constant)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write',type=Path,help='produce a fresh exact result record')
    parser.add_argument('--check',type=Path,default=Path(__file__).with_name('results.json'))
    args=parser.parse_args()
    if args.write:
        args.write.write_text(json.dumps(build_record(),indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print(f'WROTE {args.write.name}: exact finite checks passed')
    else:
        verify_record(strict_json(args.check.read_text(encoding='utf-8')))
        print('PASS: exact reconstruction, all finite checks, and all nine quadrature-node counts')
    return 0

if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f'REJECT: {exc}')
