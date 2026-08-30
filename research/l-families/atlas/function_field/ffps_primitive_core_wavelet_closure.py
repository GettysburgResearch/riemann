#!/usr/bin/env python3
"""Exact bounded replay for the full primitive-panel core-wavelet reduction.

The replay authenticates finite algebra only. It does not prove COREWAVE,
PRIMCAR, PRIMLS, RH, or GRH.
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

from _ffps_core_wavelet_costs import (  # noqa: E402
    assembly_cost_replay,
    inverse_assembly_cost_replay,
)
from _ffps_core_wavelet_replay import panel_replay, support_replay  # noqa: E402

ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md"
SOURCE_COMMIT = "b870366141fe8d5f43d5b81f6e50a67d2a888070"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md"
    ): "2abd49b975837c924009e33912e786b4b720e29c",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md"
    ): "722ca5bd8acef2efdb5591f29935b4f97102f957",
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_RHO_TILT_CONVOLUTION_ISOMORPHISM.md"
    ): "31311893b8a7ba708ae7a2813b9c44b920b788a9",
}


def check_source_blobs() -> None:
    """Pin the exact PR #757 theorem files extended by this packet."""
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
        "the entire primitive panel, not only its harmonic zero mode",
        "COREWAVE is open",
        "strictly stronger sufficient theorem",
        "COREAGG and PRIMCAR are equivalent",
        "No PRIMCAR, PRIMLS, RH, or GRH estimate is proved",
        "Architecture A only",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing from note: {marker}")


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    return {
        "architecture": "A: direct beta/primitive-pair route",
        "exact_theorems": {
            "full_primitive_product_shell": True,
            "full_primitive_core_wavelet": True,
            "core_divisor_inverse": True,
            "corewave_implies_primcar": "proved conditionally in the note",
            "coreagg_equivalent_to_primcar": "proved at all-epsilon scale in the note",
            "primcar_implies_rh": "imported from the frozen PR #757 chain",
        },
        "finite_replay": panel_replay(),
        "support_replay": support_replay(),
        "assembly_cost_replay": assembly_cost_replay(),
        "inverse_assembly_cost_replay": inverse_assembly_cost_replay(),
        "open_gate": {
            "COREWAVE": (
                "sum_(I in D_H)|Z_I^alpha(r)|^2 <<_eta (2Hr)^eta "
                "uniformly for alpha=0,1,2 and squarefree 67-free r"
            ),
            "COREAGG": (
                "sum_r tau(r)/r^2 sum_I |Z_I^alpha(r)|^2 "
                "<<_epsilon (2H)^epsilon"
            ),
        },
        "scope_firewall": {
            "corewave_proved": False,
            "coreagg_estimate_proved": False,
            "coreagg_primcar_equivalence_proved": True,
            "primcar_proved": False,
            "primls_proved": False,
            "rh_or_grh_proved": False,
            "controls_entire_primitive_panel_algebraically": True,
            "architecture_b_claims": False,
        },
        "source_contract": {
            "commit": SOURCE_COMMIT,
            "git_blobs": SOURCE_BLOBS,
        },
        "resource_caps": {
            "largest_height_endpoint": 5000,
            "largest_cost_limit": 120,
            "zeta_zeros": 0,
            "primes_scanned": 0,
            "finite_fields": 0,
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
