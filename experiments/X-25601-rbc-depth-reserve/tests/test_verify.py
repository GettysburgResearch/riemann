import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify256", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VERIFY)


class TestRBCDepthReserve(unittest.TestCase):
    def setUp(self):
        self.result = VERIFY.verify_core()

    def test_exact_core(self):
        self.assertTrue(self.result["matrix_inverse"])
        self.assertTrue(self.result["matrix_log_derivative"])
        self.assertEqual(self.result["forward_shift_anchor"], "e_(K-1)")

    def test_nonzero_endpoint_tail(self):
        self.assertEqual(self.result["tail"], "1/45")

    def test_zero_schur_reserve(self):
        self.assertEqual(self.result["aggregate_schur_reserve"], "0")
        self.assertNotEqual(self.result["packet_kernel_control"], "0")

    def test_color_parseval(self):
        self.assertEqual(
            self.result["color_energy"], self.result["depth_parseval_energy"]
        )

    def test_charge_conservation(self):
        self.assertEqual(self.result["meromorphic_quotient_rank"], 1)
        self.assertEqual(self.result["base_pole_order"], 2)
        self.assertGreaterEqual(self.result["killed_residual_order"], 0)

    def test_far_right_barrier(self):
        self.assertEqual(self.result["far_right_physical_exponent"], "1/2")

    def test_rank_scale_distinction(self):
        self.assertGreater(
            self.result["anchor_shell_count_control"],
            self.result["V_scale_control"],
        )

    def test_all_mutations(self):
        tests = VERIFY.run_mutations(self.result)
        self.assertEqual(len(tests), 8)


if __name__ == "__main__":
    unittest.main()
