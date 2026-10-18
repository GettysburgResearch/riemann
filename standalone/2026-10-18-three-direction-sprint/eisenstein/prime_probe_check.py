"""Exact F_12 cubic-Gauss interaction graph and finite probe inversion.

The individual unit Gauss phases cancel by a diagonal gauge. This is an
actual prime-ideal interaction experiment, not random replacement phases.
It does not certify an asymptotic cancellation estimate.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations
from math import isqrt, prod
from pathlib import Path
import hashlib
import json
import sys

private = Path(__file__).with_name('_packages')
if private.exists():
    sys.path.insert(0, str(private))
from flint import fmpz


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def add(x, y):
    return x[0]+y[0], x[1]+y[1]


def neg(x):
    return -x[0], -x[1]


def mul(x, y):
    # zeta_3^2+zeta_3+1=0.
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]-x[1]*y[1]


roots = ((1, 0), (0, 1), (-1, -1))


def main():
    rows = []
    k = 1
    while len(rows) < 12:
        t = 216*k
        p = t**4-t*t+1
        if fmpz(p).is_prime():
            require(p < 2**64, 'Finite primality-fixture size escaped its declared range.')
            r = (-pow(t, -1, p)) % p
            require((pow(r, 4, p)-r*r+1) % p == 0, 'Wrong F12 residue embedding.')
            require((1+t*r) % p == 0, 'Generator not in its actual prime ideal.')
            rows.append({'k': k, 't': t, 'norm': p, 'zeta12_mod_prime': r})
        k += 1
    size = len(rows)
    sextic = [[None]*size for _ in rows]
    pair_cases = 0
    for i, row in enumerate(rows):
        p, r = row['norm'], row['zeta12_mod_prime']
        zeta6 = r*r % p
        require(pow(zeta6, 3, p) == p-1, 'Chosen sixth root has wrong order.')
        for j, other in enumerate(rows):
            if i == j:
                continue
            value = (1+other['t']*r) % p
            require(value != 0, 'Distinct test ideals unexpectedly share a prime.')
            symbol = pow(value, (p-1)//6, p)
            sextic[i][j] = next(e for e in range(6) if pow(zeta6, e, p) == symbol)
            pair_cases += 1
    for i, j in combinations(range(size), 2):
        require(sextic[i][j] == sextic[j][i], 'Actual sixth-power reciprocity mismatch.')
    # chi_6(P_j/P_i)^4 = zeta_3^(2*exponent).
    edge = [[None if i == j else 2*sextic[i][j] % 3
             for j in range(size)] for i in range(size)]
    b = []
    for mask in range(1 << size):
        inds = [j for j in range(size) if mask >> j & 1]
        b.append(roots[sum(edge[i][j] for i, j in combinations(inds, 2)) % 3])
    # Exact squarefree incidence-algebra inverse of the ACTUAL Gauss graph.
    a = [(0, 0)]*(1 << size)
    a[0] = (1, 0)
    for mask in range(1, 1 << size):
        value = (0, 0)
        sub = (mask-1) & mask
        while True:
            value = add(value, mul(a[sub], b[mask ^ sub]))
            if sub == 0:
                break
            sub = (sub-1) & mask
        a[mask] = neg(value)
    equations = 0
    for mask in range(1 << size):
        value = (0, 0)
        sub = mask
        while True:
            value = add(value, mul(a[sub], b[mask ^ sub]))
            if sub == 0:
                break
            sub = (sub-1) & mask
        require(value == ((1, 0) if mask == 0 else (0, 0)),
                'A native squarefree dual column survived the exact inverse.')
        equations += 1
    # Prime-product filters cancel all primes but generally leave semiprimes.
    semiprime_nonzero = 0
    for i, j in combinations(range(size), 2):
        mask = (1 << i) | (1 << j)
        residual = add(b[mask], (-1, 0))
        if residual != (0, 0):
            semiprime_nonzero += 1
    require(semiprime_nonzero > 0, 'Actual interaction graph missed the nonmultiplicative obstruction.')
    # Rigorous rational upper resources: |A+B*zeta3|<=|A|+|B|.
    mass_half = Q(0)
    mass_one = Q(0)
    target_tail = Q(0)
    by_order = []
    for order in range(size+1):
        selected = [mask for mask in range(1 << size) if mask.bit_count() == order]
        by_order.append({'order': order, 'columns': len(selected),
                         'max_coordinate_L1': max(abs(a[m][0])+abs(a[m][1]) for m in selected)})
        for mask in selected:
            inds = [j for j in range(size) if mask >> j & 1]
            norm = prod(rows[j]['norm'] for j in inds)
            amplitude = abs(a[mask][0])+abs(a[mask][1])
            # The product of prime square-root floors is a rigorous lower
            # denominator; it also keeps a compact common rational resource.
            mass_half += Q(amplitude, prod(isqrt(rows[j]['norm']) for j in inds))
            mass_one += Q(amplitude, norm)
            if mask:
                # All actual Q>=10^12, and the uniform strip bound
                # |z_Q(s)|<=2Q^(-5/6)<=2*10^(-9), Re s>1/2.
                require(all(rows[j]['norm'] >= 10**12 for j in inds),
                        'Target-strip resource used outside its actual prime range.')
                target_tail += amplitude*Q(2, 10**9)**order
    require(mass_half < Q(100001, 100000), 'Finite future-probe root resource exceeds 1.00001.')
    require(mass_one < Q(1000000001, 10**9), 'Finite dual-root resource exceeds 1.000000001.')
    require(target_tail < Q(1, 10**6), 'Principal perturbation is not certified zero-safe.')
    # One concrete shared-prime output must remain: n=P,c=P produces
    # -lambda(P)^2/Q, with the row nonunit indicator retained.
    require(a[1] == (-1, 0), 'Prime inverse has the wrong sign.')
    result = {
        'status': 'PASS_ACTUAL_F12_FINITE_GAUSS_GRAPH_PROBE',
        'finite_scope_only': True,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'field': 'Q(zeta_12)', 'generator': '1+216*k*zeta_12',
        'primes': rows, 'ordered_sextic_symbol_checks': pair_cases,
        'sextic_exponents': sextic, 'cubic_cross_exponents': edge,
        'complete_squarefree_inverse_columns': equations,
        'nonzero_semiprime_residuals_of_simple_prime_product': semiprime_nonzero,
        'inverse_by_order': by_order,
        'raw_future_root_mass_upper': str(mass_half),
        'dual_root_mass_upper': str(mass_one),
        'principal_perturbation_upper': str(target_tail),
        'inverse_coefficients_zeta3_basis': a,
        'scope': 'Exact actual F12 prime reciprocity graph; unit Gauss phases factored by proved twisted multiplicativity. No asymptotic moment or zero-free theorem is inferred.'}
    path = Path(__file__).with_name('PRIME_PROBE_CHECKS.json')
    path.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in (
        'status', 'ordered_sextic_symbol_checks', 'complete_squarefree_inverse_columns',
        'nonzero_semiprime_residuals_of_simple_prime_product', 'inverse_by_order')}))


if __name__ == '__main__':
    main()
