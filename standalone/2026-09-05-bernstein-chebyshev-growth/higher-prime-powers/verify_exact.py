#!/usr/bin/env python3
"""Finite exact controls for HP-1--HP-6. This program does not prove RH.

Python >=3.10; standard library only. No actual prime logarithm, zeta value,
zero census, or infinite norm is evaluated. Analytic proofs are in PROOF.md.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT_BLOBS = {
    'GROWTH.md': 'c19930a24cefb6d5543098b9958f47a1d71acd87',
    'verify_exact.py': '44bf0d6ac36d9bc6f5e4e7019ebc7b14eeb2deda',
    'arithmetic-laguerre/PROOF.md': 'aff32d3b2078c3c895bd77f02e71fbe1fcfc3b49',
    'arithmetic-laguerre/verify_arithmetic.py': '5280ba28c9580bb7b324f0a43cf169b3de503335',
}


def degree(n: int) -> None:
    if type(n) is not int or n < 0:
        raise ValueError('degree must be a nonnegative integer, not bool/float')


def trim(p: list[Q]) -> list[Q]:
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(a: list[Q], b: list[Q]) -> list[Q]:
    out = [Q(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(b):
        out[j] += x
    return trim(out)


def scale(p: list[Q], c: Q) -> list[Q]:
    return trim([c*x for x in p])


def derivative(p: list[Q]) -> list[Q]:
    return [Q(0)] if len(p) == 1 else [j*p[j] for j in range(1, len(p))]


def ordinary(n: int) -> list[Q]:
    degree(n)
    return [Q((-1)**j*comb(n, j), factorial(j)) for j in range(n+1)]


def minus_one(n: int) -> list[Q]:
    degree(n)
    if n == 0:
        return [Q(1)]
    return [Q(0)] + [Q((-1)**j*comb(n-1, j-1), factorial(j))
                    for j in range(1, n+1)]


def evaluate(p: list[Q], x: Q) -> Q:
    out = Q(0)
    for c in reversed(p):
        out = out*x+c
    return out


def laplace(p: list[Q], rate: Q, argument: Q = Q(1)) -> Q:
    if rate <= 0:
        raise ValueError('Laplace rate must be positive')
    return sum((c*argument**j*factorial(j)/rate**(j+1)
                for j, c in enumerate(p)), Q(0))


def exponential_jet(tau: Q, last: int) -> list[Q]:
    """Coefficients of exp(tau*w/(1+w)), without calling Laguerre."""
    degree(last)
    out = [Q(1)]
    for n in range(1, last+1):
        out.append(sum((k*tau*(-1)**(k-1)*out[n-k]
                        for k in range(1, n+1)), Q(0))/n)
    return out


def gram(x: Q, y: Q) -> Q:
    if x < 1 or y < 1:
        raise ValueError('atom nodes must be at least one')
    return min(x, y)/max(x, y)**2-Q(1)/(x*x*y*y)


def step_norm(nodes: list[Q], weights: list[Q]) -> Q:
    if len(nodes) != len(weights) or not nodes:
        raise ValueError('nonempty equal-length node and weight lists required')
    if min(nodes) < 1:
        raise ValueError('atom nodes must be at least one')
    edges = sorted(set([Q(1)]+[x**3 for x in nodes]))
    total = Q(0)
    for lo, hi in zip(edges, edges[1:]):
        mid = (lo+hi)/2
        tail = sum((c/x**2 for x, c in zip(nodes, weights) if x**3 >= mid), Q(0))
        total += (hi-lo)*tail*tail
    return total


G = tuple[Q, Q]

def ga(a: G, b: G) -> G:
    return a[0]+b[0], a[1]+b[1]


def gm(a: G, b: G) -> G:
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]


def gd(a: G, b: G) -> G:
    den = b[0]*b[0]+b[1]*b[1]
    if not den:
        raise ValueError('zero Gaussian denominator')
    return (a[0]*b[0]+a[1]*b[1])/den, (a[1]*b[0]-a[0]*b[1])/den


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def canonical(obj: object) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, allow_nan=False)+'\n'


def verify() -> dict:
    counts: Counter = Counter()

    def require(ok: bool, group: str) -> None:
        if not ok:
            raise ValueError('failed exact check: '+group)
        counts[group] += 1

    lock = json.loads((HERE/'SOURCE_LOCK.json').read_text())
    require(lock['parent_commit'] == 'a895f734fc4243dbe81e1a0c5a17cf978a744962', 'parent_source_lock')
    require(lock['parent_git_blobs'] == PARENT_BLOBS, 'parent_source_lock')
    for name, sha in PARENT_BLOBS.items():
        require(git_blob((HERE.parent/name).read_bytes()) == sha, 'parent_source_lock')

    for n in range(1, 25):
        require(minus_one(n) == add(ordinary(n), scale(ordinary(n-1), Q(-1))), 'laguerre_difference')
        require(derivative(minus_one(n)) == scale(ordinary(n-1), Q(-1)), 'laguerre_derivative')
        require(laplace(ordinary(n), Q(1, 2)) == 2*(-1)**n, 'constant_source_correction')
        for r in range(1, 6):
            lhs = add(scale(minus_one(n), Q(-2*r)), scale(derivative(minus_one(n)), Q(3*r)))
            rhs = scale(add(scale(ordinary(n), Q(2)), ordinary(n-1)), Q(-r))
            require(lhs == rhs, 'integration_by_parts_polynomial')
        for r in range(1, 9):
            expected = Q((-1)**n*3*r, (2*r-1)**2)*Q(r+1, 2*r-1)**(n-1)
            require(laplace(minus_one(n), Q(2*r-1), Q(3*r)) == expected, 'power_continuum_integral')
        require(laplace(minus_one(n), Q(3), Q(6)) == Q(2*(-1)**n, 3), 'square_boundary_term')

    for tau in [Q(1, 3), Q(1), Q(3), Q(7, 2), Q(12)]:
        jet = exponential_jet(tau, 32)
        for n, val in enumerate(jet):
            require(val == (-1)**n*evaluate(minus_one(n), tau), 'independent_exponential_jet')

    model_norms = []
    # Positive continuous controls theta_*(x)=x-x^(1-6a), not actual primes.
    for a in [Q(1, 12), Q(1, 6), Q(1, 4), Q(1, 2), Q(1), Q(2)]:
        rate = a+Q(1, 2)
        ratio = (a-Q(1, 2))/rate
        coeff = [-ratio**n/rate for n in range(25)]
        r0 = -(1-6*a)/(3+6*a)
        require(r0 == 1+Q(2, 3)*coeff[0], 'degree_zero_endpoint')
        norm_a = Q(1, 2)/a
        norm_r = (2*ratio+1)**2/(18*a)
        require(norm_r <= norm_a, 'square_model_infinite_geometric_norm')
        partial = Q(0)
        for n in range(1, 25):
            direct = -(1-6*a)*laplace(minus_one(n), 3+6*a, Q(6))
            shifted = (2*coeff[n]+coeff[n-1])/3
            require(direct == shifted, 'square_model_source_and_shift')
            partial += direct**2
        require(partial <= norm_r, 'square_model_partial_norm')
        model_norms.append({'a': str(a), 'source_norm_squared': str(norm_a),
                            'residual_norm_squared': str(norm_r)})

    node_sets = [[Q(x) for x in xs] for xs in
                 [[1, 2, 3], [2, 3, 5, 7], [8, 16, 27, 32], [2, 2, 4, 9]]]
    node_sets += [[Q(3, 2), Q(5, 2), Q(7, 2)]]
    kernel_receipts = []
    for nodes in node_sets:
        for x in nodes:
            for y in nodes:
                require(gram(x, y) == (min(x, y)**3-1)/(x*x*y*y), 'rational_atom_gram')
        for offset in range(7):
            weights = [Q((-1)**(i+offset)*(i+offset+1), i+1) for i in range(len(nodes))]
            matrix = sum((c*d*gram(x, y) for x, c in zip(nodes, weights)
                          for y, d in zip(nodes, weights)), Q(0))
            physical = step_norm(nodes, weights)
            require(matrix == physical, 'gram_equals_step_square')
            require(matrix >= 0, 'signed_cross_term_positivity')
        kernel_receipts.append({'nodes': [str(x) for x in nodes],
                                'last_norm_squared': str(matrix)})

    for n in range(1, 13):
        for r in range(3, 25):
            val = Q(3*r, (2*r-1)**2)*Q(r+1, 2*r-1)**(n-1)
            require(val >= Q(3, 4*r)*Q(1, 2)**(n-1), 'continuum_harmonic_lower_bound')

    for gamma in [Q(1), Q(3), Q(14), Q(29, 2)]:
        rho = (Q(1, 2), gamma)
        w0 = gd((Q(3, 2), -gamma), (Q(3, 2), gamma))
        one_plus = ga((Q(1), Q(0)), w0)
        require(w0[0]**2+w0[1]**2 == 1, 'synthetic_boundary_zero_map')
        require(gd((2-w0[0], -w0[1]), one_plus) == rho, 'synthetic_boundary_zero_map')
        sprime = gd((Q(-3), Q(0)), gm(one_plus, one_plus))
        for multiplicity in [1, 2, 5]:
            res = gd((Q(3*multiplicity, 8), Q(0)), sprime)
            alternate = gm((Q(-multiplicity, 8), Q(0)), gm(one_plus, one_plus))
            require(res == alternate and res != (0, 0), 'synthetic_multiplicity_residue')

    for n in range(1, 25):
        # Independent rational bookkeeping, not actual prime values.
        prime, q, A = Q(n-3, n+1), Q(2, n+2), Q((-1)**n, 7*n)
        I = (-1)**n*3*2**(n-1)
        Qhigher = Q(2*(-1)**n, 3)+q
        d = A-Q(3, 8)*(-1)**n*(prime+Qhigher-I)
        Pcal = (-1)**n*prime-3*2**(n-1)+Q(2, 3)
        remainder = A-Q(3, 8)*(-1)**n*q
        require(d == -Q(3, 8)*Pcal+remainder, 'completed_prime_only_signs')

    bad_calls = [lambda: minus_one(-1), lambda: ordinary(True), lambda: ordinary(2.0),
                 lambda: laplace([Q(1)], Q(0)), lambda: gram(Q(1, 2), Q(2)),
                 lambda: step_norm([Q(2)], []), lambda: gd((Q(1), Q(0)), (Q(0), Q(0)))]
    for fn in bad_calls:
        try:
            fn()
        except ValueError:
            counts['malformed_input_refusal'] += 1
        else:
            raise ValueError('malformed input was accepted')

    sources = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
               for name in ['PROOF.md', 'SOURCE_LOCK.json', 'verify_exact.py']}
    return {'status': 'PASS_FINITE_HIGHER_POWER_ALGEBRA_ONLY',
            'scope': 'Exact finite algebra; analytic H2/PNT theorems and RH are not machine proved',
            'total_checks': sum(counts.values()), 'counts': dict(sorted(counts.items())),
            'square_continuous_controls_not_primes': model_norms,
            'rational_weight_gram_controls_not_prime_logs': kernel_receipts,
            'source_sha256': sources, 'RH': 'UNPROVED', 'prime_only_inequality': 'OPEN'}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', type=Path)
    mode.add_argument('--check', type=Path)
    args = parser.parse_args()
    answer = verify()
    text = canonical(answer)
    if args.write:
        args.write.write_text(text, encoding='utf-8')
    else:
        saved = json.loads(args.check.read_text(encoding='utf-8'))
        # Canonical serialized comparison deliberately distinguishes 1, 1.0, and True.
        if canonical(saved) != text:
            raise ValueError('saved result differs from independently recomputed content')
    print(text, end='')


if __name__ == '__main__':
    main()
