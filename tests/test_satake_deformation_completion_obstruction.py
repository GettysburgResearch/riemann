"""Held-out exact and fail-closed controls for the Satake deformation packet."""

import copy
import importlib.util
import json
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research/l-families/atlas/generalized/satake_deformation_completion_obstruction.py"
)
SPEC = importlib.util.spec_from_file_location("satake_completion_controls", SCRIPT)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


class ExactControls(unittest.TestCase):
    def test_fixture_and_source_replay(self):
        self.assertEqual(m.check_fixture()["status"], "PASS")
        locks = m.source_locks()
        self.assertTrue(locks["context_authenticated"])
        self.assertFalse(locks["external_theorems_machine_proved"])

    def test_mean_coefficients_independent_small_values(self):
        self.assertEqual(
            m.mean_coefficients(8),
            [
                Q(0),
                Q(0),
                Q(1, 4),
                Q(0),
                Q(-1, 64),
                Q(0),
                Q(1, 2304),
                Q(0),
                Q(-1, 147456),
            ],
        )

    def test_maximum_formal_coverage(self):
        values = m.mean_coefficients(m.MAX_ORDER)
        self.assertEqual(
            values, [m.mean_coefficient_formula(j) for j in range(m.MAX_ORDER + 1)]
        )
        self.assertEqual(m.sine_even_moment(6, 12), Q(676039, 4194304))
        report = m.build_report(m.MAX_ORDER)
        self.assertEqual(report["coverage"]["formal_degrees_inclusive"], [0, 24])

    def test_held_out_phase_controls(self):
        for frequency in range(1, 7):
            for phase in (-7, -5, -2, -1, 1, 2, 5, 7):
                values = m.phase_constant_terms(frequency, phase, 10)
                if phase % frequency:
                    self.assertTrue(all(x == 0 for x in values))
        self.assertEqual(m.phase_constant_terms(3, -3, 2)[1], Q(1, 2))
        self.assertEqual(m.cube_root_sum(3), (3, 0))
        self.assertEqual(m.cube_root_sum(-1), (0, 0))

    def test_zero_sign_and_held_out_epsilon(self):
        self.assertEqual(m.mean_bounds(0)["lower"], [0, 1])
        self.assertFalse(m.mean_bounds(0)["noninteger_order_obstruction"])
        plus, minus = m.mean_bounds(Q(7, 11)), m.mean_bounds(Q(-7, 11))
        self.assertEqual(plus["lower"], minus["lower"])
        self.assertEqual(plus["upper"], minus["upper"])
        self.assertEqual(plus["upper"], [49, 484])
        self.assertTrue(plus["noninteger_order_obstruction"])
        self.assertEqual(m.mean_bounds(1)["lower"], [15, 64])
        self.assertEqual(m.mean_bounds(1)["upper"], [1, 4])

    def test_su2_to_so3_trace_identity(self):
        # Rational cos(theta), sin(theta): the induced angle is phi=2theta.
        for c, s in ((Q(3, 5), Q(4, 5)), (Q(5, 13), Q(12, 13)), (Q(0), Q(1))):
            phi_c, phi_s = c * c - s * s, 2 * c * s
            a = m._rotation(phi_c, phi_s)
            self.assertEqual(m._trace(a), (2 * c) ** 2 - 1)
            self.assertEqual(m._trace(m.matrix_generator(a)), 0)

    def test_matrix_controls_and_held_out_conjugation(self):
        report = m.matrix_controls()
        self.assertEqual(len(report["so3_controls"]), 6)
        self.assertNotEqual(report["generic_sl3_generator_trace"], [0, 1])
        a = m._rotation(Q(7, 25), Q(24, 25))
        g = m.matrix_generator(a)
        self.assertEqual(m._transpose(g), m._matscale(g, Q(-1)))
        self.assertEqual(m.matrix_generator(m._inverse(a)), m._matscale(g, Q(-1)))

    def test_local_series_independent_controls(self):
        self.assertEqual(
            m.local_control(1, 4)["coefficients"],
            [[1, 1], [3, 1], [6, 1], [10, 1], [15, 1]],
        )
        self.assertEqual(
            m.local_control(0, 4)["coefficients"],
            [[1, 1], [1, 1], [0, 1], [0, 1], [1, 1]],
        )
        row = m.local_control(Q(7, 25), 18)
        self.assertEqual(row["denominator"], [[1, 1], [-39, 25], [39, 25], [-1, 1]])


