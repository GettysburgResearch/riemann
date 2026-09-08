#!/usr/bin/env python3
"""Finite exact controls only; NOT a machine proof of the analytic limits.

Uses Python's standard library. Checks are explicit exceptions, not assertions,
so optimization cannot disable them. Stored status flags are not accepted alone.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
# Literal SHA-256 identities of the exact source texts used by this checker.
SOURCE_SHA256: dict[str, str] = {'PROOF.md': 'e15e87fedbc3921345778dfa684cbb9ae895b05c05e1e027b1331713ff0788d5', 'ENDPOINT_DEFECT.md': '98bf9c174c6dcb5c8f93f108fa51bf864bbdf667276c10653f979ca89bcc6e1c', 'README.md': '036dd6df5335cb1c9096b8649938b72c6bd255b605c094657fbcdfdb482abf8a', 'SOURCE_LOCK.json': '9850d58448457c0f2f49f440d754635576cb3b554a9bdaeddc24f08581bf7156'}
BASE = '513d8f206bb597747afcb7a7410cdf768519d548'
COUNTS: Counter[str] = Counter()


def check(group: str, value: bool, context: str = '') -> None:
    if not value:
        raise ValueError(f'control failed: {group}: {context}')
    COUNTS[group] += 1


def trim(p: list[F]) -> list[F]:
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [F(0)]


def add(p: list[F], q: list[F]) -> list[F]:
    return trim([(p[i] if i < len(p) else F(0)) +
                 (q[i] if i < len(q) else F(0))
                 for i in range(max(len(p), len(q)))])


def scale(p: list[F], a: F) -> list[F]:
    return trim([a*x for x in p])


def mul(p: list[F], q: list[F]) -> list[F]:
    out = [F(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def deriv(p: list[F]) -> list[F]:
    return trim([i*p[i] for i in range(1, len(p))])


def int_exp(p: list[F], rate: int = 2) -> F:
    return sum((a*F(factorial(i), rate**(i+1))
                for i, a in enumerate(p)), F(0))


def laguerre(j: int, alpha: int, argument_scale: int = 2) -> list[F]:
    return [F((-argument_scale)**k*comb(j+alpha, j-k), factorial(k))
            for k in range(j+1)]


def unnormalized_basis(r: int, j: int) -> list[F]:
    return [F(0)]*r+laguerre(j, 2*r)


def differential_H(p: list[F], r: int) -> list[F]:
    # H_r(e^-t p)=e^-t[-t p''+(2t-1)p'+p+r^2 p/t].
    if p[0] != 0:
        raise ValueError('test polynomial is not divisible by t')
    return add(add(scale([F(0)]+deriv(deriv(p)), F(-1)),
                   mul([F(-1),F(2)], deriv(p))),
               add(p, scale(p[1:], F(r*r))))


def u_polynomial(j: int) -> list[F]:
    if j < 2:
        raise ValueError('j must be at least two')
    return [F(0)]*(j-2)+[F(1,factorial(j-2)), F(-1,factorial(j-1))]


def gram_u(j: int, k: int) -> F:
    a, b = j-1, k-1
    return F(factorial(a+b-2), 2**(a+b-1)*factorial(a-1)*factorial(b-1))*F(a+b-(a-b)**2, 4*a*b)


def solve(a: list[list[Any]], b: list[Any]) -> list[Any]:
    n = len(b)
    if len(a) != n or any(len(row) != n for row in a):
        raise ValueError('matrix dimension mismatch')
    mat = [list(row)+[val] for row, val in zip(a,b)]
    for i in range(n):
        pivot = next((k for k in range(i,n) if mat[k][i] != 0), None)
        if pivot is None:
            raise ValueError('singular matrix')
        mat[i], mat[pivot] = mat[pivot], mat[i]
        z = mat[i][i]
        mat[i] = [x/z for x in mat[i]]
        for k in range(n):
            if k != i:
                z = mat[k][i]
                mat[k] = [x-z*y for x,y in zip(mat[k],mat[i])]
    return [row[-1] for row in mat]


def det(a: list[list[F]]) -> F:
    if not a:
        return F(1)
    if len(a)==1:
        return a[0][0]
    return sum(((-1)**j*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]])
                for j in range(len(a))), F(0))


@dataclass(frozen=True)
class C:
    re: F = F(0)
    im: F = F(0)
    @staticmethod
    def of(z: Any) -> C:
        return z if isinstance(z,C) else C(F(z))
    def __add__(self, other: Any) -> C:
        z=self.of(other); return C(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self) -> C:
        return C(-self.re,-self.im)
    def __sub__(self, other: Any) -> C:
        return self+-self.of(other)
    def __rsub__(self, other: Any) -> C:
        return self.of(other)+-self
    def __mul__(self, other: Any) -> C:
        z=self.of(other); return C(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def __truediv__(self, other: Any) -> C:
        z=self.of(other); norm=z.re*z.re+z.im*z.im
        if norm==0: raise ZeroDivisionError
        return self*C(z.re/norm,-z.im/norm)
    def __rtruediv__(self, other: Any) -> C:
        return self.of(other)/self
    def __pow__(self, n: int) -> C:
        if n<0: return (C(F(1))/self)**(-n)
        out=C(F(1)); z=self
        while n:
            if n&1: out=out*z
            z=z*z; n//=2
        return out
    def __eq__(self, other: Any) -> bool:
        try: z=self.of(other)
        except (ValueError,TypeError): return False
        return self.re==z.re and self.im==z.im
    def real(self) -> F:
        if self.im!=0: raise ValueError('not exactly real')
        return self.re


def source_authenticate() -> None:
    if len(SOURCE_SHA256) != 4:
        raise ValueError('source lock has not been populated')
    for name,digest in SOURCE_SHA256.items():
        if sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
            raise ValueError('source authentication failed: '+name)


def no_duplicates(pairs: list[tuple[str,Any]]) -> dict[str,Any]:
    out={}
    for k,v in pairs:
        if k in out: raise ValueError('duplicate JSON key: '+k)
        out[k]=v
    return out


def strict_json(path: Path) -> Any:
    return json.loads(path.read_text(),object_pairs_hook=no_duplicates)


def typed_equal(a: Any, b: Any) -> bool:
    if type(a) is not type(b): return False
    if isinstance(a,dict): return a.keys()==b.keys() and all(typed_equal(a[k],b[k]) for k in a)
    if isinstance(a,list): return len(a)==len(b) and all(typed_equal(x,y) for x,y in zip(a,b))
    return a==b


def reconstruct() -> dict[str,Any]:
    COUNTS.clear()
    for r in range(1,6):
        polys=[unnormalized_basis(r,j) for j in range(7)]
        for j,p in enumerate(polys):
            check('laguerre_differential', differential_H(p,r)==scale(p,F(2*j+2*r+1)), f'{r},{j}')
            coeff=int_exp(p); norm=int_exp(mul(p,p))
            expected=F(r*r*factorial(j+r-1)**2,2*factorial(j)*factorial(j+2*r))
            check('exponential_coefficient',coeff*coeff/norm==expected,f'{r},{j}')
            for k,q in enumerate(polys):
                expected=F(factorial(j+2*r),2**(2*r+1)*factorial(j)) if j==k else F(0)
                check('laguerre_orthogonality',int_exp(mul(p,q))==expected,f'{r},{j},{k}')
        for n in range(7):
            capture=F(0)
            for j,p in enumerate(polys[:n+1]):
                coeff=int_exp(p)
                norm=int_exp(mul(p,p))
                capture+=2*coeff*coeff/norm
            product=F(1)
            for j in range(1,r+1): product*=F(n+j,n+r+j)
            closed=F(factorial(n+r)**2,factorial(n)*factorial(n+2*r))
            check('exact_projection_product',capture==product==closed,f'{r},{n}')
            upper=sum((F(r,n+j) for j in range(1,r+1)),F(0))
            lower=sum((F(r,n+r+j) for j in range(1,r+1)),F(0))
            check('log_product_bounds',upper<=F(r*r,n+1) and lower>=F(r*r,n+2*r))
            if n<=4:
                gram=[[F(factorial(2*r+i+j),2**(2*r+i+j+1)) for j in range(n+1)] for i in range(n+1)]
                overlaps=[F(factorial(r+i),2**(r+i+1)) for i in range(n+1)]
                solution=solve(gram,overlaps)
                check('independent_raw_projection',2*sum((x*y for x,y in zip(solution,overlaps)),F(0))==closed)
    for j in range(3,13):
        p=u_polynomial(j)
        check('endpoint_zero',int_exp(p,1)==0,f'{j}')
        # T=I-V is A/(A+1) in Laplace coordinates, checked at rational probes.
        for a in [F(1),F(2,3),F(7,2)]:
            lap=sum((v*F(factorial(k))/(a+1)**(k+1) for k,v in enumerate(p)),F(0))
            check('causal_transform',lap==a/(a+1)**j)
        for k in range(3,13):
            check('inherited_metric',int_exp(mul(p,u_polynomial(k)))==gram_u(j,k),f'{j},{k}')
    for r in range(1,6):
        for n in range(5):
            p=laguerre(n,2*r)
            wpoly=[F(0)]*(2*r)+mul(p,p)
            I=int_exp(wpoly); J=int_exp(wpoly[1:])
            energy=int_exp([F(0)]*(2*r+1)+mul(deriv(p),deriv(p)))
            check('finite_energy',energy==2*n*I and r*r*J<=2*(n+r)*I)
    atoms=[C(F(10)),C(F(20)),C(F(30)),C(F(1000),F(1)),C(F(1000),F(-1))]
    theta=6*(1+F(31,1000))**4*F(31,10)**4*F(1000**3,10**2)*F(31,1000)**10
    check('all_gap_reservoir_constant',theta<F(1,100000))
    check('source_strip_budget',sum((1/z.re for z in atoms),F(0))==F(139,750) and all(z.im*z.im<=z.re for z in atoms))
    witness_records=[]
    for m in [3,4,5,8,12]:
        A=[[z/(z+1)**m*(1/(z+1))**j for j in range(5)] for z in atoms]
        coeff=[x.real() for x in solve(A,[C(),C(),C(),C(F(0),F(1)),C(F(0),F(-1))])]
        vals=[sum((a*c for a,c in zip(row,coeff)),C()) for row in A]
        check('synthetic_interpolation',vals==[C(),C(),C(),C(F(0),F(1)),C(F(0),F(-1))])
        value=sum((z*z for z in vals),C()).real()
        check('synthetic_negative_value',value==-2)
        q=[]
        for j in range(5):
            row=[]
            for k in range(5):
                N=2*m+j+k
                raw=sum((z*z/(z+1)**N for z in atoms),C()).real()
                moments=[sum((1/(z+1)**l for z in atoms),C()).real() for l in [N-2,N-1,N]]
                check('safe_moment_compiler',raw==moments[0]-2*moments[1]+moments[2])
                row.append(raw)
            q.append(row)
        check('synthetic_matrix_sign',det(q)<0 and all(x>0 for row in q for x in row))
        norm=sum((coeff[j]*coeff[k]*gram_u(m+j,m+k) for j in range(5) for k in range(5)),F(0))
        check('synthetic_metric_norm',norm>0)
        witness_records.append({'m':m,'quadratic_value':'-2','metric_norm':str(norm)})
    for indices in [[5,6,7],[5,8,14],[7,12,25]]:
        q3=[[sum((z*z/(z+1)**(j+k) for z in atoms),C()).real() for k in indices] for j in indices]
        check('three_sparse_countercontrol',q3[0][0]>0 and det([row[:2] for row in q3[:2]])>0 and det(q3)>0)
    endpoint_records=[]
    elo=sum((F(1,factorial(j)) for j in range(33)),F(0))
    ehi=elo+F(1,32*factorial(32))
    for r in [1,2,3]:
        m=r+2; d=r*r; js=list(range(m,m+d+1))
        gram=[[gram_u(j,k) for k in js] for j in js]
        v=[F(1,2**j)*(sum((F(1,factorial(l)) for l in range(j-1)),F(0))-F(1,factorial(j-1))) for j in js]
        coef=solve(gram,v)
        theta=sum((x*y for x,y in zip(v,coef)),F(0))
        check('endpoint_projection_geometry',0<theta<elo/2)
        # Incomplete Gamma identity: coefficients of the common e^-1 factor.
        for j,vj in zip(js,v):
            poly=u_polynomial(j)
            independent=sum((a*F(factorial(k),2**(k+1))*sum((F(1,factorial(l)) for l in range(k+1)),F(0)) for k,a in enumerate(poly)),F(0))
            check('incomplete_gamma_overlap',vj==independent)
        lo=(elo/2-theta)/(ehi*ehi); hi=(ehi/2-theta)/(elo*elo)
        check('endpoint_error_enclosure',0<lo<hi)
        endpoint_records.append({'r':r,'dimension':d+1,'theta_r':str(theta),'epsilon_squared_lower':str(lo),'epsilon_squared_upper':str(hi)})
    check('finite_tail_sufficient_constant',F(108,625)+F(3840050,10**7)<1)
    check('continuous_error_constant',F(76,2)+8<50)
    # Rational calibration only. No numerical special functions or limit acceptance.
    calibration=[]
    for r,n in [(1,1),(2,4),(4,16),(8,64),(16,256),(32,1024)]:
        q=F(1)
        for j in range(1,r+1): q*=F(n+j,n+r+j)
        check('critical_calibration',0<q<1)
        calibration.append({'r':r,'n':n,'exact_capture_fraction':str(q)})
    return {'status':'PASS_FINITE_EXACT_CONTROLS','arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
            'base_commit':BASE,'groups':dict(sorted(COUNTS.items())),
            'distinct_controls':sum(COUNTS.values()),'calibration':calibration,
            'synthetic_witnesses':witness_records,'endpoint_geometry':endpoint_records,'actual_xi_matrix_evaluated':False,
            'analytic_limits_machine_proved':False,'rh_proved':False}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    source_authenticate()
    data=reconstruct()
    if args.check is not None and not typed_equal(strict_json(args.check),data):
        raise ValueError('saved result mismatch (including exact types)')
    print(json.dumps(data,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
