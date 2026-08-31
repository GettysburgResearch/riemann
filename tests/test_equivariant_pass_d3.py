"""Exact sign-isotypic and two-lift source controls for the actual d3."""

import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/segre-hadamard-source/five-hour-equivariant-pass/d3_replay.py"
)
SPEC = importlib.util.spec_from_file_location("actual_d3_under_test", PATH)
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)


class D3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = D.load_input()
        cls.domain, cls.target, cls.delta = D.q3_delta(cls.source)
        cls.rank, cls.kernels = D.complete_kernel(cls.source.q, cls.delta)
        cls.sign = D.SignComplex(cls.source.q)

    def test_full_shape_refusal_is_preserved(self):
        shape = D.shape_report(self.source)
        self.assertEqual(
            shape["internal5_W_chain_dimensions"], [180, 763, 1143, 730, 178, 9]
        )
        self.assertFalse(shape["within_registered_512_cap"])
        self.assertFalse(shape["rank_calculation_performed"])

    def test_sign_shape_is_complete_and_bounded(self):
        shape = D.sign_shape_report(self.source)
        self.assertEqual(shape["complete_Q_dimensions"], [512, 336])
        self.assertEqual(
            shape["sign_internal5_chain_dimensions"], [27, 110, 150, 76, 8, 0]
        )
        self.assertTrue(shape["within_registered_512_cap"])
        self.assertFalse(shape["rank_calculation_performed"])

    def test_Q3_complete_kernel_rank_nullity(self):
        self.assertEqual((len(self.domain), len(self.target)), (512, 336))
        self.assertEqual(self.rank + len(self.kernels), 512)
        for kernel in self.kernels:
            self.assertFalse(self.source.q.apply(self.delta, kernel))

    def test_first_lift_identity_in_original_coordinates(self):
        kernel = self.kernels[0]
        eta1 = D.eta1_for(self.source, self.domain, kernel)
        self.assertEqual(
            D.d_eta1(self.source, eta1),
            D.delta_z_original(self.source, self.domain, kernel),
        )

    def test_reversed_first_lift_sign_fails(self):
        kernel = self.kernels[0]
        eta1 = D.eta1_for(self.source, self.domain, kernel)
        changed = {key: -value for key, value in eta1.items()}
        self.assertNotEqual(
            D.d_eta1(self.source, changed),
            D.delta_z_original(self.source, self.domain, kernel),
        )

    def test_sign_basis_has_disjoint_canonical_pivots(self):
        for h, basis in enumerate(self.sign.chains):
            pivots = [next(iter(self.sign.embeddings[h][i])) for i in range(len(basis))]
            self.assertEqual(len(pivots), len(set(pivots)))
            self.assertTrue(all(len(vector) == 6 for vector in self.sign.embeddings[h]))

    def test_alternating_orbit_transposition_and_cycle(self):
        vector = self.sign.embeddings[3][0]
        wedge, _ = self.sign.full_chains[3][next(iter(vector))]
        for permutation, scalar in (((1, 0, 2), -1), ((1, 2, 0), 1)):
            moved = {}
            for index, coefficient in vector.items():
                _, record = self.sign.full_chains[3][index]
                row = self.sign.full_index[3][
                    wedge, tuple(record[i] for i in permutation)
                ]
                self.source.q.add(moved, {row: coefficient})
            self.assertEqual(moved, {i: scalar * a for i, a in vector.items()})

    def test_deleted_alternating_term_does_not_reconstruct(self):
        vector = copy.deepcopy(self.sign.embeddings[3][0])
        vector.pop(next(iter(vector)))
        coordinates = self.sign.sign_coordinates(3, vector)
        self.assertNotEqual(self.sign.expand(3, coordinates), vector)

    def test_sign_differential_original_reconstruction_and_square(self):
        for h in range(1, 6):
            for i, embedded in enumerate(self.sign.embeddings[h]):
                full = self.sign.full_apply(h, embedded)
                self.assertEqual(self.sign.expand(h - 1, self.sign.maps[h][i]), full)
        for h in range(2, 6):
            for column in self.sign.maps[h]:
                self.assertFalse(self.source.q.apply(self.sign.maps[h - 1], column))

    def test_sign_reynolds_is_idempotent(self):
        vector = {0: Fraction(1)}
        projected = self.sign.project(3, vector)
        again = self.sign.project(3, projected)
        self.assertEqual(projected, again)

    def test_sign_H3_target_is_one_dimensional(self):
        homology = self.source.q.Homology(self.sign, 3)
        self.assertEqual(len(homology.cycles), 1)
        self.assertEqual(self.sign.rank_rows[0]["homology_dimensions"][3], 1)

    def test_complete_source_authentication_precedes_compile(self):
        with (
            patch.object(D, "frozen", side_effect=ValueError("changed source")),
            patch("builtins.compile", side_effect=RuntimeError("must not compile")),
            self.assertRaisesRegex(ValueError, "changed source"),
        ):
            D.load_input()

    def test_changed_source_blob_refused(self):
        with (
            patch.object(D.subprocess, "check_output", return_value=b"changed"),
            self.assertRaisesRegex(ValueError, "source mismatch"),
        ):
            D.frozen("source", "0" * 40)

    def test_strict_json_numeric_and_duplicate_controls(self):
        for raw in (b'{"x":1,"x":1}', b'{"x":1.0}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                D.strict_json(raw)

    def test_typed_artifact_comparison(self):
        body = {"d3_image_rank": 1, "global_d3_surjectivity_claimed": False}
        original = dict(
            body, proof_sha256=hashlib.sha256(D.canonical(body).encode()).hexdigest()
        )
        D.check_record(original, original)
        for changed in (
            dict(body, d3_image_rank=True),
            dict(body, d3_image_rank=1.0),
            dict(body, global_d3_surjectivity_claimed=True),
        ):
            counterfeit = dict(
                changed,
                proof_sha256=hashlib.sha256(D.canonical(changed).encode()).hexdigest(),
            )
            with self.assertRaisesRegex(ValueError, "typed complete"):
                D.check_record(counterfeit, original)

    def test_body_digest_rejection(self):
        with self.assertRaisesRegex(ValueError, "body digest"):
            D.check_record({"d3_image_rank": 1, "proof_sha256": "0" * 64}, {})


if __name__ == "__main__":
    unittest.main()
