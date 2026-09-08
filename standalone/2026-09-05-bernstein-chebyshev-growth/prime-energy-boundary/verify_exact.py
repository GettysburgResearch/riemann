#!/usr/bin/env python3
"""Finite exact controls, not a proof of PNT, an infinite norm, or RH."""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import sys
from typing import Any

ROOT = Path(__file__).resolve().parent
PARENT_COMMIT = "3b1bb5b81b36f742b6d5840088bf79a8e1519084"
PARENT_BLOBS = {
    "GROWTH.md": "c19930a24cefb6d5543098b9958f47a1d71acd87",
    "arithmetic-laguerre/PROOF.md": "aff32d3b2078c3c895bd77f02e71fbe1fcfc3b49",
    "higher-prime-powers/PROOF.md": "fb27a2d0162034ef6588a171b1eafe25139bf873",
    "higher-prime-powers/verify_exact.py": "bf9503979a8ee84b3e636317a70f7c6a43f5510b",
}


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    obj: dict[str, Any] = {}
    for key, value in pairs:
        require(key not in obj, "duplicate JSON key: " + key)
        obj[key] = value
    return obj


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def strict_equal(a: Any, b: Any, path: str = "root") -> None:
    require(type(a) is type(b), "type mismatch at " + path)
    if isinstance(a, dict):
        require(a.keys() == b.keys(), "key mismatch at " + path)
        for k in a:
            strict_equal(a[k], b[k], path + "." + k)
    elif isinstance(a, list):
        require(len(a) == len(b), "length mismatch at " + path)
        for i, (x, y) in enumerate(zip(a, b)):
            strict_equal(x, y, path + "[" + str(i) + "]")
    else:
        require(a == b, "value mismatch at " + path)


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def authenticate() -> None:
    lock = read_json(ROOT / "SOURCE_LOCK.json")
    require(lock.get("parent_commit") == PARENT_COMMIT, "parent commit lock mismatch")
    strict_equal(lock.get("parent_blobs"), PARENT_BLOBS, "parent_blobs")
    for name, sha in PARENT_BLOBS.items():
        p = ROOT.parent / name
        require(p.is_file(), "missing parent: " + name)
        require(git_blob(p.read_bytes()) == sha, "parent blob mismatch: " + name)


@dataclass(frozen=True)
class CQ:
    re: Q = Q(0)
    im: Q = Q(0)

    @staticmethod
    def lift(x: CQ | Q | int) -> CQ:
        return x if isinstance(x, CQ) else CQ(Q(x))

    def __add__(self, x: CQ | Q | int) -> CQ:
        z = self.lift(x)
        return CQ(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self) -> CQ:
        return CQ(-self.re, -self.im)

    def __sub__(self, x: CQ | Q | int) -> CQ:
        return self + -self.lift(x)

    def __rsub__(self, x: CQ | Q | int) -> CQ:
        return self.lift(x) + -self

    def __mul__(self, x: CQ | Q | int) -> CQ:
        z = self.lift(x)
        return CQ(self.re*z.re - self.im*z.im, self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def conj(self) -> CQ:
        return CQ(self.re, -self.im)

    def norm2(self) -> Q:
        return self.re*self.re + self.im*self.im

    def __truediv__(self, x: CQ | Q | int) -> CQ:
        z = self.lift(x)
        require(z.norm2() != 0, "zero Gaussian-rational denominator")
        return (self * z.conj()) * (1/z.norm2())

    def __rtruediv__(self, x: CQ | Q | int) -> CQ:
        return self.lift(x) / self

    def __pow__(self, n: int) -> CQ:
        require(type(n) is int, "noninteger power")
        if n < 0:
            return (CQ(Q(1))/self) ** (-n)
        out, base = CQ(Q(1)), self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n //= 2
        return out


def trim(a: list[Q]) -> list[Q]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a: list[Q], b: list[Q], scale: Q = Q(1)) -> list[Q]:
    return trim([(a[i] if i < len(a) else Q(0)) +
                 scale*(b[i] if i < len(b) else Q(0))
                 for i in range(max(len(a), len(b)))])


