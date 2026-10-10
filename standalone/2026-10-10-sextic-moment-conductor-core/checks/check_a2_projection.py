"""Exact controls for the A2 twisted gluing and signed projection.

The six-point local coefficient table is an INPUT to this checker. Its Gauss
normalization is proved in A2_COMPLETION.md. This script independently glues
that table with the primary source's unreduced twisted multiplicativity,
then checks the five-label formula and the signed inverse, retaining actual
sextic residue symbols, nonunit zeros, and overlapping auxiliary/exclusion
ideals. No analytic functional equation or infinite bound is tested here.
"""

import argparse
import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

from check_local_structure import ROOTS, ring_mul, root_mul, symbol


PRIMES = ((7, 7, 4), (13, 13, 9), (19, 19, 7))
GENERATORS = ((-2, -3), (1, -3), (-2, 3))
PATTERNS = ((0, 0), (1, 0), (0, 1), (1, 2), (2, 1), (2, 2))
COUNT = defaultdict(int)
PAIR = [[symbol(q, g) for q in PRIMES] for g in GENERATORS]


def require(ok, name):
    COUNT[name] += 1
    if not ok:
        raise RuntimeError("Failed exact predicate: " + name)


def subset(mask):
    return [i for i in range(3) if mask & (1 << i)]


def generator(mask):
    value = (1, 0)
    for i in subset(mask):
        value = ring_mul(value, GENERATORS[i])
    return value


def norm_of(mask):
    return math.prod(PRIMES[i][0] for i in subset(mask))


def monomial(labels):
    # Independent formal parameters A_p and B_p from the local table.
    return (tuple(int(t in (1, 2, 5)) for t in labels),
            tuple(int(t in (3, 4, 5)) for t in labels))


def source_phase(labels):
    """Literal four-factor twist in source equation (20), before reduction."""
    phase = 0
    for i in range(3):
        x1, x2 = PATTERNS[labels[i]]
        for j in range(i + 1, 3):
            y1, y2 = PATTERNS[labels[j]]
            phase += 2 * (PAIR[i][j] * x1 * y1 + PAIR[j][i] * y1 * x1
                          + PAIR[i][j] * x2 * y2 + PAIR[j][i] * y2 * x2
                          - PAIR[i][j] * x1 * y2 - PAIR[j][i] * y1 * x2)
    return phase % 6


def gauss_phase(active):
    # Recombine squarefree Gauss factors by the repository's CRT formula.
    return sum(4 * PAIR[i][j] for i in active for j in active if i < j) % 6


def full_coefficient(labels, row, auxiliary, excluded):
    active = [i for i, t in enumerate(labels) if t]
    if any(excluded & (1 << i) for i in active):
        return None
    row_symbols = [symbol(PRIMES[i], row) for i in active]
    aux_symbols = [symbol(PRIMES[i], auxiliary) for i in active]
    if -1 in row_symbols or -1 in aux_symbols:
        return None
    phase = source_phase(labels)
    for i, sr, sf in zip(active, row_symbols, aux_symbols):
        exponent = sum(PATTERNS[labels[i]])
        phase += exponent * sr + 4 * exponent * sf
    return monomial(labels), ROOTS[phase % 6]


def exterior_coefficient(labels, outer, row, auxiliary, excluded):
    active = subset(outer)
    if any(excluded & (1 << i) for i in active):
        return None
    sr = {i: symbol(PRIMES[i], row) for i in active}
    sf = {i: symbol(PRIMES[i], auxiliary) for i in active}
    if any(sr[i] < 0 or sf[i] < 0 for i in active):
        return None
    e_primes = [i for i in active if labels[i] == 5]
    a = tuple(int(i in e_primes) for i in range(3))
    b = tuple(int(i in active) for i in range(3))
    phase = gauss_phase(e_primes)
    phase += sum((4 if labels[i] == 5 else 3) * sr[i] for i in active)
    phase += sum(4 * sf[i] for i in e_primes)
    return (a, b), ROOTS[phase % 6]


def multiply(x, y):
    if x is None or y is None:
        return None
    (xa, xb), xv = x
    (ya, yb), yv = y
    key = (tuple(a + b for a, b in zip(xa, ya)),
           tuple(a + b for a, b in zip(xb, yb)))
    return key, root_mul(xv, yv)


def term_for_subset(labels, outer, row, auxiliary, excluded):
    ext = exterior_coefficient(labels, outer, row, auxiliary, excluded)
    inner = tuple(0 if outer & (1 << i) else t for i, t in enumerate(labels))
    e_mask = sum(1 << i for i in subset(outer) if labels[i] == 5)
    aux_child = ring_mul(auxiliary, generator(e_mask))
    child = full_coefficient(inner, row, aux_child, excluded | outer)
    return multiply(ext, child)


def as_polynomial(term):
    return {} if term is None else {term[0]: term[1]}


