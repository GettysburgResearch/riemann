"""Exact replay tests for the third-order genus-two primitive inventory."""

from __future__ import annotations

import hashlib
import json
import sys
import time
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import genus2_b3_primitive_trace_average as b3
import genus2_third_order_primitive_inventory as subject


def _pairs(value: list[list[int]]) -> tuple[Fraction, ...]:
    result = tuple(Fraction(*entry) for entry in value)
    while len(result) > 1 and not result[-1]:
        result = result[:-1]
    return result


def _pad_add(
    left: tuple[Fraction, ...],
    right: tuple[Fraction, ...],
) -> tuple[Fraction, ...]:
    size = max(len(left), len(right))
    result = tuple(
        (left[index] if index < len(left) else Fraction(0))
        + (right[index] if index < len(right) else Fraction(0))
        for index in range(size)
    )
    while len(result) > 1 and not result[-1]:
        result = result[:-1]
    return result


def _scale(value: tuple[Fraction, ...], scalar: Fraction | int) -> tuple[Fraction, ...]:
    return tuple(Fraction(scalar) * coefficient for coefficient in value)


def _expression_component(
    expression: dict[str, object], key: str | None
) -> tuple[Fraction, ...]:
    if key is None:
        return _pairs(expression["constant_low_to_high"])
    coefficients = expression["level2_residual_coefficients"]
    return _pairs(coefficients.get(key, [[0, 1]]))


class Genus2ThirdOrderPrimitiveInventoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_status_and_minimal_residual_basis(self) -> None:
        self.assertEqual(
            self.fixture["status"],
            "REDUCED_EXACTLY_TO_EIGHT_LEVEL2_MOMENT_CHANNELS",
        )
        theorem = self.fixture["exact_reduction_theorem"]
        self.assertEqual(
            theorem["unresolved_level2_residuals"], list(subject.RESIDUAL_KEYS)
        )
        certificate = theorem["rank_minimality_certificate"]
        self.assertEqual(certificate["rank_over_Q(q)"], 8)
        self.assertEqual(certificate["determinant_numerator"], 13)
        self.assertEqual(certificate["determinant_denominator"], 4_194_304)

    def test_twelve_conductor_types_are_exactly_the_b4_types(self) -> None:
        rows = self.fixture["exact_reduction_theorem"]["primitive_rows"]
        self.assertEqual(len(rows), 12)
        actual = {
            (
                row["conductor_degree"],
                row["linear_prime_count"],
                row["quadratic_prime_count"],
            )
            for row in rows
        }
        expected = {
            (degree, linear, quadratic)
            for degree, types in subject.DEGREE_TYPES.items()
            for linear, quadratic in types
        }
        self.assertEqual(actual, expected)
        for row in rows:
            self.assertIn("sum_s1_cubed", row)
            self.assertIn("sum_s1_s2", row)
            self.assertIn("sum_s3", row)
            self.assertIn("sum_p3", row)

    def test_cached_lower_inventory_matches_the_b3_lemma(self) -> None:
        guard = b3.AlgebraGuard(time.monotonic() + 2)
        cached, _ = subject._lower_primitive_tables(guard)
        for factor_type in subject.ALL_TYPES:
            independent_guard = b3.AlgebraGuard(time.monotonic() + 2)
            expected = b3._primitive_moments(*factor_type, independent_guard)
            self.assertEqual(cached[factor_type], expected)

    def test_newton_p3_identity_holds_coefficientwise(self) -> None:
        rows = self.fixture["exact_reduction_theorem"]["primitive_rows"]
        for row in rows:
            for key in (None, *subject.RESIDUAL_KEYS):
                p3 = _expression_component(row["sum_p3"], key)
                p2 = (
                    _pairs(row["sum_p2_low_to_high"]) if key is None else (Fraction(0),)
                )
                left = _scale(_pad_add(p3, _scale(p2, -1)), 6)
                right = _expression_component(row["sum_s1_cubed"], key)
                right = _pad_add(
                    right,
                    _scale(_expression_component(row["sum_s1_s2"], key), 3),
                )
                right = _pad_add(
                    right, _scale(_expression_component(row["sum_s3"], key), 2)
                )
                self.assertEqual(left, right)

    def test_cubic_strata_exhaust_the_level_one_family(self) -> None:
        guard = b3.AlgebraGuard(time.monotonic() + 1)
        counts = subject._stratum_counts(guard)
        full = subject._full_model_moments(guard)
        total = b3._add(b3._add(counts["111"], counts["12"], guard), counts["3"], guard)
        self.assertEqual(total, full[0])
        strata = self.fixture["exact_reduction_theorem"]["factorization_strata"]
        self.assertEqual(strata["111"]["fibre_multiplicity_in_s1^3"], 6)
        self.assertEqual(strata["12"]["fibre_multiplicity_in_s1*s2"], 2)
        self.assertEqual(strata["3"]["fibre_multiplicity_in_s3"], 3)

    def test_trace_inventory_degree_never_exceeds_eight(self) -> None:
        guard = b3.AlgebraGuard(time.monotonic() + 2)
        for rational_roots, quadratic_factors in ((3, 0), (1, 1), (0, 0)):
            rows = subject._inventory_polynomials(
                rational_roots, quadratic_factors, guard
            )
            for factor_type, polynomial in rows.items():
                self.assertLessEqual(
                    max((a_degree for _, a_degree in polynomial), default=0),
                    factor_type[0] + 2 * factor_type[1],
                )
                self.assertLessEqual(
                    max((a_degree for _, a_degree in polynomial), default=0), 8
                )

    def test_marked_deletion_interface_is_complete(self) -> None:
        rows = self.fixture["marked_deletion_interface"]
        self.assertEqual(len(rows), 13)
        census = {}
        for row in rows:
            key = (row["conductor_degree"], row["deletion_kind"])
            census[key] = census.get(key, 0) + 1
        self.assertEqual(
            census,
            {
                (6, "one_external_linear"): 4,
                (4, "one_external_linear"): 3,
                (4, "one_external_quadratic"): 3,
                (4, "two_external_linears"): 3,
            },
        )
        for row in rows:
            residual_keys = set()
            for coefficient_name in ("sum_C1", "sum_C3", "sum_C5"):
                residual_keys.update(
                    row[coefficient_name]["level2_residual_coefficients"].keys()
                )
            if row["deletion_kind"] == "one_external_linear" and (
                row["conductor_degree"] == 4
            ):
                self.assertFalse(residual_keys)
            elif row["conductor_degree"] == 6:
                self.assertTrue(residual_keys)

    def test_frozen_b4_structure_has_54_signatures(self) -> None:
        audit = self.fixture["B4_source_structure_audit"]
        self.assertEqual(audit["signature_count"], 54)
        self.assertEqual(len(audit["primitive_conductor_types"]), 12)
        expected_weights = {
            (8, 0): 2520,
            (6, 1): 360,
            (4, 2): 72,
            (2, 3): 24,
            (0, 4): 24,
        }
        actual_weights = {
            (row["linear_prime_count"], row["quadratic_prime_count"]): row["weight"]
            for row in self.fixture["downstream_cancellation_boundary"][
                "generic_degree8_weights_by_type"
            ]
        }
        self.assertEqual(actual_weights, expected_weights)

    def test_no_enumeration_sampling_or_cap_overrun(self) -> None:
        scope = self.fixture["scope"]
        self.assertEqual(scope["finite_fields_enumerated"], 0)
        self.assertEqual(scope["cubics_enumerated"], 0)
        self.assertEqual(scope["conductors_enumerated"], 0)
        self.assertEqual(scope["genus_two_family_members_consumed"], 0)
        self.assertEqual(scope["sampled_q_values_used_as_theorem_input"], 0)
        contract = self.fixture["resource_contract"]
        self.assertLessEqual(
            contract["actual_operations_and_input_atoms"],
            contract["maximum_symbolic_operations_and_input_atoms"],
        )
        self.assertEqual(contract["maximum_symbolic_operations_and_input_atoms"], 4096)

    def test_fixture_payload_and_sources_are_locked(self) -> None:
        frozen = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(frozen, self.fixture)
        payload = dict(frozen)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(payload))
        for record in frozen["source_manifest"]:
            path = ROOT / record["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                record["sha256_lf_normalized"],
                hashlib.sha256(normalized).hexdigest(),
            )

    def test_invalid_domains_and_malformed_source_are_rejected(self) -> None:
        guard = b3.AlgebraGuard(time.monotonic() + 1)
        with self.assertRaises(ValueError):
            subject._bi_elementary(9, {}, {}, guard)
        with self.assertRaises(TypeError):
            subject._b4_structure_audit({})


if __name__ == "__main__":
    unittest.main()