def mul(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def derivative(a: list[Q]) -> list[Q]:
    return [Q(i)*a[i] for i in range(1, len(a))] or [Q(0)]


def ev(a: list[Q], x: Q | CQ) -> Q | CQ:
    ans = CQ() if isinstance(x, CQ) else Q(0)
    for c in reversed(a):
        ans = ans*x+c
    return ans


def lag(n: int) -> list[Q]:
    require(type(n) is int and n >= 0, "invalid degree")
    return [Q((-1)**j*comb(n, j), factorial(j)) for j in range(n+1)]


def fm(n: int) -> list[Q]:
    require(type(n) is int and n >= 0, "invalid degree")
    if n == 0:
        return [Q(1)]
    return [Q(0)] + [Q((-1)**j*comb(n-1, j-1), factorial(j))
                       for j in range(1, n+1)]


def exp_integral(a: list[Q], power: int = 0, rate: Q = Q(1)) -> Q:
    require(rate > 0 and power >= 0, "invalid integral parameters")
    return sum((c*factorial(j+power)/rate**(j+power+1)
                for j, c in enumerate(a)), Q(0))


def kernel(N: int, t: Q, u: Q) -> Q:
    a, b = fm(N), fm(N+1)
    if t == u:
        ans = ev(b, t)*ev(derivative(a), t)-ev(a, t)*ev(derivative(b), t)
    else:
        ans = (ev(a, t)*ev(b, u)-ev(b, t)*ev(a, u))/(t-u)
    return Q(N*(N+1))*ans


def bivar_outer(a: list[Q], b: list[Q], scale: Q = Q(1)) -> dict[tuple[int,int], Q]:
    return {(i,j): scale*x*y for i,x in enumerate(a) for j,y in enumerate(b) if x*y}


def bivar_add(target: dict[tuple[int,int], Q], other: dict[tuple[int,int], Q]) -> None:
    for key, value in other.items():
        target[key] = target.get(key, Q(0))+value
        if target[key] == 0:
            del target[key]


def run() -> dict[str, Any]:
    authenticate()
    counts: Counter[str] = Counter()

    def check(name: str, actual: Any, expected: Any) -> None:
        require(actual == expected, "failed exact control: " + name)
        counts[name] += 1

    for n in range(1, 33):
        f, df = fm(n), derivative(fm(n))
        check("laguerre_difference", f, add(lag(n), lag(n-1), Q(-1)))
        check("laguerre_derivative", df, [Q(-1)*x for x in lag(n-1)])
        lhs = [Q(0)]+f
        rhs = add(add([2*n*x for x in f], fm(n+1), Q(-n-1)), fm(n-1), Q(1-n))
        check("minus_one_recurrence", trim(lhs), rhs)
        check("squared_norm", exp_integral(mul(f, f)), Q(2))
        check("weighted_norm", exp_integral(mul(f, f), 1), Q(6*n))
        check("weighted_derivative_norm", exp_integral(mul(df, df), 1), Q(2*n-1))
        check("ordinary_cross_moment", exp_integral(mul(lag(n), lag(n-1)), 1), Q(-n))
        f3 = [a*3**j for j, a in enumerate(f)]
        check("polar_integral", exp_integral(f3), Q((-1)**n*3*2**(n-1)))
        check("square_bias_integral", exp_integral(f3, rate=Q(3,2))/2, Q(2*(-1)**n,3))
        check("continuous_diagonal", exp_integral(mul(f,f),1)/9, Q(2*n,3))

    nodes = [Q(0), Q(1,4), Q(1), Q(2), Q(7,2)]
    for N in range(1, 21):
        direct: dict[tuple[int,int],Q] = {}
        for n in range(1,N+1):
            bivar_add(direct, bivar_outer(fm(n),fm(n),Q(n)))
        crossed: dict[tuple[int,int],Q] = {}
        for (i,j), val in direct.items():
            bivar_add(crossed, {(i+1,j):val, (i,j+1):-val})
        expected = bivar_outer(fm(N),fm(N+1),Q(N*(N+1)))
        bivar_add(expected,bivar_outer(fm(N+1),fm(N),Q(-N*(N+1))))
        check("CD_polynomial_identity", crossed, expected)
        for t in nodes:
            for u in nodes:
                direct_value = sum((Q(n)*ev(fm(n),t)*ev(fm(n),u) for n in range(1,N+1)),Q(0))
                check("CD_confluent_or_distinct", kernel(N,t,u), direct_value)
        fixtures = [([Q(1),Q(2),Q(3)],[Q(1),Q(-2),Q(3)]),
                    ([Q(1),Q(1),Q(1,4)],[Q(2),Q(-1),Q(-4)]),
                    ([Q(0),Q(1,3),Q(5)],[Q(-2),Q(7,3),Q(1,2)])]
        for ts, weights in fixtures:
            coeff_energy = sum((Q(n)*sum((a*ev(fm(n),t) for a,t in zip(weights,ts)),Q(0))**2
                                for n in range(1,N+1)),Q(0))
            gram_energy = sum((a*b*kernel(N,t,u) for a,t in zip(weights,ts)
                               for b,u in zip(weights,ts)),Q(0))
            check("complete_signed_Gram", gram_energy, coeff_energy)
            check("finite_Gram_nonnegative", gram_energy>=0, True)
        check("diagonal_cubic_sum",sum((Q(2*n*n,3) for n in range(1,N+1)),Q(0)),Q(N*(N+1)*(2*N+1),9))
        check("Bergman_boundary_partial_sum",sum((Q(1,(n+1)*(n+2)) for n in range(N+1)),Q(0)),Q(N+1,N+2))

    rho = CQ(Q(3,4),Q(1))
    lam, w0 = (1+rho)/(2-rho), (2-rho)/(1+rho)
    check("counterfeit_pole_radius",w0.norm2(),Q(41,65))
    check("counterfeit_growth_square",lam.norm2(),Q(65,41))
    for m in range(33):
        check("integer_residue_noncancellation",Q(1,4)-m !=0,True)
    # Independent formal division of (1+w)/[(2-rho)-(1+rho)w].
    prev=CQ()
    for n in range(25):
        coeff=(CQ(Q(1 if n<=1 else 0))+(1+rho)*prev)/(2-rho)
        expected=1/(2-rho) if n==0 else (3/(2-rho)**2)*lam**(n-1)
        check("Cayley_pole_coefficients",coeff,expected)
        prev=coeff

    for rr in [CQ(Q(1,2),Q(2)), CQ(Q(3,4),Q(1)), CQ(Q(1,4),Q(1)), CQ(Q(2,3),Q(5))]:
        k=Q(9,4)/((2-rr)*(1+rr)); ll=(1+rr)/(2-rr); x=2*k-1
        check("Cauchy_Chebyshev_argument",(ll+1/ll)/2,x)
        t0,t1=CQ(Q(1)),x
        for n in range(25):
            t=t0 if n==0 else t1
            check("Cauchy_Chebyshev_coefficients",k*t,k*(ll**n+ll**(-n))/2)
            if n>=1:
                t0,t1=t1,2*x*t1-t0
        a=(2-rr)/(1+rr); delta=rr.re-Q(1,2)
        check("Cayley_horizontal_weight",1-a.norm2(),6*delta/(1+rr).norm2())
        for m in [1,2,5]:
            res=-Q(m,8)*(1+a)**2
            check("log_derivative_residue",res,-Q(9*m,8)/(1+rr)**2)
            check("local_area_defect",2*(1-a.norm2())*res.norm2(),Q(243,16)*m*m*delta/(1+rr).norm2()**3)
    # The finite checks above apply to models, not a new zeta-zero census.
    hashes={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            for name in ['PROOF.md','BOUNDARY.md','verify_exact.py','SOURCE_LOCK.json']}
    return {
        "schema": "PR792_PE_BR_EXACT_V1",
        "status": "FINITE_EXACT_CONTROLS_ONLY_RH_UNPROVED",
        "arithmetic": "EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "checks": sum(counts.values()),
        "counts": dict(sorted(counts.items())),
        "max_norm_degree": 32,
        "max_CD_degree": 20,
        "actual_prime_sum_evaluated": False,
        "PNT_reproved": False,
        "independent_analytic_review": False,
        "source_sha256": hashes,
        "exact_constants": {
            "continuous_diagonal_slope": "2/3",
            "weighted_diagonal_leading_coefficient": "2/9",
            "counterfeit_inverse_radius_squared": "65/41",
            "counterfeit_residue_increment": "1/4",
            "area_local_defect_coefficient": "243/16"
        }
    }


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group()
    group.add_argument('--write', type=Path)
    group.add_argument('--check', type=Path)
    args=parser.parse_args()
    try:
        result=run()
        if args.check:
            strict_equal(result,read_json(args.check))
        output=json.dumps(result,sort_keys=True,indent=2)+'\n'
        if args.write:
            args.write.write_text(output,encoding='utf-8')
        print(output,end='')
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print('REFUSED: '+str(exc),file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
