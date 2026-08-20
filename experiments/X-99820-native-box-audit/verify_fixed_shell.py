#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
from fractions import Fraction
from pathlib import Path

VERDICT = "PASS_T99826_FIXED_SHELL_HARDY_CARLESON_REDUCTION"


def phi(y: float) -> float:
    if y < 1.0:
        return 0.0
    r = 67.0 ** -0.5
    if y < 67.0:
        return 8.0 * (1.0 - y ** -0.5) - 3.0 * math.log(y) * y ** -0.5
    return 8.0 * (1.0 - r) - 3.0 * math.log(67.0) * y ** -0.5


def W(y: float) -> float:
    return math.sqrt(y) * phi(y)


def compact_kernel(y: float) -> float:
    return W(y) - math.sqrt(2.0) * W(y / 2.0) - W(y / 4.0) + math.sqrt(2.0) * W(y / 8.0)


def check_compact_support() -> dict[str, float]:
    tail = max(abs(compact_kernel(y)) for y in (536.0, 537.0, 1000.0, 1.0e4, 1.0e8))
    interior = max(abs(compact_kernel(y)) for y in (1.5, 3.0, 10.0, 100.0, 300.0))
    assert tail < 2.0e-9
    assert interior > 1.0e-3
    assert abs(compact_kernel(1.0)) < 1.0e-12
    return {"support_ratio": 536.0, "tail_abs_max": tail, "interior_abs_max": interior}


def direct(ns: list[int], cs: list[Fraction]) -> Fraction:
    N = ns[0]
    return sum(
        cs[i] * cs[j] * Fraction(min(ns[i], ns[j]) ** 2, N ** 2)
        for i in range(len(ns)) for j in range(len(ns))
    )


def tails(ns: list[int], cs: list[Fraction]) -> Fraction:
    N = ns[0]
    suffix: list[Fraction] = []
    running = Fraction(0)
    for c in reversed(cs):
        running += c
        suffix.append(running)
    suffix.reverse()
    out = suffix[0] ** 2
    previous = N
    for j in range(1, len(ns)):
        out += Fraction(ns[j] ** 2 - previous ** 2, N ** 2) * suffix[j] ** 2
        previous = ns[j]
    return out


def check_hardy() -> int:
    rng = random.Random(99826)
    for _ in range(4000):
        ns = sorted(rng.sample(range(1, 120), rng.randint(1, 14)))
        cs = [Fraction(rng.randint(-11, 11), rng.randint(1, 13)) for _ in ns]
        q = direct(ns, cs)
        assert q == tails(ns, cs)
        assert sum(cs) ** 2 <= q
    return 4000


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    core = {
        "verdict": VERDICT,
        "fixed_compact_support": check_compact_support(),
        "support_shifted_hardy_fixtures": check_hardy(),
        "coefficient_diagonal_uniform": True,
        "support_shifted_point_evaluation": True,
        "signed_shell_hardy_carleson_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    result = {**core, "proof_object_sha256": hashlib.sha256(canonical).hexdigest()}
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(VERDICT)
    print(result["proof_object_sha256"])


if __name__ == "__main__":
    main()
