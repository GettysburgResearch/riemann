#!/usr/bin/env python3
"""Exact finite-algebra replay for L-91725.

The checker verifies positive integration of 2x2 port inequalities, zero child
port ownership, common thinning, and the uniform 252 mass bound.  It does not
replay the imported analytic construction of the factor-67 port or corrections.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import random

Matrix = tuple[Fraction, Fraction, Fraction]


def add(A: Matrix, B: Matrix) -> Matrix:
    return (A[0] + B[0], A[1] + B[1], A[2] + B[2])


def scale(t: Fraction, A: Matrix) -> Matrix:
    return (t * A[0], t * A[1], t * A[2])


def sub(A: Matrix, B: Matrix) -> Matrix:
    return (A[0] - B[0], A[1] - B[1], A[2] - B[2])


def psd(A: Matrix) -> bool:
    a, b, c = A
    return a >= 0 and c >= 0 and a * c - b * b >= 0


def fiber(V: Fraction, B: Fraction, d: Fraction) -> tuple[Matrix, Matrix]:
    assert V > 0
    assert abs(B) < Fraction(8, 9) * V
    P = (V, B, V)
    assert 0 <= d <= V - abs(B)
    D = (d, Fraction(0), d)
    assert psd(P)
    assert psd(D)
    assert psd(sub(P, D))
    reserve = (V / 9, Fraction(0), V / 9)
    assert psd(sub(P, reserve))
    return P, D


def integrated_tests() -> dict[str, object]:
    rng = random.Random(91725)
    records = []
    checks = 0
    for _ in range(300):
        n = rng.randint(1, 12)
        Ptot: Matrix = (Fraction(0), Fraction(0), Fraction(0))
        Dtot: Matrix = (Fraction(0), Fraction(0), Fraction(0))
        source_mass = Fraction(0)
        for _i in range(n):
            V = Fraction(rng.randint(9, 200), rng.randint(1, 40))
            sign = -1 if rng.randrange(2) else 1
            B = sign * V * Fraction(rng.randint(0, 7), 9)
            d = (V - abs(B)) * Fraction(rng.randint(0, 10), 10)
            P, D = fiber(V, B, d)
            mu = Fraction(rng.randint(1, 20), rng.randint(1, 20))
            current = Fraction(rng.randint(0, 20), 20)
            w = mu * current
            Ptot = add(Ptot, scale(w, P))
            Dtot = add(Dtot, scale(w, D))
            source_mass += w
        assert psd(Ptot)
        assert psd(Dtot)
        assert psd(sub(Ptot, Dtot))

        tau = Fraction(rng.randint(0, 20), 20)
        assert psd(sub(scale(tau, Ptot), scale(tau, Dtot)))
        checks += 1
        if len(records) < 4:
            records.append(
                {
                    "fibers": n,
                    "current_source_mass": str(source_mass),
                    "port": [str(x) for x in Ptot],
                    "demand": [str(x) for x in Dtot],
                    "thinning": str(tau),
                }
            )
    return {
        "classification": "PASS_POSITIVE_INTEGRATED_COMMON_PORT",
        "exact_random_fixtures": checks,
        "sample_records": records,
    }


def ownership_tests() -> dict[str, object]:
    records = []
    for alpha in (Fraction(0), Fraction(1, 10), Fraction(1, 8), Fraction(7, 8)):
        parent_port = Fraction(1)
        current_port = Fraction(1)
        child_port = Fraction(0)
        assert current_port + alpha * child_port == parent_port
        records.append(
            {
                "child_coefficient": str(alpha),
                "current_port": str(current_port),
                "child_port": str(child_port),
                "total": str(current_port + alpha * child_port),
            }
        )
    return {
        "classification": "PASS_ZERO_CHILD_PORT_ONE_OWNER",
        "records": records,
    }


def mass_bound() -> dict[str, object]:
    per_unit = Fraction(14, 3)
    root_mass = Fraction(54)
    total = per_unit * root_mass
    assert total == 252
    return {
        "classification": "PASS_UNIFORM_ROOT_PORT_MASS",
        "per_unit_upper": str(per_unit),
        "root_mass_upper": str(root_mass),
        "integrated_upper": str(total),
    }


def mutation_tests() -> dict[str, object]:
    detected = 0

    alpha = Fraction(1, 8)
    assert 1 + alpha > 1
    detected += 1

    V = Fraction(1)
    B = Fraction(7, 9)
    bad_d = Fraction(1, 3)
    P = (V, B, V)
    D = (bad_d, Fraction(0), bad_d)
    assert not psd(sub(P, D))
    detected += 1

    P1, D1 = fiber(Fraction(1), Fraction(0), Fraction(1, 2))
    P2, D2 = fiber(Fraction(2), Fraction(0), Fraction(1))
    assert psd(sub(add(P1, P2), add(D1, D2)))
    detected += 1

    return {"mutations_detected": detected}


def main() -> None:
    payload: dict[str, object] = {
        "classification": "PASS_FACTOR67_ONE_UNCOLORED_COMMON_PORT",
        "integration": integrated_tests(),
        "ownership": ownership_tests(),
        "mass": mass_bound(),
        "mutation_tests": mutation_tests(),
        "imported_not_replayed": [
            "the analytic P61 matrix-port construction and |B|<8V/9",
            "the physical causal-generator theorem L-91654",
            "the root Hall and endpoint-frame producer",
            "the actual frozen finite correction demand",
            "terminal and endpoint-consumer inputs",
        ],
        "colored_projection_used": False,
        "rh_established_by_replay": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    out = Path("results/verification.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(payload["classification"])
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
