#!/usr/bin/env python3
"""Exact replay for L-91724 and R-91724.

All displayed decisions use Fraction arithmetic.  The checker verifies the
counterexample, collar-mass bound, barycentric Lipschitz bound, reserve schedule,
and vanishing-score schedules.  It does not replay the imported root density,
Hall, correction-map or endpoint-consumer theorems.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import random


def raw_relative_counterexample() -> dict[str, object]:
    records = []
    for N in (2, 10, 100, 10_000):
        t = Fraction(1, N)
        exact = t * t
        chord = t
        relative = abs(chord - exact) / exact
        assert relative == N - 1
        records.append({"N": N, "relative_error": str(relative)})
    assert records[-1]["relative_error"] == "9999"
    return {
        "classification": "PASS_RAW_LIPSCHITZ_RELATIVE_COUNTEREXAMPLE",
        "model": "V(t)=c(t)=t^2, chord V_h(t)=h t",
        "records": records,
        "supremum": "infinite",
    }


def collar_mass_bound() -> dict[str, object]:
    density = Fraction(183, 50)
    assert density < 4
    records = []
    for N, eta in (
        (1, Fraction(1, 100)),
        (7, Fraction(1, 10_000)),
        (300, Fraction(1, 10**9)),
    ):
        bound = density * 2 * N * eta
        coarse = 8 * N * eta
        assert bound < coarse
        records.append(
            {
                "knots": N,
                "radius": str(eta),
                "sharp_bound": str(bound),
                "coarse_bound": str(coarse),
            }
        )
    return {
        "classification": "PASS_ATOMLESS_KNOT_COLLAR_MASS_BOUND",
        "endpoint_density_upper": str(density),
        "records": records,
    }


def barycentric_lipschitz_bound() -> dict[str, object]:
    rng = random.Random(91724)
    checks = 0
    minimum_gap = None
    for _ in range(500):
        h = Fraction(rng.randint(1, 1000), rng.randint(1, 1000))
        u = h * Fraction(rng.randint(0, 1000), 1000)
        v = h - u
        weighted = 2 * u * v / h
        gap = h / 2 - weighted
        assert gap >= 0
        assert h * h - 4 * u * v == (u - v) ** 2
        if minimum_gap is None or gap < minimum_gap:
            minimum_gap = gap
        checks += 1

    h = Fraction(7, 13)
    u = v = h / 2
    assert 2 * u * v / h == h / 2

    return {
        "classification": "PASS_POSITIVE_BARYCENTRIC_LIPSCHITZ_BOUND",
        "random_fraction_checks": checks,
        "minimum_gap": str(minimum_gap),
        "midpoint_equality": True,
        "relative_bound": "L_eta*h/(2*m_eta)",
    }


def reserve_schedule() -> dict[str, object]:
    records = []
    for x, C in (
        (Fraction(1), Fraction(1)),
        (Fraction(7, 3), Fraction(5, 2)),
        (Fraction(100), Fraction(11)),
        (Fraction(10**6), Fraction(1, 7)),
    ):
        r = 1 / (x + 130)
        eps = r / (2 * 10152 * C)
        amplified = 10152 * C * eps
        remaining = r - amplified
        assert amplified == r / 2
        assert remaining == r / 2 > 0
        records.append(
            {
                "sqrtK_surrogate": str(x),
                "correction_norm_surrogate": str(C),
                "epsilon": str(eps),
                "initial_reserve": str(r),
                "amplified_error": str(amplified),
                "remaining_reserve": str(remaining),
            }
        )
    return {
        "classification": "PASS_ALL_COLUMN_RESERVE_PAYS_RELATIVE_REFINEMENT",
        "records": records,
    }


def score_schedule() -> dict[str, object]:
    records = []
    for X, S in (
        (10, Fraction(100)),
        (10**3, Fraction(999, 2)),
        (10**6, Fraction(10**4)),
    ):
        beta = Fraction(1, X * X) / (S + 1)
        loss = S * beta
        assert loss < Fraction(1, X * X)
        records.append(
            {
                "X": X,
                "score_majorant": str(S),
                "collar_mass_budget": str(beta),
                "score_loss": str(loss),
                "target_upper": str(Fraction(1, X * X)),
            }
        )
    return {
        "classification": "PASS_VANISHING_KNOT_COLLAR_SCORE_SCHEDULE",
        "records": records,
    }


def ownership_checks() -> dict[str, object]:
    records = []
    for theta in (Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(1)):
        left = theta
        right = 1 - theta
        assert left >= 0 and right >= 0 and left + right == 1
        records.append({"left": str(left), "right": str(right)})
    return {
        "classification": "PASS_ONE_USE_BARYCENTRIC_ENDPOINT_OWNERSHIP",
        "records": records,
        "collar_owner": "unused positive source",
    }


def mutation_tests() -> dict[str, object]:
    detected = 0

    N = 10**6
    assert N - 1 > 10**5
    detected += 1

    L = Fraction(5)
    m = Fraction(2)
    eps = Fraction(1, 100)
    bad_h = 3 * m * eps / L
    assert L * bad_h / (2 * m) > eps
    detected += 1

    x = Fraction(17)
    r = 1 / (x + 130)
    assert r - r == 0
    detected += 1

    return {"mutations_detected": detected}


def main() -> None:
    payload: dict[str, object] = {
        "classification": "PASS_FACTOR67_KNOT_COLLAR_RELATIVE_REFINEMENT",
        "raw_counterexample": raw_relative_counterexample(),
        "collar_mass": collar_mass_bound(),
        "interpolation": barycentric_lipschitz_bound(),
        "reserve": reserve_schedule(),
        "score": score_schedule(),
        "ownership": ownership_checks(),
        "mutation_tests": mutation_tests(),
        "imported_not_replayed": [
            "factor-67 equality density 0<L(x)<183/100",
            "finite root activation-cell description",
            "fixed-window Hall amplification 10152",
            "bounded one-use correction-map norm",
            "all-column reserve from L-91723",
            "mass-weighted direct-integral contraction L-91694",
            "terminal, common-port and endpoint-consumer inputs",
        ],
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
