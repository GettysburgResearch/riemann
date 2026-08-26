"""Independent tests for the uniform dyadic log-phase operator packet."""

from __future__ import annotations

import importlib.util
import json
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
    / "canonical_dyadic_log_phase_port.py"
)
SPEC = importlib.util.spec_from_file_location("canonical_dyadic_log_phase", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load canonical dyadic log-phase producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


def direct_mean_ceiling_minus_uniform(x: Fraction) -> Fraction:
    """Integrate ceil(x-t) from its two exact phase-cell lengths."""
    floor = x.numerator // x.denominator
    beta = x - floor
    return beta * (floor + 1) + (1 - beta) * floor


class CanonicalDyadicLogPhaseTests(unittest.TestCase):
    def test_mean_shift_identity_is_exact(self) -> None:
        for alpha in (Fraction(7, 11), Fraction(1, 2), Fraction(2, 5), Fraction(1, 3)):
            for j in range(4):
                x = j * alpha
                self.assertEqual(direct_mean_ceiling_minus_uniform(x), x)

    def test_k1_has_two_coefficient_moments(self) -> None:
        self.assertEqual(subject.sum_quads(subject.K1_COEFFICIENTS), subject.ZERO_QUAD)
        first_moment = subject.sum_quads(
            subject.qscale(coefficient, j)
            for j, coefficient in enumerate(subject.K1_COEFFICIENTS)
        )
        self.assertEqual(first_moment, subject.ZERO_QUAD)

    def test_phase_average_symbols_are_derived_exactly(self) -> None:
        for name, data in subject.REGIMES.items():
            actual = subject.phase_average_symbol(data["floors_j_alpha"])
            self.assertEqual(actual, subject.EXPECTED_AVERAGE_SYMBOLS[name])

    def test_phase_average_has_double_zero_in_every_regime(self) -> None:
        for name, symbol in subject.EXPECTED_AVERAGE_SYMBOLS.items():
            with self.subTest(name=name):
                self.assertEqual(
                    subject.derivative_at_one(symbol, 0), subject.ZERO_AFFINE
                )
                self.assertEqual(
                    subject.derivative_at_one(symbol, 1), subject.ZERO_AFFINE
                )

    def test_q3_and_q5_scalars_match_announced_formulas(self) -> None:
        q3_scalar = subject.EXPECTED_AVERAGE_SYMBOLS["q_3_4"][0]
        self.assertEqual(
            q3_scalar,
            (
                (Fraction(-1), Fraction(-1)),
                (Fraction(2), Fraction(1)),
            ),
        )
        q5_scalar = subject.EXPECTED_AVERAGE_SYMBOLS["q_5_7"][0]
        self.assertEqual(
            q5_scalar,
            (
                (Fraction(0), Fraction(1)),
                (Fraction(0), Fraction(-3)),
            ),
        )
        self.assertEqual(subject.EXPECTED_AVERAGE_SYMBOLS["q_ge_8"], ())

    def test_native_q2_symbol_is_unaveraged_k1(self) -> None:
        native = tuple(
            (coefficient, subject.ZERO_QUAD) for coefficient in subject.K1_COEFFICIENTS
        )
        self.assertEqual(len(native), 4)
        self.assertEqual(subject.derivative_at_one(native, 0), subject.ZERO_AFFINE)
        self.assertEqual(subject.derivative_at_one(native, 1), subject.ZERO_AFFINE)
        self.assertNotEqual(subject.derivative_at_one(native, 2), subject.ZERO_AFFINE)

    def test_phase_cell_means_vanish_and_energies_match(self) -> None:
        for name, data in subject.REGIMES.items():
            cells = subject.phase_cells(data["floors_j_alpha"], data["threshold_order"])
            with self.subTest(name=name):
                self.assertEqual(subject.cell_mean(cells), subject.ZERO_AFFINE)
                self.assertEqual(
                    subject.cell_energy(cells), subject.EXPECTED_ENERGIES[name]
                )

    def test_q_ge_8_energy_is_two_times_three_plus_sqrt2_times_alpha(self) -> None:
        self.assertEqual(
            subject.EXPECTED_ENERGIES["q_ge_8"],
            (
                (Fraction(0), Fraction(0)),
                (Fraction(6), Fraction(2)),
            ),
        )
        cells = subject.phase_cells((0, 0, 0, 0), (1, 2, 3))
        self.assertEqual(
            tuple(value for _, value in cells),
            (
                (Fraction(-1), Fraction(0)),
                (Fraction(1), Fraction(1)),
                (Fraction(0), Fraction(-1)),
                subject.ZERO_QUAD,
            ),
        )

    def test_q4_and_q8_boundary_cells_are_zero_length_only(self) -> None:
        q34_cells = subject.phase_cells((0, 0, 1, 1), (2, 1, 3))
        qge8_cells = subject.phase_cells((0, 0, 0, 0), (1, 2, 3))

        def evaluate(value: subject.Affine, alpha: Fraction) -> subject.Quad:
            return subject.qadd(value[0], subject.qscale(value[1], alpha))

        q4_lengths = tuple(evaluate(length, Fraction(1, 2)) for length, _ in q34_cells)
        q8_lengths = tuple(evaluate(length, Fraction(1, 3)) for length, _ in qge8_cells)
        self.assertEqual(
            q4_lengths,
            (
                subject.ZERO_QUAD,
                (Fraction(1, 2), Fraction(0)),
                subject.ZERO_QUAD,
                (Fraction(1, 2), Fraction(0)),
            ),
        )
        self.assertEqual(q8_lengths[-1], subject.ZERO_QUAD)

    def test_fixture_rebuild_has_exact_provenance_and_no_floats(self) -> None:
        rebuilt = subject.build_fixture()
        locked = json.loads(subject.OUTPUT_PATH.read_text(encoding="utf-8"))
        self.assertEqual(locked, rebuilt)
        subject.no_floats(locked)
        scope = locked["scope"]
        self.assertLessEqual(
            scope["symbolic_term_operations_used"],
            scope["symbolic_term_operation_cap"],
        )
        self.assertTrue(scope["operator_theorem_on_norm_step_extensions_only"])
        self.assertFalse(scope["L_function_family_evaluated"])
        self.assertFalse(scope["rh_or_grh_proved"])

    def test_producer_replays_under_optimized_python(self) -> None:
        result = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("PASS_CANONICAL_DYADIC_LOG_PHASE_PORT", result.stdout)


if __name__ == "__main__":
    unittest.main()
