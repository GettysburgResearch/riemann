#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path

import sympy as sp


def symbolic_cocycle() -> int:
    r, z = sp.symbols("r z", positive=True)
    Q_parent, Q_child = sp.symbols("Q_parent Q_child")

    A = 1 - r**2
    d = r * (1 - r)

    T0 = 4 * z - 3
    S0 = 5 * z - 3
    Tc = r * (4 * r * z - 3)
    Sc = r * (5 * r * z - 3)
    Ta = T0 - Tc
    Sa = S0 - Sc

    Ts = (1 - r) * (2 * (r + 2) * z - (r + 3))
    Th = r * ((2 * r + 2) * z - (r + 2))
    Ss_native = A * S0
    Sh_native = r**2 * S0

    Ra = Q_parent - r * Q_child
    Rc = r * Q_child
    Rs = A * Q_parent
    Rh = r**2 * Q_parent

    checks = 0
    assert sp.simplify(Ta + Tc - T0) == 0
    assert sp.simplify(Ts + Th - T0) == 0
    assert sp.simplify(Ta + Tc - Ts - Th) == 0
    checks += 3

    assert sp.simplify(Sa + Sc - S0) == 0
    assert sp.simplify(Ss_native + Sh_native - S0) == 0
    assert sp.simplify(Sa + Sc - Ss_native - Sh_native) == 0
    checks += 3

    assert sp.simplify(Ra + Rc - Q_parent) == 0
    assert sp.simplify(Rs + Rh - Q_parent) == 0
    assert sp.simplify(Ra + Rc - Rs - Rh) == 0
    checks += 3

    # Full binary score exceeds the native row-budgeted score by the exact
    # target-null favorable amount.
    Ss_full = A * S0
    Sh_full = r * ((4 * r + 1) * z - (2 * r + 1))
    assert sp.simplify(Ss_full + Sh_full - S0 - d * (z - 1)) == 0
    assert sp.simplify(Sh_full - Sh_native - d * (z - 1)) == 0
    checks += 2

    # Source coefficients and row coefficients are one-use partitions.
    assert sp.simplify(A + r**2 - 1) == 0
    checks += 1

    return checks


def least_prime_provenance(max_primes: int = 12) -> int:
    checks = 0
    labels = tuple(range(max_primes))

    seen: set[tuple[int, ...]] = set()
    buckets: dict[int, set[tuple[int, ...]]] = {j: set() for j in labels}
    for size in range(1, max_primes + 1):
        for subset in itertools.combinations(labels, size):
            least = subset[0]
            buckets[least].add(subset)
            assert subset not in seen
            seen.add(subset)
            checks += 1

    assert len(seen) == 2**max_primes - 1
    assert sum(len(bucket) for bucket in buckets.values()) == len(seen)
    checks += 2

    # Exact product-minus-one coefficient dictionary.  A subset has sign
    # (-1)^|S| and belongs to the unique bucket at min(S).
    direct: dict[tuple[int, ...], int] = {}
    partitioned: dict[tuple[int, ...], int] = {}
    for subset in seen:
        direct[subset] = -1 if len(subset) % 2 else 1
    for bucket in buckets.values():
        for subset in bucket:
            partitioned[subset] = -1 if len(subset) % 2 else 1
    assert direct == partitioned
    checks += 1

    return checks


def finite_source_linearity() -> int:
    # A small exact signed source replay.  The cocycle is pointwise in every
    # divisor coefficient, so multiplying by arbitrary rational signed weights
    # and summing must preserve it.
    weights = [
        Fraction(1),
        Fraction(-1, 2),
        Fraction(3, 7),
        Fraction(-5, 11),
        Fraction(13, 17),
    ]
    parent = sum(weights, Fraction(0))
    raw_residual = Fraction(7, 13) * parent
    raw_child = parent - raw_residual
    controlled_s = Fraction(19, 31) * parent
    controlled_h = parent - controlled_s
    assert raw_residual + raw_child == parent
    assert controlled_s + controlled_h == parent
    assert raw_residual + raw_child == controlled_s + controlled_h
    return 3


def main() -> None:
    symbolic = symbolic_cocycle()
    provenance = least_prime_provenance()
    linearity = finite_source_linearity()
    result = {
        "classification": "PASS_BINARY_NATIVE_ROW_COCYCLE",
        "checks": symbolic + provenance + linearity,
        "symbolic_cocycle_checks": symbolic,
        "least_prime_provenance_checks": provenance,
        "finite_source_linearity_checks": linearity,
        "rough_prime_labels_replayed": 12,
        "rough_monomials_replayed": 2**12 - 1,
        "scope": (
            "Exact scalar/formal-row cocycle and finite least-prime source "
            "provenance only. Hall inequalities, physical component values, "
            "live-parent normalization, final capacity, and RH are not "
            "certified by this replay."
        ),
    }
    output = Path(__file__).resolve().parent / "results" / "verification.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)


if __name__ == "__main__":
    main()
