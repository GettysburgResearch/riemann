from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_critical_beta_fourier_lattice_compression.py"
)
SPEC = importlib.util.spec_from_file_location("critical_beta_lattice", MODULE_PATH)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class CriticalBetaFourierLatticeCompressionTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_exact_four_cell_parseval(self) -> None:
        panel = subject.parseval_panel()
        for row in panel["rows"]:
            self.assertEqual(row["spectral_energy"], 4 * row["spatial_energy"])

    def test_exact_stair_block_exponent(self) -> None:
        for binary_scale in range(3, subject.BINARY_BLOCK_CAP + 1):
            self.assertEqual(
                subject.stair_block_exponent(binary_scale),
                -(binary_scale**2) + 4 * binary_scale - 2,
            )

    def test_rank_count(self) -> None:
        panel = subject.rank_panel(12)
        for row in panel["rows"]:
            self.assertEqual(
                row["nonzero_gram_rank_upper_bound"],
                2 * row["retained_radius_surrogate"],
            )
        self.assertIn("X^o(1)", panel["theorem_scale"])

    def test_scope_fences(self) -> None:
        result = subject.run(check_sources=False)
        self.assertFalse(result["scope"]["arbitrary_vector_operator_norm_compression"])
        self.assertTrue(result["scope"]["exact_continuous_to_discrete_identity"])
        self.assertTrue(result["scope"]["critical_tail_uses_only_trivial_beta_bound"])
        self.assertTrue(result["scope"]["finite_rank_is_not_an_energy_bound"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])
        self.assertFalse(
            result["finite_rank_gram"]["estimate_proved_for_retained_form"]
        )
        self.assertFalse(
            result["finite_rank_gram"]["higher_fixed_notch_reduces_rank_further"]
        )
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_gaussian_arithmetic(self) -> None:
        self.assertEqual(subject.gaussian_mul((2, 3), (-1, 4)), (-14, 5))
        self.assertEqual(subject.gaussian_abs_square((3, -4)), 25)
        self.assertEqual(subject.fourth_root_power(-1), (0, -1))

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.dft4((1, 2, 3))
        with self.assertRaises(ValueError):
            subject.stair_block_exponent(2)
        with self.assertRaises(ValueError):
            subject.rank_panel(0)


if __name__ == "__main__":
    unittest.main()
