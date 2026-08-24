#!/usr/bin/env python3
"""Exact singular-stratum audit for the ambient product-tensor coefficient hypersurface.

This follow-up performs two bounded tasks only.  First, it checks the
singular-locus and pullback identities by sparse integer polynomial algebra.
Second, it convolves the locked genus-one trace and genus-two (a,b)
histograms at q=3,5,7.  It constructs no finite field, curve, or variety.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter
from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUTPUT_PATH = HERE / "tensor_trace_zero_singular_strata.json"
NOTE_PATH = HERE / "TENSOR_TRACE_ZERO_SINGULAR_STRATA.md"
TEST_PATH = ROOT / "tests" / "test_tensor_trace_zero_singular_strata.py"

GENUS1_FIXTURE_PATH = HERE / "genus1_cubic_family_laws.json"
GENUS1_SOURCE_PATH = HERE / "genus1_cubic_family_laws.py"
BALANCED_FIXTURE_PATH = HERE / "balanced_control_family_scan.json"
BALANCED_SOURCE_PATH = HERE / "balanced_control_family_scan.py"
PRODUCT_FIXTURE_PATH = HERE / "product_variety_tensor_family.json"
PRODUCT_SOURCE_PATH = HERE / "product_variety_tensor_family.py"
PRODUCT_NOTE_PATH = HERE / "PRODUCT_VARIETY_TENSOR_FAMILY.md"

FROZEN_Q_VALUES = (3, 5, 7)
MAX_HISTOGRAM_PAIR_OPERATIONS = 20_000


# A sparse polynomial is keyed by exponent tuples in a declared variable order.
Polynomial = dict[tuple[int, ...], int]


def _poly_clean(poly: Mapping[tuple[int, ...], int]) -> Polynomial:
    return {monomial: coefficient for monomial, coefficient in poly.items() if coefficient}


def _poly_constant(value: int, variables: int) -> Polynomial:
    return {} if value == 0 else {(0,) * variables: value}


def _poly_variable(index: int, variables: int) -> Polynomial:
    if not 0 <= index < variables:
        raise ValueError("polynomial variable index out of range")
    exponent = [0] * variables
    exponent[index] = 1
    return {tuple(exponent): 1}


def _poly_add(*polys: Mapping[tuple[int, ...], int]) -> Polynomial:
    if not polys:
        return {}
    dimensions = {len(monomial) for poly in polys for monomial in poly}
    if len(dimensions) > 1:
        raise ValueError("polynomial dimensions disagree")
    output: Counter[tuple[int, ...]] = Counter()
    for poly in polys:
        output.update(poly)
    return _poly_clean(output)


def _poly_scale(poly: Mapping[tuple[int, ...], int], scalar: int) -> Polynomial:
    return _poly_clean({monomial: scalar * coefficient for monomial, coefficient in poly.items()})


def _poly_multiply(
    left: Mapping[tuple[int, ...], int], right: Mapping[tuple[int, ...], int]
) -> Polynomial:
    if not left or not right:
        return {}
    left_dimensions = {len(monomial) for monomial in left}
    right_dimensions = {len(monomial) for monomial in right}
    if len(left_dimensions) != 1 or left_dimensions != right_dimensions:
        raise ValueError("polynomial dimensions disagree")
    output: Counter[tuple[int, ...]] = Counter()
    for left_monomial, left_coefficient in left.items():
        for right_monomial, right_coefficient in right.items():
            monomial = tuple(
                left_power + right_power
                for left_power, right_power in zip(left_monomial, right_monomial)
            )
            output[monomial] += left_coefficient * right_coefficient
    return _poly_clean(output)


def _poly_power(poly: Mapping[tuple[int, ...], int], exponent: int) -> Polynomial:
    if exponent < 0:
        raise ValueError("polynomial powers must be nonnegative")
    if poly:
        variables = len(next(iter(poly)))
    else:
        raise ValueError("cannot infer the dimension of the zero polynomial")
    output = _poly_constant(1, variables)
    base = dict(poly)
    power = exponent
    while power:
        if power & 1:
            output = _poly_multiply(output, base)
        power //= 2
        if power:
            base = _poly_multiply(base, base)
    return output


def _poly_derivative(
    poly: Mapping[tuple[int, ...], int], variable: int
) -> Polynomial:
    output: Counter[tuple[int, ...]] = Counter()
    for monomial, coefficient in poly.items():
        if not 0 <= variable < len(monomial):
            raise ValueError("polynomial variable index out of range")
        power = monomial[variable]
        if power:
            differentiated = list(monomial)
            differentiated[variable] -= 1
            output[tuple(differentiated)] += coefficient * power
    return _poly_clean(output)


def _poly_compose(
    poly: Mapping[tuple[int, ...], int],
    replacements: Sequence[Mapping[tuple[int, ...], int]],
) -> Polynomial:
    if not replacements:
        raise ValueError("at least one replacement is required")
    target_dimensions = {len(monomial) for replacement in replacements for monomial in replacement}
    if len(target_dimensions) != 1:
        raise ValueError("replacement dimensions disagree")
    target_variables = next(iter(target_dimensions))
    output: Polynomial = {}
    for monomial, coefficient in poly.items():
        if len(monomial) != len(replacements):
            raise ValueError("replacement count does not match source dimension")
        term = _poly_constant(coefficient, target_variables)
        for replacement, exponent in zip(replacements, monomial):
            if exponent:
                if not replacement:
                    term = {}
                    break
                term = _poly_multiply(term, _poly_power(replacement, exponent))
        output = _poly_add(output, term)
    return output


def symbolic_geometry_certificate() -> dict[str, object]:
    """Rebuild every displayed identity with exact sparse polynomial algebra."""

    # Variable order (u,v,w,h).
    u, v, w, h = (_poly_variable(index, 4) for index in range(4))
    u2 = _poly_power(u, 2)
    hypersurface = _poly_add(
        _poly_multiply(u2, h),
        _poly_scale(_poly_power(u, 4), -1),
        _poly_scale(_poly_multiply(u2, v), 2),
        u2,
        _poly_scale(_poly_multiply(u, w), -2),
        _poly_scale(_poly_power(w, 2), -1),
    )
    expected_hypersurface: Polynomial = {
        (2, 0, 0, 1): 1,
        (4, 0, 0, 0): -1,
        (2, 1, 0, 0): 2,
        (2, 0, 0, 0): 1,
        (1, 0, 1, 0): -2,
        (0, 0, 2, 0): -1,
    }
    if hypersurface != expected_hypersurface:
        raise ArithmeticError("hypersurface polynomial construction drifted")

    derivatives = tuple(_poly_derivative(hypersurface, index) for index in range(4))
    expected_derivatives = (
        {
            (1, 0, 0, 1): 2,
            (3, 0, 0, 0): -4,
            (1, 1, 0, 0): 4,
            (1, 0, 0, 0): 2,
            (0, 0, 1, 0): -2,
        },
        {(2, 0, 0, 0): 2},
        {(1, 0, 0, 0): -2, (0, 0, 1, 0): -2},
        {(2, 0, 0, 0): 1},
    )
    if derivatives != expected_derivatives:
        raise ArithmeticError("exact partial derivative certificate drifted")

    transverse_quadratic = _poly_clean(
        {
            monomial: coefficient
            for monomial, coefficient in hypersurface.items()
            if monomial[0] + monomial[2] == 2
        }
    )
    expected_quadratic = _poly_add(
        _poly_multiply(u2, h),
        _poly_scale(_poly_multiply(u2, v), 2),
        u2,
        _poly_scale(_poly_multiply(u, w), -2),
        _poly_scale(_poly_power(w, 2), -1),
    )
    if transverse_quadratic != expected_quadratic:
        raise ArithmeticError("transverse quadratic extraction drifted")

    # Variable order (u,v,r,h), where r=u+w and L=h+2v+2.
    u_r, v_r, r_r, h_r = (_poly_variable(index, 4) for index in range(4))
    one_r = _poly_constant(1, 4)
    l_r = _poly_add(h_r, _poly_scale(v_r, 2), _poly_scale(one_r, 2))
    canonical = _poly_add(
        _poly_multiply(l_r, _poly_power(u_r, 2)),
        _poly_scale(_poly_power(u_r, 4), -1),
        _poly_scale(_poly_power(r_r, 2), -1),
    )
    w_as_r_minus_u = _poly_add(r_r, _poly_scale(u_r, -1))
    converted = _poly_compose(hypersurface, (u_r, v_r, w_as_r_minus_u, h_r))
    if canonical != converted:
        raise ArithmeticError("F=L*u^2-u^4-r^2 coordinate identity drifted")

    # Variable order (u,x,y,z).  The pullback relation is u^2=x*y.
    u_p, x_p, y_p, z_p = (_poly_variable(index, 4) for index in range(4))
    one_p = _poly_constant(1, 4)
    t_p = _poly_add(x_p, z_p, _poly_scale(one_p, -2))
    r_pullback = _poly_multiply(u_p, t_p)
    l_pullback = _poly_add(_poly_power(t_p, 2), _poly_multiply(x_p, y_p))
    pulled_canonical = _poly_add(
        _poly_multiply(l_pullback, _poly_power(u_p, 2)),
        _poly_scale(_poly_power(u_p, 4), -1),
        _poly_scale(_poly_power(r_pullback, 2), -1),
    )
    quotient_witness = _poly_multiply(
        _poly_power(u_p, 2),
        _poly_add(_poly_multiply(x_p, y_p), _poly_scale(_poly_power(u_p, 2), -1)),
    )
    if pulled_canonical != quotient_witness:
        raise ArithmeticError("coefficient-map pullback did not reduce by u^2=x*y")

    # Variable order (x,y,z) for the determinant detector and branch images.
    x_d, y_d, z_d = (_poly_variable(index, 3) for index in range(3))
    one_d = _poly_constant(1, 3)
    v_map = _poly_add(
        _poly_multiply(x_d, z_d), y_d, _poly_scale(z_d, -2)
    )
    h_map = _poly_add(
        _poly_power(x_d, 2),
        _poly_multiply(x_d, y_d),
        _poly_scale(x_d, -4),
        _poly_scale(y_d, -2),
        _poly_power(z_d, 2),
        _poly_scale(one_d, 2),
    )
    detector_map = _poly_add(h_map, _poly_scale(v_map, 2), _poly_scale(one_d, 2))
    detector_expected = _poly_add(
        _poly_power(_poly_add(x_d, z_d, _poly_scale(one_d, -2)), 2),
        _poly_multiply(x_d, y_d),
    )
    if detector_map != detector_expected:
        raise ArithmeticError("pullback h+2*v+2 identity drifted")

    # x=0,z=2, with residual variable y.
    y_e = _poly_variable(0, 1)
    one_e = _poly_constant(1, 1)
    e_replacements = ({}, y_e, _poly_scale(one_e, 2))
    e_v = _poly_compose(v_map, e_replacements)
    e_h = _poly_compose(h_map, e_replacements)
    if e_v != _poly_add(y_e, _poly_scale(one_e, -4)):
        raise ArithmeticError("E-zero degenerate-branch v sign drifted")
    if e_h != _poly_add(_poly_scale(y_e, -2), _poly_scale(one_e, 6)):
        raise ArithmeticError("E-zero degenerate-branch h sign drifted")

    # y=0,z=2-x, with residual variable x.
    x_c = _poly_variable(0, 1)
    one_c = _poly_constant(1, 1)
    z_c = _poly_add(_poly_scale(one_c, 2), _poly_scale(x_c, -1))
    c_replacements = (x_c, {}, z_c)
    c_v = _poly_compose(v_map, c_replacements)
    c_h = _poly_compose(h_map, c_replacements)
    expected_c_v = _poly_scale(_poly_power(z_c, 2), -1)
    expected_c_h = _poly_add(
        _poly_scale(_poly_power(z_c, 2), 2), _poly_scale(one_c, -2)
    )
    if c_v != expected_c_v:
        raise ArithmeticError("C-zero degenerate-branch v sign drifted")
    if c_h != expected_c_h:
        raise ArithmeticError("C-zero degenerate-branch h sign drifted")

    # Exact formal factorizations of P_C on the two rank-drop branches.
    # Variable order (T,q,a) on the E-zero branch b=2q.
    t_e, q_e, a_e = (_poly_variable(index, 3) for index in range(3))
    one_factor = _poly_constant(1, 3)
    q_t2_e = _poly_multiply(q_e, _poly_power(t_e, 2))
    pc_e = _poly_add(
        one_factor,
        _poly_multiply(a_e, t_e),
        _poly_scale(q_t2_e, 2),
        _poly_multiply(_poly_multiply(q_e, a_e), _poly_power(t_e, 3)),
        _poly_multiply(_poly_power(q_e, 2), _poly_power(t_e, 4)),
    )
    factor_e = _poly_multiply(
        _poly_add(one_factor, q_t2_e),
        _poly_add(one_factor, _poly_multiply(a_e, t_e), q_t2_e),
    )
    if pc_e != factor_e:
        raise ArithmeticError("E-zero branch P_C factorization drifted")

    # Variable order (T,q,A) on the C-zero branch b=2q-A^2.
    t_c, q_c, A_c = (_poly_variable(index, 3) for index in range(3))
    q_t2_c = _poly_multiply(q_c, _poly_power(t_c, 2))
    pc_c = _poly_add(
        one_factor,
        _poly_multiply(
            _poly_add(_poly_scale(q_c, 2), _poly_scale(_poly_power(A_c, 2), -1)),
            _poly_power(t_c, 2),
        ),
        _poly_multiply(_poly_power(q_c, 2), _poly_power(t_c, 4)),
    )
    factor_c = _poly_multiply(
        _poly_add(one_factor, _poly_multiply(A_c, t_c), q_t2_c),
        _poly_add(one_factor, _poly_scale(_poly_multiply(A_c, t_c), -1), q_t2_c),
    )
    if pc_c != factor_c:
        raise ArithmeticError("C-zero branch P_C factorization drifted")

    return {
        "arithmetic": "sparse multivariate polynomials with integer coefficients",
        "hypersurface": "F=u^2*h-u^4+2*u^2*v+u^2-2*u*w-w^2",
        "exact_partial_derivatives": {
            "dF_du": "2*u*h-4*u^3+4*u*v+2*u-2*w",
            "dF_dv": "2*u^2",
            "dF_dw": "-2*u-2*w",
            "dF_dh": "u^2",
        },
        "adapted_coordinates": {
            "r": "u+w",
            "L": "h+2*v+2",
            "identity": "F=L*u^2-u^4-r^2",
            "pinch_coordinate": "lambda=L-u^2",
            "pinch_point_identity": "r^2=u^2*lambda",
            "total_rank_drop_germ": "pinch point times the free v-line",
            "jacobian_ideal_in_characteristic_not_2": "(r,u^2,u*L)",
            "reduced_jacobian_ideal": "rad(r,u^2,u*L)=(u,r)=(u,w)",
        },
        "full_reduced_affine_singular_locus": "u=w=0, with v and h free",
        "transverse_quadratic_cone": {
            "equation": "Q=(h+2*v+1)*u^2-2*u*w-w^2=L*u^2-r^2",
            "matrix_in_(u,w)": [["h+2*v+1", -1], [-1, -1]],
            "matrix_determinant": "-(h+2*v+2)=-L",
            "hessian_determinant": "-4*(h+2*v+2)=-4*L",
            "rank_drop_line_inside_singular_plane": "u=w=0 and h+2*v+2=0",
            "rank_on_line": 1,
            "rank_off_line": 2,
            "fixed_original_v_h_slice_on_rank_drop_line_over_C": (
                "F=-u^4-r^2, a slice-dependent A3 plane-curve singularity"
            ),
            "real_fixed_slice": "r^2+u^4=0 has only the real point u=r=0",
        },
        "coefficient_map_pullback": {
            "base_ring_scope": (
                "the normalized x,y,z pullback is over Q (or any base where q is a unit); "
                "the target hypersurface singular-locus calculation separately needs only characteristic not 2"
            ),
            "parameters": "x=A^2/q, y=a^2/q, z=b/q",
            "relations": {
                "u^2": "x*y",
                "v": "x*z+y-2*z",
                "w": "u*(x+z-3)",
                "h": "x^2+x*y-4*x-2*y+z^2+2",
            },
            "adapted_relations": {
                "t": "x+z-2",
                "r=u+w": "u*t",
                "L=h+2*v+2": "t^2+x*y=t^2+u^2",
                "F_pullback": "u^2*(x*y-u^2)=0",
            },
            "singular_preimage": "x*y=0: the union x=0 (A=0) and y=0 (a=0)",
            "reduced_rank_drop_preimage": "(x=0,z=2) union (y=0,z=2-x)",
            "scheme_pullback_after_clearing_q": {
                "R": "A^2+b-2*q",
                "singular_plane_ideal": "(A*a)",
                "rank_drop_line_ideal": "(A*a,R^2)",
                "reduced_rank_drop_ideal": (
                    "rad(A*a,R^2)=(A*a,R)=(A,b-2*q) intersect "
                    "(a,A^2+b-2*q)"
                ),
            },
            "E_trace_zero_component": {
                "condition": "A=0, hence x=0",
                "detector_square": "q^2*L=(b-2*q)^2",
                "rank_drop_condition": "b=2*q",
                "rank_drop_image": "v=y-4, h=6-2*y",
                "square_restriction": "q*(v+4)=a^2 is an integer square",
                "formal_P_C_factorization": "(1+q*T^2)*(1+a*T+q*T^2)",
            },
            "C_trace_zero_component": {
                "condition": "a=0, hence y=0",
                "detector_square": "q^2*L=(A^2+b-2*q)^2",
                "rank_drop_condition": "A^2+b=2*q",
                "rank_drop_image": "z=2-x, v=-z^2, h=2*z^2-2",
                "square_restriction": "2*q-b=A^2 is an integer square",
                "formal_P_C_factorization": (
                    "(1+A*T+q*T^2)*(1-A*T+q*T^2)"
                ),
            },
            "rank_drop_intersection": {
                "parameters": "A=a=0 and b=2*q",
                "image": "(u,v,w,h)=(0,-4,0,6)",
            },
            "exact_symbolic_checks": {
                "partials_rebuilt": True,
                "adapted_coordinate_identity": True,
                "transverse_quadratic_extracted": True,
                "detector_pullback_factored": True,
                "hypersurface_pullback_reduced_mod_u2_minus_xy": True,
                "both_rank_drop_branch_images_checked": True,
                "both_formal_P_C_factorizations_checked": True,
            },
        },
    }


@dataclass
class HistogramPairGuard:
    operations: int = 0

    def charge(self) -> None:
        self.operations += 1
        if self.operations >= MAX_HISTOGRAM_PAIR_OPERATIONS:
            raise RuntimeError(
                "strict histogram-pair cap reached: "
                f"{self.operations}>={MAX_HISTOGRAM_PAIR_OPERATIONS}"
            )


@dataclass
class StratumBucket:
    pair_count: int = 0
    source_atom_pair_count: int = 0
    transverse_degenerate_pair_count: int = 0
    joint_v_h_detector: Counter[tuple[int, int, int]] = field(default_factory=Counter)
    v: Counter[int] = field(default_factory=Counter)
    h: Counter[int] = field(default_factory=Counter)
    detector: Counter[int] = field(default_factory=Counter)
    signed_square_root: Counter[int] = field(default_factory=Counter)

    def add(
        self,
        weight: int,
        v_numerator: int,
        h_numerator: int,
        detector_numerator: int,
        signed_square_root_numerator: int,
    ) -> None:
        if weight <= 0:
            raise ValueError("histogram weights must be positive")
        self.pair_count += weight
        self.source_atom_pair_count += 1
        if detector_numerator == 0:
            self.transverse_degenerate_pair_count += weight
        key = (v_numerator, h_numerator, detector_numerator)
        self.joint_v_h_detector[key] += weight
        self.v[v_numerator] += weight
        self.h[h_numerator] += weight
        self.detector[detector_numerator] += weight
        self.signed_square_root[signed_square_root_numerator] += weight


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _lf_sha256(path: Path) -> str:
    normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(normalized).hexdigest()


def _fraction(value: Fraction | int) -> list[int]:
    rational = Fraction(value)
    return [rational.numerator, rational.denominator]


def _reject_floats(value: object, location: str = "root") -> None:
    if isinstance(value, float):
        raise ValueError(f"floating-point input forbidden at {location}")
    if isinstance(value, dict):
        for key, child in value.items():
            _reject_floats(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_floats(child, f"{location}[{index}]")


def _load_locked_fixture(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    claimed = payload.get("payload_sha256")
    if not isinstance(claimed, str):
        raise ValueError(f"{path.name} has no payload_sha256")
    unhashed = dict(payload)
    unhashed.pop("payload_sha256")
    if _canonical_sha256(unhashed) != claimed:
        raise ValueError(f"{path.name} payload hash is stale")
    return payload


def _validate_locked_inputs(
    genus1: Mapping[str, object],
    balanced: Mapping[str, object],
    product: Mapping[str, object],
) -> None:
    if genus1.get("schema") != "riemann.function_field.genus1_cubic_family_laws.v1":
        raise ValueError("unexpected genus-one fixture schema")
    genus1_normalization = genus1["normalization"]  # type: ignore[assignment]
    if genus1_normalization["trace"] != (
        "a_D=q+1-#E_D(F_q)=-sum_x quadratic_character(D(x))"
    ):
        raise ValueError("genus-one trace convention drifted")
    if genus1_normalization["l_polynomial"] != "L_D(T)=1-a_D*T+q*T^2":
        raise ValueError("genus-one L-polynomial convention drifted")

    if balanced.get("schema") != "riemann.function_field.balanced_control_family_scan.v1":
        raise ValueError("unexpected balanced-control fixture schema")
    definition = balanced["definition"]  # type: ignore[assignment]
    if definition["coefficient_normalization"] != (
        "L_D(u)=1+a_D*u+b_D*u^2+q*a_D*u^3+q^2*u^4"
    ):
        raise ValueError("genus-two coefficient convention drifted")
    frozen = balanced["frozen_enumeration_facts"]  # type: ignore[assignment]
    if tuple(frozen["q_values"]) != FROZEN_Q_VALUES:
        raise ValueError("balanced-control q ladder drifted")

    if product.get("schema") != "riemann.product-variety-tensor-family.v1":
        raise ValueError("unexpected product-tensor fixture schema")
    bridge = product["input_convention_bridge"]  # type: ignore[assignment]
    if bridge["genus1_fixture_trace"] != (
        "t_E=q+1-#E(F_q), with L_E=1-t_E*T+q*T^2"
    ):
        raise ValueError("product packet genus-one source convention drifted")
    if bridge["tensor_packet_coefficient"] != (
        "A=-t_E, so P_E=1+A*T+q*T^2"
    ):
        raise ValueError("A=-t_E bridge drifted")
    if bridge["frozen_histogram_conversion"] != (
        "each genus-one trace key t_E is negated before tensor coefficient reconstruction"
    ):
        raise ValueError("frozen A=-t_E conversion drifted")
    hypersurface = product["rank_three_coefficient_hypersurface"]  # type: ignore[assignment]
    if hypersurface["equation"] != (
        "u^2*h-u^4+2*u^2*v+u^2-2*u*w-w^2=0"
    ):
        raise ValueError("product hypersurface equation drifted")
    if hypersurface["normalization"] != (
        "u=c1/q, v=c2/q^2, w=c3/q^3, h=c4/q^4"
    ):
        raise ValueError("product coefficient normalization drifted")


def coefficient_image(A: int, a: int, b: int, q: int) -> tuple[Fraction, ...]:
    """Return (u,v,w,h) with the product packet's A=-t_E convention."""

    if q <= 0:
        raise ValueError("q must be positive")
    u = Fraction(-A * a, q)
    v = Fraction(A * A * b + q * a * a - 2 * q * b, q * q)
    w = Fraction(A * a * (-A * A - b + 3 * q), q * q)
    h = Fraction(
        A**4 + A * A * a * a - 4 * q * A * A - 2 * q * a * a + b * b + 2 * q * q,
        q * q,
    )
    return u, v, w, h


