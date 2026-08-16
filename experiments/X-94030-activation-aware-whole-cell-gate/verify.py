#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> int:
    X = 10**12
    k = 3
    K = X // 67 + 1
    n = X // k
    activation = Fraction(X, k)
    s = Fraction(6 * n + 1, 6)

    assert activation == n + Fraction(1, 3)
    assert K + 2 <= n <= X - 10003
    assert k * s < X < k * (n + 1)
    assert 16 * X > 9 * k * (n + 1)

    getcontext().prec = 80
    D = Decimal
    ds = D(s.numerator) / D(s.denominator)
    q1 = D(1) - (ds.sqrt() ** D(-1) - D(n + 1).sqrt() ** D(-1)) / (
        D(n).sqrt() ** D(-1) - D(n + 1).sqrt() ** D(-1)
    )
    target_n1 = (D(4) * (D(X) / (D(k) * D(n + 1))).sqrt() - D(3)) / D(k).sqrt()
    loss = q1 * target_n1
    assert q1 > 0 and target_n1 > 0 and loss > D("0.09")

    payload = {
        "schema": "riemann.t94030.activation-aware-whole-cell.v1",
        "classification": "PASS_EXACT_SOURCE_ACTIVATION_KNOT_COUNTEREXAMPLE",
        "frozen_pr518": "3277b831b30f4783ed3b087df57e95b9f7dfd7b0",
        "counterexample": {
            "X": X,
            "K": K,
            "k": k,
            "cell": [n, n + 1],
            "activation": str(activation),
            "test_s": str(s),
            "q_n_plus_1": str(q1),
            "target_n_plus_1": str(target_n1),
            "lost_target": str(loss),
        },
        "AAWCC": "PROPOSED_OPEN",
        "rh_proved": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
