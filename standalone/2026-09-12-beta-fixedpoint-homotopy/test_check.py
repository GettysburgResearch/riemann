#!/usr/bin/env python3
"""Portable bounded regressions; actual subprocess acceptance/refusal tests."""
from __future__ import annotations
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bfc_exact',ROOT/'check.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def reseal(root):
    entries=[]
    for name in sorted(mod.FILES-{'SHA256SUMS'}):
        entries.append(hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name)
    (root/'SHA256SUMS').write_text('\n'.join(entries)+'\n',encoding='ascii')


def command(root):
    args=[sys.executable,'-I','-S','-B']
    if sys.flags.optimize:
        args.append('-O')
    return args+[str(root/'check.py'),'--check',str(root/'result.json')]


class BFCChecks(unittest.TestCase):
    def test_scale_source(self):
        for j in range(15):
            self.assertGreater(mod.beta_moment(j),0)
            self.assertGreater(mod.uniform_moment(j),0)
        self.assertEqual(mod.scale_moment(F(1,2),2),F(7,24))
        self.assertEqual(mod.peano_moment(0),F(1,960))

    def test_fixed_moment_and_response_routes(self):
        for theta in mod.PARAMETERS:
            m,dm=mod.fixed_moments(theta,14)
            q=mod.response_moments(theta,m,11)
            for j in range(12):
                self.assertEqual(q[j],dm[j+3]/((j+1)*(j+2)*(j+3)))
        m,_=mod.fixed_moments(F(1),14)
        self.assertEqual(m,mod.brownian_moments(14))

    def test_metric_and_geometric_remainder(self):
        for a,b in ((F(0),F(1)),(F(1,4),F(3,4)),(F(1,10),F(9,10))):
            c=(a+b)/2
            self.assertEqual(mod.distance(a,b),mod.distance(a,c)+mod.distance(c,b))
        self.assertEqual(mod.distance(F(0),F(1)),F(4,175))
        for theta in mod.PARAMETERS:
            r=2*mod.scale_moment(theta,3)
            a=mod.chi(theta)*(1-r)
            for J in range(10):
                partial=sum((a*r**j for j in range(J+1)),F(0))
                self.assertEqual(mod.chi(theta)-partial,mod.chi(theta)*r**(J+1))

    def test_fold_conventions(self):
        for c in (F(1,7),F(3,8)):
            for a,q in ((F(2),F(3)),(F(-2),F(3)),(F(2),F(-3))):
                self.assertEqual(mod.collision_speed(c,a,q),-2*(4*c*a)/(-q/2))
        for d in (F(-1,8),F(-1,16),F(-1,100),F(0),F(1,100),F(1,16),F(1,8)):
            # Remove the common positive exponential from the quartet weight.
            full=4*(-d)*(F(1,4)+d) if d < 0 else F(0)
            self.assertEqual(full,max(F(0),-d)*(1+4*d))
        with self.assertRaises(ValueError):
            mod.collision_speed(F(1),F(1),F(0))

    def test_reconstruction_and_inventory(self):
        mod.authenticate(ROOT)
        mod.same_typed(mod.load_strict(ROOT/'result.json'),mod.reconstruct())

    def test_actual_cli_rejections(self):
        cases=('false_rh','boolean_alias','float_alias','wrong_contraction',
               'wrong_response','wrong_fold_receipt','duplicate_json',
               'producer_fold','producer_response','extra_file','proof_drift',
               'duplicate_manifest')
        completed=0
        with tempfile.TemporaryDirectory(prefix='bfc26-tests-') as tmp:
            pristine=Path(tmp)/'pristine'
            shutil.copytree(ROOT,pristine)
            p=subprocess.run(command(pristine),capture_output=True,text=True,timeout=20)
            self.assertEqual(p.returncode,0,p.stdout+p.stderr)
            self.assertIn('PASS_BFC26_BOUNDED',p.stdout)
            for case in cases:
                root=Path(tmp)/case
                shutil.copytree(ROOT,root)
                record=mod.load_strict(root/'result.json')
                if case=='false_rh': record['status']['rh_proved']=True
                elif case=='boolean_alias': record['scope']['moment_order']=True
                elif case=='float_alias': record['scope']['moment_order']=14.0
                elif case=='wrong_contraction': record['constants']['max_response_contraction']='31/79'
                elif case=='wrong_response': record['fixed_point_panels'][3]['response_measure_moments'][0]='1/1'
                elif case=='wrong_fold_receipt': record['synthetic_fold_panels'][0][3]='0/1'
                if case in cases[:6]:
                    record.pop('semantic_sha256')
                    record['semantic_sha256']=mod.digest_obj(record)
                    (root/'result.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n',encoding='utf-8')
                    reseal(root)
                elif case=='duplicate_json':
                    text=(root/'result.json').read_text()
                    (root/'result.json').write_text('{"schema":"duplicate",'+text[1:],encoding='utf-8')
                    reseal(root)
                elif case=='producer_fold':
                    text=(root/'check.py').read_text()
                    old='return 16*c*a/q'
                    self.assertEqual(text.count(old),1)
                    (root/'check.py').write_text(text.replace(old,'return 8*c*a/q'),encoding='utf-8')
                    reseal(root)
                elif case=='producer_response':
                    text=(root/'check.py').read_text()
                    old='(born+2*a*lower)/(1-2*a)'
                    self.assertEqual(text.count(old),1)
                    (root/'check.py').write_text(text.replace(old,'(born+3*a*lower)/(1-2*a)'),encoding='utf-8')
                    reseal(root)
                elif case=='extra_file': (root/'unexpected.txt').write_text('not allowed\n')
                elif case=='proof_drift':
                    with (root/'PROOF.md').open('a',encoding='utf-8') as f:f.write('\nUnsealed alteration.\n')
                elif case=='duplicate_manifest':
                    text=(root/'SHA256SUMS').read_text()
                    (root/'SHA256SUMS').write_text(text+text.splitlines()[0]+'\n',encoding='ascii')
                p=subprocess.run(command(root),capture_output=True,text=True,timeout=20)
                self.assertNotEqual(p.returncode,0,case+' incorrectly accepted')
                self.assertNotIn('PASS_BFC26_BOUNDED',p.stdout,case)
                completed+=1
        self.assertEqual(completed,len(cases))
        print('CLI_EVIDENCE pristine_acceptances=1 executed_refusals='+str(completed))


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(BFCChecks)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)
