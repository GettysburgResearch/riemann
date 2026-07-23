#!/usr/bin/env python3
"""Ordinary high-precision evaluation of the L-4101 xi differential witness.

The zeta value and its first two derivatives are obtained from one mpmath
Riemann--Siegel call. This is discovery arithmetic, not directed ball arithmetic.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor
import json
from pathlib import Path

import mpmath as mp
from mpmath.functions.rszeta import Rzeta_simul


def simultaneous_zeta_derivatives(s: mp.mpc) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
    """Return zeta, zeta', zeta'' from one Riemann--Siegel evaluation."""
    ctx = mp.mp
    x_values, y_values = Rzeta_simul(ctx, s, 2)
    sigma = ctx.re(s)
    t = ctx.im(s)
    theta = ctx.siegeltheta(t - ctx.j * (sigma - ctx.mpf("0.5")))
    ps1 = (
        ctx.psi(0, s / 2) + ctx.psi(0, (1 - s) / 2)
    ) / 4 - ctx.log(ctx.pi) / 2
    ps2 = ctx.j * (
        ctx.psi(1, s / 2) - ctx.psi(1, (1 - s) / 2)
    ) / 8
    exponential = ctx.expj(-2 * theta)
    zeta = x_values[0] + exponential * y_values[0]
    zeta1 = x_values[1] + exponential * (
        -y_values[1] - 2 * y_values[0] * ps1
    )
    zeta2 = x_values[2] + exponential * (
        4 * y_values[1] * ps1
        + 4 * y_values[0] * ps1**2
        + y_values[2]
        + 2j * y_values[0] * ps2
    )
    return zeta, zeta1, zeta2


def evaluate(x_text: str, t_text: str, dps: int) -> dict[str, str]:
    if dps < 20:
        raise ValueError("dps must be at least 20")
    with mp.workdps(dps):
        x = mp.mpf(x_text)
        t = mp.mpf(t_text)
        if x <= 0:
            raise ValueError("x must be positive")
        s = mp.mpf("0.5") + x + mp.j * t
        zeta, zeta1, zeta2 = simultaneous_zeta_derivatives(s)
        if zeta == 0:
            raise ZeroDivisionError("zeta vanished at working precision")
        F = (
            1 / s
            + 1 / (s - 1)
            - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2
            + zeta1 / zeta
        )
        F1 = (
            -1 / s**2
            - 1 / (s - 1) ** 2
            + mp.polygamma(1, s / 2) / 4
            + zeta2 / zeta
            - (zeta1 / zeta) ** 2
        )
        differential = mp.re(F1) + mp.re(F) / x
        return {
            "x": x_text,
            "t": t_text,
            "dps": str(dps),
            "Re_xi_logderivative": mp.nstr(mp.re(F), 25),
            "Re_xi_logderivative_derivative": mp.nstr(mp.re(F1), 25),
            "differential_witness_D": mp.nstr(differential, 25),
            "abs_zeta": mp.nstr(abs(zeta), 25),
        }


def _worker(args: tuple[str, str, int]) -> dict[str, str]:
    return evaluate(*args)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("t")
    parser.add_argument("--xs", nargs="+", default=["0.0001"])
    parser.add_argument("--dps", type=int, default=30)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    work = [(x, args.t, args.dps) for x in args.xs]
    if args.workers == 1:
        rows = [_worker(item) for item in work]
    else:
        with ProcessPoolExecutor(max_workers=args.workers) as executor:
            rows = list(executor.map(_worker, work))
    result = {
        "status": "EMPIRICAL_NOT_CERTIFIED",
        "rows": rows,
        "warning": "mpmath values are not directed balls and do not certify a sign.",
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
