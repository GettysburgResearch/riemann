"""Compose bounded, fully grouped event certificates for one fixed physical minor."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction as F
from hashlib import sha1, sha256
from itertools import groupby
from math import isqrt
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PREFIX = "research/riemann-structures/native-six-hour/"
MODULI = (65521, 1000003)
MAX_BYTES = 32 * 1024 * 1024
OUTPUT_BYTES = 16 * 1024 * 1024
MAX_HORIZON = 2**48
PINS = (
    (
        "utilities",
        "63e1742ec319c532baa36f6568809f6a6b32e6e2",
        PREFIX + "native_physical_tail_extension.py",
        "bb69109f81bca6e814a87c82be86ac7b92934d27",
    ),
    (
        "helper",
        "3ba479241acf9db1554af067d5e2bea85533dde5",
        PREFIX + "native_physical_tail_scout.py",
        "24ef243220c8159f78505717d639d88287fbf439",
    ),
    (
        "base",
        "3ba479241acf9db1554af067d5e2bea85533dde5",
        PREFIX + "native_physical_tail.calibration.json",
        "e4306d1ae72043efa7f80d9d7c8b9183f5d46ac8",
    ),
    (
        "theorem",
        "3ba479241acf9db1554af067d5e2bea85533dde5",
        PREFIX + "NATIVE_PHYSICAL_MINOR_TAIL_CONTRACTION.md",
        "82c61f5e4a83da0bc0a96140bb483c02a06c3a4c",
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
    HERE / "NATIVE_EVENT_MINOR_PREREGISTRATION.md",
    HERE / "NATIVE_EVENT_MINOR_REPLAY.md",
    ROOT / "tests/test_native_six_hour_event_minor.py",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal bounded integer")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def equal(left, right):
    need(
        canonical(left) == canonical(right), "complete typed event certificate differs"
    )


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def no_float(_value):
    raise ValueError("floating or nonfinite JSON")


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
    equal(sha256(canonical(body).encode()).hexdigest(), payload["proof_object_sha256"])


def frozen(commit, path, expected=None):
    need(
        type(commit) is str
        and len(commit) == 40
        and all(c in "0123456789abcdef" for c in commit),
        "exact frozen commit",
    )
    blob = subprocess.check_output(
        ["git", "rev-parse", f"{commit}:{path}"], cwd=ROOT, text=True
    ).strip()
    if expected is not None:
        need(blob == expected, "frozen event source identity")
    size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
    need(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
    need(
        len(raw) == size
        and sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest() == blob,
        "actual Git bytes",
    )
    need(
        raw.replace(b"\r\n", b"\n")
        == (ROOT / path).read_bytes().replace(b"\r\n", b"\n"),
        "unchanged frozen file",
    )
    return raw, {"commit": commit, "path": path, "blob": blob}


def artifact_name(power):
    if power is None:
        return "native_event_minor.calibration.json"
    integer(power, 10, 48)
    return f"native_event_minor.panel_{power}.json"


def bindings():
    return {
        p.relative_to(ROOT).as_posix(): sha256(
            p.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for p in OWNED
    }


def authenticate(previous_commit=None, previous_power=None):
    raw, provenance = {}, []
    for label, commit, path, blob in PINS:
        raw[label], identity = frozen(commit, path, blob)
        provenance.append(identity)
    predecessor = []
    if previous_commit is not None:
        for p in OWNED:
            _raw, identity = frozen(previous_commit, p.relative_to(ROOT).as_posix())
            predecessor.append(identity)
        raw["previous"], identity = frozen(
            previous_commit, PREFIX + artifact_name(previous_power)
        )
        predecessor.append(identity)
    return raw, provenance, predecessor


def source(previous_commit=None, previous_power=None):
    raw, provenance, predecessor = authenticate(previous_commit, previous_power)
    path = ROOT / (PREFIX + "native_physical_tail_extension.py")
    namespace = {"__name__": "frozen_event_utilities", "__file__": str(path)}
    # Direct sources and any predecessor bytes are all authenticated first.
    exec(compile(raw["utilities"], str(path), "exec"), namespace)  # noqa: S102
    utilities = SimpleNamespace(**namespace)
    helper, minor, base, _old_later, *_ = utilities.source()
    previous = None if previous_commit is None else read_json(raw["previous"])
    if previous is not None:
        body_check(previous)
        equal(previous["owned_sha256_lf"], bindings())
        equal(previous["campaign_source"], provenance)
        need(
            previous["schema"] == "native-event-minor-v1"
            and previous["execution_status"] == "PASS",
            "verified predecessor identity",
        )
        expected_upper = 900 if previous_power is None else 2**previous_power
        integer(previous["upper_horizon"], expected_upper, expected_upper)
        equal(previous["upper_power"], previous_power)
        equal(previous["phase"], "calibration" if previous_power is None else "panel")
        need(
            previous["predecessor_proof_input"]
            in (
                "none_base_reconstructed",
                "verified_frozen_endpoint_not_replayed_here",
            ),
            "explicit predecessor scope",
        )
    return utilities, helper, minor, base, previous, provenance, predecessor


def primality_certificate(prime):
    integer(prime, 3, 1000003)
    residues = [[d, prime % d] for d in range(2, isqrt(prime) + 1)]
    need(all(r for _, r in residues), "declared field modulus must be prime")
    return {
        "modulus": prime,
        "trial_limit": isqrt(prime),
        "all_trial_divisor_residues": residues,
        "prime": True,
    }


def reduce_rational(value, prime):
    need(type(value) in (int, F), "literal exact source rational")
    value = F(value)
    need(
        max(abs(value.numerator).bit_length(), value.denominator.bit_length()) <= 4096,
        "unchanged stored-rational bit cap",
    )
    residue = value.denominator % prime
    need(residue != 0, "actual denominator eligible in declared field")
    return value.numerator * pow(residue, -1, prime) % prime, residue


def validate_state(matrix, prime, size=20):
    need(type(matrix) is list and len(matrix) == size, "state height")
    for row in matrix:
        need(type(row) is list and len(row) == size, "state width")
        for value in row:
            integer(value, 0, prime - 1)
    return matrix


def modular_lu(matrix, prime):
    integer(prime, 3, 1000003)
    n = integer(len(matrix), 1, 20)
    validate_state(matrix, prime, n)
    work = [row.copy() for row in matrix]
    rank, sign, diagonal, steps = 0, 1, 1, []
    for column in range(n):
        pivot = next((i for i in range(rank, n) if work[i][column]), None)
        if pivot is None:
            continue
        original_pivot = pivot
        if pivot != rank:
            work[pivot], work[rank] = work[rank], work[pivot]
            sign = -sign
        value = work[rank][column]
        diagonal = diagonal * value % prime
        inverse = pow(value, -1, prime)
        multipliers = []
        for i in range(rank + 1, n):
            factor = work[i][column] * inverse % prime
            if factor:
                multipliers.append([i, factor])
                for j in range(column, n):
                    work[i][j] = (work[i][j] - factor * work[rank][j]) % prime
        steps.append(
            {
                "column": column,
                "pivot_row_before_swap": original_pivot,
                "pivot_value": value,
                "elimination_multipliers": multipliers,
            }
        )
        rank += 1
    return {
        "modulus": prime,
        "rank": rank,
        "steps": steps,
        "echelon": work,
        "permutation_sign": sign,
        "determinant_mod_p": (sign * diagonal) % prime if rank == n else 0,
    }


def rank_certificate(states):
    attempts = []
    size = len(states[str(MODULI[0])])
    for prime in MODULI:
        witness = modular_lu(states[str(prime)], prime)
        attempts.append(witness)
        if witness["rank"] == size:
            need(witness["determinant_mod_p"] != 0, "nonzero full-rank determinant")
            return {"status": "PASS", "chosen_modulus": prime, "attempts": attempts}
    return {
        "status": "UNKNOWN_MODULAR_RANK",
        "chosen_modulus": None,
        "attempts": attempts,
    }


def is_certified(certificate, size=20):
    need(
        type(certificate) is dict and type(certificate.get("attempts")) is list,
        "complete group rank certificate",
    )
    attempts = certificate["attempts"]
    need(1 <= len(attempts) <= 2, "only declared modulus attempts")
    for index, attempt in enumerate(attempts):
        prime = MODULI[index]
        integer(attempt["modulus"], prime, prime)
        rank = integer(attempt["rank"], 0, size)
        determinant = integer(attempt["determinant_mod_p"], 0, prime - 1)
        validate_state(attempt["echelon"], prime, size)
        need((rank == size) == (determinant != 0), "rank/determinant agreement")
        if index < len(attempts) - 1:
            need(rank < size, "fallback only after primary modular failure")
    success = attempts[-1]["rank"] == size
    need(
        certificate["status"] == ("PASS" if success else "UNKNOWN_MODULAR_RANK"),
        "no UNKNOWN promotion",
    )
    equal(certificate["chosen_modulus"], MODULI[len(attempts) - 1] if success else None)
    need(success or len(attempts) == 2, "both declared primes before UNKNOWN")
    return success


def event_addresses(utilities, ratios, lower, upper):
    integer(lower, 0, MAX_HORIZON)
    integer(upper, 1, MAX_HORIZON)
    need(lower < upper and 0 < len(ratios) <= 20, "bounded event interval")
    result = []
    for row, ratio in enumerate(ratios):
        need(type(ratio) in (list, tuple) and len(ratio) == 2, "source ratio")
        a, b = (integer(x, 1, 900) for x in ratio)
        maximum = isqrt(upper // (a * b))
        if maximum == 0:
            continue
        for g in utilities.supported_aliases(maximum):
            horizon = g * g * a * b
            if horizon > lower:
                result.append([horizon, row, g])
    result.sort()
    need(
        len(result) <= 88000 and len({tuple(x) for x in result}) == len(result),
        "complete bounded unique event addresses",
    )
    return result


def source_update(utilities, helper, minor, row, g):
    integer(row, 0, 19)
    a, b = minor["ratios"][row]
    alpha, beta, ks = (
        utilities.exponents(a),
        utilities.exponents(b),
        utilities.exponents(g),
    )
    values = [helper.local(k, x, y) for k, x, y in zip(ks, alpha, beta, strict=True)]
    full = [helper.source_coordinate(values, c) for c in helper.COORDINATES]
    updates = [helper.exact(full[c] / g) for c in minor["coordinate_indices"]]
    modular, denominators = {}, {}
    for prime in MODULI:
        pairs = [reduce_rational(value, prime) for value in updates]
        modular[str(prime)] = [x for x, _ in pairs]
        denominators[str(prime)] = [d for _, d in pairs]
    return {
        "row": row,
        "ratio": [a, b],
        "g": g,
        "n": g * a,
        "m": g * b,
        "source_curvature": helper.sparse(full),
        "exact_selected_update": [str(x) for x in updates],
        "denominator_residues": denominators,
        "modular_update": modular,
    }


def apply_group(states, updates):
    for update in updates:
        row = update["row"]
        for prime in MODULI:
            values = update["modular_update"][str(prime)]
            need(len(values) == len(states[str(prime)][row]), "complete modular update")
            states[str(prime)][row] = [
                (a + b) % prime
                for a, b in zip(states[str(prime)][row], values, strict=True)
            ]
    # This is called only after the whole simultaneous source group is present.
    return rank_certificate(states)


def merge_intervals(intervals):
    result = []
    for lower, upper in sorted(intervals):
        integer(lower, 1, MAX_HORIZON)
        integer(upper, lower, MAX_HORIZON)
        if result and lower <= result[-1][1] + 1:
            result[-1][1] = max(result[-1][1], upper)
        else:
            result.append([lower, upper])
    return result


def certified_intervals(lower, upper, start_known, events):
    need(type(start_known) is bool, "literal predecessor endpoint rank")
    position, known, intervals = lower + 1, start_known, []
    for event in events:
        horizon = event["horizon"]
        integer(horizon, position, upper)
        if known and position <= horizon - 1:
            intervals.append([position, horizon - 1])
        known = is_certified(event["rank_certificate"])
        position = horizon
    if known and position <= upper:
        intervals.append([position, upper])
    return merge_intervals(intervals), known


def scope_fields():
    return {
        "curvature_variation_dimension": 20,
        "ambient_tensor_dimension": 64,
        "ambient64_faithfulness_threshold_claimed": False,
        "infinite_tail_claimed": False,
        "new_energy_minimum_claimed": False,
        "native_gamma_decoder_claimed": False,
    }


def selection(helper, minor):
    return helper.encoded(
        {k: minor[k] for k in ("ratios", "coordinate_indices", "row_indices")}
    )


def finish(payload):
    payload["proof_object_sha256"] = sha256(canonical(payload).encode()).hexdigest()
    need(len(canonical(payload).encode()) <= OUTPUT_BYTES, "per-artifact byte cap")
    return payload


def calibration():
    utilities, helper, minor, old, _previous, provenance, _pred = source()
    full_rows, matrix, retained = [], [], []
    for row, (a, b) in enumerate(minor["ratios"]):
        full_sum, chosen_sum, terms = [F()] * 36, [F()] * 20, []
        aliases = utilities.supported_aliases(isqrt(900 // (a * b)))
        old_row = old["result"]["rows"][row]
        equal(aliases, [entry["g"] for entry in old_row["complete_aliases"]])
        for position, g in enumerate(aliases):
            record = source_update(utilities, helper, minor, row, g)
            equal(
                record["source_curvature"],
                old_row["complete_aliases"][position]["source_curvature"],
            )
            for i, value in record["source_curvature"]:
                full_sum[i] = helper.exact(full_sum[i] + utilities.rational(value) / g)
            for i, value in enumerate(record["exact_selected_update"]):
                chosen_sum[i] = helper.exact(chosen_sum[i] + utilities.rational(value))
            terms.append(record)
        equal(helper.sparse(full_sum), old_row["all36_source_coordinates"])
        full_rows.append(helper.sparse(full_sum))
        matrix.append(chosen_sum)
        retained.append({"row": row, "aliases": terms})
    equal(helper.encoded(matrix), old["result"]["matrix"])
    inverse = [
        [utilities.rational(x) for x in r]
        for r in old["result"]["contraction"]["inverse"]["matrix"]
    ]
    identity = [[F(int(i == j)) for j in range(20)] for i in range(20)]
    need(
        helper.matrix_product(matrix, inverse) == identity
        and helper.matrix_product(inverse, matrix) == identity,
        "base exact inverse both ways",
    )
    states = {
        str(p): [[reduce_rational(x, p)[0] for x in r] for r in matrix] for p in MODULI
    }
    return finish(
        {
            "schema": "native-event-minor-v1",
            "phase": "calibration",
            "execution_status": "PASS",
            "campaign_source": provenance,
            "owned_sha256_lf": bindings(),
            "selection": selection(helper, minor),
            "fields": [primality_certificate(p) for p in MODULI],
            "upper_power": None,
            "lower_horizon": 900,
            "upper_horizon": 900,
            "predecessor_proof_input": "none_base_reconstructed",
            "predecessor": None,
            "base_exact_matrix": helper.encoded(matrix),
            "base_exact_inverse_both_products": True,
            "base_full36_rows": full_rows,
            "base_source_updates": retained,
            "base_modular_rank": rank_certificate(states),
            "endpoint_states": states,
            "endpoint_rank20_certified": True,
            "prefix_rank20_through_upper": True,
            "certified_integer_intervals": [[900, 900]],
            "scope": scope_fields(),
        }
    )


def panel(power, previous_commit):
    integer(power, 10, 48)
    need(previous_commit is not None, "verified frozen predecessor required")
    previous_power = None if power == 10 else power - 1
    utilities, helper, minor, _base, previous, provenance, pred_provenance = source(
        previous_commit, previous_power
    )
    lower, upper = (900 if power == 10 else 2 ** (power - 1)), 2**power
    equal(selection(helper, minor), previous["selection"])
    states = {
        str(p): [
            r.copy() for r in validate_state(previous["endpoint_states"][str(p)], p)
        ]
        for p in MODULI
    }
    start_states = {k: [r.copy() for r in v] for k, v in states.items()}
    addresses = event_addresses(utilities, minor["ratios"], lower, upper)
    events = []
    for horizon, group in groupby(addresses, key=lambda item: item[0]):
        group_addresses = list(group)
        need(
            len({row for _, row, _ in group_addresses}) == len(group_addresses),
            "one alias per fixed row at a horizon",
        )
        updates = [
            source_update(utilities, helper, minor, row, g)
            for _, row, g in group_addresses
        ]
        need(
            all(update["n"] * update["m"] == horizon for update in updates),
            "actual product-horizon identity",
        )
        certificate = apply_group(states, updates)
        events.append(
            {"horizon": horizon, "updates": updates, "rank_certificate": certificate}
        )
    intervals, endpoint_known = certified_intervals(
        lower, upper, previous["endpoint_rank20_certified"], events
    )
    complete = intervals == [[lower + 1, upper]]
    need(
        type(previous["prefix_rank20_through_upper"]) is bool,
        "literal previous coverage",
    )
    return finish(
        {
            "schema": "native-event-minor-v1",
            "phase": "panel",
            "execution_status": "PASS",
            "campaign_source": provenance,
            "owned_sha256_lf": bindings(),
            "selection": selection(helper, minor),
            "fields": [primality_certificate(p) for p in MODULI],
            "upper_power": power,
            "lower_horizon": lower,
            "upper_horizon": upper,
            "predecessor_proof_input": "verified_frozen_endpoint_not_replayed_here",
            "predecessor": {
                "commit": previous_commit,
                "proof_object_sha256": previous["proof_object_sha256"],
                "source_records": pred_provenance,
            },
            "start_states": start_states,
            "start_rank20_certified": previous["endpoint_rank20_certified"],
            "complete_event_addresses": addresses,
            "event_count": len(events),
            "update_count": len(addresses),
            "events": events,
            "endpoint_states": states,
            "endpoint_rank20_certified": endpoint_known,
            "certified_integer_intervals": intervals,
            "whole_panel_rank20_certified": complete,
            "prefix_rank20_through_upper": previous["prefix_rank20_through_upper"]
            and complete,
            "scope": scope_fields(),
        }
    )


def collection(commits):
    need(
        type(commits) is list and 1 <= len(commits) <= 40,
        "consecutive base plus at most39 panels",
    )
    # Collect all immutable records/owned identities before parsing any panel.
    identities = []
    for index, commit in enumerate(commits):
        power = None if index == 0 else index + 9
        for p in OWNED:
            frozen(commit, p.relative_to(ROOT).as_posix())
        raw, identity = frozen(commit, PREFIX + artifact_name(power))
        identities.append(identity)
        del raw
    utilities, helper, minor, old, _prev, provenance, _ = source()
    prior, intervals, rows = None, [], []
    for index, commit in enumerate(commits):
        power = None if index == 0 else index + 9
        raw, identity = frozen(commit, PREFIX + artifact_name(power))
        equal(identity, identities[index])
        record = read_json(raw)
        del raw
        body_check(record)
        need(
            record["schema"] == "native-event-minor-v1"
            and record["execution_status"] == "PASS",
            "accepted frozen component",
        )
        equal(record["owned_sha256_lf"], bindings())
        equal(record["campaign_source"], provenance)
        equal(record["selection"], selection(helper, minor))
        equal(record["fields"], [primality_certificate(p) for p in MODULI])
        if index == 0:
            need(
                record["phase"] == "calibration" and record["upper_power"] is None,
                "base first",
            )
            integer(record["lower_horizon"], 900, 900)
            integer(record["upper_horizon"], 900, 900)
            need(
                record["base_exact_inverse_both_products"] is True,
                "verified exact base",
            )
            equal(record["base_exact_matrix"], old["result"]["matrix"])
            equal(record["certified_integer_intervals"], [[900, 900]])
            need(
                record["endpoint_rank20_certified"] is True
                and record["prefix_rank20_through_upper"] is True,
                "exact base rank",
            )
        else:
            power = index + 9
            lower, upper = (900 if power == 10 else 2 ** (power - 1)), 2**power
            need(record["phase"] == "panel", "panel identity")
            integer(record["upper_power"], power, power)
            integer(record["lower_horizon"], lower, lower)
            integer(record["upper_horizon"], upper, upper)
            equal(record["predecessor"]["commit"], commits[index - 1])
            equal(
                record["predecessor"]["proof_object_sha256"],
                prior["proof_object_sha256"],
            )
            equal(record["start_states"], prior["endpoint_states"])
            equal(record["start_rank20_certified"], prior["endpoint_rank20_certified"])
            expected = event_addresses(utilities, minor["ratios"], lower, upper)
            equal(record["complete_event_addresses"], expected)
            observed = [
                [event["horizon"], update["row"], update["g"]]
                for event in record["events"]
                for update in event["updates"]
            ]
            equal(observed, expected)
            equal(
                [event["horizon"] for event in record["events"]],
                sorted({address[0] for address in expected}),
            )
            integer(record["event_count"], len(record["events"]), len(record["events"]))
            integer(record["update_count"], len(expected), len(expected))
            correct_intervals, last_known = certified_intervals(
                lower, upper, prior["endpoint_rank20_certified"], record["events"]
            )
            equal(record["certified_integer_intervals"], correct_intervals)
            equal(record["endpoint_rank20_certified"], last_known)
            equal(
                record["whole_panel_rank20_certified"],
                correct_intervals == [[lower + 1, upper]],
            )
            equal(
                record["prefix_rank20_through_upper"],
                prior["prefix_rank20_through_upper"]
                and record["whole_panel_rank20_certified"],
            )
        for p in MODULI:
            validate_state(record["endpoint_states"][str(p)], p)
        equal(record["scope"], scope_fields())
        intervals.extend(record["certified_integer_intervals"])
        rows.append(
            {
                "commit": commit,
                "upper_horizon": record["upper_horizon"],
                "proof_object_sha256": record["proof_object_sha256"],
                "prefix_rank20_through_upper": record["prefix_rank20_through_upper"],
            }
        )
        prior = {
            key: record[key]
            for key in (
                "proof_object_sha256",
                "endpoint_states",
                "endpoint_rank20_certified",
                "prefix_rank20_through_upper",
                "upper_horizon",
            )
        }
        del record
    return finish(
        {
            "schema": "native-event-minor-composition-v1",
            "execution_status": "PASS",
            "owned_sha256_lf": bindings(),
            "frozen_components": identities,
            "components": rows,
            "upper_horizon": prior["upper_horizon"],
            "certified_integer_intervals": merge_intervals(intervals),
            "prefix_rank20_through_upper": prior["prefix_rank20_through_upper"],
            "complete_registered_chain_through_2pow48": len(commits) == 40,
            "composition_of_previously_verified_frozen_panels": True,
            "complete_event_census_reconstructed": True,
            "local_source_updates_recomputed_by_collector": False,
            "modular_eliminations_recomputed_by_collector": False,
            "unrun_monolithic_replay_claimed": False,
            "scope": scope_fields(),
        }
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--phase", choices=("calibration", "panel", "collection"), required=True
    )
    parser.add_argument("--upper-power", type=int)
    parser.add_argument("--predecessor-commit")
    parser.add_argument("--chain-commits", nargs="+")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.phase == "calibration":
        need(
            args.upper_power is None
            and args.predecessor_commit is None
            and args.chain_commits is None,
            "calibration arguments",
        )
        payload, name = calibration(), artifact_name(None)
    elif args.phase == "panel":
        need(args.chain_commits is None, "panel arguments")
        payload, name = (
            panel(args.upper_power, args.predecessor_commit),
            artifact_name(args.upper_power),
        )
    else:
        need(
            args.upper_power is None and args.predecessor_commit is None,
            "collector arguments",
        )
        payload, name = (
            collection(args.chain_commits),
            "native_event_minor.collection.json",
        )
    target = HERE / name
    if args.write:
        target.write_text(canonical(payload) + "\n", encoding="utf-8")
    else:
        equal(payload, read_json(target.read_bytes()))
    print(
        canonical(
            {
                "phase": args.phase,
                "execution_status": "PASS",
                "upper_horizon": payload["upper_horizon"],
                "prefix_rank20_through_upper": payload["prefix_rank20_through_upper"],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
