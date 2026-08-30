#!/usr/bin/env python3
"""Non-rigorous reconnaissance for the xi-log-derivative passivity route.

This script intentionally uses mpmath, not ball arithmetic.  Its purposes are:

1. calibrate the exact formulas at modest height;
2. test the finite Pick-kernel construction on synthetic zero sets;
3. emit deterministic JSON that a future Arb producer can mirror.

Nothing emitted by this script is a proof about the Riemann hypothesis.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp


@dataclass(frozen=True)
class ComplexJSON:
    real: str
    imag: str


def _complex_json(z: mp.mpc, digits: int = 50) -> ComplexJSON:
    return ComplexJSON(mp.nstr(mp.re(z), digits), mp.nstr(mp.im(z), digits))


def xi_logderivative(s: mp.mpc) -> mp.mpc:
    """Return xi'(s)/xi(s) from the completed-zeta logarithmic derivative.

    Formula:
        1/s + 1/(s-1) - log(pi)/2
        + digamma(s/2)/2 + zeta'(s)/zeta(s).

    The caller must avoid zeros of xi.  mpmath provides no directed error
    bounds, so this function is discovery-only.
    """

    zeta = mp.zeta(s)
    if zeta == 0:
        raise ZeroDivisionError("zeta(s) vanished at the working precision")
    zeta_prime = mp.zeta(s, derivative=1)
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + zeta_prime / zeta
    )


def logderivative_from_zeros(s: mp.mpc, zeros: Iterable[mp.mpc]) -> mp.mpc:
    """Logarithmic derivative of a finite synthetic canonical product."""

    total = mp.mpc(0)
    for rho in zeros:
        if s == rho:
            raise ZeroDivisionError("evaluation point is a synthetic zero")
        total += 1 / (s - rho)
    return total


def pick_matrix(points: Sequence[mp.mpc], values: Sequence[mp.mpc]) -> mp.matrix:
    """Build K_jk=(F(s_j)+conj(F(s_k)))/(s_j+conj(s_k)-1)."""

    if len(points) != len(values):
        raise ValueError("points and values must have equal length")
    if not points:
        raise ValueError("at least one interpolation point is required")

    size = len(points)
    matrix = mp.matrix(size, size)
    for j, s in enumerate(points):
        if mp.re(s) <= mp.mpf("0.5"):
            raise ValueError("all points must lie in Re(s)>1/2")
        for k, w in enumerate(points):
            denominator = s + mp.conj(w) - 1
            if denominator == 0:
                raise ZeroDivisionError("Pick denominator vanished")
            matrix[j, k] = (values[j] + mp.conj(values[k])) / denominator
    return matrix


def hermitian_rayleigh(matrix: mp.matrix, vector: Sequence[mp.mpc]) -> mp.mpf:
    """Return the real Rayleigh numerator v* M v for a Hermitian matrix."""

    if matrix.rows != matrix.cols or matrix.rows != len(vector):
        raise ValueError("dimension mismatch")
    total = mp.mpc(0)
    for j, vj in enumerate(vector):
        for k, vk in enumerate(vector):
            total += mp.conj(vj) * matrix[j, k] * vk
    # The residual imaginary part is a numerical diagnostic, not discarded
    # silently if it is unexpectedly large.
    tolerance = mp.mpf(10) ** (-(mp.mp.dps // 2))
    if abs(mp.im(total)) > tolerance * max(1, abs(mp.re(total))):
        raise ArithmeticError(f"Rayleigh value is not numerically real: {total}")
    return mp.re(total)


def smallest_hermitian_eigenvalue(matrix: mp.matrix) -> mp.mpf:
    """Return the smallest ordinary high-precision Hermitian eigenvalue."""

    eigenvalues, _ = mp.eighe(matrix)
    return min(mp.re(eigenvalues[j]) for j in range(eigenvalues.rows))


def _matrix_json(matrix: mp.matrix, digits: int = 50) -> list[list[dict[str, str]]]:
    return [
        [vars(_complex_json(matrix[j, k], digits)) for k in range(matrix.cols)]
        for j in range(matrix.rows)
    ]


def build_demo(dps: int = 80) -> dict[str, object]:
    """Construct deterministic calibration and synthetic-control output."""

    if dps < 30:
        raise ValueError("use at least 30 decimal digits")

    with mp.workdps(dps):
        # Synthetic RH-compatible zeros, all on Re(rho)=1/2.
        online_zeros = [
            mp.mpc("0.5", "14"),
            mp.mpc("0.5", "-14"),
            mp.mpc("0.5", "21"),
            mp.mpc("0.5", "-21"),
            mp.mpc("0.5", "25"),
            mp.mpc("0.5", "-25"),
        ]
        online_points = [
            mp.mpc("0.55", "10"),
            mp.mpc("0.60", "17"),
            mp.mpc("0.70", "24"),
        ]
        online_values = [logderivative_from_zeros(s, online_zeros) for s in online_points]
        online_pick = pick_matrix(online_points, online_values)
        online_vector = [mp.mpc(1), mp.mpc("-0.75", "0.25"), mp.mpc("0.4", "-0.2")]

        # A functional-equation-symmetric off-line orbit.  The point just to
        # the left of rho=0.6+20i lies in Re(s)>1/2 and sees a negative pole
        # contribution, providing a synthetic scalar counterexample control.
        offline_zeros = [
            mp.mpc("0.6", "20"),
            mp.mpc("0.6", "-20"),
            mp.mpc("0.4", "20"),
            mp.mpc("0.4", "-20"),
        ]
        offline_points = [
            mp.mpc("0.55", "20"),
            mp.mpc("0.54", "19.9"),
        ]
        offline_values = [logderivative_from_zeros(s, offline_zeros) for s in offline_points]
        offline_pick = pick_matrix(offline_points, offline_values)

        calibration_points = [
            mp.mpc("0.51", "0"),
            mp.mpc("0.51", "5"),
            mp.mpc("0.51", "10"),
            mp.mpc("0.51", "14.134725141734693790"),
            mp.mpc("0.51", "20"),
            mp.mpc("0.55", "30"),
        ]
        calibration_values = [xi_logderivative(s) for s in calibration_points]
        calibration_pick_points = [
            mp.mpc("0.55", "10"),
            mp.mpc("0.55", "20"),
            mp.mpc("0.60", "30"),
            mp.mpc("0.70", "40"),
        ]
        calibration_pick_values = [xi_logderivative(s) for s in calibration_pick_points]
        calibration_pick = pick_matrix(calibration_pick_points, calibration_pick_values)

        return {
            "schema": "riemann.xi-passivity-recon.v1",
            "classification": "EMPIRICAL_NONRIGOROUS",
            "working_decimal_digits": dps,
            "formula": "xi'/xi = 1/s + 1/(s-1) - log(pi)/2 + digamma(s/2)/2 + zeta'(s)/zeta(s)",
            "synthetic_online_control": {
                "points": [vars(_complex_json(z)) for z in online_points],
                "values": [vars(_complex_json(z)) for z in online_values],
                "pick_matrix": _matrix_json(online_pick),
                "smallest_eigenvalue": mp.nstr(smallest_hermitian_eigenvalue(online_pick), 50),
                "test_rayleigh": mp.nstr(hermitian_rayleigh(online_pick, online_vector), 50),
            },
            "synthetic_offline_control": {
                "points": [vars(_complex_json(z)) for z in offline_points],
                "values": [vars(_complex_json(z)) for z in offline_values],
                "scalar_real_parts": [mp.nstr(mp.re(z), 50) for z in offline_values],
                "pick_matrix": _matrix_json(offline_pick),
                "smallest_eigenvalue": mp.nstr(smallest_hermitian_eigenvalue(offline_pick), 50),
            },
            "xi_low_height_calibration": {
                "points": [vars(_complex_json(z)) for z in calibration_points],
                "values": [vars(_complex_json(z)) for z in calibration_values],
                "real_parts": [mp.nstr(mp.re(z), 50) for z in calibration_values],
                "pick_points": [vars(_complex_json(z)) for z in calibration_pick_points],
                "pick_smallest_eigenvalue": mp.nstr(
                    smallest_hermitian_eigenvalue(calibration_pick), 50
                ),
            },
            "interpretation": (
                "The synthetic controls validate sign and kernel conventions. "
                "The xi values are ordinary mpmath observations only. A proof requires "
                "directed complex balls, exact input points, and an exact rational/dyadic "
                "final sign or Rayleigh check."
            ),
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dps", type=int, default=80)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = build_demo(args.dps)
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(text, end="")
    else:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
