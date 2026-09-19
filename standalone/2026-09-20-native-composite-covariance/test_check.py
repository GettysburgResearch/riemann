"""Bounded exact tests. These do not verify the infinite theorem."""
from __future__ import annotations
import copy
from fractions import Fraction as F
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import check as c


def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)), F())


def finite_T(P, k):
    return P[k] / (k+1) - sum((P[j] / (j*(j+1)) for j in range(k+1,len(P))), F())


def G_upper(d):
    z = F(1)
    for p,_ in c.factors(d):
        t = F(c.root(c.SCALE**3//(p*p),3)+1,c.SCALE)
        z /= 1-t
    return z


class Checks(unittest.TestCase):
    def test_01_roots_and_primitive(self):
        for degree in (3,11):
            for n in range(1000):
                r=c.root(n,degree)
                self.assertLessEqual(r**degree,n)
                self.assertGreater((r+1)**degree,n)
        mu=c.mobius_sieve(2048)
        for n in range(1,2049):
            self.assertEqual(mu[n],c.mobius_trial(n))
            self.assertEqual(sum(mu[d] for d in c.divisors(n)),int(n==1))

    def test_02_cubic_native_bound(self):
        m=energy=F()
        mu=c.mobius_sieve(512)
        for n in range(1,513):
            m+=F(mu[n],n);energy+=m*m
            self.assertLessEqual(abs(m),1)
            self.assertLessEqual(n*abs(m)**3,9*energy)

    def test_03_smooth_deletion(self):
        for d in (1,2,6,10,30,42):
            for n in range(1,65):
                md=sum((F(c.mobius_trial(k),k) for k in range(1,n+1) if c.gcd(k,d)==1),F())
                rhs=F()
                for h in range(1,n+1):
                    if all(d%p==0 for p,_ in c.factors(h)):
                        rhs+=sum((F(c.mobius_trial(k),k) for k in range(1,n//h+1)),F())/h
                self.assertEqual(md,rhs)

    def test_04_native_U_and_composite_amplitudes(self):
        for Y in (2,3,7,15,31):
            source,energy=c.completion(Y)
            amps,U,_,_=c.amplitudes(source)
            for d in range(1,len(source)):
                self.assertLessEqual(abs(U[d])**3*d*d,16**3*energy*G_upper(d)**3/Y)
            for q, a in amps.items():
                W=G_upper(q)**2
                for p,e in c.factors(q):
                    t=F(c.root(c.SCALE**3//(p*p),3)+1,c.SCALE)
                    W*=e+1+e*t
                self.assertLessEqual(abs(a)**3*q*q,256**3*(energy/Y)**2*W**3)
        src,_=c.completion(7); amps,U,_,_=c.amplitudes(src)
        self.assertEqual(amps[6],2*U[2]*U[3]-2*U[6]*(U[2]+U[3])+U[6]**2)
        self.assertEqual(amps[6],F(377,1260))
        self.assertNotEqual(amps[6],amps[2]*amps[3])
        self.assertGreater(amps[4],0)

    def test_05_valuation_threshold(self):
        for a in range(1,9):
            for i in range(12):
                for j in range(12):
                    x=sum(i>=u and j>=a-u for u in range(a+1))
                    x-=sum(i>=u and j>=a+1-u for u in range(1,a+1))
                    self.assertEqual(x,int(i+j>=a))

    def test_06_ramanujan_variance_and_difference(self):
        for q in range(2,81):
            r=[c.R(q,k) for k in range(q)]
            self.assertEqual(sum(r),0)
            self.assertEqual(sum(x*x for x in r)/q,F(c.jordan2(q),12))
            for k in range(1,q+1):
                ram=sum(d*c.mobius_trial(q//d) for d in c.divisors(c.gcd(q,k)))
                self.assertEqual(c.R(q,k)-c.R(q,k-1),ram)

    def test_07_tail_isometry(self):
        for values in itertools.product((-1,0,1),repeat=5):
            P=[F(0)]+list(map(F,values))
            for b in (1,2,3):
                lhs=sum(finite_T(P,k)**2 for k in range(b,len(P)))
                mean=sum((P[k]/(k*(k+1)) for k in range(b,len(P))),F())
                rhs=sum((P[k]**2/(k*(k+1)) for k in range(b,len(P))),F())-b*mean**2
                self.assertEqual(lhs,rhs)
                self.assertGreaterEqual(lhs,0)

    def test_08_activation_commutator(self):
        P=[F(0),F(1),F(-2),F(4),F(-1),F(3)]
        for K in range(2,len(P)):
            AP=[a if k>=K else F() for k,a in enumerate(P)]
            for k in range(1,len(P)):
                right=(finite_T(P,k) if k>=K else F())
                right-=sum(((int(j>=K)-int(k>=K))*P[j]/(j*(j+1))
                            for j in range(k+1,len(P))),F())
                self.assertEqual(finite_T(AP,k),right)
        AP=[a if k>=3 else F() for k,a in enumerate(P)]
        self.assertNotEqual(finite_T(AP,1),0)

    def test_09_rounding_logs_harmonics(self):
        for n in (1,2,3,5,7,11,97):
            lo,hi=c.log_iv(n)
            e=n.bit_length()-1;x=F(n,1<<e)
            # Longer positive series gives an independently chosen truncation.
            def long_series(x):
                z=(x-1)/(x+1)
                return 2*sum((z**(2*j+1)/(2*j+1) for j in range(120)),F())
            value=long_series(x)+e*long_series(F(2))
            self.assertLessEqual(F(lo,c.SCALE),value)
            self.assertLessEqual(value,F(hi,c.SCALE))
        H,other=c.harmonics(64,{97})
        for n in range(65):self.assertTrue(c.contains(H[n],harmonic(n)))
        self.assertTrue(c.contains(other[97],harmonic(97)))
        for a in (F(-7,3),F(0),F(11,7)):
            for b in (F(-9,5),F(0),F(13,17)):
                self.assertTrue(c.contains(c.mul(c.rational(a),c.rational(b)),a*b))

    def test_10_farey_row_bound(self):
        for Q in range(2,14):
            points=sorted({F(a,q) for q in range(2,Q+1) for a in range(1,q) if c.gcd(a,q)==1})
            bound=Q*Q*harmonic(Q*Q)
            for x in points:
                row=F()
                for y in points:
                    if x!=y:
                        d=min(abs(x-y),1-abs(x-y))
                        self.assertGreaterEqual(d,F(1,Q*Q))
                        row+=1/(2*d)
                self.assertLessEqual(row,bound)

    def test_11_exact_native_full_decomposition(self):
        report=c.produce([7,15])
        for p in report['panels']:
            self.assertEqual(p['annular_cells'],p['B']-p['Y'])
            corr=p['first_activation_correction']
            self.assertFalse(int(corr['lower'])<=0<=int(corr['upper']))
            cross=p['twice_signed_cross_terms']['2,3']
            self.assertGreater(int(cross['lower']),0) # native positive covariance
        mutations=[]
        a=copy.deepcopy(report); a['RH_proved']=True;mutations.append(a)
        a=copy.deepcopy(report); a['schema']=True;mutations.append(a)
        a=copy.deepcopy(report); a['panels'][0]['annular_cells']-=1;mutations.append(a)
        a=copy.deepcopy(report); del a['panels'][0]['twice_signed_cross_terms']['2,3'];mutations.append(a)
        a=copy.deepcopy(report); a['panels'][0]['first_activation_correction']['lower']='0';mutations.append(a)
        for a in mutations:self.assertFalse(c.same_types(a,report))
        with self.assertRaises(ValueError):json.loads('{"x":1,"x":2}',object_pairs_hook=c.reject_duplicates)

    def test_12_real_cli_refusal(self):
        command=[sys.executable,'-B']
        if sys.flags.optimize:command.append('-O')
        command.append(str(Path(c.__file__).resolve()))
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'report.json'
            run=subprocess.run(command+['--write',str(p),'--cutoffs','7'],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            run=subprocess.run(command+['--check',str(p),'--cutoffs','7'],capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            data=c.read_json(p);data['panels'][0]['native_F_increment']['lower']='0'
            p.write_bytes(c.canonical(data))
            run=subprocess.run(command+['--check',str(p),'--cutoffs','7'],capture_output=True,text=True)
            self.assertNotEqual(run.returncode,0)
            self.assertIn('report differs from full reconstruction',run.stderr)


if __name__=='__main__':unittest.main()
