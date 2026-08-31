#!/usr/bin/env python3
"""Full acquisition replay and independent controls at native horizon450."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
from math import gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = {
    "scout": (
        "530ab2d0ee328c4902b102a693941ab49c860949",
        "native_full_rank_path_scout.py",
        "a0c7840dc3360dfc13668fde710ec62b5ea6e9d9",
    ),
    "calibration": (
        "530ab2d0ee328c4902b102a693941ab49c860949",
        "native_full_rank_path.calibration.json",
        "6fdef16d18889ad406ad033d42090d9a4a1f5c6c",
    ),
    "preregistration": (
        "530ab2d0ee328c4902b102a693941ab49c860949",
        "NATIVE_FULL_RANK_PATH_PREREGISTRATION.md",
        "edd11b956a231ccdbcbdb7737c00a6079b2c566c",
    ),
    "heldout_scout": (
        "a4f6ea24a703d183e569d4257ed8d7e867089b86",
        "native_full_rank_path_scout.py",
        "a0c7840dc3360dfc13668fde710ec62b5ea6e9d9",
    ),
    "heldout": (
        "a4f6ea24a703d183e569d4257ed8d7e867089b86",
        "native_full_rank_path.heldout.json",
        "3ef7cfb60878a8d26466df1293ddcca5293014d3",
    ),
    "controls": (
        "284ddc66a75387cf77ec7551f93fa990724decf0",
        "native_horizon_path_certificate.py",
        "b4d0868196f65d75ad54059debd7b897dfd959cf",
    ),
    "filtration": (
        "2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a",
        "SOURCE_CURVATURE_HORIZON_FILTRATION.md",
        "e6489149479e68ee20bd042c4f03bab58e3e48bf",
    ),
}
MAX_BYTES = 8 * 1024 * 1024
FIXTURE = HERE / "native_full_rank_path_certificate.json"
NOTE = HERE / "FULL_RANK_NATIVE_PATH_OPTIMUM.md"
TEST = ROOT / "tests/test_native_six_hour_full_rank_path.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(left, right):
    require(canonical(left) == canonical(right), "typed complete full-rank replay")


def frozen(role, execute=False):
    require(role in PINS, "complete full-rank acquisition pin")
    commit, name, blob = PINS[role]
    ref = f"{commit}:{PREFIX}{name}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen full-rank source")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact full-rank source authentication",
    )
    if not execute:
        return raw
    namespace = {
        "__name__": "authenticated_full_rank_certificate_source",
        "__file__": str(HERE / name),
    }
    # Execute only fixed commit/blob-authenticated source and validation helpers.
    exec(compile(raw, str(HERE / name), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def smooth_numbers(horizon):
    require(
        type(horizon) is int and horizon in (25, 450),
        "declared calibration or full source horizon",
    )
    numbers = set()
    a = 1
    while a <= horizon:
        b = a
        while b <= horizon:
            c = b
            while c <= horizon:
                numbers.add(c)
                c *= 5
            b *= 3
        a *= 2
    return sorted(numbers)


def rank_mod65521(rows):
    require(
        type(rows) is list
        and 0 < len(rows) <= 20
        and all(type(row) is list and len(row) == len(rows[0]) for row in rows)
        and 0 < len(rows[0]) <= 600,
        "bounded twenty-direction rank matrix",
    )
    require(
        all(type(x) is F and x.denominator % 65521 for row in rows for x in row),
        "exact rank coefficients with invertible denominators",
    )
    matrix = [
        [x.numerator * pow(x.denominator, -1, 65521) % 65521 for x in row]
        for row in rows
    ]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = pow(matrix[rank][column], -1, 65521)
        matrix[rank] = [(x * scale) % 65521 for x in matrix[rank]]
        for i in range(rank + 1, len(matrix)):
            scale = matrix[i][column]
            if scale:
                matrix[i] = [
                    (a - scale * b) % 65521
                    for a, b in zip(matrix[i], matrix[rank], strict=True)
                ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def source_control(scout, helper, poly, controls, data):
    horizon = data["H"]
    numbers = smooth_numbers(horizon)
    expected = []
    for n, m in product(numbers, repeat=2):
        if n * m <= horizon:
            d = gcd(n, m)
            expected.append({"n": n, "m": m, "d": d, "a": n // d, "b": m // d})
    equal(expected, data["all_ordered_records"])
    equal(data["complete_record_count"], len(expected))
    polynomials = {n: scout.half_source(poly, n) for n in numbers}
    coefficients = [
        helper.record_decoder(polynomials[row["n"]], polynomials[row["m"]])
        for row in expected
    ]
    equal(
        data["all21_decoder_columns_per_record"],
        [list(map(str, row)) for row in coefficients],
    )
    ratios = sorted({(row["a"], row["b"]) for row in expected})
    equal(data["all_physical_ratio_order"], [{"a": a, "b": b} for a, b in ratios])
    equal(data["complete_ratio_count"], len(ratios))
    positions = {ratio: j for j, ratio in enumerate(ratios)}
    columns = [[F()] * len(ratios) for _ in range(21)]
    for record, row in zip(expected, coefficients, strict=True):
        position = positions[record["a"], record["b"]]
        for j, value in enumerate(row):
            columns[j][position] += value / record["d"]
    equal(
        data["all21_physical_rational_columns"],
        [list(map(str, row)) for row in columns],
    )
    weights = (1, 2, 3)
    moments = [controls.moment_on_power_path(i, p, weights) for i, p in helper.BASIS]
    digest = sha256()
    for record, decoder in zip(expected, coefficients, strict=True):
        direct = F()
        for left, lc in polynomials[record["n"]].items():
            dl = sum(a * b for a, b in zip(left, weights, strict=True))
            for right, rc in polynomials[record["m"]].items():
                dr = sum(a * b for a, b in zip(right, weights, strict=True))
                if dl + dr:
                    direct += lc * rc * F(2 * dl, dl + dr)
        decoded = decoder[0] + sum(
            a * b for a, b in zip(decoder[1:], moments, strict=True)
        )
        require(
            direct == decoded, "actual higher-prime-power current on a nonlinear path"
        )
        digest.update(
            (
                str(record["n"]) + "," + str(record["m"]) + ":" + str(direct) + "\n"
            ).encode()
        )
    rank = rank_mod65521(columns[1:])
    require(
        rank == (6 if horizon == 25 else 20), "previously measured physical source rank"
    )
    stream = data["complete_physical_stream"]
    equal(stream["complete_upper_pair_count"], len(ratios) * (len(ratios) + 1) // 2)
    require(
        type(stream["nonzero_upper_pair_count"]) is int
        and 0
        <= stream["nonzero_upper_pair_count"]
        <= stream["complete_upper_pair_count"],
        "literal nonzero stream count",
    )
    witness = data["one_complete_actual_witness"]
    if witness is not None:
        equal(
            witness["independent_upper_pair_count"], stream["complete_upper_pair_count"]
        )
        equal(
            witness["independent_upper_pair_sha256"],
            stream["complete_upper_pair_sha256"],
        )
    return {
        "H": horizon,
        "records": len(expected),
        "ratios": len(ratios),
        "complete_upper_pair_count": stream["complete_upper_pair_count"],
        "physical_direction_rank_mod65521": rank,
        "nonlinear_power_path": list(weights),
        "nonlinear_source_coefficient_sha256": digest.hexdigest(),
    }


def validate_outcomes(controls, data):
    attempts = data["all16_declared_start_outcomes"]
    require(
        type(attempts) is list and len(attempts) == 16,
        "all sixteen preregistered starts",
    )
    starts = [
        [str(a), str(b)]
        for a, b in product(
            (F(-1, 2), F(-1, 8), F(1, 8), F(1, 2)), (F(1, 2), F(1), F(3, 2), F(2))
        )
    ]
    equal([row["start"] for row in attempts], starts)
    successes = [i for i, row in enumerate(attempts) if controls.validate_attempt(row)]
    equal(successes, data["global_certificate_attempts"])
    first = next(
        (
            i
            for i, row in enumerate(attempts)
            if row["certificate"]["root_exists_and_unique_in_box"]
        ),
        None,
    )
    equal(first, data["first_certified_root_witness_index"])
    require(
        (data["one_complete_actual_witness"] is None) is (first is None),
        "actual witness selected by first root",
    )
    unique = [
        i
        for i in successes
        if all(
            controls.rational(row["lower_envelope_minimum"]) > 0
            for row in attempts[i]["certificate"]["eight_source_quadratics"]
        )
    ]
    for flag in (
        "full_physical_matrix_stored",
        "original_measure_replaced",
        "new_physical_rank_measurement_claimed",
        "all_height_optimizer_persistence_claimed",
        "full_gamma_identified",
    ):
        require(data[flag] is False, "unchanged finite original-source scope")
    selected = attempts[successes[0]]["certificate"] if successes else None
    return {
        "all_global_certificate_attempts": successes,
        "strict_unique_path_attempts": unique,
        "first_actual_witness_root_index": first,
        "first_global_root_box": selected["root_box"] if selected else None,
        "first_global_energy": selected["root_energy"] if selected else None,
        "first_global_clipping": selected["clipping_regime"] if selected else None,
    }


def stream_control(scout, kernel):
    ratios = [(1, 1), (2, 1)]
    plane = [[F(1), F(2)], [F(3), F()], [F(), F(5)], [F(-2), F(7)]]
    responses, stream = scout.stream_responses(kernel, ratios, plane)
    k00 = kernel.gamma(F(1))
    k01 = kernel.er(kernel.gamma(F(2)), kernel.sqrt_rational(F(1, 2)))
    k11 = kernel.es(k00, F(1, 2))
    expected = [
        [
            kernel.ea(kernel.es(k00, a), kernel.es(k01, b)),
            kernel.ea(kernel.es(k01, a), kernel.es(k11, b)),
        ]
        for a, b in plane
    ]
    require(
        responses == expected and stream["complete_upper_pair_count"] == 3,
        "original-kernel stream includes both off-diagonal responses and one diagonal",
    )
    return {
        "ratios": ratios,
        "four_rational_plane_vectors": [list(map(str, row)) for row in plane],
        "complete_upper_pair_count": 3,
        "physical_denominator_retained": True,
    }


def build():
    raw = {role: frozen(role) for role in PINS}
    require(
        raw["scout"] == raw["heldout_scout"], "unchanged heldout streaming executable"
    )
    scout, controls = frozen("scout", True), frozen("controls", True)
    helper, poly, kernel, _, _, _ = scout.sources()
    panels, objects = [], {}
    for phase, horizon in (("calibration", 25), ("heldout", 450)):
        data = json.loads(raw[phase])
        equal(data["H"], horizon)
        equal(scout.discover(phase), data)
        panel = source_control(scout, helper, poly, controls, data)
        panel.update(validate_outcomes(controls, data))
        panels.append(panel)
        objects[phase] = data["proof_object_sha256"]
    result = {
        "schema": "riemann.native_six_hour.full_rank_path_certificate.v1",
        "sources": [
            {"role": role, "commit": c, "path": PREFIX + p, "blob": b}
            for role, (c, p, b) in PINS.items()
        ],
        "panels": panels,
        "full_unchanged_acquisition_replayed": True,
        "independent_monomial_controls": controls.monomial_control(helper),
        "independent_original_kernel_stream_control": stream_control(scout, kernel),
        "acquisition_proof_objects": objects,
        "all_height_optimizer_claimed": False,
        "full_gamma_identified": False,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in (Path(__file__), NOTE, TEST)
        },
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    raw = (
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n"
    ).encode()
    require(len(raw) <= MAX_BYTES, "bounded full-rank final certificate")
    if args.write:
        FIXTURE.write_bytes(raw)
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "bounded full-rank fixture")
        equal(json.loads(FIXTURE.read_bytes()), result)
    print(
        "PASS complete original-kernel H450 replay, all source directions and independent controls"
    )


if __name__ == "__main__":
    main()
