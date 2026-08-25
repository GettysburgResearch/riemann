"""Focused exact tests for the FFPS conditioned-mask no-go theorem."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from itertools import pairwise
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import ffps_conditioned_mask_no_go as subject


class FFPSConditionedMaskNoGoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_restricted_inverse_formula_by_matrix_products(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            dimension = subject.phase_packet.sign_pair_dimension(prime)
            for support_size in range(1, dimension + 1):
                gram = subject.restricted_gram(prime, support_size)
                inverse = tuple(
                    tuple(
                        Fraction(row == column, prime)
                        + Fraction(1, prime * (prime - support_size))
                        for column in range(support_size)
                    )
                    for row in range(support_size)
                )
                product = tuple(
                    tuple(
                        sum(
                            (
                                Fraction(gram[row][inner]) * inverse[inner][column]
                                for inner in range(support_size)
                            ),
                            Fraction(0),
                        )
                        for column in range(support_size)
                    )
                    for row in range(support_size)
                )
                self.assertEqual(
                    product,
                    tuple(
                        tuple(Fraction(row == column) for column in range(support_size))
                        for row in range(support_size)
                    ),
                )

    def test_uniform_weights_are_the_sharp_principal_preserving_extremizer(
        self,
    ) -> None:
        for prime in subject.CONTROL_PRIMES:
            dimension = subject.phase_packet.sign_pair_dimension(prime)
            for support_size in range(1, dimension + 1):
                uniform = subject.uniform_weights_for_principal_amplitude(
                    prime, support_size
                )
                self.assertEqual(sum(uniform), dimension)
                optimum = subject.optimal_normalized_leverage_squared(
                    prime, support_size
                )
                self.assertEqual(
                    subject.restricted_dual_norm_squared(prime, uniform), optimum
                )
                perturbation = [Fraction(value) for value in uniform]
                if support_size > 1:
                    perturbation[0] += 1
                    perturbation[1] -= 1
                    self.assertEqual(
                        subject.fixed_amplitude_excess(prime, perturbation),
                        Fraction(2, prime),
                    )
                    self.assertGreater(
                        subject.restricted_dual_norm_squared(prime, perturbation),
                        optimum,
                    )
                else:
                    self.assertEqual(subject.fixed_amplitude_excess(prime, uniform), 0)

    def test_every_proper_mask_strictly_worsens_normalized_leverage(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            dimension = subject.phase_packet.sign_pair_dimension(prime)
            full = subject.phase_packet.principal_leverage_squared(prime)
            values = [
                subject.optimal_normalized_leverage_squared(prime, support_size)
                for support_size in range(1, dimension + 1)
            ]
            self.assertTrue(all(left > right for left, right in pairwise(values)))
            self.assertEqual(values[-1], full)
            self.assertTrue(all(value > full for value in values[:-1]))

    def test_raw_mask_gain_is_exactly_signal_attenuation(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            dimension = subject.phase_packet.sign_pair_dimension(prime)
            for support_size in range(1, dimension + 1):
                raw = subject.unnormalized_uniform_leverage_squared(prime, support_size)
                signal = subject.signal_fraction(prime, support_size)
                self.assertEqual(
                    raw / signal**2,
                    subject.optimal_normalized_leverage_squared(prime, support_size),
                )

    def test_triangular_drop_threshold(self) -> None:
        for prime in subject.CONTROL_PRIMES:
            dimension = subject.phase_packet.sign_pair_dimension(prime)
            for support_size in range(1, dimension + 1):
                row = subject.contraction_classification(prime, support_size)
                dropped = dimension - support_size
                defect = dimension - dropped * (dropped + 1)
                self.assertEqual(row["triangular_threshold_defect"], defect)
                expected = (
                    "contractive"
                    if defect > 0
                    else "critical"
                    if defect == 0
                    else "expansive"
                )
                self.assertEqual(row["classification"], expected)

    def test_fixture_and_provenance_are_locked(self) -> None:
        locked = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(locked, self.fixture)
        self.assertEqual(
            locked["source_frontier"]["dependency_sha256_lf"],
            subject._sha256_lf(subject.DEPENDENCY_PATH),
        )
        for label, path in (
            ("producer_sha256_lf", Path(subject.__file__)),
            ("note_sha256_lf", subject.NOTE_PATH),
            ("test_sha256_lf", Path(__file__)),
        ):
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                locked["provenance"][label], hashlib.sha256(normalized).hexdigest()
            )

    def test_fail_closed_domains(self) -> None:
        for support_size in (0, 2):
            with self.assertRaises(ValueError):
                subject.restricted_gram(3, support_size)
        with self.assertRaises(ValueError):
            subject.restricted_gram(9, 1)
        with self.assertRaises(ValueError):
            subject.fixed_amplitude_excess(7, (1, 1))
        with self.assertRaises(ValueError):
            subject.restricted_dual_norm_squared(5, ())


if __name__ == "__main__":
    unittest.main()
