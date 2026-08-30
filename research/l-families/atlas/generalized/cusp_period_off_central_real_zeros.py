"""Exact bounded controls, not analytic certification, for cusp-period real zeros."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import types
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
STEM = "cusp_period_off_central_real_zeros"
NOTE = HERE / "CUSP_PERIOD_OFF_CENTRAL_REAL_ZEROS.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "24bfc73fc9aa3ba115902340affa8727dfa18970"
MAX_D, MAX_Q, MAX_EXPONENT = 1024, 8, 3072
MAX_WORK, FAMILY_WORK, BITS, MAX_BYTES = 2000000, 100000, 4096, 2000000
MAX_JSON_NODES = 20000
PANELS = tuple((d, j) for d in (2, 3, 512, 513, 1024) for j in (1, 2))
BINDINGS = [
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "git_blob": "7e6ae5bb1fd9c53930cee1198eb185806a2ea118",
        "sha256_lf": "34120d58416c902db94fbeaf69ceb004694888908341b630a1b750f2f1e8316a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "git_blob": "7ca422e505e6ccd817aadee3362f1ace2fa83fd4",
        "sha256_lf": "fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "reviewed_family_release",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "reviewed_family_release",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "git_blob": "c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a",
        "sha256_lf": "84603f0412d8a7f1d2c2384c7055f55b4956db3df68b42dde7074d18cbe8265b",
    },
    {
        "commit": "a27781310ded92125ef16d97d78db4d97cec4c1b",
        "kind": "frozen_native_analytic_parent",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_DIVISOR_EXPLICIT_FORMULA.md",
        "git_blob": "1ec20ba529d34b833799d72515921fda7252da81",
        "sha256_lf": "c7123450f6201fc62af7b2c42a315a20c5e107d0348533b7348223fbbd24d373",
    },
    {
        "commit": "24bfc73fc9aa3ba115902340affa8727dfa18970",
        "kind": "frozen_authoring_context",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_SIGNED_RIEMANN_VON_MANGOLDT.md",
        "git_blob": "64c12988bda07d931fe4b9971f005ed5c238505f",
        "sha256_lf": "33fd982f0c08333bf6d21b0240e7ed47d79d5513625ee29f12d1a26f17bb3ff3",
    },
]
EXTERNAL = [
    {
        "url": "https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinRiemannZeta/eisenstein-zeta-978-3-662-00734-1_10.pdf",
        "role": "equations4-6 normalization; equation14 printed coefficient discrepancy",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p05-p.pdf",
        "role": "equations10.5-10.6 same completion and coefficient4; printed cosine variable corrected by CZ4",
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


def polynomial(row, order):
    order = integer(order, 1, MAX_Q)
    require(type(row) in (list, tuple) and len(row) == order + 1, "polynomial shape")
    converted = []
    for value in row:
        require(type(value) is int, "strict integer coefficient")
        rational(value)
        converted.append(value)
    return tuple(converted)


def qmul(left, right, order, work):
    left, right = polynomial(left, order), polynomial(right, order)
    work = checked_work(work)
    work.spend((order + 1) * (order + 2) // 2)
    out = [0] * (order + 1)
    for i, a in enumerate(left):
        for j in range(order + 1 - i):
            value = out[i + j] + a * right[j]
            rational(value)
            out[i + j] = value
    return tuple(out)


def qpower(row, exponent, order, work):
    row = polynomial(row, order)
    exponent = integer(exponent, 0, MAX_EXPONENT)
    work = checked_work(work)
    work.spend(2 * exponent.bit_length() + 1)
    out = (1,) + (0,) * order
    while exponent:
        if exponent % 2:
            out = qmul(out, row, order, work)
        exponent //= 2
        if exponent:
            row = qmul(row, row, order, work)
    return out


def primitives(order, work):
    order = integer(order, 4, MAX_Q)
    work = checked_work(work)
    work.spend(3 * (order + 1) ** 2)
    sigma1 = [0] + [
        sum(j for j in range(1, n + 1) if n % j == 0) for n in range(1, order + 1)
    ]
    e4 = (1,) + tuple(
        240 * sum(j**3 for j in range(1, n + 1) if n % j == 0)
        for n in range(1, order + 1)
    )
    product = [1]
    for n in range(1, order):
        numerator = -24 * sum(sigma1[j] * product[n - j] for j in range(1, n + 1))
        require(numerator % n == 0, "Delta recurrence integral division")
        product.append(numerator // n)
    return polynomial((0,) + tuple(product), order), polynomial(e4, order)


def native_prefix(d, j, order, work):
    d = integer(d, 2, MAX_D)
    j = integer(j, 1, d)
    order = integer(order, 4, MAX_Q)
    require(j <= order, "leading q power outside finite prefix")
    delta, e4 = primitives(order, work)
    row = qmul(
        qpower(delta, j, order, work), qpower(e4, 3 * (d - j), order, work), order, work
    )
    require(row[:j] == (0,) * j and row[j] == 1, "actual leading q coefficient")
    return {
        "dimension": d,
        "weight": 12 * d,
        "delta_power": j,
        "E4_power": 3 * (d - j),
        "q_order": order,
        "q_prefix": list(row),
        "first_coefficient": row[1],
        "is_in_W": j >= 2,
        "Miller_f_d_identification": j == d,
        "period_or_eigenvalue_evaluated": False,
    }


def taylor_lower(x, degree, work):
    x = integer(x, 0, 8)
    degree = integer(degree, 0, 12)
    work = checked_work(work)
    work.spend(2 * degree + 1)
    term, answer = Q(1), Q(1)
    for n in range(1, degree + 1):
        term = rational(term * x / n)
        answer = rational(answer + term)
    return answer


def envelope(r):
    r = rational(r)
    require(0 <= r <= Q(1, 100), "native radial envelope domain")
    cofactor = rational((1 + 11 * r + 11 * r**2 + r**3) / (1 - r) ** 5)
    return {
        "r": str(r),
        "E4_cofactor": str(cofactor),
        "E4_minus_one_bound": str(rational(240 * r * cofactor)),
        "Delta_over_q_lower": str(rational(1 - 24 * r / (1 - r))),
        "E_star_Fourier_tail_bound": str(rational(4 * r / (1 - r))),
    }


def threshold_row(k):
    k = integer(k, 3, 12 * MAX_D)
    difference = k * k - 2 * k - 1
    require(difference > 0, "integer monotonicity polynomial")
    return {
        "integer_k": k,
        "monotonicity_gap": difference,
        "successive_gap_difference": 2 * k - 1,
        "ratio_for_2_power_over_square": str(Q(2 * k * k, (k + 1) ** 2)),
        "analytic_period_sample": False,
    }


def poisson_control(n):
    n = integer(n, 1, 32)
    divisors = sum(n % j == 0 for j in range(1, n + 1))
    # Integer sign-pair ledger only; the Poisson/Mellin theorem is proved in prose.
    coefficient = Q(1, 2) * 2 * (2 * divisors) * 2
    require(coefficient == 4 * divisors, "half-lattice cosine normalization")
    require(divisors * divisors <= 4 * n, "bounded divisor-pair control")
    return {
        "n": n,
        "tau": divisors,
        "cosine_K0_coefficient_without_sqrt_y": int(coefficient),
    }


def constant_controls(work):
    work = checked_work(work)
    taylor = [
        (x, degree, taylor_lower(x, degree, work), bound)
        for x, degree, bound in ((5, 6, 100), (3, 4, 16), (4, 4, 32))
    ]
    require(
        all(value > bound for _, _, value, bound in taylor), "positive Taylor envelopes"
    )
    bound = envelope(Q(1, 100))
    require(
        Q(bound["E4_cofactor"]) < 2 and Q(bound["E4_minus_one_bound"]) < 3,
        "E4 uniform majorants",
    )
    require(Q(bound["Delta_over_q_lower"]) > Q(1, 2), "Delta lower reserve")
    require(Q(bound["E_star_Fourier_tail_bound"]) < 1, "Eisenstein tail reserve")
    require(Q(240 * 24, 16**4) < Q(1, 2), "Bernoulli reserve at k24")
    require(3**16 < 2**26 and 6144**2 < 2**26 and Q(25, 8) < 4, "threshold finite base")
    require(6144 > 2 + 26 + 26, "symbolic power2 exponent dominance")
    require(
        3072 == 48 * 64 and Q(100, 32) == Q(25, 8), "positive-mass threshold algebra"
    )
    return {
        "positive_Taylor_lower_sums": [
            {"x": x, "degree": degree, "sum": str(value), "exceeds": bound}
            for x, degree, value, bound in taylor
        ],
        "radial_boundary": bound,
        "Bernoulli_error_at_k24_upper": str(Q(240 * 24, 16**4)),
        "compact_E_star_absolute_bound": 43,
        "domain_area_upper": 2,
        "compact_mass_upper_coefficient": 100,
        "compact_mass_base": 64,
        "positive_slab_coefficient": "1/8",
        "positive_slab_native_measure_power": "k-2",
        "positive_mass_elementary_coefficient": 32,
        "positive_mass_elementary_base_divisor": 48,
        "threshold_base_divisor": 3072,
        "threshold_k": 6144,
        "threshold_d": 512,
        "power3_16": 3**16,
        "base_k_square": 6144**2,
        "comparison_power2_exponent": 26,
        "combined_required_power2_exponent": 54,
        "available_power2_exponent": 6144,
        "monotonicity_polynomial_coefficients_low_first": [-1, -2, 1],
        "successive_gap_polynomial_coefficients_low_first": [-1, 2],
        "all_integer_k_threshold_proved_in_note_not_enumerated": True,
    }


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
        "schema": "cusp-period-off-central-real-zeros-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": [dict(row) for row in EXTERNAL],
        "primitive_contract": {
            "object": "full CF period matrix, k=12d; actual h_d=Delta*E4^(3d-3)",
            "normalization": "half-lattice Mellin; central cosine coefficient4; CF completion unchanged",
            "measure": "y^k*dx*dy/y^2; full fundamental domain; no truncated replacement",
            "source_constructor": "only authenticated frozen family primitive bytes executed",
            "analytic_threshold": "all d>=512 by written bounds, not q-prefix sampling",
            "flag_boundary": "ord Q=ord full minus ord W; no noncancellation assertion",
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


def frozen_family(sources):
    path = "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py"
    raw = sources[path]
    binding = next(row for row in BINDINGS if row["path"] == path)
    require(
        lf_sha(raw) == binding["sha256_lf"], "constructor identity before execution"
    )
    module = types.ModuleType("_authenticated_cusp_real_zeros_family")
    module.__file__ = str(ROOT / path)
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def artifact_hashes():
    result = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        result[path.relative_to(ROOT).as_posix()] = lf_sha(path.read_bytes())
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
    family = frozen_family(sources)
    work, family_work = Budget(), family.Budget(FAMILY_WORK)
    delta, e4 = primitives(MAX_Q, work)
    frozen_delta, frozen_e4, _ = family.primitives(MAX_Q, family_work)
    require((delta, e4) == (frozen_delta, frozen_e4), "native Delta/E4 source equality")
    controls = constant_controls(work)
    panels = [native_prefix(d, j, MAX_Q, work) for d, j in PANELS]
    work.spend(32 * 33 // 2 + 32)
    return seal(
        {
            "schema": "cusp-period-off-central-real-zeros-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; analytic constants symbolic",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "native_primitives": {"Delta": list(delta), "E4": list(e4)},
            "native_prefixes": panels,
            "constant_controls": controls,
            "threshold_induction_controls": [
                threshold_row(k) for k in (3, 4, 24, 6144, 6145, 12288)
            ],
            "Poisson_sign_pair_controls": [poisson_control(n) for n in range(1, 33)],
            "coverage": {
                "native_prefixes": len(panels),
                "q_order": MAX_Q,
                "charged_work": work.used,
                "charged_frozen_primitive_work": family_work.used,
                "complete_high_weight_Miller_basis_constructed": False,
            },
            "caps": {
                "dimension": MAX_D,
                "q_order": MAX_Q,
                "exponent": MAX_EXPONENT,
                "work": MAX_WORK,
                "frozen_primitive_work": FAMILY_WORK,
                "bits": BITS,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_JSON_NODES,
            },
            "scope": {
                "actual_full_period_zero_by_written_proof": "k=12d, d>=512; one real zero in each (0,1/2),(1/2,1)",
                "h_d_is_CF_g1_not_Miller_f_d": True,
                "off_central_zeros_equal_order_by_reflection": True,
                "W_witness_threshold": "for each fixed j>=2, eventually in d; no common explicit onset",
                "analytic_continuation_inertia_integrals_machine_certified": False,
                "numeric_period_or_zero_samples": 0,
                "Q_uncancelled_zero_or_pole_asserted": False,
                "relative_inertia_gap_asserted": False,
                "W_negative_definite_at_center_assumed": False,
                "simplicity_uniqueness_or_optimal_onset": False,
                "zeta_RH_counterexample": False,
                "new_automorphic_family_or_exhaustive_novelty": False,
                "all_weights_all_minors_or_general_structures": False,
                "finite_controls_prove_analytic_limits": False,
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
            "PASS_CUSP_PERIOD_REAL_ZEROS; written analytic proof requires independent review"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
