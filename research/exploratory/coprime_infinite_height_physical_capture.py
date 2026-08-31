"""Exact controls for coprime infinite-height corrected physical capture."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "coprime_infinite_height_physical_capture"
NOTE = HERE / "COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "36eddbbf065959f535ca4a7b08455d489ed4bd18"
DEGREE, INDEX, INPUT_BITS, BITS = 4, 8, 32, 4096
MAX_WORK, MAX_BYTES = 200000, 2000000
BINDINGS = [
    {
        "commit": "90e8dff3d184cbfe59974969ca89615856c33c51",
        "path": "research/exploratory/HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE.md",
        "kind": "corrected_physical_interface_and_sparse_denominator",
        "git_blob": "72ac1f93b6fb0a74200ed2cc7e8399a4a10064c2",
        "sha256_lf": "490373dafd09ed491a2c3ad31b44dc152cd0936c84f58e1676aef0ffd1013a0b",
    },
    {
        "commit": BASE,
        "path": "research/exploratory/HARDY_LOW_PASS_HEIGHT_EQUIVALENCE.md",
        "kind": "bare_low_pass_equivalence_and_scope_firewalls",
        "git_blob": "d44f3b58e7dbd9ec847d771b2299c6fabc21f5df",
        "sha256_lf": "ca94d882bc9ee69ae8e0a277ccc13ca7e7b86ab95a52d60eed16bb110f32bc72",
    },
]
EXTERNAL = {
    "url": "https://arxiv.org/html/2203.15372v1",
    "passages": "introduction; Section2.2 TheoremA; Section2.4 projection/model operators",
    "role": "classical kernel/Riesz/projection context; no imported HS theorem",
    "remote_bytes_authenticated": False,
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def rational(value, *, internal=False):
    require(type(internal) is bool, "internal flag type")
    require(type(value) in (int, Q), "strict rational type")
    value = Q(value)
    cap = BITS if internal else INPUT_BITS
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= cap,
        "rational bit cap",
    )
    return value


def gaussian(value, *, internal=False):
    require(type(internal) is bool, "internal flag type")
    if type(value) in (int, Q):
        return rational(value, internal=internal), Q(0)
    require(type(value) in (tuple, list) and len(value) == 2, "Gaussian pair type")
    return tuple(rational(v, internal=internal) for v in value)


def zadd(a, b):
    a, b = gaussian(a, internal=True), gaussian(b, internal=True)
    return gaussian((a[0] + b[0], a[1] + b[1]), internal=True)


def zneg(a):
    a = gaussian(a, internal=True)
    return -a[0], -a[1]


def zsub(a, b):
    return zadd(a, zneg(b))


def zmul(a, b):
    a, b = gaussian(a, internal=True), gaussian(b, internal=True)
    return gaussian(
        (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]), internal=True
    )


def zconj(a):
    a = gaussian(a, internal=True)
    return a[0], -a[1]


def norm2(a):
    a = gaussian(a, internal=True)
    return rational(a[0] ** 2 + a[1] ** 2, internal=True)


def zdiv(a, b):
    b = gaussian(b, internal=True)
    d = norm2(b)
    require(d != 0, "zero Gaussian denominator")
    c = zmul(a, zconj(b))
    return gaussian((c[0] / d, c[1] / d), internal=True)


def zsum(values):
    out = gaussian(0)
    for value in values:
        out = zadd(out, value)
    return out


def real(a):
    a = gaussian(a, internal=True)
    require(a[1] == 0, "expected real Gaussian")
    return a[0]


def encoded(a):
    return [str(v) for v in gaussian(a, internal=True)]


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, amount):
        amount = integer(amount, 0, MAX_WORK)
        require(self.used + amount <= self.limit, "work cap before expansion")
        self.used += amount


def budget(work):
    require(type(work) is Budget, "Budget type")
    return work


def matrix(a):
    require(type(a) in (list, tuple) and 1 <= len(a) <= DEGREE, "matrix rows cap")
    require(
        type(a[0]) in (list, tuple) and 1 <= len(a[0]) <= DEGREE, "matrix columns cap"
    )
    n = len(a[0])
    require(all(type(r) in (list, tuple) and len(r) == n for r in a), "matrix shape")
    return [[gaussian(v, internal=True) for v in row] for row in a]


def eye(n):
    n = integer(n, 1, DEGREE)
    return [[gaussian(int(i == j)) for j in range(n)] for i in range(n)]


def adjoint(a):
    a = matrix(a)
    return [[zconj(v) for v in row] for row in zip(*a, strict=True)]


def multiply(a, b, work):
    a, b, work = matrix(a), matrix(b), budget(work)
    require(len(a[0]) == len(b), "matrix multiplication dimension")
    work.spend(len(a) * len(b) * len(b[0]))
    return [
        [zsum(zmul(a[i][k], b[k][j]) for k in range(len(b))) for j in range(len(b[0]))]
        for i in range(len(a))
    ]


def subtract(a, b):
    a, b = matrix(a), matrix(b)
    require(len(a) == len(b) and len(a[0]) == len(b[0]), "matrix subtraction shape")
    return [
        [zsub(x, y) for x, y in zip(r, s, strict=True)]
        for r, s in zip(a, b, strict=True)
    ]


def inverse_det(a, work):
    a, work = matrix(a), budget(work)
    n = len(a)
    require(len(a[0]) == n, "square matrix")
    work.spend(n**3)
    a = [r + s for r, s in zip(a, eye(n), strict=True)]
    det = gaussian(1)
    for j in range(n):
        p = next((i for i in range(j, n) if norm2(a[i][j])), None)
        require(p is not None, "singular matrix")
        if p != j:
            a[j], a[p] = a[p], a[j]
            det = zneg(det)
        pivot = a[j][j]
        det = zmul(det, pivot)
        a[j] = [zdiv(v, pivot) for v in a[j]]
        for i in range(n):
            if i != j:
                factor = a[i][j]
                a[i] = [
                    zsub(x, zmul(factor, y)) for x, y in zip(a[i], a[j], strict=True)
                ]
    return [r[n:] for r in a], det


def trace(a):
    a = matrix(a)
    require(len(a) == len(a[0]), "square trace")
    return real(zsum(a[i][i] for i in range(len(a))))


def pack_matrix(a):
    return [[encoded(v) for v in r] for r in matrix(a)]


def nodes(value):
    require(
        type(value) in (tuple, list) and 1 <= len(value) <= DEGREE, "node count cap"
    )
    out = []
    for row in value:
        require(type(row) in (tuple, list) and len(row) == 2, "node shape")
        a, eta = (rational(v) for v in row)
        require(abs(a) <= 4096 and 0 < eta <= 2, "node domain")
        out.append((a, eta))
    require(len(set(out)) == len(out), "duplicate nodes")
    return out


def point(n, numerator=False):
    n = integer(n, 1, INDEX)
    require(type(numerator) is bool, "numerator flag type")
    return Q(16 * 2**n), Q(1) + (Q(1, 2**n) if numerator else Q(0))


def kernel_gram(left, right, work):
    left, right, work = nodes(left), nodes(right), budget(work)
    work.spend(len(left) * len(right))
    return [[zdiv(1, (y + eta, a - x)) for a, eta in right] for x, y in left]


def factor_at(z, u):
    z, u = nodes([z])[0], nodes([u])[0]
    phi = zdiv(zsub(z, u), zsub(z, zconj(u)))
    return zmul(zdiv(zconj(u), u), phi)


def product_at(z, roots, work):
    z, roots, work = nodes([z])[0], nodes(roots), budget(work)
    work.spend(len(roots))
    out = gaussian(1)
    for u in roots:
        out = zmul(out, factor_at(z, u))
    return out


def finite_control(n, m, work=None):
    n, m = integer(n, 1, DEGREE), integer(m, 1, DEGREE)
    work = Budget() if work is None else budget(work)
    bn, un = (
        [point(j) for j in range(1, n + 1)],
        [point(j, True) for j in range(1, m + 1)],
    )
    g, d, r = (
        kernel_gram(bn, bn, work),
        kernel_gram(un, un, work),
        kernel_gram(un, bn, work),
    )
    inv, det = inverse_det(g, work)
    dinv, _ = inverse_det(d, work)
    require(multiply(g, inv, work) == eye(n), "denominator inverse")
    require(multiply(d, dinv, work) == eye(m), "numerator inverse")
    values = [product_at(b, un, work) for b in bn]
    hv = [
        [zmul(zmul(values[i], zconj(values[j])), g[i][j]) for j in range(n)]
        for i in range(n)
    ]
    hs = subtract(g, multiply(adjoint(r), multiply(dinv, r, work), work))
    require(hv == hs and adjoint(hv) == hv, "physical value/Schur projection identity")
    capture = trace(multiply(inv, hv, work))
    require(0 < capture <= n, "finite physical range")
    cauchy = Q(1)
    for i in range(n):
        for j in range(i + 1, n):
            delta = bn[i][0] - bn[j][0]
            cauchy *= delta**2 / (delta**2 + 4)
    require(real(det) * 2**n == cauchy > 0, "Cauchy determinant")
    bound_sum = sum(Q(1, (2 ** (j + 1) + 1) ** 2) for j in range(1, n + 1))
    actual_sum = sum(norm2(v) for v in values)
    if n <= m:
        require(
            all(
                norm2(v) <= Q(1, (2 ** (j + 1) + 1) ** 2)
                for j, v in enumerate(values, 1)
            ),
            "matching factor domination",
        )
        require(
            capture <= Q(4, 3) * actual_sum <= Q(4, 3) * bound_sum < Q(1, 9),
            "capture bound",
        )
    return {
        "B_prefix": n,
        "U_finite_prefix": m,
        "B_nodes": [[str(a), str(y)] for a, y in bn],
        "U_nodes": [[str(a), str(y)] for a, y in un],
        "Gram_unnormalized": pack_matrix(g),
        "Gram_inverse": pack_matrix(inv),
        "U_Gram_unnormalized": pack_matrix(d),
        "cross_Gram_U_B": pack_matrix(r),
        "U_values_at_B_nodes": [encoded(v) for v in values],
        "physical_Gram_values": pack_matrix(hv),
        "physical_Gram_Schur": pack_matrix(hs),
        "physical_trace": str(capture),
        "normalized_B_Gram_determinant": str(cauchy),
        "actual_projection_kernel_mass": str(actual_sum),
        "all_matching_factors_present": n <= m,
        "matching_factor_mass_bound": str(bound_sum) if n <= m else None,
        "global_1_over_9_bound_applies_to_this_finite_control": n <= m,
        "infinite_U_evaluated": False,
    }


def geometric_control(n):
    n = integer(n, 1, INDEX)
    delta = Q(1, 2**n)
    left = sum(Q(1, 8 * (2**n - 2**j)) for j in range(1, n))
    left_majorant = Q(n - 1, 8 * 2 ** (n - 1))
    right_majorant = Q(1, 8 * 2 ** (n - 1))
    require(
        left <= left_majorant <= Q(1, 8) and right_majorant <= Q(1, 8), "row majorants"
    )
    match = (delta / (2 + delta)) ** 2
    require(match == Q(1, (2 ** (n + 1) + 1) ** 2) < Q(1, 4 ** (n + 1)), "match bound")
    tail = Q(1, 12 * 4**n)
    cross = Q(n, 48 * 4**n)
    projection = Q(4, 3) * cross
    residual = 2 * (tail + Q(1, 9) * projection)
    source_tail = Q(4, 3) * residual
    require(
        source_tail == Q(1, 4**n) * (Q(2, 9) + Q(2 * n, 243)),
        "orthogonal tail coefficient",
    )
    return {
        "index": n,
        "B_height_prefix": n,
        "U_height_prefix": str(n + 1 - delta),
        "paired_height_gap": str(delta),
        "paired_factor_mass": str(match),
        "left_reciprocal_sum": str(left),
        "left_row_majorant": str(left_majorant),
        "right_infinite_row_majorant": str(right_majorant),
        "global_Gram_lower": "3/4",
        "global_Gram_upper": "5/4",
        "kernel_mass_tail_bound": str(tail),
        "cross_Gram_squared_HS_bound": str(cross),
        "prefix_overlap_squared_operator_bound": str(projection),
        "residual_frame_squared_HS_bound": str(residual),
        "orthogonal_source_squared_HS_tail_bound": str(source_tail),
        "pure_B_height_tail_infinite": True,
        "fixed_infinite_U_in_analytic_tail_theorem": True,
    }


def prefix_control(n, k, m, work=None):
    n, k, m = integer(n, 1, DEGREE), integer(k, 1, DEGREE), integer(m, 1, DEGREE)
    require(n < k <= m, "nested matched prefixes")
    work = Budget() if work is None else budget(work)
    before, after = finite_control(n, m, work), finite_control(k, m, work)
    difference = Q(after["physical_trace"]) - Q(before["physical_trace"])
    bound = Q(geometric_control(n)["orthogonal_source_squared_HS_tail_bound"])
    require(0 <= difference <= bound, "orthogonal prefix tail finite control")
    return {
        "retained": n,
        "full_finite_B": k,
        "fixed_finite_U": m,
        "physical_prefix_trace": before["physical_trace"],
        "physical_full_trace": after["physical_trace"],
        "orthogonal_source_tail": str(difference),
        "analytic_tail_upper": str(bound),
        "naive_kernel_tail_is_not_identified_with_source_tail": True,
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
        require(abs(value).bit_length() <= BITS, "JSON integer cap")


def canonical(data):
    json_types(data)
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False)


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
        data = json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid)
        json_types(data)
        return data
    except (UnicodeError, RecursionError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def expected_manifest():
    return {
        "schema": "coprime-infinite-height-physical-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(r) for r in BINDINGS],
        "external_context": dict(EXTERNAL),
        "primitive_contract": {
            "Fourier": "(2pi)^(-1/2) integral_0^infinity h(t) exp(izt)dt; boundary dx",
            "projection": "P_U=P_(U H2)=M_U M_U*, NOT P_(K_U) or M_U",
            "construction": "b_n=16*2^n+i; u_n=16*2^n+i*(1+2^-n); n>=1; PURE",
            "source": "O=1; N_src=U; D_src=B; R_src=U-B; nonnative",
            "tail": "fixed infinite U; orthogonal divisor prefix; overlap correction retained",
        },
    }


def authenticate(manifest=None):
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
        digest = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw
        ).hexdigest()
        require(
            digest == row["git_blob"] and lf_sha(raw) == row["sha256_lf"],
            "primitive identity",
        )


def artifact_hashes():
    out = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        out[path.relative_to(ROOT).as_posix()] = lf_sha(path.read_bytes())
    return out


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload, "unsealed payload"
    )
    raw = canonical(payload).encode()
    require(len(raw) <= MAX_BYTES, "payload byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(raw).hexdigest()}


def build_report():
    authenticate()
    work = Budget()
    controls = [
        finite_control(n, m, work)
        for n, m in [(1, 1), (2, 2), (3, 3), (4, 4), (2, 4), (3, 4), (2, 1)]
    ]
    prefixes = [
        prefix_control(n, k, m, work)
        for n, k, m in [(1, 2, 2), (1, 3, 4), (2, 3, 3), (2, 4, 4), (3, 4, 4)]
    ]
    return seal(
        {
            "schema": "coprime-infinite-height-physical-capture-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "Gaussian Fraction pairs, exact integers, no rounding/transcendental samples",
            "frozen_sources": [dict(r) for r in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "two_route_finite_projection_controls": controls,
            "orthogonal_prefix_controls": prefixes,
            "geometric_and_overlap_controls": [
                geometric_control(n) for n in range(1, INDEX + 1)
            ],
            "analytic_constants": {
                "global_Gram_lower": "3/4",
                "global_Gram_upper": "5/4",
                "global_inverse_upper": "4/3",
                "global_kernel_projection_mass_strict_upper": "1/12",
                "global_physical_trace_strict_upper": "1/9",
                "orthogonal_tail_bound": "4^(-N)*(2/9+2*N/243), N>=1",
                "bare_band_mass_each_kernel": "integral_I 2*exp(-2t)dt >0 for positive-measure I",
                "singular_or_exponential_factors": 0,
            },
            "coverage": {
                "finite_models": len(controls),
                "projection_routes": 2,
                "prefix_controls": len(prefixes),
                "charged_work": work.used,
            },
            "caps": {
                "degree": DEGREE,
                "index": INDEX,
                "input_bits": INPUT_BITS,
                "internal_bits": BITS,
                "work": MAX_WORK,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "synthetic_nonnative_pair": True,
                "both_pure_meromorphic": True,
                "coprime_inner_divisors": True,
                "both_unweighted_heights_infinite": True,
                "denominator_already_reduced": True,
                "corrected_physical_global_trace_finite": True,
                "bare_every_positive_measure_band_trace_infinite": True,
                "fixed_U_orthogonal_prefix_rate": True,
                "rate_uniform_over_output_sets_only": True,
                "global_numerator_transmitted_trace_finite": False,
                "bounded_band_numerator_transmitted_verdict": False,
                "actual_Xi_physical_capture": False,
                "physical_T_uniformity": False,
                "RH_or_GRH_claim": False,
                "analytic_limits_machine_certified": False,
                "numerical_transcendental_samples": 0,
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
            "PASS_COPRIME_INFINITE_HEIGHT_PHYSICAL_CAPTURE; analytic proof not machine-certified"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
