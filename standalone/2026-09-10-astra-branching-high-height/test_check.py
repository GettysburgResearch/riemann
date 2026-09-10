"""Bounded reconstruction and actual changed-copy CLI controls; no RH acceptance."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bhh',HERE/'check.py')
core=importlib.util.module_from_spec(spec);spec.loader.exec_module(core)

def seal(path):
    names=sorted(core.FILES-{'SHA256SUMS'})
    (path/'SHA256SUMS').write_text(''.join(hashlib.sha256((path/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

class Tests(unittest.TestCase):
    def test_literal_moments(self):
        x=core.moment_controls();self.assertEqual(x['coefficient_identities'],78)
    def test_polynomial_and_pole_routes(self):
        x=core.polynomial_controls();self.assertEqual(x['rows'][3]['P'],[1,4,3136,16384])
        self.assertEqual(core.local_pole_controls()['principal_pair_mass'],'5/64')
    def test_gamma_models(self):
        self.assertEqual(len(core.gamma_model_controls()['synthetic_gamma_ratios']),40)
    def test_actual_cli_refusals(self):
        modes=['-O'] if sys.flags.optimize else []
        refusals=0
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp)/'packet';shutil.copytree(HERE,p)
            baseline={n:(p/n).read_bytes() for n in core.FILES}
            def reset():
                for q in p.iterdir():
                    if q.is_file():q.unlink()
                for n,data in baseline.items():(p/n).write_bytes(data)
            def run():
                return subprocess.run([sys.executable,'-I','-S','-B',*modes,str(p/'check.py'),'--check',str(p/'result.json')],
                                      capture_output=True,text=True,timeout=30)
            pristine=run();self.assertEqual(pristine.returncode,0,pristine.stderr)
            mutations=[
                lambda r:r.update(rh_proved=True),
                lambda r:r.update(all_height_zero_safety_proved=True),
                lambda r:r.update(thresholds_numerically_instantiated=True),
                lambda r:r['polynomials']['rows'][2]['P'].__setitem__(2,63),
                lambda r:r['polynomials']['rows'][1].update(beta=10),
                lambda r:r['local_poles'].update(principal_pair_mass='1'),
                lambda r:r['moments'].update(coefficient_identities=True),
            ]
            for mutate in mutations:
                reset();r=json.loads((p/'result.json').read_text());mutate(r)
                (p/'result.json').write_text(json.dumps(r));seal(p)
                outcome=run();self.assertNotEqual(outcome.returncode,0);refusals+=1
            reset();text=(p/'result.json').read_text();(p/'result.json').write_text(text.replace('"rh_proved": false','"rh_proved": false, "rh_proved": false'))
            seal(p);self.assertNotEqual(run().returncode,0);refusals+=1
            reset();text=(p/'check.py').read_text();self.assertIn('DELAY_COEFFICIENT = 2',text)
            (p/'check.py').write_text(text.replace('DELAY_COEFFICIENT = 2','DELAY_COEFFICIENT = 3'));seal(p)
            outcome=run();self.assertNotEqual(outcome.returncode,0)
            self.assertIn('shared-uniform differential identity',outcome.stderr);refusals+=1
            reset();(p/'PROOF.md').write_text('altered proof')
            self.assertNotEqual(run().returncode,0);refusals+=1
            reset();(p/'extra.txt').write_text('unexpected')
            self.assertNotEqual(run().returncode,0);refusals+=1
            self.assertEqual(refusals,11)
        print('EXECUTED_BHH26_CLI: 1 pristine acceptance; 11 refusals',flush=True)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)
