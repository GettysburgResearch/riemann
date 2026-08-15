from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("x91860_verify", VERIFY)
assert SPEC and SPEC.loader
M = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = M
SPEC.loader.exec_module(M)


class TestTwoSortedHallRow(unittest.TestCase):
    def test_exact_x2_obstruction(self) -> None:
        r = M.exact_x2_obstruction()
        self.assertFalse(r["complete_target_null_bonus_packet"])

    def test_baseline(self) -> None:
        r = M.validate_certificate(M.base_certificate())
        self.assertIsNone(r["bonus_target"])
        self.assertIsNone(r["bonus_declared_score"])
        self.assertTrue(r["many_to_one_first_owner_accepted"])
        self.assertTrue(r["one_block_realization"])
        self.assertEqual(r["terminal_margin"], 581)
        self.assertEqual(r["native_total"], 60989)

    def test_all_mutations_fail_closed(self) -> None:
        for name in M.MUTATIONS:
            with self.subTest(name=name):
                with self.assertRaises((AssertionError, ValueError)):
                    M.validate_certificate(M.mutated(name))

    def test_mutation_count(self) -> None:
        self.assertEqual(len(M.run_mutations()), 20)


if __name__ == "__main__":
    unittest.main()
