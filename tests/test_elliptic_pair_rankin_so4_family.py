"""Independent exact tests for the elliptic-pair Rankin/SO(4) packet."""

from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_pair_rankin_so4_family as subject  # noqa: E402


def direct_tensor_factor(
    alpha: int, beta: int, gamma: int, delta: int
) -> tuple[int, ...]:
    roots = (
        alpha * gamma,
        alpha * delta,
        beta * gamma,
        beta * delta,
    )
    coefficients = [1]
    for root in roots:
        following = [0] * (len(coefficients) + 1)
        for degree, coefficient in enumerate(coefficients):
            following[degree] += coefficient
            following[degree + 1] -= root * coefficient
        coefficients = following
    return tuple(coefficients)


def laurent_multiply(
    left: dict[tuple[int, ...], int], right: dict[tuple[int, ...], int]
) -> dict[tuple[int, ...], int]:
    output: Counter[tuple[int, ...]] = Counter()
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            output[
                tuple(a + b for a, b in zip(left_exponent, right_exponent))
            ] += left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in output.items() if coefficient}


def weyl_density(positive_roots: tuple[tuple[int, ...], ...]) -> dict[tuple[int, ...], int]:
    dimensions = len(positive_roots[0])
    density = {(0,) * dimensions: 1}
    for root in positive_roots:
        for signed_root in (root, tuple(-coordinate for coordinate in root)):
            density = laurent_multiply(
                density,
                {(0,) * dimensions: 1, signed_root: -1},
            )
    return density


