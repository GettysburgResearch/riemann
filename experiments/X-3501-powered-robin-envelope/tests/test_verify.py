from __future__ import annotations

import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import verify  # noqa: E402


CERTIFICATE = ROOT / "certificates" / "synthetic-powered-prune.json"


def enumerate_exact(
    prefix_factors: list[tuple[int, int]],
    tail_primes: list[int],
    integer_bound: int,
) -> Fraction:
    prefix_value = 1
    prefix_abundancy = Fraction(1)
    for p, exponent in prefix_factors:
        prefix_value *= p**exponent
        prefix_abundancy *= verify.abundancy_prime_power(p, exponent)
    max_exponent = prefix_factors[-1][1]

    best = Fraction(0)

    def visit(
        index: int,
        previous_exponent: int,
        value: int,
        abundancy: Fraction,
    ) -> None:
        nonlocal best
        if index == len(tail_primes):
            best = max(best, prefix_abundancy * abundancy)
            return
        p = tail_primes[index]
        for exponent in range(1, previous_exponent + 1):
            next_value = value * p**exponent
            if prefix_value * next_value <= integer_bound:
                visit(
                    index + 1,
                    exponent,
                    next_value,
                    abundancy
                    * verify.abundancy_prime_power(p, exponent),
                )

    visit(0, max_exponent, 1, Fraction(1))
    return best


class PoweredEnvelopeTests(unittest.TestCase):
    def load_regression(self) -> dict:
        with CERTIFICATE.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def test_synthetic_regression_certifies_joint_only(self) -> None:
        result = verify.verify_certificate(self.load_regression())
        self.assertEqual(result["status"], "CERTIFIED_PRUNE")
        self.assertFalse(result["separate_alone_prunes"])
        self.assertTrue(result["powered_strictly_improves_separate"])

    def test_mutated_powered_bound_is_rejected(self) -> None:
        data = self.load_regression()
        value = int(data["claimed"]["powered_bound"]["numerator"])
        data["claimed"]["powered_bound"]["numerator"] = str(value - 1)
        with self.assertRaises(verify.CertificateError):
            verify.verify_certificate(data)

    def test_nonconsecutive_prime_support_is_rejected(self) -> None:
        data = self.load_regression()
        data["tail_primes"] = ["3", "7", "11"]
        with self.assertRaises(verify.CertificateError):
            verify.verify_certificate(data)

    def test_exact_envelope_dominates_small_exhaustive_optima(self) -> None:
        cases = [
            ([(2, 2)], [3, 5], 2 * 2 * 3 * 5 * 5),
            ([(2, 3)], [3, 5, 7], 8 * 3 * 5 * 7 * 9),
            ([(2, 4), (3, 2)], [5, 7], (16 * 9) * 5 * 7 * 20),
        ]
        duals = [(0, 1), (1, 16), (3, 64)]
        for prefix, tail, bound in cases:
            exact = enumerate_exact(prefix, tail, bound)
            for a, d in duals:
                with self.subTest(prefix=prefix, tail=tail, a=a, d=d):
                    result = verify.compute_envelope(
                        prefix, tail, bound, a, d
                    )
                    self.assertLessEqual(exact**d, result["joint_power"])

    def test_regression_true_optimum_is_403_over_105(self) -> None:
        exact = enumerate_exact([(2, 4)], [3, 5, 7], 8400)
        self.assertEqual(exact, Fraction(403, 105))

    def test_weak_dual_fails_closed_through_target_comparison(self) -> None:
        data = self.load_regression()
        data["dual"] = {"a": 0, "d": 1}
        recomputed = verify.compute_envelope(
            [(2, 4)], [3, 5, 7], 8400, 0, 1
        )
        data["claimed"] = {
            "caps": recomputed["caps"],
            "separate_ceiling": verify.fraction_json(
                recomputed["separate_ceiling"]
            ),
            "powered_bound": verify.fraction_json(
                recomputed["powered_bound"]
            ),
            "joint_power": verify.fraction_json(
                recomputed["joint_power"]
            ),
            "status": "UNRESOLVED",
        }
        result = verify.verify_certificate(data)
        self.assertEqual(result["status"], "UNRESOLVED")


if __name__ == "__main__":
    unittest.main()
