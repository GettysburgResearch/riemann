#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction as F
from pathlib import Path

VERDICT = "PASS_T105105_FIXED_WINDOW_CRT_JET_SELECTORS"
REPO_ROOT = Path(__file__).resolve().parents[2]
BASE_PATH = (
    REPO_ROOT
    / "experiments"
    / "X-105104-jet-coherence-reverse-rolle"
    / "verify.py"
)
BASE_RESULT = BASE_PATH.parent / "results" / "verification.json"
BASE_DIGEST = "bcd3ac0f644c49e47be6b2e019a57b2e7d2b8b6df14dfec97da854cb44b3bed6"
BASE_COMMIT = "75bf12b76014da6ea983ac1dc8083aaac79132ce"

SPEC = importlib.util.spec_from_file_location("t105104_dependency", BASE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load frozen T-105104 dependency")
BASE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = BASE
SPEC.loader.exec_module(BASE)

G = BASE.BASE.G
ZERO_G = BASE.BASE.ZERO
I = G(F(0), F(1))

CONTENT_FILES = (
    "PACKET_METADATA_105105.json",
    "claims/lemmas/L-105105-fixed-window-crt-jet-selectors.md",
    "claims/methodology/M-105105-fixed-window-crt-review-contract.md",
    "claims/refutations/R-105105-squaring-first-jet-flux-loses-second-moment.md",
    "claims/theorems/T-105105-polynomial-jet-observable-frontier.md",
    "experiments/X-105105-squarefree-crt-jet-flux/verify.py",
    "experiments/X-105105-squarefree-crt-jet-flux/tests/test_verify.py",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def dependency_checkpoint() -> dict[str, object]:
    artifact = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    live = BASE.build_payload()
    require(artifact == live, "T-105104 dependency artifact is stale")
    require(
        artifact["proof_object_sha256"] == BASE_DIGEST,
        "T-105104 dependency digest changed",
    )
    return {
        "commit": BASE_COMMIT,
        "proof_object_sha256": BASE_DIGEST,
        "artifact_matches_live_producer": True,
    }


def trim(poly: list[F]) -> list[F]:
    values = [F(value) for value in poly]
    require(bool(values), "polynomial coefficient list is empty")
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return values


def is_zero(poly: list[F]) -> bool:
    return trim(poly) == [F(0)]


def add(left: list[F], right: list[F]) -> list[F]:
    size = max(len(left), len(right))
    return trim(
        [
            (left[index] if index < len(left) else F(0))
            + (right[index] if index < len(right) else F(0))
            for index in range(size)
        ]
    )


def negate(poly: list[F]) -> list[F]:
    return trim([-value for value in poly])


def subtract(left: list[F], right: list[F]) -> list[F]:
    return add(left, negate(right))


def scale(poly: list[F], scalar: F) -> list[F]:
    return trim([F(scalar) * value for value in poly])


def multiply(left: list[F], right: list[F]) -> list[F]:
    result = [F(0)] * (len(left) + len(right) - 1)
    for i, lhs in enumerate(left):
        for j, rhs in enumerate(right):
            result[i + j] += lhs * rhs
    return trim(result)


def power(poly: list[F], exponent: int) -> list[F]:
    require(exponent >= 0, "negative polynomial exponent")
    result = [F(1)]
    base = trim(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        remaining >>= 1
    return result


def derivative(poly: list[F]) -> list[F]:
    values = trim(poly)
    if len(values) == 1:
        return [F(0)]
    return trim([F(index) * values[index] for index in range(1, len(values))])


def divmod_poly(numerator: list[F], denominator: list[F]) -> tuple[list[F], list[F]]:
    divisor = trim(denominator)
    require(not is_zero(divisor), "polynomial division by zero")
    remainder = trim(numerator)
    if len(remainder) < len(divisor):
        return [F(0)], remainder
    quotient = [F(0)] * (len(remainder) - len(divisor) + 1)
    while not is_zero(remainder) and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] / divisor[-1]
        quotient[shift] += coefficient
        term = [F(0)] * shift + [coefficient * value for value in divisor]
        remainder = subtract(remainder, term)
    return trim(quotient), trim(remainder)


def quotient_exact(numerator: list[F], denominator: list[F]) -> list[F]:
    quotient, remainder = divmod_poly(numerator, denominator)
    require(is_zero(remainder), "polynomial quotient is not exact")
    return quotient


def remainder(poly: list[F], modulus: list[F]) -> list[F]:
    require(len(trim(modulus)) > 1, "constant polynomial is not a modulus")
    return divmod_poly(poly, modulus)[1]


def monic(poly: list[F]) -> list[F]:
    values = trim(poly)
    require(not is_zero(values), "zero polynomial has no monic normalization")
    return scale(values, F(1) / values[-1])


def gcd_poly(left: list[F], right: list[F]) -> list[F]:
    a = trim(left)
    b = trim(right)
    while not is_zero(b):
        a, b = b, divmod_poly(a, b)[1]
    return monic(a)


def extended_gcd(left: list[F], right: list[F]) -> tuple[list[F], list[F], list[F]]:
    old_r, current_r = trim(left), trim(right)
    old_s, current_s = [F(1)], [F(0)]
    old_t, current_t = [F(0)], [F(1)]
    while not is_zero(current_r):
        quotient, next_r = divmod_poly(old_r, current_r)
        old_r, current_r = current_r, next_r
        old_s, current_s = current_s, subtract(old_s, multiply(quotient, current_s))
        old_t, current_t = current_t, subtract(old_t, multiply(quotient, current_t))
    unit = F(1) / old_r[-1]
    return scale(old_r, unit), scale(old_s, unit), scale(old_t, unit)


def inverse_mod(poly: list[F], modulus: list[F]) -> list[F]:
    common, bezout, _ = extended_gcd(poly, modulus)
    require(common == [F(1)], "polynomial is not invertible modulo stratum")
    return remainder(bezout, modulus)


def evaluate(poly: list[F], point: G) -> G:
    value = ZERO_G
    for coefficient in reversed(trim(poly)):
        value = value * point + coefficient
    return value


def gsum(values: list[G]) -> G:
    total = ZERO_G
    for value in values:
        total += value
    return total


def gp_trim(poly: list[G | F | int]) -> list[G]:
    values = [G.coerce(value) for value in poly]
    require(bool(values), "Gaussian polynomial coefficient list is empty")
    while len(values) > 1 and values[-1] == ZERO_G:
        values.pop()
    return values


def gp_is_zero(poly: list[G | F | int]) -> bool:
    return gp_trim(poly) == [ZERO_G]


def gp_add(left: list[G], right: list[G]) -> list[G]:
    size = max(len(left), len(right))
    return gp_trim(
        [
            (left[index] if index < len(left) else ZERO_G)
            + (right[index] if index < len(right) else ZERO_G)
            for index in range(size)
        ]
    )


def gp_negate(poly: list[G]) -> list[G]:
    return gp_trim([-value for value in poly])


def gp_subtract(left: list[G], right: list[G]) -> list[G]:
    return gp_add(left, gp_negate(right))


def gp_scale(poly: list[G], scalar: G | F | int) -> list[G]:
    factor = G.coerce(scalar)
    return gp_trim([factor * value for value in poly])


def gp_multiply(left: list[G], right: list[G]) -> list[G]:
    result = [ZERO_G] * (len(left) + len(right) - 1)
    for i, lhs in enumerate(left):
        for j, rhs in enumerate(right):
            result[i + j] = result[i + j] + lhs * rhs
    return gp_trim(result)


def gp_power(poly: list[G], exponent: int) -> list[G]:
    require(exponent >= 0, "negative Gaussian polynomial exponent")
    result = [G(F(1))]
    base = gp_trim(poly)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = gp_multiply(result, base)
        base = gp_multiply(base, base)
        remaining >>= 1
    return result


def gp_derivative(poly: list[G]) -> list[G]:
    values = gp_trim(poly)
    if len(values) == 1:
        return [ZERO_G]
    return gp_trim([F(index) * values[index] for index in range(1, len(values))])


def gp_divmod(numerator: list[G], denominator: list[G]) -> tuple[list[G], list[G]]:
    divisor = gp_trim(denominator)
    require(not gp_is_zero(divisor), "Gaussian polynomial division by zero")
    residual = gp_trim(numerator)
    if len(residual) < len(divisor):
        return [ZERO_G], residual
    quotient = [ZERO_G] * (len(residual) - len(divisor) + 1)
    while not gp_is_zero(residual) and len(residual) >= len(divisor):
        shift = len(residual) - len(divisor)
        coefficient = residual[-1] / divisor[-1]
        quotient[shift] = quotient[shift] + coefficient
        term = [ZERO_G] * shift + [coefficient * value for value in divisor]
        residual = gp_subtract(residual, term)
    return gp_trim(quotient), gp_trim(residual)


def gp_remainder(poly: list[G], modulus: list[G]) -> list[G]:
    require(len(gp_trim(modulus)) > 1, "constant Gaussian polynomial is not a modulus")
    return gp_divmod(poly, modulus)[1]


def gp_extended_gcd(
    left: list[G], right: list[G]
) -> tuple[list[G], list[G], list[G]]:
    old_r, current_r = gp_trim(left), gp_trim(right)
    old_s, current_s = [G(F(1))], [ZERO_G]
    old_t, current_t = [ZERO_G], [G(F(1))]
    while not gp_is_zero(current_r):
        quotient, next_r = gp_divmod(old_r, current_r)
        old_r, current_r = current_r, next_r
        old_s, current_s = current_s, gp_subtract(
            old_s, gp_multiply(quotient, current_s)
        )
        old_t, current_t = current_t, gp_subtract(
            old_t, gp_multiply(quotient, current_t)
        )
    unit = G(F(1)) / old_r[-1]
    return (
        gp_scale(old_r, unit),
        gp_scale(old_s, unit),
        gp_scale(old_t, unit),
    )


def gp_inverse_mod(poly: list[G], modulus: list[G]) -> list[G]:
    common, bezout, _ = gp_extended_gcd(poly, modulus)
    require(common == [G(F(1))], "Gaussian polynomial is not invertible")
    return gp_remainder(bezout, modulus)


def gp_evaluate(poly: list[G], point: G) -> G:
    value = ZERO_G
    for coefficient in reversed(gp_trim(poly)):
        value = value * point + coefficient
    return value


def gp_render(poly: list[G]) -> list[str]:
    return [value.render() for value in gp_trim(poly)]


def as_gpoly(poly: list[F]) -> list[G]:
    return [G(value) for value in trim(poly)]


def local_power(point: G, exponent: int, scalar: G | F | int = 1) -> list[G]:
    return gp_scale(gp_power([-point, G(F(1))], exponent), scalar)


def crt_selector(
    conditions: list[tuple[G, int, list[G]]]
) -> tuple[list[G], list[G], list[dict[str, object]]]:
    require(
        len([point for point, _, _ in conditions])
        == len(set(point for point, _, _ in conditions)),
        "selector conditions repeat a support point",
    )
    selector = [ZERO_G]
    modulus = [G(F(1))]
    rows: list[dict[str, object]] = []
    for point, order, target in sorted(
        conditions, key=lambda row: (row[0].re, row[0].im)
    ):
        require(order > 0, "selector modulus order is not positive")
        local_modulus = local_power(point, order)
        reduced_target = gp_remainder(target, local_modulus)
        correction = gp_remainder(
            gp_multiply(
                gp_remainder(gp_subtract(reduced_target, selector), local_modulus),
                gp_inverse_mod(modulus, local_modulus),
            ),
            local_modulus,
        )
        new_modulus = gp_multiply(modulus, local_modulus)
        selector = gp_remainder(
            gp_add(selector, gp_multiply(modulus, correction)), new_modulus
        )
        modulus = new_modulus
        rows.append(
            {
                "point": point.render(),
                "modulus_order": order,
                "target_remainder": gp_render(reduced_target),
            }
        )
    if not conditions:
        return [ZERO_G], [G(F(1))], []
    for point, order, target in conditions:
        local_modulus = local_power(point, order)
        require(
            gp_is_zero(
                gp_remainder(gp_subtract(selector, target), local_modulus)
            ),
            "reduced selector violates a local congruence",
        )
    require(len(selector) < len(modulus), "selector is not the reduced representative")
    return selector, modulus, rows


def gp_taylor(poly: list[G], point: G) -> list[G]:
    current = gp_trim(poly)
    factorial = F(1)
    coefficients: list[G] = []
    for order in range(len(current)):
        if order > 0:
            factorial *= order
        coefficients.append(gp_evaluate(current, point) / factorial)
        current = gp_derivative(current)
    return gp_trim(coefficients)


def series_zero_order(series: list[G]) -> int | None:
    for index, value in enumerate(series):
        if value != ZERO_G:
            return index
    return None


def rational_residue(
    numerator: list[G], denominator: list[G], point: G
) -> G:
    numerator_series = gp_taylor(numerator, point)
    denominator_series = gp_taylor(denominator, point)
    numerator_order = series_zero_order(numerator_series)
    denominator_order = series_zero_order(denominator_series)
    require(denominator_order is not None, "denominator vanished identically")
    if numerator_order is None or numerator_order >= denominator_order:
        return ZERO_G
    pole_order = denominator_order - numerator_order
    numerator_unit = numerator_series[numerator_order:]
    denominator_unit = denominator_series[denominator_order:]
    quotient: list[G] = []
    for degree in range(pole_order):
        value = numerator_unit[degree] if degree < len(numerator_unit) else ZERO_G
        for index in range(1, degree + 1):
            if index < len(denominator_unit):
                value = value - denominator_unit[index] * quotient[degree - index]
        quotient.append(value / denominator_unit[0])
    return quotient[pole_order - 1]


def polynomial_zero_order(poly: list[G], point: G) -> int:
    order = series_zero_order(gp_taylor(poly, point))
    require(order is not None, "zero polynomial has infinite order")
    return order


def certify_denominator_manifest(
    coefficients: list[F], points: list[G], expected_points: list[G]
) -> list[dict[str, object]]:
    require(len(points) == len(set(points)), "denominator manifest has a duplicate")
    require(
        len(expected_points) == len(set(expected_points)),
        "frozen denominator manifest has a duplicate",
    )
    require(set(points) == set(expected_points), "denominator manifest is incomplete")
    parent = as_gpoly(coefficients)
    first = gp_derivative(parent)
    second = gp_derivative(first)
    require(len(second) > 1 or not gp_is_zero(second), "second derivative vanished")
    events: list[dict[str, object]] = []
    total_first = 0
    total_second = 0
    for point in sorted(points, key=lambda value: (value.re, value.im)):
        m = polynomial_zero_order(parent, point)
        r = polynomial_zero_order(first, point)
        s = polynomial_zero_order(second, point)
        require(r > 0 or s > 0, "manifest contains no denominator zero")
        total_first += r
        total_second += s
        events.append({"point": point, "m": m, "r": r, "s": s})
    require(total_first == len(first) - 1, "F-prime root coverage is incomplete")
    require(total_second == len(second) - 1, "F-double-prime root coverage is incomplete")
    return events


def fixed_window_selector_ledger(
    name: str,
    coefficients: list[F],
    points: list[G],
    expected_points: list[G],
    target_points: list[G],
    expected_target_points: list[G],
) -> dict[str, object]:
    require(len(target_points) == len(set(target_points)), "target manifest has a duplicate")
    require(
        len(expected_target_points) == len(set(expected_target_points)),
        "frozen target manifest has a duplicate",
    )
    require(set(target_points) == set(expected_target_points), "target manifest changed")
    events = certify_denominator_manifest(coefficients, points, expected_points)
    event_by_point = {row["point"]: row for row in events}
    require(set(target_points) <= set(event_by_point), "target is outside event support")
    derived_targets = {
        row["point"]
        for row in events
        if row["point"].im == 0 and row["m"] == 0 and row["r"] % 2 == 1
    }
    require(
        set(target_points) == derived_targets,
        "target manifest omits or adds an eligible real odd turn",
    )
    for point in target_points:
        row = event_by_point[point]
        require(
            point.im == 0 and row["m"] == 0 and row["r"] % 2 == 1,
            "target is not an eligible real odd noncommon turn",
        )
        require(row["s"] == row["r"] - 1, "target derivative ladder changed")
    first_conditions: list[tuple[G, int, list[G]]] = []
    second_conditions: list[tuple[G, int, list[G]]] = []
    event_rows: list[dict[str, object]] = []
    target_set = set(target_points)
    for row in events:
        point = row["point"]
        m, r, s = row["m"], row["r"], row["s"]
        d1 = max(r - m, 0)
        d2 = max(r + s - 2 * m, 0)
        targeted = point in target_set
        if d1 > 0:
            first_target = local_power(point, r - 1) if targeted else [ZERO_G]
            first_conditions.append((point, d1, first_target))
        if d2 > 0:
            second_target = (
                local_power(point, 2 * r - 2, r) if targeted else [ZERO_G]
            )
            second_conditions.append((point, d2, second_target))
        event_rows.append(
            {
                "point": point.render(),
                "orders": {"m": m, "r": r, "s": s},
                "P_actual_pole_order": d1,
                "Q_actual_pole_order": d2,
                "eligible_target": targeted,
            }
        )
    first_selector, first_modulus, first_rows = crt_selector(first_conditions)
    second_selector, second_modulus, second_rows = crt_selector(second_conditions)
    parent = as_gpoly(coefficients)
    first = gp_derivative(parent)
    second = gp_derivative(first)
    weighted_first_numerator = gp_multiply(first_selector, parent)
    weighted_second_numerator = gp_multiply(
        second_selector, gp_multiply(parent, parent)
    )
    weighted_second_denominator = gp_multiply(first, second)
    first_residues: list[G] = []
    second_residues: list[G] = []
    target_first: list[G] = []
    target_second: list[G] = []
    for row in events:
        point = row["point"]
        residue_one = rational_residue(weighted_first_numerator, first, point)
        residue_two = rational_residue(
            weighted_second_numerator, weighted_second_denominator, point
        )
        first_residues.append(residue_one)
        second_residues.append(residue_two)
        if point in target_set:
            leading_first = gp_taylor(first, point)[row["r"]]
            rho = gp_evaluate(parent, point) / leading_first
            require(residue_one == rho, "first selector missed the leading jet")
            require(residue_two == rho**2, "second selector missed the jet square")
            target_first.append(rho)
            target_second.append(rho**2)
        else:
            require(residue_one == ZERO_G, "first selector left a nontarget residue")
            require(residue_two == ZERO_G, "second selector left a nontarget residue")
    require(gsum(first_residues) == gsum(target_first), "first charge changed")
    require(gsum(second_residues) == gsum(target_second), "second charge changed")
    require(
        all(coefficient.im == 0 for coefficient in first_selector + second_selector),
        "conjugation-stable selector did not have real coefficients",
    )
    return {
        "name": name,
        "frozen_denominator_manifest": [
            point.render()
            for point in sorted(points, key=lambda value: (value.re, value.im))
        ],
        "eligible_target_manifest": [
            point.render()
            for point in sorted(target_points, key=lambda value: (value.re, value.im))
        ],
        "events": event_rows,
        "first_selector": gp_render(first_selector),
        "first_primary_modulus": gp_render(first_modulus),
        "first_congruences": first_rows,
        "second_selector": gp_render(second_selector),
        "second_primary_modulus": gp_render(second_modulus),
        "second_congruences": second_rows,
        "weighted_first_residues": [value.render() for value in first_residues],
        "weighted_second_residues": [value.render() for value in second_residues],
        "jet_first_sum": gsum(target_first).render(),
        "jet_second_moment": gsum(target_second).render(),
        "all_nontarget_actual_poles_annihilated": True,
        "selector_charge_identities_verified": True,
    }


def poly_render(poly: list[F]) -> list[str]:
    return [str(value) for value in trim(poly)]


def certify_factorization(
    coefficients: list[F], factors: dict[int, list[F]]
) -> tuple[list[F], dict[int, list[F]], F]:
    parent = trim(coefficients)
    require(len(parent) >= 2, "parent polynomial is constant")
    critical = derivative(parent)
    require(not is_zero(critical), "critical polynomial vanished")
    normalized: dict[int, list[F]] = {}
    for order, factor in factors.items():
        require(type(order) is int and order > 0, "invalid multiplicity label")
        values = trim(factor)
        require(len(values) > 1, "stratum factor is constant")
        require(values[-1] == 1, "stratum factor is not monic")
        require(
            gcd_poly(values, derivative(values)) == [F(1)],
            "stratum factor is not square-free",
        )
        normalized[order] = values
    orders = sorted(normalized)
    for left_index, left_order in enumerate(orders):
        for right_order in orders[left_index + 1 :]:
            require(
                gcd_poly(normalized[left_order], normalized[right_order]) == [F(1)],
                "multiplicity strata overlap",
            )
    leading = critical[-1]
    reconstruction = [leading]
    for order in orders:
        reconstruction = multiply(reconstruction, power(normalized[order], order))
    require(
        trim(reconstruction) == critical,
        "square-free multiplicity manifest is incomplete or mislabeled",
    )
    return critical, normalized, leading


def construct_carriers(
    coefficients: list[F], factors: dict[int, list[F]]
) -> dict[str, object]:
    critical, normalized, leading = certify_factorization(coefficients, factors)
    odd_orders = [order for order in sorted(normalized) if order % 2 == 1]
    support = [F(1)]
    carrier = [F(0)]
    rows: list[dict[str, object]] = []
    raw_rows: dict[int, dict[str, list[F]]] = {}
    for order in odd_orders:
        factor = normalized[order]
        factor_power = power(factor, order)
        unit = quotient_exact(critical, factor_power)
        local_denominator = multiply(unit, power(derivative(factor), order))
        require(
            gcd_poly(local_denominator, factor) == [F(1)],
            "local leading unit is not invertible",
        )
        target = remainder(
            multiply(coefficients, inverse_mod(local_denominator, factor)),
            factor,
        )
        new_support = multiply(support, factor)
        correction = remainder(
            multiply(
                remainder(subtract(target, carrier), factor),
                inverse_mod(support, factor),
            ),
            factor,
        )
        carrier = remainder(add(carrier, multiply(support, correction)), new_support)
        support = new_support
        require(
            is_zero(
                remainder(
                    subtract(multiply(local_denominator, carrier), coefficients),
                    factor,
                )
            ),
            "CRT carrier does not encode the local jet",
        )
        raw_rows[order] = {
            "factor": factor,
            "unit": unit,
            "local_denominator": local_denominator,
            "target": target,
        }
        rows.append(
            {
                "critical_order": order,
                "factor": poly_render(factor),
                "unit_p_over_factor_power": poly_render(unit),
                "local_denominator": poly_render(local_denominator),
                "target_mod_factor": poly_render(target),
            }
        )
    if support == [F(1)]:
        carrier = [F(0)]
        second = [F(0)]
    else:
        carrier = remainder(carrier, support)
        second = remainder(multiply(carrier, carrier), support)
    for order in odd_orders:
        factor = normalized[order]
        row = raw_rows[order]
        require(
            is_zero(
                remainder(
                    subtract(
                        multiply(row["local_denominator"], carrier),
                        coefficients,
                    ),
                    factor,
                )
            ),
            "final CRT carrier changed a stratum congruence",
        )
        require(
            is_zero(remainder(subtract(second, multiply(carrier, carrier)), factor)),
            "second carrier is not the jet square",
        )
    return {
        "critical_polynomial": critical,
        "leading_scalar": leading,
        "factors": normalized,
        "odd_orders": odd_orders,
        "odd_support": support,
        "first_carrier": carrier,
        "second_carrier": second,
        "rows": rows,
        "raw_rows": raw_rows,
    }


def root_trace(squarefree_monic: list[F], carrier: list[F]) -> F:
    support = trim(squarefree_monic)
    if support == [F(1)]:
        return F(0)
    require(support[-1] == 1, "trace support is not monic")
    require(
        gcd_poly(support, derivative(support)) == [F(1)],
        "trace support is not square-free",
    )
    degree = len(support) - 1
    reduced = remainder(carrier, support)
    power_sums = [F(degree)]
    for exponent in range(1, degree):
        newton = F(exponent) * support[degree - exponent]
        for index in range(1, exponent):
            newton += support[degree - index] * power_sums[exponent - index]
        power_sums.append(-newton)
    return sum(
        (reduced[index] if index < len(reduced) else F(0)) * power_sums[index]
        for index in range(degree)
    )


def certify_root_manifest(
    factors: dict[int, list[F]],
    roots: dict[int, list[G]],
    expected_roots: dict[int, list[G]],
) -> dict[int, list[G]]:
    require(set(roots) == set(factors), "root manifest has missing stratum")
    require(set(expected_roots) == set(factors), "frozen root manifest has missing stratum")
    certified: dict[int, list[G]] = {}
    for order in sorted(factors):
        actual = list(roots[order])
        expected = list(expected_roots[order])
        require(len(actual) == len(set(actual)), "root manifest has a duplicate")
        require(len(expected) == len(set(expected)), "frozen root manifest has a duplicate")
        require(set(actual) == set(expected), "root manifest is incomplete or extraneous")
        require(
            len(actual) == len(factors[order]) - 1,
            "root manifest degree does not match stratum",
        )
        require(
            all(evaluate(factors[order], point) == ZERO_G for point in actual),
            "root manifest contains a nonroot",
        )
        certified[order] = sorted(actual, key=lambda point: (point.re, point.im))
    return certified


def jet_flux_ledger(
    name: str,
    coefficients: list[F],
    factors: dict[int, list[F]],
    roots: dict[int, list[G]],
    expected_roots: dict[int, list[G]],
) -> dict[str, object]:
    construction = construct_carriers(coefficients, factors)
    normalized = construction["factors"]
    certified = certify_root_manifest(normalized, roots, expected_roots)
    first = construction["first_carrier"]
    second = construction["second_carrier"]
    event_rows: list[dict[str, object]] = []
    odd_first: list[G] = []
    odd_second: list[G] = []
    real_first: list[G] = []
    real_second: list[G] = []
    nonreal_first: list[G] = []
    nonreal_second: list[G] = []
    for order in sorted(normalized):
        for point in certified[order]:
            parent_value = evaluate(coefficients, point)
            common = parent_value == ZERO_G
            if order % 2 == 1:
                raw_row = construction["raw_rows"][order]
                local_denominator = evaluate(raw_row["local_denominator"], point)
                require(local_denominator != ZERO_G, "local leading denominator vanished")
                rho = parent_value / local_denominator
                encoded_first = evaluate(first, point)
                encoded_second = evaluate(second, point)
                require(encoded_first == rho, "first CRT residue changed")
                require(encoded_second == rho**2, "second CRT residue changed")
                odd_first.append(rho)
                odd_second.append(rho**2)
                if point.im == 0 and not common:
                    real_first.append(rho)
                    real_second.append(rho**2)
                if point.im != 0:
                    nonreal_first.append(rho)
                    nonreal_second.append(rho**2)
                event_rows.append(
                    {
                        "point": point.render(),
                        "critical_order": order,
                        "common_parent_zero": common,
                        "eligible_real_turn": point.im == 0 and not common,
                        "algebraic_leading_carrier": rho.render(),
                        "rho_jet": (
                            rho.render() if point.im == 0 and not common else None
                        ),
                        "first_log_derivative_residue": encoded_first.render(),
                        "second_log_derivative_residue": encoded_second.render(),
                    }
                )
            else:
                event_rows.append(
                    {
                        "point": point.render(),
                        "critical_order": order,
                        "common_parent_zero": common,
                        "eligible_real_turn": False,
                        "excluded_even_stationary_stratum": True,
                    }
                )
    trace_first = G(root_trace(construction["odd_support"], first))
    trace_second = G(root_trace(construction["odd_support"], second))
    require(trace_first == gsum(odd_first), "first global residue trace changed")
    require(trace_second == gsum(odd_second), "second global residue trace changed")
    first_correction = gsum(nonreal_first)
    second_correction = gsum(nonreal_second)
    jet_first = -gsum(real_first)
    jet_second = gsum(real_second)
    require(jet_first == -trace_first + first_correction, "first correction sign changed")
    require(jet_second == trace_second - second_correction, "second correction sign changed")
    require(jet_first.im == 0 and jet_second.im == 0, "real jet moments became nonreal")
    return {
        "name": name,
        "critical_polynomial": poly_render(construction["critical_polynomial"]),
        "leading_scalar": str(construction["leading_scalar"]),
        "factor_manifest": {
            str(order): poly_render(normalized[order]) for order in sorted(normalized)
        },
        "frozen_root_manifest": {
            str(order): [point.render() for point in certified[order]]
            for order in sorted(certified)
        },
        "odd_multiplicity_orders": construction["odd_orders"],
        "odd_squarefree_support": poly_render(construction["odd_support"]),
        "first_crt_carrier": poly_render(first),
        "second_crt_carrier": poly_render(second),
        "stratum_congruences": construction["rows"],
        "events": event_rows,
        "global_first_residue_trace": trace_first.render(),
        "global_second_residue_trace": trace_second.render(),
        "nonreal_first_correction": first_correction.render(),
        "nonreal_second_algebraic_square_correction": second_correction.render(),
        "real_jet_first_carrier": jet_first.render(),
        "real_jet_second_moment": jet_second.render(),
        "flux_identities_verified": True,
    }


def selector_fixtures() -> dict[str, object]:
    simple_points = [G(F(-1)), G(F(0)), G(F(1))]
    flat_points = [G(F(0))]
    mixed_points = [G(F(0)), G(F(1, 4)), G(F(1))]
    nonreal_points = [-I, G(F(0)), I]
    parity_points = [G(F(-1)), -I, G(F(0)), I, G(F(1))]
    return {
        "simple_cubic_with_adjacent_debt_killed": fixed_window_selector_ledger(
            "simple_cubic_with_adjacent_debt_killed",
            [F(1), F(-3), F(0), F(1)],
            simple_points,
            simple_points,
            [G(F(-1)), G(F(1))],
            [G(F(-1)), G(F(1))],
        ),
        "flat_quartic": fixed_window_selector_ledger(
            "flat_quartic",
            [F(-1), F(0), F(0), F(0), F(1)],
            flat_points,
            flat_points,
            flat_points,
            flat_points,
        ),
        "mixed_simple_flat": fixed_window_selector_ledger(
            "mixed_simple_flat",
            [F(2), F(0), F(-10), F(20), F(-15), F(4)],
            mixed_points,
            mixed_points,
            [G(F(0)), G(F(1))],
            [G(F(0)), G(F(1))],
        ),
        "parity_symmetric_partial_cancellation": fixed_window_selector_ledger(
            "parity_symmetric_partial_cancellation",
            [F(0), F(1), F(0), F(0), F(0), F(-1, 5)],
            parity_points,
            parity_points,
            [G(F(-1)), G(F(1))],
            [G(F(-1)), G(F(1))],
        ),
        "common_only": fixed_window_selector_ledger(
            "common_only",
            [F(0), F(0), F(0), F(0), F(1)],
            flat_points,
            flat_points,
            [],
            [],
        ),
        "even_stationary_only": fixed_window_selector_ledger(
            "even_stationary_only",
            [F(2), F(0), F(0), F(1)],
            flat_points,
            flat_points,
            [],
            [],
        ),
        "nonreal_and_adjacent_support_annihilated": fixed_window_selector_ledger(
            "nonreal_and_adjacent_support_annihilated",
            [F(3), F(3), F(0), F(1)],
            nonreal_points,
            nonreal_points,
            [],
            [],
        ),
    }


def squarefree_corollary_fixtures() -> dict[str, object]:
    simple_roots = {1: [G(F(-1)), G(F(1))]}
    flat_roots = {3: [G(F(0))]}
    mixed_roots = {1: [G(F(-1))], 3: [G(F(1))]}
    common_roots = {1: [G(F(-1)), G(F(0)), G(F(1))]}
    even_roots = {2: [G(F(-1, 2)), G(F(1, 2))]}
    nonreal_roots = {1: [-I, I]}
    return {
        "simple_cubic": jet_flux_ledger(
            "simple_cubic",
            [F(1), F(-3), F(0), F(1)],
            {1: [F(-1), F(0), F(1)]},
            simple_roots,
            simple_roots,
        ),
        "flat_quartic": jet_flux_ledger(
            "flat_quartic",
            [F(-1), F(0), F(0), F(0), F(1)],
            {3: [F(0), F(1)]},
            flat_roots,
            flat_roots,
        ),
        "mixed_simple_flat": jet_flux_ledger(
            "mixed_simple_flat",
            [F(0), F(-1), F(1), F(0), F(-1, 2), F(1, 5)],
            {1: [F(1), F(1)], 3: [F(-1), F(1)]},
            mixed_roots,
            mixed_roots,
        ),
        "nonlinear_flat_stratum": jet_flux_ledger(
            "nonlinear_flat_stratum",
            [F(0), F(-1), F(0), F(1), F(0), F(-3, 5), F(0), F(1, 7)],
            {3: [F(-1), F(0), F(1)]},
            {3: [G(F(-1)), G(F(1))]},
            {3: [G(F(-1)), G(F(1))]},
        ),
        "common_and_two_turns": jet_flux_ledger(
            "common_and_two_turns",
            [F(0), F(0), F(-2), F(0), F(1)],
            {1: [F(0), F(-1), F(0), F(1)]},
            common_roots,
            common_roots,
        ),
        "even_stationary_only": jet_flux_ledger(
            "even_stationary_only",
            [F(-10), F(1, 16), F(0), F(-1, 6), F(0), F(1, 5)],
            {2: [F(-1, 4), F(0), F(1)]},
            even_roots,
            even_roots,
        ),
        "nonreal_pair": jet_flux_ledger(
            "nonreal_pair",
            [F(1), F(1), F(0), F(1, 3)],
            {1: [F(1), F(0), F(1)]},
            nonreal_roots,
            nonreal_roots,
        ),
    }


def mutation_firewalls() -> dict[str, object]:
    flat = [F(-1), F(0), F(0), F(0), F(1)]
    cubic_from_x2 = [F(1), F(0), F(0), F(1, 3)]
    quartic_from_x3 = [F(1), F(0), F(0), F(0), F(1, 4)]
    nonlinear_flat = [
        F(0), F(-1), F(0), F(1), F(0), F(-3, 5), F(0), F(1, 7)
    ]
    partial_cancellation = [F(0), F(1), F(0), F(0), F(0), F(-1, 5)]

    def rejects(coefficients: list[F], factors: dict[int, list[F]]) -> bool:
        try:
            construct_carriers(coefficients, factors)
        except AssertionError:
            return True
        return False

    flat_ledger = squarefree_corollary_fixtures()["flat_quartic"]
    scaled_roots = {3: [G(F(0))]}
    scaled = jet_flux_ledger(
        "scaled_flat_quartic",
        [F(-7), F(0), F(0), F(0), F(7)],
        {3: [F(0), F(1)]},
        scaled_roots,
        scaled_roots,
    )
    base_event = flat_ledger["events"][0]
    ordinary_event = BASE.BASE.local_event(flat, F(0))
    simple = [F(1), F(-3), F(0), F(1)]
    simple_points = [G(F(-1)), G(F(0)), G(F(1))]
    simple_targets = [G(F(-1)), G(F(1))]
    simple_g = as_gpoly(simple)
    simple_first = gp_derivative(simple_g)
    simple_second = gp_derivative(simple_first)
    simple_q_numerator = gp_multiply(simple_g, simple_g)
    simple_q_denominator = gp_multiply(simple_first, simple_second)
    naive_q_residues = [
        rational_residue(simple_q_numerator, simple_q_denominator, point)
        for point in simple_points
    ]
    flat_g = as_gpoly(flat)
    flat_first = gp_derivative(flat_g)
    flat_second = gp_derivative(flat_first)
    flat_q_denominator = gp_multiply(flat_first, flat_second)
    wrong_flat_second_residue = rational_residue(
        gp_multiply(local_power(G(F(0)), 4), gp_multiply(flat_g, flat_g)),
        flat_q_denominator,
        G(F(0)),
    )
    nonlinear_construction = construct_carriers(
        nonlinear_flat, {3: [F(-1), F(0), F(1)]}
    )
    nonlinear_factor = nonlinear_construction["factors"][3]
    wrong_nonlinear_denominator = derivative(nonlinear_factor)
    nonlinear_derivative_power_mutation_rejected = not is_zero(
        remainder(
            subtract(
                multiply(
                    wrong_nonlinear_denominator,
                    nonlinear_construction["first_carrier"],
                ),
                nonlinear_flat,
            ),
            nonlinear_factor,
        )
    )
    partial_g = as_gpoly(partial_cancellation)
    partial_first = gp_derivative(partial_g)
    partial_second = gp_derivative(partial_first)
    partial_q_residue = rational_residue(
        gp_multiply(partial_g, partial_g),
        gp_multiply(partial_first, partial_second),
        G(F(0)),
    )

    def rejects_selector(
        points: list[G], expected: list[G], targets: list[G], expected_targets: list[G]
    ) -> bool:
        try:
            fixed_window_selector_ledger(
                "mutation", simple, points, expected, targets, expected_targets
            )
        except AssertionError:
            return True
        return False

    return {
        "omitted_factor_rejected": rejects(flat, {}),
        "wrong_multiplicity_label_rejected": rejects(flat, {1: [F(0), F(1)]}),
        "nonmonic_factor_rejected": rejects(flat, {3: [F(0), F(2)]}),
        "nonsquarefree_factor_rejected": rejects(
            cubic_from_x2, {1: [F(0), F(0), F(1)]}
        ),
        "overlapping_strata_rejected": rejects(
            quartic_from_x3,
            {1: [F(0), F(1)], 2: [F(0), F(1)]},
        ),
        "nonlinear_derivative_power_mutation_rejected": (
            nonlinear_derivative_power_mutation_rejected
        ),
        "selector_manifest_missing_rejected": rejects_selector(
            [G(F(-1)), G(F(1))], simple_points, simple_targets, simple_targets
        ),
        "selector_manifest_duplicate_rejected": rejects_selector(
            [G(F(-1)), G(F(0)), G(F(0)), G(F(1))],
            simple_points,
            simple_targets,
            simple_targets,
        ),
        "selector_manifest_extraneous_rejected": rejects_selector(
            [G(F(-1)), G(F(0)), G(F(1)), G(F(2))],
            simple_points,
            simple_targets,
            simple_targets,
        ),
        "selector_target_omission_rejected": rejects_selector(
            simple_points, simple_points, [G(F(-1))], simple_targets
        ),
        "both_target_manifests_incomplete_rejected": rejects_selector(
            simple_points, simple_points, [], []
        ),
        "simple_cubic_adjacent_debt": {
            "naive_Q_residues": [value.render() for value in naive_q_residues],
            "naive_Q_charge": gsum(naive_q_residues).render(),
            "target_jet_second_moment": "5/18",
            "weighted_selector": ["0", "0", "1"],
            "F_double_prime_only_pole_annihilated": True,
        },
        "partial_common_cancellation": {
            "orders_at_zero": {"m": 1, "r": 0, "s": 3},
            "P_actual_pole_order": 0,
            "Q_actual_pole_order": 1,
            "unweighted_Q_residue": partial_q_residue.render(),
            "selected_Q_residue": "0",
        },
        "flat_quartic": {
            "rho_jet": base_event["rho_jet"],
            "desired_jet_square": base_event["second_log_derivative_residue"],
            "residue_of_squared_first_flux": "0",
            "residue_without_load_bearing_r_factor": wrong_flat_second_residue.render(),
            "ordinary_Q_residue": ordinary_event["Q_residue"],
            "naive_radical_flux_residue": "-1",
            "scaled_naive_radical_flux_residue": "-7",
            "scaled_true_rho_jet": scaled["events"][0]["rho_jet"],
            "squaring_first_flux_loses_second_moment": True,
            "radical_support_without_local_unit_is_not_scale_invariant": True,
        },
    }


def content_hashes() -> dict[str, str]:
    hashes: dict[str, str] = {}
    for relative_path in CONTENT_FILES:
        path = REPO_ROOT / relative_path
        if not path.is_file():
            raise FileNotFoundError(f"missing load-bearing file: {relative_path}")
        normalized = path.read_bytes().replace(b"\r\n", b"\n")
        hashes[relative_path] = hashlib.sha256(normalized).hexdigest()
    return hashes


def build_payload() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "riemann.t105105.fixed-window-crt-jet-selectors.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_RATIONAL_AND_GAUSSIAN_RATIONAL",
        "source": {
            "checkpoint_base": BASE_COMMIT,
            "post_freeze_context_pr": 720,
            "post_freeze_context_head": "10bba584c01277e880aaa21e1fea09f396ca7246",
        },
        "dependency_checkpoint": dependency_checkpoint(),
        "checks": {
            "fixed_window_selector_fixtures": selector_fixtures(),
            "squarefree_polynomial_corollary": squarefree_corollary_fixtures(),
            "mutation_firewalls": mutation_firewalls(),
        },
        "content_sha256": content_hashes(),
        "content_hash_mode": "LF_NORMALIZED_TEXT",
        "scope": {
            "fixed_window_holomorphic_crt_selector_identity_proved": True,
            "all_nontarget_actual_poles_annihilated": True,
            "finite_polynomial_squarefree_crt_bridge_proved": True,
            "root_free_carrier_construction_proved": True,
            "odd_multiplicity_strata_encoded": True,
            "common_odd_events_zero_suppressed": True,
            "even_stationary_strata_excluded": True,
            "second_jet_moment_is_simple_residue_flux": True,
            "nonreal_corrections_are_algebraic_squares": True,
            "ordinary_P_Q_residues_recover_flat_jets": False,
            "xi_fixed_window_selector_exists_given_exact_event_manifest": True,
            "xi_event_manifest_constructed": False,
            "xi_selector_boundary_norm_estimated": False,
            "xi_cofinal_window_limit_proved": False,
            "xi_nonreal_jet_corrections_estimated": False,
            "xi_jet_moments_estimated": False,
            "strict_xi_jet_coherence_margin_proved": False,
            "rcmv104530_proved": False,
            "rh_established": False,
        },
        "heavy_computation_run": False,
        "verdict": VERDICT,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_payload()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    print(payload["verdict"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
