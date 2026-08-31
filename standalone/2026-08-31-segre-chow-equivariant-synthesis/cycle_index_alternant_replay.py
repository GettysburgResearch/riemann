#!/usr/bin/env python3
"""Exact replay of the cycle-index alternant theorem at (d,m)=(3,3)."""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from typing import Dict, List, Sequence, Tuple


def compositions(n: int, d: int) -> List[Tuple[int, ...]]:
    if d == 1:
        return [(n,)]
    out: List[Tuple[int, ...]] = []
    for a in range(n + 1):
        for tail in compositions(n - a, d - 1):
            out.append((a,) + tail)
    return out


def poly_mul(a: Sequence[Fraction], b: Sequence[Fraction]) -> List[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_add(a: Sequence[Fraction], b: Sequence[Fraction]) -> List[Fraction]:
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]


def poly_scale(a: Sequence[Fraction], c: Fraction) -> List[Fraction]:
    return [c * x for x in a]


def trim(a: Sequence[Fraction]) -> List[Fraction]:
    out = list(a)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def complete_h(xs: Sequence[int | Fraction], nmax: int) -> List[Fraction]:
    h = [Fraction(0)] * (nmax + 1)
    h[0] = 1
    for x in xs:
        nxt = [Fraction(0)] * (nmax + 1)
        for n in range(nmax + 1):
            power = Fraction(1)
            for k in range(n + 1):
                nxt[n] += h[n - k] * power
                power *= x
        h = nxt
    return h


def det3(m: Sequence[Sequence[Fraction]]) -> Fraction:
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def schur3(partition: Tuple[int, int, int], xs: Sequence[int]) -> Fraction:
    h = complete_h(xs, partition[0] + 2)
    hv = lambda n: Fraction(0) if n < 0 else h[n]
    return det3([[hv(partition[i] - i + j) for j in range(3)] for i in range(3)])


def dsym_poly(xs: Sequence[int], m: int = 3) -> List[Fraction]:
    out = [Fraction(1)]
    for alpha in compositions(m, len(xs)):
        weight = Fraction(1)
        for x, a in zip(xs, alpha):
            weight *= Fraction(x) ** a
        out = poly_mul(out, [Fraction(1), -weight])
    return out


def twisted_numerator(xs: Sequence[int], cycle_lengths: Sequence[int], max_series_degree: int = 16) -> List[Fraction]:
    d = len(xs)
    hs = [complete_h([Fraction(x) ** ell for x in xs], max_series_degree) for ell in cycle_lengths]
    seq = []
    for r in range(max_series_degree + 1):
        value = Fraction(1)
        for h in hs:
            value *= h[r]
        seq.append(value)
    numerator = poly_mul(dsym_poly(xs, sum(cycle_lengths)), seq)
    n = len(compositions(sum(cycle_lengths), d))
    if any(numerator[k] != 0 for k in range(n, max_series_degree + 1)):
        raise AssertionError("twisted numerator has a nonzero certified tail")
    return trim(numerator[:n])


S3_CHARS = {
    "trivial": {"111": 1, "21": 1, "3": 1},
    "sign": {"111": 1, "21": -1, "3": 1},
    "standard": {"111": 2, "21": 0, "3": -1},
}

TOR_TABLE = [
    (0, 0, [((0, 0, 0), "trivial", 1)]),
    (0, 1, [((2, 1, 0), "standard", 1), ((1, 1, 1), "sign", 1)]),
    (0, 2, [((2, 2, 2), "trivial", 1), ((3, 3, 0), "sign", 1)]),
    (1, 2, [((4, 1, 1), "standard", 1)]),
    (1, 3, [((5, 2, 2), "trivial", 1), ((5, 2, 2), "standard", 1), ((5, 3, 1), "sign", 1), ((4, 3, 2), "sign", 1)]),
    (2, 4, [((5, 5, 2), "trivial", 1), ((5, 5, 2), "standard", 1), ((6, 4, 2), "sign", 1), ((5, 4, 3), "sign", 1)]),
    (2, 5, [((6, 6, 3), "standard", 1)]),
    (3, 5, [((5, 5, 5), "trivial", 1), ((7, 4, 4), "sign", 1)]),
    (3, 6, [((7, 6, 5), "standard", 1), ((6, 6, 6), "sign", 1)]),
    (3, 7, [((7, 7, 7), "trivial", 1)]),
]


