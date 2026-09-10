#!/usr/bin/env python3
"""Small exact tests and altered-receipt refusals; no network or external packages."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as F
import check


class CheckerTests(unittest.TestCase):
    def test_interval_arithmetic(self):
        check.self_tests()

    def test_quadrature_normalization(self):
        result = check.algebra_checks()
        self.assertEqual(result['quadrature'][0]['polynomial_ascending'], ['-2/5','1'])
        self.assertEqual(result['quadrature'][1]['polynomial_ascending'], ['4/105','-2/3','1'])
        self.assertEqual(result['quadrature'][0]['branching_rate'], '31/80')

    def test_refuse_invalid_domains(self):
        with self.assertRaises(ArithmeticError):
            check.sqrt_i(check.I.point(-1))
        with self.assertRaises(ArithmeticError):
            check.log_i(check.I.point(0))
        with self.assertRaises(ArithmeticError):
            check.phase_certificate(99)
        with self.assertRaises(ZeroDivisionError):
            check.I(-10,10).inv()
        with self.assertRaises(TypeError):
            check.as_i(0.1)

    def test_tail_length_consistency(self):
        a = check.phase_certificate(320)['phase_derivative']
        b = check.phase_certificate(400)['phase_derivative']
        self.assertLessEqual(max(int(a['lo_integer']),int(b['lo_integer'])),
                             min(int(a['hi_integer']),int(b['hi_integer'])))

    def test_receipt_and_mutations(self):
        original = check.build()
        script = Path(check.__file__).resolve()
        cases = [original]
        for key in ('rh', 'sign', 'constant'):
            obj = copy.deepcopy(original)
            if key == 'rh':
                obj['rh_proved'] = True
            elif key == 'sign':
                obj['phase']['phase_derivative']['lo_integer'] = '1'
            else:
                obj['algebra']['quadrature'][0]['d'] = '1/100'
            cases.append(obj)
        with tempfile.TemporaryDirectory() as tmp:
            for i,obj in enumerate(cases):
                path = Path(tmp)/f'case{i}.json'
                path.write_text(json.dumps(obj),encoding='utf-8')
                p = subprocess.run([sys.executable,*(['-O'] if not __debug__ else []),
                                    str(script),'--verify',str(path)],capture_output=True,text=True)
                self.assertEqual(p.returncode == 0, i == 0, p.stdout+p.stderr)


if __name__ == '__main__':
    unittest.main()
