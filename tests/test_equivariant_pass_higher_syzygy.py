"""Complete-weight and hostile-source controls for the higher Q-syzygy."""

import copy
import hashlib
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/five-hour-equivariant-pass/higher_syzygy.py"
)
SPEC = importlib.util.spec_from_file_location("higher_syzygy_under_test", PATH)
H = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(H)


class HigherSyzygyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = H.load_input()
        cls.blocks = H.all_blocks(cls.source)
        cls.central = next(block for block in cls.blocks if block[0] == (4, 4, 4))
        cls.central_record = H.block_record(cls.source, *cls.central)

    def test_shape_is_complete_and_pre_rank(self):
        shape = H.shape(self.source)
        self.assertEqual(
            (shape["weight_count"], shape["total_domain"], shape["total_target"]),
            (46, 2720, 1105),
        )
        self.assertEqual((shape["maximum_domain"], shape["maximum_target"]), (236, 112))
        self.assertTrue(shape["within_registered_512_cap"])
        self.assertFalse(shape["rank_calculation_performed"])

    def test_every_weight_once_and_dimension_totals(self):
        weights = [row[0] for row in self.blocks]
        self.assertEqual(len(weights), len(set(weights)))
        self.assertTrue(all(sum(weight) == 12 for weight in weights))
        self.assertEqual(sum(len(row[1]) for row in self.blocks), 2720)
        self.assertEqual(sum(len(row[2]) for row in self.blocks), 1105)

    def test_central_kernel_rank_nullity_and_direct_factor_action(self):
        _, domain, target, columns = self.central
        rank, kernels, digest = H.kernel_basis(self.source.q, columns)
        self.assertEqual((len(domain), len(target)), (236, 112))
        self.assertEqual(rank + len(kernels), len(domain))
        self.assertEqual(len(digest), 64)
        for permutation, expected in (
            ((1, 0, 2), self.central_record["kernel_factor_class_traces"][1]),
            ((1, 2, 0), self.central_record["kernel_factor_class_traces"][2]),
        ):
            self.assertEqual(
                H.kernel_trace(self.source, domain, columns, kernels, permutation),
                expected,
            )

    def test_factor_action_preserves_actual_kernel_not_only_dimension(self):
        _, domain, _, columns = self.central
        _, kernels, _ = H.kernel_basis(self.source.q, columns)
        moved = H.source_permutation(self.source, domain, kernels[0], (1, 0, 2))
        self.assertFalse(self.source.q.apply(columns, moved))
        self.assertNotEqual(moved, {})

    def test_changed_matrix_column_changes_digest(self):
        _, _, _, columns = self.central
        changed = copy.deepcopy(columns)
        key = next(iter(next(column for column in changed if column)))
        changed[next(i for i, column in enumerate(changed) if column)][key] *= -1
        self.assertNotEqual(
            H.kernel_basis(self.source.q, columns)[2],
            H.kernel_basis(self.source.q, changed)[2],
        )

    def test_deleted_complete_weight_is_detected_by_totals(self):
        changed = self.blocks[:-1]
        self.assertNotEqual(sum(len(row[1]) for row in changed), 2720)

    def test_exterior_square_and_factor_character_arithmetic(self):
        q_character = (17, -1, -7)
        q_squared = (17, 17, -7)
        exterior = tuple(
            (a * a - b) // 2 for a, b in zip(q_character, q_squared, strict=True)
        )
        self.assertEqual(exterior, (136, -8, 28))
        source = tuple(a * b for a, b in zip(exterior, (20, 0, -10), strict=True))
        target = tuple(a * b for a, b in zip(q_character, (65, -25, 35), strict=True))
        self.assertEqual(source, (2720, 0, -280))
        self.assertEqual(target, (1105, 25, -245))

    def test_E3_character_decomposition_is_exact(self):
        character = (1550, 0, -70)
        multiplicities = (
            (character[0] + 3 * character[1] + 2 * character[2]) // 6,
            (character[0] - 3 * character[1] + 2 * character[2]) // 6,
            (character[0] - character[2]) // 3,
        )
        self.assertEqual(multiplicities, (235, 235, 540))
        self.assertEqual(
            (
                multiplicities[0] + multiplicities[1] + 2 * multiplicities[2],
                multiplicities[0] - multiplicities[1],
                multiplicities[0] + multiplicities[1] - multiplicities[2],
            ),
            character,
        )

    def test_d2_source_authentication_precedes_compile(self):
        with (
            patch.object(H, "frozen", side_effect=ValueError("changed d2 source")),
            patch("builtins.compile", side_effect=RuntimeError("must not compile")),
            self.assertRaisesRegex(ValueError, "changed d2 source"),
        ):
            H.load_input()

    def test_changed_frozen_blob_refused(self):
        with (
            patch.object(H.subprocess, "check_output", return_value=b"changed"),
            self.assertRaisesRegex(ValueError, "frozen d2 source"),
        ):
            H.frozen("path", "0" * 40)

    def test_strict_json_rejects_duplicates_and_all_float_aliases(self):
        for raw in (b'{"x":1,"x":1}', b'{"x":1.0}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                H.strict_json(raw)

    def test_typed_complete_artifact_comparison(self):
        body = {"surjective": True, "global_rank": 1105}
        original = dict(
            body, proof_sha256=hashlib.sha256(H.canonical(body).encode()).hexdigest()
        )
        H.check_record(original, original)
        for changed in (
            dict(body, surjective=1),
            dict(body, global_rank=1105.0),
            dict(body, global_rank=1104),
        ):
            counterfeit = dict(
                changed,
                proof_sha256=hashlib.sha256(H.canonical(changed).encode()).hexdigest(),
            )
            with self.assertRaisesRegex(ValueError, "typed complete"):
                H.check_record(counterfeit, original)

    def test_body_digest_refuses_self_consistent_field_change_without_rehash(self):
        with self.assertRaisesRegex(ValueError, "body digest"):
            H.check_record({"global_rank": 1104, "proof_sha256": "0" * 64}, {})

    def test_integer_string_bool_pins_not_interchangeable(self):
        for value in (1, True, 1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                H.frozen("path", value)

    def test_shape_refuses_registered_cap_violation(self):
        with (
            patch.object(H, "MAX_BLOCK", 111),
            self.assertRaisesRegex(ValueError, "exceeds512"),
        ):
            H.all_blocks(self.source)

    def test_weight_order_is_deterministic(self):
        weights = [row[0] for row in self.blocks]
        self.assertEqual(weights, sorted(weights, reverse=True))


if __name__ == "__main__":
    unittest.main()
