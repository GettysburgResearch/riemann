from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_mollified_complete_source_adapter.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_MOLLIFIED_COMPLETE_SOURCE_ADAPTER.md")
SPEC = importlib.util.spec_from_file_location("mollified_source_adapter", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load mollified source adapter replay")
mollified_source_adapter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mollified_source_adapter)


class FfpsMollifiedCompleteSourceAdapterTest(unittest.TestCase):
    def test_frozen_source_blobs(self) -> None:
        mollified_source_adapter.check_source_blobs()

    def test_kernel_identity(self) -> None:
        for s in (2, 3, 5, 7):
            left, right = mollified_source_adapter.kernel_identity_sample(s)
            self.assertEqual(left, right)
        with self.assertRaises(ValueError):
            mollified_source_adapter.kernel_identity_sample(True)
        with self.assertRaises(ValueError):
            mollified_source_adapter.kernel_identity_sample(1)

    def test_type_i_exponents(self) -> None:
        exponents = mollified_source_adapter.type_i_exponents()
        self.assertEqual(exponents["unrestricted_lattice"], Fraction(-1, 2))
        self.assertEqual(exponents["squarefree_lattice"], Fraction(-1, 4))
        self.assertEqual(exponents["final_boolean_type_i"], Fraction(-1, 12))

    def test_duplicate_67_beta_scaling(self) -> None:
        self.assertEqual(
            mollified_source_adapter.duplicate_67_coefficients(),
            {0: 1, 1: -2, 2: 1},
        )

    def test_complete_scope(self) -> None:
        result = mollified_source_adapter.run()
        self.assertEqual(len(result["closure_rows"]), 7)
        adapter = result["adapter"]
        self.assertEqual(adapter["name"], "MEXTSRC106150")
        self.assertIn("not proved", adapter["status"])
        self.assertEqual(adapter["missing_source_gate"], "NATCOMP-MOLL106150")
        self.assertIn("remains open", adapter["mollified_one_sided_gate"])
        scope = result["scope"]
        self.assertFalse(scope["equal_and_one_sided_balanced_sectors_deleted"])
        self.assertFalse(scope["ordinary_self_convolution_used"])
        self.assertFalse(scope["anti_causal_future_used"])
        self.assertFalse(scope["multiplicative_gauge_spent_as_additive_error"])
        self.assertFalse(scope["mextsrc_proved"])
        self.assertFalse(scope["raw_wksfsc_bound_to_piecewise_gate"])
        self.assertFalse(scope["rh_proved"])

    def test_source_path_records_open_bridge(self) -> None:
        path = mollified_source_adapter.source_path_disposition()
        open_steps = [row for row in path if row["status"].startswith("open:")]
        self.assertEqual(len(open_steps), 1)
        self.assertIn("x_p x_q y_C", open_steps[0]["step"])
        self.assertIn("NATCOMP-MOLL106150", open_steps[0]["status"])

    def test_horizon_semantic_fence(self) -> None:
        result = mollified_source_adapter.run()
        horizon = result["horizon"]
        self.assertIn("half-open", horizon["endpoint_atoms"])
        self.assertIn("not established", horizon["frozen_wksfsc_binding"])
        self.assertIn("[0,T]", horizon["finite_horizon_contraction"])

    def test_display_math_delimiters_are_balanced(self) -> None:
        depth = 0
        for line in NOTE_PATH.read_text(encoding="utf-8").splitlines():
            if line == r"\[":
                depth += 1
                self.assertEqual(depth, 1)
            elif line == r"\]":
                depth -= 1
                self.assertGreaterEqual(depth, 0)
        self.assertEqual(depth, 0)

    def test_note_has_no_disallowed_control_characters(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        disallowed = [char for char in note if ord(char) < 32 and char not in "\n\t"]
        self.assertEqual(disallowed, [])

    def test_note_does_not_promote_adapter(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        self.assertIn("`MEXTSRC106150` is not proved", note)
        self.assertIn("NATCOMP-MOLL106150", note)
        self.assertNotIn("source adapter is\nproved", note)

    def test_resource_caps(self) -> None:
        caps = mollified_source_adapter.run()["resource_caps"]
        self.assertEqual(caps["mellin_samples"], 3)
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["conductors_enumerated"], 0)
        self.assertEqual(caps["curves_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
