#!/usr/bin/env python3
"""Inverse-design exact genus-two filters that isolate the weight-eight cusp trace."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections import Counter
from collections.abc import Mapping
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_inverse_cusp_trace_filters.json"
NOTE_PATH = HERE / "GENUS2_INVERSE_CUSP_TRACE_FILTERS.md"
TEST_PATH = ROOT / "tests" / "test_genus2_inverse_cusp_trace_filters.py"

NATIVE_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
SYM6_PATH = HERE / "genus2_sym6_marked_trace_average.json"
SYM8_PATH = HERE / "genus2_sym8_marked_trace_average.json"
BALANCED_PATH = HERE / "balanced_control_family_scan.json"

# Every theorem and held-out input is rejected unless both its LF-normalized
# file hash and canonical payload hash match.
SOURCE_LOCKS = {
    "native_wavelet": {
        "path": NATIVE_PATH,
        "lf": "aef506afa6b9b29f10528b634f45c7eab96abc36c6cd2de886262e834fcb2d43",
        "payload": "4e366316c6d55488b41e0104f6bee6c947220d7989ea7aa1381b5d72a099b882",
    },
    "sym6": {
        "path": SYM6_PATH,
        "lf": "4e6156e8ca4f8b652e02961d3aa5f3ea63c9b42243908d1ecab8b94c08d253a6",
        "payload": "7bf31859372bb2a292f8321794f9b05859d2def82b1dd59ad83ab992088a5e86",
    },
    "sym8": {
        "path": SYM8_PATH,
        "lf": "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233",
        "payload": "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae",
    },
    "balanced": {
        "path": BALANCED_PATH,
        "lf": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
    },
}
THEOREM_SOURCE_NAMES = ("native_wavelet", "sym6", "sym8")
HELD_OUT_SOURCE_NAMES = ("balanced",)

MAX_SOURCE_ATOMS = 512
MAX_RECURRENCE_UPDATES = 4096
MAX_TOWER_EXPONENT = 8
LATTICE_REGRESSION_RADIUS = 12
MAX_LATTICE_REGRESSION_POINTS = 1024
MAX_WALL_SECONDS = 4.0

# Coordinates are (Theta_(8,2), q, 1).
TRACE_VECTORS = {
    2: (0, 1, -1),
    4: (0, 0, -3),
    6: (0, 0, -4),
    8: (-1, -1, -6),
}


def _canonical_bytes(value: object) -> bytes:
    def normalize(item: object) -> object:
        if isinstance(item, str):
            return unicodedata.normalize("NFC", item)
        if isinstance(item, list):
            return [normalize(entry) for entry in item]
        if isinstance(item, dict):
            return {
                unicodedata.normalize("NFC", str(key)): normalize(entry)
                for key, entry in item.items()
            }
        return item

    return json.dumps(
        normalize(value),
        allow_nan=False,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")


def _canonical_sha256(value: object) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _lf_sha256(path: Path) -> str:
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(data).hexdigest()


def source_locks_ready(names: tuple[str, ...] | None = None) -> bool:
    selected = (
        SOURCE_LOCKS if names is None else {name: SOURCE_LOCKS[name] for name in names}
    )
    return all(
        isinstance(lock["lf"], str)
        and len(lock["lf"]) == 64
        and isinstance(lock["payload"], str)
        and len(lock["payload"]) == 64
        for lock in selected.values()
    )


def _load_sources(names: tuple[str, ...]) -> dict[str, dict[str, object]]:
    if not names or len(set(names)) != len(names):
        raise ValueError("source names must be nonempty and distinct")
    if any(name not in SOURCE_LOCKS for name in names):
        raise ValueError("unknown source lock")
    if not source_locks_ready(names):
        raise RuntimeError("audited source locks are not yet complete")
    loaded: dict[str, dict[str, object]] = {}
    for name in names:
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        expected_lf = lock["lf"]
        expected_payload = lock["payload"]
        if not isinstance(path, Path) or _lf_sha256(path) != expected_lf:
            raise RuntimeError(f"source LF lock failed: {name}")
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not a JSON object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != expected_payload or claimed != _canonical_sha256(payload):
            raise RuntimeError(f"source payload lock failed: {name}")
        loaded[name] = value
    return loaded


def trace_coordinates(
    coefficients: tuple[int, int, int, int],
) -> tuple[int, int, int]:
    """Return (Theta, q, constant) coefficients for c2*T2+...+c8*T8."""
    result = [0, 0, 0]
    for coefficient, weight in zip(coefficients, (2, 4, 6, 8), strict=True):
        vector = TRACE_VECTORS[weight]
        for index, value in enumerate(vector):
            result[index] += coefficient * value
    return result[0], result[1], result[2]


def lattice_solution(m: int, k: int) -> tuple[int, int, int, int]:
    """All integral nuisance-free solutions, ordered as (c2,c4,c6,c8)."""
    return m, -m - 4 * k, -m + 3 * k, m


def lattice_parameters(
    coefficients: tuple[int, int, int, int],
) -> tuple[int, int]:
    """Invert ``lattice_solution`` or reject a non-solution."""
    c2, c4, c6, c8 = coefficients
    if trace_coordinates(coefficients)[1:] != (0, 0):
        raise ValueError("coefficients do not cancel q and constant channels")
    if c2 != c8 or (c6 + c8) % 3:
        raise ArithmeticError("nuisance equations did not yield integral parameters")
    m = c8
    k = (c6 + c8) // 3
    if lattice_solution(m, k) != (c2, c4, c6, c8):
        raise ArithmeticError("lattice inverse failed")
    return m, k


def support_size(coefficients: tuple[int, int, int, int]) -> int:
    return sum(value != 0 for value in coefficients)


def haar_variance(
    coefficients: tuple[Fraction, Fraction, Fraction, Fraction], q: int
) -> Fraction:
    """USp(4) Haar variance using r_(2j)=q^j*chi_(2j,0)."""
    if q < 3 or q % 2 == 0:
        raise ValueError("q must be odd and at least three")
    return sum(
        coefficient * coefficient * q**weight
        for coefficient, weight in zip(coefficients, (2, 4, 6, 8), strict=True)
    )


def optimal_unit_response_coefficients(
    q: int,
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Unique Haar-minimizer with nuisance cancellation and c8=1."""
    if q < 3 or q % 2 == 0:
        raise ValueError("q must be odd and at least three")
    denominator = 9 * q * q + 16
    return (
        Fraction(1),
        Fraction(-21 * q * q, denominator),
        Fraction(-28, denominator),
        Fraction(1),
    )


