"""Bounded exact controls for native all-W separation and uncancelled cusp zeros."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import types
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "cusp_flag_uncancelled_off_central_real_zeros"
NOTE = HERE / "CUSP_FLAG_UNCANCELLED_OFF_CENTRAL_REAL_ZEROS.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717"
MAX_DEGREE, MAX_K, MAX_WORK = 12, 12288, 2000000
FAMILY_WORK, CUSP_WORK, BITS, MAX_BYTES, MAX_JSON_NODES = (
    100000,
    100000,
    4096,
    2000000,
    20000,
)

BINDINGS = [
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "native_family",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "native_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "git_blob": "7e6ae5bb1fd9c53930cee1198eb185806a2ea118",
        "sha256_lf": "34120d58416c902db94fbeaf69ceb004694888908341b630a1b750f2f1e8316a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "native_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "git_blob": "7ca422e505e6ccd817aadee3362f1ace2fa83fd4",
        "sha256_lf": "fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "native_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "native_family",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "git_blob": "c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a",
        "sha256_lf": "84603f0412d8a7f1d2c2384c7055f55b4956db3df68b42dde7074d18cbe8265b",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "reviewed_cusp_parent_release",
        "path": "research/l-families/atlas/generalized/CUSP_PERIOD_OFF_CENTRAL_REAL_ZEROS.md",
        "git_blob": "0fcafec61b564a1f2db4c15d24c881d99b8ebcd1",
        "sha256_lf": "cb792b56a687922573711027d9d6a43221d468c0d42311251d4b882c2d7f7906",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "reviewed_cusp_parent_release",
        "path": "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.py",
        "git_blob": "40e65f048cf602f937e326b1e1594c08da81c471",
        "sha256_lf": "cc573a19d3e64344bcb217dafb86094470b4af15304f0c647f090eb12d3fd66c",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "reviewed_cusp_parent_release",
        "path": "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.json",
        "git_blob": "ec6698279aed159326220061ccf36d6cd7ae15cd",
        "sha256_lf": "ea44f9b40af18e6657729b6bb2e2b2ffdf9d814c596f77d7b8542b4249406514",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "reviewed_cusp_parent_release",
        "path": "research/l-families/atlas/generalized/cusp_period_off_central_real_zeros.sources.json",
        "git_blob": "0d5ec23bab396ccf2d16cff89247805b935706e3",
        "sha256_lf": "35490b7422b93e2623cc492ab8fc3689f6aa969d9daec2d2caaf5c49e4887721",
    },
    {
        "commit": "a12d0fbc9b17a29f4eb3aa7f984877ffd4c5e717",
        "kind": "reviewed_cusp_parent_release",
        "path": "tests/test_cusp_period_off_central_real_zeros.py",
        "git_blob": "4f047bf05250ea6e70f93ae06ab26903b019b2ff",
        "sha256_lf": "f256d73577dc6babd3fa652f1f69738e72d26d23edc219ae8eb103d639c920ff",
    },
]


EXTERNAL = [
    {
        "url": "https://dlmf.nist.gov/10.32.E9",
        "role": "positive-real K_nu integral, orders0..1/2",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://dlmf.nist.gov/10.39.E2",
        "role": "exact positive-real K_1/2",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://dlmf.nist.gov/5.11",
        "role": "digamma asymptotic5.11.2 and positive-real remainder",
        "remote_bytes_authenticated": False,
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def rational(value):
    require(type(value) in (int, Q), "strict rational type")
    value = Q(value)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= BITS,
        "rational bit cap",
    )
    return value


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


def tail_polynomial(m, work):
    m = integer(m, 0, MAX_DEGREE)
    work = checked_work(work)
    work.spend(2 * (m + 1))
    fact = math.factorial(m)
    return [fact // math.factorial(j) for j in range(m + 1)]


def evaluate(poly, value, work):
    require(
        type(poly) in (list, tuple) and 1 <= len(poly) <= MAX_DEGREE + 1,
        "polynomial cap",
    )
    value = rational(value)
    require(0 < value <= 32, "positive scalar control domain")
    coefficients = [rational(x) for x in poly]
    work = checked_work(work)
    work.spend(len(poly))
    answer = Q(0)
    for coefficient in reversed(coefficients):
        answer = rational(answer * value + coefficient)
    return answer


def tail_control(m, c, work=None):
    m = integer(m, 0, MAX_DEGREE - 1)
    c = rational(c)
    require(0 < c <= 32, "positive tail control domain")
    work = Budget() if work is None else checked_work(work)
    p = tail_polynomial(m, work)
    nxt = tail_polynomial(m + 1, work)
    require(nxt == [(m + 1) * v for v in p] + [1], "incomplete Gamma recurrence")
    left = [(m + 1) * v for v in p] + [0]
    for i, v in enumerate(p):
        left[i + 1] += v
    gap = [a - b for a, b in zip(left, nxt, strict=True)]
    require(gap == [0] + p[:-1] + [0], "positive gap polynomial identity")
    require(all(v >= 0 for v in gap), "nonnegative coefficient gap")
    denominator = evaluate(p, c, work)
    ratio = rational(evaluate(nxt, c, work) / (c * denominator))
    upper = rational(1 + Q(m + 1) / c)
    require(ratio <= upper, "exact tail ratio bound")
    return {
        "m": m,
        "rational_c_control": str(c),
        "P_m": p,
        "P_next": nxt,
        "gap_coefficients": gap,
        "tail_ratio_after_exp_cancellation": str(ratio),
        "upper_one_plus_m1_over_c": str(upper),
        "c_equals_actual_4pi_n": False,
        "transcendental_integral_evaluated": False,
    }


def cutoff_window(c):
    c = rational(c)
    require(12 < c < 24, "strict native scale separation interval")
    positive = rational(Q(1, 24) - 1 / (2 * c))
    negative = rational(Q(1, 48) - 1 / (2 * c))
    require(positive > 0 > negative, "first-q versus W leading margins")
    return {
        "epsilon_times_k": str(c),
        "q1_witness_leading_margin": str(positive),
        "all_W_upper_leading_margin": str(negative),
        "canonical_W_first_possible_frequency": 2,
        "q1_moment_pi_exponent": -1,
        "Lambda2_pi_exponent": 1,
        "pi_exponents_cancel": True,
        "finite_onset_certified": False,
    }


def modular_envelope(k, r):
    k = integer(k, 24, MAX_K)
    require(k % 12 == 0, "native weight12d")
    r = rational(r)
    require(0 <= r <= Q(1, k**6), "high-cusp radial power envelope")
    require(r <= Q(1, 100), "CZ radial envelope")
    u = rational(48 * r / (1 - r) + 240 * k * r)
    require(0 <= u <= Q(1, 2), "modular relative-error envelope")
    upper_error = rational(289 / Q(k**5))
    require(u <= upper_error, "explicit uniform k^-5 bound")
    lower, upper = rational(1 - u), rational(1 / (1 - u))
    require(upper - 1 <= 2 * u, "geometric exponential upper envelope")
    return {
        "weight": k,
        "radial_surrogate": str(r),
        "u": str(u),
        "h_over_q_squared_lower": str(lower),
        "h_over_q_squared_upper": str(upper),
        "u_bound_289_over_k5": str(upper_error),
        "abs_relative_error_upper": str(2 * u),
        "exponential_or_modular_value_sample": False,
    }


def source_module(sources, name):
    require(type(name) is str and name in ("family", "cusp"), "fixed constructor enum")
    stem = (
        "cusp_flag_quotient_global_family"
        if name == "family"
        else "cusp_period_off_central_real_zeros"
    )
    path = "research/l-families/atlas/generalized/" + stem + ".py"
    raw = sources[path]
    binding = next(row for row in BINDINGS if row["path"] == path)
    require(
        lf_sha(raw) == binding["sha256_lf"], "constructor identity before execution"
    )
    module = types.ModuleType("_authenticated_uncancelled_" + name)
    module.__file__ = str(ROOT / path)
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def native_controls(family, cusp, family_work, cusp_work):
    basis = []
    for d in (2, 3, 4):
        rows = family.miller_basis(d, 0, d + 2, "e4", family_work)
        other = family.miller_basis(d, 0, d + 2, "e6", family_work)
        require(rows == other, "two native Miller constructions")
        require(
            rows[0][1] == 1 and all(row[1] == 0 for row in rows[1:]),
            "literal first-q flag",
        )
        basis.append(
            {
                "dimension": d,
                "weight": 12 * d,
                "q_order": d + 2,
                "Miller_rows": [list(row) for row in rows],
                "W_rows": [list(row) for row in rows[1:]],
                "every_W_vector_has_no_q1_by_definition": True,
                "finite_prefix_used_to_prove_all_W_bound": False,
            }
        )
    prefixes = [
        cusp.native_prefix(d, j, 8, cusp_work)
        for d in (2, 3, 512, 1024)
        for j in (1, 2)
    ]
    return basis, prefixes


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    try:
        raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("invalid UTF-8") from exc
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lf_sha(raw):
    return hashlib.sha256(normalized(raw)).hexdigest()


def json_types(value, depth=0, counts=None):
    counts = [0, 0] if counts is None else counts
    counts[0] += 1
    require(counts[0] <= MAX_JSON_NODES, "total JSON node cap")
    require(depth <= 24, "JSON depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "JSON type")
    if type(value) is dict:
        require(len(value) <= 1024, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key")
            counts[1] += len(key.encode("utf-8"))
            require(counts[1] <= MAX_BYTES, "total JSON text byte cap")
            json_types(child, depth + 1, counts)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            json_types(child, depth + 1, counts)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
        counts[1] += len(value.encode("utf-8"))
        require(counts[1] <= MAX_BYTES, "total JSON text byte cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= BITS, "JSON integer cap")


def canonical(value):
    json_types(value)
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    require(len(result.encode()) <= MAX_BYTES, "canonical JSON byte cap")
    return result


def parse_json(raw):
    normalized(raw)

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    def nonfinite(value):
        raise ValueError("nonfinite JSON " + value)

    try:
        result = json.loads(raw, object_pairs_hook=pairs, parse_constant=nonfinite)
        json_types(result)
        return result
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def expected_manifest():
    return {
        "schema": "cusp-flag-uncancelled-real-zeros-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": [dict(row) for row in EXTERNAL],
        "primitive_contract": {
            "object": "actual CF canonical ell=[q] flag quotient; no generic flag replacement",
            "new_uniform_gate": "all W Parseval moment <=[1+(k-1)/(8pi)]G; no coefficient freedom",
            "completion": "CF/CZ half-lattice E*; Lambda2=pi/6 and residue1/2 unchanged",
            "moving_interval": "real s in [1-18/k,1), eventually k=12d",
            "witness": "h_d=Delta E4^(3d-3)=CF g1, not Miller f_d",
            "onset": "exists k0; no numerical onset or transfer of6144",
            "constructor": "only authenticated frozen family/CZ producer bytes executed",
        },
    }


def authenticated_sources(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    output = {}
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
        output[row["path"]] = raw
    return output


def artifact_hashes():
    result = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        raw = path.read_bytes()
        require(
            all(v >= 32 or v in (9, 10, 13) for v in raw), "artifact control character"
        )
        result[path.relative_to(ROOT).as_posix()] = lf_sha(raw)
    return result


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload, "unsealed payload"
    )
    raw = canonical(payload).encode()
    require(len(raw) <= MAX_BYTES, "payload byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(raw).hexdigest()}


def build_report():
    sources = authenticated_sources()
    family, cusp = source_module(sources, "family"), source_module(sources, "cusp")
    work, family_work, cusp_work = (
        Budget(),
        family.Budget(FAMILY_WORK),
        cusp.Budget(CUSP_WORK),
    )
    basis, prefixes = native_controls(family, cusp, family_work, cusp_work)
    tails = [
        tail_control(m, c, work)
        for m in range(MAX_DEGREE)
        for c in (Q(1, 3), Q(1), Q(7, 2), Q(32))
    ]
    window = cutoff_window(18)
    require(window["q1_witness_leading_margin"] == "1/72", "native positive reserve")
    require(
        window["all_W_upper_leading_margin"] == "-1/144", "native denominator reserve"
    )
    require(Q(200, 9801) < 1 and Q(4800, 99) < 49, "uniform Fourier/product constants")
    return seal(
        {
            "schema": "cusp-flag-uncancelled-off-central-real-zeros-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; pi and analytic functions symbolic",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "incomplete_Gamma_tail_controls": tails,
            "native_scale_window": window,
            "other_strict_scale_controls": [
                cutoff_window(c) for c in (Q(25, 2), Q(23), Q(47, 2))
            ],
            "native_small_Miller_flags": basis,
            "native_modular_prefixes": prefixes,
            "high_cusp_relative_envelopes": [
                modular_envelope(k, Q(1, k**6)) for k in (24, 96, 6144, 12288)
            ],
            "uniform_rational_constants": {
                "Fourier_remainder_at_radial_boundary": "200/9801",
                "Delta48_product_coefficient_at_radial_boundary": "1600/33",
                "Delta48_coefficient_upper": 49,
                "E4_weight_coefficient_upper": 240,
                "combined_k5_error_coefficient": 289,
            },
            "coverage": {
                "tail_polynomial_models": len(tails),
                "max_polynomial_degree": MAX_DEGREE,
                "native_small_flag_models": len(basis),
                "native_modular_prefixes": len(prefixes),
                "charged_work": work.used,
                "charged_family_work": family_work.used,
                "charged_cusp_work": cusp_work.used,
            },
            "caps": {
                "polynomial_degree": MAX_DEGREE,
                "control_weight": MAX_K,
                "q_order": 8,
                "work": MAX_WORK,
                "family_work": FAMILY_WORK,
                "cusp_work": CUSP_WORK,
                "bits": BITS,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_JSON_NODES,
            },
            "scope": {
                "actual_canonical_quotient_uncancelled_real_zero_pair": True,
                "whole_W_negativity_near1_by_written_uniform_proof": True,
                "interval": "s in [1-18/k,1); k=12d eventually",
                "first_coefficient_flag_replaced": False,
                "single_vector_outside_W_used_as_sufficient": False,
                "onset_type": "existential k0, not computed",
                "explicit_6144_onset_inherited": False,
                "corank_one_and_nonzero_ell_on_kernel_at_zero": True,
                "at_least_one_odd_order_reflected_pair": True,
                "simplicity_or_uniqueness_asserted": False,
                "period_Gamma_Bessel_eigenvalue_or_zero_samples": 0,
                "analytic_limits_or_integrals_machine_certified": False,
                "all_weights_or_all_minors_claim": False,
                "zeta_RH_counterexample": False,
                "new_automorphic_family_or_exhaustive_novelty": False,
                "parent_files_modified": False,
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
        result = expected_manifest()
    elif args.emit_report:
        result = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS_CUSP_FLAG_UNCANCELLED; eventual analytic theorem requires independent review"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
