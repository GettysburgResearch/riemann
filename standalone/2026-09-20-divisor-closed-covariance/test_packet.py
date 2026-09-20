"""Small exact tests and negative controls. unittest checks survive -O."""
import copy,json,tempfile,unittest
from fractions import Fraction
from pathlib import Path
from arithmetic import sieve,divisors,residue,near_candidates,completed_source,convolution,strict_read,canonical
from exact import ZERO,S,rat,log_int,intersect
import verify
from harmonic import Gram
ROOT=Path(__file__).parent

def comparable(a,h,x):
    A={n:sum(h.get(d,0)*a.get(n//d,0) for d in verify.divs_of(verify.factor(n))) for n in range(1,x+1)}
    return sum(a.get(m,0)*A[t] for m in range(1,x+1) for t in range(1,x+1) if m%t==0 or t%m==0)

class PacketTests(unittest.TestCase):
    def test_native_closure_every_cutoff_and_prime_selection(self):
        spf,mu,rad,core,primes=sieve(70);a={n:v for n,v in enumerate(mu) if v}
        for h in ({p:1 for p in primes},{p:p for p in primes},{p:1 for p in primes if p>=11}):
            for x in range(1,71):
                rhs=sum(sum(h.get(p,0) for p,e in verify.factor(n)) for n in range(2,x+1) if mu[n] and spf[n]!=n)
                self.assertEqual(comparable(a,h,x),rhs)
    def test_native_old_matched_contained(self):
        _,mu,rad,core,primes=sieve(500)
        for p in primes:
            for n in range(1,500//p+1):
                if mu[n]:self.assertEqual((p*n)%core[p*n],0)
    def test_wrong_source_positive_weights(self):
        self.assertEqual(comparable({1:1,2:-2},{2:1},2),-1)
        self.assertEqual(comparable({1:1,2:1},{2:-1},2),-2)
    def test_zero_cube_and_crossed_endpoint(self):
        _,mu,*_=sieve(150)
        self.assertEqual(sum(mu[2*d] for d in (1,3,5,15)),0)
        # k=7 exceeds p=5: the full fibre's endpoint is beyond t=75.
        full=[7*d for d in (1,3,5,15)]
        self.assertGreater(max(full),75)
        self.assertNotEqual(sum(mu[m] for m in full if m<=75),0)
    def test_general_divisor_defect(self):
        a={1:1,2:-2,3:1,4:3};h={2:2,3:5};x=8
        ds=lambda n:verify.divs_of(verify.factor(n))
        A={n:sum(h.get(d,0)*a.get(n//d,0) for d in ds(n)) for n in range(1,x+1)}
        D={n:sum(a.get(d,0) for d in ds(n)) for n in range(1,x+1)}
        val=sum(A[n]*D[n]+a.get(n,0)*sum(h.get(d,0)*D[n//d] for d in ds(n))-a.get(n,0)*A[n] for n in range(1,x+1))
        self.assertEqual(comparable(a,h,x),val)
    def test_actual_elliptic_good_prime(self):
        p=7;b=(17*17*pow(4,-1,p))%p
        count=1+sum((y*y-x*x*x-b)%p==0 for x in range(p) for y in range(p))
        self.assertEqual(count,3)
        self.assertEqual(comparable({1:1,7:-5},{7:5},7),-20)
        self.assertEqual(-20*(Fraction(1,98)-Fraction(1,128)),Fraction(-75,1568))
    def test_near_generator_all_pairs_no_duplicates(self):
        D=150;divs=divisors(D+8)
        for h in (0,1,3,8):
            got=[(d,e) for e in range(2,D+1) for d,r in near_candidates(e,h,divs)]
            want={(d,e) for e in range(2,D+1) for d in range(1,e) if abs(residue(e,d))<=h}
            self.assertEqual(len(got),len(set(got)));self.assertEqual(set(got),want)
    def test_gram_against_independent_cells(self):
        for b in (2,4,8):
            g=Gram(b,b*b-1,b*b+2)
            for d,e in ((1,3),(2,2),(2,3),(3,5),(b,b+1),(b*b-1,b*b+2)):
                self.assertTrue(intersect(g.pair(d,e),verify.harmonic_entry_direct(d,e,b,b*b-1)))
    def test_above_endpoint_not_deleted(self):
        _,mu,*_=sieve(15);c=completed_source(3,mu);z=convolution(c)
        self.assertEqual(sum((v/d for d,v in z.items()),Fraction()),0)
        self.assertNotEqual(sum((v/d for d,v in z.items() if d<=15),Fraction()),0)
        G=Gram(4,15,max(z));self.assertGreater(G.pair(16,16)[0],0)
    def test_moment_transport_and_source_cap(self):
        for Y in (3,7,15,31):
            _,mu,*_=sieve((Y+1)**2-1);c=completed_source(Y,mu)
            self.assertLessEqual(max(abs(v) for v in c.values()),3)
            self.assertEqual(sum((v/n for n,v in c.items()),Fraction()),0)
    def test_divisor_moment_inequalities(self):
        import math
        def tau_r(n,r):
            v=1
            for p,e in verify.factor(n):v*=math.comb(e+r-1,r-1)
            return v
        for n in range(1,500):
            self.assertLessEqual(tau_r(n,2)**2,tau_r(n,4))
            self.assertLessEqual(tau_r(n,3)**2,tau_r(n,9))
            self.assertLessEqual(tau_r(n,2)*tau_r(n,3),tau_r(n,6))
    def test_complete_lcm_fibres(self):
        from math import lcm
        _,mu,_,_,primes=sieve(50)
        h={p:p for p in primes};A={n:sum(h.get(d,0)*mu[n//d] for d in verify.divs_of(verify.factor(n))) for n in range(1,51)}
        fibres={}
        for m in range(1,51):
            for t in range(1,51):
                n=lcm(m,t)
                if n<=50:fibres[n]=fibres.get(n,0)+mu[m]*A[t]
        self.assertTrue(all(v==0 for v in fibres.values()))
        b=7;X=49;w=lambda n:max(Fraction(0),Fraction(1,max(b,n))-Fraction(1,X))
        old=sum(mu[m]*A[t]*w(max(m,t)) for m in range(1,X) for t in range(1,X))
        new=sum(mu[m]*A[t]*(w(max(m,t))-w(lcm(m,t))) for m in range(1,X) for t in range(1,X))
        self.assertEqual(old,new)
    def test_report_negative_controls(self):
        full=strict_read(ROOT/'reports'/'transport_result.json');base=copy.deepcopy(full);base['stages']=base['stages'][:1]
        verify.verify_transport(base)
        for key in ('P','comparable'):
            bad=copy.deepcopy(base);bad['stages'][0][key]=[0,0]
            with self.assertRaises(ValueError):verify.verify_transport(bad)
        for key in ('near','remaining'):
            bad=copy.deepcopy(base);bad['stages'][0]['panels'][1][key]=[0,0]
            with self.assertRaises(ValueError):verify.verify_transport(bad)
        for value in (3.0,True):
            bad=copy.deepcopy(base);bad['stages'][0]['Y']=value
            with self.assertRaises(ValueError):verify.verify_transport(bad)
        bad=copy.deepcopy(base);bad['stages'][0]['N']+=1
        with self.assertRaises(ValueError):verify.verify_transport(bad)
        bad=copy.deepcopy(base);bad['stages'][0]['P']=[-S*100,S*100]
        with self.assertRaises(ValueError):verify.verify_transport(bad)
        bad=copy.deepcopy(base);bad['stages'][0]['panels'][1]['pairs']+=1
        with self.assertRaises(ValueError):verify.verify_transport(bad)
        bad=copy.deepcopy(base);bad['bits']=float(bad['bits'])
        with self.assertRaises(ValueError):verify.verify_transport(bad)
    def test_duplicate_and_nonfinite_json(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json'
            for txt in ('{"x":1,"x":2}','{"x":NaN}'):
                p.write_text(txt)
                with self.assertRaises(ValueError):strict_read(p)

if __name__=='__main__':unittest.main()
