"""Staged exact higher differentials of the ternary Chow module.

The parent controls execution stages. Frozen polynomial maps are used before
their independently known Tor dimensions are checked, never fitted to them.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
FREEZE = "1a5a63f1148fb884e9ae7aae9e9324a40aee9f33"
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
PINS = {
    "TERNARY_CUBE_RESOLUTION_PREREGISTRATION.md": "54b477ab74eccb925b471a0adeab0500bd61d8ae",
    "resolution_replay.py": "610f50d0e7ef2a47e361ba61a6b4caf53b0fb543",
    "resolution_degree4.discovery.json": "dd9898be35c4898101347e28af6c9206199bf5d8",
}
MAX_BYTES = 64 * 1024 * 1024
MAX_BLOCK = 512
FIXTURE = HERE / "full_resolution.verification.json"
OWNED = (
    HERE / "TERNARY_CUBE_FULL_RESOLUTION_PREREGISTRATION.md",
    HERE / "TERNARY_CUBE_FULL_RESOLUTION.md",
    HERE / "FULL_RESOLUTION_REPLAY.md",
    HERE / "full_resolution_replay.py",
    ROOT / "tests/test_segre_hadamard_full_resolution.py",
)


def need(condition, message):
    if not condition:
        raise ValueError(message)


def integer(value, low, high):
    need(type(value) is int and low <= value <= high, "integer outside declared cap")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest_rows(rows):
    digest = hashlib.sha256()
    for row in rows:
        digest.update((canonical(row) + "\n").encode())
    return digest.hexdigest()


def authenticate():
    result, raw_sources = {}, {}
    for name, expected in PINS.items():
        actual = subprocess.check_output(
            ["git", "rev-parse", f"{FREEZE}:{PREFIX}{name}"], cwd=ROOT, text=True
        ).strip()
        need(actual == expected, "frozen degree-four acquisition mismatch")
        raw = subprocess.check_output(["git", "cat-file", "blob", actual], cwd=ROOT)
        need(len(raw) <= MAX_BYTES, "frozen source byte cap")
        data = (HERE / name).read_bytes().replace(b"\r\n", b"\n")
        need(data == raw.replace(b"\r\n", b"\n"), "working acquisition changed")
        result[name] = {"blob": expected, "sha256_lf": hashlib.sha256(data).hexdigest()}
        raw_sources[name] = raw
    return result, json.loads(raw_sources["resolution_degree4.discovery.json"])


def source():
    provenance, acquisition = authenticate()
    name = "frozen_ternary_resolution_acquisition"
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            name, HERE / "resolution_replay.py"
        )
        need(spec is not None and spec.loader is not None, "frozen helper import")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[name] = module
    helper = sys.modules[name]
    presentation = helper.authenticate()
    helper.validate_modules(
        presentation["result"]["generators"], presentation["result"]["D1_columns"]
    )
    return helper, presentation["result"], acquisition, provenance


def blocks(weights):
    out = defaultdict(list)
    for i, weight in enumerate(weights):
        out[tuple(weight)].append(i)
    return dict(sorted(out.items()))


def sparse(vector):
    return [[i, a] for i, a in sorted(vector.items()) if a]


def preflight(evaluation):
    profiles = []
    for weight, indices in blocks(evaluation["weights"]).items():
        support = set().union(*(evaluation["columns"][i] for i in indices))
        profiles.append(
            {"weight": weight, "rows": len(support), "columns": len(indices)}
        )
    largest_rows = max((x["rows"] for x in profiles), default=0)
    largest_columns = max((x["columns"] for x in profiles), default=0)
    need(
        max(largest_rows, largest_columns) <= MAX_BLOCK,
        "preflight weight-block cap: "
        + canonical(
            {
                "grade": evaluation["grade"],
                "largest_rows": largest_rows,
                "largest_columns": largest_columns,
                "cap": MAX_BLOCK,
            }
        ),
    )
    return profiles


def kernel(helper, evaluation):
    """The acquisition algorithm, with an explicitly local staged cap."""
    preflight(evaluation)
    relations, weights, stats = [], [], []
    for weight, indices in blocks(evaluation["weights"]).items():
        support = set().union(*(evaluation["columns"][i] for i in indices))
        pivots, local, bits = {}, [], 0
        for i in indices:
            vector = {j: Fraction(a) for j, a in evaluation["columns"][i].items()}
            witness = {i: Fraction(1)}
            while vector:
                leading = min(vector)
                if leading in pivots:
                    old_image, old_witness = pivots[leading]
                    scalar = vector[leading]
                    helper.subtract_multiple(vector, old_image, scalar)
                    helper.subtract_multiple(witness, old_witness, scalar)
                else:
                    scalar = vector[leading]
                    image = {j: a / scalar for j, a in vector.items()}
                    witness = {j: a / scalar for j, a in witness.items()}
                    bits = max(
                        bits, helper.check_bits(image), helper.check_bits(witness)
                    )
                    pivots[leading] = (image, witness)
                    break
            if not vector:
                relation = helper.primitive_integer(witness)
                need(
                    not helper.image_of_relation(evaluation["columns"], relation),
                    "kernel witness has nonzero actual composition",
                )
                local.append(relation)
        need(len(indices) == len(pivots) + len(local), "kernel rank-nullity")
        relations.extend(local)
        weights.extend([weight] * len(local))
        stats.append(
            {
                "weight": weight,
                "rows": len(support),
                "columns": len(indices),
                "rank": len(pivots),
                "nullity": len(local),
                "max_exact_bits": bits,
            }
        )
    return relations, weights, stats


class Span:
    def __init__(self, helper):
        self.helper = helper
        self.pivots = {}
        self.max_bits = 0

    def add(self, raw):
        vector = {i: Fraction(a) for i, a in raw.items() if a}
        while vector:
            leading = min(vector)
            if leading in self.pivots:
                self.helper.subtract_multiple(
                    vector, self.pivots[leading], vector[leading]
                )
            else:
                scalar = vector[leading]
                vector = {i: a / scalar for i, a in vector.items()}
                self.max_bits = max(self.max_bits, self.helper.check_bits(vector))
                self.pivots[leading] = vector
                return True
        return False


def select_quotient(
    helper, evaluation, relations, weights, previous, current_generators
):
    """Select actual kernel classes modulo actual lower-degree multiples."""
    old = helper.evaluated_map(current_generators, previous, evaluation["grade"])
    need(
        old["target_basis"] == evaluation["domain_basis"],
        "old multiple coordinate basis differs",
    )
    preflight(old)
    spans = {}
    for i, weight in enumerate(old["weights"]):
        need(
            not helper.image_of_relation(evaluation["columns"], old["columns"][i]),
            "old multiple has nonzero composition",
        )
        spans.setdefault(weight, Span(helper)).add(old["columns"][i])
    old_rank = sum(len(span.pivots) for span in spans.values())
    chosen, chosen_weights = [], []
    for relation, weight in zip(relations, weights, strict=True):
        if spans.setdefault(weight, Span(helper)).add(relation):
            chosen.append(relation)
            chosen_weights.append(weight)
    need(
        sum(len(span.pivots) for span in spans.values()) == len(relations),
        "old plus new does not span full kernel",
    )
    return chosen, chosen_weights, old, old_rank


def evaluation_record(evaluation, stats, relations):
    return {
        "grade": evaluation["grade"],
        "full_target_rows": len(evaluation["target_basis"]),
        "domain_columns": len(evaluation["domain_basis"]),
        "basis_order": "generator order, then lexicographic weak compositions in ten W variables",
        "target_basis_sha256": digest_rows(evaluation["target_basis"]),
        "domain_basis_sha256": digest_rows(evaluation["domain_basis"]),
        "sparse_matrix_columns_sha256": digest_rows(
            sparse(v) for v in evaluation["columns"]
        ),
        "complete_column_weights": evaluation["weights"],
        "weight_blocks": stats,
        "full_original_coordinate_kernel_basis": [sparse(v) for v in relations],
        "rank": sum(row["rank"] for row in stats),
        "nullity": len(relations),
    }


def quotient_record(old, rank, selected):
    return {
        "old_multiple_domain_basis": old["domain_basis"],
        "old_multiple_weights": old["weights"],
        "actual_old_columns_in_current_domain": [sparse(v) for v in old["columns"]],
        "actual_old_rank": rank,
        "new_quotient_dimension": len(selected),
        "selected_original_coordinate_kernel_vectors": [sparse(v) for v in selected],
    }


def weight_check(columns, source_columns, source_degree):
    expected = Counter(
        tuple(7 - x for x in c["weight"])
        for c in source_columns
        if c["degree"] == source_degree
    )
    actual = Counter(tuple(c["weight"]) for c in columns)
    need(actual == expected, "full dual Tor weight multiplicities mismatch")
    return {
        "dimension": sum(actual.values()),
        "weight_multiplicities": [[w, a] for w, a in sorted(actual.items())],
        "complete_match": True,
    }


def build_maps(stage=5):
    integer(stage, 5, 7)
    helper, presentation, acquisition, provenance = source()
    f0, d1 = presentation["generators"], presentation["D1_columns"]
    evaluation4 = helper.evaluated_map(f0, d1, 4)
    relations4, weights4, stats4 = kernel(helper, evaluation4)
    d2 = helper.differential_columns(evaluation4, relations4, weights4)
    need(
        hashlib.sha256(canonical(d2).encode()).hexdigest()
        == acquisition["D2_degree_four_columns_sha256"],
        "acquired actual degree-four maps changed",
    )
    checks = {"D2_degree4": weight_check(d2, d1, 3)}
    stages = [
        {"map": "D1", "evaluation": evaluation_record(evaluation4, stats4, relations4)}
    ]
    del evaluation4, relations4, weights4

    evaluation5 = helper.evaluated_map(f0, d1, 5)
    relations5, weights5, stats5 = kernel(helper, evaluation5)
    need(
        (
            len(evaluation5["target_basis"]),
            len(evaluation5["domain_basis"]),
            len(relations5),
        )
        == (16577, 7975, 659),
        "actual degree-five D1 prediction",
    )
    new5, new_weights5, old5, old_rank5 = select_quotient(
        helper, evaluation5, relations5, weights5, d2, d1
    )
    need(
        (len(old5["columns"]), old_rank5, len(new5)) == (650, 639, 20),
        "actual degree-five D2 quotient prediction",
    )
    d2_new = helper.differential_columns(evaluation5, new5, new_weights5)
    checks["D2_degree5"] = weight_check(d2_new, d1, 2)
    d2.extend(d2_new)
    stages.append(
        {
            "map": "D1",
            "evaluation": evaluation_record(evaluation5, stats5, relations5),
            "minimal_quotient": quotient_record(old5, old_rank5, new5),
        }
    )
    del evaluation5, relations5, weights5, old5, new5, new_weights5

    d3 = []
    for degree in range(5, stage + 1):
        evaluation = helper.evaluated_map(d1, d2, degree)
        relations, weights, stats = kernel(helper, evaluation)
        expected_domain = {5: 670, 6: 3775, 7: 15400}[degree]
        expected_nullity = {5: 11, 6: 127, 7: 776}[degree]
        need(
            (len(evaluation["domain_basis"]), len(relations))
            == (expected_domain, expected_nullity),
            "actual D2 kernel prediction",
        )
        if d3:
            new, new_weights, old, old_rank = select_quotient(
                helper, evaluation, relations, weights, d3, d2
            )
            expected = {6: (110, 110, 17), 7: (775, 775, 1)}[degree]
            need(
                (len(old["columns"]), old_rank, len(new)) == expected,
                "actual D3 minimal quotient prediction",
            )
            quotient = quotient_record(old, old_rank, new)
        else:
            new, new_weights, quotient = relations, weights, None
        added = helper.differential_columns(evaluation, new, new_weights)
        checks[f"D3_degree{degree}"] = weight_check(added, f0, 7 - degree)
        d3.extend(added)
        stages.append(
            {
                "map": "D2",
                "evaluation": evaluation_record(evaluation, stats, relations),
                "minimal_quotient": quotient,
            }
        )
        del evaluation, relations, weights, new, new_weights
    return {
        "source_freeze": FREEZE,
        "source_bindings": provenance,
        "stage": stage,
        "F0_generators": f0,
        "D1_columns": d1,
        "D2_columns": d2,
        "D3_columns": d3,
        "stages": stages,
        "complete_Tor_weight_checks": checks,
        "all_old_and_new_compositions_zero": True,
        "complete_resolution_constructed": stage == 7,
        "marked_basis_is_GL3_equivariant": False,
        "independent_global_exactness_proof_required": True,
    }


def summary(maps):
    return {
        "stage": maps["stage"],
        "D2_columns": len(maps["D2_columns"]),
        "D3_columns": len(maps["D3_columns"]),
        "stages": [
            {
                "map": row["map"],
                "grade": row["evaluation"]["grade"],
                "rows": row["evaluation"]["full_target_rows"],
                "columns": row["evaluation"]["domain_columns"],
                "rank": row["evaluation"]["rank"],
                "nullity": row["evaluation"]["nullity"],
                "largest_block_rows": max(
                    b["rows"] for b in row["evaluation"]["weight_blocks"]
                ),
                "largest_block_columns": max(
                    b["columns"] for b in row["evaluation"]["weight_blocks"]
                ),
                "max_exact_bits": max(
                    b["max_exact_bits"] for b in row["evaluation"]["weight_blocks"]
                ),
            }
            for row in maps["stages"]
        ],
    }


def build():
    maps = build_maps(7)
    result = {
        "schema": "actual-ternary-Chow-full-minimal-resolution-v1",
        "owned_sha256_lf": {
            str(path.relative_to(ROOT)).replace("\\", "/"): hashlib.sha256(
                path.read_bytes().replace(b"\r\n", b"\n")
            ).hexdigest()
            for path in OWNED
        },
        "summary": summary(maps),
        "result": maps,
    }
    result["proof_object_sha256"] = hashlib.sha256(
        canonical(result).encode()
    ).hexdigest()
    need(len(canonical(result).encode()) <= MAX_BYTES, "full resolution artifact cap")
    return result


def check_payload(candidate, expected):
    need(
        canonical(candidate) == canonical(expected),
        "typed full-resolution artifact differs",
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--scout", type=int, choices=(5, 6, 7))
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.scout is not None:
        maps = build_maps(args.scout)
        print(
            json.dumps(
                {
                    "summary": summary(maps),
                    "complete_Tor_weight_checks": maps["complete_Tor_weight_checks"],
                    "fixture_written": False,
                },
                sort_keys=True,
            )
        )
        return
    record = build()
    if args.write:
        data = (
            json.dumps(record, indent=2, sort_keys=True, allow_nan=False) + "\n"
        ).encode()
        need(len(data) <= MAX_BYTES, "full resolution artifact cap")
        FIXTURE.write_bytes(data)
    else:
        data = FIXTURE.read_bytes()
        need(len(data) <= MAX_BYTES, "full resolution artifact cap")
        check_payload(json.loads(data), record)
    print(
        json.dumps(
            {
                "status": "PASS",
                "summary": record["summary"],
                "proof_object_sha256": record["proof_object_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
