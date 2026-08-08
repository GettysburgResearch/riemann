from __future__ import annotations

import importlib.util
import pathlib
import sys
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("fifth_shell_verify", ROOT / "verify.py")
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class FifthAlignedShellTest(unittest.TestCase):
    def test_retained_verdict(self) -> None:
        result = MODULE.run()
        self.assertEqual(
            result["classification"],
            "EXACT_FIFTH_ALIGNED_SHELL_ANNULUS_VERIFIED",
        )
        self.assertEqual(result["annulus"], [1, 100])
        self.assertEqual(result["minimum_endpoint_index"], 2)
        self.assertEqual(result["unresolved_cells"], 0)
        self.assertFalse(result["floating_point_used_in_verdict"])

    def test_cell_count(self) -> None:
        result = MODULE.run()
        self.assertEqual(sum(result["cell_classes"].values()), 99)


if __name__ == "__main__":
    unittest.main()
