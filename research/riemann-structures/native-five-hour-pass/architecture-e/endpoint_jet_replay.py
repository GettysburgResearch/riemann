"""Exact four-jet algebra and a fixed high-precision endpoint scout."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREFIX = "research/riemann-structures/native-five-hour-pass/architecture-e/"
ARTIFACT = HERE / "endpoint_jet_verification.json"
OWNED = (
    PREFIX + "ENDPOINT_FOUR_JET_FACTORIZATION.md",
    PREFIX + "ENDPOINT_JET_PREREGISTRATION.md",
    PREFIX + "endpoint_jet_replay.py",
    PREFIX + "ENDPOINT_JET_REPLAY.md",
    "tests/test_architecture_e_pass_endpoint_jet.py",
)
NVAR = 4
PRECISION = 100


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_load(text):
    def pairs(items):
        result = {}
        for key, value in items:
            need(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def reject(_value):
        raise ValueError("noncanonical JSON number")

    return json.loads(
        text, object_pairs_hook=pairs, parse_float=reject, parse_constant=reject
    )


def constant(value):
    value = Q(value)
    return {} if not value else {(0,) * NVAR: value}


def variable(index):
    exponent = [0] * NVAR
    exponent[index] = 1
    return {tuple(exponent): Q(1)}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, Q(0)) + coefficient
            if not result[exponent]:
                del result[exponent]
    return result


def scale(polynomial, coefficient):
    coefficient = Q(coefficient)
    return {e: coefficient * c for e, c in polynomial.items() if coefficient * c}


def multiply(*polynomials):
    result = constant(1)
    for polynomial in polynomials:
        product = {}
        for left, lc in result.items():
            for right, rc in polynomial.items():
                exponent = tuple(a + b for a, b in zip(left, right, strict=True))
                product[exponent] = product.get(exponent, Q(0)) + lc * rc
        result = {e: c for e, c in product.items() if c}
    return result


def permutation_sign(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def determinant(matrix):
    n = len(matrix)
    result = {}
    for permutation in itertools.permutations(range(n)):
        term = multiply(*(matrix[i][permutation[i]] for i in range(n)))
        result = add(result, scale(term, permutation_sign(permutation)))
    return result


def jet_matrix():
    f = [variable(i) for i in range(NVAR)]
    matrix = []
    for i in range(4):
        row = []
        for j in range(4):
            terms = []
            for r in range(i + 1):
                terms.append(
                    scale(f[r], math.comb(i, r) * (-1) ** r * math.factorial(i - r + j))
                )
            for r in range(j + 1):
                terms.append(
                    scale(f[r], math.comb(j, r) * (-1) ** r * math.factorial(i + j - r))
                )
            row.append(add(*terms))
        matrix.append(row)
    return matrix


def declared_factors():
    f0, f1, f2, f3 = (variable(i) for i in range(4))
    d1 = scale(f0, 2)
    d2 = multiply(add(scale(f0, 2), scale(f1, -1)), add(scale(f0, 2), scale(f1, 1)))
    d3 = scale(
        multiply(
            add(scale(f0, 4), scale(f1, -2), scale(f2, -1)),
            add(
                scale(multiply(f0, f0), 4),
                scale(multiply(f0, f1), 2),
                multiply(f0, f2),
                scale(multiply(f1, f1), -2),
            ),
        ),
        2,
    )
    minus = add(
        scale(multiply(f0, f0), 48),
        scale(multiply(f0, f1), -48),
        scale(multiply(f0, f2), -24),
        scale(multiply(f0, f3), -4),
        scale(multiply(f1, f1), 12),
        scale(multiply(f1, f2), 12),
        scale(multiply(f1, f3), 2),
        scale(multiply(f2, f2), -3),
    )
    plus = add(
        scale(multiply(f0, f0), 48),
        scale(multiply(f0, f1), 48),
        scale(multiply(f0, f2), 24),
        scale(multiply(f0, f3), 4),
        scale(multiply(f1, f1), -36),
        scale(multiply(f1, f2), -12),
        scale(multiply(f1, f3), 2),
        scale(multiply(f2, f2), -3),
    )
    return [d1, d2, d3, multiply(minus, plus)], minus, plus


def encode_polynomial(polynomial):
    return [
        {"exponents": list(exponent), "coefficient": str(coefficient)}
        for exponent, coefficient in sorted(polynomial.items())
    ]


def exact_algebra():
    matrix = jet_matrix()
    determinants = [determinant([row[:n] for row in matrix[:n]]) for n in range(1, 5)]
    declared, minus, plus = declared_factors()
    need(determinants == declared, "leading determinant factorization")

    f0, f1, f2, f3 = (variable(i) for i in range(4))
    a = Q(1, 2)
    d = scale(f0, 2)
    b1 = scale(f1, 2 * a)
    b2 = add(scale(f1, 2 * a), scale(f2, 2 * a * a))
    b3 = add(scale(f1, 2 * a), scale(f2, 4 * a * a), scale(f3, Q(4, 3) * a**3))
    toeplitz = [[d, b1, b2, b3], [b1, d, b1, b2], [b2, b1, d, b1], [b3, b2, b1, d]]
    odd = add(
        multiply(add(d, scale(b3, -1)), add(d, scale(b1, -1))),
        scale(multiply(add(b1, scale(b2, -1)), add(b1, scale(b2, -1))), -1),
    )
    even = add(
        multiply(add(d, b3), add(d, b1)), scale(multiply(add(b1, b2), add(b1, b2)), -1)
    )
    need(
        determinant(toeplitz) == multiply(odd, even),
        "Toeplitz reflection factorization",
    )
    return {
        "jet_matrix": [[encode_polynomial(x) for x in row] for row in matrix],
        "leading_determinants": [encode_polynomial(x) for x in determinants],
        "D4_reflection_factors": [encode_polynomial(minus), encode_polynomial(plus)],
        "toeplitz_reflection_factors": [
            encode_polynomial(odd),
            encode_polynomial(even),
        ],
    }


def endpoint_values():
    mp.mp.dps = PRECISION
    log2 = mp.log(2)

    def xi(s):
        h = s - 1
        removable = 1 / log2 if h == 0 else h / (-mp.expm1(-h * log2))
        return (
            mp.mpf("0.5")
            * s
            * mp.power(mp.pi, -s / 2)
            * mp.gamma(s / 2)
            * mp.altzeta(s)
            * removable
        )

    coefficients = mp.taylor(lambda z: mp.log(xi(1 + z)), 0, 8)
    f = [mp.factorial(r + 1) * coefficients[r + 1] for r in range(8)]
    a = mp.mpf("0.5")
    d = 2 * f[0]
    b1 = 2 * a * f[1]
    b2 = 2 * a * f[1] + 2 * a**2 * f[2]
    b3 = 2 * a * f[1] + 4 * a**2 * f[2] + mp.mpf(4) / 3 * a**3 * f[3]
    toeplitz = mp.matrix(
        [[d, b1, b2, b3], [b1, d, b1, b2], [b2, b1, d, b1], [b3, b2, b1, d]]
    )
    eigenvalues = list(mp.eigsy(toeplitz, eigvals_only=True))
    odd = (d - b3) * (d - b1) - (b1 - b2) ** 2
    even = (d + b3) * (d + b1) - (b1 + b2) ** 2
    need(
        all(x > 0 for x in eigenvalues) and odd > 0 and even > 0, "scout endpoint signs"
    )
    return {
        "precision_decimal_digits": PRECISION,
        "F_derivatives_0_through_7": [mp.nstr(x, 72) for x in f],
        "orthonormal_eigenvalues": [mp.nstr(x, 72) for x in eigenvalues],
        "toeplitz_odd_factor": mp.nstr(odd, 72),
        "toeplitz_even_factor": mp.nstr(even, 72),
        "endpoint_signs_positive_at_working_precision": True,
    }


def build():
    sources = {}
    for path in OWNED:
        raw = (ROOT / path).read_bytes()
        need(len(raw) < 2_000_000, "owned source cap")
        sources[path] = hashlib.sha256(raw).hexdigest()
    record = {
        "kind": "architecture-e-endpoint-four-jet",
        "exact_algebra": exact_algebra(),
        "numerical_scout": endpoint_values(),
        "owned_sources": sources,
        "scope": {
            "endpoint_exact_factorization": True,
            "numerical_endpoint_reconnaissance": True,
            "endpoint_signs_interval_certified": False,
            "local_neighborhood": False,
            "continuum_four_node_theorem": False,
            "rh": False,
        },
    }
    record["proof_sha256"] = hashlib.sha256(canonical(record).encode()).hexdigest()
    return record


def accept(candidate, fresh):
    need(
        type(candidate) is dict and canonical(candidate) == canonical(fresh),
        "fresh typed record",
    )
    body = {key: value for key, value in candidate.items() if key != "proof_sha256"}
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest()
        == candidate["proof_sha256"],
        "body digest",
    )
    need(
        candidate["scope"]["endpoint_signs_interval_certified"] is False,
        "interval scope",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    need(args.write ^ args.check, "choose exactly one mode")
    fresh = build()
    if args.write:
        ARTIFACT.write_text(json.dumps(fresh, sort_keys=True, indent=2) + "\n")
    else:
        accept(strict_load(ARTIFACT.read_text()), fresh)
    print(canonical({"status": "PASS", "proof_sha256": fresh["proof_sha256"]}))


if __name__ == "__main__":
    main()
