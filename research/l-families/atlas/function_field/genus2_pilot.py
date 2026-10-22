#!/usr/bin/env python3
"""Exact genus-two function-field detector pilot over F_3.

The frozen run exhausts the monic squarefree quintics over F_3.  It uses the
elementary polynomial arithmetic in ``pilot.py`` and a second, independent
point-count reconstruction over F_3 and F_9.  No numerical root finder or
floating-point arithmetic is used.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Sequence

import pilot


F9 = tuple[int, int]
FROZEN_Q = 3
FROZEN_CONDUCTOR_DEGREE = 5
FROZEN_RECIPROCAL_DEGREE = 4


def f9_add(left: F9, right: F9) -> F9:
    """Add in F_9 = F_3[theta]/(theta^2 + 1)."""

    return ((left[0] + right[0]) % 3, (left[1] + right[1]) % 3)


def f9_multiply(left: F9, right: F9) -> F9:
    """Multiply pairs a+b*theta using theta^2=-1=2 in F_3."""

    return (
        (left[0] * right[0] + 2 * left[1] * right[1]) % 3,
        (left[0] * right[1] + left[1] * right[0]) % 3,
    )


def f9_elements() -> tuple[F9, ...]:
    return tuple(itertools.product(range(3), repeat=2))


def evaluate_over_f9(coefficients: pilot.Poly, value: F9) -> F9:
    result = (0, 0)
    for coefficient in reversed(coefficients):
        result = f9_add(f9_multiply(result, value), (coefficient % 3, 0))
    return result


def point_count_f3(conductor: pilot.Poly) -> int:
    """Count C_D(F_3), including the unique odd-degree point at infinity."""

    conductor = pilot.validate_conductor(conductor, FROZEN_Q)
    affine = 0
    for x in range(3):
        value = sum(coefficient * pow(x, exponent, 3) for exponent, coefficient in enumerate(conductor)) % 3
        affine += sum((y * y) % 3 == value for y in range(3))
    return affine + 1


def point_count_f9(conductor: pilot.Poly) -> int:
    """Count C_D(F_9), including the same unique point at infinity."""

    conductor = pilot.validate_conductor(conductor, FROZEN_Q)
    elements = f9_elements()
    square_multiplicities = Counter(f9_multiply(value, value) for value in elements)
    affine = sum(square_multiplicities[evaluate_over_f9(conductor, x)] for x in elements)
    return affine + 1


def l_polynomial_from_point_counts(n1: int, n2: int, q: int = FROZEN_Q) -> tuple[int, ...]:
    """Recover the genus-two numerator from N_1 and N_2 plus palindromy.

    With P(u)=1+a*u+b*u^2+q*a*u^3+q^2*u^4, one has
    a=N_1-q-1 and 2b=N_2-q^2-1+a^2.
    """

    if q != FROZEN_Q:
        raise ValueError("the exact point-count model is frozen at q=3")
    a = n1 - q - 1
    twice_b = n2 - q * q - 1 + a * a
    if twice_b % 2:
        raise ArithmeticError("point counts do not define an integral genus-two coefficient")
    b = twice_b // 2
    return (1, a, b, q * a, q * q)


def purity_certificate(l_coefficients: Sequence[int], q: int = FROZEN_Q) -> dict[str, object]:
    """Return an integer-only reciprocal-root modulus certificate.

    If P(u)=1+a*u+b*u^2+q*a*u^3+q^2*u^4, write
    P(u)=(1-x_1*u+q*u^2)(1-x_2*u+q*u^2).  The x_i are the
    roots of X^2+aX+(b-2q).  The checks below put both x_i in the exact
    interval [-2*sqrt(q),2*sqrt(q)] without approximating either root.
    """

    if not isinstance(q, int) or isinstance(q, bool) or q <= 0:
        raise ValueError("q must be a positive integer")
    coefficients = tuple(l_coefficients)
    if len(coefficients) != 5 or coefficients[0] != 1:
        raise ValueError("expected a degree-four L polynomial with constant coefficient one")
    a, b = coefficients[1], coefficients[2]
    palindromic = coefficients[3] == q * a and coefficients[4] == q * q
    discriminant = a * a - 4 * (b - 2 * q)
    center_inside = a * a <= 16 * q
    endpoint_base_nonnegative = b + 2 * q >= 0
    endpoints_outside_roots = (b + 2 * q) ** 2 >= 4 * q * a * a
    certified = (
        palindromic
        and discriminant >= 0
        and center_inside
        and endpoint_base_nonnegative
        and endpoints_outside_roots
    )
    return {
        "palindromic_functional_equation": palindromic,
        "pair_trace_polynomial_low_to_high": [b - 2 * q, a, 1],
        "pair_trace_discriminant": discriminant,
        "pair_traces_are_real": discriminant >= 0,
        "pair_trace_center_inside_interval": center_inside,
        "endpoint_base_nonnegative": endpoint_base_nonnegative,
        "endpoint_square_inequality": endpoints_outside_roots,
        "reciprocal_roots_have_modulus_sqrt_q": certified,
        "L_zeros_have_modulus_q_to_minus_one_half": certified,
    }


def conductor_involution(conductor: pilot.Poly, q: int = FROZEN_Q) -> pilot.Poly:
    """Return iota(D)(T)=-D(-T), monic for odd-degree monic D."""

    conductor = pilot.validate_conductor(conductor, q)
    return pilot.poly(((-1) ** (exponent + 1) * coefficient for exponent, coefficient in enumerate(conductor)), q)


def reciprocal_hankel_numerator(reciprocal: Sequence[int]) -> int:
    if len(reciprocal) < 4:
        raise ValueError("the 2x2 coefficient minor requires B_1 through B_3")
    return reciprocal[1] * reciprocal[3] - reciprocal[2] * reciprocal[2]


def _fraction_json(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def member_record(conductor: pilot.Poly, q: int = FROZEN_Q) -> dict[str, object]:
    conductor = pilot.validate_conductor(conductor, q)
    l_coeffs = pilot.l_coefficients(conductor, q)
    n1 = point_count_f3(conductor)
    n2 = point_count_f9(conductor)
    point_count_l = l_polynomial_from_point_counts(n1, n2, q)
    if l_coeffs != point_count_l:
        raise AssertionError("point counts and character sums give different L polynomials")

    direct = pilot.reciprocal_coefficients_direct(conductor, q, FROZEN_RECIPROCAL_DEGREE)
    formal = pilot.reciprocal_coefficients_formal(l_coeffs, FROZEN_RECIPROCAL_DEGREE)
    if direct != formal:
        raise AssertionError("direct Moebius coefficients differ from the formal reciprocal")
    if pilot.convolution_identity(l_coeffs, direct) != (1, 0, 0, 0, 0):
        raise AssertionError("Euler reciprocal convolution failed")

    a, b = l_coeffs[1], l_coeffs[2]
    minor = reciprocal_hankel_numerator(direct)
    closed_form = q * a * a - b * b
    if minor != closed_form:
        raise AssertionError("genus-two coefficient-Hankel identity failed")
    certificate = purity_certificate(l_coeffs, q)
    if not certificate["reciprocal_roots_have_modulus_sqrt_q"]:
        raise AssertionError("exact purity certificate failed")
    normalized_minor = Fraction(minor, q * q)
    return {
        "conductor_coefficients_low_to_high": list(conductor),
        "conductor": pilot.poly_string(conductor),
        "point_counts": {"F_3": n1, "F_9": n2, "point_at_infinity_added": 1},
        "L_coefficients_low_to_high": list(l_coeffs),
        "frobenius_trace": -a,
        "reciprocal_coefficients_B0_to_B4": list(direct),
        "toy_coefficient_hankel_minor_numerator": minor,
        "normalized_toy_coefficient_hankel_minor": _fraction_json(normalized_minor),
        "purity_certificate": certificate,
    }


def _histogram(values: Sequence[int]) -> dict[str, int]:
    counts = Counter(values)
    return {str(key): counts[key] for key in sorted(counts)}


def build_fixture(
    q: int = FROZEN_Q,
    conductor_degree: int = FROZEN_CONDUCTOR_DEGREE,
    reciprocal_degree: int = FROZEN_RECIPROCAL_DEGREE,
) -> dict[str, object]:
    if (q, conductor_degree, reciprocal_degree) != (
        FROZEN_Q,
        FROZEN_CONDUCTOR_DEGREE,
        FROZEN_RECIPROCAL_DEGREE,
    ):
        raise ValueError("the frozen genus-two fixture requires exactly q=3, degree 5, reciprocal degree 4")

    conductors = [
        conductor
        for conductor in pilot.monic_polynomials(q, conductor_degree)
        if pilot.is_squarefree(conductor, q)
    ]
    records = [member_record(conductor, q) for conductor in conductors]
    by_conductor = {
        tuple(record["conductor_coefficients_low_to_high"]): record for record in records
    }

    involution_checks = []
    fixed_count = 0
    for conductor, record in by_conductor.items():
        partner_conductor = conductor_involution(conductor, q)
        partner = by_conductor[partner_conductor]
        coefficients = record["L_coefficients_low_to_high"]
        partner_coefficients = partner["L_coefficients_low_to_high"]
        reciprocal = record["reciprocal_coefficients_B0_to_B4"]
        partner_reciprocal = partner["reciprocal_coefficients_B0_to_B4"]
        involution_checks.append(
            partner_coefficients
            == [(-1) ** degree * value for degree, value in enumerate(coefficients)]
            and partner_reciprocal
            == [(-1) ** degree * value for degree, value in enumerate(reciprocal)]
        )
        fixed_count += partner_conductor == conductor

    minors = [int(record["toy_coefficient_hankel_minor_numerator"]) for record in records]
    odd_probes = [
        int(record["reciprocal_coefficients_B0_to_B4"][1])
        * int(record["reciprocal_coefficients_B0_to_B4"][2])
        for record in records
    ]
    l_pairs = Counter(
        (
            int(record["L_coefficients_low_to_high"][1]),
            int(record["L_coefficients_low_to_high"][2]),
        )
        for record in records
    )
    minor_mean = Fraction(sum(minors), len(minors))
    odd_probe_mean = Fraction(sum(odd_probes), len(odd_probes))
    negative = min(
        (record for record in records if int(record["toy_coefficient_hankel_minor_numerator"]) < 0),
        key=lambda record: str(record["conductor"]),
    )
    zero = min(
        (record for record in records if int(record["toy_coefficient_hankel_minor_numerator"]) == 0),
        key=lambda record: str(record["conductor"]),
    )
    positive = min(
        (record for record in records if int(record["toy_coefficient_hankel_minor_numerator"]) > 0),
        key=lambda record: str(record["conductor"]),
    )

    producer_text = Path(__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
    payload: dict[str, object] = {
        "schema": "riemann.function_field.genus2_exact_pilot.v1",
        "raw_fixture_id": "FUNCTION_FIELD.F3.QUINTIC.GENUS2.EXACT.V1",
        "rigor_level": "RIGOROUS_CERTIFIED",
        "scope": "exhaustive finite family of all monic squarefree quintics over F_3",
        "field": {
            "q": q,
            "model": "F_3[T]",
            "quadratic_extension_for_point_counts": "F_9=F_3[theta]/(theta^2+1)",
        },
        "curve_convention": {
            "model": "C_D: y^2=D(x)",
            "projective_completion": "odd-degree hyperelliptic model",
            "point_at_infinity": "exactly one rational point over every finite extension",
            "point_count_formula": "N_m=q^m+1+sum_{x in F_(q^m)} chi_m(D(x))",
        },
        "object_metadata": {
            "family": "quadratic function-field L-functions / genus-two hyperelliptic numerators",
            "object_type": "self-dual quadratic character",
            "L_degree": 4,
            "conductor": "all monic squarefree degree-5 D in F_3[T]",
            "normalization": "P_D(u)=product_j(1-alpha_j*u), with |alpha_j|=sqrt(3)",
            "functional_equation": "P_D(u)=9*u^4*P_D(1/(3*u))",
            "analytic_rank": "not computed or inferred",
            "zero_data_provenance": "no imported zeros and no numerical root finder; exact integer certificates only",
        },
        "detector": {
            "id": "FUNCTION_FIELD.NORMALIZED_RECIPROCAL.HANKEL_MINOR_2X2.TOY",
            "definition": "H_D(n)=q^(-n/2)B_n for 1/P_D(u)=sum B_nu^n; det[[H1,H2],[H2,H3]]",
            "exact_identity": "q^2*det=q*a_1^2-a_2^2 for P=1+a_1*u+a_2*u^2+q*a_1*u^3+q^2*u^4",
            "failure_mode": "purity and the functional equation alone do not force a memberwise sign",
            "parity": "even under D(T) -> -D(-T), unlike B_1*B_2",
        },
        "producer": {
            "source": "research/l-families/atlas/function_field/genus2_pilot.py",
            "source_sha256_lf_normalized": hashlib.sha256(producer_text.encode("utf-8")).hexdigest(),
            "runtime_contract": "Python 3.11+ standard library; exact integer/rational arithmetic",
            "input_provenance": "complete deterministic generation, no external data",
        },
        "family": {
            "conductor_degree": conductor_degree,
            "member_count": len(records),
            "candidate_count": q**conductor_degree,
            "expected_squarefree_count": q**conductor_degree - q ** (conductor_degree - 1),
            "reciprocal_degree_checked_through": reciprocal_degree,
        },
        "exact_checks": {
            "point_counts_reconstruct_character_L_polynomial_for_every_member": True,
            "palindromic_functional_equation_for_every_member": all(
                record["purity_certificate"]["palindromic_functional_equation"] for record in records
            ),
            "direct_Moebius_coefficients_equal_formal_inverse_for_every_member": True,
            "L_times_reciprocal_is_one_through_checked_degree_for_every_member": True,
            "integer_purity_certificate_for_every_member": all(
                record["purity_certificate"]["reciprocal_roots_have_modulus_sqrt_q"] for record in records
            ),
            "coefficient_Hankel_closed_form_for_every_member": True,
            "twist_involution_coefficient_parity_for_every_member": all(involution_checks),
        },
        "family_statistics": {
            "L_a1_histogram": _histogram(
                [int(record["L_coefficients_low_to_high"][1]) for record in records]
            ),
            "L_a1_a2_histogram": {
                f"{a_1},{a_2}": l_pairs[(a_1, a_2)] for a_1, a_2 in sorted(l_pairs)
            },
            "N1_histogram": _histogram([int(record["point_counts"]["F_3"]) for record in records]),
            "N2_histogram": _histogram([int(record["point_counts"]["F_9"]) for record in records]),
            "toy_minor_numerator_histogram": _histogram(minors),
            "toy_minor_numerator_mean": _fraction_json(minor_mean),
            "normalized_toy_minor_mean": _fraction_json(minor_mean / (q * q)),
            "negative_member_count": sum(value < 0 for value in minors),
            "zero_member_count": sum(value == 0 for value in minors),
            "positive_member_count": sum(value > 0 for value in minors),
            "parity_odd_B1_B2_mean": _fraction_json(odd_probe_mean),
            "parity_odd_B1_B2_sign_counts": {
                "negative": sum(value < 0 for value in odd_probes),
                "zero": sum(value == 0 for value in odd_probes),
                "positive": sum(value > 0 for value in odd_probes),
            },
            "twist_involution_fixed_member_count": fixed_count,
        },
        "witnesses": {"negative": negative, "zero": zero, "positive": positive},
        "asymptotic_target": {
            "status": "CONJECTURAL_TARGET_NOT_A_THEOREM",
            "statement": "for the corresponding degree-5 family as odd q tends to infinity, the normalized toy-minor mean should approach the USp(4) Haar prediction -1",
            "heuristic": "q^-2*(q*a_1^2-a_2^2) corresponds to (Tr U)^2-e_2(U)^2",
            "finite_evidence": "the exhaustive q=3 mean is -104/243; its sign agrees but one field is not asymptotic evidence",
        },
        "firewall": (
            "This is a toy reciprocal-coefficient Hankel minor, not the atlas analytic Pick/Loewner "
            "kernel and not canonical XD or HCNC. Mixed signs prove only that exact purity plus the "
            "genus-two functional equation do not determine this toy minor's memberwise sign. The "
            "USp(4) limit is recorded solely as a target, not as a theorem or a consequence of this run."
        ),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="compare the generated fixture with this JSON file")
    parser.add_argument("--write", type=Path, help="write the generated compact fixture")
    args = parser.parse_args(argv)
    if args.check and args.write:
        parser.error("--check and --write are mutually exclusive")
    fixture = build_fixture()
    if args.check:
        expected = json.loads(args.check.read_text(encoding="utf-8"))
        if fixture != expected:
            raise SystemExit(f"fixture mismatch: {args.check}")
        print(f"OK: exact genus-two fixture matches {args.check}")
        return 0
    if args.write:
        args.write.parent.mkdir(parents=True, exist_ok=True)
        args.write.write_text(json.dumps(fixture, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"OK: wrote exact genus-two fixture {args.write}")
        return 0
    print(json.dumps(fixture, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
