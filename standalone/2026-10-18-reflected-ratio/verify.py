#!/usr/bin/env python3
"""Exact finite exponent/domain certificate. Not a certification of analytic inputs."""
from __future__ import annotations
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

EPS=Q(1,10**6)
A=Q(3,7); H=1-A; THETA=A/2; SHIFT=Q(5,6)-A/3
UPPERS=tuple(map(Q, '''16/25 337/500 281/400 7219/10000 3681/5000 7473/10000
7563/10000 7637/10000 77/100 1551/2000 1951/2500 981/1250 7889/10000
7927/10000 7963/10000 7997/10000 803/1000 4031/5000 4047/5000 4063/5000
4079/5000 8191/10000 329/400 8261/10000 8299/10000 417/500 1677/2000
1687/2000 2123/2500 8557/10000 1727/2000 873/1000 8851/10000 2253/2500
9241/10000 19/20'''.split()))

def p(x): return (Q(x),Q(0),Q(0))
def add(x,y): return tuple(a+b for a,b in zip(x,y))
def scale(x,c): return tuple(a*c for a in x)
def sub(x,y): return add(x,scale(y,-1))
def mul(x,y):
 out=[Q(0)]*5
 for i,a in enumerate(x):
  for j,b in enumerate(y):out[i+j]+=a*b
 if any(out[3:]):raise ValueError('polynomial degree exceeds two')
 return tuple(out[:3])
E=(Q(0),Q(1),Q(0))
def bern(x):
 c0,c1,c2=x
 return (c0,c0+c1*EPS/2,c0+c1*EPS+c2*EPS**2)

class Checks:
 def __init__(self):self.n=0
 def ok(self,value,label):
  self.n+=1
  if not value:raise ValueError(label)
 def nonneg(self,poly,label,strict=False):
  b=bern(poly)
  self.ok(all(x>=0 for x in b),label)
  if strict:self.ok(b[-1]>0,label+' strict on (0, epsilon_max]')
  return b

def density(s):
 q=2*s-1
 if s<=Q(2,3):
  da=Q(1,2);db=2/(4-6*q);nu=1-q/(4-6*q)
 elif s<=Q(11,12):
  den=6*q*(10-6*q)-10
  da=(24*q-5)/den;db=(42*q-8)/den
  nu=(9*q*(7-6*q)-10)/den
 else:
  den=1-6*(1-q)**2
  da=(6*q-4)/den;db=(8*q-5)/den
  nu=(1-q)*(8*q-5)/den
 terms=[Q(1,2)+(c+v*da)/2+(Q(1,2)-s)*db
        for c,v in ((Q(1),Q(0)),(Q(0),Q(1)),(Q(5,6),Q(1,3)),(Q(1,3),Q(5,6)))]
 terms += [(2-2*s)*db,1+(1-2*s)*da]
 terms += [Q(1,3)+(Q(11,6)-2*s)*v for v in (da,db)]
 terms += [Q(5,6)+(Q(4,3)-2*s)*v for v in (da,db)]
 return da,db,nu,terms

def domain(x,y,z):
 return (x,y,z,sub(add(scale(z,6),y),p(1)),sub(add(x,scale(z,6)),p(1)),
         sub(add(x,y),p(1)),sub(add(add(x,y),scale(z,6)),p(2)),
         sub(add(scale(x,6),scale(z,6)),p(5)),sub(x,p(Q(1,2))))

def physical(x,y,z,mu,top):
 ans=add(p(A/2-1),x)
 ans=add(ans,scale(z,H));ans=add(ans,scale(sub(y,p(1)),A))
 return add(ans,mul(top,sub(mu,z)))

