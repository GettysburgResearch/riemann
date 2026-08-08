#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent
SCHEMA = "riemann.x23003-shell-digital-algebra.v1"
RESULT_SCHEMA = "riemann.x23003-shell-digital-algebra.result.v1"


def mobius_table(N: int) -> List[int]:
    mu = [0] * (N + 1)
    mu[1] = 1
    primes: List[int] = []
    composite = [False] * (N + 1)
    for n in range(2, N + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > N:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def v2(n: int) -> int:
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


def divisors(n: int):
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            yield d
            if d * d != n:
                yield n // d


def main() -> int:
    cert = json.loads((ROOT / "certificates/synthetic.json").read_text())
    if set(cert) != {"schema", "N", "ratio_source", "ratio_target", "ratio_test_points"}:
        raise ValueError("unexpected certificate keys")
    if cert["schema"] != SCHEMA:
        raise ValueError("wrong schema")
    N = cert["N"]
    if isinstance(N, bool) or not isinstance(N, int) or N < 4:
        raise ValueError("invalid N")

    def ratio(obj):
        if set(obj) != {"numerator", "denominator"}:
            raise ValueError("bad ratio keys")
        a, b = obj["numerator"], obj["denominator"]
        if any(isinstance(x, bool) or not isinstance(x, int) for x in (a, b)):
            raise ValueError("ratio entries must be integers")
        if not (0 < a < b):
            raise ValueError("ratio must lie in (0,1)")
        return Fraction(a, b)

    d = ratio(cert["ratio_source"])
    c = ratio(cert["ratio_target"])
    points = cert["ratio_test_points"]
    if not isinstance(points, list) or not points:
        raise ValueError("ratio_test_points must be nonempty")
    if any(isinstance(x, bool) or not isinstance(x, int) or not (1 <= x <= N) for x in points):
        raise ValueError("invalid ratio test point")

    mu = mobius_table(N)
    prefix = [0] * (N + 1)
    for n in range(1, N + 1):
        prefix[n] = prefix[n - 1] + mu[n]

    def M(x: Fraction | int) -> int:
        q = int(x.numerator // x.denominator) if isinstance(x, Fraction) else x
        if q < 1:
            return 0
        return prefix[min(q, N)]

    def I(x: Fraction, r: Fraction) -> int:
        return M(x) - M(r * x)

    transfer_rows = []
    for x0 in points:
        x = Fraction(x0)
        lhs = I(x, c)
        rhs = 0
        y = x
        while y >= 1:
            rhs += I(y, d) - I(c * y, d)
            y *= d
        if lhs != rhs:
            raise AssertionError(("ratio_transfer", x0, lhs, rhs))
        transfer_rows.append({"x": x0, "first_cell": lhs, "dyadic_filter": rhs})

    b2 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    parity = [0] * (N + 1)
    for n in range(1, N + 1):
        b2[n] = mu[n] - (mu[n // 2] if n % 2 == 0 else 0)
        c2[n] = 1 - v2(n)
        parity[n] = 1 if n % 2 else -1

    mismatch = {
        "c2_convolved_b2_mismatches": 0,
        "parity_convolved_b2_mismatches": 0,
        "binary_digit_partial_sum_mismatches": 0,
        "bit_layer_factorization_mismatches": 0,
        "dyadic_shell_summatory_mismatches": 0,
    }

    csum = 0
    bsum = 0
    for n in range(1, N + 1):
        csum += c2[n]
        bsum += b2[n]
        if csum != n.bit_count():
            mismatch["binary_digit_partial_sum_mismatches"] += 1
        if bsum != prefix[n] - prefix[n // 2]:
            mismatch["dyadic_shell_summatory_mismatches"] += 1

        layer = sum(parity[n // (2**j)] for j in range(v2(n) + 1))
        if layer != c2[n]:
            mismatch["bit_layer_factorization_mismatches"] += 1

        cb = sum(c2[d0] * b2[n // d0] for d0 in divisors(n))
        expected_cb = 1 if n == 1 else (-2 if n == 2 else 0)
        if cb != expected_cb:
            mismatch["c2_convolved_b2_mismatches"] += 1

        pb = sum(parity[d0] * b2[n // d0] for d0 in divisors(n))
        expected_pb = 1 if n == 1 else (-3 if n == 2 else (2 if n == 4 else 0))
        if pb != expected_pb:
            mismatch["parity_convolved_b2_mismatches"] += 1

    if any(mismatch.values()):
        raise AssertionError(mismatch)

    result: Dict[str, object] = {
        "schema": RESULT_SCHEMA,
        "verified": True,
        "N": N,
        "coefficient_checks": mismatch,
        "ratio_transfer": transfer_rows,
        "verdict": "EXACT_RATIO_SHELL_DIGITAL_AND_PARITY_COMB_COEFFICIENT_ALGEBRA_VERIFIED",
        "proof_boundary": (
            "Finite integer and rational-floor algebra only; no asymptotic shell estimate, "
            "parity-comb coercivity, or RH conclusion."
        ),
    }
    payload = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(payload).hexdigest()
    out = ROOT / "results/verification.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
