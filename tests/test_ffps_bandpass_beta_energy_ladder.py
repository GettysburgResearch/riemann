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
    / "ffps_bandpass_beta_energy_ladder.py"
)
SPEC = importlib.util.spec_from_file_location("bandpass_beta_energy", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BandpassBetaEnergyLadderTest(unittest.TestCase):
    def test_source_blobs(self) -> None:
        subject.check_source_blobs()

    def test_beta_square_euler_coefficients(self) -> None:
        for value in range(1, subject.COEFFICIENT_CAP + 1):
            self.assertEqual(
                subject.beta(value) ** 2, subject.beta_square_from_euler(value)
            )
        self.assertEqual(subject.exceptional_residue_ratio(), Fraction(2379, 2278))

    def test_box_convolution_preserves_mass(self) -> None:
        kernel = (Fraction(2), Fraction(-1), Fraction(4))
        box = subject.box_kernel(5)
        self.assertEqual(sum(box), 1)
        self.assertEqual(sum(subject.convolve(kernel, box)), sum(kernel))

    def test_finite_difference_has_exact_zero_order(self) -> None:
        base = (Fraction(2), Fraction(-3), Fraction(5), Fraction(1))
        for order in range(1, subject.REPLAY_ORDER_CAP + 1):
            kernel = subject.finite_difference(base, step=2, order=order)
            moments = subject.moments(kernel, order)
            self.assertTrue(all(value == 0 for value in moments[:order]))
            self.assertNotEqual(moments[order], 0)

    def test_box_smoothing_preserves_zero_order(self) -> None:
        kernel = subject.bandpass_kernel(
            (Fraction(1), Fraction(3), Fraction(-1)),
            step=1,
            order=3,
            box_width=4,
            box_order=3,
        )
        moments = subject.moments(kernel, 3)
        self.assertEqual(moments[:3], (Fraction(0),) * 3)
        self.assertNotEqual(moments[3], 0)

    def test_first_autocorrelation_is_second_difference(self) -> None:
        base = (Fraction(3), Fraction(-2), Fraction(5), Fraction(1))
        step = 3
        expected = subject.correlation_second_difference(
            subject.autocorrelation(base), step
        )
        actual = subject.autocorrelation(
            subject.finite_difference(base, step=step, order=1)
        )
        self.assertEqual(actual, expected)

    def test_autocorrelation_doubles_zero_order(self) -> None:
        order = 4
        kernel = subject.bandpass_kernel(
            (Fraction(4), Fraction(-1), Fraction(2)),
            step=1,
            order=order,
            box_width=2,
            box_order=2,
        )
        correlation = subject.autocorrelation(kernel)
        moments = subject.correlation_moments(correlation, 2 * order)
        self.assertTrue(all(value == 0 for value in moments[: 2 * order]))
        self.assertNotEqual(moments[2 * order], 0)

    def test_exact_finite_bandpass_gram_identity(self) -> None:
        source = tuple(Fraction(subject.beta(value), value) for value in range(1, 17))
        kernel = subject.bandpass_kernel(
            subject.TOY_BASE_KERNEL,
            step=2,
            order=2,
            box_width=3,
            box_order=1,
        )
        direct = subject.direct_toy_energy(source, kernel)
        gram = subject.gram_toy_energy(source, kernel)
        self.assertEqual(direct, gram)
        self.assertGreater(gram, 0)

    def test_scope_and_guards(self) -> None:
        result = subject.run(check_sources=False)
        self.assertFalse(result["energy_criterion"]["estimate_proved"])
        self.assertFalse(result["energy_criterion"]["rh_proved"])
        self.assertFalse(result["scope"]["horizon_dependent_filter"])
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)
        with self.assertRaises(ValueError):
            subject.finite_difference((Fraction(1),), step=0, order=1)
        with self.assertRaises(ValueError):
            subject.finite_difference(
                (Fraction(1),), step=1, order=subject.REPLAY_ORDER_CAP + 1
            )
        with self.assertRaises(ValueError):
            subject.bandpass_kernel(
                (Fraction(1),),
                step=1,
                order=1,
                box_width=1,
                box_order=subject.REPLAY_BOX_ORDER_CAP + 1,
            )
        with self.assertRaises(ValueError):
            subject.box_kernel(0)


if __name__ == "__main__":
    unittest.main()
