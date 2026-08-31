"""Preserve and independently audit both fixed-minor UNKNOWN outcomes."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
CALIBRATION = "3ba479241acf9db1554af067d5e2bea85533dde5"
HELDOUT = "179d4c78a81cbe9eb7214c2b5a9eca041d197c46"
PINS = (
    (
        CALIBRATION,
        PREFIX + "NATIVE_PHYSICAL_MINOR_TAIL_CONTRACTION.md",
        "82c61f5e4a83da0bc0a96140bb483c02a06c3a4c",
    ),
    (
        CALIBRATION,
        PREFIX + "NATIVE_PHYSICAL_TAIL_PREREGISTRATION.md",
        "cdadf991c63898a26b804f53cd91ac5cd8e00a95",
    ),
    (
        CALIBRATION,
        PREFIX + "native_physical_tail_scout.py",
        "24ef243220c8159f78505717d639d88287fbf439",
    ),
    (
        CALIBRATION,
        "tests/test_native_six_hour_physical_tail.py",
        "d69120d4b26290b6d356cba4c6e347b8b47cc43f",
    ),
    (
        CALIBRATION,
        PREFIX + "native_physical_tail.calibration.json",
        "e4306d1ae72043efa7f80d9d7c8b9183f5d46ac8",
    ),
    (
        HELDOUT,
        PREFIX + "native_physical_tail.heldout.json",
        "382a0268b4f31948239b98333a34277fe6cef8b6",
    ),
    (
        "2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a",
        PREFIX + "SOURCE_CURVATURE_HORIZON_FILTRATION.md",
        "e6489149479e68ee20bd042c4f03bab58e3e48bf",
    ),
)
MAX_BYTES = 32 * 1024 * 1024
OWNED = (
    Path(__file__),
    HERE / "NATIVE_PHYSICAL_TAIL_REPLAY.md",
    ROOT / "tests/test_native_six_hour_physical_tail_certificate.py",
)
FIXTURE = HERE / "native_physical_tail_certificate.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(actual, expected):
    need(canonical(actual) == canonical(expected), "complete typed certificate differs")


def no_float(_value):
    raise ValueError("floating or nonfinite JSON")


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded source bytes")
    return json.loads(
        raw, parse_float=no_float, parse_constant=no_float, object_pairs_hook=unique
    )


def rational(value):
    need(type(value) is str and 0 < len(value) <= 2500, "literal rational spelling")
    result = F(value)
    need(
        str(result) == value
        and max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= 4096,
        "canonical bounded rational",
    )
    return result


def body_check(payload):
    need(
        type(payload) is dict and type(payload.get("proof_object_sha256")) is str,
        "complete proof object",
    )
    body = {k: v for k, v in payload.items() if k != "proof_object_sha256"}
    need(
        sha256(canonical(body).encode()).hexdigest() == payload["proof_object_sha256"],
        "proof object digest",
    )


def authenticate():
    raw, provenance = {}, []
    for commit, path, expected in PINS:
        blob = subprocess.check_output(
            ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(blob == expected, "frozen final-tail source identity")
        size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
        need(0 < size <= MAX_BYTES, "source byte cap")
        data = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(
            len(data) == size
            and sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest() == blob,
            "actual Git blob bytes",
        )
        need(
            data.replace(b"\r\n", b"\n")
            == (ROOT / path).read_bytes().replace(b"\r\n", b"\n"),
            "frozen source changed in checkout",
        )
        raw[path] = data
        provenance.append({"commit": commit, "path": path, "blob": blob})
    return raw, provenance


def source():
    raw, provenance = authenticate()
    # No acquisition parse or executable import occurs before all direct pins.
    path = PREFIX + "native_physical_tail_scout.py"
    namespace = {
        "__name__": "frozen_physical_tail_acquisition",
        "__file__": str(ROOT / path),
    }
    exec(compile(raw[path], str(ROOT / path), "exec"), namespace)  # noqa: S102
    calibration = read_json(raw[PREFIX + "native_physical_tail.calibration.json"])
    heldout = read_json(raw[PREFIX + "native_physical_tail.heldout.json"])
    body_check(calibration)
    body_check(heldout)
    return SimpleNamespace(**namespace), calibration, heldout, provenance


def sparse36(raw):
    need(type(raw) is list, "sparse source list")
    result, previous = [F()] * 36, -1
    for row in raw:
        need(type(row) is list and len(row) == 2, "sparse coordinate pair")
        index, text = row
        need(
            type(index) is int and previous < index < 36,
            "ordered literal source coordinate",
        )
        result[index] = rational(text)
        need(result[index] != 0, "sparse zero omitted")
        previous = index
    return result


def matrix(raw, n):
    need(type(raw) is list and len(raw) == n, "matrix row count")
    need(all(type(row) is list and len(row) == n for row in raw), "matrix column count")
    return [[rational(x) for x in row] for row in raw]


def product(a, b):
    n = len(a)
    return [
        [sum((a[i][k] * b[k][j] for k in range(n)), F()) for j in range(n)]
        for i in range(n)
    ]


def display_interval(value):
    need(type(value) is F and value >= 0, "nonnegative exact diagnostic")
    low = value.numerator * 10**6 // value.denominator
    return [str(F(low, 10**6)), str(F(low + 1, 10**6))]


def audit_panel(panel, selection):
    need(
        type(panel["horizon"]) is int and panel["horizon"] in (900, 2**20),
        "only the two declared horizons",
    )
    indices = selection["coordinate_indices"]
    need(type(indices) is list and len(indices) == 20, "twenty frozen coordinates")
    need(
        all(type(i) is int and 0 <= i < 36 for i in indices)
        and len(set(indices)) == 20,
        "literal distinct coordinates",
    )
    need(
        type(panel["rows"]) is list and len(panel["rows"]) == 20, "twenty physical rows"
    )
    source_matrix, tail_matrix, counts = [], [], []
    for number, row in enumerate(panel["rows"]):
        equal(row["ratio"], selection["ratios"][number])
        totals, prefix, previous = [F()] * 36, [F()] * 20, 0
        for alias in row["complete_aliases"]:
            g = alias["g"]
            need(
                type(g) is int and previous < g <= row["maximum_alias"],
                "literal ordered alias",
            )
            previous = g
            actual = sparse36(alias["source_curvature"])
            majorant = [rational(x) for x in alias["majorant_coordinates"]]
            need(
                len(majorant) == 20
                and all(
                    abs(actual[c]) <= x for c, x in zip(indices, majorant, strict=True)
                ),
                "actual source majorant",
            )
            totals = [x + y / g for x, y in zip(totals, actual, strict=True)]
            prefix = [x + y / g for x, y in zip(prefix, majorant, strict=True)]
        equal(
            [str(x) for x in totals],
            [str(x) for x in sparse36(row["all36_source_coordinates"])],
        )
        equal([str(x) for x in prefix], row["positive_prefix"])
        upper = [rational(x) for x in row["infinite_majorant_upper"]]
        need(len(upper) == 20, "complete infinite majorant row")
        tails = [x - y for x, y in zip(upper, prefix, strict=True)]
        need(all(x >= 0 for x in tails), "same-majorant nonnegative tail")
        equal([str(x) for x in tails], row["tail"])
        source_matrix.append([totals[c] for c in indices])
        tail_matrix.append(tails)
        counts.append(len(row["complete_aliases"]))
    equal([[str(x) for x in row] for row in source_matrix], panel["matrix"])
    equal([[str(x) for x in row] for row in tail_matrix], panel["tail"])
    contraction = panel["contraction"]
    need(type(contraction["inverse"]) is dict, "both observed source minors invertible")
    inverse = matrix(contraction["inverse"]["matrix"], 20)
    identity = [[F(i == j) for j in range(20)] for i in range(20)]
    need(
        product(source_matrix, inverse) == identity
        and product(inverse, source_matrix) == identity,
        "independent two-sided inverse",
    )
    bounds = product([[abs(x) for x in row] for row in inverse], tail_matrix)
    sums = [sum(row, F()) for row in bounds]
    theta = max(sums)
    equal(
        [[str(x) for x in row] for row in bounds],
        contraction["absolute_inverse_times_tail"],
    )
    equal([str(x) for x in sums], contraction["row_sums"])
    equal(str(theta), contraction["theta"])
    need(
        theta >= 1 and contraction["status"] == "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        "retain the actual inconclusive contraction outcome",
    )
    need(
        contraction["all_future_horizons_certified"] is False
        and panel["every_later_partial_prefix_bounded"] is True,
        "majorant theorem is not a successful contraction",
    )
    return {
        "horizon": panel["horizon"],
        "mathematical_status": contraction["status"],
        "exact_minor_rank": 20,
        "theta": str(theta),
        "theta_outward_interval": display_interval(theta),
        "complete_alias_count_per_row": counts,
        "all_future_horizons_certified": False,
    }


def audit_pair(calibration, heldout):
    need(
        calibration["phase"] == "calibration" and heldout["phase"] == "heldout",
        "distinct original phases",
    )
    need(
        calibration["result"]["horizon"] == 900
        and heldout["result"]["horizon"] == 2**20,
        "unchanged held-out horizon",
    )
    equal(calibration["selection"], heldout["selection"])
    for payload in (calibration, heldout):
        need(
            all(value is False for value in payload["scope"].values()),
            "no stronger outcome inferred",
        )
    return [
        audit_panel(payload["result"], payload["selection"])
        for payload in (calibration, heldout)
    ]


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def build():
    scout, calibration, heldout, provenance = source()
    fresh_calibration = scout.build("calibration")
    equal(fresh_calibration, calibration)
    fresh_heldout = scout.build("heldout", CALIBRATION)
    equal(fresh_heldout, heldout)
    diagnostics = audit_pair(calibration, heldout)
    payload = {
        "schema": "native-physical-tail-two-outcome-certificate-v1",
        "owned_sha256_lf": owned_bindings(),
        "source_provenance": provenance,
        "execution_status": "PASS",
        "mathematical_status": "UNKNOWN_TAIL_NOT_CONTRACTIVE_AT_BOTH_DECLARED_HORIZONS",
        "diagnostics": diagnostics,
        "complete_acquisitions": {"calibration": calibration, "heldout": heldout},
        "scope": {
            "rank20_at_isolated_heldout_2pow20": True,
            "all_future_horizons_certified": False,
            "intervening_gap_filled": False,
            "rank_counterexample_found": False,
            "minor_or_bound_adapted_after_heldout": False,
            "old18_test_contract_replaced": False,
        },
    }
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    need(
        len(canonical(payload).encode()) <= MAX_BYTES,
        "final retained artifact byte cap",
    )
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    need(args.write != args.check, "exactly one artifact mode")
    payload = build()
    if args.write:
        FIXTURE.write_text(canonical(payload) + "\n", encoding="utf-8")
    else:
        candidate = read_json(FIXTURE.read_bytes())
        body_check(candidate)
        equal(candidate, payload)
    print(
        canonical(
            {
                "execution_status": "PASS",
                "mathematical_status": payload["mathematical_status"],
                "diagnostics": [
                    {
                        key: row[key]
                        for key in (
                            "horizon",
                            "exact_minor_rank",
                            "theta_outward_interval",
                            "all_future_horizons_certified",
                        )
                    }
                    for row in payload["diagnostics"]
                ],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
