#!/usr/bin/env python3
"""Exact finite algebra for the independent beta-smoothing review.

This verifies normalization moments, the quartet tuning polynomial, and the
first inverse-sigma coefficient. It is not a numerical proof of entire-function
zero locations, convolution log-concavity, or asymptotic remainder estimates;
those arguments are written in the associated independent review.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
p = F(3, 4)
nu = p + F(1, 2)
assert nu == F(5, 4)

def rising(x, n):
    result = F(1)
    for k in range(n):
        result *= x + k
    return result

for n in range(17):
    moment = rising(F(1, 2), n) / rising(p + F(3, 2), n)
    coefficient_from_moment = moment / factorial(2*n)
    coefficient_from_I = F(1, 4**n * factorial(n)) / rising(nu + 1, n)
    assert coefficient_from_moment == coefficient_from_I

# Q_T(1/2) = (T^2+1/16)(T^2+9/16)
linear = F(1, 16) + F(9, 16)
constant = F(1, 16) * F(9, 16)
assert linear == 2*F(5, 16)
assert constant == F(5, 16)**2 - F(1, 16)

# Reciprocal-sigma coefficients, with w=sigma-1/2.
gamma_ratio = F(5, 16)
quartet_w_power = F(-2)       # w^4 / sigma^4
beta_w_power = F(7, 8)      # w^(-7/4) / sigma^(-7/4)
inverse_sigma_minus_one = F(1)
geometric_correction = sum([gamma_ratio, quartet_w_power,
                            beta_w_power, inverse_sigma_minus_one])
assert geometric_correction == F(3, 16)
beta_asymptotic_coefficient = (4*nu*nu - 1)/8
assert beta_asymptotic_coefficient == F(21, 32)
minimum_b = F(6**2, 2) + F(21, 32)/F(1, 100) - F(3, 16)
assert minimum_b == F(1335, 16) > 0

result = {
    "status": "PASS: exact finite normalization and asymptotic-coefficient algebra",
    "arithmetic": "Python standard-library Fraction only",
    "beta_exponent": str(p),
    "bessel_order": str(nu),
    "even_moments_checked": 17,
    "normalized_MGF": "Gamma(9/4)*(2/(delta*w))^(5/4)*I_(5/4)(delta*w), defined by its even series",
    "completion_convention": "Z=pi^(s/2)*F/[s*(s-1)*Gamma(s/2)]; NO one-half",
    "normalizing_limit": "C=A*Gamma(9/4)/(pi^(1/4)*delta^(7/4))",
    "quartet_tuning_identity": "Q_T(1/2)=(T^2+5/16)^2-1/16",
    "gamma_ratio_first_coefficient": str(gamma_ratio),
    "combined_geometric_first_coefficient": str(geometric_correction),
    "beta_first_correction": str(beta_asymptotic_coefficient),
    "b_lower_bound_for_c_ge6_delta_le_0.01": str(minimum_b),
    "scope": "Finite algebra only; analytic proofs and remainders are separately reviewed."
}
destination = ROOT / 'experiments/results/beta_smoothing_third_round3.json'
destination.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
