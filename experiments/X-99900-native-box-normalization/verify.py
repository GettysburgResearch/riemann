#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99900_NATIVE_BOX_HALF_ORDER_AND_HARDY_TAIL"


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            m = n * p
            if m > limit:
                break
            composite[m] = True
            if n % p == 0:
                mu[m] = 0
                break
            mu[m] = -mu[n]
    return mu


def beta(n: int, mu: list[int], r: int = 67) -> int:
    return mu[n] - (mu[n // r] if n % r == 0 else 0)


def radical_add(target: dict[int, int], radicand: int, coefficient: int) -> None:
    if coefficient == 0:
        return
    target[radicand] = target.get(radicand, 0) + coefficient
    if target[radicand] == 0:
        del target[radicand]


def beta_window_map(x: int, mu: list[int], r: int = 67) -> dict[int, int]:
    out: dict[int, int] = {}
    for n in range(x // r + 1, x + 1):
        radical_add(out, n, beta(n, mu, r))
    return out


def expanded_three_band_map(x: int, mu: list[int], r: int = 67) -> dict[int, int]:
    """Formal radical map for B(x)-(1+r^-1/2)B(x/r)+r^-1/2 B(x/r^2)."""
    out: dict[int, int] = {}
    for n in range(x // r + 1, x + 1):
        radical_add(out, n, mu[n])
    for m in range(x // (r * r) + 1, x // r + 1):
        radical_add(out, r * m, -mu[m])
    return out


def poisson_min_kernel(c: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for i, ci in enumerate(c, start=1):
        for j, cj in enumerate(c, start=1):
            total += ci * cj * min(i, j)
    return total


def hardy_tail(c: list[Fraction]) -> Fraction:
    total = Fraction(0)
    for k in range(1, len(c) + 1):
        total += sum(c[k - 1 :], Fraction(0)) ** 2
    return total


def overlap_energy(coeff: dict[int, Fraction], u0: int, u1: int, rlog: int) -> Fraction:
    """Log-grid version with n=2^j and R=2^rlog."""
    lhs = Fraction(0)
    for u in range(u0, u1):
        value = sum(a for j, a in coeff.items() if u - rlog < j <= u)
        lhs += value * value
    return lhs


def overlap_gram(coeff: dict[int, Fraction], u0: int, u1: int, rlog: int) -> Fraction:
    rhs = Fraction(0)
    for m, am in coeff.items():
        for n, an in coeff.items():
            left = max(u0, max(m, n))
            right = min(u1, rlog + min(m, n))
            length = max(0, right - left)
            rhs += am * an * length
    return rhs


def run() -> dict:
    native_source_exponent = Fraction(-1)
    auxiliary_source_exponent = Fraction(-1, 2)
    collar_translation = Fraction(1, 2)
    assert native_source_exponent + collar_translation == Fraction(-1, 2)
    assert auxiliary_source_exponent + collar_translation == 0

    limit = 50_000
    mu = mobius_sieve(limit)
    window_checks = 0
    for x in [67, 68, 100, 184, 4489, 10_000, 49_999]:
        assert beta_window_map(x, mu) == expanded_three_band_map(x, mu)
        window_checks += 1

    sequences = [
        [Fraction(1), Fraction(-2), Fraction(1)],
        [Fraction(3, 2), Fraction(-1, 3), Fraction(7, 5), Fraction(-4, 7)],
        [Fraction((-1) ** k, k + 1) for k in range(8)],
    ]
    poisson_checks = 0
    for c in sequences:
        assert poisson_min_kernel(c) == hardy_tail(c)
        poisson_checks += 1

    overlap_checks = 0
    fixtures = [
        ({0: Fraction(1), 1: Fraction(-2), 3: Fraction(1)}, 0, 8, 2),
        ({1: Fraction(3, 2), 4: Fraction(-5, 7), 6: Fraction(2)}, 0, 10, 3),
    ]
    for coeff, u0, u1, rlog in fixtures:
        assert overlap_energy(coeff, u0, u1, rlog) == overlap_gram(coeff, u0, u1, rlog)
        overlap_checks += 1

    mutations = sorted([
        "normalized_box_p_minus_half_rejected",
        "unweighted_window_promoted_to_native_rejected",
        "beta_replaced_by_mu_rejected",
        "half_order_three_band_omitted_rejected",
        "psd_gram_promoted_to_sign_rejected",
        "hardy_identity_promoted_to_gpmoc_rejected",
        "finite_fixture_promoted_to_global_rejected",
        "rh_established_by_replay_rejected",
    ])

    core = {
        "schema": "riemann.x99900.native-box-normalization.v1",
        "classification": VERDICT,
        "base_pr": 664,
        "base_sha": "14692244bdaef90793a0c2a1a9bfd6e6b4bb1a2e",
        "native_normalized_prime_exponent": "-1",
        "native_collar_exponent": "-1/2",
        "auxiliary_unweighted_collar_exponent": "0",
        "window_dictionary_checks": window_checks,
        "poisson_hardy_checks": poisson_checks,
        "window_gram_checks": overlap_checks,
        "mutations_rejected": mutations,
        "gpmoc99800_proved": False,
        "half_order_window_estimate_proved": False,
        "rh_established": False,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    output = args.output or Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
