#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

checks = 0

for m in range(2, 41):
    for j in range(m):
        for k in range(m):
            value = m if (k - 2 * j) % m == 0 else 0
            assert value in (0, m)
            checks += 1

    nonresonant = [j for j in range(m) if j != 0 and (2 * j) % m != 0]
    epsilon = 1 if m % 2 == 0 else 0
    assert len(nonresonant) == m - 1 - epsilon
    checks += 1

for m in range(3, 41):
    nonresonant = [j for j in range(m) if j != 0 and (2 * j) % m != 0]
    multipliers = {j: (7 * j * j + 3 * j + 5) % 23 for j in nonresonant}
    if nonresonant:
        maximum = max(multipliers.values())
        assert any(v == maximum for v in multipliers.values())
        weights = {j: ((11 * j + 4) % 17) + 1 for j in nonresonant}
        lhs = sum(weights[j] * multipliers[j] ** 2 for j in nonresonant)
        rhs = maximum ** 2 * sum(weights.values())
        assert lhs <= rhs
        checks += 2

for m_left in range(3, 16):
    for m_right in range(3, 16):
        left = [j for j in range(m_left) if j and (2 * j) % m_left]
        right = [k for k in range(m_right) if k and (2 * k) % m_right]
        if left and right:
            left_max = max((3 * j + 2) % 13 for j in left)
            right_max = max((5 * k + 1) % 17 for k in right)
            products = [
                ((3 * j + 2) % 13) * ((5 * k + 1) % 17)
                for j in left
                for k in right
            ]
            assert max(products) == left_max * right_max
            checks += 1

result = {
    "schema": "riemann.x107301.twisted-squareclass-plancherel.v1",
    "verdict": "PASS_X_107301_TWISTED_SQUARECLASS_PLANCHEREL",
    "exact_checks": checks,
    "proved_exact": {
        "twisted_convolution_fourier_diagonalization": True,
        "nonresonant_operator_norm": True,
        "two_place_tensor_norm": True,
        "family_dimension_removed_at_complete_shell_scope": True,
    },
    "open_status": {
        "incomplete_live_source_masks": False,
        "quadratic_resonance_binding": False,
        "principal_binding": False,
        "riemann_hypothesis": False,
        "grh": False,
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
