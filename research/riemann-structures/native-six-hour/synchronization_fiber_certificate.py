"""Proof-bound complete native synchronization-fiber certificate."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from math import gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
FREEZE = "f97b7e00ba0bd3d6153167b477c44c6f153da10f"
PINS = {
    "NATIVE_SYNCHRONIZATION_FIBER_OBSTRUCTION.md": "b1cc4919b113e9cbdaa7c1fd34113434f6f9703f",
    "SYNCHRONIZATION_FIBER_PREREGISTRATION.md": "072019d82f9f01f6597bc22541a23def67fcc60e",
    "synchronization_fiber_scout.py": "c688715abd7819a8c4397a4f59282a511b4fa3c8",
    "synchronization_fiber.discovery.json": "4b9189ab56064db7a9aaf3375835b7d99ee38d50",
}
MAX_BYTES = 8 * 1024 * 1024
FIXTURE = HERE / "synchronization_fiber_certificate.json"
OWNED = (
    HERE / "SYNCHRONIZATION_FIBER_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_native_six_hour_synchronization_fiber.py",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def exact(value):
    need(type(value) in (int, str, F), "literal exact rational")
    if type(value) is str:
        need(len(value) <= 2500, "rational text cap")
    value = F(value)
    need(
        max(value.numerator.bit_length(), value.denominator.bit_length()) <= 4096,
        "rational bit cap",
    )
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(left, right):
    need(canonical(left) == canonical(right), "typed complete source replay mismatch")


def no_float(_value):
    raise ValueError("floating or nonfinite JSON")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")
    return json.loads(
        raw,
        parse_float=no_float,
        parse_constant=no_float,
        object_pairs_hook=unique_object,
    )


def authenticate():
    raw, provenance = {}, []
    for name, expected in PINS.items():
        path = PREFIX + name
        ref = f"{FREEZE}:{path}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        need(0 < size <= MAX_BYTES, "frozen input byte cap")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        blob = sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest()
        need(
            len(data) == size and blob == expected, "exact frozen source authentication"
        )
        if not name.endswith(".json"):
            current = (HERE / name).read_bytes()
            need(
                len(current) <= MAX_BYTES
                and current.replace(b"\r\n", b"\n") == data.replace(b"\r\n", b"\n"),
                "current frozen source changed",
            )
        raw[name] = data
        provenance.append(
            {
                "commit": FREEZE,
                "path": path,
                "blob": blob,
                "sha256": sha256(data).hexdigest(),
            }
        )
    return raw, provenance


def load_source():
    raw, provenance = authenticate()
    name = "synchronization_fiber_scout.py"
    namespace = {
        "__name__": "authenticated_synchronization_fiber",
        "__file__": str(HERE / name),
    }
    exec(compile(raw[name], str(HERE / name), "exec"), namespace)  # noqa: S102
    return (
        SimpleNamespace(**namespace),
        read_json(raw["synchronization_fiber.discovery.json"]),
        provenance,
    )


def polynomial(rows):
    need(type(rows) is list and len(rows) <= 25, "bounded polynomial coefficient list")
    result = {}
    for row in rows:
        need(
            type(row) is list
            and len(row) == 2
            and type(row[0]) is int
            and 0 <= row[0] <= 24,
            "literal polynomial degree",
        )
        degree, value = row[0], exact(row[1])
        need(
            degree not in result and value != 0,
            "nonzero distinct polynomial coefficients",
        )
        result[degree] = value
    return result


def moment(poly, degree=0):
    need(type(degree) is int and 0 <= degree <= 4, "declared moment degree")
    return exact(
        sum((value / (power + degree + 1) for power, value in poly.items()), F())
    )


def multiply(left, right):
    result = {}
    for i, a in left.items():
        for j, b in right.items():
            need(i + j <= 24, "independent polynomial degree cap")
            result[i + j] = exact(result.get(i + j, F()) + a * b)
    return {degree: value for degree, value in result.items() if value}


def determinant(matrix):
    size = len(matrix)
    need(
        1 <= size <= 7 and all(len(row) == size for row in matrix),
        "small exact determinant",
    )
    work = [[exact(value) for value in row] for row in matrix]
    result = F(1)
    for k in range(size):
        pivot = next((i for i in range(k, size) if work[i][k]), None)
        if pivot is None:
            return F()
        if pivot != k:
            work[pivot], work[k] = work[k], work[pivot]
            result = -result
        leading = work[k][k]
        result = exact(result * leading)
        for i in range(k + 1, size):
            ratio = work[i][k] / leading
            for j in range(k + 1, size):
                work[i][j] = exact(work[i][j] - ratio * work[k][j])
            work[i][k] = F()
    return result


def rank(columns):
    need(
        type(columns) is list and 1 <= len(columns) <= 7,
        "at most seven independent columns",
    )
    size = len(columns[0])
    need(
        1 <= size <= 474 and all(len(column) == size for column in columns),
        "complete bounded rank rows",
    )
    work = [[exact(column[i]) for column in columns] for i in range(size)]
    row = 0
    pivots = []
    for column in range(len(columns)):
        pivot = next((i for i in range(row, size) if work[i][column]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        leading = work[row][column]
        for j in range(column, len(columns)):
            work[row][j] = exact(work[row][j] / leading)
        for i in range(row + 1, size):
            multiple = work[i][column]
            for j in range(column, len(columns)):
                work[i][j] = exact(work[i][j] - multiple * work[row][j])
        pivots.append(column)
        row += 1
    return {"rank": row, "pivot_columns": pivots}


def moment_controls(replay):
    data = replay["exact_path_construction"]
    q = data["primitive_Q_coefficients"]
    need(
        type(q) is list
        and len(q) == 5
        and all(type(x) is int for x in q)
        and q[-1] > 0
        and gcd(*q) == 1,
        "primitive marked moment-kernel vector",
    )
    p = polynomial(data["P_coefficients"])
    expected_p = multiply(
        {i: F(value) for i, value in enumerate(q) if value},
        {3: F(1), 4: F(-2), 5: F(1)},
    )
    need(p == expected_p, "source P reconstructed from marked Q")
    observed = [moment(p, j) for j in range(5)]
    need(
        all(observed[j] == 0 for j in (0, 1, 3, 4)) and observed[2] != 0,
        "four original moments and missing quadratic moment",
    )
    replay_equal(list(map(str, observed)), data["P_moments_0_through_4"])
    gram = [
        [F(2, (i + j + 4) * (i + j + 5) * (i + j + 6)) for j in range(5)]
        for i in range(5)
    ]
    principal = [determinant([row[:n] for row in gram[:n]]) for n in range(1, 6)]
    need(
        all(value > 0 for value in principal),
        "positive full polynomial moment Gram matrix",
    )
    replay_equal([list(map(str, gram[j])) for j in (0, 1, 3, 4)], data["matrix"])
    tangent = {degree - 3: degree * value for degree, value in p.items()}
    need(all(degree >= 0 for degree in tangent), "P derivative divisible by t squared")
    norm = sum(map(abs, tangent.values()), F())
    delta = exact(data["delta"])
    need(
        delta == 1 / (1 + norm) and 3 - delta * norm > 2,
        "actual common monotonicity certificate",
    )
    replay_equal(
        [[degree, str(value)] for degree, value in sorted(tangent.items())],
        data["P_prime_div_t_squared"],
    )
    sufficient = []
    for name, sign in (("w_plus", 1), ("w_minus", -1)):
        w = polynomial(replay[name])
        target = {degree: sign * delta * value for degree, value in p.items()}
        target[3] = target.get(3, F()) + 1
        target = {degree: value for degree, value in target.items() if value}
        need(
            w == target and w.get(0, F()) == 0 and sum(w.values()) == 1,
            "same-source actual schedule endpoints",
        )
        square = multiply(w, w)
        sufficient.append([moment(w), moment(w, 1), moment(square), moment(square, 1)])
    need(
        sufficient[0] == sufficient[1], "four independent sufficient path moments agree"
    )
    return {
        "full_Gram_leading_principal_minors": list(map(str, principal)),
        "independent_P_moments": list(map(str, observed)),
        "missing_moment": str(observed[2]),
        "delta": str(delta),
        "derivative_bound_coefficient": str(3 - delta * norm),
        "four_common_original_moments": list(map(str, sufficient[0])),
        "allheight_equality_inferred_from_finite_panel": False,
    }


def census(horizon):
    need(type(horizon) is int and horizon in (60, 300), "two declared product horizons")
    supported = []
    for n in range(1, horizon + 1):
        residual = n
        for prime in (2, 3, 5):
            while residual % prime == 0:
                residual //= prime
        if residual == 1:
            supported.append(n)
    return [
        {"n": n, "m": m, "d": gcd(n, m), "a": n // gcd(n, m), "b": m // gcd(n, m)}
        for n in supported
        for m in supported
        if n * m <= horizon
    ]


def coalesce(vector, rows):
    need(len(vector) == len(rows), "all source coefficients retained")
    result = {}
    for value, row in zip(vector, rows, strict=True):
        key = row["a"], row["b"]
        result[key] = exact(result.get(key, F()) + exact(value) / row["d"])
    return result


def obstruction_controls(replay):
    rows = replay["horizon60_complete_records"]
    replay_equal(rows, census(60))
    need(len(rows) == 140, "complete horizon60 census")
    vectors = replay["horizon60_original_and_synchronized_sources"]
    plus, minus = (list(map(exact, vectors[name])) for name in ("plus", "minus"))
    need(
        len(plus) == len(minus) == 140 and plus == minus,
        "complete original source equality",
    )
    difference = [
        exact(a) - exact(b)
        for a, b in zip(vectors["sync_plus"], vectors["sync_minus"], strict=True)
    ]
    replay_equal(list(map(str, difference)), replay["horizon60_sync_source_difference"])
    image = coalesce(difference, rows)
    target = F(1, 16243587360)
    need(image[3, 5] == target, "exact physical synchronization obstruction")
    selected = [i for i, row in enumerate(rows) if (row["a"], row["b"]) == (3, 5)]
    need(
        [(rows[i]["n"], rows[i]["m"]) for i in selected] == [(3, 5), (6, 10)],
        "both and only source ratio aliases",
    )
    wrong = sum((difference[i] for i in selected), F())
    need(wrong != target, "omitted common-factor weight counterfeit rejected")
    need(
        not any(
            coalesce([a - b for a, b in zip(plus, minus, strict=True)], rows).values()
        ),
        "complete original physical equality",
    )
    return {
        "complete_record_count": 140,
        "ratio3_over5_pairs": [[3, 5], [6, 10]],
        "correct_rational_amplitude": str(target),
        "remaining_physical_weight": "1/sqrt(15)",
        "physical_squared_amplitude": str(target * target / 15),
        "wrong_unweighted_amplitude": str(wrong),
        "initial_v_segment_retained": True,
    }


def area_monomial(power, center):
    value = F(1)
    for degree, middle in zip(power, center, strict=True):
        need(type(degree) is int and 0 <= degree <= 3, "registered curvature power")
        middle = exact(middle)
        low, high = middle - F(1, 32), middle + F(1, 32)
        value *= (high ** (degree + 1) - low ** (degree + 1)) / (degree + 1)
    return exact(value)


def enrichment_controls(replay):
    rows = replay["horizon300_complete_records"]
    replay_equal(rows, census(300))
    need(len(rows) == 474, "complete horizon300 census")
    outputs = []
    need(len(replay["curvature_enrichment"]) == 2, "before and after source panels")
    for synchronized, expected, panel in zip(
        (False, True), (3, 7), replay["curvature_enrichment"], strict=True
    ):
        need(panel["synchronized"] is synchronized, "literal ordered source panel")
        columns = [
            [exact(value) for value in col] for col in panel["complete_record_columns"]
        ]
        need(
            len(columns) == expected and all(len(col) == 474 for col in columns),
            "all literal curvature columns retained",
        )
        literal = rank(columns)
        need(literal["rank"] == expected, "independent literal curvature rank")
        order = panel["ratio_order"]
        physical = []
        for column in columns:
            image = coalesce(column, rows)
            need(
                {tuple(key) for key in order} == set(image),
                "complete physical ratio order",
            )
            physical.append([image[tuple(key)] for key in order])
        replay_equal(
            [list(map(str, col)) for col in physical],
            panel["complete_rational_ratio_columns"],
        )
        observed = rank(physical)
        need(
            observed["rank"] == expected,
            "independently measured physical enrichment rank",
        )
        powers = panel["curvature_monomials"]
        wanted = (
            [[0, 0], [0, 1], [1, 0], [1, 1], [2, 0], [2, 1], [3, 0]]
            if synchronized
            else [[0, 0], [0, 1], [1, 0]]
        )
        replay_equal(powers, wanted)
        witnesses = panel["actual_rectangle_witnesses"]
        if synchronized:
            need(len(witnesses) == 7, "all seven actual rectangle witnesses")
            areas = []
            vectors = []
            for witness in witnesses:
                coefficients = [
                    area_monomial(power, witness["center"]) for power in powers
                ]
                predicted = [
                    sum(
                        (
                            column[i] * coefficient
                            for column, coefficient in zip(
                                columns, coefficients, strict=True
                            )
                        ),
                        F(),
                    )
                    for i in range(474)
                ]
                actual = list(map(exact, witness["source_difference"]))
                need(
                    actual == predicted,
                    "every actual witness record equals independent curvature area",
                )
                vectors.append(actual)
                areas.append(coefficients)
            need(
                determinant(areas) != 0 and rank(vectors)["rank"] == 7,
                "complete independent rectangle matrix",
            )
            witness_digest = sha256(
                canonical([list(map(str, row)) for row in areas]).encode()
            ).hexdigest()
        else:
            need(witnesses == [], "no undeclared original rectangle panel")
            witness_digest = None
        outputs.append(
            {
                "synchronized": synchronized,
                "literal_rank": literal,
                "physical_rank": observed,
                "complete_record_count": 474,
                "complete_ratio_count": len(order),
                "witness_count": len(witnesses),
                "rectangle_matrix_sha256": witness_digest,
            }
        )
    return outputs


def build():
    source, frozen, provenance = load_source()
    replay = source.discover()
    replay_equal(replay, frozen)
    need(
        replay["schema"]
        == "riemann.native_six_hour.synchronization_fiber_discovery.v1",
        "exact discovery schema",
    )
    payload = {
        "schema": "riemann.native_six_hour.synchronization_fiber_certificate.v1",
        "sources": provenance,
        "complete_frozen_source_replay": replay,
        "independent_moment_controls": moment_controls(replay),
        "independent_physical_obstruction": obstruction_controls(replay),
        "independent_enrichment_controls": enrichment_controls(replay),
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "scope": {
            "allheight_original_equality_from_proof_not_finite_extrapolation": True,
            "full_original_source_fiber_synchronization_descent": False,
            "H25_source_retraction_refuted": False,
            "physical_enrichment_rank_independently_checked": True,
            "full_retained_gamma_decoder_identified": False,
        },
    }
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    need(len(canonical(payload).encode()) <= MAX_BYTES, "final certificate byte cap")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        raw = (
            json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
        ).encode()
        need(len(raw) <= MAX_BYTES, "formatted certificate byte cap")
        FIXTURE.write_bytes(raw)
    else:
        need(FIXTURE.stat().st_size <= MAX_BYTES, "fixture byte cap")
        replay_equal(read_json(FIXTURE.read_bytes()), result)
    print(
        canonical(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
