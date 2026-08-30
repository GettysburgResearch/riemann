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
    / "ffps_primitive_core_gcd_gram_closure.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location(
    "ffps_primitive_core_gcd_gram_closure", SCRIPT
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class PrimitiveCoreGcdGramClosureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = MODULE.run(check_sources=False)

    def test_canonical_fixture(self) -> None:
        expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(self.result, expected)

    def test_exact_gram_and_gcd_forms(self) -> None:
        replay = self.result["exact_gram_replay"]
        self.assertTrue(replay["core_energy_equals_shared_divisor_gram"])
        self.assertTrue(replay["diagonal_off_diagonal_split"])
        self.assertTrue(replay["off_diagonal_equals_exact_gcd_form"])
        self.assertEqual(len(replay["rows"]), 4)

    def test_kernel_and_diagonal(self) -> None:
        feature = self.result["feature_gram_replay"]
        self.assertTrue(feature["feature_gram_reconstruction"])
        self.assertEqual(feature["local_condition_number_asymptotic"], "2p")
        diagonal = self.result["diagonal_majorant_replay"]
        self.assertGreater(diagonal["checked_product_shells"], 0)
        self.assertEqual(
            self.result["diagonal_theorem"]["status"], "proved unconditionally"
        )

    def test_scope_firewall(self) -> None:
        firewall = self.result["scope_firewall"]
        self.assertFalse(firewall["offgcdwave_proved"])
        self.assertFalse(firewall["coreagg_proved"])
        self.assertFalse(firewall["primcar_proved"])
        self.assertFalse(firewall["rh_or_grh_proved"])
        self.assertFalse(firewall["architecture_b_claims"])


if __name__ == "__main__":
    unittest.main()
