from __future__ import annotations

import importlib.util
import json
import math
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_mobius_carrier_calibration.py"
)
SPEC = importlib.util.spec_from_file_location("curve_mobius_carrier", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load curve Möbius carrier producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldMobiusCarrierCalibrationTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_rational_recurrence(self) -> None:
        coefficients = subject.mobius_degree_coefficients(5, 1, 6)
        numerator = (1, -6, 5)
        for degree, coefficient in enumerate(coefficients):
            recovered = coefficient
            if degree >= 1:
                recovered -= coefficients[degree - 1]
            if degree >= 2:
                recovered += 5 * coefficients[degree - 2]
            expected = numerator[degree] if degree < len(numerator) else 0
            self.assertEqual(recovered, expected)

    def test_weil_and_off_circle_root_radii(self) -> None:
        for trace in (0, 4):
            roots = subject.reciprocal_roots(5, trace)
            for root in roots:
                self.assertAlmostEqual(abs(root), math.sqrt(5.0))
        roots = subject.reciprocal_roots(5, 5)
        self.assertGreater(max(abs(root) for root in roots), math.sqrt(5.0))

    def test_support_packets_are_disjoint(self) -> None:
        support = subject.support_length(5)
        self.assertLess(support, math.log(5.0))
        self.assertAlmostEqual(subject.detector_diagonal(5), 96.0 / math.log(5.0) ** 3)

    def test_energy_is_exact_squared_coefficient_sum(self) -> None:
        normalized = subject.normalized_coefficients(5, 0, 12)
        expected = subject.detector_diagonal(5) * sum(value**2 for value in normalized)
        self.assertAlmostEqual(subject.orthogonal_energy(5, 0, 12), expected)

    def test_formal_off_circle_control_separates(self) -> None:
        rows = subject.control_rows()
        self.assertLess(
            rows[0]["energy_root_estimator"], rows[-1]["energy_root_estimator"]
        )
        self.assertGreater(rows[-1]["normalized_root_radius"], 1.0)

    def test_genus_zero_cancellation_firewall(self) -> None:
        self.assertEqual(
            subject.mobius_degree_coefficients(5, 6, 6),
            [1, 0, 0, 0, 0, 0, 0],
        )

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_payload_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["disjoint_degree_packet_energy"], "PROVED EXACT")
        self.assertEqual(
            ledger["Weil_RH_itself"], "IMPORTED KNOWN THEOREM, NOT REPROVED"
        )
        self.assertEqual(ledger["integer_RH_or_GRH"], "NOT PROVED")

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.mobius_degree_coefficients(1, 0, 2)
        with self.assertRaises(ValueError):
            subject.mobius_degree_coefficients(5, 0, -1)


if __name__ == "__main__":
    unittest.main()
