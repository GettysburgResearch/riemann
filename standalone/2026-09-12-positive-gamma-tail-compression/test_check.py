#!/usr/bin/env python3
"""Packet/CLI controls; successful tests do not certify the written analysis."""
from __future__ import annotations
import contextlib
from fractions import Fraction as Q
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('rgtcheck',ROOT/'check.py')
c=importlib.util.module_from_spec(spec);sys.modules[spec.name]=c;spec.loader.exec_module(c)
EXECUTED={'pristine_cli':0,'actual_cli_refusals':0,'symlink_refusal':False}


def seal(root):
    names=sorted(c.EXPECTED-{'SHA256SUMS'})
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n'for n in names))


def copied(root):
    for name in c.EXPECTED:shutil.copyfile(ROOT/name,root/name)


def invoke(root):
    args=[sys.executable,'-I','-S','-B']+(['-O']if sys.flags.optimize else [])
    return subprocess.run(args+[str(root/'check.py'),'--check',str(root/'result.json')],
                          cwd=root,capture_output=True,text=True,timeout=30)


class Tests(unittest.TestCase):
    def test_intervals(self):
        for a in range(-5,6):
            for b in range(1,8):
                x=Q(a,b);A=c.Iv.rounded(x,x)
                self.assertTrue(A.contains(x))
                self.assertTrue((A*A).contains(x*x))
                self.assertTrue((A+c.Iv.at(Q(1,3))).contains(x+Q(1,3)))
                if a:self.assertTrue(A.inv().contains(1/x))
        for n in range(40):
            x=Q(n,7);s=c.Iv.at(x).sqrt()
            self.assertLessEqual(s.lo*s.lo,x);self.assertGreaterEqual(s.hi*s.hi,x)
        with self.assertRaises(ValueError):c.Iv(Q(-1),Q(1)).inv()

    def test_remainder_origin_and_order(self):
        nodes=[Q(1,2),Q(1,5),Q(1,9)];weights=[Q(2),Q(3),Q(5)]
        m=[sum(w*x**k for x,w in zip(nodes,weights))for k in range(9)]
        for r in [0,1,2]:
            p,num,den,E=c.radau_from_moments(m,r)
            self.assertGreater(E,0)
            seq=c.quotient_series(num,den,2*r+3)
            self.assertEqual(seq[:2*r+1],[(-1)**k*m[k]for k in range(2*r+1)])
            self.assertEqual(m[2*r+1]+seq[2*r+1],E)
        with self.assertRaises(ValueError):c.radau_from_moments([Q(1)],2)

    def test_complete_tail_primitive(self):
        pi=c.pi_bound();B=c.bernoulli(14)
        self.assertEqual(B[2],Q(1,6));self.assertEqual(B[12],Q(-691,2730))
        for N in [4,16,64]:
            for j in [0,1,3]:
                a=c.tail_moment(N,j,pi,B);b=c.em_tail(N,2*j+2)
                self.assertTrue(a.overlaps(b));self.assertGreater(a.lo,0)
        # First-cumulant drift is indispensable, not a harmless centering option.
        self.assertEqual(Q(3)-Q(2)**2/Q(2),1)

    def test_typed_json(self):
        for s in ['{"x":1,"x":1}','{"x":1.0}','{"x":NaN}','{"x":Infinity}']:
            with self.assertRaises(ValueError):c.strict_load(s.encode())
        self.assertNotEqual(c.canonical({'x':False}),c.canonical({'x':0}))
        self.assertNotEqual(c.canonical({'x':True}),c.canonical({'x':1}))

    def test_gamma_composition(self):
        a=[Q(2),Q(3,7)];x=[Q(1,9),Q(2,13)]
        self.assertEqual(c.gamma_moments(a,x,20),c.product_gamma_moments(a,x,20))
        self.assertLess(51200*3*(1+409600*9),2**40)
        self.assertLess(Q(128,9),16)

    def test_actual_cli(self):
        with tempfile.TemporaryDirectory(prefix='rgt-cli-')as td:
            base=Path(td)/'good';base.mkdir();copied(base)
            good=invoke(base)
            self.assertEqual(good.returncode,0,good.stderr)
            self.assertIn('PASS_RGT26_BOUNDED_RECONSTRUCTION',good.stdout)
            EXECUTED['pristine_cli']+=1
            for i in range(11):
                p=Path(td)/str(i);p.mkdir();copied(p)
                obj=json.loads((p/'result.json').read_text())
                if i==0:obj['rh_proved']=True
                elif i==1:obj['groups']['actual_one_node']['rows'][0]['N']=2.0
                elif i==2:obj['groups']['uniform_error_bounds']['computed_large_order_nodes']=0
                elif i==3:
                    (p/'result.json').write_text('{"schema":"RGT26-1",'+(p/'result.json').read_text()[1:]);seal(p)
                elif i==4:obj['groups']['actual_one_node']['rows'].pop()
                elif i==5:obj['groups']['actual_one_node']['rows'][0]['drift']['upper']='1'
                elif i==6:obj['groups']['finite_radau']['rational_or_complex_resolvent_panels']-=1
                elif i==7:(p/'PROOF.md').write_text((p/'PROOF.md').read_text()+'\nchanged\n')
                elif i==8:(p/'extra.txt').write_text('extra')
                elif i==9:
                    text=(p/'check.py').read_text();old='rhs=s**(2*r+1)'
                    self.assertIn(old,text);(p/'check.py').write_text(text.replace(old,'rhs=s**(2*r+2)'));seal(p)
                elif i==10:
                    (p/'SHA256SUMS').write_text((p/'SHA256SUMS').read_text().splitlines()[0]+'\n')
                if i in [0,1,2,4,5,6]:
                    (p/'result.json').write_text(json.dumps(obj));seal(p)
                got=invoke(p)
                self.assertNotEqual(got.returncode,0,'incorrect acceptance case '+str(i))
                self.assertNotIn('PASS_RGT26',got.stdout)
                EXECUTED['actual_cli_refusals']+=1

    def test_symlink_cli(self):
        with tempfile.TemporaryDirectory(prefix='rgt-link-')as td:
            p=Path(td)/'packet';p.mkdir();copied(p)
            other=Path(td)/'readme';shutil.copyfile(p/'README.md',other);(p/'README.md').unlink()
            try:(p/'README.md').symlink_to(other)
            except OSError as exc:self.skipTest('host cannot create symlink: '+str(exc))
            got=invoke(p)
            self.assertNotEqual(got.returncode,0);self.assertIn('symlink',got.stderr)
            EXECUTED['actual_cli_refusals']+=1;EXECUTED['symlink_refusal']=True


if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    # Deterministic summary; retain failure tracebacks without claiming PASS on errors.
    stream=io.StringIO();r=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    record={'test_methods':r.testsRun,'failures':len(r.failures),'errors':len(r.errors),
            'skips':len(r.skipped),'completed_cli':EXECUTED,'success':r.wasSuccessful()}
    print(json.dumps(record,sort_keys=True))
    if not r.wasSuccessful():print(stream.getvalue(),file=sys.stderr)
    sys.exit(0 if r.wasSuccessful()else 1)
