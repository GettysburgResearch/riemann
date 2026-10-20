"""Exact finite checks only; the infinite family has a separate proof."""
from fractions import Fraction as F
from math import factorial
import json


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def difference(n):
    j = 2 * n + 4
    u = -n
    return sum((F(u ** k, factorial(k)) for k in range(1, j)), F()) - F(
        u ** (j - 1), 2 * factorial(j - 1))


expected = F(3791459973096443589997, 9495690262216704000000)
value = difference(11)
require(value == expected and value > 0, 'Primitive counterexample failed')
require(F(11 ** 25, factorial(25)) > 6, 'Initial a_11 inequality failed')
for n in range(11, 101):
    require(difference(n) > 0, f'Counterexample failed at n={n}')
    lower = F(5) + F(8, n) + F(3, n * n)
    gap = lower * (n + 1) ** 2 - (2 * n + 5) * (2 * n + 4)
    require(gap == n * n + 4 + F(14, n) + F(3, n * n),
            'Binomial gap identity failed')
    require(gap > 0, 'Binomial gap sign failed')
print(json.dumps({
    'status': 'pass',
    'source': 'arXiv:2210.03121v9, Lemma 1 and final parameter prescription',
    'u': -11, 'J': 26,
    'difference_numerator': value.numerator,
    'difference_denominator': value.denominator,
    'additional_finite_coverage': 'All integers 11 <= n <= 100',
    'limits': 'Finite rational checks only; the integral/binomial proof establishes the infinite family. No RH or QRH disproof.'
}, indent=2))
