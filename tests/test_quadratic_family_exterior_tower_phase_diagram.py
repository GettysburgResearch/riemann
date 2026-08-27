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
    / "quadratic_family_exterior_tower_phase_diagram.py"
)
FIXTURE = SCRIPT.with_suffix(".json")
SPEC = importlib.util.spec_from_file_location("exterior_tower_phase_diagram", SCRIPT)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load exterior-tower producer")
subject = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject)


class QuadraticFamilyExteriorTowerPhaseDiagramTest(unittest.TestCase):
    def test_frozen_source_contract(self) -> None:
        subject.check_source_contract()

    def test_all_ten_low_rows(self) -> None:
        for mark_count in range(1, 11):
            self.assertEqual(
                subject.raw_exterior_expression(mark_count),
                subject.expected_low_expression(mark_count),
            )

    def test_stable_collapse_through_twenty_four_marks(self) -> None:
        for mark_count in range(9, subject.MAX_MARK_COUNT + 1):
            self.assertEqual(
                subject.raw_exterior_expression(mark_count),
                subject.stable_expression(mark_count),
            )
            self.assertEqual(
                subject.recurrence_order_bound(mark_count),
                subject.choose(mark_count - 1, 5),
            )

    def test_unique_weight_five_mark_notch(self) -> None:
        weights = {
            mark_count: subject.weil_weights(
                subject.raw_exterior_expression(mark_count)
            )
            for mark_count in range(1, 15)
        }
        self.assertIn(5, weights[8])
        self.assertNotIn(5, weights[9])
        self.assertNotIn(5, weights[10])
        self.assertIn(5, weights[11])
        self.assertIn(5, weights[12])
        self.assertEqual(subject.stable_expression(11)[(0, 5)], -1)
        self.assertEqual(subject.stable_expression(12)[(0, 5)], -1)

    def test_exact_rank_formulas_and_bounds(self) -> None:
        expected_generic = {
            2: 2,
            3: 4,
            4: 6,
            5: 8,
            6: 19,
            7: 34,
            8: 48,
            9: 48,
            10: 115,
            11: 222,
            12: 385,
        }
        for mark_count, rank in expected_generic.items():
            self.assertEqual(subject.generic_minimal_rank(mark_count), rank)
            self.assertLessEqual(rank, subject.recurrence_order_bound(mark_count))
        self.assertEqual(subject.memberwise_rank_formula(11), "r1+r3+r5")
        self.assertEqual(subject.memberwise_rank_formula(12), "1+r1+r2+r3+r4+r5")

    def test_generic_weight_count_is_not_dimension(self) -> None:
        self.assertEqual(subject.primitive_dimension(4, 3), 48)
        self.assertEqual(subject.primitive_generic_distinct_roots(4, 3), 40)
        self.assertEqual(subject.primitive_dimension(4, 4), 42)
        self.assertEqual(subject.primitive_generic_distinct_roots(4, 4), 41)

    def test_even_pure_tate_baselines(self) -> None:
        self.assertEqual(subject.pure_tate_baseline(2), {0: -3, 1: 2})
        self.assertEqual(subject.pure_tate_baseline(4), {0: -10, 2: 1})
        self.assertEqual(subject.pure_tate_baseline(6), {0: -21, 1: -6, 2: 1})
        self.assertEqual(subject.pure_tate_baseline(8), {0: -36, 1: -16})
        self.assertEqual(subject.pure_tate_baseline(10), {0: -55, 1: -30, 2: -2})
        self.assertEqual(subject.pure_tate_baseline(11), {})

    def test_zero_weight_multiplicities(self) -> None:
        for g in range(4, 9):
            self.assertEqual(subject.primitive_zero_weight_multiplicity(g, 2), g - 1)
            self.assertEqual(
                subject.primitive_zero_weight_multiplicity(g, 4),
                subject.choose(g, 2) - g,
            )

    def test_fixture_and_scope_ledger(self) -> None:
        completed = subprocess.run(
            ["python", "-B", str(SCRIPT), "--check"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        )
        self.assertEqual(completed.stdout, "")
        fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(
            fixture["proof_ledger"]["all_m_exterior_formula"],
            "PROVED EXACT FROM LOCKED SOURCE",
        )
        self.assertIn("FORMAL GENERIC", fixture["proof_ledger"]["generic_torus_ranks"])
        self.assertEqual(fixture["proof_ledger"]["rh_or_grh"], "NOT PROVED")

    def test_validation_and_resource_caps(self) -> None:
        with self.assertRaises(ValueError):
            subject.genus(0)
        with self.assertRaises(TypeError):
            subject.genus(True)
        with self.assertRaises(ValueError):
            subject.h_exterior_in_primitives(-1, 2)
        with self.assertRaises(ValueError):
            subject.stable_expression(8)
        result = subject.run(check_sources=False)
        caps = result["resource_caps"]
        self.assertEqual(caps["finite_field_elements"], 0)
        self.assertEqual(caps["matrices_constructed"], 0)
        self.assertEqual(caps["largest_exterior_index"], 5)


if __name__ == "__main__":
    unittest.main()
