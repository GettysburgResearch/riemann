#!/usr/bin/env python3
"""Exact bounded controls for the analytic confluent source-band theorem."""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NOTE = HERE / "XI_CONFLUENT_SOURCE_BAND_OBSTRUCTION.md"
MANIFEST = HERE / "xi_confluent_source_band_obstruction.sources.json"
FIXTURE = HERE / "xi_confluent_source_band_obstruction.json"
TEST = ROOT / "tests/test_xi_confluent_source_band_obstruction.py"
BASE = "f3d074190e64a97ac935b93c5b628568cde90858"
MAX_Q, MAX_LAGUERRE, MAX_MATRIX = 8, 8, 4
MAX_POLY_COEFFICIENTS, MAX_INPUT_BITS, MAX_K = 20, 128, 15
SOURCE_ROWS = (
    (
        "frozen_gauge",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106620-mesoscopic-frozen-riemann-siegel-gauge.md",
        "7fbf3731f286ddfc9eb1d10ede5941ab2156817a",
        "23e368f246606b0a8b4f53bec9e65e1dec21bdd207197387461268b4ca1bb7d0",
    ),
    (
        "source_Pick_and_confluent_jets",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106671-endpoint-free-energy-is-a-source-evaluation-pick-determinant.md",
        "d0488eccf2507bcb71c7e46f3f6f9c7013dd3998",
        "fc9bc89d9129ca22a9ededed2e3a6daf78c1371c9582d023487c326309d42764",
    ),
    (
        "Hardy_Laplace_normalization",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106673-unregularized-cauchy-volume-is-logarithmic-laplace-transport.md",
        "cadbbee0c5864d4cdb9b110bc0ddc0938e0bcb54",
        "f7d68d9e64c2fb31da6db72bcd93971630cac2273fcb789052baa0679ad36b20",
    ),
    (
        "value_nonnormality_boundary",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/lemmas/L-106650-truncated-toeplitz-value-nonnormality-split.md",
        "8e80ee4e7460618807e8a041197ec6a63137672c",
        "178dd723a0e255bc897145a9459e03b685f6f03e75fa463aa2d42c8b7472dfe2",
    ),
    (
        "physical_free_energy_target",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106670-regularized-pick-free-energy-ninety-percent-equivalence.md",
        "9a61689c19b244f0176f753cef146b252256eab0",
        "b96ffe1ec8e5fc7d825e521c57c956066e25f0494e80aa4c13d4017ea98c8ae7",
    ),
    (
        "open_Xi_transfer",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/theorems/T-106710-xi-carrier-adapted-source-softening-frontier.md",
        "b06d973198898a93d584b67dbe26ce24823e2ffc",
        "1a1f27c31dccd2a3393675acfc444e712a1449b476a2e1d7812f0e4c5559eb9f",
    ),
    (
        "source_softening_firewall",
        "81d52e569cc8bb566e54043fd692fd6157406aab",
        "claims/refutations/R-106710-diagonal-source-softening-does-not-control-topological-free-energy.md",
        "e17fdf16e87d6791c64fbb6f0ac8f604ca46c396",
        "889fd0cf65cefcf83705e54d0dda5525880fc94c4542ca0be6fa40724e1107c1",
    ),
    (
        "reviewed_actual_Xi_concentration",
        "3b6972320899a82c6caa3a98e2ada5ff703a605a",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION.md",
        "fa24f9c8e0a87709d1a297a4e72136c1135d066c",
        "f7f89abe2e54d0d8df72dc830162b2083bc4f05d402c3aa70eca464678e80246",
    ),
    (
        "independent_concentration_review",
        "f3d074190e64a97ac935b93c5b628568cde90858",
        "research/exploratory/XI_ACTUAL_KERNEL_LAPLACE_CONCENTRATION_AUDIT.md",
        "da9032e15eb7be89557a54120b74fc9596c527d9",
        "aaf60c26b34296aa2e23bdad1469fce8ed3efe5ec27063d14d666f3fa5ce0536",
    ),
    (
        "earlier_single_kernel_scout",
        "939a24962a4c6a449c0b56e3b20f78b936f35f6c",
        "research/exploratory/XI_NEAR_ADAPTED_SCALE_FIREWALL.md",
        "0461a5c159d9d1094a9849e362d02ac1149a0143",
        "b770dc30ee6ab5406e159230c6ea617a1e5b1616b818dabb4c4c7f37f4408eac",
    ),
)
EXTERNAL_FORMULAS = (
    (
        "https://dlmf.nist.gov/18.3",
        "integral_0^infinity exp(-x)*L_j(x)*L_k(x) dx=delta_jk",
    ),
    ("https://dlmf.nist.gov/18.9.T2", "x*L_j=(2*j+1)*L_j-(j+1)*L_(j+1)-j*L_(j-1)"),
    ("https://dlmf.nist.gov/18.8", "x*L_j''+(1-x)*L_j'+j*L_j=0"),
)


