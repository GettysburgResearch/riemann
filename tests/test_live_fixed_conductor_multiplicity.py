"""Independent finite controls and refusal paths for the live multiplicity packet."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from copy import deepcopy
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "fixed_conductor_multiplicity",
    ROOT / "research" / "riemann-structures" / "live_fixed_conductor_multiplicity.py",
)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FixedConductorMultiplicityTests(unittest.TestCase):
    def test_independent_core_cutoff_transition(self):
        left, right = (5, 17, 19, 59), (7, 17, 19, 59)
        self.assertEqual(MODULE.vaughan_coefficient(left, 256), 2)
        self.assertEqual(MODULE.vaughan_coefficient(right, 256), 2)
        # At equality 5*59=295, the left balanced partition disappears.
        self.assertEqual(MODULE.histories(left, 295), [])
        self.assertEqual(MODULE.vaughan_coefficient(left, 295), 0)
        self.assertEqual(len(MODULE.histories(right, 295)), 2)
        self.assertEqual(MODULE.vaughan_coefficient(right, 295), 2)

    def test_two_live_panels_and_literal_resolution(self):
        first, second = map(MODULE.panel_record, MODULE.PANELS)
        self.assertEqual(first["left"]["products"], [33146, 33279, 33209])
        self.assertEqual(first["right"]["products"], [17251, 17131, 17261])
        self.assertEqual(
            (first["arithmetic_count"], first["literal_history_count"]), (9, 36)
        )
        self.assertEqual(
            (second["arithmetic_count"], second["literal_history_count"]), (12, 48)
        )
        self.assertEqual(first["residue_kernel_lower_bound_arithmetic"], 8)
        self.assertEqual(second["residue_kernel_lower_bound_literal"], 47)
        for record in (first, second):
            self.assertEqual(
                {tuple(row["cell"]) for row in record["arithmetic_pairs"]}, {(1, 4)}
            )
            self.assertFalse(record["full_native_coefficient_family_replayed"])
            self.assertFalse(record["asymptotic_prime_intervals_required_for_fixture"])

    def test_corner_operator_signs_and_source_factorization(self):
        matrix = MODULE.corner_matrix(3, 2)
        self.assertEqual(MODULE.exact_rank(matrix), 6)
        self.assertGreater(MODULE.quadratic(matrix, (1, 1, 1, 1, 1, 1)), 0)
        self.assertLess(MODULE.quadratic(matrix, (1, -1, 1, -1, 1, -1)), 0)
        # Constrained outer-product vector, not arbitrary native freedom.
        a, b = (1, -2, 4), (3, 5)
        z = tuple(x * y for x in a for y in b)
        expected = Fraction(24, 35) * (sum(a) ** 2 - sum(x * x for x in a))
        expected *= sum(b) ** 2 - sum(x * x for x in b)
        self.assertEqual(MODULE.quadratic(matrix, z), expected)

    def test_shared_row_or_column_deletion_degenerates_correctly(self):
        for m, n in ((1, 1), (1, 4), (4, 1)):
            self.assertEqual(MODULE.exact_rank(MODULE.corner_matrix(m, n)), 0)

    def test_same_cell_kernel_does_not_depend_on_other_cells(self):
        d = Fraction(24, 35)
        # An extra cell contributes the same value to both duplicated atoms.
        kernel = [
            [0, d, Fraction(1, 35)],
            [d, 0, Fraction(1, 35)],
            [Fraction(1, 35), Fraction(1, 35), 0],
        ]
        h = (1, -1, 0)
        image = tuple(sum(row[j] * h[j] for j in range(3)) for row in kernel)
        self.assertEqual(image, tuple(-d * x for x in h))

    def test_fixed_channel_correction_and_atom_counts(self):
        d, p, k = Fraction(24, 35), Fraction(2, 35), Fraction(22, 35)
        self.assertEqual(d, p + k)
        self.assertEqual((d / p, k / p), (12, 11))
        for amplitude in (Fraction(1, 225), Fraction(-7, 19)):
            grouped = 4 * amplitude
            literal_energy = 4 * amplitude**2
            delta = grouped**2 - literal_energy
            self.assertEqual(delta, Fraction(3, 4) * grouped**2)
            self.assertEqual(d * delta - k * delta, p * delta)

    def test_horizon_integer_contract(self):
        for exponent in (48, 60):
            y = 2**exponent
            u = 2 ** (exponent // 6)
            self.assertEqual(MODULE.sixth_root(y), u)
            self.assertEqual(MODULE.sixth_root(y - 1), u - 1)
        with self.assertRaises(ValueError):
            MODULE.sixth_root(True)
        with self.assertRaises(ValueError):
            MODULE.core_record(2**48 + 1, (17, 19, 59))

    def test_rejects_overlap_and_source_blind_congruence_changes(self):
        spec = deepcopy(MODULE.PANELS[0])
        spec["right_owners"] = ((2, 8513), *spec["right_owners"][1:])
        with self.assertRaisesRegex(ValueError, "distinct"):
            MODULE.panel_record(spec)
        spec = deepcopy(MODULE.PANELS[0])
        spec["left_owners"] = ((2, 16561), *spec["left_owners"][1:])
        with self.assertRaises(ValueError):
            MODULE.panel_record(spec)

    def test_refuses_bad_primes_types_and_caps(self):
        for value in (True, 1, -7, 21, MODULE.MAX_PRIME + 1):
            self.assertFalse(MODULE.is_prime(value))
        for labels in ((17, 17, 59), (17, 19, 57), [17, 19, 59]):
            with self.assertRaises(ValueError):
                MODULE.core_record(2**48, labels)
        for dims in ((0, 2), (5, 2), (True, 2)):
            with self.assertRaises(ValueError):
                MODULE.corner_matrix(*dims)
        with self.assertRaises(ValueError):
            MODULE.exact_rank([[0.0]])

    def test_source_manifest_authentication_and_tamper_refusal(self):
        self.assertEqual(len(MODULE.authenticate_sources()), 12)
        data = json.loads(MODULE.LOCK.read_text(encoding="utf-8"))
        data["sources"][0]["git_blob"] = "0" * 40
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.sources.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            with (
                patch.object(MODULE, "LOCK", path),
                self.assertRaisesRegex(ValueError, "blob mismatch"),
            ):
                MODULE.authenticate_sources()


if __name__ == "__main__":
    unittest.main()
