"""Complete conditional graph law with one positive edge. Degree 20, exact AD."""
from fractions import Fraction as F
from math import factorial
from inherited import I,source
N=20
MULT=(256,10,1,1,1,1,1,1,1,1,1)
KS=(F(1,100),)*6+(F(3),F(3))+(F(1,100),)*3
CK=source.cumulants([F(int(j%2==0)) for j in range(N+1)])
class AD:
    __slots__=('value','gradient')
    def __init__(self,value,gradient):self.value=value;self.gradient=gradient
    def cast(self,x):
        if isinstance(x,AD):return x
        return AD(x,[self.value*0 for _ in self.gradient])
    def __add__(self,x):
        x=self.cast(x);return AD(self.value+x.value,[u+v for u,v in zip(self.gradient,x.gradient)])
    __radd__=__add__
    def __neg__(self):return AD(-self.value,[-v for v in self.gradient])
    def __sub__(self,x):return self+-self.cast(x)
    def __rsub__(self,x):return self.cast(x)+-self
    def __mul__(self,x):
        x=self.cast(x);return AD(self.value*x.value,[u*x.value+self.value*v for u,v in zip(self.gradient,x.gradient)])
    __rmul__=__mul__
    def __truediv__(self,x):
        if isinstance(x,AD):raise TypeError('only scalar division is used')
        return AD(self.value/x,[v/x for v in self.gradient])
    def __pow__(self,n):
        if type(n)is not int or n<0:raise ValueError('nonnegative integer power')
        out=self.cast(1);b=self
        while n:
            if n&1:out=out*b
            n//=2
            if n:b=b*b
        return out


def divide(self,x):
 x=self.cast(x)
 return AD(self.value/x.value,[(a*x.value-self.value*b)/(x.value*x.value) for a,b in zip(self.gradient,x.gradient)])
AD.__truediv__=divide

def conv(a,b):
 zero=a[0]*0
 return [sum((a[j]*b[i-j] for j in range(i+1)),zero) for i in range(N+1)]
def ppow(p,n):
 out=[p[0]*0 for _ in p];out[0]+=1
 while n:
  if n&1:out=conv(out,p)
  n//=2
  if n:p=conv(p,p)
 return out

def evaluate(z,pair=(7,9),outmom=False,multiplicities=MULT):
 zero=z[0]*0;one=zero+1;gs=[];hs=[];biases=[]
 for i in range(11):
  p=one if i<5 else z[17] if i==5 else z[12+i-6];bias=z[11]*KS[i]*z[i];biases.append(bias)
  gs.append([one]+[p*z[i]**j*(bias if j%2 else one)/factorial(j) for j in range(1,N+1)])
  hs.append([bias]+[p*z[i]**j*(one if j%2 else bias)/factorial(j) for j in range(1,N+1)])
 i,j=pair;q=z[18]
 G=conv(gs[i],gs[j]);H=conv(hs[i],hs[j]);den=one+q*biases[i]*biases[j]
 tot=[(g+q*h)/den for g,h in zip(G,H)]
 for k in range(11):tot=conv(tot,ppow(gs[k],multiplicities[k]-int(k==i)-int(k==j)))
 for k in range(1,N+1,2):tot[k]=zero
 lg=[zero]*(N+1)
 for k in range(2,N+1,2):lg[k]=tot[k]-sum((j*lg[j]*tot[k-j] for j in range(2,k,2)),zero)/k
 vals=[lg[2*r]*factorial(2*r)/CK[2*r] for r in range(1,N//2+1)]
 return (vals,[tot[j]*factorial(j) for j in range(N+1)]) if outmom else vals

def values_jac(z,active=tuple(range(19)),pair=(7,9)):
 zero=z[0]*0;one=zero+1;lookup={j:i for i,j in enumerate(active)};args=[]
 for j,x in enumerate(z):
  g=[zero]*len(active)
  if j in lookup:g[lookup[j]]=one
  args.append(AD(x,g))
 out=evaluate(args,pair)
 return [a.value for a in out],[a.gradient for a in out]
