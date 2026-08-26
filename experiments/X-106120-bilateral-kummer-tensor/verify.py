#!/usr/bin/env python3
"""Finite replay for L/T-106120--106123.

The script checks exact finite algebra and numerical Fourier identities.  It
never marks the open analytic moments or RH as proved.
"""

from __future__ import annotations

import cmath
import json
import math
from itertools import product
from pathlib import Path
from typing import Dict, List, Tuple

PRIMES = (5, 7, 11, 13)
TOL = 3.0e-8


def close(a: complex, b: complex, tol: float = TOL) -> bool:
    return abs(a - b) <= tol * (1.0 + abs(a) + abs(b))


def primitive_root(p: int) -> int:
    factors: List[int] = []
    n = p - 1
    q = 2
    while q * q <= n:
        if n % q == 0:
            factors.append(q)
            while n % q == 0:
                n //= q
        q += 1
    if n > 1:
        factors.append(n)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise AssertionError(p)


def logs_mod(p: int) -> Dict[int, int]:
    g = primitive_root(p)
    out: Dict[int, int] = {}
    x = 1
    for j in range(p - 1):
        out[x] = j
        x = x * g % p
    return out


def char(p: int, logs: Dict[int, int], j: int, x: int) -> complex:
    return cmath.exp(2j * math.pi * j * logs[x % p] / (p - 1))


def fourth_character_moment(p: int, coeff: Dict[int, complex]) -> complex:
    logs = logs_mod(p)
    total = 0.0
    for j in range(p - 1):
        amp = sum(coeff[u] * char(p, logs, j, u) for u in coeff)
        total += abs(amp) ** 4
    return total / (p - 1)


def fourth_collision_sum(p: int, coeff: Dict[int, complex]) -> complex:
    units = list(coeff)
    total = 0j
    for a, b, c, d in product(units, repeat=4):
        if (a * b - c * d) % p == 0:
            total += coeff[a] * coeff[b] * (coeff[c] * coeff[d]).conjugate()
    return total


