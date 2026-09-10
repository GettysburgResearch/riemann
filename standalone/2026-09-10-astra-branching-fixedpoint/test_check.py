#!/usr/bin/env python3
"""Bounded algebra tests and real modified-package CLI refusal tests."""
from __future__ import annotations
import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('bsr_check',ROOT/'check.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)


def seal(p):
    (p/'SHA256SUMS').write_text(''.join(hashlib.sha256((p/name).read_bytes()).hexdigest()+'  '+name+'\n'
                  for name in sorted(c.FILES-{'SHA256SUMS'})))


def run(p):
    cmd=[sys.executable,'-I','-S','-B']
    if sys.flags.optimize:cmd.append('-O')
    return subprocess.run(cmd+[str(p/'check.py'),'--check',str(p/'verification.json')],
                          capture_output=True,text=True,timeout=25)


class Tests(unittest.TestCase):
    def test_fixed_moments(self):
        self.assertEqual(c.fixed_moments(20),c.sinh_moments(20))
        self.assertEqual(c.fixed_moments(4)[2:], [F(7,5),F(93,35),F(1143,175)])

    def test_quantization(self):
        laws=[[(F(1),F(1))],[(F(1,2),F(1,2)),(F(3,2),F(1,2))],
              [(F(1,4),F(2,5)),(F(3,2),F(3,5))]]
        for law in laws:
            for L in [1,2,3,5]:
                new=c.quantize(law,L)
                cost,rows=c.quantile_cost(law,new)
                self.assertGreaterEqual(cost,0)
                self.assertEqual(sum(m for i,j,m in rows),1)
                self.assertEqual(sum(x*p for x,p in new),1)
        with self.assertRaises(ValueError):c.validate_law([(F(2),F(1))])

    def test_bernstein_and_square_roots(self):
        self.assertTrue(all(v>0 for row in c.bernstein_quarters() for v in row))
        for j in range(65):
            q=F(j,37);lo,hi=c.sqrt_bounds(q)
            self.assertLessEqual(lo*lo,q);self.assertGreaterEqual(hi*hi,q)
            self.assertLessEqual(hi-lo,F(1,2**96))

    def test_real_cli_pristine_and_corruptions(self):
        scenarios=['rh','strip','bool_alias','float','duplicate','empty','wrong_moment',
                   'wrong_cost','wrong_gamma_polynomial','wrong_bin_map','source_drift',
                   'proof_bytes','missing_file','extra_file','symlink']
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'pristine';shutil.copytree(ROOT,p)
            good=run(p);self.assertEqual(good.returncode,0,good.stderr)
            self.assertIn('PASS_BSR26_BOUNDED_RECONSTRUCTION',good.stdout)
        for name in scenarios:
            with self.subTest(name=name),tempfile.TemporaryDirectory() as tmp:
                p=Path(tmp)/'packet';shutil.copytree(ROOT,p)
                result=p/'verification.json';r=json.loads(result.read_text())
                if name=='rh':r['rh_proved']=True
                elif name=='strip':r['orbit_strip_preservation_proved']=True
                elif name=='bool_alias':r['coverage']['quantization_transitions']=True
                elif name=='wrong_moment':r['fixed_moments_0_to_12'][2]=[8,5]
                elif name=='wrong_cost':r['quantized_laws'][0]['discrete_W2_squared']=[2,9]
                if name in ['rh','strip','bool_alias','wrong_moment','wrong_cost']:
                    result.write_text(json.dumps(r));seal(p)
                elif name=='float':
                    result.write_text(result.read_text().replace('"largest_finite_support": 350','"largest_finite_support": 350.0'));seal(p)
                elif name=='duplicate':
                    result.write_text(result.read_text().replace('{','{"rh_proved":false,',1));seal(p)
                elif name=='empty':result.write_text('{}');seal(p)
                elif name=='wrong_gamma_polynomial':
                    q=p/'check.py';s=q.read_text();self.assertIn('F(23,48)',s)
                    q.write_text(s.replace('F(23,48)','F(22,48)',1));seal(p)
                elif name=='wrong_bin_map':
                    q=p/'check.py';s=q.read_text();self.assertIn('out[(x+y)/(lo*hi)]',s)
                    q.write_text(s.replace('out[(x+y)/(lo*hi)]','out[(x+y)/(lo+hi)]',1));seal(p)
                elif name=='source_drift':
                    q=p/'SOURCES.json';s=json.loads(q.read_text());s['base']='0'*40;q.write_text(json.dumps(s));seal(p)
                elif name=='proof_bytes':
                    q=p/'PROPOSAL.md';q.write_text(q.read_text()+'\nchanged\n')
                elif name=='missing_file':(p/'README.md').unlink()
                elif name=='extra_file':(p/'extra.txt').write_text('extra')
                elif name=='symlink':
                    target=Path(tmp)/'outside.json';shutil.copyfile(result,target);result.unlink();result.symlink_to(target)
                bad=run(p)
                self.assertNotEqual(bad.returncode,0,name+' wrongly accepted')
                self.assertNotIn('PASS_BSR26',bad.stdout)
                self.assertIn('REJECT',bad.stderr)
        print('PASS_REAL_CLI: 1 pristine + 15 distinct refusal cases; optimized='+str(bool(sys.flags.optimize)))


if __name__=='__main__':
    unittest.main(verbosity=2)
