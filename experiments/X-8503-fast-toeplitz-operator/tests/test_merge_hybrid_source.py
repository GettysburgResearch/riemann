from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "merge_hybrid_source.py"
SPEC = importlib.util.spec_from_file_location("merge_hybrid_source", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
merge_hybrid_source = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(merge_hybrid_source)


def fraction(numerator: int, denominator: int = 1) -> dict[str, str]:
    return {"numerator": str(numerator), "denominator": str(denominator)}


def hex_value(value: float) -> str:
    return value.hex()


PARAMETER_SHA = "11" * 32
NORMALIZATION_SHA = "22" * 32
CONTRACT = (
    "x86 binary80 nearest basic arithmetic; binary128 segment-relative phase; "
    "MPFR setup; M=32768 R=3; two-hat coefficient deposits; balanced pairwise "
    "summation; zero guarded support-boundary events"
)


def plan() -> dict[str, object]:
    return {
        "schema": merge_hybrid_source.PLAN_SCHEMA,
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
        "operator_gate": fraction(1, 2),
    }


def budget() -> dict[str, object]:
    return {
        "schema": merge_hybrid_source.BUDGET_SCHEMA,
        "verified": True,
        "status": "STATIC_OPERATOR_BUDGET_VERIFIED",
        "components": {"total": fraction(1, 100)},
    }


def directed() -> dict[str, object]:
    return {
        "schema": merge_hybrid_source.DIRECTED_SCHEMA,
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
                "real_lower_hex": hex_value(1.0),
                "real_upper_hex": hex_value(1.2),
                # Deliberately enormous imaginary interval: the Hermitian matrix
                # map ignores Im(c_0), so it must not enter the operator radius.
                "imag_lower_hex": hex_value(-100.0),
                "imag_upper_hex": hex_value(100.0),
            },
            {
                "lag": 1,
                "real_lower_hex": hex_value(0.2),
                "real_upper_hex": hex_value(0.4),
                "imag_lower_hex": hex_value(-0.1),
                "imag_upper_hex": hex_value(0.1),
            },
        ],
    }


def fast(start: int = 2, end: int = 4, primes: int = 3) -> dict[str, object]:
    return {
        "schema": merge_hybrid_source.FAST_SCHEMA,
        "cutoff": 100,
        "carrier": "1.5",
        "cells": 2,
        "segment_size": 10,
        "total_segments": 4,
        "segment_start": start,
        "segment_end": end,
        "include_higher_powers": False,
        "prime_count": primes,
        "higher_prime_power_count": 0,
        "total_terms": primes,
        "vector_independent": True,
        "parameter_sha256": PARAMETER_SHA,
        "normalization_sha256": NORMALIZATION_SHA,
        "guarded_support_boundary_count": 0,
        "lags": [
            {"lag": 0, "real": fraction(1, 5), "imag": fraction(9, 1)},
            {"lag": 1, "real": fraction(1, 7), "imag": fraction(-1, 9)},
        ],
    }


class HybridMergeTests(unittest.TestCase):
    def test_complete_hybrid_source_passes(self) -> None:
        result = merge_hybrid_source.merge(
            plan(), budget(), [("direct.json", directed()), ("fast.json", fast())]
        )
        self.assertEqual(result["status"], "COMPLETE_REFERENCE_AND_PRIME_OPERATOR_MOAT")
        # Binary64 intervals are exact binary rationals, so compare against the
        # independently reconstructed Fraction.from_float values.
        direct_radius = (
            Fraction.from_float(1.2 - 1.0) / 2
            + Fraction.from_float(0.4 - 0.2) / 2
            + Fraction.from_float(0.1 - (-0.1)) / 2
        )
        expected = direct_radius + Fraction(1, 100)
        self.assertEqual(
            merge_hybrid_source.parse_fraction(
                result["operator_radius"]["prime_total"], "prime_total"
            ),
            expected,
        )
        self.assertEqual(result["lags"][0]["imag"], fraction(0))

    def test_global_fast_budget_is_added_once(self) -> None:
        first = fast(2, 3, 1)
        second = fast(3, 4, 2)
        result = merge_hybrid_source.merge(
            plan(),
            budget(),
            [("direct.json", directed()), ("fast-a.json", first), ("fast-b.json", second)],
        )
        total = merge_hybrid_source.parse_fraction(
            result["operator_radius"]["prime_total"], "prime_total"
        )
        direct_only = merge_hybrid_source.parse_fraction(
            result["operator_radius"]["directed_rectangle_l1"], "directed"
        )
        self.assertEqual(total - direct_only, Fraction(1, 100))

    def test_gap_is_rejected(self) -> None:
        broken = fast(3, 4, 3)
        with self.assertRaises(merge_hybrid_source.CertificateError):
            merge_hybrid_source.merge(
                plan(), budget(), [("direct.json", directed()), ("fast.json", broken)]
            )

    def test_early_fast_segment_is_rejected(self) -> None:
        broken = fast(1, 4, 3)
        direct_shard = directed()
        direct_shard["segment_end"] = 1
        with self.assertRaises(merge_hybrid_source.CertificateError):
            merge_hybrid_source.merge(
                plan(), budget(), [("direct.json", direct_shard), ("fast.json", broken)]
            )

    def test_guarded_boundary_is_rejected(self) -> None:
        broken = fast()
        broken["guarded_support_boundary_count"] = 1
        with self.assertRaises(merge_hybrid_source.CertificateError):
            merge_hybrid_source.merge(
                plan(), budget(), [("direct.json", directed()), ("fast.json", broken)]
            )

    def test_duplicate_higher_stream_is_rejected(self) -> None:
        duplicate = directed()
        duplicate["segment_start"] = 2
        duplicate["segment_end"] = 4
        duplicate["prime_count"] = 3
        duplicate["higher_prime_power_count"] = 1
        duplicate["total_terms"] = 4
        mutated_plan = plan()
        mutated_plan["expected_counts"] = {
            "prime_count": 6,
            "higher_prime_power_count": 2,
            "total_terms": 8,
        }
        with self.assertRaises(merge_hybrid_source.CertificateError):
            merge_hybrid_source.merge(
                mutated_plan,
                budget(),
                [("direct-a.json", directed()), ("direct-b.json", duplicate)],
            )


if __name__ == "__main__":
    unittest.main()
