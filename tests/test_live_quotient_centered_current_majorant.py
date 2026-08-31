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
    / "riemann-structures"
    / "live_quotient_centered_current_majorant.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "live_quotient_centered_current_majorant",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LiveQuotientCenteredCurrentMajorantTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_scope(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108106_LIVE_QUOTIENT_CENTERED_CURRENT_MAJORANT",
        )
        self.assertTrue(payload["full_grid_projection_majorant_proved"])
        self.assertTrue(payload["double_centered_current_formula_proved"])
        self.assertTrue(payload["unknown_quotient_norm_removed_from_upper_bound"])
        self.assertTrue(payload["cross_history_terms_retained_before_square"])
        self.assertTrue(payload["zero_centered_current_zero_positive_debt"])
        self.assertFalse(payload["complete_live_grouped_current_census_proved"])
        self.assertFalse(payload["signed_cross_conductor_estimate_proved"])
        self.assertFalse(payload["global_relative_trace_proved"])
        self.assertFalse(payload["principal_binding_proved"])
        self.assertFalse(payload["rh_or_grh_established"])

    def test_projection_formula(self) -> None:
        current = {(0, 0): Fraction(3), (1, 1): Fraction(-1)}
        direct = self.module.norm_squared(
            self.module.centered_projection(3, 2, current)
        )
        formula = self.module.centered_energy_formula(3, 2, current)
        self.assertEqual(direct, formula)
        self.assertEqual(formula, Fraction(7, 3))

    def test_positive_majorant_fixture(self) -> None:
        row = self.payload["two_cell"]
        positive = Fraction(
            row["positive_debt"]["numerator"],
            row["positive_debt"]["denominator"],
        )
        majorant = Fraction(
            row["centered_energy"]["numerator"],
            row["centered_energy"]["denominator"],
        )
        self.assertLessEqual(positive, majorant)
        self.assertEqual(positive, Fraction(2, 3))

    def test_additive_current_has_zero_debt(self) -> None:
        self.assertEqual(
            self.payload["zero_centered"]["centered_energy"],
            {"numerator": 0, "denominator": 1},
        )

    def test_live_one_cell_ledger(self) -> None:
        live = self.payload["live_one_cell"]
        self.assertEqual(
            live["principal_density"],
            {"numerator": 535600, "denominator": 537151},
        )
        ratio = Fraction(
            live["majorant_to_literal_energy_ratio"]["numerator"],
            live["majorant_to_literal_energy_ratio"]["denominator"],
        )
        self.assertEqual(ratio, Fraction(4, 169) * Fraction(535600, 537151))
        self.assertLess(ratio, Fraction(4, 169))

    def test_proof_object(self) -> None:
        core = {
            "two_cell": self.payload["two_cell"],
            "zero_centered": self.payload["zero_centered"],
            "live_one_cell": self.payload["live_one_cell"],
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
