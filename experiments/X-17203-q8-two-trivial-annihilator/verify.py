#!/usr/bin/env python3
"""Exact rational replay for the X-17203 q=8 auxiliary filter.

This checker deliberately inherits the nontrivial-zero certificate from
X-17202.  It imports and runs that experiment's rational verifier before
checking the two new annihilator factors.  It performs no new zero census.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path
from types import ModuleType
from typing import Any


def q(value: str | int) -> Fraction:
    if isinstance(value, int):
        return Fraction(value)
    if "/" in value:
        return Fraction(value)
    return Fraction(Decimal(value))


def decimal_string(value: Fraction, digits: int = 24) -> str:
    getcontext().prec = digits + 20
    out = Decimal(value.numerator) / Decimal(value.denominator)
    return f"{out:.{digits}E}"


def load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("x17202_verify", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve_dependency(experiment_dir: Path, relative: str) -> Path:
    path = (experiment_dir / relative).resolve()
    assert path.is_file(), f"missing inherited dependency: {path}"
    return path


def verify_certificate(
    cert: dict[str, Any], experiment_dir: Path
) -> dict[str, Any]:
    assert cert["classification"] == "DIRECTED_INHERITED_SINGLE_BACKEND_PROPOSED"
    assert cert["experiment_id"] == "X-17203"
    assert cert["claim_id"] == "L-17202"

    dependency = cert["base_dependency"]
    assert dependency["claim_id"] == "L-17201"
    assert dependency["experiment_id"] == "X-17202"
    base_cert_path = resolve_dependency(experiment_dir, dependency["certificate"])
    base_verify_path = resolve_dependency(experiment_dir, dependency["verifier"])
    base_cert = json.loads(base_cert_path.read_text(encoding="utf-8"))
    base_verifier = load_module(base_verify_path)
    base_result = base_verifier.verify_rational(base_cert)
    assert base_result["classification"] == "EXACT_RATIONAL_CHECK_PASSED"

    base_constants = base_cert["directed_constants"]
    base_line_moat = q(dependency["required_nontrivial_zero_moat"])
    assert base_line_moat == q(base_constants["nontrivial_zero_moat"])
    assert base_line_moat == Fraction(4, 10**18)
    base_l1 = q(dependency["required_base_l1_bound"])
    assert base_l1 == 3

    notch_sum = sum(
        (q(row["width"]) for row in base_cert["filter"]["notches"]),
        Fraction(0),
    )
    notch_sum_upper = q(dependency["required_notch_sum_upper"])
    assert notch_sum_upper == Fraction(17, 8)
    assert notch_sum < notch_sum_upper

    annihilators = cert["annihilators"]
    assert len(annihilators) == 2
    expected_lambdas = [Fraction(5, 2), Fraction(9, 2)]
    shift_sum = Fraction(0)
    line_factor = Fraction(1)
    for index, (row, expected_lambda) in enumerate(
        zip(annihilators, expected_lambdas), start=1
    ):
        assert row["index"] == index
        assert row["q"] == 8
        lam = q(row["lambda"])
        shift_coefficient = q(row["shift_log2_coefficient"])
        assert lam == expected_lambda
        # log(q)=3*log(2), so a=(3/lambda)*log(2).
        assert shift_coefficient * lam == 3
        assert q(row["zero_real_part"]) == -lam
        shift_sum += shift_coefficient
        line_factor *= Fraction(row["q"] + 1, row["q"])
    assert shift_sum == Fraction(28, 15)
    assert line_factor == Fraction(81, 64)

    constants = cert["directed_constants"]
    assert q(constants["critical_line_factor_upper"]) == line_factor
    line_bound = base_line_moat * line_factor

    # e^(7/10)>sum_{n=0}^3 (7/10)^n/n! = 12013/6000 > 2,
    # hence log(2)<7/10.
    log2_upper = q(constants["log2_upper"])
    assert log2_upper == Fraction(7, 10)
    exp_lower = 1 + Fraction(7, 10) + Fraction(49, 200) + Fraction(343, 6000)
    assert exp_lower == Fraction(12013, 6000)
    assert exp_lower > 2

    # b_8 = 31/8 + 2R + (2+28/15)log(2).
    support_upper = (
        Fraction(31, 8)
        + 2 * notch_sum_upper
        + (2 + shift_sum) * log2_upper
    )
    assert support_upper == Fraction(6499, 600)
    assert q(constants["support_endpoint_upper"]) == support_upper

    tail_start = q(constants["tail_domain_start"])
    assert tail_start == 18
    distance_lower = tail_start - support_upper
    assert distance_lower == Fraction(4301, 600)
    assert q(constants["distance_lower"]) == distance_lower

    l1_upper = base_l1 * line_factor
    assert l1_upper == Fraction(243, 64)
    assert q(constants["l1_upper"]) == l1_upper

    first_survivor = q(constants["first_surviving_trivial"])
    spacing = q(constants["trivial_spacing"])
    assert first_survivor == Fraction(13, 2)
    assert spacing == 2
    assert first_survivor * distance_lower > constants["numerator_exponent_floor"]
    assert spacing * distance_lower > constants["denominator_exponent_floor"]
    assert constants["numerator_exponent_floor"] == 46
    assert constants["denominator_exponent_floor"] == 14

    # e>1+1+1/2+1/6+1/24=65/24>27/10.
    e_lower = 1 + 1 + Fraction(1, 2) + Fraction(1, 6) + Fraction(1, 24)
    assert e_lower == Fraction(65, 24)
    assert e_lower > Fraction(27, 10)

    exp_base = Fraction(10, 27)
    trivial_bound = (
        l1_upper
        * exp_base ** constants["numerator_exponent_floor"]
        / (1 - exp_base ** constants["denominator_exponent_floor"])
    )
    trivial_target = q(constants["trivial_tail_target"])
    assert trivial_target == Fraction(273, 5 * 10**21)
    assert trivial_bound < trivial_target

    total_bound = line_bound + trivial_bound
    raw_tail_moat = q(constants["raw_tail_moat"])
    assert raw_tail_moat == Fraction(6, 10**18)
    assert total_bound < raw_tail_moat

    return {
        "classification": "EXACT_RATIONAL_CHECK_PASSED",
        "inherited_base_classification": base_result["classification"],
        "inherited_nontrivial_zero_moat": decimal_string(base_line_moat),
        "critical_line_factor_upper": decimal_string(line_factor),
        "critical_line_bound": decimal_string(line_bound),
        "support_endpoint_upper": decimal_string(support_upper),
        "distance_at_x_18_lower": decimal_string(distance_lower),
        "l1_upper": decimal_string(l1_upper),
        "trivial_tail_bound": decimal_string(trivial_bound),
        "trivial_tail_target": decimal_string(trivial_target),
        "total_rh_bound": decimal_string(total_bound),
        "declared_raw_tail_moat": decimal_string(raw_tail_moat),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path(__file__).with_name("certificate.json"),
    )
    args = parser.parse_args()
    certificate_path = args.certificate.resolve()
    cert = json.loads(certificate_path.read_text(encoding="utf-8"))
    result = verify_certificate(cert, certificate_path.parent)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

