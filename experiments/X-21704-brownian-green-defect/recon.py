#!/usr/bin/env python3
"""FLOATING RECONNAISSANCE ONLY for the central-binomial Brownian producer."""
from __future__ import annotations

import sys
import time
import numpy as np
from scipy.special import gammaln, loggamma


def central_weights(N: int) -> np.ndarray:
    w=np.empty(N,dtype=float)
    om=0.25
    for k in range(1,N+1):
        if k>1:
            j=k-1
            om*=((2*j+1)/(2*j+2))**2
        w[k-1]=om
    return w/w.sum()


def coefficients(N: int) -> tuple[np.ndarray,np.ndarray]:
    H=np.zeros(2*N+1,dtype=float)
    H[1:]=np.cumsum(1/np.arange(1,2*N+1,dtype=float))
    weights=central_weights(N)
    a=np.zeros(N,dtype=float)
    b=np.zeros(N,dtype=float)
    for K in range(1,N+1):
        ni=np.arange(1,K+1)
        nf=ni.astype(float)
        logC=(np.log(4)+4*gammaln(K+1)
              -2*gammaln(K-nf+1)-2*gammaln(K+nf+1))
        C=np.exp(logC)*weights[K-1]
        hd=H[K+ni]-H[K-ni]
        a[:K]+=C*(nf*hd-.5)
        b[:K]+=.5*C
    return a,b


def D_eval(s,a,b,chunk=128):
    shape=np.shape(s)
    arr=np.atleast_1d(np.asarray(s,dtype=np.complex128)).ravel()
    logs=np.log(np.arange(1,len(a)+1,dtype=float))
    out=np.zeros(arr.size,dtype=np.complex128)
    for i in range(0,arr.size,chunk):
        ss=arr[i:i+chunk]
        E=np.exp(-ss[:,None]*logs[None,:])
        out[i:i+chunk]=E@a+ss*(E@b)
    return out.reshape(shape)


def logg(s):
    s=np.asarray(s,dtype=np.complex128)
    return -.5*s*np.log(np.pi)+loggamma(1+.5*s)


def Q_eval(s,a,b):
    s=np.asarray(s,dtype=np.complex128)
    return D_eval(s,a,b)+np.exp(logg(1-s)-logg(s))*D_eval(1-s,a,b)


def line_count(T,a,b,step):
    ts=np.arange(0,T+step,step)
    s=.5+1j*ts
    D=D_eval(s,a,b)
    vals=2*np.real(np.exp(1j*np.imag(logg(s)))*D)
    signs=np.sign(vals)
    for i in range(1,len(signs)):
        if signs[i]==0:
            signs[i]=signs[i-1]
    return int(np.sum(signs[:-1]*signs[1:]<0)),float(np.min(np.abs(vals)))


def winding(T,a,b,step,eps=.02,ds=.005):
    nb=max(10,int((1-2*eps)/ds))
    nv=max(100,int(T/step))
    path=np.concatenate([
        np.linspace(eps,1-eps,nb,endpoint=False)+0j,
        (1-eps)+1j*np.linspace(0,T,nv,endpoint=False),
        np.linspace(1-eps,eps,nb,endpoint=False)+1j*T,
        eps+1j*np.linspace(T,0,nv+1),
    ])
    vals=Q_eval(path,a,b)
    angles=np.unwrap(np.angle(vals))
    return (angles[-1]-angles[0])/(2*np.pi),float(np.min(np.abs(vals)))


if __name__ == "__main__":
    N=int(sys.argv[1])
    T=float(sys.argv[2])
    step=float(sys.argv[3]) if len(sys.argv)>3 else .1
    started=time.time()
    a,b=coefficients(N)
    line,min_line=line_count(T,a,b,step)
    wind,min_boundary=winding(T,a,b,step)
    print({
        "classification":"FLOATING_RECONNAISSANCE_ONLY",
        "N":N,
        "height":T,
        "step":step,
        "critical_line_crossings":line,
        "strip_winding":wind,
        "strip_winding_rounded":round(wind),
        "minimum_line_sample":min_line,
        "minimum_boundary_sample":min_boundary,
        "elapsed_seconds":time.time()-started,
    })
