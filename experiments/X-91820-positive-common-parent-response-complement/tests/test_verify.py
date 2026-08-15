from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

HERE = Path(__file__).resolve()
VERIFY = HERE.parents[1] / "verify.py"
SPEC = importlib.util.spec_from_file_location("x91820_verify", VERIFY)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class TestPositiveCommonParentPacket(unittest.TestCase):
    def test_baseline(self) -> None:
        result = MODULE.check_packet()
        self.assertEqual(result["quantizers"], 1)
        self.assertEqual(result["all_column"]["terminal_margin"], 581)
        self.assertEqual(result["endpoint_orientation"], "F_Lambda<=native_deficit")

    def test_all_hostile_mutations_fail_closed(self) -> None:
        for mutation in MODULE.MUTATIONS:
            with self.subTest(mutation=mutation):
                with self.assertRaises(AssertionError):
                    MODULE.check_packet(mutation)

    def test_mutation_count(self) -> None:
        self.assertEqual(MODULE.run_mutations(), 10)


if __name__ == "__main__":
    unittest.main()
