from __future__ import annotations

import importlib.util
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
    / "function_field_divisor_wavelet_witt_factorization.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("divisor_wavelet_witt", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load divisor-wavelet Witt producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldDivisorWaveletWittFactorizationTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_content_refined_necklace_counts(self) -> None:
        expected_totals = (2, 1, 2, 3, 6, 9, 18, 30)
        for total, expected in enumerate(expected_totals, start=1):
            rows = [
                subject.necklace_multiplicity(left, total - left)
                for left in range(total + 1)
            ]
            self.assertEqual(sum(rows), expected)
            self.assertEqual(sum(rows), subject.binary_lyndon_count(total))
        self.assertEqual(subject.necklace_multiplicity(1, 1), 1)
        self.assertEqual(subject.necklace_multiplicity(2, 0), 0)

    def test_irreducible_counts(self) -> None:
        self.assertEqual(
            [subject.irreducible_count(3, degree) for degree in range(1, 6)],
            [3, 3, 8, 18, 48],
        )

    def test_direct_and_witt_products_agree(self) -> None:
        for q in subject.CONTROL_Q:
            self.assertEqual(
                subject.direct_euler_product(q, subject.MAX_TOTAL_DEGREE),
                subject.witt_product(q, subject.MAX_TOTAL_DEGREE),
            )

    def test_first_witt_factors_are_two_zeta_nuisance_modes(self) -> None:
        polynomial = subject.witt_product(3, 1)
        self.assertEqual(
            polynomial,
            {
                (0, 0): 1,
                (1, -1): -3,
                (1, 1): -3,
            },
        )

    def test_phase_one_coefficients(self) -> None:
        panel = subject.control_panel(3)
        coefficients = [int(value) for value in panel["phase_one_coefficients"]]
        self.assertEqual(coefficients[:4], [1, -6, 6, 12])

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
            fixture["proof_ledger"]["content_refined_witt_identity"],
            "PROVED EXACT",
        )
        self.assertEqual(
            fixture["proof_ledger"]["q_equals_three_critical_decay"],
            "NOT CLAIMED",
        )
        self.assertEqual(
            fixture["proof_ledger"]["number_field_waveprimcar"], "NOT PROVED"
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.necklace_multiplicity(0, 0)
        with self.assertRaises(ValueError):
            subject.necklace_multiplicity(-1, 2)
        with self.assertRaises(ValueError):
            subject.binary_lyndon_count(0)
        with self.assertRaises(ValueError):
            subject.irreducible_count(1, 2)


if __name__ == "__main__":
    unittest.main()
