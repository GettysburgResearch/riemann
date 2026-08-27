from __future__ import annotations

import importlib.util
import json
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
    / "ffps_carrier_ensemble_condition_firewall.py"
)
SPEC = importlib.util.spec_from_file_location("carrier_ensemble", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load carrier-ensemble producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class CarrierEnsembleConditionFirewallTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_sharp_constants_include_low_pass(self) -> None:
        self.assertEqual(
            [subject.sharp_constant(rung) for rung in range(5)],
            [1, 12, 720, 100800, 25401600],
        )

    def test_direct_sum_exact_example(self) -> None:
        data = subject.direct_sum_data(
            (
                (1, Fraction(1), Fraction(1), Fraction(2)),
                (2, Fraction(1, 30), Fraction(1), Fraction(2)),
            )
        )
        self.assertEqual(data["diagonal"], 36)
        self.assertEqual(data["reverse"], Fraction(9, 4))
        self.assertEqual(data["ratio"], 16)
        self.assertEqual(data["conditions"], (Fraction(8), Fraction(32)))

    def test_direct_sum_ratio_is_between_constituents(self) -> None:
        data = subject.direct_sum_data(
            (
                (1, Fraction(7, 3), Fraction(2), Fraction(5)),
                (3, Fraction(11, 7), Fraction(3), Fraction(8)),
            )
        )
        self.assertGreaterEqual(data["ratio"], min(data["conditions"]))
        self.assertLessEqual(data["ratio"], max(data["conditions"]))

    def test_optimal_detectors(self) -> None:
        self.assertEqual(
            subject.optimal_detector_support_one(1),
            (Fraction(6), Fraction(-12)),
        )
        self.assertEqual(
            subject.optimal_detector_support_one(2),
            (Fraction(60), Fraction(-360), Fraction(360)),
        )

    def test_coherent_higher_rung_addition(self) -> None:
        k1 = subject.optimal_detector_support_one(1)
        k2 = subject.optimal_detector_support_one(2)
        kernel = subject.polynomial_add(
            k1, subject.polynomial_scale(k2, Fraction(1, 10))
        )
        self.assertEqual(kernel, (Fraction(12), Fraction(-48), Fraction(36)))
        self.assertEqual(subject.lowest_surviving_moment(kernel), (1, Fraction(1)))
        self.assertEqual(subject.polynomial_norm_squared(kernel), Fraction(96, 5))
        self.assertEqual(subject.coherent_sharp_lower_bound(kernel), 12)

    def test_cancellation_raises_rung_exactly(self) -> None:
        kernel = (Fraction(6), Fraction(-36), Fraction(36))
        self.assertEqual(subject.polynomial_moment(kernel, 0), 0)
        self.assertEqual(subject.polynomial_moment(kernel, 1), 0)
        self.assertEqual(subject.polynomial_moment(kernel, 2), Fraction(1, 5))
        self.assertEqual(subject.lowest_surviving_moment(kernel), (2, Fraction(1, 10)))
        self.assertEqual(subject.polynomial_norm_squared(kernel), Fraction(36, 5))
        self.assertEqual(subject.coherent_sharp_lower_bound(kernel), Fraction(36, 5))

    def test_psd_factorization_example(self) -> None:
        matrix = (
            (Fraction(1), Fraction(1, 2)),
            (Fraction(0), Fraction(1)),
        )
        self.assertEqual(
            subject.matrix_transpose_product(matrix),
            (
                (Fraction(1), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(5, 4)),
            ),
        )

    def test_order_zero_condition(self) -> None:
        self.assertEqual(subject.optimal_carrier_support_one(0), (Fraction(1),))
        self.assertEqual(subject.support_condition(0, Fraction(2), Fraction(1)), 2)
        self.assertEqual(subject.polynomial_norm_squared((Fraction(1),)), 1)

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["positive_direct_sum_beats_best_constituent"], "DISPROVED"
        )
        self.assertEqual(ledger["m_0_low_pass_loophole_and_RH_equivalence"], "PROVED")
        self.assertEqual(ledger["new_unconditional_beta_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["maximum_rung"], 4)
        self.assertEqual(caps["beta_terms"], 0)
        self.assertEqual(caps["quadratures"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.sharp_constant(-1)
        with self.assertRaises(ValueError):
            subject.support_condition(1, Fraction(1), Fraction(2))
        with self.assertRaises(ValueError):
            subject.direct_sum_data(())
        with self.assertRaises(ValueError):
            subject.direct_sum_data(((1, Fraction(-1), Fraction(1), Fraction(2)),))
        with self.assertRaises(ValueError):
            subject.polynomial_derivative((Fraction(1),), -1)
        with self.assertRaises(ValueError):
            subject.lowest_surviving_moment((Fraction(0),))
        with self.assertRaises(ValueError):
            subject.matrix_transpose_product(())


if __name__ == "__main__":
    unittest.main()
