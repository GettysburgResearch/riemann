#!/usr/bin/env python3
"""Finite exact-algebra and actual CLI refusal tests; no infinite proof claim."""
from __future__ import annotations
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cascade_check',HERE/'check.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class Tests(unittest.TestCase):
    def test_complete_reconstruction(self):
        self.assertTrue(mod.same_typed(mod.reconstruct(),mod.strict_load(HERE/'checks.json')))

    def test_second_density(self):
        self.assertEqual(mod.coefficients(2),[(1,Fraction(16,9),Fraction(-32,27)),
                                              (4,Fraction(16,9),Fraction(32,27))])

    def test_harmonic_coefficient(self):
        for N in range(1,21):
            for n,(_,u,v) in enumerate(mod.coefficients(N),1):
                c=1+v*n*n/u
                harmonic=Fraction(-1,2)+n*sum((Fraction(1,k) for k in range(N-n+1,N+n+1)),Fraction(0))
                self.assertEqual(c,harmonic)

    def test_arguments_reject_aliases(self):
        for bad in [True,False,0,-2,1.0,'2',None]:
            with self.assertRaises(ValueError): mod.coefficients(bad)

    def test_typed_comparison(self):
        for a,b in [(True,1),(1,1.0),([1],[True]),({'x':0},{'x':False})]:
            self.assertFalse(mod.same_typed(a,b))

    def test_cli_pristine_and_mutations(self):
        base=json.loads((HERE/'checks.json').read_text())
        mutations=[]
        def changed(label, fn):
            d=json.loads(json.dumps(base)); fn(d)
            mutations.append((label,json.dumps(d)))
        changed('false_RH',lambda d:d.__setitem__('rh_proved',True))
        changed('false_certificate',lambda d:d.__setitem__('numerical_zero_certificate',True))
        changed('boolean_integer',lambda d:d.__setitem__('rh_proved',0))
        changed('float_integer',lambda d:d['coverage'].__setitem__('local_partial_fractions',float(d['coverage']['local_partial_fractions'])))
        changed('wrong_tail',lambda d:d['tail_budgets'].__setitem__('4','1/99'))
        changed('wrong_moment',lambda d:d['raw_moments_N4'].__setitem__(2,'0/1'))
        changed('reduced_coverage',lambda d:d['coverage']['density_cutoffs'].pop())
        changed('extra_field',lambda d:d.__setitem__('extra',True))
        changed('missing_field',lambda d:d.pop('density_N2'))
        raw=json.dumps(base)
        mutations.append(('duplicate_key','{"rh_proved":false,'+raw[1:]))
        mutations.append(('nonfinite','{"x":NaN}'))
        mutations.append(('empty','{}'))
        with tempfile.TemporaryDirectory() as tmp:
            receipt=Path(tmp)/'receipt.json'
            def run(text):
                receipt.write_text(text)
                cmd=[sys.executable,'-I','-S','-B']+(['-O'] if sys.flags.optimize else [])+[str(HERE/'check.py'),'--check',str(receipt)]
                return subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            result=run(raw)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(result.stdout.strip(),'PASS_EXACT_FINITE_ALGEBRA_ONLY')
            for label,text in mutations:
                with self.subTest(label=label):
                    result=run(text)
                    self.assertNotEqual(result.returncode,0,label)
                    self.assertIn('FAIL:',result.stderr)
        self.assertEqual(len(mutations),12)

if __name__=='__main__':
    unittest.main(verbosity=2)
