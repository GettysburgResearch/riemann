"""Finite exact mixed-replication diagnostics; no analytic theorem certification."""
from fractions import Fraction as F
from itertools import product
from math import prod
import json

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

E = ((1, 2, 2), (2, 1, 2), (2, 2, 1))
s, d = 3, 5
require(all(sum(row) == d for row in E), 'replication row degree')
require(all(sum(E[t][j] for t in range(s)) == d for j in range(s)),
        'replication target identity')
q = F(d, s)
p_native = F(2*d, d-s)
require(q == F(5, 3) and p_native == 5, 'Holder exponent values')
require(1 / p_native + 1 / (2*q) == F(1, 2), 'Holder exponent sum')

# The three terms of a physical cubic-product L2 norm are H^v M^alpha.
physical = ((F(1, 2), F(1, 2)),
            (F(1, 6), F(1)),
            (F(1, 3), F(5, 6)))
h, r, b = F(21, 20), F(5, 24), F(7, 8)
a, x = 2*b - 1, 1 - 2*r
native_H = F(d-s, 2*d)
native_X = F(1, 2) + a*s/(2*d)
require(native_H == F(1, 5) and native_X == F(29, 40),
        'native interpolation')
require(native_X >= F(1, 2) and b >= F(1, 2),
        'singleton correction weights')

monomials = []
for choices in product(range(3), repeat=s):
    weights = tuple(sum(E[t][j]*physical[choices[t]][1]
                        for t in range(s))/d for j in range(s))
    require(all(w >= F(1, 2) for w in weights),
            'unequal-scale correction weight')
    pair_H = sum(physical[choices[t]][0] for t in range(s))/d
    energy = 2*((native_H + pair_H)*h
                + (native_X + 2*b)*x + sum(weights)*r)
    excess = energy - h - 3
    monomials.append((choices, weights, energy, excess))

maximum = max(m[3] for m in monomials)
require(len(monomials) == 27, 'all three-term choices')
require(maximum == F(863, 1200), 'triangle excess')
require([m[0] for m in monomials if m[3] == maximum] == [(2, 2, 2)],
        'triangle dominant term')
require(F(119, 160) - maximum == F(59, 2400), 'q2 gain')
require(F(623, 720) - maximum == F(263, 1800), 'predecessor gain')

# Normalized rho formula independently reproduces the 27-term maximum.
R_exp = 3*r
rho = max(-q*R_exp, -2*h/3, -h/3-q*R_exp/3)
normalized = 3*a*x-a*(1-1/q)*x+rho/q
require(rho == -F(251, 360), 'rho branch')
require(normalized == maximum, 'normalized formula')

# Exact six-axis mu/mu^2 forward Euler correction, all exponents <=2.
# Convolve E with prod(1+s_j z_j); the result is 1+sum s_j z_j,
# or 1 at an excluded prime. This is also an identity after any z_j=0.
signs = (-1, -1, -1, 1, 1, 1)
local_checks = 0
for masked in (False, True):
    def coefficient(exponents):
        support = sum(e > 0 for e in exponents)
        if support == 0:
            return 1
        multiplier = 1 if masked else 1-support
        return multiplier*prod((-signs[j])**exponents[j]
                               for j in range(len(signs)))

    for exponents in product(range(3), repeat=len(signs)):
        total = 0
        for chosen in product(*[range(min(1, e)+1) for e in exponents]):
            residual = tuple(exponents[j]-chosen[j] for j in range(len(signs)))
            total += coefficient(residual)*prod(signs[j]**chosen[j]
                                                for j in range(len(signs)))
        expected = int(sum(exponents) == 0)
        if not masked and sum(exponents) == 1:
            expected = signs[exponents.index(1)]
        require(total == expected, 'mixed forward Euler identity')
        local_checks += 1

# Finite Holder checks with literal zeros, evaluated without fractional powers.
# Put U_j=a_j^3. Then (sum |U1 U2 U3|^(10/3))^3 <= prod_t sum |P_t|^2.
holder_data = [list(product(range(3), repeat=3)),
               [(j, j, j) for j in range(4)],
               [(0, 1, 2), (2, 0, 1), (1, 2, 0), (1, 1, 1)]]
for rows in holder_data:
    left = sum(prod(row)**10 for row in rows)**3
    right = prod(sum(prod(row[j]**E[t][j] for j in range(3))**6
                     for row in rows) for t in range(3))
    require(left <= right, 'finite Holder with zeros')

# A negative control: the column sums are essential for critical weights.
bad_E = ((1, 2, 2), (1, 2, 2), (1, 2, 2))
bad_weights = [sum(bad_E[t][j]*F(1, 2) for t in range(3))/5
               for j in range(3)]
require(min(bad_weights) < F(1, 2), 'imbalanced matrix negative control')

def rat(value):
    return str(value)

report = {
    'scope': 'finite exact algebra, not an analytic certification',
    'q': rat(q),
    'native_p': rat(p_native),
    'pair_monomials_checked': len(monomials),
    'pair_weight_inequalities_checked': 3*len(monomials),
    'minimum_pair_weight': rat(min(w for m in monomials for w in m[1])),
    'mixed_euler_coefficients_checked': local_checks,
    'finite_holder_datasets_with_zeros': len(holder_data),
    'negative_controls': 1,
    'triangle_excess': rat(maximum),
    'gain_over_q2': rat(F(119, 160)-maximum),
    'gain_over_pr923': rat(F(623, 720)-maximum),
    'dominant_monomial': [2, 2, 2],
    'all_monomial_excesses': [
        {'choices': list(m[0]), 'excess': rat(m[3]),
         'pair_weights': [rat(w) for w in m[1]]} for m in monomials
    ],
}
print(json.dumps(report, sort_keys=True, indent=2))
