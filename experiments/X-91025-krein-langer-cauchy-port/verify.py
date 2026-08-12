#!/usr/bin/env python3
"""Exact finite regression for L-91034.

Checks the product-kernel decomposition, model-space port expansion,
single-pole rank-one formula, and the one-pole cancellation firewall.
It proves finite algebra only; it does not certify the xi canonical
factorization, absence of zero ports, or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class QC:
    re: Fraction
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "QC":
        o = as_qc(other)
        return QC(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self) -> "QC":
        return QC(-self.re, -self.im)

    def __sub__(self, other: object) -> "QC":
        return self + (-as_qc(other))

    def __rsub__(self, other: object) -> "QC":
        return as_qc(other) - self

    def __mul__(self, other: object) -> "QC":
        o = as_qc(other)
        return QC(
            self.re * o.re - self.im * o.im,
            self.re * o.im + self.im * o.re,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "QC":
        return QC(self.re, -self.im)

    def norm2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def inverse(self) -> "QC":
        n = self.norm2()
        if n == 0:
            raise ZeroDivisionError("zero rational complex number")
        return QC(self.re / n, -self.im / n)

    def __truediv__(self, other: object) -> "QC":
        return self * as_qc(other).inverse()

    def __rtruediv__(self, other: object) -> "QC":
        return as_qc(other) / self

    def __pow__(self, exponent: int) -> "QC":
        if exponent < 0:
            return self.inverse() ** (-exponent)
        out = QC(Fraction(1))
        for _ in range(exponent):
            out *= self
        return out


def as_qc(value: object) -> QC:
    if isinstance(value, QC):
        return value
    if isinstance(value, Fraction):
        return QC(value)
    if isinstance(value, int):
        return QC(Fraction(value))
    raise TypeError(f"unsupported QC coercion: {type(value)!r}")


def blaschke(p: QC, z: QC) -> QC:
    return (z - p) / (z + p.conjugate())


def product(values: list[QC]) -> QC:
    out = QC(Fraction(1))
    for value in values:
        out *= value
    return out


def blaschke_product(points: list[QC], z: QC) -> QC:
    return product([blaschke(p, z) for p in points])


def kernel(fz: QC, fw: QC, z: QC, w: QC) -> QC:
    return (1 - fz * fw.conjugate()) / (z + w.conjugate())


def multiplier(z: QC) -> QC:
    return (z + Fraction(1, 4)) / (z + Fraction(7, 5))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=None)
    args = parser.parse_args()

    deterministic = [
        QC(Fraction(1, 2)),
        QC(Fraction(1, 2)),
        QC(Fraction(2, 3)),
        QC(Fraction(2, 3)),
    ]
    zero_poles = [
        QC(Fraction(1, 3), Fraction(2, 5)),
        QC(Fraction(2, 7), Fraction(1, 2)),
    ]
    analytic_zeros = [
        QC(Fraction(3, 4), Fraction(1, 5)),
        QC(Fraction(4, 5), Fraction(-1, 3)),
    ]
    points = [
        QC(Fraction(5, 4), Fraction(1, 7)),
        QC(Fraction(7, 6), Fraction(-2, 9)),
        QC(Fraction(9, 8), Fraction(3, 10)),
        QC(Fraction(11, 9), Fraction(-1, 4)),
    ]

    checks = 0
    decomposition_checks = 0
    product_rule_checks = 0
    rank_one_checks = 0
    model_space_checks = 0
    firewall_checks = 0

    for z in points:
        for w in points:
            dz = blaschke_product(deterministic, z)
            dw = blaschke_product(deterministic, w)
            zz = blaschke_product(zero_poles, z)
            zw = blaschke_product(zero_poles, w)
            az = blaschke_product(analytic_zeros, z)
            aw = blaschke_product(analytic_zeros, w)

            theta_z = az / zz
            theta_w = aw / zw
            inner_z = dz * az
            inner_w = dw * aw

            source = (
                multiplier(z) * multiplier(w).conjugate()
                / (dz * zz * (dw * zw).conjugate())
                * kernel(inner_z, inner_w, z, w)
            )
            critical = (
                multiplier(z) * multiplier(w).conjugate()
                * kernel(theta_z, theta_w, z, w)
            )
            stable = (
                multiplier(z) * multiplier(w).conjugate()
                / (dz * zz * (dw * zw).conjugate())
                * kernel(dz, dw, z, w)
            )
            hyperbolic = (
                multiplier(z) * multiplier(w).conjugate()
                / (zz * zw.conjugate())
                * kernel(zz, zw, z, w)
            )
            assert source == critical + stable + hyperbolic
            decomposition_checks += 1

            fg_z = dz * zz
            fg_w = dw * zw
            lhs = kernel(fg_z, fg_w, z, w)
            rhs = kernel(dz, dw, z, w) + dz * dw.conjugate() * kernel(
                zz, zw, z, w
            )
            assert lhs == rhs
            product_rule_checks += 1

    simple_pole = QC(Fraction(2, 5), Fraction(1, 3))
    for z in points:
        for w in points:
            bz = blaschke(simple_pole, z)
            bw = blaschke(simple_pole, w)
            lhs = kernel(bz, bw, z, w) / (bz * bw.conjugate())
            rhs = QC(2 * simple_pole.re) / (
                (z - simple_pole) * (w.conjugate() - simple_pole.conjugate())
            )
            assert lhs == rhs
            rank_one_checks += 1

    tm_points = zero_poles + deterministic[:2]
    for z in points:
        for w in points:
            bz = blaschke_product(tm_points, z)
            bw = blaschke_product(tm_points, w)
            lhs = kernel(bz, bw, z, w)
            rhs = QC(Fraction(0))
            prefix_z = QC(Fraction(1))
            prefix_w = QC(Fraction(1))
            for p in tm_points:
                rhs += (
                    QC(2 * p.re)
                    * prefix_z
                    * prefix_w.conjugate()
                    / ((z + p.conjugate()) * (w.conjugate() + p))
                )
                prefix_z *= blaschke(p, z)
                prefix_w *= blaschke(p, w)
            assert lhs == rhs
            model_space_checks += 1

    # Exact one-pole control: safe source kernel is zero, while the critical
    # kernel is cancelled by a nonzero positive pole port.
    for z in points:
        for w in points:
            bz = blaschke(simple_pole, z)
            bw = blaschke(simple_pole, w)
            theta_z = 1 / bz
            theta_w = 1 / bw
            critical = kernel(theta_z, theta_w, z, w)
            pole_port = kernel(bz, bw, z, w) / (bz * bw.conjugate())
            assert critical + pole_port == QC(Fraction(0))
            firewall_checks += 1

    checks = (
        decomposition_checks
        + product_rule_checks
        + rank_one_checks
        + model_space_checks
        + firewall_checks
    )

    proof_object = {
        "deterministic_points": [
            [str(z.re), str(z.im)] for z in deterministic
        ],
        "zero_poles": [[str(z.re), str(z.im)] for z in zero_poles],
        "analytic_zeros": [
            [str(z.re), str(z.im)] for z in analytic_zeros
        ],
        "evaluation_points": [[str(z.re), str(z.im)] for z in points],
    }
    digest = hashlib.sha256(
        json.dumps(proof_object, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    result: dict[str, Any] = {
        "classification": "PASS_KREIN_LANGER_CAUCHY_PORT_DECOMPOSITION",
        "checks": checks,
        "decomposition_checks": decomposition_checks,
        "product_rule_checks": product_rule_checks,
        "rank_one_port_checks": rank_one_checks,
        "takenaka_malmquist_checks": model_space_checks,
        "one_pole_firewall_checks": firewall_checks,
        "proof_object_sha256": digest,
        "scope": (
            "exact finite rational-complex kernel algebra only; "
            "does not certify the infinite xi Blaschke factorization, "
            "identify the arithmetic Hankel Stinespring kernel, "
            "remove zero ports, or prove RH"
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json is None:
        print(text, end="")
    else:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(text, encoding="utf-8")
    print("PASS_KREIN_LANGER_CAUCHY_PORT_DECOMPOSITION")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