class StrictContracts(unittest.TestCase):
    def test_scalar_type_rejections(self):
        for bad in (True, False, 0.5, "1/2", None, [], {}):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                m.mean_bounds(bad)
        for bad in (True, 2.0, "2", -1, 1, 25):
            with self.subTest(order=bad), self.assertRaises(ValueError):
                m.mean_coefficients(bad)

    def test_bounds_and_bit_rejections(self):
        for bad in (Q(1001, 1000), Q(-1001, 1000), 2, -2, Q(1, 2**128), 2**128):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                m.mean_bounds(bad)
        with self.assertRaises(ValueError):
            m.local_control(Q(3, 2), 4)
        for frequency in (0, 7, True, 3.0):
            with self.assertRaises(ValueError):
                m.phase_constant_terms(frequency, 1, 4)
        for phase in (-73, 73, True, 1.0):
            with self.assertRaises(ValueError):
                m.cube_root_sum(phase)

    def test_matrix_type_and_singularity(self):
        for bad in (
            [],
            ((1, 0), (0, 1)),
            ((True, 0, 0), (0, 1, 0), (0, 0, 1)),
            ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
        ):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                m.matrix_generator(bad)

    def test_exclusive_resource_boundary(self):
        exact = m.work_bound(12)
        with self.assertRaises(ValueError):
            m.preflight(12, exact)
        self.assertEqual(m.preflight(12, exact + 1), exact)
        with self.assertRaises(ValueError):
            m.preflight(12, True)
        with (
            patch.object(
                m, "source_locks", side_effect=RuntimeError("must not authenticate")
            ),
            self.assertRaises(ValueError),
        ):
            m.build_report(25)

    def test_json_type_duplicate_nonfinite_and_byte_rejections(self):
        for raw in (
            b'{"x":1,"x":1}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b"[" + b" " * m.MAX_BYTES + b"]",
        ):
            with self.subTest(raw=raw[:50]), self.assertRaises(ValueError):
                m.strict_json(raw)
        for actual in ({"x": True}, {"x": 1.0}, {"x": "1"}):
            with self.assertRaises(ValueError):
                m.same_json(actual, {"x": 1})

    def test_manifest_declaration_tamper(self):
        changed = m.expected_manifest()
        changed["external_theorems"][1]["import"] = "effective uniform estimate"
        with (
            patch.object(m, "strict_json", return_value=changed),
            self.assertRaises(ValueError),
        ):
            m.source_locks()

    def test_git_source_identity_tamper(self):
        fake = type("Completed", (), {"stdout": b"wrong-blob\n"})()
        with (
            patch.object(m.subprocess, "run", return_value=fake),
            self.assertRaises(ValueError),
        ):
            m.source_locks()

    def test_current_source_digest_tamper(self):
        original = m.bounded_bytes

        def altered(path):
            return (
                b"changed source" if path == m.ROOT / m.CONTEXT_PATH else original(path)
            )

        with (
            patch.object(m, "bounded_bytes", side_effect=altered),
            self.assertRaises(ValueError),
        ):
            m.source_locks()

    def test_fixture_payload_artifact_and_boolean_tamper(self):
        original = m.strict_json(m.bounded_bytes(m.FIXTURE))
        changes = []
        row = copy.deepcopy(original)
        row["mean_coefficients"][2] = [1, 3]
        changes.append(row)
        row = copy.deepcopy(original)
        row["payload_sha256"] = "0" * 64
        changes.append(row)
        row = copy.deepcopy(original)
        row["coverage"]["actual_delta_prime_samples"] = False
        changes.append(row)
        row = copy.deepcopy(original)
        row["artifact_sha256_lf"][
            str(m.NOTE.relative_to(m.ROOT)).replace("\\", "/")
        ] = "0" * 64
        changes.append(row)
        original_reader = m.bounded_bytes
        for changed in changes:

            def altered(path, changed=changed):
                return (
                    m.render(changed).encode()
                    if path == m.FIXTURE
                    else original_reader(path)
                )

            with (
                self.subTest(change=changed["payload_sha256"]),
                patch.object(m, "bounded_bytes", side_effect=altered),
                self.assertRaises(ValueError),
            ):
                m.check_fixture()

    def test_changed_artifact_fails_real_checker(self):
        original = m.bounded_bytes

        def altered(path):
            raw = original(path)
            return raw + b"\nchanged note\n" if path == m.NOTE else raw

        with (
            patch.object(m, "bounded_bytes", side_effect=altered),
            self.assertRaises(ValueError),
        ):
            m.check_fixture()

    def test_crlf_checkout_replay(self):
        original = m.bounded_bytes

        def crlf(path):
            return original(path).replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")

        with patch.object(m, "bounded_bytes", side_effect=crlf):
            self.assertEqual(m.check_fixture()["status"], "PASS")

    def test_lf_hash_and_canonical_stability(self):
        self.assertEqual(m.digest(b"a\r\nb\r\n"), m.digest(b"a\nb\n"))
        self.assertEqual(m.canonical({"b": 2, "a": 1}), m.canonical({"a": 1, "b": 2}))
        self.assertEqual(
            m.strict_json(json.dumps({"x": [1, 2]}).encode()), {"x": [1, 2]}
        )


if __name__ == "__main__":
    unittest.main()
