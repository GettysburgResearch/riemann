import importlib.util
from pathlib import Path
import unittest

P=Path(__file__).resolve().parents[1]/'verify.py'
spec=importlib.util.spec_from_file_location('v91840',P)
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)

class Test91840(unittest.TestCase):
    def test_control(self):
        out=v.verify()
        self.assertEqual(out['verdict'],'PASS_PR484_EXACT_ROOT_COMPOSITION_RECOVERY')
        self.assertLess(out['native_cost']['total'],61000)
    def test_mutations(self):
        for name,fn in v.MUTATIONS.items():
            with self.assertRaises(AssertionError,msg=name): fn(name)

if __name__=='__main__': unittest.main()
