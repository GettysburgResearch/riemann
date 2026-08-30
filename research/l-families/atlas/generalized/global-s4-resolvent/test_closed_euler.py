"""Permutation-derived local determinants and independent Euler controls."""

import copy
import importlib.util
import itertools
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "s4_closed_tested", HERE / "closed_euler.py"
)
C = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(C)
ID = (0, 1, 2, 3)
T = (1, 0, 2, 3)
OTHER = (0, 1, 3, 2)
DOUBLE = (1, 0, 3, 2)


def compose(a, b):
    return tuple(a[b[i]] for i in range(4))


def characters(g):
    sign = (-1) ** sum(g[i] > g[j] for i in range(4) for j in range(i + 1, 4))
    fixed = sum(g[i] == i for i in range(4))
    partitions = {
        frozenset((frozenset(pair), frozenset(set(range(4)) - set(pair))))
        for pair in itertools.combinations(range(4), 2)
    }
    fixed_partitions = sum(
        frozenset(frozenset(g[i] for i in pair) for pair in v) == v for v in partitions
    )
    return (1, sign, fixed_partitions - 1, fixed - 1, sign * (fixed - 1))


def representation_denominators(frobenius, inertia=ID):
    dimensions = tuple(
        (x + y) // 2 for x, y in zip(characters(ID), characters(inertia))
    )
    traces = [[] for _ in dimensions]
    current = ID
    for _ in range(3):
        current = compose(current, frobenius)
        for values, a, b in zip(
            traces, characters(current), characters(compose(current, inertia))
        ):
            if (a + b) % 2:
                raise ArithmeticError("nonintegral actual projector trace")
            values.append(-(a + b) // 2)
    return {
        name: C.P.newton_from_local_sums(values[:dim])
        for name, dim, values in zip(C.NAMES, dimensions, traces)
    }


class RepresentationControls(unittest.TestCase):
    def test_every_unramified_class_from_actual_permutations(self):
        examples = {
            "identity": ID,
            "transposition": T,
            "double_transposition": DOUBLE,
            "three_cycle": (1, 2, 0, 3),
            "four_cycle": (1, 2, 3, 0),
        }
        for label, g in examples.items():
            self.assertEqual(
                C.finite_denominators(label), representation_denominators(g)
            )

    def test_branch_denominators_from_inertia_projector(self):
        self.assertEqual(
            C.finite_denominators("branch_split"), representation_denominators(ID, T)
        )
        self.assertEqual(
            C.finite_denominators("branch_nonsplit"),
            representation_denominators(OTHER, T),
        )

    def test_infinity_denominators_from_inertia_projector(self):
        self.assertEqual(
            C.infinity_denominators(5), representation_denominators(ID, DOUBLE)
        )
        self.assertEqual(
            C.infinity_denominators(7), representation_denominators(T, DOUBLE)
        )

    def test_four_cycle_twist_changes_more_than_trace_label(self):
        factors = C.finite_denominators("four_cycle")
        self.assertEqual(factors["std"], [1, 1, 1, 1])
        self.assertEqual(factors["tw"], [1, -1, 1, -1])
        self.assertEqual(factors["two"], [1, 0, -1])


class PrimitiveEulerControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.artifact = json.loads((HERE / "euler_artifact.json").read_text())

    def test_all_declared_degree_censuses_are_complete(self):
        for panel in self.artifact["panels"]:
            for row in panel["censuses"]:
                self.assertEqual(
                    row["place_count"],
                    C.E.closed_point_count(panel["p"], row["degree"]),
                )
                self.assertEqual(
                    row["place_count"],
                    sum(group["count"] for group in row["classes"].values()),
                )
                self.assertEqual(len(row["all_primitive_places_digest"]), 64)

    def test_new_degree_two_census_is_rebuilt_from_field_orbits(self):
        for panel in self.artifact["panels"]:
            expected = panel["censuses"][1]
            actual = C.census(C.P.Field(panel["p"], 2), panel["b"], panel["c"])
            self.assertEqual(actual, expected)

    def test_residue_field_character_changes_with_degree(self):
        panel = self.artifact["panels"][2]
        degree_one, degree_two = panel["censuses"][:2]
        self.assertEqual(degree_one["classes"]["branch_nonsplit"]["count"], 2)
        self.assertNotIn("branch_nonsplit", degree_two["classes"])
        # Any degree-two branch place has square -2 in its residue field.
        for row in panel["censuses"]:
            if row["degree"] % 2 == 0:
                self.assertNotIn("branch_nonsplit", row["classes"])

    def test_wrong_infinity_invariant_dimension_changes_actual_euler_product(self):
        panel = self.artifact["panels"][1]
        wrong = copy.deepcopy(panel["infinity_denominators"])
        wrong["two"] = [1, -2, 1]
        wrong["tw"] = [1, -1]
        changed = C.multiply_censuses(panel["censuses"], wrong)
        self.assertNotEqual(changed["two"], panel["euler_products_mod_T5"]["two"])
        self.assertNotEqual(changed["tw"], panel["euler_products_mod_T5"]["tw"])

    def test_wrong_finite_branch_dimension_changes_actual_euler_product(self):
        panel = self.artifact["panels"][2]
        rows = copy.deepcopy(panel["censuses"])
        for row in rows:
            if "branch_nonsplit" in row["classes"]:
                row["classes"]["branch_nonsplit"]["denominators"]["tw"] = [1, -1]
        changed = C.multiply_censuses(rows, panel["infinity_denominators"])
        self.assertNotEqual(changed["tw"], panel["euler_products_mod_T5"]["tw"])

    def test_trivial_euler_product_is_projective_line_zeta(self):
        for panel in self.artifact["panels"]:
            self.assertEqual(
                panel["euler_products_mod_T5"]["one"],
                [sum(panel["p"] ** j for j in range(n + 1)) for n in range(5)],
            )


class ContractControls(unittest.TestCase):
    def test_local_series_inverse_and_degree_substitution(self):
        self.assertEqual(C.reciprocal([1, 0, -1], 1), [1, 0, 1, 0, 1])
        self.assertEqual(C.reciprocal([1, -2, 1], 2), [1, 0, 2, 0, 3])
        self.assertEqual(C.reciprocal([1, 1], 3), [1, 0, 0, -1, 0])

    def test_invalid_degrees_and_coercible_factors_are_rejected(self):
        for degree in (0, 5, True, 2.0):
            with self.assertRaises((TypeError, ValueError)):
                C.reciprocal([1, -1], degree)
        for denominator in ([True, -1], [1, True], [1, -1.0], [1, 4], [1, 0, 0, 0, 1]):
            with self.assertRaises(ValueError):
                C.reciprocal(denominator, 1)
        for label in (True, "not-a-class"):
            with self.assertRaises((TypeError, ValueError)):
                C.finite_denominators(label)

    def test_missing_degree_and_forged_source_rejected(self):
        with self.assertRaises(ValueError):
            C.multiply_censuses([], C.infinity_denominators(5))
        source = json.loads((HERE / "euler_source.json").read_text())
        self.assertEqual(C.P.digest(source), C.SOURCE_HASH)
        for value in (True, 4.0, 10**9):
            changed = copy.deepcopy(source)
            changed["degree_cutoff"] = value
            with self.assertRaises(ValueError):
                C.build(changed)

    def test_authentication_failure_precedes_dependency_import(self):
        with (
            patch.object(
                C.subprocess,
                "run",
                return_value=SimpleNamespace(returncode=0, stdout=b"forged dependency"),
            ),
            patch.object(
                C.importlib.util,
                "spec_from_file_location",
                side_effect=AssertionError("must not import"),
            ),
            self.assertRaises(ValueError),
        ):
            C.load_sources()


if __name__ == "__main__":
    unittest.main()
