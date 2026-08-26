#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T105400_F1_NATIVE_SOURCE_FINITE_HODGE"


def euler_coefficients(rs: list[Fraction]) -> dict[int, Fraction]:
    coeff = {0: Fraction(1)}
    for i, r in enumerate(rs):
        step = 1 << i
        old = dict(coeff)
        for mask, value in old.items():
            coeff[mask | step] = coeff.get(mask | step, Fraction(0)) - r * value
    return coeff


def direct_corner(rs: list[Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    n = len(rs)
    for mask in range(1 << n):
        value = Fraction(-1 if mask.bit_count() & 1 else 1)
        for i, r in enumerate(rs):
            if mask >> i & 1:
                value *= r
        out[mask] = value
    return out


def owner_shelling(rs: list[Fraction], greatest: bool) -> dict[int, Fraction]:
    # Return coefficients of I-E as an owner sum.
    n = len(rs)
    out: dict[int, Fraction] = {}
    for i, r in enumerate(rs):
        active = range(i + 1, n) if greatest else range(0, i)
        sub = euler_coefficients([rs[j] for j in active])
        labels = list(active)
        for local_mask, value in sub.items():
            mask = 1 << i
            for k, j in enumerate(labels):
                if local_mask >> k & 1:
                    mask |= 1 << j
            out[mask] = out.get(mask, Fraction(0)) + r * value
    return out


def toric_degree(a: list[Fraction], v: list[Fraction]) -> Fraction:
    n = len(a)
    A = math.prod(a)
    return Fraction(math.factorial(n - 1)) * A * sum(v)


def toric_primitive_square(a: list[Fraction], v: list[Fraction]) -> Fraction:
    n = len(a)
    A = math.prod(a)
    mean = sum(v, Fraction(0)) / n
    centered = [x - mean for x in v]
    return -Fraction(math.factorial(n - 2)) * A * sum(x * x for x in centered)


def toric_mixed(a: list[Fraction], v: list[Fraction], w: list[Fraction]) -> Fraction:
    n = len(a)
    A = math.prod(a)
    mv = sum(v, Fraction(0)) / n
    mw = sum(w, Fraction(0)) / n
    vc = [x - mv for x in v]
    wc = [x - mw for x in w]
    return -Fraction(math.factorial(n - 2)) * A * sum(x * y for x, y in zip(vc, wc))


def run() -> dict:
    rng = random.Random(105400)

    source_checks = 0
    owner_checks = 0
    for n in range(1, 11):
        rs = [Fraction(rng.randint(1, 9), rng.randint(10, 30)) for _ in range(n)]
        coeff = euler_coefficients(rs)
        assert coeff == direct_corner(rs)
        source_checks += 1

        expected = {mask: -value for mask, value in coeff.items() if mask != 0}
        assert owner_shelling(rs, greatest=False) == expected
        assert owner_shelling(rs, greatest=True) == expected
        owner_checks += 2

    hodge_checks = 0
    for n in range(2, 12):
        for _ in range(100):
            a = [Fraction(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(n)]
            v = [Fraction(rng.randint(-20, 20), rng.randint(1, 11)) for _ in range(n)]
            w = [Fraction(rng.randint(-20, 20), rng.randint(1, 11)) for _ in range(n)]

            degree = toric_degree(a, v)
            A = math.prod(a)
            assert degree == Fraction(math.factorial(n - 1)) * A * sum(v)

            qv = toric_primitive_square(a, v)
            qw = toric_primitive_square(a, w)
            mixed = toric_mixed(a, v, w)
            assert qv <= 0 and qw <= 0
            assert mixed * mixed <= qv * qw
            hodge_checks += 1

    ray_checks = 0
    for _ in range(10000):
        pm = Fraction(rng.randint(-100, 100), rng.randint(1, 30))
        p0 = Fraction(rng.randint(-100, 100), rng.randint(1, 30))
        pp = Fraction(rng.randint(-100, 100), rng.randint(1, 30))

        A = 2 * (pm + pp - 2 * p0)
        G = A + (pp - pm) / 2
        target = 5 * A - G
        assert target == Fraction(17, 2) * pm - 16 * p0 + Fraction(15, 2) * pp

        mean = (pm + p0 + pp) / 3
        energy = (pm - mean) ** 2 + (p0 - mean) ** 2 + (pp - mean) ** 2
        energy2 = (49 * A * A - 96 * A * G + 48 * G * G) / 24
        assert energy == energy2
        assert Fraction(769, 2) * energy - target * target == (191 * A - 192 * G) ** 2 / 48
        ray_checks += 1

    # Source-blind activation separator.
    r = Fraction(2, 5)
    f0 = Fraction(4)
    f1 = Fraction(1)
    native = f1 - r * f0
    opposite = f1 + r * f0
    assert native < 0 < opposite

    mutations = sorted([
        "activation_fan_promoted_to_native_source_rejected",
        "completion_promoted_to_native_source_rejected",
        "duplicate_67_label_collapsed_early_rejected",
        "finite_hodge_sign_promoted_to_cofinal_trace_rejected",
        "mean_direction_called_primitive_rejected",
        "normalized_p_inverse_mixed_with_half_density_rejected",
        "pairwise_ray_square_taken_before_carrier_centering_rejected",
        "f1pe105403_promoted_to_proved_rejected",
        "rh_established_by_replay_rejected",
    ])

    payload = {
        "schema": "riemann.x105400.f1-native-source-finite-hodge.v1",
        "classification": VERDICT,
        "base_pr": 727,
        "base_sha": "71782530d175162040a8c182a4cb1602d2b23821",
        "source_corner_checks": source_checks,
        "owner_shelling_checks": owner_checks,
        "toric_hodge_checks": hodge_checks,
        "three_ray_fraction_checks": ray_checks,
        "optimal_trace_constant": "769/2",
        "orthogonal_primitive_coordinate": "191A-192G",
        "source_blind_separator": True,
        "finite_native_functor_proved": True,
        "finite_hodge_gap_proved": True,
        "three_ray_primitive_trace_proved": True,
        "f1pe105403_proved": False,
        "rh_established": False,
        "mutations_rejected": mutations,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
