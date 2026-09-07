#!/usr/bin/env python3
"""Exercise the actual CLI, including resealed semantic corruptions."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('qpcheck',ROOT/'check.py')
check=importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
PARENT=ROOT.parent/'2026-09-07-astra-future-realization'/'PROOF.md'

def seal(root):
    (root/'SHA256SUMS').write_text(''.join(check.sha((root/f).read_bytes())+'  '+f+'\n' for f in check.FILES))

def command(root,parent):
    flags=['-I','-B']+(['-O'] if sys.flags.optimize else [])
    return [sys.executable,*flags,str(root/'check.py'),'--root',str(root),'--parent',str(parent)]

class Tests(unittest.TestCase):
    def test_complete_reconstruction(self):
        check.inventory(ROOT)
        check.authenticate_parent(PARENT)
        self.assertTrue(check.strict_same(check.load(ROOT/'verification.json'),check.reconstruct()))

    def test_integer_rank_validation(self):
        for x in [True,False,-1,1.5,'4',None]:
            with self.subTest(value=x):
                with self.assertRaises(check.Rejection): check.parameters(x)

    def test_type_fidelity(self):
        self.assertFalse(check.strict_same(False,0))
        self.assertFalse(check.strict_same(1,True))
        self.assertTrue(check.strict_same({'a':[1,False]},{'a':[1,False]}))

    def test_cli_pristine(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'packet'; shutil.copytree(ROOT,root)
            parent=Path(t)/'parent.md'; shutil.copy2(PARENT,parent)
            p=subprocess.run(command(root,parent),capture_output=True,text=True,timeout=10)
            self.assertEqual(p.returncode,0,p.stderr)
            self.assertEqual(json.loads(p.stdout)['result'],'PASS_SCOPED_BOUNDED_CONTROLS')

    def test_cli_rejections(self):
        cases=['false_rh','boolean_alias','wrong_floor','wrong_projection','wrong_inverse_cost',
               'narrowed_scope','float','duplicate_json','empty_manifest','extra_file',
               'parent_changed','packet_symlink']
        for case in cases:
            with self.subTest(case=case), tempfile.TemporaryDirectory() as t:
                root=Path(t)/'packet'; shutil.copytree(ROOT,root)
                parent=Path(t)/'parent.md'; shutil.copy2(PARENT,parent)
                obj=check.load(root/'verification.json')
                if case=='false_rh': obj['rh_proved']=True
                elif case=='boolean_alias': obj['rh_proved']=0
                elif case=='wrong_floor': obj['rank_panels'][0]['floor_bits']-=1
                elif case=='wrong_projection': obj['nonouter_controls'][0]['squared_error']='0'
                elif case=='wrong_inverse_cost': obj['rational_boundary_models'][0]['input_norm_squared']='1'
                elif case=='narrowed_scope': obj['config']['ranks']=[]
                if case in cases[:6]:
                    (root/'verification.json').write_text(check.canonical(obj)); seal(root)
                elif case=='float':
                    text=(root/'verification.json').read_text().replace('"bounded_controls": 1994','"bounded_controls": 1994.0')
                    (root/'verification.json').write_text(text); seal(root)
                elif case=='duplicate_json':
                    text=(root/'verification.json').read_text()
                    (root/'verification.json').write_text(text.replace('{','{"rh_proved": false,',1)); seal(root)
                elif case=='empty_manifest': (root/'SHA256SUMS').write_text('')
                elif case=='extra_file': (root/'unexpected.txt').write_text('x')
                elif case=='parent_changed': parent.write_text(parent.read_text()+'\nchanged\n')
                elif case=='packet_symlink':
                    p=root/'README.md'; real=Path(t)/'readme.txt'; p.replace(real); p.symlink_to(real)
                result=subprocess.run(command(root,parent),capture_output=True,text=True,timeout=10)
                self.assertNotEqual(result.returncode,0,case+' incorrectly accepted')
                self.assertIn('REJECT:',result.stderr)

if __name__=='__main__': unittest.main(verbosity=2)
