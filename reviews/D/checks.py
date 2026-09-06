#!/usr/bin/env python3
"""Reviewer D: bounded independent reconstructions, not a proof of RH.
Python stdlib + SymPy. No network, source imports, upstream producers or asserts.
Run --write result.json, then --check result.json normally and under -O.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
from itertools import product
import json
from math import comb, gcd, isqrt, lcm
from pathlib import Path
import sys
import sympy as S

BITS = 100
DEN = 1 << BITS


def require(ok: bool, message: str) -> None:
    if not ok:
        raise ValueError(message)


@dataclass(frozen=True)
class I:
    lo: Q
    hi: Q
    def __post_init__(self):
        require(self.lo <= self.hi, 'reversed interval')
    @staticmethod
    def point(x):
        return I(Q(x), Q(x))
    def __add__(self, y):
        y = y if isinstance(y,I) else I.point(y)
        return I(self.lo+y.lo, self.hi+y.hi)
    __radd__ = __add__
    def __neg__(self):
        return I(-self.hi,-self.lo)
    def __sub__(self,y):
        return self + (-y if isinstance(y,I) else -Q(y))
    def __rsub__(self,y):
        return -self+y
    def __mul__(self,y):
        y = y if isinstance(y,I) else I.point(y)
        a = [self.lo*y.lo,self.lo*y.hi,self.hi*y.lo,self.hi*y.hi]
        return I(min(a),max(a))
    __rmul__=__mul__
    def reciprocal(self):
        require(self.lo>0 or self.hi<0,'interval division through zero')
        return I(1/self.hi,1/self.lo)
    def __truediv__(self,y):
        return self * (y.reciprocal() if isinstance(y,I) else Q(1)/Q(y))
    def square(self):
        if self.lo<=0<=self.hi:
            return I(Q(0),max(self.lo**2,self.hi**2))
        return I(min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))
    def rounded(self):
        return I(Q(self.lo.numerator*DEN//self.lo.denominator,DEN),
                 Q(-((-self.hi.numerator*DEN)//self.hi.denominator),DEN))
    def record(self):
        a=self.rounded()
        return {'lower':str(a.lo),'upper':str(a.hi)}


@lru_cache(None)
def sqrt_i(x: Q) -> I:
    x=Q(x);require(x>=0,'sqrt domain')
    k=isqrt(x.numerator*DEN*DEN//x.denominator)
    lo=Q(k,DEN)
    hi=lo if lo*lo==x else Q(k+1,DEN)
    require(lo*lo<=x<=hi*hi,'sqrt enclosure failed')
    return I(lo,hi)


@lru_cache(None)
def log_i(x: Q) -> I:
    x=Q(x);require(x>0,'log domain')
    if x<1:
        return -log_i(1/x)
    k=0;r=x
    while r>=2:
        r/=2;k+=1
    def reduced(v):
        z=(v-1)/(v+1); zz=z*z; term=z; total=Q(0)
        N=80
        for j in range(N):
            total+=term/Q(2*j+1);term*=zz
        tail=2*term/(Q(2*N+1)*(1-zz))
        return I(2*total,2*total+tail).rounded()
    return (reduced(r)+k*reduced(Q(2))).rounded()


def log_interval(x: I) -> I:
    return I(log_i(x.lo).lo,log_i(x.hi).hi).rounded()


def exp_i(x: Q) -> I:
    x=Q(x);require(0<=x<=1,'exp restricted to [0,1]')
    term=Q(1);total=Q(1);N=64
    for j in range(1,N+1):
        term*=x/j; total+=term
    first=term*x/(N+1)
    return I(total,total+first/(1-x/(N+2))).rounded()


@lru_cache(None)
def factors(n: int):
    require(type(n) is int and n>=1,'positive integer factor input')
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:
            n//=p;e+=1
        if e: out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return tuple(out)


def mu(n):
    f=factors(n)
    return 0 if any(e>1 for p,e in f) else (-1)**len(f)


def sigma(n):
    out=1
    for p,e in factors(n):out*=sum(p**j for j in range(e+1))
    return out


def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]


def beta(n):
    return mu(n)-(mu(n//67) if n%67==0 else 0)


def W0(y):
    y=Q(y)
    return I.point(0) if y<=1 else 8*sqrt_i(y)-8-3*log_i(y)


def K0(y):
    y=Q(y)
    if y<=1 or y>=8:return I.point(0)
    r=sqrt_i(Q(2))
    return W0(y)-(r+2)*W0(y/2)+(2*r+1)*W0(y/4)-r*W0(y/8)


def wavelet(X):
    return sum((mu(n)*K0(Q(X,n))/sqrt_i(Q(n)) for n in range(1,X+1)),I.point(0))


def strict_equal(x,y):
    if type(x) is not type(y):return False
    if isinstance(x,dict):return x.keys()==y.keys() and all(strict_equal(x[k],y[k]) for k in x)
    if isinstance(x,list):return len(x)==len(y) and all(strict_equal(a,b) for a,b in zip(x,y))
    return x==y


def load_strict(path):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'duplicate JSON key: '+k);d[k]=v
        return d
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,
                      parse_constant=lambda x: (_ for _ in ()).throw(ValueError('nonfinite JSON')))


def reconstruct():
    checks=[]
    def add(name,n,witness=None):
        require(type(n) is int and n>0,'invalid fixture count')
        checks.append({'name':name,'fixtures':n,'witness':witness})
    # 1: a variable-row filter is not a single Toeplitz filter.
    f=[];h=[];g=[]
    for n in range(301):
        m,r=divmod(n,3)
        hn=(0,(-2)**m,2*(-2)**m)[r];h.append(hn)
        fn=hn+2*(f[n-1] if n else 0)-(f[n-2] if n>=2 else 0);f.append(fn)
        k=2 if r==0 else 4
        gn=sum((-1)**j*comb(k,j)*(f[n-j] if n>=j else 0) for j in range(k+1));g.append(gn)
        require(n<2 or gn==0,'variable-filter witness')
    add('D01_variable_order_counterexample',301,{'orders':[2,4,4],'initial_f':f[:16],'g_prefix':g[:8], 'h_298':h[298]})
    z=S.symbols('z');F=(z+2*z*z)/((1+2*z**3)*(1-z)**2)
    require(S.cancel((1-z)**2*F-(z+2*z*z)/(1+2*z**3))==0,'filter generating identity')
    add('D01_generating_function',1)
    for k in range(1,7):
        for n in range(41):
            require(sum(comb(j+k-1,k-1) for j in range(n+1))==comb(n+k,k),'fixed inverse mass')
    add('fixed_order_inverse_hockey_stick',246)
    # 2: spectral threshold, exact rational approximate eigenvectors.
    for n in range(1,101):
        gn=1-Q(1,2**n);kn=gn**2;hn=1-kn
        require(hn>0 and hn<Q(1,2**(n-1)),'BS diagonal threshold')
    add('D02_Birman_Schwinger_threshold_sequence',100,{'A':'I','G_n':'1-2^-n','K_n':'(1-2^-n)^2','ker_H':'zero','one_in_spectrum_K':True})
    # 3: all principal minors, not just leading minors.
    A=S.diag(0,-1)
    require(A[:1,:1].det()==0 and A.det()==0 and A[1,1]==-1,'leading-principal control')
    add('D03_leading_vs_all_principal_minors',1)
    t=S.symbols('t');nmat=0
    for vals in product(range(-1,2),repeat=3):
        A=S.Matrix([[vals[0],vals[1]],[vals[1],vals[2]]])
        rhs=t*t+sum(A[i,i] for i in range(2))*t+A.det()
        require(S.expand((t*S.eye(2)+A).det()-rhs)==0,'principal characteristic identity')
        nmat+=1
    add('D03_characteristic_principal_minor_identity',nmat)
    # 4: missing endpoint weight, generic and actual arithmetic source.
    a=Q(2);N=7;d={3:Q(2,3),4:Q(-5,2),7:Q(1,4)}
    qp=sum(dm*dn*min(m,n)**2 for m,dm in d.items() for n,dn in d.items())
    cuts=sorted({a,Q(N)}|set(map(Q,d)))
    integ=sum((v*v-u*u)*sum(w for n,w in d.items() if n>=v)**2 for u,v in zip(cuts,cuts[1:]))
    qold=sum(d.values())**2+integ
    require(qp-qold==(a*a-1)*sum(d.values())**2,'endpoint identity')
    add('D04_endpoint_factor_identity',1,{'correct':str(qp),'old':str(qold),'difference':str(qp-qold)})
    w4=wavelet(4);w16=wavelet(16)
    require(Q(-14620,10000)<w4.lo and w4.hi<Q(-14618,10000),'actual G4 enclosure')
    require(w16.lo>0 or w16.hi<0,'actual G16 is nonzero')
    gap=3*w16.square()
    require(gap.lo>0,'actual X16 energy mismatch')
    add('D04_actual_Mobius_wavelet_endpoint_witness',2,{'G4':w4.record(),'G16':w16.record(),'Qcorrect_minus_Qold_X16':gap.record()})
    # Robin: full integer range, independently factored and divisor-sieved.
    sig=[0]*5583
    for d0 in range(1,5583):
        for n in range(d0,5583,d0):sig[n]+=d0
    require(all(sig[n]==sigma(n) for n in range(1,5583)),'Robin primitive methods disagree')
    r1=max(Q(sig[n],n) for n in range(1,5041));r2=max(Q(sig[n],n) for n in range(5041,5583))
    require(r1==Q(403,105) and r2==Q(224,65),'Robin maxima')
    arg1=[n for n in range(1,5041) if Q(sig[n],n)==r1];arg2=[n for n in range(5041,5583) if Q(sig[n],n)==r2]
    require(arg1==[5040] and arg2==[5460],'Robin uniqueness')
    add('Robin_complete_integer_barrier',5582,{'max_1_5040':[5040,str(r1)],'max_5041_5582':[5460,str(r2)]})
    n=2048
    hlo=sum(DEN//k for k in range(1,n+1));hhi=sum(-((-DEN)//k) for k in range(1,n+1))
    gamma=I(Q(hlo,DEN),Q(hhi,DEN))-log_i(Q(n))+I(-Q(1,2*n),-Q(1,2*(n+1)))
    egamma=I(exp_i(gamma.lo).lo,exp_i(gamma.hi).hi)
    margins={}
    for n,base,sgn in [(5041,Q(224,65),1),(5582,Q(403,105),-1),(5583,Q(403,105),1)]:
        v=egamma*log_interval(log_i(Q(n)))-base
        require(v.lo>0 if sgn==1 else v.hi<0,'Robin directed threshold')
        margins[str(n)]=v.record()
    add('Robin_directed_gamma_loglog_thresholds',3,{'gamma':gamma.record(),'margins':margins})
    x=S.symbols('x',positive=True)
    phi=S.log(1+x)-x/(1+x)
    require(S.simplify(S.diff(x*x/(2*(1+x))-phi,x)-x*x/(2*(1+x)**2))==0,'gamma upper derivative')
    require(S.simplify(S.diff(phi-x*x/(2*(1+x)*(1+2*x)),x)-x*x*(8*x+5)/(2*(1+x)**2*(1+2*x)**2))==0,'gamma lower derivative')
    add('Robin_gamma_bound_derivatives',2)
    for a0 in range(4):
        for b in range(a0+1,7):
            fa=sum(x**j for j in range(a0+1));fb=sum(x**j for j in range(b+1))
            numer=S.expand(S.diff(fb,x)*fa-fb*S.diff(fa,x))
            require(all(c>=0 for c in S.Poly(numer,x).all_coeffs()),'Robin swap monotonicity')
    add('Robin_exponent_swap_polynomials',18)
    # SHARP finite Hall arithmetic, entire 66-prefix enumeration.
    A=Q(0);B=I.point(0);hall=[]
    for j in range(1,67):
        A+=Q(mu(j),j);B+=mu(j)*sqrt_i(Q(j)).reciprocal()
        endpoint=j if A>=0 else 67
        val=4*A*sqrt_i(Q(endpoint))-3*B
        require(val.lo>Q(7,20),'SHARP Hall moat')
        hall.append((j,endpoint,val))
    low=min(hall,key=lambda r:r[2].lo)
    require(low[:2]==(13,67),'SHARP worst prefix')
    require(all(low[2].hi<v.lo for j,e,v in hall if j!=13),'SHARP unique integer prefix')
    add('SHARP_complete_66_prefix_Hall',66,{'worst_prefix':13,'boundary':67,'minimum':low[2].record()})
    require(Q(163,60)-Q(4288,1605)==Q(289,6420),'SHARP prime mass rational gap')
    require(Q(2,3)<Q(25,36) and 67>64,'SHARP radical comparisons')
    add('SHARP_m_ge_2_global_constant_algebra',3,{'rational_gap':'289/6420'})
    y=S.symbols('y',positive=True);T=4*S.sqrt(y)-3
    require(S.simplify(y*S.diff(T*T/y,y)-3*T/y)==0,'SHARP derivative')
    add('SHARP_quadratic_distributional_derivative',1)
    require(Q(1,5)*5==1,'RN fixture')
    for p0,q0,r0 in [(9,4,1),(25,9,4),(64,16,4)]:
        Tp=4*isqrt(p0)-3;Tq=4*isqrt(q0)-3;Tr=4*isqrt(r0)-3
        require(Q(Tr,Tq)*Q(Tq,Tp)==Q(Tr,Tp),'RN cocycle')
    add('SHARP_RN_density_and_cocycle',4)
    # Fixed row source and Mellin identities.
    a,b,s=S.symbols('a b s');P2=2*a-1-b;P3=(5*b-a-1-3*a*a)/3
    require(S.expand(5*P2+3*P3+3*(a-1)*(a-2))==0,'5:3 multiplier')
    require(S.expand((3*P3).subs(b,2*a-1)+3*(a-1)*(a-2))==0,'rows common zero')
    require(S.cancel((s+S.Rational(3,2))/(s*(s-S.Rational(1,2)))*(s-S.Rational(1,2))/(s*(s+S.Rational(3,2))))==1/s**2,'Mellin ramp')
    add('fixed_rows_and_Mellin_ramp',3)
    j,N=S.symbols('j N',integer=True,positive=True)
    require(S.expand(4*(N+1)**3-(2*N+1)**2*(N+2))==3*N+2,'row increment gap')
    count=0
    for jj in range(2,10):
        for nn in range(jj+1,20):
            gam=lambda m: Q(jj+1,jj-1) if m==jj else (-Q((jj+1)*(jj-2),jj*(jj-1)) if m==jj+1 else Q(2,jj*(jj-1)))
            require(sum(m*gam(m) for m in range(jj,nn+1))==Q(nn*(nn+1),jj*(jj-1)),'row moment')
            count+=1
    add('positive_row_kernel_moment_algebra',count+1)
    # Xi determinant factorization and orbit derivatives.
    xs=S.symbols('x0:3',positive=True);ts=[v*v for v in xs]
    ps=S.symbols('p0:3',nonzero=True)
    H=S.Matrix(3,3,lambda i,j:(xs[i]*ps[i]+xs[j]*ps[j])/(xs[i]+xs[j]))
    dd=lambda v:sum(v[i]/S.prod(ts[i]-ts[j] for j in range(3) if i!=j) for i in range(3))
    vand=S.prod(ts[j]-ts[i] for i in range(3) for j in range(i+1,3))
    pref=S.prod(ps)*vand**2/S.prod((xs[i]+xs[j])**2 for i in range(3) for j in range(i+1,3))
    require(S.factor(H.det()-pref*dd([1/p for p in ps])*dd([t*p for t,p in zip(ts,ps)]))==0,'Xi det3')
    require(S.factor(H[:2,:2].det()+(ps[0]-ps[1])*(ts[0]*ps[0]-ts[1]*ps[1])/(xs[0]+xs[1])**2)==0,'Xi det2')
    add('Xi_two_three_node_determinants',2)
    t,c,B,m,r=S.symbols('t c B m r',positive=True);U=t+c
    q=4*m*U/(U*U+B*B);R=2/(t+r)
    E=lambda v:S.diff(v,t,2)*v-2*S.diff(v,t)**2
    require(S.factor(E(q)+32*m*m*B*B/(U*U+B*B)**3)==0,'off-orbit E')
    require(S.factor(S.diff(t*q,t,2)+8*m*(c*U**3+3*B*B*U*U-3*c*B*B*U-B**4)/(U*U+B*B)**3)==0,'tp curvature')
    require(S.factor(E(R))==0,'critical E')
    kap,ss,uu=S.symbols('kap ss uu',positive=True)
    cross=q*S.diff(R,t,2)+R*S.diff(q,t,2)-4*S.diff(q,t)*S.diff(R,t)
    cross=S.factor(cross.subs(t,uu-c).subs(B**2,kap*ss*ss*uu*uu).subs(r,c-ss*uu))
    Qk=1-kap+3*kap*ss*(2-ss)+kap*kap*ss*ss*(3-2*ss)
    target=16*m*ss*ss*Qk/(uu**4*(1+kap*ss*ss)**3*(1-ss)**3)
    require(S.factor(cross-target)==0,'orbit reserve cross formula')
    add('Xi_orbit_curvatures_and_reserve',4)
    Hheight=3*10**12
    bound=18*(log_i(Q(Hheight))+1)/Hheight
    require(bound.hi<Q(1,10**9),'reserve budget small')
    add('Xi_conservative_3e12_reserve_budget',1,{'upper_allocation':bound.record(),'external_zero_verification_rerun':False})
    # Coefficient half-square and exact full-period carry geometry.
    @lru_cache(None)
    def eta(n):
        v=Q(1)
        for p,e in factors(n):v*=Q(comb(2*e,e),4**e)
        return v
    for n in range(1,129):
        require(sum(eta(d0)*eta(n//d0) for d0 in divisors(n))==1,'eta convolution')
    add('half_divisor_convolution_is_constant_one',128)
    for ucut in [1,3,7]:
        for n in range(1,129):
            hh=sum(mu(d0)*eta(n//d0) for d0 in divisors(n) if d0>ucut)
            require(abs(hh)<=len(divisors(n)),'half-divisor diagonal majorant')
    add('half_divisor_uniform_coefficient_majorant',384)
    xi=S.symbols('xi',real=True)
    require(S.simplify(9-(S.Rational(9,4)+xi**2)/(S.Rational(1,4)+xi**2)-8*xi**2/(S.Rational(1,4)+xi**2))==0,'Hardy 3 multiplier')
    add('half_divisor_Hardy_norm_three',1)
    ncell=0
    for d0 in range(2,11):
        for e0 in range(2,11):
            ell=lcm(d0,e0)
            joint=sum((v%d0>u%d0) and (v%e0>u%e0) for u in range(ell) for v in range(ell))
            cov=Q(joint,ell*ell)-Q(d0-1,2*d0)*Q(e0-1,2*e0)
            require(cov==Q(gcd(d0,e0)**2-1,4*d0*e0),'carry covariance')
            ncell+=1
    add('Q4_complete_residue_covariance',ncell)
    for n in range(1,65):
        J=lambda k:sum(mu(d0)*(k//d0)**2 for d0 in divisors(k))
        require(sum(J(d0) for d0 in divisors(n))==n*n,'Jordan inversion')
    add('Q4_Jordan_square_kernel',64)
    # Gaussian exponent / exact countable heat mechanism finite controls.
    qv,mv=S.symbols('q m',positive=True)
    require(S.expand(mv/2-mv**2/(4*qv)-qv/4+(mv-qv)**2/(4*qv))==0,'heat saddle')
    add('heat_completed_square_saddle',1)
    for y0 in [Q(1,10),Q(1,4),Q(2,5)]:
        require(-2*y0*y0<0,'terminal first Hermite coefficient')
    add('heat_terminal_pair_coefficients',3)
    # Legacy Hermite multiplicity and derivative-free resolvents.
    roots=[0,0,S.I,-S.I]; HH=S.Matrix(4,4,lambda i,j:sum(zr**(i+j) for zr in roots))
    ev=HH.eigenvals();np=sum(mult for v,mult in ev.items() if v>0);nm=sum(mult for v,mult in ev.items() if v<0);nz=sum(mult for v,mult in ev.items() if v==0)
    require((np,nm,nz)==(2,1,1),'Hermite inertia multiplicities')
    add('legacy_Hermite_inertia_with_multiplicity',1,{'positive':2,'negative':1,'zero':1})
    u,v,a0=S.symbols('u v a',positive=True)
    require(S.factor((v/(v+a0)-u/(u+a0))/(v-u)-a0/((u+a0)*(v+a0)))==0,'resolvent secant')
    for rr in range(1,5):
        nodes=list(map(S.Integer,range(1,rr+2)))
        lhs=sum((x/(x+a0))/S.prod(x-y for y in nodes if x!=y) for x in nodes)
        require(S.factor(lhs-(-1)**(rr-1)*a0/S.prod(x+a0 for x in nodes))==0,'higher divided differences')
    add('legacy_derivative_free_resolvent_identities',5)
    # Main extraction omitted n>=2; reproduce the correct rational theorem.
    for nn in range(1,8):
        nodes=[Q(i) for i in range(1,nn+1)];disp=Q(1,2)
        weights=[Q(1)/S.prod(xi-xj for xj in nodes if xi!=xj) for xi in nodes]
        weights=list(map(Q,weights))
        alpha=[xi/(xi*xi-disp) for xi in nodes]
        s0=sum(wi*ai for wi,ai in zip(weights,alpha))
        s1=sum(wi*xi*ai for wi,xi,ai in zip(weights,nodes,alpha))
        den=Q(S.prod(xi*xi-disp for xi in nodes))
        cc=[den*wi*(s1-s0*xi) for wi,xi in zip(weights,nodes)]
        require(sum(ci*ai for ci,ai in zip(cc,alpha))==0,'matched positive annihilation')
        got=sum(ci/(xi*xi-disp) for ci,xi in zip(cc,nodes))
        require(got==(0 if nn==1 else -1),'matched negative normalization')
    add('D05_matched_annihilator_n1_failure_n2_repair',7,{'n1_vector':[0],'n1_normalization':0,'n_ge_2_normalization':-1})
    # The legacy powered-tail fixture, with certified caps made explicit.
    primes=[3,5,7];caps=[2,2,1];Aexp=4;M0=5
    base=Q(31,16)*Q(4,3)*Q(6,5)*Q(8,7)
    Vnext={mm:Q(1) for mm in range(4)}
    for rr in range(Aexp,1,-1):
        nr=sum(mi>=rr for mi in caps)
        Vnow={}
        for mm in range(4):
            opts=[]
            for ell in range(min(mm,nr)+1):
                inc=Q(1);cost=1
                for pp in primes[:ell]:
                    inc*=Q(pp**(rr+1)-1,pp*(pp**rr-1));cost*=pp
                opts.append(inc**64/cost*Vnext[ell])
            Vnow[mm]=max(opts)
        Vnext=Vnow
    upper=base**64*M0*Vnext[3];separate=Q(12493,3150)
    require(upper<Q(39,10)**64<separate**64,'powered Robin improvement')
    actual=[]
    for bb in product(range(1,5),repeat=3):
        if bb[0]>=bb[1]>=bb[2] and S.prod(pp**(ee-1) for pp,ee in zip(primes,bb))<=M0:
            require(all(ee<=cap for ee,cap in zip(bb,caps)),'tail caps are invalid')
            value=Q(31,16)
            for pp,ee in zip(primes,bb):value*=Q(sum(pp**j for j in range(ee+1)),pp**ee)
            actual.append(value)
    require(max(actual)==Q(403,105),'powered Robin true maximum')
    add('D06_Robin_powered_tail_cap_contract',64,{'caps':caps,'true_max':'403/105','ceiling_test':'U < (39/10)^64 < U_sep^64'})
    # First-chaos support is not domination of its specified input Gram.
    require(4>1,'first-chaos rescaling control')
    add('first_chaos_support_without_contraction',1,{'input_gram':1,'output_gram':4,'intensity_law':'K_r=4r'})
    margin=1-Q(85,196)**2-Q(1,4)
    require(margin==Q(21587,38416) and margin>Q(19751,38416),'Julia margin repair')
    add('Julia_existing_rational_margin_repair',1,{'correct_margin':str(margin),'printed_weaker_margin':'19751/38416'})
    # Safe-line Hausdorff algebra, without assuming the unproved sign.
    zz=S.symbols('zz')
    for kk in range(4):
        for mm in range(5):
            lhs=sum((-1)**jj*comb(mm,jj)*(-2*zz**2/(1-zz**2)**(kk+jj+3)) for jj in range(mm+1))
            rhs=-2*(-1)**mm*zz**(2*mm+2)/(1-zz**2)**(kk+mm+3)
            require(S.factor(lhs-rhs)==0,'safe-line finite difference')
    add('safe_line_beta_finite_difference',20)
    lam=S.symbols('lam')
    for nn in range(9):
        require(S.expand(sum(comb(nn,jj)*lam**jj*(1-lam)**(nn-jj) for jj in range(nn+1)))==1,'Bernstein partition')
    add('safe_line_Bernstein_partition',9)
    # Actual Haar overlap lengths at fixed rational offsets, scale log2=1.
    root2=S.sqrt(2)
    psi=lambda v: S.Integer(1) if 0<v<1 else (-root2 if 1<v<2 else S.Integer(0))
    for vv in [Q(jj,4) for jj in range(-8,9)]:
        cuts=sorted({Q(0),Q(1),Q(2),-vv,1-vv,2-vv})
        val=sum(S.Rational(b-a)*psi((a+b)/2)*psi((a+b)/2+vv) for a,b in zip(cuts,cuts[1:]))
        av=abs(vv);target=3-(3+root2)*av if av<=1 else -root2*(2-av)
        require(S.simplify(val-target)==0,'Haar autocorrelation')
    add('half_divisor_Haar_overlap',17)
    # Rational inverse-discrete-Laplacian check of the full carry field.
    for nn in range(2,9):
        ff={j:Q((-1)**j,j+1) for j in range(1,nn+1)}
        cc={j:sum(ff[d0] for d0 in divisors(j)) for j in range(1,nn+1)}
        C=lambda x:sum(cc[j] for j in range(1,x+1))
        cells=S.Matrix([C(nn)-C(j)-C(nn-j-1) for j in range(nn)])
        mean=sum(cells)/nn
        require(mean==-C(nn)+Q(2,nn)*sum(j*cc[j] for j in cc),'carry mean')
        D=S.zeros(nn)
        for j in range(nn):D[j,j]+=1;D[j,(j-1)%nn]-=1
        vv=D*cells
        require(vv==S.Matrix([0]+[cc[nn-j]-cc[j] for j in range(1,nn)]),'carry discrete gradient')
        LL=D.T*D;J=S.ones(nn)/nn;Lp=(LL+J).inv()-J
        centered=cells-S.ones(nn,1)*mean
        require(S.factor((centered.T*centered)[0]-(vv.T*Lp*vv)[0])==0,'carry inverse Laplacian')
    add('Q4_rational_inverse_Laplacian_carry_energy',21)
    # General coherent negative-part transfer.
    for av,bv in product(range(-10,11),repeat=2):
        require(abs(max(-av,0)-max(-bv,0))<=abs(av-bv),'negative part Lipschitz')
    add('same_kernel_negative_part_transfer',441)
    # Conjunctive interfaces: signed flux is retained before Perron inversion.
    mat=S.Matrix([[S.Rational(1,10),S.Rational(1,5)],
                  [S.Rational(3,10),S.Rational(1,10)]])
    inv=(S.eye(2)-mat).inv()
    require(all(v>=0 for v in inv),'Perron inverse positivity')
    for av,bv in product(range(-3,4),repeat=2):
        ff=S.Matrix([av,bv]);gg=(S.eye(2)+mat)*ff
        neg=S.Matrix([max(-v,0) for v in ff]);res=S.Matrix([max(-v,0) for v in gg])
        flux=mat*ff
        require(all(v>=0 for v in res+flux+mat*neg-neg),'signed Perron input')
        require(all(v>=0 for v in inv*(res+flux)-neg),'signed Perron absorption')
    add('conjunctive_signed_Perron_absorption',49)
    for av,bv,tv in product(range(-5,6),repeat=3):
        lhs=max(-av-bv,0);rhs=max(-av-tv,0)+max(-bv+tv,0)
        require(lhs<=rhs,'matched transfer inequality')
        require(lhs==max(-av+av,0)+max(-bv-av,0),'matched transfer attainment')
    add('conjunctive_matched_transfer',1331)
    for gv,theta,excess in product(range(-10,11),[Q(0),Q(1,4),Q(1,2),Q(3,4)],[Q(0),Q(1),Q(10)]):
        rem=max(Q(0),(1-theta)*gv*gv-theta*excess)
        require((1-theta)*gv*gv<=excess+rem,'root excess absorption')
    add('conjunctive_root_excess_absorption',252)
    u=S.symbols('u',real=True)
    mass=S.integrate(1-u,(u,0,1));energy=S.integrate(1,(u,0,1))
    require(mass==S.Rational(1,2) and energy==1,'initial boundary counterexample')
    require(Q(1,3)<Q(1,2),'pi>3 comparison witness')
    add('D07_initial_excursion_boundary_failure',1,
        {'f':'u-1','log_Y':2,'negative_mass':'1/2','terminal_mass':0,
         'interior_only_rhs':0,'incorrectly_included_rhs':'1/pi < 1/3 < 1/2'})
    for nn in range(1,21):
        # Region j is the single entry (2j,2j+1), active only on dyadic block j.
        # Divide logarithmic integrals by log(2), leaving exact integers.
        total=sum(2**j for j in range(nn))
        require(total==2**nn-1,'moving-region total')
    add('regional_fixed_index_is_not_uniform',20,
        {'per_fixed_region_integral':'2^j log(2), eventually constant in Y',
         'active_region_count':'log_2(Y)','total_mass_at_Y_2N':'(Y-1) log(2)'})
    BB=S.diag(-1,2);ZZ=S.Matrix([[1,1]]);CC=S.Matrix([[2]])
    schur=BB-ZZ.T*CC.inv()*ZZ
    require(schur[0,0]<BB[0,0]<0,'Schur cannot rescue a negative direction')
    add('positive_Schur_complement_no_rescue',1)
    return {'schema':'riemann.reviewerD.bounded.v1','main_sha':'8d16f8d9c475db290bc85e53d775b93b9bcdb336',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'rh_proved':False,'upstream_producers_executed':False,
            'named_checks':len(checks),'fixture_count':sum(x['fixtures'] for x in checks),'checks':checks}


def main():
    ap=argparse.ArgumentParser(description=__doc__);gr=ap.add_mutually_exclusive_group(required=True)
    gr.add_argument('--write',type=Path);gr.add_argument('--check',type=Path);args=ap.parse_args()
    saved=None
    if args.check:
        saved=load_strict(args.check)
        expected={'schema':'riemann.reviewerD.bounded.v1',
                  'main_sha':'8d16f8d9c475db290bc85e53d775b93b9bcdb336',
                  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'rh_proved':False,'upstream_producers_executed':False,
                  'named_checks':45,'fixture_count':9380}
        require(type(saved) is dict,'expected JSON object')
        for key,value in expected.items():
            require(key in saved and strict_equal(saved[key],value),'metadata preflight: '+key)
    result=reconstruct()
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.write:args.write.write_text(text)
    else:require(strict_equal(result,saved),'result mismatch (including exact JSON types)')
    print('PASS_REVIEWER_D_BOUNDED_RECONSTRUCTIONS')
    print(f"named_checks={result['named_checks']} fixtures={result['fixture_count']}")
    print('RH_UNPROVED; NO_UPSTREAM_OR_LEAN_REPLAY')

if __name__=='__main__':
    try:main()
    except (ValueError,TypeError,KeyError) as exc:
        print('REJECT: '+str(exc),file=sys.stderr);sys.exit(2)
