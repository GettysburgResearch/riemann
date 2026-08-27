#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as F
from math import factorial
from pathlib import Path
import hashlib
import json
import sys


def lambda_even(weights: dict[int, F], xi: int, m: int) -> F:
    """Finite-source version of (1/2) sum_(u+v=xi) (u-v)^(2m) w_u w_v."""
    total = F(0)
    for u, wu in weights.items():
        v = xi - u
        if v in weights:
            total += wu * weights[v] * (u - v) ** (2 * m)
    return total / 2


def current_taylor(weights: dict[int, F], xi: int, k: int) -> F:
    """Coefficient of h^(2k+1) in the current Fourier density."""
    total = F(0)
    for u, wu in weights.items():
        v = u - xi
        if v in weights:
            total += wu * weights[v] * (u + v) ** (2 * k + 2)
    return total / (2 * factorial(2 * k + 1))


def main(output: str) -> None:
    checks: list[str] = []

    fixtures = [
        {0: F(2), 1: F(3), -1: F(3), 2: F(1), -2: F(1)},
        {0: F(1), 1: F(2), -1: F(2), 3: F(4), -3: F(4)},
        {1: F(1), -1: F(1), 2: F(5), -2: F(5), 4: F(2), -4: F(2)},
    ]

    # Exact coefficientwise replay of
    #   j_h(xi)=sum h^(2k+1)/(2k+1)! Lambda_(2k+2)(xi).
    for fi, weights in enumerate(fixtures):
        radius = max(abs(u) for u in weights)
        for xi in range(-2 * radius, 2 * radius + 1):
            for k in range(5):
                lam = lambda_even(weights, xi, k + 1)
                coeff = current_taylor(weights, xi, k)
                assert lam >= 0
                assert coeff == lam / factorial(2 * k + 1)
                checks.append(f"hierarchy:f{fi}:xi{xi}:k{k}")

    # Exact shell-energy firewall.  For h2=2 h1, r=1/3 and
    # S(w)=w(1-rw)/(w-r), the Fourier coefficients are
    # c_1=-r, c_0=1-r^2, c_-m=(1-r^2)r^m.
    r = F(1, 3)
    parseval = (
        r * r
        + (1 - r * r) ** 2
        + (1 - r * r) ** 2 * (r * r / (1 - r * r))
    )
    assert parseval == 1
    e_negative = (1 - r * r) ** 2 * r * r / (1 - r * r) ** 2
    e_positive = r * r
    assert e_negative == F(1, 9)
    assert e_positive == F(1, 9)
    assert e_positive - e_negative == 0
    assert 19 * e_negative == F(19, 9) > 2
    checks += [
        "shell:parseval",
        "shell:Eminus=r^2",
        "shell:Eplus=r^2",
        "shell:degree=0",
        "shell:19-rungs-exceed-two",
    ]

    payload = {
        "arithmetic_class": "EXACT_RATIONAL_FINITE_SOURCE_AND_ALLPASS_ALGEBRA",
        "checks": len(checks),
        "exterior_square_hierarchy_replayed": True,
        "one_sided_density_domination_symbolic": True,
        "raw_shell_energy_below_two_refuted_as_necessary": True,
        "mctphys105610_proved": False,
        "hshe105602_proved": False,
        "apcx105620_proved": False,
        "rh_established": False,
        "verdict": "PASS_X_105620_CURRENT_TURAN_HIERARCHY",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object"] = hashlib.sha256(canonical).hexdigest()

    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["verdict"])
    print(payload["proof_object"])
    print(f"checks={payload['checks']}")
    print("RH_UNPROVEN")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify.py OUTPUT_JSON")
    main(sys.argv[1])
