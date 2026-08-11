#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import mpmath as mp
mp.mp.dps=60

def line_curvature(t,u):
    return u*u/(t+u*u)**3

def pair_curvature(t,d,u):
    z=mp.mpc(d,u)
    return -2*mp.re(z*z/(t-z*z)**3)

def line_A(w,u):
    a=1+u*u
    return 2*u*u/(a*a*(a-w))

def pair_A(w,z):
    a=1-z*z
    return -2*(z*z/(a*a*(a-w)) + mp.conj(z)**2/(mp.conj(a)**2*(mp.conj(a)-w)))

def peano(w,fun):
    return 4*mp.quad(lambda q:(w-q)*fun(1-q),[0,w])/(w*w)

def normalized_line(k,u):
    return 2*u*u/(1+u*u)**(k+3)

def normalized_pair(k,z):
    return -4*mp.re(z*z/(1-z*z)**(k+3))

def cder_line(k,u):
    return (-1)**k*mp.factorial(k+2)*u*u/(2*(1+u*u)**(k+3))

def cder_pair(k,z):
    return (-1)**k*(-mp.factorial(k+2))*mp.re(z*z/(1-z*z)**(k+3))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--json',type=Path); args=ap.parse_args()
    checks=0; max_peano=mp.mpf(0); max_der=mp.mpf(0)
    for u in [mp.mpf('0.2'),mp.mpf('0.9'),mp.mpf('3.1')]:
      for w in [mp.mpf('0.1'),mp.mpf('0.55'),mp.mpf('0.9')]:
        lhs=peano(w,lambda tt:line_curvature(tt,u)); rhs=line_A(w,u)
        err=abs(lhs-rhs)/max(1,abs(rhs)); max_peano=max(max_peano,err); assert err<mp.mpf('1e-50'); checks+=1
    for z in [mp.mpc('0.18','0.37'),mp.mpc('0.31','1.2')]:
      for w in [mp.mpf('0.1'),mp.mpf('0.45')]:
        lhs=peano(w,lambda tt:pair_curvature(tt,mp.re(z),mp.im(z))); rhs=pair_A(w,z)
        err=abs(lhs-rhs)/max(1,abs(rhs)); max_peano=max(max_peano,err); assert err<mp.mpf('1e-48'); checks+=1
    for k in range(10):
      for u in [mp.mpf('0.3'),mp.mpf('1.4')]:
        lhs=4*(-1)**k*cder_line(k,u)/mp.factorial(k+2); rhs=normalized_line(k,u)
        err=abs(lhs-rhs); max_der=max(max_der,err); assert err<mp.mpf('1e-55'); checks+=1
      for z in [mp.mpc('0.2','0.4'),mp.mpc('0.42','1.1')]:
        lhs=4*(-1)**k*cder_pair(k,z)/mp.factorial(k+2); rhs=normalized_pair(k,z)
        err=abs(lhs-rhs); max_der=max(max_der,err); assert err<mp.mpf('1e-55'); checks+=1
    # Exact Fourier polynomial identity from I2-a^2 I3.
    # I2 = pi e^-aL (1+aL)/(2a^3), I3 = pi e^-aL (3+3aL+a^2L^2)/(8a^5).
    for A,L in [(2,3),(5,7),(11,1)]:
      lhs=4*(1+A*L)-(3+3*A*L+A*A*L*L)
      rhs=1+A*L-A*A*L*L
      assert lhs==rhs; checks+=1
    projector=[]
    for a,d in [(mp.mpf('0.3'),mp.mpf('0.1')),(mp.mpf('0.5'),mp.mpf('0.2')),(mp.mpf('0.3'),mp.mpf('0.4')),(mp.mpf('0.5'),mp.mpf('0.7'))]:
      val=mp.quad(lambda uu:pair_curvature(a*a,d,uu),[-mp.inf,mp.inf])
      rhs=mp.pi/(4*a**3) if d<a else mp.mpf(0)
      err=abs(val-rhs)/max(1,abs(rhs)); assert err<mp.mpf('1e-35'); checks+=1
      projector.append({'a':mp.nstr(a,8),'d':mp.nstr(d,8),'integral':mp.nstr(val,20),'expected':mp.nstr(rhs,20)})
    pick=[]
    for z in [mp.mpc('0.2','0.35'),mp.mpc('0.31','0.9')]:
      a=1-z*z; R=2*z*z/(a*a)
      eig=[-abs(R),abs(R)]
      assert eig[0]<0<eig[1]; checks+=4
      pick.append([mp.nstr(eig[0],18),mp.nstr(eig[1],18)])
    y=mp.mpf('0.23'); a=1-y*y; residue=4*y*y/(a*a); eps=mp.mpf('1e-4')
    f=residue/(mp.mpc(a,eps)-a); pick_diag=mp.im(f)/eps
    assert pick_diag<0 and abs(pick_diag+residue/eps**2)<mp.mpf('1e-45'); checks+=2
    curv=[]
    for delta in [mp.mpf('1e-2'),mp.mpf('1e-3'),mp.mpf('1e-4')]:
      v=pair_curvature(y*y+delta,y,0); assert v<0; curv.append(mp.nstr(v,18)); checks+=1
    result={
      'classification':'PASS_RADIAL_CURVATURE_DEPTH_PROJECTOR',
      'checks':checks,
      'max_peano_relative_error':mp.nstr(max_peano,12),
      'max_derivative_jet_error':mp.nstr(max_der,12),
      'fourier_polynomial_identity':True,
      'depth_projector_samples':projector,
      'pick_block_eigenvalues':pick,
      'matched_pole_pick_diagonal':mp.nstr(pick_diag,18),
      'matched_target_curvature_right_limits':curv,
      'scope':'finite algebra and high-precision synthetic checks only; no Riemann-data sign or RH claim'
    }
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.json: args.json.write_text(text)
    else: print(text,end='')
    print('PASS_RADIAL_CURVATURE_DEPTH_PROJECTOR')
if __name__=='__main__': main()
