#!/usr/bin/env python3
"""Replay the closed-place fixed-degree weight notch symbolically.

The producer source-locks the committed all-degree rational-place identity,
extends its Euler quotient to a declared squarefree closed-place conductor,
and performs only bounded integer and coefficient-ring algebra. It enumerates
no fields, irreducibles, curves, roots, zeros, or samples.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import time
from collections import Counter
from math import comb
from pathlib import Path
from typing import TypeAlias

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT = HERE / "quadratic_family_closed_place_weight_notch.json"
NOTE = HERE / "QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md"
TEST = ROOT / "tests" / "test_quadratic_family_closed_place_weight_notch.py"
SOURCE = HERE / "quadratic_family_multiplace_l_function_identity.json"
SOURCE_COMMIT = "c94466e28a48ec429150f63de6d334d4c4f60110"
SOURCE_BLOB = "f6183be7e06b284f3cc2c3c4a6ffe5b970c0411e"
SOURCE_LF_SHA256 = "b4529c82d40575593e4c346e4cdfa0aaee417618886b5b1ab448c2469c87ca9e"
SOURCE_PAYLOAD_SHA256 = (
    "ddd7332102007ceda079e7b85dd0a482642c3d999dac779dde220af4e3b27c7d"
)
SOURCE_BYTES = 10_738
SCHEMA = "riemann.function_field.quadratic_family_closed_place_weight_notch.v1"

MAX_REPLAY_N = 7
MAX_REPLAY_PROFILE_TOTAL = 10
MAX_REPLAY_PROFILES = 160
MAX_SYMBOLIC_N = 10
MAX_PROFILE_LENGTH = 12
MAX_PROFILE_TOTAL = 20
MAX_SERIES_K = 8
MAX_SOURCE_BYTES = 16_384
MAX_OUTPUT_BYTES = 32_768
WALL_SECONDS = 4.0

Profile: TypeAlias = tuple[int, ...]
QPoly: TypeAlias = dict[int, int]
PCoefficients: TypeAlias = dict[int, QPoly]
CharacterExpr: TypeAlias = dict[int, int]
WeightExpr: TypeAlias = dict[tuple[int, int], int]
FactorRecord: TypeAlias = tuple[str, int, int]


def normalize_profile(degrees: tuple[int, ...] | list[int]) -> Profile:
    profile = tuple(sorted(degrees))
    if not profile or any(degree < 1 for degree in profile):
        raise ValueError("a closed-place profile requires positive factor degrees")
    if len(profile) > MAX_PROFILE_LENGTH:
        raise ValueError("closed-place profile-length cap exceeded")
    if sum(profile) > MAX_PROFILE_TOTAL:
        raise ValueError("closed-place profile-degree cap exceeded")
    return profile


def profile_coefficients(
    degrees: tuple[int, ...] | list[int], max_k: int
) -> tuple[int, ...]:
    """Return [x^k] product_i (1-x^d_i)^-1 through max_k."""
    profile = normalize_profile(degrees)
    if not 0 <= max_k <= MAX_SERIES_K:
        raise ValueError("profile-series cap exceeded")
    coefficients = [1] + [0] * max_k
    for degree in profile:
        for k in range(degree, max_k + 1):
            coefficients[k] += coefficients[k - degree]
    return tuple(coefficients)


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
    return _clean_qpoly(
        {power: scalar * coefficient for power, coefficient in polynomial.items()}
    )


def profile_kernel_coefficients(
    degrees: tuple[int, ...] | list[int], max_k: int
) -> tuple[QPoly, ...]:
    coefficients = profile_coefficients(degrees, max_k)
    rows: list[QPoly] = []
    for k, coefficient in enumerate(coefficients):
        row = {0: coefficient}
        if k:
            row[1] = -coefficients[k - 1]
        rows.append(_clean_qpoly(row))
    return tuple(rows)


def _validate_symbolic_degree(n: int) -> None:
    if not 2 <= n <= MAX_SYMBOLIC_N:
        raise ValueError(
            f"symbolic family-degree replay requires 2<=n<={MAX_SYMBOLIC_N}"
        )


def _add_p_coefficient(
    expansion: PCoefficients, index: int, coefficient: QPoly
) -> None:
    if index < 0:
        return
    expansion[index] = _add_qpoly(expansion.get(index, {}), coefficient)
    if not expansion[index]:
        expansion.pop(index)


def original_p_coefficient_expansion(
    n: int, degrees: tuple[int, ...] | list[int]
) -> PCoefficients:
    """Expand the closed-place coefficient theorem in the p_j basis."""
    _validate_symbolic_degree(n)
    profile = normalize_profile(degrees)
    kernels = profile_kernel_coefficients(profile, n // 2)
    even_conductor_degree = sum(profile) % 2 == 0
    expansion: PCoefficients = {}
    for k, coefficient in enumerate(kernels):
        index = n - 2 * k
        _add_p_coefficient(expansion, index, coefficient)
        if even_conductor_degree:
            _add_p_coefficient(expansion, index - 1, _scale_qpoly(coefficient, -1))
    return expansion


def d_coefficient_expansion(
    n: int, degrees: tuple[int, ...] | list[int]
) -> dict[int, int]:
    """Return coefficients of D_r=p_r-q*p_(r-2)."""
    _validate_symbolic_degree(n)
    profile = normalize_profile(degrees)
    coefficients = profile_coefficients(profile, n // 2)
    even_conductor_degree = sum(profile) % 2 == 0
    result: dict[int, int] = {}
    for k, coefficient in enumerate(coefficients):
        index = n - 2 * k
        result[index] = result.get(index, 0) + coefficient
        if even_conductor_degree and index - 1 >= 0:
            result[index - 1] = result.get(index - 1, 0) - coefficient
    return {index: coefficient for index, coefficient in result.items() if coefficient}


def regrouped_p_coefficient_expansion(
    n: int, degrees: tuple[int, ...] | list[int]
) -> PCoefficients:
    expansion: PCoefficients = {}
    for index, coefficient in d_coefficient_expansion(n, degrees).items():
        _add_p_coefficient(expansion, index, {0: coefficient})
        _add_p_coefficient(expansion, index - 2, {1: -coefficient})
    return expansion


def conductor_genus(degrees: tuple[int, ...] | list[int]) -> int:
    conductor_degree = sum(normalize_profile(degrees))
    return (conductor_degree - 1) // 2


def reciprocity_adapter_signs_agree(
    q: int, conductor_degree: int, prime_degree: int
) -> bool:
    """Check the parity identity behind G=(-1)^M*Q, without a field."""
    if q < 3 or q % 2 == 0 or conductor_degree < 1 or prime_degree < 1:
        raise ValueError(
            "reciprocity parity replay requires odd q>=3 and positive degrees"
        )
    reciprocity_sign = -1 if ((q - 1) // 2) * conductor_degree * prime_degree % 2 else 1
    constant_twist_sign = (
        -1 if conductor_degree * ((q**prime_degree - 1) // 2) % 2 else 1
    )
    return reciprocity_sign == constant_twist_sign


def _elementary_character(index: int, genus: int) -> CharacterExpr:
    if genus < 0:
        raise ValueError("genus must be nonnegative")
    if index < 0 or index > 2 * genus:
        return {}
    reduced = min(index, 2 * genus - index)
    return {fundamental: 1 for fundamental in range(reduced, -1, -2)}


def delta_character_expression(index: int, genus: int) -> CharacterExpr:
    result = _elementary_character(index, genus)
    for fundamental, coefficient in _elementary_character(index - 2, genus).items():
        result[fundamental] = result.get(fundamental, 0) - coefficient
    return {
        fundamental: coefficient
        for fundamental, coefficient in result.items()
        if coefficient
    }


def weighted_character_expansion(
    n: int, degrees: tuple[int, ...] | list[int]
) -> WeightExpr:
    profile = normalize_profile(degrees)
    genus = conductor_genus(profile)
    result: WeightExpr = {}
    for index, d_coefficient in d_coefficient_expansion(n, profile).items():
        sign = -1 if index % 2 else 1
        for fundamental, delta_coefficient in delta_character_expression(
            index, genus
        ).items():
            key = (index, fundamental)
            result[key] = result.get(key, 0) + d_coefficient * sign * delta_coefficient
    return {key: coefficient for key, coefficient in result.items() if coefficient}


def odd_notch_zero_condition(n: int, degrees: tuple[int, ...] | list[int]) -> bool:
    _validate_symbolic_degree(n)
    profile = normalize_profile(degrees)
    if sum(profile) != 2 * n - 1:
        raise ValueError(
            "odd-notch zero test requires primitive conductor degree 2*n-1"
        )
    return min(profile) > n // 2


def primitive_squarefree_profile(records: tuple[FactorRecord, ...]) -> Profile:
    """Validate symbolic primitive-conductor metadata; do not factor anything."""
    if not records:
        raise ValueError("at least one declared irreducible factor is required")
    labels: set[str] = set()
    degrees: list[int] = []
    for label, degree, exponent in records:
        if not label or label in labels:
            raise ValueError("declared irreducible factor labels must be distinct")
        labels.add(label)
        if degree < 1:
            raise ValueError("declared irreducible degrees must be positive")
        if exponent != 1:
            raise ValueError(
                "imprimitive/non-squarefree modulus metadata is refused; supply an already primitive squarefree conductor and handle imprimitive Euler deletions separately"
            )
        degrees.append(degree)
    return normalize_profile(degrees)


def _divisors(integer: int) -> tuple[int, ...]:
    return tuple(divisor for divisor in range(1, integer + 1) if integer % divisor == 0)


def _mobius(integer: int) -> int:
    if integer < 1:
        raise ValueError("Mobius input must be positive")
    remaining = integer
    prime_factors = 0
    prime = 2
    while prime * prime <= remaining:
        if remaining % prime == 0:
            remaining //= prime
            prime_factors += 1
            if remaining % prime == 0:
                return 0
            while remaining % prime == 0:
                remaining //= prime
        prime += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def irreducible_count(q: int, degree: int) -> int:
    """Return the exact count I_q(d), assuming q is a prime power."""
    if q < 2 or degree < 1:
        raise ValueError("irreducible-count formula requires q>=2 and d>=1")
    return (
        sum(
            _mobius(divisor) * q ** (degree // divisor) for divisor in _divisors(degree)
        )
        // degree
    )


def profile_feasibility(
    q: int, degrees: tuple[int, ...] | list[int]
) -> dict[str, object]:
    """Check degree multiplicities against I_q(d), without listing factors."""
    profile = normalize_profile(degrees)
    multiplicities = Counter(profile)
    rows = [
        {
            "degree": degree,
            "requested": requested,
            "available": irreducible_count(q, degree),
        }
        for degree, requested in sorted(multiplicities.items())
    ]
    return {
        "q_assumed_prime_power": q,
        "feasible": all(row["requested"] <= row["available"] for row in rows),
        "rows": rows,
    }


def _integer_partitions(total: int, minimum: int = 1) -> tuple[Profile, ...]:
    if total < 1 or total > MAX_REPLAY_PROFILE_TOTAL:
        raise ValueError("integer-profile replay is outside its total-degree cap")
    rows: list[Profile] = []
    if total >= minimum:
        rows.append((total,))
    for first in range(minimum, total // 2 + 1):
        for tail in _integer_partitions(total - first, first):
            rows.append((first,) + tail)
    if len(rows) > MAX_REPLAY_PROFILES:
        raise RuntimeError("integer-profile count cap exceeded")
    return tuple(rows)


def _all_replay_profiles() -> tuple[Profile, ...]:
    rows = tuple(
        profile
        for total in range(1, MAX_REPLAY_PROFILE_TOTAL + 1)
        for profile in _integer_partitions(total)
    )
    if len(rows) > MAX_REPLAY_PROFILES:
        raise RuntimeError("aggregate integer-profile cap exceeded")
    return rows


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
        "squarefree_series": "sum_{n>=0} sum_{D in H_n(q)} psi_A(D)*u^n = L(u,psi_A)*(1-q*u^2)/(1-u^2)^m",
        "general_coefficient": "If L=sum_j l_j*u^j and B_m,0=1, then S_n,m=sum_(j<=n, n-j even) l_j*B_m,(n-j)/2.",
    }
    if not isinstance(exact, dict) or any(
        exact.get(key) != value for key, value in expected.items()
    ):
        raise RuntimeError("locked Euler quotient or all-degree coefficient drifted")
    return payload


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
    reciprocity_checks = 0
    for q in (3, 5, 7, 9):
        for conductor_degree in range(1, 11):
            for prime_degree in range(1, 6):
                if not reciprocity_adapter_signs_agree(
                    q, conductor_degree, prime_degree
                ):
                    raise ArithmeticError("G=(-1)^M*Q reciprocity sign drifted")
                reciprocity_checks += 1
    profiles = _all_replay_profiles()
    replayed_pairs = 0
    for n in range(2, MAX_REPLAY_N + 1):
        for profile in profiles:
            if original_p_coefficient_expansion(
                n, profile
            ) != regrouped_p_coefficient_expansion(n, profile):
                raise ArithmeticError(
                    f"closed-place regrouping drifted at n={n}, profile={profile!r}"
                )
            replayed_pairs += 1

    for factor_count in range(1, 11):
        rational = (1,) * factor_count
        coefficients = profile_coefficients(rational, 4)
        expected = tuple(comb(factor_count + k - 1, k) for k in range(5))
        if coefficients != expected:
            raise ArithmeticError(
                f"rational-place denominator drifted at r={factor_count}"
            )

    low_cases = {
        "n_5_rational_odd_notch": weighted_character_expansion(5, (1,) * 9),
        "n_5_irreducible_odd_notch": weighted_character_expansion(5, (9,)),
        "n_5_mixed_odd_notch_2_plus_7": weighted_character_expansion(5, (2, 7)),
        "n_5_rational_even_notch": weighted_character_expansion(5, (1,) * 10),
        "n_5_irreducible_even_notch": weighted_character_expansion(5, (10,)),
        "n_5_mixed_even_notch_2_plus_8": weighted_character_expansion(5, (2, 8)),
    }
    expected_low_cases = {
        "n_5_rational_odd_notch": {(3, 3): -9, (1, 1): -45},
        "n_5_irreducible_odd_notch": {},
        "n_5_mixed_odd_notch_2_plus_7": {(1, 1): -1},
        "n_5_rational_even_notch": {
            (4, 4): -1,
            (3, 3): -10,
            (2, 2): -10,
            (1, 1): -55,
            (0, 0): -55,
        },
        "n_5_irreducible_even_notch": {(4, 4): -1},
        "n_5_mixed_even_notch_2_plus_8": {
            (4, 4): -1,
            (1, 1): -1,
            (0, 0): -1,
        },
    }
    if low_cases != expected_low_cases:
        raise ArithmeticError(f"closed-place low-case replay drifted: {low_cases!r}")

    odd_zero_profiles: list[dict[str, object]] = []
    even_leading_profiles: list[dict[str, object]] = []
    for n in range(2, 6):
        for profile in _integer_partitions(2 * n - 1):
            if odd_notch_zero_condition(n, profile):
                if weighted_character_expansion(n, profile):
                    raise ArithmeticError(
                        f"odd-notch zero drifted at n={n}, profile={profile!r}"
                    )
                odd_zero_profiles.append({"n": n, "profile": list(profile)})
        for profile in _integer_partitions(2 * n):
            expansion = weighted_character_expansion(n, profile)
            leading_key = (n - 1, n - 1)
            if expansion.get(leading_key) != (-1) ** n:
                raise ArithmeticError(
                    f"even-notch leading channel drifted at n={n}, profile={profile!r}"
                )
            if any(exponent > n - 1 for exponent, _ in expansion):
                raise ArithmeticError("even-notch higher channel survived")
            even_leading_profiles.append({"n": n, "profile": list(profile)})

    payload: dict[str, object] = {
        "schema": SCHEMA,
        "status": "PROVED_CLOSED_PLACE_EXTENSION_FROM_LOCKED_EULER_QUOTIENT_AND_EXACT_SYMBOLIC_REPLAY",
        "scope": "fixed n>=2 and fixed feasible primitive squarefree degree profile over odd prime powers q; no growing-profile or fixed-q unbounded-rank claim",
        "source_lock": {
            "path": SOURCE.relative_to(ROOT).as_posix(),
            "commit": SOURCE_COMMIT,
            "git_blob": SOURCE_BLOB,
            "sha256_lf_normalized": SOURCE_LF_SHA256,
            "payload_sha256": SOURCE_PAYLOAD_SHA256,
            "schema": source["schema"],
            "imported_squarefree_series": source["exact_identity"]["squarefree_series"],
            "imported_general_coefficient": source["exact_identity"][
                "general_coefficient"
            ],
            "transitive_packet_files": source["packet_files_lf_sha256"],
            "later_weight_notch_packets_imported": False,
        },
        "closed_place_character": {
            "conductor": "Q=product_i P_i, with distinct monic irreducibles P_i of degrees d_i and primitive conductor degree M=sum_i d_i",
            "character": "psi_Q(F)=(F/Q)=product_i (F/P_i), extended by zero when gcd(F,Q)!=1",
            "curve_adapter": "G=(-1)^M*Q and C_Q:y^2=G; polynomial reciprocity gives (R/Q)=(G/R) at every finite prime R",
            "bounded_reciprocity_parity_checks": reciprocity_checks,
            "infinity": "If M is odd, infinity ramifies and L(u,psi_Q)=P_C(u); if M is even, G is monic with split infinity and L(u,psi_Q)=(1-u)*P_C(u)",
            "genus": "g=floor((M-1)/2)",
        },
        "squarefree_series": {
            "formula": "sum_(D monic squarefree) psi_Q(D)*u^deg(D)=L(u,psi_Q)*(1-q*u^2)/product_i(1-u^(2*d_i))",
            "reason": "psi_Q^2 is the indicator of gcd(D,Q)=1, so L(u^2,psi_Q^2)=product_i(1-u^(2*d_i))/(1-q*u^2)",
            "rational_place_recovery": "When every d_i=1, the denominator is (1-u^2)^r and a_k=binom(r+k-1,k), exactly recovering the locked rational-place identity.",
        },
        "degree_profile_coefficients": {
            "definition": "a_k=[x^k] product_i(1-x^d_i)^(-1), with a_k=0 for k<0",
            "kernel": "b_k=a_k-q*a_(k-1)",
            "mixed_examples": {
                "profile_1_2_through_k_6": list(profile_coefficients((1, 2), 6)),
                "profile_2_3_through_k_6": list(profile_coefficients((2, 3), 6)),
            },
        },
        "exact_regrouped_identity": {
            "difference_channel": "Set p_j=0 outside 0<=j<=2*g. For r>=0 retain D_r=p_r-q*p_(r-2), even if p_r=0; set D_r=0 by convention for r<0.",
            "odd_M": "S_(n,Q)=sum_(k=0..floor(n/2)) a_k*D_(n-2*k)",
            "even_M": "S_(n,Q)=sum_(k=0..floor(n/2)) a_k*[D_(n-2*k)-D_(n-1-2*k)]",
            "top_channel": "D_n=(-1)^n*q^(n/2)*[e_n(U_Q)-e_(n-2)(U_Q)] is the unique q^(n/2) channel",
            "bounded_profile_count": len(profiles),
            "bounded_coefficient_pairs": replayed_pairs,
        },
        "primitive_conductor_weight_notch": {
            "location": "The interior top-weight notch is M=2*n-1 or M=2*n, both with g=n-1; smaller support zeros are not this notch.",
            "odd_M_2n_minus_1": {
                "exact_residual": "S_(n,Q)=sum_(k=1..floor(n/2)) a_k*D_(n-2*k)",
                "profile_leading_rule": "If h=min_i d_i<=floor(n/2), then a_k=0 for 1<=k<h and the first possible residual is a_h*D_(n-2*h), of raw weight (n-2*h)/2.",
                "exact_zero": "If min_i d_i>floor(n/2), then every relevant a_k vanishes and S_(n,Q)=0 exactly.",
                "irreducible_case": "A primitive irreducible conductor of degree 2*n-1 therefore has S_(n,Q)=0 exactly.",
                "normalized_scale": "For h<=floor(n/2), mu_(n,Q)=O_(n,profile)(q^(-(n+2*h)/2)); under the exact-zero condition mu_(n,Q)=0.",
            },
            "even_M_2n": {
                "exact_residual": "S_(n,Q)=-D_(n-1)+sum_(k=1..floor(n/2)) a_k*[D_(n-2*k)-D_(n-1-2*k)]",
                "profile_independent_leader": "The profile-independent leader is -D_(n-1)=(-1)^n*q^((n-1)/2)*chi_(omega_(n-1))",
                "normalized_scale": "mu_(n,Q)=O_(n,profile)(q^(-(n+1)/2))",
            },
            "bounded_odd_zero_rows": odd_zero_profiles,
            "bounded_even_leader_rows": even_leading_profiles,
            "n_5_character_replays": {
                label: _weight_rows(expression)
                for label, expression in low_cases.items()
            },
        },
        "normalization_and_connected_correction": {
            "family_size": "N_n=|H_n(q)|=q^(n-1)*(q-1)",
            "generic_raw_envelope": "For every fixed nonempty subprofile, its normalized moment is O_(n,profile)(q^(-n/2)).",
            "proper_partition_bound": "For a fixed labelled closed-place profile, kappa_(n,Q)-mu_(n,Q)=O_(n,profile)(q^(-n)); closed-place singleton means need not vanish and are retained in this bound.",
            "odd_zero_firewall": "An exact zero of the full odd-notch raw moment does not force the connected cumulant to vanish; proper-subprofile terms may leave O_(n,profile)(q^-n).",
            "even_notch": "For n>=2 the connected correction is below the profile-independent q^(-(n+1)/2) upper-weight channel.",
        },
        "primitive_and_feasibility_firewalls": {
            "primitive_only": "The input must already describe a primitive squarefree conductor: every factor is a distinct irreducible with exponent one. Nonsquarefree or imprimitive formal moduli are refused; their odd support may identify an inducing primitive character, but removed factors retain imprimitive Euler deletions and zero conditions, so no automatic reduction is made.",
            "metadata_refusal": "The producer rejects repeated factor labels and every declared exponent other than one; it never factors a polynomial.",
            "fixed_q_feasibility": "A degree-d multiplicity c_d is feasible only if c_d<=I_q(d)=(1/d)*sum_(e|d) mu(e)*q^(d/e), assuming q is a prime power.",
            "rational_special_case": "I_q(1)=q, so the old q>=r condition is recovered only for an all-degree-one profile.",
            "examples": {
                "q_3_three_rational_places": profile_feasibility(3, (1, 1, 1)),
                "q_3_four_rational_places": profile_feasibility(3, (1, 1, 1, 1)),
                "q_3_three_degree_two_places": profile_feasibility(3, (2, 2, 2)),
                "q_3_four_degree_two_places": profile_feasibility(3, (2, 2, 2, 2)),
            },
        },
        "twist_weight_and_claim_firewalls": {
            "source_sign": "The exact adapter is G=(-1)^M*Q. At odd M, silently using monic Q can be the nontrivial quadratic twist and changes odd exterior-character channels.",
            "sqrt_q": "q^(1/2) is Frobenius-weight notation, not a chosen element of F_q when q is nonsquare.",
            "fixed_profile": "All asymptotics fix n and the complete degree profile while q varies through feasible odd prime powers; no growing-rank/profile uniformity is claimed.",
            "standard_algebra": "The Euler quotient, polynomial reciprocity, infinity factor, and exterior-character identities are standard; no external novelty claim is made.",
            "no_arithmetic_promotion": "No profile channel is promoted to an individual motive, compatible system, functorial transfer, or global Euler-product identity.",
            "no_rh_claim": "No memberwise sign, zero theorem, principal-member amplifier, number-field transfer, RH, or GRH statement is proved.",
        },
        "resource_contract": {
            "distinct_source_files_read": 1,
            "source_content_reads": 1,
            "source_git_commands": 2,
            "source_bytes_read": SOURCE_BYTES,
            "maximum_source_bytes": MAX_SOURCE_BYTES,
            "profiles_replayed": len(profiles),
            "maximum_replay_profile_total_degree": MAX_REPLAY_PROFILE_TOTAL,
            "maximum_replay_profiles": MAX_REPLAY_PROFILES,
            "coefficient_pairs_replayed": replayed_pairs,
            "reciprocity_parity_checks": reciprocity_checks,
            "maximum_replay_family_degree": MAX_REPLAY_N,
            "maximum_symbolic_family_degree": MAX_SYMBOLIC_N,
            "maximum_symbolic_profile_length": MAX_PROFILE_LENGTH,
            "maximum_symbolic_profile_total_degree": MAX_PROFILE_TOTAL,
            "maximum_profile_series_index": MAX_SERIES_K,
            "maximum_output_bytes": MAX_OUTPUT_BYTES,
            "payload_build_wall_seconds_cap": WALL_SECONDS,
            "measured_wall_seconds_is_not_canonical": True,
            "finite_field_enumeration": False,
            "irreducible_enumeration": False,
            "polynomial_family_enumeration": False,
            "curve_enumeration": False,
            "root_enumeration": False,
            "zero_enumeration": False,
            "sampling": False,
            "floating_point_arithmetic": False,
        },
        "claim_boundary": [
            "The theorem is exact for a declared primitive squarefree closed-place conductor and fixed feasible degree profile; imprimitive modulus degrees are not substituted for the primitive conductor degree.",
            "All asymptotic scales are fixed-(n,profile) Weil upper envelopes, not lower bounds, attainment claims, typical-value laws, or growing-rank statements.",
            "The exact irreducible odd-notch raw zero does not imply a zero connected cumulant, special zero distribution, or memberwise sign.",
            "The curve is a finite-character adapter, not a claimed individual motive or compatible system; no external novelty claim is made.",
            "No principal-member amplification, number-field transfer, RH, or GRH statement is proved.",
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
