from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from math import isqrt


def mobius(n: int) -> int:
    if n == 1:
        return 1
    value = n
    primes = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            primes += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def lam(n: int) -> int:
    return -1 if n % 2 else 1  # (-1)^n


def convolution_mu_lam(n: int) -> int:
    total = 0
    for d in range(1, n + 1):
        if n % d == 0:
            total += mobius(d) * lam(n // d)
    return total


def inv_square(n: int) -> Fraction:
    return Fraction(1, n * n)


def check_truncated_decomposition(endpoint: int, q: int, r_max: int) -> None:
    """Check H=P+E+C termwise at exponent s=2 through multiplier r_max."""
    original = Fraction(0)
    parity = Fraction(0)
    shift = Fraction(0)

    for r in range(1, r_max + 1):
        product = r * q
        if r % 2 == 0:
            k = r // 2
            if 2 * k * q - 1 > endpoint:
                original += inv_square(2 * k * q - 1)
                shift += inv_square(2 * k * q - 1) - inv_square(2 * k * q)
            if product > endpoint:
                parity += inv_square(product)
        else:
            if r >= 3 and product > endpoint:
                original -= inv_square(product)
            if product > endpoint:
                parity -= inv_square(product)

    collar = Fraction(0)
    if (endpoint + 1) % (2 * q) == 0:
        collar = -inv_square(endpoint + 1)

    assert original == parity + shift + collar


def check_shift_bound(endpoint: int) -> None:
    q_max = (endpoint + 1) // 2
    for q in range(2, q_max + 1):
        start = (endpoint + 1) // (2 * q) + 1
        assert start >= 2
        # The symbolic proof uses floor(x)>=x/2 and the integral tail bound.
        assert start - 1 >= Fraction(endpoint + 1, 4 * q)


def check_regularized_source(endpoint: int, m: int) -> None:
    """At s=2, the transformed source uses only -delta_1+2delta_2."""
    threshold = Fraction(endpoint, m)
    total = Fraction(0)
    if Fraction(1) > threshold:
        total -= 1
    if Fraction(2) > threshold:
        total += Fraction(2, 4)  # coefficient 2 times 2^(-2)
    total *= Fraction(1, m * m)

    expected = Fraction(0)
    if 2 * m > endpoint:
        expected += Fraction(1, 2 * m * m)  # 2^(1-2)m^(-2)
    if m > endpoint:
        expected -= Fraction(1, m * m)
    assert total == expected


def main() -> None:
    convolution_rows = []
    for n in range(1, 129):
        value = convolution_mu_lam(n)
        expected = -1 if n == 1 else (2 if n == 2 else 0)
        assert value == expected
        convolution_rows.append(value)

    decomposition_cases = 0
    regularized_cases = 0
    for endpoint in range(8, 97):
        q_max = (endpoint + 1) // 2
        check_shift_bound(endpoint)
        for q in range(2, q_max + 1):
            check_truncated_decomposition(endpoint, q, 4 * endpoint + 8)
            decomposition_cases += 1
        for m in range(1, 2 * endpoint + 3):
            check_regularized_source(endpoint, m)
            regularized_cases += 1

    payload: dict[str, object] = {
        "schema": "X-30402-parity-shell-shift-collar-v1",
        "classification": "PASS_EXACT_PARITY_SHELL_SHIFT_COLLAR_DECOMPOSITION",
        "checks": {
            "mu_lambda_convolution_rows": len(convolution_rows),
            "finite_termwise_decomposition_cases": decomposition_cases,
            "regularized_source_cases_at_s_2": regularized_cases,
            "collar_source": "one atom at (N+1)/2 when N is odd",
            "shift_load_bound": "sum sqrt(q)E_N(q)<3 proved symbolically",
        },
        "scope": (
            "exact standard-library mutation replay for L-30405; the cofinal "
            "bounds and physical window theorem are written proofs; does not "
            "control the zero-order parity packet or prove RH"
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["sha256_without_digest"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
