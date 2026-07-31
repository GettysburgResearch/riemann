import copy, importlib.util, json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('v',ROOT/'verify.py')
v=importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)
BASE=json.loads((ROOT/'certificates/synthetic.json').read_text())

class TerminalVisibleTests(unittest.TestCase):
    def test_good(self):
        out=v.verify(copy.deepcopy(BASE))
        self.assertEqual(out['visible_margin'],{'numerator':7,'denominator':16})

    def test_bad_schema(self):
        x=copy.deepcopy(BASE); x['schema']='bad'
        self.assertRaises(v.CertificateError,v.verify,x)

    def test_boolean_rejected(self):
        x=copy.deepcopy(BASE); x['metric'][0][0]['numerator']=True
        self.assertRaises(v.CertificateError,v.verify,x)

    def test_cancellation_mutation(self):
        x=copy.deepcopy(BASE); x['raw_terminal'][0][0]['numerator']+=1
        self.assertRaises(v.CertificateError,v.verify,x)

    def test_theta_too_small(self):
        x=copy.deepcopy(BASE); x['theta']={'numerator':2,'denominator':1}
        self.assertRaises(v.CertificateError,v.verify,x)

    def test_visible_zero_touch(self):
        x=copy.deepcopy(BASE); x['sigma_squared']={'numerator':41,'denominator':16}
        self.assertRaises(v.CertificateError,v.verify,x)

    def test_nonpositive_metric(self):
        x=copy.deepcopy(BASE); x['metric'][1][1]={'numerator':0,'denominator':1}
        self.assertRaises(v.CertificateError,v.verify,x)

    def test_negative_loss(self):
        x=copy.deepcopy(BASE); x['assembly_radius']={'numerator':-1,'denominator':1}
        self.assertRaises(v.CertificateError,v.verify,x)

if __name__=='__main__': unittest.main()