def hypersurface_value(
    u: Fraction | int,
    v: Fraction | int,
    w: Fraction | int,
    h: Fraction | int,
) -> Fraction:
    u_q, v_q, w_q, h_q = map(Fraction, (u, v, w, h))
    return (
        u_q * u_q * h_q
        - u_q**4
        + 2 * u_q * u_q * v_q
        + u_q * u_q
        - 2 * u_q * w_q
        - w_q * w_q
    )


def hypersurface_gradient(
    u: Fraction | int,
    v: Fraction | int,
    w: Fraction | int,
    h: Fraction | int,
) -> tuple[Fraction, ...]:
    u_q, v_q, w_q, h_q = map(Fraction, (u, v, w, h))
    return (
        2 * u_q * h_q - 4 * u_q**3 + 4 * u_q * v_q + 2 * u_q - 2 * w_q,
        2 * u_q * u_q,
        -2 * u_q - 2 * w_q,
        u_q * u_q,
    )


def transverse_detector_numerator(A: int, a: int, b: int, q: int) -> int:
    """Numerator of L=h+2v+2 over q^2; it is a sum of two squares."""

    if q <= 0:
        raise ValueError("q must be positive")
    return (A * A + b - 2 * q) ** 2 + A * A * a * a


def _field_rows_by_q(rows: Iterable[Mapping[str, object]]) -> dict[int, Mapping[str, object]]:
    output = {int(row["q"]): row for row in rows}
    if not set(FROZEN_Q_VALUES).issubset(output):
        raise ValueError("locked input is missing q=3,5,7")
    return output


