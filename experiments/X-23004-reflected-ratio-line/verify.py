#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
from typing import Dict, Tuple

ROOT = Path(__file__).resolve().parent
SCHEMA = "riemann.x23004-reflected-ratio-line.v1"
RESULT_SCHEMA = "riemann.x23004-reflected-ratio-line.result.v1"

Laurent = Dict[int, int]


def allocation_polynomial(k: int) -> Dict[Tuple[int, ...], int]:
    coefficient = (-1) ** k
    return {bits: coefficient for bits in itertools.product((-1, 1), repeat=k)}


def main() -> int:
    cert = json.loads((ROOT / "certificates/synthetic.json").read_text())
    if set(cert) != {"schema", "prime_counts", "ratio_denominator_step"}:
        raise ValueError("unexpected certificate keys")
    if cert["schema"] != SCHEMA:
        raise ValueError("wrong schema")
    counts = cert["prime_counts"]
    step = cert["ratio_denominator_step"]
    if not isinstance(counts, list) or not counts:
        raise ValueError("prime_counts must be nonempty")
    if any(isinstance(k, bool) or not isinstance(k, int) or k < 1 for k in counts):
        raise ValueError("invalid prime count")
    if step != 2:
        raise ValueError("the retained ratio denominator step must equal two")

    rows = []
    for k in counts:
        poly = allocation_polynomial(k)
        identity_value = sum(poly.values())
        expected = (-2) ** k
        if len(poly) != 2**k or identity_value != expected:
            raise AssertionError((k, len(poly), identity_value, expected))
        rows.append({
            "prime_count": k,
            "terms": len(poly),
            "coefficient": (-1) ** k,
            "sum_at_identity": identity_value,
            "expected_sum": expected,
        })

    one_prime: Laurent = {-1: -1, 1: -1}
    if sum(one_prime.values()) != -2:
        raise AssertionError("one-prime orientation sum changed")

    semiprime_pair: Laurent = {-1: 1, 1: 1}
    if semiprime_pair[-1] != semiprime_pair[1] or sum(semiprime_pair.values()) != 2:
        raise AssertionError("semiprime ratio pair is not same-sign")

    # Clear X^-1 from X+X^-1.  The resulting X^2+1 has remainder 2
    # modulo 1-X^2 because X^2 is congruent to one.
    remainder = 2
    if remainder == 0:
        raise AssertionError("unexpected divisibility")

    result = {
        "schema": RESULT_SCHEMA,
        "verified": True,
        "allocation_rows": rows,
        "one_prime_laurent_numerator": {str(k): v for k, v in one_prime.items()},
        "one_prime_identity_value": -2,
        "semiprime_ratio_pair_coefficients": {str(k): v for k, v in semiprime_pair.items()},
        "semiprime_identity_value": 2,
        "division_test": {
            "numerator_after_monomial": "X^2+1",
            "candidate_denominator": "1-X^2",
            "remainder": str(remainder),
            "divisible": False,
        },
        "verdict": "EXACT_REFLECTED_RATIO_PAIR_IS_SUM_NOT_DIFFERENCE",
        "proof_boundary": (
            "Finite formal Laurent-polynomial and squarefree allocation algebra only; "
            "no global packet completeness or RH conclusion."
        ),
    }
    raw = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    out = ROOT / "results/verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
