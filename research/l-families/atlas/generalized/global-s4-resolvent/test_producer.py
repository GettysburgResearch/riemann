"""Independent permutation, primitive point, normalization and source controls."""

import copy
import importlib.util
import itertools
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("s4_source_tested", HERE / "producer.py")
S = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(S)


def compose(a, b):
    return tuple(a[b[i]] for i in range(4))


def actual_character(g):
    sign = (-1) ** sum(g[i] > g[j] for i in range(4) for j in range(i + 1, 4))
    fixed = sum(g[i] == i for i in range(4))
    partitions = (
        frozenset((frozenset((0, 1)), frozenset((2, 3)))),
        frozenset((frozenset((0, 2)), frozenset((1, 3)))),
        frozenset((frozenset((0, 3)), frozenset((1, 2)))),
    )
    fixed_partitions = sum(
        frozenset(frozenset(g[i] for i in pair) for pair in partition) == partition
        for partition in partitions
    )
    return 1, sign, fixed_partitions - 1, fixed - 1, sign * (fixed - 1)


def average_inertia(frobenius, inertia):
    left, right = (
        actual_character(frobenius),
        actual_character(compose(frobenius, inertia)),
    )
    if any((a + b) % 2 for a, b in zip(left, right)):
        raise ArithmeticError("nonintegral invariant trace")
    return tuple((a + b) // 2 for a, b in zip(left, right))


class CharacterControls(unittest.TestCase):
    def test_table_from_actual_root_and_pair_partition_actions(self):
        census = {}
        for g in itertools.permutations(range(4)):
            row = actual_character(g)
            census[row] = census.get(row, 0) + 1
        self.assertEqual(census, dict(zip(S.CHARACTERS.values(), S.CLASS_SIZES)))

    def test_character_orthogonality_and_geometric_multiplicities(self):
        rows = [actual_character(g) for g in itertools.permutations(range(4))]
        for i, j in itertools.product(range(5), repeat=2):
            self.assertEqual(sum(row[i] * row[j] for row in rows), 24 * (i == j))
        dims, trans, double = (
            S.CHARACTERS["identity"],
            S.CHARACTERS["transposition"],
            S.CHARACTERS["double_transposition"],
        )
        h1 = [
            (3 * d - 6 * t - v) // 2 for d, t, v in zip(dims[1:], trans[1:], double[1:])
        ]
        self.assertEqual(h1, [4, 2, 2, 8])
        self.assertEqual(sum(d * h for d, h in zip(dims[1:], h1)), 38)

    def test_finite_invariant_frobenius_is_not_its_dimension(self):
        identity, t, disjoint = (0, 1, 2, 3), (1, 0, 2, 3), (0, 1, 3, 2)
        self.assertEqual(average_inertia(identity, t), S.finite_class(3, 0, 1)[1])
        self.assertEqual(average_inertia(disjoint, t), S.finite_class(1, 0, -1)[1])
        self.assertEqual(average_inertia(disjoint, t)[4], -1)
        self.assertEqual(average_inertia(identity, t)[4], 1)

    def test_infinity_frobenius_normalizes_double_transposition(self):
        identity, t, double = (0, 1, 2, 3), (1, 0, 2, 3), (1, 0, 3, 2)
        self.assertEqual(compose(t, double), compose(double, t))
        self.assertEqual(average_inertia(identity, double), S.infinity_traces(1))
        self.assertEqual(average_inertia(t, double), S.infinity_traces(-1))

    def test_a3_coset_permutation_decomposition(self):
        group = tuple(itertools.permutations(range(4)))
        a3 = ((0, 1, 2, 3), (0, 2, 3, 1), (0, 3, 1, 2))
        cosets = {frozenset(compose(g, h) for h in a3) for g in group}
        self.assertEqual(len(cosets), 8)
        for g in group:
            fixed = sum(
                frozenset(compose(g, h) for h in coset) == coset for coset in cosets
            )
            c = actual_character(g)
            self.assertEqual(fixed, c[0] + c[1] + c[3] + c[4])


class PrimitiveControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = {p: S.count_source(S.make_field(p, 1), 1, 1) for p in (5, 7)}

    def test_direct_affine_equations_and_projective_completion(self):
        for p, row in self.rows.items():
            chi_minus_one = 1 if p % 4 == 1 else -1
            expected = {
                "E": 2,
                "D": 1 + chi_minus_one,
                "R": 1 + chi_minus_one,
                "C": 2 * (1 + chi_minus_one),
                "G": 1 + chi_minus_one,
                "H": 1 + chi_minus_one,
            }
            for x, y in itertools.product(range(p), repeat=2):
                f, g = x**4 + x + 1, -16 * x**6 - 40 * x**3 - 27
                expected["E"] += (y * y - f) % p == 0
                expected["G"] += (y * y - g) % p == 0
                expected["H"] += (y * y - f * g) % p == 0
                expected["D"] += (y * y - (256 * (1 - x * x) ** 3 - 27)) % p == 0
                expected["R"] += (y * y - (-(x**4) + 4 * x * x + x)) % p == 0
                for v in range(p):
                    expected["C"] += (y * y - f) % p == 0 and (v * v - g) % p == 0
            self.assertEqual(row["curve_points"], expected)

    def test_resolvent_zero_is_affine_but_over_base_infinity(self):
        for row in self.rows.values():
            self.assertEqual(
                row["resolvent_affine_map_checks"],
                row["curve_points"]["R"] - row["projective_infinity_points"]["R"] - 1,
            )
        self.assertEqual(self.rows[7]["projective_infinity_points"]["R"], 0)
        self.assertEqual(self.rows[7]["infinity_stalk_traces"]["two"] + 1, 1)

    def test_branch_nonsplit_and_split_in_actual_extension_fields(self):
        split = S.count_source(S.make_field(5, 2), 1, 1)
        nonsplit = S.count_source(S.make_field(7, 1), 3, 4)
        self.assertGreater(split["finite_class_census"].get("branch_split", 0), 0)
        self.assertGreater(nonsplit["finite_class_census"].get("branch_nonsplit", 0), 0)
        self.assertEqual(split["finite_branch_character_minus_two"], 1)
        self.assertEqual(nonsplit["finite_branch_character_minus_two"], -1)

    def test_quartic_and_remaining_cubic_discriminant_identity(self):
        for p in (5, 7):
            for x in range(p):
                # Cubic discriminant for X^3+aX^2+bX+c, independently expanded.
                a, b, c = x, x * x, x**3 + 1
                discriminant = (
                    a * a * b * b
                    - 4 * b**3
                    - 4 * a**3 * c
                    - 27 * c * c
                    + 18 * a * b * c
                )
                self.assertEqual(discriminant % p, (-16 * x**6 - 40 * x**3 - 27) % p)
                fx = x**4 + x + 1
                self.assertEqual(
                    (256 * (1 - fx) ** 3 - 27) % p,
                    ((4 * x**3 + 1) ** 2 * discriminant) % p,
                )

    def test_singular_and_smooth_cyclic_strata_are_separately_rejected(self):
        field = S.make_field(5, 1)
        with self.assertRaisesRegex(ValueError, "cyclic"):
            S.count_source(field, 0, 1)
        with self.assertRaisesRegex(ValueError, "singular"):
            S.count_source(field, 1, 3)


class ContractControls(unittest.TestCase):
    def test_source_identity_rejects_boolean_float_and_resource_forgery(self):
        source = json.loads((HERE / "source.json").read_text())
        self.assertEqual(S.P.digest(source), S.EXPECTED_SOURCE_HASH)
        for key, value in (
            ("maximum_field_order", 10**9),
            ("maximum_field_order", 15625.0),
        ):
            changed = copy.deepcopy(source)
            changed[key] = value
            with self.assertRaises(ValueError):
                S.build(changed)
        for value in (True, 1.0):
            changed = copy.deepcopy(source)
            changed["curves"][0]["b"] = value
            with self.assertRaises(ValueError):
                S.build(changed)

    def test_allocation_guards_precede_field_construction(self):
        for args in ((5, 7), (7, 5), (6, 1), (True, 2), (5, 1.0)):
            with self.assertRaises((TypeError, ValueError)):
                S.make_field(*args)
        field = S.make_field(5, 1)
        for value in (True, 1.0):
            with self.assertRaises(TypeError):
                S.count_source(field, value, 1)

    def test_impossible_fibre_types_and_coercible_characters_rejected(self):
        for args in (
            (4, -1, 1),
            (2, 1, 1),
            (2, 0, 1),
            (3, 0, -1),
            (True, 1, 1),
            (0, 1, True),
        ):
            with self.assertRaises((TypeError, ValueError, ArithmeticError)):
                S.finite_class(*args)
        with self.assertRaises(ValueError):
            S.infinity_traces(True)

    def test_reciprocity_does_not_accept_missing_source_half(self):
        with self.assertRaises(ValueError):
            S.reciprocal_from_sums([1, 2, 3], 5, 4)
        self.assertEqual(S.reciprocal_from_sums([-1], 5, 1), [1, -1, 5])

    def test_frozen_artifact_factors_and_all_recorded_source_sums(self):
        data = json.loads((HERE / "artifact.json").read_text())
        for panel in data["panels"]:
            factors, rows = panel["polynomials"], panel["rows"]
            self.assertEqual(len(factors["tw"]), 9)
            self.assertEqual(len(factors["Z"]), 39)
            self.assertEqual(
                S.D.int_product(factors["G"], factors["H"]),
                S.D.int_product(factors["D"], factors["tw"]),
            )
            self.assertEqual(
                S.P.local_sums_from_polynomial(factors["tw"], len(rows)),
                [r["local_stalk_sums"]["tw"] for r in rows],
            )


if __name__ == "__main__":
    unittest.main()
