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
    / "beta_chebyshev_chiral_cusp_source_convolution.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "beta_chebyshev_chiral_cusp_source_convolution",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BetaChebyshevChiralCuspSourceConvolutionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_boundary(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108006_BETA_CHEBYSHEV_CHIRAL_CUSP_SOURCE_CONVOLUTION",
        )
        self.assertTrue(
            payload["two_face_source_pairing_reduced_to_one_directed_face"]
        )
        self.assertTrue(payload["reflected_vertical_beta_convolution_proved"])
        self.assertTrue(
            payload["symmetric_cusp_reduced_to_one_chirality_inside_source"]
        )
        self.assertTrue(payload["one_sided_cubic_log_ratio_carrier_proved"])
        self.assertTrue(payload["exceptional_67_dual_shift_formula_proved"])
        self.assertTrue(
            payload["positive_lambda_exceptional_channel_decoupling_proved"]
        )
        self.assertFalse(
            payload["direct_lambda_zero_nonzero_tau_boundary_theorem_proved"]
        )
        self.assertFalse(
            payload["signed_reciprocal_zeta_correlation_estimate_proved"]
        )
        self.assertFalse(payload["outer_frequency_control_proved"])
        self.assertFalse(payload["perron_boundary_shift_proved"])
        self.assertFalse(payload["new_zero_free_region_proved"])
        self.assertFalse(payload["rh_established"])

    def test_beta_pair_evenness_and_directed_reduction(self) -> None:
        row = self.payload["global_source_pairing"]
        self.assertLess(row["beta_evenness_max_error"], 2e-12)
        self.assertLess(row["directed_face_sum_error"], 2e-10)
        self.assertLess(row["vertical_coordinate_max_error"], 2e-12)
        local = self.payload["local_source_pairing"]
        self.assertLess(local["beta_evenness_max_error"], 2e-12)
        self.assertLess(local["chiral_reduction_sum_error"], 2e-9)

    def test_one_sided_inverse_fourier_carrier(self) -> None:
        for row in self.payload["chiral_inverse_fourier_rows"]:
            self.assertLess(row["absolute_error"], 3e-8)
        self.assertAlmostEqual(
            self.module.chiral_density(2.0, 1.0),
            0j,
            places=14,
        )
        self.assertNotEqual(self.module.chiral_density(2.0, -1.0), 0j)

    def test_directed_boundary_errors_descend(self) -> None:
        errors = [
            row["absolute_error_to_limit"]
            for row in self.payload["directed_boundary_rows"]
        ]
        self.assertTrue(
            all(
                errors[index + 1] < errors[index]
                for index in range(len(errors) - 1)
            )
        )

    def test_exceptional_channel_decouples_for_positive_lambda(self) -> None:
        rows = self.payload["exceptional_dual_rows"]
        bounds = [row["dual_l1_difference_bound"] for row in rows]
        self.assertTrue(
            all(
                bounds[index + 1] < bounds[index]
                for index in range(len(bounds) - 1)
            )
        )
        self.assertLess(self.payload["exceptional_numerator_max_error"], 2e-12)

    def test_proof_object(self) -> None:
        core = {
            "global_source_pairing": self.payload["global_source_pairing"],
            "local_source_pairing": self.payload["local_source_pairing"],
            "chiral_inverse_fourier_rows": self.payload[
                "chiral_inverse_fourier_rows"
            ],
            "chiral_l1_norm_lambda_two": self.payload[
                "chiral_l1_norm_lambda_two"
            ],
            "directed_boundary_constant": self.payload[
                "directed_boundary_constant"
            ],
            "directed_boundary_rows": self.payload["directed_boundary_rows"],
            "exceptional_numerator_max_error": self.payload[
                "exceptional_numerator_max_error"
            ],
            "exceptional_dual_rows": self.payload["exceptional_dual_rows"],
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
