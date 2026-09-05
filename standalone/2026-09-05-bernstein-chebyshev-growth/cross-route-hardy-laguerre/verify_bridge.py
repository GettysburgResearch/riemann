#!/usr/bin/env python3
"""Bounded exact checks; does not establish RH or all-section positivity."""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib, json, sys

COUNT = 0

def check(ok: bool, name: str) -> None:
    global COUNT
    if not ok:
        raise ValueError('CHECK_FAILED: ' + name)
    COUNT += 1

@dataclass(frozen=True)
class G:
    re: F
    im: F = F(0)
    def __post_init__(self):
        object.__setattr__(self, 're', F(self.re))
        object.__setattr__(self, 'im', F(self.im))
    @staticmethod
    def cast(z): return z if isinstance(z,G) else G(F(z))
    def __add__(self,z):
        z=G.cast(z); return G(self.re+z.re,self.im+z.im)
    __radd__=__add__
    def __neg__(self): return G(-self.re,-self.im)
    def __sub__(self,z): return self+-G.cast(z)
    def __rsub__(self,z): return G.cast(z)+-self
    def __mul__(self,z):
        z=G.cast(z); return G(self.re*z.re-self.im*z.im,self.re*z.im+self.im*z.re)
    __rmul__=__mul__
    def conj(self): return G(self.re,-self.im)
    def norm2(self): return self.re*self.re+self.im*self.im
    def __truediv__(self,z):
        z=G.cast(z); d=z.norm2()
        if not d: raise ZeroDivisionError('Gaussian denominator')
        p=self*z.conj(); return G(p.re/d,p.im/d)
    def __rtruediv__(self,z): return G.cast(z)/self
    def __pow__(self,n):
        if n<0: return (1/self)**(-n)
        p=G(1); v=self
        while n:
            if n&1:p=p*v
            n//=2;v=v*v
        return p

B=F(3,2); I=G(0,1)

def spectrum_matrix(Z,dim):
    out=[[G(0) for _ in range(dim)] for _ in range(dim)]
    for z,m in Z:
        q=-I*z/(B-I*z); p=I*z/(B+I*z); c=B*B/(B*B+z*z)**2
        qs=[q**j for j in range(dim)]; ps=[p**j for j in range(dim)]
        for i in range(dim):
            for j in range(dim):out[i][j]+=m*c*qs[i]*ps[j]
    for row in out:
        for z in row:check(z.im==0,'matrix real')
    return [[z.re for z in row] for row in out]

def safe_matrix_from_spectrum_jet(Z,dim):
    # Algebraic source route: Taylor coefficients of L at b, then (A7).
    n=dim-1
    L=[sum((m*((-1)**j)/(B-I*z)**(j+1) for z,m in Z),G(0)) for j in range(n+2)]
    num=[L[1]-L[0]/B]+L[2:]
    g=[-sum((num[k]*F((-1)**(j-k))/(2*B)**(j-k+1) for k in range(j+1)),G(0)) for j in range(n+1)]
    Gc=[g[0]]+[sum((g[j]*B**j*comb(k-1,j-1) for j in range(1,k+1)),G(0)) for k in range(1,n+1)]
    out=[]
    for i in range(dim):
        row=[]
        for j in range(dim):
            q=sum((B*Gc[k]*F(comb(i+j-k,j),2**(i+j-k+1)) for k in range(i+1)),G(0))
            q+=sum((B*Gc[k]*F(comb(i+j-k,i),2**(i+j-k+1)) for k in range(j+1)),G(0))
            check(q.im==0,'safe-jet finite matrix real');row.append(q.re)
        out.append(row)
    return out

def elementary_source_checks():
    # Laplace identities for the constant, pole and gamma terms are rational.
    for r in (F(2),F(5,2),F(3),F(4)):
        check((1-r/B)/(B*B-r*r)==1/(B*(B+r)),'constant inverse source')
        for c in (F(-1,2),F(5,2),F(9,2),F(13,2)):
            direct=(1/(r+c)-(r/B)/(B+c))/(B*B-r*r)
            inverse=(1/(r+c)-(c/B)/(r+B))/(B*B-c*c)
            check(direct==inverse,'pole inverse source')
            if c> B:
                gamma=1/(B*(c+B)*(r+B))-inverse
                check(gamma==(1/(r+c)-1/(r+B))/(c*c-B*B),'paired gamma source')
    # Prime atom at n=k^2 and half-integral r: exponential factors are rational.
    for k in (2,3,5,7):
        for twicer in (5,7,9):
            r=F(twicer,2); nr=F(1,k**twicer);nb=F(1,k**3)
            direct=(-nr+(r/B)*nb)/(B*B-r*r)
            # Integral of -e^-b ell cosh(bx)/b on [0,ell]
            # plus -cosh(b ell)e^-bx/b on [ell,infinity).
            first=-nb/(2*B)*((1-nr/nb)/(r-B)+(1-nr*nb)/(r+B))
            second=-(1/nb+nb)/(2*B)*nr*nb/(r+B)
            check(direct==first+second,'prime atom piecewise inverse source')
    for j in range(1,25):
        c=2*j+F(1,2)
        check(1/(c*c-B*B)==F(1,3*(2*j-1))-F(1,6*(j+1)),'gamma telescoping')
        check(c*c-B*B>=4*j*j,'gamma tail denominator')
    # Rational constants used in the global trace-norm and shell ceilings.
    check(F(5,2)+F(2,3)+F(2,5)+F(4,3)*19 < 30,'nuclear norm ceiling')
    check(F(6*24,1)**2*8 < 200**2*5,'projection tail ceiling')
    for j in range(1,20):check(4**j>=4*j,'dyadic tail exponential control')

