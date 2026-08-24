import importlib.util,pathlib,unittest
P=pathlib.Path(__file__).resolve().parents[1]/'verify.py'; S=importlib.util.spec_from_file_location('v',P); V=importlib.util.module_from_spec(S); S.loader.exec_module(V)
class T(unittest.TestCase):
    def test_velocity(self): self.assertEqual(V.check_velocity(),['-7/12','-1/12'])
    def test_confluent(self): self.assertEqual(V.check_confluent()['pick'],'-1/3')
    def test_reflection(self): self.assertEqual(len(V.check_reflection()),3)
    def test_resolvent(self): self.assertGreater(V.check_resolvent()['nonzero'],1)
if __name__=='__main__':unittest.main()
