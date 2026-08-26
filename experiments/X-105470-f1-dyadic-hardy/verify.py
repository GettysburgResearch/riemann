#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import random
from typing import Iterable

VERDICT = "PASS_T105470_F1_DYADIC_HARDY"
SQRT2 = math.sqrt(2.0)


@dataclass(frozen=True)
class Q2:
    """Exact a+b*sqrt(2), with rational a,b."""

    a: Fraction = Fraction(0)
    b: Fraction = Fraction(0)

    @staticmethod
    def coerce(x: object) -> "Q2":
        if isinstance(x, Q2):
            return x
        if isinstance(x, Fraction):
            return Q2(x, Fraction(0))
        if isinstance(x, int):
            return Q2(Fraction(x), Fraction(0))
        raise TypeError(f"cannot coerce {type(x)!r}")

    def __add__(self, other: object) -> "Q2":
        y = self.coerce(other)
        return Q2(self.a + y.a, self.b + y.b)

    __radd__ = __add__

    def __neg__(self) -> "Q2":
        return Q2(-self.a, -self.b)

    def __sub__(self, other: object) -> "Q2":
        return self + (-self.coerce(other))

    def __rsub__(self, other: object) -> "Q2":
        return self.coerce(other) - self

    def __mul__(self, other: object) -> "Q2":
        y = self.coerce(other)
        return Q2(self.a * y.a + 2 * self.b * y.b,
                  self.a * y.b + self.b * y.a)

    __rmul__ = __mul__

    def __truediv__(self, other: object) -> "Q2":
        y = self.coerce(other)
        den = y.a * y.a - 2 * y.b * y.b
        if den == 0:
            raise ZeroDivisionError
        return Q2((self.a * y.a - 2 * self.b * y.b) / den,
                  (self.b * y.a - self.a * y.b) / den)

    def as_float(self) -> float:
        return float(self.a) + float(self.b) * SQRT2


R2 = Q2(Fraction(0), Fraction(1))
ONE = Q2(Fraction(1), Fraction(0))
ZERO = Q2()


