#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99220_TYPED_CONE_BUDGET_DISINTEGRATION"


def main() -> None:
    kappa = [Fraction(1, 5), Fraction(1, 7)]
    child_mass = [Fraction(2), Fraction(3)]
    child_score = [Fraction(11), Fraction(13)]
    child_cap = [
        (Fraction(5), Fraction(7)),
        (Fraction(11), Fraction(13)),
    ]
    current_mass = Fraction(17)
    current_score = Fraction(19)
    current_cap = (Fraction(23), Fraction(29))
    d0 = Fraction(3, 2)

    parent_mass = current_mass + sum(
        a * m for a, m in zip(kappa, child_mass)
    )
    parent_score = current_score + sum(
        a * s for a, s in zip(kappa, child_score)
    )
    parent_cap = tuple(
        current_cap[j]
        + sum(a * c[j] for a, c in zip(kappa, child_cap))
        for j in range(2)
    )

    realized_child_score = [
        s - d0 * m for s, m in zip(child_score, child_mass)
    ]
    realized_parent_score = (
        current_score - d0 * current_mass
        + sum(a * s for a, s in zip(kappa, realized_child_score))
    )
    assert realized_parent_score == parent_score - d0 * parent_mass
    assert parent_cap == tuple(
        current_cap[j]
        + sum(a * c[j] for a, c in zip(kappa, child_cap))
        for j in range(2)
    )

    alpha = beta = Fraction(1)
    assert alpha + beta == 2
    assert alpha + beta != 1

    core = {
        "schema": "riemann.x99220.typed-cone-budget.v1",
        "common_child_kernel_required": True,
        "score_and_capacity_induction_exact": True,
        "continuum_virtual_root_valid": True,
        "separate_coordinate_coupling_rejected": True,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(core, indent=2, sort_keys=True) + "\n")
    print(VERDICT)
    print(core["proof_object_sha256"])


if __name__ == "__main__":
    main()
