"""Tests for odd-notch squareclass entropy compression."""

from __future__ import annotations

import ast
import importlib.util
import itertools
import math
import subprocess
import sys
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "quadratic_family_squareclass_entropy_compression.py"
)
NOTE_PATH = MODULE_PATH.with_name("QUADRATIC_FAMILY_SQUARECLASS_ENTROPY_COMPRESSION.md")
PREDECESSOR_NOTE = MODULE_PATH.with_name(
    "QUADRATIC_FAMILY_PROFILE_CHI_SQUARE_BRIDGE.md"
)

SPEC = importlib.util.spec_from_file_location(
    "quadratic_family_squareclass_entropy_compression", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load squareclass compression replay")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def independent_irreducible_count(q_value: int, degree: int) -> int:
    def mobius(value: int) -> int:
        prime_factors = 0
        remainder = value
        divisor = 2
        while divisor * divisor <= remainder:
            if remainder % divisor == 0:
                remainder //= divisor
                prime_factors += 1
                if remainder % divisor == 0:
                    return 0
            divisor += 1
        if remainder > 1:
            prime_factors += 1
        return -1 if prime_factors % 2 else 1

    return (
        sum(
            mobius(divisor) * q_value ** (degree // divisor)
            for divisor in range(1, degree + 1)
            if degree % divisor == 0
        )
        // degree
    )


def independent_walsh(values: tuple[int, ...]) -> tuple[int, ...]:
    variable_count = len(values).bit_length() - 1
    output = []
    for frequency in range(len(values)):
        total = 0
        for point, value in enumerate(values):
            parity = (frequency & point).bit_count() % 2
            total += (-1) ** parity * value
        output.append(total)
    if 1 << variable_count != len(values):
        raise ValueError("not a cube")
    return tuple(output)


class QuadraticFamilySquareclassEntropyCompressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = MODULE.run()

    def test_irreducible_counts_and_two_entropy_dimensions(self) -> None:
        for q_value in (3, 5, 9):
            for top_degree in range(1, 8):
                counts = tuple(
                    independent_irreducible_count(q_value, degree)
                    for degree in range(1, top_degree + 1)
                )
                self.assertEqual(
                    MODULE.squareclass_dimension(q_value, top_degree), sum(counts)
                )
                self.assertEqual(
                    MODULE.modulus_degree(q_value, top_degree),
                    sum(degree * count for degree, count in enumerate(counts, start=1)),
                )
                self.assertLessEqual(
                    MODULE.squareclass_dimension(q_value, top_degree),
                    MODULE.modulus_degree(q_value, top_degree),
                )

    def test_strict_panels_cross_full_wall_but_pass_squareclass_gate(self) -> None:
        for values in MODULE.SAFE_INPUTS:
            panel = MODULE.compression_parameters(*values)
            self.assertGreater(panel["ell_r"], panel["M"])
            self.assertTrue(panel["full_residue_wall_crossed"])
            self.assertTrue(panel["squareclass_half_wall_safe"])
            self.assertTrue(panel["explicit_gate_safe"])
            self.assertGreater(panel["d"], panel["r"])

    def test_explicit_gate_is_monotone_toward_earlier_depths(self) -> None:
        q_value = 3
        h_value = 250
        ratios = []
        for depth in range(1, 4):
            panel = MODULE.compression_parameters(q_value, h_value, depth)
            numerator = q_value ** (panel["M"] - panel["r"])
            denominator = (
                2
                * MODULE.DISCREPANCY_CONSTANT
                * panel["M"] ** 11
                * (panel["ell_r"] + 1) ** 10
                * (1 << panel["K_r"])
            )
            ratios.append(Fraction(numerator, denominator))
        self.assertGreaterEqual(ratios[0], ratios[1])
        self.assertGreaterEqual(ratios[1], ratios[2])
        self.assertGreaterEqual(ratios[-1], 1)

    def test_walsh_transform_and_parseval_are_independent(self) -> None:
        for values in (
            (3, 1),
            (3, 1, 0, 2),
            (2, 0, 1, 3, 0, 1, 4, 0),
        ):
            actual = MODULE.walsh_transform(values)
            self.assertEqual(actual, independent_walsh(values))
            self.assertEqual(
                sum(value * value for value in actual),
                len(values) * sum(value * value for value in values),
            )

    def test_exact_squareclass_gate(self) -> None:
        panel = MODULE.squareclass_gate(
            (
                (3, 1, 0, 0, 0, 0, 0, 0),
                (0, 0, 2, 0, 1, 1, 0, 0),
            ),
            ((0, 1), (2, 3)),
            Fraction(1, 4),
        )
        self.assertEqual(panel["T"], 8)
        self.assertEqual(panel["Z"], 6)
        self.assertEqual(panel["Q_squared"], "3")
        self.assertEqual(panel["Q_squared"], panel["parseval_Q_squared"])
        self.assertTrue(panel["squared_gate_holds"])

    def test_orbit_multiplicities_recover_full_squareclass_entropy(self) -> None:
        for degree_sizes in MODULE.ORBIT_INPUTS:
            panel = MODULE.orbit_ledger(degree_sizes)
            expected_coordinates = math.prod(size + 1 for size in degree_sizes)
            expected_entropy = 1 << sum(degree_sizes)
            independent_sum = sum(
                math.prod(
                    math.comb(size, weight)
                    for size, weight in zip(degree_sizes, weights, strict=True)
                )
                for weights in itertools.product(
                    *(range(size + 1) for size in degree_sizes)
                )
            )
            self.assertEqual(panel["orbit_coordinates"], expected_coordinates)
            self.assertEqual(panel["sum_orbit_multiplicities"], expected_entropy)
            self.assertEqual(panel["sum_orbit_multiplicities"], independent_sum)
            self.assertTrue(panel["binomial_identity_holds"])

    def test_orbit_coordinate_upper_bound(self) -> None:
        for q_value in (3, 5, 9):
            for top_degree in range(1, 8):
                orbit_count = MODULE.orbit_coordinate_count(q_value, top_degree)
                upper = 2**top_degree * q_value ** (top_degree * (top_degree + 1) // 2)
                self.assertLessEqual(orbit_count, upper)

    def test_report_source_locks_claims_and_equation_balance(self) -> None:
        MODULE.check_source_blobs()
        self.assertEqual(
            self.report["theorems"]["discrepancy_constant"],
            MODULE.DISCREPANCY_CONSTANT,
        )
        self.assertFalse(self.report["open_gate"]["proved"])
        self.assertFalse(self.report["claim_boundary"]["individual_L_function_zero"])
        self.assertFalse(self.report["claim_boundary"]["integer_rh_or_grh"])
        self.assertEqual(self.report["resource_caps"]["characters_enumerated"], 0)
        for note_path in (PREDECESSOR_NOTE, NOTE_PATH):
            note = note_path.read_text(encoding="utf-8")
            self.assertEqual(note.count("\\["), note.count("\\]"))
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "2^{K_r}q^{-M}",
            "q^{M-r}",
            "log_qM+\\log_q\\log M",
            "quadratic sign quotient",
            "Krawtchouk orbit reduction",
            "KRAWLS",
            "not asserted",
        ):
            self.assertIn(marker, note)

    def test_invalid_inputs_fail_closed(self) -> None:
        self.assertEqual(MODULE.irreducible_count(9, 3), 240)
        for q_value in (True, 2, 4, 15, 45):
            with self.assertRaises(ValueError):
                MODULE.irreducible_count(q_value, 3)
        with self.assertRaises(ValueError):
            MODULE.compression_parameters(3, 5, 2)
        with self.assertRaises(ValueError):
            MODULE.walsh_transform((1, 2, 3))
        with self.assertRaises(ValueError):
            MODULE.squareclass_gate(((1, 0),), ((0, 1),), Fraction(1, 4))
        with self.assertRaises(ValueError):
            MODULE.orbit_ledger((8, 5))

    def test_optimized_mode_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn(
            "quadratic_family_squareclass_entropy_compression.v1",
            completed.stdout,
        )

    def test_producer_has_no_assert_statements(self) -> None:
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
