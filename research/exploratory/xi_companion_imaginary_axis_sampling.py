"""Exact finite axis-identity controls; no Xi samples or analytic certification."""

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_companion_imaginary_axis_sampling"
NOTE = HERE / "XI_COMPANION_IMAGINARY_AXIS_SAMPLING.md"
FIXTURE = HERE / (STEM + ".json")
MANIFEST = HERE / (STEM + ".sources.json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "7aed2ec0b99b9d7f2fb94a774922a83d5b84a870"
DEGREE, CUTOFF, ATOMS = 20, 8, 4
INPUT_BITS, BITS, MAX_WORK, MAX_BYTES = 16, 4096, 200000, 2000000
BINDINGS = (
    {
        "id": "GH",
        "commit": "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d",
        "path": "research/exploratory/XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md",
        "git_blob": "e592a4c031876f56f07d28b7e18a8a7cf6e826f4",
        "sha256_lf": "5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d",
        "role": "GH8 phases; GH10-14 differentiated fixed-function asymptotics; reduction",
    },
    {
        "id": "XL",
        "commit": "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "path": "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "git_blob": "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "sha256_lf": "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
        "role": "XL1-4 actual positive even kernel; XL11 superexponential tails",
    },
    {
        "id": "IW",
        "commit": "ef7bbb8dca978269f24e7ff9d97b6dceeed5b460",
        "path": "research/exploratory/HARDY_INNER_WIDTH_SOURCE_DUALITY.md",
        "git_blob": "955b92fe277bcdb3d6e260b5cc9dc02dd3f49144",
        "sha256_lf": "a946e53b956bc94b39687dffe59f0eb97d33948ace996a6d9f0797d71b20acd5",
        "role": "IW2-5 physical adjoint jets and retained outer metric",
    },
    {
        "id": "L106620",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "git_blob": "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "sha256_lf": "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
        "role": "constant lambda and literal C/R companion quotient/remainder",
    },
    {
        "id": "T106620",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/theorems/T-106620-mesoscopic-riemann-siegel-gauge-ninety-percent-frontier.md",
        "git_blob": "8db4fc42c3ea964c592224b64d0ad92b6c264018",
        "sha256_lf": "f926698271d06b2db02bd1d7e00a05034934d8b77a75496e137d127c565795b0",
        "role": "native high-T geographic scope only; no frontier theorem imported",
    },
    {
        "id": "CP",
        "commit": BASE,
        "path": "research/exploratory/COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md",
        "git_blob": "cd74bd06267eb4d60bc977353d11f6a0fb72ba6a",
        "sha256_lf": "b9ab266898129389b94a9ed494b140422fc823552c6b69bf22ed36a9dbb2e7f7",
        "role": "corrected global projection; synthetic countercontrol distinction",
    },
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    require(type(value) is int and low <= value <= high, "strict integer/cap")
    return value


def rational(value, *, internal=False):
    require(type(internal) is bool, "internal flag")
    require(type(value) in (int, Q), "strict rational")
    value = Q(value)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= (BITS if internal else INPUT_BITS),
        "rational bit cap",
    )
    return value


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, amount):
        amount = integer(amount, 0, MAX_WORK)
        require(self.used + amount <= self.limit, "work before expansion")
        self.used += amount


def budget(work):
    if work is None:
        return Budget()
    require(type(work) is Budget, "Budget type")
    return work


def polynomial(value):
    require(
        type(value) in (list, tuple) and 1 <= len(value) <= DEGREE + 1,
        "polynomial degree/shape",
    )
    out = [rational(v, internal=True) for v in value]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pad(a, cut):
    cut = integer(cut, 0, DEGREE)
    a = polynomial(a)
    return (a + [Q(0)] * (cut + 1))[: cut + 1]


def add(a, b):
    a, b = polynomial(a), polynomial(b)
    cut = max(len(a), len(b)) - 1
    return polynomial([x + y for x, y in zip(pad(a, cut), pad(b, cut), strict=True)])


