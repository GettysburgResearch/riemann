from __future__ import annotations

import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("threshold_verify", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
threshold_verify = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(threshold_verify)


def fraction(numerator: int, denominator: int = 1) -> dict[str, str]:
    return {"numerator": str(numerator), "denominator": str(denominator)}


def manifest() -> dict[str, object]:
    rows = [(0, 0) for _ in range(1025)]
    rows[0] = (1_000_000_000, 0)
    rows[1023] = (500, 0)
    return {
        "metadata": {
            "cells": "1024",
            "vector_scale_bits": "96",
            "autocorr_scale_bits": "192",
            "vector_sha256": threshold_verify.EXPECTED_VECTOR,
            "normalization_sha256": threshold_verify.EXPECTED_NORMALIZATION,
            "parameter_sha256": threshold_verify.EXPECTED_PARAMETER,
            "cutoff_power10": "11",
            "cutoff": "100000000000",
            "carrier_num": "94184072727073",
            "carrier_den": "20",
            "segment_size": "20000000",
            "total_segments": "5000",
            "a_count": "1025",
        },
        "autocorrelations": rows,
    }


def manifest_text(value: dict[str, object]) -> str:
    metadata = value["metadata"]
    rows = value["autocorrelations"]
    lines = [threshold_verify.MANIFEST_MAGIC]
    order = [
        "cells",
        "vector_scale_bits",
        "autocorr_scale_bits",
        "vector_sha256",
        "normalization_sha256",
        "parameter_sha256",
        "cutoff_power10",
        "cutoff",
        "carrier_num",
        "carrier_den",
        "segment_size",
        "total_segments",
        "a_count",
    ]
    lines.extend(f"{key} {metadata[key]}" for key in order)
    lines.extend(f"a {lag} {real} {imag}" for lag, (real, imag) in enumerate(rows))
    return "\n".join(lines) + "\n"


def verdict() -> dict[str, object]:
    return {
        "schema": threshold_verify.VERDICT_SCHEMA,
        "verdict": "CERTIFIED_POSITIVE_FIXED_VECTOR",
        "vector_sha256": threshold_verify.EXPECTED_VECTOR,
        "normalization_sha256": threshold_verify.EXPECTED_NORMALIZATION,
        "parameter_sha256": threshold_verify.EXPECTED_PARAMETER,
        "full_exact_quadratic_interval": {
            "lower": fraction(1, 3000),
            "upper": fraction(1, 2999),
        },
        "vector_norm_squared": fraction(1),
    }


class ThresholdInsusceptibilityTests(unittest.TestCase):
    def test_exact_control_passes(self) -> None:
        result = threshold_verify.verify(manifest(), verdict())
        self.assertTrue(result["verified"])
        self.assertEqual(
            result["first_cell_event"]["maximum_fraction_of_coarse_moat"],
            fraction(1, 9_000_000),
        )

    def test_large_endpoint_product_is_rejected(self) -> None:
        mutated = manifest()
        mutated["autocorrelations"][1023] = (2_000, 0)
        with self.assertRaises(threshold_verify.CertificateError):
            threshold_verify.verify(mutated, verdict())

    def test_small_directional_moat_is_rejected(self) -> None:
        mutated = verdict()
        mutated["full_exact_quadratic_interval"] = {
            "lower": fraction(1, 5000),
            "upper": fraction(1, 4999),
        }
        with self.assertRaises(threshold_verify.CertificateError):
            threshold_verify.verify(manifest(), mutated)

    def test_fingerprint_mutation_is_rejected(self) -> None:
        mutated = manifest()
        mutated["metadata"]["vector_sha256"] = "00" * 32
        with self.assertRaises(threshold_verify.CertificateError):
            threshold_verify.verify(mutated, verdict())

    def test_nonzero_terminal_row_is_rejected_by_parser(self) -> None:
        mutated = manifest()
        mutated["autocorrelations"][-1] = (1, 0)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.txt"
            path.write_text(manifest_text(mutated), encoding="utf-8")
            with self.assertRaises(threshold_verify.CertificateError):
                threshold_verify.parse_manifest(path)


if __name__ == "__main__":
    unittest.main()
