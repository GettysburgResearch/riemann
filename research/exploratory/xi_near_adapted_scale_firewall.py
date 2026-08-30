#!/usr/bin/env python3
"""Exact bounded carrier-mismatch algebra, not a source-Pick bridge."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "XI_NEAR_ADAPTED_SCALE_FIREWALL.md"
FIXTURE = HERE / "xi_near_adapted_scale_firewall.json"
MANIFEST = HERE / "xi_near_adapted_scale_firewall.sources.json"
TEST = ROOT / "tests/test_xi_near_adapted_scale_firewall.py"
PR_HEAD = "6d440eb6c82d989c046e87e13f9bdabf087f920f"
SCIENCE = "81d52e569cc8bb566e54043fd692fd6157406aab"
MAX_ORDER, MAX_SOURCE_BITS, MAX_SCALAR_BITS = 15, 64, 4096
SOURCE_ROWS = (
    (
        "exact_mismatch_identity",
        "claims/lemmas/L-106710-carrier-adapted-antiphase-density-is-source-soft.md",
        "92245b0f9cf5dcccf8f4cee0ea28c1a7c9980d85",
        "4590cdc00533a3ef8536bbff3e78444667ea68caa1b03c97ece422bc2279ce6c",
    ),
    (
        "conditional_concentration_and_raw_Hardy_node",
        "claims/lemmas/L-106502-xi-odd-current-profile-saturates-at-high-frequency.md",
        "6600a6c3026f0b7911f247e97be1e4c68b344715",
        "2750ae045bb63bc2c3d0cefbbf8cf28cd3bf3aece5e0d01eedb5fad1de0c0fd2",
    ),
    (
        "open_bridge_target",
        "claims/theorems/T-106710-xi-carrier-adapted-source-softening-frontier.md",
        "b06d973198898a93d584b67dbe26ce24823e2ffc",
        "1a1f27c31dccd2a3393675acfc444e712a1449b476a2e1d7812f0e4c5559eb9f",
    ),
    (
        "physical_carrier_is_a_different_variable",
        "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    ),
    (
        "literal_outer_normalized_source_Pick_metric",
        "claims/theorems/T-106670-regularized-pick-free-energy-ninety-percent-equivalence.md",
        "9a61689c19b244f0176f753cef146b252256eab0",
        "b96ffe1ec8e5fc7d825e521c57c956066e25f0494e80aa4c13d4017ea98c8ae7",
    ),
    (
        "nonlocality_outer_and_topological_firewall",
        "claims/refutations/R-106710-diagonal-source-softening-does-not-control-topological-free-energy.md",
        "e17fdf16e87d6791c64fbb6f0ac8f604ca46c396",
        "889fd0cf65cefcf83705e54d0dda5525880fc94c4542ca0be6fa40724e1107c1",
    ),
)


def canonical(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def sha256_lf(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def exact(value: int | Fraction, bits: int = MAX_SCALAR_BITS) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError("exact int or Fraction required")
    value = Fraction(value)
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > bits:
        raise ValueError("rational input exceeds the declared bit cap")
    return value


def odd_order(order: int) -> int:
    if type(order) is not int or order < 1 or order > MAX_ORDER or order % 2 == 0:
        raise ValueError("bounded odd order must be one of 1,3,...,15")
    return order


def polynomials(order: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    order = odd_order(order)
    return (
        tuple(math.comb(order, 2 * j) for j in range((order + 1) // 2)),
        tuple(math.comb(order, 2 * j + 1) for j in range((order + 1) // 2)),
    )


def polynomial_value(coefficients: tuple[int, ...], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def ratio_r(order: int, x: int | Fraction) -> Fraction:
    p_poly, q_poly = polynomials(order)
    x = exact(x, MAX_SOURCE_BITS)
    return polynomial_value(p_poly, x * x) / polynomial_value(q_poly, x * x)


def gaussian_polynomials(order: int) -> dict[str, tuple[int, ...]]:
    p_poly, q_poly = polynomials(order)

    def moments(coefficients: tuple[int, ...], extra: int) -> tuple[int, ...]:
        return (0,) * extra + tuple(
            coefficient * math.prod(range(1, 2 * (j + extra), 2))
            for j, coefficient in enumerate(coefficients)
        )

    return {
        "U": moments(p_poly, 0),
        "V": moments(q_poly, 1),
        "W": moments(p_poly, 1),
        "Z": moments(q_poly, 2),
    }


def gaussian_data(order: int, nu: int | Fraction, xi: int | Fraction = 2) -> dict:
    odd_order(order)
    nu, xi = exact(nu, MAX_SOURCE_BITS), exact(xi, MAX_SOURCE_BITS)
    if nu <= 0 or xi <= 0:
        raise ValueError("Gaussian variance and source frequency must be positive")
    values = {
        key: polynomial_value(poly, nu)
        for key, poly in gaussian_polynomials(order).items()
    }
    gain = values["U"] / (2 * values["V"])
    adapted = values["W"] / (2 * values["V"])
    m2 = xi * xi * values["Z"] / values["V"]
    if not Fraction(1, 2 * order) <= adapted <= Fraction(order, 2):
        raise ArithmeticError("adapted ratio escaped its proven interval")
    if gain < xi * xi / (2 * order * m2):
        raise ArithmeticError("inverse-variance gain lower bound failed")
    return {"K": order, "nu": nu, "xi": xi, "g": gain, "p": adapted, "m2": m2}


def phase(
    gain: int | Fraction, adapted: int | Fraction, eta: int | Fraction
) -> Fraction:
    gain, adapted, eta = exact(gain), exact(adapted), exact(eta)
    if min(gain, adapted, eta) <= 0:
        raise ValueError("gain, adapted ratio, and scale must be positive")
    return gain / eta + (adapted - gain) * eta


def phase_window(
    gain: int | Fraction, adapted: int | Fraction, bound: int | Fraction
) -> dict:
    gain, adapted, bound = exact(gain), exact(adapted), exact(bound)
    if adapted <= 0 or gain <= adapted or bound < 0:
        raise ValueError("finite sign-transition window requires g>p>0 and M>=0")
    b = gain - adapted
    discriminant = bound * bound + 4 * b * gain
    return {
        "b": b,
        "M": bound,
        "discriminant": discriminant,
        "eta_minus": "(sqrt(discriminant)-M)/(2b)",
        "eta_plus": "(sqrt(discriminant)+M)/(2b)",
        "width": bound / b,
        "endpoint_product": gain / b,
        "zero_scale_squared": gain / b,
        "relative_envelope_about_one": (bound + adapted) / b,
    }


def variance_window_bound(
    order: int, xi: int | Fraction, m2: int | Fraction, bound: int | Fraction
) -> dict:
    odd_order(order)
    xi, m2, bound = exact(xi), exact(m2), exact(bound)
    denominator = xi * xi - order * order * m2
    if xi <= 0 or m2 <= 0 or bound < 0 or denominator <= 0:
        raise ValueError("variance window requires xi^2>K^2*m2>0 and M>=0")
    return {
        "width_upper": 2 * order * bound * m2 / denominator,
        "relative_envelope_upper": order * (2 * bound + order) * m2 / denominator,
    }


def boundary_layer_limit(order: int, slope: int | Fraction) -> dict:
    polys = gaussian_polynomials(order)
    slope = exact(slope, MAX_SOURCE_BITS)
    if (polys["U"][0], polys["V"][0], polys["W"][0], polys["V"][1], polys["W"][1]) != (
        1,
        0,
        0,
        order,
        1,
    ):
        raise ArithmeticError("Gaussian leading-moment coefficients changed")
    numerator_linear = polys["W"][1] - 2 * slope * polys["U"][0]
    denominator_linear = 2 * polys["V"][1]
    return {
        "K": order,
        "c": slope,
        "eta": "1+c*nu+o(nu)",
        "numerator_linear": numerator_linear,
        "denominator_linear": denominator_linear,
        "rho_limit": numerator_linear / denominator_linear,
    }


def hardy_band_bound(epsilon: int | Fraction) -> Fraction:
    epsilon = exact(epsilon, MAX_SOURCE_BITS)
    if not 0 < epsilon < 1:
        raise ValueError(
            "relative half-bandwidth must lie strictly between zero and one"
        )
    # The proof gives 2 epsilon/[e(1-epsilon)]; this is a rational upper bound.
    return min(Fraction(1), 2 * epsilon / (1 - epsilon))


def expected_manifest() -> dict:
    return {
        "schema": "xi-near-adapted-scale-sources-v1",
        "pr731_head": PR_HEAD,
        "scientific_head": SCIENCE,
        "concentration_status": "L-106502 is imported conditionally; its independent constant review remains open",
        "sources": [
            {
                "role": role,
                "commit": SCIENCE,
                "path": path,
                "git_blob": blob,
                "sha256_lf": digest,
            }
            for role, path, blob, digest in SOURCE_ROWS
        ],
    }


def authenticate_sources() -> dict:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if canonical(data) != canonical(expected_manifest()):
        raise ValueError("source manifest differs from the complete typed contract")
    for _, path, blob, digest in SOURCE_ROWS:
        ref = f"{SCIENCE}:{path}"
        actual_blob = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual_blob != blob or sha256_lf(raw) != digest:
            raise ValueError("frozen scientific source identity mismatch")
    return {
        "scientific_head": SCIENCE,
        "source_count": len(SOURCE_ROWS),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(data).encode()
        ).hexdigest(),
        "Xi_concentration_independently_reproved": False,
    }


def serialized(data: object) -> object:
    if isinstance(data, Fraction):
        return str(data)
    if isinstance(data, dict):
        return {key: serialized(value) for key, value in data.items()}
    if isinstance(data, (tuple, list)):
        return [serialized(value) for value in data]
    return data


def build_report() -> dict:
    authentication = authenticate_sources()
    if any(
        isinstance(node, ast.Assert)
        for node in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing checks must survive Python -O")
    coefficient_rows = []
    for order in range(1, MAX_ORDER + 1, 2):
        p_poly, q_poly = polynomials(order)
        lower = [order * a - b for a, b in zip(p_poly, q_poly)]
        upper = [order * b - a for a, b in zip(p_poly, q_poly)]
        if min(lower + upper) < 0:
            raise ArithmeticError("ratio coefficient certificate failed")
        coefficient_rows.append(
            {
                "K": order,
                "P": p_poly,
                "Q": q_poly,
                "KP_minus_Q": lower,
                "KQ_minus_P": upper,
            }
        )
    gaussian_rows = []
    for order in (1, 3, 5, 9, 15):
        for nu in (Fraction(1, 16), Fraction(1, 256), Fraction(1, 4096), Fraction(4)):
            row = gaussian_data(order, nu)
            g, p, xi, m2 = (row[key] for key in ("g", "p", "xi", "m2"))
            row["phase_samples"] = [
                {"eta": eta, "rho": phase(g, p, eta)}
                for eta in (Fraction(9, 10), Fraction(1), Fraction(11, 10), 1 + nu)
            ]
            row["phase_window_M_equals_1"] = phase_window(g, p, 1) if g > p else None
            row["variance_window_upper"] = (
                variance_window_bound(order, xi, m2, 1)
                if xi * xi > order * order * m2
                else None
            )
            gaussian_rows.append(row)
    return serialized(
        {
            "schema": "xi-near-adapted-scale-firewall-v1",
            "status": "EXACT_SCALAR_OBSTRUCTION_CONDITIONAL_XI_NARROWING_NOT_A_PICK_BRIDGE",
            "source_authentication": authentication,
            "artifact_sha256_lf": {
                path.relative_to(ROOT).as_posix(): sha256_lf(path.read_bytes())
                for path in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "computation_caps": {
                "odd_order_max": MAX_ORDER,
                "source_parameter_bits": MAX_SOURCE_BITS,
                "derived_scalar_input_bits": MAX_SCALAR_BITS,
                "floating_point_operations": 0,
            },
            "coefficient_certificates": coefficient_rows,
            "gaussian_controls": gaussian_rows,
            "boundary_layer_certificates": [
                boundary_layer_limit(order, slope)
                for order in (1, 5, 15)
                for slope in (Fraction(-1), Fraction(0), Fraction(1, 2), Fraction(1))
            ],
            "fixed_scale_residues_nu_times_rho": [
                {"K": order, "eta": eta, "limit": (1 - eta * eta) / (2 * order * eta)}
                for order in (1, 5, 15)
                for eta in (Fraction(9, 10), Fraction(11, 10))
            ],
            "hardy_relative_band_controls": [
                {
                    "epsilon": eps,
                    "rational_mass_upper": hardy_band_bound(eps),
                    "sharper_analytic_upper": "2*epsilon/[e*(1-epsilon)]",
                }
                for eps in (Fraction(1, 16), Fraction(1, 256), Fraction(1, 4096))
            ],
            "scope": {
                "exact_general_identity": "rho(eta)=g/eta+(p-g)*eta; all odd K>=1 under the note hypotheses",
                "unique_source_uniform_scale": "eta=1; Gaussian counterfamilies rule out every other fixed eta",
                "conditional_Xi_width": "O(exp(-xi)/xi^2) in relative scale, assuming L-106502 q=1 concentration",
                "source_Pick_congruence_proved": False,
                "physical_outer_normalization_transferred": False,
                "confluent_or_collective_Hardy_localization_proved": False,
                "free_energy_or_zero_count_bound_proved": False,
                "ninety_percent_density_one_or_RH_proved": False,
                "novelty_claim": False,
            },
        }
    )


def validate_report(report: object) -> None:
    if canonical(report) != canonical(build_report()):
        raise ValueError("fixture differs from the independently rebuilt typed report")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.write:
        FIXTURE.write_text(
            json.dumps(report, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    elif canonical(json.loads(FIXTURE.read_text(encoding="utf-8"))) != canonical(
        report
    ):
        raise ValueError("fixture differs from exact replay")
    print(
        "Xi scale firewall: source locks, gain, Gaussian phases and bounded controls PASS; Pick bridge OPEN"
    )


if __name__ == "__main__":
    main()
