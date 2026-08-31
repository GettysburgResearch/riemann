#!/usr/bin/env python3
"""Independent controls for the complete twenty-moment horizon-path campaign."""

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
# The heldout capture and identical executable are installed after that phase freezes.
PINS = {
    "scout": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "native_horizon_path_scout.py",
        "ef25a81a73e66dfb347c420126e34c24033bbd8c",
    ),
    "calibration": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "native_horizon_path.calibration.json",
        "8b565dcd476cf371dfdba4c2f6427feb094613a1",
    ),
    "preregistration": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "NATIVE_HORIZON_PATH_PREREGISTRATION.md",
        "7ce6b0777aae7e36d637bbb527f1b8a55472cd38",
    ),
    "twenty_moment_source": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md",
        "2113ce2bef593e19ca647c12c4fbb3c0728572a2",
    ),
    "full_cone": (
        "69b5322bc872b46d42d4f74e13dcbeb96c1421da",
        "EIGHT_QUADRATIC_LAST_ACTIVATION_CONE.md",
        "b74e3bab62a60ef73ae269f634ffb1e9656e9e3f",
    ),
    "physical_alias_source": (
        "0daaef322d86bcc3de26037e98e24b53b72e7441",
        "NATIVE_FIXED_PLANAR_LAST_COORDINATE_SUPPORT.md",
        "8f35ebf64c5f0ca2865068e411e96bbb0a5b020b",
    ),
    "heldout_scout": (
        "833f5c6eec591bcee722a5c498a5ac46e3d3dd0a",
        "native_horizon_path_scout.py",
        "ef25a81a73e66dfb347c420126e34c24033bbd8c",
    ),
    "heldout": (
        "833f5c6eec591bcee722a5c498a5ac46e3d3dd0a",
        "native_horizon_path.heldout.json",
        "84109e72410f53101c63e2c8f8514e873efc3fa8",
    ),
}
MAX_BYTES = 8 * 1024 * 1024
FIXTURE = HERE / "native_horizon_path_certificate.json"
NOTE = HERE / "NATIVE_HIGHER_HORIZON_PATH_REPLAY.md"
TEST = ROOT / "tests/test_native_six_hour_horizon_path.py"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def strict_equal(left, right):
    require(canonical(left) == canonical(right), "typed complete horizon-path replay")


def rational(value):
    require(
        type(value) is str and 0 < len(value) <= 2500, "bounded literal rational string"
    )
    result = F(value)
    require(str(result) == value, "canonical exact rational")
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= 8192,
        "rational bit cap",
    )
    return result


def interval(value):
    require(type(value) is dict, "interval object")
    lower, upper = rational(value["lower"]), rational(value["upper"])
    require(lower <= upper, "ordered exact interval")
    return lower, upper


def frozen(name, execute=False):
    require(name in PINS, "final acquisition pins not yet installed")
    commit, path, blob = PINS[name]
    ref = f"{commit}:{PREFIX}{path}"
    size = int(
        subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
    )
    require(0 < size <= MAX_BYTES, "bounded frozen horizon source")
    raw = subprocess.check_output(["git", "show", ref], cwd=ROOT)
    require(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "exact horizon acquisition authentication",
    )
    if not execute:
        return raw
    namespace = {
        "__name__": "authenticated_horizon_path_final",
        "__file__": str(HERE / path),
    }
    # Only fixed commit/blob-authenticated acquisition bytes are executable.
    exec(compile(raw, str(HERE / path), "exec"), namespace)  # noqa: S102
    return SimpleNamespace(**namespace)


def supported(maximum):
    require(
        type(maximum) is int and maximum in (25, 30, 60), "registered finite horizon"
    )
    values = set()
    a = 1
    while a <= maximum:
        b = a
        while b <= maximum:
            c = b
            while c <= maximum:
                values.add(c)
                c *= 5
            b *= 3
        a *= 2
    return sorted(values)


def moment_on_power_path(differential, powers, weights):
    require(type(differential) is int and 0 <= differential < 3, "literal differential")
    require(
        type(powers) is tuple
        and len(powers) == 3
        and all(type(x) is int and 0 <= x <= 2 for x in powers),
        "literal moment exponents",
    )
    require(
        type(weights) is tuple
        and len(weights) == 3
        and all(type(x) is int and 1 <= x <= 4 for x in weights),
        "bounded power-path weights",
    )
    denominator = weights[differential] + sum(
        a * b for a, b in zip(powers, weights, strict=True)
    )
    return F(weights[differential], denominator)


