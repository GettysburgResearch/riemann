#!/usr/bin/env python3
"""Exact contraction checker for T-21501 finite prime-polygon tangent witnesses.

The checker performs only rational interval arithmetic.  A RIEMANN_DIRECTED
certificate must bind an externally generated complete prime-power prefix and
all directed transcendental inputs.  The checker does not itself evaluate
logarithms, square roots, Euler's constant, pi, Catalan's constant, or the
prime-prefix sums.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import string
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x21501-prime-polygon-tangent.v1"
RESULT_SCHEMA = "riemann.x21501-prime-polygon-tangent-result.v1"
CLASSIFICATIONS = {"SYNTHETIC_MODEL", "RIEMANN_DIRECTED"}


class CertificateError(ValueError):
    pass


def q(value: Any, name: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{name} must not be Boolean")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertificateError(f"{name} is not rational") from exc
    raise CertificateError(f"{name} must be an integer or rational string")


def fstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


@dataclass(frozen=True)
class Iv:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise CertificateError("reversed interval")

    def __add__(self, other: "Iv | Fraction | int") -> "Iv":
        rhs = other if isinstance(other, Iv) else Iv(Fraction(other), Fraction(other))
        return Iv(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "Iv":
        return Iv(-self.hi, -self.lo)

    def __sub__(self, other: "Iv | Fraction | int") -> "Iv":
        rhs = other if isinstance(other, Iv) else Iv(Fraction(other), Fraction(other))
        return self + (-rhs)

    def __rsub__(self, other: "Fraction | int") -> "Iv":
        return Iv(Fraction(other), Fraction(other)) - self

    def __mul__(self, other: "Iv | Fraction | int") -> "Iv":
        rhs = other if isinstance(other, Iv) else Iv(Fraction(other), Fraction(other))
        vals = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return Iv(min(vals), max(vals))

    __rmul__ = __mul__


def interval(raw: Any, name: str) -> Iv:
    if not isinstance(raw, dict):
        raise CertificateError(f"{name} must be an interval object")
    return Iv(q(raw.get("lower"), f"{name}.lower"), q(raw.get("upper"), f"{name}.upper"))


def ivjson(value: Iv) -> dict[str, str]:
    return {"lower": fstr(value.lo), "upper": fstr(value.hi)}


def check_sha(value: Any, name: str) -> str:
    if not isinstance(value, str) or len(value) != 64 or any(c not in string.hexdigits for c in value):
        raise CertificateError(f"{name} must be a 64-character hexadecimal digest")
    return value.lower()


def canonical_sha(obj: dict[str, Any]) -> str:
    payload = dict(obj)
    payload.pop("proof_object_sha256", None)
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(raw.encode("ascii")).hexdigest()


def finite_series_interval(r: Fraction, terms: int) -> Iv:
    """Enclose sum_{k>=1} r^{-(4k+1)}/(4k+1)^2 exactly.

    The lower endpoint is the retained positive partial sum.  For the omitted
    tail, each successive term is at most r^-4 times its predecessor, so the
    first omitted term divided by 1-r^-4 is a rigorous upper bound.
    """
    if terms < 0:
        raise CertificateError("series_terms must be nonnegative")
    partial = Fraction(0)
    for k in range(1, terms + 1):
        m = 4 * k + 1
        partial += Fraction(1, m * m) / (r**m)
    first_m = 4 * (terms + 1) + 1
    first_omitted = Fraction(1, first_m * first_m) / (r**first_m)
    ratio = Fraction(1, 1) / (r**4)
    if ratio >= 1:
        raise CertificateError("series tail ratio is not contractive")
    tail_upper = first_omitted / (1 - ratio)
    return Iv(partial, partial + tail_upper)


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(data, dict) or data.get("schema") != SCHEMA:
        raise CertificateError("schema mismatch")
    classification = data.get("classification")
    if classification not in CLASSIFICATIONS:
        raise CertificateError("invalid classification")

    A = interval(data.get("A_prefix"), "A_prefix")
    B = interval(data.get("B_prefix"), "B_prefix")
    log_r = interval(data.get("log_r"), "log_r")
    kappa = interval(data.get("kappa"), "kappa")
    C0 = interval(data.get("C0"), "C0")
    r = q(data.get("trial_r"), "trial_r")
    terms_raw = data.get("series_terms")
    if isinstance(terms_raw, bool) or not isinstance(terms_raw, int):
        raise CertificateError("series_terms must be an integer")

    if A.lo < 0 or B.lo < 0:
        raise CertificateError("prime-prefix moments must be nonnegative")
    if r <= 1 or r * r < 2:
        raise CertificateError("trial_r must satisfy r>=sqrt(2)")
    if log_r.lo <= 0:
        raise CertificateError("log_r must be positive")

    bindings: dict[str, Any] = {}
    if classification == "RIEMANN_DIRECTED":
        raw = data.get("prefix_binding")
        if not isinstance(raw, dict):
            raise CertificateError("RIEMANN_DIRECTED requires prefix_binding")
        endpoint = raw.get("complete_through_prime_power")
        if isinstance(endpoint, bool) or not isinstance(endpoint, int) or endpoint < 2:
            raise CertificateError("invalid complete prime-power endpoint")
        bindings = {
            "complete_through_prime_power": endpoint,
            "manifest_sha256": check_sha(raw.get("manifest_sha256"), "manifest_sha256"),
            "transcendental_producer_sha256": check_sha(
                raw.get("transcendental_producer_sha256"), "transcendental_producer_sha256"
            ),
            "constant_source_sha256": check_sha(
                raw.get("constant_source_sha256"), "constant_source_sha256"
            ),
        }

    series = finite_series_interval(r, terms_raw)

    # W_j(r)=2 A log r - 4r - kappa log r - C0 + 4 S_2(r) - B.
    witness = (
        2 * A * log_r
        - 4 * r
        - kappa * log_r
        - C0
        + 4 * series
        - B
    )

    if witness.lo > 0:
        verdict = (
            "CERTIFIED_RH_FALSE_PRIME_POLYGON_TANGENT"
            if classification == "RIEMANN_DIRECTED"
            else "SYNTHETIC_POSITIVE_TANGENT_WITNESS"
        )
    elif witness.hi <= 0:
        verdict = "NO_VIOLATION_AT_THIS_TRIAL_TANGENT"
    else:
        verdict = "UNRESOLVED_INTERVAL_OVERLAP"

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "classification": classification,
        "bindings": bindings,
        "trial_r": fstr(r),
        "series_terms": terms_raw,
        "series_interval": ivjson(series),
        "A_prefix": ivjson(A),
        "B_prefix": ivjson(B),
        "log_r": ivjson(log_r),
        "kappa": ivjson(kappa),
        "C0": ivjson(C0),
        "witness_interval": ivjson(witness),
        "verdict": verdict,
        "proof_boundary": (
            "Exact rational interval contraction of T-21501.7 only. A RIEMANN_DIRECTED "
            "verdict additionally depends on the bound complete prime-power manifest, "
            "directed logarithm/square-root producer, and directed archimedean constants."
        ),
    }
    result["proof_object_sha256"] = canonical_sha(result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.certificate.read_text(encoding="utf-8"))
        result = verify(data)
        code = 0
    except (OSError, json.JSONDecodeError, CertificateError, KeyError) as exc:
        result = {
            "schema": RESULT_SCHEMA,
            "classification": "REJECTED",
            "reason": str(exc),
        }
        code = 2
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
