#!/usr/bin/env python3
"""Exact bounded replay for the primitive core shared-divisor Gram."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from _ffps_core_gcd_gram_replay import run_replays  # noqa: E402

ROOT = HERE.parents[3]
NOTE_PATH = HERE / "FFPS_PRIMITIVE_CORE_GCD_GRAM_CLOSURE.md"
SOURCE_COMMIT = "aaccfe767c3d36a353056c9a2483e3824d89949f"
SOURCE_BLOBS = {
    (
        "research/l-families/atlas/function_field/"
        "FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md"
    ): "af735a493a5c74b7158c314079dbf4b72ee11b46",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_core_wavelet_closure.py"
    ): "e5aa81db7f574fe50a662b6356e0f67dcf0ac386",
    (
        "research/l-families/atlas/function_field/"
        "ffps_primitive_core_wavelet_closure.json"
    ): "71a0581d1b2629304258e5660b93a46e3fa082c1",
    "tests/test_ffps_primitive_core_wavelet_closure.py": (
        "d89cc149c269276492a91336051a9de6dd253593"
    ),
    (
        "research/l-families/atlas/function_field/"
        "_ffps_core_wavelet_arithmetic.py"
    ): "14e9e86fadcf4974ec9d3007aa527a120a19b101",
    (
        "research/l-families/atlas/function_field/"
        "_ffps_core_wavelet_panels.py"
    ): "549404d16e1b77340e2d2b365f78010eb505e478",
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
        "The diagonal is unconditionally paid",
        "OFFGCDWAVE",
        "outer core has no Möbius sign",
        "condition number is asymptotic to `2p`",
        "Architecture A only",
        "No OFFGCDWAVE, COREAGG, PRIMCAR, PRIMLS, RH, or GRH estimate is proved",
    ):
        if marker not in note:
            raise RuntimeError(f"scope marker missing from note: {marker}")


def run(*, check_sources: bool = True) -> dict[str, object]:
    if check_sources:
        check_source_blobs()
    check_scope_markers()
    replays = run_replays()
    return {
        "architecture": "A: direct beta/primitive-pair route",
        "diagonal_theorem": {
            "status": "proved unconditionally",
            "bound": "D_alpha(H) << L_H (1+log(4H^2+2))^12",
        },
        **replays,
        "exact_theorems": {
            "shared_divisor_gram": True,
            "kernel_positive_definite": True,
            "diagonal_subpower": True,
            "exact_gcd_decomposition": True,
            "offgcdwave_equivalent_to_coreagg": True,
            "coreagg_equivalent_to_primcar": "imported from frozen predecessor",
        },
        "open_gate": {
            "OFFGCDWAVE": (
                "absolute subpower bound for the N!=M signed shared-divisor "
                "wavelet correlation in all three alpha channels"
            )
        },
        "scope_firewall": {
            "offgcdwave_proved": False,
            "coreagg_proved": False,
            "primcar_proved": False,
            "primls_proved": False,
            "rh_or_grh_proved": False,
            "architecture_b_claims": False,
        },
        "source_contract": {"commit": SOURCE_COMMIT, "git_blobs": SOURCE_BLOBS},
        "resource_caps": {
            "largest_height_endpoint": 134,
            "feature_support_size": 8,
            "finite_fields": 0,
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


if __name__ == "__main__":
    main()
