#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99820_NATIVE_BOX_NORMALIZATION_AND_HARDY_TAIL"


def mobius(n: int) -> int:
    if n == 1:
        return 1
    x = n
    out = 1
    p = 2
    while p * p <= x:
        if x % p == 0:
            x //= p
            out = -out
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out = -out
    return out


def beta(n: int) -> int:
    return mobius(n) - (mobius(n // 67) if n % 67 == 0 else 0)


def labelled_coefficients(labels: list[int]) -> dict[int, Fraction]:
    coeff = {1: Fraction(1)}
    for p in labels:
        nxt = dict(coeff)
        for n, a in coeff.items():
            nxt[n * p] = nxt.get(n * p, Fraction(0)) - a / p
        coeff = nxt
    return {n: a for n, a in coeff.items() if a}


def check_native_label_dictionary() -> int:
    labels = [2, 3, 5, 67, 67]
    got = labelled_coefficients(labels)
    limit = 2 * 3 * 5 * 67 * 67
    checked = 0
    allowed = {2, 3, 5, 67}
    for n in range(1, limit + 1):
        x = n
        for p in allowed:
            while x % p == 0:
                x //= p
        if x != 1:
            continue
        expected = Fraction(beta(n), n)
        if got.get(n, Fraction(0)) != expected:
            raise AssertionError((n, got.get(n), expected))
        checked += 1
    return checked


def phi(y: float) -> float:
    if y < 1.0:
        return 0.0
    r = 67.0 ** -0.5
    if y < 67.0:
        return 8.0 * (1.0 - y ** -0.5) - 3.0 * math.log(y) * y ** -0.5
    return 8.0 * (1.0 - r) - 3.0 * math.log(67.0) * y ** -0.5


def W(y: float) -> float:
    return math.sqrt(y) * phi(y)


def check_normalization_mutation() -> dict[str, float]:
    p = 67.0
    y = 67.0 * 19.0
    left = W(y) - p ** -0.5 * W(y / p)
    native = math.sqrt(y) * (phi(y) - p ** -1.0 * phi(y / p))
    wrong = math.sqrt(y) * (phi(y) - p ** -0.5 * phi(y / p))
    if abs(left - native) > 1e-11:
        raise AssertionError((left, native))
    if abs(left - wrong) < 1e-4:
        raise AssertionError("p^-1/2 mutation was not detected")
    return {"native_identity_abs_error": abs(left - native),
            "wrong_operator_abs_error": abs(left - wrong)}


def collar_basis(labels: list[int]) -> dict[int, int]:
    mult: dict[int, int] = {1: 1}
    for p in labels:
        nxt = dict(mult)
        for n, a in mult.items():
            nxt[n * p] = nxt.get(n * p, 0) - a
        mult = nxt
    return {n: -3 * a for n, a in mult.items() if a}


def check_collar_dictionary() -> int:
    labels = [2, 3, 5, 67, 67]
    got = collar_basis(labels)
    for n, a in got.items():
        if a != -3 * beta(n):
            raise AssertionError((n, a, -3 * beta(n)))
    return len(got)


def hardy_direct(ns: list[int], cs: list[Fraction]) -> Fraction:
    return sum(cs[i] * cs[j] * min(ns[i], ns[j])
               for i in range(len(ns)) for j in range(len(ns)))


def hardy_tails(ns: list[int], cs: list[Fraction]) -> Fraction:
    tails = []
    running = Fraction(0)
    for c in reversed(cs):
        running += c
        tails.append(running)
    tails.reverse()
    prev = 0
    out = Fraction(0)
    for n, s in zip(ns, tails):
        out += (n - prev) * s * s
        prev = n
    return out


def check_hardy_fixtures() -> int:
    rng = random.Random(99820)
    checked = 0
    for _ in range(2000):
        ns = sorted(rng.sample(range(1, 80), rng.randint(1, 10)))
        cs = [Fraction(rng.randint(-7, 7), rng.randint(1, 9)) for _ in ns]
        if hardy_direct(ns, cs) != hardy_tails(ns, cs):
            raise AssertionError((ns, cs))
        checked += 1
    return checked


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = {
        "verdict": VERDICT,
        "native_dictionary_coordinates": check_native_label_dictionary(),
        "normalization_mutation": check_normalization_mutation(),
        "collar_basis_coordinates": check_collar_dictionary(),
        "hardy_tail_fixtures": check_hardy_fixtures(),
        "native_normalized_prime_coefficient": "1/p",
        "pr664_normalized_prime_coefficient_valid": False,
        "native_collar_window": "sum beta(n)/sqrt(n) on (x/67,x]",
        "native_window_negative_mass_proved": False,
        "gpmoc_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    text = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(VERDICT)
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
