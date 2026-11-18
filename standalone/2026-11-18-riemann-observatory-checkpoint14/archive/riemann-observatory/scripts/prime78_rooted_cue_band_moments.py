#!/usr/bin/env python3
"""Deterministic finite-N cumulants for the derivative-square rooted CUE band."""

import argparse
import json
from fractions import Fraction
from math import log

import numpy as np


LOWER = Fraction(1, 20)
UPPER = Fraction(1, 10)
DEFAULT_SIZES = (20, 40, 80, 160, 320, 640, 1000, 2000)
NAMES = ("mean", "variance", "third_cumulant")


def frequencies(size):
    return range((LOWER*size).__floor__()+1, (UPPER*size).__floor__()+1)


def limiting_cumulants():
    h = log(float(UPPER/LOWER))
    d1, d3 = UPPER-LOWER, UPPER**3-LOWER**3
    mean = h+float(-4*d1+Fraction(2, 3)*d3)
    variance = h/2+float(-4*d1**2+4*d1*d3-Fraction(4, 9)*d3**2)
    third = -8*d1**3+24*d1**2*d3-8*d1*d3**2+Fraction(16, 27)*d3**3
    assert third == -Fraction(818904257, 864000000000)
    return mean, variance, float(third)


def toeplitz_apply(coefficients, columns):
    """Apply the compressed multiplication operator in Fourier coordinates."""
    center = (len(coefficients)-1)//2
    rows = columns.shape[0]
    return np.column_stack([np.convolve(coefficients, col)[center:center+rows]
                            for col in columns.T])


def floating_cumulants(size):
    k = np.array(tuple(frequencies(size)), dtype=int)
    if not k.size:
        return (0.0, 0.0, 0.0)
    width = int(k[-1])
    assert 3*width < size+1
    coefficients = np.zeros(2*width+1)
    coefficients[width+k] = coefficients[width-k] = -1.0/(2*k)
    coefficients2 = np.convolve(coefficients, coefficients)
    coefficients3 = np.convolve(coefficients2, coefficients)
    modes = np.arange(size+1, dtype=float)
    vectors = np.column_stack((np.ones(size+1), modes-size/2))
    vectors /= np.linalg.norm(vectors, axis=0)

    f1_u = toeplitz_apply(coefficients, vectors)
    f2_u = toeplitz_apply(coefficients2, vectors)
    f3_u = toeplitz_apply(coefficients3, vectors)
    m1, m2, m3 = (vectors.T@v for v in (f1_u, f2_u, f3_u))
    f11 = f1_u.T@f1_u
    f12 = f1_u.T@f2_u
    f111 = f1_u.T@toeplitz_apply(coefficients, f1_u)
    harmonic = np.sum(1/k)
    mean = -harmonic-np.trace(m1)
    variance = harmonic/2-np.trace(m2)+2*np.trace(f11)-np.trace(m1@m1)
    third = (-np.trace(m3)+3*np.trace(f12+f12.T)-3*np.trace(m1@m2)
             -6*np.trace(f111)+6*np.trace(m1@f11)-2*np.trace(m1@m1@m1))
    return tuple(map(float, (mean, variance, third)))


def rational_cumulants(size):
    """Independently evaluate the dense projection trace formulas in Q."""
    k = tuple(frequencies(size))
    indices = range(size+1)
    coeff = {sign*j: -Fraction(1, 2*j) for j in k for sign in (-1, 1)}

    def convolution(left, right):
        out = {}
        for l, a in left.items():
            for r, b in right.items():
                out[l+r] = out.get(l+r, 0)+a*b
        return out

    def toeplitz(values):
        return [[values.get(i-j, 0) for j in indices] for i in indices]

    def multiply(left, right):
        columns = list(zip(*right))
        return [[sum(a*b for a, b in zip(row, col)) for col in columns]
                for row in left]

    def trace(matrix):
        return sum(matrix[i][i] for i in indices)

    coeff2 = convolution(coeff, coeff)
    f1, f2, f3 = map(toeplitz, (coeff, coeff2, convolution(coeff2, coeff)))
    centered = [2*i-size for i in indices]
    norm = sum(value**2 for value in centered)
    projection = [[int(i == j)-Fraction(1, size+1)
                   -Fraction(centered[i]*centered[j], norm) for j in indices]
                  for i in indices]
    h = sum(Fraction(1, j) for j in k)
    f11 = multiply(f1, f1)
    assert trace(f2)-trace(f11) == h/2
    assert trace(f3)-3*trace(multiply(f1, f2))+2*trace(multiply(f11, f1)) == 0
    pf1 = multiply(projection, f1)
    pf2 = multiply(projection, f2)
    pf11 = multiply(pf1, pf1)
    return (-h+trace(pf1),
            trace(pf2)-trace(pf11),
            trace(multiply(projection, f3))-3*trace(multiply(pf1, pf2))
            +2*trace(multiply(pf11, pf1)))


def report(sizes, exact_size):
    limit = limiting_cumulants()
    rows = []
    for size in sizes:
        values = floating_cumulants(size)
        rows.append({"N": size, "frequency_count": len(frequencies(size)),
                     "cumulants": dict(zip(NAMES, values)),
                     "error_from_limit": dict(zip(NAMES, (v-l for v, l in zip(values, limit))))})
    exact = rational_cumulants(exact_size)
    floating = floating_cumulants(exact_size)
    discrepancies = [abs(float(v)-f) for v, f in zip(exact, floating)]
    assert max(discrepancies) < 5e-14
    return {"band": [str(LOWER), str(UPPER)], "numpy": np.__version__,
            "limiting_cumulants": dict(zip(NAMES, limit)), "finite_N": rows,
            "dense_rational_cross_check": {"N": exact_size,
                "cumulants": dict(zip(NAMES, map(str, exact))),
                "absolute_float_discrepancy": dict(zip(NAMES, discrepancies))}}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sizes", type=int, nargs="+", default=DEFAULT_SIZES)
    parser.add_argument("--exact-size", type=int, default=20)
    args = parser.parse_args()
    if min(args.sizes) < 1 or not 1 <= args.exact_size <= 60:
        parser.error("sizes must be positive and the exact size must be at most 60")
    print(json.dumps(report(args.sizes, args.exact_size), indent=2))
