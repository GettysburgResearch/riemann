"""Independent finite checks for the new dimer/cumulant algebra."""
from fractions import Fraction as Q
from itertools import product
from math import comb
import unittest
import certify_dimer as c
import sensitivity as s

def cum(m):
 k=[Q(0)]*len(m)
 for n in range(1,len(m)):
  k[n]=m[n]-sum(comb(n-1,j-1)*k[j]*m[n-j] for j in range(1,n))
 return k

class Dual:
 def __init__(self,v,d=0):self.v=Q(v);self.d=Q(d)
 @classmethod
 def coerce(cls,x):return x if isinstance(x,cls) else cls(x)
 def __add__(self,x):
  x=self.coerce(x);return Dual(self.v+x.v,self.d+x.d)
 __radd__=__add__
 def __neg__(self):return Dual(-self.v,-self.d)
 def __sub__(self,x):return self+-self.coerce(x)
 def __rsub__(self,x):return self.coerce(x)+-self
 def __mul__(self,x):
  x=self.coerce(x);return Dual(self.v*x.v,self.d*x.v+self.v*x.d)
 __rmul__=__mul__
 def __truediv__(self,x):
  x=self.coerce(x);return Dual(self.v/x.v,(self.d*x.v-self.v*x.d)/x.v**2)
 def __pow__(self,n):return Dual(self.v**n,n*self.v**(n-1)*self.d) if n else Dual(1)

class Tests(unittest.TestCase):
 def test_dimer_against_all_configurations(self):
  for tau in (Q(0),Q(1,17),Q(3,5)):
   for a in (Q(1,7),Q(2,5)):
    m=[sum((Q(1,4)*(1+tau*x*y)*(a*(x+y))**n for x,y in product((-1,1),repeat=2)),Q(0)) for n in range(11)]
    k=cum(m)
    for r in range(1,6):self.assertEqual(k[2*r],a**(2*r)*c.peval(c.DP[r-1],tau))
 def test_jacobian_by_dual_differentiation(self):
  J=c.jacobian(c.CENTERS)
  for j in range(5):
   vals=c.values([Dual(x,int(i==j)) for i,x in enumerate(c.CENTERS)])
   for i in range(5):self.assertEqual(vals[i].d,J[i][j])
 def test_general_edge_derivatives_by_configuration_duals(self):
  for u,v in ((Q(1,7),Q(2,5)),(Q(3,11),Q(3,11))):
   m=[]
   for n in range(9):
    m.append(sum(((1+Dual(0,1)*x*y)*(u*x+v*y)**n/4 for x,y in product((-1,1),repeat=2)),Dual(0)))
   k=cum(m);ds=s.edge_response(u,v)
   for r,normalizer in enumerate((1,-2,16,-272),1):self.assertEqual(k[2*r].d,normalizer*ds[r])
 def test_root_jacobian_invertible(self):
  J=c.jacobian(c.CENTERS);R=c.invert(J)
  for i in range(5):
   for j in range(5):self.assertEqual(sum(J[i][k]*R[k][j] for k in range(5)),Q(i==j))

if __name__=='__main__':unittest.main()
