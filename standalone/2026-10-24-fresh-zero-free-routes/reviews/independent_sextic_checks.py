#!/usr/bin/env python3
"""Independent finite checks of the packet's sextic experiment.

Expected residue symbols use arbitrary-precision arithmetic in
Z[X]/(X^2+X+1), followed by ideal divisibility. They do not use the author's
split-prime scalar reduction, inert-prime NumPy powering, ROOTS table,
factorization routine, or quadratic energy contraction.

The implementation under review is imported only to obtain its enumerated
ideals/primes and its actual local codes and small-annulus energy polynomial.
Ideal counts are checked against the independent divisor-sum formula for
Q(sqrt(-3)), after omitting the primes over 2 and 3. The tested finite ranges
are deliberate; this program proves no asymptotic estimate.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
import json
from pathlib import Path


def product(left, right):
    # Multiply polynomials and reduce X^2 = -X-1.
    a, b = left
    c, d = right
    constant, linear, quadratic = a*c, a*d+b*c, b*d
    return constant-quadratic, linear-quadratic


def power_mod_integer(value, exponent, modulus):
    answer = (1, 0)
    value = tuple(x % modulus for x in value)
    while exponent:
        if exponent % 2:
            answer = tuple(x % modulus for x in product(answer, value))
        value = tuple(x % modulus for x in product(value, value))
        exponent //= 2
    return answer


def quotient_if_integral(value, divisor):
    # Matrix for multiplication by c+dX is [[c,-d],[d,c-d]].
    a, b = value
    c, d = divisor
    determinant = c*c-c*d+d*d
    first = (c-d)*a+d*b
    second = -d*a+c*b
    if first % determinant or second % determinant:
        return None
    return first//determinant, second//determinant


def root_table():
    # 1+omega = exp(pi*i/3), with omega = exp(2*pi*i/3).
    roots = []
    value = (1, 0)
    for _ in range(6):
        roots.append(value)
        value = product(value, (1, 1))
    if value != (1, 0) or len(set(roots)) != 6:
        raise RuntimeError('independent sixth-root construction failed')
    return roots


ROOTS_INDEPENDENT = root_table()


def expected_local(prime, value):
    q, generator = prime
    if quotient_if_integral(value, generator) is not None:
        return 6
    powered = power_mod_integer(value, (q-1)//6, q)
    matches = []
    for k, root in enumerate(ROOTS_INDEPENDENT):
        difference = powered[0]-root[0], powered[1]-root[1]
        if quotient_if_integral(difference, generator) is not None:
            matches.append(k)
    if len(matches) != 1:
        raise RuntimeError(('independent local root is not unique', prime, value, matches))
    return matches[0]


def independent_factor(value, primes):
    left = value
    indices = []
    # Deliberately no author's norm-square stopping rule or factor lookup.
    for index, (_, generator) in enumerate(primes):
        while left != (1, 0):
            quotient = quotient_if_integral(left, generator)
            if quotient is None:
                break
            indices.append(index)
            left = quotient
    if left != (1, 0):
        raise RuntimeError(('independent factorization incomplete', value, left))
    return tuple(indices)


def expected_ideal_count(n):
    if n % 2 == 0 or n % 3 == 0:
        return 0
    total = 0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            residue = divisor % 3
            total += 0 if residue == 0 else 1 if residue == 1 else -1
    return total


def load_author(path):
    spec = importlib.util.spec_from_file_location('reviewed_sextic_experiment', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check(author):
    items = author.ideals(300)
    actual_counts = Counter(q for q, _ in items)
    for n in range(1, 301):
        expected = expected_ideal_count(n)
        if actual_counts[n] != expected:
            raise RuntimeError(('ideal count mismatch', n, actual_counts[n], expected))

    primes = author.prime_ideals(items, author.prime_sieve(300))
    test_values = [(a, b) for a in range(-6, 7) for b in range(-6, 7)]
    compared = nonunits = orientation_sensitive = 0
    for prime in primes:
        actual = author.local_codes(prime, test_values).tolist()
        for value, code in zip(test_values, actual):
            expected = expected_local(prime, value)
            if code != expected:
                raise RuntimeError(('local residue mismatch', prime, value, code, expected))
            compared += 1
            nonunits += expected == 6
            orientation_sensitive += expected in (1, 2, 4, 5)

    small_items = author.ideals(256)
    small_primes = author.prime_ideals(small_items, author.prime_sieve(256))
    rows, columns = [], []
    for q, value in small_items:
        factors = independent_factor(value, small_primes)
        multiplicities = Counter(factors)
        if 64 <= q < 128 and all(v < 6 for v in multiplicities.values()):
            rows.append(value)
        if 128 <= q < 256 and len(factors) == len(multiplicities):
            columns.append((value, factors))
    if (len(rows), len(columns)) != (19, 37):
        raise RuntimeError(('unexpected independently factored annuli', len(rows), len(columns)))

    # Each row-column character is rebuilt by arbitrary-precision multiplication.
    row_terms = []
    for row in rows:
        terms = []
        for _, factors in columns:
            symbol = (1, 0)
            for index in factors:
                code = expected_local(small_primes[index], row)
                local = (0, 0) if code == 6 else ROOTS_INDEPENDENT[code]
                symbol = product(symbol, local)
            terms.append((len(factors), symbol))
        row_terms.append(terms)

    author_case = author.run_case(64, 128)
    coefficients = author_case['energy_polynomial_integer_coefficients']
    energies = []
    for z in map(Fraction, (-1, '1/4', '1/2', '3/4', 1, 2)):
        energy = Fraction(0)
        for terms in row_terms:
            a = sum((z**degree)*symbol[0] for degree, symbol in terms)
            b = sum((z**degree)*symbol[1] for degree, symbol in terms)
            energy += a*a-a*b+b*b
        polynomial = sum(Fraction(c)*z**k for k, c in enumerate(coefficients))
        if energy != polynomial:
            raise RuntimeError(('independent exact energy mismatch', z, energy, polynomial))
        energies.append({'z': str(z), 'full_energy': str(energy)})

    return {
        'status': 'INDEPENDENT_FINITE_REVIEW_CHECKS_PASS',
        'ideal_norm_count_comparisons': 300,
        'prime_ideals_tested': len(primes),
        'local_residue_comparisons': compared,
        'natural_nonunit_cases': nonunits,
        'orientation_sensitive_cases': orientation_sensitive,
        'small_annulus_independent_energies': energies,
        'scope': 'Executed finite Eisenstein cases only; no asymptotic estimate.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path,
                        default=Path(__file__).resolve().parents[1]/'sextic_interpolation_experiment.py')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = check(load_author(args.source))
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
