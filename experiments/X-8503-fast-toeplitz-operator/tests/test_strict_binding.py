from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import bind_fast_shard
import merge_hybrid_source_strict
import verify_operator_budget


def fraction(numerator: int, denominator: int = 1) -> dict[str, str]:
    return {"numerator": str(numerator), "denominator": str(denominator)}


PARAMETER_SHA = "33" * 32
NORMALIZATION_SHA = "44" * 32


def budget_certificate() -> dict[str, object]:
    return {
        "schema": verify_operator_budget.SCHEMA,
        "status": "STATIC_CONDITIONAL_BUDGET_NOT_A_PRODUCTION_RUN",
        "claims_complete_coefficient_run": False,
        "arithmetic_contract": verify_operator_budget.ARITHMETIC_CONTRACT,
        "term_count_upper": 1,
        "hardware_units_per_term": 1,
        "binary80_mantissa_bits": 64,
        "pairwise_depth": 1,
        "amplitude_sum_upper": 1,
        "guarded_support_boundary_count": 0,
        "phase_location_budget": fraction(1, 1 << 80),
        "phase_taylor_budget": fraction(1, 1 << 80),
        "algebraic_budget": fraction(1, 1 << 80),
        "required_upper": fraction(1, 1000),
    }


def verified_budget() -> dict[str, object]:
    return verify_operator_budget.verify(budget_certificate())


def plan(budget_sha: str | None = None) -> dict[str, object]:
    if budget_sha is None:
        budget_sha = verified_budget()["verification_sha256"]
    return {
        "schema": merge_hybrid_source_strict.PLAN_SCHEMA,
        "status": "PROOF_PRODUCING_HYBRID_SOURCE_PLAN",
        "cutoff": 100,
        "carrier": "1.5",
        "cells": 2,
        "segment_size": 10,
        "total_segments": 4,
        "fast_start_segment": 2,
        "expected_counts": {
            "prime_count": 6,
            "higher_prime_power_count": 1,
            "total_terms": 7,
        },
        "parameter_sha256": PARAMETER_SHA,
        "normalization_sha256": NORMALIZATION_SHA,
        "fast_budget_verification_sha256": budget_sha,
        "operator_gate": fraction(1, 2),
    }


def raw_fast(start: int = 2, end: int = 4, primes: int = 3) -> dict[str, object]:
    return {
        "schema": bind_fast_shard.RAW_SCHEMA,
        "segment_start": start,
        "segment_end": end,
        "prime_count": primes,
        "higher_prime_power_count": 0,
        "total_terms": primes,
        "include_higher_powers": False,
        "vector_independent": True,
        "source_manifest_vector_sha256": "55" * 32,
        "parameter_sha256": PARAMETER_SHA,
        "normalization_sha256": NORMALIZATION_SHA,
        "phase_grid_M": 32768,
        "phase_taylor_R": 3,
        "log_series_terms": 4,
        "sqrt_polynomial_degree": 5,
        "setup_precision_bits": 192,
        "mpfr_version": "synthetic",
        "arithmetic_contract": bind_fast_shard.ARITHMETIC_CONTRACT,
        "guarded_support_boundary_count": 0,
        "near_phase_boundary_count": 0,
        "minimum_support_boundary_distance": "0.1",
        "minimum_phase_boundary_distance": "0.1",
        "absolute_amplitude_midpoint": fraction(1, 3),
        "lags": [
            {"lag": 0, "real": fraction(1, 5), "imag": fraction(8)},
            {"lag": 1, "real": fraction(1, 7), "imag": fraction(-1, 9)},
        ],
    }


def directed() -> dict[str, object]:
    return {
        "schema": merge_hybrid_source_strict.base.DIRECTED_SCHEMA,
        "cutoff": 100,
        "carrier": "1.5",
        "cells": 2,
        "segment_size": 10,
        "total_segments": 4,
        "segment_start": 0,
        "segment_end": 2,
        "include_higher_powers": True,
        "prime_count": 3,
        "higher_prime_power_count": 1,
        "total_terms": 4,
        "ambiguous_lags": 0,
        "lags": [
            {
                "lag": 0,
                "real_lower_hex": float(1.0).hex(),
                "real_upper_hex": float(1.0).hex(),
                "imag_lower_hex": float(-100.0).hex(),
                "imag_upper_hex": float(100.0).hex(),
            },
            {
                "lag": 1,
                "real_lower_hex": float(0.25).hex(),
                "real_upper_hex": float(0.25).hex(),
                "imag_lower_hex": float(-0.125).hex(),
                "imag_upper_hex": float(-0.125).hex(),
            },
        ],
    }


class StrictBindingTests(unittest.TestCase):
    def test_bound_shard_and_budget_are_replayed(self) -> None:
        budget = verified_budget()
        source_plan = plan(budget["verification_sha256"])
        bound = bind_fast_shard.bind(raw_fast(), source_plan)
        result = merge_hybrid_source_strict.merge(
            source_plan,
            budget,
            [("direct.json", directed()), ("fast.json", bound)],
        )
        self.assertEqual(result["strict_binding"]["bound_fast_shards"], 1)
        self.assertEqual(
            result["strict_binding"]["status"],
            "CANONICAL_HASHES_REPLAYED",
        )
        self.assertEqual(result["lags"][0]["imag"], fraction(0))

    def test_budget_hash_mutation_is_rejected(self) -> None:
        budget = verified_budget()
        source_plan = plan("00" * 32)
        bound = bind_fast_shard.bind(raw_fast(), source_plan)
        with self.assertRaises(merge_hybrid_source_strict.CertificateError):
            merge_hybrid_source_strict.merge(
                source_plan,
                budget,
                [("direct.json", directed()), ("fast.json", bound)],
            )

    def test_fast_binding_hash_mutation_is_rejected(self) -> None:
        budget = verified_budget()
        source_plan = plan(budget["verification_sha256"])
        bound = bind_fast_shard.bind(raw_fast(), source_plan)
        bound["lags"][1]["real"] = fraction(2, 7)
        with self.assertRaises(merge_hybrid_source_strict.CertificateError):
            merge_hybrid_source_strict.merge(
                source_plan,
                budget,
                [("direct.json", directed()), ("fast.json", bound)],
            )

    def test_unbound_raw_shard_is_rejected(self) -> None:
        budget = verified_budget()
        source_plan = plan(budget["verification_sha256"])
        with self.assertRaises(merge_hybrid_source_strict.CertificateError):
            merge_hybrid_source_strict.merge(
                source_plan,
                budget,
                [("direct.json", directed()), ("fast.json", raw_fast())],
            )

    def test_binder_rejects_operation_order_drift(self) -> None:
        budget = verified_budget()
        source_plan = plan(budget["verification_sha256"])
        raw = raw_fast()
        raw["phase_taylor_R"] = 4
        with self.assertRaises(bind_fast_shard.CertificateError):
            bind_fast_shard.bind(raw, source_plan)

    def test_binder_rejects_early_range(self) -> None:
        budget = verified_budget()
        source_plan = plan(budget["verification_sha256"])
        with self.assertRaises(bind_fast_shard.CertificateError):
            bind_fast_shard.bind(raw_fast(1, 4, 3), source_plan)


if __name__ == "__main__":
    unittest.main()
