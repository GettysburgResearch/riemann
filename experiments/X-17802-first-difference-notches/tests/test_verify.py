import copy, importlib.util, json, sys, unittest
from pathlib import Path
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("x17802",HERE/"verify.py")
mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
BASE=json.loads((HERE/"certificates/synthetic.json").read_text())
class Tests(unittest.TestCase):
    def test_valid(self): self.assertTrue(mod.verify(copy.deepcopy(BASE))["gain_exceeds_10_pow_115"])
    def test_schema(self):
        d=copy.deepcopy(BASE);d["schema"]="bad"
        with self.assertRaises(ValueError):mod.verify(d)
    def test_boolean_height(self):
        d=copy.deepcopy(BASE);d["verified_height"]=True
        with self.assertRaises(ValueError):mod.verify(d)
    def test_short_ordinates(self):
        d=copy.deepcopy(BASE);d["ordinate_upper_integers"]=[15]
        with self.assertRaises(ValueError):mod.verify(d)
    def test_negative_shift(self):
        d=copy.deepcopy(BASE);d["synthetic_shifts"][0]={"numerator":-1,"denominator":3}
        with self.assertRaises(ValueError):mod.verify(d)
    def test_bad_phase_error(self):
        d=copy.deepcopy(BASE);d["phase_error_upper"]={"numerator":-1,"denominator":2}
        with self.assertRaises(ValueError):mod.verify(d)
    def test_displacement_outside(self):
        d=copy.deepcopy(BASE);d["normalized_displacement"]={"numerator":2,"denominator":1}
        with self.assertRaises(ValueError):mod.verify(d)
    def test_gain_mutation(self):
        d=copy.deepcopy(BASE);d["verified_height"]=1
        with self.assertRaises(ValueError):mod.verify(d)
if __name__=="__main__":unittest.main()
