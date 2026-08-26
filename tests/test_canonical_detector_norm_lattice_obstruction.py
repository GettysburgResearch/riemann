"""Independent tests for the detector norm-lattice obstruction packet."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "canonical_detector_norm_lattice_obstruction.py"
)
SPEC = importlib.util.spec_from_file_location("norm_lattice_obstruction", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load norm-lattice producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class NormLatticeObstructionTests(unittest.TestCase):
    def test_native_shift_exactly_detects_integral_powers(self) -> None:
        self.assertEqual(subject.native_integer_shift(3, 1), 0)
        self.assertEqual(subject.native_integer_shift(3, 9), 2)
        self.assertEqual(subject.native_integer_shift(4, 4), 1)
        self.assertIsNone(subject.native_integer_shift(3, 2))
        self.assertIsNone(subject.native_integer_shift(4, 2))
        self.assertIsNone(subject.native_integer_shift(9, 3))

    def test_endpoint_shift_uses_exact_ceiling_without_logs(self) -> None:
        self.assertEqual(
            tuple(subject.endpoint_shift(3, 2**j) for j in range(4)),
            (0, 1, 2, 2),
        )
        self.assertEqual(
            tuple(subject.endpoint_shift(5, 2**j) for j in range(4)),
            (0, 1, 1, 2),
        )
        self.assertEqual(
            tuple(subject.endpoint_shift(11, 2**j) for j in range(4)),
            (0, 1, 1, 1),
        )

    def test_canonical_dilations_are_non_native_for_odd_controls(self) -> None:
        for base in (3, 5, 7, 9, 11, 25):
            for dilation in subject.CANONICAL_DILATIONS:
                self.assertIsNone(subject.native_integer_shift(base, dilation))

    def test_minimal_wavelet_double_zero_survives_only_at_q2_controls(self) -> None:
        self.assertEqual(subject.collapsed_k1(2)["constant_zero_multiplicity"], 2)
        for base in subject.CONTROL_BASES:
            expected = 2 if base == 2 else 1
            self.assertEqual(
                subject.collapsed_k1(base)["constant_zero_multiplicity"], expected
            )

    def test_three_aliasing_cases_have_exact_derivatives(self) -> None:
        self.assertEqual(
            subject.collapsed_k1(3)["derivatives_at_one_until_first_nonzero"][-1],
            [0, 1],
        )
        self.assertEqual(
            subject.collapsed_k1(5)["derivatives_at_one_until_first_nonzero"][-1],
            [-1, -1],
        )
        self.assertEqual(
            subject.collapsed_k1(11)["derivatives_at_one_until_first_nonzero"][-1],
            [-1, 0],
        )

    def test_common_native_dilation_requires_multiplicative_dependence(self) -> None:
        self.assertIsNone(subject.common_native_dilation((3, 5, 7)))
        self.assertEqual(subject.common_native_dilation((3, 9)), 9)
        self.assertEqual(subject.common_native_dilation((3, 27)), 27)

    def test_prime_power_commensurability_rule(self) -> None:
        for exponent in range(1, 5):
            base = 2**exponent
            for dilation_exponent in range(1, 9):
                shift = subject.native_integer_shift(base, 2**dilation_exponent)
                expected = (
                    dilation_exponent // exponent
                    if dilation_exponent % exponent == 0
                    else None
                )
                self.assertEqual(shift, expected)

    def test_fixture_matches_rebuild_and_has_no_floats(self) -> None:
        rebuilt = subject.build_fixture()
        locked = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(locked, rebuilt)
        subject.no_floats(locked)
        self.assertEqual(locked["scope"]["source_atoms_used"], 27)
        self.assertLessEqual(
            locked["scope"]["source_atoms_used"], locked["scope"]["source_atom_cap"]
        )

    def test_producer_replays_under_optimized_python(self) -> None:
        result = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS_CANONICAL_DETECTOR_NORM_LATTICE_OBSTRUCTION", result.stdout)


if __name__ == "__main__":
    unittest.main()
