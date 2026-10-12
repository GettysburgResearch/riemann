#!/usr/bin/env python3
"""Exact actual norm-ball Fourier transport and local zero/Gauss masks."""
from math import isqrt
import json
import sympy as sp
from check_crt_product_moments import local, mul, need, norm


def remainder(coefficients, modulus):
    x = sp.Symbol('x')
    polynomial = sp.Poly.from_dict({(i,): c for i, c in enumerate(coefficients) if c}, x, domain=sp.ZZ)
    return polynomial.rem(sp.Poly(sp.cyclotomic_poly(modulus, x), x, domain=sp.ZZ))


def transform(values, frequency):
    q = len(values)
    coefficients = [0]*q
    for u, value in enumerate(values):
        coefficients[-frequency*u % q] += value
    return coefficients


def circular_product(a, b):
    q = len(a)
    out = [0]*q
    left = [(i, value) for i, value in enumerate(a) if value]
    right = [(i, value) for i, value in enumerate(b) if value]
    for i, x in left:
        for j, y in right:
            out[(i+j) % q] += x*y
    return out


def norm_ball_weights(height):
    out = [0]*91
    cap = isqrt(4*height//3)+2
    for a in range(-cap, cap+1):
        for b in range(-cap, cap+1):
            if 0 < a*a-a*b+b*b <= height:
                u7, u13 = (a+2*b) % 7, (a+3*b) % 13
                residue = (u7+7*((u13-u7)*pow(7, -1, 13) % 13)) % 91
                out[residue] += 1
    return out


def gauss_controls():
    guards = 0
    for p, omega in ((7, 2), (13, 3)):
        length = 6*p
        eps = (1+omega) % p
        exponents = {pow(eps, j, p): j for j in range(6)}
        chi = {u: exponents[pow(u, (p-1)//6, p)] for u in range(1, p)}
        for d in range(6):
            transforms = []
            for b in range(p):
                coefficients = [0]*length
                for u in range(1, p):
                    coefficients[(p*d*chi[u]-6*b*u) % length] += 1
                transforms.append(coefficients)
            zero = remainder(transforms[0], length)
            need(zero == sp.Poly(p-1 if d == 0 else 0, zero.gens[0]), 'exact zero frequency mask')
            guards += 1
            for b in range(1, p):
                actual = remainder(transforms[b], length)
                if d == 0:
                    expected = sp.Poly(-1, actual.gens[0])
                else:
                    shift = (-p*d*chi[b]) % length
                    shifted = [0]*length
                    for j, value in enumerate(transforms[1]):
                        shifted[(j+shift) % length] += value
                    expected = remainder(shifted, length)
                need(actual == expected, 'exact nonzero local Gauss factor')
                guards += 1
            if d:
                conjugate = [transforms[1][-j % length] for j in range(length)]
                square = remainder(circular_product(transforms[1], conjugate), length)
                need(square == sp.Poly(p, square.gens[0]), 'exact Gauss squared norm')
                guards += 1
    return guards


def run():
    q = 91
    t = 34
    unsigned = []
    signed = []
    for u in range(q):
        positive = negative = (1, 0)
        for p, omega in ((7, 2), (13, 3)):
            a, b = local(u, p, omega)
            positive = mul(positive, (1+a, b))
            negative = mul(negative, (1-a, -b))
        unsigned.append(norm(positive)**2)
        signed.append(norm(negative)**2)
    need(all(signed[u] == unsigned[t*u % q] for u in range(q)), 'pointwise signed translation')
    fourier = [transform(unsigned, b) for b in range(q)]
    expected = ((60, 1, 1734, 1878), (120, 2, 3666, 3522), (240, 3, 7134, 6894))
    panels = []
    for H, reference in zip((16, 32, 64), expected):
        weights = norm_ball_weights(H)
        signed_sum = sum(x*y for x, y in zip(signed, weights))
        unsigned_sum = sum(x*y for x, y in zip(unsigned, weights))
        need((sum(weights), max(weights), signed_sum, unsigned_sum) == reference,
             'complete actual lattice census and fourth sums')
        numerator = [0]*q
        for b in range(1, q):
            moved = transform(weights, -t*b)
            original = transform(weights, -b)
            difference = [x-y for x, y in zip(moved, original)]
            term = circular_product(fourier[b], difference)
            numerator = [x+y for x, y in zip(numerator, term)]
        reduced = remainder(numerator, q)
        need(reduced == sp.Poly(q*(signed_sum-unsigned_sum), reduced.gens[0]),
             'exact cyclotomic Fourier discrepancy identity')
        panels.append({'H': H, 'rows': sum(weights), 'maximum_residue_multiplicity': max(weights),
                       'signed_fourth_sum': signed_sum, 'unsigned_fourth_sum': unsigned_sum,
                       'exact_fourier_difference': signed_sum-unsigned_sum})
    return {'status': 'PASS_EXACT_SHORT_NORM_BALL_FOURIER_AND_GAUSS_MASKS',
            'modulus_norm': q, 'translator': t, 'panels': panels,
            'local_gauss_and_mask_guards': gauss_controls(),
            'arithmetic': 'integer cyclotomic polynomial remainders; no floating acceptance',
            'conditional_unit_nonreturn_analytic_input_verified_here': False,
            'native_sharp_band_profile_used': False, 'short_row_upper_bound_proved': False,
            'rh_proved': False}


if __name__ == '__main__':
    print(json.dumps(run(), sort_keys=True, indent=2))
