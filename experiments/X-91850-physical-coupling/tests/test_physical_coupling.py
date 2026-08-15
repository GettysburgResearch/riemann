import copy, sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from physical_coupling import base_certificate, validate_certificate, mutations, ContractError, run_all
class TestPhysicalCoupling(unittest.TestCase):
    def test_base(self): self.assertGreaterEqual(validate_certificate(base_certificate())['cost'],0)
    def test_mutations_fail(self):
        for name,m in mutations(base_certificate()):
            with self.subTest(name=name):
                with self.assertRaises(ContractError): validate_certificate(m)
    def test_full(self): self.assertEqual(run_all(None)['native_total'],60989)
if __name__=='__main__': unittest.main()
