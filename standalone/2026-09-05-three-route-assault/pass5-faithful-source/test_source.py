"""Exact algebra, interval rejection, and source-normalization tests."""
import unittest
from fractions import Fraction as F
from math import comb, factorial
import compile_source as c

class Tests(unittest.TestCase):
    def test_interval_exact_arithmetic(self):
        for a in [F(-7,3),F(-1,5),F(2,7),F(5,2)]:
            for b in [F(-4,3),F(1,9),F(7,2)]:
                for obj,val in [(c.I.of(a)+b,a+b),(c.I.of(a)*b,a*b),(c.I.of(a)/b,a/b)]:
                    self.assertLessEqual(F(obj.lo,c.SCALE),val)
                    self.assertGreaterEqual(F(obj.hi,c.SCALE),val)
    def test_numeric_alias_refusal(self):
        for v in [True,1.0,'1']:
            with self.assertRaises(ValueError): c.I.of(v)
    def test_domain_refusal(self):
        for v in [c.I(-1,1),c.I(0,0)]:
            with self.assertRaises(ValueError): v.reciprocal()
        with self.assertRaises(ValueError): c.sqrt_rational(F(-1))
        with self.assertRaises(ValueError): c.log_rational(F(0))
        with self.assertRaises(ValueError): c.parameters(True,0)
        with self.assertRaises(ValueError): c.parameters(33,0)
    def test_sqrt_integer_enclosure(self):
        for k in range(1,50):
            q=c.sqrt_rational(F(k))
            self.assertLessEqual(q.lo*q.lo,k*c.SCALE*c.SCALE)
            self.assertGreaterEqual(q.hi*q.hi,k*c.SCALE*c.SCALE)
    def test_log_scale_identity(self):
        for k in range(1,12):
            a=c.log_rational(F(2*k))-c.log_rational(F(k))-c.log_rational(F(2))
            self.assertLessEqual(a.lo,0);self.assertGreaterEqual(a.hi,0)
    def test_bernoulli_values(self):
        vals=[F(1),F(-1,2),F(1,6),F(0),F(-1,30),F(0),F(1,42),F(0),F(-1,30)]
        self.assertEqual([c.bernoulli(i) for i in range(9)],vals)
    def test_series_inverse_and_composition(self):
        a=[c.I.of(x) for x in [2,1,-3,4,1]]
        prod=c.mul(a,c.inv(a))
        for j,v in enumerate(prod):
            val=int(j==0)*c.SCALE
            self.assertLessEqual(v.lo,val);self.assertGreaterEqual(v.hi,val)
        h=c.const(0,4);h[1]=c.I.of(1)
        out=c.compose(a,h)
        for x,y in zip(a,out): self.assertLessEqual(x.lo,y.hi);self.assertLessEqual(y.lo,x.hi)
    def test_zeta2_full_tail(self):
        M,K,d=c.parameters(0,32)
        v=c.zeta_em(F(2),0,M,K)[0].widen(d)
        target=c.pi_interval()*c.pi_interval()/6
        self.assertLessEqual(v.lo,target.hi);self.assertLessEqual(target.lo,v.hi)
    def test_digamma_shift_full_tail(self):
        M,K,d=c.parameters(0,32)
        v=c.psi_em(F(4),0,M,K)[0]-c.psi_em(F(2),0,M,K)[0]-1
        v=v.widen(2*d)
        self.assertLessEqual(v.lo,0);self.assertGreaterEqual(v.hi,0)
    def test_tail_constants(self):
        r=F(1,16);alpha=(1-3*r)/(2*(1+r))
        self.assertEqual(alpha,F(13,34))
        self.assertEqual(1/((1-r)*alpha),F(544,195))
        self.assertEqual(F(4)-11*alpha,F(-7,34))
        for n in range(33):
            for B in range(0,129,8):
                M,K,d=c.parameters(n,B)
                self.assertLess(36*d*8**n,F(1,2**(n+B+13)))
                self.assertLess((F(55*(n+1))+F(1,2))*d*8**n,F(1,2**(n+B+12)))
    def test_critical_slope_signs(self):
        lo=F('0.08146966677');hi=F('0.08146966679')
        def f(r): return -c.log_rational(r)-F(1,4)/r+F(1,2)+3*r/4
        self.assertLess(f(lo).hi,0);self.assertGreater(f(hi).lo,0)
        C=lambda r:(1+r)**2/(2*r)
        self.assertGreater(C(hi),F('7.177988362'))
        self.assertLess(C(lo),F('7.177988364'))
    def test_laguerre_recurrence(self):
        def lag(n,x):return sum((F((-1)**j*comb(n,j),factorial(j))*x**j for j in range(n+1)),F(0))
        for n in range(1,16):
            for x in [F(0),F(1,3),F(4),F(32)]:
                self.assertEqual((n+1)*lag(n+1,x),(2*n+1-x)*lag(n,x)-n*lag(n-1,x))
    def test_hardy_recurrence_independent_weights(self):
        cs=[F(1),F(-2),F(3),F(5),F(-7),F(11)];N=len(cs)
        A=[[F(0) for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                A[i][j]=(cs[i] if not j else 0)+(cs[j] if not i else 0)+((A[i-1][j] if i else 0)+(A[i][j-1] if j else 0))/2
                b=sum((cs[k]*F(comb(i+j-k,j),2**(i+j-k)) for k in range(i+1)),F(0))
                b+=sum((cs[k]*F(comb(i+j-k,i),2**(i+j-k)) for k in range(j+1)),F(0))
                self.assertEqual(A[i][j],b)
                self.assertLessEqual(sum((F(comb(j+t,j),2**(j+t)) for t in range(i+1)),F(0)),2)
    def test_indefinite_ldl_refused(self):
        with self.assertRaises(ValueError):c.ldl_pivots([[c.I.of(1),c.I.of(2)],[c.I.of(2),c.I.of(1)]])

if __name__=='__main__':unittest.main()
