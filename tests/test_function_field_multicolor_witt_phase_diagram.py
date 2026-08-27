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
    / "function_field_multicolor_witt_phase_diagram.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("multicolor_witt", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load multicolor Witt producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class FunctionFieldMulticolorWittPhaseDiagramTest(unittest.TestCase):
    def test_frozen_sources(self) -> None:
        subject.check_source_blobs()

    def test_content_counts_sum_to_lyndon_counts(self) -> None:
        for colors in (2, 3, 4):
            for total in range(1, 7):
                self.assertEqual(
                    sum(
                        subject.content_necklace_multiplicity(content)
                        for content in subject.compositions(total, colors)
                    ),
                    subject.lyndon_count(colors, total),
                )

    def test_binary_specialization(self) -> None:
        self.assertEqual(subject.content_necklace_multiplicity((1, 1)), 1)
        self.assertEqual(subject.content_necklace_multiplicity((2, 0)), 0)
        self.assertEqual(subject.lyndon_count(2, 6), 9)

    def test_ternary_content_rows(self) -> None:
        self.assertEqual(subject.lyndon_count(3, 1), 3)
        self.assertEqual(subject.lyndon_count(3, 2), 3)
        self.assertEqual(subject.content_necklace_multiplicity((1, 1, 0)), 1)
        self.assertEqual(subject.content_necklace_multiplicity((1, 1, 1)), 2)

    def test_direct_and_witt_products_agree(self) -> None:
        for colors, q, maximum_degree in subject.CONTROL_ROWS:
            self.assertEqual(
                subject.direct_product(colors, q, maximum_degree),
                subject.witt_product(colors, q, maximum_degree),
            )

    def test_color_square_phase_transition_controls(self) -> None:
        binary = subject.control_panel(2, 5, 5)
        ternary = subject.control_panel(3, 11, 4)
        boundary = subject.control_panel(3, 9, 4)
        self.assertTrue(binary["critical_decay_regime"])
        self.assertTrue(ternary["critical_decay_regime"])
        self.assertFalse(boundary["critical_decay_regime"])

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
            fixture["proof_ledger"]["critical_decay_for_q_greater_than_color_square"],
            "PROVED",
        )
        self.assertEqual(
            fixture["proof_ledger"]["critical_decay_at_or_below_color_square"],
            "NOT CLAIMED",
        )
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_guards(self) -> None:
        with self.assertRaises(ValueError):
            subject.validate_color_count(1)
        with self.assertRaises(ValueError):
            subject.compositions(-1, 2)
        with self.assertRaises(ValueError):
            subject.content_necklace_multiplicity((0, 0))
        with self.assertRaises(ValueError):
            subject.irreducible_count(2.5, 1)
        with self.assertRaises(ValueError):
            subject.irreducible_count(5, True)
        with self.assertRaises(ValueError):
            subject.multiply_truncated({}, {}, -1)
        with self.assertRaises(ValueError):
            subject.direct_product(2, 5, -1)
        with self.assertRaises(ValueError):
            subject.witt_product(2, 5, -1)


if __name__ == "__main__":
    unittest.main()
