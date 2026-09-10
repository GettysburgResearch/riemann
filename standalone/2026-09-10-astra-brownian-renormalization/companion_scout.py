#!/usr/bin/env python3
"""NONCERTIFYING critical-band companion scout; no zeta/zero oracle.

Requires NumPy/SciPy. Quadrature, interpolation and gamma are binary64.
No reported value is an interval bound or a zero certificate.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import loggamma
import argparse,json,math,platform
from pathlib import Path
import scipy
ap=argparse.ArgumentParser(description=__doc__)
ap.add_argument('--step',type=float,default=.01)
ap.add_argument('--angle',type=float,default=-1.4)
ap.add_argument('--out',type=Path,required=True)
args=ap.parse_args()
h,angle=args.step,args.angle
if not (.002<=h<=.04 and -math.pi/2<angle<-.5):
    ap.error('unsupported step/angle; stay in the Laplace half-plane')
x=np.arange(-40,28+h/2,h);t=np.exp(x+1j*angle)

def actual(t):
    a=np.sqrt(6*t)
    L=2*a*np.exp(-a)/(-np.expm1(-2*a))
    D=.5*L*(1-a*(1+np.exp(-2*a))/(-np.expm1(-2*a)))
    small=abs(t)<1e-5
    if np.any(small):
        # first ten exact sinh coefficients generated separately by series.
        import fractions,math
        F=fractions.Fraction
        cc=[F(1)]
        for j in range(1,10):
            cc.append(-sum(F(6**k,math.factorial(2*k+1))*cc[j-k] for k in range(1,j+1)))
        cf=np.array(list(map(float,cc)))
        L[small]=np.polynomial.polynomial.polyval(t[small],cf)
        D[small]=np.polynomial.polynomial.polyval(t[small],cf*np.arange(len(cf)))
    return L,D
L,D=actual(t)
v,w=leggauss(64);u=(v+3)/2;w=w/2*u**-4/(7/24)
idx=np.arange(len(x)); offs=np.arange(-5,7);params=[]
for u0,ww in zip(u,w):
    sh=-2*np.log(u0)/h;k=int(np.floor(sh));f=sh-k
    cw=[]
    for a in offs:
        z=1.
        for b in offs:
            if b!=a:z*=(f-b)/(a-b)
        cw.append(z)
    params.append((k,np.array(cw),ww,u0))
BL=np.ones_like(L)
for n in range(96):
    out=np.zeros_like(BL)
    for k,cw,ww,u0 in params:
        val=np.zeros_like(BL)
        for off,c in zip(offs,cw):
            ii=idx+k+off
            tmp=BL[np.clip(ii,0,len(BL)-1)].copy()
            low=ii<0
            if np.any(low):
                bt=np.exp(-40+ii[low]*h+1j*angle)
                mean=(93/47)*(1-(93/140)**n)
                tmp[low]=1-mean*bt
            val+=c*tmp
        lu,_=actual(t/u0**2)
        out+=ww*val*lu
    BL=out
CL=BL*L

def mc(p):
    if p.imag<0:return np.conj(mc(np.conj(p)))
    # p=q-2, use inverse-moment integral and a contour rotation.
    integr=np.trapezoid(np.exp(-p*x)*CL,x)
    return np.exp(-loggamma(-p)-1j*angle*p)*integr

def G(s):
    q=s/2
    return .5*np.exp(q*np.log(np.pi/6))*q*(q-1)*mc(q-2)

def xi(s):
    if s.real<=0:s=1-s
    q=s/2
    if q.imag<0:return np.conj(xi(np.conj(s)))
    integ=np.trapezoid(np.exp(-q*x)*(-2*L*D),x)+2*np.exp(1j*angle+(1-q)*(-40))/(1-q)
    return .5*np.exp(q*np.log(np.pi/6)-loggamma(1-q)-1j*angle*q)*integ
records=[]
for xx in [0.,2.,5.,10.,14.,17.,20.,21.,25.,30.]:
    for yy in [.05,.2,.4]:
        z=xx+1j*yy;s=.5+1j*z
        A=xi(s)
        B=(G(s)-G(1-s))/(2j)
        score=float(np.imag(A*np.conj(B))/(abs(A)*abs(B)))
        records.append({'z':[xx,yy],'A':[float(A.real),float(A.imag)],'B':[float(B.real),float(B.imag)],'normalized_HB_score':score})
print(records)
args.out.write_text(json.dumps({'status':'EMPIRICAL_NOT_CERTIFIED','rh_proved':False,'h':h,'angle':angle,'steps':96,'xmin':-40,'xmax':28,'u_gauss_nodes':64,'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'records':records},indent=2,allow_nan=False)+'\n',encoding='utf-8')
