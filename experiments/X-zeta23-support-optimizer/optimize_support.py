#!/usr/bin/env python3
"""Nyström solver for the conditional beyond-bandwidth-one scalar optimizer.

Hypothesis-level functional:

  c_lambda(v) = lambda (int v)^2 /
    [int v^2 + lambda int int min(lambda|s-t|,1)v(s)v(t)].

For lambda <= 1 this reproduces the Montgomery--Taylor cosine optimizer.
For lambda > 1 it is conditional on the stated trace-extension hypothesis.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss


@dataclass(frozen=True)
class Optimum:
    lam: float
    nodes: int
    efficiency: float
    simple_on_line: float
    profile_min: float
    profile_max: float
    residual_inf: float


def analytic_efficiency_unsaturated(lam: float) -> float:
    theta = lam / math.sqrt(2.0)
    return math.sqrt(2.0) * math.tan(theta) / (1.0 + theta * math.tan(theta))


def flat_efficiency(lam: float) -> float:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    if lam <= 1.0:
        return lam / (1.0 + lam * lam / 3.0)
    return lam * lam / (lam * lam + 1.0 / 3.0)


def solve(lam: float, nodes: int) -> Optimum:
    if lam <= 0:
        raise ValueError("lambda must be positive")
    if nodes < 16:
        raise ValueError("nodes must be at least 16")

    x, w = leggauss(nodes)
    s = x / 2.0
    w = w / 2.0
    sqrt_w = np.sqrt(w)

    kernel = np.minimum(lam * np.abs(s[:, None] - s[None, :]), 1.0)
    bmat = np.eye(nodes) + lam * (sqrt_w[:, None] * kernel * sqrt_w[None, :])
    u = sqrt_w.copy()
    y = np.linalg.solve(bmat, u)
    efficiency = float(lam * np.dot(u, y))

    profile = y / sqrt_w
    integral = float(np.dot(w, profile))
    profile /= integral

    # A v should be a constant. Compute the quadrature residual after normalizing int v=1.
    av = profile + lam * (kernel @ (w * profile))
    residual = float(np.max(np.abs(av - np.dot(w, av))))

    return Optimum(
        lam=lam,
        nodes=nodes,
        efficiency=efficiency,
        simple_on_line=2.0 - 1.0 / efficiency,
        profile_min=float(np.min(profile)),
        profile_max=float(np.max(profile)),
        residual_inf=residual,
    )


def support_for_target(
    target: float,
    nodes: int,
    lo: float = 1.0,
    hi: float = 5.0,
    iterations: int = 24,
) -> tuple[float, float]:
    if not (0.0 < target < 1.0):
        raise ValueError("target must lie in (0,1)")
    if solve(lo, nodes).simple_on_line > target:
        lo = 0.5
    while solve(hi, nodes).simple_on_line < target:
        hi *= 2.0
        if hi > 100.0:
            raise RuntimeError("failed to bracket target")
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        if solve(mid, nodes).simple_on_line < target:
            lo = mid
        else:
            hi = mid
    lam = 0.5 * (lo + hi)
    return lam, solve(lam, nodes).simple_on_line


def self_check() -> None:
    for lam in (0.3, 0.6, 0.9, 1.0):
        numerical = solve(lam, 192).efficiency
        analytic = analytic_efficiency_unsaturated(lam)
        if abs(numerical - analytic) > 1.5e-5:
            raise AssertionError((lam, numerical, analytic))
    for lam in (0.5, 1.0, 1.2, 2.0):
        optimum = solve(lam, 160).efficiency
        if optimum + 2e-8 < flat_efficiency(lam):
            raise AssertionError((lam, optimum, flat_efficiency(lam)))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nodes", type=int, default=192)
    parser.add_argument(
        "--lambdas",
        nargs="*",
        type=float,
        default=[1.0, 1.04, 1.25, 1.7, 2.0],
    )
    parser.add_argument(
        "--targets",
        nargs="*",
        type=float,
        default=[0.70, 0.80, 0.90],
    )
    parser.add_argument("--iterations", type=int, default=24)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    self_check()
    optima = [solve(lam, args.nodes) for lam in args.lambdas]
    targets = []
    for target in args.targets:
        lam, attained = support_for_target(
            target, args.nodes, iterations=args.iterations
        )
        targets.append(
            {"target": target, "lambda": lam, "attained": attained}
        )

    payload = {
        "status": "PASS_ZETA23_CONDITIONAL_SUPPORT_OPTIMIZER",
        "scope": "conditional on the trace-extension functional in the proof note",
        "nodes": args.nodes,
        "optima": [asdict(item) for item in optima],
        "target_supports": targets,
        "convergence": {
            str(lam): [
                asdict(solve(lam, n))
                for n in sorted({64, 128, args.nodes})
                if n <= args.nodes
            ]
            for lam in args.lambdas
        },
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
