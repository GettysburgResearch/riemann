"""Bounded exact controls for the conditional actual-Xi component-height boundary."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "xi_companion_global_height_boundary"
NOTE = HERE / "XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "5b25f2dace65dd4d46e16d566f2dc7a34b98f41d"
SCHEMA = "xi-companion-global-height-boundary-v1"
SOURCE_SCHEMA = "xi-companion-global-height-boundary-sources-v1"
MAX_DEGREE = 8
MAX_ORDER = 6
MAX_TERMS = 64
MAX_WEIGHT = 7
INPUT_BITS = 16
INTERNAL_BITS = 1024
MAX_BYTES = 1048576
SOURCE_ROWS = [
    {
        "id": "kernel",
        "commit": "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "path": "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "kind": "scientific_source",
        "role": "XL1-XL4 actual full-line Xi normalization, positive even kernel and XL11 tail",
        "git_blob": "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "sha256_lf": "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    },
    {
        "id": "count",
        "commit": "76454e3db0ccce8f500297ea27668d6088b5091a",
        "path": "research/exploratory/XI_UNIFORM_COMPANION_COUNT_WIDTH.md",
        "kind": "scientific_source",
        "role": "UC2-UC6 actual companion definitions and order-one growth; finite geographic scope",
        "git_blob": "a97d25f556a2bd085a4749d1e96d883a0646e666",
        "sha256_lf": "adaef750b277b755494d57e17a3e913e8f44f1614806d8274495ac88912fb0bc",
    },
    {
        "id": "capture",
        "commit": "90e8dff3d184cbfe59974969ca89615856c33c51",
        "path": "research/exploratory/HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE.md",
        "kind": "scientific_source",
        "role": "HC1 global finite unweighted height and pure denominator hypothesis; HC10 unpaid source tail",
        "git_blob": "72ac1f93b6fb0a74200ed2cc7e8399a4a10064c2",
        "sha256_lf": "490373dafd09ed491a2c3ad31b44dc152cd0936c84f58e1676aef0ffd1013a0b",
    },
    {
        "id": "duality",
        "commit": "ef7bbb8dca978269f24e7ff9d97b6dceeed5b460",
        "path": "research/exploratory/HARDY_INNER_WIDTH_SOURCE_DUALITY.md",
        "kind": "scientific_source",
        "role": "IW corrected adjoint physical source retained; raw-value convention not imported",
        "git_blob": "955b92fe277bcdb3d6e260b5cc9dc02dd3f49144",
        "sha256_lf": "a946e53b956bc94b39687dffe59f0eb97d33948ace996a6d9f0797d71b20acd5",
    },
    {
        "id": "frozen_lambda",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "kind": "literal_source_definition",
        "role": "L-106620.1 and .4-.6 constant positive lambda and exact C/R companion allocation",
        "git_blob": "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "sha256_lf": "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    },
    {
        "id": "native",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/theorems/T-106620-mesoscopic-riemann-siegel-gauge-ninety-percent-frontier.md",
        "kind": "historical_context",
        "role": "native U5 quotient with reduced inner factors; common-zero and cofinal ledger remains unpaid",
        "git_blob": "8db4fc42c3ea964c592224b64d0ad92b6c264018",
        "sha256_lf": "f926698271d06b2db02bd1d7e00a05034934d8b77a75496e137d127c565795b0",
    },
    {
        "id": "height",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106621-constant-scale-companion-height-budget.md",
        "kind": "historical_context",
        "role": "finite-window companion height context only; not an imported entire global-height bound",
        "git_blob": "fafa4b390bc140c8bb514dba83d41a5643cb77f1",
        "sha256_lf": "e41462ea71fd1f46849f75f7ff5dd6189514743e27bd3292bd1aec9292ec9065",
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    require(type(value) is int and low <= value <= high, "strict integer/domain cap")
    return value


def rational(value, *, internal=False):
    require(type(internal) is bool, "internal flag must be bool")
    require(type(value) in (int, Fraction), "strict exact rational required")
    value = Fraction(value)
    bits = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= bits,
        "rational bit cap",
    )
    return value


def _q(a=0, b=0):
    return rational(a, internal=True), rational(b, internal=True)


def _valid_q(value):
    require(type(value) is tuple and len(value) == 2, "Gaussian pair required")
    return _q(*value)


def _add(a, b):
    a, b = _valid_q(a), _valid_q(b)
    return _q(a[0] + b[0], a[1] + b[1])


def _mul(a, b):
    a, b = _valid_q(a), _valid_q(b)
    return _q(a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _div(a, b):
    a, b = _valid_q(a), _valid_q(b)
    norm = b[0] ** 2 + b[1] ** 2
    require(norm != 0, "zero Gaussian denominator")
    c = _mul(a, _q(b[0], -b[1]))
    return _q(c[0] / norm, c[1] / norm)


def _norm(a):
    a = _valid_q(a)
    return rational(a[0] ** 2 + a[1] ** 2, internal=True)


def _encoded(a):
    return [str(v) for v in _valid_q(a)]


def _phase(k):
    k = integer(k, 0, MAX_ORDER + 1)
    value = _q(1)
    for _ in range(k):
        value = _mul(value, _q(0, -1))
    return value


def axis_control(k, h=3, next_h=5, scale=Fraction(2, 3)):
    k = integer(k, 0, MAX_ORDER)
    h, next_h, scale = map(rational, (h, next_h, scale))
    require(h > 0 and next_h > 0 and scale >= 0, "positive moments/nonnegative scale")
    f = _mul(_phase(k), _q(h))
    df = _mul(_phase(k + 1), _q(next_h))
    numerator = _add(f, _mul(_q(0, -scale), df))
    denominator = _add(f, _mul(_q(0, scale), df))
    ratio = _div(numerator, denominator)
    expected = _q((h - scale * next_h) / (h + scale * next_h))
    require(ratio == expected, "imaginary-axis companion sign identity")
    return {
        "order": k,
        "phase": _encoded(_phase(k)),
        "next_phase": _encoded(_phase(k + 1)),
        "h": str(h),
        "next_h": str(next_h),
        "lambda": str(scale),
        "numerator": _encoded(numerator),
        "denominator": _encoded(denominator),
        "ratio": _encoded(ratio),
    }


def _roots(roots):
    require(type(roots) is tuple and 1 <= len(roots) <= MAX_DEGREE, "root tuple cap")
    answer, seen, degree = [], set(), 0
    for row in roots:
        require(type(row) is tuple and len(row) == 2, "root row shape")
        r, m = rational(row[0]), integer(row[1], 1, MAX_DEGREE)
        require(r not in seen, "duplicate real root")
        seen.add(r)
        degree += m
        require(degree <= MAX_DEGREE, "total root multiplicity cap")
        answer.append((r, m))
    return tuple(answer)


def cayley_control(roots, x, y, scale):
    roots = _roots(roots)
    x, y, scale = map(rational, (x, y, scale))
    require(y > 0 and scale > 0, "upper-half-plane point/positive lambda")
    log_derivative = _q()
    for r, m in roots:
        log_derivative = _add(log_derivative, _div(_q(m), _q(x - r, y)))
    numerator = _add(_q(1), _mul(_q(0, -scale), log_derivative))
    denominator = _add(_q(1), _mul(_q(0, scale), log_derivative))
    deficit = _norm(denominator) - _norm(numerator)
    require(log_derivative[1] < 0, "real-root logarithmic derivative sign")
    require(deficit == -4 * scale * log_derivative[1] > 0, "strict Cayley deficit")
    return {
        "roots": [[str(r), m] for r, m in roots],
        "point": [str(x), str(y)],
        "lambda": str(scale),
        "log_derivative": _encoded(log_derivative),
        "denominator_minus_numerator_norm_squared": str(deficit),
        "theta": _encoded(_div(numerator, denominator)),
    }


def removable_control(roots, root):
    roots = _roots(roots)
    root = rational(root)
    matching = [m for r, m in roots if r == root]
    require(len(matching) == 1, "selected root is not present")
    coefficients = [Fraction(1)]
    for r, m in roots:
        for _ in range(m):
            out = [Fraction()] * (len(coefficients) + 1)
            for j, value in enumerate(coefficients):
                out[j] -= r * value
                out[j + 1] += value
            coefficients = [rational(v, internal=True) for v in out]
    degree = len(coefficients) - 1
    taylor = [
        sum(
            (
                coefficients[k] * math.comb(k, j) * root ** (k - j)
                for k in range(j, degree + 1)
            ),
            Fraction(),
        )
        for j in range(degree + 1)
    ]
    plus, minus = [], []
    for j in range(degree + 1):
        derivative = (j + 1) * taylor[j + 1] if j < degree else Fraction()
        plus.append(_q(taylor[j], derivative))
        minus.append(_q(taylor[j], -derivative))
    order_plus = next(j for j, c in enumerate(plus) if c != _q())
    order_minus = next(j for j, c in enumerate(minus) if c != _q())
    require(order_plus == order_minus == matching[0] - 1, "exact removable order")
    ratio = _div(minus[order_minus], plus[order_plus])
    require(ratio == _q(-1), "multiple-root removable value")
    return {
        "roots": [[str(r), m] for r, m in roots],
        "selected_root": str(root),
        "polynomial": [str(c) for c in coefficients],
        "common_order": order_plus,
        "removed_ratio": _encoded(ratio),
        "lambda_for_this_finite_control": "1",
    }


def _poly_valid(poly):
    require(type(poly) is dict and len(poly) <= MAX_TERMS, "sparse polynomial cap")
    for powers, coefficient in poly.items():
        require(type(powers) is tuple and len(powers) == MAX_ORDER, "monomial shape")
        for exponent in powers:
            integer(exponent, 0, MAX_WEIGHT)
        require(
            sum((j + 1) * e for j, e in enumerate(powers)) <= MAX_WEIGHT, "weight cap"
        )
        integer(coefficient, -(2**INTERNAL_BITS - 1), 2**INTERNAL_BITS - 1)
        require(coefficient != 0, "zero sparse coefficient")
    return poly


def _poly_add(a, b):
    _poly_valid(a)
    _poly_valid(b)
    out = dict(a)
    for p, c in b.items():
        out[p] = out.get(p, 0) + c
        if out[p] == 0:
            del out[p]
    return _poly_valid(out)


def _times_variable(poly, j, coefficient=1):
    _poly_valid(poly)
    j = integer(j, 0, MAX_ORDER - 1)
    coefficient = integer(coefficient, -128, 128)
    out = {}
    for powers, value in poly.items():
        p = list(powers)
        p[j] += 1
        if coefficient:
            out[tuple(p)] = coefficient * value
    return _poly_valid(out)


def _differentiate(poly):
    _poly_valid(poly)
    out = {}
    for powers, coefficient in poly.items():
        for j, exponent in enumerate(powers):
            if exponent:
                require(j + 1 < MAX_ORDER, "derivative variable cap")
                p = list(powers)
                p[j] -= 1
                p[j + 1] += 1
                key = tuple(p)
                out[key] = out.get(key, 0) + coefficient * exponent
    return _poly_valid({p: c for p, c in out.items() if c})


def bell(order):
    order = integer(order, 0, MAX_ORDER)
    poly = {(0,) * MAX_ORDER: 1}
    for _ in range(order):
        poly = _poly_add(_times_variable(poly, 0), _differentiate(poly))
    return poly


def _poly_encoded(poly):
    _poly_valid(poly)
    return [{"powers": list(p), "coefficient": c} for p, c in sorted(poly.items())]


def bell_control():
    p5 = bell(5)
    residual = _poly_add(
        _times_variable(_differentiate(p5), 0),
        _times_variable(p5, 1, -5),
    )
    orders = []
    for powers, coefficient in sorted(residual.items()):
        inverse_y_power = sum(j * e for j, e in enumerate(powers))
        require(
            inverse_y_power >= 2 and powers[0] <= 4, "GH14 monomial asymptotic order"
        )
        orders.append(
            {
                "powers": list(powers),
                "coefficient": coefficient,
                "inverse_y_power": inverse_y_power,
                "D_power": powers[0],
            }
        )
    return {
        "bell_polynomials": [
            {"order": k, "terms": _poly_encoded(bell(k))} for k in range(7)
        ],
        "GH14_residual": orders,
        "residual_absolute_coefficient_sum": sum(abs(c) for c in residual.values()),
        "leading_constants_without_lambda": {
            "D_over_log_y": str(Fraction(1, 2)),
            "Dprime_times_y": str(Fraction(1, 2)),
            "D5_minus_D_times_y_log_y": str(5 * Fraction(1, 2) / Fraction(1, 2)),
            "component_attenuation_times_log_y": str(2 / Fraction(1, 2)),
            "ratio_times_y_log_y_cubed": str(2 * 5 / Fraction(1, 2) ** 2),
        },
    }


def nodes_checked(nodes, *, empty=False):
    require(type(empty) is bool, "empty flag must be bool")
    require(type(nodes) is tuple and len(nodes) <= MAX_DEGREE, "node tuple cap")
    require(empty or bool(nodes), "nonempty nodes required")
    answer, seen, degree = [], set(), 0
    for row in nodes:
        require(type(row) is tuple and len(row) == 3, "node shape")
        a, eta = rational(row[0]), rational(row[1])
        m = integer(row[2], 1, MAX_DEGREE)
        require(eta > 0 and (a, eta) not in seen, "positive height/unique nodes")
        seen.add((a, eta))
        degree += m
        require(degree <= MAX_DEGREE, "total node multiplicity cap")
        answer.append((a, eta, m))
    return tuple(answer)


def _nodes_encoded(nodes):
    return [[str(a), str(eta), m] for a, eta, m in nodes]


def _multiply_real(a, b):
    require(type(a) is list and type(b) is list, "dense rational lists required")
    require(1 <= len(a) <= 2 * MAX_DEGREE + 1, "left polynomial size cap")
    require(1 <= len(b) <= 2 * MAX_DEGREE + 1, "right polynomial size cap")
    a = [rational(x, internal=True) for x in a]
    b = [rational(x, internal=True) for x in b]
    require(len(a) + len(b) - 2 <= 2 * MAX_DEGREE, "finite product degree cap")
    out = [Fraction()] * (len(a) + len(b) - 1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            out[j + k] += x * y
    return [rational(x, internal=True) for x in out]


def blaschke_control(nodes, y):
    nodes = nodes_checked(nodes)
    y = rational(y)
    height = sum((eta * m for _, eta, m in nodes), Fraction())
    require(y >= 2 * height, "GH18 y >= twice total height required")
    numerator, denominator = [Fraction(1)], [Fraction(1)]
    norm_squared = Fraction(1)
    factors = []
    for a, eta, m in nodes:
        minus = a * a + (y - eta) ** 2
        plus = a * a + (y + eta) ** 2
        u = 4 * y * eta / minus
        require(plus / minus == 1 + u, "GH17 exact logarithm argument")
        domination = 2 * y * y * eta / minus
        require(0 < domination <= 8 * eta, "GH18 rational domination")
        for _ in range(m):
            numerator = _multiply_real(
                numerator, [Fraction(1), -2 * eta, a * a + eta * eta]
            )
            denominator = _multiply_real(
                denominator, [Fraction(1), 2 * eta, a * a + eta * eta]
            )
        norm_squared = rational(norm_squared * (minus / plus) ** m, internal=True)
        factors.append(
            {
                "node": [str(a), str(eta), m],
                "inverse_squared_modulus": str(1 + u),
                "y_log_upper_bound_per_copy": str(domination),
                "dominating_height_bound_per_copy": str(8 * eta),
            }
        )
    slope = numerator[1] - denominator[1]
    require(slope == -4 * height, "finite reciprocal-axis modulus slope")
    return {
        "nodes": _nodes_encoded(nodes),
        "y": str(y),
        "total_height": str(height),
        "factor_controls": factors,
        "product_squared_modulus": str(norm_squared),
        "reciprocal_axis_numerator": [str(v) for v in numerator],
        "reciprocal_axis_denominator": [str(v) for v in denominator],
        "squared_modulus_derivative_at_zero": str(slope),
        "finite_height_limit_from_slope": str(-slope / 2),
    }


def cancel_nodes(left, right):
    left, right = nodes_checked(left, empty=True), nodes_checked(right, empty=True)
    l = {(a, eta): m for a, eta, m in left}
    r = {(a, eta): m for a, eta, m in right}
    common = []
    for key in sorted(set(l) & set(r)):
        m = min(l[key], r[key])
        common.append((*key, m))
        l[key] -= m
        r[key] -= m
    return (
        tuple(common),
        tuple((*key, m) for key, m in sorted(l.items()) if m),
        tuple((*key, m) for key, m in sorted(r.items()) if m),
    )


def cancellation_control(prefix):
    prefix = integer(prefix, 0, 4)
    common = tuple((2**j, 1, 1) for j in range(prefix))
    left = common + ((0, 2, 1),)
    right = common + ((10, 1, 1), (11, 1, 1))
    canceled, reduced_l, reduced_r = cancel_nodes(left, right)
    require(
        canceled == nodes_checked(common, empty=True), "complete common-prefix removal"
    )
    sl = sum(eta * m for _, eta, m in reduced_l)
    sr = sum(eta * m for _, eta, m in reduced_r)
    require(sl == sr == 2, "equal finite reduced height bookkeeping")
    y = 2 * (prefix + 2)
    full_l, full_r = blaschke_control(left, y), blaschke_control(right, y)
    red_l, red_r = blaschke_control(reduced_l, y), blaschke_control(reduced_r, y)
    full_ratio = Fraction(full_r["product_squared_modulus"]) / Fraction(
        full_l["product_squared_modulus"]
    )
    red_ratio = Fraction(red_r["product_squared_modulus"]) / Fraction(
        red_l["product_squared_modulus"]
    )
    require(full_ratio == red_ratio, "exact quotient preservation under cancellation")
    return {
        "common_prefix": _nodes_encoded(canceled),
        "component_heights": [str(prefix + 2), str(prefix + 2)],
        "reduced_left": _nodes_encoded(reduced_l),
        "reduced_right": _nodes_encoded(reduced_r),
        "reduced_heights": [str(sl), str(sr)],
        "squared_modulus_ratio": str(full_ratio),
        "actual_Xi_example": False,
    }


def fourth_power_tail_control(n):
    n = integer(n, 1, MAX_DEGREE)
    partial = sum((Fraction(1, j**4) for j in range(1, n + 1)), Fraction())
    lower, upper = Fraction(1, 3 * (n + 1) ** 3), Fraction(1, 3 * n**3)
    require(0 < lower < upper, "integral-comparison tail endpoints")
    return {
        "n": n,
        "partial_height_at_c_one": str(partial),
        "tail_lower": str(lower),
        "tail_upper": str(upper),
        "transcendental_zero_placement_evaluated": False,
    }


def normalize(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "bounded bytes required")
    try:
        raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("UTF-8 required") from exc
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def digest(raw):
    return hashlib.sha256(normalize(raw)).hexdigest()


def _json_types(value, depth=0):
    require(depth <= 16, "JSON depth cap")
    require(
        type(value) in (dict, list, str, int, bool, type(None)),
        "exact JSON types required",
    )
    if type(value) is dict:
        require(len(value) <= 256, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 4096, "JSON key cap")
            _json_types(child, depth + 1)
    elif type(value) is list:
        require(len(value) <= 1024, "JSON list cap")
        for child in value:
            _json_types(child, depth + 1)
    elif type(value) is str:
        require(len(value) <= 4096, "JSON string cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= INTERNAL_BITS, "JSON integer cap")


def render(value):
    _json_types(value)
    return json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n"


def _unique(pairs):
    value = {}
    for key, child in pairs:
        require(key not in value, "duplicate JSON key")
        value[key] = child
    return value


def _nonfinite(value):
    raise ValueError("nonfinite JSON " + value)


def read_json(raw):
    normalize(raw)
    try:
        value = json.loads(raw, object_pairs_hook=_unique, parse_constant=_nonfinite)
        _json_types(value)
        return value
    except (RecursionError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("invalid bounded JSON") from exc


def exact_match(value, expected):
    require(render(value) == render(expected), "complete typed replay mismatch")


def manifest_expected():
    return {
        "schema": SOURCE_SCHEMA,
        "authoring_base": BASE,
        "sources": SOURCE_ROWS,
        "external_contracts": [
            {
                "url": "https://dlmf.nist.gov/25.4",
                "role": "xi definition and functional equation 25.4.3-4",
                "remote_bytes_authenticated": False,
            },
            {
                "url": "https://dlmf.nist.gov/5.11.E2",
                "role": "classical digamma asymptotic on the positive real axis",
                "remote_bytes_authenticated": False,
            },
            {
                "url": "https://dlmf.nist.gov/5.15.E9",
                "role": "classical differentiated polygamma bounds used through order five",
                "remote_bytes_authenticated": False,
            },
            {
                "url": "https://people.math.wisc.edu/~poltoratski/ToeplitzOrder.pdf",
                "role": "Section 2.1 page 4: meromorphic inner factorization and mass at infinity",
                "remote_bytes_authenticated": False,
            },
        ],
        "other_classical_imports": [
            "Hadamard factorization for entire functions of order at most one",
            "Rolle, locally uniform derivative convergence and Hurwitz",
        ],
    }


def authenticate_raw(row, raw):
    require(
        any(render(row) == render(r) for r in SOURCE_ROWS), "unknown typed primitive"
    )
    normalize(raw)
    blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(blob == row["git_blob"], "primitive Git blob mismatch")
    require(digest(raw) == row["sha256_lf"], "primitive LF SHA mismatch")


def source_locks():
    require(MANIFEST.stat().st_size <= MAX_BYTES, "manifest byte cap")
    exact_match(read_json(MANIFEST.read_bytes()), manifest_expected())
    for row in SOURCE_ROWS:
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", row["git_blob"]], cwd=ROOT, timeout=10
            )
        )
        require(0 <= size <= MAX_BYTES, "primitive byte cap")
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT, timeout=10
        )
        authenticate_raw(row, raw)
    artifacts = {}
    for path in (NOTE, Path(__file__).resolve(), MANIFEST, TEST):
        require(path.stat().st_size <= MAX_BYTES, "artifact byte cap")
        artifacts[path.relative_to(ROOT).as_posix()] = {
            "kind": "current_artifact",
            "sha256_lf": digest(path.read_bytes()),
        }
    return {"frozen_sources": SOURCE_ROWS, "current_artifacts": artifacts}


def seal(payload):
    require(
        type(payload) is dict and "payload_sha256" not in payload,
        "unsealed object required",
    )
    raw = render(payload).encode()
    require(len(raw) <= MAX_BYTES, "payload byte cap")
    return {**payload, "payload_sha256": hashlib.sha256(raw).hexdigest()}


def build_report():
    real_panels = (
        (((-1, 1), (1, 1)), 0, 1, Fraction(1, 2)),
        (((0, 3), (2, 2)), 1, Fraction(1, 3), Fraction(2, 3)),
        (((-3, 2), (1, 1), (4, 2)), Fraction(2, 3), 2, 1),
        (((0, 1),), 2, 3, 2),
    )
    finite_nodes = (
        ((0, 1, 1),),
        ((0, 1, 3),),
        ((-2, Fraction(1, 2), 2), (3, Fraction(1, 4), 1)),
        ((Fraction(1, 3), Fraction(2, 3), 1), (7, 2, 2)),
    )
    return seal(
        {
            "schema": SCHEMA,
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
            "rounding_contract": "exact integers and Fraction/Gaussian pairs; no rounding or transcendental evaluation",
            "sources": source_locks(),
            "axis_phases": [axis_control(k) for k in range(MAX_ORDER + 1)],
            "lambda_zero_exception": axis_control(5, scale=0),
            "real_root_cayley_controls": [
                cayley_control(*panel) for panel in real_panels
            ],
            "removable_real_zeros": [
                removable_control(((-2, 1), (0, 4), (3, 2)), r) for r in (-2, 0, 3)
            ],
            "bell_asymptotic_algebra": bell_control(),
            "finite_blaschke_height_controls": [
                blaschke_control(nodes, 3 * sum(eta * m for _, eta, m in nodes))
                for nodes in finite_nodes
            ],
            "common_divisor_controls": [cancellation_control(n) for n in (0, 1, 2, 4)],
            "nonnative_fourth_power_height_prefixes": [
                fourth_power_tail_control(n) for n in (1, 2, 4, 8)
            ],
            "caps": {
                "degree": MAX_DEGREE,
                "Bell_order": MAX_ORDER,
                "sparse_terms": MAX_TERMS,
                "sparse_weight": MAX_WEIGHT,
                "input_bits": INPUT_BITS,
                "internal_bits": INTERNAL_BITS,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "actual_Xi_normalization": True,
                "conditional_real_zero_or_explicit_inner_premise": True,
                "fixed_positive_lambda": True,
                "component_height_divergence": "k=0 and k=5 under the explicit premise; written analytic proof",
                "native_quotient_orientation": "Theta0/Theta5 before common-inner cancellation",
                "reduced_height_dichotomy": "both infinite, or both finite and equal; not decided",
                "corrected_adjoint_source_preserved": True,
                "actual_reduced_denominator_infinite_height_proved": False,
                "finite_band_trace_infinity_proved": False,
                "native_cofinal_capture_failure_proved": False,
                "uniform_lambda_limit_proved": False,
                "RH_proved": False,
                "analytic_limits_machine_verified": False,
                "nonnative_controls_are_actual_Xi": False,
            },
        }
    )


def check_fixture(value, expected):
    require(
        type(value) is dict and "payload_sha256" in value,
        "sealed fixture object required",
    )
    payload = {key: child for key, child in value.items() if key != "payload_sha256"}
    exact_match(value, seal(payload))
    exact_match(value, expected)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true")
    group.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(render(manifest_expected()), end="")
        return
    report = build_report()
    if args.check:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        check_fixture(read_json(FIXTURE.read_bytes()), report)
        print("PASS_XI_COMPANION_GLOBAL_HEIGHT_BOUNDARY")
    else:
        print(render(report), end="")


if __name__ == "__main__":
    main()
