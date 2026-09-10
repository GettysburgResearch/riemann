#!/usr/bin/env python3
"""Bounded unit and actual-command rejection tests; no removable assertions."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import types
import unittest
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
module=types.ModuleType('balanced_hyperbola_replay')
module.__file__=str(ROOT/'scripts/replay.py')
exec(compile((ROOT/'scripts/replay.py').read_bytes(),module.__file__,'exec'),module.__dict__)
R=module

class ReplayTests(unittest.TestCase):
    def test_primitive_and_negative_inputs(self):
        for n in (1,2,3,9,30,49,210):self.assertEqual(R.mu_sieve(n)[n],R.mu_trial(n))
        for bad in (True,0,-1,1.0):
            with self.assertRaises(ValueError):R.mu_sieve(bad)
        mu=R.mu_sieve(31)
        for bad in (2,4,True,33):
            with self.assertRaises(ValueError):R.terminal(bad,mu)
    def test_kernel_boundary(self):
        from fractions import Fraction as F
        self.assertEqual(R.w(F(1)),0)
        self.assertEqual(R.w(F(1,2)),0)
        self.assertEqual(R.w(F(3)),2)
        self.assertEqual(R.w(F(5)),F(14,3))
    def test_exact_seed_and_terminal_boundary(self):
        from fractions import Fraction as F
        mu=R.mu_sieve(81)
        c=R.terminal(3,mu)
        self.assertEqual(c,{1:F(1),3:F(-3)})
        self.assertEqual(R.form(3,c),F(-32,35))
        self.assertEqual(R.terminal(9,mu)[9],F(-102,35))
    def test_parent_and_inventory(self):
        R.authenticate_parent();R.manifest()
    def test_full_exact_reconstruction(self):
        self.assertEqual(R.canonical(R.replay()),R.canonical(R.strict_load(ROOT/'verification.json')))
    def test_json_rejects_duplicates_and_floats(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'x.json'
            for text in ('{"a":1,"a":2}','{"a":1.0}','{"a":NaN}'):
                p.write_text(text)
                with self.assertRaises(ValueError):R.strict_load(p)
    def test_actual_cli_corruptions(self):
        cases=('rh_true','false_alias','smaller_scope','wrong_quadratic_sign','lost_terminal',
               'missing_source_row','wrong_boundary','wrong_lobe_sign','floating_alias',
               'source_lock','parent_bytes','duplicate_json','empty_manifest','extra_file','symlink')
        for case in cases:
            with self.subTest(case=case),tempfile.TemporaryDirectory() as td:
                outer=Path(td)/'standalone';p=outer/ROOT.name
                shutil.copytree(ROOT,p)
                pp=outer/'2026-09-06-astra-terminal-endpoint/PROOF.md'
                pp.parent.mkdir(parents=True);shutil.copyfile(R.PARENT,pp)
                out=R.strict_load(p/'verification.json')
                reseal=True
                if case=='rh_true':out['rh_proved']=True
                elif case=='false_alias':out['rh_proved']=0
                elif case=='smaller_scope':out['config']['primitive_mu_cap']=100
                elif case=='wrong_quadratic_sign':out['quadratic_panel'][0]['balanced_form']='32/35'
                elif case=='lost_terminal':out['quadratic_panel'][3]['terminal_coefficient']='0'
                elif case=='missing_source_row':out['quadratic_panel'].pop()
                elif case=='wrong_boundary':out['higher_order_panel'][0]['boundary_error']='0'
                elif case=='wrong_lobe_sign':out['signed_lobes'][0]['negative']['value']='1'
                elif case=='floating_alias':out['total_checks']=float(out['total_checks'])
                elif case=='source_lock':
                    lock=R.strict_load(p/'SOURCE_LOCK.json');lock['head']='0'*40
                    (p/'SOURCE_LOCK.json').write_text(R.canonical(lock))
                elif case=='parent_bytes':pp.write_bytes(pp.read_bytes()+b'\nchanged\n')
                elif case=='empty_manifest':(p/'SHA256SUMS').write_text('');reseal=False
                elif case=='extra_file':(p/'unlisted.txt').write_text('not in expected inventory')
                elif case=='symlink':(p/'unlisted-link').symlink_to('PROOF.md')
                text=R.canonical(out)
                if case=='duplicate_json':text=text.replace('{','{"rh_proved": false,',1)
                (p/'verification.json').write_text(text)
                if reseal:
                    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256((p/f).read_bytes()).hexdigest()
                        +'  '+f+'\n' for f in sorted(R.FILES)))
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
                cmd=[sys.executable]+(['-O'] if sys.flags.optimize else [])+[str(p/'scripts/replay.py')]
                run=subprocess.run(cmd,text=True,capture_output=True,timeout=15,env=env)
                self.assertNotEqual(run.returncode,0,msg=case+' incorrectly accepted')
                self.assertIn('REJECT:',run.stderr,msg=case+' did not fail through checker')
        print('ACTUAL_CLI_CORRUPTIONS_REJECTED',len(cases))

if __name__=='__main__':unittest.main(verbosity=2)