def optimal_unit_response_variance(q: int) -> Fraction:
    denominator = 9 * q * q + 16
    return Fraction(q**8 + q**2) + Fraction(49 * q**6, denominator)


def reciprocal_coefficients(
    a_coefficient: int, b_coefficient: int, q: int
) -> tuple[int, ...]:
    values = [1]
    for degree in range(1, 9):
        value = -a_coefficient * values[degree - 1]
        if degree >= 2:
            value -= b_coefficient * values[degree - 2]
        if degree >= 3:
            value -= q * a_coefficient * values[degree - 3]
        if degree >= 4:
            value -= q * q * values[degree - 4]
        values.append(value)
    return tuple(values)


def sparse_filter_value(reciprocal: tuple[int, ...], name: str) -> int:
    if len(reciprocal) < 9:
        raise ValueError("reciprocal coefficients through degree eight are required")
    if name == "F4":
        return 3 * reciprocal[8] - 7 * reciprocal[4] + 3 * reciprocal[2]
    if name == "F6":
        return 4 * reciprocal[8] - 7 * reciprocal[6] + 4 * reciprocal[2]
    raise ValueError(f"unknown sparse filter: {name}")


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _extract_family_rows(balanced: Mapping[str, object]) -> list[dict[str, object]]:
    frozen = balanced.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("balanced source lacks frozen_enumeration_facts")
    families = frozen.get("families")
    if not isinstance(families, list):
        raise TypeError("balanced source lacks families")
    if not all(isinstance(row, dict) for row in families):
        raise TypeError("balanced family row is not an object")
    return families


def _preflight_held_out_work(
    rows: list[dict[str, object]], tower_updates: int
) -> tuple[int, int]:
    source_atoms = 0
    for row in rows:
        joint = row.get("joint_a_D_b_D_law")
        if not isinstance(joint, dict) or not isinstance(joint.get("atoms"), list):
            raise TypeError("balanced source lacks a joint atom list")
        source_atoms += len(joint["atoms"])
    if source_atoms > MAX_SOURCE_ATOMS:
        raise RuntimeError("cumulative source-atom cap exceeded")
    recurrence_updates = tower_updates + 8 * source_atoms
    if recurrence_updates > MAX_RECURRENCE_UPDATES:
        raise RuntimeError("recurrence-update cap exceeded")
    return source_atoms, recurrence_updates


