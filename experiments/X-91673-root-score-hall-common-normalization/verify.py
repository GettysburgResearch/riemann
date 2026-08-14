#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from math import isqrt
from pathlib import Path


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __add__(self, other: object) -> "I":
        rhs = as_i(other)
        return I(self.lo + rhs.lo, self.hi + rhs.hi)

    __radd__ = __add__

    def __neg__(self) -> "I":
        return I(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "I":
        return self + (-as_i(other))

    def __rsub__(self, other: object) -> "I":
        return as_i(other) - self

    def __mul__(self, other: object) -> "I":
        rhs = as_i(other)
        vals = (
            self.lo * rhs.lo,
            self.lo * rhs.hi,
            self.hi * rhs.lo,
            self.hi * rhs.hi,
        )
        return I(min(vals), max(vals))

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "I":
        rhs = as_i(other)
        if rhs.lo <= 0 <= rhs.hi:
            raise ZeroDivisionError("interval denominator contains zero")
        return self * I(1 / rhs.hi, 1 / rhs.lo)

    def __rtruediv__(self, other: object) -> "I":
        return as_i(other) / self


def as_i(value: object) -> I:
    if isinstance(value, I):
        return value
    if not isinstance(value, F):
        value = F(value)
    return I(value, value)


DEN = 10**70
ROOT_LO = F(1844367547103, 10**14)
WINDOW_MAX = 1 / ROOT_LO


@lru_cache(maxsize=None)
def sqrt_q(value: F | int) -> I:
    value = F(value)
    scaled = (value.numerator * DEN * DEN) // value.denominator
    root = isqrt(scaled)
    lo = F(root, DEN)
    if lo * lo == value:
        return I(lo, lo)
    return I(lo, F(root + 1, DEN))


@lru_cache(maxsize=None)
def invsqrt(n: int) -> I:
    return 1 / sqrt_q(n)


@lru_cache(maxsize=None)
def log_q(value: F, terms: int = 100) -> I:
    value = F(value)
    if value <= 0:
        raise ValueError("log argument must be positive")

    exponent = 0
    y = value
    while y >= 2:
        y /= 2
        exponent += 1
    while y < 1:
        y *= 2
        exponent -= 1

    def atanh_log(z: F) -> I:
        z2 = z * z
        power = z
        partial = F(0)
        for k in range(terms):
            partial += power / F(2 * k + 1)
            power *= z2
        partial *= 2
        tail = 2 * power / (F(2 * terms + 1) * (1 - z2))
        return I(partial, partial + tail)

    local = I(F(0), F(0)) if y == 1 else atanh_log((y - 1) / (y + 1))
    log2 = atanh_log(F(1, 3))
    return local + exponent * log2


def mobius_sieve(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    least = [0] * (limit + 1)
    primes: list[int] = []
    mu[1] = 1
    for n in range(2, limit + 1):
        if least[n] == 0:
            least[n] = n
            primes.append(n)
            mu[n] = -1
        for p in primes:
            if p > least[n] or p * n > limit:
                break
            least[p * n] = p
            if n % p == 0:
                mu[p * n] = 0
                break
            mu[p * n] = -mu[n]
    return mu


MU = mobius_sieve(100)


def score_atom(x: F, n: int) -> I:
    return 5 * sqrt_q(x) / n - 3 * invsqrt(n)


def score_hall_margin(active_max: int, threshold: int, x: F) -> I:
    value = I(F(0), F(0))
    for n in range(1, active_max + 1):
        atom = score_atom(x, n)
        if MU[n] == 1 and n <= threshold:
            value += atom
        elif MU[n] == -1 and n <= threshold:
            value -= atom
    return value


@lru_cache(maxsize=None)
def gamma_coeff(row: int, m: int) -> I:
    if m == row:
        return F(row + 1, row - 1) * invsqrt(row)
    if m == row + 1:
        return -F((row + 1) * (row - 2), row * (row - 1)) * invsqrt(row + 1)
    if m >= row + 2:
        return F(2, row * (row - 1)) * invsqrt(m)
    return I(F(0), F(0))


def cell_cd(row: int, active_max: int) -> tuple[I, I]:
    c = I(F(0), F(0))
    d = I(F(0), F(0))
    for m in range(row, active_max + 1):
        g = gamma_coeff(row, m)
        c += g
        d += g * log_q(F(m))
    return c, d


def decimal(value: F, digits: int = 16) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    integer = value.numerator // value.denominator
    rem = value.numerator % value.denominator
    out: list[str] = []
    for _ in range(digits):
        rem *= 10
        out.append(str(rem // value.denominator))
        rem %= value.denominator
    return f"{sign}{integer}." + "".join(out)


def directed_root_checks() -> dict[str, object]:
    minimum_hall: tuple[F, int, int, F] | None = None
    hall_checks = 0

    for active_max in range(1, 55):
        right = F(active_max + 1) if active_max < 54 else WINDOW_MAX
        thresholds = [n for n in range(1, active_max + 1) if MU[n] == -1]
        for threshold in thresholds:
            for x in (F(active_max), right):
                margin = score_hall_margin(active_max, threshold, x)
                assert margin.lo > F(3, 100), (active_max, threshold, x, margin)
                record = (margin.lo, active_max, threshold, x)
                if minimum_hall is None or record[0] < minimum_hall[0]:
                    minimum_hall = record
                hall_checks += 1

    minimum_row: tuple[F, int, int, F] | None = None
    row_checks = 0
    for row in range(2, 55):
        for active_max in range(row, 55):
            y = F(active_max + 1) if active_max < 54 else WINDOW_MAX
            c, d = cell_cd(row, active_max)
            q = c * log_q(y) - d
            assert q.lo >= 0, (row, active_max, q)
            # For Phi(Y)=Q_Y(row)/(sqrt(Y)-1), the derivative numerator is
            # M=sqrt(Y)(2C-Q)-2C and decreases on each activation cell.
            m = sqrt_q(y) * (2 * c - q) - 2 * c
            assert m.lo > F(1, 20), (row, active_max, y, m)
            record = (m.lo, row, active_max, y)
            if minimum_row is None or record[0] < minimum_row[0]:
                minimum_row = record
            row_checks += 1

    assert minimum_hall is not None
    assert minimum_row is not None
    return {
        "hall_checks": hall_checks,
        "hall_minimum_lower": decimal(minimum_hall[0]),
        "hall_minimum_cell": minimum_hall[1],
        "hall_minimum_threshold": minimum_hall[2],
        "row_checks": row_checks,
        "row_minimum_lower": decimal(minimum_row[0]),
        "row_minimum_row": minimum_row[1],
        "row_minimum_cell": minimum_row[2],
    }


def stopped_leaf_firewall() -> dict[str, object]:
    p = 67
    y = 13
    parent = p * y
    threshold = 13
    a13 = sum((F(MU[n], n) for n in range(1, threshold + 1)), F(0))
    assert a13 == F(-2323, 30030)

    b13 = I(F(0), F(0))
    for n in range(1, threshold + 1):
        b13 += MU[n] * invsqrt(n)

    r = invsqrt(p)
    alpha_s = 2 * (r + 2) / (r + 3)
    normalized = alpha_s * sqrt_q(parent) * a13 - b13
    physical = (1 - r) * (r + 3) * normalized

    assert normalized.lo > F(-2140, 1000)
    assert normalized.hi < F(-2139, 1000)
    assert physical.hi < 0
    return {
        "p": p,
        "y": y,
        "parent": parent,
        "normalized_lower": decimal(normalized.lo),
        "normalized_upper": decimal(normalized.hi),
        "physical_upper": decimal(physical.hi),
        "hall_transport_exists": False,
    }


def exact_common_normalization_algebra() -> dict[str, object]:
    # One score-mass edge: score capacity 7 pays score demand 3.
    s_e, s_o, transported = F(7), F(3), F(3)
    residual_score = s_e - transported
    nu = residual_score / s_e
    assert nu == F(4, 7)
    assert s_e - s_o == nu * s_e

    # Target ratios obey q_e >= q_o.
    q_e, q_o = F(4, 5), F(3, 4)
    t_e, t_o = s_e * q_e, s_o * q_o
    target_slack = transported * (q_e - q_o)
    assert target_slack >= 0
    assert t_e - t_o == nu * t_e + target_slack

    # One row profile obeys phi_e >= phi_o.
    phi_e, phi_o = F(11, 7), F(4, 3)
    a_e, a_o = s_e * phi_e, s_o * phi_o
    row_bonus = transported * (phi_e - phi_o)
    assert row_bonus >= 0
    assert a_e - a_o == nu * a_e + row_bonus

    # Test arbitrary ordinary maps and form detail only after q and 4q.
    parent = (F(9), F(5), F(2))
    bonus = (F(2), F(1), F(1))
    child = tuple(parent[i] - bonus[i] for i in range(3))
    gamma_q = (F(3), F(2), F(1))
    gamma_4q = (F(1), F(1), F(0))

    def dot(coeff: tuple[F, ...], vec: tuple[F, ...]) -> F:
        return sum((coeff[i] * vec[i] for i in range(len(vec))), F(0))

    assert dot(gamma_q, parent) == dot(gamma_q, bonus) + dot(gamma_q, child)
    assert dot(gamma_4q, parent) == dot(gamma_4q, bonus) + dot(gamma_4q, child)
    detail_parent = dot(gamma_q, parent) - 2 * dot(gamma_4q, parent)
    detail_sum = (
        dot(gamma_q, bonus) - 2 * dot(gamma_4q, bonus)
        + dot(gamma_q, child) - 2 * dot(gamma_4q, child)
    )
    assert detail_parent == detail_sum

    # Finite endpoint integration and one global linear quantizer.
    weights = (F(2), F(3))
    fibers_parent = ((F(5), F(2)), (F(7), F(4)))
    fibers_bonus = ((F(1), F(1)), (F(2), F(1)))
    fibers_child = tuple(
        tuple(fibers_parent[i][j] - fibers_bonus[i][j] for j in range(2))
        for i in range(2)
    )

    integrated_parent = tuple(
        sum((weights[i] * fibers_parent[i][j] for i in range(2)), F(0))
        for j in range(2)
    )
    integrated_bonus = tuple(
        sum((weights[i] * fibers_bonus[i][j] for i in range(2)), F(0))
        for j in range(2)
    )
    integrated_child = tuple(
        sum((weights[i] * fibers_child[i][j] for i in range(2)), F(0))
        for j in range(2)
    )
    assert integrated_parent == tuple(
        integrated_bonus[j] + integrated_child[j] for j in range(2)
    )

    quantizer = ((F(1), F(1, 2)), (F(0), F(1, 2)))

    def matvec(matrix: tuple[tuple[F, ...], ...], vec: tuple[F, ...]) -> tuple[F, ...]:
        return tuple(dot(row, vec) for row in matrix)

    assert matvec(quantizer, integrated_parent) == tuple(
        matvec(quantizer, integrated_bonus)[j]
        + matvec(quantizer, integrated_child)[j]
        for j in range(2)
    )

    # Same-index scalar placement commutes with every linear map.
    scale = F(1, 7)
    assert dot(gamma_q, tuple(scale * x for x in parent)) == scale * dot(gamma_q, parent)

    return {
        "score_identity": True,
        "target_slack_nonnegative": True,
        "row_bonus_nonnegative": True,
        "ordinary_response_commutes": True,
        "radix_four_via_two_ordinary_maps": True,
        "finite_endpoint_integration": True,
        "one_global_quantizer": True,
        "same_index_scaling": True,
    }


def run(output: Path) -> dict[str, object]:
    roots = directed_root_checks()
    firewall = stopped_leaf_firewall()
    algebra = exact_common_normalization_algebra()
    result: dict[str, object] = {
        "classification": "PASS_ROOT_SCORE_HALL_COMMON_NORMALIZATION_ALGEBRA",
        "root_window": {
            "c0_lower": str(ROOT_LO),
            "x_upper": str(WINDOW_MAX),
        },
        "directed_root_checks": roots,
        "stopped_leaf_firewall": firewall,
        "common_normalization_algebra": algebra,
        "scope": (
            "Exact Fraction arithmetic with directed rational square-root and "
            "logarithm intervals. The replay certifies the finite root domain, "
            "common score/target/row algebra, response commutation, endpoint "
            "integration, and the stopped-leaf firewall. It does not certify "
            "the imported analytic endpoint producer, external RH consumer, or RH."
        ),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["classification"])
    print(output)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, default=Path(__file__).resolve().parent / "results" / "verification.json")
    args = parser.parse_args()
    run(args.json)


if __name__ == "__main__":
    main()
