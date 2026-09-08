#!/usr/bin/env python3
"""Fixed, source-only dyadic xi matrix enclosure. Python integers only.

Every elementary operation rounds outwards on a 2^-640 grid. Special
functions are reconstructed with explicitly bounded Euler--Maclaurin tails.
The module does not evaluate zeros or call floating-point special functions.
"""
from fractions import Fraction as F
from math import isqrt, factorial, comb
from functools import lru_cache

BITS=640
SCALE=1<<BITS
DEG=4
EM_N=256
EM_M=48
GAMMA_SHIFT=128

class Ball:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None,raw=False):
        if raw:
            self.lo=int(lo); self.hi=int(hi)
        else:
            x=F(lo); y=x if hi is None else F(hi)
            self.lo=(x.numerator*SCALE)//x.denominator
            self.hi=-((-y.numerator*SCALE)//y.denominator)
        if self.lo>self.hi: raise ValueError('reversed enclosure')
    @staticmethod
    def coerce(x): return x if isinstance(x,Ball) else Ball(x)
    def __add__(self,o):
        o=self.coerce(o); return Ball(self.lo+o.lo,self.hi+o.hi,True)
    __radd__=__add__
    def __neg__(self): return Ball(-self.hi,-self.lo,True)
    def __sub__(self,o): return self+-self.coerce(o)
    def __rsub__(self,o): return self.coerce(o)+-self
    def __mul__(self,o):
        o=self.coerce(o); a=[self.lo*o.lo,self.lo*o.hi,self.hi*o.lo,self.hi*o.hi]
        return Ball(min(a)//SCALE,-((-max(a))//SCALE),True)
    __rmul__=__mul__
    def inv(self):
        if self.lo<=0<=self.hi: raise ValueError('division through zero')
        return Ball(F(SCALE,self.hi),F(SCALE,self.lo))
    def __truediv__(self,o): return self*self.coerce(o).inv()
    def __rtruediv__(self,o): return self.coerce(o)*self.inv()
    def __pow__(self,n):
        if not isinstance(n,int): raise TypeError('integer power only')
        if n<0: return self.inv()**(-n)
        out=Ball(1); x=self
        while n:
            if n&1: out=out*x
            n//=2
            if n: x=x*x
        return out
    def sqrt(self):
        if self.lo<0: raise ValueError('negative radicand')
        a=isqrt(self.lo*SCALE); b=isqrt(self.hi*SCALE)
        if b*b<self.hi*SCALE:b+=1
        return Ball(a,b,True)
    def widen(self,r):
        r=F(r)
        if r<0: raise ValueError('negative radius')
        k=-((-r.numerator*SCALE)//r.denominator)
        return Ball(self.lo-k,self.hi+k,True)
    def dump(self): return {'lo':str(self.lo),'hi':str(self.hi),'denominator_power_of_two':BITS}
    def decimal_bounds(self,digits=90):
        scale10=10**digits
        a=self.lo*scale10//SCALE; b=-((-self.hi*scale10)//SCALE)
        def fmt(z):
            sign='-' if z<0 else ''; ss=str(abs(z)).rjust(digits+1,'0')
            return sign+ss[:-digits]+'.'+ss[-digits:]
        return [fmt(a),fmt(b)]

ZERO=Ball(0)
def _atanh_log(y):
    # y is an exact rational in [1,2]; t in [0,1/3].
    t=(Ball(y)-1)/(Ball(y)+1); t2=t*t
    n=BITS//3+12; power=t; val=Ball(0)
    for j in range(n):
        val+=power*F(2,2*j+1); power*=t2
    # Positive remainder, bounded without using any floating-point logarithm.
    tail=F(2, (2*n+1)*3**(2*n+1))*F(9,8)
    return Ball(val.lo,val.hi+Ball(tail).hi,True)

@lru_cache(None)
def log2():return _atanh_log(F(2))
@lru_cache(None)
def log_rational(x):
    x=F(x)
    if x<=0: raise ValueError('nonpositive logarithm')
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/(F(2)**k)
    while y<1:k-=1;y*=2
    while y>2:k+=1;y/=2
    return _atanh_log(y)+k*log2()

def log_ball(x):
    x=Ball.coerce(x)
    a=log_rational(F(x.lo,SCALE)); b=log_rational(F(x.hi,SCALE))
    return Ball(a.lo,b.hi,True)

def exp_rational(x):
    x=F(x)
    if x==0:return Ball(1)
    if x<0:return exp_rational(-x).inv()
    k=0;y=x
    while y>F(1,8):y/=2;k+=1
    n=BITS//3+12; term=Ball(1); val=Ball(1)
    for j in range(1,n+1):term=term*Ball(y)/j;val+=term
    # Ratios in the omitted positive series are <=1/8.
    tail=F(8,7)*F(1,8)**(n+1)/factorial(n+1)
    val=Ball(val.lo,val.hi+Ball(tail).hi,True)
    for _ in range(k):val=val*val
    return val

def exp_ball(x):
    x=Ball.coerce(x)
    a=exp_rational(F(x.lo,SCALE));b=exp_rational(F(x.hi,SCALE))
    return Ball(a.lo,b.hi,True)

def atan_inverse(n):
    terms=BITS//4+16; x=F(1,n); s=F(0)
    for j in range(terms):s+=(-1)**j*x**(2*j+1)/(2*j+1)
    t=x**(2*terms+1)/(2*terms+1)
    return Ball(s-t,s+t)

@lru_cache(None)
def pi_ball():return 16*atan_inverse(5)-4*atan_inverse(239)

@lru_cache(None)
def bernoulli(n):
    b=[F(1)]
    for m in range(1,n+1):b.append(-sum(F(comb(m+1,k))*b[k] for k in range(m))/F(m+1))
    return tuple(b)

# Fixed-degree real interval power series.
def poly(x=0):return [Ball.coerce(x)]+[ZERO for _ in range(DEG)]
def padd(a,b):return [a[i]+b[i] for i in range(DEG+1)]
def pscale(a,x):return [ai*x for ai in a]
def pmul(a,b):return [sum((a[j]*b[i-j] for j in range(i+1)),ZERO) for i in range(DEG+1)]
def pinv(a):
    out=poly(a[0].inv())
    for n in range(1,DEG+1):out[n]=-sum((a[j]*out[n-j] for j in range(1,n+1)),ZERO)/a[0]
    return out
def ppow(a,n):
    if n<0:return ppow(pinv(a),-n)
    out=poly(1)
    while n:
        if n&1:out=pmul(out,a)
        n//=2
        if n:a=pmul(a,a)
    return out
def plog(a,constant=True):
    inv=pinv(a);out=poly(log_ball(a[0]) if constant else 0)
    for n in range(1,DEG+1):
        out[n]=sum(((j+1)*a[j+1]*inv[n-1-j] for j in range(n)),ZERO)/n
    return out
def pcompose(a,b):
    out=poly(0)
    for c in reversed(a):out=padd(pmul(out,b),poly(c))
    return out

def exp_linear(constant,slope):
    out=poly(exp_ball(constant))
    for n in range(1,DEG+1):out[n]=out[n-1]*slope/n
    return out

@lru_cache(None)
def zeta_uniform_error():
    m=2*EM_M
    rise=F(factorial(m+5),factorial(5))
    return abs(bernoulli(m)[m])*rise/F(factorial(m)*m*EM_N**m)

def zeta_jet(s0):
    if s0.lo<=Ball(F(5,4)).hi or s0.hi>=Ball(F(23,4)).lo:
        raise ValueError('uniform EM disk bound requires 5/4<s0<23/4')
    sp=poly(s0);sp[1]=Ball(1)
    out=poly(0)
    for n in range(1,EM_N):
        ln=log_rational(F(n));out=padd(out,exp_linear(-s0*ln,-ln))
    ln=log_rational(F(EM_N)); en=exp_linear(-s0*ln,-ln)
    den=padd(sp,poly(-1))
    out=padd(out,pscale(pmul(en,pinv(den)),EM_N))
    out=padd(out,pscale(en,F(1,2)))
    bb=bernoulli(2*EM_M)
    # normalized rising factorial avoids huge-prefactor interval inflation
    rising=poly(1)
    for j in range(1,2*EM_M):
        rising=pscale(pmul(rising,padd(sp,poly(j-1))),F(1,j))
        if j&1:
            k=(j+1)//2
            coef=bb[2*k]/F(2*k*EM_N**(2*k-1))
            out=padd(out,pscale(pmul(en,rising),coef))
    err=zeta_uniform_error()
    return [out[j].widen(err*4**j) for j in range(DEG+1)]

@lru_cache(None)
def gamma_uniform_error():
    m=2*EM_M
    return 2*abs(bernoulli(m)[m])/F(m*(m-1)*GAMMA_SHIFT**(m-1))

def log_gamma_half_jet(s0):
    z=poly(s0/2+GAMMA_SHIFT);z[1]=Ball(F(1,2))
    out=padd(pmul(padd(z,poly(F(-1,2))),plog(z)),pscale(z,-1))
    bb=bernoulli(2*EM_M);inv=pinv(z);inv2=pmul(inv,inv);power=inv
    for k in range(1,EM_M):
        out=padd(out,pscale(power,bb[2*k]/F(2*k*(2*k-1))))
        power=pmul(power,inv2)
    for k in range(GAMMA_SHIFT):
        zp=poly(s0/2+k);zp[1]=Ball(F(1,2))
        out=padd(out,pscale(plog(zp),-1))
    # The omitted constant log(2pi)/2 does not affect nonconstant jets.
    err=gamma_uniform_error()
    return [out[j].widen(err*4**j) for j in range(DEG+1)]

def h_jet(p):
    s0=(1+Ball(1+4*p).sqrt())/2
    sp=poly(s0);sp[1]=Ball(1)
    lx=padd(plog(sp),plog(padd(sp,poly(-1))))
    lx=padd(lx,pscale(sp,-log_ball(pi_ball())/2))
    lx=padd(lx,log_gamma_half_jet(s0))
    lx=padd(lx,plog(zeta_jet(s0),constant=False))
    # u-p=(2s0-1)delta+delta^2.
    delta=poly(0);root=2*s0-1;delta[1]=1/root
    for n in range(2,DEG+1):
        delta[n]=-sum((delta[j]*delta[n-j] for j in range(1,n)),ZERO)/root
    comp=pcompose(lx,delta)
    return [comp[j+1]*(j+1) for j in range(DEG)]

def dyadic_matrix():
    nodes=[1,2,4,8,16];jets={p:h_jet(p) for p in nodes}
    labels=[(p,r) for p in nodes for r in [0,1]];n=len(labels)
    q=[[ZERO for _ in range(n)] for _ in range(n)]
    for i,(p,r) in enumerate(labels):
        for j in range(i,n):
            s,ell=labels[j]
            if p==s:
                z=jets[p][r+ell+1]*((-1)**(r+ell+1)*factorial(r)*factorial(ell))
            else:
                d=s-p;diff=jets[p][0]-jets[s][0]
                if (r,ell)==(0,0):z=diff/d
                elif (r,ell)==(1,0):z=-jets[p][1]/d-diff/(d*d)
                elif (r,ell)==(0,1):z=jets[s][1]/d+diff/(d*d)
                else:z=-(jets[p][1]+jets[s][1])/(d*d)-2*diff/(d*d*d)
            q[i][j]=q[j][i]=z
    return labels,jets,q

def ldl(q):
    n=len(q);l=[[ZERO for _ in range(n)] for _ in range(n)];d=[]
    for i in range(n):
        di=q[i][i]-sum((l[i][k]*l[i][k]*d[k] for k in range(i)),ZERO)
        if di.lo<=0:raise ValueError('pivot %d not certified positive: %s'%(i+1,di.decimal_bounds()))
        d.append(di);l[i][i]=Ball(1)
        for j in range(i+1,n):
            l[j][i]=(q[j][i]-sum((l[j][k]*l[i][k]*d[k] for k in range(i)),ZERO))/di
    return d

def build_certificate(full=False):
    import hashlib,json
    labels,jets,q=dyadic_matrix();ds=ldl(q)
    payload={'basis':labels,'jets':{str(k):[z.dump() for z in v] for k,v in jets.items()},
             'matrix':[[x.dump() for x in row] for row in q],
             'ldl_pivots':[x.dump() for x in ds]}
    encoded=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
    cert={'arithmetic':'OUTWARD_DYADIC_RATIONAL','precision_bits':BITS,
          'EM_N':EM_N,'EM_M':EM_M,'gamma_shift':GAMMA_SHIFT,
          'basis':labels,'full_payload_sha256':hashlib.sha256(encoded).hexdigest(),
          'zeta_disk_error_less_than_10_to_minus_120':zeta_uniform_error()<F(1,10**120),
          'gamma_disk_error_less_than_10_to_minus_120':gamma_uniform_error()<F(1,10**120),
          'pivot_decimal_enclosures':[x.decimal_bounds(60) for x in ds],
          'positive_dimension':len(ds),'rh_proved':False,'all_rank_sign_proved':False}
    if not cert['zeta_disk_error_less_than_10_to_minus_120'] or not cert['gamma_disk_error_less_than_10_to_minus_120']:
        raise ValueError('analytic remainder ceiling failed')
    return {'certificate':cert,'payload':payload} if full else cert

if __name__=='__main__':
    import json,argparse
    from pathlib import Path
    ap=argparse.ArgumentParser();ap.add_argument('--full',action='store_true');ap.add_argument('--check')
    args=ap.parse_args();out=build_certificate(args.full)
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.check:
        if text!=Path(args.check).read_text():raise SystemExit('REFUSED: reconstructed certificate differs')
    print(text,end='')
