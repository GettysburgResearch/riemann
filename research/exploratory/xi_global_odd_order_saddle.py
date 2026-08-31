"""Exact identities supporting the all-order actual-Xi saddle manuscript.

This verifies finite rational/symbolic controls, not the analytic tail proof.
The separate scout executes its authenticated ancestral theta evaluator;
this producer never imports ancestral code or evaluates Xi numerically.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BASE = "af809698fe6cb5046a5bcc00e9175296e4597060"
MANIFEST = HERE / "xi_global_odd_order_saddle.sources.json"
FIXTURE = HERE / "xi_global_odd_order_saddle.json"
NOTE = HERE / "XI_GLOBAL_ODD_ORDER_SADDLE.md"
SCOUT = HERE / "xi_global_odd_order_scout.py"
SCOUT_RESULTS = HERE / "xi_global_odd_order_scout_results.json"
TEST = ROOT / "tests/test_xi_global_odd_order_saddle.py"
MAX_K, MAX_INPUT_BITS = 127, 64
SCOUT_CASES = (
    (4, "1.5", "1"),
    (8, "1.5", "1"),
    (12, "1.5", "1"),
    (12, "0.75", "1"),
    (8, "2", "1"),
    (8, "2", "2*pi"),
    (12, "3", "1"),
    (12, "4", "1"),
    (12, "5", "1"),
    (20, "5", "1"),
)
SOURCE_ROWS = (
    (
        "full_line_kernel_and_complete_theta_tail",
        "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
    (
        "earlier_bounded_order_scaling_and_scalar_definitions",
        BASE,
        "research/exploratory/XI_ODD_CURRENT_DOUBLE_SCALING.md",
        "682e5b89ae99dee92741a290b5d7357bf8feef73",
        "3c7c16677311d40d8219a88ffb236984ea8704a8ef4e1a30f8b9da1637342e41",
    ),
    (
        "literal_kernel_critical_carrier_window",
        BASE,
        "research/exploratory/XI_ODD_CURRENT_CARRIER_TRANSITION.md",
        "17963babcee47e305ad8c78498d56fbf0ef67dd8",
        "b7f3b85a56dba60b1b249ddd447d68f6cd9421423fa7fc1c27aa32804891becc",
    ),
    (
        "theta_evaluator_used_only_by_separate_nondirected_scout",
        BASE,
        "research/exploratory/xi_odd_current_double_scaling_scout.py",
        "78344ddf0fe289f926a7409343fd33e2ea3082c9",
        "c9726967a842e1f0b9343bc6eae4cf54e17a45ebc0fe23f2d1f32caf6145626b",
    ),
)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_lf(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def exact(value):
    if type(value) not in (int, Fraction):
        raise TypeError("exact integer or Fraction required")
    value = Fraction(value)
    if (
        max(value.numerator.bit_length(), value.denominator.bit_length())
        > MAX_INPUT_BITS
    ):
        raise ValueError("rational input resource cap")
    return value


def expected_manifest():
    return {
        "schema": "xi-global-odd-order-saddle-sources-v1",
        "authoring_base": BASE,
        "normalization": "literal full-line even Phi; arbitrary positive odd K",
        "scout_firewall": "authenticated ancestral theta code; bounded NON_DIRECTED_HIGH_PRECISION only",
        "sources": [
            dict(zip(("role", "commit", "path", "git_blob", "sha256_lf"), row))
            for row in SOURCE_ROWS
        ],
    }


def authenticate_sources(manifest=None):
    if manifest is None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if canonical(manifest) != canonical(expected_manifest()):
        raise ValueError("source manifest differs from declared frozen inputs")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        actual_blob = (
            subprocess.check_output(["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
        if actual_blob != blob or sha256_lf(raw) != digest:
            raise ValueError("source git blob or LF digest mismatch")
    return {
        "source_count": len(SOURCE_ROWS),
        "exact_git_blobs_and_lf_bytes": True,
        "ancestral_code_executed_by_exact_producer": False,
        "ancestral_code_executed_by_separate_scout": True,
    }


def current_factor_control(k, xi, d):
    if type(k) is not int or not 1 <= k <= MAX_K or k % 2 != 1:
        raise ValueError("bounded odd order required")
    xi, d = exact(xi), exact(d)
    if xi < 2 or d < 0:
        raise ValueError("xi>=2 and d>=0 required")
    r = (xi - d) / (xi + d)
    direct = d * (((xi + d) / 2) ** k - ((xi - d) / 2) ** k)
    factored = d * (xi + d) ** k * (1 - r**k) / 2**k
    direct_plus = ((xi + d) / 2) ** k + ((xi - d) / 2) ** k
    factored_plus = (xi + d) ** k * (1 + r**k) / 2**k
    if direct != factored or direct_plus != factored_plus:
        raise ArithmeticError("literal current bracket identity failed")
    if not 0 <= 1 - r**k <= 2 or not 0 <= 1 + r**k <= 2:
        raise ArithmeticError("positive-half-line bracket bound failed")
    return {
        "K": k,
        "xi": str(xi),
        "d": str(d),
        "minus_bracket": str(1 - r**k),
        "plus_bracket": str(1 + r**k),
    }


def theta_bound_controls():
    rows = {
        "first_orbit_lower": Fraction(1) - Fraction(3, 2 * 3),
        "tail_using_pi_gt_3_e_gt_2": Fraction(512, 31) * Fraction(1, 2**9),
        "successive_half_exponent_ratio": Fraction(3, 2) ** 4 / Fraction(2**7),
        "theta_derivative_majorant": Fraction(1, 2)
        + Fraction(1, 62)
        + Fraction(32, 15),
        "B_lower": Fraction(1, 4),
        "B_upper": Fraction(32, 31) ** 2,
        "phase_downjump_lower_using_pi_gt_3": 2 * Fraction(3) - Fraction(9, 2),
        "corner_order_width_lower_per_xi": 4 * Fraction(3) - 9,
    }
    if rows["first_orbit_lower"] != Fraction(1, 2):
        raise ArithmeticError("theta lower factor")
    if rows["tail_using_pi_gt_3_e_gt_2"] != Fraction(1, 31):
        raise ArithmeticError("complete theta-tail bound")
    if rows["successive_half_exponent_ratio"] >= Fraction(1, 16):
        raise ArithmeticError("theta derivative geometric ratio")
    if rows["theta_derivative_majorant"] >= 3:
        raise ArithmeticError("theta derivative bound")
    if min(rows.values()) <= 0:
        raise ArithmeticError("positive constants")
    return {key: str(value) for key, value in rows.items()}


def symbolic_phase_controls():
    q, d, k, p = sp.symbols("q d k p", positive=True)
    half = sp.Rational(9, 2)
    balanced = k * sp.log(q + d) + half * q - p * (sp.exp(q + d) + sp.exp(q - d))
    unbalanced = k * sp.log(q + d) + half * d - p * (sp.exp(q + d) + sp.exp(d - q))
    slopes = (
        k / (q + d) - p * (sp.exp(q + d) - sp.exp(q - d)),
        k / (q + d) + half - p * (sp.exp(q + d) + sp.exp(d - q)),
    )
    curvatures = (
        k / (q + d) ** 2 + p * (sp.exp(q + d) + sp.exp(q - d)),
        k / (q + d) ** 2 + p * (sp.exp(q + d) + sp.exp(d - q)),
    )
    identities = {
        "balanced_derivative": sp.diff(balanced, d) - slopes[0],
        "unbalanced_derivative": sp.diff(unbalanced, d) - slopes[1],
        "balanced_curvature": sp.diff(balanced, d, 2) + curvatures[0],
        "unbalanced_curvature": sp.diff(unbalanced, d, 2) + curvatures[1],
        "phase_continuity": (balanced - unbalanced).subs(d, q),
        "curvature_continuity": (curvatures[0] - curvatures[1]).subs(d, q),
        "downward_slope_jump": (slopes[0] - slopes[1]).subs(d, q) - (2 * p - half),
        "left_corner_order": slopes[0].subs({d: q, k: 2 * p * q * (sp.exp(2 * q) - 1)}),
        "right_corner_order": slopes[1].subs(
            {d: q, k: 2 * q * (p * (sp.exp(2 * q) + 1) - half)}
        ),
        "wrong_center_slope_defect": slopes[1]
        - slopes[0]
        - (half - p * (sp.exp(d - q) + sp.exp(q - d))),
    }
    for label, expression in identities.items():
        if sp.simplify(expression) != 0:
            raise ArithmeticError(f"symbolic phase identity failed: {label}")
    # exp(9|q-d|/4+9(q+d)/4)=exp((9/2)max(q,d)).
    if sp.expand(sp.Rational(9, 4) * (q - d + q + d) - half * q) != 0:
        raise ArithmeticError("balanced exact kernel amplitude")
    if sp.expand(sp.Rational(9, 4) * (d - q + q + d) - half * d) != 0:
        raise ArithmeticError("unbalanced exact kernel amplitude")
    return {
        "complete_symbolic_identities": list(identities),
        "kernel_amplitude_branches": 2,
        "pi_is_symbolic_not_rounded": True,
    }


def gaussian_response_coefficients(max_index=12):
    if type(max_index) is not int or not 0 <= max_index <= 12:
        raise ValueError("Gaussian moment index resource cap")
    rows = []
    for j in range(max_index + 1):
        moment = math.prod(range(1, 2 * j, 2))
        series = Fraction(moment, math.factorial(2 * j))
        mgf = Fraction(1, 2**j * math.factorial(j))
        if series != mgf:
            raise ArithmeticError("normal exponential response coefficient failed")
        rows.append({"j": j, "normal_even_moment": moment, "coefficient": str(series)})
    return rows


def validate_scout_campaign(campaign):
    """Transport/source contract only; does not re-evaluate transcendental data."""
    if type(campaign) is not dict or campaign.get("certified") is not False:
        raise ValueError("non-certified scout campaign required")
    if (
        campaign.get("arithmetic_class") != "NON_DIRECTED_HIGH_PRECISION"
        or campaign.get("bounded_quadrature_not_full_integral_certificate") is not True
    ):
        raise ValueError("scout scope contract")
    rows = campaign.get("cases")
    if type(rows) is not list or len(rows) != len(SCOUT_CASES):
        raise ValueError("complete declared scout panel required")
    scout_hash = sha256_lf(SCOUT.read_bytes())
    for row, case in zip(rows, SCOUT_CASES):
        if type(row) is not dict or type(row.get("xi")) is not int:
            raise ValueError("strict scout record types")
        if (row["xi"], row.get("gamma"), row.get("b")) != case:
            raise ValueError("declared scout case/order mismatch")
        k = row.get("K")
        if (
            type(k) is not str
            or not 1 <= len(k) <= 310
            or not k.isascii()
            or not k.isdecimal()
            or str(int(k)) != k
            or int(k) < 1
            or int(k) % 2 != 1
            or int(k).bit_length() > 1024
        ):
            raise ValueError(
                "exact odd K must survive transport as canonical decimal text"
            )
        if (
            row.get("parent_commit") != BASE
            or row.get("parent_scout_sha256_lf") != SOURCE_ROWS[-1][-1]
            or row.get("producer_sha256_lf") != scout_hash
        ):
            raise ValueError("scout producer/parent identity")
        if (
            row.get("certified") is not False
            or row.get("arithmetic_class") != "NON_DIRECTED_HIGH_PRECISION"
            or row.get("bounded_quadrature_not_full_integral_certificate") is not True
            or type(row.get("requested_decimal_digits")) is not int
            or row["requested_decimal_digits"] != 50
            or row.get("quadrature_upper") != "24.0"
        ):
            raise ValueError("scout precision/window/scope contract")
    return {
        "case_count": len(rows),
        "canonical_odd_order_decimal_strings": True,
        "scout_source_hashes_verified": True,
        "transcendental_values_recomputed_by_exact_producer": False,
    }


def build_report():
    source = authenticate_sources()
    if any(
        isinstance(n, ast.Assert)
        for n in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing assert removed by optimized Python")
    controls = [
        current_factor_control(k, xi, d)
        for k in range(1, MAX_K + 1, 2)
        for xi in (2, 3, 7, Fraction(19, 2))
        for d in (0, Fraction(1, 11), 1, 2, 3, 7, 12, 100)
    ]
    return {
        "schema": "xi-global-odd-order-saddle-v1",
        "status": "ANALYTIC_THEOREMS_IN_NOTE_WITH_EXACT_BOUNDED_CONTROLS",
        "arithmetic_class": "EXACT_RATIONAL",
        "rounding_contract": "no rounded transcendental evaluation in exact producer; analytic estimates require proof review",
        "source_authentication": source,
        "scout_campaign_contract": validate_scout_campaign(
            json.loads(SCOUT_RESULTS.read_text(encoding="utf-8"))
        ),
        "artifact_sha256_lf": {
            p.relative_to(ROOT).as_posix(): sha256_lf(p.read_bytes())
            for p in (NOTE, SCOUT, SCOUT_RESULTS, TEST, MANIFEST, Path(__file__))
        },
        "control_caps": {
            "max_odd_K": MAX_K,
            "rational_input_bits": MAX_INPUT_BITS,
            "gaussian_moment_index": 12,
        },
        "current_grid_rows": len(controls),
        "current_grid_canonical_sha256": hashlib.sha256(
            canonical(controls).encode()
        ).hexdigest(),
        "theta_bounds": theta_bound_controls(),
        "phase_identities": symbolic_phase_controls(),
        "normal_response_coefficients": gaussian_response_coefficients(),
        "scopes": {
            "analytic_uniformity_machine_verified": False,
            "finite_panel_implies_all_K": False,
            "literal_Xi_evaluated_by_exact_producer": False,
            "numerical_scout_certified": False,
            "physical_gauge_selected": False,
            "cofinal_capture_or_RH_proved": False,
            "fixed_K_first_packet_refuted": False,
            "external_novelty_claim": False,
        },
    }


def validate_report(report):
    if canonical(report) != canonical(build_report()):
        raise ValueError("report differs from complete authenticated rebuild")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--emit-report", action="store_true")
    modes.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(json.dumps(expected_manifest(), sort_keys=True, indent=2))
    elif args.emit_report:
        print(json.dumps(build_report(), sort_keys=True, indent=2))
    else:
        validate_report(json.loads(FIXTURE.read_text(encoding="utf-8")))
        print(
            "Global Xi saddle exact identity/source PASS; analytic proof review separate; RH OPEN"
        )


if __name__ == "__main__":
    main()
