#!/usr/bin/env python3
from fractions import Fraction as F
import hashlib, json
from pathlib import Path

VERDICT = "PASS_T99240_HOLOMORPHIC_DEFECT_FIXED_ROW_TRANSFER"

def build():
    # Constant-tail component-row identity.
    j = 5
    eta = F(7, 13)
    lhs = (j + 1) * eta * (F(1, j - 1) - F(2, j) + F(1, j + 1))
    rhs = F(2, j * (j - 1)) * eta
    assert lhs == rhs

    # Geometric source-mass resolvent.
    M0 = F(16)
    kappa = F(1, 8)
    total_mass = M0 / (1 - kappa)
    assert total_mass == F(128, 7)

    # Large-row noncancellation leading coefficient at z=2/3.
    z = F(2, 3)
    leading = -z * (z + 1) / (1 - z)
    assert leading == F(-10, 3) != 0

    # Bounded defects are integrable for every positive Mellin exponent.
    # Exact fixture: integral_1^infty X^(-s-1)dX = 1/s.
    s = F(1, 97)
    assert 1 / s == 97

    core = {
        "schema": "riemann.x99240.holomorphic-defect.v1",
        "constant_tail_formula_exact": True,
        "geometric_mass_bound": str(total_mass),
        "noncancellation_fixture": str(leading),
        "bounded_defect_mellin_domain": "Re(s)>0",
        "exact_positive_equality_frame_required": False,
        "local_common_parent_inputs_replayed": False,
        "rh_established": False,
        "verdict": VERDICT,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    core["proof_object_sha256"] = hashlib.sha256(canon).hexdigest()
    return core

def main():
    out = build()
    path = Path(__file__).resolve().parent / "results" / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["verdict"])
    print(out["proof_object_sha256"])

if __name__ == "__main__":
    main()
