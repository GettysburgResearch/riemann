#!/usr/bin/env python3
"""Exact regression for the dyadic parity-dipole proposal.

Standard library only. This verifies finite algebra and fail-closed mutation
controls. It does not prove the reflected dyadic Hall reserve or RH.
"""

from fractions import Fraction
import json

MAX_N = 192


def factorint(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factorint(n).items():
        ds = [d * p**j for d in ds for j in range(e + 1)]
    return sorted(ds)


def primes_upto(n: int) -> list[int]:
    out = []
    for k in range(2, n + 1):
        f = factorint(k)
        if len(f) == 1 and next(iter(f.values())) == 1:
            out.append(k)
    return out


def is_squarefree(n: int) -> bool:
    return all(e == 1 for e in factorint(n).values())


def mobius(n: int) -> int:
    f = factorint(n)
    if any(e > 1 for e in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


def v2(n: int) -> int:
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def beta(n: int, q: int) -> Fraction:
    if q > n:
        return Fraction(0)
    k, r = divmod(n, q)
    return Fraction(k * (q - 1 - r), n + 1)


def affine_mobius_row(n: int, m: int) -> Fraction:
    return sum(
        Fraction(mobius(k)) * beta(n, m * k)
        for k in range(1, n // m + 1)
    )


def affine_formula(n: int, m: int) -> Fraction:
    if n < m:
        return Fraction(0)
    return Fraction(2 * m - n - 1, n + 1)


def omega(n: int) -> Fraction:
    """Coefficient of (1-2^-s)(1-2^(-s-1))/zeta(s)."""
    ans = Fraction(mobius(n))
    if n % 2 == 0:
        ans -= Fraction(3, 2) * mobius(n // 2)
    if n % 4 == 0:
        ans += Fraction(1, 2) * mobius(n // 4)
    return ans


def omega_local_formula(n: int) -> Fraction:
    e = v2(n)
    odd = n >> e
    layer = {
        0: Fraction(1),
        1: Fraction(-5, 2),
        2: Fraction(2),
        3: Fraction(-1, 2),
    }.get(e, Fraction(0))
    return layer * mobius(odd)


def dipole_row(n: int, m: int) -> Fraction:
    return sum(omega(k) * beta(n, m * k) for k in range(1, n // m + 1))


def dipole_formula(n: int, m: int) -> Fraction:
    if n < m:
        return Fraction(0)
    if n < 2 * m:
        return Fraction(2 * m - n - 1, n + 1)
    if n < 4 * m:
        return Fraction(n + 1 - 8 * m, 2 * (n + 1))
    return Fraction(0)


def c2(n: int) -> int:
    return 1 - v2(n)


def a_star(n: int) -> Fraction:
    """Positive inverse coefficient of zeta/[(1-x)(1-x/2)]."""
    e = v2(n)
    return Fraction(2 * e) + Fraction(1, 2**e)


def dirichlet_convolution(f, g, n: int):
    return sum(f(d) * g(n // d) for d in divisors(n))


def reconstruct_shell(values: list[Fraction], x: int) -> Fraction:
    """Invert W(x)=B(x)-B(floor(x/2))/2 pointwise."""
    ans = Fraction(0)
    scale = Fraction(1)
    y = x
    while y >= 1:
        ans += scale * values[y]
        scale /= 2
        y //= 2
    return ans


def add_positive_block(b: list[Fraction], A: int, B: int, t: Fraction) -> None:
    assert 1 <= A < B < len(b)
    assert t >= 0
    for m in range(A + 1, B + 1):
        b[m] += t


def prime_constraint(b: list[Fraction], p: int) -> Fraction:
    X = len(b) - 1
    return sum(
        b[m] * ((1 if m % p == 0 else 0) - (1 if (m - 1) % p == 0 else 0))
        for m in range(2, X + 1)
    )


def validate_bipartite_transport(
    X: int,
    defects: dict[int, Fraction],
    slacks: dict[int, Fraction],
    blocks: list[tuple[int, int, Fraction]],
) -> tuple[dict[int, Fraction], dict[int, Fraction]]:
    positive = set(defects)
    negative = set(slacks)
    assert positive.isdisjoint(negative)
    outgoing = {p: Fraction(0) for p in positive}
    incoming = {p: Fraction(0) for p in negative}
    for A, B, t in blocks:
        assert 1 <= A < B <= X
        assert t >= 0
        assert is_squarefree(A) and is_squarefree(B)
        fa = set(factorint(A))
        fb = set(factorint(B))
        assert fa and fa <= positive
        assert fb and fb <= negative
        for p in fa:
            outgoing[p] += t
        for p in fb:
            incoming[p] += t
    assert all(outgoing[p] >= defects[p] for p in positive)
    assert all(incoming[p] <= slacks[p] for p in negative)
    return outgoing, incoming


def main() -> None:
    checks = {
        "affine_rows": 0,
        "dipole_rows": 0,
        "local_coefficients": 0,
        "digital_convolution": 0,
        "positive_inverse": 0,
        "shell_inversions": 0,
        "transport_rows": 0,
        "mutations_rejected": 0,
    }

    for n in range(2, MAX_N + 1):
        for m in range(2, n + 1):
            assert affine_mobius_row(n, m) == affine_formula(n, m)
            checks["affine_rows"] += 1

    for n in range(2, MAX_N + 1):
        for m in range(2, n + 1):
            assert dipole_row(n, m) == dipole_formula(n, m)
            checks["dipole_rows"] += 1

    for n in range(1, MAX_N + 1):
        assert omega(n) == omega_local_formula(n)
        checks["local_coefficients"] += 1

    for n in range(1, MAX_N + 1):
        got = dirichlet_convolution(c2, omega, n)
        want = (
            Fraction(1) if n == 1 else
            Fraction(-5, 2) if n == 2 else
            Fraction(1) if n == 4 else
            Fraction(0)
        )
        assert got == want
        checks["digital_convolution"] += 1

    for n in range(1, MAX_N + 1):
        got = dirichlet_convolution(a_star, omega, n)
        assert got == (1 if n == 1 else 0)
        assert a_star(n) > 0
        checks["positive_inverse"] += 1

    B = [Fraction(0)] + [
        Fraction((17 * x * x + 5 * x + 3) % 101, 37)
        for x in range(1, MAX_N + 1)
    ]
    W = [Fraction(0)] * (MAX_N + 1)
    for x in range(1, MAX_N + 1):
        W[x] = B[x] - Fraction(1, 2) * B[x // 2]
    for x in range(1, MAX_N + 1):
        assert reconstruct_shell(W, x) == B[x]
        checks["shell_inversions"] += 1

    X = 30
    defects = {2: Fraction(1, 2), 3: Fraction(1, 2), 5: Fraction(1, 4)}
    slacks = {23: Fraction(2, 7), 29: Fraction(3, 5)}
    blocks = [
        (6, 29, Fraction(3, 5)),
        (5, 23, Fraction(2, 7)),
    ]
    outgoing, incoming = validate_bipartite_transport(X, defects, slacks, blocks)
    assert outgoing[2] >= defects[2] and outgoing[3] >= defects[3]
    assert outgoing[5] >= defects[5]
    assert incoming[23] <= slacks[23] and incoming[29] <= slacks[29]

    all_primes = primes_upto(X)
    base = [Fraction(0)] * (X + 1)
    after_b = base[:]
    for A, Bp, t in blocks:
        add_positive_block(after_b, A, Bp, t)
    assert all(x >= 0 for x in after_b)
    for p in all_primes:
        expected = Fraction(0)
        for A, Bp, t in blocks:
            expected -= t * (1 if A % p == 0 else 0)
            expected += t * (1 if Bp % p == 0 else 0)
        assert prime_constraint(after_b, p) == expected
    checks["transport_rows"] = len(all_primes) * len(blocks)

    def broken_dipole(n: int, m: int) -> Fraction:
        return affine_formula(n, m) - Fraction(3, 2) * affine_formula(n, 2 * m)

    assert broken_dipole(8 * 7, 7) != 0
    checks["mutations_rejected"] += 1

    def absolute_omega(n: int) -> Fraction:
        return abs(omega(n))

    assert dirichlet_convolution(c2, absolute_omega, 8) != 0
    checks["mutations_rejected"] += 1

    def wrong_source(n: int) -> Fraction:
        ans = Fraction(mobius(n))
        if n % 2 == 0:
            ans -= mobius(n // 2)
        if n % 4 == 0:
            ans += Fraction(1, 2) * mobius(n // 4)
        return ans

    wrong_tail = sum(wrong_source(k) * beta(80, 5 * k) for k in range(1, 17))
    assert wrong_tail != 0
    checks["mutations_rejected"] += 1

    try:
        add_positive_block(base[:], 29, 6, Fraction(1))
    except AssertionError:
        checks["mutations_rejected"] += 1
    else:
        raise AssertionError("reversed transport interval was accepted")

    try:
        validate_bipartite_transport(X, defects, slacks, [(6, 25, Fraction(1, 2))])
    except AssertionError:
        checks["mutations_rejected"] += 1
    else:
        raise AssertionError("wrong-side endpoint was accepted")

    try:
        validate_bipartite_transport(
            X, defects, slacks,
            [(6, 29, Fraction(4, 5)), (5, 23, Fraction(2, 7))],
        )
    except AssertionError:
        checks["mutations_rejected"] += 1
    else:
        raise AssertionError("overfilled slack capacity was accepted")

    result = {
        "classification": "EXACT_DYADIC_PARITY_DIPOLE_ALGEBRA_VERIFIED",
        "max_n": MAX_N,
        "checks": checks,
        "dipole_support_ratio": 4,
        "source_layers": ["1", "-5/2", "2", "-1/2"],
        "digital_output": ["1@1", "-5/2@2", "1@4"],
        "proof_boundary": (
            "finite algebra only; the reflected dyadic Hall reserve and RH remain unproved"
        ),
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
