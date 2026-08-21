#!/usr/bin/env python3
"""Exact finite replay for R-30102.

Checks the unrestricted central/sibling carry identity and separately checks
whether the realizing parent 4k lies inside the PR #272 endpoint 2Y.
Uses only integer arithmetic. Proves no asymptotic theorem or RH conclusion.
"""

import hashlib
import json
from pathlib import Path


def chi(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def main() -> None:
    carry_identity_rows = 0
    escaped_source_pairs = 0
    admissible_source_pairs = 0

    for Y in range(2, 129):
        X = 2 * Y
        for k in range(1, Y):
            # The source nodes are inside endpoint X.
            assert 2 * k + 1 <= X - 1

            # The unrestricted parent-4k carry identity is exact.
            for q in range(2, 4 * k + 1):
                lhs = chi(4 * k, 2 * k - 1, q) - chi(4 * k, 2 * k, q)
                rhs = int(2 * k % q == 0) - int((2 * k + 1) % q == 0)
                assert lhs == rhs
                carry_identity_rows += 1

            if 4 * k > X:
                escaped_source_pairs += 1
            else:
                admissible_source_pairs += 1

    assert escaped_source_pairs > 0
    assert 4 * 3 > 2 * 4  # Y=4, X=8, k=3 control.

    result = {
        "classification": "EXACT_PARENT_4K_ENDPOINT_ESCAPE_VERIFIED",
        "carry_identity_rows": carry_identity_rows,
        "escaped_source_pairs": escaped_source_pairs,
        "admissible_source_pairs": admissible_source_pairs,
        "control": "Y=4,X=8,k=3,parent=12",
        "proof_boundary": (
            "Finite support admissibility and unrestricted carry identity only; "
            "no asymptotic or RH conclusion."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()

    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    assert result["proof_object_sha256"] == (
        "08d8153d4ba3bfd51e1be329966e954e653ac1ce3c69d40a945dd465e62af09a"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
