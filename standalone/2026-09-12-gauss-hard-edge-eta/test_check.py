#!/usr/bin/env python3
"""Bounded tests and actual CLI refusal tests for GHE26 (standard library only)."""
from __future__ import annotations
import copy
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ghe_check',ROOT/'check.py')
if spec is None or spec.loader is None:
    raise RuntimeError('Cannot load exact checker')
c=importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def run_cli(path):
    flags=['-I','-S','-B']
    if sys.flags.optimize: flags.append('-O')
    return subprocess.run([sys.executable,*flags,str(ROOT/'check.py'),'--check',str(path)],
                          capture_output=True,text=True,timeout=90,check=False)


class ExactChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record=c.build_record()  # One complete fresh reconstruction per suite.
        cls.retained=c.strict_json((ROOT/'results.json').read_text(encoding='utf-8'))

    def test_complete_reconstruction(self):
        self.assertEqual(c.canonical(self.record),c.canonical(self.retained))
        self.assertEqual(len(self.record['nodes']),9)

    def test_coefficient_tail_beyond_polynomial_degree(self):
        for m in (1,3,8,16):
            a=c.shape(m)
            for r in range(m+1,m+17):
                base=F(2,3)**r/F(c.factorial(2*r))
                self.assertEqual(c.edge_coeff(m,r),0)
                self.assertLessEqual(base,base*r**3/a)
                first=F(r*(7-4*r*r),6)
                self.assertLessEqual(abs(base*(1+first/a)),2*base*r**6/a**2)

    def test_single_node_inertia_independently(self):
        # For m=1 the sole scaled node is (5/2)^2*(2/5)=5/2.
        self.assertEqual(c.sturm_count(1,F(2)),0)
        self.assertEqual(c.sturm_count(1,F(3)),1)
        with self.assertRaises(ValueError):
            c.sturm_count(1,F(5,2))

    def test_primitive_mutation_rejected(self):
        old=c.offsq
        with patch.object(c,'offsq',lambda n:old(n)*F(37,36)):
            with self.assertRaises(ValueError):
                c.build_record()

    def test_cli_pristine(self):
        p=run_cli(ROOT/'results.json')
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        self.assertIn('PASS:',p.stdout)

    def test_cli_changed_records(self):
        mutations=[]
        d=copy.deepcopy(self.retained);d['scope']='RH proved';mutations.append(d)
        d=copy.deepcopy(self.retained);d['max_order']=True;mutations.append(d)
        d=copy.deepcopy(self.retained);d['orders'][4]['tail_variance']='0';mutations.append(d)
        d=copy.deepcopy(self.retained);d['nodes'][0]['upper']='1';mutations.append(d)
        d=copy.deepcopy(self.retained);d['nodes'][5]['count_below_upper']=4;mutations.append(d)
        with tempfile.TemporaryDirectory() as tmp:
            for j,record in enumerate(mutations):
                with self.subTest(mutation=j):
                    path=Path(tmp)/f'bad-{j}.json'
                    path.write_text(json.dumps(record),encoding='utf-8')
                    p=run_cli(path)
                    self.assertNotEqual(p.returncode,0)
                    self.assertIn('REJECT:',p.stderr)
                    self.assertNotIn('PASS:',p.stdout)

    def test_cli_duplicate_json_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'duplicate.json'
            path.write_text('{"schema":"x","schema":"y"}',encoding='utf-8')
            p=run_cli(path)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('duplicate JSON key',p.stderr)


if __name__=='__main__':
    unittest.main(verbosity=2)
