#!/usr/bin/env python3
"""Directed-decimal verifier for one finite Robin-inequality witness.

Input is an exact prime factorization. Basic arithmetic uses directed rounding.
CPython's documented correctly-rounded Decimal ln/exp operations are expanded
by one adjacent representable value at each endpoint. Euler's constant is
bounded by

  H_m - log(m) - 1/(2m) < gamma < H_m - log(m).

This certifies a comparison for one integer; it does not certify an exploratory
search's enumeration or binary64 transition ordering.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from decimal import (
    Context,
    Decimal,
    InvalidOperation,
    ROUND_CEILING,
    ROUND_FLOOR,
    ROUND_HALF_EVEN,
)
import json
import sys
from typing import Any, Iterable, Sequence

ROBIN_EXCEPTION = 5040
SCHEMA = "riemann.robin.factorization.v1"
MAX_DETERMINISTIC_PRIME = 1 << 64


@dataclass(frozen=True)
class Interval:
    lower: Decimal
    upper: Decimal

    def __post_init__(self) -> None:
        if self.lower > self.upper:
            raise ValueError("invalid interval")

    def to_json(self) -> dict[str, str]:
        return {
            "lower": format(self.lower, "E"),
            "upper": format(self.upper, "E"),
            "width": format(self.upper - self.lower, "E"),
        }


class DecimalIntervals:
    def __init__(self, precision: int) -> None:
        if precision < 20:
            raise ValueError("precision must be at least 20 decimal digits")
        common = dict(
            prec=precision,
            Emin=-999_999_999,
            Emax=999_999_999,
            capitals=1,
            clamp=0,
        )
        self.precision = precision
        self.down = Context(rounding=ROUND_FLOOR, **common)
        self.up = Context(rounding=ROUND_CEILING, **common)
        self.nearest = Context(rounding=ROUND_HALF_EVEN, **common)

    @staticmethod
    def exact(value: int | str | Decimal) -> Interval:
        d = value if isinstance(value, Decimal) else Decimal(value)
        return Interval(d, d)

    def add(self, x: Interval, y: Interval) -> Interval:
        return Interval(self.down.add(x.lower, y.lower), self.up.add(x.upper, y.upper))

    def subtract(self, x: Interval, y: Interval) -> Interval:
        return Interval(
            self.down.subtract(x.lower, y.upper),
            self.up.subtract(x.upper, y.lower),
        )

    def multiply_nonnegative(self, x: Interval, y: Interval) -> Interval:
        if x.lower < 0 or y.lower < 0:
            raise ValueError("multiply_nonnegative received a negative interval")
        return Interval(
            self.down.multiply(x.lower, y.lower),
            self.up.multiply(x.upper, y.upper),
        )

    def divide_positive(self, x: Interval, y: Interval) -> Interval:
        if x.lower < 0 or y.lower <= 0:
            raise ValueError("divide_positive requires x >= 0 and y > 0")
        return Interval(
            self.down.divide(x.lower, y.upper),
            self.up.divide(x.upper, y.lower),
        )

    def logarithm(self, x: Interval) -> Interval:
        if x.lower <= 0:
            raise ValueError("logarithm requires a positive interval")
        if x.lower == x.upper == 1:
            return self.exact(0)
        lo = x.lower.ln(context=self.nearest)
        hi = x.upper.ln(context=self.nearest)
        return Interval(lo.next_minus(self.nearest), hi.next_plus(self.nearest))

    def exponential(self, x: Interval) -> Interval:
        lo = x.lower.exp(context=self.nearest)
        hi = x.upper.exp(context=self.nearest)
        return Interval(lo.next_minus(self.nearest), hi.next_plus(self.nearest))


def is_prime_u64(n: int) -> bool:
    """Deterministic Miller-Rabin for 0 <= n < 2**64."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        a = base % n
        if a == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True


def validate_factorization(raw: Any) -> list[tuple[int, int]]:
    if not isinstance(raw, list) or not raw:
        raise ValueError("factorization must be a nonempty list")
    factors: list[tuple[int, int]] = []
    for index, item in enumerate(raw):
        if isinstance(item, dict):
            p, a = item.get("p"), item.get("a")
        elif isinstance(item, (list, tuple)) and len(item) == 2:
            p, a = item
        else:
            raise ValueError(f"factor {index} must be an object or [p,a]")
        if isinstance(p, bool) or not isinstance(p, int):
            raise ValueError(f"factor {index} prime must be an integer")
        if isinstance(a, bool) or not isinstance(a, int) or a < 1:
            raise ValueError(f"factor {index} exponent must be positive")
        if p >= MAX_DETERMINISTIC_PRIME:
            raise ValueError(f"factor {index} prime >= 2**64 needs a primality proof")
        if not is_prime_u64(p):
            raise ValueError(f"factor {index} base {p} is not prime")
        factors.append((p, a))
    if factors != sorted(factors):
        raise ValueError("factors must be sorted by increasing prime")
    if len({p for p, _ in factors}) != len(factors):
        raise ValueError("duplicate prime factors are not allowed")
    return factors


