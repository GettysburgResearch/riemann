"""Exact bounded algebra for finite-height cofinal Hardy source capture."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STEM = "hardy_cofinal_finite_height_source_capture"
NOTE = HERE / "HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE.md"
MANIFEST = HERE / (STEM + ".sources.json")
FIXTURE = HERE / (STEM + ".json")
TEST = ROOT / "tests" / ("test_" + STEM + ".py")
BASE = "5852e785a24a2d30a8ba6c742e3650a7f6438567"
SCHEMA = "hardy-cofinal-finite-height-source-capture-v1"
SOURCE_SCHEMA = "hardy-cofinal-finite-height-source-capture-sources-v1"
MAX_DEGREE = 4
MAX_POLY = 8
MAX_PANEL = 8
INPUT_BITS = 16
INTERNAL_BITS = 1024
MAX_BYTES = 524288
SOURCE_ROWS = [
    {
        "id": "translation",
        "commit": "a07e9c3ba093abb348b849e0356f6babdf591e84",
        "path": "research/exploratory/HARDY_TRANSLATION_PHYSICAL_BAND_BOUND.md",
        "kind": "scientific_source",
        "role": "HT1 and HT5-HT6 finite origin-height identity only; historical raw jets not imported",
        "git_blob": "95338634d08fb5bde4d56d10197833b44ec64788",
        "sha256_lf": "efa2a1535e30e12e0fa20b1fabf49762843b50c72d0c8f6e44a70bbaa2feba3c",
    },
    {
        "id": "inner",
        "commit": "ef7bbb8dca978269f24e7ff9d97b6dceeed5b460",
        "path": "research/exploratory/HARDY_INNER_WIDTH_SOURCE_DUALITY.md",
        "kind": "scientific_source",
        "role": "IW2-IW6 corrected adjoint source and physical projection",
        "git_blob": "955b92fe277bcdb3d6e260b5cc9dc02dd3f49144",
        "sha256_lf": "a946e53b956bc94b39687dffe59f0eb97d33948ace996a6d9f0797d71b20acd5",
    },
    {
        "id": "count",
        "commit": "76454e3db0ccce8f500297ea27668d6088b5091a",
        "path": "research/exploratory/XI_UNIFORM_COMPANION_COUNT_WIDTH.md",
        "kind": "scientific_source",
        "role": "actual Xi geographic count and explicitly unpaid cofinal capture",
        "git_blob": "a97d25f556a2bd085a4749d1e96d883a0646e666",
        "sha256_lf": "adaef750b277b755494d57e17a3e913e8f44f1614806d8274495ac88912fb0bc",
    },
    {
        "id": "height",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/lemmas/L-106621-constant-scale-companion-height-budget.md",
        "kind": "historical_context",
        "role": "finite-window height ledger is not an imported global-height theorem",
        "git_blob": "fafa4b390bc140c8bb514dba83d41a5643cb77f1",
        "sha256_lf": "e41462ea71fd1f46849f75f7ff5dd6189514743e27bd3292bd1aec9292ec9065",
    },
    {
        "id": "native",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/theorems/T-106620-mesoscopic-riemann-siegel-gauge-ninety-percent-frontier.md",
        "kind": "historical_context",
        "role": "native partition, boundary and cofinal-exhaustion terms",
        "git_blob": "8db4fc42c3ea964c592224b64d0ad92b6c264018",
        "sha256_lf": "f926698271d06b2db02bd1d7e00a05034934d8b77a75496e137d127c565795b0",
    },
    {
        "id": "pick",
        "commit": "81d52e569cc8bb566e54043fd692fd6157406aab",
        "path": "claims/theorems/T-106670-regularized-pick-free-energy-ninety-percent-equivalence.md",
        "kind": "historical_context",
        "role": "historical total source charge remains outside this band result",
        "git_blob": "9a61689c19b244f0176f753cef146b252256eab0",
        "sha256_lf": "b96ffe1ec8e5fc7d825e521c57c956066e25f0494e80aa4c13d4017ea98c8ae7",
    },
    {
        "id": "translation_review",
        "commit": "5852e785a24a2d30a8ba6c742e3650a7f6438567",
        "path": "research/exploratory/HARDY_TRANSLATION_PHYSICAL_BAND_BOUND_AUDIT.md",
        "kind": "review_context",
        "role": "frozen origin-height and translation review",
        "git_blob": "7cf4400eac9ade2dbd8eda1271ab8cce9db0819e",
        "sha256_lf": "1b9a9426143cbe540a683887f7e351611df0028ed51aca22d7bceaa27b95d5a0",
    },
    {
        "id": "inner_review",
        "commit": "5852e785a24a2d30a8ba6c742e3650a7f6438567",
        "path": "research/exploratory/HARDY_INNER_WIDTH_SOURCE_DUALITY_AUDIT.md",
        "kind": "review_context",
        "role": "frozen all-inner and adjoint-convention review",
        "git_blob": "4f823a855cb4bcf199985856dcec7e3774c0b3d4",
        "sha256_lf": "0ce623e47c0d2e01ffd276dd13c715f92e18730bfd285e4064a9d5aff6b04cc5",
    },
    {
        "id": "count_review",
        "commit": "5852e785a24a2d30a8ba6c742e3650a7f6438567",
        "path": "research/exploratory/XI_UNIFORM_COMPANION_COUNT_WIDTH_AUDIT.md",
        "kind": "review_context",
        "role": "frozen geographic versus cofinal review",
        "git_blob": "2c160b9723850098fe80dafc4ca8309b8f3e0c1c",
        "sha256_lf": "79b0def4835824e8e03bd629362f4e11226e5f9ea54a520c19ff02ac2103c7a7",
    },
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    require(type(value) is int and low <= value <= high, "strict integer/domain cap")
    return value


def fraction(value, *, internal=False):
    require(type(internal) is bool, "internal flag must be bool")
    require(type(value) in (int, Fraction), "strict rational required")
    result = Fraction(value)
    bits = INTERNAL_BITS if internal else INPUT_BITS
    require(
        max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= bits,
        "rational bit cap",
    )
    return result


def _q(real=0, imag=0):
    return (fraction(real, internal=True), fraction(imag, internal=True))


ZERO, ONE, IMAG = _q(), _q(1), _q(0, 1)


def _add(x, y):
    return _q(x[0] + y[0], x[1] + y[1])


def _neg(x):
    return _q(-x[0], -x[1])


def _sub(x, y):
    return _add(x, _neg(y))


def _mul(x, y):
    return _q(x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def _conj(x):
    return _q(x[0], -x[1])


def _div(x, y):
    norm = y[0] ** 2 + y[1] ** 2
    require(norm != 0, "zero Gaussian denominator")
    num = _mul(x, _conj(y))
    return _q(num[0] / norm, num[1] / norm)


def _power(x, n):
    n = integer(n, 0, 2 * MAX_DEGREE + 1)
    result = ONE
    for _ in range(n):
        result = _mul(result, x)
    return result


def _encoded(x):
    return [str(x[0]), str(x[1])]


def _matrix_encoded(matrix):
    return [[_encoded(x) for x in row] for row in matrix]


def _identity(n):
    n = integer(n, 0, MAX_DEGREE)
    return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def _matrix_shape(matrix, *, square=False, empty=False):
    require(type(square) is bool and type(empty) is bool, "matrix flags must be bool")
    require(type(matrix) is list and len(matrix) <= MAX_DEGREE, "matrix row cap")
    if not matrix:
        require(empty, "empty matrix")
        return 0, 0
    require(type(matrix[0]) is list, "matrix row type")
    width = len(matrix[0])
    require(1 <= width <= MAX_DEGREE, "matrix column cap")
    require(not square or width == len(matrix), "square matrix required")
    for row in matrix:
        require(type(row) is list and len(row) == width, "rectangular matrix required")
        for entry in row:
            require(type(entry) is tuple and len(entry) == 2, "Gaussian entry shape")
            fraction(entry[0], internal=True)
            fraction(entry[1], internal=True)
    return len(matrix), width


def _adjoint(matrix):
    _matrix_shape(matrix)
    return [
        [_conj(matrix[j][i]) for j in range(len(matrix))] for i in range(len(matrix[0]))
    ]


def _mm(left, right):
    _matrix_shape(left)
    _matrix_shape(right)
    require(len(left[0]) == len(right), "matrix product shape")
    return [
        [
            sum_q(_mul(left[i][k], right[k][j]) for k in range(len(right)))
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def sum_q(values):
    result = ZERO
    for value in values:
        result = _add(result, value)
    return result


def _inverse(matrix):
    _matrix_shape(matrix, square=True)
    n = len(matrix)
    rows = [list(row) + eye for row, eye in zip(matrix, _identity(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j] != ZERO), None)
        require(pivot is not None, "singular matrix")
        rows[j], rows[pivot] = rows[pivot], rows[j]
        diagonal = rows[j][j]
        rows[j] = [_div(x, diagonal) for x in rows[j]]
        for i in range(n):
            if i != j:
                factor = rows[i][j]
                rows[i] = [_sub(x, _mul(factor, y)) for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def _det(matrix):
    _matrix_shape(matrix, square=True, empty=True)
    n = len(matrix)
    if n == 0:
        return ONE
    if n == 1:
        return matrix[0][0]
    return sum_q(
        _mul(
            _q((-1) ** j),
            _mul(
                matrix[0][j],
                _det([[row[k] for k in range(n) if k != j] for row in matrix[1:]]),
            ),
        )
        for j in range(n)
    )


def _positive_minors(matrix, *, strict):
    require(type(strict) is bool, "positivity flag must be bool")
    _matrix_shape(matrix, square=True)
    require(matrix == _adjoint(matrix), "matrix not Hermitian")
    result = []
    for size in range(1, len(matrix) + 1):
        for indices in itertools.combinations(range(len(matrix)), size):
            minor = _det([[matrix[i][j] for j in indices] for i in indices])
            require(minor[1] == 0, "nonreal Hermitian minor")
            require(minor[0] > 0 if strict else minor[0] >= 0, "positivity failure")
            result.append(str(minor[0]))
    return result


def checked_nodes(nodes):
    require(type(nodes) is tuple and 1 <= len(nodes) <= MAX_DEGREE, "node shape/count")
    parsed, degree = [], 0
    for row in nodes:
        require(type(row) is tuple and len(row) == 3, "node row shape")
        real, height = fraction(row[0]), fraction(row[1])
        multiplicity = integer(row[2], 1, MAX_DEGREE)
        require(height > 0, "positive upper-half-plane height required")
        degree += multiplicity
        require(degree <= MAX_DEGREE, "total degree cap")
        parsed.append((real, height, multiplicity))
    require(
        len({row[:2] for row in parsed}) == len(parsed), "merge duplicate node blocks"
    )
    return tuple(parsed)


def gram_control(nodes):
    nodes = checked_nodes(nodes)
    indices = [(_q(y, a), r) for a, y, count in nodes for r in range(count)]
    n = len(indices)
    gram = [
        [
            _div(
                _q(math.comb(r + s, r)),
                _power(_add(_conj(z), v), r + s + 1),
            )
            for v, s in indices
        ]
        for z, r in indices
    ]
    generator = [[ZERO for _ in range(n)] for _ in range(n)]
    for i, (z, r) in enumerate(indices):
        generator[i][i] = _neg(z)
        if i + 1 < n and indices[i + 1] == (z, r + 1):
            generator[i][i + 1] = ONE
    c = [[ONE if r == 0 else ZERO for _, r in indices]]
    first, second = _mm(_adjoint(generator), gram), _mm(gram, generator)
    boundary = _mm(_adjoint(c), c)
    require(
        all(
            _add(first[i][j], second[i][j]) == _neg(boundary[i][j])
            for i in range(n)
            for j in range(n)
        ),
        "Lyapunov identity failed",
    )
    inverse = _inverse(gram)
    require(_mm(gram, inverse) == _identity(n), "inverse verification")
    origin = _mm(_mm(c, inverse), _adjoint(c))[0][0]
    height = sum((y * count for _, y, count in nodes), Fraction())
    require(origin == _q(2 * height), "origin-height constant failed")
    return {
        "nodes": [[str(a), str(y), count] for a, y, count in nodes],
        "degree": n,
        "gram": _matrix_encoded(gram),
        "positive_principal_minors": _positive_minors(gram, strict=True),
        "height_sum": str(height),
        "origin_kernel": _encoded(origin),
        "lyapunov_identity_exact": True,
    }


def _poly_add(left, right):
    require(max(len(left), len(right)) <= MAX_POLY, "polynomial cap")
    return [
        _add(left[i] if i < len(left) else ZERO, right[i] if i < len(right) else ZERO)
        for i in range(max(len(left), len(right)))
    ]


def _poly_mul(left, right):
    require(len(left) + len(right) - 1 <= MAX_POLY, "polynomial cap")
    out = [ZERO] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] = _add(out[i + j], _mul(x, y))
    return out


def _root_poly(roots):
    require(len(roots) < MAX_POLY, "root count cap")
    result = [ONE]
    for root in roots:
        result = _poly_mul(result, [_neg(root), ONE])
    return result


def _poly_eval(poly, point):
    value = ZERO
    for coefficient in reversed(poly):
        value = _add(_mul(value, point), coefficient)
    return value


def _residues(numerator, poles):
    require(len(poles) < MAX_POLY and len(set(poles)) == len(poles), "simple pole cap")
    return [
        _div(
            _poly_eval(numerator, pole),
            math_product_q(
                _sub(pole, other) for j, other in enumerate(poles) if j != i
            ),
        )
        for i, pole in enumerate(poles)
    ]


def math_product_q(values):
    result = ONE
    for value in values:
        result = _mul(result, value)
    return result


def leakage_control():
    # Geographic split: i is retained by radius 3/2; 2+i/4 is omitted.
    geo, b, u = IMAG, _q(2, Fraction(1, 4)), _q(0, Fraction(1, 2))
    lower = (_conj(geo), _conj(b))
    all_poles = lower + (u,)
    numerator = _root_poly((geo, _conj(u)))
    residues = _residues(numerator, all_poles)
    retained = residues[:2]
    plus_num = _poly_add(
        [_mul(retained[0], x) for x in _root_poly((lower[1],))],
        [_mul(retained[1], x) for x in _root_poly((lower[0],))],
    )
    physical_num = _poly_mul(_root_poly((u,)), plus_num)
    physical_poles = (lower[0], _conj(u), lower[1])
    coefficients = _residues(physical_num, physical_poles)
    reconstructed = [ZERO] * len(physical_num)
    for i, coefficient in enumerate(coefficients):
        term = _root_poly(tuple(p for j, p in enumerate(physical_poles) if i != j))
        reconstructed = _poly_add(reconstructed, [_mul(coefficient, x) for x in term])
    require(reconstructed == physical_num, "full partial-fraction polynomial identity")

    # Independently use the literal adjoint values at both denominator nodes.
    before = _residues(_root_poly((geo,)), lower)
    values = [_div(_sub(point, u), _sub(point, _conj(u))) for point in (geo, b)]
    dual_coefficients = [_mul(c, _conj(v)) for c, v in zip(before, values)]
    require(dual_coefficients == retained, "physical Riesz adjoint mismatch")
    require(
        [_mul(c, v) for c, v in zip(before, values)] != retained,
        "raw-value falsifier failed",
    )
    for point in (geo, b):
        full_den_num = _poly_eval(_root_poly((geo, b)), point)
        require(full_den_num == ZERO, "literal denominator zero missing")

    expected = [
        _q(Fraction(24, 73), Fraction(64, 73)),
        _q(Fraction(4, 73), Fraction(-32, 219)),
        _q(Fraction(49, 73), Fraction(-64, 73)),
    ]
    require(coefficients == expected, "geographic leakage coefficients differ")
    origin = sum_q(coefficients)
    origin_square = _mul(origin, _conj(origin))[0]
    derivative_bound = sum(
        (
            (abs(c[0]) + abs(c[1])) * (abs(p[0]) + abs(p[1]))
            for c, p in zip(coefficients, physical_poles)
        ),
        Fraction(),
    )
    cutoff = (origin[0] - 1) / (2 * derivative_bound)
    lower_amplitude = origin[0] - cutoff * derivative_bound
    require(origin_square == Fraction(745, 657), "origin square")
    require(derivative_bound == Fraction(4195, 876), "derivative majorant")
    require(
        cutoff == Fraction(24, 4195) and lower_amplitude == Fraction(75, 73),
        "prefix cutoff",
    )
    require(lower_amplitude**2 > 1, "tail-height violation missing")
    require(1 < Fraction(3, 2) ** 2 < b[0] ** 2 + b[1] ** 2, "geographic split")
    return {
        "retained_node": _encoded(geo),
        "omitted_node": _encoded(b),
        "numerator_zero": _encoded(u),
        "geographic_radius": "3/2",
        "physical_poles": [_encoded(p) for p in physical_poles],
        "physical_time_coefficients": [_encoded(c) for c in coefficients],
        "literal_residual": "R=U-B; O=1; source values at denominator nodes equal U",
        "adjoint_source_coefficients": [_encoded(c) for c in retained],
        "raw_value_substitution_matches": False,
        "origin_ratio": _encoded(origin),
        "origin_ratio_squared": str(origin_square),
        "derivative_majorant": str(derivative_bound),
        "positive_prefix_cutoff": str(cutoff),
        "real_amplitude_lower": str(lower_amplitude),
        "tail_bound_violation_factor": str(lower_amplitude**2),
        "full_polynomial_identity_exact": True,
    }


def singular_control(rank):
    rank = integer(rank, 1, MAX_PANEL)
    lo, hi, delay = Fraction(1, 2), Fraction(1), Fraction(2)
    length = (hi - lo) / rank
    intervals = [(lo + j * length, lo + (j + 1) * length) for j in range(rank)]
    for i, (a, b) in enumerate(intervals):
        require(0 < a < b < delay, "indicator support")
        for j, (c, d) in enumerate(intervals):
            overlap = max(Fraction(), min(b, d) - max(a, c))
            require(overlap / length == int(i == j), "indicator orthogonality")
    return {
        "rank": rank,
        "delay": str(delay),
        "band": [str(lo), str(hi)],
        "intervals": [[str(a), str(b)] for a, b in intervals],
        "squared_indicator_amplitude": str(1 / length),
        "physical_band_trace": rank,
        "denominator_zero_count": 0,
        "zero_height_sum": "0",
        "denominator_is_pure_blaschke": False,
    }


def height_control(rank, endpoint=3):
    rank = integer(rank, 1, MAX_PANEL)
    endpoint = fraction(endpoint)
    require(endpoint > 0, "positive low-pass endpoint")
    partial = sum((Fraction(1, 2**j) for j in range(1, rank + 1)), Fraction())
    remainder = Fraction(1, 2**rank)
    require(partial + remainder == 1, "geometric height sum")
    return {
        "rank": rank,
        "height_partial_sum": str(partial),
        "height_remainder": str(remainder),
        "low_pass_endpoint": str(endpoint),
        "finite_total_bound": str(2 * endpoint * partial),
        "infinite_total_bound": str(2 * endpoint),
        "total_charge_when_U_equals_one": rank,
        "source_tail_bound_asserted": False,
    }


def lacunary_control(rank):
    rank = integer(rank, 1, MAX_PANEL)
    centers = [16 * 2**j for j in range(1, rank + 1)]
    rows = [
        sum((Fraction(2, abs(a - b)) for b in centers if b != a), Fraction())
        for a in centers
    ]
    require(all(row <= Fraction(1, 4) for row in rows), "lacunary Schur bound")
    return {
        "rank": rank,
        "centers": centers,
        "height_each": "1",
        "off_diagonal_row_majorants": [str(row) for row in rows],
        "Gram_operator_upper": "5/4",
        "band_trace_lower_coefficient": str(Fraction(4 * rank, 5)),
        "band_mass_symbol": "exp(-2A)-exp(-2D)>0 for fixed 0<=A<D",
        "scope": "infinite limit proved in note; not actual Xi data",
    }


def normalize(raw):
    require(type(raw) is bytes and len(raw) <= MAX_BYTES, "byte type/cap")
    raw.decode("utf-8")
    return raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def digest(raw):
    return hashlib.sha256(normalize(raw)).hexdigest()


def _json_types(value, depth=0):
    require(depth <= 16, "JSON depth cap")
    require(
        type(value) in (dict, list, str, int, bool, type(None)), "unsupported JSON type"
    )
    if type(value) is dict:
        require(len(value) <= 256, "JSON object cap")
        for key, child in value.items():
            require(type(key) is str and len(key) <= 2048, "JSON key cap")
            _json_types(child, depth + 1)
    elif type(value) is list:
        require(len(value) <= 4096, "JSON list cap")
        for child in value:
            _json_types(child, depth + 1)
    elif type(value) is str:
        require(len(value) <= 2048, "JSON string cap")
    elif type(value) is int:
        require(abs(value).bit_length() <= INTERNAL_BITS, "JSON integer cap")


def render(value):
    _json_types(value)
    return json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + "\n"


def _unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


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


def exact_match(actual, expected):
    require(render(actual) == render(expected), "complete typed replay mismatch")


def manifest_expected():
    return {
        "schema": SOURCE_SCHEMA,
        "authoring_base": BASE,
        "sources": SOURCE_ROWS,
        "external_contract": {
            "url": "https://arxiv.org/pdf/1605.07418v2",
            "role": "classical model-space decomposition (2.12); metadata only",
            "remote_bytes_authenticated": False,
        },
    }


def authenticate_raw(row, raw):
    require(row in SOURCE_ROWS, "unknown typed primitive identity")
    normalize(raw)
    git_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
    require(git_blob == row["git_blob"], "primitive Git blob mismatch")
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
    controls = (
        ((0, 1, 1),),
        ((0, 1, 1), (2, Fraction(1, 4), 1)),
        ((0, 1, 2), (2, Fraction(1, 4), 1)),
        ((-1, Fraction(1, 2), 2), (3, 2, 2)),
    )
    return seal(
        {
            "schema": SCHEMA,
            "arithmetic_class": "MIXED",
            "arithmetic_components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
            "rounding_contract": "exact Fraction/Gaussian pairs; no floating or transcendental evaluation",
            "sources": source_locks(),
            "finite_grams": [gram_control(nodes) for nodes in controls],
            "geographic_source_leakage": leakage_control(),
            "singular_denominator": [singular_control(n) for n in (1, 2, 4, 8)],
            "finite_height_infinite_rank": [height_control(n) for n in (1, 2, 4, 8)],
            "lacunary_infinite_height": [lacunary_control(n) for n in (1, 2, 4, 8)],
            "caps": {
                "degree": MAX_DEGREE,
                "polynomial_coefficients": MAX_POLY,
                "panel": MAX_PANEL,
                "input_bits": INPUT_BITS,
                "internal_bits": INTERNAL_BITS,
                "bytes": MAX_BYTES,
            },
            "scope": {
                "pure_blaschke_denominator_required": True,
                "finite_total_height_required": True,
                "numerator_may_be_any_inner": True,
                "same_physical_projector": True,
                "corrected_adjoint_source": True,
                "low_pass_bound": "C_I<=T_I<=2*L*S for I subset [0,L]",
                "quantitative_bare_tail": "T_I(B,U)-T_I(B_m,U)<=2*L*S_tail",
                "same_quantitative_source_tail": False,
                "source_tail_limit": "nonquantitative monotone convergence at fixed B,U,I",
                "uniform_in_T_capture_proved": False,
                "native_Xi_finite_total_height_proved": False,
                "total_charge_bound_proved": False,
                "shrinking_width_substitution_proved": False,
                "countercontrols_are_actual_Xi": False,
                "analytic_limits_machine_verified": False,
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
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.check:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        check_fixture(read_json(FIXTURE.read_bytes()), report)
        print("PASS_HARDY_COFINAL_FINITE_HEIGHT_SOURCE_CAPTURE")
    else:
        print(render(report), end="")


if __name__ == "__main__":
    main()
