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
    / "ffps_beta_second_difference_single_channel_reduction.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location(
    "ffps_beta_second_difference_single_channel_reduction", SCRIPT
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BetaSecondDifferenceSingleChannelTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = MODULE.run()

    def test_canonical_fixture(self) -> None:
        expected = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(self.result, expected)

    def test_source_is_a_second_difference(self) -> None:
        for replay in self.result["source_replay"]:
            self.assertGreater(replay["probe_count"], 0)
            self.assertEqual(
                [row["beta"] for row in replay["local_rows"]],
                [1, -2, 1, 0, 0],
            )
            self.assertTrue(
                all(
                    row["beta"] == row["second_difference"]
                    for row in replay["local_rows"]
                )
            )

    def test_sharp_prefix_inverse(self) -> None:
        replay = self.result["prefix_transform_replay"]
        self.assertEqual(len(replay["rows"]), 5)
        self.assertEqual(
            replay["inverse_convolution_first_13"], [1] + [0] * 12
        )
        self.assertTrue(all(row["formal_u_atoms"] > 0 for row in replay["rows"]))

    def test_frequency_annulus_and_sigma_firewall(self) -> None:
        replay = self.result["conditioning_replay"]
        self.assertEqual(
            replay["amplitude_annulus"]["lower"],
            {"rational": "68/67", "sqrt_67": "-2/67"},
        )
        self.assertEqual(
            replay["amplitude_annulus"]["upper"],
            {"rational": "68/67", "sqrt_67": "2/67"},
        )
        self.assertIn("exactly for sigma>0", replay["sigma_phase_boundary"])

    def test_central_panel_reassembly(self) -> None:
        replay = self.result["central_panel_replay"]
        self.assertEqual(replay["X"], 90)
        self.assertEqual({row["H"] for row in replay["rows"]}, {1, 2, 4, 8, 16, 32})
        self.assertTrue(all(row["radical_terms"] > 0 for row in replay["rows"]))

    def test_scope_firewall(self) -> None:
        firewall = self.result["scope_firewall"]
        self.assertTrue(
            firewall["exceptional_positive_gates_shown_unnecessary_for_sufficiency"]
        )
        self.assertFalse(
            firewall["exceptional_positive_gates_implied_by_central_gate"]
        )
        self.assertFalse(firewall["central_coreagg_proved"])
        self.assertFalse(firewall["central_primcar_proved"])
        self.assertFalse(firewall["rh_or_grh_proved"])
        self.assertFalse(firewall["same_prefix_fourier_multiplier_identity_claimed"])

    def test_source_authentication_cannot_be_silently_skipped(self) -> None:
        self.assertTrue(self.result["source_contract"]["frozen_and_working_sources_authenticated"])
        unbound = MODULE.run(check_sources=False)
        self.assertFalse(unbound["source_contract"]["frozen_and_working_sources_authenticated"])
        self.assertNotEqual(unbound, self.result)

    def test_authentication_flag_is_typed(self) -> None:
        with self.assertRaises(TypeError):
            MODULE.run(check_sources=1)

    def test_note_contains_no_embedded_control_bytes(self) -> None:
        raw = MODULE.NOTE_PATH.read_bytes().replace(b"\r\n", b"\n")
        self.assertFalse(any(byte < 32 and byte not in (9, 10) for byte in raw))


if __name__ == "__main__":
    unittest.main()
