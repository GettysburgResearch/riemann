"""Exact source and hostile-record controls for the two-cluster theorem."""

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
    / "research/riemann-structures/native-five-hour-pass/architecture-e/two_cluster_replay.py"
)
SPEC = importlib.util.spec_from_file_location("architecture_e_two_cluster", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class TwoClusterSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e, cls.sources, cls.mixed_proof = M.load_source()

    def test_complete_sylvester_similarity_all_panels(self):
        for nodes in M.PANELS:
            record = M.panel_record(self.e, nodes)
            self.assertEqual(len(record["sylvester_solution"]), 2)

    def test_sylvester_sign_is_material(self):
        nodes = M.PANELS[1]
        l, b, v, s = M.sylvester(self.e, nodes[:2], nodes[2:])
        s[0][0] *= -1
        residual = [
            [self.e.mm(s, b)[i][j] - self.e.mm(l, s)[i][j] for j in range(2)]
            for i in range(2)
        ]
        self.assertNotEqual(residual, v)

    def test_complete_coupling_not_one_row(self):
        nodes = M.PANELS[2]
        l, b, v, s = M.sylvester(self.e, nodes[:2], nodes[2:])
        v[1] = [Q(0), Q(0)]
        residual = [
            [self.e.mm(s, b)[i][j] - self.e.mm(l, s)[i][j] for j in range(2)]
            for i in range(2)
        ]
        self.assertNotEqual(residual, v)

    def test_polynomial_block_calculus(self):
        for nodes in M.PANELS:
            record = M.panel_record(self.e, nodes)
            self.assertEqual(
                record["polynomial_control"],
                M.cubic(self.e, self.e.source_matrix(nodes)),
            )

    def test_literal_original_source_and_gram(self):
        record = M.panel_record(self.e, M.PANELS[0])
        self.assertEqual(record["literal_source_gram"][0][0], 16)
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
        bad[1][2] /= 2
        self.assertNotEqual(
            self.e.derivative_minus(functions[2]),
            self.e.combine(functions, [row[2] for row in bad]),
        )

    def test_newton_residual_and_relative_factor(self):
        record = M.panel_record(self.e, M.PANELS[0])
        self.assertEqual(
            record["xi_residual_proved_lower_bound"],
            record["cauchy_newton_residual"] / 50,
        )

    def test_exact_source_bounds_and_schur(self):
        c = M.constants(self.e)
        self.assertEqual(c["prime_remainder_majorant"], Q(1, 3584))
        self.assertEqual(c["moderate_real_F_margin"], Q(217, 1500))
        self.assertLess(c["cross_numerator"] / 2**20, Q(1, 64))
        self.assertGreater(c["positive_schur_margin"], 0)

    def test_singular_sylvester_system_refused(self):
        with self.assertRaisesRegex(ValueError, "singular"):
            M.solve([[1, 1], [2, 2]], [1, 2])

    def test_declared_cluster_domain(self):
        for low, high in (
            ((31, 32), (M.R, M.R)),
            ((32, 257), (M.R, M.R)),
            ((32, 32), (M.R - 1, M.R)),
            ((32,), (M.R, M.R)),
        ):
            with self.subTest(low=low, high=high), self.assertRaises(ValueError):
                M.sylvester(self.e, low, high)

    def test_authentication_precedes_compilation(self):
        with (
            patch.object(M, "frozen", side_effect=ValueError("changed dependency")),
            patch("builtins.compile", side_effect=RuntimeError("must not compile")),
            self.assertRaisesRegex(ValueError, "changed dependency"),
        ):
            M.load_source()

    def test_changed_dependency_blob_refused(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=b"changed"),
            self.assertRaisesRegex(ValueError, "blob mismatch"),
        ):
            M.frozen(M.PINS[0][0], "0" * 40)


class TwoClusterAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record, cls.e = M.build()

    def test_complete_scope_and_predecessor(self):
        self.assertEqual(len(self.record["sources"]), 5)
        self.assertEqual(len(self.record["panels"]), 3)
        self.assertEqual(self.record["scope"]["moderate_third_node"], "OUTSIDE_THEOREM")
        self.assertFalse(self.record["scope"]["xi_values_sampled"])

    def test_numeric_alias_refused(self):
        bad = copy.deepcopy(self.record)
        bad["constants"]["high_minimum"] = True
        body = {key: value for key, value in bad.items() if key != "proof_sha256"}
        bad["proof_sha256"] = hashlib.sha256(M.canonical(body).encode()).hexdigest()
        with self.assertRaisesRegex(ValueError, "fresh typed"):
            M.accept(bad, self.record)

    def test_changed_body_digest_refused(self):
        bad = copy.deepcopy(self.record)
        bad["scope"]["rh"] = "PROVED"
        with self.assertRaisesRegex(ValueError, "body digest"):
            M.accept(bad, self.record)

    def test_strict_json_refuses_alias_tokens_and_duplicates(self):
        for raw in ('{"x":1,"x":1}', '{"x":1.0}', '{"x":NaN}', '{"x":Infinity}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError):
                self.e.strict_load(raw)
        self.assertEqual(self.e.strict_load('{"x":[1,true]}'), {"x": [1, True]})

    def test_fixture_is_full_fresh_reconstruction(self):
        candidate = self.e.strict_load(M.ARTIFACT.read_text(encoding="utf-8"))
        M.accept(candidate, self.record)


if __name__ == "__main__":
    unittest.main()
