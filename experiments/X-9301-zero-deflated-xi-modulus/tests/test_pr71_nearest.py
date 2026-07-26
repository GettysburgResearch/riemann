from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def import_module(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


BUILD = import_module("build_pr71_nearest_certificate")
COMPARE = import_module("compare_pr71_zero_block")
VERIFY = import_module("verify_zero_deflated_modulus")


def rational(numerator, denominator=1):
    return {"numerator": numerator, "denominator": denominator}


def binary(mantissa, exponent):
    return {"mantissa": str(mantissa), "exponent": str(exponent)}


def ball(lower, upper, exponent=-2):
    return {
        "lower": binary(lower, exponent),
        "upper": binary(upper, exponent),
    }


class NearestZeroTests(unittest.TestCase):
    def primitives(self):
        return {
            "schema": BUILD.PRIMITIVE_SCHEMA,
            "normalization_id": BUILD.NORMALIZATION,
            "precision_bits": 192,
            "ordinate": rational(10),
            "points": [
                {
                    "id": "x-2",
                    "x": rational(1, 4),
                    "xi_rectangle": {
                        "real": {"lower": rational(1), "upper": rational(1)},
                        "imag": {"lower": rational(0), "upper": rational(0)},
                    },
                    "functional_equation_residual_contains_zero": True,
                },
                {
                    "id": "x-1",
                    "x": rational(1, 2),
                    "xi_rectangle": {
                        "real": {"lower": rational(2), "upper": rational(2)},
                        "imag": {"lower": rational(0), "upper": rational(0)},
                    },
                    "functional_equation_residual_contains_zero": True,
                },
            ],
        }

    def block(self, precision=192, widen=0):
        intervals = [(28, 29), (36, 37), (44, 45), (50, 51)]
        return {
            "schema": BUILD.BLOCK_SCHEMA,
            "classification": "CERTIFIED_CRITICAL_LINE_ZERO_BLOCK",
            "precision_bits": precision,
            "target": rational(10),
            "requested_start_index": "100",
            "requested_length": 4,
            "returned_count": 4,
            "target_below_zero_index": "101",
            "target_above_zero_index": "102",
            "zeros": [
                {
                    "zero_index": str(100 + index),
                    "ball": ball(lower - widen, upper + widen),
                }
                for index, (lower, upper) in enumerate(intervals)
            ],
        }

    def config(self):
        return {
            "schema": BUILD.CONFIG_SCHEMA,
            "rows": [
                {
                    "id": "m",
                    "kind": "deflated-monotonicity",
                    "left": "x-2",
                    "right": "x-1",
                }
            ],
        }

    def test_selects_nearest_by_certified_upper_distance(self):
        output = BUILD.build(self.primitives(), self.block(), self.config(), 2)
        self.assertEqual(len(output["zero_bins"]), 2)
        self.assertEqual(set(output["source"]["selected_zero_indices"]), {101, 102})
        bindings = VERIFY.verify_source_artifacts(
            output, self.primitives(), self.block()
        )
        self.assertEqual(
            bindings["zero-block_sha256"],
            output["source"]["zero_block_sha256"],
        )

    def test_rehashed_selected_index_drift_is_rejected(self):
        primitives, block = self.primitives(), self.block()
        output = BUILD.build(primitives, block, self.config(), 2)
        output["source"]["selected_zero_indices"].reverse()
        body = dict(output)
        body.pop("certificate_sha256")
        output["certificate_sha256"] = BUILD.canonical_sha(body)
        with self.assertRaisesRegex(
            VERIFY.CertificateError, "selected zero indices"
        ):
            VERIFY.verify_source_artifacts(output, primitives, block)

    def test_excess_nearest_count_rejected(self):
        with self.assertRaises(BUILD.BuildError):
            BUILD.build(self.primitives(), self.block(), self.config(), 5)

    def test_precision_block_nesting(self):
        result = COMPARE.compare(self.block(192, 1), self.block(256, 0))
        self.assertTrue(result["all_high_balls_nested"])

    def test_zero_index_drift_rejected(self):
        high = self.block(256, 0)
        high["zeros"][0]["zero_index"] = "999"
        with self.assertRaises(COMPARE.ComparisonError):
            COMPARE.compare(self.block(192, 1), high)


if __name__ == "__main__":
    unittest.main()
