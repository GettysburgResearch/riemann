#!/usr/bin/env python3
"""Audit the exact Sym12 master adapter and isolate its one-Tate conflict.

The replay authenticates five committed packets, checks the stack, arithmetic,
boundary, stable-channel, and provenance interfaces, and evaluates three
stored raw-T residuals.  It does not enumerate a field or promote the three
residuals to an all-q Galois identity.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym12_master_adapter_contradiction_audit.json"
NOTE_PATH = HERE / "GENUS2_SYM12_MASTER_ADAPTER_CONTRADICTION_AUDIT.md"
SCRIPT_PATH = Path(__file__).resolve()
TEST_PATH = ROOT / "tests" / "test_genus2_sym12_master_adapter_contradiction_audit.py"

MAX_SOURCE_FILES = 5
MAX_SOURCE_BYTES_EACH = 45_000
MAX_SOURCE_BYTES_TOTAL = 95_000
MAX_ROW_CHECKS = 3
MAX_OUTPUT_BYTES = 32_768
MAX_WALL_SECONDS = 4.0

SOURCE_LOCKS: tuple[dict[str, object], ...] = (
    {
        "id": "marked_stack_adapter",
        "path": HERE / "genus2_marked_weierstrass_stack_adapter.json",
        "commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
        "git_blob": "79ad36346734bb41f21b570f380ad9d1af86f9ee",
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
        "role": "exact H5//G_tilde groupoid and q*(q-1) trace normalization",
    },
    {
        "id": "sym12_inventory",
        "path": HERE / "genus2_sym12_arithmetic_inventory.json",
        "commit": "70dd4a130e702a2d6df4b0fb96a0182a560009a4",
        "git_blob": "b48963d7b9bc6459046024507a2f2cb8ccbbcd40",
        "lf_sha256": "e966b54fe909570eaac7d9253f635c8067c5f874ed47c9daf485c8fd88bfbd85",
        "payload_sha256": "557ab6465a16bb6080caa2a249c3d0935f8d36fb49bdf54898a0fe72b372496f",
        "schema": "riemann.function_field.genus2_sym12_arithmetic_inventory.v1",
        "role": "exact reciprocal arithmetic and ordered decomposable boundary",
    },
    {
        "id": "sym12_finite_scout",
        "path": HERE / "genus2_sym12_finite_cusp_trace_scout.json",
        "commit": "4a27bc2f96d9995f5657c23624ed731150f3630c",
        "git_blob": "9ee1d3cb82bf896e9479cf096faa0835a31a531c",
        "lf_sha256": "21540da03e0595b119120bf957a6ebaab136a0291525b87335c852a3c5c356b4",
        "payload_sha256": "9fdc8907f9b9c61de5d4e573b04fa6e78024b4c84117db5c4831d552e51086dc",
        "schema": "riemann.function_field.genus2_sym12_finite_cusp_trace_scout.v1",
        "role": "direct raw T_(12,0) rows and explicitly inventory-derived Hhat rows",
    },
    {
        "id": "conditional_closure",
        "path": HERE / "genus2_sym12_conditional_endoscopic_closure.json",
        "commit": "db57a442b124de5d507fb7cbe45b3871d327f576",
        "git_blob": "df308ddf75f55ddd2d4d2164ec3b0711ac75cd3d",
        "lf_sha256": "78a1480fcd7b58a523bb7c43fb6747b57f7d6e57d304d7cfd4d765660db47240",
        "payload_sha256": "40c9667fe38aa6705b63467ece10af1041e5467701970274a2b431361f1cc22f",
        "schema": "riemann.function_field.genus2_sym12_conditional_endoscopic_closure.v2",
        "role": "exact G=0 adapter and source-graded Eisenstein comparison",
    },
    {
        "id": "one_tate_no_go",
        "path": HERE / "genus2_sym12_eisenstein_one_tate_no_go.json",
        "commit": "86be60a01e39651d4501fd704afc664a251f97a8",
        "git_blob": "f6ea61e047b1c3bb152ef52e9e5ea5cda68bbc74",
        "lf_sha256": "d53761f184729e1004e4fcecf42053ce40da6b9d74f0b0935c63321be8fd5ad7",
        "role": "finite constituent localization of the unique [5,1] tensor L defect",
    },
)


@dataclass
class ResourceGuard:
    source_files: int = 0
    source_bytes: int = 0
    row_checks: int = 0

    def source(self, byte_count: int) -> None:
        if (
            isinstance(byte_count, bool)
            or not isinstance(byte_count, int)
            or byte_count < 0
        ):
            raise ValueError("invalid source-byte count")
        if byte_count > MAX_SOURCE_BYTES_EACH:
            raise RuntimeError("source-file byte cap exceeded")
        if self.source_files + 1 > MAX_SOURCE_FILES:
            raise RuntimeError("source-file cap exceeded")
        if self.source_bytes + byte_count > MAX_SOURCE_BYTES_TOTAL:
            raise RuntimeError("total source-byte cap exceeded")
        self.source_files += 1
        self.source_bytes += byte_count

    def row(self) -> None:
        if self.row_checks + 1 > MAX_ROW_CHECKS:
            raise RuntimeError("finite-row cap exceeded")
        self.row_checks += 1


def _canonical_sha256(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _lf_bytes(raw: bytes) -> bytes:
    text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return unicodedata.normalize("NFC", text).encode("utf-8")


def _lf_sha256(raw: bytes) -> str:
    return hashlib.sha256(_lf_bytes(raw)).hexdigest()


def _git_blob(raw: bytes) -> str:
    normalized = _lf_bytes(raw)
    return hashlib.sha1(f"blob {len(normalized)}\0".encode() + normalized).hexdigest()


def _relative(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def _integer(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{label} must be an integer")
    return value


def _load_sources(
    guard: ResourceGuard,
) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    sources: dict[str, dict[str, object]] = {}
    manifest: list[dict[str, object]] = []
    for lock in SOURCE_LOCKS:
        path = lock.get("path")
        source_id = lock.get("id")
        if not isinstance(path, Path) or not isinstance(source_id, str):
            raise TypeError("invalid source lock")
        raw = path.read_bytes()
        guard.source(len(raw))
        if _git_blob(raw) != lock.get("git_blob") or _lf_sha256(raw) != lock.get(
            "lf_sha256"
        ):
            raise ValueError(f"source content drift: {source_id}")
        value = json.loads(_lf_bytes(raw).decode("utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not an object: {source_id}")
        schema = lock.get("schema")
        if schema is not None and value.get("schema") != schema:
            raise ValueError(f"source schema drift: {source_id}")
        expected_payload = lock.get("payload_sha256")
        if expected_payload is not None:
            payload = dict(value)
            claimed = payload.pop("payload_sha256", None)
            if claimed != expected_payload or _canonical_sha256(payload) != claimed:
                raise ValueError(f"source payload drift: {source_id}")
        sources[source_id] = value
        manifest.append(
            {
                key: _relative(item)
                if key == "path" and isinstance(item, Path)
                else item
                for key, item in lock.items()
            }
            | {"bytes_read": len(raw)}
        )
    return sources, manifest


def _validate_exact_arrows(
    sources: Mapping[str, Mapping[str, object]],
) -> dict[str, object]:
    stack = sources["marked_stack_adapter"]
    cardinalities = stack.get("exact_cardinalities")
    trace_theorem = stack.get("trace_theorem")
    if (
        not isinstance(cardinalities, Mapping)
        or not isinstance(trace_theorem, Mapping)
        or cardinalities.get("G_lifted") != "q*(q-1)"
        or trace_theorem.get("generic_groupoid_formula")
        != "Tr_stack,q(V_lambda)=1/(q*(q-1))*sum_D Tr(Frob_D|V_lambda)"
    ):
        raise ValueError("marked-stack normalization changed")

    inventory = sources["sym12_inventory"]
    definitions = inventory.get("definitions")
    dependency = inventory.get("degree_twelve_dependency")
    cubic = inventory.get("cubic_channel")
    quartic = inventory.get("quartic_channel")
    linear = inventory.get("linear_modulus_channel")
    boundary = inventory.get("ambient_boundary")
    ambient = inventory.get("ambient_inventory")
    if not all(
        isinstance(block, Mapping)
        for block in (
            definitions,
            dependency,
            cubic,
            quartic,
            linear,
            boundary,
            ambient,
        )
    ):
        raise TypeError("arithmetic-inventory block is missing")
    if (
        definitions.get("normalization") != "r_D(12)=q^6*chi_(12,0)(U_D)"
        or definitions.get("T_(12,0)")
        != "sum_(D monic squarefree quintic) r_D(12)/(q*(q-1))"
        or dependency.get("preclosure_identity")
        != "T_(12,0)=Hhat_12-(q+1)*G3hat-G4hat+Lambda3hat+Q1hat"
        or dependency.get("marked_open_formula")
        != "T_(12,0)=Hhat_12-2*q-9-4*Theta_Delta-Theta_(8,2)-Theta_(10,2)"
        or cubic.get("repeated_proof")
        != {
            "L^3_per_modulus": "-(q-1)",
            "ordered_L^2*M_per_modulus": "18-6*q",
            "normalized_total": "17-6*q",
        }
        or cubic.get("full_G3_over_q_q_minus_1") != []
        or quartic.get("telescope_verified_in") != "Z[q,a]"
        or linear.get("Q1_over_q_q_minus_1")
        != [
            {
                "coefficient": -9,
                "q_power": 0,
                "Theta_Delta_power": 0,
                "Theta_(8,2)_power": 0,
                "Theta_(10,2)_power": 0,
                "Theta_(14,2)_power": 0,
                "Hhat_12_power": 0,
            },
            {
                "coefficient": 3,
                "q_power": 1,
                "Theta_Delta_power": 0,
                "Theta_(8,2)_power": 0,
                "Theta_(10,2)_power": 0,
                "Theta_(14,2)_power": 0,
                "Hhat_12_power": 0,
            },
        ]
        or boundary.get("geometry") != "A_(1,1)(w^1)=Y_0(2) times A_1"
        or boundary.get("boundary_formula")
        != "11-3*q+4*Theta_Delta+Theta_(8,2)+Theta_(10,2)-q*Theta_(14,Gamma0(2))"
        or ambient.get("formula")
        != "Tr(F_q,e_c(A_2(w^1),V_(12,0)))=Hhat_12+2-5*q-q*Theta_(14,Gamma0(2))(q)"
    ):
        raise ValueError("arithmetic or boundary arrow changed")

    closure = sources["conditional_closure"]
    stable = closure.get("stable_invariant_vanishing_certificate")
    algebra = closure.get("exact_internal_algebra")
    eisenstein = closure.get("nonregular_Eisenstein_specialization")
    if not all(isinstance(block, Mapping) for block in (stable, algebra, eisenstein)):
        raise TypeError("conditional-closure block is missing")
    discrepancy = eisenstein.get("later_source_discrepancy")
    one_tate = algebra.get("one_Tate_discrepancy_effect")
    if (
        stable.get("exact_conclusion") != "Genuine=0"
        or not isinstance(discrepancy, Mapping)
        or discrepancy.get("Shmakov_printed_specialization") != "2-4*L"
        or discrepancy.get("missing_channel")
        != "one [5,1] tensor L copy tied to the unique Fricke-positive weight-16 level-2 newform"
        or not isinstance(one_tate, Mapping)
        or one_tate.get("if_Eisenstein_is_2_minus_4L_and_Genuine_is_zero", {}).get(
            "equality_iff"
        )
        != "Hhat_12=L-L*f_minus"
    ):
        raise ValueError("cohomological comparison arrow changed")

    no_go = sources["one_tate_no_go"]
    localization = no_go.get("exact_localization")
    proof_grade = no_go.get("proof_grade")
    if (
        not isinstance(localization, Mapping)
        or not isinstance(proof_grade, Mapping)
        or localization.get("unique_difference") != "[5,1] tensor L"
        or localization.get("natural_S5_fixed_dimension_of_unique_difference") != 1
        or "does not give a satisfactory full justification"
        not in str(proof_grade.get("source_caveated_galois"))
    ):
        raise ValueError("one-Tate localization or source caveat changed")

    return {
        "stack_group_order": "q*(q-1)",
        "local_system_normalization": "r_D(12)=q^6*chi_(12,0)(U_D)",
        "reciprocal_preclosure": dependency["preclosure_identity"],
        "cubic_rows": "G3hat=0; repeated Lambda3hat=17-6*q",
        "quartic_row": "G4hat=Theta_Delta",
        "linear_row": "Q1hat=3*q-9",
        "marked_open_formula": dependency["marked_open_formula"],
        "ordered_boundary": boundary["boundary_formula"],
        "ambient_formula": ambient["formula"],
        "stable_channel": "Genuine=0",
        "all_statuses": "PASS",
    }


def _finite_contradiction(
    sources: Mapping[str, Mapping[str, object]], guard: ResourceGuard
) -> list[dict[str, object]]:
    scout = sources["sym12_finite_scout"]
    provenance = scout.get("provenance_boundary")
    rows = scout.get("finite_rows")
    if (
        not isinstance(provenance, Mapping)
        or "not an independent audit" not in str(provenance.get("logical_use"))
        or not isinstance(rows, list)
    ):
        raise ValueError("finite-scout provenance changed")
    closure_rows = (
        sources["conditional_closure"].get("finite_scout_corroboration", {}).get("rows")
    )
    if not isinstance(closure_rows, list):
        raise TypeError("closure finite rows are missing")
    closure_by_p = {
        row.get("p"): row for row in closure_rows if isinstance(row, Mapping)
    }
    result = []
    for row in rows:
        if not isinstance(row, Mapping):
            raise TypeError("finite scout row is invalid")
        p = _integer(row.get("q"), "q")
        t12 = _integer(row.get("T_(12,0)"), "T_(12,0)")
        hhat = _integer(row.get("Hhat_12"), "Hhat_12")
        coefficient = _integer(row.get("a_p(f_-)"), "a_p(f_-)")
        traces = row.get("modular_traces")
        if not isinstance(traces, Mapping):
            raise TypeError("modular trace row is missing")
        delta = _integer(traces.get("Theta_Delta"), "Theta_Delta")
        f8 = _integer(traces.get("Theta_(8,2)"), "Theta_(8,2)")
        g10 = _integer(traces.get("Theta_(10,2)"), "Theta_(10,2)")
        guard.row()
        derived_hhat = t12 + 2 * p + 9 + 4 * delta + f8 + g10
        raw_residual = t12 + 9 + p + 4 * delta + f8 + g10 + p * coefficient
        closure_row = closure_by_p.get(p)
        if (
            derived_hhat != hhat
            or raw_residual != -p
            or not isinstance(closure_row, Mapping)
            or closure_row.get("raw_T_plus_inventory_project_minus_Shmakov_target")
            != raw_residual
            or row.get("Hhat_12_provenance")
            != "derived from replayed T_(12,0) by the source-locked Sym12 arithmetic inventory; not a direct Q_5 average"
        ):
            raise ArithmeticError("finite raw-T contradiction changed")
        result.append(
            {
                "p": p,
                "direct_T_(12,0)": t12,
                "inventory_derived_Hhat_12": hhat,
                "a_p(f_minus)": coefficient,
                "project_minus_Shmakov_from_raw_T_plus_inventory": raw_residual,
                "Shmakov_required_minus_arithmetic_branch": -raw_residual,
            }
        )
    if [row["p"] for row in result] != [3, 5, 7]:
        raise ValueError("finite support changed")
    return result


def _packet_manifest() -> list[dict[str, str]]:
    return [
        {"path": _relative(path), "sha256_lf_normalized": _lf_sha256(path.read_bytes())}
        for path in (NOTE_PATH, SCRIPT_PATH, TEST_PATH)
    ]


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    guard = ResourceGuard()
    sources, source_manifest = _load_sources(guard)
    exact_arrows = _validate_exact_arrows(sources)
    finite_rows = _finite_contradiction(sources, guard)
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym12_master_adapter_contradiction_audit.v1",
        "status": "EXACT_SOURCE_RELATIVE_THREE_PRIME_CONTRADICTION_LOCALIZATION",
        "scope": {
            "base_fields_for_exact_adapters": "all odd prime powers",
            "finite_contradiction_support": [3, 5, 7],
            "all_q_cohomological_correction": "NOT_PROVED",
            "field_or_curve_enumeration": "NONE",
        },
        "source_manifest": source_manifest,
        "exact_arrow_audit": exact_arrows,
        "finite_raw_T_contradiction": {
            "identity": (
                "T_(12,0)(p)+9+p+4*Theta_Delta(p)+Theta_(8,2)(p)+"
                "Theta_(10,2)(p)+p*a_p(f_minus)=-p"
            ),
            "rows": finite_rows,
            "provenance": (
                "T_(12,0) is replayed directly; conversion to Hhat_12 and the raw-T "
                "comparison both use the exact arithmetic inventory"
            ),
            "not_independent_of_inventory": True,
        },
        "smallest_unproved_arrow": {
            "arrow": (
                "Shmakov displayed formal associated-graded Tate ledger -> actual "
                "compact-support Galois Frobenius Euler class on A_2(w^1)"
            ),
            "reason": (
                "the arithmetic, q*(q-1) stack normalization, ordered boundary, and "
                "semisimplified stable-channel vanishing all survive the audit"
            ),
            "source_caveat": (
                "Shmakov explicitly does not fully justify the Galois action on the "
                "displayed Eisenstein cohomology"
            ),
        },
        "unique_formal_repair_within_displayed_ledger": {
            "carrier": "[5,1] tensor L",
            "location": "weight-16 Fricke-positive level-2 Siegel block in H_c^3",
            "effect_on_Eisenstein_projection": "2-4*L -> 2-5*L",
            "effect_on_master_relation_when_G_zero": (
                "Hhat_12=L-L*f_minus -> Hhat_12=-L*f_minus"
            ),
            "grade": (
                "unique formal carrier correction and forced trace correction at "
                "p=3,5,7 only; not an all-q Galois or motivic theorem"
            ),
        },
        "verdict": (
            "No missing Tate occurs in the arithmetic inventory, q*(q-1) stack "
            "normalization, or marked open-to-ambient boundary. The exact finite "
            "conflict is localized to the source-caveated cohomological realization."
        ),
        "firewalls": [
            "PROVENANCE FIREWALL: the scout directly computes T_(12,0), not H_12; its Hhat_12 and H_12 rows are inventory-derived.",
            "FINITE FIREWALL: residuals -3,-5,-7 do not prove the correction at a fourth q or at prime powers.",
            "GALOIS FIREWALL: the unique [5,1] tensor L repair is forced only inside the displayed constituent ledger and at the three trace rows; no actual all-q Galois Euler class is constructed.",
            "SCOPE FIREWALL: no motive, compatible system, novelty, RH/GRH, or global Euler-product claim is made.",
        ],
        "resource_contract": {
            "source_files": {"maximum": MAX_SOURCE_FILES, "actual": guard.source_files},
            "source_bytes": {
                "maximum_each": MAX_SOURCE_BYTES_EACH,
                "maximum_total": MAX_SOURCE_BYTES_TOTAL,
                "actual_total": guard.source_bytes,
            },
            "finite_row_checks": {
                "maximum": MAX_ROW_CHECKS,
                "actual": guard.row_checks,
            },
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "runtime_external_access": "NONE",
        },
        "packet_manifest": _packet_manifest(),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    if len(_serialized(payload).encode("utf-8")) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output byte cap exceeded")
    return payload


def _serialized(value: Mapping[str, object]) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args(argv)
    rendered = _serialized(build_fixture())
    if args.check:
        if (
            not args.output.is_file()
            or args.output.read_text(encoding="utf-8") != rendered
        ):
            raise SystemExit("canonical contradiction-audit fixture drifted")
        print(f"verified {args.output}")
        return 0
    args.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
