import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("verify",ROOT/"verify.py")
verify=importlib.util.module_from_spec(spec); assert spec.loader; spec.loader.exec_module(verify)
class TestMetric(unittest.TestCase):
    def test_object(self):
        o=verify.proof_object()
        self.assertTrue(o["packet_tonelli_identity"])
        self.assertTrue(o["capacity_orientation_mutation_rejected"])
if __name__=="__main__": unittest.main()