def monomial_control(scout):
    cases, digest = 0, sha256()
    for weights in product((1, 2, 3), repeat=3):
        moments = [moment_on_power_path(i, p, weights) for i, p in scout.BASIS]
        for left, right in product(scout.CORNERS, repeat=2):
            dl = sum(a * b for a, b in zip(weights, left, strict=True))
            dr = sum(a * b for a, b in zip(weights, right, strict=True))
            direct = F(2 * dl, dl + dr) if dl + dr else F()
            row = scout.monomial_decoder(left, right)
            decoded = row[0] + sum(x * y for x, y in zip(row[1:], moments, strict=True))
            require(decoded == direct, "independent power-path derivative integral")
            digest.update(
                (str((weights, left, right)) + ":" + str(direct) + "\n").encode()
            )
            cases += 1
    require(cases == 1728, "all64 monomial pairs on all27 fixed power paths")
    return {
        "cases": cases,
        "exact_coefficient_digest": digest.hexdigest(),
        "literal_measure_factor": 2,
    }


def minimum_quadratic(coefficients):
    require(
        type(coefficients) is tuple
        and len(coefficients) == 3
        and all(type(x) is F for x in coefficients),
        "three exact quadratic coefficients",
    )
    c, b, a = coefficients
    candidates = [(c, F()), (a + b + c, F(1))]
    if a > 0:
        vertex = -b / (2 * a)
        if 0 < vertex < 1:
            candidates.append((a * vertex * vertex + b * vertex + c, vertex))
    return min(candidates)


def validate_cone(rows):
    require(type(rows) is list and len(rows) == 8, "all eight source quadratics")
    labels = [
        (family, sigma, tau)
        for sigma, tau in product((0, 1), repeat=2)
        for family in ("p", "q")
    ]
    for row, label in zip(rows, labels, strict=True):
        require(
            type(row["sigma"]) is int and type(row["tau"]) is int,
            "literal cone endpoint",
        )
        require(
            (row["family"], row["sigma"], row["tau"]) == label,
            "complete ordered cone labels",
        )
        coefficients = tuple(
            map(interval, row["coefficient_intervals_constant_linear_quadratic"])
        )
        require(len(coefficients) == 3, "complete quadratic coefficient list")
        lower = minimum_quadratic(tuple(x[0] for x in coefficients))
        upper = minimum_quadratic(tuple(x[1] for x in coefficients))
        require(
            tuple(
                map(rational, (row["lower_envelope_minimum"], row["lower_minimizer"]))
            )
            == lower,
            "independent lower-envelope minimum",
        )
        require(
            tuple(
                map(rational, (row["upper_envelope_minimum"], row["upper_minimizer"]))
            )
            == upper,
            "independent upper-envelope minimum",
        )
        status = "PASS" if lower[0] >= 0 else "FAIL" if upper[0] < 0 else "UNKNOWN"
        require(row["status"] == status, "actual exact cone status")
    return all(row["status"] == "PASS" for row in rows)


