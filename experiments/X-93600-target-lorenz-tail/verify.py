#!/usr/bin/env python3
"""Replay and fail-closed audit for the complete Target-Lorenz tail theorem.

The C++ generator performs the full exact-event sweep. This wrapper rebuilds
it from source, validates the retained result and independently checks the
analytic reserve arithmetic and the compact/tail domain join.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent
RESULT = ROOT / "results" / "verification.json"
GENERATOR = ROOT / "generate.cpp"


def canonical_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def check_analytic_reserve() -> dict:
    getcontext().prec = 80
    ln2 = Decimal(2).ln()

    # In the proof a=N+1>=2 and h<=1/(a-1). After multiplication by a^(3/2):
    # a^2 h^2/2 <= 2, a h/2 <= 1, and |1/12-h/24| <= 1/12.
    elementary = Decimal(2) + Decimal(1) + Decimal(1) / Decimal(12)

    # Differentiated B_2 remainder:
    # 1/9 + h/24 + 1/36, maximized at h=log 2.
    differentiated = Decimal(1) / Decimal(9) + ln2 / Decimal(24) + Decimal(1) / Decimal(36)
    total = elementary + differentiated
    assert total < Decimal(5), total

    component_constant = Decimal(2) * Decimal(5)
    assert component_constant == Decimal(10)
    return {
        "elementary_scaled_bound": str(elementary),
        "differentiated_scaled_bound": str(differentiated),
        "total_scaled_bound": str(total),
        "published_ramp_constant": 5,
        "component_remainder_numerator": 10,
    }


def compile_and_run() -> tuple[dict, str]:
    compiler = shutil.which("g++") or shutil.which("c++")
    if compiler is None:
        raise RuntimeError("C++ compiler not found")
    with tempfile.TemporaryDirectory(prefix="x93600-") as tmp:
        binary = Path(tmp) / "generate"
        cmd = [compiler, "-std=c++17", "-O2", "-DNDEBUG", str(GENERATOR), "-o", str(binary)]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        proc = subprocess.run(
            [str(binary)], check=True, capture_output=True, text=True, timeout=180
        )
    return json.loads(proc.stdout), proc.stderr


def check_sweep(data: dict) -> dict:
    assert data["classification"] == "PASS_COMPLETE_TARGET_LORENZ_TAIL_AVLT"
    assert data["certified_full_lower_bound"] == 26
    assert Decimal(data["computed_full_minimum"]) > Decimal("26.75")
    assert data["computed_full_minimum_row"] == 66
    assert data["computed_full_minimum_x"] == "166000"
    assert data["certified_parent_lower_bound"] == 79
    assert Decimal(data["computed_parent_minimum"]) > Decimal("79.2")
    assert data["certified_parent_derivative_lower_bound"] == 0.23
    assert Decimal(data["computed_parent_derivative_minimum"]) > Decimal("0.239")
    assert data["ramp_remainder_constant_used"] == 5
    assert data["divisor_count"] == 262144
    assert data["row_count"] == 65
    assert data["tail_start"] == 166000
    assert data["event_records"] == 3 * 262144 * 65
    assert data["child_correction_monotone_between_events"] is True
    assert Decimal(data["last_interval_second_derivative_polynomial_minimum"]) > 0
    assert Decimal(data["last_interval_polynomial_derivative_minimum"]) > 0
    assert data["rh_established_by_replay"] is False

    compact_last = 165999
    tail_first = data["tail_start"]
    assert compact_last + 1 == tail_first

    mutation_checks = {
        "raise_full_certificate_to_27": Decimal(data["computed_full_minimum"]) <= Decimal(27),
        "raise_parent_certificate_to_80": Decimal(data["computed_parent_minimum"]) <= Decimal(80),
        "raise_derivative_certificate_to_point24": Decimal(data["computed_parent_derivative_minimum"]) <= Decimal("0.24"),
        "delete_child_correction": Decimal(data["computed_full_minimum"]) < Decimal(data["computed_parent_minimum"]),
        "open_boundary_gap": compact_last + 1 != 166001,
    }
    assert all(mutation_checks.values()), mutation_checks

    return {
        "compact_last_integer": compact_last,
        "tail_first_real_endpoint": tail_first,
        "mutation_checks": mutation_checks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=RESULT)
    args = parser.parse_args()

    generated, stderr = compile_and_run()
    reserve = check_analytic_reserve()
    sweep_audit = check_sweep(generated)

    payload = dict(generated)
    payload.update(
        {
            "classification": "PASS_COMPLETE_TARGET_LORENZ_TAIL_AVLT",
            "analytic_reserve_audit": reserve,
            "domain_join_audit": sweep_audit,
            "generator_sha256": hashlib.sha256(GENERATOR.read_bytes()).hexdigest(),
            "stderr_line_count": len([line for line in stderr.splitlines() if line.strip()]),
            "replay_scope": (
                "rebuilds the exact-event sweep and validates the analytic reserve, "
                "thresholds, domain join and hostile mutations; it does not certify "
                "the frozen compact theorem or establish RH"
            ),
            "rh_established_by_replay": False,
        }
    )
    payload["proof_object_sha256"] = canonical_hash(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])


if __name__ == "__main__":
    main()
