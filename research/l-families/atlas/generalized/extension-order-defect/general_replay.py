"""Source-bound BEFORE-radius and invariant-generator-base controls."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIXTURE = HERE / "general.verification.json"
PINS = {
    "after_proof": {
        "freeze": "075f9b203aefefb4a29f3279b6de1c4127093af6",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/ARITHMETIC_RADIUS_DICHOTOMY.md",
        "blob": "cf8d794a35c2dc88eb86c1a6f62f6a06cbe3d03f",
    },
    "after_producer": {
        "freeze": "075f9b203aefefb4a29f3279b6de1c4127093af6",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/arithmetic_radius_replay.py",
        "blob": "f33245de6552337df00f65b0bf78621fa6d6d028",
    },
    "after_artifact": {
        "freeze": "075f9b203aefefb4a29f3279b6de1c4127093af6",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/arithmetic_radius.verification.json",
        "blob": "88360519800f8ba2f8f4de6d8e62b0a0190ea9e3",
    },
    "infinite_proof": {
        "freeze": "b3fde737e790e38ae15c20ce0858e72104c55550",
        "path": "research/l-families/atlas/generalized/extension-order-defect/INFINITE_EXTENSION_ORDER.md",
        "blob": "e506acc486ab34d292538fd500cf1ec5cdd81364",
    },
    "finite_proof": {
        "freeze": "0018b73f60e42bc793d172c381547de34322d8ca",
        "path": "research/l-families/atlas/generalized/extension-order-defect/EXTENSION_ORDER_DEFECT.md",
        "blob": "dfb7fcbf1115846664fa99e71116a3635b14d7a0",
    },
}
OWNED = (
    HERE / "GENERAL_FIELD_RAMIFICATION_EXPONENT.md",
    HERE / "INVARIANT_GENERATOR_BASE.md",
    HERE / "GENERAL_REPLAY.md",
    HERE / "general_replay.py",
    ROOT / "tests/test_extension_order_general.py",
)
PRIMES = (5, 7, 11, 13, 17, 19, 23, 29, 31)
SELECTED = (
    (5, 1, 0),
    (7, 1, 0),
    (11, 1, 3),
    (11, 1, 4),
    (13, 1, 5),
    (13, 4, 1),
    (31, 1, 2),
)
MAX_BYTES = 12_000_000


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    need(type(value) is int and low <= value <= high, "integer outside declared cap")
    return value


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate() -> dict:
    out = {}
    for key, pin in PINS.items():
        need(all(value != "PENDING" for value in pin.values()), "source freeze pending")
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
        out[key] = {**pin, "sha256_lf": digest(frozen)}
    return out


def source() -> tuple:
    provenance = authenticate()
    name = "general_extension_after_source"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, ROOT / PINS["after_producer"]["path"]
        )
        need(spec is not None and spec.loader is not None, "source import unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
    module = sys.modules[name]
    module.authenticate()
    data = (ROOT / PINS["after_artifact"]["path"]).read_bytes()
    need(len(data) < MAX_BYTES, "source artifact byte cap")
    artifact = json.loads(data)
    need(
        artifact["schema"] == "actual-after-arithmetic-radius-v1",
        "wrong source artifact",
    )
    return provenance, module, artifact


def pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def nonnegative_integer(value: Fraction) -> bool:
    return value.denominator == 1 and value >= 0


def classify_before(row: dict) -> dict:
    need(type(row) is dict, "source row required")
    fields = (
        "p",
        "aE",
        "aD",
        "tZ",
        "split",
        "splitPlus",
        "splitMinus",
        "splitZero",
        "oldPlus",
        "oldMinus",
        "delta",
    )
    need(
        all(type(row.get(key)) is int for key in fields), "strict integer source fields"
    )
    p = row["p"]
    need(p in PRIMES, "declared source prime required")
    for key in ("split", "splitPlus", "splitMinus", "splitZero", "oldPlus", "oldMinus"):
        integer(row[key], 0, p)
    gp, gm, g0 = (row[key] for key in ("splitPlus", "splitMinus", "splitZero"))
    rp, rm, delta = (row[key] for key in ("oldPlus", "oldMinus", "delta"))
    need(g0 in (0, 1) and delta == int(p % 3 == 1), "zero/infinity source distinction")
    need(row["split"] == gp + gm + g0 and (rp + rm) % 2 == 0, "source partitions")
    trace = row["tZ"]
    need(
        trace == row["aD"] + 2 * row["aE"]
        and trace == p + 1 - 6 * row["split"] - 3 * (rp + rm) - 2 * delta,
        "proper Galois source identity",
    )
    need(trace % 6 == 0, "source trace six-divisibility")
    alpha = Fraction(trace, 12)
    sigma_plus = -Fraction(rp - rm, 4) - Fraction(delta, 3)
    sigma_minus = -Fraction(rm - rp, 4) - Fraction(delta, 3)
    rho_plus, rho_minus = gm + alpha + sigma_plus, gp + alpha + sigma_minus
    need(
        rho_plus == gm + Fraction(p + 1, 12) - Fraction(row["split"] + rp + delta, 2),
        "positive exponent count identity",
    )
    need(
        rho_minus == gp + Fraction(p + 1, 12) - Fraction(row["split"] + rm + delta, 2),
        "negative exponent count identity",
    )
    after_large = nonnegative_integer(gm + alpha) and nonnegative_integer(gp + alpha)
    sqrt_term = rp + rm + delta > 0
    before_large = not sqrt_term and after_large
    direct_first_test = (
        not sqrt_term
        and nonnegative_integer(rho_plus)
        and nonnegative_integer(rho_minus)
    )
    need(
        before_large == direct_first_test,
        "Puiseux criterion versus after-source criterion",
    )
    if delta:
        need(
            rho_plus.denominator != 1 and rho_minus.denominator != 1,
            "split infinity cubic component",
        )
    gamma = Fraction(row["aD"] ** 2 + 2 * row["aE"] ** 2 - 6 * p, 24)
    need((4 * gamma).denominator == 1, "second real exponent quarter lattice")
    second_controls = []
    if before_large:
        for difference in range(-2, 3):
            exponent = gamma - Fraction(difference, 4) - Fraction(1, 6)
            need(exponent.denominator != 1, "second-circle quarter/sixth obstruction")
            second_controls.append(
                {
                    "hypothetical_degree_two_sign_difference": difference,
                    "exponent_mod_integer": pair(exponent),
                    "actual_pattern_assigned": False,
                }
            )
    return {
        "alpha": pair(alpha),
        "sigma_plus": pair(sigma_plus),
        "sigma_minus": pair(sigma_minus),
        "rho_plus": pair(rho_plus),
        "rho_minus": pair(rho_minus),
        "positive_sqrt_coefficient_present": sqrt_term,
        "rational_old_count": rp + rm,
        "split_infinity": bool(delta),
        "after_radius": "1/sqrt(2)" if after_large else "1/2",
        "before_radius": "1/sqrt(2)" if before_large else "1/2",
        "extension_order_changes_radius": after_large and not before_large,
        "second_circle_quarter_sixth_controls": second_controls,
    }


def matrix_multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    need(
        len(a) == len(b) == 2 and all(len(row) == 2 for row in a + b),
        "two-dimensional source matrix",
    )
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)
    ]


def standard_source() -> dict:
    cycle, reflection = [[-1, -1], [1, 0]], [[0, 1], [1, 0]]
    identity = [[1, 0], [0, 1]]
    square = matrix_multiply(cycle, cycle)
    need(matrix_multiply(square, cycle) == identity, "actual three-cycle")
    need(matrix_multiply(reflection, reflection) == identity, "actual reflection")
    need(
        matrix_multiply(matrix_multiply(reflection, cycle), reflection) == square,
        "S3 conjugation relation",
    )
    need(cycle[0][0] + cycle[1][1] == -1, "standard cycle trace")
    return {
        "basis": ["e1-e0", "e2-e0"],
        "cycle": cycle,
        "reflection": reflection,
        "quadratic_eigenbasis": [[1, 1], [1, -1]],
        "quadratic_eigenbasis_determinant": -2,
    }


def invariant_monomials(kind: str, grade: int) -> dict:
    need(kind in ("C2", "C3"), "inertia source required")
    integer(grade, 0, 32)
    monomials, normal_forms = [], []
    if grade % 2 == 0:
        total = grade // 2
        for a in range(total + 1):
            b = total - a
            if kind == "C2" and b % 2 == 0:
                monomials.append([a, b])
                normal_forms.append([a, b // 2])
            elif kind == "C3" and (a - b) % 3 == 0:
                minimum = min(a, b)
                monomials.append([a, b])
                normal_forms.append([minimum, (a - minimum) // 3, (b - minimum) // 3])
    need(
        len({tuple(item) for item in normal_forms}) == len(monomials),
        "invariant normal-form injectivity",
    )
    if kind == "C2":
        fixed_input = int(grade % 2 == 0)
        trace = len(monomials)
        quotient_fixed_base = int(grade % 4 == 0)
    else:
        fixed_input = int(grade == 0)
        trace = sum(a == b for a, b in monomials)
        quotient_fixed_base = len(monomials)
    return {
        "inertia": kind,
        "grade": grade,
        "monomials": monomials,
        "normal_forms": normal_forms,
        "dimension": len(monomials),
        "residual_trace": trace,
        "fixed_input_dimension": fixed_input,
        "quotient_by_positive_fixed_inputs_dimension": quotient_fixed_base,
    }


def cubic_normal_product(left: tuple, right: tuple) -> tuple:
    need(
        type(left) is tuple and type(right) is tuple and len(left) == len(right) == 3,
        "C3 normal-form triples",
    )
    for item in left + right:
        integer(item, 0, 16)
    need(
        left[1] * left[2] == right[1] * right[2] == 0,
        "normal forms have only one cubic direction",
    )
    h, p, q = (a + b for a, b in zip(left, right, strict=True))
    remove = min(p, q)
    return h + 3 * remove, p - remove, q - remove


def anti_module_generators(grade: int) -> dict:
    """Every negative Segre eigenmonomial is covered by a negative coordinate."""
    integer(grade, 1, 6)
    negative_coordinates = [
        (i, j)
        for i, vi in enumerate((1, -1))
        for j, wj in enumerate((1, 1, -1))
        if vi * wj == -1
    ]
    covered = []
    for v0 in range(grade + 1):
        v = (v0, grade - v0)
        for w0 in range(grade + 1):
            for w1 in range(grade - w0 + 1):
                w = (w0, w1, grade - w0 - w1)
                if (v[1] + w[2]) % 2 == 0:
                    continue
                choices = [(i, j) for i, j in negative_coordinates if v[i] and w[j]]
                need(bool(choices), "negative monomial missing a degree-one generator")
                i, j = choices[0]
                rest_v, rest_w = list(v), list(w)
                rest_v[i] -= 1
                rest_w[j] -= 1
                need(
                    (rest_v[1] + rest_w[2]) % 2 == 0,
                    "generator quotient is not invariant",
                )
                covered.append(
                    {"v": list(v), "w": list(w), "chosen_negative_coordinate": [i, j]}
                )
    return {
        "grade": grade,
        "negative_degree_one_coordinates": [
            list(item) for item in negative_coordinates
        ],
        "dimension": len(covered),
        "coverage": covered,
    }


def base_controls() -> dict:
    source_matrix = standard_source()
    rows = [
        invariant_monomials(kind, grade) for kind in ("C2", "C3") for grade in range(33)
    ]
    for row in rows:
        n = row["grade"]
        if row["inertia"] == "C2":
            expected = sum(
                1
                for a in range(n // 2 + 1)
                for b in range(n // 4 + 1)
                if 2 * a + 4 * b == n
            )
        else:
            expected = sum(
                1
                for h in range(n // 4 + 1)
                for a in range(n // 6 + 1)
                for b in range(n // 6 + 1)
                if a * b == 0 and 4 * h + 6 * a + 6 * b == n
            )
            need(
                row["residual_trace"] == int(n % 4 == 0),
                "nonsplit invariant-ring trace",
            )
        need(row["dimension"] == expected, "literal invariant ring versus presentation")
    need(cubic_normal_product((0, 1, 0), (0, 0, 1)) == (3, 0, 0), "p3*q3=(pq)^3")
    coverage = [anti_module_generators(n) for n in range(1, 7)]
    need(coverage[0]["dimension"] == 3, "three minimal anti-invariant generators")
    return {
        "standard_source": source_matrix,
        "invariant_ring_rows": rows,
        "anti_module_source_coverage": coverage,
        "repaired_C_minimal_generators": {"0": 1, "3": 3},
        "repaired_C_rank": 2,
        "original_Q_becomes_module_over_larger_base": False,
        "C2_obstruction": {
            "one_in_B": True,
            "new_base_y_squared_in_B": False,
            "product_preserves_B": False,
        },
        "all_grade_finiteness_and_rank_proved_not_inferred": True,
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
    provenance, after, artifact = source()
    counts = {"1/2": 0, "1/sqrt(2)": 0}
    changes = 0
    panels, selected, indexed = [], [], {}
    for panel in artifact["panels"]:
        local_counts = {"1/2": 0, "1/sqrt(2)": 0}
        local_changes = 0
        for bound in panel["rows"]:
            row = {key: bound[key] for key in after.RAW_KEYS}
            result = classify_before(row)
            need(
                result["after_radius"] == bound["analytic"]["after_radius"],
                "independent after-criterion readback",
            )
            local_counts[result["before_radius"]] += 1
            local_changes += int(result["extension_order_changes_radius"])
            indexed[(row["p"], row["A"], row["B"])] = (row, result)
        for key, count in local_counts.items():
            counts[key] += count
        changes += local_changes
        panels.append(
            {
                "p": panel["p"],
                "parameter_count": panel["count"],
                "before_radius_counts": local_counts,
                "extension_order_changes": local_changes,
            }
        )
    need(
        sum(counts.values()) == artifact["total"] == 3044,
        "complete source atlas coverage",
    )
    for params in SELECTED:
        row, result = indexed[params]
        need(
            strict_equal(row, after.raw_row(*params)),
            "selected primitive source recount",
        )
        selected.append(
            {
                "row": row,
                "before": result,
                "proper_closure_recount": after.closure_control(*params),
            }
        )
    need(
        indexed[(7, 1, 0)][1]["extension_order_changes_radius"],
        "actual F7 extension-order radius change",
    )
    need(
        indexed[(5, 1, 0)][1]["before_radius"] == "1/sqrt(2)",
        "declared exceptional first-circle source",
    )
    return {
        "schema": "general-before-extension-radius-v1",
        "source": provenance,
        "owned_sha256_lf": {
            str(path.relative_to(ROOT)).replace("\\", "/"): digest(path.read_bytes())
            for path in OWNED
        },
        "total": artifact["total"],
        "panels": panels,
        "before_radius_counts": counts,
        "extension_order_changes": changes,
        "selected_actual_sources": selected,
        "generator_base_controls": base_controls(),
        "scope": "Actual same-generic-source BEFORE/AFTER radius comparison and invariant-generator-base finiteness",
        "not_claimed": [
            "different generic algebras",
            "ordinary L of boundary cokernel equals Hilbert ratio",
            "Q is a module over repaired base",
            "all-grade theorem from finite atlas",
            "larger ordinary trace-class domain",
            "number-field or archimedean transfer",
            "RH",
        ],
    }


def check_payload(candidate: object) -> None:
    need(strict_equal(candidate, build_payload()), "strict BEFORE/base replay differs")


def main() -> None:
    parser = argparse.ArgumentParser()
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--write", action="store_true")
    action.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        encoded = (
            json.dumps(build_payload(), indent=2, sort_keys=True, allow_nan=False)
            + "\n"
        ).encode()
        need(len(encoded) <= MAX_BYTES, "artifact byte cap")
        FIXTURE.write_bytes(encoded)
    else:
        data = FIXTURE.read_bytes()
        need(len(data) <= MAX_BYTES, "artifact byte cap")
        check_payload(json.loads(data))
    print("general BEFORE extension-order replay PASS")


if __name__ == "__main__":
    main()