def check_patterns():
    rows = [(1, 0), (0, 1), (-1, 0), (2, 1), (-1, 2)]
    rows += [generator(mask) for mask in range(1, 8)]
    configurations = 0
    for labels in itertools.product(range(6), repeat=3):
        a_primes = [i for i, t in enumerate(labels) if t in (1, 2, 5)]
        require(source_phase(labels) == gauss_phase(a_primes),
                "unreduced_twist_equals_five_label_formula")
        correction = sum(1 << i for i, t in enumerate(labels) if t in (3, 4, 5))
        for f_mask in range(8):
            auxiliary = generator(f_mask)
            for excluded in (0, 1, 3, 7):
                for row in rows:
                    direct = full_coefficient(labels, row, auxiliary, excluded)
                    forward = term_for_subset(labels, correction, row, auxiliary, excluded)
                    require(forward == direct, "exact_forward_completion_with_masks")
                    inverse = defaultdict(lambda: [0, 0])
                    for outer in range(8):
                        if outer & ~correction:
                            continue
                        term = term_for_subset(labels, outer, row, auxiliary, excluded)
                        if term is None:
                            continue
                        key, value = term
                        sign = (-1) ** outer.bit_count()
                        for j in (0, 1):
                            inverse[key][j] += sign * value[j]
                    inverse = {key: tuple(value) for key, value in inverse.items()
                               if value != [0, 0]}
                    expected = as_polynomial(direct) if not correction else {}
                    require(inverse == expected, "exact_signed_projection_with_masks")
                    configurations += 1
        # Normalizers use arbitrary positive rational input scales. The
        # exponents are obtained from the actual local support coordinates.
        c = sum(1 << i for i, t in enumerate(labels) if t == 3)
        d = sum(1 << i for i, t in enumerate(labels) if t == 4)
        e = sum(1 << i for i, t in enumerate(labels) if t == 5)
        nc, nd, ne, ncor = norm_of(c), norm_of(d), norm_of(e), norm_of(correction)
        x1 = math.prod(PRIMES[i][0] ** PATTERNS[labels[i]][0]
                       for i in subset(correction))
        x2 = math.prod(PRIMES[i][0] ** PATTERNS[labels[i]][1]
                       for i in subset(correction))
        require(x1 == nc * nd ** 2 * ne ** 2 and x2 == nc ** 2 * nd * ne ** 2,
                "actual_support_scale_map")
        require(Fraction(ne, x1 * x2) == Fraction(1, ncor ** 3),
                "auxiliary_normalizer_scale")
        require(Fraction(ncor * ne, x1 * x2) == Fraction(1, ncor ** 2),
                "squared_averaged_norm_cost")
        require(Fraction(ncor, x1 * x2) == Fraction(1, nc ** 2 * nd ** 2 * ne ** 3),
                "squared_fixed_auxiliary_norm_cost")
    return configurations


def check_signed_diagonal():
    # Continuum cancellation is only a finite coefficient identity here.
    for n_mask in range(8):
        active = subset(n_mask)
        total = 0
        for allocation in itertools.product(range(3), repeat=len(active)):
            value = 1
            for i, label in zip(active, allocation):
                q = PRIMES[i][0]
                value *= (1, -q, q - 1)[label]
            total += value
        require(total == int(n_mask == 0), "diagonal_continuum_mobius_cancellation")
        # For fixed z and h, the exact v-removal mask combines to (z,h)=1.
        for h_mask in range(8):
            h = generator(h_mask)
            total = 0
            for v_mask in range(8):
                if v_mask & ~n_mask:
                    continue
                m_mask = n_mask ^ v_mask
                if any(symbol(PRIMES[i], h) < 0 for i in subset(v_mask)):
                    continue
                hv4 = h
                for _ in range(4):
                    hv4 = ring_mul(hv4, generator(v_mask))
                squared_symbol = int(all(symbol(PRIMES[i], hv4) >= 0
                                         for i in subset(m_mask)))
                total += (-1) ** v_mask.bit_count() * squared_symbol
            require(total == int(n_mask == 0), "exact_diagonal_mask_recombination")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    for i, g in enumerate(GENERATORS):
        require(g[0] ** 2 - g[0] * g[1] + g[1] ** 2 == PRIMES[i][0],
                "actual_primary_prime_norm")
        require((g[0] - 1) % 3 == g[1] % 3 == 0, "actual_primary_generator")
        require(symbol(PRIMES[i], g) == -1, "actual_prime_ideal_generator")
        for j in range(i + 1, 3):
            require((2 * PAIR[i][j]) % 6 == (2 * PAIR[j][i]) % 6,
                    "actual_cubic_reciprocity")
    configurations = check_patterns()
    check_signed_diagonal()
    result = {"status": "PASS", "arithmetic": "EXACT_INTEGER_AND_SIXTH_ROOT_ALGEBRA",
              "local_table_is_assumed_input": True,
              "analytic_functional_equation_tested": False,
              "infinite_moment_proved_by_computation": False,
              "global_local_patterns": 6 ** 3,
              "row_auxiliary_mask_configurations": configurations,
              "prime_norms": [q[0] for q in PRIMES],
              "sextic_pair_exponents": PAIR,
              "checks": dict(sorted(COUNT.items())),
              "total_predicates": sum(COUNT.values())}
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
