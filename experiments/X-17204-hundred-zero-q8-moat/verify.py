#!/usr/bin/env python3
"""Directed Arb replay for the X-17204 hundred-zero q=8 moat.

The checker deliberately has no floating midpoint path.  Arb evaluates the
exact-rational filter on each certified ordinate ball, brackets each ordinate
by cumulative zero counts, and carries all sums as balls.
"""
from __future__ import annotations

import argparse
import hashlib
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


def decimal_string(value: Fraction, digits: int = 30) -> str:
    getcontext().prec = digits + 20
    out = Decimal(value.numerator) / Decimal(value.denominator)
    return f"{out:.{digits}E}"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def resolve(experiment_dir: Path, relative: str) -> Path:
    path = (experiment_dir / relative).resolve()
    assert path.is_file(), f"missing dependency: {path}"
    return path


def verify_rational(cert: dict[str, Any], experiment_dir: Path) -> dict[str, Any]:
    assert cert["classification"] == "DIRECTED_SINGLE_ARB_BACKEND_PROPOSED"
    assert cert["experiment_id"] == "X-17204"
    assert cert["claim_id"] == "L-17203"

    deps = cert["base_dependencies"]
    base_path = resolve(experiment_dir, deps["ten_notch_certificate"])
    q8_path = resolve(experiment_dir, deps["q8_certificate"])
    assert sha256(base_path) == deps["ten_notch_certificate_sha256"]
    assert sha256(q8_path) == deps["q8_certificate_sha256"]
    assert sha256(base_path.with_name("verify.py")) == deps["ten_notch_verifier_sha256"]
    assert sha256(q8_path.with_name("verify.py")) == deps["q8_verifier_sha256"]

    base_cert = json.loads(base_path.read_text(encoding="utf-8"))
    q8_cert = json.loads(q8_path.read_text(encoding="utf-8"))
    q8_verifier_path = q8_path.with_name("verify.py")
    q8_verifier = load_module(q8_verifier_path, "x17203_for_x17204")
    inherited = q8_verifier.verify_certificate(q8_cert, q8_path.parent)
    assert inherited["classification"] == "EXACT_RATIONAL_CHECK_PASSED"

    census = cert["zero_census"]
    assert census["listed_positive_zeros"] == 100
    assert q(census["count_cutoff"]) == 237
    assert census["count_at_cutoff"] == 100
    assert q(census["bracket_radius"]) == Fraction(1, 10**70)

    constants = cert["directed_constants"]
    assert q(constants["tail_transform_factor"]) == Fraction(81, 64)
    assert constants["tail_power"] == 28
    assert q(constants["support_endpoint_upper"]) == Fraction(6499, 600)
    assert q(constants["l1_upper"]) == Fraction(243, 64)
    assert q(constants["tail_domain_start"]) == 18
    assert constants["direct_trivial_indices"] == [3, 4, 5]
    assert constants["first_geometric_tail_index"] == 6
    assert q(constants["first_geometric_tail_lambda"]) == Fraction(25, 2)
    assert q(constants["trivial_spacing"]) == 2
    assert q(constants["nontrivial_line_target"]) == Fraction(349, 10**28)
    assert q(constants["raw_tail_moat"]) == Fraction(35, 10**27)
    endpoint_brackets = constants["retained_endpoint_brackets"]
    assert set(endpoint_brackets) == {
        "unlisted_line_tail",
        "nontrivial_line_total",
        "geometric_trivial_tail",
        "complete_raw_total",
    }
    for bracket in endpoint_brackets.values():
        assert set(bracket) == {"lower", "upper"}
        assert q(bracket["lower"]) < q(bracket["upper"])

    widths = [q(value) for value in base_cert["filter"]["dyadic_widths"]]
    widths.extend(q(row["width"]) for row in base_cert["filter"]["notches"])
    assert len(widths) == 14
    assert constants["tail_power"] == 2 * len(widths)
    product_widths = Fraction(1)
    for width in widths:
        assert width > 0
        product_widths *= width
    assert all(2 < width * 237 for width in widths)

    distance = q(constants["tail_domain_start"]) - q(
        constants["support_endpoint_upper"]
    )
    assert distance == Fraction(4301, 600)
    assert q(constants["first_geometric_tail_lambda"]) == Fraction(4 * 6 + 1, 2)
    return {
        "classification": "EXACT_RATIONAL_PRECHECK_PASSED",
        "inherited_classification": inherited["classification"],
        "listed_positive_zeros": census["listed_positive_zeros"],
        "tail_start": str(q(census["count_cutoff"])),
        "product_all_widths": decimal_string(product_widths),
        "distance_at_x_18_lower": decimal_string(distance),
        "nontrivial_line_target": decimal_string(
            q(constants["nontrivial_line_target"])
        ),
        "raw_tail_moat": decimal_string(q(constants["raw_tail_moat"])),
    }


