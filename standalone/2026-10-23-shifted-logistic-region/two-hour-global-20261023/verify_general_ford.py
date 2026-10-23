"""Exact rational endpoints for GENERAL_WEIGHTED_FORD_DETECTOR.md.

The interval arithmetic/Taylor pattern is adapted from the earlier independent
logistic Fraction replay. The new scalar reduction and its analytic proof are
separate inputs. No binary floating point enters an acceptance decision.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext
import json
import math

BITS=192
SCALE=1<<BITS

def require(ok,label):
    if not ok:
        raise ArithmeticError(label)

def down(x):
    x=Q(x)
    return Q(x.numerator*SCALE//x.denominator,SCALE)

def up(x):
    return -down(-Q(x))

class I:
    def __init__(self,lo,hi=None):
        self.lo=down(lo);self.hi=up(lo if hi is None else hi)
        require(self.lo<=self.hi,'ordered interval')
    @staticmethod
    def get(x):return x if isinstance(x,I) else I(x)
    def __add__(self,x):
        x=I.get(x);return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,x):return self+(-I.get(x))
    def __rsub__(self,x):return I.get(x)-self
    def __mul__(self,x):
        x=I.get(x);p=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=I.get(x);require(not x.lo<=0<=x.hi,'nonzero divisor')
        return self*I(1/x.hi,1/x.lo)
    def __rtruediv__(self,x):return I.get(x)/self
    def __pow__(self,n):
        if n<0:return 1/(self**(-n))
        if n==0:return I(1)
        if self.lo>=0:return I(self.lo**n,self.hi**n)
        if self.hi<=0:return (-self)**n if n%2==0 else -((-self)**n)
        if n%2:return I(self.lo**n,self.hi**n)
        return I(0,max(self.lo**n,self.hi**n))

def sincos(x,sine):
    x=Q(x);require(abs(x)<=3,'trig Taylor domain')
    term=x if sine else Q(1);total=term
    for j in range(1,50):
        left=2*j if sine else 2*j-1
        term*=-x*x/(left*(left+1));total+=term
    left=100 if sine else 99
    nxt=term*(-x*x)/(left*(left+1))
    return I(min(total,total+nxt),max(total,total+nxt))

def exp_point(x):
    x=Q(x)
    if x<0:return 1/exp_point(-x)
    squarings=0
    while x>1:x/=2;squarings+=1
    term=Q(1);total=term
    for n in range(1,65):term*=x/n;total+=term
    out=I(total,total+3*x**65/math.factorial(65))
    for _ in range(squarings):out=out**2
    return out

def exp_i(x):
    x=I.get(x);return I(exp_point(x.lo).lo,exp_point(x.hi).hi)

def log_unit(x):
    x=Q(x);require(1<=x<=2,'unit log domain')
    z=(x-1)/(x+1)
    total=sum((2*z**(2*j+1)/(2*j+1) for j in range(90)),Q(0))
    return I(total,total+2*z**181/(181*(1-z*z)))

LOG2=log_unit(2)

def log_point(x):
    x=Q(x);require(x>0,'positive log domain');k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    return log_unit(x)+k*LOG2

def log_i(x):
    x=I.get(x);return I(log_point(x.lo).lo,log_point(x.hi).hi)

def atan_small(x):
    x=Q(x);require(0<x<1,'atan series domain')
    total=sum(((-1)**n*x**(2*n+1)/(2*n+1) for n in range(100)),Q(0))
    nxt=x**201/201
    return I(total,total+nxt)

PI=16*atan_small(Q(1,5))-4*atan_small(Q(1,239))
THETA=Q(23,20)
ST,CT=sincos(THETA,True),sincos(THETA,False)
ST2,CT2=sincos(2*THETA,True),sincos(2*THETA,False)
TAN=ST/CT;COT=CT/ST;SEC2=1/CT**2
U=2*THETA*COT
W0=SEC2*(THETA*TAN+3*THETA*COT-3)
WMINUS=2*TAN**2+3-3*THETA*(TAN+COT)
R0=79
C0=1/(ST*CT**3)
C1=(THETA-ST*CT)*TAN**4
C2=TAN**3*ST**2
C3=(THETA-ST*CT)*TAN**2
H=C0*(C2*Q((R0+1)**2,R0**3)*(exp_i(U)+1)+C1/R0**2+C3)/(1-TAN**2/R0**2)**2
C4=1+Q(1,R0)+H*Q((R0+1)**2,R0**3)/W0

RNEW=139
HNEW=C0*(C2*Q((RNEW+1)**2,RNEW**3)*(exp_i(U)+1)+C1/RNEW**2+C3)/(1-TAN**2/RNEW**2)**2
C4NEW=1+Q(1,RNEW)+HNEW*Q((RNEW+1)**2,RNEW**3)/W0
CURVATURE=SEC2*TAN**2*(SEC2*THETA*COT-1)

def trig_moment(n,sine):
    total=Q(0)
    for m in range(1 if sine else 0,81,2):
        sign=(-1)**((m-1)//2 if sine else m//2)
        total+=sign*(2*THETA)**m/(math.factorial(m)*(n+m+1))
    tail=11*(2*THETA)**81/math.factorial(81)
    return U**(n+1)*I(total-tail,total+tail)

DEGREE=20
CM=[trig_moment(n,False) for n in range(DEGREE+2)]
SM=[trig_moment(n,True) for n in range(DEGREE+1)]
MOMENTS=[]
for n in range(DEGREE+1):
    MOMENTS.append(SEC2*((SEC2*THETA*COT-1)*CM[n]-SEC2*CM[n+1]/2
        +(2*THETA*COT-2)*U**(n+1)/(n+1)-U**(n+2)/(n+2)
        +(2*COT-CT2/ST2)*SM[n]))

def W(z):
    z=I.get(z);require(0<=z.lo<=z.hi<=Q(1,10),'W argument domain')
    total=I(0)
    for n,m in enumerate(MOMENTS):total+=m*(-z)**n/math.factorial(n)
    # 0<=w<=w0<7, U<11/10, and exp(zU)<2.
    tail=14*Q(11,10)*(Q(11,100)**21)/math.factorial(21)
    return total+I(-tail,tail)

C=[3500513104,-5906953599,-1574092731,18166603739,6213449589,
   -38436761903,-16088159026,168141762350,447056663730,
   616860378424,541372347258,298691298328,83048065550]
M=10**14;K=12;N=sum(c*c for c in C)+13*M
COEFF=[Q(1)]+[Q(2*(sum(C[j]*C[j+k] for j in range(13-k))+M*(13-k)),N) for k in range(1,13)]
EPS=Q(1,10**20)
REPS=Q(1,10**7)
AA=Q(469028,10**6);BB=Q(399399,10**5)

def margin(r,ell):
    r,ell=Q(r),Q(ell);A=1/r
    require(ell>=60 and 0<A<=Q(22,100),'endpoint domain')
    require(A/ell<=Q(1,160),'distance condition')
    h0=ell+log_point(K)
    eup=(log_point(K)+EPS)/ell
    lam=A/h0;d=A/ell
    jsum=I(0);tailsum=I(Q(18,10))
    for j,bj in enumerate(COEFF[1:],1):
        hj=ell+log_point(j)+EPS
        jsum+=bj*(hj/6+log_i(AA*hj+BB)+REPS)
        tailsum+=bj*(Q('3.5691')*hj+Q('5.316')*log_i(hj)+Q('17.934'))
    return (COEFF[1]*W(eup)/W0-WMINUS/W0
       -Q('.3334')*PI**2*COEFF[1]*lam*d
       -lam*(jsum+Q('.851'))-C4*lam**2*tailsum)

def margin_poisson_prime(r,ell):
    r,ell=Q(r),Q(ell);A=1/r
    require(ell>=60 and 0<A<=Q(22,100),'refined endpoint domain')
    h0=ell+log_point(K);lam=A/h0;d=A/ell
    require(lam.hi<Q(1,280),'R139 remainder condition')
    eup=(log_point(K)+EPS)/ell
    jsum=I(0);tailsum=I(Q(18,10))
    for j,bj in enumerate(COEFF[1:],1):
        hj=ell+log_point(j)+EPS
        jsum+=bj*(hj/6+log_i(AA*hj+BB)+REPS)
        tailsum+=bj*(Q(7,3)*hj+Q('4.8'))
    # .254999*lambda_upper <= .255*lambda_actual; the elementary
    # comparison is checked below. The cubic loss uses lambda_upper.
    return (COEFF[1]*W(eup)/W0-WMINUS/W0
       -Q('.3334')*PI**2*COEFF[1]*lam*d
       -lam*(jsum+Q('.596001'))-C4NEW*lam**2*tailsum-18*lam**3)

def display(x):
    with localcontext() as ctx:
        ctx.prec=25
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def main():
    require(0<TAN.lo<TAN.hi<R0,'kernel remainder domain')
    require(0<W0.lo<W0.hi<7 and 0<U.lo<U.hi<Q(11,10),'kernel mass bounds')
    require(exp_point(2*THETA).hi<11,'trig moment exponential remainder')
    require(exp_point(Q(11,100)).hi<2,'W exponential remainder')
    require(C4.hi<Q('1.149'),'sharper c4 bound')
    require(C4NEW.hi<Q('1.08'),'R139 c4 bound')
    require(W0.lo>6 and 0<CURVATURE.lo<CURVATURE.hi<70,'prime kernel inputs')
    require(Q('.22')/(60+log_point(12).lo)<Q(1,280),'uniform R139 domain')
    require(Q('.254999')*(60+EPS)<Q('.255')*60,'prime scale comparison')
    require(3<PI.lo<PI.hi<4 and exp_point(Q(8,5)).hi<6,'Poisson gamma constants')
    require(Q('1.506')-Q(4,5)+Q(1,10000)+Q(57,16*10000**2)<Q(3,4),'Poisson additive constant')
    require(all(b>0 for b in COEFF),'positive cosine coefficients')
    require(COEFF[1]>1 and COEFF[0]==1,'polynomial normalization')
    require(26*log_point(10).hi<60,'global shifted-envelope error at60')
    require(2*Q(1,10**8)+Q(1,2*10**18)<REPS,'smoothing error allowance')
    require(20*log_point(10).hi<60,'height logarithm enclosure')
    require(log_point(32).hi<4,'degree monotonicity range')
    require(log_point(60*AA+BB).lo>3,'weighted smoothing derivative')
    require(Q(4,6)+Q(16,15)-3<0,'smoothing-over-height decreasing')
    require(log_point(60).lo>4,'tail log derivative')
    require(Q(16,15)-2*4<0,'tail logarithm-over-square decreasing')
    cases=[('4.79','66.35'),('4.78','66.92'),('4.77','67.49'),
           ('4.75','68.67'),('4.70','71.77'),('4.65','75.13')]
    out=[]
    for r,l in cases:
        v=margin(r,l);require(v.lo>0,'positive endpoint '+r)
        out.append({'R':r,'log_height_cap':l,'lower':display(v.lo),'upper':display(v.hi)})
    for r,l in [('4.79','66.3'),('4.78','66.8'),('4.70','71.7')]:
        v=margin(r,l);require(v.hi<0,'negative endpoint control')
    # A wrong cot sign cannot repair an endpoint selected well below its root.
    require(margin('4.79','60').hi<0,'gross endpoint negative control')
    refined=[]
    for r,l in [('4.75','60'),('4.70','62.68'),('4.65','65.69'),('4.60','68.96')]:
        v=margin_poisson_prime(r,l);require(v.lo>0,'refined positive endpoint '+r)
        refined.append({'R':r,'log_height_cap':l,'lower':display(v.lo),'upper':display(v.hi)})
    for r,l in [('4.70','62.6'),('4.65','65.6')]:
        v=margin_poisson_prime(r,l);require(v.hi<0,'refined negative endpoint control')
    print(json.dumps({'status':'PASS','kernel_theta':'23/20','degree':K,
       'c4_lower':display(C4.lo),'c4_upper':display(C4.hi),
       'c4_refined_upper':display(C4NEW.hi),'kernel_w0_lower':display(W0.lo),
       'kernel_curvature_upper':display(CURVATURE.hi),
       'positive_endpoints':out,'poisson_prime_endpoints':refined,'negative_controls':6,
       'scope':'finite rational scalar endpoints and stated elementary side conditions; analytic lemma separate'},indent=2))

if __name__=='__main__':main()
