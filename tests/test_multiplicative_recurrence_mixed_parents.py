"""Independent small controls and hostile contracts for the GLO764 packet."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/multiplicative_recurrence_mixed_parents.py"
)
SPEC = importlib.util.spec_from_file_location("mulrec_mixed", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load exact packet producer")
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class CircleTests(unittest.TestCase):
    def test_direct_bivariate_polynomial(self):
        # Independent polynomial multiplication in the Laurent ring.
        for m, n in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (3, 3)):
            answer = {0: Fraction(1)}
            for shift in [1] * m + [-1] * n:
                new = {}
                for exponent, value in answer.items():
                    new[exponent] = new.get(exponent, 0) + Fraction(3, 2) * value
                    new[exponent + shift] = new.get(exponent + shift, 0) + value
                answer = new
            self.assertEqual(M.circle_spectrum(Fraction(3, 2), m, n), answer)
            self.assertEqual(len(answer), m + n + 1)

    def test_first_genuine_mixed_map(self):
        self.assertEqual(M.circle_spectrum(2, 1, 1), {-1: 2, 0: 5, 1: 2})

    def test_periodic_aliases(self):
        for m, n in ((1, 1), (3, 2), (0, 5)):
            for period in (1, 2, 3, 5, 8, 13):
                self.assertEqual(
                    M.periodic_circle_order(2, m, n, period), min(period, m + n + 1)
                )

    def test_exact_bounded_moduli_and_twist_slices(self):
        for order_cap in range(1, 17):
            lattice = [
                (m, n)
                for m in range(order_cap)
                for n in range(order_cap)
                if m + n < order_cap
            ]
            self.assertEqual(M.moduli_count(order_cap), len(lattice))
            for weight in range(-16, 17):
                self.assertEqual(
                    M.moduli_count(order_cap, weight),
                    sum(m - n == weight for m, n in lattice),
                )

    def test_moduli_caps(self):
        for order_cap in (0, 17, 10**20):
            with self.assertRaises(ValueError):
                M.moduli_count(order_cap)
        with self.assertRaises(TypeError):
            M.moduli_count(True)
        with self.assertRaises(TypeError):
            M.moduli_count(3, 1.0)

    def test_origin_touching_counterfeit_identity(self):
        # (w+w^2)(1+w^-1)=(1+w)^2; this is why c=1 is excluded.
        result = {}
        for i in (1, 2):
            for j in (-1, 0):
                result[i + j] = result.get(i + j, 0) + 1
        self.assertEqual(result, {0: 1, 1: 2, 2: 1})

    def test_scope_refusals(self):
        for c in (0, 1, -2, Fraction(1, 2)):
            with self.assertRaises(ValueError):
                M.circle_spectrum(c, 1, 1)
        for c in (True, 1.5, complex(2, 0)):
            with self.assertRaises(TypeError):
                M.circle_spectrum(c, 1, 1)
        for m, n in ((4, 4), (-1, 0), (999999999, 0)):
            with self.assertRaises(ValueError):
                M.circle_spectrum(2, m, n)
        with self.assertRaises(TypeError):
            M.circle_spectrum(2, True, 1)
        with self.assertRaises(ValueError):
            M.periodic_circle_order(2, 1, 1, 33)


class LocalShadowTests(unittest.TestCase):
    def test_generic_rank_two_order(self):
        for m, n in ((0, 0), (1, 1), (2, 1), (2, 2)):
            row = M.shadow_control(((2, 1), (3, 2)), m, n)
            self.assertEqual(row["actual_order"], (m + 1) * (n + 1))

    def test_held_out_rank_three_order(self):
        row = M.shadow_control(((2, 1), (3, 2), (4, 1)), 2, 1)
        self.assertEqual(row["actual_order"], 18)

    def test_real_input_is_not_generic_complex_input(self):
        row = M.shadow_control(((2, 0), (3, 0)), 1, 1)
        self.assertEqual(row["actual_order"], 3)
        self.assertEqual(row["generic_bound"], 4)

    def test_torsion_collision_and_zero_coefficients(self):
        row = M.shadow_control(((0, 1), (0, -1)), 1, 1)
        self.assertEqual(row["actual_order"], 2)
        self.assertEqual(row["generic_bound"], 4)

    def test_binet_matches_independent_local_recurrence(self):
        roots = M.gaussian_inputs(((2, 1), (3, 2)))
        coefficients = M.binet_coefficients(roots)
        values = M.local_h_sequence(roots, 9)
        for r, actual in enumerate(values):
            wanted = M.ZERO
            for root, coefficient in zip(roots, coefficients):
                wanted = M.gadd(wanted, M.gmul(coefficient, M.gpow(root, r)))
            self.assertEqual(actual, wanted)

    def test_prescan_spectrum_cap(self):
        # No expensive Binet denominator is built for an oversized request.
        with (
            patch.object(
                M,
                "binet_coefficients",
                side_effect=AssertionError("expanded before refusal"),
            ),
            self.assertRaises(ValueError),
        ):
            M.shadow_spectrum(((2, 1), (3, 2), (4, 1)), 3, 3)

    def test_bad_roots_refused(self):
        for roots in (
            ((0, 0), (2, 1)),
            ((2, 1), (2, 1)),
            ((1, 0), (2, 0), (3, 0), (4, 0)),
        ):
            with self.assertRaises(ValueError):
                M.shadow_spectrum(roots, 1, 1)
        with self.assertRaises(TypeError):
            M.shadow_spectrum(((2.0, 1), (3, 2)), 1, 1)


class MixedRankTests(unittest.TestCase):
    def test_known_unequal_segre_numerators(self):
        rows = {
            (1, 1, 4): [1],
            (2, 2): [1, 1],
            (2, 3): [1, 2],
            (2, 4): [1, 3],
            (3, 3): [1, 4, 1],
            (2, 2, 2): [1, 4, 1],
            (2, 3, 4): [1, 17, 33, 9],
        }
        for ranks, expected in rows.items():
            self.assertEqual(M.identity_numerator(ranks), expected)
            self.assertEqual(M.finite_difference_numerator(ranks), expected)

    def test_order_of_inputs_does_not_change_answer(self):
        self.assertEqual(
            M.identity_numerator((4, 2, 3)), M.identity_numerator((2, 3, 4))
        )

    def test_all_hard_boundary_profiles(self):
        for ranks in ((5, 5), (2, 3, 5), (2, 2, 2, 2, 2), (1, 2, 3, 3, 4)):
            row = M.rank_control(ranks)
            self.assertEqual(row["negative_roots"], row["degree"])
            self.assertTrue(row["simple"])

    def test_parent_classification_calibrations(self):
        for ranks in ((1,), (1, 1), (5,), (1, 1, 5), (2, 2), (1, 2, 1, 2)):
            self.assertTrue(M.finite_parent_case(ranks))
        for ranks in ((2, 3), (2, 4), (3, 3), (2, 2, 2), (1, 2, 3)):
            self.assertFalse(M.finite_parent_case(ranks))

    def test_second_relation_module_independent_count(self):
        for ranks, expected in (
            ((2, 2), -1),
            ((2, 3), -3),
            ((3, 3), -9),
            ((1, 2, 3), -3),
            ((1, 1, 5), 0),
        ):
            self.assertEqual(M.second_grade(ranks), (expected, expected))

    def test_sturm_rejects_repeated_or_positive_roots(self):
        self.assertEqual(M.sturm_negative_simple([1, 2, 1]), (1, False))
        self.assertEqual(M.sturm_negative_simple([1, -2, 1]), (0, False))
        self.assertEqual(M.sturm_negative_simple([-1, 0, 1]), (1, True))
        with self.assertRaisesRegex(ValueError, "zero endpoint excluded"):
            M.sturm_negative_simple([0, 1])

    def test_rank_profile_prescan_refusals(self):
        for ranks in ((), (0,), (6,), (5, 5, 5), (1,) * 6):
            with self.assertRaises(ValueError):
                M.identity_numerator(ranks)
        for ranks in ((True,), (2.0,), [2, 3]):
            with self.assertRaises(TypeError):
                M.identity_numerator(ranks)

    def test_independent_rank_two_and_jordan_identity(self):
        row = M.tensor_pair_control(((2, 1), (0, 2)), ((3, 0), (1, 3)))
        self.assertEqual(row["tensor_denominator"], [1, -24, 216, -864, 1296])
        self.assertEqual(row["numerator"], [1, 0, -36])
        # Cancellation makes the scalar order three, despite dimension four.
        self.assertEqual(M.ipoly_mul([1, -6], [1, 6]), row["numerator"])

    def test_independent_nonsymmetric_tensor_identity(self):
        row = M.tensor_pair_control(((1, 2), (3, 4)), ((-2, 1), (1, 3)))
        self.assertEqual(row["numerator"], [1, 0, -14])


class SourceAndArtifactTests(unittest.TestCase):
    def test_frozen_primitive_authentication(self):
        self.assertEqual(M.authenticate(), M.sources_contract())

    def test_manifest_tamper_is_rejected(self):
        original = Path.read_text

        def patched(path, *args, **kwargs):
            if path == M.MANIFEST:
                altered = M.sources_contract()
                altered["base_commit"] = "0" * 40
                return json.dumps(altered)
            return original(path, *args, **kwargs)

        with patch.object(Path, "read_text", patched), self.assertRaises(ValueError):
            M.authenticate()

    def test_current_source_tamper_is_rejected(self):
        original = Path.read_bytes

        def patched(path):
            if path == ROOT / M.SOURCE_ROWS[0][0]:
                return b"tampered primitive\n"
            return original(path)

        with patch.object(Path, "read_bytes", patched), self.assertRaises(ValueError):
            M.authenticate()

    def test_owned_hashes_and_canonical_payload(self):
        payload = json.loads(M.FIXTURE.read_text(encoding="utf-8"))
        recorded = payload.pop("payload_sha256")
        self.assertEqual(recorded, hashlib.sha256(M.canonical(payload)).hexdigest())
        for relative, digest in payload["owned_files"].items():
            self.assertEqual(digest, M.digest((ROOT / relative).read_bytes()))


if __name__ == "__main__":
    unittest.main()