def _law_summary(
    numerator_name: str,
    hist: Mapping[int, int],
    denominator: int,
    stratum_total: int,
    all_product_total: int,
) -> dict[str, object]:
    if stratum_total <= 0:
        raise ValueError("cannot normalize an empty stratum")
    if sum(hist.values()) != stratum_total:
        raise ArithmeticError("compressed histogram lost stratum mass")
    moments = []
    for order in range(3):
        raw_sum = sum(count * numerator**order for numerator, count in hist.items())
        moments.append(
            {
                "order": order,
                "raw_numerator_power_sum": raw_sum,
                "conditional_mean": _fraction(
                    Fraction(raw_sum, stratum_total * denominator**order)
                ),
                "all_product_pair_moment_share": _fraction(
                    Fraction(raw_sum, all_product_total * denominator**order)
                ),
            }
        )
    return {
        "numerator_name": numerator_name,
        "normalization_denominator_before_reduction": denominator,
        "support_size": len(hist),
        "minimum_normalized_value": _fraction(Fraction(min(hist), denominator)),
        "maximum_normalized_value": _fraction(Fraction(max(hist), denominator)),
        "zero_value_pair_count": hist.get(0, 0),
        "moments_0_through_2": moments,
    }


def _summarize_bucket(
    bucket: StratumBucket,
    q: int,
    all_product_total: int,
    include_complete_distribution: bool = False,
) -> dict[str, object]:
    total = bucket.pair_count
    if total <= 0:
        raise ArithmeticError("frozen singular stratum unexpectedly empty")
    joint_atoms = [
        {
            "numerators_v_h_L_over_q_squared": [v_numerator, h_numerator, detector_numerator],
            "normalized_v_h_L": [
                _fraction(Fraction(v_numerator, q * q)),
                _fraction(Fraction(h_numerator, q * q)),
                _fraction(Fraction(detector_numerator, q * q)),
            ],
            "pair_count": count,
            "pair_fraction_within_stratum": _fraction(Fraction(count, total)),
            "pair_fraction_of_all_product_pairs": _fraction(
                Fraction(count, all_product_total)
            ),
        }
        for (v_numerator, h_numerator, detector_numerator), count in sorted(
            bucket.joint_v_h_detector.items()
        )
    ]
    if sum(atom["pair_count"] for atom in joint_atoms) != total:
        raise ArithmeticError("joint singular law lost mass")
    output: dict[str, object] = {
        "pair_count": total,
        "pair_fraction_of_all_product_pairs": _fraction(
            Fraction(total, all_product_total)
        ),
        "source_atom_pair_count": bucket.source_atom_pair_count,
        "transverse_degenerate_pair_count": bucket.transverse_degenerate_pair_count,
        "transverse_degenerate_fraction_within_stratum": _fraction(
            Fraction(bucket.transverse_degenerate_pair_count, total)
        ),
        "coordinate_distribution_summaries_and_moment_shares": {
            "v": _law_summary("V", bucket.v, q * q, total, all_product_total),
            "h": _law_summary("H", bucket.h, q * q, total, all_product_total),
            "transverse_rank_drop_detector_L": _law_summary(
                "L_num", bucket.detector, q * q, total, all_product_total
            ),
            "signed_square_root_R_over_q": _law_summary(
                "R", bucket.signed_square_root, q, total, all_product_total
            ),
        },
        "square_identity": "L=(R/q)^2 on u=w=0, with R=A^2+b-2*q",
    }
    if include_complete_distribution:
        output["complete_joint_v_h_transverse_detector_law"] = {
            "normalization": "v=V/q^2, h=H/q^2, L=L_num/q^2=h+2*v+2",
            "support_size": len(joint_atoms),
            "atoms": joint_atoms,
        }
    return output


