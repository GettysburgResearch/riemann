"""Preregistered directed-ball evaluation of the literal 64 tensor fields."""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import itertools
import json
import platform
import subprocess
from fractions import Fraction
from pathlib import Path

import flint
from flint import acb, acb_mat, arb, ctx

BITS = 1024
NODES = tuple(range(1, 65))
PRIMES = (2, 3, 5)
WORDS = tuple(itertools.product((0, 1), repeat=3))
DESIGN = "8113cb407b6c7b2e64943b4485ead37b7ac0ccc3"
ROOT = Path(__file__).resolve().parents[2]
STEM = "native_physical_coercivity_pass4"
DIRECTORY = ROOT / "research/exploratory"
FIXTURE = DIRECTORY / (STEM + ".json")
MANIFEST = DIRECTORY / (STEM + ".sources.json")
SOURCE_REFS = (
    (
        "9421846721cd788ab01615c8b6d459d9de849df7",
        "research/riemann-structures/native-six-hour/FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md",
    ),
    (
        "9421846721cd788ab01615c8b6d459d9de849df7",
        "research/riemann-structures/native-six-hour/INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md",
    ),
    (
        "9421846721cd788ab01615c8b6d459d9de849df7",
        "research/riemann-structures/native-six-hour/EFFECTIVE_FULL_SUPPORT_THEOREM.md",
    ),
    (
        "9497db89e34669e2167c632c918c491bf6ee73ab",
        "research/exploratory/prs-765-766-770-781-proof-review/SOURCE_OBSERVATION_AND_EPSTEIN_WALL.md",
    ),
    (DESIGN, "research/exploratory/NATIVE_PHYSICAL_COERCIVITY_PASS4_DESIGN.md"),
    (
        "8f01064df805624c045877655893c324a220975d",
        "research/exploratory/NATIVE_TUPLE_SOURCE_ACQUISITION.md",
    ),
    (
        "8f01064df805624c045877655893c324a220975d",
        "research/exploratory/NATIVE_BOOLEAN_DECODER_DIAGNOSTIC.md",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106026-mellin-plancherel-normal-form-for-owner-conductor-moment.md",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106093-mellin-polarization-places-the-anchor-inside-one-amplified-family-moment.md",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106133-canonical-equal-pair-boolean-source-is-a-beta-half-source-square.md",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/lemmas/L-106134-common-mother-is-a-differential-self-convolution.md",
    ),
    (
        "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b",
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102741-wick-gauge-and-exact-prime-carrier-quotient.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102746-wick-tail-has-a-canonical-equal-pair-owner.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102837-shared-largest-owner-is-a-polylogarithmic-renewal.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102862-owner-core-overlaps-are-a-polylogarithmic-common-factor-renewal.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102882-stopped-vaughan-reduces-the-core-to-one-balanced-current.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102904-endpoint-color-walsh-expansion-has-only-squared-activity-off-the-midpoint.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102951-harmonic-critical-class-is-the-squarefree-boolean-euler-class.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102954-hodge-boolean-reduction-leaves-one-owner-indexed-restriction.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102959-incidence-masked-centered-phase-packing.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102963-owner-and-phase-gauges-decouple-on-the-boolean-source.md",
    ),
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/theorems/T-102990-equal-pair-boolean-core-incidence-frontier.md",
    ),
)
RUNTIME = {
    "python_flint": "0.9.0",
    "flint": "3.6.0",
    "python": "3.12.10",
    "system": "Windows",
    "machine": "AMD64",
    "native_files": 44,
    "native_files_sha256": "36c07323af58dec0eb6fd82a99bf871924eb69f1833d9af626fc09437ae5b0cc",
}
ARTIFACT_PATHS = (
    "research/exploratory/NATIVE_PHYSICAL_COERCIVITY_PASS4_DESIGN.md",
    "research/exploratory/NATIVE_PHYSICAL_COERCIVITY_PASS4.md",
    "research/exploratory/NATIVE_TUPLE_WEIGHTING_BOUNDARY_PASS4.md",
    "research/exploratory/native_physical_coercivity_pass4.py",
    "research/exploratory/native_physical_coercivity_pass4.sources.json",
    "tests/test_native_physical_coercivity_pass4.py",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def endpoint(value):
    man, exp = value.man_exp()
    man, exp = int(man), int(exp)
    return Fraction(man * (1 << exp)) if exp >= 0 else Fraction(man, 1 << -exp)


def fraction_pair(value):
    return [value.numerator, value.denominator]


def ball_record(value):
    return [
        fraction_pair(endpoint(value.lower())),
        fraction_pair(endpoint(value.upper())),
    ]


def complex_record(value):
    return [ball_record(value.real), ball_record(value.imag)]


def source_row(t, reflected=False):
    local = []
    for p in PRIMES:
        z = (acb(-arb(1) / 2, -t if reflected else t) * arb(p).log()).exp()
        local.append(((1 - z * z).sqrt(), (1 - z).sqrt()))
    values = []
    for word in WORDS:
        value = acb(1)
        for j, letter in enumerate(word):
            value *= local[j][letter]
        values.append(value)
    if reflected:
        return [values[a].conjugate() * values[b] for a in range(8) for b in range(8)]
    return [values[a] * values[b].conjugate() for a in range(8) for b in range(8)]


def kappa_hat(t):
    root2 = arb(2).sqrt()
    log2 = arb(2).log()
    constants = (8, -8 * (1 + root2), 8 * root2)
    exponential = (-4, 4 * root2, -2)
    value = acb(0)
    for j, (aa, bb) in enumerate(zip(constants, exponential)):
        lo, hi = j * log2, (j + 1) * log2
        z = acb(0, -t)
        w = acb(arb(1) / 2, -t)
        value += aa * ((z * hi).exp() - (z * lo).exp()) / z
        value += bb * ((w * hi).exp() - (w * lo).exp()) / w
    return value


def upper_power(value):
    require(value > 0, "nonpositive upper target")
    exponent = 0
    while Fraction(2) ** exponent < value:
        exponent += 1
        require(exponent <= 4096, "inverse bound cap")
    return exponent


def lower_power(value):
    require(value > 0, "nonpositive modulus lower target")
    exponent = 0
    while Fraction(1, 2**exponent) > value:
        exponent += 1
        require(exponent <= 4096, "modulus bound cap")
    return exponent


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def strict_json(raw):
    require(type(raw) is bytes and len(raw) <= 4_000_000, "JSON bytes/cap")

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def forbidden(_):
        raise ValueError("floating/nonfinite JSON number")

    result = json.loads(
        raw, object_pairs_hook=pairs, parse_float=forbidden, parse_constant=forbidden
    )
    count = 0

    def visit(value, depth):
        nonlocal count
        count += 1
        require(count <= 100_000 and depth <= 20, "JSON work cap")
        if type(value) is int:
            require(value.bit_length() <= 4096, "integer cap")
        elif type(value) is str:
            require(len(value) <= 4096, "string cap")
        elif type(value) in (list, dict):
            require(len(value) <= 4096, "container cap")
            for item in value.values() if type(value) is dict else value:
                visit(item, depth + 1)
        else:
            require(type(value) is bool or value is None, "unsupported JSON type")

    visit(result, 0)
    return result


def frozen_sources():
    result = []
    for commit, path in SOURCE_REFS:
        require(
            subprocess.check_output(["git", "cat-file", "-t", commit], cwd=ROOT).strip()
            == b"commit",
            "source is not a commit",
        )
        raw = subprocess.check_output(["git", "show", commit + ":" + path], cwd=ROOT)
        blob = (
            subprocess.check_output(["git", "rev-parse", commit + ":" + path], cwd=ROOT)
            .decode()
            .strip()
        )
        actual = (
            subprocess.check_output(
                ["git", "hash-object", "--stdin"], input=raw, cwd=ROOT
            )
            .decode()
            .strip()
        )
        require(blob == actual, "source Git blob mismatch")
        result.append(
            {
                "commit": commit,
                "path": path,
                "git_blob": blob,
                "sha256_lf": digest(raw.replace(b"\r\n", b"\n")),
            }
        )
    return result


def runtime():
    dist = importlib.metadata.distribution("python-flint")
    native = {}
    for path in dist.files:
        if str(path).endswith((".pyd", ".dll")):
            source = Path(dist.locate_file(path))
            require(
                source.is_file() and source.stat().st_size <= 100_000_000,
                "native runtime cap",
            )
            native[str(path)] = digest(source.read_bytes())
    return {
        "python_flint": flint.__version__,
        "flint": flint.__FLINT_VERSION__,
        "python": platform.python_version(),
        "system": platform.system(),
        "machine": platform.machine(),
        "native_files": len(native),
        "native_files_sha256": digest(canonical(native).encode()),
    }


def manifest():
    return {
        "schema": STEM + "-sources-v1",
        "frozen_sources": frozen_sources(),
        "runtime": RUNTIME,
        "design_commit": DESIGN,
    }


def authenticate():
    require(canonical(runtime()) == canonical(RUNTIME), "runtime mismatch")
    expected = manifest()
    require(
        canonical(strict_json(MANIFEST.read_bytes())) == canonical(expected),
        "source manifest mismatch",
    )
    return expected


def tuple_control():
    def histories(primes):
        output = []
        for tags in itertools.product(range(3), repeat=len(primes)):
            if 0 not in tags or 1 not in tags:
                continue
            parts = [[p for p, tag in zip(primes, tags) if tag == j] for j in range(3)]
            products = []
            for part in parts:
                n = 1
                for p in part:
                    n *= p
                products.append(n)
            output.append(products + [(-1) ** tags.count(2)])
        return output

    left, right = histories((71, 73, 79)), histories((401, 421))
    signed = [Fraction(a[3] * b[3], 60) for a in left for b in right]
    require(
        len(signed) == 24
        and signed.count(Fraction(1, 60)) == signed.count(Fraction(-1, 60)) == 12,
        "tuple histories",
    )
    c, d, ell, rho = 409457, 168821, 71, 401
    nn, mm = 6 * c * c, 35 * d * d
    require(
        pow(35, (ell - 1) // 2, ell) == ell - 1
        and pow(6, (rho - 1) // 2, rho) == rho - 1,
        "quadratic classes",
    )
    return {
        "U": 64,
        "Y": 64**6,
        "tuple": [6, 35, 1, c, d],
        "physical_products": [nn, mm],
        "phase_primes": [ell, rho],
        "quadratic_classes": [-1, -1],
        "principal_conductor_weight": fraction_pair(
            Fraction(ell * rho * (ell + 1) * (rho + 1), (ell - 1) * (rho - 1))
        ),
        "left_histories": left,
        "right_histories": right,
        "bilateral_coefficients": [fraction_pair(x) for x in signed],
        "canonical_coefficient_sum": fraction_pair(sum(signed)),
        "canonical_literal_diagonal": fraction_pair(sum(x * x for x in signed)),
        "common_physical_modulus_squared": fraction_pair(
            Fraction(1, 210 * c * c * d * d)
        ),
        "direct_owner_core_overlap": False,
        "direct_shared_owner": False,
        "retained_ancestry_reconstructed": False,
        "native_weighted_sum": "UNDETERMINED",
    }


def build_report():
    source_manifest = authenticate()
    ctx.prec = BITS
    rows, reflected, kappas = [], [], []
    for t in NODES:
        row, other = source_row(t), source_row(t, reflected=True)
        require(all((a - b).contains(0) for a, b in zip(row, other)), "phase mismatch")
        rows.append(row)
        reflected.append(other)
        kappas.append(kappa_hat(t))
    matrix = acb_mat(rows)
    inverse = matrix.inv()
    left, right = inverse * matrix, matrix * inverse
    for i in range(64):
        for j in range(64):
            require(left[i, j].contains(int(i == j)), "left inverse mismatch")
            require(right[i, j].contains(int(i == j)), "right inverse mismatch")
    inverse_row_bounds = []
    for i in range(64):
        bound = sum((abs(inverse[i, j]) for j in range(64)), arb(0))
        inverse_row_bounds.append(endpoint(bound.upper()))
    candidate = acb_mat(
        [
            [acb(inverse[i, j].real.mid(), inverse[i, j].imag.mid()) for j in range(64)]
            for i in range(64)
        ]
    )
    residual = candidate * matrix - acb_mat(
        [[int(i == j) for j in range(64)] for i in range(64)]
    )
    residual_upper = max(
        endpoint(sum((abs(residual[i, j]) for j in range(64)), arb(0)).upper())
        for i in range(64)
    )
    candidate_upper = max(
        endpoint(sum((abs(candidate[i, j]) for j in range(64)), arb(0)).upper())
        for i in range(64)
    )
    require(residual_upper < Fraction(1, 2), "strict candidate inverse residual")
    neumann_upper = candidate_upper / (1 - residual_upper)
    modulus_lowers = [endpoint(abs(value).lower()) for value in kappas]
    require(all(value > 0 for value in modulus_lowers), "kappa node is unresolved")
    bb = upper_power(max(max(inverse_row_bounds), neumann_upper))
    ee = lower_power(min(modulus_lowers))
    ss = bb + 3
    dd = max(2, ss + 15, ee + 7)
    qq = dd + 2 * ss + 2 * ee + 6
    report = {
        "schema": "native-physical-coercivity-pass4-v1",
        "design_commit": DESIGN,
        "runtime": RUNTIME,
        "frozen_sources": source_manifest["frozen_sources"],
        "contract": {
            "arithmetic_class": "MIXED",
            "arithmetic_components": [
                "CERTIFIED_BALL",
                "EXACT_RATIONAL",
                "CERTIFIED_INTEGER_COVERAGE",
            ],
            "rounding": "directed Arb/ACB balls; rational dyadic outward summaries",
            "precision_bits": BITS,
            "primes": list(PRIMES),
            "nodes": list(NODES),
            "tensor_dimension": 64,
            "measure": "abs(kappahat(t))^2 dt/(2*pi), unchanged",
            "source_basis": "AC tensor basis, lexicographic pairs",
            "native_retained_gamma_reconstructed": False,
            "uniform_in_primes": False,
        },
        "evaluation_stream_sha256": hashlib.sha256(
            canonical([[complex_record(x) for x in row] for row in rows]).encode()
        ).hexdigest(),
        "reflected_stream_sha256": hashlib.sha256(
            canonical([[complex_record(x) for x in row] for row in reflected]).encode()
        ).hexdigest(),
        "inverse_row_norm_upper": [fraction_pair(x) for x in inverse_row_bounds],
        "midpoint_inverse_residual_upper": fraction_pair(residual_upper),
        "midpoint_inverse_norm_upper": fraction_pair(candidate_upper),
        "neumann_inverse_norm_upper": fraction_pair(neumann_upper),
        "kappa_node_balls": [complex_record(x) for x in kappas],
        "kappa_modulus_lower": [fraction_pair(x) for x in modulus_lowers],
        "powers": {
            "inverse_infinity_upper_2pow": bb,
            "evaluation_sigma_lower_2negpow": ss,
            "kappa_modulus_lower_2negpow": ee,
            "interval_radius_2negpow": dd,
            "physical_gram_lower_2negpow": qq,
            "physical_gram_upper_2pow": 27,
            "original_monomial_gram_lower_2negpow": qq + 12,
            "original_monomial_gram_upper_2pow": 39,
            "finite_horizon_threshold_2pow": 190,
            "finite_horizon_gram_lower_2negpow": qq + 2,
        },
        "tuple_control": tuple_control(),
        "coverage": {
            "nodes": 64,
            "complex_source_evaluations": 4096,
            "reflected_source_evaluations": 4096,
            "inverse_identity_entries": 8192,
            "positive_kappa_nodes": 64,
        },
        "artifact_sha256_lf": {
            path: digest((ROOT / path).read_bytes().replace(b"\r\n", b"\n"))
            for path in ARTIFACT_PATHS
        },
    }
    report["payload_sha256"] = hashlib.sha256(canonical(report).encode()).hexdigest()
    return report


def check_report(report):
    require(type(report) is dict, "report must be object")
    unsigned = {key: value for key, value in report.items() if key != "payload_sha256"}
    require(
        report.get("payload_sha256") == digest(canonical(unsigned).encode()),
        "payload seal mismatch",
    )
    require(
        canonical(report) == canonical(build_report()),
        "fresh source reconstruction mismatch",
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--emit", action="store_true")
    parser.add_argument("--emit-sources", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    require(sum((args.emit, args.emit_sources, args.check)) <= 1, "conflicting modes")
    if args.emit_sources:
        print(json.dumps(manifest(), indent=2, sort_keys=True))
        return
    if not args.emit:
        check_report(strict_json(FIXTURE.read_bytes()))
        print(
            "PASS: fresh original-physical-norm certificate and unresolved native tuple boundary"
        )
        return
    result = build_report()
    if args.emit:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
