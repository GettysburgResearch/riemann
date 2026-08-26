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
from math import gcd
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
            "coprimality_preserved_in_generalized_panel": True,
            "dyadic_endpoint_structure_preserved": False,
            "fixed_ratio_band_is_hereditary": False,
            "generalized_primitive_carleson_estimate_proved": False,
            "harmonic_dilation_has_height_independent_absolute_cost": False,
            "harmonic_dilation_tax_is_polylog_under_native_height_cutoff": True,
            "primcar_estimate_proved": False,
            "primls_proved": False,
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
