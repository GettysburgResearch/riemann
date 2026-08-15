import copy, sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from native_fiber import base_certificate, validate, mutation_cases, ContractError, arithmetic_audits

class NativeFiberTests(unittest.TestCase):
    def test_base(self): self.assertIn('cost',validate(base_certificate()))
    def test_mutations(self):
        for name,c in mutation_cases(base_certificate()):
            with self.subTest(name=name):
                with self.assertRaises(ContractError): validate(c)
    def test_arithmetic(self): self.assertEqual(arithmetic_audits(500)['mobius_convolution_checks'],500)

if __name__=='__main__': unittest.main()
