#!/usr/bin/env python3
"""Bounded controls plus real CLI rejection tests. No infinite theorem is tested."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from hashlib import sha256
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('gfd_check',ROOT/'check.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
COUNTS={'pristine_cli_acceptances':0,'actual_cli_refusals':0,'symlink_refusal_ran':False}

def seal(root):
    (root/'SHA256SUMS').write_text(''.join(sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n'
                                       for n in sorted(c.FILES)))

def command(root):
    return [sys.executable,'-I','-S','-B',*(['-O'] if sys.flags.optimize else []),
            str(root/'check.py'),'--check',str(root/'results.json')]

class Tests(unittest.TestCase):
    def test_simplex_and_endpoint(self):
        for N in range(1,5):
            self.assertEqual(c.partial_derivative(N,2*N-1), c.factorial(N)**4)
            self.assertEqual(c.homogeneous(c.rates(N),1)[1]/(2*N),Q((N+1)*(2*N+1),6))
    def test_positive_density(self):
        for N in (1,4,8):
            x=Q(1,N*N);a,b=c.density_positive(N,x);u,v=c.density_partial(N,x)
            self.assertGreater(a,0);self.assertLessEqual(max(a,u),min(b,v))
            self.assertLess((b-a)/a,Q(1,10**25))
    def test_inertia(self):
        self.assertEqual(c.inertia([[0,1],[1,0]]),[1,1,0])
        self.assertEqual(c.inertia([[1,2],[2,4]]),[1,0,1])
        self.assertEqual(c.inertia([[-1,0],[0,2]]),[1,1,0])
        self.assertEqual(c.inertia([[0,0],[0,0]]),[0,0,2])
    def test_variance_operator(self):
        self.assertEqual(c.variance_S_value([256,0,-32,0,1],Q(4)),-8768)
        self.assertEqual(c.variance_S_value([16,0,-8,0,1],Q(2)),1024)
        self.assertEqual(Q(8768,64),137)
    def test_strict_semantics(self):
        self.assertFalse(c.typed_equal(False,0))
        self.assertFalse(c.typed_equal(1,True))
        with self.assertRaises(ValueError):c.decode('{"x":1,"x":1}')
        with self.assertRaises(ValueError):c.decode('{"x":1.0}')
    def test_real_cli(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'packet';shutil.copytree(ROOT,root)
            p=subprocess.run(command(root),capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr);self.assertIn('PASS_EXACT',p.stdout)
            COUNTS['pristine_cli_acceptances']+=1
        kinds=['rh','bool_alias','float_alias','duplicate','wrong_flow','missing_coverage',
               'wrong_scope','unsealed_proof','missing_file','extra_file','symlink','producer_mutation']
        for kind in kinds:
            with self.subTest(kind=kind),tempfile.TemporaryDirectory() as td:
                root=Path(td)/'packet';shutil.copytree(ROOT,root)
                r=json.loads((root/'results.json').read_text())
                if kind in ['rh','bool_alias','float_alias','wrong_flow','missing_coverage','wrong_scope']:
                    if kind=='rh':r['rh_proved']=True
                    elif kind=='bool_alias':r['rh_proved']=0
                    elif kind=='float_alias':r['counts']['gamma_Laplace_values']=84.0
                    elif kind=='wrong_flow':r['variance_operator'][0]['S_at_double_root'][0]+=1
                    elif kind=='missing_coverage':r['counts'].pop('gamma_derivative_identities')
                    else:r['actual_Hankel_index_computed']=True
                    (root/'results.json').write_text(json.dumps(r));seal(root)
                elif kind=='duplicate':
                    text=(root/'results.json').read_text().replace('"rh_proved": false','"rh_proved": false, "rh_proved": false')
                    (root/'results.json').write_text(text);seal(root)
                elif kind=='unsealed_proof':
                    p=root/'PROOF.md';p.write_text(p.read_text()+'\nmodified\n')
                elif kind=='missing_file':(root/'PROOF.md').unlink()
                elif kind=='extra_file':(root/'extra.txt').write_text('not inventoried')
                elif kind=='symlink':
                    target=Path(td)/'outside.md';target.write_bytes((root/'PROOF.md').read_bytes())
                    (root/'PROOF.md').unlink()
                    try:(root/'PROOF.md').symlink_to(target)
                    except OSError as exc:self.skipTest('Host cannot create symlinks: '+str(exc))
                    COUNTS['symlink_refusal_ran']=True
                else:
                    p=root/'check.py';s=p.read_text().replace('RADIAL_DIFFERENCE_FACTOR = 4','RADIAL_DIFFERENCE_FACTOR = 5')
                    self.assertNotEqual(s,p.read_text());p.write_text(s);seal(root)
                p=subprocess.run(command(root),capture_output=True,text=True)
                self.assertNotEqual(p.returncode,0,'wrongly accepted '+kind)
                self.assertNotIn('PASS_EXACT',p.stdout)
                COUNTS['actual_cli_refusals']+=1

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    summary={'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
             'skips':len(result.skipped),'successful':result.wasSuccessful(),**COUNTS}
    print(json.dumps(summary,sort_keys=True))
    sys.exit(0 if result.wasSuccessful() else 1)
