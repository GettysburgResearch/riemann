"""Outward dyadic complex L1 balls. Center=(a+ib)/2**BITS, radius=e/2**BITS.
Integers/Fractions and explicit analytic elementary-function remainder bounds.
No floating library or special-function oracle enters an enclosure.
"""
from fractions import Fraction as F
from math import isqrt,comb,factorial
BITS=512; Q=1<<BITS

def ceildiv(n,d):return -((-n)//d)
class B:
 __slots__=('a','b','e')
 def __init__(self,a=0,b=0,e=0):self.a=a;self.b=b;self.e=e
 @classmethod
 def real(cls,v):
  if isinstance(v,int):return cls(v*Q)
  v=F(v);a,rem=divmod(v.numerator*Q,v.denominator)
  return cls(a,0,int(rem!=0))
 @classmethod
 def complex(cls,re=0,im=0):
  re=cls.real(re);im=cls.real(im);return cls(re.a,im.a,re.e+im.e)
 def __add__(self,o):
  if not isinstance(o,B):o=B.real(o)
  return B(self.a+o.a,self.b+o.b,self.e+o.e)
 __radd__=__add__
 def __neg__(self):return B(-self.a,-self.b,self.e)
 def __sub__(self,o):return self+-o if isinstance(o,B) else self+-B.real(o)
 def __rsub__(self,o):return -self+o
 def __mul__(self,o):
  if not isinstance(o,B):return self.rat(F(o))
  aa=self.a*o.a-self.b*o.b;bb=self.a*o.b+self.b*o.a
  a,ra=divmod(aa,Q);b,rb=divmod(bb,Q)
  e=ceildiv((abs(self.a)+abs(self.b))*o.e+(abs(o.a)+abs(o.b))*self.e+self.e*o.e,Q)+int(ra!=0)+int(rb!=0)
  return B(a,b,e)
 __rmul__=__mul__
 def rat(self,v,den=None):
  if den is None:
   v=F(v);num,den=v.numerator,v.denominator
  else:num=v
  if den<=0:raise ValueError('denominator')
  a,ra=divmod(self.a*num,den);b,rb=divmod(self.b*num,den)
  return B(a,b,ceildiv(self.e*abs(num),den)+int(ra!=0)+int(rb!=0))
 def inv(self):
  m=max(abs(self.a),abs(self.b))
  if m<=self.e:raise ArithmeticError('ball meets zero')
  d=self.a*self.a+self.b*self.b
  a,ra=divmod(self.a*Q*Q,d);b,rb=divmod(-self.b*Q*Q,d)
  e=ceildiv(2*self.e*Q*Q,m*(m-self.e))+int(ra!=0)+int(rb!=0)
  return B(a,b,e)
 def __truediv__(self,o):
  return self*o.inv() if isinstance(o,B) else self.rat(F(1)/F(o))
 def conj(self):return B(self.a,-self.b,self.e)
 def grow(self,e):return B(self.a,self.b,self.e+int(e))
 def norm(self):return abs(self.a)+abs(self.b)+self.e
 def approx(self):return complex(self.a/Q,self.b/Q)
 def radius(self):return self.e/Q
 def __repr__(self):return f'{self.approx()} +/- {self.radius():.3g}'
ZERO=B();ONE=B.real(1);I=B.complex(0,1)

def rad(v):
 v=F(v);return ceildiv(v.numerator*Q,v.denominator)

def sqrt_real(v):
 v=F(v)
 if v<0:raise ValueError('positive root required')
 a=isqrt(v.numerator*Q*Q//v.denominator)
 e=int(a*a*v.denominator!=v.numerator*Q*Q)
 return B(a,0,e)

def exp(z):
 if not isinstance(z,B):z=B.real(z)
 k=0
 while z.norm()>Q//2:z=z.rat(1,2);k+=1
 term=ONE;s=ONE
 for j in range(1,129):term=(term*z).rat(1,j);s=s+term
 # e**(1/2) sum-tail <= 2*(1/2)**129/129! < 2**-512.
 if F(2,2**129*factorial(129))>=F(1,Q):raise ArithmeticError('exp remainder precision')
 s=s.grow(1)
 for _ in range(k):s=s*s
 return s

def logpos(v):
 v=F(v)
 if v<=0:raise ValueError('positive argument')
 k=0
 while v>=2:v/=2;k+=1
 while v<1:v*=2;k-=1
 x=B.real((v-1)/(v+1));xx=x*x;term=x;s=ZERO
 for j in range(256):s=s+term.rat(1,2*j+1);term=term*xx
 s=(2*s).grow(rad(F(2,3**513*513)*F(9,8)))
 return s+k*LOG2

def atanh13():
 s=sum((F(1,(2*j+1)*3**(2*j+1)) for j in range(256)),F(0))
 return B.real(2*s).grow(rad(F(2,3**513*513)*F(9,8)))
LOG2=atanh13()

def arctan_inv(n,terms):
 s=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(terms)),F(0))
 return B.real(s).grow(rad(F(1,(2*terms+1)*n**(2*terms+1))))
