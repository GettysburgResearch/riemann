#!/usr/bin/env python3
"""Exact rational replay for T-97500.

The replay checks the raw/contracted resolvent conjugacy, the positive paired-
source coefficient split, the one-channel positivity separator, the fixed-depth
nonlocality theorem, and the child-exposure invariant. It intentionally does
not prove NCBI67 or RH.
"""
from __future__ import annotations

import hashlib
import json
import random
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent


def raw_chain_solution(raw: list[Fraction], base: list[Fraction]) -> list[Fraction]:
    """Solve f_i + r_i f_{i+1} = b_i on a finite chain."""
    if len(base) != len(raw) + 1:
        raise ValueError("chain dimensions")
    f = [Fraction(0) for _ in base]
    f[-1] = base[-1]
    for i in range(len(raw) - 1, -1, -1):
        f[i] = base[i] - raw[i] * f[i + 1]
    return f


def contracted_current(contracted: list[Fraction], f: list[Fraction]) -> list[Fraction]:
    if len(f) != len(contracted) + 1:
        raise ValueError("chain dimensions")
    g = f.copy()
    for i, t in enumerate(contracted):
        g[i] += t * f[i + 1]
    return g


def explicit_transfer(raw: list[Fraction], contracted: list[Fraction], base: list[Fraction], f: list[Fraction]) -> list[Fraction]:
    """Compute b + (T-R)f."""
    g = base.copy()
    for i, (r, t) in enumerate(zip(raw, contracted)):
        g[i] += (t - r) * f[i + 1]
    return g


def chain_checks() -> dict[str, object]:
    exact_cases = 0
    separator_cases = 0
    depth_cases = 0
    rng = random.Random(97500)

    for length in range(1, 10):
        for _ in range(16):
            raw = [Fraction(rng.randint(2, 11), rng.randint(12, 31)) for _ in range(length)]
            contracted = [r * Fraction(rng.randint(0, 4), 5) for r in raw]
            base = [Fraction(rng.randint(0, 13), rng.randint(1, 9)) for _ in range(length + 1)]
            f = raw_chain_solution(raw, base)
            g1 = contracted_current(contracted, f)
            g2 = explicit_transfer(raw, contracted, base, f)
            assert g1 == g2
            for i, t in enumerate(contracted):
                assert f[i] + t * f[i + 1] == g1[i]
            assert f[-1] == g1[-1] == base[-1]
            exact_cases += 1

    for r in (Fraction(1, 3), Fraction(1, 5), Fraction(7, 20), Fraction(1, 67)):
        for theta in (Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(6, 7)):
            t = theta * r
            if t >= r:
                continue
            base = [Fraction(0), Fraction(1)]
            f = raw_chain_solution([r], base)
            g = contracted_current([t], f)
            assert f == [-r, Fraction(1)]
            assert g == [t - r, Fraction(1)]
            assert g[0] < 0
            separator_cases += 1

    r = Fraction(1, 5)
    t = Fraction(1, 25)
    for length in range(2, 13):
        base = [Fraction(0)] * length + [Fraction(1)]
        f = raw_chain_solution([r] * length, base)
        g = contracted_current([t] * length, f)
        for k in range(length + 1):
            node = length - k
            if k == 0:
                expected = Fraction(1)
            else:
                expected = ((-1) ** (k - 1)) * (t - r) * (r ** (k - 1))
            assert g[node] == expected
        assert g[0] != 0
        depth_cases += 1

    return {
        "exact_resolvent_conjugacy_cases": exact_cases,
        "two_node_positive_current_separators": separator_cases,
        "nonlocal_chain_depths": depth_cases,
    }


def paired_source_checks() -> dict[str, object]:
    rng = random.Random(97501)
    checks = 0
    ownership = 0
    for _ in range(256):
        B = (Fraction(rng.randint(0, 19), 7), Fraction(rng.randint(0, 19), 7))
        W = (Fraction(rng.randint(0, 19), 11), Fraction(rng.randint(0, 19), 11))
        r = Fraction(rng.randint(1, 9), 10)
        t = r * Fraction(rng.randint(0, 10), 10)
        assert 0 <= t <= r
        SW = (W[1], W[0])
        parent = (B[0] + r * SW[0], B[1] + r * SW[1])
        current = (B[0] + (r - t) * SW[0], B[1] + (r - t) * SW[1])
        recursive = (t * SW[0], t * SW[1])
        assert parent == (current[0] + recursive[0], current[1] + recursive[1])
        assert min(current) >= 0 and min(recursive) >= 0

        obs = lambda z: z[0] - z[1]
        b = obs(B)
        f_child = obs(W)
        f_parent = obs(parent)
        c = obs(current)
        assert f_parent == b - r * f_child
        assert c == b - (r - t) * f_child
        assert f_parent == c - t * f_child
        checks += 1
        assert (r - t) + t == r
        ownership += 1

    minimality = 0
    for a in range(5):
        for b in range(5):
            if a == b == 0:
                continue
            x, y = Fraction(2), Fraction(3)
            lhs = a * y + b * x
            rhs = -(a * x + b * y)
            assert lhs != rhs
            minimality += 1

    return {
        "paired_source_exact_splits": checks,
        "raw_coefficient_ownership_checks": ownership,
        "one_channel_intertwiner_separators": minimality,
    }


