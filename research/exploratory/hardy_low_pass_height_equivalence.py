"""Exact finite controls for bare low-pass / pure-Blaschke height equivalence."""

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
STEM = "hardy_low_pass_height_equivalence"
NOTE = HERE / "HARDY_LOW_PASS_HEIGHT_EQUIVALENCE.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d"
MAX_DEGREE, MAX_PREFIX, INPUT_BITS, BITS = 4, 8, 32, 4096
MAX_WORK, MAX_BYTES = 200000, 2000000
BINDINGS = [
    {
        "commit": "90e8dff3d184cbfe59974969ca89615856c33c51",
        "path": "research/exploratory/HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE.md",
        "kind": "finite_Gram_and_capture_parent",
        "git_blob": "72ac1f93b6fb0a74200ed2cc7e8399a4a10064c2",
        "sha256_lf": "490373dafd09ed491a2c3ad31b44dc152cd0936c84f58e1676aef0ffd1013a0b",
    },
    {
        "commit": BASE,
        "path": "research/exploratory/XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md",
        "kind": "conditional_actual_companion_height_parent",
        "git_blob": "e592a4c031876f56f07d28b7e18a8a7cf6e826f4",
        "sha256_lf": "5bf33ffd58c3fe277f4bfb0408f0805eae1b2f34aab49bb71e4c714afb80dc6d",
    },
]
EXTERNAL = [
    {
        "url": "https://arxiv.org/pdf/1605.07418v2",
        "role": "printed pages11-12: boundary dx Hardy model and reproducing kernel",
        "remote_bytes_authenticated": False,
    },
    {
        "url": "https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/",
        "role": "Lemma17 and disk automorphisms: Schwarz-Pick derivation in LP11",
        "remote_bytes_authenticated": False,
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, lo, hi):
    require(type(value) is int and lo <= value <= hi, "strict integer/domain cap")
    return value


def exact(value, *, internal=False):
    require(type(internal) is bool, "internal flag type")
    require(type(value) in (int, Q), "strict rational type")
    value = Q(value)
    cap = BITS if internal else INPUT_BITS
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= cap,
        "rational bit cap",
    )
    return value


def positive(value):
    value = exact(value)
    require(0 < value <= 32, "positive rational domain")
    return value


class Budget:
    def __init__(self, limit=MAX_WORK):
        self.limit = integer(limit, 1, MAX_WORK)
        self.used = 0

    def spend(self, amount):
        amount = integer(amount, 0, MAX_WORK)
        require(self.used + amount <= self.limit, "charged work before expansion")
        self.used += amount


def budget(value):
    require(type(value) is Budget, "Budget required")
    return value


def node_spec(nodes):
    require(type(nodes) in (list, tuple) and 1 <= len(nodes) <= MAX_DEGREE, "node cap")
    result = []
    for row in nodes:
        require(type(row) in (tuple, list) and len(row) == 2, "node shape")
        result.append((positive(row[0]), integer(row[1], 1, MAX_DEGREE)))
    require(len({eta for eta, _ in result}) == len(result), "duplicate height")
    require(sum(m for _, m in result) <= MAX_DEGREE, "total degree cap")
    return tuple(result)


def matrix(value, max_size=MAX_DEGREE):
    max_size = integer(max_size, 1, MAX_DEGREE)
    require(type(value) in (tuple, list) and 1 <= len(value) <= max_size, "matrix cap")
    n = len(value)
    require(
        all(type(row) in (tuple, list) and len(row) == n for row in value),
        "square matrix",
    )
    return [[exact(x, internal=True) for x in row] for row in value]


def identity(n):
    n = integer(n, 1, MAX_DEGREE)
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def multiply(a, b, work):
    a, b, work = matrix(a), matrix(b), budget(work)
    require(len(a) == len(b), "matrix dimension")
    n = len(a)
    work.spend(n**3)
    return [
        [
            exact(sum(a[i][k] * b[k][j] for k in range(n)), internal=True)
            for j in range(n)
        ]
        for i in range(n)
    ]


def transpose(a):
    a = matrix(a)
    return [list(row) for row in zip(*a, strict=True)]


def solve(a, rhs, work):
    a, work = matrix(a), budget(work)
    n = len(a)
    require(type(rhs) in (list, tuple) and len(rhs) == n, "rhs shape")
    rhs = [exact(x, internal=True) for x in rhs]
    work.spend(n**3)
    a = [row + [rhs[i]] for i, row in enumerate(a)]
    for j in range(n):
        p = next((i for i in range(j, n) if a[i][j]), None)
        require(p is not None, "singular matrix")
        a[j], a[p] = a[p], a[j]
        pivot = a[j][j]
        a[j] = [exact(v / pivot, internal=True) for v in a[j]]
        for i in range(n):
            if i != j:
                factor = a[i][j]
                a[i] = [
                    exact(x - factor * y, internal=True) for x, y in zip(a[i], a[j])
                ]
    return [row[-1] for row in a]