def validate_attempt(attempt):
    certificate = attempt["certificate"]
    require(
        type(certificate.get("root_exists_and_unique_in_box")) is bool,
        "literal root flag",
    )
    require(
        type(certificate.get("global_all_path_source_optimum_certified")) is bool,
        "literal global flag",
    )
    if not certificate["root_exists_and_unique_in_box"]:
        require(
            certificate["global_all_path_source_optimum_certified"] is False
            and type(certificate.get("retained_guard_failure")) is str,
            "retained root refusal",
        )
        return False
    centers = tuple(map(rational, attempt["proposed_exact_binary_center"]))
    require(len(centers) == 2, "complete root center")
    boxes = list(map(interval, certificate["root_box"]))
    images = list(map(interval, certificate["Krawczyk_image"]))
    require(len(boxes) == len(images) == 2, "complete root box and image")
    for center, box, image in zip(centers, boxes, images, strict=True):
        require(
            box == (center - F(1, 2**30), center + F(1, 2**30)),
            "entire declared root box",
        )
        require(
            box[0] < image[0] <= image[1] < box[1],
            "strict whole-box Krawczyk inclusion",
        )
    lam, mu = boxes
    require(
        mu[0] > 0 and lam[1] < 1 and lam[0] + mu[0] > 0,
        "nonempty increasing clipping band",
    )
    lower = True if lam[1] < 0 else False if lam[0] > 0 else None
    upper = True if lam[0] + mu[0] > 1 else False if lam[1] + mu[1] < 1 else None
    require(lower is not None and upper is not None, "strict clipping regime")
    regime = certificate["clipping_regime"]
    require(
        regime["lower_clipped"] is lower and regime["upper_clipped"] is upper,
        "actual certified endpoint clipping",
    )
    contraction = rational(certificate["contraction_upper"])
    require(0 <= contraction < 1, "strict rational contraction")
    preconditioner = [list(map(rational, row)) for row in certificate["preconditioner"]]
    require(
        len(preconditioner) == 2 and all(len(row) == 2 for row in preconditioner),
        "two-dimensional preconditioner",
    )
    require(
        preconditioner[0][0] * preconditioner[1][1]
        != preconditioner[0][1] * preconditioner[1][0],
        "invertible rational preconditioner",
    )
    positive = interval(certificate["planar_source_c"])[0] > 0
    require(
        certificate["last_activation_subclass_optimum_certified"] is positive,
        "literal planar positivity",
    )
    passed = validate_cone(certificate["eight_source_quadratics"])
    require(
        certificate["global_all_path_source_optimum_certified"]
        is (positive and passed),
        "full source cone required for global claim",
    )
    return positive and passed


