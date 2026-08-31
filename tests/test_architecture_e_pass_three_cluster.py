"""Exact controls for the three-moderate/one-high packet."""

import copy
import hashlib
import importlib.util
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/riemann-structures/native-five-hour-pass/architecture-e/three_cluster_replay.py"
)
S = importlib.util.spec_from_file_location("architecture_e_three_cluster", PATH)
M = importlib.util.module_from_spec(S)
S.loader.exec_module(M)


class SourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.e, cls.sources, cls.prior = M.load_source()

    def test_all_complete_panels(self):
        for nodes in M.PANELS:
            self.assertEqual(len(M.panel(self.e, nodes)["sylvester_column"]), 3)

    def test_wrong_column_sign(self):
        nodes = M.PANELS[1]
        l, v, r = M.column(self.e, nodes[:3], nodes[3])
        r[0] *= -1
        matrix = [
            [-l[i][j] + (nodes[3] if i == j else 0) for j in range(3)] for i in range(3)
        ]
        self.assertNotEqual(
            [sum(matrix[i][j] * r[j] for j in range(3)) for i in range(3)], v
        )

    def test_missing_coupling_row(self):
        nodes = M.PANELS[0]
        low, v, column = M.column(self.e, nodes[:3], nodes[3])
        matrix = [
            [-low[i][j] + (nodes[3] if i == j else 0) for j in range(3)]
            for i in range(3)
        ]
        residual = [sum(matrix[i][j] * column[j] for j in range(3)) for i in range(3)]
        counterfeit = v[:]
        counterfeit[-1] = 0
        self.assertNotEqual(residual, counterfeit)

    def test_polynomial_calculus(self):
        for nodes in M.PANELS:
            self.assertEqual(
                M.panel(self.e, nodes)["polynomial_control"],
                M.cubic(self.e, self.e.source_matrix(nodes)),
            )

    def test_literal_gram(self):
        g = M.panel(self.e, M.PANELS[0])["literal_source_gram"]
        self.assertEqual(g[0][0], 32)
        self.assertTrue(all(g[i][j] == 0 for i in range(4) for j in range(4) if i != j))

    def test_factor_two_counterfeit(self):
        nodes = M.PANELS[0]
        f = self.e.source_functions(nodes)
        a = self.e.source_matrix(nodes)
        a[1][3] /= 2
        self.assertNotEqual(
            self.e.derivative_minus(f[3]), self.e.combine(f, [row[3] for row in a])
        )

    def test_residual_factor(self):
        r = M.panel(self.e, M.PANELS[2])
        self.assertEqual(
            r["xi_residual_proved_lower_bound"], r["cauchy_newton_residual"] / 200
        )

    def test_constants(self):
        c = M.constants(self.e)
        self.assertGreater(c["moderate_real_F_margin_lower"], Q(1, 200))
        self.assertLess(c["cross_norm_majorant"], Q(7, 200))

    def test_singular_solve(self):
        with self.assertRaises(ValueError):
            M.solve([[1, 1], [2, 2]], [1, 2])

    def test_domain_caps(self):
        for low, y in (
            ((63, 64, 64), M.R),
            ((64, 64, 257), M.R),
            ((64, 64), M.R),
            ((64, 64, 64), M.R - 1),
        ):
            with self.subTest(low=low, y=y), self.assertRaises(ValueError):
                M.column(self.e, low, y)

    def test_auth_before_compile(self):
        with (
            patch.object(M, "frozen", side_effect=ValueError("changed")),
            patch("builtins.compile", side_effect=RuntimeError),
            self.assertRaisesRegex(ValueError, "changed"),
        ):
            M.load_source()

    def test_changed_blob(self):
        with (
            patch.object(M.subprocess, "check_output", return_value=b"changed"),
            self.assertRaises(ValueError),
        ):
            M.frozen(M.PINS[0][0], "0" * 40)


class AcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record, cls.e = M.build()

    def test_scope(self):
        self.assertEqual(len(self.record["panels"]), 3)
        self.assertFalse(self.record["scope"]["xi_values_sampled"])

    def test_typed_alias(self):
        bad = copy.deepcopy(self.record)
        bad["constants"]["high_minimum"] = True
        body = {k: v for k, v in bad.items() if k != "proof_sha256"}
        bad["proof_sha256"] = hashlib.sha256(M.canonical(body).encode()).hexdigest()
        with self.assertRaisesRegex(ValueError, "fresh typed"):
            M.accept(bad, self.record)

    def test_body_digest(self):
        bad = copy.deepcopy(self.record)
        bad["scope"]["rh"] = "PROVED"
        with self.assertRaisesRegex(ValueError, "body digest"):
            M.accept(bad, self.record)

    def test_strict_json(self):
        for raw in ('{"x":1,"x":1}', '{"x":1.0}', '{"x":NaN}'):
            with self.assertRaises(ValueError):
                self.e.strict_load(raw)

    def test_fixture(self):
        M.accept(self.e.strict_load(M.ARTIFACT.read_text()), self.record)


if __name__ == "__main__":
    unittest.main()
