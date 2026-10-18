#!/usr/bin/env python3
"""Fresh exact replay, optimized equality, and executed corruptions."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
CORRUPTIONS = (
    ("omit_overlap_assignment", "complete_mask_factorization"),
    ("drop_mode_center", "centered_mode_real_identity"),
    ("drop_balance_gamma", "linear_balance_reconstruction"),
    ("include_square_endpoint", "strict_square_endpoint"),
    ("drop_q1_mode", "complete_denominator_native_reconstruction"),
    ("delete_above_output_products", "above_output_product_retention"),
    ("impose_coprime_inputs", "complete_ordered_product_fibers"),
    ("omit_final_cell", "complete_square_step_cell_count"),
    ("duplicate_core_sector", "three_sector_complete_centering"),
)


def need(ok, label):
    if not ok:
        raise RuntimeError(label)


def run(args):
    return subprocess.run([sys.executable, "-B", *args], cwd=HERE,
                          capture_output=True, text=True)


def main():
    ordinary = run(["verify.py"])
    optimized = run(["-O", "verify.py"])
    need(ordinary.returncode == 0, "ordinary checker: " + ordinary.stderr)
    need(optimized.returncode == 0, "optimized checker: " + optimized.stderr)
    need(ordinary.stdout == optimized.stdout, "ordinary/optimized mismatch")
    report = json.loads(ordinary.stdout)
    need(report["status"] == "PASS", "checker status")
    need(report["total_cells"] == 30602, "declared complete-cell coverage")
    need(report["rho"] == "5/8", "declared rational cutoff")
    (HERE / "CHECKS.json").write_text(ordinary.stdout)
    rejected = []
    for mutation, gate in CORRUPTIONS:
        proc = run(["-O", "verify.py", "--mutation", mutation])
        need(proc.returncode != 0, "accepted corruption: " + mutation)
        need("REJECT:" + gate in proc.stderr,
             "wrong corruption gate: " + mutation + proc.stderr)
        rejected.append({"mutation": mutation, "expected_gate": gate,
                         "exit_code": proc.returncode, "rejected": True})
    receipt = {
        "status": "PASS",
        "normal_optimized_identical": True,
        "report_sha256": hashlib.sha256(ordinary.stdout.encode()).hexdigest(),
        "predicates": report["predicates"],
        "complete_cells": report["total_cells"],
        "separately_executed_optimized_corruptions": rejected,
        "scope": "Exact finite source algebra and declared coverage, not infinite analytic certification",
    }
    (HERE / "REPLAY.json").write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")
    print(json.dumps(receipt, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
