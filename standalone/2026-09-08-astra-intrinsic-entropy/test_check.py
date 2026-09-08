"""Bounded actual CLI corruption controls. Does not review analytic proofs."""
import hashlib,json,os,shutil,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PAYLOAD=('PROOF.md','README.md','REVIEW_AND_SOURCES.md','VALIDATION.md','SOURCE_LOCK.json',
         'interval_core.py','certificate.py','check.py','test_check.py','verification.json')

def reseal(p):
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256((p/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in PAYLOAD))

def cli(p):
    mode=['-O'] if sys.flags.optimize else []
    return subprocess.run([sys.executable,'-B',*mode,str(p/'check.py')],
                          capture_output=True,text=True,timeout=30)

class Tests(unittest.TestCase):
    def test_pristine(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            out=cli(p);self.assertEqual(out.returncode,0,out.stderr)
            self.assertIn('cases=86',out.stdout)
    def test_result_corruptions(self):
        for kind in ('false_RH','target_alias','wrong_energy','bool_degree','dropped_case'):
          with self.subTest(kind=kind),tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            f=p/'verification.json';z=json.loads(f.read_text())
            if kind=='false_RH':z['rh_established']=True
            elif kind=='target_alias':z['actual_certificate']['target']='ramp t exp(-t/2)'
            elif kind=='wrong_energy':z['actual_certificate']['complete_error']['hi']='0'
            elif kind=='bool_degree':z['actual_certificate']['degree']=True
            elif kind=='dropped_case':z['algebra']['data']['synthetic_strip_pairs'].pop()
            f.write_text(json.dumps(z));reseal(p)
            out=cli(p);self.assertNotEqual(out.returncode,0,kind)
            self.assertIn('primitive replay mismatch',out.stderr)
    def test_parser_and_inventory(self):
        for kind in ('duplicate_json','float_alias','empty_manifest','extra_file','symlink_core','modified_core','source_drift'):
          with self.subTest(kind=kind),tempfile.TemporaryDirectory() as td:
            p=Path(td)/'packet';shutil.copytree(ROOT,p)
            if kind=='duplicate_json':
                f=p/'verification.json';f.write_text('{"rh_established":false,"rh_established":true}');reseal(p)
            elif kind=='float_alias':
                z=json.loads((p/'verification.json').read_text());z['actual_certificate']['degree']=6.0
                (p/'verification.json').write_text(json.dumps(z));reseal(p)
            elif kind=='empty_manifest':(p/'SHA256SUMS').write_text('')
            elif kind=='extra_file':(p/'extra.txt').write_text('unaccounted')
            elif kind=='symlink_core':
                target=Path(td)/'core.py';shutil.copyfile(p/'interval_core.py',target)
                (p/'interval_core.py').unlink();os.symlink(target,p/'interval_core.py')
            elif kind=='modified_core':
                f=p/'interval_core.py';f.write_text(f.read_text()+'\n# altered\n');reseal(p)
            elif kind=='source_drift':
                z=json.loads((p/'SOURCE_LOCK.json').read_text());z['base_commit']='0'*40
                (p/'SOURCE_LOCK.json').write_text(json.dumps(z));reseal(p)
            out=cli(p);self.assertNotEqual(out.returncode,0,kind)
    def test_rational_threshold(self):
        from fractions import Fraction as F
        self.assertLess(F(13,250),F(1,1))
        self.assertLess(F(51_343_069_499,10**12),F(13,250))

if __name__=='__main__':unittest.main()
