"""Finite controls and real accepting/refusing CLI executions; not an RH proof."""
from __future__ import annotations
from fractions import Fraction as Q
import copy
import json
from math import factorial
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from interval import I,S,PI,sincos,exp_series,sqrt_series,mul
from certificate import rows,verify_analytic
from check import decode,equal
COUNTS={'rational_interval_cases':0,'finite_density_cases':0,
        'elementary_symmetric_cases':0,'cli_pristine':0,'cli_refusals':0,
        'copied_source_refusals':0}

def run_cli(root, receipt):
    return subprocess.run([sys.executable,'-I','-S','-B',
        *(['-O'] if sys.flags.optimize else []),str(root/'check.py'),
        '--expect',str(receipt)],capture_output=True,text=True)

class Tests(unittest.TestCase):
    def contains(self, interval, value):
        value=Q(value)
        self.assertLessEqual(Q(interval.lo,S),value)
        self.assertGreaterEqual(Q(interval.hi,S),value)

    def test_rational_arithmetic(self):
        for a in range(-9,10):
            for b in range(1,10):
                x,y=Q(a,13),Q(b,17)
                self.contains(I(x)+I(y),x+y)
                self.contains(I(x)*I(y),x*y)
                self.contains(I(x)/I(y),x/y)
                COUNTS['rational_interval_cases']+=1
        for n in range(1,65):
            r=I(Q(n,7)).sqrt()
            self.assertLessEqual(Q(r.lo,S)**2,Q(n,7))
            self.assertGreaterEqual(Q(r.hi,S)**2,Q(n,7))
        with self.assertRaises(ValueError):I(1)/I(-1,1)
        with self.assertRaises(ValueError):I(-1).sqrt()

    def test_primitives_and_series(self):
        self.assertGreater(Q(PI.lo,S),Q(31,10))
        self.assertLess(Q(PI.hi,S),Q(22,7))
        for n in range(-12,13):
            x=I(Q(n,7));s,c=sincos(x)
            self.contains(s*s+c*c,1)
            self.contains(x.exp()*(-x).exp(),1)
        for k in range(-6,7):
            s,c=sincos(k*PI/2)
            self.contains(s,[0,1,0,-1][k%4])
            self.contains(c,[1,0,-1,0][k%4])
        a=[I(1),I(Q(1,5))]+[I(0)]*11
        e=exp_series(a,12)
        for k in range(1,13):
            # independently verify the differential identity coefficient.
            self.assertTrue(equal((k*e[k]).pair(),(e[k-1]/5).pair()) or
                            max((k*e[k]).lo,(e[k-1]/5).lo)<=min((k*e[k]).hi,(e[k-1]/5).hi))
        q=[I(1),I(2),I(1)]+[I(0)]*10
        sq=sqrt_series(q,12)
        self.contains(sq[0],1);self.contains(sq[1],1)
        for c in sq[2:]:self.contains(c,0)

    def test_density_laplace_and_initial_jets(self):
        for rates in ([Q(1),Q(4)], [Q(1),Q(4),Q(90,7)], [Q(1),Q(4),Q(9),Q(16)]):
            rr=rows(rates);m=2*len(rates)
            for s in (Q(0),Q(1,2),Q(1),Q(2),Q(7)):
                p=Q(1)
                for a in rates:p*=(a/(s+a))**2
                partial=sum((b/(s+a)**2+b*c/(s+a) for a,b,c in rr),Q(0))
                self.assertEqual(p,partial);COUNTS['finite_density_cases']+=1
            for k in range(m):
                coeff=sum((b*(c*(-a)**k/Q(factorial(k))+
                        ((-a)**(k-1)/Q(factorial(k-1)) if k else 0)) for a,b,c in rr),Q(0))
                expected=Q(1)
                for a in rates:expected*=a*a
                expected=expected/factorial(m-1) if k==m-1 else Q(0)
                self.assertEqual(coeff,expected);COUNTS['finite_density_cases']+=1
        for rates in ([Q(1),Q(4),Q(90,7)],[Q(1),Q(4),Q(9),Q(16)]):
            verify_analytic(rates)
        with self.assertRaises(ValueError):verify_analytic([Q(1),Q(4),Q(4)])

    def test_collision_coefficient_budget(self):
        for n in range(1,7):
            for M in range(n+1,n+5):
                alpha=[Q(1,k*k) for k in range(n+1,M+1) for _ in range(2)]
                e=[Q(1)]+[Q(0)]*8
                for a in alpha:
                    for k in range(8,0,-1):e[k]+=a*e[k-1]
                tau=sum(alpha);v=sum(a*a for a in alpha)
                for k in range(2,9):
                    diff=tau**k/factorial(k)-e[k]
                    self.assertGreaterEqual(diff,0)
                    self.assertLessEqual(diff,v*tau**(k-2)/(2*factorial(k-2)))
                    COUNTS['elementary_symmetric_cases']+=1
        self.assertLess(16*16*16*10**6*Q(250,249)**3,10**10)
        self.assertLessEqual(Q(10**10,4)*Q(1,10**6)**3,Q(1,10**8))
        self.assertLess(Q(10,999),Q(1,64))

    def test_strict_reader(self):
        with self.assertRaises(ValueError):decode('{"x":1,"x":2}')
        with self.assertRaises(ValueError):decode('{"x":1.0}')
        self.assertFalse(equal({'x':1},{'x':True}))
        self.assertTrue(equal({'x':[1,'2',False]},{'x':[1,'2',False]}))

    def test_real_cli(self):
        source=json.loads((ROOT/'results.json').read_text())
        p=run_cli(ROOT,ROOT/'results.json')
        self.assertEqual(p.returncode,0,p.stderr)
        self.assertIn('PASS_GFC_TWO_COMPLETE_ROOT_CERTIFICATES',p.stdout)
        COUNTS['cli_pristine']+=1
        mutations=[]
        def change(label, fn):
            x=copy.deepcopy(source);fn(x);mutations.append((label,json.dumps(x)))
        change('false RH',lambda x:x.__setitem__('rh_proved',True))
        change('float precision',lambda x:x['zero_certificates'][0].__setitem__('bits',512.0))
        change('boolean precision',lambda x:x['zero_certificates'][0].__setitem__('bits',True))
        mutations.append(('duplicate JSON',json.dumps(source)[:-1]+',"schema":"GFC26-v1"}'))
        change('missing source',lambda x:x['zero_certificates'].pop())
        change('missing jet',lambda x:x['zero_certificates'][0]['integral_jets'].pop())
        change('wrong rate',lambda x:x['zero_certificates'][1]['rates'][-1].__setitem__(1,'8'))
        change('wrong radius',lambda x:x['zero_certificates'][0].__setitem__('radius',['1','100000']))
        change('reduced degree',lambda x:x['zero_certificates'][0].__setitem__('degree',20))
        change('wrong source label',lambda x:x['zero_certificates'][0].__setitem__('name','xi'))
        change('false numerical endpoint',lambda x:x['zero_certificates'][0]['integral_jets'][0][0].__setitem__(0,str(1<<512)))
        change('missing infinite tail',lambda x:x['zero_certificates'][1].pop('tail_error'))
        with tempfile.TemporaryDirectory() as td:
            for label, text in mutations:
                target=Path(td)/'bad.json';target.write_text(text)
                p=run_cli(ROOT,target)
                self.assertNotEqual(p.returncode,0,(label,p.stdout))
                COUNTS['cli_refusals']+=1

    def test_copied_source_boundary(self):
        with tempfile.TemporaryDirectory() as td:
            target=Path(td)/'packet';shutil.copytree(ROOT,target)
            proof=target/'PROOF.md';old=proof.read_bytes();proof.write_bytes(old+b'\nchanged\n')
            p=run_cli(target,target/'results.json');self.assertNotEqual(p.returncode,0)
            COUNTS['copied_source_refusals']+=1;proof.write_bytes(old)
            extra=target/'extra.txt';extra.write_text('extra')
            p=run_cli(target,target/'results.json');self.assertNotEqual(p.returncode,0)
            COUNTS['copied_source_refusals']+=1;extra.unlink()
            saved=Path(td)/'real-proof.md';saved.write_bytes(old);proof.unlink();proof.symlink_to(saved)
            p=run_cli(target,target/'results.json');self.assertNotEqual(p.returncode,0)
            COUNTS['copied_source_refusals']+=1

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Tests))
    if not result.wasSuccessful():sys.exit(1)
    print(json.dumps({'tests':result.testsRun,'skipped':len(result.skipped),
                      'counts':COUNTS,'rh_proved':False},sort_keys=True))