PI=16*arctan_inv(5,160)-4*arctan_inv(239,50)

def atan_rational(v):
 v=F(v)
 if v<0:return -atan_rational(-v)
 if v>1:return PI/2-atan_rational(1/v)
 if v>F(1,2):return PI/4+atan_rational((v-1)/(v+1))
 x=B.real(v);xx=x*x;term=x;ss=ZERO
 for j in range(256):ss=ss+term.rat((-1)**j,2*j+1);term=term*xx
 # Exact real argument is <=1/2: alternating tail <=2^-513/513.
 return ss.grow(1)

def clog(z):
 # Principal logarithm in the right half-plane only.
 if z.a-z.e<=0:raise ValueError('right-half-plane logarithm contract')
 re=logpos(F(z.a*z.a+z.b*z.b,Q*Q))/2
 im=atan_rational(F(z.b,z.a))
 out=B(re.a-im.b,re.b+im.a,re.e+im.e)
 # Segment from center to any input: |log w-log center| <= e/(a-e).
 # Convert absolute complex error to a conservative L1 error (factor two).
 return out.grow(ceildiv(2*z.e*Q,z.a-z.e))

def bernoulli(n):
 vals=[F(1)]
 for k in range(1,n+1):vals.append(-sum((F(comb(k+1,j))*vals[j] for j in range(k)),F(0))/F(k+1))
 return vals
BERN=bernoulli(64)

def loggamma(z):
 # Euler--Maclaurin remainder: Re(z+64)>=64 for our q values.
 if z.a-z.e<=0:raise ValueError('gamma shift contract')
 w=z+64;inv=w.inv();step=inv*inv
 s=(w-F(1,2))*clog(w)-w+F(1,2)*clog(2*PI)
 pp=inv
 for k in range(1,32):s=s+pp.rat(BERN[2*k]/F(2*k*(2*k-1)));pp=pp*step
 s=s.grow(rad(2*abs(BERN[64])/F(64*63*64**63)))
 for j in range(64):s=s-clog(z+j)
 return s

def powpos(v,z):return exp(z*logpos(v))

def polyval(coefs,x):
 s=ZERO
 for c in reversed(coefs):s=s*x+c
 return s

def convolution(a,b,n):
 out=[]
 for k in range(n+1):
  ss=ZERO
  for j in range(max(0,k-len(b)+1),min(k,len(a)-1)+1):ss=ss+a[j]*b[k-j]
  out.append(ss)
 return out

def source_laplace_series(r,h,n):
 # F(r)=sinh(sqrt(-6ir))/sqrt(-6ir); L=1/F.
 a=sqrt_real(3*r);a=B(a.a,-a.a,2*a.e)
 ep=exp(a);em=ep.inv();sh=(ep-em).rat(1,2);ch=(ep+em).rat(1,2)
 f=[sh/a]
 f.append((ch-f[0]).rat(h/(2*r)))
 for j in range(n-1):
  f.append(-(f[j+1].rat(h*(j+1)*(2*j+3))+I*f[j].rat(3*h*h)).rat(F(1,2*r*(j+2)*(j+1))))
 l=[f[0].inv()]
 for k in range(1,n+1):
  ss=ZERO
  for j in range(1,k+1):ss=ss+f[j]*l[k-j]
  l.append(-ss*l[0])
 return l
