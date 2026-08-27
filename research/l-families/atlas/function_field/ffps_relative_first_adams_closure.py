#!/usr/bin/env python3
"""Exact bounded replay for relative-first closed-point Adams extraction.

This authenticates finite cyclic character algebra and closed-point Möbius
inversion only. It does not construct the native FFPS adapter, prove a
uniform trace estimate, or prove RH/GRH.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _ffps_relative_adams_characters import character_algebra_replay  # noqa: E402
from _ffps_relative_adams_closed_points import closed_point_replay  # noqa: E402

ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_RELATIVE_FIRST_ADAMS_CLOSURE.md"
SOURCE_COMMIT = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_CYCLIC_TORSOR_RELATIVE_PROJECTOR.md"
    ): "ab16e6c0894e51303119692e67b2f2bf59ba73e4",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_CLOSED_POINT_ADAMS_COMPRESSION.md"
    ): "c79e52ebf0099fe416bc2c79dcb041cc21e025fb",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_TERNARY_UNIVERSAL_NORM_TORSOR.md"
    ): "21645bdb609320cf176893aa589af7a17c741d9a",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRINCIPAL_ANOMALY_TRANSFER_DICHOTOMY.md"
    ): "47c148187db578357035926f8ff12419b0cf3652",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_CYCLIC_CLOSURE_BUDGET.md"
    ): "b576c8a114d7e502b9b474cfed0db7e4cf6e2475",
}


def check_source_blobs() -> None:
    for path, expected in SOURCE_BLOBS.items():
        frozen = subprocess.run(
            ["git", "rev-parse", f"{SOURCE_COMMIT}:{path}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if frozen != expected:
            raise RuntimeError(f"frozen source blob mismatch: {path}")
        working = subprocess.run(
            ["git", "hash-object", path],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        ).stdout.strip()
        if working != expected:
            raise RuntimeError(f"working source blob mismatch: {path}")


def check_scope_markers() -> None:
    note = NOTE_PATH.read_text(encoding="utf-8")
    for marker in (
        "subtract before Adams extraction",
        "only the relative class needs partial Frobenius",
        "four physical parity profiles",
        "the non-deck Frobenius eigenvalues still depend on the full exponents",
        "Architecture B only",
        "No native source adapter, uniform trace estimate, RH, or GRH is proved",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing from note: {marker}")


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "B: family/sheaf amplification route",
        "character_algebra": character_algebra_replay(),
        "closed_point_adams": closed_point_replay(),
        "exact_theorems": {
            "relative_first_identity": (
                "psi_1^e psi_2^f(C-S)=psi_1^e psi_2^f(R) for every e,f"
            ),
            "relative_only_partial_frobenius_suffices": True,
            "clean_physical_deck_profiles": 4,
            "clean_relative_weighted_line_mass": 16,
            "closed_point_extractor_applies_directly_to_relative_class": True,
        },
        "open_gates": {
            "NATREL": (
                "construct the complete owner/Boolean/Artin-Schreier/incidence/Wick "
                "source as one common relative projector object"
            ),
            "RELPARTFROB": (
                "show the resulting relative class is separable or has commuting "
                "partial Frobenii"
            ),
            "RELTRACE": (
                "prove a conductor-uniform signed trace/Betti estimate after the "
                "double Adams-Mobius recombination"
            ),
            "PRINCIPAL_BINDING": (
                "identify the extracted relative trace with the native principal "
                "consumer at every horizon and normalization"
            ),
        },
        "scope_firewall": {
            "native_source_adapter_constructed": False,
            "relative_partial_frobenius_proved": False,
            "uniform_betti_or_trace_estimate_proved": False,
            "principal_binding_proved_for_new_object": False,
            "rh_or_grh_proved": False,
            "physical_profiles_do_not_control_non_deck_adams_eigenvalues": True,
            "architecture_a_claims": False,
        },
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "resource_caps": {
            "adams_exponent_limit": 12,
            "closed_point_degree_limit": 12,
            "finite_fields": 0,
            "curves": 0,
            "conductors": 0,
            "l_functions": 0,
            "zeta_zeros": 0,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--no-source-lock", action="store_true")
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(
        run(check_sources=not args.no_source_lock), indent=2, sort_keys=True
    ) + "\n"
    canonical = Path(__file__).with_suffix(".json")
    if args.check and (
        not canonical.exists() or canonical.read_text(encoding="utf-8") != rendered
    ):
        raise SystemExit("canonical JSON fixture is stale")
    if args.write_json:
        args.write_json.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
