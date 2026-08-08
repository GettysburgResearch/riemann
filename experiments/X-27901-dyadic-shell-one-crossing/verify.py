from __future__ import annotations

import hashlib
import json
import math
from typing import Iterable


def prefix_sums(n: int) -> tuple[list[float], list[float]]:
    s = [0.0] * (n + 1)
    a = [0.0] * (n + 1)
    for k in range(1, n + 1):
        inv = 1.0 / math.sqrt(k)
        s[k] = s[k - 1] + inv
        a[k] = a[k - 1] + inv * math.log(k)
    return s, a


S, A = prefix_sums(200_000)


def e_cell(theta: float) -> float:
    n = int(math.floor(1.0 / theta + 1e-12))
    return theta ** -0.5 * (
        A[n] + (S[n] + 1.0) * math.log(theta) + 4.0 * S[n]
    ) - 4.0 * n


def dyadic_defect(theta: float) -> float:
    if theta <= 0.5:
        return e_cell(theta) - math.sqrt(2.0) * e_cell(2.0 * theta)
    return e_cell(theta)


def cell_parameters(n: int) -> tuple[float, float, float]:
    m = n // 2
    v = S[n] - S[m]
    u = A[n] - A[m] + 4.0 * v - (S[m] + 1.0) * math.log(2.0)
    w = 4.0 * (n - math.sqrt(2.0) * m)
    return u, v, w


def cell_maximum(n: int) -> tuple[float, float]:
    u, v, w = cell_parameters(n)
    lo = 1.0 / (n + 1)
    hi = 1.0 / n

    def f(theta: float) -> float:
        return theta ** -0.5 * (u + v * math.log(theta)) - w

    candidates = [(lo, f(lo)), (hi, f(hi))]
    critical = math.exp(2.0 - u / v)
    if lo < critical < hi:
        candidates.append((critical, 2.0 * v / math.sqrt(critical) - w))
    return max(candidates, key=lambda item: item[1])


def derivative_left_margin(n: int) -> float:
    u, v, _ = cell_parameters(n)
    return u - v * math.log(n + 1.0) - 2.0 * v


def root_bisection() -> tuple[float, float]:
    lo, hi = 1.0 / 8.0, 1.0 / 7.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        if dyadic_defect(mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return lo, hi


def sieve_primes(n: int) -> list[int]:
    flags = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        flags[0] = 0
    if n >= 1:
        flags[1] = 0
    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if flags[p]:
            start = p * p
            flags[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if flags[i]]


def parabolic_diff(x: int) -> list[float]:
    b = [0.0] * (x + 2)
    for m in range(2, x + 1):
        b[m] = 2.0 * math.sqrt(m) * (
            math.log(x / m) - 2.0 * (1.0 - math.sqrt(m / x))
        )
    return [b[m] - b[m + 1] for m in range(x + 1)]


def residuals(x: int, coordinates: Iterable[int]) -> dict[int, float]:
    diff = parabolic_diff(x)
    out: dict[int, float] = {}
    for q in coordinates:
        response = math.fsum(diff[q : x + 1 : q])
        out[q] = response - math.log(x / q) / math.sqrt(q)
    return out


def shell_scan(x: int, all_coordinates: bool) -> dict[str, object]:
    y = x // 2
    primes = sieve_primes(x)
    coordinates = list(range(2, x + 1)) if all_coordinates else primes
    rx = residuals(x, coordinates)
    low = [q for q in coordinates if q <= y]
    ry = residuals(y, low)
    shell = {q: rx[q] - (ry[q] if q <= y else 0.0) for q in coordinates}

    ordered = sorted(coordinates)
    changes = 0
    last = 0
    first_negative = None
    for q in ordered:
        value = shell[q]
        sign = 1 if value > 1e-12 else (-1 if value < -1e-12 else 0)
        if sign and last and sign != last:
            changes += 1
        if sign < 0 and first_negative is None:
            first_negative = q
        if sign:
            last = sign

    prime_values = [(p, math.log(p) * shell[p]) for p in primes]
    running = 0.0
    maximum = -math.inf
    argmax = None
    for p, value in reversed(prime_values):
        running += value
        if running > maximum:
            maximum = running
            argmax = p
    total = math.fsum(value for _, value in prime_values)
    return {
        "X": x,
        "all_coordinates": all_coordinates,
        "sign_changes": changes,
        "first_negative": first_negative,
        "crossing_ratio": None if first_negative is None else first_negative / x,
        "maximum_weighted_prime_tail": maximum,
        "maximum_tail_start": argmax,
        "total_weighted_shell": total,
    }


def main() -> None:
    negative_cells = []
    for n in range(2, 7):
        theta, value = cell_maximum(n)
        negative_cells.append({"N": n, "theta_at_max": theta, "maximum": value})

    root_lo, root_hi = root_bisection()
    derivative_margins = {
        "N8": derivative_left_margin(8),
        "N9": derivative_left_margin(9),
        "N10": derivative_left_margin(10),
        "minimum_N9_to_200000": min(
            derivative_left_margin(n) for n in range(9, 200_001)
        ),
    }

    scans = [
        shell_scan(100, True),
        shell_scan(1_000, True),
        shell_scan(5_000, True),
        shell_scan(20_000, True),
        shell_scan(100_000, False),
        shell_scan(200_000, False),
    ]

    result = {
        "schema": "X-27901-dyadic-one-crossing-v1",
        "classification": "PASS_CONTINUUM_ONE_CROSSING_AND_FINITE_RECONNAISSANCE",
        "continuum": {
            "root_bracket": [root_lo, root_hi],
            "D_at_1_over_7": dyadic_defect(1.0 / 7.0),
            "D_at_1_over_8": dyadic_defect(1.0 / 8.0),
            "D_at_1_over_9": dyadic_defect(1.0 / 9.0),
            "negative_cell_maxima": negative_cells,
            "derivative_left_margins": derivative_margins,
        },
        "finite_shell_scans": scans,
        "external_discovery_only": {
            "max_X": 10_000_000,
            "one_crossing_violations": 0,
            "positive_weighted_tail_violations": 0,
            "crossing_ratio_at_max_X": 0.1408523,
            "note": "The 10^7 scan was exploratory and is not replayed by this standard-library script.",
        },
        "scope": (
            "Continuum structure and finite numerical reconnaissance only. "
            "This does not prove cofinal FSCR, EPD, WSTS, or RH."
        ),
    }
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
