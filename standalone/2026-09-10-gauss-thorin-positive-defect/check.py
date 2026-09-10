#!/usr/bin/env python3
"""Exact finite algebra and a directed m=2 phase diagnostic. Not an RH proof.

Only Python's standard library is trusted. Intervals have integer endpoints
in units of 2**(-BITS), and each operation rounds outward. No float enters
an acceptance test. Run: python check.py --out checks.json
"""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import platform

BITS = 288
S = 1 << BITS


def ceildiv(n: int, d: int) -> int:
    if d <= 0:
        raise ValueError('positive denominator required')
    return -((-n) // d)


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ArithmeticError(message)


@dataclass(frozen=True)
class I:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        need(self.lo <= self.hi, 'unordered interval')

    @staticmethod
    def point(x: int | F) -> 'I':
        x = F(x)
        return I(x.numerator * S // x.denominator,
                 ceildiv(x.numerator * S, x.denominator))

    def __add__(self, other: object) -> 'I':
        o = as_i(other)
        return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__

    def __neg__(self) -> 'I':
        return I(-self.hi, -self.lo)

    def __sub__(self, other: object) -> 'I':
        return self + (-as_i(other))

    def __rsub__(self, other: object) -> 'I':
        return as_i(other) - self

    def __mul__(self, other: object) -> 'I':
        o = as_i(other)
        p = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return I(min(p)//S, ceildiv(max(p), S))
    __rmul__ = __mul__

    def inv(self) -> 'I':
        if self.lo > 0:
            return I(S*S//self.hi, ceildiv(S*S, self.lo))
        if self.hi < 0:
            return -(-self).inv()
        raise ZeroDivisionError('interval contains zero')

    def __truediv__(self, other: object) -> 'I':
        return self * as_i(other).inv()

    def __rtruediv__(self, other: object) -> 'I':
        return as_i(other) / self

    def __pow__(self, k: int) -> 'I':
        if not isinstance(k, int) or k < 0:
            raise ValueError('nonnegative integer exponent required')
        ans, v = I.point(1), self
        while k:
            if k & 1:
                ans = ans*v
            v = v*v
            k >>= 1
        return ans

    def abs_upper(self) -> F:
        return F(max(abs(self.lo), abs(self.hi)), S)

    def widen(self, radius: F) -> 'I':
        need(radius >= 0, 'negative radius')
        r = ceildiv(radius.numerator*S, radius.denominator)
        return I(self.lo-r, self.hi+r)

    def contains(self, x: int | F) -> bool:
        x = F(x)
        return F(self.lo, S) <= x <= F(self.hi, S)

    def record(self) -> dict[str, object]:
        # Decimal strings here are outward bounds, not nearest-rounding claims.
        T = 10**18
        def dec(n: int) -> str:
            sign = '-' if n < 0 else ''
            n = abs(n)
            return f'{sign}{n//T}.{n%T:018d}'
        return {'lo_integer': str(self.lo), 'hi_integer': str(self.hi),
                'denominator_power_of_two': BITS,
                'outward_decimal_18': [dec(self.lo*T//S), dec(ceildiv(self.hi*T,S))]}


def as_i(x: object) -> I:
    if isinstance(x, I):
        return x
    if isinstance(x, (int, F)):
        return I.point(x)
    raise TypeError('only integer, Fraction or interval allowed')


@dataclass(frozen=True)
class C:
    re: I
    im: I

    @staticmethod
    def point(re: int | F = 0, im: int | F = 0) -> 'C':
        return C(I.point(re), I.point(im))

    def __add__(self, o: 'C') -> 'C':
        return C(self.re+o.re, self.im+o.im)

    def __neg__(self) -> 'C':
        return C(-self.re, -self.im)

    def __sub__(self, o: 'C') -> 'C':
        return self + (-o)

    def __mul__(self, o: 'C') -> 'C':
        return C(self.re*o.re-self.im*o.im, self.re*o.im+self.im*o.re)

    def scale(self, x: I | int | F) -> 'C':
        return C(self.re*x, self.im*x)

    def __truediv__(self, o: 'C') -> 'C':
        den = o.re*o.re+o.im*o.im
        need(den.lo > 0, 'complex denominator not certified nonzero')
        return C((self.re*o.re+self.im*o.im)/den,
                 (self.im*o.re-self.re*o.im)/den)

    def norm_upper(self) -> F:
        return self.re.abs_upper()+self.im.abs_upper()

    def widen(self, radius: F) -> 'C':
        return C(self.re.widen(radius), self.im.widen(radius))

    def record(self) -> dict[str, object]:
        return {'real': self.re.record(), 'imaginary': self.im.record()}


def sqrt_i(x: I) -> I:
    need(x.lo >= 0, 'nonnegative sqrt required')
    lo = isqrt(x.lo*S)
    hi = isqrt(x.hi*S)
    if hi*hi < x.hi*S:
        hi += 1
    return I(lo, hi)


def atan_small(x: F, terms: int) -> I:
    need(0 < x < 1 and terms >= 1, 'invalid arctangent parameters')
    acc = sum(((-1)**j * x**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    rem = x**(2*terms+1)/F(2*terms+1)
    return I.point(acc).widen(rem)


def pi_i() -> I:
    return 16*atan_small(F(1,5),130)-4*atan_small(F(1,239),45)


def log_core(x: I, terms: int = 120) -> I:
    need(x.lo >= S and x.hi <= 2*S, 'log_core needs [1,2]')
    y = (x-1)/(x+1)
    term, out = y, I.point(0)
    for j in range(terms):
        out = out + term/F(2*j+1)
        term = term*y*y
    yh = F(y.hi, S)
    tail = 2*yh**(2*terms+1)/(F(2*terms+1)*(1-yh*yh))
    return (2*out).widen(tail)


def log_i(x: I) -> I:
    need(x.lo > 0, 'positive logarithm required')
    k = 0
    while x.lo < S:
        x = x*2
        k -= 1
    while x.hi > 2*S:
        x = x/2
        k += 1
    # Our inputs are narrow and away from power-of-two boundaries.
    need(S <= x.lo <= x.hi <= 2*S, 'ambiguous logarithm scaling')
    return log_core(x)+k*log_core(I.point(2))


def phase_certificate(N: int = 320) -> dict[str, object]:
    need(N >= 100, 'tail estimate requires N >= 100')
    delta = sqrt_i(I.point(F(23,315)))
    lo, hi = I.point(F(1,3))-delta, I.point(F(1,3))+delta
    wlo = (hi-F(2,5))/(hi-lo)
    beta = wlo/lo
    b = 2*beta
    z = 1-lo/hi
    need(0 < lo.lo and hi.hi < S, 'invalid nodes')
    need(0 < b.lo and b.hi < 14*S, 'hypergeometric shape range')
    need(0 < z.lo and z.hi*10 < 9*S, 'hypergeometric argument range')
    q = C.point(F(1,4), 4)
    c, d = C.point(1), C.point()
    total, derivative = c, d
    for j in range(N):
        v = z*(j+b)/((j+14)*(j+1))
        ratio = (C.point(j)-q).scale(v)
        d, c = ratio*d-c.scale(v), ratio*c
        total, derivative = total+c, derivative+d
    # For j >= N: |ratio_j| <= .9(j+5)/(j+1) <= 19/20;
    # |d ratio_j / dq| <= 1/(N+1).
    need(F(9,10)*F(N+5,N+1) <= F(19,20), 'ratio majorant invalid')
    ctail = 19*c.norm_upper()
    dtail = 19*d.norm_upper()+F(400,N+1)*c.norm_upper()
    total, derivative = total.widen(ctail), derivative.widen(dtail)
    quotient = derivative/total
    a = F(57,4)
    modulus_squared = a*a+16
    # Binet remainder: |psi(w)-log(w)+1/(2w)| <= 1/(12 Re(w)^2).
    base = (log_i(pi_i()*hi/6)+log_i(I.point(modulus_squared))/2
            -a/(2*modulus_squared)+quotient.re)
    radius = 1/(12*a*a)
    answer = base.widen(radius)
    need(F(answer.lo,S) > F(-13,1000), 'phase lower bound failed')
    need(F(answer.hi,S) < F(-11,1000), 'phase upper bound failed')
    return {'status': 'DIRECTED_FINITE_DIAGNOSTIC_GIVEN_BINET_BOUND',
            'target': 'd/dsigma log|M(sigma+8i)/M(1-sigma-8i)| at sigma=1/2',
            'claimed_strict_interval': ['-13/1000','-11/1000'],
            'phase_derivative': answer.record(), 'bits': BITS, 'series_last_index': N,
            'A': total.record(), 'A_q_derivative': derivative.record(),
            'A_tail_radius': str(ctail), 'A_derivative_tail_radius': str(dtail),
            'digamma_remainder_radius': str(radius),
            'lo_node': lo.record(), 'hi_node': hi.record(),
            'b': b.record(), 'z': z.record()}


def mul(a: list[F], b: list[F]) -> list[F]:
    out = [F(0)]*(len(a)+len(b)-1)
    for j,x in enumerate(a):
        for k,y in enumerate(b):
            out[j+k] += x*y
    return out


def linear_solve(A: list[list[F]], y: list[F]) -> list[F]:
    n = len(y)
    rows = [list(a)+[b] for a,b in zip(A,y)]
    for j in range(n):
        pivot = next((k for k in range(j,n) if rows[k][j]), None)
        need(pivot is not None, 'singular rational system')
        rows[j],rows[pivot] = rows[pivot],rows[j]
        f = rows[j][j]
        rows[j] = [v/f for v in rows[j]]
        for k in range(n):
            if k != j:
                f = rows[k][j]
                rows[k] = [v-f*w for v,w in zip(rows[k],rows[j])]
    return [rows[j][-1] for j in range(n)]


def moments(n: int) -> list[F]:
    # L(t) = 1/(sinh(sqrt(6t))/sqrt(6t)); g = -L'/L = S'/S.
    coeff = [F(6**j,factorial(2*j+1)) for j in range(n+2)]
    g: list[F] = []
    for j in range(n+1):
        g.append((j+1)*coeff[j+1]-sum((coeff[k]*g[j-k] for k in range(1,j+1)), F(0)))
    return [(-1)**j*g[j] for j in range(n+1)]


def branching_a(k: int) -> F:
    return (1-F(1,2**(2*k-1)))/F(2*k-1)


def algebra_checks() -> dict[str, object]:
    mu = moments(12)
    need(mu[:3] == [F(1),F(2,5),F(8,35)], 'source moment normalization')
    expected = [F(4,175),F(16,202125),F(64,876750875),F(256,10316226545625)]
    records = []
    for m in range(1,5):
        cs = linear_solve([[mu[j+k] for j in range(m)] for k in range(m)],[-mu[m+k] for k in range(m)])
        p = cs+[F(1)]
        for k in range(m):
            need(sum((p[j]*mu[j+k] for j in range(m+1)), F(0)) == 0, 'orthogonality')
        pp = mul(p,p)
        h = sum((v*mu[j] for j,v in enumerate(pp)), F(0))
        k = 2*m+1
        d = h/k
        need(d == expected[m-1], 'wrong quadrature remainder constant')
        # Rational Padé logarithmic derivative g_m at zero.
        den = [(-1)**j*p[m-j] for j in range(m+1)]
        num = [sum((den[k]*((-1)**(j-k))*mu[j-k] for k in range(j+1)), F(0)) for j in range(m)]
        gm: list[F] = []
        for j in range(2*m+1):
            gm.append((num[j] if j < m else F(0))-sum((den[i]*gm[j-i] for i in range(1,min(m,j)+1)),F(0)))
        need(all(gm[j] == (-1)**j*mu[j] for j in range(2*m)), 'Padé moment matching')
        need(mu[2*m]-gm[2*m] == h, 'leading resolvent defect')
        r = 2*branching_a(k)
        records.append({'m':m,'polynomial_ascending':list(map(str,p)), 'h':str(h),'d':str(d), 'k':k,'branching_rate':str(r)})
    need(2*branching_a(3) == F(31,80), 'cubic branching rate')
    need(branching_a(4)/branching_a(3) == F(635,868), 'cubic perpetuity contraction')
    return {'moments':list(map(str,mu)), 'quadrature':records,
            'cubic_perpetuity_mean_B':'635/233','cubic_perpetuity_mean_C':'868/233'}


def self_tests() -> None:
    for x in [F(-7,3),F(-1,10),F(0),F(2,3),F(7,3)]:
        for y in [F(-5,7),F(1,3),F(7,5)]:
            a,b = I.point(x),I.point(y)
            need((a+b).contains(x+y), 'addition enclosure')
            need((a*b).contains(x*y), 'multiplication enclosure')
            need((a/b).contains(x/y), 'division enclosure')
    try:
        I(-1,1).inv()
    except ZeroDivisionError:
        pass
    else:
        raise ArithmeticError('zero denominator accepted')
    p = pi_i()
    need(p.lo > I.point(F(3141592653589793238,10**18)).hi, 'Machin lower sanity')
    need(p.hi < I.point(F(3141592653589793239,10**18)).lo, 'Machin upper sanity')
    need(log_i(I.point(1)).contains(0), 'log one')
    need(sqrt_i(I.point(4)).contains(2), 'sqrt four')


def build() -> dict[str, object]:
    self_tests()
    return {'status':'EXACT_FINITE_ALGEBRA_AND_DIRECTED_DIAGNOSTIC', 'rh_proved':False,
            'python':platform.python_version(), 'arithmetic':'integer-directed dyadic intervals and Fraction',
            'algebra':algebra_checks(), 'phase':phase_certificate()}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path)
    ap.add_argument('--verify',type=Path, help='recompute and compare a saved receipt (ignoring Python version)')
    args = ap.parse_args()
    result = build()
    if args.verify:
        stored = json.loads(args.verify.read_text(encoding='utf-8'))
        now = dict(result)
        stored.pop('python',None)
        now.pop('python',None)
        need(stored == now, 'receipt differs from complete recomputation')
    text = json.dumps(result,indent=2,allow_nan=False)+'\n'
    if args.out:
        args.out.write_text(text,encoding='utf-8')
    print(json.dumps({'rh_proved':False,'algebra_cases':4,'phase_interval':result['phase']['phase_derivative']['outward_decimal_18'],'receipt_verified':bool(args.verify)}))


if __name__ == '__main__':
    main()
