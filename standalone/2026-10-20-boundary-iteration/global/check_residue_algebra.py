"""Exact finite checks for RESONANT_RESIDUE_MEAN.md.

This checks local identities and exponent bookkeeping only. It does not
validate the imported residue theorem, Mellin shifting, or a zero-free region.
Python standard library; run with -I -S -B.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json


def require(condition, message="exact algebraic identity failed"):
    if not condition:
        raise ArithmeticError(message)


def subsets(items):
    for k in range(len(items) + 1):
        yield from combinations(items, k)


def mul(items):
    result = F(1)
    for item in items:
        result *= item
    return result


counts = {}

# Formal phases in Z/18Z include the cubic phase Z/3Z via k -> 6k.
# g(ra)=g(r)g(a)conj(kappa); psi_r(a)=conj(kappa).
checks = 0
for gr, ga, kappa in product(range(18), range(18), range(3)):
    gra = (gr + ga - 6 * kappa) % 18
    require((ga - 6 * kappa - gra) % 18 == -gr % 18)
    checks += 1
counts["native_phase_identities"] = checks

primes = [7, 13, 19, 31, 37]
checks = 0
for q in primes:
    residue_ratio_after_norm = F(1, q) * F(q, q + 1)
    require(residue_ratio_after_norm == F(1, q + 1))
    require(1 - residue_ratio_after_norm == F(q, q + 1))
    require(F(q - 1, q) / F(q * q - 1, q * q) == F(q, q + 1))
    checks += 3
counts["local_residue_factors"] = checks

# Completed-index coprimality includes the cube Euler factor at s=5/6.
checks = 0
for q in primes:
    require(F(q, q + 1) * (1 - F(1, q*q)) == 1 - F(1, q))
    require(1 - F(q, q + 1) * (1 - F(1, q*q)) == F(1, q))
    checks += 2
counts["completed_index_selection_identities"] = checks

# Exact sixth-root arithmetic in Z[zeta_6], zeta_6^2=zeta_6-1.
# For q=1 mod 6, the six multiplicative-character values each occur
# (q-1)/6 times; this checks the native constant Fourier support.
zeta6 = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
checks = 0
for q, j, orientation in product(primes, range(6), [1, -1]):
    power = -j - 2 * orientation
    val = tuple(
        (q - 1) // 6 * sum(zeta6[(power*h) % 6][coordinate] for h in range(6))
        for coordinate in range(2)
    )
    expected_j = (-2 * orientation) % 6
    require(val == ((q - 1, 0) if j == expected_j else (0, 0)))
    checks += 1
counts["spherical_local_digit_support"] = checks

# The permitted auxiliary cubic character has digit 2; the fixed
# numerator reciprocity contributes digit 1. Its inverse is the
# self-conjugate digit 3, outside either spherical residue support.
checks = 0
for reciprocal_orientation in [1, -1]:
    guard_digit = (reciprocal_orientation*(2 + 1)) % 6
    require(guard_digit == 3)
    for residue_digit in [0, 2, 4]:
        val = tuple(sum(zeta6[((residue_digit-guard_digit)*h) % 6][c]
                        for h in range(6)) for c in range(2))
        require(val == (0, 0))
        checks += 1
for xi_a, xi_u, xi_s in product(range(6), repeat=3):
    xi_h = (xi_u + 6*xi_a) % 6
    require((-xi_h + xi_s) % 6 == (-xi_u + xi_s) % 6)
    checks += 1
counts["auxiliary_guard_and_sixth_power_cancellation"] = checks

# The general-field physical guard uses a cubic S-character of digit 2,
# a physical row of new-prime valuation -1, and the *sextic* row-unit
# correction.  Its exact local theta digit is -2-1=3.
checks = 0
for a_phase, s_phase, h_phase, t_phase in product(range(0, 6, 2), repeat=4):
    t0_phase = (t_phase + s_phase + a_phase - h_phase) % 6
    require((-a_phase - s_phase + t0_phase) % 6 == (t_phase-h_phase) % 6)
    checks += 1
for h_valuation in range(6):
    transformed_t_valuation = (h_valuation - 1) % 6
    require((transformed_t_valuation == 5) == (h_valuation == 0))
    checks += 1
require((-2 - 1) % 6 == 3)
# A cube unit with sextic digit 3 has quadratic-guard value -1,
# but every cubic character has value 1.
require((3 * 3) % 6 == 3)
require((2 * 3) % 6 == 0)
counts["all_field_guard_character_and_valuation_identities"] = checks


def guarded_principal_survives(twist_digit, physical_row_sector):
    # Unit-supported tame local tests have Fourier valuation -1.
    # The principal frequency survives iff its norm-one selector is -1.
    # The actual theta digit includes the sextic row-unit correction.
    return (
        twist_digit % 6 != 0
        and physical_row_sector % 6 == 5
        and (physical_row_sector - twist_digit) % 2 == 1
    )


require(guarded_principal_survives(2, -1), "the valid cubic guard was rejected")
negative_controls = 0
for bad_twist, bad_sector, label in [
    (3, 0, "quadratic twist with principal-killing selector"),
    (1, -1, "wrong digit yielding an even theta character"),
]:
    try:
        require(guarded_principal_survives(bad_twist, bad_sector), label)
    except ArithmeticError:
        negative_controls += 1
    else:
        raise ArithmeticError("negative control accepted: " + label)
counts["guard_negative_controls_rejected"] = negative_controls


def primitive_root(q):
    for g in range(2, q):
        if len({pow(g, n, q) for n in range(q-1)}) == q-1:
            return g
    raise AssertionError("no primitive root")


def vanishes_at_primitive_q_squared(coefficients, q):
    """Exact test in Z[zeta_6][X]/Phi_(q^2)(X), for deg<q^2."""
    # Phi_(q^2)=1+X^q+...+X^((q-1)q). A degree<q^2 polynomial
    # is a multiple precisely when each fixed residue modulo q
    # has the same coefficient in its q positions.
    return all(
        all(coefficients[r+j*q] == coefficients[r] for j in range(q))
        for r in range(q)
    )


# An exact finite replay of the local Fourier calculation on Z/q^2Z.
# No floating point complex numbers are used.  The character on units
# is lambda=chi^2, lifted from mod q.  Frequencies of valuation -2
# vanish; frequencies h=q*u give q*tau(lambda)*lambda(u)^-1.
checks = 0
for q in [7, 13]:
    g = primitive_root(q)
    logs = {pow(g, n, q): n for n in range(q-1)}
    modulus = q*q
    for h in range(modulus):
        coefficients = [[0, 0] for _ in range(modulus)]
        for a in range(modulus):
            if a % q == 0:
                continue
            phase = (2*logs[a % q]) % 6
            position = (-a*h) % modulus
            for coordinate in range(2):
                coefficients[position][coordinate] += zeta6[phase][coordinate]
        if h and h % q == 0:
            u = h // q
            inverse_phase = (-2*logs[u]) % 6
            for a in range(1, q):
                phase = (2*logs[a] + inverse_phase) % 6
                position = (-a*q) % modulus
                for coordinate in range(2):
                    coefficients[position][coordinate] -= q*zeta6[phase][coordinate]
        require(vanishes_at_primitive_q_squared(coefficients, q))
        checks += 1
counts["exact_tame_fourier_guard_mod_prime_squared"] = checks

# Uniform shifted-label local Rankin factors. Evaluate exactly at sigma=1/2
# and q=t^6, solely as a finite algebra check of the displayed local bound.
checks = 0
for t, f_valuation in product(range(2, 8), range(6)):
    q = t**6
    shift = 4*f_valuation % 6
    numerator = sum(
        (F(1, t*t) if (v + shift) % 6 in (2, 4) else F(1))
        * F(1, t**(3*v))
        for v in range(6) if (v + shift) % 6 in (0, 2, 4)
    )
    baseline = 1 + F(1, t*t)*(F(1, t**6) + F(1, t**12))
    require(numerator <= 3*baseline)
    checks += 1
counts["shifted_label_local_majorants"] = checks

checks = 0
for excluded in subsets(primes):
    inclusion_exclusion = sum(
        (-1) ** len(mark) * mul(F(1, q + 1) for q in mark)
        for mark in subsets(excluded)
    )
    require(inclusion_exclusion == mul(F(q, q + 1) for q in excluded))
    checks += 1
counts["finite_coprimality_identities"] = checks

# Here a denotes q^{-(s+1)}; q^{-s}/(q+1)=a*q/(q+1).
checks = 0
for q, a in product(primes, [F(-3, 4), F(-1, 2), F(0), F(1, 5), F(3, 4)]):
    require((1 - a * F(q, q + 1)) / (1 - a) == 1 + a / ((q + 1) * (1 - a)))
    checks += 1
counts["reciprocal_zeta_unit_identities"] = checks

# Squared residue costs r^{-1/3}; the b^6 lift count costs
# H^{1/6} r^{-kappa/6}.
for kappa, h_power, logarithm in [(2, F(1, 3), False), (4, F(1, 6), True)]:
    r_power = F(kappa + 2, 6)
    require(F(1, 3) + F(kappa, 6) == r_power)
    if r_power < 1:
        require(F(1, 6) + (1 - r_power) / kappa == h_power)
    else:
        require(r_power == 1 and logarithm)

# Native coherent scale D^{5/6} N^{beta-1+5/6}
# equals (DN)^{5/6} N^{beta-1}.
for beta in [F(7, 8), F(11, 12), F(874886647, 10**9)]:
    require(beta - 1 + F(5, 6) == beta - F(1, 6))
    require(beta - F(1, 6) - F(5, 6) == beta - 1)

# At X=H, the weaker normalized residue energy is H exactly.
require(F(2, 3) + F(1, 3) == 1)

# The canonical residue margin and cube completion are exact exponents.
checks = 0
for n, v, m, q, z in product(range(5), repeat=5):
    family_length = n + v
    margin = family_length - m - q - z
    if margin <= 0:
        continue
    residue_gap = F(family_length) - F(2*n + m, 3)
    require(residue_gap == F(2*v + q + z + margin, 3))
    require(residue_gap >= F(margin, 3))
    checks += 1
counts["canonical_residue_margins"] = checks
require(-1 - 3*F(1, 3) == -2)

# Bessel Mellin normalization at s=5/6:
# 3^(5/2)*27^(5/6)=3^5, and the pole substitution contributes 1/2.
require(F(5, 2) + 3*F(5, 6) == 5)
require(F(1, 2) - F(5, 6) == -F(1, 3))
require(F(1, 2) + F(1, 3) == F(5, 6))

print(json.dumps({
    "status": "pass",
    "checks": counts,
    "sparse_lift_squared_mean_exponents": {
        "r_squared_b_sixth": "1/3",
        "r_fourth_b_sixth": "1/6 with log(2H)"
    },
    "marked_residue_exponent": "Y^(5/6) N^(beta-1+epsilon)",
    "scope": "Exact finite algebra only; no analytic or zero-free certification."
}, indent=2))