def _held_out_panel(
    row: Mapping[str, object],
    theta: int,
    updates: list[int],
    atoms_seen: list[int],
) -> dict[str, object]:
    q = row.get("q")
    members = row.get("member_count")
    joint = row.get("joint_a_D_b_D_law")
    if (
        not isinstance(q, int)
        or not isinstance(members, int)
        or not isinstance(joint, dict)
    ):
        raise TypeError("invalid held-out family row")
    atoms = joint.get("atoms")
    if not isinstance(atoms, list) or len(atoms) > MAX_SOURCE_ATOMS:
        raise RuntimeError("invalid or oversized held-out atom list")

    total = 0
    total_square = 0
    signs: Counter[int] = Counter()
    zero_stratum_members = 0
    zero_stratum_total = 0
    for atom in atoms:
        if not isinstance(atom, dict):
            raise TypeError("held-out atom is not an object")
        a_coefficient = atom.get("a_D")
        b_coefficient = atom.get("b_D")
        count = atom.get("member_count")
        if not all(
            isinstance(value, int) for value in (a_coefficient, b_coefficient, count)
        ):
            raise TypeError("held-out atom has a nonintegral coordinate")
        if atoms_seen[0] >= MAX_SOURCE_ATOMS:
            raise RuntimeError("cumulative source-atom cap exceeded")
        if updates[0] + 8 > MAX_RECURRENCE_UPDATES:
            raise RuntimeError("recurrence-update cap exceeded")
        atoms_seen[0] += 1
        updates[0] += 8
        reciprocal = reciprocal_coefficients(int(a_coefficient), int(b_coefficient), q)
        value = sparse_filter_value(reciprocal, "F4")
        count = int(count)
        total += count * value
        total_square += count * value * value
        signs[(value > 0) - (value < 0)] += count
        if a_coefficient == 0 and b_coefficient == 0:
            zero_stratum_members += count
            zero_stratum_total += count * value

    if sum(signs.values()) != members:
        raise ArithmeticError("held-out atom mass mismatch")
    predicted_total = -3 * q * (q - 1) * theta
    if total != predicted_total:
        raise ArithmeticError("held-out F4 sum disagrees with the cusp-trace theorem")
    mean = Fraction(total, members)
    second_moment = Fraction(total_square, members)
    variance = second_moment - mean * mean
    stratum_ratio = Fraction(zero_stratum_total, total)
    return {
        "q": q,
        "family_members": members,
        "joint_law_atoms": len(atoms),
        "theta_(8,2)": theta,
        "sign_counts": {
            "negative": signs[-1],
            "zero": signs[0],
            "positive": signs[1],
        },
        "observed_total_F4": total,
        "theorem_total_F4": predicted_total,
        "family_mean_F4": _fraction_pair(mean),
        "family_second_moment_F4": _fraction_pair(second_moment),
        "family_centered_variance_F4": _fraction_pair(variance),
        "zero_stratum": {
            "coefficient_condition": "a_D=b_D=0",
            "members": zero_stratum_members,
            "per_member_F4": q * q * (3 * q * q + 7),
            "signed_total_F4": zero_stratum_total,
            "ratio_to_full_signed_total": _fraction_pair(stratum_ratio),
        },
        "status": "SOURCE_LOCKED_HELD_OUT_DIAGNOSTIC_NOT_THEOREM_INPUT",
    }


def hecke_trace_tower(p: int, a_p: int, maximum_exponent: int) -> tuple[int, ...]:
    """Theta_(8,2)(p^r), r=0..R, from alpha+beta=a_p, alpha*beta=p^7."""
    if p < 3 or p % 2 == 0 or maximum_exponent < 1:
        raise ValueError("an odd p and positive exponent cap are required")
    values = [2, a_p]
    for _ in range(2, maximum_exponent + 1):
        values.append(a_p * values[-1] - p**7 * values[-2])
    return tuple(values)


