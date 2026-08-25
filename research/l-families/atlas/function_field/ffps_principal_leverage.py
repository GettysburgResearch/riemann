#!/usr/bin/env python3
"""Exact local leverage and physical-squareclass controls for FFPS106121.

This packet does not estimate the open global mixed or double moments.  It
extracts the sharp principal leverage of the local Kummer phase frame, proves
the exact positive direct-sum assembly formula, and checks tiny prime-field
models of the corrected Pc^2 collision coordinate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from typing import Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "ffps_principal_leverage.json"
NOTE_PATH = HERE / "FFPS_PHYSICAL_SQUARECLASS_ADAPTER.md"
TEST_PATH = ROOT / "tests" / "test_ffps_principal_leverage.py"

SOURCE_COMMIT_751 = "37d9df4b9b4fb9a8277de6ec1f77278dbbe5b0f2"
SOURCE_BLOBS_751 = {
    "T-106121": "55afc90eaf7d2cd3efa102bcc97b927943731d48",
    "L-106024": "d94787dc2cd1cedd74d33ddc6269daf8de1cc061",
    "R-106122": "dc51ae3add697ab4cec868ef8439f864ce77d71a",
    "R-106123": "f89cad68d67444280088d8bea7cbfb7c1eacc90d",
    "L-106126": "b4dbebde403a11696c56a4689b2df8b53326a157",
}

MAX_PRIME_CONTROL = 127
MAX_CONTROL_ATOMS = 4_096


def _sha256_lf(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _is_odd_prime(prime: int) -> bool:
    if prime < 3 or prime % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            return False
        divisor += 2
    return True


def sign_pair_dimension(prime: int) -> int:
    if not _is_odd_prime(prime):
        raise ValueError("the prime-field control requires an odd prime")
    return (prime - 1) // 2


def phase_gram(prime: int) -> tuple[tuple[int, ...], ...]:
    """Return G=pI-J in sign-pair coordinates."""

    dimension = sign_pair_dimension(prime)
    return tuple(
        tuple(prime - 1 if row == column else -1 for column in range(dimension))
        for row in range(dimension)
    )


def quadratic_form(matrix: Sequence[Sequence[int]], vector: Sequence[int]) -> int:
    if len(matrix) != len(vector) or any(len(row) != len(vector) for row in matrix):
        raise ValueError("quadratic-form dimension mismatch")
    return sum(
        vector[row] * matrix[row][column] * vector[column]
        for row in range(len(vector))
        for column in range(len(vector))
    )


def principal_leverage_squared(prime: int) -> Fraction:
    """Squared dual norm of w -> sum_j w_j for G=pI-J."""

    sign_pair_dimension(prime)
    return Fraction(prime - 1, prime + 1)


def leverage_spectrum(prime: int) -> dict[str, object]:
    dimension = sign_pair_dimension(prime)
    return {
        "sign_pair_dimension": dimension,
        "phase_gram_eigenvalues": [
            {"eigenvalue": Fraction(prime + 1, 2), "multiplicity": 1, "mode": "constant"},
            {"eigenvalue": prime, "multiplicity": dimension - 1, "mode": "sum_zero"},
        ],
        "principal_observation_squared_singular_values": [
            {"value": principal_leverage_squared(prime), "multiplicity": 1},
            {"value": Fraction(0), "multiplicity": dimension - 1},
        ],
    }


def tensor_leverage_squared(primes: Sequence[int]) -> Fraction:
    result = Fraction(1)
    for prime in primes:
        result *= principal_leverage_squared(prime)
    return result


def positive_block_leverage_squared(
    primes: Sequence[int], weights: Sequence[Fraction | int]
) -> Fraction:
    """Dual norm for sum_i alpha_i O_i on a positive block direct sum."""

    if len(primes) != len(weights) or not primes:
        raise ValueError("positive block assembly needs equally sized nonempty inputs")
    return sum(
        (
            Fraction(weight) ** 2 * principal_leverage_squared(prime)
            for prime, weight in zip(primes, weights)
        ),
        Fraction(0),
    )


def constant_extremizer(prime: int, total: int = 1) -> tuple[Fraction, ...]:
    dimension = sign_pair_dimension(prime)
    return tuple(Fraction(total, dimension) for _ in range(dimension))


def phase_energy(prime: int, vector: Sequence[Fraction | int]) -> Fraction:
    dimension = sign_pair_dimension(prime)
    if len(vector) != dimension:
        raise ValueError("phase vector has the wrong sign-pair dimension")
    values = tuple(Fraction(value) for value in vector)
    return prime * sum((value * value for value in values), Fraction(0)) - sum(values, Fraction(0)) ** 2


def physical_squareclass(owner: int, core: int, prime: int) -> int:
    sign_pair_dimension(prime)
    if owner % prime == 0 or core % prime == 0:
        raise ValueError("owner and core must be units modulo the marked divisor")
    return (owner * core * core) % prime


def quadratic_character(value: int, prime: int) -> int:
    sign_pair_dimension(prime)
    residue = value % prime
    if residue == 0:
        return 0
    symbol = pow(residue, (prime - 1) // 2, prime)
    return 1 if symbol == 1 else -1


def square_roots(value: int, prime: int) -> tuple[int, ...]:
    if prime > MAX_PRIME_CONTROL:
        raise ValueError(f"prime-field root control refuses p>{MAX_PRIME_CONTROL}")
    sign_pair_dimension(prime)
    roots = tuple(unit for unit in range(1, prime) if unit * unit % prime == value % prime)
    if len(roots) not in (0, 2):
        raise ArithmeticError("nonzero odd-prime residue has unexpected root count")
    return roots


def collision_slopes(
    owner: int, other_owner: int, sign: int, prime: int
) -> tuple[int, ...]:
    """Return omega with c=omega*c' for Pc^2=sign*P'c'^2."""

    if sign not in (-1, 1):
        raise ValueError("collision sign must be plus or minus one")
    if owner % prime == 0 or other_owner % prime == 0:
        raise ValueError("owners must be units")
    ratio = sign * other_owner * pow(owner, -1, prime)
    return square_roots(ratio, prime)


