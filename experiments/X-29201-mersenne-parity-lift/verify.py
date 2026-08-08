from __future__ import annotations

from fractions import Fraction


def carry(parent: int, child: int, q: int) -> int:
    return (
        parent // q
        - child // q
        - (parent - child) // q
    )


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    mu[1] = 1
    primes: list[int] = []
    composite = [False] * (limit + 1)
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if n * p > limit:
                break
            composite[n * p] = True
            if n % p == 0:
                mu[n * p] = 0
                break
            mu[n * p] = -mu[n]
    return mu


def is_mersenne(n: int) -> bool:
    return n >= 3 and ((n + 1) & n) == 0


def mcf_allowed(parent: int, child: int) -> bool:
    child = min(child, parent - child)
    if is_mersenne(parent):
        return child == 1
    scale = 1 << (parent.bit_length() - 1)
    return parent - scale < child < scale


def verify_sibling_identities(limit: int = 96) -> int:
    checks = 0
    for n in range(2, limit + 1):
        for j in range(1, n):
            k = n - j
            for q in range(2, 2 * n + 2):
                base = carry(2 * n, 2 * j, q)
                first = carry(2 * n + 1, 2 * j, q)
                second = carry(2 * n + 1, 2 * j + 1, q)

                expected_first = int((2 * n + 1) % q == 0) - int(
                    (2 * k + 1) % q == 0
                )
                expected_second = int((2 * n + 1) % q == 0) - int(
                    (2 * j + 1) % q == 0
                )
                assert first - base == expected_first
                assert second - base == expected_second
                checks += 2

            for q in range(1, n + 1):
                lower = carry(n, j, q)
                assert carry(2 * n, 2 * j, 2 * q) == lower
                assert carry(2 * n + 1, 2 * j, 2 * q) == lower
                assert carry(2 * n + 1, 2 * j + 1, 2 * q) == lower
                checks += 3
    return checks


def verify_support_preservation(limit: int = 256) -> int:
    checks = 0
    for n in range(2, limit + 1):
        if is_mersenne(n):
            continue
        for j in range(1, n):
            if not mcf_allowed(n, j):
                continue
            candidates = (
                (2 * n, 2 * j),
                (2 * n + 1, 2 * j),
                (2 * n + 1, 2 * j + 1),
            )
            for parent, child in candidates:
                assert mcf_allowed(parent, child)
                checks += 1
    return checks


def verify_odd_mobius_inversion(limit: int = 127) -> int:
    mu = mobius_sieve(limit)
    # A deterministic rational synthetic odd-column residual.
    h = [Fraction(0) for _ in range(limit + 1)]
    for q in range(3, limit + 1, 2):
        h[q] = Fraction((q * q + 3 * q + 1) % 17 - 8, q + 5)

    z = [Fraction(0) for _ in range(limit + 1)]
    for m in range(1, limit + 1, 2):
        for a in range(1, limit // m + 1, 2):
            z[m] += mu[a] * h[a * m]

    checks = 0
    for q in range(3, limit + 1, 2):
        recovered = sum(z[m] for m in range(q, limit + 1, q) if m % 2 == 1)
        assert recovered == h[q]
        checks += 1
    return checks


def verify_diagonal_parent_column(limit: int = 512) -> int:
    checks = 0
    for n in range(2, limit + 1):
        for j in range(1, n):
            assert carry(n, j, n) == 1
            checks += 1
    return checks


def main() -> None:
    sibling_checks = verify_sibling_identities()
    support_checks = verify_support_preservation()
    inversion_checks = verify_odd_mobius_inversion()
    diagonal_checks = verify_diagonal_parent_column()

    print("PASS_EXACT_MERSENNE_COLLAR_AND_PARITY_SIBLING_ALGEBRA")
    print("sibling_checks", sibling_checks)
    print("support_checks", support_checks)
    print("odd_mobius_inversion_checks", inversion_checks)
    print("diagonal_parent_checks", diagonal_checks)
    print(
        "proof_boundary",
        "finite exact algebra only; no parity-network feasibility, MCF, or RH claim",
    )


if __name__ == "__main__":
    main()
