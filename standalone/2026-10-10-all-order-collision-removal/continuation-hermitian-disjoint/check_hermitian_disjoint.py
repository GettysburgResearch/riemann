#!/usr/bin/env python3
"""Exact mixed-colour kernel and finite Eisenstein tests; not a moment proof."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import prod
from pathlib import Path

COUNTS = Counter()
SOURCE_BLOB = '08ca528df9074ff8e418a29ba240b5cc1057b93d'


def require(ok, label):
    if not ok:
        raise ValueError(label)
    COUNTS[label.split(':', 1)[0]] += 1


def source_path():
    return Path(__file__).resolve().parent.parent / 'continuation-gaussian-conductor' / 'check_eisenstein_covariance.py'


def load_arithmetic():
    p = source_path()
    data = p.read_bytes()
    digest = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    require(digest == SOURCE_BLOB, 'source:exact_git_blob')
    spec = importlib.util.spec_from_file_location('_eisenstein_saved', p)
    if spec is None or spec.loader is None:
        raise RuntimeError('cannot load checked arithmetic source')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def coefficient(e):
    occupied = sum(x != 0 for x in e)
    return 1 - occupied if occupied else 1


def local_kernel_tests():
    coverage = []
    for m in (2, 4, 6, 8):
        count = 0
        for e in product(range(3), repeat=m):
            support = [i for i, x in enumerate(e) if x]
            answer = 0
            for bits in product((0, 1), repeat=len(support)):
                v = list(e)
                for i, bit in zip(support, bits):
                    v[i] -= bit
                answer += (-1) ** sum(bits) * coefficient(v)
            expected = 1 if sum(e) == 0 else (-1 if sum(e) == 1 else 0)
            require(answer == expected, 'kernel:full_local_convolution')
            count += 1
        coverage.append({'colours': m, 'valuation_vectors': count, 'maximum_each_valuation': 2})
    return coverage


def epow(E, z, n):
    answer = E.ONE
    for _ in range(n):
        answer = E.mul(answer, z)
    return answer


def disjoint_value(E, k, active):
    """active=(prime-support mask, signed character value); mask=0 is the unit."""
    state = {0: E.ONE}
    for i in range(2 * k):
        nxt = {}
        for occupied, value in state.items():
            for mask, z in active:
                if occupied & mask:
                    continue
                z = E.conj(z) if i >= k else z
                key = occupied | mask
                nxt[key] = E.add(nxt.get(key, E.ZERO), E.mul(value, z))
        state = nxt
    out = E.ZERO
    for z in state.values():
        out = E.add(out, z)
    return out


def scale_reconstruction(E):
    bank = tuple(p for p in E.make_prime_ideals(13)
                 if (p.q, p.w) in ((7, 2), (13, 3)))
    require(len(bank) == 2, 'fixture:two_declared_prime_ideals')
    norms = (1, 7, 13)
    vv = E.rows(19)
    cuts = sorted({F(1, 2), F(1), F(7, 2), F(13, 2), F(7), F(13)})
    panels = []
    for k in (1, 2, 3):
        m = 2 * k
        kernels = []
        for d in product(range(3), repeat=m):
            a = coefficient(tuple(int(x == 1) for x in d))
            b = coefficient(tuple(int(x == 2) for x in d))
            if a * b:
                kernels.append((d, a * b))
        for u in vv:
            chars = [E.ONE] + [E.root_value(p.char(u)) for p in bank]
            def avalue(X):
                z = E.ZERO
                for label, norm in enumerate(norms):
                    if X <= norm <= 2 * X:
                        z = E.add(z, E.scale(1 if label == 0 else -1, chars[label]))
                return z
            for x, y in zip(cuts, cuts[1:]):
                X = (x + y) / 2
                active = [(0 if j == 0 else 1 << (j - 1),
                           E.scale(1 if j == 0 else -1, chars[j]))
                          for j, norm in enumerate(norms) if X <= norm <= 2 * X]
                direct = disjoint_value(E, k, active)
                rhs = E.ZERO
                shifted = [avalue(X / norm) for norm in norms]
                for d, coeff in kernels:
                    term = (coeff, 0)
                    for i, label in enumerate(d):
                        z = chars[label]
                        term = E.mul(term, E.conj(z) if i >= k else z)
                        z = shifted[label]
                        term = E.mul(term, E.conj(z) if i >= k else z)
                    rhs = E.add(rhs, term)
                require(direct == rhs, 'reconstruction:mixed_scale_identity')
                require(direct[1] == 0, 'reconstruction:Hermitian_real')
        panels.append({'k': k, 'rows': len(vv), 'scale_intervals': len(cuts)-1,
                       'nonzero_kernel_tuples': len(kernels), 'finite_prime_norms': [7, 13]})
    return panels


def norm_panel(E, k, rational_primes, power):
    bank = tuple(p for p in E.make_prime_ideals(max(rational_primes)) if p.p in rational_primes)
    D = max(rational_primes)
    m = 2 * k
    sigma = F(power, m)
    require(min(p.q for p in bank) ** 2 > 2 * D, 'fixture:no_missing_composite_columns')
    vv = E.rows(19)
    qbound = F(1)
    t_bounds = []
    for p in bank:
        n = 1
        while (n + 1) ** sigma.denominator <= p.q ** sigma.numerator:
            n += 1
        require(n ** sigma.denominator <= p.q ** sigma.numerator,
                'norm:rigorous_rational_t_majorant')
        t = F(1, n)
        t_bounds.append(str(t))
        qbound *= 2 - (1 - m * t) / (1 - t) ** m
    qbound -= 1
    require(0 < qbound < 1, 'norm:finite_alphabet_mass_below_one')
    cuts = sorted({F(1, 2), F(1), F(D)} |
                  {F(p.q, d) for p in bank for d in (1, 2) if F(p.q, d) <= D})
    M = [F(0) for _ in vv]
    C = [F(0) for _ in vv]
    negative = None
    table = [[E.root_value(p.char(u)) for p in bank] for u in vv]
    for x, y in zip(cuts, cuts[1:]):
        X = (x + y) / 2
        mass = (x ** (-power) - y ** (-power)) / power
        for j, u in enumerate(vv):
            active = []
            if X <= 1 <= 2 * X:
                active.append((0, E.ONE))
            for i, p in enumerate(bank):
                if X <= p.q <= 2 * X:
                    active.append((1 << i, E.scale(-1, table[j][i])))
            a = E.ZERO
            for _, z in active:
                a = E.add(a, z)
            c = disjoint_value(E, k, active)
            require(c[1] == 0, 'norm:Hermitian_real')
            if c[0] < 0 and negative is None:
                negative = {'row': list(u), 'scale_midpoint': str(X),
                            'C_value': c[0], 'A_moment': E.norm(a) ** k}
            M[j] += mass * E.norm(a) ** k
            C[j] += mass * c[0]
    for a, b in zip(M, C):
        require(abs(b - a) <= qbound * a, 'norm:signed_relative_bound_each_row')
        require(b >= 0, 'norm:integrated_nonnegative_each_row')
    total_m, total_c = sum(M), sum(C)
    require(abs(total_c-total_m) <= qbound * total_m, 'norm:integrated_global_bound')
    require(negative is not None, 'norm:pointwise_positivity_counterexample')
    return {'k': k, 'sigma': str(sigma), 'D': D, 'row_norm_bound': 19,
            'rows': len(vv), 'finite_prime_ideal_norms': [p.q for p in bank],
            'scale_intervals': len(cuts)-1, 'q_upper_bound': str(qbound),
            'rational_t_majorants': t_bounds, 'moment_integral': str(total_m),
            'disjoint_integral': str(total_c), 'pointwise_negative_example': negative}


def exponent_tests():
    for k in range(1, 17):
        for delta in (F(1, 8), F(1, 12), F(1, 24)):
            for h in (F(1), F(21, 20), F(11, 10)):
                q = h/(1-delta)
                require((1-delta)*q == h, 'exponent:primitive_cutoff')
                require(F(1, 2)+delta+(5*h/6)/(2*k) == F(1, 2)+delta+5*h/(12*k),
                        'exponent:conditional_boundary')
            require(F(1,2)+delta+5*(2*k*(1-delta))/(12*k) == F(4,3)+delta/6,
                    'exponent:no_global_length_shortcut')
    for H in (F(1, 3), F(1), F(2), F(7), F(31)):
        for Q in (F(7), F(13), F(91)):
            # c_K^2 is represented by an arbitrary positive rational c2;
            # this tests bookkeeping, not the transcendental Poisson theorem.
            c2 = F(13)
            dual = Q/(c2*H)
            require(Q/(c2*dual) == H, 'dual:double_transform_restores_scale')
            require(c2*H*dual/Q == 1, 'dual:prefactor_product')


def replay():
    COUNTS.clear()
    E = load_arithmetic()
    local = local_kernel_tests()
    scales = scale_reconstruction(E)
    panels = [norm_panel(E, 2, (19,31,37), 3),
              norm_panel(E, 3, (61,67,73), 4),
              norm_panel(E, 4, (193,199,211,223), 5)]
    exponent_tests()
    return {'status':'PASS', 'scope':'exact finite identities and finite-prime-alphabet norms; no infinite moment theorem',
            'arithmetic_dependency_git_blob':SOURCE_BLOB, 'kernel_coverage':local,
            'scale_reconstructions':scales, 'norm_panels':panels,
            'predicate_counts':dict(sorted(COUNTS.items())), 'total_predicates':sum(COUNTS.values())}


def self_test():
    p = Path(__file__).resolve()
    source = p.read_text()
    mutations = [
        ('wrong_kernel', 'return 1 - occupied if occupied else 1', 'return 1', 'kernel:full_local_convolution'),
        ('missing_conjugate_dilation', 'term = E.mul(term, E.conj(z) if i >= k else z)',
         'term = E.mul(term, z)', 'reconstruction:mixed_scale_identity'),
    ]
    report = []
    # Place temporary copies in the same directory so the declared relative
    # source dependency is retained. They are removed before returning.
    for optimized in (False, True):
        cmd = [sys.executable, '-I', '-S', '-B'] + (['-O'] if optimized else [])
        for name, old, new, expected in mutations:
            require(source.count(old) >= 1, 'mutation:anchor_present')
            with tempfile.NamedTemporaryFile('w', suffix='.py', prefix='_negative_',
                    dir=p.parent, delete=False) as f:
                fp = Path(f.name)
                f.write(source.replace(old, new, 1))
            try:
                r = subprocess.run(cmd+[str(fp)], capture_output=True, text=True, timeout=45)
                require(r.returncode != 0 and ('ValueError: '+expected) in r.stderr,
                        'mutation:intended_arithmetic_refusal')
                report.append({'mode':'optimized' if optimized else 'normal', 'mutation':name,
                               'failure':expected})
            finally:
                fp.unlink(missing_ok=True)
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--write', type=Path)
    ap.add_argument('--check', type=Path)
    ap.add_argument('--negative-controls', action='store_true')
    ns = ap.parse_args()
    if ns.write and ns.check:
        ap.error('choose write or check')
    if ns.negative_controls:
        print(json.dumps({'status':'PASS', 'executed_refusals':self_test()}, indent=2, sort_keys=True))
        return
    data = json.loads(json.dumps(replay(), sort_keys=True))
    if ns.check and json.loads(ns.check.read_text()) != data:
        raise SystemExit('REJECT: saved result differs from exact reconstruction')
    text = json.dumps(data, indent=2, sort_keys=True)+'\n'
    if ns.write:
        ns.write.write_text(text)
    print(text, end='')


if __name__ == '__main__':
    main()
