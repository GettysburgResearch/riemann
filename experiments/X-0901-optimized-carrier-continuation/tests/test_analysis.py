from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


analysis = load_module("x0901_analysis", ROOT / "analysis.py")
xi = load_module("x0901_xi", ROOT / "xi_crosscheck.py")


class ContinuationAuditTests(unittest.TestCase):
    def test_summary_counts_and_candidate_boundary(self) -> None:
        data = json.loads((ROOT / "results" / "continuation-summary.json").read_text())
        messages = analysis.validate_continuation_summary(data)
        self.assertEqual(len(messages), 5)
        self.assertTrue(all(float(row["leading_margin"]) > 0 for row in data["cells"]))

    def test_taylor_remainder_regression(self) -> None:
        value = analysis.taylor_remainder_bound(
            493.7546104558693,
            0.01,
            math.log(10**10),
            6,
        )
        self.assertAlmostEqual(value, 4.2324364738445655e-06, places=18)
        self.assertEqual(
            analysis.taylor_remainder_bound(493.7546104558693, 0.0, math.log(10), 6),
            0.0,
        )

    def test_no_remainder_curvature_regression(self) -> None:
        row = xi.approximate_critical_curvature("1000000")
        self.assertEqual(row["riemann_siegel_terms"], 398)
        self.assertAlmostEqual(
            float(row["curvature_no_remainder"]), 34.71809572831903, places=10
        )

    def test_simultaneous_zeta_matches_mpmath_at_moderate_height(self) -> None:
        import mpmath as mp

        with mp.workdps(35):
            s = mp.mpf("0.61") + mp.j * mp.mpf("10000")
            zeta, _ = xi.simultaneous_zeta_and_derivative(s)
            self.assertLess(abs(zeta - mp.zeta(s)), mp.mpf("1e-25"))


if __name__ == "__main__":
    unittest.main()
