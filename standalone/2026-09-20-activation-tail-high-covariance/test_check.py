#!/usr/bin/env python3
"""Bounded adversarial controls for ATC29; not verification of asymptotic proofs."""
from __future__ import annotations
import copy
from fractions import Fraction as F
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('atc29_check', ROOT/'check.py')
if spec is None or spec.loader is None:
    raise RuntimeError('cannot load checker')
a=importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)
n=a.n


def iv(obj):
    return int(obj['lower']),int(obj['upper'])


class ATC29Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p31=a.complete_panel(31)
        cls.p95=a.complete_panel(95)

    def test_01_primitive_identity_and_mutation(self):
        p=ROOT/'ncg28_primitives.py'
        self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),a.PRIMITIVE_SHA256)
        with tempfile.TemporaryDirectory() as td:
            changed=Path(td)/'primitives.py'
            changed.write_bytes(p.read_bytes()+b'\n# alteration\n')
            with self.assertRaises(ValueError):a.load_primitives(changed)

    def test_02_symlink_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            link=Path(td)/'primitives.py'
            try:link.symlink_to(ROOT/'ncg28_primitives.py')
            except (OSError,NotImplementedError):
                self.skipTest('host does not permit symlink creation')
            with self.assertRaises(ValueError):a.load_primitives(link)

    def test_03_exact_interval_arithmetic(self):
        vals=[F(-7,3),F(-1,11),F(),F(2,7),F(13,5)]
        for x in vals:
            for y in vals:
                self.assertTrue(n.contains(n.add(n.rational(x),n.rational(y)),x+y))
                self.assertTrue(n.contains(n.mul(n.rational(x),n.rational(y)),x*y))
            self.assertTrue(n.contains(n.square(n.rational(x)),x*x))
            self.assertTrue(n.contains(a.divide(n.rational(x),17),x/17))
        self.assertEqual(n.square((-n.SCALE,2*n.SCALE)),(0,4*n.SCALE))
        for v in [0,-1,True]:
            with self.assertRaises(ValueError):a.divide(n.ZERO,v)

    def test_04_all_cyclic_sums_and_variances(self):
        report=a.period_checks(16)
        self.assertEqual(report['periods'],15)
        self.assertEqual(report['full_tail_cases'],90)
        self.assertEqual(report['cyclic_partial_sums'],sum(q*q for q in range(2,17)))

    def test_05_infinite_tail_against_finite_partial_sums(self):
        # The unexplored tail after N is separately enclosed by the proved
        # periodic partial-sum bound, not treated as zero.
        for q in [2,4,6,9,15]:
            for K in [1,7,2*q+1]:
                N=K+20*q
                partial=sum((n.R(q,k)/F(k*(k+1)) for k in range(K,N+1)),F())
                H,_=n.harmonics(K-1,set())
                z=n.sumiv(n.times(H[(K-1)//d],n.mobius_trial(q//d)) for d in n.divisors(q))
                if n.pp_base(q):z=n.add(z,n.log_iv(n.pp_base(q)))
                whole=n.sub(n.rational(n.R(q,K-1)/K),z)
                rem=F(q*q,2*(N+1)*(N+2))
                self.assertTrue(n.overlap(whole,(n.rational(partial-rem)[0],n.rational(partial+rem)[1])))

    def test_06_native_semiprime_coefficients(self):
        c,_=n.completion(31)
        amps,U,_,_=n.amplitudes(c)
        for p,r in [(29,31)]:
            direct=sum((c[i]*c[j]/(i*j) for i in range(1,len(c))
                        for j in range(1,len(c)) if (i*j)%(p*r)==0),F())
            self.assertEqual(direct,F(2,p*r))
            self.assertEqual(amps[p*r],direct)
            self.assertEqual(U[p],F(-1,p))
        self.assertNotEqual(amps[29*29],F(2,29*29))

    def test_07_exact_semiprime_kernel_and_prime_square_control(self):
        H=[F()]
        for k in range(1,80):H.append(H[-1]+F(1,k))
        p,r=29,31
        for k in range(32,39):
            z=sum((n.mobius_trial(p*r//d)*H[k//d] for d in n.divisors(p*r)),F())
            self.assertEqual(z,H[k]-2)
        p=5;k=30
        harmonic=sum((n.mobius_trial(p*p//d)*H[k//d] for d in n.divisors(p*p)),F())
        z=n.add(n.rational(harmonic),n.log_iv(p))
        self.assertFalse(n.overlap(z,n.rational(harmonic)))

    def test_08_integer_schedule_and_activation(self):
        for Y in [2,7,31,95,127]:
            b=Y+1
            for q in [2,4,17,Y*Y]:
                X=b
                while q**11>Y**4*X**6:X*=2
                self.assertLessEqual(q**11,Y**4*X**6)
                if X>b:self.assertGreater(q**11,Y**4*(X//2)**6)
                Q=n.root(Y**4*X**6,11)
                self.assertLessEqual(Q**11,Y**4*X**6)
                self.assertGreater((Q+1)**11,Y**4*X**6)

    def test_09_nonzero_correction_and_complete_tail_budget(self):
        for p in [self.p31,self.p95]:
            self.assertFalse(n.contains(iv(p['correction_blocks'][0]['correction']),0))
            energy=iv(p['correction_entire_future_energy'])
            bound=iv(p['correction_entire_future_finite_envelope'])
            self.assertGreater(energy[0],0)
            self.assertLess(energy[1],bound[0])
            self.assertEqual(p['zero_correction_from'],2*p['correction_blocks'][-1]['X'])
            self.assertEqual(p['native_cells'],p['last']-p['Y'])

    def test_10_native_covariance_not_always_negative(self):
        self.assertEqual(self.p31['covariance_sign'],'negative')
        self.assertEqual(self.p95['covariance_sign'],'positive')
        self.assertGreater(iv(self.p95['energy']['twice_covariance'])[0],0)
        for p in [self.p31,self.p95]:
            e=p['energy']
            total=n.sumiv(iv(e[k]) for k in ['semiprime','other_high','twice_covariance'])
            self.assertTrue(n.overlap(total,iv(e['instantaneous_high'])))

    def test_11_large_local_source_first_reconstruction(self):
        p=a.large_band(255)
        self.assertEqual(p['independent_local_Newton_coefficients'],318)
        self.assertEqual(p['native_cells'],63)
        self.assertIn('ALL other',p['scope'])
        e=p['energy']
        self.assertTrue(n.overlap(iv(e['total_Q']),n.sumiv(iv(e[k]) for k in ['semiprime','full_other_modes','twice_covariance'])))

    def test_12_strict_report_types_coverage_and_correction(self):
        p=self.p31
        changes=[]
        x=copy.deepcopy(p);x['Y']=True;changes.append(x)
        x=copy.deepcopy(p);x['native_cells']+=1;changes.append(x)
        x=copy.deepcopy(p);x['correction_blocks'][0]['correction']['lower']='0';changes.append(x)
        x=copy.deepcopy(p);x['energy']['twice_covariance']['upper']='0';changes.append(x)
        for changed in changes:self.assertFalse(n.same_types(changed,p))
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'duplicate.json';path.write_text('{"x":1,"x":2}')
            with self.assertRaises(ValueError):n.read_json(path)

    def test_13_input_ranges(self):
        for bad in [0,1,30,128,True]:
            with self.assertRaises(ValueError):a.complete_panel(bad)
        for bad in [0,127,131072,True]:
            with self.assertRaises(ValueError):a.large_band(bad)

    def test_14_actual_cli_acceptance_and_changed_report_refusal(self):
        flags=['-O'] if sys.flags.optimize else []
        cmd=[sys.executable,*flags,'-S','-B',str(ROOT/'check.py'),'--quick']
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'quick.json'
            write=subprocess.run(cmd+['--write',str(path)],capture_output=True,text=True,timeout=120)
            self.assertEqual(write.returncode,0,write.stderr)
            good=subprocess.run(cmd+['--check',str(path)],capture_output=True,text=True,timeout=120)
            self.assertEqual(good.returncode,0,good.stderr)
            data=n.read_json(path)
            self.assertEqual(data['campaign'],'quick')
            data['complete_panels'][0]['native_cells']+=1
            path.write_bytes(n.canonical(data))
            bad=subprocess.run(cmd+['--check',str(path)],capture_output=True,text=True,timeout=120)
            self.assertNotEqual(bad.returncode,0)
            self.assertIn('report differs',bad.stderr)


if __name__=='__main__':unittest.main(verbosity=2)
