#!/usr/bin/env python3
"""Exact checker for the cumulative Weyl / Green-lift / Jordan energy identities."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any

SCHEMA = "riemann.x15410-cumulative-weyl-green.synthetic.v1"


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


def matrix(raw: Any, name: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw:
        raise CertificateError(f"{name} must be a nonempty matrix")
    out = []
    width = None
    for i, row in enumerate(raw):
        if not isinstance(row, list) or not row:
            raise CertificateError(f"{name}[{i}] must be a nonempty row")
        parsed = [frac(x, f"{name}[{i}][{j}]") for j, x in enumerate(row)]
        if width is None:
            width = len(parsed)
        elif len(parsed) != width:
            raise CertificateError(f"{name} rows must have equal length")
        out.append(parsed)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    if len(a[0]) != len(b):
        raise CertificateError("matrix shape mismatch")
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def ldl_psd(a):
    if len(a) != len(a[0]):
        raise CertificateError("PSD matrix must be square")
    n = len(a)
    if any(a[i][j] != a[j][i] for i in range(n) for j in range(n)):
        raise CertificateError("PSD matrix must be symmetric")
    ell = eye(n)
    pivots = [Fraction(0)] * n
    for i in range(n):
        pivots[i] = a[i][i] - sum(
            ell[i][k] * ell[i][k] * pivots[k] for k in range(i)
        )
        if pivots[i] < 0:
            return False, pivots
        for j in range(i + 1, n):
            numerator = a[j][i] - sum(
                ell[j][k] * ell[i][k] * pivots[k] for k in range(i)
            )
            if pivots[i] == 0:
                if numerator != 0:
                    return False, pivots
                ell[j][i] = Fraction(0)
            else:
                ell[j][i] = numerator / pivots[i]
    return True, pivots


def prime_factors(n: int) -> list[int]:
    factors = []
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            factors.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        factors.append(m)
    return factors


def jordan(n: int, exponent: int) -> int:
    if n <= 0 or exponent <= 0:
        raise CertificateError("Jordan inputs must be positive")
    value = n**exponent
    for p in prime_factors(n):
        value = value * (p**exponent - 1) // p**exponent
    return value


def verify(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("schema") != SCHEMA:
        raise CertificateError(f"schema must be {SCHEMA!r}")

    flow = data.get("flow_control")
    if not isinstance(flow, dict):
        raise CertificateError("flow_control must be an object")
    y = frac(flow.get("y"), "flow_control.y")
    q = frac(flow.get("q"), "flow_control.q")
    if y <= 0 or q <= 0:
        raise CertificateError("flow y and q must be positive")
    derivative_weight = y * (q + 1 / q)
    weyl_weight = derivative_weight / 4
    if frac(flow.get("claimed_derivative_weight"), "flow claimed derivative") != derivative_weight:
        raise CertificateError("false horizontal derivative weight")
    if frac(flow.get("claimed_weyl_weight"), "flow claimed Weyl") != weyl_weight:
        raise CertificateError("false Weyl weight")
    if derivative_weight != 4 * weyl_weight:
        raise CertificateError("flow factor-four identity failed")

    endpoint = data.get("endpoint_energy")
    if not isinstance(endpoint, dict):
        raise CertificateError("endpoint_energy must be an object")
    plus_sq = frac(endpoint.get("plus_norm_squared"), "endpoint plus")
    minus_sq = frac(endpoint.get("minus_norm_squared"), "endpoint minus")
    if plus_sq < 0 or minus_sq < 0:
        raise CertificateError("endpoint squared norms must be nonnegative")
    cumulative = (plus_sq - minus_sq) / 2
    if frac(endpoint.get("claimed_cumulative_energy"), "endpoint cumulative") != cumulative:
        raise CertificateError("false endpoint cumulative energy")

    green = data.get("green_control")
    if not isinstance(green, dict):
        raise CertificateError("green_control must be an object")
    c = matrix(green.get("C"), "green.C")
    e = matrix(green.get("E"), "green.E")
    k = matrix(green.get("K"), "green.K")
    if matmul(c, e) != eye(len(c)):
        raise CertificateError("C E is not the identity")
    k_defect = matsub(eye(len(k)), matmul(transpose(k), k))
    ok_k, _ = ldl_psd(k_defect)
    if not ok_k:
        raise CertificateError("K is not a contraction")
    t = matmul(matmul(c, k), e)
    supplied_t = matrix(green.get("claimed_T"), "green.claimed_T")
    if t != supplied_t:
        raise CertificateError("claimed compressed map mismatch")
    defect = matsub(eye(len(t)), matmul(transpose(t), t))
    ok, pivots = ldl_psd(defect)
    if not ok:
        raise CertificateError("compressed map is not a contraction")
    raw_pivots = green.get("claimed_defect_pivots")
    if not isinstance(raw_pivots, list):
        raise CertificateError("claimed_defect_pivots must be a list")
    claimed_pivots = [frac(x, f"green pivot[{i}]") for i, x in enumerate(raw_pivots)]
    if claimed_pivots != pivots:
        raise CertificateError("claimed defect pivots mismatch")

    jc = data.get("jordan_control")
    if not isinstance(jc, dict):
        raise CertificateError("jordan_control must be an object")
    n = integer(jc.get("n"), "jordan.n")
    exponent = integer(jc.get("exponent"), "jordan.exponent")
    raw_divisors = jc.get("divisors")
    raw_values = jc.get("values")
    raw_j = jc.get("claimed_jordan")
    if not all(isinstance(x, list) for x in (raw_divisors, raw_values, raw_j)):
        raise CertificateError("Jordan arrays must be lists")
    divisors = [integer(x, f"jordan.divisors[{i}]") for i, x in enumerate(raw_divisors)]
    if divisors != sorted(set(divisors)) or any(n % d for d in divisors):
        raise CertificateError("invalid divisor ledger")
    actual_divisors = [d for d in range(1, n + 1) if n % d == 0]
    if divisors != actual_divisors:
        raise CertificateError("incomplete divisor ledger")
    jvals = [jordan(d, exponent) for d in divisors]
    claimed_j = [integer(x, f"jordan.claimed_jordan[{i}]") for i, x in enumerate(raw_j)]
    if claimed_j != jvals:
        raise CertificateError("Jordan values mismatch")
    if sum(jvals) != n**exponent:
        raise CertificateError("Jordan normalization failed")
    values = [frac(x, f"jordan.values[{i}]") for i, x in enumerate(raw_values)]
    if len(values) != len(divisors):
        raise CertificateError("Jordan values length mismatch")
    probabilities = [Fraction(v, n**exponent) for v in jvals]
    mean = sum((p * x for p, x in zip(probabilities, values)), Fraction(0))
    second = sum((p * x * x for p, x in zip(probabilities, values)), Fraction(0))
    variance = second - mean * mean
    pair_energy = Fraction(1, 2) * sum(
        probabilities[i] * probabilities[j] * (values[i] - values[j]) ** 2
        for i in range(len(values))
        for j in range(len(values))
    )
    if variance != pair_energy or variance < 0:
        raise CertificateError("Jordan carre-du-champ identity failed")
    if frac(jc.get("claimed_mean"), "jordan claimed mean") != mean:
        raise CertificateError("Jordan mean mismatch")
    if frac(jc.get("claimed_variance"), "jordan claimed variance") != variance:
        raise CertificateError("Jordan variance mismatch")

    return {
        "schema": SCHEMA,
        "status": "EXACT_CUMULATIVE_WEYL_GREEN_JORDAN_ALGEBRA",
        "flow": {
            "derivative_weight": fj(derivative_weight),
            "weyl_weight": fj(weyl_weight),
            "factor": "4",
        },
        "endpoint_cumulative_energy": fj(cumulative),
        "green": {
            "compressed_map": [[fj(x) for x in row] for row in t],
            "defect_pivots": [fj(x) for x in pivots],
        },
        "jordan": {
            "probabilities": [fj(x) for x in probabilities],
            "mean": fj(mean),
            "variance": fj(variance),
            "pair_energy": fj(pair_energy),
        },
        "proof_boundary": (
            "exact finite rational algebra only; no original Riemann Weyl "
            "quotient-to-physical isometry or RH conclusion"
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
