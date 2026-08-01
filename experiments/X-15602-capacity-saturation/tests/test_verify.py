from __future__ import annotations

import copy
import importlib.util
import json
import sys
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
spec=importlib.util.spec_from_file_location("x15602_verify",ROOT/"verify.py")
module=importlib.util.module_from_spec(spec)
assert spec and spec.loader
sys.modules[spec.name]=module
spec.loader.exec_module(module)


class CapacitySaturationTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/"certificates"/"synthetic-saturation.json").read_text())

    def test_synthetic_certificate(self):
        result=module.verify(copy.deepcopy(self.data))
        self.assertEqual(result["capacity"],2)
        self.assertEqual(result["saturated_count_below_gamma"],2)
        self.assertEqual(result["certified_floor"],{"numerator":-3,"denominator":4996})

    def test_complement_floor_is_load_bearing(self):
        data=copy.deepcopy(self.data)
        data["full_operator"][2][2]={"numerator":1,"denominator":4}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_trial_packet_must_lie_below_t(self):
        data=copy.deepcopy(self.data)
        data["full_operator"][0][0]={"numerator":1,"denominator":2}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_optimistic_inverse_ritz_q_rejected(self):
        data=copy.deepcopy(self.data)
        data["q_upper"]={"numerator":-4,"denominator":1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_q_must_be_negative(self):
        data=copy.deepcopy(self.data)
        data["q_upper"]={"numerator":1,"denominator":1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_t_must_be_below_gamma(self):
        data=copy.deepcopy(self.data)
        data["t"]={"numerator":3,"denominator":4}
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_rank_deficient_packet_rejected(self):
        data=copy.deepcopy(self.data)
        data["trial_basis"][1]=copy.deepcopy(data["trial_basis"][0])
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_boolean_capacity_rejected(self):
        data=copy.deepcopy(self.data)
        data["expected_capacity"]=True
        with self.assertRaises(module.CertificateError):
            module.verify(data)

    def test_claimed_floor_cannot_be_optimistic(self):
        data=copy.deepcopy(self.data)
        data["claimed_floor"]={"numerator":0,"denominator":1}
        with self.assertRaises(module.CertificateError):
            module.verify(data)


if __name__=="__main__":
    unittest.main()
