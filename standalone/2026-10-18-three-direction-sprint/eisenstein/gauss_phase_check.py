"""Exact finite-field Gauss/Jacobi phase checks at actual exterior primes.

No floating point is needed: equality at zeta_p is checked modulo Phi_p.
The finite ray table is a finite experiment, not a global conductor proof.
"""
from math import gcd, isqrt
from pathlib import Path
import hashlib
import json


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    a, b = x
    c, d = y
    return a*c-b*d, a*d+b*c-b*d


def norm(x):
    a, b = x
    return a*a-a*b+b*b


def conjugate(x):
    return x[0]-x[1], -x[1]


UNITS = ((1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1), (0, -1))
ZERO = (0, 0)


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def quotient_unit(x, alpha):
    top = mul(x, conjugate(alpha))
    q = norm(alpha)
    require(top[0] % q == 0 and top[1] % q == 0, 'Not an exact ideal associate.')
    answer = top[0]//q, top[1]//q
    require(answer in UNITS, 'Associate quotient is not a unit.')
    return UNITS.index(answer)


def cyclotomic_equal(left, right):
    """Two O[Z]/(Z^p-1) arrays agree at primitive zeta_p iff diff constant."""
    difference = [add(a, neg(b)) for a, b in zip(left, right, strict=True)]
    return all(x == difference[0] for x in difference)


def cyclic_product(left, right):
    p = len(left)
    result = [ZERO]*p
    for a, x in enumerate(left):
        if x == ZERO:
            continue
        for b, y in enumerate(right):
            if y != ZERO:
                result[(a+b) % p] = add(result[(a+b) % p], mul(x, y))
    return result


