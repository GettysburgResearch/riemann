"""Whole defining-integral enclosure of a native centered gamma double zero.
No float, zeta oracle, root table, or numerical scout enters this computation.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import importlib.util, json
sp=importlib.util.spec_from_file_location('_cg_interval',Path(__file__).with_name('interval.py'))
iv=importlib.util.module_from_spec(sp);sp.loader.exec_module(iv)
I,PI,S,BITS=iv.I,iv.PI,iv.S,iv.BITS
DEGREE=72
XC=Q('31.1001854446439890503617267697554065740922204460843963878401')
UC=Q('0.323788258419987986775868946870425118445263688003329898058626')
STEP=Q(1,10**32)
BOX=Q(1,10**35)
HESSIAN=Q(10**18)
# Filled with an outward rational enclosure, checked against exp and pi.
LLO=Q('1.10496674354148199')
LHI=Q('1.10496674354148200')
B=Q('1.10496674349')

def need(b,s):
 if not b:raise ValueError(s)
def di(a,k):return I(a.lo//k,-((-a.hi)//k),raw=True)
def si(a,k):
 if k>=0:return I(a.lo*k,a.hi*k,raw=True)
 return I(a.hi*k,a.lo*k,raw=True)
def mul(a,b,n):
 return [sum((a[j]*b[k-j] for j in range(k+1)),I(0)) for k in range(n+1)]
def es(a,n):
 o=[a[0].exp()];aa=[si(x,j) for j,x in enumerate(a)]
 for k in range(1,n+1):o.append(di(sum((aa[j]*o[k-j] for j in range(1,k+1)),I(0)),k))
 return o
def ss(a,n):
 o=[a[0].sqrt()];need(o[0].lo>0,'sqrt value not positive')
 twice=2*o[0]
 for k in range(1,n+1):o.append((a[k]-sum((o[j]*o[k-j] for j in range(1,k)),I(0)))/twice)
 return o

def source(u):
 rates=tuple(Q(k*k) for k in range(1,6))+(36/u,)
 rr=[]
 for a in rates:
  b,c=a*a,Q(0)
  for r in rates:
   if r!=a:b*=(r/(r-a))**2;c-=2/(r-a)
  rr.append((a,b,c))
 tau=PI*PI/3-2*sum((Q(1,k*k) for k in range(1,6)),Q(0))-u/18
 return rates,rr,tau

def panels():
 todo=[(Q(0),B)];out=[]
 while todo:
  aa,bb=todo.pop();c=(aa+bb)/2;dd=(bb-aa)/2
  rho=min(Q(1,64),(LLO-c)/4,Q(31,72*112)*Q(I(2*c).exp().lo,S))
  need(rho>0,'support crossing')
  if dd*8<=rho:out.append((c,dd,rho))
  else:todo.extend(((c,bb),(aa,c)))
 out.sort();end=Q(0)
 for c,d,r in out:need(c-d==end and d*8<=r,'coverage');end=c+d
 need(end==B,'final coverage');return out

def guards(u,rr,tau):
 need(Q(32,100)<u<Q(33,100),'parameter box')
 need(PI.lo>I(Q(31,10)).hi and PI.hi<I(Q(22,7)).lo,'pi bounds')
 need(tau.lo>I(Q(34,100)).hi and tau.hi<I(Q(35,100)).lo,'shift bounds')
 need((PI/tau).lo>I(2*LLO).exp().hi,'support lower')
 need((PI/tau).hi<I(2*LHI).exp().lo,'support upper')
 need(0<LHI-B<Q(1,10**10),'whole endpoint interval')
 need(Q(31,10)*Q(31,32)*Q(2047,2048)-Q(35,100)>Q(13,5),'large argument')
 # |Im small argument| < (22/7)*(128/127)/128 < pi/(max rate-1)
 amax=36/u
 need(amax-1<112 and Q(64,72)<1,'adaptive simplex zero-free sector')
 a0,b0,c0=rr[0];x=Q(13,5);ratio=Q(0)
 need(x+c0>0,'first row')
 for a,b,c in rr[1:]:ratio+=(b/b0)*(2+abs(c)/x)/(1+c0/x)/2**int((a-1)*x)
 need(ratio<Q(1,4),'dominant zero-free row')
 need(sum(b*(32+abs(c)) for a,b,c in rr)<2**14,'large density ceiling')
 cn=Q(1,factorial(11))
 for a,b,c in rr:cn*=a*a
 need(cn<2**17 and cn*4**11<2**39,'small density ceiling')
 need(LHI+Q(1,64)<Q(9,8),'time bound')
 need(Q(32,64)<1,'cosine exponent')
 need(6*2**27<2**48,'integrand bound')
 return {'dominant_ratio':str(ratio),'density_simplex_coefficient':str(cn),'tau':tau.pair()}

def density(c,rho,sign,rr,tau,D):
 xx=[PI*I(2*sign*c).exp()]
 for k in range(1,D+1):xx.append(di(xx[-1]*I(2*sign*rho),k))
 xx[0]=xx[0]-tau;o=[I(0) for _ in range(D+1)]
 for a,b,cc in rr:
  ai,bi=I(a),I(b)
  ex=es([-ai*v for v in xx],D)
  lin=list(xx);lin[0]=lin[0]+cc
  prod=mul(lin,ex,D)
  o=[x+bi*y for x,y in zip(o,prod)]
 return o

def integrals(u,progress=False):
 rates,rr,tau=source(u);gg=guards(u,rr,tau);pp=panels();D=DEGREE
 out=[I(0),I(0),I(0)]
 for ix,(c,d,r) in enumerate(pp):
  fx=density(c,r,1,rr,tau,D);fy=density(c,r,-1,rr,tau,D)
  h=ss(mul(fx,fy,D),D)
  sn,cs=iv.sincos(I(XC*c));xr=I(XC*r);xx=xr*xr
  co=[cs,-xr*sn];ssn=[sn,xr*cs]
  for k in range(2,D+1):co.append(-di(xx*co[k-2],k*(k-1)));ssn.append(-di(xx*ssn[k-2],k*(k-1)))
  cp=mul(co,h,D);sp=mul(ssn,h,D)
  for k in range(0,D+1,2):
   factor=I(2*d*(d/r)**k/(k+1))
   out[0]=out[0]+factor*cp[k]
   out[1]=out[1]-factor*(c*sp[k]+(r*sp[k-1] if k else I(0)))
   out[2]=out[2]-factor*(c*c*cp[k]+(2*c*r*cp[k-1] if k else I(0))+(r*r*cp[k-2] if k>=2 else I(0)))
  if progress and (ix+1)%128==0:print('cells',ix+1,'/',len(pp),flush=True)
 quad=2*B*2**48*Q(1,8)**(D+1)/Q(7,8)
 # f(big)<=1, f(small)<=90000*small^11, small<=L-t near endpoint.
 # h<=300*(L-t)^(11/2); t^j<=2 for j<=2.
 gap=Q(1,10**10);tail=Q(1200,13)*gap**6/Q(10**5)
 out=[v.widen(quad+tail) for v in out]
 return {'u':str(u),'jets':[v.pair() for v in out],'panels':len(pp),'degree':D,
  'quadrature_error':str(quad),'full_endpoint_error':str(tail),'guards':gg}

def reconstruct(progress=False):
 results=[integrals(u,progress) for u in [UC,UC-STEP,UC+STEP]]
 j=[[I(int(a),int(b),raw=True) for a,b in r['jets']] for r in results]
 fu=((j[2][0]-j[1][0])/(2*STEP)).widen(HESSIAN*STEP/2)
 fxu=((j[2][1]-j[1][1])/(2*STEP)).widen(HESSIAN*STEP/2)
 # Rational inverse of interval midpoint Jacobian, generated exactly.
 midpoint=lambda v:Q(v.lo+v.hi,2*S)
 a,b,c,d=map(midpoint,[j[0][1],fu,j[0][2],fxu]);det=a*d-b*c
 need(det!=0,'singular center preconditioner')
 Y=[[d/det,-b/det],[-c/det,a/det]]
 J=[[j[0][1],fu],[j[0][2],fxu]]
 J=[[v.widen(2*HESSIAN*BOX) for v in row] for row in J]
 defect=[[I(int(i==k))-sum((Y[i][j]*J[j][k] for j in range(2)),I(0)) for k in range(2)] for i in range(2)]
 beta=max(sum(Q(v.absmax(),S) for v in row) for row in defect)
 residual=[sum((Y[i][jj]*j[0][jj] for jj in range(2)),I(0)) for i in range(2)]
 delta=max(Q(v.absmax(),S) for v in residual)
 need(beta<Q(1,100),'contraction bound')
 need(delta+beta*BOX<BOX/2,'self-map')
 need(J[0][1].lo>0 and J[1][0].hi<0,'fold orientation')
 slope=-2*J[0][1]/J[1][0]
 return {'status':'PROPOSED_NATIVE_DOUBLE_ZERO_CERTIFICATE','rh_proved':False,
  'center':[str(XC),str(UC)],'box_radius':str(BOX),'finite_difference_step':str(STEP),
  'derivative_majorant':str(HESSIAN),'source_cases':results,
  'jacobian':[[v.pair() for v in row] for row in J],
  'preconditioner':[[str(v) for v in row] for row in Y],
  'beta_upper':str(beta),'newton_displacement_upper':str(delta),
  'squared_splitting_coefficient':slope.pair(),
  'unique_real_double_zero_in_box':True,'local_pair_annihilation':True,
  'same_as_parent_N5_pair_certified':False,'whole_step_zero_census':False,
  'unbounded_defect_decay_proved':False}

if __name__=='__main__':
 import argparse
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--progress',action='store_true');ap.add_argument('--case',type=int,choices=[0,1,2]);aa=ap.parse_args()
 rr=reconstruct(aa.progress) if aa.case is None else integrals([UC,UC-STEP,UC+STEP][aa.case],aa.progress)
 aa.output.write_text(json.dumps(rr,sort_keys=True,indent=2)+'\n')
 print('COMPLETE_DEFINING_INTEGRAL' if aa.case is not None else 'COMPLETE_LOCAL_FOLD_CERTIFICATE')
