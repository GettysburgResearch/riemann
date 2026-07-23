import json
import unittest
from pathlib import Path

from phase_budget import uniform_phase_budget


class PhaseBudgetTests(unittest.TestCase):
    def test_invalid(self):
        for values in ((1, 1, 1), (1, -1, 1), (1, 0, 0)):
            with self.assertRaises(ValueError):
                uniform_phase_budget(*values)

    def test_frozen_budget(self):
        radius = uniform_phase_budget(
            0.0006076603725748697,
            4.424813255620086e-10,
            493.7546104558693,
        )
        self.assertGreater(radius, 1.2e-6)
        self.assertLess(radius, 1.3e-6)

    def test_result_positive(self):
        path = Path(__file__).parents[1] / "results" / "phase-summary.json"
        data = json.loads(path.read_text())
        self.assertGreater(
            data["complete_c1e8_backend_comparison"]["binary128_phase_kahan_margin"],
            0,
        )
        self.assertIsNone(data["counterexample_candidate"])


if __name__ == "__main__":
    unittest.main()
