#!/usr/bin/env python3
"""Bounded exact controls for one positive-kernel descent counterfeit."""

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
NOTE = HERE / "XI_POSITIVE_KERNEL_DESCENT_FIREWALL.md"
MANIFEST = HERE / "xi_positive_kernel_descent_firewall.sources.json"
FIXTURE = HERE / "xi_positive_kernel_descent_firewall.json"
TEST = ROOT / "tests/test_xi_positive_kernel_descent_firewall.py"
BASE = "58be12463b3ff909eff0d491f606e87149efa9e4"
MAX_K, MAX_Q, MAX_DERIVATIVE = 15, 6, 64
INPUT_BITS, INTERMEDIATE_BITS, MAX_JSON_BYTES = 64, 4096, 1048576
H, R, L, MASS = F(1, 8), F(65, 8), F(9), F(256, 3)
SOURCE_ROWS = (
    (
        "actual_kernel",
        "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
    (
        "actual_kernel_review",
        "f3d074190e64a97ac935b93c5b628568cde90858",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION_AUDIT.md",
        "da9032e15eb7be89557a54120b74fc9596c527d9",
        "aaf60c26b34296aa2e23bdad1469fce8ed3efe5ec27063d14d666f3fa5ce0536",
    ),
    (
        "high_derivative_endpoint",
        "1b5547c3fcd1ba116106953f44a2ee4ceb81b525",
        "research/exploratory/XI_HIGH_DERIVATIVE_SADDLE_CLOSURE.md",
        "6ad6f85b53a18295f84306393118cbaf4d829627",
        "0d68d1791e3e270160f85272f92d0a99931546c5874e93a9aadb3e426847a2c4",
    ),
    (
        "high_derivative_review",
        "58be12463b3ff909eff0d491f606e87149efa9e4",
        "research/exploratory/XI_HIGH_DERIVATIVE_SADDLE_CLOSURE_AUDIT.md",
        "c0da90c7d8db37cd2002e0bda0bc7de609ce4e1b",
        "d212d5aa9feb2d0da5fd7cf5dfc215eeac0aeefe63663afca796c0a44c631da4",
    ),
    (
        "literal_defect_definition",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/lemmas/L-107100-exact-multiplicity-sensitive-reverse-rolle.md",
        "1117fe08c334540d54e57c62af32ec7634ee0d48",
        "6e5fbc4d4998273d91e1eceef14a0d93602f27060a95c054057d46c054413858",
    ),
    (
        "literal_defect_cascade",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/theorems/T-107100-exact-xi-reverse-rolle-defect-cascade.md",
        "36f938decae31a07a9d30ef01526cc862eefda3b",
        "fcf604acfe3ee9cc40195673a4909fd2e9370e8988ddd8f6d9ec66a266a6482a",
    ),
    (
        "earlier_nondescent_firewall",
        "cdad9e88097db4925c3bbbf731f7d1ae1a9e6c57",
        "claims/refutations/R-107100-derivative-line-concentration-alone-does-not-descend.md",
        "6e74e43da002e1640d347312d4822fd9f459ad8f",
        "44dd3d888e0277a080819e1a3b6b448e3020cbfb7f8fa9f8c78d2f8c7f11f887",
    ),
    (
        "literal_theta_series_only",
        "686e23d9e5b1005aae83e3362ac1ed53a28a0352",
        "claims/lemmas/L-105413-explicit-xi-kernel-gives-global-shifted-ray-dominance.md",
        "dfe76fc1985d3366f50489ce21bdcc2cfdd325ff",
        "ae4b3b43c4ad4744337a5278d50d3887a4c83a61b9fdbd424640e5143a82475c",
    ),
)
EXTERNAL_CONTRACTS = (
    (
        "https://arxiv.org/pdf/2008.07206",
        "Farmer Section 4.2 pp8-9: moved cosine zeros and differentiation non-descent; not an exact positive theta-tail theorem",
    ),
    (
        "https://eprints.whiterose.ac.uk/134951/1/ManyDerivsXi_Resubmitted.pdf",
        "Gunns-Hughes Theorem 3.1 pp10-11: compact-domain scaled cosine universality; growing rectangles are not imported from it",
    ),
)


def integer(value, low, high):
    if type(value) is not int or not low <= value <= high:
        raise ValueError("exact integer outside domain/resource cap")
    return value


def rational(value):
    if type(value) not in (int, F):
        raise TypeError("exact int/Fraction required, not bool/float")
    value = F(value)
    if max(value.numerator.bit_length(), value.denominator.bit_length()) > INPUT_BITS:
        raise ValueError("rational input bit cap")
    return value


def checked(value):
    if type(value) not in (int, F):
        raise TypeError("exact intermediate required")
    value = F(value)
    if (
        max(value.numerator.bit_length(), value.denominator.bit_length())
        > INTERMEDIATE_BITS
    ):
        raise ValueError("intermediate bit cap")
    return value


def fixed_root_control():
    # Arithmetic in Q[sqrt(17)]: C0=(3+sqrt(17))/4.
    c0 = (F(3, 4), F(1, 4))
    c0_squared = (c0[0] ** 2 + 17 * c0[1] ** 2, 2 * c0[0] * c0[1])
    root_residual = (
        2 * c0_squared[0] - 3 * c0[0] - 1,
        2 * c0_squared[1] - 3 * c0[1],
    )
    rho = F(1, 256)
    derivative_lower = F(4 * 4, 3) * F(11, 8)
    second_upper = 16 * 9 + F(64, 3) * 81
    taylor_lower = 7 * rho - second_upper * rho**2 / 2
    bump_loss = H**2 * F(3, 2) ** 2
    product_lower = (1 - bump_loss) * taylor_lower
    perturbation_upper = F(1, 64) * F(1, 2)
    if (
        root_residual != (0, 0)
        or not F(17, 8) > F(11, 8) ** 2
        or not derivative_lower > 7
        or taylor_lower != F(107, 8192)
        or product_lower <= perturbation_upper
    ):
        raise ArithmeticError("fixed algebraic root/Rouche reserve failed")
    strip_lower, strip_upper = F(1, 8) - rho, F(3, 8) + rho
    modulus_upper = F(11, 8) + rho
    if not 0 < strip_lower < strip_upper < F(1, 2) or modulus_upper >= F(3, 2):
        raise ArithmeticError("full complex disk leaves the certified strip/modulus")
    return {
        "C0_in_Q_sqrt17": c0,
        "C0_squared": c0_squared,
        "two_C0_squared_minus_three_C0_minus_one": root_residual,
        "rho": rho,
        "imaginary_lower": strip_lower,
        "imaginary_upper": strip_upper,
        "modulus_upper": modulus_upper,
        "Pprime_strict_lower": derivative_lower,
        "Psecond_strict_upper": second_upper,
        "Taylor_strict_lower": taylor_lower,
        "B_minus_one_strict_upper": bump_loss,
        "BP_strict_lower": product_lower,
        "Xi_over_64_upper": perturbation_upper,
        "Rouche_strict_reserve": product_lower - perturbation_upper,
    }


def fixed_defect_control():
    r = F(1, 64)
    pp_lower = -F(16, 3) - 128 * r**2
    pp_upper = -F(16, 3) + F(2048, 3) * r**2
    if not -6 < pp_lower <= pp_upper < -5:
        raise ArithmeticError("real cosine curvature bounds failed")
    b_lower, bprime_upper, bsecond_upper = 1 - 2 * H**2, 2 * H**2, H**2
    function_upper = -F(2, 3) * b_lower + F(1, 128)
    endpoint_reserve = 5 * r * b_lower - F(4, 3) * bprime_upper - F(1, 64)
    second_upper = (
        -5 * b_lower + 2 * bprime_upper * 6 * r + F(4, 3) * bsecond_upper + F(4, 64)
    )
    if not function_upper < 0 < endpoint_reserve or second_upper >= 0:
        raise ArithmeticError("wrong-sign critical point strict reserve failed")
    # Counts are the analytical PF7 consequence, not found by sampling F.
    parent_count, derivative_count, order, orientation, boundary = 0, 1, 1, 1, 1
    defect = order + orientation
    residual = parent_count - (derivative_count - defect + boundary)
    if residual or defect != 2:
        raise ArithmeticError("literal multiplicity/orientation/boundary ledger failed")
    return {
        "interval_center": "pi/4",
        "interval_half_width": r,
        "Psecond_lower": pp_lower,
        "Psecond_upper": pp_upper,
        "B_lower": b_lower,
        "Bprime_absolute_upper": bprime_upper,
        "Bsecond_absolute_upper": bsecond_upper,
        "F_strict_upper": function_upper,
        "endpoint_Fprime_strict_reserve": endpoint_reserve,
        "Fsecond_strict_upper": second_upper,
        "PF7_analytically_implied_parent_count": parent_count,
        "PF7_analytically_implied_derivative_count": derivative_count,
        "r": order,
        "iota": orientation,
        "defect_r_plus_iota": defect,
        "boundary_index": boundary,
        "ledger_residual": residual,
        "endpoint_higher_derivative_nonvanishing_assumed": False,
    }


def current_weight(order, xi, d):
    order = integer(order, 1, MAX_K)
    if order % 2 == 0:
        raise ValueError("fixed positive odd K required")
    xi, d = rational(xi), rational(d)
    if xi <= 0:
        raise ValueError("positive source frequency required")
    u, v = (xi - d) / 2, (xi + d) / 2
    direct = checked(d * (v**order - u**order))
    expanded = checked(
        F(1, 2 ** (order - 1))
        * sum(
            math.comb(order, 2 * j + 1) * xi ** (order - 2 * j - 1) * d ** (2 * j + 2)
            for j in range((order + 1) // 2)
        )
    )
    if direct != expanded or direct < 0:
        raise ArithmeticError("odd-K positive binomial weight identity failed")
    return {
        "K": order,
        "xi": xi,
        "d": d,
        "u": u,
        "v": v,
        "direct": direct,
        "expanded": expanded,
        "endpoint_side": abs(d) > xi,
    }


def exterior_identity(x, y):
    x, y = rational(x), rational(y)
    if x <= 1 or y < 1:
        raise ValueError("formal X=exp(xi)>1 and Y=exp(a)>=1 required")
    left = checked(x * y * (x + 1 / x) / 2 - x * (x * y + 1 / (x * y)) / 2)
    right = checked((y - 1 / y) / 2)
    if left != right or right < 0 or not F(9, 2) < 2 * 3:
        raise ArithmeticError("endpoint exterior hyperbolic identity/sign failed")
    return {
        "formal_exp_xi": x,
        "formal_exp_d_minus_xi": y,
        "left": left,
        "right": right,
        "linear_growth_coefficient": F(9, 2),
        "two_pi_strict_lower": 6,
        "these_are_formal_variables_not_evaluated_exponentials": True,
    }


def exponent_budget(xi, order, q):
    xi = rational(xi)
    order, q = integer(order, 1, MAX_K), integer(q, 0, MAX_Q)
    if order % 2 == 0 or xi < 4 * R:
        raise ValueError("odd K and xi>=4R needed for exponent absorption budget")
    support_min, support_max = xi - 2 * R, xi + 2 * R
    reserve = checked(support_min**2 - xi**2 / 4)
    polynomial = checked(144 * R * support_max ** (2 * q + 1) * (xi + R) ** order)
    if reserve < 0 or L <= R or MASS != 64 + F(64, 3):
        raise ArithmeticError("support/exponent/compact mass budget failed")
    return {
        "xi_formal": xi,
        "K": order,
        "q": q,
        "R": R,
        "support_abs_d_lower": support_min,
        "support_abs_d_upper": support_max,
        "support_enclosure_total_length": 8 * R,
        "square_loss_reserve_above_xi_squared_over_four": reserve,
        "Dq_polynomial_before_C_H0_and_exponent_factors": polynomial,
        "exponential_factors_not_numerically_evaluated": True,
    }


def compact_mass_budget(k, a, j):
    k, j = integer(k, 0, MAX_DERIVATIVE), integer(j, 0, MAX_Q)
    a = rational(a)
    if a < 2:
        raise ValueError("formal a>=2 required")
    coefficient = checked(MASS * (a + L) ** j / 2**k)
    return {
        "k": k,
        "j": j,
        "a_formal_not_claimed_actual_saddle": a,
        "L": L,
        "M": MASS,
        "m_times_relative_weighted_mass_upper_before_exp_H_a_plus_L": coefficient,
        "m_is_the_fixed_positive_theta_mass_on_18_to_19": True,
        "no_numeric_m_or_saddle_or_limit_evaluation": True,
    }


def ratio_control(z, j, dz, dj):
    z, j, dz, dj = map(rational, (z, j, dz, dj))
    if z <= 0 or dz < 0:
        raise ValueError("positive old mass and nonnegative added mass required")
    old, delta = j / z, dz / z
    direct = checked((j + dj) / (z + dz) - old)
    transformed = checked((dj / z - old * delta) / (1 + delta))
    bound = checked(abs(dj) / z + abs(old) * delta)
    if direct != transformed or abs(direct) > bound:
        raise ArithmeticError("signed observable renormalization identity/bound failed")
    return {
        "Z": z,
        "J": j,
        "DeltaZ": dz,
        "DeltaJ": dj,
        "delta": delta,
        "direct_difference": direct,
        "retained_denominator_difference": transformed,
        "absolute_bound": bound,
    }


def sha256_lf(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False)


def read_json(path):
    with path.open("rb") as stream:
        raw = stream.read(MAX_JSON_BYTES + 1)
    if len(raw) > MAX_JSON_BYTES:
        raise ValueError("JSON byte cap")

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
        raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant
    )


def expected_manifest():
    return {
        "schema": "xi-positive-kernel-descent-sources-v1",
        "authoring_base": BASE,
        "source_scope": "literal real theta and reviewed endpoint proofs plus exact defect definitions; no complex-ray or arithmetic transport imported",
        "sources": [
            dict(
                zip(
                    ("role", "commit", "path", "git_blob", "sha256_lf"),
                    row,
                    strict=True,
                )
            )
            for row in SOURCE_ROWS
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
        raise ValueError("complete typed source/semantic contract differs")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual != blob or sha256_lf(raw) != digest:
            raise ValueError("frozen Git blob or LF source hash mismatch")
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
        return [serialize(item) for item in data]
    if type(data) is dict:
        return {key: serialize(value) for key, value in data.items()}
    return data


def build_report():
    auth = authenticate_sources()
    if any(
        isinstance(node, ast.Assert)
        for node in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing assertions may not disappear under -O")
    weights = [
        current_weight(k, xi, d)
        for k in range(1, MAX_K + 1, 2)
        for xi in (F(1), F(17))
        for d in (-xi - 1, -xi / 2, F(0), xi / 2, xi + 1)
    ]
    ratios = [
        ratio_control(*args)
        for args in ((1, 0, 0, 0), (3, 5, 1, 2), (2, -3, 4, 5), (2, -3, 4, -5))
    ]
    return serialize(
        {
            "schema": "xi-positive-kernel-descent-v1",
            "status": "NATIVE_QUANTITATIVE_FIREWALL_SUBJECT_TO_INDEPENDENT_REVIEW",
            "arithmetic_class": "EXACT_RATIONAL",
            "arithmetic_domain": "integer/Fraction algebra with explicit symbolic transcendental contracts",
            "rounding_contract": "none; no Xi, bump integral, exponential, zero or limit evaluated numerically",
            "source_authentication": auth,
            "artifact_sha256_lf": {
                path.relative_to(ROOT).as_posix(): sha256_lf(path.read_bytes())
                for path in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "K": MAX_K,
                "q": MAX_Q,
                "derivative_index": MAX_DERIVATIVE,
                "input_bits": INPUT_BITS,
                "intermediate_bits": INTERMEDIATE_BITS,
                "JSON_bytes": MAX_JSON_BYTES,
            },
            "fixed_construction": {
                "bump_half_width": H,
                "cos8_coefficient": F(1, 3),
                "Xi_perturbation_in_F": F(1, 64),
                "calF_equals_64F": True,
                "half_line_compact_mass": MASS,
                "tail_equality_threshold": R,
                "full_line_multiple_of_phi0": 2,
                "half_line_multiple_of_phi0": 4,
            },
            "root_control": fixed_root_control(),
            "defect_control": fixed_defect_control(),
            "current_weight_controls": weights,
            "exterior_identity_controls": [
                exterior_identity(x, y) for x in (2, 3, 5) for y in (1, 2, 7)
            ],
            "compact_mass_controls": [
                compact_mass_budget(k, a, j)
                for k, a in ((0, 2), (8, 3), (32, 8), (64, 16))
                for j in range(3)
            ],
            "exponent_controls": [
                exponent_budget(xi, k, q)
                for xi, k, q in ((4 * R, 1, 0), (4 * R + 1, 3, 2), (64, 15, 6))
            ],
            "normalization_controls": ratios,
            "coverage": {
                "current_weights": len(weights),
                "endpoint_side_weights": sum(row["endpoint_side"] for row in weights),
                "exterior_identities": 9,
                "compact_mass_budgets": 12,
                "exponent_budgets": 3,
                "signed_normalization_controls": len(ratios),
                "unbounded_computation": False,
            },
            "scope": {
                "one_fixed_smooth_positive_kernel": True,
                "exact_actual_theta_tail": True,
                "frequency_kernel_real_analytic": False,
                "nonreal_simple_zero_in_strip": "PF5-PF6 native Rouche proof",
                "literal_first_rung_defect": 2,
                "boundary_index": 1,
                "growing_derivative_rectangle": "T+H=o(sqrt(k/log(k)))",
                "full_disk_height": "max(H,1/(4*a_k))",
                "fixed_H_one_half_allowed": True,
                "exact_rectangle_endpoint_count": False,
                "source_frequency_limit_K_fixed": True,
                "endpoint_side_abs_d_above_xi_included": True,
                "normalized_ratio_error_retained": True,
                "asymptotic_limits_interchanged": False,
                "all_counterfeit_zeros_in_global_strip": False,
                "arithmetic_origin_or_Euler_product": False,
                "authentic_Xi_source_jets_or_Pick_transfer": False,
                "Xi_XICURV_or_descent_discharged": False,
                "RH_GRH_or_percentage_claim": False,
                "novelty_claim": False,
                "analytic_proof_formally_machine_verified": False,
                "numerical_Xi_or_zero_samples": 0,
            },
        }
    )


def validate_report(report):
    if canonical(report) != canonical(build_report()):
        raise ValueError("complete source-authenticated typed report rebuild differs")


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
            "Positive kernel firewall: exact reserves/sources PASS; native proof requires review; Xi descent/RH OPEN"
        )


if __name__ == "__main__":
    main()
