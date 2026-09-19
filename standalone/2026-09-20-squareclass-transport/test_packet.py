"""Regression and adversarial tests; run normally and with -O."""
import copy
import itertools
import json
import tempfile
import unittest
from fractions import Fraction as F
from pathlib import Path
import family
import transport as t
import verify as v
from exact import S, ZERO, add, scale, log_int, intersect

ROOT=Path(__file__).resolve().parent


def character_vectors(y, bank, weighted=True):
    b,X=y+1,(y+1)**2
    sp,mu,ps=t.sieve(X-1)
    outside=[p for p in ps if p not in bank]
    totals={p:F(0) for p in ps}
    for sig in itertools.product((-1,1),repeat=len(outside)):
        ch=dict(zip(outside,sig));chi=[1]*X;M=[0]*X
        for n in range(2,X):chi[n]=chi[n//sp[n]]*ch.get(sp[n],1)
        for n in range(1,X):M[n]=M[n-1]+mu[n]*chi[n]
        for p in ps:
            totals[p]+=sum((F(M[k]*M[k//p],k*(k+1)) for k in range(b,X)),F(0))*(ch.get(p,1) if weighted else 1)
    return {p:x/(1<<len(outside)) for p,x in totals.items()}


class PacketTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=t.build()
        cls.family=family.build()

    def test_three_case_fibres(self):
        for y in (3,7):
            sp,mu,ps=t.sieve((y+1)**2-1)
            for bank in t.BANKS:
                direct=t.sector(y,bank,sp,mu,ps);other,count=v.fibres(y,bank,mu,ps)
                self.assertEqual(direct['triples'],count)
                for k,x in other.items():self.assertEqual(direct[k],x)

    def test_exact_character_average(self):
        for bank in ((),(2,3)):
            avg=character_vectors(3,bank)
            sp,mu,ps=t.sieve(15);vals={p:F(0) for p in ps}
            def core(n):
                ans=1
                for p in ps:
                    e=0
                    while n%p==0:n//=p;e+=1
                    if p not in bank and e%2:ans*=p
                return ans
            for p in ps:
                for n in range(1,15//p+1):
                    for m in range(1,16):
                        if core(m)==core(p*n):
                            h=max(4,m,p*n)
                            vals[p]+=mu[m]*mu[n]*(F(1,h)-F(1,16))
            self.assertEqual(vals,avg)

    def test_twisting_prime_weight_is_essential(self):
        self.assertNotEqual(character_vectors(3,()),character_vectors(3,(),False))

    def test_parity_is_not_radical(self):
        # p=2,n=2,m=1 contributes through core(4)=1, not rad(4)=2.
        self.assertEqual((-1)*(F(1,4)-F(1,16)),F(-3,16))
        row=self.report['stages'][0]
        self.assertLess(row['empty']['repeated'][0],row['empty']['diagonal'][0])
        self.assertGreater(row['empty']['repeated'][0],0)

    def test_empty_sector_sign_and_budget(self):
        for row in self.report['stages']:
            e=row['empty']
            self.assertLess(e['matched'][1],0)
            self.assertLessEqual(-e['matched'][0],e['bound'][1])
            self.assertEqual(row['sectors'][0]['positive_pairs'],ZERO)

    def test_adversarial_report_mutations(self):
        changes=[('P',0),('I',1),('u_prefix',0),('u_annulus',1),('A_output',0)]
        for key,end in changes:
            bad=copy.deepcopy(self.report)
            bad['stages'][0][key]=list(bad['stages'][0][key])
            bad['stages'][0][key][end]+=S
            with self.assertRaises(ValueError):v.verify(json.loads(t.canonical(bad)))
        for key in ('matched','remainder','positive_pairs','negative_pairs','envelope'):
            bad=copy.deepcopy(self.report);item=bad['stages'][0]['sectors'][0]
            item[key]=[S*10000,S*10000]
            with self.assertRaises(ValueError):v.verify(json.loads(t.canonical(bad)))
        bad=copy.deepcopy(self.report);bad['stages'][0]['sectors'][0]['triples']+=1
        with self.assertRaises(ValueError):v.verify(json.loads(t.canonical(bad)))
        bad=copy.deepcopy(self.report);bad['stages'][0]['N']+=1
        with self.assertRaises(ValueError):v.verify(json.loads(t.canonical(bad)))

    def test_numeric_aliases_rejected(self):
        for value in (True,3.0):
            bad=copy.deepcopy(self.report);bad['stages'][0]['Y']=value
            with self.assertRaises(ValueError):v.verify(json.loads(t.canonical(bad)))

    def test_duplicate_keys_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'bad.json';p.write_text('{"schema":1,"schema":2}')
            with self.assertRaises(ValueError):t.strict_read(p)
            with self.assertRaises(ValueError):v.load(p)

    def test_squarefree_sign_obstruction(self):
        c=self.report['squarefree_sign_control']
        self.assertLess(c['remainder'][1],-100000*S)
        self.assertEqual(c['matched_empty'],self.report['stages'][-1]['empty']['matched'])

    def test_family_parseval_and_restore(self):
        r=self.family
        self.assertEqual(r['average'],r['parseval'])
        self.assertEqual(r['signatures'],256)
        self.assertEqual(r['coefficient_comparisons'],1048320)
        self.assertEqual(r['mixed_square_index'],3025)
        self.assertLessEqual(F(*r['native']),F(*r['B_plus'])**2*F(*r['average']))

    def test_family_normalization_and_inverse(self):
        a=family.source(700,[(5,(1,0,5))])
        self.assertEqual(a[25],5)
        self.assertEqual(family.delete_inert(a,5),family.source(700,[]))
        wrong=family.source(700,[(5,(1,0,1))])
        self.assertNotEqual(wrong,a)

    def test_rational_endpoint(self):
        a=[0,1]
        self.assertEqual(family.energy(a,F(3,2)),F(5,18))
        self.assertEqual(family.energy(a,F(1,2)),0)


if __name__=='__main__':unittest.main()
