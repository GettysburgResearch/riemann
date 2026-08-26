#!/usr/bin/env python3
"""Bounded exact replay for the primitive rho-tilt convolution isomorphism."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections.abc import Callable
from fractions import Fraction
from itertools import product
from math import gcd, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md"
EXCEPTIONAL_PRIME = 67
PREDECESSOR_COMMIT = "05da4d1705d994dd02d650f321196f8464034ba8"
PREDECESSOR_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md"
    ): "722ca5bd8acef2efdb5591f29935b4f97102f957",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_pair_harmonic_incidence_carleson.py"
    ): "7e780f0109264dbfaac59cae36db6fd72c3f34ee",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_pair_harmonic_incidence_carleson.json"
    ): "f0a556f8f3ab2db04f7e434646ac4c70987ae50f",
    "tests/test_ffps_primitive_pair_harmonic_incidence_carleson.py": (
        "abaded5c04b4cec8464618f2dfff74a486ab025b"
    ),
}
REPLAY_PRIMES = (2, 3, 5, 7, 11)
REPLAY_MAX_EXPONENT = 5
REPLAY_GLOBAL_LIMIT = 120
REPLAY_MATRIX_LIMIT = 24
REPLAY_SUMMATORY_LIMIT = 160
REPLAY_SUPPORT_LIMIT = 8

ArithmeticFunction = Callable[[int], Fraction]


def check_predecessor_blobs() -> None:
    """Pin both the frozen tree entries and the predecessor files being extended."""
    for path, expected in PREDECESSOR_BLOBS.items():
        frozen = subprocess.run(
            ["git", "rev-parse", f"{PREDECESSOR_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if frozen != expected:
            raise RuntimeError(f"frozen predecessor blob mismatch: {path}")
        working = subprocess.run(
            ["git", "hash-object", path],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if working != expected:
            raise RuntimeError(f"working predecessor blob mismatch: {path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "the undilated PRIMCAR parameter class is not closed",
        "does not bound the predecessor's nonzero Boolean modes",
        "The weaker weighted vector gate remains",
        "No such generalized-scale cancellation theorem is supplied.",
        "the zero mode itself is not averaged over `d`",
        "abstract positive-norm arrays",
        "neither gate implies the other",
        "Neither controls any nonzero `PRIMCAR` mode",
        "No PRIMCAR, PRIMLS, RH, or GRH estimate is proved.",
        "No external novelty claim is made.",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing from note: {marker}")


def validate_positive_integer(n: int) -> None:
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("input must be a positive integer")


def validate_domain_integer(n: int) -> None:
    validate_positive_integer(n)
    if n % EXCEPTIONAL_PRIME == 0:
        raise ValueError("input must lie in the 67-free multiplicative monoid")


def is_prime(n: int) -> bool:
    if isinstance(n, bool) or not isinstance(n, int) or n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    validate_positive_integer(n)
    factors: list[tuple[int, int]] = []
    remaining = n
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            exponent = 0
            while remaining % prime == 0:
                remaining //= prime
                exponent += 1
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return tuple(factors)


def divisors(n: int) -> tuple[int, ...]:
    validate_positive_integer(n)
    result = [1]
    for prime, exponent in factorization(n):
        old = tuple(result)
        power = 1
        for _ in range(exponent):
            power *= prime
            result.extend(item * power for item in old)
    return tuple(sorted(result))


def mobius(n: int) -> int:
    validate_positive_integer(n)
    sign = 1
    for _, exponent in factorization(n):
        if exponent > 1:
            return 0
        sign = -sign
    return sign


def rho(n: int) -> Fraction:
    validate_domain_integer(n)
    result = Fraction(1)
    for prime, _ in factorization(n):
        result *= Fraction(prime, prime + 1)
    return result


def m(n: int) -> Fraction:
    validate_domain_integer(n)
    return Fraction(mobius(n))


def a(n: int) -> Fraction:
    validate_domain_integer(n)
    return Fraction(mobius(n)) * rho(n)


def validate_prime_power(prime: int, exponent: int) -> None:
    if not is_prime(prime) or prime == EXCEPTIONAL_PRIME:
        raise ValueError("prime must be prime and different from 67")
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")


def g_prime_power(prime: int, exponent: int) -> Fraction:
    validate_prime_power(prime, exponent)
    if exponent == 0:
        return Fraction(1)
    return Fraction(1, prime + 1)


def h_prime_power(prime: int, exponent: int) -> Fraction:
    validate_prime_power(prime, exponent)
    if exponent == 0:
        return Fraction(1)
    return -Fraction(1, prime + 1) * Fraction(prime, prime + 1) ** (exponent - 1)


def g(n: int) -> Fraction:
    validate_domain_integer(n)
    result = Fraction(1)
    for prime, exponent in factorization(n):
        result *= g_prime_power(prime, exponent)
    return result


def h(n: int) -> Fraction:
    validate_domain_integer(n)
    result = Fraction(1)
    for prime, exponent in factorization(n):
        result *= h_prime_power(prime, exponent)
    return result


def delta(n: int) -> Fraction:
    validate_domain_integer(n)
    return Fraction(int(n == 1))


def dirichlet_convolution_value(
    left: ArithmeticFunction, right: ArithmeticFunction, n: int
) -> Fraction:
    validate_domain_integer(n)
    return sum(
        (left(divisor) * right(n // divisor) for divisor in divisors(n)), Fraction()
    )


def local_m(prime: int, exponent: int) -> Fraction:
    validate_prime_power(prime, exponent)
    if exponent == 0:
        return Fraction(1)
    if exponent == 1:
        return Fraction(-1)
    return Fraction(0)


def local_a(prime: int, exponent: int) -> Fraction:
    validate_prime_power(prime, exponent)
    if exponent == 0:
        return Fraction(1)
    if exponent == 1:
        return -Fraction(prime, prime + 1)
    return Fraction(0)


def local_convolution_coefficient(
    left: Callable[[int, int], Fraction],
    right: Callable[[int, int], Fraction],
    prime: int,
    exponent: int,
) -> Fraction:
    validate_prime_power(prime, exponent)
    return sum(
        (
            left(prime, item) * right(prime, exponent - item)
            for item in range(exponent + 1)
        ),
        Fraction(),
    )


def local_coefficient_panel(
    prime: int, max_exponent: int = REPLAY_MAX_EXPONENT
) -> dict[str, object]:
    validate_prime_power(prime, max_exponent)
    rows = []
    for exponent in range(max_exponent + 1):
        mg = local_convolution_coefficient(local_m, g_prime_power, prime, exponent)
        ah = local_convolution_coefficient(local_a, h_prime_power, prime, exponent)
        gh = local_convolution_coefficient(
            g_prime_power, h_prime_power, prime, exponent
        )
        expected_a = local_a(prime, exponent)
        expected_m = local_m(prime, exponent)
        expected_delta = Fraction(int(exponent == 0))
        if mg != expected_a or ah != expected_m or gh != expected_delta:
            raise ArithmeticError("local convolution identity failed")
        rows.append(
            {
                "a": str(expected_a),
                "a_times_h": str(ah),
                "delta": str(expected_delta),
                "exponent": exponent,
                "g": str(g_prime_power(prime, exponent)),
                "g_times_h": str(gh),
                "h": str(h_prime_power(prime, exponent)),
                "m": str(expected_m),
                "m_times_g": str(mg),
            }
        )
    return {"prime": prime, "rho_p": str(Fraction(prime, prime + 1)), "rows": rows}


def global_identity_panel(limit: int = REPLAY_GLOBAL_LIMIT) -> dict[str, object]:
    validate_positive_integer(limit)
    checked = 0
    sample_rows = []
    sample_set = {1, 2, 4, 6, 12, 30, 60, 84, 120}
    for n in range(1, limit + 1):
        if n % EXCEPTIONAL_PRIME == 0:
            continue
        mg = dirichlet_convolution_value(m, g, n)
        ah = dirichlet_convolution_value(a, h, n)
        gh = dirichlet_convolution_value(g, h, n)
        if mg != a(n) or ah != m(n) or gh != delta(n):
            raise ArithmeticError(f"global convolution identity failed at n={n}")
        checked += 1
        if n in sample_set:
            sample_rows.append(
                {
                    "a": str(a(n)),
                    "a_times_h": str(ah),
                    "g": str(g(n)),
                    "g_times_h": str(gh),
                    "h": str(h(n)),
                    "m": str(m(n)),
                    "m_times_g": str(mg),
                    "n": n,
                }
            )
    return {"checked_integers": checked, "limit": limit, "sample_rows": sample_rows}


def truncated_operator_matrix(
    kernel: ArithmeticFunction, limit: int
) -> tuple[tuple[int, ...], list[list[Fraction]]]:
    validate_positive_integer(limit)
    domain = tuple(n for n in range(1, limit + 1) if n % EXCEPTIONAL_PRIME)
    matrix = []
    for output in domain:
        row = []
        for input_value in domain:
            row.append(
                kernel(output // input_value)
                if output % input_value == 0
                else Fraction()
            )
        matrix.append(row)
    return domain, matrix


def multiply_matrices(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    if not left or not right or len(left[0]) != len(right):
        raise ValueError("incompatible matrix dimensions")
    return [
        [
            sum(
                (left[row][mid] * right[mid][column] for mid in range(len(right))),
                Fraction(),
            )
            for column in range(len(right[0]))
        ]
        for row in range(len(left))
    ]


def rational_matrix_digest(matrix: list[list[Fraction]]) -> str:
    payload = json.dumps(
        [[str(entry) for entry in row] for row in matrix],
        separators=(",", ":"),
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def finite_operator_certificate(limit: int = REPLAY_MATRIX_LIMIT) -> dict[str, object]:
    domain_g, matrix_g = truncated_operator_matrix(g, limit)
    domain_h, matrix_h = truncated_operator_matrix(h, limit)
    if domain_g != domain_h:
        raise ArithmeticError("finite operator domains disagree")
    identity = [
        [Fraction(int(row == column)) for column in range(len(domain_g))]
        for row in range(len(domain_g))
    ]
    if multiply_matrices(matrix_g, matrix_h) != identity:
        raise ArithmeticError("finite T_g T_h identity failed")
    if multiply_matrices(matrix_h, matrix_g) != identity:
        raise ArithmeticError("finite T_h T_g identity failed")
    return {
        "dimension": len(domain_g),
        "domain_max": limit,
        "g_matrix_digest": rational_matrix_digest(matrix_g),
        "g_nonzero_entries": sum(bool(entry) for row in matrix_g for entry in row),
        "h_matrix_digest": rational_matrix_digest(matrix_h),
        "h_nonzero_entries": sum(bool(entry) for row in matrix_h for entry in row),
        "inverse_both_orders": True,
        "unit_diagonal": all(
            matrix_g[i][i] == matrix_h[i][i] == 1 for i in range(len(domain_g))
        ),
    }


def partial_sum(function: ArithmeticFunction, limit: int) -> Fraction:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    return sum(
        (function(n) for n in range(1, limit + 1) if n % EXCEPTIONAL_PRIME),
        Fraction(),
    )


def summatory_transfer_panel(limit: int = REPLAY_SUMMATORY_LIMIT) -> dict[str, object]:
    validate_positive_integer(limit)
    samples = {1, 2, 5, 10, 20, 40, 80, limit}
    rows = []
    for x in range(1, limit + 1):
        sum_a = partial_sum(a, x)
        from_m = sum(
            (
                g(r) * partial_sum(m, x // r)
                for r in range(1, x + 1)
                if r % EXCEPTIONAL_PRIME
            ),
            Fraction(),
        )
        sum_m = partial_sum(m, x)
        from_a = sum(
            (
                h(r) * partial_sum(a, x // r)
                for r in range(1, x + 1)
                if r % EXCEPTIONAL_PRIME
            ),
            Fraction(),
        )
        if sum_a != from_m or sum_m != from_a:
            raise ArithmeticError(f"summatory transfer failed at x={x}")
        if x in samples:
            rows.append(
                {
                    "M_0": str(sum_m),
                    "M_0_from_h": str(from_a),
                    "M_rho": str(sum_a),
                    "M_rho_from_g": str(from_m),
                    "x": x,
                }
            )
    return {"checked_endpoints": limit, "sample_rows": rows}


def full_mertens(limit: int) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    return sum(mobius(n) for n in range(1, limit + 1))


def away_mertens(limit: int) -> int:
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("limit must be a nonnegative integer")
    return sum(mobius(n) for n in range(1, limit + 1) if n % EXCEPTIONAL_PRIME)


def exceptional_prime_transfer_panel(
    limit: int = REPLAY_SUMMATORY_LIMIT,
) -> dict[str, object]:
    validate_positive_integer(limit)
    rows = []
    samples = {1, 66, 67, 68, 134, limit}
    for x in range(1, limit + 1):
        full_from_away = away_mertens(x) - away_mertens(x // EXCEPTIONAL_PRIME)
        away_from_full = 0
        power = 1
        while power <= x:
            away_from_full += full_mertens(x // power)
            power *= EXCEPTIONAL_PRIME
        if full_from_away != full_mertens(x) or away_from_full != away_mertens(x):
            raise ArithmeticError(f"exceptional-prime transfer failed at x={x}")
        if x in samples:
            rows.append(
                {
                    "M": full_mertens(x),
                    "M_0": away_mertens(x),
                    "M_0_from_M": away_from_full,
                    "M_from_M_0": full_from_away,
                    "x": x,
                }
            )
    return {"checked_endpoints": limit, "sample_rows": rows}


def pair_coefficient_panel() -> dict[str, object]:
    """Check the half-weighted pair identity after clearing sqrt(u*v)."""
    pairs = ((2, 3), (6, 5), (6, 10), (12, 5), (30, 14))
    rows = []
    for u, v in pairs:
        direct_rho = a(u) * a(v)
        via_g = sum(
            (
                g(r) * g(s) * m(u // r) * m(v // s)
                for r in divisors(u)
                for s in divisors(v)
            ),
            Fraction(),
        )
        direct_ordinary = m(u) * m(v)
        via_h = sum(
            (
                h(r) * h(s) * a(u // r) * a(v // s)
                for r in divisors(u)
                for s in divisors(v)
            ),
            Fraction(),
        )
        if direct_rho != via_g or direct_ordinary != via_h:
            raise ArithmeticError("half-weighted pair coefficient identity failed")
        rows.append(
            {
                "common_half_weight": f"1/sqrt({u * v})",
                "ordinary_scaled_coefficient": str(direct_ordinary),
                "ordinary_via_h_scaled_coefficient": str(via_h),
                "rho_scaled_coefficient": str(direct_rho),
                "rho_via_g_scaled_coefficient": str(via_g),
                "u": u,
                "v": v,
            }
        )
    return {
        "identity": ("c_rho(u)c_rho(v)=sum_(rm=u,sn=v) g(r)g(s)c_0(m)c_0(n)/sqrt(rs)"),
        "rows_after_clearing_common_half_weight": rows,
    }


def primitive_boolean_pair_panel() -> dict[str, object]:
    """Replay the squarefree-coprime compression of the actual pair support."""
    pairs = ((1, 2), (2, 3), (6, 5), (30, 7), (14, 15))
    rows = []
    for u, v in pairs:
        if mobius(u) == 0 or mobius(v) == 0 or gcd(u, v) != 1:
            raise ArithmeticError("primitive Boolean replay pair is inadmissible")
        forward = Fraction()
        inverse = Fraction()
        checked_outer_pairs = 0
        for r in divisors(u):
            for s in divisors(v):
                if mobius(r) == 0 or mobius(s) == 0 or gcd(r, s) != 1:
                    raise ArithmeticError("surviving outer pair is not Boolean-coprime")
                if abs(h(r)) != g(r) or abs(h(s)) != g(s):
                    raise ArithmeticError("forward/inverse Boolean masses disagree")
                forward += g(r) * g(s) * m(u // r) * m(v // s)
                inverse += h(r) * h(s) * a(u // r) * a(v // s)
                checked_outer_pairs += 1
        if forward != a(u) * a(v) or inverse != m(u) * m(v):
            raise ArithmeticError("primitive Boolean pair identity failed")
        rows.append(
            {
                "checked_outer_pairs": checked_outer_pairs,
                "ordinary_scaled_coefficient": str(m(u) * m(v)),
                "ordinary_via_boolean_h": str(inverse),
                "rho_scaled_coefficient": str(a(u) * a(v)),
                "rho_via_boolean_g": str(forward),
                "u": u,
                "v": v,
            }
        )
    local_rows = []
    for prime in REPLAY_PRIMES:
        local_mass = g_prime_power(prime, 1)
        if abs(h_prime_power(prime, 1)) != local_mass:
            raise ArithmeticError("Boolean forward/inverse local masses disagree")
        local_rows.append(
            {
                "absolute_forward_state_mass": str(local_mass),
                "absolute_inverse_state_mass": str(local_mass),
                "local_outer_states": ["absent", "in_r", "in_s"],
                "pair_euler_factor": f"1+2/(({prime}+1)*sqrt({prime}))",
                "prime": prime,
            }
        )
    return {
        "absolute_pair_mass": ("K_67=prod_(p!=67)(1+2/((p+1)sqrt(p)))<infinity"),
        "forward_inverse_absolute_masses_equal": True,
        "local_rows": local_rows,
        "primitive_scalar_uniform_cost_both_directions": "K_67",
        "primitive_squared_energy_uniform_cost_both_directions": "K_67^2",
        "rows": rows,
        "support": "u,v squarefree and coprime; hence r,s,m,n pairwise coprime",
    }


def is_squarefree(n: int) -> bool:
    validate_positive_integer(n)
    return mobius(n) != 0


def raw_primitive_support(r: int, s: int, m_value: int, n: int, d: int) -> bool:
    """The support predicate before Boolean compression."""
    for value in (r, s, m_value, n, d):
        validate_domain_integer(value)
    return (
        is_squarefree(r * m_value)
        and is_squarefree(s * n)
        and gcd(r * m_value, s * n) == 1
        and gcd(r * s * m_value * n, d) == 1
    )


def compressed_primitive_support(r: int, s: int, m_value: int, n: int, d: int) -> bool:
    """The equivalent generalized-panel predicate after compression."""
    for value in (r, s, m_value, n, d):
        validate_domain_integer(value)
    return (
        is_squarefree(r)
        and is_squarefree(s)
        and gcd(r, s) == 1
        and gcd(r * s, d) == 1
        and is_squarefree(m_value)
        and is_squarefree(n)
        and gcd(m_value, n) == 1
        and gcd(m_value * n, d * r * s) == 1
    )


def primitive_support_equivalence_panel(
    limit: int = REPLAY_SUPPORT_LIMIT,
) -> dict[str, object]:
    """Exhaustively replay the iff support reduction under a small cap."""
    validate_positive_integer(limit)
    checked = 0
    surviving = 0
    for r in range(1, limit + 1):
        for s in range(1, limit + 1):
            for m_value in range(1, limit + 1):
                for n in range(1, limit + 1):
                    for d in range(1, limit + 1):
                        raw = raw_primitive_support(r, s, m_value, n, d)
                        compressed = compressed_primitive_support(r, s, m_value, n, d)
                        if raw != compressed:
                            raise ArithmeticError(
                                "primitive support compression equivalence failed"
                            )
                        checked += 1
                        surviving += int(raw)
    return {
        "checked_quintuples": checked,
        "equivalence": True,
        "generalized_parameters": ("A=67^alpha*r, B=67^gamma*s, q=d*r*s"),
        "limit_per_variable": limit,
        "surviving_quintuples": surviving,
    }


def finite_generalized_panel_certificate() -> dict[str, object]:
    """Replay one full coefficient/height/ratio/sieve instance of (5.13)."""
    total_product = 30
    sieve = 7
    lower_height = 5
    upper_height = 20
    direct = Fraction()
    direct_terms = 0
    for u in divisors(total_product):
        v = total_product // u
        if (
            is_squarefree(u)
            and is_squarefree(v)
            and gcd(u, v) == 1
            and gcd(u * v, sieve) == 1
            and lower_height < max(u, v) <= upper_height
        ):
            direct += a(u) * a(v) * Fraction(u, v)
            direct_terms += 1

    via_generalized = Fraction()
    generalized_terms = 0
    for r in divisors(total_product):
        for s in divisors(total_product):
            if total_product % (r * s):
                continue
            inner_product = total_product // (r * s)
            for m_value in divisors(inner_product):
                n = inner_product // m_value
                if not compressed_primitive_support(r, s, m_value, n, sieve):
                    continue
                u = r * m_value
                v = s * n
                if not lower_height < max(u, v) <= upper_height:
                    continue
                via_generalized += g(r) * g(s) * m(m_value) * m(n) * Fraction(u, v)
                generalized_terms += 1
    if direct != via_generalized:
        raise ArithmeticError("finite generalized-panel identity failed")
    return {
        "cleared_common_weight": f"sqrt({total_product})",
        "direct_scaled_value": str(direct),
        "direct_terms": direct_terms,
        "generalized_scaled_value": str(via_generalized),
        "generalized_terms": generalized_terms,
        "height_interval": f"({lower_height},{upper_height}]",
        "ratio_test": "exp(log(u/v))=u/v",
        "sieve": sieve,
        "total_product": total_product,
    }


def prime_valuation(n: int, prime: int) -> int:
    validate_positive_integer(n)
    if not is_prime(prime):
        raise ValueError("valuation base must be prime")
    valuation = 0
    while n % prime == 0:
        n //= prime
        valuation += 1
    return valuation


def compatible_triple(
    alpha: int, gamma: int, r: int, s: int, d: int
) -> tuple[int, int, int]:
    """Map an admissible colored dilation to its generalized parameters."""
    for exponent in (alpha, gamma):
        if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
            raise ValueError("scale exponents must be nonnegative integers")
    for value in (r, s, d):
        validate_domain_integer(value)
        if not is_squarefree(value):
            raise ValueError("colored dilation variables must be squarefree")
    if gcd(r, s) != 1 or gcd(r * s, d) != 1:
        raise ValueError("colored dilation variables must be pairwise coprime")
    return EXCEPTIONAL_PRIME**alpha * r, EXCEPTIONAL_PRIME**gamma * s, d * r * s


def recover_compatible_triple(
    alpha: int, gamma: int, scale_a: int, scale_b: int, modulus: int
) -> tuple[int, int, int]:
    """Invert the compatible parameter map, rejecting triples outside its image."""
    for exponent in (alpha, gamma):
        if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
            raise ValueError("scale exponents must be nonnegative integers")
    for value in (scale_a, scale_b, modulus):
        validate_positive_integer(value)
    if (
        prime_valuation(scale_a, EXCEPTIONAL_PRIME) != alpha
        or prime_valuation(scale_b, EXCEPTIONAL_PRIME) != gamma
        or modulus % EXCEPTIONAL_PRIME == 0
    ):
        raise ValueError("exceptional-prime valuations are incompatible")
    r = scale_a // EXCEPTIONAL_PRIME**alpha
    s = scale_b // EXCEPTIONAL_PRIME**gamma
    if (
        not is_squarefree(r)
        or not is_squarefree(s)
        or not is_squarefree(modulus)
        or gcd(r, s) != 1
        or modulus % (r * s)
    ):
        raise ValueError("scale cores or modulus are incompatible")
    d = modulus // (r * s)
    if not is_squarefree(d) or gcd(d, r * s) != 1:
        raise ValueError("residual sieve factor is incompatible")
    return r, s, d


def compatible_triple_panel(limit: int = REPLAY_SUPPORT_LIMIT) -> dict[str, object]:
    """Replay the bijection between colored dilations and compatible triples."""
    validate_positive_integer(limit)
    rows = []
    color_count_rows = []
    for modulus in range(1, limit + 1):
        if modulus % EXCEPTIONAL_PRIME == 0 or not is_squarefree(modulus):
            continue
        omega = len(factorization(modulus))
        compatible = 0
        saturated = 0
        for r in divisors(modulus):
            for s in divisors(modulus):
                if gcd(r, s) != 1 or modulus % (r * s):
                    continue
                compatible += 1
                if r * s == modulus:
                    saturated += 1
        if compatible != 3**omega or saturated != 2**omega:
            raise ArithmeticError("compatible color count failed")
        color_count_rows.append(
            {
                "compatible_triples": compatible,
                "modulus": modulus,
                "omega": omega,
                "zero_mode_saturated_rays": saturated,
            }
        )
    for alpha in (0, 1, 2):
        seen: set[tuple[int, int, int]] = set()
        admissible = 0
        for r in range(1, limit + 1):
            for s in range(1, limit + 1):
                for d in range(1, limit + 1):
                    if (
                        not is_squarefree(r)
                        or not is_squarefree(s)
                        or not is_squarefree(d)
                        or gcd(r, s) != 1
                        or gcd(r * s, d) != 1
                    ):
                        continue
                    triple = compatible_triple(alpha, 0, r, s, d)
                    if triple in seen:
                        raise ArithmeticError(
                            "compatible parameter map is not injective"
                        )
                    seen.add(triple)
                    if recover_compatible_triple(alpha, 0, *triple) != (r, s, d):
                        raise ArithmeticError("compatible parameter inverse failed")
                    admissible += 1
        bounded_image = {triple for triple in seen if triple[2] <= limit}
        expected_image = {
            compatible_triple(
                alpha,
                0,
                r,
                s,
                modulus // (r * s),
            )
            for modulus in range(1, limit + 1)
            if modulus % EXCEPTIONAL_PRIME != 0 and is_squarefree(modulus)
            for r in divisors(modulus)
            for s in divisors(modulus)
            if gcd(r, s) == 1 and modulus % (r * s) == 0
        }
        if bounded_image != expected_image:
            raise ArithmeticError("bounded compatible image exhaustion failed")
        rows.append(
            {
                "alpha": alpha,
                "gamma": 0,
                "admissible_triples": admissible,
                "bounded_image_exhausted": True,
                "image_triples": len(seen),
            }
        )

    bit_primes = (2, 3, 5)
    generated_bits: set[tuple[int, int, int]] = set()
    generated_zero_modes: set[tuple[int, int, int]] = set()
    for colors in product((0, 1, 2, 3), repeat=len(bit_primes)):
        r = s = d = 1
        for prime, color in zip(bit_primes, colors, strict=True):
            if color == 1:
                r *= prime
            elif color == 2:
                s *= prime
            elif color == 3:
                d *= prime
        generated_bits.add((r, s, d * r * s))
        if d == 1:
            generated_zero_modes.add((r, s, r * s))
    scanned_bits = {
        (r, s, modulus)
        for r_bits in product((0, 1), repeat=len(bit_primes))
        for s_bits in product((0, 1), repeat=len(bit_primes))
        for q_bits in product((0, 1), repeat=len(bit_primes))
        for r in (
            prod(prime for prime, bit in zip(bit_primes, r_bits, strict=True) if bit),
        )
        for s in (
            prod(prime for prime, bit in zip(bit_primes, s_bits, strict=True) if bit),
        )
        for modulus in (
            prod(prime for prime, bit in zip(bit_primes, q_bits, strict=True) if bit),
        )
        if gcd(r, s) == 1 and modulus % (r * s) == 0
    }
    if generated_bits != scanned_bits:
        raise ArithmeticError("independent compatible bit-cube scan failed")
    if len(generated_bits) != 4 ** len(bit_primes):
        raise ArithmeticError("compatible bit-cube cardinality failed")
    if len(generated_zero_modes) != 3 ** len(bit_primes):
        raise ArithmeticError("zero-mode bit-cube cardinality failed")
    return {
        "bijection": True,
        "bit_cube_exhaustion": {
            "compatible_triples": len(generated_bits),
            "independent_target_scan_equal": True,
            "primes": list(bit_primes),
            "zero_mode_triples": len(generated_zero_modes),
        },
        "color_count_rows": color_count_rows,
        "image_conditions": (
            "v_67(A)=alpha, v_67(B)=gamma; r=A/67^alpha and "
            "s=B/67^gamma squarefree coprime; q squarefree 67-free; r*s|q"
        ),
        "independent_channels": [[0, 0], [1, 0], [2, 0]],
        "limit_per_variable": limit,
        "rows": rows,
        "unique_inverse": "d=q/(r*s)",
    }


def abstract_ray_d_energy(
    core: int, dilation_limit: int, values: dict[int, Fraction]
) -> Fraction:
    """Harmonic d-energy for an abstract one-interval compatible-ray array."""
    validate_domain_integer(core)
    validate_positive_integer(dilation_limit)
    if not is_squarefree(core):
        raise ValueError("ray core must be squarefree")
    return sum(
        (
            values.get(core * d, Fraction(0)) ** 2 / d
            for d in range(1, dilation_limit + 1)
            if d % EXCEPTIONAL_PRIME != 0 and is_squarefree(d) and gcd(d, core) == 1
        ),
        Fraction(0),
    )


def abstract_q_energy(
    modulus_limit: int,
    values: dict[int, Fraction],
    *,
    required_divisor: int = 1,
) -> Fraction:
    """Harmonic full-q or restricted-multiple-ray energy."""
    validate_positive_integer(modulus_limit)
    validate_domain_integer(required_divisor)
    return sum(
        (
            values.get(modulus, Fraction(0)) ** 2 / modulus
            for modulus in range(1, modulus_limit + 1)
            if modulus % EXCEPTIONAL_PRIME != 0
            and is_squarefree(modulus)
            and modulus % required_divisor == 0
        ),
        Fraction(0),
    )


def gate_hierarchy_panel() -> dict[str, object]:
    """Give exact positive-norm witnesses for the gate hierarchy."""
    core = 6
    dilation_limit = 5
    modulus_limit = core * dilation_limit
    sharp_values = {6: Fraction(1), 30: Fraction(2)}
    compatible_ray_energy = abstract_ray_d_energy(core, dilation_limit, sharp_values)
    restricted_full_q_energy = abstract_q_energy(
        modulus_limit, sharp_values, required_divisor=core
    )
    full_q_energy = abstract_q_energy(modulus_limit, sharp_values)
    if (
        compatible_ray_energy != Fraction(9, 5)
        or restricted_full_q_energy != Fraction(3, 10)
        or full_q_energy != restricted_full_q_energy
        or compatible_ray_energy != core * restricted_full_q_energy
    ):
        raise ArithmeticError("compatible/full-q conversion failed")

    off_ray_values = {5: Fraction(1)}
    off_ray_d_energy = abstract_ray_d_energy(core, dilation_limit, off_ray_values)
    off_ray_restricted_energy = abstract_q_energy(
        modulus_limit, off_ray_values, required_divisor=core
    )
    off_ray_full_q_energy = abstract_q_energy(modulus_limit, off_ray_values)
    if (
        off_ray_d_energy
        or off_ray_restricted_energy
        or off_ray_full_q_energy != Fraction(1, 5)
    ):
        raise ArithmeticError("off-ray blindness witness failed")

    hidden_ray_rows = []
    for prime in REPLAY_PRIMES:
        weight_squared = g(prime) * g(prime) / prime
        ray_energy = Fraction((prime + 1) ** 2)
        collective_term_squared = weight_squared * ray_energy
        if collective_term_squared != Fraction(1, prime):
            raise ArithmeticError("collective hiding witness failed")
        hidden_ray_rows.append(
            {
                "amplitude": prime + 1,
                "collective_weighted_contribution_squared": str(
                    collective_term_squared
                ),
                "prime_core": prime,
                "ray_energy": str(ray_energy),
                "weight_kappa_p_squared": str(weight_squared),
            }
        )

    return {
        "collective_gate_is_weaker_than_uniform_ray_control": {
            "mechanism": (
                "put norm p+1 on one remote prime-p ray; "
                "its weighted contribution squared is 1/p"
            ),
            "rows": hidden_ray_rows,
        },
        "exact_conversion_witness": {
            "compatible_ray_energy": str(compatible_ray_energy),
            "core_rs": core,
            "dilation_limit": dilation_limit,
            "full_q_energy": str(full_q_energy),
            "modulus_limit": modulus_limit,
            "restricted_full_q_energy": str(restricted_full_q_energy),
            "ratio": str(compatible_ray_energy / restricted_full_q_energy),
            "values": {str(key): str(value) for key, value in sharp_values.items()},
        },
        "formal_implications": [
            (
                "RAYPRIMCAR -> COLLPRIMCAR -> auxiliary rho-sieved energy "
                "-> d=1 zero-mode bound"
            ),
            (
                "GENPRIMCAR -> COLLPRIMCAR -> auxiliary rho-sieved energy "
                "-> d=1 zero-mode bound under native height support"
            ),
        ],
        "off_ray_blindness_witness": {
            "compatible_d_energy": str(off_ray_d_energy),
            "full_q_energy": str(off_ray_full_q_energy),
            "restricted_ray_q_energy": str(off_ray_restricted_energy),
            "ray_core": core,
            "values": {str(key): str(value) for key, value in off_ray_values.items()},
        },
        "scope": "abstract positive-norm arrays, not realized arithmetic P^0 panels",
        "ray_and_full_q_gates_formally_comparable": False,
    }


def fixed_q_coloring_panel(witness_scale: int = 3) -> dict[str, object]:
    """Replay fixed-core equal weights and coherent pre-norm cancellation."""
    validate_positive_integer(witness_scale)
    sweep_rows = []
    for modulus in (1, 2, 6, 30):
        color_rows = []
        cleared_pair_sum = Fraction(0)
        scalar_color_sum = Fraction(0)
        for r in divisors(modulus):
            s = modulus // r
            common_cleared_weight = g(r) * g(s)
            if common_cleared_weight != g(modulus):
                raise ArithmeticError("saturated colors do not have equal weight")
            scalar_value = Fraction(r + 2 * s)
            cleared_pair_sum += common_cleared_weight * scalar_value
            scalar_color_sum += scalar_value
            color_rows.append(
                {
                    "cleared_weight": str(common_cleared_weight),
                    "r": r,
                    "s": s,
                }
            )
        if cleared_pair_sum != g(modulus) * scalar_color_sum:
            raise ArithmeticError("fixed-q coherent coloring compression failed")
        omega = len(factorization(modulus))
        if len(color_rows) != 2**omega:
            raise ArithmeticError("saturated color count failed")
        sweep_rows.append(
            {
                "cleared_common_weight": str(g(modulus)),
                "color_count": len(color_rows),
                "colors": color_rows,
                "compression_identity": True,
                "modulus": modulus,
                "omega": omega,
                "squared_actual_weight": str(g(modulus) ** 2 / modulus),
            }
        )

    modulus = 6
    scale = Fraction(witness_scale)
    vectors = {
        1: (scale,),
        2: (-scale + Fraction(1, 2),),
        3: (-scale + Fraction(1, 2),),
        6: (scale,),
    }
    color_vector = tuple(
        sum(vectors[r][coordinate] for r in divisors(modulus))
        for coordinate in range(1)
    )
    ray_energies = {
        r: sum(coordinate * coordinate for coordinate in vector)
        for r, vector in vectors.items()
    }
    color_energy = sum(coordinate * coordinate for coordinate in color_vector)
    raywise_l1_norm = 4 * scale - 1
    squared_outer_coefficient = g(modulus) ** 2 / modulus
    if (
        color_vector != (Fraction(1),)
        or color_energy != 1
        or max(ray_energies.values()) != scale**2
        or squared_outer_coefficient != Fraction(1, 864)
    ):
        raise ArithmeticError("coherent color cancellation witness failed")
    return {
        "equal_weight_scope": (
            "every fixed d and core u=rs; ordered colors at fixed alpha,d,u"
        ),
        "euler_cost": (
            "J_67=prod_(p!=67)(1+1/((p+1)*sqrt(p)))<infinity; "
            "sharp weighted-Hilbert energy cost"
        ),
        "formal_gate": (
            "AUXCOLORPRIMCAR: sum_(d<=D sf) d^-1 sum_((u,d)=1 sf) "
            "g(u)/sqrt(u) sum_I |sum_(r|u) V_(d;r,u/r)(I)|^2 "
            "<<_epsilon (2DH)^epsilon"
        ),
        "d_one_specialization": ("COLORPRIMCAR: the AUXCOLORPRIMCAR gate at D=1"),
        "formal_relations": [
            "RAYPRIMCAR -> AUXCOLORPRIMCAR -> auxiliary rho-sieved energy -> zero mode",
            "COLLPRIMCAR and AUXCOLORPRIMCAR are positive-norm incomparable",
            "GENPRIMCAR and AUXCOLORPRIMCAR are positive-norm incomparable",
        ],
        "ray_to_color_euler_cost": (
            "prod_(p!=67)(1+4*p^eta/((p+1)*sqrt(p)))<infinity exactly for eta<1/2"
        ),
        "remote_ray_reverse_witness": {
            "prime": 11,
            "ray_norm": 12,
            "raywise_weighted_l1_contribution_squared": "1/11",
            "weighted_color_energy": "12/sqrt(11)",
            "weighted_color_energy_squared": "144/11",
        },
        "sweep_rows": sweep_rows,
        "synthetic_cancellation_witness": {
            "auxcolor_quadratic_contribution": "1/(12*sqrt(6))",
            "zero_mode_coefficient_squared_times_color_energy": str(
                squared_outer_coefficient * color_energy
            ),
            "color_energy": str(color_energy),
            "color_vector": [str(coordinate) for coordinate in color_vector],
            "largest_ray_energy": str(max(ray_energies.values())),
            "outer_coefficient": "1/(12*sqrt(6))",
            "ray_energies": {
                str(r): str(energy) for r, energy in sorted(ray_energies.items())
            },
            "raywise_l1_norm": str(raywise_l1_norm),
            "scope": "abstract vectors, not realized arithmetic P^0 panels",
            "squared_outer_coefficient": str(squared_outer_coefficient),
            "zero_mode_largest_ray_contribution_energy": str(
                squared_outer_coefficient * max(ray_energies.values())
            ),
            "witness_scale": witness_scale,
        },
        "uniform_per_q_alternative": (
            "||C_q||^2 <<_eta (2Hq)^eta implies the zero mode directly "
            "by Minkowski for eta<1; it implies quadratic COLORPRIMCAR at "
            "the same eta only for eta<1/2, and as an all-epsilon family "
            "is stronger after exponent renaming"
        ),
    }


def coherent_core_gram_panel(limit: int = 30) -> dict[str, object]:
    """Replay the direct color bijection and its Boolean overlap Gram."""
    validate_positive_integer(limit)
    pair_bijection_checks = 0
    for d in (1, 5):
        for core in (1, 2, 6):
            if gcd(d, core) != 1:
                continue
            for left in range(1, limit + 1):
                if mobius(left) == 0 or gcd(left, 67 * d) != 1:
                    continue
                for right in range(1, limit + 1):
                    if (
                        mobius(right) == 0
                        or gcd(right, 67 * d) != 1
                        or gcd(left, right) != 1
                        or left * right % core != 0
                    ):
                        continue
                    r = gcd(left, core)
                    s = core // r
                    m_value = left // r
                    n_value = right // s
                    if (
                        r * s != core
                        or gcd(r, s) != 1
                        or gcd(m_value * n_value, d * core) != 1
                        or gcd(m_value, n_value) != 1
                        or m_value * n_value * core != left * right
                        or mobius(m_value) * mobius(n_value)
                        != mobius(core) * mobius(left) * mobius(right)
                    ):
                        raise ArithmeticError("coherent-core pair bijection failed")
                    pair_bijection_checks += 1

    primes = (2, 3, 5)
    configuration_count = 2 ** len(primes)
    gram_pair_checks = 0
    feature_monomial_checksum = 0
    for left_mask in range(configuration_count):
        for right_mask in range(configuration_count):
            intersection = left_mask & right_mask
            feature_masks = tuple(
                mask for mask in range(configuration_count) if mask & ~intersection == 0
            )
            expected_count = 2 ** intersection.bit_count()
            if len(feature_masks) != expected_count:
                raise ArithmeticError("Boolean overlap Gram expansion failed")
            feature_monomial_checksum += len(feature_masks)
            gram_pair_checks += 1
    if gram_pair_checks != 64 or feature_monomial_checksum != 125:
        raise ArithmeticError("Boolean overlap Gram checksum failed")

    shell_values = {
        mask: Fraction((-1) ** mask.bit_count() * (mask + 1))
        for mask in range(configuration_count)
    }
    upper_zeta = {
        divisor_mask: sum(
            (
                shell_values[shell_mask]
                for shell_mask in range(configuration_count)
                if divisor_mask & ~shell_mask == 0
            ),
            Fraction(),
        )
        for divisor_mask in range(configuration_count)
    }
    recovered_shells = {
        shell_mask: sum(
            (
                (-1) ** ((multiple_mask ^ shell_mask).bit_count())
                * upper_zeta[multiple_mask]
                for multiple_mask in range(configuration_count)
                if shell_mask & ~multiple_mask == 0
            ),
            Fraction(),
        )
        for shell_mask in range(configuration_count)
    }
    if recovered_shells != shell_values:
        raise ArithmeticError("upper-divisor zeta inversion failed")

    def polynomial_add(
        left: tuple[Fraction, ...], right: tuple[Fraction, ...]
    ) -> tuple[Fraction, ...]:
        length = max(len(left), len(right))
        return tuple(
            (left[index] if index < len(left) else Fraction())
            + (right[index] if index < len(right) else Fraction())
            for index in range(length)
        )

    def polynomial_multiply(
        left: tuple[Fraction, ...], right: tuple[Fraction, ...]
    ) -> tuple[Fraction, ...]:
        result = [Fraction()] * (len(left) + len(right) - 1)
        for left_index, left_value in enumerate(left):
            for right_index, right_value in enumerate(right):
                result[left_index + right_index] += left_value * right_value
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return tuple(result)

    one = (Fraction(1),)
    zero = (Fraction(),)
    root_c = (Fraction(), Fraction(1))
    local_left = ((one, zero), (one, root_c))
    local_right = ((one, one), (zero, root_c))
    cholesky_product = tuple(
        tuple(
            polynomial_add(
                polynomial_multiply(local_left[row][0], local_right[0][column]),
                polynomial_multiply(local_left[row][1], local_right[1][column]),
            )
            for column in range(2)
        )
        for row in range(2)
    )
    expected_kernel = ((one, one), (one, (Fraction(1), Fraction(), Fraction(1))))
    trace_polynomial = (Fraction(2), Fraction(), Fraction(1))
    determinant_polynomial = (Fraction(), Fraction(), Fraction(1))
    discriminant_polynomial = polynomial_add(
        polynomial_multiply(trace_polynomial, trace_polynomial),
        tuple(-4 * coefficient for coefficient in determinant_polynomial),
    )
    if cholesky_product != expected_kernel or discriminant_polynomial != (
        Fraction(4),
        Fraction(),
        Fraction(),
        Fraction(),
        Fraction(1),
    ):
        raise ArithmeticError("formal local Gram spectrum replay failed")
    return {
        "coefficient_normalization_checks": pair_bijection_checks,
        "configuration_count": configuration_count,
        "direct_pair_bijection_checks": pair_bijection_checks,
        "feature_monomial_checksum": feature_monomial_checksum,
        "gram_pair_checks": gram_pair_checks,
        "kernel": (
            "K(N,M)=prod_(p|gcd(N,M))(1+sqrt(p)/(p+1)); "
            "local block [[1,1],[1,1+c_p]] has determinant c_p>0"
        ),
        "primes": list(primes),
        "scope": "exact finite combinatorial replay; no AUXCOLORPRIMCAR estimate",
        "spectral_identity_checks": {
            "cholesky_entries": 4,
            "characteristic_discriminant": "4+c^2",
            "determinant": "c",
            "trace": "2+c",
        },
        "upper_zeta_inversion_checks": configuration_count,
    }


def colored_configurations(number_of_primes: int) -> tuple[tuple[int, ...], ...]:
    validate_positive_integer(number_of_primes)
    return tuple(product((0, 1, 2), repeat=number_of_primes))


def colored_leq(left: tuple[int, ...], right: tuple[int, ...]) -> bool:
    if len(left) != len(right):
        raise ValueError("colored configurations must have the same rank")
    return all(
        item_left == 0 or item_left == item_right
        for item_left, item_right in zip(left, right, strict=True)
    )


def is_downward_closed(
    chosen: frozenset[tuple[int, ...]], configurations: tuple[tuple[int, ...], ...]
) -> bool:
    return all(
        lower in chosen
        for upper in chosen
        for lower in configurations
        if colored_leq(lower, upper)
    )


def projection_intertwining_holds(
    chosen: frozenset[tuple[int, ...]], configurations: tuple[tuple[int, ...], ...]
) -> bool:
    """Support test for P_A T = P_A T P_A (and likewise for T inverse)."""
    return all(
        (upper in chosen and colored_leq(lower, upper))
        == (upper in chosen and lower in chosen and colored_leq(lower, upper))
        for upper in chosen
        for lower in configurations
    )


def colored_cube_panel(number_of_primes: int = 2) -> dict[str, object]:
    """Exhaustively replay the hereditary projection criterion at rank two."""
    configurations = colored_configurations(number_of_primes)
    downward_count = 0
    for mask in range(1 << len(configurations)):
        chosen = frozenset(
            configuration
            for index, configuration in enumerate(configurations)
            if mask & (1 << index)
        )
        downward = is_downward_closed(chosen, configurations)
        intertwines = projection_intertwining_holds(chosen, configurations)
        if downward != intertwines:
            raise ArithmeticError("colored hereditary criterion failed")
        downward_count += int(downward)
    local_rows = []
    for prime in REPLAY_PRIMES:
        t_squared = Fraction(1, prime * (prime + 1) ** 2)
        gram_trace = 2 + 2 * t_squared
        gram_determinant = Fraction(1)
        discriminant = gram_trace**2 - 4 * gram_determinant
        expected_discriminant = 4 * t_squared * (2 + t_squared)
        if discriminant != expected_discriminant:
            raise ArithmeticError("local colored shear certificate failed")
        local_rows.append(
            {
                "colored_antisymmetric_singular_value": "1",
                "local_norm": "(sqrt(4+2*t_p^2)+sqrt(2)*t_p)/2",
                "prime": prime,
                "two_dimensional_gram_determinant": str(gram_determinant),
                "two_dimensional_gram_discriminant": str(discriminant),
                "two_dimensional_gram_trace": str(gram_trace),
                "t_p_squared": str(t_squared),
            }
        )
    return {
        "checked_coordinate_projections": 1 << len(configurations),
        "configuration_count": len(configurations),
        "downward_closed_projection_count": downward_count,
        "forward_inverse_norms_equal": True,
        "hereditary_criterion": "P_A*T=P_A*T*P_A iff A is downward closed",
        "local_rows": local_rows,
        "number_of_primes": number_of_primes,
    }


def harmonic_dilation_panel(
    squarefree_dilation: int = 6, limit: int = 120
) -> dict[str, object]:
    """Replay ||D_R||=R^(w/2) on finite exact sample vectors."""
    validate_domain_integer(squarefree_dilation)
    validate_positive_integer(limit)
    if not is_squarefree(squarefree_dilation):
        raise ValueError("dilation must be squarefree")
    rows = []
    for weight in (0, 1, 2):
        left = Fraction()
        right_base = Fraction()
        checked = 0
        for d in range(1, limit // squarefree_dilation + 1):
            if (
                d % EXCEPTIONAL_PRIME == 0
                or not is_squarefree(d)
                or gcd(d, squarefree_dilation) != 1
            ):
                continue
            q = squarefree_dilation * d
            value = Fraction((q * q + 3 * q + 1) % 17 - 8)
            left += value * value / d**weight
            checked += 1
        for q in range(1, limit + 1):
            if (
                q % squarefree_dilation
                or q % EXCEPTIONAL_PRIME == 0
                or not is_squarefree(q)
                or gcd(q // squarefree_dilation, squarefree_dilation) != 1
            ):
                continue
            value = Fraction((q * q + 3 * q + 1) % 17 - 8)
            right_base += value * value / q**weight
        if not right_base or left != squarefree_dilation**weight * right_base:
            raise ArithmeticError("harmonic dilation norm identity failed")
        rows.append(
            {
                "checked_coordinates": checked,
                "dilation_norm_squared": str(Fraction(squarefree_dilation**weight)),
                "left_norm_squared": str(left),
                "right_restricted_norm_squared": str(right_base),
                "weight": weight,
            }
        )
    height_checks = 0
    for r in range(1, limit + 1):
        if r % EXCEPTIONAL_PRIME == 0 or not is_squarefree(r):
            continue
        if g(r) > Fraction(1, r):
            raise ArithmeticError("critical harmonic height majorant failed")
        height_checks += 1
    return {
        "absolute_euler_factor": "1+2*p^((w-1)/2)/(p+1)",
        "global_absolute_convergence": "exactly w<1",
        "height_majorant": "g(r)<=1/r for squarefree r",
        "height_majorant_checks": height_checks,
        "harmonic_weight_cost": "O(log(H)^2) in norm; O(log(H)^4) in energy",
        "sharpness_witness": ("A=delta_R gives ||D_R A||_w^2 / ||A||_w^2=R^w"),
        "rows": rows,
        "squarefree_dilation": squarefree_dilation,
        "weight_one_is_critical": True,
    }


def convergence_majorant_panel() -> list[dict[str, object]]:
    """Record exact rational margins behind the theta=1/2 local bounds."""
    rows = []
    for prime in REPLAY_PRIMES:
        g_square_margin = 9 * prime - 16
        h_square_margin = Fraction(prime * prime, 4) + 1
        if g_square_margin < 0 or h_square_margin <= 0:
            raise ArithmeticError("local square-root majorant failed")
        rows.append(
            {
                "g_bound": "u_g(p)<=4/p^(3/2)",
                "g_bound_square_margin_9p_minus_16": g_square_margin,
                "h_bound": "u_h(p)<=2/p^(3/2)",
                "h_bound_square_margin_p2_over_4_plus_1": str(h_square_margin),
                "prime": prime,
            }
        )
    return rows


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_predecessor_blobs()
    check_scope_markers()
    local_panels = [local_coefficient_panel(prime) for prime in REPLAY_PRIMES]
    return {
        "exact_convolution": {
            "a": "a(n)=mu(n)rho(n)",
            "domain": "N_67={n>=1:(n,67)=1}",
            "full_integer_extension": "extend m,a,g,h by zero on 67|n",
            "forward_identity": "m*g=a",
            "g_local": "g(p^k)=1/(p+1) for p!=67 and k>=1",
            "global_replay": global_identity_panel(),
            "h_local": "h(p^k)=-(1-rho_p)rho_p^(k-1) for p!=67 and k>=1",
            "inverse_identity": "a*h=m",
            "local_panels": local_panels,
            "m": "m(n)=mu(n)",
            "operator_inverse_identity": "g*h=delta",
        },
        "finite_operator_replay": finite_operator_certificate(),
        "half_weighted_pair_transfer": {
            "coefficient_identity": "c_rho=c_0*(g/sqrt(.))",
            "finite_test_identity": (
                "B_rho(F)=sum_(r,s) g(r)g(s)/sqrt(rs) B_0((m,n)->F(rm,sn))"
            ),
            "inverse_coefficient_identity": "c_0=c_rho*(h/sqrt(.))",
            "inverse_squared_energy_cost": "L_h(1/2)^4",
            "pair_panel": pair_coefficient_panel(),
            "primitive_boolean_compression": primitive_boolean_pair_panel(),
            "primitive_support_equivalence": primitive_support_equivalence_panel(),
            "finite_generalized_panel": finite_generalized_panel_certificate(),
            "scalar_uniform_bound_cost": "L_g(1/2)^2",
            "squared_energy_uniform_bound_cost": "L_g(1/2)^4",
            "total_forward_l1_weight": "L_g(1/2)^2",
            "uniformity_is_only_a_stronger_sufficient_corollary": True,
            "vector_minkowski": (
                "||Lambda_rho(F_j)||_l2(w)<=sum_(r,s)|gamma(r)gamma(s)|"
                "||Lambda_0(D_(r,s)F_j)||_l2(w)"
            ),
            "weighted_vector_sufficient_gate": (
                "sum_(r,s)|gamma(r)gamma(s)|E_0(r,s)^(1/2) << target^(1/2)"
            ),
        },
        "colored_boolean_geometry": colored_cube_panel(),
        "compatible_scale_geometry": {
            "coherent_core_gram": coherent_core_gram_panel(),
            "fixed_q_coloring": fixed_q_coloring_panel(),
            "gate_hierarchy": gate_hierarchy_panel(),
            "triple_bijection": compatible_triple_panel(),
        },
        "harmonic_sieve_dilation": harmonic_dilation_panel(),
        "resource_caps": {
            "global_identity_limit": REPLAY_GLOBAL_LIMIT,
            "local_exponent_limit": REPLAY_MAX_EXPONENT,
            "matrix_limit": REPLAY_MATRIX_LIMIT,
            "pair_rows": 5,
            "primes": list(REPLAY_PRIMES),
            "support_limit_per_variable": REPLAY_SUPPORT_LIMIT,
            "support_quintuples": REPLAY_SUPPORT_LIMIT**5,
            "summatory_limit": REPLAY_SUMMATORY_LIMIT,
            "zeta_zeros": 0,
        },
        "scope_firewall": {
            "actual_zero_mode_has_native_sieve_average": False,
            "a_or_m_is_a_vector_in_weighted_l2": False,
            "arbitrary_cross_coprimality_obstruction_remaining": False,
            "collprimcar_estimate_proved": False,
            "auxcolorprimcar_estimate_proved": False,
            "colorprimcar_estimate_proved": False,
            "compatible_scale_bijection_proved": True,
            "coprimality_preserved_in_generalized_panel": True,
            "dyadic_endpoint_structure_preserved": False,
            "fixed_ratio_band_is_hereditary": False,
            "fixed_core_equal_color_weight_extends_to_each_fixed_positive_d": True,
            "fixed_total_modulus_has_d_independent_color_weight": False,
            "generalized_primitive_carleson_estimate_proved": False,
            "genprimcar_and_rayprimcar_formally_equivalent": False,
            "harmonic_dilation_has_height_independent_absolute_cost": False,
            "harmonic_dilation_tax_is_polylog_under_native_height_cutoff": True,
            "primcar_estimate_proved": False,
            "primls_proved": False,
            "ray_gen_nonimplication_scope": "abstract positive-norm algebra only",
            "rayprimcar_estimate_proved": False,
            "ratio_kernel_preserved_in_generalized_panel": True,
            "rh_or_grh_proved": False,
            "sharp_finite_height_blocks_preserved": False,
            "undilated_primcar_is_dilation_closed": False,
            "uniform_dilation_required": False,
            "uniform_dilation_sufficient": True,
            "uniform_induced_dilation_estimate_proved": False,
            "weighted_induced_dilation_estimate_proved": False,
        },
        "source_contract": {
            "commit": PREDECESSOR_COMMIT,
            "git_blobs": PREDECESSOR_BLOBS,
            "imported_object": (
                "primitive-pair harmonic-incidence packet and its rho-tilted zero mode"
            ),
        },
        "summatory_seminorm_transfer": {
            "exceptional_prime_replay": exceptional_prime_transfer_panel(),
            "forward_bound": "S_theta(a)<=L_g(theta)S_theta(m)",
            "inverse_bound": "S_theta(m)<=L_h(theta)S_theta(a)",
            "L_g_theta": ("prod_(p!=67)(1+1/((p+1)(p^theta-1)))<infinity"),
            "L_h_theta": (
                "prod_(p!=67)(1+p^(-theta)/((p+1)(1-rho_p*p^(-theta))))<infinity"
            ),
            "mertens_exponents_coincide": True,
            "rh_equivalent_family": (
                "for every epsilon>0, S_(1/2+epsilon)(a)<infinity"
            ),
            "rh_equivalence_status": "standard imported equivalence; not proved here",
            "summatory_replay": summatory_transfer_panel(),
            "theta_domain": "theta>0",
            "theta_zero_excluded": "L_g(0)=L_h(0)=infinity",
        },
        "weighted_l2_isomorphism": {
            "forward": "T_g:f->f*g",
            "forward_young_bound": "||T_g f||_(2,-1)<=L_g(1/2)||f||_(2,-1)",
            "inverse": "T_h:f->f*h",
            "inverse_young_bound": "||T_h f||_(2,-1)<=L_h(1/2)||f||_(2,-1)",
            "L_g_half": ("prod_(p!=67)(1+1/((p+1)(sqrt(p)-1)))<infinity"),
            "L_h_half": ("prod_(p!=67)(1+1/(sqrt(p)(p+1-sqrt(p))))<infinity"),
            "majorant_panels": convergence_majorant_panel(),
            "space": "ell^2(N_67,n^-1)",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
