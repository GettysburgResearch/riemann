#!/usr/bin/env python3
"""Bounded exact search for symmetric virtual characters on USp(4).

The finite panels are deliberately small.  Candidate characters and the C2
Weyl density are exact Laurent polynomials over Z; Haar moments are Weyl
constant terms.  Finite-moment survivors are accepted only when an all-order
certificate applies: central oddness under U -> -U, or the (2,2) mod 4
support certificate of B=chi_(2,0)-chi_(0,2).

There is no sampling, numerical integration, finite-field enumeration, or
USp(6) search.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from dataclasses import dataclass, field
from math import comb
from pathlib import Path
from time import perf_counter
from typing import Mapping, Sequence

import usp_coefficient_minor_rank_scan as base


Exponent = tuple[int, int]
Laurent = dict[Exponent, int]

HERE = Path(__file__).resolve().parent
DEFAULT_OUTPUT = HERE / "virtual_character_null_directions.json"
NOTE_PATH = HERE / "VIRTUAL_CHARACTER_NULL_DIRECTIONS.md"
CHECKER_PATH = HERE.parents[3] / "tests" / "test_virtual_character_null_directions.py"
BASE_PATH = HERE / "usp_coefficient_minor_rank_scan.py"

MAX_WALL_SECONDS = 15.0
MAX_LAURENT_TERMS = 5_000
MAX_ABS_EXPONENT = 32
RESOURCE_LIMITS = {
    "candidate_vectors": 1_500,
    "laurent_pair_products": 60_000_000,
    "constant_term_lookups": 4_000_000,
    "linear_term_updates": 200_000,
}


@dataclass
class SearchGuard:
    limits: dict[str, int] = field(default_factory=lambda: dict(RESOURCE_LIMITS))
    counts: dict[str, int] = field(
        default_factory=lambda: {name: 0 for name in RESOURCE_LIMITS}
    )
    started: float = field(default_factory=perf_counter)

    def charge(self, category: str, amount: int = 1) -> None:
        if category not in self.limits or amount < 0:
            raise ValueError(f"invalid resource charge {category!r}: {amount}")
        self.counts[category] += amount
        if self.counts[category] > self.limits[category]:
            raise RuntimeError(
                f"resource cap exceeded for {category}: "
                f"{self.counts[category]} > {self.limits[category]}"
            )
        if perf_counter() - self.started > MAX_WALL_SECONDS:
            raise RuntimeError(
                f"virtual-character search exceeded {MAX_WALL_SECONDS:g} seconds"
            )

    def snapshot(self) -> dict[str, int]:
        return dict(sorted(self.counts.items()))


def _check(polynomial: Mapping[Exponent, int]) -> None:
    if len(polynomial) > MAX_LAURENT_TERMS:
        raise RuntimeError(
            f"Laurent support cap exceeded: {len(polynomial)} > {MAX_LAURENT_TERMS}"
        )
    if polynomial and max(max(abs(a), abs(b)) for a, b in polynomial) > MAX_ABS_EXPONENT:
        raise RuntimeError("Laurent exponent cap exceeded")


def add_linear(
    terms: Sequence[tuple[Mapping[Exponent, int], int]], guard: SearchGuard
) -> Laurent:
    result: Laurent = {}
    for polynomial, scalar in terms:
        guard.charge("linear_term_updates", len(polynomial))
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + scalar * coefficient
            if result[exponent] == 0:
                del result[exponent]
    _check(result)
    return result


def multiply(
    left: Mapping[Exponent, int],
    right: Mapping[Exponent, int],
    guard: SearchGuard,
) -> Laurent:
    guard.charge("laurent_pair_products", len(left) * len(right))
    result: Laurent = {}
    for (a, b), left_coefficient in left.items():
        for (c, d), right_coefficient in right.items():
            exponent = (a + c, b + d)
            result[exponent] = (
                result.get(exponent, 0) + left_coefficient * right_coefficient
            )
    result = {exponent: coefficient for exponent, coefficient in result.items() if coefficient}
    _check(result)
    return result


def scale(polynomial: Mapping[Exponent, int], scalar: int) -> Laurent:
    result = {
        exponent: scalar * coefficient
        for exponent, coefficient in polynomial.items()
        if scalar * coefficient
    }
    _check(result)
    return result


def c2_weyl_density_from_positive_roots() -> Laurent:
    """Reconstruct the complete C2 density without the character dependency."""

    density: Laurent = {(0, 0): 1}
    for root in ((2, 0), (0, 2), (1, 1), (1, -1)):
        factor = {(0, 0): 2, root: -1, (-root[0], -root[1]): -1}
        following: Laurent = {}
        for (a, b), coefficient in density.items():
            for (c, d), factor_coefficient in factor.items():
                exponent = (a + c, b + d)
                following[exponent] = (
                    following.get(exponent, 0)
                    + coefficient * factor_coefficient
                )
        density = {
            exponent: coefficient
            for exponent, coefficient in following.items()
            if coefficient
        }
    return density


def haar_constant_term(
    polynomial: Mapping[Exponent, int],
    density: Mapping[Exponent, int],
    guard: SearchGuard,
) -> int:
    guard.charge("constant_term_lookups", len(polynomial))
    numerator = sum(
        coefficient * density.get((-a, -b), 0)
        for (a, b), coefficient in polynomial.items()
    )
    if numerator % 8:
        raise ArithmeticError("nonintegral C2 Weyl constant term")
    return numerator // 8


def moments(
    polynomial: Mapping[Exponent, int],
    maximum_order: int,
    density: Mapping[Exponent, int],
    guard: SearchGuard,
) -> list[int]:
    power: Laurent = {(0, 0): 1}
    result = []
    for _order in range(1, maximum_order + 1):
        power = multiply(power, polynomial, guard)
        result.append(haar_constant_term(power, density, guard))
    return result


def odd_moments(
    polynomial: Mapping[Exponent, int],
    maximum_odd_order: int,
    density: Mapping[Exponent, int],
    guard: SearchGuard,
) -> list[int]:
    return moments(polynomial, maximum_odd_order, density, guard)[::2]


def _primitive_sign_normalized(vector: Sequence[int]) -> bool:
    if not any(vector):
        return False
    gcd = 0
    for value in vector:
        gcd = math.gcd(gcd, abs(value))
    first = next(value for value in vector if value)
    return gcd == 1 and first > 0


def _character(
    engine: base.CnCharacterEngine, fundamental_weight: tuple[int, int]
) -> Laurent:
    a, b = fundamental_weight
    return engine.character((a + b, b))


def enumerate_panel(
    *,
    name: str,
    labels: Sequence[str],
    polynomials: Sequence[Mapping[Exponent, int]],
    coefficient_bound: int,
    l1_cap: int,
    maximum_odd_order: int,
    density: Mapping[Exponent, int],
    guard: SearchGuard,
) -> dict[str, object]:
    tested = 0
    survivors = []
    coefficient_range = range(-coefficient_bound, coefficient_bound + 1)
    for vector in itertools.product(coefficient_range, repeat=len(labels)):
        if sum(abs(value) for value in vector) > l1_cap:
            continue
        if not _primitive_sign_normalized(vector):
            continue
        guard.charge("candidate_vectors")
        tested += 1
        polynomial = add_linear(
            [(basis_element, coefficient) for basis_element, coefficient in zip(polynomials, vector)],
            guard,
        )
        if not polynomial:
            raise ArithmeticError("independent character basis produced zero")
        candidate_odd_moments = odd_moments(
            polynomial, maximum_odd_order, density, guard
        )
        if all(value == 0 for value in candidate_odd_moments):
            survivors.append(
                {
                    "coefficients": list(vector),
                    "odd_moments": candidate_odd_moments,
                }
            )
    return {
        "name": name,
        "ordered_basis": list(labels),
        "coefficient_box": [-coefficient_bound, coefficient_bound],
        "l1_cap": l1_cap,
        "primitive": True,
        "overall_sign_quotient": "first nonzero coefficient positive",
        "odd_orders_screened": list(range(1, maximum_odd_order + 1, 2)),
        "candidate_count": tested,
        "survivor_count": len(survivors),
        "survivors": survivors,
    }


def _sha256_lf(path: Path) -> str:
    source = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def _survivor_vectors(panel: Mapping[str, object]) -> set[tuple[int, ...]]:
    return {
        tuple(row["coefficients"])
        for row in panel["survivors"]  # type: ignore[index]
    }


def build_fixture() -> dict[str, object]:
    guard = SearchGuard()
    character_guard = base.ResourceGuard()
    engine = base.CnCharacterEngine(2, character_guard)
    density = base.weyl_density(2, character_guard)
    reconstructed_density = c2_weyl_density_from_positive_roots()
    if density != reconstructed_density:
        raise ArithmeticError(
            "C2 Weyl density disagrees with the complete positive-root reconstruction"
        )

    one = _character(engine, (0, 0))
    chi_01 = _character(engine, (0, 1))
    chi_20 = _character(engine, (2, 0))
    chi_02 = _character(engine, (0, 2))
    chi_10 = _character(engine, (1, 0))
    chi_11 = _character(engine, (1, 1))
    chi_30 = _character(engine, (3, 0))
    chi_21 = _character(engine, (2, 1))
    chi_40 = _character(engine, (4, 0))

    e1 = base.elementary_character(2, 1)
    e2 = base.elementary_character(2, 2)
    e3 = base.elementary_character(2, 3)
    if e1 != e3:
        raise ArithmeticError("USp(4) reciprocity e_3=e_1 failed")
    e1_square = multiply(e1, e1, guard)
    e2_square = multiply(e2, e2, guard)
    e1e3 = multiply(e1, e3, guard)
    expected_e1_square = add_linear(((one, 1), (chi_01, 1), (chi_20, 1)), guard)
    expected_e2_square = add_linear(
        ((one, 2), (chi_01, 2), (chi_20, 1), (chi_02, 1)), guard
    )
    if e1_square != expected_e1_square or e2_square != expected_e2_square:
        raise ArithmeticError("coefficient-square character decomposition failed")
    if e1e3 != e1_square:
        raise ArithmeticError("e_1*e_3=e_1^2 failed")

    balanced = add_linear(((e1_square, 2), (e2_square, -1)), guard)
    virtual_balanced = add_linear(((chi_20, 1), (chi_02, -1)), guard)
    u = {(2, 0): 1, (-2, 0): 1}
    v = {(0, 2): 1, (0, -2): 1}
    factored_balanced = scale(multiply(u, v, guard), -1)
    if not (balanced == virtual_balanced == factored_balanced):
        raise ArithmeticError("B character/factorization certificate failed")

    square_panel = enumerate_panel(
        name="square_character_span",
        labels=("1", "chi_01", "chi_20", "chi_02"),
        polynomials=(one, chi_01, chi_20, chi_02),
        coefficient_bound=2,
        l1_cap=5,
        maximum_odd_order=9,
        density=density,
        guard=guard,
    )
    central_panel = enumerate_panel(
        name="central_odd_extension",
        labels=("1", "chi_01", "chi_20", "chi_02", "chi_10", "chi_11", "chi_30"),
        polynomials=(one, chi_01, chi_20, chi_02, chi_10, chi_11, chi_30),
        coefficient_bound=1,
        l1_cap=4,
        maximum_odd_order=7,
        density=density,
        guard=guard,
    )
    weight_four_panel = enumerate_panel(
        name="even_weight_four_extension",
        labels=("1", "chi_01", "chi_20", "chi_02", "chi_21", "chi_40"),
        polynomials=(one, chi_01, chi_20, chi_02, chi_21, chi_40),
        coefficient_bound=1,
        l1_cap=4,
        maximum_odd_order=7,
        density=density,
        guard=guard,
    )

    b4 = (0, 0, 1, -1)
    if _survivor_vectors(square_panel) != {b4}:
        raise ArithmeticError("unexpected survivor in square-character panel")
    if _survivor_vectors(weight_four_panel) != {(0, 0, 1, -1, 0, 0)}:
        raise ArithmeticError("unexpected survivor in even weight-four panel")
    expected_central = {
        (0, 0, 0, 0, *odd)
        for odd in itertools.product((-1, 0, 1), repeat=3)
        if _primitive_sign_normalized(odd)
    }
    expected_central.add((0, 0, 1, -1, 0, 0, 0))
    if _survivor_vectors(central_panel) != expected_central:
        raise ArithmeticError("unexpected survivor in central extension panel")

    b_moments = moments(balanced, 10, density, guard)
    expected_b_moments = [
        0 if order % 2 else comb(order, order // 2) ** 2 // (order // 2 + 1)
        for order in range(1, 11)
    ]
    if b_moments != expected_b_moments:
        raise ArithmeticError("B closed moment formula failed frozen rungs")

    forbidden_density_residue = {
        exponent: coefficient
        for exponent, coefficient in density.items()
        if exponent[0] % 4 == 2 and exponent[1] % 4 == 2
    }
    if forbidden_density_residue:
        raise ArithmeticError("C2 Weyl density meets the B odd residue class")

    return {
        "schema": "riemann.function_field.virtual_character_null_directions.v1",
        "status": "EXACT_BOUNDED_USP4_SEARCH_PLUS_ALL_ORDER_CERTIFICATES",
        "scope": {
            "group": "USp(4)",
            "usp6_searched": False,
            "finite_field_enumeration": False,
            "random_sampling": False,
            "numerical_integration": False,
            "arithmetic_family_claims": False,
        },
        "coefficient_square_lattice": {
            "raw_ordered_basis": ["e_1^2", "e_2^2", "e_1*e_3"],
            "reciprocity_relation": "e_1*e_3=e_1^2",
            "haar_means": [1, 2, 1],
            "zero_mean_equation": "a+2*b+c=0",
            "integer_basis": [[2, -1, 0], [-1, 0, 1]],
            "parameterization": "(a,b,c)=t*(2,-1,0)+s*(-1,0,1)",
            "relation_kernel_generator": [-1, 0, 1],
            "quotient_null_generator": [2, -1, 0],
            "quotient_conclusion": "Every nonzero null class is an integer multiple of B.",
        },
        "character_identities": {
            "e_1_squared": "1+chi_01+chi_20",
            "e_2_squared": "2+2*chi_01+chi_20+chi_02",
            "B": "2*e_1^2-e_2^2=chi_20-chi_02",
            "B_torus": "-(x_1^2+x_1^-2)*(x_2^2+x_2^-2)",
        },
        "exact_symmetry_certificates": {
            "central_odd": {
                "statement": "Every Z-linear combination of chi_(a,b) with odd a is odd under Haar-preserving U->-U.",
                "consequence": "The pushforward is exactly symmetric and every odd Haar moment is zero.",
                "frozen_basis": ["chi_10", "chi_11", "chi_30"],
            },
            "B_residue": {
                "residue_class_mod_4": [2, 2],
                "weyl_density_coefficients_on_possible_residue_support": [
                    {"exponent": list(exponent), "coefficient": coefficient}
                    for exponent, coefficient in sorted(forbidden_density_residue.items())
                ],
                "all_odd_moments": 0,
                "even_moment_formula": "Haar(B^(2r))=binomial(2r,r)^2/(r+1)",
                "frozen_moments_1_through_10": b_moments,
                "compact_determinacy": "A bounded real class function with all odd moments zero has symmetric pushforward.",
            },
            "infinite_residue_null_module": {
                "definition": "B*Z[u^2+v^2,u^2*v^2]",
                "u": "x_1^2+x_1^-2",
                "v": "x_2^2+x_2^-2",
                "proof": "The multiplier ring has support in 4*Z^2, so every module element has support in (2,2)+4*Z^2; odd powers cannot meet the C2 Weyl-density support.",
                "exhaustiveness_claimed": False,
            },
        },
        "search_panels": [square_panel, central_panel, weight_four_panel],
        "conclusion": {
            "bounded": "B is the unique non-central survivor in all three frozen low-weight panels.",
            "coefficient_span": "Modulo e_1*e_3=e_1^2, B is the unique primitive coefficient-square null direction.",
            "global": "B is not globally isolated: it generates a certified infinite residue-null module; the center-odd graded sector is another structured symmetry lattice.",
        },
        "stopping_rule": "No weights, coefficient boxes, moments, ranks, or finite fields beyond the three declared USp(4) panels were searched.",
        "verification": {
            "character_method": "Capped exact C2 Kostant characters followed by Laurent reconstruction.",
            "haar_method": "Exact C2 Weyl-density constant terms divided by Weyl order 8.",
            "density_cross_check": "The complete density equals an independent product over all four positive C2 roots, and its full support avoids residue (2,2) modulo 4.",
            "survivor_rule": "Finite odd-moment survivors are retained only when central oddness or the B residue proof supplies an all-order certificate.",
        },
        "producer": {
            "script": Path(__file__).name,
            "source_sha256_lf_normalized": _sha256_lf(Path(__file__)),
            "note": NOTE_PATH.name,
            "note_sha256_lf_normalized": _sha256_lf(NOTE_PATH),
            "checker": "tests/test_virtual_character_null_directions.py",
            "checker_sha256_lf_normalized": _sha256_lf(CHECKER_PATH),
            "character_dependency": BASE_PATH.name,
            "character_dependency_sha256_lf_normalized": _sha256_lf(BASE_PATH),
        },
        "resource_contract": {
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "maximum_laurent_terms": MAX_LAURENT_TERMS,
            "maximum_abs_exponent": MAX_ABS_EXPONENT,
            "hard_caps": dict(sorted(RESOURCE_LIMITS.items())),
            "observed_counts": guard.snapshot(),
            "character_engine_observed_counts": character_guard.snapshot(),
        },
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="write the exact fixture")
    mode.add_argument("--check", action="store_true", help="compare with the fixture")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(argv)

    fixture = build_fixture()
    if args.write:
        args.output.write_text(
            json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        print(f"wrote {args.output}")
        return 0

    expected = json.loads(args.output.read_text(encoding="utf-8"))
    if fixture != expected:
        raise SystemExit("virtual-character null-direction fixture mismatch")
    print("virtual-character null-direction fixture verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
