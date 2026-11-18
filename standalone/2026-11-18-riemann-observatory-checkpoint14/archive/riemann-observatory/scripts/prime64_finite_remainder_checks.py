#!/usr/bin/env python3
"""Reproducible arithmetic and synthetic checks for the finite remainder."""

from argparse import ArgumentParser
from cmath import exp
from fractions import Fraction
from math import isclose, pi, sin, sqrt
from random import Random


def integrate(function, left, right, steps=8192):
    """Composite Simpson quadrature for the smooth finite-interval fixtures."""
    width = (right - left) / steps
    total = function(left) + function(right)
    for index in range(1, steps):
        total += (4 if index % 2 else 2) * function(left + index * width)
    return width * total / 3


def kernel_squared(length, offset):
    if offset == 0:
        return length
    return 4 * sin(length * offset / 2) ** 2 / (length * offset**2)


def check_constants():
    coefficient = 9 * 10**14 * 5 * 800 * 32**2 * 16
    assert coefficient == 58_982_400_000_000_000_000_000
    assert coefficient < 6 * 10**22
    assert 10**22 * 16_384 < 2 * 10**26
    assert (Fraction(15, 10) * 10**6) ** 2 < 9 * 10**14 * 5 * Fraction(2, 3)


def check_kernel_and_localization():
    for length, delta in ((2, 0.04), (100, 0.05), (1000, 0.025)):
        square = lambda offset: kernel_squared(length, offset)
        inside = integrate(square, -delta, delta) / (2 * pi)
        debit = min(1, 4 / (pi * length * delta))
        assert 0 <= 1 - inside <= debit

        # Zeta surrogate with a double zero: f(z)=(z-rho)^2, unit residue.
        # Its resulting scalar is i*u/(rho+i*u), with center value zero.
        rho = 0.5 + 3j
        disk_radius = 2 * delta
        disk_maximum = disk_radius**2
        lipschitz = 4 * disk_maximum / disk_radius**2 + 4 * disk_maximum / disk_radius
        local = integrate(
            lambda offset: square(offset) * abs(1j * offset / (rho + 1j * offset)) ** 2,
            -delta,
            delta,
        ) / (2 * pi)
        assert 0 < local < lipschitz**2 * 4 * delta / (pi * length)

    length, distance = 100, 1e-5
    overlap = integrate(lambda time: exp(1j * time * distance), 0, length) / length
    assert isclose(overlap.real, sin(length * distance) / (length * distance))
    assert 3.999 < 2 + 2 * overlap.real < 4


def check_enclosure_algebra():
    random = Random(64)
    for _ in range(1000):
        finite = 10 * random.random()
        tail_bound = 2 * random.random()
        tail = tail_bound * random.random()
        c_lower = finite * random.random()
        c_upper = finite + random.random()
        q = random.random()
        exact_debit = q * random.random()
        alpha = random.random()
        model_norm = sqrt((1 - exact_debit) * finite)
        error_norm = max(0, model_norm + alpha * random.uniform(-1, 1))
        exact_error = error_norm**2
        constant = finite + tail
        eta = alpha + sqrt(tail_bound) + (1 - sqrt(1 - q)) * sqrt(c_upper)
        bound = 2 * sqrt(c_upper + tail_bound) * eta + eta**2
        assert abs(exact_error - constant) <= bound
        e_lower = exact_error * random.random()
        e_upper = exact_error + random.random()
        lower = max(c_lower, max(0, sqrt(e_lower) - alpha) ** 2)
        upper = min(
            c_upper + tail_bound,
            (sqrt(e_upper) + eta) ** 2,
            (sqrt(e_upper) + alpha) ** 2 / (1 - q) + tail_bound,
        )
        assert lower <= constant <= upper


def check_arb_certificate():
    from flint import __FLINT_VERSION__, acb, acb_series, arb, ctx

    ctx.prec = 128
    count = (arb(100) + arb(1) / 1024).zeta_nzeros()
    assert count == arb(29)
    roots = acb.zeta_zeros(1, 29)
    assert len(roots) == 29
    assert roots[0].imag > arb(1) / 16
    assert roots[-1].imag < 100
    assert all(right.imag - left.imag > arb(1) / 8
               for left, right in zip(roots, roots[1:]))
    finite = arb(0)
    log_two = arb(2).log()
    for root in roots:
        assert root.real == arb(1) / 2
        derivative = acb_series([root, 1], 2).zeta()[1]
        assert abs(derivative) > 0
        coefficient = derivative * (((1 - root) * log_two).exp() - 1) / root
        magnitude = abs(coefficient)
        finite += 2 * magnitude * magnitude
    assert finite > arb("0.25253801685456458")
    assert finite < arb("0.25253801685456460")
    x = arb(101)
    tail = 9 * 10**14 * x ** (-arb(1) / 8) * (8 * x.log() + 64)
    assert tail < arb("5.102e16")
    assert finite + tail < arb("5.103e16")
    print(f"FLINT {__FLINT_VERSION__} certified finite sum: {finite}")
    print(f"Coefficient tail bound at Y=100: {tail}")


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--arb", action="store_true", help="also verify the Y=100 certificate")
    args = parser.parse_args()
    check_constants()
    check_kernel_and_localization()
    check_enclosure_algebra()
    print("Tail constants, synthetic kernel/localization, and enclosure checks passed.")
    if args.arb:
        check_arb_certificate()
