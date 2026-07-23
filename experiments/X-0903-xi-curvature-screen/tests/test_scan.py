import json
import unittest
from pathlib import Path

from batch_scan import scan
from xi_differential import evaluate, simultaneous_zeta_derivatives


class ScanTests(unittest.TestCase):
    def test_invalid_batch_parameters(self):
        with self.assertRaises(ValueError):
            scan(1, 0, 10, 20, 1)

    def test_committed_summary_has_no_candidate(self):
        path = Path(__file__).parents[1] / "results" / "curvature-summary.json"
        data = json.loads(path.read_text())
        self.assertEqual(data["total_points"], 5701)
        self.assertEqual(data["negative_count"], 0)
        self.assertIsNone(data["counterexample_candidate"])

    def test_simultaneous_derivatives_match_mpmath_control(self):
        import mpmath as mp
        with mp.workdps(20):
            s = mp.mpf("0.501") + mp.j * mp.mpf("1e8")
            values = simultaneous_zeta_derivatives(s)
            for derivative, value in enumerate(values):
                reference = mp.zeta(s, derivative=derivative)
                relative = abs(value-reference) / max(1, abs(reference))
                self.assertLess(relative, mp.mpf("1e-8"))

    def test_differential_rejects_nonpositive_offset(self):
        with self.assertRaises(ValueError):
            evaluate("0", "100000000", 20)


if __name__ == "__main__":
    unittest.main()
