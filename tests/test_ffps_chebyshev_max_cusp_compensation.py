from __future__ import annotations

import importlib.util
import json
import math
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
    / "ffps_chebyshev_max_cusp_compensation.py"
)
SPEC = importlib.util.spec_from_file_location("chebyshev_cusp", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load Chebyshev max-cusp producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class ChebyshevMaxCuspCompensationTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_first_primitive_energy_ratios(self) -> None:
        self.assertAlmostEqual(subject.primitive_energy_ratio(1), 1 / 12)
        self.assertAlmostEqual(subject.primitive_energy_ratio(2), 1 / 48)
        self.assertAlmostEqual(subject.primitive_l1_ratio(1), 1 / 4)
        self.assertAlmostEqual(subject.primitive_l1_ratio(2), 1 / 8)

    def test_independent_cell_integral(self) -> None:
        for order in range(1, 9):
            self.assertAlmostEqual(
                subject.primitive_energy_ratio(order),
                subject.primitive_energy_ratio_by_cells(order),
                places=13,
            )
            self.assertAlmostEqual(
                subject.primitive_energy_ratio(order),
                subject.primitive_energy_ratio_cosine(order),
                places=13,
            )

    def test_order_constants(self) -> None:
        self.assertEqual(subject.order_constant(1), Fraction(100, 3))
        self.assertEqual(subject.order_constant(2), Fraction(3136, 45))

    def test_compensation_first_values(self) -> None:
        self.assertAlmostEqual(subject.compensation_product(1), 25 / 9)
        self.assertAlmostEqual(subject.compensation_product(2), Fraction(196, 135))

    def test_refill_asymptotic(self) -> None:
        for order in (100, 1000):
            scaled = (
                subject.primitive_energy_ratio(order)
                * 72
                * (order + 1) ** 2
                / math.pi**2
            )
            self.assertAlmostEqual(scaled, 1, delta=0.001)

    def test_compensation_limit(self) -> None:
        ratio = subject.compensation_product(1000) / subject.refill_limit()
        self.assertAlmostEqual(ratio, 1, delta=0.005)

    def test_strict_product_descent(self) -> None:
        products = [subject.compensation_product(order) for order in range(1, 50)]
        self.assertTrue(all(left > right for left, right in pairwise(products)))
        for order in range(1, 100):
            self.assertLess(subject.compensation_ratio_upper_bound(order), 1)
            self.assertGreater(subject.compensation_ratio_gap_numerator(order), 0)
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["compensation_product_strictly_decreases_for_all_orders"],
            "PROVED",
        )

    def test_uniform_relative_remainder_constant(self) -> None:
        for order in range(1, 1000):
            self.assertLessEqual(subject.relative_remainder_coefficient(order), 9 / 32)
        self.assertAlmostEqual(
            subject.relative_remainder_coefficient(1000),
            9 * math.pi**2 / 512,
            delta=0.001,
        )

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(ledger["exact_linear_max_cusp_refill"], "PROVED")
        self.assertEqual(ledger["moving_order_Perron_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_cell_replay_order"], 8)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["quadratures"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.primitive_energy_ratio(0)
        with self.assertRaises(ValueError):
            subject.cell_boundaries(-1)
        with self.assertRaises(ValueError):
            subject.order_constant(0)


if __name__ == "__main__":
    unittest.main()
