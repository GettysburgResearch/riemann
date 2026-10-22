#!/usr/bin/env python3
"""Deterministic bounded replay for PFR-T5/PFR-T6.

The replay authenticates finite identities and four floating-reconnaissance numerical
regressions.  It does not machine-prove the analytic zero-density, Laplace-pole,
or explicit-formula arguments in the manuscript.
"""

from __future__ import annotations

import hashlib
import json
import math
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from phase_resolvent import (  # noqa: E402
    TAU,
    curvature_defect_zero_count_bound,
    finite_laplace_resolvent,
    finite_resolvent_energy,
    finite_taylor_remainder_resolvent,
    first_twenty_centered_zero_model,
    forced_lag_classes,
    gamma_resolvent_zero_sum,
    hardy_clockwise_convexity_numerator,
    minimum_absolute_curvature_for_span,
    open_petal_signed_turn,
    petal_is_forced_simple_from_span,
    simple_petal_total_turn,
    source_resolvent_truncation,
)


def canonical_hash(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    checks: list[dict] = []

    spans = [0.8 * math.pi, 1.2 * math.pi, 1.7 * math.pi]
    checks.append(
        {
            "name": "open_turn",
            "values": [open_petal_signed_turn(span) for span in spans],
        }
    )
    closed_turns = [simple_petal_total_turn(span) for span in spans]
    assert all(abs(value + TAU) < 1e-12 for value in closed_turns)
    checks.append({"name": "closed_turn", "values": closed_turns})

    thresholds = {
        "at_2pi_simple": petal_is_forced_simple_from_span(TAU),
        "above_2pi_simple": petal_is_forced_simple_from_span(TAU + 1e-8),
        "lags_2_1pi": forced_lag_classes(2.1 * math.pi),
        "lags_4_1pi": forced_lag_classes(4.1 * math.pi),
    }
    assert thresholds == {
        "at_2pi_simple": True,
        "above_2pi_simple": False,
        "lags_2_1pi": 1,
        "lags_4_1pi": 2,
    }
    checks.append({"name": "span_topology", **thresholds})

    curvatures = [minimum_absolute_curvature_for_span(span) for span in spans]
    count_bound = curvature_defect_zero_count_bound(sum(spans), curvatures)
    assert abs(count_bound - 2.8) < 1e-12
    checks.append(
        {
            "name": "curvature_defect",
            "absolute_curvatures": curvatures,
            "count_bound": count_bound,
        }
    )

    theta_p, theta_pp = 2.3, -0.17
    z, z_p, z_pp = 1.2, -0.4, 0.9
    r_phi = z_p / theta_p
    r_phi_phi = z_pp / theta_p**2 - z_p * theta_pp / theta_p**3
    angular_numerator = z * r_phi_phi - z * z - 2.0 * r_phi**2
    real_numerator = hardy_clockwise_convexity_numerator(
        theta_p, theta_pp, z, z_p, z_pp
    )
    assert abs(theta_p**2 * angular_numerator + real_numerator) < 1e-12
    checks.append(
        {
            "name": "real_convexity_coordinate",
            "angular_scaled": theta_p**2 * angular_numerator,
            "real_numerator": real_numerator,
        }
    )

    finite_zeros = (0.2 + 3j, 0.2 - 3j, -0.2 + 3j, -0.2 - 3j)
    finite_energy = finite_resolvent_energy(
        0.7,
        finite_zeros,
        rate=2.0,
        order=3,
    )
    assert finite_energy > 0
    checks.append({"name": "finite_energy", "value": finite_energy})

    probe = 1.3 + 0.7j
    taylor_value = finite_taylor_remainder_resolvent(
        probe,
        finite_zeros,
        rate=2.0,
        order=3,
    )
    zero_value = finite_laplace_resolvent(
        probe,
        finite_zeros,
        rate=2.0,
        order=3,
    )
    taylor_error = abs(taylor_value - zero_value)
    assert taylor_error < 1.0e-13
    checks.append(
        {
            "name": "safe_taylor_remainder",
            "probe": [probe.real, probe.imag],
            "absolute_error": taylor_error,
        }
    )

    rate = 2.0
    order = 3
    regression_rows: list[dict] = []
    for t in (0.25, 0.5, 1.0, 1.5):
        source = source_resolvent_truncation(
            t,
            rate=rate,
            order=order,
            prime_limit=1_000_000,
        )
        zero_side = gamma_resolvent_zero_sum(
            t,
            first_twenty_centered_zero_model(),
            rate=rate,
            order=order,
        ).real
        discrepancy = abs(source - zero_side)
        assert discrepancy < 1.0e-5
        regression_rows.append(
            {
                "t": t,
                "source": source,
                "zero_side": zero_side,
                "absolute_discrepancy": discrepancy,
            }
        )
    checks.append(
        {
            "name": "actual_xi_truncated_source_zero_regression",
            "arithmetic_class": "FLOATING_RECONNAISSANCE",
            "rate": rate,
            "order": order,
            "prime_limit": 1_000_000,
            "zero_pairs": 20,
            "acceptance_threshold": 1.0e-5,
            "rows": regression_rows,
        }
    )

    payload = {
        "schema": "riemann.phase-real-resolvent.v1",
        "status": "PASS_PFR_T5_T6_CONTINUATION",
        "checks": checks,
        "scope": {
            "finite_algebra": "replayed",
            "actual_xi_numeric": "non-directed regression only",
            "analytic_manuscript": "not machine proved",
            "rh": "unproved",
        },
    }
    payload["proof_object"] = canonical_hash(payload)

    results_dir = ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    output = results_dir / "verification_108260.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    print("PASS_PFR_T5_T6_CONTINUATION")
    print(f"checks={len(checks)}")
    print(f"proof_object={payload['proof_object']}")
    print("RH_UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
