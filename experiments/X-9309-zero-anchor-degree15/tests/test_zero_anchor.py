from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


check = load("zero_anchor_check", "verify_zero_anchor.py")
patcher = load("zero_anchor_patcher", "build_zero_anchor_source.py")


def polynomial_add(left, right):
    out = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def polynomial_multiply(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def response(nodes, beta):
    out = [Fraction(0)]
    for i, coefficient in enumerate(beta):
        term = [Fraction(1)]
        for j, node in enumerate(nodes):
            if i != j:
                term = polynomial_multiply(term, [node, Fraction(1)])
        out = polynomial_add(out, [-coefficient * value for value in term])
    return out


class ZeroAnchorTests(unittest.TestCase):
    def test_zero_extension_shifts_response_degree(self):
        old_nodes = [Fraction(1), Fraction(2), Fraction(4), Fraction(8)]
        new_nodes = [Fraction(0)] + old_nodes
        for degree in range(len(old_nodes) - 1):
            old_beta = check.basis_vector(old_nodes, degree)
            extended = [Fraction(0)] + old_beta
            expected = [Fraction(0)] * (degree + 1) + [Fraction(1)]
            self.assertEqual(response(new_nodes, extended), expected)

    def test_new_basis_is_zero_sum_and_response_one(self):
        nodes = [Fraction(0), Fraction(1), Fraction(3), Fraction(7)]
        beta = check.basis_vector(nodes, 0)
        self.assertEqual(sum(beta), 0)
        self.assertEqual(response(nodes, beta), [Fraction(1)])

    def test_positive_moment_model_passes_ldl(self):
        support = [Fraction(i) for i in range(1, 9)]
        b = [sum(y**k for y in support) for k in range(16)]
        h0 = check.hankel(b, 8, 0)
        h1 = check.hankel(b, 8, 1)
        self.assertEqual(len(check.exact_ldl_positive_pivots(h0)), 8)
        self.assertEqual(len(check.exact_ldl_positive_pivots(h1)), 8)

    def test_schur_vector_exposes_lowered_b0(self):
        support = [Fraction(i) for i in range(1, 9)]
        b = [sum(y**k for y in support) for k in range(16)]
        a = b[1:]
        block = [[a[i + j + 1] for j in range(7)] for i in range(7)]
        vector = [a[i] for i in range(7)]
        solution = check.solve_linear(block, vector)
        theta = sum(x * y for x, y in zip(vector, solution))
        b[0] = theta - Fraction(1, 10)
        h0 = check.hankel(b, 8, 0)
        witness = [Fraction(1)] + [-value for value in solution]
        interval = check.interval_quadratic(h0, h0, witness)
        self.assertEqual(interval.lower, Fraction(-1, 10))
        self.assertEqual(interval.upper, Fraction(-1, 10))

    def test_zero_primitive_requires_positive_modulus(self):
        primitive = {
            "normalization_id": check.NORMALIZATION,
            "points": [{
                "x": {"numerator": 0, "denominator": 1},
                "functional_equation_residual_contains_zero": True,
                "xi_rectangle": {
                    "real": {
                        "lower": {"numerator": -1, "denominator": 1},
                        "upper": {"numerator": 1, "denominator": 1},
                    },
                    "imag": {
                        "lower": {"numerator": -1, "denominator": 1},
                        "upper": {"numerator": 1, "denominator": 1},
                    },
                },
            }],
        }
        with self.assertRaises(check.CertificateError):
            check.zero_point(primitive, "control")

    def test_precision_nesting_rejects_wider_high_interval(self):
        def primitive(precision, lower, upper):
            return {
                "precision_bits": precision,
                "normalization_id": check.NORMALIZATION,
                "common_xi_scale_power_of_two": 0,
                "ordinate": {"numerator": 1, "denominator": 1},
                "points": [{
                    "x": {"numerator": 0, "denominator": 1},
                    "functional_equation_residual_contains_zero": True,
                    "xi_rectangle": {
                        "real": {
                            "lower": {"numerator": lower, "denominator": 1},
                            "upper": {"numerator": upper, "denominator": 1},
                        },
                        "imag": {
                            "lower": {"numerator": 0, "denominator": 1},
                            "upper": {"numerator": 0, "denominator": 1},
                        },
                    },
                }],
            }
        with self.assertRaises(check.CertificateError):
            check.compare_zero_primitives(primitive(128, 1, 2), primitive(256, 1, 3))

    def test_source_patch_is_exact_and_idempotence_guarded(self):
        source = (
            "#define X_COUNT 2\n"
            "static const int X_BITS[X_COUNT] = {2, 1};\n"
            + patcher.SET_X_NEEDLE
            + patcher.DENOMINATOR_NEEDLE
            + patcher.PRINT_NEEDLE
        )
        output, manifest = patcher.patch(source)
        self.assertIn("x-critical-line", output)
        self.assertIn("{-1}", output)
        self.assertEqual(manifest["emitted_point_count"], 1)
        with self.assertRaises(ValueError):
            patcher.patch(output)


if __name__ == "__main__":
    unittest.main()
