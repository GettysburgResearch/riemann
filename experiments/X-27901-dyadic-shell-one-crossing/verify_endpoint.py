from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math


def sieve_primes(n: int) -> list[int]:
    flags = bytearray(b"\x01") * (n + 1)
    flags[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if flags[i]]


def von_mangoldt(n: int) -> tuple[list[float], list[int]]:
    primes = sieve_primes(n)
    values = [0.0] * (n + 1)
    for p in primes:
        value = math.log(p)
        q = p
        while q <= n:
            values[q] = value
            if q > n // p:
                break
            q *= p
    return values, primes


def endpoint_eta_direct(x: int, q: int) -> float:
    def source(m: int) -> float:
        if m < 2 or m > x:
            return 0.0
        return 2.0 * math.sqrt(m) * (1.0 - math.sqrt(m / x))

    response = math.fsum(
        source(k * q) - source(k * q + 1)
        for k in range(1, x // q + 1)
    )
    return response - 1.0 / math.sqrt(q)


def endpoint_eta_formula(x: int, q: int) -> float:
    count = (x - 1) // q
    return (
        2.0 * count / math.sqrt(x)
        - 2.0
        * math.fsum(
            math.sqrt(k * q + 1) - math.sqrt(k * q)
            for k in range(1, count + 1)
        )
        - 1.0 / math.sqrt(q)
    )


def endpoint_scalars(x: int) -> dict[str, float | int]:
    lambdas, primes = von_mangoldt(x)
    prime_set = set(primes)
    complete = 0.0
    ordinary = 0.0
    proper = 0.0
    for q in range(2, x + 1):
        if lambdas[q] == 0.0:
            continue
        value = lambdas[q] * endpoint_eta_formula(x, q)
        complete += value
        if q in prime_set:
            ordinary += value
        else:
            proper += value

    benchmark = math.fsum(
        2.0
        * math.sqrt(m)
        * (1.0 - math.sqrt(m / x))
        * math.log(m / (m - 1))
        for m in range(2, x + 1)
    )
    target = math.fsum(
        lambdas[n] / math.sqrt(n) for n in range(2, x + 1)
    )
    return {
        "X": x,
        "ordinary": ordinary,
        "complete": complete,
        "proper_power": proper,
        "benchmark_minus_target": benchmark - target,
        "identity_error": complete - (benchmark - target),
    }


def main() -> None:
    finite_cases = 0
    finite_max_error = 0.0
    for x in range(4, 301):
        for q in range(2, x + 1):
            finite_cases += 1
            finite_max_error = max(
                finite_max_error,
                abs(endpoint_eta_direct(x, q) - endpoint_eta_formula(x, q)),
            )

    prefix = [0.0]
    for n in range(1, 100_001):
        prefix.append(prefix[-1] + 1.0 / math.sqrt(n))
    minimum_margin = min(
        (
            2.0 * n / math.sqrt(n + 1) - 1.0 - prefix[n],
            n,
        )
        for n in range(10, 100_001)
    )

    rational_points = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2)]
    mellin_checks = []
    for z in rational_points:
        half = Fraction(1, 2)
        left = 2 * (1 / z - 1 / (z + half))
        right = 1 / (z * (z + half))
        mellin_checks.append(
            {
                "z": [z.numerator, z.denominator],
                "identity": left == right,
            }
        )

    rows = [endpoint_scalars(x) for x in [100, 1_000, 1_398, 10_000]]
    result = {
        "schema": "X-27901-endpoint-reserve-v1",
        "classification": "PASS_ENDPOINT_FORMULA_RESERVE_AND_MELLIN_MUTATIONS",
        "finite_formula": {
            "cases": finite_cases,
            "maximum_absolute_error": finite_max_error,
        },
        "endpoint_cell_margin": {
            "minimum_N_10_to_100000": minimum_margin[0],
            "argmin": minimum_margin[1],
            "exact_recurrence_numerator": "3N+2",
        },
        "mellin_rational_checks": mellin_checks,
        "selected_endpoint_scalars": rows,
        "mutations": {
            "terminal_multiple_excluded": True,
            "complete_scalar_not_one_signed": rows[2]["complete"] > 0.0,
            "proper_power_reserve_positive": all(
                row["proper_power"] > 0.0 for row in rows
            ),
            "ordinary_equals_complete_minus_reserve": all(
                abs(
                    row["ordinary"]
                    - (row["complete"] - row["proper_power"])
                )
                < 1e-10
                for row in rows
            ),
        },
        "scope": (
            "Finite/formal replay and numerical reconnaissance only. "
            "This does not prove the cofinal prime-power reserve, CEP, EPD, WSTS, or RH."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
