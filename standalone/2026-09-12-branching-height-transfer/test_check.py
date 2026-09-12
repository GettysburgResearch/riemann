#!/usr/bin/env python3
"""Fast bounded tests and real altered-copy CLI refusals, not analytic review."""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('bht_checker', ROOT/'check.py')
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


def seal(root):
    (root/'SHA256SUMS').write_text(''.join(
        hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n'
        for n in check.PAYLOAD), 'ascii')


class Tests(unittest.TestCase):
    def test_radius_boundaries(self):
        for n in (2**19-13,2**19-12,2**19-11):
            rec=check.prescription(n)
            self.assertLessEqual(n+12,2**rec['ell'])
            self.assertGreater(n+12,2**(rec['ell']-1))
        for bad in (False,1.5,2**18-1):
            with self.assertRaises(ValueError): check.prescription(bad)

    def test_log_primitives(self):
        lo,hi=check.log_bounds(Q(5,2))
        self.assertGreater(lo,Q(9,10)); self.assertLess(hi,1)
        self.assertEqual(check.inverse_moment(4),Q(319375,3456))
        self.assertEqual(check.inverse_moment(1),Q(35,24))

    def test_synthetic_direct_multiplication(self):
        for q in (Q(1,16),Q(29,400),Q(1,8)):
            left=[1600+q,-80,1]; right=[1600+q,80,1]
            product=[Q(0)]*5
            for i,a in enumerate(left):
                for j,b in enumerate(right): product[i+j]+=a*b
            self.assertEqual(product,check.coeffs(q))
            self.assertEqual(product[3],0)

    def test_full_reconstruction(self):
        check.authenticate(ROOT)
        self.assertEqual(check.canonical(check.load_strict(ROOT/'result.json')),
                         check.canonical(check.reconstruct()))

    def test_actual_cli_mutations(self):
        modes=['-I','-S','-B']
        if sys.flags.optimize: modes += ['-O']
        with tempfile.TemporaryDirectory() as td:
            base=Path(td)
            pristine=base/'pristine'; shutil.copytree(ROOT,pristine)
            command=lambda root:[sys.executable,*modes,str(root/'check.py'),'--check',str(root/'result.json')]
            result=subprocess.run(command(pristine),capture_output=True,text=True,timeout=45)
            self.assertEqual(result.returncode,0,result.stderr)
            mutations=['false_rh','false_confinement','wrong_radius','wrong_inverse',
                       'float_alias','boolean_alias','duplicate','proof_drift','extra_file','missing_file']
            executed=0
            for kind in mutations:
                root=base/kind; shutil.copytree(ROOT,root)
                path=root/'result.json'; obj=json.loads(path.read_text())
                if kind=='false_rh': obj['status']['rh_proved']=True
                elif kind=='false_confinement': obj['status']['unbounded_line_confinement_proved']=True
                elif kind=='wrong_radius': obj['height_prescriptions'][0]['radius_exponent']+=1
                elif kind=='wrong_inverse': obj['source_constants']['inverse_moments']['4']='1'
                elif kind=='float_alias': obj['height_prescriptions'][0]['height_and_onset']=float(2**18)
                elif kind=='boolean_alias': obj['synthetic_control'][1]['depth']=True
                if kind in mutations[:6]:
                    path.write_text(json.dumps(obj,sort_keys=True)+'\n','utf-8'); seal(root)
                elif kind=='duplicate':
                    text=path.read_text(); path.write_text(text.replace('{','{"schema":"BHT26-v1",',1)); seal(root)
                elif kind=='proof_drift':
                    with (root/'PROOF.md').open('a') as out: out.write('\nunauthenticated edit\n')
                elif kind=='extra_file': (root/'unlisted.txt').write_text('extra')
                elif kind=='missing_file': (root/'REVIEW.md').unlink()
                result=subprocess.run(command(root),capture_output=True,text=True,timeout=45)
                self.assertNotEqual(result.returncode,0,kind+' unexpectedly accepted')
                self.assertIn('REJECT:',result.stderr,kind)
                executed+=1
            self.assertEqual(executed,len(mutations))
            print('EXECUTED_CLI_ACCEPTANCES=1 EXECUTED_CLI_REFUSALS='+str(executed))

if __name__=='__main__':
    unittest.main(verbosity=2)
