"""Independent class-count and literal-normalization checks for the complete fibre."""

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

PATH = (
    Path(__file__).resolve().parents[1]
    / "research"
    / "riemann-structures"
    / "complete_marked_owner_pushforward.py"
)
SPEC = importlib.util.spec_from_file_location("complete_marked_owner", PATH)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)
P = M.load_scout()


class CompleteMarkedOwnerTests(unittest.TestCase):
    def test_field_norm_character_independently_matches_extension_power(self):
        field = P.Field(5, 2)
        for x in range(1, 25):
            self.assertEqual(M.norm_character(field, x), field.quadratic(x))
            self.assertEqual(field.power(field.power(x, 5), 5), x)
        self.assertEqual(field.power(5, 2), 2)
        self.assertEqual(field.power(5, 5), 20)

    def test_complete_owner_and_two_independent_combinatorial_counts(self):
        field = P.Field(5, 2)
        native = P.fibre(field, 5, 6, 1, 2)
        bins, moments = M.independent_root_data(field, 5, 6)
        self.assertEqual(moments, (19, -1, 1, 1))
        self.assertEqual(native["complete_bilateral_count"], 23256)
        self.assertEqual(native["quadratic_class_counts"], M.category_count(bins))
        self.assertEqual(native["quadratic_class_counts"], M.class_formula(*moments))

    def test_complete_partial_defect_survives_class_sum_and_wick(self):
        before = M.class_formula(19, -1, 1, 1)
        after = M.class_formula(19, 1, 3, 1)
        self.assertEqual(list(before.values()), [6440, 5800, 5800, 5216])
        self.assertEqual(list(after.values()), [6296, 5672, 5944, 5344])
        self.assertEqual(sum(before.values()), sum(after.values()))
        self.assertEqual(
            M.principal_integer(after) - M.principal_integer(before), -336420864
        )

    def test_total_frobenius_preserves_exact_additive_readout(self):
        field = P.Field(5, 2)
        before = P.fibre(field, 5, 6, 1, 2)
        total = P.fibre(field, 20, 21, 1, 2)
        self.assertEqual(
            before["exact_additive_characters"], total["exact_additive_characters"]
        )
        self.assertEqual(
            before["integer_principal_literal_wick"],
            total["integer_principal_literal_wick"],
        )

    def test_same_single_coordinate_data_but_coupled_bit_changes(self):
        field = P.Field(5, 2)
        old = [M.norm_character(field, field.sub(5, mark)) for mark in range(4)]
        new = [M.norm_character(field, field.sub(20, mark)) for mark in range(4)]
        self.assertEqual(old, [-1, 1, -1, -1])
        self.assertEqual(old, new)
        self.assertEqual(M.norm_character(field, field.sub(6, 5)), 1)
        self.assertEqual(M.norm_character(field, field.sub(6, 20)), -1)

    def test_cofinal_nested_controls_are_symbolic_not_enumerations(self):
        for m in (1, 3, 9):
            record = M.cofinal_record(m)
            self.assertLess(record["integer_defect"], 0)
            self.assertEqual(record["enumerated_over_this_field"], m == 1)
            self.assertLess(
                Fraction(record["weighted_defect_without_common_observation_mass"]), 0
            )

    def test_six_by_six_literal_history_normalization(self):
        record = M.history_record()
        self.assertEqual(len(record["one_sided_histories"]), 6)
        self.assertEqual(record["bilateral_histories"], 36)
        self.assertEqual(record["equal_pair_share"], "1/15")
        counts = {str(key): 1 for key in M.CLASSES}
        self.assertEqual(M.principal_integer(counts), 4 * (1296 - 36))

    def test_marked_domain_and_power_caps_fail_closed(self):
        field = P.Field(5, 2)
        for exponent in (-1, True, 5001, 1.0):
            with self.subTest(exponent=exponent), self.assertRaises(ValueError):
                field.power(5, exponent)
        for args in ((5, 5, 1, 2), (5, 6, 0, 2), (True, 6, 1, 2), (25, 6, 1, 2)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                P.fibre(field, *args)
        with self.assertRaises(ValueError):
            P.fibre(field, 5, 6, 1, 2, extra_excluded=())

    def test_ordered_source_weight_clears_the_literal_wick_parent(self):
        record = M.history_record()
        self.assertEqual(record["ordered_owner_counting_weight"], "1/4")
        self.assertEqual(
            16 * Fraction(record["integral_parent_prefactor"]),
            Fraction(record["q25_principal_prefactor"]),
        )
        for count in M.class_formula(19, -1, 1, 1).values():
            ordered_class_trace = 16 * count
            self.assertEqual(
                81 * ordered_class_trace**2 - 36 * ordered_class_trace,
                16 * (1296 * count**2 - 36 * count),
            )

    def test_geometric_pair_quotient_would_add_nonsplit_owners(self):
        split, nonsplit = 0, 0
        for linear in range(5):
            for constant in range(5):
                discriminant = (linear**2 - 4 * constant) % 5
                if discriminant == 0:
                    continue
                roots = sum((x * x + linear * x + constant) % 5 == 0 for x in range(5))
                if roots == 2:
                    split += 1
                else:
                    self.assertEqual(roots, 0)
                    nonsplit += 1
        self.assertEqual((split, nonsplit), (10, 10))

    def test_formula_types_coverage_and_integrality_are_not_optional(self):
        for args in ((True, 0, 0, 0), (19, 20, 1, 1), (19, -1.0, 1, 1), (19, 0, 1, 1)):
            with self.subTest(args=args), self.assertRaises(ValueError):
                M.class_formula(*args)
        with self.assertRaises(ValueError):
            M.cofinal_record(2)
        with self.assertRaises(ValueError):
            M.principal_integer({"(-1, -1)": 1})

    def test_canonical_artifact_comparison_is_type_strict(self):
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": True}))
        self.assertNotEqual(M.canonical({"n": 1}), M.canonical({"n": 1.0}))
        with self.assertRaises(ValueError):
            M.canonical({"n": float("nan")})

    def test_source_lock_is_checked_against_fixed_primitive_ids(self):
        manifest = {
            "schema": "riemann.complete_marked_owner.sources.v1",
            "sources": [
                {"commit": commit, "path": path, "git_blob": blob}
                for (commit, path), blob in M.SOURCES.items()
            ],
        }
        manifest["sources"][0]["git_blob"] = "0" * 40
        with (
            patch.object(
                Path, "read_bytes", return_value=json.dumps(manifest).encode()
            ),
            self.assertRaisesRegex(ValueError, "manifest blob mismatch"),
        ):
            M.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
