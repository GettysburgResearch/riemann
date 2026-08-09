#!/usr/bin/env python3
"""Exact formal-log replay for L-34409's Möbius Haar curvature identity."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path

ROW_LIMIT = 30
ARITH_LIMIT = 4 * ROW_LIMIT

Linear = Counter[int]
Quadratic = Counter[tuple[int, int]]


def factor(n: int) -> dict[int, int]:
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


def mobius(n: int) -> int:
    fac = factor(n)
    if any(a > 1 for a in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def odd_lambda(n: int) -> Linear:
    fac = factor(n)
    if len(fac) != 1:
        return Counter()
    p = next(iter(fac))
    return Counter() if p == 2 else Counter({p: 1})


def integer_log(n: int) -> Linear:
    return Counter(factor(n))


def add_linear(target: Linear, source: Linear, scale: int = 1) -> None:
    for p, c in source.items():
        target[p] += scale * c
        if target[p] == 0:
            del target[p]


def add_quadratic(target: Quadratic, source: Quadratic, scale: int = 1) -> None:
    for monomial, c in source.items():
        target[monomial] += scale * c
        if target[monomial] == 0:
            del target[monomial]


def product(a: Linear, b: Linear) -> Quadratic:
    out: Quadratic = Counter()
    for p, cp in a.items():
        for q, cq in b.items():
            out[tuple(sorted((p, q)))] += cp * cq
    return +out


def square(a: Linear) -> Quadratic:
    return product(a, a)


def c_odd(n: int) -> Quadratic:
    out = product(odd_lambda(n), integer_log(n))
    for d in divisors(n):
        add_quadratic(out, product(odd_lambda(d), odd_lambda(n // d)))
    return +out


def convolve_scalar_linear(a: list[int], b: list[Linear], n: int) -> Linear:
    out: Linear = Counter()
    for d in divisors(n):
        if a[d]:
            add_linear(out, b[n // d], a[d])
    return +out


def convolve_scalar_quadratic(a: list[int], b: list[Quadratic], n: int) -> Quadratic:
    out: Quadratic = Counter()
    for d in divisors(n):
        if a[d]:
            add_quadratic(out, b[n // d], a[d])
    return +out


def shift_scalar(a: list[int], multiplier: int, sign: int) -> list[int]:
    out = a.copy()
    for n in range(multiplier, len(a)):
        if n % multiplier == 0:
            out[n] += sign * a[n // multiplier]
    return out


def shift_linear(a: list[Linear], multiplier: int, sign: int) -> list[Linear]:
    out = [x.copy() for x in a]
    for n in range(multiplier, len(a)):
        if n % multiplier == 0:
            add_linear(out[n], a[n // multiplier], sign)
    return out


def shift_quadratic(a: list[Quadratic], multiplier: int, sign: int) -> list[Quadratic]:
    out = [x.copy() for x in a]
    for n in range(multiplier, len(a)):
        if n % multiplier == 0:
            add_quadratic(out[n], a[n // multiplier], sign)
    return out


def carry(n: int, j: int, q: int) -> int:
    return n // q - j // q - (n - j) // q


def carry_scalar(sequence: list[int], n: int, j: int) -> int:
    return sum(sequence[q] * carry(n, j, q) for q in range(1, n + 1))


def carry_linear(sequence: list[Linear], n: int, j: int) -> Linear:
    out: Linear = Counter()
    for q in range(1, n + 1):
        c = carry(n, j, q)
        if c:
            add_linear(out, sequence[q], c)
    return +out


def carry_quadratic(sequence: list[Quadratic], n: int, j: int) -> Quadratic:
    out: Quadratic = Counter()
    for q in range(1, n + 1):
        c = carry(n, j, q)
        if c:
            add_quadratic(out, sequence[q], c)
    return +out


def curvature(q: Linear, y: int, t: Quadratic) -> Quadratic:
    out = square(q)
    add_quadratic(out, t, -y)
    return +out


def main() -> None:
    mu = [0] * (ARITH_LIMIT + 1)
    b_odd = [0] * (ARITH_LIMIT + 1)
    lam = [Counter() for _ in range(ARITH_LIMIT + 1)]
    c = [Counter() for _ in range(ARITH_LIMIT + 1)]
    for n in range(1, ARITH_LIMIT + 1):
        mu[n] = mobius(n)
        b_odd[n] = mu[n] if n % 2 else 0
        lam[n] = odd_lambda(n)
        c[n] = c_odd(n)

    q0 = [Counter() for _ in range(ARITH_LIMIT + 1)]
    t0 = [Counter() for _ in range(ARITH_LIMIT + 1)]
    q_odd = [Counter() for _ in range(ARITH_LIMIT + 1)]
    t_odd = [Counter() for _ in range(ARITH_LIMIT + 1)]
    for n in range(1, ARITH_LIMIT + 1):
        q0[n] = convolve_scalar_linear(mu, lam, n)
        t0[n] = convolve_scalar_quadratic(mu, c, n)
        q_odd[n] = convolve_scalar_linear(b_odd, lam, n)
        t_odd[n] = convolve_scalar_quadratic(b_odd, c, n)

    b_plus = shift_scalar(mu, 2, +1)
    b_minus = shift_scalar(mu, 2, -1)
    b_relative = shift_scalar(b_odd, 4, -1)
    assert b_plus == b_relative

    q_plus = shift_linear(q0, 2, +1)
    q_minus = shift_linear(q0, 2, -1)
    q_relative = shift_linear(q_odd, 4, -1)
    assert q_plus == q_relative

    t_plus = shift_quadratic(t0, 2, +1)
    t_minus = shift_quadratic(t0, 2, -1)
    t_relative = shift_quadratic(t_odd, 4, -1)
    assert t_plus == t_relative

    checked_rows = 0
    for n in range(2, ROW_LIMIT + 1):
        for j in range(1, n):
            # Base source charges are -1 at both aligned rows.
            y4 = carry_scalar(mu, 4 * n, 4 * j)
            y2 = carry_scalar(mu, 2 * n, 2 * j)
            yp = carry_scalar(b_plus, 4 * n, 4 * j)
            ym = carry_scalar(b_minus, 4 * n, 4 * j)
            assert (y4, y2, yp, ym) == (-1, -1, -2, 0)

            q4 = carry_linear(q0, 4 * n, 4 * j)
            q2 = carry_linear(q0, 2 * n, 2 * j)
            qp = carry_linear(q_plus, 4 * n, 4 * j)
            qm = carry_linear(q_minus, 4 * n, 4 * j)
            qsum = q4.copy(); add_linear(qsum, q2)
            qdiff = q4.copy(); add_linear(qdiff, q2, -1)
            assert qp == qsum and qm == qdiff

            t4 = carry_quadratic(t0, 4 * n, 4 * j)
            t2 = carry_quadratic(t0, 2 * n, 2 * j)
            tp = carry_quadratic(t_plus, 4 * n, 4 * j)
            tm = carry_quadratic(t_minus, 4 * n, 4 * j)
            tsum = t4.copy(); add_quadratic(tsum, t2)
            tdiff = t4.copy(); add_quadratic(tdiff, t2, -1)
            assert tp == tsum and tm == tdiff

            cp = curvature(qp, yp, tp)
            cm = curvature(qm, ym, tm)
            lhs = cp.copy(); add_quadratic(lhs, cm)
            rhs = curvature(q4, y4, t4)
            rhs2 = curvature(q2, y2, t2)
            rhs = Counter({m: 2 * v for m, v in rhs.items()})
            add_quadratic(rhs, rhs2, 2)
            assert +lhs == +rhs

            # The complement has zero bare charge, hence pure square curvature.
            assert cm == square(qm)
            checked_rows += 1

    data = {
        "schema": "X-34402-odd-root-haar-complement-v1",
        "classification": "EXACT_FORMAL_LOG_ROOT_HAAR_CURVATURE_VERIFIED",
        "row_limit": ROW_LIMIT,
        "rows_checked": checked_rows,
        "source_identity": "(epsilon-delta_4)b_odd=(epsilon+delta_2)mu",
        "plus_bare_charge": -2,
        "minus_bare_charge": 0,
        "curvature_identity": (
            "C_plus(4e)+C_minus(4e)=2C_0(4e)+2C_0(2e)"
        ),
        "minus_curvature": "|Q_0(4e)-Q_0(2e)|^2",
        "arithmetic": "formal independent log(p) and log(p)*log(q) monomials",
        "does_not_prove": [
            "reflected upper recurrence",
            "subpower principal-current energy",
            "Riemann Hypothesis",
        ],
    }
    canonical = json.dumps(data, sort_keys=True, separators=(",", ":"))
    data["sha256_without_digest"] = hashlib.sha256(canonical.encode()).hexdigest()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    path = Path(__file__).with_name("results") / "haar-verification.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