def tor_cycle_numerator(xs: Sequence[int], cycle_key: str) -> List[Fraction]:
    out = [Fraction(0)] * 8
    for homological, internal, summands in TOR_TABLE:
        value = sum(mult * schur3(partition, xs) * S3_CHARS[irrep][cycle_key] for partition, irrep, mult in summands)
        out[internal] += ((-1) ** homological) * value
    return trim(out)


def tor_isotypic_numerator(xs: Sequence[int], irrep: str) -> List[Fraction]:
    out = [Fraction(0)] * 8
    for homological, internal, summands in TOR_TABLE:
        for partition, sector, mult in summands:
            if sector == irrep:
                out[internal] += ((-1) ** homological) * mult * schur3(partition, xs)
    return trim(out)


def explicit_cycle_alternant(xs: Sequence[int], cycle_lengths: Sequence[int]) -> List[Fraction]:
    d = len(xs)
    m = sum(cycle_lengths)
    monomials = compositions(m, d)
    weights: Dict[Tuple[int, ...], Fraction] = {}
    for alpha in monomials:
        w = Fraction(1)
        for x, a in zip(xs, alpha):
            w *= Fraction(x) ** a
        weights[alpha] = w
    total = [Fraction(0)]
    for choices in itertools.product(range(d), repeat=len(cycle_lengths)):
        coeff = Fraction(1)
        beta = [0] * d
        for j, ell in zip(choices, cycle_lengths):
            yj = Fraction(xs[j]) ** ell
            denom = Fraction(1)
            for a in range(d):
                if a != j:
                    denom *= yj - Fraction(xs[a]) ** ell
            coeff *= Fraction(xs[j]) ** (ell * (d - 1)) / denom
            beta[j] += ell
        term = [Fraction(1)]
        for alpha in monomials:
            if alpha != tuple(beta):
                term = poly_mul(term, [Fraction(1), -weights[alpha]])
        total = poly_add(total, poly_scale(term, coeff))
    return trim(total)


def ints_or_strings(poly: Sequence[Fraction]) -> List[int | str]:
    return [int(x) if x.denominator == 1 else str(x) for x in poly]


def run() -> dict:
    cycles = {"111": [1, 1, 1], "21": [2, 1], "3": [3]}
    panels = [(1, 1, 1), (2, 3, 5), (1, -1, 2), (2, 2, 3)]
    panel_results = []
    for xs in panels:
        rows, computed = {}, {}
        for key, lengths in cycles.items():
            actual = twisted_numerator(xs, lengths)
            expected = tor_cycle_numerator(xs, key)
            if actual != expected:
                raise AssertionError(f"cycle trace mismatch at {xs}, {key}")
            rows[key], computed[key] = ints_or_strings(actual), actual
        e, t, c = computed["111"], computed["21"], computed["3"]
        n = max(len(e), len(t), len(c))
        pad = lambda a: list(a) + [Fraction(0)] * (n - len(a))
        e, t, c = pad(e), pad(t), pad(c)
        inverted = {
            "trivial": [(e[i] + 3 * t[i] + 2 * c[i]) / 6 for i in range(n)],
            "sign": [(e[i] - 3 * t[i] + 2 * c[i]) / 6 for i in range(n)],
            "standard": [(e[i] - c[i]) / 3 for i in range(n)],
        }
        isotypic = {}
        for irrep, poly in inverted.items():
            direct = pad(tor_isotypic_numerator(xs, irrep))
            if poly != direct:
                raise AssertionError(f"character inversion mismatch at {xs}, {irrep}")
            isotypic[irrep] = ints_or_strings(trim(poly))
        panel_results.append({"diagonal": list(xs), "cycle_numerators": rows, "isotypic_numerators": isotypic})

    generic = (2, 3, 5)
    alternant_checks = {}
    for key, lengths in cycles.items():
        alt = explicit_cycle_alternant(generic, lengths)
        direct = twisted_numerator(generic, lengths)
        if alt != direct:
            raise AssertionError(f"explicit alternant mismatch for {key}")
        alternant_checks[key] = ints_or_strings(alt)

    return {
        "theorem": "cycle-index alternant reconstruction at d=m=3",
        "panels": panel_results,
        "explicit_alternant_generic_diagonal": {"diagonal": list(generic), "cycle_numerators": alternant_checks},
        "all_cycle_traces_match_complete_GL3_x_S3_Tor_table": True,
        "character_inversion_matches_every_isotypic_Euler_polynomial": True,
        "explicit_alternant_matches_all_three_cycle_types": True,
        "all_checks_passed": True,
        "rh_or_grh_established": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output")
    args = parser.parse_args()
    text = json.dumps(run(), indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
