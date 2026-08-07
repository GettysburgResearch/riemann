#!/usr/bin/env python3
"""Fail-closed exact replay for the finite carry-envelope algebra."""
from __future__ import annotations
import argparse, hashlib, json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x23801-carry-envelope.v1"
RESULT = "riemann.x23801-carry-envelope-result.v1"

class CertError(ValueError):
    pass

def frac(v: Any, name: str) -> Fraction:
    if isinstance(v, bool):
        raise CertError(f"{name} must not be Boolean")
    if isinstance(v, int):
        return Fraction(v)
    if isinstance(v, str):
        try:
            return Fraction(v)
        except (ValueError, ZeroDivisionError) as exc:
            raise CertError(f"{name} must be rational") from exc
    raise CertError(f"{name} must be integer or rational string")

def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"

def mobius(N: int) -> list[int]:
    mu = [0] * (N + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (N + 1)
    for n in range(2, N + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > N:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu

def beta(n: int, q: int) -> Fraction:
    if not (2 <= q <= n):
        return Fraction(0)
    a, r = divmod(n, q)
    return Fraction(a * (q - 1 - r), n + 1)

def canonical_sha(obj: dict[str, Any]) -> str:
    x = dict(obj)
    x.pop("proof_object_sha256", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

def parse_map(obj: Any, lo: int, hi: int, name: str) -> dict[int, Fraction]:
    if not isinstance(obj, dict):
        raise CertError(f"{name} must be object")
    expected = {str(i) for i in range(lo, hi + 1)}
    if set(obj) != expected:
        raise CertError(f"{name} keys mismatch")
    return {i: frac(obj[str(i)], f"{name}[{i}]") for i in range(lo, hi + 1)}

def verify(payload: dict[str, Any]) -> dict[str, Any]:
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise CertError("schema mismatch")
    X = payload.get("X")
    if isinstance(X, bool) or not isinstance(X, int) or X < 2:
        raise CertError("X must be integer >=2")

    w = parse_map(payload.get("weights"), 2, X, "weights")
    P = parse_map(payload.get("profile"), 2, X + 2, "profile")
    d_claim = parse_map(payload.get("claimed_d"), 2, X, "claimed_d")
    rho_claim = parse_map(payload.get("claimed_residual"), 2, X, "claimed_residual")
    if P[X + 1] or P[X + 2]:
        raise CertError("terminal profile values must be zero")

    d: dict[int, Fraction] = {}
    for n in range(2, X + 1):
        d[n] = Fraction(n + 1) * (P[n] - 2 * P[n + 1] + P[n + 2])
        if d[n] != d_claim[n]:
            raise CertError(f"claimed d mismatch at {n}")
        if d[n] < 0:
            raise CertError(f"negative packing coefficient at {n}")

    rho: dict[int, Fraction] = {}
    for q in range(2, X + 1):
        used = sum((d[n] * beta(n, q) for n in range(q, X + 1)), Fraction(0))
        rho[q] = w[q] - used
        if rho[q] != rho_claim[q]:
            raise CertError(f"claimed residual mismatch at {q}")
        if rho[q] < 0:
            raise CertError(f"infeasible residual at {q}")

    mu = mobius(X)
    u = {
        m: sum((Fraction(mu[k]) * w[m * k] for k in range(1, X // m + 1)), Fraction(0))
        for m in range(2, X + 1)
    }
    U: dict[int, Fraction] = {X + 1: Fraction(0)}
    for j in range(X, 1, -1):
        U[j] = U[j + 1] + u[j]
    F = {j: U[j] / Fraction(j - 1) for j in range(2, X + 1)}
    F[X + 1] = F[X + 2] = Fraction(0)

    v = {
        m: Fraction(m - 1) * (F[m] - P[m])
        - Fraction(m) * (F[m + 1] - P[m + 1])
        for m in range(2, X + 1)
    }
    rho2 = {
        q: sum((v[q * k] for k in range(1, X // q + 1)), Fraction(0))
        for q in range(2, X + 1)
    }
    if rho2 != rho:
        raise CertError("Mobius residual reconstruction mismatch")

    mass = sum((Fraction(n) * d[n] for n in range(2, X + 1)), Fraction(0))
    mass_profile = 6 * P[2] + 2 * sum((P[j] for j in range(4, X + 1)), Fraction(0))
    if mass != mass_profile:
        raise CertError("mass telescope failed")
    total = sum(d.values(), Fraction(0))
    total_profile = 3 * P[2] - 2 * P[3]
    if total != total_profile:
        raise CertError("coefficient telescope failed")

    out: dict[str, Any] = {
        "schema": RESULT,
        "classification": "EXACT_CARRY_ENVELOPE_ALGEBRA_VERIFIED",
        "X": X,
        "packing_mass": fstr(mass),
        "packing_total": fstr(total),
        "residual_total": fstr(sum(rho.values(), Fraction(0))),
        "minimum_residual": fstr(min(rho.values())),
        "minimum_curvature": fstr(min(d.values())),
        "proof_boundary": (
            "Exact finite carry, Mobius-curvature, residual, and telescope algebra only; "
            "no logarithmic prime-ramp, reflected contraction, asymptotic packing theorem, or RH claim."
        ),
    }
    out["proof_object_sha256"] = canonical_sha(out)
    return out

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.certificate.read_text())
        out = verify(payload)
        code = 0
    except (OSError, json.JSONDecodeError, KeyError, CertError) as exc:
        out = {"schema": RESULT, "classification": "REJECTED", "reason": str(exc)}
        code = 2
    text = json.dumps(out, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")
    return code

if __name__ == "__main__":
    raise SystemExit(main())
