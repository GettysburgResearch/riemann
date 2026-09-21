#!/usr/bin/env python3
"""Bounded finite regression/refusal suite; does not verify the infinite theorem."""
from __future__ import annotations
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import check as v
import exact as e
import inherited_mcb as m

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small=v.produce(True)

    def test_01_authentication(self):
        v.authenticate()
        self.assertEqual(e.BITS,144)

    def test_02_exponents_and_integer_roots(self):
        self.assertEqual(v.BAND_EXPONENT,F(191,82))
        self.assertEqual(v.OUTPUT_EXPONENT+v.INPUT_EXPONENT/2,1)
        for a in range(30):
            for d in (1,2,3,7):
                r=v.root_floor(a,d)
                self.assertLessEqual(r**d,a)
                self.assertGreater((r+1)**d,a)
        for bad in (True,-1,F(1,2)):
            with self.assertRaises(ValueError):v.root_floor(bad,2)

    def test_03_rank_correction_is_not_optional(self):
        r=v.polynomial_fixture([F(),F(1),F(-2)],1)
        raw=F(*map(int,r['raw']));center=F(*map(int,r['centered']));rank=F(*map(int,r['rank_one']))
        self.assertEqual((raw,center,rank),(F(33,128),F(37,640),F(1,5)))
        self.assertNotEqual(raw,center)
        self.assertNotEqual(raw,center-rank)

    def test_04_exact_polynomial_corpus(self):
        self.assertEqual(self.small['algebra']['polynomial_fixtures'],120)
        self.assertEqual(v.algebra_report(),self.small['algebra'])

    def test_05_cutoff_derivatives(self):
        # Exact quintic coefficients and endpoint flatness, no sampled theorem inference.
        p=[F(1),F(0),F(0),F(-10),F(15),F(-6)]
        def diff(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
        def ev(a,t):return sum((x*t**i for i,x in enumerate(a)),F())
        self.assertEqual(ev(p,F(0)),1);self.assertEqual(ev(p,F(1)),0)
        for q in (diff(p),diff(diff(p))):
            self.assertEqual(ev(q,F(0)),0);self.assertEqual(ev(q,F(1)),0)
        for h in (1,2,7):
            for j in range(65):self.assertTrue(0<=m.cutoff(F(j*h,32),h)<=1)

    def test_06_source_and_finite_difference(self):
        for y in (2,3,7,15):
            c,_=m.completion(y);z,amps=m.source(c)
            self.assertEqual(sum((c[n]/n for n in range(1,len(c))),F()),0)
            self.assertGreater(m.verify_difference_identity(c,z),0)
            self.assertEqual(m.frequency_map(amps,32,1),m.product_frequency_map(c,32,1))

    def test_07_reseeded_spectral_values(self):
        fm={F(1,32):F(1,7),F(3,97):F(-2,11)}
        stable,_=v.spectral_stable(fm,255)
        inherited,_=m.spectral(fm,255)
        for k in (0,1,32,63,127,255):
            direct=e.ZERO
            for a,b in fm.items():
                val=e.scale(e.log_sine(a.numerator,a.denominator),2)
                val=e.add(val,e.sumiv(e.scale(e.cos_fraction(n*a.numerator,a.denominator),F(2,n)) for n in range(1,k+1)))
                direct=e.add(direct,e.scale(val,b))
            self.assertTrue(e.overlaps(direct,stable[k]))
            self.assertTrue(e.overlaps(inherited[k],stable[k]))

    def test_08_complete_mode_derivative(self):
        X=64
        for k in (64,95,127):
            for a,q in ((1,97),(3,97),(1,8)):
                sinx=e.cos_fraction(q-2*a,4*q)
                cot=e.mul(e.cos_fraction(a,2*q),e.reciprocal(sinx))
                sins=e.sumiv(e.cos_fraction(q-4*n*a,4*q) for n in range(1,k+1))
                factor=e.scale(e.pi_iv(),F(2,X))
                differentiated=e.mul(factor,e.sub(cot,e.scale(sins,2)))
                closed=e.mul(factor,e.mul(e.cos_fraction((2*k+1)*a,2*q),e.reciprocal(sinx)))
                self.assertTrue(e.overlaps(differentiated,closed))

    def test_09_full_native_covariance(self):
        b=self.small['native_blocks'][0]
        self.assertEqual(b['cells'],32)
        self.assertEqual(b['newton_checks'],63)
        self.assertEqual(len(b['all_pairwise_cross_terms']),3)
        for p in b['panels']:
            self.assertLessEqual(int(p['micro_energy']['lo']),int(p['micro_energy']['hi']))
        self.assertEqual(self.small['RH_proved'],False)

    def test_10_bad_domains(self):
        for args in ((7,32,64,[1]),(7,32,63,[1,5]),(7,32,63,[2,1]),(7,32,63,[True])):
            with self.assertRaises(ValueError):v.native_ladder(*args)
        for h in (True,0,-1):
            with self.assertRaises(ValueError):v.power_upper(h)

    def test_11_typed_and_symlink_refusals(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json';p.write_bytes(m.canonical(self.small));v.check(p,self.small)
            for key,val in (('RH_proved',0),('schema',True),('infinite_proof_verified_by_code',True)):
                bad=copy.deepcopy(self.small);bad[key]=val;p.write_bytes(m.canonical(bad))
                with self.assertRaises(ValueError):v.check(p,self.small)
            p.write_text('{"schema":1,"schema":1}')
            with self.assertRaises(ValueError):v.load(p)
            link=Path(td)/'link.json';link.symlink_to(p)
            with self.assertRaises(ValueError):v.load(link)

    def test_12_actual_cli_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json';p.write_bytes(m.canonical(self.small))
            command=[sys.executable]+(['-O'] if sys.flags.optimize else [])+['-S','-B',str(v.ROOT/'check.py'),'--quick','--check',str(p)]
            good=subprocess.run(command,capture_output=True,text=True,timeout=30)
            self.assertEqual(good.returncode,0,good.stderr)
            bad=copy.deepcopy(self.small);bad['native_blocks'][0]['panels'][0]['micro_energy']['hi']='0'
            p.write_bytes(m.canonical(bad))
            altered=subprocess.run(command,capture_output=True,text=True,timeout=30)
            self.assertNotEqual(altered.returncode,0)
            self.assertIn('canonical typed result mismatch',altered.stderr)

if __name__=='__main__':unittest.main()
