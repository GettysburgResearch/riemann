from __future__ import annotations

import importlib.util
import json
import subprocess
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
    / "ffps_function_field_beta_divisor_wavelet_pilot.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("beta_divisor_wavelet", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load beta divisor-wavelet pilot")
subject = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = subject
SPEC.loader.exec_module(subject)


class FfpsFunctionFieldBetaDivisorWaveletPilotTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_frozen_arithmetic_fiber(self) -> None:
        self.assertTrue(subject.pilot.is_irreducible(subject.CONDUCTOR, subject.Q))
        self.assertTrue(subject.pilot.is_irreducible(subject.EXCEPTIONAL, subject.Q))
        self.assertEqual(subject.character(subject.EXCEPTIONAL), 1)
        self.assertEqual(
            subject.evaluation_l_coefficients(subject.MAXIMUM_DEGREE),
            (1, 3, 5, 0, 0),
        )

    def test_necklace_content_and_length_counts(self) -> None:
        self.assertEqual(subject.content_necklace(1, 0), 1)
        self.assertEqual(subject.content_necklace(0, 1), 1)
        self.assertEqual(subject.content_necklace(1, 1), 1)
        self.assertEqual(subject.content_necklace(2, 0), 0)
        self.assertEqual(
            [subject.lyndon_count(length) for length in range(1, 5)],
            [2, 1, 2, 3],
        )

    def test_four_exact_routes_agree(self) -> None:
        maximum_degree = subject.MAXIMUM_DEGREE
        core = subject.core_enumeration(maximum_degree)
        self.assertEqual(core, subject.literal_beta_enumeration(maximum_degree))
        self.assertEqual(core, subject.euler_product(maximum_degree))
        self.assertEqual(core, subject.witt_l_product(maximum_degree))
        self.assertEqual(len(core), 14)

    def test_quadratic_odd_even_l_channels(self) -> None:
        self.assertEqual(
            subject.serialize_univariate(
                subject.full_inverse_l(1, subject.MAXIMUM_DEGREE),
                subject.MAXIMUM_DEGREE,
            ),
            [1, -3, 4, 3, -29],
        )
        self.assertEqual(
            subject.serialize_univariate(
                subject.full_inverse_l(2, subject.MAXIMUM_DEGREE),
                subject.MAXIMUM_DEGREE,
            ),
            [1, -5, 0, 1, -5],
        )

    def test_zero_frequency_factorization_and_rows(self) -> None:
        maximum_degree = subject.MAXIMUM_DEGREE
        zero = subject.collapse_zero_frequency(
            subject.core_enumeration(maximum_degree),
            maximum_degree,
        )
        self.assertEqual(
            zero,
            subject.zero_frequency_full_l_product(maximum_degree),
        )
        self.assertEqual(
            subject.serialize_univariate(zero, maximum_degree),
            [1, -6, 13, 2, -120],
        )

    def test_scope_and_main_term_ledger(self) -> None:
        report = subject.build_report()
        self.assertEqual(
            report["proof_ledger"]["zero_mode_energy_main_term"],
            "PROVED BY DOUBLE-POLE COEFFICIENTS",
        )
        self.assertEqual(
            report["proof_ledger"]["near_square_or_maximal_wavelet_estimate"],
            "NOT PROVED",
        )
        self.assertEqual(
            report["proof_ledger"]["number_field_waveprimcar"],
            "NOT PROVED",
        )
        self.assertFalse(
            report["scope_firewall"]["finite_rows_imply_growing_cancellation"]
        )
        self.assertEqual(report["resource_caps"]["zeta_zeros"], 0)
        self.assertEqual(report["resource_caps"]["numerical_l_zeros"], 0)

    def test_fixture_is_canonical(self) -> None:
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
        self.assertEqual(fixture["source_contract"]["commit"], "3658d4c31")
        self.assertEqual(
            fixture["exact_example"]["zero_frequency_coefficients"],
            [1, -6, 13, 2, -120],
        )

    def test_guards(self) -> None:
        for bad in (True, -1, subject.MAXIMUM_DEGREE + 1, 1.5):
            with self.assertRaises(ValueError):
                subject.validate_degree(bad)
        for bad in (True, 0, -1, 1.5):
            with self.assertRaises(ValueError):
                subject.integer_moebius(bad)
        with self.assertRaises(ValueError):
            subject.content_necklace(0, 0)
        with self.assertRaises(ValueError):
            subject.power_series({(0, 0): 1}, -1, 1)
        with self.assertRaises(ValueError):
            subject.inverse_univariate((2, 1), 1)


if __name__ == "__main__":
    unittest.main()
