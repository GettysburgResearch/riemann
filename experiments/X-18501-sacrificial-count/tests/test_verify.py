import copy, importlib.util, json, sys, unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SPEC=importlib.util.spec_from_file_location("x18501",ROOT/"verify.py")
V=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=V; SPEC.loader.exec_module(V)
BASE=json.loads((ROOT/"certificates"/"synthetic.json").read_text())

class Tests(unittest.TestCase):
    def test_strict_control(self):
        out=V.verify(copy.deepcopy(BASE))
        self.assertEqual(out["count_upper"],2)
        self.assertEqual(out["count_lower"],2)
        self.assertEqual(out["angle_squared_upper"],{"numerator":3,"denominator":50})
    def test_boolean_rejected(self):
        d=copy.deepcopy(BASE); d["radical_rank"]=True
        with self.assertRaises(V.Reject): V.verify(d)
    def test_codimension_rejected(self):
        d=copy.deepcopy(BASE); d["radical_rank"]=1; d["radical_basis"]=[r[:1] for r in d["radical_basis"]]
        with self.assertRaises(V.Reject): V.verify(d)
    def test_witness_rank_rejected(self):
        d=copy.deepcopy(BASE); d["witness_basis"][3][1]={"numerator":0,"denominator":1}
        with self.assertRaises(V.Reject): V.verify(d)
    def test_false_witness_floor_rejected(self):
        d=copy.deepcopy(BASE); d["threshold"]={"numerator":5,"denominator":2}
        with self.assertRaises(V.Reject): V.verify(d)
    def test_radical_threshold_order_rejected(self):
        d=copy.deepcopy(BASE); d["radical_evaluation_upper"]={"numerator":1,"denominator":2}
        with self.assertRaises(V.Reject): V.verify(d)
    def test_false_radical_moat_rejected(self):
        d=copy.deepcopy(BASE); d["radical_evaluation_upper"]={"numerator":3,"denominator":200}
        with self.assertRaises(V.Reject): V.verify(d)
    def test_indefinite_metric_rejected(self):
        d=copy.deepcopy(BASE); d["metric"][3][3]={"numerator":-1,"denominator":1}
        with self.assertRaises(V.Reject): V.verify(d)
    def test_false_expected_rejected(self):
        d=copy.deepcopy(BASE); d["expected"]["count_upper"]=1
        with self.assertRaises(V.Reject): V.verify(d)

if __name__=="__main__": unittest.main()
