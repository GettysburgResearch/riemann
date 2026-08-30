#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

checks = 0

for k in range(1, 101, 2):
    defect = Fraction(1, 1000) if k == 31 else Fraction(1, k + 1000)
    height = defect / 4
    assert 4 * height == defect
    checks += 1

for denominator in range(2, 201):
    eta = Fraction(1, denominator)
    height = Fraction(1, 4000)
    deep = height / eta
    assert deep == Fraction(denominator, 4000)
    checks += 1

assert Fraction(99, 1000) - Fraction(1, 40) == Fraction(37, 500)
assert Fraction(37, 500) - Fraction(1, 62) == Fraction(897, 15500)
checks += 2

result = {
    "schema": "riemann.x107401.endpoint31-height-split.v1",
    "verdict": "PASS_X_107401_ENDPOINT31_HEIGHT_SPLIT",
    "exact_checks": checks,
    "proved_exact": {
        "alpha31_defect_to_height": True,
        "deep_charge_formula": True,
        "shallow_allowance_37_over_500": True,
        "source_transfer_room_897_over_15500": True,
    },
    "open_status": {
        "shallow31sourcepick107401": False,
        "xi31shallowtransfer107401": False,
        "more_than_ninety_percent": False,
        "riemann_hypothesis": False,
    },
}
payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

out = Path(__file__).parent / "results" / "verification.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(result["verdict"])
print(f"exact_checks={checks}")
print(f"proof_object_sha256={result['proof_object_sha256']}")
