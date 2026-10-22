#!/usr/bin/env python3
"""Bounded exact geometry of the frozen genus-two toy-minor tail.

This packet deliberately does *not* enumerate finite fields or family members.
It reads the existing exact q=3,5,7 q-scan and affine-orbit fixtures, performs a
tiny integer coefficient-lattice reconstruction, and certifies symbolic
identities for

    P(T) = T^4 + a*T^3 + b*T^2 + q*a*T + q^2,
    K = q*a^2 - b^2,
    Delta = a^2 - 4*b + 8*q.

Delta is the discriminant of the real Weil polynomial

    R(X) = X^2 + a*X + (b - 2*q).

The scope is intentionally narrow: exact algebra valid for every admissible
reciprocal quartic, plus exact reconstruction from the already-frozen support
histograms at q=3,5,7.  No claim about an asymptotic tail law is made.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
from typing import Iterable, Sequence


HERE = Path(__file__).resolve().parent
Q_SCAN_FIXTURE = HERE / "genus2_q_scan.json"
AFFINE_FIXTURE = HERE / "genus2_affine_orbits.json"
FIXTURE = HERE / "genus2_tail_geometry.json"
FROZEN_Q_VALUES = (3, 5, 7)
MAX_LATTICE_CANDIDATES_PER_Q = 1_000
MAX_MOMENT_ORDER = 12


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _lf_normalized_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _fraction(value: Fraction) -> dict[str, object]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "text": f"{value.numerator}/{value.denominator}",
        "decimal_display_only": f"{float(value):.12f}",
    }


def _polynomial_text(coefficients_high_to_low: Sequence[int], variable: str = "T") -> str:
    degree = len(coefficients_high_to_low) - 1
    terms: list[str] = []
    for index, coefficient in enumerate(coefficients_high_to_low):
        exponent = degree - index
        if coefficient == 0:
            continue
        magnitude = abs(coefficient)
        if exponent == 0:
            body = str(magnitude)
        elif exponent == 1:
            body = variable if magnitude == 1 else f"{magnitude}*{variable}"
        else:
            body = f"{variable}^{exponent}" if magnitude == 1 else f"{magnitude}*{variable}^{exponent}"
        if not terms:
            terms.append(body if coefficient > 0 else f"-{body}")
        else:
            terms.append((" + " if coefficient > 0 else " - ") + body)
    return "".join(terms) if terms else "0"


def _multiply_low(left: Sequence[int], right: Sequence[int]) -> list[int]:
    product = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            product[i + j] += left_value * right_value
    return product


def _laurent_add(*polynomials: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            result[exponent] = result.get(exponent, 0) + coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def _laurent_multiply(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    result: dict[int, int] = {}
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            exponent = left_exponent + right_exponent
            result[exponent] = result.get(exponent, 0) + left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def _laurent_power(polynomial: dict[int, int], exponent: int) -> dict[int, int]:
    if exponent < 0:
        raise ValueError("Laurent-polynomial exponent must be nonnegative")
    result = {0: 1}
    factor = dict(polynomial)
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = _laurent_multiply(result, factor)
        remaining //= 2
        if remaining:
            factor = _laurent_multiply(factor, factor)
    return result


def q5_quotient_identity_residual(sign: int) -> dict[int, int]:
    """Residual of D(x)*(x+sign)^2/x^4=(u^2-1)*(u+2*sign)."""

    if sign not in (-1, 1):
        raise ValueError("sign must be -1 or 1")
    conductor = {5: 1, 3: 1, 1: 1}
    x_plus_sign = {1: 1, 0: sign}
    left = _laurent_multiply(
        _laurent_multiply(conductor, _laurent_power(x_plus_sign, 2)),
        {-4: 1},
    )
    u = {1: 1, -1: 1}
    right = _laurent_multiply(
        _laurent_add(_laurent_power(u, 2), {0: -1}),
        _laurent_add(u, {0: 2 * sign}),
    )
    return _laurent_add(left, {exponent: -value for exponent, value in right.items()})


def quartic_discriminant(a: int, b: int, q: int) -> int:
    """Discriminant of T^4+a*T^3+b*T^2+q*a*T+q^2.

    The explicit monic-quartic formula is kept independent of the specialized
    factorization, so tests can compare the two exact calculations.
    """

    c = q * a
    d = q * q
    return (
        256 * d**3
        - 192 * a * c * d**2
        - 128 * b**2 * d**2
        + 144 * b * c**2 * d
        - 27 * c**4
        + 144 * a**2 * b * d**2
        - 6 * a**2 * c**2 * d
        - 80 * a * b**2 * c * d
        + 18 * a * b * c**3
        + 16 * b**4 * d
        - 4 * b**3 * c**2
        - 27 * a**4 * d**2
        + 18 * a**3 * b * c * d
        - 4 * a**3 * c**3
        - 4 * a**2 * b**3 * d
        + a**2 * b**2 * c**2
    )


def tail_invariants(q: int, abs_a: int, b: int) -> dict[str, int]:
    if q <= 0 or abs_a < 0:
        raise ValueError("q must be positive and abs_a nonnegative")
    delta = abs_a * abs_a - 4 * b + 8 * q
    endpoint_slack = (b + 2 * q) ** 2 - 4 * q * abs_a * abs_a
    k_value = q * abs_a * abs_a - b * b
    edge_defect = 20 * q * q + k_value
    upper_coefficient_defect = 6 * q - b
    return {
        "K": k_value,
        "Delta": delta,
        "endpoint_slack_Gamma": endpoint_slack,
        "haar_edge_defect_E": edge_defect,
        "upper_coefficient_defect_U": upper_coefficient_defect,
    }


def is_usp4_trace_admissible(q: int, abs_a: int, b: int) -> bool:
    """Exact integer test for two real pair traces in [-2*sqrt(q),2*sqrt(q)]."""

    if q <= 0 or abs_a < 0 or abs_a * abs_a > 16 * q:
        return False
    invariants = tail_invariants(q, abs_a, b)
    return (
        invariants["Delta"] >= 0
        and b + 2 * q >= 0
        and invariants["endpoint_slack_Gamma"] >= 0
    )


def admissible_coefficient_lattice(q: int) -> tuple[dict[str, int], ...]:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(f"coefficient reconstruction is frozen at q={FROZEN_Q_VALUES}")
    tested = 0
    rows: list[dict[str, int]] = []
    for abs_a in range(isqrt(16 * q) + 1):
        for b in range(-2 * q, 6 * q + 1):
            tested += 1
            if tested > MAX_LATTICE_CANDIDATES_PER_Q:
                raise RuntimeError("coefficient-lattice candidate cap exceeded")
            if is_usp4_trace_admissible(q, abs_a, b):
                rows.append({"abs_a": abs_a, "b": b, **tail_invariants(q, abs_a, b)})
    return tuple(rows)


def repeated_angle_ladder(q: int) -> tuple[dict[str, int], ...]:
    """Integral Delta=0 coefficient pairs, indexed by abs(a)/2=r."""

    if q not in FROZEN_Q_VALUES:
        raise ValueError(f"repeated-angle reconstruction is frozen at q={FROZEN_Q_VALUES}")
    return tuple(
        {
            "r": r,
            "abs_a": 2 * r,
            "b": 2 * q + r * r,
            "K": -4 * q * q - r**4,
        }
        for r in range(isqrt(4 * q) + 1)
    )


def support_candidates(q: int, support: Iterable[int]) -> dict[int, tuple[dict[str, int], ...]]:
    requested = set(support)
    result: dict[int, list[dict[str, int]]] = {k_value: [] for k_value in requested}
    for row in admissible_coefficient_lattice(q):
        if row["K"] in result:
            result[row["K"]].append(row)
    if any(not rows for rows in result.values()):
        missing = sorted(k_value for k_value, rows in result.items() if not rows)
        raise ArithmeticError(f"q={q} support atoms lack admissible coefficients: {missing}")
    return {k_value: tuple(rows) for k_value, rows in result.items()}


def moment_atom_share(histogram: dict[int, int], atoms: Iterable[int], order: int) -> Fraction:
    if not 1 <= order <= MAX_MOMENT_ORDER:
        raise ValueError(f"moment order must lie in [1,{MAX_MOMENT_ORDER}]")
    selected = set(atoms)
    if not selected <= histogram.keys():
        raise KeyError("requested atom is absent from the frozen histogram")
    numerator = sum(histogram[k_value] * abs(k_value) ** order for k_value in selected)
    denominator = sum(count * abs(k_value) ** order for k_value, count in histogram.items())
    if denominator == 0:
        raise ZeroDivisionError("absolute moment vanished")
    return Fraction(numerator, denominator)


def _minimum_orbit_certificate(
    q: int,
    abs_a: int,
    minimum_k: int,
    minimum_count: int,
    affine_family: dict[str, object],
) -> dict[str, object]:
    group_order = int(affine_family["group"]["order"])  # type: ignore[index]
    stabilizer_histogram = affine_family["orbit_partition"][  # type: ignore[index]
        "stabilizer_order_histogram"
    ]
    if q == 5:
        witness = affine_family["nontrivial_stabilizer_witnesses"]["2"]  # type: ignore[index]
        if (
            int(witness["K_D"]) != minimum_k
            or int(witness["a_D_squared"]) != abs_a * abs_a
            or int(witness["orbit_size"]) != minimum_count
        ):
            raise ArithmeticError("q=5 minimum stabilizer witness no longer matches the support")
        proof = (
            "the frozen order-2 stabilizer witness has the minimum invariants and orbit size 10; "
            "the minimum K atom also has exactly 10 members"
        )
        stabilizer_order = 2
        orbit_size = int(witness["orbit_size"])
        representative = witness["representative_coefficients_low_to_high"]
        stabilizer_elements = witness["stabilizer_elements_alpha_beta"]
    else:
        if q % 4 != 3 or abs_a == 0 or set(stabilizer_histogram) != {"1", "2"}:
            raise ArithmeticError("free-minimum proof hypotheses changed")
        if minimum_count != group_order:
            raise ArithmeticError("minimum atom is not one full affine orbit")
        proof = (
            "all frozen nonfree orbits have stabilizer order 2; in odd characteristic every "
            "nonidentity affine involution has multiplier -1, while q=3,7 have chi(-1)=-1; "
            "a fixed member would therefore have a=0, contrary to the unique minimum pair"
        )
        stabilizer_order = 1
        orbit_size = group_order
        representative = None
        stabilizer_elements = [[1, 0]]
    if orbit_size * stabilizer_order != group_order or orbit_size != minimum_count:
        raise ArithmeticError("minimum orbit-stabilizer reconstruction failed")
    return {
        "orbit_count": 1,
        "orbit_size": orbit_size,
        "stabilizer_order": stabilizer_order,
        "proof_from_frozen_aggregate_data": proof,
        "representative_coefficients_low_to_high_if_frozen": representative,
        "stabilizer_elements_alpha_beta_if_frozen": stabilizer_elements,
    }


def _frobenius_shape(q: int, abs_a: int, b: int, delta: int) -> dict[str, object]:
    # Choose the negative-a representative used in the existing findings.
    a = -abs_a
    polynomial_high = [1, a, b, q * a, q * q]
    real_high = [1, a, b - 2 * q]
    record: dict[str, object] = {
        "chosen_a": a,
        "frobenius_polynomial_coefficients_high_to_low": polynomial_high,
        "frobenius_polynomial": _polynomial_text(polynomial_high),
        "real_weil_polynomial_coefficients_high_to_low": real_high,
        "real_weil_polynomial": _polynomial_text(real_high),
        "real_weil_discriminant": delta,
        "quartic_discriminant": quartic_discriminant(a, b, q),
    }
    square_root = isqrt(delta)
    if square_root * square_root == delta:
        if (abs_a + square_root) % 2:
            raise ArithmeticError("square real-Weil discriminant has the wrong parity")
        traces = sorted(((abs_a - square_root) // 2, (abs_a + square_root) // 2))
        factors_low = ([q, -traces[0], 1], [q, -traces[1], 1])
        if _multiply_low(*factors_low) != list(reversed(polynomial_high)):
            raise ArithmeticError("elliptic factor reconstruction failed")
        record.update(
            {
                "elliptic_trace_factors": traces,
                "factorization": (
                    f"({_polynomial_text(list(reversed(factors_low[0])))})*"
                    f"({_polynomial_text(list(reversed(factors_low[1])))})"
                ),
                "shape": "SPLIT_ISOTYPIC" if traces[0] == traces[1] else "SPLIT_NONISOTYPIC",
                "shape_proof": (
                    "the real Weil polynomial splits over Z; the two displayed quadratic "
                    "q-Weil factors are exact"
                ),
            }
        )
    else:
        if q != 7 or polynomial_high != [1, -7, 25, -49, 49]:
            raise ArithmeticError("unexpected nonsquare frozen minimum")
        # Modulo 2 this is Phi_5.  It has no linear root, and the only monic
        # irreducible quadratic over F_2 is T^2+T+1, which leaves remainder T+1.
        record.update(
            {
                "real_trace_field": "Q(sqrt(5))",
                "factorization": "IRREDUCIBLE_OVER_Q",
                "shape": "FQ_SIMPLE",
                "shape_proof": (
                    "modulo 2 the quartic is T^4+T^3+T^2+T+1=Phi_5; it has no F_2 root "
                    "and division by the sole irreducible quadratic T^2+T+1 leaves T+1"
                ),
                "mod_2_irreducibility_certificate": {
                    "coefficients_high_to_low": [1, 1, 1, 1, 1],
                    "values_at_0_and_1": [1, 1],
                    "remainder_mod_T2_plus_T_plus_1": "T+1",
                    "remainder_coefficients_high_to_low": [1, 1],
                },
            }
        )
    return record


def _q5_special_curve_geometry(affine_family: dict[str, object]) -> dict[str, object]:
    witness = affine_family["nontrivial_stabilizer_witnesses"]["2"]  # type: ignore[index]
    coefficients = list(witness["representative_coefficients_low_to_high"])
    if coefficients != [0, 1, 0, 1, 0, 1]:
        raise ArithmeticError("q=5 minimum representative changed")
    if q5_quotient_identity_residual(1) or q5_quotient_identity_residual(-1):
        raise ArithmeticError("q=5 elliptic quotient identity failed")
    return {
        "status": "EXACT_FOR_THE_FROZEN_Q5_MINIMUM_REPRESENTATIVE",
        "curve": "y^2=x^5+x^3+x over F_5",
        "odd_affine_symmetry": {
            "map": "(x,y)->(-x,2y)",
            "order": 4,
            "square": "hyperelliptic involution (x,y)->(x,-y)",
            "affine_action_shadow": "(alpha,beta)=(-1,0) has order 2 after quotienting y-sign",
        },
        "reciprocal_involution": {
            "map": "tau:(x,y)->(1/x,y/x^3)",
            "order": 2,
            "identity": "x^6*D(1/x)=D(x)",
            "scope_note": "tau does not preserve the marked branch point at infinity and is not in AGL(1,F_5)",
        },
        "elliptic_quotients": [
            {
                "invariants": "u=x+1/x, v=y*(x+1)/x^2",
                "equation": "v^2=(u^2-1)*(u+2)",
                "symbolic_laurent_residual_zero": True,
            },
            {
                "invariants": "u=x+1/x, w=y*(x-1)/x^2",
                "equation": "w^2=(u^2-1)*(u-2)",
                "symbolic_laurent_residual_zero": True,
            },
        ],
        "interpretation": (
            "the non-affine involution gives an explicit elliptic splitting; the square "
            "Frobenius polynomial shows that the two quotient factors are in the same "
            "ordinary F_5 isogeny class of trace 2"
        ),
        "measure_warning": (
            "AGL stabilizers weight affine presentations with a marked rational Weierstrass "
            "point; they are not the full unmarked curve automorphism groups"
        ),
    }


def build_fixture() -> dict[str, object]:
    q_scan = json.loads(Q_SCAN_FIXTURE.read_text(encoding="utf-8"))
    affine = json.loads(AFFINE_FIXTURE.read_text(encoding="utf-8"))
    q_scan_by_q = {int(row["q"]): row for row in q_scan["families"]}
    affine_by_q = {int(row["q"]): row for row in affine["families"]}
    if tuple(sorted(q_scan_by_q)) != FROZEN_Q_VALUES or tuple(sorted(affine_by_q)) != FROZEN_Q_VALUES:
        raise ArithmeticError("source fixtures do not have exactly the frozen q values")

    families: list[dict[str, object]] = []
    frozen_minimum_shapes: list[str] = []
    for q in FROZEN_Q_VALUES:
        q_family = q_scan_by_q[q]
        affine_family = affine_by_q[q]
        histogram = {int(k_value): int(count) for k_value, count in q_family["K_histogram"].items()}
        candidates = support_candidates(q, histogram)
        minimum_k = min(histogram)
        minimum_candidates = candidates[minimum_k]
        if len(minimum_candidates) != 1:
            raise ArithmeticError(f"q={q} minimum K does not determine a unique coefficient pair")
        minimum = minimum_candidates[0]
        minimum_count = histogram[minimum_k]
        minimum_orbit = _minimum_orbit_certificate(
            q,
            minimum["abs_a"],
            minimum_k,
            minimum_count,
            affine_family,
        )
        lattice = admissible_coefficient_lattice(q)
        lattice_minimum_k = min(row["K"] for row in lattice)
        lattice_minima = [row for row in lattice if row["K"] == lattice_minimum_k]
        if len(lattice_minima) != 1 or lattice_minimum_k in histogram:
            raise ArithmeticError("frozen coefficient-lattice exclusion changed")
        ladder = repeated_angle_ladder(q)
        ladder_records: list[dict[str, object]] = []
        realized_positive_rungs: list[dict[str, object]] = []
        for rung in ladder:
            k_value = rung["K"]
            support_present = k_value in histogram
            row: dict[str, object] = {**rung, "support_present": support_present}
            if support_present:
                row["member_count_at_K"] = histogram[k_value]
                row["admissible_candidate_count_at_K"] = len(candidates[k_value])
                if rung["r"] > 0 and len(candidates[k_value]) == 1:
                    repeated_record = {
                        **row,
                        "all_members_at_K_are_repeated_angle": True,
                        "absolute_moment_12_share": _fraction(
                            moment_atom_share(histogram, [k_value], 12)
                        ),
                    }
                    realized_positive_rungs.append(repeated_record)
            ladder_records.append(row)

        shape = _frobenius_shape(q, minimum["abs_a"], minimum["b"], minimum["Delta"])
        frozen_minimum_shapes.append(str(shape["shape"]))
        moment_shares = {
            str(order): _fraction(moment_atom_share(histogram, [minimum_k], order))
            for order in range(2, MAX_MOMENT_ORDER + 1, 2)
        }
        first_majority = next(
            order
            for order in range(2, MAX_MOMENT_ORDER + 1, 2)
            if moment_atom_share(histogram, [minimum_k], order) > Fraction(1, 2)
        )
        negative_atoms = sorted(k_value for k_value in histogram if k_value < 0)
        member_mass = Fraction(minimum_count, int(q_family["member_count"]))
        coarse_orbit_mass = Fraction(1, int(affine_family["orbit_partition"]["orbit_count"]))
        families.append(
            {
                "q": q,
                "member_count": int(q_family["member_count"]),
                "support_atom_count": len(histogram),
                "minimum_tail_atom": {
                    "K": minimum_k,
                    "normalized_K": _fraction(Fraction(minimum_k, q * q)),
                    "member_count": minimum_count,
                    "unique_admissible_pair_up_to_a_sign": {
                        key: minimum[key]
                        for key in (
                            "abs_a",
                            "b",
                            "Delta",
                            "endpoint_slack_Gamma",
                            "haar_edge_defect_E",
                            "upper_coefficient_defect_U",
                        )
                    },
                    "orbit_certificate": minimum_orbit,
                    "frobenius_geometry": shape,
                    "absolute_moment_shares": moment_shares,
                    "first_even_moment_order_with_more_than_half_of_absolute_moment": first_majority,
                    "top_two_negative_atoms_moment_12_share": _fraction(
                        moment_atom_share(histogram, negative_atoms[:2], 12)
                    ),
                    "member_or_marked_stack_mass": _fraction(member_mass),
                    "coarse_uniform_orbit_mass": _fraction(coarse_orbit_mass),
                    "coarse_to_member_mass_ratio": _fraction(coarse_orbit_mass / member_mass),
                },
                "repeated_angle_ladder": ladder_records,
                "realized_positive_repeated_angle_rungs": realized_positive_rungs,
                "usp4_admissible_integer_coefficient_lattice": {
                    "abs_a_sign_quotiented_pair_count": len(lattice),
                    "minimum_K": lattice_minimum_k,
                    "minimum_pair": lattice_minima[0],
                    "minimum_normalized_K": _fraction(Fraction(lattice_minimum_k, q * q)),
                    "absent_from_frozen_family_support": True,
                    "actual_minus_lattice_minimum_K": minimum_k - lattice_minimum_k,
                    "actual_to_lattice_haar_edge_defect_ratio": _fraction(
                        Fraction(
                            minimum["haar_edge_defect_E"],
                            lattice_minima[0]["haar_edge_defect_E"],
                        )
                    ),
                },
                "source_reconstruction_checks": {
                    "every_K_support_atom_has_an_admissible_pair": True,
                    "minimum_pair_is_unique_up_to_a_sign": True,
                    "minimum_atom_is_one_affine_orbit": True,
                    "minimum_multiplicity_matches_q_scan": True,
                },
            }
        )

    if frozen_minimum_shapes != ["SPLIT_NONISOTYPIC", "SPLIT_ISOTYPIC", "FQ_SIMPLE"]:
        raise ArithmeticError("frozen minimum Frobenius shapes changed")
    q5_special = _q5_special_curve_geometry(affine_by_q[5])

    source_path = Path(__file__).resolve()
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_tail_geometry.v1",
        "raw_fixture_id": "FUNCTION_FIELD.GENUS2.Q3_Q5_Q7.TOY_MINOR.TAIL_GEOMETRY.V1",
        "rigor_level": "RIGOROUS_CERTIFIED_WITH_EXPLICIT_SCOPE_FIREWALLS",
        "scope": (
            "symbolic reciprocal-quartic geometry and exact reconstruction from the already-frozen "
            "q=3,5,7 K histograms and affine-orbit aggregates"
        ),
        "exact_symbolic_identities": {
            "status": (
                "VALID_FOR_EVERY_POSITIVE_INTEGER_Q_AND_INTEGER-COEFFICIENT "
                "ADMISSIBLE_RECIPROCAL_QUARTIC"
            ),
            "real_weil_polynomial": "R(X)=X^2+a*X+(b-2*q), P(T)=T^2*R(T+q/T)",
            "real_trace_discriminant": "Delta=a^2-4*b+8*q=(t_1-t_2)^2",
            "square_defect": "P(T)=(T^2+(a/2)*T+q)^2-(Delta/4)*T^2",
            "quartic_discriminant": (
                "disc(P)=q^2*Delta^2*Gamma, Gamma=(b+2*q)^2-4*q*a^2="
                "(6*q-b)^2-4*q*Delta"
            ),
            "endpoint_slack": "Gamma=(4*q-t_1^2)*(4*q-t_2^2)",
            "haar_edge_defect": (
                "20*q^2+K=q*Delta+(6*q-b)*(2*q+b), K=q*a^2-b^2"
            ),
            "repeated_angle_ladder": (
                "Delta=0 iff a=2*r, b=2*q+r^2 and P(T)=(T^2+r*T+q)^2; "
                "then K=-4*q^2-r^4 (replace r by -r to change the a convention)"
            ),
            "far_negative_implication": (
                "K<-4*q^2 implies t_1*t_2>0 and b>2*q; hence if E=20*q^2+K, "
                "then Delta<=E/q and 6*q-b<=E/(4*q)"
            ),
            "range": "K>=-20*q^2, with equality only at t_1=t_2=+/-2*sqrt(q)",
        },
        "families": families,
        "minimum_shape_trichotomy": {
            "status": "EXACT_FOR_Q_3_5_7_ONLY",
            "shapes_in_q_order": frozen_minimum_shapes,
            "consequence": (
                "all three minimum atoms dominate the tenth absolute moment, but they have split "
                "nonisotypic, repeated isotypic, and simple Frobenius types; repeated-angle or "
                "automorphism strata alone therefore do not explain the frozen high-moment tail"
            ),
        },
        "q5_special_curve_geometry": q5_special,
        "non_identifiability_ledger": {
            "uniform_orbit_K_or_H_mean": (
                "not recoverable from the frozen affine aggregate because it omits per-orbit K and H"
            ),
            "action_taken": (
                "record only the exactly identifiable minimum-orbit mass distortion; do not rerun "
                "finite-field enumeration and do not invent a coarse-orbit mean"
            ),
            "full_curve_stack_warning": (
                "the affine quotient remembers a rational branch point at infinity; non-affine PGL2 "
                "automorphisms, explicitly present at the q=5 minimum, are outside its stabilizers"
            ),
        },
        "resource_contract": {
            "frozen_q_values": list(FROZEN_Q_VALUES),
            "maximum_coefficient_lattice_candidates_per_q": MAX_LATTICE_CANDIDATES_PER_Q,
            "maximum_moment_order": MAX_MOMENT_ORDER,
            "field_enumeration": "FORBIDDEN_AND_NOT_USED",
            "member_enumeration": "FORBIDDEN_AND_NOT_USED",
            "external_dependencies": "none; Python 3.11+ standard library",
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/genus2_tail_geometry.py",
            "source_sha256_lf_normalized": _lf_normalized_sha256(source_path),
            "q_scan_fixture": "research/l-families/atlas/function_field/genus2_q_scan.json",
            "q_scan_fixture_canonical_sha256": _canonical_sha256(q_scan),
            "affine_fixture": "research/l-families/atlas/function_field/genus2_affine_orbits.json",
            "affine_fixture_canonical_sha256": _canonical_sha256(affine),
            "input_provenance": "existing exact frozen fixtures only",
        },
        "firewall": (
            "The all-q statements are algebraic identities and conditional inequalities for admissible "
            "reciprocal quartics. Every orbit, support, moment-share, lattice-exclusion, and shape "
            "classification is a three-field fact only. USp-admissible integer coefficients need not "
            "be realized by a Jacobian or by the marked quintic family. No asymptotic tail law, "
            "equidistribution rate, number-field transfer, or analytic detector claim is made."
        ),
    }
    payload["payload_sha256"] = _canonical_sha256(payload)
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare with this exact JSON fixture")
    parser.add_argument("--write", type=Path, help="write this exact JSON fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"genus-two tail-geometry fixture mismatch: {args.check}")
        print(f"OK: exact genus-two tail geometry matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact genus-two tail geometry {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