def analyze_frozen_field(
    q: int,
    genus1_row: Mapping[str, object],
    balanced_row: Mapping[str, object],
    guard: HistogramPairGuard,
) -> dict[str, object]:
    if q not in FROZEN_Q_VALUES:
        raise ValueError(f"frozen census supports only q={FROZEN_Q_VALUES}")
    trace_histogram = {
        int(trace): int(count)
        for trace, count in genus1_row["model_trace_histogram"].items()  # type: ignore[union-attr]
    }
    if sum(trace_histogram.values()) != int(genus1_row["squarefree_model_count"]):
        raise ArithmeticError("genus-one trace histogram mass drifted")
    genus2_atoms = balanced_row["joint_a_D_b_D_law"]["atoms"]  # type: ignore[index]
    if sum(int(atom["member_count"]) for atom in genus2_atoms) != int(
        balanced_row["member_count"]
    ):
        raise ArithmeticError("genus-two joint histogram mass drifted")

    buckets = {
        "E_trace_zero_only": StratumBucket(),
        "C_trace_zero_only": StratumBucket(),
        "both_trace_zero": StratumBucket(),
        "singular_trace_zero_total": StratumBucket(),
        "transverse_degenerate_union": StratumBucket(),
    }
    product_pair_count = 0
    neither_pair_count = 0
    component_counts: Counter[str] = Counter()
    component_atom_pairs: Counter[str] = Counter()
    symbolic_member_checks = 0
    square_identity_checks = 0

    for source_trace_t_E, elliptic_count in sorted(trace_histogram.items()):
        # Locked source convention: L_E=1-t_E*T+q*T^2, while the tensor
        # packet writes P_E=1+A*T+q*T^2.  Therefore A=-t_E.
        A = -source_trace_t_E
        for atom in genus2_atoms:  # type: ignore[assignment]
            guard.charge()
            a = int(atom["a_D"])
            b = int(atom["b_D"])
            weight = elliptic_count * int(atom["member_count"])
            product_pair_count += weight

            u, v, w, h = coefficient_image(A, a, b, q)
            if hypersurface_value(u, v, w, h) != 0:
                raise ArithmeticError("locked histogram atom missed the tensor hypersurface")
            if u * u != Fraction(A * A * a * a, q * q):
                raise ArithmeticError("u^2=x*y pullback identity drifted")
            symbolic_member_checks += 1

            e_zero = A == 0
            c_zero = a == 0
            if not (e_zero or c_zero):
                neither_pair_count += weight
                continue
            if u != 0 or w != 0 or hypersurface_gradient(u, v, w, h) != (
                Fraction(0),
                Fraction(0),
                Fraction(0),
                Fraction(0),
            ):
                raise ArithmeticError("trace-zero atom did not land in the singular plane")

            v_numerator = A * A * b + q * a * a - 2 * q * b
            h_numerator = (
                A**4
                + A * A * a * a
                - 4 * q * A * A
                - 2 * q * a * a
                + b * b
                + 2 * q * q
            )
            detector_numerator = transverse_detector_numerator(A, a, b, q)
            if detector_numerator != h_numerator + 2 * v_numerator + 2 * q * q:
                raise ArithmeticError("L=h+2*v+2 numerator identity drifted")
            signed_root_numerator = A * A + b - 2 * q
            if detector_numerator != signed_root_numerator**2:
                raise ArithmeticError("trace-zero detector is not the claimed square")
            if math.isqrt(detector_numerator) ** 2 != detector_numerator:
                raise ArithmeticError("trace-zero detector failed its integer-square audit")
            square_identity_checks += 1

            if e_zero and c_zero:
                category = "both_trace_zero"
            elif e_zero:
                category = "E_trace_zero_only"
            else:
                category = "C_trace_zero_only"
            for bucket_name in (category, "singular_trace_zero_total"):
                buckets[bucket_name].add(
                    weight,
                    v_numerator,
                    h_numerator,
                    detector_numerator,
                    signed_root_numerator,
                )

            if e_zero:
                component_counts["E_trace_zero_component"] += weight
                component_atom_pairs["E_trace_zero_component"] += 1
                if detector_numerator != (b - 2 * q) ** 2:
                    raise ArithmeticError("E-zero component square identity drifted")
                if (detector_numerator == 0) != (b == 2 * q):
                    raise ArithmeticError("E-zero rank-drop condition drifted")
                if detector_numerator == 0:
                    component_counts["E_component_rank_drop"] += weight
                    component_atom_pairs["E_component_rank_drop"] += 1
            if c_zero:
                component_counts["C_trace_zero_component"] += weight
                component_atom_pairs["C_trace_zero_component"] += 1
                if detector_numerator != (A * A + b - 2 * q) ** 2:
                    raise ArithmeticError("C-zero component square identity drifted")
                if (detector_numerator == 0) != (A * A + b == 2 * q):
                    raise ArithmeticError("C-zero rank-drop condition drifted")
                if detector_numerator == 0:
                    component_counts["C_component_rank_drop"] += weight
                    component_atom_pairs["C_component_rank_drop"] += 1
            if e_zero and c_zero:
                component_counts["component_intersection"] += weight
                component_atom_pairs["component_intersection"] += 1
                if detector_numerator == 0:
                    component_counts["rank_drop_intersection"] += weight
                    component_atom_pairs["rank_drop_intersection"] += 1

            if detector_numerator == 0:
                buckets["transverse_degenerate_union"].add(
                    weight,
                    v_numerator,
                    h_numerator,
                    detector_numerator,
                    signed_root_numerator,
                )

    expected_product_pairs = int(genus1_row["squarefree_model_count"]) * int(
        balanced_row["member_count"]
    )
    if product_pair_count != expected_product_pairs:
        raise ArithmeticError("histogram convolution lost product-pair mass")
    singular_count = buckets["singular_trace_zero_total"].pair_count
    if singular_count + neither_pair_count != product_pair_count:
        raise ArithmeticError("trace-zero partition lost product-pair mass")
    if (
        buckets["E_trace_zero_only"].pair_count
        + buckets["C_trace_zero_only"].pair_count
        + buckets["both_trace_zero"].pair_count
        != singular_count
    ):
        raise ArithmeticError("exclusive singular strata do not partition the singular mass")
    degenerate_union = buckets["transverse_degenerate_union"].pair_count
    inclusion_exclusion = (
        component_counts["E_component_rank_drop"]
        + component_counts["C_component_rank_drop"]
        - component_counts["rank_drop_intersection"]
    )
    if degenerate_union != inclusion_exclusion:
        raise ArithmeticError("rank-drop component inclusion-exclusion drifted")

    return {
        "q": q,
        "source_histogram_sizes": {
            "genus1_trace_atoms": len(trace_histogram),
            "genus2_joint_a_b_atoms": len(genus2_atoms),
            "cartesian_histogram_atom_pairs": len(trace_histogram) * len(genus2_atoms),
        },
        "product_model_pair_count": product_pair_count,
        "trace_zero_partition_counts": {
            "E_trace_zero_only": buckets["E_trace_zero_only"].pair_count,
            "C_trace_zero_only": buckets["C_trace_zero_only"].pair_count,
            "both_trace_zero": buckets["both_trace_zero"].pair_count,
            "neither_trace_zero": neither_pair_count,
            "singular_trace_zero_total": singular_count,
            "transverse_degenerate_union": degenerate_union,
        },
        "trace_zero_partition_fractions_of_all_product_pairs": {
            name: _fraction(Fraction(count, product_pair_count))
            for name, count in {
                "E_trace_zero_only": buckets["E_trace_zero_only"].pair_count,
                "C_trace_zero_only": buckets["C_trace_zero_only"].pair_count,
                "both_trace_zero": buckets["both_trace_zero"].pair_count,
                "neither_trace_zero": neither_pair_count,
                "singular_trace_zero_total": singular_count,
                "transverse_degenerate_union": degenerate_union,
            }.items()
        },
        "component_incidence_census": {
            name: {
                "pair_count": component_counts[name],
                "source_atom_pair_count": component_atom_pairs[name],
                "pair_fraction_of_all_product_pairs": _fraction(
                    Fraction(component_counts[name], product_pair_count)
                ),
            }
            for name in (
                "E_trace_zero_component",
                "C_trace_zero_component",
                "component_intersection",
                "E_component_rank_drop",
                "C_component_rank_drop",
                "rank_drop_intersection",
            )
        },
        "strata": {
            name: _summarize_bucket(
                bucket,
                q,
                product_pair_count,
                include_complete_distribution=name == "transverse_degenerate_union",
            )
            for name, bucket in buckets.items()
        },
        "exact_replay_checks": {
            "symbolic_member_checks": symbolic_member_checks,
            "trace_zero_integer_square_checks": square_identity_checks,
            "A_conversion": "A=-t_E applied before every histogram pair",
            "no_product_packet_histogram_reuse": True,
        },
    }


