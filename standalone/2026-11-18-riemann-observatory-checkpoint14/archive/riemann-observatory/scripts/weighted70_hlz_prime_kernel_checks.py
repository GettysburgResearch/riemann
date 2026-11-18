#!/usr/bin/env python3
"""Verify the homogeneous derivative coefficients of HLZ (5) and (24)."""
import sympy as sp


def check():
    a, b, c, x = sp.symbols("a b c x")

    def exponential_moment(degree, shifts):
        return sum(sign * shift**degree for sign, shift in shifts) / sp.factorial(degree)

    first = exponential_moment(3, [(1, -a*x), (1, -b*x)])
    second = exponential_moment(3, [(1, -a-b+a*x), (1, -a-b+b*x)])
    j_kernel = sp.cancel((first-second)/(2*(a+b)))

    def derivative_kernel(alpha, beta, gamma, time):
        shifts = [(1, time-shift*x) for shift in (alpha, beta, gamma)]
        shifts.append((-1, time))
        return beta*exponential_moment(4, shifts)/(2*(alpha+beta)*(beta+gamma))

    i_before = 0
    for alpha, beta in ((a, b), (b, a)):
        for shifts in ((alpha, beta, c, 0),
                       (-beta, -alpha, c, -alpha-beta),
                       (alpha, -c, -beta, -beta-c)):
            i_before += derivative_kernel(*shifts)
    i_kernel = sp.cancel(sp.diff(i_before, c).subs(c, 0))

    j_coeff = sp.simplify(sp.diff(j_kernel, a, b))
    i_coeff = sp.simplify(sp.diff(i_kernel, a, b))
    assert sp.expand(j_coeff - (x-1)**2*(x+2)/6) == 0
    assert sp.expand(i_coeff - (2*x-3)/12) == 0
    normalized = sp.expand(12*(j_coeff+i_coeff))
    assert normalized == 2*x**3-4*x+1
    print(f"J (mixed coefficient): {sp.factor(j_coeff)}")
    print(f"I + reflected I (mixed coefficient): {sp.factor(i_coeff)}")
    print(f"Normalized prime kernel: {normalized}")


if __name__ == "__main__":
    check()