def canonical(data: object) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), allow_nan=False)


def sha256_lf(raw: bytes) -> str:
    return hashlib.sha256(raw.replace(b"\r\n", b"\n")).hexdigest()


def read_json(path: Path) -> object:
    def pairs(items: list) -> dict:
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out

    def constant(value: str) -> None:
        raise ValueError(f"nonfinite JSON constant: {value}")

    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=pairs,
        parse_constant=constant,
    )


def exact(value: int | Fraction) -> Fraction:
    if type(value) not in (int, Fraction):
        raise TypeError("exact int/Fraction required; bool and float rejected")
    value = Fraction(value)
    if (
        max(value.numerator.bit_length(), value.denominator.bit_length())
        > MAX_INPUT_BITS
    ):
        raise ValueError("rational input exceeds bit cap")
    return value


def integer(value: int, low: int, high: int) -> int:
    if type(value) is not int or not low <= value <= high:
        raise ValueError(f"integer required in [{low},{high}]")
    return value


def polynomial(values: tuple | list) -> tuple[Fraction, ...]:
    if type(values) not in (tuple, list):
        raise TypeError("polynomial must be a list or tuple")
    if not 1 <= len(values) <= MAX_POLY_COEFFICIENTS:
        raise ValueError("polynomial length exceeds cap or is empty")
    # Validate every raw coefficient BEFORE trimming: trailing False/0.0 is invalid.
    out = [exact(value) for value in values]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def p_add(left: tuple, right: tuple) -> tuple:
    left, right = polynomial(left), polynomial(right)
    return polynomial(
        tuple(
            (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
            for i in range(max(len(left), len(right)))
        )
    )


def p_scale(poly: tuple, scalar: int | Fraction) -> tuple:
    poly, scalar = polynomial(poly), exact(scalar)
    return polynomial(tuple(scalar * value for value in poly))


def p_mul(left: tuple, right: tuple) -> tuple:
    left, right = polynomial(left), polynomial(right)
    size = len(left) + len(right) - 1
    if size > MAX_POLY_COEFFICIENTS:
        raise ValueError("polynomial product exceeds degree cap")
    out = [Fraction(0)] * size
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return polynomial(out)


def derivative(poly: tuple) -> tuple:
    poly = polynomial(poly)
    return polynomial(tuple(i * poly[i] for i in range(1, len(poly))) or (0,))


def exp_integral(poly: tuple) -> Fraction:
    """Integral_0^infinity exp(-x)*poly(x) dx, by exact factorial moments."""
    return sum(
        (value * math.factorial(i) for i, value in enumerate(polynomial(poly))),
        Fraction(0),
    )


def laguerre(order: int) -> tuple:
    order = integer(order, 0, MAX_LAGUERRE)
    return tuple(
        Fraction((-1) ** i * math.comb(order, i), math.factorial(i))
        for i in range(order + 1)
    )


def laguerre_control(order: int) -> dict:
    order = integer(order, 0, MAX_LAGUERRE - 1)
    poly = laguerre(order)
    dpoly = derivative(poly)
    ode = p_add(
        p_add(p_mul((0, 1), derivative(dpoly)), p_mul((1, -1), dpoly)),
        p_scale(poly, order),
    )
    recurrence = p_add(
        p_add(p_scale(poly, 2 * order + 1), p_scale(laguerre(order + 1), -order - 1)),
        p_scale(laguerre(order - 1), -order) if order else (0,),
    )
    if ode != (0,) or recurrence != p_mul((0, 1), poly):
        raise ArithmeticError("Laguerre coefficient identity failed")
    square = p_mul(poly, poly)
    dphi_poly = p_add(dpoly, p_scale(poly, Fraction(-1, 2)))
    norm = exp_integral(square)
    first_moment = exp_integral(p_mul((0, 1), square))
    energy = exp_integral(p_mul((0, 1), p_mul(dphi_poly, dphi_poly)))
    if (norm, first_moment, energy) != (1, 2 * order + 1, Fraction(2 * order + 1, 4)):
        raise ArithmeticError("Laguerre moment/energy identity failed")
    return {
        "j": order,
        "polynomial": poly,
        "norm_squared": norm,
        "first_moment": first_moment,
        "derivative_energy": energy,
        "pointwise_x_phi_squared_bound_from_proof": 2 * order + 1,
    }


def multiplicity_control(q: int) -> dict:
    q = integer(q, 1, MAX_Q)
    odd_sum = sum(2 * j + 1 for j in range(q))
    if odd_sum != q * q:
        raise ArithmeticError("multiplicity constant failed")
    return {
        "q": q,
        "sum_of_odd_constants": odd_sum,
        "trace_dimension_cap": q,
        "unit_vector_cap": 1,
        "log_width_coefficient": q * q,
    }


def matrix(values: tuple | list) -> tuple:
    if type(values) not in (tuple, list):
        raise TypeError("matrix must be a list or tuple")
    q = integer(len(values), 1, MAX_MATRIX)
    if any(type(row) not in (tuple, list) or len(row) != q for row in values):
        raise ValueError("matrix must be nonempty square within cap")
    return tuple(tuple(exact(value) for value in row) for row in values)


def identity(q: int) -> tuple:
    q = integer(q, 1, MAX_MATRIX)
    return tuple(tuple(Fraction(i == j) for j in range(q)) for i in range(q))


def m_add(left: tuple, right: tuple) -> tuple:
    left, right = matrix(left), matrix(right)
    if len(left) != len(right):
        raise ValueError("matrix dimensions differ")
    return tuple(tuple(a + b for a, b in zip(r, s)) for r, s in zip(left, right))


def m_scale(mat: tuple, scalar: int | Fraction) -> tuple:
    mat, scalar = matrix(mat), exact(scalar)
    return tuple(tuple(value * scalar for value in row) for row in mat)


def m_mul(left: tuple, right: tuple) -> tuple:
    left, right = matrix(left), matrix(right)
    if len(left) != len(right):
        raise ValueError("matrix dimensions differ")
    q = len(left)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(q)) for j in range(q))
        for i in range(q)
    )


