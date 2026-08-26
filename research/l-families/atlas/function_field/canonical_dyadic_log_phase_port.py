#!/usr/bin/env python3
"""Exact uniform-log-phase port of the literal canonical dyadic wavelet."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Iterable
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "canonical_dyadic_log_phase_port.json"
NOTE_PATH = HERE / "CANONICAL_DYADIC_LOG_PHASE_PORT.md"
TEST_PATH = ROOT / "tests" / "test_canonical_dyadic_log_phase_port.py"

SOURCE_LOCKS = {
    "research/l-families/atlas/function_field/CANONICAL_DETECTOR_NORM_LATTICE_OBSTRUCTION.md": "f282f0be91ea4eb72a515fba8808a33101cf2bf1401bae5eec24bbbafd335857",
    "research/l-families/atlas/function_field/canonical_detector_norm_lattice_obstruction.py": "17b4956c621a600a8f9ed5ee6d6e84b526c7ba709080e89d70e25f7109ca9b60",
    "research/l-families/atlas/function_field/canonical_detector_norm_lattice_obstruction.json": "3a2aa44f759686017495b4b2102f93d6891454856cf66d34cc9ce3750b798fa4",
    "tests/test_canonical_detector_norm_lattice_obstruction.py": "c4de4512b2538030d1b637c0a72ceb7ccc4a3bfd4d023dd6e4fec65a2d1f3d0c",
    "research/integrated/wavelet_xd/README.md": "6a04ae3f85bcf00929079dd845f12175bb4e81e88eb20997ca7b38f17c67702f",
}

SYMBOLIC_OPERATION_CAP = 4096

# Each pair denotes a+b*sqrt(2).  Entries are ordered by S_(2**j), j=0..3.
Quad = tuple[Fraction, Fraction]
Affine = tuple[Quad, Quad]  # constant term, alpha coefficient
K1_COEFFICIENTS: tuple[Quad, ...] = (
    (Fraction(1), Fraction(0)),
    (Fraction(-2), Fraction(-1)),
    (Fraction(1), Fraction(2)),
    (Fraction(0), Fraction(-1)),
)
ZERO_QUAD: Quad = (Fraction(0), Fraction(0))
ZERO_AFFINE: Affine = (ZERO_QUAD, ZERO_QUAD)
ONE_AFFINE: Affine = ((Fraction(1), Fraction(0)), ZERO_QUAD)
ALPHA: Affine = (ZERO_QUAD, (Fraction(1), Fraction(0)))


class Budget:
    """Count exact symbolic term updates, not processor instructions."""

    def __init__(self) -> None:
        self.used = 0

    def spend(self, amount: int = 1) -> None:
        self.used += amount
        if self.used > SYMBOLIC_OPERATION_CAP:
            raise RuntimeError("symbolic-operation cap exceeded")


def sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def assert_sources() -> None:
    for relative, expected in SOURCE_LOCKS.items():
        path = ROOT / relative
        if not path.is_file() or sha256_lf(path) != expected:
            raise RuntimeError(f"locked dyadic source drifted: {relative}")


def qadd(left: Quad, right: Quad) -> Quad:
    return left[0] + right[0], left[1] + right[1]


def qneg(value: Quad) -> Quad:
    return -value[0], -value[1]


def qscale(value: Quad, scalar: Fraction | int) -> Quad:
    factor = Fraction(scalar)
    return value[0] * factor, value[1] * factor


def qmul(left: Quad, right: Quad) -> Quad:
    # (a+b*s)(c+d*s)=(ac+2bd)+(ad+bc)s, s^2=2.
    return (
        left[0] * right[0] + 2 * left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def aadd(left: Affine, right: Affine) -> Affine:
    return qadd(left[0], right[0]), qadd(left[1], right[1])


def aneg(value: Affine) -> Affine:
    return qneg(value[0]), qneg(value[1])


def ascale_quad(value: Affine, scalar: Quad) -> Affine:
    return qmul(value[0], scalar), qmul(value[1], scalar)


def affine_integer_minus_alpha(integer: int, multiple: int) -> Affine:
    return (
        (Fraction(integer), Fraction(0)),
        (Fraction(-multiple), Fraction(0)),
    )


def affine_alpha_minus_integer(multiple: int, integer: int) -> Affine:
    return aneg(affine_integer_minus_alpha(integer, multiple))


def sum_quads(values: Iterable[Quad]) -> Quad:
    total = ZERO_QUAD
    for value in values:
        total = qadd(total, value)
    return total


def sum_affines(values: Iterable[Affine]) -> Affine:
    total = ZERO_AFFINE
    for value in values:
        total = aadd(total, value)
    return total


def phase_average_symbol(
    floors: tuple[int, int, int, int], budget: Budget | None = None
) -> tuple[Affine, ...]:
    """Integrate sum_j c_j z^ceil(j*alpha-t) on one floor chamber."""
    max_degree = max(floor + 1 for floor in floors)
    coefficients = [ZERO_AFFINE for _ in range(max_degree + 1)]
    for j, (floor, coefficient) in enumerate(zip(floors, K1_COEFFICIENTS, strict=True)):
        # beta_j=j*alpha-floor.  The lower shift floor has mass 1-beta_j;
        # the upper shift floor+1 has mass beta_j.
        lower_mass = affine_integer_minus_alpha(floor + 1, j)
        upper_mass = affine_alpha_minus_integer(j, floor)
        coefficients[floor] = aadd(
            coefficients[floor], ascale_quad(lower_mass, coefficient)
        )
        coefficients[floor + 1] = aadd(
            coefficients[floor + 1], ascale_quad(upper_mass, coefficient)
        )
        if budget is not None:
            budget.spend(2)
    while coefficients and coefficients[-1] == ZERO_AFFINE:
        coefficients.pop()
    return tuple(coefficients)


def phase_cells(
    floors: tuple[int, int, int, int],
    threshold_order: tuple[int, ...],
    budget: Budget | None = None,
) -> tuple[tuple[Affine, Quad], ...]:
    """Return exact (cell length, D=sum c_j*d_j) pairs a.e. in phase."""
    thresholds = {j: affine_alpha_minus_integer(j, floors[j]) for j in threshold_order}
    endpoints = [ZERO_AFFINE]
    endpoints.extend(thresholds[j] for j in threshold_order)
    endpoints.append(ONE_AFFINE)

    constant = sum_quads(
        qscale(coefficient, floors[j]) for j, coefficient in enumerate(K1_COEFFICIENTS)
    )
    active = set(threshold_order)
    cells: list[tuple[Affine, Quad]] = []
    for index in range(len(endpoints) - 1):
        length = aadd(endpoints[index + 1], aneg(endpoints[index]))
        value = qadd(constant, sum_quads(K1_COEFFICIENTS[j] for j in active))
        cells.append((length, value))
        if index < len(threshold_order):
            active.remove(threshold_order[index])
        if budget is not None:
            budget.spend()
    return tuple(cells)


def cell_mean(cells: tuple[tuple[Affine, Quad], ...]) -> Affine:
    return sum_affines(ascale_quad(length, value) for length, value in cells)


def cell_energy(cells: tuple[tuple[Affine, Quad], ...]) -> Affine:
    return sum_affines(
        ascale_quad(length, qmul(value, value)) for length, value in cells
    )


REGIMES = {
    # At q=4 the first cell has zero length; the same a.e. formula applies.
    "q_3_4": {
        "integer_q": "3<=q<=4",
        "floors_j_alpha": (0, 0, 1, 1),
        "threshold_order": (2, 1, 3),
    },
    "q_5_7": {
        "integer_q": "5<=q<=7",
        "floors_j_alpha": (0, 0, 0, 1),
        "threshold_order": (3, 1, 2),
    },
    # At q=8 the last threshold is t=1; this is a.e. identical to floor(3a)=1.
    "q_ge_8": {
        "integer_q": "q>=8",
        "floors_j_alpha": (0, 0, 0, 0),
        "threshold_order": (1, 2, 3),
    },
}

EXPECTED_AVERAGE_SYMBOLS: dict[str, tuple[Affine, ...]] = {
    "q_3_4": (
        (((Fraction(-1), Fraction(-1))), (Fraction(2), Fraction(1))),
        (((Fraction(2), Fraction(2))), (Fraction(-4), Fraction(-2))),
        (((Fraction(-1), Fraction(-1))), (Fraction(2), Fraction(1))),
    ),
    "q_5_7": (
        (((Fraction(0), Fraction(1))), (Fraction(0), Fraction(-3))),
        (((Fraction(0), Fraction(-2))), (Fraction(0), Fraction(6))),
        (((Fraction(0), Fraction(1))), (Fraction(0), Fraction(-3))),
    ),
    "q_ge_8": (),
}

EXPECTED_ENERGIES: dict[str, Affine] = {
    "q_3_4": (
        (Fraction(6), Fraction(6)),
        (Fraction(-6), Fraction(-8)),
    ),
    "q_5_7": (
        (Fraction(0), Fraction(-2)),
        (Fraction(6), Fraction(8)),
    ),
    "q_ge_8": (
        (Fraction(0), Fraction(0)),
        (Fraction(6), Fraction(2)),
    ),
}


def derivative_at_one(symbol: tuple[Affine, ...], order: int) -> Affine:
    terms: list[Affine] = []
    for exponent, coefficient in enumerate(symbol):
        if exponent < order:
            continue
        falling = 1
        for integer in range(exponent - order + 1, exponent + 1):
            falling *= integer
        terms.append(ascale_quad(coefficient, (Fraction(falling), Fraction(0))))
    return sum_affines(terms)


def fraction_json(value: Fraction) -> int | str:
    if value.denominator == 1:
        return value.numerator
    return f"{value.numerator}/{value.denominator}"


def quad_json(value: Quad) -> dict[str, int | str]:
    return {
        "rational": fraction_json(value[0]),
        "sqrt2": fraction_json(value[1]),
    }


def affine_json(value: Affine) -> dict[str, object]:
    return {
        "basis": "constant + alpha * coefficient; alpha=log_q(2)",
        "constant": quad_json(value[0]),
        "alpha_coefficient": quad_json(value[1]),
    }


def symbol_json(symbol: tuple[Affine, ...]) -> list[dict[str, object]]:
    return [
        {"degree_shift": exponent, "coefficient": affine_json(coefficient)}
        for exponent, coefficient in enumerate(symbol)
    ]


def cells_json(cells: tuple[tuple[Affine, Quad], ...]) -> list[dict[str, object]]:
    return [
        {"phase_length": affine_json(length), "D_value": quad_json(value)}
        for length, value in cells
    ]


def no_floats(value: object) -> None:
    if isinstance(value, float):
        raise TypeError("claim payload contains a float")
    if isinstance(value, dict):
        for key, item in value.items():
            no_floats(key)
            no_floats(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            no_floats(item)


def build_fixture() -> dict[str, object]:
    assert_sources()
    budget = Budget()
    regime_rows: dict[str, object] = {}
    for name, data in REGIMES.items():
        floors = data["floors_j_alpha"]
        order = data["threshold_order"]
        if not isinstance(floors, tuple) or not isinstance(order, tuple):
            raise TypeError("internal regime data malformed")
        symbol = phase_average_symbol(floors, budget)
        cells = phase_cells(floors, order, budget)
        mean = cell_mean(cells)
        energy = cell_energy(cells)
        if symbol != EXPECTED_AVERAGE_SYMBOLS[name]:
            raise ArithmeticError(f"unexpected phase-average symbol in {name}")
        if mean != ZERO_AFFINE:
            raise ArithmeticError(f"linear-test phase mean is nonzero in {name}")
        if energy != EXPECTED_ENERGIES[name]:
            raise ArithmeticError(f"unexpected phase energy in {name}")
        if derivative_at_one(symbol, 0) != ZERO_AFFINE:
            raise ArithmeticError(f"constant cancellation failed in {name}")
        if derivative_at_one(symbol, 1) != ZERO_AFFINE:
            raise ArithmeticError(f"linear cancellation failed in {name}")
        budget.spend(6)
        regime_rows[name] = {
            "integer_q": data["integer_q"],
            "a.e._phase_cells": cells_json(cells),
            "phase_average_symbol_coefficients_by_z_power": symbol_json(symbol),
            "phase_average_has_double_zero_at_z_1": True,
            "degree_linear_test_mean": affine_json(mean),
            "degree_linear_test_L2_energy": affine_json(energy),
        }

    native_symbol = tuple(((coefficient, ZERO_QUAD)) for coefficient in K1_COEFFICIENTS)
    fixture: dict[str, object] = {
        "schema": "canonical-dyadic-log-phase-port-v1",
        "ring": {
            "coefficient_ring": "Q(sqrt(2))[alpha]",
            "alpha": "log_q(2)",
            "numeric_log_or_sqrt_approximations_in_claim_payload": False,
        },
        "theorem": {
            "phase_shift": "d_j(t)=ceil(j*alpha-t) for 0<=t<1",
            "mean_shift": "integral_0^1 d_j(t) dt = j*alpha",
            "double_zero": (
                "the uniformly phase-averaged symbol has value and first "
                "derivative zero at z=1"
            ),
            "odd_q_collapse": {
                "q=3": "[((2+sqrt(2))*alpha-(1+sqrt(2)))]*(1-z)^2",
                "q=5,7": "sqrt(2)*(1-3*alpha)*(1-z)^2",
                "odd q>=9": "zero operator",
            },
            "q_ge_8_fluctuation": (
                "the zero averaged operator retains degree-linear phase energy "
                "2*(3+sqrt(2))*alpha"
            ),
        },
        "q_2_native_control": {
            "alpha": "1",
            "phase_independent": True,
            "unaveraged_native_symbol_coefficients_by_z_power": symbol_json(
                native_symbol
            ),
            "degree_linear_test_mean": affine_json(ZERO_AFFINE),
            "degree_linear_test_L2_energy": affine_json(ZERO_AFFINE),
        },
        "regimes": regime_rows,
        "scope": {
            "symbolic_term_operations_used": budget.used,
            "symbolic_term_operation_cap": SYMBOLIC_OPERATION_CAP,
            "L_function_family_evaluated": False,
            "XD_HCNC_or_BPOE_arithmetic_proved": False,
            "source_faithful_family_port_proved": False,
            "operator_theorem_on_norm_step_extensions_only": True,
            "rh_or_grh_proved": False,
        },
        "provenance": {
            "source_locks_sha256_lf": SOURCE_LOCKS,
            "producer_sha256_lf": sha256_lf(Path(__file__)),
            "note_sha256_lf": sha256_lf(NOTE_PATH),
            "test_sha256_lf": sha256_lf(TEST_PATH),
        },
    }
    no_floats(fixture)
    return fixture


def render(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    rendered = render(build_fixture())
    if args.check:
        if (
            not OUTPUT_PATH.is_file()
            or OUTPUT_PATH.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("canonical dyadic log-phase fixture drifted")
        print("PASS_CANONICAL_DYADIC_LOG_PHASE_PORT")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
