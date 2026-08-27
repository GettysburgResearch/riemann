from __future__ import annotations

import importlib.util
import json
import subprocess
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_multicolor_rough_witt_phase_surface.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("multicolor_rough_witt", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load multicolor rough-Witt producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldMulticolorRoughWittPhaseSurfaceTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_removed_and_rough_products_reassemble(self) -> None:
        for colors, q, maximum_degree in ((2, 5, 5), (3, 11, 4)):
            complete = subject.source.direct_product(colors, q, maximum_degree)
            for cutoff in range(3):
                removed = subject.removed_product(colors, q, cutoff, maximum_degree)
                rough = subject.rough_product(colors, q, cutoff, maximum_degree)
                self.assertEqual(
                    subject.source.multiply_truncated(removed, rough, maximum_degree),
                    complete,
                )

    def test_rough_support_starts_above_cutoff(self) -> None:
        rough = subject.rough_product(3, 11, 2, 4)
        self.assertFalse(any(degree in (1, 2) for degree, _phase in rough))
        self.assertTrue(any(degree == 3 for degree, _phase in rough))

    def test_conditioning_is_exact_and_increasing(self) -> None:
        radius = Fraction(8, 25)
        rows = [
            subject.conditioning_inverse(3, 11, cutoff, radius)
            for cutoff in range(1, 4)
        ]
        self.assertTrue(all(left < right for left, right in pairwise(rows)))
        self.assertGreater(rows[0], 1)
        self.assertEqual(
            subject.conditioning_inverse(3, 11, 0, radius),
            1,
        )

    def test_extreme_cutoffs_are_exact(self) -> None:
        colors, q, maximum_degree = 3, 11, 4
        complete = subject.source.direct_product(colors, q, maximum_degree)
        self.assertEqual(
            subject.removed_product(colors, q, maximum_degree, maximum_degree),
            complete,
        )
        self.assertEqual(
            subject.rough_product(colors, q, maximum_degree, maximum_degree),
            {(0, (0,) * colors): 1},
        )

    def test_binary_specialization_of_conditioning(self) -> None:
        radius = Fraction(9, 20)
        expected = Fraction(1)
        for degree in range(1, 3):
            expected *= (1 - 2 * radius**degree) ** (
                -subject.source.irreducible_count(5, degree)
            )
        self.assertEqual(
            subject.conditioning_inverse(2, 5, 2, radius),
            expected,
        )

    def test_control_lies_between_both_radii(self) -> None:
        panel = subject.control_panel()
        self.assertTrue(panel["exact_reassembly"])
        self.assertGreater(
            subject.CONTROL_Q * subject.CONTROL_RADIUS**2,
            1,
        )
        self.assertLess(
            subject.CONTROL_COLORS * subject.CONTROL_RADIUS,
            1,
        )

    def test_fixture_and_scope(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["color_square_and_depth_two_subfrontier"],
            "PROVED",
        )
        self.assertEqual(
            fixture["proof_ledger"]["actual_sharp_rough_coefficient_frontier"],
            "NOT CLAIMED",
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.validate_cutoff(2, 3)
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(3, 11, -1, Fraction(1, 4))
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(3, 11, 1, Fraction(1, 3))
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(3, 11, 1, Fraction(-1, 4))
        with self.assertRaises(ValueError):
            subject.degree_range_product(3, 11, 0, 2, 4)
        with self.assertRaises(ValueError):
            subject.degree_range_product(3, 11, 4, 2, 4)


if __name__ == "__main__":
    unittest.main()