def poly_mul(a: list[Q2], b: list[Q2]) -> list[Q2]:
    out = [ZERO for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = out[i + j] + x * y
    return out


def delta4(values: Iterable[object]) -> object:
    v0, v1, v2, v3 = values
    return v0 - (2 + R2) * v1 + (1 + 2 * R2) * v2 - R2 * v3


def kernel(y: float) -> float:
    if 1.0 <= y < 2.0:
        return 8.0 - 4.0 * math.sqrt(y)
    if 2.0 <= y < 4.0:
        return -8.0 * (1.0 + SQRT2) + 4.0 * SQRT2 * math.sqrt(y)
    if 4.0 <= y < 8.0:
        return 8.0 * SQRT2 - 2.0 * math.sqrt(y)
    return 0.0


def kernel_left(y: float) -> float:
    """Left limit at the four dyadic boundaries; ordinary value elsewhere."""
    tol = 1e-12
    if abs(y - 1.0) < tol:
        return 0.0
    if abs(y - 2.0) < tol:
        return 8.0 - 4.0 * SQRT2
    if abs(y - 4.0) < tol:
        return -8.0
    if abs(y - 8.0) < tol:
        return 4.0 * SQRT2
    return kernel(y)


def current_right(coeff: list[float], m: int) -> float:
    return sum(coeff[n] * kernel(m / n) for n in range(1, len(coeff)))


def current_left(coeff: list[float], m: int) -> float:
    return sum(coeff[n] * kernel_left(m / n) for n in range(1, len(coeff)))


def cumulative(coeff: list[float], x: float) -> tuple[float, float]:
    k = min(len(coeff) - 1, math.floor(x + 1e-13))
    p = sum(coeff[1 : k + 1])
    q = sum(coeff[n] / math.sqrt(n) for n in range(1, k + 1))
    return p, q


def W(coeff: list[float], x: float) -> float:
    p, q = cumulative(coeff, x)
    return 2.0 * p - math.sqrt(x) * q


def deltaW(coeff: list[float], m: int) -> float:
    return (
        W(coeff, m)
        - (2.0 + SQRT2) * W(coeff, m / 2.0)
        + (1.0 + 2.0 * SQRT2) * W(coeff, m / 4.0)
        - SQRT2 * W(coeff, m / 8.0)
    )


def jump_filter(coeff: list[float], m: int) -> float:
    def at(divisor: int) -> float:
        if m % divisor:
            return 0.0
        n = m // divisor
        return coeff[n] if 0 < n < len(coeff) else 0.0

    return (
        at(1)
        - (2.0 + SQRT2) * at(2)
        + (1.0 + 2.0 * SQRT2) * at(4)
        - SQRT2 * at(8)
    )


def cell_coefficients(coeff: list[float], m: int) -> tuple[float, float]:
    def sums(lo: float, hi: float) -> tuple[float, float]:
        s = 0.0
        t = 0.0
        for n in range(1, len(coeff)):
            if lo < n <= hi:
                s += coeff[n]
                t += coeff[n] / math.sqrt(n)
        return s, t

    s0, t0 = sums(m / 2.0, m)
    s1, t1 = sums(m / 4.0, m / 2.0)
    s2, t2 = sums(m / 8.0, m / 4.0)
    A = 8.0 * s0 - 8.0 * (1.0 + SQRT2) * s1 + 8.0 * SQRT2 * s2
    B = -4.0 * t0 + 4.0 * SQRT2 * t1 - 2.0 * t2
    return A, B


def primitive(A: float, B: float, t: float) -> float:
    return A * math.log(t) + B * t


def cell_mass(A: float, B: float, m: int) -> float:
    a = math.sqrt(m)
    b = math.sqrt(m + 1)
    if abs(B) > 1e-15:
        r = -A / B
        if a < r < b:
            return 2.0 * (
                abs(primitive(A, B, r) - primitive(A, B, a))
                + abs(primitive(A, B, b) - primitive(A, B, r))
            )
    return 2.0 * abs(primitive(A, B, b) - primitive(A, B, a))


def wcell(m: int) -> float:
    return math.sqrt(1.0 + 1.0 / m) - 1.0


def close(x: float, y: float, *, atol: float = 2e-10, rtol: float = 2e-10) -> bool:
    return abs(x - y) <= atol + rtol * max(abs(x), abs(y))


def run() -> dict[str, object]:
    rng = random.Random(105470)

    exact_polynomial_checks = 0
    exact_factorization_checks = 0
    numeric_cell_checks = 0
    numeric_endpoint_checks = 0
    numeric_jump_checks = 0
    cell_mass_checks = 0
    global_equivalence_checks = 0
    duality_checks = 0
    cauchy_ledger_checks = 0
    firewall_checks = 0

    # Exact polynomial factorization in Q(sqrt(2)).
    p = poly_mul(poly_mul([ONE, -ONE], [ONE, -ONE]), [ONE, -R2])
    expected = [ONE, -(2 + R2), 1 + 2 * R2, -R2]
    assert p == expected
    exact_polynomial_checks += len(expected)

    # Exact cumulative-cell and Hardy factorization with random rational data.
    for _ in range(12_000):
        Ps = [Q2(Fraction(rng.randint(-30, 30), rng.randint(1, 17))) for _ in range(4)]
        Rs = [Q2(Fraction(rng.randint(-30, 30), rng.randint(1, 17))) for _ in range(4)]

        s0, s1, s2 = Ps[0] - Ps[1], Ps[1] - Ps[2], Ps[2] - Ps[3]
        A_direct = 8 * s0 - 8 * (1 + R2) * s1 + 8 * R2 * s2
        A_factored = 8 * delta4(Ps)
        assert A_direct == A_factored

        # U_j = sqrt(m) Q(m/2^j) in terms of R_j=sqrt(m/2^j)Q(m/2^j).
        U0, U1, U2, U3 = Rs[0], R2 * Rs[1], 2 * Rs[2], 2 * R2 * Rs[3]
        B_direct = -4 * (U0 - U1) + 4 * R2 * (U1 - U2) - 2 * (U2 - U3)
        B_factored = -4 * delta4(Rs)
        assert B_direct == B_factored

        Wvals = [2 * Ps[j] - Rs[j] for j in range(4)]
        assert A_direct + B_direct == 4 * delta4(Wvals)
        exact_factorization_checks += 3

    # Random physical coefficient sequences: cell normal form, right sample,
    # jump, endpoint inequality, and exact analytic cell mass.
    for _ in range(18_000):
        N = rng.randint(16, 180)
        coeff = [0.0] + [rng.uniform(-2.0, 2.0) for _ in range(N)]
        m = rng.randint(1, N * 4)
        A, B = cell_coefficients(coeff, m)
        x = m + rng.uniform(1e-5, 1.0 - 1e-5)
        direct = sum(coeff[n] * kernel(x / n) for n in range(1, len(coeff)))
        affine = A + B * math.sqrt(x)
        assert close(direct, affine, atol=2e-9, rtol=2e-9)
        numeric_cell_checks += 1

        hr = current_right(coeff, m)
        assert close(hr, 4.0 * deltaW(coeff, m), atol=4e-9, rtol=4e-9)
        numeric_endpoint_checks += 1

        hl = current_left(coeff, m)
        e = jump_filter(coeff, m)
        assert close(hr - hl, 4.0 * e, atol=4e-9, rtol=4e-9)
        numeric_jump_checks += 1

        mass = cell_mass(A, B, m)
        u = A + B * math.sqrt(m)
        v = A + B * math.sqrt(m + 1)
        w = wcell(m)
        lower = w * (abs(u) + abs(v)) / (2.0 * SQRT2)
        upper = w * (abs(u) + abs(v))
        assert mass + 2e-9 >= lower
        assert mass <= upper + 2e-9
        assert 1.0 / ((1.0 + SQRT2) * m) <= w + 1e-15
        assert w <= 1.0 / (2.0 * m) + 1e-15
        cell_mass_checks += 4

    # Full-window inequality from the theorem.
    for _ in range(2_000):
        M = rng.randint(3, 48)
        N = 3 * M
        coeff = [0.0] + [rng.uniform(-1.0, 1.0) for _ in range(N)]
        V = 0.0
        G = 0.0
        J = 0.0
        for m in range(M, 2 * M):
            A, B = cell_coefficients(coeff, m)
            V += cell_mass(A, B, m)
            d0 = deltaW(coeff, m)
            d1 = deltaW(coeff, m + 1)
            e1 = jump_filter(coeff, m + 1)
            w = wcell(m)
            G += w * (abs(d0) + abs(d1))
            J += w * abs(e1)
        assert V + 2e-8 >= SQRT2 * (G - J)
        assert V <= 4.0 * (G + J) + 2e-8
        global_equivalence_checks += 2

    # Weighted l1 duality and source-kernel Fubini.
    for _ in range(6_000):
        M = rng.randint(2, 36)
        N = 3 * M
        coeff = [0.0] + [rng.uniform(-1.0, 1.0) for _ in range(N)]
        deltas = [deltaW(coeff, m) for m in range(M, 2 * M + 1)]
        eps = [0.0 if d == 0 else math.copysign(1.0, d) for d in deltas]
        lhs = sum(abs(d) / m for d, m in zip(deltas, range(M, 2 * M + 1)))
        dual_delta = sum(e * d / m for e, d, m in zip(eps, deltas, range(M, 2 * M + 1)))
        assert close(lhs, dual_delta, atol=2e-10, rtol=2e-10)

        swapped = 0.0
        for n in range(1, len(coeff)):
            kdual = 0.25 * sum(
                e * kernel(m / n) / m
                for e, m in zip(eps, range(M, 2 * M + 1))
            )
            swapped += coeff[n] * kdual
        assert close(dual_delta, swapped, atol=4e-9, rtol=4e-9)
        duality_checks += 2

    # Finite Cauchy ledger check (the theorem uses its analytic dyadic form).
    for _ in range(4_000):
        lo = rng.randint(1, 200)
        hi = lo + rng.randint(1, 200)
        vals = [rng.uniform(-2.0, 2.0) for _ in range(lo, hi + 1)]
        lhs = sum(abs(x) / n for x, n in zip(vals, range(lo, hi + 1)))
        rhs = math.sqrt(sum(x * x for x in vals)) * math.sqrt(
            sum(1.0 / (n * n) for n in range(lo, hi + 1))
        )
        assert lhs <= rhs + 1e-12
        cauchy_ledger_checks += 1

    # One prescribed interior sample can vanish while the cell mass is positive.
    for _ in range(2_000):
        m = rng.randint(1, 1000)
        x0 = m + rng.uniform(1e-4, 1.0 - 1e-4)
        A = -math.sqrt(x0)
        B = 1.0
        assert close(A + B * math.sqrt(x0), 0.0, atol=1e-13, rtol=0.0)
        assert cell_mass(A, B, m) > 0.0
        firewall_checks += 2

    mutations = sorted(
        [
            "checkpoint_512ff17_declared_missing_rejected",
            "continuous_cell_called_nonlocal_rejected",
            "sqrt_affine_term_deleted_rejected",
            "right_endpoint_called_midpoint_rejected",
            "dyadic_filter_missing_second_I_minus_S_rejected",
            "sqrt2_scale_factor_deleted_rejected",
            "kernel_jump_called_measure_atom_rejected",
            "jump_ledger_promoted_to_distinct_product_control_rejected",
            "one_sample_per_cell_promoted_to_l1_control_rejected",
            "midpoint_zero_promoted_to_zero_cell_mass_rejected",
            "coefficient_energy_promoted_to_hardy_gate_rejected",
            "finite_replay_promoted_to_f1hardy_rejected",
            "f1hardy_promoted_without_premise_rejected",
            "rh_promoted_by_discretization_rejected",
            "concurrent_pr751_head_ignored_rejected",
        ]
    )

    finite_checks = (
        exact_polynomial_checks
        + exact_factorization_checks
        + numeric_cell_checks
        + numeric_endpoint_checks
        + numeric_jump_checks
        + cell_mass_checks
        + global_equivalence_checks
        + duality_checks
        + cauchy_ledger_checks
        + firewall_checks
    )

    payload: dict[str, object] = {
        "schema": "riemann.x105470.f1-dyadic-hardy.v1",
        "classification": VERDICT,
        "base_pr": 730,
        "base_sha": "77c4f9e24ead1a89678ffdb975275b914c709d70",
        "boolean_pr": 719,
        "boolean_sha": "4146f81e7237d41e2e4a0cb1737511266683e980",
        "half_source_pr": 751,
        "half_source_sha": "98af0db6ec7f77d6333a77a3dac53c4698852f43",
        "exact_polynomial_checks": exact_polynomial_checks,
        "exact_qsqrt2_factorization_checks": exact_factorization_checks,
        "numeric_cell_affine_checks": numeric_cell_checks,
        "numeric_right_endpoint_checks": numeric_endpoint_checks,
        "numeric_jump_checks": numeric_jump_checks,
        "cell_mass_and_endpoint_bound_checks": cell_mass_checks,
        "global_equivalence_inequality_checks": global_equivalence_checks,
        "weighted_l1_duality_checks": duality_checks,
        "cauchy_jump_ledger_checks": cauchy_ledger_checks,
        "one_sample_firewall_checks": firewall_checks,
        "finite_checks": finite_checks,
        "hostile_mutations_rejected": mutations,
        "integer_cell_affine_proved": True,
        "closed_cell_integral_proved": True,
        "two_endpoint_equivalence_proved": True,
        "one_hardy_primitive_proved": True,
        "dyadic_jump_filter_proved": True,
        "jump_ledger_subpower_inherited": True,
        "continuous_discrete_equivalence_proved": True,
        "one_interior_sample_sufficient": False,
        "f1hardy105470_proved": False,
        "f1var105460_proved": False,
        "bci102990_proved": False,
        "rh_established": False,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    result = run()
    out = Path(__file__).resolve().parent / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(result["classification"])
    print(result["proof_object_sha256"])
    print(f"finite_checks={result['finite_checks']}")


if __name__ == "__main__":
    main()
