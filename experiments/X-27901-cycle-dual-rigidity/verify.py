#!/usr/bin/env python3
"""Exact regression for L-27901/L-27902/R-27901; no RH claim."""

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent


def chi(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def mobius_table(n: int) -> list[int]:
    mu = [0] * (n + 1)
    mu[1] = 1
    primes: list[int] = []
    lp = [0] * (n + 1)
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            lp[i * p] = p
            if p == lp[i]:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


def divergence(w: list[Fraction]) -> list[Fraction]:
    x = len(w) - 1
    mu = mobius_table(x)
    u = [Fraction(0)] * (x + 2)
    for m in range(2, x + 1):
        u[m] = sum(
            Fraction(mu[k]) * w[m * k]
            for k in range(1, x // m + 1)
        )
    r = [Fraction(0)] * (x + 1)
    for m in range(2, x + 1):
        r[m] = u[m] - u[m + 1]
    r[1] = -sum(Fraction(m) * r[m] for m in range(2, x + 1))
    return r


def run() -> dict[str, object]:
    counts = {
        "balanced_split_rows": 0,
        "dyadic_defect_rows": 0,
        "atomic_pairing_rows": 0,
    }

    # Scale away the positive factor 2^(-1/2).  F_2=floor(n/2) has exactly
    # the q=2 carry defect.
    for n in range(2, 1025):
        for j in range((n + 3) // 4, n // 2 + 1):
            delta = n // 2 - j // 2 - (n - j) // 2
            assert delta == chi(n, j, 2)
            assert delta in (0, 1)
            counts["balanced_split_rows"] += 1

    # D_2=n/2-floor(n/2).  Its dyadic curvature alternates forever, so it
    # cannot be a monotone/completely-monotone sequence.
    for n in range(1, 4097):
        defect = Fraction(n, 2) - n // 2
        defect_2n = Fraction(2 * n, 2) - (2 * n) // 2
        curvature = 2 * defect - defect_2n
        assert curvature == (1 if n % 2 else 0)
        counts["dyadic_defect_rows"] += 1

    # Rational controls replay the exact floor-atomic pairing without any
    # floating arithmetic.  The proof in L-27902 is weight-independent.
    for x in range(4, 65):
        w = [Fraction(0)] * (x + 1)
        for q in range(2, x + 1):
            w[q] = Fraction(x - q, x * q)
        r = divergence(w)
        assert sum(Fraction(n) * r[n] for n in range(1, x + 1)) == 0
        for q in range(2, x + 1):
            floor_pair = sum(r[n] * (n // q) for n in range(1, x + 1))
            assert floor_pair == w[q]
            defect_pair = sum(
                r[n] * (Fraction(n, q) - n // q)
                for n in range(1, x + 1)
            )
            assert defect_pair == -w[q]
            counts["atomic_pairing_rows"] += 1

    result: dict[str, object] = {
        "classification": "EXACT_CYCLE_DUAL_RIGIDITY_MUTATIONS_VERIFIED",
        "counts": counts,
        "scope": {
            "certifies": [
                "q=2 floor atom is capacity-feasible",
                "its defect and dyadic curvature oscillate exactly",
                "floor-atomic target pairing is nonpositive for rational controls",
            ],
            "does_not_certify": [
                "global representation of every dual",
                "DCD",
                "Cycle Debt",
                "WSTS",
                "RH",
            ],
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canonical).hexdigest()
    return result


if __name__ == "__main__":
    result = run()
    out = ROOT / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
