from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from pathlib import Path

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "source_grouped_positive_hodge_descent.py"
)


def load_module():
    spec = importlib.util.spec_from_file_location(
        "source_grouped_positive_hodge_descent",
        MODULE_PATH,
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SourceGroupedPositiveHodgeDescentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()
        cls.payload = cls.module.build_payload()

    def test_classification_and_scope(self) -> None:
        payload = self.payload
        self.assertEqual(
            payload["classification"],
            "PASS_T108104_SOURCE_GROUPED_POSITIVE_HODGE_DESCENT",
        )
        self.assertTrue(payload["two_stage_atom_group_cell_factorization_proved"])
        self.assertTrue(
            payload["positive_part_invariant_under_authorized_history_aggregation"]
        )
        self.assertTrue(payload["within_history_fluctuations_exact_negative_d_block"])
        self.assertTrue(
            payload["same_cell_cross_group_zero_current_exact_negative_d_block"]
        )
        self.assertFalse(payload["complete_live_occupancy_census_proved"])
        self.assertFalse(payload["signed_cross_conductor_recombination_proved"])
        self.assertFalse(payload["global_relative_trace_proved"])
        self.assertFalse(payload["principal_binding_proved"])
        self.assertFalse(payload["rh_or_grh_established"])

    def test_live_ledger(self) -> None:
        live = self.payload["live"]
        self.assertEqual(live["cell_sums"], [{"numerator": 4, "denominator": 1}])
        self.assertEqual(live["total_energy"], {"numerator": 676, "denominator": 1})
        self.assertEqual(
            live["quotient_input_energy"],
            {"numerator": 4, "denominator": 25},
        )
        self.assertEqual(
            live["within_history_variance"],
            {"numerator": 16896, "denominator": 25},
        )

    def test_two_stage_variances_add(self) -> None:
        toy = self.payload["toy"]
        within = self.module.Fraction(
            toy["within_history_variance"]["numerator"],
            toy["within_history_variance"]["denominator"],
        )
        between = self.module.Fraction(
            toy["within_cell_group_variance"]["numerator"],
            toy["within_cell_group_variance"]["denominator"],
        )
        total = self.module.Fraction(
            toy["total_kernel_energy"]["numerator"],
            toy["total_kernel_energy"]["denominator"],
        )
        self.assertEqual(within + between, total)

    def test_positive_debt_ignores_history_lift(self) -> None:
        self.assertEqual(
            self.payload["toy_spectral"]["positive"],
            self.payload["toy_changed_spectral"]["positive"],
        )
        self.assertNotEqual(
            self.payload["toy"]["total_energy"],
            self.payload["toy_changed_lift"]["total_energy"],
        )

    def test_cross_group_zero_current(self) -> None:
        cross = self.payload["cross_group_zero_current"]
        self.assertEqual(
            cross["quotient_input_energy"],
            {"numerator": 0, "denominator": 1},
        )
        self.assertEqual(
            cross["within_history_variance"],
            {"numerator": 0, "denominator": 1},
        )
        self.assertEqual(
            cross["within_cell_group_variance"],
            {"numerator": 4, "denominator": 1},
        )

    def test_positive_minus_negative_is_full_wick_value(self) -> None:
        positive = self.payload["toy_spectral"]["positive"]
        negative = self.payload["toy_spectral"]["full_negative"]
        p = self.module.Fraction(positive["numerator"], positive["denominator"])
        n = self.module.Fraction(negative["numerator"], negative["denominator"])
        full = self.payload["full_wick_value"]
        expected = self.module.Fraction(full["numerator"], full["denominator"])
        self.assertEqual(p - n, expected)

    def test_proof_object(self) -> None:
        keys = (
            "live",
            "toy",
            "toy_changed_lift",
            "toy_spectral",
            "toy_changed_spectral",
            "cross_group_zero_current",
            "full_wick_value",
            "quotient_wick_value",
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
