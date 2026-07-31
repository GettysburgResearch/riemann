import importlib.util,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SP=importlib.util.spec_from_file_location("x14309",ROOT/"verify.py")
V=importlib.util.module_from_spec(SP); sys.modules[SP.name]=V; SP.loader.exec_module(V)

def base():
    return {
      "schema":"riemann.x14309-symbol-bathtub-floor.v1",
      "classification":"SYNTHETIC_MODEL",
      "time_interval_length":{"numerator":2,"denominator":1},
      "pi_lower":{"numerator":333,"denominator":106},
      "tail_gate":{"status":"SYNTHETIC_SYMBOL_TAIL_FLOOR","sha256":"s"*64,
                   "symbol_lower_outside_cells":{"numerator":1,"denominator":1}},
      "cells":[{"id":"low-cell","left":{"numerator":-1,"denominator":4},
                "right":{"numerator":1,"denominator":4},
                "symbol_lower":{"numerator":-1,"denominator":1}}],
      "candidate_levels":[{"numerator":-1,"denominator":1},{"numerator":1,"denominator":1}],
      "expected":{"best_level":{"numerator":1,"denominator":1},
                  "best_floor":{"numerator":227,"denominator":333},
                  "status":"CERTIFIED_NONNEGATIVE_SYMBOL_COMPRESSION"}}

class Tests(unittest.TestCase):
    def test_strict_control(self):
        self.assertEqual(V.verify(base())["best_floor"],{"numerator":227,"denominator":333})
    def test_boolean_rejected(self):
        d=base(); d["time_interval_length"]["numerator"]=True
        with self.assertRaises(V.E): V.verify(d)
    def test_wrong_pi_rejected(self):
        d=base(); d["pi_lower"]={"numerator":3,"denominator":1}
        with self.assertRaises(V.E): V.verify(d)
    def test_wrong_gate_rejected(self):
        d=base(); d["tail_gate"]["status"]="EMPIRICAL"
        with self.assertRaises(V.E): V.verify(d)
    def test_overlap_rejected(self):
        d=base(); d["cells"].append({"id":"overlap","left":{"numerator":0,"denominator":1},
            "right":{"numerator":1,"denominator":2},"symbol_lower":{"numerator":0,"denominator":1}})
        d["candidate_levels"]=[{"numerator":-1,"denominator":1},{"numerator":0,"denominator":1},{"numerator":1,"denominator":1}]
        with self.assertRaises(V.E): V.verify(d)
    def test_incomplete_levels_rejected(self):
        d=base(); d["candidate_levels"]=[{"numerator":1,"denominator":1}]
        with self.assertRaises(V.E): V.verify(d)
    def test_false_floor_rejected(self):
        d=base(); d["expected"]["best_floor"]={"numerator":2,"denominator":3}
        with self.assertRaises(V.E): V.verify(d)
    def test_negative_floor_case(self):
        d=base(); d["cells"][0]["left"]={"numerator":-2,"denominator":1}; d["cells"][0]["right"]={"numerator":2,"denominator":1}
        d["expected"]={"best_level":{"numerator":-1,"denominator":1},"best_floor":{"numerator":-1,"denominator":1},"status":"CERTIFIED_LOWER_FLOOR_ONLY"}
        self.assertEqual(V.verify(d)["status"],"CERTIFIED_LOWER_FLOOR_ONLY")
if __name__=="__main__": unittest.main()