def transpose(mat: tuple) -> tuple:
    return tuple(zip(*matrix(mat)))


def trace(mat: tuple) -> Fraction:
    mat = matrix(mat)
    return sum((mat[i][i] for i in range(len(mat))), Fraction(0))


def inverse(mat: tuple) -> tuple:
    mat = matrix(mat)
    q = len(mat)
    out = [list(row) + list(unit) for row, unit in zip(mat, identity(q))]
    for k in range(q):
        pivot = next((i for i in range(k, q) if out[i][k]), None)
        if pivot is None:
            raise ValueError("singular matrix")
        out[k], out[pivot] = out[pivot], out[k]
        denominator = out[k][k]
        out[k] = [value / denominator for value in out[k]]
        for i in range(q):
            if i != k:
                factor = out[i][k]
                out[i] = [a - factor * b for a, b in zip(out[i], out[k])]
    return matrix(tuple(tuple(row[q:]) for row in out))


def determinant(mat: tuple) -> Fraction:
    mat = matrix(mat)
    q = len(mat)
    total = Fraction(0)
    for perm in itertools.permutations(range(q)):
        inversions = sum(perm[i] > perm[j] for i in range(q) for j in range(i + 1, q))
        total += (-1) ** inversions * math.prod(mat[i][perm[i]] for i in range(q))
    return total


def principal_minors(mat: tuple) -> tuple:
    mat = matrix(mat)
    if mat != transpose(mat):
        raise ValueError("real symmetric matrix required")
    q = len(mat)
    return tuple(
        determinant(tuple(tuple(mat[i][j] for j in indices) for i in indices))
        for size in range(1, q + 1)
        for indices in itertools.combinations(range(q), size)
    )


def characteristic_coefficients(mat: tuple) -> tuple:
    """Coefficients of det(I-z*mat), via all principal minors (not eigenvalues)."""
    mat = matrix(mat)
    q = len(mat)
    return (Fraction(1),) + tuple(
        (-1) ** size
        * sum(
            determinant(tuple(tuple(mat[i][j] for j in indices) for i in indices))
            for indices in itertools.combinations(range(q), size)
        )
        for size in range(1, q + 1)
    )


