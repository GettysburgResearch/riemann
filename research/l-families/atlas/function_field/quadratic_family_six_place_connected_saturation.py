#!/usr/bin/env python3
"""Prove the symbolic six-place connected-correlation identity.

The replay source-locks the committed multi-place packet, expands one
degree-five coefficient, and visits the 203 set partitions of six labels.
It performs no finite-field, polynomial-family, curve, or zero enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb, factorial
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_six_place_connected_saturation.json"
NOTE = HERE / "QUADRATIC_FAMILY_SIX_PLACE_CONNECTED_SATURATION.md"
TEST = ROOT / "tests" / "test_quadratic_family_six_place_connected_saturation.py"
SOURCE = HERE / "quadratic_family_multiplace_l_function_identity.json"
SOURCE_COMMIT = "c94466e28a48ec429150f63de6d334d4c4f60110"
SOURCE_BLOB = "f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e"
SOURCE_LF_SHA256 = "b4529c82d40575593e4c346e4cdfa0aaee417618886b5b1ab448c2469c87ca9e"
SOURCE_PAYLOAD_SHA256 = (
    "ddd7332102007ceda079e7b85dd0a482642c3d999dac779dde220af4e3b27c7d"
)
SOURCE_BYTES = 10_738
SCHEMA = "riemann.function_field.quadratic_family_six_place_connected_saturation.v1"

MAX_LABELS = 6
MAX_SET_PARTITIONS = 203
MAX_CENTERED_PARTITIONS = 41
MAX_FIXED_M_REPLAY = 9
MAX_INTEGER_PARTITION_PROFILES = 32
MAX_SYMBOLIC_TERMS = 64
MAX_SOURCE_BYTES = 16_384
MAX_OUTPUT_BYTES = 32_768
WALL_SECONDS = 4.0

# Sparse polynomials in (q,t,b), keyed by the corresponding exponents.
Monomial: TypeAlias = tuple[int, int, int]
Expr: TypeAlias = dict[Monomial, int]
Partition: TypeAlias = tuple[tuple[int, ...], ...]
QPoly: TypeAlias = dict[int, int]
WeightExpr: TypeAlias = dict[tuple[int, int], int]


def _clean(expression: Expr) -> Expr:
    return {
        monomial: coefficient
        for monomial, coefficient in expression.items()
        if coefficient
    }


def _add(left: Expr, right: Expr) -> Expr:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    result = _clean(result)
    if len(result) > MAX_SYMBOLIC_TERMS:
        raise RuntimeError("symbolic-term cap exceeded")
    return result


def _scale(expression: Expr, scalar: int) -> Expr:
    return _clean(
        {monomial: scalar * coefficient for monomial, coefficient in expression.items()}
    )


def _mul(left: Expr, right: Expr) -> Expr:
    result: Expr = {}
    for (q_left, t_left, b_left), left_coefficient in left.items():
        for (q_right, t_right, b_right), right_coefficient in right.items():
            monomial = (
                q_left + q_right,
                t_left + t_right,
                b_left + b_right,
            )
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
    result = _clean(result)
    if len(result) > MAX_SYMBOLIC_TERMS:
        raise RuntimeError("symbolic-term cap exceeded")
    return result


def _q_minus(integer: int) -> Expr:
    return {(1, 0, 0): 1, (0, 0, 0): -integer}


def formal_six_place_raw_sum() -> Expr:
    """Derive S_(5,6) from the locked general degree-five formula."""
    minus_one: Expr = {(0, 0, 0): -1}
    minus_t: Expr = {(0, 1, 0): -1}
    minus_b: Expr = {(0, 0, 1): -1}
    minus_qt: Expr = {(1, 1, 0): -1}
    minus_q_squared: Expr = {(2, 0, 0): -1}

    # P=1-tu+bu^2-qtu^3+q^2u^4 and L=(1-u)P.
    l_1 = _add(minus_t, minus_one)
    l_3 = _add(minus_qt, minus_b)
    l_5 = minus_q_squared

    # S_(5,m)=(binom(m+1,2)-q*m)l_1+(m-q)l_3+l_5 at m=6.
    first_coefficient: Expr = {(0, 0, 0): 21, (1, 0, 0): -6}
    second_coefficient = _scale(_q_minus(6), -1)
    return _add(
        _add(_mul(first_coefficient, l_1), _mul(second_coefficient, l_3)),
        l_5,
    )


EXPECTED_RAW_SUM: Expr = {
    (2, 1, 0): 1,
    (0, 1, 0): -21,
    (1, 0, 1): 1,
    (0, 0, 1): -6,
    (2, 0, 0): -1,
    (1, 0, 0): 6,
    (0, 0, 0): -21,
}


def evaluate_expression(expression: Expr, q: int, trace: int, middle: int) -> int:
    return sum(
        coefficient * q**q_power * trace**trace_power * middle**middle_power
        for (q_power, trace_power, middle_power), coefficient in expression.items()
    )


def raw_six_place_sum(q: int, trace: int, middle: int) -> int:
    if q < 7 or q % 2 == 0:
        raise ValueError("six distinct finite places require odd q >= 7")
    return (q**2 - 21) * trace + (q - 6) * middle - q**2 + 6 * q - 21


def six_place_character_expansion() -> WeightExpr:
    """Substitute t=sqrt(q)*chi_1 and b=q*(chi_2+1) exactly."""
    result: WeightExpr = {}
    for (
        q_power,
        trace_power,
        middle_power,
    ), coefficient in EXPECTED_RAW_SUM.items():
        if (trace_power, middle_power) == (1, 0):
            key = (2 * q_power + 1, 1)
            result[key] = result.get(key, 0) + coefficient
        elif (trace_power, middle_power) == (0, 1):
            twice_q_exponent = 2 * (q_power + 1)
            for fundamental_index in (2, 0):
                key = (twice_q_exponent, fundamental_index)
                result[key] = result.get(key, 0) + coefficient
        elif (trace_power, middle_power) == (0, 0):
            key = (2 * q_power, 0)
            result[key] = result.get(key, 0) + coefficient
        else:
            raise ArithmeticError("unexpected nonlinear six-place raw monomial")
    return {key: coefficient for key, coefficient in result.items() if coefficient}


EXPECTED_SIX_PLACE_CHARACTER: WeightExpr = {
    (5, 1): 1,
    (1, 1): -21,
    (4, 2): 1,
    (2, 2): -6,
    (0, 0): -21,
}


def raw_six_place_sum_from_second_power(
    q: int, trace: int, second_power_trace: int
) -> Fraction:
    """Rewrite b=(t^2-s_2)/2 without evaluating an extension field."""
    return Fraction((q**2 - 21) * trace - q**2 + 6 * q - 21) + Fraction(
        (q - 6) * (trace**2 - second_power_trace), 2
    )


def four_place_sum(q: int, trace: int) -> int:
    return q**2 - 10 + (4 * q - 10) * trace


def _set_partitions(labels: tuple[int, ...]) -> tuple[Partition, ...]:
    if len(labels) > MAX_LABELS:
        raise ValueError("set-partition replay is capped at six labels")
    if not labels:
        return ((),)
    first, rest = labels[0], labels[1:]
    result: list[Partition] = []
    for partition in _set_partitions(rest):
        result.append(((first,),) + partition)
        for index, block in enumerate(partition):
            updated = list(partition)
            updated[index] = (first,) + block
            result.append(tuple(updated))
    if len(result) > MAX_SET_PARTITIONS:
        raise RuntimeError("set-partition cap exceeded")
    return tuple(result)


def partition_profile_rows() -> list[dict[str, int | list[int]]]:
    partitions = _set_partitions(tuple(range(MAX_LABELS)))
    profiles = Counter(
        tuple(sorted(len(block) for block in partition))
        for partition in partitions
        if all(len(block) >= 2 for block in partition)
    )
    rows: list[dict[str, int | list[int]]] = []
    for profile, count in sorted(profiles.items()):
        blocks = len(profile)
        per_partition = (-1) ** (blocks - 1) * factorial(blocks - 1)
        rows.append(
            {
                "profile": list(profile),
                "partition_count": count,
                "per_partition_cumulant_coefficient": per_partition,
                "aggregate_coefficient_if_moments_equal": count * per_partition,
            }
        )
    return rows


def partition_channel_index() -> dict[str, object]:
    four_two: list[dict[str, list[int]]] = []
    three_three: list[dict[str, list[int]]] = []
    pair_matchings: list[list[list[int]]] = []
    centered = 0
    for partition in _set_partitions(tuple(range(MAX_LABELS))):
        if any(len(block) == 1 for block in partition):
            continue
        centered += 1
        profile = tuple(sorted(len(block) for block in partition))
        if profile == (2, 4):
            pair = next(block for block in partition if len(block) == 2)
            quadruple = next(block for block in partition if len(block) == 4)
            four_two.append({"pair": list(pair), "quadruple": list(quadruple)})
        elif profile == (3, 3):
            blocks = sorted(partition)
            three_three.append(
                {"triple": list(blocks[0]), "complement": list(blocks[1])}
            )
        elif profile == (2, 2, 2):
            pair_matchings.append([list(block) for block in sorted(partition)])

    if centered != MAX_CENTERED_PARTITIONS:
        raise ArithmeticError("centered partition count drifted")
    if (len(four_two), len(three_three), len(pair_matchings)) != (15, 10, 15):
        raise ArithmeticError("partition-channel multiplicities drifted")
    if len({tuple(row["quadruple"]) for row in four_two}) != 15:
        raise ArithmeticError("four-subset indexing drifted")
    if len({tuple(row["triple"]) for row in three_three}) != 10:
        raise ArithmeticError("complementary-triple indexing drifted")
    if (
        len({tuple(tuple(pair) for pair in matching) for matching in pair_matchings})
        != 15
    ):
        raise ArithmeticError("perfect-matching indexing drifted")
    return {
        "four_plus_two": four_two,
        "three_plus_three_unordered": three_three,
        "three_pairs": pair_matchings,
        "centered_partition_count": centered,
    }


def _required_subsets() -> tuple[
    tuple[tuple[int, ...], ...], tuple[tuple[int, ...], ...]
]:
    return tuple(combinations(range(6), 3)), tuple(combinations(range(6), 4))


def closed_connected_cumulant(
    q: int,
    full_trace: int,
    full_middle: int,
    triple_traces: dict[tuple[int, ...], int],
    quadruple_traces: dict[tuple[int, ...], int],
) -> Fraction:
    if q < 7 or q % 2 == 0:
        raise ValueError("six distinct finite places require odd q >= 7")
    triples, quadruples = _required_subsets()
    missing = sorted(
        (set(triples).difference(triple_traces))
        | (set(quadruples).difference(quadruple_traces))
    )
    if missing:
        raise ValueError(f"missing formal subset traces: {missing!r}")
    family_size = q**4 * (q - 1)
    pair_sum = 2 * q - 3
    raw = raw_six_place_sum(q, full_trace, full_middle)
    four_sum = sum(four_place_sum(q, quadruple_traces[subset]) for subset in quadruples)
    triple_products = sum(
        triple_traces[tuple(row["triple"])] * triple_traces[tuple(row["complement"])]
        for row in partition_channel_index()["three_plus_three_unordered"]
    )
    return (
        Fraction(raw, family_size)
        - Fraction(pair_sum * four_sum, family_size**2)
        - Fraction(9 * (q - 2) ** 2 * triple_products, family_size**2)
        + Fraction(30 * pair_sum**3, family_size**3)
    )


def partition_connected_cumulant(
    q: int,
    full_trace: int,
    full_middle: int,
    triple_traces: dict[tuple[int, ...], int],
    quadruple_traces: dict[tuple[int, ...], int],
) -> Fraction:
    """Evaluate the joint-cumulant partition formula from formal moments."""
    family_size = q**4 * (q - 1)
    pair_sum = 2 * q - 3
    result = Fraction(0)
    for partition in _set_partitions(tuple(range(6))):
        if any(len(block) == 1 for block in partition):
            continue
        coefficient = (-1) ** (len(partition) - 1) * factorial(len(partition) - 1)
        product_moment = Fraction(1)
        for block in partition:
            subset = tuple(block)
            if len(block) == 2:
                moment = Fraction(pair_sum, family_size)
            elif len(block) == 3:
                moment = Fraction(3 * (q - 2) * triple_traces[subset], family_size)
            elif len(block) == 4:
                moment = Fraction(
                    four_place_sum(q, quadruple_traces[subset]), family_size
                )
            elif len(block) == 6:
                moment = Fraction(
                    raw_six_place_sum(q, full_trace, full_middle), family_size
                )
            else:
                raise ArithmeticError("unexpected centered partition block")
            product_moment *= moment
        result += coefficient * product_moment
    return result


def hasse_envelope_coefficients(q: int) -> dict[str, Fraction | int]:
    """Return exact coefficients for the conservative six-place envelopes."""
    if q < 7 or q % 2 == 0:
        raise ValueError("six distinct finite places require odd q >= 7")
    family_size = q**4 * (q - 1)
    pair_sum = 2 * q - 3
    return {
        "family_size": family_size,
        "pair_sum": pair_sum,
        "raw_omega_1_sqrt_q_coefficient": Fraction(4 * (q**2 - 21), family_size),
        "raw_omega_2_and_constant_bound": Fraction(
            5 * (q**2 - 6 * q) + 21, family_size
        ),
        "four_plus_two_universal_bound": Fraction(
            15 * pair_sum * (q**2 - 10), family_size**2
        ),
        "four_plus_two_elliptic_sqrt_q_coefficient": Fraction(
            30 * pair_sum * (4 * q - 10), family_size**2
        ),
        "three_plus_three_bound": Fraction(360 * q * (q - 2) ** 2, family_size**2),
        "pair_cube": Fraction(30 * pair_sum**3, family_size**3),
    }


def inverse_root_coefficient_envelope(m: int, degree: int) -> tuple[int, Fraction]:
    """Return binom(m-1,j) and the q exponent j/2 for |ell_j|."""
    if m < 5 or not 0 <= degree <= m - 1:
        raise ValueError("fixed-m replay requires m>=5 and 0<=degree<=m-1")
    return comb(m - 1, degree), Fraction(degree, 2)


def _integer_partition_profiles(
    total: int, minimum: int = 2
) -> tuple[tuple[int, ...], ...]:
    if total > MAX_FIXED_M_REPLAY:
        raise ValueError("sharper correction replay is capped at m=9")
    if total == 0:
        return ((),)
    rows: list[tuple[int, ...]] = []
    for first in range(minimum, total + 1):
        for tail in _integer_partition_profiles(total - first, first):
            rows.append((first,) + tail)
    if len(rows) > MAX_INTEGER_PARTITION_PROFILES:
        raise RuntimeError("integer-partition profile cap exceeded")
    return tuple(rows)


def centered_block_weight(size: int) -> Fraction:
    if size == 2:
        return Fraction(4)
    if size == 3:
        return Fraction(7, 2)
    if size == 4:
        return Fraction(3)
    if size >= 5:
        return Fraction(5, 2)
    raise ValueError("singleton blocks vanish and have no centered weight")


def proper_partition_correction_exponent(m: int) -> Fraction:
    """Return the sharp exponent from the declared block-envelope ledger."""
    if not 5 <= m <= MAX_FIXED_M_REPLAY:
        raise ValueError("sharper correction replay is restricted to 5<=m<=9")
    profiles = [
        profile for profile in _integer_partition_profiles(m) if len(profile) >= 2
    ]
    if not profiles:
        raise ArithmeticError("no proper centered partition profile")
    return min(
        sum((centered_block_weight(size) for size in profile), Fraction())
        for profile in profiles
    )


def symplectic_top_weight_channel(genus: int) -> dict[int, int]:
    """Reduce e_3-e_5 using e_(2g-j)=e_j and e_j=0 outside 0..2g."""
    if genus < 2:
        raise ValueError("the top-weight classification starts at genus two")

    def reduced_index(index: int) -> int | None:
        if index > 2 * genus:
            return None
        return min(index, 2 * genus - index)

    result: dict[int, int] = {}
    for index, coefficient in ((3, 1), (5, -1)):
        reduced = reduced_index(index)
        if reduced is not None:
            result[reduced] = result.get(reduced, 0) + coefficient
    return {index: coefficient for index, coefficient in result.items() if coefficient}


def degree_five_p_coefficient_polynomials(m: int) -> dict[int, QPoly]:
    """Return the exact S_(5,m) expansion in the coefficients p_j of P."""
    if m < 5:
        raise ValueError("the weight-ceiling expansion starts at m=5")
    triangular = m * (m + 1) // 2
    first: QPoly = {0: triangular, 1: -m}
    third: QPoly = {0: m, 1: -1}
    if m % 2:
        return {1: first, 3: third, 5: {0: 1}}
    return {
        0: {0: -triangular, 1: m},
        1: first,
        2: {0: -m, 1: 1},
        3: third,
        4: {0: -1},
        5: {0: 1},
    }


def _add_qpoly(left: QPoly, right: QPoly) -> QPoly:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
    return {
        exponent: coefficient for exponent, coefficient in result.items() if coefficient
    }


def genus_four_reduced_p_expansion(m: int) -> dict[int, QPoly]:
    """Apply p_5=q*p_3 for the genus-four rows m=9,10."""
    if m not in {9, 10}:
        raise ValueError("the explicit genus-four notch rows are m=9,10")
    coefficients = degree_five_p_coefficient_polynomials(m)
    p_five = coefficients.pop(5)
    shifted = {exponent + 1: value for exponent, value in p_five.items()}
    coefficients[3] = _add_qpoly(coefficients[3], shifted)
    return coefficients


def _elementary_to_fundamental(expression: WeightExpr) -> WeightExpr:
    """Use e_j=chi_(omega_j)+chi_(omega_(j-2))+... symbolically."""
    result: WeightExpr = {}
    for (twice_q_exponent, elementary_index), coefficient in expression.items():
        for fundamental_index in range(elementary_index, -1, -2):
            key = (twice_q_exponent, fundamental_index)
            result[key] = result.get(key, 0) + coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def genus_four_character_expansion(m: int) -> WeightExpr:
    """Return the exact m=9 or m=10 row in q^(1/2)-weight coordinates."""
    elementary: WeightExpr = {}
    for index, polynomial in genus_four_reduced_p_expansion(m).items():
        sign = -1 if index % 2 else 1
        for q_exponent, coefficient in polynomial.items():
            key = (2 * q_exponent + index, index)
            elementary[key] = elementary.get(key, 0) + sign * coefficient
    return _elementary_to_fundamental(elementary)


def _canonical_sha256(payload: dict[str, object]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()


def _file_sha256(path: Path) -> str:
    return _lf_sha256(path.read_bytes())


def _git_blob(path: Path, commit: str) -> str:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "rev-parse", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _git_file(path: Path, commit: str) -> bytes:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{commit}:{relative}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return result.stdout


def load_locked_source() -> dict[str, object]:
    if _git_blob(SOURCE, SOURCE_COMMIT) != SOURCE_BLOB:
        raise RuntimeError("multi-place source git blob drifted")
    source_bytes = _git_file(SOURCE, SOURCE_COMMIT)
    if len(source_bytes) > MAX_SOURCE_BYTES:
        raise RuntimeError("source-byte cap exceeded")
    if len(source_bytes) != SOURCE_BYTES:
        raise RuntimeError("multi-place source byte count drifted")
    if _lf_sha256(source_bytes) != SOURCE_LF_SHA256:
        raise RuntimeError("multi-place source LF hash drifted")
    payload = json.loads(source_bytes.decode("utf-8"))
    claimed = payload.get("payload_sha256")
    without_hash = dict(payload)
    without_hash.pop("payload_sha256", None)
    if claimed != SOURCE_PAYLOAD_SHA256 or _canonical_sha256(without_hash) != claimed:
        raise RuntimeError("multi-place source payload lock failed")
    if (
        payload.get("schema")
        != "riemann.function_field.quadratic_family_multiplace_l_function_identity.v1"
    ):
        raise RuntimeError("multi-place source schema drifted")
    exact = payload.get("exact_identity")
    if not isinstance(exact, dict) or exact.get("degree_five_coefficient") != (
        "S_5,m=(binom(m+1,2)-q*m)*l_1+(m-q)*l_3+l_5"
    ):
        raise RuntimeError("locked degree-five coefficient theorem drifted")
    return payload


def _sparse_rows(expression: Expr) -> list[dict[str, int]]:
    return [
        {
            "q_power": q_power,
            "trace_power": trace_power,
            "middle_coefficient_power": middle_power,
            "coefficient": coefficient,
        }
        for (q_power, trace_power, middle_power), coefficient in sorted(
            expression.items()
        )
    ]


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    source = load_locked_source()
    formal = formal_six_place_raw_sum()
    if formal != EXPECTED_RAW_SUM:
        raise ArithmeticError(f"six-place raw sum drifted: {formal!r}")
    six_place_character = six_place_character_expansion()
    if six_place_character != EXPECTED_SIX_PLACE_CHARACTER:
        raise ArithmeticError(
            f"six-place character expansion drifted: {six_place_character!r}"
        )
    if raw_six_place_sum_from_second_power(7, 5, 3) != raw_six_place_sum(7, 5, 11):
        raise ArithmeticError("second-power trace reformulation drifted")

    rows = partition_profile_rows()
    expected_rows = [
        {
            "profile": [2, 2, 2],
            "partition_count": 15,
            "per_partition_cumulant_coefficient": 2,
            "aggregate_coefficient_if_moments_equal": 30,
        },
        {
            "profile": [2, 4],
            "partition_count": 15,
            "per_partition_cumulant_coefficient": -1,
            "aggregate_coefficient_if_moments_equal": -15,
        },
        {
            "profile": [3, 3],
            "partition_count": 10,
            "per_partition_cumulant_coefficient": -1,
            "aggregate_coefficient_if_moments_equal": -10,
        },
        {
            "profile": [6],
            "partition_count": 1,
            "per_partition_cumulant_coefficient": 1,
            "aggregate_coefficient_if_moments_equal": 1,
        },
    ]
    if rows != expected_rows:
        raise ArithmeticError(f"partition profile rows drifted: {rows!r}")
    channels = partition_channel_index()

    triples, quadruples = _required_subsets()
    synthetic_triples = {subset: index - 9 for index, subset in enumerate(triples)}
    synthetic_quadruples = {
        subset: 7 - index for index, subset in enumerate(quadruples)
    }
    direct_partition = partition_connected_cumulant(
        7, 5, -11, synthetic_triples, synthetic_quadruples
    )
    closed = closed_connected_cumulant(
        7, 5, -11, synthetic_triples, synthetic_quadruples
    )
    if direct_partition != closed:
        raise ArithmeticError("closed cumulant formula failed partition replay")
    correction_exponents = {
        m: proper_partition_correction_exponent(m)
        for m in range(5, MAX_FIXED_M_REPLAY + 1)
    }
    expected_exponents = {
        5: Fraction(15, 2),
        6: Fraction(7),
        7: Fraction(13, 2),
        8: Fraction(6),
        9: Fraction(11, 2),
    }
    if correction_exponents != expected_exponents:
        raise ArithmeticError("fixed-m correction exponents drifted")
    top_weight_channels = {
        genus: symplectic_top_weight_channel(genus) for genus in range(2, 6)
    }
    expected_top_weight_channels = {
        2: {1: 1},
        3: {3: 1, 1: -1},
        4: {},
        5: {3: 1, 5: -1},
    }
    if top_weight_channels != expected_top_weight_channels:
        raise ArithmeticError("symplectic top-weight classification drifted")
    m9_character = genus_four_character_expansion(9)
    m10_character = genus_four_character_expansion(10)
    if m9_character != {(3, 3): -9, (1, 1): -45}:
        raise ArithmeticError("m=9 notch expansion drifted")
    if m10_character != {
        (4, 4): -1,
        (3, 3): -10,
        (2, 2): -10,
        (1, 1): -55,
        (0, 0): -55,
    }:
        raise ArithmeticError("m=10 notch expansion drifted")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "PROVED_SIX_PLACE_CONNECTED_IDENTITY_AND_FIXED_M_WEIGHT_CLASSIFICATION_FROM_LOCKED_SOURCE",
        "scope": {
            "six_place": "uniform monic squarefree quintics H_5(q), odd q>=7, six distinct finite rational places",
            "fixed_m": "degree-five raw weight ceiling and exact top-weight classification for fixed m>=5 and odd q>=m",
        },
        "source_lock": {
            "path": SOURCE.relative_to(ROOT).as_posix(),
            "commit": SOURCE_COMMIT,
            "git_blob": SOURCE_BLOB,
            "sha256_lf_normalized": SOURCE_LF_SHA256,
            "payload_sha256": SOURCE_PAYLOAD_SHA256,
            "schema": source["schema"],
            "imported_theorem": source["exact_identity"]["degree_five_coefficient"],
            "transitive_packet_files": source["packet_files_lf_sha256"],
        },
        "six_place_adapter": {
            "curve": "C_A:y^2=product_(a in A)(a-z), genus two with split infinity",
            "zeta_numerator": "P_A=1-t_A*u+b_A*u^2-q*t_A*u^3+q^2*u^4",
            "normalized_frobenius": "P_A(u)=det(1-sqrt(q)*U_A*u), with U_A attached to this displayed C_A",
            "finite_dirichlet_polynomial": "L_A=(1-u)*P_A",
            "degree_five_L_coefficients": {
                "l_1": "-t_A-1",
                "l_3": "-q*t_A-b_A",
                "l_5": "-q^2",
            },
        },
        "raw_six_place_theorem": {
            "definition": "R_A=sum_(D in H_5(q)) product_(a in A) chi(D(a))",
            "coefficient_extraction": "R_A=(21-6*q)*l_1+(6-q)*l_3+l_5",
            "formula": "R_A=(q^2-21)*t_A+(q-6)*b_A-q^2+6*q-21",
            "formal_sparse_q_trace_middle": _sparse_rows(formal),
            "character_formula": "R_A=(q^(5/2)-21*q^(1/2))*chi_(omega_1)(U_A)+(q^2-6*q)*chi_(omega_2)(U_A)-21",
            "formal_sparse_half_q_power_fundamental_character": [
                {
                    "twice_q_exponent": twice_q_exponent,
                    "fundamental_character_index": fundamental_index,
                    "coefficient": coefficient,
                }
                for (
                    twice_q_exponent,
                    fundamental_index,
                ), coefficient in sorted(six_place_character.items())
            ],
            "middle_coefficient_reentry": "b_A cancels at five places but re-enters at six places with coefficient q-6",
        },
        "second_frobenius_power_reformulation": {
            "definition": "s_(2,A)=sum_j alpha_j^2=q^2+1-#C_A(F_(q^2))",
            "middle_coefficient": "b_A=(t_A^2-s_(2,A))/2",
            "raw_formula": "R_A=(q^2-21)*t_A+[(q-6)/2]*(t_A^2-s_(2,A))-q^2+6*q-21",
            "interpretation": "This is the first degree-five marked-place row in the m=1,...,6 ladder to retain an independent second-power or middle-coefficient channel; no F_(q^2) enumeration is performed.",
        },
        "connected_six_place_theorem": {
            "normalization": "N=q^4*(q-1), C=2*q-3",
            "four_place_raw": "R_I=q^2-10+(4*q-10)*t_I for |I|=4",
            "formula": "kappa_A=R_A/N-[C/N^2]*sum_(I subset A,|I|=4)R_I-[9*(q-2)^2/N^2]*sum_(unordered B,A\\B;|B|=3)t_B*t_(A\\B)+30*C^3/N^3",
            "partition_profile_rows": rows,
            "channel_multiplicities": {
                "four_plus_two": 15,
                "three_plus_three_unordered": 10,
                "three_pairs": 15,
                "three_pair_cumulant_coefficient_after_sum": 30,
            },
            "channel_index": channels,
        },
        "hasse_envelopes": {
            "inputs": {
                "full_genus_two_fundamental_characters": "|chi_(omega_1)(U_A)|<=4 and |chi_(omega_2)(U_A)|<=5",
                "triple_or_quadruple_genus_one_trace": "|t_I|<=2*sqrt(q)",
            },
            "raw_exact_character_form": "R_A=(q^(5/2)-21*q^(1/2))*chi_(omega_1)(U_A)+(q^2-6*q)*chi_(omega_2)(U_A)-21",
            "raw_trace": "4*(q^2-21)*sqrt(q)/N=O(q^-5/2)",
            "raw_nontrace": "[5*(q^2-6*q)+21]/N=O(q^-3)",
            "raw_combined": "|R_A|/N<=[4*(q^2-21)*sqrt(q)+5*(q^2-6*q)+21]/N for q>=7",
            "four_plus_two": "15*C*(q^2-10)/N^2+30*C*(4*q-10)*sqrt(q)/N^2=O(q^-7)+O(q^-15/2)",
            "three_plus_three": "360*q*(q-2)^2/N^2=O(q^-7)",
            "three_pairs": "30*C^3/N^3=O(q^-12)",
            "combined": "|kappa_A| is bounded by the sum of the five displayed nonnegative envelopes, hence O(q^-5/2)",
        },
        "persistence_statement": {
            "proved": "The q^-5/2 Hasse envelope first displayed at five places persists at six places; the genus-two middle coefficient re-enters at the smaller q^-3 scale.",
            "firewall": "This is a first persistence/saturation check beyond order five, not a proof that order six uniquely creates a threshold, that the envelope is attained, or that it gives a typical size.",
        },
        "fixed_m_weight_ceiling_and_genus_four_notch": {
            "scope": "fixed m>=5, odd q>=m; constants may depend on m and the statement is not uniform for growing m",
            "curve_and_twist_convention": "U is the normalized Frobenius class of C_A:y^2=product_(a in A)(a-z). For odd m, replacing this by the monic product_(a in A)(z-a) multiplies the right side by -1 and, whenever -1 is nonsquare, is the nontrivial quadratic twist and twists the odd character channels.",
            "inverse_root_bound": "|l_j|<=binom(m-1,j)*q^(j/2); for even m the trivial inverse root 1 is bounded by sqrt(q)",
            "coarse_degree_five_ceiling": "The locked degree-five identity gives raw R_(5,m)=O_m(q^(5/2)) and normalized mu_m=R_(5,m)/[q^4*(q-1)]=O_m(q^-5/2); this need not be the sharp leading channel.",
            "odd_exact_p_expansion": "S_(5,m)=[binom(m+1,2)-q*m]*p_1+(m-q)*p_3+p_5",
            "even_exact_p_expansion": "S_(5,m)=[binom(m+1,2)-q*m]*(p_1-p_0)+(m-q)*(p_3-p_2)+(p_5-p_4)",
            "top_q_power_channel": "q^(5/2)*(e_3(U)-e_5(U)); q^(1/2) denotes Frobenius weight, not a chosen field element",
            "symplectic_classification": {
                "genus_2_m_5_6": "e_1=chi_(omega_1)",
                "genus_3_m_7_8": "e_3-e_1=chi_(omega_3)",
                "genus_4_m_9_10": "0 because e_5=e_3",
                "genus_at_least_5_m_at_least_11": "e_3-e_5=-chi_(omega_5)",
            },
            "genus_four_notch": {
                "m_9_p_expansion": "S_(5,9)=9*p_3+(45-9*q)*p_1",
                "m_9_character_expansion": "S_(5,9)=-9*q^(3/2)*chi_(omega_3)-45*q^(1/2)*chi_(omega_1)",
                "m_9_scales": "mu_9=O(q^-7/2), kappa_9-mu_9=O(q^-11/2)",
                "m_10_character_expansion": "S_(5,10)=-q^2*chi_(omega_4)-10*q^(3/2)*chi_(omega_3)-10*q*chi_(omega_2)-55*q^(1/2)*chi_(omega_1)-55",
                "m_10_scales": "mu_10=O(q^-3), kappa_10-mu_10=O(q^-5)",
            },
            "coarse_block_weight_ledger": {
                "w_2": "4",
                "w_3": "7/2",
                "w_4": "3",
                "w_s_for_s>=5": "5/2",
            },
            "coarse_connected_correction": "Singleton means vanish and every proper centered partition has at least two blocks, so kappa_m-mu_m=O_m(q^-5)",
            "sharper_correction_exponents_m_5_through_9": {
                str(m): f"{exponent.numerator}/{exponent.denominator}"
                if exponent.denominator != 1
                else str(exponent.numerator)
                for m, exponent in correction_exponents.items()
            },
            "firewall": "The O_m(q^-5/2) statement is only a coarse fixed-m ceiling; the exact genus-four notch shows it is not always the leading scale. No sharpness, attainment, distribution, growing-m uniformity, or external novelty claim is made.",
        },
        "resource_contract": {
            "distinct_source_files_read": 1,
            "source_git_reads": 1,
            "source_bytes_read": SOURCE_BYTES,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "set_partitions_visited": len(_set_partitions(tuple(range(6)))),
            "maximum_set_partitions": MAX_SET_PARTITIONS,
            "centered_partitions": channels["centered_partition_count"],
            "maximum_centered_partitions": MAX_CENTERED_PARTITIONS,
            "fixed_m_exponent_replay_range": [5, MAX_FIXED_M_REPLAY],
            "top_weight_genera_replayed": [2, 5],
            "maximum_integer_partition_profiles": MAX_INTEGER_PARTITION_PROFILES,
            "maximum_symbolic_terms": MAX_SYMBOLIC_TERMS,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "payload_build_wall_seconds_cap": WALL_SECONDS,
            "measured_wall_seconds_is_not_canonical": True,
            "finite_field_enumeration": False,
            "extension_field_enumeration": False,
            "polynomial_family_enumeration": False,
            "curve_enumeration": False,
            "sampling": False,
            "floating_point_arithmetic": False,
        },
        "claim_boundary": [
            "The six-place identity is a source-relative symbolic consequence of the committed multi-place theorem and exact joint-cumulant partition algebra.",
            "The Hasse statements are uniform upper envelopes, not lower bounds, typical-value laws, or distribution theorems.",
            "The re-entry of b_A is a coefficient fact and does not identify a motive, compatible system, or full local factor from the connected statistic.",
            "No RH, GRH, principal-member amplification, number-field transfer, or external novelty claim is made.",
        ],
        "packet_files_lf_sha256": {
            "note": _file_sha256(NOTE),
            "producer": _file_sha256(Path(__file__).resolve()),
            "test": _file_sha256(TEST),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if len(rendered) > MAX_OUTPUT_BYTES:
        raise RuntimeError("output-byte cap exceeded")
    elapsed = time.monotonic() - started
    if elapsed > WALL_SECONDS:
        raise RuntimeError("payload-build wall-clock cap exceeded")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
            raise SystemExit("canonical payload drift")
        print(f"verified {OUTPUT}")
    else:
        OUTPUT.write_bytes(rendered)
        print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
