"""Small deterministic regressions; acceptance survives python -O."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
import algebra
from check import canonical, read_strict, finite_constants, require
from exact import S, log_int, intersect, rat, root4_int, inv, mul, decode

HERE = Path(__file__).resolve().parent

class Tests(unittest.TestCase):
    def test_exact_log_normalization(self):
        self.assertEqual(log_int(1), (0, 0))
        lo, hi = log_int(2)
        self.assertGreater(lo, S*69//100)
        self.assertLess(hi, S*70//100)
        for n in (2, 3, 5, 17, 257):
            a = log_int(n)
            b = log_int(n*n)
            self.assertTrue(intersect((2*a[0], 2*a[1]), b))

    def test_exact_fourth_root(self):
        self.assertEqual(root4_int(16), (2*S, 2*S))
        a = root4_int(7)
        self.assertLessEqual(a[0]**4, 7*S**4)
        self.assertGreaterEqual(a[1]**4, 7*S**4)
        self.assertTrue(intersect(mul(a, inv(a)), rat(1)))

    def test_algebra_replay(self):
        self.assertEqual(algebra.tests(), json.loads((HERE/'algebra_result.json').read_text()))

    def test_constants_replay(self):
        r = read_strict(HERE/'result.json')
        for row in r['stages']:
            got = finite_constants(row['Y']+1)
            for k, v in got.items():
                self.assertEqual(canonical(row[k]), canonical(v))

    def test_mutated_reports(self):
        original = read_strict(HERE/'result.json')
        frozen = canonical(original)
        variants = []
        for key in ('C_prime','C_powers','I','A_output','damping','positive_budget'):
            x = copy.deepcopy(original)
            x['stages'][-1][key][0] += S
            variants.append(x)
        for value in (True, 255.0, '255'):
            x = copy.deepcopy(original)
            x['stages'][-1]['Y'] = value
            variants.append(x)
        x = copy.deepcopy(original)
        x['control']['rejected'] = False
        variants.append(x)
        for bad in variants:
            with self.assertRaises(ValueError):
                require(canonical(bad) == frozen, 'changed certificate')
        self.assertEqual(len(variants), 10)

    def test_duplicate_and_interval_types(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'bad.json'
            p.write_text('{"x":1,"x":2}')
            with self.assertRaises(ValueError):
                read_strict(p)
        for v in ([True, 2], [1.0, 2], [3, 2], ['1', 2]):
            with self.assertRaises(ValueError):
                decode(v)

    def test_non_native_countercontrol(self):
        c = read_strict(HERE/'result.json')['control']
        self.assertGreater(c['C_prime'][0], c['native_bound_without_defect'][1])
        # The stronger positive-part budget also fails for this source.
        r = read_strict(HERE/'result.json')['stages'][-1]
        self.assertGreater(c['C_prime'][0], r['positive_budget'][1])

    def test_wrong_inert_sign_and_endpoint(self):
        # nu=1+2*T^2 gives higher-power logarithmic tail -4*T^2.
        ap, bp = algebra.curve_trace(17, 5), 5
        self.assertEqual(ap, 0)
        true_square = ap*ap-2*bp
        with self.assertRaises(ValueError):
            algebra.require(true_square == 2*bp, 'wrong inert square sign')
        with self.assertRaises(ValueError):
            algebra.curve_trace(17, 17)
        base = [0]+[1]*10
        nu = algebra.inverse(base)
        c = [nu[n] if n<=2 else 0 for n in range(11)]
        v = algebra.sub([2*x for x in c], algebra.conv(base, algebra.conv(c,c)))
        self.assertEqual(v[1:9], nu[1:9])
        self.assertNotEqual(v[9], nu[9])

if __name__ == '__main__':
    unittest.main()
