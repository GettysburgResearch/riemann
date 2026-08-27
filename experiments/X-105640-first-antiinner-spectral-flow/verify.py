#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json


def blaschke(r: F, z: F) -> F:
    return (z - r) / (1 - r * z)


def schur_kernel(theta_z: F, theta_w: F, z: F, w: F) -> F:
    return (1 - theta_z * theta_w) / (1 - z * w)


def main() -> None:
    checks: list[str] = []

    # Disk-model replay of
    #   B(z) B(w) K_(A/B) = K_A - K_B,
    # the rank-one Blaschke kernel, and the exact source/complement split.
    for r in (F(1, 2), F(2, 3), F(3, 4), F(4, 5)):
        for m in range(5):
            for z, w in (
                (F(1, 10), F(1, 5)),
                (F(-1, 7), F(2, 9)),
                (F(1, 3), F(-1, 4)),
            ):
                a_z, a_w = z**m, w**m
                b_z, b_w = blaschke(r, z), blaschke(r, w)
                u_z, u_w = a_z / b_z, a_w / b_w

                lhs = b_z * b_w * schur_kernel(u_z, u_w, z, w)
                rhs = (
                    schur_kernel(a_z, a_w, z, w)
                    - schur_kernel(b_z, b_w, z, w)
                )
                assert lhs == rhs
                checks.append(f"kernel:{r}:{m}:{z}:{w}")

                rank_one = schur_kernel(b_z, b_w, z, w)
                expected = (1 - r * r) / ((1 - r * z) * (1 - r * w))
                assert rank_one == expected
                checks.append(f"rank-one:{r}:{m}:{z}:{w}")

            # In the disk model, the normalized model vector has coefficients
            # sqrt(1-r^2) r^n.  A background A(z)=z^m attenuates the first
            # anti-inner Hankel charge by |A(r)|^2=r^(2m).
            for n_band in range(1, 8):
                visible_fraction = sum(
                    (1 - r * r) * r ** (2 * n)
                    for n in range(n_band)
                )
                complement_fraction = r ** (2 * n_band)
                attenuation = r ** (2 * m)

                assert visible_fraction == 1 - complement_fraction
                visible = attenuation * visible_fraction
                complement = attenuation * complement_fraction
                assert visible + complement == attenuation
                checks.append(f"split:{r}:{m}:{n_band}")

    payload = {
        "verdict": "PASS_X_105640_FIRST_ANTIINNER_SPECTRAL_FLOW",
        "arithmetic_class": "EXACT_RATIONAL_DISK_MODEL_ALGEBRA",
        "checks": len(checks),
        "kernel_congruence_replayed": True,
        "rank_one_crossing_replayed": True,
        "adaptive_band_visible_tail_conservation_replayed": True,
        "xi_descent_below_beta1_proved": False,
        "pointwise_microscope_sign_proved": False,
        "rh_established": False,
    }
    proof_object = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    payload["proof_object"] = proof_object

    print(payload["verdict"])
    print(f"checks={len(checks)}")
    print(proof_object)


if __name__ == "__main__":
    main()
