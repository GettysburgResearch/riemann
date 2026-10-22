#!/usr/bin/env python3
"""Bounded replay for PFR-T7--T9.

Arithmetic class:
  * exact closed formulas for finite algebra;
  * NON_DIRECTED_HIGH_PRECISION for actual-zeta regressions.

The replay does not machine-prove the analytic manuscript or RH.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import sys

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from phase_speiser_localization import (  # noqa: E402
    complex_source_resolvent_truncation,
    complex_zero_prefix_resolvent,
    critical_point_field_integral,
    critical_point_poisson_field,
    critical_point_signed_index,
    finite_horizon_leakage_bound,
    finite_resolvent_energy,
    hardy_curvature_from_complex_derivatives,
    normalized_gamma_weight,
    prime_knot_jump,
    soft_band_scales,
    tangent_phase_acceleration,
)


def assert_close(actual, expected, tolerance: float, label: str) -> None:
    if abs(actual - expected) > tolerance:
        raise AssertionError(
            f"{label}: |{actual!r}-{expected!r}|>{tolerance!r}"
        )


def trapezoid_energy(values: list[complex], step: float) -> float:
    if len(values) < 2:
        return 0.0
    total = 0.5 * abs(values[0]) ** 2 + 0.5 * abs(values[-1]) ** 2
    total += sum(abs(value) ** 2 for value in values[1:-1])
    return step * total


def main() -> None:
    mp.mp.dps = 45
    checks: list[dict[str, object]] = []

    # 1. Universal prime-knot jump, including independence from a.
    n = 8
    mangoldt = math.log(2.0)
    jump_m2 = prime_knot_jump(2, mangoldt, n)
    expected_jump = -mangoldt / math.sqrt(n)
    assert_close(jump_m2, expected_jump, 1e-15, "prime-knot jump")
    checks.append(
        {
            "name": "prime_knot_jump",
            "m": 2,
            "n": n,
            "jump": jump_m2,
            "status": "PASS",
        }
    )

    # 2. Actual-zeta curvature bridge at one ordinary point.
    t = mp.mpf("20")
    s = mp.mpf("0.5") + 1j * t
    theta1 = mp.diff(mp.siegeltheta, t)
    theta2 = mp.diff(mp.siegeltheta, t, 2)
    z = mp.siegelz(t)
    z1 = mp.diff(mp.siegelz, t)
    z2 = mp.diff(mp.siegelz, t, 2)
    d_h_real = theta1**2 * z**2 + z1**2
    c_h_real = (
        theta1**2 * z**2
        + 2 * z1**2
        - z * z2
        + (theta2 / theta1) * z * z1
    )
    zp = mp.diff(mp.zeta, s)
    zpp = mp.diff(mp.zeta, s, 2)
    d_h_complex, c_h_complex = hardy_curvature_from_complex_derivatives(
        float(theta1),
        complex(zp),
        complex(zpp),
    )
    assert_close(d_h_complex, float(d_h_real), 2e-12, "D_H bridge")
    assert_close(c_h_complex, float(c_h_real), 2e-12, "C_H bridge")
    acceleration = tangent_phase_acceleration(complex(zp), complex(zpp))
    assert_close(
        acceleration,
        float(-theta1 * c_h_real / d_h_real),
        2e-12,
        "phase acceleration",
    )
    checks.append(
        {
            "name": "hardy_curvature_zeta_prime_bridge",
            "t": float(t),
            "D_H": d_h_complex,
            "C_H": c_h_complex,
            "phase_acceleration": acceleration,
            "arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
            "status": "PASS",
        }
    )

    # 3. Finite critical-point Poisson index.
    critical_points = (
        complex(-1.0, -2.0),
        complex(-0.5, 3.0),
        complex(1.5, -1.0),
    )
    sigma0 = 0.0
    signed_index = critical_point_signed_index(sigma0, critical_points)
    if signed_index != 1:
        raise AssertionError(f"unexpected signed index {signed_index}")
    analytic_integral = critical_point_field_integral(sigma0, critical_points)
    assert_close(analytic_integral, math.pi, 1e-15, "Poisson index integral")
    # A wide finite quadrature checks the sign/normalization independently.
    bound = 250.0
    pieces = 200_000
    step = 2.0 * bound / pieces
    numerical_integral = 0.0
    for idx in range(pieces + 1):
        x = -bound + idx * step
        weight = 0.5 if idx in (0, pieces) else 1.0
        numerical_integral += weight * critical_point_poisson_field(
            x, sigma0, critical_points
        )
    numerical_integral *= step
    if abs(numerical_integral - analytic_integral) > 0.03:
        raise AssertionError("finite Poisson quadrature missed the signed index")
    checks.append(
        {
            "name": "critical_point_poisson_index",
            "signed_index": signed_index,
            "analytic_integral": analytic_integral,
            "truncated_integral": numerical_integral,
            "status": "PASS",
        }
    )

    # 4. Soft-band coefficient separation.
    a = 1.0
    center = 30.0
    w = 0.5
    W = 3.0
    order = 8
    d_in, d_out, eta = soft_band_scales(a, w, W)
    inside = normalized_gamma_weight(
        complex(0.49, center + w),
        a=a,
        center=center,
        m=order,
        d_in=d_in,
    )
    outside = normalized_gamma_weight(
        complex(-0.49, center + W),
        a=a,
        center=center,
        m=order,
        d_in=d_in,
    )
    if abs(inside) < 1.0 - 1e-12:
        raise AssertionError("inside mode was not retained")
    if abs(outside) > eta**order * (1.0 + 1e-12):
        raise AssertionError("outside mode exceeded the guard bound")
    checks.append(
        {
            "name": "soft_band_separation",
            "D_in": d_in,
            "D_out": d_out,
            "eta": eta,
            "order": order,
            "inside_magnitude": abs(inside),
            "outside_magnitude": abs(outside),
            "status": "PASS",
        }
    )

    # 5. Finite-horizon leakage bound on a synthetic exterior packet.
    lambdas = (
        complex(0.35, center + 4.0),
        complex(-0.1, center - 5.0),
        complex(0.2, center + 7.0),
    )
    weights = [
        normalized_gamma_weight(
            lam,
            a=a,
            center=center,
            m=order,
            d_in=d_in,
        )
        for lam in lambdas
    ]
    coefficient_mass = sum(abs(weight) for weight in weights)
    horizon = 4.0
    sigma = 0.1
    samples = 20_000
    dt = horizon / samples
    signal: list[complex] = []
    for idx in range(samples + 1):
        time = idx * dt
        value = sum(
            weight * mp.exp(lam * time)
            for weight, lam in zip(weights, lambdas, strict=True)
        )
        signal.append(complex(mp.exp(-sigma * time) * value))
    measured_norm = math.sqrt(trapezoid_energy(signal, dt))
    bound_norm = finite_horizon_leakage_bound(
        coefficient_mass,
        sigma=sigma,
        horizon=horizon,
    )
    if measured_norm > bound_norm * (1.0 + 1e-8):
        raise AssertionError("finite-horizon leakage bound failed")
    checks.append(
        {
            "name": "finite_horizon_leakage",
            "coefficient_mass": coefficient_mass,
            "measured_norm": measured_norm,
            "bound": bound_norm,
            "status": "PASS",
        }
    )

    # 6. Complex source / zero-prefix regression near the first zero ordinate.
    q = complex(2.0, 14.0)
    source = complex_source_resolvent_truncation(
        0.5,
        q=q,
        m=3,
        prime_limit=1_000_000,
    )
    zero_prefix = complex_zero_prefix_resolvent(0.5, q=q, m=3)
    discrepancy = abs(source - zero_prefix)
    if discrepancy > 1e-5:
        raise AssertionError(
            f"complex source/zero-prefix discrepancy too large: {discrepancy}"
        )
    checks.append(
        {
            "name": "complex_gamma_source_zero_prefix",
            "q": [q.real, q.imag],
            "m": 3,
            "t": 0.5,
            "prime_limit": 1_000_000,
            "source": [source.real, source.imag],
            "zero_prefix": [zero_prefix.real, zero_prefix.imag],
            "discrepancy": discrepancy,
            "arithmetic_class": "NON_DIRECTED_HIGH_PRECISION",
            "status": "PASS",
        }
    )

    # 7. Finite filtered energy remains positive and rejects its boundary.
    finite_lambdas = (
        complex(0.2, 1.0),
        complex(0.2, -1.0),
        complex(-0.2, 1.0),
        complex(-0.2, -1.0),
    )
    energy = finite_resolvent_energy(
        0.3,
        finite_lambdas,
        q=complex(1.0, 1.0),
        m=3,
    )
    if not energy > 0:
        raise AssertionError("filtered Cauchy-Gram energy must be positive")
    try:
        finite_resolvent_energy(
            0.2,
            finite_lambdas,
            q=complex(1.0, 1.0),
            m=3,
        )
    except ValueError:
        boundary_rejected = True
    else:
        boundary_rejected = False
        raise AssertionError("energy boundary was not rejected")
    checks.append(
        {
            "name": "filtered_energy_boundary",
            "energy_at_0.3": energy,
            "boundary_rejected": boundary_rejected,
            "status": "PASS",
        }
    )

    canonical = json.dumps(checks, sort_keys=True, separators=(",", ":"))
    proof_object = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    payload = {
        "schema": "riemann.phase-speiser-localization.v1",
        "status": "PASS_PFR_PRIME_KNOT_CURVATURE_AND_SOFT_LOCALIZATION",
        "checks": checks,
        "check_count": len(checks),
        "proof_object": proof_object,
        "rh_status": "UNPROVEN",
        "scope": {
            "analytic_manuscript_machine_proved": False,
            "external_novelty_certified": False,
            "directed_rounding": False,
            "actual_zeta_regressions": "NON_DIRECTED_HIGH_PRECISION",
        },
    }

    results_dir = HERE.parent / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    output = results_dir / "verification_108320.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print(payload["status"])
    print(f"checks={payload['check_count']}")
    print(f"proof_object={proof_object}")
    print("RH_UNPROVEN")


if __name__ == "__main__":
    main()
