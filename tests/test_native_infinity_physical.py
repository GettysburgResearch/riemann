"""Primitive, orientation and physical-measure controls for infinite source Gram."""
import importlib.util
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'research/riemann-structures/native-five-hour-pass/infinite-source/physical_infinity.py'
spec=importlib.util.spec_from_file_location('physical_infinity_test_target',PATH)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class PhysicalInfinityTests(unittest.TestCase):
    def test_primitive_source_authentication(self):
        self.assertEqual(len(m.authenticate()),3)

    def test_all_monomial_currents_power_paths(self):
        for weights in ((1,2,3),(2,3,5),(3,1,4)):
            moments=[F(weights[i],sum(x*y for x,y in zip(p,weights))+weights[i]) for i,p in m.BASIS]
            for a,b in product(m.BITS,repeat=2):
                row=m.decoder(a,b)
                da=sum(x*y for x,y in zip(a,weights));db=sum(x*y for x,y in zip(b,weights))
                expected=F(2*da,da+db) if da+db else F(0)
                actual=row[0]+sum(c*x for c,x in zip(row[1:],moments))
                self.assertEqual(actual,expected)

    def test_ordered_reversal_and_unit(self):
        for a,b in product(m.BITS,repeat=2):
            left=m.decoder(a,b);right=m.decoder(b,a)
            self.assertEqual([x+y for x,y in zip(left[1:],right[1:])],[0]*20)
            self.assertEqual(left[0]+right[0],2*int(any(a) or any(b)))
        for b in m.BITS:self.assertEqual(m.decoder((0,0,0),b),[0]*21)

    def test_pair_products_from_independent_root_convolution(self):
        L=16;coeff,_=m.coefficients(L)
        root=[F(1)]
        for k in range(1,L+1):root.append(-root[-1]*(F(1,2)-k+1)/k)
        a=[root[k//2] if k%2==0 else F(0) for k in range(L+1)]
        d=[root[k]-a[k] for k in range(L+1)]
        for i,(u,v) in enumerate(((a,a),(a,d),(d,d))):
            for k in range(L+1):
                self.assertEqual(coeff[i][k],sum(u[j]*v[k-j] for j in range(k+1)))

    def test_tail_magnitudes_decrease(self):
        _,first=m.coefficients(16)
        for L in range(17,130):
            _,nextvalue=m.coefficients(L)
            self.assertLess(nextvalue,first);first=nextvalue

    def test_original_mass_and_support(self):
        arb,_,_,ctx=m.arb_import();ctx.prec=192
        mass=128*(3+arb(2).sqrt())*arb(2).log()-288
        self.assertTrue(m.gamma_arb(1,1,arb).overlaps(mass))
        self.assertTrue(m.gamma_arb(8,1,arb).is_zero())
        self.assertTrue(m.gamma_arb(9,1,arb).is_zero())
        for n,d in ((3,2),(7,4),(15,8)):
            self.assertTrue(m.gamma_arb(n,d,arb).overlaps(m.gamma_arb(d,n,arb)))

    def test_numpy_kernel_inside_directed_balls(self):
        import numpy as np
        arb,_,_,ctx=m.arb_import();ctx.prec=192
        for n,d in ((1,1),(2,1),(3,2),(5,3),(4,1),(7,1),(8,1)):
            approximate=float(m.gamma_numpy(np.array([__import__('math').log(n/d)]))[0])
            reference=m.gamma_arb(n,d,arb)
            self.assertLess(abs(approximate-float(reference)),2e-11)

    def test_complete_degree_one_primitive_tensor_vs_literal_records(self):
        import numpy as np
        from math import gcd,log,sqrt
        # Primitive A=1,D=-z/2; pair products have degree at most two.
        L=2;local=[]
        for p in m.PRIMES:
            v=np.array([[1,0,0],[0,-.5/sqrt(p),0],[0,0,.25/p]])
            local.append(np.array([np.correlate(v[i],v[j],'full') for i,j in product(range(3),repeat=2)]))
        ds=np.arange(-L,L+1);tensor=np.zeros((9,9,9))
        s12=ds[:,None]*log(2)+ds[None,:]*log(3)
        for k,e in enumerate(ds):
            pair=local[0]@m.gamma_numpy(s12+e*log(5))@local[1].T
            tensor+=pair[:,:,None]*local[2][:,k][None,None,:]
        actual=m.reshuffle_numpy(tensor)
        # Independently enumerate all ordered records and apply 1/sqrt(nm).
        records=[]
        for a,b in product(m.BITS,repeat=2):
            n=__import__('math').prod(p**e for p,e in zip(m.PRIMES,a))
            d=__import__('math').prod(p**e for p,e in zip(m.PRIMES,b))
            scalar=(-.5)**(sum(a)+sum(b))/sqrt(n*d)
            records.append((n,d,scalar*np.array(m.decoder(a,b),dtype=float)))
        expected=np.zeros((21,21))
        for n,d,row in records:
            for nn,dd,col in records:
                kernel=float(m.gamma_numpy(np.array([log((n*dd)/(d*nn))]))[0])
                expected+=kernel*np.outer(row,col)
        self.assertLess(np.max(abs(actual-expected)),2e-11)

    def test_registered_limits_refuse(self):
        with self.assertRaises(ValueError):m.scout(64)
        with self.assertRaises(ValueError):m.certify_gram(256,192)
        with self.assertRaises(ValueError):m.certify_gram(96,1024)

if __name__=='__main__':unittest.main()
