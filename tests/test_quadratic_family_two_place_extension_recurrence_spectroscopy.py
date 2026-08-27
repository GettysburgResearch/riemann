from __future__ import annotations

import importlib.util
import json
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_two_place_extension_recurrence_spectroscopy.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("two_place_spectroscopy", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load two-place spectroscopy producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class TwoPlaceExtensionRecurrenceSpectroscopyTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_exact_polynomial_coefficients(self) -> None:
        rows = subject.base_polynomials()
        for order, expected in subject.EXPECTED_COEFFICIENTS.items():
            self.assertEqual(
                subject.ascending_coefficients(rows[f"P{order}"]), expected
            )
        self.assertEqual(
            subject.ascending_coefficients(rows["Q6"]), subject.EXPECTED_ORIENTATION_6
        )

    def test_clearing_powers_make_every_defect_integral(self) -> None:
        for q in (3, 5, 9, 25, 27):
            for alpha in (-1, 1):
                for epsilon in (-1, 1):
                    for order in range(2, 7):
                        raw = subject.cumulant_defect(q, alpha, epsilon, order)
                        self.assertIsInstance(raw, Fraction)
                        cleared = subject.cleared_defect(q, alpha, epsilon, order)
                        self.assertIsInstance(cleared, int)
        with self.assertRaises(ValueError):
            subject.cumulant_defect(3, 0, 1, 2)
        with self.assertRaises(ValueError):
            subject.cumulant_defect(3, 1, 1, 7)

    def test_spectral_ledgers_equal_extension_tower_defects(self) -> None:
        for prime in (3, 5):
            for alpha in (-1, 1):
                for epsilon in (-1, 1):
                    for order in range(2, 7):
                        spectrum = subject.spectral_ledger(order, prime, alpha, epsilon)
                        for degree in range(1, 7):
                            direct = subject.cleared_defect(
                                prime**degree,
                                alpha**degree,
                                epsilon**degree,
                                order,
                            )
                            self.assertEqual(
                                direct, subject.spectral_value(spectrum, degree)
                            )

    def test_minimal_rank_table_and_signed_tate_roots(self) -> None:
        expected = {
            -1: {2: 2, 3: 4, 4: 7, 5: 14, 6: 16},
            1: {2: 2, 3: 2, 4: 7, 5: 7, 6: 12},
        }
        for epsilon, row in expected.items():
            for alpha in (-1, 1):
                for order, rank in row.items():
                    spectrum = subject.spectral_ledger(order, 3, alpha, epsilon)
                    self.assertEqual(len(spectrum), rank)
                    for root in spectrum:
                        absolute = abs(root)
                        while absolute % 3 == 0:
                            absolute //= 3
                        self.assertEqual(absolute, 1)

    def test_characteristic_polynomial_annihilates_each_tower(self) -> None:
        for epsilon in (-1, 1):
            for order in range(2, 7):
                spectrum = subject.spectral_ledger(order, 3, -1, epsilon)
                self.assertTrue(
                    subject.verify_recurrence(spectrum, max(36, 2 * len(spectrum) + 2))
                )
        with self.assertRaises(ValueError):
            subject.verify_recurrence({1: 1, 3: 1}, 3)

    def test_rank_two_moonshot_fails_at_four(self) -> None:
        for epsilon in (-1, 1):
            spectrum = subject.spectral_ledger(4, 5, 1, epsilon)
            self.assertEqual(len(spectrum), 7)
        self.assertEqual(len(subject.spectral_ledger(2, 5, 1, 1)), 2)

    def test_spectral_ledger_rejects_nonprime_bases(self) -> None:
        for invalid in (True, 1, 4, 9, 15):
            with self.assertRaises(ValueError):
                subject.spectral_ledger(2, invalid, 1, 1)

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
            fixture["proof_ledger"]["rank_two_beyond_order_three"], "REFUTED"
        )
        self.assertEqual(
            fixture["proof_ledger"]["sheaf_or_tate_class_realization"], "NOT CLAIMED"
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")
        self.assertEqual(fixture["minimal_ranks"]["epsilon_plus"]["4"], 7)


if __name__ == "__main__":
    unittest.main()
