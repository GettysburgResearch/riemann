#!/usr/bin/env python3
"""Exact finite controls for the quadratic mixed-difference theorem.

Standard library only. Does not evaluate zeta, count high zeros, sample an
infinite domain, prove Rosser's bound, or prove RH. See PROOF.md for the
infinite analytic argument. Mandatory source checks bind the two original
local files to their previously published Git blob identities.
"""
from __future__ import annotations
import argparse
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path


@dataclass(frozen=True)
class G:
    """A Gaussian rational, with exact real and imaginary coordinates."""
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))

    @staticmethod
    def cast(value):
        return value if isinstance(value, G) else G(F(value))

    def __add__(self, other):
        z = G.cast(other)
        return G(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + (-G.cast(other))

    def __rsub__(self, other):
        return G.cast(other) - self

    def __mul__(self, other):
        z = G.cast(other)
        return G(self.re*z.re - self.im*z.im,
                 self.re*z.im + self.im*z.re)

    __rmul__ = __mul__

    def norm2(self):
        return self.re*self.re + self.im*self.im

    def inverse(self):
        d = self.norm2()
        if d == 0:
            raise ZeroDivisionError('zero Gaussian rational')
        return G(self.re/d, -self.im/d)

    def __truediv__(self, other):
        return self * G.cast(other).inverse()

    def __rtruediv__(self, other):
        return G.cast(other) * self.inverse()

    def __pow__(self, exponent):
        if not isinstance(exponent, int):
            raise TypeError('integer exponent required')
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result, base = G(1), self
        while exponent:
            if exponent & 1:
                result = result*base
            base = base*base
            exponent >>= 1
        return result


def blob_hash(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def source_check() -> dict[str, str]:
    parent = Path(__file__).resolve().parent.parent
    required = {
        'HEAT_BERNSTEIN.md': '0b6ea91d6e82ee6b90a01b36e3fd757ec101dded',
        'THETA_COUNT.md': '5d8d8eb8174fa4e57cdc9c058f38bdec1b278361',
    }
    for name, wanted in required.items():
        path = parent/name
        if not path.is_file() or blob_hash(path.read_bytes()) != wanted:
            raise ValueError(f'published parent source mismatch: {name}')
    return required


def run_checks() -> dict:
    counts = Counter()

    def check(ok: bool, category: str) -> None:
        # Explicit exceptions remain operative under python -O.
        if not ok:
            raise ArithmeticError(f'failed exact control: {category}')
        counts[category] += 1

    sources = source_check()
    check(len(sources) == 2, 'published_source_binding')

    C = 10**8
    constants = {
        'local_count_log_gap': F(863,1000)*4-F(443,1000)*3-F(1589,1000),
        'middle_exponential_comparison': F(C,2457600),
        'middle_budget_numerator': 128*96000,
        'cubic_error_bound': F(125,2048),
        'far_tail_integer_numerator': 136000*12500**2,
        'quadratic_constant': C,
    }
    tests = [
        (F(8,3)**8 > 1467),
        (F(1,5*1467) < F(1,1000)),
        (constants['local_count_log_gap'] > 0),
        (sum(F(1,factorial(j)) for j in range(7)) > F(8,3)),
        (sum(F(7,20)**j/F(factorial(j)) for j in range(4)) > F(7,5)),
        (F(6561,2*C) < F(1,2)),
        (F(83,C) < F(1,2)),
        (F(3,16)+F(8,C*10000) < F(1,4)),
        (F(8,C) < F(1,2)),
        (1+48*160 < 8000),
        (C > 40*2457600),
        (128*96000 < 2**40),
        (136000*12500**2*128 < 2**500),
        (F(125,2048) < F(1,16)),
        (3**8 < C),
        (F(1,1)+F(3,20000))**2 < F(100,99),
    ]
    for ok in tests:
        check(bool(ok), 'global_constant_boundary')

    # Phase numerator coefficients, obtained in two independent expansions
    # of b*x/((x^2+s^2)) - (b+n)*(x+1)/((x+1)^2+s^2).
    for n in (1,2,7,12501):
        for r in (F(3,2),F(10000),F(C*n)):
            b = n*r
            for x in (r/2,r,2*r):
                direct_constant = b*x*(x+1)**2-(b+n)*(x+1)*x*x
                direct_square = b*x-(b+n)*(x+1)
                check(direct_constant == x*(x+1)*(b-n*x), 'phase_polynomial')
                check(direct_square == -(b+n*(x+1)), 'phase_polynomial')
                if x == r:
                    check(direct_constant == 0, 'saddle_phase_cancellation')
            for w in (r/2,r,F(3,5)*r,2*r,3*r):
                check(b/w-(n+b)/(1+w) == n*(r-w)/(w*(1+w)),
                      'envelope_derivative')

    # Exact strip and modulus algebra; these instances corroborate the
    # general calculation in the proof and do not survey actual zeta zeros.
    for beta in (F(1,4),F(1,2),F(3,4)):
        for gamma in (F(101),F(10000),F(10001,100)):
            q0 = beta*(1-beta)
            x, y = gamma*gamma+q0, gamma*(1-2*beta)
            A = G(x,y)
            check(A.norm2() == gamma**4+(1-2*q0)*gamma**2+q0*q0,
                  'strip_modulus')
            check(A.norm2() <= (gamma*gamma+F(1,2))**2, 'strip_modulus')
            check(y*y <= x, 'strip_modulus')
            check((1+A).norm2()-A.norm2() == 2*x+1, 'strip_modulus')

    # Constant relations used when eta is real and n is an integer.
    for n in (1,2,20,12500,12501,100000):
        r = F(C*n)
        check(r >= C and n/r <= F(1,C), 'quadratic_parameter')
        check((r < 8000*n*n) == (n > 12500), 'case_split')
        for w in (F(10000),F(10001),F(3,5)*r):
            if w <= F(3,5)*r:
                numerator = (r-w)*(1+w)**2-2*(r+1)*w
                check(numerator >= F(2,5)*r*w*(w-10), 'low_tail_monotonicity')
        if n > 12500:
            p = F(n,3)
            check(p/(p-1) < 2, 'high_tail_constants')
            check(p/(2*r-1) <= n/(3*r), 'high_tail_constants')
    for n in range(1,41):
        check(n*n <= 4**(n-1), 'cubic_bound_induction_fixture')
        check(F(400*n*n)*F(20,2**17)**n <= F(125,2048),
              'cubic_bound_induction_fixture')

    # Mixed differences reconstructed from both finite traces and the
    # primitive atoms. Includes real positive and conjugate nonreal models.
    panels = [
        (G(1),G(2),G(5)),
        (G(1),G(2,1),G(2,-1)),
        (G(4),G(10,F(1,4)),G(10,F(-1,4))),
    ]
    witnesses = []
    for idx, atoms in enumerate(panels):
        k = [1/(1+A) for A in atoms]
        powers = {j:sum((v**j for v in k), G()) for j in range(1,25)}
        def mixed(a,b):
            return sum(((-1)**j*comb(b,j)*powers[a+j+1]
                        for j in range(b+1)), G())
        for a in range(5):
            for b in range(7):
                h = mixed(a,b)
                direct = sum((v**(a+1)*(1-v)**b for v in k),G())
                check(h == direct, 'mixed_binomial_identity')
                check(h.im == 0, 'conjugation_and_multiplicity')
                check(h == mixed(a+1,b)+mixed(a,b+1), 'mixed_recurrence')
        for N in range(9):
            check(sum((comb(N,a)*mixed(a,N-a) for a in range(N+1)),G())
                  == powers[1], 'row_mass')
        if idx == 1:
            h = mixed(0,14)
            check(h == G(F(-433316717939,10**15)), 'positive_heat_counterfeit')
            witnesses.append({'model':'(1+u)(1+4u/5+u^2/5)',
                              'H_0_14':str(h.re)})
            z = G(F(4,5),F(3,5))
            check(z.norm2() == 1, 'rate_counterfeit')
            check(((atoms[1]+z)/(1+atoms[1])).norm2() == F(26,25),
                  'rate_counterfeit')
            check(((atoms[2]+z)/(1+atoms[2])).norm2() < 1, 'rate_counterfeit')

    return {
        'status':'PASS_QUADRATIC_MIXED_WEDGE_EXACT_CONTROLS',
        'arithmetic':'EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL',
        'checks':dict(sorted(counts.items())),
        'total_checks':sum(counts.values()),
        'source_git_blobs':sources,
        'constant_boundaries':{k:str(v) for k,v in constants.items()},
        'counterfeit_witnesses':witnesses,
        'analytic_proof':'PROOF.md; independent review pending',
        'new_high_zero_census':False,
        'rosser_theorem_reproved':False,
        'unrestricted_mixed_inequality_proved':False,
        'rh_proved':False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', type=Path,
                        help='recompute and compare the entire retained JSON')
    args = parser.parse_args()
    result = run_checks()
    if args.check is not None:
        expected = json.loads(args.check.read_text())
        if result != expected:
            raise ValueError('retained result does not equal full recomputation')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