def verify_collision_lines(
    owner: int, other_owner: int, sign: int, prime: int
) -> dict[str, object]:
    slopes = collision_slopes(owner, other_owner, sign, prime)
    atom_count = (prime - 1) ** 2
    if atom_count > MAX_CONTROL_ATOMS:
        raise ValueError(
            f"collision control refuses {atom_count} atoms above {MAX_CONTROL_ATOMS}"
        )
    direct = {
        (core, other_core)
        for core in range(1, prime)
        for other_core in range(1, prime)
        if physical_squareclass(owner, core, prime)
        == sign * physical_squareclass(other_owner, other_core, prime) % prime
    }
    predicted = {
        (slope * other_core % prime, other_core)
        for slope in slopes
        for other_core in range(1, prime)
    }
    if direct != predicted:
        raise ArithmeticError("physical-squareclass collision is not the predicted line union")
    return {
        "prime": prime,
        "owner": owner % prime,
        "other_owner": other_owner % prime,
        "sign": sign,
        "slopes": list(slopes),
        "line_count": len(slopes),
        "collision_pair_count": len(direct),
        "atoms_checked": atom_count,
    }


def build_fixture() -> dict[str, object]:
    local_rows = []
    for prime in (3, 5, 7, 11):
        gram = phase_gram(prime)
        extremizer = constant_extremizer(prime)
        energy = phase_energy(prime, extremizer)
        observation = sum(extremizer, Fraction(0))
        ratio = observation * observation / energy
        if ratio != principal_leverage_squared(prime):
            raise ArithmeticError("constant packet ceased to be the sharp extremizer")
        spectrum = leverage_spectrum(prime)
        local_rows.append(
            {
                "prime": prime,
                "phase_gram": [list(row) for row in gram],
                "spectrum": {
                    "sign_pair_dimension": spectrum["sign_pair_dimension"],
                    "phase_gram_eigenvalues": [
                        {
                            **row,
                            "eigenvalue": [row["eigenvalue"].numerator, row["eigenvalue"].denominator],
                        }
                        for row in spectrum["phase_gram_eigenvalues"]
                    ],
                    "principal_observation_squared_singular_values": [
                        {
                            "value": [row["value"].numerator, row["value"].denominator],
                            "multiplicity": row["multiplicity"],
                        }
                        for row in spectrum["principal_observation_squared_singular_values"]
                    ],
                },
                "sharp_extremizer": [
                    [value.numerator, value.denominator] for value in extremizer
                ],
                "sharp_leverage_squared": [ratio.numerator, ratio.denominator],
            }
        )

    line_controls = []
    atoms = 0
    for prime in (3, 5, 7, 11):
        for sign in (1, -1):
            row = verify_collision_lines(1, 1, sign, prime)
            atoms += int(row["atoms_checked"])
            line_controls.append(row)
    if atoms > MAX_CONTROL_ATOMS:
        raise ArithmeticError("aggregate collision controls exceeded the public atom cap")

    # Explicitly separate owner-only aliases from physical-squareclass aliases.
    owner_only_false_positive = {
        "prime": 7,
        "owner_pair": [1, 1],
        "core_pair": [1, 2],
        "owner_products_equal": True,
        "physical_values": [
            physical_squareclass(1, 1, 7),
            physical_squareclass(1, 2, 7),
        ],
    }
    if owner_only_false_positive["physical_values"][0] in (
        owner_only_false_positive["physical_values"][1],
        -owner_only_false_positive["physical_values"][1] % 7,
    ):
        raise ArithmeticError("chosen owner-only false positive is not a counterexample")
    physical_alias_with_different_owners = {
        "prime": 7,
        "owner_core_pairs": [[1, 2], [2, 3]],
        "owners_equal": False,
        "physical_values": [
            physical_squareclass(1, 2, 7),
            physical_squareclass(2, 3, 7),
        ],
    }
    if len(set(physical_alias_with_different_owners["physical_values"])) != 1:
        raise ArithmeticError("chosen distinct-owner physical alias failed")

    direct_sum_example = positive_block_leverage_squared((3, 5), (1, 1))
    if direct_sum_example != Fraction(7, 6):
        raise ArithmeticError("two-fibre positive assembly control drifted")

    return {
        "schema": "riemann.function_field.ffps_principal_leverage.v1",
        "status": "EXACT_LOCAL_OPERATOR_AND_FINITE_PHYSICAL_SQUARECLASS_CONTROLS",
        "source_frontier": {
            "pr": 751,
            "commit": SOURCE_COMMIT_751,
            "live_target": "T-106121 / FFPS106121",
            "git_blob_ids": SOURCE_BLOBS_751,
            "superseded_target": "FFDA106110 owner-only global collisions",
        },
        "adapter_contract": {
            "marked_divisors": (
                "Use explicitly marked irreducible divisors ell and rho and an exact "
                "partition of tie/roughness strata; do not call a degree+lex selector "
                "an algebraic least-prime map."
            ),
            "physical_coordinates": ["(P,c)->P*c^2 mod rho", "(Q,d)->Q*d^2 mod ell"],
            "assembly_order": "retain both complete source sums and amplify before squaring",
            "principal_member": "principal-principal member equals the native untwisted Boolean incidence current",
            "exceptional_ledger": [
                "atomic diagonal",
                "equal physical product",
                "quadratic-root",
                "shared owner/incidence",
                "owner/core overlap",
                "geometrically constant constituent",
            ],
            "still_open": ["BTPS106121", "BTMS106121", "BTDS106121", "BCI102990", "RH"],
        },
        "principal_leverage_theorem": {
            "local_formula": "||O_p||^2=(p-1)/(p+1)",
            "local_spectra": local_rows,
            "tensor_formula": "for distinct marked phases, squared leverage is product_i (p_i-1)/(p_i+1)",
            "positive_block_formula": "||sum_i alpha_i O_i||^2=sum_i |alpha_i|^2 (p_i-1)/(p_i+1)",
            "two_fibre_example_primes_3_5": [
                direct_sum_example.numerator,
                direct_sum_example.denominator,
            ],
            "no_go": (
                "A block-diagonal positive sum of locally sharp Kummer frames supplies "
                "no cross-conductor saving; with unit weights its leverage grows as the "
                "sum of the local leverages. Any improvement must use coherent "
                "cross-fibre structure before the fibres are positively squared."
            ),
        },
        "physical_squareclass_controls": {
            "line_theorem": (
                "Pc^2=epsilon*P'c'^2 modulo an odd marked prime is the union of "
                "zero or two lines c=omega*c' for each sign; within one owner "
                "quadratic class the combined plus/minus collision has two lines "
                "when p=3 mod 4 and four when p=1 mod 4."
            ),
            "prime_field_replays": line_controls,
            "aggregate_atoms_checked": atoms,
            "owner_only_false_positive": owner_only_false_positive,
            "different_owner_physical_alias": physical_alias_with_different_owners,
        },
        "normalization_firewall": (
            "The canonical XD K1 is dyadic. Replacing its dilation 2 by the norm "
            "base q would define a new degree-wavelet analogue, not a literal source-"
            "faithful XD port. This packet therefore uses the polynomial Boolean/Kummer "
            "source already native to T-106121."
        ),
        "smallest_next_theorem": (
            "Construct one incomplete varying-core Kummer line family with its exact "
            "conductor and prove cancellation after the exceptional ledger is removed; "
            "a complete owner shell or fixed-core bound alone is insufficient."
        ),
        "scope": {
            "global_moment_proved": False,
            "number_field_export_proved": False,
            "rh_or_grh_proved": False,
            "prime_field_controls_only": [3, 5, 7, 11],
            "finite_field_extension_claim": "the operator and line proofs are algebraic for every odd finite residue field; only the tiny replays are prime-field",
        },
        "provenance": {
            "producer_sha256_lf": _sha256_lf(Path(__file__)),
            "note_sha256_lf": _sha256_lf(NOTE_PATH),
            "test_sha256_lf": _sha256_lf(TEST_PATH),
            "resource_caps": {
                "maximum_prime_control": MAX_PRIME_CONTROL,
                "maximum_collision_atoms": MAX_CONTROL_ATOMS,
                "aggregate_atoms_used": atoms,
            },
        },
    }


def _canonical(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--stdout", action="store_true")
    args = parser.parse_args()
    rendered = _canonical(build_fixture())
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            raise SystemExit("FFPS principal leverage fixture drifted")
        print("PASS_FFPS_PRINCIPAL_LEVERAGE")
        return
    if args.stdout:
        print(rendered, end="")
        return
    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
