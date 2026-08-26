#!/usr/bin/env python3
"""Native q-adic reciprocal-wavelet spectroscopy on locked genus-two laws."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import unicodedata
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "native_qadic_reciprocal_wavelet_spectroscopy.json"
NOTE_PATH = HERE / "NATIVE_QADIC_RECIPROCAL_WAVELET_SPECTROSCOPY.md"
TEST_PATH = ROOT / "tests" / "test_native_qadic_reciprocal_wavelet_spectroscopy.py"

BALANCED_PATH = HERE / "balanced_control_family_scan.json"
NORM_OBSTRUCTION_PATH = HERE / "canonical_detector_norm_lattice_obstruction.json"
Q_SCAN_PATH = HERE / "genus2_q_scan.json"
AFFINE_PATH = HERE / "genus2_affine_orbits.json"

SOURCE_LOCKS = {
    "balanced": {
        "path": BALANCED_PATH,
        "payload": "50fd136eb0483387246766c5f2426c3e727c69cd9a89943f9268368db0f9d39c",
        "lf": "c3494ae852fda4e754b3b0da7cb30a26e3e38ec1c87e2619cd6fee6cdc68b68e",
    },
    "norm_obstruction": {
        "path": NORM_OBSTRUCTION_PATH,
        "payload": None,
        "lf": "3a2aa44f759686017495b4b2102f93d6891454856cf66d34cc9ce3750b798fa4",
    },
    "q_scan": {
        "path": Q_SCAN_PATH,
        "payload": "80a28d820e45b2548e3e4b482982ef8313c8919f4a3fb9cc2c0b622b244870b5",
        "lf": "b49b7e2803401904b0bc1f82eb442bf1d8e81bdeb1ec388ff7fb14e7e5628dc6",
    },
    "affine": {
        "path": AFFINE_PATH,
        "payload": "9f55481e43e096d7495d1c2966634e24b69ea15b986d5777af79efe9627a98d1",
        "lf": "171a6a289bc8822aebae8b5494eeb70ebc7f54b84153e9ca1cbefc187cf12a7a",
    },
}

MIN_ENDPOINT = 2
MAX_ENDPOINT = 8
MAX_SOURCE_ATOMS = 512
MAX_ATOM_ENDPOINT_EVALUATIONS = 2048
MAX_RECURRENCE_UPDATES = 20_000
MAX_WALL_SECONDS = 4.0


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


def _load_sources() -> dict[str, dict[str, object]]:
    loaded: dict[str, dict[str, object]] = {}
    for name, lock in SOURCE_LOCKS.items():
        path = lock["path"]
        if not isinstance(path, Path) or _lf_sha256(path) != lock["lf"]:
            raise RuntimeError(f"source lock failed: {name}")
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source is not an object: {name}")
        expected_payload = lock["payload"]
        if expected_payload is not None:
            claimed = value.get("payload_sha256")
            payload = dict(value)
            payload.pop("payload_sha256", None)
            if claimed != expected_payload or claimed != _canonical_sha256(payload):
                raise ValueError(f"source payload failed: {name}")
        loaded[name] = value
    return loaded


def reciprocal_coefficients(
    a_coefficient: int, b_coefficient: int, q: int, endpoint: int
) -> tuple[int, ...]:
    """Coefficients r_n of 1/P_D(u), where P_D has genus-two reciprocity."""
    if q < 3 or endpoint < 0:
        raise ValueError("q>=3 and endpoint>=0 are required")
    values = [1]
    for n in range(1, endpoint + 1):
        value = -a_coefficient * values[n - 1]
        if n >= 2:
            value -= b_coefficient * values[n - 2]
        if n >= 3:
            value -= q * a_coefficient * values[n - 3]
        if n >= 4:
            value -= q * q * values[n - 4]
        values.append(value)
    return tuple(values)


def wavelet_coordinates(reciprocal: tuple[int, ...], endpoint: int) -> tuple[int, int]:
    """Coordinates R+S*sqrt(q) of the native q-adic wavelet."""
    if endpoint < 2 or endpoint >= len(reciprocal):
        raise ValueError("endpoint must be covered and at least two")
    return (
        reciprocal[endpoint] - reciprocal[endpoint - 1],
        -reciprocal[endpoint - 1] + reciprocal[endpoint - 2],
    )


def quadratic_sign(rational: int, radical: int, q: int) -> int:
    """Exact real sign of rational+radical*sqrt(q)."""
    if rational == 0:
        return (radical > 0) - (radical < 0)
    if radical == 0 or (rational > 0) == (radical > 0):
        return (rational > 0) - (rational < 0)
    comparison = rational * rational - q * radical * radical
    if comparison == 0:
        return 0
    return (
        (rational > 0) - (rational < 0)
        if comparison > 0
        else (radical > 0) - (radical < 0)
    )


def _fraction_pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def _extract_family_rows(balanced: dict[str, object]) -> list[dict[str, object]]:
    frozen = balanced.get("frozen_enumeration_facts")
    if not isinstance(frozen, dict):
        raise TypeError("balanced fixture lacks frozen facts")
    families = frozen.get("families")
    if not isinstance(families, list):
        raise TypeError("balanced fixture lacks families")
    return families


def _validate_source_semantics(sources: dict[str, dict[str, object]]) -> None:
    obstruction = sources["norm_obstruction"]
    theorem = obstruction.get("theorem")
    if not isinstance(theorem, dict):
        raise TypeError("norm obstruction theorem missing")
    if theorem.get("native_translation") != (
        "lambda preserves q^Z iff lambda=q^k for an integer k"
    ):
        raise ValueError("native norm-lattice translation theorem changed")

    q_scan = sources["q_scan"]
    target = q_scan.get("closed_formula_target")
    if not isinstance(target, dict):
        raise TypeError("q-scan exact formulas missing")
    profile = target.get("low_weight_character_profile")
    if not isinstance(profile, dict):
        raise TypeError("low-weight profile missing")
    if profile.get("mean_chi_(2,0)") != "1/q^3-1/q^4":
        raise ValueError("chi_(2,0) mean changed")
    if profile.get("mean_chi_(4,0)") != "-3/q^5":
        raise ValueError("chi_(4,0) mean changed")

    affine = sources["affine"]
    proof = affine.get("exact_proof")
    if not isinstance(proof, dict):
        raise TypeError("affine proof missing")
    law = proof.get("base_sum")
    if not isinstance(law, str) or "a transforms by chi_q(alpha)" not in law:
        raise ValueError("affine twist-parity law changed")


def _field_panel(row: dict[str, object], updates: list[int]) -> dict[str, object]:
    q = row.get("q")
    members = row.get("member_count")
    joint = row.get("joint_a_D_b_D_law")
    if (
        not isinstance(q, int)
        or not isinstance(members, int)
        or not isinstance(joint, dict)
    ):
        raise TypeError("invalid locked family row")
    atoms = joint.get("atoms")
    if not isinstance(atoms, list):
        raise TypeError("joint law lacks atoms")
    if len(atoms) > MAX_SOURCE_ATOMS:
        raise RuntimeError("source atom cap exceeded")

    endpoint_rows: list[dict[str, object]] = []
    even_trace_values: dict[str, int] = {}
    mean_reciprocal: dict[int, Fraction] = {
        endpoint: Fraction(0) for endpoint in range(MAX_ENDPOINT + 1)
    }
    parsed_atoms: list[tuple[int, int, int, tuple[int, ...]]] = []
    for atom in atoms:
        if not isinstance(atom, dict):
            raise TypeError("invalid joint-law atom")
        a_coefficient = atom.get("a_D")
        b_coefficient = atom.get("b_D")
        count = atom.get("member_count")
        if not all(
            isinstance(value, int) for value in (a_coefficient, b_coefficient, count)
        ):
            raise TypeError("nonintegral joint-law atom")
        reciprocal = reciprocal_coefficients(
            int(a_coefficient), int(b_coefficient), q, MAX_ENDPOINT
        )
        updates[0] += MAX_ENDPOINT
        if updates[0] > MAX_RECURRENCE_UPDATES:
            raise RuntimeError("recurrence update cap exceeded")
        parsed_atoms.append(
            (int(a_coefficient), int(b_coefficient), int(count), reciprocal)
        )
        for endpoint, value in enumerate(reciprocal):
            mean_reciprocal[endpoint] += Fraction(int(count) * value, members)

    if sum(count for _, _, count, _ in parsed_atoms) != members:
        raise ArithmeticError("joint-law mass mismatch")
    for endpoint in range(1, MAX_ENDPOINT + 1, 2):
        if mean_reciprocal[endpoint] != 0:
            raise ArithmeticError("odd reciprocal mean did not cancel")

    for endpoint in range(MIN_ENDPOINT, MAX_ENDPOINT + 1):
        signs: Counter[int] = Counter()
        coordinate_atoms: Counter[tuple[int, int]] = Counter()
        total_rational = 0
        total_radical = 0
        for _, _, count, reciprocal in parsed_atoms:
            rational, radical = wavelet_coordinates(reciprocal, endpoint)
            signs[quadratic_sign(rational, radical, q)] += count
            coordinate_atoms[(rational, radical)] += count
            total_rational += count * rational
            total_radical += count * radical
        if sum(signs.values()) != members:
            raise ArithmeticError("sign mass mismatch")
        expected_rational = (
            mean_reciprocal[endpoint]
            if endpoint % 2 == 0
            else -mean_reciprocal[endpoint - 1]
        )
        expected_radical = (
            mean_reciprocal[endpoint - 2]
            if endpoint % 2 == 0
            else -mean_reciprocal[endpoint - 1]
        )
        actual_rational = Fraction(total_rational, members)
        actual_radical = Fraction(total_radical, members)
        if (actual_rational, actual_radical) != (
            expected_rational,
            expected_radical,
        ):
            raise ArithmeticError("twist-parity wavelet identity failed")

        endpoint_rows.append(
            {
                "endpoint": endpoint,
                "sign_counts": {
                    "negative": signs[-1],
                    "zero": signs[0],
                    "positive": signs[1],
                },
                "mean_Q_sqrt_q_coordinates": {
                    "rational": _fraction_pair(actual_rational),
                    "sqrt_q": _fraction_pair(actual_radical),
                },
                "distinct_coordinate_atoms": len(coordinate_atoms),
                "memberwise_sign_is_mixed": signs[-1] > 0 and signs[1] > 0,
            }
        )
        if endpoint % 2 == 0:
            trace = q**3 * mean_reciprocal[endpoint]
            if trace.denominator != 1:
                raise ArithmeticError("marked symmetric-power trace is not integral")
            even_trace_values[f"T_({endpoint},0)"] = trace.numerator

    return {
        "q": q,
        "members": members,
        "joint_atoms": len(atoms),
        "reciprocal_means_0_through_8": {
            str(endpoint): _fraction_pair(mean_reciprocal[endpoint])
            for endpoint in range(MAX_ENDPOINT + 1)
        },
        "marked_symmetric_power_trace_values": even_trace_values,
        "wavelet_rows": endpoint_rows,
    }


def build_fixture() -> dict[str, object]:
    started = time.monotonic()
    sources = _load_sources()
    _validate_source_semantics(sources)
    updates = [0]
    panels = [
        _field_panel(row, updates) for row in _extract_family_rows(sources["balanced"])
    ]
    if [panel["q"] for panel in panels] != [3, 5, 7]:
        raise ValueError("locked field panel changed")
    total_atoms = sum(int(panel["joint_atoms"]) for panel in panels)
    atom_endpoint_evaluations = total_atoms * (MAX_ENDPOINT - MIN_ENDPOINT + 1)
    if atom_endpoint_evaluations > MAX_ATOM_ENDPOINT_EVALUATIONS:
        raise RuntimeError("atom-endpoint evaluation cap exceeded")

    finite_traces = {
        str(panel["q"]): panel["marked_symmetric_power_trace_values"]
        for panel in panels
    }
    expected_traces = {
        "3": {"T_(2,0)": 2, "T_(4,0)": -3, "T_(6,0)": -4, "T_(8,0)": -21},
        "5": {"T_(2,0)": 4, "T_(4,0)": -3, "T_(6,0)": -4, "T_(8,0)": 199},
        "7": {"T_(2,0)": 6, "T_(4,0)": -3, "T_(6,0)": -4, "T_(8,0)": -1029},
    }
    if finite_traces != expected_traces:
        raise ArithmeticError("symmetric-power spectroscopy controls changed")
    if not all(
        row["memberwise_sign_is_mixed"]
        for panel in panels
        for row in panel["wavelet_rows"]
    ):
        raise ArithmeticError("a native-wavelet panel lost mixed sign")
    if time.monotonic() - started > MAX_WALL_SECONDS:
        raise RuntimeError("native wavelet replay exceeded wall cap")

    payload: dict[str, object] = {
        "schema": "riemann.function_field.native_qadic_reciprocal_wavelet_spectroscopy.v1",
        "status": "PROVED_OPERATOR_AND_EXACT_FINITE_ARITHMETIC",
        "definition": {
            "global_numerator": "P_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4",
            "reciprocal_series": "1/P_D(u)=sum_(n>=0) r_D(n)*u^n",
            "inclusive_partial_sum": "M_D(N)=sum_(0<=n<=N) r_D(n)",
            "negative_endpoint_convention": "M_D(N)=r_D(N)=0 for N<0",
            "native_shift": "(S_q M)(N)=M(N-1)",
            "wavelet": "W_D(N)=(I-sqrt(q)*S_q)*(I-S_q)^2*M_D(N)",
            "coefficient_form": "W_D(N)=r_D(N)-(1+sqrt(q))*r_D(N-1)+sqrt(q)*r_D(N-2)",
        },
        "normalization_theorem": {
            "factorization": "(I-sqrt(q)*S_q)*(I-S_q)^2",
            "double_constant_zero": True,
            "sqrt_q_carrier_zero": True,
            "representation_identity": "r_D(n)/q^(n/2)=chi_(n,0)(U_D)",
            "symmetric_power_irreducibility": (
                "Sym^n(Standard) is the irreducible Sp4 representation of highest weight "
                "n*omega_1; both dimensions are binomial(n+3,3)"
            ),
            "marked_trace_bridge": "T_(n,0)(q)=q^3*E[r_D(n)] for even n",
            "twist_parity": "E[r_D(2k+1)]=0",
            "twist_pairing": (
                "The full AGL(1,F_q) action D(T)->alpha^-5*D(alpha*T+beta) "
                "sends a_D to chi(alpha)*a_D and fixes b_D; a nonsquare "
                "multiplier pairs P_D(u) with P_D(-u)"
            ),
            "mean_even_endpoint": "E[W_D(2k)]=E[r_D(2k)]+sqrt(q)*E[r_D(2k-2)]",
            "mean_odd_endpoint": "E[W_D(2k+1)]=-(1+sqrt(q))*E[r_D(2k)]",
        },
        "proved_all_q_trace_inputs": {
            "T_(2,0)": "q-1",
            "T_(4,0)": "-3",
            "source": "the exact low-weight character profile in the locked q-scan theorem",
        },
        "exact_finite_panels": panels,
        "spectroscopy_observation": {
            "T_(6,0)_three_field_values": [-4, -4, -4],
            "T_(8,0)_three_field_values": [-21, 199, -1029],
            "interpretation": (
                "The native filter packages adjacent symmetric-power traces. "
                "The weight-eight coordinate changes sign across the three locked characteristics, "
                "so it is a spectroscopy channel rather than a universal sign detector."
            ),
            "inference_firewall": (
                "The constant three-field T_(6,0) row and the three T_(8,0) values are exact finite data only; "
                "(q-3)(q-5)(q-7)Q(q) ambiguity forbids an all-q trace or cohomology promotion."
            ),
        },
        "source_manifest": {
            name: {
                "path": str(lock["path"].relative_to(ROOT)).replace("\\", "/"),
                "payload_sha256": lock["payload"],
                "lf_sha256": lock["lf"],
            }
            for name, lock in SOURCE_LOCKS.items()
        },
        "resource_contract": {
            "maximum_source_atoms": MAX_SOURCE_ATOMS,
            "actual_source_atoms": total_atoms,
            "maximum_atom_endpoint_evaluations": MAX_ATOM_ENDPOINT_EVALUATIONS,
            "actual_atom_endpoint_evaluations": atom_endpoint_evaluations,
            "maximum_recurrence_updates": MAX_RECURRENCE_UPDATES,
            "actual_recurrence_updates": updates[0],
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "new_finite_fields_enumerated": 0,
            "new_curves_enumerated": 0,
        },
        "firewalls": [
            "This is a project-defined native q-adic analogue, not literal dyadic XD, HCNC, or BPOE.",
            "It uses the complete global curve numerator and its reciprocal series; it does not supply the owner/cross-core arithmetic of canonical XD.",
            "Every endpoint in every q=3,5,7 panel has both signs, so purity and the native normalization do not create a memberwise sign.",
            "The finite T_(6,0) and T_(8,0) rows are not all-q theorems or named cohomology identifications.",
            "No RH, GRH, equidistribution, or novelty claim is made.",
        ],
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true")
    group.add_argument("--check", action="store_true")
    args = parser.parse_args()
    fixture = build_fixture()
    if args.write:
        OUTPUT_PATH.write_text(
            json.dumps(
                fixture,
                allow_nan=False,
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
            + "\n",
            encoding="utf-8",
        )
        print(f"OK: wrote {OUTPUT_PATH}")
        return 0
    if args.check:
        stored = json.loads(OUTPUT_PATH.read_text(encoding="utf-8"))
        if stored != fixture:
            raise SystemExit(f"fixture mismatch: {OUTPUT_PATH}")
        print(f"OK: native q-adic wavelet fixture matches {OUTPUT_PATH}")
        return 0
    print(
        json.dumps(
            fixture, allow_nan=False, ensure_ascii=False, indent=2, sort_keys=True
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
