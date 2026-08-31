"""Complete Q-syzygy source and factor character before the actual d2."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
import time
import types
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/five-hour-equivariant-pass/"
D2_FREEZE = "6cacc948f2d5f81e89d0da73cfd1814366af1ae4"
D2_PINS = {
    "ACTUAL_CHANGE_OF_RINGS_D2.md": "4092eea5ebad27027f33ddd1c675a4adaa2443cb",
    "D2_PREREGISTRATION.md": "9b1107bb8bddbd9d379b84cb13abb3d527429974",
    "D2_REPLAY.md": "ca397b8bd2599ca0ef79d6fd20311f0ed19ccb2e",
    "d2.shape.json": "b2e875c816cd77086cf7f1067257b488cdd03af8",
    "d2.verification.json": "2178fb16e88f2015c8c489f9b07b1b5c4938f323",
    "d2_replay.py": "d44b829b54a55b504fa0eacca8a5429e4b001cb2",
    "test_equivariant_pass_d2.py": "693d5f12509edc731335f04417b24e1bafb3cb3d",
}
MAX_BLOCK = 512
MAX_BYTES = 16 * 1024 * 1024
FIXTURE = HERE / "higher_syzygy.verification.json"
SHAPE = HERE / "higher_syzygy.shape.json"
TEST = ROOT / "tests/test_equivariant_pass_higher_syzygy.py"
OWNED = (
    "HIGHER_SYZYGY_PREREGISTRATION.md",
    "HIGHER_SYZYGY_MATHEMATICS.md",
    "HIGHER_SYZYGY_REPLAY.md",
    "higher_syzygy.py",
    "higher_syzygy.shape.json",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def blob_id(raw):
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def frozen(path, expected):
    need(
        type(path) is str and type(expected) is str and len(expected) == 40,
        "frozen pin shape",
    )
    raw = subprocess.check_output(["git", "show", f"{D2_FREEZE}:{path}"], cwd=ROOT)
    need(
        len(raw) <= MAX_BYTES and blob_id(raw) == expected, "frozen d2 source mismatch"
    )
    return raw


def load_input():
    # Authenticate every immediate dependency before compile or JSON parse.
    raw = {
        name: frozen(("tests/" if name.startswith("test_") else PREFIX) + name, blob)
        for name, blob in D2_PINS.items()
    }
    d = types.ModuleType("authenticated_actual_d2")
    d.__file__ = str(HERE / "d2_replay.py")
    exec(compile(raw["d2_replay.py"], d.__file__, "exec"), d.__dict__)  # noqa: S102 -- authenticated frozen definitions
    actual = d.strict_json(raw["d2.verification.json"])
    d.check_record(actual, actual)
    need(
        actual["status"] == "VERIFIED_SURJECTIVE_D2" and actual["global_d2_rank"] == 65,
        "accepted actual d2 source",
    )
    data = d.load_input()
    # Restore full quotient reducers and prove that they use the exact
    # representatives on which the frozen Q-action matrices are expressed.
    for grade in (2, 3):
        accepted = data.homology[grade]
        quotient = data.q.Homology(data.complexes[grade], 1)
        need(
            data.q.canonical([data.q.encode_vector(v) for v in quotient.cycles])
            == data.q.canonical([data.q.encode_vector(v) for v in accepted.cycles]),
            "reconstructed homology representatives differ from frozen Q source",
        )
        data.homology[grade] = quotient
    return types.SimpleNamespace(d=d, q=data.q, data=data, actual=actual)


def all_blocks(source):
    d, data = source.d, source.data
    weights = set()
    qw = [weight for weight, _ in data.qb]
    for i, j in itertools.combinations(range(17), 2):
        weights.update(
            d.plus(qw[i], qw[j], weight) for weight in data.homology[2].weights
        )
    weights.update(
        d.plus(qweight, weight) for qweight in qw for weight in data.homology[3].weights
    )
    result = []
    for weight in sorted(weights, reverse=True):
        domain, target, columns = d.q_delta(data, weight)
        need(
            max(len(domain), len(target)) <= MAX_BLOCK,
            "complete Q weight block exceeds512",
        )
        result.append((weight, domain, target, columns))
    return result


def shape(source):
    blocks = all_blocks(source)
    return {
        "schema": "equivariant-pass/higher-syzygy-shape/v1",
        "d2_freeze": D2_FREEZE,
        "weight_count": len(blocks),
        "total_domain": sum(len(domain) for _, domain, _, _ in blocks),
        "total_target": sum(len(target) for _, _, target, _ in blocks),
        "maximum_domain": max(len(domain) for _, domain, _, _ in blocks),
        "maximum_target": max(len(target) for _, _, target, _ in blocks),
        "within_registered_512_cap": all(
            max(len(domain), len(target)) <= MAX_BLOCK
            for _, domain, target, _ in blocks
        ),
        "blocks": [
            {"weight": list(weight), "domain": len(domain), "target": len(target)}
            for weight, domain, target, _ in blocks
        ],
        "rank_calculation_performed": False,
    }


def kernel_basis(q, columns):
    span = q.Span()
    kernels = []
    digest = hashlib.sha256()
    for i, column in enumerate(columns):
        digest.update(canonical(q.encode_vector(column)).encode() + b"\n")
        independent, witness = span.insert(column, {i: Fraction(1)})
        if not independent:
            kernels.append(q.primitive(witness))
    need(span.rank + len(kernels) == len(columns), "complete kernel rank-nullity")
    return span.rank, kernels, digest.hexdigest()


def wedge_action(q, matrix, i, j):
    out = {}
    for a, u in matrix[i].items():
        for b, v in matrix[j].items():
            if a == b:
                continue
            key, sign = ((a, b), 1) if a < b else ((b, a), -1)
            q.add(out, {key: u * v * sign})
    return out


def source_permutation(source, domain, vector, permutation, matrices=None):
    q, data = source.q, source.data
    if matrices is None:
        matrices = (
            q.q_permutation(data.qb, permutation),
            q.homology_permutation(data.homology[2], permutation),
        )
    qm, bm = matrices
    index = {entry: i for i, entry in enumerate(domain)}
    result = {}
    for column, coefficient in vector.items():
        i, j, b = domain[column]
        for (a, c), scalar in wedge_action(q, qm, i, j).items():
            for e, beta in bm[b].items():
                need((a, c, e) in index, "factor action leaves complete weight domain")
                q.add(result, {index[a, c, e]: coefficient * scalar * beta})
    return result


def kernel_trace(source, domain, columns, kernels, permutation, matrices=None):
    q = source.q
    if matrices is None:
        matrices = (
            q.q_permutation(source.data.qb, permutation),
            q.homology_permutation(source.data.homology[2], permutation),
        )
    space = q.Span()
    for i, vector in enumerate(kernels):
        added, _ = space.insert(vector, {i: Fraction(1)})
        need(added, "kernel basis dependence")
    trace = Fraction(0)
    for i, vector in enumerate(kernels):
        moved = source_permutation(source, domain, vector, permutation, matrices)
        need(not q.apply(columns, moved), "factor action does not preserve Q kernel")
        trace += space.coordinates(moved).get(i, 0)
    need(trace.denominator == 1, "nonintegral direct kernel trace")
    return int(trace)


def block_record(source, weight, domain, target, columns, permutation_matrices=None):
    rank, kernels, digest = kernel_basis(source.q, columns)
    traces = [len(kernels)]
    for permutation in ((1, 0, 2), (1, 2, 0)):
        matrices = (
            None if permutation_matrices is None else permutation_matrices[permutation]
        )
        traces.append(
            kernel_trace(source, domain, columns, kernels, permutation, matrices)
        )
    return {
        "weight": list(weight),
        "domain": len(domain),
        "target": len(target),
        "rank": rank,
        "kernel_dimension": len(kernels),
        "matrix_sha256": digest,
        "kernel_factor_class_traces": traces,
        "surjective": rank == len(target),
    }


def build():
    source = load_input()
    shape_record = shape(source)
    need(shape_record["within_registered_512_cap"], "shape cap")
    permutation_matrices = {
        permutation: (
            source.q.q_permutation(source.data.qb, permutation),
            source.q.homology_permutation(source.data.homology[2], permutation),
        )
        for permutation in ((1, 0, 2), (1, 2, 0))
    }
    blocks = [
        block_record(source, *block, permutation_matrices)
        for block in all_blocks(source)
    ]
    domain = sum(row["domain"] for row in blocks)
    target = sum(row["target"] for row in blocks)
    rank = sum(row["rank"] for row in blocks)
    kernel_traces = [
        sum(row["kernel_factor_class_traces"][i] for row in blocks) for i in range(3)
    ]
    surjective = rank == target and all(row["surjective"] for row in blocks)
    expected_source = [2720, 0, -280]
    expected_target = [1105, 25, -245]
    need(
        domain == expected_source[0] and target == expected_target[0],
        "complete global dimensions",
    )
    if surjective:
        need(
            kernel_traces
            == [a - b for a, b in zip(expected_source, expected_target, strict=True)],
            "direct kernel character versus quotient",
        )
    e3 = [a - b for a, b in zip(kernel_traces, [65, -25, 35], strict=True)]
    multiplicities = {
        "trivial": (e3[0] + 3 * e3[1] + 2 * e3[2]) // 6,
        "sign": (e3[0] - 3 * e3[1] + 2 * e3[2]) // 6,
        "standard": (e3[0] - e3[2]) // 3,
    }
    result = {
        "schema": "equivariant-pass/higher-syzygy/v1",
        "d2_freeze": D2_FREEZE,
        "d2_pins": D2_PINS,
        "d2_proof_sha256": source.actual["proof_sha256"],
        "owned_sha256_lf": {
            name: hashlib.sha256(
                (HERE / name).read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for name in OWNED
        },
        "test_sha256_lf": hashlib.sha256(
            TEST.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest(),
        "shape": shape_record,
        "blocks": blocks,
        "global_domain_dimension": domain,
        "global_target_dimension": target,
        "global_rank": rank,
        "global_kernel_factor_class_traces": kernel_traces,
        "surjective": surjective,
        "E3_kernel_factor_class_traces": e3 if surjective else None,
        "E3_factor_multiplicities": multiplicities if surjective else None,
        "filtered_SymQ_formality_obstructed_by_frozen_d2": True,
        "status": "VERIFIED_COMPLETE_Q_SYZYGY"
        if surjective
        else "VERIFIED_NONSURJECTIVE_Q_SYZYGY",
    }
    result["proof_sha256"] = hashlib.sha256(canonical(result).encode()).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "artifact byte cap")
    return result, source.q._peak_working


def strict_json(raw):
    need(type(raw) is bytes and len(raw) <= MAX_BYTES, "JSON byte cap")

    def pairs(items):
        out = {}
        for key, value in items:
            need(key not in out, "duplicate JSON key")
            out[key] = value
        return out

    def forbidden(_):
        raise ValueError("floating/nonfinite JSON")

    return json.loads(
        raw, object_pairs_hook=pairs, parse_float=forbidden, parse_constant=forbidden
    )


def check_record(candidate, expected):
    need(
        type(candidate) is dict and type(candidate.get("proof_sha256")) is str,
        "artifact shape",
    )
    body = dict(candidate)
    proof = body.pop("proof_sha256")
    need(
        hashlib.sha256(canonical(body).encode()).hexdigest() == proof,
        "artifact body digest",
    )
    need(canonical(candidate) == canonical(expected), "typed complete replay mismatch")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--shape", action="store_true")
    modes.add_argument("--write", action="store_true")
    modes.add_argument("--check", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    if args.shape:
        record = shape(load_input())
        SHAPE.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(json.dumps(record))
        return
    record, peak = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(record, sort_keys=True, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )
    else:
        need(FIXTURE.exists(), "missing higher-syzygy artifact")
        check_record(strict_json(FIXTURE.read_bytes()), record)
    print(
        json.dumps(
            {
                "status": record["status"],
                "proof_sha256": record["proof_sha256"],
                "global_rank": record["global_rank"],
                "kernel_traces": record["global_kernel_factor_class_traces"],
                "E3_multiplicities": record["E3_factor_multiplicities"],
                "elapsed_ms": round(1000 * (time.monotonic() - started)),
                "peak_working_bytes": peak,
            }
        )
    )


if __name__ == "__main__":
    main()
