"""Independent finite series controls; no numerical Xi, zeros, or analytic limits."""

import ast
import copy
import hashlib
import importlib.util
import json
import math
import subprocess
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "research/exploratory/xi_companion_imaginary_axis_sampling.py"
SPEC = importlib.util.spec_from_file_location("xi_axis_tested", SOURCE)
M = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(M)


def coefficients(values):
    return [Q(value) for value in values]


def padded(values, degree):
    return coefficients(values[: degree + 1]) + [Q(0)] * max(
        0, degree + 1 - len(values)
    )


def convolution(left, right, degree):
    """Direct coefficient definition, independent of producer helpers."""
    return [
        sum(
            (
                Q(left[j]) * Q(right[n - j])
                for j in range(n + 1)
                if j < len(left) and n - j < len(right)
            ),
            Q(0),
        )
        for n in range(degree + 1)
    ]


def power(values, exponent, degree):
    result = [Q(1)] + [Q(0)] * degree
    for _ in range(exponent):
        result = convolution(result, values, degree)
    return result


def substitution(outer, inner, degree):
    result = [Q(0)] * (degree + 1)
    for exponent, coefficient in enumerate(outer):
        term = power(inner, exponent, degree)
        result = [x + Q(coefficient) * y for x, y in zip(result, term)]
    return result


def reciprocal(values, degree):
    """Solve the triangular coefficient equations a*b=1."""
    result = [1 / Q(values[0])]
    for n in range(1, degree + 1):
        result.append(
            -sum(
                (
                    Q(values[j]) * result[n - j]
                    for j in range(1, min(n + 1, len(values)))
                ),
                Q(0),
            )
            / Q(values[0])
        )
    return result


def lagrange_inverse(values, degree):
    """Lagrange: inverse coefficient n is [x^(n-1)](x/f(x))^n/n."""
    quotient = reciprocal(values[1:], degree - 1)
    return [Q(0)] + [power(quotient, n, n - 1)[n - 1] / n for n in range(1, degree + 1)]


def hyperbolic_coefficients(node, degree, parity):
    return [
        Q(node) ** n / math.factorial(n) if n % 2 == parity else Q(0)
        for n in range(degree + 1)
    ]


def direct_pair(u, v, degree):
    """Symmetrized gg''-g'^2 before the cosh addition formula."""
    sinh_product = convolution(
        hyperbolic_coefficients(u, degree, 1),
        hyperbolic_coefficients(v, degree, 1),
        degree,
    )
    cosh_product = convolution(
        hyperbolic_coefficients(u, degree, 0),
        hyperbolic_coefficients(v, degree, 0),
        degree,
    )
    return [
        (u * u + v * v) * s / 2 - u * v * c for s, c in zip(sinh_product, cosh_product)
    ]


def independent_moments(nodes, weights, count):
    return [
        2 * sum((w * u**r for u, w in zip(nodes, weights)), Q(0))
        if r % 2 == 0
        else Q(0)
        for r in range(count)
    ]


def moment_series(mu, shift, degree):
    return [mu[shift + n] / math.factorial(n) for n in range(degree + 1)]


HELD_OUT_MODELS = (
    ([Q(2)], [Q(3, 5)]),
    ([Q(2, 3), Q(5, 2)], [Q(4, 7), Q(3, 2)]),
    ([Q(1, 4), Q(4, 3), Q(7, 2)], [Q(3), Q(2, 5), Q(1, 7)]),
)


class XiCompanionImaginaryAxisTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = M.build_report()

    def test_01_strict_integer_domains(self):
        for value in (True, False, 1.0, Q(1), "1", None, -1, 9):
            with self.assertRaises(ValueError):
                M.integer(value, 0, 8)
        for value in range(9):
            self.assertEqual(M.integer(value, 0, 8), value)

    def test_02_strict_rationals_and_bit_boundaries(self):
        for value in (True, False, 1.0, complex(1), "1", None, 2**16, Q(1, 2**16)):
            with self.assertRaises(ValueError):
                M.rational(value)
        for value in (-(2**16 - 1), Q(1, 2**16 - 1), Q(7, 11)):
            self.assertEqual(M.rational(value), value)
        self.assertEqual(M.rational(2**4096 - 1, internal=True), 2**4096 - 1)
        for value in (2**4096, Q(1, 2**4096)):
            with self.assertRaises(ValueError):
                M.rational(value, internal=True)
        for flag in (0, 1, None, "yes"):
            with self.assertRaises(ValueError):
                M.rational(1, internal=flag)

    def test_03_polynomial_shapes_types_and_degree_caps(self):
        for values in (
            [],
            (),
            "1",
            {0: 1},
            [True],
            [1.0],
            [complex(1)],
            [2**4096],
            [1] * 22,
        ):
            with self.assertRaises(ValueError):
                M.polynomial(values)
        self.assertEqual(coefficients(M.polynomial([Q(1, 3), -2, 0])), [Q(1, 3), -2])
        self.assertEqual(len(M.polynomial([1] * 21)), 21)

    def test_04_budget_exact_type_and_limit(self):
        for value in (True, False, 0, 200001, 1.0, Q(1)):
            with self.assertRaises(ValueError):
                M.Budget(value)
        work = M.Budget(3)
        work.spend(2)
        work.spend(1)
        self.assertEqual(work.used, 3)
        for amount in (True, -1, 1.0, 1):
            with self.assertRaises(ValueError):
                work.spend(amount)
            self.assertEqual(work.used, 3)

    def test_05_work_charged_before_expansion_and_exact_budget_type(self):
        calls = (
            lambda w: M.multiply([1, 1], [1, 1], 4, w),
            lambda w: M.inverse_series([1, 1], 4, w),
            lambda w: M.pair_control(1, 2, 4, w),
            lambda w: M.moment_control([1, 2], [1, 1], 4, w),
        )
        for function in calls:
            work = M.Budget(1)
            with self.assertRaises(ValueError):
                function(work)
            self.assertEqual(work.used, 0)
            with self.assertRaises(ValueError):
                function(object())
        for function in (M.compose, M.revert_series):
            with self.assertRaises(ValueError):
                if function is M.compose:
                    function([1, 1], [0, 1], 4, object())
                else:
                    function([0, 1], 4, object())

    def test_06_add_multiply_and_derivative_independent_coefficients(self):
        for left, right in (
            ([1, -2, 3], [Q(2, 3), 0, -1, 4]),
            ([0], [1, 1]),
            ([Q(3, 7), -4], [Q(-7, 9), 2]),
        ):
            degree = max(len(left), len(right)) - 1
            expected = [
                x + y for x, y in zip(padded(left, degree), padded(right, degree))
            ]
            self.assertEqual(padded(M.add(left, right), degree), expected)
            expected_derivative = [Q(j) * left[j] for j in range(1, len(left))] or [
                Q(0)
            ]
            self.assertEqual(
                padded(M.derivative(left), len(expected_derivative) - 1),
                expected_derivative,
            )
            for cut in (0, 1, 3, 8, 20):
                self.assertEqual(
                    padded(M.multiply(left, right, cut), cut),
                    convolution(left, right, cut),
                )
        with self.assertRaises(ValueError):
            M.multiply([2**4095], [2])

    def test_07_composition_independent_power_sum(self):
        for outer, inner in (
            ([1, 2, 3], [0, -1, Q(2, 3)]),
            ([Q(1, 2), 0, -3, 2], [0, 2, -1, 1]),
            ([1, 0, 0, 0, 1], [0, 1]),
        ):
            for cut in (0, 3, 8):
                self.assertEqual(
                    padded(M.compose(outer, inner, cut), cut),
                    substitution(outer, inner, cut),
                )

    def test_08_reciprocal_independent_triangular_equations(self):
        for values in ([2, -3, 1], [Q(3, 7), Q(2, 5)], [1, 0, 2, 0, -1], [7]):
            for cut in (0, 1, 4, 8, 20):
                actual = padded(M.inverse_series(values, cut), cut)
                self.assertEqual(actual, reciprocal(values, cut))
                self.assertEqual(
                    convolution(values, actual, cut), [Q(1)] + [Q(0)] * cut
                )

    def test_09_reversion_independent_lagrange_formula(self):
        for values in ([0, 2, -3, 1], [0, 1, 0, 2, 0, -1], [0, Q(3, 2), Q(1, 5)]):
            for cut in (1, 4, 8):
                actual = padded(M.revert_series(values, cut), cut)
                self.assertEqual(actual, lagrange_inverse(values, cut))
                identity = [Q(0), Q(1)] + [Q(0)] * (cut - 1)
                self.assertEqual(substitution(values, actual, cut), identity)
                self.assertEqual(substitution(actual, values, cut), identity)

    def test_10_series_domain_and_cutoff_guards(self):
        for bad in (True, 1.0, -1, 21, Q(2)):
            for function in (
                lambda bad=bad: M.pad([1], bad),
                lambda bad=bad: M.multiply([1], [1], bad),
                lambda bad=bad: M.compose([1], [0, 1], bad),
                lambda bad=bad: M.inverse_series([1], bad),
                lambda bad=bad: M.revert_series([0, 1], bad),
            ):
                with self.assertRaises(ValueError):
                    function()
        for values in ([0], [0, 1], [0, 0, 1]):
            with self.assertRaises(ValueError):
                M.inverse_series(values, 6)
        for values in ([1, 1], [0], [0, 0, 1]):
            with self.assertRaises(ValueError):
                M.revert_series(values, 6)
        with self.assertRaises(ValueError):
            M.revert_series([0, 1], 0)
        with self.assertRaises(ValueError):
            M.compose([1, 1], [1, 1], 6)

    def test_11_full_quadrant_pair_via_direct_hyperbolic_convolution(self):
        for u, v in ((Q(1), Q(2)), (Q(2, 3), Q(7, 4)), (Q(5), Q(1, 3))):
            for cut in (2, 5, 8):
                row = M.pair_control(u, v, cut)
                direct = direct_pair(u, v, 2 * cut)
                self.assertEqual(coefficients(row["even_coefficients"]), direct[::2])
                self.assertEqual(direct[1::2], [Q(0)] * cut)
                self.assertEqual(Q(row["full_quadrant_factor"]), Q(1, 4))
                self.assertEqual(Q(row["ordered_half_quadrant_factor"]), Q(1, 2))
                self.assertEqual(Q(row["even_coefficients"][0]), -u * v)

    def test_12_pair_symmetry_diagonal_and_homogeneity(self):
        for u, v in ((Q(1), Q(3)), (Q(2, 5), Q(7, 3))):
            row, reverse = M.pair_control(u, v), M.pair_control(v, u)
            self.assertEqual(row["even_coefficients"], reverse["even_coefficients"])
            scaled = coefficients(M.pair_control(2 * u, 2 * v)["even_coefficients"])
            self.assertEqual(
                scaled,
                [
                    2 ** (2 * j + 2) * q
                    for j, q in enumerate(coefficients(row["even_coefficients"]))
                ],
            )
        for u in (Q(1), Q(2, 3), Q(5)):
            row = M.pair_control(u, u)
            self.assertEqual(
                coefficients(row["even_coefficients"]), [-u * u] + [Q(0)] * 8
            )
            self.assertIs(row["strict_growth_control"], False)

    def test_13_pair_derivative_signs_and_first_strict_coefficient(self):
        for u, v in ((Q(1), Q(2)), (Q(3, 4), Q(5, 3))):
            row = M.pair_control(u, v)
            actual = coefficients(row["even_coefficients"])
            self.assertEqual(actual[1], 0)
            self.assertEqual(actual[2], u * v * (u * u - v * v) ** 2 / 24)
            self.assertTrue(all(value > 0 for value in actual[2:]))
            self.assertEqual(
                coefficients(row["odd_derivative_coefficients"]),
                [2 * j * actual[j] for j in range(1, 9)],
            )
            self.assertIs(row["strict_growth_control"], True)

    def test_14_pair_strict_types_positive_domain_and_caps(self):
        for value in (True, 1.0, complex(1), "1", 0, -1, 2**16, Q(1, 2**16)):
            with self.assertRaises(ValueError):
                M.pair_control(value, 1)
            with self.assertRaises(ValueError):
                M.pair_control(1, value)
        for cut in (True, 1.0, 1, 9):
            with self.assertRaises(ValueError):
                M.pair_control(1, 2, cut)

    def test_15_even_moments_and_half_line_weight_normalization(self):
        for nodes, weights in HELD_OUT_MODELS:
            row = M.moment_control(nodes, weights, 8)
            actual = coefficients(row["moments"])
            self.assertEqual(len(actual), 16)
            self.assertEqual(actual, independent_moments(nodes, weights, 16))
            self.assertEqual(actual[0], 2 * sum(weights))
            self.assertTrue(all(x > 0 for x in actual[::2]))
            self.assertEqual(actual[1::2], [Q(0)] * 8)
            self.assertIs(row["actual_Xi_measure"], False)
            self.assertIs(row["analytic_root_count_inferred_from_panel"], False)

    def test_16_covariance_full_signed_double_sum(self):
        for nodes, weights in HELD_OUT_MODELS:
            row = M.moment_control(nodes, weights, 8)
            signed = [(sign * u, w) for u, w in zip(nodes, weights) for sign in (-1, 1)]
            expected = [
                sum(
                    (
                        a
                        * b
                        * (u - v)
                        * (u**5 - v**5)
                        * (u + v) ** n
                        / (2 * math.factorial(n))
                        for u, a in signed
                        for v, b in signed
                    ),
                    Q(0),
                )
                for n in range(9)
            ]
            actual = coefficients(row["covariance_K"])
            self.assertEqual(actual, expected)
            mu = independent_moments(nodes, weights, 16)
            self.assertEqual(actual[0], mu[0] * mu[6])
            self.assertTrue(all(value >= 0 for value in actual))

    def test_17_laurent_y_D5_by_independent_division(self):
        for nodes, weights in HELD_OUT_MODELS:
            row = M.moment_control(nodes, weights, 8)
            mu = independent_moments(nodes, weights, 16)
            numerator = moment_series(mu, 6, 8)
            denominator = moment_series(mu, 5, 9)[1:]
            actual = coefficients(row["y_D5"])
            self.assertEqual(
                actual, convolution(numerator, reciprocal(denominator, 8), 8)
            )
            self.assertEqual(actual[0], 1)
            self.assertEqual(actual[2], mu[8] / (3 * mu[6]))
            self.assertEqual(
                actual[4], mu[10] / (30 * mu[6]) - mu[8] ** 2 / (18 * mu[6] ** 2)
            )
            self.assertEqual(actual[1::2], [Q(0)] * 4)

    def test_18_small_root_reversion_and_explicit_fifth_coefficient(self):
        for nodes, weights in HELD_OUT_MODELS:
            row = M.moment_control(nodes, weights, 8)
            mu = independent_moments(nodes, weights, 16)
            lambda_y = convolution(
                moment_series(mu, 5, 8), reciprocal(moment_series(mu, 6, 8), 8), 8
            )
            self.assertEqual(coefficients(row["lambda_of_y"]), lambda_y)
            actual = coefficients(row["small_root"])
            self.assertEqual(actual, lagrange_inverse(lambda_y, 8))
            self.assertEqual(actual[3], mu[8] / (3 * mu[6]))
            self.assertEqual(
                actual[5], mu[8] ** 2 / (6 * mu[6] ** 2) + mu[10] / (30 * mu[6])
            )
            self.assertEqual(actual[::2], [Q(0)] * 5)

    def test_19_raw_sample_and_square_from_independent_moments(self):
        for nodes, weights in HELD_OUT_MODELS:
            row = M.moment_control(nodes, weights, 8)
            mu = independent_moments(nodes, weights, 16)
            lambda_y = convolution(
                moment_series(mu, 5, 8), reciprocal(moment_series(mu, 6, 8), 8), 8
            )
            root = lagrange_inverse(lambda_y, 8)
            d0 = convolution(
                moment_series(mu, 1, 8), reciprocal(moment_series(mu, 0, 8), 8), 8
            )
            t = [Q(0)] + substitution(d0, root, 8)[:8]
            numerator = [Q(1)] + [-value for value in t[1:]]
            denominator = [Q(1)] + t[1:]
            raw = convolution(numerator, reciprocal(denominator, 8), 8)
            self.assertEqual(coefficients(row["raw_Theta0_small_root"]), raw)
            self.assertEqual(
                coefficients(row["raw_Theta0_small_root_squared"]),
                convolution(raw, raw, 8),
            )
            r, a = mu[2] / mu[0], mu[8] / (3 * mu[6])
            self.assertEqual(raw[2], -2 * r)
            self.assertEqual(raw[4], 3 * r * r - 2 * r * a - mu[4] / (3 * mu[0]))

    def test_20_single_atom_closed_form_all_small_branch_coefficients(self):
        # Algebraic coefficient identities only: no atanh or actual-Xi evaluation.
        for u, weight in ((Q(1), Q(1)), (Q(2, 3), Q(7, 5)), (Q(3), Q(1, 7))):
            row = M.moment_control([u], [weight], 8)
            root = [u ** (n - 1) / n if n % 2 else Q(0) for n in range(9)]
            raw = [Q(1)] + [
                2 * (-u * u) ** (n // 2) if n % 2 == 0 else Q(0) for n in range(1, 9)
            ]
            square = [Q(1)] + [
                2 * n * (-u * u) ** (n // 2) if n % 2 == 0 else Q(0)
                for n in range(1, 9)
            ]
            self.assertEqual(coefficients(row["small_root"]), root)
            self.assertEqual(coefficients(row["raw_Theta0_small_root"]), raw)
            self.assertEqual(coefficients(row["raw_Theta0_small_root_squared"]), square)
            self.assertEqual(
                coefficients(row["covariance_K"]), [4 * weight**2 * u**6] + [Q(0)] * 8
            )

    def test_21_atom_count_positivity_duplicates_and_cutoff_guards(self):
        for nodes, weights in (
            ([], []),
            ([1], []),
            ([1, 2], [1]),
            ([1] * 5, [1] * 5),
            ([1, 1], [1, 2]),
            ([0], [1]),
            ([-1], [1]),
            ([1], [0]),
            ([1], [-1]),
            ([True], [1]),
            ([1], [True]),
            ([1.0], [1]),
            ([1], [Q(1, 2**16)]),
            ([2**16], [1]),
            ({1}, [1]),
        ):
            with self.assertRaises(ValueError):
                M.moment_control(nodes, weights)
        for cut in (True, 4.0, 3, 9):
            with self.assertRaises(ValueError):
                M.moment_control([1], [1], cut)

    def test_22_six_frozen_sources_and_four_artifact_hashes(self):
        M.authenticate()
        self.assertEqual(len(M.BINDINGS), 6)
        self.assertEqual(len({(row["commit"], row["path"]) for row in M.BINDINGS}), 6)
        self.assertEqual(
            {row["id"]: row["commit"] for row in M.BINDINGS},
            {
                "GH": "9da33e7ea2b15a4badb3cb436e38e54762ad5e1d",
                "XL": "3b6972320899a82c6caa3a98e2ada5ff703a605a",
                "IW": "ef7bbb8dca978269f24e7ff9d97b6dceeed5b460",
                "L106620": "81d52e569cc8bb566e54043fd692fd6157406aab",
                "T106620": "81d52e569cc8bb566e54043fd692fd6157406aab",
                "CP": "7aed2ec0b99b9d7f2fb94a774922a83d5b84a870",
            },
        )
        artifacts = M.artifact_hashes()
        self.assertEqual(len(artifacts), 4)
        self.assertEqual(self.report["artifact_sha256_lf"], artifacts)
        for path, digest in artifacts.items():
            raw = (
                (ROOT / path).read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            )
            self.assertEqual(hashlib.sha256(raw).hexdigest(), digest)

    def test_23_manifest_full_typed_comparison(self):
        manifest = M.expected_manifest()
        self.assertEqual(M.parse_json(M.MANIFEST.read_bytes()), manifest)
        for key in ("id", "commit", "path", "role", "git_blob", "sha256_lf"):
            data = copy.deepcopy(manifest)
            data["frozen_sources"][0][key] = "forged"
            with self.assertRaises(ValueError):
                M.authenticate(data)
        for key in ("schema", "authoring_base"):
            data = copy.deepcopy(manifest)
            data[key] = "forged"
            with self.assertRaises(ValueError):
                M.authenticate(data)
        data = copy.deepcopy(manifest)
        data["unknown"] = True
        with self.assertRaises(ValueError):
            M.authenticate(data)
        for key in manifest["primitive_contract"]:
            data = copy.deepcopy(manifest)
            data["primitive_contract"][key] = "forged source normalization"
            with self.assertRaises(ValueError):
                M.authenticate(data)
        data = copy.deepcopy(manifest)
        data["external_context"]["remote_bytes_authenticated"] = 0
        with self.assertRaises(ValueError):
            M.authenticate(data)
        manifest["frozen_sources"][0]["commit"] = "forged"
        self.assertNotEqual(
            M.expected_manifest()["frozen_sources"][0]["commit"], "forged"
        )

    def test_24_primitive_identity_and_byte_cap_fail_closed(self):
        with (
            patch.object(M.subprocess, "check_output", side_effect=[b"1", b"x"]),
            self.assertRaisesRegex(ValueError, "primitive identity"),
        ):
            M.authenticate()
        read_bytes = Path.read_bytes
        for forbidden in (b"\x00", b"\x07", b"\x1b", b"\x1f"):

            def altered_bytes(path, forbidden=forbidden):
                return (
                    read_bytes(path) + forbidden if path == M.NOTE else read_bytes(path)
                )

            with (
                patch.object(Path, "read_bytes", altered_bytes),
                self.assertRaisesRegex(ValueError, "artifact C0 control"),
            ):
                M.artifact_hashes()
        with patch.object(
            M.subprocess, "check_output", return_value=b"2000001"
        ) as mocked:
            with self.assertRaisesRegex(ValueError, "byte cap"):
                M.authenticate()
            self.assertEqual(mocked.call_count, 1)
        with (
            patch.object(M, "MANIFEST", ROOT / "missing-axis-source-manifest.json"),
            self.assertRaises(FileNotFoundError),
        ):
            M.authenticate()

    def test_25_json_rejects_nonexact_duplicate_and_oversized_values(self):
        for raw in (
            b'{"x":1,"x":2}',
            b'{"x":NaN}',
            b'{"x":Infinity}',
            b'{"x":-Infinity}',
            b'{"x":1.0}',
            b'{"x":1e3}',
            b"{} trailing",
            b"\xff",
            b" " * 2000001,
            b"[" * 26 + b"0" + b"]" * 26,
        ):
            with self.assertRaises(ValueError):
                M.parse_json(raw)
        for data in (
            [0] * 1025,
            {"x": "a" * 4097},
            2**4096,
            {1: "x"},
            {True: 1},
            Q(1, 2),
            1.0,
            complex(1),
            {"x" * 4097: 1},
        ):
            with self.assertRaises(ValueError):
                M.canonical(data)
        self.assertNotEqual(M.canonical({"x": True}), M.canonical({"x": 1}))
        for data in (
            {str(n): 0 for n in range(1025)},
            {str(n): "a" * 4096 for n in range(500)},
        ):
            with self.assertRaises(ValueError):
                M.canonical(data)

    def test_26_lf_normalization_and_seal_authentication(self):
        self.assertEqual(M.normalized(b"a\r\nb\r"), b"a\nb\n")
        for raw in ("not bytes", b"\xff", b"x" * 2000001):
            with self.assertRaises(ValueError):
                M.normalized(raw)
        payload = {"label": "independent seal", "exact": [1, "2/3", True]}
        expected = hashlib.sha256(
            json.dumps(
                payload, sort_keys=True, separators=(",", ":"), allow_nan=False
            ).encode()
        ).hexdigest()
        self.assertEqual(M.seal(payload), {**payload, "payload_sha256": expected})
        self.assertNotIn("payload_sha256", payload)
        with self.assertRaises(ValueError):
            M.seal(self.report)
        data = copy.deepcopy(self.report)
        data["payload_sha256"] = "0" * 64
        with self.assertRaises(ValueError):
            M.validate_report(data)

    def test_27_fixture_complete_reconstruction(self):
        fixture = M.parse_json(M.FIXTURE.read_bytes())
        self.assertEqual(M.canonical(fixture), M.canonical(self.report))
        M.validate_report(fixture)

    def test_28_resealed_pair_moment_and_large_branch_math_tamper(self):
        variants = []
        for field in ("even_coefficients", "odd_derivative_coefficients"):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data["pair_controls"][1][field][2] = "-1"
            variants.append(data)
        data = copy.deepcopy(self.report)
        data.pop("payload_sha256")
        data["pair_controls"][0]["full_quadrant_factor"] = "1/2"
        variants.append(data)
        for field in (
            "moments",
            "y_D5",
            "lambda_of_y",
            "small_root",
            "raw_Theta0_small_root",
            "raw_Theta0_small_root_squared",
            "covariance_K",
        ):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            old = data["moment_controls"][1][field][2]
            data["moment_controls"][1][field][2] = str(Q(old) + 1)
            variants.append(data)
        data = copy.deepcopy(self.report)
        data.pop("payload_sha256")
        data["large_branch_constants"]["root_gap_coefficient_times_lambda"] = "10"
        variants.append(data)
        with patch.object(M, "build_report", return_value=self.report):
            for data in variants:
                with self.assertRaisesRegex(
                    ValueError, "complete typed reconstruction"
                ):
                    M.validate_report(M.seal(data))

    def test_29_resealed_scope_type_source_and_artifact_tamper(self):
        for section, key, value in (
            ("scope", "global_HS_divergence_proved", True),
            ("scope", "high_T_geographic_direction", True),
            ("scope", "reduced_large_branch_sample_tends_zero_proved", True),
            ("scope", "actual_Xi_numerical_samples", False),
            ("scope", "inner_physical_interpretation_conditional", 1),
            ("axis_classification", "common_positive_axis_zeros", False),
            ("axis_classification", "Theta5_at_threshold", "one simple zero"),
            ("caps", "work", True),
            ("rounding_contract", "transcendental_or_Xi_samples", False),
        ):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            data[section][key] = value
            with (
                patch.object(M, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                M.validate_report(M.seal(data))
        for attack in ("source", "artifact", "unknown", "missing"):
            data = copy.deepcopy(self.report)
            data.pop("payload_sha256")
            if attack == "source":
                data["frozen_sources"][0]["role"] = "forged"
            elif attack == "artifact":
                key = next(iter(data["artifact_sha256_lf"]))
                data["artifact_sha256_lf"][key] = "0" * 64
            elif attack == "unknown":
                data["unknown"] = True
            else:
                data.pop("scope")
            with (
                patch.object(M, "build_report", return_value=self.report),
                self.assertRaises(ValueError),
            ):
                M.validate_report(M.seal(data))

    def test_30_leading_constants_scope_taxonomy_and_coverage(self):
        constants = self.report["large_branch_constants"]
        self.assertEqual(
            {
                key: Q(constants[key])
                for key in (
                    "D5_minus_D0_coefficient_over_y_log_y",
                    "D0_derivative_coefficient_over_y",
                    "root_gap_coefficient_over_log_y",
                    "lambda_log_y_limit",
                    "root_gap_coefficient_times_lambda",
                    "raw_large_coefficient_lambda_over_y_log_y",
                    "raw_large_coefficient_over_y_log_y_squared",
                )
            },
            {
                "D5_minus_D0_coefficient_over_y_log_y": Q(5),
                "D0_derivative_coefficient_over_y": Q(1, 2),
                "root_gap_coefficient_over_log_y": Q(10),
                "lambda_log_y_limit": Q(2),
                "root_gap_coefficient_times_lambda": Q(5),
                "raw_large_coefficient_lambda_over_y_log_y": Q(5, 2),
                "raw_large_coefficient_over_y_log_y_squared": Q(5),
            },
        )
        self.assertIs(constants["reduced_U_large_upper_bound_inferred"], False)
        scope = self.report["scope"]
        for key in (
            "inner_physical_interpretation_conditional",
            "actual_source_preserved",
            "native_global_operator_norm_tends_one",
            "single_axis_direction_only",
        ):
            self.assertIs(scope[key], True)
        for key in (
            "axis_theorem_uses_RH",
            "high_T_geographic_direction",
            "global_HS_divergence_proved",
            "reduced_large_branch_sample_tends_zero_proved",
            "off_axis_common_divisor_control",
            "native_Riesz_or_confluent_sampling_bound",
            "cofinal_or_free_energy_closure",
            "RH_or_GRH_claim",
            "analytic_limits_machine_certified",
            "novelty_claim",
        ):
            self.assertIs(scope[key], False)
        self.assertIs(type(scope["actual_Xi_numerical_samples"]), int)
        self.assertEqual(scope["actual_Xi_numerical_samples"], 0)
        self.assertEqual(self.report["arithmetic_class"], "MIXED")
        self.assertEqual(
            self.report["arithmetic_components"],
            ["EXACT_RATIONAL", "CERTIFIED_INTEGER_COVERAGE"],
        )
        self.assertEqual(self.report["rounding_contract"]["rounding"], "none")
        self.assertEqual(self.report["coverage"]["pairs"], 7)
        self.assertEqual(self.report["coverage"]["moment_models"], 6)
        self.assertLessEqual(self.report["coverage"]["charged_work"], 200000)
        self.assertEqual(
            self.report["caps"],
            {
                "degree": 20,
                "cutoff": 8,
                "atoms": 4,
                "input_bits": 16,
                "internal_bits": 4096,
                "work": 200000,
                "bytes": 2000000,
            },
        )

    def test_31_no_assert_float_complex_transcendental_or_control_bytes(self):
        tree = ast.parse(SOURCE.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
        self.assertFalse(
            any(
                isinstance(node, ast.Constant) and type(node.value) in (float, complex)
                for node in ast.walk(tree)
            )
        )
        prohibited = {
            "exp",
            "log",
            "sqrt",
            "gamma",
            "sin",
            "cos",
            "sinh",
            "cosh",
            "tanh",
            "atanh",
            "complex",
            "float",
        }
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                name = (
                    node.func.id
                    if isinstance(node.func, ast.Name)
                    else node.func.attr
                    if isinstance(node.func, ast.Attribute)
                    else ""
                )
                self.assertNotIn(name, prohibited)
        for path in (M.NOTE, SOURCE, Path(__file__).resolve()):
            self.assertFalse(
                [
                    value
                    for value in path.read_bytes()
                    if value < 32 and value not in (9, 10, 13)
                ]
            )

    def test_32_optimized_python_hostile_inputs_and_resealed_scope(self):
        script = """
import importlib.util
import sys
spec = importlib.util.spec_from_file_location('optimized_axis', sys.argv[1])
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
checks = [
    lambda: m.rational(True),
    lambda: m.pair_control(1, 2, True),
    lambda: m.moment_control([1], [1.0]),
    lambda: m.inverse_series([0, 1], 6),
    lambda: m.revert_series([1, 1], 6),
    lambda: m.multiply([1, 1], [1, 1], 6, m.Budget(1)),
    lambda: m.parse_json(b'{"x":1,"x":2}'),
    lambda: m.canonical({'x': 1.0}),
]
for index, check in enumerate(checks):
    try:
        check()
    except ValueError:
        pass
    else:
        raise SystemExit('optimized guard accepted attack ' + str(index))
report = m.build_report()
report.pop('payload_sha256')
report['scope']['actual_Xi_numerical_samples'] = False
try:
    m.validate_report(m.seal(report))
except ValueError:
    pass
else:
    raise SystemExit('optimized reconstruction accepted bool-for-int scope')
print('OPTIMIZED_AXIS_GUARDS_PASS')
"""
        result = subprocess.run(
            [sys.executable, "-I", "-B", "-O", "-c", script, str(SOURCE)],
            check=False,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), "OPTIMIZED_AXIS_GUARDS_PASS")


if __name__ == "__main__":
    unittest.main()
