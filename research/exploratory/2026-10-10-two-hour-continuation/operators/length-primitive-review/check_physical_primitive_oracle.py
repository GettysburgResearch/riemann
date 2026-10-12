#!/usr/bin/env python3
"""Independent exponential Volterra expansion; no R integration or form sign."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from flint import acb, arb, ctx

HERE = Path(__file__).resolve().parent
OPS = HERE.parent
sys.path.insert(0, str(OPS))
import physical_length_source as native
import enclose_length_primitive as owner
from enclose_analytic_upper import basis

FROZEN = {
    'physical_length_source.py': 'b15da7904f2bdf4f4bc7e68b8dfe2f1de808bb0bac47a905d684c513dba24f1e',
    'enclose_length_primitive.py': '2fc80bfd130ea59bb413209cd8dd092a71e4de80cc7f387c14778626cc1e560a',
    'PHYSICAL_LENGTH_PRIMITIVE_COMPLETION.md': 'cdceae6052114119e13c5d9d6919847f339603a0109b279bb85a26bd989e7a7d',
    'enclose_length_weighted.py': 'aed3e21e0784f387fb371b871389514c60671bd4f29449b07791d97ab9b77b16',
}


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run():
    for name, digest in FROZEN.items():
        require(sha(OPS / name) == digest, ('frozen input', name))
    require(sha(native.OLD / 'enclose_analytic_upper.py') ==
            'b3832a0cddc8bc1e2603c40240b608d1f06a868bda9436d8e88a146393fe007b',
            'immutable native analytical helper')
    ctx.prec = 256
    length = arb(21) / 20
    source, upper, coefficients, _ = native.build_length(length, 7, 100)
    raw = basis(100, 7)
    require(len(raw) == coefficients.nrows() == 110, 'all raw rows')
    require(coefficients.ncols() == 10, 'all ten exact columns')
    require(raw[:7] == basis(0, 7)[:7], 'low sine inventory')
    require([r[0][0][1] for r in raw[10:]] == list(range(8, 108)), 'high sine inventory')

    # Keys are (twice real rate, integer physical frequency, t power).
    # Work directly with the two complex exponentials in the native basis,
    # rather than the owner's six-soft/cosine coefficient transformation.
    keys = [(1, 0, 0), (-1, 0, 0), (1, 0, 1), (-1, 0, 1),
            (3, 0, 0), (-3, 0, 0)]
    keys += [(0, n, 0) for n in range(-107, 108) if n]
    index = {key: i for i, key in enumerate(keys)}
    require(len(index) == 220, 'complete exponential primitive inventory')

    def rate(key):
        return acb(arb(key[0]) / 2, arb.pi() * key[1] / length)

    def primitive(alpha):
        key = (alpha[1], 0, 0) if alpha[0] == 'r' else (0, alpha[1], 0)
        if key == (1, 0, 0) or key == (-1, 0, 0):
            return {(key[0], 0, 1): acb(arb(1) / 2),
                    (1, 0, 0): acb(arb(1) / 2),
                    (-1, 0, 0): acb(-arb(1) / 2)}
        a = rate(key)
        c = arb(1) / 2
        return {key: a / (a * a - c * c),
                (1, 0, 0): -1 / (2 * (a - c)),
                (-1, 0, 0): -1 / (2 * (a + c))}

    expanded = [[acb(0) for _ in keys] for _ in range(10)]
    for row, terms in enumerate(raw):
        for alpha, multiplier in terms:
            for key, primitive_coefficient in primitive(alpha).items():
                for column in range(10):
                    expanded[column][index[key]] += coefficients[row, column] * multiplier * primitive_coefficient

    cache = {}

    def integral(real2, frequency, power):
        key = (real2, frequency, power)
        if key in cache:
            return cache[key]
        if not real2 and not frequency:
            answer = acb(length ** (power + 1) / (power + 1))
        else:
            a = rate(key)
            endpoint = (a * length).exp()
            answer = (endpoint - 1) / a
            # Physical integration by parts: J_p=(L^p exp(aL)-p J_(p-1))/a.
            for p in range(1, power + 1):
                answer = (length ** p * endpoint - p * answer) / a
        require(answer.is_finite(), ('whole physical moment', key))
        cache[key] = answer
        return answer

    norms = [acb(0) for _ in range(10)]
    # Each primitive is real, so its square, not an approximation to an
    # absolute square, is integrated. Conjugate native exponential pairs
    # guarantee the resulting imaginary intervals contain zero.
    for i, ki in enumerate(keys):
        for j in range(i, len(keys)):
            kj = keys[j]
            gram = integral(ki[0] + kj[0], ki[1] + kj[1], ki[2] + kj[2])
            for column in range(10):
                term = expanded[column][i] * expanded[column][j] * gram
                norms[column] += term if i == j else 2 * term
    require(all(x.imag.contains(0) and x.real > 0 for x in norms), 'all real positive squared norms')
    real_norms = [x.real for x in norms]
    data = {'exact_trial_z_coefficients_balls': [
        [coefficients[i, j].str(65, more=True) for j in range(10)] for i in range(110)
    ]}
    owner_norms, owner_trace = owner.synthesis(data)
    require(all(x.overlaps(y) for x, y in zip(real_norms, owner_norms)), 'every norm overlaps independent exponential integration')
    trace = sum(real_norms, arb(0))
    require(trace < 1 and trace.overlaps(owner_trace), 'strict K1 and total overlap')
    prototype = json.loads((OPS / 'physical_length_synthesis_trace_only.json').read_text())
    require(trace.overlaps(arb(prototype['synthesis_trace_ball'])), 'frozen trace-only artifact overlap')
    return {
        'status': 'DIRECTED_PHYSICAL_PRIMITIVE_ORACLE_ACCEPT_NO_FORM_SIGN',
        'arithmetic': 'python-flint directed Arb/Acb at256bits',
        'exact_length': '21/20',
        'fresh_native_coefficient_rebuild': True,
        'raw_rows': 110, 'native_columns': 10, 'complex_exponential_terms': 220,
        'whole_product_moment_keys': len(cache),
        'norm_balls': [x.str(65, more=True) for x in real_norms],
        'synthesis_trace_ball': trace.str(65, more=True),
        'K_exact': '1',
        'every_owner_norm_overlaps': True,
        'producer_sha256': sha(Path(__file__)),
        'frozen_sources': FROZEN,
        'old_analytic_helper_sha256': sha(native.OLD / 'enclose_analytic_upper.py'),
        'trace_only_owner_artifact_sha256': sha(OPS / 'physical_length_synthesis_trace_only.json'),
        'full_R_integration_performed': False,
        'weighted_gate_performed': False,
        'native_form_sign_claimed': False,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run()
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(result['status'])
