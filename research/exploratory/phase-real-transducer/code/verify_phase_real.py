#!/usr/bin/env python3
"""Deterministic bounded replay for the phase/real packet.

The replay checks exact finite algebra and high-precision regressions.  It does
not constitute a proof of the analytic theorems and does not prove RH.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from phase_real import (  # noqa: E402
    Zero,
    archimedean_depoisson_kernel,
    centered_xi_phase_velocity,
    completion_phase_term,
    depoissonized_response,
    derivative_coefficients,
    flower_curve,
    flower_signed_area_density,
    flower_speed,
    flower_velocity,
    phase_fourier_transform,
    phase_velocity,
    prime_cosine_sum,
    prime_tail_absolute_bound,
    quartet_derivative_coefficients,
    quartet_energy_closed,
    quartet_pick_two_point_eigenvalues,
    quartet_polynomial_coefficients,
    quartet_response,
    quartet_zeros,
    response_energy_cauchy,
    xi_log_derivative,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    import mpmath as mp

    mp.mp.dps = 40
    checks: list[dict[str, object]] = []

    # 1. Exact quartet derivative / Speiser-locality firewall algebra.
    aq = Fraction(3, 2)
    bq = Fraction(1, 5)
    polynomial = quartet_polynomial_coefficients(aq, bq)
    derivative = derivative_coefficients(polynomial)
    expected_derivative = quartet_derivative_coefficients(aq, bq)
    require(derivative == expected_derivative, "quartet derivative factorization failed")
    critical_square = aq * aq - bq * bq
    require(critical_square > 0, "fixture must have a>b")
    checks.append(
        {
            "id": "exact_quartet_derivative",
            "status": "PASS",
            "critical_points": [
                "0",
                f"+sqrt({critical_square})",
                f"-sqrt({critical_square})",
            ],
        }
    )

    # 2. Direct kinematic identities at deterministic points.
    for t in [0.1, 0.7, 1.4, 2.2]:
        theta = t + 0.1 * math.sin(t)
        theta_p = 1.0 + 0.1 * math.cos(t)
        z = math.sin(2.0 * t)
        z_p = 2.0 * math.cos(2.0 * t)
        gamma = flower_curve(theta, z)
        velocity = flower_velocity(theta, theta_p, z, z_p)
        lhs_area = 0.5 * (gamma.conjugate() * velocity).imag
        rhs_area = flower_signed_area_density(theta_p, z)
        require(abs(lhs_area - rhs_area) < 5e-15, "area-density identity failed")
        require(
            abs(abs(velocity) - flower_speed(theta_p, z, z_p)) < 5e-15,
            "speed identity failed",
        )
    checks.append({"id": "flower_pointwise_kinematics", "status": "PASS", "samples": 4})

    # 3. Weighted Wirtinger / petal-area inequality on one explicit petal.
    a = mp.mpf("0")
    b = mp.pi / 2
    theta = lambda t: t + mp.mpf("0.1") * mp.sin(t)
    theta_p = lambda t: 1 + mp.mpf("0.1") * mp.cos(t)
    z = lambda t: mp.sin(2 * t)
    z_p = lambda t: 2 * mp.cos(2 * t)
    lhs = mp.quad(lambda t: theta_p(t) * z(t) ** 2, [a, b])
    delta = theta(b) - theta(a)
    rhs = (delta / mp.pi) ** 2 * mp.quad(lambda t: z_p(t) ** 2 / theta_p(t), [a, b])
    require(lhs <= rhs + mp.mpf("1e-50"), "weighted Wirtinger inequality failed")
    checks.append(
        {
            "id": "weighted_petal_wirtinger",
            "status": "PASS",
            "lhs": mp.nstr(lhs, 30),
            "rhs": mp.nstr(rhs, 30),
        }
    )

    # 4. Poisson Fourier transform against an independent oscillatory quadrature.
    aa = mp.mpf("1.7")
    bb = mp.mpf("0.35")
    yy = mp.mpf("0.8")
    zeros_mp = [
        aa + 1j * bb,
        aa - 1j * bb,
        -aa + 1j * bb,
        -aa - 1j * bb,
    ]
    zeros = tuple(Zero(float(mp.re(w)), float(mp.im(w))) for w in zeros_mp)

    def v_mp(x):
        return sum(
            (yy - mp.im(w)) / ((x - mp.re(w)) ** 2 + (yy - mp.im(w)) ** 2)
            for w in zeros_mp
        )

    fourier_errors: list[str] = []
    for kval in [mp.mpf("1")]:
        numeric = 2 * mp.quadosc(
            lambda xx: v_mp(xx) * mp.cos(kval * xx),
            [0, mp.inf],
            omega=kval,
        )
        analytic = phase_fourier_transform(float(kval), float(yy), zeros)
        error = abs(numeric - analytic)
        require(error < mp.mpf("1e-12"), f"Poisson Fourier regression failed: {error}")
        fourier_errors.append(mp.nstr(error, 8))
    checks.append(
        {
            "id": "phase_poisson_fourier",
            "status": "PASS",
            "errors": fourier_errors,
        }
    )

    # 5. Cauchy energy formula and quartet closed form.
    sigma = mp.mpf("0.6")
    response_mp = lambda t: sum(
        mp.exp(mp.im(w) * t) * mp.exp(-1j * mp.re(w) * t)
        for w in zeros_mp
    )
    numeric_energy = mp.quad(
        lambda t: mp.exp(-2 * sigma * t) * abs(response_mp(t)) ** 2,
        [0, mp.inf],
    )
    cauchy_energy = response_energy_cauchy(float(sigma), zeros)
    quartet_energy = quartet_energy_closed(float(sigma), float(aa), float(bb))
    require(abs(numeric_energy - cauchy_energy) < mp.mpf("1e-12"), "Cauchy energy failed")
    require(abs(numeric_energy - quartet_energy) < mp.mpf("1e-12"), "quartet energy failed")
    checks.append(
        {
            "id": "response_energy",
            "status": "PASS",
            "numeric": mp.nstr(numeric_energy, 30),
            "cauchy": repr(cauchy_energy),
            "quartet": repr(quartet_energy),
        }
    )

    # 6. Explicit two-point positive-definiteness failure for an off-axis quartet.
    eig_min, eig_max = quartet_pick_two_point_eigenvalues(float(aa), float(bb))
    require(eig_min < 0 < eig_max, "quartet 2x2 witness did not separate")
    checks.append(
        {
            "id": "quartet_two_point_real_witness",
            "status": "PASS",
            "minimum_eigenvalue": repr(eig_min),
            "maximum_eigenvalue": repr(eig_max),
        }
    )

    # 7. Functional-equation reflection: upper centered phase = safe right-line field.
    reflection_errors: list[str] = []
    for x in [mp.mpf("0"), mp.mpf("3")]:
        y = mp.mpf("0.75")
        # Direct centered expression through the left point.
        s_left = mp.mpf("0.5") - y + 1j * x
        direct = -mp.re(xi_log_derivative(s_left))
        safe = centered_xi_phase_velocity(x, y)
        error = abs(direct - safe)
        require(error < mp.mpf("1e-32"), "xi reflection-phase identity failed")
        reflection_errors.append(mp.nstr(error, 8))
    checks.append(
        {
            "id": "xi_safe_line_phase_reflection",
            "status": "PASS",
            "errors": reflection_errors,
        }
    )

    # 8. Prime cosine formula with an elementary directed absolute tail bound.
    sigma = mp.mpf("2")
    x = mp.mpf("3")
    limit = 20_000
    exact = mp.re(xi_log_derivative(sigma + 1j * x))
    approximation = completion_phase_term(sigma + 1j * x) - prime_cosine_sum(
        sigma, x, limit
    )
    error = abs(exact - approximation)
    tail = mp.mpf(prime_tail_absolute_bound(float(sigma), limit))
    require(error <= tail, "prime cosine error exceeded elementary tail bound")
    checks.append(
        {
            "id": "safe_line_prime_cosine",
            "status": "PASS",
            "cutoff": limit,
            "absolute_error": mp.nstr(error, 30),
            "tail_bound": mp.nstr(tail, 30),
        }
    )

    # 9. Distributional critical explicit formula normalization regression.
    # g(t)=e^{-t}-e^{-2t} vanishes at zero, so the archimedean singularity cancels.
    g = lambda t: mp.exp(-t) - mp.exp(-2 * t)
    arch = mp.quad(
        lambda t: g(t) * archimedean_depoisson_kernel(t),
        [0, 1, mp.inf],
    )
    prime_exact = (
        mp.diff(lambda z: mp.zeta(z), mp.mpf("1.5")) / mp.zeta(mp.mpf("1.5"))
        - mp.diff(lambda z: mp.zeta(z), mp.mpf("2.5")) / mp.zeta(mp.mpf("2.5"))
    )
    xi_difference = xi_log_derivative(mp.mpf("1.5")) - xi_log_derivative(mp.mpf("2.5"))
    distribution_error = abs(arch + prime_exact - xi_difference)
    require(
        distribution_error < mp.mpf("1e-32"),
        "critical explicit-formula normalization failed",
    )
    checks.append(
        {
            "id": "critical_distribution_normalization",
            "status": "PASS",
            "archimedean": mp.nstr(arch, 30),
            "prime": mp.nstr(prime_exact, 30),
            "xi_difference": mp.nstr(xi_difference, 30),
            "error": mp.nstr(distribution_error, 8),
        }
    )

    payload = {
        "schema": "riemann.phase-real-transducer.verification.v1",
        "status": "PASS_PFR_PHASE_REAL_TRANSDUCER",
        "rh_established": False,
        "claims_authenticated": [
            "finite quartet polynomial algebra",
            "finite flower kinematic regressions",
            "finite Poisson/Fourier transducer regressions",
            "finite response-energy regressions",
            "safe-line xi reflection and prime-cosine regressions",
            "distributional normalization regression",
        ],
        "claims_not_authenticated": [
            "external novelty or priority",
            "the analytic proofs in the manuscript",
            "an all-zero actual-Xi inverse-Poisson energy theorem",
            "RH or GRH",
        ],
        "check_count": len(checks),
        "checks": checks,
    }
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    payload["proof_object_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    canonical = json.dumps(payload, indent=2, sort_keys=True) + "\n"

    result_dir = HERE.parent / "results"
    result_dir.mkdir(parents=True, exist_ok=True)
    (result_dir / "verification.json").write_text(canonical, encoding="utf-8")
    print(payload["status"])
    print(f"checks={payload['check_count']}")
    print(f"proof_object={payload['proof_object_sha256']}")
    print("RH_UNPROVEN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
