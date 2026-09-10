#!/usr/bin/env python3
"""Bounded regressions and actual CLI refusals; not a full integral replay.
Run check.py without --quick separately for the complete zero certificate.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('_endpoint_check',ROOT/'check.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
REFUSALS=[]


def reseal(folder):
    (folder/'SHA256SUMS').write_text(''.join(
        hashlib.sha256((folder/name).read_bytes()).hexdigest()+'  '+name+'\n'
        for name in sorted(c.FILES) if name!='SHA256SUMS'))


def command(folder,*args):
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
    return subprocess.run([sys.executable,'-I','-S','-B',*(['-O'] if sys.flags.optimize else []),
        str(folder/'check.py'),*args],capture_output=True,text=True,env=env,timeout=180)


class Tests(unittest.TestCase):
    def test_exact_bounded_reconstruction(self):
        c.expect_equal(c.bounded(),c.read_json(ROOT/'bounded.json'))

    def test_zero_diagonal_inertia(self):
        self.assertEqual(c.exact_inertia([[Q(0),Q(3)],[Q(3),Q(0)]]),[1,1,0])
        self.assertEqual(c.exact_inertia([[Q(0),Q(0)],[Q(0),Q(0)]]),[0,0,2])
        self.assertEqual(c.exact_inertia([[Q(0),Q(2),Q(1)],[Q(2),Q(0),Q(0)],[Q(1),Q(0),Q(0)]]),[1,1,1])

    def test_strict_receipt_comparison(self):
        for a,b in (({'n':1},{'n':True}),({'n':1},{'n':1.0}),({'v':['1','2']},{'v':['1','3']})):
            with self.assertRaises(ValueError):c.expect_equal(a,b)
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x.json'
            for bad in ('{"a":1,"a":2}','{"a":NaN}','{"a":Infinity}'):
                p.write_text(bad)
                with self.assertRaises(ValueError):c.read_json(p)

    def test_interval_guards(self):
        m=c.certificate_module()
        with self.assertRaises(ValueError):m.I(-1,1).sqrt()
        with self.assertRaises(ValueError):m.I(1)/m.I(-1,1)
        self.assertTrue(m.I(Q(2)).sqrt().lo**2<=2*m.S*m.S<=m.I(Q(2)).sqrt().hi**2)
        self.assertGreater(m.I(Q(1,10)).exp().lo,m.S)

    def test_center_tail_and_rouche_fields(self):
        r=c.read_json(ROOT/'results.json')
        self.assertEqual(r['N'],5);self.assertEqual(r['panels'],785)
        self.assertTrue(Q(r['rouche_margin_lower'])>Q(3,10**22))
        self.assertTrue(Q(r['residual_upper'])<Q(15,10**28))
        self.assertTrue(Q(r['derivative_lower'])>Q(3,10**10))
        self.assertTrue(Q(r['center'][1])-Q(r['radius'])>0)
        self.assertTrue(Q(r['center'][1])+Q(r['radius'])<Q(1,2))
        self.assertIs(r['zero_of_xi_claimed'],False)

    def test_actual_cli_refusals(self):
        """Pristine quick acceptance, then 12 distinct changed-copy subprocesses."""
        with tempfile.TemporaryDirectory() as d:
            base=Path(d)/'packet';shutil.copytree(ROOT,base)
            good=command(base,'--quick')
            self.assertEqual(good.returncode,0,good.stderr)
            self.assertIn('NO_ZERO_REPLAY',good.stdout)
            for case in ('false_rh','float_n','boolean_n','duplicate_receipt',
                         'changed_coverage','wrong_source_rate','changed_parent',
                         'changed_interval','unsealed_proof','extra_file',
                         'missing_file','symlink'):
                folder=Path(d)/case;shutil.copytree(ROOT,folder)
                if case in ('false_rh','float_n','boolean_n','duplicate_receipt'):
                    r=c.read_json(folder/'results.json')
                    if case=='false_rh':r['rh_proved']=True
                    if case=='float_n':r['N']=5.0
                    if case=='boolean_n':r['N']=True
                    text=json.dumps(r,sort_keys=True)
                    if case=='duplicate_receipt':text=text[:-1]+',"N":5}'
                    (folder/'results.json').write_text(text);reseal(folder)
                    args=('--check',str(folder/'results.json'))
                else:
                    args=('--quick',)
                    if case=='changed_coverage':
                        r=c.read_json(folder/'bounded.json');r['partition_cells']=784
                        (folder/'bounded.json').write_text(json.dumps(r));reseal(folder)
                    if case=='wrong_source_rate':
                        f=folder/'certificate.py';s=f.read_text();s=s.replace('tuple(Q(k*k) for k in range(1,N+1))','tuple(Q(k*k+1) for k in range(1,N+1))',1)
                        f.write_text(s);reseal(folder)
                    if case=='changed_parent':
                        f=folder/'SOURCE_LOCK.json';r=c.read_json(f);r['parent_commit']='0'*40
                        f.write_text(json.dumps(r));reseal(folder)
                    if case=='changed_interval':
                        f=folder/'interval.py';f.write_text(f.read_text()+'\n# changed inherited primitive\n');reseal(folder)
                    if case=='unsealed_proof':
                        f=folder/'PROOF.md';f.write_text(f.read_text()+'\nChanged.\n')
                    if case=='extra_file':(folder/'unlisted').write_text('extra')
                    if case=='missing_file':(folder/'CERTIFICATE.md').unlink()
                    if case=='symlink':
                        f=folder/'PROOF.md';target=Path(d)/'proof-copy';shutil.copyfile(f,target);f.unlink();f.symlink_to(target)
                result=command(folder,*args)
                self.assertNotEqual(result.returncode,0,case+' incorrectly accepted')
                self.assertIn('FAIL_GAMMA_ENDPOINT_PACKET',result.stderr,case)
                REFUSALS.append(case)


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    report={'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
            'skipped':len(result.skipped),'actual_cli_refusals':REFUSALS,
            'full_integral_replayed_by_this_suite':False}
    print(json.dumps(report,sort_keys=True))
    sys.exit(0 if result.wasSuccessful() else 1)
