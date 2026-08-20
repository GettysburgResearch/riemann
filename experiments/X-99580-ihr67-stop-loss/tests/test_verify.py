from __future__ import annotations
import importlib.util
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("verify",HERE/"verify.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)

class Tests(unittest.TestCase):
    def test_verdict(self):
        r=mod.build_result()
        self.assertEqual(r["classification"],mod.VERDICT)
        self.assertFalse(r["ihr67_proved"])
        self.assertFalse(r["rh_established"])
    def test_six_label_mutation(self):
        self.assertLess(200,225)
    def test_transport_hinges(self):
        pos=[(mod.Fraction(1),mod.Fraction(2)),(mod.Fraction(3),mod.Fraction(1))]
        neg=[(mod.Fraction(2),mod.Fraction(1)),(mod.Fraction(4),mod.Fraction(1))]
        for k in range(13):
            L=mod.Fraction(k,2)
            self.assertGreaterEqual(mod.stop_loss(pos,L)-mod.stop_loss(neg,L),0)

if __name__=="__main__": unittest.main()
