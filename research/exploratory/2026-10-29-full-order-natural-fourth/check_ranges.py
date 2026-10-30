#!/usr/bin/env python3
"""Exact endpoint checks for the fixed n=4,...,10 scalar relaxation."""
from fractions import Fraction as F

for n in range(4, 11):
    R = F(3*n*n-10, n*(6*n-10))
    left = F(3*n-10, 2*(9*n-20))
    middle = F(n, 2*(3*n-5))
    tail = 1-R
    assert 0 <= left <= middle <= tail <= F(1, 2)

    def faces(b, x):
        return ((1-b)*(1-F(3,5)*x),
                b+(1-2*b)/n+F(2,5)*(1-b)*x,
                b+(1-2*b)*(1-F(1,n))+(F(2,n)-F(3,5))*(1-b)*x)

    def short_t(b):
        return (1-2*b)/(1-b)+(F(3,5)-F(2,n))/(2*(1-F(2,n)))

    for b in (F(0), left):
        t = F(15*(n-2),4*(3*n-5))*(1-2*b)/(1-b)
        assert 1 <= t <= F(3,2)
        assert max(*faces(b,2*t/3),*faces(b,t)) <= R
    for b in (left, middle):
        assert max(*faces(b,F(2,3)),*faces(b,F(1))) <= R
    for b in (middle, tail):
        t=short_t(b)
        assert F(1,2) < t <= 1
        assert max(*faces(b,t-F(1,2)),*faces(b,t)) <= R
    D=F(12*n*n-38*n+5,21*n*n-80*n+50)
    assert D>R
    print(f'n={n}, R={R}, source={D}, gap={D-R}')
