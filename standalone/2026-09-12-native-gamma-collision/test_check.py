"""Bounded tests only. This suite does not rerun the long native integrals."""
from pathlib import Path
import importlib.util,json,tempfile,hashlib,subprocess,sys,unittest,shutil
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('_checker',P/'check.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class Tests(unittest.TestCase):
    def test_exact_reconstruction(self):
        self.assertEqual(m.canonical(m.compute()),m.canonical(m.strict((P/'algebra.json').read_text())))
    def test_density_mass(self):
        Q=m.Q
        for u in [Q(1,3),Q(7,10),Q(1)]:
            rr=m.density_rows([Q(1),Q(4),Q(36)/u])
            self.assertEqual(sum((b/l**2+b*c/l for l,b,c in rr),Q(0)),1)
    def test_strict_json(self):
        for x in ['{"a":1,"a":2}','{"a":1.0}','{"a":NaN}']:
            with self.assertRaises(ValueError):m.strict(x)
        self.assertNotEqual(m.canonical({'a':True}),m.canonical({'a':1}))
    def test_inventory(self):
        self.assertGreater(m.authenticate(),5)
        with tempfile.TemporaryDirectory() as t:
            q=Path(t)/'packet';shutil.copytree(P,q);(q/'extra').write_text('x')
            with self.assertRaises(ValueError):m.authenticate(q)
    def test_actual_algebra_cli(self):
        flags=[sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
        r=subprocess.run(flags+[str(P/'check.py')],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertEqual(r.stdout.strip(),'PASS_BOUNDED_ALGEBRA_NOT_NATIVE_REPLAY')
        with tempfile.TemporaryDirectory() as t:
            q=Path(t)/'packet';shutil.copytree(P,q)
            original=(q/'algebra.json').read_text()
            variants=[]
            a=json.loads(original);a['rh_proved']=True;variants.append(json.dumps(a))
            a=json.loads(original);a['counts']['generator_polynomial_instances']-=1;variants.append(json.dumps(a))
            a=json.loads(original);a['rh_proved']=0;variants.append(json.dumps(a))
            variants.append('{"duplicate":1,"duplicate":2}')
            for text in variants:
                (q/'algebra.json').write_text(text)
                rows=[]
                for line in (P/'SHA256SUMS').read_text().splitlines():
                    h,n=line.split('  ',1)
                    if n=='algebra.json':h=hashlib.sha256(text.encode()).hexdigest()
                    rows.append(h+'  '+n)
                (q/'SHA256SUMS').write_text('\n'.join(rows)+'\n')
                r=subprocess.run(flags+[str(q/'check.py')],capture_output=True,text=True)
                self.assertNotEqual(r.returncode,0,'resealed wrong algebra accepted')
if __name__=='__main__':unittest.main(verbosity=2)
