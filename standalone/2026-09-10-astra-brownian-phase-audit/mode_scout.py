#!/usr/bin/env python3
"""NONCERTIFYING exploration of source-prescribed renormalization modes."""
import numpy as np, mpmath as mp, json,time
from numpy.polynomial.legendre import leggauss
from scipy.special import loggamma
from scipy.signal import convolve
from pathlib import Path
mp.mp.dps=40;st=time.time();h=.004;angle=-2.6;x=np.arange(-44.,18.+h/2,h);t=np.exp(x+1j*angle)
z=np.sqrt(6*t);L=2*z*np.exp(-z)/(-np.expm1(-2*z));sm=abs(t)<1e-5
L[sm]=1-t[sm]+.7*t[sm]**2-31/70*t[sm]**3+381/1400*t[sm]**4
nodes=160;v,w=leggauss(nodes);u=(v+3)/2;w=w/2;offs=range(-6,8)
a=lambda m: np.expm1((1-2*m)*np.log(2))/(1-2*m) if abs(m-.5)>1e-12 else np.log(2)
params=[]
for uu,ww in zip(u,w):
 sh=-2*np.log(uu)/h;k=int(np.floor(sh));f=sh-k;row=[]
 for j in offs:
  v=ww
  for jj in offs:
   if jj!=j:v*=(f-jj)/(j-jj)
  row.append((k+j,v))
 params.append((uu,row))

def make(m):
 terms={}
 for uu,row in params:
  scale=uu**(-2*m)/a(m)
  for j,v in row:terms[j]=terms.get(j,0)+v*scale
 lo,hi=min(terms),max(terms);ker=np.array([terms.get(i,0) for i in range(lo,hi+1)])
 pp=np.ones_like(L);b=a(m+1)/a(m);mean=b/(1-b)
 for n in range(160):
  le=np.exp(x[0]+np.arange(lo,0)*h+1j*angle)
  pad=np.r_[1-(1+mean*(1-b**n))*le,pp*L,np.zeros(hi,complex)]
  pp=convolve(pad,ker[::-1],mode='valid',method='direct')
 return pp*L
modes=[0.,1.,.999,1.001,1.5,2.,3.,4.,5.,6.];CL={m:make(m) for m in modes}
print('laws ready',time.time()-st,flush=True)

def G(s,m):
 if s.imag<0:return G(s.conjugate(),m).conjugate()
 q=s/2
 # integral normalized by Gamma(-q), not by Gamma(m-q).
 integ=np.trapezoid(np.exp((m-q)*x)*CL[m],x)
 # Origin subtraction is necessary for m<=Re(q); test uses q.real<.5 and m>=1.
 return .5*np.exp(q*np.log(np.pi/6)-loggamma(-q)-1j*angle*(q-m)+np.pi*s.imag/4)*integ

def xi(s):
 s=mp.mpc(s);return complex(s*(s-1)/2*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)*mp.exp(mp.pi*abs(s.imag)/4))
records=[]
for height in np.arange(.5,100.1,.5):
 for y in [.02,.2,.45]:
  s=.5-y+1j*height;A=xi(s);bs={m:(G(s,m)-G(1-s,m))/(2j) for m in modes if m>=.999}
  bs['neutral_derivative']=(bs[1.001]-bs[.999])/.002
  rr={'z':[float(height),y],'A':[A.real,A.imag],'modes':{}}
  for m,B in bs.items():
   score=float(np.imag(A*np.conj(B))/(abs(A)*abs(B)))
   rr['modes'][str(m)]={'B':[B.real,B.imag],'score':score}
  records.append(rr)
summary={}
for key in records[0]['modes']:
 vals=[r['modes'][key]['score'] for r in records]
 summary[key]={'negative':sum(v<0 for v in vals),'positive':sum(v>0 for v in vals),'min':min(vals),'max':max(vals),'first_negative':next((r['z'] for r in records if r['modes'][key]['score']<0),None)}
print(summary,flush=True)
Path('mode_scout_results.json').write_text(json.dumps({'status':'EMPIRICAL_NOT_CERTIFIED','step':h,'angle':angle,'depth':160,'nodes':nodes,'summary':summary,'records':records},indent=2)+'\n')