def inverse(a, work):
    a = matrix(a)
    cols = [solve(a, row, work) for row in identity(len(a))]
    return [list(row) for row in zip(*cols, strict=True)]


def gram_data(nodes, y, work):
    nodes, y, work = node_spec(nodes), positive(y), budget(work)
    modes = [(eta, r) for eta, m in nodes for r in range(m)]
    n = len(modes)
    work.spend(3 * n * n)
    grams = []
    for shift in (Q(0), y):
        grams.append(
            [
                [
                    exact(
                        Q(math.comb(r + s, r), 1)
                        / (eta + other + 2 * shift) ** (r + s + 1),
                        internal=True,
                    )
                    for other, s in modes
                ]
                for eta, r in modes
            ]
        )
    a = [[Q(0) for _ in modes] for _ in modes]
    c = [Q(int(r == 0)) for _, r in modes]
    for j, (eta, r) in enumerate(modes):
        a[j][j] = -eta
        if r:
            a[j - 1][j] = Q(1)
    return nodes, modes, grams[0], grams[1], a, c


def poly_mul(a, b, work):
    require(
        type(a) in (list, tuple)
        and type(b) in (list, tuple)
        and 1 <= len(a) <= MAX_DEGREE + 1
        and 1 <= len(b) <= MAX_DEGREE + 1,
        "polynomial shape",
    )
    require(len(a) + len(b) - 2 <= MAX_DEGREE, "polynomial degree cap")
    a = [exact(v, internal=True) for v in a]
    b = [exact(v, internal=True) for v in b]
    work = budget(work)
    work.spend(len(a) * len(b))
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = exact(out[i + j] + x * y, internal=True)
    return out


def product_polynomial(factors, work):
    require(type(factors) in (tuple, list) and len(factors) <= MAX_DEGREE, "factor cap")
    work = budget(work)
    out = [Q(1)]
    for c in factors:
        out = poly_mul(out, [exact(c, internal=True), Q(1)], work)
    return out


def partial_fraction_bridge(nodes, y, work):
    nodes, y, work = node_spec(nodes), positive(y), budget(work)
    n = sum(m for _, m in nodes)
    den_factors = [(eta + y) ** 2 for eta, m in nodes for _ in range(m)]
    num_factors = [(eta - y) ** 2 for eta, m in nodes for _ in range(m)]
    den = product_polynomial(den_factors, work)
    num = product_polynomial(num_factors, work)
    target = [exact(a - b, internal=True) for a, b in zip(den, num, strict=True)]
    require(target[-1] == 0, "proper defect")
    labels, polys = [], []
    for eta, m in nodes:
        for order in range(1, m + 1):
            factors = list(den_factors)
            for _ in range(order):
                factors.remove((eta + y) ** 2)
            p = product_polynomial(factors, work)
            polys.append(p + [Q(0)] * (n - len(p)))
            labels.append((eta + y, order))
    a = [[p[j] for p in polys] for j in range(n)]
    coefficients = solve(a, target[:-1], work)
    reconstructed = [
        sum(coefficients[i] * polys[i][j] for i in range(n)) for j in range(n)
    ]
    require(reconstructed == target[:-1], "partial fractions polynomial identity")
    total = Q(0)
    controls = []
    for (scale, order), coefficient in zip(labels, coefficients, strict=True):
        integral_over_pi = Q(
            math.comb(2 * order - 2, order - 1), 4 ** (order - 1)
        ) / scale ** (2 * order - 1)
        total = exact(total + coefficient * integral_over_pi / (4 * y), internal=True)
        controls.append(
            {
                "scale": str(scale),
                "order": order,
                "coefficient": str(coefficient),
                "basis_integral_over_pi": str(integral_over_pi),
            }
        )
    return total, controls