def ldl(A):
    n=len(A); L=[[F(int(i==j)) for j in range(n)] for i in range(n)]; d=[]
    for i in range(n):
        d.append(A[i][i]-sum(L[i][j]**2*d[j] for j in range(i)))
        if d[-1]==0:raise ValueError('zero LDL pivot')
        for k in range(i+1,n):
            L[k][i]=(A[k][i]-sum(L[k][j]*L[i][j]*d[j] for j in range(i)))/d[i]
    for i in range(n):
        for j in range(n):
            check(sum(L[i][k]*d[k]*L[j][k] for k in range(n))==A[i][j],'LDL reconstruction')
    return L,d

# Outward rational arithmetic with a fixed decimal grid. No binary floats.
DEN=10**80
@dataclass(frozen=True)
class V:
    lo:F
    hi:F
    def __post_init__(self):
        if self.lo>self.hi:raise ValueError('reversed interval')
    @staticmethod
    def cast(x):return x if isinstance(x,V) else V(F(x),F(x))
    @staticmethod
    def bound(lo,hi):
        lo=F(lo);hi=F(hi)
        return V(F((lo*DEN).__floor__(),DEN),F((hi*DEN).__ceil__(),DEN))
    def __add__(self,x):
        x=V.cast(x);return V.bound(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self):return V(-self.hi,-self.lo)
    def __sub__(self,x):return self+-V.cast(x)
    def __rsub__(self,x):return V.cast(x)+-self
    def __mul__(self,x):
        x=V.cast(x);p=[self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi]
        return V.bound(min(p),max(p))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=V.cast(x)
        if x.lo<=0<=x.hi:raise ZeroDivisionError('interval meets zero')
        return self*V.bound(1/x.hi,1/x.lo)
    def __rtruediv__(self,x):return V.cast(x)/self
    def __pow__(self,n):
        if n<0:return (1/self)**(-n)
        a=V.cast(1)
        for _ in range(n):a=a*self
        return a

def atan_inv(n,terms=80):
    t=sum((F((-1)**j,(2*j+1)*n**(2*j+1)) for j in range(terms)),F(0))
    e=F((-1)**terms,(2*terms+1)*n**(2*terms+1))
    return V.bound(min(t,t+e),max(t,t+e))

def log_rat(x,terms=180):
    x=F(x)
    if x<=0:raise ValueError('log domain')
    k=0
    while x>2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def base(t):
        y=(t-1)/(t+1)
        # Exact rational summation, then one outward rounding.
        a=sum((y**(2*j+1)/(2*j+1) for j in range(terms)),F(0))*2
        e=2*y**(2*terms+1)/((2*terms+1)*(1-y*y))
        return V.bound(a,a+e)
    return base(x)+k*base(F(2))

def log_iv(x):
    x=V.cast(x);return V(log_rat(x.lo).lo,log_rat(x.hi).hi)

def bernoulli(n):
    a=[F(0)]*(n+1);out=[]
    for m in range(n+1):
        a[m]=F(1,m+1)
        for j in range(m,0,-1):a[j-1]=j*(a[j-1]-a[j])
        out.append(a[0])
    return out

def conv(a,b,n):
    out=[V.cast(0) for _ in range(n+1)]
    for i in range(min(len(a),n+1)):
        for j in range(min(len(b),n+1-i)):out[i+j]+=a[i]*b[j]
    return out

def reciprocal(a,n):
    out=[1/a[0]]
    for k in range(1,n+1):out.append(-sum((a[j]*out[k-j] for j in range(1,k+1)),V.cast(0))/a[0])
    return out

