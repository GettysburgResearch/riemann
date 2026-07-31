#!/usr/bin/env python3
"""Exact checker for finite half-plane Hardy pole Gram certificates."""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15408-hardy-pole-gram.synthetic.v1"


class CertificateError(ValueError):
    pass


def integer(value: Any, name: str) -> int:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value, 10)
        except ValueError as exc:
            raise CertificateError(f"{name} is not a decimal integer") from exc
    raise CertificateError(f"{name} must be an integer or decimal string")


def frac(value: Any, name: str) -> Fraction:
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be an object")
    n = integer(value.get("numerator"), f"{name}.numerator")
    d = integer(value.get("denominator"), f"{name}.denominator")
    if d <= 0:
        raise CertificateError(f"{name}.denominator must be positive")
    return Fraction(n, d)


def fj(value: Fraction) -> dict[str, str]:
    return {"numerator": str(value.numerator), "denominator": str(value.denominator)}


@dataclass(frozen=True)
class Gaussian:
    re: Fraction
    im: Fraction

    @staticmethod
    def coerce(value: "Gaussian | Fraction | int") -> "Gaussian":
        if isinstance(value, Gaussian):
            return value
        return Gaussian(Fraction(value), Fraction(0))

    def __add__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        other = self.coerce(other)
        return Gaussian(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.re, -self.im)

    def __sub__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        return self + (-self.coerce(other))

    def __rsub__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        return self.coerce(other) - self

    def __mul__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        other = self.coerce(other)
        return Gaussian(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "Gaussian":
        return Gaussian(self.re, -self.im)

    def inverse(self) -> "Gaussian":
        denominator = self.re * self.re + self.im * self.im
        if denominator == 0:
            raise CertificateError("Gaussian rational division by zero")
        return Gaussian(self.re / denominator, -self.im / denominator)

    def __truediv__(self, other: "Gaussian | Fraction | int") -> "Gaussian":
        return self * self.coerce(other).inverse()


ZERO = Gaussian(Fraction(0), Fraction(0))


def gj(value: Gaussian) -> dict[str, dict[str, str]]:
    return {"real": fj(value.re), "imag": fj(value.im)}


def parse_gaussian(raw: Any, name: str) -> Gaussian:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    return Gaussian(frac(raw.get("real"), f"{name}.real"), frac(raw.get("imag"), f"{name}.imag"))


def parse_packet(raw: Any, name: str) -> tuple[Fraction, list[Gaussian], list[Gaussian]]:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an object")
    sigma = frac(raw.get("sigma"), f"{name}.sigma")
    if sigma <= 0:
        raise CertificateError(f"{name}.sigma must be positive")
    poles_raw = raw.get("poles")
    residues_raw = raw.get("residues")
    if not isinstance(poles_raw, list) or not isinstance(residues_raw, list):
        raise CertificateError(f"{name}.poles and residues must be arrays")
    if len(poles_raw) == 0 or len(poles_raw) != len(residues_raw):
        raise CertificateError(f"{name} must have equally many nonempty poles and residues")
    poles = [parse_gaussian(v, f"{name}.poles[{i}]") for i, v in enumerate(poles_raw)]
    residues = [parse_gaussian(v, f"{name}.residues[{i}]") for i, v in enumerate(residues_raw)]
    if len({(a.re, a.im) for a in poles}) != len(poles):
        raise CertificateError(f"{name}.poles must be distinct")
    if any(r == ZERO for r in residues):
        raise CertificateError(f"{name}.residues must be nonzero")
    return sigma, poles, residues


def gram_and_energy(
    sigma: Fraction, poles: list[Gaussian], residues: list[Gaussian]
) -> tuple[list[list[Gaussian]], Gaussian]:
    if any(sigma <= pole.re for pole in poles):
        raise CertificateError("evaluation line must lie strictly right of every packet pole")
    matrix: list[list[Gaussian]] = []
    for a in poles:
        row: list[Gaussian] = []
        for b in poles:
            # C(j,k) = (2 sigma - conjugate(a_j) - a_k)^(-1).
            denominator = Gaussian(2 * sigma - a.re - b.re, a.im - b.im)
            row.append(denominator.inverse())
        matrix.append(row)

    energy = ZERO
    for j, rj in enumerate(residues):
        for k, rk in enumerate(residues):
            energy += rj.conjugate() * matrix[j][k] * rk
    if energy.im != 0 or energy.re <= 0:
        raise CertificateError("Hardy Cauchy quadratic value must be positive real")
    for j in range(len(matrix)):
        for k in range(len(matrix)):
            if matrix[j][k] != matrix[k][j].conjugate():
                raise CertificateError("Cauchy matrix is not Hermitian")
    return matrix, energy


def verify_packet(raw: Any, name: str) -> dict[str, Any]:
    sigma, poles, residues = parse_packet(raw, name)
    matrix, energy = gram_and_energy(sigma, poles, residues)
    claimed = raw.get("claimed")
    if not isinstance(claimed, dict):
        raise CertificateError(f"{name}.claimed must be an object")
    if frac(claimed.get("energy"), f"{name}.claimed.energy") != energy.re:
        raise CertificateError(f"{name} claimed energy mismatch")
    weighted = sigma * energy.re
    if frac(claimed.get("sigma_times_energy"), f"{name}.claimed.sigma_times_energy") != weighted:
        raise CertificateError(f"{name} claimed weighted energy mismatch")
    return {
        "sigma": fj(sigma),
        "poles": [gj(a) for a in poles],
        "residues": [gj(r) for r in residues],
        "cauchy_gram": [[gj(v) for v in row] for row in matrix],
        "energy": fj(energy.re),
        "sigma_times_energy": fj(weighted),
    }


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    unstable = verify_packet(data.get("unstable_packet"), "unstable_packet")
    boundary = verify_packet(data.get("boundary_packet"), "boundary_packet")
    stable = verify_packet(data.get("stable_packet"), "stable_packet")

    boundary_raw = data["boundary_packet"]
    _, _, boundary_residues = parse_packet(boundary_raw, "boundary_packet")
    # |r| <= |Re r|+|Im r| gives a rational fail-safe Abel bound.
    l1_residue_upper = sum(abs(r.re) + abs(r.im) for r in boundary_residues)
    triangle_bound = l1_residue_upper * l1_residue_upper / 2
    boundary_weighted = frac(boundary["sigma_times_energy"], "internal.boundary_weighted")
    if boundary_weighted > triangle_bound:
        raise CertificateError("boundary packet exceeds the rational l1 Abel bound")

    return {
        "schema": SCHEMA,
        "status": "EXACT_FINITE_HARDY_POLE_GRAM",
        "unstable_packet": unstable,
        "boundary_packet": boundary,
        "boundary_l1_abel_bound": fj(triangle_bound),
        "stable_packet": stable,
        "proof_boundary": (
            "exact finite Gaussian-rational pole algebra only; no assertion that "
            "the Riemann xi right-half-plane pole packet is empty"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("certificate root must be an object")
        result = verify(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"ERROR: {exc}")
        return 2
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