def field_data(alpha, p, inert):
    q = norm(alpha)
    if inert:
        elements = [(a, b) for a in range(p) for b in range(p)]
        def multiplication(x, y):
            a, b = mul(x, y)
            return a % p, b % p
        def power(x, e):
            result = (1, 0)
            while e:
                if e & 1:
                    result = multiplication(result, x)
                x = multiplication(x, x)
                e //= 2
            return result
        unit_map = {(a % p, b % p): k for k, (a, b) in enumerate(UNITS)}
        def phase(x):
            return unit_map[power(x, (q-1)//6)]
        def complement(x):
            return (1-x[0]) % p, -x[1] % p
        def additive(x):
            return (-2*x[0]+x[1]) % p
    else:
        elements = list(range(p))
        root = (-alpha[0]*pow(alpha[1], -1, p)) % p
        require((root*root+root+1) % p == 0, 'Wrong prime-ideal reduction.')
        unit_map = {(a+b*root) % p: k for k, (a, b) in enumerate(UNITS)}
        def phase(x):
            return unit_map[pow(x, (p-1)//6, p)]
        def complement(x):
            return (1-x) % p
        def additive(x):
            return ((2*alpha[0]-alpha[1])*x) % p
    zero = elements[0]
    def ch(x, j):
        return ZERO if x == zero else UNITS[(phase(x)*j) % 6]
    return elements, zero, ch, complement, additive


def one_prime(alpha, p, inert):
    q = norm(alpha)
    elements, zero, ch, complement, additive = field_data(alpha, p, inert)
    G = [[ZERO]*p for _ in range(3)]
    J12 = ZERO
    J22 = ZERO
    for x in elements:
        for j in (1, 2, 3):
            k = additive(x)
            G[j-1][k] = add(G[j-1][k], ch(x, j))
        J12 = add(J12, mul(ch(x, 1), ch(complement(x), 2)))
        J22 = add(J22, mul(ch(x, 2), ch(complement(x), 2)))
    require(norm(J12) == q and norm(J22) == q, 'Jacobi norm differs.')
    target = [mul(J12, x) for x in G[2]]
    require(cyclotomic_equal(cyclic_product(G[0], G[1]), target),
            'The exact sextic-times-cubic Gauss identity failed.')
    cube = cyclic_product(cyclic_product(G[1], G[1]), G[1])
    target_cube = [(q*J22[0], q*J22[1])]+[ZERO]*(p-1)
    require(cyclotomic_equal(cube, target_cube), 'The exact cubic Gauss cube failed.')
    # Jacobi duplication at the actual element 4, which is a unit here.
    four = (4 % p, 0) if inert else 4 % p
    require(J12 == mul(J22, conjugate(ch(four, 1))), 'Jacobi duplication phase differs.')
    lambda_unit = quotient_unit(neg(J22), alpha)
    # Classical quadratic normalized Gauss phase gamma_3=i^h.
    if inert:
        legendre_minus1 = 1 if p % 4 == 1 else -1
        h = 2 if legendre_minus1 == 1 else 0
    else:
        k = (2*alpha[0]-alpha[1]) % p
        sign = pow(k, (p-1)//2, p)
        h = (0 if p % 4 == 1 else 1)+(0 if sign == 1 else 2)
    unit_four = UNITS.index(ch(four, 1))
    G_exponent_12 = (-2*unit_four+3*h) % 12
    correction_unit_12 = (-2*lambda_unit-G_exponent_12) % 12
    return {'alpha': list(alpha), 'norm': q, 'rational_p': p, 'inert': inert,
            'Jacobi_12': list(J12), 'Jacobi_22': list(J22),
            'Lambda_relative_primary_unit_6': lambda_unit,
            'quadratic_phase_i_power': h % 4,
            'vartheta_relative_primary_minus1_unit_12': correction_unit_12}


def main():
    cap = 193
    ideals = []
    radius = 2*isqrt(cap)+2
    for a in range(-radius, radius+1):
        for b in range(-radius, radius+1):
            q = norm((a, b))
            if a % 3 == 1 and b % 3 == 0 and gcd(q, 6) == 1 and q <= cap and prime(q):
                ideals.append(((a, b), q, False))
    for p in range(5, isqrt(cap)+1):
        if prime(p) and p % 3 == 2:
            ideals.append(((-p, 0), p, True))
    rows = [one_prime(*item) for item in sorted(ideals, key=lambda x: (norm(x[0]), x[0]))]
    ray_checks = []
    for modulus in (4, 12, 24, 36):
        table = {}
        collisions = []
        for row in rows:
            residue = tuple(a % modulus for a in row['alpha'])
            value = row['vartheta_relative_primary_minus1_unit_12']
            if residue in table and table[residue] != value:
                collisions.append({'residue': residue, 'values': [table[residue], value]})
            table[residue] = value
        ray_checks.append({'element_modulus': modulus, 'occupied_classes': len(table),
                           'phase_conflicts': collisions,
                           'scope': 'Finite ray experiment; no global conductor conclusion.'})
    table4 = {tuple(a % 4 for a in row['alpha']):
              row['vartheta_relative_primary_minus1_unit_12'] for row in rows}
    failures = []
    for a, va in table4.items():
        for b, vb in table4.items():
            product = tuple(x % 4 for x in mul(a, b))
            if product in table4 and (va+vb) % 12 != table4[product]:
                failures.append({'a': a, 'b': b, 'product': product,
                                 'phase_a': va, 'phase_b': vb,
                                 'phase_product_class': table4[product]})
    require(len(table4) == 12 and len(failures) == 54,
            'Exact finite ray multiplicativity obstruction changed.')
    output = {'status': 'PASS_EXACT_PRIME_GAUSS_PHASE_IDENTITIES',
              'scope': 'Finite actual exterior prime ideals only.',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'norm_cap': cap, 'prime_ideals': len(rows), 'cases': rows,
              'ray_experiments': ray_checks,
              'ray4_multiplicativity_obstruction': {'complete_unit_classes': 12,
                  'failed_pairs': len(failures), 'first_counterexample': failures[0],
                  'scope': 'Rejects this conductor-dividing-4 character table only.'}}
    path = Path(__file__).with_name('GAUSS_PHASE_CHECKS.json')
    path.write_text(json.dumps(output, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': output['status'], 'prime_ideals': len(rows),
                      'ray_conflicts': [len(row['phase_conflicts']) for row in ray_checks]}))


if __name__ == '__main__':
    main()
