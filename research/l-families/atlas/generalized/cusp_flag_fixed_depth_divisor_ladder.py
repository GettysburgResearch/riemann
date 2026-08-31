"""Exact source-bound controls for fixed-depth native cusp divisor clusters."""

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
STEM = "cusp_flag_fixed_depth_divisor_ladder"
NOTE = HERE / "CUSP_FLAG_FIXED_DEPTH_DIVISOR_LADDER.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "7ee5e024e1d8c3dd187b40ea5d48f9c9ff46d95e"
MAX_DEPTH, MAX_Q, MAX_K, MAX_WORK = 8, 12, 1048576, 6000000
BITS, INPUT_BITS, MAX_BYTES, MAX_NODES = 4096, 128, 2000000, 40000
RESIDUAL = {0: (0, 0), 4: (1, 0), 6: (0, 1), 8: (2, 0), 10: (1, 1), 14: (2, 1)}
BINDINGS = [
    {
        "commit": "2f636755ef8605eff725562094017f501fb1db70",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_NATIVE_DENOMINATOR_POLES.md",
        "kind": "accepted_native_second_scale",
        "git_blob": "993a830e2b9b3a7ff266de5bb770e1ffc5735315",
        "sha256_lf": "e4e8133243ef84259ea011e4cba60f48b615bb74c878b6897f786fde0bc0d0a6",
    },
    {
        "commit": "2f636755ef8605eff725562094017f501fb1db70",
        "path": "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.py",
        "kind": "accepted_native_second_scale",
        "git_blob": "bd065125ae110ce9d875998e79ded8a1268fc50f",
        "sha256_lf": "60c3f727f1e3da4e2a16abe26bfae1994208f3d797e7620a52c39296418a953e",
    },
    {
        "commit": "2f636755ef8605eff725562094017f501fb1db70",
        "path": "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.json",
        "kind": "accepted_native_second_scale",
        "git_blob": "e01e1126f63a463a3274b70401af8d3137460f8e",
        "sha256_lf": "a63794971ac6d940f80009a3687eb22b619b539407df2f9e36f60c40fee7b7b1",
    },
    {
        "commit": "2f636755ef8605eff725562094017f501fb1db70",
        "path": "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.sources.json",
        "kind": "accepted_native_second_scale",
        "git_blob": "9c863a41a744e7966765b6e61e71458c77f9d5ac",
        "sha256_lf": "cdb76a5afc3c81f087533466ba3ed08e42100ac73cf5a0427ba1a8f4d28b5f9b",
    },
    {
        "commit": "2f636755ef8605eff725562094017f501fb1db70",
        "path": "tests/test_cusp_flag_native_denominator_poles.py",
        "kind": "accepted_native_second_scale",
        "git_blob": "7efee0631a8099bcd1943bf459e4915062e20ee1",
        "sha256_lf": "200576bc492ba7dbb0ecb2420aa7c73faf25e36ae990c580793e4f4ee8864a6b",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_QUOTIENT_GLOBAL_FAMILY.md",
        "kind": "literal_modular_coefficient_flag",
        "git_blob": "77820c6af8d089d22547db6cda5ba025ed96f84f",
        "sha256_lf": "d5c95db34c62d31e0bb735e09aae5599e3abf29194cd74a50ce1bbebafab1530",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.py",
        "kind": "literal_modular_coefficient_flag",
        "git_blob": "7e6ae5bb1fd9c53930cee1198eb185806a2ea118",
        "sha256_lf": "34120d58416c902db94fbeaf69ceb004694888908341b630a1b750f2f1e8316a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json",
        "kind": "literal_modular_coefficient_flag",
        "git_blob": "7ca422e505e6ccd817aadee3362f1ace2fa83fd4",
        "sha256_lf": "fb6ae6ad8535b8cc519d33ab0e901cf17b9cf53ddff9c0bde427daf61faa60db",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.sources.json",
        "kind": "literal_modular_coefficient_flag",
        "git_blob": "90dc74d185b0b9a42f865a9f9df895ba7cd1c5dd",
        "sha256_lf": "f754ecdff30b4fd3a3f8f4b8436e46ab3633ba59738021f5538051fae9e43b7a",
    },
    {
        "commit": "b69c854d9e3dd1db7b82d95fe6f032fe47d5306b",
        "path": "tests/test_cusp_flag_quotient_global_family.py",
        "kind": "literal_modular_coefficient_flag",
        "git_blob": "c2d9dc7ea92a75c7e3fd99c5463e664fb79e0d3a",
        "sha256_lf": "84603f0412d8a7f1d2c2384c7055f55b4956db3df68b42dde7074d18cbe8265b",
    },
    {
        "commit": "0f716ed43f97ecd3fd3260b16548a17f239d619b",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_NATIVE_DENOMINATOR_POLES_AUDIT.md",
        "kind": "independent_NP_acceptance",
        "git_blob": "3e020cca66760ebdcc1708e2a9e401d7d81bd5d5",
        "sha256_lf": "3d6a3fc1b0493d8d0a42679a44bdd92bf2e6b2e51ee7722ee8efb918113c66d8",
    },
    {
        "commit": "1653565cc80cde6fa882ae9e150626187d3071d0",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_LOCAL_SIMPLE_ENDPOINT_ZERO.md",
        "kind": "complex_coercivity_and_normal_families",
        "git_blob": "0fa98ad20e040ea9b2e81c9906042ed56782bfaf",
        "sha256_lf": "a8a3e87b075f0d4c4f8834001c5b40b1b027bff23c5c32df88821116a0bcc13f",
    },
    {
        "commit": "98b4058ac29ba88cf993d7a3ce67579fab0c7844",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_ALL_WEIGHT_ENDPOINT_SEPARATION.md",
        "kind": "uniform_six_class_modular_bounds",
        "git_blob": "3e6a8d13959a69bf7f261747f65ea5e52f3d82ff",
        "sha256_lf": "920a7fcf1e63de46e902846b747bed2b7da5defbd34e9fec9b98a61866cb1d2d",
    },
    {
        "commit": "27496745df9dd49fcde17699d333a54cf8620772",
        "path": "research/l-families/atlas/generalized/CUSP_FLAG_EFFECTIVE_ENDPOINT_SEPARATION.md",
        "kind": "all_vector_moment_and_Gamma_shift",
        "git_blob": "c95b70b98052c9b608ab15cd7adae39edab55363",
        "sha256_lf": "55ed2486b59066ec825efcf2beabb47da9b685f7891c1824f794733001b73941",
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def coefficient(value):
    require(type(value) is int and abs(value).bit_length() <= BITS, "integer bit cap")
    return value


def rational(value, *, input_value=False):
    require(type(input_value) is bool, "strict input-cap selector")
    require(type(value) in (int, Q), "strict rational type")
    value = Q(value)
    cap = INPUT_BITS if input_value else BITS
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= cap,
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
    require(type(work) is Budget, "native Budget required")
    return work


def parameters(weight):
    weight = integer(weight, 24, MAX_K)
    require(weight % 2 == 0, "even weight")
    residual = 14 if weight % 12 == 2 else weight % 12
    a, b = RESIDUAL[residual]
    dimension = (weight - residual) // 12
    require(dimension >= 2, "CF source dimension at least2")
    return weight, dimension, residual, a, b


def polynomial(row, order):
    require(type(row) in (list, tuple) and len(row) == order + 1, "q polynomial shape")
    return [coefficient(x) for x in row]


def qmul(left, right, order, work):
    order = integer(order, 4, MAX_Q)
    work = checked_work(work)
    left, right = polynomial(left, order), polynomial(right, order)
    work.spend((order + 1) ** 2)
    result = [0] * (order + 1)
    for i, x in enumerate(left):
        for j in range(order + 1 - i):
            result[i + j] = coefficient(result[i + j] + coefficient(x * right[j]))
    return result


def qpower(row, exponent, order, work):
    order = integer(order, 4, MAX_Q)
    exponent = integer(exponent, 0, MAX_K)
    row, work = polynomial(row, order), checked_work(work)
    result = [1] + [0] * order
    while exponent:
        if exponent & 1:
            result = qmul(result, row, order, work)
        exponent //= 2
        if exponent:
            row = qmul(row, row, order, work)
    return result


def native_chart(weight, depth, order, work):
    weight, dimension, residual, a, b = parameters(weight)
    depth = integer(depth, 1, min(MAX_DEPTH, dimension))
    order = integer(order, max(4, depth + 1), MAX_Q)
    work = checked_work(work)
    work.spend(2 * (order + 1) ** 2)
    e4 = [1] + [
        240 * sum(t**3 for t in range(1, n + 1) if n % t == 0)
        for n in range(1, order + 1)
    ]
    e6 = [1] + [
        -504 * sum(t**5 for t in range(1, n + 1) if n % t == 0)
        for n in range(1, order + 1)
    ]
    raw = []
    tau = []
    for j in range(1, depth + 1):
        product = [1] + [0] * order
        for n in range(1, order + 1):
            work.spend(min(24 * j, order // n) + 1)
            factor = [0] * (order + 1)
            for t in range(min(24 * j, order // n) + 1):
                factor[t * n] = coefficient((-1) ** t * math.comb(24 * j, t))
            product = qmul(product, factor, order, work)
        product = qmul(
            product, qpower(e4, 3 * (dimension - j) + a, order, work), order, work
        )
        if b:
            product = qmul(product, e6, order, work)
        row = [0] * j + product[: order + 1 - j]
        target = 60 * weight - 744 * j - 864 * b
        require(row[j] == 1 and row[j + 1] == target, "native leading/tau identity")
        raw.append(row)
        tau.append(target)
    lifts = [None] * depth
    for idx in range(depth - 1, -1, -1):
        row = raw[idx][:]
        for higher in range(idx + 1, depth):
            work.spend(order + 1)
            scale = raw[idx][higher + 1]
            row = [
                coefficient(x - coefficient(scale * y))
                for x, y in zip(row, lifts[higher], strict=True)
            ]
        lifts[idx] = row
    require(
        all(lifts[i][j + 1] == int(i == j) for i in range(depth) for j in range(depth)),
        "complete native partial echelon identity",
    )
    return {
        "weight": weight,
        "dimension": dimension,
        "residual": residual,
        "a": a,
        "b": b,
        "depth": depth,
        "q_order": order,
        "g_prefixes": raw,
        "tau": tau,
        "h_prefixes": lifts,
        "deep_flag_exists": dimension >= depth + 1,
        "analytic_onset_asserted": False,
        "free_coefficient_model": False,
    }


def source_chart_controls(sources, work):
    cf = parse_json(
        sources[
            "research/l-families/atlas/generalized/cusp_flag_quotient_global_family.json"
        ]
    )
    np = parse_json(
        sources[
            "research/l-families/atlas/generalized/cusp_flag_native_denominator_poles.json"
        ]
    )
    cf_rows = []
    for dimension in (2, 3, 4, 5, 6):
        for residual in RESIDUAL:
            k = 12 * dimension + residual
            chart = native_chart(k, dimension, dimension + 2, work)
            digest = hashlib.sha256(canonical(chart["h_prefixes"]).encode()).hexdigest()
            old = next(x for x in cf["family"] if x["weight"] == k)
            require(
                digest == old["complete_basis_sha256_canonical_json"],
                "frozen complete CF basis",
            )
            cf_rows.append(
                {"weight": k, "dimension": dimension, "basis_sha256": digest}
            )
    np_rows = []
    for old in np["native_shear_pairs"]:
        chart = native_chart(old["weight"], 2, 8, work)
        require(
            chart["g_prefixes"] == [old["g1"]["q_prefix"], old["g2"]["q_prefix"]]
            and chart["h_prefixes"] == [old["h_prefix"], old["g2"]["q_prefix"]]
            and chart["tau"][0] == old["tau"],
            "complete frozen NP native chart",
        )
        np_rows.append(
            {
                "weight": old["weight"],
                "chart_sha256": hashlib.sha256(canonical(chart).encode()).hexdigest(),
            }
        )
    require(
        np["native_normalization_ledger"]["s_residue_coefficient"] == "1152",
        "literal NP residue source",
    )
    return {"complete_CF_bases": cf_rows, "complete_NP_charts": np_rows}


def projection_reserve(depth, lower, rho):
    depth = integer(depth, 1, MAX_DEPTH)
    lower = integer(lower, 1, depth)
    rho = rational(rho, input_value=True)
    require(0 <= rho <= Q(1, 100), "high-cusp radial domain")
    n, ell, x = depth + 1, depth + 1 - lower, rho * rho
    exact = rational(
        Q(ell * ell) / (1 - x) + 2 * ell * x / (1 - x) ** 2 + x * (1 + x) / (1 - x) ** 3
    )
    universal = rational(n * n * (1 + x) / (1 - x) ** 3)
    require(exact <= universal < 4 * n * n, "complete infinite projection-tail reserve")
    return {
        "depth": depth,
        "lower_q_order": lower,
        "target_first_order": n,
        "rho": str(rho),
        "sum_factor_exact": str(exact),
        "sum_factor_upper": str(universal),
        "squared_reserve": 4 * n * n,
        "dual_norm_coefficient": 2 * n,
        "x_projection_not_global_Petersson_commutation": True,
    }


def tail_ledger(depth, weight):
    depth = integer(depth, 1, MAX_DEPTH)
    weight, dimension, _, _, _ = parameters(weight)
    require(dimension >= depth + 1 and weight >= 48, "native deeper-chart envelope")
    radius = Q(1, 1000 * weight)
    exponent = rational((2 / (1 - radius) + 120 + Q(1008, weight)) / 1000)
    require(exponent < Q(1, 4), "full complex-q disc bound")
    h_bounds = [2 * 3 ** (depth - j) for j in range(1, depth + 1)]
    for idx, value in enumerate(h_bounds):
        require(
            value == 2 + 2 * sum(h_bounds[idx + 1 :]), "partial lift circle recurrence"
        )
    b = coefficient(4 * 3 ** (depth - 1) * 1000**depth)
    n = depth + 1
    eta = Q(1, 10000 * n)
    exponential_base = 16 * 4 * 3 * n * eta
    require(exponential_base == Q(12, 625) < Q(1, 10), "whole low-mass factorial base")
    return {
        "depth": depth,
        "weight": weight,
        "q_radius": str(radius),
        "circle_exponent_upper": str(exponent),
        "h_circle_bounds": h_bounds,
        "tail_B_J": b,
        "tail_k_degree": depth,
        "tail_first_order": n,
        "eta_J": str(eta),
        "low_factorial_base_upper": str(exponential_base),
        "low_polynomial_degree": 2 * depth,
        "dual_k_degree": depth + 2,
        "inverse_k_degree": -1,
        "deep_correction_k_degree": 2 * depth + 3,
        "deep_correction_ratio_base_to_AJ": str(Q(depth, depth + 1)),
        "quantifiers_fixed_depth": True,
        "high_cutoff_required": "Y>=1 and exp(-2pi Y)<=1/(2000k); eventual only",
        "high_cutoff_assumptions_checked_at_test_weight": False,
        "sufficient_weight_threshold_computed": False,
    }


def chamber_control(depth, delta, radius):
    depth = integer(depth, 1, MAX_DEPTH)
    delta = rational(delta, input_value=True)
    radius = rational(radius, input_value=True)
    require(0 < delta < radius < 12, "fixed disc0<delta<R<12")
    n = depth + 1
    numerator = 36 * n * n - (6 * (depth - 1) + radius) ** 2
    margin = rational(numerator / (24 * n * (12 * depth + radius) ** 2))
    circle = rational(delta / (24 * depth * (12 * depth + delta)))
    require(margin > 0 and circle > 0, "positive complex-domain reserves")
    return {
        "depth": depth,
        "center_c": 12 * depth,
        "deep_chamber_center": 6 * n,
        "deep_chamber_radius": 6 * n,
        "delta": str(delta),
        "R": str(radius),
        "coercivity_margin": str(margin),
        "Rouche_margin": str(circle),
        "larger_fixed_buffer_required": True,
    }


def chamber_point(depth, real, imag):
    depth = integer(depth, 1, MAX_DEPTH)
    real, imag = rational(real, input_value=True), rational(imag, input_value=True)
    require(abs(real) <= 128 and abs(imag) <= 128, "point coordinate cap")
    norm = real * real + imag * imag
    require(norm != 0, "c0 pole excluded")
    n = depth + 1
    gap = rational(real / (2 * norm) - Q(1, 24 * n))
    identity = rational(
        (36 * n * n - (real - 6 * n) ** 2 - imag * imag) / (24 * n * norm)
    )
    require(gap == identity, "native deeper chamber identity")
    return {
        "depth": depth,
        "c": [str(real), str(imag)],
        "gap": str(gap),
        "inside": gap > 0,
    }


def divisor_constants(depth, quotient):
    depth = integer(depth, 2, MAX_DEPTH)
    quotient = integer(quotient, 1, depth - 1)
    mode = depth - quotient
    sigma = sum((Q(1, d) for d in range(1, mode + 1) if mode % d == 0), Q(0))
    slope = Q(1, 288 * depth * depth)
    positive = Q(depth - quotient, 24 * quotient * depth)
    residue = rational(sigma * sigma / slope)
    gap = rational(residue / positive)
    require(positive > 0 and residue > 0 and gap > 0, "actual cluster signs")
    return {
        "depth": depth,
        "quotient": quotient,
        "cosine_mode": mode,
        "sigma_minus1": str(sigma),
        "scaled_zero_center": 12 * depth,
        "FJ_slope": str(slope),
        "earlier_Fi": str(positive),
        "right_residue_coefficient": str(residue),
        "c_gap_coefficient": str(gap),
        "residue_scale": "A_J/k^2",
        "c_gap_scale": "A_J/(k^2*A_i)",
        "s_gap_scale": "A_J/(k^3*A_i)",
        "s_zero_left_of_pole": True,
        "reflected_residue_sign": -1,
        "adjacent_quotient": quotient == depth - 1,
        "actual_values_numerically_sampled": False,
    }


def projection_obstruction(depth, lower):
    depth = integer(depth, 2, MAX_DEPTH)
    lower = integer(lower, 1, depth - 1)
    bad_base = Q(depth * depth, (lower + 1) * (depth + 1))
    good_base = Q(depth, depth + 1)
    return {
        "depth": depth,
        "lower": lower,
        "unprojected_squared_ratio_base": str(bad_base),
        "unprojected_exponential_decay": bad_base < 1,
        "projected_ratio_base": str(good_base),
        "fixed_polynomial_cannot_fix_base_gt1": True,
    }


def column_scaled_control(large, small, k, coupling):
    large, small = rational(large, input_value=True), rational(small, input_value=True)
    k, coupling = rational(k, input_value=True), rational(coupling, input_value=True)
    require(
        0 < small <= large <= 1 and k >= 2 and abs(coupling) <= 1,
        "finite scaled block domain",
    )
    determinant = rational(k * k - coupling * coupling * small / large)
    require(determinant > 0, "invertible column-scaled block")
    c = [[k, coupling], [coupling * small / large, k]]
    inverse = [
        [k / determinant, -coupling / determinant],
        [-coupling * small / large / determinant, k / determinant],
    ]
    product = [
        [sum(c[i][l] * inverse[l][j] for l in range(2)) for j in range(2)]
        for i in range(2)
    ]
    require(product == [[1, 0], [0, 1]], "exact column inverse identity")
    require(
        all(abs(value) <= 2 / k for row in inverse for value in row),
        "dimension2 inverse reserve",
    )
    return {
        "nonnative_linear_algebra_only": True,
        "A": [str(large), str(small)],
        "k_control": str(k),
        "coupling": str(coupling),
        "column_scaled_C": [[str(rational(x)) for x in row] for row in c],
        "inverse_C": [[str(rational(x)) for x in row] for row in inverse],
        "inverse_H_order": "diag(A)^-1 * inverse_C",
        "false_reverse_order_not_used": True,
    }


def endpoint_countercontrol(depth):
    depth = integer(depth, 2, MAX_DEPTH)
    weight, center = 12 * depth, 12 * depth
    require(Q(1) - Q(center, weight) == 0, "terminal-depth center is endpoint")
    return {
        "depth": depth,
        "dimension": depth,
        "weight": weight,
        "center_s": "0",
        "Q_d_endpoint_residue_over_Petersson_norm": "-1/2",
        "deep_flag_exists": False,
        "fixed_depth_eventual_theorem_applies_at_this_weight": False,
        "uniform_all_the_way_to_dimension_asserted": False,
    }


def normalized(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "UTF8 byte type/cap")
    try:
        raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("invalid UTF8") from exc
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def lf_sha(raw):
    return hashlib.sha256(normalized(raw)).hexdigest()


def json_types(value, depth=0, counts=None):
    counts = [0, 0] if counts is None else counts
    counts[0] += 1
    require(counts[0] <= MAX_NODES and depth <= 28, "JSON total node/depth cap")
    require(type(value) in (dict, list, str, int, bool, type(None)), "strict JSON type")
    if type(value) is dict:
        require(len(value) <= 1024, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key")
            counts[1] += len(key.encode("utf-8"))
            require(counts[1] <= MAX_BYTES, "JSON total text cap")
            json_types(child, depth + 1, counts)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            json_types(child, depth + 1, counts)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
        counts[1] += len(value.encode("utf-8"))
        require(counts[1] <= MAX_BYTES, "JSON total text cap")
    elif type(value) is int:
        coefficient(value)


def canonical(value):
    json_types(value)
    result = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)
    require(len(result.encode()) <= MAX_BYTES, "canonical JSON bytes")
    return result


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
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def expected_manifest():
    return {
        "schema": "cusp-flag-fixed-depth-divisor-ladder-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "primitive_contract": {
            "source": "actual level-one coefficient flags and completed Eisenstein period; original Petersson norm",
            "constructor": "CF Delta^j E4^(3(d-j)+a) E6^b with exact partial unit-echelon elimination",
            "projection": "literal x-Fourier projection against all W_(J+1), complete q/Fourier tails and low domain",
            "earlier_inverse": "column-scaled H_MM diag(A_m)^-1; no exponential Cauchy loss",
            "native_cross": "sigma_(-1)(J-i)*A_J after full deep and earlier elimination",
            "cluster": "fixed J then eventual all even k; distinct real simple numerator/denominator roots",
            "gap": "exact Schur mean-value identity resolves relative exponentially small gap",
            "source_execution": "none; new bounded constructors compare complete authenticated CF basis hashes and NP charts",
            "excluded": "no effective onset, growing-depth theorem, fixed-weight global census, RH or critical-line inference",
        },
        "primary_references": [
            "https://dlmf.nist.gov/10.32.E8",
            "https://dlmf.nist.gov/10.32.E9",
            "https://dlmf.nist.gov/10.39.E2",
        ],
        "remote_bytes_authenticated": False,
    }


def authenticated_sources(manifest=None):
    if manifest is None:
        require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
        manifest = parse_json(MANIFEST.read_bytes())
    require(
        canonical(manifest) == canonical(expected_manifest()), "complete typed manifest"
    )
    out = {}
    for row in BINDINGS:
        ref = row["commit"] + ":" + row["path"]
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", ref], cwd=ROOT, timeout=15
            )
        )
        require(0 <= size <= MAX_BYTES, "primitive byte cap before acquisition")
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        require(
            blob == row["git_blob"] and lf_sha(raw) == row["sha256_lf"],
            "literal source identity",
        )
        out[row["path"]] = raw
    return out


def artifact_hashes():
    out = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        raw = path.read_bytes()
        require(all(v >= 32 or v in (9, 10, 13) for v in raw), "artifact C0 control")
        out[path.relative_to(ROOT).as_posix()] = lf_sha(raw)
    return out


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload, "unsealed payload"
    )
    return {
        **payload,
        "payload_sha256": hashlib.sha256(canonical(payload).encode()).hexdigest(),
    }


def build_report():
    sources = authenticated_sources()
    work = Budget()
    source_controls = source_chart_controls(sources, work)
    charts = [
        native_chart(12 * d + r, j, 8, work)
        for d in (5, 16)
        for r in RESIDUAL
        for j in (3, 4)
    ]
    work.spend(8192)
    return seal(
        {
            "schema": "cusp-flag-fixed-depth-divisor-ladder-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers/Fraction; no analytic value sampling or floating determinant certification",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "source_chart_controls": source_controls,
            "native_depth3_depth4_charts": charts,
            "projection_controls": [
                projection_reserve(j, l, Q(1, 100))
                for j in range(1, 9)
                for l in range(1, j + 1)
            ],
            "tail_controls": [tail_ledger(j, 65536) for j in range(1, 9)],
            "disc_controls": [chamber_control(j, 3, 6) for j in range(1, 9)],
            "cluster_constants": [
                divisor_constants(j, i) for j in range(2, 9) for i in range(1, j)
            ],
            "unprojected_obstructions": [
                projection_obstruction(j, 1) for j in range(2, 9)
            ],
            "column_scaling_controls": [
                column_scaled_control(1, Q(1, 100), 10, 1),
                column_scaled_control(1, Q(1, 2**64), 100, Q(3, 4)),
            ],
            "terminal_depth_countercontrols": [
                endpoint_countercontrol(j) for j in (2, 3, 4, 8)
            ],
            "coverage": {
                "complete_CF_bases": len(source_controls["complete_CF_bases"]),
                "complete_NP_charts": len(source_controls["complete_NP_charts"]),
                "native_depth_charts": len(charts),
                "projection_rows": 36,
                "cluster_pairs": 28,
                "charged_work": work.used,
            },
            "caps": {
                "depth": MAX_DEPTH,
                "q_order": MAX_Q,
                "weight": MAX_K,
                "bits": BITS,
                "input_bits": INPUT_BITS,
                "work": MAX_WORK,
                "bytes": MAX_BYTES,
                "json_nodes": MAX_NODES,
            },
            "scope": {
                "actual_original_Q1_depth3_depth4_clusters": True,
                "every_fixed_depth_eventually_all_even_weights": True,
                "adjacent_and_original_quotients_distinguished": True,
                "complete_projected_functional_paid": True,
                "whole_deep_flag_inverse_paid": True,
                "earlier_column_scaling_paid": True,
                "relative_exponential_gap_via_exact_identity": True,
                "local_nested_flag_interlacing": True,
                "effective_threshold": False,
                "65536_onset_inherited": False,
                "uniform_growing_depth": False,
                "all_depths_up_to_dimension": False,
                "fixed_weight_infinite_poles": False,
                "global_interlacing": False,
                "unsigned_global_divisor_asymptotic": False,
                "RH_or_critical_line_claim": False,
                "new_automorphic_family": False,
                "analytic_values_sampled": 0,
                "analytic_proof_machine_certified": False,
                "parents_modified": False,
            },
        }
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
        value = expected_manifest()
    elif args.emit_report:
        value = build_report()
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        validate_report(parse_json(FIXTURE.read_bytes()))
        print(
            "PASS_FIXED_DEPTH_CUSP_DIVISOR_LADDER; independent analytic review required"
        )
        return
    print(json.dumps(value, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
