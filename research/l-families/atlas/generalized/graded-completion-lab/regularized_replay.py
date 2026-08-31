"""Actual Frobenius powers and bounded canonical regularized determinants."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIXTURE = HERE / "regularized.verification.json"
PINS = {
    "completion_proof": {
        "freeze": "64075f1a3f81529f217dee1ae139656dfb9356f3",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/MATHEMATICS.md",
        "blob": "c0e6fe3bb24cbec75cee01ddac6f26ff5358264b",
    },
    "completion_producer": {
        "freeze": "64075f1a3f81529f217dee1ae139656dfb9356f3",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/replay.py",
        "blob": "18e370b9393d1a907b54c78bd66cc9450f3a624f",
    },
    "after_proof": {
        "freeze": "075f9b203aefefb4a29f3279b6de1c4127093af6",
        "path": "research/l-families/atlas/generalized/graded-completion-lab/ARITHMETIC_RADIUS_DICHOTOMY.md",
        "blob": "cf8d794a35c2dc88eb86c1a6f62f6a06cbe3d03f",
    },
    "before_proof": {
        "freeze": "b3fde737e790e38ae15c20ce0858e72104c55550",
        "path": "research/l-families/atlas/generalized/extension-order-defect/INFINITE_EXTENSION_ORDER.md",
        "blob": "e506acc486ab34d292538fd500cf1ec5cdd81364",
    },
}
OWNED = (
    HERE / "REGULARIZED_FROBENIUS_TOWER.md",
    HERE / "REGULARIZED_PREREGISTRATION.md",
    HERE / "REGULARIZED_REPLAY.md",
    HERE / "regularized_replay.py",
    ROOT / "tests/test_graded_completion_regularized.py",
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
    result = {}
    for name, pin in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{pin['freeze']}:{pin['path']}"], cwd=ROOT, text=True
        ).strip()
        need(actual == pin["blob"], "source Git blob mismatch")
        data = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(data) < MAX_BYTES, "source byte cap")
        need(
            digest((ROOT / pin["path"]).read_bytes()) == digest(data),
            "working source changed",
        )
        result[name] = {**pin, "sha256_lf": digest(data)}
    return result


def source() -> tuple:
    provenance = authenticate()
    name = "regularized_completion_source"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, ROOT / PINS["completion_producer"]["path"]
        )
        need(spec is not None and spec.loader is not None, "source import unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
    module = sys.modules[name]
    module.source_bytes()
    return provenance, module


def mobius(n: int) -> int:
    integer(n, 1, 64)
    result, prime = 1, 2
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            result = -result
            if n % prime == 0:
                return 0
        prime += 1
    return -result if n > 1 else result


def multiplicity(n: int) -> int:
    integer(n, 2, 64)
    need(n % 2 == 0, "even source grade")
    top = sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1, 2) if n % d == 0)
    need(top % (2 * n) == 0 and top >= 0, "source anti-invariant dimension")
    return top // (2 * n)


def frobenius_trace(exponent: int) -> int:
    integer(exponent, 0, 256)
    if exponent == 0:
        return 2
    previous, current = 2, 0
    for _ in range(1, exponent):
        previous, current = current, -7 * previous
    return current


def matrix_multiply(left: tuple, right: tuple) -> tuple:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def frobenius_matrix(exponent: int) -> tuple:
    integer(exponent, 0, 64)
    out, generator = ((1, 0), (0, 1)), ((0, -7), (1, 0))
    for _ in range(exponent):
        out = matrix_multiply(out, generator)
    return out


def validate(e: int, p: int, grade_cap: int, cut: int) -> None:
    integer(e, 1, 8)
    integer(p, 1, 8)
    integer(grade_cap, 4, 16)
    need(grade_cap % 2 == 0, "even generator cutoff beginning at four")
    integer(cut, 0, 64)


def multiply(left: list, right: list, cut: int) -> list:
    out = [Fraction(0)] * (cut + 1)
    for i, a in enumerate(left[: cut + 1]):
        if a:
            for j, b in enumerate(right[: cut - i + 1]):
                if b:
                    out[i + j] += a * b
    return out


def polynomial_power(poly: list, exponent: int, cut: int) -> list:
    integer(exponent, 0, 1_000_000)
    integer(cut, 0, 64)
    result = [Fraction(1)] + [Fraction(0)] * cut
    while exponent:
        if exponent % 2:
            result = multiply(result, poly, cut)
        poly = multiply(poly, poly, cut)
        exponent //= 2
    return result


def formal_exp(logarithm: list, cut: int) -> list:
    integer(cut, 0, 64)
    need(len(logarithm) == cut + 1 and logarithm[0] == 0, "normalized formal logarithm")
    out = [Fraction(1)]
    for n in range(1, cut + 1):
        out.append(sum(k * logarithm[k] * out[n - k] for k in range(1, n + 1)) / n)
    return out


@lru_cache(maxsize=64)
def _proper_product(e: int, grade_cap: int, cut: int) -> tuple:
    out = [Fraction(1)] + [Fraction(0)] * cut
    matrix = frobenius_matrix(e)
    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    need(
        trace == frobenius_trace(e) and determinant == 7**e,
        "matrix Frobenius trace/determinant",
    )
    for n in range(4, grade_cap + 1, 2):
        block = [Fraction(0)] * (cut + 1)
        block[0] = 1
        if n <= cut:
            block[n] = -trace
        if 2 * n <= cut:
            block[2 * n] = determinant
        out = multiply(out, polynomial_power(block, multiplicity(n), cut), cut)
    return tuple(out)


def proper_product(e: int, grade_cap: int, cut: int) -> list:
    validate(e, 1, grade_cap, cut)
    return list(_proper_product(e, grade_cap, cut))


def counterterm(e: int, first: int, stop: int, grade_cap: int, cut: int) -> list:
    validate(e, first, grade_cap, cut)
    integer(stop, first, 9)
    out = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        for h in range(first, min(stop, cut // n + 1)):
            out[n * h] += Fraction(multiplicity(n) * frobenius_trace(e * h), h)
    return out


def regularized_direct(e: int, p: int, grade_cap: int = 16, cut: int = 64) -> list:
    validate(e, p, grade_cap, cut)
    head = proper_product(e, grade_cap, cut)
    exponential = formal_exp(counterterm(e, 1, p, grade_cap, cut), cut)
    return multiply(head, exponential, cut)


def regularized_log(
    e: int, p: int, grade_cap: int = 16, cut: int = 64, norm_degree: int = 1
) -> list:
    validate(e, p, grade_cap, cut)
    integer(norm_degree, 1, 4)
    out = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        for h in range(p, cut // n + 1):
            sieve = norm_degree if h % norm_degree == 0 else 0
            out[n * h] -= Fraction(sieve * multiplicity(n) * frobenius_trace(e * h), h)
    return out


def substituted(poly: list, degree: int, cut: int) -> list:
    integer(degree, 1, 4)
    integer(cut, 0, 64)
    out = [Fraction(0)] * (cut + 1)
    for n, value in enumerate(poly):
        if n * degree <= cut:
            out[n * degree] = value
    return out


def first_difference(left: list, right: list) -> dict | None:
    for n, (a, b) in enumerate(zip(left, right, strict=True)):
        if a != b:
            return {"degree": n, "left": a, "right": b}
    return None


def radius_control(e: int, p: int) -> dict:
    validate(e, p, 4, 0)
    h0 = p if e % 2 == 0 else p + p % 2
    observed = next(h for h in range(p, p + 2) if frobenius_trace(e * h) != 0)
    need(h0 == observed, "recurrence first surviving trace order")
    eta = Fraction(frobenius_trace(e * h0), 4 * h0)
    need(eta == Fraction((-7) ** (e * h0 // 2), 2 * h0), "exact branch exponent")
    need(eta.denominator != 1, "noninteger branch exponent")
    trace = frobenius_trace(e)
    alpha = Fraction(3 * trace, 12)
    if e % 2 == 0:
        need(alpha.denominator == 2, "even field-extension half-integral alpha")
    else:
        need(alpha == 0, "odd extension has zero elliptic trace")
    before_mod_integer = alpha - Fraction(1, 3) if e % 2 else alpha - Fraction(4, 3)
    need(before_mod_integer.denominator != 1, "actual split-infinity BEFORE branch")
    return {
        "field_extension_exponent": e,
        "Q": 7**e,
        "regularization_order": p,
        "first_nonzero_trace_order": h0,
        "branch_exponent": eta,
        "scalar_radius": f"2^(-1/{h0})",
        "ordinary_Sp_radius": f"2^(-1/{p})",
        "same_germ_as_next_order_due_to_odd_trace": e % 2 == 1 and p % 2 == 1,
        "full_after_radius": "1/sqrt(2)" if e % 2 else "1/2",
        "full_before_radius": "1/2",
        "before_exponent_mod_integer": before_mod_integer,
    }


def cyclic_norm_control(e: int, p: int, degree: int, cut: int = 64) -> dict:
    integer(degree, 2, 4)
    validate(e * degree, p, 16, cut)
    validate(e, p * degree, 16, cut)
    lhs = substituted(regularized_direct(e * degree, p, 16, cut // degree), degree, cut)
    rhs_log = regularized_log(e, p * degree, 16, cut, degree)
    rhs = formal_exp(rhs_log, cut)
    need(lhs == rhs, "same-Frobenius cyclic norm with changed order")
    return {
        "e": e,
        "p": p,
        "degree": degree,
        "right_order": p * degree,
        "coefficient_cutoff": cut,
        "left_and_right_coefficients": lhs,
        "root_of_unity_sieve_applied_to_Frobenius_power_not_total_grade": True,
    }


def transition_control(e: int, p: int, q: int, cut: int = 64) -> dict:
    validate(e, p, 16, cut)
    integer(q, p + 1, 8)
    low, high = regularized_direct(e, p, 16, cut), regularized_direct(e, q, 16, cut)
    transition = formal_exp(counterterm(e, p, q, 16, cut), cut)
    need(high == multiply(low, transition, cut), "finite trace counterterm transition")
    return {
        "e": e,
        "p": p,
        "q": q,
        "cutoff": cut,
        "first_changed_coefficient": first_difference(low, high),
        "multiplicative_identity_verified_without_dividing_at_zeros": True,
    }


def encode(value):
    if type(value) is Fraction:
        return [value.numerator, value.denominator]
    if type(value) in (tuple, list):
        return [encode(item) for item in value]
    if type(value) is dict:
        return {key: encode(item) for key, item in value.items()}
    return value


def _json_tree(value) -> bool:
    if type(value) in (type(None), bool, int, float, str):
        return True
    if type(value) is list:
        return all(_json_tree(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and _json_tree(item) for key, item in value.items())
    return False


def strict_equal(left, right) -> bool:
    if not _json_tree(left) or not _json_tree(right):
        return False
    try:
        return json.dumps(
            left, sort_keys=True, separators=(",", ":"), allow_nan=False
        ) == json.dumps(right, sort_keys=True, separators=(",", ":"), allow_nan=False)
    except (TypeError, ValueError):
        return False


def build_payload() -> dict:
    provenance, frozen = source()
    source_rows = []
    for n in range(2, 65, 2):
        row = frozen.source_row(n)
        actual = sum(row["multiplicities"][1:])
        need(actual == multiplicity(n), "PBW versus odd-divisor anti-invariant source")
        deviation = Fraction(2 * actual) - Fraction(2**n, n)
        bound = Fraction(2 ** (n // 3 + 1) - 2, n)
        need(abs(deviation) <= bound, "all-grade error control at bounded source grade")
        source_rows.append(
            {
                "grade": n,
                "actual_multiplicity": actual,
                "PBW_characters": row["characters"],
                "twice_multiplicity_deviation": deviation,
                "proved_error_bound": bound,
                "included_in_operator": n >= 4,
            }
        )
    powers = []
    for e in range(1, 9):
        matrix = frobenius_matrix(e)
        trace = matrix[0][0] + matrix[1][1]
        need(trace == frobenius_trace(e), "literal same-Frobenius power")
        powers.append(
            {
                "e": e,
                "matrix_in_fixed_algebraic_basis": matrix,
                "trace": trace,
                "determinant": 7**e,
                "matrix_basis_not_declared_orthonormal_eigenbasis": True,
            }
        )
    regularizations = []
    for e in range(1, 9):
        for p in range(1, 9):
            direct = regularized_direct(e, p)
            logarithmic = formal_exp(regularized_log(e, p), 64)
            need(
                direct == logarithmic,
                "finite canonical product versus formal trace logarithm",
            )
            row = radius_control(e, p)
            expected_first = 4 * row["first_nonzero_trace_order"]
            first = next(n for n, value in enumerate(direct[1:], 1) if value)
            need(
                first == expected_first, "first omitted-grade convention or trace order"
            )
            regularizations.append(
                {
                    **row,
                    "generator_cutoff": 16,
                    "coefficient_cutoff": 64,
                    "first_nonzero_coefficient_degree": first,
                    "coefficients": direct,
                }
            )
    norms = [
        cyclic_norm_control(e, p, d) for e in (1, 2) for p in (1, 2) for d in (2, 3, 4)
    ]
    transitions = [
        transition_control(e, p, q)
        for e, p, q in (
            (1, 1, 2),
            (1, 2, 3),
            (1, 3, 4),
            (2, 1, 2),
            (2, 2, 4),
            (3, 5, 8),
        )
    ]
    right_order = substituted(regularized_direct(2, 2, 16, 32), 2, 64)
    wrong_order = multiply(regularized_direct(1, 2), regularized_direct(1, 2), 64)
    wrong = first_difference(right_order, wrong_order)
    need(
        wrong is not None
        and wrong["degree"] == 8
        and wrong["left"] == 0
        and wrong["right"] == 28,
        "unchanged-order base-change counterfeit",
    )
    limit = regularized_direct(2, 8, 16, 28)
    need(limit == [1] + [0] * 28, "coefficientwise regularization limit control")
    return encode(
        {
            "schema": "actual-regularized-frobenius-tower-v1",
            "source": provenance,
            "owned_sha256_lf": {
                str(path.relative_to(ROOT)).replace("\\", "/"): digest(
                    path.read_bytes()
                )
                for path in OWNED
            },
            "actual_F7_source": frozen.point_counts(),
            "source_multiplicities": source_rows,
            "same_Frobenius_powers": powers,
            "regularizations": regularizations,
            "cyclic_norms": norms,
            "transitions": transitions,
            "wrong_unchanged_order_base_change": wrong,
            "coefficient_limit_control": {
                "e": 2,
                "p": 8,
                "cutoff": 28,
                "coefficients": limit,
                "limit_is_one_not_native_multiplier": True,
            },
            "not_claimed": [
                "operator S_p radius inferred from finite traces",
                "scalar normalization preserved for all p",
                "finite H_N transition factors are units without cutoff condition",
                "counterterms extend original source frame globally",
                "new determinant-line theory",
                "archimedean or RH consequence",
            ],
        }
    )


def check_payload(candidate: object) -> None:
    need(strict_equal(candidate, build_payload()), "strict regularized replay differs")


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.write:
        data = (
            json.dumps(build_payload(), sort_keys=True, indent=2, allow_nan=False)
            + "\n"
        ).encode()
        need(len(data) <= MAX_BYTES, "artifact byte cap")
        FIXTURE.write_bytes(data)
    else:
        data = FIXTURE.read_bytes()
        need(len(data) <= MAX_BYTES, "artifact byte cap")
        check_payload(json.loads(data))
    print("regularized Frobenius tower replay PASS")


if __name__ == "__main__":
    main()
