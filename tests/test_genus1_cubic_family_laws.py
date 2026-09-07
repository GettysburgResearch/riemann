"""Exact tests for the genus-one monic-cubic family laws."""

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

import genus1_cubic_family_laws as subject  # noqa: E402


def as_fraction(pair: list[int]) -> Fraction:
    return Fraction(*pair)


class GenusOneCubicFamilyLawTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            row["q"]: row for row in cls.fixture["finite_regressions"]
        }

    def test_family_size_trace_symmetry_and_model_moments(self) -> None:
        for q, row in self.by_q.items():
            self.assertEqual(row["candidate_cubics_inspected"], q**3)
            self.assertEqual(row["squarefree_model_count"], q**2 * (q - 1))
            histogram = {int(key): value for key, value in row["model_trace_histogram"].items()}
            self.assertEqual(histogram, {-trace: count for trace, count in histogram.items()})
            moments = {
                int(key): value
                for key, value in row[
                    "model_moment_sums_degrees_0_through_12"
                ].items()
            }
            for degree in range(13):
                self.assertEqual(
                    moments[degree], subject.model_trace_moment_sum(degree, q)
                )
                if degree % 2:
                    self.assertEqual(moments[degree], 0)

    def test_explicit_stack_moments_and_first_cusp_term(self) -> None:
        for q in (3, 5, 7, 11, 13):
            theta = subject.delta_frobenius_trace(q)
            expected = {
                0: q,
                1: q**2 - 1,
                2: 2 * q**3 - 3 * q - 1,
                3: 5 * q**4 - 9 * q**2 - 5 * q - 1,
                4: 14 * q**5 - 28 * q**3 - 20 * q**2 - 7 * q - 1,
                5: (
                    42 * q**6
                    - 90 * q**4
                    - 75 * q**3
                    - 35 * q**2
                    - 9 * q
                    - 1
                    - theta
                ),
                6: (
                    132 * q**7
                    - 297 * q**5
                    - 275 * q**4
                    - 154 * q**3
                    - 54 * q**2
                    - 11 * q
                    - 1
                    - 11 * q * theta
                ),
            }
            for half_degree, value in expected.items():
                self.assertEqual(
                    subject.elliptic_stack_even_trace_moment(half_degree, q),
                    value,
                )

        self.assertEqual(subject.ramanujan_tau(3), 252)
        self.assertEqual(subject.ramanujan_tau(5), 4830)
        self.assertEqual(subject.ramanujan_tau(7), -16744)
        self.assertEqual(subject.ramanujan_tau(11), 534612)
        self.assertEqual(subject.ramanujan_tau(13), -577738)

    def test_prime_power_frobenius_trace_is_not_tau_of_q(self) -> None:
        theta_9 = 252**2 - 2 * 3**11
        self.assertEqual(theta_9, -290790)
        self.assertEqual(subject.delta_frobenius_trace(9), theta_9)
        self.assertNotEqual(theta_9, -113643)  # tau(9)
        self.assertEqual(
            subject.elliptic_stack_even_trace_moment(5, 9), 21963230
        )
        self.assertEqual(
            subject.elliptic_stack_even_trace_moment(6, 9), 640681550
        )

    def test_symmetric_character_and_usp2_laws(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25):
            self.assertEqual(subject.symmetric_character_stack_sum(0, q), q)
            for symmetric_power in (1, 3, 5, 7):
                self.assertEqual(
                    subject.symmetric_character_stack_sum(symmetric_power, q), 0
                )
            for symmetric_power in (2, 4, 6, 8, 12):
                self.assertEqual(
                    subject.symmetric_character_stack_sum(symmetric_power, q), -1
                )
            expected_tenth = -1 - subject.delta_frobenius_trace(q)
            self.assertEqual(
                subject.symmetric_character_stack_sum(10, q), expected_tenth
            )
        self.assertEqual(
            [subject.catalan(index) for index in range(7)],
            [1, 1, 2, 5, 14, 42, 132],
        )
        self.assertEqual(
            [subject.ballot_coefficient(6, index) for index in range(7)],
            [132, 297, 275, 154, 54, 11, 1],
        )

    def test_two_quotients_have_different_exact_orbit_laws(self) -> None:
        expected = {
            3: (5, 8),
            5: (6, 12),
            7: (10, 18),
            11: (12, 22),
            13: (16, 32),
        }
        for q, (branch_count, elliptic_count) in expected.items():
            self.assertEqual(subject.branch_affine_orbit_count(q), branch_count)
            self.assertEqual(
                subject.elliptic_isomorphism_class_count(q), elliptic_count
            )
            row = self.by_q[q]
            self.assertEqual(
                row["full_affine_branch_orbits"]["orbit_count"], branch_count
            )
            self.assertEqual(
                row["elliptic_square_affine_orbits"]["orbit_count"],
                elliptic_count,
            )

        self.assertEqual(subject.branch_affine_orbit_count(9), 11)
        self.assertEqual(subject.elliptic_isomorphism_class_count(9), 22)
        self.assertEqual(subject.branch_affine_orbit_count(13), 16)
        self.assertEqual(subject.elliptic_isomorphism_class_count(13), 32)

    def test_effective_elliptic_stabilizer_regressions(self) -> None:
        expected = {
            3: {"1": 5, "3": 3},
            5: {"1": 8, "2": 4},
            7: {"1": 12, "3": 6},
            11: {"1": 22},
            13: {"1": 22, "2": 4, "3": 6},
        }
        for q, histogram in expected.items():
            self.assertEqual(
                self.by_q[q]["elliptic_square_affine_orbits"][
                    "stabilizer_order_histogram"
                ],
                histogram,
            )

    def test_all_q_coarse_even_moment_corrections(self) -> None:
        # q=3: the characteristic-three Artin--Schreier stratum.
        self.assertEqual(subject.characteristic_three_translation_correction(1, 3), 12)
        self.assertEqual(subject.characteristic_three_translation_correction(2, 3), 108)
        # q=5: the j=1728 quartic-twist stratum.
        self.assertEqual(subject.elliptic_coarse_even_trace_moment_sum(1, 5), 68)
        # q=7: the j=0 sextic-twist stratum.
        self.assertEqual(subject.elliptic_coarse_even_trace_moment_sum(1, 7), 152)
        # q=11: no positive-moment fixed-stratum correction.
        self.assertEqual(subject.elliptic_coarse_even_trace_moment_sum(1, 11), 240)
        # q=13: order-two and order-three CM corrections occur together.
        self.assertEqual(subject.elliptic_coarse_even_trace_moment_sum(1, 13), 492)

        # Prime-power CM coordinates must power a representation of p; an
        # arbitrary representation of q gives wrong fourth and higher moments.
        self.assertEqual(
            tuple(map(abs, subject.gaussian_frobenius_coordinates(25))), (3, 4)
        )
        self.assertEqual(subject.eisenstein_frobenius_coordinates(25), (5, 0))
        self.assertEqual(
            tuple(map(abs, subject.eisenstein_frobenius_coordinates(49))), (1, 4)
        )
        self.assertEqual(
            subject.elliptic_coarse_even_trace_moment_sum(2, 25), 82740
        )

        for q, row in self.by_q.items():
            elliptic = row["elliptic_square_affine_orbits"]["even_moment_sums"]
            branch = row["full_affine_branch_orbits"]["even_moment_sums"]
            for degree in range(2, 13, 2):
                half_degree = degree // 2
                self.assertEqual(
                    elliptic[str(degree)],
                    subject.elliptic_coarse_even_trace_moment_sum(half_degree, q),
                )
                self.assertEqual(branch[str(degree)] * 2, elliptic[str(degree)])

    def test_characteristic_three_extension_parity_correction(self) -> None:
        for half_degree in range(1, 7):
            self.assertEqual(
                subject.characteristic_three_translation_correction(
                    half_degree, 27
                ),
                4 * 3 ** (half_degree - 1) * 27**half_degree,
            )
            self.assertEqual(
                subject.characteristic_three_translation_correction(
                    half_degree, 9
                ),
                2 * (4**half_degree + 2) * 9**half_degree // 3,
            )

    def test_full_affine_nonsquares_flip_trace(self) -> None:
        q = 5
        models = subject._prime_model_census(q)
        polynomial = next(
            polynomial for polynomial, trace in models.items() if trace != 0
        )
        trace = models[polynomial]
        nonsquare_transform = subject._affine_transform_prime(
            polynomial, 2, 0, q
        )
        square_transform = subject._affine_transform_prime(polynomial, 4, 1, q)
        self.assertEqual(models[nonsquare_transform], -trace)
        self.assertEqual(models[square_transform], trace)

    def test_measure_bounds_and_scope_firewall(self) -> None:
        for q in (3, 5, 7, 11, 13, 25, 27):
            laws = subject.quotient_measure_laws(q)
            self.assertEqual(laws["actual_elliptic_stack_cardinality"], q)
            self.assertEqual(laws["effective_elliptic_stack_cardinality"], 2 * q)
            self.assertLessEqual(
                as_fraction(
                    laws[
                        "elliptic_coarse_vs_model_stack_total_variation_upper_bound"
                    ]
                ),
                Fraction(4, q),
            )
        firewall = self.fixture["scope_firewall"]
        self.assertTrue(
            firewall[
                "full_affine_branch_orbits_are_not_elliptic_isomorphism_classes"
            ]
        )
        self.assertTrue(
            firewall["signed_trace_does_not_descend_to_full_affine_branch_orbits"]
        )
        self.assertTrue(
            firewall["uniform_models_equal_normalized_elliptic_stack_measure"]
        )

    def test_fixture_hashes_resource_cap_and_input_refusals(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "genus1_cubic_family_laws.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        source = Path(subject.__file__).read_text(encoding="utf-8").replace(
            "\r\n", "\n"
        )
        note = (FUNCTION_FIELD / "GENUS1_CUBIC_FAMILY_LAWS.md").read_text(
            encoding="utf-8"
        ).replace("\r\n", "\n")
        self.assertEqual(
            self.fixture["producer"]["source_sha256_lf_normalized"],
            hashlib.sha256(source.encode()).hexdigest(),
        )
        self.assertEqual(
            self.fixture["producer"]["note_sha256_lf_normalized"],
            hashlib.sha256(note.encode()).hexdigest(),
        )
        self.assertEqual(
            self.fixture["resource_contract"]["candidate_cubics_inspected"],
            4023,
        )
        with self.assertRaisesRegex(ValueError, "candidate count"):
            subject.build_fixture((29,))
        with self.assertRaisesRegex(ValueError, "distinct"):
            subject.build_fixture((3, 3))
        for invalid_q in (2, 4, 8, 15):
            with self.subTest(q=invalid_q):
                with self.assertRaises(ValueError):
                    subject.quotient_measure_laws(invalid_q)


if __name__ == "__main__":
    unittest.main()
