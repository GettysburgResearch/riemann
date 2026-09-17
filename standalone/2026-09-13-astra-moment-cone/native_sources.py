"""Complete centered-Gamma N=5 source moments; see NUMERICS.md.

The dyadic primitive is credited to CCF26. No zero coordinates enter here.
"""
from fractions import Fraction as Q
from math import factorial
from exact_interval import I,SCALE,pi,exp
import sys
ZERO=I.q(0); ONE=I.q(1)
def mul(a,b):
 k=len(a)-1
 return [sum((a[j]*b[n-j] for j in range(n+1)),ZERO) for n in range(k+1)]
def expjet(a):
 out=[exp(a[0])]
 for n in range(1,len(a)):
  out.append(sum((j*a[j]*out[n-j] for j in range(1,n+1)),ZERO)/n)
 return out
def sqrtjet(a):
 out=[a[0].sqrt()]; div=2*out[0]
 for n in range(1,len(a)):
  out.append((a[n]-sum((out[j]*out[n-j] for j in range(1,n)),ZERO))/div)
 return out
def add(a,b):return [x+y for x,y in zip(a,b)]
def scale(a,s):return [s*x for x in a]
rates=(1,4,9,16,25)
params=[]
for a in rates:
 b=Q(a*a);c=Q(0)
 for d in rates:
  if a!=d:b*=Q(d*d,(d-a)**2);c-=Q(2,d-a)
 params.append((a,b,c))
def densityjet(x):
 out=[ZERO]*len(x)
 for a,b,c in params:
  e=expjet(scale(x,-a)); p=x.copy();p[0]+=c
  out=add(out,scale(mul(p,e),b))
 return out
def partition(B,Llow):
 stack=[(Q(0),B)];cells=[]
 while stack:
  a,b=stack.pop();c=(a+b)/2;d=(b-a)/2;r=min(Q(1,64),(Llow-c)/4)
  if 8*d<=r:cells.append((a,b,c,d,r))
  else:stack.extend([(c,b),(a,c)])
 if not cells or cells[0][0]!=0 or cells[-1][1]!=B:
  raise ArithmeticError("partition endpoints")
 if any(cells[k][1]!=cells[k+1][0] for k in range(len(cells)-1)):
  raise ArithmeticError("partition gap")
 if any(not (a<b and r>0 and 8*d<=r) for a,b,c,d,r in cells):
  raise ArithmeticError("partition domain")
 return cells

