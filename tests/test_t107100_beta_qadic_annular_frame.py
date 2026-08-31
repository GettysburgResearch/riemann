from pathlib import Path
import json,subprocess,sys,tempfile,unittest
class TestT107100(unittest.TestCase):
 def test_replay(self):
  root=Path(__file__).resolve().parents[1];script=root/'experiments/X-107100-beta-qadic-annular-frame/verify.py'
  with tempfile.TemporaryDirectory() as td:
   out=Path(td)/'v.json';p=subprocess.run([sys.executable,'-B',str(script),'--output',str(out)],check=True,text=True,capture_output=True)
   self.assertIn('PASS_T107100_BETA_QADIC_ANNULAR_FRAME',p.stdout);d=json.loads(out.read_text());self.assertFalse(d['rh_established']);self.assertGreater(d['checks'],20)
if __name__=='__main__':unittest.main()
