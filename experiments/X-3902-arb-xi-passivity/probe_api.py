#!/usr/bin/env python3
"""Probe the python-flint API needed by X-3902.

The default probe is deliberately quick. The multi-trillion-height point is
opt-in because rigorous Riemann--Siegel evaluation can be expensive and should
not be restarted on every documentation push.
"""
from __future__ import annotations

import argparse
import json
import time

from flint import acb, acb_series, arb, ctx


def xi_logderivative_two_ways(s: acb, cap: int = 3) -> tuple[acb, acb, acb]:
    ctx.cap = cap
    x = acb_series([s, 1], prec=cap)
    z = x.zeta()
    g = (x / 2).gamma()
    pi = arb.pi()

    xi = (x * (x - 1) / 2) * (-(x / 2) * pi.log()).exp() * g * z
    via_xi = (xi.derivative() / xi).coeffs()[0]
    via_parts = (
        1 / x
        + 1 / (x - 1)
        - pi.log() / 2
        + g.derivative() / g
        + z.derivative() / z
    ).coeffs()[0]
    return via_xi, via_parts, z.coeffs()[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--high", action="store_true")
    args = parser.parse_args()

    ctx.prec = 128
    points = [("low", acb("0.501", "1000.25"))]
    if args.high:
        points.append(("high", acb("0.501", "4709203636353.6309")))

    output: dict[str, object] = {
        "python_flint_context": {"prec": ctx.prec, "cap": ctx.cap},
        "high_requested": args.high,
        "points": [],
    }
    for label, s in points:
        started = time.perf_counter()
        via_xi, via_parts, zeta = xi_logderivative_two_ways(s)
        reflected, _, _ = xi_logderivative_two_ways(1 - s)
        elapsed = time.perf_counter() - started
        output["points"].append(
            {
                "label": label,
                "s": repr(s),
                "zeta": repr(zeta),
                "f_via_xi": repr(via_xi),
                "f_via_parts": repr(via_parts),
                "assemblies_overlap": via_xi.overlaps(via_parts),
                "assembly_difference": repr(via_xi - via_parts),
                "functional_equation_contains_zero": (via_xi + reflected).contains(0),
                "functional_equation_residual": repr(via_xi + reflected),
                "zeta_abs_lower": repr(zeta.abs_lower()),
                "elapsed_seconds": elapsed,
            }
        )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