def unique_integer(value: Any) -> int:
    integer = value.unique_fmpz()
    if integer is None:
        raise AssertionError(f"Arb did not isolate an integer: {value}")
    return int(integer)


def verify_arb(
    cert: dict[str, Any], experiment_dir: Path
) -> dict[str, Any]:
    try:
        import flint
        from flint import acb, arb, ctx
    except ImportError as exc:  # pragma: no cover - environment dependent
        raise SystemExit("Arb replay requires python-flint on PYTHONPATH") from exc

    deps = cert["base_dependencies"]
    base_path = resolve(experiment_dir, deps["ten_notch_certificate"])
    base_cert = json.loads(base_path.read_text(encoding="utf-8"))
    constants = cert["directed_constants"]
    census = cert["zero_census"]
    ctx.prec = int(cert["backend"]["precision_bits"])

    def a(value: Fraction | int | str) -> Any:
        value = q(value) if isinstance(value, str) else Fraction(value)
        return arb(value.numerator) / value.denominator

    widths_q = [q(value) for value in base_cert["filter"]["dyadic_widths"]]
    widths_q.extend(q(row["width"]) for row in base_cert["filter"]["notches"])
    widths = [a(width) for width in widths_q]
    log2 = arb(2).log()
    log4 = 2 * log2
    shift_a1 = arb(6) * log2 / 5
    shift_a2 = arb(2) * log2 / 3

    def box(width: Any, z: Any) -> Any:
        return (1 - (-width * z).exp()) / (width * z)

    def g8_transform(z: Any) -> Any:
        phi = (-z).exp()
        for width in widths:
            phi *= box(width, z)
        g0 = phi * phi * (1 - 2 * (-log4 * z).exp())
        annihilator_1 = 1 - (-shift_a1 * z).exp() / 8
        annihilator_2 = 1 - (-shift_a2 * z).exp() / 8
        return g0 * annihilator_1 * annihilator_2

    bracket_radius = arb(census["bracket_radius"])
    listed_line = arb(0)
    listed_mass = arb(0)
    count_pairs: list[list[int]] = []
    ordinate_balls: list[str] = []
    line_contribution_balls: list[str] = []
    previous_hi = None
    for index in range(1, census["listed_positive_zeros"] + 1):
        rho = acb.zeta_zero(index)
        assert rho.real == arb(1) / 2
        gamma = rho.imag
        assert gamma > 0
        lo = gamma - bracket_radius
        hi = gamma + bracket_radius
        count_lo = unique_integer(lo.zeta_nzeros())
        count_hi = unique_integer(hi.zeta_nzeros())
        assert count_lo == index - 1
        assert count_hi == index
        if previous_hi is not None:
            assert lo > previous_hi
        previous_hi = hi
        z = acb(0, gamma)
        contribution = 2 * abs(g8_transform(z))
        reciprocal_mass = 2 / (gamma * gamma + arb(1) / 4)
        assert contribution >= 0
        assert reciprocal_mass > 0
        listed_line += contribution
        listed_mass += reciprocal_mass
        count_pairs.append([count_lo, count_hi])
        ordinate_balls.append(str(gamma))
        line_contribution_balls.append(str(contribution))

    tail_start = arb(census["count_cutoff"])
    count_at_tail = unique_integer(tail_start.zeta_nzeros())
    assert count_at_tail == census["count_at_cutoff"]
    assert previous_hi is not None and previous_hi < tail_start

    c_xi = arb(2) + arb.const_euler() - (4 * arb.pi()).log()
    residual_mass = c_xi - listed_mass
    assert residual_mass > 0

    product_widths = arb(1)
    for width in widths:
        product_widths *= width
    tail_power = constants["tail_power"]
    assert tail_power == 2 * len(widths)
    coefficient = (
        arb(3)
        * arb(4) ** len(widths)
        / (product_widths * product_widths)
        * arb(81)
        / 64
    )
    conversion = 1 + 1 / (4 * tail_start * tail_start)
    unlisted_line = (
        coefficient
        * tail_start ** (-(tail_power - 2))
        * conversion
        * residual_mass
    )
    line_total = listed_line + unlisted_line
    line_target = a(constants["nontrivial_line_target"])
    assert line_total < line_target

    x0 = a(constants["tail_domain_start"])
    direct_trivial = arb(0)
    trivial_term_balls: list[dict[str, str | int]] = []
    for index in constants["direct_trivial_indices"]:
        lam = arb(4 * index + 1) / 2
        value = (-lam * x0).exp() * abs(g8_transform(acb(-lam)))
        assert value >= 0
        direct_trivial += value
        trivial_term_balls.append(
            {"index": index, "lambda": str(lam), "contribution_ball": str(value)}
        )

    support_upper = a(constants["support_endpoint_upper"])
    distance = x0 - support_upper
    l1_upper = a(constants["l1_upper"])
    first_tail_lambda = a(constants["first_geometric_tail_lambda"])
    spacing = a(constants["trivial_spacing"])
    geometric_trivial = (
        l1_upper
        * (-first_tail_lambda * distance).exp()
        / (1 - (-spacing * distance).exp())
    )
    raw_total = line_total + direct_trivial + geometric_trivial
    raw_moat = a(constants["raw_tail_moat"])
    assert raw_total < raw_moat

    endpoint_brackets = constants["retained_endpoint_brackets"]
    endpoint_values = {
        "unlisted_line_tail": unlisted_line,
        "nontrivial_line_total": line_total,
        "geometric_trivial_tail": geometric_trivial,
        "complete_raw_total": raw_total,
    }
    explicit_endpoints: dict[str, dict[str, str]] = {}
    for name, value in endpoint_values.items():
        lower_text = endpoint_brackets[name]["lower"]
        upper_text = endpoint_brackets[name]["upper"]
        lower = arb(lower_text)
        upper = arb(upper_text)
        assert lower < value
        assert value < upper
        explicit_endpoints[name] = {
            "lower_exact_decimal": lower_text,
            "upper_exact_decimal": upper_text,
        }

    return {
        "classification": "ARB_320_DIRECTED_CHECK_PASSED",
        "python_flint_version": getattr(flint, "__version__", "0.9.0-installed"),
        "precision_bits": ctx.prec,
        "count_at_237": count_at_tail,
        "count_pairs": count_pairs,
        "ordinate_balls": ordinate_balls,
        "individual_line_contribution_balls": line_contribution_balls,
        "xi_reciprocal_sum_ball": str(c_xi),
        "listed_reciprocal_mass_ball": str(listed_mass),
        "residual_reciprocal_mass_ball": str(residual_mass),
        "listed_line_sum_ball": str(listed_line),
        "unlisted_line_tail_ball": str(unlisted_line),
        "nontrivial_line_total_ball": str(line_total),
        "nontrivial_line_target": str(line_target),
        "direct_trivial_terms_at_x_18": trivial_term_balls,
        "direct_trivial_sum_at_x_18_ball": str(direct_trivial),
        "geometric_trivial_tail_m_ge_6_ball": str(geometric_trivial),
        "complete_raw_bound_at_x_18_ball": str(raw_total),
        "explicit_outward_endpoint_bounds": explicit_endpoints,
        "declared_raw_moat": str(raw_moat),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        type=Path,
        default=Path(__file__).with_name("certificate.json"),
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--rational-only",
        action="store_true",
        help="run dependency/hash prechecks without loading Arb",
    )
    args = parser.parse_args()
    certificate_path = args.certificate.resolve()
    cert = json.loads(certificate_path.read_text(encoding="utf-8"))
    result: dict[str, Any] = {
        "rational": verify_rational(cert, certificate_path.parent)
    }
    if not args.rational_only:
        result["arb"] = verify_arb(cert, certificate_path.parent)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
