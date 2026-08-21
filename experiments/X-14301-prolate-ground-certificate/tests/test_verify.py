#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("x14301_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def load_certificate() -> dict:
    return json.loads(
        (ROOT / "certificates" / "synthetic-exact.json").read_text(encoding="utf-8")
    )


def widen(value: str | int, radius: Fraction) -> tuple[str, str]:
    center = Fraction(value)
    return str(center - radius), str(center + radius)


class ProlateGroundCertificateTests(unittest.TestCase):
    def test_synthetic_certificate_passes(self) -> None:
        result = VERIFY.verify_certificate(load_certificate())
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["midpoint_residual_norm_squared"], "1/100")
        self.assertEqual(
            result["ground_eigenvalue_interval"],
            {"lower": "-1/100", "upper": "0"},
        )
        self.assertEqual(result["tan_ground_angle_upper"], "1/10")
        self.assertEqual(
            result["weighted_projective"]["target_line_distance_upper"],
            "31/100",
        )

    def test_rejects_dimension_one(self) -> None:
        certificate = {
            "schema": VERIFY.SCHEMA,
            "matrix_interval": {"lower": [[0]], "upper": [[0]]},
        }
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_rejects_noninteger_fraction_object(self) -> None:
        certificate = load_certificate()
        certificate["matrix_interval"]["lower"][0][0] = {
            "numerator": 1.5,
            "denominator": 1,
        }
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_rejects_non_parity_invariant_radii(self) -> None:
        certificate = load_certificate()
        certificate["matrix_interval"]["lower"][0][0] = "149/100"
        certificate["matrix_interval"]["upper"][0][0] = "151/100"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_rejects_understated_weighted_complement_factor(self) -> None:
        certificate = load_certificate()
        certificate["weighted_projective"]["even_complement_factor_upper"] = "3/2"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_rejects_understated_residual(self) -> None:
        certificate = load_certificate()
        certificate["midpoint_residual_norm_upper"] = "1/20"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_rejects_false_even_gap(self) -> None:
        certificate = load_certificate()
        certificate["midpoint_gap_even"] = "3"
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_rejects_non_even_candidate(self) -> None:
        certificate = load_certificate()
        certificate["candidate"] = [1, 0, 0, 0]
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)

    def test_absorbs_small_entrywise_boxes(self) -> None:
        certificate = load_certificate()
        radius = Fraction(1, 1000)
        lower = certificate["matrix_interval"]["lower"]
        upper = certificate["matrix_interval"]["upper"]
        for i in range(4):
            for j in range(4):
                lo, hi = widen(lower[i][j], radius)
                lower[i][j] = lo
                upper[i][j] = hi
        result = VERIFY.verify_certificate(certificate)
        self.assertEqual(result["matrix_operator_radius_upper"], "1/250")
        self.assertEqual(result["effective_gap_even"], "124/125")
        self.assertEqual(result["effective_gap_odd"], "249/125")

    def test_rejects_uncertainty_larger_than_gap(self) -> None:
        certificate = load_certificate()
        radius = Fraction(1, 4)
        lower = certificate["matrix_interval"]["lower"]
        upper = certificate["matrix_interval"]["upper"]
        for i in range(4):
            for j in range(4):
                lo, hi = widen(lower[i][j], radius)
                lower[i][j] = lo
                upper[i][j] = hi
        with self.assertRaises(VERIFY.CertificateError):
            VERIFY.verify_certificate(certificate)


if __name__ == "__main__":
    unittest.main()
