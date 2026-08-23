from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest


MODULE_PATH = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("x105200_verify", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PoissonBezoutReplayTests(unittest.TestCase):
    def test_main_payload_passes(self) -> None:
        payload = MODULE.run()
        self.assertEqual(
            payload["classification"],
            "PASS_T105200_POISSON_BEZOUT_RESIDUE_LOCALIZATION",
        )
        self.assertFalse(payload["rh_established"])
        self.assertFalse(payload["entire_bezout_interpolation_proved"])

    def test_retained_fixtures_are_exact(self) -> None:
        payload = MODULE.run()
        self.assertEqual(payload["fixture_count"], 3)
        for fixture in payload["fixtures"]:
            self.assertNotEqual(fixture["cross_residue_debt"], "0")
            self.assertNotEqual(
                fixture["uncorrected_second_boundary"],
                fixture["second_moment"],
            )

    def test_mutated_fixture_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            MODULE.make_fixture(1, 7, 6, 3, 2)


if __name__ == "__main__":
    unittest.main()
