#!/usr/bin/env python3
"""Exact bounded principal-weighted protected-gauge matrix replay."""

from __future__ import annotations

import argparse
import json
import subprocess
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import product
from math import isqrt, prod
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "PHASE_PROTECTED_PRINCIPAL_GAUGE_TRANSFER.md"
FIXTURE = HERE / "phase_protected_principal_gauge_transfer.json"
TEST = ROOT / "tests" / "test_phase_protected_principal_gauge_transfer.py"
FAMILY = "86cac1d64364015ec2cc0f8fbb6fc75dc041c12b"
SOURCES = {
    (
        "ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc",
        "claims/lemmas/L-102706-euler-half-divisor-homotopies-are-subcritically-gauge-equivalent.md",
    ): "6192bec36636e2d35b2aba4fdd64eb4bcf93c2d9",
    (
        FAMILY,
        "claims/lemmas/L-106090-least-discrepancy-prime-triangularizes-the-coprime-boolean-core.md",
    ): "dadf3a4a65d2575983d692dafc0c94142c9a038d",
    (
        FAMILY,
        "claims/lemmas/L-106120-bilateral-least-prime-phases-form-a-tensor-kummer-family.md",
    ): "a8d829dc10611adb7bfb4853902bdff0ab02a065",
    (
        FAMILY,
        "claims/lemmas/L-106121-bilateral-tensor-moment-has-a-paid-atomic-diagonal.md",
    ): "955c3ed0363ca330439eedbae1bf0041a4c96468",
    (
        FAMILY,
        "claims/theorems/T-106140-wick-centered-additive-kummer-conjunction-frontier.md",
    ): "d5be8e376c88b63de0be19e0d9e8791624e99ae2",
    (
        "e501c45ecc39f71b3f26abfe952366eb529c7c2d",
        "research/riemann-structures/GAUGE_CONNECTION_SOURCE_TRANSPORT.md",
    ): "35390e5f48304e8c586c1268b8ae215bbb252aaf",
    (
        "ce0cc6e48e3cdaedd9d5f52fb087b03e8f86c257",
        "research/riemann-structures/PRINCIPAL_SELECTOR_GAUGE_OBSTRUCTION.md",
    ): "a4757412c5e9d085e2970e768cbb1d5c4953e554",
}
MAX_BYTES = 262144
MAX_DIM = 32
ELL, RHO = 5, 13
P_OWNERS, Q_OWNERS = (31, 37), (11, 17)
PRIMES = (3, 7, 29)
HORIZON = 100000000
ABS_A = Fraction(1, 16)
ABS_B = 2 * ABS_A + ABS_A**2
ABS_F = 1 + ABS_B
ZERO = Fraction(0)
ONE = Fraction(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def source_bytes(key):
    require(key in SOURCES, "frozen primitive identity")
    ref = f"{key[0]}:{key[1]}"
    size = int(
        subprocess.run(
            ["git", "cat-file", "-s", ref],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    )
    require(0 < size <= MAX_BYTES, "source byte cap")
    raw = subprocess.run(
        ["git", "show", ref],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout
    require(len(raw) == size, "source byte count")
    digest = sha1(b"blob " + str(size).encode() + b"\0" + raw).hexdigest()
    require(digest == SOURCES[key], "frozen primitive Git blob")
    return raw


def prime(p: int) -> bool:
    require(type(p) is int and 2 <= p <= 1000000, "prime type/range cap")
    return all(p % d for d in range(2, isqrt(p) + 1))


def allowed(p: int) -> tuple[int, ...]:
    require(prime(p), "prime alphabet")
    if p in P_OWNERS + Q_OWNERS or p == 67:
        return (0,)
    if p == ELL:
        return (1,)
    if p == RHO:
        return (2,)
    if p < ELL:
        return (0, 3)
    if p < RHO:
        return (0, 1, 3)
    return (0, 1, 2, 3)


def alphabet(primes: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    require(type(primes) is tuple and len(primes) <= 5, "alphabet cap/type")
    require(len(set(primes)) == len(primes), "distinct prime labels")
    require(
        not set(primes).intersection((ELL, RHO) + P_OWNERS + Q_OWNERS + (67,)),
        "variable labels avoid mandatory and forbidden primes",
    )
    states = tuple(allowed(p) for p in primes)
    require(prod(map(len, states)) <= MAX_DIM, "matrix dimension cap")
    return tuple(product(*states))


def parameter(tau: Fraction) -> tuple[Fraction, Fraction]:
    require(type(tau) is Fraction and 0 <= tau <= 1, "exact homotopy parameter")
    return -tau * (1 - tau) / 4, (2 * tau - 1) / 4


def record(state: tuple[int, ...], primes: tuple[int, ...] = PRIMES):
    require(type(state) is tuple and len(state) == len(primes), "record arity")
    require(
        all(
            type(s) is int and s in allowed(p)
            for p, s in zip(primes, state, strict=True)
        ),
        "fixed-phase allowed record",
    )
    left = (ELL,) + tuple(p for p, s in zip(primes, state, strict=True) if s & 1)
    right = (RHO,) + tuple(p for p, s in zip(primes, state, strict=True) if s & 2)
    common = set(left).intersection(right)
    c, d = set(left) - common, set(right) - common
    require(min(c) == ELL and min(d) == RHO, "literal least-prime selectors")
    a, b, g = prod(left), prod(right), prod(common)
    n, m = prod(P_OWNERS) * a * a, prod(Q_OWNERS) * b * b
    weight = Fraction(g * g * ELL * RHO * (ELL + 1) * (RHO + 1), (ELL - 1) * (RHO - 1))
    return {
        "state": list(state),
        "left": list(left),
        "right": list(right),
        "g": g,
        "N": n,
        "M": m,
        "weight": str(weight),
    }


def local_entry(
    p: int, target: int, origin: int, tau: Fraction, inverse: bool = False
) -> tuple[Fraction, Fraction]:
    a, da = parameter(tau)
    states = allowed(p)
    require(type(inverse) is bool, "inverse selector type")
    require(
        type(target) is int
        and type(origin) is int
        and target in states
        and origin in states,
        "local allowed state",
    )
    if target == origin:
        return ONE, ZERO
    if origin & target != origin:
        return ZERO, ZERO
    bits = (target ^ origin).bit_count()
    if bits == 1:
        value = a if target == 3 else a / p
        derivative = da if target == 3 else da / p
        return (-value, -derivative) if inverse else (value, derivative)
    require(origin == 0 and target == 3, "two-bit insertion")
    multiplier = 1
    if inverse:
        if len(states) == 2:
            multiplier = -1
        elif len(states) == 3:
            multiplier = 0
    return multiplier * a * a / p, multiplier * 2 * a * da / p


def tensor_entry(target, origin, primes, tau, inverse=False):
    value, derivative = ONE, ZERO
    for p, to, old in zip(primes, target, origin, strict=True):
        local, dlocal = local_entry(p, to, old, tau, inverse)
        value, derivative = value * local, derivative * local + value * dlocal
    return value, derivative


def raw_weighted_entry(target, origin, primes, tau):
    a, _ = parameter(tau)
    if any(old & to != old for to, old in zip(target, origin, strict=True)):
        return ZERO
    raw = prod(
        (a / p) ** ((to ^ old).bit_count())
        for p, to, old in zip(primes, target, origin, strict=True)
    )
    before, after = record(origin, primes), record(target, primes)
    require(
        Fraction(after["weight"]) / Fraction(before["weight"])
        == Fraction(after["g"], before["g"]) ** 2,
        "exact fixed-phase principal weight",
    )
    return raw * Fraction(after["g"], before["g"])


def matrices(primes=PRIMES, tau=Fraction(1, 3)):
    states = alphabet(primes)
    parameter(tau)
    forward, inverse, derivative, inverse_derivative = [], [], [], []
    for to in states:
        row, irow, drow, idrow = [], [], [], []
        for old in states:
            value, dvalue = tensor_entry(to, old, primes, tau)
            ivalue, idvalue = tensor_entry(to, old, primes, tau, True)
            require(
                value == raw_weighted_entry(to, old, primes, tau),
                "independent raw-gauge/weight assembly",
            )
            row.append(value)
            irow.append(ivalue)
            drow.append(dvalue)
            idrow.append(idvalue)
        forward.append(row)
        inverse.append(irow)
        derivative.append(drow)
        inverse_derivative.append(idrow)
    return states, forward, inverse, derivative, inverse_derivative


def identity(n: int):
    require(type(n) is int and 0 < n <= MAX_DIM, "matrix dimension cap")
    return [[Fraction(i == j) for j in range(n)] for i in range(n)]


def multiply(left, right):
    n = len(left)
    require(
        0 < n <= MAX_DIM
        and len(right) == n
        and all(len(row) == n for row in left + right),
        "bounded square matrices",
    )
    return [
        [sum((left[i][k] * right[k][j] for k in range(n)), ZERO) for j in range(n)]
        for i in range(n)
    ]


def add(left, right):
    return [
        [x + y for x, y in zip(a, b, strict=True)]
        for a, b in zip(left, right, strict=True)
    ]


def restrict(matrix, indices):
    require(
        indices
        and len(set(indices)) == len(indices)
        and all(type(i) is int and 0 <= i < len(matrix) for i in indices),
        "nonempty distinct retained indices",
    )
    return [[matrix[i][j] for j in indices] for i in indices]


def absolute_sums(matrix):
    n = len(matrix)
    rows = max(sum(map(abs, row), ZERO) for row in matrix)
    columns = max(sum((abs(matrix[i][j]) for i in range(n)), ZERO) for j in range(n))
    return rows, columns


def retained(states, horizon=HORIZON, ratio_mask=False):
    require(
        type(horizon) is int and 1 <= horizon <= 10**18, "physical horizon cap/type"
    )
    require(type(ratio_mask) is bool, "ratio mask type")
    indices = []
    for i, state in enumerate(states):
        item = record(state)
        if max(item["N"], item["M"]) <= horizon and (
            not ratio_mask or Fraction(1, 8) < Fraction(item["N"], item["M"]) < 8
        ):
            indices.append(i)
    require(indices, "nonempty retained physical panel")
    return indices


def build():
    for key in SOURCES:
        source_bytes(key)
    tau = Fraction(1, 3)
    states, forward, inverse, derivative, inverse_derivative = matrices(tau=tau)
    n = len(states)
    unit = identity(n)
    require(
        multiply(forward, inverse) == unit and multiply(inverse, forward) == unit,
        "two true inverse identities",
    )
    zero = [[ZERO] * n for _ in range(n)]
    require(
        add(multiply(derivative, inverse), multiply(forward, inverse_derivative))
        == zero,
        "differentiated true inverse identity",
    )
    bound = ABS_F ** len(PRIMES) * prod(1 + ABS_B / p for p in PRIMES)
    derivative_bound = 8 * len(PRIMES) * bound
    sums = {}
    for name, matrix in (
        ("forward", forward),
        ("true_inverse", inverse),
        ("derivative", derivative),
        ("inverse_derivative", inverse_derivative),
    ):
        row, column = absolute_sums(matrix)
        cap = derivative_bound if "derivative" in name else bound
        require(max(row, column) <= cap, "finite Schur majorant")
        sums[name] = {
            "max_absolute_row": str(row),
            "max_absolute_column": str(column),
            "majorant": str(cap),
        }
    downset = retained(states)
    require(
        multiply(restrict(forward, downset), restrict(inverse, downset))
        == identity(len(downset)),
        "downward physical horizon inverse",
    )
    mask = retained(states, ratio_mask=True)
    masked_forward, masked_inverse = restrict(forward, mask), restrict(inverse, mask)
    masked_product = multiply(masked_forward, masked_inverse)
    start, finish = states.index((0, 0, 0)), states.index((0, 0, 3))
    left_mid, right_mid = states.index((0, 0, 1)), states.index((0, 0, 2))
    require(
        start in mask
        and finish in mask
        and left_mid not in mask
        and right_mid not in mask,
        "physical ratio-mask deletes both inverse paths",
    )
    a, _ = parameter(tau)
    defect = masked_product[mask.index(finish)][mask.index(start)]
    require(defect == 2 * a * a / 29 and defect != 0, "masked inverse defect")
    for matrix in (masked_forward, masked_inverse):
        require(max(absolute_sums(matrix)) <= bound, "masked absolute Schur bound")
    low = local_entry(3, 3, 0, tau, True)[0]
    middle = local_entry(7, 3, 0, tau, True)[0]
    require(
        low == -a * a / 3 and middle == 0, "genuine phase-return inverse corrections"
    )
    hashes = {}
    for path in (NOTE, Path(__file__), TEST):
        raw = path.read_bytes()
        require(len(raw) <= MAX_BYTES, "local source cap")
        hashes[path.relative_to(ROOT).as_posix()] = sha256(
            raw.replace(b"\r\n", b"\n")
        ).hexdigest()
    result = {
        "schema": "riemann.phase_protected_principal_gauge.v1",
        "sources": [
            {"commit": key[0], "path": key[1], "git_blob": blob}
            for key, blob in SOURCES.items()
        ],
        "source_hashes": hashes,
        "tau": str(tau),
        "a_tau": str(a),
        "variable_primes": list(PRIMES),
        "phase_primes": [ELL, RHO],
        "owners": [list(P_OWNERS), list(Q_OWNERS)],
        "records": [record(state) for state in states],
        "full_dimension": n,
        "horizon": HORIZON,
        "horizon_dimension": len(downset),
        "ratio_mask_dimension": len(mask),
        "absolute_schur_checks": sums,
        "true_inverse_low_prime_corner": str(low),
        "true_inverse_middle_prime_corner": str(middle),
        "ratio_mask_inverse_defect": str(defect),
        "ratio_mask_endpoints": [record(states[start]), record(states[finish])],
        "deleted_intermediates": [record(states[left_mid]), record(states[right_mid])],
        "matrix_digests": {
            name: sha256(
                canonical([[str(x) for x in row] for row in matrix]).encode()
            ).hexdigest()
            for name, matrix in (
                ("forward", forward),
                ("inverse", inverse),
                ("derivative", derivative),
                ("inverse_derivative", inverse_derivative),
            )
        },
        "exact_arithmetic": "Fraction; no floating point",
        "two_sided_inverse_verified": True,
        "differentiated_inverse_verified": True,
        "uniform_subpower_bound_is_symbolic_theorem": True,
        "full_native_gamma_diagonal_adapter_asserted": False,
        "off_phase_blocks_bounded_here": False,
        "RH_conclusion": False,
    }
    result["proof_object_sha256"] = sha256(canonical(result).encode()).hexdigest()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    result = build()
    if args.write:
        FIXTURE.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
    else:
        require(FIXTURE.stat().st_size <= MAX_BYTES, "artifact cap")
        candidate = json.loads(FIXTURE.read_text(encoding="utf-8"))
        require(canonical(candidate) == canonical(result), "exact canonical replay")
    print(
        json.dumps(
            {"status": "PASS", "proof_object_sha256": result["proof_object_sha256"]}
        )
    )


if __name__ == "__main__":
    main()
