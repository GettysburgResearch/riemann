"""Authenticate and independently certify the complete native horizon-rank atlas."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import combinations, product
from math import gcd
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
CALIBRATION = "7e62a06c97ad4cd621fc70e228cb661913bf0439"
HELDOUT = "bbdf750a267b5e4c603f99a115c0cac9ec88416f"
THEORY = "2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a"
SCOUT = "native_horizon_rank_scout.py"
DECLARATION = "NATIVE_HORIZON_RANK_PREREGISTRATION.md"
PINS = (
    (
        "calibration_scout",
        CALIBRATION,
        SCOUT,
        "18d05ce42154ff6ef1ac62c8bf0daa5bd7160ad4",
    ),
    (
        "calibration_prereg",
        CALIBRATION,
        DECLARATION,
        "67758039f8d2a8ae7f2e26c3b893615560680e44",
    ),
    (
        "calibration",
        CALIBRATION,
        "native_horizon_rank.calibration.json",
        "628b79fd8d81754a103826b744c56525ba89dcb4",
    ),
    ("heldout_scout", HELDOUT, SCOUT, "18d05ce42154ff6ef1ac62c8bf0daa5bd7160ad4"),
    (
        "heldout_prereg",
        HELDOUT,
        DECLARATION,
        "67758039f8d2a8ae7f2e26c3b893615560680e44",
    ),
    (
        "heldout",
        HELDOUT,
        "native_horizon_rank.heldout.json",
        "d887d85dae45cb5912259b08d1773198a61b4219",
    ),
    (
        "theory",
        THEORY,
        "SOURCE_CURVATURE_HORIZON_FILTRATION.md",
        "e6489149479e68ee20bd042c4f03bab58e3e48bf",
    ),
)
MODULUS = 65521
MAX_BYTES = 32 * 1024 * 1024
OUTPUT_BYTES = 1024 * 1024
FIXTURE = HERE / "native_horizon_rank_certificate.json"
OWNED = (
    Path(__file__),
    HERE / "NATIVE_HORIZON_RANK_REPLAY.md",
    ROOT / "tests/test_native_six_hour_horizon_rank.py",
)
COORDINATES = tuple(
    (i, j, *powers)
    for i, j in combinations(range(3), 2)
    for powers in product(*(range(2) if k in (i, j) else range(3) for k in range(3)))
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def replay_equal(actual, expected):
    require(canonical(actual) == canonical(expected), "typed complete replay mismatch")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def no_float(_value):
    raise ValueError("nonintegral JSON number")


def read_json(raw):
    require(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "JSON byte cap")
    return json.loads(
        raw,
        object_pairs_hook=unique_object,
        parse_float=no_float,
        parse_constant=no_float,
    )


def integer(value, low, high):
    require(type(value) is int and low <= value <= high, "literal bounded integer")
    return value


def rational(value):
    require(type(value) is str and 0 < len(value) <= 2500, "literal rational string")
    result = F(value)
    require(str(result) == value, "canonical exact rational string")
    require(
        max(result.numerator.bit_length(), result.denominator.bit_length()) <= 4096,
        "rational bit cap",
    )
    return result


def sparse_row(value):
    require(type(value) is list and len(value) <= 36, "sparse coordinate row")
    result, previous = {}, -1
    for item in value:
        require(type(item) is list and len(item) == 2, "coordinate pair")
        column = integer(item[0], 0, 35)
        require(column > previous, "strictly ordered unique coordinates")
        entry = rational(item[1])
        require(entry != 0, "zero sparse entry")
        result[column], previous = entry, column
    return result


def sparse_value(row):
    return [[column, str(value)] for column, value in sorted(row.items()) if value]


def supported_numbers(maximum):
    integer(maximum, 1, 900)
    values = set()
    power2 = 1
    while power2 <= maximum:
        power3 = power2
        while power3 <= maximum:
            power5 = power3
            while power5 <= maximum:
                values.add(power5)
                power5 *= 5
            power3 *= 3
        power2 *= 2
    return sorted(values)


def literal_jumps():
    result = []
    for degree in product(range(3), repeat=3):
        partial = degree.count(1)
        jump = partial if 2 in degree else max(0, partial - 1)
        if jump:
            cost = 2 ** degree[0] * 3 ** degree[1] * 5 ** degree[2]
            result.append({"horizon": cost, "degree": list(degree), "jump": jump})
    return sorted(result, key=lambda row: row["horizon"])


def literal_dimension(horizon):
    integer(horizon, 1, 900)
    return sum(row["jump"] for row in literal_jumps() if row["horizon"] <= horizon)


def authenticate():
    raw, provenance = {}, []
    for label, commit, name, expected in PINS:
        ref = f"{commit}:{PREFIX}{name}"
        size = int(
            subprocess.check_output(["git", "cat-file", "-s", ref], cwd=ROOT, text=True)
        )
        require(0 < size <= MAX_BYTES, "frozen source byte cap")
        data = subprocess.check_output(["git", "show", ref], cwd=ROOT)
        blob = sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest()
        require(len(data) == size and blob == expected, "exact frozen atlas source")
        raw[label] = data
        provenance.append(
            {"role": label, "commit": commit, "path": PREFIX + name, "blob": blob}
        )
    require(
        raw["calibration_scout"] == raw["heldout_scout"], "unchanged heldout executable"
    )
    require(
        raw["calibration_prereg"] == raw["heldout_prereg"],
        "unchanged acquisition declaration",
    )
    for label, name in (("heldout_scout", SCOUT), ("heldout_prereg", DECLARATION)):
        current = (HERE / name).read_bytes()
        require(
            len(current) <= MAX_BYTES
            and current.replace(b"\r\n", b"\n") == raw[label].replace(b"\r\n", b"\n"),
            "frozen acquisition binding changed",
        )
    return raw, provenance


def load_source():
    raw, provenance = authenticate()
    namespace = {
        "__name__": "authenticated_horizon_atlas",
        "__file__": str(HERE / SCOUT),
    }
    exec(compile(raw["heldout_scout"], str(HERE / SCOUT), "exec"), namespace)  # noqa: S102
    captures = {phase: read_json(raw[phase]) for phase in ("calibration", "heldout")}
    return SimpleNamespace(**namespace), captures, provenance


def validate_header(record, phase):
    require(type(record) is dict and phase in ("calibration", "heldout"), "atlas phase")
    require(
        record.get("schema") == "native-original-horizon-curvature-discovery-v1",
        "discovery schema",
    )
    require(record.get("phase") == phase, "phase identity")
    require(
        record.get("predicted_rank_is_not_assigned") is True,
        "measured source-rank flag",
    )
    require(
        record.get("all_height_physical_rank_theorem_claimed") is False,
        "bounded physical scope",
    )
    require(record.get("native_gamma_decoder_claimed") is False, "native source scope")
    require(
        type(record.get("source_theory_full_rank_prediction")) is int,
        "literal source prediction",
    )
    require(record["source_theory_full_rank_prediction"] == 20, "source dimension")
    replay_equal(record.get("coordinates"), [list(row) for row in COORDINATES])
    digest = record.get("proof_object_sha256")
    core = {key: value for key, value in record.items() if key != "proof_object_sha256"}
    require(
        type(digest) is str and sha256(canonical(core).encode()).hexdigest() == digest,
        "discovery proof digest",
    )


def validate_records(record, maximum):
    numbers = supported_numbers(maximum)
    expected = [(n, m) for n in numbers for m in numbers if n * m <= maximum]
    rows = record.get("complete_source_records")
    require(
        type(rows) is list and len(rows) == len(expected) <= 5000,
        "complete ordered source census",
    )
    decoded = []
    for item, (n, m) in zip(rows, expected, strict=True):
        require(type(item) is dict, "source record object")
        for key in ("n", "m", "d", "a", "b"):
            integer(item.get(key), 1, maximum)
        divisor = gcd(n, m)
        replay_equal(
            [item[key] for key in ("n", "m", "d", "a", "b")],
            [n, m, divisor, n // divisor, m // divisor],
        )
        decoded.append(sparse_row(item.get("curvature")))
    return rows, decoded


def coalesce(rows, decoded, indices):
    result = {}
    for index in indices:
        item = rows[index]
        ratio = (item["a"], item["b"])
        target = result.setdefault(ratio, {})
        for column, value in decoded[index].items():
            target[column] = target.get(column, F()) + value / item["d"]
    return result


def modular_rank(rows):
    require(type(rows) is list and len(rows) <= 2000, "modular row cap")
    basis, selected, columns = {}, [], []
    for index, row in enumerate(rows):
        require(type(row) is dict and len(row) <= 36, "modular sparse row")
        vector = [0] * 36
        for column, value in row.items():
            integer(column, 0, 35)
            require(type(value) is F, "modular exact rational")
            denominator = value.denominator % MODULUS
            require(denominator != 0, "fixed-prime denominator refusal")
            vector[column] = value.numerator * pow(denominator, -1, MODULUS) % MODULUS
        for column in range(36):
            if not vector[column]:
                continue
            if column not in basis:
                inverse = pow(vector[column], -1, MODULUS)
                basis[column] = [value * inverse % MODULUS for value in vector]
                selected.append(index)
                columns.append(column)
                break
            multiple = vector[column]
            vector = [
                (value - multiple * pivot) % MODULUS
                for value, pivot in zip(vector, basis[column], strict=True)
            ]
    return {
        "prime": MODULUS,
        "rank": len(basis),
        "independent_rows": selected,
        "pivot_columns": columns,
    }


def audit_panel(panel, rows, decoded):
    require(type(panel) is dict, "panel object")
    horizon = integer(panel.get("horizon"), 1, 900)
    expected_indices = [
        i for i, row in enumerate(rows) if row["n"] * row["m"] <= horizon
    ]
    replay_equal(panel.get("complete_record_indices"), expected_indices)
    integer(panel.get("record_count"), 1, 5000)
    require(panel["record_count"] == len(expected_indices), "panel record coverage")
    physical = coalesce(rows, decoded, expected_indices)
    require(len(physical) <= 2000, "physical ratio cap")
    integer(panel.get("ratio_count"), 1, 2000)
    require(panel["ratio_count"] == len(physical), "complete reduced-ratio coverage")
    expected_rows = [
        {"ratio": list(ratio), "coordinates": sparse_value(physical[ratio])}
        for ratio in sorted(physical)
    ]
    replay_equal(panel.get("all_physical_curvature_rows"), expected_rows)
    source_rank = integer(panel["source_rank"].get("rank"), 0, 20)
    image_rank = integer(panel["physical_rank"].get("rank"), 0, 20)
    upper = literal_dimension(horizon)
    require(source_rank == upper, "actual raw rank equals independent source theorem")
    lower = modular_rank([physical[ratio] for ratio in sorted(physical)])
    require(
        lower["rank"] == upper == image_rank,
        "fixed-prime physical lower bound meets literal upper bound",
    )
    return {
        "horizon": horizon,
        "records": len(expected_indices),
        "ratios": len(physical),
        "literal_upper_bound": upper,
        "captured_rational_source_rank": source_rank,
        "captured_rational_physical_rank": image_rank,
        "independent_modular_physical_lower_bound": lower,
        "physical_rows_sha256": sha256(canonical(expected_rows).encode()).hexdigest(),
    }


def certify_phase(record, phase):
    validate_header(record, phase)
    maximum = 30 if phase == "calibration" else 900
    rows, decoded = validate_records(record, maximum)
    expected = [
        n for n in supported_numbers(maximum) if phase == "calibration" or n > 30
    ]
    panels = record.get("all_declared_thresholds")
    require(
        type(panels) is list and len(panels) == len(expected),
        "complete phase threshold coverage",
    )
    replay_equal([row.get("horizon") for row in panels], expected)
    certified = [audit_panel(panel, rows, decoded) for panel in panels]
    geometry = record.get("geometry")
    require(type(geometry) is dict, "geometric source controls")
    require(
        type(geometry.get("rectangle_coordinate_matrix_rank")) is int,
        "literal rectangle rank",
    )
    require(
        geometry["rectangle_coordinate_matrix_rank"] == 36,
        "complete rectangle interpolation",
    )
    checks = geometry.get("complete_row_basis_four_edge_checks")
    require(
        type(checks) is list and len(checks) == literal_dimension(maximum),
        "complete source-basis accessibility",
    )
    require(
        all(
            type(row.get("all36_actual_rectangle_differences")) is list
            and len(row["all36_actual_rectangle_differences"]) == 36
            for row in checks
        ),
        "all36 four-edge evaluations per source basis row",
    )
    return {
        "phase": phase,
        "maximum": maximum,
        "discovery_proof_object_sha256": record["proof_object_sha256"],
        "complete_records": len(rows),
        "panel_count": len(certified),
        "panels": certified,
        "literal_rectangle_interpolation_rank": 36,
        "literal_four_edge_checks": 36 * len(checks),
    }


def build():
    module, captures, provenance = load_source()
    phases = []
    for phase in ("calibration", "heldout"):
        replay, _summary = module.discover(phase)
        replay_equal(read_json(replay.encode()), captures[phase])
        phases.append(certify_phase(captures[phase], phase))
    panels = [panel for phase in phases for panel in phase["panels"]]
    require(
        len(panels) == 83
        and [row["horizon"] for row in panels] == supported_numbers(900),
        "all83 supported thresholds",
    )
    first_full = next(
        row["horizon"] for row in panels if row["literal_upper_bound"] == 20
    )
    require(
        first_full == 450, "first source and physical saturation within declared atlas"
    )
    result = {
        "schema": "native-horizon-rank-certificate-v1",
        "source": provenance,
        "owned_sha256_lf": {
            path.relative_to(ROOT).as_posix(): sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "independent_literal_jump_formula": literal_jumps(),
        "phases": phases,
        "all_integer_horizons_through": 900,
        "first_full_rank_horizon_in_declared_range": first_full,
        "physical_rank_equals_literal_at_every_declared_horizon": True,
        "physical_equality_beyond_900_claimed": False,
        "native_gamma_decoder_claimed": False,
        "scalar_energy_minimum_claimed": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    require(len(canonical(result).encode()) <= OUTPUT_BYTES, "certificate output cap")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--write", action="store_true")
    choice.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(canonical(result) + "\n", encoding="utf-8")
    else:
        replay_equal(read_json(FIXTURE.read_bytes()), result)
    print(
        canonical(
            {
                "proof_object_sha256": result["proof_object_sha256"],
                "panels": 83,
                "first_full_rank": 450,
            }
        )
    )


if __name__ == "__main__":
    main()
