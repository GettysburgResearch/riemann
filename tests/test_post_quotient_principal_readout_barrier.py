"""Native principal readout, strict literal diagonal, and whole Gram interval."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = Path(__file__).resolve().parents[1] / "research" / "riemann-structures" / "post_quotient_principal_readout_barrier.py"
SPEC = importlib.util.spec_from_file_location("principal_readout", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class PrincipalReadoutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.panels = json.loads(M.source_bytes((M.NMO,M.NMO_PATH)))["panels"]
        cls.kernel = json.loads(M.source_bytes((M.SCB,M.SCB_PATH)))["kernel"]

    def test_native_gram_positive_on_full_doubled_frequency_interval(self):
        result = M.kernel_bounds(self.kernel)
        self.assertGreater(Fraction(result["Gamma_difference_strict_lower"]),1)
        self.assertEqual(result["frequency_difference_strict_radius"],"1/5")
        self.assertEqual(result["log2_three_term_strict_lower"],"842/1215")

    def test_actual_source_panels_satisfy_two_sided_readout_bounds(self):
        for panel in self.panels:
            result = M.panel_bounds(panel)
            count = result["arithmetic_pairs"]
            self.assertGreaterEqual(Fraction(result["certified_energy_over_literal_diagonal_lower"]),
                                    Fraction(25,2904)*count)
            self.assertEqual(result["universal_energy_over_literal_diagonal_upper"],4*count)
            self.assertEqual(result["all_frequency_difference_ratio_checks"],count**2)

    def test_four_literal_histories_are_not_one_new_pair_diagonal(self):
        result = M.panel_bounds(self.panels[0])
        self.assertEqual(Fraction(result["pair_diagonal_divided_by_Gamma0"]),
                         4*Fraction(result["literal_diagonal_divided_by_Gamma0"]))
        self.assertEqual(result["literal_histories"],4*result["arithmetic_pairs"])
        panel = copy.deepcopy(self.panels[0])
        panel["entries"][0]["literal_histories_per_mode"] = 1
        with self.assertRaises(ValueError):
            M.panel_bounds(panel)

    def test_native_irrational_weights_and_source_dual_scale_are_enforced(self):
        for field in ("native_coefficient_square","source_dual_coefficient_square"):
            panel = copy.deepcopy(self.panels[0])
            panel["entries"][0][field] = "1"
            with self.subTest(field=field), self.assertRaises(ValueError):
                M.panel_bounds(panel)

    def test_negative_or_nonliteral_source_branch_is_rejected(self):
        for value in (False,1):
            panel = copy.deepcopy(self.panels[0])
            panel["entries"][0]["positive_coefficient_branch_from_histories"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.panel_bounds(panel)

    def test_kernel_endpoint_variation_cannot_be_dropped(self):
        kernel = copy.deepcopy(self.kernel)
        kernel["total_variation"] = ["0","16"]
        with self.assertRaises(ValueError):
            M.kernel_bounds(kernel)

    def test_physical_windows_and_complete_rectangle_are_checked(self):
        panel = copy.deepcopy(self.panels[0])
        panel["horizon"] *= 2
        with self.assertRaises(ValueError):
            M.panel_bounds(panel)
        panel = copy.deepcopy(self.panels[0])
        panel["entries"].pop()
        panel["literal_history_count"] -= 4
        with self.assertRaises(ValueError):
            M.panel_bounds(panel)

    def test_exact_integer_types_and_caps_survive_optimization(self):
        for value in (True,1.0,1 << 300):
            panel = copy.deepcopy(self.panels[0])
            panel["horizon"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                M.panel_bounds(panel)

    def test_wrong_source_blob_is_rejected_before_use(self):
        key = (M.NMO,M.NMO_PATH)
        with patch.dict(M.SOURCES,{key:"0"*40}), self.assertRaises(ValueError):
            M.source_bytes(key)

    def test_canonical_acceptance_distinguishes_numeric_counterfeits(self):
        for value in (True,1.0):
            self.assertNotEqual(M.canonical({"count":1}),M.canonical({"count":value}))
        with self.assertRaises(ValueError):
            M.canonical({"count":float("nan")})

    def test_full_frozen_source_schema_and_build_are_bound(self):
        result = M.build()
        self.assertEqual([p["arithmetic_pairs"] for p in result["panels"]],[9,12])
        self.assertFalse(result["complete_principal_moment_counterexample"])
        self.assertTrue(result["absolute_energy_tends_to_zero"])


if __name__ == "__main__":
    unittest.main()
