"""Bounded exact six-class controls for the actual canonical cusp endpoint."""

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
STEM = "cusp_flag_all_weight_endpoint_separation"
NOTE = HERE / "CUSP_FLAG_ALL_WEIGHT_ENDPOINT_SEPARATION.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "27496745df9dd49fcde17699d333a54cf8620772"
K, MAX_K, MAX_Q, MAX_WORK, SOURCE_WORK = 65536, 1048576, 8, 2000000, 300000
BITS, RADIAL_BITS, MAX_BYTES, MAX_JSON_NODES = 4096, 128, 2000000, 20000
RESIDUAL = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}

BINDINGS = [
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_effective_endpoint_parent",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md",
        "git_blob": "c95b70b98052c9b608ab15cd7adae39edab55363",
        "sha256_lf": "55ed2486b59066ec825efcf2beabb47da9b685f7891c1824f794733001b73941",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_effective_endpoint_parent",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.py",
        "git_blob": "7e7bed2c227e58a7c27e69a8ae3bf70e9805393d",
        "sha256_lf": "21f898a0944c13cf25a973c290f27b4703363f7d626922ad391c56ec625e1ce5",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_effective_endpoint_parent",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.json",
        "git_blob": "fd2ec70a97d1aff5b2a878dae30ef02cb4982e94",
        "sha256_lf": "45bff65cecca10a128efa142e29b6281ce81d3490e9ebceec3bcf961ecbc8b2b",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_effective_endpoint_parent",
        "path": "research/l-families/atlas/generalized/cusp_flag_effective_endpoint_separation.sources.json",
        "git_blob": "0e6a9c3aabb80def9638192f6af7a40b39f027ff",
        "sha256_lf": "9049ba583f6f1e489726576bbc3e787e31b6291db3bb3bd68be6943cef7938fb",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "kind": "native_effective_endpoint_parent",
        "path": "tests/test_cusp_flag_effective_endpoint_separation.py",
        "git_blob": "5b411d018ad3b6f88757a01e1b7e12e5f7a1d173",
        "sha256_lf": "a76a841fabad63f85f4c3156cf1aad2ddaf91468ec9b479325e768c69b5c1904",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "all_weight_native_family",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "all_weight_native_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "git_blob": "7e6ae5bb1fd9c53930cee1198eb185806a2ea118",
        "sha256_lf": "34120d58416c902db94fbeaf69ceb004694888908341b630a1b750f2f1e8316a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "all_weight_native_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "git_blob": "7ca422e505e6ccd817aadee3362f1ace2fa83fd4",
        "sha256_lf": "fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "all_weight_native_family",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "kind": "all_weight_native_family",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "git_blob": "c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a",
        "sha256_lf": "84603f0412d8a7f1d2c2384c7055f55b4956db3df68b42dde7074d18cbe8265b",
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


def bigint(value):
    require(
        type(value) is int and abs(value).bit_length() <= BITS, "strict integer bit cap"
    )
    return value


def convolution(left, right, order, work):
    order = integer(order, 0, MAX_Q)
    for row in (left, right):
        require(
            type(row) in (list, tuple) and len(row) == order + 1, "polynomial shape cap"
        )
        for value in row:
            bigint(value)
    work = checked_work(work)
    work.spend((order + 1) ** 2)
    out = [0] * (order + 1)
    for i in range(order + 1):
        for j in range(order + 1 - i):
            out[i + j] = bigint(out[i + j] + left[i] * right[j])
    return out


def unit_power(row, exponent, order, work):
    order = integer(order, 0, MAX_Q)
    exponent = integer(exponent, 0, MAX_K)
    require(type(row) in (list, tuple) and len(row) == order + 1, "unit series shape")
    for value in row:
        bigint(value)
    require(row[0] == 1, "unit series constant")
    work = checked_work(work)
    work.spend(order + 1)
    tail = [0, *row[1:]]
    answer = [1] + [0] * order
    power = answer[:]
    for j in range(1, min(exponent, order) + 1):
        power = convolution(power, tail, order, work)
        work.spend(order + 1)
        coefficient = math.comb(exponent, j)
        answer = [
            bigint(a + coefficient * b) for a, b in zip(answer, power, strict=True)
        ]
    return answer


def parameters(k):
    k = integer(k, 24, MAX_K)
    require(k % 2 == 0, "native even weight")
    r = 14 if k % 12 == 2 else k % 12
    require(r in RESIDUAL, "six native classes")
    d = (k - r) // 12
    require(d >= 2 and 12 * d + r == k, "native dimension at least2")
    a, b = RESIDUAL[r]
    return k, d, r, a, b


def class_onsets():
    rows = []
    for r, (a, b) in RESIDUAL.items():
        d = (K - r + 11) // 12
        k = 12 * d + r
        require(k >= K > k - 12, "first class threshold")
        rows.append({"r": r, "a": a, "b": b, "first_weight": k, "dimension": d})
    require(
        sorted(row["first_weight"] for row in rows) == list(range(K, K + 12, 2)),
        "complete even onset panel",
    )
    return rows


def exponent_ledger(k):
    k, d, r, a, b = parameters(k)
    p = 3 * d - 3 + a
    low = 4 * p + 8 * b
    require(4 * a + 6 * b == r, "native residual multiplier")
    require(low == k - 12 + 2 * b <= k, "low absolute square exponent")
    require(2 * p == k // 2 - 6 - 3 * b <= k // 2, "high E4 square exponent")
    return {
        "weight": k,
        "dimension": d,
        "r": r,
        "a": a,
        "b": b,
        "E4_power": p,
        "E6_power": b,
        "low_power_of2": low,
        "high_E4_square_power": 2 * p,
        "r14_not_r2": r != 14 or k % 12 == 2,
    }


def power_sum_numerator(power):
    power = integer(power, 1, 5)
    row = [1]
    denominator = 1
    for _ in range(power):
        nxt = [0] * (len(row) + 1)
        for i, c in enumerate(row):
            nxt[i] += i * c
            nxt[i + 1] += (denominator - i) * c
        row = nxt
        denominator += 1
    return row, denominator


def radial(value):
    value = rational(value)
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length())
        <= RADIAL_BITS,
        "radial rational bit cap",
    )
    require(0 <= value <= Q(1, 100), "radial domain")
    return value


