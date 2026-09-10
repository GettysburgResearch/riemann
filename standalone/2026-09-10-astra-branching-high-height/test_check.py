#!/usr/bin/env python3
"""Bounded component tests; not machine verification of the analytic theorem."""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bhh_check',HERE/'check.py')
core=importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)

class Checks(unittest.TestCase):
    def test_01_atomic_recurrence(self):
        self.assertEqual(len(core.polynomial_controls()),10)
        self.assertEqual(len(core.atom_controls()),6)

    def test_02_complete_derivative_measures(self):
        self.assertEqual(core.beta_derivative_controls(),156)
        self.assertEqual(core.scaling_controls(),
                         {'scaled_atom_moments':364,'literal_W_moments':18})

    def test_03_complex_polynomials(self):
        self.assertEqual(core.rational_polynomial_controls(),35)

    def test_04_rational_thresholds(self):
        r=core.threshold_records()
        self.assertEqual(len(r),7)
        self.assertEqual([x['threshold'] for x in r[:4]],
                         ['320','279109','1788260812445057',
                          '3097471590717602242860533234898291413963'])
        self.assertEqual([x['threshold_decimal_digits'] for x in r],[3,6,16,40,98,235,548])

    def test_05_real_cli_refusals(self):
        def seal(folder):
            names=sorted(core.FILES-{'SHA256SUMS'})
            (folder/'SHA256SUMS').write_text(''.join(
                hashlib.sha256((folder/n).read_bytes()).hexdigest()+'  '+n+'\n'
                for n in names),encoding='utf8')
        def change_data(folder,operation):
            path=folder/'result.json';o=json.loads(path.read_text())
            operation(o);path.write_text(json.dumps(o,indent=2)+'\n');seal(folder)
        def replace_source(folder,old,new):
            path=folder/'check.py';s=path.read_text()
            self.assertIn(old,s)
            path.write_text(s.replace(old,new,1));seal(folder)
        def wrong_head(folder):
            path=folder/'SOURCES.json';o=json.loads(path.read_text())
            o['primary']['head']='0'*40
            path.write_text(json.dumps(o,indent=2)+'\n');seal(folder)
        def duplicate(folder):
            path=folder/'result.json';s=path.read_text()
            path.write_text('{"schema":"BHH26-v1",'+s[1:]);seal(folder)
        cases=[
          ('false_RH',lambda p:change_data(p,lambda o:o.update(rh_proved=True))),
          ('false_bounded_window',lambda p:change_data(p,lambda o:o.update(bounded_window_confinement_proved=True))),
          ('wrong_threshold',lambda p:change_data(p,lambda o:o['thresholds'][1].update(threshold='279108'))),
          ('lost_remainder',lambda p:change_data(p,lambda o:o['thresholds'][1].update(error_E0='0'))),
          ('wrong_atom',lambda p:change_data(p,lambda o:o['polynomials'][1]['row'].__setitem__(1,-3))),
          ('lost_coverage',lambda p:change_data(p,lambda o:o.update(beta_derivative_moments=0))),
          ('float_alias',lambda p:change_data(p,lambda o:o['thresholds'][0].update(depth=0.0))),
          ('bool_alias',lambda p:change_data(p,lambda o:o['thresholds'][0].update(depth=False))),
          ('duplicate_JSON',duplicate),
          ('source_drift',wrong_head),
          ('proof_drift',lambda p:(p/'PROOF.md').write_text((p/'PROOF.md').read_text()+'\nUNREVIEWED CHANGE\n')),
          ('extra_file',lambda p:(p/'extra.txt').write_text('not covered\n')),
          ('missing_file',lambda p:(p/'README.md').unlink()),
          ('resealed_coefficient_mutation',lambda p:replace_source(p,'else 0)-2*(u[j-1]**2','else 0)-3*(u[j-1]**2')),
          ('resealed_offdiagonal_deletion',lambda p:replace_source(p,'hi**power-2*off','hi**power-off')),
          ('resealed_uniform_endpoint',lambda p:replace_source(p,'2*F(4)**(m+1-j)-1','F(4)**(m+1-j)-1')),
        ]
        executed=[]
        with tempfile.TemporaryDirectory(prefix='bhh_cli_') as tmp:
            base=Path(tmp)
            def run(folder):
                cmd=[sys.executable,'-I','-S','-B']
                if sys.flags.optimize:cmd.append('-O')
                cmd += [str(folder/'check.py'),'--check',str(folder/'result.json')]
                return subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            pristine=base/'pristine';shutil.copytree(HERE,pristine)
            p=run(pristine)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            self.assertTrue(p.stdout.startswith('PASS_BHH26 '),p.stdout)
            for name,mutation in cases:
                folder=base/name;shutil.copytree(HERE,folder)
                mutation(folder)
                p=run(folder)
                self.assertNotEqual(p.returncode,0,name+' unexpectedly accepted')
                self.assertIn('REJECT_BHH26',p.stderr,name+': '+p.stdout+p.stderr)
                executed.append(name)
        self.assertEqual(len(executed),16)
        print('PASS_REAL_CLI: one acceptance; '+str(len(executed))+' executed refusals',flush=True)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Checks)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
