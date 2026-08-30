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
    / "beta_chebyshev_perron_fourier_cusp_carrier.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "beta_chebyshev_perron_fourier_cusp_carrier",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BetaChebyshevPerronFourierCuspCarrierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_boundary(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108004_BETA_CHEBYSHEV_PERRON_FOURIER_CUSP_CARRIER",
        )
        self.assertTrue(payload["frequency_split_identity_proved"])
        self.assertTrue(payload["complex_cusp_extension_proved"])
        self.assertTrue(payload["two_parameter_perron_fourier_cusp_proved"])
        self.assertTrue(payload["exact_dual_lag_carrier_proved"])
        self.assertFalse(payload["beta_source_correlation_estimate_proved"])
        self.assertFalse(payload["new_zero_free_region_proved"])
        self.assertFalse(payload["rh_established"])

    def test_independent_cell_and_jump_transforms_agree(self) -> None:
        for row in self.payload["split_rows"]:
            self.assertLess(row["absolute_error"], 2e-12)

    def test_dual_carrier_inverts_to_cusp(self) -> None:
        for row in self.payload["cusp_rows"]:
            self.assertLess(row["inverse_dual_error"], 2e-10)

    def test_finite_two_parameter_errors_descend(self) -> None:
        for row in self.payload["cusp_rows"]:
            errors = [entry["absolute_error_to_limit"] for entry in row["finite"]]
            self.assertTrue(
                all(
                    errors[index + 1] < errors[index]
                    for index in range(len(errors) - 1)
                )
            )

    def test_tau_zero_recovers_parent_profile(self) -> None:
        value = self.module.perron_fourier_cusp(2.0, 0.0)
        parent = self.module.cubic_cusp_profile_complex(2.0 + 0j)
        self.assertAlmostEqual(value.real, parent.real, places=13)
        self.assertAlmostEqual(value.imag, parent.imag, places=13)

    def test_evenness(self) -> None:
        left = self.module.perron_fourier_cusp(2.0, -1.375)
        right = self.module.perron_fourier_cusp(2.0, 1.375)
        self.assertAlmostEqual(left.real, right.real, places=13)
        self.assertAlmostEqual(left.imag, right.imag, places=13)

    def test_proof_object(self) -> None:
        core = {
            "split_rows": self.payload["split_rows"],
            "cusp_rows": self.payload["cusp_rows"],
            "evenness_error": self.payload["evenness_error"],
            "dual_sample": self.payload["dual_sample"],
        }
        expected = hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.assertEqual(self.payload["proof_object_sha256"], expected)

    def test_retained_output(self) -> None:
        expected = json.dumps(self.payload, indent=2, sort_keys=True) + "\n"
        self.assertEqual(self.module.OUTPUT.read_text(), expected)


if __name__ == "__main__":
    unittest.main()
