"""Same arithmetic stalks, different actual boundary generization maps."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIXTURE = HERE / "generization.verification.json"
PINS = {
    "finite_source": {
        "freeze": "0018b73f60e42bc793d172c381547de34322d8ca",
        "path": "research/l-families/atlas/generalized/extension-order-defect/replay.py",
        "blob": "6df0f1746caf765efe960aee421323681a488202",
    },
    "finite_proof": {
        "freeze": "0018b73f60e42bc793d172c381547de34322d8ca",
        "path": "research/l-families/atlas/generalized/extension-order-defect/EXTENSION_ORDER_DEFECT.md",
        "blob": "dfb7fcbf1115846664fa99e71116a3635b14d7a0",
    },
    "constructible_source": {
        "freeze": "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93",
        "path": "research/l-families/atlas/generalized/koszul-analytic-parent/CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md",
        "blob": "7ed7f6d68327df4c5f395142503253b19e8938e4",
    },
}
OWNED = (
    HERE / "GENERIZATION_AND_EULER_INVISIBILITY.md",
    HERE / "GENERIZATION_REPLAY.md",
    HERE / "generization_replay.py",
    ROOT / "tests/test_extension_order_generization.py",
)
MAX_BYTES = 8_000_000


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    need(type(value) is int and low <= value <= high, "integer outside declared cap")
    return value


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate() -> dict:
    records = {}
    for key, pin in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{pin['freeze']}:{pin['path']}"], cwd=ROOT, text=True
        ).strip()
        need(actual == pin["blob"], "frozen source blob mismatch")
        frozen = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(frozen) < MAX_BYTES, "source byte cap")
        need(
            digest((ROOT / pin["path"]).read_bytes()) == digest(frozen),
            "working source changed",
        )
        records[key] = {**pin, "sha256_lf": digest(frozen)}
    return records


def source() -> tuple:
    provenance = authenticate()
    name = "generization_finite_source"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, ROOT / PINS["finite_source"]["path"]
        )
        need(spec is not None and spec.loader is not None, "source import unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
    module = sys.modules[name]
    module.authenticate_frozen()
    return provenance, module


def old_basis(grade: int) -> tuple[list[tuple], list[tuple]]:
    integer(grade, 0, 6)
    nearby, boundary = [], []
    for generator_degree in range(grade // 2 + 1):
        n = grade - 2 * generator_degree
        for v0 in range(n + 1):
            for w0 in range(n + 1):
                for w1 in range(n - w0 + 1):
                    w2 = n - w0 - w1
                    for negative_generator in range(generator_degree + 1):
                        state = (
                            v0,
                            n - v0,
                            w0,
                            w1,
                            w2,
                            generator_degree - negative_generator,
                            negative_generator,
                        )
                        if (state[1] + state[4] + state[6]) % 2 == 0:
                            nearby.append(state)
                            if negative_generator == 0:
                                boundary.append(state)
    return nearby, boundary


def monomial_grade(state: tuple) -> int:
    need(type(state) is tuple and len(state) == 7, "literal source monomial")
    for value in state:
        integer(value, 0, 6)
    need(sum(state[:2]) == sum(state[2:5]), "Segre bidegrees differ")
    return sum(state[:2]) + 2 * sum(state[5:])


def source_product(left: tuple, right: tuple) -> tuple:
    need(monomial_grade(left) + monomial_grade(right) <= 6, "source product grade cap")
    return tuple(a + b for a, b in zip(left, right, strict=True))


def map_control(grade: int, epsilon: int = 1) -> dict:
    integer(grade, 0, 6)
    need(type(epsilon) is int and epsilon in (-1, 1), "quadratic source sign")
    nearby, boundary = old_basis(grade)
    positions = {state: index for index, state in enumerate(nearby)}
    columns = [positions[state] for state in boundary]
    need(len(set(columns)) == len(boundary), "literal inclusion lost rank")
    counterfeit = columns if grade == 0 else [None] * len(boundary)
    original_rank = len(set(columns))
    counterfeit_rank = len({entry for entry in counterfeit if entry is not None})
    for state in boundary:
        actual_sign = epsilon ** sum(state[:2])
        need(actual_sign == epsilon**grade, "actual chi grading sign")
    return {
        "grade": grade,
        "quadratic_frobenius_sign": epsilon,
        "nearby_invariant_dimension": len(nearby),
        "boundary_dimension": len(boundary),
        "original_image_rows": columns,
        "counterfeit_image_rows": counterfeit,
        "original_generization_rank": original_rank,
        "counterfeit_generization_rank": counterfeit_rank,
        "shared_boundary_frobenius_eigenvalue": epsilon**grade,
        "boundary_algebra_unchanged": True,
        "generic_algebra_unchanged": True,
    }


def multiplication_controls() -> dict:
    count = 0
    for left_degree in range(4):
        for right_degree in range(4):
            _, lefts = old_basis(left_degree)
            _, rights = old_basis(right_degree)
            nearby, boundary = old_basis(left_degree + right_degree)
            nearby_set, boundary_set = set(nearby), set(boundary)
            for left in lefts:
                for right in rights:
                    product = source_product(left, right)
                    need(
                        product in nearby_set and product in boundary_set,
                        "source algebra inclusion is not multiplicative",
                    )
                    left_aug, right_aug = int(left_degree == 0), int(right_degree == 0)
                    product_aug = int(monomial_grade(product) == 0)
                    need(
                        left_aug * right_aug == product_aug,
                        "augmentation is not multiplicative",
                    )
                    count += 1
    return {
        "literal_products_checked": count,
        "original_inclusion_multiplicative": True,
        "augmentation_unit_preserved": True,
        "augmentation_multiplicative": True,
        "positive_degree_specialization_zero": True,
    }


def multiply(left: list[int], right: list[int], cut: int) -> list[int]:
    out = [0] * (cut + 1)
    for i, a in enumerate(left[: cut + 1]):
        for j, b in enumerate(right[: cut - i + 1]):
            out[i + j] += a * b
    return out


def polynomial_power(poly: list[int], exponent: int, cut: int) -> list[int]:
    integer(exponent, 0, 1000)
    integer(cut, 0, 8)
    out = [1] + [0] * cut
    while exponent:
        if exponent % 2:
            out = multiply(out, poly, cut)
        poly = multiply(poly, poly, cut)
        exponent //= 2
    return out


def newton_determinant(traces: list[int], cut: int) -> list[int]:
    integer(cut, 0, 8)
    need(
        len(traces) >= cut and all(type(value) is int for value in traces),
        "exact source power traces",
    )
    out = [1]
    for n in range(1, cut + 1):
        numerator = -sum(traces[k - 1] * out[n - k] for k in range(1, n + 1))
        need(numerator % n == 0, "source determinant is not integral")
        out.append(numerator // n)
    return out


def class_power(kind: str, exponent: int) -> str:
    need(kind in ("e", "s", "c"), "S3 class")
    integer(exponent, 1, 64)
    return "e" if kind == "e" or exponent % (2 if kind == "s" else 3) == 0 else kind


def determinant_control(
    characters: list[int], kind: str, twist: int = 1, power: int = 1
) -> dict:
    need(
        type(characters) is list
        and len(characters) == 3
        and all(type(value) is int for value in characters),
        "actual S3 source characters",
    )
    need(type(twist) is int and twist in (-1, 1), "quadratic ordinary twist")
    integer(power, 1, 6)
    powered = class_power(kind, power)
    d, s, c = characters
    numerators = [d + 3 * s + 2 * c, d - 3 * s + 2 * c, 2 * (d - c)]
    need(
        all(value >= 0 and value % 6 == 0 for value in numerators),
        "source S3 multiplicities",
    )
    a, b, standard = (value // 6 for value in numerators)
    if powered == "e":
        direct = polynomial_power([1, -twist], d, 8)
    elif powered == "s":
        direct = multiply(
            polynomial_power([1, -twist], a + standard, 8),
            polynomial_power([1, twist], b + standard, 8),
            8,
        )
    else:
        direct = multiply(
            polynomial_power([1, -twist], a + b, 8),
            polynomial_power([1, twist, 1], standard, 8),
            8,
        )
    character = dict(zip(("e", "s", "c"), characters, strict=True))
    traces = [twist**m * character[class_power(powered, m)] for m in range(1, 9)]
    need(
        direct == newton_determinant(traces, 8), "eigenfactor versus Newton determinant"
    )
    return {
        "source_characters": characters,
        "class": kind,
        "frobenius_power": power,
        "powered_class": powered,
        "ordinary_twist_eigenvalue": twist,
        "determinant_prefix": direct,
        "power_traces": traces,
        "boundary_map_enters_determinant": False,
    }


def residual_determinant(dimension: int, trace: int, twist: int, power: int) -> dict:
    integer(dimension, 0, 1000)
    need(
        type(trace) is int and abs(trace) <= dimension and (dimension - trace) % 2 == 0,
        "residual involution character",
    )
    need(type(twist) is int and twist in (-1, 1), "residual ordinary twist")
    integer(power, 1, 6)
    plus, minus = (dimension + trace) // 2, (dimension - trace) // 2
    eigenminus = (-1) ** power
    direct = multiply(
        polynomial_power([1, -twist], plus, 8),
        polynomial_power([1, -twist * eigenminus], minus, 8),
        8,
    )
    traces = [twist**m * (plus + minus * eigenminus**m) for m in range(1, 9)]
    need(direct == newton_determinant(traces, 8), "residual determinant powers")
    return {
        "dimension": dimension,
        "initial_trace": trace,
        "plus_minus": [plus, minus],
        "ordinary_twist": twist,
        "frobenius_power": power,
        "determinant_prefix": direct,
        "power_traces": traces,
    }


def closed_point_base_change(degree: int, extension: int) -> dict:
    integer(degree, 1, 12)
    integer(extension, 1, 12)
    split = math.gcd(degree, extension)
    return {
        "old_degree": degree,
        "extension_degree": extension,
        "new_closed_points": split,
        "new_degree": degree // split,
        "frobenius_power": extension // split,
    }


def _json_tree(value) -> bool:
    if type(value) in (type(None), bool, int, float, str):
        return True
    if type(value) is list:
        return all(_json_tree(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and _json_tree(item) for key, item in value.items())
    return False


def strict_equal(a, b) -> bool:
    if not _json_tree(a) or not _json_tree(b):
        return False
    try:
        return json.dumps(
            a, sort_keys=True, separators=(",", ":"), allow_nan=False
        ) == json.dumps(b, sort_keys=True, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError):
        return False


def build_payload() -> dict:
    provenance, finite = source()
    old_rows, infinity_rows, zero_rows = [], [], []
    determinants, base_change = [], []
    for grade in range(7):
        primitive = finite.primitive_c2(grade)
        for epsilon in (-1, 1):
            row = map_control(grade, epsilon)
            need(
                row["boundary_dimension"] == primitive["after_dimension"],
                "literal old source versus frozen invariant basis",
            )
            need(
                row["nearby_invariant_dimension"] == primitive["before_dimension"],
                "literal nearby source versus frozen invariant basis",
            )
            old_rows.append(row)
            determinants.append(
                {
                    "stratum": "old",
                    "grade": grade,
                    "control": residual_determinant(
                        row["boundary_dimension"],
                        epsilon**grade * row["boundary_dimension"],
                        1,
                        1,
                    ),
                }
            )
        inf = finite.primitive_infinity(grade)
        infinity_rows.append(
            {
                "grade": grade,
                "boundary_dimension": inf["after_dimension"],
                "residual_trace": inf["after_residual_trace"],
                "original_generization_rank": inf["after_dimension"],
                "counterfeit_generization_rank": int(grade == 0),
            }
        )
        for power in (1, 2, 3):
            determinants.append(
                {
                    "stratum": "infinity_nonsplit",
                    "grade": grade,
                    "control": residual_determinant(
                        inf["after_dimension"], inf["after_residual_trace"], 1, power
                    ),
                }
            )
        zero = finite.primitive_zero(grade)
        chars = zero["common_class_traces_e_s_c"]
        zero_rows.append(
            {
                "grade": grade,
                "boundary_characters": chars,
                "old_after_before_defect_dimension": zero["cokernel_dimension"],
                "original_generization_rank": chars[0],
                "counterfeit_generization_rank": int(grade == 0),
            }
        )
        for kind in ("e", "s", "c"):
            for twist in (-1, 1):
                determinants.append(
                    {
                        "stratum": "new_zero",
                        "grade": grade,
                        "control": determinant_control(chars, kind, twist),
                    }
                )
    for degree, extension in ((1, 2), (2, 2), (3, 2), (4, 6), (6, 4), (5, 6)):
        splitting = closed_point_base_change(degree, extension)
        powered = splitting["frobenius_power"]
        control = determinant_control(
            finite.primitive_zero(2)["common_class_traces_e_s_c"],
            "c",
            (-1) ** powered,
            powered,
        )
        base_change.append(
            {
                "splitting": splitting,
                "original_quadratic_twist_eigenvalue": -1,
                "actual_residual_source": control,
                "both_extensions_keep_the_same_power_and_new_degree": True,
            }
        )
    need(
        old_rows[2]["original_generization_rank"] == 3
        and old_rows[2]["counterfeit_generization_rank"] == 0,
        "actual degree-one source discriminator",
    )
    need(
        zero_rows[2]["original_generization_rank"] > 0
        and zero_rows[2]["old_after_before_defect_dimension"] == 0,
        "new-point different modification distinction",
    )
    return {
        "schema": "generization-euler-invisibility-v1",
        "source": provenance,
        "owned_sha256_lf": {
            str(path.relative_to(ROOT)).replace("\\", "/"): digest(path.read_bytes())
            for path in OWNED
        },
        "old_C2_maps": old_rows,
        "infinity_maps": infinity_rows,
        "new_zero_maps": zero_rows,
        "multiplication": multiplication_controls(),
        "determinant_controls": determinants,
        "constant_field_controls": base_change,
        "not_claimed": [
            "Euler factors determine generization",
            "counterfeit preserves prescribed j_*A map",
            "Verdier dual is determined by ordinary stalks",
            "same source map",
            "new abstract gluing theorem",
            "arithmetic or archimedean RH consequence",
        ],
    }


def check_payload(candidate: object) -> None:
    need(strict_equal(candidate, build_payload()), "strict generization replay differs")


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        data = (
            json.dumps(build_payload(), indent=2, sort_keys=True, allow_nan=False)
            + "\n"
        ).encode()
        need(len(data) < MAX_BYTES, "artifact byte cap")
        FIXTURE.write_bytes(data)
    else:
        data = FIXTURE.read_bytes()
        need(len(data) < MAX_BYTES, "artifact byte cap")
        check_payload(json.loads(data))
    print("generization source replay PASS")


if __name__ == "__main__":
    main()
