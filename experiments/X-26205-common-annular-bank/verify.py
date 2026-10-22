#!/usr/bin/env python3
"""Exact replay for L-26213 and R-26202.

Uses only the Python standard library and Fraction arithmetic.
It verifies finite source convolution, the weighted potential embedding,
common oversupport rows, exact dilation scaling, and the real specialization
of the rank-one parity determinant identity.

It proves no asymptotic observation bound and no statement about RH.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def g(m: int, r: int) -> Fraction:
    if m <= r < 2 * m:
        return Fraction(1)
    if 2 * m <= r < 4 * m:
        return Fraction(-1, 2)
    return Fraction(0)


def convolve(a: dict[int, Fraction], x: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for d, ad in a.items():
        for m, xm in x.items():
            out[d * m] = out.get(d * m, Fraction(0)) + ad * xm
    return {k: v for k, v in out.items() if v}


def potential(x: dict[int, Fraction], r: int) -> Fraction:
    return sum((xm * g(m, r) for m, xm in x.items()), Fraction(0))


def observed_potential(a: dict[int, Fraction], x: dict[int, Fraction], r: int) -> Fraction:
    return sum((ad * potential(x, r // d) for d, ad in a.items()), Fraction(0))


def weighted_norm(x: dict[int, Fraction]) -> Fraction:
    if not x:
        return Fraction(0)
    stop = 4 * max(x)
    return sum(
        (potential(x, r) ** 2 * Fraction(1, r * (r + 1)) for r in range(1, stop)),
        Fraction(0),
    )


def split_value(x: dict[int, Fraction], n: int, j: int) -> Fraction:
    return potential(x, n) - potential(x, j) - potential(x, n - j)


def verify_embedding() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for seed in range(1, 10):
        x = {
            m: Fraction(((m * seed) % 7) - 3, (m % 3) + 1)
            for m in range(3, 8)
        }
        x = {m: v for m, v in x.items() if v}
        a = {
            d: Fraction(((d + 2 * seed) % 5) - 2, (d % 2) + 1)
            for d in range(1, 6)
        }
        a = {d: v for d, v in a.items() if v}

        y = convolve(a, x)
        max_m = max(y)

        for r in range(1, 4 * max_m + 5):
            assert potential(y, r) == observed_potential(a, x, r)

        direct = weighted_norm(y)
        embedded = sum(
            (
                observed_potential(a, x, r) ** 2
                * Fraction(1, r * (r + 1))
                for r in range(1, 4 * max_m)
            ),
            Fraction(0),
        )
        assert direct == embedded

        u = 4 * max_m
        n = 2 * u - 1
        carry = sum(
            (
                split_value(y, n, j) ** 2 * Fraction(1, j * (j + 1))
                for j in range(1, u)
            ),
            Fraction(0),
        )
        assert carry == direct

        records.append(
            {
                "seed": seed,
                "support_size": len(y),
                "weighted_norm": str(direct),
                "common_row": n,
            }
        )
    return records


def verify_dilation() -> int:
    checks = 0
    f = {k: Fraction((3 * k) % 11 - 5, (k % 4) + 1) for k in range(1, 20)}
    for d in range(1, 13):
        lhs = sum(
            (
                f.get(r // d, Fraction(0)) ** 2 * Fraction(1, r * (r + 1))
                for r in range(1, d * 20)
            ),
            Fraction(0),
        )
        rhs = Fraction(1, d) * sum(
            (f[k] ** 2 * Fraction(1, k * (k + 1)) for k in range(1, 20)),
            Fraction(0),
        )
        assert lhs == rhs
        checks += 1
    return checks


def verify_rank_one_no_go() -> int:
    checks = 0
    for v1 in range(1, 6):
        for v2 in range(1, 5):
            for a in range(-2, 3):
                for b in range(-2, 3):
                    if a == b:
                        continue
                    # Real specialization of det(vv^T - ww^T).
                    g11 = v1 * v1
                    g12 = v1 * v2
                    g22 = v2 * v2
                    w1 = a * v1
                    w2 = b * v2
                    a11 = g11 - w1 * w1
                    a12 = g12 - w1 * w2
                    a22 = g22 - w2 * w2
                    det = a11 * a22 - a12 * a12
                    expected = -(v1 * v2) ** 2 * (a - b) ** 2
                    assert det == expected < 0
                    checks += 1
    return checks


def main() -> None:
    embedding = verify_embedding()
    dilation_checks = verify_dilation()
    rank_checks = verify_rank_one_no_go()

    proof = {
        "verdict": "PASS_EXACT_COMMON_WEIGHTED_ANNULAR_EMBEDDING_AND_PARITY_NO_GO",
        "embedding_cases": embedding,
        "dilation_checks": dilation_checks,
        "rank_one_checks": rank_checks,
        "rank_one_identity": "det(vv*-T*vv*T)=-|v1 v2|^2|a-b|^2",
        "transition_warning": (
            "quotient cells 2,3,4 correspond to 2^-s,3^-s,4^-s; "
            "they are not z^2,z^3,z^4 when z=2^-s"
        ),
        "scope": "finite exact algebra only; no quantitative bank bound and no RH claim",
    }
    canonical = json.dumps(proof, sort_keys=True, separators=(",", ":")).encode()
    proof["proof_object_sha256"] = sha256(canonical).hexdigest()

    output = Path(__file__).parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(proof, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(proof["verdict"])
    print(proof["proof_object_sha256"])


if __name__ == "__main__":
    main()
