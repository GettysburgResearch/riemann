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
    / "function_field_witt_rough_sieve_frontier.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("witt_rough_frontier", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Witt rough-frontier producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldWittRoughSieveFrontierTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_removed_and_rough_factors_reassemble(self) -> None:
        for cutoff in range(4):
            complete = subject.source.direct_euler_product(5, 7)
            removed = subject.removed_product(5, cutoff, 7)
            rough = subject.rough_product(5, cutoff, 7)
            self.assertEqual(
                subject.source.multiply_truncated(removed, rough, 7),
                complete,
            )

    def test_rough_support_begins_above_cutoff(self) -> None:
        rough = subject.rough_product(5, 2, 8)
        self.assertFalse(any(degree in (1, 2) for degree, _phase in rough))
        self.assertTrue(any(degree == 3 for degree, _phase in rough))

    def test_conditioning_inverse_is_exact_and_increasing(self) -> None:
        radius = Fraction(9, 20)
        rows = [
            subject.conditioning_inverse(5, cutoff, radius) for cutoff in range(1, 4)
        ]
        self.assertTrue(all(left < right for left, right in pairwise(rows)))
        self.assertGreater(rows[0], 1)

    def test_control_radius_is_critical_and_subhalf(self) -> None:
        self.assertLess(subject.CONTROL_RADIUS, Fraction(1, 2))
        self.assertGreater(subject.CONTROL_Q * subject.CONTROL_RADIUS**2, 1)
        panel = subject.control_panel()
        self.assertTrue(panel["exact_reassembly"])

    def test_fixture_and_scope(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=15,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["exponent_two_subfrontier"],
            "PROVED FOR THE COMPLETE DEGREE SHELL",
        )
        self.assertEqual(
            fixture["proof_ledger"]["sharp_actual_rough_coefficient_frontier"],
            "NOT CLAIMED",
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.validate_cutoff(2, 3)
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(5, -1, Fraction(1, 3))
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(1, 0, Fraction(1, 3))
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(5, 2, Fraction(1, 2))
        with self.assertRaises(ValueError):
            subject.conditioning_inverse(5, 2, Fraction(-1, 3))


if __name__ == "__main__":
    unittest.main()
