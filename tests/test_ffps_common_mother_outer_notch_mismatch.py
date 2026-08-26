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
    / "ffps_common_mother_outer_notch_mismatch.py"
)
SPEC = importlib.util.spec_from_file_location("notch_mismatch", MODULE_PATH)
assert SPEC and SPEC.loader
notch_mismatch = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(notch_mismatch)


class FfpsCommonMotherOuterNotchMismatchTest(unittest.TestCase):
    def test_exact_mismatch_and_corrected_ratio(self) -> None:
        for s in (1, 2, 3, 5, 8):
            mother = notch_mismatch.mother_at_integer(s)
            printed = notch_mismatch.l102740_declared_mother_at_integer(s)
            self.assertNotEqual(mother, printed)
            self.assertEqual(
                mother,
                notch_mismatch.qmul(notch_mismatch.q_at_integer(s), printed),
            )

    def test_three_way_outer_mismatch_and_d_out_relation(self) -> None:
        for s in (1, 2, 3, 5, 8):
            q_value = notch_mismatch.q_at_integer(s)
            explicit_direct = (
                notch_mismatch.explicit_piecewise_derivative_outer_at_integer(s)
            )
            explicit_closed = (
                notch_mismatch.explicit_derivative_outer_closed_at_integer(s)
            )
            self.assertEqual(explicit_direct, explicit_closed)
            stable_filter = notch_mismatch.l102740_stable_filter_at_integer(s)
            l102740_derivative = notch_mismatch.l102740_derivative_outer_at_integer(s)
            self.assertEqual(
                l102740_derivative,
                notch_mismatch.qscale(stable_filter, explicit_closed),
            )
            l102740_outer = notch_mismatch.l102740_outer_at_integer(s)
            common_outer = notch_mismatch.common_mother_outer_at_integer(s)
            self.assertEqual(
                common_outer,
                notch_mismatch.qmul(q_value, l102740_outer),
            )
            self.assertEqual(
                notch_mismatch.d_out_j_at_integer(s),
                notch_mismatch.qmul(
                    q_value,
                    notch_mismatch.qscale(stable_filter, explicit_closed),
                ),
            )

    def test_causal_inverse_has_square_root_scale_loss(self) -> None:
        for k in range(13):
            a, b = notch_mismatch.causal_inverse_peak(k)
            self.assertEqual(a * a + 2 * b * b, Fraction(2**k))
            mass = notch_mismatch.causal_inverse_l1_mass(k)
            if k:
                self.assertEqual(
                    mass,
                    notch_mismatch.qadd(
                        notch_mismatch.causal_inverse_l1_mass(k - 1),
                        notch_mismatch.causal_inverse_peak(k),
                    ),
                )

    def test_anti_causal_inverse_is_bounded_but_uses_future(self) -> None:
        for k in range(1, 13):
            a, b = notch_mismatch.anti_causal_inverse_magnitude(k)
            self.assertEqual(a * a + 2 * b * b, Fraction(1, 2**k))
            mass = notch_mismatch.anti_causal_inverse_l1_mass(k)
            if k > 1:
                self.assertEqual(
                    mass,
                    notch_mismatch.qadd(
                        notch_mismatch.anti_causal_inverse_l1_mass(k - 1),
                        notch_mismatch.anti_causal_inverse_magnitude(k),
                    ),
                )
            self.assertEqual(
                notch_mismatch.anti_causal_truncation_product(k),
                {
                    0: (Fraction(1), Fraction(0)),
                    -k: notch_mismatch.qscale(
                        -1, notch_mismatch.anti_causal_inverse_magnitude(k)
                    ),
                },
            )

    def test_guards(self) -> None:
        with self.assertRaises(TypeError):
            notch_mismatch.q_power_two_half(0.5)
        with self.assertRaises(ValueError):
            notch_mismatch.q_at_integer(0)
        with self.assertRaises(ValueError):
            notch_mismatch.causal_inverse_peak(-1)
        with self.assertRaises(ValueError):
            notch_mismatch.causal_inverse_l1_mass(-1)
        with self.assertRaises(ValueError):
            notch_mismatch.anti_causal_inverse_magnitude(0)
        with self.assertRaises(ValueError):
            notch_mismatch.anti_causal_inverse_l1_mass(0)
        with self.assertRaises(ValueError):
            notch_mismatch.anti_causal_truncation_product(0)

    def test_scope_and_caps(self) -> None:
        result = notch_mismatch.run()
        self.assertFalse(
            result["causal_inverse"][
                "subpower_transfer_from_naive_coefficientwise_causal_inverse"
            ]
        )
        self.assertIn(
            "positive causal inverse", result["causal_inverse"]["one_sided_transfer"]
        )
        self.assertEqual(result["anti_causal_inverse"]["global_l1_norm"], "1+sqrt(2)")
        self.assertIn("EXTSRC", result["impact"]["required_repair"])
        caps = result["resource_caps"]
        self.assertEqual(caps["piecewise_cells_integrated"], 3)
        self.assertEqual(caps["source_atoms_enumerated"], 0)
        self.assertEqual(caps["point_counts"], 0)


if __name__ == "__main__":
    unittest.main()
