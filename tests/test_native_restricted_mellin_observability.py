"""Independent normalization, separation, degeneracy and authentication controls."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from fractions import Fraction
from math import isqrt
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "restricted_mellin",
    ROOT
    / "research"
    / "riemann-structures"
    / "native_restricted_mellin_observability.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RestrictedMellinTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.predecessor = MODULE.load_predecessor()

    def test_native_normalization_from_physical_integers(self):
        record = MODULE.panel_record(self.predecessor, self.predecessor.PANELS[0])
        self.assertEqual(record["one_sided_boolean_history_sum"], 2)
        self.assertEqual(record["one_sided_equal_pair_share"], "1/15")
        for entry in record["entries"]:
            square = Fraction(entry["native_coefficient_square"])
            self.assertEqual(square, Fraction(16, 225**2 * entry["N"] * entry["M"]))
            dual_square = Fraction(entry["source_dual_coefficient_square"])
            self.assertEqual(dual_square / square, (35 * record["common_core"]) ** 2)
        expected_diagonal = (
            sum(
                (
                    Fraction(e["source_dual_coefficient_square"])
                    for e in record["entries"]
                ),
                Fraction(0),
            )
            / 4
        )
        self.assertEqual(
            Fraction(record["source_dual_literal_diagonal"]), expected_diagonal
        )

    def test_held_out_same_cell_retains_twelve_different_modes(self):
        for spec, count in zip(self.predecessor.PANELS, (9, 12), strict=True):
            record = MODULE.panel_record(self.predecessor, spec)
            certificate = record["mode_certificate"]
            self.assertEqual(certificate["exact_mode_count"], count)
            self.assertEqual(record["literal_history_count"], 4 * count)
            self.assertEqual({tuple(e["cell"]) for e in record["entries"]}, {(1, 4)})
            self.assertFalse(record["complete_weighted_source_assembly_replayed"])
            self.assertFalse(certificate["logarithms_or_square_roots_evaluated"])

    def test_irrational_native_amplitudes_are_not_rational_surrogates(self):
        record = MODULE.panel_record(self.predecessor, self.predecessor.PANELS[1])
        for entry in record["entries"]:
            square = Fraction(entry["native_coefficient_square"])
            self.assertFalse(
                isqrt(square.numerator) ** 2 == square.numerator
                and isqrt(square.denominator) ** 2 == square.denominator
            )
            self.assertTrue(entry["positive_coefficient_branch_from_histories"])

    def test_orientation_and_its_conjugate_have_same_mode_count(self):
        record = MODULE.panel_record(self.predecessor, self.predecessor.PANELS[0])
        ratios = tuple(Fraction(e["N"], e["M"]) for e in record["entries"])
        self.assertEqual(
            ratios, tuple(Fraction(e["ratio_N_over_M"]) for e in record["entries"])
        )
        squares = tuple(
            Fraction(e["native_coefficient_square"]) for e in record["entries"]
        )
        conjugate = MODULE.mode_certificate(tuple(1 / r for r in ratios), squares)
        self.assertEqual(conjugate["exact_mode_count"], 9)

    def test_independent_three_node_vandermonde_expansion(self):
        a, b, c = Fraction(2, 3), Fraction(4, 5), Fraction(7, 6)
        # Direct determinant of rows [1,1,1], [a,b,c], [a^2,b^2,c^2].
        determinant = b * c**2 - c * b**2 - a * c**2 + c * a**2 + a * b**2 - b * a**2
        certificate = MODULE.mode_certificate((c, a, b), (Fraction(1),) * 3)
        self.assertEqual(
            Fraction(certificate["rational_vandermonde_surrogate"]), determinant
        )
        self.assertFalse(certificate["surrogate_is_native_derivative_hankel"])

    def test_repeated_frequency_can_cancel_or_aggregate(self):
        r, s = Fraction(7, 5), Fraction(11, 8)
        collapsed = MODULE.collapse_rational_control(
            ((r, Fraction(2)), (r, Fraction(-2)), (s, Fraction(3)))
        )
        self.assertEqual(collapsed, {s: Fraction(3)})
        self.assertEqual(
            MODULE.collapse_rational_control(((r, Fraction(1)), (r, Fraction(1)))),
            {r: Fraction(2)},
        )

    def test_zero_coefficient_or_duplicate_ratio_is_not_a_full_mode_certificate(self):
        with self.assertRaisesRegex(ValueError, "nonzero positive"):
            MODULE.mode_certificate((Fraction(1),), (Fraction(0),))
        with self.assertRaisesRegex(ValueError, "duplicate ratio"):
            MODULE.mode_certificate(
                (Fraction(1), Fraction(1)), (Fraction(1), Fraction(4))
            )
        one = MODULE.mode_certificate((Fraction(1),), (Fraction(4, 9),))
        self.assertEqual(one["exact_mode_count"], 1)
        self.assertEqual(one["rational_vandermonde_surrogate"], "1")

    def test_positive_mass_bounds_and_literal_wick_diagonal(self):
        for spec in self.predecessor.PANELS:
            record = MODULE.panel_record(self.predecessor, spec)
            upper = Fraction(record["source_dual_sum_strict_upper"])
            diagonal = Fraction(record["source_dual_literal_diagonal"])
            self.assertLess(diagonal, upper**2 / 4)
            self.assertEqual(
                Fraction(record["wick_absolute_pointwise_upper"]),
                Fraction(24, 35) * upper**2,
            )
            self.assertLess(
                Fraction(record["sum_coefficients_strict_lower"]),
                Fraction(record["sum_coefficients_strict_upper"]),
            )

    def test_refuses_bad_rational_types_sizes_and_empty_modes(self):
        for ratios, squares in (
            ((), ()),
            ((1.0,), (Fraction(1),)),
            ((Fraction(-1),), (Fraction(1),)),
            ((Fraction(1),), (Fraction(-1),)),
            ((Fraction(1),) * 17, (Fraction(1),) * 17),
            ((Fraction(1 << 1025),), (Fraction(1),)),
        ):
            with self.assertRaises(ValueError):
                MODULE.mode_certificate(ratios, squares)

    def test_owner_overlap_is_rejected_before_mode_claim(self):
        spec = deepcopy(self.predecessor.PANELS[0])
        spec["right_owners"] = ((2, 8513), *spec["right_owners"][1:])
        with self.assertRaisesRegex(ValueError, "distinct"):
            MODULE.panel_record(self.predecessor, spec)

    def test_predecessor_bytes_are_checked_before_import(self):
        with (
            patch.object(
                MODULE, "frozen_blob", return_value=b"not the reviewed producer\n"
            ),
            self.assertRaisesRegex(ValueError, "unreviewed predecessor"),
        ):
            MODULE.load_predecessor()

    def test_source_authentication_and_manifest_tamper_refusal(self):
        self.assertEqual(len(MODULE.authenticate_sources()), 10)
        data = json.loads(MODULE.LOCK.read_text(encoding="utf-8"))
        data["sources"][0]["git_blob"] = "0" * 40
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tampered.sources.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with (
                patch.object(MODULE, "LOCK", path),
                self.assertRaisesRegex(ValueError, "manifest blob mismatch"),
            ):
                MODULE.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