def s5_envelope(rho):
    rho = radial(rho)
    row, power = power_sum_numerator(5)
    require(row == [0, 1, 26, 66, 26, 1] and power == 6, "fifth power-sum identity")
    value = Q(0)
    for c in reversed(row[1:]):
        value = rational(value * rho + c)
    value = rational(value / (1 - rho) ** power)
    require(value <= Q(8, 5), "S5 whole radial interval bound")
    e6 = 504 * Q(5, 4) * Q(8, 5)
    require(e6 == 1008 and 1 + e6 * Q(1, 100) == Q(277, 25) < 16, "E6 bound")
    return {
        "rho": str(rho),
        "S5": str(value),
        "S5_upper": "8/5",
        "numerator": row,
        "denominator_power": power,
        "sigma5_over_n5_upper": "5/4",
        "E6_linear_error": 1008,
        "E6_absolute_upper": "277/25",
        "analytic_E6_or_zeta_value_evaluated": False,
    }


def modular_envelope(k, rho):
    k, d, r, a, b = parameters(k)
    require(k >= K, "effective high-cusp weight")
    rho = radial(rho)
    require(rho <= Q(1, k**6), "native high radial envelope")
    p = 3 * d - 3 + a
    actual = rational(48 * rho / (1 - rho) + 960 * p * rho + 2016 * b * rho)
    uniform = rational(48 * rho / (1 - rho) + 240 * k * rho + 2016 * rho)
    require(
        actual <= uniform <= 289 * k * rho <= Q(289, k**5) < Q(1, 1000),
        "uniform six-class squared envelope",
    )
    v = rational(24 * rho / (1 - rho) + 480 * p * rho + 1008 * b * rho)
    require(2 * v == actual and v <= Q(1, 2), "complex telescoping envelope")
    return {
        "weight": k,
        "r": r,
        "rho": str(rho),
        "actual_squared_u": str(actual),
        "uniform_squared_u": str(uniform),
        "u_bound": str(Q(289, k**5)),
        "squared_lower": str(1 - uniform),
        "squared_upper": str(rational(1 / (1 - uniform))),
        "complex_v": str(v),
        "complex_ratio_error_upper": str(2 * v),
        "modulus_only_argument": False,
        "modular_function_sample": False,
    }