def run(mutation=None,details=False):
 c=Checks();top=add(p(H),E)
 c.ok(Q(0)<A<Q(1,2),'short physical support')
 c.ok(SHIFT+THETA==Q(19,21),'true Mellin normalization')
 if mutation=='wrong-mellin-shift':c.ok(Q(37,54)+THETA==Q(19,21),'wrong borrowed Mellin shift')
 c.ok(all(x<y for x,y in zip(UPPERS,UPPERS[1:])),'ordered thresholds')
 classes=[{'mode':'M2','upper':UPPERS[0],'nu':Q(1),'lower':None}]
 density_rows=[]
 for lo,hi in zip(UPPERS,UPPERS[1:]):
  da,db,nu,terms=density(lo)
  c.ok(0<=da<=db,'detector lengths')
  for v in terms:c.ok(v<=nu,'all ten density monomials')
  c.ok(Q(0)<=nu<=1,'count exponent range')
  density_rows.append(dict(sigma=str(lo),A=str(da),B=str(db),nu=str(nu),terms=list(map(str,terms))))
  if mutation=='upper-count':nu=density(hi)[2]
  c.ok(nu==density(lo)[2],'count at lower threshold')
  classes.append({'mode':'FE','upper':hi,'nu':nu,'lower':lo})
 da,db,nu,terms=density(UPPERS[-1])
 for v in terms:c.ok(v<=nu,'terminal detector monomial')
 c.ok(nu==Q(11,47),'terminal density')
 density_rows.append(dict(sigma=str(UPPERS[-1]),A=str(da),B=str(db),nu=str(nu),terms=list(map(str,terms))))
 if mutation!='missing-terminal':classes.append({'mode':'terminal','upper':Q(1),'nu':nu,'lower':UPPERS[-1]})
 c.ok(len(classes)==37 and classes[-1]['mode']=='terminal','all 37 classes including terminal')
 report=[]
 for j,row in enumerate(classes):
  s=row['upper'];nu=row['nu'];mode=row['mode'];z=p(Q(1,2))
  if mode=='M2':
   x=add(p(s),scale(E,3));y=p(Q(1,2));mu=p(1)
  elif mode=='FE':
   x=add(p(s),scale(E,3));y=sub(p(1-s),E)
   exponent=sub(p(Q(1,2)),y)
   if mutation=='reverse-fe-power':exponent=scale(exponent,-1)
   c.ok(exponent==add(p(s-Q(1,2)),E),'functional equation conductor power')
   c.nonneg(exponent,'positive conductor power',strict=True)
   c.ok(sub(p(1),y)==add(p(s),E),'reflected point in same zero-free region')
   target='chi' if mutation=='wrong-character' else 'bar_chi'
   c.ok(target=='bar_chi','functional-equation character matches denominator')
   mu=add(p(nu),exponent)
   if mutation=='convex-numerator':mu=add(p(nu+s/2),scale(E,Q(1,2)))
  else:
   x=add(p(1),E);y=E;mu=add(p(nu+Q(1,2)),scale(E,Q(-1,2)))
  corners=((add(p(1),scale(E,3)),add(p(1),scale(E,3)),z),
           (x,add(p(1),scale(E,3)),z),(x,y,z))
  for xx,yy,zz in corners:
   for d in domain(xx,yy,zz):c.nonneg(d,'correction domain',strict=True)
   if mutation=='old-domain':c.nonneg(sub(scale(xx,3),p(2)),'old ramified domain',strict=True)
  c.nonneg(sub(mu,z),'positive U dyad exponent',strict=True)
  growth=physical(x,y,z,mu,top)
  c.nonneg(sub(add(p(THETA),scale(E,5)),growth),'central class budget')
  if mode=='FE':
   c.ok(growth[0]==A-Q(3,2)+H*(nu+2*s),'independent FE exponent expansion')
   c.ok(growth[0]<THETA,'strict zero-buffer central slack')
  if mode!='terminal':
   R=sub(p(2-s),scale(E,Q(1,4)));ro=sub(p(2-s),scale(E,Q(1,2)))
   rt=sub(p(2-s),E);ri=sub(p(1),scale(E,Q(1,4)))
   for d in (ri,sub(rt,ri),sub(ro,rt),sub(R,ro)):
    c.nonneg(d,'nested logarithm disks',strict=True)
  report.append({k:(str(v) if v is not None else None) for k,v in row.items()}|
                {'growth_coefficients':list(map(str,growth)),
                 'zero_buffer_slack':str(THETA-growth[0])})
 # Principal contours have x>1, so never use a proposed improved zero-free line.
 xx=add(p(1),E)
 for yy,zz in ((add(p(1),E),add(p(Q(1,6)),E)),(p(Q(1,2)),add(p(Q(1,6)),E)),
               (p(1),add(p(Q(1,6)),E)),(p(1),E)):
  for d in domain(xx,yy,zz):c.nonneg(d,'principal correction domain',strict=True)
 for base in (H/6,A/2):
  c.nonneg(sub(add(p(THETA),scale(E,2)),add(p(base),scale(E,1+H))),'principal remainder')
 small=add(p(H/4+Q(3,400)),E)
 c.nonneg(sub(add(p(THETA),scale(E,2)),small),'small frequencies')
 # Exact large line L=10/e+2; clearing e gives a polynomial.
 gap=p(0) if mutation=='lost-tail-gap' else E
 # E_large=3+7a/2+h + gap*(1-L) =4+5a/2 - 10 - e.
 if mutation=='lost-tail-gap':large=p(4+Q(5,2)*A)
 else:large=add(p(-6+Q(5,2)*A),scale(E,-1))
 c.nonneg(sub(p(-1),large),'large-frequency negative power',strict=True)
 c.ok(Q(49,54)-Q(19,21)==Q(1,378),'comparison with #969')
 c.ok(Q(68,75)-Q(19,21)==Q(1,525),'comparison with #970 archive')
 c.ok(Q(3,8)-(Q(3,4)-Q(1,2))==Q(1,8),'three-quarter selected-row gain')
 return {'status':'PASS_FINITE_CERTIFICATE_NOT_ANALYTIC_CERTIFICATION',
         'predicates':c.n,'classes':len(classes),'FE_classes':sum(x['mode']=='FE' for x in classes),
         'epsilon_max':str(EPS),'physical_a':str(A),'theta':str(THETA),'Mellin_shift':str(SHIFT),
         'proposed_boundary':str(SHIFT+THETA),'minimum_FE_slack':str(min(Q(x['zero_buffer_slack']) for x in report if x['mode']=='FE')),
         'density':density_rows if details else len(density_rows),
         'class_data':report if details else 'run --details',
         'independent_review':False,'RH_proved':False}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--details',action='store_true')
 ap.add_argument('--mutate',choices=['convex-numerator','reverse-fe-power','wrong-character','old-domain','upper-count','lost-tail-gap','missing-terminal','wrong-mellin-shift'])
 args=ap.parse_args()
 print(json.dumps(run(args.mutate,args.details),indent=2,sort_keys=True))
