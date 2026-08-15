from __future__ import annotations

import importlib.util
import json
import unittest
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE.parent / "verify.py"
SPEC = importlib.util.spec_from_file_location("x92930_verify", MODULE_PATH)
assert SPEC and SPEC.loader
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)


class T92930Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.control = json.loads(
            (HERE.parent / "certificates/control.json").read_text(encoding="utf-8")
        )

    def test_exact_q2_bounds(self) -> None:
        evidence = MOD.validate(self.control)
        q2 = evidence["q2"]
        self.assertEqual(Fraction(q2["conditional_final_lower"]), Fraction(343, 3600))
        self.assertGreater(
            Fraction(q2["conditional_final_lower"]),
            Fraction(q2["historical_threshold"]),
        )
        self.assertEqual(q2["unqualified_pr_application"], "WITHDRAWN")

    def test_native_is_not_rough_lift(self) -> None:
        evidence = MOD.validate(self.control)["native_source_tree"]
        native = tuple(Fraction(x) for x in evidence["native"])
        rough = tuple(Fraction(x) for x in evidence["rough_lift"])
        self.assertNotEqual(native, rough)

    def test_total_bound(self) -> None:
        cost = MOD.validate(self.control)["native_cost"]
        self.assertEqual(Fraction(cost["total"]), Fraction(493951, 8))
        self.assertLess(Fraction(cost["total"]), cost["strict_integer_bound"])

    def test_mutations_fail_closed(self) -> None:
        self.assertTrue(all(MOD.mutation_suite(self.control).values()))


if __name__ == "__main__":
    unittest.main()
