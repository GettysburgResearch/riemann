"""Source orientation and exact constants for the varying-prime collision packet."""
import cmath
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
TARGET=ROOT/'research/riemann-structures/native-five-hour-pass/infinite-source/prime_collision_scout.py'
spec=importlib.util.spec_from_file_location('prime_collision_test',TARGET)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class PrimeCollisionTests(unittest.TestCase):
    def test_frozen_original_physical_core(self):
        raw=m.source_bytes()
        self.assertEqual(len(raw)>10000,True)
        core,_=m.load_core()
        self.assertEqual(len(core.authenticate()),3)

    def test_decoder_on_independent_power_paths(self):
        for weights in ((1,2),(2,5),(7,3)):
            moments=[F(weights[i],sum(x*y for x,y in zip(power,weights))+weights[i])
                     for i,power in m.BASIS]
            for a,b in __import__('itertools').product(m.BITS,repeat=2):
                row=m.decoder(a,b);da=sum(x*y for x,y in zip(a,weights));db=sum(x*y for x,y in zip(b,weights))
                expected=F(2*da,da+db) if da+db else F(0)
                self.assertEqual(row[0]+sum(c*x for c,x in zip(row[1:],moments)),expected)

    def test_three_fields_from_all_sixteen_ordered_pairs(self):
        Ap=complex(.8,.1);Dp=complex(-.2,.3);Aq=complex(.7,-.2);Dq=complex(.1,.4)
        values=[]
        for a in m.BITS:
            values.append((Dp if a[0] else Ap)*(Dq if a[1] else Aq))
        actual=[0j]*4
        pairs=list(__import__('itertools').product(m.BITS,repeat=2))
        for a,b in pairs:
            row=m.decoder(a,b);term=values[m.BITS.index(a)]*values[m.BITS.index(b)].conjugate()
            actual=[x+c*term for x,c in zip(actual,row)]
        Pp=Dp*Ap.conjugate();Pq=Dq*Aq.conjugate()
        expected=(2*(Pp*Pq.conjugate()-Pp.conjugate()*Pq),
                  (Pp-Pp.conjugate())*abs(Dq)**2,
                  abs(Dp)**2*(Pq-Pq.conjugate()))
        for got,want in zip(actual[1:],expected):self.assertAlmostEqual(abs(got-want),0,places=13)

    def test_jump_square_and_cusp_constants(self):
        # Represent a+b*sqrt(2) independently to avoid a floating radical.
        raw=((4,0),(-8,-4),(4,8),(0,-4))
        rational=sum(a*a+2*b*b for a,b in raw);radical=sum(2*a*b for a,b in raw)
        self.assertEqual((rational,radical),(288,128))
        self.assertEqual((rational//2,radical//2),(144,64))
        self.assertEqual(len(raw),4)

    def test_leading_field_orientation(self):
        p,q,t=1000003,1000033,F(3,10)
        def factors(prime):
            z=prime**(-.5)*cmath.exp(1j*float(t)*__import__('math').log(prime))
            A=cmath.sqrt(1-z*z);D=cmath.sqrt(1-z)-A
            return D*A.conjugate(),abs(D)**2
        Pp,Np=factors(p);Pq,Nq=factors(q)
        EA=(-1j)*(p*q)**.5*2*(Pp*Pq.conjugate()-Pp.conjugate()*Pq)
        EC=4j*q*p**.5*(Pp-Pp.conjugate())*Nq
        ED=4j*p*q**.5*Np*(Pq-Pq.conjugate())
        import math
        self.assertLess(abs(EA-math.sin(float(t)*math.log(p/q))),.003)
        self.assertLess(abs(EC-math.sin(float(t)*math.log(p))),.003)
        self.assertLess(abs(ED-math.sin(float(t)*math.log(q))),.003)

    def test_artifact_has_directed_positive_panels(self):
        data=json.loads((TARGET.parent/'prime_collision_scout.verification.json').read_text())
        self.assertEqual(data['status'],'DIRECTED FINITE RECONNAISSANCE; theorem is proved separately')
        self.assertEqual([x['primes'] for x in data['panels']],[list(x) for x in m.PAIRS])
        for panel in data['panels']:
            self.assertTrue(all(F(x[0])>0 for x in panel['LDL_pivot_intervals']))

    def test_nearby_prime_correlations_approach_one_in_scout(self):
        data=json.loads((TARGET.parent/'prime_collision_scout.verification.json').read_text())
        values=[float(F(x['EC_ED_correlation_interval'][0])) for x in data['panels']]
        self.assertTrue(all(a<b<1 for a,b in zip(values,values[1:])))


if __name__=='__main__':unittest.main()
