#!/usr/bin/env python3
"""Complete-source BRN phase check. Outward balls, all finite and infinite tails.
Experimental implementation; analytic bounds and arithmetic require review.
"""
from ball_core import *
import argparse,json,time,sys
from pathlib import Path

HSTEP=F(1,8); R0=F(1,2); QR=[B.complex(F(3,20),F(119,4)),B.complex(F(7,20),F(119,4))]

def rot(v,k):
 k%=4
 if k==0:return v
 if k==1:return B(-v.b,v.a,v.e)
 if k==2:return B(-v.a,-v.b,v.e)
 return B(v.b,-v.a,v.e)

def norm_moments(m):
 ff=[B.real(F((-6)**n,factorial(2*n+1))) for n in range(m+1)]
 xx=[ONE]
 for n in range(1,m+1):
  ss=ZERO
  for k in range(1,n+1):ss=ss+ff[k]*xx[n-k]
  xx.append(-ss)
 pp=[ONE]
 for n in range(1,m+1):
  a=F(1-F(1,2**(2*n+3)),2*n+3); b=a/F(7,24)
  ss=ZERO
  for j in range(n):ss=ss+pp[j]*xx[n-j]
  pp.append(ss.rat(b/(1-b)))
 hh=convolution(pp,xx,m);zz=convolution(xx,xx,m)
 return xx,pp,hh,zz

def origin_delay(hh,r,h,n):
 # h_j are normalized C moments; compute H(-i(r+h*z)).
 out=[];M=len(hh)-1
 for k in range(n+1):
  ss=ZERO
  for j in range(M,k-1,-1):ss=ss.rat(r)+rot(hh[j],j).rat(comb(j,k))
  ss=ss.rat(h**k)
  out.append(ss.grow(rad(F(512)*(F(3,4)**(M+1))/2**k)))
 return out

def make_translate(n):
 cache={}
 for a in range(1,4):
  d=F(a,4);rows=[]
  for k in range(n+1):rows.append([(j,F(comb(j,k),4**k)*d**(j-k)) for j in range(k,n+1)])
  cache[a]=rows
 return cache

def delayed(old,a,n,cache):
 if a==0:return [old[k].rat(1,4**k) for k in range(n+1)]
 s=F(16)*(F(5,16)**(n+1))/(1-F(5,16))
 out=[]
 for k,row in enumerate(cache[a]):
  ss=ZERO
  for j,f in row:ss=ss+old[j].rat(f)
  out.append(ss.grow(rad(s/2**k)))
 return out

def weight_integral(f,r,alpha,h,n,kind):
 """h*r**alpha sum f_k int_0^1 z^k*(1+h/r*z)**alpha dz."""
 u=h/r; ws=[ONE]
 for j in range(1000):
  nxt=(ws[-1]*(alpha-j)).rat(u/F(j+1))
  if j>=32 and nxt.norm()<=Q//(1<<230):
   tail=ceildiv(nxt.norm()*(1-2*u).denominator,(1-2*u).numerator)
   break
  ws.append(nxt)
 else:raise ArithmeticError('weight series did not stop')
 ss=ZERO
 for k in range(n+1):
  ww=ZERO
  for j,w in enumerate(ws):ww=ww+w.rat(1,j+k+1)
  ss=ss+f[k]*ww
 out=powpos(r,alpha)*ss.rat(h)
 # Polynomial weight-series error, exact Taylor-polynomial bound <=32.
 scale=(r+1) if kind=='K' else F(2)
 out=out.grow(ceildiv(tail*(64*h*scale).numerator,(64*h*scale).denominator))
 # Whole true Taylor tail, |H|<=8 and |J|<=16 in radius 1/2 disks.
 bound=8 if kind=='K' else 16
 scale=(r+h+1) if kind=='K' else F(2)
 out=out.grow(rad(2*h*scale*bound*F(1,4)**(n+1)/(1-F(1,4))))
 return out

def origin_integrals(hh,zz,m):
 kk=[]
 for q in QR:
  ss=ZERO
  for j in range(m+1):ss=ss+rot(hh[j],j).rat(R0**j)/(j+2-q)
  kk.append((powpos(R0,2-q)*ss).grow(rad(F(1024)*F(2,3)**(m+1))))
 ss=ZERO;q=QR[0]
 for j in range(1,m+2):ss=ss-rot(zz[j],j).rat(j*R0**(j-1))/(j-q)
 jj=(powpos(R0,1-q)*ss).grow(rad(F(1024)*F(2,3)**(m+1)))
 return kk,jj

