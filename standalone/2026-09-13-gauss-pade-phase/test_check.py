#!/usr/bin/env python3
"""Bounded exact tests and actual CLI refusals. No numerical-zero certification."""
from __future__ import annotations
import argparse,copy,hashlib,json,os,shutil,subprocess,sys,tempfile,unittest
from pathlib import Path
import importlib.util

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("gpp26_check",ROOT/"check.py")
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load sibling exact checker")
check=importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)
OPT=sys.flags.optimize>0


def seal(root):
    data={'algorithm':'sha256','files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.iterdir()) if p.is_file() and p.name!='MANIFEST.json'}}
    (root/'MANIFEST.json').write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')


class PacketTests(unittest.TestCase):
    accepted=0;refused=0

    def copy_and_run(self,mutate=None,reseal=False,expected=0):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)/'packet';shutil.copytree(ROOT,root)
            if mutate:mutate(root)
            if reseal:seal(root)
            cmd=[sys.executable,'-I','-S','-B']+(['-O'] if OPT else [])+['check.py','--check','results.json']
            result=subprocess.run(cmd,cwd=root,text=True,capture_output=True,timeout=40)
            if expected==0:
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertIn('PASS_BOUNDED_EXACT_GPP26',result.stdout);type(self).accepted+=1
            else:
                self.assertNotEqual(result.returncode,0,'altered CLI unexpectedly accepted')
                self.assertIn('REFUSED:',result.stderr);type(self).refused+=1

    def test_01_exact_small_source(self):
        p,q=check.continuants(1)
        self.assertEqual(p,[check.F(1),check.F(2,5)])
        self.assertEqual(q,[check.F(1)])
        self.assertEqual(check.pade(3),[check.F(1),check.F(1),check.F(2,5),check.F(1,15)])
        self.assertEqual(check.ring_controls(),5)

    def test_02_pristine_cli(self):self.copy_and_run()

    def test_03_resealed_receipt_refusals(self):
        actions=[lambda d:d.update(status='RH_PROVED'),
                 lambda d:d.update(native_zero_certificates=1),
                 lambda d:d['counts'].update(pade_orders=50),
                 lambda d:d.update(analytic_limits_machine_proved=0)]
        for action in actions:
            def mutate(root,action=action):
                p=root/'results.json';d=json.loads(p.read_text());action(d)
                p.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n')
            self.copy_and_run(mutate,True,1)

    def test_04_json_parser_refusals(self):
        for text in ['{"x":1,"x":2}', '{"x":1.0}']:
            self.copy_and_run(lambda root,text=text:(root/'results.json').write_text(text),True,1)

    def test_05_resealed_mathematical_mutation(self):
        def mutate(root):
            p=root/'check.py';s=p.read_text()
            old='return -F(r*(4*r*r-7),6)'
            self.assertEqual(s.count(old),1)
            p.write_text(s.replace(old,'return F(r*(4*r*r-7),6)'))
        self.copy_and_run(mutate,True,1)

    def test_06_inventory_refusal(self):
        self.copy_and_run(lambda root:(root/'unexpected.txt').write_text('extra'),False,1)

    def test_07_unsealed_source_refusal(self):
        self.copy_and_run(lambda root:(root/'PROOF.md').write_text((root/'PROOF.md').read_text()+'\nchanged\n'),False,1)


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(PacketTests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if result.wasSuccessful():
        print('PASS_TEST_SUITE',{'methods':result.testsRun,'actual_cli_acceptances':PacketTests.accepted,
                                'actual_cli_refusals':PacketTests.refused,'optimized':OPT})
    sys.exit(0 if result.wasSuccessful() else 1)
