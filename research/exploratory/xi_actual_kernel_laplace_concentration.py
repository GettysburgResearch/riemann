#!/usr/bin/env python3
"""Source authentication and exact bounded algebra, not a formal Laplace prover."""

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
NOTE = HERE / "XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md"
MANIFEST = HERE / "xi_actual_kernel_laplace_concentration.sources.json"
FIXTURE = HERE / "xi_actual_kernel_laplace_concentration.json"
TEST = ROOT / "tests/test_xi_actual_kernel_laplace_concentration.py"
BASE = "939a24962a4c6a449c0b56e3b20f78b936f35f6c"
SCIENCE = "81d52e569cc8bb566e54043fd692fd6157406aab"
KERNEL_SOURCE = "686e23d9e5b1005aae83e3362ac1ed53a28a0352"
MAX_ORDER, MAX_MOMENT, MAX_INPUT_BITS = 15, 6, 64
SOURCE_ROWS = (
    (
        "literal_half_kernel_only_not_complex_ray_theorem",
        KERNEL_SOURCE,
        "claims/lemmas/L-105413-explicit-xi-kernel-gives-global-shifted-ray-dominance.md",
        "dfe76fc1985d3366f50489ce21bdcc2cfdd325ff",
        "ae4b3b43c4ad4744337a5278d50d3887a4c83a61b9fdbd424640e5143a82475c",
    ),
    (
        "full_line_Fourier_convention",
        SCIENCE,
        "claims/lemmas/L-106401-xi-turan-exterior-square-hankel-source.md",
        "1424cf2a073d16c0f4a6cdd89600e3ebb40b54fc",
        "bf68ecbd1c32969df9491a90da617389ee35ab4fe8f19b76ebd8f706c311a694",
    ),
    (
        "literal_positive_odd_current",
        SCIENCE,
        "claims/lemmas/L-106500-odd-endpoint-wronskian-is-a-positive-current-chaos.md",
        "4c790971237897406b5e0492a13129fad24f37a9",
        "397460968e1718911857eb3c70e87c8fde77458ce4fe4f0fb12f31c09aabadd9",
    ),
    (
        "real_concentration_reproved_not_assumed",
        SCIENCE,
        "claims/lemmas/L-106502-xi-odd-current-profile-saturates-at-high-frequency.md",
        "6600a6c3026f0b7911f247e97be1e4c68b344715",
        "2750ae045bb63bc2c3d0cefbbf8cf28cd3bf3aece5e0d01eedb5fad1de0c0fd2",
    ),
    (
        "antiphase_density_and_scale_definition",
        SCIENCE,
        "claims/lemmas/L-106710-carrier-adapted-antiphase-density-is-source-soft.md",
        "92245b0f9cf5dcccf8f4cee0ea28c1a7c9980d85",
        "4590cdc00533a3ef8536bbff3e78444667ea68caa1b03c97ece422bc2279ce6c",
    ),
    (
        "near_adapted_scale_scout_before_concentration_reproof",
        BASE,
        "research/exploratory/XI_NEAR_ADAPTED_SCALE_FIREWALL.md",
        "0461a5c159d9d1094a9849e362d02ac1149a0143",
        "b770dc30ee6ab5406e159230c6ea617a1e5b1616b818dabb4c4c7f37f4408eac",
    ),
)
EXTERNAL_FORMULAS = (
    (
        "https://dlmf.nist.gov/25.4.E4",
        "xi_R(z)=z(z-1)*pi^(-z/2)*Gamma(z/2)*zeta(z)/2",
    ),
    (
        "https://dlmf.nist.gov/20.7.E32",
        "theta(x)=x^(-1/2)*theta(1/x), x>0; theta(x)=sum_{n in Z}exp(-pi*n^2*x)",
    ),
    (
        "https://dlmf.nist.gov/20.10.E2",
        "integral_0^infty x^(z-1)*(theta(x^2)-1) dx=pi^(-z/2)*Gamma(z/2)*zeta(z), Re z>1",
    ),
)


