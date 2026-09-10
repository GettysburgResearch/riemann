#!/usr/bin/env python3
"""Run bounded and real-CLI controls; report success only from the test result.
The symlink test explicitly skips on hosts without symlink privilege. A skip
is reported and never counted as a completed corruption refusal.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bor_check',ROOT/'check.py')
check=importlib.util.module_from_spec(spec);spec.loader.exec_module(check)
TALLY={'cli_acceptances':0,'cli_refusals':0}


def seal(root):
    names=sorted(check.FILES-{'SHA256SUMS'})
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names),encoding='ascii')


def run(root,args):
    cmd=[sys.executable,'-I','-S','-B']
    if sys.flags.optimize:cmd+=['-O']
    cmd+=[str(root/'check.py')]+args
    return subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=90)


class Tests(unittest.TestCase):
    def accepted(self,r):
        self.assertEqual(r.returncode,0,r.stderr.decode());self.assertIn(b'PASS_BOR26_',r.stdout)
        TALLY['cli_acceptances']+=1
    def rejected(self,r):
        self.assertEqual(r.returncode,2,(r.stdout+r.stderr).decode());self.assertIn(b'REJECT_BOR26',r.stderr)
        TALLY['cli_refusals']+=1
    def test_exact_components(self):
        check.authenticate();r=check.reconstruct(only_algebra=True)
        self.assertIs(r['root_certificate_executed'],False)
        self.assertEqual(len(r['algebra']['ordered_moment_stages']),33)
        self.assertEqual(len(r['algebra']['peano_models']),6)
    def test_primitive_rejections(self):
        m=check.module()
        for x in (True,1.0,'1'):
            with self.assertRaises(TypeError):m.I.of(x)
        with self.assertRaises(ValueError):m.I(1,0)
        with self.assertRaises(ZeroDivisionError):m.I.of(1)/m.I(-1,1)
        with self.assertRaises(ValueError):m.log_i(0)
        with self.assertRaises(ValueError):m.sqrt_i(-1)
        with self.assertRaises(ValueError):m.log_c(m.C(-1,1))
    def test_fast_real_cli(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'packet';shutil.copytree(ROOT,root)
            self.accepted(run(root,['--algebra']))
            original={n:(root/n).read_bytes() for n in check.FILES}
            def reset():
                for p in root.iterdir():
                    if p.is_file() or p.is_symlink():p.unlink()
                for n,b in original.items():(root/n).write_bytes(b)
            mutations=[
                ('unsealed proof',lambda:(root/'PROOF.md').write_text('changed')),
                ('extra inventory',lambda:(root/'extra').write_text('x')),
                ('missing file',lambda:(root/'README.md').unlink()),
                ('empty manifest',lambda:(root/'SHA256SUMS').write_text('')),
            ]
            for name,mut in mutations:
                with self.subTest(name=name):
                    reset();mut();self.rejected(run(root,['--algebra']))
            # Resealed semantic mutations must fail reconstruction or exact source pin.
            for name in ('source','uniform moment','mixing factor'):
                with self.subTest(name=name):
                    reset()
                    if name=='source':
                        p=root/'SOURCES.json';d=json.loads(p.read_text());d['parent']['head']='0'*40;p.write_text(json.dumps(d))
                    elif name=='uniform moment':
                        p=root/'check.py';s=p.read_text();old='(1-Q(2)**(1-2*j))/(2*j-1)';new='(1-Q(3)**(1-2*j))/(2*j-1)'
                        self.assertIn(old,s);p.write_text(s.replace(old,new,1))
                    else:
                        p=root/'certificate.py';s=p.read_text();old='raw.append(6*v/Q(';new='raw.append(5*v/Q('
                        self.assertIn(old,s);p.write_text(s.replace(old,new,1))
                    seal(root);self.rejected(run(root,['--algebra']))
            reset()
            for name,b in [('duplicate',b'{"x":1,"x":2}'),('float',b'{"x":1.0}'),('empty',b'{}'),('nonobject',b'[]')]:
                with self.subTest(name=name):
                    p=Path(t)/'bad.json';p.write_bytes(b);self.rejected(run(root,['--check',str(p)]))
    def test_symlink_real_cli(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'packet';shutil.copytree(ROOT,root)
            target=Path(t)/'real-proof';target.write_bytes((root/'PROOF.md').read_bytes());(root/'PROOF.md').unlink()
            try:(root/'PROOF.md').symlink_to(target)
            except (OSError,NotImplementedError) as e:self.skipTest('host cannot create symlink: '+str(e))
            self.rejected(run(root,['--algebra']))
    def test_full_real_cli(self):
        with tempfile.TemporaryDirectory() as t:
            root=Path(t)/'packet';shutil.copytree(ROOT,root)
            self.accepted(run(root,['--check',str(root/'result.json')]))
            original=json.loads((root/'result.json').read_text())
            for name in ('numeric alias','wrong full endpoint'):
                with self.subTest(name=name):
                    d=copy.deepcopy(original)
                    if name=='numeric alias':d['root']['moment_degree']=True
                    else:d['root']['whole_value']['real']['hi_hex']='0x0'
                    p=Path(t)/'altered.json';p.write_text(json.dumps(d))
                    self.rejected(run(root,['--check',str(p)]))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--part',choices=['all','fast','full'],default='all');a=ap.parse_args()
    names=unittest.defaultTestLoader.getTestCaseNames(Tests)
    if a.part=='fast':names=[n for n in names if n!='test_full_real_cli']
    if a.part=='full':names=['test_full_real_cli']
    result=unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(Tests(n) for n in names))
    report={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),**TALLY,'optimized':bool(sys.flags.optimize)}
    print(json.dumps(report,sort_keys=True))
    sys.exit(0 if result.wasSuccessful() else 1)
