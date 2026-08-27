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
    / "quadratic_family_four_place_universal_tate_notch.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("four_place_tate_notch", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load four-place Tate-notch producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FourPlaceUniversalTateNotchTest(unittest.TestCase):
    def test_frozen_source_contract(self) -> None:
        subject.check_source_contract()

    def test_notch_has_exact_nuisance_roots(self) -> None:
        for prime in (5, 7, 11):
            notch = subject.notch_polynomial(prime)
            self.assertEqual(subject.polynomial_value(notch, 1), 0)
            self.assertEqual(subject.polynomial_value(notch, prime**2), 0)
            self.assertEqual(len(notch) - 1, 2)

    def test_linear_vanishing_system_has_nonzero_determinant(self) -> None:
        for prime in (5, 7):
            # The equations F(1)=F(p^2)=0 for F(T)=a+bT have determinant
            # p^2-1, so their only solution over Q is a=b=0.
            self.assertNotEqual(prime**2 - 1, 0)

    def test_trace_and_raw_tower(self) -> None:
        prime, trace = 5, -3
        values = [subject.trace_value(prime, trace, degree) for degree in range(7)]
        self.assertEqual(values[:2], [2, trace])
        for degree in range(5):
            self.assertEqual(
                values[degree + 2],
                trace * values[degree + 1] - prime * values[degree],
            )
        self.assertEqual(subject.raw_correlation(prime, trace, 1), -15)

    def test_filtered_rank_four_recurrence(self) -> None:
        for prime, traces in subject.CONTROL_TRACES.items():
            for trace in traces:
                filtered = lambda degree, p=prime, t=trace: (
                    subject.filtered_correlation(p, t, degree)
                )
                recurrence = subject.geometric_recurrence_polynomial(prime, trace)
                self.assertEqual(len(recurrence) - 1, 4)
                self.assertTrue(subject.verify_recurrence(filtered, recurrence))
                self.assertNotEqual(subject.hankel_determinant(filtered, 4), 0)

    def test_adaptive_filters_have_rank_two_residuals(self) -> None:
        prime, trace = 7, 2
        raw = lambda degree: subject.raw_correlation(prime, trace, degree)
        untwisted_filter = subject.polynomial_multiply(
            subject.notch_polynomial(prime),
            subject.twisted_polynomial(prime, trace),
        )
        twisted_filter = subject.polynomial_multiply(
            subject.notch_polynomial(prime),
            subject.untwisted_polynomial(prime, trace),
        )
        self.assertEqual(len(untwisted_filter) - 1, 4)
        self.assertEqual(len(twisted_filter) - 1, 4)
        untwisted = lambda degree: subject.apply_filter(raw, untwisted_filter, degree)
        twisted = lambda degree: subject.apply_filter(raw, twisted_filter, degree)
        self.assertTrue(
            subject.verify_recurrence(
                untwisted, subject.untwisted_polynomial(prime, trace)
            )
        )
        self.assertTrue(
            subject.verify_recurrence(twisted, subject.twisted_polynomial(prime, trace))
        )
        self.assertNotEqual(subject.hankel_determinant(untwisted, 2), 0)
        self.assertNotEqual(subject.hankel_determinant(twisted, 2), 0)

    def test_control_panel_and_exact_hankel_guard(self) -> None:
        panel = subject.control_panel(5, 1)
        self.assertEqual(panel["prime"], 5)
        self.assertEqual(panel["trace"], 1)
        self.assertNotEqual(int(panel["hankel_rank_four_determinant"]), 0)
        with self.assertRaises(ValueError):
            subject.bareiss_determinant(((1, 2, 3), (4, 5, 6)))

    def test_fixture_and_scope(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(fixture["theorem"]["post_notch_minimal_rank"], 4)
        self.assertIn("impossible", fixture["theorem"]["universal_rank_two_verdict"])
        self.assertEqual(
            fixture["proof_ledger"]["sheaf_or_tate_class_realization"],
            "NOT CLAIMED",
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_validation_and_resource_caps(self) -> None:
        with self.assertRaises(ValueError):
            subject.validate_prime(4)
        with self.assertRaises(ValueError):
            subject.validate_prime(9)
        with self.assertRaises(ValueError):
            subject.validate_trace(5, 5)
        with self.assertRaises(ValueError):
            subject.raw_correlation(5, 1, 0)
        result = subject.run(check_sources=False)
        self.assertEqual(result["resource_caps"]["largest_exact_matrix"], 4)
        self.assertEqual(result["resource_caps"]["maximum_raw_extension_index"], 14)
        self.assertEqual(result["resource_caps"]["finite_field_elements"], 0)


if __name__ == "__main__":
    unittest.main()
