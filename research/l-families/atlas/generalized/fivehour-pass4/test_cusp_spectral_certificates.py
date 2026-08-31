"""Finite algebra, primitive-formula and strict-checker controls."""

import copy
import json
import unittest
from pathlib import Path

from flint import arb, ctx

import cusp_spectral_certificates as c


class CuspCertificateTests(unittest.TestCase):
    def setUp(self):
        self.old = ctx.prec
        ctx.prec = 256

    def tearDown(self):
        ctx.prec = self.old

    def test_constants_and_uniform_fourier_tail(self):
        v = c.constants()
        self.assertTrue(v["a0"] > arb(4) / 5)
        self.assertTrue(v["r0"] < arb(1) / 100)
        self.assertTrue(v["c0"] < 0)

    def test_gaussian_gamma_identity(self):
        for shape in (1, 2, 3, 16, 96):
            for argument in (arb(1) / 3, arb(shape), arb(2 * shape)):
                self.assertTrue(c.gamma_q(shape, argument).overlaps(c.gamma_q_finite_sum(shape, argument)))

    def test_gamma_recurrence(self):
        for shape in (2, 17, 95):
            x = arb(shape) / 2
            lhs = c.gamma_q(shape + 1, x) - c.gamma_q(shape, x)
            rhs = (-x).exp() * x**shape / arb(shape + 1).gamma()
            self.assertTrue(lhs.overlaps(rhs))

    def test_directed_integer_selection(self):
        self.assertEqual(c.exact_floor(arb("3.25 +/- 0.01")), 3)
        self.assertEqual(c.exact_ceil(arb("3.25 +/- 0.01")), 4)
        self.assertIsNone(c.exact_floor(arb("3 +/- 0.01")))

    def test_roundtrip_balls_contain_source(self):
        for x in (arb.pi(), arb(1) / 3, arb("-7 +/- 0.001")):
            self.assertTrue(c.unpack(c.pack(x)).contains(x))

    def test_operator_panel_is_declared_and_bounded(self):
        self.assertEqual(c.operator_indices(96), [1, 2, 4])
        row = c.operator_cell(384, 2)
        self.assertEqual(row["lower_status"], "CERTIFIED_ANALYTIC_BOUND")
        self.assertTrue(c.unpack(row["lower_eigenvalue"]) < c.unpack(row["upper_eigenvalue"]))

    def test_source_signs_for_all_declared_epsilons(self):
        for denominator in c.EPS_DENOMINATORS:
            epsilon = arb(1) / denominator
            self.assertTrue(c.completed_zeta(2 - 2 * epsilon) > 0)
            self.assertTrue(c.completed_zeta(1 - 2 * epsilon) < 0)

    def test_work_and_type_caps(self):
        for args in ((True, 1), (2, 1), (100001, 1), (96, 0), (96, 10001)):
            with self.assertRaises(ValueError):
                c.gram_delta(*args)
        with self.assertRaises(ValueError):
            c.build_report(53)
        with self.assertRaises(ValueError):
            c.period_cell(1000, 16, 4)

    def test_mutation_rejection_is_full_structure(self):
        expected = {"source": {"sha": "abc"}, "cells": [{"k": 96, "status": "UNRESOLVED"}]}
        c.validate_against(copy.deepcopy(expected), expected)
        mutants = []
        x = copy.deepcopy(expected); x["cells"][0]["status"] = "CERTIFIED"; mutants.append(x)
        x = copy.deepcopy(expected); x["cells"] = []; mutants.append(x)
        x = copy.deepcopy(expected); x["source"]["sha"] = "resealed"; mutants.append(x)
        x = copy.deepcopy(expected); x["extra"] = True; mutants.append(x)
        for mutant in mutants:
            with self.assertRaises(ValueError):
                c.validate_against(mutant, expected)

        bool_mutant = copy.deepcopy(expected)
        bool_mutant["cells"][0]["k"] = True
        with self.assertRaises(ValueError):
            c.validate_against(bool_mutant, expected)

    def test_strict_json_guards(self):
        bad = (
            b'{"a":1,"a":2}', b'{"a":1.0}', b'{"a":NaN}',
            json.dumps(2**4097).encode(), json.dumps("x" * 1001).encode(),
            b"[" * 25 + b"0" + b"]" * 25,
        )
        for raw in bad:
            with self.subTest(raw=raw[:20]), self.assertRaises(ValueError):
                c.strict_json(raw)

    def test_all_reported_gamma_values_have_finite_sum_control(self):
        for k in c.OPERATOR_WEIGHTS:
            for j in c.operator_indices(k):
                argument = 4 * arb.pi() * j
                self.assertTrue(
                    c.gamma_q(k, argument).overlaps(
                        c.gamma_q_finite_sum(k, argument)
                    )
                )
        for k in c.PERIOD_WEIGHTS:
            for denominator in c.EPS_DENOMINATORS:
                for margin_denominator in c.MARGIN_DENOMINATORS:
                    row = c.period_cell(k, denominator, margin_denominator)
                    if "gamma_q" not in row:
                        continue
                    argument = (
                        4 * arb.pi() * row["jminus"] * c.unpack(row["height"])
                    )
                    self.assertTrue(
                        c.gamma_q(k - 1, argument).overlaps(
                            c.gamma_q_finite_sum(k - 1, argument)
                        )
                    )

    def test_512_bit_fixture_overlaps_256_bit_fixture(self):
        directory = Path(c.__file__).resolve().parent
        low = c.strict_json((directory / "cusp_certificates_256.json").read_bytes())
        high = c.strict_json((directory / "cusp_certificates_512.json").read_bytes())

        def collect(value):
            output = {}

            def visit(item, path=()):
                if type(item) is dict and set(item) == {"mid", "rad", "exp10"}:
                    output[path] = c.unpack(item)
                elif type(item) is dict:
                    for key, child in item.items():
                        visit(child, path + (key,))
                elif type(item) is list:
                    for index, child in enumerate(item):
                        visit(child, path + (index,))

            visit(value)
            return output

        low_balls, high_balls = collect(low), collect(high)
        self.assertEqual(low_balls.keys(), high_balls.keys())
        for path in low_balls:
            with self.subTest(path=path):
                # Separate Arb evaluations are not required to be nested;
                # directed overlap is the precision-replay acceptance rule.
                self.assertTrue(low_balls[path].overlaps(high_balls[path]))


if __name__ == "__main__":
    unittest.main()
