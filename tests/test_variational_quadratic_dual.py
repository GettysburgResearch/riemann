"""Hostile and source checks for the repaired global quadratic dual."""

import importlib.util
import json
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "research/riemann-structures/native-five-hour-pass/infinite-source"
TARGET = HERE / "variational_quadratic_dual_certificate.py"
spec = importlib.util.spec_from_file_location("tested_quadratic_dual", TARGET)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class QuadraticDualTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = m.build()

    def test_global_status_and_scope(self):
        self.assertEqual(self.result["status"], "CERTIFIED_GLOBAL_ORIGINAL_OPTIMIZER")
        self.assertIs(self.result["global_all_monotone_paths"], True)
        self.assertIs(self.result["full_retained_gamma_identified"], False)

    def test_original_root_artifact_binding(self):
        self.assertEqual(self.result["root_input_sha256"], m.ROOT_SHA)

    def test_corrupted_root_hash_refused(self):
        with (
            patch.object(m, "ROOT_SHA", "0" * 64),
            self.assertRaisesRegex(ValueError, "root artifact"),
        ):
            m.context()

    def test_source_profile_is_actually_lower_clipped(self):
        _arb, _h, _t, u0, _root, _y, _moments, _G = m.context()
        lo, hi = m.base.bounds(u0)
        self.assertGreater(lo, 0)
        self.assertLess(hi, 1)

    def test_lower_clipped_piece_was_executed(self):
        self.assertGreaterEqual(self.result["subdivision"]["clipped_cells"], 1)

    def test_invalid_first_output_is_preserved(self):
        path = HERE / "variational_quadratic_dual.invalid_missing_lower_clip.v1.json"
        self.assertTrue(path.is_file())
        self.assertNotEqual(
            path.read_bytes(),
            (HERE / "variational_quadratic_dual.verification.json").read_bytes(),
        )

    def test_typed_artifact_distinguishes_bool_and_int(self):
        self.assertFalse(
            m.base.typed_equal(
                {"global_all_monotone_paths": True}, {"global_all_monotone_paths": 1}
            )
        )

    def test_degree_holdout_rejects_underdeclared_polynomial(self):
        arb, _h, _t, _u0, _root, _y, _moments, _G = m.context()
        wrong = m.interpolate(0, 1, lambda u, v: u + v + v * v, arb)
        with self.assertRaisesRegex(ValueError, "degree holdout"):
            m.holdout(wrong, lambda u, v: u + v + v * v, arb, "counterfeit")

    def test_bernstein_known_positive_and_negative_controls(self):
        arb, _h, _t, _u0, _root, _y, _moments, _G = m.context()
        eps = m.base.arb_fraction(F(1, 100), arb)
        positive = m.interpolate(2, 2, lambda u, v: u * u + v * v + eps, arb)
        negative = m.interpolate(1, 1, lambda u, v: u - v - eps, arb)
        self.assertGreater(
            m.bernstein_range(positive, (F(0), F(1)), (F(0), F(1)), arb)[0], 0
        )
        self.assertLess(
            m.bernstein_range(negative, (F(0), F(1)), (F(0), F(1)), arb)[0], 0
        )

    def test_subdivision_cap_counterfeit_refused(self):
        with (
            patch.object(m, "CAP", 0),
            self.assertRaisesRegex(ValueError, "cap UNKNOWN"),
        ):
            m.build()

    def test_depth_counterfeit_refused(self):
        with (
            patch.object(m, "MAX_DEPTH", 0),
            self.assertRaisesRegex(ValueError, "UNKNOWN"),
        ):
            m.build()

    def test_current_artifact_has_exact_energy_interval(self):
        data = json.loads(
            (HERE / "variational_quadratic_dual.verification.json").read_text()
        )
        self.assertEqual(data["schema"], "native-quadratic-dual-global-certificate/v1")
        self.assertEqual(len(data["ordered_energy"]), 2)
        self.assertLess(F(data["ordered_energy"][0]), F(data["ordered_energy"][1]))


if __name__ == "__main__":
    unittest.main()
