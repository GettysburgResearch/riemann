"""Independent finite controls and hostile-input drills for tensor moments."""

import copy
import importlib.util
import unittest
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT / "research/l-families/atlas/generalized/tensor_moment_completion_rigidity.py"
)
SPEC = importlib.util.spec_from_file_location("tensor_moment_controls", SCRIPT)
m = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(m)


def factorial_coefficient(degree, k):
    k = abs(k)
    return sum(
        factorial(degree)
        // (factorial(r) * factorial(r + k) * factorial(degree - 2 * r - k))
        for r in range((degree - k) // 2 + 1)
    )


class ExactControls(unittest.TestCase):
    def test_full_fixture_replay(self):
        self.assertEqual(m.check_fixture()["status"], "PASS")

    def test_known_baseline_moments(self):
        self.assertEqual(
            [m.baseline_moment(r) for r in range(13)],
            [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585, 4213],
        )

    def test_factorial_formula_held_out(self):
        for degree in (0, 1, 2, 5, 11, 17, 24):
            row = m.tensor_weights(degree)
            for k in range(-degree - 1, degree + 2):
                self.assertEqual(row.get(k, 0), factorial_coefficient(degree, k))
                self.assertEqual(
                    m.trinomial_coefficient(degree, k), factorial_coefficient(degree, k)
                )

    def test_first_missing_moments_all_supported_j(self):
        for j in range(1, m.MAX_J + 1):
            self.assertEqual(
                [m.perturbation_shift(j, degree) for degree in range(j + 1)],
                [0] * j + [1],
            )
            self.assertEqual(m.perturbation_shift(j, j + 1), j)

    def test_j2_mean_preserving_failure(self):
        self.assertEqual(m.kernel_trace_polynomial(2), {0: -1, 1: -1, 2: 1})
        for epsilon in (Q(1, 7), Q(-1, 7), Q(3, 17), Q(-3, 17)):
            self.assertEqual(m.perturbed_moment(2, 1, epsilon), 0)
            self.assertEqual(m.perturbed_moment(2, 2, epsilon), 1 + epsilon)
            self.assertFalse(
                m.density_control(2, epsilon)["lower_euler_meromorphy_proved"]
            )

    def test_signed_zero_and_tiny_epsilon(self):
        for j in (1, 2, 7, 11, 12):
            zero = m.density_control(j, 0)
            self.assertFalse(zero["jth_nonmeromorphy_obstruction"])
            epsilon = Q(1, 2**127 - 1)
            for sign in (-1, 1):
                control = m.density_control(j, sign * epsilon)
                self.assertTrue(control["jth_nonmeromorphy_obstruction"])
                self.assertEqual(
                    m.perturbed_moment(j, j, sign * epsilon),
                    m.baseline_moment(j) + sign * epsilon,
                )

    def test_density_telescope_and_cdf_derivative(self):
        for j in (1, 3, 8, 11, 12):
            wanted = {-j: Q(1, 2), j: Q(1, 2), -j - 1: Q(-1, 2), j + 1: Q(-1, 2)}
            self.assertEqual(m.density_laurent(j), wanted)
            self.assertEqual(
                m.cdf_perturbation(j)["sine_coefficients"],
                [[j, 1, j], [j + 1, -1, j + 1]],
            )

    def test_kernel_polynomial_held_out(self):
        self.assertEqual(m.kernel_trace_polynomial(0), {0: 1})
        self.assertEqual(m.kernel_trace_polynomial(3), {0: 1, 1: -1, 2: -2, 3: 1})
        for j in (4, 9, 12):
            self.assertEqual(
                m._substitute_trace(m.kernel_trace_polynomial(j)), m.dirichlet_kernel(j)
            )

    def test_maximum_rectangular_coverage(self):
        report = m.build_report(m.MAX_J, m.MAX_M)
        self.assertEqual(report["coverage"]["complete_shift_cells"], 300)
        self.assertEqual(len(report["perturbations"]), 12)
        self.assertTrue(
            all(len(row["moment_shifts"]) == 25 for row in report["perturbations"])
        )
        self.assertEqual(report["coverage"]["actual_delta_prime_samples"], 0)


class StrictContracts(unittest.TestCase):
    def test_scalar_types_fail_closed(self):
        for bad in (True, False, 0.1, "1/10", None, [], {}):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                m.density_control(2, bad)
        for bad in (True, 2.0, "2", -1, 25):
            with self.subTest(value=bad), self.assertRaises(ValueError):
                m.tensor_weights(bad)
        for bad in (0, 13, True, 2.0):
            with self.assertRaises(ValueError):
                m.dirichlet_kernel(bad)

    def test_strict_density_chamber_and_bits(self):
        for j in (1, 2, 12):
            endpoint = Q(1, 2 * j + 1)
            for bad in (endpoint, -endpoint, 2 * endpoint, Q(1, 2**128), 2**128):
                with self.subTest(j=j, epsilon=bad), self.assertRaises(ValueError):
                    m.density_control(j, bad)
            self.assertGreater(
                Q(
                    *m.density_control(j, endpoint * Q(99, 100))[
                        "density_margin_lower_bound"
                    ]
                ),
                0,
            )

    def test_exclusive_resource_cap_and_preflight(self):
        score = m.work_score(8, 12)
        with self.assertRaises(ValueError):
            m.preflight(8, 12, score)
        self.assertEqual(m.preflight(8, 12, score + 1), score)
        for args in ((13, 24), (12, 11), (1, 25), (True, 12), (1, 1)):
            with (
                patch.object(
                    m, "source_locks", side_effect=RuntimeError("preflight first")
                ),
                self.assertRaises(ValueError),
            ):
                m.build_report(*args)
        with self.assertRaises(ValueError):
            m.preflight(8, 12, True)

    def test_json_duplicates_nonfinite_types_bytes(self):
        for raw in (
            b'{"x":1,"x":1}',
            b'{"x":NaN}',
            b'{"x":-Infinity}',
            b"[" + b" " * m.MAX_BYTES + b"]",
        ):
            with self.assertRaises(ValueError):
                m.strict_json(raw)
        for bad in ({"x": True}, {"x": 1.0}, {"x": "1"}):
            with self.assertRaises(ValueError):
                m.same_json(bad, {"x": 1})

    def test_manifest_tamper(self):
        changed = m.expected_manifest()
        changed["prior_art"][0]["role"] = "proves new group reconstruction"
        with (
            patch.object(m, "strict_json", return_value=changed),
            self.assertRaises(ValueError),
        ):
            m.source_locks()

    def test_git_blob_tamper(self):
        fake = type("Completed", (), {"stdout": b"wrong-blob\n"})()
        with (
            patch.object(m.subprocess, "run", return_value=fake),
            self.assertRaises(ValueError),
        ):
            m.source_locks()

    def test_current_parent_tamper(self):
        original = m.bounded_bytes
        target = m.ROOT / m.SOURCE_ROWS[0][0]

        def altered(path):
            return b"changed mathematical parent" if path == target else original(path)

        with (
            patch.object(m, "bounded_bytes", side_effect=altered),
            self.assertRaises(ValueError),
        ):
            m.source_locks()

    def test_fixture_real_checker_tamper(self):
        original = m.strict_json(m.bounded_bytes(m.FIXTURE))
        variants = []
        row = copy.deepcopy(original)
        row["baseline_moments"][2] = 2
        variants.append(row)
        row = copy.deepcopy(original)
        row["perturbations"][0]["moment_shifts"][0] = 1
        variants.append(row)
        row = copy.deepcopy(original)
        row["coverage"]["actual_delta_prime_samples"] = False
        variants.append(row)
        row = copy.deepcopy(original)
        row["payload_sha256"] = "0" * 64
        variants.append(row)
        original_reader = m.bounded_bytes
        for changed in variants:

            def altered(path, changed=changed):
                return (
                    m.render(changed).encode()
                    if path == m.FIXTURE
                    else original_reader(path)
                )

            with (
                patch.object(m, "bounded_bytes", side_effect=altered),
                self.assertRaises(ValueError),
            ):
                m.check_fixture()

    def test_changed_note_artifact_fails(self):
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

    def test_lf_and_canonical_stability(self):
        self.assertEqual(m.digest(b"a\r\nb\r\n"), m.digest(b"a\nb\n"))
        self.assertEqual(m.canonical({"a": 1, "b": 2}), m.canonical({"b": 2, "a": 1}))


if __name__ == "__main__":
    unittest.main()
