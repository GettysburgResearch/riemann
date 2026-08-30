from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
MODULE_DIR = ROOT / "research/l-families/atlas/function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

import ffps_relative_phase_stratified_externalization as packet  # noqa: E402


class RelativePhaseExternalizationTests(unittest.TestCase):
    def test_phase_factorizes_at_fixed_labels(self) -> None:
        panel = packet.phase_factorization_panel()
        self.assertEqual(panel["fixed_label_external_rank"], 1)

    def test_coprimality_externalizes_exactly(self) -> None:
        panel = packet.coprimality_panel()
        self.assertEqual(len(panel["rows"]), 3)
        for row in panel["rows"]:
            self.assertEqual(row["direct"], row["external"])

    def test_mixed_phase_rank_grows(self) -> None:
        panel = packet.mixed_fourier_gram_panel()
        self.assertFalse(panel["bounded_rank_as_prime_grows"])
        self.assertEqual(panel["rows"][-1]["rank"], 10)

    def test_scope_firewall(self) -> None:
        rendered = packet.run(check_sources=False)
        self.assertFalse(rendered["scope_firewall"]["relpartfrob_proved"])
        self.assertFalse(rendered["scope_firewall"]["rh_or_grh_proved"])


if __name__ == "__main__":
    unittest.main()
