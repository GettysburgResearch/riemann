"""Exact tests for the genus-two model/stack measure identity."""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_family_measures as subject  # noqa: E402


def as_fraction(pair: list[int]) -> Fraction:
    return Fraction(*pair)


class FamilyMeasureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {row["q"]: row for row in cls.fixture["families"]}

    def test_all_q_stack_identity_is_replayed_on_frozen_fields(self) -> None:
        for q, row in self.by_q.items():
            self.assertEqual(row["member_count"], q**5 - q**4)
            self.assertEqual(row["group_order"], q * (q - 1))
            self.assertEqual(as_fraction(row["quotient_stack_cardinality"]), q**3)

    def test_exact_burnside_orbit_formula_and_fixed_loci(self) -> None:
        expected = {
            3: (29, {"identity": 162, "order_2_scalings": 12}),
            5: (
                132,
                {
                    "identity": 2500,
                    "order_2_scalings": 80,
                    "order_4_scalings": 40,
                    "nonidentity_translations": 20,
                },
            ),
            7: (349, {"identity": 14406, "order_2_scalings": 252}),
        }
        for q, (orbit_count, nonzero_contributions) in expected.items():
            census = self.by_q[q]["burnside_census"]
            self.assertEqual(census["orbit_count"], orbit_count)
            self.assertEqual(census["closed_formula_value"], orbit_count)
            actual_nonzero = {
                key: value
                for key, value in census["fixed_point_contribution_sums"].items()
                if value
            }
            self.assertEqual(actual_nonzero, nonzero_contributions)

        q11 = subject.burnside_census(11)
        self.assertEqual(q11["orbit_count"], 11**3 + 10 + 4)
        self.assertEqual(
            q11["fixed_point_contribution_sums"]["order_5_scalings"],
            4 * 11 * 10,
        )
        q25 = subject.burnside_census(25)
        self.assertEqual(q25["orbit_count"], 25**3 + 24 + 2 + 1)
        q49 = subject.burnside_census(49)
        self.assertEqual(q49["characteristic"], 7)
        self.assertEqual(q49["orbit_count"], 49**3 + 48 + 2)
        with self.assertRaisesRegex(ValueError, "prime power"):
            subject.burnside_census(15)
        for even_q in (2, 4, 8, 16):
            with self.subTest(q=even_q):
                with self.assertRaisesRegex(ValueError, "only for odd q"):
                    subject.burnside_census(even_q)

    def test_exact_measure_distortions(self) -> None:
        expected = {
            3: (
                Fraction(50, 783),
                Fraction(2, 27),
                Fraction(19, 29),
                Fraction(17, 27),
            ),
            5: (
                Fraction(77, 1500),
                Fraction(7, 125),
                Fraction(43, 66),
                Fraction(33, 50),
            ),
            7: (
                Fraction(2022, 119707),
                Fraction(6, 343),
                Fraction(237, 349),
                Fraction(33, 49),
            ),
        }
        for q, (tv, tv_bound, coarse_negative, stack_negative) in expected.items():
            row = self.by_q[q]
            self.assertEqual(
                as_fraction(
                    row["total_variation_uniform_orbits_vs_model_affine_stack"]
                ),
                tv,
            )
            self.assertEqual(
                as_fraction(row["total_variation_from_free_orbit_deficit"]),
                tv,
            )
            self.assertEqual(
                as_fraction(row["universal_total_variation_upper_bound"]),
                tv_bound,
            )
            self.assertLessEqual(tv, tv_bound)
            negative = row["sign_measures"]["negative"]
            self.assertEqual(
                as_fraction(negative["uniform_coarse_orbit_fraction"]),
                coarse_negative,
            )
            self.assertEqual(
                as_fraction(negative["uniform_model_equals_affine_stack_fraction"]),
                stack_negative,
            )

    def test_nonfree_locus_and_maximal_q5_amplification(self) -> None:
        expected = {
            3: (Fraction(4, 29), Fraction(2, 27)),
            5: (Fraction(1, 12), Fraction(4, 125)),
            7: (Fraction(12, 349), Fraction(6, 343)),
        }
        for q, (coarse, stack) in expected.items():
            row = self.by_q[q]["nonfree_locus"]
            self.assertEqual(as_fraction(row["uniform_orbit_fraction"]), coarse)
            self.assertEqual(
                as_fraction(row["uniform_model_equals_affine_stack_fraction"]), stack
            )
        q5_strata = {
            row["stabilizer_order"]: row for row in self.by_q[5]["stabilizer_strata"]
        }
        fixed = q5_strata[20]
        self.assertEqual(fixed["orbit_size"], 1)
        self.assertEqual(as_fraction(fixed["stack_weight_each"]), Fraction(1, 2500))
        self.assertEqual(
            as_fraction(fixed["coarse_to_stack_weight_ratio"]), Fraction(625, 33)
        )

    def test_fixture_source_locks_and_scope(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "genus2_family_measures.json").read_text(encoding="utf-8")
        )
        self.assertEqual(stored, self.fixture)
        source = Path(subject.__file__).read_text(encoding="utf-8").replace("\r\n", "\n")
        self.assertEqual(
            self.fixture["producer"]["source_sha256_lf_normalized"],
            hashlib.sha256(source.encode("utf-8")).hexdigest(),
        )
        scope = self.fixture["scope"]
        self.assertTrue(scope["not_the_full_curve_isomorphism_stack"])
        self.assertTrue(scope["marked_infinity_affine_model_quotient_only"])
        self.assertTrue(scope["frozen_measure_distortions_are_not_asymptotic_laws"])

    def test_resource_cap_refuses_oversized_contract(self) -> None:
        with self.assertRaisesRegex(ValueError, "input-byte cap"):
            subject.build_fixture(maximum_input_bytes=subject.MAX_INPUT_BYTES + 1)
        with self.assertRaisesRegex(ValueError, "above cap"):
            subject.build_fixture(maximum_input_bytes=1)


if __name__ == "__main__":
    unittest.main()
