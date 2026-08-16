from __future__ import annotations
import copy, importlib.util, json, sys, unittest
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('x20201_verify',HERE/'verify.py')
mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod)
BASE=json.loads((HERE/'certificates/synthetic.json').read_text())

class VerifyTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(mod.verify(copy.deepcopy(BASE))['verified'])
    def test_schema(self):
        d=copy.deepcopy(BASE); d['schema']='bad'
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_boolean_integer(self):
        d=copy.deepcopy(BASE); d['moment_model']['order']=True
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_cosine_outside(self):
        d=copy.deepcopy(BASE); d['cosine_samples'][0]['cosine']={'numerator':2,'denominator':1}
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_claimed_square_mutation(self):
        d=copy.deepcopy(BASE); d['cosine_samples'][2]['claimed_defect']={'numerator':1,'denominator':1}
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_negative_weight(self):
        d=copy.deepcopy(BASE); d['moment_model']['atoms'][0]['weight']={'numerator':-1,'denominator':1}
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_pole_zero(self):
        d=copy.deepcopy(BASE); d['pole_square']['a']={'numerator':0,'denominator':1}
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_cocycle_claim_mutation(self):
        d=copy.deepcopy(BASE); d['cocycle']['claimed_d4']={'numerator':0,'denominator':1}
        with self.assertRaises(mod.CertificateError): mod.verify(d)
    def test_insufficient_atoms(self):
        d=copy.deepcopy(BASE); d['moment_model']['atoms']=d['moment_model']['atoms'][:2]
        with self.assertRaises(mod.CertificateError): mod.verify(d)

if __name__=='__main__': unittest.main()