def finite_control(nodes, y, work=None):
    work = Budget() if work is None else budget(work)
    nodes, modes, g, gy, a, c = gram_data(nodes, y, work)
    inv = inverse(g, work)
    require(multiply(g, inv, work) == identity(len(g)), "Gram inverse")
    atg, ga = multiply(transpose(a), g, work), multiply(g, a, work)
    require(
        all(
            atg[i][j] + ga[i][j] == -c[i] * c[j]
            for i in range(len(g))
            for j in range(len(g))
        ),
        "Lyapunov",
    )
    v = [sum(inv[i][j] * c[j] for j in range(len(g))) for i in range(len(g))]
    derivative_a = multiply(a, inv, work)
    derivative_b = multiply(inv, transpose(a), work)
    require(
        all(
            derivative_a[i][j] + derivative_b[i][j] == -v[i] * v[j]
            for i in range(len(g))
            for j in range(len(g))
        ),
        "negative-square derivative coefficient",
    )
    origin = exact(sum(c[i] * v[i] for i in range(len(g))), internal=True)
    height = sum(eta * m for eta, m in nodes)
    require(origin == 2 * height, "origin height")
    shifted = multiply(inv, gy, work)
    gram_trace = exact(sum(shifted[i][i] for i in range(len(g))), internal=True)
    partial, terms = partial_fraction_bridge(nodes, y, work)
    require(gram_trace == partial > 0, "two-route weighted bridge")
    return {
        "nodes_eta_multiplicity": [[str(eta), m] for eta, m in nodes],
        "degree": len(modes),
        "y": str(Q(y)),
        "height": str(height),
        "Gram": [[str(x) for x in row] for row in g],
        "Gram_inverse": [[str(x) for x in row] for row in inv],
        "origin": str(origin),
        "Lyapunov_verified": True,
        "negative_square_derivative_verified": True,
        "shifted_Gram_trace": str(gram_trace),
        "horizontal_defect_integral_over_4pi_y": str(partial),
        "partial_fractions_in_x_squared": terms,
        "log_integral_over_2pi": str(sum(m * min(Q(y), eta) for eta, m in nodes)),
        "analytic_limit_evaluated": False,
    }


def factor_control(a, eta, x, y):
    a, x, eta, y = exact(a), exact(x), positive(eta), positive(y)
    require(abs(a) <= 32 and abs(x) <= 32, "horizontal domain")
    den = (x - a) ** 2 + (y + eta) ** 2
    modulus_squared = exact(((x - a) ** 2 + (y - eta) ** 2) / den, internal=True)
    defect = exact(4 * y * eta / den, internal=True)
    require(modulus_squared + defect == 1 and 0 <= defect <= 1, "factor modulus")
    return {
        "a": str(a),
        "eta": str(eta),
        "x": str(x),
        "y": str(y),
        "modulus_squared": str(modulus_squared),
        "defect": str(defect),
        "weighted_mass": str(eta / (eta + y)),
        "log_integral_over_2pi": str(min(eta, y)),
        "log_singularity_on_line": eta == y,
    }


def product_control(factors):
    require(
        type(factors) in (list, tuple) and 1 <= len(factors) <= 8, "factor prefix cap"
    )
    residual, telescoping = Q(1), Q(0)
    for row in factors:
        require(type(row) in (list, tuple) and len(row) == 4, "factor row")
        data = factor_control(*row)
        q = Q(data["defect"])
        telescoping += residual * q
        residual *= 1 - q
    require(residual + telescoping == 1, "nonnegative product telescoping")
    return {
        "modulus_squared": str(residual),
        "defect": str(telescoping),
        "factors": len(factors),
    }


def real_inequality_control(epsilon, y, L):
    epsilon, y, L = positive(epsilon), positive(y), positive(L)
    require(epsilon <= Q(1, 2), "epsilon domain")
    return {
        "epsilon": str(epsilon),
        "y": str(y),
        "L": str(L),
        "Lipschitz_constant": str(1 / y),
        "half_interval_width": str(epsilon * y / 2),
        "disjoint_interval_mass_lower": str(epsilon**2 * y / 2),
        "q_minus_half_negative_log_derivative": str(
            (1 - 2 * epsilon) / (2 * (1 - epsilon))
        ),
        "weighted_trace_bound_per_A": str(1 + 1 / (2 * y * L)),
        "exponentials_or_logs_evaluated": False,
    }


def delay_control(L, tau):
    L, tau = positive(L), exact(tau)
    require(0 <= tau <= 32, "delay domain")
    overlap = max(Q(0), L - tau)
    return {
        "L": str(L),
        "tau": str(tau),
        "remaining_input_low_pass_length": str(overlap),
        "T_and_C_identically_zero": tau >= L,
        "any_B_including_infinite_height": True,
    }


