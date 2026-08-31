"""A separately registered, streamed extension of the fixed-minor tail test."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import product
from math import isqrt
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
OLD_CALIBRATION = "3ba479241acf9db1554af067d5e2bea85533dde5"
OLD_HELDOUT = "179d4c78a81cbe9eb7214c2b5a9eca041d197c46"
CALIBRATION_HORIZON = 2**20
EXTENSION_HORIZON = 2**48
MAX_ALIAS = 2**24
MAX_ALIASES = 4400
MAX_BYTES = 32 * 1024 * 1024
OUTPUT_BYTES = 16 * 1024 * 1024
DOMAIN = b"native-physical-tail-extension-alias-v1\n"
PINS = (
    (
        "proof",
        OLD_CALIBRATION,
        PREFIX + "NATIVE_PHYSICAL_MINOR_TAIL_CONTRACTION.md",
        "82c61f5e4a83da0bc0a96140bb483c02a06c3a4c",
    ),
    (
        "prior_declaration",
        OLD_CALIBRATION,
        PREFIX + "NATIVE_PHYSICAL_TAIL_PREREGISTRATION.md",
        "cdadf991c63898a26b804f53cd91ac5cd8e00a95",
    ),
    (
        "helper",
        OLD_CALIBRATION,
        PREFIX + "native_physical_tail_scout.py",
        "24ef243220c8159f78505717d639d88287fbf439",
    ),
    (
        "prior_tests",
        OLD_CALIBRATION,
        "tests/test_native_six_hour_physical_tail.py",
        "d69120d4b26290b6d356cba4c6e347b8b47cc43f",
    ),
    (
        "old_calibration",
        OLD_CALIBRATION,
        PREFIX + "native_physical_tail.calibration.json",
        "e4306d1ae72043efa7f80d9d7c8b9183f5d46ac8",
    ),
    (
        "old_heldout",
        OLD_HELDOUT,
        PREFIX + "native_physical_tail.heldout.json",
        "382a0268b4f31948239b98333a34277fe6cef8b6",
    ),
    (
        "filtration",
        "2952d7c0c9fd0fbbbf04fa6321cc2ff4bb392c8a",
        PREFIX + "SOURCE_CURVATURE_HORIZON_FILTRATION.md",
        "e6489149479e68ee20bd042c4f03bab58e3e48bf",
    ),
)
OWNED = (
    Path(__file__),
    HERE / "NATIVE_PHYSICAL_TAIL_EXTENSION_PREREGISTRATION.md",
    HERE / "NATIVE_PHYSICAL_TAIL_EXTENSION_REPLAY.md",
    ROOT / "tests/test_native_six_hour_physical_tail_extension.py",
)


class Refusal(ValueError):
    """An acceptance or arithmetic refusal, not a mathematical UNKNOWN."""


def need(condition, message):
    if not condition:
        raise Refusal(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal bounded integer")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(actual, expected):
    need(canonical(actual) == canonical(expected), "complete typed replay differs")


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def no_float(_value):
    raise Refusal("floating or nonfinite JSON")


def read_json(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded JSON bytes")
    return json.loads(
        raw, parse_float=no_float, parse_constant=no_float, object_pairs_hook=unique
    )


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


def rational(value):
    need(type(value) is str and 0 < len(value) <= 2500, "canonical rational string")
    result = F(value)
    need(
        str(result) == value
        and max(abs(result.numerator).bit_length(), result.denominator.bit_length())
        <= 4096,
        "canonical bounded rational",
    )
    return result


def git_bytes(commit, path, expected=None, compare_current=True):
    need(
        type(commit) is str
        and len(commit) == 40
        and all(c in "0123456789abcdef" for c in commit),
        "exact commit",
    )
    blob = subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
    ).strip()
    if expected is not None:
        need(blob == expected, "frozen source identity")
    size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
    need(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
    need(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "actual Git bytes",
    )
    if compare_current:
        need(
            raw.replace(b"\r\n", b"\n")
            == (ROOT / path).read_bytes().replace(b"\r\n", b"\n"),
            "frozen file differs from current LF bytes",
        )
    return raw, {"commit": commit, "path": path, "blob": blob}


def owned_bindings():
    return {
        p.relative_to(ROOT).as_posix(): sha256(
            p.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for p in OWNED
    }


def authenticate(calibration_commit=None):
    raw, provenance = {}, []
    for label, commit, path, expected in PINS:
        raw[label], identity = git_bytes(commit, path, expected)
        provenance.append(identity)
    gate_provenance = []
    if calibration_commit is not None:
        for p in OWNED:
            relative = p.relative_to(ROOT).as_posix()
            _data, identity = git_bytes(calibration_commit, relative)
            gate_provenance.append(identity)
        raw["new_calibration"], identity = git_bytes(
            calibration_commit,
            PREFIX + "native_physical_tail_extension.calibration.json",
        )
        gate_provenance.append(identity)
    return raw, provenance, gate_provenance


def source(calibration_commit=None):
    raw, provenance, gate_provenance = authenticate(calibration_commit)
    # All direct old/new blobs are authenticated before either compile or JSON parse.
    original_path = ROOT / (PREFIX + "native_physical_tail_scout.py")
    namespace = {
        "__name__": "frozen_tail_extension_helpers",
        "__file__": str(original_path),
    }
    exec(compile(raw["helper"], str(original_path), "exec"), namespace)  # noqa: S102
    helper = SimpleNamespace(**namespace)
    old_calibration = read_json(raw["old_calibration"])
    old_heldout = read_json(raw["old_heldout"])
    for capture, phase, horizon in (
        (old_calibration, "calibration", 900),
        (old_heldout, "heldout", CALIBRATION_HORIZON),
    ):
        body_check(capture)
        need(
            capture["schema"] == "native-fixed-physical-minor-future-tail-v1"
            and capture["phase"] == phase,
            "fixed prior campaign identity",
        )
        integer(capture["result"]["horizon"], horizon, horizon)
        need(
            capture["result"]["contraction"]["status"] == "UNKNOWN_TAIL_NOT_CONTRACTIVE"
            and capture["result"]["contraction"]["all_future_horizons_certified"]
            is False,
            "both previous UNKNOWN outcomes retained",
        )
    equal(old_calibration["selection"], old_heldout["selection"])
    gate = None
    if calibration_commit is not None:
        gate = read_json(raw["new_calibration"])
        body_check(gate)
        need(
            gate["schema"] == "native-physical-tail-extension-v1"
            and gate["phase"] == "calibration",
            "accepted new calibration identity",
        )
        equal(gate["owned_sha256_lf"], owned_bindings())
    # This authenticates the unchanged helper's complete frozen minor source chain.
    minor = helper.frozen_minor()
    selection = helper.encoded(
        {k: minor[k] for k in ("ratios", "coordinate_indices", "row_indices")}
    )
    equal(selection, old_heldout["selection"])
    return (
        helper,
        minor,
        old_calibration,
        old_heldout,
        gate,
        provenance,
        gate_provenance,
    )


def exponents(number):
    integer(number, 1, MAX_ALIAS)
    rest, result = number, []
    for prime, cap in ((2, 24), (3, 15), (5, 10)):
        power = 0
        while rest % prime == 0:
            rest //= prime
            power += 1
        integer(power, 0, cap)
        result.append(power)
    need(rest == 1, "three-prime supported alias or ratio")
    return tuple(result)


def validate_aliases(values, maximum):
    integer(maximum, 1, MAX_ALIAS)
    need(
        type(values) is list and 0 < len(values) <= MAX_ALIASES,
        "bounded complete alias list",
    )
    previous = 0
    for g in values:
        integer(g, 1, maximum)
        need(g > previous, "strictly increasing unique aliases")
        exponents(g)
        previous = g
    return values


def supported_aliases(maximum):
    integer(maximum, 1, MAX_ALIAS)
    powers = []
    for prime in (2, 3, 5):
        values, number = [], 1
        while number <= maximum:
            values.append(number)
            number *= prime
        powers.append(values)
    need(
        len(powers[0]) <= 25 and len(powers[1]) <= 16 and len(powers[2]) <= 11,
        "registered complete exponent box",
    )
    values = sorted(a * b * c for a, b, c in product(*powers) if a * b * c <= maximum)
    return validate_aliases(values, maximum)


def stream_start(ratio):
    need(type(ratio) in (tuple, list) and len(ratio) == 2, "stream ratio")
    for n in ratio:
        integer(n, 1, 900)
    return sha256(DOMAIN + canonical(list(ratio)).encode() + b"\n")


def stream_record(digest, encoded_record):
    need(type(encoded_record) is dict, "complete encoded alias record")
    digest.update(canonical(encoded_record).encode() + b"\n")


def compact_prior(result):
    """A typed projection of the complete captured alias records, not a recomputation."""
    rows = []
    for row in result["rows"]:
        digest = stream_start(row["ratio"])
        aliases = row["complete_aliases"]
        indices = [item["g"] for item in aliases]
        validate_aliases(indices, row["maximum_alias"])
        for item in aliases:
            stream_record(digest, item)
        rows.append(
            {
                **{k: v for k, v in row.items() if k != "complete_aliases"},
                "alias_indices": indices,
                "alias_count": len(indices),
                "source_majorant_sha256": digest.hexdigest(),
            }
        )
    return {**result, "rows": rows}


def panel(helper, minor, horizon, prior=None):
    integer(horizon, 1, EXTENSION_HORIZON)
    need(
        horizon in (CALIBRATION_HORIZON, EXTENSION_HORIZON),
        "only two registered horizons",
    )
    if prior is not None:
        need(horizon == CALIBRATION_HORIZON, "prior result only for calibration")
        integer(prior["horizon"], horizon, horizon)
    indices = minor["coordinate_indices"]
    need(len(indices) == 20 and len(set(indices)) == 20, "fixed twenty coordinates")
    for c in indices:
        integer(c, 0, 35)
    need(len(minor["ratios"]) == 20, "fixed twenty ratios")
    matrix, tails, rows, tables = [], [], [], {}
    processed = 0
    for number, (a, b) in enumerate(minor["ratios"]):
        alpha, beta = exponents(a), exponents(b)
        need(max(alpha + beta) <= 9, "unchanged local shifts")
        maximum = isqrt(horizon // (a * b))
        aliases = supported_aliases(maximum)
        source_total, prefix = [F()] * 36, [F()] * 20
        digest = stream_start((a, b))
        old_row = None if prior is None else prior["rows"][number]
        if old_row is not None:
            equal(old_row["ratio"], [a, b])
            equal([entry["g"] for entry in old_row["complete_aliases"]], aliases)
        for position, g in enumerate(aliases):
            ks = exponents(g)
            need(max(ks) <= 24, "new alias uses old local helper within original cap")
            values = [
                helper.local(k, x, y) for k, x, y in zip(ks, alpha, beta, strict=True)
            ]
            source_values = [
                helper.source_coordinate(values, c) for c in helper.COORDINATES
            ]
            majorant = [
                helper.source_coordinate(values, helper.COORDINATES[c], True)
                for c in indices
            ]
            need(
                all(
                    abs(source_values[c]) <= bound
                    for c, bound in zip(indices, majorant, strict=True)
                ),
                "own positive source majorant",
            )
            record = helper.encoded(
                {
                    "g": g,
                    "source_curvature": helper.sparse(source_values),
                    "majorant_coordinates": majorant,
                }
            )
            if old_row is not None:
                equal(record, old_row["complete_aliases"][position])
            stream_record(digest, record)
            for i, value in enumerate(source_values):
                source_total[i] = helper.exact(source_total[i] + value / g)
            for i, value in enumerate(majorant):
                prefix[i] = helper.exact(prefix[i] + value / g)
            processed += 1
            need(processed <= 20 * MAX_ALIASES, "total streamed alias cap")
        total = [
            helper.total_majorant(alpha, beta, helper.COORDINATES[c], tables)
            for c in indices
        ]
        tail = [
            helper.exact(upper - known)
            for upper, known in zip(total, prefix, strict=True)
        ]
        need(all(value >= 0 for value in tail), "same-majorant prefix subtraction")
        matrix.append([source_total[c] for c in indices])
        tails.append(tail)
        rows.append(
            {
                "ratio": (a, b),
                "maximum_alias": maximum,
                "alias_indices": aliases,
                "alias_count": len(aliases),
                "source_majorant_sha256": digest.hexdigest(),
                "all36_source_coordinates": helper.sparse(source_total),
                "positive_prefix": prefix,
                "infinite_majorant_upper": total,
                "tail": tail,
            }
        )
    result = helper.encoded(
        {
            "horizon": horizon,
            "rows": rows,
            "matrix": matrix,
            "tail": tails,
            "local_tables": [tables[key] for key in sorted(tables)],
            "contraction": helper.contraction(matrix, tails),
            "every_later_partial_prefix_bounded": True,
        }
    )
    if prior is not None:
        equal(result, compact_prior(prior))
    return result


def scope(result):
    inverse = result["contraction"]["inverse"]
    success = result["contraction"]["all_future_horizons_certified"]
    need(type(success) is bool, "literal future certificate flag")
    status = result["contraction"]["status"]
    if inverse is None:
        need(
            status == "UNKNOWN_SINGULAR_MINOR"
            and not success
            and result["contraction"]["theta"] is None,
            "singular outcome consistency",
        )
    else:
        theta = rational(result["contraction"]["theta"])
        need(
            theta >= 0
            and success == (theta < 1)
            and status == ("PASS" if success else "UNKNOWN_TAIL_NOT_CONTRACTIVE"),
            "strict exact outcome consistency",
        )
    return {
        "same_frozen_minor_and_local_cutoff": True,
        "old_900_status": "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        "old_2pow20_status": "UNKNOWN_TAIL_NOT_CONTRACTIVE",
        "current_minor_rank20_certified": inverse is not None,
        "all_integer_horizons_at_or_above_target_certified": success,
        "effective_sufficient_threshold": result["horizon"] if success else None,
        "first_faithful_horizon_claimed": False,
        "gap_901_to_extension_minus1_bridged": False,
        "all_integer_horizons_rank20_claimed": False,
        "new_energy_minimum_claimed": False,
        "native_gamma_decoder_claimed": False,
        "all_prime_completion_claimed": False,
    }


def build(phase, calibration_commit=None):
    need(
        type(phase) is str and phase in ("calibration", "extension"), "registered phase"
    )
    need(
        (phase == "extension") == (calibration_commit is not None),
        "freeze required only for the extension phase",
    )
    helper, minor, old_cal, old_later, gate, provenance, gate_provenance = source(
        calibration_commit
    )
    selection = helper.encoded(
        {k: minor[k] for k in ("ratios", "coordinate_indices", "row_indices")}
    )
    calibration_result = panel(helper, minor, CALIBRATION_HORIZON, old_later["result"])
    if gate is not None:
        equal(selection, gate["selection"])
        equal(calibration_result, gate["result"])
    result = (
        calibration_result
        if phase == "calibration"
        else panel(helper, minor, EXTENSION_HORIZON)
    )
    payload = {
        "schema": "native-physical-tail-extension-v1",
        "phase": phase,
        "execution_status": "PASS",
        "source": provenance,
        "minor_source": minor["provenance"],
        "new_calibration_freeze": gate_provenance,
        "old_campaign_proof_objects": {
            "900": old_cal["proof_object_sha256"],
            "2pow20": old_later["proof_object_sha256"],
        },
        "owned_sha256_lf": owned_bindings(),
        "selection": selection,
        "calibration_result": calibration_result,
        "result": result,
        "scope": scope(result),
    }
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    need(len(canonical(payload).encode()) <= OUTPUT_BYTES, "retained artifact cap")
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase", choices=("calibration", "extension"), required=True)
    parser.add_argument("--calibration-commit")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build(args.phase, args.calibration_commit)
    target = HERE / f"native_physical_tail_extension.{args.phase}.json"
    if args.write:
        target.write_text(canonical(payload) + "\n", encoding="utf-8")
    else:
        equal(payload, read_json(target.read_bytes()))
    result = payload["result"]
    print(
        canonical(
            {
                "phase": args.phase,
                "execution_status": "PASS",
                "horizon": result["horizon"],
                "mathematical_status": result["contraction"]["status"],
                "effective_threshold": payload["scope"][
                    "effective_sufficient_threshold"
                ],
                "theta": result["contraction"]["theta"],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
