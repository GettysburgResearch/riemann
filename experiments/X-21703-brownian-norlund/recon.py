#!/usr/bin/env python3
"""FLOATING RECONNAISSANCE ONLY: contour and line-zero counts."""
import numpy as np
from scipy.special import gammaln, loggamma
import time, sys


def raw_coeff(N):
    H=np.zeros(2*N+1,dtype=np.float64)
    H[1:]=np.cumsum(1/np.arange(1,2*N+1,dtype=np.float64))
    n=np.arange(1,N+1,dtype=np.float64)
    logC=np.log(4)+4*gammaln(N+1)-2*gammaln(N-n+1)-2*gammaln(N+n+1)
    C=np.exp(logC)
    a=C*(n*(H[N+np.arange(1,N+1)]-H[N-np.arange(1,N+1)])-.5)
    b=.5*C
    return a,b

def norlund_coeff(N):
    H=np.zeros(2*N+1,dtype=np.float64)
    H[1:]=np.cumsum(1/np.arange(1,2*N+1,dtype=np.float64))
    HN=H[N]
    a=np.zeros(N); b=np.zeros(N)
    for K in range(1,N+1):
        ni=np.arange(1,K+1)
        nf=ni.astype(float)
        logC=np.log(4)+4*gammaln(K+1)-2*gammaln(K-nf+1)-2*gammaln(K+nf+1)
        C=np.exp(logC)/(K*HN)
        hd=H[K+ni]-H[K-ni]
        a[:K]+=C*(nf*hd-.5)
        b[:K]+=.5*C
    return a,b

def D_eval(s,a,b,chunk=256):
    sarr=np.atleast_1d(np.asarray(s,dtype=np.complex128))
    logs=np.log(np.arange(1,len(a)+1,dtype=float))
    out=np.zeros(sarr.size,dtype=np.complex128)
    for i in range(0,sarr.size,chunk):
        ss=sarr[i:i+chunk]
        E=np.exp(-ss[:,None]*logs[None,:])
        out[i:i+chunk]=E@a + ss*(E@b)
    return out.reshape(np.shape(s))

def logg(s):
    return -.5*s*np.log(np.pi)+loggamma(1+.5*s)

def Q_eval(s,a,b):
    s=np.asarray(s,dtype=np.complex128)
    D=D_eval(s,a,b)
    Dr=D_eval(1-s,a,b)
    ratio=np.exp(logg(1-s)-logg(s))
    return D+ratio*Dr

def Aline(t,a,b):
    s=.5+1j*np.asarray(t)
    D=D_eval(s,a,b)
    lg=logg(s)
    return 2*np.real(np.exp(1j*np.imag(lg))*D)

def line_count(T,a,b,step=.03):
    ts=np.arange(0,T+step,step)
    vals=Aline(ts,a,b)
    signs=np.sign(vals)
    for i in range(1,len(signs)):
        if signs[i]==0: signs[i]=signs[i-1]
    return int(np.sum(signs[:-1]*signs[1:]<0)), np.min(np.abs(vals)), ts, vals

def winding(T,a,b,eps=.02,dt=.03,ds=.002):
    nb=max(10,int((1-2*eps)/ds))
    nv=max(100,int(T/dt))
    bottom=np.linspace(eps,1-eps,nb,endpoint=False)+0j
    right=(1-eps)+1j*np.linspace(0,T,nv,endpoint=False)
    top=np.linspace(1-eps,eps,nb,endpoint=False)+1j*T
    left=eps+1j*np.linspace(T,0,nv+1)
    path=np.concatenate([bottom,right,top,left])
    vals=Q_eval(path,a,b)
    angles=np.unwrap(np.angle(vals))
    w=(angles[-1]-angles[0])/(2*np.pi)
    return w, np.min(np.abs(vals))

if __name__=='__main__':
    kind=sys.argv[1]; N=int(sys.argv[2]); T=float(sys.argv[3]); step=float(sys.argv[4]) if len(sys.argv)>4 else .05
    st=time.time(); a,b=(raw_coeff(N) if kind=='raw' else norlund_coeff(N)); print('coeff',time.time()-st)
    lc,mn,*_=line_count(T,a,b,step)
    print('line',lc,'min',mn)
    st=time.time(); w,mb=winding(T,a,b,dt=step,ds=.003); print('wind',w,'round',round(w),'minb',mb,'time',time.time()-st)
