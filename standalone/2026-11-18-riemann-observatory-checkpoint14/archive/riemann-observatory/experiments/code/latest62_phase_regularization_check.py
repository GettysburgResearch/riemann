"""Numerical cross-check of a Mellin-phase filter and its variational gap."""

from cmath import exp
from math import cos, pi, sqrt, tan

from scipy.integrate import quad


def spectral_values(t, tau, direction):
    s = complex(0.5, t)
    squared_frequency = abs(s) ** 2
    phase = exp(1j * direction * (t * t + 0.7))
    target = phase / s
    filtered = target / (1 + tau * squared_frequency)
    perturbation = (0.15 - 0.11j) * phase / (1 + squared_frequency) ** 2
    return squared_frequency, target, filtered, perturbation


def integrate_spectrum(tau, integrand):
    scale = sqrt((1 + tau / 4) / tau)
    result = 0.0
    for direction in (-1, 1):

        def transformed(angle):
            t = direction * scale * tan(angle)
            return integrand(*spectral_values(t, tau, direction)) * scale / cos(angle) ** 2

        result += quad(transformed, 0, pi / 2, epsabs=1e-9, epsrel=1e-9)[0]
    return result / (2 * pi)


def check(tau):
    a = 1 + tau / 4
    expected_derivative = 1 / (4 * sqrt(tau) * a ** 1.5)
    expected_error = sqrt(tau) * (1 + tau / 2) / (4 * a ** 1.5)
    derivative = integrate_spectrum(tau, lambda q, g, f, _: q * abs(f) ** 2)
    error = integrate_spectrum(tau, lambda q, g, f, _: abs(f - g) ** 2)

    def objective_at_perturbation(q, g, f, p):
        return abs(f + p - g) ** 2 + tau * q * abs(f + p) ** 2

    objective = integrate_spectrum(tau, objective_at_perturbation)
    gap = integrate_spectrum(tau, lambda q, g, f, p: (1 + tau * q) * abs(p) ** 2)
    assert abs(derivative - expected_derivative) <= 1e-8 * expected_derivative
    assert abs(error - expected_error) <= 1e-8 * expected_error
    assert abs(objective - (error + tau * derivative + gap)) <= 1e-8 * objective
    print(f"tau={tau:g}  error²={error:.10g}  derivative²={derivative:.10g}  "
          f"product={sqrt(error * derivative):.10g}  objective gap={gap:.10g}")


if __name__ == "__main__":
    for parameter in (1e-4, 0.01, 0.3, 1.0, 4.0, 100.0):
        check(parameter)
