#!/usr/bin/env python3
"""Riemann--Siegel reconnaissance for the independent xi'/xi criterion.

STATUS: ordinary high-precision discovery arithmetic, not directed balls.
The fast curvature screen deliberately omits the Riemann--Siegel remainder and
must never be used as a certificate. Exact-point escalation uses mpmath's
simultaneous Riemann--Siegel zeta and zeta-derivative implementation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Iterable

import mpmath as mp
import numpy as np
from mpmath.functions.rszeta import Rzeta_simul

TWO_PI_LD = np.longdouble(2) * np.longdouble(np.pi)


def _theta_data(t_text: str, dps: int = 40) -> tuple[np.longdouble, ...]:
    with mp.workdps(dps):
        t = mp.mpf(t_text)
        z = mp.mpf("0.25") + mp.j * t / 2
        theta = mp.siegeltheta(t)
        psi = mp.digamma(z)
        psi1 = mp.polygamma(1, z)
        theta1 = mp.re(psi) / 2 - mp.log(mp.pi) / 2
        theta2 = -mp.im(psi1) / 4
        completion1 = 2 * t / (t * t + mp.mpf("0.25")) - mp.im(psi) / 2
        completion2 = (
            2 * (mp.mpf("0.25") - t * t) / (t * t + mp.mpf("0.25")) ** 2
            - mp.re(psi1) / 4
        )
        return tuple(
            np.longdouble(mp.nstr(x, 35))
            for x in (theta, theta1, theta2, completion1, completion2)
        )


def approximate_critical_curvature(t_text: str) -> dict[str, float | int | str]:
    """Return a no-remainder approximation to Re (xi'/xi)' on Re(s)=1/2."""
    t = np.longdouble(t_text)
    theta, theta1, theta2, _completion1, completion2 = _theta_data(t_text)
    n_max = int(np.floor(np.sqrt(t / TWO_PI_LD)))
    n = np.arange(1, n_max + 1, dtype=np.int64)
    log_n = np.log(n.astype(np.longdouble))
    weight = 1 / np.sqrt(n.astype(np.float64))
    phase = np.remainder(theta - t * log_n, TWO_PI_LD).astype(np.float64)
    local_frequency = (theta1 - log_n).astype(np.float64)
    cosine = np.cos(phase)
    sine = np.sin(phase)

    z0 = 2 * np.sum(weight * cosine, dtype=np.float64)
    z1 = -2 * np.sum(weight * sine * local_frequency, dtype=np.float64)
    z2 = 2 * np.sum(
        weight
        * (-cosine * local_frequency * local_frequency - sine * float(theta2)),
        dtype=np.float64,
    )
    if z0 == 0:
        raise ZeroDivisionError("no-remainder Hardy Z approximation vanished")
    curvature = -(float(completion2) + z2 / z0 - (z1 / z0) ** 2)
    return {
        "t": str(t_text),
        "riemann_siegel_terms": n_max,
        "hardy_Z_no_remainder": float(z0),
        "curvature_no_remainder": float(curvature),
    }


def simultaneous_zeta_and_derivative(s: mp.mpc) -> tuple[mp.mpc, mp.mpc]:
    """Compute zeta(s), zeta'(s) using one Riemann--Siegel call."""
    ctx = mp.mp
    x_values, y_values = Rzeta_simul(ctx, s, 1)
    sigma = ctx.re(s)
    t = ctx.im(s)
    theta = ctx.siegeltheta(t - ctx.j * (sigma - ctx.mpf("0.5")))
    psi_sum = (
        ctx.psi(0, s / 2) + ctx.psi(0, (1 - s) / 2)
    ) / 4 - ctx.log(ctx.pi) / 2
    exponential = ctx.expj(-2 * theta)
    zeta = x_values[0] + exponential * y_values[0]
    zeta_prime = x_values[1] + exponential * (
        -y_values[1] - 2 * y_values[0] * psi_sum
    )
    return zeta, zeta_prime


def xi_logderivative(sigma_text: str, t_text: str, dps: int) -> dict[str, str]:
    """Evaluate the corrected D-3201 formula at one exact decimal input."""
    with mp.workdps(dps):
        sigma = mp.mpf(sigma_text)
        t = mp.mpf(t_text)
        if sigma <= mp.mpf("0.5"):
            raise ValueError("sigma must exceed 1/2")
        s = sigma + mp.j * t
        zeta, zeta_prime = simultaneous_zeta_and_derivative(s)
        if zeta == 0:
            raise ZeroDivisionError("zeta evaluation is zero at working precision")
        value = (
            1 / s
            + 1 / (s - 1)
            - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2
            + zeta_prime / zeta
        )
        return {
            "sigma": sigma_text,
            "t": t_text,
            "Re_xi_logderivative": mp.nstr(mp.re(value), 25),
            "Im_xi_logderivative": mp.nstr(mp.im(value), 25),
            "abs_zeta": mp.nstr(abs(zeta), 25),
        }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    curvature = subparsers.add_parser("curvature")
    curvature.add_argument("t")

    point = subparsers.add_parser("point")
    point.add_argument("t")
    point.add_argument("--sigmas", nargs="+", default=["0.5001", "0.501", "0.505"])
    point.add_argument("--dps", type=int, default=35)
    point.add_argument("--output", type=Path)
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "curvature":
        print(json.dumps(approximate_critical_curvature(args.t), indent=2))
        return 0
    rows = [xi_logderivative(sigma, args.t, args.dps) for sigma in args.sigmas]
    text = json.dumps({"status": "EMPIRICAL_NOT_CERTIFIED", "rows": rows}, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