def product_exceeds_5040(factors: Iterable[tuple[int, int]]) -> bool:
    value = 1
    for p, a in factors:
        for _ in range(min(a, 13)):
            if value > ROBIN_EXCEPTION // p:
                return True
            value *= p
        if a > 13:
            return True
    return value > ROBIN_EXCEPTION


def gamma_interval(engine: DecimalIntervals, terms: int) -> Interval:
    """Use H_m-log(m)-1/(2m) < gamma < H_m-log(m)."""
    if terms < 1:
        raise ValueError("gamma_terms must be positive")
    h_lo = Decimal(0)
    h_hi = Decimal(0)
    one = Decimal(1)
    for k in range(1, terms + 1):
        d = Decimal(k)
        h_lo = engine.down.add(h_lo, engine.down.divide(one, d))
        h_hi = engine.up.add(h_hi, engine.up.divide(one, d))
    h = Interval(h_lo, h_hi)
    a_m = engine.subtract(h, engine.logarithm(engine.exact(terms)))
    remainder = engine.divide_positive(engine.exact(1), engine.exact(2 * terms))
    return Interval(engine.subtract(a_m, remainder).lower, a_m.upper)


def certify_factorization(
    factors: list[tuple[int, int]],
    *,
    precision: int = 60,
    gamma_terms: int = 100_000,
) -> dict[str, Any]:
    engine = DecimalIntervals(precision)
    log_n = engine.exact(0)
    abundancy = engine.exact(1)
    for p, a in factors:
        log_n = engine.add(
            log_n,
            engine.multiply_nonnegative(engine.logarithm(engine.exact(p)), engine.exact(a)),
        )
        numerator = p ** (a + 1) - 1
        denominator = p**a * (p - 1)
        local = engine.divide_positive(engine.exact(numerator), engine.exact(denominator))
        abundancy = engine.multiply_nonnegative(abundancy, local)

    log_log_n = engine.logarithm(log_n)
    gamma = gamma_interval(engine, gamma_terms)
    exp_gamma = engine.exponential(gamma)
    rhs = engine.multiply_nonnegative(exp_gamma, log_log_n)
    difference = engine.subtract(abundancy, rhs)
    in_domain = product_exceeds_5040(factors)
    if not in_domain:
        verdict = "OUT_OF_DOMAIN"
    elif difference.lower >= 0:
        verdict = "CERTIFIED_VIOLATION"  # equality also violates the strict inequality
    elif difference.upper < 0:
        verdict = "CERTIFIED_SATISFACTION"
    else:
        verdict = "UNRESOLVED"

    return {
        "schema": SCHEMA,
        "criterion": "sigma(n)/n < exp(gamma) * log(log(n)) for every n > 5040",
        "verdict": verdict,
        "factorization": [{"p": p, "a": a} for p, a in factors],
        "n_gt_5040": in_domain,
        "precision_decimal_digits": precision,
        "gamma_terms": gamma_terms,
        "intervals": {
            "log_n": log_n.to_json(),
            "log_log_n": log_log_n.to_json(),
            "gamma": gamma.to_json(),
            "exp_gamma": exp_gamma.to_json(),
            "sigma_over_n": abundancy.to_json(),
            "robin_rhs": rhs.to_json(),
            "difference_sigma_over_n_minus_rhs": difference.to_json(),
        },
        "certification_basis": [
            "Exact integer prime powers and exact Decimal construction",
            "Directed ROUND_FLOOR/ROUND_CEILING for basic arithmetic",
            "Documented correctly-rounded Decimal ln/exp, expanded by one adjacent value",
            "Elementary gamma enclosure H_m-log(m)-1/(2m) < gamma < H_m-log(m)",
            "Deterministic Miller-Rabin primality checking for every p < 2**64",
        ],
        "remaining_verification": (
            "Independently reproduce any CERTIFIED_VIOLATION with another "
            "interval/ball library before accepting an RH counterexample."
        ),
    }


def factor_small_integer(n: int) -> list[tuple[int, int]]:
    if n < 2:
        raise ValueError("integer must be at least 2")
    remaining = n
    factors: list[tuple[int, int]] = []
    p = 2
    while p * p <= remaining:
        if remaining % p == 0:
            a = 0
            while remaining % p == 0:
                remaining //= p
                a += 1
            factors.append((p, a))
        p = 3 if p == 2 else p + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def load_request(path: str | None) -> dict[str, Any]:
    try:
        if path is None or path == "-":
            return json.load(sys.stdin)
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"could not read certificate request: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--request")
    source.add_argument("--integer", type=int)
    parser.add_argument("--precision", type=int, default=60)
    parser.add_argument("--gamma-terms", type=int, default=100_000)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.integer is not None:
            factors = factor_small_integer(args.integer)
            precision = args.precision
            gamma_terms = args.gamma_terms
        else:
            request = load_request(args.request)
            if request.get("schema", SCHEMA) != SCHEMA:
                raise ValueError(f"unsupported schema: {request.get('schema')!r}")
            factors = validate_factorization(request.get("factorization"))
            precision = int(request.get("precision", args.precision))
            gamma_terms = int(request.get("gamma_terms", args.gamma_terms))
        result = certify_factorization(
            factors, precision=precision, gamma_terms=gamma_terms
        )
    except (ValueError, InvalidOperation, OverflowError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
