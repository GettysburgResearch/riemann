"""Tests for the block-checkerboard coset interferometer."""

from __future__ import annotations

import ast
import importlib.util
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
    / "ffps_block_checkerboard_coset_interferometer.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_BLOCK_CHECKERBOARD_COSET_INTERFEROMETER.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_block_checkerboard_coset_interferometer", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load block-checkerboard interferometer module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class BlockCheckerboardCosetInterferometerTests(unittest.TestCase):
    def test_bounded_replay(self) -> None:
        report = MODULE.run_checks()
        self.assertEqual(
            report["status"],
            "EXACT_FORMAL_BLOCK_INTERFEROMETER_AND_TRANSVERSE_PATH_MODEL",
        )
        self.assertEqual(report["resource_ledger"]["direct_gram_cells"], 2304)
        self.assertEqual(report["resource_ledger"]["selected_graph_modes"], 120)

    def test_block_leverage_factorization(self) -> None:
        row = MODULE.block_panel((5, 13, 17), ((0, 1), (2,)))
        self.assertEqual(row["quotient_order_h"], 4)
        self.assertEqual(row["coset_size"], 24)
        self.assertEqual(row["restricted_constant_eigenvalue"], 559)
        self.assertEqual(row["indicator_gram_energy"], 13416)
        self.assertEqual(row["sharp_uniform_weight"], 4)
        self.assertEqual(row["sharp_hard_leverage"], "384/559")
        self.assertEqual(row["product_of_block_leverages"], "384/559")

    def test_direct_coset_gram_rows(self) -> None:
        row = MODULE.direct_coset_gram_control((5, 13, 17), ((0, 1), (2,)))
        self.assertEqual(
            row,
            {
                "phase_coordinates": 96,
                "cosets": 4,
                "coset_size": 24,
                "direct_gram_cells": 2304,
                "common_row_sum": 559,
            },
        )

    def test_formula_panel_has_strict_amplification(self) -> None:
        row = MODULE.block_panel((5, 13, 17, 29), ((0, 1), (2, 3)))
        block_leverage = Fraction(row["sharp_hard_leverage"])
        full_leverage = Fraction(row["complete_frame_leverage"])
        self.assertEqual(block_leverage, Fraction(2688, 6751))
        self.assertEqual(full_leverage, Fraction(448, 945))
        self.assertLess(block_leverage, full_leverage)
        self.assertTrue(row["strictly_improves_complete_frame"])

    def test_off_coset_fourier_identity_and_atomic_ledger(self) -> None:
        for block_count in range(1, 6):
            row = MODULE.interferometer_control(
                block_count, MODULE.deterministic_atoms(block_count)
            )
            quotient_order = 1 << block_count
            self.assertEqual(row["averaged_selected_atomic_diagonal"], 1)
            self.assertEqual(row["same_coset_kernel"], 0)
            self.assertEqual(
                Fraction(row["different_coset_kernel"]),
                Fraction(quotient_order, quotient_order - 1),
            )

    def test_interferometer_zero_threshold(self) -> None:
        row = MODULE.interferometer_control(4, ((0, (3, -2)),))
        self.assertEqual(row["interferometer"], "0")
        self.assertEqual(row["total_selected_energy"], row["off_coset_zero_target"])
        self.assertEqual(row["total_selected_energy"], 195)

    def test_endpoint_disjoint_path_spectrum(self) -> None:
        row = MODULE.path_block_control((1, 2, 3), degree=2)
        self.assertEqual(row["ambient_cycle_dimension"], 0)
        self.assertEqual(row["selected_boundary_rank"], 3)
        self.assertEqual(row["nonzero_invariant_selected_modes"], 0)
        self.assertEqual(row["branch_vertex_multiplicities"], {"2": 3, "4": 3, "6": 1})
        self.assertEqual(row["maximally_extended_hc1_sum"], 34)
        self.assertEqual(row["average_maximally_extended_hc1"], "34/7")
        self.assertEqual(row["average_hc1_exact_excess"], "6/7")
        self.assertEqual(row["average_removable_puncture_tax"], "78/7")

    def test_invalid_inputs_fail_closed(self) -> None:
        invalid_panels = (
            ((), ()),
            ((5, 5), ((0,), (1,))),
            ((3,), ((0,),)),
            ((9,), ((0,),)),
            ((True,), ((0,),)),
            ((5, 13), ((0,),)),
            ((5, 13), ((0, 1), (1,))),
            ((5, 13), ((), (0, 1))),
        )
        for primes, blocks in invalid_panels:
            with self.assertRaises(ValueError):
                MODULE.validate_panel(primes, blocks)
        for lengths, degree in (
            ((), 1),
            ((0,), 1),
            ((True,), 1),
            ((1.5,), 1),
            ((1,), 0),
            ((1,), True),
        ):
            with self.assertRaises(ValueError):
                MODULE.path_block_control(lengths, degree)

    def test_optimized_replay(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10.0,
        )
        self.assertIn("EXACT_FORMAL_BLOCK_INTERFEROMETER", completed.stdout)

    def test_note_firewalls_and_no_asserts(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "block-leverage factorization theorem",
            "off-coset interferometer",
            "maximal-extension firewall",
            "coupled candidate, not a native-source theorem",
            "OPEN / CENTRAL",
        ):
            self.assertIn(marker, note)
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))


if __name__ == "__main__":
    unittest.main()
