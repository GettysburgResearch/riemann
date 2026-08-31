"""Authenticated exact bounded algebra for three actual-Xi current scales.

The analytic uniformity and tail estimates require review of the two notes.
This producer neither evaluates transcendental Xi values nor runs the scout.
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

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MANIFEST = HERE / "xi_odd_current_scaling.sources.json"
FIXTURE = HERE / "xi_odd_current_scaling.json"
NOTES = (
    HERE / "XI_ODD_CURRENT_DOUBLE_SCALING.md",
    HERE / "XI_ODD_CURRENT_CARRIER_TRANSITION.md",
)
TEST = ROOT / "tests/test_xi_odd_current_scaling.py"
SCOUT = HERE / "xi_odd_current_double_scaling_scout.py"
BASE = "1904d20cdb76ecd26e0e63472625da930075303e"
PARENT = "3b6972320899a82c6caa3a98e2ada5ff703a605a"
SOURCE = "81d52e569cc8bb566e54043fd692fd6157406aab"
MAX_ORDER, MAX_MOMENT, MAX_INPUT_BITS = 63, 8, 64
SOURCE_ROWS = (
    (
        "actual_full_line_kernel_and_global_real_tail_bound",
        PARENT,
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
    (
        "full_line_Fourier_convention",
        SOURCE,
        "claims/lemmas/L-106401-xi-turan-exterior-square-hankel-source.md",
        "1424cf2a073d16c0f4a6cdd89600e3ebb40b54fc",
        "bf68ecbd1c32969df9491a90da617389ee35ab4fe8f19b76ebd8f706c311a694",
    ),
    (
        "literal_positive_odd_current",
        SOURCE,
        "claims/lemmas/L-106500-odd-endpoint-wronskian-is-a-positive-current-chaos.md",
        "4c790971237897406b5e0492a13129fad24f37a9",
        "397460968e1718911857eb3c70e87c8fde77458ce4fe4f0fb12f31c09aabadd9",
    ),
    (
        "literal_scalar_carrier_gain_phase",
        SOURCE,
        "claims/lemmas/L-106710-carrier-adapted-antiphase-density-is-source-soft.md",
        "92245b0f9cf5dcccf8f4cee0ea28c1a7c9980d85",
        "4590cdc00533a3ef8536bbff3e78444667ea68caa1b03c97ece422bc2279ce6c",
    ),
)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_lf(raw):
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def serialize(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, dict):
        return {key: serialize(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [serialize(item) for item in value]
    return value


def exact(value):
    if type(value) not in (int, Fraction):
        raise TypeError("exact integer or Fraction required; bool and float rejected")
    value = Fraction(value)
    if (
        max(value.numerator.bit_length(), value.denominator.bit_length())
        > MAX_INPUT_BITS
    ):
        raise ValueError("rational input resource cap")
    return value


def order(value):
    if type(value) is not int or value % 2 != 1 or not 1 <= value <= MAX_ORDER:
        raise ValueError("bounded control requires odd K in 1,...,63")
    return value


def moment_order(value):
    if type(value) is not int or not 0 <= value <= MAX_MOMENT:
        raise ValueError("bounded control requires integer moment index in 0,...,8")
    return value


def trim(poly):
    result = list(poly)
    while len(result) > 1 and not result[-1]:
        result.pop()
    return tuple(result or [Fraction(0)])


def add(left, right):
    result = [Fraction(0)] * max(len(left), len(right))
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index] += value
    return trim(result)


def multiply(left, right):
    result = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def derivative(poly):
    return trim([j * poly[j] for j in range(1, len(poly))])


def value_at(poly, x):
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * x + coefficient
    return result


def current_polynomials(k):
    k = order(k)
    p = tuple(Fraction(math.comb(k, 2 * j)) for j in range((k + 1) // 2))
    f = tuple(Fraction(math.comb(k, 2 * j + 1), k) for j in range((k + 1) // 2))
    integral = tuple(
        Fraction(math.comb(k - 1, 2 * j), 2 * j + 1) for j in range((k + 1) // 2)
    )
    if f != integral:
        raise ArithmeticError("integral resummation coefficient identity failed")
    return p, f


def current_control(k, xi, d):
    k = order(k)
    xi, d = exact(xi), exact(d)
    if xi <= 0:
        raise ValueError("positive source frequency required")
    p, f = current_polynomials(k)
    z = d**2 / xi**2
    direct_plus = ((1 + d / xi) ** k + (1 - d / xi) ** k) / 2
    direct_weight = d * (((xi + d) / 2) ** k - ((xi - d) / 2) ** k)
    expanded_weight = k * xi ** (k - 1) * d**2 * value_at(f, z) / 2 ** (k - 1)
    if direct_plus != value_at(p, z) or direct_weight != expanded_weight:
        raise ArithmeticError("direct versus resummed current mismatch")
    if direct_plus < 1 or direct_weight < 0:
        raise ArithmeticError("current positivity control failed")
    return direct_weight


def likelihood_derivative(k):
    k = order(k)
    if k + 2 > MAX_ORDER:
        raise ValueError("successor order exceeds cap")
    a, _ = current_polynomials(k)
    b, _ = current_polynomials(k + 2)
    direct = add(
        multiply(derivative(b), a), tuple(-x for x in multiply(b, derivative(a)))
    )
    pairs = [Fraction(0)] * (len(a) + len(b) - 2)
    aa = a + (Fraction(0),)
    for j in range(1, len(b)):
        for i in range(j):
            pairs[i + j - 1] += (j - i) * (b[j] * aa[i] - b[i] * aa[j])
    if (
        direct != trim(pairs)
        or any(x < 0 for x in direct)
        or not any(x > 0 for x in direct)
    ):
        raise ArithmeticError("strict polynomial likelihood-ratio identity failed")
    return direct


def gaussian_derivative_moment(q):
    q = moment_order(q)
    poly = (Fraction(1),)
    for _ in range(2 * q + 1):
        poly = add(derivative(poly), (Fraction(0),) + tuple(x / 2 for x in poly))
    if any(poly[j] for j in range(0, len(poly), 2)):
        raise ArithmeticError("Gaussian derivative parity failed")
    return tuple(2 * poly[j] for j in range(1, len(poly), 2))


def gaussian_mgf_moment(q):
    q = moment_order(q)
    result = []
    for j in range(q + 1):
        coefficient = Fraction(
            math.factorial(2 * q),
            math.factorial(q - j) * 4 ** (q - j) * math.factorial(2 * j) * 2 ** (2 * j),
        )
        if j < q:
            coefficient += Fraction(
                math.factorial(2 * q),
                math.factorial(q - j - 1)
                * 4 ** (q - j - 1)
                * math.factorial(2 * j + 1)
                * 2 ** (2 * j + 1),
            )
        result.append(coefficient)
    return tuple(result)


def current_translation_coefficients(q):
    q = moment_order(q)
    observed = tuple(
        x / math.factorial(2 * q + 1) for x in gaussian_derivative_moment(q)
    )
    predicted = tuple(
        Fraction(
            1,
            4 ** (q - j)
            * math.factorial(q - j)
            * 2 ** (2 * j)
            * math.factorial(2 * j + 1),
        )
        for j in range(q + 1)
    )
    if observed != predicted:
        raise ArithmeticError("translated sinhc current series identity failed")
    return observed


def boundary_control(q, delta):
    q, delta = exact(q), exact(delta)
    if q <= 0:
        raise ValueError("positive source frequency required")
    ell, a = 1 + 1 / (2 * q), 1 - 1 / (2 * q**2)
    u = delta / (2 * q) + Fraction(9, 4)
    # Gaussian E[y^2]=1/ell and E[y^4]=3/ell^2; odd order-M^-1 term integrates to zero.
    mean_coefficient = u / ell - a * Fraction(3, 6) / ell**2
    second_coefficient = 1 / ell
    rebuilt = ell * (2 * q * mean_coefficient + second_coefficient)
    predicted = delta + Fraction(7, 2) * q + Fraction(3, 2) + 1 / (4 * q + 2)
    if rebuilt != predicted:
        raise ArithmeticError("critical scalar window coefficient failed")
    return {"xi": q, "Delta": delta, "ell": ell, "window_coefficient": rebuilt}


def carrier_boundary_control(kappa, w):
    kappa, w = exact(kappa), exact(w)
    if kappa < 0:
        raise ValueError("nonnegative kappa required")
    # eta=1+w/S. The inverse's linear coefficient is -w.
    direct_constant = 2 * (-w - w) + 1 + kappa**2 / 2
    predicted = 1 + kappa**2 / 2 - 4 * w
    if direct_constant != predicted:
        raise ArithmeticError("compact-kappa carrier scale mismatch")
    return predicted


def expected_manifest():
    return {
        "schema": "xi-odd-current-scaling-sources-v1",
        "authoring_base": BASE,
        "normalization": "full-line PhiXi=2*historical phi0; no frequency rescaling",
        "parameter_firewall": "K varies; no prescribed physical lambda is changed",
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
    }


def authenticate_sources(manifest=None):
    if manifest is None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if canonical(manifest) != canonical(expected_manifest()):
        raise ValueError(
            "source manifest differs from the exact declared primitive panel"
        )
    for _, commit, path, blob, digest in SOURCE_ROWS:
        actual_blob = (
            subprocess.check_output(["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT)
        if actual_blob != blob or sha256_lf(raw) != digest:
            raise ValueError("primitive source blob or LF digest mismatch")
    return {
        "source_count": len(SOURCE_ROWS),
        "exact_git_blobs_and_lf_bytes": True,
        "ancestral_code_executed": False,
    }


def build_report():
    authenticated = authenticate_sources()
    if any(
        isinstance(node, ast.Assert)
        for node in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing assertions must survive Python -O")
    current_rows = 0
    for k in range(1, MAX_ORDER + 1, 2):
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
                current_control(k, xi, d)
                current_rows += 1
    likelihood = []
    for k in range(1, MAX_ORDER - 1, 2):
        coefficients = likelihood_derivative(k)
        likelihood.append(
            {
                "K": k,
                "successor_K": k + 2,
                "degree": len(coefficients) - 1,
                "complete_coefficients_sha256": hashlib.sha256(
                    canonical(serialize(coefficients)).encode()
                ).hexdigest(),
                "first_coefficient": coefficients[0],
                "last_coefficient": coefficients[-1],
                "nonnegative_coefficients": True,
                "strictly_positive_coefficient_exists": True,
            }
        )
    moments = []
    for q in range(MAX_MOMENT + 1):
        derivative_result = gaussian_derivative_moment(q)
        if derivative_result != gaussian_mgf_moment(q):
            raise ArithmeticError(
                "independent Gaussian generating-function check failed"
            )
        moments.append(
            {
                "q": q,
                "moment_polynomial_in_kappa_squared": derivative_result,
                "sinhc_translation_tau_2q_coefficient": current_translation_coefficients(
                    q
                ),
            }
        )
    boundary = [
        boundary_control(q, delta)
        for q in (2, 3, 5, 8, 10, 16, 32, 64)
        for delta in (-4 * q, -3 * q, 0, q)
    ]
    # Cleared general rational identity q*A/ell=q-1/2-1/(4q+2).
    cleared_left = (Fraction(-1), Fraction(0), Fraction(2))
    cleared_right = add(
        multiply((Fraction(1), Fraction(2)), (Fraction(-1, 2), Fraction(1))),
        (Fraction(-1, 2),),
    )
    if cleared_left != cleared_right:
        raise ArithmeticError("general cleared boundary rational identity failed")
    return serialize(
        {
            "schema": "xi-odd-current-scaling-v1",
            "status": "ANALYTIC_THEOREMS_IN_NOTES_WITH_EXACT_BOUNDED_ALGEBRA",
            "arithmetic_class": "EXACT_RATIONAL",
            "rounding_contract": "no rounded transcendental evaluation; analytic tails and limits are not machine proved",
            "source_authentication": authenticated,
            "artifact_sha256_lf": {
                p.relative_to(ROOT).as_posix(): sha256_lf(p.read_bytes())
                for p in (*NOTES, Path(__file__), TEST, SCOUT, MANIFEST)
            },
            "caps": {
                "K_max": MAX_ORDER,
                "moment_index_max": MAX_MOMENT,
                "rational_input_bits": MAX_INPUT_BITS,
            },
            "complete_current_grid_rows": current_rows,
            "likelihood_successor_panel": likelihood,
            "gaussian_moment_panel": moments,
            "boundary_window_panel": boundary,
            "general_boundary_cleared_coefficients": cleared_left,
            "carrier_panel": [
                {
                    "kappa": kappa,
                    "w": w,
                    "limit_2K_rho": carrier_boundary_control(kappa, w),
                }
                for kappa in (Fraction(0), Fraction(1, 2), Fraction(1), Fraction(4))
                for w in (
                    Fraction(-1),
                    Fraction(0),
                    Fraction(1, 4),
                    Fraction(1),
                    Fraction(3),
                )
            ],
            "scopes": {
                "analytic_proof_formally_machine_verified": False,
                "analytic_uniformity_from_finite_panel": False,
                "literal_Xi_numerically_evaluated_by_this_producer": False,
                "scout_is_directed_or_certified": False,
                "physical_gauge_changed": False,
                "native_source_capture_or_RH_conclusion": False,
                "noninteger_current_order_defined": False,
                "external_novelty_claim": False,
            },
        }
    )


def validate_report(report):
    if canonical(report) != canonical(build_report()):
        raise ValueError(
            "artifact differs from the complete source-authenticated rebuild"
        )


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
            "Xi odd-current exact source/algebra PASS; analytic review required; physical capture/RH OPEN"
        )


if __name__ == "__main__":
    main()
