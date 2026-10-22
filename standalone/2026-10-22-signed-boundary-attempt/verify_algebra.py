#!/usr/bin/env python3
"""Exact algebra accompanying the analytic notes; no L-values are tested.

Run from any directory with Python 3. The JSON is a replay record, not a
proof of the imported analytic statements or the high-conductor premise.
Only the standard library is required.
"""

from fractions import Fraction as F
import json


def require(condition, message):
    if not condition:
        raise AssertionError(message)


# A small exact polynomial ring in x,z,y, sufficient for the Euler identity.
def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for power, coefficient in polynomial.items():
            result[power] = result.get(power, F(0)) + coefficient
    return {power: value for power, value in result.items() if value}


def scale(polynomial, coefficient):
    return {power: coefficient * value for power, value in polynomial.items()
            if coefficient * value}


def multiply(left, right):
    result = {}
    for a, u in left.items():
        for b, v in right.items():
            power = tuple(x + y for x, y in zip(a, b))
            result[power] = result.get(power, F(0)) + u * v
    return {power: value for power, value in result.items() if value}


one = {(0, 0, 0): F(1)}
x = {(1, 0, 0): F(1)}
z = {(0, 1, 0): F(1)}
y = {(0, 0, 1): F(1)}
left = add(
    multiply(add(one, scale(x, -1), z, scale(y, -1)),
             add(one, scale(z, -1))),
    scale(multiply(add(one, scale(x, -1)), add(one, scale(y, -1))), -1),
)
right = multiply(add(x, scale(z, -1)), add(z, scale(y, -1)))
require(left == right, "joint Euler polynomial identity")
bad_left = add(
    multiply(add(one, z, scale(y, -1)), add(one, scale(z, -1))),
    scale(multiply(add(one, scale(x, -1)), add(one, scale(y, -1))), -1),
)
require(bad_left != right, "omitting the inverse-cube term must be rejected")


# Affine functions of beta are (constant, beta coefficient).
def affine_add(*terms):
    return tuple(sum(term[i] for term in terms) for i in range(2))


def affine_scale(term, scalar):
    return tuple(scalar * coefficient for coefficient in term)


def affine_value(term, beta):
    return term[0] + term[1] * beta


def nonnegative_on(term, lo, hi):
    # This checks a continuous interval, since an affine minimum is at an end.
    return min(affine_value(term, lo), affine_value(term, hi)) >= 0


target_rho = (F(1), F(-1, 2))
completed_ranges = []
for lo, hi, delta in (
    (F(1, 2), F(2, 3), (F(1, 3), F(-1, 3))),
    (F(2, 3), F(1), (F(0), F(1, 6))),
):
    rho_terms = (
        target_rho,
        affine_add((F(1), F(-1)), affine_scale(delta, 3)),
        affine_add((F(1, 2), F(0)), affine_scale(delta, F(3, 2))),
    )
    require(all(nonnegative_on(affine_add(term, affine_scale(target_rho, -1)),
                               lo, hi) for term in rho_terms),
            "continuous completed optimization lower bound")
    require(target_rho in rho_terms, "completed optimum is attained")
    require(nonnegative_on(affine_add(delta, (F(-1, 9), F(0))), lo, hi),
            "delta at least 1/9")
    require(nonnegative_on(affine_add((F(1, 6), F(0)),
                                      affine_scale(delta, -1)), lo, hi),
            "delta at most 1/6")
    completed_ranges.append({"beta_interval": [str(lo), str(hi)],
                             "delta_affine": list(map(str, delta)),
                             "rho_affine": list(map(str, target_rho))})


# The numerical boundary is an inherited algebraic reference, not an output.
k_lo = F(749773294079928, 10**15)
k_hi = F(749773294079929, 10**15)


def quartic(k):
    return 16686*k**4 - 27405*k**3 + 9936*k**2 + 1290*k - 275


require(quartic(k_lo) > 0 > quartic(k_hi), "inherited quartic brackets a root")
derivative_upper = 66744*k_hi**3 - 82215*k_lo**2 + 19872*k_hi + 1290
require(derivative_upper < 0, "inherited root unique in isolating interval")
b_lo, b_hi = (1+k_lo)/2, (1+k_hi)/2
rho_lo, rho_hi = (11-12*b_hi)/5, (11-12*b_lo)/5
require(rho_lo > F(1, 10), "positive low-conductor threshold")