def congruence(mat: tuple, change: tuple) -> tuple:
    return m_mul(m_mul(transpose(change), mat), change)


def source_trace(metric: tuple, jet: tuple, band: tuple) -> Fraction:
    return trace(m_mul(inverse(metric), congruence(band, jet)))


def model_matrices(q: int) -> tuple:
    q = integer(q, 1, MAX_MATRIX)
    gram = tuple(
        tuple(
            Fraction(
                math.factorial(i + j),
                math.factorial(i) * math.factorial(j) * 2 ** (i + j + 1),
            )
            for j in range(q)
        )
        for i in range(q)
    )
    tail = tuple(
        tuple(
            gram[i][j]
            * sum(Fraction(2**k, math.factorial(k)) for k in range(i + j + 1))
            for j in range(q)
        )
        for i in range(q)
    )
    outer = tuple(
        tuple(
            Fraction(4, 2 ** (j - i + 1)) if j >= i else Fraction(0) for j in range(q)
        )
        for i in range(q)
    )
    inner = tuple(
        tuple(
            Fraction(1, 3)
            if i == j
            else -(Fraction(2, 3) ** (j - i + 1))
            if j > i
            else Fraction(0)
            for j in range(q)
        )
        for i in range(q)
    )
    return gram, tail, outer, inner


def metric_control(q: int) -> dict:
    q = integer(q, 2, MAX_MATRIX)
    gram, tail, outer, inner = model_matrices(q)
    if m_mul(outer, inner) != m_mul(inner, outer):
        raise ArithmeticError("multiplication jets must commute")
    noncommutation = {
        name: m_mul(jet, weight) != m_mul(weight, jet)
        for name, jet, weight in (
            ("outer_with_G", outer, gram),
            ("outer_with_H", outer, tail),
            ("inner_with_G", inner, gram),
            ("inner_with_H", inner, tail),
        )
    }
    if not all(noncommutation.values()):
        raise ArithmeticError("control must not accidentally diagonalize its metric")
    gram_o, tail_o = congruence(gram, outer), congruence(tail, outer)
    source = m_mul(outer, inner)
    defect = congruence(gram, inner)
    favorable = m_add(gram, m_scale(defect, -1))
    if min(principal_minors(gram)) <= 0 or min(principal_minors(favorable)) < 0:
        raise ArithmeticError("native Hardy control lost positivity")
    tau = Fraction(1, 2)
    det_native = determinant(m_add(gram, m_scale(defect, -tau))) / determinant(gram)
    det_outer = determinant(
        m_add(gram_o, m_scale(congruence(gram, source), -tau))
    ) / determinant(gram_o)
    if det_native != det_outer:
        raise ArithmeticError("outer-retaining determinant covariance failed")
    source_band = tuple(source_trace(gram, inner, item) for item in (gram, tail))
    outer_band = tuple(source_trace(gram_o, source, item) for item in (gram, tail))
    if source_band != outer_band:
        raise ArithmeticError("source band coefficients failed covariance")
    localization = m_mul(inverse(gram), tail)
    localization_o = m_mul(inverse(gram_o), tail_o)
    char = characteristic_coefficients(localization)
    char_o = characteristic_coefficients(localization_o)
    if char != char_o:
        raise ArithmeticError("generalized localization spectra differ")
    if localization_o != m_mul(m_mul(inverse(outer), localization), outer):
        raise ArithmeticError("exact similarity, not just characteristic data, failed")
    native_charge = source_band[0]
    naive_charge = source_trace(gram, source, gram)
    native_band_trace = (Fraction(q), trace(localization))
    dropped_band_trace = (
        trace(m_mul(inverse(gram), gram_o)),
        trace(m_mul(inverse(gram), tail_o)),
    )
    if native_charge == naive_charge or native_band_trace == dropped_band_trace:
        raise ArithmeticError("dropping outer metric must change the control")
    return {
        "q": q,
        "basis": "xi^j*exp(-xi)/j!, 0<=j<q",
        "G": gram,
        "H_in_G_I_equals_G_minus_exp_minus_two_H": tail,
        "C_outer_jet": outer,
        "V_inner_jet": inner,
        "J_R": source,
        "G_O": gram_o,
        "CV_equals_VC": True,
        "noncommuting_pairs": noncommutation,
        "tau": tau,
        "regularized_determinant_native_and_outer": det_native,
        "source_band_coefficients_constant_and_minus_exp_minus_two": source_band,
        "generalized_band_characteristic_coefficients_det_I_minus_z_GinvH": char,
        "native_band_trace_constant_and_minus_exp_minus_two": native_band_trace,
        "incorrect_dropped_outer_band_trace": dropped_band_trace,
        "native_total_charge": native_charge,
        "incorrect_outer_dropped_charge": naive_charge,
        "G_positive_and_inner_Pick_semidefinite_exact_minors": True,
    }


