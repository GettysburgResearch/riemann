#!/usr/bin/env python3
"""Exact Fraction verifier for the L-15632 joint-profile direct-short bound."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def q(obj: dict[str, str]) -> Fraction:
    return Fraction(int(obj["numerator"]), int(obj["denominator"]))


def qout(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def det2(a: Fraction, b: Fraction, d: Fraction) -> Fraction:
    return a * d - b * b


def psd2(a: Fraction, b: Fraction, d: Fraction) -> bool:
    return a >= 0 and d >= 0 and det2(a, b, d) >= 0


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    L = q(data["log_scale"])
    tau = q(data["tau"])
    eps = q(data["relative_error"])
    G = q(data["G"])
    M = q(data["M"])

    Dss = q(data["profile"]["ss"])
    Des = q(data["profile"]["es"])
    Dee = q(data["profile"]["ee"])
    Wss = q(data["remainder"]["ss"])
    Wes = q(data["remainder"]["es"])
    Wee = q(data["remainder"]["ee"])

    if min(L, tau, G, M, Dee) <= 0:
        raise ValueError("positive scalar gate failed")
    if eps < 0 or eps > Fraction(1, 4):
        raise ValueError("relative error must lie in [0,1/4]")
    if tau > Fraction(1, 2):
        raise ValueError("tau must be <=1/2")
    if not psd2(Dss, Des, Dee):
        raise ValueError("joint profile Gram is not PSD")
    if Dss > 2 * tau * G:
        raise ValueError("declared soft profile gate failed")

    # Dhat = D + tau diag(G, Dee).  The ambient regularizer uses the
    # actual main profile metric, as in L-15632.
    Hss = Dss + tau * G
    Hes = Des
    Hee = Dee * (1 + tau)
    radius = eps * L

    # Check -radius Dhat <= W <= radius Dhat.
    if not psd2(radius * Hss - Wss, radius * Hes - Wes, radius * Hee - Wee):
        raise ValueError("upper relative remainder LMI failed")
    if not psd2(radius * Hss + Wss, radius * Hes + Wes, radius * Hee + Wee):
        raise ValueError("lower relative remainder LMI failed")

    Ass = L * Dss + Wss
    Aes = L * Des + Wes
    Aee = L * Dee + Wee
    if Aee <= 0:
        raise ValueError("ambient block is not positive")

    short = Ass - Aes * Aes / Aee
    negative_part = max(Fraction(0), -short / G)
    theorem_bound = 4 * (eps + 4 * eps * eps) * L * tau
    if negative_part > theorem_bound:
        raise ValueError("negative part exceeds theorem bound")

    X0 = Des / Dee
    residual = Aes - Aee * X0
    trial_energy = Ass - 2 * Aes * X0 + Aee * X0 * X0
    direct_identity = trial_energy - residual * residual / Aee
    if direct_identity != short:
        raise ValueError("direct-short identity mismatch")

    return {
        "schema": "riemann.x15613-joint-soft-short.result.v1",
        "classification": "EXACT_JOINT_PROFILE_SOFT_SHORT_BOUND_PASSES",
        "certificate_sha256": sha256(path),
        "main_profile_schur": qout(Dss - Des * Des / Dee),
        "trial_profile_solve": qout(X0),
        "actual_solve_residual": qout(residual),
        "exact_shorted_value": qout(short),
        "normalized_negative_part": qout(negative_part),
        "theorem_upper_bound": qout(theorem_bound),
        "verdict": "PASS_EXACT_L15632_DIRECT_SHORT_LMI",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    result = verify(args.certificate)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
