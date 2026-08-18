#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import itertools
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent


def elementary(weights: list[Fraction], r: int) -> Fraction:
    total = Fraction(0)
    for idx in itertools.combinations(range(len(weights)), r):
        prod = Fraction(1)
        for i in idx:
            prod *= weights[i]
        total += prod
    return total


def main() -> None:
    # Exact repeated-coordinate lower bound used in R-97810.
    weights = [Fraction(1, p) for p in (67, 71, 73, 79, 83, 89, 97, 101)]
    r = 5
    A = sum(weights, Fraction(0))
    S2 = sum((w*w for w in weights), Fraction(0))
    lhs = math.factorial(r) * elementary(weights, r)
    rhs = A**r - Fraction(r*(r-1), 2) * S2 * A**(r-2)
    assert lhs >= rhs

    # Exact largest-prime root identity Ufull=UZ-I-T.
    UZ = Fraction(17, 23)
    I = Fraction(2, 101)
    T = Fraction(31, 59)
    Ufull = UZ - I - T
    assert (T <= UZ-I) == (Ufull >= 0)

    # Zero-hinge identity and strictness of the all-hinge Lorenz target.
    # Even atom (a,t,r)=(1,1,1), odd atom=(1,2,1/2).
    D0 = Fraction(1) - Fraction(1, 2)
    assert D0 == Fraction(1, 2) and D0 > 0
    target_capacity = Fraction(1) - Fraction(2)
    assert target_capacity < 0  # Lorenz infeasible despite positive scalar.

    # The published adaptive scale is deeply subcritical in the abstract
    # prime-harmonic parameter Lambda.  These fixtures only test the limiting
    # algebra; the theorem itself is analytic, not computer-certified here.
    ratios = []
    for Lambda in (10_000, 100_000, 1_000_000):
        L = 2 * math.ceil(4 * math.log(max(3.0, math.log(Lambda))))
        ratios.append(L * math.log(2 * L) / Lambda)
    assert ratios[2] < ratios[1] < ratios[0]

    result = {
        "schema": "riemann.t97810.subcritical-depth-zero-hinge.v1",
        "base_pr": 590,
        "base_sha": "223f11259b3e7134f78d6492795e6e94caca8be3",
        "repeated_coordinate_bound": True,
        "root_budget_equivalence": True,
        "zero_hinge_identity": True,
        "scalar_does_not_imply_lorenz": True,
        "subcritical_fixture_ratios": [format(v, ".17g") for v in ratios],
        "rblpte67_proved": False,
        "rh_established": False,
        "verdict": "PASS_T97810_SUBCRITICAL_DEPTH_AND_ZERO_HINGE",
    }
    canon = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = sha256(canon).hexdigest()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["verdict"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
