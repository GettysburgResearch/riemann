#!/usr/bin/env python3
"""Small exact controls and actual CLI refusals, not analytic-proof validation."""
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

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('bub_check', ROOT/'check.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BoundedControls(unittest.TestCase):
    def test_integer_ceilings(self):
        for R in (1,2,3,10,30,99,100,1000):
            for a in (0,1,5,20):
                p = module.schedule(R, a)
                # A separately written small integer loop verifies the ceil exponents.
                c = F(6,175)*(2*(R+5)**3+3)
                m = 0
                while 2**m < c:
                    m += 1
                self.assertEqual(m, p['m'])
                self.assertGreaterEqual(15*(p['depth']//11), p['B']+m+1)
                self.assertLess(15*(p['depth']//11-1), p['B']+m+1)
        for bad in (True, 1.0, -1, '1'):
            with self.assertRaises(ValueError):
                module.schedule(bad, 2)
        with self.assertRaises(ValueError):
            module.schedule(1, False)

    def test_analytic_constant_algebra(self):
        self.assertLess(31**11*2**15, 80**11)
        self.assertGreater(F(2,3)+F(2,81)+F(2,1215), F(11,16))
        self.assertEqual(F(8,7)*F(11,16), F(22,7)/4)
        for L in range(1,50):
            for a in (0,1,7,16):
                self.assertEqual(4*L+8*L*(a+3), (8*a+28)*L)

    def test_pairing_and_sharpness(self):
        for m in range(5):
            for p in range(4):
                row = module.ordinate(m,p)
                actual_roots = m+2*p
                self.assertEqual(row['N'], actual_roots)
                self.assertGreaterEqual(2*row['G'], 3*row['S']-row['N'])
        sharp = module.sharp_synthetic()
        self.assertEqual((sharp['positive_height_N'], sharp['simple_central_S'], sharp['clean_G']),
                         (10,4,1))
        self.assertEqual(sharp['degree'], 20)

    def test_full_reconstruction(self):
        expected = module.reconstruct()
        module.same_typed(module.strict_load(ROOT/'result.json'), expected)
        self.assertEqual(expected['source_moments'][0]['m3'], '63/25')
        self.assertEqual(expected['source_moments'][1]['m3'], '651/250')
        self.assertEqual(expected['source_moments'][0]['peano_mass'], '4/175')

    def test_cli_rejections(self):
        expected = module.reconstruct()
        changes = []
        r = copy.deepcopy(expected); r['status']['rh_proved'] = True; changes.append(r)
        r = copy.deepcopy(expected); r['status']['gap_free_cover_proved'] = True; changes.append(r)
        r = copy.deepcopy(expected); r['schedules'][0]['depth'] -= 1; changes.append(r)
        r = copy.deepcopy(expected); r['schedules'][0]['R'] = 30.0; changes.append(r)
        r = copy.deepcopy(expected); r['ordinate_panels'][0]['N'] = False; changes.append(r)
        r = copy.deepcopy(expected); r['parent'] = '0'*40; changes.append(r)
        r = copy.deepcopy(expected); r['constants']['rho'] = '7/12'; changes.append(r)
        r = copy.deepcopy(expected); r['sharp_count_example']['clean_G'] = 4; changes.append(r)
        r = copy.deepcopy(expected); r['dyadic_schedules'].pop(); changes.append(r)
        prefix = [sys.executable, '-I', '-S', '-B']
        if sys.flags.optimize:
            prefix.append('-O')
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)/'candidate.json'
            command = prefix+[str(ROOT/'check.py'), '--check', str(p)]
            p.write_text(json.dumps(expected), encoding='utf-8')
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
            for j, obj in enumerate(changes):
                p.write_text(json.dumps(obj), encoding='utf-8')
                with self.subTest(case=j):
                    run = subprocess.run(command, capture_output=True, text=True)
                    self.assertNotEqual(run.returncode, 0)
                    self.assertIn('REJECT:', run.stderr)
            p.write_text('{"schema":"BUB26-v1","schema":"BUB26-v1"}', encoding='utf-8')
            run = subprocess.run(command, capture_output=True, text=True)
            self.assertNotEqual(run.returncode,0)
            self.assertIn('duplicate JSON key', run.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
