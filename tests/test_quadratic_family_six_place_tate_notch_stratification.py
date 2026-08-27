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
    / "quadratic_family_six_place_tate_notch_stratification.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("six_place_notch", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load six-place Tate-notch producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SixPlaceTateNotchStratificationTest(unittest.TestCase):
    def test_frozen_source_contract(self) -> None:
        subject.check_source_contract()

    def test_primitive_pair_special_values(self) -> None:
        for prime, trace, middle in ((7, 4, 17), (11, 5, 26), (7, 2, 15)):
            q_poly = subject.primitive_pair_polynomial(prime, trace, middle)
            delta = trace**2 - 4 * middle + 8 * prime
            self.assertEqual(subject.polynomial_value(q_poly, prime), prime**3 * delta)
            self.assertEqual(
                subject.polynomial_value(q_poly, -prime), prime**3 * trace**2
            )

    def test_raw_centered_decomposition(self) -> None:
        prime, trace, middle = 7, 4, 17
        for degree in range(1, 7):
            trace_n, middle_n, centered_n = subject.tower_traces(
                prime, trace, middle, degree
            )
            q = prime**degree
            centered = (
                q**2
                - 6 * q
                - 21
                + q**2 * trace_n
                - 21 * trace_n
                + q * centered_n
                - 6 * centered_n
            )
            self.assertEqual(
                centered,
                subject.raw_correlation(prime, trace, middle, degree),
            )
            self.assertEqual(centered_n, middle_n - 2 * q)

    def test_unique_cubic_notch_roots(self) -> None:
        for prime in (7, 11):
            notch = subject.notch_polynomial(prime)
            self.assertEqual(len(notch) - 1, 3)
            for root in (1, prime, prime**2):
                self.assertEqual(subject.polynomial_value(notch, root), 0)
            # Three distinct vanishing conditions have a nonzero Vandermonde.
            self.assertNotEqual((prime - 1) * (prime**2 - 1) * (prime**2 - prime), 0)

    def test_generic_rank_sixteen_and_recurrence(self) -> None:
        for prime, first_trace, second_trace in subject.GENERIC_CONTROLS:
            trace = first_trace + second_trace
            middle = first_trace * second_trace + 2 * prime
            self.assertEqual(subject.memberwise_rank(prime, trace, middle), 16)
            annihilator = subject.generic_annihilator(prime, trace, middle)
            self.assertEqual(len(annihilator) - 1, 16)
            filtered = lambda degree, p=prime, t=trace, b=middle: (
                subject.filtered_correlation(p, t, b, degree)
            )
            self.assertTrue(subject.verify_recurrence(filtered, annihilator))

    def test_square_collision_factorizations_and_ranks(self) -> None:
        for (
            prime,
            nonsquare,
            marks,
            trace,
            middle,
            expected_rank,
        ) in subject.REALIZED_SQUARE_CONTROLS:
            realized_trace, realized_middle, trace_two = (
                subject.realized_curve_coefficients(prime, nonsquare, marks)
            )
            self.assertEqual((realized_trace, realized_middle), (trace, middle))
            self.assertEqual(trace_two, trace**2 - 2 * middle)
            elliptic_trace = trace // 2
            p_poly = subject.weil_polynomial(prime, trace, middle)
            expected_p = subject.polynomial_multiply(
                (prime, -elliptic_trace, 1),
                (prime, -elliptic_trace, 1),
            )
            self.assertEqual(p_poly, expected_p)
            q_poly = subject.primitive_pair_polynomial(prime, trace, middle)
            expected_q = subject.polynomial_multiply(
                subject.polynomial_multiply((-prime, 1), (-prime, 1)),
                (prime**2, -(elliptic_trace**2 - 2 * prime), 1),
            )
            self.assertEqual(q_poly, expected_q)
            self.assertEqual(
                subject.memberwise_rank(prime, trace, middle), expected_rank
            )

    def test_trace_zero_negative_tate_modes_survive(self) -> None:
        prime, trace, middle = 7, 0, 14
        q_poly = subject.primitive_pair_polynomial(prime, trace, middle)
        self.assertEqual(subject.polynomial_value(q_poly, -prime), 0)
        notch = subject.notch_polynomial(prime)
        self.assertNotEqual(subject.polynomial_value(notch, -prime), 0)
        self.assertNotEqual(subject.polynomial_value(notch, -(prime**2)), 0)

    def test_fixture_and_claim_scope(self) -> None:
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
        self.assertEqual(fixture["theorem"]["generic_rank"], 16)
        self.assertEqual(
            fixture["theorem"]["square_stratum_ranks"],
            {"t_nonzero": 8, "t_zero": 6},
        )
        self.assertEqual(
            fixture["proof_ledger"]["square_stratum_realization_in_six_branch_family"],
            "PROVED BY TWO EXACT BOUNDED CONTROLS",
        )
        self.assertEqual(len(fixture["realized_exceptional_curves"]), 2)
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_resource_caps_and_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.power_sum((1, -1, 1), -1)
        with self.assertRaises(ValueError):
            subject.tower_traces(7, 1, 14, 0)
        result = subject.run(check_sources=False)
        self.assertEqual(result["resource_caps"]["largest_polynomial_degree"], 16)
        self.assertEqual(result["resource_caps"]["maximum_raw_extension_index"], 22)
        self.assertEqual(result["resource_caps"]["maximum_power_sum_exponent"], 44)
        self.assertEqual(result["resource_caps"]["matrices"], 0)
        self.assertEqual(
            result["resource_caps"]["largest_quadratic_extension_field"], 169
        )
        self.assertEqual(
            result["resource_caps"]["quadratic_extension_elements_visited"], 290
        )
        self.assertEqual(result["resource_caps"]["curves_enumerated"], 2)


if __name__ == "__main__":
    unittest.main()