def validate_panel(panel):
    horizon = panel["H"]
    numbers = supported(horizon)
    expected = [(n, m) for n in numbers for m in numbers if n * m <= horizon]
    rows = panel["all_ordered_records"]
    require(
        type(rows) is list and len(rows) == len(expected),
        "complete actual ordered-record census",
    )
    for row, (n, m) in zip(rows, expected, strict=True):
        d = gcd(n, m)
        strict_equal(row, {"n": n, "m": m, "d": d, "a": n // d, "b": m // d})
    require(
        type(panel["complete_record_count"]) is int
        and panel["complete_record_count"] == len(rows),
        "literal record count",
    )
    decoders = panel["all21_decoder_columns_per_record"]
    require(
        type(decoders) is list and len(decoders) == len(rows),
        "every record decoder retained",
    )
    decoded = [list(map(rational, row)) for row in decoders]
    require(
        all(len(row) == 21 for row in decoded), "constant plus all20 source columns"
    )
    ratios = sorted({(row["a"], row["b"]) for row in rows})
    strict_equal(
        panel["all_physical_ratio_order"], [{"a": a, "b": b} for a, b in ratios]
    )
    require(
        type(panel["complete_ratio_count"]) is int
        and panel["complete_ratio_count"] == len(ratios),
        "literal ratio count",
    )
    positions = {ratio: i for i, ratio in enumerate(ratios)}
    columns = [[F()] * len(ratios) for _ in range(21)]
    for row, coefficients in zip(rows, decoded, strict=True):
        position = positions[row["a"], row["b"]]
        for i, value in enumerate(coefficients):
            columns[i][position] += value / row["d"]
    strict_equal(
        panel["all21_physical_rational_columns"],
        [list(map(str, row)) for row in columns],
    )
    require(
        panel["all20_physical_directions_claimed_independent"] is False
        and panel["full_gamma_identified"] is False,
        "actual source scope",
    )
    attempts = panel["all16_declared_start_outcomes"]
    require(
        type(attempts) is list and len(attempts) == 16, "all declared starts retained"
    )
    expected_starts = [
        [str(a), str(b)]
        for a, b in product(
            (F(-1, 2), F(-1, 8), F(1, 8), F(1, 2)), (F(1, 2), F(1), F(3, 2), F(2))
        )
    ]
    strict_equal([row["start"] for row in attempts], expected_starts)
    successes = [i for i, attempt in enumerate(attempts) if validate_attempt(attempt)]
    strict_equal(panel["global_certificate_attempts"], successes)
    unique = [
        i
        for i in successes
        if all(
            rational(row["lower_envelope_minimum"]) > 0
            for row in attempts[i]["certificate"]["eight_source_quadratics"]
        )
    ]
    first = attempts[successes[0]]["certificate"] if successes else None
    return {
        "horizon": horizon,
        "records": len(rows),
        "ratios": len(ratios),
        "all_global_certificate_attempts": successes,
        "strict_unique_oriented_path_attempts": unique,
        "first_certified_root_box": first["root_box"] if first else None,
        "first_certified_clipping_regime": first["clipping_regime"] if first else None,
        "first_certified_energy": first["root_energy"] if first else None,
        "refused_attempts": [
            i
            for i, row in enumerate(attempts)
            if not row["certificate"]["root_exists_and_unique_in_box"]
        ],
    }


def source_alias_control(scout, panel):
    require(panel["H"] == 60, "registered complete higher-source control")
    weights = (1, 1, 2)
    moments = [moment_on_power_path(i, p, weights) for i, p in scout.BASIS]
    require(
        (moments[5], moments[12]) == (F(1, 5), F(1, 2)),
        "actual quadratic last-coordinate moments",
    )
    sums = {2: F(), 5: F()}
    divisors = {2: [], 5: []}
    for record, values in zip(
        panel["all_ordered_records"],
        panel["all21_decoder_columns_per_record"],
        strict=True,
    ):
        if record["b"] == 1 and record["a"] in sums:
            coefficients = list(map(rational, values))
            value = coefficients[0] + sum(
                x * y for x, y in zip(coefficients[1:], moments, strict=True)
            )
            sums[record["a"]] += value / record["d"]
            divisors[record["a"]].append(record["d"])
    require(
        divisors == {2: [1, 2, 3, 4, 5], 5: [1, 2, 3]},
        "complete actual H60 ratio aliases",
    )
    require(
        sums[2] == -F(26831, 23040) - F(1, 200) and sums[5] == -F(53, 48) - F(5, 96),
        "independent physical coefficient formulas",
    )
    return {
        "power_path": [1, 1, 2],
        "M6": "1/5",
        "M13": "1/2",
        "sqrt2_times_ratio2_coefficient": str(sums[2]),
        "sqrt5_times_ratio5_coefficient": str(sums[5]),
        "all_gcd_aliases": divisors,
    }


def build():
    require(
        "heldout" in PINS and "heldout_scout" in PINS,
        "final heldout acquisition pins not yet installed",
    )
    raw = {name: frozen(name) for name in PINS}
    require(
        raw["scout"] == raw["heldout_scout"], "unchanged heldout horizon executable"
    )
    scout = frozen("scout", True)
    captures = {phase: json.loads(raw[phase]) for phase in ("calibration", "heldout")}
    panels = []
    for phase, horizons in (("calibration", [25]), ("heldout", [30, 60])):
        data = captures[phase]
        strict_equal(scout.discover(phase), data)
        require(
            data["physical_measure_is_original"] is True
            and data["all_height_global_optimum_claimed"] is False
            and data["full_retained_gamma_identified"] is False,
            "original measure and finite source scope",
        )
        strict_equal([row["H"] for row in data["panels"]], horizons)
        panels.extend(validate_panel(row) for row in data["panels"])
    result = {
        "schema": "riemann.native_six_hour.higher_horizon_path_certificate.v1",
        "sources": [
            {"role": name, "commit": commit, "path": PREFIX + path, "blob": blob}
            for name, (commit, path, blob) in PINS.items()
        ],
        "panels": panels,
        "independent_all_monomial_control": monomial_control(scout),
        "independent_physical_alias_control": source_alias_control(
            scout, captures["heldout"]["panels"][1]
        ),
        "complete_acquisition_proof_objects": {
            phase: data["proof_object_sha256"] for phase, data in captures.items()
        },
        "full_gamma_identified": False,
        "all_height_optimum_claimed": False,
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
    require(len(raw) <= MAX_BYTES, "bounded final source-path certificate")
    if args.write:
        FIXTURE.write_bytes(raw)
    else:
        require(
            FIXTURE.stat().st_size <= MAX_BYTES, "bounded final source-path fixture"
        )
        strict_equal(json.loads(FIXTURE.read_bytes()), result)
    print("PASS complete original-source horizon paths and independent exact controls")


if __name__ == "__main__":
    main()
