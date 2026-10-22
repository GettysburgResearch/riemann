"""Generate the exact, lightweight GL(2) deflation control report."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from deflation import (
    CONVENTIONS,
    LOEWNER_DIFFERENCE,
    add,
    central_atom,
    correction_norm_squared,
    determinant,
    determinant_affine_prediction,
    frobenius_norm_squared,
    make_packet,
    matrix_summary,
    rank,
    subtract,
)


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "synthetic_controls.json"


def _packet(control: dict[str, Any], convention: str):
    return make_packet(
        nodes=control["nodes"],
        root_number=control["root_number"],
        central_order=control["central_order"],
        c=control["background"]["c"],
        d=control["background"]["d"],
        convention=convention,
    )


def _same(left, right) -> bool:
    return left == right


def _rank_one_inertia_check(left, right) -> bool:
    a = matrix_summary(left)["inertia"]
    b = matrix_summary(right)["inertia"]
    return (
        abs(a["positive"] - b["positive"]) <= 1
        and abs(a["negative"] - b["negative"]) <= 1
    )


def build_report() -> dict[str, Any]:
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    output: dict[str, Any] = {
        "schema": "gl2-deflation-verification-v1",
        "status": "EXACT_RATIONAL_SYNTHETIC_CONTROL_ONLY",
        "kernel_conventions": {
            "loewner_difference": "(F(x)-F(y))/(x-y); central atom -r/(xy)",
            "pick_sum": "(F(x)+F(y))/(x+y); central atom +r/(xy)",
        },
        "controls": [],
    }

    for control in fixture["controls"]:
        if "expected_error" in control:
            for convention in CONVENTIONS:
                try:
                    _packet(control, convention)
                except ValueError as exc:
                    if str(exc) != control["expected_error"]:
                        raise AssertionError(
                            f"{control['id']}: wrong fail-closed error: {exc}"
                        ) from exc
                else:
                    raise AssertionError(
                        f"{control['id']}: parity mismatch was not rejected"
                    )
            output["controls"].append(
                {
                    "id": control["id"],
                    "label": control["label"],
                    "result": "EXPECTED_ERROR_CONFIRMED",
                    "error": control["expected_error"],
                }
            )
            continue

        record: dict[str, Any] = {
            "id": control["id"],
            "label": control["label"],
            "root_number": control["root_number"],
            "central_order": control["central_order"],
            "conventions": {},
        }
        for convention in CONVENTIONS:
            packet = _packet(control, convention)
            excess_atom = central_atom(
                packet.nodes, packet.excess_order, convention
            )
            forced_atom = central_atom(
                packet.nodes, packet.forced_order, convention
            )
            full_atom = central_atom(
                packet.nodes, packet.central_order, convention
            )

            if not _same(packet.fully_deflated, packet.background):
                raise AssertionError(f"{control['id']}: full deflation failed")
            if not _same(
                packet.parity_deflated, add(packet.background, excess_atom)
            ):
                raise AssertionError(
                    f"{control['id']}: parity residual identity failed"
                )
            if not _same(subtract(packet.raw, packet.parity_deflated), forced_atom):
                raise AssertionError(f"{control['id']}: forced atom identity failed")
            if determinant(packet.raw) != determinant_affine_prediction(
                packet.background,
                packet.nodes,
                packet.central_order,
                convention,
            ):
                raise AssertionError(f"{control['id']}: determinant law failed")
            if rank(full_atom) != (1 if packet.central_order else 0):
                raise AssertionError(f"{control['id']}: atom rank failed")
            if not _rank_one_inertia_check(packet.raw, packet.background):
                raise AssertionError(f"{control['id']}: inertia bound failed")

            raw_correction = subtract(packet.raw, packet.fully_deflated)
            parity_correction = subtract(
                packet.parity_deflated, packet.fully_deflated
            )
            if frobenius_norm_squared(raw_correction) != correction_norm_squared(
                packet.nodes, packet.central_order
            ):
                raise AssertionError(f"{control['id']}: full norm law failed")
            if frobenius_norm_squared(parity_correction) != correction_norm_squared(
                packet.nodes, packet.excess_order
            ):
                raise AssertionError(f"{control['id']}: excess norm law failed")

            record["conventions"][convention] = {
                "atom_sign": -1 if convention == LOEWNER_DIFFERENCE else 1,
                "forced_order": packet.forced_order,
                "excess_order": packet.excess_order,
                "central_atom_rank": rank(full_atom),
                "raw": matrix_summary(packet.raw),
                "parity_deflated": matrix_summary(packet.parity_deflated),
                "fully_deflated": matrix_summary(packet.fully_deflated),
                "raw_minus_full_frobenius_squared": str(
                    correction_norm_squared(packet.nodes, packet.central_order)
                ),
                "parity_minus_full_frobenius_squared": str(
                    correction_norm_squared(packet.nodes, packet.excess_order)
                ),
            }
        output["controls"].append(record)
    output["result"] = "PASS"
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", type=Path, help="write the deterministic verification report")
    parser.add_argument("--check", type=Path, help="compare against a checked-in report")
    args = parser.parse_args()
    if args.write and args.check:
        parser.error("--write and --check are mutually exclusive")
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(rendered, encoding="utf-8")
        print(f"OK: wrote exact GL(2) report {args.write}")
        return
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if report != expected:
            raise SystemExit(f"verification report mismatch: {args.check}")
        print(f"OK: exact GL(2) report matches {args.check}")
        return
    print(rendered, end="")


if __name__ == "__main__":
    main()
