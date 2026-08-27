from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_boolean_frobenius_tomography.py"
)
SPEC = importlib.util.spec_from_file_location(
    "boolean_frobenius_tomography", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class BooleanFrobeniusTomographyTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_member_adaptive_filter_is_exact_and_minimal(self) -> None:
        row = subject.member_minimal_filter(
            {"a": 3, "b": 2},
            {"a": 1, "b": 1},
            {"a": 1, "b": 2},
        )
        self.assertEqual(row["filter_orders"], {"a": 2, "b": 1})
        self.assertEqual(row["filter_degree"], 4)
        self.assertEqual(
            subject.residual_profile({"a": 3, "b": 2}, row["filter_orders"]),
            {"a": 1, "b": 1},
        )
        with self.assertRaises(ValueError):
            subject.member_minimal_filter({"a": 1}, {"a": 2}, {"a": 1})
        with self.assertRaises(ValueError):
            subject.member_minimal_filter({"a": 1}, {}, {"a": 0})
        self.assertEqual(
            subject.member_minimal_filter({"a": 1}, {"a": 0, "absent": 0}, {"a": 1})[
                "filter_orders"
            ],
            {"a": 1},
        )

    def test_compatible_universal_filter(self) -> None:
        row = subject.universal_filter_trilemma(
            ({"a": 2, "b": 1}, {"a": 3, "c": 1}),
            ({"a": 1}, {"a": 2}),
            {"a": 1, "b": 2, "c": 2},
        )
        self.assertTrue(row["feasible"])
        self.assertEqual(row["filter_orders"], {"a": 1, "b": 1, "c": 1})
        self.assertEqual(row["filter_degree"], 5)
        self.assertEqual(row["residual_profiles"], ({"a": 1}, {"a": 2}))

    def test_full_deletion_is_the_lcm_profile(self) -> None:
        row = subject.universal_filter_trilemma(
            ({"a": 2, "b": 1}, {"a": 3, "c": 1}),
            ({"absent": 0}, {}),
            {"a": 1, "b": 2, "c": 2},
        )
        self.assertTrue(row["feasible"])
        self.assertEqual(row["filter_orders"], {"a": 3, "b": 1, "c": 1})
        self.assertEqual(row["filter_degree"], 7)

    def test_both_universal_obstruction_cases(self) -> None:
        retention_deletion = subject.universal_filter_trilemma(
            ({"a": 2}, {"a": 3}),
            ({"a": 1}, {}),
            {"a": 1},
        )
        unequal_retention = subject.universal_filter_trilemma(
            ({"a": 2}, {"a": 3}),
            ({"a": 1}, {"a": 1}),
            {"a": 1},
        )
        self.assertFalse(retention_deletion["feasible"])
        self.assertIn("below deletion bound", retention_deletion["conflicts"][0])
        self.assertFalse(unequal_retention["feasible"])
        self.assertIn("incompatible exact orders", unequal_retention["conflicts"][0])

    def test_galois_descent_requires_whole_orbits(self) -> None:
        orbit = (("i", "-i"),)
        self.assertTrue(subject.galois_stable_selection(orbit, frozenset(("i", "-i"))))
        self.assertFalse(subject.galois_stable_selection(orbit, frozenset(("i",))))
        with self.assertRaises(ValueError):
            subject.galois_stable_selection(orbit, frozenset(("other",)))

    def test_formal_double_root_energy(self) -> None:
        row = subject.formal_energy_control(40)
        self.assertEqual(row["character_energy"], "32923/3")
        self.assertEqual(row["character_leading_energy_coefficient"], "4/27")
        self.assertEqual(row["positive_boolean_leading_energy_coefficient"], "2/27")
        self.assertEqual(row["retained_principal_coefficient"], "2/3")
        self.assertTrue(row["positive_energy_identity_verified"])

    def test_exact_rational_series_recurrence(self) -> None:
        values = subject.rational_series(
            (Fraction(1), Fraction(1, 3)),
            (Fraction(1), Fraction(2), Fraction(1)),
            4,
        )
        self.assertEqual(
            values,
            (
                Fraction(1),
                Fraction(-5, 3),
                Fraction(7, 3),
                Fraction(-3),
                Fraction(11, 3),
            ),
        )

    def test_fixture_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)
        self.assertEqual(
            result["proof_ledger"]["finite_family_universal_trilemma"],
            "PROVED EXACT BY ORBIT VALUATIONS",
        )
        self.assertEqual(result["proof_ledger"]["rh_or_grh"], "NOT PROVED")
        self.assertEqual(result["resource_caps"]["moduli_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
