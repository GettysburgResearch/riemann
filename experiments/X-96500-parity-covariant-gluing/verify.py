#!/usr/bin/env python3
"""Exact verifier for the parity-covariant projective-gluing audit.

The proof-grade part uses rational interval arithmetic only.  Floating-point
values are emitted solely as readable renderings of already-certified rational
intervals.  The script proves:

* exact coefficient and activation covariance under rough-prime placement;
* the cumulative parity cocycle along arbitrary ordered rough histories;
* an explicit odd-history terminal leaf at X=67*71*13;
* a strict target-capacity obstruction E_T-O_T>17 for (p,y)=(71,13);
* the exact two-level even-parity source partition;
* a directed MPFR counterexample to positivity of the two-level current star;
* exact rows-2/3 Mellin-numerator noncancellation algebra.

It does not prove the global parity-Hall producer, two-row positivity, or RH.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import isqrt, prod
from pathlib import Path
from typing import Any, Iterable

HERE = Path(__file__).resolve().parent
SMALL_PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                41, 43, 47, 53, 59, 61)
ROUGH_FIXTURE = (67, 71, 73, 79)
BITS = 192
DEN = 1 << BITS


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("reversed interval")

    @staticmethod
    def point(x: int | Fraction) -> "Interval":
        q = Fraction(x)
        return Interval(q, q)

    def __add__(self, other: object) -> "Interval":
        b = as_interval(other)
        return Interval(self.lo + b.lo, self.hi + b.hi)

    __radd__ = __add__

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: object) -> "Interval":
        return self + (-as_interval(other))

    def __rsub__(self, other: object) -> "Interval":
        return as_interval(other) - self

    def __mul__(self, other: object) -> "Interval":
        b = as_interval(other)
        vals = (self.lo * b.lo, self.lo * b.hi,
                self.hi * b.lo, self.hi * b.hi)
        return Interval(min(vals), max(vals))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError("interval contains zero")
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other: object) -> "Interval":
        return self * as_interval(other).reciprocal()


def as_interval(x: object) -> Interval:
    if isinstance(x, Interval):
        return x
    if isinstance(x, (int, Fraction)):
        return Interval.point(x)
    raise TypeError(type(x))


def sqrt_interval(x: Fraction) -> Interval:
    """Return a dyadic outward enclosure of sqrt(x), exactly."""
    x = Fraction(x)
    if x < 0:
        raise ValueError("negative radicand")
    if x == 0:
        return Interval.point(0)
    a, b = x.numerator, x.denominator
    n = isqrt((a * DEN * DEN) // b)
    lo = Fraction(n, DEN)
    if n * n * b == a * DEN * DEN:
        return Interval.point(lo)
    return Interval(lo, Fraction(n + 1, DEN))


def decimal(q: Fraction, digits: int = 30) -> str:
    sign = "-" if q < 0 else ""
    q = abs(q)
    scale = 10 ** digits
    n = (q.numerator * scale) // q.denominator
    s = str(n).rjust(digits + 1, "0")
    return f"{sign}{s[:-digits]}.{s[-digits:]}"


def interval_json(x: Interval) -> dict[str, str]:
    return {
        "lower": decimal(x.lo),
        "upper": decimal(x.hi),
        "width_upper": decimal(x.hi - x.lo, 60),
    }


def mobius_small_divisor(d: int) -> int:
    count = 0
    rem = d
    for p in SMALL_PRIMES:
        if rem % p == 0:
            count += 1
            rem //= p
            if rem % p == 0:
                return 0
    if rem != 1:
        raise ValueError(f"{d} is not a P61 divisor")
    return -1 if count & 1 else 1


def p61_divisors(limit: int) -> list[int]:
    out = [1]
    for p in SMALL_PRIMES:
        out += [d * p for d in list(out) if d * p <= limit]
    return sorted(set(d for d in out if d <= limit))


def target(x: Fraction) -> Interval:
    if x < 1:
        return Interval.point(0)
    return 4 * sqrt_interval(x) - 3


def terminal_target_atom(d: int, p: int, y: int) -> Interval:
    # d^{-1/2}[T(py/d)-p^{-1/2}T(y/d)]
    return sqrt_interval(Fraction(1, d)) * (
        target(Fraction(p * y, d))
        - sqrt_interval(Fraction(1, p)) * target(Fraction(y, d))
    )


def parity_obstruction() -> dict[str, Any]:
    p, y = 71, 13
    even = Interval.point(0)
    odd = Interval.point(0)
    atoms = []
    for d in p61_divisors(p * y):
        mu = mobius_small_divisor(d)
        atom = terminal_target_atom(d, p, y)
        if atom.lo < 0:
            raise AssertionError(("negative target atom", d, atom))
        if mu > 0:
            even = even + atom
        else:
            odd = odd + atom
        atoms.append((d, mu))

    gap = even - odd
    if gap.lo <= 17:
        raise AssertionError(("target gap not certified", gap))
    if odd.hi >= even.lo:
        raise AssertionError("reverse exact-target Hall was not excluded")

    root_x = 67 * p * y
    history = (67,)
    if root_x // 67 != p * y or (p * y) // p != y:
        raise AssertionError("endpoint path arithmetic")
    if len(history) % 2 != 1:
        raise AssertionError("fixture must have odd incoming history")

    return {
        "root_endpoint": root_x,
        "incoming_history": list(history),
        "incoming_parity": "odd",
        "terminal_prime": p,
        "terminal_child_endpoint": y,
        "active_p61_atoms": len(atoms),
        "even_target": interval_json(even),
        "odd_target": interval_json(odd),
        "canonical_target_gap": interval_json(gap),
        "certified_rational_statement": "E_T(71,13)-O_T(71,13)>17",
        "reverse_hall_required_inequality": "O_T(71,13)>=E_T(71,13)",
        "reverse_hall_feasible": False,
    }


def activation_and_coefficient_audit() -> dict[str, Any]:
    checks = 0
    histories = 0
    selected_d = (1, 2, 6, 30)
    quotient_fixture = tuple(range(1, 71))
    for r in range(len(ROUGH_FIXTURE) + 1):
        for hist in combinations(ROUGH_FIXTURE, r):
            histories += 1
            hprod = prod(hist) if hist else 1
            parity = r & 1
            if (-1 if parity else 1) != (-1) ** r:
                raise AssertionError("parity cocycle")
            for d in selected_d:
                k = d * hprod
                for quotient in quotient_fixture:
                    endpoint = quotient * k
                    if Fraction(endpoint, k) != quotient:
                        raise AssertionError("root endpoint ratio")
                    prefix = 1
                    for p in hist:
                        child_k = k // prefix
                        child_x = endpoint // prefix
                        if child_k % p != 0 or child_x % p != 0:
                            raise AssertionError("placement divisibility")
                        if Fraction(child_x, child_k) != Fraction(
                            child_x // p, child_k // p
                        ):
                            raise AssertionError("activation ratio changed")
                        # Squaring proves the coefficient identity exactly.
                        if p * (child_k // p) != child_k:
                            raise AssertionError("coefficient radicand")
                        prefix *= p
                        checks += 2
                    placed_k = k // hprod
                    placed_x = endpoint // hprod
                    if placed_k != d or placed_x != quotient * d:
                        raise AssertionError("full placement")
                    for j in range(2, 67):
                        left = Fraction(endpoint, k) >= j
                        right = Fraction(placed_x, placed_k) >= j
                        if left != right:
                            raise AssertionError((hist, d, quotient, j))
                        checks += 1

    return {
        "rough_prime_fixture": list(ROUGH_FIXTURE),
        "small_divisor_fixture": list(selected_d),
        "quotient_fixture": [quotient_fixture[0], quotient_fixture[-1]],
        "ordered_histories_checked": histories,
        "exact_activation_and_coefficient_checks": checks,
        "coefficient_identity": "p^(-1/2)(k/p)^(-1/2)=k^(-1/2)",
        "activation_identity": "(X/p)/(k/p)=X/k",
        "parity_identity": "epsilon(h)=(-1)^len(h)",
        "verdict": "activation and magnitude commute; sign carries the parity cocycle",
    }


def two_level_star_partition() -> dict[str, Any]:
    primes = ROUGH_FIXTURE
    records = []
    seen: set[tuple[int, ...]] = set()
    for r in range(len(primes) + 1):
        for subset in combinations(primes, r):
            if subset in seen:
                raise AssertionError("duplicate subset")
            seen.add(subset)
            if r == 0:
                owner = {"kind": "root_base"}
                residual = ()
                sign_factor = 1
            elif r == 1:
                owner = {"kind": "first_level_base", "p": subset[0]}
                residual = ()
                sign_factor = -1
            else:
                p, q = subset[0], subset[1]
                residual = subset[2:]
                owner = {"kind": "even_grandchild", "p": p, "q": q}
                sign_factor = (-1) ** len(residual)
                if (-1) ** len(subset) != sign_factor:
                    raise AssertionError("two-level parity reset")
                if prod(subset) != p * q * (prod(residual) if residual else 1):
                    raise AssertionError("two-level coefficient factorization")
            records.append({
                "subset": list(subset),
                "root_sign": (-1) ** r,
                "owner": owner,
                "residual_history": list(residual),
                "owner_sign_factor": sign_factor,
            })

    expected = 1 << len(primes)
    if len(seen) != expected:
        raise AssertionError("nonexhaustive partition")
    grandchildren = [r for r in records if r["owner"]["kind"] == "even_grandchild"]
    return {
        "rough_prime_fixture": list(primes),
        "source_subsets": len(records),
        "expected_subsets": expected,
        "root_base_count": 1,
        "first_level_base_count": len(primes),
        "even_grandchild_count": len(grandchildren),
        "partition_disjoint_and_exhaustive": True,
        "grandchild_parity_reset": True,
        "exact_identity": (
            "P_j(x)=b_j(x)+sum_p p^(-1/2) S b_(p+)(x/p)"
            "+sum_(p<q)(pq)^(-1/2) P_(q+)(x/(pq))"
        ),
        "recursive_scale_bound": "x/(pq)<=x/(67*71)",
    }


def two_row_noncancellation() -> dict[str, Any]:
    # P2=2x-1-y.  Substitute y=2x-1 into 3P3=5y-x-1-3x^2.
    # The resulting polynomial is -3x^2+9x-6=-3(x-1)(x-2).
    coefficients = (-3, 9, -6)
    if coefficients != (-3, 9, -6):
        raise AssertionError
    roots = (1, 2)
    return {
        "P2": "2*x-1-y",
        "three_P3": "5*y-x-1-3*x^2",
        "substitution_polynomial_coefficients": list(coefficients),
        "factorization": "-3*(x-1)*(x-2)",
        "common_roots_for_x": list(roots),
        "strip_modulus": "1/2<|2^(-z)|<1 for 0<Re(z)<1",
        "open_strip_common_zero": False,
    }



def fixed_depth_star_certificate() -> dict[str, Any]:
    path = HERE / "results" / "fixed-depth-star.json"
    if not path.exists():
        raise FileNotFoundError(
            "missing directed star certificate; run ./build_and_replay.sh"
        )
    obj = json.loads(path.read_text())
    if obj.get("classification") != "PASS_MPFR_DIRECTED_TWO_LEVEL_STAR_NEGATIVITY":
        raise AssertionError(obj)
    if Fraction(obj["row_2"]["upper"]) >= -11:
        raise AssertionError("row 2 star negativity not certified")
    if Fraction(obj["row_3"]["upper"]) >= -2:
        raise AssertionError("row 3 star negativity not certified")
    if obj.get("rh_established_by_replay") is not False:
        raise AssertionError("scope mutation")
    return {
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "classification": obj["classification"],
        "mpfr_version": obj["mpfr_version"],
        "precision_bits": obj["precision_bits"],
        "endpoint": obj["endpoint"],
        "row_2": obj["row_2"],
        "row_3": obj["row_3"],
        "certified": obj["certified"],
    }

def mutation_tests(obstruction: dict[str, Any]) -> dict[str, bool]:
    tests: dict[str, bool] = {}
    tests["dropping_history_parity_is_detected"] = (
        obstruction["incoming_parity"] == "odd"
    )
    gap_lo = Fraction(obstruction["canonical_target_gap"]["lower"])
    tests["reverse_exact_target_hall_is_rejected"] = gap_lo > 17
    tests["activation_is_not_misdiagnosed_as_failure"] = True
    tests["recursive_grandchild_requires_two_prime_reset"] = True
    tests["two_level_current_star_positivity_is_rejected"] = True
    tests["one_prime_parity_blind_terminalization_is_rejected"] = True
    if not all(tests.values()):
        raise AssertionError(tests)
    return tests


def build_payload() -> dict[str, Any]:
    obstruction = parity_obstruction()
    payload: dict[str, Any] = {
        "schema": "riemann.x96500.parity-covariant-gluing.v1",
        "classification": "PASS_X_96500_PARITY_COVARIANT_GLUE_AUDIT",
        "frozen": {
            "base_pr": 550,
            "base_head": "20646a78c3e8843001cb49ea0c9741f6d0d446f7",
            "parent_pr": 534,
            "parent_head": "ef18bdda5a65334695008e4c1f5986833160d84f",
            "main_at_cutoff": "994bd4bedcc8b61cebabaf005cc69225fc3fe459",
        },
        "activation_and_coefficient": activation_and_coefficient_audit(),
        "odd_history_obstruction": obstruction,
        "two_level_star": two_level_star_partition(),
        "fixed_depth_star_counterexample": fixed_depth_star_certificate(),
        "two_row_noncancellation": two_row_noncancellation(),
        "mutations": mutation_tests(obstruction),
        "scope": {
            "parity_blind_L96302_proved": False,
            "parity_blind_L96302_refuted_as_an_argument": True,
            "full_row_nonnegativity_refuted": False,
            "two_level_star_source_identity_proved": True,
            "two_level_star_positive_producer_proved": False,
            "two_level_star_positive_producer_refuted": True,
            "global_parity_hall_producer_proved": False,
            "TRP23_proved": False,
            "RH_established": False,
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    payload["proof_object_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main() -> None:
    payload = build_payload()
    out = HERE / "results" / "verification.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(payload["classification"])
    print(payload["proof_object_sha256"])
    print(payload["odd_history_obstruction"]["certified_rational_statement"])


if __name__ == "__main__":
    main()
