#!/usr/bin/env python3
"""Exact partial crossing in finite CUE and rigorous continuum enclosures."""

from itertools import product
from math import factorial, prod

from flint import arb, ctx, fmpq as Q, fmpq_mat as Matrix


def direct_moments(n, band):
    """Taylor coefficients of the full free-point compression and fixed root."""
    identity = Matrix(n, n, [int(i == j) for i in range(n) for j in range(n)])
    centered = [2*i - n + 1 for i in range(n)]
    norm = sum(x*x for x in centered)
    projection = identity - Matrix(n, n, [
        Q(1, n) + Q(x*y, norm) for x in centered for y in centered
    ])
    symbol = {s*k: -Q(1, 2*k) for k in band for s in (-1, 1)}
    power = {0: Q(1)}
    coefficients = [identity]
    for degree in range(1, 5):
        next_power = {}
        for i, value in power.items():
            for j, weight in symbol.items():
                next_power[i+j] = next_power.get(i+j, 0) + value*weight
        power = next_power
        toeplitz = Matrix(n, n, [
            power.get(i-j, 0) / Q(factorial(degree))
            for i in range(n) for j in range(n)
        ])
        coefficients.append(projection * toeplitz * projection)

    # Jacobi's identity: logarithmic derivative is tr(M^-1 M').
    inverse = [identity]
    log_coefficients = [Q(0)]
    zero = Matrix(n, n)
    for degree in range(1, 5):
        derivative = sum((
            j * inverse[degree-j] * coefficients[j] for j in range(1, degree+1)
        ), zero)
        log_coefficients.append(sum(derivative[i, i] for i in range(n)) / degree)
        inverse.append(-sum((
            coefficients[j] * inverse[degree-j] for j in range(1, degree+1)
        ), zero))
    log_coefficients[1] -= sum(Q(1, k) for k in band)
    return [factorial(j)*value for j, value in enumerate(exp_series(log_coefficients))]


def exp_series(log_coefficients):
    out = [Q(1)]
    for degree in range(1, len(log_coefficients)):
        out.append(sum(j * log_coefficients[j] * out[degree-j]
                       for j in range(1, degree+1))/degree)
    return out


def formal_moments(n, band):
    harmonic = sum(Q(1, k) for k in band)
    d = Q(len(band), n)
    j3 = Q(sum(k*k for k in band), n**3)
    e = exp_series([Q(0), harmonic, harmonic/4, Q(0), Q(0)])
    # Numerator of the cosine prefactor in the degree-four finite surrogate.
    numerator = [
        1-Q(1, n*n), -4*d+2*j3+2*d/(n*n),
        6*d*d-2*j3*d-d*d/(n*n), -4*d**3, d**4,
    ]
    return [
        factorial(j)*sum(e[j-i]*numerator[i] for i in range(j+1))/numerator[0]
        for j in range(5)
    ]


def crossing_trace(n, m):
    return Q(2*(m-n)*(m*m+n*m-n*n+1), n*(n*n-1))


def finite():
    N = 40
    n = N + 1
    band = tuple(range(11*N//50+1, 7*N//25+1))
    tuple_count = {"below": 0, "equal": 0, "above": 0}
    correction = Q(0)
    for frequencies in product(band, repeat=4):
        total = sum(frequencies)
        if total > n:
            tuple_count["above"] += 1
            correction -= crossing_trace(n, total) / (8*prod(frequencies))
        elif total == n:
            tuple_count["equal"] += 1
        else:
            tuple_count["below"] += 1
    assert all(tuple_count.values()) and 3*max(band) <= n < 4*max(band)
    direct = direct_moments(n, band)
    formal = formal_moments(n, band)
    assert direct[:4] == formal[:4] and direct[4] == formal[4]+correction
    print(f"Finite N={N}, n={n}, frequencies={band}")
    print(f"Ordered tuple counts relative to n: {tuple_count}")
    print("Direct raw moments through order 4:", ", ".join(map(str, direct)))
    print("Formal raw fourth moment:", formal[4])
    print("Exact fourth-moment correction:", correction)


def A(s):
    return 2*(s-1)*(s*s+s-1)


def full_cube(a, b, r):
    assert r >= 3 and r*a >= 1
    h = arb(b/a).log()
    m1, m2, m3 = [arb((b**j-a**j)/j) for j in (1, 2, 3)]
    return (2*h**r + (2*r*m3-4*r*m1)*h**(r-1)
            + 6*r*(r-1)*m2*m1*h**(r-2)
            + 2*r*(r-1)*(r-2)*m1**3*h**(r-3))


def simplex(r, offset, caps, degree):
    """Integrate a product of truncated geometric series over a simplex."""
    limit = offset-1
    q = max(limit/cap for cap in caps)
    assert 0 < q < 1
    scale = Q(1)
    weights = [Q(1)]
    for cap in caps:
        scale /= cap
        factors = [Q(factorial(j))/cap**j for j in range(degree+1)]
        combined = [Q(0)]*(len(weights)+degree)
        for i, w in enumerate(weights):
            for j, f in enumerate(factors):
                combined[i+j] += w*f
        weights = combined
    # A(offset-S)=A(offset)+(4-6 offset^2)S+6 offset S^2-2 S^3.
    poly = [A(offset), 4-6*offset*offset, 6*offset, -2]
    integral = scale * sum(
        weight / factorial(m+r-1)
        * sum(c*limit**(m+r+j)/(m+r+j) for j, c in enumerate(poly))
        for m, weight in enumerate(weights)
    )
    # Union bound over which geometric-series factor was truncated.
    error = scale * r * q**(degree+1)/(1-q)**r * A(offset) * limit**r/factorial(r)
    return integral, error


def continuum():
    ctx.prec = 160
    r = 4
    a, b = Q(13, 50), Q(8, 25)
    closed = -full_cube(a, b, r)/8
    assert closed < 0
    print(f"Full-cube continuum correction for a={a}, b={b}: {closed}")

    a, b = Q(11, 50), Q(7, 25)
    width = b-a
    assert (r-1)*b <= 1 < r*b and r*a < 1
    assert width < r*b-1 <= 2*width
    total, total_error = simplex(r, r*b, [b]*r, 64)
    cap, cap_error = simplex(r, r*b-width, [a]+[b]*(r-1), 64)
    # Inclusion-exclusion removes the four caps. Their pair intersections have
    # zero volume by the bandwidth condition above.
    approx = total-r*cap
    lower = -(approx+total_error)/8
    upper = -(approx-r*cap_error)/8
    assert lower < upper < 0
    interval = arb((lower+upper)/2, (upper-lower)/2)
    print(f"Partial-crossing continuum correction for a={a}, b={b}: {interval}")
    assert upper-lower < Q(263, 10**29)
    print("Width of exact rational enclosure < 2.63e-27")


if __name__ == "__main__":
    finite()
    continuum()
