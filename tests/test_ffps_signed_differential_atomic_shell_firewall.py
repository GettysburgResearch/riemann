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
    / "ffps_signed_differential_atomic_shell_firewall.py"
)
NOTE_PATH = MODULE_PATH.with_name("FFPS_SIGNED_DIFFERENTIAL_ATOMIC_SHELL_FIREWALL.md")
SPEC = importlib.util.spec_from_file_location("signed_atomic_shell", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load signed atomic shell replay")
signed_atomic_shell = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(signed_atomic_shell)


class FfpsSignedDifferentialAtomicShellFirewallTest(unittest.TestCase):
    def test_display_math_delimiters_are_balanced(self) -> None:
        depth = 0
        for line in NOTE_PATH.read_text(encoding="utf-8").splitlines():
            if line == r"\[":
                depth += 1
                self.assertEqual(depth, 1)
            elif line == r"\]":
                depth -= 1
                self.assertGreaterEqual(depth, 0)
        self.assertEqual(depth, 0)

    def test_frozen_source_blobs(self) -> None:
        signed_atomic_shell.check_source_blobs()

    def test_exact_dyadic_atoms(self) -> None:
        atoms = signed_atomic_shell.atomic_coefficients()
        self.assertEqual(atoms[0], (Fraction(5), Fraction(0)))
        self.assertEqual(atoms[1], (Fraction(-10), Fraction(-10)))
        self.assertEqual(atoms[2], (Fraction(15), Fraction(20)))
        self.assertEqual(atoms[3], (Fraction(-20), Fraction(-10)))
        self.assertEqual(atoms[4], (Fraction(10), Fraction(0)))

    def test_negative_atomic_mass(self) -> None:
        self.assertEqual(
            signed_atomic_shell.negative_atomic_mass(),
            (Fraction(30), Fraction(20)),
        )
        result = signed_atomic_shell.run()
        self.assertEqual(result["prime_singleton_beta_weight"], "1/12")
        self.assertEqual(
            result["beta_weighted_negative_atomic_mass"], "5/2+5/3*sqrt(2)"
        )
        self.assertEqual(signed_atomic_shell.beta_weight(2), Fraction(1, 12))
        with self.assertRaises(ValueError):
            signed_atomic_shell.beta_weight(True)

    def test_partial_fraction_and_zero_atomic_total(self) -> None:
        self.assertTrue(signed_atomic_shell.partial_fraction_check())
        total = (Fraction(0), Fraction(0))
        for atom in signed_atomic_shell.atomic_coefficients():
            total = signed_atomic_shell.qadd(total, atom)
        self.assertEqual(total, (Fraction(0), Fraction(0)))

    def test_extra_notch_typing_and_scope(self) -> None:
        result = signed_atomic_shell.run()
        reduction = result["exact_mellin_reduction"]
        self.assertEqual(
            reduction["exact_operator_relations"],
            "K_740=V*K_explicit; K_extra=Q*K_740=Q*V*K_explicit",
        )
        self.assertIn("s^2*(s-1/2)", reduction["L102740_outer_multiplier"])
        self.assertIn("s*(s-1/2)", reduction["L102740_derivative_outer_multiplier"])
        self.assertIn("4*q(s)", reduction["explicit_piecewise_derivative_multiplier"])
        self.assertEqual(reduction["stable_filter_V"], "(5*D+3/2)/4")
        self.assertEqual(reduction["dyadic_shift_convention"], "S_2 f(X)=f(X/2)")
        self.assertEqual(
            reduction["D_mellin_convention"],
            "Mellin(D f)(s)=s*Mellin(f)(s)",
        )
        self.assertIn("three distinct", reduction["parent_adapter_status"])
        self.assertIn("three-way", result["conclusion"]["parent_blocker"])
        self.assertIn("does_not_rule_out", result["conclusion"])
        self.assertIn(
            "refutes", result["conclusion"]["later_complete_source_disposition"]
        )
        self.assertIn(
            "native-kernel fence",
            result["conclusion"]["later_complete_source_disposition"],
        )

    def test_scale_gap_and_caps(self) -> None:
        ledger = signed_atomic_shell.scale_ledger()
        self.assertEqual(ledger["signed_negative_atomic_mass"], 1)
        self.assertEqual(ledger["free_diagonal"], -2)
        self.assertEqual(ledger["negative_mass_to_diagonal_gap"], 3)
        result = signed_atomic_shell.run()
        ledger_y = result["asymptotic_ledger_in_Y"]
        self.assertEqual(ledger_y["signed_negative_atomic_mass"], "1/10")
        self.assertEqual(ledger_y["free_diagonal"], "-1/5")
        self.assertEqual(ledger_y["negative_mass_to_diagonal_gap"], "3/10")
        fixture = result["scale_fixture"]
        self.assertEqual(fixture["negative_atom_ratios"], [2, 8])
        self.assertTrue(fixture["negative_atoms_lie_below_horizon"])
        self.assertTrue(
            fixture["distinct_dyadic_layers_are_disjoint_by_2_adic_valuation"]
        )
        caps = result["resource_caps"]
        self.assertEqual(caps["prime_intervals_enumerated"], 0)
        self.assertEqual(caps["source_atoms_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
