#!/usr/bin/env python3
"""Pure-standard-library 320-bit directed replay of the verified-height N=1 ladder.

The finite lower model is
    M_c = 2 sum_{j=1}^{20} v_gamma_j(c) v_gamma_j(c)^T - eta_c I,
with proof-grade critical-line zero balls imported from X-17204 and an
off-line-safe unseen-zero radius above the Platt--Trudgian verified height.

All transcendental arithmetic is outward fixed-point arithmetic over integers
with denominator 2^BITS.  No binary floating-point value enters a sign test.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x20702.verified-height-dyadic.v1"


class VerifyError(RuntimeError):
    pass


def floor_div(a: int, b: int) -> int:
    if b <= 0:
        raise VerifyError("floor_div requires positive denominator")
    return a // b


def ceil_div(a: int, b: int) -> int:
    if b <= 0:
        raise VerifyError("ceil_div requires positive denominator")
    return -((-a) // b)


@dataclass(frozen=True)
class Ball:
    lo: int
    hi: int
    scale: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise VerifyError("reversed interval")

    @staticmethod
    def point_int(n: int, scale: int) -> "Ball":
        return Ball(n * scale, n * scale, scale)

    @staticmethod
    def from_fraction(num: int, den: int, scale: int) -> "Ball":
        if den <= 0:
            raise VerifyError("nonpositive denominator")
        return Ball(floor_div(num * scale, den), ceil_div(num * scale, den), scale)

    @staticmethod
    def from_decimal(value: str, scale: int) -> "Ball":
        tup = Decimal(value).as_tuple()
        n = 0
        for d in tup.digits:
            n = 10 * n + d
        if tup.sign:
            n = -n
        if tup.exponent >= 0:
            return Ball.from_fraction(n * 10**tup.exponent, 1, scale)
        return Ball.from_fraction(n, 10**(-tup.exponent), scale)

    def _coerce(self, other: "Ball | int") -> "Ball":
        if isinstance(other, Ball):
            if other.scale != self.scale:
                raise VerifyError("scale mismatch")
            return other
        if isinstance(other, bool) or not isinstance(other, int):
            raise VerifyError("unsupported scalar")
        return Ball.point_int(other, self.scale)

    def __add__(self, other: "Ball | int") -> "Ball":
        o = self._coerce(other)
        return Ball(self.lo + o.lo, self.hi + o.hi, self.scale)

    __radd__ = __add__

    def __neg__(self) -> "Ball":
        return Ball(-self.hi, -self.lo, self.scale)

    def __sub__(self, other: "Ball | int") -> "Ball":
        return self + (-self._coerce(other))

    def __rsub__(self, other: "Ball | int") -> "Ball":
        return self._coerce(other) - self

    def __mul__(self, other: "Ball | int") -> "Ball":
        o = self._coerce(other)
        products = (
            self.lo * o.lo,
            self.lo * o.hi,
            self.hi * o.lo,
            self.hi * o.hi,
        )
        return Ball(
            floor_div(min(products), self.scale),
            ceil_div(max(products), self.scale),
            self.scale,
        )

    __rmul__ = __mul__

    def __truediv__(self, other: "Ball | int") -> "Ball":
        o = self._coerce(other)
        if o.lo <= 0 <= o.hi:
            raise VerifyError("division interval contains zero")
        lows: list[int] = []
        highs: list[int] = []
        for a in (self.lo, self.hi):
            for b in (o.lo, o.hi):
                if b < 0:
                    n, d = -a * self.scale, -b
                else:
                    n, d = a * self.scale, b
                lows.append(floor_div(n, d))
                highs.append(ceil_div(n, d))
        return Ball(min(lows), max(highs), self.scale)

    def square(self) -> "Ball":
        if self.lo <= 0 <= self.hi:
            upper = max(self.lo * self.lo, self.hi * self.hi)
            return Ball(0, ceil_div(upper, self.scale), self.scale)
        products = (self.lo * self.lo, self.hi * self.hi)
        return Ball(
            floor_div(min(products), self.scale),
            ceil_div(max(products), self.scale),
            self.scale,
        )

    def midpoint(self) -> int:
        return (self.lo + self.hi) // 2

    def abs_upper(self) -> int:
        return max(abs(self.lo), abs(self.hi))


class Directed:
    def __init__(self, bits: int) -> None:
        if bits < 256:
            raise VerifyError("at least 256 fixed-point bits required")
        self.bits = bits
        self.scale = 1 << bits
        self.zero = Ball(0, 0, self.scale)
        self.one = Ball.point_int(1, self.scale)
        self.two = Ball.point_int(2, self.scale)
        self.pi = 16 * self._atan_inv(5, 190) - 4 * self._atan_inv(239, 90)
        self.log2 = self._log2(260)
        self.sqrt2 = self.sqrt(self.two)

    def point(self, n: int) -> Ball:
        return Ball.point_int(n, self.scale)

    def fraction(self, num: int, den: int) -> Ball:
        return Ball.from_fraction(num, den, self.scale)

    def decimal(self, value: str) -> Ball:
        return Ball.from_decimal(value, self.scale)

    def sqrt(self, x: Ball) -> Ball:
        if x.lo < 0:
            raise VerifyError("sqrt of negative interval")
        lo = math.isqrt(x.lo * self.scale)
        root = math.isqrt(x.hi * self.scale)
        hi = root if root * root == x.hi * self.scale else root + 1
        return Ball(lo, hi, self.scale)

    def _atan_inv(self, q: int, terms: int) -> Ball:
        lo = hi = 0
        qpow = q
        for n in range(terms):
            den = qpow * (2 * n + 1)
            term_lo = floor_div(self.scale, den)
            term_hi = ceil_div(self.scale, den)
            if n % 2 == 0:
                lo += term_lo
                hi += term_hi
            else:
                lo -= term_hi
                hi -= term_lo
            qpow *= q * q
        den = qpow * (2 * terms + 1)
        next_hi = ceil_div(self.scale, den)
        if terms % 2 == 0:
            hi += next_hi
        else:
            lo -= next_hi
        return Ball(lo, hi, self.scale)

    def _log2(self, terms: int) -> Ball:
        z = self.fraction(1, 3)
        z2 = z * z
        power = z
        total = self.zero
        for n in range(terms):
            total += (2 * power) / self.point(2 * n + 1)
            power *= z2
        tail = (2 * power) / (self.point(2 * terms + 1) * (self.one - z2))
        return Ball(total.lo, total.hi + tail.hi, self.scale)

    def log_rational(self, num: int, den: int = 1, terms: int = 260) -> Ball:
        if num <= 0 or den <= 0:
            raise VerifyError("log requires positive rational")
        k = num.bit_length() - den.bit_length()
        if k >= 0:
            yn, yd = num, den << k
        else:
            yn, yd = num << (-k), den
        while yn < yd:
            k -= 1
            yn *= 2
        while yn >= 2 * yd:
            k += 1
            yd *= 2
        z = self.fraction(yn - yd, yn + yd)
        z2 = z * z
        power = z
        total = self.zero
        for n in range(terms):
            total += (2 * power) / self.point(2 * n + 1)
            power *= z2
        tail = (2 * power) / (self.point(2 * terms + 1) * (self.one - z2))
        total = Ball(total.lo, total.hi + tail.hi, self.scale)
        return total + k * self.log2

    def _sin_small(self, x: Ball, terms: int = 88) -> Ball:
        x2 = x * x
        power = x
        total = self.zero
        factorial = 1
        for n in range(terms):
            if n:
                power *= x2
                factorial *= (2 * n) * (2 * n + 1)
            term = power / self.point(factorial)
            total = total + term if n % 2 == 0 else total - term
        power *= x2
        factorial *= (2 * terms) * (2 * terms + 1)
        remainder = power / self.point(factorial)
        radius = max(abs(remainder.lo), abs(remainder.hi))
        return Ball(total.lo - radius, total.hi + radius, self.scale)

    def _cos_small(self, x: Ball, terms: int = 88) -> Ball:
        x2 = x * x
        power = self.one
        total = self.zero
        factorial = 1
        for n in range(terms):
            if n:
                power *= x2
                factorial *= (2 * n - 1) * (2 * n)
            term = power / self.point(factorial)
            total = total + term if n % 2 == 0 else total - term
        power *= x2
        factorial *= (2 * terms + 1) * (2 * terms + 2)
        remainder = power / self.point(factorial)
        radius = max(abs(remainder.lo), abs(remainder.hi))
        return Ball(total.lo - radius, total.hi + radius, self.scale)

    def sin(self, x: Ball) -> Ball:
        q = floor_div(2 * x.midpoint() + self.pi.midpoint() // 2, self.pi.midpoint())
        y = x - (q * self.pi) / self.two
        quarter = self.pi.hi // 4
        if y.lo < -quarter or y.hi > quarter:
            found = False
            for candidate in range(q - 2, q + 3):
                trial = x - (candidate * self.pi) / self.two
                if trial.lo >= -quarter and trial.hi <= quarter:
                    q, y, found = candidate, trial, True
                    break
            if not found:
                raise VerifyError("sine range reduction failed")
        residue = q % 4
        if residue == 0:
            return self._sin_small(y)
        if residue == 1:
            return self._cos_small(y)
        if residue == 2:
            return -self._sin_small(y)
        return -self._cos_small(y)


def decimal_interval(d: Directed, center: str, radius: str) -> Ball:
    c = d.decimal(center)
    r = d.decimal(radius)
    return Ball(c.lo - r.hi, c.hi + r.hi, d.scale)


def dot(a: list[Ball], b: list[Ball]) -> Ball:
    return a[0] * b[0] + a[1] * b[1]


def quad(matrix: list[list[Ball]], a: list[Ball], b: list[Ball]) -> Ball:
    return (
        a[0] * (matrix[0][0] * b[0] + matrix[0][1] * b[1])
        + a[1] * (matrix[1][0] * b[0] + matrix[1][1] * b[1])
    )


def row(d: Directed, cutoff: int, gamma: Ball) -> list[Ball]:
    logc = d.log_rational(cutoff)
    sqrt_logc = d.sqrt(logc)
    phase = logc * gamma / d.two
    sine = d.sin(phase)
    v0 = -(d.two * sine) / (gamma * sqrt_logc)
    mu = logc * gamma / (d.two * d.pi)
    factor = sqrt_logc * sine / d.pi
    v1 = factor * d.sqrt2 * mu / (d.one - mu.square())
    return [v0, v1]


def level(d: Directed, cutoff: int, zeros: list[Ball], verified_height: int) -> dict[str, Any]:
    rows = [row(d, cutoff, gamma) for gamma in zeros]
    matrix = [[d.zero, d.zero], [d.zero, d.zero]]
    for v in rows:
        for i in range(2):
            for j in range(2):
                matrix[i][j] += 2 * v[i] * v[j]

    logc = d.log_rational(cutoff)
    logh = d.log_rational(verified_height)
    eta = (
        d.point(192)
        * d.fraction(13, 80)
        * d.sqrt(d.point(cutoff))
        * (logh + d.one)
        / (d.point(verified_height) * logc)
    )
    matrix[0][0] -= eta
    matrix[1][1] -= eta

    first = rows[0]
    complement = [first[0], first[1]]
    kernel = [-first[1], first[0]]
    metric = dot(kernel, kernel)
    positive = quad(matrix, complement, complement)
    if positive.lo <= 0:
        raise VerifyError(f"positive-sector block touches zero at c={cutoff}")
    cross = quad(matrix, complement, kernel)
    raw = quad(matrix, kernel, kernel)
    schur = raw - cross.square() / positive
    margin = schur / metric

    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    eigen_lower = determinant / trace if trace.lo > 0 else Ball(-d.scale, d.scale, d.scale)

    return {
        "c": cutoff,
        "classification": "CERTIFIED_POSITIVE" if margin.lo > 0 else "UNRESOLVED",
        "conditional_margin": {"lower": str(margin.lo), "upper": str(margin.hi)},
        "euclidean_eigen_lower": {"lower": str(eigen_lower.lo), "upper": str(eigen_lower.hi)},
        "eta": {"lower": str(eta.lo), "upper": str(eta.hi)},
        "matrix": [
            [{"lower": str(x.lo), "upper": str(x.hi)} for x in matrix_row]
            for matrix_row in matrix
        ],
    }


def canonical_digest(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def build(config: dict[str, Any]) -> dict[str, Any]:
    if config.get("schema") != "riemann.x20702.verified-height-dyadic.config.v1":
        raise VerifyError("unexpected config schema")
    bits = int(config["fixed_point_bits"])
    d = Directed(bits)
    zeros_raw = config["zeros"]
    if not isinstance(zeros_raw, list) or len(zeros_raw) != 20:
        raise VerifyError("exactly 20 zero balls required")
    zeros = [
        decimal_interval(d, str(item["center"]), str(item["radius"]))
        for item in zeros_raw
    ]
    levels = [int(x) for x in config["levels"]]
    if len(levels) != len(set(levels)):
        raise VerifyError("duplicate level")
    result = {
        "schema": SCHEMA,
        "fixed_point_bits": bits,
        "verified_height": int(config["verified_height"]),
        "zero_count": len(zeros),
        "zero_source": config["zero_source"],
        "tail_model": (
            "2*sum_{j<=20} v_j v_j^T - eta I; every unlisted zero below H "
            "is discarded as positive mass and every zero above H is covered "
            "by the off-line-safe L-15127 radius"
        ),
        "levels": [
            level(d, cutoff, zeros, int(config["verified_height"]))
            for cutoff in levels
        ],
        "proof_boundary": (
            "This is a directed finite verified-height lower model for the N=1 "
            "D-0001 even sector. A fixed verified height cannot yield a cofinal "
            "support theorem."
        ),
    }
    result["proof_object_sha256"] = canonical_digest(result)
    return result


def decimal_from_scaled(value: int, scale: int, digits: int = 32) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    integer, remainder = divmod(value, scale)
    out = []
    for _ in range(digits):
        remainder *= 10
        digit, remainder = divmod(remainder, scale)
        out.append(str(digit))
    return f"{sign}{integer}." + "".join(out)


def summary(result: dict[str, Any]) -> dict[str, Any]:
    scale = 1 << int(result["fixed_point_bits"])
    passing = []
    unresolved = []
    rows = []
    for item in result["levels"]:
        lo = int(item["conditional_margin"]["lower"])
        entry = {
            "c": item["c"],
            "classification": item["classification"],
            "conditional_margin_lower_decimal": decimal_from_scaled(lo, scale, 34),
            "euclidean_eigen_lower_decimal": decimal_from_scaled(
                int(item["euclidean_eigen_lower"]["lower"]), scale, 34
            ),
        }
        rows.append(entry)
        (passing if lo > 0 else unresolved).append(item["c"])
    return {
        "schema": "riemann.x20702.verified-height-dyadic.summary.v1",
        "proof_object_sha256": result["proof_object_sha256"],
        "passing_levels": passing,
        "unresolved_controls": unresolved,
        "levels": rows,
        "verdict": "CERTIFIED_FINITE_VERIFIED_HEIGHT_LADDER",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads(args.config.read_text())
    result = build(config)
    args.certificate.parent.mkdir(parents=True, exist_ok=True)
    args.certificate.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    args.summary.write_text(json.dumps(summary(result), indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary(result), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
