"""Complete Chow kernels certified after selecting original matrix rows."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from itertools import zip_longest
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
CACHE_FREEZE = "742d68b6d3c37191589b0e6463bc122af6d90f76"
CACHE_PINS = {
    PREFIX
    + "RESOLUTION_STAGE5_CACHE_PREREGISTRATION.md": "b3f9807415543a780ea18db2f07b2293c9a0aa3a",
    PREFIX + "resolution_stage5_cache.py": "fb7420f12e667d73b8f51bc3ed3ff3150be372ba",
    PREFIX + "resolution_stage5.cache.json": "3f1689a7388de3b4cf3f33e3cc7057d51a94118b",
    "tests/test_segre_hadamard_stage5_cache.py": "7506e6b226360f81a85e662e2f0c9ec2e67a50a3",
}
MODULI = (65521, 1000003)
MAX_ROWS = 4096
MAX_COLUMNS = 512
MAX_BYTES = 64 * 1024 * 1024
DIRECTORY = HERE / "row_restricted_weightblocks"
FIXTURE = HERE / "row_restricted_resolution.verification.json"
PREREG = HERE / "ROW_RESTRICTED_RESOLUTION_PREREGISTRATION.md"
OWNED = (
    PREREG,
    HERE / "TERNARY_CUBE_FULL_RESOLUTION.md",
    HERE / "ROW_RESTRICTED_RESOLUTION_REPLAY.md",
    Path(__file__),
    ROOT / "tests/test_segre_hadamard_row_restricted_resolution.py",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal integer outside cap")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def normalized(value):
    return json.loads(canonical(value))


def digest(value):
    result = hashlib.sha256()
    size = 0
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    for chunk in encoder.iterencode(value):
        raw = chunk.encode()
        size += len(raw)
        need(size < MAX_BYTES, "canonical object byte cap")
        result.update(raw)
    return result.hexdigest()


def check_payload(candidate, expected):
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    missing = object()
    for left, right in zip_longest(
        encoder.iterencode(candidate), encoder.iterencode(expected), fillvalue=missing
    ):
        need(left == right, "typed complete row-restriction replay differs")


def no_float(_value):
    raise ValueError("floating or nonfinite JSON")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "bounded JSON source")
    return json.loads(
        raw,
        parse_float=no_float,
        parse_constant=no_float,
        object_pairs_hook=unique_object,
    )


def authenticate():
    need(
        type(CACHE_FREEZE) is str
        and len(CACHE_FREEZE) == 40
        and all(c in "0123456789abcdef" for c in CACHE_FREEZE),
        "exact freeze required before source access",
    )
    need(
        all(
            type(value) is str
            and len(value) == 40
            and all(c in "0123456789abcdef" for c in value)
            for value in CACHE_PINS.values()
        ),
        "exact frozen blob identities required",
    )
    raw, provenance = {}, {}
    for path, expected in CACHE_PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{CACHE_FREEZE}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "certified cache source mismatch")
        size = int(
            subprocess.check_output(
                ["git", "cat-file", "-s", actual], cwd=ROOT, text=True
            )
        )
        need(0 < size <= MAX_BYTES, "frozen source byte cap")
        data = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        current = (ROOT / path).read_bytes()
        need(len(data) == size and len(current) <= MAX_BYTES, "source length")
        need(
            current.replace(b"\r\n", b"\n") == data.replace(b"\r\n", b"\n"),
            "current certified source changed",
        )
        raw[path] = data
        provenance[path] = {
            "blob": actual,
            "sha256_lf": hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest(),
        }
    return raw, provenance


def load_frozen():
    raw, provenance = authenticate()
    path = PREFIX + "resolution_stage5_cache.py"
    namespace = {
        "__name__": "authenticated_row_restriction_cache",
        "__file__": str(ROOT / path),
    }
    exec(compile(raw[path], str(ROOT / path), "exec"), namespace)  # noqa: S102
    return (
        SimpleNamespace(**namespace),
        read_json(raw[PREFIX + "resolution_stage5.cache.json"]),
        provenance,
    )


def verified_source():
    verifier, cache, provenance = load_frozen()
    verification = verifier.verify_cache(cache)
    upstream, _, _ = verifier.source()
    helper, presentation, acquisition, _ = upstream.source()
    maps = cache["candidate"]["maps"]
    need(
        type(maps["stage"]) is int
        and maps["stage"] == 5
        and maps["complete_resolution_constructed"] is False,
        "complete stage-five input only",
    )
    return SimpleNamespace(
        verifier=verifier,
        upstream=upstream,
        helper=helper,
        presentation=presentation,
        acquisition=acquisition,
        maps=maps,
        cache_provenance={
            "freeze": CACHE_FREEZE,
            "bindings": provenance,
            "proof_object_sha256": cache["proof_object_sha256"],
            "fresh_verification_sha256": digest(verification),
            "all_cached_witnesses_reverified": True,
            "expensive_stage5_rational_kernel_recomputed": False,
        },
    )


def source_ownership(context):
    return {
        "cache_provenance": context.cache_provenance,
        "algorithm_sha256_lf": hashlib.sha256(
            Path(__file__).read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "preregistration_sha256_lf": hashlib.sha256(
            PREREG.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "moduli": list(MODULI),
        "full_rows_per_weight": MAX_ROWS,
        "columns_per_weight": MAX_COLUMNS,
    }


def preflight_full(upstream, evaluation):
    need(
        len(evaluation["target_basis"]) <= 90000
        and len(evaluation["domain_basis"]) <= 16000,
        "unchanged full basis caps",
    )
    need(
        len(evaluation["columns"])
        == len(evaluation["weights"])
        == len(evaluation["domain_basis"]),
        "complete matrix column metadata",
    )
    need(
        all(
            type(weight) in (tuple, list)
            and len(weight) == 3
            and all(type(value) is int and 0 <= value <= 21 for value in weight)
            for weight in evaluation["weights"]
        ),
        "literal source weights before grouping",
    )
    profiles = []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        need(
            len(weight) == 3
            and all(type(value) is int and 0 <= value <= 21 for value in weight),
            "literal source weight",
        )
        columns = [evaluation["columns"][i] for i in indices]
        support = (
            set().union(*(set(column) for column in columns)) if columns else set()
        )
        need(
            len(indices) <= MAX_COLUMNS and len(support) <= MAX_ROWS,
            "new full weight-block cap",
        )
        for column in columns:
            need(
                all(
                    type(row) is int
                    and 0 <= row < len(evaluation["target_basis"])
                    and type(value) is int
                    and value != 0
                    for row, value in column.items()
                ),
                "literal full original integer matrix",
            )
        profiles.append(
            {"weight": list(weight), "rows": len(support), "columns": len(indices)}
        )
    return profiles


def select_original_rows(columns, modulus):
    need(type(modulus) is int and modulus in MODULI, "fixed row-selection modulus")
    need(1 <= len(columns) <= MAX_COLUMNS, "row-selection column cap")
    support = sorted(set().union(*(set(column) for column in columns)))
    need(len(support) <= MAX_ROWS, "streamed row cap")
    need(
        all(
            type(row) is int and row >= 0 and type(value) is int
            for column in columns
            for row, value in column.items()
        ),
        "literal integer row selection input",
    )
    pivots, selected = {}, []
    for row in support:
        vector = {
            i: column[row] % modulus
            for i, column in enumerate(columns)
            if row in column and column[row] % modulus
        }
        while vector:
            leading = min(vector)
            if leading not in pivots:
                inverse = pow(vector[leading], modulus - 2, modulus)
                pivots[leading] = {
                    i: value * inverse % modulus for i, value in vector.items()
                }
                selected.append(row)
                break
            scalar = vector[leading]
            for i, value in pivots[leading].items():
                result = (vector.get(i, 0) - scalar * value) % modulus
                if result:
                    vector[i] = result
                else:
                    vector.pop(i, None)
    return {
        "modulus": modulus,
        "selected_original_rows": selected,
        "pivot_local_column_indices": list(pivots),
        "modular_row_rank": len(selected),
    }


def restricted_columns(columns, selected):
    need(
        type(selected) is list
        and all(type(row) is int and row >= 0 for row in selected)
        and selected == sorted(set(selected)),
        "ordered literal selected original rows",
    )
    retained = set(selected)
    return [
        {row: value for row, value in column.items() if row in retained}
        for column in columns
    ]


def certify_attempt(verifier, helper, columns, weight, attempt):
    need(
        type(attempt) is dict
        and set(attempt)
        == {
            "row_selection",
            "restricted_kernel",
            "restricted_statistics",
            "certificate",
        },
        "complete row-selection attempt",
    )
    selection = attempt["row_selection"]
    need(
        type(selection) is dict and type(selection.get("modulus")) is int,
        "literal row-selection metadata",
    )
    expected = select_original_rows(columns, selection["modulus"])
    check_payload(selection, expected)
    restricted = restricted_columns(columns, expected["selected_original_rows"])
    rank = expected["modular_row_rank"]
    modular = verifier.modular_rank(restricted, expected["modulus"])
    need(modular["rank"] == rank, "independent selected-row modular rank")
    vectors = [
        verifier.parse_vector(raw, len(columns), helper)
        for raw in attempt["restricted_kernel"]
    ]
    need(len(vectors) == len(columns) - rank, "complete restricted kernel dimension")
    peaks = [max(vector) for vector in vectors]
    need(len(set(peaks)) == len(peaks), "restricted kernel triangular independence")
    need(
        all(not helper.image_of_relation(restricted, vector) for vector in vectors),
        "actual restricted kernel compositions",
    )
    stat = attempt["restricted_statistics"]
    need(
        type(stat) is dict
        and set(stat)
        == {"weight", "rows", "columns", "rank", "nullity", "max_exact_bits"},
        "original restricted kernel statistics",
    )
    check_payload(
        {key: stat[key] for key in ("weight", "rows", "columns", "rank", "nullity")},
        {
            "weight": list(weight),
            "rows": rank,
            "columns": len(columns),
            "rank": rank,
            "nullity": len(vectors),
        },
    )
    integer(stat["max_exact_bits"], 0, 4096)
    failures = []
    for i, vector in enumerate(vectors):
        residual = helper.image_of_relation(columns, vector)
        helper.check_bits(residual)
        if residual:
            failures.append(
                {
                    "kernel_vector": i,
                    "full_original_residual": [
                        [row, value] for row, value in sorted(residual.items())
                    ],
                }
            )
    certificate = {
        "selected_modular_rank_certificate": modular,
        "kernel_dimension": len(vectors),
        "largest_local_kernel_coordinates": peaks,
        "verified_kernel_coefficient_bits": max(
            (helper.check_bits(vector) for vector in vectors), default=0
        ),
        "every_full_original_row_checked": True,
        "full_composition_failures": failures,
        "full_and_restricted_kernels_equal": not failures,
    }
    return vectors, certificate


def fresh_attempt(context, columns, weight, grade, modulus):
    selection = select_original_rows(columns, modulus)
    restricted = restricted_columns(columns, selection["selected_original_rows"])
    evaluation = {
        "grade": grade,
        "columns": restricted,
        "weights": [weight] * len(columns),
    }
    vectors, weights, stats = context.upstream.kernel(context.helper, evaluation)
    need(
        weights == [weight] * len(vectors) and len(stats) == 1,
        "unchanged exact one-weight kernel",
    )
    attempt = {
        "row_selection": selection,
        "restricted_kernel": [context.upstream.sparse(vector) for vector in vectors],
        "restricted_statistics": normalized(stats[0]),
        "certificate": None,
    }
    vectors, certificate = certify_attempt(
        context.verifier, context.helper, columns, weight, attempt
    )
    attempt["certificate"] = certificate
    return attempt, vectors


def checkpoint_input(upstream, evaluation, matrix, weight, indices, ownership):
    return {
        "ownership": ownership,
        "matrix": matrix,
        "grade": evaluation["grade"],
        "weight": list(weight),
        "original_column_indices": indices,
        "complete_block_columns_sha256": upstream.digest_rows(
            upstream.sparse(evaluation["columns"][i]) for i in indices
        ),
    }


def verify_checkpoint(payload, expected_input, context, columns, weight):
    need(
        type(payload) is dict
        and set(payload)
        == {"schema", "status", "input", "attempts", "proof_object_sha256"},
        "complete certified checkpoint schema",
    )
    need(
        payload["schema"] == "certified-original-row-kernel-v1"
        and payload["status"] == "FULL_KERNEL_CERTIFIED",
        "only completed full kernels are reusable",
    )
    check_payload(payload["input"], expected_input)
    need(
        payload["proof_object_sha256"]
        == digest(
            {
                key: value
                for key, value in payload.items()
                if key != "proof_object_sha256"
            }
        ),
        "checkpoint body digest",
    )
    attempts = payload["attempts"]
    need(
        type(attempts) is list and 1 <= len(attempts) <= 2,
        "fixed fallback attempt count",
    )
    vectors = None
    for i, attempt in enumerate(attempts):
        need(
            attempt["row_selection"]["modulus"] == MODULI[i],
            "fixed modulus order with no hidden fallback",
        )
        vectors, certificate = certify_attempt(
            context.verifier, context.helper, columns, weight, attempt
        )
        check_payload(attempt["certificate"], certificate)
        need(
            certificate["full_and_restricted_kernels_equal"]
            is (i == len(attempts) - 1),
            "all failed attempts retained before one success",
        )
    return vectors


def write_atomic(path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    size = 0
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    with temporary.open("wb") as output:
        for text in encoder.iterencode(payload):
            raw = text.encode()
            size += len(raw)
            need(size <= MAX_BYTES, "atomic object byte cap")
            output.write(raw)
        need(size + 1 <= MAX_BYTES, "atomic object byte cap")
        output.write(b"\n")
        output.flush()
        os.fsync(output.fileno())
    os.replace(temporary, path)


def certified_kernel(context, evaluation, directory=DIRECTORY):
    upstream, helper = context.upstream, context.helper
    preflight_full(upstream, evaluation)
    for column in evaluation["columns"]:
        helper.check_bits(column)
    matrix = {
        "grade": evaluation["grade"],
        "full_target_rows": len(evaluation["target_basis"]),
        "domain_columns": len(evaluation["domain_basis"]),
        "target_basis_sha256": upstream.digest_rows(evaluation["target_basis"]),
        "domain_basis_sha256": upstream.digest_rows(evaluation["domain_basis"]),
        "complete_weights_sha256": upstream.digest_rows(evaluation["weights"]),
        "full_original_matrix_sha256": upstream.digest_rows(
            upstream.sparse(column) for column in evaluation["columns"]
        ),
    }
    ownership = source_ownership(context)
    relations, weights, stats, certificates = [], [], [], []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        columns = [evaluation["columns"][i] for i in indices]
        expected_input = checkpoint_input(
            upstream, evaluation, matrix, weight, indices, ownership
        )
        path = Path(directory) / (digest(expected_input) + ".json")
        if path.is_file():
            need(path.stat().st_size <= MAX_BYTES, "completed checkpoint byte cap")
            payload = read_json(path.read_bytes())
            vectors = verify_checkpoint(
                payload, expected_input, context, columns, weight
            )
        else:
            attempts, vectors = [], None
            for modulus in MODULI:
                attempt, vectors = fresh_attempt(
                    context, columns, weight, evaluation["grade"], modulus
                )
                attempts.append(attempt)
                if attempt["certificate"]["full_and_restricted_kernels_equal"]:
                    break
            if not attempts[-1]["certificate"]["full_and_restricted_kernels_equal"]:
                failure = {
                    "schema": "certified-original-row-kernel-v1",
                    "status": "FIXED_MODULI_FAILED",
                    "input": expected_input,
                    "attempts": attempts,
                }
                failure["proof_object_sha256"] = digest(failure)
                write_atomic(path.with_suffix(".failure.json"), failure)
                raise ValueError(
                    "both fixed row-selection moduli failed; full residuals retained"
                )
            payload = {
                "schema": "certified-original-row-kernel-v1",
                "status": "FULL_KERNEL_CERTIFIED",
                "input": expected_input,
                "attempts": attempts,
            }
            payload["proof_object_sha256"] = digest(payload)
            write_atomic(path, payload)
        accepted = payload["attempts"][-1]
        translated = [
            {indices[i]: value for i, value in vector.items()} for vector in vectors
        ]
        need(
            all(
                not helper.image_of_relation(evaluation["columns"], vector)
                for vector in translated
            ),
            "full global original-coordinate compositions",
        )
        relations.extend(translated)
        weights.extend([weight] * len(vectors))
        support = set().union(*(set(column) for column in columns))
        stats.append(
            {
                "weight": weight,
                "rows": len(support),
                "columns": len(indices),
                "rank": accepted["row_selection"]["modular_row_rank"],
                "nullity": len(vectors),
                "max_exact_bits": max(
                    accepted["restricted_statistics"]["max_exact_bits"],
                    accepted["certificate"]["verified_kernel_coefficient_bits"],
                ),
                "selected_original_rows": len(
                    accepted["row_selection"]["selected_original_rows"]
                ),
                "successful_modulus": accepted["row_selection"]["modulus"],
                "every_full_original_row_checked": True,
            }
        )
        certificates.append(payload)
    return relations, weights, stats, certificates


def extend_maps(context, stage, directory=DIRECTORY):
    integer(stage, 6, 7)
    upstream, helper, maps = context.upstream, context.helper, context.maps
    need(
        maps["stage"] == 5
        and (len(maps["D2_columns"]), len(maps["D3_columns"])) == (85, 11),
        "complete certified stage-five maps",
    )
    d1, d2, d3 = maps["D1_columns"], maps["D2_columns"], maps["D3_columns"]
    for degree in range(6, stage + 1):
        evaluation = helper.evaluated_map(d1, d2, degree)
        relations, weights, stats, certificates = certified_kernel(
            context, evaluation, directory
        )
        need(
            (len(evaluation["domain_basis"]), len(relations))
            == {6: (3775, 127), 7: (15400, 776)}[degree],
            "actual complete higher-kernel prediction",
        )
        chosen, chosen_weights, old, old_rank = upstream.select_quotient(
            helper, evaluation, relations, weights, d3, d2
        )
        need(
            (len(old["columns"]), old_rank, len(chosen))
            == {6: (110, 110, 17), 7: (775, 775, 1)}[degree],
            "unchanged exact old/new minimal quotient prediction",
        )
        added = helper.differential_columns(evaluation, chosen, chosen_weights)
        maps["complete_Tor_weight_checks"][f"D3_degree{degree}"] = (
            upstream.weight_check(added, maps["F0_generators"], 7 - degree)
        )
        d3.extend(added)
        maps["stages"].append(
            {
                "map": "D2",
                "evaluation": upstream.evaluation_record(evaluation, stats, relations),
                "minimal_quotient": upstream.quotient_record(old, old_rank, chosen),
                "complete_row_restriction_certificates": certificates,
            }
        )
        del evaluation, relations, weights, chosen, chosen_weights, old, certificates
    maps["stage"] = stage
    maps["complete_resolution_constructed"] = stage == 7
    maps["all_old_and_new_compositions_zero"] = True
    return maps


def build_maps(stage=7, directory=DIRECTORY):
    integer(stage, 6, 7)
    context = verified_source()
    maps = extend_maps(context, stage, directory)
    return maps, context.cache_provenance, context.upstream.summary(maps)


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def build(stage=7, directory=DIRECTORY):
    maps, provenance, summary = build_maps(stage, directory)
    payload = {
        "schema": "actual-ternary-Chow-certified-original-row-resolution-v1",
        "owned_sha256_lf": owned_bindings(),
        "cache_provenance": provenance,
        "summary": summary,
        "result": maps,
        "row_restriction_contract": {
            "prior_898_row_preflight_succeeded": False,
            "full_rows_cap": MAX_ROWS,
            "columns_cap": MAX_COLUMNS,
            "every_original_row_verified": True,
            "fixed_moduli": list(MODULI),
            "old_26_test_contract_replaced": False,
        },
    }
    payload["proof_object_sha256"] = digest(payload)
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scout", type=int, choices=(6, 7))
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stage = args.scout if args.scout is not None else 7
    payload = build(stage)
    if args.scout is not None:
        # Root captures the complete maps; successful stdout is not a final fixture.
        json.dump(
            payload, sys.stdout, sort_keys=True, separators=(",", ":"), allow_nan=False
        )
        sys.stdout.write("\n")
        return
    if args.write:
        write_atomic(FIXTURE, payload)
    else:
        need(FIXTURE.stat().st_size <= MAX_BYTES, "final fixture byte cap")
        check_payload(read_json(FIXTURE.read_bytes()), payload)
    print(
        canonical(
            {
                "status": "PASS",
                "summary": payload["summary"],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
