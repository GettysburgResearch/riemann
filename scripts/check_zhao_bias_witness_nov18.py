"""Certify X=1 integrated prime-bias witnesses for signed prime discriminants."""
from decimal import Decimal as D, getcontext
from functools import lru_cache
from math import isqrt

getcontext().prec = 35


@lru_cache(maxsize=None)
def terms(n):
    x = D(n)
    u = 1 / x
    v = u / x
    log_x = x.ln()
    return u, -log_x * u, v, -log_x * v


def witness(d):
    p = abs(d)
    assert d % 4 == 1 and p > 2 and all(p % a for a in range(2, isqrt(p) + 1))
    char = [-1] * p
    for a in range(1, p):
        char[a * a % p] = 1
    char[0] = 0
    total = maximum = 0
    for n in range(1, p + 1):
        total += char[n % p]
        maximum = max(maximum, abs(total))
    assert total == 0
    N = 16 * p
    assert N < 100000
    sums = [D(0)] * 4
    for n in range(1, N + 1):
        sign = char[n % p]
        for i, term in enumerate(terms(n)):
            sums[i] += sign * term
    # The tail of a decreasing positive weight is at most maximum times
    # its value at N by summation by parts, since N is a whole period.
    # At 35 significant digits all individual summands have absolute
    # roundoff <1e-32, and all partial sums stay below N. Even N
    # successive rounding errors of size 1e-29 are covered by 1e-20.
    eps = D('1e-20')
    errors = [maximum * abs(t) + eps for t in terms(N)]
    def ratio(offset):
        a, b = sums[offset:offset + 2]
        da, db = errors[offset:offset + 2]
        assert a > da
        vals = [(b + j * db) / (a + k * da)
                for j in (-1, 1) for k in (-1, 1)]
        return min(vals), max(vals)
    lo1, hi1 = ratio(0)
    lo2, hi2 = ratio(2)
    arch = D(2).ln() if d > 0 else 1 - D(2).ln()
    lower = lo1 - hi2 - arch - eps
    upper = hi1 - lo2 - arch + eps
    assert upper < -D(2) / 3
    print(f'{d:+d}  {lower:.8f} < K(0) < {upper:.8f} (rounded display)')


if __name__ == '__main__':
    for discriminant in (2221, 2237, 2269, -2207, -2239, -2287):
        witness(discriminant)
