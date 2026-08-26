from __future__ import annotations

import importlib.util
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
    / "ffps_relative_boundary_trace_tower_gate.py"
)
SPEC = importlib.util.spec_from_file_location("boundary_trace_tower_gate", MODULE_PATH)
assert SPEC and SPEC.loader
boundary_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(boundary_gate)


class RelativeBoundaryTraceTowerGateTest(unittest.TestCase):
    def test_exterior_selector_is_exact_d_cycle_indicator(self) -> None:
        for degree in range(1, 9):
            for cycle_type in boundary_gate.partitions(degree):
                expected = Fraction(int(len(cycle_type) == 1))
                self.assertEqual(
                    boundary_gate.irreducible_cycle_selector_trace(cycle_type),
                    expected,
                )

    def test_irreducible_selector_kills_universal_root_incidence(self) -> None:
        for degree in range(2, 9):
            for cycle_type in boundary_gate.partitions(degree):
                self.assertEqual(
                    boundary_gate.selected_incidence_trace(cycle_type),
                    0,
                )
        self.assertEqual(boundary_gate.selected_incidence_trace((1,)), 1)

    def test_fixed_divisor_has_base_shadow_but_not_tower_equality(self) -> None:
        profile = (2, 3, 5)
        self.assertEqual(boundary_gate.fixed_boundary_trace(profile, 1), 0)
        self.assertEqual(boundary_gate.fixed_boundary_trace(profile, 2), 2)
        self.assertEqual(boundary_gate.fixed_boundary_trace(profile, 3), 3)
        self.assertEqual(boundary_gate.fixed_boundary_trace(profile, 5), 5)
        self.assertEqual(boundary_gate.fixed_boundary_trace(profile, 30), 10)

    def test_full_trace_tower_recovers_degree_profile(self) -> None:
        profile = (2, 2, 3, 5, 5, 5)
        maximum = max(profile)
        tower = {
            extension: boundary_gate.fixed_boundary_trace(profile, extension)
            for extension in range(1, maximum + 1)
        }
        self.assertEqual(
            boundary_gate.recover_degree_profile(tower, maximum),
            {1: 0, 2: 2, 3: 1, 4: 0, 5: 3},
        )

    def test_selector_absolute_rank_mass(self) -> None:
        for degree in range(1, 9):
            self.assertEqual(
                boundary_gate.selector_absolute_rank_mass(degree),
                Fraction(2 ** (degree - 1), degree),
            )

    def test_input_firewalls_and_resource_caps(self) -> None:
        with self.assertRaises(ValueError):
            boundary_gate.partitions(0)
        with self.assertRaises(ValueError):
            boundary_gate.irreducible_cycle_selector_trace(())
        with self.assertRaises(ValueError):
            boundary_gate.fixed_boundary_trace((), 1)
        with self.assertRaises(ValueError):
            boundary_gate.recover_degree_profile({1: 0}, 2)
        caps = boundary_gate.run()["resource_caps"]
        self.assertEqual(caps["maximum_cycle_degree"], 8)
        self.assertEqual(caps["cycle_types_checked"], 66)
        self.assertEqual(caps["finite_field_points"], 0)
        self.assertEqual(caps["closed_places_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
