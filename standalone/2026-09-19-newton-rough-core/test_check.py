"""Bounded regression tests. Infinite estimates are in PROOF.md."""
import copy
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import check as m

class Tests(unittest.TestCase):
    def test_signed_rounding(self):
        for num in range(-9,10):
            for den in range(1,17):
                a=m.enclosure(F(num,den))
                self.assertLessEqual(F(a[0],m.S),F(num,den))
                self.assertGreaterEqual(F(a[1],m.S),F(num,den))
                b=m.scale(a,-7,3)
                self.assertLessEqual(F(b[0],m.S),F(-7*num,3*den))
                self.assertGreaterEqual(F(b[1],m.S),F(-7*num,3*den))

    def test_log_enclosures(self):
        for n in range(1,65):
            k=n.bit_length()-1;t=1<<k
            l2,u2=m.log_series(F(1,3),72)
            lo,hi=m.log_series(F(n-t,n+t),72)
            lo+=k*l2;hi+=k*u2
            a=m.log_bounds(n)
            self.assertLessEqual(F(a[0],m.S),lo)
            self.assertGreaterEqual(F(a[1],m.S),hi)

    def test_harmonic_enclosures(self):
        lo,hi=m.harmonic(128);q=F(0)
        for k in range(1,129):
            q+=F(1,k)
            self.assertLessEqual(F(lo[k],m.S),q)
            self.assertGreaterEqual(F(hi[k],m.S),q)

    def test_complete_small_newton_prefixes(self):
        for y in range(1,25):
            B,mu,prefix,c,z,v=m.exact_source(y)
            self.assertTrue(all(v[n]==mu[n] for n in range(1,B+1)))
            self.assertLessEqual(max(c),2*y)

    def test_zero_and_nonzero_collars(self):
        for y in (15,95):
            c=m.clipped(m.sieve(y))
            self.assertEqual(sum((a/n for n,a in c.items()),F(0)),0)
            self.assertLessEqual(max(abs(v) for v in c.values()),3)
        self.assertEqual(max(m.clipped(m.sieve(15))),16)
        self.assertGreater(max(m.clipped(m.sieve(95))),96)

    def test_parity_not_radical(self):
        self.assertEqual(m.rough_core(12,frozenset()),3)
        self.assertEqual(m.rough_core(18,frozenset()),2)
        self.assertEqual(m.rough_core(72,frozenset({2})),1)
        self.assertEqual(m.rough_core(72,frozenset({3})),2)

    def test_recorded_strict_controls(self):
        data=m.load_strict(Path(__file__).with_name('result.json'))
        p=data['panels']
        self.assertGreater(int(p[1]['partitions'][0]['within_block_off_diagonal']['lo_numerator']),0)
        self.assertGreater(int(p[2]['partitions'][2]['block_energy']['lo_numerator']),int(p[2]['partitions'][1]['block_energy']['hi_numerator']))
        self.assertGreater(int(p[-1]['partitions'][0]['cross_block_covariance']['lo_numerator']),0)
        self.assertLess(int(data['checks']['complete_G_2_4_enclosure']['hi_numerator']),0)
        self.assertEqual(data['checks']['fake_Y128_entire_large_interval_checks'],2049)
        self.assertEqual(p[-1]['source_input_energy']['lo_numerator'],str(15*m.S*m.S))

    def test_duplicate_key_refusal(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/'bad.json';p.write_text('{"x": 1, "x": 2}')
            with self.assertRaisesRegex(ValueError,'duplicate'):
                m.load_strict(p)

    def test_real_cli_resealed_mutation_refusal(self):
        here=Path(__file__).parent
        with tempfile.TemporaryDirectory() as td:
            td=Path(td)
            (td/'check.py').write_bytes((here/'check.py').read_bytes())
            data=m.load_strict(here/'result.json')
            data['panels'][2]['partitions'][1]['groups']+=1
            (td/'changed.json').write_text(m.canonical(data))
            p=subprocess.run([sys.executable,'-S','-B',str(td/'check.py'),'--check',str(td/'changed.json')],cwd=td,capture_output=True,text=True,timeout=60)
            self.assertNotEqual(p.returncode,0)
            self.assertIn('result mismatch',p.stderr)

if __name__=='__main__':unittest.main()