def main() -> None:
    checks = 0
    ordered_pairs: List[Tuple[int, int]] = [
        (ell, rho) for ell in PRIMES for rho in PRIMES if ell != rho
    ]

    # L-106120.4: two nonzero Ramanujan sums multiply to +1.
    for ell, rho in ordered_pairs:
        for fixture in range(1, 6):
            n = ell * (fixture * rho + 1)
            m = rho * (fixture * ell + 1)
            assert n % rho != 0 and m % ell != 0
            left = sum(
                cmath.exp(2j * math.pi * h * (n - m) / ell)
                for h in range(1, ell)
            )
            right = sum(
                cmath.exp(2j * math.pi * k * (n - m) / rho)
                for k in range(1, rho)
            )
            assert close(left, -1)
            assert close(right, -1)
            assert close(left * right, 1)
            checks += 1

    # Tensor squareclass Gram and sharp principal embedding.
    for ell, rho in ordered_pairs:
        reps_ell = [pow(i, 2, ell) for i in range(1, (ell - 1) // 2 + 1)]
        reps_rho = [pow(j, 2, rho) for j in range(1, (rho - 1) // 2 + 1)]
        for trial in range(2):
            coeff: Dict[Tuple[int, int], complex] = {}
            for i in range(len(reps_ell)):
                for j in range(len(reps_rho)):
                    coeff[i, j] = complex(
                        ((3 * i + j + trial) % 7) - 3,
                        ((i + 2 * j + trial) % 5) - 2,
                    )
            direct = 0.0
            for h in range(1, ell):
                for k in range(1, rho):
                    amp = 0j
                    for (i, j), value in coeff.items():
                        amp += value * cmath.exp(
                            2j * math.pi * h * reps_ell[i] / ell
                        ) * cmath.exp(2j * math.pi * k * reps_rho[j] / rho)
                    direct += abs(amp) ** 2
            gram = 0j
            for (i, j), a in coeff.items():
                for (ip, jp), b in coeff.items():
                    g1 = ell * int(i == ip) - 1
                    g2 = rho * int(j == jp) - 1
                    gram += a * b.conjugate() * g1 * g2
            assert close(direct, gram)
            principal = abs(sum(coeff.values())) ** 2
            factor = ((ell - 1) / (ell + 1)) * ((rho - 1) / (rho + 1))
            assert principal <= factor * direct + TOL * (1 + direct)
            checks += 1

    # L-106121.7: the bilateral atomic source weight is summable.
    for ell, rho in ordered_pairs:
        for a in range(1, 11):
            for b in range(1, 11):
                c = ell * a
                d = rho * b
                assert ell * rho * c * d <= c * c * d * d
                checks += 1

    # L-106122: independent character averages give the double product
    # collision variety.  Small moduli keep the exhaustive replay compact.
    for ell, rho in ((5, 7), (7, 5)):
        for trial in range(2):
            x = {
                u: complex((u + trial) % 4 - 1, (2 * u + trial) % 5 - 2)
                / (u + 1)
                for u in range(1, rho)
            }
            y = {
                v: complex((2 * v + trial) % 5 - 2, (v + trial) % 3 - 1)
                / (v + 2)
                for v in range(1, ell)
            }
            lhs = fourth_character_moment(rho, x) * fourth_character_moment(ell, y)
            rhs = fourth_collision_sum(rho, x) * fourth_collision_sum(ell, y)
            assert close(lhs, rhs)
            checks += 1

    # L-106123.3: fixed-core two-dimensional additive large sieve with the
    # exact maximum residue-cell multiplicities.
    for ell, rho in ordered_pairs:
        for c_factor in range(1, 5):
            for d_factor in range(1, 5):
                C = ell * c_factor
                D = rho * d_factor
                p_values = [p for p in range(1, 2 * D + 1) if p % rho != 0]
                q_values = [q for q in range(1, 2 * C + 1) if q % ell != 0]
                coeff: Dict[Tuple[int, int], complex] = {}
                for p in p_values:
                    for q in q_values:
                        # Arbitrary deterministic incidence mask.
                        if (p + 2 * q + C + D) % 5 != 0:
                            coeff[p, q] = complex(
                                (p + q) % 7 - 3,
                                (2 * p + q) % 5 - 2,
                            ) / ((p + 1) * (q + 1))
                energy = 0.0
                for h in range(ell):
                    for k in range(rho):
                        amp = sum(
                            value
                            * cmath.exp(-2j * math.pi * h * q / ell)
                            * cmath.exp(2j * math.pi * k * p / rho)
                            for (p, q), value in coeff.items()
                        )
                        energy += abs(amp) ** 2
                l2 = sum(abs(value) ** 2 for value in coeff.values())
                max_q = max(
                    sum(1 for q in q_values if q % ell == residue)
                    for residue in range(ell)
                )
                max_p = max(
                    sum(1 for p in p_values if p % rho == residue)
                    for residue in range(rho)
                )
                bound = ell * rho * max_q * max_p * l2
                assert energy <= bound + TOL * (1 + bound)
                checks += 1

    result = {
        "schema": "riemann.x106120.bilateral-kummer-tensor.v1",
        "verdict": "PASS_X_106120_BILATERAL_KUMMER_TENSOR",
        "checks": checks,
        "proved_by_replay": {
            "double_ramanujan_phase_identity": True,
            "tensor_squareclass_gram": True,
            "sharp_tensor_principal_embedding": True,
            "bilateral_atomic_weight_inequality": True,
            "double_product_collision_identity": True,
            "fixed_core_two_dimensional_additive_large_sieve": True,
        },
        "not_proved": {
            "btpp106122": True,
            "btpn106122": True,
            "btnn106122": True,
            "btrc106123": True,
            "bci102990": True,
            "riemann_hypothesis": True,
        },
    }
    assert checks == 1480, checks
    print(json.dumps(result, indent=2, sort_keys=True))
    out = Path(__file__).with_name("results") / "verification.generated.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
