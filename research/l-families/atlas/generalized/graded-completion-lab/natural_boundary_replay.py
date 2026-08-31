"""Exact source Euler transforms, logarithmic residues and continuation bounds."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FIXTURE = HERE / "natural_boundary.verification.json"
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
    "coherent_meromorphy": {
        "freeze": "5104c38614461a3e080c93631b855094d0e5961a",
        "path": "research/l-families/atlas/generalized/koszul-analytic-parent/COHERENT_QUADRATIC_PLACE_EULER.md",
        "blob": "2b5b7ef94b0c4c6326a0e06221d01d23475ec58e",
    },
    "finite_ladder_source": {
        "freeze": "c3cdd2528595cbf22c31d88a40c8a611b6385752",
        "path": "research/l-families/atlas/generalized/koszul-analytic-parent/CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md",
        "blob": "7ed7f6d68327df4c5f395142503253b19e8938e4",
    },
}
OWNED = (
    HERE / "FROBENIUS_LADDER_NATURAL_BOUNDARY.md",
    HERE / "NATURAL_BOUNDARY_REPLAY.md",
    HERE / "natural_boundary_replay.py",
    ROOT / "tests/test_graded_completion_natural_boundary.py",
)
MAX_BYTES = 4_000_000
MAX_BITS = 16384


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def integer(value: object, low: int, high: int) -> int:
    need(type(value) is int and low <= value <= high, "integer outside declared cap")
    return value


def parameter(b: object) -> int:
    integer(b, -343, 343)
    need(
        abs(b) > 1 and b % 2 != 0, "nonzero odd source parameter of magnitude above one"
    )
    return b


def bit_guard(value: int | Fraction) -> None:
    value = Fraction(value)
    need(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= MAX_BITS,
        "rational bit cap",
    )


def digest(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def authenticate() -> dict:
    result = {}
    for name, pin in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{pin['freeze']}:{pin['path']}"], cwd=ROOT, text=True
        ).strip()
        need(actual == pin["blob"], "frozen source Git blob mismatch")
        data = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(data) <= MAX_BYTES, "source byte cap")
        need(
            digest((ROOT / pin["path"]).read_bytes()) == digest(data),
            "working source changed",
        )
        result[name] = {**pin, "sha256_lf": digest(data)}
    return result


def source() -> tuple:
    provenance = authenticate()
    name = "natural_boundary_frozen_completion"
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
    integer(n, 1, 256)
    remaining, sign, prime = n, 1, 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            sign = -sign
            if remaining % prime == 0:
                return 0
        prime += 1
    return -sign if remaining > 1 else sign


def multiplicity(j: int) -> int:
    integer(j, 1, 256)
    top = sum(mobius(d) * 4 ** (j // d) for d in range(1, j + 1, 2) if j % d == 0)
    need(top >= 0 and top % (4 * j) == 0, "integral nonnegative source multiplicity")
    answer = top // (4 * j)
    need(j * answer <= 4**j, "source majorant")
    return answer


def residue(b: int, m: int) -> Fraction:
    parameter(b)
    integer(m, 1, 256)
    value = Fraction(
        sum(mobius(d) * b ** (m // d) for d in range(1, m + 1, 2) if m % d == 0),
        4 * m,
    )
    bit_guard(value)
    return value


def multiply(left: list, right: list, cut: int) -> list:
    integer(cut, 0, 64)
    out = [0] * (cut + 1)
    for i, a in enumerate(left[: cut + 1]):
        if a:
            for j, b in enumerate(right[: cut - i + 1]):
                if b:
                    out[i + j] += a * b
    for value in out:
        bit_guard(value)
    return out


def polynomial_power(poly: list, exponent: int, cut: int) -> list:
    integer(exponent, 0, 4**64)
    integer(cut, 0, 64)
    result = [1] + [0] * cut
    while exponent:
        if exponent % 2:
            result = multiply(result, poly, cut)
        poly = multiply(poly, poly, cut)
        exponent //= 2
    return result


def canonical_product(b: int, cut: int = 32, first_grade: int = 2) -> list:
    """Literal factors; no use of logarithmic residue coefficients."""
    parameter(b)
    integer(cut, 0, 64)
    integer(first_grade, 1, 2)
    out = [1] + [0] * cut
    for j in range(first_grade, cut + 1):
        exponent = multiplicity(j)
        factor = [0] * (cut + 1)
        for k in range(min(exponent, cut // j) + 1):
            factor[j * k] = math.comb(exponent, k) * (-b) ** k
        out = multiply(out, factor, cut)
    return out


def polynomial_log_derivative(poly: list) -> list:
    """Entry n is the coefficient of x^(n-1); entry zero is a placeholder."""
    need(
        type(poly) is list and 1 <= len(poly) <= 65 and poly[0] == 1, "unit polynomial"
    )
    need(all(type(value) is int for value in poly), "integer polynomial coefficients")
    out = [0]
    for n in range(1, len(poly)):
        out.append(n * poly[n] - sum(out[k] * poly[n - k] for k in range(1, n)))
        bit_guard(out[-1])
    return out


def direct_log_derivative(b: int, cut: int) -> list:
    parameter(b)
    integer(cut, 0, 64)
    return [0] + [
        -sum(j * multiplicity(j) * b ** (n // j) for j in range(2, n + 1) if n % j == 0)
        for n in range(1, cut + 1)
    ]


def residue_log_derivative(
    b: int, cut: int, restore_missing_grade: bool = True
) -> list:
    parameter(b)
    integer(cut, 0, 64)
    need(type(restore_missing_grade) is bool, "literal missing-grade switch")
    return [Fraction(0)] + [
        -sum(m * residue(b, m) * 4 ** (n // m) for m in range(1, n + 1) if n % m == 0)
        + (b**n if restore_missing_grade else 0)
        for n in range(1, cut + 1)
    ]


def tail_witness(b: int, radius: Fraction) -> dict:
    parameter(b)
    need(type(radius) is Fraction and 0 < radius < 1, "exact rational subdisk radius")
    h = next((k for k in range(1, 129) if 4 * radius ** (k + 1) < 1), None)
    j = next(
        (k for k in range(1, 129) if abs(b) * radius ** (k + 1) < Fraction(1, 2)), None
    )
    need(h is not None and j is not None and j + 8 <= 256, "two-cutoff search cap")
    q = 4 * radius ** (h + 1)
    bound = 2 * abs(b) ** (h + 1) / radius * q ** (j + 1) / (1 - q)
    partial = sum(
        n * multiplicity(n) * abs(b) ** ell * radius ** (n * ell - 1)
        for n in range(j + 1, j + 9)
        for ell in range(h + 1, h + 9)
    )
    need(0 < partial < bound, "original derivative majorant exceeds proved bound")
    bit_guard(bound)
    bit_guard(partial)
    return {
        "b": b,
        "radius": radius,
        "H": h,
        "J": j,
        "4_r_to_H_plus_one": q,
        "abs_b_r_to_J_plus_one": abs(b) * radius ** (j + 1),
        "geometric_derivative_tail_bound": bound,
        "original_positive_majorant_partial_sum": partial,
        "partial_j_count": 8,
        "partial_h_count": 8,
        "unbounded_tail_justified_by_proof_not_partial_sum": True,
    }


def matrix_power(e: int) -> tuple:
    integer(e, 1, 4)
    out, generator = ((1, 0), (0, 1)), ((0, -7), (1, 0))
    for _ in range(e):
        out = tuple(
            tuple(sum(out[i][k] * generator[k][j] for k in range(2)) for j in range(2))
            for i in range(2)
        )
    return out


def proper_frobenius_product(e: int, cut: int = 32) -> list:
    integer(e, 1, 4)
    integer(cut, 0, 64)
    matrix = matrix_power(e)
    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    need(determinant == 7**e, "same Frobenius determinant")
    out = [1] + [0] * cut
    for j in range(2, cut // 2 + 1):
        block = [1] + [0] * cut
        block[2 * j] -= trace
        if 4 * j <= cut:
            block[4 * j] += determinant
        out = multiply(out, polynomial_power(block, multiplicity(j), cut), cut)
    return out


def substitute(poly: list, power: int, cut: int) -> list:
    integer(power, 1, 4)
    integer(cut, 0, 64)
    out = [0] * (cut + 1)
    for n, value in enumerate(poly):
        if power * n > cut:
            break
        out[power * n] = value
    return out


def coordinate_control(e: int, cut: int = 32) -> dict:
    integer(e, 1, 4)
    integer(cut, 8, 64)
    b, power, copies = (-(7**e), 4, 1) if e % 2 else ((-7) ** (e // 2), 2, 2)
    translated = substitute(canonical_product(b, cut // power), power, cut)
    if copies == 2:
        translated = multiply(translated, translated, cut)
    direct = proper_frobenius_product(e, cut)
    need(translated == direct, "actual Frobenius pair versus auxiliary coordinate")
    first = next((i for i in range(1, cut + 1) if direct[i]), None)
    return {
        "extension_degree": e,
        "same_frobenius_matrix": matrix_power(e),
        "auxiliary_b": b,
        "auxiliary_x_equals_z_power": power,
        "copies": copies,
        "first_nonzero_degree": first,
        "coefficients": direct,
    }


def encode(value):
    if type(value) is Fraction:
        return [value.numerator, value.denominator]
    if type(value) in (tuple, list):
        return [encode(item) for item in value]
    if type(value) is dict:
        return {key: encode(item) for key, item in value.items()}
    return value


def json_tree(value) -> bool:
    if type(value) in (type(None), bool, int, float, str):
        return True
    if type(value) is list:
        return all(json_tree(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and json_tree(item) for key, item in value.items())
    return False


def canonical(value) -> str:
    need(json_tree(value), "JSON tree required")
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(left, right) -> bool:
    try:
        return canonical(left) == canonical(right)
    except (TypeError, ValueError):
        return False


def build_payload() -> dict:
    provenance, frozen = source()
    source_rows = []
    for j in range(1, 33):
        row = frozen.source_row(2 * j)
        actual = sum(row["multiplicities"][1:])
        need(actual == multiplicity(j), "actual PBW anti-invariant source multiplicity")
        source_rows.append({"j": j, "source_grade": 2 * j, "a_j": actual, "PBW": row})
    panels = []
    for b in (-7, 7, -49, 49):
        product = canonical_product(b)
        literal = polynomial_log_derivative(product)
        direct = direct_log_derivative(b, 32)
        transformed = residue_log_derivative(b, 32)
        need(literal == direct == transformed, "three independent finite Euler routes")
        dyadic = []
        for v in range(9):
            m, value = 2**v, residue(b, 2**v)
            need(
                value.denominator == 2 ** (v + 2), "exact dyadic monodromy denominator"
            )
            dyadic.append(
                {"v": v, "m": m, "residue": value, "monodromy_order": value.denominator}
            )
        panels.append(
            {
                "b": b,
                "cutoff": 32,
                "literal_product_coefficients": product,
                "log_derivative_coefficient_n_minus_one": literal,
                "residues_m_1_through_32": [residue(b, m) for m in range(1, 33)],
                "dyadic_residues": dyadic,
                "wrong_unrestored_grade_one_log_derivative_at_degree_zero": residue_log_derivative(
                    b, 1, False
                )[1],
                "correct_log_derivative_at_degree_zero": literal[1],
            }
        )
    payload = encode(
        {
            "schema": "frobenius-ladder-logarithmic-natural-boundary-v1",
            "source": provenance,
            "owned_sha256_lf": {
                str(path.relative_to(ROOT)).replace("\\", "/"): digest(
                    path.read_bytes()
                )
                for path in OWNED
            },
            "actual_F7_source": frozen.point_counts(),
            "source_multiplicities": source_rows,
            "euler_transform_panels": panels,
            "two_cutoff_tail_witnesses": [
                tail_witness(b, r)
                for b in (-7, -49)
                for r in (Fraction(1, 2), Fraction(3, 4), Fraction(7, 8))
            ],
            "actual_constant_field_coordinates": [
                coordinate_control(e) for e in range(1, 5)
            ],
            "scope": {
                "all_grade_natural_boundary_proved_not_sampled": True,
                "full_after_uses_frozen_H2_meromorphy": True,
                "full_before_unit_natural_boundary_claimed": False,
                "native_scalar_is_globally_single_valued_on_unit_disk": False,
                "logarithmic_derivative_meromorphic_on_unit_disk": True,
                "determinant_line_topological_nontriviality_claimed": False,
            },
        }
    )
    payload["proof_object_sha256"] = hashlib.sha256(
        canonical(payload).encode()
    ).hexdigest()
    return payload


def check_payload(candidate: object) -> None:
    need(
        strict_equal(candidate, build_payload()),
        "strict natural-boundary replay differs",
    )


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
    print("Frobenius ladder natural-boundary replay PASS")


if __name__ == "__main__":
    main()
