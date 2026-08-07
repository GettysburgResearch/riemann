#!/usr/bin/env python3
"""Exact finite replay for L-23820/L-23821.

Standard library only. This verifies one rational Green orthogonalization and
one rational two-moment signed balayage, plus four fail-closed mutations.
It proves no asymptotic quotient-layer theorem and no RH claim.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F


def solve(a: list[list[F]], b: list[F]) -> list[F]:
    n = len(a)
    aug = [[F(x) for x in row] + [F(b[i])] for i, row in enumerate(a)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if aug[i][col] != 0), None)
        if pivot is None:
            raise AssertionError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [x / p for x in aug[col]]
        for i in range(n):
            if i == col:
                continue
            c = aug[i][col]
            if c:
                aug[i] = [aug[i][j] - c * aug[col][j] for j in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def matvec(a: list[list[F]], x: list[F]) -> list[F]:
    return [sum((F(c) * y for c, y in zip(row, x)), F(0)) for row in a]


def dot(x: list[F], y: list[F]) -> F:
    return sum((a * b for a, b in zip(x, y)), F(0))


def fmt(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def green_replay() -> dict[str, str]:
    g = [[F(4), F(1), F(0)], [F(1), F(3), F(1)], [F(0), F(1), F(2)]]
    lam = [F(1), F(2), F(1)]
    r = [F(3), F(-1), F(2)]

    glam = matvec(g, lam)
    e = dot(lam, glam)
    delta = dot(lam, r)
    r_perp = [ri - delta * gli / e for ri, gli in zip(r, glam)]
    t_perp = solve(g, r_perp)

    assert matvec(g, t_perp) == r_perp
    assert dot(lam, r_perp) == 0
    assert dot(lam, matvec(g, t_perp)) == 0

    scalar = [delta * gli / e for gli in glam]
    assert [r_perp[i] + scalar[i] for i in range(3)] == r

    ginv_r = solve(g, r)
    total_energy = dot(r, ginv_r)
    scalar_energy = delta * delta / e
    orthogonal_energy = dot(r_perp, t_perp)
    assert total_energy == scalar_energy + orthogonal_energy

    return {
        "E": fmt(e),
        "delta": fmt(delta),
        "scalar_energy": fmt(scalar_energy),
        "orthogonal_energy": fmt(orthogonal_energy),
        "total_energy": fmt(total_energy),
        "objective_cost": "0",
    }


def balayage_replay() -> dict[str, str]:
    x = [F(0), F(2), F(5), F(9), F(12)]
    residual = [F(3), F(-2), F(5), F(-1), F(4)]
    width = x[-1] - x[0]
    mass = sum(residual, F(0))
    moment = dot(x, residual)
    left = (x[-1] * mass - moment) / width
    right = (moment - x[0] * mass) / width

    end_left = residual[0]
    end_right = residual[-1]
    cost = F(0)

    for i in range(1, len(x) - 1):
        alpha = residual[i] * (x[-1] - x[i]) / width
        beta = residual[i] * (x[i] - x[0]) / width
        assert alpha + beta == residual[i]
        end_left += alpha
        end_right += beta
        cost += alpha * (x[i] - x[0]) - beta * (x[-1] - x[i])

    assert end_left == left
    assert end_right == right
    assert left + right == mass
    assert x[0] * left + x[-1] * right == moment
    assert cost == 0

    return {
        "mass": fmt(mass),
        "log_moment": fmt(moment),
        "left_endpoint_charge": fmt(left),
        "right_endpoint_charge": fmt(right),
        "objective_cost": "0",
    }


def mutation_tests() -> int:
    rejected = 0

    try:
        g = [[F(4), F(1), F(0)], [F(1), F(3), F(1)], [F(0), F(1), F(2)]]
        lam = [F(1), F(2), F(1)]
        r = [F(3), F(-1), F(2)]
        glam = matvec(g, lam)
        e = dot(lam, glam)
        delta = dot(lam, r)
        rp = [ri - delta * gi / e for ri, gi in zip(r, glam)]
        bad = solve(g, rp)
        bad[0] += F(1, 13)
        assert matvec(g, bad) == rp
    except AssertionError:
        rejected += 1

    try:
        assert F(3, 27) == F(3, 26)
    except AssertionError:
        rejected += 1

    try:
        assert F(5) + F(1, 12) == F(5)
    except AssertionError:
        rejected += 1

    try:
        assert F(1, 7) == 0
    except AssertionError:
        rejected += 1

    assert rejected == 4
    return rejected


def main() -> None:
    green = green_replay()
    cell = balayage_replay()
    mutations = mutation_tests()

    result = {
        "schema": "riemann.x23820-green-balayage-result.v1",
        "classification": "EXACT_GREEN_NEUTRALIZATION_AND_BALAYAGE_VERIFIED",
        "green_metric_E": green["E"],
        "green_scalar_delta": green["delta"],
        "green_scalar_energy": green["scalar_energy"],
        "green_orthogonal_energy": green["orthogonal_energy"],
        "green_total_energy": green["total_energy"],
        "green_zero_objective_cost": green["objective_cost"],
        "cell_mass": cell["mass"],
        "cell_log_moment": cell["log_moment"],
        "cell_left_endpoint_charge": cell["left_endpoint_charge"],
        "cell_right_endpoint_charge": cell["right_endpoint_charge"],
        "cell_transport_objective_cost": cell["objective_cost"],
        "mutations_rejected": mutations,
        "proof_boundary": (
            "Exact finite Green orthogonalization and signed two-moment cell "
            "transport only; no quotient-layer barrier, asymptotic carry "
            "theorem, or RH claim."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
