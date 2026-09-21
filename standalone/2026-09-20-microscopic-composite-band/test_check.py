#!/usr/bin/env python3
"""Bounded algebra and refusal tests; not a verifier of infinite proofs."""
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import check as c
import exact as e

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.quick=c.produce(True)

    def test_01_smooth_mask(self):
        for j in range(129):
            u=F(j,128);v=1-10*u**3+15*u**4-6*u**5
            d=-30*u*u*(1-u)**2
            dd=-60*u*(1-u)*(1-2*u)
            self.assertTrue(0<=v<=1)
            self.assertLessEqual(abs(d),2);self.assertLessEqual(abs(dd),6)
            self.assertEqual(c.cutoff(1+u,1),v)
        self.assertEqual(c.cutoff(F(3,2),1),F(1,2))
        self.assertEqual(c.cutoff(F(2),1),0)
        self.assertEqual(c.cutoff(F(1),1),1)
        for t,H in [(F(-1),1),(F(1),0),(F(1),True)]:
            with self.assertRaises(ValueError):c.cutoff(t,H)

    def test_02_local_completion_price(self):
        for y in range(2,128):
            source,old=c.completion(y);inn=c.innovations(source)
            tail=sum((v*v for v in inn[y+1:]),F())
            recent=sum((v*v for v in old[y//2+1:]),F())
            self.assertLessEqual(tail,recent)
            self.assertLessEqual(sum(v*v for v in inn),2*sum(v*v for v in old))

    def test_03_two_frequency_dictionaries(self):
        for y in range(3,16):
            source,_=c.completion(y);_,amps=c.source(source)
            X=(y+1)**2//2
            for H in (1,2):
                if X>=8*H:
                    self.assertEqual(c.frequency_map(amps,X,H),c.product_frequency_map(source,X,H))

    def test_04_formal_double_difference(self):
        for y in range(2,24):
            source,_=c.completion(y);z,_=c.source(source)
            self.assertEqual(c.verify_difference_identity(source,z),(len(source)-1)**2)

    def test_05_localization_zeros(self):
        def from_innovations(xs):
            return [F()]+[n*(xs[n]-xs[n-1]) for n in range(1,len(xs))]
        x=[F()]*33;x[7]=F(3);x[24]=F(1,5)
        source=from_innovations(x);_,amps=c.source(source)
        before=c.frequency_map(amps,512,1)
        x[7]=0;after_source=from_innovations(x);_,after_amps=c.source(after_source)
        self.assertEqual(before,c.frequency_map(after_amps,512,1))
        self.assertTrue(before)

    def test_06_finite_trig_derivative_identity(self):
        for q in range(5,16):
            for k in (1,3,7,12):
                a=1
                sn=e.cos_fraction(q-2*a,4*q)
                sins=e.sumiv(e.cos_fraction(q-4*n*a,4*q) for n in range(1,k+1))
                lhs=e.scale(e.mul(sn,sins),2)
                rhs=e.sub(e.cos_fraction(a,2*q),e.cos_fraction((2*k+1)*a,2*q))
                self.assertTrue(e.contains(e.sub(lhs,rhs),0))

    def test_07_complete_mode_tail_bound(self):
        X=16
        for q in (9,13,17,29,41,67):
            vals,_=c.spectral({F(1,q):F(1)},31)
            bound=e.rat(F(q,X))[1]
            for k in range(X,32):self.assertLessEqual(max(abs(v) for v in vals[k]),bound)

    def test_08_strict_newton_endpoint(self):
        source,_=c.completion(7);z,_=c.source(source)
        c.newton(source,z,7,63)
        with self.assertRaises(ValueError):c.newton(source,z,7,64)
        n=64
        output=-sum((z[d] for d in e.divisors(n) if d<len(z)),F())
        err=-sum((source[d] for d in e.divisors(8) if d<len(source)),F())
        self.assertEqual(F(e.mu_trial(n))-output,err*err)
        self.assertNotEqual(err,0)

    def test_09_native_positive_covariance_and_constants(self):
        p=self.quick['focused_panels'][0]
        self.assertGreater(int(p['twice_micro_complement']['lo']),0)
        self.assertLess(int(p['pp_centering_constant']['hi']),0)
        source,_=c.completion(7);_,amps=c.source(source)
        vals,const=c.spectral(c.frequency_map(amps,32,1),63)
        dropped=[e.sub(v,const) for v in vals]
        self.assertFalse(e.overlaps(c.energy(vals,32,63),c.energy(dropped,32,63)))

    def test_10_homogeneity_and_baseline(self):
        source,_=c.completion(7);_,amps=c.source(source)
        freq=c.frequency_map(amps,32,1)
        for t in (F(1,2),F(-3)):
            _,scaled=c.source([t*v for v in source])
            self.assertEqual(c.frequency_map(scaled,32,1),{a:t*t*b for a,b in freq.items()})
        alpha=[F()]*31
        for n in (1,10,15,30):alpha[n]=F(1)
        for n in (2,3,5,6):alpha[n]=F(-1)
        inn=c.innovations(alpha)
        self.assertEqual(sum(x*x for x in inn),F(23,15))
        self.assertEqual(sum(alpha[d] for d in e.divisors(6)),-2)

    def test_11_report_refusals(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'result.json';p.write_bytes(c.canonical(self.quick));c.validate(p,self.quick)
            for key,value in [('RH_proved',True),('evaluated_cells_including_overlap',0),('schema',True)]:
                bad=copy.deepcopy(self.quick);bad[key]=value;p.write_bytes(c.canonical(bad))
                with self.assertRaises(ValueError):c.validate(p,self.quick)
            bad=copy.deepcopy(self.quick);bad['focused_panels'][0]['centering_constant']['lo']='0'
            p.write_bytes(c.canonical(bad))
            with self.assertRaises(ValueError):c.validate(p,self.quick)
            p.write_text('{"schema":1,"schema":1}')
            with self.assertRaises(ValueError):c.validate(p,self.quick)
            rp=Path(tmp)/'receipt.json';rp.write_bytes(c.canonical(c.receipt(self.quick)));c.validate_receipt(rp,self.quick)
            badr=c.receipt(self.quick);badr['full_report_sha256']='0'*64;rp.write_bytes(c.canonical(badr))
            with self.assertRaises(ValueError):c.validate_receipt(rp,self.quick)
            p.write_bytes(c.canonical(self.quick));link=Path(tmp)/'link.json';link.symlink_to(p)
            with self.assertRaises(ValueError):c.validate(link,self.quick)

    def test_12_real_cli_acceptance_and_refusal(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'result.json';p.write_bytes(c.canonical(self.quick))
            cmd=[sys.executable]+(['-O'] if sys.flags.optimize else [])+['-S','-B',str(c.ROOT/'check.py'),'--quick','--check',str(p)]
            ok=subprocess.run(cmd,capture_output=True,text=True,timeout=15)
            self.assertEqual(ok.returncode,0,ok.stderr)
            bad=copy.deepcopy(self.quick);bad['focused_panels'][0]['cells']-=1;p.write_bytes(c.canonical(bad))
            no=subprocess.run(cmd,capture_output=True,text=True,timeout=15)
            self.assertNotEqual(no.returncode,0)
            self.assertIn('report differs',no.stderr)

if __name__=='__main__':unittest.main()
