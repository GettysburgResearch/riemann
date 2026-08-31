"""Resume exact stage-five acquisition using certified complete weight blocks."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
FREEZE = "356160f075ee72aed21ee03a6daf30fa3222799a"
PINS = {
    PREFIX
    + "RESOLUTION_STAGE5_CACHE_PREREGISTRATION.md": "b3f9807415543a780ea18db2f07b2293c9a0aa3a",
    PREFIX + "resolution_stage5_cache.py": "fb7420f12e667d73b8f51bc3ed3ff3150be372ba",
    "tests/test_segre_hadamard_stage5_cache.py": "7506e6b226360f81a85e662e2f0c9ec2e67a50a3",
}
OWNED = (
    HERE / "RESOLUTION_BLOCKWISE_PREREGISTRATION.md",
    Path(__file__),
    ROOT / "tests/test_segre_hadamard_blockwise.py",
)
BLOCK_DIRECTORY = HERE / "resolution_stage5.weightblocks"
MANIFEST = HERE / "resolution_stage5_blockwise.discovery.json"
MAX_BYTES = 64 * 1024 * 1024


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def normalized(value):
    return json.loads(canonical(value))


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def equal(left, right, message):
    need(canonical(left) == canonical(right), message)


def no_float(_value):
    raise ValueError("floating or nonfinite checkpoint value")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate checkpoint key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "checkpoint byte cap")
    return json.loads(
        raw,
        parse_float=no_float,
        parse_constant=no_float,
        object_pairs_hook=unique_object,
    )


def authenticate():
    raw, provenance = {}, {}
    for path, expected in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen cache verifier mismatch")
        data = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(data) <= MAX_BYTES, "frozen verifier byte cap")
        current = (ROOT / path).read_bytes()
        need(len(current) <= MAX_BYTES, "current verifier byte cap")
        need(
            current.replace(b"\r\n", b"\n") == data.replace(b"\r\n", b"\n"),
            "current verifier source changed",
        )
        raw[path] = data
        provenance[path] = {
            "blob": actual,
            "sha256_lf": hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest(),
        }
    return raw, provenance


def source():
    raw, provenance = authenticate()
    path = PREFIX + "resolution_stage5_cache.py"
    namespace = {
        "__name__": "authenticated_blockwise_cache_verifier",
        "__file__": str(ROOT / path),
    }
    exec(compile(raw[path], str(ROOT / path), "exec"), namespace)  # noqa: S102
    verifier = SimpleNamespace(**namespace)
    upstream, summary, algorithm_bindings = verifier.source()
    return verifier, upstream, summary, algorithm_bindings, provenance


def owned_bindings():
    result = {}
    for path in OWNED:
        raw = path.read_bytes()
        need(len(raw) <= MAX_BYTES, "owned source byte cap")
        result[path.relative_to(ROOT).as_posix()] = hashlib.sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    return result


def matrix_identity(upstream, evaluation):
    return {
        "grade": evaluation["grade"],
        "target_basis_sha256": upstream.digest_rows(evaluation["target_basis"]),
        "domain_basis_sha256": upstream.digest_rows(evaluation["domain_basis"]),
        "matrix_columns_sha256": upstream.digest_rows(
            upstream.sparse(v) for v in evaluation["columns"]
        ),
        "column_weights_sha256": upstream.digest_rows(evaluation["weights"]),
        "target_rows": len(evaluation["target_basis"]),
        "domain_columns": len(evaluation["domain_basis"]),
    }


def block_input(upstream, evaluation, identity, weight, indices, ownership):
    need(
        type(weight) is tuple
        and len(weight) == 3
        and all(type(x) is int and x >= 0 for x in weight),
        "literal integer block weight",
    )
    need(
        type(indices) is list
        and indices == sorted(set(indices))
        and all(
            type(i) is int and 0 <= i < len(evaluation["columns"]) for i in indices
        ),
        "ordered original block indices",
    )
    return {
        "ownership": ownership,
        "matrix": identity,
        "weight": list(weight),
        "original_column_indices": indices,
        "literal_columns_sha256": upstream.digest_rows(
            upstream.sparse(evaluation["columns"][i]) for i in indices
        ),
    }


def certify_output(verifier, helper, columns, weight, output):
    need(
        type(output) is dict and set(output) == {"local_kernel", "stat"},
        "exact block-output keys",
    )
    need(type(output["local_kernel"]) is list, "complete block kernel list")
    stat = output["stat"]
    need(
        type(stat) is dict
        and set(stat)
        == {"weight", "rows", "columns", "rank", "nullity", "max_exact_bits"},
        "exact block-stat keys",
    )
    equal(stat["weight"], list(weight), "literal block-stat weight")
    need(
        type(stat["max_exact_bits"]) is int and 0 <= stat["max_exact_bits"] <= 4096,
        "diagnostic elimination bit cap",
    )
    vectors = [
        verifier.parse_vector(raw, len(columns), helper)
        for raw in output["local_kernel"]
    ]
    peaks = []
    for vector in vectors:
        need(
            not helper.image_of_relation(columns, vector),
            "block kernel has nonzero actual composition",
        )
        peaks.append(max(vector))
    need(len(set(peaks)) == len(peaks), "block triangular kernel independence")
    nullity = len(vectors)
    rank = len(columns) - nullity
    rows = len(set().union(*(set(column) for column in columns))) if columns else 0
    equal(
        {key: stat[key] for key in ("rows", "columns", "rank", "nullity")},
        {"rows": rows, "columns": len(columns), "rank": rank, "nullity": nullity},
        "block rank must follow independent actual kernel witnesses",
    )
    attempts = []
    for modulus in verifier.MODULI:
        certificate = verifier.modular_rank(columns, modulus)
        attempts.append(certificate)
        need(
            certificate["rank"] <= rank, "block modular rank contradicts actual kernel"
        )
        if certificate["rank"] == rank:
            break
    need(attempts[-1]["rank"] == rank, "fixed primes did not certify complete block")
    return vectors, {
        "rational_rank": rank,
        "kernel_dimension": nullity,
        "largest_local_coordinates": peaks,
        "finite_field_attempts": attempts,
    }


def make_checkpoint(input_record, output, certificate):
    payload = {
        "schema": "ternary-stage5-complete-weight-block-v1",
        "status": "COMPLETE_SOURCE_BLOCK",
        "input": input_record,
        "input_sha256": digest(input_record),
        "output": output,
        "fresh_rank_certificate": certificate,
    }
    payload["proof_object_sha256"] = digest(payload)
    return payload


def check_checkpoint(payload, input_record, verifier, helper, columns, weight):
    need(
        type(payload) is dict
        and set(payload)
        == {
            "schema",
            "status",
            "input",
            "input_sha256",
            "output",
            "fresh_rank_certificate",
            "proof_object_sha256",
        },
        "exact completed-block schema",
    )
    need(
        payload["schema"] == "ternary-stage5-complete-weight-block-v1"
        and payload["status"] == "COMPLETE_SOURCE_BLOCK",
        "only completed blocks are reusable",
    )
    equal(payload["input"], input_record, "checkpoint source/matrix ownership changed")
    need(payload["input_sha256"] == digest(input_record), "checkpoint input digest")
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
    vectors, certificate = certify_output(
        verifier, helper, columns, weight, payload["output"]
    )
    equal(
        payload["fresh_rank_certificate"],
        certificate,
        "checkpoint exact rank certificate changed",
    )
    return vectors, payload["output"]["stat"]


def write_checkpoint(path, payload):
    raw = (
        json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n"
    ).encode()
    need(len(raw) <= MAX_BYTES, "completed block byte cap")
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("wb") as output:
        output.write(raw)
        output.flush()
        os.fsync(output.fileno())
    os.replace(temporary, path)


def blockwise_kernel(
    verifier,
    upstream,
    original_kernel,
    helper,
    evaluation,
    ownership,
    manifest,
    directory,
):
    upstream.preflight(evaluation)
    identity = matrix_identity(upstream, evaluation)
    relations, weights, stats = [], [], []
    for weight, indices in upstream.blocks(evaluation["weights"]).items():
        input_record = block_input(
            upstream, evaluation, identity, weight, indices, ownership
        )
        key = digest(input_record)
        path = directory / (key + ".json")
        columns = [evaluation["columns"][i] for i in indices]
        reused = path.is_file()
        if reused:
            need(path.stat().st_size <= MAX_BYTES, "stored completed block byte cap")
            vectors, stat = check_checkpoint(
                read_json(path.read_bytes()),
                input_record,
                verifier,
                helper,
                columns,
                weight,
            )
        else:
            restricted = {
                "grade": evaluation["grade"],
                "columns": columns,
                "weights": [weight] * len(indices),
            }
            vectors, local_weights, local_stats = original_kernel(helper, restricted)
            need(
                local_weights == [weight] * len(vectors) and len(local_stats) == 1,
                "unchanged one-weight kernel output",
            )
            output = normalized(
                {
                    "local_kernel": [upstream.sparse(vector) for vector in vectors],
                    "stat": local_stats[0],
                }
            )
            vectors, certificate = certify_output(
                verifier, helper, columns, weight, output
            )
            payload = make_checkpoint(input_record, output, certificate)
            write_checkpoint(path, payload)
            stat = output["stat"]
        for vector in vectors:
            translated = {indices[i]: value for i, value in vector.items()}
            need(
                not helper.image_of_relation(evaluation["columns"], translated),
                "translated original-coordinate composition",
            )
            relations.append(translated)
            weights.append(weight)
        stats.append(stat)
        manifest.append(
            {
                "key": key,
                "grade": evaluation["grade"],
                "domain_columns": len(evaluation["domain_basis"]),
                "weight": list(weight),
                "reused": reused,
                "kernel_dimension": len(vectors),
            }
        )
    return relations, weights, stats


def acquire():
    verifier, upstream, summary, algorithm_bindings, provenance = source()
    ownership = {
        "verifier_freeze": FREEZE,
        "verifier_bindings": provenance,
        "algorithm_bindings": algorithm_bindings,
        "fallback_owned_sha256_lf": owned_bindings(),
    }
    directory = BLOCK_DIRECTORY.resolve()
    need(
        directory.parent == HERE.resolve(),
        "checkpoint directory outside assigned source lane",
    )
    directory.mkdir(exist_ok=True)
    manifest = []
    original_kernel = upstream.kernel
    globals_ = upstream.build_maps.__globals__
    need(globals_["kernel"] is original_kernel, "unmodified frozen kernel entry point")

    def checkpointed(helper, evaluation):
        return blockwise_kernel(
            verifier,
            upstream,
            original_kernel,
            helper,
            evaluation,
            ownership,
            manifest,
            directory,
        )

    globals_["kernel"] = checkpointed
    try:
        maps = verifier.normalized(upstream.build_maps(5))
    finally:
        globals_["kernel"] = original_kernel
    verifier.equal(
        upstream.summary(maps),
        summary["summary"],
        "complete blockwise acquisition matches successful frozen summary",
    )
    candidate = {
        "schema": "ternary-stage5-durable-acquisition-v1",
        "algorithm_freeze": verifier.FREEZE,
        "algorithm_bindings": algorithm_bindings,
        "owned_sha256_lf": verifier.owned_bindings(),
        "maps": maps,
        "certified_for_continuation": False,
    }
    candidate["proof_object_sha256"] = verifier.digest(candidate)
    verifier.atomic_write(verifier.PENDING, candidate)
    diagnostic = {
        "schema": "ternary-stage5-blockwise-acquisition-v1",
        "ownership": ownership,
        "complete_blocks": manifest,
        "reused_blocks": sum(row["reused"] for row in manifest),
        "computed_blocks": sum(not row["reused"] for row in manifest),
        "pending_candidate_sha256": candidate["proof_object_sha256"],
        "certified_for_continuation": False,
        "unchanged_final_cache_verification_required": True,
    }
    diagnostic["proof_object_sha256"] = digest(diagnostic)
    verifier.atomic_write(MANIFEST, diagnostic)
    return diagnostic


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--acquire", required=True, action="store_true")
    parser.parse_args()
    result = acquire()
    print(
        canonical(
            {
                "status": "ACQUIRED_NOT_CERTIFIED",
                "complete_blocks": len(result["complete_blocks"]),
                "reused_blocks": result["reused_blocks"],
                "computed_blocks": result["computed_blocks"],
                "pending_candidate_sha256": result["pending_candidate_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
