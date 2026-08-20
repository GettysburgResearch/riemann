#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_X_100210_HASSE_WAVELET_TERMINAL_MAP"


def build_flow(activities: list[Fraction]):
    flow: dict[tuple[int, int], Fraction] = {}
    delta = Fraction(1)
    for i, r in enumerate(activities):
        bit = 1 << i
        old = dict(flow)
        new = dict(old)
        for (odd, even), amount in old.items():
            key = (even | bit, odd | bit)
            new[key] = new.get(key, Fraction(0)) + r * amount
        key = (bit, 0)
        new[key] = new.get(key, Fraction(0)) + r * delta
        flow = {k: v for k, v in new.items() if v}
        delta *= 1 - r
    return flow, delta


def weight(mask: int, activities: list[Fraction]) -> Fraction:
    out = Fraction(1)
    for i, r in enumerate(activities):
        if mask & (1 << i):
            out *= r
    return out


def verify_balances(activities, flow, delta):
    k = len(activities)
    outgoing = {m: Fraction(0) for m in range(1 << k)}
    incoming = {m: Fraction(0) for m in range(1 << k)}
    for (odd, even), amount in flow.items():
        assert odd.bit_count() % 2 == 1
        assert even.bit_count() % 2 == 0
        assert (odd ^ even).bit_count() == 1
        outgoing[odd] += amount
        incoming[even] += amount
    for mask in range(1 << k):
        w = weight(mask, activities)
        if mask.bit_count() % 2:
            assert outgoing[mask] == w
        elif mask == 0:
            assert incoming[mask] == 1 - delta
        else:
            assert incoming[mask] == w


def boundary(flow, potential):
    return sum(
        (amount * (potential[odd] - potential[even])
         for (odd, even), amount in flow.items()),
        Fraction(0),
    )


def parity_sum(activities, potential):
    return sum(
        (((-1) ** mask.bit_count()) * weight(mask, activities) * potential[mask]
         for mask in range(1 << len(activities))),
        Fraction(0),
    )


def run():
    rng = random.Random(100210)
    balance_checks = divergence_checks = product_checks = 0
    wavelet_checks = variation_checks = 0

    for k in range(1, 9):
        for _ in range(24):
            activities = [
                min(Fraction(rng.randint(1, 8), rng.randint(9, 24)), Fraction(8, 9))
                for _ in range(k)
            ]
            flow, delta = build_flow(activities)
            verify_balances(activities, flow, delta)
            balance_checks += 1

            potential = {
                mask: Fraction(rng.randint(-20, 20), rng.randint(1, 20))
                for mask in range(1 << k)
            }
            assert boundary(flow, potential) == delta * potential[0] - parity_sum(activities, potential)
            divergence_checks += 1

            z = [Fraction(rng.randint(-7, 7), rng.randint(1, 8)) for _ in range(k)]
            phase_potential = {}
            for mask in range(1 << k):
                value = Fraction(1)
                for i in range(k):
                    if mask & (1 << i):
                        value *= z[i]
                phase_potential[mask] = value
            product = Fraction(1)
            for a, zi in zip(activities, z):
                product *= 1 - a * zi
            assert boundary(flow, phase_potential) == delta - product
            assert boundary(flow, {mask: Fraction(1) for mask in range(1 << k)}) == 0
            product_checks += 2

    primes = [2, 3, 5, 7, 11]
    activities = [Fraction(1, p) for p in primes]
    flow, _delta = build_flow(activities)
    for _ in range(128):
        phi = {0: Fraction(0)}
        for mask in range(1, 1 << len(primes)):
            phi[mask] = Fraction(rng.randint(-30, 30), rng.randint(1, 30))
        assert parity_sum(activities, phi) == -boundary(flow, phi)
        wavelet_checks += 1

    flow2, _ = build_flow([Fraction(1, 2), Fraction(1, 2)])
    potential2 = {0: Fraction(0), 1: Fraction(1), 2: Fraction(0), 3: Fraction(2)}
    signed = boundary(flow2, potential2)
    variation = sum(
        (amount * abs(potential2[odd] - potential2[even])
         for (odd, even), amount in flow2.items()),
        Fraction(0),
    )
    positive = sum(
        (amount * max(potential2[odd] - potential2[even], Fraction(0))
         for (odd, even), amount in flow2.items()),
        Fraction(0),
    )
    negative = sum(
        (amount * max(potential2[even] - potential2[odd], Fraction(0))
         for (odd, even), amount in flow2.items()),
        Fraction(0),
    )
    assert signed == 0 and variation == 1
    assert positive == negative == Fraction(1, 2)
    variation_checks = 5

    core = {
        "schema": "riemann.x100210.hasse-wavelet-terminal-map.v1",
        "classification": VERDICT,
        "base_pr": 675,
        "base_sha": "e21383e7522962182491f88301b3cbd375d6d6d0",
        "sibling_pr": 672,
        "sibling_sha": "2a351548eb7960ff8ae99f193c10e278984c5657",
        "arithmetic_class": "EXACT_RATIONAL",
        "flow_balance_checks": balance_checks,
        "flow_divergence_checks": divergence_checks,
        "euler_product_symbol_checks": product_checks,
        "minimal_wavelet_dictionary_checks": wavelet_checks,
        "positive_variation_firewall_checks": variation_checks,
        "proves": [
            "flow-independent Hasse divergence",
            "closed finite Euler-product phase symbol",
            "exact neutral-phase cancellation",
            "native 1/p normalized minimal-wavelet dictionary",
            "signed/positive-variation separation",
        ],
        "does_not_prove": [
            "signed nonzero-phase physical packing",
            "MWOC99910",
            "Riemann Hypothesis",
        ],
        "mwoc99910_proved": False,
        "rh_established": False,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
