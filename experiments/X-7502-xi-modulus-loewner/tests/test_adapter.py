from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


ADAPTER = load_module(
    "adapt_modulus_certificate", ROOT / "adapt_modulus_certificate.py"
)
VERIFY = load_module(
    "verify_log_loewner_adapter_test", ROOT / "verify_log_loewner.py"
)


class AdapterTests(unittest.TestCase):
    def source(self):
        points = []
        for identifier, x, real in [
            ("a", 1, 1),
            ("b", 2, 2),
            ("c", 3, 3),
            ("d", 4, 4),
        ]:
            points.append(
                {
                    "id": identifier,
                    "x": {"numerator": x, "denominator": 1},
                    "xi_rectangle": {
                        "real": {
                            "lower": {"numerator": real, "denominator": 1},
                            "upper": {"numerator": real, "denominator": 1},
                        },
                        "imag": {
                            "lower": {"numerator": 0, "denominator": 1},
                            "upper": {"numerator": 0, "denominator": 1},
                        },
                    },
                }
            )
        return {
            "schema": "riemann.xi-modulus-witness.v1",
            "classification": "SYNTHETIC_MODEL",
            "normalization_id": "riemann-xi-standard-half-s-sminus1-v1",
            "certificate_sha256": "synthetic",
            "points": points,
        }

    def manifest(self):
        return {
            "schema": "riemann.xi-modulus-log-loewner-manifest.v1",
            "normalization_id": "riemann-xi-standard-half-s-sminus1-v1",
            "log_series_terms": 64,
            "rows": [
                {
                    "id": "r",
                    "kind": "cross-log-loewner-minor",
                    "row_points": ["a", "c"],
                    "column_points": ["b", "d"],
                }
            ],
        }

    def test_adapter_binds_and_verifies(self):
        adapted = ADAPTER.adapt(self.source(), self.manifest())
        self.assertEqual(
            adapted["points"][1]["u"], {"numerator": 4, "denominator": 1}
        )
        result = VERIFY.verify(adapted)
        self.assertEqual(result["unresolved_rows"], 0)

    def test_unknown_point_rejected(self):
        manifest = self.manifest()
        manifest["rows"][0]["column_points"][1] = "missing"
        with self.assertRaises(ADAPTER.AdapterError):
            ADAPTER.adapt(self.source(), manifest)


if __name__ == "__main__":
    unittest.main()
