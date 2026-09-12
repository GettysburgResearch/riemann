#!/usr/bin/env python3
"""Exact interval controls for a connected infinite Ising-chain proposal.
Theta integration/dyadics adapted from ICR26 (#863), not an independent backend.
All chain, transfer, and matching controls are reconstructed in this file.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
BITS=192
SCALE=1<<BITS
DEGREE=80
ROOT=Path(__file__).resolve().parent
def require(ok, message):
    if not ok:
        raise ValueError(message)


def ceildiv(a,b):
    require(b>0, 'positive divisor required')
    return -((-a)//b)


class I:
    __slots__=('lo','hi')
    def __init__(self, lo, hi=None):
        self.lo=int(lo); self.hi=int(lo if hi is None else hi)
        require(self.lo<=self.hi,'reversed interval')
    @staticmethod
    def rat(p,q=1):
        require(q>0,'positive rational denominator required')
        return I((p*SCALE)//q,ceildiv(p*SCALE,q))
    @staticmethod
    def coerce(x):
        if isinstance(x,I): return x
        if type(x) is int: return I(x*SCALE)
        if isinstance(x,F): return I.rat(x.numerator,x.denominator)
        raise TypeError('only exact numbers accepted')
    def __add__(self,x):
        x=I.coerce(x); return I(self.lo+x.lo,self.hi+x.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,x): return self+(-I.coerce(x))
    def __rsub__(self,x): return I.coerce(x)+(-self)
    def __mul__(self,x):
        x=I.coerce(x)
        p=(self.lo*x.lo,self.lo*x.hi,self.hi*x.lo,self.hi*x.hi)
        return I(min(p)//SCALE,ceildiv(max(p),SCALE))
    __rmul__=__mul__
    def __truediv__(self,x):
        if type(x) is int:
            if x<0:return (-self)/(-x)
            require(x>0,'zero divisor');return I(self.lo//x,ceildiv(self.hi,x))
        x=I.coerce(x)
        require(x.lo>0 or x.hi<0,'division through zero')
        if x.hi<0:return (-self)/(-x)
        return self*I((SCALE*SCALE)//x.hi,ceildiv(SCALE*SCALE,x.lo))
    def __rtruediv__(self,x): return I.coerce(x)/self
    def __pow__(self,k):
        require(type(k) is int and k>=0,'nonnegative integer power required')
        out=I.coerce(1); base=self
        while k:
            if k&1: out=out*base
            k//=2
            if k:base=base*base
        return out
    def sqrt(self):
        require(self.lo>=0,'negative square root')
        lo=isqrt(self.lo*SCALE); h=self.hi*SCALE; hi=isqrt(h)
        return I(lo,hi if hi*hi==h else hi+1)
    def record(self): return [self.lo,self.hi]


def exp_endpoint(x):
    """Enclose exp(x/SCALE) for an integer x."""
    if x<0:return 1/exp_endpoint(-x)
    k=0
    while x> (SCALE//8)*(1<<k):k+=1
    y=I.rat(x,SCALE*(1<<k))
    term=I.coerce(1); total=term
    for j in range(1,97):
        term=term*y/j;total=total+term
    nxt=term*y/97
    rem=nxt/(1-y/98)
    total=I(total.lo,total.hi+rem.hi)
    for _ in range(k):total=total*total
    return total


def exp(x):
    x=I.coerce(x)
    return I(exp_endpoint(x.lo).lo,exp_endpoint(x.hi).hi)


def atan_recip(n):
    # Alternating series: 96 terms, first omitted term bounds remainder.
    total=F(0)
    for k in range(96):total+=F((-1)**k,(2*k+1)*n**(2*k+1))
    rem=F(1,193*n**193)
    return I.rat(total.numerator,total.denominator)+I(0,I.rat(rem.numerator,rem.denominator).hi)


def pi_interval():return 16*atan_recip(5)-4*atan_recip(239)


def series_exp_linear(a,center,h):
    out=[exp(a*center)]; v=a*h
    for k in range(1,DEGREE+1):out.append(out[-1]*v/k)
    return out


def mulpoly(a,b,limit=None):
    last=len(a)+len(b)-2
    if limit is not None:last=min(last,limit)
    c=[I.coerce(0) for _ in range(last+1)]
    for i,u in enumerate(a):
        for j in range(min(len(b),last-i+1)):
            c[i+j]=c[i+j]+u*b[j]
    return c


def cell_density(n,center,pi):
    h=I.rat(1,32); c=I.coerce(center);q=pi*n*n
    e2=series_exp_linear(I.coerce(2),c,h)
    g=[-q*v for v in e2]
    hh=[exp(g[0])]
    for j in range(1,DEGREE+1):
        hh.append(sum((k*g[k]*hh[j-k] for k in range(1,j+1)),I.coerce(0))/j)
    e9=series_exp_linear(I.rat(9,2),c,h)
    e5=series_exp_linear(I.rat(5,2),c,h)
    pref=[4*q*q*x-6*q*y for x,y in zip(e9,e5)]
    return mulpoly(pref,hh,DEGREE)


def integrate_moment(poly,center,j):
    h=I.rat(1,32); c=I.coerce(center)
    power=[comb(j,k)*(c**(j-k))*(h**k) for k in range(j+1)]
    out=mulpoly(poly,power)
    # Full-line moment: factor two times half-line cell integral.
    return 4*h*sum((out[k]/(k+1) for k in range(0,len(out),2)),I.coerce(0))


def theta_moments():
    pi=pi_interval()
    require(pi.lo>3*SCALE and pi.hi<4*SCALE,'pi')
    js=tuple(range(0,7,2));counts=(32,24,16,12)
    totals={j:I.coerce(0) for j in js}
    for n,cnt in enumerate(counts,1):
        for k in range(cnt):
            center=F(2*k+1,32)
            d=cell_density(n,center,pi)
            for j in js:totals[j]+=integrate_moment(d,center,j)
    errs={}
    for j in js:
        # Cauchy circle radius1/8, half-cell1/32. Full source, not just a truncation.
        e=I.rat(16*10**11*2**j,4**(DEGREE+1))/F(3,4)
        tails=I.coerce(0)
        for n,cnt in enumerate(counts,1):
            U=F(cnt,16);q=pi*n*n;E=exp(2*I.coerce(U));lam=2*q*E-F(9,2)
            tails+=8*q*q*exp(F(9,2)*I.coerce(U)-q*E)*sum(
                (comb(j,k)*U**(j-k)*factorial(k)/lam**(k+1) for k in range(j+1)),I.coerce(0))
        omitted=16*pi*pi*625*exp(-25*pi)*factorial(j)/(50*pi-F(9,2))**(j+1)
        totals[j]=I(totals[j].lo-e.hi, totals[j].hi+e.hi+tails.hi+omitted.hi)
        errs[str(j)]={'taylor':e.record(),'time':tails.record(),'index':omitted.record()}
    require(totals[0].lo>0,'normalization')
    mu={j:totals[j]/totals[0] for j in js[1:]}
    return totals,mu,errs


def log2_init():
    z=I.rat(1,3);t=z;out=I.coerce(0)
    for k in range(100):out+=t/(2*k+1);t=t*z*z
    return 2*out+I(0,(2*t/201/(1-z*z)).hi)
LN2=log2_init()

def log_endpoint(n):
    require(n>0,'positive logarithm')
    e=n.bit_length()-1-BITS
    m=I.rat(n,SCALE*(1<<e)) if e>=0 else I.rat(n*(1<<(-e)),SCALE)
    z=(m-1)/(m+1);t=z;out=I.coerce(0)
    for k in range(72):out+=t/(2*k+1);t=t*z*z
    return 2*out+I(0,(2*t/145/(1-z*z)).hi)+e*LN2

def log(x):
    x=I.coerce(x);return I(log_endpoint(x.lo).lo,log_endpoint(x.hi).hi)

def fixed_constants():
    r=I.rat(2,3)
    def magnet(u):
        eu=exp(u);sh=(eu-1/eu)/2
        return sh/(sh*sh+r*r).sqrt()
    def f0(u):return 1/r if u.lo==0 and u.hi==0 else magnet(u)/u
    def f1(u):return (magnet(u)-1)/u
    def simpson(f,a,b,n):
        require(n%2==0,'even Simpson count')
        h=(b-a)/n;out=f(I.coerce(a))+f(I.coerce(b))
        for j in range(1,n):out+=(4 if j%2 else 2)*f(I.coerce(a)+j*h)
        return h*out/3
    # PROOF: Cauchy radius 1/4, |f|<4, |f^(4)|<24576.
    n0=512;n1=4096
    i0=simpson(f0,F(0),F(1),n0);i1=simpson(f1,F(1),F(8),n1)
    err0=I.rat(24576,180*n0**4);err1=I.rat(24576*7**5,180*n1**4)
    et=exp(-16)/16
    C=-1+i0+i1+I(-err0.hi-err1.hi-et.hi,err0.hi+err1.hi)
    ell=log(I.rat(3,5));d=I.rat(7,8)/ell;pi=pi_interval()
    M=8192
    harm=sum((I.rat(1,n) for n in range(1,M+1)),I.coerce(0))
    ge=I.rat(1,6*(M-1)**2)
    gamma=harm-log(M)-I.rat(1,2*M)+I(-ge.hi,ge.hi)
    N=256
    ss=sum((log(n)/(n*n) for n in range(32,N)),I.coerce(0))
    ln=log(N);ff=ln/(N*N);fp=(1-2*ln)/(N**3);fppp=(26-24*ln)/(N**5)
    rem=(-fppp)/720
    S=ss+(ln+1)/N+ff/2-fp/12+fppp/720+I(-rem.hi,rem.hi)
    H31=sum((I.rat(1,n) for n in range(1,32)),I.coerce(0))
    B0=(-LN2+C+gamma)/2;Btheta=-(1+log(2*pi))/2
    A=Btheta-B0+H31/2-d*S
    require(A.lo>I.rat(80716,100000).hi and A.hi<I.rat(80717,100000).lo,'head-sum bracket')
    require(d.lo>I.rat(-171292,100000).hi and d.hi<I.rat(-171291,100000).lo,'log-weight correction')
    require((exp(I.rat(13,10))+exp(I.rat(-13,10))).hi<4*SCALE,'Cauchy cosh bound')
    return {'d':d,'A':A,'C':C,'ell':ell,'gamma':gamma,'S':S,
            'quadrature':{'near0':n0,'middle':n1,'C_error_upper':err0.hi+err1.hi+et.hi}}

def blank():return (I.coerce(0),)*6

def step(state,a):
    # S=E[sigma_last exp(iu X)]/(i E exp(iu X)); positive odd coefficients.
    s1,s3,s5,l2,l4,l6=state;q=I.rat(1,5)
    a2=a*a;a3=a2*a;a4=a2*a2;a5=a4*a;a6=a3*a3
    k2=q*a*s1;k4=q*(a*s3+a3*s1/3);k6=q*(a*s5+a3*s3/3+2*a5*s1/15)
    n1=a+q*s1;n3=a3/3+q*s3;n5=2*a5/15+q*s5
    return (n1,n3+n1*k2,n5+n3*k2+n1*(k4+k2*k2),
            l2+a2/2+k2,l4+a4/12+k4+k2*k2/2,
            l6+a6/45+k6+k2*k4+k2*k2*k2/3)

def combine(p,t):
    # t is the REVERSED tail so its endpoint is adjacent to the head.
    x1,x3,x5,l2,l4,l6=p;y1,y3,y5,m2,m4,m6=t;q=I.rat(1,5)
    k2=q*x1*y1;k4=q*(x1*y3+x3*y1);k6=q*(x1*y5+x3*y3+x5*y1)
    return (2*(l2+m2+k2),24*(l4+m4+k4+k2*k2/2),
            720*(l6+m6+k6+k2*k4+k2*k2*k2/3))

def tail_data(constants,N=16384):
    d=constants['d'];weights=[]
    for n in range(32,N+1):
        a=I.rat(1,2*n)+d*log(n)/(n*n)
        require(a.lo>0 and a.hi<I.rat(1,2*n).hi,'positive tail weights')
        weights.append(a)
    state=blank()
    for a in reversed(weights):state=step(state,a)
    z=I.rat(81,100)
    fw=(z,z**3/3,2*z**5/15,I.coerce(0),I.coerce(0),I.coerce(0))
    for a in weights:fw=step(fw,a)
    require(fw[0].hi<I.rat(3,4*N).lo,'order-1 tail majorant')
    require(fw[0].hi<I.rat(3,2*N).lo and fw[1].hi<(I.rat(3,2*N)**3/3).lo,'order-3 tail majorant')
    require(fw[0].hi<I.rat(3,N).lo and fw[1].hi<(I.rat(3,N)**3/3).lo and fw[2].hi<(2*I.rat(3,N)**5/15).lo,'order-5 tail majorant')
    def integral(m):
        ln=log(m)
        return I.rat(1,4*m)+d*(ln+F(1,2))/(2*m*m)+d*d*(ln*ln+F(2,3)*ln+F(2,9))/(3*m**3)
    vlo=F(3,2)*integral(N+1)-I.rat(5,64*N*N)
    vhi=F(3,2)*integral(N)+I.rat(3,16*N*(N+1))
    variance_tail=I(vlo.lo,vhi.hi)
    k4tail=I(0,I.rat(27,8*N**3).hi)
    k6tail=I(0,I.rat(11664,5*N**5).hi)
    return {'state':state,'tail':(variance_tail,k4tail,k6tail),'N':N,'forward':fw[:3]}

def head(constants,t,lam):
    A=constants['A'];t=I.coerce(t);lam=I.coerce(lam)
    base=A*(1-t)/31
    aa=[base+A*t/(3+lam)]*3+[base+A*t*lam/(3+lam)]+[base]*27
    require(all(a.lo>0 for a in aa),'positive head')
    s=blank()
    for a in aa:s=step(s,a)
    return s

def all_cumulants(constants,tail,t,lam):
    v,k4,k6=combine(head(constants,t,lam),tail['state'])
    tv,t4,t6=tail['tail']
    return v+tv,k4+t4,k6+t6

def rational_bracket(constants,tail,target,lam):
    # Isolate the unique positive variance root with conservative strict signs.
    lo=F(19,100);hi=F(1,5)
    # This range applies to the narrow lambda rectangle used by this certificate.
    require(all_cumulants(constants,tail,lo,lam)[0].hi<target.lo,'variance bracket left')
    require(all_cumulants(constants,tail,hi,lam)[0].lo>target.hi,'variance bracket right')
    for _ in range(32):
        mid=(lo+hi)/2;vv=all_cumulants(constants,tail,mid,lam)[0]
        if vv.hi<target.lo:lo=mid
        elif vv.lo>target.hi:hi=mid
        else:
            left=(3*lo+hi)/4;right=(lo+3*hi)/4
            vl=all_cumulants(constants,tail,left,lam)[0]
            vr=all_cumulants(constants,tail,right,lam)[0]
            old=(lo,hi)
            if vl.hi<target.lo:lo=left
            if vr.lo>target.hi:hi=right
            if old==(lo,hi):break
    return lo,hi

def pos_cumulants(mu):
    v=mu[2]
    return v,3*v*v-mu[4],mu[6]-15*mu[4]*v+30*v**3

def strict_json(path):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'duplicate JSON key');d[k]=v
        return d
    def reject(x):raise ValueError('nonintegral JSON number')
    return json.loads(Path(path).read_text(),object_pairs_hook=pairs,parse_float=reject,parse_constant=reject)


def algebra_controls():
    from itertools import product
    q=F(1,5)
    def enumerate_law(weights):
        mom=[F(0) for _ in range(7)];odd=[F(0) for _ in range(6)]
        for signs in product((-1,1),repeat=len(weights)):
            p=F(1,2)
            for i in range(len(signs)-1):p*=(1+q*signs[i]*signs[i+1])/2
            x=sum((a*s for a,s in zip(weights,signs)),F(0))
            for j in range(7):mom[j]+=p*x**j
            for j in (1,3,5):odd[j]+=p*signs[-1]*x**j
        require(mom[0]==1 and all(mom[j]==0 for j in (1,3,5)),'enumerated normalization/symmetry')
        m2,m4,m6=mom[2],mom[4],mom[6]
        exact=(odd[1],odd[1]*m2/2-odd[3]/6,
               odd[1]*(m2*m2/4-m4/24)-odd[3]*m2/12+odd[5]/120,
               m2/2,(3*m2*m2-m4)/24,(m6-15*m4*m2+30*m2**3)/720)
        return exact
    def contains(interval,rational):
        require(F(interval.lo,SCALE)<=rational<=F(interval.hi,SCALE),'independent spin reconstruction')
    chain_cases=combine_cases=0
    for n in range(1,8):
        for mode in (0,1):
            weights=[F(1,i+2) if mode==0 else F(2*i+1,32) for i in range(n)]
            exact=enumerate_law(weights);st=blank()
            for a in weights:st=step(st,I.coerce(a))
            for x,e in zip(st,exact):contains(x,e)
            chain_cases+=1
            if n>=2:
                k=n//2;p=blank();t=blank()
                for a in weights[:k]:p=step(p,I.coerce(a))
                for a in reversed(weights[k:]):t=step(t,I.coerce(a))
                out=combine(p,t)
                for x,e in zip(out,(2*exact[3],24*exact[4],720*exact[5])):contains(x,e)
                combine_cases+=1
    def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    P=[[F(5,8),F(3,8)],[F(3,8),F(5,8)]]
    R=[[F(3,4),F(1,4)],[F(1,4),F(3,4)]]
    require(mm(R,R)==P,'positive transition square root')
    matrix_cases=0
    for n in range(1,6):
        fields=[F(i+3,2) for i in range(n)];Q=[[F(1),F(0)],[F(0),F(1)]]
        for x in fields:
            T=mm(mm(R,[[x,F(0)],[F(0),1/x]]),R)
            require(T[0][0]*T[1][1]-T[0][1]*T[1][0]==F(1,4),'transfer determinant')
            require(T[0][0]+T[1][1]==F(5,8)*(x+1/x),'Perron trace')
            Q=mm(Q,T)
        expect=F(0)
        for signs in product((-1,1),repeat=n):
            p=F(1,2)
            for i in range(n-1):p*=(1+F(1,4)*signs[i]*signs[i+1])/2
            for x,s in zip(fields,signs):p*=x**s
            expect+=p
        require(sum(map(sum,Q))/2==expect,'complete transfer product')
        matrix_cases+=1
    integral_cases=0
    for d in (F(-2),F(-7,4),F(-1),F(0),F(1,3)):
        poly={(1,0):F(1,4),(2,1):d/2,(2,0):d/4,
              (3,2):d*d/3,(3,1):2*d*d/9,(3,0):2*d*d/27}
        deriv={}
        for (k,j),a in poly.items():
            deriv[k+1,j]=deriv.get((k+1,j),F(0))-k*a
            if j:deriv[k+1,j-1]=deriv.get((k+1,j-1),F(0))+j*a
        deriv={k:v for k,v in deriv.items() if v}
        want={k:v for k,v in {(2,0):F(-1,4),(3,1):-d,(4,2):-d*d}.items() if v}
        require(deriv==want,'analytic tail integral derivative')
        integral_cases+=1
    for deg,alpha,a in ((1,F(1,5),F(3,4)),(3,F(3,5),F(3,2)),(5,F(3,4),F(3))):
        require(all(q<=alpha**j for j in range(1,deg+1,2)),'coefficientwise q bound')
        require(F(1,2)+alpha*a*F(65,64)<=a,'all-future induction')
    require(2*q/(1+q*q)==F(5,13),'conditional odd-spin bias')
    require(F(72,169)*F(1,256)>F(1,640),'density Fourier constant')
    return {'direct_spin_panels':chain_cases,'joined_segment_panels':combine_cases,
            'rational_transfer_panels':matrix_cases,'tail_integral_derivatives':integral_cases,
            'all_future_induction_panels':3,'density_constants':2}


def reconstruct():
    algebra=algebra_controls()
    raw,mu,errs=theta_moments();target=pos_cumulants(mu)
    require(target[0].lo>I.rat(46,1000).hi and target[0].hi<I.rat(47,1000).lo,'theta variance')
    con=fixed_constants();tail=tail_data(con)
    lams=(F(325,1000),F(328,1000));panels=[]
    for lam in lams:
        lo,hi=rational_bracket(con,tail,target[0],lam)
        tbox=I(I.coerce(lo).lo,I.coerce(hi).hi)
        vals=all_cumulants(con,tail,tbox,lam)
        diff=(vals[1]-target[1])/(2*target[0]**2)
        panels.append({'lambda':str(lam),'t_interval':[str(lo),str(hi)],'fourth_ratio_difference':diff.record()})
    require(panels[0]['fourth_ratio_difference'][0]>0,'positive fourth endpoint')
    require(panels[1]['fourth_ratio_difference'][1]<0,'negative fourth endpoint')
    # Subdivision is a finite COVER of the whole lambda interval; at each
    # cell both strict variance signs enclose every root in that cell.
    curve=[];sixths=[];parts=16
    for j in range(parts):
        la=lams[0]+(lams[1]-lams[0])*F(j,parts)
        lb=lams[0]+(lams[1]-lams[0])*F(j+1,parts)
        lam_box=I(I.coerce(la).lo,I.coerce(lb).hi)
        tl,th=rational_bracket(con,tail,target[0],lam_box)
        box=I(I.coerce(tl).lo,I.coerce(th).hi)
        vk=all_cumulants(con,tail,box,lam_box)
        sixth=(vk[2]-target[2])/target[0]**3
        require(sixth.lo>I.rat(1,200).hi and sixth.hi<I.rat(1,20).lo,
                'nonzero sixth moment defect on curve cell '+str(j))
        sixths.append(sixth)
        curve.append({'lambda':[str(la),str(lb)],'t':[str(tl),str(th)],
                      'sixth_defect':sixth.record()})
    sixth=I(min(x.lo for x in sixths),max(x.hi for x in sixths))
    return {'schema':'CTC26.v1','status':'proposed-component-not-RH','rh_proved':False,
      'algebra_controls':algebra,'bits':BITS,'theta_cells':84,'theta_degree':DEGREE,'theta_raw':{str(k):x.record() for k,x in raw.items()},
      'theta_positive_cumulants':[x.record() for x in target],
      'constants':{k:x.record() for k,x in con.items() if isinstance(x,I)},
      'constant_quadrature':con['quadrature'], 'tail_index':tail['N'],
      'complete_tail_bounds':[x.record() for x in tail['tail']],
      'matching_panels':panels,'curve_cover':curve,
      'standardized_sixth_defect':sixth.record(), 'theta_tail_errors':errs}


def authenticate():
    paths={}
    for line in (ROOT/'SHA256SUMS').read_text().splitlines():
        h,p=line.split('  ',1);require(p not in paths and '/' not in p,'manifest path')
        f=ROOT/p;require(f.is_file() and not f.is_symlink(),'regular file')
        require(hashlib.sha256(f.read_bytes()).hexdigest()==h,'hash '+p);paths[p]=h
    require({p.name for p in ROOT.iterdir()}==set(paths)|{'SHA256SUMS'},'exact inventory')
    require('verify.py' in paths and 'PROOF.md' in paths,'required files')
    sources=strict_json(ROOT/'SOURCES.json')
    require(sources['parent']['head']=='0640c9c59be0bf20c18258460a7517fb09728e82','parent source lock')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--emit',action='store_true');ap.add_argument('--check');a=ap.parse_args()
    require(a.emit!=bool(a.check),'choose --emit or --check')
    if a.check:
        authenticate();old=strict_json(a.check)
        require(old.get('rh_proved') is False and old.get('status')=='proposed-component-not-RH','scope header')
        require(type(old.get('bits')) is int and old['bits']==BITS,'arithmetic type/header')
    result=reconstruct()
    if a.check:require(json.dumps(result,sort_keys=True,separators=(',',':'))==json.dumps(old,sort_keys=True,separators=(',',':')),'reconstruction mismatch')
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
