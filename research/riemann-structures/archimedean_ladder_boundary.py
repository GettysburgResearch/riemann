#!/usr/bin/env python3
"""Exact finite replay of the archimedean ladder and its boundary defects."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIXTURE = HERE / "archimedean_ladder_boundary.json"
SOURCES = HERE / "archimedean_ladder_boundary.sources.json"
SOURCE_COMMIT = "6675c19f20760301d8c91dedc4a7836170003512"
SOURCE_PATH = "research/riemann-structures/RIEMANN_STRUCTURES_WAVE2_PORTFOLIO.md"
SOURCE_BLOB = "f5e0eb316f29d5e44cc3c7124401cb3e784fef49"


def exact_fraction(value: int | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("exact int or Fraction required")
    return Fraction(value)


@dataclass(frozen=True)
class GammaTerm:
    shift: Fraction
    multiplicity: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "shift", exact_fraction(self.shift))
        if isinstance(self.multiplicity, bool) or not isinstance(self.multiplicity, int):
            raise TypeError("integer multiplicity required")


def reduce_shifts(terms: tuple[GammaTerm, ...]) -> dict:
    """F = prod Gamma_R(s+c)^M_c * (2pi)^h * prod (s+a)^e_a."""
    tails: Counter = Counter()
    linear: Counter = Counter()
    two_pi_power = 0
    for term in terms:
        k = term.shift // 2
        c = term.shift - 2 * k
        tails[c] += term.multiplicity
        two_pi_power -= k * term.multiplicity
        indices = range(k) if k >= 0 else range(k, 0)
        sign = 1 if k >= 0 else -1
        for j in indices:
            linear[c + 2 * j] += sign * term.multiplicity
    return {
        "rational": all(value == 0 for value in tails.values()),
        "tail_multiplicities": [
            [str(c), tails[c]] for c in sorted(tails) if tails[c]
        ],
        "two_pi_power": two_pi_power,
        "linear_factors": [[str(a), linear[a]] for a in sorted(linear) if linear[a]],
    }


def divisor_order(terms: tuple[GammaTerm, ...], point: int | Fraction) -> int:
    """Positive is a zero, negative is a pole; exact at rational points."""
    s = exact_fraction(point)
    result = 0
    for term in terms:
        n = -(s + term.shift) / 2
        if n.denominator == 1 and n >= 0:
            result -= term.multiplicity
    return result


def stable_tails(terms: tuple[GammaTerm, ...]) -> list[dict]:
    groups: dict[Fraction, list[GammaTerm]] = defaultdict(list)
    for term in terms:
        groups[term.shift % 2].append(term)
    rows = []
    for c, members in sorted(groups.items()):
        start = max(0, *(int((term.shift - c) / 2) for term in members))
        points = [-c - 2 * (start + j) for j in range(3)]
        expected = -sum(term.multiplicity for term in members)
        orders = [divisor_order(terms, point) for point in points]
        if orders != [expected] * 3:
            raise ArithmeticError("stable divisor-tail identity failed")
        rows.append({"coset": str(c), "points": list(map(str, points)), "orders": orders})
    return rows


def rational_value(
    terms: tuple[GammaTerm, ...], s: int | Fraction, two_pi: int | Fraction
) -> Fraction:
    """Evaluate the formal rational shift identity, not the gamma function."""
    data = reduce_shifts(terms)
    if not data["rational"]:
        raise ValueError("unbalanced gamma tails do not define a rational reduction")
    x = exact_fraction(s)
    scale = exact_fraction(two_pi)
    if scale <= 0:
        raise ValueError("positive formal scale required")
    answer = scale ** data["two_pi_power"]
    for shift, exponent in data["linear_factors"]:
        answer *= (x + Fraction(shift)) ** exponent
    return answer


def parity(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value not in (0, 1):
        raise ValueError("parity must be exactly 0 or 1")
    return value


def tensor_data(epsilon: int, eta: int) -> tuple[int, int]:
    e, f = parity(epsilon), parity(eta)
    return e ^ f, e * f


def basis_weight(par: int, twist: int | Fraction, degree: int) -> tuple[Fraction, Fraction]:
    parity(par)
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("one-sided degree must be a nonnegative integer")
    return Fraction(2 * degree + par), exact_fraction(twist)


def pair_record(epsilon: int, eta: int) -> dict:
    target_parity, carry = tensor_data(epsilon, eta)
    checks = 0
    for n, m in product(range(5), repeat=2):
        left = basis_weight(epsilon, Fraction(2, 3), n)
        right = basis_weight(eta, Fraction(-5, 7), m)
        source = tuple(a + b for a, b in zip(left, right))
        target = basis_weight(target_parity, Fraction(2, 3) - Fraction(5, 7), n + m + carry)
        if source != target:
            raise ArithmeticError("balanced tensor map failed to intertwine")
        checks += 1
    return {
        "input_parities": [epsilon, eta],
        "output_parity": target_parity,
        "u_power": carry,
        "cokernel_dimension": carry,
        "basis_checks": checks,
    }


def triple_record(epsilon: int, eta: int, kappa: int) -> dict:
    ef, first = tensor_data(epsilon, eta)
    _, second = tensor_data(ef, kappa)
    fk, third = tensor_data(eta, kappa)
    _, fourth = tensor_data(epsilon, fk)
    left, right = first + second, third + fourth
    if left != right or left != (epsilon + eta + kappa) // 2:
        raise ArithmeticError("parity carry is not associative")
    return {"parities": [epsilon, eta, kappa], "left_u_power": left, "right_u_power": right}


def dual_record(epsilon: int) -> dict:
    e = parity(epsilon)
    twist = Fraction(3, 5)
    for n in range(5):
        character_dual = basis_weight(e, -twist, n)
        connection_dual_after_map = (Fraction(2 * (n + e) - e), -twist)
        if character_dual != connection_dual_after_map:
            raise ArithmeticError("dual boundary failed to intertwine")
    return {"parity": e, "u_power": e, "cokernel_dimension": e, "perfect_over_A": e == 0}


def authenticate_sources() -> dict:
    data = json.loads(SOURCES.read_text(encoding="utf-8"))
    expected = {
        "source_commit": SOURCE_COMMIT,
        "frozen_programme_path": SOURCE_PATH,
        "frozen_programme_blob": SOURCE_BLOB,
        "current_programme_may_evolve": True,
    }
    for key, value in expected.items():
        if data.get(key) != value:
            raise ValueError(f"source manifest mismatch: {key}")
    raw = subprocess.check_output(
        ["git", "rev-parse", f"{SOURCE_COMMIT}:{SOURCE_PATH}"], cwd=ROOT, text=True
    ).strip()
    if raw != SOURCE_BLOB:
        raise ValueError("frozen programme blob mismatch")
    return {
        **expected,
        "source_manifest_sha256": hashlib.sha256(SOURCES.read_bytes()).hexdigest(),
        "imported_analytic_facts_are_not_computationally_certified": True,
    }


def build_report() -> dict:
    examples = {
        "empty_product": (),
        "one_effective_real_type": (GammaTerm(0, 1),),
        "even_odd_pair": (GammaTerm(0, 1), GammaTerm(1, 1)),
        "forward_shift": (GammaTerm(2, 1), GammaTerm(0, -1)),
        "backward_shift": (GammaTerm(-2, 1), GammaTerm(0, -1)),
        "false_total_rank_cancellation": (GammaTerm(1, 1), GammaTerm(0, -1)),
        "fractional_shift_balanced": (GammaTerm(Fraction(9, 2), 1), GammaTerm(Fraction(1, 2), -1)),
        "mixed_balanced": (GammaTerm(4, 2), GammaTerm(0, -2), GammaTerm(3, -1), GammaTerm(1, 1)),
        "mixed_unbalanced": (GammaTerm(Fraction(-7, 3), 2), GammaTerm(Fraction(5, 3), -1)),
    }
    rows = []
    for name, terms in examples.items():
        rows.append({
            "name": name,
            "terms": [[str(t.shift), t.multiplicity] for t in terms],
            **reduce_shifts(terms),
            "stable_tail_checks": stable_tails(terms),
        })
    ordinary_multiplicities = [
        sum(1 for n in range(k + 1) for m in range(k + 1) if n + m == k)
        for k in range(7)
    ]
    if ordinary_multiplicities != list(range(1, 8)):
        raise ArithmeticError("ordinary tensor multiplicity failed")
    parity_split = sorted([2 * n for n in range(6)] + [2 * n + 1 for n in range(6)])
    if parity_split != list(range(12)):
        raise ArithmeticError("real/complex ladder split failed")
    return {
        "schema": "archimedean-ladder-boundary-v1",
        "scope": "exact finite algebra, not a gamma or global-L proof certificate",
        "source_authentication": authenticate_sources(),
        "gamma_shift_examples": rows,
        "tensor_pairs": [pair_record(e, f) for e, f in product((0, 1), repeat=2)],
        "tensor_associativity": [triple_record(*p) for p in product((0, 1), repeat=3)],
        "duals": [dual_record(e) for e in (0, 1)],
        "ordinary_C_tensor_multiplicities": ordinary_multiplicities,
        "balanced_A_tensor_multiplicity": 1,
        "spacing_one_split": parity_split,
        "regularized_determinant": {
            "real": "sqrt(2)/Gamma_R(s+mu)",
            "complex": "2/Gamma_C(s+mu)",
            "proof_kind": "analytic derivation from imported Hurwitz zeta values; not numeric replay",
        },
        "firewalls": {
            "finite_affine_effective_gamma_model": "excluded by infinite divisor",
            "shift_balanced_virtual_gamma_products": "rational; essential exception",
            "one_sided_tensor_assignment": "lax, not strong",
            "localized_positive_time_heat_trace": "divergent; original regularization unavailable",
            "global_completion": "not constructed",
            "external_novelty": "not claimed",
            "RH_or_GRH": "not proved",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()
    report = build_report()
    if args.write:
        FIXTURE.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"wrote {FIXTURE.name}")
    elif json.loads(FIXTURE.read_text(encoding="utf-8")) != report:
        raise SystemExit("fixture differs from exact replay")
    else:
        print("archimedean ladder: source lock, 9 shift fixtures, 100 basis maps, 8 parity triples PASS")


if __name__ == "__main__":
    main()
