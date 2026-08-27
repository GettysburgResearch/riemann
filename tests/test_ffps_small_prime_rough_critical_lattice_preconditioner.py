from __future__ import annotations

import importlib.util
import json
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
    / "ffps_small_prime_rough_critical_lattice_preconditioner.py"
)
SPEC = importlib.util.spec_from_file_location(
    "small_prime_rough_critical_lattice_preconditioner", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SmallPrimeRoughCriticalLatticePreconditionerTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_prime_sieve(self) -> None:
        self.assertEqual(subject.primes_up_to(1), ())
        self.assertEqual(subject.primes_up_to(7), subject.TOY_PRIMES)

    def test_forward_and_inverse_coefficient_identities(self) -> None:
        for value in range(1, subject.COEFFICIENT_CAP + 1):
            self.assertEqual(
                subject.forward_coefficient(value, subject.TOY_PRIMES),
                subject.mobius(value),
            )
            self.assertEqual(
                subject.inverse_coefficient(value, subject.TOY_PRIMES),
                subject.rough_mobius(value, subject.TOY_PRIMES),
            )
        panel = subject.coefficient_panel()
        self.assertGreater(panel["rough_nonzero"], 0)
        self.assertLess(panel["rough_nonzero"], subject.COEFFICIENT_CAP)

    def test_duplicate_67_layers_remain_literal(self) -> None:
        residue = 2
        expected = [
            coefficient * subject.mobius(residue) for coefficient in (1, -2, 1, 0)
        ]
        actual = [
            subject.beta(subject.EXCEPTIONAL_PRIME**exponent * residue)
            for exponent in range(4)
        ]
        self.assertEqual(actual, expected)

    def test_scale_filters_commute(self) -> None:
        values = (Fraction(0),) + tuple(
            Fraction(((-1) ** height) * (height + 4), 2 * height + 1)
            for height in range(1, subject.PREFIX_CAP + 1)
        )
        omegas = {prime: Fraction(1, prime + 1) for prime in subject.TOY_PRIMES}
        forward = subject.apply_filters(values, subject.TOY_PRIMES, omegas)
        reverse = subject.apply_filters(
            values, tuple(reversed(subject.TOY_PRIMES)), omegas
        )
        self.assertEqual(forward, reverse)

    def test_terminating_scale_inverses_reconstruct(self) -> None:
        values = (Fraction(0),) + tuple(
            Fraction(height * height + 1, height + 2)
            for height in range(1, subject.PREFIX_CAP + 1)
        )
        omegas = {prime: Fraction(1, prime + 1) for prime in subject.TOY_PRIMES}
        filtered = subject.apply_filters(values, subject.TOY_PRIMES, omegas)
        reconstructed = subject.apply_inverse_filters(
            filtered, tuple(reversed(subject.TOY_PRIMES)), omegas
        )
        self.assertEqual(reconstructed, values)

    def test_canonical_json_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        self.assertTrue(result["scope"]["exact_prefix_coordinate_theorem"])
        self.assertTrue(result["scope"]["pnt_asymptotic_imported"])
        self.assertFalse(result["scope"]["rough_prefix_estimate_proved"])
        self.assertFalse(result["scope"]["critical_retained_estimate_proved"])
        self.assertFalse(result["scope"]["cancellation_or_rh_proved"])
        self.assertFalse(
            result["scope"]["operator_norm_claim_for_discarded_lattice_tail"]
        )
        self.assertTrue(
            result["moving_y_lattice_equivalence"]["subfrontier_is_admissible"]
        )
        self.assertFalse(
            result["moving_y_lattice_equivalence"]["critical_scale_transfers_subpower"]
        )
        self.assertEqual(result["resource_caps"]["floating_point_operations"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.primes_up_to(0)
        with self.assertRaises(ValueError):
            subject.mobius(0)
        with self.assertRaises(ValueError):
            subject.is_smooth(0, subject.TOY_PRIMES)
        with self.assertRaises(ValueError):
            subject.scale_filter((Fraction(1),), 2, Fraction(1, 3))
        with self.assertRaises(ValueError):
            subject.inverse_scale_filter((Fraction(1), Fraction(2)), 2, Fraction(1, 3))


if __name__ == "__main__":
    unittest.main()
