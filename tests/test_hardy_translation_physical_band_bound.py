"""Hostile exact replay controls; the analytic proofs remain in the note."""

import ast
import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/exploratory/hardy_translation_physical_band_bound.py"
SPEC = importlib.util.spec_from_file_location("hardy_translation_packet", PATH)
M = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = M
SPEC.loader.exec_module(M)


class HardyTranslationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_gaussian_hand_arithmetic(self):
        a, b = M.Q(F(1), F(2)), M.Q(F(3), F(-1))
        self.assertEqual(a * b, M.Q(F(5), F(5)))
        self.assertEqual(a / b, M.Q(F(1, 10), F(7, 10)))
        self.assertEqual(a**0, M.ONE)
        self.assertEqual(a.conjugate(), M.Q(F(1), F(-2)))

    def test_gaussian_raw_types(self):
        for bad in (True, 1.0, 1j, "1", None):
            with self.subTest(bad=bad), self.assertRaises(TypeError):
                M.gaussian(bad)
        with self.assertRaises(TypeError):
            M.Q(1, F(0))
        with self.assertRaises(ValueError):
            M.Q(F(2**M.INTERMEDIATE_BITS))

    def test_division_and_power_guards(self):
        with self.assertRaises(ZeroDivisionError):
            M.ONE / M.ZERO
        for bad in (True, -1, 14, F(2), 2.0):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                M.ONE**bad

    def test_pole_types_heights_and_caps(self):
        for bad in ((), ((0, 0),), ((-1, 2),), ((True, 0),), ((1.0, 0),)):
            with self.subTest(bad=bad), self.assertRaises((ValueError, TypeError)):
                M.poles(bad)
        for pair in ((1,), (1, 2, 3), "xy", (1, 1j), (2**16, 0)):
            with self.subTest(pair=pair), self.assertRaises((ValueError, TypeError)):
                M.poles((pair,))
        self.assertEqual(M.poles((), allow_empty=True), ())
        with self.assertRaises(TypeError):
            M.poles((), allow_empty=1)
        with self.assertRaises(ValueError):
            M.poles(((1, 0),) * 7)

    def test_total_degree_guard_before_algebra(self):
        with (
            patch.object(M, "gram", side_effect=AssertionError("allocated")),
            self.assertRaises(ValueError),
        ):
            M.physical_control(((1, 0),) * 6, ((1, 0),))
        with self.assertRaises(ValueError):
            M.physical_control((), ((1, 0),))
        with self.assertRaises(TypeError):
            M.physical_control(iter(((1, 0),)), ())

    def test_basis_guards_before_factorials(self):
        z = M.gaussian(1)
        for bad in ((), ((z, True),), ((z, 10**9),), ((z, 2),), ((z, 1),) * 2):
            with (
                self.subTest(bad=bad),
                patch.object(
                    M.math, "factorial", side_effect=AssertionError("factorial reached")
                ),
                self.assertRaises((ValueError, TypeError)),
            ):
                M.gram(bad)
        with self.assertRaises(ValueError):
            M.generator(((M.gaussian(0), 1),))

    def test_simple_gram(self):
        r = M.translation_control(M.poles(((F(3, 2), 9),)))
        self.assertEqual(r["G"], M.matrix(((F(1, 3),),)))
        self.assertEqual(r["origin_kernel"], M.gaussian(3))

    def test_complex_gram_conjugation(self):
        b = M.basis_from_poles(M.poles(((1, 0), (2, 3))))
        g = M.gram(b)
        self.assertEqual(g[0][1], M.Q(F(1, 6), F(-1, 6)))
        self.assertEqual(g[1][0], g[0][1].conjugate())
        self.assertEqual(g, M.adjoint(g))

    def test_confluent_gram_and_phase_safe_generator(self):
        r = M.translation_control(M.poles(((1, 3),) * 2))
        self.assertEqual(r["G"], M.matrix(((F(1, 2), F(1, 4)), (F(1, 4), F(1, 4)))))
        self.assertEqual(r["A"][0][1], M.ONE)
        self.assertEqual(r["A"][0][0], M.Q(F(-1), F(-3)))
        self.assertEqual(M.inv(r["G"]), M.matrix(((4, -4), (-4, 8))))

    def test_permuted_basis_keeps_native_identity(self):
        b = tuple(reversed(M.basis_from_poles(M.poles(((1, 2), (1, 2), (3, 0))))))
        g, a = M.gram(b), M.generator(b)
        c = (tuple(M.ONE if r == 1 else M.ZERO for _, r in b),)
        self.assertEqual(
            M.ma(M.mm(M.adjoint(a), g), M.mm(g, a)),
            M.ms(M.mm(M.adjoint(c), c), -1),
        )

    def test_near_collision_and_wide_phase_controls(self):
        for raw in (((1, 0), (F(32768, 32767), 0)), ((F(1, 7), -32767), (8, 32767))):
            result = M.translation_control(M.poles(raw))
            self.assertTrue(result["both_Lyapunov_identities_exact"])
            self.assertTrue(all(x > 0 for x in result["positive_LDL_pivots"]))

    def test_predeclared_physical_cases(self):
        for den, num in M.CASES:
            with self.subTest(den=den, num=num):
                r = M.physical_control(den, num)
                self.assertTrue(r["J_star_G_product_J_equals_G_denominator"])
                self.assertEqual(r["rational_identity_columns_checked"], len(den))

    def test_heldout_maximum_degree_and_collision(self):
        r = M.physical_control(((1, 0),) * 3, ((1, 0), (2, 3), (2, -3)))
        self.assertEqual(r["d_product"], 6)
        self.assertEqual(r["translation"]["integrated_kernel"], 6)

    def test_zero_numerator_gives_identity_inclusion(self):
        r = M.physical_control(((1, 2), (1, 2), (3, -1)), ())
        self.assertEqual(r["physical_inclusion_matrix"], M.eye(3))

    def test_collision_partial_fraction_hand_control(self):
        z = M.gaussian(1)
        image = M.multiply_inner({(z, 1): M.ONE}, z)
        self.assertEqual(image, {(z, 1): M.ONE, (z, 2): M.gaussian(-2)})

    def test_distinct_partial_fraction_hand_control(self):
        z, c = M.gaussian(1), M.gaussian(2)
        image = M.multiply_inner({(z, 2): M.ONE}, c)
        self.assertEqual(
            image,
            {(z, 2): M.gaussian(-3), (z, 1): M.gaussian(4), (c, 1): M.gaussian(-4)},
        )

    def test_isometry_tamper_is_detected(self):
        with (
            patch.object(
                M, "multiply_inner", return_value={(M.gaussian(1), 1): M.gaussian(2)}
            ),
            self.assertRaises(ArithmeticError),
        ):
            M.physical_control(((1, 0),), ((1, 0),))

    def test_polynomial_exact_division(self):
        a, b = M.poly((1, 2, 1)), M.poly((1, 1))
        self.assertEqual(M.divide_monic(a, b), b)
        self.assertEqual(M.pm(b, b), a)
        with self.assertRaises(ValueError):
            M.divide_monic((1, 0, 1), b)
        with self.assertRaises(ValueError):
            M.divide_monic(a, (1, 2))

    def test_polynomial_raw_trailing_type_and_size_guards(self):
        for bad in ((1, False), (1, 0.0), (), (1,) * 14):
            with self.subTest(bad=bad), self.assertRaises((TypeError, ValueError)):
                M.poly(bad)
        with self.assertRaises(ValueError):
            M.pm((1,) * 13, (1, 1))

    def test_matrix_guards_and_positive_definiteness(self):
        for bad in ((), ((1, 2), (3,)), ((True,),), ((1.0,),)):
            with self.subTest(bad=bad), self.assertRaises((TypeError, ValueError)):
                M.matrix(bad)
        for bad in (((1, 1), (1, 1)), ((-1,),), ((1, 2), (0, 1))):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                M.hpd_pivots(bad)
        with self.assertRaises(ValueError):
            M.inv(((1, 1), (1, 1)))
        with self.assertRaises(ValueError):
            M.mm(((1, 2),), ((1, 2),))

    def test_band_factor_and_guards(self):
        self.assertEqual(M.band_factor(3, 10, 11)["trace_bound"], F(3, 11))
        self.assertEqual(M.band_factor(6, 1, 2)["unit_vector_bound"], 1)
        for args in (
            (True, 1, 2),
            (0, 1, 2),
            (7, 1, 2),
            (1, 0, 2),
            (1, 2, 2),
            (1, 2, 1),
            (1, 1.0, 2),
        ):
            with self.subTest(args=args), self.assertRaises((ValueError, TypeError)):
                M.band_factor(*args)

    def test_exact_complex_source_covariance(self):
        r = M.source_covariance_control()
        self.assertEqual(r["literal_and_reduced_trace"], M.gaussian(F(41, 8)))
        self.assertNotEqual(
            r["incorrect_dropped_outer_trace"], r["literal_and_reduced_trace"]
        )
        self.assertTrue(r["C_V_commute_but_neither_commutes_G_or_H"])
        self.assertTrue(r["H_is_abstract_positive_weight_not_claimed_actual_Xi_band"])

    def test_nonmonotone_and_delay_scope_countercontrols(self):
        r = M.countercontrols()
        self.assertEqual(r["zero_at_t_half"], 0)
        self.assertEqual(r["square_coefficient_at_t_one_before_exp_minus_two"], 2)
        self.assertEqual(r["denominator_rank_and_height"], (1, 1))
        self.assertTrue(r["finite_degree_needed_not_actual_Xi_example"])

    def test_complete_source_authentication(self):
        auth = M.authenticate_sources()
        self.assertEqual(auth["source_count"], 13)
        self.assertFalse(auth["remote_bytes_authenticated"])

    def test_manifest_contract_mutations_rejected_before_git(self):
        base = M.expected_manifest()
        candidates = []
        for field, value in (("authoring_base", "0" * 40), ("extra", True)):
            r = copy.deepcopy(base)
            r[field] = value
            candidates.append(r)
        r = copy.deepcopy(base)
        r["external_contracts"][0]["remote_bytes_authenticated"] = 0
        candidates.append(r)
        r = copy.deepcopy(base)
        r["sources"][0]["git_blob"] = "0" * 40
        candidates.append(r)
        with patch.object(
            M.subprocess, "check_output", side_effect=AssertionError("git reached")
        ):
            for r in candidates:
                with self.subTest(r=r), self.assertRaises(ValueError):
                    M.authenticate_sources(r)

    def test_source_blob_tamper_rejected(self):
        with (
            patch.object(
                M.subprocess, "check_output", side_effect=[b"0" * 40, b"wrong"]
            ),
            self.assertRaises(ValueError),
        ):
            M.authenticate_sources(M.expected_manifest())

    def test_lf_hash_and_canonical_json_invariance(self):
        self.assertEqual(M.sha256_lf(b"a\r\nb\r\n"), M.sha256_lf(b"a\nb\n"))
        a, b = {"z": False, "a": 1}, {"a": 1, "z": False}
        self.assertEqual(M.canonical(a), M.canonical(b))
        self.assertNotEqual(M.canonical(a), M.canonical({"a": True, "z": 0}))

    def test_strict_json_rejects_duplicates_and_nonfinite(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "input.json"
            for raw in (
                '{"x":1,"x":2}',
                '{"x":NaN}',
                '{"x":Infinity}',
                '{"x":-Infinity}',
            ):
                path.write_text(raw, encoding="utf-8")
                with self.subTest(raw=raw), self.assertRaises(ValueError):
                    M.read_json(path)

    def test_fixture_exact_rebuild_and_artifacts(self):
        self.assertEqual(M.canonical(M.read_json(M.FIXTURE)), M.canonical(self.report))
        self.assertEqual(len(self.report["artifact_sha256_lf"]), 4)
        self.assertEqual(self.report["arithmetic_class"], "EXACT_RATIONAL")

    def test_report_mutations_cannot_hide_in_python_numeric_equality(self):
        candidates = []
        for field, value in (
            ("predeclared_native_cases", 5.0),
            ("unbounded_search", 0),
            ("rational_identity_columns", 9),
        ):
            r = copy.deepcopy(self.report)
            r["coverage"][field] = value
            candidates.append(r)
        r = copy.deepcopy(self.report)
        r["scope"]["actual_Xi_degree_bound_proved"] = True
        candidates.append(r)
        r = copy.deepcopy(self.report)
        r["native_controls"][0]["translation"]["G"][0][0]["re"] = "2/4"
        candidates.append(r)
        with patch.object(M, "build_report", return_value=self.report):
            for r in candidates:
                with self.subTest(r=r), self.assertRaises(ValueError):
                    M.validate_report(r)

    def test_report_coverage_and_boundaries(self):
        self.assertEqual(self.report["coverage"]["predeclared_native_cases"], 5)
        self.assertEqual(self.report["coverage"]["rational_identity_columns"], 10)
        self.assertEqual(self.report["coverage"]["band_rows"], 18)
        for field in (
            "actual_Xi_degree_bound_proved",
            "height_sum_used_as_degree_bound",
            "infinite_inner_approximation_error_controlled",
            "outer_or_inner_commuted_with_projection",
            "total_free_energy_bound",
            "topological_index_removed",
            "analytic_proof_formally_machine_verified",
            "novelty_claim",
            "RH_or_critical_line_percentage",
        ):
            self.assertIs(self.report["scope"][field], False)
        self.assertEqual(self.report["scope"]["physical_cutoff"], "m+n=o(X^2*exp(X))")

    def test_no_optimized_away_result_predicates(self):
        tree = ast.parse(PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertNotIn("float(", PATH.read_text(encoding="utf-8"))

    def test_json_serialization_retains_exact_complex_pairs(self):
        q = M.Q(F(2, 3), F(-4, 7))
        self.assertEqual(
            json.loads(M.canonical(M.serialize(q))), {"re": "2/3", "im": "-4/7"}
        )


if __name__ == "__main__":
    unittest.main()
