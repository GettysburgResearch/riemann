"""Actual quotient counts, diagonal inertia and non-invented factor controls."""

import copy
import importlib.util
import itertools
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "s4_quadratic_tested", HERE / "quadratic_twist_replay.py"
)
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
ID, T, DOUBLE = (0, 1, 2, 3), (1, 0, 2, 3), (1, 0, 3, 2)


def compose(a, b):
    return tuple(a[b[i]] for i in range(4))


def character(g):
    sign = (-1) ** sum(g[i] > g[j] for i in range(4) for j in range(i + 1, 4))
    fixed = sum(g[i] == i for i in range(4))
    partitions = {
        frozenset((frozenset(pair), frozenset(set(range(4)) - set(pair))))
        for pair in itertools.combinations(range(4), 2)
    }
    fixed_pairs = sum(
        frozenset(frozenset(g[i] for i in pair) for pair in part) == part
        for part in partitions
    )
    return (1, sign, fixed_pairs - 1, fixed - 1, sign * (fixed - 1))


def twisted_projector_traces(g):
    return tuple(
        (a - b) // 2 for a, b in zip(character(g), character(compose(g, DOUBLE)))
    )


class InertiaControls(unittest.TestCase):
    def test_diagonal_inertia_has_anti_invariants_not_zero_stalk(self):
        self.assertEqual(twisted_projector_traces(ID), (0, 0, 0, 2, 2))
        self.assertEqual(twisted_projector_traces(T), (0, 0, 0, 0, 0))
        self.assertEqual(twisted_projector_traces(compose(T, T)), (0, 0, 0, 2, 2))

    def test_zero_first_trace_still_gives_nontrivial_local_denominator(self):
        first, second = (
            twisted_projector_traces(T),
            twisted_projector_traces(compose(T, T)),
        )
        for i in (3, 4):
            self.assertEqual(
                R.P.newton_from_local_sums([-first[i], -second[i]]), [1, 0, -1]
            )
        self.assertEqual(R.P.newton_from_local_sums([-2, -2]), [1, -2, 1])

    def test_all_constituent_cohomology_ranks_and_regular_anti_genus(self):
        dims, trans, double = character(ID), character(T), character(DOUBLE)
        ranks = tuple((5 * d - 6 * t + v) // 2 for d, t, v in zip(dims, trans, double))
        self.assertEqual(ranks, (0, 6, 6, 4, 10))
        self.assertEqual(sum(d * h for d, h in zip(dims, ranks)), 60)
        self.assertEqual(2 * 49 - 2 * 19, 60)


class PrimitiveControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = {
            (p, b, c): R.count_source(R.S.make_field(p, 1), b, c)
            for p, b, c in ((5, 1, 1), (7, 1, 1), (7, 3, 4))
        }

    def test_direct_prime_field_equations_all_four_curves(self):
        for (p, b, c), row in self.rows.items():
            delta = 1 if p % 4 == 1 else -1
            counts = {
                "Dchi": 1,
                "X": 3 + delta,
                "Rchi": 2 + delta,
                "Cchi": 4 * (1 + delta),
            }
            for x, w in itertools.product(range(p), repeat=2):
                f, g = x**4 + b * x + c, -16 * x**6 - 40 * b * x**3 - 27 * b * b
                counts["X"] += (w**4 - f) % p == 0
                counts["Dchi"] += (
                    w * w - x * (256 * (c - x * x) ** 3 - 27 * b**4)
                ) % p == 0
                counts["Rchi"] += (4 * x * w**4 + x**3 - 4 * c * x - b * b) % p == 0
                for v in range(p):
                    counts["Cchi"] += (w**4 - f) % p == 0 and (v * v - g) % p == 0
            self.assertEqual(counts, row["counts"])

    def test_degree_one_branch_values_have_opposite_twists(self):
        branches = self.rows[7, 3, 4]["rational_branch_twists"]
        self.assertEqual(
            branches,
            [
                {"u": 1, "chi_u": 1, "old_class": "branch_nonsplit"},
                {"u": 6, "chi_u": -1, "old_class": "branch_nonsplit"},
            ],
        )

    def test_infinity_changes_over_quadratic_extension_without_losing_dimension(self):
        first = self.rows[7, 1, 1]
        second = R.count_source(R.S.make_field(7, 2), 1, 1)
        self.assertEqual(first["twisted_infinity_stalk_traces"]["std"], 0)
        self.assertEqual(second["twisted_infinity_stalk_traces"]["std"], 2)
        for row in (first, second):
            self.assertEqual(row["twisted_infinity_stalk_dimensions"]["std"], 2)
        self.assertEqual(first["projective_exceptional_points"]["Rchi"], 1)
        self.assertEqual(second["projective_exceptional_points"]["Rchi"], 3)

    def test_batch_inverses_satisfy_field_identity(self):
        for p in (5, 7):
            field = R.S.make_field(p, 2)
            inverse = R.inverse_table(field)
            self.assertEqual(inverse[0], 0)
            for x in range(1, field.q):
                self.assertEqual(field.mul(x, inverse[x]), 1)
            for x in (1, 2, field.q - 1):
                self.assertEqual(inverse[x], field.power(x, field.q - 2))

    def test_trivial_twist_has_zero_complete_cohomological_trace(self):
        for row in self.rows.values():
            self.assertEqual(row["twisted_stalk_sums"]["one"], 0)

    def test_joint_normalized_fibres_obey_double_cover_bound(self):
        for row in self.rows.values():
            old = row["Z_points_from_normalized_regular_character"]
            new = row["Ztilde_points_from_normalized_joint_regular_character"]
            self.assertGreaterEqual(new, 0)
            self.assertLessEqual(new, 2 * old)
            self.assertEqual(new - old, row["signed_regular_source_sum"])
            self.assertEqual(
                new - old,
                sum(
                    d * row["twisted_stalk_sums"][name]
                    for d, name in zip(R.DIMS, R.NAMES)
                ),
            )


class ArtifactControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((HERE / "quadratic_twist_artifact.json").read_text())

    def test_full_degree_ten_only_where_five_independent_traces_exist(self):
        for panel in self.data["panels"]:
            factor = panel["twisted_polynomials"]["tw"]
            self.assertEqual(panel["full_degree_ten_available"], panel["p"] == 5)
            if panel["p"] == 5:
                self.assertEqual(len(factor), 11)
                self.assertEqual(panel["degree_ten_held_out_extensions"], [6])
                self.assertEqual(factor[:5], panel["tw_prefix_mod_T5"])
            else:
                self.assertIsNone(factor)
                self.assertIsNone(panel["curve_polynomials"]["Cchi"])
                self.assertIsNone(panel["curve_polynomials"]["Ztilde"])
                self.assertEqual(len(panel["tw_prefix_mod_T5"]), 5)

    def test_p5_sixth_extension_is_predicted_from_first_five(self):
        panel = self.data["panels"][0]
        sums = [row["twisted_stalk_sums"]["tw"] for row in panel["rows"]]
        reconstructed = R.S.reciprocal_from_sums(sums[:5], 5, 5)
        self.assertEqual(R.P.local_sums_from_polynomial(reconstructed, 6)[5], sums[5])

    def test_large_curve_dimensions_follow_proved_decompositions(self):
        panel = self.data["panels"][0]
        self.assertEqual(len(panel["curve_polynomials"]["Cchi"]), 35)
        self.assertEqual(len(panel["curve_polynomials"]["Ztilde"]), 99)
        for name, degree in (("sign", 6), ("two", 6), ("std", 4)):
            for source in self.data["panels"]:
                self.assertEqual(len(source["twisted_polynomials"][name]), degree + 1)

    def test_source_forgery_cannot_increase_allocation_or_promote_prefix(self):
        source = json.loads((HERE / "quadratic_twist_source.json").read_text())
        self.assertEqual(R.P.digest(source), R.SOURCE_HASH)
        for value in (True, 15625.0, 10**9):
            altered = copy.deepcopy(source)
            altered["maximum_field_order"] = value
            with self.assertRaises(ValueError):
                R.build(altered)
        altered = copy.deepcopy(source)
        altered["curves"][1]["extensions"].append(5)
        with self.assertRaises(ValueError):
            R.build(altered)

    def test_invalid_source_strata_rejected(self):
        field = R.S.make_field(5, 1)
        for b, c in ((0, 1), (1, 3), (True, 1), (1, 1.0)):
            with self.assertRaises((TypeError, ValueError)):
                R.count_source(field, b, c)


if __name__ == "__main__":
    unittest.main()
