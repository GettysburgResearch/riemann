#!/usr/bin/env python3
"""Independent exact-rational scalar and selected primitive checks.
The selected kernel checks are diagnostics, not a substitute for the complete
MPFR table and exhaustive six-dimensional cover.
"""
from fractions import Fraction as F
from math import isqrt, factorial
from dataclasses import dataclass
import argparse, json
@dataclass(frozen=True)
class I:
    lo:F
    hi:F
    def __post_init__(self):
        if self.lo>self.hi: raise ValueError('reversed interval')
        den=1<<256
        lo=F(self.lo)*den; hi=F(self.hi)*den
        object.__setattr__(self,'lo',F(lo.numerator//lo.denominator,den))
        object.__setattr__(self,'hi',F(-((-hi).numerator//(-hi).denominator),den))
    @staticmethod
    def exact(x):
        f=F(x);return I(f,f)
    def __add__(self,b):
        b=cv(b);return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-cv(b)
    def __rsub__(self,b):return cv(b)+-self
    def __mul__(self,b):
        b=cv(b);p=[x*y for x in (self.lo,self.hi) for y in (b.lo,b.hi)];return I(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=cv(b)
        if b.lo<=0<=b.hi:raise ValueError('zero denominator')
        return self*I(1/b.hi,1/b.lo)
    def __pow__(self,n):
        if n<0:raise ValueError('negative power')
        ans=I.exact(1)
        for _ in range(n):ans=ans*self
        return ans

def cv(x):return x if isinstance(x,I) else I.exact(x)
def root(q,bits=224):
    q=F(q);d=1<<bits;n=isqrt(q.numerator*d*d//q.denominator)
    return I(F(n,d),F(n+1,d))
def atan_inv(n):
    a=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(100)),F(0))
    # last retained term negative; first omitted positive
    return I(a,a+F(1,201*n**201))
PI=16*atan_inv(5)-4*atan_inv(239)
Q=root(F(1,2))
def sincos(x,cosine=False):
    # Range reduction by an ENCLOSURE of pi/2, integer chosen from rational midpoint.
    x=cv(x);z=((x.lo+x.hi)/2)/((PI.lo+PI.hi)/4)
    k=(z+F(1,2)).numerator//(z+F(1,2)).denominator
    u=x-k*PI/2
    if not (-1<=u.lo<=u.hi<=1):raise ValueError('failed range reduction')
    ss=sum(((-1)**j*u**(2*j+1)/factorial(2*j+1) for j in range(25)),I.exact(0))
    cc=sum(((-1)**j*u**(2*j)/factorial(2*j) for j in range(25)),I.exact(0))
    ss=ss+I(-F(1,factorial(51)),F(1,factorial(51)))
    cc=cc+I(-F(1,factorial(50)),F(1,factorial(50)))
    seq=[cc,-ss,-cc,ss] if cosine else [ss,cc,-ss,-cc]
    return seq[k%4]
C=Q*sincos(Q,True)/sincos(Q)
def scalar_bound(n,b,pressure):
    b=F(b);eta=F(n-1,n);q=b*(n-6)
    cap=I.exact(q) if q<=F(n,n-1) else 2*root(eta*q)-1+q/n
    h=F(3,2)-C
    bound=(h-F(6*(n-1),pressure*n))/(1-cap/n)
    return bound,cap,q

def decimal_enclosure(a,digits=18):
    d=10**digits;l=(a.lo*d).numerator//(a.lo*d).denominator
    h=-((-a.hi*d).numerator//(-a.hi*d).denominator)
    return {'lower_numerator':l,'upper_numerator':h,'denominator':d}

def kernel_point(x):
    if x==0:return I.exact(1),I.exact(0),None
    a=PI*F(x);u=a-Q;v=a+Q;k0=sincos(Q)/Q
    def triple(t):
        ss=sincos(t);cc=sincos(t,True)
        return ss/t,(t*cc-ss)/(t**2),((2-t**2)*ss-2*t*cc)/(t**3)
    U=triple(u);V=triple(v)
    k=(U[0]+V[0])/(2*k0);kp=PI*(U[1]+V[1])/(2*k0);kpp=PI**2*(U[2]+V[2])/(2*k0)
    return k**2,2*k*kp,2*(kp**2+k*kpp)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--table');args=ap.parse_args()
    h,c,q=scalar_bound(308,F(13777,4000000),3433)
    old,_,_=scalar_bound(280,F(19,5000),3000)
    if not h.lo>F(6730308386381655,10**16):raise RuntimeError('new scalar floor failed')
    if not h.hi<F(6730308386381656,10**16):raise RuntimeError('new scalar ceiling failed')
    if not c.hi<2*root(2).lo-1 or not F(308,307)<q<2:raise RuntimeError('block range')
    out={'new_constant':decimal_enclosure(h),'old_280_constant':decimal_enclosure(old),
         'gain':decimal_enclosure(h-old),'distinct_constant':decimal_enclosure((1+h)/2),
         'q':str(q),'block':308,'pressure_denominator':3433,'lower_local':str(F(13777,4000000)),
         'phi':decimal_enclosure(c)}
    g=[F(n,10**12) for n in [1045037800304,1977075744062,1041610314108,1986449992801,1989188338767,1046116442247]]
    witness=I.exact(sum(g)/3433)
    for span in range(1,7):
        for start in range(7-span):
            witness=witness+F(2,7-span)*kernel_point(sum(g[start:start+span]))[0]
    if not witness.hi<F(3444256,10**9):raise RuntimeError('rational near-sharp witness failed')
    out['rational_witness_value']=decimal_enclosure(witness)
    out['rational_witness_gaps']=[str(x) for x in g]
    if args.table:
        indexes=[0,1,17,1600,1799,1800,1801,3800,7614,7999,8000,8301,12001,16804,24017,32000,47001,80000,96032]
        cells=[3800,3827,4000,4180,4747,7264,7933,9268,10673,16000,24000,45388,47296]
        with open(args.table) as f:
            hdr=f.readline().split()
            if hdr[:3]!=['MPFR_KERNEL_V1','4000','48016']:raise RuntimeError('table metadata')
            points={}
            for j in range(96033):
                row=f.readline().split()
                if j in indexes:points[j]=[F.from_float(float.fromhex(x)) for x in row]
            tabcells={}
            for i in range(48016):
                row=f.readline().split()
                if i in cells:tabcells[i]=[F.from_float(float.fromhex(x)) for x in row]
            if f.read().strip():raise RuntimeError('extra table rows')
        for j,row in points.items():
            w,dw,_=kernel_point(F(j,8000))
            if not row[0]<=w.lo<=w.hi<=row[1] or not row[2]<=dw.lo<=dw.hi<=row[3]:
                raise RuntimeError(f'independent point comparison {j} failed')
        for i,(wl,d2l) in tabcells.items():
            for off in [F(0),F(1,2),F(1)]:
                w,_,d2=kernel_point((i+off)/4000)
                if not wl<=w.lo or not d2l<=d2.lo:raise RuntimeError(f'cell sample {i} failed')
        out['independent_selected_point_rows']=len(points);out['independent_selected_cell_sample_points']=len(cells)*3
    print(json.dumps(out,sort_keys=True,indent=2))
if __name__=='__main__': main()
