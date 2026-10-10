#!/usr/bin/env python3
"""Exact scalar replica pricing; the source moment remains unproved."""
from fractions import Fraction as Q
import hashlib
import itertools
import json
from pathlib import Path


def need(condition, message):
    if not condition:
        raise ArithmeticError(message)


def theta(kappa, h):
    need(0 <= kappa <= Q(1, 2) and 0 < h < 1, 'stated pricing domain')
    return max((1+kappa+h*(Q(5, 6)-kappa))/2, 1-h/6)


def run():
    records = []
    for kappa in [Q(j, 200) for j in range(101)]:
        denominator = 7-6*kappa
        need(denominator > 0, 'positive optimization denominator')
        h = 6*(1-kappa)/denominator
        bound = (6-5*kappa)/denominator
        need(0 < h < 1 and theta(kappa, h) == bound, 'balanced costs')
        need((Q(5, 6)-kappa)/2 > 0, 'increasing first cost')
        for test_h in [Q(j, 100) for j in range(1, 100)]:
            need(theta(kappa, test_h) >= bound, 'finite minimizer controls')
        need(bound >= Q(6, 7), 'prime-sixth architecture floor')
        need((bound < Q(7, 8)) == (kappa < Q(1, 2)), 'exact 7/8 threshold')
        records.append({'kappa': str(kappa), 'optimal_h': str(h), 'theta': str(bound)})
    kappa = Q(2, 5)
    need(6*(1-kappa)/(7-6*kappa) == Q(18, 23), 'target row height')
    need(theta(kappa, Q(18, 23)) == Q(20, 23), 'target half-plane')
    primes = [2, 3, 5, 7, 11]
    for size in range(6):
        for selected in itertools.combinations(primes, size):
            c = 1
            for p in selected:
                c *= p
            for k in range(1, 100):
                value = 0
                for mask in range(1 << size):
                    complement_coprime = all(k % p != 0 for j, p in enumerate(selected)
                                               if not mask & (1 << j))
                    if complement_coprime:
                        value += (-1)**mask.bit_count()
                need(value == ((-1)**size if k % c == 0 else 0), 'signed divisor collapse')
    return {'status': 'PASS_EXACT_CONDITIONAL_REPLICA_PRICING',
            'arithmetic': 'exact rational scalar controls and exact integer divisor controls',
            'target_kappa': '2/5', 'target_h': '18/23', 'conditional_half_plane': '20/23',
            'open_source_moment_proved': False, 'rh_proved': False,
            'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'pricing_controls': records}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2)+'\n', end='')
