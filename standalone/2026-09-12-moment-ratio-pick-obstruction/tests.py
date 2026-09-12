#!/usr/bin/env python3
"""Tests of the finite certificate, not independent analytic verification."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from check import (coefficients, native_moments, reconstruct, rational_control,
                   bernstein_numerator, ratios, poly_product_except)
from numeric_core import I, S, exp_i, pi_i

ROOT = Path(__file__).resolve().parent

class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record = reconstruct(64)

    def test_record_and_complete_second_mesh(self):
        self.assertEqual(json.loads((ROOT/'results.json').read_text()), self.record)
        other = reconstruct(96)
        for a,b in zip(self.record['moments'],other['moments']):
            self.assertLessEqual(max(int(a['lo_integer']), int(b['lo_integer'])),
                                 min(int(a['hi_integer']), int(b['hi_integer'])))
        self.assertTrue(all(int(b['hi_integer']) < -S//2
                            for b in other['theta_numerator_Bernstein']))

    def test_positive_rational_kernel_at_exact_nodes(self):
        c = coefficients()
        for t in [F(0),F(1,7),F(1),F(5),F(12),F(90),F(1000)]:
            left = sum((x*n/(t+n) for n,x in enumerate(c,1)),F(0))
            den=F(1)
            for n in range(1,11): den*=t+n
            self.assertEqual(left,t*(t*t-24*t+90)**2/den)
            self.assertGreaterEqual(left,0)

    def test_complete_bernstein_positive_controls(self):
        c=coefficients()
        for t in [F(1,7),F(1),F(7),F(90)]:
            values=[F(3)+F(2)*n+F(5)*n/(n+t) for n in range(1,11)]
            self.assertGreaterEqual(sum((a*b for a,b in zip(c,values)),F(0)),0)

    def test_all_real_control_fails_stronger_test(self):
        v,q=rational_control()
        self.assertLess(q,0)
        self.assertGreater(q,F(-321,10**6))
        self.assertLess(q,F(-320,10**6))

    def test_interval_rational_and_elementary_controls(self):
        for x in [F(-7,13),F(0),F(3,11),F(9,4)]:
            for y in [F(-2,5),F(1,3),F(5,2)]:
                a,b=I.point(x),I.point(y)
                self.assertTrue((a+b).contains(x+y))
                self.assertTrue((a*b).contains(x*y))
                self.assertTrue((a/b).contains(x/y))
        self.assertTrue(exp_i(I.point(0)).contains(1))
        for x in [F(-17,3),F(-1,8),F(1,7),F(9,2)]:
            self.assertTrue((exp_i(I.point(x))*exp_i(I.point(-x))).contains(1))
        p=pi_i()
        self.assertGreater(p.lo*106,333*S)
        self.assertLess(p.hi*113,355*S)
        with self.assertRaises(ZeroDivisionError):
            I(-1,1).inv()
        with self.assertRaises(TypeError):
            _=I.point(1)+0.1
        with self.assertRaises(TypeError):
            I.point(0.1)

    def test_bernstein_basis_reconstructs_polynomial(self):
        from math import comb
        values=[I.point(F(n+1,3)) for n in range(10)]
        b=bernstein_numerator(values)
        c=coefficients()
        for theta in [F(0),F(1,7),F(1,2)]:
            lhs=I.point(0)
            for n,(cn,vn) in enumerate(zip(c,values),1):
                f=F(n)*cn
                for j in range(1,11):
                    if j!=n: f*=j-theta
                lhs+=f*vn
            rhs=sum((b[j]*comb(9,j)*(2*theta)**j*(1-2*theta)**(9-j)
                     for j in range(10)),I.point(0))
            self.assertLessEqual(max(lhs.lo,rhs.lo),min(lhs.hi,rhs.hi))

    def test_actual_cli_accepts_pristine_and_rejects_changes(self):
        flags=['-S','-B']+(['-O'] if sys.flags.optimize else [])
        command=[sys.executable,*flags,str(ROOT/'check.py'),'--check']
        good=subprocess.run(command+[str(ROOT/'results.json')],capture_output=True,text=True)
        self.assertEqual(good.returncode,0,good.stderr)
        mutations=[]
        r=copy.deepcopy(self.record);r['Q_zero']['hi_integer']='0';mutations.append(r)
        r=copy.deepcopy(self.record);r['moments'][5]['lo_integer']='0';mutations.append(r)
        r=copy.deepcopy(self.record);r['theta_numerator_Bernstein'][0]['hi_integer']='0';mutations.append(r)
        r=copy.deepcopy(self.record);r['rational_witness'][0]='0';mutations.append(r)
        with tempfile.TemporaryDirectory() as td:
            for i,r in enumerate(mutations):
                p=Path(td)/f'altered-{i}.json';p.write_text(json.dumps(r))
                bad=subprocess.run(command+[str(p)],capture_output=True,text=True)
                self.assertNotEqual(bad.returncode,0)
                self.assertIn('record differs from complete source reconstruction',bad.stderr)

if __name__=='__main__':
    unittest.main(verbosity=2)
