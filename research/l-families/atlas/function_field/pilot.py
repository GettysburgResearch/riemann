#!/usr/bin/env python3
"""Exact small-prime function-field detector pilot.

Polynomials are tuples of coefficients in ascending order.  The empty tuple is
zero.  This module intentionally uses elementary algorithms: it is a finite
audit tool for tiny prime fields, not a general computer-algebra package.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Iterator, Sequence


Poly = tuple[int, ...]
MAX_MONIC_ENUMERATION = 100_000


def _is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def check_field(q: int) -> None:
    if q == 2 or not _is_prime(q):
        raise ValueError("q must be an odd prime")


def poly(coefficients: Iterable[int], q: int) -> Poly:
    check_field(q)
    out = [coefficient % q for coefficient in coefficients]
    while out and out[-1] == 0:
        out.pop()
    return tuple(out)


def degree(f: Poly) -> int:
    return len(f) - 1


def is_monic(f: Poly) -> bool:
    return bool(f) and f[-1] == 1


def add(f: Poly, g: Poly, q: int) -> Poly:
    n = max(len(f), len(g))
    return poly(
        ((f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) for i in range(n)),
        q,
    )


def subtract(f: Poly, g: Poly, q: int) -> Poly:
    n = max(len(f), len(g))
    return poly(
        ((f[i] if i < len(f) else 0) - (g[i] if i < len(g) else 0) for i in range(n)),
        q,
    )


def multiply(f: Poly, g: Poly, q: int) -> Poly:
    if not f or not g:
        return ()
    out = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            out[i + j] = (out[i + j] + a * b) % q
    return poly(out, q)


def divmod_poly(f: Poly, g: Poly, q: int) -> tuple[Poly, Poly]:
    if not g:
        raise ZeroDivisionError("polynomial division by zero")
    remainder = list(poly(f, q))
    divisor = poly(g, q)
    quotient = [0] * max(0, len(remainder) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], -1, q)
    while remainder and len(remainder) >= len(divisor):
        shift = len(remainder) - len(divisor)
        coefficient = remainder[-1] * inverse_lead % q
        quotient[shift] = coefficient
        for j, value in enumerate(divisor):
            remainder[shift + j] = (remainder[shift + j] - coefficient * value) % q
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return poly(quotient, q), poly(remainder, q)


def monic(f: Poly, q: int) -> Poly:
    f = poly(f, q)
    if not f:
        raise ValueError("zero polynomial has no monic associate")
    inverse_lead = pow(f[-1], -1, q)
    return poly((inverse_lead * value for value in f), q)


def gcd_poly(f: Poly, g: Poly, q: int) -> Poly:
    f, g = poly(f, q), poly(g, q)
    while g:
        _, remainder = divmod_poly(f, g, q)
        f, g = g, remainder
    return monic(f, q) if f else ()


def derivative(f: Poly, q: int) -> Poly:
    return poly((i * f[i] for i in range(1, len(f))), q)


def powmod_poly(base: Poly, exponent: int, modulus: Poly, q: int) -> Poly:
    if exponent < 0:
        raise ValueError("negative polynomial exponent")
    if not modulus:
        raise ZeroDivisionError("zero polynomial modulus")
    result: Poly = (1,)
    _, base = divmod_poly(poly(base, q), modulus, q)
    while exponent:
        if exponent & 1:
            _, result = divmod_poly(multiply(result, base, q), modulus, q)
        _, base = divmod_poly(multiply(base, base, q), modulus, q)
        exponent >>= 1
    return result


def monic_polynomials(q: int, n: int) -> Iterator[Poly]:
    check_field(q)
    if n < 0:
        return
    count = q**n
    if count > MAX_MONIC_ENUMERATION:
        raise ValueError(f"refusing to enumerate {count} monic polynomials")
    for coefficients in itertools.product(range(q), repeat=n):
        yield tuple(coefficients) + (1,)


def is_irreducible(f: Poly, q: int) -> bool:
    f = poly(f, q)
    if not is_monic(f) or degree(f) < 1:
        return False
    for divisor_degree in range(1, degree(f) // 2 + 1):
        for divisor in monic_polynomials(q, divisor_degree):
            if not divmod_poly(f, divisor, q)[1]:
                return False
    return True


@lru_cache(maxsize=None)
def factor_monic(f: Poly, q: int) -> tuple[Poly, ...]:
    """Return irreducible monic factors with multiplicity."""

    f = poly(f, q)
    if not is_monic(f):
        raise ValueError("factor_monic requires a nonzero monic polynomial")
    if degree(f) == 0:
        return ()
    remaining = f
    factors: list[Poly] = []
    divisor_degree = 1
    while 2 * divisor_degree <= degree(remaining):
        for divisor in monic_polynomials(q, divisor_degree):
            if not is_irreducible(divisor, q):
                continue
            while True:
                quotient, remainder = divmod_poly(remaining, divisor, q)
                if remainder:
                    break
                factors.append(divisor)
                remaining = quotient
        divisor_degree += 1
    if degree(remaining) > 0:
        factors.append(remaining)
    return tuple(factors)


def is_squarefree(f: Poly, q: int) -> bool:
    f = poly(f, q)
    return bool(f) and gcd_poly(f, derivative(f, q), q) == (1,)


def residue_symbol(numerator: Poly, prime: Poly, q: int) -> int:
    """Quadratic residue symbol (numerator/prime) in F_q[T]."""

    prime = poly(prime, q)
    if not is_irreducible(prime, q):
        raise ValueError("denominator must be monic irreducible")
    return _residue_symbol_irreducible(poly(numerator, q), prime, q)


def _residue_symbol_irreducible(numerator: Poly, prime: Poly, q: int) -> int:
    _, remainder = divmod_poly(poly(numerator, q), prime, q)
    if not remainder:
        return 0
    power = powmod_poly(remainder, (q ** degree(prime) - 1) // 2, prime, q)
    if power == (1,):
        return 1
    if power == (q - 1,):
        return -1
    raise ArithmeticError("Euler criterion did not return a sign")


def validate_conductor(conductor: Poly, q: int) -> Poly:
    conductor = poly(conductor, q)
    if not is_monic(conductor):
        raise ValueError("conductor must be monic")
    if degree(conductor) < 1 or degree(conductor) % 2 == 0:
        raise ValueError("conductor must have positive odd degree")
    if not is_squarefree(conductor, q):
        raise ValueError("conductor must be squarefree")
    return conductor


def quadratic_character(conductor: Poly, f: Poly, q: int) -> int:
    """The geometric quadratic character chi_D(f)=(D/f), for monic f."""

    conductor = validate_conductor(conductor, q)
    f = poly(f, q)
    if not is_monic(f):
        raise ValueError("character input must be monic")
    return _quadratic_character_validated(conductor, f, q)


def _quadratic_character_validated(conductor: Poly, f: Poly, q: int) -> int:
    value = 1
    for prime in factor_monic(f, q):
        value *= _residue_symbol_irreducible(conductor, prime, q)
    return value


def moebius_polynomial(f: Poly, q: int) -> int:
    f = poly(f, q)
    if not is_monic(f):
        raise ValueError("Moebius input must be monic")
    factors = factor_monic(f, q)
    if len(set(factors)) != len(factors):
        return 0
    return -1 if len(factors) % 2 else 1


def l_coefficients(conductor: Poly, q: int) -> tuple[int, ...]:
    """Return coefficients through degree deg(D)-1 of L(u,chi_D)."""

    conductor = validate_conductor(conductor, q)
    return tuple(
        sum(_quadratic_character_validated(conductor, f, q) for f in monic_polynomials(q, n))
        for n in range(degree(conductor))
    )


def reciprocal_coefficients_direct(conductor: Poly, q: int, n_max: int) -> tuple[int, ...]:
    """Return B_n=sum_{deg f=n} mu(f)chi_D(f), 0<=n<=n_max."""

    conductor = validate_conductor(conductor, q)
    if n_max < 0:
        raise ValueError("n_max must be nonnegative")
    return tuple(
        sum(
            moebius_polynomial(f, q) * _quadratic_character_validated(conductor, f, q)
            for f in monic_polynomials(q, n)
        )
        for n in range(n_max + 1)
    )


def reciprocal_coefficients_formal(l_coeffs: Sequence[int], n_max: int) -> tuple[int, ...]:
    if not l_coeffs or l_coeffs[0] != 1:
        raise ValueError("L polynomial must have constant coefficient one")
    reciprocal = [1]
    for n in range(1, n_max + 1):
        reciprocal.append(
            -sum(l_coeffs[k] * reciprocal[n - k] for k in range(1, min(n, len(l_coeffs) - 1) + 1))
        )
    return tuple(reciprocal)


def convolution_identity(l_coeffs: Sequence[int], reciprocal: Sequence[int]) -> tuple[int, ...]:
    return tuple(
        sum(l_coeffs[k] * reciprocal[n - k] for k in range(max(0, n - len(reciprocal) + 1), min(n, len(l_coeffs) - 1) + 1))
        for n in range(len(reciprocal))
    )


@dataclass(frozen=True)
class Qsqrt:
    """An exact element a+b*sqrt(q), with a,b rational."""

    q: int
    rational: Fraction = Fraction(0)
    sqrt_coefficient: Fraction = Fraction(0)

    def __add__(self, other: "Qsqrt") -> "Qsqrt":
        if self.q != other.q:
            raise ValueError("incompatible quadratic fields")
        return Qsqrt(self.q, self.rational + other.rational, self.sqrt_coefficient + other.sqrt_coefficient)

    def __mul__(self, other: "Qsqrt") -> "Qsqrt":
        if self.q != other.q:
            raise ValueError("incompatible quadratic fields")
        return Qsqrt(
            self.q,
            self.rational * other.rational + self.q * self.sqrt_coefficient * other.sqrt_coefficient,
            self.rational * other.sqrt_coefficient + self.sqrt_coefficient * other.rational,
        )

    def as_json(self) -> dict[str, list[int]]:
        return {
            "rational": [self.rational.numerator, self.rational.denominator],
            "sqrt_q": [self.sqrt_coefficient.numerator, self.sqrt_coefficient.denominator],
        }


def normalized_reciprocal(value: int, n: int, q: int) -> Qsqrt:
    """Encode q^(-n/2)*value exactly in Q(sqrt(q))."""

    check_field(q)
    if n < 0:
        raise ValueError("degree must be nonnegative")
    if n % 2 == 0:
        return Qsqrt(q, Fraction(value, q ** (n // 2)), Fraction(0))
    return Qsqrt(q, Fraction(0), Fraction(value, q ** ((n + 1) // 2)))


def _fraction_json(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def poly_string(f: Poly, variable: str = "T") -> str:
    if not f:
        return "0"
    terms: list[str] = []
    for exponent in range(len(f) - 1, -1, -1):
        coefficient = f[exponent]
        if coefficient == 0:
            continue
        if exponent == 0:
            term = str(coefficient)
        elif exponent == 1:
            term = variable if coefficient == 1 else f"{coefficient}*{variable}"
        else:
            term = f"{variable}^{exponent}" if coefficient == 1 else f"{coefficient}*{variable}^{exponent}"
        terms.append(term)
    return " + ".join(terms)


def member_record(conductor: Poly, q: int, n_max: int) -> dict[str, object]:
    l_coeffs = l_coefficients(conductor, q)
    direct = reciprocal_coefficients_direct(conductor, q, n_max)
    formal = reciprocal_coefficients_formal(l_coeffs, n_max)
    convolution = convolution_identity(l_coeffs, direct)
    if direct != formal or convolution != (1,) + (0,) * n_max:
        raise AssertionError("Euler reciprocal identity failed")
    normalized = [normalized_reciprocal(value, n, q) for n, value in enumerate(direct)]
    cross = normalized[1] * normalized[2]
    root_certificate = None
    if len(l_coeffs) == 3:
        root_certificate = {
            "quadratic_lead_is_q": l_coeffs[2] == q,
            "discriminant_nonpositive": l_coeffs[1] ** 2 <= 4 * q,
            "discriminant": l_coeffs[1] ** 2 - 4 * q,
        }
    return {
        "conductor_coefficients_low_to_high": list(conductor),
        "conductor": poly_string(conductor),
        "L_coefficients_low_to_high": list(l_coeffs),
        "reciprocal_coefficients_B0_to_Bn": list(direct),
        "normalized_Bn_in_Q_sqrt_q": [value.as_json() for value in normalized],
        "signed_lag_one_numerator_B1_B2": direct[1] * direct[2],
        "normalized_signed_lag_one": cross.as_json(),
        "root_modulus_certificate": root_certificate,
    }


def build_fixture(q: int = 5, conductor_degree: int = 3, n_max: int = 3) -> dict[str, object]:
    check_field(q)
    if (q, conductor_degree, n_max) != (5, 3, 3):
        raise ValueError("the frozen family fixture requires exactly q=5, conductor degree 3, n_max=3")
    conductors = [f for f in monic_polynomials(q, conductor_degree) if is_squarefree(f, q)]
    records = [member_record(conductor, q, n_max) for conductor in conductors]
    signed = [int(record["signed_lag_one_numerator_B1_B2"]) for record in records]
    trace_histogram = Counter(int(record["L_coefficients_low_to_high"][1]) for record in records)
    signed_histogram = Counter(signed)
    negative = min((record for record in records if int(record["signed_lag_one_numerator_B1_B2"]) < 0), key=lambda r: str(r["conductor"]))
    positive = min((record for record in records if int(record["signed_lag_one_numerator_B1_B2"]) > 0), key=lambda r: str(r["conductor"]))
    zero = min((record for record in records if int(record["signed_lag_one_numerator_B1_B2"]) == 0), key=lambda r: str(r["conductor"]))
    mean = Fraction(sum(signed), len(signed))
    producer_text = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    payload: dict[str, object] = {
        "schema": "riemann.function_field.exact_pilot.v1",
        "raw_fixture_id": "FUNCTION_FIELD.F5.CUBIC.EXACT.V1",
        "rigor_level": "RIGOROUS_CERTIFIED",
        "scope": "exhaustive finite family of monic squarefree cubic conductors",
        "field": {"q": q, "model": f"F_{q}[T]", "quadratic_basis": f"Q(sqrt({q}))"},
        "character": "chi_D(f)=(D/f) on monic f",
        "object_metadata": {
            "family": "quadratic function-field L-functions / genus-one hyperelliptic numerators",
            "object_type": "self-dual quadratic character",
            "L_degree": 2,
            "conductor": "all monic squarefree degree-3 D in F_5[T]",
            "normalization": "L_D(u)=sum_monic chi_D(f)u^deg(f)=product_j(1-alpha_j*u)",
            "gamma_factors": "not present in the finite numerator normalization",
            "root_number": "not used by this pilot",
            "analytic_rank": "not computed or inferred",
            "zero_data_provenance": "no imported zeros; modulus certified from exact quadratic coefficients",
        },
        "detector": {
            "id": "FUNCTION_FIELD.NORMALIZED_RECIPROCAL_COEFFICIENT.TOY",
            "definition": "H_D(n)=q^(-n/2) sum_deg(f)=n mu(f)chi_D(f)",
            "cross_probe": "C_D=H_D(1)H_D(2), a toy lag-one probe only",
            "invariance": "critical Frobenius scaling; native coordinate is polynomial degree",
            "failure_mode": "family cancellation and root purity do not imply a memberwise sign",
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/pilot.py",
            "source_sha256_lf_normalized": hashlib.sha256(producer_text.encode("utf-8")).hexdigest(),
            "runtime_contract": "Python 3.11+ standard library; exact integer/rational arithmetic",
            "input_provenance": "complete deterministic generation, no external data",
        },
        "family": {
            "conductor_degree": conductor_degree,
            "member_count": len(records),
            "reciprocal_degree_checked_through": n_max,
        },
        "exact_checks": {
            "direct_Moebius_coefficients_equal_formal_inverse_for_every_member": True,
            "L_times_reciprocal_is_one_through_checked_degree_for_every_member": True,
            "genus_one_root_modulus_certificates_for_every_member": all(
                record["root_modulus_certificate"]["quadratic_lead_is_q"]
                and record["root_modulus_certificate"]["discriminant_nonpositive"]
                for record in records
            ),
        },
        "family_statistics": {
            "L_linear_coefficient_histogram": {str(key): trace_histogram[key] for key in sorted(trace_histogram)},
            "B1_times_B2_histogram": {str(key): signed_histogram[key] for key in sorted(signed_histogram)},
            "mean_B1_times_B2": _fraction_json(mean),
            "negative_member_count": sum(value < 0 for value in signed),
            "zero_member_count": sum(value == 0 for value in signed),
            "positive_member_count": sum(value > 0 for value in signed),
        },
        "witnesses": {"negative": negative, "zero": zero, "positive": positive},
        "firewall": (
            "B1*B2 is an explicitly declared toy cross-degree statistic, not canonical XD or HCNC; "
            "its mixed memberwise signs show only that purity/root modulus does not determine this sign."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare the generated fixture with this JSON file")
    parser.add_argument("--write", type=Path, help="write the generated compact fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"fixture mismatch: {args.check}")
        print(f"OK: exact fixture matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
