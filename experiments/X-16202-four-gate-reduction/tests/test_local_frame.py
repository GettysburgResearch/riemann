from __future__ import annotations

import importlib.util
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "local_frame_verify", ROOT / "verify_local_frame.py"
)
assert SPEC is not None and SPEC.loader is not None
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class LocalTripleFrameTests(unittest.TestCase):
    def test_complete_control(self):
        result = module.verify()
        self.assertEqual(result["maximum_ratio"], "1/101")
        self.assertEqual(result["certified_frame_lower_bound"], "1/100")

    def test_constraints(self):
        defects = [F(1), F(10), F(1000), F(100000), F(10000000)]
        q = [F(1), F(2), F(1), F(2), F(1)]
        frame, _ = module.build_frame(defects, q)
        for column in module.transpose(frame):
            x = [q[i] * column[i] for i in range(len(q))]
            self.assertEqual(sum(x), 0)
            self.assertEqual(sum(defects[i] * x[i] for i in range(len(q))), 0)

    def test_unsorted_defects_rejected(self):
        with self.assertRaises(module.CertificateError):
            module.build_frame([F(1), F(3), F(2)], [F(1), F(1), F(1)])

    def test_zero_point_value_rejected(self):
        with self.assertRaises(module.CertificateError):
            module.build_frame([F(1), F(2), F(3)], [F(1), F(0), F(1)])

    def test_singular_matrix_rejected(self):
        with self.assertRaises(module.CertificateError):
            module.require_pd([[F(1), F(1)], [F(1), F(1)]], "singular")

    def test_bad_dimension_rejected(self):
        with self.assertRaises(module.CertificateError):
            module.build_frame([F(1), F(2)], [F(1), F(1)])


if __name__ == "__main__":
    unittest.main()
