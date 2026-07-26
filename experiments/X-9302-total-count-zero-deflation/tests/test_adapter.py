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


adapter = load_module("build_total_count_certificate", ROOT / "build_pr71_total_count_certificate.py")
checker = load_module("verify_total_count_deflation_adapter", ROOT / "verify_total_count_deflation.py")


def exact_binary(value: int) -> dict:
    endpoint = {"mantissa": str(value), "exponent": "0"}
    return {"lower": dict(endpoint), "upper": dict(endpoint)}


def fixtures() -> tuple[dict, dict, dict]:
    points = []
    for x, u in ((1, 1), (2, 4), (3, 9), (4, 16)):
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
        "common_xi_scale_power_of_two": 123,
        "ordinate": {"numerator": 10, "denominator": 1},
        "points": points,
    }
    counts = {
        "schema": adapter.COUNT_SCHEMA,
        "classification": adapter.COUNT_CLASSIFICATION,
        "count_interval_convention": adapter.COUNT_INTERVAL_CONVENTION,
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
            {"id": "m", "kind": "deflated-monotonicity", "left": "x1", "right": "x2"},
            {
                "id": "d2",
                "kind": "deflated-cross-loewner-determinant",
                "rows": ["x1", "x3"],
                "columns": ["x2", "x4"],
            },
        ],
    }
    return primitives, counts, config


class AdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.primitives, self.counts, self.config = fixtures()

    @staticmethod
    def resign(certificate: dict) -> None:
        body = copy.deepcopy(certificate)
        body.pop("certificate_sha256", None)
        certificate["certificate_sha256"] = adapter.canonical_sha(body)

    def test_end_to_end_total_count_bridge(self) -> None:
        certificate = adapter.build(
            copy.deepcopy(self.primitives), copy.deepcopy(self.counts), copy.deepcopy(self.config)
        )
        result = checker.verify(certificate)
        self.assertTrue(result["verified"])
        self.assertFalse(result["source_artifacts_verified"])
        self.assertEqual(result["common_xi_scale_power_of_two"], 123)
        self.assertEqual(result["certified_negative_rows"], 2)
        self.assertEqual(result["count_windows"][0]["count_lower"], 20)
        bindings = checker.verify_source_artifacts(
            certificate, self.primitives, self.counts
        )
        self.assertEqual(
            bindings["primitive_sha256"],
            certificate["source"]["primitive_sha256"],
        )

    def test_source_artifact_mutation_is_rejected(self) -> None:
        certificate = adapter.build(
            copy.deepcopy(self.primitives),
            copy.deepcopy(self.counts),
            copy.deepcopy(self.config),
        )
        mutated = copy.deepcopy(self.counts)
        mutated["precision_bits"] = 999
        with self.assertRaisesRegex(
            checker.CertificateError, "total-count artifact digest"
        ):
            checker.verify_source_artifacts(certificate, self.primitives, mutated)

    def test_rehashed_certificate_point_drift_is_rejected(self) -> None:
        certificate = adapter.build(
            copy.deepcopy(self.primitives),
            copy.deepcopy(self.counts),
            copy.deepcopy(self.config),
        )
        point = certificate["points"][0]
        point["xi_rectangle"]["real"]["lower"]["numerator"] += 1
        point["xi_rectangle"]["real"]["upper"]["numerator"] += 1
        canonical = {
            "id": point["id"],
            "u": point["u"],
            "xi_rectangle": point["xi_rectangle"],
        }
        point["point_sha256"] = adapter.canonical_sha(canonical)
        self.resign(certificate)
        with self.assertRaisesRegex(
            checker.CertificateError, "differs from primitive artifact"
        ):
            checker.verify_source_artifacts(
                certificate, self.primitives, self.counts
            )

    def test_rehashed_certificate_count_drift_is_rejected(self) -> None:
        certificate = adapter.build(
            copy.deepcopy(self.primitives),
            copy.deepcopy(self.counts),
            copy.deepcopy(self.config),
        )
        certificate["count_windows"][0]["count_lower"] = 19
        self.resign(certificate)
        with self.assertRaisesRegex(
            checker.CertificateError, "differs from total-count artifact"
        ):
            checker.verify_source_artifacts(
                certificate, self.primitives, self.counts
            )

    def test_missing_count_convention_is_rejected(self) -> None:
        counts = copy.deepcopy(self.counts)
        counts.pop("count_interval_convention")
        self.assert_bridge_rejected(counts, "interval convention")

    def assert_bridge_rejected(self, counts: dict, message: str) -> None:
        with self.assertRaisesRegex(adapter.BridgeError, message):
            adapter.build(copy.deepcopy(self.primitives), counts, copy.deepcopy(self.config))

    def test_nonunique_count_ball_is_rejected(self) -> None:
        counts = copy.deepcopy(self.counts)
        counts["windows"][0]["N_upper_ball"]["lower"]["mantissa"] = "119"
        self.assert_bridge_rejected(counts, "does not isolate one integer")

    def test_false_claimed_count_is_rejected(self) -> None:
        counts = copy.deepcopy(self.counts)
        counts["windows"][0]["count_lower"] = "19"
        self.assert_bridge_rejected(counts, "does not equal")

    def test_endpoint_drift_is_rejected(self) -> None:
        counts = copy.deepcopy(self.counts)
        counts["windows"][0]["upper_endpoint"]["upper"]["mantissa"] = "12"
        self.assert_bridge_rejected(counts, "not exact|do not equal")

    def test_decreasing_nested_count_is_rejected(self) -> None:
        counts = copy.deepcopy(self.counts)
        second = copy.deepcopy(counts["windows"][0])
        second.update(
            {
                "id": "r_p1",
                "radius": {"numerator": "2", "denominator": "1"},
                "lower_endpoint": exact_binary(8),
                "upper_endpoint": exact_binary(12),
                "N_lower_ball": exact_binary(101),
                "N_upper_ball": exact_binary(119),
                "N_lower": "101",
                "N_upper": "119",
                "count_lower": "18",
            }
        )
        counts["windows"].append(second)
        self.assert_bridge_rejected(counts, "not nondecreasing")


if __name__ == "__main__":
    unittest.main()
