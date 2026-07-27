from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "certified_scan", ROOT / "certified_scan.py"
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class TerminalCoverageTests(unittest.TestCase):
    def test_non_prime_power_cutoff_needs_terminal_cell(self):
        self.assertTrue(module.terminal_cell_needed(9_999_991, 10_000_000))

    def test_prime_power_cutoff_has_no_terminal_cell(self):
        self.assertFalse(module.terminal_cell_needed(8, 8))

    def test_empty_manifest_still_needs_whole_interval(self):
        self.assertTrue(module.terminal_cell_needed(None, 10))

    def test_manifest_above_cutoff_is_not_a_valid_no_cell_case(self):
        # The production loop separately rejects such a manifest. The pure
        # planner must not silently call it complete.
        self.assertFalse(module.terminal_cell_needed(11, 10))


if __name__ == "__main__":
    unittest.main()
