"""Independent small checks for the affine Burnside formulas."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import hyperelliptic_affine_burnside as subject  # noqa: E402


def trim(poly: tuple[int, ...], q: int) -> tuple[int, ...]:
    values = list(poly)
    while values and values[-1] % q == 0:
        values.pop()
    return tuple(value % q for value in values)


def remainder(
    dividend: tuple[int, ...], divisor: tuple[int, ...], q: int
) -> tuple[int, ...]:
    work = list(trim(dividend, q))
    divisor = trim(divisor, q)
    inverse = pow(divisor[-1], -1, q)
    while len(work) >= len(divisor):
        scale = work[-1] * inverse % q
        offset = len(work) - len(divisor)
        for index, coefficient in enumerate(divisor):
            work[offset + index] = (work[offset + index] - scale * coefficient) % q
        while work and work[-1] == 0:
            work.pop()
    return tuple(work)


def is_squarefree(poly: tuple[int, ...], q: int) -> bool:
    derivative = tuple(index * poly[index] % q for index in range(1, len(poly)))
    left = trim(poly, q)
    right = trim(derivative, q)
    while right:
        left, right = right, remainder(left, right, q)
    return len(left) == 1


def affine_transform(
    poly: tuple[int, ...], alpha: int, beta: int, q: int
) -> tuple[int, ...]:
    degree = len(poly) - 1
    output = [0] * (degree + 1)
    leading_scale = pow(pow(alpha, degree, q), -1, q)
    for exponent, coefficient in enumerate(poly):
        for power in range(exponent + 1):
            output[power] += (
                leading_scale
                * coefficient
                * math.comb(exponent, power)
                * pow(alpha, power, q)
                * pow(beta, exponent - power, q)
            )
    return tuple(value % q for value in output)


def direct_prime_field_orbit_count(q: int, degree: int) -> int:
    models = {
        coefficients + (1,)
        for coefficients in itertools.product(range(q), repeat=degree)
        if is_squarefree(coefficients + (1,), q)
    }
    unseen = set(models)
    orbit_count = 0
    while unseen:
        representative = next(iter(unseen))
        orbit = {
            affine_transform(representative, alpha, beta, q)
            for alpha in range(1, q)
            for beta in range(q)
        }
        if not orbit <= models:
            raise AssertionError("affine action left the squarefree family")
        unseen -= orbit
        orbit_count += 1
    return orbit_count


class HyperellipticAffineBurnsideTests(unittest.TestCase):
    def test_squarefree_counting_lemmas(self) -> None:
        for q in (3, 5, 7):
            self.assertEqual(subject.squarefree_monic_count(q, 1), q)
            self.assertEqual(subject.squarefree_monic_count(q, 5), q**5 - q**4)
            self.assertEqual(
                subject.squarefree_nonzero_constant_count(q, 1), q - 1
            )
            self.assertEqual(
                subject.squarefree_nonzero_constant_count(q, 2), (q - 1) ** 2
            )

    def test_direct_tiny_orbit_enumerations(self) -> None:
        expected = {(3, 3): 5, (5, 3): 6, (3, 5): 29}
        for (q, degree), orbit_count in expected.items():
            with self.subTest(q=q, degree=degree):
                genus = (degree - 1) // 2
                self.assertEqual(direct_prime_field_orbit_count(q, degree), orbit_count)
                self.assertEqual(
                    subject.burnside_census(q, genus)["coarse_orbit_count"],
                    orbit_count,
                )

    def test_genus_two_specialization(self) -> None:
        expected = {3: 29, 5: 132, 7: 349}
        for q, orbit_count in expected.items():
            row = subject.burnside_census(q, 2)
            self.assertEqual(row["affine_stack_cardinality"], q**3)
            self.assertEqual(row["coarse_orbit_count"], orbit_count)
            self.assertEqual(row["universal_involution_correction"], q - 1)

    def test_all_degree_rational_series_coefficients(self) -> None:
        for q in (3, 5, 7, 9):
            series = subject.affine_orbit_series(q, 9)
            coefficients = series["coefficients_degree_0_up"]
            self.assertEqual(coefficients[0:2], [1, 1])
            for genus in range(1, 5):
                degree = 2 * genus + 1
                self.assertEqual(
                    coefficients[degree],
                    subject.burnside_census(q, genus)["coarse_orbit_count"],
                )
        for q, maximum_degree in ((3, 5), (5, 3)):
            coefficients = subject.affine_orbit_series(q, maximum_degree)[
                "coefficients_degree_0_up"
            ]
            for degree in range(maximum_degree + 1):
                with self.subTest(q=q, degree=degree):
                    self.assertEqual(
                        coefficients[degree],
                        direct_prime_field_orbit_count(q, degree),
                    )
        with self.assertRaisesRegex(ValueError, "maximum_degree"):
            subject.affine_orbit_series(3, subject.MAX_SERIES_DEGREE + 1)

    def test_involution_is_the_leading_fixed_genus_correction(self) -> None:
        for genus in range(1, 9):
            row = subject.burnside_census(25, genus)
            expected = (25**genus - (-1) ** genus) // 26
            self.assertEqual(row["universal_involution_correction"], expected)
            self.assertGreaterEqual(row["lower_order_correction"], 0)

    def test_translation_and_scaling_exception_strata(self) -> None:
        genus_one_char_three = subject.burnside_census(9, 1)
        self.assertEqual(
            genus_one_char_three["closed_divisor_sum"]["translation_correction"],
            1,
        )
        genus_three_char_seven = subject.burnside_census(7, 3)
        self.assertEqual(
            genus_three_char_seven["closed_divisor_sum"]["translation_correction"],
            1,
        )
        q13_g3_orders = {
            row["order"]
            for row in subject.burnside_census(13, 3)["fixed_loci"][
                "nontrivial_scalings"
            ]
        }
        self.assertEqual(q13_g3_orders, {2, 3, 6})

    def test_scope_refusals_and_frozen_source_lock(self) -> None:
        for q in (2, 4, 8, 15):
            with self.subTest(q=q):
                with self.assertRaises(ValueError):
                    subject.burnside_census(q, 2)
        with self.assertRaisesRegex(ValueError, "genus"):
            subject.burnside_census(3, 0)
        fixture = subject.build_fixture()
        stored = json.loads(
            (FUNCTION_FIELD / "hyperelliptic_affine_burnside.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, fixture)
        source = Path(subject.__file__).read_text(encoding="utf-8").replace(
            "\r\n", "\n"
        )
        self.assertEqual(
            fixture["producer"]["source_sha256_lf_normalized"],
            hashlib.sha256(source.encode()).hexdigest(),
        )
        note = (FUNCTION_FIELD / "HYPERELLIPTIC_AFFINE_BURNSIDE.md").read_text(
            encoding="utf-8"
        ).replace("\r\n", "\n")
        self.assertEqual(
            fixture["producer"]["note_sha256_lf_normalized"],
            hashlib.sha256(note.encode()).hexdigest(),
        )
        self.assertIn("not unpointed", fixture["firewall"])


if __name__ == "__main__":
    unittest.main()
