#!/usr/bin/env python3
"""Bounded exact guards for the new Mobius overlap and cubic-group proofs.

Authenticates local residue symbols over two actual split Eisenstein primes,
formal forward-correction coefficients, retained nonunit zeros, and rational
exponent certificates. It does not test a moment estimate, PW_b, an infinite
Euler product, or an imported character sieve. All checks remain active in -O.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


EXPECTED_NOTE_SHA256 = "980c0e5d4e82e4c6105a21db37aeeb84ff19da9c985be571002fe4f3e9bfba04"
COUNTS = {}


def require(predicate, category, witness):
    COUNTS[category] = COUNTS.get(category, 0) + 1
    if not predicate:
        raise ArithmeticError((category, witness))


@dataclass(frozen=True)
class C6:
    """Z[zeta_6], with zeta_6^2 = zeta_6 - 1."""

    a: int = 0
    b: int = 0

    @staticmethod
    def lift(value):
        return value if isinstance(value, C6) else C6(value, 0)

    def __add__(self, other):
        other = self.lift(other)
        return C6(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __mul__(self, other):
        other = self.lift(other)
        return C6(self.a * other.a - self.b * other.b,
                  self.a * other.b + self.b * other.a + self.b * other.b)

    __rmul__ = __mul__

    def conjugate(self):
        return C6(self.a + self.b, -self.b)

    def __pow__(self, exponent):
        if exponent < 0:
            raise ArithmeticError("use literal_power for a negative exponent")
        result, base = ONE, self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result


ZERO, ONE, ZETA = C6(), C6(1), C6(0, 1)


def literal_power(value, exponent):
    """An incidence has positive multiplicity even when its net power is 0."""
    if value == ZERO:
        return ZERO
    if exponent < 0:
        return value.conjugate() ** (-exponent)
    return value ** exponent


def cproduct(values):
    result = ONE
    for value in values:
        result = result * value
    return result


def primitive_tables():
    tables = {}
    records = []
    for prime, omega in ((7, 2), (13, 3)):
        require((omega * omega + omega + 1) % prime == 0,
                "prime_ideal_embedding", (prime, omega))
        zeta_image = (1 + omega) % prime
        residues = [pow(zeta_image, j, prime) for j in range(6)]
        require(len(set(residues)) == 6 and pow(zeta_image, 6, prime) == 1,
                "primitive_sixth_root", (prime, residues))
        table = []
        for x in range(prime):
            target = pow(x, (prime - 1) // 6, prime)
            value = ZERO if x == 0 else ZETA ** residues.index(target)
            require((value.a + value.b * zeta_image) % prime == target,
                    "primitive_symbol_lift", (prime, x, target, value))
            table.append(value)
        for x, y in itertools.product(range(prime), repeat=2):
            require(table[x * y % prime] == table[x] * table[y],
                    "primitive_symbol_multiplicativity", (prime, x, y))
        for x in range(prime):
            for e in range(-6, 7):
                value = literal_power(table[x], e)
                if x == 0:
                    require(value == ZERO, "literal_nonunit_powers", (prime, e))
                else:
                    require(value * value.conjugate() == ONE,
                            "unit_character_powers", (prime, x, e))
        require(literal_power(table[0], 0) != table[0] ** 0,
                "principal_zero_guard", prime)
        tables[prime] = table
        records.append({
            "prime_ideal": [prime, omega],
            "description": "ideal (p, omega - omega_residue), Np=p",
            "zeta6_image": zeta_image,
            "complete_residue_count": prime,
        })
    return tables, records


def binary_terms(signs):
    result = []
    for beta in itertools.product((0, 1), repeat=len(signs)):
        coefficient = 1
        for sign, bit in zip(signs, beta):
            if bit:
                coefficient *= sign
        result.append((beta, coefficient))
    return result


def below(beta, alpha):
    return all(x <= y for x, y in zip(beta, alpha))


def subtract(alpha, beta):
    return tuple(x - y for x, y in zip(alpha, beta))


def phase_monomial(etas, alpha):
    return cproduct(eta ** exponent for eta, exponent in zip(etas, alpha))


def designated_coefficient(alpha, inside):
    """Independent closed expansion of (3.3), not recursive polynomial division."""
    epsilon = (-1) ** len(inside)
    support = {i for i in range(1, len(alpha)) if alpha[i]}
    value = int(not any(alpha))
    if alpha[0] and support:
        value += epsilon * (-epsilon) ** (alpha[0] - 1)
    if all(i + 1 in support for i in inside):
        value -= epsilon * (-epsilon) ** alpha[0]
    return value


def designated_local_checks(tables):
    records = []
    cases = [(2, (0, 1)), (3, (0, 1)), (3, (0, 1, 2)),
             (4, (0, 1, 2, 3)), (6, tuple(range(6)))]
    for k, inside in cases:
        m, index_mask = len(inside), sum(1 << i for i in inside)
        target = {}
        for original in range(1 << k):
            bits = tuple((original >> i) & 1 for i in range(k))
            alpha = (1,) + (0,) * k if original == index_mask else (0,) + bits
            target[alpha] = (-1) ** original.bit_count()
        signs = ((-1) ** m,) + (-1,) * k
        denominator = binary_terms(signs)
        cap = 2
        checked = 0
        for alpha in itertools.product(range(cap + 1), repeat=k + 1):
            convolution = sum(
                coefficient * designated_coefficient(subtract(alpha, beta), inside)
                for beta, coefficient in denominator if below(beta, alpha)
            )
            require(convolution == target.get(alpha, 0),
                    "designated_forward_local_coefficients", (k, inside, alpha))
            checked += 1
            if sum(x > 0 for x in alpha) == 1:
                require(designated_coefficient(alpha, inside) == 0,
                        "designated_unmasked_one_axis_zero", (k, inside, alpha))
        for prime, table in tables.items():
            for x, chi in enumerate(table):
                for original in range(1 << k):
                    bits = [(original >> i) & 1 for i in range(k)]
                    lhs = ((-1) ** sum(bits)) * (chi ** sum(bits))
                    for ordinary in (False, True):
                        is_common = (original & index_mask) == index_mask
                        c = int(is_common if ordinary else original == index_mask)
                        residual = [bit - c if i in inside else bit
                                    for i, bit in enumerate(bits)]
                        rhs = ((-1) ** (m * c + sum(residual))) * cproduct(
                            [literal_power(chi, m) ** c]
                            + [chi ** bit for bit in residual])
                        require(lhs == rhs, "designated_primitive_phase_identity",
                                (prime, x, k, inside, original, ordinary))
                        if m == 6 and c and x == 0:
                            require(rhs == ZERO, "designated_principal_nonunit_mask",
                                    (prime, original, ordinary))
        records.append({"degree": k, "inside": list(inside),
                        "max_local_exponent": cap,
                        "formal_coefficients_checked": checked})
    return records


def mixed_coefficient(alpha, signs, masked):
    value = 1
    for exponent, sign in zip(alpha, signs):
        value *= (-sign) ** exponent
    if not masked:
        value *= 1 - sum(x > 0 for x in alpha)
    return value


def mixed_local_checks(tables):
    cases = [
        ((1, 1, 2), (1, -1, 2)),
        ((2, 2, 1, 1), (2, -2, 1, -1)),
        ((2, 2, 1, 3), (0, 2, 1, 3)),
        ((6, 2, 1), (0, -2, -1)),
    ]
    records = []
    for multiplicities, powers in cases:
        signs = tuple((-1) ** m for m in multiplicities)
        dimension = len(signs)
        alphas = list(itertools.product(range(3), repeat=dimension))
        denominator = binary_terms(signs)
        for masked in (False, True):
            for alpha in alphas:
                support = [i for i, e in enumerate(alpha) if e]
                target = int(not any(alpha))
                if not masked and sum(alpha) == 1:
                    target = signs[support[0]]
                convolution = sum(
                    coefficient * mixed_coefficient(subtract(alpha, beta), signs, masked)
                    for beta, coefficient in denominator if below(beta, alpha)
                )
                require(convolution == target, "mixed_forward_local_coefficients",
                        (multiplicities, powers, masked, alpha))
                if len(support) == 1:
                    value = mixed_coefficient(alpha, signs, masked)
                    require((value != 0) if masked else (value == 0),
                            "mixed_one_axis_mask_adapter", (masked, alpha, signs))
            for prime, table in tables.items():
                for x, chi in enumerate(table):
                    etas = tuple(literal_power(chi, e) for e in powers)
                    weighted_e = {
                        alpha: mixed_coefficient(alpha, signs, masked)
                        * phase_monomial(etas, alpha) for alpha in alphas
                    }
                    weighted_b = [
                        (beta, coefficient * phase_monomial(etas, beta))
                        for beta, coefficient in denominator
                    ]
                    for alpha in alphas:
                        actual = sum((
                            weighted_e[subtract(alpha, beta)] * coefficient
                            for beta, coefficient in weighted_b if below(beta, alpha)
                        ), ZERO)
                        expected = ONE if not any(alpha) else ZERO
                        if not masked and sum(alpha) == 1:
                            i = next(i for i, e in enumerate(alpha) if e)
                            expected = signs[i] * etas[i]
                        require(actual == expected, "mixed_primitive_symbol_convolution",
                                (prime, x, multiplicities, powers, masked, alpha))
        records.append({"multiplicities": list(multiplicities),
                        "net_powers": list(powers), "max_local_exponent": 2})
    return records


def crt_tuple_checks(tables):
    def char(mask, u):
        return cproduct(tables[p][u % p] for i, p in enumerate((7, 13))
                        if mask & (1 << i))

    cases = [(2, (0, 1)), (3, (0, 1)), (3, (0, 1, 2))]
    total_tuples = 0
    for k, inside in cases:
        for ns in itertools.product(range(4), repeat=k):
            common, outside_union = 3, 0
            for i, n in enumerate(ns):
                if i in inside:
                    common &= n
                else:
                    outside_union |= n
            c = common & (3 ^ outside_union)
            residuals = tuple(n ^ c if i in inside else n for i, n in enumerate(ns))
            total_tuples += 1
            for u in range(91):  # Complete simultaneous residue system by integer CRT.
                lhs = cproduct(((-1) ** n.bit_count()) * char(n, u) for n in ns)
                rhs = (((-1) ** (len(inside) * c.bit_count()))
                       * literal_power(char(c, u), len(inside))
                       * cproduct(((-1) ** n.bit_count()) * char(n, u)
                                  for n in residuals))
                require(lhs == rhs, "CRT_designated_tuple_identity", (k, inside, ns, u))
                if any(char(n, u) == ZERO for n in ns):
                    require(rhs == ZERO, "CRT_retained_nonunit_zero", (ns, u))
    return {"prime_norms": [7, 13], "simultaneous_residue_count": 91,
            "squarefree_ideal_tuple_count": total_tuples}


def affine_add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def affine_scale(c, a):
    return (c * a[0], c * a[1])


def certify_affine(name, expression, lo, hi, strict=False):
    values = [expression[0] + expression[1] * h for h in (lo, hi)]
    require(all(v > 0 if strict else v >= 0 for v in values),
            "exact_affine_interval_certificate", (name, lo, hi, expression, values))
    return {"name": name, "h_interval": [str(lo), str(hi)],
            "affine_coefficients": list(map(str, expression)),
            "endpoint_values": list(map(str, values)), "strict": strict}


def exponent_checks():
    b, lo, hi = F(7, 8), F(1), F(11, 10)
    records = []
    fourth = (F(9, 11), F(-2, 11))
    for index, (hp, cp) in enumerate(
            ((F(1), 1 - 4*b), (F(1, 3), 2 - 4*b),
             (F(2, 3), F(5, 3) - 4*b)), 1):
        excess = affine_add((4*b - 2, hp - 1), affine_scale(cp, fourth))
        records.append(certify_affine(f"fourth tail term {index}",
                                     affine_scale(-1, excess), lo, hi))
    saving = affine_add((F(6, 7), F(-1, 7)), affine_scale(-1, fourth))
    require(saving == (F(3, 77), F(3, 77)), "cutoff_formula_identity", saving)
    records.append(certify_affine("sharp fourth strict improvement", saving, lo, hi, True))
    triple = (F(9, 17), F(0))
    for index, (hp, cp) in enumerate(
            ((F(1), 1 - 6*b), (F(1, 2), 1 - 5*b)), 1):
        excess = affine_add((6*b - 3, hp - 1), affine_scale(cp, triple))
        records.append(certify_affine(f"refined triple term {index}",
                                     affine_scale(-1, excess), lo, hi))
    branches = [
        (lo, F(27, 26), (F(1, 2), F(-4, 27))),
        (F(27, 26), hi, (F(27, 66), F(-4, 66))),
    ]
    for left, right, r in branches:
        for index, (hp, rp) in enumerate(
                ((F(0), 3 - 12*b), (F(-2, 3), 6 - 12*b),
                 (F(-1, 3), 5 - 12*b)), 1):
            excess = affine_add((6*b - 3, hp), affine_scale(rp, r))
            records.append(certify_affine(f"grouped triangle term {index}",
                                         affine_scale(-1, excess), left, right))
        old_minus_new = affine_add((F(1, 2), F(-1, 12)), affine_scale(-1, r))
        records.append(certify_affine("grouped triangle strict extension",
                                     old_minus_new, left, right, True))
        records.append(certify_affine("positive singleton log scale",
                                     affine_add((F(1), F(0)), affine_scale(-2, r)),
                                     left, right, True))
    switch = F(27, 26)
    require(F(1, 2) - 4*switch/27 == (27 - 4*switch)/66,
            "cutoff_formula_identity", ("grouped switch", switch))
    example_h = F(21, 20)
    grouped_example = max(F(3, 10), F(1, 2) - 4*example_h/27,
                          (27 - 4*example_h)/66)
    require(grouped_example == F(19, 55), "cutoff_formula_identity", grouped_example)
    require(F(33, 80) - grouped_example == F(59, 880),
            "cutoff_formula_identity", "matched grouped gain")
    require((6*b - 3)/(12*b - 5) == F(9, 22),
            "cutoff_formula_identity", "individual cubic axes")
    for m in (2, 3, 4, 6, 7):
        for beta in (F(3, 5), b, F(1)):
            for alpha in (F(1, 2), F(1), F(5, 6), (1+beta)/2):
                require(alpha + beta > 1 and m*beta > 1,
                        "designated_kernel_strict_weights", (m, beta, alpha))
            require(1-m*beta < 0, "tail_geometric_sign", (m, beta))
    for multiplicity in range(2, 9):
        weights = (F(multiplicity, 2), F(multiplicity), F(5*multiplicity, 6))
        require(all(w >= 1 for w in weights),
                "physical_cubic_shared_weights", (multiplicity, weights))
        require([i for i, w in enumerate(weights) if w == 1]
                == ([0] if multiplicity == 2 else []),
                "physical_cubic_critical_pair_only", (multiplicity, weights))
    critical = [F(1, 2)] * 6 + [b] * 6
    for i, j in itertools.combinations(range(len(critical)), 2):
        require(critical[i] + critical[j] >= 1,
                "grouped_mixed_kernel_critical_weights", (i, j))
    return {"scope": "exact affine endpoint certificates prove each stated interval",
            "certificates": records, "grouped_example_h": str(example_h),
            "grouped_example_cutoff": str(grouped_example),
            "old_example_cutoff": "33/80", "exact_example_gain": "59/880"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--note", type=Path,
                        default=Path(__file__).with_name("MOBIUS_OVERLAP_TAILS.md"))
    parser.add_argument("--json", type=Path,
                        default=Path(__file__).with_name("mobius_overlap_validation.json"))
    parser.add_argument("--expected-note-sha256", default=EXPECTED_NOTE_SHA256)
    args = parser.parse_args()
    note_hash = hashlib.sha256(args.note.read_bytes()).hexdigest()
    require(note_hash == args.expected_note_sha256,
            "frozen_source_note_binding", (note_hash, args.expected_note_sha256))
    tables, primitives = primitive_tables()
    designated = designated_local_checks(tables)
    mixed = mixed_local_checks(tables)
    crt = crt_tuple_checks(tables)
    exponents = exponent_checks()
    report = {
        "status": "PASS",
        "scope": "bounded primitive/local algebra and exact exponent certificates only",
        "not_verified": ["PW_b", "R_b", "an infinite character sieve",
                         "an infinite Euler product", "a full moment theorem"],
        "arithmetic": "integer pairs in Z[zeta_6] and fractions.Fraction; no floating point",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "note_sha256": note_hash,
        "checks": dict(sorted(COUNTS.items())),
        "total_checks": sum(COUNTS.values()),
        "primitive_split_prime_panels": primitives,
        "designated_local_cases": designated,
        "mixed_positive_inverse_cases": mixed,
        "CRT_tuple_panel": crt,
        "exponent_certificates": exponents,
        "reproducibility": "No absolute paths, timestamps, or optimization-mode fields.",
    }
    args.json.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n",
                         encoding="utf-8")
    print(json.dumps({key: report[key] for key in
                      ("status", "total_checks", "source_sha256", "note_sha256")},
                     sort_keys=True))


if __name__ == "__main__":
    main()
