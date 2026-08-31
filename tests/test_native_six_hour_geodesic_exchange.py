"""Complete physical factorizations, native integration and exchange controls."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "geodesic_factor_exchange.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_geodesic_exchange", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeGeodesicExchangeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zero = M.factor_control(*M.zero_spec())
        native = json.loads(M.source_bytes((M.DENSE, M.DENSE_JSON)))
        cls.positive = M.factor_control(*M.held_out_spec(native))

    def test_literal_local_half_geodesic_endpoints_and_derivatives(self):
        self.assertEqual(M.local(0), (Fraction(1),))
        self.assertEqual(M.local(1), (Fraction(0), Fraction(-1, 2)))
        self.assertEqual(M.local(2), (Fraction(-1, 2), Fraction(3, 8)))
        self.assertEqual(M.local(4), (Fraction(-1, 8), Fraction(11, 128)))
        for e in range(5):
            self.assertEqual(M.evaluate(M.local(e), 1), M.sqrt_coefficient(e))

    def test_complete_zero_chart_not_selected_twenty_four_histories(self):
        self.assertEqual(self.zero["complete_factor_count"], 3888)
        self.assertEqual(sum(self.zero["coefficient_histogram"].values()), 3888)
        self.assertEqual(
            sum(x["multiplicity"] for x in self.zero["coalesced_patterns"]), 3888
        )
        self.assertEqual(self.zero["complete_stripped_coefficient"], "0")
        self.assertGreater(len(self.zero["coefficient_histogram"]), 2)

    def test_fixed_tuple_actual_derivative_sites_and_nonzero_swapped_sum(self):
        N, K = 1005930209094, self.zero["K"]
        a = self.zero["selected_records"][str(N)]
        b = self.zero["selected_records"][str(K // N)]
        self.assertNotEqual(Fraction(a["coefficient"]), 0)
        self.assertNotEqual(Fraction(b["coefficient"]), 0)
        self.assertEqual(
            Fraction(a["coefficient"]) + Fraction(b["coefficient"]),
            Fraction(-1, 262144),
        )
        self.assertEqual(
            {p for p, _ in a["integrated_derivative_sites_by_prime"]},
            {2, 3, 71, 73, 79},
        )
        for row in (a, b):
            self.assertEqual(
                sum(
                    (
                        Fraction(v)
                        for _, v in row["integrated_derivative_sites_by_prime"]
                    ),
                    Fraction(),
                ),
                Fraction(row["coefficient"]),
            )

    def test_root_free_left_tangent_and_native_right_unit(self):
        rows = self.zero["selected_records"]
        self.assertEqual(rows["1"]["coefficient"], "0")
        self.assertEqual(rows["1"]["integrated_derivative_sites_by_prime"], [])
        self.assertEqual(rows[str(self.zero["K"])]["coefficient"], "-1/262144")
        self.assertEqual(self.zero["primitive_measure"], "2 d_tau; not probability")

    def test_complete_swap_closed_owner_sectors_have_paid_complements(self):
        sectors = self.zero["physical_odd_owner_sectors"]
        self.assertEqual(
            sectors["exactly_two_odd_each"], {"count": 192, "coefficient": "-3/8192"}
        )
        self.assertEqual(
            sectors["and_two_squared_each"], {"count": 120, "coefficient": "-15/65536"}
        )
        self.assertEqual(Fraction(self.zero["complete_stripped_coefficient"]), 0)

    def test_exchange_diagonal_and_distinct_site_resolutions(self):
        for row in (self.zero, self.positive):
            diag = Fraction(row["aggregated_coefficient_diagonal_times_K"])
            symmetric = Fraction(row["symmetric_diagonal_times_K"])
            antisymmetric = Fraction(row["antisymmetric_diagonal_times_K"])
            self.assertEqual(diag, symmetric + antisymmetric)
            self.assertGreater(symmetric, 0)
            self.assertGreater(antisymmetric, 0)
            self.assertNotEqual(
                Fraction(row["primitive_site_diagonal_times_K"]),
                Fraction(row["separately_integrated_site_diagonal_times_K"]),
            )
            self.assertFalse(row["site_aggregation_is_an_isometry"])

    def test_held_out_positive_chart_retains_fourth_power_contractions(self):
        self.assertEqual(self.positive["complete_factor_count"], 720)
        self.assertEqual(sorted(self.positive["exponents"]), [1, 1, 1, 1, 2, 2, 4])
        self.assertEqual(self.positive["complete_stripped_coefficient"], "0")
        self.assertTrue(
            any(
                e == 4 and a == 2
                for row in self.positive["coalesced_patterns"]
                for e, a in row["pattern"]
            )
        )

    def test_primewise_schedule_chain_rule_changes_only_antisymmetric_area(self):
        rows = [M.deformation_control(k) for k in (1, 2, 3)]
        self.assertEqual([r["antisymmetric_p_q"] for r in rows], ["0", "-1/12", "-1/8"])
        for row in rows:
            self.assertEqual(row["complete_endpoint"], "1")
            self.assertEqual(row["symmetric_each"], "1/4")
            self.assertFalse(row["original_product_current_changes"])
        self.assertTrue(rows[1]["positive_ratio_energy_changes"])

    def test_source_authentication_and_typed_replay_reject_counterfeits(self):
        key = (
            M.OLD,
            "claims/lemmas/L-102707-continuous-half-divisor-geodesic-and-polarized-hankel-current.md",
        )
        with (
            patch.dict(M.SOURCES, {key: "0" * 40}),
            self.assertRaisesRegex(ValueError, "authentication"),
        ):
            M.source_bytes(key)
        expected = {"count": 1, "coefficient": "0"}
        for bad in (True, 1.0):
            candidate = copy.deepcopy(expected)
            candidate["count"] = bad
            with self.assertRaisesRegex(ValueError, "typed canonical"):
                M.replay_equal(candidate, expected)

    def test_resource_and_nonprime_guards_remain_active_under_optimization(self):
        for bad in (True, 1.0, -1, 5):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                M.local(bad)
        for bad in (0, 4, True):
            with self.subTest(schedule=bad), self.assertRaises(ValueError):
                M.deformation_control(bad)
        with self.assertRaises(ValueError):
            M.factor_control((3, 9), (1, 1), 3)
        with self.assertRaises(ValueError):
            M.factor_control((2, 3, 5, 7, 11, 13), (4, 4, 4, 4, 4, 4), 2)


if __name__ == "__main__":
    unittest.main()
