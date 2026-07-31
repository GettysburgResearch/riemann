import importlib.util,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SP=importlib.util.spec_from_file_location("x14310",ROOT/"verify.py")
V=importlib.util.module_from_spec(SP); sys.modules[SP.name]=V; SP.loader.exec_module(V)

def base():
    return {
      "schema":"riemann.x14310-packet-leverage-floor.v1",
      "classification":"SYNTHETIC_MODEL",
      "tail_gate":{"status":"SYNTHETIC_SYMBOL_TAIL_FLOOR","sha256":"t"*64,
                   "symbol_lower_outside_cells":{"numerator":1,"denominator":1}},
      "packet_gate":{"status":"SYNTHETIC_EXACT_PACKET","sha256":"p"*64},
      "cells":[{"id":"central-well","left":{"numerator":-1,"denominator":2},
                "right":{"numerator":1,"denominator":2},
                "symbol_lower":{"numerator":-10,"denominator":1},
                "density_cap_upper":{"numerator":53,"denominator":1998}}],
      "candidate_levels":[{"numerator":-10,"denominator":1},{"numerator":1,"denominator":1}],
      "expected":{"best_level":{"numerator":1,"denominator":1},
                  "best_floor":{"numerator":1415,"denominator":1998},
                  "status":"CERTIFIED_NONNEGATIVE_PACKET_COMPLEMENT"}}

class Tests(unittest.TestCase):
    def test_strict_radical_control(self):
        self.assertEqual(V.verify(base())["best_floor"],{"numerator":1415,"denominator":1998})
    def test_boolean_rejected(self):
        d=base(); d["cells"][0]["density_cap_upper"]["numerator"]=True
        with self.assertRaises(V.E): V.verify(d)
    def test_wrong_tail_gate_rejected(self):
        d=base(); d["tail_gate"]["status"]="EMPIRICAL"
        with self.assertRaises(V.E): V.verify(d)
    def test_wrong_packet_gate_rejected(self):
        d=base(); d["packet_gate"]["status"]="APPROXIMATE_PACKET"
        with self.assertRaises(V.E): V.verify(d)
    def test_negative_cap_rejected(self):
        d=base(); d["cells"][0]["density_cap_upper"]["numerator"]=-1
        with self.assertRaises(V.E): V.verify(d)
    def test_overlap_rejected(self):
        d=base(); d["cells"].append({"id":"overlap","left":{"numerator":0,"denominator":1},
            "right":{"numerator":1,"denominator":1},"symbol_lower":{"numerator":0,"denominator":1},
            "density_cap_upper":{"numerator":1,"denominator":1}})
        d["candidate_levels"]=[{"numerator":-10,"denominator":1},{"numerator":0,"denominator":1},{"numerator":1,"denominator":1}]
        with self.assertRaises(V.E): V.verify(d)
    def test_incomplete_levels_rejected(self):
        d=base(); d["candidate_levels"]=[{"numerator":1,"denominator":1}]
        with self.assertRaises(V.E): V.verify(d)
    def test_false_floor_rejected(self):
        d=base(); d["expected"]["best_floor"]={"numerator":7,"denominator":10}
        with self.assertRaises(V.E): V.verify(d)
if __name__=="__main__": unittest.main()
