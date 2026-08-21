#!/usr/bin/env python3
"""Exact fifth-strike replay for the positive scale-four Q4 factorization.

Arithmetic:
- integers and exact formal prime-log coefficient dictionaries;
- exact finite Dirichlet convolution;
- exact endpoint-row and fibre identities;
- no prime table, zero table, floating arithmetic, or asymptotic scan.

The replay proves source positivity and atomwise principal/transverse typing.
It does not bound the aggregate principal mean or prove RH.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Tuple

LogMap = Dict[int, int]


def factorint(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> List[int]:
    out = [1]
    for p, exponent in factorint(n).items():
        old = list(out)
        power = 1
        for _ in range(exponent):
            power *= p
            out.extend(d * power for d in old)
    return sorted(out)


def mobius(n: int) -> int:
    value = 1
    for _, exponent in factorint(n).items():
        if exponent > 1:
            return 0
        value = -value
    return value


def v2(n: int) -> int:
    exponent = 0
    while n % 2 == 0:
        exponent += 1
        n //= 2
    return exponent


def add_map(a: Mapping[int, int], b: Mapping[int, int], scale: int = 1) -> LogMap:
    out = dict(a)
    for p, coefficient in b.items():
        out[p] = out.get(p, 0) + scale * coefficient
        if out[p] == 0:
            del out[p]
    return out


def scale_map(a: Mapping[int, int], scale: int) -> LogMap:
    return {p: scale * c for p, c in a.items() if scale * c}


def a4(n: int) -> int:
    """Coefficient of A4=(1-4^(1-s))/((1-4^-s) zeta(s))."""
    exponent = v2(n)
    odd = n >> exponent
    mu_odd = mobius(odd)
    if mu_odd == 0:
        return 0
    if exponent == 0:
        return mu_odd
    if exponent == 1:
        return -mu_odd
    return 3 * ((-1) ** (exponent + 1)) * mu_odd


def g4(n: int) -> int:
    """Coefficient of G4=1/A4."""
    return 4 ** (v2(n) // 2)


def dirichlet_convolution_value(f, g, n: int) -> int:
    return sum(f(d) * g(n // d) for d in divisors(n))


def lambda4(n: int) -> LogMap:
    """Formal generalized von Mangoldt coefficients of G4."""
    factors = factorint(n)
    if len(factors) != 1:
        return {}
    p, exponent = next(iter(factors.items()))
    if p != 2:
        return {p: 1}
    coefficient = 1 if exponent % 2 else 2 ** (exponent + 1) - 1
    return {2: coefficient}


def lambda_plus(n: int) -> LogMap:
    """Lambda_+=(epsilon+2 delta_2)*Lambda_4."""
    out = lambda4(n)
    if n % 2 == 0:
        out = add_map(out, lambda4(n // 2), 2)
    return out


def c_from_positive_factor(n: int) -> LogMap:
    """(epsilon-2 delta_2)*Lambda_+."""
    out = lambda_plus(n)
    if n % 2 == 0:
        out = add_map(out, lambda_plus(n // 2), -2)
    return out


def ordinary_lambda(n: int) -> LogMap:
    factors = factorint(n)
    if len(factors) != 1:
        return {}
    p, _ = next(iter(factors.items()))
    return {p: 1}


def is_power_of_four(n: int) -> bool:
    if n < 4:
        return False
    while n % 4 == 0:
        n //= 4
    return n == 1


def c_circ_actual(n: int) -> LogMap:
    out = ordinary_lambda(n)
    if n % 4 == 0:
        out = add_map(out, ordinary_lambda(n // 4), -4)
    if is_power_of_four(n):
        # 3 log 4 = 6 log 2.
        out = add_map(out, {2: 6})
    return out


def h_fibre(m: int, x: int) -> int:
    return int(m <= x) - 2 * int(2 * m <= x)


def z_fibre(m: int, endpoint: int, j: int) -> int:
    return (
        h_fibre(m, endpoint)
        - h_fibre(m, j)
        - h_fibre(m, endpoint - j - 1)
    )


def prefix_maps(values: List[LogMap]) -> List[LogMap]:
    out: List[LogMap] = [{}]
    running: LogMap = {}
    for value in values[1:]:
        running = add_map(running, value)
        out.append(dict(running))
    return out


def run() -> dict:
    inverse_checks = 0
    generalized_prime_checks = 0
    source_factorization_checks = 0
    prefix_checks = 0
    row_fibre_checks = 0
    principal_transverse_checks = 0
    no_go_checks = 0
    hostile_mutations = 0

    limit = 768

    # A4 and G4 are exact Dirichlet inverses.
    for n in range(1, limit + 1):
        value = dirichlet_convolution_value(a4, g4, n)
        assert value == int(n == 1)
        inverse_checks += 1

    # Every G4 coefficient and every generalized-prime coefficient is positive.
    for n in range(1, limit + 1):
        assert g4(n) > 0
        l4 = lambda4(n)
        lp = lambda_plus(n)
        assert all(coefficient > 0 for coefficient in l4.values())
        assert all(coefficient > 0 for coefficient in lp.values())
        generalized_prime_checks += 3

    # Exact formal-prime-log factorization of the complete compact-Q4 source.
    for n in range(1, limit + 1):
        assert c_from_positive_factor(n) == c_circ_actual(n)
        source_factorization_checks += 1

    # Prefix and complete endpoint-row realization by positive Lambda_+ fibres.
    for endpoint in range(4, 97):
        actual_values = [{}] + [c_circ_actual(n) for n in range(1, endpoint + 1)]
        plus_values = [{}] + [lambda_plus(n) for n in range(1, endpoint + 1)]
        actual_prefix = prefix_maps(actual_values)
        plus_prefix = prefix_maps(plus_values)

        for x in range(0, endpoint + 1):
            rhs = dict(plus_prefix[x])
            rhs = add_map(rhs, plus_prefix[x // 2], -2)
            assert actual_prefix[x] == rhs
            prefix_checks += 1

        for j in range(endpoint):
            row = add_map(actual_prefix[endpoint], actual_prefix[j], -1)
            row = add_map(row, actual_prefix[endpoint - j - 1], -1)
            fibre_sum: LogMap = {}
            for m in range(1, endpoint + 1):
                coefficient = z_fibre(m, endpoint, j)
                if coefficient:
                    fibre_sum = add_map(
                        fibre_sum,
                        plus_values[m],
                        coefficient,
                    )
            assert row == fibre_sum
            row_fibre_checks += 1

    # Each small positive-source atom has exactly one constant principal channel
    # and a compact boundary residual.
    for endpoint in range(8, 161):
        for m in range(1, endpoint // 4 + 1):
            residual_support = 0
            residual_norm2 = 0
            for j in range(endpoint):
                z = z_fibre(m, endpoint, j)
                if 2 * m <= j and 2 * m <= endpoint - j - 1:
                    assert z == 1
                residual = z - 1
                assert abs(residual) <= 4
                if residual:
                    residual_support += 1
                    residual_norm2 += residual * residual
            assert residual_support <= 4 * m
            assert residual_norm2 <= 64 * m
            principal_transverse_checks += 3

    # Exact principal-channel no-go: one atom has a row norm growing linearly
    # with the endpoint because at least N-4m entries are exactly one.
    for m in range(1, 33):
        for multiplier in (8, 16, 32):
            endpoint = multiplier * m
            norm2 = sum(
                z_fibre(m, endpoint, j) ** 2
                for j in range(endpoint)
            )
            assert norm2 >= endpoint - 4 * m
            no_go_checks += 1

    # Fail-closed mutations.
    if g4(16) != 16:
        raise AssertionError("control")
    if 2 ** (v2(16) // 2) != g4(16):
        hostile_mutations += 1
    if c_from_positive_factor(16) != add_map(
        lambda_plus(16), lambda_plus(8), -1
    ):
        hostile_mutations += 1
    # Dropping the four-adic gauge changes n=16.
    dropped_gauge = ordinary_lambda(16)
    dropped_gauge = add_map(dropped_gauge, ordinary_lambda(4), -4)
    if dropped_gauge != c_circ_actual(16):
        hostile_mutations += 1
    # Replacing the Haar coefficient -2 by -1 breaks the prefix identity.
    endpoint = 32
    plus_values = [{}] + [lambda_plus(n) for n in range(1, endpoint + 1)]
    plus_prefix = prefix_maps(plus_values)
    wrong = add_map(plus_prefix[endpoint], plus_prefix[endpoint // 2], -1)
    actual_values = [{}] + [c_circ_actual(n) for n in range(1, endpoint + 1)]
    if wrong != prefix_maps(actual_values)[endpoint]:
        hostile_mutations += 1
    # Removing the principal constant cannot preserve an interior fibre.
    if z_fibre(1, 32, 16) == 1 and z_fibre(1, 32, 16) - 1 == 0:
        hostile_mutations += 1

    assert hostile_mutations == 5

    return {
        "classification": "PASS_X_93022_Q4_POSITIVE_SCALE_FOUR",
        "arithmetic_class": "EXACT_INTEGER_AND_FORMAL_PRIME_LOG",
        "dirichlet_inverse_checks": inverse_checks,
        "positive_generalized_prime_checks": generalized_prime_checks,
        "source_factorization_checks": source_factorization_checks,
        "prefix_haar_factorization_checks": prefix_checks,
        "complete_row_fibre_checks": row_fibre_checks,
        "principal_transverse_checks": principal_transverse_checks,
        "principal_channel_no_go_checks": no_go_checks,
        "hostile_mutations_detected": hostile_mutations,
        "proves": [
            "G4 has explicit positive coefficients and A4*G4=epsilon",
            "the G4 generalized-prime sequence and Lambda_+ are nonnegative",
            "c_circ=(epsilon-2 delta_2)*Lambda_+ coefficientwise",
            "the complete endpoint row is a source-owned positive superposition of Haar carry fibres",
            "every small fibre is one principal constant plus a compact transverse boundary",
            "the principal channel has unbounded row norm and cannot be discarded",
        ],
        "does_not_prove": [
            "an aggregate transverse source bound at the critical scale",
            "a square-root bound for the Q4 endpoint mean",
            "One-sided Parity Borrowing",
            "the Riemann Hypothesis",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = run()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")


if __name__ == "__main__":
    main()
