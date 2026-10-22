#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("t105100_verify", ROOT / "verify.py")
assert SPEC and SPEC.loader
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)


class TestT105100(unittest.TestCase):
    def test_cubic_balance(self) -> None:
        coefficients = [F(1), F(-3), F(0), F(1)]
        rho, tau = V.residue_sums(coefficients, [F(-1), F(1)], [F(0)])
        self.assertEqual(rho, [F(-1, 2), F(-1, 6)])
        self.assertEqual(tau, [F(-1, 18)])
        self.assertEqual(
            sum((value**2 for value in rho), F(0)) + sum(tau, F(0)),
            V.root_moment_ledger(coefficients),
        )

    def test_asymmetric_quartic_balance(self) -> None:
        coefficients = [F(1), F(64), F(-32), F(-4, 3), F(1)]
        rho, tau = V.residue_sums(
            coefficients,
            [F(-4), F(1), F(4)],
            [F(-2), F(8, 3)],
        )
        self.assertEqual(
            sum((value**2 for value in rho), F(0)) + sum(tau, F(0)),
            F(5437, 3888),
        )
        self.assertEqual(V.root_moment_ledger(coefficients), F(5437, 3888))

    def test_factor_free_laurent_coefficient(self) -> None:
        fixtures = [
            [F(-2), F(3), F(1)],
            [F(1), F(-3), F(0), F(1)],
            [F(2), F(3), F(-1), F(5), F(-2), F(1)],
        ]
        for coefficients in fixtures:
            self.assertEqual(
                V.laurent_minus_one_coefficient(coefficients),
                V.root_moment_ledger(coefficients),
            )

    def test_translation_invariance(self) -> None:
        coefficients = [F(1), F(-3), F(0), F(1)]
        translated = V.translate_polynomial(coefficients, F(11))
        self.assertEqual(
            V.centered_root_moments(coefficients),
            V.centered_root_moments(translated),
        )
        self.assertEqual(
            V.root_moment_ledger(coefficients),
            V.root_moment_ledger(translated),
        )

    def test_quartic_firewall_requires_debt(self) -> None:
        firewall = V.quartic_firewall_exact()
        self.assertEqual(firewall["critical_square_sum"], "9/32")
        self.assertEqual(firewall["root_moment_ledger"], "37/432")
        self.assertEqual(firewall["second_level_debt"], "-169/864")
        self.assertTrue(firewall["root_ledger_is_not_an_upper_bound"])
        self.assertTrue(firewall["dropping_second_level_debt_fails"])

    def test_nonreal_critical_correction(self) -> None:
        fixture = V.nonreal_critical_correction_exact()
        self.assertEqual(fixture["real_critical_residue_m2"], "0")
        self.assertEqual(fixture["off_real_algebraic_square_sum"], "-23/162")
        self.assertEqual(fixture["off_real_absolute_square_sum"], "31/162")
        self.assertNotEqual(
            fixture["off_real_algebraic_square_sum"],
            fixture["off_real_absolute_square_sum"],
        )
        self.assertEqual(fixture["second_level_debt"], "1/6")
        self.assertEqual(fixture["root_moment_ledger"], "2/81")
        self.assertTrue(fixture["real_nonreal_decomposition_verified"])

    def test_incomplete_root_coverage_is_rejected(self) -> None:
        coefficients = [F(1), F(-3), F(0), F(1)]
        with self.assertRaises(ValueError):
            V.residue_sums(coefficients, [F(-1)], [F(0)])

    def test_second_critical_coverage_is_rejected(self) -> None:
        coefficients = [F(1), F(64), F(-32), F(-4, 3), F(1)]
        with self.assertRaises(ValueError):
            V.residue_sums(
                coefficients,
                [F(-4), F(1), F(4)],
                [F(-2)],
            )
        with self.assertRaises(ValueError):
            V.residue_sums(
                coefficients,
                [F(-4), F(1), F(4)],
                [F(-2), F(-2)],
            )

    def test_committed_artifact_matches_producer_and_content(self) -> None:
        artifact_path = ROOT / "results" / "verification.json"
        committed = json.loads(artifact_path.read_text(encoding="utf-8"))
        self.assertEqual(committed, V.build_payload())
        self.assertEqual(set(committed["content_sha256"]), set(V.CONTENT_FILES))

    def test_scope_remains_open(self) -> None:
        scope = V.build_payload()["scope"]
        self.assertFalse(scope["height_localization_proved"])
        self.assertFalse(scope["canonical_product_limit_proved"])
        self.assertFalse(scope["off_real_correction_controlled"])
        self.assertFalse(scope["second_level_debt_controlled"])
        self.assertFalse(scope["rcmv104530_proved"])
        self.assertFalse(scope["rh_established"])


if __name__ == "__main__":
    unittest.main()
