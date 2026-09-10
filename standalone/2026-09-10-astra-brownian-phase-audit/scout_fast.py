#!/usr/bin/env python3
"""Exploratory binary64 slit-sector companion scout, NOT certified."""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import loggamma
from scipy.signal import convolve
import mpmath as mp
import argparse,json,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--angle',type=float,default=-2.5);p.add_argument('--step',type=float,default=.006);p.add_argument('--depth',type=int,default=128);p.add_argument('--nodes',type=int,default=128);p.add_argument('--max-height',type=int,default=100);p.add_argument('--out',required=True)
a=p.parse_args();st=time.time();mp.mp.dps=40
h=a.step;ang=a.angle;x=np.arange(-44.,18.+h/2,h);t=np.exp(x+1j*ang)
def lap(t):
 z=np.sqrt(6*t);out=2*z*np.exp(-z)/(-np.expm1(-2*z));sm=np.abs(t)<1e-5
 out[sm]=1-t[sm]+.7*t[sm]**2-31/70*t[sm]**3+381/1400*t[sm]**4
 return out
L=lap(t)
u,w=leggauss(a.nodes);u=(u+3)/2;w=w/2*u**-4/(7/24)
offs=range(-6,8);terms={}
for uu,ww in zip(u,w):
 sh=-2*np.log(uu)/h;k=int(np.floor(sh));f=sh-k
 for j in offs:
  v=ww
  for jj in offs:
   if jj!=j:v*=(f-jj)/(j-jj)
  terms[k+j]=terms.get(k+j,0)+v
lo,hi=min(terms),max(terms);ker=np.array([terms.get(i,0) for i in range(lo,hi+1)])
BL=np.ones_like(L)
for n in range(a.depth):
 le=np.exp(x[0]+np.arange(lo,0)*h+1j*ang)
 pad=np.r_[1-(1+93/47*(1-(93/140)**n))*le,BL*L,np.zeros(hi,complex)]
 BL=convolve(pad,ker[::-1],mode='valid',method='direct')
CL=BL*L
print('built',time.time()-st, 'max P',max(abs(BL)), flush=True)
def G(s):
 if s.imag<0:return G(s.conjugate()).conjugate()
 q=s/2
 it=np.trapezoid(np.exp((2-q)*x)*CL,x)
 pref=q*np.log(np.pi/6)-loggamma(2-q)-1j*ang*(q-2)+np.pi*s.imag/4
 return .5*q*(q-1)*np.exp(pref)*it

def xi(s):
 ss=mp.mpc(s)
 if s==0 or s==1:return complex(mp.mpf('.5'))
 return complex(ss*(ss-1)/2*mp.pi**(-ss/2)*mp.gamma(ss/2)*mp.zeta(ss)*mp.exp(mp.pi*abs(ss.imag)/4))

records=[]
for xx in np.arange(0,a.max_height+.1,.5):
 for yy in [.02,.2,.45]:
  s=.5-yy+1j*xx;A=xi(s);g=G(s);gr=G(1-s);B=(g-gr)/(2j)
  score=float(np.imag(A*np.conj(B))/(abs(A)*abs(B)))
  records.append({'z':[float(xx),yy],'score':score,'scaled_A':[A.real,A.imag], 'scaled_B':[B.real,B.imag]})
neg=[r for r in records if r['score']<0]
print('min',min(r['score'] for r in records), 'negative',len(neg), 'first',neg[:5], 'time',time.time()-st,flush=True)
Path(a.out).write_text(json.dumps({'status':'EMPIRICAL_NOT_CERTIFIED','args':vars(a),'kernel_sum':float(sum(ker)),'records':records},indent=2)+'\n')
np.savez(str(a.out)+'.npz',x=x,CL=CL,BL=BL,L=L,angle=ang)
