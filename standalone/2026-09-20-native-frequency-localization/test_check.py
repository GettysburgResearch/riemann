#!/usr/bin/env python3
"""Bounded NCL29 controls. Independent runs do not mean independent authorship."""
from fractions import Fraction as F
import copy
import importlib.util
import itertools
import json
from math import comb,gcd
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

P=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('c',P/'check.py')
c=importlib.util.module_from_spec(sp)
sp.loader.exec_module(c)


class Tests(unittest.TestCase):
    def test_01_interval_arithmetic(self):
        xs=[F(-7,3),F(-1,8),F(),F(1,7),F(11,4)]
        for x,y in itertools.product(xs,repeat=2):
            self.assertTrue(c.contains(c.add(c.rat(x),c.rat(y)),x+y))
            self.assertTrue(c.contains(c.mul(c.rat(x),c.rat(y)),x*y))
            self.assertTrue(c.contains(c.scale(c.rat(x),y),x*y))
        for x in xs:
            self.assertTrue(c.contains(c.square(c.rat(x)),x*x))
        self.assertEqual(c.square(c.rat(0)),c.ZERO)
        with self.assertRaises(ValueError):c.log_iv(c.rat(-1))
        with self.assertRaises(ValueError):c.reciprocal((-1,1))

    def test_02_pi_and_elementary_values(self):
        # Different identity and exact-rational series, not production fixed point.
        def at(d):
            n=190
            s=sum((F((-1)**j,(2*j+1)*d**(2*j+1)) for j in range(n)),F())
            return s,s+F(1,(2*n+1)*d**(2*n+1))
        a,b=at(2),at(3)
        lo=4*(a[0]+b[0]);hi=4*(a[1]+b[1])
        piv=c.pi_iv()
        self.assertLessEqual(F(piv[0],c.SCALE),lo)
        self.assertGreaterEqual(F(piv[1],c.SCALE),hi)
        for a,q,v in [(0,1,1),(1,6,F(1,2)),(1,4,0),(1,3,F(-1,2)),(1,2,-1)]:
            self.assertTrue(c.contains(c.cos_fraction(a,q),v))
        for q in range(2,33):
            for a in range(q):self.assertEqual(c.cos_fraction(a,q),c.cos_fraction(q-a,q))
        ref=sum((F(2,(2*j+1)*3**(2*j+1)) for j in range(160)),F())
        err=F(9,4*321*3**321)
        self.assertLessEqual(F(c.log2_iv()[0],c.SCALE),ref)
        self.assertGreaterEqual(F(c.log2_iv()[1],c.SCALE),ref+err)
        self.assertTrue(c.contains(c.log_iv(c.rat(1)),0))
        self.assertTrue(c.overlaps(c.log_iv(c.rat(F(1,8))),c.scale(c.log2_iv(),-3)))

    def test_03_roots_and_block_schedule(self):
        for n in range(257):
            for k in [2,3,11]:
                r=c.iroot(n,k);self.assertLessEqual(r**k,n);self.assertGreater((r+1)**k,n)
        for Y in range(7,513):
            bs=c.blocks(Y)
            self.assertEqual(bs[0][0],Y+1)
            self.assertEqual(bs[-1][1],(Y+1)**2-1)
            self.assertEqual(sum(hi-lo+1 for lo,hi,_ in bs),Y*(Y+1))
            for (lo,hi,y),(lo2,_,_) in zip(bs,bs[1:]):self.assertEqual(hi+1,lo2)
        with self.assertRaises(ValueError):c.blocks(6)
        with self.assertRaises(ValueError):c.completion(True)

    def test_04_prime_threshold_and_majorant(self):
        for a in range(1,8):
            for i,j in itertools.product(range(10),repeat=2):
                rhs=sum(i>=u and j>=a-u for u in range(a+1))
                rhs-=sum(i>=u and j>=a+1-u for u in range(1,a+1))
                self.assertEqual(int(i+j>=a),rhs)
        for q in range(1,257):
            A=F(1);d4=1;g=F(1)
            for p,a in c.factors(q):
                A*=a+1+F(a,p);d4*=comb(a+3,3);g*=(1+F(1,p))**2
            self.assertLessEqual(A*A,d4*g)
        for p in range(2,101):
            self.assertLessEqual(1+F(8,p*p)+F(4,p**3),(1-F(1,p*p))**(-10))

    def test_05_arbitrary_balanced_source_identities(self):
        for tail in itertools.product([-1,0,1],repeat=3):
            vals=[F(),F(1)]+[F(x) for x in tail]
            vals.append(-5*sum((vals[n]/n for n in range(1,5)),F()))
            amps,z=c.source_data(vals)
            for n in range(1,21):
                ram=sum((b*sum(d*c.mu_trial(q//d) for d in c.divisors(gcd(q,n)))
                         for q,b in amps.items()),F())
                target=sum((z[d] for d in c.divisors(n) if d<len(z)),F())
                self.assertEqual(ram,target)
        with self.assertRaises(ValueError):c.source_data([F(),F(1),F(1)])

    def test_06_angular_coefficient_mass(self):
        for q in range(2,33):
            for H in [2,3,8]:
                vals=[c.reciprocal(c.sub(c.rat(2),c.scale(c.cos_fraction(a,q),2)))
                      for a in range(1,q) if H*min(a,q-a)>=q]
                upper=F(c.sumiv(vals)[1],c.SCALE)
                self.assertLessEqual(upper,F(q*H,4))

    def test_07_exact_tail_identity(self):
        vals=[F((7*n)%11-5,1+n%4) for n in range(19)]
        for b in range(1,8):
            t=[vals[k]/(k+1)-sum((vals[j]/(j*(j+1)) for j in range(k+1,len(vals))),F())
               for k in range(b,len(vals))]
            lhs=sum((v*v for v in t),F())
            mean=sum((vals[j]/(j*(j+1)) for j in range(b,len(vals))),F())
            rhs=sum((vals[j]**2/(j*(j+1)) for j in range(b,len(vals))),F())-b*mean*mean
            self.assertEqual(lhs,rhs)

    def test_08_centered_frequency_mode_identity(self):
        for q in range(2,13):
            far,lf,_=c.spectral_values({q:F(1)},13,6,True)
            near,ln,_=c.spectral_values({q:F(1)},13,6,False)
            fs=c.factors(q)
            L=c.log_iv(c.rat(fs[0][0])) if len(fs)==1 else c.ZERO
            self.assertTrue(c.overlaps(c.add(lf,ln),L))
            for k in range(14):
                hr=sum((F(sum(d*c.mu_trial(q//d) for d in c.divisors(gcd(q,n))),n)
                        for n in range(1,k+1)),F())
                self.assertTrue(c.overlaps(c.add(far[k],near[k]),c.add(c.rat(hr),L)))

    def test_09_partial_centering_cannot_be_removed(self):
        amps,_=c.source_data([F(),F(1),F(-2)])
        self.assertEqual(amps,{2:F(-1),4:F(1)})
        _,lf,_=c.spectral_values(amps,8,3,True)
        _,ln,_=c.spectral_values(amps,8,3,False)
        self.assertTrue(c.overlaps(lf,c.neg(c.log2_iv())))
        self.assertTrue(c.overlaps(ln,c.log2_iv()))
        self.assertFalse(c.contains(lf,0));self.assertFalse(c.contains(ln,0))
        self.assertTrue(c.contains(c.add(lf,ln),0))

    def test_10_native_signed_covariance_and_full_source(self):
        p=c.block_panel(16,31,5,8,True)
        self.assertGreater(int(p['twice_far_near']['lo']),0)
        p2=c.block_panel(32,63,7,8,True)
        self.assertLess(int(p2['twice_far_near']['hi']),0)
        self.assertGreater(p2['far_composite_frequencies_beyond_local_NCG28_denominator_cut'],0)
        for y in [2,3,5,7,11,15]:
            a,_=c.completion(y);_,z=c.source_data(a)
            _,n=c.native_values(y,(y+1)**2-1,a,z)
            self.assertEqual(n,(y+1)**2-1)

        # Exact source-pair versus reduced-frequency near-band dictionaries.
        for y in [2,3,5,7]:
            src,_=c.completion(y);amps,_=c.source_data(src);L=len(src)-1
            for H in [3,8]:
                left={}
                for q,bq in amps.items():
                    if len(c.factors(q))<2:continue
                    for a in range(1,q):
                        if gcd(a,q)==1 and H*min(a,q-a)<q:left[(a,q)]=bq
                right={}
                for r in range(1,L+1):
                    for t in range(1,L+1):
                        d=r*t;v=src[r]*src[t]/d
                        if not v:continue
                        for j in range(1,d):
                            g=gcd(j,d);a=j//g;q=d//g
                            if H*min(j,d-j)<d and len(c.factors(q))>=2:
                                right[(a,q)]=right.get((a,q),F())+v
                right={k:v for k,v in right.items() if v}
                self.assertEqual(left,right)

    def test_11_report_schema_and_missing_terms(self):
        actual=c.produce((7,))
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json';p.write_bytes(c.canonical(actual));c.validate_report(p,actual)
            for mut in ['bool','cross','constant','coverage']:
                v=copy.deepcopy(actual)
                if mut=='bool':v['schema']=True
                if mut=='cross':v['campaigns'][0]['totals'].pop('twice_good_near')
                if mut=='constant':v['campaigns'][0]['panels'][0]['far_centering_constant']=c.enc(c.ZERO)
                if mut=='coverage':v['campaigns'][0]['covered_cells']-=1
                p.write_bytes(c.canonical(v))
                with self.assertRaises(ValueError):c.validate_report(p,actual)
            p.write_text('{"schema":1,"schema":1}')
            with self.assertRaises(ValueError):c.read_report(p)

    def test_12_actual_cli_acceptance_and_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'r.json'
            base=[sys.executable,'-S','-B']
            if sys.flags.optimize:base+=['-O']
            base += [str(P/'check.py'),'--cutoffs','7']
            ok=subprocess.run(base+['--write',str(p)],capture_output=True,text=True)
            self.assertEqual(ok.returncode,0,ok.stderr)
            ok=subprocess.run(base+['--check',str(p)],capture_output=True,text=True)
            self.assertEqual(ok.returncode,0,ok.stderr)
            v=c.read_report(p);v['campaigns'][0]['B']-=1;p.write_bytes(c.canonical(v))
            bad=subprocess.run(base+['--check',str(p)],capture_output=True,text=True)
            self.assertNotEqual(bad.returncode,0)
            self.assertIn('report differs',bad.stderr)


if __name__=='__main__':unittest.main(verbosity=2)
