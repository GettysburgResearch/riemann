"""A fixed rational physical minor and absolute bounds for every future alias."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha1, sha256
from itertools import combinations, product
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PRIMES = (2, 3, 5)
LOCAL_CUTOFF = 64
MAX_BYTES = 32 * 1024 * 1024
OUTPUT_BYTES = 16 * 1024 * 1024
PINS = (
    (
        "certificate",
        "a4d610431d5edaf26b00bae903bb9111837e4c31",
        "native_horizon_rank_certificate.json",
        "5e1e3471e9428b339d652440b04cda829673b54d",
    ),
    (
        "certificate_code",
        "a4d610431d5edaf26b00bae903bb9111837e4c31",
        "native_horizon_rank_certificate.py",
        "e77b5d06dc860ea4d4dfe13d12f6ef2fb6db76cf",
    ),
    (
        "heldout",
        "bbdf750a267b5e4c603f99a115c0cac9ec88416f",
        "native_horizon_rank.heldout.json",
        "d887d85dae45cb5912259b08d1773198a61b4219",
    ),
    (
        "completion",
        "822646ffea23d906c385f0273a8c45693e982c4d",
        "FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md",
        "851e4331c12d9f3f073ab73dca26baa33bd5e548",
    ),
    (
        "faithfulness",
        "822646ffea23d906c385f0273a8c45693e982c4d",
        "INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md",
        "f7c42135e276a34d4da00279110666b0f4636080",
    ),
)
OWNED = (
    Path(__file__),
    HERE / "NATIVE_PHYSICAL_MINOR_TAIL_CONTRACTION.md",
    HERE / "NATIVE_PHYSICAL_TAIL_PREREGISTRATION.md",
    ROOT / "tests/test_native_six_hour_physical_tail.py",
)
COORDINATES = tuple(
    (i, j, *powers)
    for i, j in combinations(range(3), 2)
    for powers in product(*(range(2) if k in (i, j) else range(3) for k in range(3)))
)


class Refusal(ValueError):
    """Input/arithmetic/coverage refusal, distinct from an UNKNOWN norm test."""


def need(condition, message):
    if not condition:
        raise Refusal(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal bounded integer")
    return value


def exact(value):
    need(type(value) in (int, F), "literal rational arithmetic")
    value = F(value)
    need(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= 4096,
        "registered rational coefficient bit cap",
    )
    return value


def plus(values):
    result = F()
    for value in values:
        result = exact(result + exact(value))
    return result


def times(values):
    result = F(1)
    for value in values:
        result = exact(result * exact(value))
    return result


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(actual, expected):
    need(canonical(actual) == canonical(expected), "typed complete tail replay")


def no_float(_value):
    raise Refusal("nonintegral JSON number")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded JSON bytes")
    return json.loads(
        raw,
        parse_float=no_float,
        parse_constant=no_float,
        object_pairs_hook=unique_object,
    )


def rational(value):
    need(type(value) is str and 0 < len(value) <= 2500, "canonical rational string")
    result = exact(F(value))
    need(str(result) == value, "canonical rational spelling")
    return result


def git_bytes(commit, path, expected=None):
    need(
        type(commit) is str
        and len(commit) == 40
        and all(c in "0123456789abcdef" for c in commit),
        "exact commit required",
    )
    ref = f"{commit}:{path}"
    blob = subprocess.check_output(
        ["git", "rev-parse", ref], cwd=ROOT, text=True
    ).strip()
    if expected is not None:
        need(blob == expected, "frozen tail source blob")
    size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
    need(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
    need(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "actual frozen Git bytes",
    )
    return raw, {"commit": commit, "path": path, "blob": blob}


def body_check(payload):
    need(
        type(payload) is dict and type(payload.get("proof_object_sha256")) is str,
        "complete proof object",
    )
    body = {
        key: value for key, value in payload.items() if key != "proof_object_sha256"
    }
    need(
        sha256(canonical(body).encode()).hexdigest() == payload["proof_object_sha256"],
        "complete proof object digest",
    )


def frozen_minor():
    raw, provenance = {}, []
    # Every direct source is authenticated before any discovery is parsed.
    for label, commit, name, blob in PINS:
        raw[label], identity = git_bytes(commit, PREFIX + name, blob)
        provenance.append(identity)
    certificate, capture = read_json(raw["certificate"]), read_json(raw["heldout"])
    body_check(certificate)
    body_check(capture)
    need(
        certificate["schema"] == "native-horizon-rank-certificate-v1"
        and certificate["physical_rank_equals_literal_at_every_declared_horizon"]
        is True
        and type(certificate["all_integer_horizons_through"]) is int
        and certificate["all_integer_horizons_through"] == 900,
        "complete bounded atlas certificate",
    )
    need(
        capture["schema"] == "native-original-horizon-curvature-discovery-v1"
        and capture["phase"] == "heldout",
        "actual held-out capture",
    )
    equal(capture["coordinates"], [list(row) for row in COORDINATES])
    panels = [
        row for row in capture["all_declared_thresholds"] if row["horizon"] == 900
    ]
    need(len(panels) == 1, "unique frozen H900 panel")
    panel = panels[0]
    rank = panel["physical_rank"]
    need(type(rank["rank"]) is int and rank["rank"] == 20, "actual frozen rank20")
    rows, columns = rank["independent_rows"], rank["pivot_coordinates"]
    need(
        type(rows) is list
        and type(columns) is list
        and len(rows) == len(columns) == 20,
        "fixed20 rational rows and coordinates",
    )
    for value in rows:
        integer(value, 0, len(panel["all_physical_curvature_rows"]) - 1)
    for value in columns:
        integer(value, 0, 35)
    need(len(set(rows)) == len(set(columns)) == 20, "distinct fixed minor indices")
    selected = [panel["all_physical_curvature_rows"][i] for i in rows]
    ratios = []
    for row in selected:
        ratio = row["ratio"]
        need(type(ratio) is list and len(ratio) == 2, "reduced physical ratio")
        a, b = (integer(n, 1, 900) for n in ratio)
        need(gcd(a, b) == 1 and a * b <= 900, "actual fixed ratio and norm")
        exponents(a)
        exponents(b)
        ratios.append((a, b))
    need(len(set(ratios)) == 20, "distinct fixed physical ratios")
    return {
        "ratios": ratios,
        "coordinate_indices": columns,
        "row_indices": rows,
        "frozen_selected_rows": selected,
        "source_records": capture["complete_source_records"],
        "provenance": provenance,
    }


def exponents(number):
    integer(number, 1, 2**20)
    result = []
    for prime in PRIMES:
        exponent = 0
        while number % prime == 0:
            exponent += 1
            number //= prime
        result.append(exponent)
    need(number == 1, "three-prime supported index")
    return tuple(result)


@lru_cache(maxsize=81, typed=True)
def coefficient(degree):
    integer(degree, 0, 80)
    return (
        F(1)
        if degree == 0
        else exact(coefficient(degree - 1) * F(2 * degree - 3, 2 * degree))
    )


def local_source(degree):
    integer(degree, 0, 80)
    a = coefficient(degree // 2) if degree % 2 == 0 else F()
    return a, exact(coefficient(degree) - a)


@lru_cache(maxsize=20000, typed=True)
def local(k, alpha, beta):
    integer(k, 0, 64)
    integer(alpha, 0, 9)
    integer(beta, 0, 9)
    a, b = local_source(k + alpha)
    c, d = local_source(k + beta)
    return (exact(a * c), exact(a * d + b * c), exact(b * d), exact(b * c - a * d))


def coordinate_terms(coordinate):
    i, j, *powers = coordinate
    if powers[i] == powers[j] == 1:
        return ()
    rest = list(powers)
    if powers[i] == powers[j] == 0:
        first, second = rest.copy(), rest.copy()
        first[i], first[j], second[i], second[j] = 3, 1, 1, 3
        return ((1, tuple(first)), (-1, tuple(second)))
    if powers[i] == 0:
        rest[i], rest[j] = 3, 2
        return ((2, tuple(rest)),)
    rest[i], rest[j] = 2, 3
    return ((-2, tuple(rest)),)


def source_coordinate(values, coordinate, majorant=False):
    terms = []
    for scalar, types in coordinate_terms(coordinate):
        term = times(values[k][types[k]] for k in range(3))
        terms.append(exact(abs(scalar) * abs(term) if majorant else scalar * term))
    return plus(terms)


def supported_aliases(maximum):
    integer(maximum, 1, 1024)
    powers = []
    for prime in PRIMES:
        row, number = [], 1
        while number <= maximum:
            row.append(number)
            number *= prime
        powers.append(row)
    values = sorted(a * b * c for a, b, c in product(*powers) if a * b * c <= maximum)
    need(
        len(values) == len(set(values)) and len(values) <= 200,
        "complete bounded alias set",
    )
    return values


@lru_cache(maxsize=1000, typed=True)
def local_sum(prime, alpha, beta, kind):
    need(type(prime) is int and prime in PRIMES, "declared local prime")
    integer(kind, 0, 3)
    terms = [
        exact(abs(local(k, alpha, beta)[kind]) / prime**k)
        for k in range(LOCAL_CUTOFF + 1)
    ]
    partial = plus(terms)
    ua = abs(coefficient((LOCAL_CUTOFF + 1 + alpha) // 2))
    ub = abs(coefficient((LOCAL_CUTOFF + 1 + beta) // 2))
    multiplier = 2 if kind in (1, 3) else 1
    remainder = exact(
        multiplier * ua * ub * F(1, prime ** (LOCAL_CUTOFF + 1)) / (1 - F(1, prime))
    )
    if kind == 3 and alpha == beta:
        need(partial == 0, "equal local sources have zero determinant")
        remainder = F()
    upper = exact(partial + remainder)
    return {
        "prime": prime,
        "alpha": alpha,
        "beta": beta,
        "kind": kind,
        "terms": terms,
        "partial": partial,
        "remainder": remainder,
        "upper": upper,
        "endpoint_coefficient_bounds": (ua, ub),
    }


def total_majorant(alpha, beta, coordinate, tables):
    result = F()
    for scalar, kinds in coordinate_terms(coordinate):
        factors = []
        for k, prime in enumerate(PRIMES):
            key = (prime, alpha[k], beta[k], kinds[k])
            table = local_sum(*key)
            tables[key] = table
            factors.append(table["upper"])
        result = exact(result + abs(scalar) * times(factors))
    return result


def sparse(values):
    return [[i, str(value)] for i, value in enumerate(values) if value]


def decode_sparse(raw):
    need(type(raw) is list and len(raw) <= 36, "bounded sparse source row")
    result, previous = [F()] * 36, -1
    for pair in raw:
        need(type(pair) is list and len(pair) == 2, "literal sparse pair")
        i = integer(pair[0], 0, 35)
        need(i > previous, "ordered unique sparse coordinates")
        value = rational(pair[1])
        need(value != 0, "nonzero sparse value")
        result[i], previous = value, i
    return result


def matrix_product(left, right):
    need(
        type(left) is list and type(right) is list and left and right,
        "nonempty exact matrices",
    )
    width = len(right[0])
    need(
        all(len(row) == len(right) for row in left)
        and all(len(row) == width for row in right),
        "matrix product dimensions",
    )
    return [
        [
            plus(exact(a * b) for a, b in zip(row, column, strict=True))
            for column in zip(*right, strict=True)
        ]
        for row in left
    ]


def inverse_exact(matrix):
    need(type(matrix) is list and 1 <= len(matrix) <= 20, "inverse matrix cap")
    n = len(matrix)
    need(
        all(type(row) is list and len(row) == n for row in matrix),
        "square exact matrix",
    )
    identity = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    work = [
        [exact(x) for x in row] + identity[i].copy() for i, row in enumerate(matrix)
    ]
    determinant = F(1)
    for column in range(n):
        pivot = next((i for i in range(column, n) if work[i][column]), None)
        if pivot is None:
            return None
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            determinant = -determinant
        value = work[column][column]
        determinant = exact(determinant * value)
        work[column] = [exact(x / value) for x in work[column]]
        for i in range(n):
            if i != column:
                factor = work[i][column]
                work[i] = [
                    exact(x - factor * y)
                    for x, y in zip(work[i], work[column], strict=True)
                ]
    inverse = [row[n:] for row in work]
    need(
        matrix_product(matrix, inverse) == identity
        and matrix_product(inverse, matrix) == identity,
        "both actual inverse products",
    )
    return {
        "matrix": inverse,
        "determinant": determinant,
        "both_products_identity": True,
    }


def contraction(matrix, tail):
    n = len(matrix)
    need(
        len(tail) == n and all(len(row) == n for row in tail), "tail matrix dimensions"
    )
    need(
        all(exact(value) >= 0 for row in tail for value in row),
        "nonnegative entrywise tail",
    )
    inverse = inverse_exact(matrix)
    if inverse is None:
        return {
            "status": "UNKNOWN_SINGULAR_MINOR",
            "inverse": None,
            "row_sums": None,
            "theta": None,
            "all_future_horizons_certified": False,
        }
    product_bound = matrix_product(
        [[abs(x) for x in row] for row in inverse["matrix"]], tail
    )
    row_sums = [plus(row) for row in product_bound]
    theta = max(row_sums)
    success = theta < 1
    return {
        "status": "PASS" if success else "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        "inverse": inverse,
        "absolute_inverse_times_tail": product_bound,
        "row_sums": row_sums,
        "theta": theta,
        "all_future_horizons_certified": success,
    }


def panel(minor, horizon):
    need(
        type(horizon) is int and horizon in (900, 2**20), "only declared fixed horizons"
    )
    indices = minor["coordinate_indices"]
    matrix, tails, rows, tables = [], [], [], {}
    frozen_records = {
        (row["n"], row["m"]): row["curvature"] for row in minor["source_records"]
    }
    for number, (a, b) in enumerate(minor["ratios"]):
        alpha, beta = exponents(a), exponents(b)
        maximum = isqrt(horizon // (a * b))
        source_total, prefix = [F()] * 36, [F()] * 20
        aliases = []
        for g in supported_aliases(maximum):
            values = [
                local(k, x, y)
                for k, x, y in zip(exponents(g), alpha, beta, strict=True)
            ]
            source = [source_coordinate(values, c) for c in COORDINATES]
            majorant = [
                source_coordinate(values, COORDINATES[c], True) for c in indices
            ]
            need(
                all(
                    abs(source[c]) <= bound
                    for c, bound in zip(indices, majorant, strict=True)
                ),
                "actual coordinate bounded by its own positive majorant",
            )
            if horizon == 900:
                need((g * a, g * b) in frozen_records, "complete frozen alias source")
                equal(sparse(source), frozen_records[(g * a, g * b)])
            for i, value in enumerate(source):
                source_total[i] = exact(source_total[i] + value / g)
            for i, value in enumerate(majorant):
                prefix[i] = exact(prefix[i] + value / g)
            aliases.append(
                {
                    "g": g,
                    "source_curvature": sparse(source),
                    "majorant_coordinates": majorant,
                }
            )
        if horizon == 900:
            equal(
                sparse(source_total),
                minor["frozen_selected_rows"][number]["coordinates"],
            )
        total = [total_majorant(alpha, beta, COORDINATES[c], tables) for c in indices]
        tail = [
            exact(upper - known) for upper, known in zip(total, prefix, strict=True)
        ]
        need(all(value >= 0 for value in tail), "same-majorant prefix subtraction")
        matrix.append([source_total[c] for c in indices])
        tails.append(tail)
        rows.append(
            {
                "ratio": (a, b),
                "maximum_alias": maximum,
                "complete_aliases": aliases,
                "all36_source_coordinates": sparse(source_total),
                "positive_prefix": prefix,
                "infinite_majorant_upper": total,
                "tail": tail,
            }
        )
    result = {
        "horizon": horizon,
        "rows": rows,
        "matrix": matrix,
        "tail": tails,
        "local_tables": [tables[key] for key in sorted(tables)],
        "contraction": contraction(matrix, tails),
        "every_later_partial_prefix_bounded": True,
    }
    if horizon == 900:
        need(
            result["contraction"]["inverse"] is not None,
            "independent frozen minor invertibility",
        )
    return result


def encoded(value):
    if type(value) is F:
        return str(value)
    if type(value) in (tuple, list):
        return [encoded(x) for x in value]
    if type(value) is dict:
        return {key: encoded(x) for key, x in value.items()}
    need(value is None or type(value) in (str, int, bool), "serializable exact record")
    return value


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def calibration_gate(commit):
    provenance = []
    for path in OWNED:
        relative = path.relative_to(ROOT).as_posix()
        raw, identity = git_bytes(commit, relative)
        need(
            raw.replace(b"\r\n", b"\n") == path.read_bytes().replace(b"\r\n", b"\n"),
            "unchanged calibration algorithm/declaration/tests before heldout",
        )
        provenance.append(identity)
    raw, identity = git_bytes(commit, PREFIX + "native_physical_tail.calibration.json")
    payload = read_json(raw)
    body_check(payload)
    need(
        payload["schema"] == "native-fixed-physical-minor-future-tail-v1"
        and payload["phase"] == "calibration",
        "accepted calibration identity",
    )
    equal(payload["owned_sha256_lf"], owned_bindings())
    provenance.append(identity)
    return payload, provenance


def build(phase, calibration_commit=None):
    need(phase in ("calibration", "heldout"), "declared acquisition phase")
    calibration, calibration_provenance = None, None
    if phase == "heldout":
        calibration, calibration_provenance = calibration_gate(calibration_commit)
    else:
        need(calibration_commit is None, "calibration has no prior-result override")
    minor = frozen_minor()
    selection = {
        key: minor[key] for key in ("ratios", "coordinate_indices", "row_indices")
    }
    calibration_result = panel(minor, 900)
    if calibration is not None:
        equal(calibration["selection"], encoded(selection))
        equal(calibration["result"], encoded(calibration_result))
    result = calibration_result if phase == "calibration" else panel(minor, 2**20)
    payload = {
        "schema": "native-fixed-physical-minor-future-tail-v1",
        "phase": phase,
        "source": minor["provenance"],
        "calibration_freeze": calibration_provenance,
        "owned_sha256_lf": owned_bindings(),
        "selection": selection,
        "result": result,
        "scope": {
            "native_gamma_decoder_claimed": False,
            "new_energy_minimum_claimed": False,
            "heldout_only_result_bridges_901_to_2pow20minus1": False,
            "all_horizons_rank_equality_certified": calibration_result["contraction"][
                "all_future_horizons_certified"
            ],
        },
    }
    payload = encoded(payload)
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    need(len(canonical(payload).encode()) <= OUTPUT_BYTES, "retained artifact byte cap")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "heldout"), required=True)
    parser.add_argument("--calibration-commit")
    args = parser.parse_args()
    payload = build(args.phase, args.calibration_commit)
    target = HERE / f"native_physical_tail.{args.phase}.json"
    target.write_text(canonical(payload) + "\n", encoding="utf-8")
    result = payload["result"]
    print(
        canonical(
            {
                "phase": args.phase,
                "horizon": result["horizon"],
                "status": result["contraction"]["status"],
                "theta": result["contraction"]["theta"],
                "all_future_horizons_certified": result["contraction"][
                    "all_future_horizons_certified"
                ],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
