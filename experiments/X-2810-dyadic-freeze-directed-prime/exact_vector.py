#!/usr/bin/env python3
"""Exact utilities for dyadic carrier vectors and autocorrelations.

All exact routines use Python integers and fractions.Fraction only.
"""
from __future__ import annotations
from fractions import Fraction
import hashlib
import json
from typing import Any

SCHEMA = "riemann.piecewise-carrier-vector.v1"


class VectorError(ValueError):
    pass


def canonical_sha256(value: Any) -> str:
    text = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(text.encode("ascii")).hexdigest()


def parse_vector(data: dict[str, Any]):
    if data.get("schema") != SCHEMA:
        raise VectorError(f"schema must be {SCHEMA}")
    cells = data.get("cells")
    if isinstance(cells, bool) or not isinstance(cells, int) or cells < 1:
        raise VectorError("cells must be a positive integer")
    vector = data.get("vector")
    if not isinstance(vector, dict):
        raise VectorError("vector must be an object")
    bits = vector.get("scale_bits")
    if isinstance(bits, bool) or not isinstance(bits, int) or bits < 0:
        raise VectorError("scale_bits must be a nonnegative integer")
    real = vector.get("real_numerators")
    imag = vector.get("imag_numerators")
    if not isinstance(real, list) or not isinstance(imag, list):
        raise VectorError("numerator fields must be lists")
    if len(real) != cells or len(imag) != cells:
        raise VectorError("numerator lists must match cells")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in real + imag):
        raise VectorError("all numerators must be integers")
    canonical = {
        "imag_numerators": imag,
        "real_numerators": real,
        "scale_bits": bits,
    }
    digest = canonical_sha256(canonical)
    if data.get("vector_sha256") != digest:
        raise VectorError("vector_sha256 mismatch")
    return cells, bits, real, imag, digest


def norm_numerator(real: list[int], imag: list[int]) -> int:
    return sum(a * a + b * b for a, b in zip(real, imag))


def autocorrelation_numerators(real: list[int], imag: list[int]):
    """Return Gaussian-integer autocorrelations on the common scale 2^(2b)."""
    cells = len(real)
    out_real: list[int] = []
    out_imag: list[int] = []
    for lag in range(cells):
        rr = 0
        ii = 0
        for j in range(cells - lag):
            r0, i0 = real[j], imag[j]
            r1, i1 = real[j + lag], imag[j + lag]
            rr += r1 * r0 + i1 * i0
            ii += i1 * r0 - r1 * i0
        out_real.append(rr)
        out_imag.append(ii)
    return out_real, out_imag


def target_rounding_bound(*, cells: int, bits: int, operator_norm_upper: int) -> Fraction:
    """Return the exact bound 4*M*delta with delta <= ceil(sqrt(K/2))*2^-b."""
    if cells < 1 or bits < 0 or operator_norm_upper < 0:
        raise VectorError("invalid bound input")
    root_upper = 0
    while 2 * root_upper * root_upper < cells:
        root_upper += 1
    return Fraction(4 * operator_norm_upper * root_upper, 1 << bits)


def midpoint_rayleigh_from_lags(coefficients, real: list[int], imag: list[int], bits: int) -> float:
    """Midpoint regression for x^*Sx from lag coefficients; not a certificate."""
    ar, ai = autocorrelation_numerators(real, imag)
    scale = float(1 << (2 * bits))
    total = float(coefficients[0].real) * (ar[0] / scale)
    for lag in range(1, len(coefficients)):
        z = coefficients[lag]
        total += float(z.real) * (ar[lag] / scale) - float(z.imag) * (ai[lag] / scale)
    return total
