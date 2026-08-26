"""Tests for the guarded chi_(0,4) primary-source reconciliation."""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PRODUCER_PATH = (
    ROOT
    / "research"
    / "l-families"
    / "atlas"
    / "function_field"
    / "genus2_chi04_stack_trace_reconciliation.py"
)
FIXTURE_PATH = PRODUCER_PATH.with_suffix(".json")

SPEC = importlib.util.spec_from_file_location("chi04_reconciliation", PRODUCER_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load chi04 reconciliation producer")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Chi04StackTraceReconciliationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_fixture_replays_exactly(self) -> None:
        self.assertEqual(MODULE.build_fixture(), self.fixture)

    def test_payload_hash_is_canonical(self) -> None:
        payload = dict(self.fixture)
        claimed = payload.pop("payload_sha256")
        self.assertEqual(MODULE._canonical_sha256(payload), claimed)

    def test_project_theorem_is_source_locked(self) -> None:
        theorem = self.fixture["project_theorem"]
        self.assertEqual(theorem["mean"], "<chi_(0,4)>=-(2*q^2+1)/q^7")
        self.assertEqual(theorem["marked_stack_trace"], "T_(0,4)(q)=-(2*q^2+1)")

    def test_no_printed_all_q_target_formula_was_found(self) -> None:
        verdict = self.fixture["primary_source_verdict"]
        self.assertFalse(verdict["printed_all_q_M_2(w^1)_V_(4,4)_formula_found"])

    def test_moduli_problems_remain_distinct(self) -> None:
        firewall = self.fixture["moduli_firewall"]
        self.assertEqual(
            set(firewall),
            {"M_2(w^1)", "M_(2,1)", "M_2", "A_2(w^1)", "A_2[2]"},
        )

    def test_s5_projection(self) -> None:
        reconciliation = self.fixture["BFG_conjectural_reconciliation"]
        self.assertEqual(
            reconciliation["S5_invariant_multiplicities"],
            {
                "A": 0,
                "B": 0,
                "C": 2,
                "A_prime": 0,
                "B_prime": 1,
                "C_prime": 1,
            },
        )
        self.assertEqual(
            reconciliation["representation_dimensions"],
            {
                "A": 15,
                "B": 30,
                "C": 15,
                "A_prime": 15,
                "B_prime": 30,
                "C_prime": 15,
            },
        )
        self.assertEqual(
            reconciliation["dimension_forgetting_modular_coefficients"],
            {"Phi_(4,6)": 15, "Phi_(4,12)": -5},
        )

    def test_ambient_boundary_difference(self) -> None:
        reconciliation = self.fixture["BFG_conjectural_reconciliation"]
        ambient = reconciliation["A_2(w^1)_components_low_to_high"]["expected_total"]
        boundary = self.fixture["exact_decomposable_boundary"]["class_low_to_high"]
        marked = self.fixture["reconciled_difference"][
            "M_2(w^1)_predicted_class_low_to_high"
        ]
        self.assertEqual(
            ambient, [[1, 1], [0, 1], [0, 1], [0, 1], [0, 1], [-1, 1], [1, 1]]
        )
        self.assertEqual(
            boundary, [[2, 1], [0, 1], [2, 1], [0, 1], [0, 1], [-1, 1], [1, 1]]
        )
        self.assertEqual(marked, [[-1, 1], [0, 1], [-2, 1]])
        self.assertIn(
            "does not itself prove equality of motivic Grothendieck classes",
            self.fixture["reconciled_difference"]["interpretation"],
        )

    def test_branching_is_exact_and_dimension_55(self) -> None:
        branching = self.fixture["exact_decomposable_boundary"]["branching"]
        self.assertEqual(branching["summand_degrees"], [0, 1, 2, 3, 4])
        self.assertEqual(branching["summand_dimensions"], [1, 4, 9, 16, 25])
        self.assertEqual(branching["total_dimension"], 55)

    def test_resource_guard(self) -> None:
        audit = self.fixture["resource_audit"]
        self.assertLessEqual(audit["exact_operations"], audit["operation_cap"])
        self.assertEqual(audit["finite_fields_enumerated"], 0)
        self.assertEqual(audit["curves_enumerated"], 0)


if __name__ == "__main__":
    unittest.main()
