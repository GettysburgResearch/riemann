"""Tests for the shared-fibre Wick occupancy spectrum packet."""

from __future__ import annotations

import ast
import importlib.util
import subprocess
import sys
import unittest
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_shared_fibre_wick_occupancy_spectrum.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_SHARED_FIBRE_WICK_OCCUPANCY_SPECTRUM.md")

SPEC = importlib.util.spec_from_file_location(
    "ffps_shared_fibre_wick_occupancy_spectrum", MODULE_PATH
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load shared-fibre Wick module")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SharedFibreWickOccupancySpectrumTests(unittest.TestCase):
    def test_source_locks_resolve_exact_git_blobs(self) -> None:
        MODULE.check_source_blobs()
        MODULE.check_source_lock_manifest()
        self.assertEqual(len(MODULE.SOURCE_BLOBS), 8)

    def test_allowed_cells_are_fixed_raw_quadratic_classes(self) -> None:
        for ell, rho in (*MODULE.CONTROL_PAIRS, MODULE.HELD_OUT_PAIR):
            cells = MODULE.allowed_cells(ell, rho, sigma=1, tau=-1)
            self.assertEqual(len(cells), ((ell - 1) // 2) * ((rho - 1) // 2))
            expected_x_character = MODULE.legendre_symbol(-1, ell)
            for x_value, y_value in cells:
                self.assertEqual(
                    MODULE.legendre_symbol(x_value, ell), expected_x_character
                )
                self.assertEqual(MODULE.legendre_symbol(y_value, rho), -1)

    def test_owner_cofactor_map_has_exact_uniform_envelope_fibres(self) -> None:
        for ell, rho in (*MODULE.CONTROL_PAIRS, MODULE.HELD_OUT_PAIR):
            counts = MODULE.residue_envelope_counts(ell, rho)
            expected_cells = set(MODULE.allowed_cells(ell, rho))
            self.assertEqual(set(counts), expected_cells)
            self.assertEqual(
                counts,
                Counter({cell: (ell - 1) * (rho - 1) for cell in expected_cells}),
            )

    def test_physical_map_retains_shared_conductors_and_unit_classes(self) -> None:
        ell, rho = 5, 7
        x_value, y_value = MODULE.physical_residue_map(
            ell,
            rho,
            q_owner=1,
            v_cofactor=2,
            p_owner=4,
            u_cofactor=3,
        )
        self.assertEqual(x_value, (-1 * rho**2 * 2**2) % ell)
        self.assertEqual(y_value, (4 * ell**2 * 3**2) % rho)
        self.assertEqual(MODULE.legendre_symbol(x_value, ell), 1)
        self.assertEqual(MODULE.legendre_symbol(y_value, rho), 1)

    def test_arbitrary_occupancy_pullback_equals_direct_off_atomic_sum(self) -> None:
        ell, rho = 5, 7
        assignments = (0, 0, 1, 4, 4)
        vector = tuple(Fraction(value) for value in (2, -1, 3, 1, -2))
        matrix = MODULE.occupancy_wick_matrix(ell, rho, assignments)
        self.assertEqual(
            MODULE.quadratic_form(matrix, vector),
            MODULE.direct_off_atomic_form(ell, rho, assignments, vector),
        )

    def test_kernel_of_residue_aggregation_is_negative_diagonal(self) -> None:
        ell, rho = 5, 7
        dimension = len(MODULE.allowed_cells(ell, rho))
        assignments = (0, 0)
        vector = (Fraction(1), Fraction(-1))
        self.assertEqual(
            MODULE.aggregate_vector(dimension, assignments, vector),
            tuple(Fraction() for _ in range(dimension)),
        )
        self.assertEqual(
            MODULE.quadratic_form(
                MODULE.occupancy_wick_matrix(ell, rho, assignments),
                vector,
            ),
            -2 * MODULE.atomic_diagonal(ell, rho),
        )

    def test_same_residue_aggregate_does_not_determine_literal_energy(self) -> None:
        ell, rho = 5, 7
        dimension = len(MODULE.allowed_cells(ell, rho))
        assignments = (0, 0)
        first = (Fraction(1), Fraction(1))
        second = (Fraction(3, 2), Fraction(1, 2))
        self.assertEqual(
            MODULE.aggregate_vector(dimension, assignments, first),
            MODULE.aggregate_vector(dimension, assignments, second),
        )
        matrix = MODULE.occupancy_wick_matrix(ell, rho, assignments)
        self.assertEqual(
            MODULE.quadratic_form(matrix, second)
            - MODULE.quadratic_form(matrix, first),
            -Fraction(1, 2) * MODULE.atomic_diagonal(ell, rho),
        )

    def test_residue_sufficiency_is_equivalent_to_injective_aggregation(self) -> None:
        self.assertTrue(MODULE.aggregation_is_injective((0, 2, 4, 6)))
        self.assertFalse(MODULE.aggregation_is_injective((0, 2, 2, 6)))

        ell, rho = 5, 7
        assignments = (0, 1, 4)
        vector = tuple(Fraction(value) for value in (2, -3, 5))
        aggregate = MODULE.aggregate_vector(
            len(MODULE.allowed_cells(ell, rho)), assignments, vector
        )
        self.assertEqual(
            sum((value * value for value in aggregate), Fraction()),
            sum((value * value for value in vector), Fraction()),
        )

    def test_simple_complete_cell_spectrum_is_full_rank_indefinite(self) -> None:
        for ell, rho in (*MODULE.CONTROL_PAIRS, MODULE.HELD_OUT_PAIR):
            MODULE.verify_spectrum(ell, rho)
            dimension = ((ell - 1) // 2) * ((rho - 1) // 2)
            matrix = MODULE.simple_complete_cell_wick_matrix(ell, rho)
            self.assertEqual(MODULE.matrix_rank(matrix), dimension)
            positive, negative, zero = MODULE.simple_inertia(ell, rho)
            self.assertGreater(positive, 0)
            self.assertGreater(negative, 0)
            self.assertEqual(zero, 0)

    def test_absent_zero_eigenvalue_at_three_seven_has_zero_multiplicity(self) -> None:
        spectrum = {row["space"]: row for row in MODULE.simple_spectrum(3, 7)}
        row = spectrum["mean_zero_x_constant"]
        self.assertEqual(row["eigenvalue"], "0")
        self.assertEqual(row["multiplicity"], 0)
        self.assertEqual(
            MODULE.matrix_rank(MODULE.simple_complete_cell_wick_matrix(3, 7)),
            3,
        )

    def test_singleton_and_collision_only_counterfeits_vanish(self) -> None:
        self.assertEqual(
            MODULE.occupancy_wick_matrix(5, 7, (0,)),
            ((Fraction(),),),
        )
        assignments = tuple(range(len(MODULE.allowed_cells(5, 7))))
        collision_only = MODULE.strict_double_collision_matrix(assignments)
        self.assertEqual(MODULE.matrix_rank(collision_only), 0)
        self.assertGreater(
            MODULE.matrix_rank(MODULE.simple_complete_cell_wick_matrix(5, 7)),
            0,
        )

    def test_nontrivial_incomplete_occupancy_is_singular(self) -> None:
        control = MODULE.singular_rectangle_control()
        self.assertEqual((control["ell"], control["rho"]), (5, 11))
        self.assertEqual(control["rank"], 5)
        self.assertEqual(control["null_vector"], ["-1", "-1", "-1", "1", "1", "1"])
        self.assertEqual(
            control["scaled_matrix"][0],
            ["0", "-4", "-4", "-10", "1", "1"],
        )

    def test_exact_singular_rectangle_family_and_symmetric_orientation(self) -> None:
        parameters = (
            *MODULE.RECTANGLE_CONTROL_PARAMETERS,
            MODULE.RECTANGLE_HELD_OUT_PARAMETER,
        )
        for base_prime, n in parameters:
            for transposed in (False, True):
                control = MODULE.singular_rectangle_family_member(
                    base_prime, n, transposed=transposed
                )
                self.assertEqual(control["rank"], 2 * n - 1)
                self.assertEqual(len(control["occupied_cell_indices"]), 2 * n)
                self.assertEqual(
                    control["shape"], [n, 2] if transposed else [2, n]
                )
                self.assertEqual(
                    control["rho"] if transposed else control["ell"],
                    base_prime,
                )

        unmaterialized = MODULE.singular_rectangle_symbolic_spectrum(5, 13)
        self.assertEqual(unmaterialized["large_prime"], 61)
        self.assertEqual(unmaterialized["dimension"], 26)
        self.assertEqual(unmaterialized["rank"], 25)
        self.assertEqual(unmaterialized["nullity"], 1)
        self.assertEqual(
            [
                row["multiplicity"]
                for row in unmaterialized["spectral_blocks"]
                if row["eigenvalue"] == "0"
            ],
            [1],
        )
        with self.assertRaises(RuntimeError):
            MODULE.singular_rectangle_family_member(5, 13)

    def test_ambient_envelope_control_has_both_signs_and_full_rank(self) -> None:
        for ell, rho in (*MODULE.CONTROL_PAIRS, MODULE.HELD_OUT_PAIR):
            positive, negative, zero = MODULE.ambient_envelope_inertia(ell, rho)
            cells = ((ell - 1) // 2) * ((rho - 1) // 2)
            multiplicity = (ell - 1) * (rho - 1)
            self.assertEqual(positive, cells)
            self.assertEqual(negative, (multiplicity - 1) * cells)
            self.assertEqual(zero, 0)

    def test_report_preserves_scope_and_resource_firewalls(self) -> None:
        report = MODULE.build_report()
        self.assertEqual(
            report["status"],
            "EXACT_FIXED_FIBRE_IDENTITY_AND_RESIDUE_FORGETTING_CRITERION",
        )
        self.assertEqual(report["arithmetic_class"], "MIXED")
        self.assertIn(
            "literal diagonal energy",
            report["ontology"]["exact_scalar_sufficient_statistic"],
        )
        self.assertIn(
            "noncancellation in any complete native conductor fibre",
            report["not_proved"],
        )
        resources = report["resource_ledger"]
        self.assertEqual(resources["maximum_simple_matrix_dimension"], 15)
        self.assertEqual(resources["maximum_ambient_envelope_points"], 900)
        self.assertEqual(resources["singular_rectangle_control_members"], 8)
        self.assertEqual(resources["maximum_singular_rectangle_atoms"], 14)
        self.assertEqual(resources["floating_point_operations"], 0)
        self.assertEqual(resources["live_source_atoms_enumerated"], 0)

    def test_invalid_inputs_fail_closed(self) -> None:
        for pair in ((2, 3), (3, 3), (4, 5), (True, 5)):
            with self.assertRaises(ValueError):
                MODULE.validate_pair(*pair)
        with self.assertRaises(ValueError):
            MODULE.allowed_cells(3, 5, sigma=0)
        with self.assertRaises(ValueError):
            MODULE.allowed_cells(3, 5, sigma=True)
        with self.assertRaises(ValueError):
            MODULE.physical_residue_map(3, 5, 0, 1, 1, 1)
        with self.assertRaises(ValueError):
            MODULE.aggregation_matrix(2, (0, 2))
        with self.assertRaises(ValueError):
            MODULE.aggregation_is_injective((0, -1))
        with self.assertRaises(ValueError):
            MODULE.singular_rectangle_family_member(3, 3)
        with self.assertRaises(ValueError):
            MODULE.singular_rectangle_family_member(5, 5)
        with self.assertRaises(ValueError):
            MODULE.matrix_rank(((Fraction(1),), (Fraction(1), Fraction(2))))

    def test_note_preserves_ontology_and_global_firewalls(self) -> None:
        note = NOTE_PATH.read_text(encoding="utf-8")
        for marker in (
            "shared marked fibre",
            "not an independent marked-place product",
            "raw Legendre class",
            "MPD-W2.2 — exact arbitrary-occupancy pullback",
            "residue-only forgetting criterion",
            "exact sufficient statistic",
            "live occupancy",
            "ONEPLACEWEIL",
            "RELTRACE",
            "principal binding",
            "RH and GRH remain unproved",
        ):
            self.assertIn(marker, note)

    def test_no_control_characters_or_assert_statements(self) -> None:
        for path in (MODULE_PATH, NOTE_PATH):
            text = path.read_text(encoding="utf-8")
            self.assertFalse(
                any(
                    ord(character) < 32 and character not in ("\n", "\r", "\t")
                    for character in text
                )
            )
        tree = ast.parse(MODULE_PATH.read_text(encoding="utf-8"))
        self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))

    def test_optimized_producer_replays(self) -> None:
        completed = subprocess.run(
            [sys.executable, "-O", str(MODULE_PATH), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=20.0,
        )
        self.assertIn(
            "EXACT_FIXED_FIBRE_IDENTITY_AND_RESIDUE_FORGETTING_CRITERION",
            completed.stdout,
        )


if __name__ == "__main__":
    unittest.main()
