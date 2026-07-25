from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify_target_gate.py"
SPEC = importlib.util.spec_from_file_location("verify_target_gate", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
verify_target_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify_target_gate)


def fraction(numerator: int, denominator: int = 1) -> dict[str, str]:
    return {"numerator": str(numerator), "denominator": str(denominator)}


def verdict() -> dict[str, object]:
    return {
        "schema": verify_target_gate.VERDICT_SCHEMA,
        "verdict": "CERTIFIED_POSITIVE_FIXED_VECTOR",
        "certified_positive": True,
        "certified_negative": False,
        "vector_sha256": verify_target_gate.EXPECTED_VECTOR,
        "parameter_sha256": verify_target_gate.EXPECTED_PARAMETER,
        "normalization_sha256": verify_target_gate.EXPECTED_NORMALIZATION,
        "coverage": dict(verify_target_gate.EXPECTED_COUNTS),
        "full_exact_quadratic_interval": {
            "lower": fraction(1, 3000),
            "upper": fraction(1, 2999),
        },
        "vector_norm_squared": fraction(1),
    }


def gate() -> dict[str, object]:
    return {
        "schema": verify_target_gate.GATE_SCHEMA,
        "gate_status": "CONDITIONAL_TARGETS_NOT_YET_PROVED",
        "claims_whole_matrix_certificate": False,
        "directional_baseline": fraction(1, 4000),
        "complement_lower_target": fraction(7, 1000),
        "residual_upper_target": fraction(1, 5000),
        "operator_moat_target": fraction(1, 1000),
    }


class TargetGateTests(unittest.TestCase):
    def test_strict_coarse_gate_passes(self) -> None:
        result = verify_target_gate.verify(verdict(), gate())
        self.assertTrue(result["verified"])
        self.assertEqual(
            result["conditional_targets"]["coarse_schur_margin"],
            fraction(3, 50_000_000),
        )

    def test_equality_or_worse_is_rejected(self) -> None:
        mutated = gate()
        mutated["complement_lower_target"] = fraction(1, 1000)
        with self.assertRaises(verify_target_gate.CertificateError):
            verify_target_gate.verify(verdict(), mutated)

    def test_false_whole_matrix_claim_is_rejected(self) -> None:
        mutated = gate()
        mutated["claims_whole_matrix_certificate"] = True
        with self.assertRaises(verify_target_gate.CertificateError):
            verify_target_gate.verify(verdict(), mutated)

    def test_nonpositive_source_interval_is_rejected(self) -> None:
        mutated = verdict()
        mutated["full_exact_quadratic_interval"] = {
            "lower": fraction(-1, 3000),
            "upper": fraction(1, 3000),
        }
        with self.assertRaises(verify_target_gate.CertificateError):
            verify_target_gate.verify(mutated, gate())

    def test_vector_fingerprint_mutation_is_rejected(self) -> None:
        mutated = verdict()
        mutated["vector_sha256"] = "00" * 32
        with self.assertRaises(verify_target_gate.CertificateError):
            verify_target_gate.verify(mutated, gate())

    def test_boolean_integer_is_rejected(self) -> None:
        mutated = verdict()
        mutated["vector_norm_squared"] = {
            "numerator": "1",
            "denominator": True,
        }
        with self.assertRaises(verify_target_gate.CertificateError):
            verify_target_gate.verify(mutated, gate())


if __name__ == "__main__":
    unittest.main()
