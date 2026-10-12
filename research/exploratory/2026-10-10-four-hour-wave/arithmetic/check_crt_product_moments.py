#!/usr/bin/env python3
"""Exact complete-residue product controls; no infinite moment estimate."""
from fractions import Fraction as F
from itertools import product
from math import comb, prod
import json

ROOTS = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def mul(left, right):
    a, b = left
    c, d = right
    return a*c-b*d, a*d+b*c+b*d


def norm(value):
    a, b = value
    return a*a+a*b+b*b


def local(u, p, omega):
    if u % p == 0:
        return (0, 0)
    residue = pow(u, (p-1)//6, p)
    eps = (1+omega) % p
    exponents = [j for j in range(6) if pow(eps, j, p) == residue]
    need(len(exponents) == 1, 'unique literal split sixth-residue character')
    return ROOTS[exponents[0]]


def local_moment(k, rho):
    diagonal = 1+rho*(comb(2*k, k)-1)
    extra = 2*rho*sum(comb(k, j+6*h)*comb(k, j)
                     for h in range(1, k//6+1) for j in range(k-6*h+1))
    return diagonal+extra, diagonal


def cumulant(rs):
    A = prod(1+r for r in rs)
    B = prod(1+2*r for r in rs)
    D = prod(1+5*r for r in rs)
    return D-4*B+8*A-3-2*A*A


def run():
    prime_fields = ((7, 2), (13, 3), (19, 7))
    modulus = 7*13*19
    rho = [F(p-1, p) for p, _ in prime_fields]
    values = []
    for u in range(modulus):
        value = (1, 0)
        for p, omega in prime_fields:
            a, b = local(u, p, omega)
            value = mul(value, (1-a, -b))
        values.append(value)
    need((sum(v[0] for v in values), sum(v[1] for v in values)) == (modulus, 0),
         'exact product mean is one')
    squares = [mul(v, v) for v in values]
    need((sum(v[0] for v in squares), sum(v[1] for v in squares)) == (modulus, 0),
         'exact second mixed moment is one')
    mixed = [mul(s, (v[0]+v[1], -v[1])) for s, v in zip(squares, values)]
    B = prod(1+2*r for r in rho)
    need(F(sum(v[0] for v in mixed), modulus) == B and sum(v[1] for v in mixed) == 0,
         'exact X^2 conjugate X moment')
    moments = []
    for k in range(1, 9):
        actual = F(sum(norm(v)**k for v in values), modulus)
        factors = [local_moment(k, r) for r in rho]
        expected = prod(value[0] for value in factors)
        diagonal = prod(value[1] for value in factors)
        need(actual == expected, 'exact all-order local moment formula')
        need(actual == diagonal if k < 6 else actual > diagonal,
             'first extra sextic collision occurs at k=6')
        moments.append({'k': k, 'exact_moment': str(actual), 'torus_mask_diagonal': str(diagonal)})
    centered = [(a-1, b) for a, b in values]
    variance = F(sum(norm(v) for v in centered), modulus)
    pseudo = [mul(v, v) for v in centered]
    need(sum(v[0] for v in pseudo) == sum(v[1] for v in pseudo) == 0,
         'centered pseudovariance is zero')
    fourth = F(sum(norm(v)**2 for v in centered), modulus)
    kappa = fourth-2*variance**2
    need(kappa == cumulant(rho) == F(8445096, 229957), 'exact positive centered cumulant')
    vertex_values = [F(3985434, 117649), F(87023, 2401), F(1893, 49), F(41)]
    for rs in product((F(6, 7), F(1)), repeat=3):
        value = cumulant(rs)
        need(value == vertex_values[sum(r == 1 for r in rs)] and value >= vertex_values[0],
             'all rational cube vertices and positive minimum')
    return {'status': 'PASS_EXACT_CRT_PRODUCT_MOMENTS_AND_POSITIVE_CUMULANT',
            'complete_rows': modulus, 'prime_ideal_norms': [7, 13, 19],
            'moments': moments, 'centered_fourth_cumulant': str(kappa),
            'uniform_three_prime_cumulant_lower_bound': str(vertex_values[0]),
            'native_sharp_band_used': False, 'infinite_short_row_bound_proved': False,
            'rh_proved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
