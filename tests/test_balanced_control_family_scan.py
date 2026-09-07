"""Focused replay tests for the bounded balanced-control family scan."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import balanced_control_family_scan as subject  # noqa: E402
import genus2_q_scan as q_scan  # noqa: E402


class BalancedControlFamilyScanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()
        cls.by_q = {
            row["q"]: row
            for row in cls.fixture["frozen_enumeration_facts"]["families"]
        }

    def test_exact_joint_support_and_sign_laws(self) -> None:
        expected = {
            3: (162, 32, 14, (48, 12, 102), [-19, 9], [29, 9]),
            5: (2500, 81, 33, (986, 50, 1464), [-4, 1], [96, 25]),
            7: (14406, 138, 55, (6258, 336, 7812), [-4, 1], [181, 49]),
        }
        for q, control in expected.items():
            family = self.by_q[q]
            members, joint_size, support_size, signs, lower, upper = control
            self.assertEqual(family["candidate_count"], q**5)
            self.assertEqual(family["member_count"], members)
            joint = family["joint_a_D_b_D_law"]
            support = family["balanced_support"]
            self.assertEqual(joint["support_size"], joint_size)
            self.assertEqual(len(joint["atoms"]), joint_size)
            self.assertEqual(sum(atom["member_count"] for atom in joint["atoms"]), members)
            self.assertEqual(support["support_size"], support_size)
            self.assertEqual(len(support["atoms"]), support_size)
            self.assertEqual(support["minimum"], lower)
            self.assertEqual(support["maximum"], upper)
            self.assertTrue(support["contained_in_exact_haar_support_minus4_to4"])
            comparison = family["sign_law"]["comparisons"]
            self.assertEqual(
                tuple(comparison[sign]["member_count"] for sign in ("negative", "zero", "positive")),
                signs,
            )
            histogram = {int(key): value for key, value in support["J_histogram"].items()}
            self.assertEqual(sum(histogram.values()), members)
            self.assertEqual(set(histogram), {atom["B_numerator_J"] for atom in support["atoms"]})

    def test_joint_histograms_reconstruct_B_and_have_a_sign_symmetry(self) -> None:
        for q, family in self.by_q.items():
            atoms = family["joint_a_D_b_D_law"]["atoms"]
            joint = {(atom["a_D"], atom["b_D"]): atom["member_count"] for atom in atoms}
            reconstructed: Counter[int] = Counter()
            for atom in atoms:
                a = atom["a_D"]
                b = atom["b_D"]
                j = 2 * q * a * a - b * b
                self.assertEqual(atom["B_numerator_J"], j)
                self.assertEqual(Fraction(*atom["B_D"]), Fraction(j, q**2))
                self.assertEqual(joint[a, b], joint.get((-a, b), 0))
                reconstructed[j] += atom["member_count"]
            self.assertEqual(
                dict(sorted(reconstructed.items())),
                {
                    int(key): value
                    for key, value in family["balanced_support"]["J_histogram"].items()
                },
            )

    def test_six_exact_moments_and_haar_comparator(self) -> None:
        expected = {
            3: [
                [88, 243],
                [3560, 2187],
                [42136, 19683],
                [1531592, 177147],
                [28210648, 1594323],
                [889288040, 14348907],
            ],
            5: [
                [646, 3125],
                [141284, 78125],
                [2362156, 1953125],
                [514468844, 48828125],
                [14061597676, 1220703125],
                [2745781777004, 30517578125],
            ],
            7: [
                [2444, 16807],
                [1536800, 823543],
                [34798640, 40353607],
                [21877044944, 1977326743],
                [648054364784, 96889010407],
                [442530198951440, 4747561509943],
            ],
        }
        self.assertEqual(
            self.fixture["proved_all_q_and_haar_facts"]["usp4_haar_law"][
                "moments_1_through_6"
            ],
            [0, 2, 0, 12, 0, 100],
        )
        for q, means in expected.items():
            records = self.by_q[q]["moments_1_through_6"]
            self.assertEqual([record["family_mean_B_D_to_order"] for record in records], means)
            for order, record in enumerate(records, start=1):
                self.assertEqual(record["order"], order)
                self.assertEqual(record["haar_moment"], subject.balanced_haar_moment(order))
                mean = Fraction(*record["family_mean_B_D_to_order"])
                self.assertEqual(
                    Fraction(*record["family_minus_haar"]),
                    mean - subject.balanced_haar_moment(order),
                )
            self.assertEqual(Fraction(*means[0]), subject.balanced_mean_all_q(q))
        for r in range(21):
            self.assertEqual(
                subject.balanced_haar_moment(2 * r),
                math.comb(2 * r, r) ** 2 // (r + 1),
            )
            if r:
                self.assertEqual(subject.balanced_haar_moment(2 * r - 1), 0)

    def test_required_raw_sums_are_hard_frozen(self) -> None:
        expected = {
            3: {"b_cubed": 8256, "a_squared_b_squared": 8352, "b_fourth": 45552},
            5: {
                "b_cubed": 788080,
                "a_squared_b_squared": 857040,
                "b_fourth": 8278480,
            },
            7: {
                "b_cubed": 14205744,
                "a_squared_b_squared": 16117248,
                "b_fourth": 221057088,
            },
        }
        for q, sums in expected.items():
            records = self.by_q[q]["source_locked_raw_aggregate_controls"]
            self.assertEqual({name: row["sum"] for name, row in records.items()}, sums)
            for name, value in sums.items():
                self.assertEqual(
                    Fraction(*records[name]["mean"]),
                    Fraction(value, self.by_q[q]["member_count"]),
                )

    def test_independent_raw_sum_replay_from_complete_candidate_generation(self) -> None:
        # Deliberately do not call subject.analyze_q or read its stored histogram.
        for q in subject.FROZEN_Q_VALUES:
            tables = q_scan.build_field_tables(q)
            sums = {"b_cubed": 0, "a_squared_b_squared": 0, "b_fourth": 0}
            members = 0
            for coefficients in itertools.product(range(q), repeat=5):
                conductor = tuple(coefficients) + (1,)
                if not q_scan.is_squarefree_quintic(conductor, q):
                    continue
                a, b = q_scan.coefficients_from_character_sums(conductor, tables)
                sums["b_cubed"] += b**3
                sums["a_squared_b_squared"] += a**2 * b**2
                sums["b_fourth"] += b**4
                members += 1
            self.assertEqual(members, q**5 - q**4)
            stored = self.by_q[q]["source_locked_raw_aggregate_controls"]
            self.assertEqual(sums, {name: row["sum"] for name, row in stored.items()})

    def test_high_weight_triangular_channels_and_third_moment_reduction(self) -> None:
        expected_channels = {
            3: {"chi_(0,3)": [74, 3**6], "chi_(2,2)": [37, 3**6], "chi_(0,4)": [-19, 3**7]},
            5: {"chi_(0,3)": [614, 5**6], "chi_(2,2)": [213, 5**6], "chi_(0,4)": [-51, 5**7]},
            7: {"chi_(0,3)": [2386, 7**6], "chi_(2,2)": [621, 7**6], "chi_(0,4)": [-99, 7**7]},
        }
        expected_r6 = {
            3: [3364, 19683],
            5: [93156, 1953125],
            7: [1227172, 40353607],
        }
        for q in subject.FROZEN_Q_VALUES:
            self.assertEqual(self.by_q[q]["derived_high_weight_channel_means"], expected_channels[q])
            reduction = self.by_q[q]["third_moment_reduction_frozen_evaluation"]
            self.assertEqual(reduction["remaining_mean_R6"], expected_r6[q])
            self.assertTrue(reduction["identity_checked"])
        reduction = subject.build_third_moment_reduction()
        self.assertEqual(reduction["first_unresolved_family_odd_moment"], 3)
        self.assertEqual(reduction["haar_check"], {"third_moment": 0, "trivial_character_coefficient": 0})
        self.assertEqual(
            [(row["notation"], row["coefficient"]) for row in reduction["character_decomposition"]],
            [
                ("chi_(0,0)", 6),
                ("chi_(2,0)", 6),
                ("chi_(0,2)", -6),
                ("chi_(0,3)", -2),
                ("chi_(2,3)", 2),
                ("chi_(6,0)", 3),
                ("chi_(4,2)", -3),
                ("chi_(2,4)", 1),
                ("chi_(0,6)", -1),
            ][1:],
        )

    def test_affine_orbit_and_endpoint_records(self) -> None:
        expected = {
            3: (29, {"3": 4, "6": 25}, [-19], [6], [29], [6]),
            5: (132, {"1": 1, "4": 1, "5": 3, "10": 6, "20": 121}, [-100], [5, 1], [96], [10, 10]),
            7: (349, {"21": 12, "42": 337}, [-196], [21, 21], [181], [42]),
        }
        for q, control in expected.items():
            orbit_count, histogram, lower_js, lower_sizes, upper_js, upper_sizes = control
            family = self.by_q[q]
            affine = family["affine_orbit_analysis"]
            self.assertEqual(affine["orbit_count"], orbit_count)
            self.assertEqual(affine["orbit_size_histogram"], histogram)
            tail = family["tail_concentration"]
            self.assertEqual([tail["lower_endpoint"]["B_numerator_J"]], lower_js)
            self.assertEqual(
                [record["orbit_size"] for record in tail["lower_endpoint"]["affine_orbits"]],
                lower_sizes,
            )
            self.assertEqual([tail["upper_endpoint"]["B_numerator_J"]], upper_js)
            self.assertEqual(
                [record["orbit_size"] for record in tail["upper_endpoint"]["affine_orbits"]],
                upper_sizes,
            )
            for share in tail["absolute_extreme_share_of_absolute_moments"].values():
                value = Fraction(*share)
                self.assertGreater(value, 0)
                self.assertLess(value, 1)

    def test_fixture_replay_hashes_and_firewalls(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        payload = dict(stored)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(subject._canonical_sha256(payload), claimed)
        locks = stored["producer_and_source_locks"]["locks"]
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(hashlib.sha256(normalized).hexdigest(), lock["sha256_lf_normalized"])
        self.assertEqual(
            stored["conjectures_and_nonclaims"]["status"],
            "NO_NEW_ALL_Q_FORMULA_CLAIMED",
        )
        self.assertIn("Nothing here proves", stored["firewall"])

    def test_resource_contract_and_refusals(self) -> None:
        resources = self.fixture["resource_contract"]
        self.assertEqual(resources["frozen_q_values"], [3, 5, 7])
        self.assertEqual(resources["candidate_cap_per_field"], 20_000)
        self.assertEqual(resources["maximum_candidate_count_in_any_field"], 7**5)
        self.assertLess(resources["maximum_candidate_count_in_any_field"], 20_000)
        self.assertFalse(resources["random_sampling"])
        self.assertFalse(resources["floating_point_in_results"])
        with self.assertRaisesRegex(ValueError, "supports only"):
            subject.analyze_q(11)
        with self.assertRaisesRegex(ValueError, "above per-field cap"):
            subject.analyze_q(7, candidate_cap=10_000)
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture(q_values=(3, 5))


if __name__ == "__main__":
    unittest.main()
