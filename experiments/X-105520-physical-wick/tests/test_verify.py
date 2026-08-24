import importlib.util
import unittest
from pathlib import Path

P=Path(__file__).resolve().parents[1]/"verify.py"
S=importlib.util.spec_from_file_location("verify105520",P)
M=importlib.util.module_from_spec(S); S.loader.exec_module(M)

class TestT105520(unittest.TestCase):
    def test_algebra(self):
        x=M.algebra_checks()
        self.assertEqual(x["target"],"1/7000")
    def test_operator(self):
        self.assertEqual(M.operator_checks()["exact_nilpotent_resolvent_fixtures"],18)
    def test_threshold(self):
        self.assertEqual(M.threshold_checks()["negative_trace_cut"],"1/20")
    def test_fail_closed(self):
        x=M.payload()
        self.assertFalse(x["stripneg105520_proved"])
        self.assertFalse(x["ninety_percent_established"])
        self.assertFalse(x["rh_established"])

if __name__=="__main__":
    unittest.main()