def tail_integral_bound(degree,rate,lower,mult):
 poly=sum((F(factorial(degree),factorial(degree-j))*lower**(degree-j)/rate**(j+1) for j in range(degree+1)),F(0))
 val=exp(B.real(-rate*lower)).rat(mult*poly)
 return abs(val.a)+abs(val.b)+val.e

def ball_record(z):return {'re_num':str(z.a),'im_num':str(z.b),'radius_num':str(z.e),'denominator_power_of_two':BITS}

def compute(n=80,m=384,end=512,progress=128):
 start=time.time();xx,pp,hh,zz=norm_moments(m+1)
 print('moments complete',time.time()-start,flush=True)
 kk,jj=origin_integrals(hh,zz,m)
 p0=ZERO
 for j in range(m+1):p0=p0+rot(pp[j],j).rat(R0**j)
 p0=p0.grow(rad(F(m+3,2**m)))
 origin_h=hh[:m+1];translations=make_translate(n);history={};max_prad=0;count=0
 for index in range(4,8*end):
  r=F(index,8);h=HSTEP
  ll=source_laplace_series(r,h,n+1)
  if index<16:dd=origin_delay(origin_h,r/4,h/4,n)
  else:dd=delayed(history[index//4],index%4,n,translations)
  ps=[p0];hs=[]
  for k in range(n+1):
   ss=ZERO
   for j in range(k+1):ss=ss+ll[j]*ps[k-j]
   hs.append(ss)
   if k<n:
    nxt=(ss.rat(h*F(24,7))-ps[k].rat(h*(3+2*k))-dd[k].rat(h*F(3,7))).rat(1/F(2*r*(k+1)))
    ps.append(nxt)
  history[index]=hs
  p0=sum(ps,ZERO).grow(rad(F(8)*F(1,4)**(n+1)/F(3,4)))
  max_prad=max(max_prad,p0.e)
  for k,q in enumerate(QR):kk[k]=kk[k]+weight_integral(hs,r,1-q,h,n,'K')
  lsq=convolution(ll,ll,n+1)
  js=[-lsq[k+1].rat((k+1)/h) for k in range(n+1)]
  jj=jj+weight_integral(js,r,-QR[0],h,n,'J')
  count+=1
  if progress and count%progress==0:
   print('cell',count,'r',float(r+h),'P',p0,'K radii',[v.radius() for v in kk],'J radius',jj.radius(),'elapsed',time.time()-start,flush=True)
 # A complete future bound is specified here for endpoint 512, no extrapolation.
 if end!=512:raise ValueError('tail contract currently requires endpoint 512')
 v=F(22627,1000);ak=F(13423,4000);aj=F(433,125)
 tailk=tail_integral_bound(8,ak,v,200)
 tailj=tail_integral_bound(2,aj,v,1152)
 kk=[v.grow(2*tailk) for v in kk];jj=jj.grow(2*tailj)
 cs=[]
 for q in QR:
  cs.append(exp(q*clog(PI/F(6))+I*PI*q/F(2)-loggamma(1-q)+PI*F(119,8))/2)
 aa=cs[0]*jj
 gg=[q*c*k for q,c,k in zip(QR,cs,kk)]
 bb=(gg[0]-gg[1].conj())/(2*I)
 phase=aa*bb.conj()
 passed=(-4700000*Q < phase.b-phase.e and phase.b+phase.e < -4600000*Q)
 return {'status':'PROPOSED_DIRECTED_NATIVE_PHASE_REFUTATION' if passed else 'INCONCLUSIVE','rh_proved':False,'off_line_zeta_zero_claimed':False,'point':{'x':'119/2','y':'1/5'},'positive_scale':'exp(119*pi/8) for A and B','bits':BITS,'degree':n,'origin_degree':m,'step':'1/8','endpoint':end,'cells':count,'P_max_radius':str(max_prad),'K':[ball_record(k) for k in kk],'J':ball_record(jj),'tail_K':str(tailk),'tail_J':str(tailj),'Cscaled':[ball_record(c) for c in cs],'A_scaled':ball_record(aa),'B_scaled':ball_record(bb),'phase_scaled':ball_record(phase),'strict_negative':passed,'coarse_phase_interval':['-4700000','-4600000']}

if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--degree',type=int,default=80);ap.add_argument('--origin-degree',type=int,default=384);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--progress',type=int,default=128);args=ap.parse_args()
 result=compute(args.degree,args.origin_degree,progress=args.progress)
 args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
 print(result['status'],[int(result['phase_scaled'][k])/Q for k in ['im_num','radius_num']],flush=True)
 if not result['strict_negative']:raise SystemExit(1)