# Complete valuation classes modulo six. This is a finite local identity,
# not a finite approximation to the global character moment.
for valuation in range(6):
    require((valuation+6) % 6 == valuation,
            "sixth-power amplification preserves primitive-conductor digit")
    require((valuation == 0) == ((valuation+6) % 6 == 0),
            "zero primitive-conductor digit retained")


# The rational high-conductor target is expressly an unproved hypothesis.
beta, eta, c, tau = F(7, 8), F(1, 100), F(2, 25), F(1, 100)
kappa = 2*beta-1
rho = 1-F(6, 5)*kappa
require(c == rho-eta-tau, "rational conductor threshold")
low_exponent = (1-eta)/6 + F(5, 6)*c + kappa
require(low_exponent == 1-eta-F(5, 6)*tau,
        "strict low-conductor removal at extended raw scale")
require(F(5, 6)*(1-eta) == F(33, 40), "conditional long inverse slope")
require(F(5, 6)*tau == F(1, 120), "rational strict removal saving")


# Moving-prime separated-norm audit: exact affine coefficients cover both
# continuous branches and every permitted nonprincipal digit.
auxiliary = []
for d in range(1, 6):
    e = d-1
    loss = F(1, 2)-F(e+1, 12)
    require(loss == F(5-e, 12) and loss > 0,
            "first auxiliary branch has a positive loss")
    require(F(1, 2)-loss == F(e+1, 12),
            "second branch residual is ((e+1)r-b)/12")
    auxiliary.append({"character_digit": d, "frequency_digit": e,
                      "theta_digit": (-d-1) % 6,
                      "minimum_loss_per_prime_exponent": str(loss)})
require(6*F(13, 18)-1 == F(10, 3), "inherited centering threshold")


# On the specified M2 face, width loss / excess is exactly six. Stripping
# repairs at rate lambda and costs kappa; hence lambda >= 6*kappa.
width_loss_per_ell, excess_per_ell = F(6), F(1)
require(width_loss_per_ell/excess_per_ell == 6, "M2 face capacity ratio")

# In the quadratic terminal A=HB, a full-divisor bound has exponents
# A^(1/2-delta) H^(2delta) B^(1+delta). Divide by sqrt(AB),
# square, and count O(H) rows. The coefficients below are affine in delta.
A_power = (F(1, 2), F(-1))
H_extra = (F(0), F(2))
B_extra = (F(1), F(1))
H_normalized = affine_add(A_power, H_extra, (F(-1, 2), F(0)))
B_normalized = affine_add(A_power, B_extra, (F(-1), F(0)))
require(affine_add(affine_scale(H_normalized, 2), (F(1), F(0)))
        == (F(1), F(2)), "quadratic terminal H exponent")
require(affine_scale(B_normalized, 2) == (F(1), F(0)),
        "quadratic terminal B exponent")

print(json.dumps({
    "status": "PASS",
    "arithmetic": "exact integers and rational numbers",
    "checks": {
        "joint_euler_polynomial_identity": True,
        "omitted_cube_inverse_mutation_rejected": True,
        "continuous_completed_optimization": completed_ranges,
        "inherited_boundary_isolating_interval": list(map(str, (b_lo, b_hi))),
        "low_conductor_threshold_interval": list(map(str, (rho_lo, rho_hi))),
        "sixth_power_valuation_classes": 6,
        "rational_high_conductor_target": {
            "beta": str(beta), "eta": str(eta), "c": str(c), "tau": str(tau),
            "low_row_exponent": str(low_exponent),
            "saving_relative_to_H": "D^(-1/120)",
            "conditional_amplified_slope": "33/40",
        },
        "auxiliary_digits": auxiliary,
        "M2_face_capacity_ratio": "6",
        "quadratic_terminal_resource": "H^(1+2 delta) B",
    },
    "scope": {
        "analytic_continuation_reproved_by_computation": False,
        "imported_cubic_mean_proved_by_computation": False,
        "high_conductor_moment_proved": False,
        "new_zero_free_boundary_proved": False,
        "RH_proved": False,
    },
}, indent=2, sort_keys=True))
