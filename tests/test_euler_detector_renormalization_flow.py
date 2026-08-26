from __future__ import annotations

import importlib
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_DIR = ROOT / "research" / "l-families" / "atlas" / "function_field"
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

flow = importlib.import_module("euler_detector_renormalization_flow")


class EulerDetectorRenormalizationFlowTests(unittest.TestCase):
    def test_su2_character_product_and_finite_span_obstruction(self) -> None:
        self.assertEqual(flow.su2_irrep_product(3, 2), (1, 3, 5))
        square = flow.multiply_character_polynomials({1: 1}, {1: 1})
        self.assertEqual(square, {0: 1, 2: 1})
        retained, discarded = flow.project_character_span(square, cutoff=1)
        self.assertEqual(retained, {0: 1})
        self.assertEqual(discarded, {2: 1})

        exact_fourth = flow.character_raw_moments({1: 1}, 4)[4]
        projected_fourth = flow.projected_power_haar_mean({1: 1}, 4, cutoff=1)
        self.assertEqual(exact_fourth, 2)
        self.assertEqual(projected_fourth, 1)

        for cutoff in range(1, 9):
            square_at_edge = flow.multiply_character_polynomials(
                {cutoff: 1}, {cutoff: 1}
            )
            _, edge_defect = flow.project_character_span(square_at_edge, cutoff)
            self.assertEqual(edge_defect[2 * cutoff], 1)

    def test_truncated_local_euler_log_character_and_exact_cumulants(self) -> None:
        raw = flow.truncated_euler_log_character(Fraction(1, 2), 2)
        centered = flow.center_character_polynomial(raw)
        self.assertEqual(
            raw, {0: Fraction(-1, 8), 1: Fraction(1, 2), 2: Fraction(1, 8)}
        )
        self.assertEqual(centered, {1: Fraction(1, 2), 2: Fraction(1, 8)})

        moments = flow.character_raw_moments(centered, 6)
        cumulants = flow.cumulants_from_raw_moments(moments)
        self.assertEqual(
            moments,
            (
                Fraction(1),
                Fraction(0),
                Fraction(17, 64),
                Fraction(49, 512),
                Fraction(707, 4096),
                Fraction(2243, 16384),
                Fraction(45695, 262144),
            ),
        )
        self.assertEqual(
            cumulants,
            (
                Fraction(0),
                Fraction(0),
                Fraction(17, 64),
                Fraction(49, 512),
                Fraction(-5, 128),
                Fraction(-961, 8192),
                Fraction(-5605, 131072),
            ),
        )

    def test_trace_channel_variance_hierarchy(self) -> None:
        self.assertEqual(flow.centered_trace_power_character(1), {1: 1})
        self.assertEqual(flow.centered_trace_power_character(2), {2: 1})
        self.assertEqual(flow.centered_trace_power_character(3), {1: -1, 3: 1})
        self.assertEqual(
            [flow.trace_power_variance(power) for power in range(1, 9)],
            [1, 1, 2, 2, 2, 2, 2, 2],
        )
        self.assertEqual(
            [flow.trace_channel_critical_sigma(power) for power in range(1, 5)],
            [Fraction(1, 2), Fraction(1, 4), Fraction(1, 6), Fraction(1, 8)],
        )

    def test_cumulant_jet_closes_exactly_under_independent_convolution(self) -> None:
        left = flow.DiscreteLaw.from_mapping({-1: Fraction(1, 2), 1: Fraction(1, 2)})
        right = flow.DiscreteLaw.from_mapping({0: Fraction(1, 3), 3: Fraction(2, 3)})
        convolved = left.convolve(right)
        left_jet = left.cumulants(6)
        right_jet = right.cumulants(6)
        aggregate_jet = convolved.cumulants(6)
        self.assertEqual(
            aggregate_jet,
            flow.add_cumulant_jets(left_jet, right_jet),
        )

    def test_four_copy_rg_has_only_contracting_centered_higher_directions(self) -> None:
        expected = {
            2: Fraction(1),
            3: Fraction(1, 2),
            4: Fraction(1, 4),
            5: Fraction(1, 8),
            6: Fraction(1, 16),
            7: Fraction(1, 32),
            8: Fraction(1, 64),
        }
        self.assertEqual(
            {order: flow.four_block_eigenvalue(order) for order in expected},
            expected,
        )
        coordinates = {3: Fraction(7, 3), 4: -2, 6: 5, 8: -56}
        mapped = flow.four_block_standardized_flow(coordinates)
        self.assertEqual(
            mapped,
            {
                3: Fraction(7, 6),
                4: Fraction(-1, 2),
                6: Fraction(5, 16),
                8: Fraction(-7, 8),
            },
        )
        self.assertTrue(
            all(abs(mapped[key]) < abs(value) for key, value in coordinates.items())
        )

    def test_weighted_su2_flow_and_maximum_leverage_bound(self) -> None:
        weights = tuple(Fraction(1, prime) for prime in (2, 3, 5, 7, 11, 13))
        total = sum(weights)
        coordinates = flow.weighted_su2_even_flow(weights)
        self.assertEqual(coordinates[4], -sum(value**2 for value in weights) / total**2)
        self.assertEqual(
            coordinates[6], 5 * sum(value**3 for value in weights) / total**3
        )
        self.assertEqual(
            coordinates[8], -56 * sum(value**4 for value in weights) / total**4
        )
        self.assertLessEqual(abs(coordinates[4]), flow.leverage_bound(weights, 2))
        self.assertLessEqual(abs(coordinates[6]) / 5, flow.leverage_bound(weights, 3))
        self.assertLessEqual(abs(coordinates[8]) / 56, flow.leverage_bound(weights, 4))

        equal_weights = (Fraction(1),) * 16
        equal_coordinates = flow.weighted_su2_even_flow(equal_weights)
        self.assertEqual(
            equal_coordinates,
            {4: Fraction(-1, 16), 6: Fraction(5, 256), 8: Fraction(-7, 512)},
        )

    def test_critical_and_summable_prefixes_separate_in_the_probe(self) -> None:
        primes = (2, 3, 5, 7, 11, 13, 17, 19)
        critical = flow.weighted_su2_even_flow(Fraction(1, prime) for prime in primes)
        summable = flow.weighted_su2_even_flow(
            Fraction(1, prime * prime) for prime in primes
        )
        self.assertLess(abs(critical[4]), abs(summable[4]))
        self.assertLess(abs(critical[6]), abs(summable[6]))
        self.assertLess(abs(critical[8]), abs(summable[8]))

    def test_four_jet_does_not_identify_sign_or_the_next_cumulant(self) -> None:
        even, odd = flow.finite_difference_twin(4)
        self.assertEqual(even.raw_moments(4), odd.raw_moments(4))
        self.assertEqual(even.cumulants(4), odd.cumulants(4))
        self.assertEqual(even.cumulants(5)[5], Fraction(-15, 4))
        self.assertEqual(odd.cumulants(5)[5], Fraction(15, 4))
        self.assertEqual(even.positive_probability_after_centering(), Fraction(5, 16))
        self.assertEqual(odd.positive_probability_after_centering(), Fraction(11, 16))

    def test_equal_local_marginals_do_not_identify_the_aggregate_flow(self) -> None:
        packet = flow.two_place_chi1_coupling_packet(8)
        self.assertEqual(packet["individual_marginal"], "Haar_SU2_chi_1_in_every_mode")
        modes = packet["modes"]
        independent = modes["independent"]
        diagonal = modes["diagonal"]
        antidiagonal = modes["central_antidiagonal"]

        self.assertEqual(independent["aggregate_cumulants"]["2"], [2, 1])
        self.assertEqual(independent["aggregate_cumulants"]["4"], [-2, 1])
        self.assertTrue(
            all(
                value == [0, 1]
                for value in independent["mixed_cumulant_defect"].values()
            )
        )

        self.assertEqual(diagonal["aggregate_cumulants"]["2"], [4, 1])
        self.assertEqual(diagonal["aggregate_cumulants"]["4"], [-16, 1])
        self.assertEqual(diagonal["mixed_cumulant_defect"]["2"], [2, 1])
        self.assertEqual(diagonal["mixed_cumulant_defect"]["4"], [-14, 1])

        self.assertTrue(
            all(
                value == [0, 1]
                for value in antidiagonal["aggregate_cumulants"].values()
            )
        )
        self.assertEqual(antidiagonal["mixed_cumulant_defect"]["2"], [-2, 1])
        self.assertEqual(antidiagonal["mixed_cumulant_defect"]["4"], [2, 1])

    def test_probe_is_exact_bounded_and_explicitly_non_arithmetic(self) -> None:
        probe = flow.build_probe()
        self.assertEqual(probe["status"], "EXACT_COMPACT_MODEL_AND_FORMAL_JET_PROBE")
        self.assertFalse(probe["scope"]["arithmetic_family"])
        self.assertFalse(probe["scope"]["global_euler_product"])
        self.assertFalse(probe["scope"]["rh_or_grh_consequence"])
        resource = probe["resource_contract"]
        self.assertTrue(resource["exact_rational_arithmetic"])
        self.assertFalse(resource["random_sampling"])
        self.assertFalse(resource["finite_field_or_curve_enumeration"])
        self.assertFalse(resource["zero_computation"])
        self.assertLessEqual(
            resource["actual_local_factors"], resource["maximum_local_factors"]
        )

    def test_fail_closed_resource_and_domain_guards(self) -> None:
        with self.assertRaises(ValueError):
            flow.truncated_euler_log_character(Fraction(1, 2), 0)
        with self.assertRaises(ValueError):
            flow.weighted_su2_even_flow([])
        with self.assertRaises(ValueError):
            flow.weighted_su2_even_flow([1, -1])
        with self.assertRaises(RuntimeError):
            flow.weighted_su2_even_flow([1] * (flow.MAX_LOCAL_FACTORS + 1))
        with self.assertRaises(RuntimeError):
            flow.su2_irrep_product(flow.MAX_CHARACTER_WEIGHT, 1)


if __name__ == "__main__":
    unittest.main()
