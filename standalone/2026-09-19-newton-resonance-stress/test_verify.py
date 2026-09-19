"""Bounded tests. Run separately from the complete report replay."""
import copy
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('nsr_verify',HERE/'verify.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)


class Checks(unittest.TestCase):
    def test_primitive_and_moments(self):
        d=v.read_source();a,b,c,C=v.audit_source(d)
        self.assertEqual(sum(c),0);self.assertEqual(set(c),{-1,0,1})
        self.assertEqual(sum(v.ALPHA.values()),0)
        self.assertEqual(sum(F(z,n) for n,z in v.ALPHA.items()),0)
        self.assertGreater(a,30);self.assertLess(b,d['Y'])

    def test_source_refusals(self):
        d=v.read_source()
        changes=[('X1',2*d['start']**2),('X0',2*(d['Y']+1)),
                 ('word_length',d['word_length']+1),('bins',9000),
                 ('Y',True),('word_codec','float'),('word_zlib_b64','bad!')]
        for key,value in changes:
            with self.subTest(key=key):
                e=copy.deepcopy(d);e[key]=value
                with self.assertRaises((ValueError,TypeError,KeyError)):v.audit_source(e)
        e=copy.deepcopy(d);e['alpha'][0][1]=0
        with self.assertRaises(ValueError):v.audit_source(e)

    def test_directed_negative_arithmetic(self):
        for n in range(-19,20):
            for d in range(1,27):
                q=n*256//d
                self.assertLessEqual(F(q,256),F(n,d))
                self.assertGreaterEqual(F(q+1,256),F(n,d))
        self.assertEqual(v.square_interval(F(-2),F(3)),(F(0),F(9)))
        self.assertEqual(v.interval_text(F(-1,3),F(1,3),3),['-0.334','0.334'])

    def test_divisor_first_and_endpoint(self):
        mu=v.mobius_linear(4095)
        self.assertEqual(mu,v.mobius_square_sieve(4095))
        for y in (1,2,3,4,7,15,31,63):v.divisor_first(mu,y)
        # The original balanced seed reconstructs through 3, not necessarily 4.
        c={1:F(1),2:F(-3),4:F(2)}
        value=2*c.get(4,0)-sum(a*b for r,a in c.items() for s,b in c.items() if 4%(r*s)==0)
        self.assertEqual(value,-4);self.assertEqual(mu[4],0)
        bad=mu.copy();bad[6]=-1
        with self.assertRaises(ValueError):v.divisor_first(bad,7)

    def test_short_shift_budget_and_product_sign(self):
        mu=v.mobius_linear(64)
        for y in range(2,33):
            H=sum(F(1,n) for n in range(1,y+1))
            for h in (0,1,3,7):
                absolute=sum(abs(mu[m]*mu[n])* (F(1,max(m,n))-F(1,y+1))
                             for m in range(1,y+1) for n in range(1,y+1) if abs(m-n)<=h)
                self.assertLessEqual(absolute,(2*h+1)*H)
        # No cancellation occurs among nonzero mu(r)mu(s) having the same product.
        fibers={}
        for r in range(1,33):
            for s in range(1,33):
                if mu[r]*mu[s]:fibers.setdefault(r*s,set()).add(mu[r]*mu[s])
        self.assertTrue(all(len(signs)==1 for signs in fibers.values()))

    def test_typed_result_and_duplicate_refusals(self):
        actual={'schema':1,'RH_proved':False,'value':'1.5'}
        with tempfile.TemporaryDirectory() as t:
            p=Path(t)/'x.json';p.write_text(json.dumps(actual));v.check_result(p,actual)
            for bad in ({'schema':True,'RH_proved':False,'value':'1.5'},
                        {'schema':1,'RH_proved':True,'value':'1.5'},
                        {'schema':1,'RH_proved':False,'value':'1.6'}):
                p.write_text(json.dumps(bad))
                with self.assertRaises(ValueError):v.check_result(p,actual)
            p.write_text('{"schema":1,"schema":1}')
            with self.assertRaises(ValueError):v.check_result(p,actual)


if __name__=='__main__':unittest.main()
