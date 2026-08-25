#!/usr/bin/env python3
"""Exact endpoint-three zero stratum for the native q-adic wavelet."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "native_qadic_wavelet_zero_stratum.json"
NOTE_PATH = HERE / "NATIVE_QADIC_WAVELET_ZERO_STRATUM.md"
TEST_PATH = ROOT / "tests" / "test_native_qadic_wavelet_zero_stratum.py"

NATIVE_NOTE_PATH = HERE / "NATIVE_QADIC_RECIPROCAL_WAVELET_SPECTROSCOPY.md"
NATIVE_PRODUCER_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.py"
NATIVE_FIXTURE_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
NATIVE_TEST_PATH = (
    ROOT / "tests" / "test_native_qadic_reciprocal_wavelet_spectroscopy.py"
)
BALANCED_PRODUCER_PATH = HERE / "balanced_control_family_scan.py"
BALANCED_FIXTURE_PATH = HERE / "balanced_control_family_scan.json"
AFFINE_PRODUCER_PATH = HERE / "genus2_affine_orbits.py"
AFFINE_FIXTURE_PATH = HERE / "genus2_affine_orbits.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "native_note": {
        "path": NATIVE_NOTE_PATH,
        "lf_sha256": "b19f8f129d348bd9351c80f50908a220c3418902ef28cdb180baa0ece6a97ff6",
    },
    "native_producer": {
        "path": NATIVE_PRODUCER_PATH,
        "lf_sha256": "051264601cdb72bb75e660c2bbfc657cf892e599f689a2cd10d355d7dae257fb",
    },
    "native_fixture": {
        "path": NATIVE_FIXTURE_PATH,
        "lf_sha256": "aef506afa6b9b29f10528b634f45c7eab96abc36c6cd2de886262e834fcb2d43",
        "payload_sha256": "4e366316c6d55488b41e0104f6bee6c947220d7989ea7aa1381b5d72a099b882",
    },
    "native_test": {
        "path": NATIVE_TEST_PATH,
        "lf_sha256": "ceee093e9258f7ca13aa82d37e4f37cc0b7399321da80cab53cd1a12c36479f9",
    },
    "balanced_producer": {
        "path": BALANCED_PRODUCER_PATH,
        "lf_sha256": "7192fa26b0ea17cb68cff288620ea4dfb124e07807986d9c74fbd37e66087d3b",
    },
    "balanced_fixture": {
        "path": BALANCED_FIXTURE_PATH,
        "lf_sha256": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
        "payload_sha256": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
    },
    "affine_producer": {
        "path": AFFINE_PRODUCER_PATH,
        "lf_sha256": "32e440750b2832ec4cc84473187b4b1aa6396eda87c64f5ac845b2a96dc88f08",
    },
    "affine_fixture": {
        "path": AFFINE_FIXTURE_PATH,
        "lf_sha256": "171a6a289bc8822aebae8b5494eeb70ebc7f54b84153e9ca1cbefc187cf12a7a",
        "payload_sha256": "9f55481e43e096d7495d1c2966634e24b69ea15b986d5777af79efe9627a98d1",
    },
}

MAX_SOURCE_ATOMS = 4096
MAX_RECURRENCE_UPDATES = 4096
MAX_WAVELET_COORDINATE_CHECKS = 1024
MAX_SYMBOLIC_TERMS = 256
MAX_WALL_SECONDS = 5.0

Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, int]


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


def _relative(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def _load_sources() -> dict[str, dict[str, object]]:
    for name, lock in SOURCE_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError(f"source path is not a Path: {name}")
        if _lf_sha256(path) != lock["lf_sha256"]:
            raise RuntimeError(f"source LF lock failed: {name}")

    loaded: dict[str, dict[str, object]] = {}
    for name in ("native_fixture", "balanced_fixture", "affine_fixture"):
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError(f"fixture path is not a Path: {name}")
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"locked fixture is not an object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != lock["payload_sha256"] or claimed != _canonical_sha256(payload):
            raise ValueError(f"source payload lock failed: {name}")
        loaded[name] = value
    return loaded


def _poly_clean(value: Polynomial) -> Polynomial:
    return {
        monomial: coefficient for monomial, coefficient in value.items() if coefficient
    }


def _poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
    return _poly_clean(result)


def _poly_scale(coefficient: int, value: Polynomial) -> Polynomial:
    return _poly_clean(
        {monomial: coefficient * entry for monomial, entry in value.items()}
    )


def _poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    result: Polynomial = {}
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_monomial[index] + right_monomial[index] for index in range(3)
            )
            result[monomial] = (
                result.get(monomial, 0) + left_coefficient * right_coefficient
            )
    return _poly_clean(result)


def _poly_sub(left: Polynomial, right: Polynomial) -> Polynomial:
    return _poly_add(left, _poly_scale(-1, right))


def symbolic_certificate() -> dict[str, object]:
    """Prove the endpoint-three reduction by exact polynomial arithmetic."""
    one: Polynomial = {(0, 0, 0): 1}
    a_variable: Polynomial = {(1, 0, 0): 1}
    b_variable: Polynomial = {(0, 1, 0): 1}
    q_variable: Polynomial = {(0, 0, 1): 1}
    a_squared = _poly_mul(a_variable, a_variable)
    r1 = _poly_scale(-1, a_variable)
    r2 = _poly_sub(a_squared, b_variable)
    r3 = _poly_scale(
        -1,
        _poly_mul(
            a_variable,
            _poly_add(_poly_sub(a_squared, _poly_scale(2, b_variable)), q_variable),
        ),
    )
    rational_coordinate = _poly_sub(r3, r2)
    radical_coordinate = _poly_add(_poly_scale(-1, r2), r1)

    expected_r1: Polynomial = {(1, 0, 0): -1}
    expected_r2: Polynomial = {(2, 0, 0): 1, (0, 1, 0): -1}
    expected_r3: Polynomial = {
        (3, 0, 0): -1,
        (1, 1, 0): 2,
        (1, 0, 1): -1,
    }
    expected_rational: Polynomial = {
        (3, 0, 0): -1,
        (2, 0, 0): -1,
        (1, 1, 0): 2,
        (1, 0, 1): -1,
        (0, 1, 0): 1,
    }
    expected_radical: Polynomial = {
        (2, 0, 0): -1,
        (1, 0, 0): -1,
        (0, 1, 0): 1,
    }
    identities = (
        (r1, expected_r1),
        (r2, expected_r2),
        (r3, expected_r3),
        (rational_coordinate, expected_rational),
        (radical_coordinate, expected_radical),
    )
    if any(actual != expected for actual, expected in identities):
        raise ArithmeticError("endpoint-three polynomial certificate failed")

    b_on_radical_zero = _poly_add(a_squared, a_variable)
    reduced_r2 = _poly_sub(a_squared, b_on_radical_zero)
    reduced_r3 = _poly_scale(
        -1,
        _poly_mul(
            a_variable,
            _poly_add(
                _poly_sub(a_squared, _poly_scale(2, b_on_radical_zero)),
                q_variable,
            ),
        ),
    )
    reduced_rational = _poly_sub(reduced_r3, reduced_r2)
    expected_reduced = _poly_mul(
        a_variable,
        _poly_sub(
            _poly_mul(_poly_add(a_variable, one), _poly_add(a_variable, one)),
            q_variable,
        ),
    )
    if reduced_rational != expected_reduced:
        raise ArithmeticError("radical-zero substitution certificate failed")

    k_polynomial = _poly_sub(
        _poly_mul(q_variable, a_squared), _poly_mul(b_variable, b_variable)
    )
    expected_k: Polynomial = {(2, 0, 1): 1, (0, 2, 0): -1}
    if k_polynomial != expected_k:
        raise ArithmeticError("K polynomial certificate failed")

    terms_checked = sum(
        len(value)
        for value in (
            r1,
            r2,
            r3,
            rational_coordinate,
            radical_coordinate,
            reduced_rational,
            expected_reduced,
            k_polynomial,
        )
    )
    if terms_checked > MAX_SYMBOLIC_TERMS:
        raise RuntimeError("symbolic-term cap exceeded")
    return {
        "r_1": "-a",
        "r_2": "a^2-b",
        "r_3": "-a*(a^2-2*b+q)",
        "W_3_Q_sqrt_q_coordinates": {
            "rational": "r_3-r_2=-a^3-a^2+2*a*b-a*q+b",
            "sqrt_q": "-r_2+r_1=b-a^2-a",
        },
        "radical_zero_substitution": "b=a^2+a",
        "reduced_rational_coordinate": "a*((a+1)^2-q)",
        "K_D": "q*a^2-b^2",
        "terms_checked": terms_checked,
    }


def reciprocal_coefficients(
    a_coefficient: int, b_coefficient: int, q: int, endpoint: int
) -> tuple[int, ...]:
    """Return r_0 through r_endpoint for the reciprocal genus-two numerator."""
    if q < 3 or q % 2 == 0 or endpoint < 0:
        raise ValueError(
            "q must be odd and at least three; endpoint must be nonnegative"
        )
    values = [1]
    for degree in range(1, endpoint + 1):
        value = -a_coefficient * values[degree - 1]
        if degree >= 2:
            value -= b_coefficient * values[degree - 2]
        if degree >= 3:
            value -= q * a_coefficient * values[degree - 3]
        if degree >= 4:
            value -= q * q * values[degree - 4]
        values.append(value)
    return tuple(values)


def wavelet_coordinates(reciprocal: tuple[int, ...], endpoint: int) -> tuple[int, int]:
    """Return R,S for W_endpoint=R+S*sqrt(q)."""
    if endpoint < 0 or endpoint >= len(reciprocal):
        raise ValueError("endpoint must be nonnegative and covered")

    def coefficient(index: int) -> int:
        return reciprocal[index] if index >= 0 else 0

    return (
        coefficient(endpoint) - coefficient(endpoint - 1),
        -coefficient(endpoint - 1) + coefficient(endpoint - 2),
    )


def is_nonsquare_integer(q: int) -> bool:
    """Return whether positive integer q is not an integer square."""
    return q > 0 and math.isqrt(q) ** 2 != q


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _locked_family_rows(
    source: dict[str, object], outer_key: str
) -> list[dict[str, object]]:
    container: object = source
    if outer_key:
        container = source.get(outer_key)
        if not isinstance(container, dict):
            raise TypeError(f"locked family container missing: {outer_key}")
    families = container.get("families") if isinstance(container, dict) else None
    if not isinstance(families, list):
        raise TypeError("locked family rows missing")
    if not all(isinstance(row, dict) for row in families):
        raise TypeError("locked family row is not an object")
    return families


def _native_zero_count(panel: dict[str, object], endpoint: int) -> int:
    rows = panel.get("wavelet_rows")
    if not isinstance(rows, list):
        raise TypeError("native panel lacks wavelet rows")
    matches = [
        row for row in rows if isinstance(row, dict) and row.get("endpoint") == endpoint
    ]
    if len(matches) != 1:
        raise ValueError(f"native endpoint {endpoint} is not unique")
    counts = matches[0].get("sign_counts")
    if not isinstance(counts, dict) or not isinstance(counts.get("zero"), int):
        raise TypeError("native zero count missing")
    return int(counts["zero"])


def _orbit_types(
    zero_summary: dict[str, object], group_order: int
) -> list[dict[str, int]]:
    histogram = zero_summary.get("orbit_size_histogram")
    stabilizers = zero_summary.get("stabilizer_order_histogram")
    if not isinstance(histogram, dict) or not isinstance(stabilizers, dict):
        raise TypeError("affine zero-orbit histograms missing")
    reconstructed_stabilizers: dict[str, int] = {}
    types: list[dict[str, int]] = []
    for size_text, count in sorted(histogram.items(), key=lambda item: int(item[0])):
        orbit_size = int(size_text)
        if not isinstance(count, int) or group_order % orbit_size:
            raise ArithmeticError("invalid zero-orbit size")
        stabilizer_order = group_order // orbit_size
        reconstructed_stabilizers[str(stabilizer_order)] = (
            reconstructed_stabilizers.get(str(stabilizer_order), 0) + count
        )
        types.append(
            {
                "orbit_size": orbit_size,
                "stabilizer_order": stabilizer_order,
                "orbit_count": count,
            }
        )
    if reconstructed_stabilizers != stabilizers:
        raise ArithmeticError("orbit-size and stabilizer histograms disagree")
    return types


def _frozen_panels(
    native: dict[str, object],
    balanced: dict[str, object],
    affine: dict[str, object],
) -> tuple[list[dict[str, object]], dict[str, int]]:
    native_rows = native.get("exact_finite_panels")
    if not isinstance(native_rows, list) or not all(
        isinstance(row, dict) for row in native_rows
    ):
        raise TypeError("native finite panels missing")
    balanced_rows = _locked_family_rows(balanced, "frozen_enumeration_facts")
    affine_rows = _locked_family_rows(affine, "")
    native_by_q = {int(row["q"]): row for row in native_rows}
    affine_by_q = {int(row["q"]): row for row in affine_rows}
    if sorted(native_by_q) != [3, 5, 7] or sorted(affine_by_q) != [3, 5, 7]:
        raise ValueError("locked q panels changed")

    total_atoms = 0
    recurrence_updates = 0
    coordinate_checks = 0
    panels: list[dict[str, object]] = []
    for family in balanced_rows:
        q = family.get("q")
        members = family.get("member_count")
        joint = family.get("joint_a_D_b_D_law")
        if (
            not isinstance(q, int)
            or not isinstance(members, int)
            or not isinstance(joint, dict)
        ):
            raise TypeError("invalid balanced family row")
        if q not in native_by_q or q not in affine_by_q or not is_nonsquare_integer(q):
            raise ValueError("balanced family is outside the locked nonsquare panels")
        atoms = joint.get("atoms")
        if not isinstance(atoms, list):
            raise TypeError("balanced joint histogram lacks atoms")
        total_atoms += len(atoms)
        if total_atoms > MAX_SOURCE_ATOMS:
            raise RuntimeError("source-atom cap exceeded")
        member_mass = 0
        coefficient_zero_count = 0
        k_zero_count = 0
        w3_zero_count = 0
        w7_zero_count = 0
        for atom in atoms:
            if not isinstance(atom, dict):
                raise TypeError("joint histogram atom is not an object")
            a_coefficient = atom.get("a_D")
            b_coefficient = atom.get("b_D")
            count = atom.get("member_count")
            if not all(
                isinstance(value, int)
                for value in (a_coefficient, b_coefficient, count)
            ):
                raise TypeError("joint histogram atom is nonintegral")
            a_value = int(a_coefficient)
            b_value = int(b_coefficient)
            atom_count = int(count)
            member_mass += atom_count
            reciprocal = reciprocal_coefficients(a_value, b_value, q, 7)
            recurrence_updates += 7
            if recurrence_updates > MAX_RECURRENCE_UPDATES:
                raise RuntimeError("recurrence-update cap exceeded")
            w3_zero = wavelet_coordinates(reciprocal, 3) == (0, 0)
            w7_zero = wavelet_coordinates(reciprocal, 7) == (0, 0)
            coordinate_checks += 2
            if coordinate_checks > MAX_WAVELET_COORDINATE_CHECKS:
                raise RuntimeError("wavelet-coordinate cap exceeded")
            coefficient_zero = a_value == 0 and b_value == 0
            k_zero = q * a_value * a_value - b_value * b_value == 0
            if w3_zero != coefficient_zero or k_zero != coefficient_zero:
                raise ArithmeticError("frozen endpoint-three equivalence failed")
            if w7_zero and not coefficient_zero:
                raise ArithmeticError("frozen endpoint-seven off-stratum zero found")
            if coefficient_zero:
                coefficient_zero_count += atom_count
            if k_zero:
                k_zero_count += atom_count
            if w3_zero:
                w3_zero_count += atom_count
            if w7_zero:
                w7_zero_count += atom_count
        if member_mass != members:
            raise ArithmeticError("balanced histogram mass mismatch")

        native_panel = native_by_q[q]
        affine_panel = affine_by_q[q]
        native_w3 = _native_zero_count(native_panel, 3)
        native_w7 = _native_zero_count(native_panel, 7)
        sign_summaries = affine_panel.get("sign_summaries")
        group = affine_panel.get("group")
        if not isinstance(sign_summaries, dict) or not isinstance(group, dict):
            raise TypeError("affine sign or group summary missing")
        zero_summary = sign_summaries.get("zero")
        group_order = group.get("order")
        if not isinstance(zero_summary, dict) or not isinstance(group_order, int):
            raise TypeError("affine zero summary missing")
        affine_k_zero = zero_summary.get("member_count")
        if not isinstance(affine_k_zero, int):
            raise TypeError("affine K-zero count missing")
        counts = {
            coefficient_zero_count,
            k_zero_count,
            w3_zero_count,
            w7_zero_count,
            native_w3,
            native_w7,
            affine_k_zero,
        }
        if len(counts) != 1:
            raise ArithmeticError("locked zero counts do not authenticate each other")
        orbit_types = _orbit_types(zero_summary, group_order)
        orbit_count = zero_summary.get("orbit_count")
        if (
            not isinstance(orbit_count, int)
            or sum(row["orbit_count"] for row in orbit_types) != orbit_count
        ):
            raise ArithmeticError("zero-orbit count mismatch")
        panels.append(
            {
                "q": q,
                "members": members,
                "joint_histogram_atoms": len(atoms),
                "W_3_zero_count": w3_zero_count,
                "K_D_zero_count": k_zero_count,
                "a_D_b_D_zero_count": coefficient_zero_count,
                "W_7_zero_count": w7_zero_count,
                "W_7_off_stratum_zero_count": 0,
                "affine_zero_orbit_count": orbit_count,
                "affine_zero_orbit_types": orbit_types,
                "marked_stack_mass": _fraction_pair(
                    Fraction(affine_k_zero, group_order)
                ),
            }
        )

    expected = {
        3: {
            "zero_count": 12,
            "orbit_types": [{"orbit_size": 6, "stabilizer_order": 1, "orbit_count": 2}],
            "stack_mass": [2, 1],
        },
        5: {
            "zero_count": 50,
            "orbit_types": [
                {"orbit_size": 5, "stabilizer_order": 4, "orbit_count": 2},
                {"orbit_size": 20, "stabilizer_order": 1, "orbit_count": 2},
            ],
            "stack_mass": [5, 2],
        },
        7: {
            "zero_count": 336,
            "orbit_types": [
                {"orbit_size": 42, "stabilizer_order": 1, "orbit_count": 8}
            ],
            "stack_mass": [8, 1],
        },
    }
    for panel in panels:
        control = expected[int(panel["q"])]
        if panel["W_3_zero_count"] != control["zero_count"]:
            raise ArithmeticError("frozen zero-count control changed")
        if panel["affine_zero_orbit_types"] != control["orbit_types"]:
            raise ArithmeticError("frozen orbit tomography changed")
        if panel["marked_stack_mass"] != control["stack_mass"]:
            raise ArithmeticError("frozen stack mass changed")

    resources = {
        "source_atoms": total_atoms,
        "recurrence_updates": recurrence_updates,
        "wavelet_coordinate_checks": coordinate_checks,
    }
    return panels, resources


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    sources = _load_sources()
    certificate = symbolic_certificate()
    panels, actual_resources = _frozen_panels(
        sources["native_fixture"],
        sources["balanced_fixture"],
        sources["affine_fixture"],
    )
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("zero-stratum replay exceeded wall cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.native_qadic_wavelet_zero_stratum.v1",
        "status": "PROVED_ALL_NONSQUARE_ODD_PRIME_POWERS_AND_FROZEN_TOMOGRAPHY",
        "scope": {
            "all_q": (
                "q is an odd prime power that is not a square as an integer; "
                "a_D,b_D are integral genus-two Frobenius coefficients"
            ),
            "frozen": "complete source-locked q=3,5,7 histograms and affine orbit summaries",
        },
        "definition": {
            "P_D(u)": "1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4",
            "reciprocal": "1/P_D(u)=sum_(n>=0) r_D(n)*u^n",
            "wavelet": ("W_D(N)=(r_D(N)-r_D(N-1))+sqrt(q)*(-r_D(N-1)+r_D(N-2))"),
            "K_D": "q*a_D^2-b_D^2",
        },
        "endpoint_three_theorem": {
            "statement": "W_D(3)=0 iff K_D=0 iff (a_D,b_D)=(0,0)",
            "quantifier": "every nonsquare odd prime power q and every family member D",
            "polynomial_certificate": certificate,
            "nonsquare_steps": [
                "R+S*sqrt(q)=0 with R,S integers implies R=S=0",
                "(a+1)^2=q has no integral solution",
                "b^2=q*a^2 has no nonzero integral solution",
            ],
        },
        "zero_stratum_spectral_theorem": {
            "numerator": "P_D(u)=1+q^2*u^4",
            "frobenius_polynomial": "x^4+q^2",
            "supersingular_certificate": (
                "every root is sqrt(q)*zeta with zeta^4=-1, hence zeta is a root of unity"
            ),
            "irreducibility_certificate": (
                "a rational quadratic factorization forces c^2=2*q or c^2=-2*q; "
                "the positive case is impossible because v_2(2*q) is odd"
            ),
            "F_q_simplicity": (
                "the irreducible rational Frobenius polynomial rules out a nontrivial "
                "F_q-isogeny factor"
            ),
            "reciprocal_coefficients": "r_(4*m)=(-q^2)^m and r_n=0 when 4 does not divide n",
            "wavelet_zero_endpoints": "W_D(N)=0 iff N is congruent to 3 modulo 4",
            "endpoint_range": "N>=0, using r_D(n)=0 for n<0",
        },
        "frozen_q_3_5_7_authentication": panels,
        "source_manifest": {
            name: {
                "path": _relative(lock["path"]),
                "lf_sha256": lock["lf_sha256"],
                **(
                    {"payload_sha256": lock["payload_sha256"]}
                    if "payload_sha256" in lock
                    else {}
                ),
            }
            for name, lock in SOURCE_LOCKS.items()
        },
        "artifact_manifest": {
            "producer_lf_sha256": _lf_sha256(Path(__file__)),
            "note_lf_sha256": _lf_sha256(NOTE_PATH),
            "test_lf_sha256": _lf_sha256(TEST_PATH),
        },
        "resource_contract": {
            "maximum_source_atoms": MAX_SOURCE_ATOMS,
            "actual_source_atoms": actual_resources["source_atoms"],
            "maximum_recurrence_updates": MAX_RECURRENCE_UPDATES,
            "actual_recurrence_updates": actual_resources["recurrence_updates"],
            "maximum_wavelet_coordinate_checks": MAX_WAVELET_COORDINATE_CHECKS,
            "actual_wavelet_coordinate_checks": actual_resources[
                "wavelet_coordinate_checks"
            ],
            "maximum_symbolic_terms": MAX_SYMBOLIC_TERMS,
            "actual_symbolic_terms": certificate["terms_checked"],
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "new_finite_fields_enumerated": 0,
            "new_family_members_enumerated": 0,
        },
        "firewalls": [
            "The endpoint-three converse is proved only when q is nonsquare as an integer.",
            "The endpoint-seven off-stratum exclusion is authenticated only for q=3,5,7.",
            "The counts 12, 50, and 336 are frozen data, not an all-q count law.",
            "Supersingularity and F_q-simplicity classify any member on the proved zero stratum; they do not assert that the stratum is nonempty for every q.",
            "No RH, GRH, equidistribution, motive-identification, or novelty claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fixture = build_fixture()
    if args.write:
        with OUTPUT_PATH.open("w", encoding="utf-8", newline="\n") as stream:
            json.dump(fixture, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write("\n")
        print(f"OK: wrote {OUTPUT_PATH}")
        return 0
    stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
    if stored != fixture:
        raise RuntimeError(f"fixture mismatch: rerun {Path(__file__).name} --write")
    print(f"OK: native q-adic wavelet zero-stratum fixture matches {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
