"""Exact symbolic compression and an independent finite CUE moment check."""

from math import factorial

import sympy as sp


def continuum_trace():
    length, shift, y, t, h = sp.symbols("length shift y t h")
    basis = [sp.Integer(1), sp.sqrt(12) * y, sp.sqrt(5) * (6 * y**2 - sp.Rational(1, 2))]
    compression = sp.Matrix([
        [
            sp.integrate(
                left.subs(y, y + shift / 2) * right.subs(y, y - shift / 2),
                (y, -length / 2, length / 2),
            )
            for right in basis
        ]
        for left in basis
    ])
    trace = sp.expand(compression.trace().subs({length: 1 - t, shift: t}))
    assert trace == -6 * t**5 + 12 * t**3 - 9 * t + 3
    assert all(coefficient < 0 for coefficient in sp.Poly(trace.subs(t, 1 + h), h).coeffs())
    return compression, trace


def average_compression(compression):
    p, q, z = sp.symbols("p q z")
    moments = sp.symbols("m1:6")
    length, shift, _ = sp.symbols("length shift y")
    cumulants = [z * moment / 2 for moment in moments]
    values = [sp.Integer(1)]
    for degree in range(1, 6):
        values.append(sp.expand(sum(
            sp.binomial(degree - 1, j) * cumulants[j] * values[degree - 1 - j]
            for j in range(degree)
        )))

    def average(entry):
        polynomial = sp.Poly(entry.subs({length: 1 - p - q, shift: p - q}), p, q)
        return sp.expand(sum(
            coefficient * values[i] * values[j]
            for (i, j), coefficient in polynomial.terms()
        ))

    averaged = compression.applyfunc(average)
    d, m2, m3, *_ = moments
    ell = 1 - d * z
    assert averaged[0, 0] == ell
    assert sp.expand(averaged[1, 1] - ell**3 - 2 * z * m3) == 0
    assert sp.expand(averaged[0, 2] - sp.sqrt(5) / 2 * (
        ell**3 - ell + 6 * ell * z * m2 - 4 * z * m3
    )) == 0
    assert averaged[0, 1] == averaged[1, 2] == 0
    barrier = sp.factor(averaged.subs(z, 1 / d).det())
    assert barrier == -40 * m3**3 / d**3
    return barrier


def finite_check():
    # N=4 original eigenvalues, n=N+2 modes, only k=2 in the band.
    # Degree four is the first crossing, with the lower boundary 3*k=n.
    n, k, r = 6, 2, 4
    z, w, j = sp.symbols("z w j")
    basis = sp.zeros(n, n - 3)
    for column in range(n - 3):
        for offset, coefficient in enumerate((-1, 3, -3, 1)):
            basis[column + offset, column] = coefficient
    gram = basis.T * basis
    symbol = -(w**k + w**(-k)) / (2 * k)
    toeplitz = sp.zeros(n)
    for degree in range(r + 1):
        coefficients = sp.expand(symbol**degree)
        toeplitz += sp.Matrix(n, n, lambda a, b: coefficients.coeff(w, a - b)) * z**degree / factorial(degree)
    exact = sp.expand((basis.T * toeplitz * basis).det() / gram.det())

    # Use the rational polynomial basis for the orthogonal complement.
    # Compress oriented shifts and convert by its Gram matrix.
    rows = sp.Matrix(n, 3, lambda a, b: a**b)
    removed_gram = rows.T * rows

    def oriented(p, q):
        first, stop = q, n - p
        interval = range(min(first, stop), max(first, stop))
        sign = 1 if first <= stop else -1
        return removed_gram.inv() * sp.Matrix(
            3, 3, lambda a, b: sign * sum((j + p - q)**a * j**b for j in interval)
        )

    inverse_surrogate = sp.zeros(3)
    for positive in range(r + 1):
        for negative in range(r + 1 - positive):
            degree = positive + negative
            weight = (z / (2 * k))**degree / (factorial(positive) * factorial(negative))
            inverse_surrogate += oriented(positive * k, negative * k) * weight
    stable_base = 1 + z**2 / (4 * k) + z**4 / (32 * k**2)
    surrogate = sp.series(stable_base * inverse_surrogate.det(), z, 0, r + 1).removeO()
    difference = sp.expand(exact - surrogate)
    assert all(difference.coeff(z, j) == 0 for j in range(r))
    observed = factorial(r) * difference.coeff(z, r)
    predicted = -2 * oriented(r * k, 0).trace() / (2 * k)**r
    assert observed == predicted and observed > 0
    # The deterministic root has factor exp(-z/k); it preserves the first discrepancy.
    return observed


if __name__ == "__main__":
    compression, trace = continuum_trace()
    print("Oriented continuum trace:", trace)
    print("Barrier determinant:", average_compression(compression))
    print("Finite first-crossing raw moment difference:", finite_check())
