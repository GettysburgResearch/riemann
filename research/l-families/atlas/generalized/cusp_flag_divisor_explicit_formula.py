"""Exact finite frequency algebra for the actual cusp-flag explicit formula."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "cusp_flag_divisor_explicit_formula"
NOTE = HERE / "CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "282ce03941444d0e02daba5fde260ccb54a3f909"
MAX_CUTOFF, MAX_SUPPORT, MAX_DEGREE = 28, 512, 16
INPUT_BITS, INTERNAL_BITS, MAX_WORK, MAX_BYTES = 32, 4096, 500000, 2000000
RESIDUALS = (0, 4, 6, 8, 10, 14)
BINDINGS = [
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "kind": "reviewed_family_release",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "kind": "reviewed_family_release",
        "git_blob": "7e6ae5bb1fd9c53930cee1198eb185806a2ea118",
        "sha256_lf": "34120d58416c902db94fbeaf69ceb004694888908341b630a1b750f2f1e8316a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "kind": "reviewed_family_release",
        "git_blob": "7ca422e505e6ccd817aadee3362f1ace2fa83fd4",
        "sha256_lf": "fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "kind": "reviewed_family_release",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "kind": "reviewed_family_release",
        "git_blob": "c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a",
        "sha256_lf": "84603f0412d8a7f1d2c2384c7055f55b4956db3df68b42dde7074d18cbe8265b",
    },
    {
        "commit": "1483ff25e9100276ac7064ba7d7d696b45afb9ea",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_POSITIVE_SPECTRUM_BOUNDARY.md",
        "kind": "scientific_normalization_context",
        "git_blob": "d241501272a32771717494dd4c59aa17a6888e98",
        "sha256_lf": "62925bbe9ebe327ed491f99e886eea5599253295c69f05878d278dd453abe0d7",
    },
]
EXTERNAL = [
    {
        "url": "https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf",
        "role": "printed page277 equations6-7; theta normalization and Poisson identity",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://arxiv.org/pdf/1301.6511v2",
        "role": "section2 and Theorem3.5/Corollary3.6; signed Poisson-Newton away from zero",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://people.math.osu.edu/cogdell.1/rorsc-www.pdf",
        "role": "Theorem2.3 classical Rankin-Selberg context; not a hidden growth dependency",
        "remote_bytes_authenticated": False,
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def rational(value, *, internal=False):
    require(type(internal) is bool, "internal flag must be bool")
    require(type(value) in (int, Q), "strict rational type")
    result = Q(value)
    bits = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= bits,
        "rational bit cap",
    )
    return result


def qtext(value, *, internal=False):
    require(type(value) is str and 1 <= len(value) <= 2500, "rational text cap")
    require(all(ch in "-0123456789/" for ch in value), "rational text syntax")
    try:
        result = rational(Q(value), internal=internal)
    except (ZeroDivisionError, ValueError) as exc:
        raise ValueError("invalid rational text") from exc
    require(str(result) == value, "canonical rational text required")
    return result


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, amount):
        amount = integer(amount, 0, MAX_WORK)
        require(self.used + amount <= self.limit, "charged work cap before expansion")
        self.used += amount


def checked_work(work):
    require(type(work) is Budget, "Budget required")
    return work


def cutoff_value(value):
    result = rational(value)
    require(1 <= result <= MAX_CUTOFF, "cutoff domain")
    return result


def checked_series(value, cutoff, *, constant):
    require(type(constant) is bool, "constant flag must be bool")
    cutoff = cutoff_value(cutoff)
    require(
        type(value) is dict and len(value) <= MAX_SUPPORT, "series shape/support cap"
    )
    result = {}
    for frequency, coefficient in value.items():
        frequency = rational(frequency)
        coefficient = rational(coefficient, internal=True)
        require(
            (frequency >= 1 if constant else frequency > 1) and frequency <= cutoff,
            "frequency domain",
        )
        if coefficient:
            result[frequency] = coefficient
    if constant:
        require(result.get(Q(1)) == 1, "normalized constant coefficient required")
    return result


def accumulate(out, frequency, coefficient):
    require(type(out) is dict and len(out) <= MAX_SUPPORT, "accumulator shape/cap")
    frequency = rational(frequency, internal=True)
    require(frequency >= 1, "accumulator frequency domain")
    coefficient = rational(coefficient, internal=True)
    updated = rational(out.get(frequency, Q(0)) + coefficient, internal=True)
    if updated:
        out[frequency] = updated
    else:
        out.pop(frequency, None)
    require(len(out) <= MAX_SUPPORT, "output support cap")


def product(left, right, cutoff, work):
    cutoff = cutoff_value(cutoff)
    require(
        type(left) is dict
        and type(right) is dict
        and max(len(left), len(right)) <= MAX_SUPPORT,
        "product input support cap",
    )
    checked_work(work).spend(len(left) * len(right))
    for series in (left, right):
        for frequency, coefficient in series.items():
            require(rational(frequency, internal=True) >= 1, "product frequency domain")
            rational(coefficient, internal=True)
    out = {}
    for a, x in left.items():
        for b, y in right.items():
            frequency = rational(a * b, internal=True)
            if frequency <= cutoff:
                accumulate(out, frequency, rational(x * y, internal=True))
    return out


def word_degree(minimum, cutoff):
    minimum = rational(minimum, internal=True)
    require(minimum > 1, "positive logarithmic generator required")
    cutoff = cutoff_value(cutoff)
    degree, power = 0, Q(1)
    while power * minimum <= cutoff:
        require(degree < MAX_DEGREE, "word degree cap; do not truncate silently")
        power = rational(power * minimum, internal=True)
        degree += 1
    return degree, rational(power * minimum, internal=True)


def minus_log_prefix(series, cutoff, work=None):
    cutoff = cutoff_value(cutoff)
    series = checked_series(series, cutoff, constant=True)
    work = Budget() if work is None else checked_work(work)
    h = {
        frequency: coefficient
        for frequency, coefficient in series.items()
        if frequency > 1
    }
    if not h:
        return {}, 0, None
    degree, next_frequency = word_degree(min(h), cutoff)
    out, power = {}, {Q(1): Q(1)}
    for order in range(1, degree + 1):
        power = product(power, h, cutoff, work)
        work.spend(len(power))
        for frequency, coefficient in power.items():
            accumulate(out, frequency, Q((-1) ** order, order) * coefficient)
    return out, degree, next_frequency


def exp_minus_prefix(series, cutoff, work=None):
    cutoff = cutoff_value(cutoff)
    series = checked_series(series, cutoff, constant=False)
    work = Budget() if work is None else checked_work(work)
    out, power = {Q(1): Q(1)}, {Q(1): Q(1)}
    if not series:
        return out
    degree, _ = word_degree(min(series), cutoff)
    for order in range(1, degree + 1):
        power = product(power, series, cutoff, work)
        work.spend(len(power))
        for frequency, coefficient in power.items():
            accumulate(
                out, frequency, Q((-1) ** order, math.factorial(order)) * coefficient
            )
    return out


def zeta_minus_log(weight, cutoff, work=None):
    weight = integer(weight, 2, 302)
    cutoff = cutoff_value(cutoff)
    work = Budget() if work is None else checked_work(work)
    top = math.isqrt(cutoff.numerator // cutoff.denominator)
    work.spend(top * top)
    out = {}
    for prime in range(2, top + 1):
        if any(prime % d == 0 for d in range(2, math.isqrt(prime) + 1)):
            continue
        power, order = prime * prime, 1
        while power <= cutoff:
            work.spend(1)
            accumulate(out, Q(power), -Q(prime ** ((2 * weight - 2) * order), order))
            power *= prime * prime
            order += 1
    return out


def decode_parent_map(value, cutoff):
    require(type(value) is dict and len(value) <= MAX_SUPPORT, "parent map cap")
    converted = {}
    for key, coefficient in value.items():
        frequency = qtext(key)
        require(type(coefficient) is int, "parent coefficient must be integer")
        converted[frequency] = rational(coefficient, internal=True)
    return checked_series(converted, cutoff, constant=True)


def encoded_map(value):
    return {str(key): str(value[key]) for key in sorted(value)}


def frequency_control(row, work=None):
    require(type(row) is dict, "parent row type")
    work = Budget() if work is None else checked_work(work)
    d = integer(row["dimension"], 2, 24)
    r = row["residual"]
    require(type(r) is int and r in RESIDUALS, "parent residual")
    weight = integer(row["weight"], 24, 302)
    require(weight == 12 * d + r, "parent weight")
    require(
        row["complete_tail_and_word_coverage_by_CF9"] is True,
        "parent coverage contract",
    )
    cutoff = cutoff_value(qtext(row["cutoff"]))
    target = qtext(row["first_fractional_frequency"])
    require(target.denominator > 1, "fractional target")
    a_star = row["first_fractional_coefficient_w"]
    require(type(a_star) is int and a_star < 0, "negative source target coefficient")
    a_star = rational(a_star, internal=True)
    first = decode_parent_map(row["bare_F"], cutoff)
    second = decode_parent_map(row["zeta_times_F"], cutoff)
    require(
        first.get(target) == second.get(target) == a_star, "parent target collision"
    )
    log_f, degree_f, next_f = minus_log_prefix(first, cutoff, work)
    log_l, degree_l, next_l = minus_log_prefix(second, cutoff, work)
    require(
        exp_minus_prefix(log_f, cutoff, work) == first, "complete F exponential inverse"
    )
    require(
        exp_minus_prefix(log_l, cutoff, work) == second,
        "complete L exponential inverse",
    )
    difference = dict(log_l)
    for frequency, coefficient in log_f.items():
        accumulate(difference, frequency, -coefficient)
    zeta = zeta_minus_log(weight, cutoff, work)
    require(difference == zeta, "independent zeta prime-power correction")
    require(
        log_f.get(target) == log_l.get(target) == -a_star, "fractional log atom changed"
    )
    log_s = {
        rho: rational(coefficient * rho ** (-(weight - 1)), internal=True)
        for rho, coefficient in log_l.items()
    }
    first_frequency = min(log_l)
    require(log_l[first_frequency] < 0 and log_l[target] > 0, "signed atom calibration")
    return {
        "weight": weight,
        "dimension": d,
        "residual": r,
        "cutoff": str(cutoff),
        "minus_log_F_w": encoded_map(log_f),
        "minus_log_L_w": encoded_map(log_l),
        "minus_log_L_in_s": encoded_map(log_s),
        "zeta_minus_log_difference": encoded_map(zeta),
        "maximum_log_degree_F_L": [degree_f, degree_l],
        "next_word_lower_bound_F_L": [str(next_f), str(next_l)],
        "exponential_reconstruction_complete": True,
        "fractional_frequency": str(target),
        "fractional_b_w": str(-a_star),
        "fractional_PN_rational_multiplier_s": str(log_s[target]),
        "PN_mass_contract": "mass at t=log(rho) is log(rho) times minus_log_L_in_s[rho]",
        "first_atom_frequency": str(first_frequency),
        "first_atom_b_w": str(log_l[first_frequency]),
        "actual_zero_or_pole_samples": 0,
    }


def completion_control(weight):
    weight = integer(weight, 2, 302)
    samples = sorted({1, 0, -1, -(weight - 2), -(weight - 1), -weight})
    gamma_orders = {str(s): -int(s <= 0) - int(s <= -(weight - 1)) for s in samples}
    endpoints = {str(s): -1 - gamma_orders[str(s)] for s in (0, 1)}
    require(endpoints == {"0": 0, "1": -1}, "native endpoint cancellation")
    require(gamma_orders[str(-(weight - 1))] == -2, "overlapping gamma ladders")
    return {
        "weight": weight,
        "A_gamma_signed_orders": gamma_orders,
        "source_Q_endpoint_orders": {"0": -1, "1": -1},
        "L_in_s_endpoint_orders": endpoints,
        "kernel_contract": "-(1+exp(-(k-1)*t))/(1-exp(-t)) for t>0",
        "unknown_actual_determinant_divisor_supplied": False,
    }


def theta_jensen_control(root_u, height, radius):
    root_u, height, radius = rational(root_u), rational(height), rational(radius)
    require(root_u >= 1 and height >= 1 and radius >= 1, "positive finite calibration")
    require(max(root_u, height, radius) <= 32, "calibration magnitude cap")
    gap = 2 * height + root_u * root_u / (2 * height) - 2 * root_u
    square = (2 * height - root_u) ** 2 / (2 * height)
    require(gap == square and gap >= 0, "theta reserve algebra")
    require(root_u * root_u >= root_u, "u>=sqrt(u)")
    return {
        "sqrt_u": str(root_u),
        "height": str(height),
        "theta_gap_divided_by_pi": str(gap),
        "Jensen_input_radius": str(radius),
        "Jensen_center": 2,
        "inner_radius": str(radius + 2),
        "outer_radius": str(2 * radius + 4),
        "global_outer_radius": str(2 * radius + 6),
        "numerical_theta_Gamma_or_Jensen_value": False,
    }


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    raw.decode("utf-8")
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lf_sha(raw):
    return hashlib.sha256(normalized(raw)).hexdigest()


def json_types(value, depth=0):
    require(depth <= 24, "JSON depth cap")
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
        require(abs(value).bit_length() <= INTERNAL_BITS, "JSON integer cap")


def canonical(value):
    json_types(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


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
        value = json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
        json_types(value)
        return value
    except (RecursionError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def manifest_expected():
    return {
        "schema": "cusp-flag-divisor-explicit-formula-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": [dict(row) for row in EXTERNAL],
        "primitive_contract": {
            "object": "actual full cusp-flag quotient Q=det I/det I_W; CF1-CF12",
            "logarithm": "-log L(w); lambda=log(rho), w=s+k-1",
            "atomic_mass_s": "lambda*b_lambda*exp(-(k-1)*lambda)",
            "gamma_kernel": "-(1+exp(-(k-1)*t))/(1-exp(-t)); t>0",
            "test_space": "C_c^infinity((0,infinity)); origin excluded",
            "parent_prefix": "complete reviewed CF9 frequency prefixes; parent q/word producer not rerun",
        },
    }


def authenticated_sources(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(manifest_expected()), "complete typed manifest"
    )
    parent = None
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
            "primitive identity",
        )
        if row["path"].endswith("/cusp_flag_quotient_global_family.json"):
            parent = parse_json(raw)
    require(
        type(parent) is dict
        and parent.get("schema") == "cusp-flag-quotient-global-family-v1",
        "parent schema",
    )
    return parent


def artifact_hashes():
    out = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        out[path.relative_to(ROOT).as_posix()] = lf_sha(path.read_bytes())
    return out


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload,
        "unsealed payload required",
    )
    raw = canonical(payload).encode()
    require(len(raw) <= MAX_BYTES, "payload byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(raw).hexdigest()}


def build_report():
    parent = authenticated_sources()
    rows = parent["frequency_controls"]
    require(type(rows) is list and len(rows) == 6, "six complete parent prefixes")
    require(
        [(r["dimension"], r["residual"], r["cutoff"]) for r in rows]
        == [
            (2, 0, "12"),
            (3, 0, "10"),
            (3, 14, "8"),
            (4, 0, "10"),
            (10, 4, "14"),
            (20, 8, "24"),
        ],
        "ordered prefix coverage",
    )
    work = Budget()
    controls = [frequency_control(row, work) for row in rows]
    return seal(
        {
            "schema": "cusp-flag-divisor-explicit-formula-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; log(rho) is symbolic",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "frequency_controls": controls,
            "completion_controls": [completion_control(row["weight"]) for row in rows],
            "theta_Jensen_algebra": [
                theta_jensen_control(*args)
                for args in ((1, 1, 1), (2, 1, Q(3, 2)), (7, 2, 8))
            ],
            "Mellin_integer_controls": [
                {
                    "R": r,
                    "power_of_c_in_denominator": 2 * r + 2,
                    "integral_0_infinity_u_to_R_exp_minus_c_sqrt_u_multiplier": 2
                    * math.factorial(2 * r + 1),
                }
                for r in (1, 2, 3, 4)
            ],
            "coverage": {
                "complete_parent_prefixes": 6,
                "F_and_L_log_prefixes": 12,
                "parent_q_word_producer_rerun": False,
                "charged_work": work.used,
            },
            "caps": {
                "cutoff": MAX_CUTOFF,
                "support": MAX_SUPPORT,
                "word_degree": MAX_DEGREE,
                "frequency_input_bits": INPUT_BITS,
                "coefficient_internal_bits": INTERNAL_BITS,
                "work": MAX_WORK,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "actual_fixed_weight_full_cusp_flag_source": True,
                "meromorphic_order_at_most_one_by_written_proof": True,
                "unsigned_count_bound": "O_k(R log(R+2)); constants not numerically certified",
                "Q_net_divisor_finite_vertical_strip": True,
                "L_divisor_assigned_same_strip": False,
                "signed_net_divisor_multiplicities": True,
                "test_space": "C_c^infinity((0,infinity))",
                "pointwise_zero_exponential_series_asserted": False,
                "origin_delta_discarded_for_tests_meeting_zero": False,
                "finite_zero_census_substituted": False,
                "actual_zero_or_pole_samples": 0,
                "numerical_growth_constants_or_Jensen_anchors": False,
                "analytic_proof_machine_certified": False,
                "positive_Weil_RH_GRH_or_novelty_claim": False,
            },
        }
    )


def validate_report(report):
    require(
        type(report) is dict and "payload_sha256" in report, "sealed report required"
    )
    payload = {key: value for key, value in report.items() if key != "payload_sha256"}
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
        result = manifest_expected()
    elif args.emit_report:
        result = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS_CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA; analytic proof is not machine certification"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
