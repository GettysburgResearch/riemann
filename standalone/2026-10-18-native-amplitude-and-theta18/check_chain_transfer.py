#!/usr/bin/env python3
"""Independent rational probability/transfer check of the complete T18C tree.

The generating-function construction uses conditional spin probabilities and
polynomial multiplication. It does not call the author's cumulant construction
until the final comparison. A separate 128-configuration graph is enumerated.
This checks graph encoding; it does not certify the nearby moment root.
"""
import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def mul(a, b, degree):
    out = [F(0) for _ in range(degree + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b[:degree + 1 - i]):
            out[i + j] += x * y
    return out


def power(a, n, degree):
    out = [F(1)] + [F(0)] * degree
    while n:
        if n & 1:
            out = mul(out, a, degree)
        n //= 2
        if n:
            a = mul(a, a, degree)
    return out


def exponential(weight, degree):
    out = [F(1)]
    for k in range(1, degree + 1):
        out.append(out[-1] * weight / k)
    return out


def child_mixture(plus, correlation):
    # Conditional child spin is +1 with probability (1+q)/2.
    return [((1 + correlation) * x + (1 - correlation) * (-1)**k * x) / 2
            for k, x in enumerate(plus)]


def transfer(leaf_weights, counts, weights, edges, eta, degree):
    require(len(edges) + 1 == len(weights), 'chain length mismatch')
    plus = exponential(weights[-1], degree)
    for i in range(len(weights) - 2, -1, -1):
        plus = mul(exponential(weights[i], degree),
                   child_mixture(plus, edges[i]), degree)
    hub_plus = child_mixture(plus, eta)
    for weight, count in zip(leaf_weights, counts):
        branch = child_mixture(exponential(weight, degree), eta * weight)
        hub_plus = mul(hub_plus, power(branch, count, degree), degree)
    return [math.factorial(k) * (x if k % 2 == 0 else F(0))
            for k, x in enumerate(hub_plus)]


def enumerate_small(leaf_weights, weights, edges, eta, degree):
    # Hub + two leaves of type0 + one leaf of type1 + three chain spins.
    vertex_weights = [F(0), leaf_weights[0], leaf_weights[0],
                      leaf_weights[1], *weights[:3]]
    links = [(0, 1, eta * leaf_weights[0]),
             (0, 2, eta * leaf_weights[0]),
             (0, 3, eta * leaf_weights[1]),
             (0, 4, eta), (4, 5, edges[0]), (5, 6, edges[1])]
    out = [F(0)] * (degree + 1)
    for spins in itertools.product((-1, 1), repeat=7):
        probability = F(1, 2**7)
        for i, j, q in links:
            probability *= 1 + q * spins[i] * spins[j]
        value = sum(w * s for w, s in zip(vertex_weights, spins))
        term = probability
        for k in range(degree + 1):
            out[k] += term
            term *= value
    return out


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', type=Path, required=True)
    ap.add_argument('--output', type=Path)
    args = ap.parse_args()
    base = args.data.resolve()
    parameters = json.loads((base / 'chain_parameters.json').read_text())
    z = list(map(F, parameters['centers']))
    require(len(z) == 29, 'parameter count')
    require(parameters['counts'] == [256, 10], 'leaf multiplicities')
    require(all(x > 0 for x in z), 'positive weights and correlations')
    require(all(x < 1 for x in z[16:]), 'finite ferromagnetic couplings')
    eta = F(parameters['hub_core_correlation'])
    require(eta == F(1, 1000), 'hub correlation')
    require(all(eta * x < 1 for x in z[:2]), 'leaf couplings')
    degree = 20
    full = transfer(z[:2], (256, 10), z[2:16], z[16:], eta, degree)
    sys.path.insert(0, str(base))
    from chain_exact import evaluate
    _, authored = evaluate(z, degree=degree)
    require(full == authored, 'complete281-spin moment maps disagree')
    small = transfer(z[:2], (2, 1), z[2:5], z[16:18], eta, degree)
    enumerated = enumerate_small(z[:2], z[2:5], z[16:18], eta, degree)
    require(small == enumerated, 'small graph enumeration disagrees')
    require(full[0] == 1 and small[0] == 1, 'normalization')
    require(all(full[k] == 0 for k in range(1, degree + 1, 2)), 'spin-flip symmetry')
    q_removed = list(z[16:])
    q_removed[0] = F(0)
    no_strong = transfer(z[:2], (256, 10), z[2:16], q_removed, eta, 2)
    require(no_strong[2] != full[2], 'strong edge deletion must change the model')
    q_removed = [z[16]] + [F(0)] * 12
    no_weak = transfer(z[:2], (256, 10), z[2:16], q_removed, eta, 2)
    require(no_weak[2] != full[2], 'weak edge deletion must change the model')
    source = json.loads((base / 'theta_tight.json').read_text())
    scale = 1 << source['bits']
    source_overlap = []
    for k in range(0, 19, 2):
        lo, hi = source['standardized_moments'][k]
        source_overlap.append(F(lo, scale) <= full[k] <= F(hi, scale))
    report = {
        'status': 'PASS',
        'role': 'Independent exact graph-encoding check, not a contraction certificate',
        'vertices': 281, 'edges': 280,
        'complete_raw_moments_checked': list(range(21)),
        'enumerated_small_graph_configurations': 128,
        'small_graph_raw_moments_checked': list(range(21)),
        'negative_controls': ['deleting the strong edge changes variance',
                              'deleting the twelve weak edges changes variance'],
        'center_moments_inside_source_intervals': source_overlap,
        'normalization_and_symmetry': 'PASS',
        'input_sha256': {name: digest(base / name) for name in
                         ['chain_parameters.json', 'chain_exact.py', 'theta_tight.json']},
        'checker_sha256': digest(Path(__file__)),
        'not_proved': ['existence of the nearby exact root',
                       'independent transcendental source bounds',
                       'an all-order approximation or RH'],
    }
    payload = json.dumps(report, indent=2, sort_keys=True) + '\n'
    if args.output:
        args.output.write_text(payload)
    print(payload, end='')


if __name__ == '__main__':
    main()
