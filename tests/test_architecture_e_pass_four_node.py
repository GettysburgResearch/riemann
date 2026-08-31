"""Independent exact controls; finite checks do not prove an all-node theorem."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = (
    ROOT
    / "research/riemann-structures/native-five-hour-pass/architecture-e/four_node_replay.py"
)
SPEC = importlib.util.spec_from_file_location("architecture_e_four_node", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


class SourceAlgebra(unittest.TestCase):
    def test_literal_time_basis_and_derivative(self):
        for nodes in M.PANELS:
            record = M.panel_record(nodes)
            self.assertEqual(len(record["literal_source_functions"]), 4)

    def test_factor_two_counterfeit(self):
        nodes = tuple(map(Q, (256, 257, 300, 1024)))
        f = M.source_functions(nodes)
        bad = M.source_matrix(nodes)
        bad[0][1] /= 2
        self.assertNotEqual(
            M.derivative_minus(f[1]), M.combine(f, [row[1] for row in bad])
        )

    def test_resolvent_product_both_sides(self):
        nodes = tuple(map(Q, (256, 256, 512, 512)))
        for shift in M.SHIFTS:
            a = M.source_matrix(nodes)
            for i in range(4):
                a[i][i] += shift
            r = M.resolvent_product(nodes, shift)
            self.assertEqual(M.mm(a, r), M.ident(4))
            self.assertEqual(M.mm(r, a), M.ident(4))

    def test_intermediate_product_sign_matters(self):
        nodes = tuple(map(Q, (256, 300, 512, 1024)))
        r = M.resolvent_product(nodes, Q(1, 2))
        bad = [row[:] for row in r]
        bad[0][2] = -bad[0][2]
        a = M.source_matrix(nodes)
        for i in range(4):
            a[i][i] += Q(1, 2)
        self.assertNotEqual(M.mm(a, bad), M.ident(4))

    def test_fully_confluent_gram_from_moments(self):
        for x in (Q(256), Q(512)):
            functions = M.newton_functions((x,) * 4)
            gram = [[M.inner(f, g) for g in functions] for f in functions]
            independent = [
                [
                    Q(
                        (-1) ** (i + j) * M.math.factorial(i + j),
                        M.math.factorial(i) * M.math.factorial(j),
                    )
                    / (2 * x) ** (i + j + 1)
                    for j in range(4)
                ]
                for i in range(4)
            ]
            self.assertEqual(gram, independent)
            pivot = M.det(gram) / M.det([row[:3] for row in gram[:3]])
            self.assertEqual(pivot / 4, 1 / (512 * x**7))

    def test_distinct_cauchy_newton_determinant(self):
        nodes = tuple(map(Q, (256, 257, 300, 1024)))
        c = [[1 / (x + y) for y in nodes] for x in nodes]
        v = Q(1)
        for j in range(4):
            for i in range(j):
                v *= nodes[j] - nodes[i]
        functions = M.newton_functions(nodes)
        gram = [[M.inner(f, g) for g in functions] for f in functions]
        self.assertEqual(M.det(c) / v**2, M.det(gram))

    def test_prime_power_owner_not_log_n(self):
        labels = dict(M.prime_power_labels())
        self.assertEqual([labels[n] for n in (2, 4, 8, 16, 32)], [2] * 5)
        self.assertEqual([labels[n] for n in (9, 27)], [3, 3])
        self.assertIsNone(labels[12])


class ConstantBounds(unittest.TestCase):
    def test_complete_rational_margin(self):
        c = M.constant_record()
        self.assertEqual(c["real_operator_margin_lower"], Q(293, 2048))
        self.assertGreater(c["real_operator_margin_lower"], Q(1, 8))
        self.assertEqual(
            c["claimed_kernel_relative_margin"], 2 * c["claimed_real_operator_margin"]
        )

    def test_gamma_path_majorant_all_dimensions(self):
        for n in range(1, 5):
            self.assertEqual(1 + 2 * sum(3**j for j in range(n - 1)), 3 ** (n - 1))

    def test_pi_positive_integral_exact_division(self):
        record = M.pi_integral_identity()
        reconstructed = M.poly_mul(record["quotient"], [Q(1), Q(0), Q(1)])
        reconstructed[0] -= 4
        target = [Q(0)] * 4 + [Q(1), Q(-4), Q(6), Q(-4), Q(1)]
        self.assertEqual(reconstructed, target)

    def test_taylor_upper_and_next_degree(self):
        low, upper = M.exp_upper(Q(7, 2), 16)
        low_next, upper_next = M.exp_upper(Q(7, 2), 17)
        self.assertLess(low, low_next)
        self.assertLess(low_next, upper_next)
        self.assertLess(upper_next, upper)
        self.assertLess(upper, 34)

    def test_resource_and_domain_refusals(self):
        for nodes in ((256,) * 5, (0,), (True,), (256.0,)):
            with self.assertRaises(ValueError):
                M.source_matrix(nodes)
        with self.assertRaises(ValueError):
            M.rational(1 << 4096)
        with self.assertRaises(ValueError):
            M.resolvent_product((256,), Q(-256))
        with self.assertRaises(ValueError):
            M.exp_upper(Q(5), 2)


class Acceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fresh = M.build()

    @classmethod
    def tearDownClass(cls):
        del cls.fresh

    def test_fresh_roundtrip_and_current_artifact(self):
        M.accept(M.strict_load(json.dumps(self.fresh)), self.fresh)
        if M.ARTIFACT.exists():
            M.accept(M.strict_load(M.ARTIFACT.read_text(encoding="utf-8")), self.fresh)

    def test_owned_or_scope_counterfeit(self):
        for key in ("owned_sources", "scope"):
            bad = copy.deepcopy(self.fresh)
            bad[key] = {}
            with self.assertRaises(ValueError):
                M.accept(bad, self.fresh)

    def test_resealed_constant_counterfeit(self):
        bad = copy.deepcopy(self.fresh)
        bad["constants"]["claimed_kernel_relative_margin"] = [1, 2]
        body = {key: value for key, value in bad.items() if key != "proof_sha256"}
        bad["proof_sha256"] = M.hashlib.sha256(M.canonical(body).encode()).hexdigest()
        with self.assertRaises(ValueError):
            M.accept(bad, self.fresh)

    def test_source_blob_tampering(self):
        changed = list(M.PINS)
        commit, path, _ = changed[0]
        changed[0] = commit, path, "0" * 40
        with patch.object(M, "PINS", tuple(changed)), self.assertRaises(ValueError):
            M.authenticated_sources()

    def test_strict_numeric_and_duplicate_json(self):
        for raw in ('{"a":1,"a":2}', '{"a":1.0}', '{"a":NaN}', '{"a":Infinity}'):
            with self.assertRaises(ValueError):
                M.strict_load(raw)
        for raw in ([True, 1], [1, True], [2, 4], [1, 0], [1.0, 1]):
            with self.assertRaises(ValueError):
                M.decode_fraction(raw)
        bad = copy.deepcopy(self.fresh)
        bad["constants"]["maximum_jet_dimension"] = True
        with self.assertRaises(ValueError):
            M.accept(bad, self.fresh)


if __name__ == "__main__":
    unittest.main()