def raw_trace_recurrence_polynomial(p: int, a_p: int) -> tuple[int, ...]:
    """Low-to-high coefficients of (X^2-a_p X+p^7)(X-p)(X-1)."""
    return (
        p**8,
        -(p**7 * (p + 1) + a_p * p),
        p**7 + a_p * (p + 1) + p,
        -(a_p + p + 1),
        1,
    )


def _recurrence_residual(
    sequence: tuple[int, ...], polynomial: tuple[int, ...]
) -> tuple[int, ...]:
    order = len(polynomial) - 1
    if polynomial[-1] != 1 or len(sequence) <= order:
        raise ValueError("a longer sequence and monic polynomial are required")
    return tuple(
        sum(
            polynomial[index] * sequence[degree - order + index]
            for index in range(order + 1)
        )
        for degree in range(order, len(sequence))
    )


def _validate_source_semantics(
    sources: Mapping[str, Mapping[str, object]],
) -> dict[int, int]:
    native = sources["native_wavelet"]
    low = native.get("proved_all_q_trace_inputs")
    if (
        not isinstance(low, dict)
        or low.get("T_(2,0)") != "q-1"
        or low.get("T_(4,0)") != "-3"
    ):
        raise RuntimeError("T2/T4 theorem inputs changed")

    sym6 = sources["sym6"].get("theorem")
    if not isinstance(sym6, dict) or sym6.get("marked_stack_trace") != "T_(6,0)(q)=-4":
        raise RuntimeError("T6 theorem input changed")

    sym8_source = sources["sym8"]
    sym8 = sym8_source.get("theorem")
    if (
        not isinstance(sym8, dict)
        or sym8.get("marked_stack_trace") != "T_(8,0)(q)=-Theta_(8,2)(q)-q-6"
    ):
        raise RuntimeError("T8 theorem input changed")
    eta = sym8_source.get("eta_product_certificate")
    if not isinstance(eta, dict):
        raise TypeError("Sym8 eta-product certificate missing")
    checks = eta.get("good_prime_checks")
    if not isinstance(checks, dict):
        raise TypeError("Sym8 good-prime controls missing")
    theta = {}
    for q in (3, 5, 7):
        value = checks.get(f"c_{q}")
        if not isinstance(value, int):
            raise TypeError(f"Sym8 c_{q} control missing")
        theta[q] = value
    if theta != {3: 12, 5: -210, 7: 1016}:
        raise ArithmeticError("Sym8 good-prime controls changed")
    return theta


def _classification_certificate() -> dict[str, object]:
    lattice_points = (2 * LATTICE_REGRESSION_RADIUS + 1) ** 2
    if lattice_points > MAX_LATTICE_REGRESSION_POINTS:
        raise RuntimeError("lattice-regression point cap exceeded")

    sparse_f4 = (3, -7, 0, 3)
    sparse_f6 = (4, 0, -7, 4)
    null_direction = (0, 4, -3, 0)
    for coefficients, expected in (
        (sparse_f4, (-3, 0, 0)),
        (sparse_f6, (-4, 0, 0)),
        (null_direction, (0, 0, 0)),
    ):
        if trace_coordinates(coefficients) != expected:
            raise ArithmeticError("sparse-filter trace certificate failed")
        lattice_parameters(coefficients)

    for m in range(-LATTICE_REGRESSION_RADIUS, LATTICE_REGRESSION_RADIUS + 1):
        for k in range(-LATTICE_REGRESSION_RADIUS, LATTICE_REGRESSION_RADIUS + 1):
            coefficients = lattice_solution(m, k)
            if trace_coordinates(coefficients) != (-m, 0, 0):
                raise ArithmeticError("lattice parametrization failed")
            if lattice_parameters(coefficients) != (m, k):
                raise ArithmeticError("lattice inverse failed")

    return {
        "trace_formula": ("T_c(q)=-c8*Theta_(8,2)(q)+(c2-c8)*q-(c2+3*c4+4*c6+6*c8)"),
        "nuisance_equations": ["c2=c8", "3*c4+4*c6=-7*c8"],
        "integral_lattice": ("(c2,c4,c6,c8)=m*(1,-1,-1,1)+k*(0,-4,3,0), m,k in Z"),
        "cusp_response": "T_c(q)=-m*Theta_(8,2)(q)",
        "integral_unit_response_baseline": {
            "coefficients_c2_c4_c6_c8": [1, -1, -1, 1],
            "formula": "r_D(8)-r_D(6)-r_D(4)+r_D(2)",
            "marked_trace": "-Theta_(8,2)(q)",
        },
        "two_scale_classification": (
            "the only primitive nuisance-free two-scale direction is "
            "(0,4,-3,0), with zero cusp response; no support-at-most-two "
            "solution has c8 nonzero"
        ),
        "primitive_three_scale_cusp_filters_up_to_sign": [
            {
                "name": "F4",
                "coefficients_c2_c4_c6_c8": list(sparse_f4),
                "formula": "3*r_D(8)-7*r_D(4)+3*r_D(2)",
                "marked_trace": "-3*Theta_(8,2)(q)",
            },
            {
                "name": "F6",
                "coefficients_c2_c4_c6_c8": list(sparse_f6),
                "formula": "4*r_D(8)-7*r_D(6)+4*r_D(2)",
                "marked_trace": "-4*Theta_(8,2)(q)",
            },
        ],
        "bounded_checker_is_not_infinite_proof": (
            "the displayed linear elimination proves the lattice; the bounded m,k replay is only a regression check"
        ),
    }


