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
    / "ffps_primitive_core_wavelet_closure.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("ffps_primitive_core_wavelet_closure", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PrimitiveCoreWaveletClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = MODULE.run(check_sources=False)

    def test_canonical_fixture(self) -> None:
        expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(self.result, expected)

    def test_full_panel_and_core_inverse(self) -> None:
        replay = self.result["finite_replay"]
        self.assertTrue(replay["full_panel_identity"])
        self.assertEqual({row["alpha"] for row in replay["rows"]}, {0, 1, 2})
        self.assertTrue(all(row["core_inversion_checks"] == 4 for row in replay["rows"]))

    def test_support_and_cost(self) -> None:
        self.assertGreater(self.result["support_replay"]["factor_64_shell_checks"], 0)
        self.assertTrue(self.result["assembly_cost_replay"]["exact_reindexing"])
        self.assertTrue(
            self.result["inverse_assembly_cost_replay"][
                "inverse_condition_number_is_polylogarithmic_up_to_tau_s_squared"
            ]
        )

    def test_scope_firewall(self) -> None:
        firewall = self.result["scope_firewall"]
        self.assertFalse(firewall["corewave_proved"])
        self.assertFalse(firewall["coreagg_estimate_proved"])
        self.assertTrue(firewall["coreagg_primcar_equivalence_proved"])
        self.assertFalse(firewall["primcar_proved"])
        self.assertFalse(firewall["rh_or_grh_proved"])
        self.assertTrue(firewall["controls_entire_primitive_panel_algebraically"])


if __name__ == "__main__":
    unittest.main()
