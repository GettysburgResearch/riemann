"""Source-derived cusp, all eight factor modes, and a fixed admissible path."""

import importlib.util
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "native-six-hour"
    / "clustered_native_activation_selection.py"
)
SPEC = importlib.util.spec_from_file_location("native_six_hour_cluster_selection", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class NativeClusterSelectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kernel, cls.geodesic = M.modules()
        cls.primes = (71, 73, 79)
        cls.panel = M.panel(cls.kernel, cls.geodesic, cls.primes)

    def test_literal_jump_cusp_and_exact_second_derivative_endpoints(self):
        certificate = M.cusp_certificate(self.kernel)
        self.assertEqual(certificate["jump_squared_half_sum"], ["144", "64"])
        self.assertEqual(certificate["Gamma_second_derivative_at_0"], -72)
        self.assertEqual(certificate["Gamma_second_derivative_at_log2"], 48)
        self.assertEqual(certificate["Taylor_remainder_constant"], 36)

    def test_closed_formula_equals_independent_primitive_overlap(self):
        for ratio in (F(1), F(73, 71), F(79, 73), F(79, 71)):
            a = M.normalize_logs(
                self.kernel, M.closed_gamma(self.kernel, ratio), self.primes
            )
            b = M.normalize_logs(
                self.kernel, self.kernel.gamma_square_ratio(ratio), self.primes
            )
            self.assertEqual(a, b)

    def test_all_native_factors_and_derivative_sites_remain(self):
        for key in (
            "all_eight_uniform_source_records",
            "all_eight_selected_source_records",
        ):
            records = self.panel[key]
            self.assertEqual(len(records), 8)
            self.assertEqual(sum(len(row["sites"]) for row in records), 12)
            self.assertEqual(sum(F(row["coefficient"]) for row in records), -1)
            self.assertEqual(records[0]["coefficient"], "0")
            self.assertEqual(records[-1]["coefficient"], "-1/4")

    def test_selected_path_is_fixed_one_two_one_not_fitted_coefficients(self):
        self.assertEqual(self.panel["selected_source_powers"], (1, 2, 1))
        singleton = {
            row["n"]: F(row["coefficient"])
            for row in self.panel["all_eight_selected_source_records"]
            if row["cardinality"] == 1
        }
        self.assertEqual(singleton, {71: F(-1, 16), 73: F(-1, 8), 79: F(-1, 16)})

    def test_full_source_energy_equals_band_formula(self):
        uniform = M.full_energy(
            self.kernel, self.primes, self.panel["all_eight_uniform_source_records"]
        )
        self.assertEqual(
            uniform, M.band_energy(self.kernel, self.primes, (F(1, 3),) * 3)
        )
        self.assertNotEqual(uniform, self.kernel.expr())

    def test_strict_actual_energy_gain_exceeds_uniform_theorem_bound(self):
        gap = self.panel["certified_improvement_interval"]
        lower = self.panel["theorem_lower_bound_interval"]
        self.assertGreater(F(gap["lower"]), F(lower["upper"]))
        self.assertGreater(F(lower["lower"]), 0)
        self.assertEqual(self.panel["K"], 71 * 73 * 79)

    def test_second_declared_cluster_with_same_path(self):
        second = M.panel(self.kernel, self.geodesic, (41, 43, 47))
        self.assertEqual(second["selected_source_powers"], (1, 2, 1))
        self.assertGreater(F(second["certified_improvement_interval"]["lower"]), 0)

    def test_domain_guards_do_not_promote_crowded_or_nonprime_panels(self):
        for bad in (
            (3, 5, 7),
            (71, 73, 77),
            (71, 79, 73),
            (71.0, 73, 79),
            (71, 73, 103),
        ):
            with self.assertRaises(ValueError):
                M.validate_primes(bad)
        for ratio in (True, F(3, 2), F(1, 2)):
            with self.assertRaises(ValueError):
                M.closed_gamma(self.kernel, ratio)

    def test_exact_log_relations_and_unknown_factors_rejected(self):
        raw = self.kernel.expr(logs={F(73**2, 2 * 71): self.kernel.q(3, 4)})
        expected = self.kernel.expr(
            logs={
                F(73): self.kernel.q(6, 8),
                F(2): self.kernel.q(-3, -4),
                F(71): self.kernel.q(-3, -4),
            }
        )
        self.assertEqual(M.normalize_logs(self.kernel, raw, self.primes), expected)
        with self.assertRaises(ValueError):
            M.normalize_logs(
                self.kernel,
                self.kernel.expr(logs={F(11): self.kernel.q(1)}),
                self.primes,
            )

    def test_typed_json_and_exact_frozen_code_authentication(self):
        with self.assertRaises(ValueError):
            M.replay_equal({"count": 8}, {"count": 8.0})
        with patch.object(M, "KERNEL_BLOB", "0" * 40), self.assertRaises(ValueError):
            M.modules()


if __name__ == "__main__":
    unittest.main()
