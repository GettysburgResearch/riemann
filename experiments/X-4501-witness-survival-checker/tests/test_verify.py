from __future__ import annotations

import copy
from fractions import Fraction
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from verify import (  # noqa: E402
    CertificateError,
    QComplex,
    as_complex,
    pick_midpoint_direct,
    verify_certificate,
)

CERTIFICATES = ROOT / "certificates"


def load(name: str) -> dict:
    return json.loads((CERTIFICATES / name).read_text(encoding="utf-8"))


class CommittedCertificateTests(unittest.TestCase):
    def test_affine_box_survives(self) -> None:
        result = verify_certificate(load("affine-box-survives.json"))
        self.assertEqual(result["status"], "CERTIFIED_QUANTITATIVE_SURVIVAL")
        self.assertEqual(result["robust_upper"], "-4/5")
        self.assertEqual(result["strict_moat"], "4/5")

    def test_affine_box_zero_touch_does_not_certify(self) -> None:
        result = verify_certificate(load("affine-box-touches-zero.json"))
        self.assertEqual(result["status"], "NOT_CERTIFIED")
        self.assertEqual(result["robust_upper"], "0")

    def test_correlated_polytope_dual_survives(self) -> None:
        certificate = load("affine-polytope-correlation.json")
        result = verify_certificate(certificate)
        self.assertEqual(result["robust_upper"], "-1/10")
        # Forgetting the equality u1+u2=0 and using the independent box
        # [-1,1]^2 would give the useless upper bound -1/10+2=19/10.
        self.assertGreater(Fraction(19, 10), 0)

    def test_pick_disk_compression_survives(self) -> None:
        result = verify_certificate(load("pick-disks-survives.json"))
        self.assertEqual(result["status"], "CERTIFIED_QUANTITATIVE_SURVIVAL")
        self.assertEqual(result["details"]["midpoint"], "-225/104")
        self.assertEqual(result["details"]["uncertainty_increment"], "137/4000")
        self.assertEqual(result["robust_upper"], "-110719/52000")

    def test_pick_disk_too_wide_does_not_certify(self) -> None:
        result = verify_certificate(load("pick-disks-too-wide.json"))
        self.assertEqual(result["status"], "NOT_CERTIFIED")
        self.assertEqual(result["robust_upper"], "82/65")

    def test_pick_compressed_identity_matches_direct_matrix(self) -> None:
        certificate = load("pick-disks-survives.json")
        points = [as_complex(value, field="point") for value in certificate["points"]]
        vector = [as_complex(value, field="vector") for value in certificate["vector"]]
        centers = [as_complex(value["center"], field="center") for value in certificate["samples"]]
        direct = pick_midpoint_direct(points, vector, centers)
        self.assertEqual(direct, Fraction(-225, 104))


class FailClosedMutationTests(unittest.TestCase):
    def test_undeclared_quantitative_channel_is_rejected(self) -> None:
        certificate = load("affine-box-survives.json")
        certificate["terms"][0]["channel_id"] = "hidden-channel"
        with self.assertRaisesRegex(CertificateError, "uncertainty closure mismatch"):
            verify_certificate(certificate)

    def test_declared_but_unused_channel_is_rejected(self) -> None:
        certificate = load("affine-box-survives.json")
        certificate["uncertainty_manifest"]["quantitative_channels"].append(
            {"id": "forgotten-tail", "state": "TAIL_BOUNDED"}
        )
        with self.assertRaisesRegex(CertificateError, "uncertainty closure mismatch"):
            verify_certificate(certificate)

    def test_blocking_gate_is_rejected(self) -> None:
        certificate = load("affine-box-survives.json")
        certificate["uncertainty_manifest"]["logical_gates"][0]["state"] = "BLOCKING"
        with self.assertRaisesRegex(CertificateError, "remains blocking"):
            verify_certificate(certificate)

    def test_broken_polytope_dual_equality_is_rejected(self) -> None:
        certificate = load("affine-polytope-correlation.json")
        certificate["dual"][0] = "1/2"
        with self.assertRaisesRegex(CertificateError, r"A\^T y = objective fails"):
            verify_certificate(certificate)

    def test_infeasible_polytope_anchor_is_rejected(self) -> None:
        certificate = load("affine-polytope-correlation.json")
        certificate["feasible_point"] = ["2", "0"]
        with self.assertRaisesRegex(CertificateError, "feasible_point violates"):
            verify_certificate(certificate)

    def test_too_small_pick_coefficient_bound_is_rejected(self) -> None:
        certificate = load("pick-disks-survives.json")
        certificate["samples"][0]["coefficient_abs_upper"] = "1"
        with self.assertRaisesRegex(CertificateError, "too small"):
            verify_certificate(certificate)

    def test_pick_point_on_boundary_is_rejected(self) -> None:
        certificate = load("pick-disks-survives.json")
        certificate["points"][0]["re"] = "1/2"
        with self.assertRaisesRegex(CertificateError, r"not in Re\(s\)>1/2"):
            verify_certificate(certificate)

    def test_claimed_upper_mismatch_is_rejected(self) -> None:
        certificate = load("affine-box-survives.json")
        certificate["claimed_robust_upper"] = "-3/4"
        with self.assertRaisesRegex(CertificateError, "exact reconstruction"):
            verify_certificate(certificate)

    def test_closed_gate_manifest_changes_status_but_not_arithmetic(self) -> None:
        certificate = load("affine-box-survives.json")
        gate = certificate["uncertainty_manifest"]["logical_gates"][0]
        gate["state"] = "INDEPENDENTLY_VERIFIED"
        gate["evidence"] = "claims/example-independent-proof.md"
        result = verify_certificate(certificate)
        self.assertEqual(result["status"], "QUANTITATIVE_SURVIVAL_WITH_CLOSED_GATE_MANIFEST")
        self.assertEqual(result["robust_upper"], "-4/5")


if __name__ == "__main__":
    unittest.main()
