from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_bandpass_assembled_perron_leakage.py"
)
SPEC = importlib.util.spec_from_file_location("bandpass_perron_leakage", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BandpassAssembledPerronLeakageTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_autocorrelation_has_doubled_notch(self) -> None:
        for order in range(1, subject.REPLAY_ORDER_CAP + 1):
            bandpass = subject.box_smooth(
                subject.finite_difference(subject.TOY_BOUNDARY_KERNEL, order),
                width=3,
                order=1,
            )
            correlation = subject.autocorrelation(bandpass)
            self.assertTrue(
                all(
                    subject.signed_moment(correlation, exponent) == 0
                    for exponent in range(2 * order)
                )
            )
            self.assertNotEqual(subject.signed_moment(correlation, 2 * order), 0)

    def test_absolute_lag_identity_is_strict(self) -> None:
        for row in subject.leakage_rows():
            primitive_energy = Fraction(row["primitive_energy"])
            absolute_first = Fraction(row["absolute_first_moment"])
            self.assertGreater(primitive_energy, 0)
            self.assertEqual(absolute_first, -2 * primitive_energy)
            self.assertEqual(
                Fraction(row["linear_leakage_coefficient"]), primitive_energy
            )
            self.assertTrue(row["linear_leakage_is_strict"])

    def test_assembled_reindex_is_kernel_agnostic(self) -> None:
        direct, direct_pairs = subject.direct_energy()
        assembled, assembled_pairs = subject.assembled_energy()
        self.assertEqual(direct_pairs, assembled_pairs)
        self.assertEqual(direct, assembled)
        panel = subject.assembled_reindex_panel()
        self.assertEqual(panel["ordered_pairs"], 729)
        self.assertEqual(panel["radical_dimension"], 190)

    def test_barnes_normalization(self) -> None:
        panel = subject.barnes_panel()
        self.assertEqual(panel["jacobian_absolute_value"], 1)
        self.assertEqual(panel["residue_coefficient"], "1/z on both signs of x")
        self.assertEqual(panel["x_positive_pole"], "v=z/2")
        self.assertEqual(panel["x_negative_pole"], "v=-z/2")

    def test_scope_fences(self) -> None:
        result = subject.run(check_sources=False)
        self.assertTrue(
            result["bandpass_assembled_identity"]["sharp_identity_survives_verbatim"]
        )
        self.assertTrue(result["bandpass_assembled_identity"]["rh_equivalent"])
        self.assertFalse(result["bandpass_assembled_identity"]["estimate_proved"])
        self.assertTrue(result["double_perron"]["exact_t_zero_notch_retained"])
        self.assertFalse(result["max_tilt_leakage"]["repeated_notch_improves_z_order"])
        self.assertFalse(result["scope"]["perron_contour_shift"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.finite_difference((Fraction(1),), 0)
        with self.assertRaises(ValueError):
            subject.finite_difference((Fraction(1),), subject.REPLAY_ORDER_CAP + 1)
        with self.assertRaises(ValueError):
            subject.box_smooth((Fraction(1),), 0, 1)
        with self.assertRaises(ValueError):
            subject.cumulative_cells((Fraction(1),))


if __name__ == "__main__":
    unittest.main()
