#!/usr/bin/env python3
"""Adversarial contracts for reviewer arithmetic and typed receipt reconstruction.

These are not the research authors' package tests or a full repository audit.
"""
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('reviewer_contracts',HERE/'checks.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class Contracts(unittest.TestCase):
    def test_endpoint_types(self):
        for a in (True,1.0,'1'):
            with self.subTest(a=a),self.assertRaises(TypeError):m.I(a)
    def test_reversed_endpoints(self):
        with self.assertRaises(ValueError):m.I(3,2)
    def test_zero_division(self):
        for a in (m.I(0),m.I(-1,1),m.I(0,1)):
            with self.subTest(a=a.lo),self.assertRaises(ValueError):a.reciprocal()
    def test_negative_sqrt(self):
        with self.assertRaises(ValueError):m.I(-1).sqrt()
    def test_signed_products(self):
        for a,b in ((F(-2,3),F(5,7)),(F(-2,3),F(-5,7)),(F(0),F(-2))):
            x=m.I.q(a)*m.I.q(b)
            self.assertLessEqual(F(x.lo,m.SCALE),a*b)
            self.assertGreaterEqual(F(x.hi,m.SCALE),a*b)
    def test_signed_reciprocal(self):
        a=F(-7,3);x=m.I.q(a).reciprocal()
        self.assertLessEqual(F(x.lo,m.SCALE),1/a)
        self.assertGreaterEqual(F(x.hi,m.SCALE),1/a)
    def test_square_crossing_zero(self):
        self.assertEqual(m.I(-m.SCALE,2*m.SCALE).sq().lo,0)
        self.assertEqual(m.I(-m.SCALE,2*m.SCALE).sq().hi,4*m.SCALE)
    def test_decimal_directions(self):
        for q in (F(-1,3),F(1,3),F(0),F(2)):
            self.assertLessEqual(F(m.decimal(q,8)),q)
            self.assertGreaterEqual(F(m.decimal(q,8,True)),q)
    def test_duplicate_keys(self):
        with self.assertRaises(ValueError):m.strict_json('{"a":1,"a":2}')
    def test_nonfinite_values(self):
        for v in ('NaN','Infinity','-Infinity'):
            with self.subTest(v=v),self.assertRaises(ValueError):m.strict_json('{"a":'+v+'}')
    def test_bool_int_float_distinction(self):
        for v in (0,0.0,True):
            with self.subTest(v=v),self.assertRaises(ValueError):m.verify_receipt({'rh_proved':False},json.dumps({'rh_proved':v}))
    def test_changed_and_missing_output(self):
        for d in ({'x':2},{},{'x':1,'extra':False}):
            with self.subTest(d=d),self.assertRaises(ValueError):m.verify_receipt({'x':1},json.dumps(d))
    def test_ldl_bad_pivot(self):
        with self.assertRaises(ValueError):m.ldl_pivots([[F(1),F(2)],[F(2),F(1)]])
    def test_kkt_singular(self):
        with self.assertRaises(ValueError):m.solve([[F(1),F(1)],[F(1),F(1)]],[F(1),F(1)])
    def test_actual_cli_reconstruction_and_seven_refusals(self):
        cmd=[sys.executable,'-I','-S','-B',*(['-O'] if sys.flags.optimize else []),str(HERE/'checks.py'),'--group','interval']
        out=subprocess.run(cmd,capture_output=True,check=True).stdout
        result=json.loads(out)
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'receipt.json';path.write_bytes(out)
            good=subprocess.run(cmd+['--verify-receipt',str(path)],capture_output=True)
            self.assertEqual(good.returncode,0);self.assertEqual(good.stdout,out)
            mutations=[]
            for field,value in (('rh_proved',True),('rh_proved',0),('bits',1),('marker','PASS_RH'),('author_research_code_executed',True)):
                changed=dict(result);changed[field]=value;mutations.append(json.dumps(changed))
            changed=dict(result);changed.pop('groups');mutations.append(json.dumps(changed))
            mutations.append('{"a":1,"a":2}')
            for text in mutations:
                path.write_text(text)
                bad=subprocess.run(cmd+['--verify-receipt',str(path)],capture_output=True)
                self.assertNotEqual(bad.returncode,0)
                self.assertEqual(bad.stdout,b'')

if __name__=='__main__':
    run=unittest.TextTestRunner(stream=sys.stderr).run(unittest.defaultTestLoader.loadTestsFromTestCase(Contracts))
    print(json.dumps({'marker':'PASS_REVIEWER_CONTRACTS' if run.wasSuccessful() else 'FAIL',
       'methods':run.testsRun,'errors':len(run.errors),'failures':len(run.failures),'skips':len(run.skipped),
       'actual_cli_corruption_refusals':7,'author_package_tests_run':False,'rh_proved':False},sort_keys=True,indent=2))
    sys.exit(0 if run.wasSuccessful() else 1)
