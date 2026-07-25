#!/usr/bin/env python3
"""Exact synthetic checker for L-8301/L-8302/T-8301.

Uses only Python integers and fractions.Fraction. It does not construct a
Riemann--Weil matrix or evaluate any prime phase.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable

SCHEMA = "riemann.endpoint-green-threshold.synthetic.v1"


class CertificateError(ValueError):
    pass


def parse_fraction(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not a rational string") from exc
    if isinstance(value, dict):
        try:
            num, den = value["numerator"], value["denominator"]
        except KeyError as exc:
            raise CertificateError(f"{name} needs numerator and denominator") from exc
        if isinstance(num, bool) or isinstance(den, bool):
            raise CertificateError(f"{name} numerator/denominator must not be boolean")
        try:
            return Fraction(int(num), int(den))
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is malformed") from exc
    raise CertificateError(f"{name} must be integer, rational string, or fraction object")


@dataclass(frozen=True)
class GQ:
    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __add__(self, other: object) -> "GQ":
        z = as_gq(other)
        return GQ(self.re + z.re, self.im + z.im)

    __radd__ = __add__

    def __neg__(self) -> "GQ":
        return GQ(-self.re, -self.im)

    def __sub__(self, other: object) -> "GQ":
        return self + (-as_gq(other))

    def __rsub__(self, other: object) -> "GQ":
        return as_gq(other) - self

    def __mul__(self, other: object) -> "GQ":
        z = as_gq(other)
        return GQ(self.re * z.re - self.im * z.im,
                  self.re * z.im + self.im * z.re)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "GQ":
        z = as_gq(other)
        den = z.abs2()
        if den == 0:
            raise ZeroDivisionError("Gaussian rational division by zero")
        return self * GQ(z.re / den, -z.im / den)

    def conj(self) -> "GQ":
        return GQ(self.re, -self.im)

    def abs2(self) -> Fraction:
        return self.re * self.re + self.im * self.im

    def is_zero(self) -> bool:
        return self.re == 0 and self.im == 0

    def to_json(self) -> dict[str, str]:
        return {"re": str(self.re), "im": str(self.im)}


def as_gq(value: object) -> GQ:
    if isinstance(value, GQ):
        return value
    if isinstance(value, Fraction):
        return GQ(value)
    if isinstance(value, int):
        return GQ(Fraction(value))
    raise TypeError(f"cannot convert {type(value)!r} to GQ")


def parse_gq(value: Any, name: str) -> GQ:
    if isinstance(value, (int, str)) and not isinstance(value, bool):
        return GQ(parse_fraction(value, name))
    if not isinstance(value, dict):
        raise CertificateError(f"{name} must be a Gaussian-rational object")
    return GQ(parse_fraction(value.get("re", 0), f"{name}.re"),
              parse_fraction(value.get("im", 0), f"{name}.im"))


Matrix = list[list[GQ]]
Vector = list[GQ]


def parse_matrix(value: Any, name: str) -> Matrix:
    if not isinstance(value, list) or not value:
        raise CertificateError(f"{name} must be a nonempty array")
    n = len(value)
    out: Matrix = []
    for i, row in enumerate(value):
        if not isinstance(row, list) or len(row) != n:
            raise CertificateError(f"{name}[{i}] must have length {n}")
        out.append([parse_gq(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)])
    return out


def parse_vector(value: Any, name: str, n: int) -> Vector:
    if not isinstance(value, list) or len(value) != n:
        raise CertificateError(f"{name} must have length {n}")
    return [parse_gq(x, f"{name}[{i}]") for i, x in enumerate(value)]


def identity(n: int) -> Matrix:
    return [[GQ(1 if i == j else 0) for j in range(n)] for i in range(n)]


def is_hermitian(a: Matrix) -> bool:
    n = len(a)
    return all(a[i][j] == a[j][i].conj() for i in range(n) for j in range(n))


def matvec(a: Matrix, x: Vector) -> Vector:
    return [sum((a[i][j] * x[j] for j in range(len(x))), GQ()) for i in range(len(a))]


def inner(x: Vector, y: Vector) -> GQ:
    return sum((xj.conj() * yj for xj, yj in zip(x, y)), GQ())


def vector_norm2(x: Vector) -> Fraction:
    return sum((z.abs2() for z in x), Fraction(0))


def invert(a: Matrix) -> Matrix:
    n = len(a)
    aug = [a[i][:] + identity(n)[i] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if not aug[r][col].is_zero()), None)
        if pivot is None:
            raise CertificateError("matrix is singular")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        p = aug[col][col]
        aug[col] = [z / p for z in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            if factor.is_zero():
                continue
            aug[r] = [aug[r][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def determinant(a: Matrix) -> GQ:
    n = len(a)
    m = [row[:] for row in a]
    det = GQ(1)
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if not m[r][col].is_zero()), None)
        if pivot is None:
            return GQ()
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            sign *= -1
        p = m[col][col]
        det = det * p
        for r in range(col + 1, n):
            factor = m[r][col] / p
            for j in range(col + 1, n):
                m[r][j] = m[r][j] - factor * m[col][j]
    return det * sign


def psd_ldl(a: Matrix, *, strict: bool) -> bool:
    if not is_hermitian(a):
        return False
    n = len(a)
    l = [[GQ(1 if i == j else 0) for j in range(n)] for i in range(n)]
    d: list[Fraction] = []
    for j in range(n):
        pivot = a[j][j]
        for k in range(j):
            pivot = pivot - l[j][k] * l[j][k].conj() * d[k]
        if pivot.im != 0:
            return False
        dj = pivot.re
        if dj < 0 or (strict and dj == 0):
            return False
        d.append(dj)
        for i in range(j + 1, n):
            num = a[i][j]
            for k in range(j):
                num = num - l[i][k] * l[j][k].conj() * d[k]
            if dj == 0:
                if not num.is_zero():
                    return False
                l[i][j] = GQ()
            else:
                l[i][j] = num / dj
    return True


def matrix_minus_mu(a: Matrix, mu: Fraction) -> Matrix:
    out = [row[:] for row in a]
    for i in range(len(out)):
        out[i][i] = out[i][i] - mu
    return out


def corner_matrix(n: int, left: int, right: int, zeta: GQ) -> Matrix:
    c = [[GQ() for _ in range(n)] for _ in range(n)]
    c[left][right] = zeta
    c[right][left] = zeta.conj()
    return c


def matrix_linear_combination(a: Matrix, b: Matrix, scale_b: Fraction) -> Matrix:
    return [[a[i][j] + b[i][j] * scale_b for j in range(len(a))] for i in range(len(a))]


def sqrt_bounds(x: Fraction, bits: int = 160) -> tuple[Fraction, Fraction]:
    if x < 0 or bits < 1:
        raise CertificateError("invalid square-root request")
    if x == 0:
        return Fraction(0), Fraction(0)
    scale = 1 << bits
    floor_scaled_square = (x.numerator * scale * scale) // x.denominator
    lo_int = math.isqrt(floor_scaled_square)
    lo = Fraction(lo_int, scale)
    if lo * lo == x:
        return lo, lo
    return lo, Fraction(lo_int + 1, scale)


def endpoint_green(h: Matrix, left: int, right: int, zeta: GQ) -> dict[str, Any]:
    inv = invert(h)
    a, b, d = inv[left][left], inv[left][right], inv[right][right]
    if a.im != 0 or d.im != 0:
        raise AssertionError("Hermitian inverse diagonal is not real")
    disc = a.re * d.re - b.abs2()
    if disc <= 0:
        raise CertificateError("endpoint Green matrix is not positive definite")
    r = (zeta.conj() * b).re
    root_lo, root_hi = sqrt_bounds(r * r + disc)
    return {"a": a.re, "b": b, "d": d.re, "D": disc, "r": r,
            "lambda_lower": r + root_lo, "lambda_upper": r + root_hi}


def fraction_json(x: Fraction) -> dict[str, str]:
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}


def verify_case(case: dict[str, Any]) -> dict[str, Any]:
    case_id = case.get("id")
    if not isinstance(case_id, str) or not case_id:
        raise CertificateError("case id must be nonempty")
    h = parse_matrix(case.get("H"), f"{case_id}.H")
    n = len(h)
    if not is_hermitian(h) or not psd_ldl(h, strict=True):
        raise CertificateError(f"{case_id}: H must be positive-definite Hermitian")
    endpoints = case.get("endpoints")
    if (not isinstance(endpoints, list) or len(endpoints) != 2 or
            any(isinstance(x, bool) or not isinstance(x, int) for x in endpoints)):
        raise CertificateError(f"{case_id}: endpoints must be two integers")
    left, right = endpoints
    if not (0 <= left < n and 0 <= right < n and left != right):
        raise CertificateError(f"{case_id}: invalid endpoints")
    zeta = parse_gq(case.get("phase"), f"{case_id}.phase")
    if zeta.abs2() != 1:
        raise CertificateError(f"{case_id}: phase must have exact unit modulus")
    tau = parse_fraction(case.get("tau"), f"{case_id}.tau")
    mu = parse_fraction(case.get("mu"), f"{case_id}.mu")
    beta = parse_fraction(case.get("beta"), f"{case_id}.beta")
    if tau < 0 or mu <= 0 or beta < 0:
        raise CertificateError(f"{case_id}: require tau>=0, mu>0, beta>=0")
    if not psd_ldl(matrix_minus_mu(h, mu), strict=False):
        raise CertificateError(f"{case_id}: claimed mu is not a lower spectral floor")

    g = endpoint_green(h, left, right, zeta)
    positive_moat = mu * (1 - tau * g["lambda_upper"]) - beta
    negative_moat = mu * (tau * g["lambda_lower"] - 1) - beta
    if positive_moat > 0:
        status = "ROBUST_POSITIVE"
    elif negative_moat > 0:
        status = "ROBUST_CROSSING"
    else:
        status = "UNRESOLVED_MOAT"
    if case.get("expected_status") != status:
        raise CertificateError(f"{case_id}: expected {case.get('expected_status')!r}, reconstructed {status!r}")

    c = corner_matrix(n, left, right, zeta)
    ht = matrix_linear_combination(h, c, -tau)
    det_h, det_ht = determinant(h), determinant(ht)
    if det_h.im != 0 or det_ht.im != 0 or det_h.re <= 0:
        raise AssertionError("determinant audit failed")
    ratio = det_ht.re / det_h.re
    secular = 1 - 2 * g["r"] * tau - g["D"] * tau * tau
    if ratio != secular:
        raise AssertionError(f"{case_id}: determinant ratio identity failed")

    leading_susceptibility = None
    if "leading_vector" in case:
        v = parse_vector(case["leading_vector"], f"{case_id}.leading_vector", n)
        hv, cv = inner(v, matvec(h, v)), inner(v, matvec(c, v))
        if hv.im != 0 or cv.im != 0 or hv.re <= 0:
            raise CertificateError(f"{case_id}: invalid leading vector")
        leading_susceptibility = cv.re / hv.re
        claimed = parse_fraction(case.get("claimed_leading_susceptibility"),
                                 f"{case_id}.claimed_leading_susceptibility")
        if leading_susceptibility != claimed:
            raise CertificateError(f"{case_id}: leading susceptibility mismatch")

    return {
        "id": case_id,
        "status": status,
        "green": {"a": fraction_json(g["a"]), "b": g["b"].to_json(),
                  "d": fraction_json(g["d"]), "D": fraction_json(g["D"]),
                  "r": fraction_json(g["r"])},
        "lambda_interval": {"lower": fraction_json(g["lambda_lower"]),
                            "upper": fraction_json(g["lambda_upper"])},
        "positive_moat": fraction_json(positive_moat),
        "negative_moat": fraction_json(negative_moat),
        "determinant_ratio": fraction_json(ratio),
        "leading_susceptibility": (None if leading_susceptibility is None
                                   else fraction_json(leading_susceptibility)),
    }


def residual_green_enclosure(h: Matrix, left: int, right: int, mu: Fraction,
                             yu: Vector, yw: Vector) -> dict[str, Any]:
    n = len(h)
    u = [GQ(1 if i == left else 0) for i in range(n)]
    w = [GQ(1 if i == right else 0) for i in range(n)]
    hyu, hyw = matvec(h, yu), matvec(h, yw)
    ru = [u[i] - hyu[i] for i in range(n)]
    rw = [w[i] - hyw[i] for i in range(n)]
    _, ru_hi = sqrt_bounds(vector_norm2(ru))
    _, rw_hi = sqrt_bounds(vector_norm2(rw))
    eta_u, eta_w = ru_hi / mu, rw_hi / mu
    return {
        "a_center": inner(u, yu).re, "a_radius": eta_u,
        "d_center": inner(w, yw).re, "d_radius": eta_w,
        "b_center": (inner(u, yw) + inner(w, yu).conj()) / 2,
        "b_radius": (eta_u + eta_w) / 2,
    }


def verify_certificate(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")
    cases = data.get("cases")
    if not isinstance(cases, list) or not cases:
        raise CertificateError("cases must be a nonempty array")
    ids: set[str] = set()
    outputs = []
    for case in cases:
        if not isinstance(case, dict):
            raise CertificateError("each case must be an object")
        if case.get("id") in ids:
            raise CertificateError("duplicate case id")
        ids.add(case.get("id"))
        outputs.append(verify_case(case))
    return {"schema": SCHEMA,
            "status": "EXACT_SYNTHETIC_GREEN_CERTIFICATES_RECONSTRUCTED",
            "cases": outputs,
            "proof_boundary": "finite synthetic Hermitian matrices only; no D-0801 production sign"}


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CertificateError(f"cannot read certificate: {exc}") from exc
    if not isinstance(value, dict):
        raise CertificateError("certificate root must be an object")
    return value


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        output = verify_certificate(load_json(args.certificate))
    except CertificateError as exc:
        print(json.dumps({"schema": SCHEMA, "status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