def gamma5(order=14,degree=48, progress=False):
 if type(order) is not int or order!=14 or type(degree) is not int or degree not in (48,50):raise ValueError("certified protocol is order14, degree48/50")
 p=pi();tau=p*p/3-2*sum((Q(1,r) for r in rates),Q(0))
 LL=Q('1.07952912855616');LU=Q('1.07952912855618'); B=Q('1.0795291285')
 ratio=p/tau
 if not exp(2*LL).hi<ratio.lo or not ratio.hi<exp(2*LU).lo:raise ArithmeticError('endpoint brackets')
 # certificate large-argument dominance, same domain proof as GE4
 b1,c1=params[0][1:]; dom=Q(0)
 for a,b,c in params[1:]:
  dom+=b/b1*(2+abs(c)/Q(13,5))/(1+c1/Q(13,5))*Q(1,2**int((a-1)*Q(13,5)))
 if not dom<Q(1,4):raise ArithmeticError('analytic density domain')
 big=sum((b*(32+abs(c))*Q(1,2**int(a*Q(13,5))) for a,b,c in params),Q(0))
 if not big<2**11:raise ArithmeticError('whole large-density ceiling')
 if not factorial(5)**4<Q(600)*factorial(9):raise ArithmeticError('simplex coefficient')
 if not tau.hi<I.q(Q(2,5)).lo:raise ArithmeticError('tail rate')
 if not (Q(4,5)*exp(Q(1,50))).hi<I.q(1).lo:raise ArithmeticError('support-tail bound')
 cells=partition(B,LL); out=[ZERO]*(order+1)
 for ii,(a,b,c,d,r) in enumerate(cells):
  plus=[p*exp(2*c)];minus=[p*exp(-2*c)]
  for k in range(1,degree+1):plus.append(plus[-1]*(2*r)/k);minus.append(minus[-1]*(-2*r)/k)
  plus[0]-=tau;minus[0]-=tau
  h=sqrtjet(mul(densityjet(plus),densityjet(minus)))
  # multiply successively by t^2=(c+r v)^2 and integrate
  power=h
  factors=[Q(0)]*(degree+1)
  for k in range(0,degree+1,2):factors[k]=2*d*(d/r)**k/Q(k+1)
  for j in range(order+1):
   out[j]+=sum((power[k]*factors[k] for k in range(0,degree+1,2)),ZERO)
   if j<order:
    power=[c*c*power[k]+(2*c*r*power[k-1] if k>=1 else ZERO)+(r*r*power[k-2] if k>=2 else ZERO) for k in range(degree+1)]
  if progress and ii%200==0:print('gamma cells',ii,'of',len(cells),file=sys.stderr,flush=True)
 # total complex-disk ceiling for h: sqrt(2^11*2^28)<2^20;
 # |t|<11/10, therefore each moment ceiling is 2^21 (11/10)^(2j).
 delta=LU-B
 tailbase=10*I.q(delta)**5*I.q(delta).sqrt()
 for j in range(order+1):
  M=Q(2**21)*Q(11,10)**(2*j)
  quad=2*B*M*Q(1,8)**(degree+1)/Q(7,8)
  err=(I.q(quad)+tailbase*Q(11,10)**(2*j)).hi
  out[j]=I(out[j].lo-err,out[j].hi+err)
 norm=out[0]
 if norm.lo<=0:raise ArithmeticError('normalization')
 f=[out[k]/norm/factorial(2*k) for k in range(order+1)];f[0]=ONE
 s=power_sums(f)
 report={'source':'literal centered gamma N=5','N':5,'order':order,'degree':degree,'cells':len(cells),'normalization':norm.bounds(),'dominance_ratio':str(dom),'large_density_ceiling':str(big),'endpoint_lower':str(LL),'endpoint_upper':str(LU),'integration_end':str(B),'f':[v.bounds() for v in f],'scaled_power_sums':[v.bounds() for v in s]}
 return report

def power_sums(f,sc=200):
 b=[x*sc**k for k,x in enumerate(f)];q=[]
 for k in range(len(f)-1):q.append((k+1)*b[k+1]-sum((b[j]*q[k-j] for j in range(1,k+1)),ZERO))
 return [(-1)**k*q[k] for k in range(len(q))]


def theta(order=16,mesh=256):
 if type(order) is not int or order!=16 or type(mesh) is not int or mesh not in (256,320):raise ValueError('protocol')
 p=pi();mom=[I.q(0)]*(order+1)
 for j in range(3*mesh+1):
  t=Q(j,mesh);e2=exp(2*t);e9=exp(Q(9,2)*t);e5=exp(Q(5,2)*t)
  ph=I.q(0)
  for n in range(1,21):
   nn=n*n; ph+=(4*(p**2)*nn**2*e9-6*p*nn*e5)*exp(-p*nn*e2)
  wt=Q(1 if j==0 else 2,mesh)
  for r in range(order+1):mom[r]+=wt*t**(2*r)*ph
 for r in range(order+1):
  er=I.q(Q(factorial(2*r),1<<490)).hi
  mom[r]=I(mom[r].lo-er,mom[r].hi+er)
 f=[v/mom[0]/factorial(2*k) for k,v in enumerate(mom)];f[0]=I.q(1)
 s=power_sums(f)
 report={'source':'complete native theta','order':order,'mesh':mesh,'normalization':mom[0].bounds(),'f':[v.bounds() for v in f],'scaled_power_sums':[v.bounds() for v in s]}
 return report
