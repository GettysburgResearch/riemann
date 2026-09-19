#!/usr/bin/env python3
"""BCP26: exact cutoff-pivot channels and directed complete annular Grams.

Python standard library only. This computes finite identities, not RH.
The native channels are produced from the input prefix by g * e_p. Output
factorization is used only by the independent checker, never as source data.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Iterable

BITS = 80
SCALE = 1 << BITS
CUTOFFS = (3, 7, 15, 31, 63, 255)


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


def spf_sieve(limit: int) -> list[int]:
    require(type(limit) is int and limit >= 1, "positive integer limit required")
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def mobius_prefix(limit: int) -> list[int]:
    """The producer generates only the requested input prefix."""
    spf = spf_sieve(limit)
    mu = [0, 1] + [0] * (limit - 1)
    for n in range(2, limit + 1):
        p, m = spf[n], n // spf[n]
        mu[n] = 0 if m % p == 0 else -mu[m]
    return mu


def native_channels(Y: int) -> tuple[list[str], list[dict[int, int]], list[int]]:
    require(type(Y) is int and Y >= 1, "Y must be a positive integer")
    b, stop = Y + 1, (Y + 1) ** 2
    B = stop - 1
    mu = mobius_prefix(Y)
    spf = spf_sieve(B)  # Used for residual labels, not future Mobius values.
    ps = [p for p in range(2, Y + 1) if spf[p] == p]
    labels = ["prefix"] + [str(p) for p in ps] + ["p>Y"]
    index = {p: i + 1 for i, p in enumerate(ps)}
    last = len(labels) - 1
    e = [0] * (B + 1)
    e[1] = 1
    for r in range(1, b):
        if mu[r]:
            for n in range(r, stop, r):
                e[n] -= mu[r]
    require(not any(e[1:b]), "native low-divisor identities failed")
    rows: list[dict[int, int]] = [{b: sum(mu)}] + [{} for _ in labels[1:]]
    for r in range(1, b):
        if not mu[r]:
            continue
        for n in range(b, B // r + 1):
            if e[n]:
                row = rows[index.get(spf[n], last)]
                t = r * n
                row[t] = row.get(t, 0) + mu[r] * e[n]
    rows = [{t: v for t, v in row.items() if v} for row in rows]
    return labels, rows, mu


def dyadic_sum_terms(terms: Iterable[tuple[int, int]]) -> tuple[int, int]:
    lo = hi = 0
    for numerator, denominator in terms:
        require(denominator > 0, "nonpositive denominator")
        q, r = divmod(SCALE * numerator, denominator)
        lo += q
        hi += q + bool(r)
    return lo, hi


def gram(a: dict[int, int], b: dict[int, int], left: int, right: int) -> tuple[int, int]:
    """Integrate the actual step functions on EVERY cell, via event merging.

    On a constant interval [s,t), the exact term is va*vb*(1/s-1/t).
    Directed rounding is applied to that entire signed rational term.
    """
    require(0 < left < right, "invalid interval")
    require(all(left <= n < right for n in a), "left row event out of range")
    require(all(left <= n < right for n in b), "right row event out of range")
    va = vb = 0
    pos = left
    lo = hi = 0
    for t in sorted(a.keys() | b.keys()):
        if t > pos and va and vb:
            q, r = divmod(SCALE * va * vb * (t - pos), pos * t)
            lo += q
            hi += q + bool(r)
        va += a.get(t, 0)
        vb += b.get(t, 0)
        pos = t
    if pos < right and va and vb:
        q, r = divmod(SCALE * va * vb * (right - pos), pos * right)
        lo += q
        hi += q + bool(r)
    return lo, hi


def add(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] + y[0], x[1] + y[1]


def subtract(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return x[0] - y[1], x[1] - y[0]


def squared_term(x: tuple[int, int], coefficient: int) -> tuple[int, int]:
    a, b = x
    low = 0 if a <= 0 <= b else min(a * a, b * b)
    high = max(a * a, b * b)
    l = coefficient * low // SCALE
    h = -(-coefficient * high // SCALE)
    return l, h


def encoded(x: tuple[int, int]) -> list[str]:
    return [str(x[0]), str(x[1])]


def decoded(x: object) -> tuple[int, int]:
    require(isinstance(x, list) and len(x) == 2, "interval must have two string endpoints")
    require(all(type(v) is str and str(int(v)) == v for v in x), "noncanonical endpoint")
    result = int(x[0]), int(x[1])
    require(result[0] <= result[1], "reversed interval")
    return result


def row_digest(row: dict[int, int]) -> str:
    text = "".join(f"{n}:{row[n]}\n" for n in sorted(row))
    return hashlib.sha256(text.encode()).hexdigest()


def positive_sector(Y: int, spf: list[int]) -> dict:
    """Finite lower bounds of PROOF.md, valid for Y >= 17; exact prime counts."""
    if Y < 17:
        return {"applicable": False}
    P = [p for p in range(2, Y + 1) if spf[p] == p and 3 * Y < 4 * p and 5 * p <= 4 * Y]
    Q = [q for q in range(2, Y + 1) if spf[q] == q and 4 * Y < 5 * q and 10 * q <= 9 * Y]
    n, m = len(P), len(Q)
    return {
        "applicable": True, "P": P, "Q": Q,
        "diagonal_lower": str(Fraction(n * m * m, 3 * Y * Y)),
        "ordered_cross_lower": str(Fraction(n * (n - 1) * m * m, 3 * Y * Y)),
        "coprime_ordered_cross_lower": str(Fraction(n * (n - 1) * m * (m - 1), 3 * Y * Y)),
    }


def panel(Y: int) -> dict:
    labels, rows, mu = native_channels(Y)
    b, stop = Y + 1, (Y + 1) ** 2
    total: dict[int, int] = {}
    for row in rows:
        for n, v in row.items():
            total[n] = total.get(n, 0) + v
    total = {n: v for n, v in total.items() if v}
    I = gram(total, total, b, stop)
    D = (0, 0)
    upper = []
    for i, row in enumerate(rows):
        for j in range(i, len(rows)):
            g = gram(row, rows[j], b, stop)
            upper.append([i, j, *encoded(g)])
            if i == j:
                D = add(D, g)
    means = [gram(row, {b: 1}, b, stop) for row in rows]
    ell = gram(total, {b: 1}, b, stop)
    M = 0
    e_terms, u_terms = [], []
    for n in range(1, b):
        M += mu[n]
        e_terms.append((M * M, n * (n + 1)))
        u_terms.append((M, n * (n + 1)))
    E0, u0 = dyadic_sum_terms(e_terms), dyadic_sum_terms(u_terms)
    Eout = add(E0, I)
    uout = add(u0, ell)
    Aout = add(Eout, squared_term(uout, 2 * stop))
    Fout = add(Eout, squared_term(uout, stop))
    Ain = add(E0, squared_term(u0, 2 * b))
    return {
        "Y": Y, "b": b, "B": stop - 1, "labels": labels,
        "row_event_counts": [len(r) for r in rows],
        "row_sha256": [row_digest(r) for r in rows],
        "gram_upper_triangle": upper,
        "means": [encoded(x) for x in means],
        "annular_I": encoded(I), "diagonal_D": encoded(D),
        "ordered_cross_C": encoded(subtract(I, D)),
        "E_input": encoded(E0), "u_input": encoded(u0),
        "A_input": encoded(Ain), "E_output": encoded(Eout),
        "u_output": encoded(uout), "A_output": encoded(Aout),
        "F_output": encoded(Fout),
        "native_positive_sector": positive_sector(Y, spf_sieve(Y)),
    }


def report(cutoffs: tuple[int, ...] = CUTOFFS) -> dict:
    return {
        "schema": "BCP26.boundary-pivot.v1", "arithmetic": "directed rational",
        "dyadic_denominator_bits": BITS,
        "status": "FINITE IDENTITIES; NO UNBOUNDED NATIVE UPPER BOUND",
        "panels": [panel(Y) for Y in cutoffs],
    }


def canonical(obj: object) -> str:
    return json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=True) + "\n"


def reject_duplicates(pairs: list[tuple[str, object]]) -> dict:
    obj = {}
    for k, v in pairs:
        require(k not in obj, f"duplicate JSON key: {k}")
        obj[k] = v
    return obj


def load(path: Path) -> object:
    return json.loads(path.read_text(), object_pairs_hook=reject_duplicates)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path)
    p.add_argument("--check", type=Path)
    args = p.parse_args()
    result = canonical(report())
    if args.check:
        require(args.check.read_text() == result, "report does not reproduce byte for byte")
        print("BCP26 producer: PASS (byte-identical report)")
    elif args.output:
        args.output.write_text(result)
        print(f"BCP26 producer: wrote {args.output}")
    else:
        print(result, end="")

if __name__ == "__main__":
    main()
