"""Exact local constant-term densities, not an analytic remainder test."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


def req(v, message):
    if not v:
        raise ArithmeticError(message)


def delta(q, e):
    return F(1, q ** e) * sum((F(1) if j == 0 else
                              F(q ** (6 * j) - q ** (6 * j - 1), q ** (5 * j))
                              for j in range(e // 6 + 1)), F(0))


def main():
    density_gates = periodicity_gates = boolean_gates = 0
    rows = []
    for q in [7, 13, 19, 25, 31, 37, 43, 49]:
        for e in range(19):
            value = delta(q, e)
            req(value == F(q ** (e // 6), q ** e), 'constant density formula')
            density_gates += 1
            req(delta(q, e + 6) == value / q ** 5, 'sixth-power density periodicity')
            periodicity_gates += 1
            rows.append([q, e, str(value)])
        req(delta(q, 6) != F(1 + q ** 6 - q ** 5, q ** 6), 'omitted cusp-height mutation')
    primes = [7, 13, 19]
    for js in product(range(6), repeat=3):
        for aa in product([0, 1], repeat=3):
            left = right = F(1)
            locals_L = []
            for q, j, a in zip(primes, js, aa):
                vp = F(q * q, q * q + q - 1)
                h = -F(1, q + 1)
                z = 1 + h / q
                primitive = z if j + a == 0 else (1 + h) * delta(q, j + a)
                base_R = z if j == 0 else (1 + h) * delta(q, j)
                L = F(1) if j == 0 else (F(q, 1) / vp if j == 5 else 1 / vp)
                left *= primitive / base_R
                right *= (vp / q if a else 1) * (L if a else 1)
                locals_L.append(L)
            req(left == right, 'shared-prime primitive label factor')
            expansion = F(0)
            for gg in product([0, 1], repeat=3):
                if any(g and (not a or not j) for g, a, j in zip(gg, aa, js)):
                    continue
                term = F(1)
                for L, g in zip(locals_L, gg):
                    if g:
                        term *= L - 1
                expansion += term
            local_product = F(1)
            for L, a in zip(locals_L, aa):
                if a:
                    local_product *= L
            req(expansion == local_product, 'complete Boolean expansion')
            boolean_gates += 1
    out = {'status': 'PASS', 'scope': 'Exact local cusp-height, all-valuation primitive-density and Boolean identities only.',
           'constant_density_gates': density_gates, 'sixth_power_periodicity_gates': periodicity_gates,
           'three_prime_full_boolean_gates': boolean_gates, 'height_mutations_rejected': 8,
           'density_records_sha256': hashlib.sha256(json.dumps(rows, separators=(',', ':')).encode()).hexdigest()}
    Path(__file__).with_name('RESIDUE_VALUATION_CHECKS.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
