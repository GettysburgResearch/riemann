"""Directed enclosure for ONE zero of a changed three-term theta transform.
No zeta zero is computed or certified. Standard-library integer arithmetic.
"""
from fractions import Fraction as Q
from math import factorial
import json
import argparse
from pathlib import Path
BITS=384
S=1<<BITS

def up(a,b): return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi):
        if type(lo) is not int or type(hi) is not int or lo>hi: raise ValueError('bad interval')
        self.lo,self.hi=lo,hi
    @staticmethod
    def of(x):
        if isinstance(x,I): return x
        if type(x) is not int and type(x) is not Q: raise TypeError('exact rational required')
        x=Q(x);return I(x.numerator*S//x.denominator,up(x.numerator*S,x.denominator))
    def __add__(a,b):
        b=I.of(b);return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a):return I(-a.hi,-a.lo)
    def __sub__(a,b):return a+-I.of(b)
    def __rsub__(a,b):return I.of(b)+-a
    def __mul__(a,b):
        b=I.of(b);v=[a.lo*b.lo,a.lo*b.hi,a.hi*b.lo,a.hi*b.hi]
        return I(min(v)//S,up(max(v),S))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=I.of(b)
        if b.lo<=0<=b.hi:raise ZeroDivisionError('zero interval')
        v=[(x*S,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(x//y for x,y in v),max(up(x,y) for x,y in v))
    def __rtruediv__(a,b):return I.of(b)/a
    def abs_upper(a):return Q(max(abs(a.lo),abs(a.hi)),S)
    def inflate(a,e):
        e=I.of(e).hi;return I(a.lo-e,a.hi+e)
    def rec(a):return {'lo_hex':hex(a.lo),'hi_hex':hex(a.hi),'bits':BITS}

class C:
    __slots__=('re','im')
    def __init__(self,re=0,im=0):self.re,self.im=I.of(re),I.of(im)
    @staticmethod
    def of(x):return x if isinstance(x,C) else C(x)
    def __add__(a,b):
        b=C.of(b);return C(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __neg__(a):return C(-a.re,-a.im)
    def __sub__(a,b):return a+-C.of(b)
    def __mul__(a,b):
        b=C.of(b);return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def __truediv__(a,b):
        if isinstance(b,C):raise TypeError('only real divisor needed')
        return C(a.re/b,a.im/b)
    def l1_upper(a):return a.re.abs_upper()+a.im.abs_upper()
    def rec(a):return {'real':a.re.rec(),'imag':a.im.rec()}


def expi(x):
    x=I.of(x);k=0
    while x.abs_upper()>Q(1,8):x=x/2;k+=1
    term=I.of(1);total=term
    for j in range(1,97):term=term*x/j;total+=term
    # |x|<=1/8: exponential remainder <= 2 |x|^97/97!.
    total=total.inflate(2*Q(1,8)**97/factorial(97))
    for _ in range(k):total=total*total
    return total

def cis(x):
    x=I.of(x);k=0
    while x.abs_upper()>Q(1,8):x=x/2;k+=1
    x2=x*x;c=I.of(1);s=x;ct=I.of(1);st=x
    for j in range(1,49):
        ct=-ct*x2/((2*j-1)*(2*j));c+=ct
        st=-st*x2/((2*j)*(2*j+1));s+=st
    c=c.inflate(Q(1,8)**98/factorial(98))
    s=s.inflate(Q(1,8)**99/factorial(99))
    for _ in range(k):c,s=c*c-s*s,2*s*c
    return C(c,s)

def atanq(x,terms):
    x=Q(x);v=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    err=x**(2*terms+1)/Q(2*terms+1)
    a=I.of(v);return a.inflate(err)

def pi_interval():return 16*atanq(Q(1,5),96)-4*atanq(Q(1,239),32)

XR=Q('67.8801896551476196444591034890974615868760577967044779253851906685118397')
YI=Q('0.4773438417708229856896978584442346997998462219509442426117227298339156')
RADIUS=Q(1,10**25)
DEGREE=80
HALF=Q(1,64)
CUTOFFS=(Q(9,4),Q(3,2),Q(1))


def integral_term(n,A,t,sign,pi):
    """Cell Taylor polynomial of exp(Au-pi*n*n*exp(2u)+sign*i*z*u).
    y=(u-t)/HALF; coefficient interval in y; exact even-moment integration.
    """
    q=pi*(n*n);b=q*expi(2*t)
    c0=cis(sign*XR*t)*expi(A*t-b-sign*YI*t)
    hs=[C(0)]
    for j in range(1,DEGREE+1):
        real=-b*Q(2**j,factorial(j))*HALF**j
        imag=0
        if j==1:real+=(A-sign*YI)*HALF;imag=sign*XR*HALF
        hs.append(C(real,imag))
    es=[c0]
    for m in range(1,DEGREE+1):
        es.append(sum((j*hs[j]*es[m-j] for j in range(1,m+1)),C())/m)
    val=sum((es[j]*Q(2, j+1) for j in range(0,DEGREE+1,2)),C())*HALF
    first=sum((es[j]*Q(2,j+2) for j in range(1,DEGREE+1,2)),C())*HALF**2
    derivative=C(0,sign)*(t*val+first)
    return val,derivative


def reconstruct():
    if not (0<XR<68 and 0<YI<Q(1,2)):raise ValueError('source box bounds')
    if not 9_000_000*Q(3,8)**190<Q(1,10**70):raise ValueError('infinite tail bound')
    if not 256*sum((Q(n**4,(6*n*n-5)**3) for n in range(1,4)),Q(0))<1000:
        raise ValueError('second derivative bound')
    for n,U in enumerate(CUTOFFS,1):
        power=up((5*(U+Q(1,8))+Q(68,8)).numerator,(5*(U+Q(1,8))+Q(68,8)).denominator)
        if 4*(4*n*n)**2*3**power>=10**13:raise ValueError('Cauchy circle bound')
    if not min(3*Q(8,3)**4*Q(3,2),12*Q(8,3)**3,27*Q(8,3)**2)>190:
        raise ValueError('tail starting exponent')
    pi=pi_interval();total=C();derivative=C();cells=0
    for n,U in enumerate(CUTOFFS,1):
        count=int(U/(2*HALF))
        if Q(count)*2*HALF!=U:raise ValueError('nonintegral cell coverage')
        for j in range(count):
            t=(2*j+1)*HALF
            for sign in (-1,1):
                va,da=integral_term(n,Q(9,2),t,sign,pi)
                vb,db=integral_term(n,Q(5,2),t,sign,pi)
                q=pi*n*n
                total+=va*(4*q*q)-vb*(6*q)
                derivative+=da*(4*q*q)-db*(6*q)
            cells+=1
    # Cauchy radius 1/8 around cell midpoints. On each circle:
    # exp(-q exp(2u)) has modulus <=1 since |Im u|<=1/8;
    # each full term, including coefficients and oscillation, is <10^13.
    # |u|<3 also bounds the z derivative by three times this.
    # h/r=1/8, six summands, total interval length <5.
    cauchy_error=Q(10**16)*Q(1,8)**(DEGREE+1)/(1-Q(1,8))
    # See manuscript: each complete omitted tail for j=0,1 is <10^-70.
    err=cauchy_error+Q(1,10**69)
    total=C(total.re.inflate(err),total.im.inflate(err))
    derivative=C(derivative.re.inflate(3*err),derivative.im.inflate(3*err))
    residual=total.l1_upper()
    # |F'|>=|Im F'|. The latter is strictly negative on its enclosure.
    if derivative.im.hi>=0:raise ValueError('derivative sign unproved')
    slope=Q(-derivative.im.hi,S)
    second_bound=Q(1000)
    rouche_rhs=slope*RADIUS
    rouche_lhs=residual+second_bound*RADIUS**2/2
    if not (YI-RADIUS>0 and YI+RADIUS<Q(1,2)):raise ValueError('disk outside band')
    if not rouche_lhs<rouche_rhs:raise ValueError('Rouche certificate failed')
    return {'scope':'one simple zero of F_3, NOT of Xi or zeta',
            'rh_proved':False,'theta_terms':3,'center_real':str(XR),'center_imag':str(YI),
            'radius':str(RADIUS),'cells':cells,'degree':DEGREE,
            'cutoffs':[str(x) for x in CUTOFFS],
            'F_center':total.rec(),'F_prime_center':derivative.rec(),
            'residual_upper':str(residual),'derivative_lower':str(slope),
            'cauchy_remainder_upper':str(cauchy_error),
            'each_omitted_tail_upper':'1/10^70',
            'second_derivative_bound':1000,
            'rouche_left':str(rouche_lhs),'rouche_right':str(rouche_rhs),
            'rouche_strict':True}

def strict_json(path):
    if path.is_symlink() or not path.is_file():raise ValueError('regular receipt required')
    if path.stat().st_size>20000:raise ValueError('oversize receipt')
    def pairs(rows):
        out={}
        for k,v in rows:
            if k in out:raise ValueError('duplicate JSON key')
            out[k]=v
        return out
    def bad(value):raise ValueError('noninteger JSON number')
    value=json.loads(path.read_text(),object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)
    if type(value) is not dict or not value:raise ValueError('nonempty object required')
    return value

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check',type=Path)
    args=ap.parse_args()
    expected=strict_json(args.check) if args.check else None
    result=reconstruct()
    if expected is not None and json.dumps(expected,sort_keys=True)!=json.dumps(result,sort_keys=True):
        raise ValueError('receipt differs from primitive reconstruction')
    print(json.dumps(result,sort_keys=True,indent=2))
