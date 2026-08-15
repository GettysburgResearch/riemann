from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE.parent / "verify.py"
spec = importlib.util.spec_from_file_location("t92920_verify", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


class NativeParityQ2Tests(unittest.TestCase):
    def test_q2_exact_separator(self):
        ctl = mod.json.loads((HERE.parent / "certificates/control.json").read_text())
        result = mod.q2_certificate(ctl)
        self.assertEqual(result["separator"], "109/1200")

    def test_oriented_pair_is_native(self):
        result = mod.parity_fixture()
        self.assertEqual(result["output"], result["native"])

    def test_dropped_orientation_is_not_native(self):
        good = mod.parity_fixture()
        bad = mod.parity_fixture(drop_orientation=True)
        self.assertNotEqual(bad["output"], good["native"])

    def test_full_capacity_promotion_is_not_native(self):
        good = mod.parity_fixture()
        bad = mod.parity_fixture(promote_full_capacity=True)
        self.assertNotEqual(bad["output"], good["native"])


if __name__ == "__main__":
    unittest.main()
