import importlib.util
from pathlib import Path
import unittest
import sys
HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("verify",HERE/"verify.py")
v=importlib.util.module_from_spec(spec);sys.modules[spec.name]=v;spec.loader.exec_module(v)
class Tests(unittest.TestCase):
    def test_verdict(self):
        self.assertEqual(v.build()["verdict"],"PASS_T99280_COMPACT_HALL_SUBPOWER_LANDAU_HARDENING")
    def test_hall(self):
        self.assertEqual(v.build()["compact_hall_witness_t"],13)
    def test_profile(self):
        r=v.build();self.assertEqual((r["profile_witness_j"],r["profile_witness_cell"]),(65,66))
    def test_fail_closed(self):
        r=v.build();self.assertFalse(r["local_common_source_ledger_reconstructed"]);self.assertFalse(r["rh_established"])
if __name__=="__main__":unittest.main()
