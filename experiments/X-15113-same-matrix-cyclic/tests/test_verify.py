import importlib.util
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
VERIFY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VERIFY)


def load(name):
    return json.loads((ROOT / "certificates" / name).read_text())


class SameMatrixCyclicTests(unittest.TestCase):
    def test_graded_all_orders_pass(self):
        out = VERIFY.verify(load("graded-cyclic-pass.json"))
        self.assertEqual(out["status"], "CERTIFIED_GRADED_SAME_MATRIX_ALL_ORDERS")
        self.assertEqual(out["direct_order_three"], 0)
        self.assertEqual(out["trace_moments"]["3"], 0)
        self.assertEqual(out["basis_invariance"], "PASS")

    def test_gram_omission_obstruction(self):
        out = VERIFY.verify(load("gram-omission-obstruction.json"))
        self.assertEqual(out["true_gram_cyclic_cubic"], 1)
        self.assertEqual(out["naive_seam_cubic"], 64)

    def test_compression_leakage_obstruction(self):
        out = VERIFY.verify(load("compression-leakage-obstruction.json"))
        self.assertEqual(out["compressed_cubic"], {"numerator": 64, "denominator": 125})

    def test_same_side_seam_mutation_rejected(self):
        data = load("graded-cyclic-pass.json")
        data["seam"][0][0] = 1
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_wrong_trace_rejected(self):
        data = load("graded-cyclic-pass.json")
        data["trace_moments"]["4"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_wrong_transformed_gram_rejected(self):
        data = load("graded-cyclic-pass.json")
        data["transformed_gram"][0][0] = 2
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_boolean_injection_rejected(self):
        data = load("graded-cyclic-pass.json")
        data["gram"][0][0] = True
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_nonpositive_gram_rejected(self):
        data = load("graded-cyclic-pass.json")
        data["gram"][0][0] = -1
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_singular_basis_change_rejected(self):
        data = load("graded-cyclic-pass.json")
        data["basis_change"][3] = [0, 0, 0, 0]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_false_zero_compressed_cubic_rejected(self):
        data = load("compression-leakage-obstruction.json")
        data["compressed_cubic"] = 0
        with self.assertRaises(ValueError):
            VERIFY.verify(data)

    def test_projection_preserving_grading_not_an_obstruction(self):
        data = load("compression-leakage-obstruction.json")
        data["projection"] = [[1, 0], [0, 0]]
        with self.assertRaises(ValueError):
            VERIFY.verify(data)


if __name__ == "__main__":
    unittest.main()
