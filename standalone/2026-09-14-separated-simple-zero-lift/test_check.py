#!/usr/bin/env python3
"""Bounded SPL26 tests and actual copied-package CLI refusals."""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as Q

sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('spl_exact',ROOT/'check.py')
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)
OPTIMIZED=False
REFUSALS=0
ACCEPTANCES=0


def reseal(path: Path):
    lines=[]
    for p in sorted(path.iterdir()):
        if p.name!='SHA256SUMS' and p.is_file():
            lines.append(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.name)
    (path/'SHA256SUMS').write_text('\n'.join(lines)+'\n',encoding='utf-8')


def command(path: Path):
    flags=['-I','-S','-B']+(['-O'] if OPTIMIZED else [])
    return subprocess.run([sys.executable,*flags,str(path/'check.py'),'--check',str(path/'result.json')],
                          capture_output=True,text=True,timeout=60)


class ExactTests(unittest.TestCase):
    def test_full_reconstruction(self):
        c.authenticate()
        self.assertTrue(c.same(c.reconstruct(),c.load_json(ROOT/'result.json')))

    def test_threshold_and_repetitions(self):
        ys,pairs=c.greedy([Q(0),Q(0),Q(2,3),Q(4,3),Q(3,2)])
        self.assertEqual(pairs,[(0,1),(3,4)])
        self.assertEqual(ys,[2])
        ys,pairs=c.greedy([Q(0),Q(2,3),Q(4,3)])
        self.assertEqual(ys,[0,1,2]); self.assertEqual(pairs,[])
        self.assertEqual(c.greedy([]),([],[]))

    def test_independent_series_and_scalar_minimum(self):
        h50,_=c.trig_constant_bounds(50)
        h62,_=c.trig_constant_bounds(62)
        self.assertLessEqual(h50[0],h62[0]); self.assertGreaterEqual(h50[1],h62[1])
        for p in [Q(j,8) for j in range(81)]:
            n=max(Q(0),p-2)
            self.assertEqual((p-n)**2+4*n,2*p-1+c.psi(p))
            for other in [Q(0),n/2,n,n+Q(1,3),n+2]:
                self.assertGreaterEqual((p-other)**2+4*other,2*p-1+c.psi(p))

    def test_typed_parser(self):
        self.assertFalse(c.same(True,1))
        self.assertFalse(c.same(['1/2'],[Q(1,2)]))
        with self.assertRaises(ValueError): c.no_duplicate([('x',1),('x',2)])

    def test_actual_cli_refusals(self):
        global REFUSALS,ACCEPTANCES
        with tempfile.TemporaryDirectory(prefix='spl26-tests-') as td:
            dest=Path(td)/'packet';shutil.copytree(ROOT,dest)
            pristine={p.name:p.read_bytes() for p in dest.iterdir()}
            run=command(dest)
            self.assertEqual(run.returncode,0,run.stderr);ACCEPTANCES+=1
            cases=['simple_endpoint','pair_price','majorant_minimum','rh_status','support',
                   'boolean_alias','duplicate_key','proof_drift','extra_file','producer_change']
            for case in cases:
                for p in dest.iterdir():p.unlink()
                for name,data in pristine.items():(dest/name).write_bytes(data)
                data=json.loads((dest/'result.json').read_text('utf-8'))
                if case=='simple_endpoint':data['constants']['new_simple'][0]='0.674'
                elif case=='pair_price':data['pair']['price']='0/1'
                elif case=='majorant_minimum':data['majorant']['minimum']='-1/1'
                elif case=='rh_status':data['status']['rh_proved']=True
                elif case=='support':data['majorant']['support_radius']='1/1'
                elif case=='boolean_alias':data['coverage']['adapter_constant_cases']=True
                elif case=='duplicate_key':
                    text=(dest/'result.json').read_text('utf-8')
                    text=text.replace('"schema": "SPL26-bounded-v1",',
                                      '"schema": "SPL26-bounded-v1", "schema": "duplicate",')
                    (dest/'result.json').write_text(text,'utf-8');reseal(dest)
                elif case=='proof_drift':
                    with (dest/'PROOF.md').open('a',encoding='utf-8') as f:f.write('\nunsealed change\n')
                elif case=='extra_file':(dest/'unexpected.txt').write_text('extra','utf-8')
                elif case=='producer_change':
                    text=(dest/'check.py').read_text('utf-8').replace('SEPARATION = Q(2, 3)','SEPARATION = Q(3, 4)')
                    (dest/'check.py').write_text(text,'utf-8');reseal(dest)
                if case in cases[:6]:
                    (dest/'result.json').write_text(json.dumps(data,sort_keys=True,indent=2)+'\n','utf-8')
                    reseal(dest)
                run=command(dest)
                self.assertNotEqual(run.returncode,0,case+': accepted altered input')
                self.assertIn('REFUSE:',run.stderr,case+': failed without controlled refusal')
                REFUSALS+=1

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--optimized',action='store_true')
    a=ap.parse_args();OPTIMIZED=a.optimized
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ExactTests))
    print(f'ACTUAL_CLI_ACCEPTANCES={ACCEPTANCES} ACTUAL_CLI_REFUSALS={REFUSALS}')
    sys.exit(0 if result.wasSuccessful() else 1)
