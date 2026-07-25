from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "verify_operator_budget.py"
SPEC = importlib.util.spec_from_file_location("verify_operator_budget", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
verify_operator_budget = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verify_operator_budget)


def fraction(numerator: int, denominator: int) -> dict[str, str]:
    return {"numerator": str(numerator), "denominator": str(denominator)}


def certificate() -> dict[str, object]:
    return {
        "schema": verify_operator_budget.SCHEMA,
        "status": "STATIC_CONDITIONAL_BUDGET_NOT_A_PRODUCTION_RUN",
        "claims_complete_coefficient_run": False,
        "arithmetic_contract": verify_operator_budget.ARITHMETIC_CONTRACT,
        "term_count_upper": 4_200_000_000,
        "hardware_units_per_term": 256,
        "binary80_mantissa_bits": 64,
        "pairwise_depth": 64,
        "amplitude_sum_upper": 11_000_001,
        "guarded_support_boundary_count": 0,
        "phase_location_budget": fraction(1, 10**12),
        "phase_taylor_budget": fraction(1, 20_000_000_000),
        "algebraic_budget": fraction(1, 90_000_000_000_000),
        "required_upper": fraction(1, 17_000_000),
        "claimed_total": fraction(
            8671901269709261619909050612478389,
            148552804714245632472498831360000000000000,
        ),
    }


class OperatorBudgetTests(unittest.TestCase):
    def test_target_budget_passes(self) -> None:
        result = verify_operator_budget.verify(certificate())
        self.assertTrue(result["verified"])
        self.assertEqual(
            result["components"]["hardware_term_sum"],
            fraction(8_203_125, 140_737_488_355_328),
        )

    def test_guarded_boundary_requires_fallback(self) -> None:
        mutated = certificate()
        mutated["guarded_support_boundary_count"] = 1
        with self.assertRaises(verify_operator_budget.CertificateError):
            verify_operator_budget.verify(mutated)

    def test_false_production_claim_is_rejected(self) -> None:
        mutated = certificate()
        mutated["claims_complete_coefficient_run"] = True
        with self.assertRaises(verify_operator_budget.CertificateError):
            verify_operator_budget.verify(mutated)

    def test_understated_total_is_rejected(self) -> None:
        mutated = certificate()
        mutated["claimed_total"] = fraction(1, 10**9)
        with self.assertRaises(verify_operator_budget.CertificateError):
            verify_operator_budget.verify(mutated)

    def test_tighter_unsupported_threshold_is_rejected(self) -> None:
        mutated = certificate()
        mutated["required_upper"] = fraction(1, 20_000_000)
        with self.assertRaises(verify_operator_budget.CertificateError):
            verify_operator_budget.verify(mutated)

    def test_arithmetic_contract_drift_is_rejected(self) -> None:
        mutated = certificate()
        mutated["arithmetic_contract"] = "fast-math enabled"
        with self.assertRaises(verify_operator_budget.CertificateError):
            verify_operator_budget.verify(mutated)

    def test_boolean_term_count_is_rejected(self) -> None:
        mutated = certificate()
        mutated["term_count_upper"] = True
        with self.assertRaises(verify_operator_budget.CertificateError):
            verify_operator_budget.verify(mutated)


if __name__ == "__main__":
    unittest.main()
