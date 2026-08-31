#!/usr/bin/env python3
"""Bounded exact saddle and perturbation controls, not an analytic prover."""

import argparse
import ast
import hashlib
import json
import math
import subprocess
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "XI_HIGH_DERIVATIVE_SADDLE_CLOSURE.md"
MANIFEST = HERE / "xi_high_derivative_saddle_closure.sources.json"
FIXTURE = HERE / "xi_high_derivative_saddle_closure.json"
TEST = ROOT / "tests/test_xi_high_derivative_saddle_closure.py"
BASE = "a07e9c3ba093abb348b849e0356f6babdf591e84"
MAX_ORDER, MAX_MOMENT, INPUT_BITS, INTERMEDIATE_BITS = 12, 8, 96, 4096
B = F(9, 2)
SOURCE_ROWS = (
    (
        "PR767_full_disk_gate",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/lemmas/L-107102-spectral-concentration-forces-laguerre-positivity-and-real-zero-localization.md",
        "8e83995d592b6e5666a90f7fbf10a427e4361dfb",
        "68cafeb7a9cabad1fe393a1866b67eacd1f7c3955729f30ac5dd13e362d3b332",
    ),
    (
        "PR767_endpoint_frontier",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/theorems/T-107110-xi-saddle-concentration-frontier.md",
        "75fe03b66d89244b3aaafa9e55a86192fb0d382a",
        "a517f6d71804e1ac3f2737cd6c69a7d8f82d85104c7287c9ccefb82e12db1df2",
    ),
    (
        "retained_descent_ledger",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/theorems/T-107100-exact-xi-reverse-rolle-defect-cascade.md",
        "36f938decae31a07a9d30ef01526cc862eefda3b",
        "fcf604acfe3ee9cc40195673a4909fd2e9370e8988ddd8f6d9ec66a266a6482a",
    ),
    (
        "descent_counterexample_firewall",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/refutations/R-107100-derivative-line-concentration-alone-does-not-descend.md",
        "6e74e43da002e1640d347312d4822fd9f459ad8f",
        "44dd3d888e0277a080819e1a3b6b448e3020cbfb7f8fa9f8c78d2f8c7f11f887",
    ),
    (
        "actual_theta_normalization_and_real_bounds",
        "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
    (
        "literal_theta_series_not_complex_ray_theorem",
        "686e23d9e5b1005aae83e3362ac1ed53a28a0352",
        "claims/lemmas/L-105413-explicit-xi-kernel-gives-global-shifted-ray-dominance.md",
        "dfe76fc1985d3366f50489ce21bdcc2cfdd325ff",
        "ae4b3b43c4ad4744337a5278d50d3887a4c83a61b9fdbd424640e5143a82475c",
    ),
    (
        "actual_real_kernel_independent_review",
        "f3d074190e64a97ac935b93c5b628568cde90858",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION_AUDIT.md",
        "da9032e15eb7be89557a54120b74fc9596c527d9",
        "aaf60c26b34296aa2e23bdad1469fce8ed3efe5ec27063d14d666f3fa5ce0536",
    ),
)

EXTERNAL_CONTRACTS = (
    (
        "https://www.sciencedirect.com/science/article/pii/S0022314X05002489",
        "Ki 2006 publisher abstract: repeated Xi derivatives converge after scaling on compact complex sets; no growing-domain theorem imported",
    ),
    (
        "https://eprints.whiterose.ac.uk/134951/1/ManyDerivsXi_Resubmitted.pdf",
        "Gunns-Hughes 2019 primary accepted manuscript, Theorem 3.1 pp10-11: extended-Selberg compact-domain scaled cosine limit and explicit saddle",
    ),
)


def integer(value, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("exact integer outside resource/domain cap")
    return value


def rational(value):
    if type(value) not in (int, F):
        raise TypeError("exact int/Fraction required; bool/float rejected")
    value = F(value)
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > INPUT_BITS:
        raise ValueError("rational input bit cap")
    return value


def checked(value):
    if type(value) not in (int, F):
        raise TypeError("exact intermediate integer/Fraction required")
    value = F(value)
    if (
        max(value.numerator.bit_length(), value.denominator.bit_length())
        > INTERMEDIATE_BITS
    ):
        raise ValueError("intermediate rational bit cap")
    return value


def coordinates(a, s):
    a, s = rational(a), rational(s)
    if a < 2 or s < 64:
        raise ValueError("formal saddle coordinates require a>=2 and S>=64")
    return a, s


def series(values):
    if type(values) not in (tuple, list):
        raise TypeError("finite coefficient list or tuple required")
    integer(len(values), 1, MAX_ORDER + 1)
    # Validate raw trailing values too: never trim away bool/float contamination.
    return tuple(rational(value) for value in values)


def direct_logratio(a, s, order):
    a, s = coordinates(a, s)
    order = integer(order, 2, MAX_ORDER)
    k = a * s
    return (F(0), F(0)) + tuple(
        checked(
            k * F((-1) ** (n + 1), n) / a**n
            - (s + B) * F(2 ** (n - 1), math.factorial(n))
        )
        for n in range(2, order + 1)
    )


def integrated_logderivative(a, s, order):
    a, s = coordinates(a, s)
    order = integer(order, 2, MAX_ORDER)
    # Independently expand k/(a+x)+b-(S+b)*exp(2x), then integrate.
    reciprocal, exponential = F(1, a), F(1)
    result = [F(0)]
    for n in range(order):
        derivative = checked(
            a * s * reciprocal - (s + B) * exponential + (B if n == 0 else 0)
        )
        result.append(checked(derivative / (n + 1)))
        reciprocal = checked(-reciprocal / a)
        exponential = checked(2 * exponential / (n + 1))
    return tuple(result)


def saddle_control(a, s, order):
    a, s = coordinates(a, s)
    direct = direct_logratio(a, s, order)
    independent = integrated_logderivative(a, s, order)
    if direct != independent:
        raise ArithmeticError(
            "exact logratio and integrated logarithmic derivative differ"
        )
    precision = s / a + 2 * s + 9
    if -2 * direct[2] != precision or precision <= 2 * s:
        raise ArithmeticError("saddle precision identity/positive lower bound failed")
    if precision > F(169, 64) * s or s * s / precision < F(4096, 169):
        raise ArithmeticError("unnormalized dominated-limit budget failed")
    return {
        "a_formal": a,
        "S_formal": s,
        "k_formal_equals_aS": a * s,
        "order": order,
        "logratio_coefficients": direct,
        "independent_coefficients": independent,
        "precision": precision,
        "sigma_squared": 1 / precision,
        "sigma_squared_below_one_over_2S": True,
        "S_sigma_squared": s / precision,
        "S_sigma_squared_between_64_over_169_and_one_half": True,
        "square_of_S_times_sigma_lower_bound": F(4096, 169),
        "coordinates_are_not_claimed_actual_transcendental_saddles": True,
    }


def curvature_control():
    rational_upper = F(128, 225) + F(137, 48)
    if not rational_upper < 4:
        raise ArithmeticError("local curvature reserve failed")
    if not F(1, 16) < F(1, 9) or not F(1, 16) < F(1, 2):
        raise ArithmeticError("global three-region conservative loss failed")
    return {
        "a_min": 2,
        "S_min": 64,
        "local_k_over_u_squared_coefficient": F(128, 225),
        "local_exponential_coefficient_after_exp_quarter_below_4_over_3": F(137, 48),
        "combined_coefficient": rational_upper,
        "local_absolute_second_derivative_below_4S": True,
        "used_coarse_second_derivative_bound": 8,
        "normalization_log_loss_budget": 4,
        "global_loss_coefficient": F(1, 16),
        "analytic_exponential_inequalities_proved_in_note_not_sampled": True,
    }


def moment_majorants():
    m1 = 243 * (16 * 3**8 + 32**2)
    m2 = 243 * (96 * 3**8 + 2 * 32**3)
    if (m1, m2) != (25758000, 168980256):
        raise ArithmeticError("integer moment majorant rebuild differs")
    return {
        "B_weight_cap": 1,
        "S_min_for_B_one": 1024,
        "M1": m1,
        "M2": m2,
        "near_integral_bounds_before_exp8": (16, 96),
        "e_upper_bound": 3,
        "pi_upper_bound": 4,
        "limits_or_transcendental_integrals_numerically_evaluated": False,
    }


def perturbation_budget(rho, alpha):
    rho, alpha = rational(rho), rational(alpha)
    if rho < 0 or alpha <= 0 or rho < 3 * alpha / 4:
        raise ValueError("nonnegative geometry must include full-disk enlargement")
    m = moment_majorants()
    e0 = checked(m["M1"] * rho)
    e1 = checked(m["M1"] * (rho + alpha))
    # beta is the dependent alpha**2, never independently selected.
    e2 = checked(m["M1"] * (rho + 2 * alpha) + m["M2"] * alpha**2)
    loss = checked(e1 * (2 + e1) + e0 * (1 + e2) + e2)
    accepted = max(e0, e1, e2) <= F(1, 32)
    if accepted and not (e0 < F(1, 10) and 1 - loss >= F(447, 512)):
        raise ArithmeticError("accepted budget did not imply Rouche/Laguerre reserves")
    return {
        "rho_R_over_sqrtS": rho,
        "alpha_one_over_a_sqrtS": alpha,
        "dependent_beta": alpha**2,
        "normalized_F_Fprime_Fsecond_errors": (e0, e1, e2),
        "rouche_reference_lower_bound": F(1, 10),
        "rouche_margin": F(1, 10) - e0,
        "laguerre_relative_error_bound": loss,
        "laguerre_relative_reserve": 1 - loss,
        "accepted_sufficient_budget": accepted,
        "formal_budget_not_an_actual_Xi_sample": True,
    }


def repaired_tail_budget(eta, phase, tau):
    eta, phase, tau = map(rational, (eta, phase, tau))
    if min(eta, phase, tau) < 0:
        raise ValueError("nonnegative perturbation parameters required")
    if eta > F(1, 32) or phase > F(1, 256) or tau > F(1, 256):
        raise ValueError("outside the repaired sufficient tail contract")
    normalized_error = 2 * phase + 2 * tau
    real_loss = 6 * eta + 6 * F(1, 32) + 11 * tau
    if normalized_error >= F(1, 10) or 1 - real_loss <= F(1, 3):
        raise ArithmeticError("repaired abstract tail reserves failed")
    return {
        "eta": eta,
        "phase_budget": phase,
        "weighted_tail_at_enlarged_height": tau,
        "complex_error_bound": normalized_error,
        "reference_lower_bound": F(1, 10),
        "real_laguerre_reserve_lower_bound": 1 - real_loss,
        "requires_Hstar_max_H_disk_radius": True,
        "requires_holomorphic_neighborhood_not_just_one_moment": True,
    }


def gaussian_control(order):
    order = integer(order, 0, MAX_MOMENT)
    recurrence = 1
    rows = []
    for j in range(order + 1):
        if j:
            recurrence *= 2 * j - 1
        product = math.prod(range(1, 2 * j, 2))
        if recurrence != product:
            raise ArithmeticError("Gaussian moment recurrence/product mismatch")
        rows.append({"power": 2 * j, "standard_normal_moment": recurrence})
    return rows


def fixed_window_control(c):
    c = integer(c, 2, 12)
    if c % 2:
        raise ValueError("finite Mills panel uses even positive integer C only")
    exponent = c * c // 2
    strict_upper = F(4, c * 2**exponent)
    return {
        "C_standard_deviations": c,
        "positive_limit_formula_at_h_zero": "4*normal_upper_tail(C)",
        "Mills_upper_before_exp_bound": "4*exp(-C^2/2)/(C*sqrt(2*pi))",
        "strict_dyadic_upper_bound": strict_upper,
        "below_fixed_1_over_256_eventually": strict_upper <= F(1, 256),
        "fixed_C_tail_tends_to_zero": False,
        "exponential_in_k_decay": False,
        "Gaussian_limit_is_native_analytic_proof_not_inferred_from_panel": True,
    }


def disk_height_countercontrol():
    r, c = 511, F(1, 2**20)
    if r % 4 != 3 or (r + 1) % 8:
        raise ArithmeticError("counterexample frequency congruence failed")
    exponent = (r + 1) // 8
    sinh_lower = c * 2**exponent / (4 * (1 + r * r))
    central_derivative_loss_upper = c * (1 + r) / (1 + r * r)
    phase_upper = 2 * F(1, 4096) * (2 + F(1, 8) + 1)
    if not (
        sinh_lower > 1
        and central_derivative_loss_upper < c < F(1, 256)
        and phase_upper < F(1, 256)
    ):
        raise ArithmeticError("exact full-disk countercontrol lost its strict signs")
    return {
        "u0": 1,
        "T": 2,
        "H": F(1, 8),
        "disk_radius": F(1, 4),
        "R_frequency": r,
        "tail_c_exact": c,
        "core_half_width": F(1, 4096),
        "original_phase_upper_using_exp_below_two": phase_upper,
        "epsilon_formula": "c*exp(-(R-1)/8)/(1+R^2)",
        "epsilon_sinh_R_over_four_strict_lower_bound": sinh_lower,
        "central_derivative_loss_strict_upper_bound": central_derivative_loss_upper,
        "extra_conjugate_pair_inside_full_disk_proved_by_IVT": True,
        "not_an_actual_Xi_measure": True,
        "no_hyperbolic_values_numerically_sampled": True,
    }


def parity_control(order):
    order = integer(order, 0, MAX_ORDER)
    derivative = (1, 0)
    rows = []
    cosine = (1, 0, -1, 0)
    sine = (0, 1, 0, -1)
    for k in range(order + 1):
        normalized = (cosine[k % 4], sine[k % 4])
        signed = tuple((-1) ** k * value for value in normalized)
        if signed != derivative:
            raise ArithmeticError("actual derivative/normalized theta parity failed")
        rows.append(
            {
                "k": k,
                "actual_derivative_cos_sin": derivative,
                "normalized_F_cos_sin": normalized,
                "actual_scalar_sign": (-1) ** k,
            }
        )
        derivative = (derivative[1], -derivative[0])
    return rows


def descent_countercontrols():
    rows = ((0, 1, 2, 1), (0, 3, 4, 1))
    for parent, derivative, defect, endpoint in rows:
        if parent != derivative - defect + endpoint:
            raise ArithmeticError("retained reverse-Rolle firewall changed")
    return {"parent_derivative_defect_endpoint": rows, "descent_discharge": False}


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_lf(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def read_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate JSON key")
            result[key] = value
        return result

    def constant(value):
        raise ValueError("nonfinite JSON constant: " + value)

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=pairs,
        parse_constant=constant,
    )


def expected_manifest():
    return {
        "schema": "xi-high-derivative-saddle-sources-v1",
        "authoring_base": BASE,
        "source_scope": "real theta bounds only; PR767 full-disk tail-height repair; no imported moving-ray theorem",
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
        "external_contracts": [
            {"url": url, "contract": contract, "remote_bytes_authenticated": False}
            for url, contract in EXTERNAL_CONTRACTS
        ],
    }


def authenticate_sources(manifest=None):
    if manifest is None:
        manifest = read_json(MANIFEST)
    if canonical(manifest) != canonical(expected_manifest()):
        raise ValueError("complete typed source contract differs")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual != blob or sha256_lf(raw) != digest:
            raise ValueError("frozen source blob/content mismatch")
    return {
        "source_count": len(SOURCE_ROWS),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "remote_bytes_authenticated": False,
    }


def serialize(data):
    if type(data) is F:
        return str(data)
    if type(data) in (tuple, list):
        return [serialize(value) for value in data]
    if type(data) is dict:
        return {key: serialize(value) for key, value in data.items()}
    return data


CASES = ((2, 64, 4), (3, 128, 6), (F(7, 2), 1024, 8), (8, 4096, 12))


def build_report():
    auth = authenticate_sources()
    if any(
        isinstance(node, ast.Assert)
        for node in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing assertions cannot disappear under -O")
    controls = [saddle_control(*case) for case in CASES]
    m1 = moment_majorants()["M1"]
    budgets = [
        perturbation_budget(F(j, 1024 * m1), F(1, 1024 * m1)) for j in range(1, 9)
    ]
    if not all(row["accepted_sufficient_budget"] for row in budgets):
        raise ArithmeticError("predeclared sufficient budget failed")
    return serialize(
        {
            "schema": "xi-high-derivative-saddle-v1",
            "status": "NATIVE_ANALYTIC_ENDPOINT_PROOF_SUBJECT_TO_INDEPENDENT_REVIEW",
            "arithmetic_class": "EXACT_RATIONAL",
            "arithmetic_domain": "integers and Fractions; symbolic transcendental comparison contracts",
            "rounding_contract": "no floating Xi/saddle/quadrature/zero evaluation and no numerical proof of limits",
            "source_authentication": auth,
            "artifact_sha256_lf": {
                path.relative_to(ROOT).as_posix(): sha256_lf(path.read_bytes())
                for path in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "Taylor_order": MAX_ORDER,
                "Gaussian_moment_index": MAX_MOMENT,
                "rational_input_bits": INPUT_BITS,
                "intermediate_bits": INTERMEDIATE_BITS,
            },
            "coverage": {
                "saddle_coordinate_cases": len(CASES),
                "Taylor_coefficients_compared": sum(case[2] + 1 for case in CASES),
                "perturbation_budgets": len(budgets),
                "Gaussian_moments": MAX_MOMENT + 1,
                "parity_orders": MAX_ORDER + 1,
                "fixed_window_controls": 3,
                "unbounded_search": False,
            },
            "saddle_controls": controls,
            "curvature_control": curvature_control(),
            "moment_majorants": moment_majorants(),
            "perturbation_budgets": budgets,
            "repaired_tail_budget": repaired_tail_budget(
                F(1, 32), F(1, 256), F(1, 256)
            ),
            "Gaussian_moments": gaussian_control(MAX_MOMENT),
            "fixed_window_controls": [fixed_window_control(c) for c in (2, 4, 6)],
            "disk_height_countercontrol": disk_height_countercontrol(),
            "parity_controls": parity_control(MAX_ORDER),
            "normalization": {
                "full_line_multiple_of_phi0": 2,
                "half_line_cosine_multiple_of_phi0": 4,
                "probability_measure_unchanged_by_positive_scalar": True,
                "frequency_rescaled": False,
            },
            "descent_countercontrols": descent_countercontrols(),
            "scope": {
                "all_sufficiently_large_integer_orders_by_native_proof": True,
                "both_parities": True,
                "actual_theta_kernel_not_Gaussian_substitution": True,
                "global_origin_side_tail_controlled": True,
                "load_bearing_route": "native global real density bound and weighted moments",
                "growing_rectangle": "T+H=o(sqrt(k/log(k)))",
                "fixed_H_one_half_allowed": True,
                "full_disk_height": "max(H,1/(4*a_k))",
                "horizontal_enlargement": "T+O(1/a_k)",
                "fixed_four_sigma_tail_limit": "4*normal_upper_tail(4), strictly positive and less than 1/256",
                "fixed_C_sigma_tail_exponentially_small_in_k": False,
                "exact_rectangle_endpoint_count_claimed": False,
                "full_theta_kernel_log_concavity_assumed": False,
                "old_complex_moving_ray_theorem_imported": False,
                "finite_controls_are_actual_transcendental_saddles": False,
                "analytic_proof_formally_machine_verified": False,
                "XICURV107110_discharged": False,
                "reverse_Rolle_descent_discharged": False,
                "source_Pick_transfer": False,
                "RH_or_percentage": False,
                "cosine_universality_novelty_claim": False,
                "Xi_numerical_samples": 0,
            },
        }
    )


def validate_report(report):
    if canonical(report) != canonical(build_report()):
        raise ValueError("complete source-authenticated typed rebuild differs")


def main():
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
        validate_report(read_json(FIXTURE))
        print(
            "Xi high derivative: source/exact saddle budgets PASS; analytic endpoint requires review; XICURV/descent/RH OPEN"
        )


if __name__ == "__main__":
    main()
