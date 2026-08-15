import sys
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import verify  # noqa: E402


class CanonicalFactor67Tests(unittest.TestCase):
    def test_main(self):
        self.assertEqual(
            verify.verify()["verdict"],
            "PASS_CANONICAL_FACTOR67_ONE_SHOT_NATIVE_ENDPOINT_ALGEBRA",
        )

    def test_duplicate_child_rejected(self):
        with self.assertRaises(AssertionError):
            verify.common_parent_check("duplicate_child")

    def test_duplicate_source_rejected(self):
        with self.assertRaises(AssertionError):
            verify.common_parent_check("duplicate_source")

    def test_child_port_rejected(self):
        with self.assertRaises(AssertionError):
            verify.common_parent_check("child_port")

    def test_missing_slack_rejected(self):
        with self.assertRaises(AssertionError):
            verify.common_parent_check("drop_slack")

    def test_bad_coefficient_budget_rejected(self):
        with self.assertRaises(AssertionError):
            verify.hereditary_check("non_subcritical")

    def test_child_requantization_rejected(self):
        with self.assertRaises(AssertionError):
            verify.one_shot_check("requantize_child")

    def test_bad_y4_support_rejected(self):
        with self.assertRaises(AssertionError):
            verify.native_cost_check("y4_support")

    def test_benchmark_bridge_rejected(self):
        with self.assertRaises(AssertionError):
            verify.native_cost_check("benchmark_bridge")

    def test_missing_prime_square_moat_rejected(self):
        with self.assertRaises(AssertionError):
            verify.endpoint_check("remove_moat")


if __name__ == "__main__":
    unittest.main()
