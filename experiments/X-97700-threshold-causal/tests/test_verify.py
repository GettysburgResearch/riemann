import importlib.util
import sys
from pathlib import Path
import unittest

HERE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('t97700',HERE/'verify.py')
mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)

class TestT97700(unittest.TestCase):
    def test_one_prime(self):
        self.assertEqual(mod.one_prime_fixture()['p'],67)
    def test_resolvent(self):
        self.assertEqual(mod.matrix_fixture()['two_node_current'],'-2/9')
    def test_full(self):
        obj=mod.run()
        self.assertFalse(obj['rh_established'])
        self.assertIn('LAPBR67 as stated',obj['refuted'])

if __name__=='__main__':unittest.main()
