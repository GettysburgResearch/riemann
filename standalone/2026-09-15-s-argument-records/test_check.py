#!/usr/bin/env python3
"""Finite same-author controls; not an independent mathematical review."""
import copy
from fractions import Fraction as Q
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('sarg26_checker', ROOT/'check.py')
c = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = c
spec.loader.exec_module(c)


def contains(a, q):
    return Q(a.lo, c.SCALE) <= q <= Q(a.hi, c.SCALE)


class Checks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = (ROOT/'news.txt').read_text(encoding='utf-8')
        cls.report, cls.jobs = c.reconstruct(cls.text)

    def test_exact_arithmetic(self):
        values = [Q(n, 7) for n in range(-15, 16)]
        for a, b in itertools.product(values, repeat=2):
            for got, exact in ((c.iv(a)+b, a+b), (c.iv(a)-b, a-b), (c.iv(a)*b, a*b)):
                self.assertTrue(contains(got, exact))
            if b:
                self.assertTrue(contains(c.iv(a)/b, a/b))
        ranges = [(Q(a, 3), Q(a+2, 3)) for a in (-8, -5, -3, -1, 1, 3, 5, 8)]
        for (a, b), (d, e) in itertools.product(ranges, repeat=2):
            x, y = c.hull(a, b), c.hull(d, e)
            for u, v in itertools.product((a, b), (d, e)):
                for got, exact in ((x+y, u+v), (x-y, u-v), (x*y, u*v)):
                    self.assertTrue(contains(got, exact))
                if not d <= 0 <= e:
                    self.assertTrue(contains(x/y, u/v))
        for bad in (0.1, True, False):
            with self.assertRaises(ValueError):
                c.iv(bad)
        with self.assertRaises(ValueError):
            c.iv(1)/c.hull(-1, 1)

    def test_separate_rational_series(self):
        # Same classical identities, but Fraction arithmetic and another truncation.
        def atan(q, n=100):
            s = sum(((-1)**j*q**(2*j+1)/Q(2*j+1) for j in range(n)), Q(0))
            tail = q**(2*n+1)/Q(2*n+1)
            return s-tail, s+tail
        a, b = atan(Q(1, 5)), atan(Q(1, 239))
        lo, hi = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
        self.assertTrue(contains(c.pi(), lo) and contains(c.pi(), hi))
        for z in (Q(1, 3), Q(1, 7), Q(1, 11)):
            n = 220
            s = 2*sum((z**(2*j+1)/Q(2*j+1) for j in range(n)), Q(0))
            tail = 2*z**(2*n+1)/Q((2*n+1)) / (1-z*z)
            got = c.atanh2(z)
            self.assertTrue(contains(got, s) and contains(got, s+tail))
        self.assertTrue(contains(c.log_point(Q(1)), Q(0)))

    def test_monotone_defect_controls(self):
        # 448 complete synthetic staircases; the general lemma is proved in prose.
        h = Q(4)
        xs = (Q(1, 2), Q(2), Q(7, 2))
        checked = 0
        for k in range(-3, 4):
            for bits in itertools.product((0, 1), repeat=6):
                left, right = bits[:3], bits[3:]
                im = h*k-sum((b*(h-x) for b, x in zip(left, xs)), Q(0))
                ip = h*k+sum((b*(h-x) for b, x in zip(right, xs)), Q(0))
                B = max(abs(im), abs(ip))
                self.assertGreaterEqual(k, -B/h)
                self.assertLessEqual(k, B/h)
                if B < h:
                    self.assertEqual(k, 0)
                    for b, x in zip(left, xs):
                        if b:
                            self.assertGreaterEqual(x, h-B)
                    for b, x in zip(right, xs):
                        if b:
                            self.assertGreaterEqual(x, h-B)
                checked += 1
        self.assertEqual(checked, 448)

    def test_full_reconstruction_and_jobs(self):
        expected = json.loads((ROOT/'results.json').read_text(encoding='utf-8'), object_pairs_hook=c.unique_object)
        self.assertEqual(c.canonical(self.report), c.canonical(expected))
        self.assertEqual(len(self.jobs), 310)
        self.assertEqual([sum(row[0] == i for row in self.jobs) for i in (1, 2)], [153, 157])
        self.assertFalse(self.report['primitive_z_replayed'])
        self.assertFalse(self.report['record_independently_certified'])
        for row in self.jobs:
            self.assertIsInstance(row[1], str)
            self.assertLess(Q(row[3]), Q(row[4]))
        for r in self.report['records']:
            lo, hi = map(Q, r['compressed']['conditional_complete_core'])
            self.assertLess(lo, -1)
            self.assertGreater(hi, 1)

    def test_bad_inputs(self):
        changes = [
            ('427 Hardy-Z', '426 Hardy-Z'),
            ('-19.9871 -19.8961', '-19.8961 -19.9871'),
            ('-19.9871 -19.8961', '-19.9871 -19.9861'),
            ('8012833507866431746081933196518', '8012833507866431746081933196519'),
            ('I+=.2506382', 'I+=.2506383'),
            ('B=6.1266298', 'B=6.1266296'),
            ('E+=.210', 'E+=.209'),
            ('+0.71e−5,+1.32e−5', '-0.71e−5,+1.32e−5'),
            ('−.3404339,.3042996', '−.0404339,.3042996'),
            ('4.184313<S', '4.184314<S'),
        ]
        exercised = 0
        for old, new in changes:
            self.assertIn(old, self.text)
            with self.subTest(old=old), self.assertRaises(ValueError):
                c.reconstruct(self.text.replace(old, new, 1))
            exercised += 1
        self.assertEqual(exercised, 10)
        model = c.Model(c.parse_news(self.text)[0])
        with self.assertRaises(ValueError):
            model.pair(Q(1), Q(1), True)

    def test_real_cli_acceptance_and_refusals(self):
        # Each interpreter mode really launches pristine and mutated subprocesses.
        flags = ['-I', '-S', '-B'] + (['-'+'O'*sys.flags.optimize] if sys.flags.optimize else [])
        base = [sys.executable, *flags, str(ROOT/'check.py')]
        with tempfile.TemporaryDirectory() as tmp:
            d = Path(tmp)
            def run(extra, code):
                p = subprocess.run(base+extra, capture_output=True, text=True, timeout=30)
                self.assertEqual(p.returncode, code, p.stderr)
                return p
            jobs = d/'jobs.tsv'
            run(['--check', str(ROOT/'results.json'), '--jobs', str(jobs)], 0)
            self.assertEqual(len(jobs.read_text().splitlines()), 311)
            mutations = []
            for key in ('primitive_z_replayed', 'record_independently_certified', 'rh_established'):
                changed = copy.deepcopy(self.report)
                changed[key] = True
                mutations.append(changed)
            changed = copy.deepcopy(self.report)
            changed['records'][0]['conditional_S_record'][0] = '4.3'
            mutations.append(changed)
            changed = copy.deepcopy(self.report)
            changed['compressed_brackets'] = 309
            mutations.append(changed)
            changed = copy.deepcopy(self.report)
            changed['primitive_z_replayed'] = 0  # Python false == 0 must not authenticate.
            mutations.append(changed)
            for i, changed in enumerate(mutations):
                p = d/f'bad{i}.json'
                p.write_text(c.canonical(changed), encoding='utf-8')
                run(['--check', str(p)], 2)
            duplicate = d/'duplicate.json'
            duplicate.write_text('{"schema":0,'+c.canonical(self.report)[1:], encoding='utf-8')
            run(['--check', str(duplicate)], 2)
            refusal = run(['--require-primitive'], 2)
            self.assertIn('not implemented or replayed', refusal.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
