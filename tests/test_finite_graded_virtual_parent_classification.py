"""Exact finite controls and hostile boundaries for graded virtual parents."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = (
    ROOT
    / "research/l-families/atlas/generalized/finite_graded_virtual_parent_classification.py"
)
SPEC = importlib.util.spec_from_file_location("graded_parent_tested", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load finite-graded producer")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class FiniteGradedVirtualParentTests(unittest.TestCase):
    def test_small_numerators_and_constructive_chambers(self):
        controls = {
            (1, 0): [1],
            (1, 5): [1],
            (5, 0): [1],
            (5, 1): [1],
            (2, 2): [1, 1],
            (2, 3): [1, 4, 1],
            (2, 4): [1, 11, 11, 1],
            (3, 2): [1, 4, 1],
            (3, 3): [1, 20, 48, 20, 1],
        }
        for parameters, expected in controls.items():
            with self.subTest(parameters=parameters):
                report = module.differential_numerator(*parameters)
                self.assertEqual(report["numerator"], expected)
                self.assertEqual(
                    report["pole_order"], parameters[1] * (parameters[0] - 1) + 1
                )

    def test_interlacing_step_inequality_including_first_cycle(self):
        for n in range(2, 6):
            for k in range(2, 6):
                report = module.differential_numerator(n, k)
                steps = report["steps_d_j_m_newdegree_qminusm"]
                for index, (_, j, degree, new_degree, gap) in enumerate(steps):
                    if index < n - 1:
                        self.assertEqual((degree, new_degree, gap), (0, 0, 0))
                    else:
                        self.assertEqual(gap, n - j)
                        self.assertEqual(new_degree, degree + 1)

    def test_sturm_certifies_negative_and_simple(self):
        report = module.sturm_data((1, 20, 48, 20, 1))
        self.assertTrue(report["simple"])
        self.assertEqual(report["negative_roots"], 4)
        self.assertEqual(report["positive_roots"], 0)
        self.assertEqual(module.sturm_data((1,))["degree"], 0)

    def test_sturm_repeated_positive_and_nonreal_countercontrols(self):
        repeated = module.sturm_data((1, 2, 1))
        self.assertFalse(repeated["simple"])
        self.assertEqual(repeated["negative_roots"], 1)
        positive = module.sturm_data((1, -1))
        self.assertEqual(positive["positive_roots"], 1)
        nonreal = module.sturm_data((1, 0, 1))
        self.assertEqual(nonreal["negative_roots"], 0)
        self.assertEqual(nonreal["positive_roots"], 0)

    def test_polynomial_types_checked_before_zero_trim(self):
        for bad in (
            (1, False),
            (1, 0.0),
            (1, Fraction(0)),
            (0,),
            (),
            [1, 1],
            (1,) * 18,
            (1, 1 << 257),
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                module.sturm_data(bad)

    def test_exact_euler_dimensions_and_exceptional_zero_tail(self):
        exception = module.euler_transform(module.coefficients(2, 2, 16))
        self.assertEqual(exception["graded_dimensions"], [4, -1] + [0] * 14)
        expected = [
            8,
            -9,
            16,
            -45,
            144,
            -456,
            1440,
            -4680,
            15600,
            -52488,
            177840,
            -608160,
        ]
        self.assertEqual(
            module.euler_transform(module.coefficients(2, 3, 12))["graded_dimensions"],
            expected,
        )
        expected[0] = 9
        self.assertEqual(
            module.euler_transform(module.coefficients(3, 2, 12))["graded_dimensions"],
            expected,
        )

    def test_independent_triangular_and_product_controls(self):
        for n in range(1, 6):
            for k in range(6):
                values = module.coefficients(n, k, 16)
                weights = tuple(module.euler_transform(values)["graded_dimensions"])
                self.assertEqual(weights, module.triangular_weights(values))
                self.assertEqual(values, module.reconstruct_product(weights))

    def test_signed_integer_series_do_not_require_positive_weights(self):
        for values in ((1, -1, 0, 0, 0), (1, 0, -1, 0, 0), (1, 2, -3, 4, -5)):
            weights = tuple(module.euler_transform(values)["graded_dimensions"])
            self.assertEqual(module.reconstruct_product(weights), values)
            self.assertEqual(module.triangular_weights(values), weights)

    def test_series_and_weight_hostile_types_and_caps(self):
        for values in (
            (1, True, 0),
            (1, 1.0, 0),
            (1, Fraction(1), 0),
            (0, 1, 2),
            (1, 1),
            (1,) * 18,
            [1, 1, 1],
            (1, 1 << 257, 0),
        ):
            with self.subTest(values=values), self.assertRaises(ValueError):
                module.euler_transform(values)
        for weights in (
            (1, False),
            (1, 0.0),
            (1, Fraction(0)),
            (),
            (1,),
            (1,) * 17,
            (1, 1 << 257),
        ):
            with self.subTest(weights=weights), self.assertRaises(ValueError):
                module.reconstruct_product(weights)

    def test_mobius_values_and_guards(self):
        self.assertEqual(
            [module.mobius(i) for i in range(1, 17)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0],
        )
        for value in (True, 1.0, 0, 17):
            with self.assertRaises(ValueError):
                module.mobius(value)

    def test_direct_tensor_determinant_at_jordan_and_nonsquare_spectrum(self):
        jordan = module.rank_two_control(((1, 1), (0, 1)))
        self.assertEqual(jordan["tensor_determinant"], ["1", "-4", "6", "-4", "1"])
        self.assertEqual(jordan["graded_numerator"], ["1", "0", "-1"])
        self.assertEqual(
            jordan["coefficients_checked"],
            list(map(str, [1, 4, 9, 16, 25, 36, 49, 64, 81])),
        )
        nonsquare = module.rank_two_control(((2, 1), (1, 3)))
        self.assertEqual(nonsquare["determinant"], "5")
        self.assertEqual(nonsquare["graded_numerator"], ["1", "0", "-25"])

    def test_rational_and_rotation_matrix_controls(self):
        rotation = module.rank_two_control(((0, -1), (1, 0)))
        self.assertEqual(
            rotation["coefficients_checked"],
            list(map(str, [1, 0, 1, 0, 1, 0, 1, 0, 1])),
        )
        rational = module.rank_two_control(
            ((Fraction(1, 2), Fraction(1, 3)), (Fraction(-2, 3), Fraction(3, 2)))
        )
        self.assertEqual(rational["determinant"], "35/36")

    def test_matrix_shape_type_and_group_scope_guards(self):
        for value in (
            ((1, 0), (0, 0)),
            ((True, 0), (0, 1)),
            ((1.0, 0), (0, 1)),
            ((1, 0), (1,)),
            [[1, 0], [0, 1]],
            ((1 << 257, 0), (0, 1)),
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                module.rank_two_control(value)
        for value in ((), ((1,),) * 5, [[1]]):
            with self.assertRaises(ValueError):
                module.determinant_polynomial(value)

    def test_parameter_caps_precede_authentication(self):
        bound = module.work_bound(1, 0, 2)
        with mock.patch.object(
            module, "source_locks", side_effect=RuntimeError("must not authenticate")
        ):
            with self.assertRaisesRegex(ValueError, "exclusive work cap"):
                module.build_fixture(1, 0, 2, cap=bound)
            for parameters in (
                (True, 2, 4),
                (2, 2.0, 4),
                (6, 2, 4),
                (2, 6, 4),
                (2, 2, 17),
                (2, -1, 4),
            ):
                with self.assertRaises(ValueError):
                    module.build_fixture(*parameters)
        self.assertLess(module.work_bound(5, 5, 16), module.WORK_CAP)

    def test_source_manifest_authentication_and_lf_stability(self):
        locks = module.source_locks()
        self.assertEqual(len(locks["sources"]), 3)
        self.assertEqual(module.digest(b"a\r\nb\r"), module.digest(b"a\nb\n"))
        payload = json.loads(module.MANIFEST.read_text(encoding="utf-8"))
        payload["sources"][0]["git_blob"] = "0" * 40
        with self.assertRaises(ValueError):
            module.validate_manifest(payload)
        payload = json.loads(module.MANIFEST.read_text(encoding="utf-8"))
        payload["extra"] = True
        with self.assertRaises(ValueError):
            module.validate_manifest(payload)

    def test_source_authentication_precedes_prior_import(self):
        with (
            mock.patch.object(
                module, "source_locks", side_effect=ValueError("locked source changed")
            ),
            mock.patch.object(module, "_load_authenticated_prior") as imported,
        ):
            with self.assertRaisesRegex(ValueError, "locked source changed"):
                module.build_fixture(1, 0, 2)
            imported.assert_not_called()

    def test_typed_fixture_rejects_mutation(self):
        with self.assertRaises(ValueError):
            module.same_json({"count": True}, {"count": 1})
        expected = module.euler_transform(module.coefficients(2, 2, 4))
        bad = copy.deepcopy(expected)
        bad["graded_dimensions"][1] = 0
        with self.assertRaises(ValueError):
            module.same_json(bad, expected)

    def test_default_canonical_fixture_and_payload_hash(self):
        report = module.build_fixture()
        actual = json.loads(module.FIXTURE.read_text(encoding="utf-8"))
        module.same_json(actual, report)
        payload = dict(report)
        digest = payload.pop("payload_sha256")
        self.assertEqual(digest, hashlib.sha256(module.canonical(payload)).hexdigest())
        self.assertFalse(report["scope"]["analytic_global_convergence_or_RH_claim"])
        self.assertEqual(report["arithmetic_class"], "MIXED")

    def test_maximum_census_and_held_out_ranks(self):
        report = module.build_fixture(5, 5, 16)
        self.assertEqual(len(report["identity_rows"]), 30)
        held_out = next(
            row for row in report["identity_rows"] if (row["n"], row["k"]) == (5, 5)
        )
        self.assertEqual(held_out["sturm"]["negative_roots"], 16)
        self.assertTrue(held_out["sturm"]["simple"])
        self.assertLess(held_out["graded_dimensions"][1], 0)
        self.assertGreater(held_out["first_numerator_coefficient_minus_degree"], 0)

    def test_no_assert_or_float_proof_checks(self):
        syntax = ast.parse(PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(syntax)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(syntax)
            )
        )

    def test_cli_normal_and_optimized(self):
        for optimized in (False, True):
            command = (
                [sys.executable, "-B"]
                + (["-O"] if optimized else [])
                + [str(PATH), "--check"]
            )
            completed = subprocess.run(
                command,
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
                timeout=40,
            )
            self.assertIn(
                "PASS_FINITE_GRADED_VIRTUAL_PARENT_CLASSIFICATION", completed.stdout
            )


if __name__ == "__main__":
    unittest.main()
