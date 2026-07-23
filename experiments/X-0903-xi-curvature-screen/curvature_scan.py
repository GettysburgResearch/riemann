#!/usr/bin/env python3
"""No-remainder Riemann--Siegel curvature reconnaissance.

STATUS: ordinary floating-point discovery arithmetic, not a certificate.
"""
from __future__ import annotations

import json
import time

import mpmath as mp
import numpy as np

TWO_PI_LD = np.longdouble(2) * np.longdouble(np.pi)


def theta_data(t_text: str, dps: int = 35) -> tuple[np.longdouble, ...]:
    with mp.workdps(dps):
        t = mp.mpf(t_text)
        z = mp.mpf("0.25") + mp.j * t / 2
        theta = mp.siegeltheta(t)
        psi = mp.digamma(z)
        psi1 = mp.polygamma(1, z)
        theta1 = mp.re(psi) / 2 - mp.log(mp.pi) / 2
        theta2 = -mp.im(psi1) / 4
        completion2 = (
            2 * (mp.mpf("0.25") - t * t) / (t * t + mp.mpf("0.25")) ** 2
            - mp.re(psi1) / 4
        )
        return tuple(
            np.longdouble(mp.nstr(value, 35))
            for value in (theta, theta1, theta2, completion2)
        )


def curvature(t_text: str) -> dict[str, float | int | str]:
    """Return a no-remainder approximation to Re (xi'/xi)' on the line."""
    t = np.longdouble(t_text)
    theta, theta1, theta2, completion2 = theta_data(str(t_text))
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
    value = -(float(completion2) + z2 / z0 - (z1 / z0) ** 2)
    return {
        "t": str(t_text),
        "nmax": n_max,
        "Z": float(z0),
        "curvature": float(value),
    }


if __name__ == "__main__":
    start = time.time()
    row = curvature("4709203636353.65")
    row["seconds"] = time.time() - start
    print(json.dumps(row, indent=2))
