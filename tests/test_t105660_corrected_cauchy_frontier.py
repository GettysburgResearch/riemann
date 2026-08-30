from pathlib import Path
import json,subprocess,sys,tempfile,unittest
class TestT105660(unittest.TestCase):
 def test_replay(self):
  root=Path(__file__).resolve().parents[1];s=root/'experiments/X-105660-cauchy-first-contact/verify.py'
  with tempfile.TemporaryDirectory() as td:
   o=Path(td)/'v.json';p=subprocess.run([sys.executable,'-B',str(s),'--output',str(o)],check=True,text=True,capture_output=True);self.assertIn('PASS_T105660_CORRECTED_CAUCHY_FRONTIER',p.stdout);d=json.loads(o.read_text());self.assertTrue(d['mlc_refuted']);self.assertFalse(d['cti_general_proved']);self.assertFalse(d['rh_established'])
if __name__=='__main__':unittest.main()
