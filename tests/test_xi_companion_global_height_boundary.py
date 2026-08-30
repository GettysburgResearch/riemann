"""Exact finite tests; no numerical Xi or formal verification of analytic limits."""

import ast
import copy
import importlib.util
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "research/exploratory/xi_companion_global_height_boundary.py"
SPEC = importlib.util.spec_from_file_location("xi_height_boundary", PRODUCER)
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)


def decoded(pair):
    return tuple(Fraction(v) for v in pair)


def partitions(n, weight=1):
    if weight == 7:
        if n == 0:
            yield ()
        return
    for count in range(n // weight + 1):
        for remaining in partitions(n - count * weight, weight + 1):
            yield (count,) + remaining


class XiCompanionHeightTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_fixture_full_replay(self):
        m.check_fixture(m.read_json(m.FIXTURE.read_bytes()), self.report)

    def test_taxonomy_and_no_rounding(self):
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["CERTIFIED_INTEGER_COVERAGE", "EXACT_RATIONAL"],
        )
        self.assertIn("no rounding", self.report["rounding_contract"])
        self.assertIn(
            "no rounding", " ".join(m.NOTE.read_text(encoding="utf-8").split())
        )

    def test_axis_phase_cycle_and_fifth_sign(self):
        cycle = ((1, 0), (0, -1), (-1, 0), (0, 1))
        for k in range(7):
            row = m.axis_control(k)
            self.assertEqual(decoded(row["phase"]), cycle[k % 4])
            self.assertEqual(decoded(row["next_phase"]), cycle[(k + 1) % 4])
            self.assertEqual(decoded(row["ratio"]), (Fraction(-1, 19), 0))
        self.assertEqual(decoded(m.axis_control(5)["phase"]), (0, -1))
        self.assertEqual(decoded(m.axis_control(5)["next_phase"]), (-1, 0))

    def test_axis_moments_held_out(self):
        for k in (0, 3, 5, 6):
            for h, h1, scale in (
                (1, 3, 1),
                (Fraction(2, 5), Fraction(7, 11), Fraction(1, 3)),
                (7, 2, Fraction(7, 2)),
            ):
                row = m.axis_control(k, h, h1, scale)
                self.assertEqual(
                    decoded(row["ratio"]), ((h - scale * h1) / (h + scale * h1), 0)
                )

    def test_zero_lambda_exception(self):
        for k in (0, 5):
            self.assertEqual(decoded(m.axis_control(k, scale=0)["ratio"]), (1, 0))

    def test_axis_domain_caps(self):
        for bad in (-1, 7, True, 1.0, "5"):
            with self.assertRaises(ValueError):
                m.axis_control(bad)
        for name in ("h", "next_h", "scale"):
            for bad in (True, 1.0, "1", None, Fraction(1, 2**16)):
                with self.assertRaises(ValueError):
                    m.axis_control(5, **{name: bad})
        for kwargs in ({"h": 0}, {"next_h": -1}, {"scale": -1}):
            with self.assertRaises(ValueError):
                m.axis_control(0, **kwargs)

    def test_cayley_known_quadratic_zero(self):
        # P=z^2-1, lambda=1: P-iP'=(z-i)^2 and Theta(i)=0.
        row = m.cayley_control(((-1, 1), (1, 1)), 0, 1, 1)
        self.assertEqual(decoded(row["log_derivative"]), (0, -1))
        self.assertEqual(decoded(row["theta"]), (0, 0))
        self.assertEqual(Fraction(row["denominator_minus_numerator_norm_squared"]), 4)

    def test_cayley_independent_polynomial_evaluation(self):
        # P=(z+2)(z-1)^2, evaluated by product and polynomial derivative.
        for x, y, scale in ((2, 1, 1), (-1, 2, Fraction(2, 3)), (0, 3, 2)):
            z = m._q(x, y)
            z2, zm1 = m._add(z, m._q(2)), m._add(z, m._q(-1))
            p = m._mul(z2, m._mul(zm1, zm1))
            dp = m._add(m._mul(zm1, zm1), m._mul(m._q(2), m._mul(z2, zm1)))
            direct = m._div(
                m._add(p, m._mul(m._q(0, -scale), dp)),
                m._add(p, m._mul(m._q(0, scale), dp)),
            )
            row = m.cayley_control(((-2, 1), (1, 2)), x, y, scale)
            self.assertEqual(decoded(row["theta"]), direct)
            self.assertLess(m._norm(direct), 1)

    def test_real_root_domain_and_multiplicity_caps(self):
        for roots in (
            [],
            (),
            ((1, 0),),
            ((1, 9),),
            ((1, 1), (1, 2)),
            ((1, 5), (2, 4)),
            ((True, 1),),
            ((0, True),),
            ((1, 1.0),),
            ((1, 1, 1),),
        ):
            with self.assertRaises(ValueError):
                m.cayley_control(roots, 0, 1, 1)
        for x, y, scale in ((True, 1, 1), (0, 0, 1), (0, -1, 1), (0, 1, 0), (0, 1, -1)):
            with self.assertRaises(ValueError):
                m.cayley_control(((0, 1),), x, y, scale)

    def test_multiple_real_root_removal(self):
        for multiplicity in range(1, 8):
            row = m.removable_control(
                ((Fraction(1, 3), multiplicity), (2, 1)), Fraction(1, 3)
            )
            self.assertEqual(row["common_order"], multiplicity - 1)
            self.assertEqual(decoded(row["removed_ratio"]), (-1, 0))
        with self.assertRaises(ValueError):
            m.removable_control(((1, 2),), 2)

    def test_native_quotient_orientation_algebra(self):
        scale = Fraction(2, 3)
        a, b, c, d = map(m._q, (2, 3, 5, 7))
        minus0 = m._add(a, m._mul(m._q(0, -scale), b))
        plus0 = m._add(a, m._mul(m._q(0, scale), b))
        minus5 = m._add(c, m._mul(m._q(0, -scale), d))
        plus5 = m._add(c, m._mul(m._q(0, scale), d))
        native = m._div(m._mul(minus0, plus5), m._mul(plus0, minus5))
        theta0, theta5 = m._div(minus0, plus0), m._div(minus5, plus5)
        self.assertEqual(native, m._div(theta0, theta5))
        self.assertNotEqual(native, m._div(theta5, theta0))

    def test_bell_independent_partition_formula(self):
        for order in range(7):
            independent = {}
            for powers in partitions(order):
                denominator = math.prod(
                    math.factorial(count) * math.factorial(j + 1) ** count
                    for j, count in enumerate(powers)
                )
                independent[powers] = math.factorial(order) // denominator
            self.assertEqual(m.bell(order), independent)

    def test_bell_fifth_explicit(self):
        expected = {
            (5, 0, 0, 0, 0, 0): 1,
            (3, 1, 0, 0, 0, 0): 10,
            (2, 0, 1, 0, 0, 0): 10,
            (1, 2, 0, 0, 0, 0): 15,
            (1, 0, 0, 1, 0, 0): 5,
            (0, 1, 1, 0, 0, 0): 10,
            (0, 0, 0, 0, 1, 0): 1,
        }
        self.assertEqual(m.bell(5), expected)

    def test_bell_residual_and_asymptotic_weights(self):
        row = m.bell_control()
        self.assertEqual(len(row["GH14_residual"]), 10)
        self.assertEqual(row["residual_absolute_coefficient_sum"], 181)
        for term in row["GH14_residual"]:
            self.assertGreaterEqual(term["inverse_y_power"], 2)
            self.assertLessEqual(term["D_power"], 4)
        constants = row["leading_constants_without_lambda"]
        self.assertEqual(constants["component_attenuation_times_log_y"], "4")
        self.assertEqual(constants["D5_minus_D_times_y_log_y"], "5")
        self.assertEqual(constants["ratio_times_y_log_y_cubed"], "40")

    def test_sparse_polynomial_caps(self):
        for bad in (-1, 7, True, 2.0):
            with self.assertRaises(ValueError):
                m.bell(bad)
        for poly in (
            {(0,) * 5: 1},
            {(0,) * 6: True},
            {(0,) * 6: 0},
            {(0,) * 6: 2**1024},
            {(8, 0, 0, 0, 0, 0): 1},
            {(0, 0, 0, 0, 0, 2): 1},
        ):
            with self.assertRaises(ValueError):
                m._poly_valid(poly)
        with self.assertRaises(ValueError):
            m._differentiate(m.bell(6))
        with self.assertRaises(ValueError):
            m._times_variable(m.bell(1), True)

    def test_blaschke_single_factor_exact_modulus(self):
        row = m.blaschke_control(((2, 1, 1),), 3)
        self.assertEqual(Fraction(row["product_squared_modulus"]), Fraction(2, 5))
        self.assertEqual(row["reciprocal_axis_numerator"], ["1", "-2", "5"])
        self.assertEqual(row["reciprocal_axis_denominator"], ["1", "2", "5"])
        self.assertEqual(Fraction(row["finite_height_limit_from_slope"]), 2)

    def test_blaschke_multiple_factor_slope_and_domination(self):
        panels = (
            ((0, Fraction(1, 3), 4),),
            ((-7, Fraction(2, 3), 2), (9, Fraction(1, 5), 3)),
            ((Fraction(1, 7), 2, 1), (0, 3, 1)),
        )
        for nodes in panels:
            height = sum(eta * count for _, eta, count in nodes)
            for multiple in (2, 3, 5):
                row = m.blaschke_control(nodes, multiple * height)
                self.assertEqual(
                    Fraction(row["finite_height_limit_from_slope"]), 2 * height
                )
                expected = math.prod(
                    Fraction(
                        a * a + (multiple * height - eta) ** 2,
                        a * a + (multiple * height + eta) ** 2,
                    )
                    ** count
                    for a, eta, count in nodes
                )
                self.assertEqual(Fraction(row["product_squared_modulus"]), expected)
                for factor in row["factor_controls"]:
                    self.assertLessEqual(
                        Fraction(factor["y_log_upper_bound_per_copy"]),
                        Fraction(factor["dominating_height_bound_per_copy"]),
                    )

    def test_node_shape_caps_and_y_gate(self):
        for nodes in (
            [],
            (),
            ((0, 0, 1),),
            ((0, -1, 1),),
            ((0, 1, 0),),
            ((0, 1, True),),
            ((0, 1.0, 1),),
            ((0, 1, 5), (1, 1, 4)),
            ((0, 1, 1), (0, 1, 1)),
            ((0, 1),),
        ):
            with self.assertRaises(ValueError):
                m.blaschke_control(nodes, 20)
        for bad in (1, 0, -1, True, 2.0):
            with self.assertRaises(ValueError):
                m.blaschke_control(((0, 1, 1),), bad)
        with self.assertRaises(ValueError):
            m.nodes_checked((), empty=1)

    def test_cancellation_preserves_multiplicities(self):
        left = ((0, 1, 4), (2, 3, 1))
        right = ((0, 1, 2), (4, 5, 2))
        common, l, r = m.cancel_nodes(left, right)
        self.assertEqual(common, ((0, 1, 2),))
        self.assertEqual(l, ((0, 1, 2), (2, 3, 1)))
        self.assertEqual(r, ((4, 5, 2),))
        self.assertEqual(m.cancel_nodes((), ()), ((), (), ()))
        self.assertEqual(m.cancel_nodes(left, ()), ((), left, ()))

    def test_common_prefix_does_not_pay_reduced_height(self):
        for n in range(5):
            row = m.cancellation_control(n)
            self.assertEqual(row["component_heights"], [str(n + 2)] * 2)
            self.assertEqual(row["reduced_heights"], ["2", "2"])
            self.assertFalse(row["actual_Xi_example"])
        for bad in (-1, 5, True, 1.0):
            with self.assertRaises(ValueError):
                m.cancellation_control(bad)

    def test_fourth_power_tail_prefix_contract(self):
        for n in range(1, 9):
            row = m.fourth_power_tail_control(n)
            partial = sum((Fraction(1, j**4) for j in range(1, n + 1)), Fraction())
            self.assertEqual(Fraction(row["partial_height_at_c_one"]), partial)
            self.assertEqual(Fraction(row["tail_lower"]), Fraction(1, 3 * (n + 1) ** 3))
            self.assertEqual(Fraction(row["tail_upper"]), Fraction(1, 3 * n**3))
            tail_first_100 = sum(
                (Fraction(1, j**4) for j in range(n + 1, 101)), Fraction()
            )
            self.assertLess(tail_first_100, Fraction(row["tail_upper"]))
        for bad in (0, 9, True, 1.0):
            with self.assertRaises(ValueError):
                m.fourth_power_tail_control(bad)

    def test_exact_arithmetic_caps(self):
        for value in (True, False, 1.0, "1", None, 2**16, Fraction(1, 2**16)):
            with self.assertRaises(ValueError):
                m.rational(value)
        self.assertEqual(m.rational(2**16 - 1), 2**16 - 1)
        with self.assertRaises(ValueError):
            m.rational(2**1024, internal=True)
        with self.assertRaises(ValueError):
            m.rational(1, internal=1)
        with self.assertRaises(ValueError):
            m._div(m._q(1), m._q())
        with self.assertRaises(ValueError):
            m._valid_q((True, 0))

    def test_seven_typed_sources_and_frozen_states(self):
        sources = self.report["sources"]["frozen_sources"]
        self.assertEqual(len(sources), 7)
        by_id = {row["id"]: row for row in sources}
        self.assertEqual(
            by_id["count"]["commit"], "76454e3db0ccce8f500297ea27668d6088b5091a"
        )
        self.assertEqual(
            by_id["capture"]["commit"], "90e8dff3d184cbfe59974969ca89615856c33c51"
        )
        self.assertIn("claims/lemmas/L-106620", by_id["frozen_lambda"]["path"])
        self.assertIn("claims/theorems/T-106620", by_id["native"]["path"])
        self.assertEqual(by_id["height"]["kind"], "historical_context")

    def test_dense_product_helper_caps(self):
        for left, right in (
            ((), [1]),
            ([], [1]),
            ([True], [1]),
            ([1.0], [1]),
            ([2**1024], [1]),
            ([1] * 17, [1, 1]),
        ):
            with self.assertRaises(ValueError):
                m._multiply_real(left, right)
        self.assertEqual(m._multiply_real([1, 2], [1, -2]), [1, 0, -4])

    def test_primitive_raw_authentication_and_tamper(self):
        row = m.SOURCE_ROWS[0]
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT, timeout=10
        )
        m.authenticate_raw(row, raw)
        for altered in (raw + b"x", b"", b"counterfeit"):
            with self.assertRaises(ValueError):
                m.authenticate_raw(row, altered)
        with self.assertRaises(ValueError):
            m.authenticate_raw({**row, "kind": "forged"}, raw)

    def test_manifest_typed_complete_comparison(self):
        expected = m.manifest_expected()
        m.exact_match(m.read_json(m.MANIFEST.read_bytes()), expected)
        for key in ("schema", "authoring_base"):
            changed = copy.deepcopy(expected)
            changed[key] = "forged"
            with self.assertRaises(ValueError):
                m.exact_match(changed, expected)
        for key in ("commit", "path", "role", "kind", "git_blob", "sha256_lf"):
            changed = copy.deepcopy(expected)
            changed["sources"][0][key] = "forged"
            with self.assertRaises(ValueError):
                m.exact_match(changed, expected)

    def test_source_locks_fail_closed_missing_manifest(self):
        with (
            mock.patch.object(
                m, "MANIFEST", m.HERE / "not-a-real-manifest-for-height-tests.json"
            ),
            self.assertRaises(FileNotFoundError),
        ):
            m.source_locks()

    def test_four_current_artifact_hashes(self):
        artifacts = self.report["sources"]["current_artifacts"]
        self.assertEqual(len(artifacts), 4)
        for path, row in artifacts.items():
            self.assertEqual(row["kind"], "current_artifact")
            self.assertEqual(row["sha256_lf"], m.digest((ROOT / path).read_bytes()))

    def test_bytes_utf8_lf_and_caps(self):
        self.assertEqual(m.digest(b"a\r\nb\r\n"), m.digest(b"a\nb\n"))
        self.assertEqual(m.digest(b"a\rb\r"), m.digest(b"a\nb\n"))
        for raw in ("not bytes", b"\xff", b"x" * (m.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                m.digest(raw)

    def test_json_rejects_nonexact_and_excessive_data(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"a":1.0}',
            b'{"a":NaN}',
            b'{"a":Infinity}',
            b'{"a":-Infinity}',
            b"[] trailing",
            b"[" * 20 + b"0" + b"]" * 20,
            b" " * (m.MAX_BYTES + 1),
        ):
            with self.assertRaises(ValueError):
                m.read_json(raw)
        for value in (Fraction(1, 2), [0] * 1025, "x" * 4097, 2**1024, {True: 1}):
            with self.assertRaises(ValueError):
                m.render(value)

    def test_fixture_resealed_math_and_scope_tamper(self):
        for target in ("bell", "scope", "source", "unknown"):
            payload = copy.deepcopy(self.report)
            payload.pop("payload_sha256")
            if target == "bell":
                payload["bell_asymptotic_algebra"]["GH14_residual"][0][
                    "coefficient"
                ] += 1
            elif target == "scope":
                payload["scope"][
                    "actual_reduced_denominator_infinite_height_proved"
                ] = True
            elif target == "source":
                payload["sources"]["frozen_sources"][0]["role"] = "forged"
            else:
                payload["unknown"] = 1
            with self.assertRaises(ValueError):
                m.check_fixture(m.seal(payload), self.report)
        altered = copy.deepcopy(self.report)
        altered["payload_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            m.check_fixture(altered, self.report)
        with self.assertRaises(ValueError):
            m.exact_match([True], [1])

    def test_scope_firewalls(self):
        scope = self.report["scope"]
        for key in (
            "actual_reduced_denominator_infinite_height_proved",
            "finite_band_trace_infinity_proved",
            "native_cofinal_capture_failure_proved",
            "uniform_lambda_limit_proved",
            "RH_proved",
            "analytic_limits_machine_verified",
            "nonnative_controls_are_actual_Xi",
        ):
            self.assertIs(scope[key], False)
        self.assertIs(scope["fixed_positive_lambda"], True)
        self.assertIs(scope["corrected_adjoint_source_preserved"], True)
        self.assertEqual(
            scope["native_quotient_orientation"],
            "Theta0/Theta5 before common-inner cancellation",
        )

    def test_note_proof_markers_and_boundaries(self):
        note = m.NOTE.read_text(encoding="utf-8")
        for marker in (
            "GH3",
            "GH8",
            "GH14",
            "GH16",
            "GH19",
            "GH20",
            "NONNATIVE",
            "RH remains unsolved",
            "does NOT prove",
        ):
            self.assertIn(marker, note)

    def test_producer_no_assert_no_float_no_writes(self):
        tree = ast.parse(PRODUCER.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(tree)
            )
        )
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                self.assertNotIn(node.attr, ("write_text", "write_bytes"))

    def test_manifest_emit_and_cli_conflict(self):
        emitted = subprocess.check_output(
            [sys.executable, "-B", str(PRODUCER), "--emit-manifest"],
            cwd=ROOT,
            timeout=20,
        )
        m.exact_match(m.read_json(emitted), m.manifest_expected())
        conflict = subprocess.run(
            [sys.executable, "-B", str(PRODUCER), "--check", "--emit-manifest"],
            cwd=ROOT,
            capture_output=True,
            timeout=20,
            check=False,
        )
        self.assertNotEqual(conflict.returncode, 0)


if __name__ == "__main__":
    unittest.main()
