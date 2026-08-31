"""Bounded canonical products of actual Frobenius blocks with a grading genus."""

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
FIXTURE = HERE / "grading_genus.verification.json"
BASE = "7b320b3a9a55a16e73d99dd9bbab5bf592d50c93"
PREFIX = "research/l-families/atlas/generalized/"
PINS = {
    "regularized_proof": {
        "freeze": "8985f69d22f8de6254405aa27ca511b3cd21f57c",
        "path": PREFIX + "graded-completion-lab/REGULARIZED_FROBENIUS_TOWER.md",
        "blob": "890e66e5faa77143dfcc7dc72d7cbe30ee0959a1",
    },
    "regularized_producer": {
        "freeze": "8985f69d22f8de6254405aa27ca511b3cd21f57c",
        "path": PREFIX + "graded-completion-lab/regularized_replay.py",
        "blob": "260471c856289f699d2cc780109b39ba3075d618",
    },
    "coherent_good_place_zeros": {
        "freeze": BASE,
        "path": PREFIX + "koszul-analytic-parent/COHERENT_QUADRATIC_PLACE_EULER.md",
        "blob": "2b5b7ef94b0c4c6326a0e06221d01d23475ec58e",
    },
    "geometric_joint_cover": {
        "freeze": BASE,
        "path": PREFIX + "koszul-analytic-parent/RAMIFIED_TWISTED_GLOBAL_COMPLETION.md",
        "blob": "e54a39f39833f446fec68840f28b7466fe52aa67",
    },
    "constructible_H2": {
        "freeze": BASE,
        "path": PREFIX + "koszul-analytic-parent/CONSTRUCTIBLE_POLE_CLEARING_SOURCE.md",
        "blob": "7ed7f6d68327df4c5f395142503253b19e8938e4",
    },
}
OWNED = (
    HERE / "GRADING_GENUS_COMPLETION.md",
    HERE / "GRADING_GENUS_PREREGISTRATION.md",
    HERE / "GRADING_GENUS_REPLAY.md",
    HERE / "grading_genus_replay.py",
    ROOT / "tests/test_graded_completion_grading_genus.py",
)
MAX_BYTES = 4_000_000
MAX_BITS = 16384


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
    name = "grading_genus_frozen_regularized"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, ROOT / PINS["regularized_producer"]["path"]
        )
        need(spec is not None and spec.loader is not None, "source import unavailable")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
    module = sys.modules[name]
    _, original = module.source()
    return provenance, module, original


def bit_guard(value: int | Fraction) -> None:
    value = Fraction(value)
    need(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= MAX_BITS,
        "rational bit cap",
    )


def mobius(n: int) -> int:
    integer(n, 1, 64)
    sign, prime = 1, 2
    while prime * prime <= n:
        if n % prime == 0:
            n //= prime
            sign = -sign
            if n % prime == 0:
                return 0
        prime += 1
    return -sign if n > 1 else sign


