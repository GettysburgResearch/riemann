"""Bounded independent controls and real accepting/refusing CLI executions."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb, isqrt
import contextlib
import copy
import hashlib
import importlib.util
import io
import itertools
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).absolute().parent

def module(name,file):
    spec=importlib.util.spec_from_file_location(name,ROOT/file)
    out=importlib.util.module_from_spec(spec);spec.loader.exec_module(out);return out
V=module('_verify_test','verify.py');C=module('_cert_test','certificate.py');D=C._mod

def reseal(root):
    names=sorted(V.FILES-{'SHA256SUMS'})
    (root/'SHA256SUMS').write_text(''.join(hashlib.sha256((root/n).read_bytes()).hexdigest()+'  '+n+'\n' for n in names))

def cli(root,receipt):
    args=[sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])
    return subprocess.run(args+[str(root/'verify.py'),'--check',str(receipt)],cwd=root,
                          stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=240)

class Checks(unittest.TestCase):
    def test_interval_rational_and_sqrt(self):
        values=[Q(i,j) for i in (-7,-2,1,3,8) for j in (1,3,11)]
        def contains(a,x):
            self.assertLessEqual(Q(a.lo,D.S),x);self.assertGreaterEqual(Q(a.hi,D.S),x)
        for x,y in itertools.product(values,repeat=2):
            contains(D.I(x)+D.I(y),x+y);contains(D.I(x)*D.I(y),x*y)
            contains(D.I(x)/D.I(y),x/y)
        for x in (Q(0),Q(1,7),Q(2),Q(49,4)):
            a=D.I(x).sqrt();self.assertLessEqual(Q(a.lo,D.S)**2,x);self.assertGreaterEqual(Q(a.hi,D.S)**2,x)
        with self.assertRaises(ValueError):D.I(1)/D.I(-1,1)
        with self.assertRaises(ValueError):D.I(-1).sqrt()

    def test_elementary_primitives_and_constants(self):
        low=sum((Q(1,factorial(k)) for k in range(241)),Q(0))
        high=low+Q(2,factorial(241));en=D.I(1).exp()
        self.assertLessEqual(Q(en.lo,D.S),high);self.assertGreaterEqual(Q(en.hi,D.S),low)
        self.assertGreater(sum((Q(4**k,factorial(k)) for k in range(17)),Q(0)),54)
        self.assertGreater(D.PI.lo,D.I(Q(31,10)).hi);self.assertLess(D.PI.hi,D.I(Q(22,7)).lo)
        for x in (Q(-10),Q(-1,7),Q(0),Q(1,3),Q(9)):
            s,c=D.sincos(D.I(x));unit=s*s+c*c
            self.assertLessEqual(unit.lo,D.S);self.assertGreaterEqual(unit.hi,D.S)
            product=D.I(x).exp()*D.I(-x).exp()
            self.assertLessEqual(product.lo,D.S);self.assertGreaterEqual(product.hi,D.S)

    def test_gamma_laplace_source(self):
        for _,rates,_,_ in C.CASES:
            for q in (Q(0),Q(1,5),Q(1),Q(7),Q(31,3)):
                direct=Q(1)
                for a in rates:direct*=(a/(q+a))**2
                partial=sum((b/(q+a)**2+b*c/(q+a) for a,b,c in C.rows(rates)),Q(0))
                self.assertEqual(direct,partial)
            C.analytic_guards(rates)
        self.assertEqual(C.CELLS*2*C.DELTA,2)
        self.assertEqual(Q(1,8),C.DELTA/Q(1,32))
        self.assertLess(C.tail_bound().hi,D.I(Q(1,2**105)).lo)

    def test_complete_bonferroni_coefficients(self):
        for N in range(1,7):
            aa=[Q(1,n*n) for n in range(N+1,N+5) for _ in range(2)]
            tau=sum(aa);v=sum(x*x for x in aa);w=sum(x**3 for x in aa)
            coeff=[Q(1)]+[Q(0)]*12
            for a in aa:
                for k in range(12,0,-1):coeff[k]+=a*coeff[k-1]
            for k in range(13):
                pair=v*tau**(k-2)/2/factorial(k-2) if k>=2 else 0
                d=coeff[k]-tau**k/factorial(k)+pair
                bound=(w*tau**(k-3)/2/factorial(k-3) if k>=3 else 0)+(v*v*tau**(k-4)/8/factorial(k-4) if k>=4 else 0)
                self.assertGreaterEqual(d,0);self.assertLessEqual(d,bound)

    def test_spectral_difference_algebra(self):
        for q in [Q(i,3) for i in range(-15,16)]:
            self.assertEqual((q+4)**2-7*(q+4)+Q(45,4),q*q+q-Q(3,4))
            self.assertEqual((q-4)**2+7*(q-4)+Q(45,4),q*q-q-Q(3,4))
        # Moment generating coefficient: e2=(tau^2-v)/2, not tau^2/2.
        self.assertEqual(Q(1,2)**2+Q(1,3)**2,Q(13,36))
        self.assertFalse(V.typed_equal({'a':1},{'a':True}))
        for raw in ('{"a":1,"a":2}','{"a":1.0}','{"a":NaN}'):
            with self.assertRaises(ValueError):V.strict_json(raw)

    def test_real_cli_acceptance_and_refusals(self):
        original=(ROOT/'results.json').read_bytes();data=json.loads(original)
        with tempfile.TemporaryDirectory(prefix='gamma-test-') as temp:
            temp=Path(temp);packet=temp/'packet';shutil.copytree(ROOT,packet)
            ok=cli(packet,packet/'results.json')
            self.assertEqual(ok.returncode,0,ok.stderr)
            self.assertEqual(ok.stdout.strip(),'PASS_COMPLETE_TWO_DISK_RECONSTRUCTION')
            refused=0
            alterations=[]
            x=copy.deepcopy(data);x['rh_proved']=True;alterations.append(x)
            x=copy.deepcopy(data);x['bits']=True;alterations.append(x)
            x=copy.deepcopy(data);x['cells_per_case']=255;alterations.append(x)
            x=copy.deepcopy(data);x['cases']=x['cases'][:1];alterations.append(x)
            x=copy.deepcopy(data);x['cases'][1]['disk_inside_xi_critical_band']=False;alterations.append(x)
            x=copy.deepcopy(data);x['cases'][0]['radius']='1/1000';alterations.append(x)
            # This last change passes metadata and forces a complete fresh integral replay.
            x=copy.deepcopy(data);x['cases'][0]['integral_jets'][0][0][0]=str(int(x['cases'][0]['integral_jets'][0][0][0])+1);alterations.append(x)
            for j,x in enumerate(alterations):
                p=temp/('bad-%d.json'%j);p.write_text(json.dumps(x))
                done=cli(packet,p);self.assertNotEqual(done.returncode,0,done.stdout);refused+=1
            for j,raw in enumerate((b'{"rh_proved":false,"rh_proved":false}',original.replace(b'"bits": 512',b'"bits": 512.0'))):
                p=temp/('syntax-%d.json'%j);p.write_bytes(raw)
                done=cli(packet,p);self.assertNotEqual(done.returncode,0,done.stdout);refused+=1
            (packet/'EXTRA').write_text('uncovered')
            self.assertNotEqual(cli(packet,packet/'results.json').returncode,0);refused+=1
            (packet/'EXTRA').unlink()
            p=packet/'PROOF.md';keep=p.read_bytes();p.write_bytes(keep+b'changed\n')
            self.assertNotEqual(cli(packet,packet/'results.json').returncode,0);refused+=1
            p.write_bytes(keep)
            external=temp/'proof-copy';external.write_bytes(keep);p.unlink();p.symlink_to(external)
            self.assertNotEqual(cli(packet,packet/'results.json').returncode,0);refused+=1
            p.unlink();p.write_bytes(keep)
            # Resealed producer sign/scale defect fails an independent transform identity.
            source=packet/'certificate.py';keep=source.read_bytes()
            changed=keep.replace(b'out.append((a,a*a*B,-2*ss))',b'out.append((a,a*a*B,-ss))')
            self.assertNotEqual(changed,keep);source.write_bytes(changed);reseal(packet)
            bad=cli(packet,packet/'results.json')
            self.assertNotEqual(bad.returncode,0)
            self.assertIn('independent gamma transform control',bad.stderr);refused+=1
            source.write_bytes(keep);reseal(packet)
            self.assertEqual(refused,13)

if __name__=='__main__':
    stream=io.StringIO();result=unittest.TextTestRunner(stream=stream,verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
    if not result.wasSuccessful():
        print(stream.getvalue(),file=sys.stderr);sys.exit(1)
    print(json.dumps({'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),'pristine_full_cli_replays':1,'actual_cli_refusals':13},sort_keys=True))