def _haar_certificate() -> dict[str, object]:
    f4 = tuple(Fraction(value) for value in (3, -7, 0, 3))
    f6 = tuple(Fraction(value) for value in (4, 0, -7, 4))
    rows = []
    for q in (3, 5, 7, 9):
        optimal = optimal_unit_response_coefficients(q)
        denominator = 9 * q * q + 16
        cleared = (denominator, -21 * q * q, -28, denominator)
        if trace_coordinates(cleared) != (-denominator, 0, 0):
            raise ArithmeticError("cleared optimal filter has the wrong trace")
        if 3 * optimal[1] + 4 * optimal[2] != -7:
            raise ArithmeticError("optimal coefficients violate the nuisance equation")
        computed = haar_variance(optimal, q)
        formula = optimal_unit_response_variance(q)
        if computed != formula:
            raise ArithmeticError("optimal variance formula failed")
        f4_unit = haar_variance(tuple(value / 3 for value in f4), q)
        f6_unit = haar_variance(tuple(value / 4 for value in f6), q)
        expected_difference = Fraction(49 * q**4 * (9 * q * q - 16), 144)
        if f6_unit - f4_unit != expected_difference or expected_difference <= 0:
            raise ArithmeticError("sparse Haar-variance comparison failed")
        rows.append(
            {
                "q": q,
                "optimal_coefficients_c2_c4_c6_c8": [
                    _fraction_pair(value) for value in optimal
                ],
                "optimal_unit_response_variance": _fraction_pair(computed),
                "F4_unit_response_variance": _fraction_pair(f4_unit),
                "F6_unit_response_variance": _fraction_pair(f6_unit),
            }
        )
    return {
        "orthogonality_input": (
            "r_D(2j)=q^j*chi_(2j,0)(U_D), and the four nontrivial irreducible USp(4) characters are Haar-orthonormal"
        ),
        "general_variance": "c2^2*q^2+c4^2*q^4+c6^2*q^6+c8^2*q^8",
        "F4_variance": "9*q^8+49*q^4+9*q^2",
        "F4_unit_cusp_response_variance": "q^8+(49/9)*q^4+q^2",
        "F6_variance": "16*q^8+49*q^6+16*q^2",
        "F6_unit_cusp_response_variance": "q^8+(49/16)*q^6+q^2",
        "sparse_comparison": ("V(F6/4)-V(F4/3)=49*q^4*(9*q^2-16)/144>0 for odd q>=3"),
        "integral_unit_response_optimum": {
            "filter": "H=r8-r6-r4+r2",
            "variance": "q^8+q^6+q^4+q^2",
            "all_integral_unit_response_filters": (
                "H_k=r8+(-1-4*k)*r4+(-1+3*k)*r6+r2, k in Z"
            ),
            "difference_from_H": (
                "V(H_k)-V(H)=q^4*k*((8-6*q^2)+(16+9*q^2)*k), "
                "strictly positive for every nonzero integer k and odd q>=3"
            ),
        },
        "optimal_denominator": "Delta=9*q^2+16",
        "optimal_unit_response_filter": ("G_q=r8+r2-(21*q^2/Delta)*r4-(28/Delta)*r6"),
        "optimal_variance": "q^8+q^2+49*q^6/Delta",
        "completion_of_square": (
            "under c6=(-7-3*c4)/4, V-V_min=(q^4*Delta/16)*(c4+21*q^2/Delta)^2"
        ),
        "cleared_integer_filter": (
            "Delta*(r8+r2)-21*q^2*r4-28*r6, with marked trace -Delta*Theta_(8,2)(q)"
        ),
        "exact_numeric_checks": rows,
    }


