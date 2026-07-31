from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
spec = importlib.util.spec_from_file_location("x14304_verify", ROOT / "verify.py")
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

CERT = json.loads(
    (ROOT / "certificates" / "synthetic-squared-residual.json").read_text()
)


def frac(raw):
    return Fraction(int(raw["numerator"]), int(raw["denominator"]))


class BlockTempleFloorTests(unittest.TestCase):
    def test_synthetic_certificate(self):
        result = module.verify(copy.deepcopy(CERT))
        self.assertEqual(result["verdict"], "CERTIFIED_AMBIENT_LOWER_FLOOR")
        self.assertEqual(
            frac(result["certified_ambient_floor"]), Fraction(-1001, 1_000_000)
        )
        diagnostic = result["scalar_diagnostics"]
        self.assertEqual(
            frac(diagnostic["dual_residual_squared"]), Fraction(1, 1_000_000)
        )
        self.assertEqual(frac(diagnostic["energy_penalty"]), Fraction(1, 1000))
        self.assertEqual(frac(diagnostic["distance_ratio_squared"]), Fraction(1))
        self.assertEqual(
            frac(diagnostic["corrected_low_scalar"]), Fraction(-1, 1000)
        )
        self.assertEqual(
            result["exact_proof_object_sha256"],
            "bdc5d3a7d70ae9fe048411d2195f6c18de2323015a86c9e85ac8e9fd6de09463",
        )

    def test_epsilon_family_separates_distance_and_energy(self):
        for denominator in (10, 100, 1000):
            eps = Fraction(1, denominator)
            cert = copy.deepcopy(CERT)
            cert["blocks"]["R"] = [
                [{"numerator": 1, "denominator": denominator}]
            ]
            cert["blocks"]["C"] = [
                [{"numerator": denominator + 2, "denominator": denominator}]
            ]
            cert["h"] = {"numerator": 1, "denominator": denominator}
            floor = -eps - eps * eps
            cert["claimed_midpoint_floor"] = {
                "numerator": floor.numerator,
                "denominator": floor.denominator,
            }
            result = module.verify(cert)
            diagnostic = result["scalar_diagnostics"]
            self.assertEqual(frac(diagnostic["energy_penalty"]), eps)
            self.assertEqual(frac(diagnostic["distance_ratio_squared"]), 1)

    def test_doubled_cross_map_breaks_claimed_floor(self):
        cert = copy.deepcopy(CERT)
        cert["blocks"]["R"] = [[{"numerator": 1, "denominator": 500}]]
        with self.assertRaises(module.CertificateError):
            module.verify(cert)

    def test_nonpositive_metric_rejected(self):
        cert = copy.deepcopy(CERT)
        cert["blocks"]["M"] = [[0]]
        with self.assertRaises(module.CertificateError):
            module.verify(cert)

    def test_gamma_below_floor_rejected(self):
        cert = copy.deepcopy(CERT)
        cert["gamma"] = -2
        with self.assertRaises(module.CertificateError):
            module.verify(cert)

    def test_production_requires_radius_gate(self):
        cert = copy.deepcopy(CERT)
        cert["classification"] = module.PRODUCTION
        with self.assertRaises(module.CertificateError):
            module.verify(cert)
        cert["operator_radius_gate"] = {
            "status": module.RADIUS_GATE,
            "sha256": "a" * 64,
        }
        result = module.verify(cert)
        self.assertEqual(result["classification"], module.PRODUCTION)

    def test_operator_radius_is_subtracted_exactly(self):
        cert = copy.deepcopy(CERT)
        cert["operator_radius"] = {"numerator": 1, "denominator": 1_000_000}
        result = module.verify(cert)
        self.assertEqual(
            frac(result["certified_ambient_floor"]), Fraction(-1002, 1_000_000)
        )

    def test_boolean_integer_rejected(self):
        cert = copy.deepcopy(CERT)
        cert["blocks"]["B"] = [[True]]
        with self.assertRaises(module.CertificateError):
            module.verify(cert)

    def test_bad_cross_dimension_rejected(self):
        cert = copy.deepcopy(CERT)
        cert["blocks"]["R"] = [[0, 0]]
        with self.assertRaises(module.CertificateError):
            module.verify(cert)


if __name__ == "__main__":
    unittest.main()
