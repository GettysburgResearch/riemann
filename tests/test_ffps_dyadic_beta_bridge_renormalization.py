from __future__ import annotations

import importlib.util
import json
import subprocess
import unittest
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "ffps_dyadic_beta_bridge_renormalization.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("dyadic_beta_bridge", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load dyadic beta bridge producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class DyadicBetaBridgeRenormalizationTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_contracts()

    def test_factor_three_is_exact_and_sharp(self) -> None:
        panel = subject.sharp_ratio_panel()
        self.assertEqual(Fraction(panel["dyadic_bridge"]), 1)
        self.assertEqual(Fraction(panel["floor_ratio_bridge"]), 3)
        self.assertEqual(Fraction(panel["sharp_increment"]), 3)

    def test_terminating_scale_inverse(self) -> None:
        increments = tuple(Fraction(((-1) ** n) * (n + 1), n + 3) for n in range(1, 82))
        ordinary = subject.prefix_sums(increments)
        duplicate = subject.scale_filter(ordinary, 3, Fraction(-2, 5))
        self.assertEqual(
            subject.inverse_scale_filter(duplicate, 3, Fraction(-2, 5)),
            ordinary,
        )

    def test_scale_bridge_bounds(self) -> None:
        panel = subject.scale_panel()
        ordinary = Fraction(panel["ordinary_dyadic_bridge"])
        duplicate = Fraction(panel["duplicate_dyadic_bridge"])
        modulus = Fraction(2, 5)
        self.assertLessEqual(duplicate, (1 + 3 * modulus) * ordinary)
        self.assertLessEqual(
            ordinary,
            (1 + 2 * modulus) / (1 - modulus) * duplicate,
        )
        self.assertTrue(panel["inverse_exact"])

    def test_bridge_controls_the_complete_maximal_prefix(self) -> None:
        increments = tuple(Fraction((n % 5) - 2, n + 1) for n in range(1, 65))
        prefixes = subject.prefix_sums(increments)
        bridge = subject.dyadic_bridge(prefixes)
        maximal = subject.maximal_prefix(prefixes)
        self.assertLessEqual(bridge, 2 * maximal)
        self.assertLessEqual(maximal, 8 * bridge)

    def test_rough_hidden_excursion(self) -> None:
        panel = subject.rough_hidden_excursion()
        self.assertTrue(panel["all_queries_zero"])
        self.assertTrue(panel["all_dyadic_boundaries_zero"])
        self.assertEqual(Fraction(panel["hidden_bridge_height"]), Fraction(1, 2))
        self.assertEqual(
            panel["rough_support_size"],
            sum(
                1
                for value in range(1, subject.TOY_LIMIT + 1)
                if subject.math.gcd(value, subject.TOY_ROUGH_MODULUS) == 1
                and subject.is_squarefree(value)
            ),
        )

    def test_canonical_fixture_and_scope(self) -> None:
        result = subject.run(check_sources=False)
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(result, fixture)
        self.assertFalse(result["scope"]["dyadic_endpoint_gate_needed_separately"])
        self.assertFalse(result["scope"]["literal_beta_bridge_estimate_proved"])
        self.assertFalse(result["scope"]["duplicate_67_contraction"])
        self.assertFalse(result["scope"]["rh_or_grh_proved"])

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.dyadic_boundaries(1)
        with self.assertRaises(ValueError):
            subject.dyadic_bridge((Fraction(0), Fraction(1)))
        with self.assertRaises(ValueError):
            subject.scale_filter(
                (Fraction(0), Fraction(1), Fraction(2)), 1, Fraction(1, 2)
            )
        with self.assertRaises(ValueError):
            subject.is_squarefree(0)

    def test_producer_check(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=15,
        )
        self.assertEqual(completed.stdout, "")


if __name__ == "__main__":
    unittest.main()
