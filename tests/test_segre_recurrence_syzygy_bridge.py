"""Exact-map and hostile release tests, independent of scalar rank fitting."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT / "research/l-families/atlas/generalized/segre_recurrence_syzygy_bridge.py"
)
SPEC = importlib.util.spec_from_file_location("segre_bridge", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SegreBridgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()
        cls.native = cls.report["native_cubic_maps"]
        cls.scalar = cls.report["scalar_controls"]

    def test_fixture(self):
        M.same_json(M.strict_json(M.bounded_bytes(M.FIXTURE)), self.report)

    def test_preregistered_dimensions_are_distinct(self):
        self.assertEqual(self.native["generators"], 27)
        self.assertEqual(self.native["quadrics"], 162)
        self.assertEqual(self.native["cubic_syzygies"], 1720)
        self.assertEqual(self.native["cubic_dual_algebra"], 9019)
        self.assertNotEqual(1720, 9019)

    def test_complete_maps(self):
        self.assertEqual(
            self.native["totals"],
            {
                "symmetric_cubic_rows": 3654,
                "syzygy_columns": 4374,
                "syzygy_map_rank": 2654,
                "tensor_words": 19683,
                "dual_columns": 11664,
                "dual_ideal_rank": 10664,
                "cubic_lie_dimension": 1720,
                "bar_vertices": 11664,
            },
        )
        self.assertEqual(len(self.native["blocks"]), 1000)
        self.assertEqual(len(self.native["cubic_character"]), 460)

    def test_every_weight_block_has_native_equalities(self):
        for row in self.native["blocks"]:
            self.assertEqual(row["syzygy_map_rank"], row["symmetric_cubic_rows"] - 1)
            self.assertEqual(
                row["cubic_lie_dimension"],
                row["syzygy_columns"] - row["syzygy_map_rank"],
            )
            self.assertEqual(row["bar_components"], 1)
            self.assertEqual(row["dual_ideal_rank"], row["bar_vertices"] - 1)

    def test_full_character_not_only_dimension(self):
        self.assertEqual(
            self.native["cubic_character"],
            M.character_rows(M.predicted_character((3, 3, 3), 3)),
        )
        self.assertEqual(
            self.native["quadratic_character"],
            M.character_rows(M.predicted_character((3, 3, 3), 2)),
        )
        central = next(
            row for row in self.native["blocks"] if row["weight"] == [[0, 1, 2]] * 3
        )
        self.assertEqual(central["cubic_lie_dimension"], 46)
        self.assertEqual(central["tensor_words"] - central["dual_ideal_rank"], 163)

    def test_wrong_character_prediction_is_a_falsifier(self):
        original = M.predicted_character

        def wrong(ranks, degree):
            value = original(ranks, degree)
            if degree == 3:
                value[next(iter(value))] += 1
            return value

        with (
            patch.object(M, "predicted_character", side_effect=wrong),
            self.assertRaisesRegex(ValueError, "cubic Schur"),
        ):
            M.native_cubic((2, 2, 2))

    def test_cyclic_spectrum_whole_character(self):
        self.assertEqual(self.scalar["cyclic_syzygy_multiplicities"], [568, 576, 576])
        self.assertEqual(self.scalar["cyclic_syzygy_trace"], -8)

    def test_cyclic_cancellation(self):
        s = self.slice(Fraction(-1))
        self.assertEqual(s["reduced_numerator"], [[1, 1]])
        self.assertEqual(s["reduced_denominator"], [[1, 1], [0, 1], [0, 1], [-1, 1]])
        self.assertEqual(len(self.scalar["cyclic_universal_numerator"]) - 1, 7)
        self.assertEqual(len(self.scalar["cyclic_ambient_K"]) - 1, 24)

    def slice(self, x):
        return next(
            row
            for row in self.scalar["self_dual_slice_panels"]
            if row["x"] == [x.numerator, x.denominator]
        )

    def test_cancellation_without_input_collision(self):
        a, b = self.slice(Fraction(-3)), self.slice(Fraction(-8))
        self.assertEqual(a["reduced_numerator"], M.encoded([1, 2, 1]))
        self.assertEqual(b["reduced_numerator"], M.encoded([1, 91, -91, -1]))
        self.assertEqual(len(a["reduced_denominator"]) - 1, 5)
        self.assertEqual(len(b["reduced_denominator"]) - 1, 6)

    def test_symbolic_not_interpolated_slice(self):
        row = self.scalar["symbolic_slice"]
        self.assertEqual(row["coefficient_identities"], 13)
        self.assertEqual(row["sampled_x_for_identity"], 0)
        self.assertEqual(row["M_minus2"], M.encoded([0, -3, 2, 1]))
        self.assertEqual(row["M_plus2"], M.encoded([8, 17, 10, 1]))

    def test_purity_root_bracket_and_positive_derivative(self):
        self.assertEqual(self.scalar["root_bracket_values"], [[-71, 81], [1, 1024]])
        self.assertTrue(
            all(x > 0 for x in self.scalar["positive_Bernstein_coefficients"])
        )
        self.assertEqual(M.evaluate([4, -8, 9, 16, 4], Fraction(-2)), -8)
        self.assertEqual(M.evaluate([4, -8, 9, 16, 4], Fraction(-1)), 9)

    def test_unitary_input_can_have_nonpure_defect(self):
        # x=1: input eigenvalues 1 and primitive sixth roots, but reduced
        # defect 1+7T+T² has inverse-root sum -7, outside [-2,2].
        self.assertEqual(
            self.slice(Fraction(1))["reduced_numerator"], M.encoded([1, 7, 1])
        )

    def test_additional_heldout_matrix_matches_slice(self):
        # Not one of the thirteen scalar panels: compare to literal eigenvalues.
        x = Fraction(5, 2)
        literal = M.recurrence_panel((2, 1, Fraction(1, 2)), 3)
        sliced = M.slice_polynomials(x)
        self.assertEqual(literal["reduced_numerator"], sliced["reduced_numerator"])
        self.assertEqual(literal["reduced_denominator"], sliced["reduced_denominator"])
        p = [Fraction(a, b) for a, b in sliced["numerator"]]
        self.assertEqual(
            literal["universal_numerator"],
            M.encoded(M.pmul(p, M.pmul([1, -1], [1, -x, 1]))),
        )

    def test_generic_identity_and_specialization_are_different(self):
        rows = self.scalar["rational_recurrence_panels"]
        generic, identity = rows[2], rows[3]
        self.assertEqual(len(generic["reduced_denominator"]) - 1, 10)
        self.assertEqual(len(generic["reduced_numerator"]) - 1, 7)
        self.assertEqual(len(identity["universal_denominator"]) - 1, 10)
        self.assertEqual(len(identity["reduced_denominator"]) - 1, 7)
        self.assertEqual(identity["reduced_numerator"], M.encoded([1, 20, 48, 20, 1]))

    def test_rank_two_small_discriminator(self):
        square, cube = self.scalar["rational_recurrence_panels"][:2]
        self.assertEqual(square["universal_numerator"], M.encoded([1, 6]))
        self.assertEqual(cube["universal_numerator"], M.encoded([1, 60, 216]))
        self.assertEqual(M.pmul([1, 6], [1, -6]), [1, 0, -36])

    def test_hankel_rank_strata(self):
        rows = self.scalar["rational_recurrence_panels"]
        self.assertEqual([row["finite_Hankel_rank"] for row in rows], [3, 4, 10, 7, 2])
        for row in rows:
            self.assertEqual(
                row["finite_Hankel_rank"], len(row["reduced_denominator"]) - 1
            )

    def test_rank_two_identity_noncyclotomic(self):
        row = M.recurrence_panel((1, 1), 3)
        self.assertEqual(row["reduced_numerator"], M.encoded([1, 4, 1]))
        self.assertEqual(M.evaluate([1, 4, 1], Fraction(-1)), -2)

    def test_small_native_controls_and_factor_permutations(self):
        for ranks, syz, dual in [
            ((2, 2), 0, 8),
            ((2, 3), 2, 40),
            ((3, 2), 2, 40),
            ((3, 3), 16, 181),
            ((2, 2, 2), 16, 144),
        ]:
            row = M.native_cubic(ranks)
            self.assertEqual(
                (row["cubic_syzygies"], row["cubic_dual_algebra"]), (syz, dual)
            )

    def test_polynomial_ring_controls(self):
        for ranks in ((1,), (3,), (1, 3, 1)):
            row = M.native_cubic(ranks)
            self.assertEqual(row["quadrics"], 0)
            self.assertEqual(row["cubic_syzygies"], 0)

    def test_matrix_caps_before_allocation(self):
        with patch.object(M, "product", side_effect=RuntimeError("allocated early")):
            for ranks in ([4], [3] * 4, [True], [3.0], [], None):
                with self.assertRaises(ValueError):
                    M.native_cubic(ranks)

    def test_strict_integer_and_exact_scalar_types(self):
        class IntSubclass(int):
            pass

        for value in (True, 1.0, IntSubclass(1), "1", None):
            with self.assertRaises(ValueError):
                M.integer(value, 0, 4)
            with self.assertRaises(ValueError):
                M.exact(value)

    def test_bit_degree_and_matrix_caps(self):
        for value in (1 << (M.MAX_BITS + 1), Fraction(1, 1 << (M.MAX_BITS + 1))):
            with self.assertRaises(ValueError):
                M.exact(value)
        with self.assertRaises(ValueError):
            M.poly([0] * (M.MAX_POLY + 1))
        with self.assertRaises(ValueError):
            M.sparse_basis([{}] * (M.MAX_BLOCK_COLS + 1), 1)
        with self.assertRaises(ValueError):
            M.sparse_basis([], M.MAX_BLOCK_ROWS + 1)
        with self.assertRaises(ValueError):
            M.sparse_basis([{True: 1}], 2)

    def test_recurrence_input_guards(self):
        for values, power in [
            ((0, 1), 2),
            ((1, 2), True),
            ((1, 2), 4),
            ((1, 2, 3, 4), 2),
            ((1.0, 2), 2),
            ((1 << 40,), 1),
        ]:
            with self.assertRaises(ValueError):
                M.recurrence_panel(values, power)
        for x in (True, 1.0, 17, Fraction(1, 1 << 40)):
            with self.assertRaises(ValueError):
                M.slice_polynomials(x)

    def test_exact_rank_and_gcd_controls(self):
        self.assertEqual(len(M.sparse_basis([{0: 1, 1: 2}, {0: 2, 1: 4}], 2)), 1)
        self.assertEqual(
            len(M.sparse_basis([{0: Fraction(1, 3), 1: 1}, {0: 1, 1: 2}], 2)), 2
        )
        p, q, g = M.reduced([1, 0, -1], [1, -1])
        self.assertEqual((p, q, g), ([1, 1], [1], [1, -1]))

    def test_json_duplicate_float_nonfinite_and_caps(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"x":1.0}',
            b"NaN",
            b"Infinity",
            b"-Infinity",
            b"[" * 1500 + b"0" + b"]" * 1500,
            b"1" * 2000,
            b" " * (M.MAX_BYTES + 1),
            "{}",
            bytearray(b"{}"),
        ):
            with self.assertRaises(ValueError):
                M.strict_json(raw)

    def test_typed_replay(self):
        for value in (True, 1.0, "1"):
            with self.assertRaises(ValueError):
                M.same_json(value, 1)

    def test_source_manifest_rejects_resealed_drift(self):
        manifest = copy.deepcopy(M.EXPECTED_MANIFEST)
        manifest["parents"][0]["git_blob"] = "0" * 40
        with (
            patch.object(M, "bounded_bytes", return_value=M.canonical(manifest)),
            self.assertRaises(ValueError),
        ):
            M.source_locks()

    def test_source_blob_size_bytes_and_missing_object_guards(self):
        blob = M.EXPECTED_MANIFEST["parents"][0]["git_blob"]
        for outputs, pattern in [
            (["0" * 40], "blob mismatch"),
            ([blob, str(M.MAX_BYTES + 1)], "byte cap"),
            ([blob, "3", b"bad"], "digest mismatch"),
        ]:
            with (
                patch.object(M.subprocess, "check_output", side_effect=outputs),
                self.assertRaisesRegex(ValueError, pattern),
            ):
                M.source_locks()
        with (
            patch.object(
                M.subprocess,
                "check_output",
                side_effect=M.subprocess.CalledProcessError(1, ["git"]),
            ),
            self.assertRaisesRegex(ValueError, "unavailable"),
        ):
            M.source_locks()

    def test_current_source_bytes_are_authenticated(self):
        original = M.bounded_bytes
        parent = M.ROOT / M.EXPECTED_MANIFEST["parents"][0]["path"]
        with (
            patch.object(
                M,
                "bounded_bytes",
                side_effect=lambda p: b"bad" if p == parent else original(p),
            ),
            self.assertRaisesRegex(ValueError, "current parent"),
        ):
            M.source_locks()

    def test_preregistered_record_is_frozen_not_current(self):
        row = self.report["sources"]["parents"][-1]
        self.assertFalse(row["current_copy_required"])
        self.assertEqual(row["commit"], "64c8664a2fee08ae2e249743d6f784a7bec61b83")
        self.assertNotEqual(row["sha256_lf"], M.digest(M.bounded_bytes(M.NOTE)))

    def test_seals_payload_and_arithmetic(self):
        for path, value in self.report["artifact_sha256_lf"].items():
            self.assertEqual(value, M.digest(M.bounded_bytes(ROOT / path)))
        payload = copy.deepcopy(self.report)
        expected = payload.pop("payload_sha256")
        self.assertEqual(hashlib.sha256(M.canonical(payload)).hexdigest(), expected)
        self.assertEqual(
            payload["arithmetic"],
            {
                "class": "MIXED",
                "components": ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
                "rounding": "none",
            },
        )

    def test_full_resealed_fixture_mutations_rejected(self):
        for kind in ("weight", "rank", "missing", "taxonomy", "scope", "unknown"):
            altered = copy.deepcopy(self.report)
            if kind == "weight":
                altered["native_cubic_maps"]["cubic_character"][0]["multiplicity"] += 1
            elif kind == "rank":
                altered["native_cubic_maps"]["blocks"][0]["dual_ideal_rank"] += 1
            elif kind == "missing":
                altered["native_cubic_maps"]["blocks"].pop()
            elif kind == "taxonomy":
                altered["arithmetic"]["class"] = "EXACT"
            elif kind == "scope":
                altered["coverage"]["fitted_matrix_ranks"] = 1
            else:
                altered["extra"] = 1
            altered.pop("payload_sha256")
            altered["payload_sha256"] = hashlib.sha256(M.canonical(altered)).hexdigest()
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                M.same_json(altered, self.report)

    def test_lf_hash_and_source_boundaries(self):
        self.assertEqual(M.digest(b"a\nb\n"), M.digest(b"a\r\nb\r\n"))
        self.assertEqual(self.report["coverage"]["fitted_matrix_ranks"], 0)
        self.assertEqual(self.report["coverage"]["sampled_primes"], 0)
        note = M.NOTE.read_text(encoding="utf-8")
        for phrase in (
            "RH and GRH remain open",
            "not a superdeterminant",
            "Snowden",
            "specialization",
            "1720",
            "9019",
        ):
            self.assertIn(phrase, note)


if __name__ == "__main__":
    unittest.main()
