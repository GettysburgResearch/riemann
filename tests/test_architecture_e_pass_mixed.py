"""Exact source-algebra and acceptance controls for the mixed-node packet."""

import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/riemann-structures/native-five-hour-pass/architecture-e/mixed_packet_replay.py"
)
SPEC = importlib.util.spec_from_file_location("architecture_e_mixed", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class MixedSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e, cls.sources, cls.e4_proof = M.load_source()

    def test_complete_block_row_and_similarity(self):
        for nodes in M.PANELS:
            record = M.panel_record(self.e, nodes)
            self.assertEqual(len(record["block_row"]), 3)

    def test_row_sign_is_material(self):
        nodes = M.PANELS[1]
        a = self.e.source_matrix(nodes)
        b = self.e.source_matrix(nodes[1:])
        r = M.row_product(self.e, nodes)
        r[1] *= -1
        shifted = [
            [b[i][j] - (nodes[0] if i == j else 0) for j in range(3)] for i in range(3)
        ]
        self.assertNotEqual(self.e.mm([r], shifted)[0], a[0][1:])

    def test_row_is_complete_not_diagonal_only(self):
        nodes = M.PANELS[2]
        product = M.row_product(self.e, nodes)
        diagonal_only = [2 * y / (y - nodes[0]) for y in nodes[1:]]
        self.assertNotEqual(product[1:], diagonal_only[1:])

    def test_polynomial_functional_calculus_independent_control(self):
        for nodes in M.PANELS:
            record = M.panel_record(self.e, nodes)
            self.assertEqual(
                record["polynomial_control_matrix"],
                M.cubic(self.e, self.e.source_matrix(nodes)),
            )

    def test_literal_mixed_gram_and_derivative(self):
        record = M.panel_record(self.e, M.PANELS[0])
        self.assertEqual(record["literal_source_gram"][0][0], Q(1, 4))
        self.assertTrue(
            all(
                record["literal_source_gram"][i][j] == 0
                for i in range(4)
                for j in range(4)
                if i != j
            )
        )

    def test_factor_two_counterfeit(self):
        nodes = M.PANELS[0]
        functions = self.e.source_functions(nodes)
        bad = self.e.source_matrix(nodes)
        bad[0][1] /= 2
        self.assertNotEqual(
            self.e.derivative_minus(functions[1]),
            self.e.combine(functions, [row[1] for row in bad]),
        )

    def test_confluent_newton_residual(self):
        record = M.panel_record(self.e, M.PANELS[0])
        expected = Q(1, 2 * M.R)
        for node in M.PANELS[0][:-1]:
            expected /= (node + M.R) ** 2
        self.assertEqual(record["cauchy_newton_residual"], expected)
        self.assertEqual(record["xi_residual_proved_lower_bound"], expected / 100)

    def test_exact_endpoint_and_cross_constants(self):
        constants = M.constants(self.e)
        self.assertGreater(constants["exp_log10_lower"], 10)
        self.assertGreater(constants["exp_log4pi_lower"], Q(88, 7))
        self.assertEqual(constants["low_F_lower"], Q(3, 200))
        self.assertLess(constants["cross_row_upper"], Q(1, 16))
        self.assertGreater(constants["positive_block_schur_margin"], 0)

    def test_weaker_taylor_counterfeit_does_not_certify(self):
        self.assertLess(M.taylor_lower(self.e, Q(127, 50), 4), Q(88, 7))

    def test_declared_domain_and_dimension_caps(self):
        for nodes in (
            (Q(49, 100), M.R),
            (257, M.R),
            (1, M.R - 1),
            (1,),
            (1, M.R, M.R, M.R, M.R),
        ):
            with self.subTest(nodes=nodes), self.assertRaises(ValueError):
                M.checked(self.e, nodes)

    def test_source_authentication_precedes_compilation(self):
        with (
            patch.object(M, "frozen", side_effect=ValueError("changed source")),
            patch("builtins.compile", side_effect=RuntimeError("must not compile")),
            self.assertRaisesRegex(ValueError, "changed source"),
        ):
            M.load_source()

    def test_changed_frozen_blob_refused(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=b"changed"),
            self.assertRaisesRegex(ValueError, "blob mismatch"),
        ):
            M.frozen(M.FREEZE, M.PINS[0][1], "0" * 40)


class MixedAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record, cls.e = M.build()

    def test_complete_scope_and_source_chain(self):
        self.assertEqual(len(self.record["sources"]), 6)
        self.assertEqual(len(self.record["panels"]), 3)
        self.assertFalse(self.record["scope"]["xi_values_sampled"])
        self.assertEqual(self.record["scope"]["two_low_nodes"], "OUTSIDE_THEOREM")

    def test_typed_fresh_comparison_rejects_numeric_alias(self):
        bad = copy.deepcopy(self.record)
        bad["constants"]["high_minimum"] = True
        body = {key: value for key, value in bad.items() if key != "proof_sha256"}
        bad["proof_sha256"] = hashlib.sha256(M.canonical(body).encode()).hexdigest()
        with self.assertRaisesRegex(ValueError, "fresh typed"):
            M.accept(bad, self.record)

    def test_body_digest_rejected(self):
        bad = copy.deepcopy(self.record)
        bad["scope"]["rh"] = "PROVED"
        with self.assertRaisesRegex(ValueError, "body digest"):
            M.accept(bad, self.record)

    def test_strict_json_duplicate_float_nonfinite(self):
        for raw in ('{"x":1,"x":1}', '{"x":1.0}', '{"x":NaN}', '{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                self.e.strict_load(raw)
        self.assertEqual(self.e.strict_load('{"x":[1,true]}'), {"x": [1, True]})

    def test_fixture_matches_full_fresh_reconstruction(self):
        candidate = self.e.strict_load(M.ARTIFACT.read_text(encoding="utf-8"))
        M.accept(candidate, self.record)


if __name__ == "__main__":
    unittest.main()
