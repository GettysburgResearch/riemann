"""Hostile and independent checks of the declared native source interfaces."""

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
    / "native_weighted_source_quotient.py"
)
SPEC = importlib.util.spec_from_file_location("native_weighted_quotient", PATH)
Q = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(Q)


class NativeWeightedQuotientTests(unittest.TestCase):
    def test_canonical_comparison_rejects_python_numeric_type_aliases(self):
        expected = {"count": 1}
        for candidate in ({"count": True}, {"count": 1.0}):
            self.assertEqual(candidate, expected)
            self.assertNotEqual(Q.canonical_json(candidate), Q.canonical_json(expected))
        with self.assertRaises(ValueError):
            Q.canonical_json({"count": float("nan")})

    def test_squarefree_word_diagonal_is_not_occupation_diagonal(self):
        record = Q.carrier_record(5)
        self.assertEqual(record["ordered_words"], 120)
        self.assertEqual(Fraction(record["word_counting_diagonal"]), Fraction(1, 120))
        self.assertEqual(Fraction(record["occupation_diagonal"]), 1)
        self.assertEqual(record["occupation_diagonal"], record["probability_diagonal"])

    def test_repeated_label_occupation_has_multinomial_not_factorial_tax(self):
        record = Q.occupation_record((2, 2))
        self.assertEqual(record["words"], 6)
        self.assertEqual(Fraction(record["coefficient"]), Fraction(1, 4))
        self.assertEqual(Fraction(record["counting_diagonal"]), Fraction(1, 96))

    def test_taylor_and_probability_resolutions_have_same_member(self):
        record = Q.carrier_record(3)
        count = record["ordered_words"]
        word = Fraction(record["coefficient_per_word"])
        member = Fraction(record["complete_coefficient"])
        self.assertEqual(count * word, member)
        self.assertEqual(
            sum((member / count for _ in range(count)), Fraction(0)), member
        )
        self.assertNotEqual(count * word * word, member * member)

    def test_one_direction_and_two_choices_are_source_ordered(self):
        self.assertEqual(Q.eligible((2, 3, 5, 7), (5, 7, 11, 13)), ((0, 5), (0, 7)))
        self.assertEqual(Q.eligible((5, 7, 11, 13), (2, 3, 5, 7)), ((1, 5), (1, 7)))

    def test_paths_keep_union_and_do_not_repeat(self):
        for a, b, path in Q.renewal_paths((2, 3, 5, 7), (5, 7, 11, 13)):
            self.assertEqual(set(a) | set(b), {2, 3, 5, 7, 11, 13})
            self.assertEqual(len(path), len({p for _, p in path}))
            self.assertLessEqual(len({side for side, _ in path}), 1)

    def test_complete_small_support_coverage(self):
        record = Q.renewal_coverage()
        self.assertEqual(record["assignment_coverage"], 729)
        self.assertGreater(record["hard_ancestors"], 0)
        self.assertGreater(record["literal_paths"], record["terminal_outputs"])

    def test_common_extraction_is_exact_but_recompletion_changes_ratio(self):
        record = Q.transport_record()
        self.assertEqual(record["original_products"], [1260, 175175])
        self.assertEqual(record["literal_extracted_products"], [180, 25025])
        self.assertEqual(record["recompleted_owners"], [[3, 5], [11, 13]])
        self.assertEqual(record["recompleted_products"], [60, 175175])
        self.assertEqual(record["ratio_defect"], "21")
        self.assertEqual(record["ancestral_transport_ratios"], ["210", "10"])

    def test_support_and_work_caps_fail_closed(self):
        for invalid in (True, 1, 8, 3.0):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                Q.carrier_record(invalid)
        for invalid in ((2, 2), (5, 3), (2, 4), (True, 3), tuple(range(2, 10))):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                Q.support(invalid)
        with self.assertRaises(ValueError):
            Q.occupation_record((4, 4))

    def test_forged_source_manifest_is_rejected_before_git_import(self):
        fake = {
            "schema": "riemann.native_weighted_quotient.sources.v1",
            "sources": [
                {"commit": commit, "path": path, "git_blob": blob}
                for (commit, path), blob in Q.SOURCE_BLOBS.items()
            ],
        }
        fake["sources"][0]["git_blob"] = "0" * 40
        with (
            patch.object(Path, "read_bytes", return_value=json.dumps(fake).encode()),
            self.assertRaisesRegex(ValueError, "manifest blob mismatch"),
        ):
            Q.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
