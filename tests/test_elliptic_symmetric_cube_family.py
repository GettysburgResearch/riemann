"""Independent exact tests for the elliptic symmetric-cube packet."""

from __future__ import annotations

import hashlib
import json
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_symmetric_cube_family as subject  # noqa: E402


def direct_factor_from_integral_roots(alpha: int, beta: int) -> tuple[int, ...]:
    q = alpha * beta
    roots = (alpha**3, q * alpha, q * beta, beta**3)
    coefficients = [1]
    for root in roots:
        following = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            following[degree] += coefficient
            following[degree + 1] -= root * coefficient
        coefficients = following
    return tuple(coefficients)


class EllipticSymmetricCubeFamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.frozen = {
            row["q"]: row for row in cls.fixture["frozen_histogram_transforms"]
        }

    def test_closed_newton_and_direct_root_derivations(self) -> None:
        for alpha, beta in ((1, 3), (2, 5), (-1, -3), (-2, -5), (3, 7)):
            q = alpha * beta
            A = -(alpha + beta)
            direct = direct_factor_from_integral_roots(alpha, beta)
            self.assertEqual(subject.sym3_coefficients_closed(A, q), direct)
            self.assertEqual(subject.sym3_coefficients_via_newton(A, q), direct)

        # Explicitly pin the source sign bridge: q=5, geometric trace t=1,
        # hence A=-1 and Sym^3 trace S=1^3-2*5*1=-9.
        self.assertEqual(
            subject.sym3_coefficients_closed(-1, 5),
            (1, 9, 180, 1125, 15625),
        )
        self.assertEqual(-subject.sym3_coefficients_closed(-1, 5)[1], -9)

    def test_normalized_curve_and_cleared_integral_identity(self) -> None:
        for t0 in (
            Fraction(-2),
            Fraction(-3, 2),
            Fraction(-1),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1),
            Fraction(2),
        ):
            x = t0**3 - 2 * t0
            y = t0**4 - 3 * t0**2 + 2
            self.assertEqual(subject.coefficient_curve_value(x, y), 0)
            if x * x != y:
                self.assertEqual(x * (y - 1) / (x * x - y), t0)

        for q, row in self.frozen.items():
            for atom in row["transformed_atoms"]:
                self.assertEqual(
                    subject.scaled_coefficient_curve_value(
                        atom["sym3_trace_S"],
                        atom["reduced_second_coefficient_D"],
                        q,
                    ),
                    0,
                )
                coefficients = tuple(atom["polynomial_coefficients_T0_through_T4"])
                self.assertEqual(coefficients[3], q**3 * coefficients[1])
                self.assertEqual(coefficients[4], q**6)

    def test_nodes_tangent_cones_and_no_cusp_certificate(self) -> None:
        singular_points = ((-1, 1), (0, 0), (1, 1))
        tangent_cones = {
            (-1, 1): (-4, -2, 1),
            (0, 0): (1, 0, -2),
            (1, 1): (-4, 2, 1),
        }
        for x, y in singular_points:
            F = -x**4 + x * x * y + x * x + y**3 - 2 * y * y
            Fx = -4 * x**3 + 2 * x * y + 2 * x
            Fy = x * x + 3 * y * y - 4 * y
            self.assertEqual((F, Fx, Fy), (0, 0, 0))
            quadratic = (
                (-12 * x * x + 2 * y + 2) // 2,
                2 * x,
                (6 * y - 4) // 2,
            )
            self.assertEqual(quadratic, tangent_cones[(x, y)])
            # b^2-4ac is nonzero and positive: two distinct real tangents.
            a, b, c = quadratic
            self.assertGreater(b * b - 4 * a * c, 0)

        # Completeness reduction for the singular locus.  In the Fx branch
        # y=2r-1, r=x^2, the remaining equations factor as below and share
        # only r=1; the x=0 branch shares only y=0.
        for r in range(-5, 6):
            y = 2 * r - 1
            restricted_F = -r * r + r * y + r + y**3 - 2 * y * y
            restricted_Fy = r + 3 * y * y - 4 * y
            self.assertEqual(restricted_F, (r - 1) ** 2 * (8 * r - 3))
            self.assertEqual(restricted_Fy, (r - 1) * (12 * r - 7))

        # Common normalization factors for the two preimages of each node.
        # x-1=(t+1)(t^2-t-1), x+1=(t-1)(t^2+t-1), and
        # y-1=(t^2-t-1)(t^2+t-1); y=(t^2-1)(t^2-2).
        for t in range(-5, 6):
            x = t**3 - 2 * t
            y = t**4 - 3 * t * t + 2
            self.assertEqual(x - 1, (t + 1) * (t * t - t - 1))
            self.assertEqual(x + 1, (t - 1) * (t * t + t - 1))
            self.assertEqual(y - 1, (t * t - t - 1) * (t * t + t - 1))
            self.assertEqual(y, (t * t - 1) * (t * t - 2))

        # If dx/dt=0 then t^2=2/3, and the nonzero factor in dy/dt is
        # 2t^2-3=-5/3.  Also t cannot be zero.  Hence there is no cusp.
        self.assertEqual(2 * Fraction(2, 3) - 3, Fraction(-5, 3))
        self.assertNotEqual(Fraction(2, 3), 0)
        self.assertEqual(subject.coefficient_curve_value(Fraction(0), Fraction(-2)), -16)

        false_positive = self.fixture["rank_one_coefficient_curve"][
            "odd_q_arithmetic_false_positive"
        ]
        self.assertEqual(false_positive["coefficient_point"], [0, 0])
        self.assertEqual(subject.coefficient_curve_value(Fraction(0), Fraction(0)), 0)
        for q in (3, 5, 7, 9, 11, 13, 25, 27):
            self.assertNotEqual(math.isqrt(2 * q) ** 2, 2 * q)
        self.assertIn("not sufficient", false_positive["conclusion"])

    def test_odd_q_integral_trace_map_has_no_arithmetic_fold_collision(self) -> None:
        residues = {
            (first * first + first * second + second * second) % 4
            for first in range(4)
            for second in range(4)
        }
        self.assertEqual(residues, {0, 1, 3})
        for q in (3, 5, 7, 9, 11, 13, 25):
            seen: dict[int, int] = {}
            for trace in range(-4 * q, 4 * q + 1):
                image = trace**3 - 2 * q * trace
                self.assertNotIn(image, seen)
                seen[image] = trace
            for first in range(-10, 11):
                for second in range(-10, 11):
                    self.assertEqual(
                        (first**3 - 2 * q * first)
                        - (second**3 - 2 * q * second),
                        subject.sym3_trace_difference_factor(first, second, q),
                    )
        self.assertEqual(0**3 - 2 * 2 * 0, 2**3 - 2 * 2 * 2)
        theorem = self.fixture["odd_q_arithmetic_lattice_avoidance"]
        self.assertEqual(
            theorem["mod_4_certificate"]["values_of_r2_rs_s2_mod_4"],
            [0, 1, 3],
        )
        self.assertFalse(theorem["hasse_bound_needed"])

    def test_su2_character_decompositions(self) -> None:
        expected = {
            "trace_square_x2": {0: 1, 2: 1, 4: 1, 6: 1},
            "second_coefficient_y": {0: 1, 4: 1},
            "second_coefficient_square_y2": {0: 2, 2: 1, 4: 3, 6: 1, 8: 1},
            "trace_square_times_second_x2y": {
                0: 2,
                2: 4,
                4: 5,
                6: 4,
                8: 2,
                10: 1,
            },
            "trace_fourth_x4": {
                0: 4,
                2: 9,
                4: 11,
                6: 10,
                8: 6,
                10: 3,
                12: 1,
            },
            "second_coefficient_cube_y3": {
                0: 5,
                2: 6,
                4: 11,
                6: 7,
                8: 6,
                10: 2,
                12: 1,
            },
        }
        for name, decomposition in expected.items():
            trace_power, e2_power = subject.ALL_Q_OBSERVABLES[name]
            polynomial = subject.observable_polynomial(trace_power, e2_power)
            self.assertEqual(
                subject.decompose_into_su2_characters(polynomial), decomposition
            )

    def test_thin_and_generic_compact_moments(self) -> None:
        comparison = self.fixture["compact_haar_comparison"]
        trace = comparison["trace_moments_degrees_0_through_12"]
        self.assertEqual(
            trace["sym3_su2"],
            [1, 0, 1, 0, 4, 0, 34, 0, 364, 0, 4269, 0, 52844],
        )
        self.assertEqual(
            trace["generic_usp4"],
            [1, 0, 1, 0, 3, 0, 14, 0, 84, 0, 594, 0, 4719],
        )
        e2 = comparison["second_coefficient_moments_degrees_0_through_6"]
        self.assertEqual(e2["sym3_su2"], [1, 1, 2, 5, 16, 62, 272])
        self.assertEqual(e2["generic_usp4"], [1, 1, 2, 4, 10, 27, 82])
        mixed = {row["trace_power"]: row for row in comparison["mixed_moments"]}
        self.assertEqual(mixed[2]["sym3_su2"], [1, 2, 7, 29, 131])
        self.assertEqual(mixed[2]["generic_usp4"], [1, 2, 5, 14, 43])

    def test_all_q_expectations_have_two_independent_routes(self) -> None:
        # Include a prime-power value and the source packet's exact Delta trace.
        cases = ((3, 252), (9, -290790), (13, -577738))
        for q, theta12 in cases:
            for name, (trace_power, e2_power) in subject.ALL_Q_OBSERVABLES.items():
                polynomial = subject.observable_polynomial(trace_power, e2_power)
                via_moments = subject.observable_expectation_via_base_moments(
                    polynomial, q, theta12
                )
                via_characters = subject.observable_expectation_via_characters(
                    polynomial, q, theta12
                )
                self.assertEqual(via_moments, via_characters, name)

        q = 9
        theta12 = -290790
        self.assertEqual(
            subject.observable_expectation_via_characters(
                subject.observable_polynomial(2, 0), q, theta12
            ),
            1 - Fraction(1, q**2) - Fraction(1, q**3) - Fraction(1, q**4),
        )
        self.assertEqual(
            subject.observable_expectation_via_characters(
                subject.observable_polynomial(0, 1), q, theta12
            ),
            1 - Fraction(1, q**3),
        )

    def test_frozen_transforms_use_only_source_histograms(self) -> None:
        source = json.loads(subject.SOURCE_FIXTURE.read_text(encoding="utf-8"))
        source_rows = {row["q"]: row for row in source["finite_regressions"]}
        self.assertEqual(set(self.frozen), {3, 5, 7, 11, 13})
        self.assertEqual(
            sum(row["source_histogram_atom_count"] for row in self.frozen.values()),
            55,
        )
        self.assertEqual(
            sum(row["source_members_represented"] for row in self.frozen.values()),
            3650,
        )
        expected_theta12 = {
            3: 252,
            5: 4830,
            7: -16744,
            11: 534612,
            13: -577738,
        }
        for q, transformed in self.frozen.items():
            self.assertEqual(
                transformed["theta12_frobenius_trace"], expected_theta12[q]
            )
            source_histogram = {
                int(trace): count
                for trace, count in source_rows[q]["model_trace_histogram"].items()
            }
            expected_trace_histogram: dict[int, int] = {}
            for trace, count in source_histogram.items():
                image = trace**3 - 2 * q * trace
                expected_trace_histogram[image] = (
                    expected_trace_histogram.get(image, 0) + count
                )
            self.assertEqual(
                transformed["sym3_trace_histogram"],
                {str(key): expected_trace_histogram[key] for key in sorted(expected_trace_histogram)},
            )
            self.assertTrue(
                transformed["source_to_full_factor_map_is_injective_on_frozen_support"]
            )
            self.assertTrue(
                transformed["source_to_sym3_trace_map_is_injective_on_frozen_support"]
            )
            for observable in transformed["exact_model_stack_observable_averages"].values():
                self.assertEqual(
                    observable["routes_agree"],
                    ["source_histogram", "base_moments", "SU2_characters"],
                )

    def test_source_payload_file_locks_and_scope_firewall(self) -> None:
        source_text = subject.SOURCE_FIXTURE.read_text(encoding="utf-8").replace(
            "\r\n", "\n"
        )
        self.assertEqual(
            hashlib.sha256(source_text.encode()).hexdigest(),
            subject.EXPECTED_SOURCE_FILE_SHA256_LF,
        )
        source = json.loads(source_text)
        self.assertEqual(
            source["payload_sha256"], subject.EXPECTED_SOURCE_PAYLOAD_SHA256
        )
        unhashed_source = dict(source)
        source_payload_hash = unhashed_source.pop("payload_sha256")
        self.assertEqual(
            source_payload_hash, subject._canonical_sha256(unhashed_source)
        )
        firewall = self.fixture["scope_firewall"]
        self.assertTrue(firewall["representation_image_not_generic_usp4"])
        self.assertTrue(
            firewall[
                "local_factor_algebra_does_not_assert_a_new_variety_realizing_each_factor"
            ]
        )
        self.assertTrue(
            firewall["actual_elliptic_h1_symmetric_cube_is_a_genuine_l_adic_representation"]
        )
        self.assertTrue(
            firewall["coefficient_curve_alone_does_not_prove_global_recognition_or_descent"]
        )
        self.assertTrue(
            firewall[
                "coefficient_curve_alone_does_not_certify_local_arithmetic_sym3_origin"
            ]
        )
        self.assertTrue(
            firewall["classical_global_automorphy_is_not_needed_or_reproved_here"]
        )
        self.assertEqual(
            self.fixture["resource_contract"]["new_curve_or_field_enumerations"], 0
        )
        self.assertLessEqual(
            self.fixture["resource_contract"]["laurent_product_pairs"],
            self.fixture["resource_contract"]["laurent_product_pair_cap"],
        )
        references = self.fixture["literature_boundary"][
            "classical_primary_references"
        ]
        self.assertEqual(
            [reference["url"] for reference in references],
            [
                "https://arxiv.org/abs/math/9909198",
                "https://arxiv.org/abs/math/0409607",
            ],
        )
        self.assertIn(
            "odd-q integral-trace injectivity across the real folds",
            self.fixture["literature_boundary"]["project_specific_calculations"],
        )

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(self.fixture)

    def test_stored_fixture_hashes_caps_and_refusals(self) -> None:
        stored = json.loads(
            (FUNCTION_FIELD / "elliptic_symmetric_cube_family.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(stored, self.fixture)
        unhashed = dict(self.fixture)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        producer = self.fixture["producer"]
        for path, field in (
            (Path(subject.__file__), "source_sha256_lf_normalized"),
            (FUNCTION_FIELD / "ELLIPTIC_SYMMETRIC_CUBE_FAMILY.md", "note_sha256_lf_normalized"),
            (Path(__file__), "test_sha256_lf_normalized"),
        ):
            text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
            self.assertEqual(producer[field], hashlib.sha256(text.encode()).hexdigest())

        with self.assertRaisesRegex(ValueError, "at least one"):
            subject.build_fixture(())
        with self.assertRaisesRegex(ValueError, "distinct"):
            subject.build_fixture((3, 3))
        with self.assertRaisesRegex(ValueError, "absent"):
            subject.build_fixture((17,))
        with self.assertRaises(ValueError):
            subject.sym3_coefficients_via_newton(1, 0)


if __name__ == "__main__":
    unittest.main()
