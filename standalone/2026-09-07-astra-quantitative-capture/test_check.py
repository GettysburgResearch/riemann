#!/usr/bin/env python3
"""Bounded HC26 regressions. These do not validate infinite analytic proofs."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).absolute().parent
ns={'__name__':'hc26_tests_core','__file__':str(ROOT/'check.py')}
exec(compile((ROOT/'check.py').read_bytes(),str(ROOT/'check.py'),'exec'),ns)
FILES=ns['FILES']

class Tests(unittest.TestCase):
    def seal(self,p:Path)->None:
        (p/'SHA256SUMS').write_text(''.join(
            hashlib.sha256((p/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in FILES),encoding='ascii')

    def run_cli(self,p:Path,root_arg:Path|None=None)->subprocess.CompletedProcess:
        cmd=[sys.executable,'-I','-B']
        if sys.flags.optimize: cmd.append('-O')
        cmd += [str(p/'check.py')]
        if root_arg is not None: cmd += ['--root',str(root_arg)]
        return subprocess.run(cmd,capture_output=True,text=True,timeout=15)

    def test_exact_reconstruction(self):
        result=ns['reconstruct']()
        self.assertEqual(result['bounded_controls'],1235)
        self.assertEqual(result['groups']['synthetic_projection'],211)
        self.assertEqual(ns['canon'](result),(ROOT/'verification.json').read_bytes())

    def test_reference_projection(self):
        F=ns['F']
        e,_,_=ns['projection'](2,[F(1)])
        self.assertEqual(e,F(16,21))
        e,_,_=ns['projection'](1,[F(1),F(-2)])
        self.assertEqual(e,F(0))
        self.assertGreater(ns['reconstruct']()['groups']['fejer_factors'],600)

    def test_cli_corruptions(self):
        names=['rh_true','bound_true','paper_as_machine_verified','boolean_alias',
               'narrow_scope','wrong_error','source_drift','float','duplicate_json',
               'empty_manifest','missing_manifest_entry','extra_file','missing_file']
        with tempfile.TemporaryDirectory(prefix='hc26_cli_') as td:
            base=Path(td)
            pristine=base/'pristine';shutil.copytree(ROOT,pristine)
            out=self.run_cli(pristine)
            self.assertEqual(out.returncode,0,out.stdout+out.stderr)
            for name in names:
                p=base/name;shutil.copytree(ROOT,p)
                rec=json.loads((p/'verification.json').read_text())
                if name=='rh_true': rec['rh_proved']=True
                elif name=='bound_true': rec['full_bound_10_proved']=True
                elif name=='paper_as_machine_verified': rec['paper_capture_theorem']='machine verified'
                elif name=='boolean_alias': rec['bounded_controls']=True
                elif name=='narrow_scope': rec['scope']['targets']=1
                elif name=='wrong_error': rec['synthetic_projection_panels'][0]['error']='0/1'
                if name in names[:6]:
                    (p/'verification.json').write_bytes(ns['canon'](rec));self.seal(p)
                elif name=='source_drift':
                    rec=json.loads((p/'SOURCE_LOCK.json').read_text());rec['parent_sha256']='0'*64
                    (p/'SOURCE_LOCK.json').write_bytes(ns['canon'](rec));self.seal(p)
                elif name=='float':
                    s=(p/'verification.json').read_text().replace('"bounded_controls": 1235','"bounded_controls": 1235.0')
                    (p/'verification.json').write_text(s);self.seal(p)
                elif name=='duplicate_json':
                    s=(p/'verification.json').read_text();s=s.replace('{','{"rh_proved": false,',1)
                    (p/'verification.json').write_text(s);self.seal(p)
                elif name=='empty_manifest': (p/'SHA256SUMS').write_text('')
                elif name=='missing_manifest_entry':
                    lines=(p/'SHA256SUMS').read_text().splitlines();(p/'SHA256SUMS').write_text('\n'.join(lines[1:])+'\n')
                elif name=='extra_file': (p/'undeclared.txt').write_text('extra')
                elif name=='missing_file': (p/'README.md').unlink()
                out=self.run_cli(p)
                self.assertNotEqual(out.returncode,0,name+' unexpectedly passed')
                self.assertIn('REJECT_HC26',out.stdout,name+': '+out.stderr)
        print('CLI_CORRUPTIONS_REJECTED=13; PRISTINE_CLI_PASSES=1')

    def test_symlink_rejections(self):
        with tempfile.TemporaryDirectory(prefix='hc26_links_') as td:
            base=Path(td);p=base/'packet';shutil.copytree(ROOT,p)
            outside=base/'outside.md';outside.write_bytes((p/'PROOF.md').read_bytes())
            (p/'PROOF.md').unlink()
            try: (p/'PROOF.md').symlink_to(outside)
            except OSError as e:
                if getattr(e,'winerror',None)==1314:
                    self.skipTest('Windows account lacks symlink privilege; two controls unexecuted')
                raise
            out=self.run_cli(p)
            self.assertNotEqual(out.returncode,0,out.stdout+out.stderr)
            self.assertIn('REJECT_HC26',out.stdout)
            p2=base/'clean';shutil.copytree(ROOT,p2)
            link=base/'root_link';link.symlink_to(p2,target_is_directory=True)
            out=self.run_cli(p2,link)
            self.assertNotEqual(out.returncode,0,out.stdout+out.stderr)
            self.assertIn('REJECT_HC26',out.stdout)
        print('SYMLINK_CLI_REJECTIONS=2')

if __name__=='__main__': unittest.main(verbosity=2)
