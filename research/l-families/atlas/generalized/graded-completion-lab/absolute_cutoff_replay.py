"""Actual Frobenius canonical factors selected by an absolute trace cutoff."""

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
FIXTURE = HERE / "absolute_cutoff.verification.json"
FREEZE = "32c4a249d188612729f093815b4a445b796893a0"
PREFIX = "research/l-families/atlas/generalized/graded-completion-lab/"
PINS = {
    "genus_proof": {
        "freeze": FREEZE,
        "path": PREFIX + "GRADING_GENUS_COMPLETION.md",
        "blob": "d133bba85a2f335b9f795fb041df4b4d204de27b",
    },
    "genus_producer": {
        "freeze": FREEZE,
        "path": PREFIX + "grading_genus_replay.py",
        "blob": "0830bfca1ef77db26f754b59aedb03805af95042",
    },
}
OWNED = (
    HERE / "ABSOLUTE_FROBENIUS_CUTOFF.md",
    HERE / "ABSOLUTE_CUTOFF_PREREGISTRATION.md",
    HERE / "ABSOLUTE_CUTOFF_REPLAY.md",
    HERE / "absolute_cutoff_replay.py",
    ROOT / "tests/test_graded_completion_absolute_cutoff.py",
)
MAX_BYTES = 4_000_000


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
    name = "absolute_cutoff_frozen_genus"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, ROOT / PINS["genus_producer"]["path"]
        )
        need(spec is not None and spec.loader is not None, "source import unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
    module = sys.modules[name]
    _, _, original = module.source()
    return provenance, module, original


def absolute_order(n: int, policy: str = "linear", slope: int = 1) -> int:
    integer(n, 4, 64)
    need(n % 2 == 0, "even source grade")
    need(
        type(policy) is str and policy in ("linear", "nonmonotone"),
        "declared absolute cutoff",
    )
    integer(slope, 1, 2)
    if policy == "linear":
        return slope * n
    need(slope == 1, "slope belongs to linear cutoff")
    return n if n % 4 == 0 else n // 2


def relative_order(cutoff: int, e: int) -> int:
    integer(cutoff, 1, 384)
    integer(e, 1, 36)
    return (cutoff + e - 1) // e


def surviving_order(e: int, threshold: int) -> int:
    integer(e, 1, 36)
    integer(threshold, 1, 384)
    return threshold if e % 2 == 0 else threshold + threshold % 2


def phase(value: object) -> Fraction:
    need(type(value) in (int, Fraction), "exact rational phase required")
    value = Fraction(value)
    need(
        abs(value) <= 8 and value.denominator <= 64,
        "phase magnitude or denominator cap",
    )
    return value


def validate(
    e: int, policy: str, slope: int, grade_cap: int, cut: int, xi: object
) -> Fraction:
    integer(e, 1, 6)
    integer(grade_cap, 4, 16)
    need(grade_cap % 2 == 0, "even generator cutoff")
    integer(cut, 0, 64)
    absolute_order(4, policy, slope)
    return phase(xi)


def proper_product(g, e: int, grade_cap: int, cut: int, xi: object = 1) -> list:
    xi = validate(e, "linear", 1, grade_cap, cut, xi)
    matrix = g.frobenius_matrix(e)
    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    need(
        trace == g.trace(e) and determinant == 7**e,
        "actual source characteristic polynomial",
    )
    out = [Fraction(1)] + [Fraction(0)] * cut
    for n in range(4, grade_cap + 1, 2):
        block = [Fraction(1)] + [Fraction(0)] * cut
        if n <= cut:
            block[n] -= xi * trace
        if 2 * n <= cut:
            block[2 * n] += xi * xi * determinant
        out = g.multiply(out, g.polynomial_power(block, g.multiplicity(n), cut), cut)
    return out


def canonical_product(
    g,
    e: int,
    policy: str = "linear",
    slope: int = 1,
    grade_cap: int = 16,
    cut: int = 64,
    xi: object = 1,
) -> list:
    xi = validate(e, policy, slope, grade_cap, cut, xi)
    counterterm = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        threshold = relative_order(absolute_order(n, policy, slope), e)
        for h in range(1, min(threshold, cut // n + 1)):
            counterterm[n * h] += (
                Fraction(g.multiplicity(n) * g.trace(e * h), h) * xi**h
            )
    return g.multiply(
        proper_product(g, e, grade_cap, cut, xi), g.formal_exp(counterterm, cut), cut
    )


def absolute_log(
    g,
    e: int,
    policy: str = "linear",
    slope: int = 1,
    grade_cap: int = 16,
    cut: int = 64,
    xi: object = 1,
    norm_degree: int = 1,
) -> list:
    xi = validate(e, policy, slope, grade_cap, cut, xi)
    integer(norm_degree, 1, 3)
    out = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        for h in range(1, cut // n + 1):
            if e * h >= absolute_order(n, policy, slope) and h % norm_degree == 0:
                out[n * h] -= (
                    Fraction(norm_degree * g.multiplicity(n) * g.trace(e * h), h)
                    * xi**h
                )
    return out


def frame_log(
    g,
    e: int,
    first: tuple,
    second: tuple,
    grade_cap: int = 16,
    cut: int = 64,
    xi: object = 1,
    norm_degree: int = 1,
) -> list:
    need(
        type(first) is tuple
        and type(second) is tuple
        and len(first) == len(second) == 2,
        "two declared absolute policies",
    )
    xi = validate(e, *first, grade_cap, cut, xi)
    validate(e, *second, grade_cap, cut, xi)
    integer(norm_degree, 1, 3)
    out = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        p = relative_order(absolute_order(n, *first), e)
        q = relative_order(absolute_order(n, *second), e)
        sign = 1 if q >= p else -1
        for h in range(min(p, q), min(max(p, q), cut // n + 1)):
            if h % norm_degree == 0:
                out[n * h] += (
                    Fraction(sign * norm_degree * g.multiplicity(n) * g.trace(e * h), h)
                    * xi**h
                )
    return out


def block_product(g, e: int, n: int, threshold: int, cut: int = 64) -> list:
    integer(e, 1, 6)
    integer(n, 4, 16)
    need(n % 2 == 0, "even source block")
    integer(threshold, 1, 128)
    integer(cut, 0, 64)
    factor = [Fraction(1)] + [Fraction(0)] * cut
    if n <= cut:
        factor[n] -= g.trace(e)
    if 2 * n <= cut:
        factor[2 * n] += 7**e
    logarithm = [Fraction(0)] * (cut + 1)
    for h in range(1, min(threshold, cut // n + 1)):
        logarithm[n * h] += Fraction(g.multiplicity(n) * g.trace(e * h), h)
    return g.multiply(
        g.polynomial_power(factor, g.multiplicity(n), cut),
        g.formal_exp(logarithm, cut),
        cut,
    )


def norm_control(
    g,
    e: int,
    degree: int,
    policy: str = "linear",
    slope: int = 1,
    xi: object = 1,
    cut: int = 64,
) -> dict:
    integer(e, 1, 2)
    integer(degree, 2, 3)
    xi = phase(xi)
    left = g.substituted(
        canonical_product(
            g, e * degree, policy, slope, cut=cut // degree, xi=xi**degree
        ),
        degree,
        cut,
    )
    right = g.formal_exp(
        absolute_log(g, e, policy, slope, cut=cut, xi=xi, norm_degree=degree), cut
    )
    need(left == right, "same absolute-cutoff Frobenius norm")
    return {
        "e": e,
        "degree": degree,
        "policy": policy,
        "slope": slope,
        "phase": xi,
        "left_and_right_coefficients": left,
        "absolute_cutoff_sequence_unchanged": True,
    }


def threshold_controls() -> list:
    rows = []
    for p1 in range(1, 17):
        effective = p1 + p1 % 2
        for e in range(1, 7):
            direct = relative_order(p1, e)
            effective_threshold = relative_order(effective, e)
            need(
                surviving_order(e, direct) == surviving_order(e, effective_threshold),
                "actual zero-trace cutoff ambiguity",
            )
            for d in range(1, 7):
                need(
                    relative_order(direct, d) == relative_order(p1, e * d),
                    "literal ceiling composition",
                )
            rows.append(
                {
                    "p_at_e1": p1,
                    "effective_even_absolute_cutoff": effective,
                    "e": e,
                    "literal_threshold": direct,
                    "effective_threshold": effective_threshold,
                    "same_first_surviving_order": surviving_order(e, direct),
                }
            )
    return rows


def normalization_controls(g) -> dict:
    one = canonical_product(g, 1)
    two = canonical_product(g, 2)
    need(
        one[16] == -49 and one[24] == Fraction(686, 3),
        "original absolute cutoff agrees with genus at e1",
    )
    need(
        two[8] == -98 and two[12] == Fraction(1372, 3),
        "constant-field coherent normalization",
    )
    need(
        g.substituted(two, 2, 64) == g.multiply(one, one, 64),
        "odd-source quadratic norm is a square",
    )
    wrong = g.canonical_product(2)
    difference = g.first_difference(two, wrong)
    need(
        difference == {"degree": 8, "left": -98, "right": 0},
        "extension-relative slope counterfeit",
    )
    return {
        "e1_degree16": one[16],
        "e1_degree24": one[24],
        "e2_degree8": two[8],
        "e2_degree12": two[12],
        "wrong_fixed_relative_slope_first_difference": difference,
        "native_normalization_recovered": False,
    }


def encode(value):
    if type(value) is Fraction:
        return [value.numerator, value.denominator]
    if type(value) in (list, tuple):
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
    provenance, g, original = source()
    policies = (("linear", 1), ("linear", 2), ("nonmonotone", 1))
    panels = []
    for e in range(1, 5):
        for policy, slope in policies:
            product = canonical_product(g, e, policy, slope)
            log = absolute_log(g, e, policy, slope)
            need(
                product == g.formal_exp(log, 64),
                "proper-factor cutoff versus absolute trace selection",
            )
            panels.append(
                {
                    "e": e,
                    "policy": policy,
                    "slope": slope,
                    "absolute_cutoffs": [
                        absolute_order(n, policy, slope) for n in range(4, 17, 2)
                    ],
                    "relative_thresholds": [
                        relative_order(absolute_order(n, policy, slope), e)
                        for n in range(4, 17, 2)
                    ],
                    "coefficients": product,
                    "log_coefficients": log,
                }
            )
    norms = [
        norm_control(g, e, d, *policy)
        for e in (1, 2)
        for d in (2, 3)
        for policy in policies
    ]
    phase_controls = [norm_control(g, 1, d, xi=xi) for d in (2, 3) for xi in (-1, 0, 2)]
    frame_changes = []
    first, second = policies[0], policies[1]
    for e in (1, 2):
        correction = frame_log(g, e, first, second)
        need(
            canonical_product(g, e, *second)
            == g.multiply(
                canonical_product(g, e, *first), g.formal_exp(correction, 64), 64
            ),
            "oriented absolute frame change",
        )
        for d in (2, 3):
            left = g.substituted(frame_log(g, e * d, first, second, cut=64 // d), d, 64)
            right = frame_log(g, e, first, second, norm_degree=d)
            need(left == right, "additive frame-change Frobenius norm")
        frame_changes.append(
            {
                "e": e,
                "log_of_second_over_first": correction,
                "counterterm_norm_degrees_checked": [2, 3],
            }
        )
    block_controls = []
    for e in range(1, 5):
        for first_cutoff, second_cutoff in ((3, 4), (4, 6)):
            first_threshold, second_threshold = (
                relative_order(first_cutoff, e),
                relative_order(second_cutoff, e),
            )
            first_block = block_product(g, e, 4, first_threshold)
            second_block = block_product(g, e, 4, second_threshold)
            same = surviving_order(e, first_threshold) == surviving_order(
                e, second_threshold
            )
            need(
                (first_block == second_block) == same,
                "actual block cutoff classification at phase one",
            )
            block_controls.append(
                {
                    "e": e,
                    "grade": 4,
                    "absolute_cutoffs": [first_cutoff, second_cutoff],
                    "relative_thresholds": [first_threshold, second_threshold],
                    "same_block": same,
                    "first_difference": g.first_difference(first_block, second_block),
                }
            )
    payload = encode(
        {
            "schema": "absolute-frobenius-cutoff-v1",
            "source": provenance,
            "owned_sha256_lf": {
                str(path.relative_to(ROOT)).replace("\\", "/"): digest(
                    path.read_bytes()
                )
                for path in OWNED
            },
            "actual_F7_source": original.point_counts(),
            "same_source_multiplicities_even4_through16": [
                g.multiplicity(n) for n in range(4, 17, 2)
            ],
            "absolute_cutoff_panels": panels,
            "same_family_norms": norms,
            "rational_phase_norms": phase_controls,
            "literal_and_effective_thresholds": threshold_controls(),
            "actual_block_classification_controls": block_controls,
            "coherent_frame_changes": frame_changes,
            "normalization_control": normalization_controls(g),
            "scope": {
                "same_absolute_sequence_under_constant_field_norm": True,
                "all_grade_scalar_identity_classified_without_block_hypothesis": False,
                "unrestricted_sheaf_source_uniqueness_claimed": False,
                "phase_one_zero_divisor_and_natural_boundary": True,
                "arbitrary_phase_natural_boundary_claimed": False,
                "zero_phase_product_is_one": True,
                "native_integral_normalization_recovered": False,
                "full_place_Euler_basechange_law_claimed": False,
                "new_field_enumeration": False,
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
        "strict absolute-cutoff replay differs",
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
    print("absolute Frobenius cutoff replay PASS")


if __name__ == "__main__":
    main()
