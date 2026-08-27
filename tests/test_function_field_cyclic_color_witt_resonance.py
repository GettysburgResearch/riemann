from __future__ import annotations

import importlib.util
import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "function_field_cyclic_color_witt_resonance.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("cyclic_color_witt", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load cyclic-color Witt producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldCyclicColorWittResonanceTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_root_of_unity_power_sum(self) -> None:
        for colors in range(2, 7):
            for exponent in range(1, 2 * colors + 1):
                self.assertEqual(
                    subject.cyclic_power_sum(colors, exponent),
                    colors if exponent % colors == 0 else 0,
                )

    def test_cyclic_necklace_values_match_content_sum(self) -> None:
        for colors in (2, 3, 4):
            for total in range(1, 7):
                content_coefficients: dict[int, int] = {}
                for content in subject.source.compositions(total, colors):
                    multiplicity = subject.source.content_necklace_multiplicity(content)
                    exponent = sum(index * value for index, value in enumerate(content))
                    content_coefficients[exponent] = (
                        content_coefficients.get(exponent, 0) + multiplicity
                    )
                remainder = subject.cyclotomic_remainder(colors, content_coefficients)
                self.assertEqual(
                    remainder,
                    (subject.cyclic_necklace_value(colors, total),)
                    + (0,) * (subject.sp.totient(colors) - 1),
                )

    def test_direct_and_witt_cyclic_collapses(self) -> None:
        for colors, q, maximum_degree in subject.CONTROL_ROWS:
            panel = subject.control_panel(colors, q, maximum_degree)
            self.assertTrue(panel["exact_direct_and_witt_collapse"])

    def test_exact_critical_threshold(self) -> None:
        self.assertTrue(3**2 > 2**2)
        self.assertTrue(3**3 > 3**2)
        self.assertFalse(2**3 > 3**2)
        self.assertTrue(2**5 > 5**2)

    def test_binary_collapse_has_only_even_prime_degrees(self) -> None:
        coefficients = subject.cyclic_direct_coefficients(2, 3, 7)
        self.assertEqual(coefficients[:4], (1, 0, -6, 0))
        self.assertNotEqual(coefficients[4], 0)

    def test_fixture_and_scope(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=20,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"][
                "critical_decay_for_q_power_c_greater_than_c_square"
            ],
            "PROVED",
        )
        self.assertEqual(
            fixture["proof_ledger"]["optimality_or_natural_boundary"],
            "NOT CLAIMED",
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.cyclic_power_sum(1, 2)
        with self.assertRaises(ValueError):
            subject.cyclic_power_sum(3, -1)
        with self.assertRaises(ValueError):
            subject.cyclic_necklace_value(3, 0)
        with self.assertRaises(ValueError):
            subject.cyclic_direct_coefficients(3, 3, -1)


if __name__ == "__main__":
    unittest.main()
