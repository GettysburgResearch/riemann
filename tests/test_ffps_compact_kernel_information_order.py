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
    / "ffps_compact_kernel_information_order.py"
)
SPEC = importlib.util.spec_from_file_location("compact_kernel_order", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load compact-kernel producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class CompactKernelInformationOrderTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_blobs()

    def test_information_orders(self) -> None:
        self.assertEqual(
            subject.information_order_and_sensitivity((Fraction(1),)),
            (0, Fraction(1)),
        )
        self.assertEqual(
            subject.information_order_and_sensitivity((Fraction(1), Fraction(-2))),
            (1, Fraction(1, 6)),
        )
        self.assertEqual(
            subject.information_order_and_sensitivity((Fraction(6), Fraction(-12))),
            (1, Fraction(1)),
        )
        self.assertEqual(
            subject.information_order_and_sensitivity(
                (Fraction(60), Fraction(-360), Fraction(360))
            ),
            (2, Fraction(1)),
        )

    def test_coefficient_bv_envelopes(self) -> None:
        self.assertEqual(subject.coefficient_bv_envelope((Fraction(1),)), 3)
        self.assertEqual(
            subject.coefficient_bv_envelope((Fraction(1), Fraction(-2))), 7
        )

    def test_exact_linear_variation(self) -> None:
        self.assertEqual(
            subject.exact_zero_extended_variation_linear((Fraction(6), Fraction(-12))),
            24,
        )

    def test_normalized_reverse_factor(self) -> None:
        self.assertEqual(
            subject.normalized_reverse_energy_factor(1, Fraction(1), Fraction(2)),
            Fraction(2, 3),
        )

    def test_moving_geometric_factor(self) -> None:
        self.assertEqual(
            subject.moving_kernel_geometric_factor(
                1, Fraction(1), Fraction(2), Fraction(30)
            ),
            1200,
        )

    def test_translation_preserves_order_and_sensitivity(self) -> None:
        base = (Fraction(1), Fraction(-2))
        shifted = subject.translate_polynomial(base, Fraction(3))
        self.assertEqual(shifted, (Fraction(7), Fraction(-2)))
        self.assertEqual(
            subject.information_order_and_sensitivity(
                shifted, Fraction(1), Fraction(3)
            ),
            subject.information_order_and_sensitivity(base),
        )

    def test_dilation_preserves_order_and_sensitivity(self) -> None:
        base = (Fraction(1), Fraction(-2))
        dilated = subject.sensitivity_preserving_dilation(base, 1, Fraction(5))
        self.assertEqual(dilated, (Fraction(1, 25), Fraction(-2, 125)))
        self.assertEqual(
            subject.information_order_and_sensitivity(dilated, Fraction(5)),
            subject.information_order_and_sensitivity(base),
        )

    def test_sharp_constants(self) -> None:
        self.assertEqual(
            [subject.sharp_constant(i) for i in range(4)], [1, 12, 720, 100800]
        )

    def test_canonical_fixture_matches_payload(self) -> None:
        fixture = json.loads(subject.OUTPUT.read_text(encoding="utf-8"))
        self.assertEqual(fixture, subject.run())

    def test_firewalls(self) -> None:
        ledger = subject.run()["proof_ledger"]
        self.assertEqual(
            ledger["every_fixed_nonzero_compact_BV_kernel_RH_equivalence"],
            "PROVED",
        )
        self.assertEqual(ledger["failure_outside_safe_geometric_window"], "NOT PROVED")
        self.assertEqual(ledger["new_unconditional_beta_estimate"], "NOT PROVED")
        self.assertEqual(ledger["RH_or_GRH"], "NOT PROVED")

    def test_resource_caps(self) -> None:
        caps = subject.run()["resource_caps"]
        self.assertEqual(caps["exact_polynomial_examples"], 4)
        self.assertEqual(caps["beta_terms"], 0)

    def test_validation(self) -> None:
        with self.assertRaises(ValueError):
            subject.sharp_constant(-1)
        with self.assertRaises(ValueError):
            subject.polynomial_moment_on_interval((Fraction(1),), -1)
        with self.assertRaises(ValueError):
            subject.information_order_and_sensitivity((Fraction(0),))
        with self.assertRaises(ValueError):
            subject.coefficient_bv_envelope(())
        with self.assertRaises(ValueError):
            subject.normalized_reverse_energy_factor(1, Fraction(0), Fraction(2))
        with self.assertRaises(ValueError):
            subject.moving_kernel_geometric_factor(
                1, Fraction(1), Fraction(2), Fraction(-1)
            )
        with self.assertRaises(ValueError):
            subject.sensitivity_preserving_dilation((Fraction(1),), 0, Fraction(0))


if __name__ == "__main__":
    unittest.main()
