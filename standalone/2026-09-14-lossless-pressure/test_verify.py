"""Tests for the new arithmetic, not a replacement for the pressure search."""
import copy
import importlib.util
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('lossless_verify', ROOT/'verify.py')
v = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = v
spec.loader.exec_module(v)


class Tests(unittest.TestCase):
    def test_complete_reconstruction(self):
        self.assertEqual(v.run(), json.loads((ROOT/'results.json').read_text()))

    def test_alternative_series_lengths(self):
        pi, c, A = v.constants(30)
        pi0, c0, A0 = v.constants(26)
        for fine, coarse in [(pi,pi0),(c,c0),(A,A0)]:
            self.assertGreaterEqual(fine.lo,coarse.lo)
            self.assertLessEqual(fine.hi,coarse.hi)
        self.assertEqual(v.run(30)['new_bound_rational'], v.run()['new_bound_rational'])

    def test_wrong_majorant_rejected(self):
        S = F(85368367,1250000000)
        with self.assertRaises(ValueError):
            v.majorant(S, F(7,5))
        with self.assertRaises(ValueError):
            v.majorant(S, F(2))

    def test_changed_capacity_rejected(self):
        d = copy.deepcopy(v.read_inputs())
        d['pairs'][0][2] += 1
        with self.assertRaises(ValueError):
            v.capacities(d)

    def test_partition_coverage_and_separation(self):
        # Finite implementation check; the all-size argument is in PROOF.md.
        alphabet = [F(0),F(1,5),F(4,5),F(6,5)]
        for gaps in itertools.product(alphabet, repeat=6):
            points = [F(0)]
            for g in gaps:
                points.append(points[-1]+g)
            r, pairs = v.partition(points)
            used = r+[i for pair in pairs for i in pair]
            self.assertEqual(sorted(used),list(range(len(points))))
            self.assertTrue(all(points[j]-points[i] < F(4,5) for i,j in pairs))
            self.assertTrue(all(points[j]-points[i] >= F(4,5) for i,j in zip(r,r[1:])))

    def test_clipping_is_not_removed_for_arbitrary_gram(self):
        # A 3x3 all-ones Gram: eigenvalues 3,0,0; Phi trace=5, energy=6.
        phi = lambda x: (x-1)**2 if x <= 2 else 2*x-3
        self.assertEqual(sum(phi(x) for x in [3,0,0]),5)
        self.assertEqual(sum((x-1)**2 for x in [3,0,0]),6)

    def test_changed_record_refused_by_cli(self):
        d = json.loads((ROOT/'results.json').read_text())
        d['new_bound_rational'] = '1'
        with tempfile.TemporaryDirectory() as td:
            target = Path(td)/'bad.json'
            target.write_text(json.dumps(d))
            flags = ['-I'] + (['-O'] if sys.flags.optimize else [])
            p = subprocess.run([sys.executable,*flags,str(ROOT/'verify.py'),'--check',str(target)],
                               capture_output=True,text=True,check=False)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('Saved result differs',p.stderr)


if __name__ == '__main__':
    unittest.main(verbosity=2)