def inner_noncommutator(a: int | Fraction, b: int | Fraction) -> dict:
    a, b = exact(a), exact(b)
    if not 0 <= a < b:
        raise ValueError("band requires 0<=A<B")
    # For s>B, Pi_I B f=0 and B Pi_I f=-2 exp(-s) integral_A^B du.
    width = b - a
    coefficient = 2 * width
    return {
        "A": a,
        "B": b,
        "tail_commutator_coefficient_of_exp_minus_s": coefficient,
        "squared_tail_norm_coefficient": coefficient * coefficient / 2,
        "squared_tail_norm_exponent": -2 * b,
        "tail_norm_is_strictly_positive_by_proof": True,
        "physical_inner": "(t-i)/(t+i)",
        "test_function": "exp(-xi)",
    }


def envelope_constants(order: int, tolerance: int | Fraction) -> dict:
    order = integer(order, 1, MAX_K)
    if order % 2 == 0:
        raise ValueError("fixed odd order required")
    tolerance = exact(tolerance)
    if tolerance <= 0:
        raise ValueError("positive fixed tolerance required for width asymptotic")
    center = Fraction(1, 4)
    radius = order * tolerance / 2
    # Each endpoint is this exact coefficient / pi; no floating pi.
    low, high = center - radius, center + radius
    p = Fraction(1, 2 * order)
    if p - 2 * low / order != tolerance or p - 2 * high / order != -tolerance:
        raise ArithmeticError("fixed-scale endpoint constants failed")
    return {
        "K": order,
        "M": tolerance,
        "p_limit": p,
        "pi_times_center_shift_coefficient": center,
        "pi_times_lower_shift_coefficient": low,
        "pi_times_upper_shift_coefficient": high,
        "pi_times_log_width_coefficient": high - low,
        "accepted_set_is_only_enclosed_not_asserted_interval": True,
    }


def expected_manifest() -> dict:
    return {
        "schema": "xi-confluent-source-band-sources-v1",
        "authoring_base": BASE,
        "native_object": "one confluent denominator cluster; literal common-outer source jets and Gram",
        "source_concentration": "reviewed fixed-positive-odd-K actual Xi theorem; not growing K",
        "sources": [
            {
                "role": role,
                "commit": commit,
                "path": path,
                "git_blob": blob,
                "sha256_lf": digest,
            }
            for role, commit, path, blob, digest in SOURCE_ROWS
        ],
        "external_formulas": [
            {
                "url": url,
                "formula": formula,
                "remote_content_machine_authenticated": False,
            }
            for url, formula in EXTERNAL_FORMULAS
        ],
    }


def authenticate_sources(manifest: object | None = None) -> dict:
    if manifest is None:
        manifest = read_json(MANIFEST)
    if canonical(manifest) != canonical(expected_manifest()):
        raise ValueError("manifest differs from complete typed source contract")
    for _, commit, path, blob, digest in SOURCE_ROWS:
        ref = f"{commit}:{path}"
        actual = (
            subprocess.check_output(["git", "rev-parse", ref], cwd=ROOT, timeout=15)
            .decode()
            .strip()
        )
        raw = subprocess.check_output(["git", "show", ref], cwd=ROOT, timeout=15)
        if actual != blob or sha256_lf(raw) != digest:
            raise ValueError("frozen source blob or LF content digest mismatch")
    return {
        "source_count": len(SOURCE_ROWS),
        "manifest_sha256_canonical_json": hashlib.sha256(
            canonical(manifest).encode()
        ).hexdigest(),
        "remote_pages_authenticated": False,
        "source_text_authenticated_not_formally_proved": True,
    }


def serialized(data: object) -> object:
    if isinstance(data, Fraction):
        return str(data)
    if isinstance(data, dict):
        return {key: serialized(value) for key, value in data.items()}
    if isinstance(data, (tuple, list)):
        return [serialized(value) for value in data]
    return data


