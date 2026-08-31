from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "beta_chiral_source_cauchy_decomposition.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "beta_chiral_source_cauchy_decomposition",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class BetaChiralSourceCauchyDecompositionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_scope(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108008_BETA_CHIRAL_SOURCE_CAUCHY_DECOMPOSITION",
        )
        self.assertTrue(payload["t108006_chiral_source_front_door_authenticated"])
        self.assertTrue(payload["t108006_primitive_pair_orientation_sign_corrected"])
        self.assertTrue(payload["beta_pair_evenness_oriented_reduction_proved"])
        self.assertTrue(payload["exact_cauchy_transfer_proved"])
        self.assertTrue(payload["finite_jump_spectrum_inserted_before_source_norm"])
        self.assertTrue(payload["signed_chebyshev_cell_current_identity_proved"])
        self.assertTrue(payload["duplicate67_cross_scale_field_identity_proved"])
        self.assertTrue(payload["diagonal_beta_square_euler_product_proved"])
        self.assertTrue(payload["diagonal_has_no_cusp_amplification_proved"])
        self.assertTrue(payload["first_edge_two_cauchy_channels_proved"])
        self.assertFalse(payload["signed_off_diagonal_cusp_correlation_estimate_proved"])
        self.assertFalse(payload["outer_frequency_tails_paid"])
        self.assertFalse(payload["new_zero_free_region_proved"])
        self.assertFalse(payload["rh_established"])

    def test_duplicate67_scale_identity(self) -> None:
        for row in self.payload["scale_filter_rows"]:
            self.assertLess(row["absolute_error"], 2e-13)

    def test_three_source_coordinates_agree_exactly(self) -> None:
        fixture = self.payload["rational_cell_fixture"]
        self.assertEqual(fixture["jump_masses"], [1, -2, 2, -1])
        energy = Fraction(fixture["energy"][0], fixture["energy"][1])
        self.assertGreater(energy, 0)

    def test_cauchy_partial_fraction(self) -> None:
        for row in self.payload["partial_fraction_rows"]:
            self.assertLess(row["absolute_error"], 2e-15)

    def test_diagonal_off_diagonal_split(self) -> None:
        row = self.payload["pair_transfer_fixture"]
        self.assertAlmostEqual(
            row["total_real"],
            row["diagonal"] + row["off_diagonal_real"],
            places=13,
        )
        self.assertAlmostEqual(row["total_imag"], 0.0, places=13)
        self.assertAlmostEqual(
            row["off_diagonal_real"],
            row["oriented_off_diagonal_real"],
            places=13,
        )

    def test_directed_orientation_sign(self) -> None:
        fixture = self.payload["directed_orientation_fixture"]
        self.assertEqual(fixture["negative_carrier_support_selects"], "m>k")
        for row in fixture["rows"]:
            self.assertEqual(
                row["selected_by_negative_carrier_support"],
                row["numerator"] > row["denominator"],
            )

    def test_exceptional_euler_factor(self) -> None:
        row = self.payload["exceptional_euler_fixture"]
        self.assertEqual(row["direct"], row["product"])

    def test_edge_channels(self) -> None:
        for row in self.payload["edge_channel_rows"]:
            self.assertLess(row["pole_error"], 2e-14)

    def test_proof_object(self) -> None:
        keys = (
            "scale_filter_rows",
            "rational_cell_fixture",
            "partial_fraction_rows",
            "pair_transfer_fixture",
            "directed_orientation_fixture",
            "exceptional_euler_fixture",
            "edge_channel_rows",
        )
        core = {key: self.payload[key] for key in keys}
        expected = hashlib.sha256(
            json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
        self.assertEqual(self.payload["proof_object_sha256"], expected)

    def test_retained_output(self) -> None:
        expected = json.dumps(self.payload, indent=2, sort_keys=True) + "\n"
        self.assertEqual(self.module.OUTPUT.read_text(), expected)


if __name__ == "__main__":
    unittest.main()
