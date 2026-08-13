#!/usr/bin/env python3
from __future__ import annotations

import json
import sympy as sp


def matrices(r: sp.Expr) -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    A = 1 - r**2
    B = 1 - r
    d = sp.factor(A - B)
    C = sp.Matrix([[A, sp.Rational(2, 3) * d], [0, (4 * B - A) / 3]])
    H = sp.diag(r**2, r)
    return C, H, d


def run() -> dict[str, object]:
    checks = 0
    r = sp.symbols("r", positive=True)
    t = sp.Matrix([[1, 2]])
    s = sp.Matrix([[2, 1]])
    C, H, d = matrices(r)

    assert sp.simplify(d - r * (1 - r)) == 0
    assert sp.simplify(t * (C + H) - t) == sp.zeros(1, 2)
    assert sp.simplify(s * (C + H) - s - sp.Matrix([[0, d]])) == sp.zeros(1, 2)
    expected_correction = d * sp.Matrix([[0, sp.Rational(2, 3)], [0, -sp.Rational(1, 3)]])
    assert sp.simplify(C + H - sp.eye(2) - expected_correction) == sp.zeros(2, 2)
    checks += 4

    L, R = sp.symbols("L R", nonnegative=True)
    u = sp.Matrix([L, R])
    hidden_hazard_score = r**2 * (2 * L + R)
    physical_hazard_score = (s * H * u)[0]
    assert sp.simplify(physical_hazard_score - hidden_hazard_score - d * R) == 0
    checks += 1

    # Pure reserve: d is the exact minimum score subsidy at fixed target 2r.
    pure_reserve_target = (t * H * sp.Matrix([0, 1]))[0]
    pure_reserve_score = (s * H * sp.Matrix([0, 1]))[0]
    assert sp.simplify(pure_reserve_target / 2 - r**2 - d) == 0
    assert sp.simplify(pure_reserve_score - r) == 0
    checks += 2

    # Exact three-prime telescope at rational surrogates r=1/sqrt(p).
    rs = [sp.sqrt(sp.Rational(1, p)) for p in (67, 71, 73)]
    survival = sp.eye(2)
    hazards: list[sp.Matrix] = []
    score_surplus = sp.zeros(1, 2)
    for rv in rs:
        Cv, Hv, dv = matrices(rv)
        hazards.append(Hv * survival)
        score_surplus += sp.Matrix([[0, dv]]) * survival
        survival = Cv * survival

    target_total = t * survival
    score_total = s * survival
    for Z in hazards:
        target_total += t * Z
        score_total += s * Z
    assert sp.simplify(target_total - t) == sp.zeros(1, 2)
    assert sp.simplify(score_total - s - score_surplus) == sp.zeros(1, 2)
    checks += 2

    sample_u = sp.Matrix([sp.Rational(7, 5), sp.Rational(3, 5)])
    parent_target = sp.N((t * sample_u)[0], 50)
    fractions = [sp.N((t * Z * sample_u)[0] / parent_target, 50) for Z in hazards]
    fractions.append(sp.N((t * survival * sample_u)[0] / parent_target, 50))
    for value in fractions:
        assert value >= 0
        checks += 1
    assert abs(sum(fractions) - 1) < sp.Float("1e-45")
    checks += 1

    # Entrywise positivity on representative rough primes.
    min_entry = None
    for p in (67, 71, 73, 101, 1009):
        rv = sp.sqrt(sp.Rational(1, p))
        Cv, Hv, _ = matrices(rv)
        for value in list(Cv) + list(Hv):
            numeric = sp.N(value, 50)
            assert numeric >= 0
            min_entry = numeric if min_entry is None else min(min_entry, numeric)
            checks += 1

    return {
        "verdict": "PASS_SURVIVAL_HAZARD_BINARY_RETURN",
        "checks": checks,
        "three_prime_target_fractions": [str(v) for v in fractions],
        "minimum_sample_matrix_entry": str(min_entry),
        "symbolic_target_identity": "t(C_p+H_p)=t",
        "symbolic_score_identity": "s(C_p+H_p)=s+(0,r(1-r))",
        "scope": "exact finite algebra only; physical row/capacity lift and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