def multiply(a, b, cut=DEGREE, work=None):
    a, b = polynomial(a), polynomial(b)
    cut, work = integer(cut, 0, DEGREE), budget(work)
    work.spend(len(a) * len(b))
    out = [Q(0)] * (cut + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= cut:
                out[i + j] = rational(out[i + j] + x * y, internal=True)
    return polynomial(out)


def derivative(a):
    a = polynomial(a)
    return polynomial([j * a[j] for j in range(1, len(a))] or [0])


def inverse_series(a, cut, work=None):
    a = polynomial(a)
    cut, work = integer(cut, 0, DEGREE), budget(work)
    require(a[0] != 0, "invertible constant")
    work.spend((cut + 1) ** 2)
    out = [Q(1) / a[0]]
    for n in range(1, cut + 1):
        value = -sum(a[j] * out[n - j] for j in range(1, min(n + 1, len(a))))
        out.append(rational(value / a[0], internal=True))
    return polynomial(out)


def compose(a, b, cut, work=None):
    a, b = polynomial(a), polynomial(b)
    cut, work = integer(cut, 0, DEGREE), budget(work)
    require(b[0] == 0, "composition zero constant")
    out = [Q(0)]
    for value in reversed(a):
        out = add(multiply(out, b, cut, work), [value])
    return polynomial(out)


def revert_series(a, cut, work=None):
    a = polynomial(a)
    cut, work = integer(cut, 1, DEGREE), budget(work)
    require(len(a) >= 2 and a[0] == 0 and a[1] != 0, "reversion domain")
    out = [Q(0), Q(1) / a[1]]
    for n in range(2, cut + 1):
        trial = pad(compose(a, out, n, work), n)
        out.append(rational(-trial[n] / a[1], internal=True))
    require(
        pad(compose(a, out, cut, work), cut) == pad([0, 1], cut), "inverse identity"
    )
    return polynomial(out)


def encoded(a, cut):
    return [str(v) for v in pad(a, cut)]


def pair_control(u, v, cut=8, work=None):
    u, v = rational(u), rational(v)
    require(u > 0 and v > 0, "positive pair")
    cut, work = integer(cut, 2, CUTOFF), budget(work)
    work.spend(4 * (cut + 1))
    sinh_u = [u**j / math.factorial(j) if j % 2 else Q(0) for j in range(2 * cut + 1)]
    sinh_v = [v**j / math.factorial(j) if j % 2 else Q(0) for j in range(2 * cut + 1)]
    cosh_u = [
        u**j / math.factorial(j) if not j % 2 else Q(0) for j in range(2 * cut + 1)
    ]
    cosh_v = [
        v**j / math.factorial(j) if not j % 2 else Q(0) for j in range(2 * cut + 1)
    ]
    s = multiply(sinh_u, sinh_v, 2 * cut, work)
    c = multiply(cosh_u, cosh_v, 2 * cut, work)
    direct = add(
        multiply([(u * u + v * v) / 2], s, 2 * cut, work),
        multiply([-u * v], c, 2 * cut, work),
    )
    closed = [
        rational(
            ((u - v) ** 2 * (u + v) ** (2 * j) - (u + v) ** 2 * (u - v) ** (2 * j))
            / (4 * math.factorial(2 * j)),
            internal=True,
        )
        for j in range(cut + 1)
    ]
    require(
        [pad(direct, 2 * cut)[2 * j] for j in range(cut + 1)] == closed, "pair identity"
    )
    require(closed[0] == -u * v and closed[1] == 0, "pair constant/quadratic")
    require(
        all(x > 0 for x in closed[2:]) if u != v else all(x == 0 for x in closed[1:]),
        "pair signs",
    )
    return {
        "u": str(u),
        "v": str(v),
        "cut": cut,
        "even_coefficients": [str(x) for x in closed],
        "odd_derivative_coefficients": [
            str(2 * j * closed[j]) for j in range(1, cut + 1)
        ],
        "full_quadrant_factor": "1/4",
        "ordered_half_quadrant_factor": "1/2",
        "strict_growth_control": u != v,
    }


def atoms(nodes, weights):
    require(
        type(nodes) in (list, tuple) and type(weights) in (list, tuple), "atom lists"
    )
    require(1 <= len(nodes) == len(weights) <= ATOMS, "atom count")
    nodes, weights = [rational(x) for x in nodes], [rational(x) for x in weights]
    require(all(x > 0 for x in nodes + weights), "positive atoms/weights")
    require(len(set(nodes)) == len(nodes), "duplicate atoms")
    return nodes, weights


def moment_control(nodes, weights, cut=6, work=None):
    nodes, weights = atoms(nodes, weights)
    cut, work = integer(cut, 4, CUTOFF), budget(work)
    work.spend(len(nodes) * (cut + 8))
    mu = [
        rational(
            2 * sum(w * u**r for u, w in zip(nodes, weights, strict=True)),
            internal=True,
        )
        if r % 2 == 0
        else Q(0)
        for r in range(cut + 8)
    ]

    def hs(shift, n):
        return polynomial([mu[shift + j] / math.factorial(j) for j in range(n + 1)])

    h, h1, h5, h6 = hs(0, cut), hs(1, cut), hs(5, cut + 1), hs(6, cut)
    yd5 = multiply(h6, inverse_series(h5[1:], cut, work), cut, work)
    lambda_y = multiply(h5, inverse_series(h6, cut, work), cut, work)
    small = revert_series(lambda_y, cut, work)
    d0 = multiply(h1, inverse_series(h, cut, work), cut, work)
    t = multiply([0, 1], compose(d0, small, cut, work), cut, work)
    raw = multiply(
        add([1], multiply([-1], t, cut, work)),
        inverse_series(add([1], t), cut, work),
        cut,
        work,
    )
    square = multiply(raw, raw, cut, work)
    covariance = add(
        multiply(h, h6, cut, work),
        multiply([-1], multiply(h1, h5, cut, work), cut, work),
    )
    require(
        pad(yd5, cut)[0] == 1 and pad(yd5, cut)[2] == mu[8] / (3 * mu[6]), "D5 Laurent"
    )
    require(
        pad(small, cut)[1] == 1 and pad(small, cut)[3] == mu[8] / (3 * mu[6]),
        "small root",
    )
    require(pad(raw, cut)[2] == -2 * mu[2] / mu[0], "small raw sample")
    require(pad(square, cut)[2] == -4 * mu[2] / mu[0], "physical lower coefficient")
    require(
        covariance[0] == mu[0] * mu[6] and all(x >= 0 for x in covariance), "covariance"
    )
    return {
        "positive_nodes": [str(x) for x in nodes],
        "half_line_weights": [str(x) for x in weights],
        "cut": cut,
        "moments": [str(x) for x in mu],
        "y_D5": encoded(yd5, cut),
        "lambda_of_y": encoded(lambda_y, cut),
        "small_root": encoded(small, cut),
        "raw_Theta0_small_root": encoded(raw, cut),
        "raw_Theta0_small_root_squared": encoded(square, cut),
        "covariance_K": encoded(covariance, cut),
        "actual_Xi_measure": False,
        "analytic_root_count_inferred_from_panel": False,
    }


def leading_constants():
    return {
        "D5_minus_D0_coefficient_over_y_log_y": "5",
        "D0_derivative_coefficient_over_y": "1/2",
        "root_gap_coefficient_over_log_y": str(Q(5) / Q(1, 2)),
        "lambda_log_y_limit": "2",
        "root_gap_coefficient_times_lambda": str(Q(10) / 2),
        "raw_large_coefficient_lambda_over_y_log_y": str(Q(5) / 2),
        "raw_large_coefficient_over_y_log_y_squared": str(Q(5, 2) * 2),
        "exponential_scale": "2*pi*exp(2/lambda), symbolic",
        "reduced_U_large_upper_bound_inferred": False,
    }


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    raw.decode("utf-8")
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def json_types(value, depth=0):
    require(depth <= 24, "JSON depth")
    require(type(value) in (dict, list, str, int, bool, type(None)), "JSON type")
    if type(value) is dict:
        require(len(value) <= 1024, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key")
            json_types(child, depth + 1)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            json_types(child, depth + 1)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= BITS, "JSON integer cap")


def canonical(value):
    json_types(value)
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    require(len(result.encode("utf-8")) <= MAX_BYTES, "canonical byte cap")
    return result


def parse_json(raw):
    normalized(raw)

    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def invalid(value):
        raise ValueError("nonfinite JSON " + value)

    try:
        out = json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)
        json_types(out)
        return out
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def expected_manifest():
    return {
        "schema": "xi-companion-imaginary-axis-sampling-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": {
            "urls": [
                "https://dlmf.nist.gov/25.4",
                "https://dlmf.nist.gov/5.11.E2",
                "https://dlmf.nist.gov/5.15.E9",
            ],
            "role": "normalization and differentiated gamma contracts inherited through GH/XL",
            "remote_bytes_authenticated": False,
        },
        "primitive_contract": {
            "kernel": "actual positive even Phi_Xi=2*phi_0; no frequency rescaling",
            "native_ratio": "Theta0/Theta5=U/B after maximal common G",
            "physical_projection": "P_U=M_U M_U*, adjoint value jets with retained outer metric",
            "axis": "no common positive-axis zero; finite sector only",
            "small_lambda": "global operator lower bound, not high-T geographic source",
        },
    }


