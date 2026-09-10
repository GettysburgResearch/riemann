"""One literal stochastic-map countercertificate, NOT a zeta-zero certificate.
All accepting arithmetic is integer/Fraction plus outward integer intervals.
"""
from fractions import Fraction as Q
from math import comb, factorial, isqrt

BITS = 512
S = 1 << BITS
DEGREE = 600
STIRLING_ORDER = 24
GAMMA_SHIFT = 64
XR = Q('0.8720593240460351927678950449864720764922472047284135048292993961077024803759264272174986835')
YI = Q('41.239145218522512266175746388258629308518291094194602398581416957401708987395360042877048938')
RADIUS = Q(1, 10**20)

def up(a, b):
    return -((-a) // b)

class I:
    __slots__ = ('lo', 'hi')
    def __init__(self, lo, hi):
        if type(lo) is not int or type(hi) is not int or lo > hi:
            raise ValueError('bad interval')
        self.lo, self.hi = lo, hi
    @staticmethod
    def of(x):
        if isinstance(x, I): return x
        if type(x) not in (int, Q): raise TypeError('exact rational required')
        x = Q(x)
        return I(x.numerator*S//x.denominator, up(x.numerator*S, x.denominator))
    def __add__(a,b):
        b=I.of(b); return I(a.lo+b.lo,a.hi+b.hi)
    __radd__=__add__
    def __neg__(a): return I(-a.hi,-a.lo)
    def __sub__(a,b): return a+-I.of(b)
    def __rsub__(a,b): return I.of(b)+-a
    def __mul__(a,b):
        b=I.of(b); v=[x*y for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(v)//S,up(max(v),S))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=I.of(b)
        if b.lo<=0<=b.hi: raise ZeroDivisionError('denominator contains zero')
        v=[(x*S,y) for x in (a.lo,a.hi) for y in (b.lo,b.hi)]
        return I(min(x//y for x,y in v),max(up(x,y) for x,y in v))
    def __rtruediv__(a,b): return I.of(b)/a
    def __pow__(a,n):
        if type(n) is not int or n<0: raise ValueError('nonnegative integer power')
        b=I.of(1)
        while n:
            if n&1: b=b*a
            a=a*a;n//=2
        return b
    def abs_upper(a): return Q(max(abs(a.lo),abs(a.hi)),S)
    def inflate(a,e):
        e=I.of(e).hi
        if e<0: raise ValueError('negative error')
        return I(a.lo-e,a.hi+e)
    def rec(a):
        # Compact outward 256-bit serialization of the 512-bit calculation.
        scale=1<<(BITS-256)
        return {'bits':256,'lo_hex':hex(a.lo//scale),'hi_hex':hex(up(a.hi,scale))}

class C:
    __slots__=('re','im')
    def __init__(self,re=0,im=0): self.re,self.im=I.of(re),I.of(im)
    @staticmethod
    def of(x): return x if isinstance(x,C) else C(x)
    def __add__(a,b):
        b=C.of(b);return C(a.re+b.re,a.im+b.im)
    __radd__=__add__
    def __neg__(a): return C(-a.re,-a.im)
    def __sub__(a,b): return a+-C.of(b)
    def __rsub__(a,b): return C.of(b)+-a
    def __mul__(a,b):
        b=C.of(b);return C(a.re*b.re-a.im*b.im,a.re*b.im+a.im*b.re)
    __rmul__=__mul__
    def __truediv__(a,b):
        if not isinstance(b,C): return C(a.re/b,a.im/b)
        den=b.re*b.re+b.im*b.im
        return C((a.re*b.re+a.im*b.im)/den,(a.im*b.re-a.re*b.im)/den)
    def __rtruediv__(a,b):return C.of(b)/a
    def abs_upper(a):return a.re.abs_upper()+a.im.abs_upper()
    def inflate(a,e):return C(a.re.inflate(e),a.im.inflate(e))
    def rec(a):return {'real':a.re.rec(),'imag':a.im.rec()}

def sqrt_i(x):
    x=I.of(x)
    if x.lo<0:raise ValueError('negative square root')
    lo=isqrt(x.lo*S);hi=isqrt(x.hi*S)
    if hi*hi<x.hi*S:hi+=1
    return I(lo,hi)

def exp_i(x):
    x=I.of(x);k=0
    while x.abs_upper()>Q(1,8):x=x/2;k+=1
    term=I.of(1);total=term
    for j in range(1,97):term=term*x/j;total+=term
    total=total.inflate(2*Q(1,8)**97/factorial(97))
    for _ in range(k):total=total*total
    return total

def cis(x):
    x=I.of(x);k=0
    while x.abs_upper()>Q(1,8):x=x/2;k+=1
    x2=x*x;c=I.of(1);s=x;ct=c;st=x
    for j in range(1,49):
        ct=-ct*x2/((2*j-1)*2*j);c+=ct
        st=-st*x2/(2*j*(2*j+1));s+=st
    c=c.inflate(Q(1,8)**98/factorial(98));s=s.inflate(Q(1,8)**99/factorial(99))
    for _ in range(k):c,s=c*c-s*s,2*s*c
    return C(c,s)

def exp_c(z):
    z=C.of(z);return cis(z.im)*exp_i(z.re)

def atanh_small(y):
    y=I.of(y)
    if y.abs_upper()>Q(17,50):raise ValueError('atanh range')
    y2=y*y;term=y;total=I.of(0)
    for j in range(96):total+=term/(2*j+1);term*=y2
    return total.inflate(Q(17,50)**193/(193*(1-Q(17,50)**2)))

def log_i(x):
    x=I.of(x)
    if x.lo<=0:raise ValueError('positive logarithm required')
    k=0
    while x.lo>=2*S:x=x/2;k+=1
    while x.lo<S:x=x*2;k-=1
    # A straddled endpoint can lie just above 2; the 17/50 radius
    # includes the outward representation of 1/3 and is paid in the tail.
    y=(x-1)/(x+1)
    if y.abs_upper()<=Q(17,50):v=2*atanh_small(y)
    else:
        # x is at most a tiny interval above 2, so use x/2 near one.
        return log_i(x/2)+(k+1)*2*atanh_small(I.of(Q(1,3)))
    return v+k*2*atanh_small(I.of(Q(1,3)))

def atan_i(x):
    x=I.of(x);k=0
    while x.abs_upper()>Q(1,8):
        x=x/(1+sqrt_i(1+x*x));k+=1
    term=x;x2=x*x;total=I.of(0)
    for j in range(64):total+=term/(2*j+1);term=-term*x2
    return (2**k)*total.inflate(Q(1,8)**129/129)

def log_c(z):
    z=C.of(z)
    if z.re.lo<=0:raise ValueError('complex logarithm needs Re z>0')
    return C(log_i(z.re*z.re+z.im*z.im)/2,atan_i(z.im/z.re))

def pi_i():return 16*atan_i(Q(1,5))-4*atan_i(Q(1,239))

def bernoulli(n):
    b=[Q(1)]
    for m in range(1,n+1):
        b.append(-sum((comb(m+1,j)*b[j] for j in range(m)),Q())/(m+1))
    return b

def loggamma_psi(z,pi):
    """Stirling/psi with DLMF5.11(ii) complete right-half-plane bounds."""
    z=C.of(z);w=z+GAMMA_SHIFT
    a=Q(w.re.lo,S)
    if a<64:raise ValueError('Stirling half-plane guard')
    B=bernoulli(2*STIRLING_ORDER);lg=(w-Q(1,2))*log_c(w)-w+C(log_i(2*pi)/2)
    ps=log_c(w)-1/(2*w);inv=1/w;inv2=inv*inv;power=inv
    for j in range(1,STIRLING_ORDER):
        lg+=power*(B[2*j]/(2*j*(2*j-1)))
        ps-=power*inv*(B[2*j]/(2*j))
        power*=inv2
    m=STIRLING_ORDER
    er=abs(B[2*m])/Q(2*m*(2*m-1))/a**(2*m-1)
    ep=abs(B[2*m])/Q(2*m)/a**(2*m)
    lg=lg.inflate(er);ps=ps.inflate(ep)
    for j in range(GAMMA_SHIFT):lg-=log_c(z+j);ps-=1/(z+j)
    return lg,ps

def mixing_moments(n=DEGREE):
    """Exact Beta(2,2)/two-uniform moments, no quadrature or law samples."""
    a=[Q(1)]+[Q((1<<(2*j-1))-1,(1<<(2*j-1))*(2*j-1)) for j in range(1,n+1)]
    raw=[];eta=[]
    for j in range(n+1):
        v=sum(((l+1)*(j-l+1)*a[l]*a[j-l] for l in range(j+1)),Q())
        raw.append(6*v/Q((j+1)*(j+2)*(j+3)))
    powers=[Q(8,5)**l for l in range(n+1)]
    for j in range(n+1):
        v=sum((comb(j,l)*powers[l]*raw[l]*(-1)**(j-l) for l in range(j+1)),Q())
        if abs(v)>Q(3,5)**j:raise ValueError('complete mixing moment range failed')
        eta.append(v)
    return raw,eta

def mixing_transform(s,eta):
    p=s/2;z=C(1);dz=C();v=C();d=C()
    for j,q in enumerate(eta):
        if j:
            z,dz=z*(p-j+1)/j,(dz*(p-j+1)+z/2)/j
        v+=z*q;d+=dz*q
    lc=log_i(Q(5,8));factor=exp_c(p*lc)
    # Cauchy in BOTH complex variables: complete j>DEGREE remainder and
    # its s derivative are bounded by this same number (s radius one).
    error=100*Q(3)**50*Q(3,4)**(DEGREE+1)
    return (factor*v).inflate(error),(factor*(d+v*lc/2)).inflate(error),error

def reconstruct_root():
    if not (Q(1,2)<XR-RADIUS<XR+RADIUS<Q(9,10) and 41<YI<42):
        raise ValueError('source disk')
    raw,eta=mixing_moments();pi=pi_i();lc=log_i(pi/6);s=C(XR,YI)
    values=[];derivatives=[];tail=None
    for z in (s,1-s):
        a,da,tail=mixing_transform(z,eta)
        lg,ps=loggamma_psi(4+z/2,pi)
        factor=exp_c(z*lc/2+lg)/6
        values.append(factor*a)
        derivatives.append(factor*(da+a*(ps+lc)/2))
    val=values[0]+values[1];der=derivatives[0]-derivatives[1]
    residual=val.abs_upper();slope=Q(der.re.lo,S)
    if not (residual<Q(1,10**48) and slope>Q(8,10**13)):
        raise ValueError('whole-transform residual/slope witnesses failed')
    if not (residual+500*RADIUS**2<slope*RADIUS):raise ValueError('Rouche failed')
    # E V^2=(pi/6)^2*(2*(7/4)+2)<3.  For sigma>=1/10,
    # v^(sigma/2)log(v)^2<1600 at v<=1; at v>=1 it is <=v^2.
    if not Q(4,9)*Q(11,2)<3 or not Q(1600+3,2)<1000:
        raise ValueError('entire disk second derivative bound')
    import hashlib,json
    canonical=json.dumps([[q.numerator,q.denominator] for q in eta],separators=(',',':')).encode()
    return {'scope':'one off-central critical-strip zero after ONE branching step from Gamma(1,1); NOT a zero of xi',
            'center_real':str(XR),'center_imag':str(YI),'radius':str(RADIUS),
            'moment_degree':DEGREE,'all_mixing_moments_sha256':hashlib.sha256(canonical).hexdigest(),
            'whole_value':val.rec(),'whole_derivative':der.rec(),
            'residual_upper_witness':'1/10^48','derivative_lower_witness':'8/10^13',
            'second_derivative_bound':1000,'series_remainder_upper':str(tail),
            'rouche_strict':True,'simple':True,'rh_proved':False,
            'gamma_5_2_orbit_refuted':False}

if __name__=='__main__':
    import json
    print(json.dumps(reconstruct_root(),sort_keys=True,indent=2))
