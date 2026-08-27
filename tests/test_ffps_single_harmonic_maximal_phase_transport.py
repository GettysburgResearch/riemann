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
    / "ffps_single_harmonic_maximal_phase_transport.py"
)
SPEC = importlib.util.spec_from_file_location(
    "single_harmonic_maximal_phase_transport", MODULE_PATH
)
assert SPEC and SPEC.loader
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class SingleHarmonicMaximalPhaseTransportTest(unittest.TestCase):
    def test_source_contract(self) -> None:
        subject.check_source_contract()

    def test_rational_gaussian_unit_powers(self) -> None:
        unit = (Fraction(3, 5), Fraction(4, 5))
        for exponent in range(subject.TOY_PREFIX_CAP + 1):
            power = subject.gpower(unit, exponent)
            norm_square = subject.gmul(power, subject.gconjugate(power))
            self.assertEqual(norm_square, (Fraction(1), Fraction(0)))

    def test_forward_and_reverse_abel_phase_identities(self) -> None:
        panel = subject.phase_transport_panel()
        self.assertEqual(len(panel["rows"]), subject.TOY_PREFIX_CAP)
        for row in panel["rows"]:
            self.assertTrue(row["forward_identity"])
            self.assertTrue(row["reverse_identity"])
        self.assertEqual(panel["fixed_harmonic_cost"], "1+2*pi*|h|")

    def test_direct_abel_identity_on_explicit_prefix(self) -> None:
        coefficients = (
            (Fraction(1), Fraction(2)),
            (Fraction(-3), Fraction(1)),
            (Fraction(4), Fraction(-2)),
            (Fraction(2), Fraction(5)),
        )
        unit = (Fraction(3, 5), Fraction(4, 5))
        multipliers = tuple(
            subject.gpower(unit, index + 1) for index in range(len(coefficients))
        )
        for height in range(1, len(coefficients) + 1):
            self.assertEqual(
                subject.direct_twisted_sum(coefficients, multipliers, height),
                subject.abel_twisted_sum(coefficients, multipliers, height),
            )

    def test_duplicate_scale_inverse(self) -> None:
        panel = subject.beta_zero_scale_panel()
        self.assertTrue(panel["reconstruction"])
        self.assertIn("1-67^(-1/2)", panel["theorem_bounds"])

    def test_canonical_json_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(
            MODULE_PATH.with_suffix(".json").read_text(encoding="utf-8")
        )
        self.assertEqual(result, fixture)
        theorem = result["single_harmonic_equivalence"]["theorem"]
        self.assertIn("RH iff", theorem)
        self.assertIn(
            "one nonzero guarded lattice harmonic",
            result["single_harmonic_equivalence"]["minimal_window"],
        )
        scope = result["load_bearing_scope"]
        self.assertTrue(scope["one_common_period_before_prefix_supremum"])
        self.assertTrue(scope["maximal_prefix_assembly"])
        self.assertTrue(scope["actual_signed_beta_source"])
        self.assertFalse(scope["endpoint_only_first_harmonic_equivalence"])
        self.assertFalse(scope["dyadic_endpoint_replacement_proved"])
        self.assertFalse(scope["moving_kernel_order"])
        self.assertFalse(scope["rh_proved"])

    def test_classical_input_and_weight_fences(self) -> None:
        result = subject.run(check_sources=False)
        self.assertEqual(
            result["classical_input"]["status"],
            "IMPORTED CLASSICAL MERTENS CRITERION",
        )
        self.assertIn(
            "L_X^(-(2r+1))",
            result["single_harmonic_equivalence"]["weight_asymptotic"],
        )
        self.assertEqual(result["resource_caps"]["floating_point_operations"], 0)
        self.assertEqual(result["resource_caps"]["zeta_zeros"], 0)

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.gpower((Fraction(1), Fraction(0)), -1)
        with self.assertRaises(ValueError):
            subject.direct_twisted_sum(
                ((Fraction(1), Fraction(0)),),
                ((Fraction(1), Fraction(0)),),
                0,
            )
        with self.assertRaises(ValueError):
            subject.abel_twisted_sum(
                ((Fraction(1), Fraction(0)),),
                (),
                1,
            )
        with self.assertRaises(ValueError):
            subject.scale_filter((), (Fraction(1, 5), Fraction(0)))


if __name__ == "__main__":
    unittest.main()
