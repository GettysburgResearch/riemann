#!/usr/bin/env python3
"""Enclose the full squared error of the anchored k=2 prime array at finite cutoffs."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import isqrt
from pathlib import Path
import sys

import flint
from flint import arb, ctx


CERTIFICATE_VERSION = 2


def prime_power_bases(limit: int) -> list[int]:
    """Return p at prime powers p^j and zero elsewhere."""
    prime_flags = bytearray(b"\x01") * (limit + 1)
    prime_flags[:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if prime_flags[candidate]:
            first = candidate * candidate
            prime_flags[first::candidate] = bytes((limit - first) // candidate + 1)

    bases = [0] * (limit + 1)
    for prime in range(2, limit + 1):
        if prime_flags[prime]:
            power = prime
            while power <= limit:
                bases[power] = prime
                power *= prime
    return bases


def tapered_coefficients(length: int) -> tuple[arb, list[tuple[int, arb]]]:
    log_length = arb(length).log()
    bases = prime_power_bases(length)
    prime_logs = {0: arb(0)}
    for index in range(2, length + 1):
        if bases[index] == index:
            prime_logs[index] = arb(index).log()

    coefficients = []
    # At d=N the taper is exactly zero. There is also no term at d=1.
    for index in range(2, length):
        base = bases[index]
        half_base = bases[index // 2] if index % 2 == 0 else 0
        if not (base or half_base):
            continue
        weight = 2 * prime_logs[half_base] - prime_logs[base]
        if index == 2:
            weight += 2 * prime_logs[2]
        taper = (log_length - arb(index).log()) / log_length
        coefficients.append((index, weight * taper))
    return log_length, coefficients


def jump_block(start: int, stop: int, coefficients: list[tuple[int, arb]]) -> list[arb | None]:
    """Sieve sum_{d|n} a_d on start <= n < stop."""
    jumps: list[arb | None] = [None] * (stop - start)
    for divisor, coefficient in coefficients:
        first_offset = (-start) % divisor
        for offset in range(first_offset, stop - start, divisor):
            previous = jumps[offset]
            jumps[offset] = coefficient if previous is None else previous + coefficient
    return jumps


def direct_floor(n: int, coefficients: list[tuple[int, arb]]) -> arb:
    """Evaluate the defining sum, using an exact numerator for each floor difference."""
    return sum(
        (coefficient * ((n // d) * d - n) / d for d, coefficient in coefficients),
        arb(0),
    )


def direct_factorial(n: int) -> arb:
    q = n // 2
    return q * arb(4).log() + 2 * arb(q + 1).lgamma() - arb(n + 1).lgamma()


def dyadic(value: arb) -> dict[str, str | int]:
    if not value.is_exact() or not value.is_finite():
        raise ArithmeticError("Expected a finite exact dyadic endpoint.")
    mantissa, exponent = value.man_exp()
    return {"mantissa": str(mantissa), "exponent": int(exponent)}


def outward_decimal(value: arb, *, upward: bool, places: int = 18) -> str:
    mantissa, exponent = value.man_exp()
    numerator = int(mantissa) * 10**places
    denominator = 1
    if exponent >= 0:
        numerator <<= int(exponent)
    else:
        denominator <<= -int(exponent)
    units = -((-numerator) // denominator) if upward else numerator // denominator
    quotient, remainder = divmod(abs(units), 10**places)
    sign = "-" if units < 0 else ""
    return f"{sign}{quotient}.{remainder:0{places}d}"


def endpoints(lower: arb, upper: arb) -> dict[str, object]:
    return {
        "lower_dyadic": dyadic(lower),
        "upper_dyadic": dyadic(upper),
        "lower_decimal_outward": outward_decimal(lower, upward=False),
        "upper_decimal_outward": outward_decimal(upper, upward=True),
    }


def ball_bounds(value: arb) -> dict[str, object]:
    return endpoints(value.lower(), value.upper())


def certify(length: int, cutoff: int, block_cells: int) -> dict[str, object]:
    log_length, coefficients = tapered_coefficients(length)
    anchor = sum((coefficient / d for d, coefficient in coefficients), arb(0))
    coefficient_l1 = sum((abs(coefficient) for _, coefficient in coefficients), arb(0))
    checkpoints = {
        n
        for n in (
            1, 2, 3, 4, 5, 6, length - 1, length, length + 1,
            2 * length, block_cells - 1, block_cells, block_cells + 1,
            cutoff // 2, cutoff - 1, cutoff,
        )
        if 1 <= n <= cutoff
    }

    target = arb(0)
    approximation = arb(0)
    finite_sum = arb(0)
    checks = []
    for start in range(1, cutoff + 1, block_cells):
        stop = min(start + block_cells, cutoff + 1)
        for n, jump in enumerate(jump_block(start, stop, coefficients), start):
            log_n = arb(n).log()
            if n % 2 == 0:
                target += log_n
            else:
                target -= log_n
            approximation -= anchor
            if jump is not None:
                approximation += jump
            residual = target - approximation
            # General ball exponentiation can be indeterminate for an inexact ball centered at zero.
            finite_sum += (residual * residual) / (n * (n + 1))

            if n in checkpoints:
                floor_value = direct_floor(n, coefficients)
                factorial_value = direct_factorial(n)
                if not approximation.overlaps(floor_value):
                    raise ArithmeticError(f"Jump sieve and floor sum disagree at N={length}, n={n}.")
                if not target.overlaps(factorial_value):
                    raise ArithmeticError(f"Log recurrence and factorial formula disagree at n={n}.")
                checks.append({
                    "n": n,
                    "jump_approximation_minus_direct_floor": ball_bounds(approximation - floor_value),
                    "log_recurrence_minus_direct_factorial": ball_bounds(target - factorial_value),
                })

    first_tail_cell = cutoff + 1
    u = 2 * arb(first_tail_cell).log() + coefficient_l1
    tail_majorant = (u * u + 4 * u + 8) / first_tail_cell
    sum_with_tail_majorant = finite_sum + tail_majorant
    return {
        "N": length,
        "X": cutoff,
        "first_tail_cell": first_tail_cell,
        "nonzero_coefficient_indices": [index for index, _ in coefficients],
        "anchor_A_at_1": ball_bounds(anchor),
        "coefficient_l1": ball_bounds(coefficient_l1),
        "finite_squared_error": ball_bounds(finite_sum),
        "tail_majorant_enclosure": ball_bounds(tail_majorant),
        "full_squared_error": endpoints(finite_sum.lower(), sum_with_tail_majorant.upper()),
        "log_N_times_full_squared_error": endpoints(
            (finite_sum * log_length).lower(),
            (sum_with_tail_majorant * log_length).upper(),
        ),
        "independent_direct_cell_checks": checks,
    }


def case_argument(value: str) -> tuple[int, int]:
    try:
        length, cutoff = map(int, value.split(":"))
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Use N:X for each case.") from exc
    if length < 2 or cutoff < 1:
        raise argparse.ArgumentTypeError("Require N >= 2 and X >= 1.")
    return length, cutoff


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", type=case_argument, required=True)
    parser.add_argument("--precision", type=int, default=160)
    parser.add_argument("--block-cells", type=int, default=32768)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.precision < 2 or args.block_cells < 1:
        parser.error("Require precision >= 2 and positive block-cells.")

    ctx.prec = args.precision
    ctx.threads = 1
    cases = []
    for length, cutoff in args.case:
        try:
            case = certify(length, cutoff, args.block_cells)
        except ArithmeticError as exc:
            parser.exit(1, f"Certificate failed for N={length}, X={cutoff}: {exc}\n")
        cases.append(case)
        bounds = case["full_squared_error"]
        print(
            f"N={length}, X={cutoff}: "
            f"[{bounds['lower_decimal_outward']}, {bounds['upper_decimal_outward']}]",
            file=sys.stderr,
            flush=True,
        )
    payload = {
        "description": "Unconditional finite-N enclosure of the full squared error for k=2",
        "certificate_version": CERTIFICATE_VERSION,
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python_version": sys.version.split()[0],
        "python_flint_version": flint.__version__,
        "flint_version": flint.__FLINT_VERSION__,
        "precision_bits": args.precision,
        "arb_threads": ctx.threads,
        "block_cells": args.block_cells,
        "dyadic_convention": "mantissa * 2**exponent; mantissa is an exact decimal integer string",
        "tail_majorant": "((2*log(X+1)+S_N)^2+4*(2*log(X+1)+S_N)+8)/(X+1)",
        "cases": cases,
    }
    pending = args.out.with_name(args.out.name + ".pending")
    pending.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    pending.replace(args.out)


if __name__ == "__main__":
    main()