def rising_series(start,degree,n):
    a=[V.cast(1)]+[V.cast(0)]*n
    for j in range(degree):a=conv(a,[V.cast(start+j),V.cast(1)],n)
    return a

def actual_safe_matrix(dim=4):
    N=64;m=12;kmax=2*dim; bs=bernoulli(2*m)
    check(bs[2]==F(1,6) and bs[24]==F(-236364091,2730),'Bernoulli anchors')
    logs={n:log_rat(F(n)) for n in range(1,N+1)}; LN=logs[N]
    def expjet(L):return [(-L)**j/factorial(j) for j in range(kmax+1)]
    z=[V.cast(0) for _ in range(kmax+1)]
    for n in range(1,N):
        e=expjet(logs[n])
        for j in range(kmax+1):z[j]+=e[j]/(n*n)
    e=expjet(LN)
    tail=conv(e,[V.cast((-1)**j) for j in range(kmax+1)],kmax)
    for j in range(kmax+1):z[j]+=tail[j]/N+e[j]/(2*N*N)
    for k in range(1,m+1):
        c=bs[2*k]/factorial(2*k)/N**(2*k+1)
        t=conv(rising_series(2,2*k-1,kmax),e,kmax)
        for j in range(kmax+1):z[j]+=c*t[j]
    # Cauchy circle |s-2|=1/4, Bernstein periodic bound |B_24({x})|<=|B_24|.
    rising=F(1)
    for j in range(24):rising*=F(9,4)+j
    R0=abs(bs[24])*rising/factorial(24)/24/N**24
    for j in range(kmax+1):
        err=R0*4**j;z[j]+=V(-err,err)
    check(z[0].lo>1,'zeta2 positive')
    zi=reciprocal(z,kmax-1)
    lz=conv([(j+1)*z[j+1] for j in range(kmax)],zi,kmax-1)
    # gamma_E from harmonic Euler--Maclaurin.
    gam=V.cast(sum((F(1,j) for j in range(1,N)),F(0)))-LN+F(1,2*N)
    for k in range(1,m+1):gam+=bs[2*k]/(2*k*N**(2*k))
    err=abs(bs[24])/(24*N**24);gam+=V(-err,err)
    pi=16*atan_inv(5)-4*atan_inv(239);logpi=log_iv(pi)
    def zeta_int(k):
        ans=V.cast(sum((F(1,j**k) for j in range(1,N)),F(0))+F(1,(k-1)*N**(k-1))+F(1,2*N**k))
        for r in range(1,m+1):
            rising=F(factorial(k+2*r-2),factorial(k-1))
            ans+=bs[2*r]*rising/factorial(2*r)/N**(k+2*r-1)
        rising=F(factorial(k+23),factorial(k-1))
        err=abs(bs[24])*rising/factorial(24)/(k+23)/N**(k+23)
        return ans+V(-err,err)
    # L_j = [h^j] (xi'/xi)(2+h).
    L=[]
    for j in range(kmax):
        k=j+1
        arch=V.cast(F((-1)**(k+1),2**k)+(-1)**(k+1))
        if k==1:arch+=-(gam+logpi)/2
        else:arch+=((-1)**k)*zeta_int(k)/2**k
        L.append(lz[j]+arch)
    # g(b+h) = -((L_1-L_0/b)+L_2 h+...)/(2b+h)
    n=2*dim-2
    num=[L[1]-L[0]/B]+L[2:n+2]
    g=conv([-x for x in num],[V.cast(F((-1)**j,(2*B)**(j+1))) for j in range(n+1)],n)
    Gc=[g[0]]
    for k in range(1,n+1):Gc.append(sum((g[j]*B**j*comb(k-1,j-1) for j in range(1,k+1)),V.cast(0)))
    A=[[V.cast(0) for _ in range(dim)] for _ in range(dim)]
    A[0][0]=B*Gc[0]
    # Boundary coefficients are needed up to 2*dim-2 before filling the square.
    boundary=[B*Gc[0]]
    for k in range(1,n+1):boundary.append((boundary[-1]+B*Gc[k])/2)
    for i in range(dim):A[i][0]=A[0][i]=boundary[i]
    for i in range(1,dim):
        for j in range(1,dim):A[i][j]=(A[i-1][j]+A[i][j-1])/2
    # Important: the harmonic recurrence alone makes the matrix from its first row.
    # Exact source matrix coefficient extraction independently uses the full numerator.
    for i in range(dim):
        for j in range(dim):
            q=V.cast(0)
            for k in range(i+1):q+=B*Gc[k]*F(comb(i+j-k,j),2**(i+j-k+1))
            for k in range(j+1):q+=B*Gc[k]*F(comb(i+j-k,i),2**(i+j-k+1))
            check(max(A[i][j].lo,q.lo)<=min(A[i][j].hi,q.hi),'actual two matrix constructions overlap')
    Lv=[[V.cast(int(i==j)) for j in range(dim)] for i in range(dim)]; piv=[]
    for i in range(dim):
        d=A[i][i]-sum((Lv[i][j]**2*piv[j] for j in range(i)),V.cast(0));piv.append(d)
        check(d.lo>0,'actual source LDL pivot '+str(i))
        for k in range(i+1,dim):
            Lv[k][i]=(A[k][i]-sum((Lv[k][j]*Lv[i][j]*piv[j] for j in range(i)),V.cast(0)))/d
    return {'dimension':dim,'N':N,'m':m,'cauchy_remainder_bound':str(R0),
            'L0':ivjson(L[0]),'pivots':[ivjson(x) for x in piv],
            'matrix':[[ivjson(x) for x in row] for row in A]}