def _spectroscopy_certificate(theta_controls: Mapping[int, int]) -> dict[str, object]:
    expected_updates = len(theta_controls) * (MAX_TOWER_EXPONENT - 1)
    if expected_updates > MAX_RECURRENCE_UPDATES:
        raise RuntimeError("tower recurrence-update cap exceeded")

    panels = []
    updates = 0
    for p, a_p in theta_controls.items():
        theta = hecke_trace_tower(p, a_p, MAX_TOWER_EXPONENT)
        updates += MAX_TOWER_EXPONENT - 1
        raw = tuple(-theta[r] - p**r - 6 for r in range(MAX_TOWER_EXPONENT + 1))
        polynomial = raw_trace_recurrence_polynomial(p, a_p)
        residuals = _recurrence_residual(raw, polynomial)
        if any(residuals):
            raise ArithmeticError("raw four-root recurrence failed")
        cusp = tuple(-3 * value for value in theta)
        quadratic_residuals = tuple(
            cusp[r] - a_p * cusp[r - 1] + p**7 * cusp[r - 2]
            for r in range(2, len(cusp))
        )
        if any(quadratic_residuals):
            raise ArithmeticError("cusp-isolated Hecke recurrence failed")
        panels.append(
            {
                "p": p,
                "a_p": a_p,
                "theta_powers_r0_through_8": list(theta),
                "raw_T_(8,0)_r0_through_8": list(raw),
                "F4_marked_trace_r0_through_8": list(cusp),
                "raw_recurrence_polynomial_low_to_high": list(polynomial),
                "raw_recurrence_residuals": list(residuals),
                "F4_quadratic_recurrence_residuals": list(quadratic_residuals),
            }
        )
    return {
        "good_prime_setup": (
            "alpha_p+beta_p=a_p, alpha_p*beta_p=p^7, Theta_(8,2)(p^r)=alpha_p^r+beta_p^r"
        ),
        "raw_trace_roots": ["alpha_p", "beta_p", "p", "1"],
        "raw_trace_formula": ("T_(8,0)(p^r)=-alpha_p^r-beta_p^r-p^r-6*1^r"),
        "raw_annihilator": "(X^2-a_p*X+p^7)*(X-p)*(X-1)",
        "inverse_filter_effect": (
            "the two nuisance equations kill the p and 1 amplitudes exactly, leaving -c8*(alpha_p^r+beta_p^r)"
        ),
        "isolated_recurrence": "C_r=a_p*C_(r-1)-p^7*C_(r-2)",
        "formal_r0_convention": "Theta_(8,2)(1)=2; r>=1 are the prime-power field traces",
        "panels": panels,
        "actual_tower_recurrence_updates": updates,
    }


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    theorem_sources = _load_sources(THEOREM_SOURCE_NAMES)
    theta_controls = _validate_source_semantics(theorem_sources)

    classification = _classification_certificate()
    haar = _haar_certificate()
    spectroscopy = _spectroscopy_certificate(theta_controls)

    held_out_sources = _load_sources(HELD_OUT_SOURCE_NAMES)
    family_rows = _extract_family_rows(held_out_sources["balanced"])
    tower_updates = int(spectroscopy["actual_tower_recurrence_updates"])
    expected_atoms, expected_updates = _preflight_held_out_work(
        family_rows,
        tower_updates,
    )
    updates = [tower_updates]
    atoms_seen = [0]
    held_out = [
        _held_out_panel(
            row,
            theta_controls[int(row["q"])],
            updates,
            atoms_seen,
        )
        for row in family_rows
    ]
    if [row["q"] for row in held_out] != [3, 5, 7]:
        raise ArithmeticError("held-out field panel changed")
    expected_diagnostics = {
        3: ((75, 0, 87), -216, Fraction(85916, 3), 3672),
        5: ((1300, 0, 1200), 12600, Fraction(1672701534, 625), 102500),
        7: ((7434, 0, 6972), -128016, Fraction(4844515276200, 117649), 2535456),
    }
    for row in held_out:
        q = int(row["q"])
        signs, total, variance, stratum_total = expected_diagnostics[q]
        observed_signs = row["sign_counts"]
        observed_variance = Fraction(*row["family_centered_variance_F4"])
        zero_stratum = row["zero_stratum"]
        if (
            (
                observed_signs["negative"],
                observed_signs["zero"],
                observed_signs["positive"],
            )
            != signs
            or row["observed_total_F4"] != total
            or observed_variance != variance
            or zero_stratum["signed_total_F4"] != stratum_total
        ):
            raise ArithmeticError("held-out diagnostic changed")

    actual_atoms = atoms_seen[0]
    if actual_atoms != expected_atoms or actual_atoms != sum(
        int(row["joint_law_atoms"]) for row in held_out
    ):
        raise ArithmeticError("source-atom accounting mismatch")
    total_updates = updates[0]
    if total_updates != expected_updates:
        raise ArithmeticError("recurrence-update accounting mismatch")
    lattice_points = (2 * LATTICE_REGRESSION_RADIUS + 1) ** 2
    if (
        actual_atoms > MAX_SOURCE_ATOMS
        or total_updates > MAX_RECURRENCE_UPDATES
        or lattice_points > MAX_LATTICE_REGRESSION_POINTS
    ):
        raise RuntimeError("resource cap exceeded")
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_inverse_cusp_trace_filters.v1",
        "status": "PROVED_EXACT_COROLLARY_OF_SOURCE_LOCKED_MARKED_TRACE_THEOREMS",
        "scope": {
            "family": "monic squarefree quintics D in F_q[T]",
            "q": "every odd prime power",
            "coefficient_support": ["r_D(2)", "r_D(4)", "r_D(6)", "r_D(8)"],
            "arithmetic": "exact integer and Fraction arithmetic",
            "numeric_approximations": 0,
        },
        "source_trace_inputs": {
            "T_(2,0)(q)": "q-1",
            "T_(4,0)(q)": "-3",
            "T_(6,0)(q)": "-4",
            "T_(8,0)(q)": "-Theta_(8,2)(q)-q-6",
        },
        "classification_theorem": classification,
        "haar_variance_theorem": haar,
        "prime_power_spectroscopy": spectroscopy,
        "held_out_F4_diagnostics": held_out,
        "source_manifest": {
            name: {
                "path": str(lock["path"].relative_to(ROOT)).replace("\\", "/"),
                "payload_sha256": lock["payload"],
                "sha256_lf_normalized": lock["lf"],
            }
            for name, lock in SOURCE_LOCKS.items()
        },
        "resource_contract": {
            "maximum_source_atoms": MAX_SOURCE_ATOMS,
            "actual_source_atoms": actual_atoms,
            "maximum_recurrence_updates": MAX_RECURRENCE_UPDATES,
            "actual_recurrence_updates": total_updates,
            "maximum_tower_exponent": MAX_TOWER_EXPONENT,
            "maximum_lattice_regression_points": MAX_LATTICE_REGRESSION_POINTS,
            "actual_lattice_regression_points": lattice_points,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "new_finite_fields_enumerated": 0,
            "new_curves_enumerated": 0,
            "held_out_joint_laws_iterated_only_after_trace_theorem_validation": True,
            "held_out_source_parsed_only_after_theorem_certificates": True,
        },
        "firewalls": [
            "This packet is an exact inverse-design corollary of source-locked marked family trace theorems; it does not re-prove those source theorems.",
            "Haar variance is a compact-group L2 calculation and is not the finite arithmetic-family variance.",
            "The q=3,5,7 diagnostics are held-out source replays and do not prove an all-q sign or variance law.",
            "The preferred sparse filter F4 has mixed sign in every held-out family; no memberwise sign claim is made.",
            "No RH, GRH, novelty, motive, compatible-system, or global Euler-product claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("inverse-filter replay exceeded wall cap")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fixture = build_fixture()
    rendered = (
        json.dumps(
            fixture,
            allow_nan=False,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8")
        print(f"OK: wrote {OUTPUT_PATH}")
        return 0
    if args.check:
        stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: inverse cusp-trace filter fixture matches {OUTPUT_PATH}")
        return 0
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
