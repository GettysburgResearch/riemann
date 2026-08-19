from __future__ import annotations

import importlib.util
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify", ROOT / "verify.py")
verify = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(verify)


class TestT99000(unittest.TestCase):
    def test_invsqrt_brackets(self):
        for n in list(range(1, 1000)) + [48433, 99991]:
            q = verify.invsqrt_floor(n)
            self.assertLessEqual(q * q * n, verify.SCALE2)
            self.assertGreater((q + 1) * (q + 1) * n, verify.SCALE2)

    def test_sparse_dictionary(self):
        self.assertEqual(verify.sparse_dictionary_check(500), 500)

    def test_exact_minimum_through_100k(self):
        result = verify.exact_prefix_scan(100_000)
        self.assertEqual(result["min_lower_num"], 1226685126915)
        self.assertEqual(result["min_lower_at"], 48433)
        self.assertGreater(result["min_lower_num"], 0)

    def test_retained_full_transcript(self):
        got = verify.parse_retained(ROOT / "results" / "cprefix_exact_1e9.txt")
        for key, expected in verify.EXPECTED_FULL.items():
            self.assertEqual(got[key], expected)

    def test_finite_pointwise_port_is_negative(self):
        lo, hi, scale = verify.finite_threshold_counterexample()
        self.assertLess(lo, hi)
        self.assertLess(hi, 0)
        self.assertLess(hi / scale, -0.1306)

    def test_status_fail_closed(self):
        import json
        result = json.loads((ROOT / "results" / "verification.json").read_text())
        self.assertTrue(result["status"]["primitive_prefix_through_1e9"])
        self.assertFalse(result["status"]["c4mbi67_global_sign"])
        self.assertFalse(result["status"]["rh_established"])


if __name__ == "__main__":
    unittest.main()
