from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "beta_chebyshev_cubic_cusp_edge_profile.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "beta_chebyshev_cubic_cusp_edge_profile",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BetaChebyshevCubicCuspEdgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_boundary(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108002_BETA_CHEBYSHEV_CUBIC_CUSP_EDGE_PROFILE",
        )
        self.assertTrue(payload["finite_cubic_cusp_profile_proved"])
        self.assertTrue(payload["critical_window_exponent_two_thirds_proved"])
        self.assertTrue(payload["amplitude_exponent_one_third_proved"])
        self.assertTrue(payload["exact_edge_gamma_constant_proved"])
        self.assertTrue(payload["outer_matching_to_stieltjes_threshold_proved"])
        self.assertFalse(payload["finite_edge_airy_asymptotic_proved"])
        self.assertFalse(payload["beta_source_cancellation_proved"])
        self.assertFalse(payload["new_zero_free_region_proved"])
        self.assertFalse(payload["rh_established"])

    def test_exact_edge_constant(self) -> None:
        value = self.module.edge_gamma_constant()
        self.assertAlmostEqual(value.real, 2.5281648323743786, places=12)
        self.assertAlmostEqual(value.imag, -1.4596366465270922, places=12)
        self.assertAlmostEqual(
            self.module.cubic_cusp_profile(0.0).real,
            value.real,
            places=14,
        )

    def test_positive_lambda_profile(self) -> None:
        value = self.module.cubic_cusp_profile(2.0)
        self.assertAlmostEqual(value.real, 1.60722845137069, places=10)
        self.assertAlmostEqual(value.imag, -1.29749076763844, places=10)

    def test_finite_edge_errors_descend(self) -> None:
        for key in ("finite_edge_lambda_zero", "finite_edge_lambda_two"):
            errors = [
                row["absolute_error_to_limit"] for row in self.payload[key]
            ]
            self.assertTrue(
                all(
                    errors[index + 1] < errors[index]
                    for index in range(len(errors) - 1)
                )
            )

    def test_proof_object(self) -> None:
        core = {
            "edge_gamma_constant": self.payload["edge_gamma_constant"],
            "lambda_two_profile": self.payload["lambda_two_profile"],
            "finite_edge_lambda_zero": self.payload["finite_edge_lambda_zero"],
            "finite_edge_lambda_two": self.payload["finite_edge_lambda_two"],
            "outer_matching_constant": self.payload["outer_matching_constant"],
            "outer_matching": self.payload["outer_matching"],
        }
        expected = hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.assertEqual(self.payload["proof_object_sha256"], expected)

    def test_retained_output(self) -> None:
        expected = json.dumps(
            self.payload,
            indent=2,
            sort_keys=True,
        ) + "\n"
        self.assertEqual(self.module.OUTPUT.read_text(), expected)


if __name__ == "__main__":
    unittest.main()
