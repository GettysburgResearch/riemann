from __future__ import annotations

import importlib.util
import json
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
    / "ffps_critical_beta_spectral_witness_principle.py"
)
SPEC = importlib.util.spec_from_file_location(
    "critical_beta_spectral_witness_principle", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class CriticalBetaSpectralWitnessPrincipleTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_subpower_coordinate_count_makes_l2_and_max_equivalent(self) -> None:
        panel = subject.ell2_linfty_panel()
        for row in panel["rows"]:
            size = row["coordinate_count"]
            maximum = Fraction(row["maximum_square"])
            energy = Fraction(row["energy"])
            self.assertLessEqual(maximum, energy)
            self.assertLessEqual(energy, size * maximum)
        self.assertIn("N(X)=X^o(1)", panel["subpower_consequence"])

    def test_weight_only_parseval_and_central_notch(self) -> None:
        panel = subject.weight_mass_panel()
        self.assertEqual(Fraction(panel["total_weight"]), Fraction(2))
        self.assertEqual(Fraction(panel["spatial_energy"]), Fraction(2))
        self.assertEqual(Fraction(panel["central_weight"]), Fraction(0))
        self.assertEqual(
            [Fraction(value) for value in panel["weight_mass"]],
            [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(1, 2)],
        )

    def test_gaussian_scale_filter_reconstructs(self) -> None:
        omega = (Fraction(3, 25), Fraction(4, 25))
        values = tuple(
            (Fraction(index + 1, index + 2), Fraction((-1) ** index, index + 3))
            for index in range(subject.SCALE_DEPTH)
        )
        filtered = subject.scale_filter(values, omega)
        self.assertEqual(subject.inverse_scale_filter(filtered, omega), values)

    def test_common_lattice_scale_bounds(self) -> None:
        panel = subject.common_lattice_scale_panel()
        beta = Fraction(panel["beta_weighted_max_square"])
        single_lower, single_upper = (
            Fraction(value) for value in panel["single_filter_bounds"]
        )
        squared_lower, squared_upper = (
            Fraction(value) for value in panel["squared_filter_bounds"]
        )
        self.assertLessEqual(single_lower, beta)
        self.assertLessEqual(beta, single_upper)
        self.assertLessEqual(squared_lower, beta)
        self.assertLessEqual(beta, squared_upper)

    def test_scope_fences(self) -> None:
        result = subject.run(check_sources=False)
        self.assertTrue(result["scope"]["continuum_replaced_by_exact_lattice"])
        self.assertTrue(
            result["scope"]["subpower_lattice_replaced_by_weighted_maximum"]
        )
        self.assertFalse(result["scope"]["raw_unweighted_pointwise_bound_equivalent"])
        self.assertFalse(result["scope"]["retained_witness_estimate_proved"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertIn(
            "not the raw D_X",
            result["single_witness"]["unweighted_warning"],
        )

    def test_fixture_and_resource_caps(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(json.loads(json.dumps(result)), fixture)
        self.assertEqual(result["resource_caps"]["toy_fourier_cells"], 4)
        self.assertEqual(result["resource_caps"]["floating_point_operations"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.scale_filter((), (Fraction(1, 5), Fraction(0)))
        with self.assertRaises(ValueError):
            subject.inverse_scale_filter((), (Fraction(1, 5), Fraction(0)))
        with self.assertRaises(ValueError):
            subject.weighted_max_square(
                (((Fraction(1), Fraction(0)),),),
                (Fraction(1), Fraction(2)),
            )


if __name__ == "__main__":
    unittest.main()
