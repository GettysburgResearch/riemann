from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
spec=importlib.util.spec_from_file_location("x15603_verify",ROOT/"verify.py")
module=importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name]=module
spec.loader.exec_module(module)


class WeightedIndexDimensionGapTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/"certificates"/"synthetic.json").read_text())

    def test_synthetic_refutation(self):
        result=module.verify(copy.deepcopy(self.data))
        self.assertEqual(result["threshold_index"],1)
        self.assertEqual(result["source_dimension"],1)
        self.assertTrue(result["dimension_comparison_holds"])
        self.assertTrue(result["trace_saturation_fails"])

    def test_aligned_source_does_not_refute(self):
        data=copy.deepcopy(self.data)
        data["source_basis"]=[[{"numerator":1,"denominator":1}],
                              [{"numerator":0,"denominator":1}]]
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_dimension_comparison_must_hold(self):
        data=copy.deepcopy(self.data)
        data["weighted_deficit"][1][1]={"numerator":1,"denominator":1}
        data["deficit_eigenvalues"][1]={"numerator":1,"denominator":1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_nondiagonal_regression_rejected(self):
        data=copy.deepcopy(self.data)
        data["weighted_deficit"][0][1]={"numerator":1,"denominator":10}
        data["weighted_deficit"][1][0]={"numerator":1,"denominator":10}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_boolean_rational_rejected(self):
        data=copy.deepcopy(self.data)
        data["kappa"]["numerator"]=True
        with self.assertRaises(module.CertificateError):
            module.verify(data)


if __name__=="__main__":
    unittest.main()
