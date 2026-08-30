"""Independent finite controls and strict replay boundaries for global parents."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import unittest
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "research/l-families/atlas/generalized/graded_parent_global_boundary.py"
SPEC = importlib.util.spec_from_file_location("global_parent_tested", PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load the global-boundary producer")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def independent_product(weights: tuple[int, ...], order: int) -> tuple[int, ...]:
    """Multiply the specified finite graded factors directly, with integer powers."""
    result = [1] + [0] * order
    for grade, weight in enumerate(weights, 1):
        factor = [0] * (order + 1)
        for j in range(order // grade + 1):
            if weight > 0:
                value = comb(weight + j - 1, j)
            else:
                value = (-1) ** j * comb(-weight, j) if j <= -weight else 0
            factor[grade * j] = value
        result = [
            sum(result[j] * factor[m - j] for j in range(m + 1))
            for m in range(order + 1)
        ]
    return tuple(result)


class GradedParentGlobalBoundaryTests(unittest.TestCase):
    def test_small_numerators(self):
        controls = {
            (1, 0): (1,),
            (1, 5): (1,),
            (5, 0): (1,),
            (5, 1): (1,),
            (2, 2): (1, 1),
            (2, 3): (1, 4, 1),
            (2, 4): (1, 11, 11, 1),
            (3, 2): (1, 4, 1),
            (3, 3): (1, 20, 48, 20, 1),
        }
        for pair, expected in controls.items():
            with self.subTest(pair=pair):
                data = module.numerator(*pair)
                self.assertEqual(data["H"], expected)
                self.assertEqual(data["tail"], (0,) * 5)

    def test_complete_maximal_rectangle_and_strengthened_equality(self):
        equalities = []
        count = 0
        for n in range(1, 6):
            for k in range(6):
                row = module.row_control(n, k, 32)
                self.assertEqual(len(row["formal_graded_dimensions"]), 32)
                if row["h1_minus_2q"] is not None:
                    count += 1
                    self.assertGreaterEqual(row["h1_minus_2q"], 0)
                    if row["h1_minus_2q"] == 0:
                        equalities.append((n, k))
        self.assertEqual(count, 15)
        self.assertEqual(equalities, [(2, 3), (3, 2)])

    def test_exception_products_by_direct_factor_multiplication(self):
        for n in range(1, 6):
            self.assertEqual(
                module.coefficients(n, 1, 32), independent_product((n,), 32)
            )
            self.assertEqual(
                module.coefficients(n, 0, 32), independent_product((1,), 32)
            )
        self.assertEqual(
            module.coefficients(2, 2, 32), independent_product((4, -1), 32)
        )
        self.assertEqual(
            module.euler_weights(module.coefficients(2, 2, 32)), (4, -1) + (0,) * 30
        )

    def test_quadratic_held_out_integer_dimensions(self):
        expected = (
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
        )
        self.assertEqual(module.euler_weights(module.coefficients(2, 3, 12)), expected)
        self.assertEqual(
            module.euler_weights(module.coefficients(3, 2, 12)), (9,) + expected[1:]
        )

    def test_newton_sums_against_second_order_recurrence(self):
        values = [2, 4]
        for _ in range(2, 33):
            values.append(4 * values[-1] - values[-2])
        self.assertEqual(module.newton_sums((1, 4, 1), 32), tuple(values[1:]))
        self.assertEqual(module.newton_sums((1, 0, 1), 6), (0, -2, 0, 2, 0, -2))
        self.assertEqual(module.newton_sums((1,), 6), (0,) * 6)

    def test_signed_grades_against_independent_products(self):
        for first in range(-2, 3):
            for second in range(-2, 3):
                weights = (first, second, 3, 0, -2)
                values = independent_product(weights, 16)
                wanted = weights + (0,) * 11
                self.assertEqual(module.euler_weights(values), wanted)
                self.assertEqual(module.triangular_weights(values), wanted)

    def test_signed_nonpositive_series_do_not_require_effectivity(self):
        for values in ((1,), (1, -1, 0, 0, 0), (1, 2, -3, 4, -5), (1, 0, -2, 0, 3)):
            weights = module.euler_weights(values)
            self.assertEqual(weights, module.triangular_weights(values))
            self.assertEqual(independent_product(weights, len(values) - 1), values)

    def test_polynomial_types_checked_before_trimming(self):
        for bad in (
            (1, False),
            (1, 0.0),
            (1, Q(0)),
            (0,),
            (),
            (1,) * 18,
            (1, 1 << 128),
            "1",
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                module.polynomial(bad)
        self.assertEqual(module.polynomial([1, 2, 0, 0]), (1, 2))

    def test_series_types_and_caps(self):
        for bad in (
            (1, True),
            (1, 1.0),
            (1, Q(1)),
            (0,),
            (),
            (1,) * 34,
            (1, 1 << 128),
            "1",
        ):
            for operation in (
                module.logarithmic_coefficients,
                module.euler_weights,
                module.triangular_weights,
            ):
                with (
                    self.subTest(bad=bad, operation=operation),
                    self.assertRaises(ValueError),
                ):
                    operation(bad)
        self.assertEqual(module.series([1, -2, 3]), (1, -2, 3))

    def test_integer_rational_and_arithmetic_bit_boundaries(self):
        for bad in (True, 1.0, Q(1), 1 << 128):
            with self.assertRaises(ValueError):
                module.input_integer(bad)
        self.assertEqual(module.input_integer((1 << 128) - 1), (1 << 128) - 1)
        for bad in (True, 1.0, Q(1), 1 << 4096):
            with self.assertRaises(ValueError):
                module.arithmetic(bad)
        for bad in (True, 1.0, "1/2", Q(1, 1 << 128)):
            with self.assertRaises(ValueError):
                module.rational(bad)
        self.assertEqual(module.rational(Q(-3, 7)), Q(-3, 7))

    def test_mobius_values_and_guards(self):
        self.assertEqual(
            [module.mobius(i) for i in range(1, 17)],
            [1, -1, -1, 0, -1, 1, -1, 0, 0, 1, -1, 0, -1, 1, 1, 0],
        )
        for bad in (True, 1.0, 0, 33):
            with self.assertRaises(ValueError):
                module.mobius(bad)

    def test_parameter_preflight_precedes_source_authentication(self):
        bound = module.preflight(1, 0, 2)
        with mock.patch.object(
            module, "source_locks", side_effect=RuntimeError("not reached")
        ):
            with self.assertRaisesRegex(ValueError, "strictly below cap"):
                module.build_report(1, 0, 2, cap=bound)
            for values in (
                (True, 2, 4),
                (2, 2.0, 4),
                (0, 2, 4),
                (6, 2, 4),
                (2, 6, 4),
                (2, -1, 4),
                (2, 2, 1),
                (2, 2, 33),
            ):
                with self.subTest(values=values), self.assertRaises(ValueError):
                    module.build_report(*values)
        self.assertLess(module.preflight(5, 5, 32), module.WORK_CAP)
        self.assertEqual(module.preflight(1, 0, 2, cap=bound + 1), bound)

    def test_chambers_and_direct_api_parameter_guards(self):
        self.assertEqual(module.chamber(1, 5), "ZETA")
        self.assertEqual(module.chamber(5, 0), "ZETA")
        self.assertEqual(module.chamber(5, 1), "ZETA_POWER")
        self.assertEqual(module.chamber(2, 2), "ZETA4_OVER_ZETA2")
        self.assertEqual(module.chamber(2, 3), "ESTERMANN_NATURAL_BOUNDARY")
        for operation, values in (
            (module.coefficients, (2, 2, True)),
            (module.numerator, (True, 2)),
            (module.chamber, (2, 6)),
            (module.newton_sums, ((1, 1), 33)),
            (module.reconstruct_series, ((1, 1), 0, 2)),
            (module.reconstruct_series, ((1, 1), True, 2)),
        ):
            with self.assertRaises(ValueError):
                operation(*values)

    def test_centered_grade_affine_identity(self):
        for grade in range(1, 33):
            data = module.centered_grade(grade)
            shift = Q(data["argument_shift"])
            for s in (Q(-3, 7), Q(0), Q(1, 2), Q(2)):
                self.assertEqual(grade * (1 - s) + shift, 1 - (grade * s + shift))
            self.assertEqual(Q(data["local_prime_weight_exponent"]), -shift)
        for bad in (True, 1.0, 0, 33):
            with self.assertRaises(ValueError):
                module.centered_grade(bad)

    def test_synthetic_halving_forest(self):
        points = ((Q(1, 2), 4), (Q(1, 8), 1), (Q(1, 4), 2), (Q(2, 3), -1))
        data = module.halving_forest(points)
        self.assertEqual([row["depth"] for row in data], [0, 1, 2, 0])
        self.assertEqual(data[2]["terminal"], ["1/8", "1"])
        for row in data:
            for value, terminal in zip(row["point"], row["terminal"]):
                self.assertEqual(Q(value), 2 ** row["depth"] * Q(terminal))

    def test_halving_forest_rejects_nonexact_and_nonstrip_points(self):
        for bad in (
            (),
            "x",
            ((0, 1),),
            ((1, 1),),
            ((Q(1, 2), 0),),
            ((Q(1, 2), True),),
            ((Q(1, 2), 1.0),),
            ((Q(1, 2), Q(1, 1 << 128)),),
            ((Q(1, 2),),),
            ((Q(1, 2), 1),) * 2,
            ((Q(1, 2), 1),) * 17,
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                module.halving_forest(bad)

    def test_pole_order_and_cancellation_are_separate(self):
        self.assertEqual(module.pole_order(7, 0), 7)
        self.assertEqual(module.pole_order(1, 1), -3)
        self.assertEqual(module.pole_order(4, 1), 0)
        self.assertEqual(module.pole_order(5, 1), 1)
        for values in ((True, 0), (0, 0), (33, 0), (1, True), (1, -1), (1, 33)):
            with self.assertRaises(ValueError):
                module.pole_order(*values)

    def test_strict_json_and_typed_replay(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"a":NaN}',
            b'{"a":Infinity}',
            b'{"a":-Infinity}',
            b" " * (module.MAX_BYTES + 1),
            "{}",
        ):
            with self.subTest(raw=str(raw)[:50]), self.assertRaises(ValueError):
                module.strict_json(raw)
        for left, right in (
            ({"count": True}, {"count": 1}),
            ({"count": 1.0}, {"count": 1}),
            ({"rows": []}, {"rows": [], "extra": False}),
        ):
            with self.assertRaises(ValueError):
                module.same_json(left, right)

    def test_source_manifest_and_lf_stability(self):
        locks = module.source_locks()
        self.assertEqual(locks["authenticated_parent_files"], 2)
        self.assertFalse(locks["external_theorems_machine_proved"])
        self.assertEqual(module.digest(b"a\r\nb\r"), module.digest(b"a\nb\n"))
        self.assertEqual(
            module.strict_json(module.bounded_bytes(module.MANIFEST)),
            module.expected_manifest(),
        )

    def test_manifest_and_live_source_tampering_are_rejected(self):
        original = module.bounded_bytes
        changed = copy.deepcopy(module.expected_manifest())
        changed["parent_sources"][0]["git_blob"] = "0" * 40
        with (
            mock.patch.object(
                module, "bounded_bytes", return_value=module.canonical(changed)
            ),
            self.assertRaisesRegex(ValueError, "canonical replay"),
        ):
            module.source_locks()
        source = ROOT / module.SOURCE_ROWS[0][0]

        def tampered(path):
            return original(path) + b"changed" if path == source else original(path)

        with (
            mock.patch.object(module, "bounded_bytes", side_effect=tampered),
            self.assertRaisesRegex(ValueError, "current digest"),
        ):
            module.source_locks()

    def test_default_fixture_payload_and_scope(self):
        report = module.build_report()
        module.same_json(
            module.strict_json(module.bounded_bytes(module.FIXTURE)), report
        )
        payload = dict(report)
        fingerprint = payload.pop("payload_sha256")
        self.assertEqual(
            fingerprint, hashlib.sha256(module.canonical(payload)).hexdigest()
        )
        self.assertEqual(report["coverage"]["complete_rows"], 30)
        self.assertEqual(
            report["coverage"]["natural_boundary_rows_by_written_theorem"], 15
        )
        self.assertEqual(report["coverage"]["actual_zeta_zero_samples"], 0)
        self.assertEqual(report["arithmetic"]["class"], "MIXED")
        self.assertEqual(
            report["centered_square_coefficient"]["unmodified_p_squared"], 9
        )
        self.assertTrue(all(value is False for value in report["scope"].values()))

    def test_complete_replay_rejects_row_and_scope_mutation(self):
        expected = module.build_report()
        changed = copy.deepcopy(expected)
        changed["rows"][0]["formal_graded_dimensions"] = [2] + [0] * 23
        with self.assertRaises(ValueError):
            module.same_json(changed, expected)
        changed = copy.deepcopy(expected)
        changed["scope"]["D22_arbitrary_meromorphic_multiplier_no_rescue"] = True
        with self.assertRaises(ValueError):
            module.same_json(changed, expected)

    def test_maximal_report_and_artifact_bindings(self):
        report = module.build_report(5, 5, 32)
        self.assertEqual(report["coverage"]["grade_inclusive"], [1, 32])
        for relative, fingerprint in report["artifact_sha256_lf"].items():
            self.assertEqual(
                fingerprint, module.digest(module.bounded_bytes(ROOT / relative))
            )
        self.assertLessEqual(len(module.render(report).encode()), module.MAX_BYTES)

    def test_no_assert_or_float_mathematical_checks(self):
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
            command = [sys.executable, "-B"] + (["-O"] if optimized else [])
            result = subprocess.run(
                command + [str(PATH), "--check"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
                timeout=40,
            )
            self.assertEqual(json.loads(result.stdout)["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
