#!/usr/bin/env python3
"""Stream the complete original physical metric at the first full source horizon."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from math import comb, gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
PINS = {
    "helpers": (
        "833f5c6eec591bcee722a5c498a5ac46e3d3dd0a",
        "native_horizon_path_scout.py",
        "ef25a81a73e66dfb347c420126e34c24033bbd8c",
    ),
    "filtration": (
        "2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a",
        "SOURCE_CURVATURE_HORIZON_FILTRATION.md",
        "e6489149479e68ee20bd042c4f03bab58e3e48bf",
    ),
    "twenty_source": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md",
        "2113ce2bef593e19ca647c12c4fbb3c0728572a2",
    ),
    "full_cone": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "EIGHT_QUADRATIC_LAST_ACTIVATION_CONE.md",
        "b74e3bab62a60ef73ae269f634ffb1e9656e9e3f",
    ),
}
PRIMES = (2, 3, 5)
ZERO = (0, 0, 0)
MAX_INDEX = 450
MAX_DEGREE = 8
MAX_RECORDS = 1500
MAX_RATIOS = 600
MAX_BYTES = 8 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sources():
    raw, manifest = {}, []
    for role, (commit, name, blob) in PINS.items():
        ref = f"{commit}:{PREFIX}{name}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "bounded frozen full-source helper")
        value = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        require(
            len(value) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + value).hexdigest() == blob,
            "exact original-source helper identity",
        )
        raw[role] = value
        manifest.append(
            {"role": role, "commit": commit, "path": PREFIX + name, "blob": blob}
        )
    namespace = {
        "__name__": "authenticated_full_rank_path_helpers",
        "__file__": str(HERE / PINS["helpers"][1]),
    }
    # Execute only exact fixed commit/blob-authenticated source-agnostic helpers.
    exec(compile(raw["helpers"], str(HERE / PINS["helpers"][1]), "exec"), namespace)  # noqa: S102
    helper = SimpleNamespace(**namespace)
    poly, kernel, interval = (
        helper.frozen(name, True) for name in ("polynomial", "kernel", "interval")
    )
    kernel.authenticate()
    reference = json.loads(helper.frozen("H25_Gram"))
    return helper, poly, kernel, interval, reference, manifest


def exponents(n):
    require(type(n) is int and 1 <= n <= MAX_INDEX, "declared full-source index")
    result = []
    for prime in PRIMES:
        degree = 0
        while n % prime == 0:
            n //= prime
            degree += 1
        result.append(degree)
    require(all(e <= MAX_DEGREE for e in result), "declared local full-source degree")
    return tuple(result) if n == 1 else None


def root_coefficient(degree):
    require(
        type(degree) is int and 0 <= degree <= MAX_DEGREE,
        "bounded actual half-source degree",
    )
    return (
        F(1)
        if degree == 0
        else -F(comb(2 * degree, degree), 4**degree * (2 * degree - 1))
    )


def half_source(poly, n):
    powers = exponents(n)
    require(powers is not None, "actual fixed-prime support")
    value = {ZERO: F(1)}
    for i, degree in enumerate(powers):
        constant = root_coefficient(degree // 2) if degree % 2 == 0 else F()
        slope = root_coefficient(degree) - constant
        variable = tuple(int(j == i) for j in range(3))
        value = poly.multiply(value, poly.poly({ZERO: constant, variable: slope}))
    if n <= 25:
        require(value == poly.half_source(n), "unchanged actual H25 source")
    return value


def stream_responses(kernel, ratios, plane):
    require(
        len(ratios) <= MAX_RATIOS
        and len(plane) == 4
        and all(len(row) == len(ratios) for row in plane),
        "complete four-plane response dimensions",
    )
    responses = [[kernel.ex() for _ in ratios] for _ in range(4)]
    digest, count, nonzero = sha256(), 0, 0
    for r, (a, b) in enumerate(ratios):
        for s in range(r, len(ratios)):
            c, d = ratios[s]
            entry = kernel.er(
                kernel.gamma(F(a * d, b * c)), kernel.sqrt_rational(F(1, a * b * c * d))
            )
            digest.update(
                (
                    str(r)
                    + ","
                    + str(s)
                    + ":"
                    + canonical(kernel.expr_json(entry))
                    + "\n"
                ).encode()
            )
            count += 1
            if any(entry):
                nonzero += 1
            for j in range(4):
                if plane[j][s]:
                    responses[j][r] = kernel.ea(
                        responses[j][r], kernel.es(entry, plane[j][s])
                    )
                if s != r and plane[j][r]:
                    responses[j][s] = kernel.ea(
                        responses[j][s], kernel.es(entry, plane[j][r])
                    )
    require(
        count == len(ratios) * (len(ratios) + 1) // 2,
        "every upper physical pair streamed",
    )
    return responses, {
        "complete_upper_pair_count": count,
        "nonzero_upper_pair_count": nonzero,
        "complete_upper_pair_sha256": digest.hexdigest(),
    }


def build_model(helper, poly, kernel, interval, reference, horizon):
    require(
        type(horizon) is int and horizon in (25, 450), "registered full-rank horizon"
    )
    numbers = [n for n in range(1, horizon + 1) if exponents(n) is not None]
    polynomials = {n: half_source(poly, n) for n in numbers}
    records, decoders = [], []
    for n in numbers:
        for m in numbers:
            if n * m <= horizon:
                divisor = gcd(n, m)
                records.append(
                    {"n": n, "m": m, "d": divisor, "a": n // divisor, "b": m // divisor}
                )
                decoders.append(helper.record_decoder(polynomials[n], polynomials[m]))
    require(len(records) <= MAX_RECORDS, "complete full-source record cap")
    ratios = sorted({(row["a"], row["b"]) for row in records})
    require(len(ratios) <= MAX_RATIOS, "complete full-source ratio cap")
    positions = {ratio: i for i, ratio in enumerate(ratios)}
    columns = [[F()] * len(ratios) for _ in range(21)]
    for record, decoder in zip(records, decoders, strict=True):
        position = positions[record["a"], record["b"]]
        for j, value in enumerate(decoder):
            columns[j][position] += value / record["d"]
    base_moments = [F(int(i == 2 or j == 9)) for j, (i, _) in enumerate(helper.BASIS)]
    baseline = [
        columns[0][r] + sum(base_moments[j] * columns[j + 1][r] for j in range(20))
        for r in range(len(ratios))
    ]
    plane = [
        baseline,
        columns[1],
        [-2 * x for x in columns[10]],
        [2 * x for x in columns[7]],
    ]
    controls = []
    for name, points in helper.fixed_paths():
        moments = helper.path_moments(poly, points)
        actual = helper.literal_path(poly, polynomials, records, points)
        require(
            actual == helper.decoded_records(decoders, moments),
            "all actual source records on fixed path controls",
        )
        controls.append(
            {
                "name": name,
                "moments": list(map(str, moments)),
                "complete_source": list(map(str, actual)),
            }
        )
    responses, stream = stream_responses(kernel, ratios, plane)
    constant = helper.exact_dot(kernel, plane[0], responses[0])
    cross = [helper.exact_dot(kernel, vector, responses[0]) for vector in plane[1:]]
    gram = [
        [helper.exact_dot(kernel, vector, response) for response in responses[1:]]
        for vector in plane[1:]
    ]
    couplings = [
        [helper.exact_dot(kernel, vector, response) for response in responses]
        for vector in columns[1:]
    ]
    require(
        all(gram[i][j] == gram[j][i] for i in range(3) for j in range(3)),
        "exact symmetric streamed physical Gram",
    )
    for i, (j, scale) in enumerate(((0, 1), (9, -2), (6, 2))):
        require(
            [kernel.es(value, scale) for value in couplings[j]] == [cross[i]] + gram[i],
            "full20 source-gradient normalization",
        )
    if horizon == 25:
        require(
            len(records) == 63 and len(ratios) == 45,
            "complete literal calibration census",
        )
        require(
            kernel.expr_json(constant) == reference["exact_reference_energy"]
            and [kernel.expr_json(x) for x in cross]
            == reference["exact_cross_terms"][:3]
            and [[kernel.expr_json(x) for x in row] for row in gram]
            == [row[:3] for row in reference["exact_Gram"][:3]],
            "streaming original H25 Gram calibration",
        )
        require(
            next(
                row["complete_source"] for row in controls if row["name"] == "axis_235"
            )
            == next(
                row["complete_source"]
                for row in reference["actual_paths"]
                if row["name"] == "axis_235"
            ),
            "unchanged literal H25 source reference",
        )
    return SimpleNamespace(
        helper=helper,
        poly=poly,
        kernel=kernel,
        interval=interval,
        horizon=horizon,
        polynomials=polynomials,
        records=records,
        decoders=decoders,
        ratios=ratios,
        positions=positions,
        columns=columns,
        plane=plane,
        responses=responses,
        stream=stream,
        controls=controls,
        constant=constant,
        cross=cross,
        gram=gram,
        full_couplings=couplings,
        gram_I=[[interval.rounded(kernel.ei(x)) for x in row] for row in gram],
        cross_I=[interval.rounded(kernel.ei(x)) for x in cross],
        constant_I=interval.rounded(kernel.ei(constant)),
        coupling_I=[[interval.rounded(kernel.ei(x)) for x in row] for row in couplings],
    )


def actual_witness(model, attempt):
    helper, kernel, interval = model.helper, model.kernel, model.interval
    center = tuple(map(F, attempt["proposed_exact_binary_center"]))
    points, x6 = interval.rational_path(center)
    x = x6[:3]
    moments = helper.path_moments(model.poly, points)
    actual = helper.literal_path(model.poly, model.polynomials, model.records, points)
    require(
        actual == helper.decoded_records(model.decoders, moments),
        "complete actual rational source witness",
    )
    require(
        (moments[0], (1 - moments[9]) / 2, moments[6] / 2) == x,
        "actual C/2 planar normalization",
    )
    image = [F()] * len(model.ratios)
    for record, value in zip(model.records, actual, strict=True):
        image[model.positions[record["a"], record["b"]]] += value / record["d"]
    predicted = [
        model.plane[0][r] + sum(x[j] * model.plane[j + 1][r] for j in range(3))
        for r in range(len(model.ratios))
    ]
    require(image == predicted, "complete actual physical collection")
    direct, count, digest = kernel.ex(), 0, sha256()
    for r, (a, b) in enumerate(model.ratios):
        for s in range(r, len(model.ratios)):
            c, d = model.ratios[s]
            entry = kernel.er(
                kernel.gamma(F(a * d, b * c)), kernel.sqrt_rational(F(1, a * b * c * d))
            )
            digest.update(
                (
                    str(r)
                    + ","
                    + str(s)
                    + ":"
                    + canonical(kernel.expr_json(entry))
                    + "\n"
                ).encode()
            )
            direct = kernel.ea(
                direct, kernel.es(entry, image[r] * image[s] * (1 if r == s else 2))
            )
            count += 1
    require(
        count == model.stream["complete_upper_pair_count"]
        and digest.hexdigest() == model.stream["complete_upper_pair_sha256"],
        "independent complete physical entry stream",
    )
    predicted_energy = helper.plane_energy(model, x)
    require(
        direct == predicted_energy,
        "literal complete energy equals streamed planar Gram",
    )
    return {
        "exact_binary_center": list(map(str, center)),
        "actual_path_vertices": [list(map(str, row)) for row in points],
        "all_twenty_moments": list(map(str, moments)),
        "planar_A_B_C_half": list(map(str, x)),
        "all_ordered_source_coefficients": list(map(str, actual)),
        "all_physical_rational_coefficients": list(map(str, image)),
        "independent_upper_pair_count": count,
        "independent_upper_pair_sha256": digest.hexdigest(),
        "exact_original_energy": kernel.expr_json(direct),
        "original_energy": interval.interval_json(kernel.ei(direct)),
    }


def discover(phase):
    require(phase in ("calibration", "heldout"), "declared streaming full-source phase")
    helper, poly, kernel, interval, reference, manifest = sources()
    horizon = 25 if phase == "calibration" else 450
    model = build_model(helper, poly, kernel, interval, reference, horizon)
    attempts = []
    for start in interval.STARTS:
        attempt = helper.seed(model, start)
        try:
            attempt["certificate"] = helper.certify(model, attempt)
        except ValueError as error:
            attempt["certificate"] = {
                "root_exists_and_unique_in_box": False,
                "global_all_path_source_optimum_certified": False,
                "retained_guard_failure": str(error),
            }
        attempts.append(attempt)
    first = next(
        (
            i
            for i, row in enumerate(attempts)
            if row["certificate"]["root_exists_and_unique_in_box"]
        ),
        None,
    )
    witness = actual_witness(model, attempts[first]) if first is not None else None
    result = {
        "schema": "riemann.native_six_hour.full_rank_streaming_path_discovery.v1",
        "phase": phase,
        "H": horizon,
        "sources": manifest,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in (
                Path(__file__),
                HERE / "NATIVE_FULL_RANK_PATH_PREREGISTRATION.md",
            )
        },
        "complete_record_count": len(model.records),
        "complete_ratio_count": len(model.ratios),
        "all_ordered_records": model.records,
        "all21_decoder_columns_per_record": [
            list(map(str, row)) for row in model.decoders
        ],
        "all_physical_ratio_order": [{"a": a, "b": b} for a, b in model.ratios],
        "all21_physical_rational_columns": [
            list(map(str, row)) for row in model.columns
        ],
        "all4_exact_planar_response_vectors": [
            [kernel.expr_json(value) for value in row] for row in model.responses
        ],
        "complete_physical_stream": model.stream,
        "fixed_path_decoder_controls": model.controls,
        "exact_planar_reference_energy": kernel.expr_json(model.constant),
        "exact_planar_cross": [kernel.expr_json(value) for value in model.cross],
        "exact_planar_Gram": [
            [kernel.expr_json(value) for value in row] for row in model.gram
        ],
        "exact_full20_by4_physical_couplings": [
            [kernel.expr_json(value) for value in row] for row in model.full_couplings
        ],
        "all16_declared_start_outcomes": attempts,
        "global_certificate_attempts": [
            i
            for i, row in enumerate(attempts)
            if row["certificate"]["global_all_path_source_optimum_certified"]
        ],
        "first_certified_root_witness_index": first,
        "one_complete_actual_witness": witness,
        "full_physical_matrix_stored": False,
        "original_measure_replaced": False,
        "new_physical_rank_measurement_claimed": False,
        "all_height_optimizer_persistence_claimed": False,
        "full_gamma_identified": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "heldout"), required=True)
    args = parser.parse_args()
    raw = (
        json.dumps(discover(args.phase), sort_keys=True, indent=2, allow_nan=False)
        + "\n"
    ).encode()
    require(len(raw) <= MAX_BYTES, "bounded complete streaming-source artifact")
    print(raw.decode(), end="")


if __name__ == "__main__":
    main()
