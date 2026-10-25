#!/usr/bin/env python3
"""Exact finite sextic coefficient polynomials; exploratory, not a zero-free proof.

Uses NumPy only for integer vector arithmetic. Residue symbols and output energy
polynomials are exact. The annuli are sharp, not the smooth asymptotic profiles.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import isqrt
from pathlib import Path
import numpy as np

ROOTS = [(1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1)]


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def divide(x, y):
    a, b = x
    c, d = y
    q = norm(y)
    u, v = a*(c-d)+b*d, b*c-a*d
    return (u//q, v//q) if u % q == v % q == 0 else None


def prime_sieve(n):
    flags = bytearray(b'\x01')*(n+1)
    flags[:2] = b'\x00\x00'
    for p in range(2, isqrt(n)+1):
        if flags[p]:
            flags[p*p:n+1:p] = b'\x00'*((n-p*p)//p+1)
    return flags


def ideals(limit):
    # a+b*omega is the unique generator congruent to 1 modulo 3.
    # Exclude the prime over 2 as well as 3, matching fixed good-prime data.
    out = []
    radius = isqrt(4*limit//3)+2
    for b in range(-radius, radius+1):
        if b % 3:
            continue
        for a in range(-radius, radius+1):
            if a % 3 != 1 or (a % 2 == b % 2 == 0):
                continue
            q = a*a-a*b+b*b
            if 0 < q <= limit:
                out.append((q, (a, b)))
    return sorted(out)


def prime_ideals(items, prime_flags):
    out = []
    for q, x in items:
        p = isqrt(q)
        if (prime_flags[q] and q % 3 == 1) or (
            p*p == q and prime_flags[p] and p % 3 == 2
        ):
            out.append((q, x))
    return out


def factor(x, primes, prime_ids):
    left = x
    factors = []
    for idx, (q, p) in enumerate(primes):
        if q*q > norm(left):
            break
        while norm(left) % q == 0:
            quotient = divide(left, p)
            if quotient is None:
                break
            factors.append(idx)
            left = quotient
    if left != (1, 0):
        if left not in prime_ids:
            raise RuntimeError(('unfactored', x, left))
        factors.append(prime_ids[left])
    return tuple(factors)


def ff_power(a, b, exponent, p):
    ra, rb = np.ones_like(a), np.zeros_like(b)
    while exponent:
        if exponent & 1:
            ra, rb = (ra*a-rb*b) % p, (ra*b+rb*a-rb*b) % p
        a, b = (a*a-b*b) % p, (2*a*b-b*b) % p
        exponent //= 2
    return ra, rb


def local_codes(prime, rows):
    q, (c, d) = prime
    a = np.array([x[0] for x in rows], dtype=np.int64)
    b = np.array([x[1] for x in rows], dtype=np.int64)
    if d:
        p = q
        root = (-c*pow(d % p, -1, p)) % p
        values = (a+b*root) % p
        out = np.ones_like(values)
        base, exponent = values.copy(), (p-1)//6
        while exponent:
            if exponent & 1:
                out = out*base % p
            base = base*base % p
            exponent //= 2
        code = np.full(len(rows), -1, dtype=np.int8)
        for k, (u, v) in enumerate(ROOTS):
            code[out == (u+v*root) % p] = k
        code[values == 0] = 6
    else:
        p = isqrt(q)
        a, b = a % p, b % p
        u, v = ff_power(a, b, (q-1)//6, p)
        code = np.full(len(rows), -1, dtype=np.int8)
        for k, (x, y) in enumerate(ROOTS):
            code[(u == x % p) & (v == y % p)] = k
        code[(a == 0) & (b == 0)] = 6
    if np.any(code < 0):
        raise RuntimeError(('not a sixth root', prime))
    return code


def eval_poly(coeffs, z):
    value = Fraction(0)
    for c in reversed(coeffs):
        value = value*z+c
    return value


def interpolation_at(coeffs, target):
    degree = len(coeffs)-1
    nodes = [Fraction(1, 4)+Fraction(j, 2*degree) for j in range(degree+1)]
    total, absolute_weight = Fraction(0), Fraction(0)
    for j, x in enumerate(nodes):
        weight = Fraction(1)
        for k, y in enumerate(nodes):
            if k != j:
                weight *= (target-y)/(x-y)
        total += weight*eval_poly(coeffs, x)
        absolute_weight += abs(weight)
    return total, absolute_weight


def run_case(U, D):
    items = ideals(2*max(U, D))
    primes = prime_ideals(items, prime_sieve(2*max(U, D)))
    prime_ids = {p: i for i, (_, p) in enumerate(primes)}
    rows = []
    columns = []
    for q, x in items:
        if U <= q < 2*U:
            f = factor(x, primes, prime_ids)
            if all(f.count(p) < 6 for p in set(f)):
                rows.append(x)
        if D <= q < 2*D:
            f = factor(x, primes, prime_ids)
            if len(f) == len(set(f)):
                columns.append((x, f))
    if not rows or not columns:
        raise RuntimeError('empty experiment')
    degree = max(len(f) for _, f in columns)
    real = np.zeros((degree+1, len(rows)), dtype=np.int64)
    omega = np.zeros_like(real)
    diagonal = [0]*(2*degree+1)
    local = {}
    root_a = np.array([x for x, _ in ROOTS]+[0], dtype=np.int64)
    root_b = np.array([y for _, y in ROOTS]+[0], dtype=np.int64)
    masks = 0
    for _, factors in columns:
        code = np.zeros(len(rows), dtype=np.int8)
        for p in factors:
            if p not in local:
                local[p] = local_codes(primes[p], rows)
            this = local[p]
            code = np.where((code == 6) | (this == 6), 6, (code+this) % 6)
        k = len(factors)
        real[k] += root_a[code]
        omega[k] += root_b[code]
        diagonal[2*k] += int(np.count_nonzero(code != 6))
        masks += int(np.count_nonzero(code == 6))
    # Bound before vector contractions; no silent fixed-width integer overflow.
    if len(rows)*len(columns)**2 >= 2**60:
        raise RuntimeError('integer arithmetic bound exceeded')
    energy = [0]*(2*degree+1)
    for j in range(degree+1):
        for k in range(degree+1):
            energy[j+k] += int(np.sum(real[j]*real[k]-real[j]*omega[k]+omega[j]*omega[k]))
    centered = [x-y for x, y in zip(energy, diagonal)]
    reconstructed, weight = interpolation_at(centered, Fraction(-1))
    if reconstructed != eval_poly(centered, Fraction(-1)):
        raise RuntimeError('exact centered interpolation failed')
    # Independent direct accumulation at integer signs, versus quadratic polynomial.
    for sign in [-1, 1]:
        a = sum(sign**k*real[k] for k in range(degree+1))
        b = sum(sign**k*omega[k] for k in range(degree+1))
        direct = int(np.sum(a*a-a*b+b*b))
        if eval_poly(energy, Fraction(sign)) != direct:
            raise RuntimeError('energy identity failed')
    values = []
    for z in [Fraction(-1), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(2)]:
        full = eval_poly(energy, z)/D
        diag = eval_poly(diagonal, z)/D
        values.append({'z': str(z), 'moment_exact': str(full),
                       'diagonal_exact': str(diag),
                       'moment_over_U_float': float(full/U),
                       'centered_over_U_float': float((full-diag)/U)})
    return {'U': U, 'D': D, 'row_count': len(rows), 'column_count': len(columns),
            'max_omega': degree, 'collision_zeros_retained': masks,
            'energy_polynomial_integer_coefficients': energy,
            'diagonal_polynomial_integer_coefficients': diagonal,
            'centered_polynomial_integer_coefficients': centered,
            'exact_interpolation_verified': True,
            'equal_grid_extrapolation_weight_sum': str(weight), 'values': values}


def local_checks():
    items = ideals(300)
    primes = prime_ideals(items, prime_sieve(300))
    ids = {p:i for i, (_, p) in enumerate(primes)}
    count = 0
    for _, x in items:
        product = (1, 0)
        for p in factor(x, primes, ids):
            product = mul(product, primes[p][1])
        if product != x:
            raise RuntimeError('factor reconstruction failed')
        count += 1
    multiplicative = 0
    for prime in primes[:12]:
        xs = [x for _, x in items[:25]]
        pairs = [(x,y) for x in xs for y in xs]
        left = local_codes(prime, [mul(x,y) for x,y in pairs])
        cx = local_codes(prime, [x for x,y in pairs])
        cy = local_codes(prime, [y for x,y in pairs])
        right = np.where((cx == 6)|(cy == 6),6,(cx+cy)%6)
        if not np.array_equal(left,right):
            raise RuntimeError('multiplicativity with zero masks failed')
        if local_codes(prime,[prime[1]])[0] != 6:
            raise RuntimeError('natural zero failed')
        multiplicative += len(pairs)
    return {'factor_reconstructions': count, 'local_multiplicativity_checks': multiplicative,
            'split_and_inert_prime_examples': [list(p) for p in primes[:12]]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    cases = [(64,128),(128,256),(256,512),(512,1024),
             (256,4096),(400,8000),(576,13824),
             (1600,64000),(2500,125000)]
    report = {'scope': 'EXACT_FINITE_ALGEBRA_AND_EXPLORATORY_SHARP_ANNULI',
              'asymptotic_zero_free_claim': False, 'checks': local_checks(), 'cases': []}
    for U,D in cases:
        case = run_case(U,D)
        report['cases'].append(case)
        print(json.dumps({'U':U,'D':D,'rows':case['row_count'],'columns':case['column_count'],
              'max_omega':case['max_omega'],'mobius_moment_over_U':case['values'][0]['moment_over_U_float']}),flush=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
