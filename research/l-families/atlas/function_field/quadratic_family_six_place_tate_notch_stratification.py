#!/usr/bin/env python3
"""Exact bounded replay for the six-place Tate-notch stratification."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections.abc import Callable
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE_COMMIT = "b653f272954bf7e1d93d6e54c1883b4cb00b181c"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "QUADRATIC_FAMILY_SIX_PLACE_CONNECTED_SATURATION.md"
    ): "21edbccca1c21a4e058aaeccb8f3a92688c9e2ff",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_six_place_connected_saturation.py"
    ): "379ba7af057b3997b119a967d8f47e17437932da",
    (
        "research/l-families/atlas/function_field/"
        "quadratic_family_six_place_connected_saturation.json"
    ): "7e5ad04886abedaf7da4df5fc91fdb05787cb25a",
    "tests/test_quadratic_family_six_place_connected_saturation.py": (
        "1673941ca46dbf4591a677fa80fad82af2b095c4"
    ),
}

T = sp.symbols("T")
RECURRENCE_CHECKS = 3
MAX_RAW_EXTENSION = 22
GENERIC_CONTROLS = ((7, 1, 3), (11, 1, 4))
REALIZED_SQUARE_CONTROLS = (
    (11, 2, (0, 1, 2, 3, 5, 9), 0, 22, 6),
    (13, 2, (0, 1, 2, 3, 5, 11), -4, 30, 8),
)


def check_source_contract() -> None:
    for path, expected in SOURCE_BLOBS.items():
        completed = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=3,
        )
        if completed.stdout.strip() != expected:
            raise RuntimeError(f"source blob mismatch: {path}")


def polynomial_multiply(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for left_index, left_value in enumerate(left):
        for right_index, right_value in enumerate(right):
            output[left_index + right_index] += left_value * right_value
    return tuple(output)


def polynomial_value(coefficients: tuple[int, ...], value: int) -> int:
    total = 0
    for coefficient in reversed(coefficients):
        total = total * value + coefficient
    return total


def to_sympy(coefficients: tuple[int, ...]) -> sp.Poly:
    return sp.Poly(
        sum(coefficient * T**power for power, coefficient in enumerate(coefficients)),
        T,
        domain=sp.QQ,
    )


def from_sympy(poly: sp.Poly) -> tuple[int, ...]:
    primitive = sp.Poly(poly.monic(), T, domain=sp.QQ)
    values = tuple(primitive.nth(power) for power in range(primitive.degree() + 1))
    if any(value.q != 1 for value in values):
        raise ArithmeticError("expected an integral monic polynomial")
    return tuple(int(value) for value in values)


def weil_polynomial(prime: int, trace: int, middle: int) -> tuple[int, ...]:
    return prime**2, -prime * trace, middle, -trace, 1


def primitive_pair_polynomial(prime: int, trace: int, middle: int) -> tuple[int, ...]:
    return (
        prime**4,
        -(prime**2) * (middle - 2 * prime),
        prime * trace**2 - 2 * prime * middle + 2 * prime**2,
        -(middle - 2 * prime),
        1,
    )


def scale_roots(coefficients: tuple[int, ...], scale: int) -> tuple[int, ...]:
    degree = len(coefficients) - 1
    return tuple(
        coefficient * scale ** (degree - power)
        for power, coefficient in enumerate(coefficients)
    )


def notch_polynomial(prime: int) -> tuple[int, ...]:
    return polynomial_multiply(
        polynomial_multiply((-1, 1), (-prime, 1)), (-(prime**2), 1)
    )


def field_multiply(
    left: tuple[int, int], right: tuple[int, int], prime: int, nonsquare: int
) -> tuple[int, int]:
    a, b = left
    c, d = right
    return (
        (a * c + nonsquare * b * d) % prime,
        (a * d + b * c) % prime,
    )


def field_power(
    value: tuple[int, int], exponent: int, prime: int, nonsquare: int
) -> tuple[int, int]:
    output = (1, 0)
    base = value
    while exponent:
        if exponent & 1:
            output = field_multiply(output, base, prime, nonsquare)
        base = field_multiply(base, base, prime, nonsquare)
        exponent //= 2
    return output


def extension_character(value: tuple[int, int], prime: int, nonsquare: int) -> int:
    if value == (0, 0):
        return 0
    power = field_power(value, (prime**2 - 1) // 2, prime, nonsquare)
    if power == (1, 0):
        return 1
    if power == (prime - 1, 0):
        return -1
    raise ArithmeticError("quadratic-extension character left {0,+1,-1}")


def realized_curve_coefficients(
    prime: int, nonsquare: int, marks: tuple[int, ...]
) -> tuple[int, int, int]:
    if len(marks) != 6 or len(set(marks)) != 6:
        raise ValueError("control curve requires six distinct marks")
    if pow(nonsquare, (prime - 1) // 2, prime) != prime - 1:
        raise ValueError("quadratic-extension parameter must be nonsquare")
    base_sum = 0
    for z in range(prime):
        value = 1
        for mark in marks:
            value = value * (mark - z) % prime
        base_sum += (
            0 if value == 0 else (1 if pow(value, (prime - 1) // 2, prime) == 1 else -1)
        )
    trace = -1 - base_sum

    extension_sum = 0
    for real in range(prime):
        for imaginary in range(prime):
            z = (real, imaginary)
            value = (1, 0)
            for mark in marks:
                factor = ((mark - real) % prime, (-imaginary) % prime)
                value = field_multiply(value, factor, prime, nonsquare)
            extension_sum += extension_character(value, prime, nonsquare)
    trace_two = -1 - extension_sum
    numerator = trace**2 - trace_two
    if numerator % 2:
        raise ArithmeticError("realized middle coefficient ceased to be integral")
    return trace, numerator // 2, trace_two


def generic_annihilator(prime: int, trace: int, middle: int) -> tuple[int, ...]:
    p_poly = weil_polynomial(prime, trace, middle)
    q_poly = primitive_pair_polynomial(prime, trace, middle)
    return polynomial_multiply(
        polynomial_multiply(p_poly, scale_roots(p_poly, prime**2)),
        polynomial_multiply(q_poly, scale_roots(q_poly, prime)),
    )


def power_sum(coefficients: tuple[int, ...], exponent: int) -> int:
    if exponent < 0:
        raise ValueError("power-sum exponent must be nonnegative")
    degree = len(coefficients) - 1
    if coefficients[-1] != 1:
        raise ValueError("power-sum polynomial must be monic")
    if exponent == 0:
        return degree
    # c_j is the coefficient of T^(degree-j).
    c = (0,) + tuple(coefficients[degree - index] for index in range(1, degree + 1))
    sums = [degree]
    for current in range(1, exponent + 1):
        if current <= degree:
            value = -sum(
                c[index] * sums[current - index] for index in range(1, current)
            )
            value -= current * c[current]
        else:
            value = -sum(
                c[index] * sums[current - index] for index in range(1, degree + 1)
            )
        sums.append(value)
    return sums[exponent]


def tower_traces(
    prime: int, trace: int, middle: int, extension_degree: int
) -> tuple[int, int, int]:
    if extension_degree < 1:
        raise ValueError("extension degree must be positive")
    p_poly = weil_polynomial(prime, trace, middle)
    trace_n = power_sum(p_poly, extension_degree)
    trace_2n = power_sum(p_poly, 2 * extension_degree)
    pair_numerator = trace_n**2 - trace_2n
    if pair_numerator % 2:
        raise ArithmeticError("pair trace ceased to be integral")
    middle_n = pair_numerator // 2
    centered_n = middle_n - 2 * prime**extension_degree
    return trace_n, middle_n, centered_n


def raw_correlation(prime: int, trace: int, middle: int, extension_degree: int) -> int:
    trace_n, middle_n, _ = tower_traces(prime, trace, middle, extension_degree)
    q = prime**extension_degree
    return (q**2 - 21) * trace_n + (q - 6) * middle_n - q**2 + 6 * q - 21


def apply_filter(
    sequence: Callable[[int], int],
    coefficients: tuple[int, ...],
    extension_degree: int,
) -> int:
    return sum(
        coefficient * sequence(extension_degree + offset)
        for offset, coefficient in enumerate(coefficients)
    )


def filtered_correlation(
    prime: int, trace: int, middle: int, extension_degree: int
) -> int:
    return apply_filter(
        lambda degree: raw_correlation(prime, trace, middle, degree),
        notch_polynomial(prime),
        extension_degree,
    )


def verify_recurrence(
    sequence: Callable[[int], int],
    coefficients: tuple[int, ...],
    checks: int = RECURRENCE_CHECKS,
) -> bool:
    return all(
        sum(
            coefficient * sequence(extension_degree + offset)
            for offset, coefficient in enumerate(coefficients)
        )
        == 0
        for extension_degree in range(1, checks + 1)
    )


def remove_root(poly: sp.Poly, root: int) -> sp.Poly:
    factor = sp.Poly(T - root, T, domain=sp.QQ)
    output = poly
    while output.eval(root) == 0:
        output = output.exquo(factor)
    return output


def radical(poly: sp.Poly) -> sp.Poly:
    return poly.exquo(sp.gcd(poly, poly.diff())).monic()


def distinct_root_count(coefficients: tuple[int, ...]) -> int:
    return radical(to_sympy(coefficients)).degree()


def nonnotched_pair_root_count(prime: int, trace: int, middle: int) -> int:
    q_poly = to_sympy(primitive_pair_polynomial(prime, trace, middle))
    return radical(remove_root(q_poly, prime)).degree()


def memberwise_rank(prime: int, trace: int, middle: int) -> int:
    return 2 * distinct_root_count(weil_polynomial(prime, trace, middle)) + 2 * (
        nonnotched_pair_root_count(prime, trace, middle)
    )


def minimal_filtered_polynomial(prime: int, trace: int, middle: int) -> tuple[int, ...]:
    p_radical = radical(to_sympy(weil_polynomial(prime, trace, middle)))
    q_clean = radical(
        remove_root(to_sympy(primitive_pair_polynomial(prime, trace, middle)), prime)
    )
    p_coefficients = from_sympy(p_radical)
    q_coefficients = from_sympy(q_clean)
    return polynomial_multiply(
        polynomial_multiply(p_coefficients, scale_roots(p_coefficients, prime**2)),
        polynomial_multiply(q_coefficients, scale_roots(q_coefficients, prime)),
    )


def control_panel(
    prime: int, trace: int, middle: int, expected_rank: int, label: str
) -> dict[str, object]:
    p_poly = weil_polynomial(prime, trace, middle)
    q_poly = primitive_pair_polynomial(prime, trace, middle)
    delta = trace**2 - 4 * middle + 8 * prime
    if polynomial_value(q_poly, prime) != prime**3 * delta:
        raise ArithmeticError("Q(p) collision identity failed")
    if polynomial_value(q_poly, -prime) != prime**3 * trace**2:
        raise ArithmeticError("Q(-p) trace-zero identity failed")
    for extension_degree in range(1, 7):
        _, _, centered = tower_traces(prime, trace, middle, extension_degree)
        if power_sum(q_poly, extension_degree) != centered:
            raise ArithmeticError("Q power sums disagree with centered pair trace")
    rank = memberwise_rank(prime, trace, middle)
    if rank != expected_rank:
        raise ArithmeticError("memberwise rank classification changed")
    minimal = minimal_filtered_polynomial(prime, trace, middle)
    if len(minimal) - 1 != rank:
        raise ArithmeticError("minimal polynomial degree disagrees with rank")
    filtered = lambda degree: filtered_correlation(prime, trace, middle, degree)
    if not verify_recurrence(filtered, minimal):
        raise ArithmeticError("minimal filtered recurrence failed")
    annihilator = generic_annihilator(prime, trace, middle)
    if not verify_recurrence(filtered, annihilator):
        raise ArithmeticError("degree-sixteen annihilator failed")
    return {
        "collision_delta": delta,
        "first_three_filtered": [str(filtered(degree)) for degree in range(1, 4)],
        "generic_annihilator_degree": len(annihilator) - 1,
        "label": label,
        "memberwise_minimal_degree": len(minimal) - 1,
        "middle": middle,
        "p_distinct_roots": distinct_root_count(p_poly),
        "prime": prime,
        "q_nonnotched_distinct_roots": nonnotched_pair_root_count(prime, trace, middle),
        "trace": trace,
    }


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_contract()
    if MAX_RAW_EXTENSION != RECURRENCE_CHECKS + 19:
        raise ArithmeticError("declared extension cap no longer matches replay")
    notch_checks = {}
    for prime in (7, 11):
        notch = notch_polynomial(prime)
        values = {
            str(root): polynomial_value(notch, root) for root in (1, prime, prime**2)
        }
        if any(values.values()):
            raise ArithmeticError("cubic notch lost a scalar root")
        notch_checks[str(prime)] = {
            "degree": len(notch) - 1,
            "root_values": values,
        }
    controls = []
    for prime, first_trace, second_trace in GENERIC_CONTROLS:
        trace = first_trace + second_trace
        middle = first_trace * second_trace + 2 * prime
        controls.append(control_panel(prime, trace, middle, 16, "generic_split"))
    realized_rows = []
    for (
        prime,
        nonsquare,
        marks,
        expected_trace,
        expected_middle,
        expected_rank,
    ) in REALIZED_SQUARE_CONTROLS:
        trace, middle, trace_two = realized_curve_coefficients(prime, nonsquare, marks)
        if (trace, middle) != (expected_trace, expected_middle):
            raise ArithmeticError("realized square-stratum coefficients changed")
        elliptic_trace = trace // 2
        panel = control_panel(prime, trace, middle, expected_rank, "realized_square")
        square_p = polynomial_multiply(
            (prime, -elliptic_trace, 1), (prime, -elliptic_trace, 1)
        )
        if weil_polynomial(prime, trace, middle) != square_p:
            raise ArithmeticError("square-stratum P factorization failed")
        expected_q = polynomial_multiply(
            polynomial_multiply((-prime, 1), (-prime, 1)),
            (prime**2, -(elliptic_trace**2 - 2 * prime), 1),
        )
        if primitive_pair_polynomial(prime, trace, middle) != expected_q:
            raise ArithmeticError("square-stratum Q factorization failed")
        panel["marks"] = list(marks)
        panel["trace_two"] = trace_two
        controls.append(panel)
        realized_rows.append(
            {
                "middle": middle,
                "marks": list(marks),
                "minimal_rank": expected_rank,
                "prime": prime,
                "trace": trace,
                "trace_two": trace_two,
            }
        )
    return {
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
            "import": "exact six-place raw correlation and genus-two convention",
        },
        "theorem": {
            "raw_decomposition": (
                "S_n=p^(2n)-6*p^n-21 + H1[p^2 twist,-21] "
                "+ centered-cross-pairs[p twist,-6]"
            ),
            "unique_scalar_notch": "(E-1)*(E-p)*(E-p^2)",
            "memberwise_rank": "2*#distinct(P roots)+2*#distinct(Q roots other than p)",
            "generic_rank": 16,
            "generic_annihilator": "P(T)*p^8 P(T/p^2)*Q(T)*p^4 Q(T/p)",
            "collision_iff": "t^2-4*b+8*p=0 iff P(T)=(T^2-(t/2)T+p)^2",
            "square_stratum_ranks": {"t_nonzero": 8, "t_zero": 6},
            "aliasing_no_go": (
                "a scalar filter killing nuisance roots p,p^2 necessarily kills "
                "geometric cross-pair modes occupying the same roots"
            ),
        },
        "primitive_pair_polynomial": (
            "T^4-(b-2p)T^3+(p*t^2-2p*b+2p^2)T^2-p^2(b-2p)T+p^4"
        ),
        "notch_controls": notch_checks,
        "controls": controls,
        "realized_exceptional_curves": realized_rows,
        "proof_ledger": {
            "raw_six_place_tower": "IMPORTED EXACT",
            "primitive_pair_polynomial": "PROVED EXACT",
            "unique_minimal_cubic_notch": "PROVED EXACT",
            "generic_rank_sixteen": "PROVED OFF THE STATED LOCI",
            "memberwise_rank_formula": "PROVED EXACT",
            "square_collision_classification": "PROVED EXACT",
            "square_stratum_realization_in_six_branch_family": "PROVED BY TWO EXACT BOUNDED CONTROLS",
            "sheaf_or_tate_class_realization": "NOT CLAIMED",
            "rh_or_grh": "NOT PROVED",
        },
        "resource_caps": {
            "control_rows": len(controls),
            "largest_polynomial_degree": 16,
            "largest_quadratic_extension_field": 13**2,
            "maximum_raw_extension_index": MAX_RAW_EXTENSION,
            "maximum_power_sum_exponent": 2 * MAX_RAW_EXTENSION,
            "matrices": 0,
            "quadratic_extension_elements_visited": 11**2 + 13**2,
            "curves_enumerated": len(realized_rows),
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rendered = json.dumps(run(), indent=2, sort_keys=True) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if not args.check:
        print(rendered, end="")


if __name__ == "__main__":
    main()
