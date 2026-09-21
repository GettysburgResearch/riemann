"""Exact bounded tests; no finite test proves the unbounded native estimate."""
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import check as d


def divisors(n):
    return [k for k in range(1, n+1) if n % k == 0]


def modes(c):
    z = {}
    for r, a in c.items():
        for s, b in c.items():
            z[r*s] = z.get(r*s,F(0)) + a*b
    amplitudes = {}
    for n, value in z.items():
        for q in divisors(n):
            if q > 1:
                amplitudes[q] = amplitudes.get(q,F(0)) + value/n
    return z, amplitudes


def ramanujan_saw(q, k):
    return sum((F(d.primitive_trial(q//r)) * (F(r-1,2) - k%r)
                for r in divisors(q)), F(0))


class ExactChecks(unittest.TestCase):
    def test_seed_and_divisor_inverse(self):
        a = d.mobius(4095)
        self.assertEqual(a, [d.primitive_trial(k) for k in range(4096)])
        for n in range(1, 513):
            self.assertEqual(sum(a[k] for k in divisors(n)), int(n==1))

    def test_recurrence_all_small_future_arguments(self):
        M, _, _, _ = d.mertens_solver(31)
        actual = d.prefix(d.mobius(4095))
        for n in range(1, 4096):
            self.assertEqual(M(n), actual[n])

    def test_mesh_every_path(self):
        for steps in itertools.product((-1,0,1), repeat=7):
            values=d.prefix([0]+list(steps))
            exact=sum((F(values[k]**2,k*(k+1)) for k in range(1,8)),F(0))
            for points in ([1,7],[1,3,5,7],list(range(1,8))):
                panel=d.energy_from_samples(points,[values[k] for k in points])
                lo,hi=panel['energy_enclosure']
                self.assertLessEqual(F(lo,d.SCALE),exact)
                self.assertLessEqual(exact,F(hi,d.SCALE))
                self.assertEqual(panel['covered_integer_cells'],7)

    def test_unseen_tent_needs_error_budget(self):
        values=[0,0,1,2,1,0]
        panel=d.energy_from_samples([1,5],[0,0])
        exact=sum((F(values[k]**2,k*(k+1)) for k in range(1,6)),F(0))
        self.assertEqual(panel['sample_energy'],[0,0])
        self.assertGreater(exact,0)
        self.assertLessEqual(exact,F(panel['energy_enclosure'][1],d.SCALE))

    def test_mesh_quadratic_residues_and_endpoints(self):
        for lo in range(1,32):
            for last in range(lo,lo+80):
                pts=d.square_mesh(lo,last)
                self.assertEqual((pts[0],pts[-1]),(lo,last))
                self.assertEqual(pts,sorted(set(pts)))
        for j in range(4096):
            t,r=divmod(j,16)
            self.assertEqual(j*j//16,16*t*t+2*r*t+r*r//16)

    def test_full_rational_fourier_identity(self):
        for Y in range(1,13):
            mu=d.mobius((Y+1)**2)
            c={n:F(mu[n]) for n in range(1,Y+1) if mu[n]}
            c[Y+1]=-(Y+1)*sum((c[n]/n for n in c),F(0))
            z,amp=modes(c); S=sum(c.values(),F(0))
            self.assertEqual(sum((c[n]/n for n in c),F(0)),0)
            for k in range(1,(Y+1)**2):
                direct=2*sum((v for n,v in c.items() if n<=k),F(0))
                direct-=sum((v*(k//n) for n,v in z.items()),F(0))
                spectral=2*sum((v for n,v in c.items() if n<=k),F(0))+S*S/2
                spectral-=sum((v*ramanujan_saw(q,k) for q,v in amp.items()),F(0))
                self.assertEqual(direct,spectral)
                self.assertEqual(direct,sum(mu[1:k+1]))
            for p in range(2,Y+2):
                if d.primitive_trial(p)==-1 and len(divisors(p))==2:
                    T=sum((v/n for n,v in c.items() if n%p==0),F(0))
                    self.assertEqual(amp.get(p,F(0)),-T*T)

    def test_native_rough_sum_and_crossing_amplitudes(self):
        mu=d.mobius(128)
        for p in (2,3,5,7,11,13,17,19,23,29,31):
            value=F(0)
            for n in range(1,129):
                if n%p:value+=F(mu[n],n)
                self.assertLessEqual(abs(value),1)
        m=F(0)
        crossings=0
        for y in range(1,65):
            before=m;m+=F(mu[y],y)
            if y>=2 and mu[y] and before*m<=0:
                crossings+=1
                c={n:F(mu[n]) for n in range(1,y+1) if mu[n]}
                c[y+1]=-(y+1)*m
                for p in range(2,y+2):
                    if len(divisors(p))!=2:continue
                    u=sum((v/n for n,v in c.items() if n%p==0),F(0))
                    self.assertLessEqual(abs(u),F(3,p))
        self.assertGreater(crossings,0)

    def test_prime_power_is_not_prime_mode(self):
        _,amp=modes({1:F(1),2:F(-2)})
        self.assertEqual(amp[2],-1)
        self.assertEqual(amp[4],1)
        # Distinct quadratic phases are not orthogonal: 1, i, 1, i.
        self.assertEqual([n*n%4 for n in range(4)],[0,1,0,1])

    def test_bad_input_rejected(self):
        for points, values in (([1,1],[0,0]),([2,1],[0,0]),([1,3],[0,3]),([1],[True])):
            with self.assertRaises(ValueError):d.energy_from_samples(points,values)
        with self.assertRaises(ValueError):json.loads('{"x":1,"x":2}',object_pairs_hook=d.reject_duplicates)
        for bad in (0,-1,4096,True):
            with self.assertRaises(ValueError):d.run(bad)

    def test_real_cli_corrupted_report_refusal(self):
        script=Path(d.__file__).resolve()
        with tempfile.TemporaryDirectory() as td:
            report=Path(td)/'result.json'
            base=[sys.executable,'-B',str(script),'--Y','31']
            subprocess.run(base+['--write',str(report)],check=True,capture_output=True)
            subprocess.run(base+['--check',str(report)],check=True,capture_output=True)
            data=json.loads(report.read_text());data['result']['sample_count']+=1
            report.write_text(json.dumps(data))
            failed=subprocess.run(base+['--check',str(report)],capture_output=True)
            self.assertNotEqual(failed.returncode,0)

if __name__=='__main__':unittest.main()
