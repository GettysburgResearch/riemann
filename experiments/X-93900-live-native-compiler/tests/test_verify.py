import unittest,sys
from pathlib import Path
HERE=Path(__file__).resolve().parents[1];sys.path.insert(0,str(HERE));import verify
class T(unittest.TestCase):
 def test_live(self):x=verify.build();verify.check(x);self.assertEqual(len(x['leaf']['occurrences']),229)
 def test_mutations(self):
  x=verify.build()
  for n,z in verify.muts(x):
   with self.subTest(n=n):
    with self.assertRaises(verify.ContractError):verify.check(z)
if __name__=='__main__':unittest.main()
