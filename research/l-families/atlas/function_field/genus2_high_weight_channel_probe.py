#!/usr/bin/env python3
"""Bounded exact probe of the genus-two high-weight second-moment packet.

This packet does not enumerate a finite field.  It performs four exact tasks:

* verify Laurent-polynomial formulas for chi_(0,3), chi_(2,2), chi_(0,4);
* triangularize those characters against b^3, a^2*b^2, and b^4;
* enumerate the 23 factor signatures in the new b^3 roadmap; and
* replay frozen q=3,5,7 aggregate controls while keeping their sparse all-q
  continuation explicitly conjectural.

The finite controls do not prove any formula outside q=3,5,7.  In particular,
this is not an all-q second-moment certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence

import genus2_second_moment_reduction as second_moment
import usp4_toy_minor_character_decomposition as c2


HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "genus2_high_weight_channel_probe.json"
SECOND_MOMENT_FIXTURE = HERE / "genus2_second_moment_reduction.json"
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"

FROZEN_Q_VALUES = (3, 5, 7)
MAX_SIGNATURES = 23
MAX_EXACT_OPERATIONS = 12_000
MAX_WALL_SECONDS = 2.0

Exponent = tuple[int, int]
Laurent = dict[Exponent, int]
InvariantMonomial = tuple[int, int]  # powers of t=Tr(U) and e=e_2(U)
InvariantPolynomial = dict[InvariantMonomial, int]


CHANNEL_POLYNOMIALS: dict[str, InvariantPolynomial] = {
    "chi_(0,3)": {
        (0, 3): 1,
        (0, 2): -1,
        (2, 1): -2,
        (0, 1): -1,
        (2, 0): 3,
    },
    "chi_(2,2)": {
        (0, 3): -1,
        (2, 2): 1,
        (0, 2): 1,
        (2, 1): -1,
        (0, 1): 1,
        (4, 0): -1,
        (2, 0): 2,
        (0, 0): -1,
    },
    "chi_(0,4)": {
        (0, 4): 1,
        (0, 3): -1,
        (2, 2): -3,
        (0, 2): -2,
        (2, 1): 6,
        (0, 1): 1,
        (4, 0): 1,
        (2, 0): -4,
        (0, 0): 1,
    },
}

CHANNEL_HIGHEST_WEIGHTS = {
    "chi_(0,3)": (3, 3),
    "chi_(2,2)": (4, 2),
    "chi_(0,4)": (4, 4),
}

CHANNEL_DIMENSIONS = {
    "chi_(0,3)": 30,
    "chi_(2,2)": 81,
    "chi_(0,4)": 55,
}

TRIANGULAR_POLYNOMIALS: dict[str, InvariantPolynomial] = {
    # R3=chi_(0,3): its only unproved raw moment is e^3=b^3/q^3.
    "R3": CHANNEL_POLYNOMIALS["chi_(0,3)"],
    # R22=chi_(0,3)+chi_(2,2): e^3 cancels, leaving e^2*t^2.
    "R22": {
        (2, 2): 1,
        (2, 1): -3,
        (4, 0): -1,
        (2, 0): 5,
        (0, 0): -1,
    },
    # R4=H+2*R22=chi04+3*chi22+4*chi03: only e^4 is new.
    "R4": {
        (0, 4): 1,
        (2, 1): -5,
        (4, 0): -2,
        (2, 0): 14,
        (0, 2): -3,
        (0, 0): -2,
    },
}

TRIANGULAR_CHARACTER_COMBINATIONS = {
    "R3": {"chi_(0,3)": 1},
    "R22": {"chi_(0,3)": 1, "chi_(2,2)": 1},
    "R4": {"chi_(0,3)": 4, "chi_(2,2)": 3, "chi_(0,4)": 1},
}

# These exact aggregate sums came from the already frozen q=3,5,7 family
# calculation.  This packet only replays them; it deliberately does not run a
# fourth field or use them as interpolation evidence for a theorem.  Unlike the
# lower moments and K-histograms, these three separate raw sums do not have an
# independently checked-in provenance artifact; they are recorded controls.
FROZEN_RAW_SUMS = {
    3: {"b_cubed": 8_256, "a_squared_b_squared": 8_352, "b_fourth": 45_552},
    5: {
        "b_cubed": 788_080,
        "a_squared_b_squared": 857_040,
        "b_fourth": 8_278_480,
    },
    7: {
        "b_cubed": 14_205_744,
        "a_squared_b_squared": 16_117_248,
        "b_fourth": 221_057_088,
    },
}

EXPECTED_CHANNEL_MEANS = {
    3: {
        "chi_(0,3)": Fraction(74, 3**6),
        "chi_(2,2)": Fraction(37, 3**6),
        "chi_(0,4)": Fraction(-19, 3**7),
    },
    5: {
        "chi_(0,3)": Fraction(614, 5**6),
        "chi_(2,2)": Fraction(213, 5**6),
        "chi_(0,4)": Fraction(-51, 5**7),
    },
    7: {
        "chi_(0,3)": Fraction(2_386, 7**6),
        "chi_(2,2)": Fraction(621, 7**6),
        "chi_(0,4)": Fraction(-99, 7**7),
    },
}


def _normalize_json(value: object) -> object:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [_normalize_json(item) for item in value]
    if isinstance(value, dict):
        return {
            unicodedata.normalize("NFC", str(key)): _normalize_json(item)
            for key, item in value.items()
        }
    return value


def _canonical_bytes(value: object) -> bytes:
    return json.dumps(
        _normalize_json(value),
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _fraction_polynomial_pairs(values: Iterable[Fraction]) -> list[list[int]]:
    return [_fraction_pair(value) for value in values]


def _clean_laurent(value: Mapping[Exponent, int]) -> Laurent:
    return {exponent: coefficient for exponent, coefficient in value.items() if coefficient}


def _laurent_power(
    value: Mapping[Exponent, int], exponent: int, guard: c2.ResourceGuard
) -> Laurent:
    if exponent < 0 or exponent > 8:
        raise ValueError("Laurent exponent must lie in [0,8]")
    result: Laurent = {(0, 0): 1}
    for _ in range(exponent):
        result = c2.multiply(result, value, guard)
    return result


def _expand_invariant_polynomial(
    polynomial: Mapping[InvariantMonomial, int], guard: c2.ResourceGuard
) -> Laurent:
    trace = c2.standard_trace_character()
    exterior_square = c2.standard_exterior_square_character()
    result: Laurent = {}
    for (trace_power, exterior_power), coefficient in sorted(polynomial.items()):
        term = c2.multiply(
            _laurent_power(trace, trace_power, guard),
            _laurent_power(exterior_square, exterior_power, guard),
            guard,
        )
        result = c2.add_scaled(result, term, coefficient, guard)
    return _clean_laurent(result)


def _add_invariant_polynomials(
    terms: Iterable[tuple[int, Mapping[InvariantMonomial, int]]]
) -> InvariantPolynomial:
    result: InvariantPolynomial = {}
    for scalar, polynomial in terms:
        for monomial, coefficient in polynomial.items():
            result[monomial] = result.get(monomial, 0) + scalar * coefficient
    return {monomial: coefficient for monomial, coefficient in result.items() if coefficient}


def _serialize_invariant_polynomial(
    polynomial: Mapping[InvariantMonomial, int]
) -> list[dict[str, int]]:
    return [
        {
            "trace_power": trace_power,
            "exterior_square_power": exterior_power,
            "coefficient": coefficient,
        }
        for (trace_power, exterior_power), coefficient in sorted(polynomial.items())
    ]


def _character_certificate() -> dict[str, object]:
    guard = c2.ResourceGuard()
    engine = c2.C2CharacterEngine(guard)
    channel_laurents: dict[str, Laurent] = {}
    channel_rows: dict[str, object] = {}

    for name in ("chi_(0,3)", "chi_(2,2)", "chi_(0,4)"):
        expanded = _expand_invariant_polynomial(CHANNEL_POLYNOMIALS[name], guard)
        expected = engine.character(CHANNEL_HIGHEST_WEIGHTS[name])
        if expanded != expected:
            raise ArithmeticError(f"invariant-polynomial identity failed for {name}")
        dimension = c2.evaluate_at_identity(expanded)
        if dimension != CHANNEL_DIMENSIONS[name]:
            raise ArithmeticError(f"dimension checksum failed for {name}")
        channel_laurents[name] = expanded
        channel_rows[name] = {
            "highest_weight_e_basis": list(CHANNEL_HIGHEST_WEIGHTS[name]),
            "dimension": dimension,
            "invariant_polynomial_terms": _serialize_invariant_polynomial(
                CHANNEL_POLYNOMIALS[name]
            ),
            "laurent_support_size": len(expanded),
            "status": "EXACT_C2_CHARACTER_IDENTITY",
        }

    expected_triangular = {
        "R3": CHANNEL_POLYNOMIALS["chi_(0,3)"],
        "R22": _add_invariant_polynomials(
            (
                (1, CHANNEL_POLYNOMIALS["chi_(0,3)"]),
                (1, CHANNEL_POLYNOMIALS["chi_(2,2)"]),
            )
        ),
        "R4": _add_invariant_polynomials(
            (
                (4, CHANNEL_POLYNOMIALS["chi_(0,3)"]),
                (3, CHANNEL_POLYNOMIALS["chi_(2,2)"]),
                (1, CHANNEL_POLYNOMIALS["chi_(0,4)"]),
            )
        ),
    }
    if expected_triangular != TRIANGULAR_POLYNOMIALS:
        raise ArithmeticError("triangular invariant-polynomial identities failed")

    triangular_rows: dict[str, object] = {}
    for name, combination in TRIANGULAR_CHARACTER_COMBINATIONS.items():
        expected_laurent: Laurent = {}
        for channel, multiplicity in combination.items():
            expected_laurent = c2.add_scaled(
                expected_laurent, channel_laurents[channel], multiplicity, guard
            )
        expanded = _expand_invariant_polynomial(TRIANGULAR_POLYNOMIALS[name], guard)
        if expanded != expected_laurent:
            raise ArithmeticError(f"triangular Laurent identity failed for {name}")
        triangular_rows[name] = {
            "character_combination": combination,
            "invariant_polynomial_terms": _serialize_invariant_polynomial(
                TRIANGULAR_POLYNOMIALS[name]
            ),
            "dimension_checksum": c2.evaluate_at_identity(expanded),
            "status": "EXACT_POINTWISE_IDENTITY",
        }

    # The middle character has a useful exact factorization.
    factorized_chi22 = (
        "chi_(2,2)=((1-e)^2-t^2)*(t^2-e-1), "
        "where t=Tr(U), e=e_2(U)"
    )
    return {
        "method": "Kostant C2 characters compared coefficientwise as Laurent polynomials",
        "channels": channel_rows,
        "factorization": factorized_chi22,
        "triangular_basis": triangular_rows,
        "resource_counts": guard.snapshot(),
    }


def _load_locked_fixture(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError(f"expected object fixture at {path}")
    claimed = value.get("payload_sha256")
    payload = dict(value)
    payload.pop("payload_sha256", None)
    if claimed != _canonical_sha256(payload):
        raise ValueError(f"payload hash mismatch for {path}")
    return value


def _known_raw_sums(q_family: Mapping[str, object]) -> dict[str, int]:
    moments = q_family.get("moments")
    if not isinstance(moments, dict):
        raise TypeError("q-scan moments are not an object")
    names = {
        "a_squared": "a_squared",
        "a_fourth": "a_fourth",
        "a_squared_b": "a_squared_b",
        "b": "b",
        "b_squared": "b_squared",
    }
    result: dict[str, int] = {}
    for output_name, source_name in names.items():
        row = moments.get(source_name)
        if not isinstance(row, dict) or not isinstance(row.get("sum"), int):
            raise TypeError(f"q-scan moment {source_name} is malformed")
        result[output_name] = int(row["sum"])
    return result


def _channel_values_from_raw_sums(
    q: int,
    member_count: int,
    known: Mapping[str, int],
    new: Mapping[str, int],
) -> dict[str, Fraction]:
    n = member_count
    a2 = known["a_squared"]
    a4 = known["a_fourth"]
    a2b = known["a_squared_b"]
    b1 = known["b"]
    b2 = known["b_squared"]
    b3 = new["b_cubed"]
    a2b2 = new["a_squared_b_squared"]
    b4 = new["b_fourth"]

    chi03_sum = (
        Fraction(b3, q**3)
        - Fraction(b2, q**2)
        - Fraction(2 * a2b, q**2)
        - Fraction(b1, q)
        + Fraction(3 * a2, q)
    )
    chi22_sum = (
        -Fraction(b3, q**3)
        + Fraction(a2b2, q**3)
        + Fraction(b2, q**2)
        - Fraction(a2b, q**2)
        + Fraction(b1, q)
        - Fraction(a4, q**2)
        + Fraction(2 * a2, q)
        - n
    )
    chi04_sum = (
        Fraction(b4, q**4)
        - Fraction(b3, q**3)
        - Fraction(3 * a2b2, q**3)
        - Fraction(2 * b2, q**2)
        + Fraction(6 * a2b, q**2)
        + Fraction(b1, q)
        + Fraction(a4, q**2)
        - Fraction(4 * a2, q)
        + n
    )
    return {
        "chi_(0,3)": chi03_sum / n,
        "chi_(2,2)": chi22_sum / n,
        "chi_(0,4)": chi04_sum / n,
    }


def _candidate_channel_means(q: int) -> dict[str, Fraction]:
    return {
        "chi_(0,3)": Fraction(q**4 - 2 * q - 1, q**6),
        "chi_(2,2)": Fraction(2 * q**3 - q**2 - 2 * q - 2, q**6),
        "chi_(0,4)": -Fraction(2 * q**2 + 1, q**7),
    }


def _candidate_h_mean(q: int) -> Fraction:
    return (
        Fraction(2, q**2)
        + Fraction(2, q**3)
        - Fraction(1, q**4)
        - Fraction(8, q**5)
        - Fraction(4, q**6)
        - Fraction(1, q**7)
    )


def _candidate_second_moment(q: int) -> Fraction:
    return (
        3
        - Fraction(8, q)
        + Fraction(6, q**2)
        + Fraction(8, q**3)
        - Fraction(9, q**4)
        - Fraction(19, q**5)
        - Fraction(4, q**6)
        - Fraction(1, q**7)
    )


def _candidate_raw_means(q: int) -> dict[str, Fraction]:
    return {
        "b_cubed": Fraction(
            4 * q**6
            - 9 * q**5
            + 7 * q**4
            + 8 * q**3
            - 12 * q**2
            - 9 * q
            - 1,
            q**3,
        ),
        "a_squared_b_squared": Fraction(
            (q + 1)
            * (5 * q**5 - 19 * q**4 + 29 * q**3 - 5 * q**2 - 21 * q - 3),
            q**3,
        ),
        "b_fourth": Fraction(
            10 * q**7
            - 29 * q**6
            + 21 * q**5
            + 44 * q**4
            - 47 * q**3
            - 56 * q**2
            - 10 * q
            - 1,
            q**3,
        ),
    }


def _finite_control_rows(
    q_scan: Mapping[str, object], second: Mapping[str, object]
) -> list[dict[str, object]]:
    families = q_scan.get("families")
    finite_checks = second.get("finite_histogram_checks")
    if not isinstance(families, list) or not isinstance(finite_checks, list):
        raise TypeError("bound finite fixtures lost family/check arrays")
    by_q = {int(row["q"]): row for row in families}
    second_by_q = {int(row["q"]): row for row in finite_checks}
    if tuple(sorted(by_q)) != FROZEN_Q_VALUES or tuple(sorted(second_by_q)) != FROZEN_Q_VALUES:
        raise ValueError("bound fixtures lost q=3,5,7 coverage")

    rows: list[dict[str, object]] = []
    for q in FROZEN_Q_VALUES:
        family = by_q[q]
        check = second_by_q[q]
        member_count = int(family["member_count"])
        if member_count != q**4 * (q - 1):
            raise ArithmeticError(f"q={q} member count drifted")
        known = _known_raw_sums(family)
        new = FROZEN_RAW_SUMS[q]
        means = _channel_values_from_raw_sums(q, member_count, known, new)
        if means != EXPECTED_CHANNEL_MEANS[q]:
            raise ArithmeticError(f"q={q} high-weight channel controls drifted")
        candidates = _candidate_channel_means(q)
        if means != candidates:
            raise ArithmeticError(f"q={q} sparse channel candidate lost finite agreement")

        h_mean = means["chi_(0,4)"] + means["chi_(2,2)"] + 2 * means["chi_(0,3)"]
        expected_h = Fraction(*check["normalized_honest_high_weight_packet"])
        if h_mean != expected_h or h_mean != _candidate_h_mean(q):
            raise ArithmeticError(f"q={q} H-packet bridge failed")

        m22 = new["a_squared_b_squared"]
        b4 = new["b_fourth"]
        residual = b4 - 2 * q * m22
        if residual != int(check["unresolved_B4_minus_2qM22"]):
            raise ArithmeticError(f"q={q} raw second-moment bridge failed")
        second_mean = Fraction(*check["normalized_second_moment_Z"])
        if second_mean != _candidate_second_moment(q):
            raise ArithmeticError(f"q={q} second-moment candidate lost finite agreement")

        raw_candidates = _candidate_raw_means(q)
        raw_means = {
            name: Fraction(total, member_count) for name, total in new.items()
        }
        if raw_means != raw_candidates:
            raise ArithmeticError(f"q={q} raw sparse candidate lost finite agreement")

        rows.append(
            {
                "q": q,
                "member_count": member_count,
                "frozen_new_raw_sums": dict(new),
                "channel_means": {
                    name: _fraction_pair(value) for name, value in means.items()
                },
                "H_mean": _fraction_pair(h_mean),
                "second_moment": _fraction_pair(second_mean),
                "raw_candidate_means": {
                    name: _fraction_pair(value) for name, value in raw_means.items()
                },
                "all_internal_bridges_match": True,
            }
        )
    return rows


def _aggregate_signature_polynomials(
    signatures: Sequence[Mapping[str, object]],
) -> tuple[dict[int, list[Fraction]], dict[int, int]]:
    totals: dict[int, list[Fraction]] = defaultdict(list)
    counts: Counter[int] = Counter()
    for row in signatures:
        radical = row["odd_radical"]
        type_count = row["type_count"]
        if not isinstance(radical, dict) or not isinstance(type_count, dict):
            raise TypeError("signature row lost nested data")
        degree = int(radical["degree"])
        counts[degree] += 1
        coefficients = [
            Fraction(*pair) * int(row["tuple_weight"])
            for pair in type_count["coefficients_low_to_high"]
        ]
        if len(totals[degree]) < len(coefficients):
            totals[degree].extend(
                [Fraction(0)] * (len(coefficients) - len(totals[degree]))
            )
        for index, coefficient in enumerate(coefficients):
            totals[degree][index] += coefficient
    return dict(totals), dict(counts)


def _b3_signature_certificate() -> dict[str, object]:
    clock = time.monotonic
    budget = second_moment.Budget(
        MAX_EXACT_OPERATIONS, clock() + MAX_WALL_SECONDS, clock
    )
    block = second_moment._build_signature_block(
        "B3",
        quadratic_slots=3,
        slot_kinds=("Q", "Q", "Q"),
        expected_count=MAX_SIGNATURES,
        total_degree=6,
        budget=budget,
    )
    signatures = block["signatures"]
    if not isinstance(signatures, list) or len(signatures) != MAX_SIGNATURES:
        raise ArithmeticError("B3 signature count is not 23")
    totals, counts = _aggregate_signature_polynomials(signatures)
    expected_counts = {0: 4, 2: 10, 4: 5, 6: 4}
    expected_totals = {
        0: [0, 2, -6, 5],
        2: [0, -16, 40, -36, 12],
        4: [0, 30, -70, 63, -29, 6],
        6: [0, -16, 36, -32, 17, -6, 1],
    }
    if counts != expected_counts:
        raise ArithmeticError("B3 radical-degree census drifted")
    integer_totals: dict[int, list[int]] = {}
    for degree, coefficients in totals.items():
        if any(value.denominator != 1 for value in coefficients):
            raise ArithmeticError("B3 aggregate polynomial is not integral")
        integer_totals[degree] = [value.numerator for value in coefficients]
    if integer_totals != expected_totals:
        raise ArithmeticError("B3 aggregate conductor polynomials drifted")

    generic: list[dict[str, object]] = []
    expected_mixture = [Fraction(1, 8), Fraction(3, 8), Fraction(3, 8), Fraction(1, 8)]
    for row in signatures:
        radical = row["odd_radical"]
        if not isinstance(radical, dict) or int(radical["degree"]) != 6:
            continue
        type_count = row["type_count"]
        if not isinstance(type_count, dict):
            raise TypeError("B3 generic signature lost type-count data")
        coefficients = [Fraction(*pair) for pair in type_count["coefficients_low_to_high"]]
        linear_count = int(radical["linear_prime_count"])
        quadratic_count = int(radical["quadratic_prime_count"])
        p1_coefficient_constant = linear_count * (linear_count + 1) // 2 + quadratic_count
        generic.append(
            {
                "signature": row["signature"],
                "leading_mixture_weight": _fraction_pair(
                    coefficients[-1] * int(row["tuple_weight"])
                ),
                "linear_prime_count": linear_count,
                "quadratic_prime_count": quadratic_count,
                "S5_p1_coefficient": f"{p1_coefficient_constant}-q^2",
                "S5_p2_coefficient": f"q-{linear_count}",
            }
        )
    actual_mixture = [Fraction(*row["leading_mixture_weight"]) for row in generic]
    if actual_mixture != expected_mixture or sum(actual_mixture) != 1:
        raise ArithmeticError("B3 generic leading mixture drifted")
    if any(
        row["S5_p1_coefficient"] == "0" or row["S5_p2_coefficient"] == "0"
        for row in generic
    ):
        raise ArithmeticError("generic primitive coefficient unexpectedly vanished")

    compact_signatures = [
        {
            "signature": row["signature"],
            "tuple_weight": row["tuple_weight"],
            "radical_degree": row["odd_radical"]["degree"],
            "type_count_coefficients_low_to_high": row["type_count"][
                "coefficients_low_to_high"
            ],
        }
        for row in signatures
    ]
    return {
        "status": "EXACT_SIGNATURE_ROADMAP_PRIMITIVE_AVERAGES_UNRESOLVED",
        "signature_count": len(signatures),
        "signature_count_derivation": "11+5+4+3=23",
        "weighted_tuple_count_formula": "q^6",
        "radical_degree_signature_counts": {str(k): v for k, v in counts.items()},
        "radical_degree_tuple_polynomials_low_to_high": {
            str(k): _fraction_polynomial_pairs(v) for k, v in totals.items()
        },
        "generic_degree_six_rows": generic,
        "generic_mixture": "(1,3,3,1)/8",
        "signature_level_cancellation_result": (
            "FAILED: all four generic conductor types retain nonzero p1 and p2 "
            "coefficients; an averaged primitive-trace identity is genuinely required"
        ),
        "primitive_normalization": (
            "For degree-six r, L_r=(1-u)(1+p1*u+p2*u^2+q*p1*u^3+q^2*u^4); "
            "S5 has p1 coefficient -q^2+binom(l+1,2)+k and p2 coefficient q-l"
        ),
        "signatures": compact_signatures,
        "exact_operations_used": budget.operations,
    }


def _source_locks(
    q_scan: Mapping[str, object], second: Mapping[str, object]
) -> dict[str, object]:
    return {
        "q_scan_fixture": {
            "path": "research/l-families/atlas/function_field/genus2_q_scan.json",
            "canonical_sha256": _canonical_sha256(q_scan),
            "payload_sha256": q_scan["payload_sha256"],
        },
        "second_moment_fixture": {
            "path": (
                "research/l-families/atlas/function_field/"
                "genus2_second_moment_reduction.json"
            ),
            "canonical_sha256": _canonical_sha256(second),
            "payload_sha256": second["payload_sha256"],
        },
        "second_moment_generator": {
            "path": (
                "research/l-families/atlas/function_field/"
                "genus2_second_moment_reduction.py"
            ),
            "sha256_lf_normalized": _lf_normalized_sha256(
                Path(second_moment.__file__).resolve()
            ),
        },
        "C2_character_generator": {
            "path": (
                "research/l-families/atlas/function_field/"
                "usp4_toy_minor_character_decomposition.py"
            ),
            "sha256_lf_normalized": _lf_normalized_sha256(Path(c2.__file__).resolve()),
        },
        "probe_generator": {
            "path": (
                "research/l-families/atlas/function_field/"
                "genus2_high_weight_channel_probe.py"
            ),
            "sha256_lf_normalized": _lf_normalized_sha256(Path(__file__).resolve()),
        },
    }


def build_fixture() -> dict[str, object]:
    q_scan = _load_locked_fixture(Q_SCAN_FIXTURE)
    second = _load_locked_fixture(SECOND_MOMENT_FIXTURE)
    character_certificate = _character_certificate()
    b3_signatures = _b3_signature_certificate()
    finite_rows = _finite_control_rows(q_scan, second)

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_high_weight_channel_probe.v1",
        "status": "DRAFT_EXACT_TRIANGULAR_REDUCTION_WITH_UNPROVED_SPARSE_CANDIDATE",
        "scope": (
            "exact C2 and factor-signature algebra for every odd q; finite aggregate "
            "controls only at q=3,5,7; no field enumeration in this generator"
        ),
        "definition": (
            "For t=Tr(U), e=e_2(U), a_D/sqrt(q)=-t, b_D/q=e, split "
            "H=chi_(0,4)+chi_(2,2)+2*chi_(0,3) into raw-moment-aligned packets."
        ),
        "source_locks": _source_locks(q_scan, second),
        "character_certificate": character_certificate,
        "triangular_raw_moment_bridge": {
            "status": "EXACT_POINTWISE_FOR_EVERY_FAMILY_MEMBER",
            "R3": {
                "character": "chi_(0,3)",
                "only_new_raw_moment": "b_D^3",
                "identity": (
                    "R3=e^3-e^2-2*e*t^2-e+3*t^2"
                ),
            },
            "R22": {
                "character": "chi_(0,3)+chi_(2,2)",
                "only_new_raw_moment": "a_D^2*b_D^2",
                "identity": "R22=e^2*t^2-3*e*t^2-t^4+5*t^2-1",
            },
            "R4": {
                "character": "chi_(0,4)+3*chi_(2,2)+4*chi_(0,3)",
                "only_new_raw_moment": "b_D^4",
                "identity": "R4=e^4-5*e*t^2-2*t^4+14*t^2-3*e^2-2",
            },
            "interpretation": (
                "This is an invertible triangular organization of the three missing "
                "raw moments; it does not evaluate any of their family averages."
            ),
        },
        "b_cubed_signature_roadmap": b3_signatures,
        "finite_aggregate_controls": finite_rows,
        "sparse_all_q_candidate": {
            "status": "CONJECTURE_MATCHING_ONLY_Q3_Q5_Q7_NOT_INTERPOLATION_THEOREM",
            "channel_means": {
                "chi_(0,3)": "(q^4-2*q-1)/q^6",
                "chi_(2,2)": "(2*q^3-q^2-2*q-2)/q^6",
                "chi_(0,4)": "-(2*q^2+1)/q^7",
            },
            "implied_raw_means": {
                "b_D^3": (
                    "(4*q^6-9*q^5+7*q^4+8*q^3-12*q^2-9*q-1)/q^3"
                ),
                "a_D^2*b_D^2": (
                    "(q+1)*(5*q^5-19*q^4+29*q^3-5*q^2-21*q-3)/q^3"
                ),
                "b_D^4": (
                    "(10*q^7-29*q^6+21*q^5+44*q^4-47*q^3-56*q^2-10*q-1)/q^3"
                ),
            },
            "implied_H_mean": (
                "2/q^2+2/q^3-1/q^4-8/q^5-4/q^6-1/q^7"
            ),
            "implied_second_moment": (
                "3-8/q+6/q^2+8/q^3-9/q^4-19/q^5-4/q^6-1/q^7"
            ),
            "implied_H_rescaled_limit": 2,
            "affine_quotient_trace_normalization": {
                "exact_measure_identity": (
                    "For an affine-invariant weight-w character, define "
                    "T_lambda(q)=q^(w/2)/(q*(q-1))*sum_(D in H_5(q)) chi_lambda(D)."
                ),
                "candidate_T_(0,3)": "q^4-2*q-1",
                "candidate_T_(2,2)": "2*q^3-q^2-2*q-2",
                "candidate_T_(0,4)": "-(2*q^2+1)",
                "geometric_handoff": (
                    "The quotient [H_5/AGL_1] is the branch-configuration model "
                    "with infinity marked.  Identifying its normalized character sum "
                    "with a precise marked-Weierstrass local-system trace, including "
                    "the central hyperelliptic involution convention, is a proposed "
                    "cohomological route and is not certified here."
                ),
            },
            "relation_to_previous_9_over_4_nomination": (
                "If proved, this structured channelwise candidate would replace the "
                "three-field 9/4 nomination by 2; neither constant is currently a theorem."
            ),
        },
        "failed_attempt_ledger": [
            {
                "attempt": "Cancel degree-six primitive coefficients signature by signature in b_D^3",
                "result": "FAILED_EXACTLY",
                "evidence": (
                    "The four generic rows have p1 coefficients 21-q^2, 11-q^2, "
                    "5-q^2, 3-q^2 and p2 coefficients q-6, q-4, q-2, q."
                ),
            },
            {
                "attempt": "Infer an eta_q=chi_q(-1) branch from q=3,5,7",
                "result": "UNDERDETERMINED",
                "evidence": (
                    "Only q=5 lies in the eta_q=+1 branch; no branch formula is fitted."
                ),
            },
            {
                "attempt": "Promote sparse rational functions from three fields",
                "result": "REJECTED_AS_PROOF",
                "evidence": (
                    "Primitive p1,p2 averages can carry genuine Frobenius traces; three "
                    "specializations cannot exclude them."
                ),
            },
        ],
        "next_exact_lemmas": [
            {
                "name": "B3-PRIMITIVE-TRACE-AVERAGE",
                "target": (
                    "Evaluate the p1,p2 and deletion-character averages across the 23 B3 "
                    "signatures; this decides mean(chi_(0,3))."
                ),
            },
            {
                "name": "M22-TRIANGULAR-TRACE-AVERAGE",
                "target": (
                    "Evaluate the 20 M22 signatures in the R22 combination; this decides "
                    "mean(chi_(0,3)+chi_(2,2))."
                ),
            },
            {
                "name": "B4-TRIANGULAR-TRACE-AVERAGE",
                "target": (
                    "Evaluate the 54 B4 signatures in R4; this decides the remaining "
                    "chi_(0,4) channel after R3 and R22."
                ),
            },
        ],
        "resource_contract": {
            "field_enumeration": "FORBIDDEN_AND_NOT_IMPORTED",
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "maximum_B3_signatures": MAX_SIGNATURES,
            "actual_B3_signatures": b3_signatures["signature_count"],
            "maximum_exact_signature_operations": MAX_EXACT_OPERATIONS,
            "exact_signature_operations_used": b3_signatures["exact_operations_used"],
            "maximum_signature_wall_seconds": MAX_WALL_SECONDS,
            "numeric_approximation": "NONE",
            "external_computer_algebra": "NONE",
        },
        "firewalls": [
            "The triangular character identities are exact; the sparse all-q formulas are not proved.",
            "The q=3,5,7 aggregate rows are regression controls, not interpolation data for a theorem.",
            "The three separate high raw sums are frozen one-time controls without an independently replayable provenance artifact.",
            "The B3 signature packet proves that generic primitive coefficients survive; it does not average them.",
            "No eta_q branch is proved or excluded by the three frozen fields.",
            "No effective equidistribution, number-field transfer, RH, or GRH conclusion is asserted.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--write", type=Path)
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        stored = json.loads(args.check.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"high-weight channel fixture mismatch: {args.check}")
        print(f"OK: high-weight channel fixture matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(
            json.dumps(fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote high-weight channel fixture {args.write}")
        return 0
    print(json.dumps(fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
