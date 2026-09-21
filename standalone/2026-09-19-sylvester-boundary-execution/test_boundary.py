#!/usr/bin/env python3
"""Focused algebra, source controls, endpoint and report-adversarial tests."""
import copy
import json
import unittest
from fractions import Fraction
from pathlib import Path
import boundary
import verify
import lfamily

ROOT=Path(__file__).resolve().parent


def divisors(n):return [d for d in range(1,n+1) if n%d==0]


def convolution(a,b,N):
    out=[0]*(N+1)
    for n in range(1,N+1):
        out[n]=sum(a[d]*b[n//d] for d in divisors(n) if d<len(a) and n//d<len(b))
    return out


class BoundaryTests(unittest.TestCase):
    def test_one_and_two_prime_boundary(self):
        mu=boundary.mobius_prefix(256)
        for Y in range(1,17):
            for n in range(2,257):
                primes=sorted(set(verify.factor(n)))
                R=sum(mu[d] for d in divisors(n) if d<=Y)
                for p in primes:
                    m=n
                    while m%p==0:m//=p
                    rhs=sum(mu[d] for d in divisors(m) if Y<p*d and d<=Y)
                    self.assertEqual(R,rhs)
                if len(primes)>=2:
                    p,q=primes[:2];m=n
                    for r in (p,q):
                        while m%r==0:m//=r
                    rhs=sum(mu[d]*(int(d<=Y)-int(p*d<=Y)-int(q*d<=Y)+int(p*q*d<=Y)) for d in divisors(m))
                    self.assertEqual(R,rhs)

    def test_antichain_needs_rough_support(self):
        for Y in range(1,33):
            for p in (2,3,5,7,11):
                ds=[d for d in range(1,Y+1) if p*d>Y and all(q>p for q in verify.factor(d))
                    and len(verify.factor(d))==len(set(verify.factor(d)))]
                self.assertFalse(any(e%d==0 for d in ds for e in ds if e>d))
        # Window alone is not an antichain when small primes are allowed.
        self.assertTrue(Fraction(15,5)<4<8<=15 and 8%4==0)

    def test_convolution_collapse_all_small_prefixes(self):
        for Y in range(1,25):
            labs,rows,_=boundary.native_channels(Y)
            rlabs,rrows,_=verify.reference(Y)
            self.assertEqual(labs,rlabs);self.assertEqual(rows,rrows)

    def test_sharp_squared_endpoint(self):
        for Y in range(1,13):
            b=Y+1;N=b*b
            mu=boundary.mobius_prefix(N);g=mu[:b];one=[0]+[1]*N
            t=convolution(one,g,N);e=[0]+[int(n==1)-t[n] for n in range(1,N+1)]
            ge=convolution(g,e,N)
            Newton=[0]+[(g[n] if n<len(g) else 0)+ge[n] for n in range(1,N+1)]
            self.assertEqual(Newton[1:N],mu[1:N])
            self.assertEqual(mu[N]-Newton[N],e[b]**2)
        self.assertEqual(boundary.mobius_prefix(3)[3]**2,1)  # Y=2 endpoint really fails.

    def test_not_every_multiplicative_squarefree_source_is_native(self):
        Y=15;B=(Y+1)**2-1
        mu=boundary.mobius_prefix(Y)
        fake=[x*(-1 if n and n%2==0 else 1) for n,x in enumerate(mu)]
        self.assertTrue(all(x in (-1,0,1) for x in fake))
        self.assertEqual([x!=0 for x in fake],[x!=0 for x in mu])
        self.assertEqual(sum(fake[d] for d in divisors(2)),2)
        e=[0]*(B+1);e[1]=1
        for r in range(1,Y+1):
            for n in range(r,B+1,r):e[n]-=fake[r]
        # The native low-source vanishing, and hence the stage collapse, is false.
        self.assertEqual(e[2],-2)
        ep=[e[n] if n>=2 and min(verify.factor(n))==2 else 0 for n in range(B+1)]
        self.assertNotEqual(convolution(fake,ep,B)[4],0)

    def test_moment_balance_does_not_restore_inverse_equations(self):
        alpha={1:1,2:-1,3:-1,5:-1,6:-1,10:1,15:1,30:1}
        self.assertEqual(sum(alpha.values()),0)
        self.assertEqual(sum((Fraction(a,n) for n,a in alpha.items()),Fraction()),0)
        self.assertEqual(sum(alpha.get(d,0) for d in divisors(6)),-2)

    def test_gram_simultaneous_jumps_and_interval_endpoints(self):
        for a,b in [({4:2,7:-3,12:1},{4:-1,7:2,15:-4}),({4:1},{8:1}),({}, {4:1})]:
            prod=boundary.gram(a,b,4,16)
            exact=Fraction();va=vb=0
            for k in range(4,16):
                va+=a.get(k,0);vb+=b.get(k,0)
                exact+=Fraction(va*vb,k*(k+1))
            self.assertLessEqual(Fraction(prod[0],boundary.SCALE),exact)
            self.assertLessEqual(exact,Fraction(prod[1],boundary.SCALE))
            sbp=sum((Fraction(n,d) for n,d in verify.jump_terms(a,b,4,16)),Fraction())
            self.assertEqual(sbp,exact)
        with self.assertRaises(ValueError):boundary.gram({16:1},{4:1},4,16)

    def test_report_mutations(self):
        data=json.loads((ROOT/'result.json').read_text());data['panels']=data['panels'][:1]
        verify.verify(data,cutoffs=(3,))
        changes=[
            lambda d:d.update(status='RH PROVED'),
            lambda d:d.update(dyadic_denominator_bits=True),
            lambda d:d['panels'][0].update(B=16),
            lambda d:d['panels'][0]['labels'].__setitem__(1,'5'),
            lambda d:d['panels'][0]['row_sha256'].__setitem__(1,'0'*64),
            lambda d:d['panels'][0]['row_event_counts'].__setitem__(0,True),
            lambda d:d['panels'][0]['gram_upper_triangle'][0].__setitem__(0,False),
            lambda d:d['panels'][0]['gram_upper_triangle'][0].__setitem__(2,'99999999999999999999999999999999'),
            lambda d:d['panels'][0]['means'].__setitem__(0,['0','0']),
            lambda d:d['panels'][0].update(A_output=['0','0']),
            lambda d:d['panels'][0].update(ordered_cross_C=['0','0']),
            lambda d:d['panels'][0].update(unpaid_tail='ignored'),
        ]
        for i,change in enumerate(changes):
            bad=copy.deepcopy(data);change(bad)
            with self.subTest(mutation=i),self.assertRaises((ValueError,KeyError)):
                verify.verify(bad,cutoffs=(3,))

    def test_duplicate_json(self):
        for hook in (boundary.reject_duplicates,verify.no_duplicates):
            with self.assertRaises(ValueError):json.loads('{"x":1,"x":2}',object_pairs_hook=hook)

    def test_positive_native_sector(self):
        labels,rows,_=verify.reference(255)
        ps=[193,197,199];qs=[211,223,227,229]
        for p in ps:
            row=rows[labels.index(str(p))]
            self.assertTrue(all(v==1 for v in row.values()))
            for q in qs:self.assertEqual(row[p*q],1)
        # Different pivot and cofactor primes give coprime positive semiprimes.
        import math
        self.assertEqual(math.gcd(193*211,197*223),1)

    def test_sylvester_projector_and_admissibility_controls(self):
        data=lfamily.fixture()
        self.assertEqual(len(data['family_below_500']),14)
        for n in (1,2,4,8):
            with self.assertRaises(ValueError):lfamily.projector(n,1)
        for p in (13,25,35):
            with self.assertRaises(ValueError):lfamily.family_row(p)
        for z in data['family_below_500']:
            if z['q']==67:self.assertEqual(z['eta_q'],'not determined here')
        with self.assertRaises(ValueError):lfamily.fermat(13,lfamily.omega+1,lfamily.K(1))

    def test_rank_deflation_is_subtraction_not_addition(self):
        raw=lfamily.imaginary_pick(1,1,[Fraction(1,2)])[0][0]
        self.assertEqual(raw,Fraction(4,3));self.assertEqual(raw-4,Fraction(-8,3))
        self.assertGreater(raw+4,0)
        self.assertEqual(lfamily.imaginary_pick(1,-1,[Fraction(1,2)])[0][0]-4,Fraction(8,5))
        with self.assertRaises(ValueError):lfamily.imaginary_pick(1,1,[1])

if __name__=='__main__':unittest.main()
