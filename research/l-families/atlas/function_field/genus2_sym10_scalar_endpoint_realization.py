#!/usr/bin/env python3
"""Build an exact scalar-endpoint realization packet for genus-two Sym10."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
import unicodedata
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "genus2_sym10_scalar_endpoint_realization.json"
NOTE_PATH = HERE / "GENUS2_SYM10_SCALAR_ENDPOINT_REALIZATION.md"
TEST_PATH = ROOT / "tests" / "test_genus2_sym10_scalar_endpoint_realization.py"

MARKED_STACK_PATH = HERE / "genus2_marked_weierstrass_stack_adapter.json"
RARE_EVENT_PATH = HERE / "genus2_sym10_rare_event_tomography.json"

SOURCE_LOCKS: dict[str, dict[str, object]] = {
    "marked_stack_adapter": {
        "path": MARKED_STACK_PATH,
        "schema": "riemann.function_field.genus2_marked_weierstrass_stack_adapter.v1",
        "lf_sha256": "fe8f23f6379a70ea150a8e4f1b87054553536fde3bd23e6c1d21e252baf3b26c",
        "payload_sha256": "7b091cc158c7ff378774dcbaef5802c469c3d377384034bced1caf4fe92b3601",
        "audited_commit": "c8eff406f49daf9f09c0bb3e63e21659275d224e",
    },
    "rare_event_certificate": {
        "path": RARE_EVENT_PATH,
        "schema": "riemann.function_field.genus2_sym10_rare_event_tomography.v1",
        "lf_sha256": "7156cda07b0afa551f7c34054308c1c8b55dfb94af909c8fb753efa097ad6098",
        "payload_sha256": "6d28e9ac614d2c61744c7e224522f6e44e495aed239a112e658659fcec3186fb",
        "audited_commit": "0f0baf7529ec0ac756d50f252515d48814b98ed8",
    },
}

MAX_SOURCE_BYTES = 64_000
MAX_SOURCE_RECORDS = 2
MAX_EXACT_OPERATIONS = 4_096
MAX_WALL_SECONDS = 2.0

Polynomial: TypeAlias = tuple[int, ...]  # increasing powers


@dataclass
class ResourceGuard:
    source_bytes: int = 0
    source_records: int = 0
    exact_operations: int = 0

    def bytes(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("source-byte increment must be nonnegative")
        self.source_bytes += amount
        if self.source_bytes > MAX_SOURCE_BYTES:
            raise RuntimeError("source-byte cap exceeded")

    def records(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("source-record increment must be nonnegative")
        self.source_records += amount
        if self.source_records > MAX_SOURCE_RECORDS:
            raise RuntimeError("source-record cap exceeded")

    def operations(self, amount: int = 1) -> None:
        if amount < 0:
            raise ValueError("exact-operation increment must be nonnegative")
        self.exact_operations += amount
        if self.exact_operations > MAX_EXACT_OPERATIONS:
            raise RuntimeError("exact-operation cap exceeded")


@dataclass(frozen=True)
class KMonomial:
    """Represent (-1)^(parity*k) * 3^(three_exponent*k)."""

    parity: int
    three_exponent: int

    def __post_init__(self) -> None:
        object.__setattr__(self, "parity", self.parity % 2)

    def powered(self, exponent: int, guard: ResourceGuard) -> KMonomial:
        if exponent < 0:
            raise ValueError("K-monomial power must be nonnegative")
        guard.operations()
        return KMonomial(self.parity * exponent, self.three_exponent * exponent)

    def divided_by(self, other: KMonomial, guard: ResourceGuard) -> KMonomial:
        guard.operations()
        return KMonomial(
            self.parity - other.parity,
            self.three_exponent - other.three_exponent,
        )

    def json(self) -> dict[str, int | str]:
        return {
            "meaning": "(-1)^(parity*k)*3^(three_exponent*k)",
            "parity": self.parity,
            "three_exponent": self.three_exponent,
        }


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(data: bytes) -> str:
    normalized = unicodedata.normalize(
        "NFC", data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    )
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _trim_mod(value: list[int] | Polynomial, modulus: int) -> Polynomial:
    reduced = [coefficient % modulus for coefficient in value]
    while len(reduced) > 1 and reduced[-1] == 0:
        reduced.pop()
    return tuple(reduced)


def _derivative_mod(
    value: Polynomial, modulus: int, guard: ResourceGuard
) -> Polynomial:
    guard.operations(max(1, len(value) - 1))
    if len(value) <= 1:
        return (0,)
    return _trim_mod(
        [degree * value[degree] for degree in range(1, len(value))], modulus
    )


def _divmod_mod(
    dividend: Polynomial,
    divisor: Polynomial,
    modulus: int,
    guard: ResourceGuard,
) -> tuple[Polynomial, Polynomial]:
    divisor = _trim_mod(divisor, modulus)
    if divisor == (0,):
        raise ZeroDivisionError("zero polynomial divisor")
    remainder = list(_trim_mod(dividend, modulus))
    quotient = [0] * max(1, len(remainder) - len(divisor) + 1)
    inverse_lead = pow(divisor[-1], -1, modulus)
    guard.operations()
    while len(remainder) >= len(divisor) and tuple(remainder) != (0,):
        shift = len(remainder) - len(divisor)
        factor = remainder[-1] * inverse_lead % modulus
        quotient[shift] = factor
        guard.operations()
        for index, coefficient in enumerate(divisor):
            remainder[index + shift] = (
                remainder[index + shift] - factor * coefficient
            ) % modulus
            guard.operations()
        remainder = list(_trim_mod(remainder, modulus))
    return _trim_mod(quotient, modulus), _trim_mod(remainder, modulus)


def _gcd_mod(
    left: Polynomial, right: Polynomial, modulus: int, guard: ResourceGuard
) -> Polynomial:
    left = _trim_mod(left, modulus)
    right = _trim_mod(right, modulus)
    while right != (0,):
        _, remainder = _divmod_mod(left, right, modulus, guard)
        left, right = right, remainder
    inverse_lead = pow(left[-1], -1, modulus)
    guard.operations(len(left) + 1)
    return _trim_mod([inverse_lead * coefficient for coefficient in left], modulus)


def _derive_seed_certificate(guard: ResourceGuard) -> dict[str, object]:
    modulus = 3
    polynomial: Polynomial = (1, 0, 0, 0, 0, 1)  # 1+T^5
    derivative = _derivative_mod(polynomial, modulus, guard)
    gcd = _gcd_mod(polynomial, derivative, modulus, guard)
    if derivative != (0, 0, 0, 0, 2) or gcd != (1,):
        raise ArithmeticError("the seed quintic squarefreeness certificate failed")

    point_rows: list[dict[str, object]] = []
    for extension_degree in (1, 2):
        field_order = 3**extension_degree
        multiplicative_order = field_order - 1
        coprimality = math.gcd(5, multiplicative_order)
        guard.operations(4)
        if coprimality != 1:
            raise ArithmeticError("fifth-power map lost bijectivity")
        point_rows.append(
            {
                "extension_degree": extension_degree,
                "field_order": field_order,
                "multiplicative_group_order": multiplicative_order,
                "gcd_5_group_order": coprimality,
                "fifth_power_map": "bijection on the field",
                "quadratic_character_sum": 0,
                "affine_point_count": field_order,
                "projective_point_count": field_order + 1,
            }
        )

    n1 = int(point_rows[0]["projective_point_count"])
    n2 = int(point_rows[1]["projective_point_count"])
    power_sum_1 = 3 + 1 - n1
    power_sum_2 = 3**2 + 1 - n2
    second_coefficient = Fraction(power_sum_1**2 - power_sum_2, 2)
    guard.operations(8)
    if power_sum_1 != 0 or power_sum_2 != 0 or second_coefficient != 0:
        raise ArithmeticError("Newton reconstruction of the seed factor failed")

    local_factor = [1, -power_sum_1, int(second_coefficient), -3 * power_sum_1, 9]
    characteristic_polynomial = list(reversed(local_factor))
    if local_factor != [1, 0, 0, 0, 9]:
        raise ArithmeticError("seed local factor drifted")
    if characteristic_polynomial != [9, 0, 0, 0, 1]:
        raise ArithmeticError("seed characteristic polynomial drifted")

    return {
        "curve": "C: y^2=T^5+1 over F_3, with the point at infinity",
        "squarefree_quintic": {
            "D_coefficients_increasing_T": list(polynomial),
            "derivative_mod_3": list(derivative),
            "monic_gcd_with_derivative_mod_3": list(gcd),
            "reason": "D'=2*T^4 and D mod T^4=1",
        },
        "point_counts_without_field_sweep": {
            "rows": point_rows,
            "proof": (
                "gcd(5,3^n-1)=1 for n=1,2, so x->x^5 is a field "
                "bijection; translating its image makes sum_x chi(x^5+1)="
                "sum_u chi(u)=0"
            ),
            "N_1": n1,
            "N_2": n2,
        },
        "newton_reconstruction": {
            "power_sum_1": power_sum_1,
            "power_sum_2": power_sum_2,
            "second_elementary_coefficient": [
                second_coefficient.numerator,
                second_coefficient.denominator,
            ],
            "local_factor_coefficients_increasing_T": local_factor,
            "local_factor": "P_3(T)=1+9*T^4",
            "frobenius_characteristic_polynomial_coefficients_increasing_X": (
                characteristic_polynomial
            ),
            "frobenius_characteristic_polynomial": "X^4+9",
        },
    }


def _derive_base_change_certificate(guard: ResourceGuard) -> dict[str, object]:
    lambda_k = KMonomial(1, 2)
    q_k = KMonomial(0, 4)
    sqrt_q_k = KMonomial(0, 2)
    normalized_scalar = lambda_k.divided_by(sqrt_q_k, guard)
    if lambda_k.powered(2, guard) != q_k:
        raise ArithmeticError("base-change scalar no longer squares to q")
    if lambda_k.powered(10, guard) != q_k.powered(5, guard):
        raise ArithmeticError("Sym10 endpoint normalization drifted")

    dimension = math.comb(13, 3)
    guard.operations(6)
    if dimension != 286:
        raise ArithmeticError("Sym10 dimension drifted")

    q_small = 3**4
    lambda_small = -9
    a_small = -4 * lambda_small
    b_small = 6 * q_small
    point_count_small = q_small + 1 + a_small
    twist_a_small = -a_small
    twist_point_count_small = q_small + 1 + twist_a_small
    r10_small = dimension * q_small**5
    guard.operations(12)

    return {
        "tower": "q=3^(4*k), k>=1",
        "seed_root_relation": "every seed Frobenius root alpha satisfies alpha^4=-9",
        "base_change_relation": "alpha^(4*k)=(-9)^k for all four roots",
        "q_as_K_monomial": q_k.json(),
        "sqrt_q_as_K_monomial": sqrt_q_k.json(),
        "lambda_k=(-9)^k_as_K_monomial": lambda_k.json(),
        "lambda_k_squared_equals_q": True,
        "lambda_k_tenth_equals_q_fifth": True,
        "normalized_scalar_as_K_monomial": normalized_scalar.json(),
        "normalized_frobenius": "U=(-1)^k*I_4",
        "local_factor": "P_q(T)=(1-(-9)^k*T)^4",
        "coefficient_row": {
            "a": "-4*(-9)^k",
            "b": "6*q",
            "point_count": "q+1-4*(-9)^k=q+1+a",
        },
        "quadratic_twist_row": {
            "normalized_frobenius": "U=(-1)^(k+1)*I_4",
            "local_factor": "P_q_twist(T)=(1+(-9)^k*T)^4",
            "a": "4*(-9)^k",
            "b": "6*q",
            "point_count": "q+1+4*(-9)^k=q+1+a_twist",
        },
        "sym10": {
            "dimension": dimension,
            "reciprocal_coefficient": "r_D(10)=286*q^5",
            "normalized_character": "chi_(10,0)(U)=286",
        },
        "smallest_tower_specialization_not_a_field_sweep": {
            "k": 1,
            "q": q_small,
            "lambda": lambda_small,
            "U": "-I_4",
            "a": a_small,
            "b": b_small,
            "point_count": point_count_small,
            "r_D_10": r10_small,
            "quadratic_twist": {
                "U": "I_4",
                "a": twist_a_small,
                "b": b_small,
                "point_count": twist_point_count_small,
                "r_D_10": r10_small,
            },
        },
    }


def _derive_orbit_certificate(guard: ResourceGuard) -> dict[str, object]:
    binomial_mod_3 = [math.comb(5, degree) % 3 for degree in range(6)]
    guard.operations(len(binomial_mod_3) + 12)
    if binomial_mod_3 != [1, 2, 1, 1, 2, 1]:
        raise ArithmeticError("characteristic-three affine expansion drifted")
    if pow(81, 1, 10) != 1:
        raise ArithmeticError("tower congruence q=1 mod 10 drifted")

    q_small = 81
    square_group_small = q_small * (q_small - 1) // 2
    full_group_small = q_small * (q_small - 1)
    square_orbit_small = square_group_small // 5
    full_orbit_small = full_group_small // 5
    family_small = q_small**4 * (q_small - 1)
    if square_orbit_small != 648 or full_orbit_small != 1296:
        raise ArithmeticError("smallest tower orbit specialization drifted")
    if Fraction(square_orbit_small, family_small) != Fraction(1, 10 * q_small**3):
        raise ArithmeticError("single-sign density cancellation drifted")
    if Fraction(full_orbit_small, family_small) != Fraction(1, 5 * q_small**3):
        raise ArithmeticError("combined density cancellation drifted")

    return {
        "full_affine_action": "D(T)|(alpha,beta)=alpha^(-5)*D(alpha*T+beta)",
        "characteristic_three_expansion": {
            "binomial_coefficients_mod_3_in_increasing_T_power": binomial_mod_3,
            "T4_coefficient_after_monic_rescaling": "2*beta/alpha",
            "constant_after_beta_zero": "alpha^(-5)",
        },
        "stabilizer": {
            "translation_condition": "beta=0",
            "scaling_condition": "alpha^5=1",
            "group": "mu_5",
            "order": 5,
            "all_elements_are_squares": (
                "q=81^k is 1 mod 10; if g generates F_q^x, mu_5 is generated "
                "by g^((q-1)/5), whose exponent is even"
            ),
        },
        "orbit_decomposition": {
            "full_affine_group_order": "q*(q-1)",
            "square_affine_group_order": "q*(q-1)/2",
            "full_orbit_size": "q*(q-1)/5",
            "square_affine_orbit_size": "q*(q-1)/10",
            "number_of_square_affine_orbits_in_full_orbit": 2,
            "signs": (
                "the square orbit of the seed has U=(-1)^k*I; its nonsquare "
                "affine coset is the quadratic twist and has U=(-1)^(k+1)*I"
            ),
        },
        "nonsquare_twist_sign_derivation": {
            "setup": "alpha is nonsquare, r^2=alpha in F_(q^2), and r^q=-r",
            "coordinate_map": (
                "C_(D|(alpha,beta)) -> C_D: (T,Y) maps to (alpha*T+beta,r^5*Y)"
            ),
            "equation_check": (
                "D(alpha*T+beta)=alpha^5*(D|(alpha,beta))(T)=r^10*(D|(alpha,beta))(T)"
            ),
            "descent_cocycle": (
                "q-Frobenius sends r^5 to -r^5, so the conjugate map differs "
                "by the hyperelliptic involution"
            ),
            "conclusion": (
                "the nonsquare coset is the nontrivial quadratic twist and "
                "negates all Frobenius eigenvalues, hence U maps to -U"
            ),
        },
        "family_and_density": {
            "family_size": "|H5(q)|=q^4*(q-1)",
            "constructed_members_each_endpoint_sign": "q*(q-1)/10",
            "constructed_members_both_endpoint_signs": "q*(q-1)/5",
            "constructed_density_each_endpoint_sign": "1/(10*q^3)",
            "constructed_density_both_endpoint_signs": "1/(5*q^3)",
            "lower_bound_each_endpoint_sign": "at least 1/(10*q^3)",
            "lower_bound_both_endpoint_signs": "at least 1/(5*q^3)",
        },
        "normalized_moment_contribution": {
            "definition": "M_m=|H5(q)|^(-1)*sum_D (r_D(10)/q^5)^m",
            "integer_m": "m>=1",
            "exact_contribution_from_constructed_two_orbit_union": ("286^m/(5*q^3)"),
            "absolute_moment_lower_bound": "E[|chi_(10,0)|^m]>=286^m/(5*q^3)",
            "even_moment_lower_bound": "E[chi_(10,0)^(2*j)]>=286^(2*j)/(5*q^3)",
            "odd_moment_firewall": (
                "the subset contribution is exact, but other members can cancel it "
                "in the full signed odd moment"
            ),
        },
        "log_order_boundary_layer": {
            "fixed_m": "286^m/(5*q^3) tends to 0 as q tends to infinity",
            "logarithmic_order": "m_q=floor(3*log(q)/log(286))",
            "exact_bounds_at_m_q": "1/(5*286)<=286^m_q/(5*q^3)<=1/5",
            "warning": (
                "the exact endpoint contribution vanishes at every fixed moment "
                "order but remains order one when moment order grows like log(q)"
            ),
        },
        "smallest_tower_specialization_not_a_field_sweep": {
            "q": q_small,
            "square_affine_group_order": square_group_small,
            "full_affine_group_order": full_group_small,
            "members_each_endpoint_sign": square_orbit_small,
            "members_both_endpoint_signs": full_orbit_small,
        },
    }


def _derive_exact_certificate(guard: ResourceGuard) -> dict[str, object]:
    return {
        "seed": _derive_seed_certificate(guard),
        "base_change": _derive_base_change_certificate(guard),
        "affine_orbits_and_moments": _derive_orbit_certificate(guard),
    }


def _load_sources(guard: ResourceGuard) -> dict[str, dict[str, object]]:
    loaded: dict[str, dict[str, object]] = {}
    for name in sorted(SOURCE_LOCKS):
        guard.records()
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source-lock path must be a Path")
        remaining = MAX_SOURCE_BYTES - guard.source_bytes
        if remaining < 0:
            raise RuntimeError("source-byte cap already exceeded")
        with path.open("rb") as source_handle:
            data = source_handle.read(remaining + 1)
        if len(data) > remaining:
            raise RuntimeError("source-byte cap exceeded before full read")
        guard.bytes(len(data))
        if _lf_sha256(data) != lock["lf_sha256"]:
            raise RuntimeError(f"LF-normalized source hash mismatch: {name}")
        parsed = json.loads(data)
        if parsed.get("schema") != lock["schema"]:
            raise RuntimeError(f"source schema mismatch: {name}")
        claimed = parsed.get("payload_sha256")
        if claimed != lock["payload_sha256"]:
            raise RuntimeError(f"source payload lock mismatch: {name}")
        payload = dict(parsed)
        payload.pop("payload_sha256")
        if _canonical_sha256(payload) != claimed:
            raise RuntimeError(f"canonical source payload mismatch: {name}")
        loaded[name] = parsed
    return loaded


def _validate_source_compatibility(
    sources: dict[str, dict[str, object]], guard: ResourceGuard
) -> dict[str, object]:
    stack = sources["marked_stack_adapter"]
    rare = sources["rare_event_certificate"]
    guard.operations(24)

    cardinalities = stack.get("exact_cardinalities")
    groupoid = stack.get("groupoid_equivalence")
    odd_weight = stack.get("odd_central_weight")
    if not isinstance(cardinalities, dict) or not isinstance(groupoid, dict):
        raise TypeError("marked-stack source schema drifted")
    square_group = groupoid.get("square_affine_group")
    if not isinstance(square_group, dict):
        raise TypeError("marked-stack square-affine source drifted")
    if cardinalities.get("H5") != "q^4*(q-1)=q^5-q^4":
        raise ArithmeticError("marked-stack family cardinality drifted")
    if cardinalities.get("AGL_full") != "q*(q-1)":
        raise ArithmeticError("marked-stack full affine order drifted")
    if square_group.get("order") != "q*(q-1)/2":
        raise ArithmeticError("marked-stack square affine order drifted")
    if square_group.get("polynomial_right_action") != (
        "D(T)|(alpha,beta)=alpha^(-5)*D(alpha*T+beta)"
    ):
        raise ArithmeticError("marked-stack affine action drifted")
    if not isinstance(odd_weight, dict) or "sends U_D to -U_D" not in str(
        odd_weight.get("exact_result")
    ):
        raise ArithmeticError("marked-stack twist sign drifted")

    definition = rare.get("definition")
    compact = rare.get("compact_resonance_certificate")
    if not isinstance(definition, dict) or not isinstance(compact, dict):
        raise TypeError("rare-event source schema drifted")
    if definition.get("channel") != "r_D(10)=q^5*chi_(10,0)(U_D)":
        raise ArithmeticError("rare-event Sym10 normalization drifted")
    if compact.get("sym10_dimension") != 286:
        raise ArithmeticError("rare-event Sym10 dimension drifted")
    rigidity = compact.get("equality_rigidity")
    if not isinstance(rigidity, dict) or rigidity.get("only_equality_classes") != [
        "I",
        "-I",
    ]:
        raise ArithmeticError("rare-event scalar equality classification drifted")
    expected_rows = [
        {
            "U": "I",
            "a": "-4*sqrt(q)",
            "b": "6*q",
            "P": "(1-sqrt(q)*T)^4",
            "r_10": "286*q^5",
        },
        {
            "U": "-I",
            "a": "4*sqrt(q)",
            "b": "6*q",
            "P": "(1+sqrt(q)*T)^4",
            "r_10": "286*q^5",
        },
    ]
    if compact.get("scalar_coefficient_rows") != expected_rows:
        raise ArithmeticError("rare-event scalar coefficient rows drifted")

    return {
        "marked_stack_adapter": {
            "validated_claims": [
                "|H5(q)|=q^4*(q-1)",
                "|AGL(1,q)|=q*(q-1)",
                "|G_square|=q*(q-1)/2",
                "D|(alpha,beta)=alpha^(-5)*D(alpha*T+beta)",
                "a nonsquare affine coset sends U_D to -U_D",
            ],
            "role": (
                "independent locked cross-check of the rederived action, counting "
                "measure, and quadratic-twist sign"
            ),
        },
        "rare_event_certificate": {
            "validated_claims": [
                "r_D(10)=q^5*chi_(10,0)(U_D)",
                "dim Sym^10(C^4)=286",
                "compact equality occurs only at U=I or U=-I",
                "the two scalar coefficient rows have r_D(10)=286*q^5",
            ],
            "role": "normalization and compatibility only; realization is rederived here",
        },
    }


def _source_manifest() -> list[dict[str, object]]:
    manifest: list[dict[str, object]] = []
    for name in sorted(SOURCE_LOCKS):
        lock = SOURCE_LOCKS[name]
        path = lock["path"]
        if not isinstance(path, Path):
            raise TypeError("source-lock path must be a Path")
        manifest.append(
            {
                "name": name,
                "path": path.relative_to(ROOT).as_posix(),
                "schema": lock["schema"],
                "lf_sha256": lock["lf_sha256"],
                "payload_sha256": lock["payload_sha256"],
                "audited_commit": lock["audited_commit"],
            }
        )
    return manifest


def build_fixture() -> dict[str, object]:
    started = time.perf_counter()
    guard = ResourceGuard()

    exact = _derive_exact_certificate(guard)
    exact_operations_before_sources = guard.exact_operations
    sources = _load_sources(guard)
    compatibility = _validate_source_compatibility(sources, guard)

    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_sym10_scalar_endpoint_realization.v1",
        "status": "EXACT_ALL_K_SCALAR_ENDPOINT_REALIZATION",
        "scope": {
            "family": "H5(q), monic squarefree quintics",
            "tower": "q=3^(4*k), k>=1",
            "finite_fields_enumerated": 0,
            "field_elements_enumerated": 0,
            "curves_enumerated": 0,
            "roots_numerically_approximated": 0,
            "random_samples": 0,
            "external_literature_used_by_producer": False,
        },
        "exact_certificate": exact,
        "source_compatibility": compatibility,
        "source_order_firewall": {
            "seed_base_change_and_orbit_algebra_closed_before_sources": True,
            "exact_operations_before_sources": exact_operations_before_sources,
            "locked_sources_applied_only_as_compatibility_checks": True,
        },
        "source_manifest": _source_manifest(),
        "claim_boundaries": [
            "The constructed two-orbit union gives lower bounds; it is not a classification of all scalar-endpoint members.",
            "The exact subset contribution is not a lower bound for the full signed odd moment, because other members can cancel it.",
            "No field-wide enumeration, asymptotic equidistribution, monodromy classification, motive, RH, GRH, or average-to-individual theorem is claimed.",
            "External characteristic-three classifications are literature consistency only and are not used by this replay.",
        ],
        "resource_contract": {
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "actual_source_bytes": guard.source_bytes,
            "maximum_source_records": MAX_SOURCE_RECORDS,
            "actual_source_records": guard.source_records,
            "maximum_exact_operations": MAX_EXACT_OPERATIONS,
            "actual_exact_operations": guard.exact_operations,
            "exact_operations_before_sources": exact_operations_before_sources,
            "maximum_wall_seconds": MAX_WALL_SECONDS,
            "arithmetic": (
                "theorem arithmetic uses exact integers and Fraction values; "
                "perf_counter is used only for the wall guard"
            ),
        },
        "replay": {
            "producer": OUTPUT_PATH.with_suffix(".py").relative_to(ROOT).as_posix(),
            "note": NOTE_PATH.relative_to(ROOT).as_posix(),
            "test": TEST_PATH.relative_to(ROOT).as_posix(),
            "write": (
                "python -B research/l-families/atlas/function_field/"
                "genus2_sym10_scalar_endpoint_realization.py --write"
            ),
            "check": (
                "python -B research/l-families/atlas/function_field/"
                "genus2_sym10_scalar_endpoint_realization.py --check"
            ),
        },
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    elapsed = time.perf_counter() - started
    if elapsed > MAX_WALL_SECONDS:
        raise RuntimeError("scalar-endpoint replay exceeded wall cap")
    return payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write canonical JSON")
    parser.add_argument("--check", action="store_true", help="check canonical JSON")
    args = parser.parse_args()
    if args.write == args.check:
        parser.error("choose exactly one of --write or --check")

    fixture = build_fixture()
    rendered = json.dumps(fixture, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
        print(f"wrote {OUTPUT_PATH}")
        return
    if not OUTPUT_PATH.exists():
        raise FileNotFoundError(f"missing canonical fixture: {OUTPUT_PATH}")
    if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
        raise RuntimeError(f"canonical fixture mismatch: {OUTPUT_PATH}")
    print(f"verified {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
