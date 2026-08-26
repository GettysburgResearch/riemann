from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_quintic_growing_marked_place_phase_diagram.py"
)
SPEC = importlib.util.spec_from_file_location("growing_marks", MODULE_PATH)
assert SPEC and SPEC.loader
growing_marks = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(growing_marks)


class QuadraticQuinticGrowingMarkedPlacePhaseDiagramTest(unittest.TestCase):
    def test_stable_formula_symbolically(self) -> None:
        exterior_rows = ((1, 3, -2, 5, 7), (4, -1, 6, 2, -3))
        for mark_count in range(11, 25):
            for q in (29, 31):
                for exterior in exterior_rows:
                    self.assertTrue(
                        growing_marks.verify_stable_identity(mark_count, q, exterior)
                    )

    def test_character_dimensions(self) -> None:
        self.assertEqual(growing_marks.character_dimension(5, 1), 10)
        self.assertEqual(growing_marks.character_dimension(5, 2), 44)
        self.assertEqual(growing_marks.character_dimension(5, 5), 132)

    def test_envelope_is_bounded_and_phase_sensitive(self) -> None:
        small = growing_marks.normalized_envelope(1009, 11)
        medium = growing_marks.normalized_envelope(1009, 31)
        large = growing_marks.normalized_envelope(1009, 100)
        self.assertLess(small, medium)
        self.assertLessEqual(medium, large)
        self.assertLessEqual(large, 1.0)

    def test_full_aperture_panel_records_exact_override(self) -> None:
        row = growing_marks.panel(101, 101)
        self.assertEqual(row["full_aperture_exact_value"], 0)
        self.assertEqual(
            growing_marks.panel(101, 50)["full_aperture_exact_value"], None
        )

    def test_guards_and_caps(self) -> None:
        with self.assertRaises(ValueError):
            growing_marks.stable_character_formula(10)
        with self.assertRaises(ValueError):
            growing_marks.normalized_envelope(101, 102)
        with self.assertRaises(ValueError):
            growing_marks.normalized_envelope(15, 11)
        caps = growing_marks.run()["resource_caps"]
        self.assertEqual(caps["finite_fields_enumerated"], 0)
        self.assertLessEqual(caps["symbolic_identity_rows"], 100)


if __name__ == "__main__":
    unittest.main()
