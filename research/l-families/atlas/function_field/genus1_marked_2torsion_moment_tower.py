#!/usr/bin/env python3
"""Bounded exact marked-two-torsion moment tower over odd finite fields.

For a monic squarefree cubic h, let m1(h) be its number of rational roots
and let a_h be the Frobenius trace of y^2=h(x).  This producer records the
all-weight identity

    J_(2n) / (q*(q-1))
      = C_n*q^n*(q-1)
        - sum_(j=1)^n c(n,j)*q^(n-j)*(2+Theta_(2j+2, Gamma0(2))(q)).

The symbolic theorem uses two source-locked packets and the standard
Grothendieck--Lefschetz/Eichler--Shimura trace theorem on Y_0(2).  Only after
that theorem and the modular-form expansions have closed does the producer
enumerate the 495 candidate cubics over F_3, F_5, and F_7 as held-out checks.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import time
import unicodedata
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

Poly = dict[tuple[int, int], int]

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SCRIPT_PATH = Path(__file__).resolve()
OUTPUT_PATH = HERE / "genus1_marked_2torsion_moment_tower.json"
NOTE_PATH = HERE / "GENUS1_MARKED_2TORSION_MOMENT_TOWER.md"
TEST_PATH = ROOT / "tests" / "test_genus1_marked_2torsion_moment_tower.py"

GENUS1_JSON_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_NOTE_PATH = HERE / "GENUS1_CUBIC_FAMILY_LAWS.md"
SYM8_JSON_PATH = HERE / "genus2_sym8_marked_trace_average.json"
SYM8_NOTE_PATH = HERE / "GENUS2_SYM8_MARKED_TRACE_AVERAGE.md"

SOURCE_PACKETS: dict[str, dict[str, object]] = {
    "genus1_cubic_family_laws": {
        "commit": "955ea1e25160075fb4b498018319c80f7e4db9d5",
        "json_path": GENUS1_JSON_PATH,
        "json_git_blob": "49cde8d3a1881d0d626e4f288abc53f370a33244",
        "json_lf_sha256": (
            "b9016ae801cff40d15c53d96210b66a7d44fae7d916e827a0526b9dd42017227"
        ),
        "payload_sha256": (
            "183ffb31ae2f5776944e162e59390c40bd7081827b8731246e72e25a882e50df"
        ),
        "note_path": GENUS1_NOTE_PATH,
        "note_git_blob": "c6c9c24d941c25846a2252436e9cd3efd25295fd",
        "note_lf_sha256": (
            "aad40573c6378c919ee6659bcd1c4b89a8981621c61feb0dcde9911d127c6b9f"
        ),
        "role": "all-n SU(2) ballot decomposition and genus-one normalization",
    },
    "genus2_sym8_marked_trace_average": {
        "commit": "dc63f02d0897e10936ef0767a1c8e6f15ac49e06",
        "json_path": SYM8_JSON_PATH,
        "json_git_blob": "1dece87cbec2731f858e3dd38d2ceb0a96959d53",
        "json_lf_sha256": (
            "a92700980ac7fef22f7a36db7b3d4d8bb7aa8d763904677e64bfca3182be0233"
        ),
        "payload_sha256": (
            "423b8c37b69fb56b459beb7ebd9e6b94d12cf658f5819f7ac481e83560f5d0ae"
        ),
        "note_path": SYM8_NOTE_PATH,
        "note_git_blob": "f882ff91ba28421cf20bfe806a28912c9df71f40",
        "note_lf_sha256": (
            "96a31bef0bd1f38764c8fb09edcd4585bffb6eea88e8141bcaac0ca808d01939"
        ),
        "role": "marked-model/Y_0(2) bridge and audited stack trace theorem",
    },
}

HELD_OUT_Q_VALUES = (3, 5, 7)
MAX_EXACT_OPERATIONS = 16_384
MAX_CANDIDATE_CUBICS = sum(q**3 for q in HELD_OUT_Q_VALUES)
MAX_POINT_EVALUATIONS = 3_000
MAX_FOURIER_DEGREE = 9
MAX_SU2_REGRESSION_HALF_DEGREE = 12
MAX_WALL_SECONDS = 5.0


@dataclass
class ResourceGuard:
    exact_operations: int = 0
    candidate_cubics: int = 0
    point_evaluations: int = 0

    def operation(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("operation increment must be nonnegative")
        if self.exact_operations + amount > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")
        self.exact_operations += amount

    def candidate(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("candidate increment must be nonnegative")
        if self.candidate_cubics + amount > MAX_CANDIDATE_CUBICS:
            raise RuntimeError("candidate-cubic cap exceeded")
        self.candidate_cubics += amount

    def point(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("point increment must be nonnegative")
        if self.point_evaluations + amount > MAX_POINT_EVALUATIONS:
            raise RuntimeError("finite-field point-evaluation cap exceeded")
        self.point_evaluations += amount


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
    return path.relative_to(ROOT).as_posix()


def _load_source_packets() -> dict[str, dict[str, object]]:
    sources: dict[str, dict[str, object]] = {}
    for name, lock in SOURCE_PACKETS.items():
        json_path = lock["json_path"]
        note_path = lock["note_path"]
        if not isinstance(json_path, Path) or not isinstance(note_path, Path):
            raise TypeError(f"invalid source paths for {name}")
        if _lf_sha256(json_path) != lock["json_lf_sha256"]:
            raise RuntimeError(f"JSON source lock failed: {name}")
        if _lf_sha256(note_path) != lock["note_lf_sha256"]:
            raise RuntimeError(f"note source lock failed: {name}")
        value = json.loads(json_path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise TypeError(f"source packet is not an object: {name}")
        claimed = value.get("payload_sha256")
        payload = dict(value)
        payload.pop("payload_sha256", None)
        if claimed != lock["payload_sha256"]:
            raise ValueError(f"unexpected source payload: {name}")
        if claimed != _canonical_sha256(payload):
            raise ValueError(f"source payload authentication failed: {name}")
        sources[name] = value
    return sources


def catalan(index: int) -> int:
    if index < 0:
        raise ValueError("Catalan index must be nonnegative")
    return math.comb(2 * index, index) // (index + 1)


def ballot_coefficient(half_degree: int, character_index: int) -> int:
    if not 0 <= character_index <= half_degree:
        raise ValueError("character index must lie in [0,half_degree]")
    lower = half_degree - character_index
    reflected = math.comb(2 * half_degree, lower - 1) if lower else 0
    return math.comb(2 * half_degree, lower) - reflected


def _poly_add(left: Poly, right: Poly, guard: ResourceGuard) -> Poly:
    guard.operation(len(left) + len(right))
    result = dict(left)
    for monomial, coefficient in right.items():
        result[monomial] = result.get(monomial, 0) + coefficient
        if result[monomial] == 0:
            del result[monomial]
    return result


def _poly_shift(
    value: Poly,
    *,
    a_degree: int = 0,
    q_degree: int = 0,
    scale: int = 1,
    guard: ResourceGuard,
) -> Poly:
    if a_degree < 0 or q_degree < 0:
        raise ValueError("polynomial shifts must be nonnegative")
    guard.operation(len(value))
    return {
        (a_exp + a_degree, q_exp + q_degree): scale * coefficient
        for (a_exp, q_exp), coefficient in value.items()
        if scale * coefficient
    }


def symmetric_power_polynomial(index: int, guard: ResourceGuard) -> Poly:
    """Return P_index(a,q) from P_m=a*P_(m-1)-q*P_(m-2)."""

    if index < 0:
        raise ValueError("symmetric-power index must be nonnegative")
    if index == 0:
        return {(0, 0): 1}
    previous_previous: Poly = {(0, 0): 1}
    previous: Poly = {(1, 0): 1}
    for _ in range(2, index + 1):
        current = _poly_add(
            _poly_shift(previous, a_degree=1, guard=guard),
            _poly_shift(
                previous_previous,
                q_degree=1,
                scale=-1,
                guard=guard,
            ),
            guard,
        )
        previous_previous, previous = previous, current
    return previous


def su2_identity_certificate(
    maximum_half_degree: int, guard: ResourceGuard
) -> list[dict[str, object]]:
    """Replay finite exact regressions of the all-n Clebsch--Gordan identity."""

    if not 0 <= maximum_half_degree <= MAX_SU2_REGRESSION_HALF_DEGREE:
        raise ValueError("SU(2) regression degree exceeds its hard cap")
    certificates: list[dict[str, object]] = []
    symmetric_powers = {
        2 * index: symmetric_power_polynomial(2 * index, guard)
        for index in range(maximum_half_degree + 1)
    }
    for half_degree in range(maximum_half_degree + 1):
        reconstructed: Poly = {}
        terms: list[dict[str, int]] = []
        for character_index in range(half_degree + 1):
            coefficient = ballot_coefficient(half_degree, character_index)
            q_power = half_degree - character_index
            reconstructed = _poly_add(
                reconstructed,
                _poly_shift(
                    symmetric_powers[2 * character_index],
                    q_degree=q_power,
                    scale=coefficient,
                    guard=guard,
                ),
                guard,
            )
            terms.append(
                {
                    "character_index": character_index,
                    "coefficient": coefficient,
                    "q_power": q_power,
                }
            )
        target = {(2 * half_degree, 0): 1}
        if reconstructed != target:
            raise ArithmeticError(f"SU(2) identity failed at n={half_degree}")
        certificates.append(
            {
                "half_degree": half_degree,
                "terms": terms,
                "verified_polynomial": f"a^{2 * half_degree}",
            }
        )
    return certificates


def _expanded_tate_polynomial(half_degree: int) -> list[int]:
    coefficients = [0] * (half_degree + 2)
    coefficients[half_degree + 1] += catalan(half_degree)
    coefficients[half_degree] -= catalan(half_degree)
    for character_index in range(1, half_degree + 1):
        coefficients[half_degree - character_index] -= 2 * ballot_coefficient(
            half_degree, character_index
        )
    return coefficients


EXPLICIT_FORMULAS = {
    0: "J_0=q*(q-1)*(q-1)",
    1: "J_2=q*(q-1)*(q^2-q-2)",
    2: "J_4=q*(q-1)*(2*q^3-2*q^2-6*q-2)",
    3: ("J_6=q*(q-1)*(5*q^4-5*q^3-18*q^2-10*q-2-Theta_f(q))"),
    4: ("J_8=q*(q-1)*(14*q^5-14*q^4-56*q^3-40*q^2-14*q-2-7*q*Theta_f(q)-Theta_g(q))"),
    5: (
        "J_10=q*(q-1)*(42*q^6-42*q^5-180*q^4-150*q^3-70*q^2"
        "-18*q-2-35*q^2*Theta_f(q)-9*q*Theta_g(q)-2*Theta_Delta(q))"
    ),
}

EXPECTED_TATE_POLYNOMIALS = {
    0: [-1, 1],
    1: [-2, -1, 1],
    2: [-2, -6, -2, 2],
    3: [-2, -10, -18, -5, 5],
    4: [-2, -14, -40, -56, -14, 14],
    5: [-2, -18, -70, -150, -180, -42, 42],
}


def _explicit_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    aliases = {
        8: "Theta_f(q)",
        10: "Theta_g(q)",
        12: "2*Theta_Delta(q)",
    }
    cusp_dimensions = {4: 0, 6: 0, 8: 1, 10: 1, 12: 2}
    for half_degree in range(6):
        tate_polynomial = _expanded_tate_polynomial(half_degree)
        if tate_polynomial != EXPECTED_TATE_POLYNOMIALS[half_degree]:
            raise ArithmeticError(f"expanded row failed at n={half_degree}")
        channels = []
        for character_index in range(1, half_degree + 1):
            weight = 2 * character_index + 2
            channels.append(
                {
                    "character_index": character_index,
                    "weight": weight,
                    "ballot_coefficient": ballot_coefficient(
                        half_degree, character_index
                    ),
                    "q_power": half_degree - character_index,
                    "full_cusp_space_dimension": cusp_dimensions[weight],
                    "trace": aliases.get(weight, f"Theta_({weight},Gamma0(2))(q)"),
                }
            )
        rows.append(
            {
                "half_degree": half_degree,
                "moment": 2 * half_degree,
                "formula": EXPLICIT_FORMULAS[half_degree],
                "normalized_tate_polynomial_low_to_high": tate_polynomial,
                "character_channels": channels,
            }
        )
    return rows


def _build_symbolic_theorem(
    sources: Mapping[str, Mapping[str, object]], guard: ResourceGuard
) -> dict[str, object]:
    genus1 = sources["genus1_cubic_family_laws"]
    sym8 = sources["genus2_sym8_marked_trace_average"]
    genus1_theorem = genus1.get("all_q_moment_theorem")
    sym8_bridge = sym8.get("marked_cubic_sixth_moment")
    if not isinstance(genus1_theorem, dict) or not isinstance(sym8_bridge, dict):
        raise TypeError("source theorem blocks are missing")
    if "c_(n,j)=binom(2n,n-j)-binom(2n,n-j-1)" not in str(
        genus1_theorem.get("raw_even_moment")
    ):
        raise ValueError("source SU(2) ballot formula changed")
    if sym8_bridge.get("model_stack_bridge") != (
        "J_6=q*(q-1)*sum_[(E,T)]a_E^6/|Aut_q(E,T)|, T in E[2](F_q)-{0}"
    ):
        raise ValueError("source marked-stack bridge changed")
    trace_rows = sym8_bridge.get("Y0(2)_character_traces")
    if not isinstance(trace_rows, dict) or trace_rows.get("P_6") != (
        "-Theta_(8,2)(q)-2"
    ):
        raise ValueError("source Y_0(2) trace normalization changed")

    su2_regressions = su2_identity_certificate(MAX_SU2_REGRESSION_HALF_DEGREE, guard)
    rows = _explicit_rows()
    guard.operation(sum(len(row["character_channels"]) for row in rows))
    return {
        "scope": "every odd prime power q and every integer n>=0",
        "definition": ("J_(2n)(q)=sum_(h monic squarefree cubic) m1(h)*a_h^(2n)"),
        "ballot_coefficient": ("c(n,j)=binom(2n,n-j)-binom(2n,n-j-1)"),
        "theorem": (
            "J_(2n)/(q*(q-1))=C_n*q^n*(q-1)"
            "-sum_(j=1)^n c(n,j)*q^(n-j)"
            "*(2+Theta_(2j+2,Gamma0(2))(q))"
        ),
        "trace_convention": (
            "Theta_(k,Gamma0(2))(p^r) is the full cuspidal Frobenius-power "
            "trace, summed over underlying normalized newforms with oldform "
            "multiplicity; it is not generally a single Fourier coefficient"
        ),
        "proof_chain": [
            "orbit-stabilizer identifies root-marked cubics with Y_1(2)=Y_0(2) and contributes q*(q-1)",
            "Clebsch--Gordan/reflection gives the all-n SU(2) ballot decomposition of a^(2n)",
            "the P_0 stack trace is q-1",
            "for every positive even m the Y_0(2) stack trace is -2-Theta_(m+2,Gamma0(2))(q)",
            "substitution proves the displayed identity without interpolation",
        ],
        "all_n_proof_mode": (
            "Clebsch--Gordan induction plus the reflection-principle ballot "
            "multiplicity; finite symbolic rows are regression certificates"
        ),
        "su2_exact_regressions": su2_regressions,
        "explicit_rows_through_n_5": rows,
    }


def _multiply_factor(
    coefficients: list[int], degree: int, multiplicity: int, guard: ResourceGuard
) -> None:
    maximum = len(coefficients) - 1
    if degree <= 0 or multiplicity < 0:
        raise ValueError("invalid truncated-product factor")
    for _ in range(multiplicity):
        for index in range(maximum, degree - 1, -1):
            coefficients[index] -= coefficients[index - degree]
            guard.operation()


def eta_level2_coefficients(maximum: int, guard: ResourceGuard) -> list[int]:
    """Coefficients of eta(z)^8 eta(2z)^8 through Q^maximum."""

    if not 1 <= maximum <= MAX_FOURIER_DEGREE:
        raise ValueError("level-two eta-product degree exceeds its hard cap")
    coefficients = [0] * (maximum + 1)
    coefficients[1] = 1
    for degree in range(1, maximum + 1):
        _multiply_factor(coefficients, degree, 8, guard)
        if 2 * degree <= maximum:
            _multiply_factor(coefficients, 2 * degree, 8, guard)
    return coefficients


def delta_coefficients(maximum: int, guard: ResourceGuard) -> list[int]:
    """Coefficients of Delta=eta(z)^24 through Q^maximum."""

    if not 1 <= maximum <= MAX_FOURIER_DEGREE:
        raise ValueError("Delta expansion degree exceeds its hard cap")
    coefficients = [0] * (maximum + 1)
    coefficients[1] = 1
    for degree in range(1, maximum + 1):
        _multiply_factor(coefficients, degree, 24, guard)
    return coefficients


def level2_weight2_coefficients(maximum: int, guard: ResourceGuard) -> list[int]:
    """Coefficients of 2E_2(2z)-E_2(z)."""

    if not 0 <= maximum <= MAX_FOURIER_DEGREE:
        raise ValueError("weight-two expansion degree exceeds its hard cap")
    sigma_one = [0] * (maximum + 1)
    for divisor in range(1, maximum + 1):
        for multiple in range(divisor, maximum + 1, divisor):
            sigma_one[multiple] += divisor
            guard.operation()
    coefficients = [0] * (maximum + 1)
    coefficients[0] = 1
    for degree in range(1, maximum + 1):
        coefficients[degree] = 24 * sigma_one[degree]
        if degree % 2 == 0:
            coefficients[degree] -= 48 * sigma_one[degree // 2]
        guard.operation()
    return coefficients


def _convolve(
    left: list[int], right: list[int], maximum: int, guard: ResourceGuard
) -> list[int]:
    if maximum < 0 or maximum >= len(left) or maximum >= len(right):
        raise ValueError("invalid convolution truncation")
    result = [0] * (maximum + 1)
    for left_index in range(maximum + 1):
        for right_index in range(maximum + 1 - left_index):
            result[left_index + right_index] += left[left_index] * right[right_index]
            guard.operation()
    return result


def prime_power_trace(coefficients: list[int], weight: int, q: int) -> int:
    """Return a_(p^r)-p^(k-1)*a_(p^(r-2)) for a normalized eigenform."""

    characteristic, exponent = prime_power_data(q)
    if q >= len(coefficients):
        raise ValueError("Fourier expansion is too short for this q")
    previous_index = characteristic ** (exponent - 2) if exponent >= 2 else 0
    previous = coefficients[previous_index] if previous_index else 0
    return coefficients[q] - characteristic ** (weight - 1) * previous


def prime_power_data(q: int) -> tuple[int, int]:
    if q < 3:
        raise ValueError("q must be an odd prime power")
    for candidate in range(2, math.isqrt(q) + 1):
        if q % candidate:
            continue
        if any(
            candidate % divisor == 0 for divisor in range(2, math.isqrt(candidate) + 1)
        ):
            continue
        residual = q
        exponent = 0
        while residual % candidate == 0:
            residual //= candidate
            exponent += 1
        if residual != 1:
            raise ValueError("q must be a prime power")
        if candidate == 2:
            raise ValueError("q must be odd")
        return candidate, exponent
    if q % 2 == 0:
        raise ValueError("q must be odd")
    return q, 1


def _build_modular_form_certificate(guard: ResourceGuard) -> dict[str, object]:
    f_coefficients = eta_level2_coefficients(MAX_FOURIER_DEGREE, guard)
    weight2_coefficients = level2_weight2_coefficients(MAX_FOURIER_DEGREE, guard)
    g_coefficients = _convolve(
        f_coefficients, weight2_coefficients, MAX_FOURIER_DEGREE, guard
    )
    delta_values = delta_coefficients(MAX_FOURIER_DEGREE, guard)
    expected_f = [0, 1, -8, 12, 64, -210, -96, 1016, -512, -2043]
    expected_g = [0, 1, 16, -156, 256, 870, -2496, -952, 4096, 4653]
    if f_coefficients != expected_f:
        raise ArithmeticError("weight-eight eta-product expansion failed")
    if g_coefficients != expected_g:
        raise ArithmeticError("weight-ten product expansion failed")
    expected_delta = [0, 1, -24, 252, -1472, 4830, -6048, -16744, 84480, -113643]
    if delta_values != expected_delta:
        raise ArithmeticError("Delta expansion failed")

    theta_f_9 = prime_power_trace(f_coefficients, 8, 9)
    theta_g_9 = prime_power_trace(g_coefficients, 10, 9)
    theta_delta_9 = prime_power_trace(delta_values, 12, 9)
    if (theta_f_9, theta_g_9, theta_delta_9) != (-4230, -15030, -290790):
        raise ArithmeticError("q=9 prime-power trace convention failed")

    return {
        "spaces_through_weight_12": [
            {
                "weight": 4,
                "full_cusp_dimension": 0,
                "old_dimension": 0,
                "new_dimension": 0,
                "trace": "0",
            },
            {
                "weight": 6,
                "full_cusp_dimension": 0,
                "old_dimension": 0,
                "new_dimension": 0,
                "trace": "0",
            },
            {
                "weight": 8,
                "full_cusp_dimension": 1,
                "old_dimension": 0,
                "new_dimension": 1,
                "basis": "f=eta(z)^8*eta(2z)^8",
                "trace": "Theta_f(q)",
            },
            {
                "weight": 10,
                "full_cusp_dimension": 1,
                "old_dimension": 0,
                "new_dimension": 1,
                "basis": ("g=f*(2*E_2(2z)-E_2(z))"),
                "trace": "Theta_g(q)",
            },
            {
                "weight": 12,
                "full_cusp_dimension": 2,
                "old_dimension": 2,
                "new_dimension": 0,
                "basis": "Delta(z), Delta(2z)",
                "trace": "2*Theta_Delta(q)",
            },
        ],
        "dimension_argument": (
            "multiplication by f identifies M_k(Gamma0(2)) with "
            "S_(k+8)(Gamma0(2)); dimensions through 12 are 1,1,2, and "
            "the two independent Delta degeneracy maps exhaust weight 12"
        ),
        "f_coefficients_c_0_through_c_9": f_coefficients,
        "weight2_coefficients_h_0_through_h_9": weight2_coefficients,
        "g_coefficients_d_0_through_d_9": g_coefficients,
        "delta_coefficients_tau_0_through_tau_9": delta_values,
        "required_g_coefficients": {
            "g_3": g_coefficients[3],
            "g_5": g_coefficients[5],
            "g_7": g_coefficients[7],
            "g_9": g_coefficients[9],
        },
        "q_9_prime_power_traces": {
            "Theta_f(9)": theta_f_9,
            "Theta_g(9)": theta_g_9,
            "Theta_Delta(9)": theta_delta_9,
            "Theta_(12,Gamma0(2))(9)": 2 * theta_delta_9,
            "Theta_g_identity": "4653-3^9=-15030",
        },
    }


def evaluate_normalized_marked_moment(
    half_degree: int,
    q: int,
    full_cusp_traces: Mapping[int, int],
) -> int:
    if half_degree < 0:
        raise ValueError("half degree must be nonnegative")
    result = catalan(half_degree) * q**half_degree * (q - 1)
    for character_index in range(1, half_degree + 1):
        weight = 2 * character_index + 2
        theta = int(full_cusp_traces.get(weight, 0))
        result -= (
            ballot_coefficient(half_degree, character_index)
            * q ** (half_degree - character_index)
            * (2 + theta)
        )
    return result


def _cubic_discriminant(a_value: int, b_value: int, c_value: int, q: int) -> int:
    return (
        a_value * a_value * b_value * b_value
        - 4 * b_value**3
        - 4 * a_value**3 * c_value
        - 27 * c_value * c_value
        + 18 * a_value * b_value * c_value
    ) % q


def _quadratic_character(value: int, q: int) -> int:
    residue = value % q
    if residue == 0:
        return 0
    return 1 if pow(residue, (q - 1) // 2, q) == 1 else -1


def _enumerate_held_out(
    q_values: tuple[int, ...],
    modular_forms: Mapping[str, object],
    guard: ResourceGuard,
) -> list[dict[str, object]]:
    if not q_values or len(set(q_values)) != len(q_values):
        raise ValueError("held-out q values must be nonempty and distinct")
    if any(prime_power_data(q) != (q, 1) for q in q_values):
        raise ValueError("held-out census supports prime fields only")
    requested_candidates = sum(q**3 for q in q_values)
    requested_point_evaluations = sum(q**3 * (q - 1) for q in q_values)
    if requested_candidates > MAX_CANDIDATE_CUBICS:
        raise ValueError("requested held-out census exceeds candidate cap")
    if requested_point_evaluations > MAX_POINT_EVALUATIONS:
        raise ValueError("requested held-out census exceeds point-evaluation cap")
    if guard.candidate_cubics + requested_candidates > MAX_CANDIDATE_CUBICS:
        raise ValueError("cumulative held-out census exceeds candidate cap")
    if guard.point_evaluations + requested_point_evaluations > MAX_POINT_EVALUATIONS:
        raise ValueError("cumulative held-out census exceeds point-evaluation cap")
    f_coefficients = modular_forms["f_coefficients_c_0_through_c_9"]
    g_coefficients = modular_forms["g_coefficients_d_0_through_d_9"]
    delta_values = modular_forms["delta_coefficients_tau_0_through_tau_9"]
    if not all(
        isinstance(value, list)
        for value in (f_coefficients, g_coefficients, delta_values)
    ):
        raise TypeError("modular coefficient blocks are invalid")

    rows: list[dict[str, object]] = []
    for q in q_values:
        j8 = 0
        j10 = 0
        squarefree = 0
        for a_value, b_value, c_value in itertools.product(range(q), repeat=3):
            guard.candidate()
            if _cubic_discriminant(a_value, b_value, c_value, q) == 0:
                continue
            squarefree += 1
            root_count = 0
            character_sum = 0
            for x_value in range(q):
                guard.point()
                polynomial_value = (
                    x_value**3
                    + a_value * x_value * x_value
                    + b_value * x_value
                    + c_value
                ) % q
                root_count += int(polynomial_value == 0)
                character_sum += _quadratic_character(polynomial_value, q)
            trace = -character_sum
            j8 += root_count * trace**8
            j10 += root_count * trace**10
        if squarefree != q * q * (q - 1):
            raise ArithmeticError("squarefree cubic count failed")
        traces = {
            8: int(f_coefficients[q]),
            10: int(g_coefficients[q]),
            12: 2 * int(delta_values[q]),
        }
        predicted_j8 = q * (q - 1) * evaluate_normalized_marked_moment(4, q, traces)
        predicted_j10 = q * (q - 1) * evaluate_normalized_marked_moment(5, q, traces)
        rows.append(
            {
                "q": q,
                "candidate_cubics": q**3,
                "squarefree_cubics": squarefree,
                "observed_J_8": j8,
                "theorem_J_8": predicted_j8,
                "J_8_difference": j8 - predicted_j8,
                "observed_J_10": j10,
                "theorem_J_10": predicted_j10,
                "J_10_difference": j10 - predicted_j10,
                "status": "HELD_OUT_FINITE_REGRESSION_NOT_THEOREM_INPUT",
            }
        )
    return rows


def _source_manifest() -> list[dict[str, object]]:
    manifest = []
    for name, lock in SOURCE_PACKETS.items():
        json_path = lock["json_path"]
        note_path = lock["note_path"]
        if not isinstance(json_path, Path) or not isinstance(note_path, Path):
            raise TypeError("invalid source manifest paths")
        manifest.append(
            {
                "id": name,
                "commit": lock["commit"],
                "role": lock["role"],
                "json_path": _relative(json_path),
                "json_git_blob": lock["json_git_blob"],
                "json_sha256_lf_normalized": lock["json_lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "note_path": _relative(note_path),
                "note_git_blob": lock["note_git_blob"],
                "note_sha256_lf_normalized": lock["note_lf_sha256"],
            }
        )
    return manifest


def _packet_manifest() -> list[dict[str, str]]:
    return [
        {
            "path": _relative(path),
            "sha256_lf_normalized": _lf_sha256(path),
        }
        for path in (NOTE_PATH, SCRIPT_PATH, TEST_PATH)
    ]


def build_fixture() -> dict[str, object]:
    start = time.monotonic()
    guard = ResourceGuard()
    sources = _load_source_packets()
    symbolic = _build_symbolic_theorem(sources, guard)
    operations_after_symbolic = guard.exact_operations
    modular_forms = _build_modular_form_certificate(guard)
    operations_before_controls = guard.exact_operations

    theta_9 = modular_forms["q_9_prime_power_traces"]
    if not isinstance(theta_9, dict):
        raise TypeError("q=9 trace block is invalid")
    full_traces_9 = {
        8: int(theta_9["Theta_f(9)"]),
        10: int(theta_9["Theta_g(9)"]),
        12: int(theta_9["Theta_(12,Gamma0(2))(9)"]),
    }
    normalized_j8_9 = evaluate_normalized_marked_moment(4, 9, full_traces_9)
    normalized_j10_9 = evaluate_normalized_marked_moment(5, 9, full_traces_9)
    q9_consequence = {
        "q": 9,
        "J_8_over_q_q_minus_1": normalized_j8_9,
        "J_8": 9 * 8 * normalized_j8_9,
        "J_10_over_q_q_minus_1": normalized_j10_9,
        "J_10": 9 * 8 * normalized_j10_9,
        "status": "THEOREM_CONSEQUENCE_NOT_FIELD_ENUMERATION",
    }
    if q9_consequence["J_8"] != 69_995_520:
        raise ArithmeticError("q=9 J_8 consequence failed")

    controls = _enumerate_held_out(HELD_OUT_Q_VALUES, modular_forms, guard)
    if any(row["J_8_difference"] or row["J_10_difference"] for row in controls):
        raise ArithmeticError("held-out finite regression failed")

    sym8 = sources["genus2_sym8_marked_trace_average"]
    primary_sources = sym8.get("primary_source_ledger")
    if not isinstance(primary_sources, list):
        raise TypeError("audited primary-source ledger is missing")

    fixture: dict[str, object] = {
        "schema": "riemann.genus1_marked_2torsion_moment_tower.v1",
        "status": "PROVED_ALL_ODD_PRIME_POWERS",
        "theorem": symbolic,
        "modular_form_certificate": modular_forms,
        "q_9_consequences": q9_consequence,
        "held_out_finite_regressions": controls,
        "source_manifest": _source_manifest(),
        "packet_manifest": _packet_manifest(),
        "primary_source_ledger": primary_sources,
        "resource_contract": {
            "arithmetic": "exact integers and finite polynomial recurrences",
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "actual_operations_after_symbolic_theorem": operations_after_symbolic,
            "actual_operations_before_controls": operations_before_controls,
            "maximum_candidate_cubics": MAX_CANDIDATE_CUBICS,
            "actual_candidate_cubics": guard.candidate_cubics,
            "maximum_point_evaluations": MAX_POINT_EVALUATIONS,
            "actual_point_evaluations": guard.point_evaluations,
            "maximum_fourier_degree": MAX_FOURIER_DEGREE,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "enumerated_fields": list(HELD_OUT_Q_VALUES),
            "q_9_field_enumerated": False,
        },
        "firewalls": [
            "Theta_(k,Gamma0(2)) is the full cusp-space trace with old/new multiplicity, not automatically one newform coefficient.",
            "The q=3,5,7 enumerations occur only after the symbolic theorem and form expansions close; they are not proof inputs.",
            "The q=9 rows use Frobenius-power traces and no F_9 enumeration.",
            "No novelty claim is made for the modular trace or moment formulas.",
            "This family theorem makes no RH, GRH, memberwise sign, motive, compatible-system, or global Euler-product claim.",
        ],
    }
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    if time.monotonic() - start > MAX_WALL_SECONDS:
        raise RuntimeError("wall-time cap exceeded")
    return fixture


def _serialized(fixture: Mapping[str, object]) -> str:
    return (
        json.dumps(
            fixture,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    arguments = parser.parse_args()
    fixture = build_fixture()
    rendered = _serialized(fixture)
    if arguments.check:
        if not arguments.output.exists():
            raise SystemExit(f"missing fixture: {arguments.output}")
        if arguments.output.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"stale fixture: {arguments.output}")
        print(f"verified {arguments.output}")
        return 0
    arguments.output.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {arguments.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
