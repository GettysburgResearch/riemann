"""Independently check HLZ leading polynomials by evaluating in two shift directions."""

from itertools import product

from sympy import Rational, expand, integrate, symbols

c, x, y = symbols("c x y")
half = Rational(1, 2)


def local_terms(u, v, w, left, right):
    """List exponential weights in one ordered Euler multiplier."""
    base = -v * sum(left)
    factors = [[(-u * z, 1), (-w * z, 1), (0, -1)] for z in right]
    return [
        (base + sum(exponent for exponent, _ in choice), multiply_signs(choice))
        for choice in product(*factors)
    ]


def multiply_signs(choice):
    sign = 1
    for _, coefficient in choice:
        sign *= coefficient
    return sign


def ordered_mixed_direction(a, b, left, right):
    l_sum = sum(left)
    r_sum = sum(right)
    total = 0
    for h, k in ((l_sum, r_sum), (r_sum, l_sum)):
        direct = -b * h - a * k
        reflected = -a - b + a * h + b * k
        total += (direct**3 - reflected**3) / (12 * (a + b))

    for aa, bb in ((a, b), (b, a)):
        residues = ((aa, bb, c, 0), (-bb, -aa, c, -aa - bb),
                    (aa, -c, -bb, -bb - c))
        for u, v, w, time in residues:
            scalar = v / (48 * (u + v) * (v + w))
            scalar_0 = scalar.subs(c, 0)
            scalar_1 = scalar.diff(c).subs(c, 0)
            terms = local_terms(u, v, w, left, right)
            terms += local_terms(u, v, w, right, left)
            for e, sign in terms:
                e = time + e
                e0, e1 = e.subs(c, 0), e.diff(c).subs(c, 0)
                total += sign * (scalar_1 * e0**4 + 4 * scalar_0 * e0**3 * e1)
    return expand(total)


def coefficient(left, right):
    # Source symmetry makes the complete polynomial A(a²+b²)+B ab.
    at_11 = ordered_mixed_direction(Rational(1), Rational(1), left, right)
    at_12 = ordered_mixed_direction(Rational(1), Rational(2), left, right)
    at_13 = ordered_mixed_direction(Rational(1), Rational(3), left, right)
    a = at_12 - 2 * at_11
    b = at_11 - 2 * a
    assert expand(at_13 - 10 * a - 3 * b) == 0
    return b


untwisted = coefficient((), ())
assert untwisted == Rational(1, 12)
first = expand(coefficient((x,), ()) / untwisted)
ratio = expand(coefficient((x,), (y,)) / untwisted)
prod = expand(coefficient((x, y), ()) / untwisted)

assert first == 1 - 4 * x + 2 * x**3
shared = first + first.subs(x, y) - 1 + 12*x*y - 2*x*y*(x*x+y*y)
assert expand(ratio - shared + 6*x*x*y*y) == 0
assert expand(prod - shared - 6*x*x*y*y) == 0

covariance = expand((ratio + prod) / 2 - first * first.subs(x, y))
g = 2*x - 3*x**3
assert expand(covariance + g * g.subs(x, y) - 5*x**3*y**3) == 0
norm_bound = integrate(g**2 / x, (x, 0, Rational(1, 4)))
assert norm_bound == Rational(931, 8192) < half
print("Independent HLZ residue-direction checks passed.")
print("Kernel norm bound on (0, 1/4):", norm_bound)