def weyl_trace_moments(
    trace: dict[tuple[int, ...], int],
    positive_roots: tuple[tuple[int, ...], ...],
    weyl_order: int,
    maximum: int,
) -> list[int]:
    dimensions = len(next(iter(trace)))
    density = weyl_density(positive_roots)
    power = {(0,) * dimensions: 1}
    moments = []
    for _ in range(maximum + 1):
        constant_term = laurent_multiply(power, density).get((0,) * dimensions, 0)
        if constant_term % weyl_order:
            raise ArithmeticError("independent Weyl constant term lost divisibility")
        moments.append(constant_term // weyl_order)
        power = laurent_multiply(power, trace)
    return moments


class EllipticPairRankinSO4FamilyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.frozen = {
            row["q"]: row
            for row in cls.fixture["frozen_histogram_cartesian_transforms"]
        }

    def test_closed_newton_and_direct_root_derivations(self) -> None:
        root_cases = (
            (1, 9, 3, 3),
            (1, 25, 5, 5),
            (1, 27, 3, 9),
            (-1, -9, 1, 9),
            (-3, -3, -1, -9),
        )
        for alpha, beta, gamma, delta in root_cases:
            q = alpha * beta
            self.assertEqual(q, gamma * delta)
            A = -(alpha + beta)
            B = -(gamma + delta)
            direct = direct_tensor_factor(alpha, beta, gamma, delta)
            self.assertEqual(subject.tensor_coefficients_closed(A, B, q), direct)
            self.assertEqual(subject.tensor_coefficients_via_newton(A, B, q), direct)

        # Explicitly pin the load-bearing source sign conversion.
        # Source traces t1=1,t2=2 at q=5 mean A=-1,B=-2.
        self.assertEqual(
            subject.tensor_coefficients_closed(-1, -2, 5),
            (1, -2, -25, -50, 625),
        )
        self.assertEqual(
            subject.normalized_coefficients(-1, -2, 5),
            (Fraction(2, 5), Fraction(-1)),
        )

    def test_functional_equation_shape_and_input_symmetries(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49):
            for A, B in ((0, 0), (1, 2), (-1, 3), (2, -4), (-3, -5)):
                coefficients = subject.tensor_coefficients_closed(A, B, q)
                self.assertEqual(coefficients[3], q**2 * coefficients[1])
                self.assertEqual(coefficients[4], q**4)
                self.assertEqual(
                    coefficients, subject.tensor_coefficients_closed(B, A, q)
                )
                self.assertEqual(
                    coefficients, subject.tensor_coefficients_closed(-A, -B, q)
                )
                single_twist = subject.tensor_coefficients_closed(-A, B, q)
                self.assertEqual(single_twist[2], coefficients[2])
                self.assertEqual(single_twist[1], -coefficients[1])
                self.assertEqual(single_twist[3], -coefficients[3])

    def test_semialgebraic_image_forward_and_converse_certificate(self) -> None:
        for q in (3, 5, 7, 9, 11, 13):
            bound = 2 * math.isqrt(q) + 2
            for A in range(-bound, bound + 1):
                for B in range(-bound, bound + 1):
                    certificate = subject.coefficient_image_certificate(A, B, q)
                    x = certificate["x"]
                    y = certificate["y"]
                    p = certificate["p"]
                    r = certificate["r"]
                    discriminant = certificate["coefficient_map_fold_D"]
                    self.assertEqual(x * x, p * r)
                    self.assertEqual(y, p + r - 2)
                    self.assertEqual(discriminant, (p - r) ** 2)
                    self.assertGreaterEqual(discriminant, 0)

        # Independent exact sufficiency witnesses for the real coefficient
        # criterion: roots of z^2-(y+2)z+x^2 are p and r in [0,4].
        for p, r, sign in (
            (Fraction(1, 4), Fraction(9, 4), 1),
            (Fraction(1), Fraction(4), -1),
            (Fraction(0), Fraction(3), 1),
            (Fraction(4), Fraction(4), -1),
        ):
            product_root = p * r
            numerator = product_root.numerator
            denominator = product_root.denominator
            numerator_root = math.isqrt(numerator)
            denominator_root = math.isqrt(denominator)
            self.assertEqual(numerator_root**2, numerator)
            self.assertEqual(denominator_root**2, denominator)
            x = sign * Fraction(numerator_root, denominator_root)
            y = p + r - 2
            discriminant = (y + 2) ** 2 - 4 * x * x
            self.assertEqual(discriminant, (p - r) ** 2)
            roots = {(y + 2 + abs(p - r)) / 2, (y + 2 - abs(p - r)) / 2}
            self.assertEqual(roots, {p, r})
            self.assertTrue(all(0 <= root <= 4 for root in roots))

    def test_equal_and_opposite_trace_wall_factorizations(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25):
            for A in range(-8, 9):
                equal = subject.tensor_coefficients_closed(A, A, q)
                opposite = subject.tensor_coefficients_closed(A, -A, q)
                self.assertEqual(equal, subject.wall_factorization(A, q, "equal"))
                self.assertEqual(
                    opposite, subject.wall_factorization(A, q, "opposite")
                )
                x_equal, y_equal = subject.normalized_coefficients(A, A, q)
                x_opposite, y_opposite = subject.normalized_coefficients(A, -A, q)
                self.assertEqual((y_equal + 2) ** 2 - 4 * x_equal**2, 0)
                self.assertEqual((y_opposite + 2) ** 2 - 4 * x_opposite**2, 0)

        firewall = self.fixture["coefficient_map_fold_walls"][
            "local_global_firewall"
        ]
        self.assertIn("does not prove", firewall)
        self.assertIn("global", firewall)

    def test_full_quartic_discriminant_has_fold_and_endpoint_components(self) -> None:
        symbolic = subject.full_quartic_symbolic_certificates()
        self.assertEqual(
            set(symbolic),
            {
                "factor_trace_D_residual",
                "factor_trace_E_residual",
                "factor_trace_full_discriminant_residual",
                "squared_base_trace_D_residual",
                "squared_base_trace_E_residual",
                "squared_base_trace_full_discriminant_residual",
            },
        )
        self.assertTrue(all(not residual for residual in symbolic.values()))

        # D=0 but E!=0: equal squared base traces give the coefficient-map fold.
        fold_only = subject.full_quartic_discriminant_certificate(1, -1, 9)
        self.assertEqual(fold_only["coefficient_map_fold_D"], 0)
        self.assertNotEqual(fold_only["hasse_endpoint_factor_E"], 0)
        self.assertTrue(fold_only["on_fold_wall"])
        self.assertFalse(fold_only["on_hasse_endpoint_wall"])
        self.assertTrue(fold_only["has_repeated_quartic_root"])

        # E=0 but D!=0: A is at the Hasse endpoint A^2=4q.  This
        # repeated-root wall would be missed if D were called exhaustive.
        endpoint_only = subject.full_quartic_discriminant_certificate(6, 1, 9)
        self.assertNotEqual(endpoint_only["coefficient_map_fold_D"], 0)
        self.assertEqual(endpoint_only["hasse_endpoint_factor_E"], 0)
        self.assertFalse(endpoint_only["on_fold_wall"])
        self.assertTrue(endpoint_only["on_hasse_endpoint_wall"])
        self.assertTrue(endpoint_only["has_repeated_quartic_root"])

        intersection = subject.full_quartic_discriminant_certificate(6, -6, 9)
        self.assertEqual(intersection["coefficient_map_fold_D"], 0)
        self.assertEqual(intersection["hasse_endpoint_factor_E"], 0)
        self.assertTrue(intersection["on_fold_wall"])
        self.assertTrue(intersection["on_hasse_endpoint_wall"])

        generic = subject.full_quartic_discriminant_certificate(1, 2, 9)
        self.assertFalse(generic["has_repeated_quartic_root"])
        for certificate in (fold_only, endpoint_only, intersection, generic):
            p = certificate["p"]
            r = certificate["r"]
            D = certificate["coefficient_map_fold_D"]
            E = certificate["hasse_endpoint_factor_E"]
            full = certificate["full_quartic_root_discriminant"]
            self.assertEqual(D, (p - r) ** 2)
            self.assertEqual(E, (p - 4) * (r - 4))
            self.assertEqual(full, D * E**2)
            self.assertEqual(full, certificate["resultant_discriminant"])

        theorem = self.fixture["full_reciprocal_quartic_root_discriminant"]
        self.assertIn("D*E^2", theorem["full_identity"])
        self.assertIn("p=4 or r=4", theorem["repeated_root_locus"])
        self.assertIn("not called the full", theorem["normalization_firewall"])

    def test_so4_haar_trace_moments_are_catalan_squares(self) -> None:
        expected = [1, 0, 1, 0, 4, 0, 25, 0, 196, 0, 1764, 0, 17424]
        self.assertEqual(
            [subject.so4_haar_trace_moment(order) for order in range(13)],
            expected,
        )
        for half_order in range(7):
            self.assertEqual(
                subject.so4_haar_trace_moment(2 * half_order),
                subject.catalan(half_order) ** 2,
            )

    def test_cross_family_compact_discriminator_by_independent_weyl_terms(self) -> None:
        sym3_trace = {(3,): 1, (1,): 1, (-1,): 1, (-3,): 1}
        independent_sym3 = weyl_trace_moments(sym3_trace, ((2,),), 2, 6)
        usp4_trace = {
            (1, 0): 1,
            (-1, 0): 1,
            (0, 1): 1,
            (0, -1): 1,
        }
        independent_usp4 = weyl_trace_moments(
            usp4_trace,
            ((2, 0), (0, 2), (1, -1), (1, 1)),
            8,
            6,
        )
        so4 = [subject.so4_haar_trace_moment(order) for order in range(7)]
        sym3 = [subject.sym3_su2_haar_trace_moment(order) for order in range(7)]
        generic = [
            subject.generic_usp4_standard_trace_moment(order)
            for order in range(7)
        ]
        self.assertEqual(so4, [1, 0, 1, 0, 4, 0, 25])
        self.assertEqual(sym3, independent_sym3)
        self.assertEqual(sym3, [1, 0, 1, 0, 4, 0, 34])
        self.assertEqual(generic, independent_usp4)
        self.assertEqual(generic, [1, 0, 1, 0, 3, 0, 14])
        self.assertEqual(so4[:5], sym3[:5])
        self.assertNotEqual(so4[6], sym3[6])

        certificates = subject.sym3_comparison_polynomial_certificates()
        self.assertEqual(certificates["curve_residual"], (0,))
        self.assertEqual(
            certificates["region_discriminant"],
            certificates["expected_region_discriminant"],
        )
        self.assertEqual(
            certificates["region_discriminant"],
            (16, -40, 33, -10, 1),
        )

        # Independently verify the one-dimensional comparison curve.
        for parameter in (
            Fraction(-2),
            Fraction(-3, 2),
            Fraction(-1),
            Fraction(0),
            Fraction(1, 2),
            Fraction(1),
            Fraction(2),
        ):
            x = parameter**3 - 2 * parameter
            y = parameter**4 - 3 * parameter**2 + 2
            self.assertEqual(subject.sym3_coefficient_curve_residual(x, y), 0)
            discriminant = (y + 2) ** 2 - 4 * x * x
            self.assertGreaterEqual(discriminant, 0)
        comparison = self.fixture["compact_image_discriminator"]
        self.assertIn("alias through order 4", comparison["first_trace_moment_separations"]["SO4_vs_Sym3_SU2"])
        self.assertIn("no Sym3 fixture", comparison["upstream_consumption"])
        self.assertIn("not prove finite-family convergence", comparison["scope_firewall"])

    def test_all_q_moment_formulas_have_independent_base_route(self) -> None:
        for q in (3, 5, 7, 9, 11, 13, 25, 27, 49, 121):
            m2 = 1 - Fraction(1, q**2)
            m4 = 2 - Fraction(3, q**2) - Fraction(1, q**3)
            independent = {
                "mean_x_squared": m2**2,
                "mean_x_fourth": m4**2,
                "mean_y": 2 * m2 - 2,
                "mean_y_squared": 2 * m4 + 2 * m2**2 - 8 * m2 + 4,
                "mean_x_squared_times_y": 2 * m4 * m2 - 2 * m2**2,
                "mean_coefficient_map_fold_D": 2 * m4 - 2 * m2**2,
            }
            self.assertEqual(subject.rankin_moments_via_base_moments(q), independent)
            self.assertEqual(subject.rankin_moment_formulas(q), independent)

        q = 9
        self.assertEqual(
            subject.rankin_moment_formulas(q)["mean_y_squared"],
            2
            - Fraction(2, q**2)
            - Fraction(2, q**3)
            + Fraction(2, q**4),
        )

    def test_frozen_histograms_are_complete_cartesian_transforms(self) -> None:
        source = json.loads(subject.SOURCE_FIXTURE_PATH.read_text(encoding="utf-8"))
        source_rows = {row["q"]: row for row in source["finite_regressions"]}
        expected_sizes = {
            3: (7, 18, 49, 324),
            5: (9, 100, 81, 10_000),
            7: (11, 294, 121, 86_436),
            11: (13, 1_210, 169, 1_464_100),
            13: (15, 2_028, 225, 4_112_784),
        }
        self.assertEqual(set(self.frozen), set(expected_sizes))
        self.assertEqual(
            sum(row["source_trace_atom_count"] for row in self.frozen.values()),
            55,
        )
        self.assertEqual(
            sum(row["ordered_cartesian_atom_pairs"] for row in self.frozen.values()),
            645,
        )
        for q, row in self.frozen.items():
            source_histogram = {
                int(trace): count
                for trace, count in source_rows[q]["model_trace_histogram"].items()
            }
            expected_atom_count, members, atom_pairs, pair_members = expected_sizes[q]
            self.assertEqual(len(source_histogram), expected_atom_count)
            self.assertEqual(sum(source_histogram.values()), members)
            self.assertEqual(row["source_members_represented"], members)
            self.assertEqual(row["ordered_cartesian_atom_pairs"], atom_pairs)
            self.assertEqual(row["ordered_model_pairs_represented"], pair_members)

            coefficient_law: Counter[tuple[int, ...]] = Counter()
            coordinate_law: Counter[tuple[Fraction, Fraction]] = Counter()
            trace_law: Counter[Fraction] = Counter()
            equal_mass = opposite_mass = intersection_mass = 0
            for left_trace, left_count in source_histogram.items():
                for right_trace, right_count in source_histogram.items():
                    pair_count = left_count * right_count
                    A, B = -left_trace, -right_trace
                    coefficients = subject.tensor_coefficients_closed(A, B, q)
                    x, y = subject.normalized_coefficients(A, B, q)
                    coefficient_law[coefficients] += pair_count
                    coordinate_law[(x, y)] += pair_count
                    trace_law[x] += pair_count
                    if A == B:
                        equal_mass += pair_count
                    if A == -B:
                        opposite_mass += pair_count
                    if A == B == 0:
                        intersection_mass += pair_count

            stored_coefficients = {
                tuple(atom["coefficients_T0_through_T4"]): atom["pair_count"]
                for atom in row["complete_integral_local_factor_law"]["atoms"]
            }
            stored_coordinates = {
                (Fraction(*atom["x"]), Fraction(*atom["y"])): atom["pair_count"]
                for atom in row["complete_normalized_coefficient_law"]["atoms"]
            }
            stored_trace = {
                Fraction(*atom["x"]): atom["pair_count"]
                for atom in row["normalized_tensor_trace_histogram"]["atoms"]
            }
            self.assertEqual(dict(coefficient_law), stored_coefficients)
            self.assertEqual(dict(coordinate_law), stored_coordinates)
            self.assertEqual(dict(trace_law), stored_trace)
            walls = row["coefficient_map_fold_wall_masses"]
            self.assertEqual(walls["A_equals_B"], equal_mass)
            self.assertEqual(walls["A_equals_minus_B"], opposite_mass)
            self.assertEqual(
                walls["intersection_A_equals_B_equals_zero"], intersection_mass
            )
            self.assertEqual(
                walls["fold_union_D_equals_zero_by_inclusion_exclusion"],
                equal_mass + opposite_mass - intersection_mass,
            )
            repeated = row["full_quartic_repeated_root_masses"]
            self.assertEqual(
                repeated["fold_wall_D_equals_zero"],
                equal_mass + opposite_mass - intersection_mass,
            )
            # All five locked q are nonsquare primes, so integral traces cannot
            # attain A^2=4q.  This zero is a property of these rows, not a
            # deletion of the all-prime-power endpoint component.
            self.assertEqual(repeated["hasse_endpoint_wall_E_equals_zero"], 0)
            self.assertEqual(repeated["fold_and_endpoint_intersection"], 0)
            self.assertEqual(
                repeated["exhaustive_union_full_discriminant_equals_zero"],
                equal_mass + opposite_mass - intersection_mass,
            )

    def test_frozen_moments_match_exact_all_q_theorem(self) -> None:
        for q, row in self.frozen.items():
            expected = subject.rankin_moment_formulas(q)
            stored = {
                name: Fraction(*value)
                for name, value in row["selected_exact_moments"].items()
            }
            self.assertEqual(stored, expected)
            for atom in row["complete_normalized_coefficient_law"]["atoms"]:
                x = Fraction(*atom["x"])
                y = Fraction(*atom["y"])
                D = Fraction(*atom["coefficient_map_fold_D"])
                E = Fraction(*atom["hasse_endpoint_factor_E"])
                full = Fraction(*atom["full_quartic_root_discriminant"])
                self.assertEqual(D, (y + 2) ** 2 - 4 * x * x)
                self.assertEqual(E, x * x - 4 * (y - 2))
                self.assertEqual(full, D * E**2)
                self.assertEqual(
                    full,
                    subject.reciprocal_quartic_discriminant_via_resultant(x, y),
                )
                self.assertGreaterEqual(D, 0)

    def test_payload_file_locks_resource_caps_and_no_floats(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        payload_hash = unhashed.pop("payload_sha256")
        self.assertEqual(payload_hash, subject._canonical_sha256(unhashed))

        locks = stored["producer_and_source_locks"]["locks"]
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(
                b"\r", b"\n"
            )
            self.assertEqual(
                lock["sha256_lf_normalized"],
                hashlib.sha256(normalized).hexdigest(),
            )
        self.assertEqual(
            locks["genus1_fixture"]["payload_sha256"],
            subject.EXPECTED_SOURCE_PAYLOAD_SHA256,
        )

        resources = stored["resource_contract"]
        self.assertEqual(resources["actual_total_source_histogram_atom_pairs"], 645)
        self.assertLessEqual(
            resources["actual_total_source_histogram_atom_pairs"],
            resources["atom_pair_cap_inclusive"],
        )
        self.assertLess(
            resources["accounted_work_unit_ledger"]["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertEqual(resources["field_curve_or_model_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(stored)

    def test_literature_novelty_and_scope_firewalls(self) -> None:
        literature = self.fixture["literature_boundary"]
        self.assertIn("math/0007203", literature["classical_primary_context"])
        self.assertIn("do not invoke", literature["dependency_status"])
        self.assertEqual(
            literature["novelty_status"].split(";")[0],
            "NO_LITERATURE_PRIORITY_CLAIM",
        )
        self.assertTrue(
            any(
                "GL(2) x GL(2) tensor-product local factor" in item
                for item in literature["not_claimed_novel"]
            )
        )
        firewall = self.fixture["scope_firewall"]
        self.assertIn("do not identify", firewall["no_local_to_global_curve_relation"])
        self.assertIn("not reproved", firewall["no_automorphy_claim"])
        self.assertIn("not relabeled", firewall["no_measure_substitution"])
        self.assertIn(
            "not the full",
            firewall["no_fold_to_full_discriminant_conflation"],
        )
        self.assertIn("RH", firewall["no_RH_or_GRH_claim"])

    def test_note_math_controls_and_delimiters_are_well_formed(self) -> None:
        note_path = FUNCTION_FIELD / "ELLIPTIC_PAIR_RANKIN_SO4_FAMILY.md"
        text = note_path.read_text(encoding="utf-8")
        lines = text.splitlines()
        known_control_words = {
            "alpha",
            "begin",
            "beta",
            "bigl",
            "bigr",
            "boxed",
            "delta",
            "end",
            "gamma",
            "ge",
            "le",
            "lambda",
            "mathbb",
            "operatorname",
            "otimes",
            "over",
            "qquad",
            "quad",
            "simeq",
            "sqrt",
            "tag",
            "times",
        }
        bare_control_pattern = re.compile(
            r"(?<!\\)\b(?:"
            + "|".join(sorted(known_control_words, key=len, reverse=True))
            + r")\b"
        )
        seen_controls: set[str] = set()
        in_display = False
        brace_balance = 0
        display_openers = display_closers = 0
        for line_number, line in enumerate(lines, start=1):
            if line.strip() == r"\[":
                self.assertFalse(in_display, f"nested display opener at {line_number}")
                in_display = True
                brace_balance = 0
                display_openers += 1
                continue
            if line.strip() == r"\]":
                self.assertTrue(in_display, f"orphan display closer at {line_number}")
                self.assertEqual(
                    brace_balance,
                    0,
                    f"unbalanced braces before display closer at {line_number}",
                )
                in_display = False
                display_closers += 1
                continue
            if not in_display:
                continue
            self.assertIsNone(
                bare_control_pattern.search(line),
                f"bare TeX control word in display math at line {line_number}",
            )
            seen_controls.update(re.findall(r"\\([A-Za-z]+)", line))
            brace_balance += line.count("{") - line.count("}")
            self.assertGreaterEqual(
                brace_balance,
                0,
                f"closing brace precedes its opener at line {line_number}",
            )
        self.assertFalse(in_display, "unclosed display-math block")
        self.assertEqual(display_openers, display_closers)
        self.assertEqual(display_openers, 32)
        self.assertEqual(
            seen_controls - known_control_words,
            set(),
            "unexpected or malformed TeX control sequence",
        )
        self.assertEqual(text.count(r"\begin{aligned}"), text.count(r"\end{aligned}"))
        self.assertEqual(text.count(chr(96) * 3) % 2, 0)
        self.assertIsNone(
            re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text),
            "forbidden ASCII control character in note",
        )

    def test_strict_refusals_survive_optimized_python(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture((3, 5, 7))
        for invalid_q in (2, 4, 8, 15, 21, 45):
            with self.subTest(q=invalid_q):
                with self.assertRaisesRegex(ValueError, "odd prime power"):
                    subject.tensor_coefficients_closed(1, 2, invalid_q)
        for malformed_q in (True, False, Fraction(9), "9", 9.0, None):
            with self.subTest(q=malformed_q):
                with self.assertRaises(TypeError):
                    subject.tensor_coefficients_closed(1, 2, malformed_q)
        for malformed_coefficient in (True, Fraction(1), "1", 1.0, None):
            with self.subTest(coefficient=malformed_coefficient):
                with self.assertRaises(TypeError):
                    subject.tensor_coefficients_closed(malformed_coefficient, 2, 5)
        for malformed_order in (True, Fraction(2), "2", 2.0):
            with self.subTest(order=malformed_order):
                with self.assertRaises(TypeError):
                    subject.so4_haar_trace_moment(malformed_order)
        with self.assertRaisesRegex(ValueError, "restricted"):
            subject.so4_haar_trace_moment(13)
        with self.assertRaisesRegex(ValueError, "restricted"):
            subject.base_normalized_trace_moment(5, 5)
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.wall_factorization(1, 5, "same")
        for malformed_coordinate in (True, "1", 1.0, None):
            with self.subTest(coordinate=malformed_coordinate):
                with self.assertRaises(TypeError):
                    subject.reciprocal_quartic_discriminant_via_resultant(
                        malformed_coordinate, 1
                    )
        with self.assertRaisesRegex(RuntimeError, "cap exceeded"):
            subject.ResourceGuard().charge_pairs(subject.ATOM_PAIR_CAP_INCLUSIVE + 1)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.ResourceGuard().charge(
                "deliberate_refusal", subject.ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE
            )


if __name__ == "__main__":
    unittest.main()