def ivjson(x):return {'lower':str(x.lo),'upper':str(x.hi)}

def run():
    spectra=[[(G(1),1),(G(-1),1)],
             [(G(1),2),(G(-1),2),(G(3),1),(G(-3),1)],
             [(G(1),1),(G(-1),1)]+[(G(x,y),1) for x in (3,-3) for y in (F(1,4),F(-1,4))]]
    controls=[]
    elementary_source_checks()
    for ind,Z in enumerate(spectra):
        T=spectrum_matrix(Z,13)
        U=safe_matrix_from_spectrum_jet(Z,7)
        for i in range(7):
            for j in range(7):check(U[i][j]==T[i][j],'independent safe-source matrix equality')
        for i in range(12):
            for j in range(12):check(T[i][j]==T[j][i],'symmetric')
        for i in range(12):
            for j in range(12):check(T[i+1][j]+T[i][j+1]==2*T[i+1][j+1],'Stein entries')
        for n in range(7):
            for M in (max(1,n),max(1,n)+2):
                if M+n>13:continue
                part=sum((F(comb(n,j)*(-2)**j)*T[i][i+j] for i in range(M) for j in range(n+1)),F(0))
                full=G(0);tail=G(0)
                for z,m in Z:
                    lam=(B-I*z)/(B+I*z);t=z*z/(B*B+z*z);g=m/(B*B+z*z)
                    full+=g*lam**n;tail+=g*t**M*lam**n
                    # Exact algebra for the simultaneous damping estimate.
                    yy=abs(z.im);RR=z.norm2();dm=RR+B*B-2*B*yy;dp=RR+B*B+2*B*yy
                    check(dm>=z.re*z.re+1,'strip denominator')
                    check((t.norm2()**M)*(lam.norm2()**n)<= (RR/dm)**(2*M),'linear trace-tail damping')
                check(full-G(part)==tail,'exact partial trace tail')
        if ind==2:
            _,piv=ldl([row[:6] for row in T[:6]])
            check(all(x>0 for x in piv[:4]) and piv[4]<0 and piv[5]<0,'quartet inertia and first failure')
            controls.append({'first_negative_dimension':5,'six_pivots':[str(x) for x in piv]})
    actual=actual_safe_matrix()
    return {'schema':1,'status':'FINITE_IDENTITIES_AND_ACTUAL_4X4_ONLY','checks':COUNT,
            'actual_safe_point_certificate':actual,'synthetic_controls':controls,
            'source_sha256':{name:hashlib.sha256((Path(__file__).parent/name).read_bytes()).hexdigest() for name in ('BRIDGE.md','REVIEW.md','SOURCE_LOCK.json')},
            'all_section_positivity':'OPEN','RH':'UNPROVED'}

def strict_load(path):
    def pairs(xs):
        d={}
        for k,v in xs:
            if k in d:raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    def bad(x):raise ValueError('noninteger JSON numeric literal')
    data=json.loads(Path(path).read_text(),object_pairs_hook=pairs,parse_float=bad,parse_constant=bad)
    def validate(x):
        if type(x) is bool or x is None:raise ValueError('Boolean/null alias refused')
        if isinstance(x,dict):
            for v in x.values():validate(v)
        elif isinstance(x,list):
            for v in x:validate(v)
    validate(data)
    return data

def main():
    p=argparse.ArgumentParser();p.add_argument('--check',type=Path);p.add_argument('--write',type=Path);args=p.parse_args()
    result=run()
    if args.check and strict_load(args.check)!=result:raise ValueError('saved result differs from recomputation')
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:args.write.write_text(text)
    print(text,end='')

if __name__=='__main__':
    try:main()
    except Exception as e:
        print(type(e).__name__+': '+str(e),file=sys.stderr);sys.exit(1)
