"""Durable full stage-five maps with exact, cheaper completeness certificates."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from collections import defaultdict
from math import isqrt
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
FREEZE = "b1c48ff9f09ec521a7f33b2ecbf81f661e8145cd"
PINS = {
    "full_resolution_replay.py": "421fd58e65c529b93b0d3bb781f135c3bd3b090a",
    "TERNARY_CUBE_FULL_RESOLUTION_PREREGISTRATION.md": "5e6f37cd49df1b0f18664638828953b6bb01f55c",
    "full_resolution_stage5.discovery.json": "4c9f58cc8383855504b333852d677756c271163c",
}
PENDING = HERE / "resolution_stage5.pending.json"
CACHE = HERE / "resolution_stage5.cache.json"
OWNED = (
    HERE / "RESOLUTION_STAGE5_CACHE_PREREGISTRATION.md",
    Path(__file__),
    ROOT / "tests/test_segre_hadamard_stage5_cache.py",
)
MAX_BYTES = 64 * 1024 * 1024
MODULI = (65521, 1000003)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "literal integer outside cap")
    return value


def json_tree(value):
    if type(value) in (type(None), bool, int, float, str):
        return True
    if type(value) is list:
        return all(json_tree(item) for item in value)
    if type(value) is dict:
        return all(type(key) is str and json_tree(item) for key, item in value.items())
    return False


def canonical(value):
    need(json_tree(value), "literal JSON tree required")
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def normalized(value):
    # The frozen mathematical producer uses tuples for marked weights/bases.
    return json.loads(json.dumps(value, sort_keys=True, allow_nan=False))


def equal(left, right, message):
    need(canonical(normalized(left)) == canonical(normalized(right)), message)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def owned_bindings():
    result = {}
    for path in OWNED:
        data = path.read_bytes()
        need(len(data) <= MAX_BYTES, "owned byte cap")
        result[path.relative_to(ROOT).as_posix()] = hashlib.sha256(
            data.replace(b"\r\n", b"\n")
        ).hexdigest()
    return result


def authenticate():
    raw, provenance = {}, {}
    for name, expected in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen stage-five algorithm/source mismatch")
        data = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(data) <= MAX_BYTES, "source byte cap")
        raw[name] = data
        provenance[name] = {
            "blob": expected,
            "sha256_lf": hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest(),
        }
    return raw, provenance


def source():
    raw, provenance = authenticate()
    name = "full_resolution_replay.py"
    namespace = {
        "__name__": "authenticated_stage5_cache_source",
        "__file__": str(HERE / name),
    }
    exec(compile(raw[name], str(HERE / name), "exec"), namespace)  # noqa: S102
    module = SimpleNamespace(**namespace)
    return module, json.loads(raw["full_resolution_stage5.discovery.json"]), provenance


def is_prime(value):
    integer(value, 2, 1000003)
    return all(value % divisor for divisor in range(2, isqrt(value) + 1))


def modular_rank(columns, modulus):
    need(
        modulus in MODULI and type(modulus) is int and is_prime(modulus),
        "fixed prime rank certificate",
    )
    need(len(columns) <= 512, "modular column block cap")
    support = set().union(*(set(column) for column in columns)) if columns else set()
    need(len(support) <= 512, "modular row block cap")
    pivots, selected = {}, []
    for index, column in enumerate(columns):
        need(
            all(
                type(row) is int and row >= 0 and type(value) is int
                for row, value in column.items()
            ),
            "literal integer matrix required",
        )
        vector = {
            row: value % modulus for row, value in column.items() if value % modulus
        }
        while vector:
            row = min(vector)
            if row not in pivots:
                inverse = pow(vector[row], modulus - 2, modulus)
                pivots[row] = {
                    key: value * inverse % modulus for key, value in vector.items()
                }
                selected.append(index)
                break
            scalar = vector[row]
            for key, value in pivots[row].items():
                new = (vector.get(key, 0) - scalar * value) % modulus
                if new:
                    vector[key] = new
                else:
                    vector.pop(key, None)
    return {
        "modulus": modulus,
        "rank": len(pivots),
        "pivot_rows_in_insertion_order": list(pivots),
        "independent_local_column_indices": selected,
    }


def parse_vector(raw, size, helper):
    need(type(raw) is list and bool(raw), "nonempty original-coordinate kernel vector")
    vector, previous = {}, -1
    for entry in raw:
        need(type(entry) is list and len(entry) == 2, "sparse coordinate pair")
        row = integer(entry[0], 0, size - 1)
        value = entry[1]
        need(
            row > previous and type(value) is int and value != 0,
            "ordered literal nonzero sparse entries",
        )
        vector[row], previous = value, row
    helper.check_bits(vector)
    need(
        helper.primitive_integer(vector) == vector,
        "primitive positive integer kernel normalization",
    )
    return vector


def certify_kernel(upstream, helper, evaluation, record):
    upstream.preflight(evaluation)
    expected_header = {
        "grade": evaluation["grade"],
        "full_target_rows": len(evaluation["target_basis"]),
        "domain_columns": len(evaluation["domain_basis"]),
        "basis_order": "generator order, then lexicographic weak compositions in ten W variables",
        "target_basis_sha256": upstream.digest_rows(evaluation["target_basis"]),
        "domain_basis_sha256": upstream.digest_rows(evaluation["domain_basis"]),
        "sparse_matrix_columns_sha256": upstream.digest_rows(
            upstream.sparse(column) for column in evaluation["columns"]
        ),
        "complete_column_weights": evaluation["weights"],
    }
    equal(
        {key: record[key] for key in expected_header},
        expected_header,
        "complete cached matrix/basis descriptors changed",
    )
    raw_vectors = record["full_original_coordinate_kernel_basis"]
    need(type(raw_vectors) is list, "complete cached kernel list")
    relations, weights, largest_coordinates = [], [], set()
    by_weight = defaultdict(list)
    for raw in raw_vectors:
        vector = parse_vector(raw, len(evaluation["domain_basis"]), helper)
        need(
            not helper.image_of_relation(evaluation["columns"], vector),
            "cached kernel has nonzero actual composition",
        )
        weight = tuple(evaluation["weights"][next(iter(vector))])
        need(
            all(tuple(evaluation["weights"][i]) == weight for i in vector),
            "cached vector not weight homogeneous",
        )
        largest = max(vector)
        need(
            largest not in largest_coordinates,
            "triangular kernel independence witness duplicated",
        )
        largest_coordinates.add(largest)
        by_weight[weight].append(vector)
        relations.append(vector)
        weights.append(weight)
    need(type(record["weight_blocks"]) is list, "cached weight block list")
    for row in record["weight_blocks"]:
        need(
            type(row) is dict
            and type(row.get("weight")) is list
            and len(row["weight"]) == 3
            and all(type(value) is int and value >= 0 for value in row["weight"]),
            "literal integer cached block weight",
        )
    block_records = {tuple(row["weight"]): row for row in record["weight_blocks"]}
    blocks = upstream.blocks(evaluation["weights"])
    need(
        set(block_records) == set(blocks)
        and len(block_records) == len(record["weight_blocks"]),
        "complete unique cached block coverage",
    )
    certificates = []
    total_rank = 0
    for weight, indices in blocks.items():
        columns = [evaluation["columns"][i] for i in indices]
        row_count = len(set().union(*(set(column) for column in columns)))
        nullity = len(by_weight.get(weight, []))
        target_rank = len(indices) - nullity
        old = block_records[weight]
        equal(
            {key: old[key] for key in ("rows", "columns", "rank", "nullity")},
            {
                "rows": row_count,
                "columns": len(indices),
                "rank": target_rank,
                "nullity": nullity,
            },
            "cached block dimensions not certified by actual witnesses",
        )
        attempts = []
        for modulus in MODULI:
            certificate = modular_rank(columns, modulus)
            certificate["independent_original_column_indices"] = [
                indices[i] for i in certificate["independent_local_column_indices"]
            ]
            attempts.append(certificate)
            need(
                certificate["rank"] <= target_rank,
                "modular rank contradicts certified rational kernel",
            )
            if certificate["rank"] == target_rank:
                break
        need(
            attempts[-1]["rank"] == target_rank,
            "declared primes did not certify full rational rank; no unregistered fallback",
        )
        certificates.append(
            {
                "weight": list(weight),
                "rational_rank": target_rank,
                "independent_integer_kernel_dimension": nullity,
                "kernel_largest_coordinates": sorted(
                    max(v) for v in by_weight.get(weight, [])
                ),
                "finite_field_attempts": attempts,
            }
        )
        total_rank += target_rank
    equal(
        {"rank": record["rank"], "nullity": record["nullity"]},
        {"rank": total_rank, "nullity": len(relations)},
        "full actual rank/nullity",
    )
    return (
        relations,
        weights,
        {
            "grade": evaluation["grade"],
            "rank": total_rank,
            "nullity": len(relations),
            "all_integer_compositions_zero": True,
            "independence_by_distinct_largest_coordinates": True,
            "complete_weight_rank_certificates": certificates,
        },
    )


def verify_maps(upstream, maps, frozen_summary):
    helper, presentation, acquisition, provenance = upstream.source()
    equal(
        maps["F0_generators"], presentation["generators"], "cached primitive F0 changed"
    )
    equal(maps["D1_columns"], presentation["D1_columns"], "cached primitive D1 changed")
    equal(
        maps["source_bindings"], provenance, "cached predecessor authentication changed"
    )
    equal(
        {
            key: maps[key]
            for key in (
                "source_freeze",
                "stage",
                "all_old_and_new_compositions_zero",
                "complete_resolution_constructed",
                "marked_basis_is_GL3_equivariant",
                "independent_global_exactness_proof_required",
            )
        },
        {
            "source_freeze": upstream.FREEZE,
            "stage": 5,
            "all_old_and_new_compositions_zero": True,
            "complete_resolution_constructed": False,
            "marked_basis_is_GL3_equivariant": False,
            "independent_global_exactness_proof_required": True,
        },
        "stage-five source scope",
    )
    equal(
        upstream.summary(maps),
        frozen_summary["summary"],
        "frozen successful stage-five summary changed",
    )
    need(len(maps["stages"]) == 3, "exact stage-five matrix coverage")
    f0, d1, d2, d3 = (
        maps["F0_generators"],
        maps["D1_columns"],
        maps["D2_columns"],
        maps["D3_columns"],
    )
    need(len(d2) == 85 and len(d3) == 11, "complete cached polynomial maps")
    certificates, checks = [], {}
    evaluation4 = helper.evaluated_map(f0, d1, 4)
    stage4 = maps["stages"][0]
    need(stage4["map"] == "D1", "degree-four source map")
    relations4, weights4, certificate4 = certify_kernel(
        upstream, helper, evaluation4, stage4["evaluation"]
    )
    actual_d2_low = helper.differential_columns(evaluation4, relations4, weights4)
    equal(actual_d2_low, d2[:65], "cached D2 degree-four entries changed")
    need(
        hashlib.sha256(upstream.canonical(actual_d2_low).encode()).hexdigest()
        == acquisition["D2_degree_four_columns_sha256"],
        "original degree-four acquisition digest",
    )
    checks["D2_degree4"] = upstream.weight_check(actual_d2_low, d1, 3)
    certificates.append(certificate4)
    del evaluation4, relations4, weights4
    evaluation5 = helper.evaluated_map(f0, d1, 5)
    stage5 = maps["stages"][1]
    need(stage5["map"] == "D1", "degree-five first map")
    relations5, weights5, certificate5 = certify_kernel(
        upstream, helper, evaluation5, stage5["evaluation"]
    )
    selected, selected_weights, old, old_rank = upstream.select_quotient(
        helper, evaluation5, relations5, weights5, actual_d2_low, d1
    )
    equal(
        upstream.quotient_record(old, old_rank, selected),
        stage5["minimal_quotient"],
        "actual cached old-span/minimal quotient witness changed",
    )
    need(
        (len(old["columns"]), old_rank, len(selected)) == (650, 639, 20),
        "actual lower multiples and new quotient",
    )
    d2_high = helper.differential_columns(evaluation5, selected, selected_weights)
    equal(d2_high, d2[65:], "cached D2 degree-five entries changed")
    checks["D2_degree5"] = upstream.weight_check(d2_high, d1, 2)
    certificates.append(certificate5)
    del evaluation5, relations5, weights5, selected, selected_weights, old
    evaluation_d2 = helper.evaluated_map(d1, d2, 5)
    stage_d2 = maps["stages"][2]
    need(
        stage_d2["map"] == "D2" and stage_d2["minimal_quotient"] is None,
        "initial third-map minimal cover",
    )
    relations_d2, weights_d2, certificate_d2 = certify_kernel(
        upstream, helper, evaluation_d2, stage_d2["evaluation"]
    )
    actual_d3 = helper.differential_columns(evaluation_d2, relations_d2, weights_d2)
    equal(actual_d3, d3, "cached actual degree-five third map changed")
    checks["D3_degree5"] = upstream.weight_check(actual_d3, f0, 2)
    equal(
        checks, maps["complete_Tor_weight_checks"], "all cached Tor weight characters"
    )
    equal(
        checks,
        frozen_summary["complete_Tor_weight_checks"],
        "frozen stage-five Tor checks",
    )
    certificates.append(certificate_d2)
    return normalized(
        {
            "all_three_actual_matrices_reconstructed": True,
            "all_cached_maps_reconstructed_from_certified_kernels": True,
            "old_multiple_rank": old_rank,
            "new_degree5_D2_classes": len(d2_high),
            "weight_rank_certificates": certificates,
            "complete_Tor_weight_checks": checks,
            "rational_D1_kernel_elimination_repeated": False,
        }
    )


def atomic_write(path, payload):
    data = (
        json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n"
    ).encode()
    need(len(data) <= MAX_BYTES, "cache artifact byte cap")
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def acquire():
    upstream, frozen_summary, provenance = source()
    maps = normalized(upstream.build_maps(5))
    equal(
        upstream.summary(maps),
        frozen_summary["summary"],
        "acquisition reproduces exact frozen successful summary",
    )
    payload = {
        "schema": "ternary-stage5-durable-acquisition-v1",
        "algorithm_freeze": FREEZE,
        "algorithm_bindings": provenance,
        "owned_sha256_lf": owned_bindings(),
        "maps": maps,
        "certified_for_continuation": False,
    }
    payload["proof_object_sha256"] = digest(payload)
    atomic_write(PENDING, payload)
    return payload


def verify_candidate(candidate):
    need(
        type(candidate) is dict
        and set(candidate)
        == {
            "schema",
            "algorithm_freeze",
            "algorithm_bindings",
            "owned_sha256_lf",
            "maps",
            "certified_for_continuation",
            "proof_object_sha256",
        },
        "exact acquisition schema keys",
    )
    need(
        candidate["schema"] == "ternary-stage5-durable-acquisition-v1"
        and candidate["algorithm_freeze"] == FREEZE
        and candidate["certified_for_continuation"] is False,
        "unmodified acquisition source/scope",
    )
    body = {
        key: value for key, value in candidate.items() if key != "proof_object_sha256"
    }
    need(digest(body) == candidate["proof_object_sha256"], "acquisition body digest")
    equal(
        candidate["owned_sha256_lf"],
        owned_bindings(),
        "acquisition verifier/contract bytes changed",
    )
    upstream, frozen_summary, provenance = source()
    equal(
        candidate["algorithm_bindings"],
        provenance,
        "acquisition frozen algorithm bindings",
    )
    return verify_maps(upstream, candidate["maps"], frozen_summary)


def read_json(path):
    need(path.stat().st_size <= MAX_BYTES, "cache input byte cap")
    return json.loads(path.read_bytes())


def certify_pending():
    candidate = read_json(PENDING)
    verification = verify_candidate(candidate)
    payload = {
        "schema": "ternary-stage5-certified-cache-v1",
        "candidate": candidate,
        "verification": verification,
        "requires_exact_frozen_blob_before_continuation": True,
    }
    payload["proof_object_sha256"] = digest(payload)
    atomic_write(CACHE, payload)
    return payload


def verify_cache(payload):
    need(
        type(payload) is dict
        and set(payload)
        == {
            "schema",
            "candidate",
            "verification",
            "requires_exact_frozen_blob_before_continuation",
            "proof_object_sha256",
        },
        "exact certified-cache keys",
    )
    need(
        payload["schema"] == "ternary-stage5-certified-cache-v1"
        and payload["requires_exact_frozen_blob_before_continuation"] is True,
        "certified cache scope",
    )
    need(
        digest(
            {
                key: value
                for key, value in payload.items()
                if key != "proof_object_sha256"
            }
        )
        == payload["proof_object_sha256"],
        "certified cache body digest",
    )
    actual = verify_candidate(payload["candidate"])
    equal(
        actual, payload["verification"], "all cached completeness certificates replayed"
    )
    return actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--acquire", action="store_true")
    mode.add_argument("--verify-pending", action="store_true")
    mode.add_argument("--check-cache", action="store_true")
    args = parser.parse_args()
    if args.acquire:
        payload = acquire()
        status = {
            "status": "ACQUIRED_NOT_CERTIFIED",
            "path": str(PENDING),
            "proof_object_sha256": payload["proof_object_sha256"],
        }
    elif args.verify_pending:
        payload = certify_pending()
        status = {
            "status": "CERTIFIED_AWAITING_ROOT_FREEZE",
            "path": str(CACHE),
            "proof_object_sha256": payload["proof_object_sha256"],
        }
    else:
        payload = read_json(CACHE)
        verify_cache(payload)
        status = {
            "status": "CACHE_WITNESSES_PASS",
            "proof_object_sha256": payload["proof_object_sha256"],
        }
    print(json.dumps(status, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
