"""Exact local controls for generic native Xi companion coprimality."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_companion_generic_parameter_coprimality"
NOTE = HERE / "XI_COMPANION_GENERIC_PARAMETER_COPRIMALITY.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "cce5552c9de8a6ec0206977fdd7119a7fab3d874"
INPUT_BITS, BITS, MAX_DEGREE, INTERNAL_DEGREE = 32, 4096, 16, 32
MAX_WORK, MAX_BYTES, MAX_NODES = 200000, 2000000, 20000
BINDINGS = [
    {
        "commit": "d38961c15fc76d671cef4fddfc92d3c866af4fd5",
        "git_blob": "9688e30825fcc3d2b13570539bf03299407eae87",
        "id": "NA",
        "path": "research/exploratory/XI_COMPANION_IMAGINARY_AXIS_SAMPLING.md",
        "role": "AX1-2 moments and companion; AX7 no common axis zero; AX21 Wronskian",
        "sha256_lf": "a9d6b51b3b2f1ccb388fb8d74e115023c622115b169d3214f071ef9005034081",
    },
    {
        "commit": "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d",
        "git_blob": "e592a4c031876f56f07d28b7e18a8a7cf6e826f4",
        "id": "GH",
        "path": "research/exploratory/XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md",
        "role": "GH1-4 native ratio and inner premise; GH3/16 pure component infinite height",
        "sha256_lf": "5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d",
    },
    {
        "commit": "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "git_blob": "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "id": "XL",
        "path": "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "role": "XL1-4 actual Phi=2phi0; XL11 entire positive-kernel moment justification",
        "sha256_lf": "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    },
    {
        "commit": "36eddbbf065959f535ca4a7b08455d489ed4bd18",
        "git_blob": "d44f3b58e7dbd9ec847d771b2299c6fabc21f5df",
        "id": "LP",
        "path": "research/exploratory/HARDY_LOW_PASS_HEIGHT_EQUIVALENCE.md",
        "role": "LP1-3 pure Blaschke infinite height implies every bare zero-start lowpass trace infinite",
        "sha256_lf": "ca94d882bc9ee69ae8e0a277ccc13ca7e7b86ab95a52d60eed16bb110f32bc72",
    },
    {
        "commit": "7aed2ec0b99b9d7f2fb94a774922a83d5b84a870",
        "git_blob": "cd74bd06267eb4d60bc977353d11f6a0fb72ba6a",
        "id": "CP",
        "path": "research/exploratory/COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md",
        "role": "CP2-4 coprime infinite-height does not imply corrected physical trace divergence",
        "sha256_lf": "b9ab266898129389b94a9ed494b140422fc823552c6b69bf22ed36a9dbb2e7f7",
    },
    {
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "git_blob": "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "id": "L106620",
        "path": "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "role": "L106620.1,.4-.6 constant positive lambda and native Theta0/Theta5",
        "sha256_lf": "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    },
]
CONTROLS = {
    "genuine": [5, 0, 0, 0, 0, 0, -1],
    "real_rooted_common": [125, 0, -75, 0, 15, 0, -1],
    "excess_W_order": [5, 0, -15, 0, -5, 0, -1],
    "cancelled_raw": [1, 0, -25, 0, -60, 0, -42, 0, -9, 0, -1],
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def rational(value, *, internal=False):
    require(type(internal) is bool, "internal flag")
    require(type(value) in (int, Q), "strict rational type")
    result = Q(value)
    cap = BITS if internal else INPUT_BITS
    require(
        max(abs(result.numerator).bit_length(), result.denominator.bit_length()) <= cap,
        "rational bit cap",
    )
    return result


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, amount):
        amount = integer(amount, 0, MAX_WORK)
        require(self.used + amount <= self.limit, "work cap before expansion")
        self.used += amount


def budget(work):
    require(type(work) is Budget, "Budget required")
    return work


def gauss(value, *, internal=False):
    require(type(value) in (tuple, list) and len(value) == 2, "Gaussian pair shape")
    return tuple(rational(x, internal=internal) for x in value)


def plus(a, b):
    a, b = gauss(a, internal=True), gauss(b, internal=True)
    return gauss((a[0] + b[0], a[1] + b[1]), internal=True)


def minus(a, b):
    return plus(a, tuple(-x for x in gauss(b, internal=True)))


def times(a, b):
    a, b = gauss(a, internal=True), gauss(b, internal=True)
    return gauss((a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]), internal=True)


def divide(a, b):
    a, b = gauss(a, internal=True), gauss(b, internal=True)
    denominator = rational(b[0] ** 2 + b[1] ** 2, internal=True)
    require(denominator != 0, "Gaussian division by zero")
    out = times(a, (b[0], -b[1]))
    return gauss(tuple(x / denominator for x in out), internal=True)


def trim(row):
    row = list(row)
    while len(row) > 1 and row[-1] == 0:
        row.pop()
    return row


def polynomial(row, *, internal=False):
    require(type(internal) is bool, "internal flag")
    cap = INTERNAL_DEGREE if internal else MAX_DEGREE
    require(
        type(row) in (list, tuple) and 1 <= len(row) <= cap + 1,
        "polynomial degree/shape",
    )
    return trim([rational(v, internal=internal) for v in row])


def derivative(row, order, work):
    row = polynomial(row, internal=True)
    order = integer(order, 0, INTERNAL_DEGREE)
    budget(work).spend((len(row) + 1) * (order + 1))
    for _ in range(order):
        row = [rational(j * row[j], internal=True) for j in range(1, len(row))] or [
            Q(0)
        ]
    return row


def real_product(a, b, work):
    a, b = polynomial(a, internal=True), polynomial(b, internal=True)
    degree = len(a) + len(b) - 2
    require(degree <= INTERNAL_DEGREE, "product degree cap")
    budget(work).spend(len(a) * len(b))
    out = [Q(0)] * (degree + 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] = rational(out[j + k] + x * y, internal=True)
    return trim(out)


def real_difference(a, b):
    a, b = polynomial(a, internal=True), polynomial(b, internal=True)
    return trim(
        [
            rational(
                (a[j] if j < len(a) else 0) - (b[j] if j < len(b) else 0), internal=True
            )
            for j in range(max(len(a), len(b)))
        ]
    )


def evaluate(row, point, work):
    row, point = polynomial(row, internal=True), gauss(point, internal=True)
    budget(work).spend(len(row))
    out = (Q(0), Q(0))
    for x in reversed(row):
        out = plus(times(out, point), (x, Q(0)))
    return out


def order_at(row, point, work):
    row = polynomial(row, internal=True)
    require(any(row), "zero polynomial has no finite zero order")
    for j in range(len(row)):
        if evaluate(derivative(row, j, work), point, work) != (0, 0):
            return j
    raise ValueError("finite order reconstruction")


def companion_value(row, point, lam, sign, work):
    lam = rational(lam)
    require(lam > 0 and type(sign) is int and sign in (-1, 1), "positive scale/sign")
    h = evaluate(row, point, work)
    hp = evaluate(derivative(row, 1, work), point, work)
    return plus(h, times((0, sign * lam), hp))


def companion_order(row, point, lam, sign, work):
    row = polynomial(row, internal=True)
    require(any(row), "nonzero companion input")
    for j in range(len(row)):
        value = companion_value(derivative(row, j, work), point, lam, sign, work)
        if value != (0, 0):
            return j, value
    raise ValueError("nonzero polynomial companion")


def local_quotient(row, point, lam, work):
    row = polynomial(row)
    point, lam = gauss(point), rational(lam)
    require(any(row) and lam > 0, "nonzero h and positive lambda")
    budget(work)
    numerator, nlead = companion_order(row, point, lam, -1, work)
    denominator, dlead = companion_order(row, point, lam, 1, work)
    return {
        "h_zero_order": order_at(row, point, work),
        "numerator_order": numerator,
        "denominator_order": denominator,
        "internal_cancelled_order": min(numerator, denominator),
        "genuine_zero_order": max(0, numerator - denominator),
        "pole_order": max(0, denominator - numerator),
        "regular_nonzero_value": divide(nlead, dlead)
        if numerator == denominator
        else None,
    }


def wronskian(row, work):
    row = polynomial(row)
    require(len(row) >= 7, "derivative-linked degree at least6")
    first = derivative(row, 1, work)
    fifth = derivative(row, 5, work)
    sixth = derivative(row, 6, work)
    return real_difference(
        real_product(row, sixth, work), real_product(first, fifth, work)
    )


def complex_product(a, b, work):
    for row in (a, b):
        require(
            type(row) in (list, tuple) and 1 <= len(row) <= INTERNAL_DEGREE + 1,
            "complex polynomial shape",
        )
        for v in row:
            gauss(v, internal=True)
    require(len(a) + len(b) - 2 <= INTERNAL_DEGREE, "complex product degree cap")
    budget(work).spend(len(a) * len(b))
    out = [(Q(0), Q(0))] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = plus(out[i + j], times(x, y))
    return out


def companion_coefficients(row, lam, sign, work):
    row = polynomial(row, internal=True)
    lam = rational(lam)
    require(lam > 0 and type(sign) is int and sign in (-1, 1), "positive scale/sign")
    dp = derivative(row, 1, work)
    return [
        (x, rational(sign * lam * (dp[j] if j < len(dp) else 0), internal=True))
        for j, x in enumerate(row)
    ]


def exact_bridge(row, lam, work):
    row = polynomial(row)
    g = derivative(row, 5, work)
    r0, c0 = (companion_coefficients(row, lam, sign, work) for sign in (-1, 1))
    r5, c5 = (companion_coefficients(g, lam, sign, work) for sign in (-1, 1))
    lhs1, lhs2 = complex_product(r0, c5, work), complex_product(c0, r5, work)
    w = wronskian(row, work)
    expected = [(Q(0), rational(2 * lam * x, internal=True)) for x in w]
    expected += [(Q(0), Q(0))] * (len(lhs1) - len(expected))
    require(
        [minus(x, y) for x, y in zip(lhs1, lhs2, strict=True)] == expected,
        "coefficientwise 2i lambda W",
    )
    differentiated = [
        tuple(
            rational(math.factorial(j + 5) * v / math.factorial(j), internal=True)
            for v in r0[j + 5]
        )
        for j in range(len(r0) - 5)
    ]
    require(differentiated == r5, "constant lambda derivative linkage")
    return {
        "coefficient_count": len(expected),
        "difference_factor": 2,
        "R5_equals_fifth_derivative_R0": True,
    }


def control(name, point, lam, work):
    require(type(name) is str and name in CONTROLS, "fixed nonnative control enum")
    point, lam = gauss(point), rational(lam)
    require(point[1] > 0 and lam > 0, "upper point and positive fixed parameter")
    row = polynomial(CONTROLS[name])
    g, gp = derivative(row, 5, work), derivative(row, 6, work)
    w = wronskian(row, work)
    fvalue = evaluate(row, point, work)
    fpvalue = evaluate(derivative(row, 1, work), point, work)
    gpvalue = evaluate(gp, point, work)
    wvalue = evaluate(w, point, work)
    quotient_f = local_quotient(row, point, lam, work)
    # The derivative has bounded internal coefficients; local normalization
    # preserves the quotient while meeting the public rational input cap.
    scale = max(Q(1), max(abs(x) for x in g))
    normalized_g = [x / scale for x in g]
    quotient_g = local_quotient(normalized_g, point, lam, work)
    derivatives_nonzero = fpvalue != (0, 0) and gpvalue != (0, 0)
    ratio = divide(fvalue, times((0, 1), fpvalue)) if fpvalue != (0, 0) else None
    criterion = wvalue == (0, 0) and derivatives_nonzero and ratio == (lam, 0)
    common = (
        quotient_f["genuine_zero_order"] > 0 and quotient_g["genuine_zero_order"] > 0
    )
    require(criterion == common, "cancellation-safe iff")
    worder = order_at(w, point, work)
    if common:
        require(
            min(quotient_f["genuine_zero_order"], quotient_g["genuine_zero_order"])
            <= worder,
            "Wronskian multiplicity domination",
        )
    return {
        "model": name,
        "native_Xi": False,
        "positive_kernel_surrogate": False,
        "point": point,
        "lambda": lam,
        "f_coefficients": row,
        "g_coefficients": g,
        "W_coefficients": w,
        "W_value": wvalue,
        "W_zero_order": worder,
        "fprime_gprime_nonzero": derivatives_nonzero,
        "ratio_f_over_ifprime": ratio,
        "criterion": criterion,
        "genuine_common_zero": common,
        "Theta0_local": quotient_f,
        "Theta5_local": quotient_g,
        "coefficientwise_bridge": exact_bridge(row, lam, work),
    }


def cancellation_control(multiplicity, lam, work):
    multiplicity = integer(multiplicity, 1, 8)
    lam = rational(lam)
    require(lam > 0, "positive lambda")
    row = [Q(0)] * (2 * multiplicity + 1)
    for j in range(multiplicity + 1):
        row[2 * j] = Q(math.comb(multiplicity, j))
    local = local_quotient(row, (0, 1), lam, work)
    require(local["h_zero_order"] == multiplicity, "literal h multiplicity")
    require(local["internal_cancelled_order"] == multiplicity - 1, "cancel exactly r-1")
    require(
        local["regular_nonzero_value"] == (-1, 0) and local["genuine_zero_order"] == 0,
        "removable value minus1",
    )
    return {
        "multiplicity": multiplicity,
        "lambda": lam,
        "local": local,
        "native_Xi": False,
    }


def moment_control(mu0, mu6):
    mu0, mu6 = rational(mu0), rational(mu6)
    require(mu0 > 0 and mu6 > 0, "positive moments")
    phase = (Q(1), Q(0))
    for _ in range(6):
        phase = times(phase, (0, 1))
    value = times((mu0, 0), times(phase, (mu6, 0)))
    require(value == (-mu0 * mu6, 0) and value[0] < 0, "W0 moment sign")
    return {
        "mu0": mu0,
        "mu6": mu6,
        "i_power6": phase,
        "W0": value,
        "actual_Xi_moments_evaluated": False,
    }


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    try:
        raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("UTF8 required") from exc
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lf_sha(raw):
    return hashlib.sha256(normalized(raw)).hexdigest()


def json_types(value, depth=0, counts=None):
    counts = [0, 0] if counts is None else counts
    counts[0] += 1
    require(counts[0] <= MAX_NODES and depth <= 24, "JSON node/depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "strict JSON type")
    if type(value) is dict:
        require(len(value) <= 1024, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key")
            counts[1] += len(key.encode("utf-8"))
            require(counts[1] <= MAX_BYTES, "JSON text cap")
            json_types(child, depth + 1, counts)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            json_types(child, depth + 1, counts)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
        counts[1] += len(value.encode("utf-8"))
        require(counts[1] <= MAX_BYTES, "JSON text cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= BITS, "JSON integer cap")


def canonical(value):
    json_types(value)
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    require(len(raw.encode()) <= MAX_BYTES, "canonical byte cap")
    return raw


def serialize(value):
    if type(value) is Q:
        return str(value)
    if type(value) in (list, tuple):
        return [serialize(v) for v in value]
    if type(value) is dict:
        return {k: serialize(v) for k, v in value.items()}
    return value


def parse_json(raw):
    normalized(raw)

    def pairs(items):
        out = {}
        for key, value in items:
            require(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def nonfinite(value):
        raise ValueError("nonfinite JSON " + value)

    try:
        out = json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
        json_types(out)
        return out
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def expected_manifest():
    return {
        "schema": "xi-companion-generic-parameter-coprimality-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "primitive_contract": {
            "source": "actual unrescaled Xi, Phi=2phi0, g=f fifth derivative",
            "lambda": "one positive constant; not variable scale or gauge reselection",
            "exceptional_set": "Wzero plus fprime*gprime nonzero plus f/(i*fprime) positive real",
            "equivalence": "exact genuine common zero iff exceptional membership",
            "nonvanishing": "W(0)=-mu0*mu6<0 from positive actual kernel",
            "conditional": "outside E AND both companions inner; RH sufficient not proved",
            "downstream": "pure coprime reduced infinite heights and bare [0,L] traces only",
            "excluded": "no explicit good lambda, finite/dense E claim, physical capture, prescribed gauge or RH conclusion",
            "execution": "no ancestor code or actual Xi numeric values",
        },
    }


def authenticated_sources(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    for row in BINDINGS:
        ref = row["commit"] + ":" + row["path"]
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", ref], cwd=ROOT, timeout=15
            )
        )
        require(0 <= size <= MAX_BYTES, "primitive byte cap")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and lf_sha(raw) == row["sha256_lf"],
            "frozen primitive identity",
        )
    return len(BINDINGS)


def artifact_hashes():
    out = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        raw = path.read_bytes()
        require(
            all(v >= 32 or v in (9, 10, 13) for v in raw), "artifact control character"
        )
        out[path.relative_to(ROOT).as_posix()] = lf_sha(raw)
    return out


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload,
        "unsealed payload required",
    )
    return {
        **payload,
        "payload_sha256": hashlib.sha256(canonical(payload).encode()).hexdigest(),
    }


def build_report():
    count = authenticated_sources()
    work = Budget()
    controls = [
        control(name, point, lam, work)
        for name, point, lam in (
            ("genuine", (0, 1), Q(1)),
            ("genuine", (0, 1), Q(1, 2)),
            ("genuine", (1, 1), Q(1)),
            ("excess_W_order", (0, 1), Q(1)),
            ("cancelled_raw", (0, 1), Q(1, 2)),
            ("cancelled_raw", (0, 1), Q(1)),
            ("cancelled_raw", (0, 1), Q(2)),
            ("real_rooted_common", (0, 1), Q(1)),
        )
    ]
    cancellations = [
        cancellation_control(m, lam, work)
        for m in range(1, 9)
        for lam in (Q(1, 2), Q(1), Q(3))
    ]
    return seal(
        serialize(
            {
                "schema": "xi-companion-generic-parameter-coprimality-v1",
                "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
                "arithmetic_class": "MIXED",
                "arithmetic_components": [
                    "EXACT_RATIONAL",
                    "CERTIFIED_INTEGER_COVERAGE",
                ],
                "rounding_contract": "exact integers/Fraction Gaussian pairs; no rounding or analytic sampling",
                "frozen_sources": [dict(row) for row in BINDINGS],
                "artifact_sha256_lf": artifact_hashes(),
                "local_derivative_linked_controls": controls,
                "internal_cancellation_controls": cancellations,
                "moment_sign_controls": [
                    moment_control(a, b)
                    for a, b in ((1, 1), (2, 3), (Q(3, 7), Q(5, 11)))
                ],
                "coverage": {
                    "source_notes": count,
                    "linked_controls": len(controls),
                    "cancellation_controls": len(cancellations),
                    "charged_work": work.used,
                },
                "caps": {
                    "public_bits": INPUT_BITS,
                    "internal_bits": BITS,
                    "input_degree": MAX_DEGREE,
                    "internal_degree": INTERNAL_DEGREE,
                    "work": MAX_WORK,
                    "bytes": MAX_BYTES,
                    "json_nodes": MAX_NODES,
                },
                "scope": {
                    "actual_source_exceptional_set_countable_unconditionally": True,
                    "exact_common_zero_equivalence": True,
                    "bounded_disk_parameter_image_finite": True,
                    "minimum_multiplicity_dominated": True,
                    "no_positive_axis_exception_point": True,
                    "reduced_infinite_heights_only_with_inner_premise_and_lambda_outside_E": True,
                    "bare_every_fixed_zero_start_lowpass_under_same_premises": True,
                    "E_is_empty_or_nonempty_decided": False,
                    "E_is_finite_or_locally_finite_in_parameter_space": False,
                    "E_is_dense_asserted": False,
                    "explicit_good_parameter": False,
                    "prescribed_physical_parameters_avoid_E": False,
                    "gauge_reselection_authorized": False,
                    "uniform_or_shifted_shrinking_band_claim": False,
                    "corrected_physical_capture_or_fixed_lambda_HS_divergence": False,
                    "RH_or_density_conclusion": False,
                    "native_Xi_values_or_zeros_sampled": 0,
                    "analytic_limits_machine_certified": False,
                    "new_abstract_principle_or_exhaustive_novelty": False,
                    "parents_modified": False,
                },
            }
        )
    )


def validate_report(report):
    require(
        type(report) is dict and "payload_sha256" in report, "sealed report required"
    )
    payload = {k: v for k, v in report.items() if k != "payload_sha256"}
    require(canonical(report) == canonical(seal(payload)), "payload digest")
    require(
        canonical(report) == canonical(build_report()), "complete typed reconstruction"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit-report", action="store_true")
    mode.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        out = expected_manifest()
    elif args.emit_report:
        out = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS_XI_GENERIC_PARAMETER_COPRIMALITY; independent analytic review required"
        )
        return
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
