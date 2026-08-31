"""One exactly certified top relation, discovered by bounded Dixon lifting."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from array import array
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PREFIX = "research/l-families/atlas/generalized/segre-hadamard-source/"
FREEZE = "547d91b6c8f8432f0f594c634e8a58349c929288"
PINS = {
    "central_top_resolution.py": "30ec95de4345a4998775bb9a8f85b8207ab84dff",
    "CENTRAL_TOP_CLASS_PREREGISTRATION.md": "463ea123f326e053d6029f2c8985308f7aebbb60",
    "CENTRAL_TOP_CLASS_REPLAY.md": "665b3b7b75e1a749da6101c0e023fb67bcb5fb2e",
    "@tests/test_segre_hadamard_central_top.py": "cac53e90c84a2b4dcf81e2c3ec77a79062ba4923",
}
PROOF_FREEZE = "ed8c7251719a381abf6d55f57d768d69e76b776d"
PROOF_NAME = "CENTRAL_TOP_CLASS_GLOBAL_EXACTNESS.md"
PROOF_BLOB = "ca97c3ebdbd813181f1716899f662e63a3bc7ee7"
MODULI = (65521, 1000003)
MAX_LIFTS = 16
MAX_BITS = 4096
MAX_ROWS = 4096
MAX_COLUMNS = 592
MAX_BYTES = 64 * 1024 * 1024
PREREG = HERE / "SINGLE_TOP_WITNESS_PREREGISTRATION.md"
OWNED = (
    Path(__file__),
    PREREG,
    HERE / "SINGLE_TOP_WITNESS_REPLAY.md",
    ROOT / "tests/test_segre_hadamard_single_top_witness.py",
)
FIXTURE = HERE / "single_top_witness.verification.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


class CapacityError(ValueError):
    """A declared exact-data cap, not a mathematical nonexistence result."""


def checked(value):
    need(type(value) is int, "literal exact integer")
    if abs(value).bit_length() > MAX_BITS:
        raise CapacityError("stored exact integer exceeds 4096 bits")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def digest(value):
    output, size = hashlib.sha256(), 0
    encoder = json.JSONEncoder(sort_keys=True, separators=(",", ":"), allow_nan=False)
    for chunk in encoder.iterencode(value):
        raw = chunk.encode()
        size += len(raw)
        need(size <= MAX_BYTES, "proof byte cap")
        output.update(raw)
    return output.hexdigest()


def equal(left, right):
    need(canonical(left) == canonical(right), "typed complete witness differs")


def no_float(_value):
    raise ValueError("nonintegral JSON number")


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, "duplicate JSON key")
        result[key] = value
    return result


def read_json(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_BYTES, "bounded JSON bytes")
    return json.loads(
        raw, parse_float=no_float, parse_constant=no_float, object_pairs_hook=unique
    )


def body_check(payload):
    need(type(payload) is dict and "proof_object_sha256" in payload, "proof body")
    need(
        digest({k: v for k, v in payload.items() if k != "proof_object_sha256"})
        == payload["proof_object_sha256"],
        "complete body digest",
    )


def authenticate():
    entries = [(FREEZE, name, blob) for name, blob in PINS.items()]
    entries.append((PROOF_FREEZE, PROOF_NAME, PROOF_BLOB))
    need(
        all(
            type(x) is str and len(x) == 40 and all(c in "0123456789abcdef" for c in x)
            for freeze, _, blob in entries
            for x in (freeze, blob)
        ),
        "exact fixed input pins required",
    )
    raw, provenance = {}, []
    for freeze, name, expected in entries:
        path = name[1:] if name.startswith("@") else PREFIX + name
        blob = subprocess.check_output(
            ["git", "rev-parse", f"{freeze}:{path}"], cwd=ROOT, text=True
        ).strip()
        need(blob == expected, "frozen source identity")
        size = int(subprocess.check_output(["git", "cat-file", "-s", blob], cwd=ROOT))
        need(0 < size <= MAX_BYTES, "frozen byte cap")
        data = subprocess.check_output(["git", "cat-file", "blob", blob], cwd=ROOT)
        need(
            len(data) == size
            and hashlib.sha1(b"blob " + str(size).encode() + b"\0" + data).hexdigest()
            == blob,
            "actual frozen bytes",
        )
        current = ROOT / path
        need(current.stat().st_size <= MAX_BYTES, "working byte cap")
        need(
            data.replace(b"\r\n", b"\n")
            == current.read_bytes().replace(b"\r\n", b"\n"),
            "frozen working source changed",
        )
        raw[name] = data
        provenance.append({"freeze": freeze, "path": path, "blob": blob})
    return raw, provenance


def owned_bindings():
    return {
        path.relative_to(ROOT).as_posix(): hashlib.sha256(
            path.read_bytes().replace(b"\r\n", b"\n")
        ).hexdigest()
        for path in OWNED
    }


def source():
    raw, provenance = authenticate()
    path = HERE / "central_top_resolution.py"
    namespace = {
        "__name__": "single_witness_authenticated_central",
        "__file__": str(path),
    }
    exec(compile(raw[path.name], str(path), "exec"), namespace)  # noqa: S102
    central = SimpleNamespace(**namespace)
    prefix, context = central.source()
    context.single_witness_provenance = provenance
    return central, prefix, context


def validate_columns(columns):
    need(type(columns) is list and 0 < len(columns) <= MAX_COLUMNS, "column cap")
    support = set()
    for column in columns:
        need(type(column) is dict, "literal sparse column")
        for row, value in column.items():
            need(type(row) is int and row >= 0, "literal original row address")
            checked(value)
            need(value != 0, "sparse zero entry")
            support.add(row)
    need(len(support) <= MAX_ROWS, "supported original row cap")
    return sorted(support)


def select_rows(columns, modulus, target):
    """Bounded modular search; stops at target, not a full-rank assertion."""
    need(type(modulus) is int and modulus in MODULI, "fixed prime")
    need(type(target) is int and 0 < target <= len(columns), "target selection rank")
    support = validate_columns(columns)
    pivots, selected = {}, []
    for row in support:
        vector = array("I", (column.get(row, 0) % modulus for column in columns))
        for lead in range(len(columns)):
            scalar = vector[lead]
            if not scalar:
                continue
            if lead not in pivots:
                inverse = pow(scalar, modulus - 2, modulus)
                for j in range(lead, len(columns)):
                    vector[j] = vector[j] * inverse % modulus
                pivots[lead] = vector
                selected.append(row)
                break
            pivot = pivots[lead]
            for j in range(lead, len(columns)):
                vector[j] = (vector[j] - scalar * pivot[j]) % modulus
        if len(selected) == target:
            break
    return {
        "modulus": modulus,
        "selected_original_rows": selected,
        "pivot_columns": sorted(pivots),
        "selected_rank": len(selected),
        "requested_rank": target,
        "remaining_rows_censused": False,
    }


def lu_factor(matrix, modulus):
    need(type(modulus) is int and modulus in MODULI, "fixed LU prime")
    n = len(matrix)
    need(0 < n <= MAX_COLUMNS and all(len(row) == n for row in matrix), "square LU cap")
    lu = [array("I", (checked(value) % modulus for value in row)) for row in matrix]
    permutation, determinant = list(range(n)), 1
    for k in range(n):
        pivot = next((i for i in range(k, n) if lu[i][k]), None)
        if pivot is None:
            return None
        if pivot != k:
            lu[k], lu[pivot] = lu[pivot], lu[k]
            permutation[k], permutation[pivot] = permutation[pivot], permutation[k]
            determinant = -determinant
        diagonal = lu[k][k]
        determinant = determinant * diagonal % modulus
        inverse = pow(diagonal, modulus - 2, modulus)
        pivot_row = lu[k]
        for i in range(k + 1, n):
            if not lu[i][k]:
                continue
            factor = lu[i][k] * inverse % modulus
            row = lu[i]
            row[k] = factor
            for j in range(k + 1, n):
                row[j] = (row[j] - factor * pivot_row[j]) % modulus
    return {
        "rows": lu,
        "permutation": permutation,
        "determinant_mod_prime": determinant % modulus,
        "modulus": modulus,
    }


def lu_solve(factor, rhs):
    lu, permutation, modulus = factor["rows"], factor["permutation"], factor["modulus"]
    n = len(lu)
    need(len(rhs) == n, "LU right-hand side")
    y = [0] * n
    for i in range(n):
        y[i] = (rhs[permutation[i]] - sum(lu[i][j] * y[j] for j in range(i))) % modulus
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (
            (y[i] - sum(lu[i][j] * x[j] for j in range(i + 1, n)))
            * pow(lu[i][i], modulus - 2, modulus)
        ) % modulus
    return x


def rational_reconstruct(residue, modulus):
    need(
        type(residue) is int and type(modulus) is int and modulus > 1,
        "literal reconstruction inputs",
    )
    residue %= modulus
    if not residue:
        return (0, 1)
    bound = math.isqrt((modulus - 1) // 2)
    r0, r1, t0, t1 = modulus, residue, 0, 1
    while abs(r1) > bound:
        quotient = r0 // r1
        r0, r1, t0, t1 = r1, r0 - quotient * r1, t1, t0 - quotient * t1
    if t1 < 0:
        r1, t1 = -r1, -t1
    if not (
        0 < t1 <= bound
        and abs(r1) <= bound
        and math.gcd(abs(r1), t1) == math.gcd(t1, modulus) == 1
        and (r1 - residue * t1) % modulus == 0
    ):
        return None
    return checked(r1), checked(t1)


def primitive_candidate(pairs, pivot_coordinates, free_coordinate):
    need(len(pairs) == len(pivot_coordinates), "candidate coordinates")
    need(
        type(free_coordinate) is int
        and 0 <= free_coordinate < MAX_COLUMNS
        and all(type(i) is int and 0 <= i < MAX_COLUMNS for i in pivot_coordinates)
        and len(set(pivot_coordinates)) == len(pivot_coordinates)
        and free_coordinate not in pivot_coordinates,
        "distinct literal candidate coordinates",
    )
    denominator = 1
    for numerator, divisor in pairs:
        checked(numerator)
        checked(divisor)
        need(divisor > 0, "positive reconstructed denominator")
        denominator = checked(math.lcm(denominator, divisor))
    vector = {free_coordinate: denominator}
    for coordinate, (numerator, divisor) in zip(pivot_coordinates, pairs, strict=True):
        coefficient = checked(numerator * (denominator // divisor))
        if coefficient:
            vector[coordinate] = coefficient
    common = math.gcd(*vector.values())
    vector = {
        coordinate: checked(value // common) for coordinate, value in vector.items()
    }
    if vector[min(vector)] < 0:
        vector = {coordinate: -value for coordinate, value in vector.items()}
    return vector


def full_residual(columns, vector):
    need(type(vector) is dict and bool(vector), "nonzero sparse candidate")
    result = {}
    for index, coefficient in vector.items():
        need(
            type(index) is int and 0 <= index < len(columns),
            "original vector coordinate",
        )
        checked(coefficient)
        need(coefficient != 0, "candidate sparse zero")
        for row, value in columns[index].items():
            result[row] = result.get(row, 0) + coefficient * value
    result = {row: checked(value) for row, value in result.items() if value}
    need(len(result) <= MAX_ROWS, "full residual row cap")
    return result


def minor_certificate(old, gauge, modulus):
    need(
        type(gauge) is list
        and len(gauge) == len(old)
        and all(type(row) is int and 0 <= row < MAX_COLUMNS for row in gauge)
        and len(set(gauge)) == len(gauge),
        "complete old-coordinate gauge",
    )
    validate_columns(old)
    minor = [[column.get(row, 0) for column in old] for row in gauge]
    factor = lu_factor(minor, modulus)
    need(
        factor is not None and factor["determinant_mod_prime"] != 0,
        "actual old-coordinate minor must be nonsingular",
    )
    return {
        "modulus": modulus,
        "gauge_coordinates": gauge,
        "all_old_column_count": len(old),
        "integer_minor": minor,
        "determinant_mod_prime": factor["determinant_mod_prime"],
        "row_permutation": factor["permutation"],
        "exact_old_independence_certified": True,
    }


def verify_witness(columns, old, gauge, modulus, vector):
    support = validate_columns(columns)
    need(
        len(old) == len(gauge) and all(not full_residual(columns, v) for v in old),
        "every complete old column is an actual relation",
    )
    certificate = minor_certificate(old, gauge, modulus)
    need(
        type(vector) is dict and vector and math.gcd(*vector.values()) == 1,
        "nonzero primitive integer witness",
    )
    need(all(vector.get(row, 0) == 0 for row in gauge), "all gauge coordinates vanish")
    residual = full_residual(columns, vector)
    need(not residual, "every original row of the top relation")
    need(vector[min(vector)] > 0, "canonical primitive sign")
    return {
        "minor": certificate,
        "supported_original_row_count": len(support),
        "every_original_row_checked": True,
        "full_original_residual": [],
        "nonzero_primitive_witness": True,
        "all_gauge_coordinates_zero": True,
        "exact_nonmembership": "invertible_complete_old_coordinate_minor",
        "central_kernel_dimension_measured": False,
    }


def dixon_attempt(columns, old, modulus, max_lifts=MAX_LIFTS):
    need(type(max_lifts) is int and 1 <= max_lifts <= MAX_LIFTS, "fixed lift cap")
    n = len(columns)
    validate_columns(columns)
    selection = select_rows(old, modulus, len(old))
    record = {"modulus": modulus, "old_row_selection": selection, "lifts": []}
    if selection["selected_rank"] != len(old):
        record["status"] = "UNKNOWN_OLD_MINOR_RANK_DROP"
        return None, record
    gauge = selection["selected_original_rows"]
    record["old_minor"] = minor_certificate(old, gauge, modulus)
    retained = [i for i in range(n) if i not in set(gauge)]
    reduced = [columns[i] for i in retained]
    needed = len(reduced) - 1
    need(0 < needed <= 542, "bounded normalized subsystem")
    selected = select_rows(reduced, modulus, needed)
    record["subsystem_row_selection"] = selected
    if selected["selected_rank"] != needed:
        record["status"] = "UNKNOWN_SUBSYSTEM_RANK_DROP"
        return None, record
    pivots = selected["pivot_columns"]
    free = [i for i in range(len(reduced)) if i not in set(pivots)]
    need(len(free) == 1, "one normalized search coordinate")
    free_coordinate = retained[free[0]]
    pivot_coordinates = [retained[i] for i in pivots]
    rows = selected["selected_original_rows"]
    matrix = [[columns[i].get(row, 0) for i in pivot_coordinates] for row in rows]
    rhs = [-columns[free_coordinate].get(row, 0) for row in rows]
    factor = lu_factor(matrix, modulus)
    need(factor is not None, "selected modular subsystem is invertible")
    record["subsystem"] = {
        "pivot_central_coordinates": pivot_coordinates,
        "free_central_coordinate": free_coordinate,
        "selected_original_rows": rows,
        "integer_matrix_sha256": digest(matrix),
        "integer_rhs": rhs,
        "determinant_mod_prime": factor["determinant_mod_prime"],
        "search_rank_is_not_a_full_rational_rank_claim": True,
    }
    sparse_matrix = [[(j, x) for j, x in enumerate(row) if x] for row in matrix]
    del matrix
    solution, power = [0] * needed, 1
    for lift in range(1, max_lifts + 1):
        residual = [
            rhs[i] - sum(x * solution[j] for j, x in row)
            for i, row in enumerate(sparse_matrix)
        ]
        need(all(x % power == 0 for x in residual), "exact Dixon divisibility")
        correction = lu_solve(factor, [x // power for x in residual])
        solution = [
            value + power * delta
            for value, delta in zip(solution, correction, strict=True)
        ]
        power *= modulus
        need(
            all(
                (rhs[i] - sum(x * solution[j] for j, x in row)) % power == 0
                for i, row in enumerate(sparse_matrix)
            ),
            "exact lifted congruences",
        )
        item = {
            "lift": lift,
            "modulus_power": power,
            "normalized_residues": solution.copy(),
        }
        pairs = [rational_reconstruct(value, power) for value in solution]
        failed = [i for i, value in enumerate(pairs) if value is None]
        if failed:
            item.update(
                status="NO_COMPLETE_RATIONAL_RECONSTRUCTION", failed_coordinates=failed
            )
            record["lifts"].append(item)
            continue
        item["reconstructed_fractions"] = pairs
        try:
            vector = primitive_candidate(pairs, pivot_coordinates, free_coordinate)
            original_residual = full_residual(columns, vector)
        except CapacityError as error:
            item.update(status="CANDIDATE_CAP_REFUSAL", reason=str(error))
            record["lifts"].append(item)
            continue
        item["candidate"] = [[i, x] for i, x in sorted(vector.items())]
        item["full_original_residual"] = [
            [i, x] for i, x in sorted(original_residual.items())
        ]
        if original_residual:
            item["status"] = "EXACT_FULL_ROW_RESIDUAL_NONZERO"
            record["lifts"].append(item)
            continue
        certificate = verify_witness(columns, old, gauge, modulus, vector)
        item["status"] = "EXACT_WITNESS_ACCEPTED"
        record["lifts"].append(item)
        record.update(status="PASS_SINGLE_WITNESS", acceptance=certificate)
        return vector, record
    record["status"] = "UNKNOWN_LIFT_BUDGET_EXHAUSTED"
    return None, record


def search(columns, old):
    attempts = []
    for modulus in MODULI:
        vector, attempt = dixon_attempt(columns, old, modulus)
        attempts.append(attempt)
        if vector is not None:
            return vector, attempts
    return None, attempts


def promote(prefix, context, evaluation, vector):
    helper, maps = context.helper, context.maps
    added = helper.differential_columns(evaluation, [vector], [(7, 7, 7)])
    need(len(added) == 1 and added[0]["degree"] == 7, "one actual top polynomial map")
    maps["D3_columns"].extend(added)
    maps["complete_Tor_weight_checks"]["D3_degree7"] = context.upstream.weight_check(
        added, maps["F0_generators"], 0
    )
    for key in ("F0_generators", "D1_columns", "D2_columns", "stages"):
        need(
            prefix.digest(maps[key]) == context.inherited["lower_map_hashes"][key],
            "accepted lower source preserved",
        )
    need(
        prefix.digest(maps["D3_columns"][:28])
        == context.inherited["lower_map_hashes"]["D3_columns"],
        "accepted lower D3 preserved",
    )
    checks = prefix.map_checks(
        helper,
        context.upstream,
        maps,
        context.presentation,
        context.acquisition,
        final=True,
    )
    maps["stage"] = 7
    maps["complete_resolution_constructed"] = True
    maps["all_old_and_new_compositions_zero"] = True
    return added[0], checks


def build():
    central, prefix, context = source()
    evaluation, original_indices = central.central_matrix(context)
    old, old_records = central.old_central_columns(
        context, evaluation, original_indices
    )
    need(
        len(evaluation["columns"]) == 592 and len(old) == 49,
        "actual complete 592-column source and 49 old columns",
    )
    vector, attempts = search(evaluation["columns"], old)
    payload = {
        "schema": "single-top-witness-dixon-v1",
        "owned_sha256_lf": owned_bindings(),
        "source_provenance": {
            "single_witness": context.single_witness_provenance,
            "inherited": context.source_provenance,
        },
        "inherited_proofs": context.inherited,
        "fresh_prefix_polynomial_checks": context.prefix_checks,
        "original_central_data": {
            "weight": [7, 7, 7],
            "original_domain_indices": original_indices,
            "original_domain_descriptors": evaluation["domain_basis"],
            "original_target_basis_sha256": context.upstream.digest_rows(
                evaluation["target_basis"]
            ),
            "all_original_columns": [
                context.upstream.sparse(c) for c in evaluation["columns"]
            ],
            "complete_old_columns": old_records,
        },
        "attempts": attempts,
        "status": "UNKNOWN_NO_CERTIFIED_WITNESS"
        if vector is None
        else "PASS_SINGLE_WITNESS",
        "complete_minimal_resolution": vector is not None,
        "contract": {
            "all_original_rows_checked_for_acceptance": True,
            "complete_old_list_retained": True,
            "full_central_kernel_computed": False,
            "central_kernel_dimension_measured": False,
            "modular_rank_promoted_to_rational_nullity": False,
            "old20_contract_completed": False,
            "old52_contract_completed": False,
            "old42_contract_completed": False,
            "old26_contract_completed": False,
            "full_composed_contract_completed": False,
            "lower_stage_elimination_replayed": False,
            "coordinate_acquisition_replayed": False,
            "marked_lifts_claimed_GL3_equivariant": False,
        },
    }
    if vector is not None:
        top, checks = promote(prefix, context, evaluation, vector)
        payload.update(
            selected_top_vector=context.upstream.sparse(vector),
            selected_original_F2_vector=[
                [original_indices[i], x] for i, x in sorted(vector.items())
            ],
            actual_top_polynomial_column=top,
            final_polynomial_checks=checks,
            result=context.maps,
            deductions_after_top_class={
                "global_degree7_old_dimension": 775,
                "global_degree7_kernel_dimension": 776,
                "these_global_dimensions_are_measurements": False,
            },
        )
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
        body_check(candidate)
        equal(candidate, payload)
    print(
        canonical(
            {
                "execution": "PASS",
                "mathematical_status": payload["status"],
                "complete_minimal_resolution": payload["complete_minimal_resolution"],
                "attempts": [
                    {
                        "modulus": a["modulus"],
                        "status": a["status"],
                        "lifts": len(a["lifts"]),
                    }
                    for a in payload["attempts"]
                ],
                "proof_object_sha256": payload["proof_object_sha256"],
            }
        )
    )


if __name__ == "__main__":
    main()
