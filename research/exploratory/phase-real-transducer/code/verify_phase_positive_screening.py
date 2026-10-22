#!/usr/bin/env python3
"""Replay PFR-T10--T11 and PFR-R4 finite algebra and regressions.

The script emits a deterministic JSON result.  Actual-zeta comparisons are
ordinary high-precision reconnaissance and are explicitly not directed proof
certificates.
"""

from __future__ import annotations

import hashlib
import json
import math
import pathlib
import sys
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from phase_positive_screening import (  # noqa: E402
    CriticalPoint,
    finite_hermite_source_resolvent,
    finite_partial_fraction_resolvent,
    green_kernel_order_two,
    mirrored_screening_field,
    partial_fraction_coefficients,
    rectangle_argument_ledger,
    screening_overlap_numeric,
    symmetric_resolvent_energy,
    symmetric_resolvent_response,
    two_point_toeplitz_eigenvalues,
    two_point_hermite_coefficients,
    evaluate_polynomial,
)


def require_mpmath():
    try:
        import mpmath as mp  # type: ignore
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("mpmath is required") from exc
    return mp


def centered_xi_log_derivative(z):
    mp = require_mpmath()
    s = mp.mpf("0.5") + z
    return (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def actual_xi_hermite_regression() -> dict[str, Any]:
    mp = require_mpmath()
    mp.mp.dps = 60
    rate = mp.mpf(2)
    order = 2
    z = mp.mpf("1.2") + mp.mpf("0.7") * 1j

    def derivative(point: complex, degree: int) -> complex:
        value = mp.diff(centered_xi_log_derivative, mp.mpc(point), degree)
        return complex(value)

    coefficients = two_point_hermite_coefficients(float(rate), order, derivative)
    f_value = centered_xi_log_derivative(z)
    interpolation = sum(mp.mpc(coefficients[k]) * z**k for k in range(2 * order))
    source = (f_value - interpolation) / (rate * rate - z * z) ** order

    prefix = mp.mpc(0)
    prefix_count = 30
    for index in range(1, prefix_count + 1):
        gamma = mp.im(mp.zetazero(index))
        for lam in (1j * gamma, -1j * gamma):
            prefix += 1 / ((rate * rate - lam * lam) ** order * (z - lam))

    discrepancy = abs(source - prefix)
    if not discrepancy < mp.mpf("3e-11"):
        raise AssertionError(f"actual-Xi prefix regression failed: {discrepancy}")
    return {
        "name": "actual_xi_safe_hermite_zero_prefix",
        "status": "PASS",
        "arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
        "rate": float(rate),
        "order": order,
        "z": [float(mp.re(z)), float(mp.im(z))],
        "zero_pairs": prefix_count,
        "source": [float(mp.re(source)), float(mp.im(source))],
        "zero_prefix": [float(mp.re(prefix)), float(mp.im(prefix))],
        "discrepancy": float(discrepancy),
    }


def run_checks() -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    # Exact-form finite Hermite remainder identity, replayed numerically.
    zeros = (
        0.2 + 3.0j,
        0.2 - 3.0j,
        -0.2 + 3.0j,
        -0.2 - 3.0j,
    )
    z = 1.4 + 0.6j
    source = finite_hermite_source_resolvent(z, zeros, rate=1.2, order=2)
    direct = finite_partial_fraction_resolvent(z, zeros, rate=1.2, order=2)
    error = abs(source - direct)
    if not error < 1e-11:
        raise AssertionError("finite Hermite identity failed")
    checks.append(
        {
            "name": "finite_two_point_hermite_resolvent",
            "status": "PASS",
            "error": error,
        }
    )

    # Partial-fraction bridge back to the one-sided Gamma ladder.
    rate = 1.7
    order = 4
    point = 0.2 + 0.7j
    coefficients = partial_fraction_coefficients(rate, order)
    reconstructed = sum(
        coefficients[k - 1]
        * ((rate - point) ** (-k) + (rate + point) ** (-k))
        for k in range(1, order + 1)
    )
    target = (rate * rate - point * point) ** (-order)
    pf_error = abs(reconstructed - target)
    if not pf_error < 1e-12:
        raise AssertionError("partial-fraction bridge failed")
    checks.append(
        {
            "name": "symmetric_to_one_sided_partial_fraction_bridge",
            "status": "PASS",
            "error": pf_error,
            "order": order,
        }
    )

    # Synthetic RH-line model: two-point Toeplitz positivity.
    line_zeros = (3.0j, -3.0j, 5.0j, -5.0j)
    s0 = symmetric_resolvent_response(0.0, line_zeros, rate=1.0, order=2).real
    st = symmetric_resolvent_response(1.0, line_zeros, rate=1.0, order=2).real
    low, high = two_point_toeplitz_eigenvalues(s0, st)
    if low < -1e-14:
        raise AssertionError("line-zero Toeplitz model lost positivity")
    checks.append(
        {
            "name": "line_zero_toeplitz_positive",
            "status": "PASS",
            "eigenvalues": [low, high],
        }
    )

    # One off-axis quartet gives a finite 2x2 negative witness.
    quartet = (
        0.2 + 3.0j,
        0.2 - 3.0j,
        -0.2 + 3.0j,
        -0.2 - 3.0j,
    )
    q0 = symmetric_resolvent_response(0.0, quartet, rate=1.0, order=2).real
    qt = symmetric_resolvent_response(0.98, quartet, rate=1.0, order=2).real
    qlow, qhigh = two_point_toeplitz_eigenvalues(q0, qt)
    if not qlow < 0:
        raise AssertionError("off-axis Toeplitz witness was not negative")
    checks.append(
        {
            "name": "off_axis_two_point_toeplitz_witness",
            "status": "PASS",
            "time": 0.98,
            "eigenvalues": [qlow, qhigh],
        }
    )

    # Weighted-energy boundary for the same finite model.
    boundary_rejected = False
    try:
        symmetric_resolvent_energy(0.2, quartet, rate=1.0, order=2)
    except ValueError:
        boundary_rejected = True
    energy = symmetric_resolvent_energy(0.3, quartet, rate=1.0, order=2)
    if not boundary_rejected or not energy > 0:
        raise AssertionError("symmetric energy boundary failed")
    checks.append(
        {
            "name": "symmetric_energy_abscissa",
            "status": "PASS",
            "boundary_rejected": boundary_rejected,
            "energy_at_0.3": energy,
        }
    )

    # m=2 Green kernel: third derivative jump is +1, hence a negative prime
    # atom gives the PFR-T10 jump -Lambda(n)/sqrt(n).
    mp = require_mpmath()
    mp.mp.dps = 50
    a = mp.mpf("1.3")
    g_plus = lambda x: mp.e ** (-a * x) * (1 + a * x) / (4 * a**3)
    g_minus = lambda x: mp.e ** (a * x) * (1 - a * x) / (4 * a**3)
    green_jump = mp.diff(g_plus, 0, 3) - mp.diff(g_minus, 0, 3)
    if not abs(green_jump - 1) < mp.mpf("1e-40"):
        raise AssertionError("order-two Green jump failed")
    n = 8
    prime_jump = -math.log(2.0) / math.sqrt(n) * float(green_jump)
    expected_jump = -math.log(2.0) / math.sqrt(n)
    checks.append(
        {
            "name": "symmetric_prime_knot_jump_m2",
            "status": "PASS",
            "green_jump": float(green_jump),
            "n": n,
            "jump": prime_jump,
            "expected": expected_jump,
        }
    )

    # Harmonic screening identity.
    points = (
        CriticalPoint(-0.4, -1.0),
        CriticalPoint(-0.2, 1.5),
        CriticalPoint(0.3, -0.2),
    )
    positive, overlap, negative, n_left, n_right = screening_overlap_numeric(
        0.0,
        points,
        cutoff=500.0,
        panels=100_000,
    )
    positive_error = abs(positive - (math.pi * n_left - overlap))
    negative_error = abs(negative - (math.pi * n_right - overlap))
    if positive_error > 5e-3 or negative_error > 5e-3:
        raise AssertionError("Poisson screening regression failed")
    checks.append(
        {
            "name": "finite_poisson_screening",
            "status": "PASS",
            "n_left": n_left,
            "n_right": n_right,
            "positive_mass": positive,
            "negative_mass": negative,
            "overlap": overlap,
            "positive_error": positive_error,
            "negative_error": negative_error,
        }
    )

    # Exact mirror-screening firewall.
    mirror_values = [
        mirrored_screening_field(
            t,
            observation_sigma=0.0,
            distance=0.4,
            ordinate=1.2,
        )
        for t in (-10.0, -1.0, 0.0, 2.5, 11.0)
    ]
    if max(abs(value) for value in mirror_values) > 1e-14:
        raise AssertionError("mirror screening did not cancel")
    checks.append(
        {
            "name": "mirrored_speiser_screening_firewall",
            "status": "PASS",
            "max_abs_field": max(abs(value) for value in mirror_values),
        }
    )

    # Finite Gauss/argument-principle rectangle.
    rectangle_zeros = (
        0.1 + 0.3j,
        0.3 + 1.2j,
        0.7 + 0.5j,
        -0.5 + 0.4j,
    )
    change, count = rectangle_argument_ledger(
        rectangle_zeros,
        sigma_left=-0.2,
        sigma_right=0.5,
        t_bottom=-0.5,
        t_top=1.8,
        quadrature_steps=20_000,
    )
    ledger_error = abs(change - 2.0 * math.pi * count)
    if count != 2 or ledger_error > 2e-7:
        raise AssertionError("rectangle Gauss ledger failed")
    checks.append(
        {
            "name": "finite_rectangle_gauss_ledger",
            "status": "PASS",
            "count": count,
            "boundary_change": change,
            "error": ledger_error,
        }
    )

    checks.append(actual_xi_hermite_regression())
    return checks


def main() -> None:
    checks = run_checks()
    payload: dict[str, Any] = {
        "schema": "riemann.phase-positive-screening.v1",
        "status": "PASS_PFR_SYMMETRIC_POSITIVITY_AND_SPEISER_SCREENING",
        "check_count": len(checks),
        "checks": checks,
        "scope": {
            "exact_finite_algebra": True,
            "analytic_manuscript_machine_proved": False,
            "actual_zeta_regressions": "NON_DIRECTED_HIGH_PRECISION",
            "directed_rounding": False,
            "external_novelty_certified": False,
        },
        "rh_status": "UNPROVEN",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["proof_object"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()

    output = ROOT / "results" / "verification_108420.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(payload["status"])
    print(f"checks={payload['check_count']}")
    print(f"proof_object={payload['proof_object']}")
    print("RH_UNPROVEN")


if __name__ == "__main__":
    main()