def multiplicity(n: int) -> int:
    integer(n, 2, 64)
    need(n % 2 == 0, "even source grade")
    top = sum(mobius(d) * 2 ** (n // d) for d in range(1, n + 1, 2) if n % d == 0)
    need(top > 0 and top % (2 * n) == 0, "positive integral source multiplicity")
    return top // (2 * n)


def trace(power: int) -> int:
    integer(power, 0, 256)
    old, current = 2, 0
    if power == 0:
        return old
    for _ in range(1, power):
        old, current = current, -7 * old
    return current


def frobenius_matrix(e: int) -> tuple:
    integer(e, 1, 6)
    out, generator = ((1, 0), (0, 1)), ((0, -7), (1, 0))
    for _ in range(e):
        out = tuple(
            tuple(sum(out[i][k] * generator[k][j] for k in range(2)) for j in range(2))
            for i in range(2)
        )
    return out


def policy_order(n: int, policy: str = "linear", slope: int = 1) -> int:
    integer(n, 4, 64)
    need(n % 2 == 0, "even grading policy")
    need(
        type(policy) is str and policy in ("linear", "slow", "nonmonotone"),
        "declared genus policy",
    )
    integer(slope, 1, 6)
    if policy == "linear":
        return slope * n
    need(slope == 1, "slope applies only to the linear policy")
    if policy == "slow":
        return n.bit_length()
    return n if n % 4 == 0 else n // 2


def validate(e: int, policy: str, slope: int, grade_cap: int, cut: int) -> None:
    integer(e, 1, 6)
    integer(grade_cap, 4, 16)
    need(grade_cap % 2 == 0, "even generator cutoff")
    integer(cut, 0, 64)
    policy_order(4, policy, slope)


def multiply(left: list, right: list, cut: int) -> list:
    integer(cut, 0, 64)
    out = [Fraction(0)] * (cut + 1)
    for i, a in enumerate(left[: cut + 1]):
        if a:
            for j, b in enumerate(right[: cut - i + 1]):
                if b:
                    out[i + j] += a * b
    for value in out:
        bit_guard(value)
    return out


def polynomial_power(poly: list, exponent: int, cut: int) -> list:
    integer(exponent, 0, 1_000_000)
    integer(cut, 0, 64)
    out = [Fraction(1)] + [Fraction(0)] * cut
    while exponent:
        if exponent % 2:
            out = multiply(out, poly, cut)
        poly = multiply(poly, poly, cut)
        exponent //= 2
    return out


def formal_exp(logarithm: list, cut: int) -> list:
    integer(cut, 0, 64)
    need(len(logarithm) == cut + 1 and logarithm[0] == 0, "normalized formal logarithm")
    out = [Fraction(1)]
    for n in range(1, cut + 1):
        value = sum(k * logarithm[k] * out[n - k] for k in range(1, n + 1)) / n
        bit_guard(value)
        out.append(value)
    return out


def proper_product(e: int, grade_cap: int = 16, cut: int = 64) -> list:
    validate(e, "linear", 1, grade_cap, cut)
    matrix = frobenius_matrix(e)
    t = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    need(
        t == trace(e) and determinant == 7**e,
        "actual Frobenius characteristic polynomial",
    )
    out = [Fraction(1)] + [Fraction(0)] * cut
    for n in range(4, grade_cap + 1, 2):
        block = [Fraction(1)] + [Fraction(0)] * cut
        if n <= cut:
            block[n] -= t
        if 2 * n <= cut:
            block[2 * n] += determinant
        out = multiply(out, polynomial_power(block, multiplicity(n), cut), cut)
    return out


def canonical_product(
    e: int, policy: str = "linear", slope: int = 1, grade_cap: int = 16, cut: int = 64
) -> list:
    validate(e, policy, slope, grade_cap, cut)
    counterterm = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        for h in range(1, min(policy_order(n, policy, slope), cut // n + 1)):
            counterterm[n * h] += Fraction(multiplicity(n) * trace(e * h), h)
    return multiply(
        proper_product(e, grade_cap, cut), formal_exp(counterterm, cut), cut
    )


def policy_log(
    e: int,
    policy: str = "linear",
    slope: int = 1,
    grade_cap: int = 16,
    cut: int = 64,
    norm_degree: int = 1,
) -> list:
    validate(e, policy, slope, grade_cap, cut)
    integer(norm_degree, 1, 3)
    out = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        for h in range(policy_order(n, policy, slope), cut // n + 1):
            sieve = norm_degree if h % norm_degree == 0 else 0
            out[n * h] -= Fraction(sieve * multiplicity(n) * trace(e * h), h)
    return out


def policy_counterterm(
    e: int, first: tuple, second: tuple, grade_cap: int = 16, cut: int = 64
) -> list:
    need(
        type(first) is tuple
        and type(second) is tuple
        and len(first) == len(second) == 2,
        "policy pairs",
    )
    validate(e, *first, grade_cap, cut)
    validate(e, *second, grade_cap, cut)
    out = [Fraction(0)] * (cut + 1)
    for n in range(4, grade_cap + 1, 2):
        p, q = policy_order(n, *first), policy_order(n, *second)
        sign = 1 if q >= p else -1
        for h in range(min(p, q), min(max(p, q), cut // n + 1)):
            out[n * h] += Fraction(sign * multiplicity(n) * trace(e * h), h)
    return out


def substituted(poly: list, degree: int, cut: int) -> list:
    integer(degree, 1, 3)
    integer(cut, 0, 64)
    out = [Fraction(0)] * (cut + 1)
    for n, value in enumerate(poly):
        if degree * n <= cut:
            out[degree * n] = value
    return out


def first_difference(left: list, right: list) -> dict | None:
    for n, (a, b) in enumerate(zip(left, right, strict=True)):
        if a != b:
            return {"degree": n, "left": a, "right": b}
    return None


def norm_control(e: int, slope: int, degree: int, cut: int = 64) -> dict:
    integer(e, 1, 2)
    integer(slope, 1, 2)
    integer(degree, 2, 3)
    left = substituted(
        canonical_product(e * degree, "linear", slope, cut=cut // degree), degree, cut
    )
    right = formal_exp(
        policy_log(e, "linear", slope * degree, cut=cut, norm_degree=degree), cut
    )
    need(left == right, "changed-slope Frobenius norm")
    wrong = formal_exp(policy_log(e, "linear", slope, cut=cut, norm_degree=degree), cut)
    return {
        "e": e,
        "slope": slope,
        "degree": degree,
        "right_slope": slope * degree,
        "coefficients": left,
        "unchanged_slope_first_difference": first_difference(left, wrong),
    }


def normalization_control() -> dict:
    product = canonical_product(1)
    need(
        product[16] == -49 and product[24] == Fraction(686, 3),
        "exact first nonintegral normalization",
    )
    need(all(value == 0 for value in product[1:16]), "first correction degree sixteen")
    need(
        all(value.denominator == 1 for value in product[:24]),
        "all earlier canonical coefficients integral",
    )
    native = proper_product(1)
    need(native[8] == 14 and product[8] == 0, "native germ already differs")
    return {
        "native_coefficient_degree8": native[8],
        "new_coefficient_degree8": product[8],
        "new_coefficient_degree16": product[16],
        "new_coefficient_degree24": product[24],
        "full_Hhat_degree24_formula": "H2_24 - 49*H2_8 + 686/3",
        "fractional_part_for_every_integral_H2_with_constant_one": Fraction(2, 3),
        "uncomputed_H2_coefficients_invented": False,
    }


def source_zero_controls() -> list:
    rows = []
    for e in range(1, 5):
        for n in range(4, 17, 2):
            noncollisions = [7 ** (e * d) != 2 ** (2 * n) for d in range(1, 17)]
            need(all(noncollisions), "good-place versus weight zero norm collision")
            rows.append(
                {
                    "e": e,
                    "grade": n,
                    "multiplicity_per_distinct_Frobenius_eigenvalue": multiplicity(n)
                    * (2 if e % 2 == 0 else 1),
                    "distinct_eigenvalue_count": 2 if e % 2 else 1,
                    "radius_power_2n": Fraction(1, 7**e),
                    "good_degree_1_through_16_noncollision": noncollisions,
                    "infinite_density_is_proved_not_sampled": True,
                }
            )
    return rows


def bounded_policy_controls() -> list:
    rows = []
    radius = Fraction(15, 16)
    for e in range(1, 5):
        for p in range(1, 5):
            h0 = p if e % 2 == 0 else p + p % 2
            base = 2 * radius**h0
            coefficient = Fraction(-trace(e * h0), 2 * h0)
            need(base > 1 and coefficient != 0, "bounded-policy necessity witness")
            rows.append(
                {
                    "e": e,
                    "fixed_subsequence_order": p,
                    "first_surviving_trace_order": h0,
                    "real_radius": radius,
                    "exponential_base": base,
                    "leading_real_log_coefficient": coefficient,
                    "all_grade_divergence_is_proved_not_fitted": True,
                }
            )
    return rows


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
    provenance, frozen, original = source()
    source_rows = []
    for n in range(2, 65, 2):
        pbw = original.source_row(n)
        value = sum(pbw["multiplicities"][1:])
        need(
            value == multiplicity(n) == frozen.multiplicity(n),
            "actual PBW source versus independent odd-divisor formula",
        )
        source_rows.append({"grade": n, "multiplicity": value, "PBW": pbw})
    policies = [
        ("linear", 1),
        ("linear", 2),
        ("linear", 3),
        ("slow", 1),
        ("nonmonotone", 1),
    ]
    panels = []
    for e in range(1, 5):
        need(
            frobenius_matrix(e) == frozen.frobenius_matrix(e),
            "same actual Frobenius powers",
        )
        for policy, slope in policies:
            direct = canonical_product(e, policy, slope)
            logarithm = policy_log(e, policy, slope)
            need(
                direct == formal_exp(logarithm, 64),
                "proper block factors versus formal trace-log product",
            )
            first = next((j for j in range(1, 65) if direct[j]), None)
            if policy == "linear":
                need(
                    first == 16 * slope
                    and direct[first] == Fraction(-(7 ** (2 * e * slope)), slope),
                    "linear-policy first correction",
                )
            panels.append(
                {
                    "e": e,
                    "policy": policy,
                    "slope": slope,
                    "genus_orders_even4_through16": [
                        policy_order(n, policy, slope) for n in range(4, 17, 2)
                    ],
                    "first_nonzero_degree": first,
                    "coefficients": direct,
                    "formal_log_coefficients": logarithm,
                }
            )
    quotients = []
    for e in (1, 2):
        for first, second in (
            (policies[0], policies[1]),
            (policies[3], policies[4]),
            (policies[4], policies[3]),
        ):
            low, high = canonical_product(e, *first), canonical_product(e, *second)
            correction = policy_counterterm(e, first, second)
            need(
                high == multiply(low, formal_exp(correction, 64), 64),
                "oriented policy quotient",
            )
            quotients.append(
                {
                    "e": e,
                    "first_policy": first,
                    "second_policy": second,
                    "counterterm_coefficients": correction,
                    "product_first_difference": first_difference(low, high),
                }
            )
    norms = [
        norm_control(e, slope, degree)
        for e in (1, 2)
        for slope in (1, 2)
        for degree in (2, 3)
    ]
    need(
        norms[0]["unchanged_slope_first_difference"] is not None,
        "wrong unchanged-slope norm must fail",
    )
    payload = encode(
        {
            "schema": "grading-genus-global-completion-v1",
            "source": provenance,
            "owned_sha256_lf": {
                str(path.relative_to(ROOT)).replace("\\", "/"): digest(
                    path.read_bytes()
                )
                for path in OWNED
            },
            "actual_F7_source": original.point_counts(),
            "source_multiplicities": source_rows,
            "policies": panels,
            "policy_quotients": quotients,
            "frobenius_norms": norms,
            "normalization_change": normalization_control(),
            "source_zero_controls": source_zero_controls(),
            "bounded_policy_necessity_controls": bounded_policy_controls(),
            "scope": {
                "all_policy_criterion_proved_not_sampled": True,
                "global_scalar_frame_equals_native_germ": False,
                "ordinary_fixed_order_Fredholm_determinant_claimed": False,
                "policy_uniqueness_claimed": False,
                "full_Hhat_zeros_use_separate_good_place_source": True,
                "full_place_Euler_scalar_basechange_law_claimed": False,
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
        strict_equal(candidate, build_payload()), "strict grading-genus replay differs"
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
    print("grading-genus global completion replay PASS")


if __name__ == "__main__":
    main()
