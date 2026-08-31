"""An actual central top relation, with theorem-guided global exactness."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
HELPER_FREEZE = "ed8c7251719a381abf6d55f57d768d69e76b776d"
HELPER_PINS = {
    "composed_grade7_replay.py": "8b65553b2505533b3bb4471631c73eb8aa4266db",
    "COMPOSED_GRADE7_PREREGISTRATION.md": "424dae98a5978a5ffd1f66f52044f036d2b98cbb",
    "COMPOSED_GRADE7_REPLAY.md": "38edad9e9747f45c45c35740925bf8a777c71889",
    "@tests/test_segre_hadamard_composed_grade7.py": "d0a2cc3f3f4f49173a9f31c077c818ade7dec781",
    "composed_grade7_prefix.discovery.json": "9e057f58f16f4853a65dd152d5c83ca719e829fb",
}
PROOF_FREEZE = "ed8c7251719a381abf6d55f57d768d69e76b776d"
PROOF_PINS = {
    "CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md": "ca97c3ebdbd813181f1716899f662e63a3bc7ee7"
}
THEOREM_PINS = (
    (
        "a895f47628b0bc7c7ee5e0392df2f79c24166f92",
        "MATHEMATICS.md",
        "bbd847461b4955a93b4533fa687cdd8724e2347c",
    ),
    (
        "08147ccecfe684af76a8417861fcccda61abe601",
        "TERNARY_CUBE_TOR_CHARACTERS.md",
        "f8edf2aac25e96434f77e1fc1681b8f22c609071",
    ),
    (
        "08147ccecfe684af76a8417861fcccda61abe601",
        "tor_characters.verification.json",
        "4ea01d1d6fbb0383e31f03f060a8511dd3c7a1e4",
    ),
)
MAX_BYTES = 64 * 1024 * 1024
WEIGHT = (7, 7, 7)
PREREG = HERE / "CENTRAL_TOP_CLASS_PREREGISTRATION.md"
OWNED = (
    Path(__file__),
    PREREG,
    HERE / "CENTRAL_TOP_CLASS_REPLAY.md",
    ROOT / "tests/test_segre_hadamard_central_top.py",
)
DIRECTORY = HERE / "central_top_weightblock"
FIXTURE = HERE / "central_top_resolution.verification.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    result, size = hashlib.sha256(), 0
    for chunk in json.JSONEncoder(
        sort_keys=True, separators=(",", ":"), allow_nan=False
    ).iterencode(value):
        raw = chunk.encode()
        size += len(raw)
        need(size <= MAX_BYTES, "central proof byte cap")
        result.update(raw)
    return result.hexdigest()


def equal(left, right):
    need(
        canonical(left) == canonical(right),
        "typed complete central certificate differs",
    )


def no_float(_value):
    raise ValueError("nonintegral JSON number")


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded artifact bytes")
    return json.loads(
        raw, parse_float=no_float, parse_constant=no_float, object_pairs_hook=unique
    )


def authenticate():
    entries = [(HELPER_FREEZE, name, blob) for name, blob in HELPER_PINS.items()]
    entries += [(PROOF_FREEZE, name, blob) for name, blob in PROOF_PINS.items()]
    entries += list(THEOREM_PINS)
    # Pending inputs fail before even the first Git/source access.
    need(
        all(
            type(value) is str
            and len(value) == 40
            and all(c in "0123456789abcdef" for c in value)
            for freeze, _, blob in entries
            for value in (freeze, blob)
        ),
        "exact helper/theorem freezes required",
    )
    raw, provenance = {}, []
    for freeze, name, expected in entries:
        path = name[1:] if name.startswith("@") else PREFIX + name
        blob = subprocess.check_output(
            ["git", "rev-parse", f"{freeze}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(blob == expected, "central source identity")
        size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
        need(0 < size <= MAX_BYTES, "central source byte cap")
        data = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(
            len(data) == size
            and hashlib.sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest()
            == blob,
            "actual Git bytes",
        )
        current = ROOT / path
        need(current.stat().st_size <= MAX_BYTES, "working source byte cap")
        need(
            data.replace(b"\r\n", b"\n")
            == current.read_bytes().replace(b"\r\n", b"\n"),
            "frozen source changed",
        )
        raw[name] = data
        provenance.append({"freeze": freeze, "path": path, "blob": blob})
    return raw, provenance


def algorithm_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in (Path(__file__), PREREG)
    }


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def source():
    raw, provenance = authenticate()
    path = HERE / "composed_grade7_replay.py"
    namespace = {"__name__": "central_top_authenticated_prefix", "__file__": str(path)}
    exec(compile(raw[path.name], str(path), "exec"), namespace)  # noqa: S102
    prefix = SimpleNamespace(**namespace)
    context = prefix.source()
    accepted_prefix = prefix.read_json(raw["composed_grade7_prefix.discovery.json"])
    prefix.body_check(accepted_prefix)
    need(
        accepted_prefix["proof_object_sha256"]
        == "2301613316c82b81debf817ecf4580a1476e1b78e663dd23a57317a03eda8bb3",
        "accepted prefix exact proof",
    )
    equal(accepted_prefix["fresh_polynomial_checks"], context.prefix_checks)
    equal(accepted_prefix["inherited_proofs"], context.inherited)
    need(
        accepted_prefix["grade7_constructed"] is False
        and accepted_prefix["new_kernel_rank_claimed"] is False,
        "prefix acceptance is not grade-seven acceptance",
    )
    context.source_provenance = {
        "prefix_proofs": context.source_provenance,
        "central_sources": provenance,
        "central_algorithm": algorithm_bindings(),
    }
    return prefix, context


def central_matrix(context):
    streamed, helper, maps = context.streamed, context.helper, context.maps
    full = streamed.lazy_evaluation(helper, maps["D1_columns"], maps["D2_columns"], 7)
    indices = [i for i, weight in enumerate(full["weights"]) if tuple(weight) == WEIGHT]
    need(len(indices) == 592, "exact frozen central domain shape")
    evaluation = {
        "grade": 7,
        "target_basis": full["target_basis"],
        "domain_basis": tuple(full["domain_basis"][i] for i in indices),
        "weights": [WEIGHT] * len(indices),
        "columns": [full["columns"][i] for i in indices],
    }
    context.streamed.preflight_full(context.upstream, evaluation)
    need(len(evaluation["target_basis"]) == 86515, "original target address space")
    return evaluation, indices


def old_central_columns(context, evaluation, original_indices):
    helper, maps = context.helper, context.maps
    need(
        len(maps["D3_columns"]) == 28
        and Counter(column["degree"] for column in maps["D3_columns"])
        == {5: 11, 6: 17},
        "complete accepted lower D3 list",
    )
    lookup = {descriptor: i for i, descriptor in enumerate(evaluation["domain_basis"])}
    need(len(lookup) == 592, "distinct original central descriptors")
    columns, records = [], []
    for generator, column in enumerate(maps["D3_columns"]):
        degree = column["degree"]
        need(
            type(degree) is int and degree in (5, 6), "all accepted lower D3 generators"
        )
        for multiplier in helper.compositions(7 - degree, 10):
            if (
                helper.add(helper.polynomial_weight(multiplier), column["weight"])
                != WEIGHT
            ):
                continue
            vector = {}
            for term in column["terms"]:
                descriptor = (
                    term["generator"],
                    helper.add(multiplier, term["S_exponent"]),
                )
                need(
                    descriptor in lookup, "complete central old polynomial coordinates"
                )
                row = lookup[descriptor]
                vector[row] = vector.get(row, 0) + term["coefficient"]
            vector = {row: value for row, value in vector.items() if value}
            helper.check_bits(vector)
            need(
                vector and not helper.image_of_relation(evaluation["columns"], vector),
                "actual old column full-row composition",
            )
            columns.append(vector)
            records.append(
                {
                    "D3_generator": generator,
                    "multiplier": list(multiplier),
                    "weight": list(WEIGHT),
                    "central_coordinates": context.upstream.sparse(vector),
                    "original_F2_coordinates": [
                        [original_indices[row], value]
                        for row, value in sorted(vector.items())
                    ],
                }
            )
    need(0 < len(columns) <= 640, "bounded complete central old list")
    return columns, records


def outside_old_span(context, old, relations):
    need(len(old) <= 640 and len(relations) <= 640, "central quotient cap")
    span = context.upstream.Span(context.helper)
    for column in old:
        span.add(column)
    old_rank = len(span.pivots)
    selected = []
    for relation in relations:
        if span.add(relation):
            selected.append(relation)
    need(
        len(selected) == 1 and len(span.pivots) == old_rank + 1 == len(relations),
        "one actual class outside the complete exact old span",
    )
    return selected[0], {
        "complete_old_columns": len(old),
        "exact_old_rank": old_rank,
        "exact_augmented_rank": len(span.pivots),
        "central_kernel_dimension_measured": len(relations),
        "nonmembership_method": "exact_rational_span_rank_increase",
        "global_775_column_rank_measured": False,
    }


def build(directory=DIRECTORY):
    prefix, context = source()
    evaluation, original_indices = central_matrix(context)
    relations, weights, stats, certificates = context.streamed.certified_kernel(
        context, evaluation, directory
    )
    need(
        len(stats) == len(certificates) == 1
        and all(tuple(weight) == WEIGHT for weight in weights),
        "single central block only",
    )
    old, old_records = old_central_columns(context, evaluation, original_indices)
    vector, quotient = outside_old_span(context, old, relations)
    need(
        not context.helper.image_of_relation(evaluation["columns"], vector),
        "top vector every original target row",
    )
    added = context.helper.differential_columns(evaluation, [vector], [WEIGHT])
    need(
        len(added) == 1 and added[0]["degree"] == 7,
        "one actual top polynomial generator",
    )
    maps = context.maps
    maps["D3_columns"].extend(added)
    maps["complete_Tor_weight_checks"]["D3_degree7"] = context.upstream.weight_check(
        added, maps["F0_generators"], 0
    )
    for key in ("F0_generators", "D1_columns", "D2_columns"):
        need(
            prefix.digest(maps[key]) == context.inherited["lower_map_hashes"][key],
            "accepted lower map unchanged",
        )
    need(
        prefix.digest(maps["D3_columns"][:28])
        == context.inherited["lower_map_hashes"]["D3_columns"],
        "accepted lower D3 unchanged",
    )
    need(
        prefix.digest(maps["stages"])
        == context.inherited["lower_map_hashes"]["stages"],
        "accepted lower witnesses unchanged",
    )
    final_checks = prefix.map_checks(
        context.helper,
        context.upstream,
        maps,
        context.presentation,
        context.acquisition,
        final=True,
    )
    maps["stage"] = 7
    maps["complete_resolution_constructed"] = True
    maps["all_old_and_new_compositions_zero"] = True
    payload = {
        "schema": "actual-central-top-class-minimal-resolution-v1",
        "owned_sha256_lf": owned_bindings(),
        "source_provenance": context.source_provenance,
        "inherited_proofs": context.inherited,
        "fresh_prefix_polynomial_checks": context.prefix_checks,
        "final_polynomial_checks": final_checks,
        "central_certificate": {
            "weight": list(WEIGHT),
            "original_domain_indices": original_indices,
            "original_domain_descriptors": evaluation["domain_basis"],
            "original_target_basis_sha256": context.upstream.digest_rows(
                evaluation["target_basis"]
            ),
            "all_original_columns": [
                context.upstream.sparse(column) for column in evaluation["columns"]
            ],
            "complete_central_kernel": [
                context.upstream.sparse(relation) for relation in relations
            ],
            "full_row_certificate": certificates[0],
            "measured_statistics": stats[0],
            "complete_old_columns": old_records,
            "quotient": quotient,
            "selected_top_vector": context.upstream.sparse(vector),
            "selected_original_F2_vector": [
                [original_indices[row], value] for row, value in sorted(vector.items())
            ],
            "actual_top_polynomial_column": added[0],
        },
        "result": maps,
        "deductions_after_top_class": {
            "complete_minimal_resolution": True,
            "global_degree7_old_dimension": 775,
            "global_degree7_kernel_dimension": 776,
            "these_global_dimensions_are_measurements": False,
        },
        "contract": {
            "all_central_old_multiples_retained": True,
            "all_original_target_rows_checked": True,
            "exact_rational_nonmembership_checked": True,
            "lower_stage_elimination_replayed": False,
            "coordinate_acquisition_replayed": False,
            "global_775_column_elimination_executed": False,
            "global_776_vector_kernel_census_executed": False,
            "old52_contract_completed": False,
            "old42_contract_completed": False,
            "old26_contract_completed": False,
            "full_composed_contract_completed": False,
            "marked_lifts_claimed_GL3_equivariant": False,
        },
    }
    payload["proof_object_sha256"] = digest(payload)
    return payload


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--scout", action="store_true")
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build()
    if args.scout:
        print(canonical(payload))
        return
    if args.write:
        FIXTURE.write_text(canonical(payload) + "\n", encoding="utf-8")
    else:
        candidate = read_json(FIXTURE.read_bytes())
        need(
            digest({k: v for k, v in candidate.items() if k != "proof_object_sha256"})
            == candidate["proof_object_sha256"],
            "complete candidate body",
        )
        equal(candidate, payload)
    print(
        canonical(
            {
                "status": "PASS",
                "measured_central_quotient": payload["central_certificate"]["quotient"],
                "deductions_after_top_class": payload["deductions_after_top_class"],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
