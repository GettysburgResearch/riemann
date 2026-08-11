#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
from scipy.integrate import quad


def line_curvature(t,u):
    return u*u/(t+u*u)**3

def pair_curvature(t,d,u):
    z=complex(d,u)
    return -2*(z*z/(t-z*z)**3).real

def line_A(w,u):
    a=1+u*u
    return 2*u*u/(a*a*(a-w))

def pair_A(w,z):
    a=1-z*z
    return -2*(z*z/(a*a*(a-w)) + z.conjugate()**2/(a.conjugate()**2*(a.conjugate()-w))).real

def peano_numeric(w,fun):
    val,_=quad(lambda q:(w-q)*fun(1-q),0,w,epsabs=1e-12,epsrel=1e-12,limit=200)
    return 4*val/(w*w)

def line_ft_closed(t,xi):
    a=math.sqrt(t); L=abs(xi)
    return math.pi/(8*a**3)*(1+a*L-a*a*L*L)*math.exp(-a*L)

def line_ft_numeric(t,xi):
    if xi==0:
        val,_=quad(lambda u:line_curvature(t,u),-np.inf,np.inf,epsabs=1e-11,epsrel=1e-11,limit=300)
        return val
    val,_=quad(lambda u:line_curvature(t,u),0,np.inf,weight='cos',wvar=xi,epsabs=1e-11,epsrel=1e-11,limit=300,limlst=300)
    return 2*val

def normalized_line(k,u):
    return 2*u*u/(1+u*u)**(k+3)

def normalized_pair(k,z):
    return -4*(z*z/(1-z*z)**(k+3)).real

def Cder_line(k,u):
    return (-1)**k*math.factorial(k+2)/2*u*u/(1+u*u)**(k+3)

def Cder_pair(k,z):
    return (-1)**k*(-math.factorial(k+2))*(z*z/(1-z*z)**(k+3)).real

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json',type=Path); args=ap.parse_args()
    checks=0; max_peano=0; max_der=0; max_ft=0
    for u in [0.2,0.9,3.1]:
      for w in [0.1,0.55,0.9]:
        lhs=peano_numeric(w,lambda tt:line_curvature(tt,u)); rhs=line_A(w,u)
        err=abs(lhs-rhs)/max(1,abs(rhs)); max_peano=max(max_peano,err); assert err<1e-10; checks+=1
    for z in [complex(0.18,0.37),complex(0.31,1.2)]:
      for w in [0.1,0.45]:
        lhs=peano_numeric(w,lambda tt:pair_curvature(tt,z.real,z.imag)); rhs=pair_A(w,z)
        err=abs(lhs-rhs)/max(1,abs(rhs)); max_peano=max(max_peano,err); assert err<1e-10; checks+=1
    for k in range(10):
      for u in [0.3,1.4]:
        lhs=4*(-1)**k*Cder_line(k,u)/math.factorial(k+2); rhs=normalized_line(k,u)
        err=abs(lhs-rhs); max_der=max(max_der,err); assert err<1e-12; checks+=1
      for z in [complex(0.2,0.4),complex(0.42,1.1)]:
        lhs=4*(-1)**k*Cder_pair(k,z)/math.factorial(k+2); rhs=normalized_pair(k,z)
        err=abs(lhs-rhs); max_der=max(max_der,err); assert err<1e-12; checks+=1
    for a in [0.3,0.8]:
      for xi in [0,0.7,2.0]:
        num=line_ft_numeric(a*a,xi); rhs=line_ft_closed(a*a,xi)
        err=abs(num-rhs)/max(1,abs(rhs)); max_ft=max(max_ft,err); assert err<2e-9; checks+=1
    projector=[]
    for a,d in [(0.3,0.1),(0.5,0.2),(0.3,0.4),(0.5,0.7)]:
      val,_=quad(lambda uu:pair_curvature(a*a,d,uu),-np.inf,np.inf,epsabs=1e-10,epsrel=1e-10,limit=500)
      rhs=math.pi/(4*a**3) if d<a else 0.0
      err=abs(val-rhs)/max(1,abs(rhs)); assert err<2e-8; checks+=1
      projector.append({'a':a,'d':d,'integral':val,'expected':rhs})
    pick=[]
    for z in [complex(0.2,0.35),complex(0.31,0.9)]:
      a=1-z*z; R=2*z*z/(a*a)
      M=np.array([[0,-R],[-R.conjugate(),0]],dtype=complex)
      ev=np.linalg.eigvalsh(M)
      assert np.max(np.abs(ev-np.array([-abs(R),abs(R)])))<1e-12; checks+=4
      pick.append(ev.tolist())
    y=0.23; a=1-y*y; residue=4*y*y/(a*a); eps=1e-4
    f=residue/(complex(a,eps)-a); pick_diag=f.imag/eps
    assert pick_diag<0 and abs(pick_diag+residue/eps**2)<1e-6; checks+=2
    curv=[]
    for delta in [1e-2,1e-3,1e-4]:
      v=pair_curvature(y*y+delta,y,0); assert v<0; curv.append(v); checks+=1
    result={
      'classification':'PASS_RADIAL_CURVATURE_DEPTH_PROJECTOR',
      'checks':checks,
      'max_peano_relative_error':max_peano,
      'max_derivative_jet_error':max_der,
      'max_fourier_relative_error':max_ft,
      'depth_projector_samples':projector,
      'pick_block_eigenvalues':pick,
      'matched_pole_pick_diagonal':pick_diag,
      'matched_target_curvature_right_limits':curv,
      'scope':'finite algebra and numerical controls only; no Riemann-data sign or RH claim'
    }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.json: args.json.write_text(text)
    else: print(text,end='')
    print('PASS_RADIAL_CURVATURE_DEPTH_PROJECTOR')
if __name__=='__main__': main()
