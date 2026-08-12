#!/usr/bin/env python3
from __future__ import annotations

import json
import mpmath as mp
import sympy as sp


def run() -> dict[str, object]:
    mp.mp.dps = 80
    checks = 0

    x = sp.symbols("x", positive=True)
    R = (
        -sp.Rational(1, 4) * (1 + x) * sp.exp(-x)
        + sp.Rational(17, 32) * (1 + 2 * x) * sp.exp(-2 * x)
        - sp.Rational(1, 16) * (1 + 4 * x) * sp.exp(-4 * x)
    )
    expected = x * sp.exp(-4 * x) * (2 * sp.exp(3 * x) - 17 * sp.exp(2 * x) + 8) / 8
    assert sp.simplify(sp.diff(R, x) - expected) == 0
    assert sp.simplify(R.subs(x, 0) - sp.Rational(7, 32)) == 0
    assert sp.integrate(R, (x, 0, sp.oo)) == 0
    checks += 3

    def Rf(t: mp.mpf) -> mp.mpf:
        return (
            -mp.mpf(1) / 4 * (1 + t) * mp.e ** (-t)
            + mp.mpf(17) / 32 * (1 + 2 * t) * mp.e ** (-2 * t)
            - mp.mpf(1) / 16 * (1 + 4 * t) * mp.e ** (-4 * t)
        )

    tau = mp.findroot(Rf, (mp.mpf("1"), mp.mpf("1.5")))
    varpi = mp.findroot(lambda y: y**3 - y - 1, mp.mpf("1.3"))
    kappa = mp.log(varpi)
    astar = tau / kappa
    aprime = tau / mp.log(2)
    checks += 4
    assert 1 < tau < 2
    assert 1 < varpi < mp.sqrt(2)
    assert astar / 2 > aprime
    assert astar / 4 < aprime

    def B(u: mp.mpf) -> mp.mpf:
        return 1 / (1 - mp.e ** (-2 * u)) - (1 + mp.e**u)

    max_violation = mp.mpf("0")
    for j in range(1, 4001):
        u = mp.mpf(j) / 500
        product = Rf(astar * u) * B(u)
        max_violation = max(max_violation, -product)
        assert product >= -mp.mpf("1e-65")
        checks += 1

    for factor in (mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("1.1"), mp.mpf("2")):
        a = astar * factor
        residual_boundary = tau / a
        if a < astar:
            u = (kappa + residual_boundary) / 2
        else:
            u = (residual_boundary + kappa) / 2
        assert Rf(a * u) * B(u) < 0
        checks += 1

    c = lambda a, u: -2 * a ** (-3) * Rf(a * u)
    assert c(astar / 2, mp.log(2)) > 0
    assert c(astar / 4, mp.log(2)) < 0
    checks += 2

    return {
        "verdict": "PASS_ROOT_LOCK_UNIQUENESS_AND_DYADIC_FIREWALL",
        "checks": checks,
        "tau_star": mp.nstr(tau, 50),
        "kappa": mp.nstr(kappa, 50),
        "a_star": mp.nstr(astar, 50),
        "a_prime_threshold": mp.nstr(aprime, 50),
        "maximum_root_lock_sign_violation": mp.nstr(max_violation, 12),
        "prime_signs": {
            "a_star_over_2_at_log2": mp.nstr(c(astar / 2, mp.log(2)), 20),
            "a_star_over_4_at_log2": mp.nstr(c(astar / 4, mp.log(2)), 20),
        },
        "scope": "analytic identities plus high-precision diagnostics; operator domination and RH are not proved",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