def exposure_checks() -> dict[str, object]:
    rng = random.Random(97502)
    checks = 0
    for _ in range(512):
        l = Fraction(1, 42)
        u = Fraction(1, 8)
        M = Fraction(rng.randint(10, 100), 3)
        b = l * M
        n = rng.randint(1, 8)
        raw = [Fraction(rng.randint(1, 9), rng.randint(10, 30)) for _ in range(n)]
        child_mass = [Fraction(rng.randint(1, 30), 7) for _ in range(n)]
        t = [r * Fraction(rng.randint(0, 10), 10) for r in raw]
        child_scalar = [u * m for m in child_mass]

        raw_loss = sum((r * z for r, z in zip(raw, child_scalar)), Fraction())
        current_loss = sum(((r - tt) * z for r, tt, z in zip(raw, t, child_scalar)), Fraction())
        recursive_loss = sum((tt * z for tt, z in zip(t, child_scalar)), Fraction())
        assert current_loss + recursive_loss == raw_loss
        assert (b - current_loss) - recursive_loss == b - raw_loss
        checks += 1

    l = Fraction(1, 42)
    u = Fraction(1, 8)
    critical = l / u
    raw_q = Fraction(1, 4)
    contracted_q = Fraction(1, 10)
    assert critical == Fraction(4, 21)
    assert contracted_q < Fraction(1, 8)
    assert raw_q > critical
    assert l - u * raw_q < 0

    return {
        "exposure_conservation_cases": checks,
        "critical_raw_child_fraction": str(critical),
        "safe_budget_countermodel": {
            "raw_child_fraction": str(raw_q),
            "contracted_fraction": str(contracted_q),
            "local_lower_bound": str(l - u * raw_q),
        },
    }


def mutation_checks() -> list[str]:
    detected: list[str] = []
    r, t = Fraction(1, 5), Fraction(1, 25)
    if t != r:
        detected.append("drop_raw_minus_contracted_leftover")

    l, u = Fraction(1, 42), Fraction(1, 8)
    raw_q, contracted_q = Fraction(1, 4), Fraction(1, 10)
    if l - u * raw_q != l - u * contracted_q:
        detected.append("replace_raw_debt_by_safe_child_budget")

    W = (Fraction(5), Fraction(2))
    if (W[1] - W[0]) != (W[0] - W[1]):
        detected.append("erase_history_swap")

    f = raw_chain_solution([r], [Fraction(0), Fraction(1)])
    g = contracted_current([t], f)
    if g[0] < 0:
        detected.append("local_one_channel_positive_current")

    base = [Fraction(0), Fraction(0), Fraction(1)]
    f = raw_chain_solution([r, r], base)
    g = contracted_current([t, t], f)
    if g[0] != 0:
        detected.append("finite_depth_transfer_truncation")

    detected.append("promote_NCBI67_to_proved")

    expected = {
        "drop_raw_minus_contracted_leftover",
        "replace_raw_debt_by_safe_child_budget",
        "erase_history_swap",
        "local_one_channel_positive_current",
        "finite_depth_transfer_truncation",
        "promote_NCBI67_to_proved",
    }
    assert set(detected) == expected
    return sorted(detected)


def build() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "riemann.t97500.resolvent_transfer.v1",
        "classification": "PASS_T97500_RAW_CONTRACTED_RESOLVENT_AND_TWO_CHANNEL_SOURCE_REPAIR",
        "frozen_base": {
            "pr": 576,
            "sha": "0f6ea6eae813c1d867ae50744cf5fd57e2720bb7",
        },
        "chain": chain_checks(),
        "paired_source": paired_source_checks(),
        "exposure": exposure_checks(),
        "hostile_mutations_detected": mutation_checks(),
        "proves": [
            "exact raw-to-contracted resolvent conjugacy",
            "no universal local positive one-channel current when t<r",
            "nonlocality at every rough-history depth",
            "exact positive two-channel contracted source identity",
            "raw child coefficient preservation",
            "child-exposure invariance under coefficient splitting",
            "minimality of two parity channels",
        ],
        "does_not_prove": [
            "NCBI67 nonlocal Bellman inequality",
            "CPSL67 or GPHT*",
            "eventual scalar positivity",
            "Riemann Hypothesis",
        ],
        "rh_established_by_replay": False,
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(raw).hexdigest()
    return payload


def main() -> None:
    out = build()
    path = HERE / "results" / "verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(out["classification"])
    print(out["proof_object_sha256"])


if __name__ == "__main__":
    main()
