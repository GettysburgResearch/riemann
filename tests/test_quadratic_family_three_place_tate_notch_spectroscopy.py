from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_three_place_tate_notch_spectroscopy.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("three_place_tate_notch", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load three-place Tate-notch producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class ThreePlaceTateNotchSpectroscopyTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_elliptic_trace_towers(self) -> None:
        self.assertEqual(
            subject.elliptic_trace_tower(3, 0, 6), (2, 0, -6, 0, 18, 0, -54)
        )
        self.assertEqual(subject.elliptic_trace_tower(5, -2, 4), (2, -2, -6, 22, -14))
        with self.assertRaises(ValueError):
            subject.elliptic_trace_tower(3, 4, 5)

    def test_universal_notch_kills_every_orientation_profile(self) -> None:
        for prime, epsilon in ((3, -1), (5, 1)):
            for deltas in itertools.product((-1, 1), repeat=3):
                nuisance = tuple(
                    subject.nuisance_value(degree, prime, epsilon, deltas)
                    for degree in range(12)
                )
                self.assertTrue(
                    all(
                        subject.notch_value(nuisance, degree, prime) == 0
                        for degree in range(8)
                    )
                )

    def test_notch_polynomial_has_exact_signed_tate_roots(self) -> None:
        for prime in (3, 5):
            self.assertEqual(
                {
                    root
                    for root in range(-prime, prime + 1)
                    if (root**2 - 1) * (root**2 - prime**2) == 0
                },
                {-prime, -1, 1, prime},
            )

    def test_notched_total_equals_geometric_channel(self) -> None:
        for prime, trace, epsilon in ((3, 0, -1), (5, -2, 1)):
            traces = subject.elliptic_trace_tower(prime, trace, 20)
            deltas = (1, -1, 1)
            nuisance = tuple(
                subject.nuisance_value(degree, prime, epsilon, deltas)
                for degree in range(20)
            )
            geometric = tuple(
                subject.geometric_value(degree, prime, traces) for degree in range(20)
            )
            total = tuple(a + b for a, b in zip(nuisance, geometric, strict=True))
            self.assertEqual(
                tuple(
                    subject.notch_value(total, degree, prime) for degree in range(16)
                ),
                tuple(
                    subject.notch_value(geometric, degree, prime)
                    for degree in range(16)
                ),
            )

    def test_rank_four_recurrence_and_trace_recovery(self) -> None:
        for prime, trace, epsilon in ((3, 0, -1), (5, -2, 1)):
            row = subject.control_panel(prime, trace, epsilon, (1, -1, 1))
            coefficients = tuple(row["characteristic_low_to_high"])
            self.assertEqual(coefficients[-1], 1)
            self.assertEqual(-coefficients[3] // (prime + 1), trace)
            self.assertEqual(row["hankel_rank"], 4)
            self.assertTrue(row["nuisance_notch_zero"])

    def test_characteristic_formula(self) -> None:
        self.assertEqual(subject.characteristic_polynomial(3, 0), (81, 0, 30, 0, 1))
        self.assertEqual(
            subject.characteristic_polynomial(5, -2), (625, 300, 150, 12, 1)
        )

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.orientation_sum(1, (1, 0, -1))
        with self.assertRaises(ValueError):
            subject.notch_value((1, 2, 3), 0, 3)
        with self.assertRaises(ValueError):
            subject.recurrence_holds((1, 2, 3), (1, 1, 1))
        for invalid in (True, 1, 4, 9, 15):
            with self.assertRaises(ValueError):
                subject.validate_base(invalid, 0)

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
        self.assertEqual(fixture["proof_ledger"]["elliptic_isolation"], "PROVED EXACT")
        self.assertEqual(
            fixture["proof_ledger"]["new_sheaf_or_cohomology_class"], "NOT CLAIMED"
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")
        self.assertEqual(fixture["theorem"]["universal_notch"], "(E^2-1)(E^2-p^2)")


if __name__ == "__main__":
    unittest.main()