def lacunary_control(n):
    n = integer(n, 1, MAX_PREFIX)
    eta = [256**j for j in range(1, n + 1)]
    g = [
        [Q(2 * 16 ** (j + k), 256**j + 256**k) for k in range(1, n + 1)]
        for j in range(1, n + 1)
    ]
    row_sums = [sum(abs(g[i][j]) for j in range(n) if i != j) for i in range(n)]
    require(all(s < Q(4, 15) for s in row_sums), "lacunary Gram bound")
    return {
        "prefix": n,
        "heights": eta,
        "Gram": [[str(x) for x in row] for row in g],
        "off_diagonal_row_sums": [str(x) for x in row_sums],
        "global_off_diagonal_bound": "4/15",
        "global_Gram_lower": "11/15",
        "global_Gram_upper": "19/15",
        "global_inverse_upper": "15/11",
        "band_exponentials_evaluated": False,
        "finite_prefix_used_as_infinite_proof": False,
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
        "schema": "hardy-low-pass-height-sources-v1",
        "authoring_base": BASE,
        "frozen_sources": [dict(row) for row in BINDINGS],
        "external_context": [dict(row) for row in EXTERNAL],
        "primitive_contract": {
            "Fourier": "(2pi)^(-1/2) integral_0^infinity h(t) exp(izt) dt; boundary dx",
            "object": "BARE U=1 trace of Pi_[0,L] P_KB Pi_[0,L]; PURE Blaschke",
            "bridge": "integral exp(-2yt) k_B(t)dt = integral (1-|B(x+iy)|^2)dx/(4pi*y)",
            "height": "unweighted sum Im b with multiplicity; no boundary extension needed",
            "Xi_corollary": "only GH-premised UNREDUCED components at each fixed lambda>0",
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
    authenticated_sources()
    work = Budget()
    choices = [
        ([(1, 1)], 1),
        ([(Q(1, 3), 1)], 2),
        ([(1, 2)], 1),
        ([(Q(1, 2), 3)], Q(3, 2)),
        ([(1, 1), (2, 1)], Q(1, 2)),
        ([(Q(1, 2), 2), (3, 2)], 2),
        ([(1, 1), (2, 1), (3, 1), (4, 1)], 3),
    ]
    return seal(
        {
            "schema": "hardy-low-pass-height-equivalence-v1",
            "status": "PROPOSED_REQUIRING_INDEPENDENT_FROZEN_REVIEW",
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction; no rounding; no transcendental evaluation",
            "frozen_sources": [dict(row) for row in BINDINGS],
            "artifact_sha256_lf": artifact_hashes(),
            "finite_Gram_bridge_controls": [
                finite_control(nodes, y, work) for nodes, y in choices
            ],
            "one_factor_controls": [
                factor_control(*row)
                for row in [
                    (0, 1, 0, 1),
                    (2, Q(1, 3), -1, 2),
                    (-3, 2, 4, Q(1, 2)),
                    (1, 3, 1, 2),
                ]
            ],
            "product_controls": [
                product_control([(0, 1, 1, 2), (2, 3, 1, 2)]),
                product_control([(0, 1, 0, 1)] * 3),
            ],
            "real_inequality_controls": [
                real_inequality_control(*row)
                for row in [
                    (Q(1, 4), 1, 2),
                    (Q(1, 2), Q(3, 2), Q(1, 3)),
                    (Q(1, 8), 3, 4),
                ]
            ],
            "delay_controls": [
                delay_control(*row) for row in [(1, 0), (1, Q(1, 2)), (1, 1), (1, 2)]
            ],
            "shifted_band_lacunary_controls": [
                lacunary_control(n) for n in (1, 2, 4, 8)
            ],
            "coverage": {
                "confluent_Gram_models": 7,
                "weighted_bridge_routes": 2,
                "charged_work": work.used,
            },
            "caps": {
                "degree": MAX_DEGREE,
                "lacunary_prefix": MAX_PREFIX,
                "input_bits": INPUT_BITS,
                "internal_bits": BITS,
                "work": MAX_WORK,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "pure_Blaschke_required_for_equivalence": True,
                "meromorphic_real_boundary_extension_required": False,
                "bare_U_equals_one": True,
                "band": "[0,L], fixed L>0",
                "some_low_pass_finite_iff_every_low_pass_finite_iff_height_finite": True,
                "infinite_height_implies_every_shifted_band_infinite": False,
                "arbitrary_inner_numerator_lower_bound": False,
                "corrected_P_U_physical_capture": False,
                "native_reduced_denominator_determined": False,
                "Xi_unreduced_corollary_requires_GH_premise": True,
                "cofinal_physical_uniformity": False,
                "RH_or_critical_line_claim": False,
                "analytic_limits_machine_certified": False,
                "numerical_transcendental_samples": 0,
                "novelty_or_new_abstract_theory_claim": False,
            },
        }
    )


def validate_report(report):
    require(type(report) is dict and "payload_sha256" in report, "sealed report")
    payload = {key: value for key, value in report.items() if key != "payload_sha256"}
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
            "PASS_HARDY_LOW_PASS_HEIGHT_EQUIVALENCE; analytic proof is not machine-certified"
        )
        return
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