def build_report() -> dict:
    authentication = authenticate_sources()
    if any(
        isinstance(node, ast.Assert)
        for node in ast.walk(ast.parse(Path(__file__).read_text(encoding="utf-8")))
    ):
        raise ValueError("result-bearing assertions must survive Python -O")
    orthogonality = []
    for j in range(MAX_Q):
        for k in range(MAX_Q):
            value = exp_integral(p_mul(laguerre(j), laguerre(k)))
            if value != int(j == k):
                raise ArithmeticError("cross-orthogonality failed")
            orthogonality.append({"j": j, "k": k, "integral": value})
    return serialized(
        {
            "schema": "xi-confluent-source-band-v1",
            "status": "ANALYTIC_PROOF_IN_NOTE_WITH_EXACT_BOUNDED_CONTROLS",
            "arithmetic_class": "EXACT_RATIONAL",
            "arithmetic_domain": "integer/rational polynomials, factorial integrals and real rational matrices; pi and exponentials are symbolic labels",
            "rounding_contract": "no rounded transcendental evaluation, quadrature, numerical eigenvalues or Xi samples",
            "source_authentication": authentication,
            "artifact_sha256_lf": {
                path.relative_to(ROOT).as_posix(): sha256_lf(path.read_bytes())
                for path in (NOTE, Path(__file__), TEST, MANIFEST)
            },
            "caps": {
                "q_panel_max": MAX_Q,
                "Laguerre_public_max": MAX_LAGUERRE,
                "matrix_size_max": MAX_MATRIX,
                "polynomial_coefficient_max": MAX_POLY_COEFFICIENTS,
                "rational_input_bits": MAX_INPUT_BITS,
                "odd_K_max": MAX_K,
            },
            "coverage": {
                "cross_orthogonality_cells": MAX_Q**2,
                "Laguerre_energy_rows": MAX_Q,
                "multiplicity_rows": MAX_Q,
                "native_matrix_rows": 2,
                "phase_constant_rows": 24,
                "search_or_asymptotic_fitting": False,
            },
            "Laguerre_cross_orthogonality": orthogonality,
            "Laguerre_rows": [laguerre_control(j) for j in range(MAX_Q)],
            "multiplicity_rows": [multiplicity_control(q) for q in range(1, MAX_Q + 1)],
            "native_metric_controls": [metric_control(q) for q in (2, 3)],
            "physical_inner_noncommutator": inner_noncommutator(1, 2),
            "fixed_order_envelope_constants": [
                envelope_constants(k, m)
                for k in range(1, MAX_K + 1, 2)
                for m in (Fraction(1, 2), Fraction(1), Fraction(2))
            ],
            "scope": {
                "one_confluent_cluster": True,
                "analytic_bound_all_positive_integer_q": True,
                "growing_q_o_X_exp_X_over_2_permitted": True,
                "actual_Xi_accepted_set_envelope_only": True,
                "fixed_K_and_M": True,
                "literal_source_J_R_coefficients_not_free": True,
                "common_outer_jet_metric_retained": True,
                "arbitrary_distinct_node_clusters": False,
                "physical_inner_weighted_band_Gram_controlled": False,
                "outer_or_inner_commuted_with_projection": False,
                "unbounded_q_uniform_localization_obstruction": False,
                "abstract_density_implies_actual_Xi_multiplicity": False,
                "analytic_proof_formally_machine_verified": False,
                "Pick_free_energy_bound": False,
                "topological_index_removed": False,
                "ninety_percent_density_one_or_RH": False,
                "novelty_claim": False,
                "floating_point_Xi_samples": 0,
            },
        }
    )


def validate_report(report: object) -> None:
    if canonical(report) != canonical(build_report()):
        raise ValueError(
            "artifact differs from complete source-authenticated typed rebuild"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--emit-report", action="store_true")
    mode.add_argument("--emit-manifest", action="store_true")
    args = parser.parse_args()
    if args.emit_manifest:
        print(json.dumps(expected_manifest(), indent=2, sort_keys=True))
    elif args.emit_report:
        print(json.dumps(build_report(), indent=2, sort_keys=True))
    else:
        validate_report(read_json(FIXTURE))
        print(
            "Xi confluent source band: source locks/exact controls PASS; physical inner/Pick/RH OPEN"
        )


if __name__ == "__main__":
    main()
