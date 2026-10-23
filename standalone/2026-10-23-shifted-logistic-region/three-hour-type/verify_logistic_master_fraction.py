"""Independent exact-rational replay of the logistic scalar master inequality.

All interval endpoints are Fractions, rounded outwards to 192 binary places
after each operation. No floating-point or transcendental library is used in
any bound. Analytic inputs and the global zero-free wrapper remain separate.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math

BITS=192
SCALE=1<<BITS


def down(x):
    x=Q(x)
    return Q((x.numerator*SCALE)//x.denominator,SCALE)


def up(x):
    x=Q(x)
    return -down(-x)


class I:
    def __init__(self,lo,hi=None):
        self.lo=down(lo)
        self.hi=up(lo if hi is None else hi)
        if self.lo>self.hi:
            raise ValueError('reversed interval')

    @staticmethod
    def get(x):
        return x if isinstance(x,I) else I(x)

    def __add__(self,x):
        x=I.get(x)
        return I(self.lo+x.lo,self.hi+x.hi)

    __radd__=__add__

    def __neg__(self):
        return I(-self.hi,-self.lo)

    def __sub__(self,x):
        return self+(-I.get(x))

    def __rsub__(self,x):
        return I.get(x)-self

    def __mul__(self,x):
        x=I.get(x)
        p=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return I(min(p),max(p))

    __rmul__=__mul__

    def __truediv__(self,x):
        x=I.get(x)
        if x.lo<=0<=x.hi:
            raise ZeroDivisionError('interval contains zero')
        return self*I(1/x.hi,1/x.lo)

    def __rtruediv__(self,x):
        return I.get(x)/self

    def __pow__(self,n):
        if n<0:
            return 1/(self**(-n))
        if n==0:
            return I(1)
        if self.lo>=0:
            return I(self.lo**n,self.hi**n)
        if self.hi<=0:
            return (-self)**n if n%2==0 else -((-self)**n)
        if n%2:
            return I(self.lo**n,self.hi**n)
        return I(0,max(self.lo**n,self.hi**n))


def check(ok,label):
    if not ok:
        raise RuntimeError(label)


def sincos(x,sine):
    x=Q(x)
    term=x if sine else Q(1)
    total=term
    for j in range(1,40):
        left=2*j if sine else 2*j-1
        term*=-x*x/(left*(left+1))
        total+=term
    left=80 if sine else 79
    nxt=term*(-x*x)/(left*(left+1))
    return I(min(total,total+nxt),max(total,total+nxt))


def exp_point(x):
    x=Q(x)
    if x<0:
        return 1/exp_point(-x)
    squarings=0
    while x>1:
        x/=2
        squarings+=1
    term=Q(1)
    total=term
    for n in range(1,65):
        term*=x/n
        total+=term
    # exp(x)<=3 for 0<=x<=1, so Taylor's Lagrange remainder is enclosed.
    rem=3*x**65/math.factorial(65)
    out=I(total,total+rem)
    for _ in range(squarings):
        out=out**2
    return out


def exp_i(x):
    x=I.get(x)
    return I(exp_point(x.lo).lo,exp_point(x.hi).hi)


def log_unit(x):
    x=Q(x)
    check(1<=x<=2,'log normalization')
    z=(x-1)/(x+1)
    total=sum((2*z**(2*j+1)/(2*j+1) for j in range(80)),Q(0))
    rem=2*z**161/(161*(1-z*z))
    return I(total,total+rem)


LOG2=log_unit(Q(2))


def log_point(x):
    x=Q(x)
    check(x>0,'positive logarithm argument')
    k=0
    while x>=2:
        x/=2
        k+=1
    while x<1:
        x*=2
        k-=1
    return log_unit(x)+k*LOG2


def log_i(x):
    x=I.get(x)
    return I(log_point(x.lo).lo,log_point(x.hi).hi)


THETA=Q(5669,5000)
ST,CT=sincos(THETA,True),sincos(THETA,False)
S2,C2=sincos(2*THETA,True),sincos(2*THETA,False)
TAN=ST/CT
COT=CT/ST
SEC2=1/(CT**2)
U=2*THETA*COT
W0=SEC2*(THETA*TAN+3*THETA*COT-3)
A1=Q(865534,497079)
AP=Q(2919857,828465)
WDEGREE=24
JLAST=48


def trig_moment(n,sine):
    """Direct integral power series, independent of a moment recurrence.

    Integral v^n exp(i tan(theta)v)dv = U^(n+1) *
    sum_m (2i theta)^m/[m!(n+m+1)].
    """
    total=Q(0)
    for m in range(1 if sine else 0,65,2):
        sign=(-1)**((m-1)//2 if sine else m//2)
        total+=sign*(2*THETA)**m/(math.factorial(m)*(n+m+1))
    # The full complex exponential tail after degree64 bounds each part.
    # exp(2theta)<10 and U<1.1 are independently checked below.
    tail=10*Q(23,10)**65/math.factorial(65)
    return U**(n+1)*I(total-tail,total+tail)


CM=[trig_moment(n,False) for n in range(WDEGREE+2)]
SM=[trig_moment(n,True) for n in range(WDEGREE+1)]
MOMENTS=[]
for n in range(WDEGREE+1):
    MOMENTS.append(SEC2*((SEC2*THETA*COT-1)*CM[n]
       -SEC2*CM[n+1]/2+(2*THETA*COT-2)*U**(n+1)/(n+1)
       -U**(n+2)/(n+2)+(2*COT-C2/S2)*SM[n]))


def W(z):
    z=I.get(z)
    check(z.lo>=-1 and z.hi<=1,'W domain')
    # Direct polynomial sum, rather than the other replay's Horner scheme.
    out=I(0)
    for n,moment in enumerate(MOMENTS):
        out+=moment*((-z)**n)/math.factorial(n)
    return out+I(Q(-1,10**20),Q(1,10**20))


def J(z,a):
    z,a=I.get(z),I.get(a)
    b=z+a
    check(a.lo>0 and b.lo>0,'J domain')
    term=1/(2*b)
    total=term
    for n in range(1,JLAST+1):
        term*=n*a/(2*(b+n*a))
        total+=term
    tail=1/(2**(JLAST+1)*b)
    return total+I(0,tail.hi)


def margin(A,l):
    A,l=I.get(A),I.get(l)
    c=log_i(16+10**10*exp_i(-l))
    # x/(x+y) is increasing in x and decreasing in positive y.
    mu=I(l.lo/(l.lo+c.hi),l.hi/(l.hi+c.lo))
    eta=A/l
    sigma=1-A/(l+c)
    a=2*sigma-1
    z0=sigma-1
    z1=z0+eta
    z2=sigma-eta
    base=A1*W(1-mu)-W(-mu)
    correction=eta*W0*(A1/z2+J(z0,a)-A1*J(z1,a)-A1*J(z2,a))
    error=1000*eta**3*(1/(z0+a)**3+A1/(z1+a)**3+A1/z2**3)
    resource=W0*(A*AP/4-Q(15063,5000)*eta/2)+Q(1,10**7)
    return base+correction-error-resource


def main():
    check(W0.lo>Q(567,100) and W0.hi<6 and U.hi<Q(11,10),'kernel constants')
    check(exp_point(2*THETA).hi<10,'trig moment tail exponential')
    check(exp_point(Q(11,10)).hi<Q(31,10),'W tail exponential')
    check(Q(66,10)*Q(31,10)*Q(11,10)**25/math.factorial(25)<Q(1,10**20),'W remainder')
    check(exp_point(Q(21233,1000)*Q(25,121)).hi<81,'Littlewood endpoint')
    check(exp_point(Q(28)).hi<3*10**12,'verified height endpoint')
    check(Q(25,121)/28<Q(3,400),'eta domain')
    check((1-I(Q(25,121))/(28+log_point(Q(16)))).lo>Q(99,100),'sigma domain')
    pending=[(Q(0),Q(25,121),Q(28),Q(81),0)]
    accepted=[]
    evaluations=0
    while pending:
        al,ah,ll,lh,depth=pending.pop()
        value=margin(I(al,ah),I(ll,lh))
        evaluations+=1
        if value.lo>0:
            accepted.append({'A':[str(al),str(ah)],'log_t':[str(ll),str(lh)],
                             'margin_lower':str(value.lo),'margin_upper':str(value.hi)})
            continue
        if depth>=32:
            raise RuntimeError('unresolved rectangle '+str((al,ah,ll,lh,value.lo,value.hi)))
        # Alternating coordinate bisection is independent of sensitivity tuning.
        if depth%2==0:
            m=(ll+lh)/2
            pending.extend([(al,ah,ll,m,depth+1),(al,ah,m,lh,depth+1)])
        else:
            m=(al+ah)/2
            pending.extend([(al,m,ll,lh,depth+1),(m,ah,ll,lh,depth+1)])
    # The same scalar resource must reject a deliberately overlarge A.
    bad=margin(I(Q(1,4)),I(Q(81)))
    check(bad.hi<0,'negative control: overlarge claimed improvement')
    area=Q(0)
    for i,row in enumerate(accepted):
        al,ah=map(Q,row['A'])
        ll,lh=map(Q,row['log_t'])
        check(0<=al<ah<=Q(25,121) and 28<=ll<lh<=81,'box containment')
        area+=(ah-al)*(lh-ll)
        for old in accepted[:i]:
            bl,bh=map(Q,old['A'])
            ml,mh=map(Q,old['log_t'])
            check(not (max(al,bl)<min(ah,bh) and max(ll,ml)<min(lh,mh)),
                  'overlapping box interiors')
    check(area==Q(25,121)*53,'exact area coverage')
    minimum=min(Q(row['margin_lower']) for row in accepted)
    out={'status':'pass','scope':'scalar logistic master inequality only; analytic/global inputs separate',
         'arithmetic':'exact Fraction intervals rounded outward to 192 binary places',
         'domain':{'A':['0','25/121'],'log_t':['28','81']},
         'W_degree':WDEGREE,'J_last_index':JLAST,'accepted_boxes':len(accepted),
         'evaluations':evaluations,'coverage_area_rational':str(area),
         'minimum_certified_lower_rational':str(minimum),
         'minimum_certified_lower_decimal':float(minimum),'negative_controls':1,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'boxes':accepted}
    dest=Path(__file__).with_name('LOGISTIC_FRACTION_CERTIFICATE.json')
    dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='boxes'},sort_keys=True))


if __name__=='__main__':
    main()
