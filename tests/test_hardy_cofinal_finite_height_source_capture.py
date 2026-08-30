"""Bounded exact controls, with analytic and native-capture firewalls."""

import ast
import copy
import importlib.util
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER = ROOT / "research/exploratory/hardy_cofinal_finite_height_source_capture.py"
SPEC = importlib.util.spec_from_file_location("hardy_capture", PRODUCER)
m = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = m
SPEC.loader.exec_module(m)


def gaussian(pair):
    return tuple(Fraction(value) for value in pair)


class HardyCaptureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = m.build_report()

    def test_fixture_exact(self):
        m.check_fixture(m.read_json(m.FIXTURE.read_bytes()), self.report)

    def test_single_node_origin_and_gram(self):
        row = m.gram_control(((7, Fraction(1, 4), 1),))
        self.assertEqual(row["gram"], [[["2", "0"]]])
        self.assertEqual(row["origin_kernel"], ["1/2", "0"])

    def test_confluent_gram_factorial_integrals(self):
        row = m.gram_control(((0, 1, 4),))
        for i, values in enumerate(row["gram"]):
            for j, entry in enumerate(values):
                expected = Fraction(
                    math.factorial(i + j),
                    math.factorial(i) * math.factorial(j) * 2 ** (i + j + 1),
                )
                self.assertEqual(gaussian(entry), (expected, 0))
        self.assertEqual(row["origin_kernel"], ["8", "0"])

    def test_held_out_nonreal_and_confluent(self):
        for nodes in (
            ((Fraction(1, 3), Fraction(2, 3), 2),),
            ((-3, 2, 1), (4, Fraction(1, 2), 2)),
            ((0, 1, 1), (Fraction(1, 100), 1, 1)),
        ):
            row = m.gram_control(nodes)
            self.assertTrue(row["lyapunov_identity_exact"])
            self.assertTrue(
                all(Fraction(x) > 0 for x in row["positive_principal_minors"])
            )
            self.assertEqual(
                Fraction(row["origin_kernel"][0]), 2 * sum(y * n for _, y, n in nodes)
            )

    def test_gram_shape_degree_caps(self):
        for nodes in (
            [],
            (),
            ((0, 1),),
            ((0, 1, 0),),
            ((0, 1, 5),),
            ((0, 1, 3), (2, 1, 2)),
            ((0, 1, 1), (0, 1, 1)),
            ((0, -1, 1),),
            ((0, 0, 1),),
        ):
            with self.subTest(nodes=nodes), self.assertRaises(ValueError):
                m.gram_control(nodes)

    def test_node_strict_scalar_types(self):
        for bad in (True, False, 1.0, "1", None):
            for index in range(3):
                row = [0, 1, 1]
                row[index] = bad
                with self.assertRaises(ValueError):
                    m.gram_control((tuple(row),))

    def test_rational_caps_and_flag(self):
        for value in (2**16, Fraction(1, 2**16), -(2**16), True, 1.0):
            with self.assertRaises(ValueError):
                m.fraction(value)
        self.assertEqual(m.fraction(65535), 65535)
        with self.assertRaises(ValueError):
            m.fraction(2**1024, internal=True)
        for flag in (1, "yes", None):
            with self.assertRaises(ValueError):
                m.fraction(2**20, internal=flag)

    def test_geographic_split(self):
        row = self.report["geographic_source_leakage"]
        retained, omitted = map(gaussian, (row["retained_node"], row["omitted_node"]))
        radius = Fraction(row["geographic_radius"])
        self.assertLess(sum(x * x for x in retained), radius**2)
        self.assertGreater(sum(x * x for x in omitted), radius**2)

    def test_independent_leakage_origin_residue(self):
        # Sum of the lower residues is one minus the single upper residue.
        # u=1/2,v=1,A=2,y=1/4 gives 1+(1/3)*(3/4-2i)/(73/16).
        origin = (
            1 + Fraction(1, 3) * Fraction(3, 4) / Fraction(73, 16),
            -Fraction(1, 3) * 2 / Fraction(73, 16),
        )
        row = self.report["geographic_source_leakage"]
        self.assertEqual(gaussian(row["origin_ratio"]), origin)
        self.assertEqual(sum(x * x for x in origin), Fraction(745, 657))

    def test_leakage_full_time_coefficients(self):
        row = self.report["geographic_source_leakage"]
        expected = [
            (Fraction(24, 73), Fraction(64, 73)),
            (Fraction(4, 73), Fraction(-32, 219)),
            (Fraction(49, 73), Fraction(-64, 73)),
        ]
        self.assertEqual(
            list(map(gaussian, row["physical_time_coefficients"])), expected
        )
        self.assertTrue(row["full_polynomial_identity_exact"])
        self.assertEqual(
            tuple(sum(z[k] for z in expected) for k in (0, 1)),
            gaussian(row["origin_ratio"]),
        )

    def test_actual_adjoint_not_raw_values(self):
        row = self.report["geographic_source_leakage"]
        self.assertFalse(row["raw_value_substitution_matches"])
        self.assertEqual(
            list(map(gaussian, row["adjoint_source_coefficients"])),
            [
                (Fraction(8, 73), Fraction(64, 219)),
                (Fraction(69, 73), Fraction(-32, 73)),
            ],
        )
        self.assertIn("R=U-B", row["literal_residual"])

    def test_quantitative_prefix_interval(self):
        row = self.report["geographic_source_leakage"]
        coefficients = list(map(gaussian, row["physical_time_coefficients"]))
        poles = list(map(gaussian, row["physical_poles"]))
        bound = sum(
            (abs(a) + abs(b)) * (abs(c) + abs(d))
            for (a, b), (c, d) in zip(coefficients, poles)
        )
        self.assertEqual(bound, Fraction(4195, 876))
        cutoff = Fraction(row["positive_prefix_cutoff"])
        self.assertEqual(cutoff, Fraction(24, 4195))
        self.assertEqual(Fraction(77, 73) - bound * cutoff, Fraction(75, 73))
        self.assertGreater(Fraction(row["tail_bound_violation_factor"]), 1)
        for divisor in (1, 2, 7, 31):
            self.assertGreater(Fraction(77, 73) - bound * cutoff / divisor, 1)

    def test_projection_polynomial_identity_held_out_points(self):
        # Exact evaluation of the published partial fractions at non-pole rational points.
        row = self.report["geographic_source_leakage"]
        lower = [m._q(0, -1), m._q(2, Fraction(-1, 4))]
        u = m._q(0, Fraction(1, 2))
        cs = list(map(gaussian, row["adjoint_source_coefficients"]))
        poles = list(map(gaussian, row["physical_poles"]))
        coeffs = list(map(gaussian, row["physical_time_coefficients"]))
        for x in (-3, -1, 0, 3, 7):
            point = m._q(x)
            left = m.sum_q(m._div(c, m._sub(point, p)) for c, p in zip(coeffs, poles))
            plus = m.sum_q(m._div(c, m._sub(point, p)) for c, p in zip(cs, lower))
            right = m._mul(m._div(m._sub(point, u), m._sub(point, m._conj(u))), plus)
            self.assertEqual(left, right)

    def test_singular_indicator_traces(self):
        for rank in (1, 3, 5, 8):
            row = m.singular_control(rank)
            intervals = [
                tuple(Fraction(v) for v in values) for values in row["intervals"]
            ]
            weight = Fraction(row["squared_indicator_amplitude"])
            gram = [
                [weight * max(Fraction(), min(b, d) - max(a, c)) for c, d in intervals]
                for a, b in intervals
            ]
            self.assertEqual(
                gram, [[int(i == j) for j in range(rank)] for i in range(rank)]
            )
            self.assertEqual(row["physical_band_trace"], rank)
            self.assertEqual(row["denominator_zero_count"], 0)
            self.assertFalse(row["denominator_is_pure_blaschke"])

    def test_panel_caps(self):
        for function in (m.singular_control, m.height_control, m.lacunary_control):
            for bad in (0, -1, 9, True, 2.0, "2"):
                with self.assertRaises(ValueError):
                    function(bad)

    def test_finite_height_infinite_rank_control(self):
        for rank in range(1, 9):
            row = m.height_control(rank, Fraction(3, 2))
            partial = Fraction(row["height_partial_sum"])
            tail = Fraction(row["height_remainder"])
            self.assertEqual(partial + tail, 1)
            self.assertEqual(tail, Fraction(1, 2**rank))
            self.assertEqual(Fraction(row["finite_total_bound"]), 3 * partial)
            self.assertFalse(row["source_tail_bound_asserted"])
            self.assertEqual(row["total_charge_when_U_equals_one"], rank)

    def test_lowpass_endpoint_not_width(self):
        for endpoint in (Fraction(1, 2), 7):
            row = m.height_control(4, endpoint)
            self.assertEqual(Fraction(row["infinite_total_bound"]), 2 * endpoint)
        for bad in (0, -1, True, 1.0, Fraction(1, 2**16)):
            with self.assertRaises(ValueError):
                m.height_control(1, bad)

    def test_lacunary_schur_bound(self):
        for rank in (2, 3, 5, 8):
            row = m.lacunary_control(rank)
            centers = row["centers"]
            for i, a in enumerate(centers):
                total = sum(
                    (Fraction(2, abs(a - b)) for j, b in enumerate(centers) if j != i),
                    Fraction(),
                )
                self.assertEqual(total, Fraction(row["off_diagonal_row_majorants"][i]))
                self.assertLessEqual(total, Fraction(1, 4))
            self.assertEqual(
                Fraction(row["band_trace_lower_coefficient"]), Fraction(4 * rank, 5)
            )

    def test_gaussian_inverse_held_out(self):
        matrix = [
            [m._q(2), m._q(1, 1)],
            [m._q(1, -1), m._q(3)],
        ]
        inverse = m._inverse(matrix)
        self.assertEqual(m._mm(matrix, inverse), m._identity(2))
        self.assertEqual(m._det(matrix), m._q(4))
        self.assertEqual(m._positive_minors(matrix, strict=True), ["2", "3", "4"])

    def test_private_algebra_fail_closed(self):
        with self.assertRaises(ValueError):
            m._div(m.ONE, m.ZERO)
        with self.assertRaises(ValueError):
            m._inverse([[m.ZERO]])
        with self.assertRaises(ValueError):
            m._poly_mul([m.ONE] * 8, [m.ONE] * 2)
        with self.assertRaises(ValueError):
            m._residues([m.ONE], (m.ONE, m.ONE))
        for matrix in ([], [[m.ONE] * 5] * 5, [[m.ONE], []], [[(True, 0)]]):
            with self.assertRaises(ValueError):
                m._inverse(matrix)
        for bad in (5, True, 1.0):
            with self.assertRaises(ValueError):
                m._identity(bad)
        with self.assertRaises(ValueError):
            m._positive_minors([[m.ONE]], strict=1)

    def test_source_roles_and_original_states(self):
        sources = self.report["sources"]["frozen_sources"]
        self.assertEqual(len(sources), 9)
        self.assertEqual(
            {row["kind"] for row in sources},
            {"scientific_source", "historical_context", "review_context"},
        )
        by_id = {row["id"]: row for row in sources}
        self.assertEqual(
            by_id["inner"]["commit"], "ef7bbb8dca978269f24e7ff9d97b6dceeed5b460"
        )
        self.assertEqual(
            by_id["count"]["commit"], "76454e3db0ccce8f500297ea27668d6088b5091a"
        )
        self.assertEqual(by_id["count_review"]["commit"], m.BASE)

    def test_manifest_schema_and_metadata_tamper(self):
        original = m.manifest_expected()
        m.exact_match(m.read_json(m.MANIFEST.read_bytes()), original)
        for key in ("schema", "authoring_base"):
            changed = copy.deepcopy(original)
            changed[key] = "forged"
            with self.assertRaises(ValueError):
                m.exact_match(changed, original)
        for key in ("commit", "path", "kind", "role", "git_blob", "sha256_lf"):
            changed = copy.deepcopy(original)
            changed["sources"][0][key] = "forged"
            with self.assertRaises(ValueError):
                m.exact_match(changed, original)

    def test_primitive_raw_authentication(self):
        row = m.SOURCE_ROWS[1]
        raw = subprocess.check_output(
            ["git", "show", row["commit"] + ":" + row["path"]], cwd=ROOT, timeout=10
        )
        m.authenticate_raw(row, raw)
        for altered in (raw + b"x", b"", b"counterfeit"):
            with self.assertRaises(ValueError):
                m.authenticate_raw(row, altered)
        with self.assertRaises(ValueError):
            m.authenticate_raw({**row, "kind": "untyped"}, raw)

    def test_lf_normalization_and_bytes(self):
        self.assertEqual(m.digest(b"a\nb\n"), m.digest(b"a\r\nb\r\n"))
        self.assertEqual(m.digest(b"a\nb\n"), m.digest(b"a\rb\r"))
        for value in ("text", b"x" * (m.MAX_BYTES + 1)):
            with self.assertRaises(ValueError):
                m.digest(value)

    def test_json_fail_closed(self):
        for raw in (
            b'{"a":1,"a":2}',
            b'{"a":NaN}',
            b'{"a":1.0}',
            b'{"a":Infinity}',
            b"[] trailing",
            b"[" * 20 + b"0" + b"]" * 20,
            b" " * (m.MAX_BYTES + 1),
        ):
            with self.assertRaises(ValueError):
                m.read_json(raw)
        for value in ({"a": Fraction(1, 2)}, {"a": "x" * 2049}, {"a": 2**1024}):
            with self.assertRaises(ValueError):
                m.render(value)

    def test_fixture_types_digest_and_unknown_keys(self):
        for key, value in (
            ("schema", "forged"),
            ("arithmetic_class", "DIRECTED_INTERVAL"),
            ("payload_sha256", "0" * 64),
            ("unknown", 1),
        ):
            altered = copy.deepcopy(self.report)
            altered[key] = value
            with self.assertRaises(ValueError):
                m.check_fixture(altered, self.report)
        payload = copy.deepcopy(self.report)
        payload.pop("payload_sha256")
        payload["scope"]["finite_total_height_required"] = 1
        with self.assertRaises(ValueError):
            m.check_fixture(m.seal(payload), self.report)
        with self.assertRaises(ValueError):
            m.exact_match([True], [1])

    def test_all_current_artifacts_bound(self):
        artifacts = self.report["sources"]["current_artifacts"]
        self.assertEqual(len(artifacts), 4)
        for path, row in artifacts.items():
            self.assertEqual(row["kind"], "current_artifact")
            self.assertEqual(row["sha256_lf"], m.digest((ROOT / path).read_bytes()))

    def test_producer_has_no_assert_or_float(self):
        tree = ast.parse(PRODUCER.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) is float
                for node in ast.walk(tree)
            )
        )

    def test_scope_fields(self):
        scope = self.report["scope"]
        for key in (
            "pure_blaschke_denominator_required",
            "finite_total_height_required",
            "same_physical_projector",
            "corrected_adjoint_source",
        ):
            self.assertIs(scope[key], True)
        for key in (
            "same_quantitative_source_tail",
            "uniform_in_T_capture_proved",
            "native_Xi_finite_total_height_proved",
            "total_charge_bound_proved",
            "shrinking_width_substitution_proved",
            "countercontrols_are_actual_Xi",
            "analytic_limits_machine_verified",
        ):
            self.assertIs(scope[key], False)

    def test_note_preserves_native_gaps(self):
        note = m.NOTE.read_text(encoding="utf-8")
        for marker in (
            "HC10",
            "HC13",
            "HC14",
            "HC15",
            "LOW-PASS",
            "No actual-Xi",
            "Historical raw value jets",
            "no uniform rate",
        ):
            self.assertIn(marker, note)


if __name__ == "__main__":
    unittest.main()