def native_prefix(k, j, order, work):
    k, d, r, a, b = parameters(k)
    j = integer(j, 1, 2)
    order = integer(order, j + 1, MAX_Q)
    work = checked_work(work)
    work.spend(2 * (order + 1) ** 2)
    e4 = [1] + [
        240 * sum(divisor**3 for divisor in range(1, n + 1) if n % divisor == 0)
        for n in range(1, order + 1)
    ]
    e6 = [1] + [
        -504 * sum(divisor**5 for divisor in range(1, n + 1) if n % divisor == 0)
        for n in range(1, order + 1)
    ]
    delta = [1] + [0] * order
    for n in range(1, order + 1):
        work.spend(min(24 * j, order // n) + 1)
        factor = [0] * (order + 1)
        for i in range(min(24 * j, order // n) + 1):
            factor[i * n] = (-1) ** i * math.comb(24 * j, i)
        delta = convolution(delta, factor, order, work)
    p = 3 * (d - j) + a
    result = convolution(delta, unit_power(e4, p, order, work), order, work)
    if b:
        result = convolution(result, e6, order, work)
    result = [0] * j + result[: order + 1 - j]
    require(
        result[j] == 1 and all(x == 0 for x in result[:j]), "actual leading q power"
    )
    return {
        "weight": k,
        "dimension": d,
        "r": r,
        "a": a,
        "b": b,
        "delta_power": j,
        "E4_power": p,
        "E6_power": b,
        "q_order": order,
        "q_prefix": result,
        "is_in_W": j == 2,
        "numerical_period_or_special_function": False,
    }


def source_module(sources, name):
    require(
        type(name) is str and name in ("endpoint", "family"),
        "fixed source constructor enum",
    )
    stem = (
        "cusp_flag_effective_endpoint_separation"
        if name == "endpoint"
        else "cusp_flag_quotient_global_family"
    )
    path = "research/l-families/atlas/generalized/" + stem + ".py"
    raw = sources[path]
    binding = next(row for row in BINDINGS if row["path"] == path)
    require(lf_sha(raw) == binding["sha256_lf"], "source identity before execution")
    module = types.ModuleType("_authenticated_all_weight_" + name)
    module.__file__ = str(ROOT / path)
    exec(compile(raw, module.__file__, "exec"), module.__dict__)  # noqa: S102
    return module


def native_controls(family, work, source_work):
    delta, e4, e6 = family.primitives(8, source_work)
    small = []
    for d in (2, 3):
        for r, (a, b) in RESIDUAL.items():
            for j in (1, 2):
                row = native_prefix(12 * d + r, j, 8, work)
                dp = family.qpower(delta, j, 8, source_work)
                ep = family.qpower(e4, 3 * (d - j) + a, 8, source_work)
                ep = family.qmul(
                    ep, family.qpower(e6, b, 8, source_work), 8, source_work
                )
                expected = family.qmul(dp, ep, 8, source_work)
                require(
                    row["q_prefix"] == list(expected),
                    "authenticated CF primitive agreement",
                )
                small.append(row)
    large = [
        native_prefix(row["first_weight"], j, 8, work)
        for row in class_onsets()
        for j in (1, 2)
    ]
    return small, large


def endpoint_transfer(endpoint, k):
    parameters(k)
    old = endpoint.onset_certificate(k)
    fields = (
        "all_W_upper",
        "witness_lower",
        "M_over_A_lower",
        "M_over_A_upper",
        "Gamma_Jensen_product_lower",
        "epsilon_moment_upper",
    )
    return {
        "weight": k,
        "r": parameters(k)[2],
        "unchanged_EP_integer_bounds": {key: old[key] for key in fields},
        "native_class_decoded_here": True,
        "EP_multiple12_scope_blindly_inherited": False,
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
        "schema": "cusp-flag-all-weight-endpoint-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "primitive_contract": {
            "object": "actual six CF classes, ell=[q], native Petersson norm",
            "r14": "k mod12=2 uses r14 and d=(k-14)/12, not r2",
            "witness": "Delta E4^(3d-3+a) E6^b; not generally Miller f1",
            "new_modular_input": "E6 error1008rho and abs277/25; squared/complex product envelopes",
            "effective": "every even k>=65536, sufficient not optimal",
            "asymptotic": "same normalized12/288 and C12, uniform six classes, noneffective error onset",
            "source_execution": "only frozen authenticated endpoint/family code; capped finite functions",
            "excluded": "no uniqueness, simplicity, RH, optimality or new automorphic family",
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
    endpoint, family = (
        source_module(sources, "endpoint"),
        source_module(sources, "family"),
    )
    work, source_work = Budget(), family.Budget(SOURCE_WORK)
    small, large = native_controls(family, work, source_work)
    onsets = class_onsets()
    return seal(
        {
            "schema": "cusp-flag-all-weight-endpoint-separation-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; analytic values not sampled",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "six_class_onsets": onsets,
            "S5_radial_controls": [
                s5_envelope(rho) for rho in (Q(0), Q(1, 1000), Q(1, 200), Q(1, 100))
            ],
            "exponent_ledgers": [
                exponent_ledger(row["first_weight"]) for row in onsets
            ],
            "squared_and_complex_envelopes": [
                modular_envelope(row["first_weight"], Q(1, row["first_weight"] ** 6))
                for row in onsets
            ],
            "effective_transfers": [
                endpoint_transfer(endpoint, row["first_weight"]) for row in onsets
            ],
            "unchanged_Lambda_bounds": endpoint.lambda_constants(),
            "unchanged_location_ledger": endpoint.location_ledger(),
            "unchanged_decay_orders": [
                endpoint.decoupling_order(m) for m in (0, 1, 4, 8, 16, 32)
            ],
            "native_CF_small_prefixes": small,
            "native_first_effective_prefixes": large,
            "coverage": {
                "native_small_prefixes": len(small),
                "native_effective_prefixes": len(large),
                "residual_classes": len(onsets),
                "charged_work": work.used,
                "charged_source_work": source_work.used,
            },
            "caps": {
                "weight": MAX_K,
                "q_order": MAX_Q,
                "bits": BITS,
                "radial_bits": RADIAL_BITS,
                "work": MAX_WORK,
                "source_work": SOURCE_WORK,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_JSON_NODES,
            },
            "scope": {
                "every_even_weight_ge65536": True,
                "first_weight": K,
                "all_six_actual_CF_classes": True,
                "r14_not_r2": True,
                "native_W_not_free_or_basis_only": True,
                "same_effective_margins": True,
                "same_C12_no_residue_shift": True,
                "complex_not_modulus_only": True,
                "onset_optimal": False,
                "6144_certified": False,
                "effective_fine_asymptotic_onset": False,
                "uniqueness_or_simplicity": False,
                "endpoint_escape_excluded": False,
                "all_odd_or_small_weights": False,
                "RH_or_global_zero_claim": False,
                "analytic_values_sampled": 0,
                "analytic_limits_machine_certified": False,
                "new_automorphic_family_or_exhaustive_novelty": False,
                "parents_modified": False,
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
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--check", action="store_true")
    modes.add_argument("--emit-report", action="store_true")
    modes.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        result = expected_manifest()
    elif args.emit_report:
        result = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print("PASS_ALL_WEIGHT_CUSP_ENDPOINT; independent analytic review required")
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