def authenticate(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest bytes")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    for row in BINDINGS:
        ref = row["commit"] + ":" + row["path"]
        size = int(subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT))
        require(0 <= size <= MAX_BYTES, "primitive byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(len(raw) == size, "primitive size")
        blob = hashlib.sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
        sha = hashlib.sha256(normalized(raw)).hexdigest()
        require(
            blob == row["git_blob"] and sha == row["sha256_lf"], "primitive identity"
        )


def artifact_hashes():
    out = {}
    for path in [NOTE, Path(__file__).resolve(), MANIFEST, TEST]:
        require(path.stat().st_size <= MAX_BYTES, "artifact bytes")
        raw = normalized(path.read_bytes())
        require(
            not any(x < 32 and x not in (9, 10) for x in raw), "artifact C0 control"
        )
        out[path.relative_to(ROOT).as_posix()] = hashlib.sha256(raw).hexdigest()
    return out


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload, "unsealed payload"
    )
    digest = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
    return dict(payload, payload_sha256=digest)


def build_report():
    authenticate()
    work = Budget()
    pairs = [(1, 1), (1, 2), (2, 1), (1, 3), (2, 3), (Q(1, 2), Q(3, 2)), (Q(1, 3), 2)]
    models = [
        ([1], [1]),
        ([1, 2], [1, 1]),
        ([Q(1, 2), Q(3, 2)], [2, 1]),
        ([1, 2, 4], [1, 3, 2]),
        ([Q(1, 3), 1, 3], [1, 2, 1]),
        ([1, 2, 3, 4], [1, 1, 1, 1]),
    ]
    pair_rows = [pair_control(u, v, 8, work) for u, v in pairs]
    moment_rows = [moment_control(n, w, 6, work) for n, w in models]
    return seal(
        {
            "schema": "xi-companion-imaginary-axis-sampling-v1",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding_contract": {
                "integer_and_Fraction_only": True,
                "rounding": "none",
                "transcendental_or_Xi_samples": 0,
                "analytic_limits_are_written_proofs_not_machine_certificates": True,
            },
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "pair_controls": pair_rows,
            "moment_controls": moment_rows,
            "large_branch_constants": leading_constants(),
            "axis_classification": {
                "Theta0_positive_axis": "one simple zero",
                "Theta5_below_threshold": "two simple zeros",
                "Theta5_at_threshold": "one double zero",
                "Theta5_above_threshold": "none",
                "threshold_numerically_located": False,
                "all_denominator_axis_zeros": "lambda < y < y0(lambda)",
                "common_positive_axis_zeros": 0,
            },
            "coverage": {
                "pairs": len(pair_rows),
                "moment_models": len(moment_rows),
                "charged_work": work.used,
            },
            "caps": {
                "degree": DEGREE,
                "cutoff": CUTOFF,
                "atoms": ATOMS,
                "input_bits": INPUT_BITS,
                "internal_bits": BITS,
                "work": MAX_WORK,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "axis_theorem_uses_RH": False,
                "inner_physical_interpretation_conditional": True,
                "actual_source_preserved": True,
                "native_global_operator_norm_tends_one": True,
                "single_axis_direction_only": True,
                "high_T_geographic_direction": False,
                "global_HS_divergence_proved": False,
                "reduced_large_branch_sample_tends_zero_proved": False,
                "off_axis_common_divisor_control": False,
                "native_Riesz_or_confluent_sampling_bound": False,
                "cofinal_or_free_energy_closure": False,
                "RH_or_GRH_claim": False,
                "analytic_limits_machine_certified": False,
                "actual_Xi_numerical_samples": 0,
                "novelty_claim": False,
            },
        }
    )


def validate_report(report):
    require(type(report) is dict and "payload_sha256" in report, "sealed report")
    payload = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(canonical(report) == canonical(seal(payload)), "payload seal")
    require(
        canonical(report) == canonical(build_report()), "complete typed reconstruction"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit-report", action="store_true")
    group.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        result = expected_manifest()
    elif args.emit_report:
        result = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture bytes")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS_XI_COMPANION_IMAGINARY_AXIS_SAMPLING; analytic proof not machine-certified"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
