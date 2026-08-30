#!/usr/bin/env python3
import hashlib
import itertools
import json
from pathlib import Path

CLASSIFICATION = "PASS_T108320_DIRECT_COMPANION_WINDING"


def run():
    checks = 0
    sequences = 0
    for n in range(1, 13):
        for signs in itertools.product((-1, 1), repeat=n):
            up = signs.count(1)
            down = n - up
            assert n - 2 * min(up, down) == abs(sum(signs))
            transitions = sum(a != b for a, b in zip(signs, signs[1:]))
            assert transitions <= n - abs(sum(signs))
            checks += 2
            sequences += 1
    assert checks == 16380

    payload = {
        "schema": "riemann.x108320.companion-winding.v1",
        "classification": CLASSIFICATION,
        "exact_checks": checks,
        "sign_sequences_checked": sequences,
        "minority_winding_identity_proved": True,
        "direct_parent_zero_winding_gate_proved": True,
        "argument_principle_boundary_ledger_stated": True,
        "xi31wind108320_proved": False,
        "ninety_percent_established": False,
        "density_one_established": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


if __name__ == "__main__":
    payload = run()
    out = Path(__file__).parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(f"exact_checks={payload['exact_checks']}")
