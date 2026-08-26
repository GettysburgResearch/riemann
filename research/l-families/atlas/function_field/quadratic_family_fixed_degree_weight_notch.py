#!/usr/bin/env python3
"""Replay the fixed-degree marked-place weight notch symbolically.

The producer source-locks the committed all-degree multi-place identity and
uses only bounded integer, rational, coefficient-ring, and set-partition
algebra. It performs no field, curve, root, zero, or sampling enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_fixed_degree_weight_notch.json"
NOTE = HERE / "QUADRATIC_FAMILY_FIXED_DEGREE_WEIGHT_NOTCH.md"
TEST = ROOT / "tests" / "test_quadratic_family_fixed_degree_weight_notch.py"
SOURCE = HERE / "quadratic_family_multiplace_l_function_identity.json"
SOURCE_COMMIT = "c94466e28a48ec429150f63de6d334d4c4f60110"
SOURCE_BLOB = "f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e"
SOURCE_LF_SHA256 = "b4529c82d40575593e4c346e4cdfa0aaee417618886b5b1ab448c2469c87ca9e"
SOURCE_PAYLOAD_SHA256 = (
    "ddd7332102007ceda079e7b85dd0a482642c3d999dac779dde220af4e3b27c7d"
)
SOURCE_BYTES = 10_738
SCHEMA = "riemann.function_field.quadratic_family_fixed_degree_weight_notch.v1"

MAX_REPLAY_N = 9
MAX_REPLAY_M = 14
MAX_CLASSIFICATION_N = 8
MAX_CLASSIFICATION_GENUS = 9
MAX_PARTITION_ORDER = 3
MAX_SET_PARTITIONS = 5
MAX_SOURCE_BYTES = 16_384
MAX_OUTPUT_BYTES = 32_768
WALL_SECONDS = 4.0

QPoly: TypeAlias = dict[int, int]
PCoefficients: TypeAlias = dict[int, QPoly]
CharacterExpr: TypeAlias = dict[int, int]
WeightExpr: TypeAlias = dict[tuple[int, int], int]
Partition: TypeAlias = tuple[tuple[int, ...], ...]


def _clean_qpoly(polynomial: QPoly) -> QPoly:
    return {
        power: coefficient for power, coefficient in polynomial.items() if coefficient
    }


def _add_qpoly(left: QPoly, right: QPoly) -> QPoly:
    result = dict(left)
    for power, coefficient in right.items():
        result[power] = result.get(power, 0) + coefficient
    return _clean_qpoly(result)


def _scale_qpoly(polynomial: QPoly, scalar: int) -> QPoly:
    return _clean_qpoly({power: scalar * value for power, value in polynomial.items()})


def binomial_channel(m: int, k: int) -> int:
    if m < 1 or k < 0:
        raise ValueError("binomial channels require m>=1 and k>=0")
    return comb(m + k - 1, k)


def kernel_coefficient(m: int, k: int) -> QPoly:
    """Return B_(m,k)=A_(m,k)-q*A_(m,k-1)."""
    if k == 0:
        return {0: 1}
    return {0: binomial_channel(m, k), 1: -binomial_channel(m, k - 1)}


def _add_p_coefficient(
    expansion: PCoefficients, index: int, coefficient: QPoly
) -> None:
    if index < 0:
        return
    expansion[index] = _add_qpoly(expansion.get(index, {}), coefficient)
    if not expansion[index]:
        expansion.pop(index)


def original_p_coefficient_expansion(n: int, m: int) -> PCoefficients:
    """Expand the locked coefficient theorem after L=P or L=(1-u)P."""
    if n < 2 or m < 1:
        raise ValueError("the fixed-degree replay requires n>=2 and m>=1")
    expansion: PCoefficients = {}
    for k in range(n // 2 + 1):
        coefficient = kernel_coefficient(m, k)
        index = n - 2 * k
        _add_p_coefficient(expansion, index, coefficient)
        if m % 2 == 0:
            _add_p_coefficient(expansion, index - 1, _scale_qpoly(coefficient, -1))
    return expansion


def d_coefficient_expansion(n: int, m: int) -> dict[int, int]:
    """Return coefficients of D_r=p_r-q*p_(r-2) in the regrouped identity."""
    if n < 2 or m < 1:
        raise ValueError("the fixed-degree replay requires n>=2 and m>=1")
    result: dict[int, int] = {}
    for k in range(n // 2 + 1):
        coefficient = binomial_channel(m, k)
        index = n - 2 * k
        result[index] = result.get(index, 0) + coefficient
        if m % 2 == 0 and index - 1 >= 0:
            result[index - 1] = result.get(index - 1, 0) - coefficient
    return {index: coefficient for index, coefficient in result.items() if coefficient}


def regrouped_p_coefficient_expansion(n: int, m: int) -> PCoefficients:
    """Expand the D_r regrouping back into the p_j basis."""
    expansion: PCoefficients = {}
    for index, coefficient in d_coefficient_expansion(n, m).items():
        _add_p_coefficient(expansion, index, {0: coefficient})
        _add_p_coefficient(expansion, index - 2, {1: -coefficient})
    return expansion


def _elementary_character(index: int, genus: int) -> CharacterExpr:
    """Reduce e_index by reciprocity, then expand it in fundamental characters."""
    if genus < 0:
        raise ValueError("genus must be nonnegative")
    if index < 0 or index > 2 * genus:
        return {}
    reduced = min(index, 2 * genus - index)
    return {fundamental: 1 for fundamental in range(reduced, -1, -2)}


def delta_character_expression(index: int, genus: int) -> CharacterExpr:
    """Return e_index-e_(index-2), with e_j=0 outside 0..2g."""
    result = _elementary_character(index, genus)
    for fundamental, coefficient in _elementary_character(index - 2, genus).items():
        result[fundamental] = result.get(fundamental, 0) - coefficient
    return {
        fundamental: coefficient
        for fundamental, coefficient in result.items()
        if coefficient
    }


def expected_top_delta(n: int, genus: int) -> CharacterExpr:
    """Return the four-region USp classification of e_n-e_(n-2)."""
    if n < 2 or genus < 0:
        raise ValueError("top-delta classification requires n>=2 and g>=0")
    if 2 * genus < n - 2:
        return {}
    if genus <= n - 2:
        return {2 * genus - n + 2: -1}
    if genus == n - 1:
        return {}
    return {n: 1}


def top_delta_region(n: int, genus: int) -> str:
    if 2 * genus < n - 2:
        return "BELOW_RANGE"
    if genus <= n - 2:
        return "PRE_NOTCH"
    if genus == n - 1:
        return "NOTCH"
    return "POST_NOTCH"


def weighted_character_expansion(n: int, m: int, genus: int) -> WeightExpr:
    """Expand S_(n,m) in q^(r/2)*chi_(omega_j) channels."""
    result: WeightExpr = {}
    for index, d_coefficient in d_coefficient_expansion(n, m).items():
        sign = -1 if index % 2 else 1
        for fundamental, delta_coefficient in delta_character_expression(
            index, genus
        ).items():
            key = (index, fundamental)
            result[key] = result.get(key, 0) + d_coefficient * sign * delta_coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def notch_leading_row(n: int, even_mark_count: bool) -> dict[str, int | str]:
    """Return the first nonzero weight channel at g=n-1."""
    if n < 2:
        raise ValueError("notch replay requires n>=2")
    if even_mark_count:
        return {
            "marked_places": 2 * n,
            "d_index": n - 1,
            "twice_q_exponent": n - 1,
            "fundamental_character_index": n - 1,
            "coefficient": (-1) ** n,
            "normalized_exponent": f"{n + 1}/2",
        }
    return {
        "marked_places": 2 * n - 1,
        "d_index": n - 2,
        "twice_q_exponent": n - 2,
        "fundamental_character_index": n - 2,
        "coefficient": (2 * n - 1) * (-1) ** n,
        "normalized_exponent": f"{n + 2}/2",
    }


def family_size(n: int, q: int) -> int:
    if n < 2 or q < 2:
        raise ValueError("family size requires n>=2 and q>=2")
    return q ** (n - 1) * (q - 1)


def one_place_raw_sum(n: int, q: int) -> int:
    if n < 2 or q < 2:
        raise ValueError("one-place replay requires n>=2 and q>=2")
    return 0 if n % 2 else 1 - q


def one_place_mean(n: int, q: int) -> Fraction:
    return Fraction(one_place_raw_sum(n, q), family_size(n, q))


def _set_partitions(labels: tuple[int, ...]) -> tuple[Partition, ...]:
    if len(labels) > MAX_PARTITION_ORDER:
        raise ValueError("partition replay is capped at order three")
    if not labels:
        return ((),)
    first, rest = labels[0], labels[1:]
    rows: list[Partition] = []
    for partition in _set_partitions(rest):
        rows.append(((first,),) + partition)
        for index, block in enumerate(partition):
            updated = list(partition)
            updated[index] = (first,) + block
            rows.append(tuple(updated))
    if len(rows) > MAX_SET_PARTITIONS:
        raise RuntimeError("set-partition cap exceeded")
    return tuple(rows)


def cumulant_from_block_size_moments(
    order: int, block_moments: dict[int, Fraction]
) -> Fraction:
    result = Fraction(0)
    for partition in _set_partitions(tuple(range(order))):
        coefficient = (-1) ** (len(partition) - 1) * factorial(len(partition) - 1)
        product = Fraction(1)
        for block in partition:
            product *= block_moments[len(block)]
        result += coefficient * product
    return result


def n2_third_cumulant(q: int) -> Fraction:
    if q < 3 or q % 2 == 0:
        raise ValueError("three marked places require odd q>=3")
    size = family_size(2, q)
    moments = {
        1: Fraction(-1, q),
        2: Fraction(2 - q, size),
        3: Fraction(3, size),
    }
    return cumulant_from_block_size_moments(3, moments)


def n2_third_cumulant_closed(q: int) -> Fraction:
    if q < 3 or q % 2 == 0:
        raise ValueError("three marked places require odd q>=3")
    return Fraction(2 * (2 * q + 1), q**3 * (q - 1))


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
    exact = payload.get("exact_identity")
    expected = {
        "general_coefficient": "If L=sum_j l_j*u^j and B_m,0=1, then S_n,m=sum_(j<=n, n-j even) l_j*B_m,(n-j)/2.",
        "kernel": "[u^(2k)](1-q*u^2)/(1-u^2)^m=binom(m+k-1,k)-q*binom(m+k-2,k-1) for k>=1",
        "odd_m": "L(u,psi_A)=P_C_A(u)",
        "even_m": "L(u,psi_A)=(1-u)*P_C_A(u)",
    }
    if not isinstance(exact, dict) or any(
        exact.get(key) != value for key, value in expected.items()
    ):
        raise RuntimeError("locked all-degree identity drifted")
    return payload


def _classification_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(2, MAX_CLASSIFICATION_N + 1):
        for genus in range(MAX_CLASSIFICATION_GENUS + 1):
            if genus > n + 1:
                continue
            actual = delta_character_expression(n, genus)
            expected = expected_top_delta(n, genus)
            if actual != expected:
                raise ArithmeticError(
                    f"USp classification drifted at n={n}, g={genus}: {actual!r}"
                )
            rows.append(
                {
                    "n": n,
                    "genus": genus,
                    "region": top_delta_region(n, genus),
                    "character": [
                        {"omega_index": index, "coefficient": coefficient}
                        for index, coefficient in sorted(actual.items())
                    ],
                }
            )
    return rows


def _weight_rows(expression: WeightExpr) -> list[dict[str, int]]:
    return [
        {
            "twice_q_exponent": exponent,
            "omega_index": omega,
            "coefficient": coefficient,
        }
        for (exponent, omega), coefficient in sorted(expression.items())
    ]


def build_payload() -> dict[str, object]:
    started = time.monotonic()
    source = load_locked_source()

    replayed_pairs = 0
    for n in range(2, MAX_REPLAY_N + 1):
        for m in range(1, MAX_REPLAY_M + 1):
            original = original_p_coefficient_expansion(n, m)
            regrouped = regrouped_p_coefficient_expansion(n, m)
            if original != regrouped:
                raise ArithmeticError(f"coefficient regrouping drifted at n={n}, m={m}")
            replayed_pairs += 1

    classification_rows = _classification_rows()
    low_cases = {
        "n_2_m_3": weighted_character_expansion(2, 3, 1),
        "n_2_m_4": weighted_character_expansion(2, 4, 1),
        "n_5_m_9": weighted_character_expansion(5, 9, 4),
        "n_5_m_10": weighted_character_expansion(5, 10, 4),
    }
    expected_low_cases = {
        "n_2_m_3": {(0, 0): 3},
        "n_2_m_4": {(1, 1): 1, (0, 0): 4},
        "n_5_m_9": {(3, 3): -9, (1, 1): -45},
        "n_5_m_10": {
            (4, 4): -1,
            (3, 3): -10,
            (2, 2): -10,
            (1, 1): -55,
            (0, 0): -55,
        },
    }
    if low_cases != expected_low_cases:
        raise ArithmeticError(f"low-case character replay drifted: {low_cases!r}")

    for q in (3, 5, 7, 9):
        if n2_third_cumulant(q) != n2_third_cumulant_closed(q):
            raise ArithmeticError(f"n=2 third-cumulant replay drifted at q={q}")

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "PROVED_FROM_LOCKED_ALL_DEGREE_IDENTITY_BY_BOUNDED_SYMBOLIC_REPLAY",
        "scope": "fixed integers n>=2 and m>=1; odd prime powers q>=m; m distinct finite rational places; asymptotics hold only for fixed (n,m)",
        "source_lock": {
            "path": SOURCE.relative_to(ROOT).as_posix(),
            "commit": SOURCE_COMMIT,
            "git_blob": SOURCE_BLOB,
            "sha256_lf_normalized": SOURCE_LF_SHA256,
            "payload_sha256": SOURCE_PAYLOAD_SHA256,
            "schema": source["schema"],
            "imported_general_coefficient": source["exact_identity"][
                "general_coefficient"
            ],
            "imported_kernel": source["exact_identity"]["kernel"],
            "imported_parity_adapter": {
                "odd_m": source["exact_identity"]["odd_m"],
                "even_m": source["exact_identity"]["even_m"],
            },
            "transitive_packet_files": source["packet_files_lf_sha256"],
            "six_place_packet_imported": False,
        },
        "notation": {
            "family": "H_n(q) is the monic squarefree degree-n family; |H_n(q)|=N_n=q^(n-1)*(q-1)",
            "curve": "C_A:y^2=product_(a in A)(a-z), with g=floor((m-1)/2)",
            "numerator": "P_A(u)=sum_j p_j*u^j=det(1-sqrt(q)*U_A*u)",
            "coefficient_conventions": "p_j=e_j=0 outside 0<=j<=2*g; p_j=(-1)^j*q^(j/2)*e_j(U_A); chi_(omega_0)=1",
            "binomial_channel": "A_(m,k)=binom(m+k-1,k)",
            "difference_channel": "D_r=p_r-q*p_(r-2), with p_j=0 for j<0",
        },
        "exact_regrouped_identity": {
            "odd_m": "S_(n,m)=sum_(0<=k<=floor(n/2)) A_(m,k)*D_(n-2k)",
            "even_m": "S_(n,m)=sum_(0<=k<=floor(n/2)) A_(m,k)*[D_(n-2k)-D_(n-1-2k)], with D_r=0 for r<0",
            "derivation": "B_(m,k)=A_(m,k)-q*A_(m,k-1), while L=P for odd m and L=(1-u)*P for even m",
            "bounded_replay_pairs": replayed_pairs,
            "replay_rectangle": {
                "n": [2, MAX_REPLAY_N],
                "m": [1, MAX_REPLAY_M],
            },
        },
        "unique_top_weight_channel": {
            "formula": "D_n=p_n-q*p_(n-2)=(-1)^n*q^(n/2)*Delta_(n,g)",
            "delta": "Delta_(n,g)=e_n-e_(n-2)",
            "uniqueness": "Every other odd-m channel has weight at most (n-2)/2; for even m the extra -D_(n-1) has weight (n-1)/2 and all remaining channels are lower.",
            "classification": {
                "below_range": "Delta_(n,g)=0 if 2*g<n-2",
                "pre_notch": "Delta_(n,g)=-chi_(omega_(2*g-n+2)) if n-2<=2*g and g<=n-2; chi_(omega_0)=1",
                "notch": "Delta_(n,n-1)=0, corresponding exactly to m=2*n-1 and m=2*n",
                "post_notch": "Delta_(n,g)=chi_(omega_n) for g>=n",
            },
            "bounded_classification_rows": classification_rows,
        },
        "notch_leading_residual_channels": {
            "warning": "These are leading residual weight channels after D_n vanishes, not complete equalities for S_(n,m); the displayed exact lower-channel sums remain.",
            "odd_mark_count": {
                "m": "2*n-1",
                "exact_residual": "S_(n,2*n-1)=(2*n-1)*D_(n-2)+sum_(k=2..floor(n/2)) A_(2*n-1,k)*D_(n-2k)",
                "exact_character_expansion": "S_(n,2*n-1)=(-1)^n*sum_(k=1..floor(n/2)) binom(2*n+k-2,k)*q^((n-2*k)/2)*chi_(omega_(n-2*k))",
                "leading_channel": "(2*n-1)*(-1)^n*q^((n-2)/2)*chi_(omega_(n-2))",
                "raw_scale": "O_n(q^((n-2)/2))",
                "normalized_scale": "mu_(n,2*n-1)=O_n(q^(-(n+2)/2))",
                "n_5_symbolic_row": notch_leading_row(5, False),
            },
            "even_mark_count": {
                "m": "2*n",
                "exact_residual": "S_(n,2*n)=-D_(n-1)+sum_(k=1..floor(n/2)) A_(2*n,k)*[D_(n-2k)-D_(n-1-2k)]",
                "exact_character_expansion": "S_(n,2*n)=(-1)^n*[q^((n-1)/2)*chi_(omega_(n-1))+sum_(k=1..floor(n/2)) binom(2*n+k-1,k)*q^((n-2*k)/2)*chi_(omega_(n-2*k))+sum_(k=1..floor((n-1)/2)) binom(2*n+k-1,k)*q^((n-2*k-1)/2)*chi_(omega_(n-2*k-1))]",
                "leading_channel": "(-1)^n*q^((n-1)/2)*chi_(omega_(n-1))",
                "raw_scale": "O_n(q^((n-1)/2))",
                "normalized_scale": "mu_(n,2*n)=O_n(q^(-(n+1)/2))",
                "n_5_symbolic_row": notch_leading_row(5, True),
            },
            "low_case_character_replays": {
                label: _weight_rows(expression)
                for label, expression in low_cases.items()
            },
        },
        "marked_place_spectrometer": {
            "pre_notch": "Within the supported pre-notch range, the top exterior-character index runs through the parity of n: 1,3,...,n-2 for odd n and 0,2,...,n-2 for even n, with top-channel sign (-1)^(n+1).",
            "notch": "The two mark counts 2*n-1 and 2*n null the q^(n/2) channel exactly.",
            "post_notch": "For m>=2*n+1 the top channel is (-1)^n*q^(n/2)*chi_(omega_n).",
            "interpretation_firewall": "This is an exact detector-design and aliasing diagnostic, not an equidistribution, independence, motive, or novelty theorem.",
        },
        "connected_correction": {
            "raw_normalized_moment_envelope": "For every fixed block size s, mu_(n,s)=O_(n,s)(q^(-n/2)).",
            "one_place_mean": "E[X_a]=0 for odd n and E[X_a]=-q^(-(n-1)) for even n.",
            "proper_partition_bound": "For fixed (n,m), every proper partition has at least two blocks, hence kappa_(n,m)-mu_(n,m)=O_(n,m)(q^(-n)).",
            "inheritance": "For n>=3 the proper-partition bound is below both notch upper-envelope scales; for the even notch it is also below the leading scale when n=2. This does not assert pointwise attainment of a character channel.",
            "n_2_caveat": {
                "raw_three_place": "mu_(2,3)=3/[q*(q-1)]=O(q^-2)",
                "block_moments": "M_1=-1/q, M_2=(2-q)/[q*(q-1)], M_3=3/[q*(q-1)]",
                "connected_formula": "kappa_(2,3)=M_3-3*M_2*M_1+2*M_1^3=2*(2*q+1)/[q^3*(q-1)]=O(q^-3)",
                "warning": "At the odd-mark-count n=2 notch the O(q^-2) proper terms can match and cancel the raw leading scale, so no general raw-to-connected inheritance statement may include this case.",
            },
            "set_partitions_visited_for_n_2_control": len(_set_partitions((0, 1, 2))),
        },
        "twist_infinity_and_weight_conventions": {
            "source_curve": "U_A belongs to C_A:y^2=product_(a in A)(a-z)",
            "odd_m_twist": "For odd m, replacing the source polynomial by the monic product_(a in A)(z-a) is a quadratic twist when -1 is nonsquare and changes odd exterior-character channels.",
            "even_m_infinity": "For even m, split infinity gives L=(1-u)*P and is exactly the source of the -D_(n-1-2k) summand.",
            "sqrt_q": "q^(1/2) denotes Frobenius weight, not a chosen element of F_q when q is nonsquare.",
        },
        "resource_contract": {
            "distinct_source_files_read": 1,
            "source_content_reads": 1,
            "source_git_commands": 2,
            "source_bytes_read": SOURCE_BYTES,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "coefficient_pairs_replayed": replayed_pairs,
            "maximum_replay_n": MAX_REPLAY_N,
            "maximum_replay_m": MAX_REPLAY_M,
            "classification_rows_replayed": len(classification_rows),
            "maximum_classification_n": MAX_CLASSIFICATION_N,
            "maximum_classification_genus": MAX_CLASSIFICATION_GENUS,
            "set_partitions_visited": len(_set_partitions((0, 1, 2))),
            "maximum_set_partitions": MAX_SET_PARTITIONS,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "payload_build_wall_seconds_cap": WALL_SECONDS,
            "measured_wall_seconds_is_not_canonical": True,
            "finite_field_enumeration": False,
            "extension_field_enumeration": False,
            "polynomial_family_enumeration": False,
            "curve_enumeration": False,
            "root_enumeration": False,
            "zero_enumeration": False,
            "sampling": False,
            "floating_point_arithmetic": False,
        },
        "claim_boundary": [
            "All asymptotics hold for fixed (n,m) as q tends through odd prime powers with q>=m; no growing-degree or growing-mark uniformity is claimed.",
            "Every scale is a Weil upper envelope and weight-channel statement, not a lower bound, attainment claim, typical-value law, or equidistribution theorem.",
            "The curve is the source adapter for a finite Dirichlet character; no local channel is promoted to an individual motive or compatible system.",
            "The regrouping uses the standard Euler quotient and standard exterior-character algebra; no external novelty claim is made.",
            "No memberwise sign, zero theorem, principal-member amplifier, number-field transfer, RH, or GRH statement is proved.",
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
    if time.monotonic() - started > WALL_SECONDS:
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
