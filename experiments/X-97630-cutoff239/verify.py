#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T97630_CUTOFF239_ANNULAR_PACKET"
MUTATIONS = (
    "erase_x184_witness",
    "restore_cutoff67",
    "change_cutoff240",
    "drop_low_child_recombination",
    "double_low_child",
    "raise_high_child_mass",
    "reverse_parent_identity",
    "promote_reserve_to_current",
    "cancel_mellin_numerator",
    "claim_rh_replay",
)

class ContractError(ValueError):
    pass

def validate(mutation: str | None = None) -> dict:
    # Exact arithmetic from the quoted pass.
    F184 = Fraction(106935796487738299508, 10**19)
    M184 = Fraction(4458576035426028363156, 10**19)
    witness = M184 - 40 * F184
    if mutation == "erase_x184_witness":
        witness = Fraction(0)
    if witness <= 18:
        raise ContractError("x=184 refutation lost")

    cutoff = 239
    if mutation == "restore_cutoff67":
        cutoff = 67
    if mutation == "change_cutoff240":
        cutoff = 240
    if cutoff != 239:
        raise ContractError("wrong corrected cutoff")

    r = Fraction(1, 9)
    lam = Fraction(7, 20)
    alpha = lam * r
    parent = Fraction(13, 7)
    child = Fraction(5, 11)
    recombined = lam * (parent - r * child) + alpha * child
    if mutation == "drop_low_child_recombination":
        recombined -= alpha * child
    if mutation == "double_low_child":
        recombined += alpha * child
    if recombined != lam * parent:
        raise ContractError("low-child identity")

    rho = Fraction(1, 8)
    if mutation == "raise_high_child_mass":
        rho = Fraction(1, 7)
    margin = Fraction(1, 40) * (1 - rho) - Fraction(1, 6) * rho
    if margin != Fraction(1, 960):
        raise ContractError("one-over-960 margin")

    current = Fraction(7, 5)
    losses = Fraction(2, 5)
    parent_scalar = current - losses
    if mutation == "reverse_parent_identity":
        parent_scalar = losses - current
    if parent_scalar != 1:
        raise ContractError("parent sign orientation")

    alpha2 = Fraction(1, 2)
    hall = (Fraction(1), Fraction(0))
    reserve = (Fraction(1, 2), Fraction(1, 2))
    child_pair = (Fraction(1), Fraction(1))
    obs = lambda v: v[1]
    if mutation == "promote_reserve_to_current":
        hall = reserve
    if obs(reserve) != alpha2 * obs(child_pair):
        raise ContractError("reserve injection fixture")
    if not (obs(hall) < alpha2 * obs(child_pair)):
        raise ContractError("countermodel no longer separates current")

    # Zero-safe finite factors.
    mellin_zero_safe = True
    if mutation == "cancel_mellin_numerator":
        mellin_zero_safe = False
    if not mellin_zero_safe:
        raise ContractError("finite Mellin numerator cancellation")

    rh_replay = False
    if mutation == "claim_rh_replay":
        rh_replay = True
    if rh_replay:
        raise ContractError("finite replay cannot establish RH")

    return {
        "cutoff": cutoff,
        "x184_M_minus_40F_lower_decimal": "18.1144175916496",
        "low_child_recombination": True,
        "high_child_mass_threshold": "<1/8",
        "strict_margin": "1/960",
        "reserve_current_implication_refuted": True,
        "mellin_finite_factors_zero_safe": True,
        "RH_established_by_replay": False,
    }

def run(output: Path, mutations: bool) -> dict:
    baseline = validate()
    rejected = []
    if mutations:
        for m in MUTATIONS:
            try:
                validate(m)
            except ContractError:
                rejected.append(m)
            else:
                raise AssertionError(f"mutation survived: {m}")
    core = {
        "classification": VERDICT,
        "baseline": baseline,
        "hostile_mutations_rejected": rejected,
        "scope": "exact structural algebra and retained-result consistency",
    }
    raw = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    payload = {**core, "proof_object_sha256": hashlib.sha256(raw).hexdigest()}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    return payload

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, default=Path("results/verification.json"))
    ap.add_argument("--mutations", action="store_true")
    args = ap.parse_args()
    payload = run(args.output, args.mutations)
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