def canonical(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_lf(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def exact(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError("exact int or Fraction required; bool and float rejected")
    value = Fraction(value)
    if (
        max(value.numerator.bit_length(), value.denominator.bit_length())
        > MAX_INPUT_BITS
    ):
        raise ValueError("input exceeds the exact rational resource cap")
    return value


def odd_order(order: int) -> int:
    if type(order) is not int or not 1 <= order <= MAX_ORDER or order % 2 != 1:
        raise ValueError("bounded control requires odd K in 1,...,15")
    return order


def moment_order(order: int) -> int:
    if type(order) is not int or not 0 <= order <= MAX_MOMENT:
        raise ValueError("bounded control requires integer q in 0,...,6")
    return order


def polynomials(order: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    order = odd_order(order)
    return (
        tuple(math.comb(order, 2 * j) for j in range((order + 1) // 2)),
        tuple(math.comb(order, 2 * j + 1) for j in range((order + 1) // 2)),
    )


def polynomial_value(poly: tuple[int, ...], value: Fraction) -> Fraction:
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def current_weight(order: int, xi: int | Fraction, d: int | Fraction) -> Fraction:
    _, q_poly = polynomials(order)
    xi, d = exact(xi), exact(d)
    if xi <= 0:
        raise ValueError("source frequency must be positive")
    expanded = (
        Fraction(1, 2 ** (order - 1))
        * xi ** (order - 1)
        * d**2
        * polynomial_value(q_poly, d * d / (xi * xi))
    )
    direct = d * (((xi + d) / 2) ** order - ((xi - d) / 2) ** order)
    if expanded != direct or expanded < 0:
        raise ArithmeticError("literal current binomial identity failed")
    return direct


def kernel_operator() -> dict:
    # D acting on e^(u/2)*x^j*psi^(j)(x), x=e^(2u).
    def derivative(coefficients: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
        out = [Fraction(0)] * (len(coefficients) + 1)
        for j, value in enumerate(coefficients):
            out[j] += (Fraction(1, 2) + 2 * j) * value
            out[j + 1] += 2 * value
        return tuple(out)

    twice = list(derivative(derivative((Fraction(1),))))
    twice[0] -= Fraction(1, 4)
    source = tuple(value / 2 for value in twice)
    if source != (0, 3, 2) or tuple(twice) != (0, 6, 4):
        raise ArithmeticError("theta differential operator changed")
    mellin_factor = Fraction(1, 2)
    phi0_factor = Fraction(1, 2) * mellin_factor
    xi_factor = Fraction(1, 2)
    if xi_factor / phi0_factor != 2:
        raise ArithmeticError("full-line Xi normalization is not twice phi0")
    return {
        "basis": "e^(u/2)*[psi(x),x*psi'(x),x^2*psi''(x)]",
        "phi0_operator_coefficients": source,
        "PhiXi_operator_coefficients": twice,
        "phi0_Mellin_coefficient_of_z_times_z_minus_one": phi0_factor,
        "standard_Xi_Mellin_coefficient": xi_factor,
        "actual_kernel_over_historical_phi0": 2,
        "quadratic_density_multiplier": 4,
        "frequency_rescaling": False,
    }


def gaussian_moment_constant(order: int) -> Fraction:
    order = moment_order(order)
    # The result multiplies (pi*E)^(-q), after the current's d^2 weighting.
    return Fraction(math.prod(range(1, 2 * order + 2, 2)), 2**order)


def asymptotic_constants(order: int) -> dict:
    p_poly, q_poly = polynomials(order)
    p1 = p_poly[1] if len(p_poly) > 1 else 0
    q1 = q_poly[1] if len(q_poly) > 1 else 0
    r_linear = Fraction(order * p1 - q1, order * order)
    if r_linear != Fraction(order * order - 1, 3 * order):
        raise ArithmeticError("R_K Taylor coefficient failed")
    correction = r_linear * gaussian_moment_constant(1) / 2
    return {
        "K": order,
        "P": p_poly,
        "Q": q_poly,
        "R_constant": Fraction(1, order),
        "R_x_squared_coefficient": r_linear,
        "m2_times_pi_E_limit": gaussian_moment_constant(1),
        "gain_divided_by_pi_xi_squared_E_limit": Fraction(1, order),
        "adapted_p_limit": Fraction(1, 2 * order),
        "p_correction_times_pi_E_xi_squared_limit": correction,
        "zero_shift_times_pi_E_xi_squared_limit": Fraction(1, 4),
        "window_width_times_pi_E_xi_squared_divided_by_M_limit_M_positive": order,
        "current_defect_times_pi_E_divided_by_h_squared_limit": Fraction(1, 4),
    }


def boundary_limit(order: int, gamma: int | Fraction) -> Fraction:
    order, gamma = odd_order(order), exact(gamma)
    # eta=1+c exp(-xi)/xi^2, c=gamma/pi: no numerical pi is evaluated.
    return Fraction(1, 2 * order) - 2 * gamma / order


def expected_manifest() -> dict:
    return {
        "schema": "xi-actual-kernel-laplace-sources-v1",
        "scout_base": BASE,
        "normalization": "PhiXi=2*phi0; no frequency rescaling; quadratic densities multiply by four",
        "concentration_dependency": "new real-kernel proof in note; L106502 concentration is not assumed",
        "sources": [
            {
                "role": role,
                "commit": commit,
                "path": path,
                "git_blob": blob,
                "sha256_lf": digest,
            }
            for role, commit, path, blob, digest in SOURCE_ROWS
        ],
        "external_formulas": [
            {
                "url": url,
                "formula": formula,
                "remote_content_machine_authenticated": False,
            }
            for url, formula in EXTERNAL_FORMULAS
        ],
    }


def authenticate_sources(manifest: object | None = None) -> dict:
    if manifest is None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if canonical(manifest) != canonical(expected_manifest()):
        raise ValueError("source manifest differs from the complete typed contract")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual != blob or sha256_lf(raw) != digest:
            raise ValueError("frozen source blob or content digest mismatch")
    return {
        "source_count": len(SOURCE_ROWS),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "remote_pages_authenticated": False,
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
        raise ValueError("result-bearing assertions must survive Python -O")
    current_rows = 0
    for order in range(1, MAX_ORDER + 1, 2):
        p_poly, q_poly = polynomials(order)
        if any(order * a < b or order * b < a for a, b in zip(p_poly, q_poly)):
            raise ArithmeticError("global R_K coefficient bounds failed")
        for xi in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(7)):
            for d in (
                Fraction(-10),
                Fraction(-2),
                Fraction(-1, 3),
                Fraction(0),
                Fraction(1, 3),
                Fraction(2),
                Fraction(10),
            ):
                current_weight(order, xi, d)
                current_rows += 1
    coarse_ratio = Fraction(16, 2**9)
    theta_sum_upper = 1 / (1 - coarse_ratio)
    if coarse_ratio != Fraction(1, 32) or 2 * theta_sum_upper >= 3:
        raise ArithmeticError("exact coarse theta majorant failed")
    return serialized(
        {
            "schema": "xi-actual-kernel-laplace-v1",
            "status": "ANALYTIC_PROOF_IN_NOTE_WITH_EXACT_BOUNDED_ALGEBRA_CONTROLS",
            "arithmetic_class": "EXACT_INTEGER_RATIONAL_WITH_SYMBOLIC_PI",
            "source_authentication": authentication,
            "artifact_sha256_lf": {
                path.relative_to(ROOT).as_posix(): sha256_lf(path.read_bytes())
                for path in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "K_max": MAX_ORDER,
                "q_max": MAX_MOMENT,
                "rational_input_bits": MAX_INPUT_BITS,
            },
            "normalization": kernel_operator(),
            "tail_constants": {
                "coarse_r_upper_from_pi_gt_3_e_gt_2": coarse_ratio,
                "theta_sum_upper": theta_sum_upper,
                "phi0_upper_divided_by_pi_squared_U": 2 * theta_sum_upper,
                "global_product_Gaussian_majorant_multiplier": 9,
                "denominator_lower_factor_before_kappa_xi_power_H0_E_minus_3_over_2": "2*exp(-2*pi)/27",
            },
            "current_weight_identities_replayed": current_rows,
            "odd_order_constants": [
                asymptotic_constants(order) for order in range(1, MAX_ORDER + 1, 2)
            ],
            "weighted_moment_constants_times_pi_E_power_q": [
                {"q": q, "limit": gaussian_moment_constant(q)}
                for q in range(MAX_MOMENT + 1)
            ],
            "boundary_layer_controls": [
                {
                    "K": order,
                    "gamma": gamma,
                    "c": "gamma/pi",
                    "rho_limit": boundary_limit(order, gamma),
                }
                for order in range(1, MAX_ORDER + 1, 2)
                for gamma in (
                    Fraction(-1),
                    Fraction(0),
                    Fraction(1, 4),
                    Fraction(1, 2),
                    Fraction(1),
                )
            ],
            "scope": {
                "new_real_concentration_proof_resident": True,
                "analytic_proof_formally_machine_verified": False,
                "L105413_complex_ray_claim_imported": False,
                "floating_point_Xi_samples": 0,
                "quadrature_or_fitted_asymptotics": False,
                "source_Pick_or_physical_scale_transfer": False,
                "ninety_percent_density_one_or_RH": False,
                "novelty_claim": False,
            },
        }
    )


def validate_report(report: object) -> None:
    if canonical(report) != canonical(build_report()):
        raise ValueError("artifact differs from complete source-authenticated rebuild")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit-report", action="store_true")
    mode.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(json.dumps(expected_manifest(), indent=2, sort_keys=True))
    elif args.emit_report:
        print(json.dumps(build_report(), indent=2, sort_keys=True))
    else:
        validate_report(json.loads(FIXTURE.read_text(encoding="utf-8")))
        print(
            "Xi actual kernel: source locks and exact bounded algebra PASS; analytic proof requires review; Pick/RH OPEN"
        )


if __name__ == "__main__":
    main()
