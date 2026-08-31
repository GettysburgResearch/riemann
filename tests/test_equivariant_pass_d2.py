"""Source-chain and hostile-record controls for the actual higher differential."""

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
    / "research/l-families/atlas/generalized/segre-hadamard-source/five-hour-equivariant-pass/d2_replay.py"
)
SPEC = importlib.util.spec_from_file_location("equivariant_d2_under_test", PATH)
D = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(D)


class D2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = D.load_input()
        cls.q = cls.data.q
        cls.weight = (6, 4, 2)
        cls.target = D.WeightComplex(cls.q, cls.weight)
        cls.homology = cls.q.Homology(cls.target, 2)
        cls.domain, cls.codomain, cls.delta = D.q_delta(cls.data, cls.weight)
        cls.block = D.build_block(cls.data, cls.weight)
        cls.row = next(row for row in cls.block["d2_rows"] if row["image"])

    def verify(self, row):
        D.verify_d2_row(self.data, self.domain, self.delta, self.homology, row)

    def test_original_chain_lift_and_target_quotient(self):
        self.verify(self.row)
        self.assertEqual(self.block["target_H2_class_traces"], [1, -1, 1])

    def test_complete_kernel_rank_nullity(self):
        span = self.q.Span()
        for row in self.block["d2_rows"]:
            vector = self.q.decode_vector(row["kernel"], len(self.domain))
            self.assertFalse(self.q.apply(self.delta, vector))
            self.assertTrue(span.insert(vector)[0])
        self.assertEqual(span.rank + self.block["Q_delta_rank"], len(self.domain))

    def test_wrong_lift_sign(self):
        row = copy.deepcopy(self.row)
        for term in row["lift"]:
            term[2] *= -1
        with self.assertRaisesRegex(ValueError, "W boundary lift"):
            self.verify(row)

    def test_wrong_higher_differential_sign(self):
        row = copy.deepcopy(self.row)
        for term in row["source_cycle"]:
            term[1] *= -1
        with self.assertRaisesRegex(ValueError, "delta of lift"):
            self.verify(row)

    def test_false_target_homology_projection(self):
        row = copy.deepcopy(self.row)
        row["image"][0][1] *= -1
        with self.assertRaisesRegex(ValueError, "target quotient"):
            self.verify(row)

    def test_missing_lift_term(self):
        row = copy.deepcopy(self.row)
        row["lift"].pop()
        with self.assertRaises(ValueError):
            self.verify(row)

    def test_zero_kernel_refused(self):
        row = copy.deepcopy(self.row)
        row["kernel"] = []
        with self.assertRaisesRegex(ValueError, "nonzero Q-Koszul"):
            self.verify(row)

    def test_noncycle_kernel_refused(self):
        index = next(i for i, column in enumerate(self.delta) if column)
        row = copy.deepcopy(self.row)
        row["kernel"] = [[index, 1, 1]]
        with self.assertRaisesRegex(ValueError, "Q-Koszul kernel"):
            self.verify(row)

    def test_unknown_row_field_refused(self):
        row = copy.deepcopy(self.row)
        row["guessed_sign"] = 1
        with self.assertRaisesRegex(ValueError, "row fields"):
            self.verify(row)

    def test_typed_lift_indices(self):
        for value in (True, 1.0, "1"):
            with self.subTest(value=value):
                row = copy.deepcopy(self.row)
                row["lift"][0][0] = value
                with self.assertRaises(ValueError):
                    self.verify(row)

    def test_duplicate_lift_and_noncanonical_fraction(self):
        row = copy.deepcopy(self.row)
        row["lift"].insert(1, row["lift"][0])
        with self.assertRaises(ValueError):
            self.verify(row)
        row = copy.deepcopy(self.row)
        row["lift"][0][2] *= 2
        row["lift"][0][3] *= 2
        with self.assertRaises(ValueError):
            self.verify(row)

    def test_complete_weight_and_original_row_caps(self):
        report = D.shape_report(self.data.character)
        self.assertEqual(
            [r["W_chain_dimensions"] for r in report["blocks"]],
            [[75, 238, 244, 86, 6], [81, 264, 279, 98, 6], [105, 364, 401, 146, 10]],
        )
        self.assertFalse(report["rank_calculation_performed"])
        with self.assertRaises(ValueError):
            D.WeightComplex(self.q, (4, 4, 4))
        with self.assertRaises(ValueError):
            D.source_by_weight(5)

    def test_source_authentication_precedes_compilation(self):
        with (
            patch.object(D, "frozen", side_effect=ValueError("changed primitive")),
            patch("builtins.compile", side_effect=RuntimeError("must not compile")),
            self.assertRaisesRegex(ValueError, "changed primitive"),
        ):
            D.load_input()

    def test_changed_frozen_blob_refused(self):
        with (
            patch.object(D.subprocess, "check_output", return_value=b"changed"),
            self.assertRaisesRegex(ValueError, "blob mismatch"),
        ):
            D.frozen(D.Q_FREEZE, "source.py", "0" * 40)

    def test_strict_json_all_numeric_aliases_and_duplicates(self):
        for raw in (b'{"x":1,"x":1}', b'{"x":[1.0]}', b'{"x":NaN}', b'{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                D.strict_json(raw)
        self.assertEqual(D.strict_json(b'{"x":[1,true]}'), {"x": [1, True]})

    def test_artifact_typed_comparison_and_complete_coverage(self):
        body = {"rank": 1, "weights": [[6, 4, 2], [5, 5, 2], [5, 4, 3]]}
        original = dict(
            body, proof_sha256=hashlib.sha256(D.canonical(body).encode()).hexdigest()
        )
        D.check_record(original, original)
        for changed in (
            dict(body, rank=True),
            dict(body, rank=1.0),
            dict(body, weights=body["weights"][:-1]),
        ):
            counterfeit = dict(
                changed,
                proof_sha256=hashlib.sha256(D.canonical(changed).encode()).hexdigest(),
            )
            with self.assertRaisesRegex(ValueError, "typed complete"):
                D.check_record(counterfeit, original)

    def test_body_digest_rejection(self):
        with self.assertRaisesRegex(ValueError, "body digest"):
            D.check_record({"rank": 65, "proof_sha256": "0" * 64}, {})

    def test_factor_action_matches_quotient_not_only_dimensions(self):
        image = self.q.decode_vector(self.row["image"], len(self.homology.cycles))
        transposition = self.q.homology_permutation(self.homology, (1, 0, 2))
        cycle = self.q.homology_permutation(self.homology, (1, 2, 0))
        self.assertEqual(
            self.q.apply(transposition, image), {i: -a for i, a in image.items()}
        )
        self.assertEqual(self.q.apply(cycle, image), image)
        self.assertTrue(all(isinstance(a, Fraction) for a in image.values()))


if __name__ == "__main__":
    unittest.main()