def _source_locks(
    genus1: Mapping[str, object],
    balanced: Mapping[str, object],
    product: Mapping[str, object],
) -> dict[str, object]:
    paths = {
        "genus1_fixture": GENUS1_FIXTURE_PATH,
        "genus1_source": GENUS1_SOURCE_PATH,
        "balanced_fixture": BALANCED_FIXTURE_PATH,
        "balanced_source": BALANCED_SOURCE_PATH,
        "product_tensor_fixture": PRODUCT_FIXTURE_PATH,
        "product_tensor_source": PRODUCT_SOURCE_PATH,
        "product_tensor_note": PRODUCT_NOTE_PATH,
        "producer": Path(__file__).resolve(),
        "note": NOTE_PATH,
        "test": TEST_PATH,
    }
    locks: dict[str, object] = {
        name: {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256_lf_normalized": _lf_sha256(path),
        }
        for name, path in paths.items()
    }
    fixture_payloads = {
        "genus1_fixture": genus1["payload_sha256"],
        "balanced_fixture": balanced["payload_sha256"],
        "product_tensor_fixture": product["payload_sha256"],
    }
    for name, payload_sha256 in fixture_payloads.items():
        locks[name]["payload_sha256"] = payload_sha256  # type: ignore[index]
    return locks


def build_fixture(q_values: Sequence[int] = FROZEN_Q_VALUES) -> dict[str, object]:
    if tuple(q_values) != FROZEN_Q_VALUES:
        raise ValueError(f"fixture requires exactly q={FROZEN_Q_VALUES}")
    geometry = symbolic_geometry_certificate()
    genus1 = _load_locked_fixture(GENUS1_FIXTURE_PATH)
    balanced = _load_locked_fixture(BALANCED_FIXTURE_PATH)
    product = _load_locked_fixture(PRODUCT_FIXTURE_PATH)
    _validate_locked_inputs(genus1, balanced, product)

    genus1_by_q = _field_rows_by_q(genus1["finite_regressions"])  # type: ignore[arg-type]
    balanced_by_q = _field_rows_by_q(
        balanced["frozen_enumeration_facts"]["families"]  # type: ignore[index]
    )
    guard = HistogramPairGuard()
    families = [
        analyze_frozen_field(q, genus1_by_q[q], balanced_by_q[q], guard)
        for q in q_values
    ]
    expected_operations = sum(
        row["source_histogram_sizes"]["cartesian_histogram_atom_pairs"]  # type: ignore[index]
        for row in families
    )
    if guard.operations != expected_operations:
        raise ArithmeticError("histogram-pair operation ledger drifted")

    fixture: dict[str, object] = {
        "schema": "riemann.product-tensor-trace-zero-singular-strata.v1",
        "raw_fixture_id": "product-tensor-trace-zero-singular-strata-q3-q5-q7-v1",
        "status": "EXACT_SYMBOLIC_GEOMETRY_AND_LOCKED_HISTOGRAM_CENSUS",
        "rigor_level": {
            "singular_locus": "PROVED_OVER_CHARACTERISTIC_NOT_2_AS_A_REDUCED_AFFINE_LOCUS",
            "transverse_rank_drop": "PROVED_BY_EXACT_QUADRATIC_MATRIX_DETERMINANT",
            "coefficient_map_pullback": "PROVED_BY_EXACT_INTEGER_POLYNOMIAL_IDENTITIES",
            "finite_census": "EXACT_ONLY_FOR_Q_3_5_7_FROM_LOCKED_HISTOGRAMS",
        },
        "normalization_and_source_bridge": {
            "genus1_fixture": "t_E=q+1-#E(F_q), L_E=1-t_E*T+q*T^2",
            "tensor_coefficient": "A=-t_E, P_E=1+A*T+q*T^2",
            "genus2_fixture": "P_C=1+a*T+b*T^2+q*a*T^3+q^2*T^4",
            "coefficient_space": "u=c1/q, v=c2/q^2, w=c3/q^3, h=c4/q^4",
            "trace_zero_meaning": "E trace zero iff A=0; C trace zero iff a=0",
        },
        "symbolic_geometry": geometry,
        "frozen_histogram_census": families,
        "producer_and_source_locks": {
            "input_method": "locked JSON histogram convolution plus exact symbolic algebra",
            "locks": _source_locks(genus1, balanced, product),
        },
        "resource_contract": {
            "strict_histogram_pair_cap": MAX_HISTOGRAM_PAIR_OPERATIONS,
            "histogram_pair_operations": guard.operations,
            "strict_cap_satisfied": guard.operations < MAX_HISTOGRAM_PAIR_OPERATIONS,
            "field_or_curve_enumerations": 0,
            "random_samples": 0,
            "floating_point_arithmetic_or_results": 0,
            "arithmetic": "integers, fractions, and sparse integer polynomials only",
        },
        "scope_firewall": {
            "coefficient_image_only": (
                "This packet studies an ambient hypersurface containing the normalized "
                "coefficient image and the pullback of its singular strata to histogram "
                "parameters; equality with the full coefficient image is not asserted."
            ),
            "no_extra_endomorphism_claim": (
                "Trace-zero or transverse rank drop is not evidence, by itself, of extra "
                "endomorphisms, a correspondence, or enhanced geometric monodromy."
            ),
            "no_singular_product_variety_claim": (
                "A singular point of the ambient coefficient hypersurface does not say that "
                "E, C, or E x C is a singular variety."
            ),
            "no_causal_classification": (
                "The q=3,5,7 census counts coefficient states only; it does not classify "
                "supersingularity, twists, or endomorphism mechanisms."
            ),
            "no_honda_tate_or_isogeny_import": (
                "The two formal P_C factorizations are polynomial identities only in this "
                "packet; no Honda-Tate/Tate theorem is imported and no Jacobian splitting, "
                "isogeny, or extra-endomorphism conclusion is asserted."
            ),
            "no_asymptotic_or_global_claim": (
                "Three frozen finite fields imply no equidistribution theorem, asymptotic "
                "law, number-field transfer, RH statement, or GRH statement."
            ),
        },
    }
    _reject_floats(fixture)
    fixture["payload_sha256"] = _canonical_sha256(fixture)
    return fixture


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--write", type=Path, nargs="?", const=OUTPUT_PATH, default=None
    )
    mode.add_argument(
        "--check", type=Path, nargs="?", const=OUTPUT_PATH, default=None
    )
    args = parser.parse_args()
    fixture = build_fixture()
    encoded = json.dumps(fixture, indent=2, sort_keys=True) + "\n"
    if args.write is not None:
        args.write.write_text(encoded, encoding="utf-8")
        print(f"wrote {args.write}")
    elif args.check is not None:
        if args.check.read_text(encoding="utf-8") != encoded:
            raise SystemExit(f"stale fixture: {args.check}")
        print(f"fixture current: {args.check}")
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
