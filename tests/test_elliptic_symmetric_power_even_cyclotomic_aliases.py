"""Independent replay tests for even-cyclotomic complete-spectrum aliases."""

from __future__ import annotations

import hashlib
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

import elliptic_symmetric_power_even_cyclotomic_aliases as subject  # noqa: E402


def independent_units(order: int) -> tuple[int, ...]:
    return tuple(a for a in range(1, order) if math.gcd(a, order) == 1)


def independent_exponents(order: int, m: int) -> Counter[int]:
    return Counter((m - 2 * j) % order for j in range(m + 1))


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


def trim_polynomial(values: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    output = list(values)
    while len(output) > 1 and output[-1] == 0:
        output.pop()
    return tuple(output)


def multiply_polynomials(
    left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[int, ...]:
    output = [0] * (len(left) + len(right) - 1)
    for i, first in enumerate(left):
        for j, second in enumerate(right):
            output[i + j] += first * second
    return trim_polynomial(output)


def power_polynomial(base: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    result = (1,)
    for _ in range(exponent):
        result = multiply_polynomials(result, base)
    return result


class EllipticSymmetricPowerEvenCyclotomicAliasesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = subject.build_fixture()

    def test_complete_cycle_decomposition_with_multiplicity(self) -> None:
        checks = 0
        for order in range(4, 65, 2):
            half_order = order // 2
            for m in range(3 * order):
                k, s = divmod(m + 1, half_order)
                expected = Counter(
                    {residue: k for residue in range(m % 2, order, 2) if k}
                )
                expected.update((m - 2 * j) % order for j in range(s))
                self.assertEqual(independent_exponents(order, m), expected)
                self.assertEqual(subject.exponent_multiplicities(order, m), expected)
                self.assertEqual(subject.reconstructed_cycle_counts(order, m), expected)
                self.assertEqual(subject.cycle_remainder(order, m), (
                    k,
                    s,
                    tuple((m - 2 * j) % order for j in range(s)),
                ))
                checks += 1
        self.assertEqual(checks, 3_162)

    def test_exact_stabilizer_theorem_independent_replay(self) -> None:
        candidate_checks = 0
        comparisons = 0
        for order in range(4, 65, 2):
            half_order = order // 2
            units = independent_units(order)
            for m in range(2 * order):
                _, s = divmod(m + 1, half_order)
                if s in {0, 1, half_order - 1}:
                    predicted = units
                elif m % 2 == 0:
                    predicted = tuple(
                        a
                        for a in units
                        if a % half_order in {1 % half_order, -1 % half_order}
                    )
                else:
                    predicted = (1, order - 1)
                actual = independent_stabilizer(order, m)
                self.assertEqual(actual, predicted, (order, m, s))
                self.assertEqual(subject.exact_stabilizer(order, m), actual)
                self.assertEqual(subject.predicted_stabilizer(order, m), predicted)
                candidate_checks += len(units)
                comparisons += 1
        ledger = self.fixture["resource_contract"]["accounted_work_unit_ledger"]
        self.assertEqual(
            ledger["bounded_stabilizer_unit_candidates"], candidate_checks
        )
        self.assertEqual(comparisons, 2_108)

    def test_interval_autocorrelation_and_half_shift_lemmas(self) -> None:
        autocorrelation_checks = 0
        half_shift_checks = 0
        for modulus in range(2, 33):
            for length in range(2, modulus - 1):
                interval = set(range(length))
                correlations = {}
                for displacement in range(1, modulus):
                    direct = len(
                        interval
                        & {
                            (value + displacement) % modulus
                            for value in interval
                        }
                    )
                    closed = subject.cyclic_interval_autocorrelation(
                        modulus, length, displacement
                    )
                    self.assertEqual(closed, direct)
                    correlations[displacement] = direct
                    autocorrelation_checks += 1
                self.assertEqual(
                    {
                        displacement
                        for displacement, value in correlations.items()
                        if value == length - 1
                    },
                    {1, modulus - 1},
                )
            if modulus % 2 == 0:
                for length in range(modulus):
                    interval = Counter(range(length))
                    shifted = Counter(
                        (value + modulus // 2) % modulus for value in range(length)
                    )
                    self.assertEqual(interval == shifted, length == 0)
                    self.assertEqual(
                        subject.half_shift_interval_invariant(modulus, length),
                        length == 0,
                    )
                    half_shift_checks += 1
        ledger = self.fixture["resource_contract"]["accounted_work_unit_ledger"]
        self.assertEqual(ledger["bounded_autocorrelation_checks"], autocorrelation_checks)
        self.assertEqual(ledger["bounded_half_shift_checks"], half_shift_checks)

    def test_central_sign_lifts_are_exactly_the_generic_even_kernel(self) -> None:
        for order in range(4, 65, 2):
            half_order = order // 2
            lifts = subject.generic_even_power_lifts(order)
            expected = tuple(
                a
                for a in independent_units(order)
                if a % half_order in {1 % half_order, -1 % half_order}
            )
            self.assertEqual(lifts, expected)
            if order % 4:
                self.assertEqual(lifts, (1, order - 1))
            elif order == 4:
                self.assertEqual(lifts, (1, 3))
            else:
                self.assertEqual(
                    set(lifts), {1, order - 1, half_order - 1, half_order + 1}
                )
                central = half_order + 1
                for residue in range(1, order, 2):
                    self.assertEqual(
                        (central * residue) % order,
                        (residue + half_order) % order,
                    )

        # Interior odd powers reject the central lifts, while interior even
        # powers retain them.  N=16 supplies both parities in one modulus.
        order, half_order = 16, 8
        odd_m = 1  # s=2, interior
        even_m = 2  # s=3, interior
        self.assertEqual(subject.predicted_stabilizer(order, odd_m), (1, 15))
        self.assertEqual(
            set(subject.predicted_stabilizer(order, even_m)), {1, 7, 9, 15}
        )
        for residue in independent_exponents(order, odd_m):
            self.assertEqual(
                ((half_order + 1) * residue) % order,
                (residue + half_order) % order,
            )

    def test_all_three_edge_factor_identities_independently(self) -> None:
        rows = {
            (row["even_root_order_N"], row["symmetric_power_m"]): row
            for row in self.fixture["edge_factor_theorem"]["certificates"]
        }
        self.assertEqual(len(rows), 24)
        for order in subject.EXAMPLE_ORDERS:
            half_order = order // 2
            units = independent_units(order)
            for m in (half_order - 2, half_order - 1, half_order):
                k, s = divmod(m + 1, half_order)
                base = independent_exponents(order, m)
                for a in units:
                    transformed = Counter(
                        (a * residue) % order
                        for residue, multiplicity in base.items()
                        for _ in range(multiplicity)
                    )
                    self.assertEqual(transformed, base)

                cycle = [0] * (half_order + 1)
                cycle[0] = 1
                cycle[-1] = -((-1) ** m)
                cycle_tuple = tuple(cycle)
                actual = subject.edge_factor_polynomial(order, m)
                if s == 0:
                    expected = power_polynomial(cycle_tuple, k)
                elif s == 1:
                    expected = multiply_polynomials(
                        power_polynomial(cycle_tuple, k),
                        (1, -((-1) ** k)),
                    )
                else:
                    denominator = (1, -((-1) ** (k + 1)))
                    numerator = power_polynomial(cycle_tuple, k + 1)
                    self.assertEqual(
                        multiply_polynomials(actual, denominator), numerator
                    )
                    expected = actual
                self.assertEqual(actual, expected)
                self.assertEqual(len(actual) - 1, m + 1)
                self.assertEqual(rows[(order, m)]["factor_coefficients_T0_up"], list(actual))

        # The first genuine nonsign edge factor is explicit and integral.
        self.assertEqual(
            subject.edge_factor_polynomial(10, 3), (1, -1, 1, -1, 1)
        )

    def test_primitive_class_counts_and_exact_threshold(self) -> None:
        nongenuine = []
        for order in range(4, 65, 2):
            row = subject.primitive_collapse_certificate(order)
            phi = len(independent_units(order))
            self.assertEqual(row["Euler_phi_N"], phi)
            self.assertEqual(row["primitive_classes_modulo_inversion"], phi // 2)
            if order % 4 == 0:
                kernel_size = 2 if order == 4 else 4
                expected_orbits = phi // kernel_size
            else:
                expected_orbits = phi // 2
            self.assertEqual(
                row["primitive_classes_modulo_inversion_and_available_central_sign"],
                expected_orbits,
            )
            self.assertEqual(
                row["all_unit_edge_collapses_genuinely_nonsign_classes"],
                expected_orbits > 1,
            )
            if expected_orbits == 1:
                nongenuine.append(order)
        self.assertEqual(nongenuine, [4, 6, 8, 12])
        self.assertFalse(subject.primitive_collapse_certificate(8)[
            "all_unit_edge_collapses_genuinely_nonsign_classes"
        ])
        self.assertTrue(subject.primitive_collapse_certificate(10)[
            "all_unit_edge_collapses_genuinely_nonsign_classes"
        ])

    def test_corner_moduli_have_only_edge_residues(self) -> None:
        for order in (4, 6):
            half_order = order // 2
            for m in range(4 * order):
                s = (m + 1) % half_order
                self.assertIn(s, {0, 1, half_order - 1})
                self.assertEqual(
                    subject.exact_stabilizer(order, m), independent_units(order)
                )
        self.assertEqual(independent_units(4), (1, 3))
        self.assertEqual(independent_units(6), (1, 5))

    def test_payload_locks_resources_and_no_floats(self) -> None:
        stored = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(stored, self.fixture)
        unhashed = dict(stored)
        claimed = unhashed.pop("payload_sha256")
        self.assertEqual(claimed, subject._canonical_sha256(unhashed))

        expected_payloads = {
            subject.EXPECTED_ODD_SOURCE_PAYLOAD_SHA256,
            subject.EXPECTED_SIGN_SOURCE_PAYLOAD_SHA256,
        }
        self.assertEqual(
            {lock["payload_sha256"] for lock in stored["source_locks"]},
            expected_payloads,
        )
        for lock in stored["source_locks"]:
            path = ROOT / lock["path"]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                lock["file_sha256_lf_normalized"],
                hashlib.sha256(normalized).hexdigest(),
            )
            source = json.loads(path.read_text(encoding="utf-8"))
            source_unhashed = dict(source)
            source_claimed = source_unhashed.pop("payload_sha256")
            self.assertEqual(source_claimed, subject._canonical_sha256(source_unhashed))

        for key in ("script", "note", "test"):
            path = ROOT / stored["producer"][key]
            normalized = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            self.assertEqual(
                stored["producer"][f"{key}_sha256_lf_normalized"],
                hashlib.sha256(normalized).hexdigest(),
            )

        resources = stored["resource_contract"]
        self.assertEqual(
            resources["accounted_work_unit_ledger"],
            {
                "bounded_autocorrelation_checks": 9_425,
                "bounded_cycle_decomposition_checks": 2_108,
                "bounded_half_shift_checks": 272,
                "bounded_stabilizer_unit_candidates": 37_904,
                "locked_source_files_verified": 2,
                "named_edge_factor_certificates": 24,
            },
        )
        self.assertEqual(resources["total_accounted_work_units"], 49_735)
        self.assertLess(
            resources["total_accounted_work_units"],
            resources["exclusive_accounted_work_unit_cap"],
        )
        self.assertEqual(resources["field_curve_polynomial_or_trace_range_enumerations"], 0)
        self.assertEqual(resources["random_samples"], 0)
        self.assertEqual(resources["floating_point_results"], 0)
        self.assertEqual(resources["symbolic_packages"], 0)

        def reject_float(value: object) -> None:
            self.assertNotIsInstance(value, float)
            if isinstance(value, dict):
                for item in value.values():
                    reject_float(item)
            elif isinstance(value, list):
                for item in value:
                    reject_float(item)

        reject_float(stored)

    def test_note_math_controls_and_delimiters_are_well_formed(self) -> None:
        text = subject.NOTE_PATH.read_text(encoding="utf-8")
        known_controls = {
            "Longleftrightarrow",
            "begin",
            "bigl",
            "bigr",
            "bmod",
            "boxed",
            "cap",
            "cases",
            "diag",
            "equiv",
            "end",
            "frac",
            "gcd",
            "in",
            "le",
            "left",
            "ldots",
            "mapsto",
            "mathbb",
            "max",
            "mid",
            "ne",
            "operatorname",
            "pm",
            "pmod",
            "prod",
            "quad",
            "qquad",
            "right",
            "subset",
            "text",
            "varphi",
            "zeta",
        }
        seen: set[str] = set()
        in_display = False
        brace_balance = 0
        openers = closers = 0
        for line_number, line in enumerate(text.splitlines(), start=1):
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
        self.assertGreaterEqual(openers, 20)
        self.assertEqual(seen - known_controls, set())
        self.assertEqual(text.count("```") % 2, 0)
        self.assertIsNone(re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", text))

    def test_scope_firewalls_and_strict_refusals(self) -> None:
        firewall = self.fixture["scope_firewall"]
        self.assertTrue(firewall["local_representation_theory_only"])
        self.assertTrue(firewall["no_global_Euler_product_or_compatible_family_constructed"])
        self.assertTrue(firewall["no_rational_nonsign_counterexample_claim"])
        self.assertTrue(firewall["no_literature_priority_or_novelty_claim"])
        self.assertTrue(firewall["no_RH_GRH_or_zero_distribution_consequence"])

        with self.assertRaisesRegex(ValueError, "exactly"):
            subject.build_fixture(62)
        for invalid_order in (-4, 0, 1, 2, 3, 5, 9):
            with self.subTest(order=invalid_order):
                with self.assertRaisesRegex(ValueError, "even integer"):
                    subject.exponent_multiplicities(invalid_order, 1)
        for malformed_order in (True, False, 4.0, "4", None):
            with self.subTest(order=malformed_order):
                with self.assertRaises(TypeError):
                    subject.exponent_multiplicities(malformed_order, 1)
        for malformed_m in (True, False, 1.0, "1", None):
            with self.subTest(m=malformed_m):
                with self.assertRaises(TypeError):
                    subject.exponent_multiplicities(4, malformed_m)
        with self.assertRaisesRegex(ValueError, "nonnegative"):
            subject.exponent_multiplicities(4, -1)
        with self.assertRaisesRegex(ValueError, "three"):
            subject.edge_factor_polynomial(16, 3)
        with self.assertRaisesRegex(ValueError, "between"):
            subject.cyclic_interval_autocorrelation(8, 9, 1)
        with self.assertRaisesRegex(ValueError, "positive and even"):
            subject.half_shift_interval_invariant(7, 0)
        with self.assertRaisesRegex(RuntimeError, "exclusive cap"):
            subject.ResourceGuard().charge(
                "deliberate_refusal", subject.ACCOUNTED_WORK_UNIT_CAP_EXCLUSIVE
            )


if __name__ == "__main__":
    unittest.main()
