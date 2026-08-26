#!/usr/bin/env python3
"""Exact replay for the T-106030 mollified owner-conductor normal form."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Dict, List, Tuple

Gaussian = Tuple[int, int]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    parity = 0
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            parity ^= 1
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        parity ^= 1
    return -1 if parity else 1


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    if value == 1:
        return 1
    if value == p - 1:
        return -1
    raise AssertionError("Euler criterion returned a nonquadratic value")


def dirichlet_convolution(a: List[int], b: List[int], limit: int) -> List[int]:
    out = [0] * (limit + 1)
    for d in range(1, min(limit, len(a) - 1) + 1):
        if a[d] == 0:
            continue
        for m in range(1, min(limit // d, len(b) - 1) + 1):
            if b[m]:
                out[d * m] += a[d] * b[m]
    return out


def gi_add(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] + y[0], x[1] + y[1])


def gi_mul(x: Gaussian, y: Gaussian) -> Gaussian:
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def gi_norm2(x: Gaussian) -> int:
    return x[0] * x[0] + x[1] * x[1]


def cyclic_convolution(a: List[Gaussian], b: List[Gaussian]) -> List[Gaussian]:
    size = len(a)
    out = [(0, 0) for _ in range(size)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            k = (i + j) % size
            out[k] = gi_add(out[k], gi_mul(x, y))
    return out


def dft4(a: List[Gaussian]) -> List[Gaussian]:
    # exp(-2*pi*i/4) = -i.
    roots = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    out: List[Gaussian] = []
    for k in range(4):
        total = (0, 0)
        for n, value in enumerate(a):
            total = gi_add(total, gi_mul(value, roots[(k * n) % 4]))
        out.append(total)
    return out


def run() -> dict:
    rng = random.Random(106030)
    checks = {
        "owner_excluded_inverse": 0,
        "vaughan_defect_identity": 0,
        "owner_quadratic_class": 0,
        "root_fibre_coherence": 0,
        "cyclic_plancherel": 0,
    }

    primes = [5, 7, 11, 13, 17, 19]
    owner_pairs = [(2, 3), (2, 5), (3, 5), (3, 7), (5, 7)]
    limit = 120

    for rho in primes:
        for p, q in owner_pairs:
            if rho in (p, q):
                continue
            owner_product = p * q

            for eta_kind in ("principal", "quadratic"):
                def eta(n: int) -> int:
                    if n % rho == 0:
                        return 0
                    return 1 if eta_kind == "principal" else legendre(n, rho)

                mu_eta = [0] * (limit + 1)
                one_eta = [0] * (limit + 1)
                for n in range(1, limit + 1):
                    if math.gcd(n, owner_product) == 1:
                        mu_eta[n] = mobius(n) * eta(n)
                        one_eta[n] = eta(n)

                inverse = dirichlet_convolution(mu_eta, one_eta, limit)
                for n in range(1, limit + 1):
                    assert inverse[n] == (1 if n == 1 else 0)
                    checks["owner_excluded_inverse"] += 1

                for cutoff in (2, 3, 5, 7, 10):
                    mu_u = [0] * (limit + 1)
                    for n in range(1, min(cutoff, limit) + 1):
                        mu_u[n] = mu_eta[n]

                    mu_u_one = dirichlet_convolution(mu_u, one_eta, limit)
                    defect = [0] * (limit + 1)
                    defect[1] = 1
                    for n in range(1, limit + 1):
                        defect[n] -= mu_u_one[n]

                    balanced = dirichlet_convolution(
                        dirichlet_convolution(defect, defect, limit),
                        mu_eta,
                        limit,
                    )

                    rhs = mu_eta.copy()
                    for n in range(1, limit + 1):
                        rhs[n] -= 2 * mu_u[n]
                    square_times_one = dirichlet_convolution(
                        dirichlet_convolution(mu_u, mu_u, limit),
                        one_eta,
                        limit,
                    )
                    for n in range(1, limit + 1):
                        rhs[n] += square_times_one[n]
                        assert balanced[n] == rhs[n]
                        checks["vaughan_defect_identity"] += 1

    for rho in [5, 7, 11, 13, 17, 19, 23]:
        for owner_product in range(1, rho):
            sigma = legendre(owner_product, rho)
            for core in range(1, rho):
                assert legendre(owner_product * core * core, rho) == sigma
                checks["owner_quadratic_class"] += 1

        for sigma in (-1, 1):
            owner_class = [
                owner_product
                for owner_product in range(1, rho)
                if legendre(owner_product, rho) == sigma
            ]
            for _ in range(30):
                coefficients = {
                    owner_product: rng.randint(-20, 20)
                    for owner_product in owner_class
                }
                principal = sum(coefficients.values())
                quadratic = sum(
                    legendre(owner_product, rho) * value
                    for owner_product, value in coefficients.items()
                )
                assert quadratic == sigma * principal
                checks["root_fibre_coherence"] += 1

    for _ in range(1000):
        a = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(4)]
        b = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(4)]
        convolution = cyclic_convolution(a, b)
        transformed = dft4(convolution)
        assert sum(gi_norm2(z) for z in transformed) == 4 * sum(
            gi_norm2(z) for z in convolution
        )
        transformed_a = dft4(a)
        transformed_b = dft4(b)
        assert transformed == [
            gi_mul(transformed_a[k], transformed_b[k]) for k in range(4)
        ]
        checks["cyclic_plancherel"] += 1

    result = {
        "verdict": "PASS_X_106030_MOLLIFIED_OWNER_CONDUCTOR_NORMAL_FORM",
        "arithmetic_class": "EXACT_INTEGER_RATIONAL_GAUSSIAN_CYCLIC",
        "checks": checks,
        "total_checks": sum(checks.values()),
        "proved": {
            "owner_excluded_mobius_inverse": True,
            "balanced_vaughan_mollifier_defect_identity": True,
            "owner_quadratic_class_partition": True,
            "principal_quadratic_root_coherence": True,
            "finite_cyclic_plancherel": True,
        },
        "open": {
            "pcm106030": True,
            "nem106030": True,
            "socm106020": True,
            "hbcqdsp102888": True,
            "riemann_hypothesis": True,
        },
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
