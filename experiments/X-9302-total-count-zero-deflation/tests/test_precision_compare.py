from __future__ import annotations

import copy
import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


adapter = load_module(
    "build_total_count_certificate_compare",
    ROOT / "build_pr71_total_count_certificate.py",
)
compare = load_module(
    "compare_total_deflation_precision_test",
    ROOT / "compare_total_deflation_precision.py",
)


def exact_binary(value: int) -> dict:
    endpoint = {"mantissa": str(value), "exponent": "0"}
    return {"lower": dict(endpoint), "upper": dict(endpoint)}


def fixtures() -> tuple[dict, dict, dict]:
    points = []
    for x in (1, 2, 3, 4):
        u = x * x
        value = (u - 5) * (u + 1) ** 10
        points.append(
            {
                "id": f"x{x}",
                "x": {"numerator": x, "denominator": 1},
                "xi_rectangle": {
                    "real": {
                        "lower": {"numerator": value, "denominator": 1},
                        "upper": {"numerator": value, "denominator": 1},
                    },
                    "imag": {
                        "lower": {"numerator": 0, "denominator": 1},
                        "upper": {"numerator": 0, "denominator": 1},
                    },
                },
                "functional_equation_residual_contains_zero": True,
            }
        )
    primitives = {
        "schema": adapter.PRIMITIVE_SCHEMA,
        "normalization_id": adapter.NORMALIZATION,
        "ordinate": {"numerator": 10, "denominator": 1},
        "points": points,
    }
    counts = {
        "schema": adapter.COUNT_SCHEMA,
        "classification": adapter.COUNT_CLASSIFICATION,
        "target": {"numerator": "10", "denominator": "1"},
        "windows": [
            {
                "id": "r_p0",
                "radius": {"numerator": "1", "denominator": "1"},
                "lower_endpoint": exact_binary(9),
                "upper_endpoint": exact_binary(11),
                "N_lower_ball": exact_binary(100),
                "N_upper_ball": exact_binary(120),
                "N_lower": "100",
                "N_upper": "120",
                "count_lower": "20",
            }
        ],
    }
    config = {
        "schema": adapter.CONFIG_SCHEMA,
        "normalization_id": adapter.NORMALIZATION,
        "log_terms": 192,
        "rows": [
            {
                "id": "d2",
                "kind": "deflated-cross-loewner-determinant",
                "rows": ["x1", "x3"],
                "columns": ["x2", "x4"],
            }
        ],
    }
    return primitives, counts, config


class PrecisionComparisonTests(unittest.TestCase):
    def setUp(self) -> None:
        primitives, counts, config = fixtures()
        low_primitives = copy.deepcopy(primitives)
        high_primitives = copy.deepcopy(primitives)
        low_counts = copy.deepcopy(counts)
        high_counts = copy.deepcopy(counts)
        low_primitives["precision_bits"] = 192
        high_primitives["precision_bits"] = 256
        low_counts["precision_bits"] = 192
        high_counts["precision_bits"] = 256
        self.low = adapter.build(low_primitives, low_counts, copy.deepcopy(config))
        self.high = adapter.build(
            high_primitives, high_counts, copy.deepcopy(config)
        )

    def test_precision_specific_gate_digests_are_allowed(self) -> None:
        self.assertNotEqual(
            self.low["count_windows"][0]["gate"]["sha256"],
            self.high["count_windows"][0]["gate"]["sha256"],
        )
        result = compare.compare(self.low, self.high)
        self.assertTrue(result["all_high_intervals_nested"])
        self.assertEqual(result["stable_count_windows"], 1)

    def test_semantic_count_change_is_rejected(self) -> None:
        self.high["count_windows"][0]["count_lower"] = 19
        with self.assertRaisesRegex(compare.ComparisonError, "semantic field"):
            compare.compare(self.low, self.high)


if __name__ == "__main__":
    unittest.main()
