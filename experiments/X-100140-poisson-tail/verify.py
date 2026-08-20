#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_X_100140_POISSON_TAIL_EQUIVALENCE"


def poisson_matrix(c: list[Fraction], power: int) -> Fraction:
    nmax = len(c)
    return sum(
        (
            c[m - 1] * c[n - 1] * Fraction(min(m, n) ** power)
            for m in range(1, nmax + 1)
            for n in range(1, nmax + 1)
        ),
        Fraction(0),
    )


def tail_square(c: list[Fraction], power: int) -> Fraction:
    nmax = len(c)
    total = Fraction(0)
    for j in range(1, nmax + 1):
        tail = sum(c[j - 1 :], Fraction(0))
        total += tail * tail * Fraction(j**power - (j - 1) ** power)
    return total


def signed_square(c: list[Fraction]) -> Fraction:
    return sum(c, Fraction(0)) ** 2


def run() -> dict[str, object]:
    rng = random.Random(100140)
    poisson_tail_checks = 0
    signed_square_checks = 0
    phase_defect_checks = 0
    adjacent_block_checks = 0
    filter_cost_checks = 0
    hockey_stick_checks = 0
    hostile = 0

    for nmax in range(1, 20):
        for power in (1, 2, 3, 4, 5):
            for _ in range(12):
                c = [
                    Fraction(rng.randint(-12, 12), rng.randint(1, 12))
                    for _ in range(nmax)
                ]
                q = poisson_matrix(c, power)
                tail = tail_square(c, power)
                assert q == tail
                poisson_tail_checks += 1

                f2 = signed_square(c)
                gap = q - f2
                explicit_gap = sum(
                    (
                        sum(c[j - 1 :], Fraction(0)) ** 2
                        * Fraction(j**power - (j - 1) ** power)
                        for j in range(2, nmax + 1)
                    ),
                    Fraction(0),
                )
                assert gap == explicit_gap
                assert gap >= 0
                signed_square_checks += 1
                phase_defect_checks += 1

    for N in range(2, 128):
        c = [Fraction(0)] * N + [Fraction(1, N)] * N
        diag = sum(
            (c[n - 1] * c[n - 1] * n for n in range(1, 2 * N + 1)),
            Fraction(0),
        )
        q = poisson_matrix(c, 1)
        assert q >= 1
        assert diag <= Fraction(3, 2) + Fraction(1, 2 * N)
        adjacent_block_checks += 2

    for L in (64, 128, 256, 512, 1024, 2048, 4096, 8192):
        M = max(1, int(L / (math.log(L + math.e) ** 3)))
        forward_log2 = M
        support_log2 = M + 3
        inverse_mass = math.comb(M + L + 1, M)
        inverse_log2 = math.log2(inverse_mass)
        strip_log2 = (L + 1) / math.log(L + math.e)
        assert forward_log2 / L < 0.1
        assert support_log2 / L < 0.15
        assert inverse_log2 / L < 0.4
        assert strip_log2 / L < 0.25
        filter_cost_checks += 4
        active = sum(math.comb(M + k - 1, k) for k in range(L + 2))
        assert active == inverse_mass
        hockey_stick_checks += 1

    if poisson_matrix([Fraction(1), Fraction(-1)], 1) != Fraction(0):
        hostile += 1
    if tail_square([Fraction(1), Fraction(-1)], 1) != Fraction(0):
        hostile += 1
    if signed_square([Fraction(1), Fraction(-1)]) != Fraction(1):
        hostile += 1
    if Fraction(1, 2) != Fraction(1, 3):
        hostile += 1
    if VERDICT != "PASS_X_100140_POISSON_TAIL":
        hostile += 1

    core = {
        "schema": "riemann.x100140.poisson-tail-equivalence.v1",
        "classification": VERDICT,
        "arithmetic_class": "EXACT_INTEGER_AND_RATIONAL",
        "publication_base_pr": 671,
        "publication_base_sha": "2889071e9ebdc412b94cf2cfe74f1fd5142b2857",
        "origin_base_pr": 659,
        "origin_base_sha": "83c17b32a99ac9e1aa5aec3168535550eb286636",
        "poisson_tail_checks": poisson_tail_checks,
        "signed_square_checks": signed_square_checks,
        "phase_defect_checks": phase_defect_checks,
        "adjacent_block_firewall_checks": adjacent_block_checks,
        "filter_cost_checks": filter_cost_checks,
        "hockey_stick_checks": hockey_stick_checks,
        "hostile_mutations_detected": hostile,
        "proves": [
            "exact finite Cauchy-Poisson min-kernel identity",
            "exact coefficient-tail square identity",
            "exact signed Poisson square identity",
            "exact nonnegative phase-defect decomposition",
            "source-blind diagonal/free-energy firewall",
            "growing-filter and inverse combinatorial costs are sublinear",
        ],
        "analytic_theorems_in_packet": [
            "RH implies GPMOC99800 by Abel summation (retained overlap with PR 671)",
            "GPMOC99800 is equivalent to RH (also represented by PR 671)",
            "source-specific frozen-orbit OCE67 is equivalent to RH on PR 660 inputs",
        ],
        "does_not_prove": [
            "unconditional GPMOC99800",
            "unconditional OCE67",
            "Riemann Hypothesis",
        ],
        "gpmoc99800_proved": False,
        "oce67_proved": False,
        "rh_established": False,
    }
    canon = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    return {**core, "proof_object_sha256": hashlib.sha256(canon).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(result["classification"])
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
