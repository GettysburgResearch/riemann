#!/usr/bin/env python3
"""Adversarial accepting-CLI tests, in normal and optimized interpreters."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('tha26_check',ROOT/'check.py')
check=importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)

class Controls(unittest.TestCase):
    pristine_replays = 0
    refusal_cases = 0
    @classmethod
    def setUpClass(cls):
        cls.text=(ROOT/'result.json').read_text()
        cls.result=check.load_json(cls.text)

    def cli(self,expected=None,input_bytes=None,symlink=False):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            receipt=folder/'expect.json'
            receipt.write_text(expected if expected is not None else self.text)
            cmd=[sys.executable,'-I','-S','-B']
            if sys.flags.optimize: cmd.append('-O')
            cmd += [str(ROOT/'check.py'),'--expect',str(receipt)]
            if input_bytes is not None:
                inp=folder/'INPUTS.json';inp.write_bytes(input_bytes)
                cmd += ['--inputs',str(inp)]
            if symlink:
                alias=folder/'alias.json';alias.symlink_to(ROOT/'INPUTS.json')
                cmd += ['--inputs',str(alias)]
            return subprocess.run(cmd,capture_output=True,timeout=30)

    def altered(self,fn):
        obj=json.loads(self.text)
        fn(obj)
        return json.dumps(obj)

    def rejected(self,**kw):
        result=self.cli(**kw)
        self.assertNotEqual(result.returncode,0)
        self.assertIn(b'FAIL_THA26',result.stderr)
        type(self).refusal_cases += 1

    def test_pristine_full_reconstruction(self):
        result=self.cli()
        self.assertEqual(result.returncode,0,result.stderr.decode())
        self.assertEqual(result.stdout.decode(),self.text)
        type(self).pristine_replays += 1

    def test_duplicate_key(self):
        self.rejected(expected=self.text.replace('{','{"schema":1,',1))

    def test_float_alias(self):
        self.rejected(expected=self.text.replace('"schema": 1','"schema": 1.0'))

    def test_boolean_integer_alias(self):
        self.rejected(expected=self.text.replace('"schema": 1','"schema": true'))

    def test_false_rh_promotion(self):
        self.rejected(expected=self.altered(lambda x:x.update(rh_proved=True)))

    def test_drop_complete_tail(self):
        self.rejected(expected=self.altered(lambda x:x['bounds'].pop('tail_absolute_mass_upper')))

    def test_zero_tail_claim(self):
        self.rejected(expected=self.altered(lambda x:x['bounds'].update(tail_absolute_mass_upper=[0,1])))

    def test_reverse_negative_determinant(self):
        def mutate(x):
            x['compact_control']['hankel_d4_shift2_determinant'][0] *= -1
        self.rejected(expected=self.altered(mutate))

    def test_change_imported_ordinate(self):
        inp=(ROOT/'INPUTS.json').read_bytes().replace(b'1413',b'1412')
        self.rejected(input_bytes=inp)

    def test_change_imported_height(self):
        inp=(ROOT/'INPUTS.json').read_bytes().replace(b'3000000000000',b'3000000000001')
        self.rejected(input_bytes=inp)

    def test_symlink_input(self):
        self.rejected(symlink=True)

    def test_empty_receipt(self):
        self.rejected(expected='{}')

    def test_overlapping_interpolation_nodes(self):
        with self.assertRaises(ValueError):
            check.interpolation_budget([(Q(1),Q(2)),(Q(1),Q(2))],Q(1,10),Q(1,10),2)

    def test_shift_zero_not_admissible(self):
        with self.assertRaises(ValueError):
            check.interpolation_budget([(Q(1),Q(1))],Q(1,10),Q(1,10),0)

    def test_factorial_removal_is_not_psd(self):
        self.assertEqual(check.determinant([[Q(1),Q(1,2)],[Q(1,2),Q(1,6)]]),-Q(1,12))

    def test_wrong_cumulant_sign_does_not_reconstruct(self):
        mu=check.comparator_moments(Q(1,2),Q(6,5),16)
        correct=check.trace_by_log_derivative(mu,8)
        other=check.trace_by_cumulants(mu,8)
        other[2] *= -1
        self.assertNotEqual(correct,other)

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(Controls)
    result=unittest.TextTestRunner(verbosity=1).run(suite)
    summary={'tests':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),
             'skips':len(result.skipped),'passed':result.wasSuccessful(),
             'full_pristine_cli_replays':Controls.pristine_replays,'actual_cli_refusal_cases':Controls.refusal_cases}
    print(json.dumps(summary,sort_keys=True))
    raise SystemExit(0 if result.wasSuccessful() else 1)
