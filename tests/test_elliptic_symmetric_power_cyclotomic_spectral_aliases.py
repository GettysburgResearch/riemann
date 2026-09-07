"""Independent replay tests for cyclotomic complete-spectrum aliases."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
import sys
import unittest
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FUNCTION_FIELD = ROOT / "research" / "l-families" / "atlas" / "function_field"
sys.path.insert(0, str(FUNCTION_FIELD))

import elliptic_symmetric_power_cyclotomic_spectral_aliases as subject  # noqa: E402


def independent_exponents(order: int, m: int) -> Counter[int]:
    return Counter((m - 2 * j) % order for j in range(m + 1))


def independent_units(order: int) -> tuple[int, ...]:
    return tuple(a for a in range(1, order) if math.gcd(a, order) == 1)


def independent_stabilizer(order: int, m: int) -> tuple[int, ...]:
    base = independent_exponents(order, m)
    return tuple(
        a
        for a in independent_units(order)
        if Counter(
            (a * residue) % order
            for residue, multiplicity in base.items()
            for _ in range(multiplicity)
        )
        == base
    )


def poly_trim(values: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    output = list(values)
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return tuple(output)


def poly_add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return poly_trim(
        [
            (left[i] if i < len(left) else 0)
            + (right[i] if i < len(right) else 0)
            for i in range(max(len(left), len(right)))
        ]
    )


def poly_mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i + j] += first * second
    return poly_trim(output)


def independent_trace_polynomial(order: int) -> tuple[int, ...]:
    if order == 0:
        return (2,)
    older, previous = (2,), (0, 1)
    for _ in range(2, order + 1):
        shifted = (0,) + previous
        current = poly_add(shifted, tuple(-value for value in older))
        older, previous = previous, current
    return previous


def monic_divides_mod_two(
    dividend: tuple[int, ...], divisor: tuple[int, ...]
) -> bool:
    remainder = [value % 2 for value in dividend]
    divisor = tuple(value % 2 for value in divisor)
    while len(remainder) >= len(divisor):
        coefficient = remainder[-1]
        shift = len(remainder) - len(divisor)
        if coefficient:
            for index, value in enumerate(divisor):
                remainder[index + shift] ^= value
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return not remainder


class EllipticSymmetricPowerCyclotomicSpectralAliasesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_complete_cycle_decomposition_and_all_edge_cases(self) -> None:
        for order in range(3, 52, 2):
            for m in range(3 * order):
                with self.subTest(order=order, m=m):
                    counts = subject.exponent_multiplicities(order, m)
                    k, s = divmod(m + 1, order)
                    remainder = Counter(subject.remainder_residues(order, m))
                    reconstructed = Counter({residue: k for residue in range(order)})
                    reconstructed.update(remainder)
                    self.assertEqual(counts, reconstructed)
                    scaled = subject.scaled_remainder_interval(order, m)
                    self.assertEqual(len(scaled), s)
                    if s:
                        self.assertEqual(
                            {(scaled[j] - scaled[j + 1]) % order for j in range(s - 1)},
                            {1} if s > 1 else set(),
                        )

            self.assertEqual(subject.remainder_residues(order, order - 1), ())
            self.assertEqual(subject.remainder_residues(order, order), (0,))
            self.assertEqual(
                set(subject.remainder_residues(order, order - 2)),
                set(range(1, order)),
            )

    def test_exact_stabilizer_theorem_independent_replay(self) -> None:
        comparisons = 0
        for order in range(3, 52, 2):
            units = independent_units(order)
            for m in range(2 * order):
                actual = independent_stabilizer(order, m)
                expected = (
                    units
                    if m % order in (order - 2, order - 1, 0)
                    else (1, order - 1)
                )
                self.assertEqual(actual, expected, (order, m))
                self.assertEqual(subject.exact_stabilizer(order, m), actual)
                self.assertEqual(subject.predicted_stabilizer(order, m), expected)
                comparisons += len(units)
        self.assertEqual(comparisons, 37_508)

    def test_autocorrelation_formula_and_unique_maximum(self) -> None:
        comparisons = 0
        for order in range(3, 52, 2):
            for length in range(2, order - 1):
                interval = set(range(length))
                correlations = {}
                for displacement in range(1, order):
                    direct = len(
                        interval
                        & {(value + displacement) % order for value in interval}
                    )
                    closed = subject.interval_autocorrelation(
                        order, length, displacement
                    )
                    self.assertEqual(closed, direct)
                    correlations[displacement] = direct
                    comparisons += 1
                self.assertEqual(
                    {d for d, value in correlations.items() if value == length - 1},
                    {1, order - 1},
                )
                self.assertTrue(
                    all(
                        value <= length - 2
                        for d, value in correlations.items()
                        if d not in (1, order - 1)
                    )
                )
        self.assertEqual(comparisons, 20_800)

    def test_special_factor_identities_and_scalar_lift_audit(self) -> None:
        by_order = {
            row["root_order_N"]: row
            for row in self.fixture["special_factor_identities"]
        }
        for order in subject.EXAMPLE_ORDERS:
            row = by_order[order]
            expected_signatures = {
                order - 2: (0,) + (1,) * (order - 1),
                order - 1: (1,) * order,
                order: (2,) + (1,) * (order - 1),
            }
            for m, expected in expected_signatures.items():
                self.assertEqual(subject.exponent_edge_signature(order, m), expected)
                base = independent_exponents(order, m)
                for a in independent_units(order):
                    transformed = Counter(
                        (a * residue) % order
                        for residue, multiplicity in base.items()
                        for _ in range(multiplicity)
                    )
                    self.assertEqual(base, transformed)

                # A common fixed-determinant scalar lift contributes the same
                # symbolic scalar exponent m to every atom on both sides.
                common_lift = Counter(
                    (m, residue)
                    for residue, multiplicity in base.items()
                    for _ in range(multiplicity)
                )
                for a in independent_units(order):
                    compared = Counter(
                        (m, (a * residue) % order)
                        for residue, multiplicity in base.items()
                        for _ in range(multiplicity)
                    )
                    self.assertEqual(common_lift, compared)

            self.assertEqual(
                row["m_N_minus_2"]["coefficients_T0_through_T_to_N_minus_1"],
                [1] * order,
            )
            expected_n_minus_1 = [0] * (order + 1)
            expected_n_minus_1[0] = 1
            expected_n_minus_1[-1] = -1
            self.assertEqual(
                row["m_N_minus_1"]["coefficients_T0_through_T_to_N"],
                expected_n_minus_1,
            )
            expected_n = [0] * (order + 2)
            expected_n[0], expected_n[1] = 1, -1
            expected_n[order], expected_n[order + 1] = -1, 1
            self.assertEqual(
                row["m_N"]["coefficients_T0_through_T_to_N_plus_1"],
                expected_n,
            )

            # The negative lift is invisible only at the even power N-1.
            self.assertEqual((-1) ** (order - 1), 1)
            self.assertEqual((-1) ** (order - 2), -1)
            self.assertEqual((-1) ** order, -1)
            lift = row["lift_sign_audit"]
            self.assertIn("same factor", lift["m_N_minus_1"])
            self.assertIn("F(-T)", lift["m_N_minus_2_and_m_N"])

    def test_trace_minimal_polynomial_certificates_independently(self) -> None:
        expected = {
            5: (-1, 1, 1),
            7: (-1, -2, 1, 1),
            9: (1, -3, 0, 1),
            11: (1, 3, -3, -4, 1, 1),
        }
        rows = {row["root_order"]: row for row in self.fixture["orders_5_7_9_11"]}
        for order, minimal in expected.items():
            left = poly_add(independent_trace_polynomial(order), (-2,))
            right = poly_mul((-2, 1), poly_mul(minimal, minimal))
            if order == 9:
                right = poly_mul(right, (1, 2, 1))
            self.assertEqual(left, right)
            self.assertEqual(subject.trace_chebyshev_polynomial(order), independent_trace_polynomial(order))
            self.assertEqual(
                tuple(rows[order]["minimal_polynomial_coefficients_low_to_high"]),
                minimal,
            )

            degree = len(minimal) - 1
            tested = 0
            for trial_degree in range(1, degree // 2 + 1):
                for lower in itertools.product(range(2), repeat=trial_degree):
                    tested += 1
                    self.assertFalse(monic_divides_mod_two(minimal, tuple(lower) + (1,)))
            self.assertEqual(
                rows[order]["irreducibility"]["monic_candidates_exhausted"],
                tested,
            )
            self.assertEqual(
                rows[order]["primitive_class_count"],
                len(independent_units(order)) // 2,
            )

    def test_rational_recovery_torsion_exhaustion(self) -> None:
        theorem = self.fixture["rational_fixed_determinant_recovery_theorem"]
        table = theorem["torsion_table"]
        self.assertEqual(
            [
                (
                    row["eigenratio_order"],
                    row["r_plus_r_inverse"],
                    row["trace_square_over_q"],
                )
                for row in table
            ],
            [(1, 2, 4), (2, -2, 0), (3, -1, 1), (4, 0, 2), (6, 1, 3)],
        )
        for order in (1, 2, 3, 4, 6):
            units = tuple(a for a in range(1, order + 1) if math.gcd(a, order) == 1)
            residues = {a % order for a in units}
            self.assertTrue(residues <= {1 % order, (-1) % order})
        self.assertIn("m=1", theorem["quotient_group_certificate"]["consequence"])
        self.assertIn("irrational", theorem["why_cyclotomic_examples_do_not_contradict_it"])

    def test_payload_source_file_locks_resources_and_no_floats(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        locks = stored["source_and_file_locks"]["locks"]
        for lock in locks.values():
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                lock["sha256_lf_normalized"], hashlib.sha256(normalized).hexdigest()
            )
        self.assertEqual(
            locks["scalar_trace_fixture"]["payload_sha256"],
            subject.EXPECTED_SOURCE_PAYLOAD_SHA256,
        )

        resources = stored["resource_contract"]
        ledger = resources["accounted_work_unit_ledger"]
        self.assertEqual(ledger["bounded_stabilizer_unit_candidates"], 37_508)
        self.assertEqual(ledger["bounded_autocorrelation_formula_checks"], 20_800)
        self.assertEqual(ledger["total_accounted_work_units"], 58_326)
        self.assertLess(
            ledger["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertEqual(resources["field_curve_or_polynomial_model_enumerations"], 0)
        self.assertEqual(resources["symbolic_packages"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(stored)

    def test_scope_firewalls_and_upstream_independence(self) -> None:
        firewall = self.fixture["scope_firewall"]
        self.assertIn("need not", firewall["no_scalar_full_factor_conflation"])
        self.assertIn("not advertised", firewall["no_rational_example_claim"])
        self.assertIn("does not supply", firewall["no_curve_or_global_family_claim"])
        self.assertIn("F(-T)", firewall["no_negative_lift_conflation"])
        self.assertIn("odd root order", firewall["no_even_order_classification_claim"])
        self.assertIn("without", firewall["no_priority_claim"])
        self.assertIn("RH", firewall["no_RH_or_GRH_claim"])
        source = self.fixture["source_and_file_locks"]
        self.assertIn("provenance", source["upstream_role"])
        self.assertIn("no in-progress sign packet", source["upstream_role"])

    def test_note_math_controls_and_delimiters_are_well_formed(self) -> None:
        text = subject.NOTE_PATH.read_text(encoding="utf-8")
        lines = text.splitlines()
        known_controls = {
            "Gamma",
            "Longleftrightarrow",
            "alpha",
            "beta",
            "bigl",
            "bigr",
            "bmod",
            "boxed",
            "cap",
            "cdots",
            "delta",
            "diag",
            "equiv",
            "frac",
            "gamma",
            "gcd",
            "iff",
            "in",
            "lambda",
            "langle",
            "ldots",
            "le",
            "left",
            "mathbb",
            "max",
            "ne",
            "operatorname",
            "pm",
            "pmod",
            "prod",
            "quad",
            "qquad",
            "rangle",
            "rho",
            "right",
            "sum",
            "tau",
            "text",
            "zeta",
        }
        seen: set[str] = set()
        in_display = False
        brace_balance = 0
        openers = closers = 0
        for line_number, line in enumerate(lines, start=1):
            if line.strip() == r"\[":
                self.assertFalse(in_display, f"nested opener at line {line_number}")
                in_display = True
                brace_balance = 0
                openers += 1
                continue
            if line.strip() == r"\]":
                self.assertTrue(in_display, f"orphan closer at line {line_number}")
                self.assertEqual(brace_balance, 0, f"brace imbalance at line {line_number}")
                in_display = False
                closers += 1
                continue
            if in_display:
                seen.update(re.findall(r"\\([A-Za-z]+)", line))
                brace_balance += line.count("{") - line.count("}")
                self.assertGreaterEqual(brace_balance, 0)
        self.assertFalse(in_display)
        self.assertEqual(openers, closers)
        self.assertEqual(openers, 32)
        self.assertEqual(seen - known_controls, set())
        self.assertEqual(text.count("```") % 2, 0)
        self.assertIsNone(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))

    def test_strict_refusals_survive_optimized_python(self) -> None:
        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture(49)
        for invalid_order in (1, 2, 4, 8, -3):
            with self.subTest(order=invalid_order):
                with self.assertRaisesRegex(ValueError, "odd integer"):
                    subject.exponent_multiplicities(invalid_order, 1)
        for malformed_order in (True, False, 5.0, "5", None):
            with self.subTest(order=malformed_order):
                with self.assertRaises(TypeError):
                    subject.exponent_multiplicities(malformed_order, 1)
        for malformed_m in (True, False, 1.0, "1", None):
            with self.subTest(m=malformed_m):
                with self.assertRaises(TypeError):
                    subject.exponent_multiplicities(5, malformed_m)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.exponent_multiplicities(5, -1)
        with self.assertRaisesRegex(ValueError, "between"):
            subject.interval_autocorrelation(5, 6, 1)
        with self.assertRaisesRegex(ValueError, "one of"):
            subject.primitive_trace_certificate(13)
        with self.assertRaisesRegex(ValueError, "at least 5"):
            subject.special_factor_certificate(3)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.ResourceGuard().charge(
                "deliberate_refusal", subject.ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE
            )


if __name__ == "__main__":
    unittest.main()
