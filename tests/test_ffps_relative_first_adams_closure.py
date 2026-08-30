from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_relative_first_adams_closure.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("ffps_relative_first_adams_closure", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RelativeFirstAdamsClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = MODULE.run(check_sources=False)

    def test_canonical_fixture(self) -> None:
        expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(self.result, expected)

    def test_relative_character_profiles(self) -> None:
        algebra = self.result["character_algebra"]
        self.assertTrue(algebra["hard_minus_selected_equals_relative"])
        self.assertTrue(algebra["partial_adams_preserves_difference"])
        profiles = algebra["four_physical_parity_profiles"]
        self.assertEqual(len(profiles), 4)
        self.assertEqual({row["line_mass"] for row in profiles}, {"16"})
        self.assertEqual({row["distinct_lines"] for row in profiles}, {1, 4, 16})

    def test_closed_point_extraction(self) -> None:
        replay = self.result["closed_point_adams"]
        self.assertEqual(replay["one_place_checks"], 12)
        self.assertEqual(replay["two_place_checks"], 144)
        self.assertEqual(replay["diagonal_correction_checks"], 3)

    def test_scope_firewall(self) -> None:
        firewall = self.result["scope_firewall"]
        self.assertFalse(firewall["native_source_adapter_constructed"])
        self.assertFalse(firewall["relative_partial_frobenius_proved"])
        self.assertFalse(firewall["uniform_betti_or_trace_estimate_proved"])
        self.assertFalse(firewall["rh_or_grh_proved"])
        self.assertTrue(firewall["physical_profiles_do_not_control_non_deck_adams_eigenvalues"])


if __name__ == "__main__":
    unittest.main()
